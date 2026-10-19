---
id: running_rotational_reversal
canonical_id: running.rotation.reversal
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Rotational Reversal
aliases: [Rotational Reversal]
domain: running
directly_measured: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016]
relationships:
  required_inputs: [running_pelvis_rotation, running_thorax_rotation, running_shoulder_rotation, running_running_cycle]
  supports: [running_rotational_coupling, running_altered_rotational_coordination, running_fatigue_drift]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 13
hub_score: 17
centrality: 0.116
updated: 2026-09-09
---

# Running - Rotational Reversal

## Definition

The event time at which a smoothed, quality-gated rotational proxy changes direction.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_pelvis_rotation]]
- [[running_thorax_rotation]]
- [[running_shoulder_rotation]]
- [[running_running_cycle]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_rotational_coupling]]
- [[running_altered_rotational_coordination]]
- [[running_fatigue_drift]]

## What It Cannot Prove

A reversal proxy does not measure angular momentum, torque, or spinal segment motion.

## Literature Evidence

- [[running_preece_spine_pelvis_2016]]

## Reporting Language

Permitted: "Thorax-proxy reversal occurred later in right support than in comparable left support cycles."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
