# ARCHITECTURAL_BRIEF: Excalibur
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/excaliburjs/Excalibur.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1797 |
| Analyzed Artifacts (Scanned) | 738 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1059 |
| Total LOC | 80574 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 41.1% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.525 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2608 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 20.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3976 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 21 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 546 | 71257 | 74.0% |
| HTML | 119 | 1810 | 16.1% |
| JSON | 19 | 604 | 2.6% |
| GLSL | 19 | 459 | 2.6% |
| JAVASCRIPT | 10 | 5951 | 1.4% |
| PLAINTEXT | 8 | 1 | 1.1% |
| MARKDOWN | 7 | 0 | 0.9% |
| XML | 4 | 1 | 0.5% |
| CSS | 4 | 434 | 0.5% |
| PYTHON | 2 | 57 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.01; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 26%, Declarative / Non-Code 25%, Large Core Modules 13%, Interface Declarations Files 11%, Callbacks & Closures Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 722 | 97.8% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 14 | 1.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1059*

**Composition by Extension & Reason:**
- `.png`: 597x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 73x Excluded (Explicitly Denied Extension: '.gif')
- `.ts`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Packed Payload Guard (Impossible Density: 4.66 hits/line)
- `.md`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3214 LOC)
- `.json`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14105 LOC), 1x Excluded (Static Asset Blob without Intent: 2081 LOC)
- `.mp3`: 18x Excluded (Explicitly Denied Extension: '.mp3')
- `.jpg`: 13x Excluded (Explicitly Denied Extension: '.jpg')
- `.mp4`: 12x Excluded (Explicitly Denied Extension: '.mp4')
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 9x Excluded (Explicitly Denied Extension: '.woff2')
- `.css`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 16.9 | 4.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 46.6 | 57.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.5 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 68.0 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 76.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.9 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 27.7 | 1.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 35.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 209 | 67 | 0 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| cleanup | 268 | 71 | 0 | `src/spec/vitest/engine-spec.ts` |
| guards | 3162 | 284 | 13 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| danger | 1369 | 213 | 4 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| concurrency | 1721 | 159 | 6 | `src/spec/vitest/coroutine-spec.ts` |
| connectivity | 4609 | 475 | 15 | `src/engine/events.ts` |
| io | 463 | 168 | 1 | `sandbox/index.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 3 | 0 | `scripts/apidocs.js` |
| time | 53 | 26 | 0 | `src/engine/entity-component-system/system-manager.ts` |
| serialization | 17 | 9 | 0 | `src/engine/util/serializer.ts` |
| regex | 41 | 12 | 0 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| events | 2476 | 302 | 7 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| tests | 7439 | 133 | 24 | `src/spec/vitest/action-spec.ts` |
| docs | 2714 | 344 | 10 | `src/engine/engine.ts` |
| debt | 541 | 134 | 2 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| mutation | 21911 | 655 | 80 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| dead_code | 125 | 69 | 0 | `sandbox/src/game.ts` |
| credential | 2 | 1 | 0 | `src/spec/vitest/image-source-spec.ts` |
| threat | 298 | 50 | 0 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| ml_ai | 1035 | 159 | 3 | `src/spec/vitest/action-spec.ts` |
| ui | 192 | 35 | 0 | `sandbox/excalibur-dev-tools/dev-tools.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `sandbox/index.html` (Hits: 132)
- `src/spec/vitest/graph-spec.ts` (Hits: 25)
- `playground/index.html` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **vector.ts** (`src/engine/math/vector.ts`) — 96 inbound connections
2. **color.ts** (`src/engine/color.ts`) — 47 inbound connections
3. **test-utils.ts** (`src/spec/__util__/test-utils.ts`) — 45 inbound connections
4. **engine.ts** (`src/engine/engine.ts`) — 41 inbound connections
5. **log.ts** (`src/engine/util/log.ts`) — 41 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/engine/index.ts`) — 67 outbound dependencies
2. **index.ts** (`src/engine/graphics/index.ts`) — 46 outbound dependencies
3. **index.ts** (`src/engine/collision/index.ts`) — 37 outbound dependencies
4. **engine.ts** (`src/engine/engine.ts`) — 37 outbound dependencies
5. **excalibur-graphics-context-webgl.ts** (`src/engine/graphics/context/excalibur-graphics-context-webgl.ts`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `draw` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/material-renderer/material-renderer.ts`) -> Impact: **172.3** | LOC: 158
- `draw` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/image-renderer/image-renderer.ts`) -> Impact: **147.0** | LOC: 157
- `draw` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/image-renderer-v2/image-renderer-v2.ts`) -> Impact: **143.9** | LOC: 95
- `constructor` **(Compute Cores)** (@ `src/engine/engine.ts`) -> Impact: **116.7** | LOC: 270
  * *Intent:* * height: 0, // the height of the canvas * enableCanvasTransparency: true, // the transparencySection of the canvas * canvasElementId: '', // the DOM ...
- `constructor` **(Defensive Guards)** (@ `src/engine/graphics/font.ts`) -> Impact: **86.6** | LOC: 34
- `rayCast` **(Many-Argument Workhorses)** (@ `src/engine/collision/detection/sparse-hash-grid-collision-processor.ts`) -> Impact: **77.0** | LOC: 119
- `constructor` **(Compute Cores)** (@ `src/engine/actor.ts`) -> Impact: **72.5** | LOC: 120
  * *Intent:* // #endregion /** * * @param config */
- `glTypeToUniformTypeName` **(Compute Cores)** (@ `src/engine/graphics/context/shader.ts`) -> Impact: **71.4** | LOC: 112
  * *Intent:* /** * */
- `drawImage` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/excalibur-graphics-context-webgl.ts`) -> Impact: **68.4** | LOC: 39
- `FindContactSeparation` **(Compute Cores)** (@ `src/engine/collision/colliders/collision-jump-table.ts`) -> Impact: **61.5** | LOC: 86

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/spec/vitest` | 127 | 17316.83 | 8.49% | 0.0% |
| `__monolith__` | 17 | 5177.32 | 2.57% | 9.56% |
| `src/engine` | 24 | 4624.66 | 25.86% | 13.76% |
| `src/engine/graphics` | 33 | 3732.44 | 32.99% | 3.72% |
| `sandbox/excalibur-dev-tools` | 2 | 3352.02 | 28.84% | 98.1% |
| `src/engine/graphics/context` | 19 | 2508.42 | 29.7% | 19.46% |
| `src/engine/math` | 19 | 2349.3 | 26.68% | 1.92% |
| `src/engine/util` | 28 | 1975.63 | 33.01% | 8.18% |
| `src/engine/actions/action` | 22 | 1864.92 | 45.17% | 0.0% |
| `src/engine/collision/detection` | 11 | 1714.42 | 27.41% | 7.91% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `sandbox/excalibur-dev-tools/dev-tools.d.ts` -> **100.0%** Exposure
- `sandbox/tests/postprocessor/main.ts` -> **100.0%** Exposure
- `sandbox/tests/transition/index.ts` -> **100.0%** Exposure
- `src/engine/interfaces/lifecycle-events.ts` -> **100.0%** Exposure
- `src/engine/events.ts` -> **99.9998%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `sandbox/stats/stats.js` -> **100.0%** Exposure
- `src/engine/camera.ts` -> **100.0%** Exposure
- `src/engine/collision/colliders/polygon-collider.ts` -> **100.0%** Exposure
- `src/engine/collision/colliders/separating-axis.ts` -> **100.0%** Exposure
- `src/engine/collision/detection/collision-contact.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **0** Orphaned Functions | **93** Duplicates
- `src/engine/events.ts` -> **0** Orphaned Functions | **32** Duplicates
- `src/engine/interfaces/lifecycle-events.ts` -> **0** Orphaned Functions | **23** Duplicates
- `src/engine/input/gamepad.ts` -> **0** Orphaned Functions | **20** Duplicates
- `src/engine/tile-map/tile-map.ts` -> **0** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `285` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/engine/event-emitter.ts` (TYPESCRIPT) -> Cumulative Risk: **731.93**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.01)
- **Magnitude:** 162.9 | **LOC:** 144 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9995%), Safety Score (97.0892%)
- **Heaviest Functions:** `emit` (Compute Cores, Impact: 16.8), `off` (Defensive Guards, Impact: 10.9), `on` (Generic / Templated Code, Impact: 5.6)

### 2. `src/engine/input/gamepad.ts` (TYPESCRIPT) -> Cumulative Risk: **722.44**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.15)
- **Magnitude:** 315.22 | **LOC:** 564 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9998%), State Flux (94.9429%), Safety Score (85.6167%)
- **Heaviest Functions:** `update` (I/O & Config Routines, Impact: 27.9), `_clonePad` (Compute Cores, Impact: 8.0), `_isGamepadValid` (Callbacks & Closures, Impact: 7.9)

### 3. `src/engine/tile-map/tile-map.ts` (TYPESCRIPT) -> Cumulative Risk: **696.63**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.29)
- **Magnitude:** 791.78 | **LOC:** 1004 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Tech Debt (96.4393%), Safety Score (90.7288%)
- **Heaviest Functions:** `checkAndCombine` (Many-Argument Workhorses, Impact: 45.9), `_updateColliders` (I/O & Config Routines, Impact: 30.6), `debug` (Compute Cores, Impact: 30.6)

### 4. `src/engine/resources/gif.ts` (TYPESCRIPT) -> Cumulative Risk: **680.64**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.06)
- **Magnitude:** 599.4 | **LOC:** 635 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8238%), Concurrency (93.1845%)
- **Heaviest Functions:** `arrayToImage` (Defensive Guards, Impact: 28.2), `lzwDecode` (Compute Cores, Impact: 26.0), `cpRow` (Many-Argument Workhorses, Impact: 20.2)

### 5. `src/engine/entity-component-system/components/transform-component.ts` (TYPESCRIPT) -> Cumulative Risk: **670.19**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.22)
- **Magnitude:** 125.5 | **LOC:** 199 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (88.3804%), Safety Score (82.3635%)
- **Heaviest Functions:** `coordPlane` (Defensive Guards, Impact: 6.1), `onAdd` (Callbacks & Closures, Impact: 4.9), `deserialize` (Type Conversions, Impact: 4.8)

### 6. `src/engine/resources/sound/sound-manager.ts` (TYPESCRIPT) -> Cumulative Risk: **656.17**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.03)
- **Magnitude:** 344.48 | **LOC:** 416 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9983%), Concurrency (99.2939%), Documentation (86.5385%)
- **Heaviest Functions:** `addChannel` (Compute Cores, Impact: 13.3), `play` (Defensive Guards, Impact: 13.0), `toggle` (Compute Cores, Impact: 12.5)

### 7. `src/engine/director/default-loader.ts` (TYPESCRIPT) -> Cumulative Risk: **654.46**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.01)
- **Magnitude:** 198.16 | **LOC:** 288 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (97.9699%), Safety Score (90.1792%)
- **Heaviest Functions:** `isLoaderConstructor` (Defensive Guards, Impact: 8.6), `load` (Callbacks & Closures, Impact: 7.7), `constructor` (Defensive Guards, Impact: 7.3)

### 8. `src/engine/util/clock.ts` (TYPESCRIPT) -> Cumulative Risk: **653.36**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.76)
- **Magnitude:** 198.64 | **LOC:** 322 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (88.6231%), Tech Debt (87.9974%)
- **Heaviest Functions:** `update` (Compute Cores, Impact: 16.4), `__runScheduledCbs` (Compute Cores, Impact: 11.0), `constructor` (Defensive Guards, Impact: 10.4)

### 9. `src/engine/entity-component-system/entity.ts` (TYPESCRIPT) -> Cumulative Risk: **651.06**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.09)
- **Magnitude:** 432.44 | **LOC:** 709 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), State Flux (99.9826%), Safety Score (84.6541%)
- **Heaviest Functions:** `constructor` (Compute Cores, Impact: 21.8), `removeComponent` (Generic / Templated Code, Impact: 15.6), `addComponent` (Type Conversions, Impact: 15.4)

### 10. `src/engine/resources/sound/sound.ts` (TYPESCRIPT) -> Cumulative Risk: **649.34**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.18)
- **Magnitude:** 409.46 | **LOC:** 555 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), State Flux (99.9911%), Safety Score (81.7409%)
- **Heaviest Functions:** `constructor` (Defensive Guards, Impact: 27.4), `play` (Defensive Guards, Impact: 24.1), `wireEngine` (Callbacks & Closures, Impact: 9.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sandbox/excalibur-dev-tools/dev-tools.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3351.64 | **LOC:** 5255 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.6862%), Tech Debt (96.1928%)
**Top Internal Functions/Classes:**
  * `_processPointerToEntity` **(Defensive Guards)** (Impact: 32.5)
  * `createMonitor` **(Defensive Guards)** (Impact: 23.9)
  * `vn` **(Compute Cores)** (Impact: 23.2)
  * `rgb` **(Compute Cores)** (Impact: 23.2)
  * `S` **(Defensive Guards)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 822
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 821`, `structural_boundaries: 1053`, `args: 981`, `func_start: 708`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 212`, `high_risk_execution: 2`, `state_mutation: 424`, `duplicate_logic: 93`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 353`, `test: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00271
  * `Imports (Out-Degree: 0):` excalibur
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/spec/vitest/excalibur-graphics-context-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2664.3 | **LOC:** 1223 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.7764%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 53 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 332
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 101`, `args: 63`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 160`, `fragile_debt: 1`
* *Architecture:* `concurrency: 67`, `import: 2`
* *Defense:* `safety: 5`, `test: 128`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spec/vitest/sound-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1656.27 | **LOC:** 612 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.6137%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 272
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 174`, `args: 118`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 41`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 67`, `import: 6`
* *Defense:* `safety: 6`, `test: 123`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` sound, util, web-audio, test-utils, @excalibur, context
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/engine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 913.44 | **LOC:** 1906 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1125%), Tech Debt (19.8998%)
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 116.7)
    * *Intent:* * height: 0, // the height of the canvas * enableCanvasTransparency: true, // the transparencySectio...
  * `start` **(Defensive Guards)** (Impact: 19.0)
  * `_initialize` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* /** * Initializes the internal canvas, rendering context, display mode, and native event listeners *...
  * `_monitorPerformanceThresholdAndTriggerFallback` **(I/O & Config Routines)** (Impact: 15.6)
  * `useCanvas2DFallback` **(I/O & Config Routines)** (Impact: 15.1)
    * *Intent:* /** * Switches the engine's graphics context to the 2D Canvas. * @warning Some features of Excalibur...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 92
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 198`, `args: 113`, `func_start: 99`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 123`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 122`, `concurrency: 37`, `import: 47`
* *Defense:* `safety: 34`, `doc: 135`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.034581 | `Ripple Effect (Closeness):` 0.116164
  * `Imports (Out-Degree: 32):` , actor, physics-config, color, context, debug-config, default-loader, director...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `src/engine/tile-map/tile-map.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 791.78 | **LOC:** 1004 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.6101%), Tech Debt (96.4393%)
**Top Internal Functions/Classes:**
  * `checkAndCombine` **(Many-Argument Workhorses)** (Impact: 45.9)
    * *Intent:* /** * Potentially merges the current collider into a list of previous ones, mutating the list * If c...
  * `_updateColliders` **(I/O & Config Routines)** (Impact: 30.6)
    * *Intent:* /** * Tiles colliders based on the solid tiles in the tilemap. */
  * `debug` **(Compute Cores)** (Impact: 30.6)
  * `constructor` **(Compute Cores)** (Impact: 20.7)
    * *Intent:* /** * @param options */
  * `onPostDraw` **(Many-Argument Workhorses)** (Impact: 20.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 148`, `args: 87`, `func_start: 84`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 109`, `planned_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `api: 101`, `concurrency: 13`, `import: 29`
* *Defense:* `safety: 23`, `doc: 48`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.191
  * `Choke Point (Betweenness):` 0.005641 | `Ripple Effect (Closeness):` 0.086209
  * `Imports (Out-Degree: 23):` body-component, bounding-box, collider-component, collider, composite-collider, shape, collision-type, debug...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/spec/vitest/image-source-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 731.58 | **LOC:** 446 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.3763%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 84
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 59`, `args: 24`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 17`
* *Architecture:* `io: 7`, `concurrency: 49`, `import: 2`
* *Defense:* `safety: 3`, `test: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` image-renderer, @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spec/vitest/animation-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 698.83 | **LOC:** 937 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4332%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 44`, `args: 37`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 11`
* *Architecture:* `concurrency: 4`, `import: 2`
* *Defense:* `safety: 2`, `test: 160`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` graphics, @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spec/vitest/coroutine-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 675.35 | **LOC:** 377 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5205%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 196
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 57`, `args: 32`, `func_start: 8`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `concurrency: 41`, `import: 2`
* *Defense:* `test: 69`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-utils, @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/screen.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 673.86 | **LOC:** 1232 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.4236%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `enterFullscreen` **(Defensive Guards)** (Impact: 36.6)
    * *Intent:* /** * Requests to enter fullscreen using the browser fullscreen api, requires user interaction to be...
  * `_computeFitAndZoom` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `applyResolutionAndViewport` **(I/O & Config Routines)** (Impact: 17.2)
  * `_setResolutionAndViewportByDisplayMode` **(Compute Cores)** (Impact: 15.4)
    * *Intent:* /** * Sets the resolution and viewport based on the selected display mode. */
  * `_computeFitAndFill` **(Many-Argument Workhorses)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 125`, `args: 77`, `func_start: 76`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 132`, `dead_code: 3`
* *Architecture:* `io: 2`, `api: 74`, `concurrency: 9`, `import: 10`
* *Defense:* `safety: 24`, `doc: 63`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` camera, index, event-emitter, excalibur-graphics-context, excalibur-graphics-context-2d-canvas, excalibur-graphics-context-webgl, vector, browser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/camera.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 612.54 | **LOC:** 901 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `action` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `move` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* /** * This moves the camera focal point to the specified position using specified easing function. C...
  * `zoomOverTime` **(Many-Argument Workhorses)** (Impact: 11.4)
    * *Intent:* /** * Zooms the camera in or out by the specified scale over the specified duration. * If no duratio...
  * `_initialize` **(State Mutators)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 70 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 123`, `args: 78`, `func_start: 71`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 100`
* *Architecture:* `api: 95`, `concurrency: 15`, `import: 20`
* *Defense:* `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.308
  * `Choke Point (Betweenness):` 0.001435 | `Ripple Effect (Closeness):` 0.073064
  * `Imports (Out-Degree: 14):` actor, bounding-box, engine, event-emitter, events, graphics, excalibur-graphics-context, lifecycle-events...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/engine/resources/gif.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 599.4 | **LOC:** 635 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.1208%), Tech Debt (14.9005%)
**Top Internal Functions/Classes:**
  * `arrayToImage` **(Defensive Guards)** (Impact: 28.2)
  * `lzwDecode` **(Compute Cores)** (Impact: 26.0)
  * `cpRow` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `parseUnknownExt` **(Compute Cores)** (Impact: 14.3)
  * `parseUnknownAppExt` **(Compute Cores)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 92 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 98`, `args: 41`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 139`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 28`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 11`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.083
  * `Choke Point (Betweenness):` 0.000179 | `Ripple Effect (Closeness):` 0.001807
  * `Imports (Out-Degree: 6):` animation, image-source, sprite, sprite-sheet, index, resource
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 595.94 | **LOC:** 861 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.9451%), Tech Debt (11.9042%)
**Top Internal Functions/Classes:**
  * `drawImage` **(Many-Argument Workhorses)** (Impact: 68.4)
  * `constructor` **(Defensive Guards)** (Impact: 42.6)
  * `flush` **(I/O & Config Routines)** (Impact: 30.7)
    * *Intent:* /** * Flushes all batched rendering to the screen */
  * `draw` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `drawImage` **(Many-Argument Workhorses)** (Impact: 22.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 122`, `args: 70`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 90`, `fragile_debt: 2`
* *Architecture:* `api: 57`, `import: 35`
* *Defense:* `safety: 21`, `doc: 13`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.806
  * `Choke Point (Betweenness):` 0.014624 | `Ripple Effect (Closeness):` 0.065641
  * `Imports (Out-Degree: 31):` color, flags, garbage-collector, affine-matrix, matrix, vector, screen, log...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/spec/vitest/sprite-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 513.99 | **LOC:** 329 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.0684%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Concurrency (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 39`, `args: 16`, `func_start: 7`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `io: 3`, `concurrency: 28`, `import: 2`
* *Defense:* `safety: 4`, `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/collision/detection/dynamic-tree.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 511.56 | **LOC:** 503 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.8007%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_balance` **(Compute Cores)** (Impact: 32.5)
    * *Intent:* /** * Balances the tree about a node */
  * `_insert` **(Compute Cores)** (Impact: 30.9)
    * *Intent:* /** * Inserts a node into the dynamic tree */
  * `updateCollider` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* /** * Updates the dynamic tree given the current bounds of each body being tracked */
  * `rayCastQuery` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* /** * Queries the Dynamic Axis Aligned Tree for bodies that could be intersecting. By default the ra...
  * `query` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* /** * Queries the Dynamic Axis Aligned Tree for bodies that could be colliding with the provided bod...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 54`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `state_mutation: 106`, `dead_code: 1`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `safety: 2`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.903
  * `Choke Point (Betweenness):` 0.000693 | `Ripple Effect (Closeness):` 0.059036
  * `Imports (Out-Degree: 7):` .., entity, id, ray, log, body-component, bounding-box, physics-config
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/engine/collision/colliders/polygon-collider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 504.48 | **LOC:** 739 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.0842%), Tech Debt (10.4397%)
**Top Internal Functions/Classes:**
  * `triangulate` **(I/O & Config Routines)** (Impact: 27.9)
    * *Intent:* /** * Triangulate the polygon collider using the "Ear Clipping" algorithm. * Returns a new {@apilink...
  * `isConvex` **(I/O & Config Routines)** (Impact: 13.9)
    * *Intent:* /** * Returns if the polygon collider is convex, Excalibur does not handle non-convex collision shap...
  * `rayCast` **(Defensive Guards)** (Impact: 13.7)
    * *Intent:* /** * Casts a ray into the polygon and returns a vector representing the point of contact (in world ...
  * `findEarTip` **(I/O & Config Routines)** (Impact: 13.1)
    * *Intent:* /** * Calculate the area of the triangle */ // function triangleArea(a: Vector, b: Vector, c: Vector...
  * `getClosestLineBetween` **(Compute Cores)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 86`, `args: 46`, `func_start: 41`, `class_start: 2`
* *Risk/State:* `state_mutation: 90`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 35`, `import: 18`
* *Defense:* `safety: 3`, `doc: 38`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.606
  * `Choke Point (Betweenness):` 0.000525 | `Ripple Effect (Closeness):` 0.061565
  * `Imports (Out-Degree: 16):` .., color, line-segment, projection, ray, transform, vector, bounding-box...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/engine/actions/action-context.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 497.36 | **LOC:** 575 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1245%), Tech Debt (9.5494%)
**Top Internal Functions/Classes:**
  * `moveTo` **(Compute Cores)** (Impact: 24.9)
  * `moveBy` **(Compute Cores)** (Impact: 23.1)
  * `scaleTo` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `meet` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* /** * This method will cause the entity to move towards another until they * collide "meet" at a spe...
  * `scaleBy` **(Many-Argument Workhorses)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 61 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 85`, `args: 48`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 76`, `planned_debt: 1`
* *Architecture:* `api: 47`, `concurrency: 2`, `import: 36`
* *Defense:* `safety: 5`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.129
  * `Choke Point (Betweenness):` 0.007246 | `Ripple Effect (Closeness):` 0.057329
  * `Imports (Out-Degree: 25):` color, entity, math, easing-functions, action, action-queue, blink, call-method...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/spec/vitest/arcade-solver-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 478.58 | **LOC:** 369 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.5472%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 17`, `args: 12`, `func_start: 2`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `concurrency: 4`, `import: 3`
* *Defense:* `safety: 2`, `test: 31`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` physics-config, test-utils, @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/actor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 466.96 | **LOC:** 1130 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.1154%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 72.5)
    * *Intent:* // #endregion /** * * @param config */
  * `draggable` **(State Mutators)** (Impact: 10.7)
  * `contains` **(Many-Argument Workhorses)** (Impact: 9.1)
    * *Intent:* // #region Collision /** * Tests whether the x/y specified are contained in the actor * @param x X c...
  * `clone` **(I/O & Config Routines)** (Impact: 6.0)
  * `within` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* /** * Returns true if the two actor.collider's surfaces are less than or equal to the distance speci...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 134`, `args: 91`, `func_start: 86`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 46`
* *Architecture:* `api: 95`, `concurrency: 7`, `import: 33`
* *Defense:* `safety: 16`, `doc: 94`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.607
  * `Choke Point (Betweenness):` 0.018963 | `Ripple Effect (Closeness):` 0.092595
  * `Imports (Out-Degree: 27):` actions-component, body-component, collider-component, shape, collision-type, index, color, engine...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/engine/math/graph.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 451.88 | **LOC:** 775 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.4314%), Tech Debt (9.868%)
**Top Internal Functions/Classes:**
  * `aStar` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* * * This method calculates the shortest path from the specified start node to the * specified end no...
  * `dijkstra` **(Compute Cores)** (Impact: 28.2)
    * *Intent:* * Finds the shortest path between two nodes in the graph using Dijkstra's algorithm. * * This method...
  * `addEdge` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* /** * Adds a new edge between two nodes in the graph. If the edge already exists, it does not add a ...
  * `constructor` **(Generic / Templated Code)** (Impact: 16.6)
  * `isDataWithId` **(C Struct Operations)** (Impact: 16.5)
    * *Intent:* /** * Return true if obj implement DataWithId interface * @param obj value to test * @returns true i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 87`, `args: 55`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 79`, `planned_debt: 2`
* *Architecture:* `io: 13`, `api: 17`, `import: 2`
* *Defense:* `safety: 10`, `doc: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.8
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001807
  * `Imports (Out-Degree: 2):` random, vector
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/engine/graphics/graphics-component.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 446.54 | **LOC:** 581 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.8126%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 40.6)
  * `deserialize` **(Defensive Guards)** (Impact: 32.7)
    * *Intent:* /** * Custom deserialization * NOTE - This only restores the component's settings, it does NOT resto...
  * `add` **(Compute Cores)** (Impact: 29.2)
  * `use` **(Defensive Guards)** (Impact: 14.9)
    * *Intent:* /** * Use a graphic only, will set the default graphic. Returns the new {@apilink Graphic} * * Optio...
  * `recalculateBounds` **(Defensive Guards)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 73`, `args: 43`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 71`
* *Architecture:* `api: 45`, `import: 14`
* *Defense:* `safety: 25`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.953
  * `Choke Point (Betweenness):` 0.006679 | `Ripple Effect (Closeness):` 0.074195
  * `Imports (Out-Degree: 12):` index, color, entity-component-system, component, graphics-group, vector, watch-vector, log...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/spec/vitest/material-renderer-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 444.41 | **LOC:** 469 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.6519%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 43`, `args: 17`, `func_start: 6`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* `concurrency: 19`, `import: 2`
* *Defense:* `safety: 3`, `test: 34`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-utils, @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/director/director.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 440.74 | **LOC:** 632 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.607%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `goToScene` **(Defensive Guards)** (Impact: 48.6)
    * *Intent:* /** * Go to a specific scene, and optionally override loaders and transitions * @param destinationSc...
  * `configureStart` **(Defensive Guards)** (Impact: 29.8)
    * *Intent:* /** * Configures the start scene, and optionally the transition & loader for the director * * Typica...
  * `playTransition` **(Defensive Guards)** (Impact: 20.3)
    * *Intent:* /** * Plays a transition in the current scene and does book keeping for input. * @param transition *...
  * `getSceneName` **(Compute Cores)** (Impact: 19.7)
    * *Intent:* /** * Returns the name of the registered scene, null if none can be found * @param scene */
  * `remove` **(Compute Cores)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 85`, `args: 25`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 42`, `dead_code: 1`
* *Architecture:* `api: 19`, `concurrency: 20`, `import: 10`
* *Defense:* `safety: 31`, `doc: 39`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.592
  * `Choke Point (Betweenness):` 0.001241 | `Ripple Effect (Closeness):` 0.083578
  * `Imports (Out-Degree: 8):` engine, event-emitter, events, scene, log, default-loader, loader, transition
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/engine/entity-component-system/entity.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 432.44 | **LOC:** 709 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.8271%), Tech Debt (40.5925%)
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 21.8)
  * `removeComponent` **(Generic / Templated Code)** (Impact: 15.6)
    * *Intent:* /** * Removes a component from the entity, by default removals are deferred to the end of entity upd...
  * `addComponent` **(Type Conversions)** (Impact: 15.4)
    * *Intent:* /** * Adds a component to the entity * @param component Component or Entity to add copy of component...
  * `hasChild` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* /** * Check if a child entity exists on the parent entity * @param child entity to check for * @para...
  * `_getClassHierarchyRoot` **(Defensive Guards)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 125`, `args: 63`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 41`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 79`, `concurrency: 14`, `import: 13`
* *Defense:* `safety: 5`, `doc: 49`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.824
  * `Choke Point (Betweenness):` 0.01626 | `Ripple Effect (Closeness):` 0.108698
  * `Imports (Out-Degree: 9):` engine, event-emitter, events, lifecycle-events, scene, observable, util, component...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/image-renderer/image-renderer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 411.28 | **LOC:** 409 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `draw` **(Many-Argument Workhorses)** (Impact: 147.0)
  * `_transformFragmentSource` **(Compute Cores)** (Impact: 14.7)
  * `_addImageAsTexture` **(Compute Cores)** (Impact: 8.4)
  * `_getTextureIdForImage` **(Defensive Guards)** (Impact: 6.0)
  * `_bindTextures` **(State Mutators)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 42`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 119`
* *Architecture:* `api: 11`, `import: 17`
* *Defense:* `safety: 13`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.532
  * `Choke Point (Betweenness):` 0.000605 | `Ripple Effect (Closeness):` 0.053291
  * `Imports (Out-Degree: 14):` color, util, filtering, graphics-diagnostics, image-source, wrapping, excalibur-graphics-context, excalibur-graphics-context-webgl...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/spec/vitest/sound-spec.ts` -> **Girts Silis** (100.0% isolated ownership) | Magnitude: 1656.27
- `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` -> **keasy9** (100.0% isolated ownership) | Magnitude: 595.94
- `src/engine/actor.ts` -> **Justin Young** (100.0% isolated ownership) | Magnitude: 466.96
- `src/engine/math/graph.ts` -> **THEVENOUX Jean-Philippe** (100.0% isolated ownership) | Magnitude: 451.88
- `src/engine/graphics/graphics-component.ts` -> **Justin Young** (100.0% isolated ownership) | Magnitude: 446.54

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/engine/engine.ts` -> **Severity: 3.458** (Bridge: 0.0346 * Flux: 99.9882%)
- `src/engine/scene.ts` -> **Severity: 2.147** (Bridge: 0.0216 * Flux: 99.2333%)
- `src/engine/actor.ts` -> **Severity: 1.883** (Bridge: 0.019 * Flux: 99.2865%)
- `src/engine/util/log.ts` -> **Severity: 1.85** (Bridge: 0.0185 * Flux: 100.0%)
- `src/engine/entity-component-system/entity.ts` -> **Severity: 1.626** (Bridge: 0.0163 * Flux: 99.9826%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/engine/math/vector.ts` -> **Severity: 13.782** (Embedded: 0.1806 * Error Risk: 76.329%)
- `src/engine/util/log.ts` -> **Severity: 12.221** (Embedded: 0.1258 * Error Risk: 97.1263%)
- `src/engine/event-emitter.ts` -> **Severity: 10.904** (Embedded: 0.1123 * Error Risk: 97.0892%)
- `src/engine/color.ts` -> **Severity: 10.493** (Embedded: 0.1326 * Error Risk: 79.1167%)
- `src/engine/util/util.ts` -> **Severity: 9.843** (Embedded: 0.1106 * Error Risk: 89.0097%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/engine/interfaces/clonable.ts` -> **Severity: 1911.4** (Blast Radius: 19.114 * Doc Risk: 100.0%)
- `src/engine/entity-component-system/entity.ts` -> **Severity: 766.92** (Blast Radius: 24.824 * Doc Risk: 30.8943%)
- `src/engine/collision/physics-config.ts` -> **Severity: 503.5** (Blast Radius: 5.035 * Doc Risk: 100.0%)
- `src/engine/event-emitter.ts` -> **Severity: 502.46** (Blast Radius: 8.479 * Doc Risk: 59.2593%)
- `src/engine/util/future.ts` -> **Severity: 501.5** (Blast Radius: 5.015 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
