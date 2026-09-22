---
id: running_arm_leg_coordination
canonical_id: running.rotation.arm_leg_coordination
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Arm Leg Coordination
aliases: [Arm Leg Coordination]
domain: running
directly_measured: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_arellano_arm_swing_2014, running_pontzer_arm_swing_2009, running_active_arm_swing_2025]
relationships:
  required_inputs: [running_shoulder_rotation, running_running_cycle, running_initial_contact, running_toe_off]
  supports: [running_cross_body_coordination, running_altered_rotational_coordination]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 15
hub_score: 23
centrality: 0.134
updated: 2026-09-09
---

# Running - Arm Leg Coordination

## Definition

A derived timing relationship between arm landmark cycles and contralateral leg events.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_shoulder_rotation]]
- [[running_running_cycle]]
- [[running_initial_contact]]
- [[running_toe_off]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_cross_body_coordination]]
- [[running_altered_rotational_coordination]]

## What It Cannot Prove

It cannot establish whether an arm is actively or passively driven, metabolic cost, or optimal amplitude.

## Literature Evidence

- [[running_arellano_arm_swing_2014]]
- [[running_pontzer_arm_swing_2009]]
- [[running_active_arm_swing_2025]]

## Reporting Language

Permitted: "Left-arm and right-leg phase timing was more variable than the opposite pairing."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
