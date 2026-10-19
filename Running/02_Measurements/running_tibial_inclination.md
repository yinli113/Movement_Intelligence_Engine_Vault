---
id: running_tibial_inclination
canonical_id: running.landing.tibial_inclination
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Tibial Inclination
aliases: [Tibial Inclination]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: high
related_nodes: []
source_nodes: [running_anderson_step_rate_2022]
relationships:
  required_events: [running_initial_contact]
  supports: [running_long_forward_landing_pattern, running_landing_relationship, running_different_load_distribution_strategy]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 14
hub_score: 19
centrality: 0.125
updated: 2026-09-09
---

# Running - Tibial Inclination

## Definition

A Level A camera-derived measurement or named proxy. The right tibial-inclination proxy was more rearward at initial contact in this trial.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]

## Required Landmarks

Contact-side knee and ankle landmarks.

## Calculation Concept

Calculate the sagittal image-plane angle of the knee-to-ankle vector relative to vertical at initial contact.

## Normalisation

Report degrees with sign convention and camera-side orientation.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require high-confidence knee/ankle landmarks, a near-orthogonal side view, and a valid contact event. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_long_forward_landing_pattern]]
- [[running_landing_relationship]]
- [[running_different_load_distribution_strategy]]

## What It Cannot Prove

This 2D angle does not directly measure tibial loading, braking force, or joint moment. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_anderson_step_rate_2022]]

## Reporting Language

Permitted: "The right tibial-inclination proxy was more rearward at initial contact in this trial."

## Forbidden Claims

- Do not report: "Tibial load is excessive."
