# EVALS.md — Movement Intelligence Evaluation & Verification Specification

> **MANDATORY GOVERNANCE FOR ALL AI AGENTS & APPS**  
> This specification defines the mandatory, living evaluation (Eval) standards for all movement intelligence and posture applications across the TillYes ecosystem (`tillyes_apps/movement_squats`, `tillyes_apps/movement_assessment`, `tillyes_apps/static_posture_app`, and future motor-control/golf engines).
>
> Any AI agent building, modifying, or refactoring movement analysis code **must** strictly adhere to this evaluation pipeline before declaring a feature complete or pushing changes.

---

## 1. The Medallion Movement Evaluation Architecture

Every movement analysis pipeline in TillYes is evaluated across four progressive quality tiers: **Raw $\rightarrow$ Bronze $\rightarrow$ Silver $\rightarrow$ Gold**.

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │ 1. RAW LAYER (Ingestion & Capture Telemetry Quality)                   │
  │ Standards: Landmark visibility ≥ 0.45, camera perpendicularity/square, │
  │            FPS ≥ 24, temporal duration ≤ 45s, occlusion detection.     │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
  ┌───────────────────────────────────▼────────────────────────────────────┐
  │ 2. BRONZE LAYER (Cleansing, Calibration & Baseline Extraction)         │
  │ Standards: Temporal interpolation gap ≤ 200ms, standing frame filter,  │
  │            dynamic reference guide alignment (Toe/Midfoot/Heel).       │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
  ┌───────────────────────────────────▼────────────────────────────────────┐
  │ 3. SILVER LAYER (Kinematic Extraction & Repetition Segmentation)       │
  │ Standards: Mathematical angle bounds [0°, 180°], rep state machine,    │
  │            repetition persistence (≥50% rule), 100% test pass rate.    │
  └───────────────────────────────────┬────────────────────────────────────┘
                                      │
  ┌───────────────────────────────────▼────────────────────────────────────┐
  │ 4. GOLD LAYER (Cross-View Synthesis & Clinical Myofascial Graph)       │
  │ Standards: Multi-planar triangulation, conflict resolution protocol,   │
  │            non-diagnostic terminology audit, vault sync (8/8 pass).    │
  └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Layer-by-Layer Evaluation Contracts

### Tier 1: Raw Layer (Ingestion & Telemetry Quality)
* **Landmark Reliability Threshold**:
  * Every key anatomical joint (ankle, knee, hip, shoulder, ear) must satisfy $\text{visibility} \ge 0.45$.
  * If key joints drop below $0.45$ across $>30\%$ of video duration, tag as `unreliable_capture` and prompt user for better framing.
* **Camera Perspective Verification**:
  * **Side (Sagittal) View**: Perpendicular angle ($90^\circ \pm 15^\circ$ to sagittal plane). Key side ankle, knee, hip, shoulder, and ear must remain in-frame.
  * **Front (Coronal) View**: Square frontal angle ($0^\circ \pm 15^\circ$). Bilateral ankles, knees, hips, and shoulders must remain in-frame.
* **Frame Rate & Duration**:
  * Frame rate must be $\ge 24\text{ FPS}$ (ideal $30–60\text{ FPS}$).
  * Video duration bounded to $\le 45\text{ seconds}$ to prevent browser memory exhaustion.

---

### Tier 2: Bronze Layer (Cleansing, Calibration & Baseline Extraction)
* **Temporal Continuity & Interpolation**:
  * Binary-search interpolation windowing (`interpolatePoseAtTime.ts`) must enforce $\text{gap} \le 200\text{ms}$ (`MAX_INTERPOLATION_GAP_MS`).
* **Starting Posture Frame Isolation**:
  * Extract standing baseline from the first $25\%$ of upright frames (`selectStartingPostureFrame`).
  * Compute baseline posture observations (Cervical alignment, Thoracic lean, Standing knee angle, Base of support).
* **Reference Guide Anchoring**:
  * **Sagittal (Side) View**:
    * Anterior Outer Line: Anchored to **Pointed Toes / Forefoot (Index 31/32)**.
    * Center Solid Line: Anchored to **Mid-Foot / Lateral Malleolus (Index 27/28)**.
    * Posterior Outer Line: Anchored to **Heel / Calcaneus (Index 29/30)**.
  * **Coronal (Front) View**:
    * Left/Right Dashed Lines: Anchored to **Bilateral Stance Width Envelope**.
    * Center Solid Line: Anchored to **Midline Gravity Plumb Line**.

---

### Tier 3: Silver Layer (Kinematics & Repetition State Machine)
* **Kinematic Mathematical Invariants**:
  * Joint angles (flexion, extension, lateral shift) must be clamped to physically possible biological ranges $[0^\circ, 180^\circ]$.
  * NaN / undefined / infinite coordinates must be caught and rejected before metric computation.
* **State Machine Repetition Validation**:
  * Every valid repetition must execute the full cyclic state sequence:
    $$\text{Standing Baseline} \longrightarrow \text{Descent Phase} \longrightarrow \text{Bottom Inflection Point} \longrightarrow \text{Ascent Phase} \longrightarrow \text{Standing Return}$$
  * Incomplete or aborted squats are rejected from average metric pools.
* **Repetition Persistence Threshold ($\ge 50\%$ Rule)**:
  * A kinematic compensation or fascial trigger is **only** surfaced if it occurs in $\ge 50\%$ of completed repetitions.
  * Transient one-off balance twitches are filtered out.
* **Automated Unit Testing Gate**:
  * $100\%$ pass rate on all automated unit test suites (`npm test` in app directory).

---

### Tier 4: Gold Layer (Cross-View Synthesis & Clinical Myofascial Graph)
* **Multi-Planar Cross-View Synthesis**:
  * Front and Side observations are triangulated across planes (`synthesizeCrossView.ts`).
  * Relationships must be strictly classified into:
    * `corroborating`: Multi-plane findings reinforce a unified motor control strategy.
    * `complementary`: Plane-specific findings describe different dimensions of movement.
    * `conflicting`: Opposing observations across planes (e.g. overactive in coronal vs underactive in sagittal).
    * `limited`: One or both views lack sufficient reliability.
* **Conflict Resolution Governance**:
  * **Never** forcibly average opposing observations into a false "neutral" score.
  * Downgrade combined reliability floor to `low` or `moderate`.
  * Surface distinct plane-specific hypotheses with targeted hands-on physical retest protocols (e.g., Manual Muscle Testing, length-tension palpation).
* **Non-Diagnostic Clinical Boundary Audit**:
  * All findings must use observational hypothesis terminology:
    * 🔴 **Hypothesized Overactive** (Suspected Superficial Mover)
    * 🔵 **Hypothesized Underactive** (Suspected Local Stabilizer)
    * 🟡 **Bony Station Anchor Point** (Palpation Target)
  * **Prohibited Terms:** The engine must never output medical diagnosis claims (*"patellar tendinitis"*, *"scoliosis"*, *"torn ligament"*, *"joint pathology"*).
* **Workspace Knowledge Synchronization Gate**:
  * Deployable app knowledge must match the source-of-truth knowledge graph in `tillyes_vault/Movement_Intelligence_Engine_Vault/`.
  * `bash scripts/check_consistency.sh` must return `PASS` (8/8 checks).

---

## 3. App-Specific Evaluation Matrix

| Domain / App | Core Kinematic Invariants | Fascial Line Meridians Evaluated | Primary Eval Thresholds |
|---|---|---|---|
| **Squats** (`movement_squats`) | Knee flexion depth, Trunk-tibia parallel angle, Heel rise proxy, Knee-to-foot valgus/varus | Lateral Line, Spiral Line, Deep Front Line, Superficial Back Line, Superficial Front Line | Repetition persistence $\ge 50\%$, Heel rise $>0.015$, Valgus excursion $>0.04$ |
| **Static Posture** (`static_posture_app`) | Bilateral shoulder/pelvis level, Head-neck lateral shift, Coronal & Sagittal plumb offsets | Superficial Back Line, Superficial Front Line, Lateral Line, Deep Front Line | Bilateral asymmetry $>1.5\%$ image height, Plumb offset $>2.0\%$ image width |
| **Gait & Movement** (`movement_assessment`) | Stride length, Cadence, Stance/Swing phase ratio, Pelvic rotation / Trendelenburg | Functional Lines, Spiral Line, Deep Front Line, Lateral Line | Asymmetry index $>5\%$, Ground contact phase duration balance |
| **Golf Swing** (`00_Spec/` Engine) | 6-Phase swing intervals, Pelvis-torso separation (X-Factor), Lead hip internal rotation | Spiral Line, Functional Lines, Lateral Line, Deep Front Line | Transition sequencing (Pelvis leads Torso leads Arms), Lateral sway vs rotational pivot |

---

## 4. Mandatory Agent Operating Protocol

Whenever an AI agent works on any movement application in this workspace:

1. **Pre-Implementation Check**:
   * Read `AGENTS.md`, `CONSISTENCY_MAP.md`, and this `EVALS.md`.
2. **Implementation Requirements**:
   * Write deterministic mathematical calculations in the Silver Layer (TypeScript/Python).
   * Bind clinical reasoning to canonical JSON knowledge files in the Gold Layer.
   * Frame all outputs with non-diagnostic hypothesis language.
3. **Verification & Testing Protocol (Mandatory Before Push)**:
   ```bash
   # 1. Run app-specific unit and build tests
   npm test && npm run build
   
   # 2. Run workspace consistency lint backstop
   bash scripts/check_consistency.sh
   ```
4. **Living Document Updates**:
   * When a new movement pattern, camera edge case, or biomechanical evaluation criterion is discovered, update this `EVALS.md` in the same session.
