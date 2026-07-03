# Vault Audit and Graph Conversion Plan

## 1. Current Vault Problems

The vault has useful raw material, but it currently behaves more like a notebook than a reasoning graph.

- The dominant note shape is lecture-summary prose, not entity-relationship data.
- Existing node types are inconsistent with the product graph: `line`, `mechanic`, `phase`, and `intervention` are mixed with graph concepts like Fascial Line, Joint Action, Limitation Pattern, Compensation, Assessment, and Exercise.
- Many notes use wiki links inside YAML frontmatter, while `AGENTS.md` says frontmatter should use plain IDs.
- Evidence is mostly implicit. Notes often state anatomy or golf relevance without a structured `evidence` field.
- The vault contains generated anatomy coverage beyond the 2-week MVP scope, but the golf reasoning slice is still thin.
- The Thomas Myers PDF exists locally at `raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf`, but it has not yet been converted into a proper Evidence Source node.
- `wiki/sources/julie_hammond_breakout.md` links to `raw/literature/Julie Hammond Breakout.pdf` using an Obsidian link to a raw PDF; the file exists, but this should be normalized as evidence metadata rather than a graph entity link.
- `AGENTS.md` contains an example link written as an Obsidian page placeholder, which appears as a broken link during automated checks.

Current audit counts:

- Markdown notes: 113
- Type counts: 64 `muscle`, 20 `mechanic`, 10 `line`, 10 `joint`, 2 `intervention`, 1 `assessment`, 1 `movement`, 1 `phase`, 1 `source`
- Notes with wiki links inside YAML: 100
- Orphans found: 0
- Broken links found by markdown-only checker: `Page Name`, `raw/literature/Julie Hammond Breakout.pdf`

## 2. Duplicate or Inconsistent Terms

No exact duplicate H1/title terms were found, but the vocabulary is inconsistent enough to reduce AI reasoning quality.

- `line` should become canonical type `Fascial Line`.
- `mechanic` currently mixes Joint Action, Movement Pattern, Limitation Pattern, and Compensation.
- `phase` should become canonical type `Golf Phase`.
- `intervention` should split into `Exercise`, `Release`, or a more general future `Intervention` only if needed.
- `myofascial_line`, `Myofascial Line`, and `Fascial Line` should be normalized. Use `Fascial Line` as the product node type; use `Anatomy Trains fascial line model` in definitions when referencing Myers.
- `peroneus` and `fibularis` should be handled with aliases. Use current filenames for stability, but add aliases such as `fibularis_longus`.
- `golf_swing_transition`, `Golf Swing - Transition`, and `Golf Transition Phase` should normalize to preferred name `Golf Transition Phase` with ID `golf_swing_transition`.
- `shoulder_external_rotation` is a general Joint Action; `trail_shoulder_external_rotation` is a golf-specific Movement Pattern or Joint Action instance.
- Terms like `jaw_clenching`, `neck_tension`, and `toe_loading` should not be generic mechanics. They should become `Compensation` or `Limitation Pattern` nodes depending on role.

## 3. Proposed Canonical Naming Rules

- File IDs use `snake_case`: `deep_front_line`, `trail_shoulder_external_rotation`.
- `preferred_name` uses readable title case: `Deep Front Line`, `Trail Shoulder External Rotation`.
- Keep existing filenames when possible to avoid graph churn.
- Use `aliases` for clinical, coaching, and anatomy variants.
- Use node type names exactly:
  - `Fascial Line`
  - `Muscle`
  - `Joint`
  - `Joint Action`
  - `Golf Phase`
  - `Movement Pattern`
  - `Limitation Pattern`
  - `Compensation`
  - `Assessment`
  - `Exercise`
  - `Evidence Source`
- Use relationship predicates from the controlled set:
  - `contains`
  - `connects_to`
  - `produces`
  - `assists`
  - `stabilizes`
  - `limits`
  - `compensates_for`
  - `active_during`
  - `assessed_by`
  - `improved_by`
  - `supported_by`
  - `relevant_to`
- Use IDs in YAML relationship fields, and wiki links in the markdown body.
- Do not use `meridian` as a synonym for fascial lines in product graph labels. If discussing Myers' source terminology, store it as source terminology only.

## 4. Proposed Folder Structure

Keep the current vault readable, but introduce graph-oriented folders gradually.

```text
00_Project_Reports/
wiki/
  fascial_lines/
  muscles/
  joints/
  joint_actions/
  golf_phases/
  movement_patterns/
  limitation_patterns/
  compensations/
  assessments/
  exercises/
  evidence_sources/
raw/
  literature/
  movements/
```

MVP migration rule: do not move files immediately. First normalize frontmatter and relationships in place. Move folders only after the top MVP graph slice is stable.

## 5. Proposed Note Template

```yaml
---
id: node_id
type: Fascial Line
preferred_name: Human Name
aliases: []
short_definition: "One sentence definition."
relationships:
  contains: []
  connects_to: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: []
  improved_by: []
  supported_by: []
  relevant_to: []
golf_relevance: "One or two sentences on why this matters for golf movement reasoning."
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "chapter/page/section"
    supports: "Specific relationship or definition."
confidence: medium
review_status: draft_graph_mvp
updated: 2026-06-29
---
```

Markdown body:

- `## Relationships` with predicate bullets using wiki links.
- `## Golf Reasoning` with concise graph traversal logic.
- `## Evidence Notes` with source caveats.
- `## Open Questions` for claims needing review.

## 6. Top 20 MVP Nodes for Golf

1. `golf_swing`
2. `golf_swing_transition`
3. `toe_loading`
4. `lead_hip_internal_rotation`
5. `hip_internal_rotation`
6. `thoracic_rotation`
7. `trail_shoulder_external_rotation`
8. `jaw_clenching`
9. `neck_tension`
10. `deep_front_line`
11. `lateral_line`
12. `functional_line`
13. `spiral_line`
14. `superficial_back_line`
15. `hip_joint`
16. `thoracic_spine`
17. `shoulder_joint`
18. `ankle_joint`
19. `gluteus_maximus`
20. `latissimus_dorsi`

## 7. Top 10 Limitation Patterns

1. Loss of lead toe loading
2. Limited lead hip internal rotation
3. Pelvic sway during transition
4. Restricted thoracic rotation
5. Trail shoulder over-bracing
6. Neck tension during transition
7. Jaw clenching during load or impact preparation
8. Foot pronation collapse under pressure
9. Early arm throw from poor trunk transfer
10. Lumbar twist substituting for thoracic rotation

## 8. Step-by-Step Conversion Plan

1. Freeze bulk generation. Do not add more anatomy notes until the MVP graph behavior works.
2. Create Evidence Source nodes for the Myers PDF, Julie Hammond PDF, and selected standard anatomy references.
3. Normalize the 10 sample notes first using the graph template.
4. Convert existing line notes from `line` to `Fascial Line`; keep Myers as the primary source for fascial-line relationships.
5. Convert existing mechanics into either `Joint Action`, `Movement Pattern`, `Limitation Pattern`, or `Compensation`.
6. Convert only golf-relevant muscles first: gluteus maximus, latissimus dorsi, psoas major, diaphragm, masseter, temporalis, scalenes, sternocleidomastoid, infraspinatus, teres minor, peroneus longus, flexor hallucis longus.
7. Add minimal Assessment nodes only where they close a reasoning loop.
8. Add minimal Exercise nodes only when linked from a limitation and supported by reasonable movement rationale.
9. Run a link and relationship audit after each batch of 10-20 notes.
10. Only after the reasoning graph is stable, consider MediaPipe-derived observations as evidence inputs.
