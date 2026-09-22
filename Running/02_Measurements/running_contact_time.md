---
id: running_contact_time
canonical_id: running.rhythm.contact_time
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Contact Time
aliases: [Contact Time]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: medium
related_nodes: []
source_nodes: [running_trowell_fatigue_2025, running_anderson_step_rate_2022]
relationships:
  required_events: [running_initial_contact, running_toe_off]
  supports: [running_compression_and_rebound, running_left_right_asymmetry, running_fatigue_drift]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 15
hub_score: 25
centrality: 0.134
updated: 2026-09-09
---

# Running - Contact Time

## Definition

A Level A camera-derived measurement or named proxy. Right contact-time proxy was longer than left across 8 valid stance periods.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]
- [[running_toe_off]]

## Required Landmarks

Contact-side foot/heel/toe landmarks with a visible ground plane.

## Calculation Concept

Elapsed time from estimated initial contact to estimated toe-off for the same foot.

## Normalisation

Report milliseconds and as a percentage of stride time; label as a video-derived contact-time proxy.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require visible contact and toe-off frames, adequate frame rate, stable ground plane, and side-view geometry. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_compression_and_rebound]]
- [[running_left_right_asymmetry]]
- [[running_fatigue_drift]]

## What It Cannot Prove

Video contact time does not measure force, impulse, stiffness, or pressure. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_trowell_fatigue_2025]]
- [[running_anderson_step_rate_2022]]

## Reporting Language

Permitted: "Right contact-time proxy was longer than left across 8 valid stance periods."

## Forbidden Claims

- Do not report: "Long contact time proves low propulsive force."
