---
id: running_cross_body_coordination
canonical_id: running.rotation.cross_body_coordination
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Cross Body Coordination
aliases: [Cross Body Coordination]
domain: running
directly_measured: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_arellano_arm_swing_2014, running_pontzer_arm_swing_2009, running_preece_spine_pelvis_2016]
relationships:
  required_inputs: [running_shoulder_rotation, running_pelvis_rotation, running_arm_leg_coordination, running_rotational_coupling, running_pelvis_thorax_rotation]
  supports: [running_altered_rotational_coordination, running_cross_body_myofascial_hypothesis]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 16
hub_score: 25
centrality: 0.143
updated: 2026-09-09
---

# Running - Cross Body Coordination

## Definition

A repeated relationship among opposite arm and leg timing plus pelvis-thorax proxy behaviour.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_shoulder_rotation]]
- [[running_pelvis_rotation]]
- [[running_arm_leg_coordination]]
- [[running_rotational_coupling]]
- [[running_pelvis_thorax_rotation]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_altered_rotational_coordination]]
- [[running_cross_body_myofascial_hypothesis]]

## What It Cannot Prove

Cross-body coordination does not measure fascial tension, muscle activation, or energy transfer.

## Literature Evidence

- [[running_arellano_arm_swing_2014]]
- [[running_pontzer_arm_swing_2009]]
- [[running_preece_spine_pelvis_2016]]

## Reporting Language

Permitted: "A repeated cross-body timing difference was present across valid strides."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
