---
id: angular_momentum
type: Movement Pattern
preferred_name: Angular Momentum
aliases: [rotational momentum, system angular momentum, H]
category: Physics
short_definition: "A reference-dependent vector quantity describing rotational motion of a defined system."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Establishes that external golfer-ground moments are required to change whole-system angular momentum."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [golfer_ground_interaction_model, ground_reaction_moment, pivoting_moment, foot_contact_moment, torque, center_of_mass, angular_impulse, kinematic_sequence]
confidence: high
review_status: active_spec
relationship_count: 14
hub_score: 24
centrality: 0.126
updated: 2026-07-16
---

# Angular Momentum

## Definition

**Angular momentum** $\mathbf H$ is a vector describing rotational motion for a defined system about a stated reference. For a multi-segment golfer it is the sum of segment orbital and spin contributions, not generally the single-axis rigid-body shortcut $I\omega$.

About whole-system COM:

$$\frac{d\mathbf H_{COM}}{dt}=\mathbf M_{ext,COM}$$

## Why It Matters

Only external moments change whole-system angular momentum. Internal joint and muscular moments redistribute angular momentum between segments but cancel in the whole-system balance. The time integral is [[angular_impulse]].

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] supplies Level 3 golf-specific evidence for the non-overlapping axis-specific formulation: combined [[ground_reaction_force|GRF]] through combined COP about COM projected to the frontal-plane F/B axis, vertical-axis [[pivoting_moment]] from individual horizontal foot GRFs about combined COP, and direct/residual torsional [[foot_contact_moment]]. The residual [[ground_reaction_moment|GRM]] is already represented within foot-contact moment. Pivoting must not be added to a full foot-by-foot COM moment sum because that would double-count its separated-foot vertical-axis effect. This evidence does not establish how angular momentum is transferred through fascial tissues.

## Measurement Boundary

Whole-system angular momentum requires calibrated 3D kinematics, segment inertial parameters and an explicit golfer-only or golfer-club system definition. Ordinary video cannot measure angular momentum, external moment, energy, muscle activation or fascial tension.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| changes_via | [[angular_impulse]] | External moment integrated over time changes angular momentum. |
| changes_via | [[golfer_ground_interaction_model]] | GRF, COM and line-of-action geometry define the first external-moment class. |
| changes_via | [[pivoting_moment]] | Foot-specific force geometry contributes externally. |
| changes_via | [[foot_contact_moment]] | Direct torsional GRM contributes externally. |
| distinguished_from | [[kinematic_sequence]] | Peak angular-velocity order is not angular-momentum transfer. |
| classified_by | [[golfer_ground_interaction_model]] | Defines the non-overlapping axis-specific external-moment components. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[angular_impulse]]
- [[ground_reaction_moment]]
- [[pivoting_moment]]
- [[foot_contact_moment]]
- [[center_of_mass]]
- [[kinematic_sequence]]

## Evidence Level

General angular-momentum mechanics are Level 2; golfer-ground application is Level 3.

## App Use

Do not label segment angular velocity, deceleration or temporal sequence as measured momentum transfer. Reserve angular-momentum output for compatible 3D modelling.

## Open Questions

- Which segment inertial model is accurate enough for golfer-club angular-momentum estimates?
