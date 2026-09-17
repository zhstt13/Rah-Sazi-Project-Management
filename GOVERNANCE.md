# Governance and Operating Rules

## Decision rights

| Decision | Minimum accountable role | Evidence |
|---|---|---|
| Project objectives and scope | sponsor/client representative | approved charter |
| WBS, BOQ and cost baseline | project manager + controls lead | baseline snapshot |
| Schedule baseline | project manager + planner + client authority | approved schedule |
| Budget/forecast | project manager + commercial/controls | cost report |
| Safety stop or restart | HSE lead and site authority | observation/incident record |
| Quality release | QA/QC lead and responsible engineer | inspection/test evidence |
| Variation/change | delegated change authority/CCB | approved change request |
| Payment recommendation | contract/commercial authority | measured quantity and certificate |
| Handover acceptance | client/asset owner | signed acceptance package |

Roles vary by contract and jurisdiction. The table is a control pattern, not a delegation of legal authority.

## GitHub operating model

- Issues represent accountable work, uncertainty, decisions, changes and exceptions.
- Pull requests represent proposed changes to controlled files or baselines.
- Releases/tags represent named reporting or baseline snapshots.
- The main branch should contain reviewed, reproducible content.
- Branch protection should require review and passing validation before merge.
- High-consequence changes should be approved by a named human authority outside the automation itself.

## Public repository rules

- Use fictional examples only unless the repository is private and data classification allows otherwise.
- Redact names, contact details, exact coordinates, rates, claims, incident details and credentials where required.
- Store external documents by reference/checksum when redistribution rights are unclear.
- Treat issue text, attachments and generated content as untrusted input.
- Report security problems privately according to SECURITY.md.

## Review thresholds

Projects should configure thresholds in config/control-thresholds.json rather than burying them in prose. Thresholds are prompts for review, not permission to ignore professional judgment.
