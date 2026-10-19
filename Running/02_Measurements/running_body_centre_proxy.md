---
id: running_body_centre_proxy
canonical_id: running.body_centre.proxy
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Body Centre Proxy
aliases: [Body Centre Proxy]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: medium
related_nodes: []
source_nodes: [running_van_hooren_economy_2024]
relationships:
  required_events: [running_running_cycle]
  supports: [running_com_progression, running_vertical_oscillation, running_horizontal_progression, running_landing_relationship]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 15
hub_score: 20
centrality: 0.134
updated: 2026-09-09
---

# Running - Body Centre Proxy

## Definition

A Level A camera-derived measurement or named proxy. The hip-midpoint body-centre proxy moved vertically through this range; true whole-body COM was not measured.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_running_cycle]]

## Required Landmarks

At minimum bilateral hips; a weighted segmental method requires its complete declared landmark set.

## Calculation Concept

Use either the hip midpoint or a named weighted segmental estimate. Store the method identifier; never silently substitute methods.

## Normalisation

Express coordinates in a calibrated or body-height-normalised frame.

## Recommended Camera View

- side
- front
- back

## Confidence / Quality Gate

Require the landmarks specified by the selected method and stable tracking; gaps invalidate dependent samples. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_com_progression]]
- [[running_vertical_oscillation]]
- [[running_horizontal_progression]]
- [[running_landing_relationship]]

## What It Cannot Prove

A hip midpoint is not true whole-body centre of mass and does not measure ground reaction or balance control. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_van_hooren_economy_2024]]

## Reporting Language

Permitted: "The hip-midpoint body-centre proxy moved vertically through this range; true whole-body COM was not measured."

## Forbidden Claims

- Do not report: "Whole-body COM was directly measured."
- Do not report: "Balance was normal because the hip midpoint was stable."
