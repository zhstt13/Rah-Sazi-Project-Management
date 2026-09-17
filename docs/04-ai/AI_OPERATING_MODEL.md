# AI Operating Model

## Purpose

AI can reduce administrative load across project controls, but it must operate inside the evidence and approval model.

## Safe AI roles

- classify incoming records and suggest the owning register;
- extract fields from approved documents with source citations;
- calculate deterministic metrics;
- compare revisions and summarize deltas;
- draft a risk, change, RFI, report or decision record;
- identify missing fields, stale data, contradictions and likely duplicates;
- generate a look-ahead summary from approved records;
- propose questions for human review.

## Prohibited autonomous actions

An agent must not independently:

- approve a baseline, payment, variation, claim, safety release or quality release;
- invent quantities, costs, dates, test results, contract terms or legal conclusions;
- close a risk, NCR, incident or corrective action without evidence;
- overwrite an approved record;
- publish personal or confidential information;
- infer a utility location, hazard control or engineering acceptance from silence;
- conceal uncertainty or replace unknown with a plausible value.

## Agent response contract

Every AI-generated output should identify:

- records and revisions used;
- cut-off date;
- facts vs calculations vs assumptions;
- missing or conflicting evidence;
- recommendation, if any;
- human role required to approve;
- proposed next action and owner.

## Suggested agents

| Agent | Input | Output | Human gate |
|---|---|---|---|
| Controls analyst | schedule, cost and progress snapshots | variance/forecast draft | controls lead |
| Risk analyst | risks, issues, constraints and changes | exposure and action draft | PM/HSE/commercial |
| Document analyst | approved document index | missing/superseded/link report | document controller |
| Field-report assistant | daily reports and photos | structured draft and anomalies | site lead |
| Handover analyst | asset/evidence index | readiness gap report | QA/QC and asset owner |

The repository should make an agent’s evidence boundary inspectable before any integration is enabled.
