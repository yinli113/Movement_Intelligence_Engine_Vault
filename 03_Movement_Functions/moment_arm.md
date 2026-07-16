---
id: moment_arm
type: Movement Pattern
preferred_name: Moment Arm
aliases: [lever arm, perpendicular distance]
category: Physics
short_definition: "The perpendicular distance from a chosen centre or axis to a force's line of action."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines moment arm and the 3D line-of-action requirement for GRF moment about COM."
relationships:
  parent_concepts: [golfer_ground_interaction_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, ground_reaction_moment, torque, center_of_mass, center_of_pressure]
relationship_count: 8
hub_score: 15
centrality: 0.163
confidence: high
review_status: active_spec
updated: 2026-07-16
---

# Moment Arm

## Definition

**Moment arm is the perpendicular distance from the chosen centre/axis to a force's line of action.** If $\mathbf r$ joins the reference point to any point on that line and $\theta$ is the angle between $\mathbf r$ and $\mathbf F$:

$$d=r\sin\theta,\qquad |\mathbf M|=F d$$

The position-vector magnitude $r$ is not generally the scalar moment arm.

## Why It Matters

Moment depends on force magnitude and 3D geometry. Horizontal COM-COP separation is the moment arm only for a vertical force in the relevant plane; it is not a universal substitute for the perpendicular distance to the measured force line.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors the line-of-action definition and vertical-GRF example at `kwon_moment` and `kwon_fgmom`.

## Measurement Boundary

Calculating a GRF moment arm requires the chosen reference point, force-plate COP, measured 3D force vector and compatible coordinate systems. Ordinary video cannot locate the force's line of action or measure the moment arm.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| defines_geometry_for | [[torque]] | Perpendicular distance scales moment magnitude. |
| defines_geometry_for | [[ground_reaction_moment]] | GRF moment about COM requires this geometry. |
| references | [[center_of_mass]] | COM may be the chosen centre. |
| uses | [[center_of_pressure]] | COP supplies a point on the measured GRF line. |
| classified_by | [[golfer_ground_interaction_model]] | Places the term in the external-moment model. |

## Parent Concepts

- [[golfer_ground_interaction_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[ground_reaction_force]]
- [[ground_reaction_moment]]
- [[torque]]
- [[center_of_mass]]
- [[center_of_pressure]]

## Evidence Level

General moment-arm mechanics are Level 2; the golf application is Level 3.

## App Use

Do not convert landmark separation into a kinetic moment arm unless compatible force and coordinate data establish the line of action.

## Open Questions

- Which 3D calibration requirements are sufficient for combined motion-capture and force-plate analysis?
