---
id: running_flight_time
canonical_id: running.rhythm.flight_time
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Flight Time
aliases: [Flight Time]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: medium
related_nodes: []
source_nodes: [running_masson_stiffness_2026]
relationships:
  required_events: [running_toe_off, running_initial_contact]
  supports: [running_running_cycle, running_variability, running_compression_and_rebound]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 15
hub_score: 20
centrality: 0.134
updated: 2026-09-09
---

# Running - Flight Time

## Definition

A Level A camera-derived measurement or named proxy. Median flight-time proxy was 82 ms across six valid intervals.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_toe_off]]
- [[running_initial_contact]]

## Required Landmarks

Both feet/ankles and a visible ground plane through the airborne interval.

## Calculation Concept

Elapsed time from one foot's toe-off until the next initial contact, when neither foot is classified in contact.

## Normalisation

Report milliseconds and frame-count resolution.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require both event boundaries and clear bilateral non-contact; suppress when the ground plane or feet are obscured. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_running_cycle]]
- [[running_variability]]
- [[running_compression_and_rebound]]

## What It Cannot Prove

Flight time does not establish running economy, elastic return, or force. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_masson_stiffness_2026]]

## Reporting Language

Permitted: "Median flight-time proxy was 82 ms across six valid intervals."

## Forbidden Claims

- Do not report: "Short flight time proves poor stiffness."
