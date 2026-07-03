# Atlas

Atlas is a cognitive continuity subsystem.

Hierarchy:

```text
Global Project
`-- Future powerful / self-improving AI system
    `-- Atlas
        `-- Cognitive continuity ecosystem
            `-- PAC
                `-- Portable capsule and CLI tooling
```

## Mission

Atlas aims to ensure cognitive continuity based on information that is:

- traceable;
- verified;
- transmissible.

## Important clarification

The current `Atlas.zip` is not yet a fully living memory file.

It currently contains:

- architecture;
- releases;
- QA packages;
- reviews;
- handover material;
- project governance;
- PAC implementation artifacts.

It does not yet contain the future cognitive memory layer:

```text
user/memory.json
projects/<project_id>/memory.json
shared/memory.json
```

This memory layer is expected to emerge through:

- PAC-007.2 - Knowledge Selection & Classification;
- PAC-007.3 - Memory Commit;
- PAC-008 - Generate Cognitive Views & Handover.

## Canonical PAC pipeline

```text
PAC-005   Import Conversation
PAC-006   Extract Candidate Knowledge
PAC-007.1 Create Validation Artifact
PAC-007.2 Select + Classify Knowledge
PAC-007.3 Commit to Memory
PAC-008   Generate Cognitive Views & Handover
PAC-009   Review & Maintain Memory
```

## Current PAC status

- PAC-001: DONE
- PAC-002: DONE
- PAC-003: DONE
- PAC-004: DONE
- PAC-005: DONE
- PAC-006: DONE
- PAC-007.1: DONE
- PAC-007.2: DONE
- PAC-007.3: DONE
- PAC-008: DONE
- PAC-009: DONE

## Governance status

- ATLAS-GOV-001: DONE
- ATLAS-GOV-002: DONE
- ATLAS-GOV-003: DONE
- ATLAS-GOV-004: DONE
- ATLAS-GOV-005: DONE
- ATLAS-GOV-006: DONE
- ATLAS-GOV-007: DONE
- ATLAS-GOV-008: DONE
- ATLAS-GOV-009: DONE
- ATLAS-GOV-010: DONE

Historical note:

```text
PAC-007.2.1 -> ATLAS-GOV-001
PAC-007.2.2 -> ATLAS-GOV-002
PAC-007.2.3 -> ATLAS-GOV-003
PAC-007.2.4 -> ATLAS-GOV-004
PAC-007.2.5 -> ATLAS-GOV-005
```

The legacy `Current/PAC-007.2.1` through `Current/PAC-007.2.5` folders were removed by `ATLAS-GOV-007`.
Their historical release archives remain under `Releases/PAC-007.2.x/`.

Status note:

`ATLAS-GOV-008` defines `DONE` as the final status for completed PACs after implementation, release archive, QA archive, manifest alignment, generated entrypoint alignment, and passing Atlas validation.

Memory feedback note:

`ATLAS-GOV-009` says assistants may keep stable user information through the Atlas memory pipeline without asking again every time. They should explicitly tell the user whether the information was recorded in Atlas.

Transfer note:

`ATLAS-GOV-010` separates local rollback backups from assistant transfer packages. Use `py tools/atlas_handoff.py` to create `Handover/Atlas_handoff.zip` for a new assistant. Do not send `BACKUPS/`.

## Change governance

Before structural Atlas changes, read:

```text
GOVERNANCE/CHANGE_PROTOCOL.md
```

Then run:

```bash
py tools/atlas_validate.py
```

Before future structural changes, create a rollback backup:

```bash
py tools/atlas_backup.py <PAC_ID>
```

After manifest or status changes, regenerate the resume entrypoint:

```bash
py tools/atlas_generate_start_here.py
```

To create a lightweight handoff package for a new assistant:

```bash
py tools/atlas_handoff.py
```

## Current next step

No active PAC - define next Atlas roadmap item

Goal:

Review the completed PAC-005 through PAC-009 continuity pipeline and define the next Atlas roadmap item.

PAC-009 now reviews and maintains committed memory. It does not replace PAC-007.3 memory commit or PAC-008 view generation.
