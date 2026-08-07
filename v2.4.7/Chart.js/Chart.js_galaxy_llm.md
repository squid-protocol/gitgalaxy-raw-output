# ARCHITECTURAL_BRIEF: Chart.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/Chart.js` |
| **Timestamp** | `2026-08-07T04:20:58.967002+00:00` |
| **Scan Duration** | `0.77s` |
| **Git Branch** | `master` |
| **Git Commit** | `a153556861074e827358446ec937555ac58c3d11` |
| **Git Remote** | `https://github.com/chartjs/Chart.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 108 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.088`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 58 | 47.2% |
| file_cluster_13 | 47 | 38.2% |
| file_cluster_16 | 6 | 4.9% |
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
| Cognitive Load Exposure | 0.0 | 95.7 | 22.6 | 17.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 47.4 | 55.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 31.7 | 2.6 | 80.0 |
| API Exposure | 0.0 | 19.6 | 7.0 | 6.8 | 0.0 |
| Concurrency Exposure | 0.0 | 89.5 | 2.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 47.9 | 32.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.2 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.5 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 96.3 | 2.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.3 | 19.8 | 11.9 |
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

- `itemsEqual` (@ `src/plugins/plugin.legend.js`) -> Impact: **149.6** | LOC: 498
- `drawPointLegend` (@ `src/helpers/helpers.canvas.ts`) -> Impact: **124.7** | LOC: 142
- `computeFlexCategoryTraits` (@ `src/controllers/controller.bar.js`) -> Impact: **90.7** | LOC: 204
- `getMinMax` (@ `src/core/core.datasetController.js`) -> Impact: **85.3** | LOC: 252
  * *Intent:* /** * Parse array of objects * @param {object} meta - dataset meta * @param {array} data - data array. Example [{x:1, y:5}, {x:2, y:10}] * @param {num...
- `strokePathDirect` (@ `src/elements/element.line.js`) -> Impact: **53.3** | LOC: 166
- `updateElements` (@ `src/controllers/controller.line.js`) -> Impact: **49.2** | LOC: 45
- `drawBorder` (@ `src/elements/element.arc.ts`) -> Impact: **47.5** | LOC: 50
- `elasticOut` (@ `src/helpers/helpers.easing.ts`) -> Impact: **45.6** | LOC: 112
- `_draw` (@ `src/plugins/plugin.legend.js`) -> Impact: **43.2** | LOC: 156
- `updateElements` (@ `src/controllers/controller.scatter.js`) -> Impact: **42.3** | LOC: 41

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/core` | 21 | 2804.18 | 27.39% | 30.96% |
| `src/scales` | 8 | 1504.46 | 35.88% | 22.99% |
| `src/plugins` | 7 | 1430.08 | 34.24% | 18.69% |
| `src/controllers` | 9 | 1410.7 | 32.31% | 9.5% |
| `src/elements` | 5 | 590.98 | 24.86% | 72.62% |
| `src/plugins/plugin.filler` | 8 | 578.94 | 32.38% | 35.72% |
| `src/helpers` | 18 | 457.63 | 19.53% | 35.63% |
| `src/platform` | 4 | 116.38 | 6.13% | 0.0% |
| `__monolith__` | 9 | 93.24 | 3.84% | 13.23% |
| `scripts` | 5 | 80.97 | 45.09% | 58.16% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/plugins/plugin.filler/filler.drawing.js` -> **100.0%** Exposure
- `src/helpers/helpers.color.ts` -> **100.0%** Exposure
- `src/helpers/helpers.rtl.ts` -> **100.0%** Exposure
- `scripts/docs-config.sh` -> **100.0%** Exposure
- `scripts/publish.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/controllers/controller.bar.js` -> **100.0%** Exposure
- `src/controllers/controller.bubble.js` -> **100.0%** Exposure
- `src/controllers/controller.doughnut.js` -> **100.0%** Exposure
- `src/controllers/controller.line.js` -> **100.0%** Exposure
- `src/controllers/controller.scatter.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/types/index.d.ts` -> **17** Orphaned Functions | **0** Duplicates
- `src/helpers/helpers.config.ts` -> **0** Orphaned Functions | **16** Duplicates
- `src/elements/element.line.js` -> **0** Orphaned Functions | **13** Duplicates
- `src/plugins/plugin.filler/filler.drawing.js` -> **0** Orphaned Functions | **12** Duplicates
- `src/scales/scale.radialLinear.js` -> **0** Orphaned Functions | **10** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `33` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/helpers/helpers.extras.ts` (TYPESCRIPT) -> Cumulative Risk: **648.05**
- **Archetype:** `file_cluster_13` (Distance: 11.525 IQR)
- **Magnitude:** 13.18 | **LOC:** 164 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.4309%), Concurrency (89.5496%), Tech Debt (88.5488%)
- **Heaviest Functions:** `_getStartAndCountOfVisiblePoints` (Impact: 24.4), `_scaleRangesChanged` (Impact: 9.7), `_textX` (Impact: 9.1)

### 2. `src/core/core.animations.js` (JAVASCRIPT) -> Cumulative Risk: **606.13**
- **Archetype:** `file_cluster_13` (Distance: 12.192 IQR)
- **Magnitude:** 134.3 | **LOC:** 163 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9989%), Tech Debt (88.9273%), Concurrency (88.3095%)
- **Heaviest Functions:** `_createAnimations` (Impact: 28.1), `configure` (Impact: 12.6), `resolveTargetOptions` (Impact: 7.7)

### 3. `src/core/core.animation.js` (JAVASCRIPT) -> Cumulative Risk: **598.26**
- **Archetype:** `file_cluster_13` (Distance: 13.687 IQR)
- **Magnitude:** 197.64 | **LOC:** 120 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0033%), Concurrency (89.036%)
- **Heaviest Functions:** `color` (Impact: 12.3), `constructor` (Impact: 12.1), `tick` (Impact: 11.3)

### 4. `src/elements/element.point.ts` (TYPESCRIPT) -> Cumulative Risk: **591.08**
- **Archetype:** `file_cluster_13` (Distance: 12.18 IQR)
- **Magnitude:** 10.93 | **LOC:** 108 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.7023%), Safety Score (91.7738%)
- **Heaviest Functions:** `size` (Impact: 20.5), `draw` (Impact: 7.5), `inRange` (Impact: 4.8)

### 5. `src/scales/scale.logarithmic.js` (JAVASCRIPT) -> Cumulative Risk: **542.68**
- **Archetype:** `file_cluster_13` (Distance: 14.146 IQR)
- **Magnitude:** 250.54 | **LOC:** 227 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.7502%), Tech Debt (90.808%)
- **Heaviest Functions:** `handleTickRangeOptions` (Impact: 12.7), `determineDataLimits` (Impact: 12.2), `setMax` (Impact: 9.2)

### 6. `src/scales/scale.radialLinear.js` (JAVASCRIPT) -> Cumulative Risk: **540.26**
- **Archetype:** `file_cluster_8` (Distance: 12.64 IQR)
- **Magnitude:** 529.5 | **LOC:** 685 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (93.0862%), Safety Score (84.9967%)
- **Heaviest Functions:** `drawGrid` (Impact: 19.6), `drawRadiusLine` (Impact: 18.2), `updateLimits` (Impact: 18.1)

### 7. `src/core/core.datasetController.js` (JAVASCRIPT) -> Cumulative Risk: **527.45**
- **Archetype:** `file_cluster_8` (Distance: 14.019 IQR)
- **Magnitude:** 884.56 | **LOC:** 1078 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (93.0525%), Safety Score (87.8632%)
- **Heaviest Functions:** `getMinMax` (Impact: 85.3), `parse` (Impact: 29.7), `clearStacks` (Impact: 18.3)

### 8. `src/elements/element.line.js` (JAVASCRIPT) -> Cumulative Risk: **518.99**
- **Archetype:** `file_cluster_13` (Distance: 13.48 IQR)
- **Magnitude:** 407.42 | **LOC:** 446 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9903%), Safety Score (82.5264%)
- **Heaviest Functions:** `strokePathDirect` (Impact: 53.3), `fastPathSegment` (Impact: 32.1), `pathSegment` (Impact: 26.1)

### 9. `src/plugins/plugin.legend.js` (JAVASCRIPT) -> Cumulative Risk: **516.53**
- **Archetype:** `file_cluster_8` (Distance: 13.635 IQR)
- **Magnitude:** 851.6 | **LOC:** 721 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.2142%), Verification (80.0%)
- **Heaviest Functions:** `itemsEqual` (Impact: 149.6), `_draw` (Impact: 43.2), `drawLegendBox` (Impact: 25.1)

### 10. `src/helpers/helpers.math.ts` (TYPESCRIPT) -> Cumulative Risk: **514.46**
- **Archetype:** `file_cluster_13` (Distance: 12.504 IQR)
- **Magnitude:** 13.79 | **LOC:** 208 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.6704%), Verification (80.0%)
- **Heaviest Functions:** `_angleBetween` (Impact: 16.2), `niceNum` (Impact: 10.4), `_factorize` (Impact: 8.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/core/core.datasetController.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.019 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.466 IQR)
- **Top Global Matches:** file_cluster_8: 14.019, file_cluster_13: 14.019, file_cluster_11: 14.083
- **Magnitude:** 884.56 | **LOC:** 1078 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5086%), Tech Debt (93.0525%)
**Top Internal Functions/Classes:**
  * `getMinMax` (Impact: 85.3)
    * *Intent:* /** * Parse array of objects * @param {object} meta - dataset meta * @param {array} data - data arra...
  * `parse` (Impact: 29.7)
    * *Intent:* // Re-sync meta data in case the user replaced the data array or if we missed
  * `clearStacks` (Impact: 18.3)
  * `getLastIndexInStack` (Impact: 13.9)
  * `_resolveAnimations` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 74`, `args: 69`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `state_mutation: 378`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 36`, `doc: 58`, `immutability_locks: 128`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.animations.js, index.js, core.scale.js, core.controller.js, helpers.core.js, core.defaults.js, helpers.collection.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.legend.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.635 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.186 IQR)
- **Top Global Matches:** file_cluster_8: 13.635, file_cluster_13: 13.657, file_cluster_17: 13.664
- **Magnitude:** 851.6 | **LOC:** 721 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.4167%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `itemsEqual` (Impact: 149.6)
  * `_draw` (Impact: 43.2)
  * `drawLegendBox` (Impact: 25.1)
  * `overrideTextDirection` (Impact: 20.6)
  * `handleEvent` (Impact: 15.4)
    * *Intent:* // See if we are touching one of the dataset boxes
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 73`, `args: 44`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 389`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 23`, `doc: 13`, `immutability_locks: 81`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, index.js, helpers.options.js, core.defaults.js, core.layouts.js, core.element.js, helpers.canvas.js, helpers.extras.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.radialLinear.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.64 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.252 IQR)
- **Top Global Matches:** file_cluster_8: 12.64, file_cluster_13: 12.757, file_cluster_17: 12.905
- **Magnitude:** 529.5 | **LOC:** 685 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7805%), Tech Debt (93.0862%)
**Top Internal Functions/Classes:**
  * `drawGrid` (Impact: 19.6)
  * `drawRadiusLine` (Impact: 18.2)
  * `updateLimits` (Impact: 18.1)
  * `determineLimits` (Impact: 15.6)
  * `yForAngle` (Impact: 12.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 59`, `args: 42`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 232`, `dead_code: 1`, `duplicate_logic: 10`
* *Architecture:* `api: 13`, `import: 7`
* *Defense:* `safety: 14`, `doc: 17`, `immutability_locks: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.options.js, core.defaults.js, helpers.canvas.js, core.ticks.js, scale.linearbase.js, helpers.math.js, helpers.core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.scale.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.349 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.858 IQR)
- **Top Global Matches:** file_cluster_13: 14.349, file_cluster_8: 14.531, file_cluster_7: 14.61
- **Magnitude:** 461.04 | **LOC:** 1713 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.4751%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `titleArgs` (Impact: 28.6)
  * `_computeLabelSizes` (Impact: 26.3)
  * `getPixelForGridLine` (Impact: 19.3)
  * `getMinMax` (Impact: 15.5)
  * `titleAlign` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 58`, `args: 33`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 243`, `dead_code: 1`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 16`, `doc: 106`, `immutability_locks: 37`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, types.js, helpers.options.js, core.element.js, helpers.canvas.js, core.scale.autoskip.js, helpers.core.js, helpers.math.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/elements/element.line.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.48 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.362 IQR)
- **Top Global Matches:** file_cluster_13: 13.48, file_cluster_8: 13.565, file_cluster_7: 13.7
- **Magnitude:** 407.42 | **LOC:** 446 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.7416%), Tech Debt (99.9903%)
**Top Internal Functions/Classes:**
  * `strokePathDirect` (Impact: 53.3)
  * `fastPathSegment` (Impact: 32.1)
  * `pathSegment` (Impact: 26.1)
  * `draw` (Impact: 14.3)
    * *Intent:* /** * Interpolate a point in this line at the same value on `property` as * the reference `point` pr...
  * `_getSegmentMethod` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 40`, `args: 25`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 142`, `duplicate_logic: 13`
* *Architecture:* `io: 8`, `api: 7`, `import: 6`
* *Defense:* `safety: 12`, `doc: 66`, `immutability_locks: 48`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.interpolation.js, index.js, element.point.js, helpers.curve.js, helpers.canvas.js, core.element.js, helpers.segment.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.doughnut.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.875 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.29 IQR)
- **Top Global Matches:** file_cluster_8: 12.875, file_cluster_13: 13.015, file_cluster_7: 13.192
- **Magnitude:** 355.72 | **LOC:** 400 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.4047%), Tech Debt (35.2067%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 22.1)
  * `getMaxBorderWidth` (Impact: 15.6)
  * `_indexable` (Impact: 14.5)
  * `_circumference` (Impact: 10.8)
  * `parse` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 53`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 187`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 8`, `doc: 16`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.datasetController.js, core.controller.js, helpers.core.js, helpers.math.js, helpers.intl.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.tooltip.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.235 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.535 IQR)
- **Top Global Matches:** file_cluster_8: 13.235, file_cluster_13: 13.237, file_cluster_7: 13.487
- **Magnitude:** 347.62 | **LOC:** 1351 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2129%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drawBackground` (Impact: 19.9)
  * `handleEvent` (Impact: 19.7)
  * `draw` (Impact: 15.3)
  * `_updateAnimationTarget` (Impact: 12.6)
  * `_getActiveElements` (Impact: 12.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 33`, `args: 21`, `func_start: 23`
* *Risk/State:* `state_mutation: 186`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `safety: 17`, `doc: 29`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, helpers.options.js, core.interaction.js, helpers.canvas.js, core.element.js, core.animations.js, helpers.core.js, helpers.math.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.bar.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.336 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.598 IQR)
- **Top Global Matches:** file_cluster_8: 13.336, file_cluster_13: 13.376, file_cluster_17: 13.436
- **Magnitude:** 339.08 | **LOC:** 683 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5221%), Tech Debt (50.2854%)
**Top Internal Functions/Classes:**
  * `computeFlexCategoryTraits` (Impact: 90.7)
  * `_calculateBarValuePixels` (Impact: 26.1)
  * `_calculateBarIndexPixels` (Impact: 13.7)
  * `computeMinSampleSize` (Impact: 13.6)
    * *Intent:* /**
  * `updateMinAndPrev` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 33`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 133`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 15`, `doc: 12`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.datasetController.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/helpers/helpers.segment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.806 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.14 IQR)
- **Top Global Matches:** file_cluster_8: 12.806, file_cluster_13: 12.837, file_cluster_7: 13.017
- **Magnitude:** 291.32 | **LOC:** 365 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.551%), Tech Debt (42.3416%)
**Top Internal Functions/Classes:**
  * `_boundSegment` (Impact: 36.6)
  * `doSplitByStyles` (Impact: 27.4)
  * `findStartAndEnd` (Impact: 24.0)
  * `shouldStop` (Impact: 22.2)
  * `solidSegments` (Impact: 21.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 50`, `args: 20`, `func_start: 22`
* *Risk/State:* `state_mutation: 72`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 16`, `doc: 42`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.color.js, element.point.js, helpers.math.js, helpers.options.js, element.line.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.logarithmic.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.146 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.428 IQR)
- **Top Global Matches:** file_cluster_13: 14.146, file_cluster_11: 14.437, file_cluster_8: 14.472
- **Magnitude:** 250.54 | **LOC:** 227 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.1902%), Tech Debt (90.808%)
**Top Internal Functions/Classes:**
  * `handleTickRangeOptions` (Impact: 12.7)
    * *Intent:* // if data has `0` in it or `beginAtZero` is true, min (non zero) value is at bottom // of scale, an...
  * `determineDataLimits` (Impact: 12.2)
  * `setMax` (Impact: 9.2)
  * `getPixelForValue` (Impact: 9.0)
  * `parse` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 33`, `args: 17`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 154`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 11`, `doc: 16`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.scale.js, core.ticks.js, scale.linearbase.js, helpers.core.js, helpers.math.js, helpers.intl.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.time.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.848 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_13: 14.848, file_cluster_17: 15.079, file_cluster_11: 15.169
- **Magnitude:** 242.92 | **LOC:** 676 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.0694%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initOffsets` (Impact: 17.2)
  * `buildTicks` (Impact: 17.1)
  * `parse` (Impact: 9.6)
    * *Intent:* /** * @type {Unit[]} */
  * `getDataTimestamps` (Impact: 9.5)
  * `getLabelTimestamps` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 25`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 165`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 9`, `doc: 27`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.scale.js, helpers.core.js, helpers.math.js, core.adapters.js, helpers.collection.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.controller.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.089 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.772 IQR)
- **Top Global Matches:** file_cluster_13: 13.089, file_cluster_8: 13.52, file_cluster_17: 13.61
- **Magnitude:** 207.34 | **LOC:** 1270 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.4056%), Tech Debt (68.8564%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 31.2)
  * `getCanvas` (Impact: 14.6)
  * `moveNumericKeys` (Impact: 10.7)
  * `determineLastEvent` (Impact: 9.4)
  * `_getActiveElements` (Impact: 7.4)
    * *Intent:* // If aspectRatio is defined in options, use that.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 32`, `args: 17`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 90`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `import: 12`
* *Defense:* `safety: 10`, `doc: 18`, `immutability_locks: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, core.plugins.js, index.js, core.config.js, package.json, index.js, helpers.core.js, core.defaults.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.animation.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.687 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.844 IQR)
- **Top Global Matches:** file_cluster_13: 13.687, file_cluster_4: 13.7, file_cluster_8: 13.853
- **Magnitude:** 197.64 | **LOC:** 120 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.5215%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `color` (Impact: 12.3)
    * *Intent:* /**
  * `constructor` (Impact: 12.1)
  * `tick` (Impact: 11.3)
  * `_notify` (Impact: 6.0)
  * `update` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 15`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 121`
* *Architecture:* `api: 8`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 2`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.options.js, helpers.easing.js, helpers.color.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.scatter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.712 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.396 IQR)
- **Top Global Matches:** file_cluster_13: 12.712, file_cluster_8: 12.756, file_cluster_7: 13.063
- **Magnitude:** 193.72 | **LOC:** 180 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.8087%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 42.3)
  * `getMaxOverflow` (Impact: 12.5)
  * `update` (Impact: 10.7)
  * `getLabelAndValue` (Impact: 4.9)
  * `addElements` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 112`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 2`, `doc: 6`, `immutability_locks: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.math.js, helpers.extras.js, core.datasetController.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.category.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.125 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.191 IQR)
- **Top Global Matches:** file_cluster_13: 14.125, file_cluster_8: 14.145, file_cluster_11: 14.306
- **Magnitude:** 191.08 | **LOC:** 159 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.1344%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addIfString` (Impact: 9.4)
  * `buildTicks` (Impact: 9.4)
  * `parse` (Impact: 7.4)
  * `findOrAddLabel` (Impact: 7.1)
  * `determineDataLimits` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 27`, `args: 15`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 110`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 13`, `doc: 5`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.scale.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.plugins.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.234 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.636 IQR)
- **Top Global Matches:** file_cluster_13: 14.234, file_cluster_17: 14.252, file_cluster_8: 14.264
- **Magnitude:** 162.24 | **LOC:** 189 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.8035%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `notify` (Impact: 12.2)
    * *Intent:* /** * @typedef { import('./core.controller.js').default } Chart * @typedef { import('../types/index....
  * `_notify` (Impact: 11.8)
  * `allPlugins` (Impact: 9.7)
  * `_createDescriptors` (Impact: 9.0)
    * *Intent:* // When plugins are registered, there is the possibility of a double // invalidate situation. In thi...
  * `getOpts` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 22`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 92`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 10`, `doc: 23`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` plugin.tooltip.js, core.config.js, core.controller.js, helpers.core.js, core.registry.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/core.layouts.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.153 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_8: 11.153, file_cluster_17: 11.173, file_cluster_13: 11.409
- **Magnitude:** 154.08 | **LOC:** 456 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5602%), Tech Debt (99.779%)
**Top Internal Functions/Classes:**
  * `fitBoxes` (Impact: 30.5)
  * `updateDims` (Impact: 17.3)
  * `setLayoutDims` (Impact: 16.5)
  * `buildStacks` (Impact: 11.0)
  * `wrapBoxes` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 25`, `args: 22`, `func_start: 27`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`, `duplicate_logic: 7`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 7`, `doc: 3`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.core.js, helpers.options.js, core.controller.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.polarArea.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.587 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.982 IQR)
- **Top Global Matches:** file_cluster_8: 11.587, file_cluster_13: 11.896, file_cluster_7: 11.964
- **Magnitude:** 149.92 | **LOC:** 228 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.2858%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 20.2)
  * `getMinMax` (Impact: 8.1)
  * `_computeAngle` (Impact: 6.2)
  * `generateLabels` (Impact: 5.5)
  * `getLabelAndValue` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 23`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 78`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 1`, `doc: 7`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.datasetController.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scales/scale.timeseries.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.378 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.697 IQR)
- **Top Global Matches:** file_cluster_13: 13.378, file_cluster_8: 13.388, file_cluster_7: 13.525
- **Magnitude:** 140.24 | **LOC:** 178 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.7448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `interpolate` (Impact: 17.1)
    * *Intent:* /**
  * `buildLookupTable` (Impact: 11.5)
  * `_getTimestampsForTable` (Impact: 10.9)
  * `_generate` (Impact: 7.7)
  * `constructor` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 23`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 79`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 2`, `doc: 28`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` scale.time.js, helpers.collection.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.line.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.2 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.398 IQR)
- **Top Global Matches:** file_cluster_13: 12.2, file_cluster_8: 12.239, file_cluster_7: 12.57
- **Magnitude:** 139.38 | **LOC:** 144 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.3601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 49.2)
  * `getMaxOverflow` (Impact: 7.7)
  * `update` (Impact: 5.9)
  * `initialize` (Impact: 1.7)
  * `draw` (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 68`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.math.js, helpers.extras.js, core.datasetController.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controllers/controller.bubble.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.397 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.355 IQR)
- **Top Global Matches:** file_cluster_8: 12.397, file_cluster_13: 12.491, file_cluster_7: 12.655
- **Magnitude:** 135.14 | **LOC:** 170 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2434%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateElements` (Impact: 23.7)
  * `parseObjectData` (Impact: 9.3)
    * *Intent:* /** * Parse array of arrays * @protected */
  * `resolveDataElementOptions` (Impact: 7.8)
  * `getLabelAndValue` (Impact: 6.4)
  * `parseArrayData` (Impact: 4.9)
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

### `src/core/core.animations.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.192 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.823 IQR)
- **Top Global Matches:** file_cluster_13: 12.192, file_cluster_4: 12.297, file_cluster_8: 12.306
- **Magnitude:** 134.3 | **LOC:** 163 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.5899%), Tech Debt (88.9273%)
**Top Internal Functions/Classes:**
  * `_createAnimations` (Impact: 28.1)
  * `configure` (Impact: 12.6)
  * `resolveTargetOptions` (Impact: 7.7)
  * `awaitAll` (Impact: 7.5)
  * `_animateOptions` (Impact: 6.2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 25`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 7`, `import: 4`
* *Defense:* `safety: 4`, `doc: 6`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.animator.js, helpers.core.js, core.defaults.js, core.animation.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.filler/filler.drawing.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.288 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_8: 10.288, file_cluster_13: 10.738, file_cluster_7: 11.001
- **Magnitude:** 131.16 | **LOC:** 188 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fill` (Impact: 17.5)
  * `clipBounds` (Impact: 17.3)
  * `clipVertical` (Impact: 13.4)
  * `clipHorizontal` (Impact: 13.4)
  * `doFill` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 11`, `args: 7`, `func_start: 20`
* *Risk/State:* `state_mutation: 22`, `duplicate_logic: 12`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 7`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` filler.target.js, filler.segment.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/elements/element.bar.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.351 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.256 IQR)
- **Top Global Matches:** file_cluster_8: 11.351, file_cluster_13: 11.505, file_cluster_7: 11.676
- **Magnitude:** 129.8 | **LOC:** 227 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.3757%), Tech Debt (67.5966%)
**Top Internal Functions/Classes:**
  * `parseBorderRadius` (Impact: 20.9)
  * `inRange` (Impact: 18.4)
  * `hasRadius` (Impact: 7.1)
  * `draw` (Impact: 6.8)
  * `getBarBounds` (Impact: 6.2)
    * *Intent:* /** @typedef {{ x: number, y: number, base: number, horizontal: boolean, width: number, height: numb...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 22`, `args: 16`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 9`, `doc: 17`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.options.js, helpers.canvas.js, core.element.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.title.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.153 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.782 IQR)
- **Top Global Matches:** file_cluster_13: 12.153, file_cluster_8: 12.181, file_cluster_7: 12.584
- **Magnitude:** 128.78 | **LOC:** 167 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.4563%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 9.9)
  * `_drawArgs` (Impact: 8.3)
  * `draw` (Impact: 3.9)
  * `isHorizontal` (Impact: 3.0)
  * `constructor` (Impact: 2.3)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 17`, `args: 9`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 81`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.074
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, core.layouts.js, helpers.canvas.js, core.element.js, helpers.extras.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/helpers/helpers.collection.ts` (TYPESCRIPT) | Magnitude: 10.08 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 73, state_mutation: 33, structural_boundaries: 29, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/scales/scale.timeseries.js` (JAVASCRIPT) | Magnitude: 140.24 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 79, doc: 28, branch: 24
- `src/core/core.animation.js` (JAVASCRIPT) | Magnitude: 197.64 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 121, indent_spaces: 89, branch: 23, immutability_locks: 18
- `src/core/core.interaction.js` (JAVASCRIPT) | Magnitude: 102.46 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, doc: 47, immutability_locks: 31, branch: 29
- `src/core/core.plugins.js` (JAVASCRIPT) | Magnitude: 162.24 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 105, state_mutation: 92, branch: 28, immutability_locks: 25
- `src/scales/scale.category.js` (JAVASCRIPT) | Magnitude: 191.08 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 110, indent_spaces: 108, branch: 28, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/helpers/helpers.core.ts` (TYPESCRIPT) | Magnitude: 8.69 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 51, indent_spaces: 39, doc: 25, api: 24
- `src/helpers/helpers.options.ts` (TYPESCRIPT) | Magnitude: 9.51 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 42, branch: 41, doc: 35
- `src/types/index.d.ts` (TYPESCRIPT) | Magnitude: 22.92 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 655, structural_boundaries: 350, doc: 294, generics: 184
- `src/core/core.adapters.ts` (TYPESCRIPT) | Magnitude: 3.03 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, doc: 27, structural_boundaries: 21, args: 20
- `src/types/basic.d.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.68 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, generics: 2, safety: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/core/core.datasetController.js` (JAVASCRIPT) | Magnitude: 884.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 591, state_mutation: 378, branch: 142, immutability_locks: 128
- `src/plugins/plugin.tooltip.js` (JAVASCRIPT) | Magnitude: 347.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 319, state_mutation: 186, branch: 57, immutability_locks: 41
- `src/core/core.defaults.js` (JAVASCRIPT) | Magnitude: 85.54 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 30, state_mutation: 30, args: 18
- `src/platform/platform.base.js` (JAVASCRIPT) | Magnitude: 30.98 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 29, indent_spaces: 22, api: 9, args: 8
- `src/core/core.layouts.js` (JAVASCRIPT) | Magnitude: 154.08 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 180, immutability_locks: 41, branch: 37, func_start: 27

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/core/core.scale.js` -> **asmenezes** (100.0% isolated ownership) | Magnitude: 461.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/core/index.ts` -> **Severity: 807.4** (Blast Radius: 8.074 * Doc Risk: 100.0%)
- `src/helpers/index.ts` -> **Severity: 807.4** (Blast Radius: 8.074 * Doc Risk: 100.0%)
- `src/types/geometric.d.ts` -> **Severity: 807.4** (Blast Radius: 8.074 * Doc Risk: 100.0%)
- `src/helpers/helpers.math.ts` -> **Severity: 804.739** (Blast Radius: 8.074 * Doc Risk: 99.6704%)
- `src/index.ts` -> **Severity: 804.481** (Blast Radius: 8.074 * Doc Risk: 99.6385%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
