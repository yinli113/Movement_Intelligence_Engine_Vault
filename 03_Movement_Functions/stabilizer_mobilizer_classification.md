---
id: stabilizer_mobilizer_classification
type: Movement Function
preferred_name: "Stabilizer/Mobilizer Functional Muscle Classification"
aliases: [Bergmark Richardson classification, stabilizer mobilizer model, functional muscle classification]
short_definition: "The Bergmark/Richardson functional classification of skeletal muscles into local stabilisers, global stabilisers, and mobilisers, with reflectory inhibition (hypoactivity) and reflectory excitation (hyperactivity); the engine's functional muscle-organisation model."
domain: static_posture
evidence_level: 2
source_role: foundational_clinical_philosophy
supported_by: [czaprowski_nonstructural_posture_2018]
status: reviewed
reviewed_date: 2026-07-22
contains: [muscle_hypoactivity, muscle_hyperactivity]
connects_to: [non_structural_sagittal_posture, bodyreading_static_posture]
directly_supported_claims:
  - "Muscles are functionally classified as local stabilisers (deep, mono-articular, joint-segment control), global stabilisers (antigravity, multi-articular), and mobilisers (movement-producing)."
  - "Local stabilisers are prone to reflectory inhibition (hypoactivity); mobilisers are prone to reflectory excitation (hyperactivity) and decreased flexibility."
  - "A deficit of locomotor stability triggers a compensatory mechanism: stabilising function is overtaken by mobilisers, producing hyperactivity and decreased flexibility."
app_translation:
  - "Use this classification as the functional-organisation layer paired with fascial-line reading: which stabiliser is under-recruited AND which mobiliser is over-recruited."
  - "The app must not assign a specific muscle's hypo/hyperactivity from a static silhouette alone; that is a hypothesis to flag, not a measurement."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 13
hub_score: 28
centrality: 0.117
---

# Stabilizer/Mobilizer Functional Muscle Classification

## Definition

The **Bergmark/Richardson functional classification** sorts skeletal muscles into **local stabilisers** (deep, mono-articular, joint-segment control), **global stabilisers** (antigravity, multi-articular), and **mobilisers** (movement-producing). Local stabilisers are prone to **reflectory inhibition** ([[muscle_hypoactivity]]); mobilisers are prone to **reflectory excitation** ([[muscle_hyperactivity]]) and decreased flexibility (Czaprowski et al., 2018, p.3-5).

## Why it matters

This is the core of the engine's "how does the body organise movement" philosophy: a deficit of locomotor stability triggers a compensatory mechanism in which the stabilising function is overtaken by mobilisers, producing hyperactivity and decreased flexibility (p.2). It pairs with [[bodyreading_static_posture]] to form a two-layer posture interpretation.

## Source-derived model

- Local stabilisers: deep, mono-articular, segmental control (e.g., multifidus, transversus abdominis, diaphragm, pelvic floor) — prone to hypoactivity.
- Global stabilisers: antigravity, multi-articular — intermediate.
- Mobilisers: movement-producing, superficial — prone to hyperactivity and decreased flexibility.
- Compensation: stabiliser hypoactivity → mobiliser hyperactivity.

## Joint involvement

Segmental spinal control and major movement joints; the classification is functional, not joint-specific.

## Muscle involvement

This node defines the *classification*; specific muscle memberships are listed in the source's tables (p.5-7) and applied per posture type in the child nodes. The app must not assert a specific muscle's state from a silhouette.

## Movement or phase relationships

Functional layer under [[non_structural_sagittal_posture]] (A); complements [[bodyreading_static_posture]] (B).

## Possible myofascial relationships

Cross-linking a stabiliser/mobiliser role to a fascial line is an engine synthesis (C): e.g., a hypoactive deep stabiliser and a shortened superficial fascial line may co-occur, but the link is inferred, not measured.

## What a 2D app can observe

- The silhouette that *suggests* a posture type; it cannot observe muscle hypo/hyperactivity directly.

## What the app must not infer

- A specific muscle's hypoactivity or hyperactivity from a silhouette.
- Fascial tension, muscle length, or diagnosis.

## Related concepts

[[muscle_hypoactivity]], [[muscle_hyperactivity]], [[non_structural_sagittal_posture]], [[apparent_shortness_vs_structural_shortening]], [[bodyreading_static_posture]].

## Sources

- [[czaprowski_nonstructural_posture_2018]] — p.2-7.

## Evidence-separation rules

- **(A)** The three-class model and the inhibition/excitation responses — directly from Czaprowski et al.
- **(B)** Cross-link to [[bodyreading_static_posture]] — Anatomy Trains (Level 1).
- **(C)** Any fascial-line mapping is `engine_synthesis`.
