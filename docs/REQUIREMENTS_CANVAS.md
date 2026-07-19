# Fraud, Trust, and Inclusion Requirements Canvas

## Purpose gate

- What protected decision or service is being assured?
- Who benefits, who bears risk, and who may be excluded?
- Is identity or credential verification necessary and proportionate?
- What outcome would justify redesign or no-go?

## Threat and failure ontology

- impersonation, substitution, duplicate enrollment;
- presentation and injection attack;
- document or credential forgery;
- issuer compromise, invalid accreditation, revocation failure;
- account takeover, synthetic identity, collusive network;
- operator error, migration conflict, stale record;
- process exclusion, inaccessible channel, repeated failure, excessive delay.

## Evidence contract

- signal owner and lawful basis;
- schema, unit, range, quality, timestamp, and provenance;
- model, matcher, sensor, policy, and credential version;
- missingness semantics;
- retention, access, and redaction rules;
- prohibited raw data in logs.

## Decision contract

- permitted actions and prohibited automation;
- thresholds and uncertainty bands;
- review capacity and service time;
- required reason codes;
- alternative path and human override;
- appeal, correction, reprocessing, and propagation verification.

## Evaluation contract

- fraud recall and precision;
- novel-fraud recall;
- false-alert and false-adverse-action rates;
- calibration and residual risk;
- recall at 5/10/20% review capacity;
- average number of additional proofs requested;
- legitimate-user completion, delay, abandonment, and repeat attempts;
- segment, channel, site, device, and temporal stability;
- remedy completion and downstream repair latency.

## Deployment contract

- shadow, controlled support, then governed production;
- canary, rollback, and kill switch;
- drift and policy-version monitoring;
- human accountability and operator protection;
- independent audit and citizen-facing explanation.

