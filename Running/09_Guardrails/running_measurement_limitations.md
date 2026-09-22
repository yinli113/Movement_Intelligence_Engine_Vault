---
id: running_measurement_limitations
canonical_id: running.guardrail.measurement_limitations
type: App Logic
running_node_type: guardrail
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Measurement Limitations
aliases: [running camera limitations]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: []
relationships:
  governs: [running_event_detection, running_body_centre_proxy, running_pelvis_rotation, running_thorax_rotation, running_foot_strike]
  connects_to: [running_kinematics_are_not_kinetics, running_reporting_guardrails, running_evidence_gate]
confidence: high
review_status: canonical
relationship_count: 49
hub_score: 97
centrality: 0.438
updated: 2026-09-09
---

# Running - Measurement Limitations

## Camera Contract

- Side view is preferred for sagittal timing, landing, progression, trunk lean, and compression proxies.
- Front/back views are preferred for frontal asymmetry and selected rotation proxies.
- Monocular transverse rotation is a proxy: `is_rotation_proxy: true`, `true_3d_rotation: false`.
- Suppress outputs affected by occlusion, foreshortening, an uncertain contact frame, poor calibration, or unreliable landmark confidence.
- Never invent or interpolate across a quality-gate failure without retaining that failure in provenance.

## Terminology

A hip midpoint is a [[running_body_centre_proxy|body-centre proxy]], not whole-body COM. Foot-strike classification is estimated and view/frame-rate dependent.

## Required Output Fields

`value, unit, view, valid_samples, confidence, quality_flags, algorithm_version`.

## Relationships

Applies to all measurements in [[running_canonical_measurement_contract]] and is enforced by [[running_evidence_gate]].
