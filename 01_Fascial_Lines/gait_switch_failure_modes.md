---
id: gait_switch_failure_modes
type: Myofascial Line Concept
preferred_name: Gait Phase Switch Failure Modes
aliases: [gait fascial switches, gait cycle switch failure, walking derailment modes]
domain: gait
evidence_level: 5
source_role: engine_synthesis
supported_by: [anatomy_trains_myofascial_thomas_w_myers, chambers_sutherland_gait_analysis_2002, perry_burnfield_gait_analysis]
status: reviewed_engine_synthesis
reviewed_date: 2026-08-31
connects_to: [superficial_back_line, superficial_front_line, deep_front_line, lateral_line, spiral_line, back_functional_line, front_functional_line, gait_myofascial_mapping]
relationships:
  parent_concepts: [gait_myofascial_mapping]
  child_concepts: [superficial_back_line, superficial_front_line, deep_front_line, lateral_line, spiral_line, back_functional_line, front_functional_line]
  related_concepts: [gait_cycle, stance_phase, swing_phase, initial_contact, loading_response, mid_stance, terminal_stance, preswing, initial_swing, midswing, terminal_swing]
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 19
hub_score: 41
centrality: 0.171
---

# Gait Phase Switch Failure Modes

## Overview

In James Earls' "Anatomy Trains in Gait" framework (Myers Ch. 10), walking is modeled as **controlled falling decelerated by multi-line viscoelastic pre-stress**, where force transitions dynamically across gait phases. A **Gait Phase Switch** is the point where tension transfers from one line pair to another (e.g. from heel strike deceleration to terminal stance catapult propulsion).

A gait compensation (Vaulting, Circumduction, Hip Hike, Steppage Gait, Trendelenburg Drop) reflects a specific **Gait Switch Failure Mode** where a line fails to derail or transfer elastic load.

All gait switch failure modes are **Level 5 Engine Synthesis** hypotheses. They describe camera-observable gait descriptors and do not constitute measured joint moments, force plate ground reaction forces, or medical diagnoses.

---

## 1. Heel Strike Loading Response Switch (SPL / BFL Deceleration)

* **Associated Meridians:** [[spiral_line]] (SPL) & [[back_functional_line]] (BFL)
* **Anatomical Junction:** Calcaneus station, Tibialis Anterior $\rightarrow$ ITB $\rightarrow$ Upper Gluteus Maximus sling, Thoracolumbar Fascia.
* **Normal Function:** Decelerates calcaneal/talar medial rotation, hip flexion, and tibial internal rotation at heel strike (`initial_contact` to `loading_response`).
* **Failure Mode (Heel Strike Deceleration Failure):** If SPL or BFL fails to absorb heel strike impact, foot slaps medially into unbraked over-pronation (**Foot Slap / Equinus**), or motion is exported upward into pelvic wobble.

---

## 2. Mid-Stance Single-Limb Stability Switch (LL Glute Medius vs. DFL Adductors)

* **Associated Meridians:** [[lateral_line]] (LL) & [[deep_front_line]] (DFL)
* **Anatomical Junction:** Greater Trochanter station and Linea Aspera of Femur.
* **Normal Function:** Gluteus Medius (Local LL) holds the weighted pelvis level in single-limb stance (`mid_stance`), counteracting medial DFL adductor pull.
* **Failure Mode (Trendelenburg Drop Switch):** Weakness or timing inhibition in Gluteus Medius allows the unweighted hip to drop (**Trendelenburg Sign**), forcing the trunk to flex laterally toward the stance leg to keep Center of Mass over the foot.

---

## 3. Terminal Stance Propulsive Catapult Switch (SBL / DFL Catapult Recoil)

* **Associated Meridians:** [[superficial_back_line]] (SBL) & [[deep_front_line]] (DFL)
* **Anatomical Junction:** Achilles tendon, Calcaneus, Plantar Fascia, and Tibialis Posterior.
* **Normal Function:** Plantarflexors pre-stretch under dorsiflexion load during `terminal_stance`, loading the elastic catapult for toe-off (`preswing`).
* **Failure Mode (Catapult Recoil Block):** Soleus (Local SBL) or Gastrocnemius tightness prevents full ankle dorsiflexion before heel-off, cutting off the DFL/SBL elastic recoil and producing a flat-footed push-off.

---

## 4. Swing-Phase Advancement Switch (SFL / DFL Limb Acceleration)

* **Associated Meridians:** [[superficial_front_line]] (SFL) & [[deep_front_line]] (DFL)
* **Anatomical Junction:** ASIS station, Rectus Femoris, Psoas / Iliacus, Tibialis Anterior.
* **Normal Function:** Elastic recoil of SFL and DFL psoas accelerates the unweighted limb into hip flexion, knee flexion, and MTP dorsiflexion (`initial_swing` to `midswing`).
* **Failure Mode (Swing Clearance Emergency Switches):**
  * *Vaulting Switch:* If SFL/DFL fails to flex the swing knee/ankle, opposite SBL calf vaultingly extends the stance leg to clear the toe.
  * *Circumduction Switch:* SPL/LL swings the leg outward in an arc.
  * *Hip Hike Switch:* LL hikes the ipsilateral hip upward.
  * *Steppage Gait Switch:* SFL Extensor Digitorum over-flexes the hip and knee to lift a paralyzed dorsiflexor.

---

## Vault Report Boundary & Clinical Rules

When referencing gait switch failure modes in app reports:
1. **Never report measured kinetic loading:** Use *"Gait descriptors may be consistent with a Terminal Stance Catapult Switch failure"*, never *"Measured push-off force loss"*.
2. **Preserve view observability boundary:** Lines not visible from the active camera angle (e.g. SPL transverse rotation from a single side view) must be reported as `unavailable_from_this_view`.
3. **Include retest prompt:** Cue gait speed change or barefoot treadmill observation.
