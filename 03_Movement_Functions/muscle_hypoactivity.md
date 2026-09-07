---
id: muscle_hypoactivity
type: Movement Function
preferred_name: "Muscle Hypoactivity (Reflectory Inhibition)"
aliases: [hypoactivity, reflectory inhibition, under-recruitment]
short_definition: "Reduced recruitment/activity of a muscle (typically a local stabiliser) due to reflectory inhibition; often lengthened-but-weak, not the same as true structural shortening or weakness."
domain: static_posture
evidence_level: 2
source_role: foundational_clinical_philosophy
supported_by: [czaprowski_nonstructural_posture_2018]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [stabilizer_mobilizer_classification, muscle_hyperactivity, non_structural_sagittal_posture, apparent_shortness_vs_structural_shortening]
directly_supported_claims:
  - "Hypoactivity is reduced recruitment/activity of a muscle, typically a local stabiliser, due to reflectory inhibition."
  - "A hypoactive muscle is often lengthened-but-weak; hypoactivity is not the same as true structural shortening or simple weakness."
app_translation:
  - "The app may flag a stabiliser as 'possibly hypoactive' as a hypothesis when its posture type implies under-recruitment, but must label it a hypothesis, not a measurement."
  - "The app must not assert a muscle is hypoactive from a static silhouette alone (no EMG)."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 11
hub_score: 22
centrality: 0.099
---

# Muscle Hypoactivity (Reflectory Inhibition)

## Definition

**Muscle hypoactivity** is reduced recruitment/activity of a muscle — typically a local stabiliser — due to **reflectory inhibition**. A hypoactive muscle is often **lengthened-but-weak**; hypoactivity is not the same as true structural shortening or simple weakness (Czaprowski et al., 2018, p.3-5, 12-13).

## Why it matters

Hypoactivity is the stabiliser-side failure in the compensation model: when a local stabiliser is under-recruited, mobilisers over-recruit ([[muscle_hyperactivity]]). Reading a posture as "stabiliser hypoactivity" is the engine's functional-organisation interpretation — a hypothesis, not a measurement.

## Source-derived model

- Reflectory inhibition reduces a stabiliser's recruitment.
- Lengthened-but-weak ≠ structurally shortened.
- Corrective logic targets regaining stabiliser activity (e.g., gluteus maximus), not stretching the lengthened muscle.

## Joint involvement

Segmental joints controlled by the inhibited stabiliser; functional, not joint-specific.

## Muscle involvement

By definition this node is about muscle state, but the app cannot measure it; it can only hypothesise from the posture type. Specific muscle claims are traced to the source's per-type tables in the child posture nodes.

## Movement or phase relationships

Paired with [[muscle_hyperactivity]] (A) within [[stabilizer_mobilizer_classification]] (A); applied per [[non_structural_sagittal_posture]] type (A).

## Possible myofascial relationships

Linking hypoactivity to a fascial line is an engine synthesis (C): a hypoactive deep stabiliser may co-occur with a shortened superficial fascial line, but the link is inferred, not measured.

## What a 2D app can observe

- The silhouette that *suggests* a posture type implying under-recruitment; it cannot observe muscle activity (no EMG).

## What the app must not infer

- That a specific muscle is hypoactive from a silhouette alone.
- Muscle length, activation level, fascial tension, or diagnosis.

## Related concepts

[[stabilizer_mobilizer_classification]], [[muscle_hyperactivity]], [[non_structural_sagittal_posture]], [[apparent_shortness_vs_structural_shortening]].

## Sources

- [[czaprowski_nonstructural_posture_2018]] — p.3-5, 12-13.

## Evidence-separation rules

- **(A)** Hypoactivity definition, reflectory inhibition, lengthened-but-weak — directly from Czaprowski et al.
- **(B)** Cross-links to [[stabilizer_mobilizer_classification]], [[muscle_hyperactivity]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
