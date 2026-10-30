---
id: running_event_detection
canonical_id: running.events.detection
type: Movement Pattern
running_node_type: event
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Event Detection
aliases: [Event Detection]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [till_yes_running_literature_foundation]
relationships:
  parent_concepts: []
  child_concepts: [running_initial_contact, running_midstance, running_maximum_compression, running_toe_off, running_flight_phase]
  constrained_by: [running_measurement_limitations, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 10
hub_score: 19
centrality: 0.089
updated: 2026-09-09
---

# Running - Event Detection

## Definition

The quality-gated process that identifies running-cycle event frames from pose/video signals.

## Why It Matters

Reliable event boundaries are prerequisites for downstream timing, landing, compression, and multi-stride calculations.

## Observable Inputs

Foot/ankle trajectories, body-centre-proxy motion, ground-plane relationship, and monotonic timestamps.

## Camera and Quality Gate

Side view is preferred. Require event-order plausibility, temporal separation, side assignment, and confidence; retain manual-review and unavailable states. Apply [[running_measurement_limitations]] and [[running_evidence_gate]].

## Supports

- [[running_initial_contact]]
- [[running_midstance]]
- [[running_maximum_compression]]
- [[running_toe_off]]
- [[running_flight_phase]]

## What It Cannot Prove

An event frame does not measure force, pressure, impulse, tissue loading, or injury risk.

## Reporting Language

Permitted: "Seven valid right contacts and six valid left contacts were detected; one uncertain event was excluded."

## Forbidden Claims

Do not describe ground reaction, braking, propulsion, or tissue state as measured from the event alone.

## Literature Evidence

- [[till_yes_running_literature_foundation]]


## Website pilot release rule — 2026-10-20

The website pilot retires horizontal foot-extremum contact inference. Local image-ground-band transitions may generate exploratory candidates only: require sustained height evidence, continuous source samples and no detected limb-label swap. These conditions are engineering heuristics, not camera-validated contact identification. Candidates and detector scores do not establish ground contact.

User-approved revision: automatic source-frame candidates may drive preliminary website timing, landing and phase estimates without manual confirmation. Manual correction remains optional; automatic support and contact are estimates, not independently validated observations. All panels share the same sequence/stride eligibility rule; review edits rebuild derived outputs. Missing or ambiguous boundaries remain unavailable. Keep a source-frame marking and removal path because review cannot be limited to accepting detector suggestions.

Uploaded capture uses a fixed 30 Hz media-time grid, not inferred native FPS. Wait for decoded seeks, stop on abort/decode failure, retain source timestamps, and distinguish analysis samples from independent source frames. The running-woman regression contains 247 decoded source frames; earlier website capture emitted 756 analysis samples and a 12 ms false stance. A narrow replay regression guards against that failure and does not validate the replacement detector.

The provisional geometry policy is stored in `running_measurement_quality.v1.json` (source-pixel resolution, in-frame requirements and camera-conflict review). Thresholds are Level 5 engineering settings and remain unvalidated against independent camera measurements. Preserve rejected raw values and reasons.


## Feature-specific movement intervals — 2026-10-22

Retain an ordered same-leg contact → single toe-off → next same-leg contact interval for exploratory knee/trunk range and arm–opposite-thigh movement comparisons even when the opposite-foot contact sequence is incomplete. Keep unique boundaries, broad duration integrity and all existing landmark/coverage checks. Call these estimated movement intervals, not complete timing cycles; missing opposite events are not inferred. They must never enter cadence, contact/flight summaries, timing charts, ballistic estimates or the strict timing audit. Strict bilateral timing eligibility remains unchanged. Export both sets with source event provenance. Rebuild these intervals from saved events without requiring a new video capture.

Do not recommend repeating analysis to obtain a higher coordination score: fixed-grid decoded capture already covers the clip; shader warm-up or a converged score does not validate physical mechanics or millisecond accuracy.
