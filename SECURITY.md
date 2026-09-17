# Security and Sensitive Information

## Scope

This repository may contain project-control records. Even when the repository is public, project records can expose sensitive commercial, personal, location, security or safety information.

## Do not commit

- credentials, tokens, private keys or connection strings;
- personal identifiers, phone numbers, private addresses or health data;
- unredacted incidents, investigations or near-miss details;
- exact security-sensitive infrastructure information;
- confidential contract rates, claims, legal advice or privileged correspondence;
- unpublished land, utility or stakeholder data;
- proprietary drawings, models, laboratory reports or vendor documents without permission.

## Safe pattern

Store a sanitized record with:

- a stable internal ID;
- classification;
- owner;
- source-system reference;
- access-controlled location;
- checksum where appropriate;
- redacted summary;
- decision and follow-up.

## Reporting

Do not open a public issue for a security vulnerability or exposure. Contact the repository owner through a private channel and include the minimum necessary detail.

This file is a repository practice, not a substitute for the project’s formal information-security, privacy, HSE or emergency procedures.
