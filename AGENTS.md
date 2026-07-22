# Myofascial Lines LLM-Wiki Schema & Guidelines

This document defines the structure, metadata conventions, and workflows for maintaining the Myofascial Lines Obsidian vault. All updates, additions, and analyses must adhere to this schema.

Before major graph changes, read `00_Spec/spec.md`. That file is the controlling project specification for evidence hierarchy, fascial-line-first reasoning, golf interpretation boundaries, and app-readiness requirements.

> **Cross-repo consistency (read first):** This vault is the knowledge source-of-truth for the whole TillYes workspace. When you change a canonical fact here (evidence hierarchy in `00_Spec/evidence_levels.md`, vault scope in `index.md`, source-note ids/filenames, or the location of `fascial_knowledge.json`), the same fact is duplicated in `tillyes_doc`, `tillyes_web`, `tillyes_apps/*`, and the workspace-root docs — and those copies must be updated in the same session. Before and after editing, read `../../AGENTS.md` and `../../CONSISTENCY_MAP.md`, then run `../../scripts/check_consistency.sh`. This vault's `id == filename` convention applies to **new** source notes; the legacy `anatomy_trains_myofascial_thomas_w_myers` note uses `id: anatomy_trains_myers_2009` (citation slug used as `source_id` in evidence blocks) — see `../../CONSISTENCY_MAP.md` §3.

---

## 1. Directory Structure

- **`raw/`** (Immutable User Uploads)
  - `literature/`: PDF articles, textbook screenshots, or text clips regarding anatomy and biomechanics.
  - `movements/`: Log entries, video frames, posture photos, or text descriptions of captured movement sessions.
- **`wiki/`** (Persistent LLM-Compiled Knowledge)
  - `movements/`: Overall movement patterns (e.g., `golf_swing.md`) and their phases.
  - `golf_phases/`: Source-defined golf swing phase intervals.
  - `movement_patterns/`: Reusable movement, motor-control, biomechanics, physics, and sport-context concepts.
  - `lines/`: Myofascial lines (e.g., `superficial_back_line.md`).
  - `connective_structures/`: First-class connective tissue nodes involved in force transmission (e.g., `thoracolumbar_fascia.md`).
  - `joints/`: Physical joint notes (e.g., `hip_joint.md`).
  - `mechanics/`: Joint kinematics, biomechanics, and compensations (e.g., `hip_rotation.md`).
  - `muscles/`: Individual muscle cards (e.g., `gluteus_maximus.md`).
  - `assessments/`: Movement capture reports, mechanical inferences, and test protocols.
  - `interventions/`: Mobilizations, releases, activations, and functional integrations.
  - `sources/`: Structured summaries of files in `raw/` with back-links.

---

## 2. Document Naming & Linking Conventions

1. **File Names**: Use `snake_case` or `lower_spaced_case` for filenames, but keep titles human-readable.
2. **Obsidian Links**: Always use double-bracket page links for referencing other pages.
   - Example: "The gluteus maximus is part of the `[[superficial_back_line]]`..."
3. **No Orphans**: Every new page must be linked from `wiki/index.md` and at least one other relevant page.
4. **Multidirectional Graph Traversal**: Ensure files link hierarchically and laterally:
   `Movement` -> `Phase` -> `Joint` -> `Line` -> `Muscle` -> `Actions (Releases/Activations/Tests)`.

---

## 3. Metadata Standards (YAML Frontmatter)

Every wiki page must begin with a YAML block specifying its type and relationships. Do not use double brackets inside YAML lists; use simple text strings or single brackets if referencing paths.

### Graph Philosophy

The vault is a movement intelligence graph, not an anatomy notebook. Prioritize relationships over isolated facts. Prefer linking concepts through force transmission, energy transfer, movement sequencing, motor control, external forces, connective structures, joints, muscles, fascial lines, compensations, assessments, and exercises.

When converting a source:

1. Create reusable concept nodes instead of long summaries.
2. Merge new information into existing nodes when possible.
3. Add explicit relationship tables using wiki links.
4. Classify concepts by category: Anatomy, Muscle, Joint, Bone, Ligament, Fascia, Fascial Line, Movement Phase, Movement Pattern, Biomechanics, Physics, Motor Control, Rehabilitation, or Golf.
5. Mark inferred relationships with appropriate confidence.

### Primary Node Types

- Fascial Line
- Muscle
- Connective Structure
- Joint
- Joint Action
- Golf Phase
- Movement Pattern
- Limitation Pattern
- Compensation
- Assessment
- Exercise
- Evidence Source

### Graph Metrics

Every graph node should maintain:

```yaml
relationship_count: 0
hub_score: 0
centrality: 0.0
confidence: medium
review_status: draft
```

Hub Score is a prioritization metric for movement reasoning. Increase it when a node has many relationships, connects multiple fascial lines, attaches to multiple muscles, influences golf phases, appears in assessments, or participates in limitation patterns.

### Movement Page
```yaml
---
type: movement
phases: [golf_swing_transition]
sports: [Golf]
updated: 2026-06-27
---
```

### Phase Page
```yaml
---
type: phase
parent_movement: golf_swing
key_mechanics: [hip_rotation, thoracic_rotation]
updated: 2026-06-27
---
```

### Myofascial Line Page (in `wiki/lines/`)
```yaml
---
type: line
category: myofascial_line
key_muscles: [Gluteus Maximus, Hamstrings]
joints_crossed: [Ankle, Knee, Hip, Spine]
updated: 2026-06-27
---
```

### Connective Structure Page (in `wiki/connective_structures/`)
```yaml
---
id: thoracolumbar_fascia
type: Connective Structure
subtype: Fascia
preferred_name: Thoracolumbar Fascia
aliases: [lumbodorsal fascia]
short_definition: "Connective tissue structure involved in force transmission."
relationships:
  connects_to: [latissimus_dorsi, gluteus_maximus, sacrum, lumbar_spine]
  part_of: [functional_line]
  transmits_force_between: [upper_limb, pelvis]
  relevant_to: [golf_swing_transition]
relationship_count: 0
hub_score: 0
centrality: 0.0
confidence: medium
review_status: draft_graph_mvp
updated: 2026-06-29
---
```

### Joint Page (in `wiki/joints/`)
```yaml
---
type: joint
lines_crossing: [Superficial Back Line, Deep Front Line]
key_muscles: [Gluteus Maximus, Psoas Major, Adductors]
associated_mechanics: [hip_rotation]
updated: 2026-06-27
---
```

### Joint Mechanic / Compensation Page (in `wiki/mechanics/`)
```yaml
---
type: mechanic
joints_involved: [hip_joint]
compensations: [Knee Valgus, Foot Pronation]
associated_lines: [lateral_line, deep_front_line]
key_muscles: [gluteus_maximus]
updated: 2026-06-27
---
```

### Muscle Page (in `wiki/muscles/`)
```yaml
---
type: muscle
associated_lines: [functional_line, superficial_back_line]
joints_crossed: [hip_joint]
activations: [glute_max_activations]
releases: [glute_max_releases]
tests: [glute_max_tests]
updated: 2026-06-27
---
```

---

## 4. Key Workflows

### A. Source Ingestion Workflow
When a new file is added to `raw/literature/`:
1. Read the source file.
2. Create a summary in `wiki/sources/source_name.md`.
3. Extract key anatomy/biomechanics insights and integrate them into relevant files in `wiki/lines/`, `wiki/joints/`, or `wiki/muscles/`.
4. Update `wiki/index.md` and `wiki/log.md`.

### B. Movement Assessment Workflow
When a movement description or capture file is added to `raw/movements/`:
1. **Analyze Movement**: Identify key joint positions (e.g., restricted ankle dorsiflexion, hip shift).
2. **Infer Joint Mechanics**: Link joint positions to muscle states (e.g., overactive tensor fasciae latae, underactive gluteus medius).
3. **Map to Myofascial Lines**: Trace the chain of tension/slack along Anatomy Trains (e.g., restriction in the `[[deep_front_line]]` causing compensatory patterns in the `[[lateral_line]]`).
4. **Identify Weak Links**: Target the primary driver or "weak link" causing the issue.
5. **Recommend Interventions**: Recommend specific exercises or releases.
6. **Create Files**:
   - Create a page in `wiki/assessments/assessment_date.md` detailing the breakdown.
   - If not present, create/update relevant pages under `wiki/lines/`, `wiki/joints/`, `wiki/muscles/`, `wiki/mechanics/`, or `wiki/interventions/`.
7. **Log**: Record the assessment in `wiki/log.md` and update `wiki/index.md`.

### C. Wiki Maintenance & Linting Workflow
Periodically run a health check:
1. Search for broken links.
2. Find "orphan" notes (notes with no incoming links) and link them appropriately.
3. Identify contradictions (e.g., if one note suggests calf stretching for anterior tilt, and another advises against it, flag and resolve the biomechanical context).
