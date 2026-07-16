---
id: impact_to_hands_chest_height
type: Golf Phase
preferred_name: Impact to Hands Chest Height
aliases: [phase 6, early follow-through, post-impact to hands chest height]
short_definition: "Sixth source-defined golf swing phase interval from Impact to Hands Chest Height."
relationships:
  contains: [impact_position, hands_chest_height_position, force_transmission, energy_transfer]
  connects_to: [max_unweighting_to_impact, golf_swing]
  produces: [early_follow_through_checkpoint]
  assists: [movement_sequencing]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_post_impact_deceleration_screen]
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing, dr_kwon_golfer_ground_interaction]
  relevant_to: [golfer_ground_interaction_model, ground_reaction_force, moment_arm, center_of_mass, linear_impulse, angular_impulse, functional_lines, spiral_line, superficial_back_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 25
hub_score: 71
centrality: 0.431
updated: 2026-07-16
---

# Impact to Hands Chest Height

## Definition

Impact to Hands Chest Height is the source-defined post-impact interval ending when the hands reach chest height.

## Why It Matters

It gives the graph an early deceleration and follow-through checkpoint that can reflect quality of prior force transmission.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the sixth interval as Impact -> Hands Chest Height.

## Source-Defined Boundary

This Level 4 vault phase begins at [[impact_position]], which crosswalks to Kwon's BI event, and ends at [[hands_chest_height_position]], which is not yet mapped. Hands Chest Height must not be treated as Kwon's MF or LF event without matching operational definitions.

## Golf Biomechanics (Level 3)

BI provides a supported start-time anchor. With compatible kinetic sensors, external forces and moments may be integrated over a declared post-impact interval through [[linear_impulse]] and [[angular_impulse]], using the non-overlapping axis-specific moment components in [[golfer_ground_interaction_model]]. The dossier does not establish a phase-specific force or moment direction for BI-to-Hands-Chest-Height.

## Myofascial-Line Interpretation

[[functional_lines]], the [[spiral_line]] and [[superficial_back_line]] provide Level 1 structural pathways for the vault's post-impact interpretation. Kwon does not establish myofascial-line loading, fascial release or tissue state in this interval.

## App Observability (Level 5)

**Camera-observable:** BI and Hands Chest Height can be labelled as kinematic events when their operational criteria are met and the club, ball and hands are visible. Camera event time is bounded by frame rate and visibility; exact contact may fall between frames, and timing uncertainty must be reported. **Unavailable from ordinary video:** ordinary video cannot measure force, moment, impulse, energy dissipation or tissue state. **Hypothesised:** deceleration quality, line loading and release remain Level 5 interpretations.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[impact_position]] |
| ends_at | [[hands_chest_height_position]] |
| follows | [[max_unweighting_to_impact]] |
| related_to | [[force_transmission]], [[energy_transfer]] |
| relevant_to | [[golfer_ground_interaction_model]], [[ground_reaction_force]], [[moment_arm]], [[center_of_mass]], [[linear_impulse]], [[angular_impulse]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[impact_position]]
- [[hands_chest_height_position]]
- [[force_transmission]]
- [[energy_transfer]]

## Category

Movement Phase
