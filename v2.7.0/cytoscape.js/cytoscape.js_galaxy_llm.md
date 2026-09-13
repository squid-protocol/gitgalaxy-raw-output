# ARCHITECTURAL_BRIEF: cytoscape.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cytoscape/cytoscape.js.git` |
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
| Total Artifacts | 772 |
| Analyzed Artifacts (Scanned) | 626 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 146 |
| Total LOC | 54328 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 81.1% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4906 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4081 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6673 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 275 | 40820 | 43.9% |
| MARKDOWN | 209 | 331 | 33.4% |
| CSS | 80 | 7734 | 12.8% |
| HTML | 37 | 851 | 5.9% |
| JSON | 17 | 2517 | 2.7% |
| SHELL | 4 | 193 | 0.6% |
| XML | 2 | 0 | 0.3% |
| TYPESCRIPT | 1 | 1882 | 0.2% |
| PLAINTEXT | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 416 | 66.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 209 | 33.4% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 146*

**Composition by Extension & Reason:**
- `.png`: 56x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Massive Static Asset Blob: 12896 LOC), 2x Excluded (Massive Static Asset Blob: 5251 LOC)
- `.js`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 31815 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 32410 LOC exceeds safe regex boundaries)
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.cycss`: 1x Excluded (Unsupported Extension: '.cycss')
- `.otf`: 1x Excluded (Explicitly Denied Extension: '.otf')
- `.eot`: 1x Excluded (Explicitly Denied Extension: '.eot')
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 24.8 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 46.5 | 57.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.0 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 82.2 | 3.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 84.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 37.0 | 0.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 55.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 13 | 11 | 0 | `documentation/docmaker.mjs` |
| cleanup | 32 | 16 | 0 | `test/core-init.mjs` |
| guards | 1339 | 183 | 6 | `src/extensions/renderer/base/coord-ele-math/edge-control-points.mjs` |
| danger | 840 | 152 | 3 | `index.d.ts` |
| concurrency | 511 | 58 | 0 | `tests-examples/demo-todo-app.spec.js` |
| connectivity | 1121 | 250 | 4 | `documentation/template.html` |
| io | 313 | 73 | 1 | `documentation/template.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 117 | 9 | 0 | `src/collection/algorithms/k-clustering.mjs` |
| time | 52 | 17 | 0 | `src/extensions/renderer/base/load-listeners.mjs` |
| serialization | 24 | 9 | 0 | `.github/workflows/scripts/merge_unstable_to_master.sh` |
| regex | 82 | 25 | 0 | `documentation/docmaker.mjs` |
| events | 764 | 94 | 1 | `test/events.mjs` |
| tests | 4392 | 137 | 3 | `test/core-graph-manipulation.mjs` |
| docs | 1135 | 57 | 0 | `index.d.ts` |
| debt | 305 | 43 | 0 | `index.d.ts` |
| mutation | 15448 | 306 | 70 | `src/math.mjs` |
| dead_code | 467 | 136 | 1 | `index.d.ts` |
| credential | 1 | 1 | 0 | `documentation/demos/wine-cheese-map/index.html` |
| threat | 77 | 44 | 0 | `src/extension.mjs` |
| ml_ai | 33 | 9 | 0 | `src/extensions/renderer/canvas/webgl/fxaa-upscaler.mjs` |
| ui | 160 | 83 | 1 | `documentation/css/style.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `documentation/template.html` (Hits: 28)
- `documentation/demos/fcose-gene/index.html` (Hits: 22)
- `documentation/demos/colajs-graph/index.html` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.mjs** (`src/util/index.mjs`) — 85 inbound connections
2. **is.mjs** (`src/is.mjs`) — 64 inbound connections
3. **test.mjs** (`src/test.mjs`) — 33 inbound connections
4. **index.mjs** (`src/define/index.mjs`) — 8 inbound connections
5. **promise.mjs** (`src/promise.mjs`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.mjs** (`src/collection/index.mjs`) — 21 outbound dependencies
2. **index.mjs** (`src/collection/algorithms/index.mjs`) — 19 outbound dependencies
3. **index.mjs** (`src/core/index.mjs`) — 16 outbound dependencies
4. **index.mjs** (`src/extensions/renderer/canvas/index.mjs`) — 16 outbound dependencies
5. **index.html** (`documentation/demos/fcose-gene/index.html`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `load` (@ `src/extensions/renderer/base/load-listeners.mjs`) -> Impact: **525.7** | LOC: 1954
- `drawNode` (@ `src/extensions/renderer/canvas/drawing-nodes.mjs`) -> Impact: **375.0** | LOC: 569
- `parseImpl` (@ `src/style/parse.mjs`) -> Impact: **311.6** | LOC: 373
  * *Intent:* // parse a property; return null on invalid; return parsed property otherwise // fields : // - name : the name of the property // - value : the parsed...
- `drawText` (@ `src/extensions/renderer/canvas/drawing-label-text.mjs`) -> Impact: **192.4** | LOC: 223
- `getAllInBox` (@ `src/extensions/renderer/base/coord-ele-math/coords.mjs`) -> Impact: **185.0** | LOC: 256
  * *Intent:* // 'Give me everything from this box'
- `render` (@ `src/extensions/renderer/canvas/drawing-redraw.mjs`) -> Impact: **171.7** | LOC: 352
- `makeEvent` (@ `src/extensions/renderer/base/load-listeners.mjs`) -> Impact: **169.9** | LOC: 429
- `findNearestElements` (@ `src/extensions/renderer/base/coord-ele-math/coords.mjs`) -> Impact: **150.7** | LOC: 242
- `getElement` (@ `src/extensions/renderer/canvas/ele-texture-cache.mjs`) -> Impact: **136.4** | LOC: 181
- `boundingBoxImpl` (@ `src/collection/dimensions/bounds.mjs`) -> Impact: **134.8** | LOC: 306
  * *Intent:* // get the bounding box of the elements (in raw model position)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/extensions/renderer/canvas` | 15 | 4928.06 | 70.4% | 0.0% |
| `src/collection/algorithms` | 20 | 3591.36 | 69.2% | 1.52% |
| `src/extensions/renderer/base` | 6 | 3097.72 | 63.29% | 10.43% |
| `src` | 17 | 3000.48 | 55.61% | 0.84% |
| `src/extensions/renderer/base/coord-ele-math` | 10 | 2992.76 | 71.42% | 0.0% |
| `documentation` | 4 | 2835.25 | 25.38% | 3.09% |
| `src/collection` | 18 | 2752.54 | 49.2% | 0.0% |
| `src/style` | 9 | 2187.04 | 63.34% | 0.0% |
| `src/extensions/renderer/canvas/webgl` | 7 | 2055.58 | 47.6% | 22.17% |
| `src/extensions/layout` | 9 | 1668.74 | 52.71% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `index.d.ts` -> **100.0%** Exposure
- `benchmark/suite/index.js` -> **99.9877%** Exposure
- `documentation/demos/multiple-instances/code.js` -> **97.5465%** Exposure
- `src/selector/state.mjs` -> **83.3014%** Exposure
- `benchmark/a-star.js` -> **73.1059%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmark/graphs/random.js` -> **100.0%** Exposure
- `benchmark/suite/index.js` -> **100.0%** Exposure
- `documentation/docmaker.mjs` -> **100.0%** Exposure
- `src/animation.mjs` -> **100.0%** Exposure
- `src/collection/algorithms/a-star.mjs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `index.d.ts` -> **180** Orphaned Functions | **71** Duplicates
- `test/collection-algorithms.mjs` -> **1** Orphaned Functions | **29** Duplicates
- `test/events.mjs` -> **0** Orphaned Functions | **21** Duplicates
- `test/modules/webgl-atlas.mjs` -> **8** Orphaned Functions | **6** Duplicates
- `test/collection-astar.mjs` -> **1** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `240` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/style/apply.mjs` (JAVASCRIPT) -> Cumulative Risk: **704.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 804.0 | **LOC:** 850 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.5733%)
- **Heaviest Functions:** `applyParsedProperty` (Impact: 125.4), `updateStyleHints` (Impact: 46.9), `updateTransitions` (Impact: 44.4)

### 2. `src/collection/class.mjs` (JAVASCRIPT) -> Cumulative Risk: **691.29**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 129.0 | **LOC:** 143 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.9213%)
- **Heaviest Functions:** `toggleClass` (Impact: 28.2), `classes` (Impact: 19.8), `flashClass` (Impact: 7.7)

### 3. `src/extensions/renderer/base/load-listeners.mjs` (JAVASCRIPT) -> Cumulative Risk: **681.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2191.9 | **LOC:** 2203 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (96.9516%)
- **Heaviest Functions:** `load` (Impact: 525.7), `makeEvent` (Impact: 169.9), `mousemoveHandler` (Impact: 120.8)

### 4. `src/extensions/renderer/canvas/export-image.mjs` (JAVASCRIPT) -> Cumulative Risk: **680.54**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 153.7 | **LOC:** 173 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.1631%)
- **Heaviest Functions:** `bufferCanvasImage` (Impact: 26.1), `output` (Impact: 19.5), `getB64Uri` (Impact: 10.6)

### 5. `src/animation.mjs` (JAVASCRIPT) -> Cumulative Risk: **679.08**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 214.54 | **LOC:** 261 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.3253%)
- **Heaviest Functions:** `Animation` (Impact: 18.4), `promise` (Impact: 9.5), `progress` (Impact: 8.1)

### 6. `src/math.mjs` (JAVASCRIPT) -> Cumulative Risk: **675.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1474.62 | **LOC:** 1479 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `roundRectangleIntersectLine` (Impact: 73.2), `finiteLinesIntersect` (Impact: 53.9), `polygonIntersectLine` (Impact: 36.1)

### 7. `src/style/bypass.mjs` (JAVASCRIPT) -> Cumulative Risk: **666.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 181.0 | **LOC:** 174 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.8704%)
- **Heaviest Functions:** `applyBypass` (Impact: 58.2), `overrideBypass` (Impact: 25.7), `removeBypasses` (Impact: 13.7)

### 8. `src/util/index.mjs` (JAVASCRIPT) -> Cumulative Risk: **660.73**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 143.28 | **LOC:** 160 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `uuid` (Impact: 9.8), `copy` (Impact: 9.1), `removeFromArray` (Impact: 8.6)

### 9. `src/extensions/renderer/canvas/webgl/atlas.mjs` (JAVASCRIPT) -> Cumulative Risk: **659.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 408.18 | **LOC:** 647 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Documentation (93.8462%), Safety Score (87.7908%)
- **Heaviest Functions:** `draw` (Impact: 34.2), `getOrCreateAtlas` (Impact: 17.3), `gc` (Impact: 11.6)

### 10. `src/extensions/renderer/canvas/drawing-redraw.mjs` (JAVASCRIPT) -> Cumulative Risk: **644.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 745.74 | **LOC:** 722 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (95.9195%)
- **Heaviest Functions:** `render` (Impact: 171.7), `createGradientStyleFor` (Impact: 64.9), `drawSelectionRectangle` (Impact: 32.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `documentation/template.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2417.39 | **LOC:** 303 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.8753%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 100`, `args: 47`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 11`
* *Architecture:* `io: 28`, `api: 29`, `concurrency: 2`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` font-awesome.css, github.css, reset.css, style.css, js.cytoscape.org, classList.min.js, cytoscape-logo.png, cytoscape-logo.svg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/load-listeners.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2191.9 | **LOC:** 2203 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.9516%), Tech Debt (20.9223%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 525.7)
  * `makeEvent` (Impact: 169.9)
  * `mousemoveHandler` (Impact: 120.8)
  * `mouseupHandler` (Impact: 85.3)
  * `makeEvent` (Impact: 68.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 231 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 745
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 368`, `args: 88`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 283`, `dead_code: 10`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 10`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 48`, `test: 82`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.369
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002667
  * `Imports (Out-Degree: 2):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/math.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1474.62 | **LOC:** 1479 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3609%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `roundRectangleIntersectLine` (Impact: 73.2)
  * `finiteLinesIntersect` (Impact: 53.9)
    * *Intent:* // (x1,y1)=>(x2,y2) intersect with (x3,y3)=>(x4,y4)
  * `polygonIntersectLine` (Impact: 36.1)
    * *Intent:* // math.polygonIntersectLine( x, y, basePoints, centerX, centerY, width, height, padding ) // inters...
  * `intersectLineCircle` (Impact: 34.0)
    * *Intent:* // Returns intersections of increasing distance from line's start point
  * `median` (Impact: 33.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 619
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 466`, `args: 89`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 251`, `dead_code: 5`
* *Architecture:* `api: 73`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0016
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/collection/dimensions/bounds.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1235.52 | **LOC:** 1045 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.8841%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `boundingBoxImpl` (Impact: 134.8)
    * *Intent:* // get the bounding box of the elements (in raw model position)
  * `isDisplayed` (Impact: 109.3)
    * *Intent:* // must use `display` prop only, as reading `compound.width()` causes recursion // (other factors li...
  * `updateBoundsFromLabel` (Impact: 68.8)
  * `updateCompoundBounds` (Impact: 67.9)
  * `update` (Impact: 55.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 519
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 258`, `args: 33`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 201`, `dead_code: 2`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 36`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.407
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004126
  * `Imports (Out-Degree: 2):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/base/coord-ele-math/edge-control-points.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1001.16 | **LOC:** 1058 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.4501%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getKey` (Impact: 106.2)
  * `findTaxiPoints` (Impact: 95.3)
  * `findEdgeControlPoints` (Impact: 92.6)
  * `subDWH` (Impact: 51.3)
    * *Intent:* // take away the effective w/h from the magnitude of the delta value
  * `tryToCorrectInvalidPoints` (Impact: 34.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 207`, `args: 24`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 151`, `dead_code: 5`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 49`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002743
  * `Imports (Out-Degree: 4):` is.mjs, map.mjs, math.mjs, round.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/drawing-nodes.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 967.98 | **LOC:** 805 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.0756%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawNode` (Impact: 375.0)
  * `drawOutline` (Impact: 68.3)
  * `drawPie` (Impact: 42.1)
  * `drawStripe` (Impact: 35.3)
  * `drawBorder` (Impact: 22.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 300
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 171`, `args: 22`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 110`, `dead_code: 5`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002667
  * `Imports (Out-Degree: 3):` is.mjs, math.mjs, round.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/layout/cose.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 865.8 | **LOC:** 1341 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.7446%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createLayoutInfo` (Impact: 49.0)
    * *Intent:* /** * @brief : Creates an object which is contains all the data * used in the layout process * @arg ...
  * `findClippingPoint` (Impact: 42.1)
    * *Intent:* /** * @brief : Finds the point in which an edge (direction dX, dY) intersects * the rectangular boun...
  * `run` (Impact: 28.0)
    * *Intent:* /** * @brief : runs the layout */
  * `findLCA_aux` (Impact: 24.3)
    * *Intent:* /** * @brief : Auxiliary function used for LCA computation * * @arg node1 : node1's ID * @arg node2 ...
  * `nodeRepulsion` (Impact: 23.8)
    * *Intent:* /** * @brief : Compute the node repulsion forces between a pair of nodes */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 447
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 283`, `args: 40`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 181`, `dead_code: 13`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 30`, `doc: 22`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00256
  * `Imports (Out-Degree: 2):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 832.0 | **LOC:** 1154 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.7477%), Tech Debt (10.2784%)
**Top Internal Functions/Classes:**
  * `_createShaderProgram` (Impact: 116.5)
  * `drawNode` (Impact: 36.1)
    * *Intent:* /** * Draw a node using either a texture or a "simple shape". */
  * `drawTexture` (Impact: 33.4)
    * *Intent:* /** * Draws a texture using the texture atlas. */
  * `drawEdgeArrow` (Impact: 26.9)
    * *Intent:* /** * Only supports drawing triangles at the moment. */
  * `drawEdgeLine` (Impact: 23.6)
    * *Intent:* /** * Draw straight-line or bezier curve edges. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 73`, `args: 37`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 185`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 16`, `import: 6`
* *Defense:* `safety: 13`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002743
  * `Imports (Out-Degree: 4):` math.mjs, index.mjs, atlas.mjs, shader-sdf.mjs, webgl-util.mjs, gl-matrix
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/style/apply.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 804.0 | **LOC:** 850 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.4363%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applyParsedProperty` (Impact: 125.4)
    * *Intent:* // // now, this function flattens the property, and here's how: // // for parsedProp:{ bypass: true,...
  * `updateStyleHints` (Impact: 46.9)
  * `updateTransitions` (Impact: 44.4)
    * *Intent:* // diffProps : { name => { prev, next } }
  * `cleanNum` (Impact: 40.3)
  * `getPropertiesDiff` (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 96 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 237`, `args: 39`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 122`, `dead_code: 14`
* *Architecture:* `api: 5`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 25`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.309
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.0032
  * `Imports (Out-Degree: 3):` is.mjs, promise.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/drawing-redraw.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 745.74 | **LOC:** 722 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.9195%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 171.7)
  * `createGradientStyleFor` (Impact: 64.9)
  * `drawSelectionRectangle` (Impact: 32.3)
  * `setContextTransform` (Impact: 24.5)
  * `matchCanvasSize` (Impact: 14.5)
    * *Intent:* // Resize canvas
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 109 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 347
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 121`, `args: 19`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 129`, `dead_code: 7`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 26`, `test: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002667
  * `Imports (Out-Degree: 1):` math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/collection/index.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 741.38 | **LOC:** 839 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.3322%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `restore` (Impact: 103.0)
  * `remove` (Impact: 56.5)
  * `Collection` (Impact: 56.3)
    * *Intent:* // represents a set of nodes, edges, or both together
  * `json` (Impact: 45.4)
  * `toString` (Impact: 32.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 194`, `args: 38`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 119`, `dead_code: 5`
* *Architecture:* `api: 10`, `import: 21`
* *Defense:* `safety: 14`, `test: 23`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006667
  * `Imports (Out-Degree: 16):` is.mjs, map.mjs, set.mjs, index.mjs, index.mjs, animation.mjs, class.mjs, comparators.mjs...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/base/coord-ele-math/coords.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 611.54 | **LOC:** 581 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.1373%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAllInBox` (Impact: 185.0)
    * *Intent:* // 'Give me everything from this box'
  * `findNearestElements` (Impact: 150.7)
  * `checkEdge` (Impact: 34.9)
  * `addEle` (Impact: 27.6)
  * `checkLabel` (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 182`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 51`, `dead_code: 3`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 31`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002743
  * `Imports (Out-Degree: 1):` math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/core/viewport.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 545.36 | **LOC:** 610 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.8044%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getFitViewport` (Impact: 44.6)
  * `getZoomedViewport` (Impact: 31.5)
  * `viewport` (Impact: 29.5)
  * `zoomRange` (Impact: 23.6)
  * `panBy` (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 125`, `args: 32`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 79`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 24`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.245
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00288
  * `Imports (Out-Degree: 1):` is.mjs, math.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/layered-texture-cache.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 532.44 | **LOC:** 669 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.6485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLayers` (Impact: 91.6)
  * `drawEleInLayer` (Impact: 18.9)
  * `dequeue` (Impact: 18.8)
  * `updateElementsInLayers` (Impact: 16.9)
  * `validateLayersElesOrdering` (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 176`, `args: 29`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 81`, `dead_code: 14`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 14`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002667
  * `Imports (Out-Degree: 4):` heap.mjs, is.mjs, math.mjs, index.mjs, texture-cache-defs.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/collection/algorithms/k-clustering.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 527.36 | **LOC:** 469 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.3282%), Tech Debt (15.4694%)
**Top Internal Functions/Classes:**
  * `kMeans` (Impact: 25.4)
  * `kMedoids` (Impact: 23.4)
  * `fuzzyCMeans` (Impact: 19.2)
  * `updateCentroids` (Impact: 15.7)
  * `assign` (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 146`, `args: 20`, `func_start: 18`
* *Risk/State:* `state_mutation: 116`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 14`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.196
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.004126
  * `Imports (Out-Degree: 2):` index.mjs, clustering-distances.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/base/coord-ele-math/labels.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 477.94 | **LOC:** 566 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.9527%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLabelText` (Impact: 58.1)
  * `recalculateEdgeLabelProjections` (Impact: 56.8)
  * `calculateEndProjection` (Impact: 36.9)
  * `recalculateNodeLabelProjection` (Impact: 16.6)
  * `calculateLabelAngle` (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 185`, `args: 17`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 79`, `dead_code: 4`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 16`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.741
  * `Choke Point (Betweenness):` 0.000192 | `Ripple Effect (Closeness):` 0.003564
  * `Imports (Out-Degree: 2):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/style/parse.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 477.54 | **LOC:** 436 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.2837%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseImpl` (Impact: 311.6)
    * *Intent:* // parse a property; return null on invalid; return parsed property otherwise // fields : // - name ...
  * `parse` (Impact: 28.4)
    * *Intent:* // a caching layer for property parsing
  * `parseImplWarn` (Impact: 18.5)
  * `checkEnums` (Impact: 3.8)
    * *Intent:* // several types also allow enums
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 94`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 36`, `dead_code: 3`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests-examples/demo-todo-app.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 470.98 | **LOC:** 450 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.4459%), Tech Debt (64.6821%)
**Top Internal Functions/Classes:**
  * `createDefaultTodos` (Impact: 4.7)
  * `checkNumberOfTodosInLocalStorage` (Impact: 2.0)
    * *Intent:* /** * @param {import('@playwright/test').Page} page * @param {number} expected */
  * `checkNumberOfCompletedTodosInLocalStorage` (Impact: 2.0)
    * *Intent:* /** * @param {import('@playwright/test').Page} page * @param {number} expected */
  * `checkTodosInLocalStorage` (Impact: 2.0)
    * *Intent:* /** * @param {import('@playwright/test').Page} page * @param {string} title */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 47 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 426
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 207`, `args: 50`, `func_start: 4`
* *Risk/State:* `state_mutation: 14`, `planned_debt: 18`
* *Architecture:* `io: 3`, `concurrency: 191`, `import: 1`
* *Defense:* `safety: 2`, `doc: 3`, `test: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/ele-texture-cache.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 456.82 | **LOC:** 556 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.5922%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getElement` (Impact: 136.4)
  * `invalidateElement` (Impact: 10.4)
  * `shouldRedraw` (Impact: 9.7)
  * `dequeue` (Impact: 8.7)
  * `removeFromQueue` (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 129`, `args: 26`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 83`, `dead_code: 5`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0036
  * `Imports (Out-Degree: 4):` heap.mjs, math.mjs, index.mjs, ele-texture-cache-lookup.mjs, texture-cache-defs.mjs
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/drawing-label-text.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 456.18 | **LOC:** 403 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.2071%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawText` (Impact: 192.4)
  * `drawElementText` (Impact: 61.4)
  * `getTextAngle` (Impact: 13.0)
  * `getFontCache` (Impact: 6.7)
  * `eleTextBiggerThanMin` (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 98`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 54`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002667
  * `Imports (Out-Degree: 1):` math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/base/node-shapes.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 437.94 | **LOC:** 659 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.9558%), Tech Debt (41.6533%)
**Top Internal Functions/Classes:**
  * `checkPoint` (Impact: 48.5)
  * `checkPoint` (Impact: 27.1)
  * `checkPoint` (Impact: 23.6)
  * `generateBarrel` (Impact: 22.4)
  * `checkPoint` (Impact: 21.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 137`, `args: 37`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 46`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.mjs, round.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/drawing-edges.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 429.7 | **LOC:** 432 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2633%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawArrowShape` (Impact: 73.0)
  * `drawEdgePath` (Impact: 71.5)
  * `drawEdge` (Impact: 59.7)
  * `drawArrowhead` (Impact: 41.8)
  * `drawEdgeOverlayUnderlay` (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 96`, `args: 14`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 46`, `dead_code: 3`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002667
  * `Imports (Out-Degree: 2):` round.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/webgl/atlas.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 408.18 | **LOC:** 647 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.2691%), Tech Debt (42.5904%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 34.2)
  * `getOrCreateAtlas` (Impact: 17.3)
  * `gc` (Impact: 11.6)
  * `draw` (Impact: 10.9)
  * `moveToStartOfNextRow` (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 80`, `args: 59`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 91`, `dead_code: 5`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 11`, `doc: 5`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.396
  * `Choke Point (Betweenness):` 0.000208 | `Ripple Effect (Closeness):` 0.003531
  * `Imports (Out-Degree: 2):` index.mjs, webgl-util.mjs
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/collection/algorithms/affinity-propagation.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 402.44 | **LOC:** 330 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `affinityPropagation` (Impact: 58.3)
  * `getPreference` (Impact: 16.4)
  * `assign` (Impact: 15.7)
  * `assignClusters` (Impact: 13.3)
  * `setOptions` (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 104`, `args: 14`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 87`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 11`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.196
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.004126
  * `Imports (Out-Degree: 3):` is.mjs, math.mjs, index.mjs, clustering-distances.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/collection/algorithms/hierarchical-clustering.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 401.48 | **LOC:** 317 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.0389%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mergeClosest` (Impact: 71.1)
  * `getDist` (Impact: 51.5)
  * `buildClustersFromTree` (Impact: 34.2)
  * `getDist` (Impact: 29.6)
  * `hierarchicalClustering` (Impact: 23.7)
    * *Intent:* } /* eslint-enable */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 75`, `args: 14`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 19`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.196
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.004126
  * `Imports (Out-Degree: 2):` index.mjs, clustering-distances.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` -> **Mike Kucera** (100.0% isolated ownership) | Magnitude: 832.0
- `src/extensions/renderer/canvas/webgl/webgl-util.mjs` -> **Mike Kucera** (100.0% isolated ownership) | Magnitude: 249.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/util/index.mjs` -> **Severity: 0.205** (Bridge: 0.0021 * Flux: 100.0%)
- `src/extensions/renderer/canvas/webgl/atlas.mjs` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 99.9993%)
- `src/style/index.mjs` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)
- `src/extensions/renderer/base/coord-ele-math/labels.mjs` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 100.0%)
- `src/selector/index.mjs` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/util/index.mjs` -> **Severity: 12.422** (Embedded: 0.1384 * Error Risk: 89.7216%)
- `src/util/maps.mjs` -> **Severity: 7.438** (Embedded: 0.0767 * Error Risk: 96.9839%)
- `src/util/hash.mjs` -> **Severity: 6.948** (Embedded: 0.0767 * Error Risk: 90.5963%)
- `src/util/extend.mjs` -> **Severity: 6.679** (Embedded: 0.0778 * Error Risk: 85.8149%)
- `src/util/colors.mjs` -> **Severity: 6.556** (Embedded: 0.077 * Error Risk: 85.1023%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/util/index.mjs` -> **Severity: 5716.0** (Blast Radius: 57.16 * Doc Risk: 100.0%)
- `src/is.mjs` -> **Severity: 4470.9** (Blast Radius: 44.709 * Doc Risk: 100.0%)
- `src/util/memoize.mjs` -> **Severity: 853.4** (Blast Radius: 8.534 * Doc Risk: 100.0%)
- `src/util/colors.mjs` -> **Severity: 620.6** (Blast Radius: 6.206 * Doc Risk: 100.0%)
- `src/util/hash.mjs` -> **Severity: 599.4** (Blast Radius: 5.994 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
