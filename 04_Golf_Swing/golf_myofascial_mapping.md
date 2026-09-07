---
id: golf_myofascial_mapping
type: Movement Function
preferred_name: Golf Swing Myofascial Mapping (Engine Synthesis)
aliases: [golf fascial mapping, golf swing line synthesis, anatomy trains in golf]
domain: golf
evidence_level: 5
source_role: engine_synthesis
supported_by: [anatomy_trains_myofascial_thomas_w_myers, dr_kwon_golfer_ground_interaction, bourgain_golf_swing_biomechanics_2022]
status: reviewed_engine_synthesis
reviewed_date: 2026-08-31
connects_to: [golf_swing, golf_swing_events, golf_swing_transition, x_factor, superficial_back_line, superficial_front_line, deep_front_line, lateral_line, spiral_line, back_functional_line, front_functional_line, golf_switch_failure_modes]
relationships:
  parent_concepts: [golf_swing]
  child_concepts: [superficial_back_line, superficial_front_line, deep_front_line, lateral_line, spiral_line, back_functional_line, front_functional_line, golf_switch_failure_modes]
  related_concepts: [golf_kinetics_observability_boundary, gluteus_maximus, gluteus_medius, latissimus_dorsi, adductor_magnus, thoracolumbar_fascia]
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 20
hub_score: 69
centrality: 0.18
---

# Golf Swing Myofascial Mapping & Switch Failure Taxonomy

## Evidence Status

*Anatomy Trains* defines structural continuities, while Dr. Young-Hoo Kwon and Bourgain et al. (2022) define golf swing mechanics and kinematic sequences. Camera metrics describe 2D image-plane motion and swing events; they do not measure ground reaction forces (GRF), 3D moments (GRM at COP), muscular torque, or fascial loading. All golf-to-line relationships in this node are **Level 5 Engine Synthesis** hypotheses.

See [[golf_switch_failure_modes]] for the foundational dynamic switch derailments during the golf swing.

---

## The Golf Swing Misalignment & Switch Failure Taxonomy

Below is the matrix linking camera-observable swing flaws to myofascial line pairs, bony stations, dynamic switch failures, express vs. local muscle dynamics, and in-person retest protocols.

| Swing Flaw / Finding | Swing Phase | Primary Line Pair | Bony Station Anchor | Switch Failure Mode | Express vs. Local Dynamics | Retest Protocol |
|---|---|---|---|---|---|---|
| **Trail Pelvis Sway (Lateral Slide)** | [[shaft_parallel_to_end_pelvis_rotation]] | [[lateral_line]] & [[spiral_line]] | Trail Greater Trochanter | [[golf_switch_failure_modes#1-backswing-trail-hip-loading-switch-spl--ll-trail-anchor\|Backswing Trail Loading Switch]] | Trail Gluteus Medius (Local LL) fails to anchor; TFL/ITB (Express LL) slides hip away from target. | Step-and-turn backswing drill. |
| **Reverse Spine Angle** | [[end_pelvis_rotation_to_top_backswing]] | [[superficial_back_line]] & [[lateral_line]] | Thoracic Spine / Iliac Crest | Upper Trunk Over-Tilt Switch | Thoracic Erectors (Express SBL) & QL (Express LL) hyper-extend spine toward target. | Cross-arms chest turn with spine angle check. |
| **Over-the-Top (Steep Downswing)** | [[golf_swing_transition]] | [[back_functional_line]] & [[front_functional_line]] | Thoracolumbar Fascia / Shoulder | [[golf_switch_failure_modes#2-transition-pelvis-thorax-x-factor-dissociation-switch-bfl--ffl-stretch-shortening\|Transition X-Factor Switch]] | Upper body Pectoralis/Latissimus (Express FFL/BFL) fire before pelvic transition. | Step-first downswing transition drill. |
| **Early Extension (Pelvis Thrust)** | [[max_unweighting_to_impact]] | [[deep_front_line]] & [[superficial_front_line]] | Pubic Symphysis / ASIS | [[golf_switch_failure_modes#3-impact-lead-leg-post--ground-transfer-switch-dfl--ll-lead-post\|Impact Lead Leg Post Switch]] | Lead Psoas/Adductors (DFL) fail to centrate hip; pelvis thrusts forward toward ball. | Chair-behind-glutes contact drill during impact. |
| **Hanging Back (Trail Foot Weight)** | [[max_unweighting_to_impact]] | [[deep_front_line]] & [[lateral_line]] | Trail Calcaneus / Lead Arch | Impact Weight Transfer Failure | Lead Tibialis Posterior (Local DFL) fails to grip arch; weight remains on trail foot. | Trail-foot-raised step-through impact drill. |
| **Casting / Early Wrist Release** | [[golf_swing_transition]] / [[max_unweighting_to_impact]] | [[deep_back_arm_line]] & [[front_functional_line]] | Lead Wrist / Coracoid | Upper Limb Lag Switch Failure | Forearm flexors/extensors fire prematurely before lead hip post anchors. | Impact bag / lag stick drill. |

---

## App Clinical Report Guidelines

When surfacing golf swing findings in the Movement App:
1. **Cite event-bounded metric trigger:** e.g. *"Camera detected 12° lateral trail pelvis sway during backswing transition."*
2. **Present line as candidate hypothesis:** *"May be consistent with a Trail Hip Loading Switch failure involving the Lateral and Spiral Lines."*
3. **Respect kinetic proxy non-upgrade rule:** Do not convert 2D rotation proxies into 3D torque or force-plate moment claims.
4. **Prompt swing drill retest:** Provide the retest drill to confirm or rule out the hypothesis.
