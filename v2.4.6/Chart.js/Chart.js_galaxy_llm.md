# ARCHITECTURAL_BRIEF: Chart.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/Chart.js` |
| **Timestamp** | `2026-08-03T20:00:18.170543+00:00` |
| **Scan Duration** | `0.85s` |
| **Git Branch** | `master` |
| **Git Commit** | `a153556861074e827358446ec937555ac58c3d11` |
| **Git Remote** | `https://github.com/chartjs/Chart.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 108 malicious artifacts.

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
| Total Artifacts | 1750 |
| Analyzed Artifacts (Scanned) | 123 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1627 |
| Total LOC | 11223 |
| Volatility Index | 0.016 |
| % Scanned of codebase = | 7.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 64 | 7409 | 52.0% |
| TYPESCRIPT | 40 | 3645 | 32.5% |
| PLAINTEXT | 8 | 0 | 6.5% |
| SHELL | 4 | 80 | 3.3% |
| MARKDOWN | 3 | 0 | 2.4% |
| JSON | 2 | 62 | 1.6% |
| YAML | 1 | 3 | 0.8% |
| HTML | 1 | 24 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.037`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 58 | 47.2% |
| file_cluster_13 | 46 | 37.4% |
| file_cluster_16 | 6 | 4.9% |
| file_cluster_4 | 1 | 0.8% |
| file_cluster_11 | 1 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 8.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1627*

**Composition by Extension & Reason:**
- `.png`: 679x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 588x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 140x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.styl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.drawio`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 17244 LOC)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 95.7 | 22.8 | 17.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 29.5 | 14.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 32.4 | 2.6 | 80.0 |
| API Exposure | 0.0 | 19.6 | 6.8 | 6.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 48.0 | 32.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.2 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.5 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 96.3 | 2.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.9 | 21.8 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 23.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/types/autogen.js` (Hits: 10)
- `src/elements/element.line.js` (Hits: 8)
- `scripts/sample-redirect-template.html` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **App.tsx** (`test/integration/react-browser/src/App.tsx`) — 1 inbound connections
2. **AppAuto.tsx** (`test/integration/react-browser/src/AppAuto.tsx`) — 1 inbound connections
3. **LICENSE.md** (`LICENSE.md`) — 0 inbound connections
4. **MAINTAINING.md** (`MAINTAINING.md`) — 0 inbound connections
5. **README.md** (`README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.umd.ts** (`src/index.umd.ts`) — 18 outbound dependencies
2. **index.ts** (`src/helpers/index.ts`) — 16 outbound dependencies
3. **index.ts** (`src/core/index.ts`) — 14 outbound dependencies
4. **core.controller.js** (`src/core/core.controller.js`) — 13 outbound dependencies
5. **index.d.ts** (`src/types/index.d.ts`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `itemsEqual` (@ `src/plugins/plugin.legend.js`) -> Impact: **523.7** | LOC: 498
- `computeFlexCategoryTraits` (@ `src/controllers/controller.bar.js`) -> Impact: **251.7** | LOC: 204
- `drawPointLegend` (@ `src/helpers/helpers.canvas.ts`) -> Impact: **183.5** | LOC: 142
- `elasticOut` (@ `src/helpers/helpers.easing.ts`) -> Impact: **125.6** | LOC: 112
- `getMinMax` (@ `src/core/core.datasetController.js`) -> Impact: **121.7** | LOC: 252
  * *Intent:* /** * Parse array of objects * @param {object} meta - dataset meta * @param {array} data - data array. Example [{x:1, y:5}, {x:2, y:10}] * @param {num...
- `fitBoxes` (@ `src/core/core.layouts.js`) -> Impact: **79.7** | LOC: 119
- `updateElements` (@ `src/controllers/controller.line.js`) -> Impact: **72.7** | LOC: 45
- `binarySearch` (@ `src/core/core.interaction.js`) -> Impact: **69.2** | LOC: 43
  * *Intent:* /** * @typedef { import('./core.controller.js').default } Chart * @typedef { import('../types/index.js').ChartEvent } ChartEvent
- `updateElements` (@ `src/controllers/controller.scatter.js`) -> Impact: **62.4** | LOC: 41
- `parse` (@ `src/core/core.datasetController.js`) -> Impact: **57.4** | LOC: 39
  * *Intent:* // Re-sync meta data in case the user replaced the data array or if we missed

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `itemsEqual` (@ `src/plugins/plugin.legend.js`) -> **O(2^N) [Recursive]**
- `computeFlexCategoryTraits` (@ `src/controllers/controller.bar.js`) -> **O(2^N) [Recursive]**
- `index` (@ `src/core/core.interaction.js`) -> **O(2^N) [Recursive]**
- `fitBoxes` (@ `src/core/core.layouts.js`) -> **O(2^N) [Recursive]**
- `getMinMax` (@ `src/core/core.scale.js`) -> **O(2^N) [Recursive]**
- `fill` (@ `src/plugins/plugin.filler/filler.drawing.js`) -> **O(2^N) [Recursive]**
- `beforeDraw` (@ `src/plugins/plugin.filler/index.js`) -> **O(2^N) [Recursive]**
- `beforeDatasetsDraw` (@ `src/plugins/plugin.filler/index.js`) -> **O(2^N) [Recursive]**
- `init` (@ `src/scales/scale.category.js`) -> **O(2^N) [Recursive]**
- `generateTickLabels` (@ `src/scales/scale.radialLinear.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**

### Highest Data Gravity (Database Complexity)
- `itemsEqual` (@ `src/plugins/plugin.legend.js`) -> DB Complexity: **164**
- `getMinMax` (@ `src/core/core.datasetController.js`) -> DB Complexity: **63**
  * *Intent:* /** * Parse array of objects * @param {object} meta - dataset meta * @param {array} data - data array. Example [{x:1, y:5}, {x:2, y:10}] * @param {num...
- `computeFlexCategoryTraits` (@ `src/controllers/controller.bar.js`) -> DB Complexity: **43**
- `constructor` (@ `src/core/core.controller.js`) -> DB Complexity: **41**
- `constructor` (@ `src/core/core.scale.js`) -> DB Complexity: **41**
- `constructor` (@ `src/core/core.defaults.js`) -> DB Complexity: **27**
  * *Intent:* /**
- `strokePathWithCache` (@ `src/elements/element.line.js`) -> DB Complexity: **22**
- `buildTicks` (@ `src/scales/scale.time.js`) -> DB Complexity: **22**
- `constructor` (@ `src/core/core.datasetController.js`) -> DB Complexity: **21**
  * *Intent:* /** * Element type used to generate a meta dataset (e.g. Chart.element.LineElement).
- `update` (@ `src/controllers/controller.doughnut.js`) -> DB Complexity: **20**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/core` | 21 | 2909.13 | 26.83% | 4.8% |
| `src/plugins` | 7 | 1664.26 | 31.68% | 0.0% |
| `src/controllers` | 9 | 1645.3 | 32.31% | 0.0% |
| `src/scales` | 8 | 1549.56 | 35.88% | 0.0% |
| `src/plugins/plugin.filler` | 8 | 670.44 | 32.64% | 10.8% |
| `src/elements` | 5 | 551.93 | 24.86% | 52.13% |
| `src/helpers` | 18 | 458.1 | 19.73% | 12.37% |
| `__monolith__` | 9 | 100.44 | 3.84% | 13.23% |
| `src/platform` | 4 | 99.98 | 6.13% | 0.0% |
| `scripts` | 5 | 81.54 | 53.06% | 58.16% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/helpers/helpers.color.ts` -> **100.0%** Exposure
- `scripts/docs-config.sh` -> **100.0%** Exposure
- `scripts/publish.sh` -> **100.0%** Exposure
- `src/helpers/helpers.collection.ts` -> **99.9992%** Exposure
- `src/types/animation.d.ts` -> **98.4733%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/controllers/controller.bar.js` -> **100.0%** Exposure
- `src/controllers/controller.bubble.js` -> **100.0%** Exposure
- `src/controllers/controller.doughnut.js` -> **100.0%** Exposure
- `src/controllers/controller.line.js` -> **100.0%** Exposure
- `src/controllers/controller.scatter.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/types/index.d.ts` -> **9** Orphaned Functions | **0** Duplicates
- `src/elements/element.line.js` -> **0** Orphaned Functions | **6** Duplicates
- `src/helpers/helpers.collection.ts` -> **0** Orphaned Functions | **3** Duplicates
- `rollup.config.js` -> **0** Orphaned Functions | **2** Duplicates
- `src/core/core.datasetController.js` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`karma.conf.cjs`** -> AI Confidence: **99.31%**
2. **`src/controllers/index.js`** -> AI Confidence: **99.31%**
3. **`src/core/core.controller.js`** -> AI Confidence: **99.31%**
4. **`src/core/core.datasetController.js`** -> AI Confidence: **99.31%**
5. **`src/core/core.interaction.js`** -> AI Confidence: **99.31%**
6. **`src/core/core.scale.js`** -> AI Confidence: **99.31%**
7. **`src/elements/element.line.js`** -> AI Confidence: **99.31%**
8. **`src/plugins/index.js`** -> AI Confidence: **99.31%**
9. **`src/plugins/plugin.legend.js`** -> AI Confidence: **99.31%**
10. **`src/plugins/plugin.tooltip.js`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/controllers/controller.doughnut.js` -> **100.0%** Exposure
- `src/controllers/controller.polarArea.js` -> **100.0%** Exposure
- `src/core/core.datasetController.js` -> **100.0%** Exposure
- `src/plugins/plugin.legend.js` -> **100.0%** Exposure
- `src/helpers/helpers.extras.ts` -> **65.953%** Exposure
### Algorithmic DoS Exposure
- `src/controllers/controller.doughnut.js` -> **100.0%** Exposure
- `src/controllers/controller.polarArea.js` -> **100.0%** Exposure
- `src/controllers/controller.scatter.js` -> **100.0%** Exposure
- `src/core/core.controller.js` -> **100.0%** Exposure
- `src/core/core.datasetController.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `33` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/helpers/helpers.extras.ts` (TYPESCRIPT) -> Cumulative Risk: **769.25**
- **Archetype:** `file_cluster_13` (Distance: 11.734 IQR)
- **Magnitude:** 13.08 | **LOC:** 164 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9996%), Concurrency (99.4007%)
- **Heaviest Functions:** `_getStartAndCountOfVisiblePoints` (Impact: 46.5), `_scaleRangesChanged` (Impact: 9.7), `_textX` (Impact: 9.1)

### 2. `src/plugins/plugin.legend.js` (JAVASCRIPT) -> Cumulative Risk: **663.98**
- **Archetype:** `file_cluster_8` (Distance: 13.703 IQR)
- **Magnitude:** 1027.9 | **LOC:** 721 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `itemsEqual` (Impact: 523.7), `generateLabels` (Impact: 18.4), `isListened` (Impact: 14.3)

### 3. `src/controllers/controller.polarArea.js` (JAVASCRIPT) -> Cumulative Risk: **626.13**
- **Archetype:** `file_cluster_8` (Distance: 11.587 IQR)
- **Magnitude:** 171.92 | **LOC:** 228 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9993%)
- **Heaviest Functions:** `updateElements` (Impact: 29.1), `generateLabels` (Impact: 11.9), `getMinMax` (Impact: 11.6)

### 4. `src/core/core.datasetController.js` (JAVASCRIPT) -> Cumulative Risk: **621.65**
- **Archetype:** `file_cluster_8` (Distance: 14.045 IQR)
- **Magnitude:** 830.16 | **LOC:** 1078 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getMinMax` (Impact: 121.7), `parse` (Impact: 57.4), `_dataCheck` (Impact: 18.4)

### 5. `src/core/core.animation.js` (JAVASCRIPT) -> Cumulative Risk: **606.43**
- **Archetype:** `file_cluster_13` (Distance: 13.687 IQR)
- **Magnitude:** 197.64 | **LOC:** 120 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.0873%), Concurrency (89.036%)
- **Heaviest Functions:** `color` (Impact: 12.3), `constructor` (Impact: 12.1), `tick` (Impact: 11.3)

### 6. `src/controllers/controller.doughnut.js` (JAVASCRIPT) -> Cumulative Risk: **605.39**
- **Archetype:** `file_cluster_8` (Distance: 12.863 IQR)
- **Magnitude:** 379.72 | **LOC:** 400 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_indexable` (Impact: 32.7), `updateElements` (Impact: 32.1), `getMaxBorderWidth` (Impact: 22.7)

### 7. `src/elements/element.point.ts` (TYPESCRIPT) -> Cumulative Risk: **595.19**
- **Archetype:** `file_cluster_13` (Distance: 12.229 IQR)
- **Magnitude:** 10.5 | **LOC:** 108 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.7023%), Safety Score (91.7738%)
- **Heaviest Functions:** `size` (Impact: 20.5), `draw` (Impact: 7.5), `inRange` (Impact: 4.8)

### 8. `scripts/utils.sh` (SHELL) -> Cumulative Risk: **589.65**
- **Archetype:** `file_cluster_8` (Distance: 11.324 IQR)
- **Magnitude:** 4.2 | **LOC:** 24 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9479%), Algorithmic Dos (99.8003%)
- **Heaviest Functions:** `tag_from_version` (Impact: 26.3), `__global_context__` (Impact: 1.3)

### 9. `src/core/core.animations.js` (JAVASCRIPT) -> Cumulative Risk: **576.49**
- **Archetype:** `file_cluster_4` (Distance: 12.257 IQR)
- **Magnitude:** 158.6 | **LOC:** 163 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9989%), State Flux (99.9989%), Algorithmic Dos (98.7738%)
- **Heaviest Functions:** `_createAnimations` (Impact: 41.1), `configure` (Impact: 18.2), `_animateOptions` (Impact: 8.8)

### 10. `src/plugins/plugin.filler/filler.segment.js` (JAVASCRIPT) -> Cumulative Risk: **572.48**
- **Archetype:** `file_cluster_8` (Distance: 11.053 IQR)
- **Magnitude:** 99.98 | **LOC:** 100 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9123%), State Flux (99.8542%), Documentation (97.3557%)
- **Heaviest Functions:** `_segments` (Impact: 26.4), `_getEdge` (Impact: 11.5), `_findSegmentEnd` (Impact: 10.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/plugins/plugin.legend.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.703 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.142 IQR)
- **Top Global Matches:** file_cluster_8: 13.703, file_cluster_13: 13.737, file_cluster_17: 13.739
- **Magnitude:** 1027.9 | **LOC:** 721 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 164
- **Risk Profile:** Cognitive Load (71.7508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `itemsEqual` (Impact: 523.7 | O(2^N) | DB: 164)
  * `generateLabels` (Impact: 18.4 | O(N^3))
  * `isListened` (Impact: 14.3 | O(N^1))
  * `onClick` (Impact: 9.6 | O(N^2))
    * *Intent:* // The labels need to be built after datasets are updated to ensure that colors // and other styling...
  * `calculateItemWidth` (Impact: 9.3 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 73`, `args: 44`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 403`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 23`, `doc: 13`, `immutability_locks: 81`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.layouts.js, index.js, helpers.options.js, helpers.canvas.js, core.defaults.js, helpers.extras.js, index.js, core.element.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.datasetController.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.045 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.508 IQR)
- **Top Global Matches:** file_cluster_8: 14.045, file_cluster_13: 14.07, file_cluster_11: 14.13
- **Magnitude:** 830.16 | **LOC:** 1078 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (37.5086%), Tech Debt (27.6935%)
**Top Internal Functions/Classes:**
  * `getMinMax` (Impact: 121.7 | O(N^2) | DB: 63)
    * *Intent:* /** * Parse array of objects * @param {object} meta - dataset meta * @param {array} data - data arra...
  * `parse` (Impact: 57.4 | O(N^3) | DB: 7)
    * *Intent:* // Re-sync meta data in case the user replaced the data array or if we missed
  * `_dataCheck` (Impact: 18.4 | O(N^2) | DB: 7)
  * `clearStacks` (Impact: 18.3 | O(N^1))
  * `getLastIndexInStack` (Impact: 13.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 74`, `args: 69`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `state_mutation: 390`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 36`, `doc: 58`, `immutability_locks: 128`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, core.animations.js, core.scale.js, helpers.core.js, helpers.collection.js, core.defaults.js, core.controller.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.radialLinear.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.654 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.014 IQR)
- **Top Global Matches:** file_cluster_8: 12.654, file_cluster_13: 12.783, file_cluster_17: 12.938
- **Magnitude:** 539.0 | **LOC:** 685 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (49.7805%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawGrid` (Impact: 28.1 | O(N^2) | DB: 16)
  * `drawRadiusLine` (Impact: 18.2 | O(N^1))
  * `updateLimits` (Impact: 18.1 | O(N^1) | DB: 2)
  * `buildPointLabelItems` (Impact: 16.3 | O(N^2) | DB: 3)
  * `determineLimits` (Impact: 15.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 59`, `args: 42`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 232`, `dead_code: 1`
* *Architecture:* `api: 13`, `import: 7`
* *Defense:* `safety: 14`, `doc: 17`, `immutability_locks: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.options.js, helpers.canvas.js, core.defaults.js, helpers.core.js, helpers.math.js, scale.linearbase.js, core.ticks.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.scale.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.36 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.859 IQR)
- **Top Global Matches:** file_cluster_13: 14.36, file_cluster_8: 14.539, file_cluster_7: 14.619
- **Magnitude:** 498.64 | **LOC:** 1713 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (35.4751%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getMinMax` (Impact: 43.8 | O(2^N) | DB: 5)
  * `_computeLabelSizes` (Impact: 38.3 | O(N^2) | DB: 13)
  * `titleArgs` (Impact: 28.6 | O(N^1) | DB: 2)
  * `getPixelForGridLine` (Impact: 19.3 | O(N^1) | DB: 2)
  * `titleAlign` (Impact: 10.4 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 58`, `args: 33`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 245`, `dead_code: 1`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `safety: 16`, `doc: 106`, `immutability_locks: 37`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.options.js, helpers.canvas.js, core.element.js, core.scale.autoskip.js, helpers.core.js, types.js, helpers.extras.js, index.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.bar.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.405 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.55 IQR)
- **Top Global Matches:** file_cluster_8: 13.405, file_cluster_13: 13.489, file_cluster_17: 13.521
- **Magnitude:** 420.28 | **LOC:** 683 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (37.5221%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `computeFlexCategoryTraits` (Impact: 251.7 | O(2^N) | DB: 43)
  * `computeMinSampleSize` (Impact: 13.6 | O(N^1) | DB: 2)
    * *Intent:* /**
  * `computeFitCategoryTraits` (Impact: 7.8 | O(N^1) | DB: 1)
  * `getAllScaleValues` (Impact: 5.8 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 33`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 137`, `dead_code: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 15`, `doc: 12`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, core.datasetController.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.tooltip.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.235 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.535 IQR)
- **Top Global Matches:** file_cluster_8: 13.235, file_cluster_13: 13.237, file_cluster_7: 13.487
- **Magnitude:** 388.42 | **LOC:** 1351 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (34.2129%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleEvent` (Impact: 28.7 | O(N^2) | DB: 9)
  * `drawBackground` (Impact: 19.9 | O(N^1) | DB: 4)
  * `_updateAnimationTarget` (Impact: 18.2 | O(N^2) | DB: 12)
  * `_getActiveElements` (Impact: 18.0 | O(N^2) | DB: 6)
  * `draw` (Impact: 15.3 | O(N^1) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 33`, `args: 21`, `func_start: 23`
* *Risk/State:* `state_mutation: 186`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `safety: 17`, `doc: 29`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, core.animations.js, helpers.options.js, helpers.rtl.js, helpers.canvas.js, core.interaction.js, platform.base.js, helpers.core.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.doughnut.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.863 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.254 IQR)
- **Top Global Matches:** file_cluster_8: 12.863, file_cluster_13: 13.02, file_cluster_7: 13.187
- **Magnitude:** 379.72 | **LOC:** 400 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (36.4047%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_indexable` (Impact: 32.7 | O(N^4))
  * `updateElements` (Impact: 32.1 | O(N^2) | DB: 13)
  * `getMaxBorderWidth` (Impact: 22.7 | O(N^2) | DB: 3)
  * `parse` (Impact: 14.0 | O(N^2) | DB: 6)
  * `calculateTotal` (Impact: 13.5 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 53`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 187`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* `safety: 8`, `doc: 16`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.core.js, helpers.intl.js, core.controller.js, helpers.math.js, core.datasetController.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/elements/element.line.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.484 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.143 IQR)
- **Top Global Matches:** file_cluster_13: 13.484, file_cluster_8: 13.545, file_cluster_7: 13.697
- **Magnitude:** 373.02 | **LOC:** 446 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (37.7416%), Tech Debt (95.3292%)
**Top Internal Functions/Classes:**
  * `fastPathSegment` (Impact: 46.7 | O(N^2) | DB: 5)
  * `draw` (Impact: 27.7 | O(2^N) | DB: 5)
    * *Intent:* /** * Interpolate a point in this line at the same value on `property` as * the reference `point` pr...
  * `pathSegment` (Impact: 26.1 | O(N^1) | DB: 7)
  * `interpolate` (Impact: 17.0 | O(N^2) | DB: 5)
  * `_getSegmentMethod` (Impact: 14.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 40`, `args: 25`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 142`, `duplicate_logic: 6`
* *Architecture:* `io: 8`, `api: 6`, `import: 6`
* *Defense:* `safety: 12`, `doc: 66`, `immutability_locks: 48`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` element.point.js, helpers.curve.js, index.js, helpers.canvas.js, helpers.interpolation.js, helpers.segment.js, core.element.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/helpers/helpers.segment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.814 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.247 IQR)
- **Top Global Matches:** file_cluster_8: 12.814, file_cluster_13: 12.851, file_cluster_7: 13.026
- **Magnitude:** 275.12 | **LOC:** 365 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (30.551%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doSplitByStyles` (Impact: 39.7 | O(N^2) | DB: 6)
  * `_boundSegment` (Impact: 36.6 | O(N^1) | DB: 6)
  * `solidSegments` (Impact: 31.7 | O(N^2) | DB: 5)
  * `findStartAndEnd` (Impact: 24.0 | O(N^1) | DB: 2)
  * `getSegment` (Impact: 19.4 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 50`, `args: 20`, `func_start: 22`
* *Risk/State:* `state_mutation: 72`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 16`, `doc: 42`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.options.js, helpers.math.js, element.line.js, element.point.js, helpers.color.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.time.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.848 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_13: 14.848, file_cluster_17: 15.079, file_cluster_11: 15.169
- **Magnitude:** 255.22 | **LOC:** 676 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (38.0694%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initOffsets` (Impact: 25.2 | O(N^2) | DB: 9)
  * `buildTicks` (Impact: 17.1 | O(N^1) | DB: 22)
  * `parse` (Impact: 13.9 | O(N^2) | DB: 2)
    * *Intent:* /** * @type {Unit[]} */
  * `getDataTimestamps` (Impact: 9.5 | O(N^1) | DB: 8)
  * `getLabelTimestamps` (Impact: 7.8 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 25`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 165`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 9`, `doc: 27`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.math.js, helpers.core.js, core.adapters.js, helpers.collection.js, core.scale.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.logarithmic.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.166 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.497 IQR)
- **Top Global Matches:** file_cluster_13: 14.166, file_cluster_11: 14.452, file_cluster_8: 14.482
- **Magnitude:** 246.14 | **LOC:** 227 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (38.1902%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleTickRangeOptions` (Impact: 18.4 | O(N^2) | DB: 7)
    * *Intent:* // if data has `0` in it or `beginAtZero` is true, min (non zero) value is at bottom // of scale, an...
  * `parse` (Impact: 14.3 | O(2^N) | DB: 1)
  * `determineDataLimits` (Impact: 12.2 | O(N^1) | DB: 14)
  * `getPixelForValue` (Impact: 9.0 | O(N^1) | DB: 5)
  * `buildTicks` (Impact: 7.0 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 33`, `args: 17`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 154`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 11`, `doc: 16`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.core.js, helpers.intl.js, scale.linearbase.js, helpers.math.js, core.scale.js, core.ticks.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.scatter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.712 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.396 IQR)
- **Top Global Matches:** file_cluster_13: 12.712, file_cluster_8: 12.756, file_cluster_7: 13.063
- **Magnitude:** 227.82 | **LOC:** 180 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (45.8087%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 62.4 | O(N^2) | DB: 14)
  * `getMaxOverflow` (Impact: 18.1 | O(N^2) | DB: 7)
  * `update` (Impact: 14.9 | O(N^2) | DB: 16)
  * `addElements` (Impact: 8.9 | O(2^N) | DB: 4)
  * `getLabelAndValue` (Impact: 4.9 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 112`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 2`, `doc: 6`, `immutability_locks: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.math.js, index.js, core.datasetController.js, helpers.extras.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.controller.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.106 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.862 IQR)
- **Top Global Matches:** file_cluster_13: 13.106, file_cluster_8: 13.529, file_cluster_17: 13.632
- **Magnitude:** 212.24 | **LOC:** 1270 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (35.4056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 44.2 | O(N^2) | DB: 41)
  * `moveNumericKeys` (Impact: 15.7 | O(N^2))
  * `getCanvas` (Impact: 14.6 | O(N^1))
  * `determineLastEvent` (Impact: 9.4 | O(N^1))
  * `positionIsHorizontal` (Impact: 7.1 | O(N^1))
    * *Intent:* /** * @typedef { import('../types/index.js').ChartEvent } ChartEvent * @typedef { import('../types/i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 32`, `args: 17`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 90`
* *Architecture:* `api: 9`, `import: 12`
* *Defense:* `safety: 10`, `doc: 18`, `immutability_locks: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, index.js, package.json, core.registry.js, helpers.core.js, core.animator.js, core.plugins.js, core.config.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.category.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.125 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.191 IQR)
- **Top Global Matches:** file_cluster_13: 14.125, file_cluster_8: 14.145, file_cluster_11: 14.306
- **Magnitude:** 208.08 | **LOC:** 159 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (49.1344%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 17.6 | O(2^N) | DB: 4)
  * `addIfString` (Impact: 9.4 | O(N^1) | DB: 2)
  * `buildTicks` (Impact: 9.4 | O(N^1) | DB: 10)
  * `determineDataLimits` (Impact: 9.3 | O(N^2) | DB: 7)
  * `parse` (Impact: 7.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 27`, `args: 15`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 110`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 13`, `doc: 5`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, core.scale.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.animation.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.687 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.844 IQR)
- **Top Global Matches:** file_cluster_13: 13.687, file_cluster_4: 13.7, file_cluster_8: 13.853
- **Magnitude:** 197.64 | **LOC:** 120 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (55.5215%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `color` (Impact: 12.3 | O(N^1))
    * *Intent:* /**
  * `constructor` (Impact: 12.1 | O(N^1) | DB: 12)
  * `tick` (Impact: 11.3 | O(N^1) | DB: 15)
  * `_notify` (Impact: 6.0 | O(N^1) | DB: 2)
  * `update` (Impact: 4.8 | O(N^1) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 15`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 121`
* *Architecture:* `api: 8`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 2`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.color.js, helpers.easing.js, helpers.options.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.layouts.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.177 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.199 IQR)
- **Top Global Matches:** file_cluster_8: 11.177, file_cluster_17: 11.227, file_cluster_13: 11.45
- **Magnitude:** 188.18 | **LOC:** 456 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (22.796%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fitBoxes` (Impact: 79.7 | O(2^N) | DB: 1)
  * `updateDims` (Impact: 17.3 | O(N^1))
  * `setLayoutDims` (Impact: 16.5 | O(N^1) | DB: 1)
  * `buildStacks` (Impact: 11.0 | O(N^1))
  * `wrapBoxes` (Impact: 7.9 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 25`, `args: 22`, `func_start: 27`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 7`, `doc: 3`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.core.js, helpers.options.js, core.controller.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.bubble.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.397 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.355 IQR)
- **Top Global Matches:** file_cluster_8: 12.397, file_cluster_13: 12.491, file_cluster_7: 12.655
- **Magnitude:** 172.64 | **LOC:** 170 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (37.2434%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 34.9 | O(N^2) | DB: 6)
  * `parseObjectData` (Impact: 18.3 | O(2^N) | DB: 2)
    * *Intent:* /** * Parse array of arrays * @protected */
  * `resolveDataElementOptions` (Impact: 14.8 | O(2^N) | DB: 2)
  * `parsePrimitiveData` (Impact: 9.3 | O(2^N) | DB: 2)
  * `parseArrayData` (Impact: 9.3 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 23`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 64`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 2`, `doc: 12`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.core.js, core.datasetController.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.polarArea.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.587 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.982 IQR)
- **Top Global Matches:** file_cluster_8: 11.587, file_cluster_13: 11.896, file_cluster_7: 11.964
- **Magnitude:** 171.92 | **LOC:** 228 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (43.2858%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 29.1 | O(N^2) | DB: 13)
  * `generateLabels` (Impact: 11.9 | O(N^4))
  * `getMinMax` (Impact: 11.6 | O(N^2) | DB: 3)
  * `countVisibleElements` (Impact: 7.0 | O(N^2) | DB: 4)
  * `_computeAngle` (Impact: 6.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 23`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 78`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 1`, `doc: 7`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, core.datasetController.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.plugins.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.234 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.636 IQR)
- **Top Global Matches:** file_cluster_13: 14.234, file_cluster_17: 14.252, file_cluster_8: 14.264
- **Magnitude:** 167.84 | **LOC:** 189 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (36.8035%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_notify` (Impact: 17.4 | O(N^2))
  * `notify` (Impact: 12.2 | O(N^1) | DB: 12)
    * *Intent:* /** * @typedef { import('./core.controller.js').default } Chart * @typedef { import('../types/index....
  * `allPlugins` (Impact: 9.7 | O(N^1) | DB: 4)
  * `_createDescriptors` (Impact: 9.0 | O(N^1))
    * *Intent:* // When plugins are registered, there is the possibility of a double // invalidate situation. In thi...
  * `getOpts` (Impact: 7.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 22`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 92`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 10`, `doc: 23`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` plugin.tooltip.js, core.registry.js, helpers.core.js, core.config.js, index.js, core.controller.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.line.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.2 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.398 IQR)
- **Top Global Matches:** file_cluster_13: 12.2, file_cluster_8: 12.239, file_cluster_7: 12.57
- **Magnitude:** 165.68 | **LOC:** 144 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (45.3601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 72.7 | O(N^2) | DB: 11)
  * `getMaxOverflow` (Impact: 7.7 | O(N^1) | DB: 3)
  * `update` (Impact: 5.9 | O(N^1) | DB: 12)
  * `initialize` (Impact: 3.1 | O(2^N) | DB: 2)
  * `draw` (Impact: 3.1 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 68`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.math.js, index.js, core.datasetController.js, helpers.extras.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.interaction.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.094 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.801 IQR)
- **Top Global Matches:** file_cluster_13: 12.094, file_cluster_8: 12.111, file_cluster_7: 12.267
- **Magnitude:** 158.86 | **LOC:** 388 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (14.0274%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `binarySearch` (Impact: 69.2 | O(N^3) | DB: 1)
    * *Intent:* /** * @typedef { import('./core.controller.js').default } Chart * @typedef { import('../types/index....
  * `index` (Impact: 34.6 | O(2^N))
  * `evaluateInteractionItems` (Impact: 15.4 | O(N^2) | DB: 2)
  * `getNearestItems` (Impact: 13.7 | O(N^1))
  * `getDistanceMetricForAxis` (Impact: 5.7 | O(N^1))
    * *Intent:* /** * Helper function to select candidate elements for interaction * @param {Chart} chart - the char...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 20`, `args: 11`, `func_start: 9`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 7`, `doc: 47`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, helpers.math.js, core.element.js, index.js, helpers.collection.js, helpers.dom.js, core.controller.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.animations.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.257 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.687 IQR)
- **Top Global Matches:** file_cluster_4: 12.257, file_cluster_13: 12.29, file_cluster_8: 12.393
- **Magnitude:** 158.6 | **LOC:** 163 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (53.7643%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_createAnimations` (Impact: 41.1 | O(N^2) | DB: 6)
  * `configure` (Impact: 18.2 | O(N^2) | DB: 2)
  * `_animateOptions` (Impact: 8.8 | O(N^2) | DB: 1)
    * *Intent:* /**
  * `resolveTargetOptions` (Impact: 7.7 | O(N^1) | DB: 1)
  * `awaitAll` (Impact: 7.5 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 25`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 2`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 4`, `doc: 6`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.animation.js, core.animator.js, core.defaults.js, helpers.core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.filler/filler.drawing.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.447 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.002 IQR)
- **Top Global Matches:** file_cluster_8: 10.447, file_cluster_13: 10.905, file_cluster_7: 11.15
- **Magnitude:** 147.26 | **LOC:** 188 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (28.9311%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fill` (Impact: 48.7 | O(2^N) | DB: 2)
  * `clipBounds` (Impact: 17.3 | O(N^1) | DB: 1)
  * `clipVertical` (Impact: 13.4 | O(N^1) | DB: 2)
  * `clipHorizontal` (Impact: 13.4 | O(N^1) | DB: 2)
  * `doFill` (Impact: 11.7 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 11`, `args: 7`, `func_start: 20`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 7`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` filler.target.js, filler.segment.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.timeseries.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.378 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.697 IQR)
- **Top Global Matches:** file_cluster_13: 13.378, file_cluster_8: 13.388, file_cluster_7: 13.525
- **Magnitude:** 146.64 | **LOC:** 178 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (36.7448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `interpolate` (Impact: 17.1 | O(N^1) | DB: 5)
    * *Intent:* /**
  * `buildLookupTable` (Impact: 16.5 | O(N^2) | DB: 3)
  * `_getTimestampsForTable` (Impact: 10.9 | O(N^1) | DB: 6)
  * `_generate` (Impact: 7.7 | O(N^1) | DB: 6)
  * `initOffsets` (Impact: 3.2 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 23`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 79`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 2`, `doc: 28`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.collection.js, scale.time.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.title.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.157 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.782 IQR)
- **Top Global Matches:** file_cluster_13: 12.157, file_cluster_8: 12.186, file_cluster_7: 12.589
- **Magnitude:** 130.88 | **LOC:** 167 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (48.2433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_drawArgs` (Impact: 11.8 | O(N^2) | DB: 3)
  * `update` (Impact: 9.9 | O(N^1) | DB: 16)
  * `draw` (Impact: 3.9 | O(N^1) | DB: 4)
  * `isHorizontal` (Impact: 3.0 | O(N^1) | DB: 1)
  * `constructor` (Impact: 2.3 | O(N^1) | DB: 13)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 17`, `args: 9`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 81`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.layouts.js, index.js, helpers.canvas.js, helpers.extras.js, core.element.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/helpers/helpers.collection.ts` (TYPESCRIPT) | Magnitude: 10.08 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 73, state_mutation: 33, structural_boundaries: 29, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/scales/scale.timeseries.js` (JAVASCRIPT) | Magnitude: 146.64 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 79, doc: 28, branch: 24
- `src/core/core.animation.js` (JAVASCRIPT) | Magnitude: 197.64 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 121, indent_spaces: 89, branch: 23, immutability_locks: 18
- `src/core/core.interaction.js` (JAVASCRIPT) | Magnitude: 158.86 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, doc: 47, immutability_locks: 31, branch: 29
- `src/core/core.plugins.js` (JAVASCRIPT) | Magnitude: 167.84 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 105, state_mutation: 92, branch: 28, immutability_locks: 25
- `src/scales/scale.category.js` (JAVASCRIPT) | Magnitude: 208.08 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 110, indent_spaces: 108, branch: 28, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/helpers/helpers.core.ts` (TYPESCRIPT) | Magnitude: 9.92 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 51, indent_spaces: 39, doc: 25, api: 24
- `src/helpers/helpers.options.ts` (TYPESCRIPT) | Magnitude: 10.28 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 42, branch: 41, doc: 35
- `src/types/index.d.ts` (TYPESCRIPT) | Magnitude: 21.54 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 655, structural_boundaries: 350, doc: 294, generics: 184
- `src/core/core.adapters.ts` (TYPESCRIPT) | Magnitude: 2.98 | Delta: **0.262 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, doc: 27, structural_boundaries: 21, func_start: 20
- `src/types/basic.d.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.68 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, generics: 2, safety: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/core/core.animations.js` (JAVASCRIPT) | Magnitude: 158.6 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, state_mutation: 51, branch: 32, structural_boundaries: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/plugins/plugin.tooltip.js` (JAVASCRIPT) | Magnitude: 388.42 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 319, state_mutation: 186, branch: 57, immutability_locks: 41
- `src/platform/platform.base.js` (JAVASCRIPT) | Magnitude: 30.98 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 29, indent_spaces: 22, api: 9, args: 8
- `src/core/core.datasetController.js` (JAVASCRIPT) | Magnitude: 830.16 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 591, state_mutation: 390, branch: 142, immutability_locks: 128
- `src/core/core.defaults.js` (JAVASCRIPT) | Magnitude: 84.64 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 30, state_mutation: 30, args: 18
- `src/plugins/plugin.legend.js` (JAVASCRIPT) | Magnitude: 1027.9 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 500, state_mutation: 403, branch: 94, immutability_locks: 81

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/core/core.scale.js` -> **asmenezes** (100.0% isolated ownership) | Magnitude: 498.64

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/core/index.ts` -> **Severity: 807.4** (Blast Radius: 8.074 * Doc Risk: 100.0%)
- `src/helpers/index.ts` -> **Severity: 807.4** (Blast Radius: 8.074 * Doc Risk: 100.0%)
- `src/types/geometric.d.ts` -> **Severity: 807.4** (Blast Radius: 8.074 * Doc Risk: 100.0%)
- `src/index.ts` -> **Severity: 807.397** (Blast Radius: 8.074 * Doc Risk: 99.9996%)
- `src/helpers/helpers.color.ts` -> **Severity: 807.385** (Blast Radius: 8.074 * Doc Risk: 99.9981%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
