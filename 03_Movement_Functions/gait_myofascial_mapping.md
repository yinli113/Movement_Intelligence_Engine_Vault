---
id: gait_myofascial_mapping
type: Movement Function
preferred_name: "Gait–Myofascial Line Mapping (Engine Synthesis)"
aliases: [gait fascial mapping, walking line synthesis, anatomy trains in gait]
short_definition: "Engine synthesis mapping Anatomy Trains myofascial lines to gait phases, motion-restriction patterns, compensation signatures, and camera-view observability. Built from the Earls/Myers 'Anatomy Trains in Gait' framework; all line mappings are engine_synthesis (C), not measured kinetics."
domain: gait
evidence_level: 1
source_role: foundational_anatomical_framework
supported_by: [anatomy_trains_myers_2009]
status: reviewed
reviewed_date: 2026-07-26
contains: []
connects_to: [gait_cycle, stance_phase, swing_phase, initial_contact, loading_response, mid_stance, terminal_stance, preswing, initial_swing, midswing, terminal_swing, superficial_front_line, superficial_back_line, lateral_line, spiral_line, deep_front_line, back_functional_line, front_functional_line, gait_observability_boundary]
directly_supported_claims:
  - "Anatomy Trains (Myers) contains a dedicated 'Anatomy Trains in Gait' section by James Earls mapping myofascial meridians onto the gait cycle."
  - "Earls states the Spiral Line is 'especially significant in the dynamic anatomy of walking, as walking is very much a movement derived from rotational forces.'"
  - "Earls describes walking as controlled falling decelerated by long myofascial chains via the stretch–shortening cycle (viscoelastic pre-stress, isometric muscle contraction, elastic recoil)."
  - "The SFL drives swing-phase limb advancement (hip flexion, knee extension, dorsiflexion); the SBL drives stance-phase hip extension and plantarflexion."
app_translation:
  - "A 2D gait app may use this synthesis to traverse from an observed motion restriction or compensation to candidate fascial lines for follow-up assessment."
  - "The app must not report line mapping as measured tissue loading, fascial tension, or causal diagnosis; all mappings remain engine_synthesis (C)."
---

# Gait–Myofascial Line Mapping (Engine Synthesis)

## Definition

This node is the vault's **engine synthesis** mapping of Anatomy Trains myofascial lines onto the gait cycle. It is built from the "Anatomy Trains in Gait" section by James Earls in Myers' *Anatomy Trains* (Ch. 10). It exists so that an app agent observing a gait motion restriction or compensation can traverse the graph to candidate fascial lines — the missing edge flagged by every gait phase node's "Possible myofascial relationships: None directly" placeholder.

## Why it matters

Before this node, the vault graph had **no edge** from a gait observation to a fascial line. The line files linked to golf phases; the gait phase files explicitly deferred fascial mapping to "engine synthesis (C)". As a result, an AI agent reporting on gait could not reason about which line to investigate from an observed restriction. This node provides four edge types that close that gap:

1. **Line → gait phase** — what each line does, and when.
2. **Line → motion-restriction pattern** — which line shortness produces which restriction (reciprocal pairs).
3. **Line → compensation signature** — which compensations a restricted line tends to produce.
4. **View → line observability** — which camera views can observe which line's action, restriction, and compensation.

## Source-derived model (Level 1)

From Earls/Myers, the gait engine rests on three principles:

- **Controlled falling.** Walking is the body falling forward, decelerated by myofascial chains that lengthen under load.
- **Stretch–shortening cycle (SSC).** Viscoelastic pre-stress → isometric muscle contraction (taking up slack) → elastic fascial loading → elastic recoil. Recoil, not concentric contraction, is the preferred propulsive return.
- **Rotational organisation.** Heel strike drives calcaneal/talar medial rotation up the tibia "like a screwdriver"; the Spiral Line manages this rotation. Walking is fundamentally transverse-plane.

All twelve lines are involved; the **Spiral Line is "especially significant"** because gait is rotational. The seven lines below are the vault's (C) prioritization of the most gait-relevant lines for this synthesis — Ch.10 does not rank them as "primary drivers."

## Edge type 1 — Line → gait phase

**Source attribution:** the "Primary gait role" column quotes Myers' planar **Walking** section and/or Earls' **Anatomy Trains in Gait** section (both Ch.10) — these are **(A) source-supported**. The "Phases" column maps those roles onto Perry eight-phase IDs (`initial_swing`, `midswing`, etc.) — this mapping is **(C) engine synthesis**; the source uses heel strike / weight acceptance / toe-off / swing, not the Rancho phase names.

| Line | Primary gait role (A: Myers Walking / Earls) | Phases (C: Perry-phase mapping) |
|---|---|---|
| [[superficial_front_line]] | Drives swing: hip flexion, knee extension, ankle/MTP dorsiflexion (Myers). Anterior tissues lengthen / elastically load as the body progresses over the planted foot; muscle action is often isometric per Earls' SSC framing (not eccentric). Recoil assists **swing initiation**; toe-off propulsion itself is shared with the SBL/LL/DFL catapult (Earls — catapult is multi-line, not SFL-only). | [[initial_swing]], [[midswing]], [[preswing]] |
| [[superficial_back_line]] | Drives stance: hip extension + plantarflexion from heel strike through foot roll-over (Myers). Plantarflexors of the SBL **plus LL and DFL** load the "catapult" for toe-off (Earls — catapult is multi-line, not SBL-only). | [[loading_response]], [[mid_stance]], [[terminal_stance]], [[preswing]] |
| [[lateral_line]] | Frontal-plane stability; prevents weighted hip adduction (Myers). Most range to travel; most adjustment work (Myers). X-fibre pattern controls pelvis–ribcage rotation. | Whole stance; pelvic tilt/shift |
| [[spiral_line]] | **Especially significant** (Earls: "walking is very much a movement derived from rotational forces"). Decelerates pronation + hip flexion + tibial IR at heel strike via tibialis anterior → ITB → upper glute max. Anterior SPL assists foot re-supination before toe-off. Upper SPL manages contralateral counter-rotation. | [[initial_contact]], [[loading_response]], [[terminal_stance]], [[preswing]] |
| [[back_functional_line]] | Posterior pelvic sling (glute max → thoracolumbar fascia → contralateral lat). Brakes hip flexion/IR at heel strike. "Swingwalker" mechanism (Zorn); posterior sling (Vleeming) — both attributed correctly in Earls. | [[initial_contact]], [[loading_response]] |
| [[front_functional_line]] | Counter-rotates trunk: right shoulder + rib cage forward counterbalances left swinging leg (Myers). Winding/unwinding of torso. | [[initial_swing]], [[midswing]] (contralateral pattern) |
| [[deep_front_line]] | Initiates swing (psoas/iliacus from T12/L1) (Myers). Inner-leg stability from medial arch to medial hip; guides hip, prevents excess rotation. Ideally tensions through entire length at toe-off (Earls). | [[preswing]], [[initial_swing]], [[terminal_stance]] |

## Edge type 2 — Line → motion-restriction pattern (reciprocal pairs)

This is the table an app agent needs when a gait report says "restricted [motion]". The logic is fascial-reciprocal: the line that **resists** a motion, when short, restricts that motion. **Entire table is (C) engine synthesis** — derived from line anatomy + fascial-reciprocal logic, not enumerated in the source. Spine-to-spine ROM propagation is NOT supported; only elastic-recoil propagation is.

| Observed restriction | Primary line to investigate | Why (fascial logic) | Confirmatory co-findings |
|---|---|---|---|
| Restricted **knee flexion** | [[superficial_front_line]] | SFL is the knee extensor line; it must lengthen for flexion. Short SFL holds knee in extension. | Limited hip extension (rectus femoris biarticular link) |
| Restricted **knee extension** | [[superficial_back_line]] | SBL crosses posterior knee (hamstrings, gastrocnemius). Short SBL holds knee in flexion. | Tight hamstrings on table; limited hip flexion |
| Restricted **hip extension** | [[superficial_front_line]] | SFL anterior hip structures must lengthen for extension. | Anterior pelvic tilt; limited knee flexion when hip extended |
| Restricted **hip flexion** | [[superficial_back_line]] | SBL posterior chain must lengthen for hip flexion. | Posterior pelvic tilt; tight hamstrings |
| Restricted **ankle dorsiflexion** | [[superficial_back_line]] | SBL plantarflexors (gastroc/soleus) must lengthen for DF. | Tight calf; limited knee flexion in standing |
| Restricted **ankle plantarflexion** | [[superficial_front_line]] | SFL anterior compartment must lengthen for PF. | Shin tightness; dorsiflexor overactivity |
| Restricted **hip internal rotation** (in gait) | [[lateral_line]] / [[spiral_line]] | LL/SPL manage frontal/transverse hip control. | ITB tightness; foot over-pronation |
| Restricted **foot supination** before toe-off | [[spiral_line]] | Anterior SPL (tibialis anterior → ITB) assists supination. | Foot stays pronated; poor push-off |
| Restricted **trunk counter-rotation** | [[front_functional_line]] / [[spiral_line]] | FFL/SPL drive the contralateral winding/unwinding. | Excessive arm swing; eyes drift with pelvis |
| Knee "locked" from full extension | [[deep_front_line]] | (C) general DFL anatomy (not Earls gait): DFL contains popliteus, which unlocks the extended knee. A knee that cannot unlock from full extension is a popliteus **underactivity / failed-unlock** problem (NOT popliteus shortness — short popliteus would bias toward flexion/IR, the opposite). Listed here as a DFL control-failure pattern, not a shortness restriction. | Medial arch dropped; knee tracks medially |
| Restricted **neck rotation** (cervical, in gait) | [[spiral_line]] | Upper SPL (splenii) drives the counter-rotation that keeps eyes forward. | Eyes drift with pelvis; head leads the rotation instead of counter-rotating |
| Restricted **neck extension** (forward head / chin poke) | [[superficial_front_line]] / [[deep_front_line]] | SFL anterior neck (SCM shortness) and/or DFL deep neck (longus colli shortness) hold the cervical spine in flexion. | **Whole-chain effect:** forward head reduces SFL/DFL elastic recoil all the way to the foot — swing-leg return loses power even though no hip flexor is directly tight |
| Restricted **neck flexion** (can't tuck the chin) | [[superficial_back_line]] | SBL posterior neck (suboccipitals, nuchal ligament, occipitofrontalis) holds the cervical spine in extension. | Tight suboccipitals; head held back |
| Restricted **thoracic extension** | [[superficial_front_line]] / [[deep_front_line]] | (C) fascial-reciprocal: the line that resists thoracic extension is the anterior line (SFL/DFL); short SFL/DFL holds the thorax in flexion. (SBL resists thoracic *flexion*, not extension.) | Reduced DFL toe-off engagement; poor swing recoil; forward shoulder posture |
| Restricted **thoracic rotation** | [[spiral_line]] / [[front_functional_line]] | SPL (rhomboid/serratus) and FFL (pectoralis/obliques) drive the contralateral winding/unwinding. | Excessive arm swing (motion exported outward); eyes drift with pelvis |
| Restricted **thoracic lateral flexion** | [[lateral_line]] | LL intercostals/lateral obliques manage side-bend. | Asymmetric shoulder height; lateral trunk lean |
| Restricted **thoracic flexion** | [[superficial_back_line]] | (C) fascial-reciprocal: SBL erector spinae crosses the posterior thoracic spine; short SBL resists thoracic flexion. | Tight thoracic erectors; extended thorax posture |
| Restricted **lumbar extension** (stuck in flexion) | [[superficial_front_line]] | (C) fascial-reciprocal: SFL rectus abdominis crosses the anterior lumbar spine; short SFL holds the lumbar in flexion. | Posterior pelvic tilt / reduced lumbar lordosis (from RA pull); reduced push-off; swing limb feels "heavy" |
| Restricted **lumbar flexion** (stuck in extension) | [[superficial_back_line]] | SBL erector spinae tightness holds the lumbar in extension. | Posterior pelvic tilt; tight lower back; poor shock absorption |
| Restricted **lumbar rotation** | [[spiral_line]] / [[lateral_line]] | SPL/LL obliques drive the rotational component of the winding/unwinding. | Reduced contralateral pattern; excessive arm swing; pelvis and shoulders rotate together |
| Lumbar **lordosis / anterior tilt** (separate pattern, not "stuck in flexion") | [[deep_front_line]] | (C) general DFL anatomy (not Earls gait): short iliopsoas classically presents as anterior pelvic tilt / lumbar lordosis (extension), NOT lumbar flexion. Listed separately to avoid conflating with the lumbar-extension-restriction row above. | Anterior pelvic tilt; lumbar hyperextension |
| Lumbar **shear/instability** (control failure, not restriction) | [[deep_front_line]] | DFL psoas/QL/TVA provide core stability; underactivity → shear instead of restriction. | Pelvic wobble; poor single-limb stance; Trendelenburg-like pattern |

**Counterintuitive note for the agent:** tight hamstrings (SBL) make knee flexion *easier*, not harder. If a gait report shows restricted knee flexion AND tight hamstrings, the SFL is still the primary suspect — the hamstring tightness is a co-find, not the cause.

**Evidence boundary for the restriction-pattern table:** the source (Myers/Earls, Ch.10) directly supports (A) the **line membership** (which muscles/fascia each line contains) and the **line gait roles** (what each line does in which phase). The **restriction-pattern pairings** in this table (short line X → restricted motion Y) are **engine synthesis (C)** derived from line anatomy + fascial-reciprocal logic (the line that resists a motion, when short, restricts that motion). The source does not enumerate these restriction pairings as direct gait findings. The spine rows in particular: the source supports that each line crosses these spine segments and that a spine restriction reduces the DFL/SFL **elastic recoil** distally (box exercise); the source does **not** support that a cervical restriction *causes* a lumbar extension ROM restriction, nor that the chain transmits ROM restrictions segment-to-segment. Treat all spine-to-spine ROM implications as engine synthesis, not measured findings.

## Whole-chain insight (spine → distal elastic recoil)

A restriction in a spine segment can reduce the **elastic recoil** of the myofascial chain many segments away, producing a **distal recoil symptom**. The DFL ideally tensions through its entire length at toe-off: toe extension → ankle DF → knee extension → hip extension/IR/abduction → **thoracic extension** → **cervical balance** (source, Ch.10). If any segment in that chain is restricted, the DFL cannot **load elastic energy** fully, and the elastic recoil that should assist hip flexion into swing is compromised.

**Evidence boundary — what the source supports vs what it does not:**
- **(A) Source-supported:** the DFL tensions through its entire length at toe-off (Ch.10); forward head reduces the ability to load elastic energy through the SFL and DFL (Earls box exercise, Ch.10); a small adjustment in one segment affects the efficiency of elastic recoil many segments distant.
- **(C) Engine synthesis, NOT source-supported:** the source does **not** establish that a cervical restriction *propagates as a lumbar extension range-of-motion restriction*, nor that the chain transmits *range of motion* restrictions segment-to-segment. The chain transmits **elastic tension/recoil**, not necessarily **ROM at each segment**. A cervical fault can reduce distal recoil without restricting lumbar ROM, and lumbar extension ROM can be restricted by local SFL shortness (rectus abdominis) without any cervical involvement.

This is the regional-interdependence logic ([[regional_interdependence]]) applied to gait: a "stiff swing / reduced hip-flexion recoil" finding might **not** be a primary SFL problem — it could be a cervical/thoracic restriction reducing the DFL **elastic recoil** upstream, leaving the SFL to compensate by over-working to flex the hip. (Note: a gait report may label this as "restricted knee flexion" because the knee does not appear to flex normally in swing — but the actual mechanism is loss of elastic contribution to **hip flexion initiation**, not loss of knee-flexion ROM. The knee-flexion observation is a *proxy symptom*; the *driver* might be a spine restriction reducing elastic loading.) The Earls box exercise in the source supports this: moving the head forward (a cervical fault) measurably reduced the elastic return of the leg at the hip, even though gravity stayed constant and no hip flexor was touched directly.

**Agent rule:** when a distal restriction is observed but the distal line looks fine on direct test, check the spine segments upstream for a restriction that could be reducing the DFL/SFL **elastic loading** (not necessarily the distal line's ROM). The candidate driver is a spine restriction reducing elastic recoil, not a spine restriction causing distal ROM restriction.

## Edge type 3 — Line → compensation signature

When a primary line cannot perform its gait role, the body clears the limb or stabilises by other means. These compensations are *secondary line overwork* and are observable in 2D video. **Entire table is (C) engine synthesis** — clinical-reasoning synthesis, not direct source statements.

| Restricted line | Expected compensation | Compensating lines |
|---|---|---|
| [[superficial_front_line]] (can't flex knee for swing) | Hip hike, circumduction, vaulting | [[lateral_line]] (hip hike), [[spiral_line]] (circumduction), [[superficial_back_line]] (vaulting) |
| [[superficial_back_line]] (can't extend hip/plantarflex) | Flat-footed push-off, forward lean, reduced propulsion | [[deep_front_line]] (psoas over-pull), [[superficial_front_line]] (anterior drag) |
| [[lateral_line]] (can't stabilise frontal plane) | Trendelenburg sign, lateral trunk lean over stance leg | [[spiral_line]] (rotational compensation), [[deep_front_line]] (core brace) |
| [[spiral_line]] (can't manage rotation) | Excessive arm swing, eyes drift with pelvis, foot stays pronated | [[front_functional_line]] (arm over-drive), [[lateral_line]] (frontal brace) |
| [[deep_front_line]] (can't initiate swing / unlock knee) | Delayed swing initiation, stiff-knee gait, dropped medial arch | [[superficial_front_line]] (compensatory hip flexion), [[lateral_line]] (hip hike) |

## Edge type 4 — View → line observability

A camera view can only reason about the fascial lines whose anatomical surface it can see. This edge type maps each gait view to the lines it can observe, and — critically — the lines it is **blind** to. This is the view-side observability boundary that complements [[gait_observability_boundary]]. **Entire section is (C) engine synthesis** — the source does not discuss camera views; derived from line anatomy + camera geometry.

| View | Plane revealed | Lines observable | Lines blind / poorly seen |
|---|---|---|---|
| **Side** | Sagittal (flexion/extension) | [[superficial_front_line]], [[superficial_back_line]], [[deep_front_line]] (psoas/sagittal only) | [[lateral_line]], [[spiral_line]] rotation, [[back_functional_line]], [[front_functional_line]], DFL medial arch |
| **Front** | Frontal (abduction/adduction) | [[lateral_line]], [[deep_front_line]] (medial arch / adductors), [[spiral_line]] (upper counter-rotation + foot pronation), [[front_functional_line]] (shoulders) | [[superficial_front_line]] sagittal, [[superficial_back_line]], [[back_functional_line]] posterior |
| **Back** | Posterior coronal + transverse | [[back_functional_line]], [[lateral_line]] (glute med), [[superficial_back_line]] (calf/hamstring), [[spiral_line]] (posterior diagonal + heel) | [[superficial_front_line]] anterior, [[deep_front_line]] deep, [[front_functional_line]] anterior |

**The transverse-plane problem (Spiral Line):** [[spiral_line]] is the transverse-plane line and is the hardest to capture from any single view. Rotation is best seen from above or inferred from a combination. Practical approach: **front + back together** gives the upper SPL (shoulders vs pelvis) + posterior SPL diagonal (glute → lat) + heel mechanics. A single side view will miss SPL restriction patterns even though SPL is "especially significant in gait."

**View → restriction-pattern observability** (combining with edge type 2):

| Observed restriction | Primary line | Best view(s) to catch it | Views that miss it |
|---|---|---|---|
| Restricted **knee flexion** | [[superficial_front_line]] | **Side** (sagittal knee angle) | Front, Back |
| Restricted **knee extension** | [[superficial_back_line]] | **Side** | Front, Back |
| Restricted **hip extension** | [[superficial_front_line]] | **Side** | Front, Back |
| Restricted **ankle dorsiflexion** | [[superficial_back_line]] | **Side** | Front, Back |
| Restricted **hip internal rotation** (in gait) | [[lateral_line]] / [[spiral_line]] | **Front** + **Back** | Side |
| Restricted **foot supination** before toe-off | [[spiral_line]] | **Back** (heel) + **Front** (arch) | Side |
| Restricted **trunk counter-rotation** | [[front_functional_line]] / [[spiral_line]] | **Front** | Side |
| Knee **locked** from full extension | [[deep_front_line]] | **Front** (medial arch) + **Side** (sagittal lock) | Back |
| Trendelenburg / lateral trunk lean | [[lateral_line]] | **Front** + **Back** | Side |
| Dropped medial arch / knee valgus | [[deep_front_line]] | **Front** only | Side, Back |
| Restricted **neck rotation** (cervical) | [[spiral_line]] | **Front** (head vs pelvis) | Side, Back |
| Restricted **neck extension** (forward head) | [[superficial_front_line]] / [[deep_front_line]] | **Side** (cervical angle) | Front, Back |
| Restricted **neck flexion** (can't tuck chin) | [[superficial_back_line]] | **Side** (cervical angle) | Front, Back |
| Restricted **thoracic extension** | [[superficial_front_line]] / [[deep_front_line]] | **Side** (thoracic curve) | Front, Back |
| Restricted **thoracic rotation** | [[spiral_line]] / [[front_functional_line]] | **Front** (shoulders vs pelvis) | Side, Back |
| Restricted **thoracic lateral flexion** | [[lateral_line]] | **Front** + **Back** (shoulder height) | Side |
| Restricted **thoracic flexion** | [[superficial_back_line]] | **Side** (thoracic curve) | Front, Back |
| Restricted **lumbar extension** | [[superficial_front_line]] | **Side** (lumbar curve) | Front, Back |
| Restricted **lumbar flexion** | [[superficial_back_line]] | **Side** (lumbar curve) | Front, Back |
| Restricted **lumbar rotation** | [[spiral_line]] / [[lateral_line]] | **Front** (pelvis vs shoulders) | Side, Back |
| Lumbar **lordosis / anterior tilt** | [[deep_front_line]] | **Side** (lumbar curve) + **Front** (pelvic tilt) | Back |
| Lumbar **shear/instability** | [[deep_front_line]] | **Front** + **Back** (pelvic wobble) | Side |

**View → compensation observability** (combining with edge type 3):

| Compensation | Restricted line | Best view to catch it | Views that miss it |
|---|---|---|---|
| Hip hike | [[superficial_front_line]] | **Front** + **Back** (pelvic level) | Side |
| Circumduction | [[superficial_front_line]] | **Front** (leg swings wide) | Side (partial), Back |
| Vaulting | [[superficial_front_line]] | **Side** (rise onto toes) + **Front** (pelvic rise) | Back |
| Steppage gait | (weak/inhibited dorsiflexors — NOT an SFL-restriction compensation; SFL not firing, opposite problem) | **Side** (excess hip flexion + foot slap) | Front, Back |
| Flat-footed push-off | [[superficial_back_line]] | **Side** (no heel rise) + **Back** (calf) | Front |
| Trendelenburg | [[lateral_line]] | **Front** + **Back** | Side |
| Excessive arm swing | [[front_functional_line]] / [[spiral_line]] | **Front** | Side (partial), Back |
| Eyes drift with pelvis | [[spiral_line]] | **Front** | Side, Back |

**Single-view blind-spot rule for the app:** a side-only gait report can only reason about SFL and SBL. It is blind to LL, DFL, BFL, and most of SPL. A side-only finding of "no restriction observed" must not be reported as "no LL/DFL/BFL/SPL restriction" — those lines were not visible from the view. The app must declare `unavailable_from_this_view` for lines outside the view's observability, not `absent`.

## Worked example — restricted knee flexion in gait

A side-walking gait shows restricted knee flexion. Traversal:

1. **Edge type 2 lookup:** restricted knee flexion → primary line = [[superficial_front_line]].
2. **Edge type 1 confirmation:** SFL anterior tissues lengthen / elastically load during [[loading_response]] (knee flexes ~15° for shock absorption) and during [[terminal_stance]]/[[preswing]] (hip extension tensions anterior tissues for swing recoil). Both gait moments require SFL to yield. (Muscle action is often isometric per Earls' SSC framing, not eccentric.)
3. **Edge type 3 prediction:** expect hip hike / circumduction / vaulting as compensations, driven by [[lateral_line]], [[spiral_line]], [[superficial_back_line]] overwork.
4. **Disambiguation:**
   - If hip extension is also limited → confirms SFL (rectus femoris biarticular).
   - If passive knee flexion is normal but gait flexion is restricted → suspect [[spiral_line]] (rotational coupling, not sagittal).
   - If knee is "locked" from full extension with dropped medial arch → suspect [[deep_front_line]] (popliteus; (C) general DFL anatomy, not Earls gait).
   - **Spine-driver differential (see Whole-chain insight):** if knee flexion is restricted but the SFL looks fine on direct test, the upstream issue is **reduced elastic loading**, not distal ROM restriction. A restricted **thoracic extension** (SFL/DFL) or a **forward head** (SFL/DFL cervical) can reduce the DFL/SFL **elastic recoil** at toe-off (source-supported, (A)). The mechanism is loss of elastic contribution to hip flexion into swing — **not** cervical-causes-lumbar ROM restriction (unsupported). Side view catches thoracic/cervical sagittal angle; front view catches cervical rotation.

## Evidence boundary (A vs C, per edge type)

This hub mixes directly source-supported claims with engine synthesis. The app agent must respect the boundary:

| Edge type | (A) Source-supported (Myers/Earls Ch.10) | (C) Engine synthesis (not in source) |
|---|---|---|
| **1. Line → gait phase** | Line membership; line gait roles (SFL drives swing, SBL drives stance, LL frontal stability, SPL rotational deceleration, BFL posterior sling, FFL counter-rotation, DFL swing initiation + full-length tension at toe-off); SSC; controlled falling; rotational organisation; "SPL especially significant" | Specific phase-timing claims beyond what the source states |
| **2. Line → restriction pattern** | Line anatomy (which structures each line crosses) | The restriction pairings (short line X → restricted motion Y) are derived from line anatomy + fascial-reciprocal logic, not enumerated in the source. Spine-to-spine ROM propagation is NOT supported — only elastic-recoil propagation is. |
| **3. Line → compensation signature** | The source describes what each line does in gait | The compensation patterns (hip hike, circumduction, etc. when a line is restricted) are clinical-reasoning synthesis, not direct source statements |
| **4. View → line observability** | Nothing — the source does not discuss camera views | Entirely engine synthesis from line anatomy + camera geometry |

**Agent rule:** when reporting a finding, label it (A) if it is a direct line-membership or line-gait-role claim from Ch.10; label it (C) if it is a restriction pairing, compensation signature, or view-observability claim. Never report a (C) claim as a measured finding or as a source-direct statement. The spine-to-spine ROM propagation claim in particular must not be reported as established — only the elastic-recoil propagation is source-supported.

## What a 2D app can observe

- Knee-flexion angle proxy during [[loading_response]] and [[initial_swing]] (side view).
- Hip-flexion/extension range and hip-hike / circumduction / vaulting compensations (side + front + back depending on compensation — see edge type 4).
- Foot contact pattern (heel vs flat), pelvic levelness, trunk sway, arm-swing amplitude (view-dependent).
- Phase bounds (foot-strike, toe-off, heel-rise) for timing (side view).
- **View dependency:** each camera view can only observe the lines whose anatomical surface it sees (see edge type 4). A side-only report can reason about SFL/SBL; a front-only report can reason about LL/DFL/upper SPL; a back-only report can reason about BFL/LL/SBL/posterior SPL. Lines outside the view's observability must be reported as `unavailable_from_this_view`, not as `absent`.

## What the app must not infer

- Fascial tension, line loading, stored elastic energy, or muscle activation from any of the above.
- That an observed restriction is *caused by* a specific line shortness — the mapping is a candidate list for follow-up assessment, not a diagnosis.
- Joint moments, GRF, pressure, or any kinetic quantity.
- Causal etiology of an abnormal gait pattern.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[swing_phase]], [[initial_contact]], [[loading_response]], [[mid_stance]], [[terminal_stance]], [[preswing]], [[initial_swing]], [[midswing]], [[terminal_swing]], [[superficial_front_line]], [[superficial_back_line]], [[lateral_line]], [[spiral_line]], [[deep_front_line]], [[back_functional_line]], [[front_functional_line]], [[gait_observability_boundary]], [[observational_gait_analysis]].

## Sources

- [[anatomy_trains_myofascial_thomas_w_myers]] — Ch. 10, "Anatomy Trains in Gait" by James Earls; Ch. 10 "Walking" planar analysis by Myers.

## Evidence-separation rules

- **(A)** Source-derived framework (SSC, controlled falling, rotational organisation, line membership, "Spiral Line is especially significant") — directly from Myers/Earls, Ch. 10.
- **(B)** Cross-links to gait phase nodes — same Level 1 domain (Chambers & Sutherland / Perry & Burnfield).
- **(C)** All four edge-type tables (line→phase role, line→restriction pattern, line→compensation signature, view→line observability) are `engine_synthesis`. They are the vault's Anatomy Trains-based interpretation, not measured kinetics or causal proof. No table entry upgrades a 2D proxy to a measured variable.
