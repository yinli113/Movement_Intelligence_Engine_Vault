---
id: linear_impulse
type: Movement Pattern
preferred_name: Linear Impulse
aliases: [force impulse, translational impulse, J]
category: Physics
tags: []
short_definition: "The time integral of net external force, equal to the change in linear momentum."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Provides the measured external-force and swing-event context required for golf-specific impulse analysis."
  - source_id: external_open_textbook_openstax_university_physics_volume_1
    source_type: open_textbook
    evidence_level: 2
    citation: "Moebs, William; Ling, Samuel J.; and Sanny, Jeff. University Physics Volume 1. OpenStax, 2016."
    url: https://openstax.org/books/university-physics-volume-1/pages/9-2-impulse-and-collisions
    locator: "Section 9.2, Equations 9.3 and 9.7: impulse is the time integral of force and equals the system's change in momentum."
    supports: "Provides Level 2 general-mechanics support for the linear impulse-momentum identity."
relationships:
  parent_concepts: [golfer_ground_interaction_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, center_of_mass, angular_impulse]
  stable_anatomy: []
  golf_interpretation: []
  app_hypotheses: []
confidence: high
review_status: active_spec
relationship_count: 11
hub_score: 33
centrality: 0.099
updated: 2026-07-16
---

# Linear Impulse

## Definition

**Linear impulse** is the time integral of net external force:

$$\mathbf{J}=\int \mathbf{F}_{ext}\,dt=\Delta\mathbf{p}$$

For the golfer system, the complete external-force balance includes measured [[ground_reaction_force|GRF]] and gravity; the result is the change in whole-system linear momentum associated with [[center_of_mass|COM]] motion.

## Why It Matters

Impulse distinguishes the effect accumulated across an interval from an instantaneous force peak. A large peak does not necessarily produce a large impulse, and neither quantity alone establishes efficient interaction.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] supplies Level 3 GRF definitions, measurement requirements and operational swing events. [OpenStax University Physics Volume 1, Section 9.2](https://openstax.org/books/university-physics-volume-1/pages/9-2-impulse-and-collisions), Equations 9.3 and 9.7, supplies Level 2 general-mechanics support for impulse as the time integral of force and for the impulse-momentum identity. Golf-specific integration still requires measured forces and defined time bounds.

## Measurement Boundary

**Direct calculation:** synchronised force-plate samples are integrated over a stated interval, with gravity and system definition handled consistently.

**Camera observation:** video may locate approximate events and describe COM-proxy displacement or timing. It does not measure external force or linear impulse, and kinematic timing is not a substitute for force-plate integration.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| integrates | [[ground_reaction_force]] | Measured external force contributes to impulse. |
| changes_motion_of | [[center_of_mass]] | Net external impulse changes whole-system linear momentum. |
| complements | [[angular_impulse]] | Separates translational and rotational system balances. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Level 3 golf measurement context. |

## Parent Concepts

- [[golfer_ground_interaction_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[ground_reaction_force]]
- [[center_of_mass]]
- [[angular_impulse]]

## Evidence Level

**Level 2 for the general impulse-momentum identity; Level 3 for golf-specific application.** It is not evidence of fascial loading.

## App Use

Calculate impulse only from compatible kinetic sensor data. In video-only mode, expose event timing and qualified COM-proxy kinematics without force or impulse labels.

## Open Questions

- Which event definitions and gravity convention should standardise golf impulse windows?
