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
  supported_by: [golf_decoded_six_phases_swing, dr_kwon_golfer_ground_interaction]
  relevant_to: [golfer_ground_interaction_model, ground_reaction_force, moment_arm, center_of_mass, functional_lines, spiral_line, neck_tension, jaw_clenching]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 28
hub_score: 90
centrality: 0.483
updated: 2026-07-16
---

# End Pelvis Rotation to Top Backswing

## Definition

End Pelvis Rotation to Top Backswing is the third phase interval in the source model.

## Why It Matters

It lets the graph reason about continued upper-body loading after pelvis rotation reaches its endpoint.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the third interval as End Pelvis Rotation -> Top of Backswing.

## Source-Defined Boundary

This Level 4 vault phase runs from [[end_pelvis_rotation|EPR]] to [[top_backswing_position|TB]], both supported Kwon event matches. Kwon's extended-downswing convention begins at EPR, whereas this vault preserves the source-defined EPR-to-TB interval; the event crosswalk therefore does not claim phase equivalence.

## Golf Biomechanics (Level 3)

The EPR and TB events can bound timing comparisons when their operational definitions are applied consistently. The [[golfer_ground_interaction_model]] permits a measured [[ground_reaction_force|GRF]] moment about [[center_of_mass|COM]] to be formed from the force and [[moment_arm]], but the dossier does not assign a universal force or moment direction to this vault interval.

## Myofascial-Line Interpretation

[[functional_lines]] and the [[spiral_line]] provide Level 1 structural pathways for the vault's interpretation of continued trunk and shoulder organisation. Kwon does not establish myofascial-line loading, stored fascial energy or tissue state during EPR-to-TB.

## App Observability (Level 5)

**Camera-observable:** EPR and TB timing and qualified pelvis/thorax orientations may be estimated with suitable visibility and a declared rotation convention. **Unavailable from ordinary video:** ordinary video cannot measure force, moment, impulse or tissue state. **Hypothesised:** fascial loading and energy-storage language remains Level 5.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[end_pelvis_rotation]] |
| ends_at | [[top_backswing_position]] |
| follows | [[shaft_parallel_to_end_pelvis_rotation]] |
| precedes | [[golf_swing_transition]] |
| relevant_to | [[thoracic_rotation]], [[trail_shoulder_external_rotation]] |
| relevant_to | [[golfer_ground_interaction_model]], [[ground_reaction_force]], [[moment_arm]], [[center_of_mass]] |

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
