---
id: running_com_progression
canonical_id: running.body_centre.progression
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - COM Progression
aliases: [COM Progression]
domain: running
directly_measured: true
proxy_measurement: true
com_method: body_centre_proxy_unless_validated_segmental_model
camera_views: [side]
requires_clinical_correlation: false
confidence_required: medium
related_nodes: []
source_nodes: [running_van_hooren_economy_2024]
relationships:
  required_events: [running_running_cycle]
  supports: [running_horizontal_progression, running_vertical_oscillation, running_compression_and_rebound]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 15
hub_score: 20
centrality: 0.134
updated: 2026-09-09
---

# Running - COM Progression

## Definition

A Level A camera-derived measurement or named proxy. The body-centre proxy progressed consistently while vertical excursion increased later in the trial.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_running_cycle]]

## Required Landmarks

The validated [[running_body_centre_proxy]] trajectory and a stable image coordinate system.

## Calculation Concept

Describe the body-centre proxy's horizontal and vertical trajectory across each valid stride; name the proxy method.

## Normalisation

Use body height or a calibrated spatial scale and normalise each cycle to 0-100% time where appropriate.

## Recommended Camera View

- side

## Confidence / Quality Gate

Inherit the body-centre proxy gate and require stable camera motion or explicit stabilisation. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_horizontal_progression]]
- [[running_vertical_oscillation]]
- [[running_compression_and_rebound]]

## What It Cannot Prove

Unless a validated segmental COM model is used, this is not true COM; it cannot establish metabolic economy or force. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_van_hooren_economy_2024]]

## Reporting Language

Permitted: "The body-centre proxy progressed consistently while vertical excursion increased later in the trial."

## Forbidden Claims

- Do not report: "COM efficiency was 82%."
- Do not report: "Ground reaction caused this trajectory."
