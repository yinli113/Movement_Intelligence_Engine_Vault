# EVALS.md — Movement Intelligence Evaluation & Verification Specification

> **MANDATORY GOVERNANCE FOR ALL AI AGENTS & APPS**  
> This specification defines the mandatory, living evaluation (Eval) standards for all movement intelligence and posture applications across the TillYes ecosystem (`tillyes_apps/movement_squats`, `tillyes_apps/movement_assessment`, `tillyes_apps/static_posture_app`, and future motor-control/golf engines).
>
> Any AI agent building, modifying, or refactoring movement analysis code **must** strictly adhere to this evaluation pipeline before declaring a feature complete or pushing changes.
> Squat-specific criteria are copied into [`movement_squats/EVALS.md`](../../../tillyes_apps/movement_squats/EVALS.md); Running-specific criteria are recorded in [`movement_running/EVALS.md`](../../../tillyes_apps/movement_running/EVALS.md).

---

## 1. The Medallion Movement Evaluation Architecture

Every movement analysis pipeline in TillYes is evaluated across four progressive quality tiers: **Raw $\rightarrow$ Bronze $\rightarrow$ Silver $\rightarrow$ Gold**.

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │ 1. RAW LAYER (Ingestion & Capture Telemetry Quality)                   │
  │ Standards: Landmark visibility ≥ 0.45, camera perpendicularity/square, │
  │            app-specific FPS and duration, occlusion detection.         │
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
  * Define frame-rate requirements per app from the movement speed and sampling needs; use $\ge 24\text{ FPS}$ (ideal $30–60\text{ FPS}$) only where appropriate to that app.
  * There is no workspace-wide maximum video duration. Each app sets a duration and resource limit that captures the required task or complete cycles at usable quality. A limit around 45 seconds may suit gait capture when it reliably includes at least three complete cycles; it is not a default for other apps. Browser resource caps are implementation safeguards, not movement-quality criteria.

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
| **Running** (`movement_running`) | Initial-contact/toe-off timing, cadence, step time, stride time, contact/flight-time proxies | None in V0; myofascial interpretation remains disabled pending validated Level B/C support | Side view, reported frame rate $\ge 30$ FPS, at least 3 complete cycles; no clinical thresholding in V0 |
| **Static Posture** (`static_posture_app`) | Bilateral shoulder/pelvis level, Head-neck lateral shift, Coronal & Sagittal plumb offsets | Superficial Back Line, Superficial Front Line, Lateral Line, Deep Front Line | Bilateral asymmetry $>1.5\%$ image height, Plumb offset $>2.0\%$ image width |
| **Gait & Movement** (`movement_assessment`) | Stride length, Cadence, Stance/Swing phase ratio, Pelvic rotation / Trendelenburg | Functional Lines, Spiral Line, Deep Front Line, Lateral Line | At least 3 complete cycles; a capture limit around 45 seconds may be used if it reliably captures them; asymmetry index $>5\%$, ground-contact phase balance |
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


### Reviewed mesh surface sessions (2026-09-28)

For `scoliosis_workbench` upright/forward-bend surface sessions, require explicit
units, reviewed orientation and crop, retained OBJ faces, original-triangle-only
sampling and exclusion of overlapping surface layers. Test pose invariance,
one-sided/missing coverage, separate posture state, duplicate-geometry rejection,
and matched within-posture repeat grids. Region names refer to thirds of the
marked span. Coverage and repeat tolerances are engineering gates, not clinical
accuracy claims; no combined posture score or exercise-benefit inference.

### Side squat coordination (2026-09-30)
New angular timing channels require image aspect metadata and selected-side visibility.
Test mirrored geometry, missing/degenerate segments, baseline-to-phase gaps,
shin plateau with continuing descent, hip/shoulder vertical travel ordering,
phase-specific replay and no automatic fascial trigger. Study agreement does not
validate app thresholds; synthetic verification is not real-video accuracy validation.

### Claim-to-source grounding for graph RAG
Treat citation integrity and semantic support as separate checks: a valid node, edge, DOI, or URL does not prove that the cited source passage supports the generated claim. Preserve the retrieved graph path and exact source passage/locator, map each atomic generated claim to its evidence, and rate support, partial support, contradiction, or non-addressal. Separately verify session-specific values against the supplied metric IDs, units, sides, events, views, and evidence status. Keep independent reviewer labels and adjudication, report retrieval failures separately from generation failures, and do not treat automated or LLM-as-judge checks as human source-support judgments.


## Squat evidence and local ETL regression checkpoint — 2026-10-28

- Reject automatic switch-failure, inhibited/overactive muscle, palpation-target and release/activation prescription payloads in current camera knowledge/report output. Retain measured observations, regional questions, competing explanations and non-specific retests. Wedge responses cannot confirm a tissue block.
- Exercise actual DuckDB filter views at strict 50% deviation and 10% rarity boundaries, including nulls, zeros, sign ties, either minority sign, partial windows and independent capture/metric partitions. Preserve original facts and non-iterative baselines.
- Verify SCD2 profile isolation, unchanged-version reuse, opt-out, protected historical links and repeated migration of active versions. Verify longitudinal first-save ordering, reprocessing and withheld deltas for unknown/different algorithms, policies, filter modes, units or missing values.
- The optional peak filter is a review choice, not evidence of tracking error. Future timing must retain original continuous trajectories and view-specific baseline/geometry/visibility gates. Engineering thresholds, descriptive set changes and table-screen associations are not clinical validation or fatigue/causal classifiers.

Squat schematic-overlay regression: translated/shifted poses retain the same neutral path style, produce no tissue-state scalar/classification and reject nonfinite/missing landmark paths. The optional overlay defaults off.


### Squat paired-recording alignment — 2026-10-28

Require same-set confirmation, four reviewed marker times with positive per-camera uncertainty, source SHA-256 identities and finite durations. Test offset/rate mapping, non-overlapping marker intervals, propagated interval bounds, no extrapolation, source replacement and metadata/marker invalidation, failed/buffering playback and export confirmation gates. Original per-view evidence and legacy ETL `synchronized: false` remain unchanged. A synthetic replay pass is not hardware synchronization or real-video timing validation.


### Phase 3 regional sequence regression — 2026-10-28
Require interval comparisons (including touching bounds), partial/baseline/geometry/channel-history gates, descent vs ascent carry-over, no fake global causal ranking, signed mirror behavior, native replay and complete ±200 ms observation windows. Test source/duration/side mismatches, reviewed-span limits and compounded marker/event uncertainty across different camera repetition indices. Silver validates browser DTOs, quarantines malformed phases, preserves Bronze/legacy peaks and excludes invalid repetitions. Gold persistence uses all included reps and cannot be changed by the peak filter. Tests must include real DuckDB roundtrip, API-to-browser presentation, legacy schema upgrade and revoked-alignment stale-response protection. Synthetic results do not establish real-video accuracy.
