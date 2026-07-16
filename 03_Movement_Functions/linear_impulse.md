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
relationships:
  parent_concepts: [golfer_ground_interaction_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, center_of_mass, angular_impulse]
  stable_anatomy: []
  golf_interpretation: []
  app_hypotheses: []
relationship_count: 6
hub_score: 11
centrality: 0.122
confidence: high
review_status: active_spec
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

[[dr_kwon_golfer_ground_interaction]] supplies Level 3 GRF definitions, measurement requirements and operational swing events. The impulse-momentum identity is general mechanics; golf-specific integration requires those measured forces and defined time bounds.

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

**Level 3 for golf-specific application; general mechanics for the impulse-momentum identity.** It is not evidence of fascial loading.

## App Use

Calculate impulse only from compatible kinetic sensor data. In video-only mode, expose event timing and qualified COM-proxy kinematics without force or impulse labels.

## Open Questions

- Which event definitions and gravity convention should standardise golf impulse windows?
