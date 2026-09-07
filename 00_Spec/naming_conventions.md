---
id: naming_conventions
type: Spec
preferred_name: Naming and Linking Conventions Spec
aliases: [naming conventions, linking conventions, style guide]
short_definition: "Conventions governing file naming, page titles, aliases, and wikilink syntax in the Obsidian vault."
relationships:
  governs: [vault_spec]
  contains: []
  connects_to: []
confidence: high
review_status: active_spec
relationship_count: 4
hub_score: 11
centrality: 0.036
updated: 2026-07-08
---

# Naming and Linking Conventions

## 1. File Names and Directory Structure
- All Markdown filenames must use `lower_snake_case`.
  - *Correct:* `superficial_back_line.md`, `ground_reaction_force.md`
  - *Incorrect:* `Superficial Back Line.md`, `Ground-Reaction-Force.md`
- Subdirectories are organized by numbers to define clear conceptual domains:
  - `00_Spec/`: System specifications, standards, and literature/evidence sources.
  - `01_Fascial_Lines/`: Anatomy Trains myofascial lines.
  - `02_Body_Structures/`: Physical anatomical nodes (muscles, joints, connective tissues, joint actions).
  - `03_Movement_Functions/`: Force, torque, biomechanics, sequencing, and movement patterns.
  - `04_Golf_Swing/`: Golf swing analysis, overview, and phases.
  - `05_App_Logic/`: Metrics definitions, assessments, and exercises.

## 2. Page Titles (H1 Headings)
- The main heading (H1) at the top of each note should be in **Sentence Case** or **Proper Title Case** and match the `preferred_name` metadata field.
  - *Correct:* `# Superficial Back Line`, `# Ground Reaction Force`

## 3. Frontmatter Metadata
- Every note must start with a YAML frontmatter block containing:
  - `id`: The unique lower_snake_case identifier.
  - `type`: Node type (e.g., `Fascial Line`, `Muscle`, `Joint`, `Joint Action`, `Connective Structure`, `Movement Pattern`, `Golf Phase`, `Evidence Source`, `App Logic`, `Spec`).
  - `preferred_name`: The human-readable title.
  - `aliases`: An array of common aliases.
  - `relationships`: A mapping of parent/child/related connections.
  - `hub_score` / `relationship_count` / `centrality`: Computed metrics updated by `update_graph_metrics.py`.
  - `confidence`: `high`, `medium`, or `low`.
  - `review_status`: Review status string.
  - `updated`: Date in `YYYY-MM-DD` format.

### 3.1 Anatomical Structure Metadata Standards (Muscles & Connective Structures)
For physical anatomical nodes (`Muscle`, `Connective Structure`), the frontmatter should include:
- `origin`: Array of proximal bony or fascial attachment points.
- `insertion`: Array of distal bony or fascial attachment points.
- `innervation`: Nerve supply and spinal roots (e.g., `Femoral nerve (L2-L4)`).
- `fma_id`: Foundational Model of Anatomy ontology identifier (e.g., `FMA:22442`).
- `bodyparts3d_id`: BodyParts3D 3D polygon mesh ID for `motionflow_anatomy_studio` 3D rendering.
- `openstax_ref`: Standard reference to OpenStax Anatomy and Physiology 2e chapter/section.

## 4. Wikilink Conventions
- Always use double-bracket links to create connections between notes: ``target_node_id``.
- To render custom link text, use the pipe syntax: `[[rectus_abdominis|Rectus Abdominis]]`.
  - *Correct:* "The [[gluteus_maximus]] is part of the [[superficial_back_line|Superficial Back Line]]."
- Do not use markdown links (e.g., `[text](file.md)`) for internal vault links, except when linking to raw PDFs or external URLs.
- In frontmatter, do not wrap relationships in double brackets; use plain strings corresponding to the node's `id`.
  - *Correct in YAML:* `connects_to: [plantar_fascia, gluteus_maximus]`
  - *Incorrect in YAML:* `connects_to: [\[\[plantar_fascia\]\], \[\[gluteus_maximus\]\]]`
