---
id: running_different_load_distribution_strategy
canonical_id: running.interpretation.load_distribution_strategy
type: App Logic
running_node_type: biomechanical_interpretation
evidence_level: 5
running_claim_level: C
status: canonical
preferred_name: Running - Different Load Distribution Strategy
aliases: [Different Load Distribution Strategy]
domain: running
directly_measured: false
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_trunk_lean_loading_2024, running_almeida_foot_strike_2015]
relationships:
  required_inputs: [running_compression_and_rebound, running_trunk_lean, running_knee_flexion_at_contact, running_leg_compression_proxy]
  supports: [running_cross_body_myofascial_hypothesis]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 18
hub_score: 31
centrality: 0.161
updated: 2026-09-09
---

# Running - Different Load Distribution Strategy

## Definition

A cautious interpretation that multiple kinematic features differ in a way that may redistribute mechanical demand, without quantifying that demand.

## Why It Matters

This node makes the transition from observed patterns to a bounded biomechanical interpretation explicit.

## Required Inputs

- [[running_compression_and_rebound]]
- [[running_trunk_lean]]
- [[running_knee_flexion_at_contact]]
- [[running_leg_compression_proxy]]

## Evidence Gate

Apply [[running_evidence_gate]]. Require mutually supporting inputs, matched literature, sufficient confidence, and contextual wording.

## Camera Boundary

side view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_cross_body_myofascial_hypothesis]]

## What It Cannot Prove

It does not measure forces, moments, tissue load, or injury risk.

## Literature Evidence

- [[running_trunk_lean_loading_2024]]
- [[running_almeida_foot_strike_2015]]

## Reporting Language

Permitted: "The combined contact, trunk, knee, and compression proxies may reflect a different sagittal load-distribution strategy."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
