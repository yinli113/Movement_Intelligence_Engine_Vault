---
id: squat_stance_foot_context
type: Movement Pattern
preferred_name: "Squat Stance and Foot Context"
domain: squat
evidence_level: 4
source_role: applied_clinical_biomechanics_commentary
relationships:
  supported_by: [straub_powers_squat_biomechanics_2024]
  connects_to: [bodyweight_squat, ankle_dorsiflexion, squat_trunk_tibia_relationship, squat_myofascial_mapping, squat_article_app_contract]
confidence: medium
review_status: source_checked_app_translation_unvalidated
relationship_count: 6
hub_score: 8
centrality: 0.053
updated: 2026-10-28
---

# Squat Stance and Foot Context

## Source-grounded concept

[[straub_powers_squat_biomechanics_2024]], “Stance Width”: narrow = 75–100%, medium = 100–150%, wide = 150–200% of shoulder width. Sagittal moment findings conflict. “Foot Rotation” describes plane-dependent loading effects, not a universal optimal toe angle: compared with 0° (toes straight forward), rotating the feet outward to 30° has minimal effect on sagittal plane moments, decreases external knee valgus moment by approximately 50%, and increases knee varus moment by approximately 80%. “Tibia Inclination” distinguishes heel elevation from increased ankle dorsiflexion.

## App translation — Level 5 engine synthesis

The existing [[bodyweight_squat]] app convention calls a projected ankle/shoulder ratio >1.0 wide. Keep its name and provenance separate from the article taxonomy; do not silently replace the user-defined convention. The paper’s interval endpoints overlap and do not define exhaustive software bins. Preserve raw ratios and measurement definitions before any future bin conversion.

For optional manual ETL setup context (`dim_video_set_condition`), self-reported categorical setup options record stance width relative to shoulder width (`narrower_than_shoulders`, `equal_to_shoulders`, `wider_than_shoulders`) and left/right foot toe-angle categories relative to straight ahead (`toes_forward` ~0°, `moderate_turn_out_up_to_30` 1°–30°, `wide_turn_out_over_30` >30°, `toes_inward` <0°), anchored to the 0° vs. 30° benchmark in [[straub_powers_squat_biomechanics_2024]] while retaining left/right separation for asymmetrical foot flare context in [[squat_myofascial_mapping]]. Label these explicitly as self-reported task-context categories: they are not camera ratios, research stance percentages, passive hip rotation measurements, or movement-quality score modifiers.

Projected ankle separation is not automatically equivalent to a research stance-width measurement. Camera yaw, foot rotation, stance landmarks and shoulder projection can change the ratio. Foot direction cannot establish hip external rotation, tibial rotation, pressure distribution or compartment loading.

Record footwear, wedges, deliberate heel elevation and spontaneous heel rise separately. A wedge retest changes task mechanics; improvement does not confirm a soleus, Achilles or fascial restriction. Passive range and tissue findings require direct assessment.

## Relationships

| Node | Relationship | Evidence boundary |
|---|---|---|
| [[bodyweight_squat]] | Existing stance convention | App definition, not source taxonomy |
| [[ankle_dorsiflexion]] | Possible contributor to forward shin motion | Not a passive-range measurement |
| [[squat_trunk_tibia_relationship]] | Combined sagittal context | Avoid isolated shin inference |
| [[squat_myofascial_mapping]] | Optional anatomical hypotheses | Article supplies no line-specific evidence |
| [[squat_article_app_contract]] | App implementation handoff | No automatic scoring change |


## Set-condition SCD2 extension — 2026-10-28

Level 5 app translation: `video-context/1.4.0` adds optional self-reported
`footwear_category` (barefoot, socks, flat shoes, heeled lifting shoes, other shoes),
`heel_wedge_category` (no separate wedge, both heels, left only, right only), and
`external_load_kg` (total external mass, excluding body mass; explicit 0 means
unloaded). These belong in `dim_video_set_condition` alongside stance and toe
angles. Hip IR/ER and ankle knee-to-wall remain independent measured entries in
`dim_video_mobility_screen`. Missing values stay null, including migrated rows;
never infer footwear, wedge or load from video. Separate wedges are independent
of built-in shoe heels and observed heel rise. Changed recorded conditions create
a new person-scoped SCD2 version; unchanged entries reuse their key and earlier
run links stay unchanged. Enter context for the selected recordings, not a
verified capture-time history. Matching entries do not verify task equivalence or
explain symptoms. Streamlit entry is under **Setup & context**. No new charts or
clinical interpretation are part of this extension.
