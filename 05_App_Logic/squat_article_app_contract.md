---
id: squat_article_app_contract
type: App Logic
preferred_name: "Squat Article-to-App Evidence Contract"
domain: squat
evidence_level: 5
source_role: engine_synthesis
relationships:
  supported_by: [straub_powers_squat_biomechanics_2024]
  connects_to: [bodyweight_squat, squat_trunk_tibia_relationship, squat_stance_foot_context, squat_depth_context, squat_observability_boundary, squat_spinal_loading_correspondence_2026]
confidence: medium
review_status: source_checked_app_translation_unvalidated
relationship_count: 10
hub_score: 15
centrality: 0.088
updated: 2026-10-08
---

# Squat Article-to-App Evidence Contract

## Purpose and status

This is the canonical retrieval and future implementation contract for [[straub_powers_squat_biomechanics_2024]]. It is a vault knowledge addition, not a claim that the running app consumes these new notes. Numeric evidence levels here follow [[evidence_levels]]; the article’s own Level 5 and the vault’s Level 4 classification are different systems.

## Retrieval graph

[[bodyweight_squat]] → [[straub_powers_squat_biomechanics_2024]] → [[squat_trunk_tibia_relationship]], [[squat_stance_foot_context]], [[squat_depth_context]] → [[squat_observability_boundary]]. For spinal interpretation, also retrieve [[squat_spinal_loading_correspondence_2026]]. Optional line interpretations remain [[squat_myofascial_mapping]] engine synthesis.

## Claim contract

| Claim class | Required provenance | Allowed use |
|---|---|---|
| Source statement | Source ID, named section/figure, source role | Describe what the commentary proposes |
| Camera observation | Frame/time, view, geometry, quality and protocol | Report image-plane movement |
| Strategy interpretation | Observation plus source anchor and transfer limitations | Qualified apparent strategy |
| Muscle/line hypothesis | Explicit engine_synthesis plus competing explanations | Assessment question only |
| Clinical prescription | Independently established clinical context and clinician assessment | Not generated from appearance alone |

Store the measured value separately from its interpretation. Preserve `unavailable_from_this_view` when geometry is unsupported. No source category becomes an injury-risk threshold, normality score, weakness diagnosis, force estimate or treatment recommendation.

## Existing-knowledge conflicts to keep visible

The existing `squat_knowledge.v1.json` contains a heel-wedge retest statement claiming confirmation of a distal SBL/Achilles block. This paper cannot establish that causal inference. A wedge changes the task and any response has multiple explanations.

The existing [[knee_to_toe_progression_boundary]] attributes large numerical load changes and fascial stress interpretations to multiple sources. This ingestion does not verify those numbers, tissue labels or attributions. Do not propagate them as findings of this article; review their primary sources separately.

These are recorded provenance gaps, not silently certified by adding the article. Existing runtime JSON and app behaviour have not been changed in this vault-only ingestion.

## Future app acceptance checks

- Preserve the user-defined stance convention separately from the paper’s stance taxonomy.
- Verify angle reference/sign, aspect ratio, selected side and simultaneous sampling at peak knee flexion.
- Treat near-boundary uncertainty and missing data explicitly; neither is a normal result.
- Do not infer lumbar curvature from a shoulder–hip segment.
- Do not infer passive ankle restriction or tissue causality from heel rise or a wedge response.
- Preserve clinical and spinal disagreements in retrieval; suppress unsupported causal wording.
- When implementing, change canonical JSON first, then use the supported knowledge synchronization command and verify both runtime copies. This note does not itself release new runtime thresholds.
