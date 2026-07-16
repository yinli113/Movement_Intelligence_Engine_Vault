---
id: torque
type: Movement Pattern
preferred_name: Torque
aliases: [moment, moment of force, external torque, joint torque]
category: Physics
short_definition: "An alias for moment of force: the vector rotational effect of force about a chosen reference."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Uses moment of force for the angular effect of measured GRF about a reference point."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: [ground_reaction_moment]
  related_concepts: [golfer_ground_interaction_model, moment_arm, center_of_mass, angular_impulse, angular_momentum]
confidence: high
review_status: active_spec
relationship_count: 8
hub_score: 12
centrality: 0.138
updated: 2026-07-16
---

# Torque

## Definition

**“Torque” is retained as an alias, but “moment of force” is preferred in Kwon-derived explanations.** For force $\mathbf F$ applied at position $\mathbf r$ from a chosen reference:

$$\mathbf M=\mathbf r\times\mathbf F$$

External moment, internal joint moment and free contact moment are not interchangeable labels.

## Why It Matters

Net external moment changes whole-system [[angular_momentum]]. Internal joint moments affect segment dynamics and redistribute momentum within the system; they require kinetic measurements and modelling such as inverse dynamics.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors moment of force, line of action and the golfer-ground moment taxonomy.

## Measurement Boundary

Ordinary video can measure or estimate qualified kinematics, but it cannot measure external moments, joint moments, muscle moments or [[angular_impulse]]. Angular acceleration alone does not disclose moment without inertial properties and a complete dynamics model.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| geometry_defined_by | [[moment_arm]] | The force line and reference determine leverage. |
| specialised_as | [[ground_reaction_moment]] | A measured external foot-ground moment. |
| changes | [[angular_momentum]] | Net external moment changes whole-system momentum. |
| integrates_as | [[angular_impulse]] | External moment integrated over time. |
| classified_by | [[golfer_ground_interaction_model]] | Separates external moment classes. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- [[ground_reaction_moment]]

## Related Concepts

- [[golfer_ground_interaction_model]]
- [[moment_arm]]
- [[center_of_mass]]
- [[angular_impulse]]
- [[angular_momentum]]

## Evidence Level

General moment mechanics are Level 2; Kwon-derived golf application is Level 3.

## App Use

Use “moment of force” in Kwon-derived explanations. Never infer torque or moment from ordinary video alone.

## Open Questions

- Which inverse-dynamics assumptions will be permitted for future joint-moment features?
