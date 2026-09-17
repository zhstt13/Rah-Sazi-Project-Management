# Repository Map

This map names the intended navigation and canonical ownership. It is deliberately shorter than the playbooks; details belong to the owning file.

## Start here

| Question | Read |
|---|---|
| What is this project? | README.md |
| What is the system boundary? | ARCHITECTURE.md |
| Where does a concern belong? | this file |
| How do I change the repository? | CONTRIBUTING.md |
| How are decisions and approvals governed? | GOVERNANCE.md |
| What has been decided? | DECISIONS.md |
| How do I validate changes? | tools/validate_repository.py and .github/workflows/validate.yml |
| How do I see the sample control room? | apps/dashboard/index.html |

## Canonical ownership

| Concern | Single owner | Do not duplicate as a competing source |
|---|---|---|
| Project identity and contract context | config/project-profile.example.json plus project record | README prose |
| WBS, BOQ and cost coding | docs/02-controls/WBS_CBS_AND_COST_CODES.md plus schemas | ad-hoc spreadsheet columns |
| Schedule control | docs/02-controls/SCHEDULE_CONTROL.md | dashboard calculations |
| Cost/EVM | docs/02-controls/COST_AND_EVM.md plus tools/evm.py | manually typed KPI claims |
| Risk/issue/opportunity | docs/02-controls/RISK_ISSUE_OPPORTUNITY.md | hidden chat lists |
| Change | docs/02-controls/CHANGE_CONTROL.md | unlinked edits to baselines |
| Contract/claim/payment | docs/02-controls/CONTRACTS_CLAIMS_AND_PAYMENTS.md | informal commercial notes |
| Quality | docs/02-controls/QUALITY_CONTROL.md | untracked inspection decisions |
| HSE/environment | docs/02-controls/HSE_AND_ENVIRONMENT.md | private-only incident records |
| Procurement | docs/02-controls/PROCUREMENT_AND_SUPPLY_CHAIN.md | unowned purchase lists |
| Stakeholder/land/utilities | docs/02-controls/STAKEHOLDER_AND_LAND_UTILITIES.md | unlinked interface assumptions |
| Documents | docs/02-controls/DOCUMENT_CONTROL.md | duplicate uncontrolled files |
| Reporting | docs/03-reporting/ plus source records | copied numbers without cut-off date |
| AI assistance | docs/04-ai/AI_OPERATING_MODEL.md | agent-invented project facts |

## Directory contract

- apps/ contains executable or viewable product surfaces.
- config/ contains project-level configuration and thresholds.
- data/ contains controlled reference data and explicitly fictional examples.
- docs/ contains human-readable operating rules and playbooks.
- schemas/ contains machine-readable record contracts.
- templates/ contains copyable forms; templates are not records.
- tools/ contains deterministic, dependency-light utilities.
- .github/ contains collaboration governance and CI.

## Evidence labels

Use one of these labels in reports and decisions:

- Observed — directly supported by a source record.
- Calculated — deterministically derived from source records.
- Estimated — produced with a stated method and uncertainty.
- Assumed — used temporarily and awaiting confirmation.
- Decided — approved by an accountable authority.
- Unknown — not available; do not replace with a guess.

## Current snapshot

The initial repository was empty. The foundation commit establishes the target control plane, not a real project baseline. All values under data/examples/demo-road-project are fictional and must not be used for payment, safety, engineering or contractual decisions.
