# ATLAS-GOV-010 - Transfer Package & Backup Exclusion

Status: Done

## Purpose

Separate the local Atlas workspace from the lightweight package that should be transmitted to a new assistant.

## Problem

Atlas rollback backups had started to include previous backups because the exclusion rule used `Backups` while the actual directory is `BACKUPS`.

That made backup archives grow recursively and pushed the full workspace above assistant upload limits.

## Rule

The local Atlas workspace may keep rollback backups under:

```text
BACKUPS/
```

The assistant transfer package must exclude:

```text
BACKUPS/
.codex_tmp/
__pycache__/
.pytest_cache/
Atlas_handoff.zip
```

## Added Tool

```bash
py tools\atlas_handoff.py
```

Default output:

```text
Handover/Atlas_handoff.zip
```

The generated handoff ZIP must stay below 512 MB.

## Updated Tool

`tools/atlas_backup.py` now excludes `BACKUPS/` case-insensitively and also excludes `.codex_tmp/`.

## Release artifacts

- `Releases/ATLAS-GOV-010/atlas-gov-010-transfer-package-backup-exclusion.zip`
- `Releases/ATLAS-GOV-010/atlas-gov-010-qa-package.zip`

## Verification

```text
py tools\atlas_handoff.py
py tools\atlas_generate_start_here.py --check
py tools\atlas_validate.py
```

## Non-goals

- no deletion of existing rollback backups;
- no PAC CLI behavior changes;
- no memory behavior changes.
