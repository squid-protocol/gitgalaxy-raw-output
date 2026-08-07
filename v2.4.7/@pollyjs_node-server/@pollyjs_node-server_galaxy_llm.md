# ARCHITECTURAL_BRIEF: @pollyjs_node-server
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@pollyjs_node-server` |
| **Timestamp** | `2026-08-07T05:12:45.127631+00:00` |
| **Scan Duration** | `0.07s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6 malicious artifacts.

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
| Total Artifacts | 9 |
| Analyzed Artifacts (Scanned) | 8 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 176 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.378 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 5 | 139 | 62.5% |
| MARKDOWN | 1 | 0 | 12.5% |
| PLAINTEXT | 1 | 0 | 12.5% |
| TYPESCRIPT | 1 | 37 | 12.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.839`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 4 | 50.0% |
| file_cluster_8 | 2 | 25.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 25.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 72.2 | 26.8 | 8.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.3 | 36.7 | 23.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 55.1 | 9.2 | 0.0 | 0.0 |
| Testing Exposure | 0.6 | 2.5 | 2.0 | 2.5 | 2.5 |
| API Exposure | 5.3 | 13.4 | 8.3 | 7.4 | 8.9 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 26.7 | 100.0 | 78.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 88.8 | 42.0 | 38.6 | 88.8 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/api.js` (Hits: 10)
- `package/types.d.ts` (Hits: 4)
- `package/src/server.js` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.js** (`package/src/config.js`) — 3 inbound connections
2. **api.js** (`package/src/api.js`) — 2 inbound connections
3. **register-api.js** (`package/src/express/register-api.js`) — 2 inbound connections
4. **server.js** (`package/src/server.js`) — 1 inbound connections
5. **README.md** (`package/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **server.js** (`package/src/server.js`) — 6 outbound dependencies
2. **register-api.js** (`package/src/express/register-api.js`) — 5 outbound dependencies
3. **index.js** (`package/src/index.js`) — 4 outbound dependencies
4. **api.js** (`package/src/api.js`) — 3 outbound dependencies
5. **types.d.ts** (`package/types.d.ts`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `listen` (@ `package/src/server.js`) -> Impact: **15.3** | LOC: 28
- `respond` (@ `package/types.d.ts`) -> Impact: **10.9** | LOC: 11
- `registerAPI` (@ `package/src/express/register-api.js`) -> Impact: **7.3** | LOC: 42
- `prependSlash` (@ `package/src/express/register-api.js`) -> Impact: **4.8** | LOC: 7
- `getRecording` (@ `package/src/api.js`) -> Impact: **3.3** | LOC: 9
- `deleteRecording` (@ `package/src/api.js`) -> Impact: **3.3** | LOC: 9
- `saveRecording` (@ `package/src/api.js`) -> Impact: **2.1** | LOC: 7
- `respond` (@ `package/src/api.js`) -> Impact: **1.9** | LOC: 3
- `filenameFor` (@ `package/src/api.js`) -> Impact: **1.6** | LOC: 3
- `registerAPI` (@ `package/src/server.js`) -> Impact: **1.2** | LOC: 4

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src` | 4 | 142.32 | 36.2% | 0.0% |
| `package/src/express` | 1 | 14.96 | 8.0% | 0.0% |
| `package` | 3 | 4.62 | 2.72% | 18.35% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/types.d.ts` -> **55.0503%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/api.js` -> **100.0%** Exposure
- `package/src/server.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/types.d.ts` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/config.js`** -> AI Confidence: **99.06%**
2. **`package/src/index.js`** -> AI Confidence: **99.06%**
3. **`package/src/server.js`** -> AI Confidence: **99.03%**
4. **`package/src/express/register-api.js`** -> AI Confidence: **98.93%**
5. **`package/src/api.js`** -> AI Confidence: **98.92%**
6. **`package/types.d.ts`** -> AI Confidence: **98.89%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/api.js` (JAVASCRIPT) -> Cumulative Risk: **489.91**
- **Archetype:** `file_cluster_13` (Distance: 12.493 IQR)
- **Magnitude:** 40.08 | **LOC:** 54 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (88.7734%), Safety Score (77.1227%)
- **Heaviest Functions:** `getRecording` (Impact: 3.3), `deleteRecording` (Impact: 3.3), `saveRecording` (Impact: 2.1)

### 2. `package/src/server.js` (JAVASCRIPT) -> Cumulative Risk: **470.83**
- **Archetype:** `file_cluster_13` (Distance: 13.141 IQR)
- **Magnitude:** 71.52 | **LOC:** 60 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.3285%), Cognitive Load (72.2425%)
- **Heaviest Functions:** `listen` (Impact: 15.3), `registerAPI` (Impact: 1.2), `constructor` (Impact: 1.1)

### 3. `package/types.d.ts` (TYPESCRIPT) -> Cumulative Risk: **284.33**
- **Archetype:** `file_cluster_13` (Distance: 9.427 IQR)
- **Magnitude:** 1.86 | **LOC:** 46 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (55.0503%), Stability (50.0%), Safety Score (45.9301%)
- **Heaviest Functions:** `respond` (Impact: 10.9)

### 4. `package/src/express/register-api.js` (JAVASCRIPT) -> Cumulative Risk: **213.49**
- **Archetype:** `file_cluster_8` (Distance: 7.759 IQR)
- **Magnitude:** 14.96 | **LOC:** 58 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (47.6208%), Cognitive Load (8.0036%)
- **Heaviest Functions:** `registerAPI` (Impact: 7.3), `prependSlash` (Impact: 4.8)

### 5. `package/src/config.js` (JAVASCRIPT) -> Cumulative Risk: **142.29**
- **Archetype:** `file_cluster_8` (Distance: 4.97 IQR)
- **Magnitude:** 14.64 | **LOC:** 8 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (46.6667%), Documentation (33.7734%), Api Exposure (5.7813%)

### 6. `package/src/index.js` (JAVASCRIPT) -> Cumulative Risk: **122.32**
- **Archetype:** `file_cluster_13` (Distance: 6.851 IQR)
- **Magnitude:** 16.08 | **LOC:** 5 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (26.6667%), Documentation (26.6194%), Api Exposure (13.4238%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.141 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.304 IQR)
- **Top Global Matches:** file_cluster_13: 13.141, file_cluster_11: 13.619, file_cluster_8: 13.637
- **Magnitude:** 71.52 | **LOC:** 60 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2425%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `listen` (Impact: 15.3)
  * `registerAPI` (Impact: 1.2)
  * `constructor` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 14`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `io: 2`, `api: 2`, `import: 6`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 106.835
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142857
  * `Imports (Out-Degree: 2):` register-api, http-graceful-shutdown, cors, express, config, morgan
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/api.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.493 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.72 IQR)
- **Top Global Matches:** file_cluster_13: 12.493, file_cluster_0: 12.645, file_cluster_8: 12.825
- **Magnitude:** 40.08 | **LOC:** 54 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.5467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRecording` (Impact: 3.3)
  * `deleteRecording` (Impact: 3.3)
  * `saveRecording` (Impact: 2.1)
  * `respond` (Impact: 1.9)
  * `filenameFor` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 6`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `io: 10`, `api: 5`, `import: 3`
* *Defense:* `safety: 3`, `test: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 171.537
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.321429
  * `Imports (Out-Degree: 0):` utils, fs-extra, path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.851 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.058 IQR)
- **Top Global Matches:** file_cluster_13: 6.851, file_cluster_8: 7.804, file_cluster_7: 8.647
- **Magnitude:** 16.08 | **LOC:** 5 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 88.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` config, register-api, api, server
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/express/register-api.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.759 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.92 IQR)
- **Top Global Matches:** file_cluster_8: 7.759, file_cluster_13: 8.132, file_cluster_7: 8.783
- **Magnitude:** 14.96 | **LOC:** 58 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.0036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `registerAPI` (Impact: 7.3)
  * `prependSlash` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 5`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 152.24
  * `Choke Point (Betweenness):` 0.02381 | `Ripple Effect (Closeness):` 0.285714
  * `Imports (Out-Degree: 2):` nocache, express, api, config, body-parser
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.97 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.989 IQR)
- **Top Global Matches:** file_cluster_8: 4.97, file_cluster_7: 6.443, file_cluster_1: 6.726
- **Magnitude:** 14.64 | **LOC:** 8 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 216.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.428571
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/types.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.427 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.987 IQR)
- **Top Global Matches:** file_cluster_13: 9.427, file_cluster_16: 9.556, file_cluster_8: 9.602
- **Magnitude:** 1.86 | **LOC:** 46 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.1544%), Tech Debt (55.0503%)
**Top Internal Functions/Classes:**
  * `respond` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 16`, `args: 9`, `func_start: 9`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 7`, `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 88.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` express, cors, http
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.64 | **LOC:** 82 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 88.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.12 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 88.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/types.d.ts` (TYPESCRIPT) | Magnitude: 1.86 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, args: 9, func_start: 9
- `package/src/api.js` (JAVASCRIPT) | Magnitude: 40.08 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 21, structural_boundaries: 11, io: 10
- `package/src/server.js` (JAVASCRIPT) | Magnitude: 71.52 | Delta: **0.478 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 51, indent_spaces: 38, structural_boundaries: 14, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/express/register-api.js` (JAVASCRIPT) | Magnitude: 14.96 | Delta: **0.373 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 9, immutability_locks: 8, args: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/api.js` -> **Severity: 24.789** (Embedded: 0.3214 * Error Risk: 77.1227%)
- `package/src/server.js` -> **Severity: 13.904** (Embedded: 0.1429 * Error Risk: 97.3285%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/api.js` -> **Severity: 15227.923** (Blast Radius: 171.537 * Doc Risk: 88.7734%)
- `package/src/config.js` -> **Severity: 7326.869** (Blast Radius: 216.942 * Doc Risk: 33.7734%)
- `package/src/express/register-api.js` -> **Severity: 7249.791** (Blast Radius: 152.24 * Doc Risk: 47.6208%)
- `package/src/server.js` -> **Severity: 4633.306** (Blast Radius: 106.835 * Doc Risk: 43.3688%)
- `package/src/index.js` -> **Severity: 2345.462** (Blast Radius: 88.111 * Doc Risk: 26.6194%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
