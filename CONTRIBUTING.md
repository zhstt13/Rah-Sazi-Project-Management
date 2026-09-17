# Contributing

## Before opening a change

1. Identify the owning domain in REPOSITORY_MAP.md.
2. State whether the change is documentation, schema, data, calculation, workflow or UI.
3. Preserve existing behavior unless the change explicitly updates the contract.
4. Link evidence, issue, decision or external-source record when the change affects project facts.
5. Never commit secrets, private personal data, unapproved commercial terms or real incident details to a public repository.

## Change types

- docs: clarify or extend an operating rule;
- schema: add or change a machine-readable contract;
- data: add controlled reference or fictional example data;
- control: change a calculation, threshold or workflow;
- ui: change the dashboard or another view;
- ci: change validation or repository governance.

## Required checks

Run:

    python tools/validate_repository.py
    python -m py_compile tools/validate_repository.py tools/evm.py
    python tools/evm.py --pv 1200000 --ev 1140000 --ac 1180000

For schema or data changes, explain compatibility and migration impact in the PR.

## Review standard

A reviewer should be able to answer:

- What problem is solved?
- Which file owns the new rule?
- What evidence supports the change?
- What behavior or data remains unchanged?
- What is verified automatically?
- What remains unproven or project-specific?

## Commit style

Use a short, imperative subject:

- docs: define gate-3 exit criteria
- schema: add payment certificate fields
- control: clarify ETC calculation
- ci: validate JSON examples
