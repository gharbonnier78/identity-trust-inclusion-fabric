# Identity Trust & Inclusion Fabric — Thread and Artifact Inventory

**Prepared for:** Guillaume Harbonnier  
**Date:** 19 July 2026  
**Purpose:** recovery checklist for consolidating earlier discussions, LaTeX sources, PDFs, notebooks, archives, and design decisions into the Identity Trust & Inclusion Fabric research lineage.

> This inventory deliberately separates confirmed conversation URLs from title/date anchors. Some internal ChatGPT URLs are not exposed by history search; those threads should be located by their exact title and date.

## 1. Priority A — direct research lineage

### A1. Anomaly detection and the new ecosystem product

- [ ] **Thread:** `M3-W1-10 — Anomaly Detection / Finding unusual events`
- **Date:** 19 July 2026
- **Confirmed URL:** https://chatgpt.com/c/6a5d2a35-2e78-83ed-988f-c2895d11ec46
- **Recover:** complete discussion; aircraft-engine density-estimation notes; fraud/manufacturing/data-centre analogies; transition to biometric and credential anomaly detection; product opportunity; anti-exclusion perspective; final thesis package.

### A2. Beyond the Matcher / CETRA-R

- [ ] **Thread anchor:** `Problèmes ML et DL`
- **Date:** 12 July 2026
- **URL status:** exact conversation URL not recovered; search the history using the exact title and date.
- **Recover:**
  - `THESIS_PROPOSAL.md`
  - `Beyond_the_Matcher_CETRA.pdf`
  - `Beyond_the_Matcher_CETRA_R.pdf`
  - `Beyond_the_Matcher_CETRA_R-v0.5.0.zip`
  - `beyond-the-matcher-cetra-r-v0.4.0.zip`
  - `cetra-r-ml-system-companion-v1.0.0.zip`
  - `cetra-r-ml-system-companion-v1.3.0.zip`
  - `Building_the_CETRA_R_ML_System.pdf`
  - `CETRA_R_Deployment_xBOMs_v0.2.0.xlsx`
  - `MMALS_CETRA_RELEASE_SHA256SUMS`
- **Contribution:** multibiometric post-matcher decisions; risk/friction/latency/support/expert-capacity trade-off; selective automation; learning to defer; contestation, remedy, and identity-record repair.

### A3. Jupyter, Jarvis, MBSS, Matcher Mock, and fraud scenarios

- [ ] **Thread:** `Jupyter Jarvis Integration`
- **Date:** 12 March 2026
- **Confirmed URL:** https://chatgpt.com/c/69b2c333-6cfc-8327-b8e6-115515a5e54e
- **Recover:** notebook/environment artifacts; MBSS-compatible interface notes; AMQP versus SOAP decisions; 10-print, face, biographic data, national-ID scenarios; Matcher Mock; GCCNS Gateway/Decision Engine; probability models for genuine/impostor/quality; truth and trace comparison.

### A4. Synthetic biometric fraud evaluation platform

- [ ] **Thread:** `Biometric Fraud Detection Platform`
- **Date:** 16 March 2026
- **Confirmed URL:** https://chatgpt.com/c/69b804d1-eed4-832b-b2a4-ccb85f3a7510
- **Recover:** generator and truth-matrix specifications; SFinGe/Anguli/PrintsGAN discussion; face and optional iris generation; ImageAdjuster; Jarvis integration; HIT/NO HIT/possible hit; FAR/FRR/EER/ROC/DET; Stitch prompts and UI architecture.

### A5. National Identity Fraud Risk Engine and GNN

- [ ] **Thread anchor:** `Notebook Publication and Arxiv`
- **Date:** 12 July 2026
- **URL status:** exact conversation URL not recovered; search by title/date and the phrase `National Identity Fraud Risk Engine / GNN`.
- **Recover:**
  - `NationalIdentityFraudRiskEngine_GrahNeurolNetworkPyTorch.pdf`
  - original 419-cell development chronicle
  - reviewer edition
  - `notebooks/02_reproducible_graph_benchmark.ipynb`
  - paper `From Manual Neural Networks to Identity Graphs: A Reproducible Development Chronicle and Synthetic Benchmark for National Identity Fraud Risk`
- **Existing repository:** https://github.com/gharbonnier78/national-identity-fraud-risk-engine-gnn
- **Contribution:** manual neural-network lineage; identity/device/IP graph; coordinated fraud rings; leakage-resistant ring and temporal holdouts; GNN benchmark.

### A6. Production-grade biometric calibration

- [ ] **Thread:** `how to design a calibrated biometric decision system (production-grade)`
- **Date:** 5 April 2026
- **URL status:** exact conversation URL not recovered; search exact title/date.
- **Recover:** similarity-to-probability calibration; logistic/isotonic/Platt calibration; accept/reject/manual-review thresholds; FAR/FRR/EER/DET; likelihood ratios; drift and context-aware calibration; FAISS/embedding observations.

### A7. Biometric threshold change 3200 → 3500

- [ ] **Thread/artifact anchor:** `Biometric Threshold Evaluation Playbook (1:1 Verification)`
- **Date:** 13 January 2026
- **URL status:** exact conversation URL not recovered; search title/date and `3200 3500`.
- **Recover:**
  - `Biometric_Threshold_Evaluation_Playbook_ColabReady.ipynb`
  - `biometric_threshold_ops_arxiv.pdf`
  - `biometric_threshold_ops_github_package.zip`
- **Contribution:** borderline/degraded datasets; FAR/FNMR/TMR; assisted-flow routing; green/orange/red zones; SLA and cost model; threshold governance.

## 2. Priority B — ecosystem, credentials, and inclusion

### B1. Evolution of the ML and biometric research programme

- [ ] **Thread:** `ML Evolution and Influence`
- **Date:** 14 May 2026
- **Confirmed URL:** https://chatgpt.com/c/6a062ecf-497c-83e9-9bad-57a2b13fd17e
- **Recover:** cross-review of playbooks; course-to-research lineage; STRAT-Q; probabilistic MTP/PyMC; threshold calibration; manual NN; GNN; TOPAS/virtual identity; SFinGe; minutiae/orientation; ImageAdjuster; REW/Dynamic Trust Graph; MMALS and geometric ML.

### B2. Foundational ML training and industrial motivation

- [ ] **Thread:** `Formation ML et IA`
- **Date:** 9 July 2025
- **Confirmed URL:** https://chatgpt.com/c/686e5a63-a778-8007-aa4e-ef94eea735d7
- **Recover:** original ML/AI learning motivation and intended applications to engineering, biometric products, innovation, and customer solutions.

### B3. Brazil national identity ecosystem

- [ ] **Thread:** `CIN Identidade Nacional Brasil`
- **Date:** 13–14 April 2026
- **Confirmed URL:** https://chatgpt.com/c/69dd6ba3-989c-83e9-b05a-41aef6386802
- **Recover:** CPF, CIN, passport, CNH, Gov.br, biometrics, deduplication and fraud-prevention architecture.

### B4. Verifiable trust, credentials, and trust registries

- [ ] **Thread anchors:** `Verifiable Trust v4`, `IIW`, `Trust Architecture & Identity Validation Strategy`
- **Dates:** 19–20 April and 20 May 2026
- **URL status:** exact URLs not recovered; search titles and phrases.
- **Recover:** W3C VC/DID; wallets; OpenID; trust registry; issuer/verifier governance; DID resolution; secure-channel establishment; runtime trust enforcement; refugees/EUDI and national-scale identity discussions.

### B5. LAC identity opportunity and system-of-systems views

- [ ] **Artifact:** `lac-digital-identity-opportunity-framework-v0.6.0.pdf`
- **Repository:** https://github.com/gharbonnier78/lac-digital-identity-opportunity-framework
- **Recover:** five-layer identity architecture; civil registry; credentials; authentication; consent, complaints, correction, redress; ecosystem activation.

### B6. Airport, travel, border, and digital identity architecture

- [ ] **Repository:** https://github.com/gharbonnier78/airport-travel-border-identity-architecture
- **Date anchor:** 14–21 May 2026
- **Recover:** high-level ecosystem view; technical-stack view; border, travel, credentials, biometrics, and trust architecture.

## 3. Priority C — adjacent evidence worth reviewing

- [ ] `DATA_CARD.md` — Decision-Side Multibiometric Evidence; face, multiple fingerprints, optional iris, versions, contexts, review outcomes, action labels.
- [ ] `ESC_v0.2_beta_m2_passport_case_study.pdf` — process spans, adjudication, fraud registration, evidence and replay.
- [ ] `geometry_inspired_multibiometric_reconstruction_lab_v0_1.ipynb` — finite-dimensional geometry-inspired biometric reconstruction analogue.
- [ ] STRAT-Q ML Pilot Factory packages — evidence-centric lifecycle, selective automation, policy, xBOMs and deployment gates.
- [ ] TOPAS / virtual identity system discussions — ecosystem entities, credentials, trust and identity lifecycle.
- [ ] REW risk calculator / Dynamic Trust Graph discussions — temporal and relational risk evidence.
- [ ] Fingerprint minutiae/orientation and ImageAdjuster threads — quality, robustness, sensor/population drift and synthetic pair generation.
- [ ] Ethics/fairness threads from 12 July 2026 — harm analysis, demographic performance, audit and explicit REDESIGN/NO-GO gates.

## 4. Canonical destination already created

- **Main repository:** https://github.com/gharbonnier78/identity-trust-inclusion-fabric
- **Current thesis PDF:** https://github.com/gharbonnier78/identity-trust-inclusion-fabric/blob/main/output/pdf/Identity_Trust_Inclusion_Fabric_Thesis_v0.1.0.pdf
- **GNN repository:** https://github.com/gharbonnier78/national-identity-fraud-risk-engine-gnn
- **Diderot ML repository:** https://github.com/gharbonnier78/diderot-machine-learning-specialization

## 5. Collection procedure for tomorrow

For each recovered thread:

1. Download every original `.tex`, `.bib`, `.pdf`, `.md`, `.ipynb`, `.yaml`, `.json`, `.xlsx`, figure, ZIP, and checksum file.
2. Record the exact thread title, URL, date, artifact version, and one-sentence contribution.
3. Preserve original files unchanged under `archive/artifacts/<lineage>/<version>/`.
4. Add a short manifest under `archive/threads/YYYY-MM-DD_<slug>/MANIFEST.md`.
5. Record whether each item should be **merged**, **cited**, **superseded**, or kept as **historical evidence**.
6. Do not publish customer-confidential data, operational identities, raw biometric samples/templates, secrets, internal endpoints, or personal documents.
7. Open one integration issue per coherent contribution; avoid copying an entire older package into the product architecture without a traceable decision.

## 6. Minimal manifest template

```markdown
# Source-thread manifest

- Thread title:
- Thread URL:
- Date:
- Research lineage:
- Artifacts recovered:
- Version/checksum:
- Key contribution:
- Decision: merge | cite | supersede | historical
- Target chapter/module:
- Confidentiality review:
- Notes:
```

## 7. Known search limitation

History search exposed several exact conversation URLs, but not all of them. For missing links, the exact titles, dates, artifact names, and distinctive search phrases above are the most reliable recovery keys. Once a missing thread is opened, copy its URL into this inventory so that GitHub becomes the durable index.
