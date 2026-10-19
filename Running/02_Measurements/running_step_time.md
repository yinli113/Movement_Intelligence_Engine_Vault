---
id: running_step_time
canonical_id: running.rhythm.step_time
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Step Time
aliases: [Step Time]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: high
related_nodes: []
source_nodes: [running_anderson_step_rate_2022]
relationships:
  required_events: [running_initial_contact]
  supports: [running_left_right_asymmetry, running_variability, running_fatigue_drift]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 10
hub_score: 13
centrality: 0.089
updated: 2026-09-09
---

# Running - Step Time

## Definition

A Level A camera-derived measurement or named proxy. Right-to-left step time was 8 ms longer on median across valid transitions.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]

## Required Landmarks

Bilateral feet or ankles with reliable consecutive contralateral contact events.

## Calculation Concept

Elapsed time from one foot's initial contact to the contralateral foot's next initial contact.

## Normalisation

Report milliseconds and preserve side transition, speed, and frame-rate provenance.

## Recommended Camera View

- side
- front
- back

## Confidence / Quality Gate

Require consecutive valid contralateral contacts and monotonic media timestamps. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_left_right_asymmetry]]
- [[running_variability]]
- [[running_fatigue_drift]]

## What It Cannot Prove

Step time alone does not identify pathology, force, or propulsion. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_anderson_step_rate_2022]]

## Reporting Language

Permitted: "Right-to-left step time was 8 ms longer on median across valid transitions."

## Forbidden Claims

- Do not report: "Long step time proves weakness."
