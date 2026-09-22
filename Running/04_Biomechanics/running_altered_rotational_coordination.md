---
id: running_altered_rotational_coordination
canonical_id: running.interpretation.altered_rotational_coordination
type: App Logic
running_node_type: biomechanical_interpretation
evidence_level: 5
running_claim_level: C
status: canonical
preferred_name: Running - Altered Rotational Coordination
aliases: [Altered Rotational Coordination]
domain: running
directly_measured: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_pontzer_arm_swing_2009, running_arellano_arm_swing_2014]
relationships:
  required_inputs: [running_rotational_coupling, running_rotational_reversal, running_arm_leg_coordination, running_cross_body_coordination, running_variability]
  supports: [running_cross_body_myofascial_hypothesis]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 20
hub_score: 35
centrality: 0.179
updated: 2026-09-09
---

# Running - Altered Rotational Coordination

## Definition

A cautious interpretation of repeated, high-confidence differences in multi-segment proxy timing or relative phase.

## Why It Matters

This node makes the transition from observed patterns to a bounded biomechanical interpretation explicit.

## Required Inputs

- [[running_rotational_coupling]]
- [[running_rotational_reversal]]
- [[running_arm_leg_coordination]]
- [[running_cross_body_coordination]]
- [[running_variability]]

## Evidence Gate

Apply [[running_evidence_gate]]. Require mutually supporting inputs, matched literature, sufficient confidence, and contextual wording.

## Camera Boundary

front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_cross_body_myofascial_hypothesis]]

## What It Cannot Prove

It cannot diagnose spinal restriction, muscle imbalance, fascial tightness, or true 3D rotation.

## Literature Evidence

- [[running_preece_spine_pelvis_2016]]
- [[running_pontzer_arm_swing_2009]]
- [[running_arellano_arm_swing_2014]]

## Reporting Language

Permitted: "The repeated proxy differences may reflect a different rotational coordination strategy between sides."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
