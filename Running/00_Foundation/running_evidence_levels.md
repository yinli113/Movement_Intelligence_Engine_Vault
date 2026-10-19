---
id: running_evidence_levels
canonical_id: running.foundation.evidence_levels
type: App Logic
running_node_type: guardrail
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Evidence Levels
aliases: [running evidence levels, running claim ladder]
domain: running
directly_measured: false
camera_views: []
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: []
relationships:
  governs: [running_canonical_measurement_contract, running_reporting_guardrails, running_measurement_limitations, running_evidence_gate]
  connects_to: [evidence_levels, running_kinematics_are_not_kinetics]
confidence: high
review_status: canonical
relationship_count: 8
hub_score: 12
centrality: 0.071
updated: 2026-09-09
---

# Running - Evidence Levels

## Definition

This note defines the running-domain claim ladder without replacing the vault-wide [[evidence_levels|Evidence Hierarchy Specification]].

| Running claim level | Meaning | Vault evidence mapping |
|---|---|---|
| A | Camera-derived measurement or explicitly named proxy that passed its quality gate | Level 5 app logic, unless independently validated |
| B | Pattern derived from multiple valid Level A observations | Level 5 app logic |
| C | Biomechanical interpretation supported by literature and measurements but not directly observed as force or tissue state | Usually Level 5 interpretation informed by Level 3 literature |
| D | Myofascial hypothesis | Level 5 hypothesis informed by Level 1 Anatomy Trains framework |

The letters govern **claim distance from the video**. The numeric hierarchy governs **source role and evidence provenance**. Both fields must be retained.

## Evidence Chain

`literature -> measurement definition -> derived movement pattern -> biomechanical interpretation -> myofascial hypothesis -> reporting language`

No arrow proves causation. If a required link is absent, the downstream claim is unavailable.

## Relationships

- Governs [[running_canonical_measurement_contract]], [[running_reporting_guardrails]], and [[running_evidence_gate]].
- Defers source hierarchy to [[evidence_levels]].
- Enforces [[running_kinematics_are_not_kinetics]].

## App Use

Return the claim level, source nodes, view, valid sample count, confidence, and algorithm version with every output.

## Open Questions

- Which Level A proxy implementations will receive independent validation and therefore qualify for a stronger numeric evidence assignment?
