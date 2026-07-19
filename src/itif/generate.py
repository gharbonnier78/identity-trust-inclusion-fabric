"""Generate synthetic identity, credential, biometric, and process events.

The generator deliberately works with scores and metadata rather than raw
biometric samples. It is a research fixture, not a population model.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class GeneratorConfig:
    seed: int = 42
    n_events: int = 12_000
    n_identities: int = 6_500
    n_devices: int = 1_800
    n_issuers: int = 45
    fraud_rate: float = 0.055
    novel_fraud_fraction: float = 0.28
    exclusion_rate: float = 0.075


def _bounded(rng: np.random.Generator, mean: np.ndarray, std: float) -> np.ndarray:
    return np.clip(rng.normal(mean, std), 0.0, 1.0)


def generate_events(cfg: GeneratorConfig) -> pd.DataFrame:
    """Return a temporally ordered synthetic event table."""
    rng = np.random.default_rng(cfg.seed)
    n = cfg.n_events
    month = rng.integers(0, 24, n)
    order = np.argsort(month + rng.random(n))
    month = month[order]

    identity_id = rng.integers(0, cfg.n_identities, n)[order]
    device_id = rng.integers(0, cfg.n_devices, n)[order]
    issuer_id = rng.integers(0, cfg.n_issuers, n)[order]
    channel = rng.choice(["office", "mobile", "partner", "kiosk"], n, p=[0.35, 0.36, 0.19, 0.10])[order]
    credential_type = rng.choice(["national_id", "passport", "degree", "professional", "telco_kyc"], n,
                                 p=[0.30, 0.18, 0.16, 0.12, 0.24])[order]

    legitimate_quality = rng.beta(6.5, 2.1, n)[order]
    fp_quality = _bounded(rng, legitimate_quality, 0.09)
    face_quality = _bounded(rng, legitimate_quality + 0.03, 0.08)
    fp_score = _bounded(rng, 0.48 + 0.47 * fp_quality, 0.055)
    face_score = _bounded(rng, 0.46 + 0.48 * face_quality, 0.06)
    iris_present = rng.random(n)[order] < 0.08
    iris_score = np.where(iris_present, _bounded(rng, 0.90 * np.ones(n), 0.07), np.nan)
    liveness = _bounded(rng, 0.94 * np.ones(n), 0.045)
    document_score = _bounded(rng, 0.91 * np.ones(n), 0.07)
    issuer_trust = _bounded(rng, 0.93 * np.ones(n), 0.05)
    credential_active = (rng.random(n) > 0.018).astype(int)[order]
    device_risk = rng.beta(1.4, 9.0, n)[order]
    velocity_24h = rng.poisson(1.2, n)[order]
    process_attempts = 1 + rng.poisson(0.35, n)[order]
    duration_seconds = rng.lognormal(np.log(95), 0.48, n)[order]

    fraud = rng.random(n)[order] < cfg.fraud_rate
    novel = fraud & (rng.random(n) < cfg.novel_fraud_fraction)
    known = fraud & ~novel

    # Known attacks: recognizable score, liveness, document, and device patterns.
    fp_score[known] = _bounded(rng, 0.40 + 0.12 * fp_quality[known], 0.13)
    face_score[known] = _bounded(rng, 0.43 + 0.10 * face_quality[known], 0.14)
    liveness[known] = _bounded(rng, 0.41 * np.ones(known.sum()), 0.20)
    document_score[known] = _bounded(rng, 0.48 * np.ones(known.sum()), 0.20)
    device_risk[known] = rng.beta(6.0, 2.0, known.sum())
    velocity_24h[known] += rng.poisson(6.0, known.sum())

    # Novel attacks: individually plausible signals but unusual joint coherence.
    fp_score[novel] = _bounded(rng, 0.86 * np.ones(novel.sum()), 0.06)
    face_score[novel] = _bounded(rng, 0.38 * np.ones(novel.sum()), 0.10)
    liveness[novel] = _bounded(rng, 0.88 * np.ones(novel.sum()), 0.07)
    document_score[novel] = _bounded(rng, 0.83 * np.ones(novel.sum()), 0.09)
    device_risk[novel] = rng.beta(4.0, 3.0, novel.sum())
    velocity_24h[novel] += rng.poisson(3.0, novel.sum())

    # Fraud rings reuse a small device pool; the detector never sees ring ids.
    fraud_indices = np.flatnonzero(fraud)
    ring_devices = rng.choice(np.arange(max(30, cfg.n_devices // 15)), size=fraud_indices.size, replace=True)
    device_id[fraud_indices] = ring_devices

    # Exclusion cases are legitimate but suffer repeated or slow processes.
    exclusion = (~fraud) & (rng.random(n) < cfg.exclusion_rate)
    affected_site = (channel == "kiosk") | ((channel == "partner") & (month >= 16))
    exclusion = exclusion | ((~fraud) & affected_site & (rng.random(n) < 0.16))
    process_attempts[exclusion] += rng.integers(2, 6, exclusion.sum())
    duration_seconds[exclusion] *= rng.uniform(3.0, 7.0, exclusion.sum())
    fp_quality[exclusion] = _bounded(rng, fp_quality[exclusion] - 0.24, 0.10)

    df = pd.DataFrame({
        "event_id": np.arange(n),
        "month": month,
        "identity_id": identity_id,
        "device_id": device_id,
        "issuer_id": issuer_id,
        "channel": channel,
        "credential_type": credential_type,
        "fp_score": fp_score,
        "face_score": face_score,
        "iris_score": iris_score,
        "fp_quality": fp_quality,
        "face_quality": face_quality,
        "liveness": liveness,
        "document_score": document_score,
        "issuer_trust": issuer_trust,
        "credential_active": credential_active,
        "device_risk": device_risk,
        "velocity_24h": velocity_24h,
        "process_attempts": process_attempts,
        "duration_seconds": duration_seconds,
        "fraud": fraud.astype(int),
        "novel_fraud": novel.astype(int),
        "exclusion": exclusion.astype(int),
    })
    return df

