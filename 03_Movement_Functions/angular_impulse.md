---
id: angular_impulse
type: Movement Pattern
preferred_name: Angular Impulse
aliases: [moment impulse, rotational impulse, J_H]
category: Physics
tags: []
short_definition: "The time integral of net external moment about COM, equal to the change in whole-system angular momentum about COM."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Provides the external-moment taxonomy and event context required for golf-specific angular-impulse analysis."
relationships:
  parent_concepts: [golfer_ground_interaction_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, moment_arm, center_of_mass, pivoting_moment, foot_contact_moment, angular_momentum]
  stable_anatomy: []
  golf_interpretation: []
  app_hypotheses: []
relationship_count: 12
hub_score: 21
centrality: 0.245
confidence: high
review_status: active_spec
updated: 2026-07-16
---

# Angular Impulse

## Definition

**Angular impulse about COM** is the time integral of net external moment about the system COM:

$$\mathbf{J}_{H}=\int \mathbf{M}_{ext,COM}\,dt=\Delta\mathbf{H}_{COM}$$

It relates external moment to the change in whole-system [[angular_momentum|angular momentum]] about COM. Internal segment and joint moments can redistribute angular momentum within the system but do not change its total.

## Why It Matters

Angular impulse captures both moment magnitude and duration. It also requires the three moment classes to remain explicit: the moment of [[ground_reaction_force|GRF]] about [[center_of_mass|COM]] using the [[moment_arm|GRF line-of-action geometry]], [[pivoting_moment]], and [[foot_contact_moment]]. The residual [[ground_reaction_moment|GRM]] at COP underlies the foot-contact class and must not be added again as a separate fourth contribution.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors the golfer-ground moment taxonomy and source-defined swing events. The angular impulse-momentum identity is general mechanics; golf-specific calculation requires measured moments and declared integration bounds.

## Measurement Boundary

**Direct calculation:** synchronised foot-specific force-plate forces, moments and COP geometry are used to construct the external moment about COM and integrate it over time.

**Camera observation:** video can identify approximate kinematic events and segment orientation timing. It cannot measure external moments or angular impulse, and visible rotation is not a substitute for force-plate integration.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| integrates | [[ground_reaction_force]] | GRF and its line of action produce the first moment class about COM. |
| references | [[center_of_mass]] | The net external moment is formed about COM. |
| uses_geometry_from | [[moment_arm]] | Perpendicular force-line geometry defines the GRF moment. |
| integrates | [[pivoting_moment]] | Pivoting moment contributes to angular impulse. |
| integrates | [[foot_contact_moment]] | Direct torsional GRM contributes to angular impulse. |
| changes | [[angular_momentum]] | Net external angular impulse equals its change about COM. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Level 3 golf measurement context. |

## Parent Concepts

- [[golfer_ground_interaction_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[ground_reaction_force]]
- [[moment_arm]]
- [[center_of_mass]]
- [[pivoting_moment]]
- [[foot_contact_moment]]
- [[angular_momentum]]

## Evidence Level

**Level 3 for golf-specific application; general mechanics for the impulse-momentum identity.** It does not demonstrate fascial loading or energy transfer.

## App Use

Calculate angular impulse only with compatible kinetic and kinematic sensor data. Video-only mode may report event timing and segment kinematics, not angular impulse.

## Open Questions

- How should golfer-only and golfer-club system boundaries be reported when comparing angular impulse intervals?
