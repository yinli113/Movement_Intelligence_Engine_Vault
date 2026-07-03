#!/usr/bin/env python3
"""Update lightweight graph metrics in wiki node frontmatter.

The vault is still Markdown-first, so this script computes metrics from:
- frontmatter relationship lists
- Obsidian body links
- inbound links from other node notes

It intentionally avoids a database. Hub Score is a prioritization heuristic,
not a clinical score.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SKIP_DIRS = {"templates"}
METRIC_KEYS = {"relationship_count", "hub_score", "centrality"}
DEFAULT_CONFIDENCE = "medium"
DEFAULT_REVIEW_STATUS = "generated_legacy_needs_review"

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
ID_RE = re.compile(r"^id:\s*(.+?)\s*$", re.MULTILINE)
TYPE_RE = re.compile(r"^type:\s*(.+?)\s*$", re.MULTILINE)
REL_BLOCK_RE = re.compile(r"^relationships:\s*\n(?P<body>(?:\s{2}.+\n?)*)", re.MULTILINE)
LIST_VALUE_RE = re.compile(r"\[([^\]]*)\]")


@dataclass
class Node:
    path: Path
    stem: str
    node_id: str
    node_type: str
    frontmatter: str
    body: str
    out_refs: set[str] = field(default_factory=set)
    in_refs: set[str] = field(default_factory=set)
    metrics: dict[str, float | int] = field(default_factory=dict)


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1].strip("\n"), parts[2].lstrip("\n")


def clean_scalar(value: str) -> str:
    return value.strip().strip('"').strip("'")


def parse_node(path: Path) -> Node | None:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        return None

    id_match = ID_RE.search(frontmatter)
    type_match = TYPE_RE.search(frontmatter)
    node_id = clean_scalar(id_match.group(1)) if id_match else path.stem
    node_type = clean_scalar(type_match.group(1)) if type_match else "Unknown"

    return Node(
        path=path,
        stem=path.stem,
        node_id=node_id,
        node_type=node_type,
        frontmatter=frontmatter,
        body=body,
    )


def parse_relationship_refs(frontmatter: str) -> set[str]:
    refs: set[str] = set()
    block_match = REL_BLOCK_RE.search(frontmatter)
    if not block_match:
        return refs

    for line in block_match.group("body").splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        value = line.split(":", 1)[1].strip()
        list_match = LIST_VALUE_RE.search(value)
        if list_match:
            values = list_match.group(1).split(",")
        elif value:
            values = [value]
        else:
            values = []
        for item in values:
            item = clean_scalar(item)
            if item:
                refs.add(item)
    return refs


def node_files() -> list[Path]:
    paths: list[Path] = []
    for path in WIKI.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(WIKI).parts):
            continue
        if path.name in {"index.md", "log.md"}:
            continue
        paths.append(path)
    return sorted(paths)


def compute_metrics(nodes: dict[str, Node]) -> None:
    aliases: dict[str, str] = {}
    for node in nodes.values():
        aliases[node.stem] = node.node_id
        aliases[node.node_id] = node.node_id

    for node in nodes.values():
        refs = parse_relationship_refs(node.frontmatter)
        refs.update(clean_scalar(m.group(1)) for m in LINK_RE.finditer(node.body))
        node.out_refs = {aliases[ref] for ref in refs if ref in aliases and aliases[ref] != node.node_id}

    for node in nodes.values():
        for ref in node.out_refs:
            nodes[ref].in_refs.add(node.node_id)

    max_degree = max((len(n.out_refs | n.in_refs) for n in nodes.values()), default=1)
    fascial = {n.node_id for n in nodes.values() if n.node_type in {"Fascial Line", "line"}}
    muscles = {n.node_id for n in nodes.values() if n.node_type == "muscle" or n.node_type == "Muscle"}
    phases = {n.node_id for n in nodes.values() if n.node_type in {"Golf Phase", "phase", "movement"}}
    assessments = {n.node_id for n in nodes.values() if n.node_type in {"Assessment", "assessment"}}
    limitations = {n.node_id for n in nodes.values() if n.node_type in {"Limitation Pattern", "Compensation"}}

    for node in nodes.values():
        neighbors = node.out_refs | node.in_refs
        relationship_count = len(neighbors)
        fascial_count = len(neighbors & fascial)
        muscle_count = len(neighbors & muscles)
        phase_count = len(neighbors & phases)
        assessment_count = len(neighbors & assessments)
        limitation_count = len(neighbors & limitations)
        inbound_bonus = len(node.in_refs)

        hub_score = (
            relationship_count
            + inbound_bonus
            + 3 * fascial_count
            + 2 * muscle_count
            + 4 * phase_count
            + 3 * assessment_count
            + 3 * limitation_count
        )
        centrality = round(relationship_count / max_degree, 3) if max_degree else 0.0
        node.metrics = {
            "relationship_count": relationship_count,
            "hub_score": hub_score,
            "centrality": centrality,
        }


def update_frontmatter(node: Node) -> None:
    lines = node.frontmatter.splitlines()
    preserved: list[str] = []
    has_confidence = False
    has_review_status = False

    for line in lines:
        key = line.split(":", 1)[0].strip() if ":" in line else ""
        if key in METRIC_KEYS:
            continue
        if key == "confidence":
            has_confidence = True
        if key == "review_status":
            has_review_status = True
        preserved.append(line)

    insert_at = len(preserved)
    for idx, line in enumerate(preserved):
        if line.startswith("updated:"):
            insert_at = idx
            break

    metric_lines = [
        f"relationship_count: {int(node.metrics['relationship_count'])}",
        f"hub_score: {int(node.metrics['hub_score'])}",
        f"centrality: {node.metrics['centrality']}",
    ]
    if not has_confidence:
        metric_lines.append(f"confidence: {DEFAULT_CONFIDENCE}")
    if not has_review_status:
        metric_lines.append(f"review_status: {DEFAULT_REVIEW_STATUS}")

    new_lines = preserved[:insert_at] + metric_lines + preserved[insert_at:]
    new_text = "---\n" + "\n".join(new_lines).rstrip() + "\n---\n\n" + node.body.lstrip("\n")
    node.path.write_text(new_text, encoding="utf-8")


def main() -> None:
    nodes_by_id: dict[str, Node] = {}
    for path in node_files():
        node = parse_node(path)
        if node is None:
            continue
        nodes_by_id[node.node_id] = node

    compute_metrics(nodes_by_id)

    for node in nodes_by_id.values():
        update_frontmatter(node)

    print(f"updated_nodes={len(nodes_by_id)}")
    print("top_hubs=")
    for node in sorted(nodes_by_id.values(), key=lambda n: int(n.metrics["hub_score"]), reverse=True)[:20]:
        rel = node.path.relative_to(ROOT).as_posix()
        print(f"{int(node.metrics['hub_score']):>3} {int(node.metrics['relationship_count']):>3} {node.node_id} {node.node_type} {rel}")


if __name__ == "__main__":
    main()
