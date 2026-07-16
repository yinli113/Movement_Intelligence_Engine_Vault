---
id: movement_chain_model
type: Movement Pattern
preferred_name: Biomechanical Movement Chain Model
aliases: [movement chain, kinetic chain, movement_chain]
category: Biomechanics
short_definition: "A layered reasoning model that keeps measured external mechanics, myofascial interpretation and app hypotheses distinct."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Provides the external force, moment and event mechanics layer."
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Provides the primary myofascial-line anatomy layer."
relationships:
  parent_concepts: []
  child_concepts: [golfer_ground_interaction_model, ground_reaction_force, ground_reaction_moment, force_transmission, energy_transfer, functional_lines]
  related_concepts: [linear_impulse, angular_impulse, angular_momentum, kinematic_sequence]
confidence: high
review_status: active_spec
relationship_count: 12
hub_score: 24
centrality: 0.207
updated: 2026-07-16
---

# Biomechanical Movement Chain Model

## Definition

The **Biomechanical Movement Chain Model** is a layered graph framework, not a claim that one measured quantity passes unchanged from the ground to the club:

```text
Measured external mechanics (Levels 2–3)
→ anatomical and myofascial interpretation (Levels 1–2 plus stated inference)
→ golf application interpretation (Levels 3–4)
→ app hypothesis (Level 5)
```

[[functional_lines]] remain the primary anatomy. [[golfer_ground_interaction_model]] supplies reusable external mechanics without being treated as fascial-loading evidence.

## Why It Matters

The layered model prevents a kinematic observation from being relabelled as force, moment, impulse, energy or tissue loading. It supports graph traversal while retaining the five evidence levels.

## Supporting Evidence

### Measured Mechanics — Levels 2–3

Force plates and calibrated motion capture can quantify external force, COP, moment, impulse and kinematics under declared system and coordinate conventions. Only external moments change whole-system [[angular_momentum]].

### Fascial Interpretation — Levels 1–2 plus explicit inference

Anatomy Trains defines the vault's myofascial-line structure. A proposed pathway through [[functional_lines]] or another line must cite appropriate anatomy/fascia evidence and remain separate from Kwon's Level 3 kinetics.

### App Hypothesis — Level 5

Connections from an observed movement pattern to a causal “weak link”, energy loss, tissue tension or intervention are hypotheses. Alternative explanations and confidence must be reported.

## Sensor Boundary

Ordinary video cannot measure force, pressure, moments, impulses, energy, muscle activation or fascial tension. It may support qualified kinematic observations and event timing only.

## Relationships

| Layer | Canonical node | Evidence-safe role |
| :--- | :--- | :--- |
| External mechanics | [[golfer_ground_interaction_model]] | Defines force, moment and impulse relationships. |
| Linear balance | [[linear_impulse]] | Measured external force integrated over time. |
| Angular balance | [[angular_impulse]] | Measured external moment integrated over time. |
| Kinematics | [[kinematic_sequence]] | Describes motion timing, not transfer. |
| Myofascial anatomy | [[functional_lines]] | Primary anatomy with separate evidence. |
| Interpretation | [[force_transmission]] | Layered load-path interpretation. |
| Energetics | [[energy_transfer]] | Requires work/power/energy evidence. |

## Parent Concepts

- Biomechanics
- Movement intelligence graph

## Child Concepts

- [[golfer_ground_interaction_model]]
- [[ground_reaction_force]]
- [[ground_reaction_moment]]
- [[force_transmission]]
- [[energy_transfer]]
- [[functional_lines]]

## Related Concepts

- [[linear_impulse]]
- [[angular_impulse]]
- [[angular_momentum]]
- [[kinematic_sequence]]

## Evidence Level

This framework preserves Levels 1–5 rather than assigning one evidence level to the entire causal chain.

## App Use

Generate reports in four labelled layers: observation, measured mechanics where sensors permit, fascial/golf interpretation, and Level 5 hypothesis. Do not present a hypothesis as measurement.

## Open Questions

- Which validation datasets can test the app's cross-layer hypotheses without collapsing their evidence levels?
