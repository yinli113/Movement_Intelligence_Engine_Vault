# LLM-Wiki Operation Log

This is an append-only log of all operations performed on the Myofascial Lines vault.

---

## [2026-06-27] setup | Initialize Vault Structure
- Created folder directories: `raw/literature`, `raw/movements`, `wiki/concepts`, `wiki/mechanics`, `wiki/assessments`, `wiki/interventions`, and `wiki/sources`.
- Created `[[AGENTS]]` outlining the vault's design, YAML frontmatter conventions, and workflows.
- Initialized `[[index]]` note to map categories and links.
- Initialized this operation log (`[[log]]`).

## [2026-06-27] Ingest & Graph Setup | Julie Hammond PDF & Golf Swing Graph
- Ingested raw source `raw/literature/Julie Hammond Breakout.pdf` and wrote summary `[[julie_hammond_breakout]]`.
- Captured posture philosophy of ease, balance, resilience, and adaptability.
- Updated `[[AGENTS]]` to support the Movement Knowledge Graph paradigm.
- Built out a full functional slice of the graph for `[[golf_swing]]`:
  - Movements: `[[golf_swing]]` and its phase `[[golf_swing_transition]]`.
  - Joint Mechanics: `[[hip_internal_rotation]]`.
  - Myofascial Lines: `[[functional_lines]]` and `[[deep_front_line]]`.
  - Muscles: `[[gluteus_maximus]]`.
  - Actionable Sheets: `[[glute_max_activations]]`, `[[glute_max_releases]]`, and `[[glute_max_tests]]`.
- Updated `[[index]]` note to link all new graph assets.

## [2026-06-27] Reorganization | Symmetrical Graph with Dedicated Joints and Lines
- Created dedicated directories `wiki/joints/` and `wiki/lines/` to make joints and lines first-class nodes in the vault.
- Moved existing line notes into `wiki/lines/` and removed the old `wiki/concepts/` folder.
- Updated `[[AGENTS]]` to define the new folder structure and templates.
- Created physical joint notes: `[[hip_joint]]`, `[[knee_joint]]`, and `[[ankle_joint]]`.
- Created new myofascial line note: `[[superficial_front_line]]`.
- Created new muscle note: `[[adductor_longus]]` (replacing the old grouped adductors note).
- Updated existing muscle notes (`[[gluteus_maximus]]`, `[[latissimus_dorsi]]`, `[[psoas_major]]`) and other concepts to build cross-links to joint notes.
- Updated `[[index]]` and `[[log]]` to catalog all changes.

## [2026-06-27] Comprehensive Generation | Thomas Myers Anatomy Trains Database
- Wrote and executed Python generator script `generate_anatomy_graph.py` to systematically build out the entire Anatomy Trains database.
- Created all **12 Myofascial Lines** in `wiki/lines/`.
- Created all **7 Physical Joints** in `wiki/joints/`.
- Created **59 Individual Muscle Cards** in `wiki/muscles/` (splitting up adductors, hamstrings, and erector columns).
- Fully cross-linked all notes dynamically to build the ultimate Movement Knowledge Graph.
- Updated `[[index]]` and `[[log]]` to catalog the 92 fully connected assets.

## [2026-06-27] Graph Refinement | Biomechanical Actions & Synergies Integration
- Re-ran the generation script to create **16 distinct biomechanical action notes** under `wiki/mechanics/` (such as `[[hip_extension]]`, `[[hip_internal_rotation]]`, `[[hip_adduction]]`, `[[elbow_flexion]]`, etc.).
- Connected each of the 59 individual muscles directly to its joint movements, replacing static text functions with dynamic wiki links.
- Set up the biomechanical action notes to dynamically scan and list their synergistic muscle groups and crossing myofascial lines.
- Cleaned up obsolete links and verified vault integrity.

## [2026-06-29] MVP Slice | Golf Movement Reasoning Sample
- Inspected the current vault structure and link health before adding new notes.
- Upgraded the requested sample notes for `[[functional_lines]]`, `[[spiral_line]]`, `[[superficial_back_line]]`, `[[hip_internal_rotation]]`, `[[thoracic_rotation]]`, and `[[golf_swing_transition]]`.
- Added only four missing golf-specific mechanics: `[[trail_shoulder_external_rotation]]`, `[[jaw_clenching]]`, `[[neck_tension]]`, and `[[toe_loading]]`.
- Linked the sample slice through `[[golf_swing_transition]]` to prove graph reasoning before integrating MediaPipe or generating more notes.

## [2026-06-29] Graph Conversion | Golf MVP Audit and Sample Nodes
- Created `[[Vault_Audit_and_Graph_Conversion_Plan]]` to document current vault problems, naming rules, proposed folder structure, node template, MVP nodes, limitation patterns, and conversion plan.
- Converted 10 sample notes into graph-style nodes with `id`, canonical `type`, `preferred_name`, `relationships`, `evidence`, `confidence`, and `review_status`.
- Used `raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf` as the main fascial-line reference and online standard anatomy references for basic shoulder, neck, and foot anatomy.
- Fixed two pre-existing broken links caused by an example link in `[[AGENTS]]` and raw PDF source metadata in `[[julie_hammond_breakout]]`.

## [2026-06-29] Source Summary | Thomas Myers Anatomy Trains
- Created `[[anatomy_trains_myofascial_thomas_w_myers]]` as a graph-style Evidence Source note for `raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf`.
- Stored a concise source summary focused on fascial-line relationships relevant to the golf movement MVP rather than a long textbook summary.
- Linked the source to `[[superficial_back_line]]`, `[[lateral_line]]`, `[[spiral_line]]`, `[[functional_lines]]`, `[[deep_front_line]]`, and `[[golf_swing_transition]]`.

## [2026-06-29] Graph Architecture v2 | Connective Structures and Hub Scores
- Added `Connective Structure` as a primary node type in `[[AGENTS]]`, including graph metric fields.
- Created `[[connective_structure_template]]` for new connective structure nodes.
- Created first-class connective structure nodes: `[[sacrotuberous_ligament]]`, `[[thoracolumbar_fascia]]`, `[[plantar_fascia]]`, `[[nuchal_ligament]]`, and `[[iliotibial_tract]]`.
- Linked connective structures into fascial-line and movement-reasoning nodes so force transmission can traverse through tissue structures, not only muscles.
- Added `scripts/update_graph_metrics.py` and calculated `relationship_count`, `hub_score`, and `centrality` across wiki graph nodes.
- Created `[[Connective_Structure_Hub_Report]]` with current hub rankings and candidate connective structures for the next conversion pass.

## [2026-06-30] Source Update | 3D Golf Decoded Six Phases Video Link
- Linked the primary YouTube source to `[[golf_decoded_six_phases_swing]]`: [On the Mark podcast / 3D Golf Decoded](https://www.youtube.com/watch?v=eDFQrVB2PXc&t=206s) (starts at 3:26).
- Updated `[[Six_Phases_Swing_Graph_Extraction]]` to list the video as the primary source artifact.

## [2026-06-30] Source Conversion | 3D Golf Decoded Six Phases
- Created `[[golf_decoded_six_phases_swing]]` as an Evidence Source node for the provided screenshot.
- Converted the six-phase model into graph interval nodes: `[[address_to_shaft_parallel]]`, `[[shaft_parallel_to_end_pelvis_rotation]]`, `[[end_pelvis_rotation_to_top_backswing]]`, `[[golf_swing_transition]]`, `[[max_unweighting_to_impact]]`, and `[[impact_to_hands_chest_height]]`.
- Added boundary-event nodes including `[[address_position]]`, `[[shaft_parallel_position]]`, `[[end_pelvis_rotation]]`, `[[top_backswing_position]]`, `[[max_unweighting]]`, `[[impact_position]]`, and `[[hands_chest_height_position]]`.
- Added reusable graph concepts: `[[movement_sequencing]]`, `[[force_transmission]]`, `[[energy_transfer]]`, `[[ground_reaction_force]]`, and `[[golf]]`.
- Created `[[Six_Phases_Swing_Graph_Extraction]]` with relationship tables, inferred relationships, and missing concept candidates.

## [2026-07-01] Spec | Fascial Movement Intelligence Governance
- Created `[[spec]]` in `00_Spec/` as the controlling specification for future vault work.
- Defined the evidence hierarchy from Anatomy Trains structure through AI app hypotheses.
- Documented the target numbered folder structure, required note fields, fascial line note requirements, golf phase note requirements, MediaPipe-readiness rules, and migration rules.
- Updated `[[AGENTS]]` to direct future agents to read `00_Spec/spec.md` before major graph changes.

## [2026-07-06] Source Extraction | Static-Posture BodyReading
- Created [[bodyreading_static_posture]] as an Assessment concept node capturing the Anatomy Trains method for reading fascial-line hypotheses from static standing posture, with the four descriptors (tilt, bend, rotation, shift) and the static-to-line reading (SFL/SBL balance, Lateral Line, Spiral Line, Functional Line, Deep Front Line core, foot/calcaneus, pelvic tilt-by-shift).
- Added Chapter 11 "Structural analysis" page-level evidence (pp.239-264) to [[anatomy_trains_myofascial_thomas_w_myers]].
- Linked the posture philosophy and BodyReading slides (pp.9-12, 16, 21) in [[julie_hammond_breakout]] to the new node.
- Purpose: align the vault with the static-posture app's `fascial_knowledge.json`, which attributes fascial lines from static stance as cautious hypotheses (not diagnosis).

## [2026-07-16] Integration | Dr Kwon Golfer-Ground Mechanics
- **Research scope and primary sources**: Converted the Dr Kwon research-program dossier into bounded Level 3 claims with source and sample anchors, while retaining the five-level evidence hierarchy.
- **New mechanics nodes**: Added [[golfer_ground_interaction_model]], [[pivoting_moment]], [[foot_contact_moment]], [[linear_impulse]], and [[angular_impulse]], preserving direct/residual foot-interface GRM as distinct from the combined-GRF frontal-plane/F-B-axis moment about COM.
- **Six-phase integration**: Connected the measured mechanics and conservative event crosswalk to the existing six source-defined golf phases without substituting unmatched events or inferring kinetics from video.
- **Myofascial-line integration and evidence boundary**: Kept myofascial lines as the primary anatomical structure and labelled mechanics-to-line mappings by evidence level rather than as measured tissue loading.
- **App observability safeguards**: Added [[golf_kinetics_observability_boundary]] as the authoritative allow-list separating instrumented kinetics, camera-observable descriptors, and Level 5 hypotheses; no diagnosis or treatment claims were added.
- **Verification performed**: Recalculated graph metrics, checked index and contextual backlinks, compared unresolved wikilinks with the four-target legacy baseline, searched for unsupported camera-kinetics or fascial claims, and ran diff, status, and repository-scope checks.

## [2026-07-22] Spec | Generalize Evidence Hierarchy to Cross-Domain Foundational Frameworks
- Revised `[[evidence_levels]]`: Level 1 redefined as **Foundational Frameworks** (philosophy, terminology, observational logic, interpretation boundaries) — foundational to the engine's reasoning, *not* "highest-quality evidence" and *not* necessarily gold-standard biomechanics.
- Renamed Levels 2-4: L2 Domain Taxonomies & General Movement Models; L3 Domain-Specific Instrumented Biomechanics; L4 Applied Coaching/Clinical/Practice Frameworks (must never override L1-3 or upgrade a 2D proxy into a measured kinetic/causal claim).
- Added `source_role` field with values: foundational_anatomical_framework, foundational_clinical_philosophy, foundational_movement_framework, foundational_domain_taxonomy, domain_biomechanics, applied_practice.
- Updated "Current domain population" table: gait and static posture now have Level 1 foundations but still lack Level 3 instrumented sources (recorded as future domain-expansion, not MVP blockers); Gray Cook supports future squat/functional-movement modules but is not an instrumented squat-biomechanics source.
- Strengthened Content Separation Rule: a foundational source may define philosophy/terminology/taxonomy/observability limits but does not automatically support every measurement, causal interpretation, treatment, or report statement; claims must be traced to the specific source and source_role.
- Updated `[[index]]` to present the vault as a cross-domain movement-intelligence engine with the five Level 1 sources and the app philosophy ("How does your body organise movement?").

## [2026-07-22] Sources | Five Level 1 Foundational Source Notes
- `[[gray_cook_movement_2010]]` — evidence_level 1, source_role foundational_movement_framework (raw/literature/Movement.pdf).
- `[[chambers_sutherland_gait_analysis_2002]]` — evidence_level 1, source_role foundational_domain_taxonomy (raw/literature/A_Practical_Guide_to_Gait_Analysis.9.pdf).
- `[[czaprowski_nonstructural_posture_2018]]` — evidence_level 1, source_role foundational_clinical_philosophy, is_philosophy_source true (raw/literature/Non-structural misalignments of body posture in the sagittal plane.pdf).
- `[[anatomy_trains_myofascial_thomas_w_myers]]` — set evidence_level 1, source_role foundational_anatomical_framework.
- `[[julie_hammond_breakout]]` — set evidence_level 1, source_role foundational_clinical_philosophy.
- Renamed the three new source files so filename == id slug (vault convention).

## [2026-07-22] Concepts | Minimum Scaffold Stubs (status: scaffold)
- Movement/FMS (03_Movement_Functions): functional_movement_screen, selective_functional_movement_assessment, deep_squat, hurdle_step, inline_lunge, shoulder_mobility_reaching, active_straight_leg_raise, trunk_stability_pushup, rotary_stability, joint_by_joint_concept, performance_pyramid, movement_screening, movement_assessment, corrective_strategy, squat_assessment.
- Gait (03_Movement_Functions): gait_cycle, stance_phase, swing_phase, gait_cycle_events, gait_temporal_parameters, determinants_of_gait, gait_kinematics, gait_kinetics, gait_emg, foot_pressure, gait_energetics, gait_analysis, gait_assessment, observational_gait_analysis.
- Posture (03_Movement_Functions): lordotic_posture, kyphotic_posture, kyphotic_lordotic_posture, flat_back_posture, sway_back_posture, stabilizer_mobilizer_classification, local_stabilizers, global_stabilizers, mobilizers, hypoactivity, hyperactivity, head_line, base_line, sagittal_posture_types, posture_assessment, app_philosophy, corrective_exercise, muscle_length_strength_assessment.
- Future domain-expansion source stubs (00_Spec/sources, status: future_source, NOT yet in vault): kendall_muscles_testing_function, sahrmann_movement_impairment_syndromes, bergmark_lumbar_stability, richardson_lumbopelvic_stabilization, perry_burnfield_gait_analysis, whittle_gait_analysis.
- All 187 wikilinks across the Level 1 source notes, evidence_levels.md, and index.md now resolve to a vault node. Stubs are concise and marked status: scaffold; no detailed corrective protocols or unsupported muscle-by-muscle conclusions were created.

## [2026-07-22] Spec | Align Vault spec.md + Cross-Workspace Links to Generalized Hierarchy
- Aligned `00_Spec/spec.md` (Foundational Rules, Evidence Hierarchy table, source-role table) with the generalized `evidence_levels.md` (Level 1 = Foundational Frameworks; five Level 1 sources with source_role; Levels 2-4 renamed).
- Workspace-root docs updated to reflect cross-domain scope: `TillYes_Workspace/README.md` (§7.2 vault description, tree comment, "which folder" row, operating checklist), `ACTIVE_PROJECTS.md`, `NEW_COMPUTER_SETUP.md`, `scripts/bootstrap_new_computer.sh`.
- `tillyes_doc` evidence hierarchy aligned to the vault: `shared/terminology.md` (Evidence Level Hierarchy 1-5) and `MASTER_BIBLE.md` (Evidence Separation Philosophy table). `shared/clinical_principles.md` unchanged (uses app evidence-state tags, already consistent).
- Fixed stale `tillyes_apps/static_posture_app/config.yaml` `fascial_lines_path` (was pointing at non-existent old path) to the vault's current location; the app's only vault link is `fascial_knowledge.json`, which was not modified by the generalization.
- No app code changes required: the static_posture_app and movement_assessment apps do not reference evidence_levels, source_role, or the new concept nodes; their `evidence` field is the app's own Level-5 proxy vocabulary, already aligned with the observability boundary.

## [2026-07-22] Concepts | Reviewed Nodes Generated (37) + Orphan Cleanup
- Applied the refined Level 1 wording to `00_Spec/evidence_levels.md` (five foundational source groups described as foundational to the engine's reasoning, not equal in research design; `spec.md`/`terminology.md`/`MASTER_BIBLE.md` dependents already aligned).
- Deleted 17 superseded/out-of-scope orphan scaffolds from `03_Movement_Functions/`: gait_cycle_events, gait_analysis, gait_assessment, sagittal_posture_types, posture_assessment, app_philosophy, corrective_exercise, muscle_length_strength_assessment, head_line, base_line, local_stabilizers, global_stabilizers, mobilizers, movement_screening, movement_assessment, corrective_strategy, squat_assessment.
- Renamed `hypoactivity` -> `muscle_hypoactivity` and `hyperactivity` -> `muscle_hyperactivity` (old stubs deleted; new reviewed nodes created).
- Kept 7 directly-supported scaffolds for later upgrade: shoulder_mobility_reaching, joint_by_joint_concept, performance_pyramid, determinants_of_gait, gait_emg, foot_pressure, gait_energetics.
- Updated the three new Level 1 source notes (gray_cook_movement_2010, chambers_sutherland_gait_analysis_2002, czaprowski_nonstructural_posture_2018) frontmatter + body wikilinks to remove orphan-delete references and point to the new reviewed nodes.
- Generated 37 reviewed concept nodes (`status: reviewed`), each with frontmatter (node_type, status, domain, evidence_level, source_role, supported_by, directly_supported_claims, app_translation) and body sections (Definition, Why it matters, Source-derived model, Joint/Muscle involvement, Movement/phase relationships, Possible myofascial relationships, What a 2D app can observe, What the app must not infer, Related concepts, Sources, Evidence-separation rules A/B/C):
  - General movement (12): functional_movement_screen, selective_functional_movement_assessment, movement_vs_motion, movement_pattern, mobility_stability_relationship, regional_interdependence, deep_squat, hurdle_step, inline_lunge, active_straight_leg_raise, trunk_stability_pushup, rotary_stability.
  - Gait (14): gait_cycle, stance_phase, swing_phase, initial_double_limb_support, single_limb_stance, second_double_limb_support, initial_swing, midswing, terminal_swing, gait_temporal_parameters, observational_gait_analysis, gait_observability_boundary, gait_kinematics, gait_kinetics.
  - Static posture (11): non_structural_sagittal_posture, structural_vs_non_structural_posture, stabilizer_mobilizer_classification, muscle_hypoactivity, muscle_hyperactivity, apparent_shortness_vs_structural_shortening, lordotic_posture, kyphotic_posture, kyphotic_lordotic_posture, flat_back_posture, sway_back_posture.
- Discipline applied: every node separates (A) directly source-supported claims, (B) cross-links to other Level 1 sources, and (C) engine_synthesis/hypothesis (fascial-line mappings explicitly labelled as `engine_synthesis`). No node upgrades a 2D proxy to a measured kinetic/EMG/causal claim; each node states what a 2D app can observe and what it must not infer.
- Fixed one broken wikilink in the `kendall_muscles_testing_function` future-source stub (pointed at deleted `muscle_length_strength_assessment` -> repointed to `apparent_shortness_vs_structural_shortening`).
- `CONSISTENCY_MAP.md` already carries the MASTER_BIBLE §1 philosophy dependency (§1.1 row + change-log). Re-ran `scripts/check_consistency.sh`: checks 1-4 pass; check 5 = expected WARN (legacy anatomy_trains dual-identifier, documented); check 6 (wikilinks) verified clean via a standalone check — all vault wikilinks resolve to a node.

## [2026-07-24] Sources | Perry & Burnfield Eight-Phase Gait Taxonomy Elevated to Level 1
- Elevated `00_Spec/sources/perry_burnfield_gait_analysis.md` from `future_source` (evidence_level: null, source_role: domain_biomechanics) to **Level 1** `foundational_domain_taxonomy`, **framework-cited** via [[chambers_sutherland_gait_analysis_2002]] (which presents Perry's phase nomenclature, p.2 Table 2). The full Perry & Burnfield text is **not yet in the vault** (no PDF); the source note carries `status: reviewed`, `review_basis: framework_cited_via_chambers_sutherland`, `is_framework_cited: true`, and a prominent caveat. No page-locator claims are made against Perry & Burnfield directly; such claims are traced to Chambers & Sutherland (read in full) until the PDF is obtained.
- Perry & Burnfield **complements** Chambers & Sutherland (observational structure + observability boundary) as the gait domain's phase-taxonomy foundation. The gait domain now has **two** Level 1 sources with distinct roles.
- Added 5 eight-phase stance concept nodes (reviewed, supported_by perry_burnfield + chambers): `initial_contact`, `loading_response`, `mid_stance`, `terminal_stance`, `preswing`. The 3 swing phases (initial_swing, midswing, terminal_swing) already existed and were updated to add perry_burnfield to `supported_by` and note Perry's phase numbering (phases 6/7/8).
- Cross-linked the 3 coarser Chambers stance-period nodes (initial_double_limb_support, single_limb_stance, second_double_limb_support) to their Perry eight-phase equivalents (mapping notes).
- Updated Level 1 count 5 -> 6 across all dependents: `00_Spec/evidence_levels.md` (Level 1 table, source-groups section, domain-population table gait row + note), `00_Spec/spec.md` (Evidence Hierarchy Level 1 row + source-role table), `index.md` (Evidence Sources list), `tillyes_doc/shared/terminology.md` (Level 1 list), `tillyes_doc/MASTER_BIBLE.md` (Core Philosophy + Evidence Separation table), `TillYes_Workspace/README.md` §7.2.
- Cleaned the `whittle_gait_analysis` future-source stub: repointed stale `connects_to` slugs (gait_analysis/gait_assessment -> observational_gait_analysis/gait_cycle) and noted Perry & Burnfield is now Level 1 (Whittle remains future depth).
- Updated `CONSISTENCY_MAP.md`: §1.1 canonical wording (six Level 1 sources + framework-cited caveat), §1.3 Level 1 source ids (added perry_burnfield), §3 old-name trap (do not regress perry to "future_source" wording), change-log entry.
- Re-ran `scripts/check_consistency.sh`: checks 1-4 pass; check 5 = expected WARN (legacy anatomy_trains); check 6 (wikilinks) verified clean via standalone check — all vault wikilinks resolve to a node (one broken link to a non-existent `metatarsophalangeal_joint` node in `terminal_stance.md` was fixed by converting to plain text).

## [2026-07-26] Concepts | Gait–Myofascial Line Mapping (Engine Synthesis)
- Created `[[gait_myofascial_mapping]]` in `03_Movement_Functions/` as the engine synthesis hub mapping Anatomy Trains myofascial lines to the gait cycle. Built from the "Anatomy Trains in Gait" section by James Earls in Myers' *Anatomy Trains* (Ch. 10); `supported_by: anatomy_trains_myers_2009`; all line mappings are `engine_synthesis` (C), not measured kinetics.
- **Problem solved:** before this node, the vault graph had no edge from a gait observation to a fascial line. Line files linked to golf phases; every gait phase file's "Possible myofascial relationships" section read *"None directly. Fascial-line mapping is an engine synthesis (C)."* As a result, the movement_assessment app's AI agent could not reason from an observed gait restriction (e.g. restricted knee flexion) to a candidate fascial line — the only links that existed were golf-phase links.
- **Hub structure — three edge types** (so the agent can reason from what it actually sees in 2D video, not just from phase labels):
  1. Line → gait phase (which line does what, when).
  2. Line → motion-restriction pattern (reciprocal pairs: e.g. short SFL → restricted knee flexion; short SBL → restricted knee extension — with the counterintuitive note that tight hamstrings make knee flexion *easier*, not harder).
  3. Line → compensation signature (e.g. SFL restriction → hip hike / circumduction / vaulting / steppage as secondary LL/SPL/SBL overwork).
- Includes a worked example for restricted knee flexion (the case that prompted this work): primary line = [[superficial_front_line]] (rectus femoris biarticular link); secondary = [[spiral_line]] (rotational coupling); tertiary = [[deep_front_line]] (popliteus unlock), with disambiguation clues.
- **Line files updated** (added "Gait Role (Engine Synthesis, Level C)" section + `gait_synthesis -> [[gait_myofascial_mapping]]` relationship): [[superficial_front_line]], [[superficial_back_line]], [[lateral_line]], [[spiral_line]], [[deep_front_line]], [[back_functional_line]], [[front_functional_line]].
- **Gait phase/period files updated** (replaced "None directly" placeholder with synthesis links to the hub): [[gait_cycle]], [[stance_phase]], [[swing_phase]], [[initial_contact]], [[loading_response]], [[mid_stance]], [[terminal_stance]], [[preswing]], [[initial_swing]], [[midswing]], [[terminal_swing]], [[single_limb_stance]], [[initial_double_limb_support]], [[second_double_limb_support]]. The [[gait_observability_boundary]] was updated to point at the synthesis while keeping its restrictive wording (synthesis is for follow-up assessment only, not measured tissue loading from 2D observation).
- Non-gait "None directly" placeholders (deep_squat, hurdle_step, inline_lunge, FMS/SFMA nodes, posture nodes) were intentionally left unchanged — out of scope for this gait-focused work.
- Updated `index.md` to list `[[gait_myofascial_mapping]]` at the top of §03.
- No cross-repo propagation required: this is a new vault-internal synthesis node with no duplicated facts in `tillyes_doc`, `tillyes_web`, or `tillyes_apps/*`. The apps reference `fascial_knowledge.json` (unchanged); the new node is graph-internal for the movement_assessment AI agent's reasoning.

## [2026-07-26] Concepts | Gait–Myofascial View Observability (Edge Type 4)
- Extended `[[gait_myofascial_mapping]]` with a fourth edge type: **view → line observability**. Maps each gait camera view (side / front / back) to the fascial lines whose anatomical surface that view can see, and — critically — the lines each view is blind to.
  - **Side view** (sagittal plane) → observes [[superficial_front_line]], [[superficial_back_line]], (DFL sagittal only); blind to [[lateral_line]], [[spiral_line]] rotation, [[back_functional_line]], [[front_functional_line]], DFL medial arch.
  - **Front view** (frontal plane) → observes [[lateral_line]], [[deep_front_line]] (medial arch/adductors), [[spiral_line]] (upper counter-rotation + foot pronation), [[front_functional_line]] (shoulders); blind to SFL/SBL sagittal, BFL posterior.
  - **Back view** (posterior coronal + transverse) → observes [[back_functional_line]], [[lateral_line]] (glute med), [[superficial_back_line]] (calf/hamstring), [[spiral_line]] (posterior diagonal + heel); blind to SFL anterior, DFL deep, FFL anterior.
- Added two derived tables: view → restriction-pattern observability, and view → compensation observability (combining edge type 4 with edge types 2 and 3).
- Added the **single-view blind-spot rule**: a side-only report can only reason about SFL/SBL; it is blind to LL/DFL/BFL/most SPL. A side-only "no restriction observed" must not be reported as "no LL/DFL/BFL/SPL restriction" — those lines were not visible from the view. The app must declare `unavailable_from_this_view` for lines outside the view's observability, not `absent`. This is the view-side observability boundary that complements [[gait_observability_boundary]].
- Noted the **transverse-plane problem**: [[spiral_line]] is the transverse-plane line and is the hardest to capture from any single view. Practical approach is front + back together; a single side view will miss SPL restriction patterns even though SPL is "especially significant in gait."
- Updated the hub's `What a 2D app can observe` section to state view dependency explicitly.
- Added a **"Best observed from"** note to each of the 7 line files' Gait Role section: [[superficial_front_line]] (side), [[superficial_back_line]] (side), [[lateral_line]] (front + back), [[spiral_line]] (front + back together), [[deep_front_line]] (front), [[back_functional_line]] (back), [[front_functional_line]] (front).
- Fixed a content error introduced in the prior batch: `superficial_back_line.md` had accidentally received SFL Gait Role content (drives swing / knee flexion restriction). Corrected to SBL content (drives stance / hip extension / plantarflexion / restricted knee extension / flat-footed push-off).
- No cross-repo propagation required: still vault-internal synthesis. No facts duplicated to `tillyes_doc`, `tillyes_web`, or `tillyes_apps/*`.

## [2026-07-27] Spec | Gait–Myofascial Evidence Boundary Tightening
- **Trigger:** user questioned whether "forward head → restricted lumbar extension" is source-supported. Honest answer: NO — the source (Earls/Myers Ch.10) supports forward head → reduced SFL/DFL **elastic recoil** distally (box exercise), NOT forward head → restricted lumbar extension ROM. The prior batch's Whole-chain insight wording could be misread as implying spine-to-spine ROM propagation, which the source does not establish.
- **Whole-chain insight (hub):** retitled "spine → distal **elastic recoil**" (was "spine → distal symptom"). Reworded to state explicitly that the source supports **elastic recoil propagation** (cervical → distal recoil), NOT **range-of-motion propagation** (cervical → lumbar ROM). Added an inline "Evidence boundary — what the source supports vs what it does not" block separating (A) source-supported (DFL full-length tension at toe-off; forward head reduces elastic loading; small adjustment affects distant recoil) from (C) engine synthesis (the chain transmits elastic tension, not necessarily ROM at each segment; cervical fault can reduce distal recoil without restricting lumbar ROM).
- **Agent rule (hub):** retitled to clarify the candidate driver is a spine restriction reducing **elastic loading**, not a spine restriction causing distal ROM restriction.
- **Worked example (hub):** spine-driver differential reworded to "check the spine segments upstream for a restriction that could be reducing the DFL/SFL **elastic loading** (not necessarily the distal line's ROM)" and explicitly notes the source supports cervical/thoracic → distal elastic recoil, NOT cervical → lumbar ROM.
- **Edge type 2 (hub):** added an "Evidence boundary for the restriction-pattern table" note stating the source directly supports line membership + line gait roles; the restriction pairings are engine synthesis from line anatomy + fascial-reciprocal logic; the spine rows in particular — the source supports elastic-recoil propagation, NOT spine-to-spine ROM propagation.
- **New "Evidence boundary (A vs C, per edge type)" section (hub):** a table separating (A) source-supported from (C) engine synthesis for all four edge types (line→phase, line→restriction, line→compensation, view→observability). Includes an agent rule: label (A) for direct line-membership/line-gait-role claims, (C) for restriction pairings/compensations/view-observability; never report (C) as a measured finding; spine-to-spine ROM propagation must not be reported as established.
- **Line files (all 7):** expanded the "All mappings are engine_synthesis (C)" line in each Gait Role section to explicitly state the **phase role** is source-supported (Myers/Earls Ch.10 line gait roles) while the **restriction pattern** and **compensation signature** are engine synthesis from line anatomy + fascial-reciprocal logic, not enumerated in the source. Each links to [[gait_myofascial_mapping]] Evidence boundary.
- **SFL, SBL, DFL "Spine in gait" notes:** reworded to explicitly state the spine patterns are **independent local-segment patterns** from line anatomy (each caused by line shortness at that segment's point on the line), NOT a causal chain where one spine restriction causes another. The SFL and DFL notes now explicitly separate the elastic-recoil effect (source-supported) from the ROM-restriction implication (not supported). The SBL note now states the source does not establish SBL transmits ROM restrictions segment-to-segment.
- **Why this matters:** the movement_assessment app's AI agent must not report "forward head causes restricted lumbar extension" as a finding — that would be wrong guidance. The source supports "forward head reduces distal elastic recoil," which is a different and weaker claim. The vault now separates these explicitly so the agent cannot conflate them.
- No cross-repo propagation required: still vault-internal synthesis. No facts duplicated to `tillyes_doc`, `tillyes_web`, or `tillyes_apps/*`.

## [2026-07-27] Concepts | Gait–Myofascial Spine Mapping (Whole-Chain)
- Extended `[[gait_myofascial_mapping]]` to cover the spine joints (cervical, thoracic, lumbar), which were missing from the prior batch's edge type 2 table (it had been knee/hip/ankle/foot-centric because the knee-flexion case was the original prompt).
- **Edge type 2 (line → restriction pattern):** added 10 spine rows — cervical (neck rotation → SPL; neck extension/forward head → SFL/DFL; neck flexion → SBL), thoracic (extension → SBL/DFL; rotation → SPL/FFL; lateral flexion → LL), lumbar (extension → SFL/DFL; flexion → SBL; rotation → SPL/LL; shear/instability → DFL).
- **New "Whole-chain insight" subsection:** documents that the DFL tensions through its entire length at toe-off (toe extension → ankle DF → knee extension → hip extension/IR/abduction → thoracic extension → cervical balance). A restriction in any spine segment breaks the DFL elastic chain and produces a **distal symptom** — e.g. restricted knee flexion with a spine driver, not a primary SFL problem. Cites the Earls box exercise (forward head measurably reduced leg recoil with no hip flexor touched). Adds the **agent rule**: when a distal restriction is observed but the distal line looks fine on direct test, check the spine segments upstream before concluding the distal line is the driver. Links to [[regional_interdependence]].
- **Edge type 4 (view → observability):** added spine rows to both derived tables (view → restriction-pattern observability; view → compensation observability). Cervical rotation → front; forward head / cervical angle → side; thoracic extension/curve → side; thoracic rotation → front; thoracic lateral flexion → front + back; lumbar extension/curve → side; lumbar rotation → front; lumbar shear → front + back.
- **Worked example extended:** added a "Spine-driver differential" to the restricted-knee-flexion worked example — if knee flexion is restricted but the SFL looks fine on direct test, check thoracic extension (SBL/DFL) or forward head (SFL/DFL cervical) upstream before concluding SFL is the driver.
- **Line files updated** (added a "Spine in gait" note to the Gait Role section): [[superficial_front_line]] (cervical SCM, lumbar rectus abdominis), [[superficial_back_line]] (cervical nuchal/suboccipitals, thoracic/lumbar erector spinae), [[spiral_line]] (cervical splenii, thoracic rhomboid/serratus, lumbar obliques), [[deep_front_line]] (cervical longus colli, thoracic diaphragm, lumbar psoas/QL/TVA), [[lateral_line]] (thoracic intercostals, lumbar lateral obliques), [[front_functional_line]] (thoracic pectoralis/obliques). Each note links back to [[gait_myofascial_mapping]] Whole-chain insight where relevant.
- No cross-repo propagation required: still vault-internal synthesis. No facts duplicated to `tillyes_doc`, `tillyes_web`, or `tillyes_apps/*`.

## [2026-07-27] Spec | Gait–Myofascial Mapping — 12 Overreach Fixes (Grok Audit)
- **Trigger:** Grok audit of the gait–myofascial mapping flagged 12 OVERREACH findings where claims exceeded what the Anatomy Trains source (Myers/Earls Ch.10) actually supports. All 12 fixed in this batch.
- **#1/#2 SFL recoil assists knee flexion (contradicts source):** the SFL elastic-recoil pre-stretch assists **hip flexion** into swing, NOT knee flexion (knee flexion in swing is active hamstring + popliteus, not SFL recoil). Fixed in hub Whole-chain insight ("assists hip flexion" — dropped "AND knee flexion") and in `superficial_front_line.md` Phase role.
- **#3 Cervical elastic-recoil loss conflated with a "restricted knee flexion" driver:** the worked example's spine-driver differential presented cervical recoil loss as a knee-flexion-restriction driver. Reworded: the upstream issue is **reduced elastic loading** (source-supported, (A)), not distal ROM restriction; mechanism is loss of elastic contribution to hip flexion into swing, NOT cervical-causes-lumbar ROM restriction (unsupported).
- **#4 Restricted thoracic extension blamed on short SBL (reciprocal logic inverted):** SBL erector spinae crosses the POSTERIOR thoracic spine; short SBL resists thoracic **flexion** (holds thorax extended), NOT thoracic extension. Thoracic-extension restriction is an **SFL/DFL** (anterior line) pattern. Fixed in hub edge type 2 (split into "restricted thoracic extension → SFL/DFL" and "restricted thoracic flexion → SBL") and in `superficial_back_line.md` Spine in gait note.
- **#5 Short psoas "holds the lumbar in flexion":** short iliopsoas classically presents as **anterior pelvic tilt / lumbar lordosis (extension)**, NOT lumbar flexion. Removed psoas from the lumbar-extension-restriction row (now primary SFL rectus abdominis only) and added a separate "Lumbar lordosis / anterior tilt" row for short iliopsoas. Fixed in hub edge type 2 and in `deep_front_line.md` Spine in gait note.
- **#6 Steppage listed as compensation for "SFL can't flex knee":** steppage gait compensates for weak/inhibited dorsiflexors (SFL not firing) — the OPPOSITE problem to SFL restriction. Removed steppage from SFL compensation in hub edge type 3, `superficial_front_line.md`, `swing_phase.md`, and `initial_swing.md`; added an explicit note that steppage is NOT an SFL-restriction compensation.
- **#7 "Most significant" upgrades "especially significant":** Earls' actual wording is "especially significant in the dynamic anatomy of walking." Replaced "Most significant" with "especially significant" in hub edge type 1 and `spiral_line.md`.
- **#8 Edge type 1 Source column over-cites "Earls, Ch.10":** the gait-role column mixes Myers' planar Walking section, Earls' Anatomy Trains in Gait section, and the Perry-phase mapping (engine synthesis). Split the Source column into "(A) Myers Walking / Earls" for the role and "(C) Perry-phase mapping" for the phase IDs, with a header note that the source uses heel strike / weight acceptance / toe-off / swing, not Rancho phase names.
- **#9 "Loaded eccentrically" as Earls-supported SFL stance loading:** Earls' SSC framing is isometric muscle contraction + elastic fascial loading, not eccentric. Reworded to "anterior tissues lengthen / elastically load; muscle action is often isometric per Earls' SSC framing (not eccentric)" in hub edge type 1, hub worked example, and `superficial_front_line.md`.
- **#10 Catapult attributed to SBL alone:** Earls' catapult is multi-line (SBL + LL + DFL plantarflexors). Reworded to "Plantarflexors of the SBL **plus LL and DFL** load the catapult" in hub edge type 1 and `superficial_back_line.md`.
- **#11 Popliteus "unlocks the knee" imported as gait restriction mechanism:** Ch.10 gait text does not discuss popliteus; it is general DFL anatomy. Tagged the popliteus row and reference as "(C) general DFL anatomy (not Earls gait)" in hub edge type 2, hub worked example, and `deep_front_line.md`.
- **#12 Internal A/C contradiction (agent will pick the wrong rule):** the hub frontmatter/Why-it-matters said "three edge types" while the boundary table and edge type 4 implied four; the footer said "All three edge-type tables"; a "Myers/Ears" typo remained. Fixed: frontmatter short_definition and Why-it-matters now say "four edge types" and list view→observability; footer says "All four edge-type tables"; "Ears" → "Earls"; added inline "(C) engine synthesis" headers to edge type 2, 3, and 4 tables so the agent cannot miss the boundary.
- **Files touched:** `03_Movement_Functions/gait_myofascial_mapping.md` (hub), `01_Fascial_Lines/superficial_front_line.md`, `superficial_back_line.md`, `spiral_line.md`, `deep_front_line.md`, `03_Movement_Functions/swing_phase.md`, `initial_swing.md`.
- No cross-repo propagation required: still vault-internal synthesis. No facts duplicated to `tillyes_doc`, `tillyes_web`, or `tillyes_apps/*`.

## [2026-07-27] Spec | Gait–Myofascial Mapping — Composer 2.5 Follow-up Fixes
- **Trigger:** Composer 2.5 audit of the 12-fix batch found 10 additional issues — most importantly, **edge type 4 had not been brought in line** with fixes #4 and #6, plus reciprocal-logic errors and source-attribution stretches. All fixed in this follow-up batch.
- **Edge type 4 regression (the biggest miss):** the view→observability derived tables still carried the OLD thoracic-extension→SBL and steppage→SFL mappings that fixes #4 and #6 had removed from edge types 2 and 3. Fixed: "Restricted thoracic extension" row → SFL/DFL (matching edge type 2); "Restricted lumbar extension" row → SFL only (matching fix #5); added "Restricted thoracic flexion → SBL" and "Lumbar lordosis/anterior tilt → DFL" rows for parity with edge type 2. Steppage row in compensation-observability table reassigned to "(weak/inhibited dorsiflexors — NOT an SFL-restriction compensation; SFL not firing, opposite problem)".
- **Popliteus logic inversion (Findings 2, 3):** "knee locked from full extension (popliteus cannot unlock)" was framed as a shortness restriction, but a knee that cannot unlock from full extension is a popliteus **underactivity / failed-unlock** problem (short popliteus would bias toward flexion/IR, the opposite). Reframed in hub edge type 2 and `deep_front_line.md` as a DFL control-failure pattern, not a shortness restriction.
- **RA→anterior pelvic tilt co-finding error (Finding 8):** short rectus abdominis pulls toward lumbar/thoracic flexion and **posterior** pelvic tilt / reduced lordosis, not anterior tilt. Corrected the lumbar-extension-restriction row's co-finding to "Posterior pelvic tilt / reduced lumbar lordosis (from RA pull)".
- **SFL recoil "assists toe-off" (Finding 4):** toe-off propulsion is the multi-line catapult (SBL+LL+DFL); SFL recoil assists **swing initiation**. Reworded the SFL edge type 1 row to split the two.
- **"Seven primary gait drivers" (Finding 5):** Ch.10 does not rank seven lines as primary. Reframed as "(C) vault prioritization of the most gait-relevant lines for this synthesis."
- **Whole-chain knee-flexion anchor (Finding 9):** the whole-chain insight anchored on "restricted knee flexion," re-conflating hip-recoil loss with knee ROM. Reframed the entry symptom as "stiff swing / reduced hip-flexion recoil" with an explicit note that a "restricted knee flexion" gait label may be a misread proxy for hip-initiation failure.
- **SFL file popliteus qualifier (Finding 10):** added the "(C) general DFL anatomy, not Earls gait" qualifier to the popliteus reference in `superficial_front_line.md` phase role, matching the hub and `deep_front_line.md`.
- **Gait phase file propagation (Composer additional notes):** fixes #1, #9, #10 had not been propagated to all gait phase files. Fixed: `preswing.md` (SBL+LL+DFL catapult; SFL recoil assists hip flexion only, not knee flexion), `loading_response.md` (eccentric → lengthen/elastically load; isometric SSC framing), `stance_phase.md` (same), `initial_double_limb_support.md` (same).
- **Files touched:** `03_Movement_Functions/gait_myofascial_mapping.md` (hub), `01_Fascial_Lines/superficial_front_line.md`, `deep_front_line.md`, `03_Movement_Functions/preswing.md`, `loading_response.md`, `stance_phase.md`, `initial_double_limb_support.md`.
- No cross-repo propagation required: still vault-internal synthesis. No facts duplicated to `tillyes_doc`, `tillyes_web`, or `tillyes_apps/*`.

## [2026-07-27] Cross-repo | Gait–myofascial synthesis now mirrored in movement_assessment
- Vault `[[gait_myofascial_mapping]]` and related fascial-line gait sections are now cited by `tillyes_apps/movement_assessment/src/knowledge/fixtures/movement-knowledge.v1.json` (`sourceRefs`) and drive optional clinical-report myofascial / cross-view synthesis UI.
- Added `CONSISTENCY_MAP.md` §1.5 so future hub edits must propagate to the app knowledge fixture + report builders + AGENTS/docs in the same session.
- Updated app docs (`AGENTS.md`, `README.md`, `docs/vault-integration.md`, `docs/limitations.md`) and fixed `tillyes_doc/AGENTS.md` Level 1 count five → six.
- Evidence boundary unchanged: myofascial language remains engine synthesis (C); view blind-spot rule applies.

## [2026-07-27] Extension | Temporal, Individual and Interpretive Framework
- Extended the movement-intelligence framework per the TillYes principle that the goal is each person's own effective, sustainable pattern — not one ideal movement or one maximised angle. All changes additive; no folders restructured, no notes renamed or overwritten.
- Created shared-biomechanics nodes in `03_Movement_Functions/`: `[[temporal_movement_metrics]]` (metrics across time), `[[stretch_shortening_cycle]]`, `[[energy_flow]]` (operational definition), `[[segment_angle_metrics]]`, `[[personalised_movement_intelligence]]`.
- Created golf nodes in `04_Golf_Swing/`: `[[golf_swing_events]]` (normalised swing time + event set), `[[x_factor]]` (pelvis-thorax dissociation curve incl. transition X-factor stretch), `[[golf_movement_sequence]]` (full-body sequence).
- Created `01_Fascial_Lines/myofascial_interpretive_layer.md` (cautious fascial-association rules).
- Created app-policy nodes in `05_App_Logic/`: `[[metric_evidence_classification]]` (claim typing) and `[[movement_reporting_standards]]` (non-judgmental seven-question reports).
- Targeted section/link updates to `[[golf_swing]]`, `[[golf_swing_transition]]`, `[[kinematic_sequence]]`, `[[functional_lines]]`, and `[[index]]`. Preserved the six-phase model, the Kwon event crosswalk, and the Kinetic Proxy Non-Upgrade Rule throughout.

## [2026-07-29] Source | Bourgain et al. 2022 golf-swing kinematics systematic review added
- User supplied https://pmc.ncbi.nlm.nih.gov/articles/PMC9227529/ (Bourgain, Rouch, Rouillon, Thoreux, Sauret, *Sports* 10(6): 91, 2022, DOI 10.3390/sports10060091). The PDF was already present in `raw/literature/` but had no source note and was not yet synced to the Mac.
- Created `[[bourgain_golf_swing_biomechanics_2022]]` in `00_Spec/sources/` as a **Level 3** (`source_role: domain_biomechanics`) source note with claim-level evidence, terminology, "what it does / does not support", and app-use boundaries, after reading the full-text HTML.
- Wired it in: added to the `evidence` blocks of `[[x_factor]]` and `[[kinematic_sequence]]`, registered in `[[index]]`, added to the golf Level 3 row and `supported_by` of `[[evidence_levels]]`.
- Evidence boundary preserved: the review is 3D instrumented evidence; it does not license 2D/MediaPipe proxies, does not establish "larger X-factor is better", and reports no crunch-factor/lumbar-injury correlation. Male/right-hand cohort bias recorded.
- No cross-repo propagation required: additive source registration only; no canonical duplicated facts altered.

## [2026-07-29] Maintenance | 00_Project_Reports historical banners added
- Annotated the three 2026-07-13 project reports in `00_Project_Reports/` with a status banner marking them as historical records (paths/snapshot values superseded) rather than living specs, per the vault rule against deleting or rewriting completed documents.
- `Six_Phases_Swing_Graph_Extraction.md`: banner notes the then→now folder mapping and that the "missing concepts" list is partly fulfilled (`[[x_factor]]`, COM proxy in `[[golf_movement_sequence]]`, `[[temporal_movement_metrics]]`); `Clubhead Speed`, `Ball Flight`, `Pressure Shift`, `Center of Pressure` remain intentionally uncreated.
- `Connective_Structure_Hub_Report.md`: banner notes `wiki/connective_structures/` → `02_Body_Structures/connective_structures/` and that hub-score / top-20 tables are a 2026-07-13 snapshot recomputed by `scripts/update_graph_metrics.py`.
- `Vault_Audit_and_Graph_Conversion_Plan.md`: banner notes the audit/plan is complete, its naming/relationship/template proposals are now formalised in `00_Spec/naming_conventions.md` and `00_Spec/spec.md`, and the proposed `wiki/` layout was not adopted.
- Bodies not rewritten; banners added above the original H1 content. No cross-repo propagation required.

## [2026-08-17] App Logic | Mandatory AI Reading Routes for Static Posture
- Added a task-based `Start Here for AI Agents` section to `[[index]]` with short routes for static posture, gait, golf, and vault maintenance.
- Static-posture agents now start from `[[bodyreading_static_posture]]`, `[[myofascial_interpretive_layer]]`, and `[[movement_reporting_standards]]`, then traverse only the matching finding and linked line/structure nodes.
- Added an explicit stopping rule so agents do not read the entire vault or source PDF by default; source notes and PDF locators are verification fallbacks.
- Registered the route and structured-report dependency in the workspace `CONSISTENCY_MAP.md` and enforced required markers through `scripts/check_consistency.sh`.

## [2026-08-17] App Logic | Client-Focused Structural Posture Contract
- Extended all 40 mapped static-posture findings with an observed pattern, priority region, client summary, compensation summary, two-to-four structural concerns, and quick confirmation checks.
- Kept source references, line-level detail, evidence limits, and caution data internally while enabling the client report to present one concise screening notice and structure-first explanations.
- Updated the canonical knowledge version to 1.2; the synchronized web copy and its validator must carry the same contract.

## [2026-08-17] App Logic | Detailed Cross-View Myofascial Contract
- Updated the canonical static-posture knowledge to v1.3 for all 40 findings with an integrated compensation mechanism and structured line-level roles, mechanism steps, interactions, client relevance, and measurement support gates.
- Curated forward-head posture across the SFL, SBL, DFL, Spiral Line, Lateral Line, and DFAL; conditional lines appear only when matching front/back or shoulder evidence is present.
- The web report and PDF now consume this deterministic contract and keep one concise screening notice rather than repeating cautions inside every result.

## [2026-08-24] Knowledge | Anatomy Trains line figures and track/station tables
- Added Myers Anatomy Trains figures under `01_Fascial_Lines/assets/` and embedded them on the matching line notes (SFL, SBL, DFL, Spiral, Lateral, Functional, Superficial Front Arm).
- Added Table-style bony-station / myofascial-track summaries on those notes so apps can cite the same diagrams and stations.
- Synced deployable copies live in `tillyes_apps/movement_assessment/public/assets/fascial-lines/` and `tillyes_web/public/assets/myofascial_lines/` (plus PDF assets).
