# ARCHITECTURAL_BRIEF: @nx_node
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
| Total Artifacts | 71 |
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 34 |
| Total LOC | 1270 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 52.1% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4619 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0367 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 15 | 109 | 40.5% |
| JAVASCRIPT | 11 | 727 | 29.7% |
| JSON | 9 | 434 | 24.3% |
| MARKDOWN | 1 | 0 | 2.7% |
| PLAINTEXT | 1 | 0 | 2.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Guard/Validation-Heavy` (z -0.25; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 62%, Declarative / Non-Code 16%, Defensive Guards Files 11%, Large Core Modules 8%, Callbacks & Closures Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 35 | 94.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 34*

**Composition by Extension & Reason:**
- `.ts__tmpl__`: 11x Excluded (Unsupported Extension: '.ts__tmpl__'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 11x Excluded (Unsupported Extension: '.map')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.json__tmpl__'), 1x Unsupported Format (.undeterminable)
- `.js__tmpl__`: 1x Excluded (Unsupported Extension: '.js__tmpl__')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.3 | 16.7 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 86.8 | 23.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 50.0 | 10.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 6.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.4 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 22.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 57.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 35.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 1 | 1 | 0 | `package/src/utils/wait-for-port-open.js` |
| guards | 58 | 7 | 6 | `package/src/generators/e2e-project/e2e-project.js` |
| danger | 9 | 8 | 1 | `package/src/generators/setup-docker/setup-docker.js` |
| concurrency | 53 | 12 | 3 | `package/src/generators/application/application.js` |
| connectivity | 89 | 26 | 3 | `package/src/utils/versions.js` |
| io | 10 | 3 | 0 | `package/src/generators/e2e-project/e2e-project.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 2 | 0 | `package/src/utils/kill-port.js` |
| serialization | 2 | 2 | 0 | `package/src/utils/kill-port.js` |
| regex | 6 | 3 | 0 | `package/src/generators/setup-docker/setup-docker.js` |
| events | 12 | 2 | 0 | `package/src/utils/wait-for-port-open.js` |
| tests | 18 | 2 | 0 | `package/src/generators/e2e-project/e2e-project.js` |
| docs | 9 | 6 | 1 | `package/src/utils/wait-for-port-open.d.ts` |
| debt | 2 | 1 | 0 | `package/src/generators/e2e-project/e2e-project.js` |
| mutation | 203 | 13 | 13 | `package/src/generators/e2e-project/e2e-project.js` |
| dead_code | 7 | 7 | 1 | `package/src/generators/application/application.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 16 | 11 | 1 | `package/index.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/generators/e2e-project/e2e-project.js` (Hits: 7)
- `package/src/generators/setup-docker/setup-docker.js` (Hits: 2)
- `package/src/utils/wait-for-port-open.js` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **init.js** (`package/src/generators/init/init.js`) — 3 inbound connections
2. **versions.js** (`package/src/utils/versions.js`) — 3 inbound connections
3. **application.js** (`package/src/generators/application/application.js`) — 2 inbound connections
4. **kill-port.js** (`package/src/utils/kill-port.js`) — 2 inbound connections
5. **wait-for-port-open.js** (`package/src/utils/wait-for-port-open.js`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **e2e-project.js** (`package/src/generators/e2e-project/e2e-project.js`) — 13 outbound dependencies
2. **application.js** (`package/src/generators/application/application.js`) — 12 outbound dependencies
3. **setup-docker.js** (`package/src/generators/setup-docker/setup-docker.js`) — 4 outbound dependencies
4. **index.d.ts** (`package/index.d.ts`) — 3 outbound dependencies
5. **index.js** (`package/index.js`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `e2eProjectGeneratorInternal` **(Many-Argument Workhorses)** (@ `package/src/generators/e2e-project/e2e-project.js`) -> Impact: **82.2** | LOC: 190
- `applicationGeneratorInternal` **(Many-Argument Workhorses)** (@ `package/src/generators/application/application.js`) -> Impact: **53.8** | LOC: 141
- `addDocker` **(Compute Cores)** (@ `package/src/generators/setup-docker/setup-docker.js`) -> Impact: **28.3** | LOC: 46
- `waitForPortOpen` **(Defensive Guards)** (@ `package/src/utils/wait-for-port-open.js`) -> Impact: **24.4** | LOC: 37
  * *Intent:* /** * Waits for the given port to be open * @param port * @param options */
- `installTask` **(I/O & Config Routines)** (@ `package/src/generators/setup-docker/setup-docker.js`) -> Impact: **17.2** | LOC: 45
- `addVSCodeDebugConfiguration` **(Defensive Guards)** (@ `package/src/utils/vscode-debug-config.js`) -> Impact: **16.5** | LOC: 53
- `normalizeOptions` **(Defensive Guards)** (@ `package/src/generators/setup-docker/setup-docker.js`) -> Impact: **16.0** | LOC: 9
- `normalizeOptions` **(Defensive Guards)** (@ `package/src/generators/e2e-project/e2e-project.js`) -> Impact: **15.2** | LOC: 27
- `findFreeDebugPort` **(Defensive Guards)** (@ `package/src/utils/vscode-debug-config.js`) -> Impact: **12.6** | LOC: 25
- `cleanupClient` **(Callbacks & Closures)** (@ `package/src/utils/wait-for-port-open.js`) -> Impact: **10.6** | LOC: 31

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src/utils` | 10 | 208.69 | 18.48% | 20.0% |
| `package/src/generators/application` | 4 | 204.01 | 30.6% | 12.5% |
| `package/src/generators/e2e-project` | 4 | 182.78 | 18.74% | 16.2% |
| `package/src/generators/setup-docker` | 4 | 143.35 | 19.69% | 12.5% |
| `package` | 9 | 88.92 | 2.98% | 0.0% |
| `package/src/generators/init` | 4 | 53.1 | 24.54% | 0.0% |
| `package/src/generators/application/files/common` | 2 | 29.88 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/generators/application/application.d.ts` -> **50.0%** Exposure
- `package/src/generators/e2e-project/e2e-project.d.ts` -> **50.0%** Exposure
- `package/src/generators/setup-docker/setup-docker.d.ts` -> **50.0%** Exposure
- `package/src/utils/has-webpack-plugin.d.ts` -> **50.0%** Exposure
- `package/src/utils/kill-port.d.ts` -> **50.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/utils/kill-port.js` -> **100.0%** Exposure
- `package/src/utils/versions.js` -> **100.0%** Exposure
- `package/src/utils/vscode-debug-config.js` -> **100.0%** Exposure
- `package/src/generators/application/application.js` -> **99.9413%** Exposure
- `package/src/generators/setup-docker/setup-docker.js` -> **99.9163%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/generators/application/application.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/generators/e2e-project/e2e-project.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/generators/setup-docker/setup-docker.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/utils/has-webpack-plugin.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/utils/kill-port.d.ts` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `38` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/generators/application/application.js` (JAVASCRIPT) -> Cumulative Risk: **730.24**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.02)
- **Magnitude:** 184.94 | **LOC:** 193 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9413%)
- **Heaviest Functions:** `applicationGeneratorInternal` (Many-Argument Workhorses, Impact: 53.8), `updateTsConfigOptions` (Compute Cores, Impact: 8.3), `applicationGenerator` (Parameter Forwarders, Impact: 2.1)

### 2. `package/src/generators/setup-docker/setup-docker.js` (JAVASCRIPT) -> Cumulative Risk: **701.78**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.70)
- **Magnitude:** 126.44 | **LOC:** 104 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%), State Flux (99.9163%)
- **Heaviest Functions:** `addDocker` (Compute Cores, Impact: 28.3), `installTask` (I/O & Config Routines, Impact: 17.2), `normalizeOptions` (Defensive Guards, Impact: 16.0)

### 3. `package/src/generators/init/init.js` (JAVASCRIPT) -> Cumulative Risk: **662.81**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.37)
- **Magnitude:** 36.64 | **LOC:** 23 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.998%), State Flux (99.1837%)
- **Heaviest Functions:** `initGenerator` (Callbacks & Closures, Impact: 5.7), `installTask` (Callbacks & Closures, Impact: 4.5), `updateDependencies` (Annotated Framework Methods, Impact: 2.0)

### 4. `package/src/generators/e2e-project/e2e-project.js` (JAVASCRIPT) -> Cumulative Risk: **585.34**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.43)
- **Magnitude:** 165.16 | **LOC:** 243 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9082%), State Flux (92.9468%)
- **Heaviest Functions:** `e2eProjectGeneratorInternal` (Many-Argument Workhorses, Impact: 82.2), `normalizeOptions` (Defensive Guards, Impact: 15.2), `e2eProjectGenerator` (Parameter Forwarders, Impact: 2.1)

### 5. `package/src/utils/kill-port.js` (JAVASCRIPT) -> Cumulative Risk: **559.91**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.78)
- **Magnitude:** 47.52 | **LOC:** 37 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (83.5205%)
- **Heaviest Functions:** `killPort` (Defensive Guards, Impact: 9.9)

### 6. `package/src/utils/vscode-debug-config.js` (JAVASCRIPT) -> Cumulative Risk: **488.17**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.64)
- **Magnitude:** 54.58 | **LOC:** 83 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (75.6976%)
- **Heaviest Functions:** `addVSCodeDebugConfiguration` (Defensive Guards, Impact: 16.5), `findFreeDebugPort` (Defensive Guards, Impact: 12.6)

### 7. `package/src/utils/wait-for-port-open.js` (JAVASCRIPT) -> Cumulative Risk: **371.31**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.51)
- **Magnitude:** 45.24 | **LOC:** 48 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (53.3284%), Stability (50.0%), Documentation (50.0%)
- **Heaviest Functions:** `waitForPortOpen` (Defensive Guards, Impact: 24.4), `cleanupClient` (Callbacks & Closures, Impact: 10.6), `checkPort` (Defensive Guards, Impact: 4.4)

### 8. `package/src/generators/application/application.d.ts` (TYPESCRIPT) -> Cumulative Risk: **369.54**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 0.43 | **LOC:** 6 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (53.3284%), Tech Debt (50.0%)
- **Heaviest Functions:** `applicationGenerator` (Generic / Templated Code, Impact: 1.8), `applicationGeneratorInternal` (Generic / Templated Code, Impact: 1.8)

### 9. `package/src/generators/e2e-project/e2e-project.d.ts` (TYPESCRIPT) -> Cumulative Risk: **369.54**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 0.43 | **LOC:** 6 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (53.3284%), Tech Debt (50.0%)
- **Heaviest Functions:** `e2eProjectGenerator` (Generic / Templated Code, Impact: 1.8), `e2eProjectGeneratorInternal` (Generic / Templated Code, Impact: 1.8)

### 10. `package/src/generators/setup-docker/setup-docker.d.ts` (TYPESCRIPT) -> Cumulative Risk: **343.07**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 0.39 | **LOC:** 6 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (50.0%), Stability (50.0%)
- **Heaviest Functions:** `updateProjectConfig` (Parameter Forwarders, Impact: 1.8), `setupDockerGenerator` (Generic / Templated Code, Impact: 1.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/generators/application/application.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 184.94 | **LOC:** 193 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.3377%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applicationGeneratorInternal` **(Many-Argument Workhorses)** (Impact: 53.8)
  * `updateTsConfigOptions` **(Compute Cores)** (Impact: 8.3)
  * `applicationGenerator` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 68
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 26`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 3`, `concurrency: 18`, `import: 12`
* *Defense:* `safety: 10`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.957
  * `Choke Point (Betweenness):` 0.006349 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 4):` versions, e2e-project, init, setup-docker, lib, devkit, log-show-project-command, jest...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/e2e-project/e2e-project.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 165.16 | **LOC:** 243 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.26%), Tech Debt (14.8183%)
**Top Internal Functions/Classes:**
  * `e2eProjectGeneratorInternal` **(Many-Argument Workhorses)** (Impact: 82.2)
  * `normalizeOptions` **(Defensive Guards)** (Impact: 15.2)
  * `e2eProjectGenerator` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 21`, `args: 9`, `func_start: 3`
* *Risk/State:* `state_mutation: 11`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 3`, `concurrency: 9`, `import: 13`
* *Defense:* `safety: 22`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 1):` versions, devkit, project-name-and-root-utils, log-show-project-command, eslint, global-eslint-config, eslint-file, config-file...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/generators/setup-docker/setup-docker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 126.44 | **LOC:** 104 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.4321%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addDocker` **(Compute Cores)** (Impact: 28.3)
  * `installTask` **(I/O & Config Routines)** (Impact: 17.2)
  * `normalizeOptions` **(Defensive Guards)** (Impact: 16.0)
  * `updateProjectConfig` **(Compute Cores)** (Impact: 6.2)
  * `setupDockerGenerator` **(Parameter Forwarders)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 5`, `import: 4`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.83
  * `Choke Point (Betweenness):` 0.002381 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 1):` devkit, generators, fs, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/utils/vscode-debug-config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 54.58 | **LOC:** 83 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.8139%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addVSCodeDebugConfiguration` **(Defensive Guards)** (Impact: 16.5)
  * `findFreeDebugPort` **(Defensive Guards)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 5`, `args: 3`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils/versions.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 52.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`
* *Architecture:* `api: 24`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 89.573
  * `Choke Point (Betweenness):` 0.003968 | `Ripple Effect (Closeness):` 0.099206
  * `Imports (Out-Degree: 1):` package.json
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/utils/kill-port.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 47.52 | **LOC:** 37 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.5205%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `killPort` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* /** * Kills the process on the given port * @param port * @param killPortDelay */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 3`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`
* *Architecture:* `api: 4`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.957
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 0):` devkit, kill-port, tcp-port-used
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/utils/wait-for-port-open.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 45.24 | **LOC:** 48 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.5911%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `waitForPortOpen` **(Defensive Guards)** (Impact: 24.4)
    * *Intent:* /** * Waits for the given port to be open * @param port * @param options */
  * `cleanupClient` **(Callbacks & Closures)** (Impact: 10.6)
  * `checkPort` **(Defensive Guards)** (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 7`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 6`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.957
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 0):` devkit, net
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/init/init.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 36.64 | **LOC:** 23 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.6533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initGenerator` **(Callbacks & Closures)** (Impact: 5.7)
  * `installTask` **(Callbacks & Closures)** (Impact: 4.5)
  * `updateDependencies` **(Annotated Framework Methods)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 5`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.81
  * `Choke Point (Betweenness):` 0.001587 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` versions, devkit
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 18.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` application, init, library
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 18.64 | **LOC:** 8 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.4436%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` kill-port, wait-for-port-open
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/application/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 17.76 | **LOC:** 139 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/e2e-project/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.38 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/migrations.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.14 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/project.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.04 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/setup-docker/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.76 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/generators.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.68 | **LOC:** 35 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 43.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/generators/init/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.54 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/application/files/common/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.2 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/application/files/common/tsconfig.app.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils/has-webpack-plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6.7 | **LOC:** 11 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.7433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hasWebpackPlugin` **(Defensive Guards)** (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 2`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils/versions.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1.36 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 24`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.34 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.02 | **LOC:** 51 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 96.112
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.076923
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/generators/application/schema.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 0.88 | **LOC:** 33 | **CtrlFlow:** 82.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.2384%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 6`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eslint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/e2e-project/schema.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 0.81 | **LOC:** 14 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.8874%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.977
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

- `package/src/generators/application/application.js` -> **Severity: 0.635** (Bridge: 0.0063 * Flux: 99.9413%)
- `package/src/utils/versions.js` -> **Severity: 0.397** (Bridge: 0.004 * Flux: 100.0%)
- `package/src/generators/setup-docker/setup-docker.js` -> **Severity: 0.238** (Bridge: 0.0024 * Flux: 99.9163%)
- `package/src/generators/init/init.js` -> **Severity: 0.157** (Bridge: 0.0016 * Flux: 99.1837%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/utils/versions.js` -> **Severity: 8.614** (Embedded: 0.0992 * Error Risk: 86.8266%)
- `package/src/generators/init/init.js` -> **Severity: 6.528** (Embedded: 0.0833 * Error Risk: 78.3421%)
- `package/src/utils/kill-port.js` -> **Severity: 3.979** (Embedded: 0.0556 * Error Risk: 71.6205%)
- `package/src/generators/application/application.js` -> **Severity: 3.881** (Embedded: 0.0556 * Error Risk: 69.8587%)
- `package/src/generators/setup-docker/setup-docker.js` -> **Severity: 3.526** (Embedded: 0.05 * Error Risk: 70.5119%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/generators/init/init.js` -> **Severity: 4481.0** (Blast Radius: 44.81 * Doc Risk: 100.0%)
- `package/src/generators/application/application.js` -> **Severity: 3695.7** (Blast Radius: 36.957 * Doc Risk: 100.0%)
- `package/src/generators/e2e-project/e2e-project.js` -> **Severity: 2783.0** (Blast Radius: 27.83 * Doc Risk: 100.0%)
- `package/src/generators/setup-docker/setup-docker.js` -> **Severity: 2783.0** (Blast Radius: 27.83 * Doc Risk: 100.0%)
- `package/src/generators/application/application.d.ts` -> **Severity: 1997.7** (Blast Radius: 19.977 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
