from __future__ import annotations

import json
import sys
from pathlib import Path

from atlas_generate_start_here import render_start_here


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "MANIFEST.json"
FINAL_STATUSES = {"DONE", "FEATURE_COMPLETE"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_manifest() -> dict:
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"MANIFEST.json is invalid JSON: {exc}") from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_entrypoint(manifest: dict) -> None:
    entrypoint = manifest.get("entrypoint")
    require(isinstance(entrypoint, str) and entrypoint, "MANIFEST.json must declare entrypoint")
    require((ROOT / entrypoint).exists(), f"entrypoint does not exist: {entrypoint}")

    read_order = manifest.get("recommended_read_order")
    require(isinstance(read_order, list) and read_order, "recommended_read_order must be a non-empty list")
    require(read_order[0] == entrypoint, "recommended_read_order must start with entrypoint")
    for item in read_order:
        require(isinstance(item, str), "recommended_read_order entries must be strings")
        require((ROOT / item).exists(), f"recommended_read_order path does not exist: {item}")


def validate_manifest_sections(manifest: dict) -> None:
    for section in ("status", "included_files", "missing_files"):
        require(isinstance(manifest.get(section), dict), f"MANIFEST.json must contain object section: {section}")

    status_keys = set(manifest["status"])
    included_keys = set(manifest["included_files"])
    missing_keys = set(manifest["missing_files"])
    require(status_keys == included_keys, "status and included_files PAC keys must match")
    require(status_keys == missing_keys, "status and missing_files PAC keys must match")


def validate_included_files(manifest: dict) -> None:
    for pac_id, files in manifest["included_files"].items():
        require(isinstance(files, list), f"included_files.{pac_id} must be a list")
        missing = []
        for file_name in files:
            require(isinstance(file_name, str), f"included_files.{pac_id} entries must be strings")
            if not (ROOT / file_name).exists():
                missing.append(file_name)
        declared_missing = manifest["missing_files"].get(pac_id)
        require(declared_missing == missing, f"missing_files.{pac_id} does not match filesystem state")


def validate_finished_pacs(manifest: dict) -> None:
    for pac_id, status in manifest["status"].items():
        if status not in FINAL_STATUSES:
            continue
        files = manifest["included_files"].get(pac_id, [])
        require(files, f"{pac_id} is {status} but has no included release files")
        zip_files = [file_name for file_name in files if file_name.endswith(".zip")]
        require(zip_files, f"{pac_id} is {status} but has no release archive")
        qa_files = [file_name for file_name in files if "qa" in Path(file_name).name.lower()]
        require(qa_files, f"{pac_id} is {status} but has no QA archive")

        current_status = ROOT / "Current" / pac_id / "STATUS.md"
        if pac_id.startswith("PAC-007.2.") or pac_id.startswith("ATLAS-GOV-"):
            require(current_status.exists(), f"{pac_id} must have {rel(current_status)}")


def validate_governance() -> None:
    required = [
        ROOT / "START_HERE.md",
        ROOT / "GOVERNANCE" / "CHANGE_PROTOCOL.md",
        ROOT / "BACKUPS" / "README.md",
        ROOT / "tools" / "atlas_backup.py",
        ROOT / "tools" / "atlas_generate_start_here.py",
        ROOT / "tools" / "atlas_handoff.py",
        ROOT / "tools" / "atlas_validate.py",
    ]
    for path in required:
        require(path.exists(), f"required governance file missing: {rel(path)}")


def validate_backup_policy(manifest: dict) -> None:
    policy = manifest.get("backup_policy")
    require(isinstance(policy, dict), "MANIFEST.json must declare backup_policy")
    require(policy.get("tool") == "tools/atlas_backup.py", "backup_policy.tool must be tools/atlas_backup.py")
    require(policy.get("directory") == "BACKUPS/", "backup_policy.directory must be BACKUPS/")
    require(
        policy.get("enforced_from") == "ATLAS-GOV-003",
        "backup_policy.enforced_from must be ATLAS-GOV-003",
    )
    require((ROOT / policy["tool"]).exists(), f"backup policy tool does not exist: {policy['tool']}")
    require((ROOT / policy["directory"]).exists(), f"backup policy directory does not exist: {policy['directory']}")


def validate_generated_entrypoint(manifest: dict) -> None:
    current = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
    expected = render_start_here(manifest)
    require(current == expected, "START_HERE.md is not generated from current MANIFEST.json")


def main() -> int:
    try:
        manifest = load_manifest()
        validate_entrypoint(manifest)
        validate_manifest_sections(manifest)
        validate_included_files(manifest)
        validate_finished_pacs(manifest)
        validate_governance()
        validate_backup_policy(manifest)
        validate_generated_entrypoint(manifest)
    except AssertionError as exc:
        print(f"Atlas validation failed: {exc}")
        return 1

    print("Atlas validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
