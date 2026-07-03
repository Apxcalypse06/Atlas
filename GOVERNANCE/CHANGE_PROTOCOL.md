# Atlas Change Protocol

## Rule

No structural Atlas change should be made without a PAC or PAC patch.

This applies to changes that affect:

- architecture;
- governance;
- manifest;
- README;
- entrypoints;
- current status files;
- release artifacts;
- QA packages;
- handover structure;
- memory architecture.

## Required Flow

Before editing structural Atlas files:

1. Identify the PAC or PAC patch.
2. Define why the change exists.
3. Define the files that will be added or updated.
4. Create a rollback backup.
5. Define the expected release archive.
6. Define the expected QA archive.
7. Apply the change.
8. Update `MANIFEST.json`.
9. Regenerate `START_HERE.md`.
10. Run `tools/atlas_validate.py`.

## Backup Requirement

Before future structural changes, run:

```bash
py tools/atlas_backup.py <PAC_ID>
```

Example:

```bash
py tools/atlas_backup.py PAC-007.3 --label before-memory-commit
```

Backups are written under:

```text
BACKUPS/
```

Backup archives are rollback snapshots. They do not replace release archives or QA packages.

Backups must exclude `BACKUPS/` itself so rollback snapshots do not recursively include previous rollback snapshots.

## Assistant Handoff Package

Do not send the full local Atlas workspace to a new assistant if it contains rollback backups.

Create a lightweight transfer package instead:

```bash
py tools/atlas_handoff.py
```

Default output:

```text
Handover/Atlas_handoff.zip
```

The handoff package excludes rollback backups and local working caches.

## Patch Requirements

Every PAC patch should include:

- `Current/<PAC_ID>/STATUS.md`;
- one release archive under `Releases/<PAC_ID>/`;
- one QA archive under `Releases/<PAC_ID>/`;
- a `MANIFEST.json` entry in `status`;
- a `MANIFEST.json` entry in `included_files`;
- a `MANIFEST.json` entry in `missing_files`.

## Status Semantics

For pipeline PAC work, `FEATURE_COMPLETE` is a temporary state before final release / QA / Atlas validation closure.

Once a PAC has implementation, status file, release archive, QA archive, manifest alignment, generated entrypoint alignment, and passing Atlas validation, its final status should be `DONE`.

## Memory Feedback

For stable user information that clearly concerns the user, assistants do not need to ask for confirmation every time before keeping it in Atlas memory.

Assistants must still use the controlled Atlas memory pipeline. They must also tell the user whether the information was recorded in Atlas.

Acceptable feedback examples:

```text
I noted this in Atlas memory.
I did not note this in Atlas because it looked temporary / not useful for continuity.
I cannot note this yet because the memory pipeline was not run.
```

## Naming

Pipeline PAC IDs use the `PAC-*` namespace:

```text
PAC-007.2
PAC-007.3
PAC-008
```

Atlas governance patches use the `ATLAS-GOV-*` namespace:

```text
ATLAS-GOV-001
ATLAS-GOV-002
```

Use `ATLAS-GOV-*` for entrypoints, validation, backups, generated files, taxonomy, manifest governance, or change protocol updates.

Historical `PAC-007.2.x` governance patches are preserved as reclassified history and should not be used for new governance work.

## Validation

Regenerate the entrypoint:

```bash
py tools/atlas_generate_start_here.py
```

Run:

```bash
py tools/atlas_validate.py
```

The validator checks that `START_HERE.md` matches the generator output.

The validator should pass before a patch is considered complete.

## Non-goals

This protocol does not replace human review.

It prevents obvious untracked structural changes and makes future assistants start from the same discipline.
