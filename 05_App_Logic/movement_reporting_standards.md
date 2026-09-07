---
id: movement_reporting_standards
type: App Logic
preferred_name: Movement Reporting Standards
aliases: [reporting philosophy, report language rules, movement report standards]
category: App Logic
short_definition: "Reporting philosophy that forbids value-laden labels (good, bad, correct, perfect, dysfunctional) without a clinical or safety reason, and structures every report around what happened, when, how segments coordinated, repeatability, meaning, re-measurement, and the limits of the data."
evidence_level: 5
evidence:
  - source_id: czaprowski_nonstructural_posture_2018
    evidence_level: 1
    supports: "Movement and posture are questions about individual organisation, not deviations from an ideal — the philosophical basis for non-judgmental reporting."
relationships:
  parent_concepts: [evidence_levels]
  child_concepts: []
  related_concepts: [metric_evidence_classification, personalised_movement_intelligence, myofascial_interpretive_layer, golf_kinetics_observability_boundary, energy_flow]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 7
hub_score: 10
centrality: 0.063
updated: 2026-07-27
---

# Movement Reporting Standards

## Definition

Reports describe movement; they do not judge it. Labels such as **good, bad, correct, incorrect, perfect,** and **dysfunctional** are avoided unless there is a clearly defined clinical or safety reason.

## Preferred Vocabulary

| Use | Instead of |
| :--- | :--- |
| movement strategy | good/bad technique |
| observed pattern | correct/incorrect form |
| asymmetry | imbalance (as a flaw) |
| timing difference | late/early fault |
| reduced or increased range | tight/restricted (as a verdict) |
| possible compensation | dysfunction |
| individual variation | deviation from ideal |
| consistency | repeatability judged against self |
| adaptability | ability to vary strategy |
| confidence-limited observation | a finding stated beyond the data |

## Every Report Answers Seven Questions

1. **What happened?** — the observed descriptors;
2. **When did it happen?** — timing on the event/normalised axis;
3. **How did the segments coordinate?** — sequence and transition behaviour;
4. **Was the movement smooth and repeatable?** — continuity and trial-to-trial consistency;
5. **What might the pattern mean?** — cautiously labelled interpretation;
6. **What can be measured again after practice?** — concrete re-assessment metrics;
7. **Which conclusions cannot be made from the available data?** — explicit limits.

## Why It Matters

Value-laden labels push users toward copying an ideal and away from discovering their own effective pattern ([[personalised_movement_intelligence]]). Stating the seventh question — what the data *cannot* say — is what keeps reports honest.

## Governing Rules

Reports inherit every metric's claim type and confidence from [[metric_evidence_classification]], apply the allow-lists and prohibited inferences of [[golf_kinetics_observability_boundary]], and use the cautious myofascial wording of [[myofascial_interpretive_layer]]. No report diagnoses, prescribes treatment, or implies injury risk from camera descriptors.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[evidence_levels]] | Reporting strength follows the hierarchy. |
| inherits_types_from | [[metric_evidence_classification]] | Each metric keeps its claim type. |
| serves | [[personalised_movement_intelligence]] | Language supports self-discovery. |
| enforces | [[myofascial_interpretive_layer]] | Cautious fascial wording in output. |
| bounded_by | [[golf_kinetics_observability_boundary]] | Golf allow-list and prohibitions. |

## Parent Concepts

- [[evidence_levels]]

## Child Concepts

- None currently.

## Related Concepts

- [[energy_flow]]
- [[temporal_movement_metrics]]

## Evidence Level

Level 5 app policy, grounded in the Level 1 clinical philosophy that movement is a question, not a verdict.

## App Use

Lint report text for forbidden labels; require the seven-question structure; attach claim types and confidence to every stated metric; end each report with the explicit limits of the available data.

## Open Questions

- Should forbidden-label detection be an automated lint stage in the report pipeline with a clinician-override list?
- What is the clearest plain-language template for the "cannot conclude" section for consumer users?
