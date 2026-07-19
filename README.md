# Identity Trust & Inclusion Fabric

[![CI](https://github.com/gharbonnier78/identity-trust-inclusion-fabric/actions/workflows/ci.yml/badge.svg)](https://github.com/gharbonnier78/identity-trust-inclusion-fabric/actions/workflows/ci.yml)

Research, industrialization, and product-opportunity package for a federated identity and credential assurance infrastructure that detects fraud, novelty, relational risk, systemic exclusion, and process failure while preserving privacy, human agency, and redress.

> **Claim boundary.** The demonstrator uses synthetic score-level and process data. It is not an operational fraud detector, a biometric matcher, a citizen-scoring system, or evidence of real-world performance.

## Core proposition

Existing markets provide strong components for biometric matching, presentation-attack detection, document verification, behavioral biometrics, and transaction fraud. The proposed product occupies the orchestration gap between those components:

1. ingest evidence without centralizing raw biometrics;
2. detect known fraud, unknown anomalies, relational patterns, and exclusion patterns;
3. calibrate risk and uncertainty;
4. select a proportionate action: approve, monitor, step-up, human review, or escalation;
5. preserve purpose limitation, contestability, record repair, and evidence traceability.

## Repository map

```text
.
├── paper/                 # LaTeX thesis and bibliography
├── output/pdf/            # compiled thesis
├── src/itif/              # synthetic generator and hybrid models
├── scripts/               # reproducible experiment entry point
├── config/                # controlled experiment manifest
├── results/               # generated metrics and synthetic outputs
├── figures/               # generated evaluation figures
├── docs/                  # product, market, governance, and research notes
└── tests/                 # reproducibility and range checks
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
make experiment
make test
make paper
make verify
```

## Main artifacts

- `output/pdf/Identity_Trust_Inclusion_Fabric_Thesis_v0.1.0.pdf`
- `paper/main.tex`
- `docs/PRODUCT_BRIEF.md`
- `docs/MARKET_LANDSCAPE.md`
- `docs/REQUIREMENTS_CANVAS.md`
- `docs/RESEARCH_TRACEABILITY.md`
- `results/demo_metrics.json`

## Research lineage

This package consolidates four previously separate lines of work:

- **Beyond the Matcher**: calibrated, explainable, human-AI post-matcher decision and remedy;
- **Biometric Fraud Simulation Framework**: Matcher Mock, real Matcher, truth matrix, and Jarvis validation;
- **National Identity Fraud Risk Engine GNN**: relational identity-device-IP risk;
- **Identity Trust & Inclusion Fabric**: federated credentials, fraud, process anomaly, exclusion monitoring, and rights-preserving orchestration.

## Responsible-use boundary

The platform must never produce a universal citizen score or infer guilt from anomaly. Every deployment requires a declared purpose, lawful basis, privacy-risk assessment, data minimization, accessible alternative path, human review where adverse effects are possible, appeal, correction, and measurable propagation of remedies.

## Status

Version 0.1.0 is a research and product-discovery package. It is not peer reviewed and must be validated with lawful, representative, customer-specific evidence before any operational use.

