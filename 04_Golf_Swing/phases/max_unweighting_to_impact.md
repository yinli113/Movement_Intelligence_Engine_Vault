---
id: max_unweighting_to_impact
type: Golf Phase
preferred_name: Max Unweighting to Impact
aliases: [phase 5, downswing to impact, unweighting to impact]
short_definition: "Fifth source-defined golf swing phase interval from Max Unweighting to Impact."
relationships:
  contains: [max_unweighting, impact_position, ground_reaction_force, force_transmission, energy_transfer]
  connects_to: [golf_swing_transition, impact_to_hands_chest_height, golf_swing]
  produces: [impact_position]
  assists: [force_transmission, energy_transfer]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_impact_sequence_screen]
  improved_by: [planned_transition_sequence_drill]
  supported_by: [golf_decoded_six_phases_swing, dr_kwon_golfer_ground_interaction]
  relevant_to: [golfer_ground_interaction_model, ground_reaction_force, moment_arm, center_of_mass, linear_impulse, angular_impulse, functional_lines, spiral_line, plantar_fascia]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 33
hub_score: 100
centrality: 0.297
updated: 2026-07-16
---

# Max Unweighting to Impact

## Definition

Max Unweighting to Impact is the source-defined interval from the unweighting boundary event to ball impact.

## Why It Matters

This interval is where the graph should reason about force redirection into impact, not just local muscle contraction.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the fifth interval as Max Unweighting -> Impact.

## Source-Defined Boundary

This Level 4 vault phase begins at [[max_unweighting]], which is not yet mapped to a Kwon event, and ends at [[impact_position]], which crosswalks to Kwon's BI event. The phase is retained even though only one boundary has a supported event match.

## Golf Biomechanics (Level 3)

BI provides a supported timing anchor. Instrumented [[ground_reaction_force|GRF]] and the external moments in the [[golfer_ground_interaction_model]] can be analysed over explicitly defined intervals; the frontal-plane F/B-axis moment of combined GRF through combined COP about [[center_of_mass|COM]] traverses [[ground_reaction_force]], [[moment_arm]], [[center_of_mass]] and the central model, not [[ground_reaction_moment]]. No universal force or moment direction is assigned to this partially mapped vault interval.

## Myofascial-Line Interpretation

[[functional_lines]], the [[spiral_line]] and [[plantar_fascia]] supply structural pathways for a separate vault interpretation of whole-body force transmission. Kwon does not establish myofascial-line loading or tissue-specific energy transfer.

## App Observability (Level 5)

**Camera-observable:** the source-labelled Max Unweighting boundary may be emitted only under a separately declared annotation rule specifying camera view, required landmarks, operational event criterion, reliability gate and timing uncertainty; visibility alone is insufficient. BI timing must likewise retain its event rule and uncertainty. **Unavailable from ordinary video:** ordinary video cannot measure force, moment, [[linear_impulse]], [[angular_impulse]] or tissue state. **Hypothesised:** any unweighting, fascial loading or energy-flow score remains Level 5; pose landmarks do not establish measured vertical GRF or a jump.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[max_unweighting]] |
| ends_at | [[impact_position]] |
| follows | [[golf_swing_transition]] |
| precedes | [[impact_to_hands_chest_height]] |
| related_to | [[ground_reaction_force]], [[force_transmission]], [[energy_transfer]] |
| relevant_to | [[golfer_ground_interaction_model]], [[moment_arm]], [[center_of_mass]], [[linear_impulse]], [[angular_impulse]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[max_unweighting]]
- [[impact_position]]
- [[ground_reaction_force]]
- [[force_transmission]]
- [[energy_transfer]]

## Category

Movement Phase
