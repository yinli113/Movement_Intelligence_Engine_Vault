---
id: running_pelvis_thorax_rotation
canonical_id: running.rotation.pelvis_thorax
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Pelvis Thorax Rotation
aliases: [Pelvis Thorax Rotation]
domain: running
directly_measured: false
is_rotation_proxy: true
true_3d_rotation: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_schache_lumbopelvic_1999]
relationships:
  required_inputs: [running_pelvis_rotation, running_thorax_rotation, running_running_cycle]
  supports: [running_rotational_coupling, running_altered_rotational_coordination]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 15
hub_score: 24
centrality: 0.134
updated: 2026-09-09
---

# Running - Pelvis Thorax Rotation

## Definition

The time-varying relationship between declared pelvis- and thorax-orientation proxies.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_pelvis_rotation]]
- [[running_thorax_rotation]]
- [[running_running_cycle]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_rotational_coupling]]
- [[running_altered_rotational_coordination]]

## What It Cannot Prove

It is not true 3D segment rotation, vertebral motion, torque, or tissue loading.

## Literature Evidence

- [[running_preece_spine_pelvis_2016]]
- [[running_schache_lumbopelvic_1999]]

## Reporting Language

Permitted: "Pelvis and thorax proxies showed repeatable counter-directional phases with contextual confidence."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
