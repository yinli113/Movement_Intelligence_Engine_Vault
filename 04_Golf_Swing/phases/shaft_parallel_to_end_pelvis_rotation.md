---
id: shaft_parallel_to_end_pelvis_rotation
type: Golf Phase
preferred_name: Shaft Parallel to End Pelvis Rotation
aliases: [phase 2, early backswing pelvis rotation interval]
short_definition: "Second source-defined golf swing phase interval from Shaft Parallel to End Pelvis Rotation."
relationships:
  contains: [shaft_parallel_position, end_pelvis_rotation, hip_internal_rotation, hip_external_rotation]
  connects_to: [address_to_shaft_parallel, end_pelvis_rotation_to_top_backswing, golf_swing]
  produces: [pelvis_rotation_checkpoint]
  assists: [movement_sequencing, energy_transfer]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_pelvis_rotation_timing_screen]
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [hip_joint, lateral_line, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 13
hub_score: 34
centrality: 0.26
updated: 2026-06-30
---

# Shaft Parallel to End Pelvis Rotation

## Definition

Shaft Parallel to End Pelvis Rotation is the second phase interval in the source model.

## Why It Matters

It separates early club movement from pelvis rotation timing, which helps the graph reason about lower-body contribution during the backswing.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the second interval as Shaft Parallel -> End Pelvis Rotation.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[shaft_parallel_position]] |
| ends_at | [[end_pelvis_rotation]] |
| follows | [[address_to_shaft_parallel]] |
| precedes | [[end_pelvis_rotation_to_top_backswing]] |
| relevant_to | [[hip_joint]], [[spiral_line]], [[lateral_line]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[shaft_parallel_position]]
- [[end_pelvis_rotation]]
- [[hip_internal_rotation]]
- [[hip_external_rotation]]

## Category

Movement Phase
