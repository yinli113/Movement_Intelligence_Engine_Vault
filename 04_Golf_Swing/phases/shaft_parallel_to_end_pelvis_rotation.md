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
  supported_by: [golf_decoded_six_phases_swing, dr_kwon_golfer_ground_interaction]
  relevant_to: [golfer_ground_interaction_model, ground_reaction_force, center_of_mass, moment_arm, hip_joint, lateral_line, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 19
hub_score: 43
centrality: 0.388
updated: 2026-07-16
---

# Shaft Parallel to End Pelvis Rotation

## Definition

Shaft Parallel to End Pelvis Rotation is the second phase interval in the source model.

## Why It Matters

It separates early club movement from pelvis rotation timing, which helps the graph reason about lower-body contribution during the backswing.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the second interval as Shaft Parallel -> End Pelvis Rotation.

## Source-Defined Boundary

This Level 4 vault phase begins at [[shaft_parallel_position]], which is not yet mapped to a Kwon event, and ends at [[end_pelvis_rotation]], which crosswalks to Kwon's EPR event. The event match does not make the whole interval equivalent to a Kwon phase.

## Golf Biomechanics (Level 3)

EPR can provide a source-defined timing anchor for instrumented analysis. In the [[golfer_ground_interaction_model]], any moment of [[ground_reaction_force|GRF]] about [[center_of_mass|COM]] requires the measured force vector and [[moment_arm|line-of-action geometry]]; visible pelvis rotation does not establish that moment or its direction.

## Myofascial-Line Interpretation

The [[spiral_line]], [[lateral_line]] and [[functional_lines]] are the primary anatomical pathways for a separate vault interpretation of rotational organisation. Kwon does not establish myofascial-line loading or tissue-specific force transfer in this phase.

## App Observability (Level 5)

**Camera-observable:** shaft-parallel and EPR timing may be estimated from visible club and pelvis kinematics under declared view and frame-rate limits. **Unavailable from ordinary video:** ordinary video cannot measure force, moment, moment arm or tissue state. **Hypothesised:** line loading and kinetic effectiveness remain Level 5 interpretations.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[shaft_parallel_position]] |
| ends_at | [[end_pelvis_rotation]] |
| follows | [[address_to_shaft_parallel]] |
| precedes | [[end_pelvis_rotation_to_top_backswing]] |
| relevant_to | [[hip_joint]], [[spiral_line]], [[lateral_line]] |
| relevant_to | [[golfer_ground_interaction_model]], [[ground_reaction_force]], [[center_of_mass]], [[moment_arm]] |

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
