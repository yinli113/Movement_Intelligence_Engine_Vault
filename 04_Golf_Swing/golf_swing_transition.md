---
id: golf_swing_transition
type: Golf Phase
preferred_name: Golf Transition Phase
aliases: [transition, golf swing transition, backswing to downswing transition, top backswing to max unweighting, phase 4]
short_definition: "The source-aligned golf swing phase interval from Top Backswing to Max Unweighting where backswing load is redirected into downswing sequencing."
relationships:
  contains: [top_backswing_position, max_unweighting, toe_loading, hip_internal_rotation, thoracic_rotation, trail_shoulder_external_rotation]
  connects_to: [golf_swing, end_pelvis_rotation_to_top_backswing, max_unweighting_to_impact, movement_sequencing]
  produces: [downswing_sequence, max_unweighting]
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: [planned_transition_observation_screen]
  improved_by: [planned_transition_sequence_drill]
  supported_by: [golf_movement_reasoning_mvp, golf_decoded_six_phases_swing]
  relevant_to: [deep_front_line, lateral_line, functional_lines, spiral_line, superficial_back_line, jaw_clenching, neck_tension, force_transmission, energy_transfer]
golf_relevance: "Primary MVP hub for testing whether the vault can reason from a swing phase through ground contact, hip rotation, trunk rotation, fascial-line transfer, and compensation signals."
evidence:
  - source_id: golf_decoded_six_phases_swing
    source_type: screenshot
    locator: "The 6 Phases of the Swing; phase label Top Backswing -> Max Unweighting"
    supports: "The existing transition node maps to the source-defined phase interval from Top Backswing to Max Unweighting."
  - source_id: golf_movement_reasoning_mvp
    source_type: project_model
    locator: "MVP graph design"
    supports: "Transition is selected as the first reasoning slice because it links ground contact, hip, thorax, shoulder, and compensation patterns."
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Chapters 3, 5, 6, 8, 9"
    supports: "Fascial-line nodes used by this phase are supported by Myers as source model references."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 30
hub_score: 89
centrality: 0.6
updated: 2026-06-29
---

# Golf Transition Phase

## Relationships

- starts_at -> [[top_backswing_position]]
- ends_at -> [[max_unweighting]]
- follows -> [[end_pelvis_rotation_to_top_backswing]]
- precedes -> [[max_unweighting_to_impact]]
- contains -> [[toe_loading]]
- contains -> [[hip_internal_rotation]]
- contains -> [[thoracic_rotation]]
- contains -> [[trail_shoulder_external_rotation]]
- relevant_to -> [[deep_front_line]]
- relevant_to -> [[lateral_line]]
- relevant_to -> [[functional_lines]]
- relevant_to -> [[spiral_line]]
- relevant_to -> [[superficial_back_line]]
- possible_compensation -> [[neck_tension]]
- possible_compensation -> [[jaw_clenching]]
- connects_to -> [[golf_swing]]
- supported_by -> [[golf_decoded_six_phases_swing]]

## MVP Traversal

Use this as the graph entry point for the first product demo:

[[golf_swing_transition]] -> [[toe_loading]] -> [[hip_internal_rotation]] -> [[thoracic_rotation]] -> [[functional_lines]] -> [[trail_shoulder_external_rotation]]

Source-aligned interval:

[[top_backswing_position]] -> [[golf_swing_transition]] -> [[max_unweighting]]

Compensation branch:

[[golf_swing_transition]] -> [[thoracic_rotation]] -> [[neck_tension]] -> [[jaw_clenching]]

Fascial-line branch:

[[golf_swing_transition]] -> [[deep_front_line]] / [[lateral_line]] / [[spiral_line]] / [[functional_lines]] / [[superficial_back_line]]

## Golf Reasoning

This note is the hub, not a lecture summary. Its job is to connect observations and constraints:

- If foot pressure fails, start with [[toe_loading]].
- If pelvis slides or knee collapses, inspect [[hip_internal_rotation]].
- If the upper body turns by bracing, inspect [[thoracic_rotation]], [[neck_tension]], and [[jaw_clenching]].
- If the trail shoulder overworks, inspect [[functional_lines]] and [[trail_shoulder_external_rotation]].

## Evidence Notes

This is a product reasoning node. Its relationships are supported by the sample graph design and by the source-backed fascial and anatomy nodes it connects to.

## Open Questions

- Create `transition_observation_screen` as the first Assessment node.
- Create `transition_sequence_drill` as the first Exercise node.
