---
id: anatomy_trains_myers_2009
type: Evidence Source
preferred_name: "Anatomy Trains: Myofascial Meridians for Manual and Movement Therapists"
aliases: [Anatomy Trains, Thomas Myers Anatomy Trains, Anatomy_Trains_Myofascial_Thomas_W_Myers]
short_definition: "Primary fascial-line reference source for the MVP golf movement knowledge graph."
author: Thomas W. Myers
publication_year: 2009
format: textbook_pdf
raw_file: raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf
relationships:
  contains: [superficial_back_line, lateral_line, spiral_line, functional_lines, deep_front_line, sacrotuberous_ligament, thoracolumbar_fascia, plantar_fascia, nuchal_ligament, iliotibial_tract]
  connects_to: [golf_swing_transition]
  produces: []
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: []
  improved_by: []
  supported_by: []
  relevant_to: [fascial_line_model, golf_movement_reasoning_mvp]
golf_relevance: "Use this as the main source for fascial-line membership and continuity when building the golf movement graph; use standard anatomy references separately for muscle actions, joints, and definitions."
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Table of contents, local PDF page 6"
    supports: "Chapters identify Superficial Back Line, Lateral Line, Spiral Line, Functional Lines, Deep Front Line, Anatomy Trains in motion, and structural analysis as relevant sections."
confidence: medium
review_status: source_summary_for_graph_mvp
relationship_count: 23
hub_score: 81
centrality: 0.397
updated: 2026-06-29
---

# Anatomy Trains: Myofascial Meridians for Manual and Movement Therapists

## Source Role

This source should be used as the primary fascial-line reference for the golf movement knowledge graph. It should not be used as a standalone medical authority, and it should not replace standard anatomy references for muscle actions, joint definitions, or clinical claims.

Important terminology caveat: the book title uses "myofascial meridians". In this vault, use `Fascial Line` as the canonical graph type and avoid treating fascial lines and other meridian systems as the same system.

## Graph Extraction Targets

- supports -> [[superficial_back_line]]
- supports -> [[lateral_line]]
- supports -> [[spiral_line]]
- supports -> [[functional_lines]]
- supports -> [[deep_front_line]]
- supports -> [[sacrotuberous_ligament]]
- supports -> [[thoracolumbar_fascia]]
- supports -> [[plantar_fascia]]
- supports -> [[nuchal_ligament]]
- supports -> [[iliotibial_tract]]
- relevant_to -> [[golf_swing_transition]]

## Relevant Sections

- Chapter 3: Superficial Back Line
- Chapter 5: Lateral Line
- Chapter 6: Spiral Line
- Chapter 8: Functional Lines
- Chapter 9: Deep Front Line
- Chapter 10: Anatomy Trains in motion
- Chapter 11: Structural analysis

## Source Summary for Graph Use

Myers presents a fascial-line model for describing continuity through connected myofascial tissues and bony stations. For the golf MVP, the useful extraction is not a full textbook summary. The useful extraction is a set of source-backed relationships:

- The [[superficial_back_line]] can be used as a posterior-chain model from plantar foot structures through calves, hamstrings, spinal extensors, and head/scalp region.
- The [[lateral_line]] can be used as a lateral balance and rotational-braking model involving fibular/peroneal structures, lateral leg tissues, iliotibial tract, lateral abdominal tissues, ribs, and neck-related structures.
- The [[spiral_line]] can be used as a rotational continuity model involving foot, leg, trunk, scapular sling, and neck relationships.
- The [[functional_lines]] can be used as a cross-body force-transfer model involving shoulder girdle, trunk fascia, pelvis, and lower limb relationships.
- The [[deep_front_line]] can be used as a deep support model involving inner foot, deep leg, pelvis, diaphragm, thoracic inlet, neck, and jaw-related structures.
- Connective structures such as [[plantar_fascia]], [[iliotibial_tract]], [[thoracolumbar_fascia]], [[sacrotuberous_ligament]], and [[nuchal_ligament]] should become first-class graph nodes where they transmit force between muscles, joints, and fascial lines.

## Golf MVP Interpretation

For the golf graph, this source should support fascial-line membership and connection hypotheses only. Example reasoning paths:

- [[toe_loading]] -> [[deep_front_line]] -> [[hip_internal_rotation]]
- [[toe_loading]] -> [[lateral_line]] -> pelvic sway limitation patterns
- [[thoracic_rotation]] -> [[spiral_line]] -> [[trail_shoulder_external_rotation]]
- [[hip_internal_rotation]] -> [[functional_lines]] -> [[trail_shoulder_external_rotation]]
- [[neck_tension]] / [[jaw_clenching]] -> [[deep_front_line]] and [[superficial_back_line]] as possible bracing-context links

## Extracted Evidence Notes

- Local PDF page 6 lists chapters for the main line model: Superficial Back Line, Lateral Line, Spiral Line, Functional Lines, Deep Front Line, motion, and structural analysis.
- Local PDF pages 130-132 include Lateral Line material describing continuity through peroneals/fibularii, lateral knee tissues, iliotibial tract, abductors, lateral abdominal obliques, intercostal layers, scalenes, sternocleidomastoid, and splenii.
- Local PDF page 147 includes Spiral Line material describing the rhomboids and serratus anterior as a scapular myofascial sling.
- Local PDF page 185 includes Functional Line table material identifying Back Functional Line and Front Functional Line tracks including latissimus dorsi, lumbodorsal/sacral fascia, gluteus maximus, pectoralis major, rectus sheath, and adductor longus.
- Local PDF pages 137 and 209 include Deep Front Line references involving scalenes, quadratus lumborum, diaphragm, thoracic inlet, and throat/neck-related structures.
- Chapter 11 "Structural analysis" (local PDF pages 239-264) is the source's static-posture BodyReading method and directly supports [[bodyreading_static_posture]]:
  - p.239 states useful clinical information can be gleaned from analysis of the standing client, referring only to still photos of standing posture, and that the Anatomy Trains map was first developed as a visual assessment tool for standing bodyreading.
  - pp.241-244 define the four descriptors (tilt, bend, shift, rotation) applied to standing posture.
  - pp.248-252 read specific fascial lines as shortened from static photos only (SFL/SBL balance, Lateral Line ear-to-hip and lower-leg, Spiral Line rib-on-pelvis rotation, Functional Line cross-body, Deep Front Line groin/inner-leg/psoas core).
  - p.245 maps static calcaneus/arch pattern to the Superficial Back Line bridle and the lateral band of the plantar fascia.
  - p.261 defines four pelvic tilt-by-shift static positional types with line-based soft-tissue strategies.

## Review Notes

- Confidence is `medium` because this is a source summary extracted from PDF text, not a full manual chapter-by-chapter review.
- Use direct page checks before adding high-stakes relationships.
- Do not infer treatment claims from this source alone.
