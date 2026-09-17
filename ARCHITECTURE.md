# Architecture

## Purpose

Rah-Sazi Project Management is a repository-native project operating system for road and infrastructure delivery. It is intentionally a control plane: it defines the trusted structure, approvals, evidence links, calculation rules, and reporting surfaces that connect project teams and specialist systems.

The repository is not intended to replace Primavera/P6 or Microsoft Project, an ERP, a common data environment, a GIS/BIM platform, a safety platform, or an accounting system. It creates a traceable management layer around them.

## System boundary

### Inside the repository

- approved project profile and contract metadata;
- WBS, BOQ/pay-item, CBS and cost-code definitions;
- schedule and cost baseline references;
- progress measurements and earned-value snapshots;
- risks, issues, opportunities, decisions and actions;
- change requests, claims, approvals and impact assessments;
- procurement packages, supplier records and material approvals;
- RFIs, submittals, inspections, tests, NCRs and corrective actions;
- daily reports, HSE observations, incidents and environmental controls;
- stakeholder, land, right-of-way and utility interfaces;
- document register, revisions, transmittals and evidence checksums;
- handover, asset and lessons-learned records;
- validation scripts, templates, dashboards and GitHub workflow.

### Outside the repository

Specialist systems may remain authoritative for detailed scheduling, accounting, document storage, field capture, surveying, GIS, BIM, laboratory results and legal/contract administration. A record imported from an external system must retain:

1. source system and record identifier;
2. extraction or snapshot date;
3. revision/baseline identifier;
4. source URL or location;
5. checksum where practical;
6. owner responsible for confirming the snapshot;
7. limitations and unresolved differences.

## Domain model

| Domain | Canonical repository owner | Primary records |
|---|---|---|
| Project definition | project profile and charter | project, contract, objectives, assumptions |
| Scope and location | WBS/CBS/BOQ records | WBS item, pay item, chainage/location |
| Time | schedule-control records | activity, baseline, look-ahead, constraint |
| Cost | cost-control records | budget, commitment, actual, forecast, payment |
| Performance | progress records | quantity, physical progress, PV, EV, AC |
| Uncertainty | risk-control records | risk, opportunity, issue, trigger, response |
| Decisions | decision log | decision, options, authority, rationale |
| Change | change-control records | change request, impact, approval, implementation |
| Commercial | contract/claim/payment records | notice, variation, claim, certificate |
| Quality | quality records | ITP, submittal, inspection, test, NCR, CAR |
| HSE/environment | HSE records | hazard, observation, incident, permit, aspect |
| Supply chain | procurement records | package, requisition, bid, PO, delivery, supplier |
| Interfaces | stakeholder/land/utilities records | stakeholder, parcel, utility, interface |
| Information | document-control records | document, revision, transmittal, RFI |
| Completion | handover records | punch item, test pack, asset, acceptance |

## Record contract

Every controlled record should have, directly or through its schema:

- a stable identifier;
- project and contract context;
- lifecycle status;
- accountable owner;
- created/updated timestamps;
- source and evidence links;
- related WBS, location, cost code or contract item where relevant;
- explicit baseline/revision context;
- confidence or data-quality note when information is incomplete;
- change history or a link to the issue/PR that changed it.

The words fact, estimate, assumption, decision, recommendation and unknown must not be treated as interchangeable.

## Control flow

1. Define the project, contract, location and governance.
2. Build and approve the WBS, BOQ/pay-item and cost-code dictionary.
3. Build the integrated schedule and identify the approved baseline.
4. Load the cost baseline and map budget to work packages.
5. Record field progress against measurable quantities and evidence.
6. Calculate performance indicators and forecast; explain variances.
7. Register risks, issues, opportunities, changes and decisions.
8. Route quality, HSE, commercial and stakeholder records to accountable owners.
9. Freeze approved revisions and publish a reporting snapshot.
10. Close, hand over, archive evidence and capture lessons.

## Baseline and revision rules

- A baseline is a named, dated, approved snapshot; it is never silently overwritten.
- A revision must state what changed, why it changed, who approved it and the effective date.
- A progress record must reference the baseline against which it is measured.
- A change request must identify impact on scope, time, cost, quality, HSE, environment, risk and contract.
- A report is a view of records at a stated cut-off date, not a second source of truth.
- A dashboard must display stale, missing or unverified data rather than hiding it.

## Dependency direction

The intended dependency direction is:

Project profile → WBS/BOQ/CBS → schedule and cost baseline → progress and actuals → forecast/KPIs → risks/issues/changes → decisions and reports → handover/lessons.

Reference dictionaries and schemas are upstream contracts. Dashboards and reports are downstream views. No dashboard should become the canonical place where project data is edited.

## Enforcement

| Boundary | Check |
|---|---|
| Required repository surfaces | validate_repository.py |
| JSON syntax and identifier uniqueness | validate_repository.py |
| EVM arithmetic | tools/evm.py and targeted tests |
| Pull-request review and evidence | PR template and CODEOWNERS |
| Change traceability | issue/PR links and decision log |
| Baseline protection | branch protection and release/tag policy configured by repository owner |
| Sensitive data handling | SECURITY.md and review checklist |
| Human approval | gate and control playbooks |

## Growth path

The repository can evolve in bounded slices:

1. foundation: schemas, templates, examples, validation and dashboard starter;
2. adapters: CSV/Excel, schedule, cost-ledger and payment imports;
3. interfaces: GIS/chainage, BIM references, CDE and ERP links;
4. workflow: approvals, role-based access, notifications and audit APIs;
5. analytics: time-series performance, forecast confidence, portfolio views and lessons retrieval.

Each slice must preserve the canonical record contract and add tests before adding automation.
