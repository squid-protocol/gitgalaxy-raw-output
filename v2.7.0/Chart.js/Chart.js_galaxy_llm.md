# ARCHITECTURAL_BRIEF: Chart.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/chartjs/Chart.js.git` |
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
| Total Artifacts | 1750 |
| Analyzed Artifacts (Scanned) | 894 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 856 |
| Total LOC | 68406 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 51.1% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5788 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1261 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9099 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 646 | 55596 | 72.3% |
| JSON | 146 | 6970 | 16.3% |
| TYPESCRIPT | 84 | 5716 | 9.4% |
| PLAINTEXT | 8 | 0 | 0.9% |
| SHELL | 4 | 80 | 0.4% |
| MARKDOWN | 3 | 0 | 0.3% |
| HTML | 2 | 41 | 0.2% |
| YAML | 1 | 3 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 883 | 98.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 1.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 856*

**Composition by Extension & Reason:**
- `.png`: 679x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 140x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.styl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.drawio`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 17244 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 75.7 | 4.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 47.8 | 64.6 | 64.6 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 89.8 | 6.5 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.2 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 29.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 96.3 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 25.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 43 | 16 | 0 | `src/helpers/helpers.dom.ts` |
| cleanup | 43 | 15 | 0 | `test/specs/core.controller.tests.js` |
| guards | 885 | 125 | 2 | `src/core/core.scale.js` |
| danger | 169 | 55 | 0 | `scripts/deploy-docs.sh` |
| concurrency | 253 | 39 | 0 | `test/specs/plugin.tooltip.tests.js` |
| connectivity | 1434 | 626 | 1 | `src/types/index.d.ts` |
| io | 13 | 4 | 0 | `test/types/autogen.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 2 | 0 | `test/BasicChartWebWorker.js` |
| time | 32 | 14 | 0 | `test/specs/core.animations.tests.js` |
| serialization | 9 | 6 | 0 | `src/helpers/helpers.segment.js` |
| regex | 19 | 14 | 0 | `karma.conf.cjs` |
| events | 102 | 29 | 0 | `test/specs/plugin.tooltip.tests.js` |
| tests | 4075 | 58 | 0 | `test/specs/core.controller.tests.js` |
| docs | 1092 | 72 | 0 | `src/types/index.d.ts` |
| debt | 130 | 41 | 0 | `src/types/index.d.ts` |
| mutation | 9316 | 711 | 16 | `src/core/core.scale.js` |
| dead_code | 354 | 138 | 1 | `src/types/index.d.ts` |
| credential | 2 | 2 | 0 | `test/specs/helpers.color.tests.js` |
| threat | 157 | 42 | 0 | `test/specs/helpers.config.tests.js` |
| ml_ai | 124 | 10 | 0 | `src/helpers/helpers.canvas.ts` |
| ui | 22 | 9 | 0 | `test/specs/platform.dom.tests.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/types/autogen.js` (Hits: 8)
- `scripts/sample-redirect-template.html` (Hits: 3)
- `rollup.config.js` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.controller.js** (`src/core/core.controller.js`) — 13 inbound connections
2. **core.scale.js** (`src/core/core.scale.js`) — 11 inbound connections
3. **core.datasetController.js** (`src/core/core.datasetController.js`) — 10 inbound connections
4. **core.defaults.js** (`src/core/core.defaults.js`) — 9 inbound connections
5. **basic.js** (`test/fixtures/plugin.subtitle/basic.js`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.umd.ts** (`src/index.umd.ts`) — 18 outbound dependencies
2. **index.ts** (`src/helpers/index.ts`) — 16 outbound dependencies
3. **index.ts** (`src/core/index.ts`) — 14 outbound dependencies
4. **core.controller.js** (`src/core/core.controller.js`) — 13 outbound dependencies
5. **index.d.ts** (`src/types/index.d.ts`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `drawPointLegend` (@ `src/helpers/helpers.canvas.ts`) -> Impact: **100.2** | LOC: 142
  * *Intent:* // eslint-disable-next-line complexity
- `_computeLabelItems` (@ `src/core/core.scale.js`) -> Impact: **96.8** | LOC: 183
  * *Intent:* /** * @private */
- `generateTicks` (@ `src/scales/scale.linearbase.js`) -> Impact: **75.3** | LOC: 121
  * *Intent:* * * 2. If generationOptions.min, generationOptions.max, and generationOptions.count is defined * spacing = (max - min) / count * Ticks are generated a...
- `_longestText` (@ `src/helpers/helpers.canvas.ts`) -> Impact: **49.6** | LOC: 52
  * *Intent:* /** * @private */ // eslint-disable-next-line complexity
- `updateElements` (@ `src/controllers/controller.line.js`) -> Impact: **47.0** | LOC: 45
- `drawBorder` (@ `src/elements/element.arc.ts`) -> Impact: **44.1** | LOC: 50
- `_computeGridLineItems` (@ `src/core/core.scale.js`) -> Impact: **43.3** | LOC: 130
  * *Intent:* /** * @private */
- `updateElements` (@ `src/controllers/controller.scatter.js`) -> Impact: **42.3** | LOC: 41
- `_getYAxisLabelAlignment` (@ `src/core/core.scale.js`) -> Impact: **38.7** | LOC: 67
- `_calculatePadding` (@ `src/core/core.scale.js`) -> Impact: **38.2** | LOC: 49

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/core` | 21 | 4961.6 | 30.54% | 1.11% |
| `src/helpers` | 18 | 2854.55 | 29.33% | 1.83% |
| `test/specs` | 54 | 2560.98 | 3.3% | 0.0% |
| `src/plugins` | 7 | 1873.46 | 39.25% | 1.28% |
| `src/scales` | 8 | 1571.72 | 35.71% | 0.0% |
| `src/controllers` | 9 | 1395.18 | 29.61% | 0.0% |
| `src/elements` | 5 | 813.56 | 31.85% | 0.0% |
| `src/plugins/plugin.filler` | 8 | 621.94 | 40.24% | 6.25% |
| `src/platform` | 4 | 261.46 | 10.77% | 0.0% |
| `test/types` | 16 | 252.96 | 2.56% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/types/animation.d.ts` -> **100.0%** Exposure
- `src/types/index.d.ts` -> **99.9968%** Exposure
- `src/types/layout.d.ts` -> **99.9665%** Exposure
- `karma.conf.cjs` -> **81.6962%** Exposure
- `src/plugins/plugin.filler/simpleArc.js` -> **50.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/controllers/controller.bar.js` -> **100.0%** Exposure
- `src/controllers/controller.line.js` -> **100.0%** Exposure
- `src/core/core.animation.js` -> **100.0%** Exposure
- `src/core/core.animator.js` -> **100.0%** Exposure
- `src/core/core.layouts.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/types/index.d.ts` -> **157** Orphaned Functions | **22** Duplicates
- `src/types/animation.d.ts` -> **11** Orphaned Functions | **0** Duplicates
- `test/specs/plugin.tooltip.tests.js` -> **3** Orphaned Functions | **6** Duplicates
- `test/specs/scale.radialLinear.tests.js` -> **0** Orphaned Functions | **8** Duplicates
- `test/specs/core.plugin.tests.js` -> **3** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `43` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/core/core.animation.js` (JAVASCRIPT) -> Cumulative Risk: **694.78**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 140.54 | **LOC:** 120 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.0024%), Documentation (94.1176%)
- **Heaviest Functions:** `color` (Impact: 12.3), `constructor` (Impact: 12.1), `tick` (Impact: 11.3)

### 2. `src/core/core.animations.js` (JAVASCRIPT) -> Cumulative Risk: **616.71**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 118.5 | **LOC:** 163 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9975%), Concurrency (99.025%), Safety Score (82.6353%)
- **Heaviest Functions:** `_createAnimations` (Impact: 21.2), `configure` (Impact: 12.6), `resolveTargetOptions` (Impact: 7.7)

### 3. `src/helpers/helpers.dom.ts` (TYPESCRIPT) -> Cumulative Risk: **599.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 249.7 | **LOC:** 287 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (96.27%), Safety Score (92.411%)
- **Heaviest Functions:** `getMaximumSize` (Impact: 35.4), `retinaScale` (Impact: 21.8), `getContainerSize` (Impact: 17.3)

### 4. `src/core/core.scale.js` (JAVASCRIPT) -> Cumulative Risk: **585.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1429.02 | **LOC:** 1713 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.2083%), Verification (80.0%)
- **Heaviest Functions:** `_computeLabelItems` (Impact: 96.8), `_computeGridLineItems` (Impact: 43.3), `_getYAxisLabelAlignment` (Impact: 38.7)

### 5. `src/plugins/plugin.decimation.js` (JAVASCRIPT) -> Cumulative Risk: **579.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 225.22 | **LOC:** 288 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.3646%)
- **Heaviest Functions:** `minMaxDecimation` (Impact: 37.2), `beforeElementsUpdate` (Impact: 24.6), `lttbDecimation` (Impact: 21.0)

### 6. `src/helpers/helpers.extras.ts` (TYPESCRIPT) -> Cumulative Risk: **566.28**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 119.3 | **LOC:** 164 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (89.5496%), Safety Score (89.0454%)
- **Heaviest Functions:** `_getStartAndCountOfVisiblePoints` (Impact: 24.4), `_textX` (Impact: 9.4), `_scaleRangesChanged` (Impact: 8.1)

### 7. `src/scales/scale.category.js` (JAVASCRIPT) -> Cumulative Risk: **564.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 137.08 | **LOC:** 159 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (92.0%), Safety Score (82.7958%)
- **Heaviest Functions:** `addIfString` (Impact: 9.4), `parse` (Impact: 7.4), `findOrAddLabel` (Impact: 7.1)

### 8. `src/plugins/plugin.filler/filler.drawing.js` (JAVASCRIPT) -> Cumulative Risk: **551.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 155.06 | **LOC:** 188 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (86.8486%)
- **Heaviest Functions:** `fill` (Impact: 17.5), `clipBounds` (Impact: 17.3), `clipVertical` (Impact: 13.4)

### 9. `src/plugins/plugin.legend.js` (JAVASCRIPT) -> Cumulative Risk: **549.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 502.6 | **LOC:** 721 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (90.6183%), Verification (80.0%)
- **Heaviest Functions:** `_draw` (Impact: 32.8), `drawLegendBox` (Impact: 25.1), `handleEvent` (Impact: 15.4)

### 10. `src/scales/scale.linearbase.js` (JAVASCRIPT) -> Cumulative Risk: **544.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 306.38 | **LOC:** 314 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.4341%), Verification (80.0%)
- **Heaviest Functions:** `generateTicks` (Impact: 75.3), `setMax` (Impact: 16.8), `handleTickRangeOptions` (Impact: 13.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/core/core.scale.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1429.02 | **LOC:** 1713 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.2407%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_computeLabelItems` (Impact: 96.8)
    * *Intent:* /** * @private */
  * `_computeGridLineItems` (Impact: 43.3)
    * *Intent:* /** * @private */
  * `_getYAxisLabelAlignment` (Impact: 38.7)
  * `_calculatePadding` (Impact: 38.2)
  * `titleArgs` (Impact: 28.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 220 instances
* *State Mutation (weighted view):* 748
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 131`, `args: 89`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `state_mutation: 308`, `dead_code: 1`
* *Architecture:* `api: 21`, `import: 7`
* *Defense:* `safety: 80`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.387
  * `Choke Point (Betweenness):` 0.000493 | `Ripple Effect (Closeness):` 0.020915
  * `Imports (Out-Degree: 1):` helpers.canvas.js, helpers.core.js, helpers.extras.js, helpers.math.js, helpers.options.js, types.js, index.js, core.element.js...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/plugins/plugin.tooltip.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 927.58 | **LOC:** 1351 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.9105%), Tech Debt (8.9379%)
**Top Internal Functions/Classes:**
  * `_drawColorBox` (Impact: 28.5)
    * *Intent:* /** * @private */
  * `getCaretPosition` (Impact: 24.8)
  * `getBackgroundPoint` (Impact: 21.4)
    * *Intent:* /** * Helper to get the location a tooltip needs to be placed at given the initial position (via the...
  * `drawBackground` (Impact: 19.9)
  * `handleEvent` (Impact: 19.7)
    * *Intent:* /** * Handle an event * @param {ChartEvent} e - The event to handle * @param {boolean} [replay] - Th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 113`, `args: 69`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `state_mutation: 193`, `planned_debt: 2`
* *Architecture:* `api: 12`, `import: 8`
* *Defense:* `safety: 50`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.843
  * `Choke Point (Betweenness):` 0.000121 | `Ripple Effect (Closeness):` 0.012781
  * `Imports (Out-Degree: 3):` core.animations.js, core.element.js, core.interaction.js, helpers.canvas.js, helpers.core.js, helpers.math.js, helpers.options.js, helpers.rtl.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/core/core.datasetController.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 826.26 | **LOC:** 1078 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2587%), Tech Debt (9.3842%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 29.7)
    * *Intent:* /** * @param {number} start * @param {number} count */
  * `applyStack` (Impact: 26.1)
  * `getMinMax` (Impact: 19.3)
    * *Intent:* /** * @protected */
  * `clearStacks` (Impact: 18.3)
  * `getLastIndexInStack` (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 93`, `args: 80`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 24`, `import: 5`
* *Defense:* `safety: 38`, `doc: 42`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.385
  * `Choke Point (Betweenness):` 0.000504 | `Ripple Effect (Closeness):` 0.01479
  * `Imports (Out-Degree: 4):` helpers.collection.js, helpers.core.js, index.js, core.animations.js, core.controller.js, core.defaults.js, core.scale.js
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/core/core.controller.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 727.8 | **LOC:** 1270 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.2719%), Tech Debt (13.8538%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 21.0)
    * *Intent:* // eslint-disable-next-line max-statements
  * `update` (Impact: 15.9)
  * `buildOrUpdateScales` (Impact: 15.2)
    * *Intent:* /** * Builds a map of scale ID to scale object for future lookup. */
  * `_resize` (Impact: 13.4)
  * `updateHoverStyle` (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 136`, `args: 114`, `func_start: 83`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 114`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 12`
* *Defense:* `safety: 43`, `doc: 37`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.828
  * `Choke Point (Betweenness):` 0.0012 | `Ripple Effect (Closeness):` 0.023265
  * `Imports (Out-Degree: 8):` package.json, helpers.core.js, helpers.extras.js, index.js, index.js, index.js, core.animator.js, core.config.js...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/controllers/controller.bar.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 589.06 | **LOC:** 683 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8053%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 37.4)
  * `_getStacks` (Impact: 26.5)
    * *Intent:* /** * Returns the stacks based on groups and bar visibility. * @param {number} [last] - The dataset ...
  * `setBorderSkipped` (Impact: 26.1)
  * `_calculateBarValuePixels` (Impact: 26.1)
    * *Intent:* /** * Note: pixel values are not clamped to the scale area. * @private */
  * `skipNull` (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 68`, `args: 40`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`, `dead_code: 1`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 44`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.035
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002016
  * `Imports (Out-Degree: 1):` core.datasetController.js, index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.canvas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 507.74 | **LOC:** 528 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.5501%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawPointLegend` (Impact: 100.2)
    * *Intent:* // eslint-disable-next-line complexity
  * `_longestText` (Impact: 49.6)
    * *Intent:* /** * @private */ // eslint-disable-next-line complexity
  * `renderText` (Impact: 23.3)
    * *Intent:* /** * Render text onto the canvas */
  * `_steppedLineTo` (Impact: 20.6)
    * *Intent:* /** * @private */
  * `_isPointInArea` (Impact: 16.5)
    * *Intent:* /** * Returns true if the point is inside the rectangle * @param point - The point to test * @param ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 49`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `dead_code: 2`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.916
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` geometric.js, index.js, helpers.core.js, helpers.math.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.legend.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 502.6 | **LOC:** 721 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.3812%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_draw` (Impact: 32.8)
    * *Intent:* /** * @private */
  * `drawLegendBox` (Impact: 25.1)
    * *Intent:* // current position
  * `handleEvent` (Impact: 15.4)
    * *Intent:* /** * Handle an event * @param {ChartEvent} e - The event to handle */
  * `isListened` (Impact: 14.3)
  * `_getLegendItemAt` (Impact: 11.4)
    * *Intent:* /** * @private */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 73`, `args: 44`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 120`, `dead_code: 1`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 23`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.075
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.002016
  * `Imports (Out-Degree: 2):` core.defaults.js, core.element.js, core.layouts.js, helpers.canvas.js, helpers.extras.js, helpers.options.js, index.js, index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/scales/scale.radialLinear.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 401.8 | **LOC:** 685 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4862%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawRadiusLine` (Impact: 18.2)
  * `updateLimits` (Impact: 18.1)
  * `determineLimits` (Impact: 15.6)
  * `drawGrid` (Impact: 13.7)
    * *Intent:* /** * @protected */
  * `yForAngle` (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 61`, `args: 42`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`, `dead_code: 1`
* *Architecture:* `api: 15`, `import: 7`
* *Defense:* `safety: 14`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.075
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.002016
  * `Imports (Out-Degree: 3):` core.defaults.js, core.ticks.js, helpers.canvas.js, helpers.core.js, helpers.math.js, helpers.options.js, scale.linearbase.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/scales/scale.time.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 400.12 | **LOC:** 676 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.8061%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_tickFormatFunction` (Impact: 21.0)
    * *Intent:* /** * Function to format an individual tick mark * @param {number} time * @param {number} index * @p...
  * `parse` (Impact: 18.9)
    * *Intent:* /** * @param {TimeScale} scale * @param {*} input * @return {number} */
  * `determineDataLimits` (Impact: 15.9)
  * `_generate` (Impact: 14.0)
    * *Intent:* /** * Generates a maximum of `capacity` timestamps between min and max, rounded to the * `minor` uni...
  * `determineUnitForFormatting` (Impact: 12.7)
    * *Intent:* /** * Figures out what unit to format a set of ticks with * @param {TimeScale} scale * @param {numbe...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 63`, `args: 33`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`, `dead_code: 1`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 23`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.989
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.002986
  * `Imports (Out-Degree: 1):` core.adapters.js, core.scale.js, helpers.collection.js, helpers.core.js, helpers.math.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.segment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 349.82 | **LOC:** 365 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.6729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_boundSegment` (Impact: 32.6)
    * *Intent:* /** * Returns the sub-segment(s) of a line segment that fall in the given bounds * @param {object} s...
  * `doSplitByStyles` (Impact: 27.4)
    * *Intent:* /** * @param {LineElement} line * @param {Segment[]} segments * @param {PointElement[]} points * @pa...
  * `findStartAndEnd` (Impact: 24.0)
    * *Intent:* /** * Find start and end index of a line. */
  * `solidSegments` (Impact: 21.7)
    * *Intent:* /** * Compute solid segments from Points, when spanGaps === false * @param {PointElement[]} points -...
  * `addStyle` (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 53`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 46`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 16`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.413
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.005375
  * `Imports (Out-Degree: 1):` element.line.js, element.point.js, helpers.color.js, helpers.math.js, helpers.options.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.core.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 347.88 | **LOC:** 417 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.9685%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `each` (Impact: 25.9)
  * `merge` (Impact: 19.3)
  * `_elementsEqual` (Impact: 13.0)
    * *Intent:* /** * Returns true if the `a0` and `a1` arrays have the same content, else returns false. * @param a...
  * `_mergerIf` (Impact: 12.7)
    * *Intent:* /** * Merges source[key] in target[key] only if target[key] is undefined. * @private */
  * `toDimension` (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 123`, `args: 51`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 22`
* *Architecture:* `api: 45`, `import: 2`
* *Defense:* `safety: 5`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.916
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` basic.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.layouts.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 327.36 | **LOC:** 456 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.2666%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `placeBoxes` (Impact: 33.4)
  * `fitBoxes` (Impact: 21.6)
  * `update` (Impact: 21.2)
    * *Intent:* /** * Fits boxes of the given chart into the given size by having each box measure itself * then run...
  * `updateDims` (Impact: 17.3)
  * `setLayoutDims` (Impact: 16.5)
    * *Intent:* /** * store dimensions used instead of available chartArea in fitBoxes **/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 32`, `args: 31`, `func_start: 22`
* *Risk/State:* `state_mutation: 61`, `dead_code: 2`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 10`, `doc: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.887
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.017255
  * `Imports (Out-Degree: 1):` helpers.core.js, helpers.options.js, core.controller.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/elements/element.line.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 323.42 | **LOC:** 446 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2031%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fastPathSegment` (Impact: 29.9)
    * *Intent:* * Create path from points, grouping by truncated x-coordinate * Points need to be in order by x-coor...
  * `pathSegment` (Impact: 23.9)
    * *Intent:* * Create path from points, grouping by truncated x-coordinate * Points need to be in order by x-coor...
  * `draw` (Impact: 14.3)
    * *Intent:* /** * Draw * @param {CanvasRenderingContext2D} ctx * @param {object} chartArea * @param {number} [st...
  * `pathVars` (Impact: 12.8)
  * `drawX` (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 43`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 12`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.952
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.007679
  * `Imports (Out-Degree: 1):` core.element.js, helpers.canvas.js, helpers.curve.js, helpers.interpolation.js, helpers.segment.js, index.js, element.point.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/core/core.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 312.0 | **LOC:** 419 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8228%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mergeScaleConfig` (Impact: 26.4)
  * `needContext` (Impact: 16.3)
  * `getOptionScopes` (Impact: 13.5)
    * *Intent:* /** * Resolves the objects from options and defaults for option value resolution. * @param {object} ...
  * `determineAxis` (Impact: 12.8)
  * `getIndexAxis` (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 67`, `args: 54`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `safety: 16`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.017206
  * `Imports (Out-Degree: 1):` helpers.config.js, helpers.core.js, core.defaults.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.config.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 308.98 | **LOC:** 457 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.5335%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addScopes` (Impact: 25.7)
  * `_resolveArray` (Impact: 16.8)
  * `_attachContext` (Impact: 15.1)
    * *Intent:* /** * Returns an Proxy for resolving option values with context. * @param proxy - The Proxy returned...
  * `_resolveWithContext` (Impact: 15.1)
  * `createSubResolver` (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 85`, `args: 44`, `func_start: 38`
* *Risk/State:* `state_mutation: 27`, `dead_code: 1`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.916
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` basic.js, index.js, helpers.config.types.js, helpers.core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.linearbase.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 306.38 | **LOC:** 314 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.7619%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generateTicks` (Impact: 75.3)
    * *Intent:* * * 2. If generationOptions.min, generationOptions.max, and generationOptions.count is defined * spa...
  * `setMax` (Impact: 16.8)
  * `handleTickRangeOptions` (Impact: 13.6)
  * `parse` (Impact: 9.2)
  * `buildTicks` (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 32`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `dead_code: 1`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 11`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003665
  * `Imports (Out-Degree: 1):` core.scale.js, helpers.core.js, helpers.intl.js, helpers.math.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/core/core.interaction.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 260.92 | **LOC:** 388 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.0676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `binarySearch` (Impact: 35.7)
    * *Intent:* * @typedef { import('../types/index.js').ChartEvent } ChartEvent * @typedef {{axis?: string, interse...
  * `getNearestCartesianItems` (Impact: 25.3)
    * *Intent:* /** * Helper function to get the items nearest to the event position for a cartesian chart * @param ...
  * `evaluationFunc` (Impact: 19.1)
  * `getAxisItems` (Impact: 18.1)
    * *Intent:* /** * Helper function to get the items matching along the given X or Y axis * @param {Chart} chart -...
  * `index` (Impact: 17.0)
    * *Intent:* /** * Returns items at the same index. If the options.intersect parameter is true, we only return it...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 40`, `args: 22`, `func_start: 17`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 9`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.192
  * `Choke Point (Betweenness):` 8e-05 | `Ripple Effect (Closeness):` 0.016698
  * `Imports (Out-Degree: 1):` helpers.collection.js, helpers.dom.js, helpers.math.js, index.js, index.js, core.controller.js, core.element.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/controllers/controller.doughnut.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 253.82 | **LOC:** 400 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.1469%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 22.1)
  * `getMaxBorderWidth` (Impact: 14.2)
  * `_circumference` (Impact: 10.8)
    * *Intent:* /** * @private */
  * `parse` (Impact: 9.7)
    * *Intent:* /** * Override data parsing, since we are not using scales */
  * `getRatioAndOffset` (Impact: 9.3)
    * *Intent:* /** * @typedef { import('../core/core.controller.js').default } Chart */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 54`, `args: 27`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 8`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.915
  * `Choke Point (Betweenness):` 0.000258 | `Ripple Effect (Closeness):` 0.002986
  * `Imports (Out-Degree: 2):` core.controller.js, core.datasetController.js, helpers.core.js, helpers.intl.js, helpers.math.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.dom.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 249.7 | **LOC:** 287 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.7109%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getMaximumSize` (Impact: 35.4)
    * *Intent:* // eslint-disable-next-line complexity
  * `retinaScale` (Impact: 21.8)
    * *Intent:* /** * @param chart * @param forceRatio * @param forceStyle * @returns True if the canvas context siz...
  * `getContainerSize` (Impact: 17.3)
  * `getPositionedStyle` (Impact: 10.6)
  * `getRelativePosition` (Impact: 10.0)
    * *Intent:* /** * Gets an event's x, y coordinates, relative to the chart area * @param event * @param chart * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 34`, `args: 15`, `func_start: 14`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 2`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.916
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core.controller.js, types.js, index.js, helpers.math.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/specs/plugin.tooltip.tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 249.4 | **LOC:** 1952 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.3301%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getContext` (Impact: 18.5)
  * `testSlice` (Impact: 8.4)
  * `recursive` (Impact: 6.7)
  * `makeView` (Impact: 5.0)
  * `setContext` (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 108
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 183`, `args: 92`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10`, `dead_code: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 63`
* *Defense:* `safety: 7`, `test: 166`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.916
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/helpers/helpers.curve.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 242.38 | **LOC:** 224 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.4665%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_updateBezierControlPoints` (Impact: 21.5)
    * *Intent:* /** * @private */
  * `splineCurveMonotone` (Impact: 15.6)
    * *Intent:* /** * This function calculates Bézier control points in a similar way than |splineCurve|, * but pres...
  * `monotoneAdjust` (Impact: 13.4)
    * *Intent:* /** * Adjust tangents to ensure monotonic properties */
  * `splineCurve` (Impact: 13.2)
  * `monotoneCompute` (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 21`, `args: 10`, `func_start: 9`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.916
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` geometric.js, index.js, helpers.canvas.js, helpers.math.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/elements/element.arc.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 237.86 | **LOC:** 422 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8833%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawBorder` (Impact: 44.1)
  * `pathArc` (Impact: 36.8)
    * *Intent:* /** * Path the arc, respecting border radius by separating into left and right halves. * * Start End...
  * `draw` (Impact: 14.1)
  * `clipSelf` (Impact: 13.6)
  * `drawArc` (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 24`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.916
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.element.js, helpers.math.js, helpers.options.js, index.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/specs/core.controller.tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 234.88 | **LOC:** 2340 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6803%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `color` (Impact: 7.3)
  * `iterateOptions` (Impact: 2.3)
  * `onResize` (Impact: 2.0)
  * `beforeDatasetDraw` (Impact: 1.9)
  * `afterDatasetDraw` (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 183`, `args: 166`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 113`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 5`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 22`
* *Defense:* `safety: 6`, `test: 365`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.916
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.decimation.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 225.22 | **LOC:** 288 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.0013%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `minMaxDecimation` (Impact: 37.2)
  * `beforeElementsUpdate` (Impact: 24.6)
  * `lttbDecimation` (Impact: 21.0)
  * `getStartAndCountOfVisiblePointsSimplified` (Impact: 7.9)
  * `cleanDecimatedDataset` (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 34`, `args: 11`, `func_start: 9`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 9`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002016
  * `Imports (Out-Degree: 0):` index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/platform/platform.dom.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 204.98 | **LOC:** 390 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.7342%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initCanvas` (Impact: 19.9)
    * *Intent:* /** * Initializes the canvas style and render size without modifying the canvas display size, * sinc...
  * `createResizeObserver` (Impact: 13.9)
  * `createAttachObserver` (Impact: 10.8)
  * `createDetachObserver` (Impact: 10.8)
  * `acquireContext` (Impact: 9.8)
    * *Intent:* /** * @param {HTMLCanvasElement} canvas * @param {number} [aspectRatio] * @return {CanvasRenderingCo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 39`, `args: 29`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`, `dead_code: 3`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 15`, `doc: 11`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012398
  * `Imports (Out-Degree: 2):` core.controller.js, helpers.core.js, helpers.dom.js, helpers.extras.js, platform.base.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/types/index.d.ts` -> Churn: **92.56%** | Cog Load: 5.1017% | Debt: 99.9968%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/core/core.scale.js` -> **asmenezes** (100.0% isolated ownership) | Magnitude: 1429.02
- `src/helpers/helpers.dom.ts` -> **Josh Kelley** (100.0% isolated ownership) | Magnitude: 249.7
- `test/specs/core.scale.tests.js` -> **asmenezes** (100.0% isolated ownership) | Magnitude: 70.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/core/core.controller.js` -> **Severity: 0.12** (Bridge: 0.0012 * Flux: 99.997%)
- `src/core/core.datasetController.js` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 99.9999%)
- `src/core/core.scale.js` -> **Severity: 0.049** (Bridge: 0.0005 * Flux: 100.0%)
- `src/core/core.scale.autoskip.js` -> **Severity: 0.04** (Bridge: 0.0004 * Flux: 100.0%)
- `src/core/core.defaults.js` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 99.9694%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/core/core.scale.js` -> **Severity: 1.97** (Embedded: 0.0209 * Error Risk: 94.2083%)
- `src/core/core.controller.js` -> **Severity: 1.836** (Embedded: 0.0233 * Error Risk: 78.9296%)
- `src/core/core.defaults.js` -> **Severity: 1.72** (Embedded: 0.0221 * Error Risk: 77.8881%)
- `src/core/core.layouts.js` -> **Severity: 1.568** (Embedded: 0.0173 * Error Risk: 90.8543%)
- `src/core/core.animator.js` -> **Severity: 1.556** (Embedded: 0.0166 * Error Risk: 93.9135%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/core/core.controller.js` -> **Severity: 1393.407** (Blast Radius: 24.828 * Doc Risk: 56.1224%)
- `src/core/core.defaults.js` -> **Severity: 892.09** (Blast Radius: 15.218 * Doc Risk: 58.6207%)
- `src/elements/element.line.js` -> **Severity: 761.019** (Blast Radius: 13.952 * Doc Risk: 54.5455%)
- `src/helpers/helpers.segment.js` -> **Severity: 726.538** (Blast Radius: 13.413 * Doc Risk: 54.1667%)
- `src/core/core.scale.js` -> **Severity: 635.243** (Blast Radius: 15.387 * Doc Risk: 41.2844%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
