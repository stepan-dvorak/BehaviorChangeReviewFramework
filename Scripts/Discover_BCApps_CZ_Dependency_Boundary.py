#!/usr/bin/env python3
"""Generate the fixed source boundary for CZL subscriber-context resolution."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path


EXPECTED_COMMIT = "397d01199c321e774edaf23a7290fee40f75c6a6"
EXPECTED_VERSION = "29.0.0.0"

APPS = [
    {
        "boundary_id": "CZDEP-0001",
        "app_id": "267b59d3-7302-44c5-ba77-c87000380514",
        "app_name": "Core Localization Pack for Czech",
        "manifest_path": "src/Apps/CZ/CoreLocalizationPack/app/app.json",
        "source_root": "src/Apps/CZ/CoreLocalizationPack/app/Src",
        "relationship_to_subject": "Subject",
        "evidence_basis": "Fixed subject manifest",
        "resolution_order": "1",
    },
    {
        "boundary_id": "CZDEP-0002",
        "app_id": "0a9a9ce1-6f98-4cf0-82e2-0b3e7cabb32a",
        "app_name": "EU 3-Party Trade Purchase",
        "manifest_path": "src/Apps/W1/EU3PartyTradePurchase/app/app.json",
        "source_root": "src/Apps/W1/EU3PartyTradePurchase/app",
        "relationship_to_subject": "Explicit Dependency",
        "evidence_basis": "Listed in fixed subject manifest",
        "resolution_order": "2",
    },
    {
        "boundary_id": "CZDEP-0003",
        "app_id": "437dbf0e-84ff-417a-965d-ed2bb9650972",
        "app_name": "Base Application",
        "manifest_path": "src/Layers/W1/BaseApp/app.json",
        "source_root": "src/Layers/W1/BaseApp",
        "relationship_to_subject": "Application Resolution Layer",
        "evidence_basis": "Application abstraction guidance and fixed Base Application manifest",
        "resolution_order": "3",
    },
    {
        "boundary_id": "CZDEP-0004",
        "app_id": "f3552374-a1f2-4356-848e-196002525837",
        "app_name": "Business Foundation",
        "manifest_path": "src/Business Foundation/App/app.json",
        "source_root": "src/Business Foundation/App",
        "relationship_to_subject": "Base Application Dependency",
        "evidence_basis": "Listed in fixed Base Application manifest",
        "resolution_order": "4",
    },
    {
        "boundary_id": "CZDEP-0005",
        "app_id": "63ca2fa4-4f03-4f2b-a480-172fef340d3f",
        "app_name": "System Application",
        "manifest_path": "src/System Application/App/app.json",
        "source_root": "src/System Application/App",
        "relationship_to_subject": "Base and Business Foundation Dependency",
        "evidence_basis": "Listed in fixed Base Application and Business Foundation manifests",
        "resolution_order": "5",
    },
]

FIELDS = [
    "boundary_id", "source_commit", "app_id", "app_name", "publisher",
    "version", "application_version", "platform_version", "manifest_path",
    "source_root", "relationship_to_subject", "evidence_basis",
    "source_availability", "resolution_order",
]


def git_commit(root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True, capture_output=True, text=True,
    )
    return result.stdout.strip()


def load_manifest(root: Path, relative: str) -> dict[str, object]:
    path = root / relative
    if not path.is_file():
        raise ValueError(f"manifest does not exist: {relative}")
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_git_path(root: Path, relative: str) -> None:
    """Require a path in the fixed commit even when sparse checkout omits it."""
    result = subprocess.run(
        ["git", "-C", str(root), "cat-file", "-e", f"HEAD:{relative}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise ValueError(f"source root does not exist at fixed commit: {relative}")


def dependencies(manifest: dict[str, object]) -> dict[str, dict[str, object]]:
    return {
        str(item["id"]): item
        for item in manifest.get("dependencies", [])
        if isinstance(item, dict) and "id" in item
    }


def validate_relationships(manifests: dict[str, dict[str, object]]) -> None:
    czl = manifests[APPS[0]["app_id"]]
    eu = APPS[1]["app_id"]
    if eu not in dependencies(czl):
        raise ValueError("CZL manifest does not contain the expected explicit dependency")
    if czl.get("application") != EXPECTED_VERSION:
        raise ValueError("CZL application version does not match the fixed boundary")

    base = manifests[APPS[2]["app_id"]]
    if base.get("propagateDependencies") is not True:
        raise ValueError("Base Application does not propagate dependencies")
    base_dependencies = dependencies(base)
    for app in (APPS[3], APPS[4]):
        if app["app_id"] not in base_dependencies:
            raise ValueError(f"Base Application dependency missing: {app['app_name']}")

    foundation = manifests[APPS[3]["app_id"]]
    if APPS[4]["app_id"] not in dependencies(foundation):
        raise ValueError("Business Foundation dependency on System Application is missing")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bcapps-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    root = args.bcapps_root.resolve()
    commit = git_commit(root)
    if commit != EXPECTED_COMMIT:
        parser.error(f"BCApps HEAD is {commit}; expected {EXPECTED_COMMIT}")

    manifests: dict[str, dict[str, object]] = {}
    rows: list[dict[str, str]] = []
    for expected in APPS:
        manifest = load_manifest(root, expected["manifest_path"])
        require_git_path(root, expected["source_root"])
        if manifest.get("id") != expected["app_id"]:
            raise ValueError(f"unexpected app ID in {expected['manifest_path']}")
        if manifest.get("name") != expected["app_name"]:
            raise ValueError(f"unexpected app name in {expected['manifest_path']}")
        if manifest.get("publisher") != "Microsoft" or manifest.get("version") != EXPECTED_VERSION:
            raise ValueError(f"unexpected publisher or version in {expected['manifest_path']}")
        manifests[expected["app_id"]] = manifest
        rows.append({
            **expected,
            "source_commit": commit,
            "publisher": str(manifest["publisher"]),
            "version": str(manifest["version"]),
            "application_version": str(manifest.get("application", "")),
            "platform_version": str(manifest.get("platform", "")),
            "source_availability": "Public Source at Fixed Commit",
        })

    validate_relationships(manifests)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"commit={commit}")
    print(f"boundary_applications={len(rows)}")
    print(f"output={args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
