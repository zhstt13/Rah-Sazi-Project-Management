# Rah-Sazi Project Management

> An evidence-first Project Operating System for road and infrastructure delivery.

**Rah-Sazi Project Management** turns a GitHub repository into a controlled project-management workspace for road construction: scope, WBS, BOQ, schedule, cost, earned value, risk, change, contracts, procurement, quality, HSE, environment, stakeholders, land/utilities, GIS/BIM references, reporting, handover, and lessons learned.

It is designed to be:

- **Operational** — usable by project managers, planners, cost engineers, site teams, commercial teams, QA/QC, HSE, and document control.
- **Traceable** — every important status is linked to an owner, a date, a baseline, and evidence.
- **Auditable** — changes are reviewable through issues, pull requests, commits, releases, and immutable baseline snapshots.
- **Localizable** — BOQ/pay-item, schedule-of-rates, chainage, local currency, contract, and public-works fields can be adapted without breaking the core model.
- **AI-ready** — ChatGPT/agents can work from structured records and evidence instead of guessing from unstructured chat.

> This repository is a management system blueprint and starter implementation. It is not legal, contractual, safety, engineering, or regulatory advice, and it does not by itself certify compliance with any standard or contract.

## What is included

| Capability | Repository surface |
|---|---|
| Project charter and lifecycle gates | `docs/01-operating-model/` |
| WBS, BOQ, CBS and cost coding | `docs/02-controls/WBS_CBS_AND_COST_CODES.md`, `schemas/` |
| Schedule and look-ahead control | `docs/02-controls/SCHEDULE_CONTROL.md` |
| Cost control and EVM | `docs/02-controls/COST_AND_EVM.md`, `tools/evm.py` |
| Risk, issue, opportunity and decision control | `docs/02-controls/RISK_ISSUE_OPPORTUNITY.md`, issue forms |
| Change, claims, contracts and payments | `docs/02-controls/CHANGE_CONTROL.md`, `docs/02-controls/CONTRACTS_CLAIMS_AND_PAYMENTS.md` |
| Quality, inspections and NCR/CAR | `docs/02-controls/QUALITY_CONTROL.md` |
| HSE, traffic management and environment | `docs/02-controls/HSE_AND_ENVIRONMENT.md` |
| Procurement, materials and suppliers | `docs/02-controls/PROCUREMENT_AND_SUPPLY_CHAIN.md` |
| Land, utilities, stakeholders and interfaces | `docs/02-controls/STAKEHOLDER_AND_LAND_UTILITIES.md` |
| Survey, GIS/BIM and location-based control | `docs/02-controls/SURVEY_GIS_BIM.md` |
| Document control and transmittals | `docs/02-controls/DOCUMENT_CONTROL.md` |
| Commissioning, handover and asset data | `docs/02-controls/COMMISSIONING_AND_HANDOVER.md` |
| Structured records and validation | `schemas/`, `data/`, `tools/validate_repository.py` |
| Executive/project-controls dashboard starter | `apps/dashboard/index.html` |
| GitHub governance and automation | `.github/`, `GOVERNANCE.md`, `CONTRIBUTING.md` |

## Repository map

```text
.
├── apps/dashboard/                 # Static control-room dashboard starter
├── config/                         # Project profile, thresholds and taxonomies
├── data/
│   ├── examples/demo-road-project/ # Safe, fictional example project
│   └── reference/                  # Controlled dictionaries and statuses
├── docs/
│   ├── 00-foundations/             # Principles and reference frameworks
│   ├── 01-operating-model/        # Lifecycle, gates, roles and governance
│   ├── 02-controls/                # Delivery-control playbooks
│   └── 03-reporting/               # Cadence, KPIs and decision reporting
├── schemas/                        # JSON Schema contracts for core records
├── templates/                      # Copyable issue/report/register templates
├── tools/                          # Dependency-light validation and calculations
└── .github/                        # Issue forms, PR rules and CI
```

## Fast start

1. Read [ARCHITECTURE.md](ARCHITECTURE.md) and [REPOSITORY_MAP.md](REPOSITORY_MAP.md).
2. Copy `data/examples/demo-road-project/` to a project-specific workspace, then replace fictional values.
3. Define the project profile and control thresholds under `config/`.
4. Establish the WBS/CBS/BOQ dictionary before recording progress.
5. Freeze the first approved schedule and cost baseline; identify it explicitly.
6. Record risks, issues, changes, decisions, inspections, daily reports and evidence using the provided schemas/templates.
7. Run the local validator:

   ```bash
   python tools/validate_repository.py
   python tools/evm.py --pv 1200000 --ev 1140000 --ac 1180000
   ```

8. Open `apps/dashboard/index.html` locally for the fictional control-room example.

## Operating rule

GitHub is the collaboration and audit layer, not a replacement for a licensed scheduling, ERP, CDE, GIS, BIM, safety, or accounting platform. External systems may remain systems of record for specialized data; this repository stores the approved snapshot, identifier, source link, checksum, decision, and evidence needed to control and audit the project.

## Design principles

1. **Evidence before status.**
2. **One canonical owner per concern.**
3. **Baselines are immutable; revisions are explicit.**
4. **No silent overwrite of approved plans or records.**
5. **Unknown is a valid value; invented data is not.**
6. **Separate fact, estimate, assumption, decision and recommendation.**
7. **Every change carries scope, time, cost, risk, quality, HSE and contract impact.**
8. **Human approval remains mandatory for safety, contractual, financial and baseline decisions.**
9. **Automate checks, not accountability.**
10. **Keep the repository useful at small-project scale while allowing enterprise integrations later.**

## Reference basis

The operating model is informed by the public descriptions of project-management practice in ISO 21502, PMI standards, FIDIC contract-management materials, and ISO quality, occupational-health-and-safety, and environmental-management standards. The repository deliberately uses them as design references, not as a claim of certification or legal compliance. See [REFERENCE_FRAMEWORKS.md](docs/00-foundations/REFERENCE_FRAMEWORKS.md).

## Status

**Foundation release: v0.1.0 — architecture and control-plane starter.**

The next intended increments are:

- a richer dashboard backed by validated project data;
- CSV/Excel import-export adapters;
- schedule import adapters (for example, P6/MS Project exports);
- cost-ledger and payment-certificate adapters;
- GIS/chainage map views;
- approval workflow integrations;
- role-based access and external CDE/ERP connectors;
- Persian localization and configurable public-works rate libraries.

## License

No license has been selected yet. Do not reuse, redistribute, or deploy this repository as a product until the owner adds the intended license and project-specific legal notices.
