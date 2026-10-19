---
id: running_long_forward_landing_pattern
canonical_id: running.pattern.long_forward_landing
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Long Forward Landing Pattern
aliases: [Long Forward Landing Pattern]
domain: running
directly_measured: false
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_anderson_step_rate_2022, running_schubert_stride_frequency_2014]
relationships:
  required_inputs: [running_landing_relationship, running_tibial_inclination, running_knee_flexion_at_contact, running_left_right_asymmetry]
  supports: [running_longer_landing_strategy]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 11
hub_score: 17
centrality: 0.098
updated: 2026-09-09
---

# Running - Long Forward Landing Pattern

## Definition

A repeated, within-runner pattern of greater positive foot-to-body-centre-proxy offset at initial contact.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_landing_relationship]]
- [[running_tibial_inclination]]
- [[running_knee_flexion_at_contact]]
- [[running_left_right_asymmetry]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

side view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_longer_landing_strategy]]

## What It Cannot Prove

This pattern is not a measured braking force and should not be called injury-causing overstriding.

## Literature Evidence

- [[running_anderson_step_rate_2022]]
- [[running_schubert_stride_frequency_2014]]

## Reporting Language

Permitted: "A longer forward landing relationship repeated on the right across high-confidence contacts."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
