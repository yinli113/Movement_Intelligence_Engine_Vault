---
id: end_pelvis_rotation_to_top_backswing
type: Golf Phase
preferred_name: End Pelvis Rotation to Top Backswing
aliases: [phase 3, late backswing, pelvis stopped to top backswing]
short_definition: "Third source-defined golf swing phase interval from End Pelvis Rotation to Top Backswing."
relationships:
  contains: [end_pelvis_rotation, top_backswing_position, thoracic_rotation, trail_shoulder_external_rotation]
  connects_to: [shaft_parallel_to_end_pelvis_rotation, golf_swing_transition, golf_swing]
  produces: [backswing_loaded_state]
  assists: [energy_transfer]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_top_backswing_load_screen]
  improved_by: [planned_thoracic_rotation_breath_drill]
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [functional_line, spiral_line, neck_tension, jaw_clenching]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 14
hub_score: 41
centrality: 0.286
updated: 2026-06-30
---

# End Pelvis Rotation to Top Backswing

## Definition

End Pelvis Rotation to Top Backswing is the third phase interval in the source model.

## Why It Matters

It lets the graph reason about continued upper-body loading after pelvis rotation reaches its endpoint.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the third interval as End Pelvis Rotation -> Top of Backswing.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[end_pelvis_rotation]] |
| ends_at | [[top_backswing_position]] |
| follows | [[shaft_parallel_to_end_pelvis_rotation]] |
| precedes | [[golf_swing_transition]] |
| relevant_to | [[thoracic_rotation]], [[trail_shoulder_external_rotation]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[end_pelvis_rotation]]
- [[top_backswing_position]]
- [[thoracic_rotation]]
- [[trail_shoulder_external_rotation]]

## Category

Movement Phase
