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
  supported_by: [golf_decoded_six_phases_swing, dr_kwon_golfer_ground_interaction]
  relevant_to: [golfer_ground_interaction_model, ground_reaction_force, moment_arm, center_of_mass, functional_lines, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 17
hub_score: 35
centrality: 0.153
updated: 2026-07-16
---

# End Pelvis Rotation

## Definition

End Pelvis Rotation is the source-defined boundary event where the pelvis has completed its backswing rotation interval.

## Why It Matters

It lets the graph separate what the historical vault called pelvis-driven loading from upper-body completion of the backswing. “Pelvis-driven loading” and “elastic energy storage” are historical/vault interpretation, not measurements available from ordinary video; the golf kinetics observability boundary permits only qualified geometry and timing descriptors without compatible kinetic or tissue-level instrumentation.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels End Pelvis Rotation as the end of [[shaft_parallel_to_end_pelvis_rotation]] and the start of [[end_pelvis_rotation_to_top_backswing]].

## Related Concepts

| Relationship | Target |
|---|---|
| ends | [[shaft_parallel_to_end_pelvis_rotation]] |
| starts | [[end_pelvis_rotation_to_top_backswing]] |
| connects_to | [[hip_joint]] |
| related_to | [[thoracic_rotation]] |
| relevant_to | [[functional_lines]], [[spiral_line]] |
| relevant_to | [[golfer_ground_interaction_model]], [[ground_reaction_force]], [[moment_arm]], [[center_of_mass]] |
| crosswalks_to | Kwon EPR event |

This is a kinematic timing boundary. Pelvis motion does not measure [[ground_reaction_force]] or the combined-GRF frontal-plane/F-B-axis moment about [[center_of_mass]]; that calculation requires measured GRF and [[moment_arm|line-of-action geometry]] within the [[golfer_ground_interaction_model]].

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[hip_internal_rotation]]
- [[hip_external_rotation]]

## Category

Golf
