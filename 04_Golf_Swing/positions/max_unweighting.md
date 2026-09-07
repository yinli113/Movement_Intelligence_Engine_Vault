---
id: max_unweighting
type: Movement Pattern
preferred_name: Max Unweighting
aliases: [maximum unweighting]
short_definition: "Golf swing boundary event in the source model marking the end of the transition interval and start of the impact-directed interval."
relationships:
  contains: [toe_loading, force_transmission]
  connects_to: [golf_swing_transition, max_unweighting_to_impact, golfer_ground_interaction_model, ground_reaction_force, center_of_mass, energy_transfer]
  produces: [downswing_force_redirection]
  assists: [force_transmission]
  stabilizes: [golf_swing_transition]
  limits: []
  compensates_for: []
  active_during: [golf_swing_transition, max_unweighting_to_impact]
  assessed_by: [planned_unweighting_timing_screen]
  improved_by: [planned_transition_sequence_drill]
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [golfer_ground_interaction_model, ground_reaction_force, center_of_mass, center_of_pressure, plantar_fascia, deep_front_line, functional_lines]
confidence: low
review_status: draft_graph_mvp
relationship_count: 15
hub_score: 33
centrality: 0.135
updated: 2026-07-16
---

# Max Unweighting

## Definition

Max Unweighting is the source-defined boundary event after Top Backswing and before Impact.

## Why It Matters

It gives the graph a source-defined timing checkpoint for transition-to-impact reasoning. The label alone is not measured vertical [[ground_reaction_force|GRF]], measured [[center_of_pressure|COP]], or evidence of a jump; those interpretations require additional source support and compatible instruments.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels Max Unweighting as the end of [[golf_swing_transition]] and the start of [[max_unweighting_to_impact]].

## Related Concepts

| Relationship | Target |
|---|---|
| ends | [[golf_swing_transition]] |
| starts | [[max_unweighting_to_impact]] |
| related_to | [[force_transmission]] |
| related_to | [[energy_transfer]] |
| possible_related_to | [[toe_loading]], [[plantar_fascia]] |
| relevant_to | [[golfer_ground_interaction_model]], [[ground_reaction_force]], [[center_of_mass]], [[center_of_pressure]] |

Max Unweighting is not yet mapped to a Kwon event. The label may be emitted only under a separately declared annotation rule specifying camera view, required landmarks, operational event criterion, reliability gate and timing uncertainty; visibility alone is insufficient. The [[golfer_ground_interaction_model]] does not permit vertical GRF, COP, impulse or tissue state to be inferred from that label.

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[force_transmission]]
- [[energy_transfer]]

## Category

Golf
