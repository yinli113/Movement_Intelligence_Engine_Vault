---
id: running_left_right_asymmetry
canonical_id: running.variability.left_right_asymmetry
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Left Right Asymmetry
aliases: [Left Right Asymmetry]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [till_yes_running_literature_foundation]
relationships:
  required_inputs: [running_variability, running_running_cycle, running_step_time, running_landing_relationship, running_leg_compression_proxy]
  supports: [running_long_forward_landing_pattern, running_altered_rotational_coordination, running_different_load_distribution_strategy]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 31
hub_score: 54
centrality: 0.277
updated: 2026-09-09
---

# Running - Left Right Asymmetry

## Definition

A side-paired difference for comparable, quality-gated cycles using a declared signed or absolute formula.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_variability]]
- [[running_running_cycle]]
- [[running_step_time]]
- [[running_landing_relationship]]
- [[running_leg_compression_proxy]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

side or front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_long_forward_landing_pattern]]
- [[running_altered_rotational_coordination]]
- [[running_different_load_distribution_strategy]]

## What It Cannot Prove

Asymmetry does not equal dysfunction, pathology, injury, or treatment need.

## Literature Evidence

- [[till_yes_running_literature_foundation]]

## Reporting Language

Permitted: "A persistent left-right difference was detected across 10 valid strides."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
