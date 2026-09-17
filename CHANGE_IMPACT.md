# Change Impact — Foundation

## Current → target

### Current, proven

- Repository: zhstt13/Rah-Sazi-Project-Management
- Default branch: main
- Visibility: public
- Repository contents before foundation: empty
- Existing application behavior: none
- Existing data contracts: none
- Existing CI or deployment: none

### Target

A repository-native project operating system with:

- explicit domain ownership;
- machine-readable schemas;
- controlled example data;
- deterministic validation;
- human approval gates;
- issue and PR workflows;
- a static dashboard starter;
- a documented path to external schedule, ERP, CDE, GIS and BIM integrations.

## Foundation change set

| Surface | Change | Risk | Verification |
|---|---|---:|---|
| Root docs | architecture, map, governance and decisions | low | link and content review |
| docs/ | operating and control playbooks | medium | review against architecture |
| schemas/ | JSON Schema contracts | medium | JSON parsing and required fields |
| data/ | fictional examples and dictionaries | medium | validator and referential checks |
| tools/ | validation and EVM calculator | medium | Python compile/run checks |
| .github/ | issue forms, PR template and CI | medium | YAML structure review; Actions execution after push |
| apps/dashboard/ | static example dashboard | low | syntax and manual browser review |

## Preservation constraints

- Do not treat sample data as real project data.
- Do not silently change an approved baseline.
- Do not add personal, financial, health, incident or security-sensitive information to public files.
- Do not turn the dashboard into a second editable source of truth.
- Do not claim compliance with a standard solely because a similarly named folder exists.
- Do not add external integrations without a source identifier, access boundary and failure behavior.

## Unresolved risks

1. GitHub branch protection and required reviewers are not configured by repository content alone.
2. A public repository needs a deliberate license and data-classification decision.
3. JSON Schema files are contracts; the current dependency-light validator is not a full JSON Schema implementation.
4. Local regulations, contract conditions, schedule-of-rates and safety rules must be supplied by the project owner.
5. Dashboard values are fictional until a data adapter is implemented.
