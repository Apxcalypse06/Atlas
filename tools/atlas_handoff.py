from __future__ import annotations

import argparse
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "Handover" / "Atlas_handoff.zip"
MAX_HANDOFF_BYTES = 512 * 1024 * 1024
EXCLUDED_DIRS = {".git", "backups", "__pycache__", ".pytest_cache", ".codex_tmp"}
EXCLUDED_FILE_NAMES = {"Atlas_handoff.zip"}
EXCLUDED_PREFIXES = (".tmp_",)


def should_exclude(path: Path, output: Path) -> bool:
    if path.resolve() == output.resolve():
        return True
    relative_parts = path.relative_to(ROOT).parts
    lowered_parts = [part.lower() for part in relative_parts]
    if any(part in EXCLUDED_DIRS for part in lowered_parts):
        return True
    if path.name in EXCLUDED_FILE_NAMES:
        return True
    return any(part.startswith(EXCLUDED_PREFIXES) for part in relative_parts)


def iter_files(output: Path) -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and not should_exclude(path, output):
            files.append(path)
    return sorted(files)


def create_handoff(output: Path = DEFAULT_OUTPUT, max_bytes: int = MAX_HANDOFF_BYTES) -> Path:
    output = output if output.is_absolute() else ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    files = iter_files(output)
    now = datetime.now(timezone.utc)
    metadata = {
        "created_at": now.isoformat(),
        "purpose": "assistant handoff package",
        "max_bytes": max_bytes,
        "excluded_dirs": sorted(EXCLUDED_DIRS),
        "excluded_file_names": sorted(EXCLUDED_FILE_NAMES),
        "excluded_prefixes": list(EXCLUDED_PREFIXES),
        "file_count": len(files),
        "entrypoint": "START_HERE.md",
    }

    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("HANDOFF_MANIFEST.json", json.dumps(metadata, ensure_ascii=False, indent=2))
        for path in files:
            archive.write(path, path.relative_to(ROOT).as_posix())

    with zipfile.ZipFile(output, "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise ValueError(f"handoff ZIP failed integrity check at {bad}")

    size = output.stat().st_size
    if size > max_bytes:
        raise ValueError(f"handoff ZIP is too large: {size} bytes > {max_bytes} bytes")
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="atlas_handoff")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT.relative_to(ROOT)), help="Output ZIP path")
    parser.add_argument("--max-mb", type=int, default=512, help="Maximum allowed handoff size in MB")
    args = parser.parse_args(argv)

    output = create_handoff(Path(args.output), args.max_mb * 1024 * 1024)
    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"Atlas handoff created: {output.relative_to(ROOT).as_posix()} ({size_mb:.2f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
