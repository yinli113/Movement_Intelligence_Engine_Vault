---
id: force_transmission
type: Biomechanics
preferred_name: Force Transmission
aliases: [force transfer, load transfer]
category: Biomechanics
short_definition: "A mechanics concept for how applied loads are conveyed through connected structures, requiring explicit distinction from tissue interpretation."
evidence_level: 2
evidence:
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Provides the vault's primary myofascial-line anatomy."
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Provides measured external golfer-ground mechanics, not evidence of fascial loading."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [golfer_ground_interaction_model, ground_reaction_force, energy_transfer, kinematic_sequence, functional_lines, plantar_fascia, thoracolumbar_fascia]
confidence: medium
review_status: active_spec
relationship_count: 26
hub_score: 75
centrality: 0.448
updated: 2026-07-16
---

# Force Transmission

## Definition

**Force transmission** is a general mechanics description of how loads are conveyed through connected contacts and structures. The phrase must name the measured quantity and system boundary; it must not collapse external force, internal joint loading and fascial interpretation into one claim.

## Why It Matters

The node bridges mechanics and the vault's myofascial graph while preserving evidence boundaries. [[functional_lines]] remain the primary anatomical framework, but golfer-ground force measurements do not directly measure line-specific loading.

## Supporting Evidence

### Measured Mechanics — Levels 2–3

Force plates measure external [[ground_reaction_force]], COP and moments. Kinematics describe motion. Establishing internal loads requires modelling beyond Kwon's external golfer-ground measurements.

### Fascial Interpretation — Levels 1–2 plus explicit inference

Anatomy Trains and fascia research may support anatomical continuity or load-sharing interpretations. Kwon supplies Level 3 mechanics, not fascial-loading evidence.

### App Hypothesis — Level 5

Links from observed sequencing or compensation to a specific transmission pathway are hypotheses. They must include alternatives and uncertainty.

## Sensor Boundary

Ordinary video cannot measure force transmission, force, pressure, moments, impulses, energy, muscle activation or fascial tension. Video may report observable positions and timing only.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| contextualises | [[golfer_ground_interaction_model]] | External mechanics input to later interpretation. |
| distinguished_from | [[energy_transfer]] | Force and energy are different quantities. |
| interpreted_through | [[functional_lines]] | Primary anatomy, with evidence level stated. |
| observed_alongside | [[kinematic_sequence]] | Sequence is kinematic evidence, not force transfer. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | External mechanics only. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[ground_reaction_force]]
- [[energy_transfer]]
- [[kinematic_sequence]]
- [[functional_lines]]
- [[plantar_fascia]]
- [[thoracolumbar_fascia]]

## Evidence Level

Measured external mechanics are Levels 2–3; fascial anatomy is Levels 1–2; app causal inferences are Level 5.

## App Use

Use layered wording: observation, mechanics interpretation, fascial interpretation and app hypothesis. Never present a video proxy as measured force transmission.

## Open Questions

- Which tissue-specific studies can support particular myofascial load-sharing claims?
