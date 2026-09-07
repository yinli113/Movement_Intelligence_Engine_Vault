---
id: muscle_hyperactivity
type: Movement Function
preferred_name: "Muscle Hyperactivity (Reflectory Excitation)"
aliases: [hyperactivity, reflectory excitation, over-recruitment]
short_definition: "Increased recruitment/activity of a muscle (typically a mobiliser) due to reflectory excitation, often compensating for stabiliser hypoactivity; associated with decreased flexibility, but not the same as true structural shortening/contracture."
domain: static_posture
evidence_level: 2
source_role: foundational_clinical_philosophy
supported_by: [czaprowski_nonstructural_posture_2018]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [stabilizer_mobilizer_classification, muscle_hypoactivity, non_structural_sagittal_posture, apparent_shortness_vs_structural_shortening]
directly_supported_claims:
  - "Hyperactivity is increased recruitment/activity of a muscle, typically a mobiliser, due to reflectory excitation."
  - "Mobiliser hyperactivity often compensates for stabiliser hypoactivity and is associated with decreased flexibility, but is not the same as true structural shortening or contracture."
app_translation:
  - "The app may flag a mobiliser as 'possibly hyperactive' as a hypothesis when its posture type implies over-recruitment, but must label it a hypothesis, not a measurement."
  - "The app must not assert a muscle is shortened/contractured from a silhouette; apparent shortness ≠ structural shortening (see [[apparent_shortness_vs_structural_shortening]])."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 11
hub_score: 22
centrality: 0.099
---

# Muscle Hyperactivity (Reflectory Excitation)

## Definition

**Muscle hyperactivity** is increased recruitment/activity of a muscle — typically a mobiliser — due to **reflectory excitation**. It often compensates for stabiliser [[muscle_hypoactivity]] and is associated with decreased flexibility, but is **not** the same as true structural shortening or contracture (Czaprowski et al., 2018, p.3-5, 12-13).

## Why it matters

Hyperactivity is the mobiliser-side compensation. The hamstrings example (p.12-13) shows that a muscle can appear shortened (decreased flexibility) due to hyperactivity, yet not be structurally contracted — so stretching it blindly is wrong; the fix is to regain stabiliser activity.

## Source-derived model

- Reflectory excitation increases a mobiliser's recruitment.
- Decreased flexibility from hyperactivity ≠ structural contracture.
- Corrective logic: reduce mobiliser overactivity, regain stabiliser activity, in internal range of motion.

## Joint involvement

Joints crossed by the over-active mobiliser; functional, not joint-specific.

## Muscle involvement

By definition about muscle state, but the app cannot measure it; it can only hypothesise from the posture type. Specific muscle claims are traced to the source's per-type tables in the child posture nodes.

## Movement or phase relationships

Paired with [[muscle_hypoactivity]] (A) within [[stabilizer_mobilizer_classification]] (A); applied per [[non_structural_sagittal_posture]] type (A).

## Possible myofascial relationships

Linking hyperactivity to a fascial line is an engine synthesis (C): an over-active mobiliser may lie along a fascial line that *appears* shortened, but fascial-line shortening is read from Anatomy Trains, not confirmed here.

## What a 2D app can observe

- The silhouette that *suggests* a posture type implying over-recruitment; it cannot observe muscle activity (no EMG).

## What the app must not infer

- That a specific muscle is hyperactive, shortened, or contractured from a silhouette alone.
- Muscle length, activation, fascial tension, or diagnosis.

## Related concepts

[[stabilizer_mobilizer_classification]], [[muscle_hypoactivity]], [[non_structural_sagittal_posture]], [[apparent_shortness_vs_structural_shortening]].

## Sources

- [[czaprowski_nonstructural_posture_2018]] — p.3-5, 12-13.

## Evidence-separation rules

- **(A)** Hyperactivity definition, reflectory excitation, decreased-flexibility-≠-contracture — directly from Czaprowski et al.
- **(B)** Cross-links to [[stabilizer_mobilizer_classification]], [[muscle_hypoactivity]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
