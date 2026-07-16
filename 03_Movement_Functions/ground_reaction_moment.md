---
id: ground_reaction_moment
type: Movement Pattern
preferred_name: Ground Reaction Moment
aliases: [GRM, foot-ground reaction moment]
category: Biomechanics
short_definition: "The residual/direct ground reaction moment associated with a resultant GRF represented at COP."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines the residual/direct GRM at COP that underlies the foot-contact-moment class."
relationships:
  parent_concepts: [foot_contact_moment, movement_chain_model]
  child_concepts: []
  related_concepts: [golfer_ground_interaction_model, ground_reaction_force, center_of_pressure, torque]
confidence: high
review_status: active_spec
relationship_count: 18
hub_score: 46
centrality: 0.31
updated: 2026-07-16
---

# Ground Reaction Moment

## Definition

**Ground reaction moment (GRM)** has one responsibility in this vault: it is the residual/direct GRM associated with the resultant [[ground_reaction_force|GRF]] represented at [[center_of_pressure|COP]]. It is the direct torsional interaction underlying [[foot_contact_moment]], not the combined-GRF moment about golfer COM projected to the frontal-plane F/B axis and not the vertical-axis [[pivoting_moment]].

## Why It Matters

This binding prevents the contact residual from being counted once as GRM and again as foot-contact moment. The frontal-plane F/B-axis GRF component uses the combined/resultant GRF through combined COP about golfer COM and is represented separately by [[ground_reaction_force]], [[moment_arm]], [[center_of_mass]] and [[golfer_ground_interaction_model]].

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors the distinction between a force moment about a reference and the residual/direct moment measured with the resultant force at COP. [[golfer_ground_interaction_model]] places this GRM only under the foot-contact-moment class.

## Measurement Boundary

A force plate measures three force components and moment components; two plates permit foot-specific analysis. A pressure mat cannot measure full 3D GRF/GRM. Ordinary video cannot measure GRM.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| underlies | [[foot_contact_moment]] | This residual/direct COP moment is the measured quantity for that taxonomy class. |
| associated_with | [[ground_reaction_force]] | The residual moment accompanies the resultant GRF representation at COP. |
| represented_at | [[center_of_pressure]] | COP is the representation point for the resultant force and residual moment. |
| classified_by | [[golfer_ground_interaction_model]] | The model keeps this quantity within foot-contact moment, not the combined-GRF frontal-plane/F-B-axis component. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Level 3 mechanics source. |

## Parent Concepts

- [[foot_contact_moment]]
- [[movement_chain_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[golfer_ground_interaction_model]]
- [[ground_reaction_force]]
- [[center_of_pressure]]
- [[torque]]

## Evidence Level

**Level 3 — golf biomechanics research.** This direct contact measurement does not identify muscle activation or fascial tension.

## App Use

Reserve GRM for compatible force-plate moment data at the foot-ground interface. Do not use the label for a camera-derived combined-GRF frontal-plane/F-B-axis moment about COM or as a duplicate of foot-contact moment.

## Open Questions

- Which force-plate origin and free-moment transformation conventions will the app accept?
