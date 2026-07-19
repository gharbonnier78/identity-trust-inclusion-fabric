#!/usr/bin/env python3
"""Run the synthetic proof of function and generate paper artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from itif.evaluate import evaluate, save_figures, write_results
from itif.generate import GeneratorConfig, generate_events
from itif.model import assign_actions, fit_hybrid, score_exclusion, score_hybrid


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/experiment.yaml")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    cfg = yaml.safe_load((root / args.config).read_text(encoding="utf-8"))
    gcfg = GeneratorConfig(**{k: cfg[k] for k in GeneratorConfig.__dataclass_fields__})
    events = generate_events(gcfg)
    split_month = events["month"].quantile(1 - cfg["temporal_test_fraction"])
    train = events.loc[events["month"] < split_month].copy()
    test = events.loc[events["month"] >= split_month].copy()
    w = cfg["weights"]
    model = fit_hybrid(train, (w["supervised"], w["anomaly"], w["graph"]), cfg["seed"])
    scored = score_hybrid(model, test)
    exclusion_score = score_exclusion(train, test)
    scored["exclusion_score"] = exclusion_score
    scored["action"] = assign_actions(scored["risk"].to_numpy(), cfg["thresholds"])
    metrics = evaluate(test, scored, exclusion_score, cfg["review_capacity"])

    (root / "results").mkdir(exist_ok=True)
    events.to_csv(root / "results" / "synthetic_events.csv", index=False)
    test.join(scored).to_csv(root / "results" / "scored_test_events.csv", index=False)
    save_figures(test, scored, exclusion_score, root / "figures")
    write_results(metrics, root / "results" / "demo_metrics.json", root / "paper" / "generated" / "results.tex")
    print(yaml.safe_dump(metrics, sort_keys=True))


if __name__ == "__main__":
    main()

