---
id: ground_reaction_moment
type: Movement Pattern
preferred_name: Ground Reaction Moment
aliases: [GRM, foot-ground reaction moment]
category: Biomechanics
short_definition: "A measured external moment from distributed foot-ground reactions; GRF moment about COM is one class in the golfer-ground model."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Separates GRF moment about COM, pivoting moment and direct foot-contact GRM."
relationships:
  parent_concepts: [golfer_ground_interaction_model, movement_chain_model]
  child_concepts: [pivoting_moment, foot_contact_moment]
  related_concepts: [ground_reaction_force, center_of_pressure, center_of_mass, moment_arm, torque, angular_impulse, angular_momentum]
relationship_count: 17
hub_score: 46
centrality: 0.347
confidence: high
review_status: active_spec
updated: 2026-07-16
---

# Ground Reaction Moment

## Definition

**Ground reaction moment (GRM)** is the net moment remaining from distributed foot-ground reactions when represented with a resultant GRF at COP. It is mechanically distinct from GRF. The GRF moment about whole-body COM is:

$$\mathbf M_{GRF,COM}=\mathbf r_{COM\rightarrow COP}\times\mathbf F_{GRF}$$

The scalar [[moment_arm]] is the perpendicular distance from the chosen centre or axis to the force's line of action.

## Why It Matters

Only net external moments change whole-system [[angular_momentum]]. Internal moments redistribute momentum between segments. A vertical GRF can create a non-zero moment when its line of action misses COM, but force magnitude alone does not determine moment or efficiency.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors the three-class taxonomy used by [[golfer_ground_interaction_model]]:

1. GRF moment about golfer COM.
2. [[pivoting_moment]] from individual-foot GRFs about combined COP and the vertical axis.
3. [[foot_contact_moment]] as direct torsional GRM at a foot-ground interface.

## Measurement Boundary

A force plate measures three force components and moment components; two plates permit foot-specific analysis. A pressure mat cannot measure full 3D GRF/GRM. Ordinary video cannot measure any moment class or [[angular_impulse]].

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| classified_by | [[golfer_ground_interaction_model]] | Defines the three distinct moment classes. |
| calculated_with | [[ground_reaction_force]] | GRF moment about COM requires the force vector. |
| referenced_to | [[center_of_mass]] | Whole-system external moment uses COM as reference. |
| distinguishes | [[pivoting_moment]] | Force-vector moment about combined COP. |
| distinguishes | [[foot_contact_moment]] | Direct torsional foot-contact GRM. |
| integrates_as | [[angular_impulse]] | External moment integrated over time. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Level 3 mechanics source. |

## Parent Concepts

- [[golfer_ground_interaction_model]]
- [[movement_chain_model]]

## Child Concepts

- [[pivoting_moment]]
- [[foot_contact_moment]]

## Related Concepts

- [[ground_reaction_force]]
- [[center_of_pressure]]
- [[center_of_mass]]
- [[moment_arm]]
- [[angular_impulse]]
- [[angular_momentum]]

## Evidence Level

**Level 3 — golf biomechanics research.** GRM does not identify muscle activation or fascial tension.

## App Use

Sensor-derived metrics must state system boundary, reference point, axes and event interval. Video-only scores cannot be labelled moment or kinetic efficiency.

## Open Questions

- How should golfer-only and golfer-club external moments be separated in app data schemas?
