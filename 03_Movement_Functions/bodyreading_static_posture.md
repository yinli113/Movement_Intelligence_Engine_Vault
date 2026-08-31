---
id: bodyreading_static_posture
type: Assessment
preferred_name: BodyReading of Static Posture
aliases: [static posture assessment, structural analysis, bodyreading, standing posture reading]
short_definition: "A static-standing-posture reading method that uses four relational descriptors (tilt, bend, rotation, shift) to infer fascial-line pattern hypotheses, to be confirmed by movement and gait."
relationships:
  contains: [posture_tilt, posture_bend, posture_rotation, posture_shift]
  connects_to: [superficial_back_line, superficial_front_line, lateral_line, spiral_line, deep_front_line, functional_lines]
  produces: [fascial_line_pattern_hypothesis]
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: [bodyreading_static_posture]
  improved_by: []
  supported_by: [anatomy_trains_myofascial_thomas_w_myers, julie_hammond_breakout]
  relevant_to: [fascial_knowledge_json, static_posture_app, golf_swing]
confidence: high
review_status: source_extracted
relationship_count: 12
hub_score: 32
centrality: 0.207
updated: 2026-07-06
---

# BodyReading of Static Posture

## Definition

BodyReading is the Anatomy Trains method for reading myofascial-line pattern hypotheses from a **static standing posture**. It uses four relational descriptors applied between bony structures, and reads the relative tension/shortening of the fascial lines as a first-pass hypothesis. Static posture is explicitly treated as informative: it "raises questions" and gives insight into the client's story and movement patterns, but it is not the full story and must be corroborated by gait and functional movement.

This node exists to record the source-backed rule that **static posture manifests fascial-line patterns as hypotheses**, so the static-posture app can attribute lines without claiming diagnosis.

## Why It Matters for the App

The static-posture app (`static_posture_app`) reads posture findings from a single standing image and maps them to the external `fascial_knowledge.json` knowledge file. Both Level 1 sources support emitting cautious line suggestions from static stance (hypothesis language, not diagnosis). Without this node, the app's knowledge base and the wiki disagree on whether static posture can carry fascial-line information.

## The Four BodyReading Descriptors

Applied to the relationship of one bony structure to another (or occasionally to gravity):

1. **Tilt** — deviation from vertical or horizontal; named from the top of the structure (e.g. anterior pelvic tilt, left shoulder-tilt).
2. **Bend** — a series of tilts that creates a curve; shorthand for spinal curves (e.g. uncompensated bend, two compensating bends, scoliotic three-four bend patterns).
3. **Rotation** — rotation of one structure relative to another, usually around a vertical axis in the horizontal plane (e.g. right-rotated rib cage relative to pelvis); named for where the front of the structure points.
4. **Shift** — displacement of the center of one body part relative to the center of another; a shear or translation (e.g. anterior shift of pelvis, left shift of head).

None of the four are mutually exclusive: a rib cage can be shifted, tilted, and rotated relative to the pelvis at the same time.

## Static-Posture to Fascial-Line Reading

Read from standing photos only, as a hypothesis to confirm with movement:

- **SFL vs SBL balance** — the first BodyReading question: compare the relative tension/shortening of the [[superficial_front_line]] and [[superficial_back_line]] from the side. "SFL pulled down along most of its length" and "SBL pulled up from heels to shoulders" are static readings.
- **Lateral Line** — lateral tilts and side-bend of trunk/neck read the [[lateral_line]]; a shorter right LL ear-to-hip or shorter left lower LL read from stance.
- **Spiral Line** — rotations of rib cage relative to pelvis, and across-body shoulder/rib asymmetry, read the [[spiral_line]].
- **Functional Line** — diagonal cross-body shortening (e.g. right Front Functional Line shorter, pulling shoulder toward opposite hip) read the [[functional_lines]].
- **Deep Front Line** — the "core" line is repeatedly the key to opening a static pattern: shortness in the groin / inner leg / psoas complex read from stance points to [[deep_front_line]].
- **Foot/calcaneus** — static calcaneus medial rotation/tilt and fallen arch read the SBL "bridle" around the heel and the lateral band of the [[plantar_fascia]].
- **Pelvic position** — four static pelvic types (anterior/posterior tilt × anterior/posterior shift) each imply different soft-tissue and line strategies.

## Supporting Evidence From Sources

### [[anatomy_trains_myofascial_thomas_w_myers]] — Chapter 11 "Structural analysis"
- p.239: "useful clinical information can be gleaned from an analysis of the standing client... In this chapter, we refer only to still photos of standing posture."
- p.239: "The Anatomy Trains map was first developed as a visual assessment tool... describes the language and method of 'bodyreading'... to standing assessment."
- pp.241-244: definitions of tilt, bend, shift, rotation applied to standing posture.
- pp.248-252: four worked clients where specific lines are read as shortened from static photos only (Client 1: SFL down, SBL up, right LL shorter, right upper SPL shorter; Client 2: right FFL shorter, DFL groin shortness; Client 3: both LLs in thigh, abductors short, left SPL shorter, DFL core as key).
- p.245: static calcaneus/arch pattern maps to the SBL bridle and plantar fascia lateral band.
- p.261: four pelvic tilt×shift positional types as static patterns with line-based strategies.

### [[julie_hammond_breakout]] — Introduction to Anatomy Trains
- p.9: "Static posture starts to raise questions and gives us an insight into the client's story and movement patterns. It is not THE full story."
- p.9: BodyReading sequence — static raises questions → assess function and gait → how does the static posture move?
- p.10-12: the four descriptors (tilt, shift, rotation, bend) applied to standing posture.
- p.12: first BodyReading question is "What is the balance between the SFL and SBL?"
- p.16: lateral tilts read into the Lateral Line / QL; p.21: DFL BodyRead from stance.

## Static Posture Switch Failure Matrix (Level 5)

See [[posture_switch_failure_modes]] for the foundational dynamic switch derailments governing standing postural alignment.

| Postural Alignment Finding | Primary Line Pair | Bony Station | Switch Failure Mode | Express vs. Local Dynamics | Retest Protocol |
|---|---|---|---|---|---|
| **Forward Head Posture** | [[superficial_back_line]] (SBL) vs [[deep_front_line]] (DFL) | Occipital Ridge / C1-C7 | [[posture_switch_failure_modes#1-suboccipital-cervical-switch-sbl-vs-dfl-neck-flexors\|Suboccipital Cervical Switch]] | Suboccipitals (Local SBL) hyper-extend upper neck over weak Longus Colli (Local DFL). | Cue "double chin" chin retraction in standing posture. |
| **Lordotic / Kyphotic-Lordotic (Anterior Tilt)** | [[superficial_front_line]] (SFL) & [[deep_front_line]] (DFL) | ASIS / Lesser Trochanter | [[posture_switch_failure_modes#2-asis-pelvic-sagittal-switch-sfl-rectus-femoris-vs-sfl-abdominal-wall\|ASIS Pelvic Sagittal Switch]] | Rectus Femoris (SFL Express) & Psoas (DFL Express) pull ASIS down against weak Rectus Abdominis. | Cue posterior pelvic tuck & active core engagement. |
| **Flat-Back Posture (Loss of Lordosis)** | [[superficial_back_line]] (SBL) & [[deep_front_line]] (DFL) | Lumbar Spine ($L1-L5$) | Lumbar Erector / Psoas Switch | SBL lumbar erectors and DFL psoas lose lordotic tone, flattening lumbar curve. | Cue active thoracic extension & gentle anterior pelvic tilt. |
| **Sway-Back Posture (Anterior Pelvic Shift)** | [[superficial_back_line]] (SBL) & [[deep_front_line]] (DFL) | Pubic Symphysis / Thorax | Pelvic Anterior Shift Lock | Pelvis shifts anteriorly onto Y-ligaments; lower DFL core under-engages while SBL upper erecters brace. | Cue pelvis-over-foot shift and active DFL core activation. |
| **Pelvic Unleveling / Lateral Trunk Shift** | [[lateral_line]] (LL) & [[deep_front_line]] (DFL) | Iliac Crest / Greater Trochanter | Unilateral Lateral Line Lock | Quadratus Lumborum (Express LL) hikes hip to compensate for weak stance Gluteus Medius (Local LL). | Perform side-plank endurance and single-leg stance test. |
| **Torso Yaw Rotation** | [[spiral_line]] (SPL) & [[functional_lines]] | ASIS / Rib Cage | Asymmetric Spiral Sling Switch | Obliques (Express SPL) twist ribcage relative to pelvis in standing stance. | Seated thoracic rotation assessment. |
| **Medial Arch Collapse (Foot Pronation)** | [[deep_front_line]] (DFL) & [[spiral_line]] (SPL) | Navicular / Medial Malleolus | [[posture_switch_failure_modes#4-calcaneal-navicular-tripod-switch-dfl-arch-vs-ll-peroneal-track\|Calcaneal-Navicular Tripod Switch]] | Tibialis Posterior (Local DFL) arch support fails; Peroneus Longus (Express SPL) pulls 1st metatarsal into eversion. | Place 5mm wedge under 1st metatarsal head or active short foot grip. |

## App Integration

The app's `fascial_knowledge.json` encodes this method: each static finding carries `possible_myofascial_lines`, `possible_related_structures`, cautious `report_language`, and a `caution_note` that static posture cannot confirm restriction. The mapper (`fascial_mapper.py`) matches engine measurements to these findings by name, alias, and `left_`/`right_` prefix-stripped fallback, filtered by view. Output is hypothesis-level only.

## Confidence and Limits

- `confidence: high` that static posture carries fascial-line pattern information — directly stated in both Level 1 sources.
- Static posture cannot diagnose fascial restriction, pain source, or pathology. All line attributions from static stance are pattern suggestions to be confirmed by clinical assessment and movement testing.
- MediaPipe Pose landmarks are 2D proxies; they do not directly measure fascia.

## Related Concepts

- [[superficial_back_line]], [[superficial_front_line]], [[lateral_line]], [[spiral_line]], [[deep_front_line]], [[functional_lines]]
- [[anatomy_trains_myofascial_thomas_w_myers]], [[julie_hammond_breakout]]
- [[plantar_fascia]], [[iliotibial_tract]], [[thoracolumbar_fascia]]

## Parent Concepts

- Assessment

## Category

Assessment
