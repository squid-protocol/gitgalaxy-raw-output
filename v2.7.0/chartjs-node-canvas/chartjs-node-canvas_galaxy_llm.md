# ARCHITECTURAL_BRIEF: chartjs-node-canvas
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 14 |
| Analyzed Artifacts (Scanned) | 13 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 358 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4132 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6133 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5091 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 9 | 358 | 69.2% |
| MARKDOWN | 3 | 0 | 23.1% |
| PLAINTEXT | 1 | 0 | 7.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9 | 69.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 30.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 72.8 | 13.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.1 | 48.3 | 59.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 11.0 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 38.3 | 20.9 | 25.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 32.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.6 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 8.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 66.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 50.0 | 69.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 13 | 4 | 3 | `package/src/chartJSNodeCanvas.ts` |
| cleanup | 7 | 2 | 2 | `package/src/chartJSNodeCanvas.ts` |
| guards | 51 | 4 | 7 | `package/src/chartJSNodeCanvasBase.ts` |
| danger | 37 | 4 | 10 | `package/src/animatedChartJSNodeCanvas.ts` |
| concurrency | 18 | 4 | 5 | `package/src/animatedChartJSNodeCanvas.ts` |
| connectivity | 31 | 7 | 6 | `package/src/chartJSNodeCanvasBase.ts` |
| io | 9 | 2 | 3 | `package/src/example.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1 | 1 | 0 | `package/src/animatedChartJSNodeCanvas.ts` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 19 | 3 | 5 | `package/src/chartJSNodeCanvasBase.ts` |
| debt | 2 | 1 | 0 | `package/src/example.ts` |
| mutation | 86 | 6 | 21 | `package/src/animatedChartJSNodeCanvas.ts` |
| dead_code | 2 | 1 | 0 | `package/src/freshImport.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 3 | 1 | 0 | `package/src/animatedChartJSNodeCanvas.ts` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/example.ts` (Hits: 6)
- `package/src/chartJSNodeCanvasBase.ts` (Hits: 3)
- `package/API.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **chartJSNodeCanvasBase.ts** (`package/src/chartJSNodeCanvasBase.ts`) — 3 inbound connections
2. **backgroundColourPlugin.ts** (`package/src/backgroundColourPlugin.ts`) — 2 inbound connections
3. **API.md** (`package/API.md`) — 1 inbound connections
4. **CHANGELOG.md** (`package/CHANGELOG.md`) — 1 inbound connections
5. **package.json** (`package/package.json`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`package/README.md`) — 9 outbound dependencies
2. **chartJSNodeCanvasBase.ts** (`package/src/chartJSNodeCanvasBase.ts`) — 6 outbound dependencies
3. **example.ts** (`package/src/example.ts`) — 5 outbound dependencies
4. **chartJSNodeCanvas.ts** (`package/src/chartJSNodeCanvas.ts`) — 3 outbound dependencies
5. **index.ts** (`package/src/index.ts`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `initialize` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **29.5** | LOC: 52
- `renderChart` (@ `package/src/animatedChartJSNodeCanvas.ts`) -> Impact: **22.1** | LOC: 41
- `renderToStream` (@ `package/src/chartJSNodeCanvas.ts`) -> Impact: **13.1** | LOC: 19
  * *Intent:* /** * Render to a stream. * @see https://github.com/Automattic/node-canvas#canvascreatepngstream * * @param configuration The Chart JS configuration f...
- `constructor` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **12.4** | LOC: 21
  * *Intent:* /** * Create a new instance of CanvasRenderService. * * @param options Configuration for this instance */
- `onComplete` (@ `package/src/animatedChartJSNodeCanvas.ts`) -> Impact: **8.1** | LOC: 20
- `renderToDataURL` (@ `package/src/chartJSNodeCanvas.ts`) -> Impact: **6.0** | LOC: 17
  * *Intent:* /** * Render to a data url. * @see https://github.com/Automattic/node-canvas#canvastodataurl * * @param configuration The Chart JS configuration for t...
- `renderToBuffer` (@ `package/src/chartJSNodeCanvas.ts`) -> Impact: **6.0** | LOC: 17
  * *Intent:* /** * Render to a buffer. * @see https://github.com/Automattic/node-canvas#canvastobuffer * * @param configuration The Chart JS configuration for the ...
- `toBuffer` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **6.0** | LOC: 1
  * *Intent:* // https://github.com/Automattic/node-canvas#non-standard-apis
- `registerFont` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **5.4** | LOC: 4
  * *Intent:* /** * Use to register the font with Canvas to use a font file that is not installed as a system font, this must be done before the Canvas is created. ...
- `toBuffer` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **5.2** | LOC: 1

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src` | 9 | 317.29 | 13.07% | 0.0% |
| `package` | 4 | 9.68 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/animatedChartJSNodeCanvas.ts` -> **99.9959%** Exposure
- `package/src/chartJSNodeCanvasBase.ts` -> **86.1853%** Exposure
- `package/src/chartJSNodeCanvas.ts` -> **85.0424%** Exposure
- `package/src/example.ts` -> **41.7989%** Exposure
- `package/src/freshRequire.ts` -> **16.7982%** Exposure

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
- **Unknown Dependencies:** `14` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/animatedChartJSNodeCanvas.ts` (TYPESCRIPT) -> Cumulative Risk: **620.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 94.8 | **LOC:** 112 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9992%), State Flux (99.9959%), Safety Score (98.122%)
- **Heaviest Functions:** `renderChart` (Impact: 22.1), `onComplete` (Impact: 8.1), `onProgress` (Impact: 4.8)

### 2. `package/src/chartJSNodeCanvasBase.ts` (TYPESCRIPT) -> Cumulative Risk: **556.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 103.28 | **LOC:** 170 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (86.1853%), Safety Score (82.6535%), Verification (80.0%)
- **Heaviest Functions:** `initialize` (Impact: 29.5), `constructor` (Impact: 12.4), `toBuffer` (Impact: 6.0)

### 3. `package/src/example.ts` (TYPESCRIPT) -> Cumulative Risk: **471.06**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 19.16 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (86.4762%), Safety Score (59.4986%)
- **Heaviest Functions:** `main` (Impact: 4.4), `chartCallback` (Impact: 2.7), `beforeDraw` (Impact: 1.9)

### 4. `package/src/chartJSNodeCanvas.ts` (TYPESCRIPT) -> Cumulative Risk: **456.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 59.94 | **LOC:** 141 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (85.0424%), Concurrency (82.7987%), Safety Score (73.6532%)
- **Heaviest Functions:** `renderToStream` (Impact: 13.1), `renderToDataURL` (Impact: 6.0), `renderToBuffer` (Impact: 6.0)

### 5. `package/src/freshRequire.ts` (TYPESCRIPT) -> Cumulative Risk: **351.78**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 4.06 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (62.5811%), Stability (50.0%)
- **Heaviest Functions:** `freshRequire` (Impact: 1.9)

### 6. `package/src/backgroundColourPlugin.ts` (TYPESCRIPT) -> Cumulative Risk: **339.39**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 10.44 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (58.4884%), Stability (50.0%)
- **Heaviest Functions:** `constructor` (Impact: 2.2), `beforeDraw` (Impact: 1.9)

### 7. `package/src/freshImport.ts` (TYPESCRIPT) -> Cumulative Risk: **125.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 10.52 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Dead Code (72.9345%), Stability (50.0%), Verification (2.2977%)

### 8. `package/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **59.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 14.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Api Exposure (7.0517%), Verification (2.2977%)

### 9. `package/src/global.d.ts` (TYPESCRIPT) -> Cumulative Risk: **52.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.53 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/chartJSNodeCanvasBase.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 103.28 | **LOC:** 170 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.7493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initialize` (Impact: 29.5)
  * `constructor` (Impact: 12.4)
    * *Intent:* /** * Create a new instance of CanvasRenderService. * * @param options Configuration for this instan...
  * `toBuffer` (Impact: 6.0)
    * *Intent:* // https://github.com/Automattic/node-canvas#non-standard-apis
  * `registerFont` (Impact: 5.4)
    * *Intent:* /** * Use to register the font with Canvas to use a font file that is not installed as a system font...
  * `toBuffer` (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 31`, `args: 9`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 7`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 7`, `doc: 12`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 174.763
  * `Choke Point (Betweenness):` 0.045455 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 2):` backgroundColourPlugin, freshRequire, canvas, auto, path, stream
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/animatedChartJSNodeCanvas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 94.8 | **LOC:** 112 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.8016%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderChart` (Impact: 22.1)
  * `onComplete` (Impact: 8.1)
  * `onProgress` (Impact: 4.8)
  * `renderToBuffer` (Impact: 4.5)
    * *Intent:* /** * Render to a buffer. * @see https://github.com/Automattic/node-canvas#canvastobuffer * * @param...
  * `renderToDataURL` (Impact: 4.4)
    * *Intent:* /** * Render to a data url array. * @see https://github.com/Automattic/node-canvas#canvastodataurl *...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 25`, `args: 16`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 9`
* *Architecture:* `api: 3`, `concurrency: 8`, `import: 2`
* *Defense:* `safety: 2`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 64.727
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` chartJSNodeCanvasBase, auto
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/chartJSNodeCanvas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 59.94 | **LOC:** 141 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.0864%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderToStream` (Impact: 13.1)
    * *Intent:* /** * Render to a stream. * @see https://github.com/Automattic/node-canvas#canvascreatepngstream * *...
  * `renderToDataURL` (Impact: 6.0)
    * *Intent:* /** * Render to a data url. * @see https://github.com/Automattic/node-canvas#canvastodataurl * * @pa...
  * `renderToBuffer` (Impact: 6.0)
    * *Intent:* /** * Render to a buffer. * @see https://github.com/Automattic/node-canvas#canvastobuffer * * @param...
  * `renderChart` (Impact: 4.9)
  * `renderToDataURLSync` (Impact: 4.2)
    * *Intent:* /** * Render to a data url synchronously. * @see https://github.com/Automattic/node-canvas#canvastod...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 24`, `args: 11`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`
* *Architecture:* `api: 6`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 5`, `doc: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 64.727
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` chartJSNodeCanvasBase, auto, stream
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/example.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.16 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 4.4)
  * `chartCallback` (Impact: 2.7)
  * `beforeDraw` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` , auto, fs, make-a-gif, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 50.437
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` animatedChartJSNodeCanvas, chartJSNodeCanvas, chartJSNodeCanvasBase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/freshImport.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `dead_code: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.437
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/backgroundColourPlugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.44 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 2.2)
  * `beforeDraw` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 133.284
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.260417
  * `Imports (Out-Degree: 0):` auto
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.22 | **LOC:** 261 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 50.437
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` API.md, example.png, package.json, logo.png, backgroundColourPlugin.ts, example.ts, nodejs.yml, CHANGELOG.md...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/freshRequire.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4.06 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `freshRequire` (Impact: 1.9)
    * *Intent:* // https://github.com/hughsk/fresh-require
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 124.71
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.190476
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/API.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.12 | **LOC:** 106 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.34 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/global.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 0.53 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.437
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/chartJSNodeCanvasBase.ts` -> **Severity: 3.918** (Bridge: 0.0455 * Flux: 86.1853%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/chartJSNodeCanvasBase.ts` -> **Severity: 20.663** (Embedded: 0.25 * Error Risk: 82.6535%)
- `package/src/backgroundColourPlugin.ts` -> **Severity: 15.231** (Embedded: 0.2604 * Error Risk: 58.4884%)
- `package/src/freshRequire.ts` -> **Severity: 11.92** (Embedded: 0.1905 * Error Risk: 62.5811%)
- `package/src/animatedChartJSNodeCanvas.ts` -> **Severity: 8.177** (Embedded: 0.0833 * Error Risk: 98.122%)
- `package/src/chartJSNodeCanvas.ts` -> **Severity: 6.138** (Embedded: 0.0833 * Error Risk: 73.6532%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/backgroundColourPlugin.ts` -> **Severity: 13328.4** (Blast Radius: 133.284 * Doc Risk: 100.0%)
- `package/src/freshRequire.ts` -> **Severity: 12471.0** (Blast Radius: 124.71 * Doc Risk: 100.0%)
- `package/src/chartJSNodeCanvasBase.ts` -> **Severity: 12098.982** (Blast Radius: 174.763 * Doc Risk: 69.2308%)
- `package/src/example.ts` -> **Severity: 5901.1** (Blast Radius: 59.011 * Doc Risk: 100.0%)
- `package/src/animatedChartJSNodeCanvas.ts` -> **Severity: 4623.359** (Blast Radius: 64.727 * Doc Risk: 71.4286%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
