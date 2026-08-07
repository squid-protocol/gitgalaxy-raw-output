# ARCHITECTURAL_BRIEF: cytoscape.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/cytoscape.js` |
| **Timestamp** | `2026-08-07T04:23:54.287559+00:00` |
| **Scan Duration** | `1.38s` |
| **Git Branch** | `unstable` |
| **Git Commit** | `816e98077a6447f491efec81b22cab19e5a56f25` |
| **Git Remote** | `https://github.com/cytoscape/cytoscape.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 233 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
> **Architectural Drift Z-Score:** `3.303`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 208 | 38.2% |
| file_cluster_13 | 72 | 13.2% |
| file_cluster_17 | 23 | 4.2% |
| file_cluster_11 | 21 | 3.9% |
| file_cluster_4 | 16 | 2.9% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 39.3 | 31.5 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 55.7 | 70.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.0 | 2.4 | 2.3 |
| API Exposure | 0.0 | 16.7 | 3.8 | 4.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 55.7 | 99.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 75.4 | 3.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 95.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.2 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 66.4 | 0.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.0 | 32.1 | 11.9 |
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

- `median` (@ `src/math.mjs`) -> Impact: **452.3** | LOC: 1002
- `allowPanningPassthrough` (@ `src/extensions/renderer/base/load-listeners.mjs`) -> Impact: **381.1** | LOC: 833
- `load` (@ `src/extensions/renderer/base/load-listeners.mjs`) -> Impact: **330.4** | LOC: 866
- `siblings` (@ `index.d.ts`) -> Impact: **323.0** | LOC: 1159
- `inBezierVicinity` (@ `src/math.mjs`) -> Impact: **241.3** | LOC: 463
- `mouseupHandler` (@ `src/extensions/renderer/base/load-listeners.mjs`) -> Impact: **201.3** | LOC: 359
- `run` (@ `src/extensions/layout/cose.mjs`) -> Impact: **195.4** | LOC: 741
  * *Intent:* // Exclude any edge that has a source or target node that is not in the set of passed-in nodes
- `mousemoveHandler` (@ `src/extensions/renderer/base/load-listeners.mjs`) -> Impact: **183.2** | LOC: 266
  * *Intent:* // auto resize
- `nodeRepulsion` (@ `src/extensions/layout/cose.mjs`) -> Impact: **164.4** | LOC: 382
  * *Intent:* /** * @brief : This function finds the index of the lowest common * graph ancestor between 2 nodes in the subtree * (from the graph hierarchy induced ...
- `boundingBoxImpl` (@ `src/collection/dimensions/bounds.mjs`) -> Impact: **138.3** | LOC: 306

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/collection/algorithms` | 20 | 3795.36 | 69.86% | 33.24% |
| `src/collection` | 18 | 3748.46 | 67.58% | 16.72% |
| `src/extensions/renderer/canvas` | 15 | 3501.54 | 78.78% | 18.63% |
| `src` | 17 | 3316.54 | 53.99% | 18.38% |
| `src/extensions/renderer/base` | 6 | 2810.16 | 80.81% | 49.97% |
| `src/extensions/renderer/base/coord-ele-math` | 10 | 2125.88 | 76.91% | 24.87% |
| `src/extensions/layout` | 9 | 2100.12 | 75.35% | 42.99% |
| `src/style` | 9 | 2024.06 | 75.18% | 24.25% |
| `src/collection/dimensions` | 5 | 2012.92 | 64.91% | 58.14% |
| `src/extensions/renderer/canvas/webgl` | 7 | 1602.24 | 40.91% | 54.13% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/workflows/scripts/merge_unstable_to_master.sh` -> **100.0%** Exposure
- `.github/workflows/scripts/pre_release_test.sh` -> **100.0%** Exposure
- `benchmark/suite/index.js` -> **100.0%** Exposure
- `rollup.config.mjs` -> **100.0%** Exposure
- `src/collection/algorithms/a-star.mjs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/workflows/scripts/new-feature-version.sh` -> **100.0%** Exposure
- `.github/workflows/scripts/new-patch-version.sh` -> **100.0%** Exposure
- `benchmark/add-remove.js` -> **100.0%** Exposure
- `benchmark/add.js` -> **100.0%** Exposure
- `benchmark/all/index.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `index.d.ts` -> **33** Orphaned Functions | **12** Duplicates
- `src/extensions/renderer/base/arrow-shapes.mjs` -> **0** Orphaned Functions | **33** Duplicates
- `src/collection/dimensions/bounds.mjs` -> **0** Orphaned Functions | **31** Duplicates
- `src/selector/state.mjs` -> **0** Orphaned Functions | **29** Duplicates
- `src/extensions/renderer/base/load-listeners.mjs` -> **0** Orphaned Functions | **24** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`rollup.config.mjs`** -> AI Confidence: **99.31%**
2. **`src/extensions/renderer/base/index.mjs`** -> AI Confidence: **99.31%**
3. **`.github/workflows/scripts/pre_release_test.sh`** -> AI Confidence: **99.29%**
4. **`src/cjs.mjs`** -> AI Confidence: **99.29%**
5. **`src/selector/tokens.mjs`** -> AI Confidence: **99.29%**
6. **`src/util/regex.mjs`** -> AI Confidence: **99.29%**
7. **`src/collection/index.mjs`** -> AI Confidence: **99.24%**
8. **`documentation/docmaker.mjs`** -> AI Confidence: **99.23%**
9. **`src/extension.mjs`** -> AI Confidence: **99.23%**
10. **`src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs`** -> AI Confidence: **99.22%**
11. **`src/index.mjs`** -> AI Confidence: **99.18%**
12. **`src/util/index.mjs`** -> AI Confidence: **99.18%**
13. **`.github/workflows/scripts/merge_unstable_to_master.sh`** -> AI Confidence: **99.17%**
14. **`src/extensions/renderer/canvas/webgl/fxaa-upscaler.mjs`** -> AI Confidence: **99.17%**
15. **`src/core/index.mjs`** -> AI Confidence: **99.16%**
16. **`src/extensions/renderer/canvas/index.mjs`** -> AI Confidence: **99.16%**
17. **`src/style/index.mjs`** -> AI Confidence: **99.16%**
18. **`src/define/data.mjs`** -> AI Confidence: **99.13%**
19. **`src/extensions/renderer/base/coord-ele-math/edge-control-points.mjs`** -> AI Confidence: **99.13%**
20. **`src/selector/index.mjs`** -> AI Confidence: **99.13%**
21. **`.github/workflows/scripts/new-patch-version.sh`** -> AI Confidence: **99.11%**
22. **`playwright.config.js`** -> AI Confidence: **99.09%**
23. **`src/collection/algorithms/index.mjs`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `153` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/promise.mjs` (JAVASCRIPT) -> Cumulative Risk: **664.62**
- **Archetype:** `file_cluster_4` (Distance: 14.216 IQR)
- **Magnitude:** 247.38 | **LOC:** 212 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9987%), Concurrency (99.9959%)
- **Heaviest Functions:** `resolve` (Impact: 30.2), `all` (Impact: 13.7), `execute_handlers` (Impact: 11.1)

### 2. `src/style/apply.mjs` (JAVASCRIPT) -> Cumulative Risk: **656.94**
- **Archetype:** `file_cluster_17` (Distance: 15.347 IQR)
- **Magnitude:** 599.98 | **LOC:** 850 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.7842%), Cognitive Load (95.9985%)
- **Heaviest Functions:** `applyContextStyle` (Impact: 88.1), `cleanNum` (Impact: 34.9), `getPropertiesDiff` (Impact: 33.7)

### 3. `src/extensions/layout/grid.mjs` (JAVASCRIPT) -> Cumulative Risk: **640.06**
- **Archetype:** `file_cluster_11` (Distance: 14.385 IQR)
- **Magnitude:** 297.28 | **LOC:** 248 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9763%), Safety Score (97.3366%)
- **Heaviest Functions:** `run` (Impact: 85.8), `getPos` (Impact: 11.8), `small` (Impact: 10.6)

### 4. `documentation/demos/fcose-gene/code.js` (JAVASCRIPT) -> Cumulative Risk: **627.63**
- **Archetype:** `file_cluster_8` (Distance: 10.645 IQR)
- **Magnitude:** 117.14 | **LOC:** 248 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9719%), State Flux (99.964%), Concurrency (81.4266%)
- **Heaviest Functions:** `makeLayout` (Impact: 9.4), `makeSlider` (Impact: 8.3), `hideAllTippies` (Impact: 5.9)

### 5. `src/style/string-sheet.mjs` (JAVASCRIPT) -> Cumulative Risk: **617.79**
- **Archetype:** `file_cluster_8` (Distance: 12.018 IQR)
- **Magnitude:** 184.14 | **LOC:** 137 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (92.6096%)
- **Heaviest Functions:** `appendFromString` (Impact: 72.0), `removeSelAndBlockFromRemaining` (Impact: 16.6), `removeSelAndBlockFromRemaining` (Impact: 5.6)

### 6. `src/collection/dimensions/width-height.mjs` (JAVASCRIPT) -> Cumulative Risk: **617.48**
- **Archetype:** `file_cluster_8` (Distance: 12.26 IQR)
- **Magnitude:** 173.62 | **LOC:** 131 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.5596%), Safety Score (90.915%)
- **Heaviest Functions:** `defineDimFns` (Impact: 42.3), `dimImpl` (Impact: 18.8), `outerDimImpl` (Impact: 15.3)

### 7. `src/extensions/renderer/base/load-listeners.mjs` (JAVASCRIPT) -> Cumulative Risk: **617.09**
- **Archetype:** `file_cluster_11` (Distance: 13.405 IQR)
- **Magnitude:** 1711.08 | **LOC:** 2203 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8358%), Cognitive Load (97.0572%)
- **Heaviest Functions:** `allowPanningPassthrough` (Impact: 381.1), `load` (Impact: 330.4), `mouseupHandler` (Impact: 201.3)

### 8. `src/collection/dimensions/bounds.mjs` (JAVASCRIPT) -> Cumulative Risk: **615.24**
- **Archetype:** `file_cluster_8` (Distance: 13.291 IQR)
- **Magnitude:** 1425.76 | **LOC:** 1045 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9495%), Cognitive Load (93.6109%)
- **Heaviest Functions:** `boundingBoxImpl` (Impact: 138.3), `updateCompoundBounds` (Impact: 93.1), `updateBoundsFromLabel` (Impact: 88.8)

### 9. `src/collection/algorithms/dijkstra.mjs` (JAVASCRIPT) -> Cumulative Risk: **613.8**
- **Archetype:** `file_cluster_17` (Distance: 14.519 IQR)
- **Magnitude:** 239.6 | **LOC:** 134 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2347%), Tech Debt (95.2574%)
- **Heaviest Functions:** `dijkstra` (Impact: 41.9), `weight` (Impact: 37.4), `distBetween` (Impact: 9.7)

### 10. `documentation/demos/radius-types/code.js` (JAVASCRIPT) -> Cumulative Risk: **609.74**
- **Archetype:** `file_cluster_4` (Distance: 12.472 IQR)
- **Magnitude:** 128.12 | **LOC:** 95 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.5111%)
- **Heaviest Functions:** `setTimeout` (Impact: 14.7), `drawTrace` (Impact: 14.4), `setTimeout` (Impact: 14.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/math.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.982 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.751 IQR)
- **Top Global Matches:** file_cluster_8: 12.982, file_cluster_11: 13.064, file_cluster_17: 13.158
- **Magnitude:** 1741.92 | **LOC:** 1479 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.8257%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `median` (Impact: 452.3)
  * `inBezierVicinity` (Impact: 241.3)
  * `roundRectangleIntersectLine` (Impact: 73.0)
  * `finiteLinesIntersect` (Impact: 53.8)
    * *Intent:* // Find minimum distance by using the minimum of the distance // function between the given point an...
  * `polygonIntersectLine` (Impact: 36.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 366`, `args: 77`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 440`, `dead_code: 2`
* *Architecture:* `api: 92`
* *Defense:* `safety: 23`, `immutability_locks: 89`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/load-listeners.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.405 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.487 IQR)
- **Top Global Matches:** file_cluster_11: 13.405, file_cluster_8: 13.515, file_cluster_13: 13.529
- **Magnitude:** 1711.08 | **LOC:** 2203 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.0572%), Tech Debt (99.8358%)
**Top Internal Functions/Classes:**
  * `allowPanningPassthrough` (Impact: 381.1)
  * `load` (Impact: 330.4)
  * `mouseupHandler` (Impact: 201.3)
  * `mousemoveHandler` (Impact: 183.2)
    * *Intent:* // auto resize
  * `mousedownHandler` (Impact: 59.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 165`, `args: 27`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 356`, `dead_code: 6`, `duplicate_logic: 24`
* *Architecture:* `api: 7`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 22`, `test: 37`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/dimensions/bounds.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.291 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.665 IQR)
- **Top Global Matches:** file_cluster_8: 13.291, file_cluster_17: 13.415, file_cluster_11: 13.466
- **Magnitude:** 1425.76 | **LOC:** 1045 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.6109%), Tech Debt (99.9495%)
**Top Internal Functions/Classes:**
  * `boundingBoxImpl` (Impact: 138.3)
  * `updateCompoundBounds` (Impact: 93.1)
  * `updateBoundsFromLabel` (Impact: 88.8)
  * `update` (Impact: 84.1)
  * `isDisplayed` (Impact: 78.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 244`, `args: 33`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 518`, `dead_code: 2`, `duplicate_logic: 31`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 34`, `test: 16`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, is.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/layout/cose.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.945 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.885 IQR)
- **Top Global Matches:** file_cluster_11: 14.945, file_cluster_17: 14.958, file_cluster_0: 15.071
- **Magnitude:** 1087.98 | **LOC:** 1341 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.3455%), Tech Debt (92.4828%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 195.4)
    * *Intent:* // Exclude any edge that has a source or target node that is not in the set of passed-in nodes
  * `nodeRepulsion` (Impact: 164.4)
    * *Intent:* /** * @brief : This function finds the index of the lowest common * graph ancestor between 2 nodes i...
  * `findClippingPoint` (Impact: 42.1)
  * `separateComponents` (Impact: 26.3)
  * `propagateForces` (Impact: 22.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 192`, `args: 32`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 476`, `dead_code: 9`, `duplicate_logic: 10`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 24`, `doc: 15`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, is.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/coord-ele-math/edge-control-points.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.173 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.717 IQR)
- **Top Global Matches:** file_cluster_8: 13.173, file_cluster_11: 13.312, file_cluster_13: 13.317
- **Magnitude:** 951.56 | **LOC:** 1058 | **CtrlFlow:** 50.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.8268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `findTaxiPoints` (Impact: 95.3)
  * `findEdgeControlPoints` (Impact: 81.3)
  * `getKey` (Impact: 67.8)
  * `storeAllpts` (Impact: 47.2)
  * `tryToCorrectInvalidPoints` (Impact: 34.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 167`, `args: 21`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 427`, `dead_code: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 40`, `test: 1`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` map.mjs, math.mjs, index.mjs, is.mjs, round.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/traversing.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.984 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.631 IQR)
- **Top Global Matches:** file_cluster_17: 13.984, file_cluster_11: 14.271, file_cluster_13: 14.377
- **Magnitude:** 704.7 | **LOC:** 425 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.6144%), Tech Debt (73.1059%)
**Top Internal Functions/Classes:**
  * `defineEdgesWithFunction` (Impact: 42.1)
  * `edgesWithImpl` (Impact: 41.9)
  * `dagExtremityImpl` (Impact: 30.8)
  * `defineDagExtremity` (Impact: 27.8)
    * *Intent:* // DAG functions ////////////////
  * `defineParallelEdgesFunction` (Impact: 24.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 129`, `args: 26`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 384`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 12`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, cache-traversal-call.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.568 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.857 IQR)
- **Top Global Matches:** file_cluster_8: 12.568, file_cluster_13: 12.632, file_cluster_17: 12.701
- **Magnitude:** 674.88 | **LOC:** 1154 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.4251%), Tech Debt (10.3673%)
**Top Internal Functions/Classes:**
  * `_createShaderProgram` (Impact: 116.5)
    * *Intent:* /** * @param { string } collectionName
  * `drawNode` (Impact: 36.1)
  * `drawEdgeArrow` (Impact: 26.9)
  * `drawEdgeLine` (Impact: 23.6)
  * `drawTexture` (Impact: 21.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 64`, `args: 34`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 320`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 12`, `doc: 24`, `immutability_locks: 92`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` atlas.mjs, shader-sdf.mjs, math.mjs, index.mjs, webgl-util.mjs, gl-matrix
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/filter.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.711 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.443 IQR)
- **Top Global Matches:** file_cluster_17: 13.711, file_cluster_8: 13.875, file_cluster_11: 13.916
- **Magnitude:** 648.44 | **LOC:** 394 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.9179%), Tech Debt (79.5807%)
**Top Internal Functions/Classes:**
  * `filter` (Impact: 96.3)
  * `merge` (Impact: 13.6)
  * `not` (Impact: 13.2)
  * `intersect` (Impact: 13.2)
  * `diff` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 123`, `args: 23`, `func_start: 25`
* *Risk/State:* `state_mutation: 385`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 2`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, is.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/node-shapes.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.306 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.684 IQR)
- **Top Global Matches:** file_cluster_8: 12.306, file_cluster_11: 12.599, file_cluster_13: 12.639
- **Magnitude:** 615.64 | **LOC:** 659 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.3016%), Tech Debt (99.9715%)
**Top Internal Functions/Classes:**
  * `checkPoint` (Impact: 51.5)
  * `generateBarrel` (Impact: 30.0)
  * `checkPoint` (Impact: 27.1)
  * `checkPoint` (Impact: 23.6)
  * `checkPoint` (Impact: 21.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 136`, `args: 37`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 253`, `dead_code: 2`, `duplicate_logic: 21`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 9`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math.mjs, round.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/drawing-redraw.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.17 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.673 IQR)
- **Top Global Matches:** file_cluster_11: 14.17, file_cluster_17: 14.277, file_cluster_0: 14.301
- **Magnitude:** 614.88 | **LOC:** 722 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.555%), Tech Debt (72.9284%)
**Top Internal Functions/Classes:**
  * `createGradientStyleFor` (Impact: 84.5)
  * `render` (Impact: 62.5)
  * `drawSelectionRectangle` (Impact: 32.3)
  * `matchCanvasSize` (Impact: 19.1)
    * *Intent:* // Resize canvas
  * `getPixelRatio` (Impact: 13.6)
    * *Intent:* // var isFirefox = typeof InstallTrigger !== 'undefined';
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 101`, `args: 17`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 295`, `dead_code: 7`, `duplicate_logic: 6`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 22`, `test: 11`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/style/apply.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.347 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.843 IQR)
- **Top Global Matches:** file_cluster_17: 15.347, file_cluster_4: 15.42, file_cluster_11: 15.432
- **Magnitude:** 599.98 | **LOC:** 850 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.9985%), Tech Debt (94.4723%)
**Top Internal Functions/Classes:**
  * `applyContextStyle` (Impact: 88.1)
  * `cleanNum` (Impact: 34.9)
    * *Intent:* // save cycles when the context prop doesn't need to be applied
  * `getPropertiesDiff` (Impact: 33.7)
  * `apply` (Impact: 15.7)
    * *Intent:* // (potentially expensive calculation) // apply the style to the element based on // - its bypass //...
  * `getContextStyle` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 130`, `args: 27`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 310`, `dead_code: 11`, `duplicate_logic: 8`
* *Architecture:* `api: 4`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 14`, `test: 2`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, index.mjs, promise.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/drawing-edges.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.408 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.418 IQR)
- **Top Global Matches:** file_cluster_11: 13.408, file_cluster_17: 13.498, file_cluster_0: 13.55
- **Magnitude:** 543.8 | **LOC:** 432 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.7461%), Tech Debt (65.347%)
**Top Internal Functions/Classes:**
  * `drawEdgePath` (Impact: 84.9)
  * `drawArrowShape` (Impact: 73.0)
  * `drawEdge` (Impact: 59.7)
  * `drawArrowhead` (Impact: 41.8)
  * `drawEdgeOverlayUnderlay` (Impact: 15.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 90`, `args: 14`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 206`, `dead_code: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 11`, `api: 2`, `import: 2`
* *Defense:* `safety: 19`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` round.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/viewport.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.309 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.408 IQR)
- **Top Global Matches:** file_cluster_8: 13.309, file_cluster_11: 13.513, file_cluster_13: 13.576
- **Magnitude:** 543.08 | **LOC:** 610 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.7636%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `viewport` (Impact: 40.6)
  * `getFitViewport` (Impact: 37.8)
  * `pan` (Impact: 29.8)
  * `panBy` (Impact: 28.4)
  * `zoom` (Impact: 15.2)
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

### `documentation/docmaker.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.839 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.441 IQR)
- **Top Global Matches:** file_cluster_17: 13.839, file_cluster_13: 13.962, file_cluster_11: 13.966
- **Magnitude:** 457.98 | **LOC:** 458 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.5885%), Tech Debt (99.5369%)
**Top Internal Functions/Classes:**
  * `compileConfig` (Impact: 84.0)
  * `md2html` (Impact: 20.1)
    * *Intent:* // let html = converter.makeHtml("**I am bold!**"); // let html = Handlebars.compile();
  * `sortSoftwareVersions` (Impact: 16.7)
  * `parseSubsections` (Impact: 14.6)
  * `processFields` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 96`, `args: 22`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 212`, `dead_code: 5`, `duplicate_logic: 10`
* *Architecture:* `io: 19`, `import: 7`
* *Defense:* `safety: 12`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jsonlint, handlebars, marked, process, highlight.js, path, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/style.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.889 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.967 IQR)
- **Top Global Matches:** file_cluster_17: 13.889, file_cluster_11: 13.951, file_cluster_13: 14.108
- **Magnitude:** 436.02 | **LOC:** 458 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.0293%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `defineDerivedStateFunction` (Impact: 35.0)
  * `updateStyle` (Impact: 17.8)
    * *Intent:* // fully updates (recalculates) the style for the elements
  * `parsedStyle` (Impact: 15.2)
    * *Intent:* // get the internal parsed style object for the specified property
  * `effectiveOpacity` (Impact: 11.2)
  * `checkCompound` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 117`, `args: 31`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 248`, `dead_code: 2`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 16`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/algorithms/affinity-propagation.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.643 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.349 IQR)
- **Top Global Matches:** file_cluster_17: 13.643, file_cluster_13: 13.656, file_cluster_11: 13.693
- **Magnitude:** 432.24 | **LOC:** 330 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.4374%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `affinityPropagation` (Impact: 80.8)
  * `getPreference` (Impact: 16.4)
  * `assign` (Impact: 15.7)
  * `assignClusters` (Impact: 13.3)
  * `setOptions` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 103`, `args: 14`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 267`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 11`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` clustering-distances.mjs, index.mjs, is.mjs, math.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/define/animation.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.609 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.015 IQR)
- **Top Global Matches:** file_cluster_13: 13.609, file_cluster_8: 13.693, file_cluster_11: 13.701
- **Magnitude:** 417.28 | **LOC:** 240 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.2548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `animationImpl` (Impact: 58.4)
  * `animation` (Impact: 48.6)
  * `stopImpl` (Impact: 17.5)
  * `animateImpl` (Impact: 16.8)
  * `stop` (Impact: 14.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 78`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 178`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 8`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` animation.mjs, math.mjs, index.mjs, is.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/algorithms/bellman-ford.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.915 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.44 IQR)
- **Top Global Matches:** file_cluster_8: 12.915, file_cluster_13: 12.934, file_cluster_17: 13.046
- **Magnitude:** 366.82 | **LOC:** 203 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.7519%), Tech Debt (94.2568%)
**Top Internal Functions/Classes:**
  * `bellmanFord` (Impact: 83.2)
    * *Intent:* // Implemented from pseudocode from wikipedia
  * `weight` (Impact: 73.8)
  * `warn` (Impact: 21.6)
  * `pathTo` (Impact: 13.3)
  * `checkForEdgeReplacement` (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 63`, `args: 9`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 152`, `duplicate_logic: 3`
* *Architecture:* `io: 5`, `api: 2`, `import: 3`
* *Defense:* `safety: 3`, `test: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, is.mjs, map.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/emitter.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.011 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.756 IQR)
- **Top Global Matches:** file_cluster_11: 14.011, file_cluster_17: 14.162, file_cluster_13: 14.164
- **Magnitude:** 362.92 | **LOC:** 241 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.4202%), Tech Debt (99.9237%)
**Top Internal Functions/Classes:**
  * `forEachEvent` (Impact: 38.4)
  * `trigger` (Impact: 33.1)
  * `off` (Impact: 28.1)
  * `forEachEventObj` (Impact: 26.6)
  * `forEachEventObj` (Impact: 21.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 51`, `args: 21`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 140`, `dead_code: 2`, `duplicate_logic: 7`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 13`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` event.mjs, is.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/define/data.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.807 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.524 IQR)
- **Top Global Matches:** file_cluster_11: 13.807, file_cluster_13: 13.81, file_cluster_17: 13.975
- **Magnitude:** 354.28 | **LOC:** 209 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.2596%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `data` (Impact: 82.6)
    * *Intent:* // access data field
  * `dataImpl` (Impact: 71.4)
  * `removeDataImpl` (Impact: 36.1)
  * `removeData` (Impact: 33.1)
    * *Intent:* // remove data field
  * `set` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 53`, `args: 8`, `func_start: 9`
* *Risk/State:* `state_mutation: 114`, `dead_code: 2`
* *Architecture:* `io: 5`, `api: 4`, `import: 5`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` get.js, toPath.js, set.js, is.mjs, index.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/dimensions/position.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.817 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.918 IQR)
- **Top Global Matches:** file_cluster_11: 13.817, file_cluster_13: 13.875, file_cluster_17: 13.973
- **Magnitude:** 353.14 | **LOC:** 273 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.939%), Tech Debt (91.2033%)
**Top Internal Functions/Classes:**
  * `relativePosition` (Impact: 44.6)
    * *Intent:* // get/set the position relative to the parent
  * `shift` (Impact: 32.4)
  * `renderedPosition` (Impact: 29.5)
    * *Intent:* // get/set the rendered (i.e. on screen) positon of the element
  * `positions` (Impact: 18.9)
  * `beforePositionSet` (Impact: 17.0)
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

### `src/extensions/renderer/base/coord-ele-math/labels.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.185 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.911 IQR)
- **Top Global Matches:** file_cluster_11: 13.185, file_cluster_13: 13.2, file_cluster_8: 13.228
- **Magnitude:** 345.7 | **LOC:** 566 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.222%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `recalculateEdgeLabelProjections` (Impact: 62.5)
  * `recalculateNodeLabelProjection` (Impact: 30.5)
  * `calculateEndProjection` (Impact: 19.6)
  * `getLabelJustification` (Impact: 13.8)
  * `createControlPointInfo` (Impact: 13.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 84`, `args: 11`, `func_start: 19`
* *Risk/State:* `state_mutation: 162`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.mjs, math.mjs, is.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/index.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.094 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.759 IQR)
- **Top Global Matches:** file_cluster_13: 12.094, file_cluster_8: 12.231, file_cluster_11: 12.438
- **Magnitude:** 330.82 | **LOC:** 391 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.8054%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CanvasRenderer` (Impact: 77.8)
    * *Intent:* //
  * `getLabelRotationOffset` (Impact: 29.0)
  * `redrawHint` (Impact: 18.2)
  * `getImgSmoothing` (Impact: 10.3)
  * `path2dEnabled` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 120`, `args: 37`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 127`
* *Architecture:* `api: 9`, `import: 16`
* *Defense:* `safety: 7`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` drawing-elements.mjs, is.mjs, drawing-label-text.mjs, drawing-shapes.mjs, drawing-images.mjs, drawing-nodes.mjs, math.mjs, arrow-shapes.mjs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/index.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.954 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.235 IQR)
- **Top Global Matches:** file_cluster_13: 12.954, file_cluster_8: 13.294, file_cluster_11: 13.361
- **Magnitude:** 322.52 | **LOC:** 839 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.9592%), Tech Debt (48.3413%)
**Top Internal Functions/Classes:**
  * `move` (Impact: 41.4)
  * `Collection` (Impact: 38.0)
    * *Intent:* // represents a set of nodes, edges, or both together
  * `toString` (Impact: 22.3)
  * `restore` (Impact: 19.0)
  * `checkSwitch` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 87`, `args: 11`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 172`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 21`
* *Defense:* `safety: 9`, `test: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` switch-functions.mjs, style.mjs, events.mjs, traversing.mjs, index.mjs, is.mjs, filter.mjs, class.mjs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/collection/algorithms/k-clustering.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.485 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.791 IQR)
- **Top Global Matches:** file_cluster_11: 13.485, file_cluster_13: 13.53, file_cluster_8: 13.574
- **Magnitude:** 313.7 | **LOC:** 469 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.0388%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fuzzyCMeans` (Impact: 25.6)
  * `assign` (Impact: 14.8)
    * *Intent:* // If we've already chosen this node to be a medoid, don't choose it again (for small data sets).
  * `setOptions` (Impact: 9.7)
  * `randomCentroids` (Impact: 9.2)
  * `haveMatricesConverged` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 84`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 194`, `dead_code: 1`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 4`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` clustering-distances.mjs, index.mjs
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
- `src/define/data.mjs` (JAVASCRIPT) | Magnitude: 354.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 146, state_mutation: 114, structural_boundaries: 53, branch: 52
- `src/extensions/layout/cose.mjs` (JAVASCRIPT) | Magnitude: 1087.98 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 476, indent_spaces: 467, structural_boundaries: 192, branch: 112
- `src/collection/class.mjs` (JAVASCRIPT) | Magnitude: 182.2 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 101, indent_spaces: 99, structural_boundaries: 41, branch: 31
- `src/extensions/renderer/base/coord-ele-math/labels.mjs` (JAVASCRIPT) | Magnitude: 345.7 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 201, state_mutation: 162, structural_boundaries: 84, branch: 50
- `src/extensions/layout/concentric.mjs` (JAVASCRIPT) | Magnitude: 221.26 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 166, indent_spaces: 134, structural_boundaries: 62, branch: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/core/animation/step.mjs` (JAVASCRIPT) | Magnitude: 194.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 87, branch: 44, structural_boundaries: 41
- `src/selector/data.mjs` (JAVASCRIPT) | Magnitude: 40.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 18, state_mutation: 18, branch: 7
- `src/extensions/renderer/base/coord-ele-math/edge-projection.mjs` (JAVASCRIPT) | Magnitude: 87.56 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 39, structural_boundaries: 16, branch: 12
- `src/extensions/layout/random.mjs` (JAVASCRIPT) | Magnitude: 35.58 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 20, structural_boundaries: 13, args: 5
- `src/collection/algorithms/floyd-warshall.mjs` (JAVASCRIPT) | Magnitude: 222.42 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 107, indent_spaces: 89, structural_boundaries: 54, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/collection/algorithms/affinity-propagation.mjs` (JAVASCRIPT) | Magnitude: 432.24 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 267, indent_spaces: 224, structural_boundaries: 103, branch: 64
- `src/collection/algorithms/hierholzer.mjs` (JAVASCRIPT) | Magnitude: 234.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 110, branch: 51, structural_boundaries: 38
- `src/extensions/layout/breadthfirst.mjs` (JAVASCRIPT) | Magnitude: 251.24 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, state_mutation: 62, immutability_locks: 59, branch: 48
- `src/collection/style.mjs` (JAVASCRIPT) | Magnitude: 436.02 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 248, indent_spaces: 241, structural_boundaries: 117, branch: 83
- `src/event.mjs` (JAVASCRIPT) | Magnitude: 151.36 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 100, indent_spaces: 64, branch: 19, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `index.d.ts` (TYPESCRIPT) | Magnitude: 92.12 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1372, doc: 791, branch: 356, args: 327

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/extensions/renderer/canvas/export-image.mjs` (JAVASCRIPT) | Magnitude: 187.7 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, state_mutation: 80, structural_boundaries: 40, branch: 26
- `src/extensions/renderer/base/redraw.mjs` (JAVASCRIPT) | Magnitude: 26.72 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, branch: 6, state_mutation: 6, structural_boundaries: 5
- `documentation/demos/tokyo-railways/tokyo-railways.js` (JAVASCRIPT) | Magnitude: 74.24 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 45, concurrency: 24, state_mutation: 20, structural_boundaries: 16
- `documentation/demos/edge-types/code.js` (JAVASCRIPT) | Magnitude: 30.22 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 16, structural_boundaries: 15, concurrency: 12
- `documentation/demos/edge-arrows/index.html` (HTML) | Magnitude: 19.32 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, io: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/extensions/renderer/canvas/ele-texture-cache-lookup.mjs` (JAVASCRIPT) | Magnitude: 188.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 122, indent_spaces: 122, structural_boundaries: 44, args: 22
- `src/collection/group.mjs` (JAVASCRIPT) | Magnitude: 40.82 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 18, structural_boundaries: 8, args: 5
- `benchmark/a-star.js` (JAVASCRIPT) | Magnitude: 7.9 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 5, state_mutation: 4, args: 2
- `src/collection/algorithms/bellman-ford.mjs` (JAVASCRIPT) | Magnitude: 366.82 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 152, indent_spaces: 143, structural_boundaries: 63, branch: 37
- `benchmark/add.js` (JAVASCRIPT) | Magnitude: 24.76 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 18, structural_boundaries: 6, globals: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` -> Churn: **66.36%** | Cog Load: 72.4251% | Debt: 10.3673%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` -> **Mike Kucera** (100.0% isolated ownership) | Magnitude: 674.88
- `documentation/docmaker.mjs` -> **Max Franz** (100.0% isolated ownership) | Magnitude: 457.98
- `src/collection/index.mjs` -> **Felix Pahl** (100.0% isolated ownership) | Magnitude: 322.52
- `src/extensions/renderer/canvas/webgl/webgl-util.mjs` -> **Mike Kucera** (100.0% isolated ownership) | Magnitude: 139.02

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `benchmark/collection-creation.js` -> **Severity: 0.155** (Embedded: 0.0018 * Error Risk: 84.3762%)
- `src/test.mjs` -> **Severity: 0.14** (Embedded: 0.0018 * Error Risk: 76.2542%)
- `documentation/demos/tokyo-railways/tokyo-railways.js` -> **Severity: 0.114** (Embedded: 0.0018 * Error Risk: 61.9149%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `benchmark/collection-creation.js` -> **Severity: 257.786** (Blast Radius: 3.38 * Doc Risk: 76.2681%)
- `src/extensions/renderer/canvas/webgl/webgl-util.mjs` -> **Severity: 182.7** (Blast Radius: 1.827 * Doc Risk: 100.0%)
- `src/is.mjs` -> **Severity: 182.697** (Blast Radius: 1.827 * Doc Risk: 99.9983%)
- `src/util/index.mjs` -> **Severity: 182.664** (Blast Radius: 1.827 * Doc Risk: 99.9804%)
- `src/util/hash.mjs` -> **Severity: 181.834** (Blast Radius: 1.827 * Doc Risk: 99.526%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
