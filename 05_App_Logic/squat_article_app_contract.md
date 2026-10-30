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

## Resolved evidence conflicts — 2026-10-28

The reviewed canonical notes and export v1.4.0 withdraw wedge-confirmed tissue blocks, deterministic switch failures and automatic muscle-state/prescription fields. Wedge responses remain task responses with competing explanations. Existing saved reports are not rewritten.

The knee-to-toe note now preserves Fry's measured hip/knee torque outcomes and loaded protocol; it does not substitute lumbar shear or fascial stress. The Wilke source now separates anatomical continuity from functional transmission, and the Rajagopal source preserves its walking/running validation scope. The Kuljian note separates source discussion from withdrawn camera/IMU classifiers. None validates onset thresholds or clinical event labels.

## Future app acceptance checks

- Preserve the user-defined stance convention separately from the paper’s stance taxonomy.
- Verify angle reference/sign, aspect ratio, selected side and simultaneous sampling at peak knee flexion.
- Treat near-boundary uncertainty and missing data explicitly; neither is a normal result.
- Do not infer lumbar curvature from a shoulder–hip segment.
- Do not infer passive ankle restriction or tissue causality from heel rise or a wedge response.
- Preserve clinical and spinal disagreements in retrieval; suppress unsupported causal wording.
- When implementing, change canonical JSON first, then use the supported knowledge synchronization command and verify both runtime copies. This note does not itself release new runtime thresholds.


## Plain-language chart summaries and competing explanations — 2026-10-29

Consumer dashboard contract v1.1.0 (knowledge v1.9.0) adds short descriptions of
complete average curves. Describe start/bottom/finish relationships or the phase
containing the largest absolute departure from standing. These are coarse shape
descriptions, not monotonicity, sustained-onset, repetition-persistence, abnormality
or anatomical left/right claims. Zero curves do not generate movement claims.

Optional explanations require an existing gated persistent finding in the same
view. For a trunk-lean finding, consider a hip-oriented strategy using
[[squat_trunk_tibia_relationship]], with ankle–foot/setup as a competing assessment
question using [[squat_stance_foot_context]]. Keep the observed relationship,
source mechanism, personal hypothesis and distinguishing assessment separate.
The source is [[straub_powers_squat_biomechanics_2024]], particularly Tibia
Inclination and Knee vs. Hip Extensor Biased Squatting; application to the person
is Level 5 engine synthesis. Do not rank causes, infer calf tightness, assign
measured loading, infer symptoms or generate treatment. A wedge response alone
cannot identify restricted tissue. No front hypothesis is generated merely from
an average sideways offset. Public evidence names literature, not vault paths.
No external LLM calls or new measurements are introduced.


## Optional Squat Gemini explanation — 2026-10-29

Knowledge v1.10.0 adds `squat-explanation/1.0.0` as an opt-in Streamlit explanation
layer. Reuse Running's allowlisted evidence, curated retrieval and provider
separation, with squat-specific gates. A local packet reconstructs only
average-shape anchors/counts, supported repeated findings and their eligible
curated hypotheses/source reasoning. Independent views remain separate. No
video, raw landmarks, capture/person identifiers, timestamps, SCD2 screens or
user notes are sent. A preview shows the exact packet before explicit Generate.

Generated prose references supplied observation and eligible hypothesis IDs.
Attach original observations, public literature metadata and curated
distinguishing checks independently of model wording. Format, reference and
conservative language checks are not semantic or clinical validation. Reject
unknown references, numerical/causal/tissue/prescription claims, links and HTML.
Retain model, prompt/evidence/knowledge provenance and label output unverified.
Errors never replace the deterministic report. A password key stays in local
Streamlit session memory or server environment (`SQUATS_GEMINI_API`), never ETL,
files, model prompts or exports. No call on page load or key entry. This release
uses a mocked provider for verification; no real credential or live generation
is required. No deployment or chat agent is part of this addition.
