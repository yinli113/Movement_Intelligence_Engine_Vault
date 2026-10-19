---
id: running_till_yes_progression_ratio
canonical_id: running.descriptor.till_yes_progression_ratio
type: Movement Pattern
running_node_type: derived_kinematic_descriptor
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - TillYes Progression Ratio
aliases: [TillYes Progression Ratio]
domain: running
directly_measured: false
not_equivalent_to_running_economy: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_van_hooren_economy_2024]
relationships:
  required_inputs: [running_horizontal_progression, running_vertical_oscillation, running_body_centre_proxy]
  supports: []
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 10
hub_score: 14
centrality: 0.089
updated: 2026-09-09
---

# Running - TillYes Progression Ratio

## Definition

An optional app-derived kinematic descriptor dividing horizontal body-centre-proxy progression by vertical excursion under one declared protocol.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_horizontal_progression]]
- [[running_vertical_oscillation]]
- [[running_body_centre_proxy]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

side view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

No stronger downstream claim is authorised by this node alone.

## What It Cannot Prove

It is not metabolic efficiency or running economy, and cross-trial comparison requires matched calibration, speed, and protocol.

## Literature Evidence

- [[running_van_hooren_economy_2024]]

## Reporting Language

Permitted: "TillYes Progression Ratio was 4.2 under this protocol; it is a kinematic descriptor, not running economy."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
