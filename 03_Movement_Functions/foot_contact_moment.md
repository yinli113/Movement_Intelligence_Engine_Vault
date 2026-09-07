---
id: foot_contact_moment
type: Movement Pattern
preferred_name: Foot-Contact Moment
aliases: [foot contact moment, torsional GRM, free moment]
category: Biomechanics
tags: []
short_definition: "The direct torsional ground reaction moment acting on a foot at the foot-ground interface."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines foot-contact moments as direct torsional GRMs and bounds the reported sample finding."
relationships:
  parent_concepts: [golfer_ground_interaction_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, ground_reaction_moment, center_of_pressure, angular_impulse, pivoting_moment]
  stable_anatomy: []
  golf_interpretation: []
  app_hypotheses: []
confidence: high
review_status: active_spec
relationship_count: 10
hub_score: 20
centrality: 0.09
updated: 2026-07-16
---

# Foot-Contact Moment

## Definition

The **foot-contact moment** is the direct/residual torsional [[ground_reaction_moment|GRM]] at a foot-ground interface. Its relevant vertical-axis component can be described as the measured free moment $M_{contact,z}$. It is not the [[pivoting_moment]] created by separated individual horizontal foot GRFs, nor the combined-GRF moment through combined COP about golfer COM projected to the frontal-plane F/B axis.

## Why It Matters

Keeping this component separate prevents direct torsional contact mechanics from being mislabelled as the combined-GRF frontal-plane/F-B-axis moment about whole-body COM or as a two-foot vertical-axis pivoting couple. The reported magnitude ranking in Kwon's skilled-male sample is sample-specific, not universal across golfers, footwear, surfaces or tasks.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors the definition to `kwon_fgmom`, “Foot Contact Moments,” Figure 6, and to the methods and sample boundary of `han_etal_2019_ground_interaction`.

## Measurement Requirements

A force plate beneath each foot must measure the moment components as well as the 3D force components and COP. A pressure mat measures vertical sensor forces and COP, not this torsional GRM.

Ordinary single-camera video cannot measure this moment. Apparent foot direction, pelvis rotation, or body motion is not a substitute for force-plate kinetics.

## Phase Relevance

Foot-contact moment may be integrated over a defined swing interval as one contribution to [[angular_impulse]]. Timing comparisons require synchronised force data and explicit event definitions.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| class_of | [[golfer_ground_interaction_model]] | The direct/residual torsional foot-ground component in the axis-specific formulation. |
| represented_by | [[ground_reaction_moment]] | The residual/direct GRM is the measured quantity underlying this class, not an additional moment contribution. |
| co_measured_with | [[ground_reaction_force]] | Force and moment components come from the force plate. |
| located_at | [[center_of_pressure]] | Represented at the foot COP. |
| integrates_as | [[angular_impulse]] | Its time integral contributes to change in angular momentum. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Level 3 mechanics source. |

## Parent Concepts

- [[golfer_ground_interaction_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[ground_reaction_force]]
- [[ground_reaction_moment]]
- [[center_of_pressure]]
- [[pivoting_moment]]
- [[angular_impulse]]

## Evidence Level

**Level 3 — golf biomechanics research.** The measurement does not identify muscle activation or fascial tension.

## App Use

Reserve this label for force-plate moment data. Do not infer it from visible shoe rotation, stance or body motion.

## Open Questions

- How do footwear and surface friction affect foot-contact moments across matched swing tasks?
