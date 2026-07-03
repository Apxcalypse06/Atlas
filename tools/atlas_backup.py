from __future__ import annotations

import argparse
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKUPS = ROOT / "BACKUPS"
EXCLUDED_DIRS = {".git", "backups", "__pycache__", ".pytest_cache", ".codex_tmp"}
EXCLUDED_FILE_NAMES = {"Atlas_handoff.zip"}
EXCLUDED_PREFIXES = (".tmp_",)


def should_exclude(path: Path) -> bool:
    relative_parts = path.relative_to(ROOT).parts
    lowered_parts = [part.lower() for part in relative_parts]
    if any(part in EXCLUDED_DIRS for part in lowered_parts):
        return True
    if path.name in EXCLUDED_FILE_NAMES:
        return True
    return any(part.startswith(EXCLUDED_PREFIXES) for part in relative_parts)


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and not should_exclude(path):
            files.append(path)
    return sorted(files)


def safe_name(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in ".-" else "-" for ch in value.strip())
    return cleaned.strip("-") or "atlas-change"


def create_backup(pac_id: str, label: str | None = None) -> Path:
    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    name_parts = ["Atlas", "before", safe_name(pac_id)]
    if label:
        name_parts.append(safe_name(label))
    backup_path = BACKUPS / ("_".join(name_parts) + f"_{stamp}.zip")

    BACKUPS.mkdir(parents=True, exist_ok=True)
    files = iter_files()
    metadata = {
        "created_at": now.isoformat(),
        "purpose": "pre-change rollback snapshot",
        "pac_id": pac_id,
        "label": label,
        "root": str(ROOT),
        "file_count": len(files),
        "excluded_dirs": sorted(EXCLUDED_DIRS),
        "excluded_file_names": sorted(EXCLUDED_FILE_NAMES),
        "excluded_prefixes": list(EXCLUDED_PREFIXES),
    }

    with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("BACKUP_MANIFEST.json", json.dumps(metadata, ensure_ascii=False, indent=2))
        for path in files:
            archive.write(path, path.relative_to(ROOT).as_posix())

    with zipfile.ZipFile(backup_path, "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise ValueError(f"backup ZIP failed integrity check at {bad}")

    return backup_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="atlas_backup")
    parser.add_argument("pac_id", help="PAC or PAC patch id that is about to change Atlas")
    parser.add_argument("--label", help="Optional backup label")
    args = parser.parse_args(argv)

    backup_path = create_backup(args.pac_id, args.label)
    print(f"Atlas backup created: {backup_path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
