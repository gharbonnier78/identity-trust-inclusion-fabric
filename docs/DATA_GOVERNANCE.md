# Data Governance and Privacy Architecture

## Default posture

Keep authoritative records and raw biometrics at their source. Exchange the minimum proof needed for the declared purpose. Prefer signatures, status responses, derived claims, pseudonymous identifiers, and local computation over bulk replication.

## Prohibited telemetry

- raw fingerprint, face, or iris samples;
- reusable biometric templates;
- full names, national identifiers, and document numbers in traces;
- secret keys or wallet material;
- unbounded free-text investigator notes in shared analytics stores.

## Required provenance

Every decision bundle identifies evidence schema, source, timestamp, purpose, policy, rule, model, feature set, threshold, action, reviewer state, and correction state. SBOM, ML-BOM, Data-BOM, and policy manifests are linked but access-controlled.

## Federation

Cross-domain queries are authorized, purpose-limited, logged, and capable of returning a derived yes/no or confidence statement without disclosing the underlying record. Linkage keys are scoped by purpose and domain to prevent creation of a universal citizen graph.

## Redress and repair

An overturned suspicion must trigger deterministic repair: update the decision state, remove unsupported adverse labels, reprocess affected decisions where lawful, notify relying parties where required, and verify propagation.

