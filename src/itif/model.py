"""Hybrid score, anomaly, graph, and inclusion models."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler


FEATURES = [
    "fp_score", "face_score", "fp_quality", "face_quality", "liveness",
    "document_score", "issuer_trust", "credential_active", "device_risk",
    "velocity_24h",
]


@dataclass
class HybridModel:
    supervised: RandomForestClassifier
    anomaly: IsolationForest
    anomaly_scaler: MinMaxScaler
    device_counts: pd.Series
    weights: tuple[float, float, float]


def fit_hybrid(train: pd.DataFrame, weights: tuple[float, float, float], seed: int) -> HybridModel:
    x = train[FEATURES].fillna(0.0)
    clf = RandomForestClassifier(
        n_estimators=180,
        max_depth=8,
        min_samples_leaf=12,
        class_weight="balanced",
        random_state=seed,
        n_jobs=-1,
    )
    # Simulate incomplete labels: novel fraud is excluded from supervised learning.
    supervised_mask = train["novel_fraud"].eq(0)
    clf.fit(x.loc[supervised_mask], train.loc[supervised_mask, "fraud"])

    normal = x.loc[train["fraud"].eq(0)]
    iso = IsolationForest(n_estimators=220, contamination=0.06, random_state=seed, n_jobs=-1)
    iso.fit(normal)
    raw = -iso.score_samples(x)
    scaler = MinMaxScaler().fit(raw.reshape(-1, 1))
    counts = train.groupby("device_id")["identity_id"].nunique()
    return HybridModel(clf, iso, scaler, counts, weights)


def score_hybrid(model: HybridModel, df: pd.DataFrame) -> pd.DataFrame:
    x = df[FEATURES].fillna(0.0)
    p_supervised = model.supervised.predict_proba(x)[:, 1]
    raw_anomaly = -model.anomaly.score_samples(x)
    p_anomaly = np.clip(model.anomaly_scaler.transform(raw_anomaly.reshape(-1, 1)).ravel(), 0, 1)
    reuse = df["device_id"].map(model.device_counts).fillna(1).to_numpy()
    p_graph = np.clip((reuse - 1) / 8.0 + df["device_risk"].to_numpy() * 0.30, 0, 1)
    ws, wa, wg = model.weights
    risk = np.clip(ws * p_supervised + wa * p_anomaly + wg * p_graph, 0, 1)
    return pd.DataFrame({
        "p_supervised": p_supervised,
        "p_anomaly": p_anomaly,
        "p_graph": p_graph,
        "risk": risk,
    }, index=df.index)


def score_exclusion(train: pd.DataFrame, df: pd.DataFrame) -> np.ndarray:
    """Detect unusually burdensome legitimate journeys within each channel."""
    baselines = train.loc[train["fraud"].eq(0)].groupby("channel").agg(
        duration_median=("duration_seconds", "median"),
        attempts_median=("process_attempts", "median"),
        duration_mad=("duration_seconds", lambda s: np.median(np.abs(s - np.median(s))) + 1.0),
    )
    b = baselines.reindex(df["channel"]).reset_index(drop=True)
    duration_z = (df["duration_seconds"].to_numpy() - b["duration_median"].to_numpy()) / (3 * b["duration_mad"].to_numpy())
    attempts = (df["process_attempts"].to_numpy() - b["attempts_median"].to_numpy()) / 4.0
    return np.clip(0.65 * duration_z + 0.35 * attempts, 0, 1)


def assign_actions(risk: np.ndarray, thresholds: dict[str, float]) -> np.ndarray:
    return np.select(
        [risk >= thresholds["block"], risk >= thresholds["human_review"],
         risk >= thresholds["step_up"], risk >= thresholds["monitor"]],
        ["block_or_escalate", "human_review", "step_up", "monitor"],
        default="approve",
    )

