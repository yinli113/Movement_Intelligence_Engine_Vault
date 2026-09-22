---
id: running_rotational_coupling
canonical_id: running.rotation.coupling
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Rotational Coupling
aliases: [Rotational Coupling]
domain: running
directly_measured: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_pontzer_arm_swing_2009, running_upper_body_rotation_energy_2023]
relationships:
  required_inputs: [running_pelvis_rotation, running_thorax_rotation, running_shoulder_rotation, running_pelvis_thorax_rotation, running_running_cycle]
  supports: [running_altered_rotational_coordination, running_cross_body_coordination]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 17
hub_score: 28
centrality: 0.152
updated: 2026-09-09
---

# Running - Rotational Coupling

## Definition

A derived description of timing, relative phase, and repeatability among pelvis, thorax, shoulder, arm, and leg proxy signals.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_pelvis_rotation]]
- [[running_thorax_rotation]]
- [[running_shoulder_rotation]]
- [[running_pelvis_thorax_rotation]]
- [[running_running_cycle]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_altered_rotational_coordination]]
- [[running_cross_body_coordination]]

## What It Cannot Prove

Greater or smaller coupling is not automatically better and does not diagnose restriction.

## Literature Evidence

- [[running_preece_spine_pelvis_2016]]
- [[running_pontzer_arm_swing_2009]]
- [[running_upper_body_rotation_energy_2023]]

## Reporting Language

Permitted: "Pelvis-thorax proxy coupling was less repeatable during right support phases."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
