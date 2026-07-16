# Dr. Kwon Golf Biomechanics Vault Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a citation-backed, fascial-line-first Dr. Kwon golfer-ground interaction graph that future golf analysis can traverse without claiming camera-derived kinetics or tissue loading.

**Architecture:** Dr. Kwon's primary pages and peer-reviewed work form the Level 3 kinetics source layer. Reusable movement-function nodes translate that evidence into existing golf phases, while separate Level 1 anatomy and clearly labelled golf interpretations connect phases through connective structures to myofascial lines. A dedicated observability boundary prevents the future app from treating video geometry as force, pressure, torque, energy, or fascial tension.

**Tech Stack:** Obsidian Markdown, YAML frontmatter, wikilinks, Mermaid, Git, existing `scripts/update_graph_metrics.py`, shell-based vault integrity checks.

## Global Constraints

- Modify only `Movement_Intelligence_Engine_Vault`; do not change the current gait application.
- Preserve the five evidence levels defined in `00_Spec/spec.md`.
- Myofascial lines remain the primary anatomical reasoning structure.
- Do not attribute fascial loading findings to Dr. Kwon; his work supplies Level 3 external-force and motion evidence.
- Stable fascial anatomy requires Level 1 or Level 2 support; golf application must be visibly separated and labelled.
- Do not infer force, pressure, torque, impulse, energy transfer, muscle activation, or fascial tension from ordinary video.
- Do not diagnose, predict injury, or prescribe treatment.
- Reuse existing nodes before creating new nodes; do not bulk-rename or migrate the vault.
- Every new note must be linked from `index.md` and at least one contextual note.
- Preserve the user's existing `.obsidian/workspace.json` modification and exclude it from all commits.
- Use Australian/British prose spelling in narrative text while retaining canonical biomechanical terms and existing snake-case IDs.

---

## Planned File Map

### New files

- `03_Movement_Functions/golfer_ground_interaction_model.md` — central Level 3 model and graph traversal hub.
- `03_Movement_Functions/pivoting_moment.md` — horizontal-plane moment from individual foot GRFs about combined COP.
- `03_Movement_Functions/foot_contact_moment.md` — direct torsional foot-ground moment, kept distinct from pivoting and GRF moments.
- `03_Movement_Functions/linear_impulse.md` — time integral of net external force, including sensor requirements.
- `03_Movement_Functions/angular_impulse.md` — time integral of external moment and its relation to angular-momentum change.
- `05_App_Logic/golf_kinetics_observability_boundary.md` — direct-measurement/proxy/prohibited-claim matrix.

### Existing files to modify

- Source/evidence: `00_Spec/sources/dr_kwon_golfer_ground_interaction.md`, `00_Spec/evidence_levels.md`.
- Core mechanics: `03_Movement_Functions/ground_reaction_force.md`, `ground_reaction_moment.md`, `center_of_pressure.md`, `center_of_mass.md`, `moment_arm.md`, `torque.md`, `angular_momentum.md`, `kinematic_sequence.md`, `force_transmission.md`, `energy_transfer.md`, `movement_chain_model.md`.
- Golf graph: `04_Golf_Swing/golf_swing.md`, all six files under `04_Golf_Swing/phases/`, and `end_pelvis_rotation.md`, `top_backswing_position.md`, `max_unweighting.md`, `impact_position.md` under `04_Golf_Swing/positions/`.
- Fascial graph: `01_Fascial_Lines/functional_lines.md`, `back_functional_line.md`, `front_functional_line.md`, `ipsilateral_functional_line.md`, `spiral_line.md`, `deep_front_line.md`, `lateral_line.md`, `superficial_back_line.md`, `superficial_front_arm_line.md`, `superficial_back_arm_line.md`, `deep_front_arm_line.md`, `deep_back_arm_line.md`.
- App/index/log: `05_App_Logic/ai_movement_analysis_layer.md`, `index.md`, `00_Spec/log.md`.

---

### Task 1: Build the Kwon Source Dossier

**Files:**
- Modify: `00_Spec/sources/dr_kwon_golfer_ground_interaction.md`

**Interfaces:**
- Consumes: evidence hierarchy from `00_Spec/spec.md` and `00_Spec/evidence_levels.md`.
- Produces: canonical source IDs, URLs, DOIs, claim locators, definitions, and evidence boundaries used by Tasks 2–5.

- [ ] **Step 1: Capture and verify the primary source register**

Open and verify these sources, recording access date `2026-07-16`:

```text
https://drkwongolf.info/biom/fgmom.html
https://www.drkwongolf.info/biom/grf.html
https://www.drkwongolf.info/biom/events-phases.html
https://drkwongolf.info/biom/kinem-kin.html
https://drkwongolf.info/biom/moment.html
https://drkwongolf.info/biom/oa.html
https://drkwongolf.info/biom/fsp.html
https://doi.org/10.1080/14763141.2019.1586983
https://doi.org/10.1080/14763141.2019.1629617
https://doi.org/10.1080/14763141.2012.660799
```

Expected: each Kwon webpage loads or is documented as inaccessible; each DOI resolves to the stated publication. Do not substitute secondary coaching summaries for inaccessible claims.

- [ ] **Step 2: Replace the one-page summary with a research-program dossier**

Preserve `id: dr_kwon_golfer_ground_interaction`, then add:

```yaml
evidence_level: 3
source_scope: research_program_dossier
primary_urls:
  - https://drkwongolf.info/biom/fgmom.html
  - https://www.drkwongolf.info/biom/grf.html
  - https://www.drkwongolf.info/biom/events-phases.html
peer_reviewed_dois:
  - 10.1080/14763141.2019.1586983
  - 10.1080/14763141.2019.1629617
  - 10.1080/14763141.2012.660799
accessed: 2026-07-16
```

Required markdown sections:

```text
## Definition
## Source Register
## Terminology
## Claim-Level Evidence
## What Kwon Directly Supports
## What Kwon Does Not Directly Support
## Relationships
## Evidence Level
## App Use
## Open Questions
```

The claim table must include: GRF versus GRM; COP versus COM; COP shift versus weight shift; vertical GRF moment about COM; pivoting moment; foot-contact moment; force magnitude versus direction; pressure-mat versus force-plate capability; event/phase timing; and the difference between kinematics and kinetics.

- [ ] **Step 3: Remove or qualify unsupported source claims**

Replace claims such as “Functional Lines convert ground moments into upper-body torque” with this evidence-safe structure:

```text
Kwon supports the external-force and external-moment description of golfer-ground interaction (Level 3). Anatomy Trains supplies the separate structural line model (Level 1). Mapping between those layers is a vault golf interpretation and is not a direct finding of Kwon's research.
```

Expected: no sentence attributes fascia, myofascial elasticity, or MediaPipe scoring to Kwon.

- [ ] **Step 4: Validate the dossier and commit**

Run:

```bash
rg -n "Source Register|Claim-Level Evidence|What Kwon Does Not Directly Support|10.1080/14763141" 00_Spec/sources/dr_kwon_golfer_ground_interaction.md
git diff --check -- 00_Spec/sources/dr_kwon_golfer_ground_interaction.md
```

Expected: all required headings/DOIs appear; `git diff --check` is silent.

Commit:

```bash
git add 00_Spec/sources/dr_kwon_golfer_ground_interaction.md
git commit -m "Expand Dr Kwon evidence dossier"
```

---

### Task 2: Build the Golfer-Ground Mechanics Layer

**Files:**
- Create: `03_Movement_Functions/golfer_ground_interaction_model.md`
- Create: `03_Movement_Functions/pivoting_moment.md`
- Create: `03_Movement_Functions/foot_contact_moment.md`
- Create: `03_Movement_Functions/linear_impulse.md`
- Create: `03_Movement_Functions/angular_impulse.md`
- Modify: `03_Movement_Functions/ground_reaction_force.md`
- Modify: `03_Movement_Functions/ground_reaction_moment.md`
- Modify: `03_Movement_Functions/center_of_pressure.md`
- Modify: `03_Movement_Functions/center_of_mass.md`
- Modify: `03_Movement_Functions/moment_arm.md`
- Modify: `03_Movement_Functions/torque.md`
- Modify: `03_Movement_Functions/angular_momentum.md`
- Modify: `03_Movement_Functions/kinematic_sequence.md`
- Modify: `03_Movement_Functions/force_transmission.md`
- Modify: `03_Movement_Functions/energy_transfer.md`
- Modify: `03_Movement_Functions/movement_chain_model.md`

**Interfaces:**
- Consumes: the claim-level source anchors from Task 1.
- Produces: reusable mechanics IDs and sensor-boundary language used by golf phases, fascial-line interpretations, and app logic.

- [ ] **Step 1: Create the central model with exact moment taxonomy**

Create `golfer_ground_interaction_model.md` with required frontmatter and sections from `00_Spec/spec.md`. Include this taxonomy:

```text
External moment about golfer COM
├── GRF moment: r(COM→foot COP) × foot GRF
├── Pivoting moment: individual foot GRFs about the combined COP/vertical axis
└── Foot-contact moment: direct torsional GRM at the foot-ground interface
```

State that only external moments change whole-system angular momentum, and that a vertical GRF can create a non-zero moment when its line of action does not pass through COM. Do not state that large GRF automatically means efficient interaction.

- [ ] **Step 2: Create focused pivoting- and foot-contact-moment nodes**

Both notes must include definitions, equations or vector descriptions, measurement requirements, phase relevance, links to `ground_reaction_force`, `ground_reaction_moment`, `center_of_pressure`, `angular_impulse`, and `dr_kwon_golfer_ground_interaction`, plus this limitation:

```text
Ordinary single-camera video cannot measure this moment. Apparent foot direction, pelvis rotation, or body motion is not a substitute for force-plate kinetics.
```

- [ ] **Step 3: Create linear- and angular-impulse nodes**

Use these canonical definitions:

```text
Linear impulse: J = ∫F_ext dt = Δp
Angular impulse about COM: J_H = ∫M_ext,COM dt = ΔH_COM
```

Each note must separate direct force-plate integration from camera-observed timing. Link `angular_impulse` to all three moment classes and `angular_momentum`; link `linear_impulse` to `ground_reaction_force` and `center_of_mass`.

- [ ] **Step 4: Correct the existing GRF/GRM/COP/COM/moment terminology**

Apply these exact distinctions across the existing notes:

```text
- COP is the point of application of the resultant GRF, not the body's COM.
- Combined COP location reflects relative vertical forces under the feet; “COP shift” and “weight shift” are not synonyms.
- A pressure mat measures vertical sensor forces and COP, not full 3D GRF/GRM.
- A force plate measures three force components and moment components; two plates permit foot-specific analysis.
- Moment arm is the perpendicular distance from the chosen centre/axis to a force's line of action.
- “Torque” is retained as an alias, but “moment of force” is preferred in Kwon-derived explanations.
```

- [ ] **Step 5: Harden sequencing, force-transmission, energy-transfer, and chain language**

In `kinematic_sequence.md`, explicitly state that temporal peaks in segment angular velocity are kinematics and do not by themselves prove energy transfer. In `force_transmission.md`, `energy_transfer.md`, and `movement_chain_model.md`, separate measured mechanics from the vault's fascial interpretation and Level 5 app hypotheses.

- [ ] **Step 6: Validate bidirectional mechanics links and commit**

Run:

```bash
rg -n "golfer_ground_interaction_model|pivoting_moment|foot_contact_moment|linear_impulse|angular_impulse" 03_Movement_Functions 00_Spec/sources/dr_kwon_golfer_ground_interaction.md
rg -n "COP shift.*weight shift|pressure mat|force plate|line of action" 03_Movement_Functions
git diff --check -- 03_Movement_Functions
```

Expected: each new ID appears in its own file and at least two contextual files; terminology checks find the new safeguards; diff check is silent.

Commit:

```bash
git add 03_Movement_Functions 00_Spec/sources/dr_kwon_golfer_ground_interaction.md
git commit -m "Model golfer ground interaction mechanics"
```

---

### Task 3: Connect Kwon Mechanics to the Six-Phase Golf Graph

**Files:**
- Modify: `04_Golf_Swing/golf_swing.md`
- Modify: `04_Golf_Swing/phases/address_to_shaft_parallel.md`
- Modify: `04_Golf_Swing/phases/shaft_parallel_to_end_pelvis_rotation.md`
- Modify: `04_Golf_Swing/phases/end_pelvis_rotation_to_top_backswing.md`
- Modify: `04_Golf_Swing/golf_swing_transition.md`
- Modify: `04_Golf_Swing/phases/max_unweighting_to_impact.md`
- Modify: `04_Golf_Swing/phases/impact_to_hands_chest_height.md`
- Modify: `04_Golf_Swing/positions/end_pelvis_rotation.md`
- Modify: `04_Golf_Swing/positions/top_backswing_position.md`
- Modify: `04_Golf_Swing/positions/max_unweighting.md`
- Modify: `04_Golf_Swing/positions/impact_position.md`

**Interfaces:**
- Consumes: mechanics IDs and sensor boundaries from Task 2.
- Produces: phase-specific Level 3 relationships and explicit hooks for the fascial-line mappings in Task 4.

- [ ] **Step 1: Add the Kwon event crosswalk without replacing the existing six phases**

Add a table to `golf_swing.md` mapping existing vault events to Kwon terminology only where supported. Use `not yet mapped` when the definitions differ rather than claiming equivalence. Preserve the six phases sourced from `golf_decoded_six_phases_swing`.

- [ ] **Step 2: Add a four-layer evidence block to every phase**

Every phase must contain these headings:

```text
## Source-Defined Boundary
## Golf Biomechanics (Level 3)
## Myofascial-Line Interpretation
## App Observability (Level 5)
```

The Level 3 section may describe only source-supported force/moment direction or timing. The myofascial section must link structural pathways without presenting them as Kwon findings. The app section must state whether the described quantity is direct, camera-observable, hypothesised, or unavailable.

- [ ] **Step 3: Link key boundary positions to mechanics**

Update end-pelvis-rotation, top-backswing, maximum-unweighting, and impact notes with `relevant_to`/relationship-table links to the central model and applicable mechanics. Do not label `max_unweighting` as measured vertical GRF or a jump from pose landmarks.

- [ ] **Step 4: Validate phase coverage and commit**

Run:

```bash
for f in 04_Golf_Swing/phases/*.md 04_Golf_Swing/golf_swing_transition.md; do rg -q "Source-Defined Boundary" "$f" || echo "missing boundary: $f"; rg -q "Myofascial-Line Interpretation" "$f" || echo "missing fascia: $f"; rg -q "App Observability" "$f" || echo "missing app boundary: $f"; done
rg -n "golfer_ground_interaction_model" 04_Golf_Swing
git diff --check -- 04_Golf_Swing
```

Expected: the loop prints nothing; central-model links appear in the golf graph; diff check is silent.

Commit:

```bash
git add 04_Golf_Swing
git commit -m "Link Kwon mechanics to golf phases"
```

---

### Task 4: Make Myofascial Lines the Primary Anatomical Bridge

**Files:**
- Modify: `01_Fascial_Lines/functional_lines.md`
- Modify: `01_Fascial_Lines/back_functional_line.md`
- Modify: `01_Fascial_Lines/front_functional_line.md`
- Modify: `01_Fascial_Lines/ipsilateral_functional_line.md`
- Modify: `01_Fascial_Lines/spiral_line.md`
- Modify: `01_Fascial_Lines/deep_front_line.md`
- Modify: `01_Fascial_Lines/lateral_line.md`
- Modify: `01_Fascial_Lines/superficial_back_line.md`
- Modify: `01_Fascial_Lines/superficial_front_arm_line.md`
- Modify: `01_Fascial_Lines/superficial_back_arm_line.md`
- Modify: `01_Fascial_Lines/deep_front_arm_line.md`
- Modify: `01_Fascial_Lines/deep_back_arm_line.md`

**Interfaces:**
- Consumes: phase-specific mechanics from Task 3 and stable anatomy already cited in each line note.
- Produces: explicit, evidence-labelled force-to-structure-to-line traversal paths.

- [ ] **Step 1: Replace direct Kwon-to-fascia claims with a three-layer template**

Each modified line note must separate:

```text
## Stable Anatomy (Level 1 & 2)
## Golf Application Interpretation (Level 3 & 4 context)
## App Hypotheses (Level 5)
```

Use this wording rule: “Kwon describes the external mechanics; the following line mapping is the vault's Anatomy Trains-based golf interpretation.”

- [ ] **Step 2: Add phase-specific line roles**

Add a relationship table with columns:

```text
Swing phase | External/mechanical context | Anatomical bridge | Line role | Evidence boundary
```

Use only `loading`, `stabilising`, `releasing/decelerating`, or `role uncertain`. Avoid “primary power source,” “whipping fascia,” and quantified elastic-energy claims unless separately supported.

- [ ] **Step 3: Encode the minimum anatomical bridges**

Ensure the graph contains these paths as interpretations, not direct kinetic findings:

```text
foot/ankle -> plantar fascia/deep leg -> Deep Front, Spiral, Lateral, Superficial Back Lines
hip/sacrum -> thoracolumbar fascia -> Back Functional Line
adductors/abdominal wall -> Front Functional Line
ipsilateral trunk/hip linkage -> Ipsilateral Functional Line
rib cage/scapula/shoulder -> relevant Functional and Arm Lines
```

- [ ] **Step 4: Correct overclaiming already present in functional-line notes**

Qualify or remove statements that a line “converts” GRM, directly “drives” clubhead speed, stores a quantified amount of elastic energy, or can be measured directly from shoulder-to-hip distance. Replace “direct proxy for line stretch” with “camera-derived diagonal-distance descriptor; tissue loading remains unknown.”

- [ ] **Step 5: Validate fascial-line separation and commit**

Run:

```bash
rg -n "Kwon describes the external mechanics|Golf Application Interpretation|App Hypotheses" 01_Fascial_Lines
rg -n "direct proxy|converts ground|whipping|primary power" 01_Fascial_Lines
git diff --check -- 01_Fascial_Lines
```

Expected: separation language appears across the reviewed nodes; any risky-phrase matches are either removed or explicitly negated; diff check is silent.

Commit:

```bash
git add 01_Fascial_Lines
git commit -m "Map Kwon mechanics through fascial lines"
```

---

### Task 5: Define the Future-App Observability Boundary

**Files:**
- Create: `05_App_Logic/golf_kinetics_observability_boundary.md`
- Modify: `05_App_Logic/ai_movement_analysis_layer.md`
- Modify: `00_Spec/evidence_levels.md`

**Interfaces:**
- Consumes: mechanics definitions from Task 2, phase hooks from Task 3, fascial interpretation boundaries from Task 4, and current app limitations from `movement_assessment/docs/metrics.md` and `movement_assessment/docs/extending-the-engine.md`.
- Produces: the authoritative future-golf measurement and reporting policy.

- [ ] **Step 1: Create the observability matrix**

Include rows for GRF, GRM, COP, COM, moment arm, pivoting moment, foot-contact moment, linear impulse, angular impulse, angular momentum, pelvis orientation, thorax orientation, pelvis-thorax separation, segment angular velocity, phase timing, hip-midpoint vertical displacement, foot geometry, and diagonal shoulder-hip distance.

Use these columns:

```text
Concept | Gold-standard measurement | Single-camera status | Permitted app label | Prohibited inference
```

Classify single-camera status as exactly one of `unavailable`, `camera-observable descriptor`, or `Level 5 hypothesis`.

- [ ] **Step 2: Retire unsupported metric claims in the AI layer**

Mark Torque Generation Score, COM-COP Separation Score, Functional Line Loading Index, and Energy Transmission Efficiency as unvalidated Level 5 concepts that are not implementable from the current single-camera pipeline. Do not delete their historical design context; add explicit sensor and validation prerequisites.

- [ ] **Step 3: Strengthen the evidence-level policy**

Add this rule to `00_Spec/evidence_levels.md`:

```text
A Level 3 relationship does not upgrade a linked Level 5 proxy into a measured kinetic variable. Camera geometry and timing may describe motion, but they may not be reported as force, pressure, moment, impulse, energy flow, muscle activation, or fascial loading without independent validation and the required instrumentation.
```

- [ ] **Step 4: Validate app-safety language and commit**

Run:

```bash
rg -n "Gold-standard measurement|Prohibited inference|unavailable|camera-observable descriptor|Level 5 hypothesis" 05_App_Logic/golf_kinetics_observability_boundary.md
rg -n "unvalidated|force plate|single-camera" 05_App_Logic/ai_movement_analysis_layer.md 00_Spec/evidence_levels.md
git diff --check -- 05_App_Logic 00_Spec/evidence_levels.md
```

Expected: every status and safeguard is present; diff check is silent.

Commit:

```bash
git add 05_App_Logic 00_Spec/evidence_levels.md
git commit -m "Define golf kinetics observability boundary"
```

---

### Task 6: Integrate the Graph, Recalculate Metrics, and Verify Integrity

**Files:**
- Modify: `index.md`
- Modify: `00_Spec/log.md`
- Modify mechanically: graph-node YAML fields updated by `scripts/update_graph_metrics.py`

**Interfaces:**
- Consumes: every node and relationship created in Tasks 1–5.
- Produces: discoverable index links, append-only operation history, current graph metrics, and a verified vault.

- [ ] **Step 1: Add index routes**

Under Movement Biomechanics, link the central model, pivoting moment, foot-contact moment, linear impulse, and angular impulse. Under AI Application Logic, link the observability boundary. In the source section, describe the Kwon note as a research-program dossier rather than a single-page summary.

- [ ] **Step 2: Append an operation-log entry**

Append a dated `2026-07-16` entry containing:

```text
Research scope and primary sources
New mechanics nodes
Six-phase integration
Myofascial-line integration and evidence boundary
App observability safeguards
Verification performed
```

Do not rewrite earlier log entries.

- [ ] **Step 3: Recalculate graph metrics**

Run:

```bash
python3 scripts/update_graph_metrics.py
```

Expected: command exits 0 and updates relationship counts, hub scores, and centrality fields without changing note prose.

- [ ] **Step 4: Check new-note index and contextual backlinks**

Run:

```bash
for id in golfer_ground_interaction_model pivoting_moment foot_contact_moment linear_impulse angular_impulse golf_kinetics_observability_boundary; do count=$(rg -l "\[\[$id(\||\]\])" --glob '*.md' . | wc -l | tr -d ' '); test "$count" -ge 3 || echo "insufficient links: $id ($count files)"; done
```

Expected: prints nothing. Each new ID occurs in its own note, `index.md`, and at least one contextual note.

- [ ] **Step 5: Check all wikilink targets**

Run this read-only checker:

```bash
python3 -c 'from pathlib import Path; import re; root=Path("."); files=list(root.rglob("*.md")); stems={p.stem for p in files}; missing={}; [(missing.setdefault(t,[]).append(str(p))) for p in files for t in re.findall(r"\[\[([^\]|#]+)",p.read_text(errors="ignore")) if "/" not in t and t not in stems]; print("\n".join(f"{k}: {len(v)}" for k,v in sorted(missing.items())))'
```

Expected: no new missing targets. Compare output with `git show HEAD:index.md` and pre-existing vault state if legacy unresolved links appear; fix only links introduced by this integration.

- [ ] **Step 6: Run evidence-boundary and diff checks**

Run:

```bash
rg -n "MediaPipe.*measure.*(force|pressure|torque|moment|fascial)|direct proxy for.*(fascia|line stretch)" 00_Spec 01_Fascial_Lines 03_Movement_Functions 04_Golf_Swing 05_App_Logic
git diff --check
git status --short
```

Expected: risky-language search has no positive unsupported claims; diff check is silent; status includes intended integration files and the pre-existing `.obsidian/workspace.json` modification.

- [ ] **Step 7: Commit integration metadata without the Obsidian workspace file**

```bash
git add index.md 00_Spec/log.md 00_Spec 01_Fascial_Lines 03_Movement_Functions 04_Golf_Swing 05_App_Logic
git restore --staged .obsidian/workspace.json 2>/dev/null || true
git commit -m "Complete Dr Kwon vault integration"
```

Expected: commit succeeds; `.obsidian/workspace.json` remains modified and uncommitted.

- [ ] **Step 8: Perform final repository verification**

Run:

```bash
git log -7 --oneline
git status --short
git diff --name-only HEAD~6..HEAD
```

Expected: task commits are visible; status shows only the user's pre-existing `.obsidian/workspace.json` change; changed-file list contains only the design, plan, and intended vault integration paths.

