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
  - source_id: external_open_textbook_openstax_university_physics_volume_1
    source_type: open_textbook
    evidence_level: 2
    citation: "Moebs, William; Ling, Samuel J.; and Sanny, Jeff. University Physics Volume 1. OpenStax, 2016."
    url: https://openstax.org/books/university-physics-volume-1/pages/11-2-angular-momentum
    locator: "Section 11.2, Equations 11.6 and 11.8: net torque is the time derivative of angular momentum for a particle and for a system; angular impulse follows by integration over a declared interval."
    supports: "Provides Level 2 general-mechanics support for the torque-angular-momentum relation and its time-integrated angular-impulse identity."
relationships:
  parent_concepts: [golfer_ground_interaction_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, moment_arm, center_of_mass, pivoting_moment, foot_contact_moment, angular_momentum]
  stable_anatomy: []
  golf_interpretation: []
  app_hypotheses: []
confidence: high
review_status: active_spec
relationship_count: 18
hub_score: 45
centrality: 0.162
updated: 2026-07-16
---

# Angular Impulse

## Definition

**Angular impulse about COM** is the time integral of net external moment about the system COM:

$$\mathbf{J}_{H}=\int \mathbf{M}_{ext,COM}\,dt=\Delta\mathbf{H}_{COM}$$

It relates external moment to the change in whole-system [[angular_momentum|angular momentum]] about COM. Internal segment and joint moments can redistribute angular momentum within the system but do not change its total.

## Why It Matters

Angular impulse captures both moment magnitude and duration. The Kwon-context formulation keeps three non-overlapping, axis-specific components explicit: the frontal-plane F/B-axis moment of the combined [[ground_reaction_force|GRF]] acting through combined COP about [[center_of_mass|COM]], the vertical-axis [[pivoting_moment]] from individual horizontal foot GRFs about combined COP, and the direct/residual torsional [[foot_contact_moment]]. The residual [[ground_reaction_moment|GRM]] underlies the foot-contact component and must not be added again as a separate contribution.

For the reported axes, the component balance may be written as:

$$\mathbf M_{ext,reported}=M_{\mathrm{GRF},F/B}\hat{\mathbf e}_{F/B}+M_{pivot,z}\hat{\mathbf e}_z+\sum_i\mathbf M_{foot-contact,i}$$

Do not add pivoting moment to a full foot-by-foot COM moment sum $\sum_i\mathbf r_{COM\rightarrow COP_i}\times\mathbf F_i$. The vertical-axis part of that full sum already contains the separated-foot force couple, so adding pivoting separately would double-count it.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors the golfer-ground moment taxonomy and source-defined swing events. [OpenStax University Physics Volume 1, Section 11.2](https://openstax.org/books/university-physics-volume-1/pages/11-2-angular-momentum), Equations 11.6 and 11.8, supplies Level 2 general-mechanics support for $\boldsymbol\tau_{net}=d\mathbf H/dt$; integrating that relation over declared bounds gives the angular impulse-momentum identity. Golf-specific calculation remains Level 3 and requires measured moments and declared integration bounds.

## Measurement Boundary

**Direct calculation:** synchronised foot-specific force-plate forces, moments and COP geometry are used to construct the external moment about COM and integrate it over time.

**Camera observation:** video can identify approximate kinematic events and segment orientation timing. It cannot measure external moments or angular impulse, and visible rotation is not a substitute for force-plate integration.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| integrates | [[ground_reaction_force]] | Combined GRF through combined COP produces the frontal-plane F/B-axis component about COM. |
| references | [[center_of_mass]] | The net external moment is formed about COM. |
| uses_geometry_from | [[moment_arm]] | Perpendicular force-line geometry defines the combined-GRF frontal-plane/F-B-axis component. |
| integrates | [[pivoting_moment]] | The separate vertical-axis pivoting component contributes without a duplicate foot-by-foot COM sum. |
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

**Level 2 for the general angular impulse-momentum identity; Level 3 for golf-specific application.** It does not demonstrate fascial loading or energy transfer.

## App Use

Calculate angular impulse only with compatible kinetic and kinematic sensor data. Video-only mode may report event timing and segment kinematics, not angular impulse.

## Open Questions

- How should golfer-only and golfer-club system boundaries be reported when comparing angular impulse intervals?
