---
id: center_of_pressure
type: Movement Pattern
preferred_name: Center of Pressure
aliases: [COP, pressure centre]
category: Physics
short_definition: "The point of application of a resultant ground reaction force."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines COP, combined COP and the pressure-mat versus force-plate boundary."
relationships:
  parent_concepts: [golfer_ground_interaction_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, ground_reaction_moment, pivoting_moment, foot_contact_moment, center_of_mass, moment_arm]
confidence: high
review_status: active_spec
relationship_count: 15
hub_score: 34
centrality: 0.135
updated: 2026-07-16
---

# Center of Pressure

## Definition

**COP is the point of application of the resultant GRF, not the body's COM.** For a pressure surface, COP is calculated from the distribution of measured normal forces.

Combined COP location reflects relative vertical forces under the feet; “COP shift” and “weight shift” are not synonyms. Combined COP does not locate body mass.

## Why It Matters

COP supplies point-of-application information for force and moment calculations. COP trajectory alone does not reveal full 3D GRF, GRM, COM, moment or mechanical efficiency.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors COP/COM and instrument distinctions at `kwon_grf_grm`, Figures 3–4.

## Measurement Boundary

A pressure mat measures vertical sensor forces and COP, not full 3D GRF/GRM. A force plate measures three force components and moment components; two plates permit foot-specific analysis. Ordinary video cannot measure pressure or COP; a visible foot or ankle landmark is not COP.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| point_of_application_for | [[ground_reaction_force]] | Locates the resultant GRF. |
| distinguished_from | [[center_of_mass]] | COP is not body COM. |
| referenced_by | [[pivoting_moment]] | Combined COP is its calculation reference. |
| locates | [[foot_contact_moment]] | Direct torsional GRM is represented at foot COP. |
| contributes_to | [[moment_arm]] | Geometry and force line of action determine the arm. |
| classified_by | [[golfer_ground_interaction_model]] | Separates COP, COM and the axis-specific moment components. |

## Parent Concepts

- [[golfer_ground_interaction_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[ground_reaction_force]]
- [[ground_reaction_moment]]
- [[pivoting_moment]]
- [[foot_contact_moment]]
- [[center_of_mass]]
- [[moment_arm]]

## Evidence Level

General COP mechanics are Level 2; golf instrumentation distinctions are Level 3.

## App Use

Use COP labels only with pressure or force-platform data. In video-only mode describe visible kinematics without pressure, COP or weight-shift claims.

## Open Questions

- Which pressure-sensor quality criteria are sufficient for app COP reporting?
