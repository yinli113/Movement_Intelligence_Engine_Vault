---
id: running_evidence_gate
canonical_id: running.guardrail.evidence_gate
type: App Logic
running_node_type: guardrail
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Evidence Gate
aliases: [running interpretation gate]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: []
relationships:
  governs: [running_longer_landing_strategy, running_altered_rotational_coordination, running_cross_body_myofascial_hypothesis]
  connects_to: [running_measurement_limitations, running_reporting_guardrails, running_variability]
confidence: high
review_status: canonical
relationship_count: 52
hub_score: 104
centrality: 0.464
updated: 2026-09-09
---

# Running - Evidence Gate

## Level A Gate

Require the declared camera view, event confidence, landmark confidence, usable scale/normalisation where required, and an algorithm version.

## Level B Gate

Require multiple valid strides, aggregation statistics, persistence, and the Level A inputs named by the pattern.

## Level C Gate

Require either one strong direct measurement plus relevant context or multiple mutually supporting A/B findings, sufficient confidence, and literature whose scope matches the interpretation.

## Level D Gate

Require a supported Level C interpretation, a repeated pattern rather than one noisy frame, explicit hypothesis wording, and `requires_clinical_correlation: true`.

## Failure State

If any gate fails: "Insufficient reliable evidence to interpret this feature." Preserve the reason and do not force an answer.
