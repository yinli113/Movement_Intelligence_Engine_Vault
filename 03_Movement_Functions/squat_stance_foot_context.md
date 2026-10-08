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
updated: 2026-10-08
---

# Squat Stance and Foot Context

## Source-grounded concept

[[straub_powers_squat_biomechanics_2024]], “Stance Width”: narrow = 75–100%, medium = 100–150%, wide = 150–200% of shoulder width. Sagittal moment findings conflict. “Foot Rotation” describes plane-dependent loading effects, not a universal optimal toe angle. “Tibia Inclination” distinguishes heel elevation from increased ankle dorsiflexion.

## App translation — Level 5 engine synthesis

The existing [[bodyweight_squat]] app convention calls a projected ankle/shoulder ratio >1.0 wide. Keep its name and provenance separate from the article taxonomy; do not silently replace the user-defined convention. The paper’s interval endpoints overlap and do not define exhaustive software bins. Preserve raw ratios and measurement definitions before any future bin conversion.

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
