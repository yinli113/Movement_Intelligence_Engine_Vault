---
id: running_landing_relationship
canonical_id: running.landing.relationship
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Landing Relationship
aliases: [Landing Relationship]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: high
related_nodes: []
source_nodes: [running_anderson_step_rate_2022, running_schubert_stride_frequency_2014]
relationships:
  required_events: [running_initial_contact]
  supports: [running_long_forward_landing_pattern, running_longer_landing_strategy, running_left_right_asymmetry]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 17
hub_score: 30
centrality: 0.152
updated: 2026-09-09
---

# Running - Landing Relationship

## Definition

A Level A camera-derived measurement or named proxy. The contacting foot landed farther ahead of the body-centre proxy on the right across 8 of 10 valid strides.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]

## Required Landmarks

Contacting foot/ankle plus the declared body-centre proxy at the same frame.

## Calculation Concept

Signed horizontal image-plane distance from the contacting-foot reference to the body-centre proxy at initial contact.

## Normalisation

Divide by estimated body height or leg length using one declared method; retain sign and side.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require high-confidence initial contact, stable side-view geometry, visible contact foot, and a valid scale denominator. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_long_forward_landing_pattern]]
- [[running_longer_landing_strategy]]
- [[running_left_right_asymmetry]]

## What It Cannot Prove

Landing offset does not directly measure braking force, impulse, injury risk, or overstriding. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_anderson_step_rate_2022]]
- [[running_schubert_stride_frequency_2014]]

## Reporting Language

Permitted: "The contacting foot landed farther ahead of the body-centre proxy on the right across 8 of 10 valid strides."

## Forbidden Claims

- Do not report: "Excessive braking force detected."
- Do not report: "Overstriding caused the runner's symptoms."
