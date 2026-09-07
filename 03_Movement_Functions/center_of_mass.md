---
id: center_of_mass
type: Movement Pattern
preferred_name: Center of Mass
aliases: [COM, centre of mass, body COM]
category: Physics
short_definition: "The mass-weighted mean position of a defined system."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Uses whole-body COM as the reference for external force moments and distinguishes it from COP."
relationships:
  parent_concepts: [golfer_ground_interaction_model]
  child_concepts: []
  related_concepts: [center_of_pressure, ground_reaction_force, ground_reaction_moment, moment_arm, linear_impulse, angular_impulse, angular_momentum]
confidence: high
review_status: active_spec
relationship_count: 31
hub_score: 106
centrality: 0.279
updated: 2026-07-16
---

# Center of Mass

## Definition

**Center of Mass (COM)** is the mass-weighted mean position of the defined system. Whole-body COM changes as body segments move. Golfer-only and golfer-club COM are different system definitions.

## Why It Matters

Net external force changes COM linear momentum, while net external moment about COM changes whole-system angular momentum about COM. COM is not [[center_of_pressure|COP]], and visible pressure distribution does not locate COM.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] provides the Level 3 golf context for COM as a moment reference and for the COP/COM distinction.

## Measurement Boundary

COM requires a stated segment model, mass parameters and calibrated kinematics, or another validated measurement method. A hip midpoint or torso midpoint from ordinary video is a geometric proxy, not measured whole-body COM. Ordinary video does not measure force, pressure, moments or impulses.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| distinguished_from | [[center_of_pressure]] | COM is mass-weighted; COP is force application. |
| changes_via | [[linear_impulse]] | Net external impulse changes linear momentum. |
| reference_for | [[golfer_ground_interaction_model]] | The model forms the combined-GRF frontal-plane/F-B-axis moment about this chosen centre. |
| reference_for | [[angular_impulse]] | External moment is integrated about COM. |
| classified_by | [[golfer_ground_interaction_model]] | Defines the whole-system mechanics context. |

## Parent Concepts

- [[golfer_ground_interaction_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[center_of_pressure]]
- [[ground_reaction_force]]
- [[ground_reaction_moment]]
- [[moment_arm]]
- [[linear_impulse]]
- [[angular_impulse]]
- [[angular_momentum]]

## Evidence Level

General COM mechanics are Level 2; golf-specific use is Level 3.

## App Use

Label camera-derived midpoints explicitly as geometric proxies. Do not use them to claim COM-COP separation, force or moment without compatible sensors and modelling.

## Open Questions

- Which segment model is appropriate for golfer-only versus golfer-club COM estimates?
