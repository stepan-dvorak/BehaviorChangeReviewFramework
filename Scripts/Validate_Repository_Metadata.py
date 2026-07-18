#!/usr/bin/env python3
"""Validate Orden repository metadata, relationships, and retrieval index."""

from __future__ import annotations

import argparse
import fnmatch
import json
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - exercised before dependencies exist
    print(
        "Validation dependency missing. Run: "
        "python -m pip install -r requirements-validation.txt",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


ENTRYPOINTS = {"README.md", "AGENTS.md", "AGENTS.override.md"}
RELATIONSHIP_KEYS = (
    "depends_on",
    "related_documents",
    "supersedes",
    "superseded_by",
)


class Report:
    def __init__(self, strict: bool) -> None:
        self.strict = strict
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def migration_gap(self, message: str, approved: bool) -> None:
        if self.strict or not approved:
            self.error(message)
        else:
            self.warnings.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def print(self) -> None:
        for message in sorted(set(self.errors)):
            print(f"ERROR: {message}")
        for message in sorted(set(self.warnings)):
            print(f"WARNING: {message}")
        print(
            f"Validation completed: {len(set(self.errors))} error(s), "
            f"{len(set(self.warnings))} warning(s)."
        )


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def exact_path(root: Path, value: str) -> Path | None:
    """Resolve a root-relative POSIX path while checking exact filename case."""
    candidate = PurePosixPath(value)
    if candidate.is_absolute() or ".." in candidate.parts or "\\" in value:
        return None
    current = root
    try:
        for part in candidate.parts:
            names = {child.name for child in current.iterdir()}
            if part not in names:
                return None
            current = current / part
    except (FileNotFoundError, NotADirectoryError, OSError):
        return None
    return current if current.exists() else None


def load_yaml(path: Path, report: Report) -> Any | None:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        report.error(f"{path.name}: YAML parsing failed: {exc}")
        return None


def front_matter(path: Path, report: Report) -> dict[str, Any] | None:
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.error(f"{path}: cannot read UTF-8 content: {exc}")
        return None
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end < 0:
        report.error(f"{path}: YAML front matter has no closing delimiter")
        return None
    try:
        metadata = yaml.safe_load(content[4:end])
    except yaml.YAMLError as exc:
        report.error(f"{path}: front matter is invalid YAML: {exc}")
        return None
    if not isinstance(metadata, dict):
        report.error(f"{path}: front matter must be a YAML mapping")
        return None
    return metadata


def schema_message(error: Any) -> str:
    location = ".".join(str(part) for part in error.absolute_path)
    return f"{location}: {error.message}" if location else error.message


def check_machine_index(index: Any, root: Path, report: Report) -> dict[str, Any]:
    if not isinstance(index, dict):
        report.error("Repository_Index.yaml: root must be a YAML mapping")
        return {}

    required = {
        "schema_version": index.get("schema_version"),
        "project.id": (index.get("project") or {}).get("id"),
        "project.name": (index.get("project") or {}).get("name"),
        "artifact.id": (index.get("artifact") or {}).get("id"),
        "artifact.title": (index.get("artifact") or {}).get("title"),
        "artifact.type": (index.get("artifact") or {}).get("type"),
        "artifact.version": (index.get("artifact") or {}).get("version"),
        "artifact.status": (index.get("artifact") or {}).get("status"),
        "artifact.owner": (index.get("artifact") or {}).get("owner"),
        "artifact.maintenance": (index.get("artifact") or {}).get("maintenance"),
        "generation.generated_on": (index.get("generation") or {}).get("generated_on"),
    }
    for field, value in required.items():
        if value in (None, ""):
            report.error(f"Repository_Index.yaml: missing required field {field}")

    if index.get("schema_version") != "1.0.0":
        report.error("Repository_Index.yaml: schema_version must be 1.0.0")
    if (index.get("project") or {}).get("id") != "Orden":
        report.error("Repository_Index.yaml: project.id must be Orden")
    if (index.get("project") or {}).get("name") != "Behavior Change Review Framework":
        report.error("Repository_Index.yaml: project.name is not canonical")
    artifact = index.get("artifact") or {}
    if artifact.get("type") != "Machine Index":
        report.error("Repository_Index.yaml: artifact.type must be Machine Index")
    if artifact.get("status") != "Active":
        report.error("Repository_Index.yaml: artifact.status must be Active")
    if artifact.get("maintenance") != "Generated":
        report.error("Repository_Index.yaml: artifact.maintenance must be Generated")
    if "source_commit" in json.dumps(index, default=str):
        report.error("Repository_Index.yaml: source_commit is prohibited")

    documents = index.get("documents")
    if not isinstance(documents, list):
        report.error("Repository_Index.yaml: documents must be a list")
        return {}

    by_path: dict[str, Any] = {}
    for number, item in enumerate(documents, 1):
        if not isinstance(item, dict) or not isinstance(item.get("path"), str):
            report.error(f"Repository_Index.yaml: documents item {number} has no path")
            continue
        path = item["path"]
        if path in by_path:
            report.error(f"Repository_Index.yaml: duplicate documents.path {path}")
        by_path[path] = item
        if exact_path(root, path) is None:
            report.error(f"Repository_Index.yaml: documents.path does not resolve exactly: {path}")

    for section in ("non_markdown_artifacts",):
        for item in index.get(section) or []:
            path = item.get("path") if isinstance(item, dict) else None
            if not isinstance(path, str) or exact_path(root, path) is None:
                report.error(f"Repository_Index.yaml: invalid {section} path: {path}")

    for key in ("startup_context",):
        for path in (index.get("retrieval_policy") or {}).get(key) or []:
            if exact_path(root, path) is None:
                report.error(f"Repository_Index.yaml: {key} path does not resolve: {path}")

    validation = index.get("metadata_validation") or {}
    for key in ("schema", "validator", "requirements"):
        path = validation.get(key)
        if not isinstance(path, str) or exact_path(root, path) is None:
            report.error(f"Repository_Index.yaml: metadata_validation.{key} is invalid: {path}")
    backlog = validation.get("migration_backlog")
    if not isinstance(backlog, list) or len(backlog) != len(set(backlog)):
        report.error("Repository_Index.yaml: metadata_validation.migration_backlog must be a unique list")
    else:
        for path in backlog:
            if not isinstance(path, str) or exact_path(root, path) is None:
                report.error(f"Repository_Index.yaml: invalid migration backlog path: {path}")

    for route in index.get("query_routes") or []:
        intent = route.get("intent", "<unknown>")
        for key in ("retrieve", "then", "optional_history"):
            for path in route.get(key) or []:
                if exact_path(root, path) is None:
                    report.error(f"Repository_Index.yaml: route {intent} has invalid {key} path {path}")

    for item in index.get("planned_or_missing_documents") or []:
        path = item.get("path") if isinstance(item, dict) else None
        if isinstance(path, str) and exact_path(root, path) is not None:
            report.error(f"Repository_Index.yaml: planned artifact already exists: {path}")

    archive_files = [relative(path, root) for path in (root / "Archive").rglob("*") if path.is_file()]
    for family in index.get("archive_families") or []:
        pattern = family.get("path_pattern") if isinstance(family, dict) else None
        if not isinstance(pattern, str) or not any(fnmatch.fnmatch(path, pattern) for path in archive_files):
            report.error(f"Repository_Index.yaml: archive pattern has no match: {pattern}")
        replacements = family.get("current_replacements", family.get("current_replacement"))
        if replacements is None:
            continue
        if isinstance(replacements, str):
            replacements = [replacements]
        for path in replacements:
            if exact_path(root, path) is None:
                report.error(f"Repository_Index.yaml: archive replacement does not resolve: {path}")

    return by_path


def check_cycles(graph: dict[str, list[str]], report: Report) -> None:
    complete: set[str] = set()
    active: list[str] = []

    def visit(node: str) -> None:
        if node in active:
            cycle = " -> ".join(active[active.index(node) :] + [node])
            report.error(f"dependency cycle: {cycle}")
            return
        if node in complete:
            return
        active.append(node)
        for dependency in graph.get(node, []):
            if dependency in graph:
                visit(dependency)
        active.pop()
        complete.add(node)

    for node in graph:
        visit(node)


def validate(root: Path, strict: bool) -> Report:
    report = Report(strict)
    schema_path = root / "Schemas" / "Repository_Document_Metadata.schema.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, SchemaError) as exc:
        report.error(f"metadata schema cannot be loaded: {exc}")
        return report
    validator = Draft202012Validator(schema)

    index = load_yaml(root / "Repository_Index.yaml", report)
    indexed = check_machine_index(index, root, report) if index is not None else {}
    migration_backlog = set(
        ((index or {}).get("metadata_validation") or {}).get("migration_backlog") or []
    )
    observed_gaps: set[str] = set()

    normalized: dict[str, dict[str, Any]] = {}
    ids: defaultdict[str, list[str]] = defaultdict(list)
    graph: dict[str, list[str]] = {}

    markdown_files = sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and "Archive" not in path.parts
    )
    for path in markdown_files:
        name = relative(path, root)
        metadata = front_matter(path, report)

        if name in ENTRYPOINTS:
            if metadata is not None:
                report.error(f"{name}: repository entrypoint must not use front matter")
            entry = indexed.get(name)
            if not entry or entry.get("profile") != "repository_entrypoint":
                report.error(f"{name}: entrypoint profile is missing from Repository_Index.yaml")
            continue

        if metadata is None:
            observed_gaps.add(name)
            report.migration_gap(
                f"{name}: active Markdown artifact has no schema 1.0 front matter",
                name in migration_backlog,
            )
            continue
        if metadata.get("metadata_schema") != "1.0":
            observed_gaps.add(name)
            report.migration_gap(
                f"{name}: legacy front matter is not metadata schema 1.0",
                name in migration_backlog,
            )
            continue

        normalized[name] = metadata
        errors = sorted(validator.iter_errors(metadata), key=lambda error: list(error.absolute_path))
        for error in errors:
            report.error(f"{name}: {schema_message(error)}")

        document = metadata.get("document") or {}
        classification = metadata.get("classification") or {}
        document_id = document.get("id")
        if isinstance(document_id, str):
            ids[document_id].append(name)

        entry = indexed.get(name)
        if entry is None:
            report.error(f"{name}: normalized active document is absent from Repository_Index.yaml")
        else:
            expected = {
                "document_id": document_id,
                "version": document.get("version"),
                "status": str(document.get("status", "")).lower(),
                "maturity": str(classification.get("maturity", "")).lower(),
            }
            for key, value in expected.items():
                if entry.get(key) != value:
                    report.error(
                        f"{name}: index {key} is {entry.get(key)!r}; expected {value!r}"
                    )
            if entry.get("authority") == "normative" and "audience" not in metadata:
                report.error(f"{name}: normative document requires audience metadata")
            if (
                entry.get("authority") == "normative"
                or entry.get("category") in {"core_research", "framework", "empirical_study"}
            ) and "quality" not in metadata:
                report.error(f"{name}: profile requires quality metadata")

        dependencies: list[str] = []
        for key in RELATIONSHIP_KEYS:
            values = metadata.get(key) or []
            if not isinstance(values, list):
                continue
            for value in values:
                if not isinstance(value, str) or exact_path(root, value) is None:
                    report.error(f"{name}: {key} path does not resolve exactly: {value}")
            if key == "depends_on":
                dependencies = [value for value in values if isinstance(value, str)]
        graph[name] = dependencies

    for document_id, paths in ids.items():
        if len(paths) > 1:
            report.error(f"duplicate document ID {document_id}: {', '.join(sorted(paths))}")

    for name in sorted(migration_backlog - observed_gaps):
        report.error(f"Repository_Index.yaml: stale migration backlog entry: {name}")

    check_cycles(graph, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Orden metadata, relationships, and Repository_Index.yaml."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root; defaults to the parent of Scripts/.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat active legacy Markdown artifacts as errors instead of migration warnings.",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    report = validate(root, args.strict)
    report.print()
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
