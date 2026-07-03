# PAC-009 - Memory Review & Maintenance

Status: Done

## Goal

Review and maintain committed memory entries without physically deleting memory.

## Implemented commands

```bash
pac memory review project.pac.zip
pac memory review project.pac.zip --include-deprecated
pac memory update project.pac.zip --memory-id MEM-... --statement "..." --updated-by Tommy --reason "..."
pac memory deprecate project.pac.zip --memory-id MEM-... --deprecated-by Tommy --reason "..."
pac memory merge project.pac.zip --target-id MEM-a --source-id MEM-b --merged-by Tommy --reason "..."
```

## Input artifacts

```text
user/memory.json
projects/<project_id>/memory.json
shared/memory.json
```

## Maintenance rules

```text
review
    -> list memory entries

update
    -> replace statement/text and append maintenance_history

deprecate
    -> mark status=deprecated and keep the entry

merge
    -> annotate target with merged_from and deprecate source
```

Deprecated entries are hidden from default review and can be shown with `--include-deprecated`.

## Source artifact boundary

PAC-009 does not modify:

- source session files;
- analysis artifacts;
- validation artifacts;
- selection artifacts.

PAC-009 may update:

- memory domain files;
- `MANIFEST.json.updated_at`;
- `logs/changelog.md`.

PAC-009 does not automatically regenerate PAC-008 views. Run `pac session handover` after maintenance to refresh generated views and handover artifacts.

## Release artifacts

- `Releases/PAC-009/pac-cli-pac009-memory-review-maintenance.zip`
- `Releases/PAC-009/pac-cli-pac009-qa-package.zip`

## Verification

```text
py -m pytest -q
77 passed in 6.42s

py tools\atlas_generate_start_here.py --check
START_HERE.md is up to date

py tools\atlas_validate.py
Atlas validation passed
```

## Non-goals

- no KEEP / IGNORE decision logic;
- no candidate classification;
- no conversation import;
- no physical deletion of memory entries;
- no automatic PAC-008 view regeneration;
- no LLM dependency.
