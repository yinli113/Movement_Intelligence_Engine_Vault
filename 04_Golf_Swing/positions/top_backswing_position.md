---
id: top_backswing_position
type: Movement Pattern
preferred_name: Top Backswing Position
aliases: [top backswing, top of backswing]
short_definition: "Golf swing boundary event marking completion of the backswing interval before transition into unweighting."
relationships:
  contains: [thoracic_rotation, trail_shoulder_external_rotation]
  connects_to: [end_pelvis_rotation_to_top_backswing, golf_swing_transition, spiral_line, functional_lines]
  produces: [backswing_loaded_state]
  assists: [energy_transfer]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [end_pelvis_rotation_to_top_backswing, golf_swing_transition]
  assessed_by: [planned_top_backswing_load_screen]
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [neck_tension, jaw_clenching]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 11
hub_score: 35
centrality: 0.22
updated: 2026-06-30
---

# Top Backswing Position

## Definition

Top Backswing Position is the source-defined boundary between backswing completion and the transition interval represented in this vault by [[golf_swing_transition]].

## Why It Matters

It anchors the point where stored rotation, shoulder loading, neck bracing, and later force redirection must be interpreted as sequencing relationships.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels Top Backswing as the end of [[end_pelvis_rotation_to_top_backswing]] and the start of the interval merged into [[golf_swing_transition]].

## Related Concepts

| Relationship | Target |
|---|---|
| ends | [[end_pelvis_rotation_to_top_backswing]] |
| starts | [[golf_swing_transition]] |
| contains | [[thoracic_rotation]] |
| contains | [[trail_shoulder_external_rotation]] |
| possible_compensation | [[neck_tension]], [[jaw_clenching]] |

## Parent Concepts

- [[golf_swing]]

## Child Concepts

- [[thoracic_rotation]]
- [[trail_shoulder_external_rotation]]

## Category

Golf
