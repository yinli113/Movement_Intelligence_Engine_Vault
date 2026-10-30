---
id: running_variability
canonical_id: running.variability.stride_to_stride
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Variability
aliases: [Variability]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_zandbergen_fatigue_2023, running_trowell_fatigue_2025, running_winter_fatigue_2017]
relationships:
  required_inputs: [running_running_cycle, running_cadence, running_contact_time, running_landing_relationship, running_evidence_gate]
  supports: [running_fatigue_drift, running_left_right_asymmetry]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 33
hub_score: 62
centrality: 0.295
updated: 2026-09-09
---

# Running - Variability

## Definition

Within-trial stride-to-stride dispersion and structure for a named Level A metric.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_running_cycle]]
- [[running_cadence]]
- [[running_contact_time]]
- [[running_landing_relationship]]
- [[running_evidence_gate]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

side or front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_fatigue_drift]]
- [[running_left_right_asymmetry]]

## What It Cannot Prove

Variability is not automatically error or dysfunction; it may reflect biology, fatigue, task change, or measurement noise.

## Literature Evidence

- [[running_zandbergen_fatigue_2023]]
- [[running_trowell_fatigue_2025]]
- [[running_winter_fatigue_2017]]

## Reporting Language

Permitted: "Contact-time proxy varied by 9 ms SD across ten valid right stances."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?

## Website Gold recovery pilot — 2026-10-20

Gold means prepared movement evidence, not validated clinical truth. The first website slice uses one recording: retain own-foot swing intervals, observed maxima, peak location only where covered, per-phase support and left/right pair identities. Keep partial observations rather than rejecting an entire video. Investigate amplitude and timing separately; any bounded alignment must preserve the original curves. Compare identical pair sets under a higher-visibility subset and adjacent analysis-time boundary shifts. Failed checks limit the interpretation without erasing valid baseline observations. Keep source frames, units, event provenance and policy versions. Repetition counts concern intervals or pairs, never raw-frame counts. Thresholds and pairing/alignment methods are provisional engineering settings; repeatability or sensitivity alone does not validate tracking or establish injury, tissue state or optimal technique.
