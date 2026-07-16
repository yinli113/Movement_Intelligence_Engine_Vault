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
relationship_count: 11
hub_score: 20
centrality: 0.224
confidence: high
review_status: active_spec
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

[[dr_kwon_golfer_ground_interaction]] supplies Level 3 golf-specific evidence for external [[ground_reaction_moment|GRF moment]], [[pivoting_moment]] and [[foot_contact_moment]]. It does not establish how angular momentum is transferred through fascial tissues.

## Measurement Boundary

Whole-system angular momentum requires calibrated 3D kinematics, segment inertial parameters and an explicit golfer-only or golfer-club system definition. Ordinary video cannot measure angular momentum, external moment, energy, muscle activation or fascial tension.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| changes_via | [[angular_impulse]] | External moment integrated over time changes angular momentum. |
| changes_via | [[ground_reaction_moment]] | GRF moment about COM contributes externally. |
| changes_via | [[pivoting_moment]] | Foot-specific force geometry contributes externally. |
| changes_via | [[foot_contact_moment]] | Direct torsional GRM contributes externally. |
| distinguished_from | [[kinematic_sequence]] | Peak angular-velocity order is not angular-momentum transfer. |
| classified_by | [[golfer_ground_interaction_model]] | Defines the external-moment classes. |

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
