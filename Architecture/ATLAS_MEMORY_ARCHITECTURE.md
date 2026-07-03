# Atlas Memory Architecture

## Current Architectural Decision

Atlas has the cognitive pipeline and PAC release machinery.

PAC-007.3 introduces the first memory commit stage for selected knowledge candidates.

PAC-008 introduces generated cognitive views and handovers from committed memory.

PAC-009 introduces memory review and maintenance for committed memory entries.

Atlas now contains the reference continuity pipeline through handover generation, but it is still not a complete long-term cognitive memory system.

## Distinction

```text
Atlas

|-- Cognitive Operating System
|   |-- PAC releases
|   |-- architecture
|   |-- QA
|   |-- reviews
|   |-- handovers
|   `-- governance
|
`-- Cognitive Memory
    |-- user/memory.json
    |-- projects/<project_id>/memory.json
    `-- shared/memory.json
```

## Memory Domains

### User Memory

Path:

```text
user/memory.json
```

Purpose:

Information about the user that may be useful for continuity.

Examples:

- identity;
- preferences;
- constraints;
- working style;
- stable personal attributes;
- long-term goals.

### Project Memory

Path:

```text
projects/<project_id>/memory.json
```

Purpose:

Information about a specific project.

Examples:

- architecture decisions;
- roadmap;
- releases;
- QA results;
- risks;
- open tasks;
- principles;
- project state.

### Shared Memory

Path:

```text
shared/memory.json
```

Purpose:

Cross-project knowledge or general Atlas-level principles.

## PAC-007.2 Role

PAC-007.2 does not commit memory.

It selects and classifies candidate information:

```text
candidate information
    -> keep / ignore
    -> if keep: user / project / shared
    -> if project: project_id
```

## PAC-007.3 Role

PAC-007.3 commits selected information into the appropriate memory domain:

```text
keep=true, category=user
    -> user/memory.json

keep=true, category=project, project_id=Atlas
    -> projects/Atlas/memory.json

keep=true, category=shared
    -> shared/memory.json
```

PAC-007.3 ignores candidates where `keep` is not `true`.

PAC-007.3 preserves provenance from:

- session;
- analysis;
- validation;
- selection;
- candidate source.

## PAC-008 Role

PAC-008 generates cognitive views and handovers from committed memory:

```text
user/memory.json
projects/<project_id>/memory.json
shared/memory.json
    -> views/current/*.json
    -> handovers/current.md
```

PAC-008 should not replace PAC-007.3. It should consume memory after commit.

PAC-008 preserves committed memory entries as source artifacts and writes derived view and handover artifacts.

## PAC-009 Role

PAC-009 maintains committed memory entries:

```text
review
update
deprecate
merge
```

PAC-009 does not physically delete memory entries.

PAC-009 preserves maintenance history so changes remain auditable.

## Principle

Atlas should not only store data.

Atlas should preserve continuity by organizing memory according to domain, provenance, and purpose.
