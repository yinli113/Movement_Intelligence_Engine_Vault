---
id: running_knee_flexion_at_contact
canonical_id: running.landing.knee_flexion_at_contact
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Knee Flexion at Contact
aliases: [Knee Flexion at Contact]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: high
related_nodes: []
source_nodes: [running_almeida_foot_strike_2015, running_anderson_step_rate_2022]
relationships:
  required_events: [running_initial_contact]
  supports: [running_long_forward_landing_pattern, running_leg_compression_proxy, running_different_load_distribution_strategy]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 15
hub_score: 22
centrality: 0.134
updated: 2026-09-09
---

# Running - Knee Flexion at Contact

## Definition

A Level A camera-derived measurement or named proxy. Knee-flexion proxy at contact was smaller on the right across valid contacts.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]

## Required Landmarks

Contact-side hip, knee, and ankle landmarks.

## Calculation Concept

Calculate the 2D included angle at the knee at the estimated contact frame and express flexion using a documented convention.

## Normalisation

Report degrees and side; do not compare across materially different camera geometry.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require reliable hip/knee/ankle landmarks, side view, and a high-confidence contact event. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_long_forward_landing_pattern]]
- [[running_leg_compression_proxy]]
- [[running_different_load_distribution_strategy]]

## What It Cannot Prove

The angle does not measure knee force, moment, cartilage load, or injury risk. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_almeida_foot_strike_2015]]
- [[running_anderson_step_rate_2022]]

## Reporting Language

Permitted: "Knee-flexion proxy at contact was smaller on the right across valid contacts."

## Forbidden Claims

- Do not report: "Knee load is high because flexion is low."
