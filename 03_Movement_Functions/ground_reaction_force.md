---
id: ground_reaction_force
type: Movement Pattern
preferred_name: Ground Reaction Force
aliases: [GRF, ground forces, ground reaction forces]
category: Physics
short_definition: "The three-dimensional external force exerted by the ground on a foot."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines foot-specific 3D GRF and its point of application, measurement and role in golfer-ground moments."
relationships:
  parent_concepts: [golfer_ground_interaction_model, movement_chain_model]
  child_concepts: [linear_impulse, toe_loading]
  related_concepts: [ground_reaction_moment, pivoting_moment, foot_contact_moment, center_of_pressure, center_of_mass, moment_arm]
  stable_anatomy: [plantar_fascia, ankle_joint, knee_joint, hip_joint]
  golf_interpretation: []
  app_hypotheses: []
relationship_count: 21
hub_score: 45
centrality: 0.429
confidence: high
review_status: active_spec
updated: 2026-07-16
---

# Ground Reaction Force

## Definition

**Ground Reaction Force (GRF)** is the external force exerted by the ground on a contacting foot. It is a vector resolved into vertical and two horizontal components in a declared coordinate system. Its resultant acts at the [[center_of_pressure|COP]].

## Why It Matters

Net external force changes the golfer system's linear momentum; its time integral contributes to [[linear_impulse]]. GRF also contributes to external moments through its direction and line of action. Large GRF does not automatically mean efficient interaction.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] provides Level 3 golf-specific definitions and measurement boundaries. A vertical GRF can create a non-zero moment about [[center_of_mass|COM]] when its line of action does not pass through COM.

## Measurement Boundary

A force plate measures three force components and moment components; two plates permit foot-specific analysis. A pressure mat measures vertical sensor forces and COP, not full 3D GRF/GRM. Ordinary video cannot measure force, pressure, moment or impulse.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| classified_by | [[golfer_ground_interaction_model]] | Places GRF within the whole-system mechanics model. |
| acts_at | [[center_of_pressure]] | COP is the resultant GRF's point of application. |
| creates | [[ground_reaction_moment]] | Its moment about COM depends on 3D geometry. |
| contributes_to | [[pivoting_moment]] | Foot-specific GRFs create this moment about combined COP. |
| co_measured_with | [[foot_contact_moment]] | Force-plate moment components distinguish direct torsional contact moment. |
| integrates_as | [[linear_impulse]] | External force integrated over time changes linear momentum. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Level 3 golf mechanics source. |

## Parent Concepts

- [[golfer_ground_interaction_model]]
- [[movement_chain_model]]

## Child Concepts

- [[linear_impulse]]
- [[toe_loading]]

## Related Concepts

- [[ground_reaction_moment]]
- [[pivoting_moment]]
- [[foot_contact_moment]]
- [[center_of_pressure]]
- [[center_of_mass]]
- [[moment_arm]]

## Evidence Level

General force mechanics are Level 2; golf-specific applications here are Level 3. Neither establishes myofascial loading.

## App Use

Use force labels only with compatible kinetic sensors. Video-only output may report displacement or event timing, but not GRF magnitude or direction.

## Open Questions

- Which force-plate axes and normalisation rules will the app standardise?
