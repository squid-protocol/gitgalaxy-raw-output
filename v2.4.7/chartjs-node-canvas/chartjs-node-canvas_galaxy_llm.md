# ARCHITECTURAL_BRIEF: chartjs-node-canvas
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/chartjs-node-canvas` |
| **Timestamp** | `2026-08-07T05:14:19.286089+00:00` |
| **Scan Duration** | `0.08s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 9 malicious artifacts.

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
| Modularity | 0.0714 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4951 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 9 | 358 | 69.2% |
| MARKDOWN | 3 | 0 | 23.1% |
| PLAINTEXT | 1 | 0 | 7.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.184`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4 | 30.8% |
| file_cluster_4 | 2 | 15.4% |
| file_cluster_13 | 2 | 15.4% |
| file_cluster_9 | 1 | 7.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 30.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 49.7 | 17.8 | 5.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 97.1 | 43.3 | 54.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 97.7 | 14.4 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 18.8 | 2.4 | 80.0 |
| API Exposure | 0.0 | 11.6 | 5.1 | 5.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.9 | 35.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 8.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 65.2 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.8 | 25.5 | 19.2 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/example.ts` (Hits: 6)
- `package/src/chartJSNodeCanvasBase.ts` (Hits: 3)
- `package/API.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **chartJSNodeCanvasBase.ts** (`package/src/chartJSNodeCanvasBase.ts`) — 3 inbound connections
2. **animatedChartJSNodeCanvas.ts** (`package/src/animatedChartJSNodeCanvas.ts`) — 1 inbound connections
3. **backgroundColourPlugin.ts** (`package/src/backgroundColourPlugin.ts`) — 1 inbound connections
4. **chartJSNodeCanvas.ts** (`package/src/chartJSNodeCanvas.ts`) — 1 inbound connections
5. **freshRequire.ts** (`package/src/freshRequire.ts`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **chartJSNodeCanvasBase.ts** (`package/src/chartJSNodeCanvasBase.ts`) — 6 outbound dependencies
2. **example.ts** (`package/src/example.ts`) — 5 outbound dependencies
3. **chartJSNodeCanvas.ts** (`package/src/chartJSNodeCanvas.ts`) — 3 outbound dependencies
4. **index.ts** (`package/src/index.ts`) — 3 outbound dependencies
5. **animatedChartJSNodeCanvas.ts** (`package/src/animatedChartJSNodeCanvas.ts`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `initialize` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **40.6** | LOC: 52
- `requestAnimationFrame` (@ `package/src/animatedChartJSNodeCanvas.ts`) -> Impact: **25.4** | LOC: 93
- `renderChart` (@ `package/src/animatedChartJSNodeCanvas.ts`) -> Impact: **22.1** | LOC: 41
- `constructor` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **14.9** | LOC: 21
  * *Intent:* /**
- `delete` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **14.0** | LOC: 12
- `renderToStream` (@ `package/src/chartJSNodeCanvas.ts`) -> Impact: **13.1** | LOC: 19
- `createPDFStream` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **11.2** | LOC: 17
- `setImmediate` (@ `package/src/chartJSNodeCanvas.ts`) -> Impact: **9.0** | LOC: 11
  * *Intent:* /** * Render to a buffer synchronously. * @see https://github.com/Automattic/node-canvas#canvastobuffer
- `renderChart` (@ `package/src/chartJSNodeCanvas.ts`) -> Impact: **6.7** | LOC: 14
- `require` (@ `package/src/chartJSNodeCanvasBase.ts`) -> Impact: **6.3** | LOC: 12

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src` | 9 | 44.61 | 17.83% | 14.36% |
| `package` | 4 | 9.68 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/animatedChartJSNodeCanvas.ts` -> **97.7023%** Exposure
- `package/src/example.ts` -> **31.5212%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/chartJSNodeCanvas.ts` -> **99.9439%** Exposure
- `package/src/animatedChartJSNodeCanvas.ts` -> **99.6316%** Exposure
- `package/src/chartJSNodeCanvasBase.ts` -> **93.0862%** Exposure
- `package/src/backgroundColourPlugin.ts` -> **22.7316%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/animatedChartJSNodeCanvas.ts` -> **0** Orphaned Functions | **2** Duplicates
- `package/src/example.ts` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/chartJSNodeCanvasBase.ts`** -> AI Confidence: **99.13%**
2. **`package/src/chartJSNodeCanvas.ts`** -> AI Confidence: **98.89%**
3. **`package/src/index.ts`** -> AI Confidence: **98.88%**
4. **`package/src/animatedChartJSNodeCanvas.ts`** -> AI Confidence: **98.85%**
5. **`package/src/backgroundColourPlugin.ts`** -> AI Confidence: **98.84%**
6. **`package/src/example.ts`** -> AI Confidence: **98.84%**
7. **`package/src/freshImport.ts`** -> AI Confidence: **98.84%**
8. **`package/src/freshRequire.ts`** -> AI Confidence: **98.84%**
9. **`package/src/global.d.ts`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/animatedChartJSNodeCanvas.ts` (TYPESCRIPT) -> Cumulative Risk: **704.34**
- **Archetype:** `file_cluster_4` (Distance: 12.797 IQR)
- **Magnitude:** 13.2 | **LOC:** 112 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.6316%), Tech Debt (97.7023%)
- **Heaviest Functions:** `requestAnimationFrame` (Impact: 25.4), `renderChart` (Impact: 22.1), `onProgress` (Impact: 5.7)

### 2. `package/src/chartJSNodeCanvas.ts` (TYPESCRIPT) -> Cumulative Risk: **542.27**
- **Archetype:** `file_cluster_4` (Distance: 13.081 IQR)
- **Magnitude:** 11.67 | **LOC:** 141 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9439%), Safety Score (85.0473%)
- **Heaviest Functions:** `renderToStream` (Impact: 13.1), `setImmediate` (Impact: 9.0), `renderChart` (Impact: 6.7)

### 3. `package/src/chartJSNodeCanvasBase.ts` (TYPESCRIPT) -> Cumulative Risk: **480.26**
- **Archetype:** `file_cluster_13` (Distance: 12.623 IQR)
- **Magnitude:** 13.01 | **LOC:** 170 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (93.0862%), Verification (80.0%), Safety Score (73.4218%)
- **Heaviest Functions:** `initialize` (Impact: 40.6), `constructor` (Impact: 14.9), `delete` (Impact: 14.0)

### 4. `package/src/backgroundColourPlugin.ts` (TYPESCRIPT) -> Cumulative Risk: **353.11**
- **Archetype:** `file_cluster_8` (Distance: 10.825 IQR)
- **Magnitude:** 1.4 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.7839%), Safety Score (54.0452%), Stability (50.0%)
- **Heaviest Functions:** `beforeDraw` (Impact: 2.5), `constructor` (Impact: 2.2)

### 5. `package/src/example.ts` (TYPESCRIPT) -> Cumulative Risk: **270.37**
- **Archetype:** `file_cluster_8` (Distance: 7.59 IQR)
- **Magnitude:** 1.43 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (86.4762%), Stability (50.0%), Tech Debt (31.5212%)
- **Heaviest Functions:** `main` (Impact: 5.1), `beforeDraw` (Impact: 2.1), `ChartCallback` (Impact: 1.9)

### 6. `package/src/freshRequire.ts` (TYPESCRIPT) -> Cumulative Risk: **212.87**
- **Archetype:** `file_cluster_8` (Distance: 8.329 IQR)
- **Magnitude:** 0.34 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (80.0%), Spec Match (53.3333%), Stability (50.0%), Documentation (17.8236%)
- **Heaviest Functions:** `any` (Impact: 2.2)

### 7. `package/src/freshImport.ts` (TYPESCRIPT) -> Cumulative Risk: **129.75**
- **Archetype:** `file_cluster_9` (Distance: 34.268 IQR)
- **Magnitude:** 1.05 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Dead Code (72.9345%), Stability (50.0%), Spec Match (6.6667%), Verification (0.1532%)

### 8. `package/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **106.25**
- **Archetype:** `file_cluster_13` (Distance: 7.189 IQR)
- **Magnitude:** 1.46 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (20.0%), Documentation (19.2297%), Api Exposure (11.5626%)

### 9. `package/src/global.d.ts` (TYPESCRIPT) -> Cumulative Risk: **56.82**
- **Archetype:** `file_cluster_8` (Distance: 5.394 IQR)
- **Magnitude:** 1.05 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Verification (0.1532%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/animatedChartJSNodeCanvas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.797 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.201 IQR)
- **Top Global Matches:** file_cluster_4: 12.797, file_cluster_13: 13.096, file_cluster_11: 13.211
- **Magnitude:** 13.2 | **LOC:** 112 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.697%), Tech Debt (97.7023%)
**Top Internal Functions/Classes:**
  * `requestAnimationFrame` (Impact: 25.4)
  * `renderChart` (Impact: 22.1)
  * `onProgress` (Impact: 5.7)
  * `onComplete` (Impact: 5.6)
  * `renderToBuffer` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 23`, `args: 21`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 26`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `concurrency: 28`, `import: 2`
* *Defense:* `safety: 4`, `doc: 6`, `immutability_locks: 20`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 67.626
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` auto, chartJSNodeCanvasBase
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/chartJSNodeCanvasBase.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.623 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.427 IQR)
- **Top Global Matches:** file_cluster_13: 12.623, file_cluster_8: 13.136, file_cluster_7: 13.24
- **Magnitude:** 13.01 | **LOC:** 170 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.988%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initialize` (Impact: 40.6)
  * `constructor` (Impact: 14.9)
    * *Intent:* /**
  * `delete` (Impact: 14.0)
  * `createPDFStream` (Impact: 11.2)
  * `require` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 26`, `args: 12`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 27`
* *Architecture:* `io: 3`, `api: 10`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 12`, `doc: 15`, `immutability_locks: 28`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 182.591
  * `Choke Point (Betweenness):` 0.045455 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 2):` freshRequire, auto, stream, backgroundColourPlugin, canvas, path
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/chartJSNodeCanvas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.081 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.611 IQR)
- **Top Global Matches:** file_cluster_4: 13.081, file_cluster_13: 13.251, file_cluster_11: 13.595
- **Magnitude:** 11.67 | **LOC:** 141 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.8608%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderToStream` (Impact: 13.1)
  * `setImmediate` (Impact: 9.0)
    * *Intent:* /** * Render to a buffer synchronously. * @see https://github.com/Automattic/node-canvas#canvastobuf...
  * `renderChart` (Impact: 6.7)
  * `renderToDataURL` (Impact: 6.0)
    * *Intent:* /**
  * `renderToBuffer` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 24`, `args: 12`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 29`
* *Architecture:* `api: 12`, `concurrency: 25`, `import: 3`
* *Defense:* `safety: 5`, `doc: 15`, `immutability_locks: 15`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 67.626
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` auto, stream, chartJSNodeCanvasBase
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.189 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.03 IQR)
- **Top Global Matches:** file_cluster_13: 7.189, file_cluster_8: 7.895, file_cluster_7: 8.783
- **Magnitude:** 1.46 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 52.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` animatedChartJSNodeCanvas, chartJSNodeCanvas, chartJSNodeCanvasBase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/example.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.59 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.225 IQR)
- **Top Global Matches:** file_cluster_8: 7.59, file_cluster_13: 8.354, file_cluster_7: 8.681
- **Magnitude:** 1.43 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (31.5212%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 5.1)
  * `beforeDraw` (Impact: 2.1)
  * `ChartCallback` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 5`, `func_start: 5`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 6`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` auto, make-a-gif, fs, path, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/backgroundColourPlugin.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.825 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.159 IQR)
- **Top Global Matches:** file_cluster_8: 10.825, file_cluster_13: 10.886, file_cluster_7: 11.448
- **Magnitude:** 1.4 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.9632%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `beforeDraw` (Impact: 2.5)
  * `constructor` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 130.296
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.190476
  * `Imports (Out-Degree: 0):` auto
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/freshImport.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_9` (Drift: 34.268 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.223 IQR)
- **Top Global Matches:** file_cluster_9: 34.268, file_cluster_6: 34.342, file_cluster_17: 34.442
- **Magnitude:** 1.05 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `dead_code: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/global.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.394 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.214 IQR)
- **Top Global Matches:** file_cluster_8: 5.394, file_cluster_7: 6.892, file_cluster_1: 7.012
- **Magnitude:** 1.05 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/freshRequire.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.329 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.891 IQR)
- **Top Global Matches:** file_cluster_8: 8.329, file_cluster_13: 8.512, file_cluster_7: 9.125
- **Magnitude:** 0.34 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `any` (Impact: 2.2)
    * *Intent:* // https://github.com/hughsk/fresh-require
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 130.296
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.190476
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/chartJSNodeCanvasBase.ts` (TYPESCRIPT) | Magnitude: 13.01 | Delta: **0.513 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 87, branch: 43, immutability_locks: 28, state_mutation: 27
- `package/src/index.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.706 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/src/chartJSNodeCanvas.ts` (TYPESCRIPT) | Magnitude: 11.67 | Delta: **0.17 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 82, state_mutation: 29, concurrency: 25, structural_boundaries: 24
- `package/src/animatedChartJSNodeCanvas.ts` (TYPESCRIPT) | Magnitude: 13.2 | Delta: **0.299 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 72, concurrency: 28, state_mutation: 26, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/backgroundColourPlugin.ts` (TYPESCRIPT) | Magnitude: 1.4 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 14, api: 6, immutability_locks: 5, structural_boundaries: 4
- `package/src/freshRequire.ts` (TYPESCRIPT) | Magnitude: 0.34 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 4, immutability_locks: 4, args: 2
- `package/src/example.ts` (TYPESCRIPT) | Magnitude: 1.43 | Delta: **0.764 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 51, structural_boundaries: 10, immutability_locks: 8, io: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `package/src/freshImport.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/chartJSNodeCanvasBase.ts` -> **Severity: 4.231** (Bridge: 0.0455 * Flux: 93.0862%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/chartJSNodeCanvasBase.ts` -> **Severity: 18.355** (Embedded: 0.25 * Error Risk: 73.4218%)
- `package/src/freshRequire.ts` -> **Severity: 15.238** (Embedded: 0.1905 * Error Risk: 80.0%)
- `package/src/backgroundColourPlugin.ts` -> **Severity: 10.294** (Embedded: 0.1905 * Error Risk: 54.0452%)
- `package/src/animatedChartJSNodeCanvas.ts` -> **Severity: 8.096** (Embedded: 0.0833 * Error Risk: 97.1474%)
- `package/src/chartJSNodeCanvas.ts` -> **Severity: 7.087** (Embedded: 0.0833 * Error Risk: 85.0473%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/backgroundColourPlugin.ts` -> **Severity: 12871.147** (Blast Radius: 130.296 * Doc Risk: 98.7839%)
- `package/src/chartJSNodeCanvasBase.ts` -> **Severity: 4287.072** (Blast Radius: 182.591 * Doc Risk: 23.4791%)
- `package/src/chartJSNodeCanvas.ts` -> **Severity: 3128.96** (Blast Radius: 67.626 * Doc Risk: 46.2686%)
- `package/src/freshRequire.ts` -> **Severity: 2322.344** (Blast Radius: 130.296 * Doc Risk: 17.8236%)
- `package/src/animatedChartJSNodeCanvas.ts` -> **Severity: 1612.785** (Blast Radius: 67.626 * Doc Risk: 23.8486%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
