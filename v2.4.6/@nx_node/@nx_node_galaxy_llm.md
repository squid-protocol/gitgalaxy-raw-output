# ARCHITECTURAL_BRIEF: @nx_node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@nx_node` |
| **Timestamp** | `2026-08-03T21:09:34.511973+00:00` |
| **Scan Duration** | `0.2s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 26 malicious artifacts.

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
| Total Artifacts | 71 |
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 34 |
| Total LOC | 1053 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 52.1% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4395 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1657 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7857 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 15 | 109 | 40.5% |
| JAVASCRIPT | 11 | 510 | 29.7% |
| JSON | 9 | 434 | 24.3% |
| MARKDOWN | 1 | 0 | 2.7% |
| PLAINTEXT | 1 | 0 | 2.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.716`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 18 | 48.6% |
| file_cluster_13 | 10 | 27.0% |
| file_cluster_4 | 5 | 13.5% |
| file_cluster_0 | 2 | 5.4% |

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 98.9 | 15.9 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 12.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Testing Exposure | 0.3 | 80.0 | 10.5 | 1.8 | 2.3 |
| API Exposure | 0.0 | 22.7 | 6.4 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 30.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 69.5 | 80.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 1.6 | 100.0 | 44.3 | 33.3 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 14.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/generators/e2e-project/e2e-project.js` (Hits: 3)
- `package/src/generators/setup-docker/setup-docker.js` (Hits: 3)
- `package/README.md` (Hits: 0)

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

- `checkPort` (@ `package/src/utils/wait-for-port-open.js`) -> Impact: **205.2** | LOC: 30
  * *Intent:* /** * Waits for the given port to be open * @param port * @param options */
- `applicationGeneratorInternal` (@ `package/src/generators/application/application.js`) -> Impact: **124.0** | LOC: 141
- `addDocker` (@ `package/src/generators/setup-docker/setup-docker.js`) -> Impact: **67.3** | LOC: 46
- `findFreeDebugPort` (@ `package/src/utils/vscode-debug-config.js`) -> Impact: **61.9** | LOC: 25
- `killPort` (@ `package/src/utils/kill-port.js`) -> Impact: **31.5** | LOC: 24
  * *Intent:* /**
- `addVSCodeDebugConfiguration` (@ `package/src/utils/vscode-debug-config.js`) -> Impact: **31.2** | LOC: 18
- `normalizeOptions` (@ `package/src/generators/setup-docker/setup-docker.js`) -> Impact: **23.8** | LOC: 9
- `updateTsConfigOptions` (@ `package/src/generators/application/application.js`) -> Impact: **22.2** | LOC: 28
- `e2eProjectGeneratorInternal` (@ `package/src/generators/e2e-project/e2e-project.js`) -> Impact: **19.3** | LOC: 23
- `updateProjectConfig` (@ `package/src/generators/setup-docker/setup-docker.js`) -> Impact: **14.0** | LOC: 20

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `checkPort` (@ `package/src/utils/wait-for-port-open.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Waits for the given port to be open * @param port * @param options */
- `findFreeDebugPort` (@ `package/src/utils/vscode-debug-config.js`) -> **O(N^6)**
- `updateTsConfigOptions` (@ `package/src/generators/application/application.js`) -> **O(N^5)**
- `applicationGeneratorInternal` (@ `package/src/generators/application/application.js`) -> **O(N^4)**
- `addDocker` (@ `package/src/generators/setup-docker/setup-docker.js`) -> **O(N^4)**
- `updateProjectConfig` (@ `package/src/generators/setup-docker/setup-docker.js`) -> **O(N^4)**
- `killPort` (@ `package/src/utils/kill-port.js`) -> **O(N^4)**
  * *Intent:* /**
- `addVSCodeDebugConfiguration` (@ `package/src/utils/vscode-debug-config.js`) -> **O(N^4)**

### Highest Data Gravity (Database Complexity)
- `applicationGeneratorInternal` (@ `package/src/generators/application/application.js`) -> DB Complexity: **12**
- `addDocker` (@ `package/src/generators/setup-docker/setup-docker.js`) -> DB Complexity: **5**
- `killPort` (@ `package/src/utils/kill-port.js`) -> DB Complexity: **3**
  * *Intent:* /**
- `findFreeDebugPort` (@ `package/src/utils/vscode-debug-config.js`) -> DB Complexity: **3**
- `updateDependencies` (@ `package/src/generators/init/init.js`) -> DB Complexity: **2**
- `addVSCodeDebugConfiguration` (@ `package/src/utils/vscode-debug-config.js`) -> DB Complexity: **2**
- `initGenerator` (@ `package/src/generators/init/init.js`) -> DB Complexity: **1**
- `updateProjectConfig` (@ `package/src/generators/setup-docker/setup-docker.js`) -> DB Complexity: **1**
- `setupDockerGenerator` (@ `package/src/generators/setup-docker/setup-docker.js`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src/utils` | 10 | 435.47 | 16.36% | 17.13% |
| `package/src/generators/application` | 4 | 282.58 | 28.48% | 0.0% |
| `package/src/generators/setup-docker` | 4 | 177.14 | 19.96% | 0.0% |
| `package` | 9 | 93.3 | 3.14% | 0.0% |
| `package/src/generators/e2e-project` | 4 | 52.35 | 10.58% | 10.48% |
| `package/src/generators/init` | 4 | 44.98 | 29.58% | 0.0% |
| `package/src/generators/application/files/common` | 2 | 29.88 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/utils/wait-for-port-open.d.ts` -> **99.9992%** Exposure
- `package/src/utils/vscode-debug-config.js` -> **71.2814%** Exposure
- `package/src/generators/e2e-project/e2e-project.js` -> **41.9193%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/utils/vscode-debug-config.js` -> **100.0%** Exposure
- `package/utils.js` -> **100.0%** Exposure
- `package/index.js` -> **99.9984%** Exposure
- `package/src/generators/init/init.js` -> **98.3433%** Exposure
- `package/src/generators/application/application.js` -> **90.132%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/utils/wait-for-port-open.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/utils/vscode-debug-config.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/generators/application/application.js`** -> AI Confidence: **99.31%**
2. **`package/src/generators/e2e-project/e2e-project.js`** -> AI Confidence: **99.31%**
3. **`package/src/generators/application/schema.d.ts`** -> AI Confidence: **99.29%**
4. **`package/src/generators/e2e-project/schema.d.ts`** -> AI Confidence: **99.29%**
5. **`package/src/utils/vscode-debug-config.js`** -> AI Confidence: **99.29%**
6. **`package/src/generators/setup-docker/schema.d.ts`** -> AI Confidence: **99.17%**
7. **`package/src/generators/setup-docker/setup-docker.js`** -> AI Confidence: **99.17%**
8. **`package/src/generators/init/schema.d.ts`** -> AI Confidence: **99.06%**
9. **`package/src/utils/wait-for-port-open.d.ts`** -> AI Confidence: **99.06%**
10. **`package/src/utils/has-webpack-plugin.js`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/src/generators/application/application.js` -> **100.0%** Exposure
- `package/src/generators/setup-docker/setup-docker.js` -> **82.6997%** Exposure
- `package/src/utils/vscode-debug-config.js` -> **54.947%** Exposure
- `package/src/utils/wait-for-port-open.js` -> **0.0741%** Exposure
- `package/src/utils/kill-port.js` -> **0.0453%** Exposure
### Algorithmic DoS Exposure
- `package/src/generators/application/application.js` -> **100.0%** Exposure
- `package/src/generators/setup-docker/setup-docker.js` -> **100.0%** Exposure
- `package/src/utils/vscode-debug-config.js` -> **100.0%** Exposure
- `package/src/utils/kill-port.js` -> **99.57%** Exposure
- `package/src/utils/wait-for-port-open.js` -> **98.0876%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `38` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/generators/application/application.js` (JAVASCRIPT) -> Cumulative Risk: **815.77**
- **Archetype:** `file_cluster_4` (Distance: 11.228 IQR)
- **Magnitude:** 258.84 | **LOC:** 193 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `applicationGeneratorInternal` (Impact: 124.0), `updateTsConfigOptions` (Impact: 22.2), `applicationGenerator` (Impact: 2.9)

### 2. `package/src/generators/setup-docker/setup-docker.js` (JAVASCRIPT) -> Cumulative Risk: **732.7**
- **Archetype:** `file_cluster_4` (Distance: 10.666 IQR)
- **Magnitude:** 155.74 | **LOC:** 104 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.7828%)
- **Heaviest Functions:** `addDocker` (Impact: 67.3), `normalizeOptions` (Impact: 23.8), `updateProjectConfig` (Impact: 14.0)

### 3. `package/src/utils/vscode-debug-config.js` (JAVASCRIPT) -> Cumulative Risk: **706.56**
- **Archetype:** `file_cluster_8` (Distance: 11.916 IQR)
- **Magnitude:** 103.98 | **LOC:** 83 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9968%)
- **Heaviest Functions:** `findFreeDebugPort` (Impact: 61.9), `addVSCodeDebugConfiguration` (Impact: 31.2)

### 4. `package/src/utils/kill-port.js` (JAVASCRIPT) -> Cumulative Risk: **622.16**
- **Archetype:** `file_cluster_4` (Distance: 11.242 IQR)
- **Magnitude:** 61.12 | **LOC:** 37 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.57%), Documentation (95.9945%)
- **Heaviest Functions:** `killPort` (Impact: 31.5)

### 5. `package/src/generators/init/init.js` (JAVASCRIPT) -> Cumulative Risk: **577.19**
- **Archetype:** `file_cluster_4` (Distance: 10.751 IQR)
- **Magnitude:** 24.74 | **LOC:** 23 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (98.8508%), State Flux (98.3433%)
- **Heaviest Functions:** `initGenerator` (Impact: 8.3), `updateDependencies` (Impact: 2.0)

### 6. `package/src/utils/wait-for-port-open.js` (JAVASCRIPT) -> Cumulative Risk: **476.28**
- **Archetype:** `file_cluster_8` (Distance: 11.336 IQR)
- **Magnitude:** 210.14 | **LOC:** 48 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9959%), Algorithmic Dos (98.0876%), Verification (80.0%)
- **Heaviest Functions:** `checkPort` (Impact: 205.2), `waitForPortOpen` (Impact: 1.1)

### 7. `package/src/utils/versions.js` (JAVASCRIPT) -> Cumulative Risk: **363.93**
- **Archetype:** `file_cluster_8` (Distance: 7.857 IQR)
- **Magnitude:** 39.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (63.3333%), Stability (50.0%)

### 8. `package/src/generators/e2e-project/e2e-project.js` (JAVASCRIPT) -> Cumulative Risk: **346.41**
- **Archetype:** `file_cluster_13` (Distance: 9.754 IQR)
- **Magnitude:** 30.12 | **LOC:** 243 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9234%), Stability (50.0%), Tech Debt (41.9193%)
- **Heaviest Functions:** `e2eProjectGeneratorInternal` (Impact: 19.3), `e2eProjectGenerator` (Impact: 2.9)

### 9. `package/index.js` (JAVASCRIPT) -> Cumulative Risk: **315.09**
- **Archetype:** `file_cluster_13` (Distance: 11.709 IQR)
- **Magnitude:** 20.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9984%), Safety Score (80.0%), Spec Match (60.0%), Stability (50.0%)

### 10. `package/src/utils/versions.d.ts` (TYPESCRIPT) -> Cumulative Risk: **307.94**
- **Archetype:** `file_cluster_8` (Distance: 7.901 IQR)
- **Magnitude:** 2.72 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (80.0%), Documentation (80.0%), Safety Score (71.6667%), Stability (50.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/generators/application/application.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.228 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.935 IQR)
- **Top Global Matches:** file_cluster_4: 11.228, file_cluster_13: 11.616, file_cluster_8: 11.711
- **Magnitude:** 258.84 | **LOC:** 193 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (97.4727%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applicationGeneratorInternal` (Impact: 124.0 | O(N^4) | DB: 12)
  * `updateTsConfigOptions` (Impact: 22.2 | O(N^5))
  * `applicationGenerator` (Impact: 2.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 26`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 35`
* *Architecture:* `api: 3`, `concurrency: 68`, `import: 12`
* *Defense:* `safety: 10`, `test: 3`, `immutability_locks: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.002
  * `Choke Point (Betweenness):` 0.005556 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 4):` jest, lib, versions, ensure-dependencies, setup-docker, js, e2e-project, log-show-project-command...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/utils/wait-for-port-open.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.336 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 6.943 IQR)
- **Top Global Matches:** file_cluster_8: 11.336, file_cluster_13: 11.397, file_cluster_1: 11.464
- **Magnitude:** 210.14 | **LOC:** 48 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (18.3749%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkPort` (Impact: 205.2 | O(2^N))
    * *Intent:* /** * Waits for the given port to be open * @param port * @param options */
  * `waitForPortOpen` (Impact: 1.1 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 7`, `args: 7`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 6`, `doc: 3`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 0):` devkit, net
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/setup-docker/setup-docker.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.666 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.96 IQR)
- **Top Global Matches:** file_cluster_4: 10.666, file_cluster_8: 11.023, file_cluster_13: 11.072
- **Magnitude:** 155.74 | **LOC:** 104 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (64.4049%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addDocker` (Impact: 67.3 | O(N^4) | DB: 5)
  * `normalizeOptions` (Impact: 23.8 | O(N^2))
  * `updateProjectConfig` (Impact: 14.0 | O(N^4) | DB: 1)
  * `setupDockerGenerator` (Impact: 5.7 | O(N^2) | DB: 1)
  * `sanitizeProjectName` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 11`, `args: 6`, `func_start: 8`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 25`, `import: 4`
* *Defense:* `safety: 6`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.123
  * `Choke Point (Betweenness):` 0.002381 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 1):` path, generators, fs, devkit
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/utils/vscode-debug-config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.916 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.953 IQR)
- **Top Global Matches:** file_cluster_8: 11.916, file_cluster_13: 11.98, file_cluster_0: 12.005
- **Magnitude:** 103.98 | **LOC:** 83 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (42.134%), Tech Debt (71.2814%)
**Top Internal Functions/Classes:**
  * `findFreeDebugPort` (Impact: 61.9 | O(N^6) | DB: 3)
  * `addVSCodeDebugConfiguration` (Impact: 31.2 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 4`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils/kill-port.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.242 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 6.552 IQR)
- **Top Global Matches:** file_cluster_4: 11.242, file_cluster_13: 11.587, file_cluster_0: 11.947
- **Magnitude:** 61.12 | **LOC:** 37 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (52.4818%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `killPort` (Impact: 31.5 | O(N^4) | DB: 3)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `args: 3`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 4`, `concurrency: 22`, `import: 3`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 0):` kill-port, tcp-port-used, devkit
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/utils/versions.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.857 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.087 IQR)
- **Top Global Matches:** file_cluster_8: 7.857, file_cluster_13: 8.624, file_cluster_7: 8.748
- **Magnitude:** 39.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.5724%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 24`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 96.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.099206
  * `Imports (Out-Degree: 0):` package.json
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/generators/e2e-project/e2e-project.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.754 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 6.939 IQR)
- **Top Global Matches:** file_cluster_13: 9.754, file_cluster_0: 9.758, file_cluster_8: 10.136
- **Magnitude:** 30.12 | **LOC:** 243 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (32.3194%), Tech Debt (41.9193%)
**Top Internal Functions/Classes:**
  * `e2eProjectGeneratorInternal` (Impact: 19.3 | O(N^2))
  * `e2eProjectGenerator` (Impact: 2.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 4`, `args: 2`, `func_start: 2`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 4`, `import: 13`
* *Defense:* `safety: 4`, `test: 2`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 1):` versions, eslint, eslint-file, posix, config-file, project-name-and-root-utils, path, versions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/generators/init/init.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.751 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.084 IQR)
- **Top Global Matches:** file_cluster_4: 10.751, file_cluster_13: 11.084, file_cluster_0: 11.096
- **Magnitude:** 24.74 | **LOC:** 23 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (98.8508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initGenerator` (Impact: 8.3 | O(N^2) | DB: 1)
  * `updateDependencies` (Impact: 2.0 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 5`, `args: 3`, `func_start: 4`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 2`, `concurrency: 7`, `import: 2`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 48.503
  * `Choke Point (Betweenness):` 0.000794 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` versions, devkit
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.709 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.364 IQR)
- **Top Global Matches:** file_cluster_13: 11.709, file_cluster_12: 12.089, file_cluster_11: 12.31
- **Magnitude:** 20.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` library, init, application
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.146 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.193 IQR)
- **Top Global Matches:** file_cluster_13: 12.146, file_cluster_12: 12.518, file_cluster_11: 12.584
- **Magnitude:** 19.64 | **LOC:** 8 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` kill-port, wait-for-port-open
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/application/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 17.76 | **LOC:** 139 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/e2e-project/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 16.38 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/migrations.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 16.14 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/project.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 16.04 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/setup-docker/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.76 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.4407%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/generators.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.68 | **LOC:** 35 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.228%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/generators/init/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.54 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.4554%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/application/files/common/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.2 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/application/files/common/tsconfig.app.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils/has-webpack-plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.088 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 6.34 IQR)
- **Top Global Matches:** file_cluster_0: 12.088, file_cluster_17: 12.407, file_cluster_13: 12.465
- **Magnitude:** 9.3 | **LOC:** 11 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hasWebpackPlugin` (Impact: 8.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 2`, `args: 2`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/application/application.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.404 IQR)
- **Local Micro-Species:** `Cluster 3: UI Frameworks & View Layers` (Drift: 5.896 IQR)
- **Top Global Matches:** file_cluster_13: 10.404, file_cluster_4: 10.813, file_cluster_2: 10.887
- **Magnitude:** 4.22 | **LOC:** 6 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit, schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/e2e-project/e2e-project.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.404 IQR)
- **Local Micro-Species:** `Cluster 3: UI Frameworks & View Layers` (Drift: 5.896 IQR)
- **Top Global Matches:** file_cluster_13: 10.404, file_cluster_4: 10.813, file_cluster_2: 10.887
- **Magnitude:** 4.22 | **LOC:** 6 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit, schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/setup-docker/setup-docker.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.942 IQR)
- **Local Micro-Species:** `Cluster 3: UI Frameworks & View Layers` (Drift: 5.523 IQR)
- **Top Global Matches:** file_cluster_13: 11.942, file_cluster_0: 12.255, file_cluster_4: 12.372
- **Magnitude:** 4.12 | **LOC:** 6 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit, schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils/vscode-debug-config.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.158 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.167 IQR)
- **Top Global Matches:** file_cluster_0: 10.158, file_cluster_13: 10.236, file_cluster_8: 10.28
- **Magnitude:** 3.39 | **LOC:** 8 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/init/init.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.684 IQR)
- **Local Micro-Species:** `Cluster 3: UI Frameworks & View Layers` (Drift: 5.771 IQR)
- **Top Global Matches:** file_cluster_13: 9.684, file_cluster_0: 10.301, file_cluster_4: 10.305
- **Magnitude:** 3.34 | **LOC:** 5 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devkit, schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/src/utils/vscode-debug-config.d.ts` (TYPESCRIPT) | Magnitude: 3.39 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 3, api: 2, branch: 1
- `package/src/utils/has-webpack-plugin.js` (JAVASCRIPT) | Magnitude: 9.3 | Delta: **0.319 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: safety: 5, indent_spaces: 4, decorators: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/generators/e2e-project/e2e-project.js` (JAVASCRIPT) | Magnitude: 30.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, immutability_locks: 20, import: 13, decorators: 10
- `package/src/utils/has-webpack-plugin.d.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.177 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, api: 1
- `package/src/generators/setup-docker/setup-docker.d.ts` (TYPESCRIPT) | Magnitude: 4.12 | Delta: **0.313 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 7, api: 3, args: 2, func_start: 2
- `package/utils.js` (JAVASCRIPT) | Magnitude: 19.64 | Delta: **0.372 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 4, state_mutation: 4, reflection_metaprogramming: 3, args: 2
- `package/index.js` (JAVASCRIPT) | Magnitude: 20.68 | Delta: **0.38 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 6, reflection_metaprogramming: 4, args: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/src/utils/kill-port.d.ts` (TYPESCRIPT) | Magnitude: 3.23 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 3, api: 2, branch: 1
- `package/src/generators/init/init.js` (JAVASCRIPT) | Magnitude: 24.74 | Delta: **0.333 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, concurrency: 7, structural_boundaries: 5, state_mutation: 5
- `package/src/utils/kill-port.js` (JAVASCRIPT) | Magnitude: 61.12 | Delta: **0.345 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 22, indent_spaces: 22, structural_boundaries: 10, branch: 6
- `package/src/generators/setup-docker/setup-docker.js` (JAVASCRIPT) | Magnitude: 155.74 | Delta: **0.357 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, branch: 26, concurrency: 25, immutability_locks: 14
- `package/src/generators/application/application.js` (JAVASCRIPT) | Magnitude: 258.84 | Delta: **0.388 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, concurrency: 68, state_mutation: 35, branch: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/utils/wait-for-port-open.js` (JAVASCRIPT) | Magnitude: 210.14 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, branch: 12, func_start: 9, structural_boundaries: 7
- `package/src/utils/vscode-debug-config.js` (JAVASCRIPT) | Magnitude: 103.98 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, branch: 15, state_mutation: 9, safety: 7
- `package/src/utils/wait-for-port-open.d.ts` (TYPESCRIPT) | Magnitude: 0.67 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 6, branch: 4, structural_boundaries: 4, indent_spaces: 3
- `package/src/generators/application/schema.d.ts` (TYPESCRIPT) | Magnitude: 1.76 | Delta: **0.75 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 25, branch: 24, structural_boundaries: 6, api: 2
- `package/src/utils/versions.js` (JAVASCRIPT) | Magnitude: 39.3 | Delta: **0.767 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 24, bitwise_ops: 10, safety_bypasses: 1, reflection_metaprogramming: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/generators/application/application.js` -> **Severity: 0.501** (Bridge: 0.0056 * Flux: 90.132%)
- `package/src/generators/setup-docker/setup-docker.js` -> **Severity: 0.106** (Bridge: 0.0024 * Flux: 44.5679%)
- `package/src/generators/init/init.js` -> **Severity: 0.078** (Bridge: 0.0008 * Flux: 98.3433%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/utils/versions.js` -> **Severity: 6.283** (Embedded: 0.0992 * Error Risk: 63.3333%)
- `package/src/utils/kill-port.js` -> **Severity: 2.563** (Embedded: 0.0556 * Error Risk: 46.129%)
- `package/src/generators/init/init.js` -> **Severity: 1.272** (Embedded: 0.0833 * Error Risk: 15.2609%)
- `package/src/generators/application/application.js` -> **Severity: 0.447** (Embedded: 0.0556 * Error Risk: 8.0451%)
- `package/src/generators/setup-docker/setup-docker.js` -> **Severity: 0.314** (Embedded: 0.05 * Error Risk: 6.2822%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/utils/versions.js` -> **Severity: 9696.2** (Blast Radius: 96.962 * Doc Risk: 100.0%)
- `package/src/generators/init/init.js` -> **Severity: 4701.716** (Blast Radius: 48.503 * Doc Risk: 96.9366%)
- `package/src/utils/kill-port.js` -> **Severity: 3839.972** (Blast Radius: 40.002 * Doc Risk: 95.9945%)
- `package/src/generators/application/application.js` -> **Severity: 3394.542** (Blast Radius: 40.002 * Doc Risk: 84.8593%)
- `package/src/generators/setup-docker/setup-docker.js` -> **Severity: 2975.634** (Blast Radius: 30.123 * Doc Risk: 98.7828%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
