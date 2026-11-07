# ARCHITECTURAL_BRIEF: css_doom_typescript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/yurkagon/Doom-Nukem-CSS.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 138 analyzed artifact(s), 3633 LOC.
- **Load-bearing artifact:** `src/ui/components/Text/index.ts` -- 8 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/levels/level_1/level.ts` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/utils/ResourceLoader/models/AudioLoader.ts` at magnitude 42.78 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 273 |
| Analyzed Artifacts (Scanned) | 138 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 135 |
| Total LOC | 3633 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 50.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6865 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1742 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5491 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 34 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 105 | 1469 | 76.1% |
| CSS | 28 | 2059 | 20.3% |
| MARKDOWN | 1 | 0 | 0.7% |
| PLAINTEXT | 1 | 0 | 0.7% |
| HTML | 1 | 20 | 0.7% |
| JSON | 1 | 18 | 0.7% |
| JAVASCRIPT | 1 | 67 | 0.7% |

## 4.1 SOURCE ENCODINGS
All 138 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 49%, Declarative / Non-Code 18%, Large Core Modules 9%, Callbacks & Closures Files 7%, Generic / Templated Code Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 136 | 98.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 135*

**Composition by Extension & Reason:**
- `.ts`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 23x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 20x Excluded (Explicitly Denied Extension: '.png')
- `.wav`: 10x Excluded (Explicitly Denied Extension: '.wav')
- `.scss`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mp3`: 3x Excluded (Explicitly Denied Extension: '.mp3')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.template`: 1x Excluded (Unsupported Extension: '.template')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.4 | 5.1 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 58.5 | 7.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 2.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.7 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 80.0 | 14.0 | 5.6 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.8 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 33.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8 | 4 | 0 | `src/ui/screens/Menu/Menu.tsx` |
| cleanup | 4 | 3 | 0 | `src/utils/ResourceLoader/models/AudioLoader.ts` |
| guards | 37 | 16 | 1 | `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` |
| danger | 7 | 6 | 0 | `style/index.scss` |
| concurrency | 62 | 13 | 0 | `src/utils/ResourceLoader/models/OperationHandler.ts` |
| connectivity | 176 | 105 | 2 | `src/State/Loader.ts` |
| io | 35 | 20 | 1 | `src/models/House/style.scss` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 6 | 3 | 0 | `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `src/ui/components/Text/Text.tsx` |
| events | 1 | 1 | 0 | `src/utils/ResourceLoader/models/AudioLoader.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 1 | 1 | 0 | `public/index.html` |
| debt | 3 | 3 | 0 | `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx` |
| mutation | 263 | 60 | 6 | `src/models/House/data.ts` |
| dead_code | 45 | 5 | 0 | `src/models/House/style.scss` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 17 | 4 | 0 | `src/helpers/index.ts` |
| ui | 132 | 35 | 4 | `src/ui/screens/About/About.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/models/House/style.scss` (Hits: 12)
- `webpack.config.js` (Hits: 3)
- `public/index.html` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.ts** (`src/ui/components/Text/index.ts`) — 8 inbound connections
2. **index.ts** (`src/ui/components/Screen/index.ts`) — 6 inbound connections
3. **State.ts** (`src/State/State.ts`) — 4 inbound connections
4. **sleep.ts** (`src/utils/sleep.ts`) — 4 inbound connections
5. **types.ts** (`src/State/types.ts`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **level.ts** (`src/levels/level_1/level.ts`) — 12 outbound dependencies
2. **preloadData.ts** (`src/ui/preloadData.ts`) — 12 outbound dependencies
3. **Menu.tsx** (`src/ui/screens/Menu/Menu.tsx`) — 11 outbound dependencies
4. **level.ts** (`src/levels/level_2/level.ts`) — 10 outbound dependencies
5. **Weapon.tsx** (`src/ui/screens/Game/Weapon/Weapon.tsx`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getCharClassName` **(Compute Cores)** (@ `src/ui/components/Text/getCharClassName.ts`) -> Impact: **25.9** | LOC: 37
- `render` **(Generic / Templated Code)** (@ `src/ui/UserInterface.tsx`) -> Impact: **10.0** | LOC: 20
- `load` **(Compute Cores)** (@ `src/utils/ResourceLoader/ResourceLoader.ts`) -> Impact: **8.6** | LOC: 31
- `handleUrl` **(Callbacks & Closures)** (@ `src/utils/ResourceLoader/models/AudioLoader.ts`) -> Impact: **8.6** | LOC: 34
- `load` **(Compute Cores)** (@ `src/utils/ResourceLoader/models/UrlLoader.ts`) -> Impact: **7.4** | LOC: 9
- `render` **(I/O & Config Routines)** (@ `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx`) -> Impact: **6.9** | LOC: 18
- `isAngleBetween` **(Compute Cores)** (@ `src/helpers/angle.ts`) -> Impact: **6.5** | LOC: 10
- `setLevel` **(I/O & Config Routines)** (@ `src/levels/level_1/level.ts`) -> Impact: **6.3** | LOC: 46
- `setLevel` **(I/O & Config Routines)** (@ `src/levels/level_2/level.ts`) -> Impact: **6.3** | LOC: 46
- `render` **(I/O & Config Routines)** (@ `src/ui/screens/Game/Weapon/Weapon.tsx`) -> Impact: **6.3** | LOC: 27

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/utils/ResourceLoader/models` | 4 | 107.78 | 54.51% | 0.0% |
| `src/levels/level_1` | 4 | 64.2 | 7.62% | 0.0% |
| `src/levels/level_2` | 4 | 64.12 | 7.88% | 0.0% |
| `src/utils/ImageProcessor` | 2 | 53.34 | 52.69% | 0.0% |
| `src/sounds/menu` | 4 | 52.32 | 5.12% | 0.0% |
| `src/State` | 4 | 50.17 | 9.74% | 0.0% |
| `src/ui/components/Text` | 6 | 46.93 | 6.19% | 0.0% |
| `src/ui/screens/Game/HUD/HealthBar/Face` | 4 | 44.27 | 17.07% | 0.0% |
| `src/helpers` | 2 | 39.38 | 6.56% | 99.94% |
| `src/sounds/music` | 3 | 39.24 | 5.12% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/helpers/angle.ts` -> **99.9447%** Exposure
- `src/helpers/index.ts` -> **99.9447%** Exposure
- `src/models/House/index.ts` -> **81.7574%** Exposure
- `src/ui/index.tsx` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` -> **100.0%** Exposure
- `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx` -> **100.0%** Exposure
- `src/utils/ResourceLoader/models/AudioLoader.ts` -> **100.0%** Exposure
- `src/utils/ResourceLoader/models/ImageLoader.ts` -> **100.0%** Exposure
- `src/levels/level_2/level.ts` -> **95.8452%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/helpers/angle.ts` -> **5** Orphaned Functions | **0** Duplicates
- `src/helpers/index.ts` -> **5** Orphaned Functions | **0** Duplicates
- `src/models/House/index.ts` -> **2** Orphaned Functions | **0** Duplicates
- `src/ui/index.tsx` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `173` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/utils/ResourceLoader/models/AudioLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.663)
- **Top Global Matches:** file_cluster_10: 6.663, file_cluster_0: 8.594, file_cluster_13: 9.527
- **Magnitude:** 42.78 | **LOC:** 41 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 9.006; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (56.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleUrl` **(Callbacks & Closures)** (Impact: 8.6)
  * `onEnd` **(Callbacks & Closures)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 2`, `concurrency: 3`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.006
  * `Choke Point (Betweenness):` 0.000564 | `Ripple Effect (Closeness):` 0.032515
  * `Imports (Out-Degree: 1):` UrlLoader
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/utils/ImageProcessor/ImageProcessor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.579)
- **Top Global Matches:** file_cluster_16: 7.579, file_cluster_0: 8.133, file_cluster_10: 8.777
- **Magnitude:** 41.82 | **LOC:** 61 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 7.22; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (57.5%), Guard Balance (formerly Safety Score) (52.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyBrightness` **(Parameter Forwarders)** (Impact: 2.5)
  * `createImageElement` **(Stateful Encapsulated Methods)** (Impact: 2.1)
  * `createImageCanvasContext` **(Encapsulated Accessors)** (Impact: 1.9)
  * `getImageData` **(Encapsulated Accessors)** (Impact: 1.8)
  * `getUrlFromImageData` **(Encapsulated Accessors)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 14`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `concurrency: 11`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007299
  * `Imports (Out-Degree: 0):` image-brightness, image-filter-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.659)
- **Top Global Matches:** file_cluster_0: 7.659, file_cluster_11: 8.253, file_cluster_16: 8.55
- **Magnitude:** 31.28 | **LOC:** 55 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 9.449; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFaceState` **(Encapsulated Accessors)** (Impact: 3.6)
  * `startIteration` **(Encapsulated Accessors)** (Impact: 3.5)
  * `render` **(Interface Declarations)** (Impact: 1.2)
  * `componentDidMount` **(State Mutators)** (Impact: 1.1)
  * `componentWillUnmount` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 5`, `concurrency: 1`, `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.449
  * `Choke Point (Betweenness):` 0.001073 | `Ripple Effect (Closeness):` 0.013271
  * `Imports (Out-Degree: 2):` style.scss, types, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/models/ImageLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.201)
- **Top Global Matches:** file_cluster_10: 6.201, file_cluster_0: 7.566, file_cluster_13: 9.066
- **Magnitude:** 29.7 | **LOC:** 26 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 9.006; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.6%), Complexity Load (formerly Cognitive Load) (73.3%), Guard Balance (formerly Safety Score) (57.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleUrl` **(Callbacks & Closures)** (Impact: 6.1)
  * `onEnd` **(Callbacks & Closures)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 10`, `args: 3`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.006
  * `Choke Point (Betweenness):` 0.000564 | `Ripple Effect (Closeness):` 0.032515
  * `Imports (Out-Degree: 1):` UrlLoader
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/ui/components/Text/getCharClassName.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.87)
- **Top Global Matches:** file_cluster_1: 5.87, file_cluster_3: 48.222, file_cluster_8: 70.049
- **Magnitude:** 27.62 | **LOC:** 40 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 8.174; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (20.1%), Complexity Load (formerly Cognitive Load) (16.2%), Test Surface (formerly Verification) (2.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCharClassName` **(Compute Cores)** (Impact: 25.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 17`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0403
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/screens/Menu/Menu.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.304)
- **Top Global Matches:** file_cluster_0: 8.304, file_cluster_10: 9.515, file_cluster_16: 10.819
- **Magnitude:** 24.96 | **LOC:** 97 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 8.26; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (72.9%), Guard Balance (formerly Safety Score) (53.1%), Concurrency Surface (formerly Concurrency) (44.9%), Complexity Load (formerly Cognitive Load) (19.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Generic / Templated Code)** (Impact: 4.0)
  * `startMenu` **(Callbacks & Closures)** (Impact: 2.5)
  * `onMenuInit` **(Encapsulated Accessors)** (Impact: 1.4)
  * `onClick` **(Callbacks & Closures)** (Impact: 1.2)
  * `onClick` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 22`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 2`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.26
  * `Choke Point (Betweenness):` 0.003784 | `Ripple Effect (Closeness):` 0.011679
  * `Imports (Out-Degree: 9):` style.scss, State, BackgroundMusic, react, menu_music, start_menu, ButtonGroup, types...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/helpers/angle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.078)
- **Top Global Matches:** file_cluster_15: 5.078, file_cluster_11: 7.299, file_cluster_2: 7.484
- **Magnitude:** 22.56 | **LOC:** 40 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Connectivity (formerly Api Exposure) (10.6%), Complexity Load (formerly Cognitive Load) (6.9%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isAngleBetween` **(Compute Cores)** (Impact: 6.5)
  * `getAngleBetween` **(Parameter Forwarders)** (Impact: 2.1)
  * `normalize` **(Parameter Forwarders)** (Impact: 1.7)
  * `normalize180` **(Parameter Forwarders)** (Impact: 1.7)
  * `toRad` **(Parameter Forwarders)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 5`
* *Architecture:* `api: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.903
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/ResourceLoader/ResourceLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.616)
- **Top Global Matches:** file_cluster_10: 7.616, file_cluster_15: 8.144, file_cluster_16: 8.8
- **Magnitude:** 22.56 | **LOC:** 48 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 9.634; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.6%), Mutation Surface (formerly State Flux) (57.5%), Guard Balance (formerly Safety Score) (52.1%), Complexity Load (formerly Cognitive Load) (29.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Compute Cores)** (Impact: 8.6)
  * `handler` **(Callbacks & Closures)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 2`, `concurrency: 5`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.634
  * `Choke Point (Betweenness):` 0.003131 | `Ripple Effect (Closeness):` 0.036046
  * `Imports (Out-Degree: 5):` AudioLoader, ImageLoader, OperationHandler, types, sleep
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/State/Loader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.318)
- **Top Global Matches:** file_cluster_10: 6.318, file_cluster_13: 7.163, file_cluster_15: 8.761
- **Magnitude:** 22.14 | **LOC:** 37 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 7.997; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (64.0%), Connectivity (formerly Api Exposure) (60.2%), Guard Balance (formerly Safety Score) (51.4%), Mutation Surface (formerly State Flux) (26.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadResources` **(Callbacks & Closures)** (Impact: 5.8)
  * `addLoadedItem` **(State Mutators)** (Impact: 1.6)
  * `setLoadingStatus` **(State Mutators)** (Impact: 1.6)
  * `onUpdate` **(Callbacks & Closures)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.997
  * `Choke Point (Betweenness):` 0.005108 | `Ripple Effect (Closeness):` 0.035158
  * `Imports (Out-Degree: 3):` ResourceLoader, types, mobx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.342)
- **Top Global Matches:** file_cluster_9: 7.342, file_cluster_0: 12.87, file_cluster_16: 13.06
- **Magnitude:** 21.32 | **LOC:** 31 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 9.247; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (39.0%), Connectivity (formerly Api Exposure) (34.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(I/O & Config Routines)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.247
  * `Choke Point (Betweenness):` 0.000429 | `Ripple Effect (Closeness):` 0.012976
  * `Imports (Out-Degree: 1):` style.scss, Player, mobx-react, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/levels/level_1/level.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 8.431)
- **Top Global Matches:** file_cluster_2: 8.431, file_cluster_15: 8.548, file_cluster_13: 8.894
- **Magnitude:** 19.78 | **LOC:** 92 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 7.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.4%), Guard Balance (formerly Safety Score) (55.0%), Connectivity (formerly Api Exposure) (29.6%), Complexity Load (formerly Cognitive Load) (15.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setLevel` **(I/O & Config Routines)** (Impact: 6.3)
  * `start` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.22
  * `Choke Point (Betweenness):` 0.001342 | `Ripple Effect (Closeness):` 0.007299
  * `Imports (Out-Degree: 11):` floor.jpg, map, preloadData, skybox.jpg, Level, Guard, Zombie, helpers...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/levels/level_2/level.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 8.246)
- **Top Global Matches:** file_cluster_2: 8.246, file_cluster_15: 8.394, file_cluster_13: 8.749
- **Magnitude:** 19.7 | **LOC:** 87 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 7.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Guard Balance (formerly Safety Score) (55.3%), Connectivity (formerly Api Exposure) (29.9%), Complexity Load (formerly Cognitive Load) (16.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setLevel` **(I/O & Config Routines)** (Impact: 6.3)
  * `start` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.22
  * `Choke Point (Betweenness):` 0.001181 | `Ripple Effect (Closeness):` 0.007299
  * `Imports (Out-Degree: 10):` map, preloadData, skybox.jpg, Level, Guard, Zombie, helpers, MedkitItem...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/models/UrlLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.282)
- **Top Global Matches:** file_cluster_7: 7.282, file_cluster_12: 7.759, file_cluster_5: 9.623
- **Magnitude:** 19.06 | **LOC:** 23 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 19.211; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (53.3%), Guard Balance (formerly Safety Score) (51.8%), Connectivity (formerly Api Exposure) (49.9%), Complexity Load (formerly Cognitive Load) (11.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Compute Cores)** (Impact: 7.4)
  * `handleUrl` **(Parameter Forwarders)** (Impact: 3.7)
  * `getExactPath` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 4`, `concurrency: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.03165
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `public/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.534)
- **Top Global Matches:** file_cluster_13: 4.534, file_cluster_2: 5.418, file_cluster_17: 6.666
- **Magnitude:** 18.4 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.903; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (7.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.903
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` icon.png, main.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `webpack.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.808)
- **Top Global Matches:** file_cluster_2: 2.808, file_cluster_17: 5.296, file_cluster_13: 6.369
- **Magnitude:** 18.34 | **LOC:** 70 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.903; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Mutation Surface (formerly State Flux) (14.1%), Complexity Load (formerly Cognitive Load) (5.6%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.903
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` clean-webpack-plugin, copy-webpack-plugin, path, tsconfig-paths-webpack-plugin, uglifyjs-webpack-plugin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.358)
- **Top Global Matches:** file_cluster_10: 4.358, file_cluster_2: 5.876, file_cluster_17: 6.559
- **Magnitude:** 17.24 | **LOC:** 19 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.903; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (53.3%), Complexity Load (formerly Cognitive Load) (8.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 1`
* *Risk/State:* None
* *Architecture:* `concurrency: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.903
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.scss, State, Level, ui
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/models/House/data.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.232)
- **Top Global Matches:** file_cluster_2: 3.232, file_cluster_17: 4.831, file_cluster_13: 5.463
- **Magnitude:** 17.0 | **LOC:** 53 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 5.799; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (19.8%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 43`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010949
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/helpers/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.562)
- **Top Global Matches:** file_cluster_10: 7.562, file_cluster_15: 9.114, file_cluster_11: 10.351
- **Magnitude:** 16.82 | **LOC:** 21 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Connectivity (formerly Api Exposure) (8.2%), Complexity Load (formerly Cognitive Load) (6.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateCoordinateNoiseValue` **(Compute Cores)** (Impact: 4.4)
  * `to` **(Callbacks & Closures)** (Impact: 3.0)
  * `Distance` **(Callbacks & Closures)** (Impact: 1.9)
  * `generateTranslate3d` **(Callbacks & Closures)** (Impact: 1.7)
  * `chance` **(Parameter Forwarders)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`
* *Risk/State:* `unreferenced_by_name: 5`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.903
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/levels/level_1/map.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.365)
- **Top Global Matches:** file_cluster_2: 1.365, file_cluster_17: 4.226, file_cluster_13: 5.374
- **Magnitude:** 16.68 | **LOC:** 38 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 4.461; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (21.5%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009732
  * `Imports (Out-Degree: 0):` MapHandler
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/levels/level_2/map.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.365)
- **Top Global Matches:** file_cluster_2: 1.365, file_cluster_17: 4.226, file_cluster_13: 5.374
- **Magnitude:** 16.68 | **LOC:** 38 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 4.517; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (21.5%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009732
  * `Imports (Out-Degree: 0):` MapHandler
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/preloadData.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.517)
- **Top Global Matches:** file_cluster_2: 4.517, file_cluster_17: 5.184, file_cluster_13: 5.805
- **Magnitude:** 16.52 | **LOC:** 33 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 5.562; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (22.5%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.562
  * `Choke Point (Betweenness):` 0.000215 | `Ripple Effect (Closeness):` 0.007299
  * `Imports (Out-Degree: 4):` background.jpg, State, menu_back, menu_click, menu_music, start_menu, font.png, about.jpg...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/screens/About/About.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.043)
- **Top Global Matches:** file_cluster_0: 8.043, file_cluster_10: 11.366, file_cluster_13: 11.714
- **Magnitude:** 16.44 | **LOC:** 33 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 8.26; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (21.5%), Complexity Load (formerly Cognitive Load) (5.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.26
  * `Choke Point (Betweenness):` 0.002827 | `Ripple Effect (Closeness):` 0.011679
  * `Imports (Out-Degree: 5):` style.scss, react, BackButton, Header, Screen, Text
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/screens/FakeQuit/FakeQuit.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.224)
- **Top Global Matches:** file_cluster_0: 7.224, file_cluster_10: 10.041, file_cluster_13: 10.589
- **Magnitude:** 16.36 | **LOC:** 25 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 8.26; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (21.5%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.26
  * `Choke Point (Betweenness):` 0.00229 | `Ripple Effect (Closeness):` 0.011679
  * `Imports (Out-Degree: 4):` style.scss, react, BackButton, Screen, Text
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/models/OperationHandler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.056)
- **Top Global Matches:** file_cluster_10: 8.056, file_cluster_16: 8.234, file_cluster_15: 8.835
- **Magnitude:** 16.24 | **LOC:** 34 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.541; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (33.5%), Connectivity (formerly Api Exposure) (21.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Defensive Guards)** (Impact: 2.7)
  * `handleOperation` **(Encapsulated Accessors)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 12`, `args: 3`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.541
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.031559
  * `Imports (Out-Degree: 2):` types, sleep
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/levels/level_1/preloadData.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.756)
- **Top Global Matches:** file_cluster_2: 3.756, file_cluster_17: 4.764, file_cluster_13: 5.371
- **Magnitude:** 16.22 | **LOC:** 16 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 4.461; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (22.5%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.461
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.009732
  * `Imports (Out-Degree: 2):` State, Front.png, Side.png, sidingTexture.jpg, doom_e1m1, medkitVoice
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/ui/components/BackButton/BackButton.tsx` (TYPESCRIPT) | Magnitude: 6.42 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, import: 5, ui_framework: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `src/ui/components/Screen/types.ts` (TYPESCRIPT) | Magnitude: 0.68 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 3, indent_spaces: 3, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/items/MedkitItem/MedkitItem.ts` (TYPESCRIPT) | Magnitude: 10.22 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, import: 6, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/levels/level_1/level.ts` (TYPESCRIPT) | Magnitude: 19.78 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 14, import: 12, core_var_decl: 8
- `src/levels/level_2/level.ts` (TYPESCRIPT) | Magnitude: 19.7 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 12, import: 10, core_var_decl: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/ui/components/BackButton/BackButton.tsx` -> **Severity: 0.342** (Bridge: 0.0062 * Flux: 55.0%)
- `src/ui/screens/Menu/Menu.tsx` -> **Severity: 0.276** (Bridge: 0.0038 * Flux: 72.9357%)
- `src/utils/ResourceLoader/ResourceLoader.ts` -> **Severity: 0.18** (Bridge: 0.0031 * Flux: 57.5%)
- `src/State/Loader.ts` -> **Severity: 0.135** (Bridge: 0.0051 * Flux: 26.3522%)
- `src/levels/level_1/level.ts` -> **Severity: 0.127** (Bridge: 0.0013 * Flux: 94.3608%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/State/State.ts` -> **Severity: 2.204** (Embedded: 0.0435 * Error Risk: 50.7142%)
- `src/utils/ResourceLoader/ResourceLoader.ts` -> **Severity: 1.879** (Embedded: 0.036 * Error Risk: 52.1415%)
- `src/utils/ResourceLoader/models/ImageLoader.ts` -> **Severity: 1.861** (Embedded: 0.0325 * Error Risk: 57.2346%)
- `src/utils/ResourceLoader/types.ts` -> **Severity: 1.842** (Embedded: 0.0353 * Error Risk: 52.1415%)
- `src/utils/ResourceLoader/models/AudioLoader.ts` -> **Severity: 1.822** (Embedded: 0.0325 * Error Risk: 56.0418%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/ui/components/Text/Text.tsx` -> **Severity: 2169.7** (Blast Radius: 21.697 * Doc Risk: 100.0%)
- `src/utils/ResourceLoader/models/UrlLoader.ts` -> **Severity: 1921.1** (Blast Radius: 19.211 * Doc Risk: 100.0%)
- `src/ui/components/Screen/Screen.tsx` -> **Severity: 1594.1** (Blast Radius: 15.941 * Doc Risk: 100.0%)
- `src/enemies/Guard/Guard.ts` -> **Severity: 1220.9** (Blast Radius: 12.209 * Doc Risk: 100.0%)
- `src/items/ShotgunItem/ShotgunItem.ts` -> **Severity: 1136.8** (Blast Radius: 11.368 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 124 call pairs -- scoped 27.4%, unique 0.0%, ambiguous 4.8%, external 67.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 124 | 27.4% | 0.0% | 4.8% | 67.7% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
