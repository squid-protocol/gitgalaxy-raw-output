# ARCHITECTURAL_BRIEF: cytoscape.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/cytoscape.js` |
| **Timestamp** | `2026-08-03T20:03:02.895325+00:00` |
| **Scan Duration** | `1.41s` |
| **Git Branch** | `unstable` |
| **Git Commit** | `816e98077a6447f491efec81b22cab19e5a56f25` |
| **Git Remote** | `https://github.com/cytoscape/cytoscape.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 233 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 772 |
| Analyzed Artifacts (Scanned) | 544 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 228 |
| Total LOC | 35281 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 70.5% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.75 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 228 | 23829 | 41.9% |
| MARKDOWN | 197 | 331 | 36.2% |
| CSS | 69 | 7471 | 12.7% |
| HTML | 27 | 698 | 5.0% |
| JSON | 15 | 1380 | 2.8% |
| SHELL | 4 | 193 | 0.7% |
| XML | 2 | 0 | 0.4% |
| TYPESCRIPT | 1 | 1379 | 0.2% |
| PLAINTEXT | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.325`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 211 | 38.8% |
| file_cluster_13 | 68 | 12.5% |
| file_cluster_17 | 23 | 4.2% |
| file_cluster_11 | 21 | 3.9% |
| file_cluster_4 | 17 | 3.1% |
| file_cluster_0 | 5 | 0.9% |
| file_cluster_2 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 197 | 36.2% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 228*

**Composition by Extension & Reason:**
- `.png`: 56x Excluded (Explicitly Denied Extension: '.png')
- `.mjs`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 12896 LOC), 1x Excluded (Massive Static Asset Blob: 14960 LOC)
- `.js`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 31815 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 32410 LOC exceeds safe regex boundaries)
- `.md`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.cycss`: 1x Excluded (Unsupported Extension: '.cycss')
- `.otf`: 1x Excluded (Explicitly Denied Extension: '.otf')
- `.eot`: 1x Excluded (Explicitly Denied Extension: '.eot')
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 39.0 | 31.5 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 32.8 | 14.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.7 | 2.4 | 2.3 |
| API Exposure | 0.0 | 16.7 | 3.6 | 3.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 55.7 | 99.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 75.4 | 3.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 95.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.2 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 66.4 | 0.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 53.7 | 50.8 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 28.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `documentation/template.html` (Hits: 30)
- `documentation/demos/fcose-gene/index.html` (Hits: 23)
- `documentation/docmaker.mjs` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **png.md** (`documentation/md/core/png.md`) — 1 inbound connections
2. **collection-creation.js** (`benchmark/collection-creation.js`) — 1 inbound connections
3. **tokyo-railways.js** (`documentation/demos/tokyo-railways/tokyo-railways.js`) — 1 inbound connections
4. **test.mjs** (`src/test.mjs`) — 1 inbound connections
5. **.babelrc** (`.babelrc`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.mjs** (`src/collection/index.mjs`) — 21 outbound dependencies
2. **index.mjs** (`src/collection/algorithms/index.mjs`) — 19 outbound dependencies
3. **index.mjs** (`src/core/index.mjs`) — 16 outbound dependencies
4. **index.mjs** (`src/extensions/renderer/canvas/index.mjs`) — 16 outbound dependencies
5. **index.html** (`documentation/demos/fcose-gene/index.html`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `load` (@ `src/extensions/renderer/base/load-listeners.mjs`) -> Impact: **761.0** | LOC: 866
- `cytoscape` (@ `index.d.ts`) -> Impact: **747.0** | LOC: 301
  * *Intent:* // // Translation from Objects in help to Typescript interface. // http://js.cytoscape.org/#notation/functions // TypeScript Version: 2.3 /** * WARNIN...
- `median` (@ `src/math.mjs`) -> Impact: **653.3** | LOC: 1002
- `compileConfig` (@ `documentation/docmaker.mjs`) -> Impact: **388.1** | LOC: 159
- `data` (@ `src/define/data.mjs`) -> Impact: **386.6** | LOC: 132
  * *Intent:* // access data field
- `weight` (@ `src/collection/algorithms/bellman-ford.mjs`) -> Impact: **330.2** | LOC: 195
- `run` (@ `src/extensions/layout/cose.mjs`) -> Impact: **274.6** | LOC: 741
  * *Intent:* // Exclude any edge that has a source or target node that is not in the set of passed-in nodes
- `_createShaderProgram` (@ `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs`) -> Impact: **267.1** | LOC: 321
  * *Intent:* /** * @param { string } collectionName
- `boundingBoxImpl` (@ `src/collection/dimensions/bounds.mjs`) -> Impact: **261.3** | LOC: 306
- `filter` (@ `src/collection/filter.mjs`) -> Impact: **255.6** | LOC: 332

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `cytoscape` (@ `index.d.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* // // Translation from Objects in help to Typescript interface. // http://js.cytoscape.org/#notation/functions // TypeScript Version: 2.3 /** * WARNIN...
- `setTimeout` (@ `documentation/demos/radius-types/code.js`) -> **O(2^N) [Recursive]**
- `compileConfig` (@ `documentation/docmaker.mjs`) -> **O(2^N) [Recursive]**
- `weight` (@ `src/collection/algorithms/bellman-ford.mjs`) -> **O(2^N) [Recursive]**
- `data` (@ `src/define/data.mjs`) -> **O(2^N) [Recursive]**
  * *Intent:* // access data field
- `weight` (@ `src/collection/algorithms/closeness-centrality.mjs`) -> **O(2^N) [Recursive]**
- `weight` (@ `src/collection/algorithms/degree-centrality.mjs`) -> **O(2^N) [Recursive]**
- `weight` (@ `src/collection/algorithms/dijkstra.mjs`) -> **O(2^N) [Recursive]**
- `weight` (@ `src/collection/algorithms/floyd-warshall.mjs`) -> **O(2^N) [Recursive]**
- `move` (@ `src/collection/index.mjs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `median` (@ `src/math.mjs`) -> DB Complexity: **164**
- `run` (@ `src/extensions/layout/cose.mjs`) -> DB Complexity: **162**
  * *Intent:* // Exclude any edge that has a source or target node that is not in the set of passed-in nodes
- `filter` (@ `src/collection/filter.mjs`) -> DB Complexity: **122**
- `load` (@ `src/extensions/renderer/base/load-listeners.mjs`) -> DB Complexity: **121**
- `registerArrowShapes` (@ `src/extensions/renderer/base/arrow-shapes.mjs`) -> DB Complexity: **81**
- `weight` (@ `src/collection/algorithms/bellman-ford.mjs`) -> DB Complexity: **75**
- `weight` (@ `src/collection/algorithms/floyd-warshall.mjs`) -> DB Complexity: **61**
- `run` (@ `src/extensions/layout/concentric.mjs`) -> DB Complexity: **56**
- `CanvasRenderer` (@ `src/extensions/renderer/canvas/index.mjs`) -> DB Complexity: **54**
  * *Intent:* //
- `generateBarrel` (@ `src/extensions/renderer/base/node-shapes.mjs`) -> DB Complexity: **53**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/collection/algorithms` | 20 | 4354.56 | 68.82% | 0.0% |
| `src/collection` | 18 | 4155.76 | 67.71% | 8.24% |
| `src/extensions/renderer/canvas` | 15 | 3767.44 | 78.36% | 3.11% |
| `src` | 17 | 2941.54 | 54.71% | 6.56% |
| `src/extensions/renderer/base/coord-ele-math` | 10 | 2162.98 | 76.91% | 0.0% |
| `src/style` | 9 | 2137.66 | 75.19% | 7.06% |
| `src/collection/dimensions` | 5 | 2083.12 | 65.42% | 38.15% |
| `src/extensions/renderer/base` | 6 | 1993.66 | 72.12% | 0.0% |
| `src/extensions/renderer/canvas/webgl` | 7 | 1850.84 | 40.7% | 23.32% |
| `src/extensions/layout` | 9 | 1749.62 | 77.38% | 11.11% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/workflows/scripts/merge_unstable_to_master.sh` -> **100.0%** Exposure
- `.github/workflows/scripts/pre_release_test.sh` -> **100.0%** Exposure
- `src/extensions/layout/null.mjs` -> **100.0%** Exposure
- `src/selector/state.mjs` -> **100.0%** Exposure
- `.github/workflows/scripts/new-patch-version.sh` -> **99.9995%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/workflows/scripts/new-feature-version.sh` -> **100.0%** Exposure
- `.github/workflows/scripts/new-patch-version.sh` -> **100.0%** Exposure
- `benchmark/add-remove.js` -> **100.0%** Exposure
- `benchmark/add.js` -> **100.0%** Exposure
- `benchmark/all/index.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/selector/state.mjs` -> **0** Orphaned Functions | **29** Duplicates
- `index.d.ts` -> **18** Orphaned Functions | **3** Duplicates
- `.github/workflows/scripts/merge_unstable_to_master.sh` -> **1** Orphaned Functions | **8** Duplicates
- `src/collection/switch-functions.mjs` -> **0** Orphaned Functions | **7** Duplicates
- `.github/workflows/scripts/pre_release_test.sh` -> **1** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`rollup.config.mjs`** -> AI Confidence: **99.31%**
2. **`src/extensions/renderer/base/index.mjs`** -> AI Confidence: **99.31%**
3. **`src/cjs.mjs`** -> AI Confidence: **99.29%**
4. **`src/selector/tokens.mjs`** -> AI Confidence: **99.29%**
5. **`src/util/regex.mjs`** -> AI Confidence: **99.29%**
6. **`src/collection/index.mjs`** -> AI Confidence: **99.24%**
7. **`documentation/docmaker.mjs`** -> AI Confidence: **99.23%**
8. **`src/extension.mjs`** -> AI Confidence: **99.23%**
9. **`src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs`** -> AI Confidence: **99.22%**
10. **`src/index.mjs`** -> AI Confidence: **99.18%**
11. **`src/util/index.mjs`** -> AI Confidence: **99.18%**
12. **`.github/workflows/scripts/pre_release_test.sh`** -> AI Confidence: **99.17%**
13. **`src/extensions/renderer/canvas/webgl/fxaa-upscaler.mjs`** -> AI Confidence: **99.17%**
14. **`src/core/index.mjs`** -> AI Confidence: **99.16%**
15. **`src/extensions/renderer/canvas/index.mjs`** -> AI Confidence: **99.16%**
16. **`src/style/index.mjs`** -> AI Confidence: **99.16%**
17. **`src/define/data.mjs`** -> AI Confidence: **99.13%**
18. **`src/extensions/renderer/base/coord-ele-math/edge-control-points.mjs`** -> AI Confidence: **99.13%**
19. **`src/selector/index.mjs`** -> AI Confidence: **99.13%**
20. **`playwright.config.js`** -> AI Confidence: **99.09%**
21. **`src/collection/algorithms/index.mjs`** -> AI Confidence: **99.09%**
22. **`src/collection/dimensions/bounds.mjs`** -> AI Confidence: **99.09%**
23. **`src/collection/element.mjs`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `documentation/demos/radius-types/code.js` -> **100.0%** Exposure
- `documentation/docmaker.mjs` -> **100.0%** Exposure
- `documentation/js/script.js` -> **100.0%** Exposure
- `src/collection/algorithms/bellman-ford.mjs` -> **100.0%** Exposure
- `src/collection/algorithms/betweenness-centrality.mjs` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `documentation/demos/fcose-gene/code.js` -> **100.0%** Exposure
- `documentation/demos/radius-types/code.js` -> **100.0%** Exposure
- `documentation/docmaker.mjs` -> **100.0%** Exposure
- `src/collection/algorithms/affinity-propagation.mjs` -> **100.0%** Exposure
- `src/collection/algorithms/bellman-ford.mjs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `153` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/promise.mjs` (JAVASCRIPT) -> Cumulative Risk: **870.36**
- **Archetype:** `file_cluster_4` (Distance: 14.267 IQR)
- **Magnitude:** 320.78 | **LOC:** 212 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `resolve` (Impact: 113.3), `all` (Impact: 25.7), `resolver` (Impact: 15.8)

### 2. `src/collection/dimensions/width-height.mjs` (JAVASCRIPT) -> Cumulative Risk: **819.21**
- **Archetype:** `file_cluster_8` (Distance: 12.192 IQR)
- **Magnitude:** 172.82 | **LOC:** 131 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9911%)
- **Heaviest Functions:** `defineDimFns` (Impact: 80.3), `padding` (Impact: 14.9), `paddedHeight` (Impact: 1.7)

### 3. `documentation/demos/radius-types/code.js` (JAVASCRIPT) -> Cumulative Risk: **809.13**
- **Archetype:** `file_cluster_4` (Distance: 12.502 IQR)
- **Magnitude:** 147.92 | **LOC:** 95 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setTimeout` (Impact: 63.2), `onchange` (Impact: 2.3), `toJson` (Impact: 1.9)

### 4. `src/extensions/renderer/canvas/webgl/misc-upscaler.js` (JAVASCRIPT) -> Cumulative Risk: **807.95**
- **Archetype:** `file_cluster_8` (Distance: 13.008 IQR)
- **Magnitude:** 264.68 | **LOC:** 208 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `createShader` (Impact: 14.5), `createProgram` (Impact: 14.5), `resize` (Impact: 8.8)

### 5. `src/extensions/renderer/canvas/export-image.mjs` (JAVASCRIPT) -> Cumulative Risk: **807.68**
- **Archetype:** `file_cluster_4` (Distance: 12.275 IQR)
- **Magnitude:** 250.8 | **LOC:** 173 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `output` (Impact: 89.5), `bufferCanvasImage` (Impact: 49.9), `png` (Impact: 4.2)

### 6. `src/collection/dimensions/position.mjs` (JAVASCRIPT) -> Cumulative Risk: **795.94**
- **Archetype:** `file_cluster_11` (Distance: 13.817 IQR)
- **Magnitude:** 462.64 | **LOC:** 273 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `relativePosition` (Impact: 86.1), `renderedPosition` (Impact: 57.2), `shift` (Impact: 47.4)

### 7. `src/extensions/renderer/canvas/texture-cache-defs.mjs` (JAVASCRIPT) -> Cumulative Risk: **766.85**
- **Archetype:** `file_cluster_11` (Distance: 14.617 IQR)
- **Magnitude:** 184.58 | **LOC:** 92 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setupDequeueing` (Impact: 129.2)

### 8. `src/collection/switch-functions.mjs` (JAVASCRIPT) -> Cumulative Risk: **754.55**
- **Archetype:** `file_cluster_8` (Distance: 12.426 IQR)
- **Magnitude:** 195.5 | **LOC:** 165 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9988%)
- **Heaviest Functions:** `defineSwitchFunction` (Impact: 83.4), `defineSwitchSet` (Impact: 15.1), `grabbed` (Impact: 6.0)

### 9. `src/collection/iteration.mjs` (JAVASCRIPT) -> Cumulative Risk: **750.5**
- **Archetype:** `file_cluster_11` (Distance: 13.931 IQR)
- **Magnitude:** 229.56 | **LOC:** 156 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `zDepth` (Impact: 26.7), `defineSymbolIterator` (Impact: 18.7), `forEach` (Impact: 16.3)

### 10. `src/collection/algorithms/dijkstra.mjs` (JAVASCRIPT) -> Cumulative Risk: **748.92**
- **Archetype:** `file_cluster_17` (Distance: 14.507 IQR)
- **Magnitude:** 262.0 | **LOC:** 134 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `weight` (Impact: 131.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/collection/dimensions/bounds.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.331 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.974 IQR)
- **Top Global Matches:** file_cluster_8: 13.331, file_cluster_17: 13.483, file_cluster_11: 13.516
- **Magnitude:** 1378.56 | **LOC:** 1045 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (76.3983%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `boundingBoxImpl` (Impact: 261.3 | O(N^3) | DB: 44)
  * `updateCompoundBounds` (Impact: 179.1 | O(N^3) | DB: 25)
  * `updateBoundsFromLabel` (Impact: 168.8 | O(N^3) | DB: 45)
  * `cachedBoundingBoxImpl` (Impact: 54.7 | O(N^2) | DB: 6)
  * `boundingBox` (Impact: 48.1 | O(N^2) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 244`, `args: 33`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 518`, `dead_code: 2`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 34`, `test: 16`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, is.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/math.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.986 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.745 IQR)
- **Top Global Matches:** file_cluster_8: 12.986, file_cluster_11: 13.079, file_cluster_17: 13.162
- **Magnitude:** 1228.42 | **LOC:** 1479 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 164
- **Risk Profile:** Cognitive Load (91.9767%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `median` (Impact: 653.3 | O(N^2) | DB: 164)
  * `min` (Impact: 12.7 | O(2^N) | DB: 3)
  * `max` (Impact: 12.7 | O(2^N) | DB: 3)
  * `mean` (Impact: 6.8 | O(N^1) | DB: 4)
  * `modelToRenderedPosition` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 366`, `args: 77`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 452`, `dead_code: 2`
* *Architecture:* `api: 67`
* *Defense:* `safety: 23`, `immutability_locks: 89`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/load-listeners.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.468 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.023 IQR)
- **Top Global Matches:** file_cluster_11: 13.468, file_cluster_8: 13.548, file_cluster_13: 13.597
- **Magnitude:** 1202.38 | **LOC:** 2203 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 121
- **Risk Profile:** Cognitive Load (96.0836%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 761.0 | O(N^4) | DB: 121)
  * `binder` (Impact: 35.8 | O(N^2) | DB: 8)
  * `registerBinding` (Impact: 14.3 | O(N^2) | DB: 9)
    * *Intent:* /* global document, ResizeObserver, MutationObserver */
  * `nodeIsDraggable` (Impact: 8.4 | O(N^1))
  * `nodeIsGrabbable` (Impact: 4.3 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 165`, `args: 27`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 356`, `dead_code: 6`
* *Architecture:* `api: 2`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 22`, `test: 37`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, math.mjs, is.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/coord-ele-math/edge-control-points.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.2 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.718 IQR)
- **Top Global Matches:** file_cluster_8: 13.2, file_cluster_11: 13.34, file_cluster_13: 13.345
- **Magnitude:** 1035.96 | **LOC:** 1058 | **CtrlFlow:** 50.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (78.8268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `findEdgeControlPoints` (Impact: 153.3 | O(N^3) | DB: 37)
  * `findTaxiPoints` (Impact: 138.6 | O(N^2) | DB: 21)
  * `storeAllpts` (Impact: 89.2 | O(N^3) | DB: 19)
  * `tryToCorrectInvalidPoints` (Impact: 49.7 | O(N^2) | DB: 27)
  * `findBezierPoints` (Impact: 34.4 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 167`, `args: 21`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 433`, `dead_code: 3`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 40`, `test: 1`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, is.mjs, math.mjs, map.mjs, round.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.568 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.857 IQR)
- **Top Global Matches:** file_cluster_8: 12.568, file_cluster_13: 12.632, file_cluster_17: 12.701
- **Magnitude:** 906.38 | **LOC:** 1154 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (72.4251%), Tech Debt (10.3673%)
**Top Internal Functions/Classes:**
  * `_createShaderProgram` (Impact: 267.1 | O(N^4) | DB: 4)
    * *Intent:* /** * @param { string } collectionName
  * `drawNode` (Impact: 52.1 | O(N^2) | DB: 21)
  * `drawEdgeLine` (Impact: 33.1 | O(N^2) | DB: 30)
  * `drawTexture` (Impact: 31.7 | O(N^2) | DB: 7)
  * `_setCurvePoint` (Impact: 27.6 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 64`, `args: 34`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 320`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 12`, `doc: 24`, `immutability_locks: 92`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, gl-matrix, atlas.mjs, shader-sdf.mjs, math.mjs, webgl-util.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/viewport.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.309 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.408 IQR)
- **Top Global Matches:** file_cluster_8: 13.309, file_cluster_11: 13.513, file_cluster_13: 13.576
- **Magnitude:** 828.78 | **LOC:** 610 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (78.7636%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `viewport` (Impact: 116.7 | O(2^N) | DB: 14)
  * `pan` (Impact: 83.6 | O(2^N) | DB: 9)
  * `getFitViewport` (Impact: 55.1 | O(N^2) | DB: 10)
  * `zoom` (Impact: 43.1 | O(2^N) | DB: 7)
  * `panBy` (Impact: 41.4 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 85`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 265`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/layout/cose.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.977 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.635 IQR)
- **Top Global Matches:** file_cluster_11: 14.977, file_cluster_17: 14.988, file_cluster_0: 15.114
- **Magnitude:** 780.88 | **LOC:** 1341 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 162
- **Risk Profile:** Cognitive Load (70.0161%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 274.6 | O(N^2) | DB: 162)
    * *Intent:* // Exclude any edge that has a source or target node that is not in the set of passed-in nodes
  * `CoseLayout` (Impact: 5.3 | O(N^1) | DB: 6)
  * `nodeRepulsion` (Impact: 2.0 | O(N^1))
  * `idealEdgeLength` (Impact: 2.0 | O(N^1))
  * `edgeElasticity` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 192`, `args: 32`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 478`, `dead_code: 9`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 24`, `doc: 15`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, index.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `documentation/docmaker.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.886 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.037 IQR)
- **Top Global Matches:** file_cluster_17: 13.886, file_cluster_11: 13.997, file_cluster_13: 13.999
- **Magnitude:** 757.18 | **LOC:** 458 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (73.5885%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compileConfig` (Impact: 388.1 | O(2^N) | DB: 34)
  * `md2html` (Impact: 29.1 | O(N^2) | DB: 12)
    * *Intent:* // let html = converter.makeHtml("**I am bold!**"); // let html = Handlebars.compile();
  * `processFields` (Impact: 23.1 | O(2^N) | DB: 3)
  * `sortSoftwareVersions` (Impact: 16.7 | O(N^1) | DB: 3)
  * `parseSubsections` (Impact: 14.6 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 96`, `args: 22`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 212`, `dead_code: 5`
* *Architecture:* `io: 19`, `import: 7`
* *Defense:* `safety: 12`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` handlebars, process, fs, path, jsonlint, marked, highlight.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/traversing.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.988 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.483 IQR)
- **Top Global Matches:** file_cluster_17: 13.988, file_cluster_11: 14.285, file_cluster_13: 14.392
- **Magnitude:** 707.2 | **LOC:** 425 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (76.6144%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `defineEdgesWithFunction` (Impact: 62.2 | O(N^2) | DB: 16)
  * `components` (Impact: 58.8 | O(2^N) | DB: 9)
  * `defineDagExtremity` (Impact: 53.8 | O(N^3) | DB: 12)
    * *Intent:* // DAG functions ////////////////
  * `defineParallelEdgesFunction` (Impact: 35.5 | O(N^2) | DB: 21)
  * `defineDagOneHop` (Impact: 31.4 | O(N^2) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 129`, `args: 26`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 384`, `dead_code: 2`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 12`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, cache-traversal-call.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/drawing-redraw.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.195 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.598 IQR)
- **Top Global Matches:** file_cluster_11: 14.195, file_cluster_17: 14.298, file_cluster_0: 14.33
- **Magnitude:** 695.48 | **LOC:** 722 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (81.555%), Tech Debt (46.6268%)
**Top Internal Functions/Classes:**
  * `createGradientStyleFor` (Impact: 165.4 | O(N^3) | DB: 14)
  * `render` (Impact: 62.5 | O(N^1) | DB: 26)
  * `drawSelectionRectangle` (Impact: 46.1 | O(N^2) | DB: 8)
  * `matchCanvasSize` (Impact: 19.1 | O(N^1) | DB: 13)
    * *Intent:* // Resize canvas
  * `getPixelRatio` (Impact: 13.6 | O(N^1) | DB: 7)
    * *Intent:* // var isFirefox = typeof InstallTrigger !== 'undefined';
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 101`, `args: 17`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 297`, `dead_code: 7`, `duplicate_logic: 4`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 22`, `test: 11`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/filter.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.731 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.262 IQR)
- **Top Global Matches:** file_cluster_17: 13.731, file_cluster_8: 13.873, file_cluster_11: 13.949
- **Magnitude:** 665.54 | **LOC:** 394 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 122
- **Risk Profile:** Cognitive Load (89.0675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `filter` (Impact: 255.6 | O(2^N) | DB: 122)
  * `byGroup` (Impact: 9.3 | O(N^2) | DB: 9)
    * *Intent:* // internal helper to get nodes and edges as separate collections with single iteration over element...
  * `nodes` (Impact: 2.1 | O(N^1) | DB: 1)
  * `edges` (Impact: 2.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 123`, `args: 23`, `func_start: 25`
* *Risk/State:* `state_mutation: 389`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 2`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/drawing-edges.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.449 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.284 IQR)
- **Top Global Matches:** file_cluster_11: 13.449, file_cluster_17: 13.549, file_cluster_0: 13.597
- **Magnitude:** 608.8 | **LOC:** 432 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (76.7461%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawEdgePath` (Impact: 165.4 | O(N^3) | DB: 29)
  * `drawEdge` (Impact: 86.2 | O(N^2) | DB: 24)
  * `drawArrowShape` (Impact: 73.0 | O(N^1) | DB: 32)
  * `drawArrowhead` (Impact: 41.8 | O(N^1) | DB: 10)
  * `drawEdgeOverlayUnderlay` (Impact: 15.9 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 90`, `args: 14`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 206`, `dead_code: 3`
* *Architecture:* `io: 11`, `api: 2`, `import: 2`
* *Defense:* `safety: 19`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, round.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/style/apply.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.379 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.623 IQR)
- **Top Global Matches:** file_cluster_17: 15.379, file_cluster_4: 15.463, file_cluster_11: 15.468
- **Magnitude:** 605.88 | **LOC:** 850 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (96.0969%), Tech Debt (39.7315%)
**Top Internal Functions/Classes:**
  * `applyContextStyle` (Impact: 128.1 | O(N^2) | DB: 36)
  * `getPropertiesDiff` (Impact: 49.3 | O(N^2) | DB: 17)
  * `printMappingErr` (Impact: 17.8 | O(2^N) | DB: 5)
  * `apply` (Impact: 15.7 | O(N^1) | DB: 11)
    * *Intent:* // (potentially expensive calculation) // apply the style to the element based on // - its bypass //...
  * `getContextStyle` (Impact: 15.5 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 130`, `args: 27`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 312`, `dead_code: 11`, `duplicate_logic: 3`
* *Architecture:* `api: 2`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 14`, `test: 2`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, promise.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/define/data.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.822 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.526 IQR)
- **Top Global Matches:** file_cluster_11: 13.822, file_cluster_13: 13.822, file_cluster_17: 13.972
- **Magnitude:** 568.78 | **LOC:** 209 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (80.2596%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `data` (Impact: 386.6 | O(2^N) | DB: 37)
    * *Intent:* // access data field
  * `removeData` (Impact: 63.1 | O(N^3) | DB: 17)
    * *Intent:* // remove data field
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 53`, `args: 8`, `func_start: 9`
* *Risk/State:* `state_mutation: 114`, `dead_code: 2`
* *Architecture:* `io: 5`, `api: 2`, `import: 5`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, get.js, toPath.js, set.js, is.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/algorithms/bellman-ford.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.929 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.15 IQR)
- **Top Global Matches:** file_cluster_8: 12.929, file_cluster_13: 12.977, file_cluster_17: 13.083
- **Magnitude:** 488.22 | **LOC:** 203 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (73.7519%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `weight` (Impact: 330.2 | O(2^N) | DB: 75)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 63`, `args: 9`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 154`
* *Architecture:* `io: 5`, `api: 1`, `import: 3`
* *Defense:* `safety: 3`, `test: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` map.mjs, is.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/style.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.879 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.966 IQR)
- **Top Global Matches:** file_cluster_17: 13.879, file_cluster_11: 13.947, file_cluster_8: 14.098
- **Magnitude:** 479.12 | **LOC:** 458 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (77.0293%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `defineDerivedStateFunction` (Impact: 51.8 | O(N^2) | DB: 10)
  * `parsedStyle` (Impact: 22.1 | O(N^2) | DB: 3)
    * *Intent:* // get the internal parsed style object for the specified property
  * `updateStyle` (Impact: 17.8 | O(N^1) | DB: 9)
    * *Intent:* // fully updates (recalculates) the style for the elements
  * `styleCache` (Impact: 16.6 | O(2^N) | DB: 3)
  * `effectiveOpacity` (Impact: 16.2 | O(N^2) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 117`, `args: 31`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 248`, `dead_code: 2`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 16`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/algorithms/affinity-propagation.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.645 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.349 IQR)
- **Top Global Matches:** file_cluster_17: 13.645, file_cluster_13: 13.658, file_cluster_11: 13.696
- **Magnitude:** 478.54 | **LOC:** 330 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (74.4374%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `affinityPropagation` (Impact: 116.8 | O(N^2) | DB: 50)
  * `assign` (Impact: 22.6 | O(N^2) | DB: 10)
  * `assignClusters` (Impact: 19.3 | O(N^2) | DB: 8)
  * `getPreference` (Impact: 16.4 | O(N^1) | DB: 1)
  * `setOptions` (Impact: 10.8 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 103`, `args: 14`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 267`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 11`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, clustering-distances.mjs, index.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/index.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.959 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.235 IQR)
- **Top Global Matches:** file_cluster_13: 12.959, file_cluster_8: 13.3, file_cluster_11: 13.367
- **Magnitude:** 464.82 | **LOC:** 839 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (75.9592%), Tech Debt (48.3413%)
**Top Internal Functions/Classes:**
  * `move` (Impact: 155.4 | O(2^N) | DB: 20)
  * `Collection` (Impact: 73.8 | O(N^3) | DB: 7)
    * *Intent:* // represents a set of nodes, edges, or both together
  * `restore` (Impact: 27.6 | O(N^2) | DB: 9)
  * `checkSwitch` (Impact: 15.6 | O(N^2) | DB: 1)
  * `clone` (Impact: 6.4 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 87`, `args: 11`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 172`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 21`
* *Defense:* `safety: 9`, `test: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, degree.mjs, data.mjs, layout.mjs, is.mjs, comparators.mjs, traversing.mjs, index.mjs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/dimensions/position.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.817 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.918 IQR)
- **Top Global Matches:** file_cluster_11: 13.817, file_cluster_13: 13.875, file_cluster_17: 13.973
- **Magnitude:** 462.64 | **LOC:** 273 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (79.939%), Tech Debt (91.2033%)
**Top Internal Functions/Classes:**
  * `relativePosition` (Impact: 86.1 | O(N^3) | DB: 18)
    * *Intent:* // get/set the position relative to the parent
  * `renderedPosition` (Impact: 57.2 | O(N^3) | DB: 11)
    * *Intent:* // get/set the rendered (i.e. on screen) positon of the element
  * `shift` (Impact: 47.4 | O(N^2) | DB: 9)
  * `positions` (Impact: 36.2 | O(N^3) | DB: 9)
  * `beforePositionSet` (Impact: 25.0 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 61`, `args: 13`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 178`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 12`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, index.mjs, is.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/node-shapes.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.188 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.955 IQR)
- **Top Global Matches:** file_cluster_8: 12.188, file_cluster_11: 12.519, file_cluster_13: 12.564
- **Magnitude:** 421.94 | **LOC:** 659 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (59.5396%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generateBarrel` (Impact: 52.7 | O(N^3) | DB: 53)
  * `generateRoundPolygon` (Impact: 21.5 | O(N^2) | DB: 10)
  * `generateBottomRoundrectangle` (Impact: 21.4 | O(N^2) | DB: 16)
  * `generateRoundRectangle` (Impact: 21.3 | O(N^2) | DB: 10)
  * `generateCutRectangle` (Impact: 20.2 | O(N^2) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 136`, `args: 37`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 253`, `dead_code: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 9`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math.mjs, round.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/define/animation.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.586 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.01 IQR)
- **Top Global Matches:** file_cluster_13: 13.586, file_cluster_8: 13.624, file_cluster_11: 13.683
- **Magnitude:** 346.28 | **LOC:** 240 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (80.2548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `animation` (Impact: 70.6 | O(N^2) | DB: 19)
  * `stop` (Impact: 27.5 | O(N^3) | DB: 12)
  * `animate` (Impact: 20.4 | O(N^2) | DB: 9)
  * `delay` (Impact: 13.4 | O(2^N) | DB: 3)
  * `clearQueue` (Impact: 11.5 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 78`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 178`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 8`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, math.mjs, animation.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/emitter.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.03 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.353 IQR)
- **Top Global Matches:** file_cluster_11: 14.03, file_cluster_13: 14.191, file_cluster_17: 14.198
- **Magnitude:** 345.62 | **LOC:** 241 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (94.8612%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `trigger` (Impact: 48.1 | O(N^2) | DB: 11)
  * `off` (Impact: 41.5 | O(N^2) | DB: 8)
  * `forEachEvent` (Impact: 38.4 | O(N^1) | DB: 7)
  * `forEachEventObj` (Impact: 31.6 | O(N^2) | DB: 7)
  * `addListener` (Impact: 8.1 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 51`, `args: 21`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 140`, `dead_code: 2`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 13`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, event.mjs, is.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/webgl/atlas.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.391 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.016 IQR)
- **Top Global Matches:** file_cluster_13: 13.391, file_cluster_8: 13.428, file_cluster_17: 13.473
- **Magnitude:** 343.66 | **LOC:** 647 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (87.7343%), Tech Debt (46.5185%)
**Top Internal Functions/Classes:**
  * `gc` (Impact: 47.5 | O(N^3) | DB: 32)
    * *Intent:* // called on every frame
  * `draw` (Impact: 30.9 | O(2^N) | DB: 9)
  * `drawWrapped` (Impact: 9.4 | O(N^3) | DB: 6)
    * *Intent:* // if the scaled width is too wide then scale to fit max width instead
  * `bufferIfNeeded` (Impact: 9.2 | O(N^2) | DB: 10)
  * `constructor` (Impact: 8.8 | O(N^2) | DB: 20)
    * *Intent:* // A "texture atlas" is a big canvas, and sections of it are used as textures for nodes/labels. /** ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 25`, `args: 22`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 203`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 3`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` webgl-util.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/algorithms/hierholzer.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.583 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.336 IQR)
- **Top Global Matches:** file_cluster_17: 12.583, file_cluster_8: 12.602, file_cluster_13: 12.757
- **Magnitude:** 326.74 | **LOC:** 137 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (84.1481%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hierholzer` (Impact: 210.2 | O(N^3) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 38`, `args: 8`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 112`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/coord-ele-math/labels.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.198 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.815 IQR)
- **Top Global Matches:** file_cluster_11: 13.198, file_cluster_13: 13.215, file_cluster_8: 13.229
- **Magnitude:** 324.0 | **LOC:** 566 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (79.222%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `recalculateEdgeLabelProjections` (Impact: 89.5 | O(N^2) | DB: 42)
  * `recalculateNodeLabelProjection` (Impact: 30.5 | O(N^1) | DB: 13)
  * `getLabelJustification` (Impact: 20.1 | O(N^2) | DB: 2)
  * `lineAngleFromDelta` (Impact: 5.6 | O(N^1) | DB: 1)
  * `bezierAngle` (Impact: 2.7 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 84`, `args: 11`, `func_start: 19`
* *Risk/State:* `state_mutation: 162`, `dead_code: 2`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `documentation/demos/colajs-graph/index.html` (HTML) | Magnitude: 19.72 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, io: 19, decorators: 11, structural_boundaries: 10
- `playwright.config.js` (JAVASCRIPT) | Magnitude: 16.46 | Delta: **0.175 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, globals: 4, branch: 3, sec_io: 3
- `documentation/demos/radius-types/index.html` (HTML) | Magnitude: 20.42 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, args: 4, api: 4
- `documentation/template.html` (HTML) | Magnitude: 78.86 | Delta: **0.616 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 235, ssr_boundaries: 132, structural_boundaries: 100, decorators: 91
- `documentation/demos/fcose-gene/index.html` (HTML) | Magnitude: 19.8 | Delta: **0.821 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, io: 23, decorators: 13, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/define/data.mjs` (JAVASCRIPT) | Magnitude: 568.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 146, state_mutation: 114, structural_boundaries: 53, branch: 52
- `src/collection/class.mjs` (JAVASCRIPT) | Magnitude: 244.2 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 101, indent_spaces: 99, structural_boundaries: 41, branch: 31
- `src/extensions/layout/cose.mjs` (JAVASCRIPT) | Magnitude: 780.88 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 478, indent_spaces: 467, structural_boundaries: 192, branch: 112
- `src/extensions/renderer/base/coord-ele-math/labels.mjs` (JAVASCRIPT) | Magnitude: 324.0 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 201, state_mutation: 162, structural_boundaries: 84, branch: 50
- `src/extensions/layout/concentric.mjs` (JAVASCRIPT) | Magnitude: 236.76 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 166, indent_spaces: 134, structural_boundaries: 62, branch: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/core/animation/step.mjs` (JAVASCRIPT) | Magnitude: 236.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 87, branch: 44, structural_boundaries: 41
- `src/selector/data.mjs` (JAVASCRIPT) | Magnitude: 40.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 18, state_mutation: 18, branch: 7
- `src/collection/algorithms/betweenness-centrality.mjs` (JAVASCRIPT) | Magnitude: 265.32 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 129, indent_spaces: 118, structural_boundaries: 46, branch: 25
- `src/collection/algorithms/page-rank.mjs` (JAVASCRIPT) | Magnitude: 163.86 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 80, indent_spaces: 66, structural_boundaries: 34, branch: 14
- `src/extensions/layout/random.mjs` (JAVASCRIPT) | Magnitude: 33.58 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 20, structural_boundaries: 13, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/collection/algorithms/floyd-warshall.mjs` (JAVASCRIPT) | Magnitude: 252.22 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 111, indent_spaces: 89, structural_boundaries: 54, branch: 19
- `src/collection/algorithms/affinity-propagation.mjs` (JAVASCRIPT) | Magnitude: 478.54 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 267, indent_spaces: 224, structural_boundaries: 103, branch: 64
- `src/collection/algorithms/hierholzer.mjs` (JAVASCRIPT) | Magnitude: 326.74 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 112, branch: 51, structural_boundaries: 38
- `src/collection/style.mjs` (JAVASCRIPT) | Magnitude: 479.12 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 248, indent_spaces: 241, structural_boundaries: 117, branch: 83
- `src/event.mjs` (JAVASCRIPT) | Magnitude: 172.76 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 100, indent_spaces: 64, branch: 19, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `index.d.ts` (TYPESCRIPT) | Magnitude: 116.1 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1372, doc: 791, branch: 356, args: 326

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/extensions/renderer/base/redraw.mjs` (JAVASCRIPT) | Magnitude: 26.72 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, branch: 6, state_mutation: 6, structural_boundaries: 5
- `documentation/demos/tokyo-railways/tokyo-railways.js` (JAVASCRIPT) | Magnitude: 84.24 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 45, concurrency: 24, state_mutation: 20, structural_boundaries: 16
- `documentation/demos/edge-types/code.js` (JAVASCRIPT) | Magnitude: 30.22 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 16, structural_boundaries: 15, concurrency: 12
- `documentation/demos/edge-arrows/index.html` (HTML) | Magnitude: 19.32 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, io: 3, api: 3
- `documentation/demos/edge-types/index.html` (HTML) | Magnitude: 18.3 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, io: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/extensions/layout/breadthfirst.mjs` (JAVASCRIPT) | Magnitude: 190.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 183, state_mutation: 62, immutability_locks: 59, branch: 48
- `src/extensions/renderer/base/coord-ele-math/edge-projection.mjs` (JAVASCRIPT) | Magnitude: 89.66 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 44, indent_spaces: 39, structural_boundaries: 16, branch: 12
- `src/extensions/renderer/canvas/ele-texture-cache-lookup.mjs` (JAVASCRIPT) | Magnitude: 188.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 122, indent_spaces: 122, structural_boundaries: 44, args: 22
- `src/collection/group.mjs` (JAVASCRIPT) | Magnitude: 43.62 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 18, structural_boundaries: 8, args: 5
- `benchmark/a-star.js` (JAVASCRIPT) | Magnitude: 7.9 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 5, state_mutation: 4, args: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` -> Churn: **66.36%** | Cog Load: 72.4251% | Debt: 10.3673%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` -> **Mike Kucera** (100.0% isolated ownership) | Magnitude: 906.38
- `documentation/docmaker.mjs` -> **Max Franz** (100.0% isolated ownership) | Magnitude: 757.18
- `src/collection/index.mjs` -> **Felix Pahl** (100.0% isolated ownership) | Magnitude: 464.82
- `src/extensions/renderer/canvas/webgl/webgl-util.mjs` -> **Mike Kucera** (100.0% isolated ownership) | Magnitude: 124.72

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `documentation/demos/tokyo-railways/tokyo-railways.js` -> **Severity: 0.114** (Embedded: 0.0018 * Error Risk: 61.9149%)
- `benchmark/collection-creation.js` -> **Severity: 0.061** (Embedded: 0.0018 * Error Risk: 33.0615%)
- `src/test.mjs` -> **Severity: 0.035** (Embedded: 0.0018 * Error Risk: 19.0858%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `benchmark/collection-creation.js` -> **Severity: 335.486** (Blast Radius: 3.38 * Doc Risk: 99.2563%)
- `src/is.mjs` -> **Severity: 182.7** (Blast Radius: 1.827 * Doc Risk: 99.9999%)
- `src/util/index.mjs` -> **Severity: 182.699** (Blast Radius: 1.827 * Doc Risk: 99.9996%)
- `src/util/strings.mjs` -> **Severity: 182.688** (Blast Radius: 1.827 * Doc Risk: 99.9937%)
- `src/collection/group.mjs` -> **Severity: 182.601** (Blast Radius: 1.827 * Doc Risk: 99.946%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
