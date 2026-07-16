---
id: golfer_ground_interaction_model
type: Movement Pattern
preferred_name: Golfer-Ground Interaction Model
aliases: [golfer-ground mechanics, golfer-ground interaction moments, FGMOM model]
category: Biomechanics
tags: []
short_definition: "A whole-system model relating measured foot-ground forces and moments to changes in the golfer's linear and angular momentum."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines the non-overlapping axis-specific components of golfer-ground interaction moment and their measurement boundaries."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: [pivoting_moment, foot_contact_moment, linear_impulse, angular_impulse]
  related_concepts: [ground_reaction_force, ground_reaction_moment, center_of_pressure, center_of_mass, moment_arm, angular_momentum]
  stable_anatomy: []
  golf_interpretation: []
  app_hypotheses: []
confidence: high
review_status: active_spec
relationship_count: 37
hub_score: 122
centrality: 0.638
updated: 2026-07-16
---

# Golfer-Ground Interaction Model

## Definition

The **Golfer-Ground Interaction Model** describes how external foot-ground forces and moments act on the golfer. Its non-overlapping, axis-specific moment formulation is:

```text
Reported external interaction-moment components
├── Frontal-plane / F-B-axis GRF moment: combined GRF through combined COP about golfer COM
├── Vertical-axis pivoting moment: individual horizontal foot GRFs about the vertical axis through combined COP
└── Foot-contact moment: direct/residual torsional GRM at the foot-ground interface
```

The first component is the moment of the combined/resultant measured [[ground_reaction_force|GRF]] acting through combined [[center_of_pressure|COP]] about whole-body [[center_of_mass|COM]], projected to the frontal-plane F/B axis. The second is the vertical-axis couple-like [[pivoting_moment]] produced by the individual feet's horizontal GRFs about the vertical axis through combined COP. The third is the [[foot_contact_moment]], whose underlying measured quantity is the residual/direct [[ground_reaction_moment|GRM]] at the foot-ground interface. These components are mechanically distinct, axis-specific and must not be collapsed into a single magnitude.

Only external moments change whole-system angular momentum. Internal joint or muscular moments redistribute momentum between segments but cancel in the whole-system balance. A vertical GRF can create a non-zero moment about COM when its line of action does not pass through COM:

$$M_{\mathrm{GRF},F/B}=\left[\left(\mathbf{r}_{COM\rightarrow combined\ COP}\times\mathbf{F}_{combined}\right)\cdot\hat{\mathbf e}_{F/B}\right]$$

$$M_{pivot,z}=\sum_i\left[\left(\mathbf{r}_{combined\ COP\rightarrow COP_i}\times\mathbf{F}_{i,horizontal}\right)\cdot\hat{\mathbf e}_z\right]$$

Do not add pivoting moment to a full foot-by-foot COM moment sum $\sum_i\mathbf r_{COM\rightarrow COP_i}\times\mathbf F_i$: its vertical-axis component already contains the separated-foot force couple, so adding $M_{pivot,z}$ again would double-count pivoting. When pivoting is reported separately, use the combined-COP/resultant-GRF formulation above for the frontal-plane F/B-axis GRF component.

## Why It Matters

The model prevents three common errors: treating GRF and GRM as synonyms, treating visible rotation as a measured moment, and assuming that large GRF automatically means efficient interaction. Mechanical effect depends on force direction, point of application, reference point and timing, not force magnitude alone.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] provides Level 3 claim anchors for the axis-specific taxonomy, the combined-GRF frontal-plane/F-B-axis component, COP/COM distinctions and instrumentation. These golf-biomechanics claims do not establish myofascial loading.

## Measurement Boundary

A force plate measures three force components and moment components; two plates permit foot-specific analysis. A pressure mat measures vertical sensor forces and COP, not full 3D GRF/GRM. Ordinary video can describe qualified kinematics and event timing, but cannot measure force, pressure, moments, impulses, energy, muscle activation or fascial tension.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| calculates_from | [[ground_reaction_force]] | The frontal-plane F/B-axis GRF component uses the combined measured force vector through combined COP. |
| references | [[center_of_mass]] | COM is the reference for the frontal-plane F/B-axis GRF component. |
| uses_geometry_from | [[moment_arm]] | The combined GRF line of action determines the frontal-plane F/B-axis component's leverage. |
| decomposes_into | [[pivoting_moment]] | Individual horizontal foot GRFs about the vertical axis through combined COP. |
| decomposes_into | [[foot_contact_moment]] | Direct torsional foot-contact GRM. |
| measures_contact_residual_as | [[ground_reaction_moment]] | Underlying GRM for foot-contact moment; not an additional fourth class. |
| integrates_as | [[linear_impulse]] | External force over time changes linear momentum. |
| integrates_as | [[angular_impulse]] | External moment over time changes angular momentum. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Level 3 mechanics source. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- [[pivoting_moment]]
- [[foot_contact_moment]]
- [[linear_impulse]]
- [[angular_impulse]]

## Related Concepts

- [[ground_reaction_force]]
- [[ground_reaction_moment]]
- [[center_of_pressure]]
- [[center_of_mass]]
- [[moment_arm]]
- [[angular_momentum]]

## Evidence Level

**Level 3 — golf biomechanics research.** This node describes measured mechanics; it is not evidence that a particular fascial line loaded or transferred energy.

## App Use

Use the taxonomy to label sensor-derived kinetic quantities. With ordinary video, report only observable kinematics and timing, and do not convert pose proxies into kinetic measurements or efficiency scores.

## Open Questions

- Which force-plate coordinate and sign conventions will the app require for comparable foot-specific moment curves?
