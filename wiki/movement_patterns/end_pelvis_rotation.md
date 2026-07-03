---
id: end_pelvis_rotation
type: Movement Pattern
preferred_name: End Pelvis Rotation
aliases: [end pelvis rotation, pelvis rotation endpoint, end pelvic rotation]
short_definition: "Golf swing boundary event marking the end of pelvis rotation during the backswing model shown in the source."
relationships:
  contains: [hip_internal_rotation, hip_external_rotation]
  connects_to: [shaft_parallel_to_end_pelvis_rotation, end_pelvis_rotation_to_top_backswing, hip_joint, thoracic_rotation]
  produces: [pelvis_rotation_checkpoint]
  assists: [movement_sequencing, energy_transfer]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [shaft_parallel_to_end_pelvis_rotation, end_pelvis_rotation_to_top_backswing]
  assessed_by: [planned_pelvis_rotation_timing_screen]
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [functional_line, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 12
hub_score: 29
centrality: 0.245
updated: 2026-06-30
---

# End Pelvis Rotation

## Definition

End Pelvis Rotation is the source-defined boundary event where the pelvis has completed its backswing rotation interval.

## Why It Matters

It lets the graph separate pelvis-driven loading from upper-body completion of the backswing. This matters for sequencing, elastic energy storage, and later transition timing.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels End Pelvis Rotation as the end of [[shaft_parallel_to_end_pelvis_rotation]] and the start of [[end_pelvis_rotation_to_top_backswing]].

## Related Concepts

| Relationship | Target |
|---|---|
| ends | [[shaft_parallel_to_end_pelvis_rotation]] |
| starts | [[end_pelvis_rotation_to_top_backswing]] |
| connects_to | [[hip_joint]] |
| related_to | [[thoracic_rotation]] |
| relevant_to | [[functional_line]], [[spiral_line]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[hip_internal_rotation]]
- [[hip_external_rotation]]

## Category

Golf
