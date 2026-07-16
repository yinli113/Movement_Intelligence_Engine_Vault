---
id: address_to_shaft_parallel
type: Golf Phase
preferred_name: Address to Shaft Parallel
aliases: [phase 1, early takeaway, address to shaft parallel]
short_definition: "First source-defined golf swing phase interval from Address to Shaft Parallel."
relationships:
  contains: [address_position, shaft_parallel_position, toe_loading]
  connects_to: [golf_swing, shaft_parallel_to_end_pelvis_rotation, movement_sequencing]
  produces: [early_backswing_sequence]
  assists: [force_transmission]
  stabilizes: [toe_loading]
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_address_setup_screen, planned_early_backswing_sequence_screen]
  improved_by: [planned_tripod_foot_transition_drill]
  supported_by: [golf_decoded_six_phases_swing, dr_kwon_golfer_ground_interaction]
  relevant_to: [golfer_ground_interaction_model, ground_reaction_force, center_of_pressure, plantar_fascia]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 13
hub_score: 23
centrality: 0.265
updated: 2026-07-16
---

# Address to Shaft Parallel

## Definition

Address to Shaft Parallel is the first phase interval in the source model.

## Why It Matters

This interval establishes starting conditions for pressure, posture, and early sequencing.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the first interval as Address -> Shaft Parallel.

## Source-Defined Boundary

This Level 4 vault phase begins at [[address_position]] and ends at [[shaft_parallel_position]]. Neither boundary is yet mapped to a Kwon event because equivalence between the operational definitions has not been established.

## Golf Biomechanics (Level 3)

[[dr_kwon_golfer_ground_interaction]] defines [[ground_reaction_force|GRF]] by magnitude, direction and point of action at [[center_of_pressure|COP]], within the [[golfer_ground_interaction_model]]. The dossier does not provide a phase-specific force or moment direction for this vault interval, so none is assigned here.

## Myofascial-Line Interpretation

[[plantar_fascia]] provides a Level 1 structural pathway for linking the foot to the vault's line model during this interval. Any phase-specific loading interpretation is a separate vault hypothesis; Kwon does not establish myofascial-line loading.

## App Observability (Level 5)

**Camera-observable:** address and shaft-parallel timing may be labelled when the golfer and club are visible. **Unavailable from ordinary video:** ordinary video cannot measure force, moment, COP, pressure or tissue state. **Hypothesised:** any score for [[toe_loading]] or fascial loading must be labelled Level 5 rather than direct measurement.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[address_position]] |
| ends_at | [[shaft_parallel_position]] |
| precedes | [[shaft_parallel_to_end_pelvis_rotation]] |
| relevant_to | [[toe_loading]], [[plantar_fascia]], [[ground_reaction_force]] |
| relevant_to | [[golfer_ground_interaction_model]], [[center_of_pressure]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[address_position]]
- [[shaft_parallel_position]]
- [[toe_loading]]

## Category

Movement Phase
