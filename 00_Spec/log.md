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
- **New mechanics nodes**: Added [[golfer_ground_interaction_model]], [[pivoting_moment]], [[foot_contact_moment]], [[linear_impulse]], and [[angular_impulse]], preserving direct/residual GRM at COP as distinct from the GRF moment about COM.
- **Six-phase integration**: Connected the measured mechanics and conservative event crosswalk to the existing six source-defined golf phases without substituting unmatched events or inferring kinetics from video.
- **Myofascial-line integration and evidence boundary**: Kept myofascial lines as the primary anatomical structure and labelled mechanics-to-line mappings by evidence level rather than as measured tissue loading.
- **App observability safeguards**: Added [[golf_kinetics_observability_boundary]] as the authoritative allow-list separating instrumented kinetics, camera-observable descriptors, and Level 5 hypotheses; no diagnosis or treatment claims were added.
- **Verification performed**: Recalculated graph metrics, checked index and contextual backlinks, compared unresolved wikilinks with the four-target legacy baseline, searched for unsupported camera-kinetics or fascial claims, and ran diff, status, and repository-scope checks.
