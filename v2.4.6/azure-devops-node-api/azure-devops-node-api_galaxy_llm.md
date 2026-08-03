# ARCHITECTURAL_BRIEF: azure-devops-node-api
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/azure-devops-node-api` |
| **Timestamp** | `2026-08-03T21:11:28.460817+00:00` |
| **Scan Duration** | `0.76s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 86 malicious artifacts.

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
| Total Artifacts | 164 |
| Analyzed Artifacts (Scanned) | 90 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 74 |
| Total LOC | 18568 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 54.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.214 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6342 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2899 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 74 | 17310 | 82.2% |
| JAVASCRIPT | 12 | 1258 | 13.3% |
| PLAINTEXT | 3 | 0 | 3.3% |
| MARKDOWN | 1 | 0 | 1.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.676`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 45 | 50.0% |
| file_cluster_2 | 27 | 30.0% |
| file_cluster_13 | 9 | 10.0% |
| file_cluster_16 | 2 | 2.2% |
| file_cluster_4 | 2 | 2.2% |
| file_cluster_11 | 1 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 4.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 74*

**Composition by Extension & Reason:**
- `.js`: 8x Excluded (Saturation: Line 12 exceeds 500 chars), 2x Excluded (Machine-Generated Source Code Signature: 122 LOC), 2x Excluded (Machine-Generated Source Code Signature: 76 LOC)
- `.ts`: 1x Excluded (Saturation: Line 23 exceeds 500 chars), 1x Excluded (Saturation: Line 26 exceeds 500 chars), 1x Excluded (Saturation: Line 63 exceeds 500 chars)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 66.3 | 23.2 | 10.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 36.8 | 47.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Testing Exposure | 0.5 | 80.0 | 22.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 12.8 | 7.3 | 7.5 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 41.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 5.6 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 94.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.1 | 99.9 | 23.1 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/GitApi.d.ts` (Hits: 12)
- `package/TfvcApi.d.ts` (Hits: 8)
- `package/WebApi.js` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **VsoBaseInterfaces.js** (`package/interfaces/common/VsoBaseInterfaces.js`) — 37 inbound connections
2. **ClientApiBases.js** (`package/ClientApiBases.js`) — 27 inbound connections
3. **VsoClient.js** (`package/VsoClient.js`) — 4 inbound connections
4. **TaskAgentApi.js** (`package/TaskAgentApi.js`) — 2 inbound connections
5. **Serialization.js** (`package/Serialization.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **WebApi.js** (`package/WebApi.js`) — 41 outbound dependencies
2. **WebApi.d.ts** (`package/WebApi.d.ts`) — 34 outbound dependencies
3. **WikiApi.d.ts** (`package/WikiApi.d.ts`) — 6 outbound dependencies
4. **CoreApi.d.ts** (`package/CoreApi.d.ts`) — 5 outbound dependencies
5. **GitApi.d.ts** (`package/GitApi.d.ts`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getTreeZip` (@ `package/GitApi.d.ts`) -> Impact: **1009.8** | LOC: 194
- `queryTestResultWorkItems` (@ `package/TestResultsApi.d.ts`) -> Impact: **827.0** | LOC: 248
- `_getTranslatedField` (@ `package/Serialization.js`) -> Impact: **614.7** | LOC: 86
- `updateWorkItemTypeDefinition` (@ `package/WorkItemTrackingApi.d.ts`) -> Impact: **594.6** | LOC: 148
- `updateVSCodeWebExtensionStatistics` (@ `package/GalleryApi.d.ts`) -> Impact: **537.0** | LOC: 180
- `getTfvcStatistics` (@ `package/TfvcApi.d.ts`) -> Impact: **244.8** | LOC: 46
- `getItems` (@ `package/FileContainerApiBase.d.ts`) -> Impact: **209.8** | LOC: 13
- `updateTestVariable` (@ `package/TestPlanApi.d.ts`) -> Impact: **200.9** | LOC: 99
- `constructor` (@ `package/WebApi.js`) -> Impact: **176.1** | LOC: 78
  * *Intent:* ; // --------------------------------------------------------------------------- // Factory to return client apis // When new APIs are added, a method...
- `updateWiki` (@ `package/WikiApi.d.ts`) -> Impact: **138.5** | LOC: 50

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_getTranslatedField` (@ `package/Serialization.js`) -> **O(2^N) [Recursive]**
- `_getTranslatedArray` (@ `package/Serialization.js`) -> **O(2^N) [Recursive]**
- `getTaskContentZip` (@ `package/TaskAgentApi.js`) -> **O(2^N) [Recursive]**
- `getTaskDefinition` (@ `package/TaskAgentApi.js`) -> **O(2^N) [Recursive]**
- `getTaskDefinitions` (@ `package/TaskAgentApi.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @param {string} taskId * @param {string} versionString * @param {string[]} visibility * @param {boolean} scopeLocal * @param onResult callback f...
- `deleteTaskDefinition` (@ `package/TaskAgentApi.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `updateVSCodeWebExtensionStatistics` (@ `package/GalleryApi.d.ts`) -> **O(2^N) [Recursive]**
- `getTimelines` (@ `package/TaskApi.d.ts`) -> **O(2^N) [Recursive]**
- `updateWorkItemTypeDefinition` (@ `package/WorkItemTrackingApi.d.ts`) -> **O(2^N) [Recursive]**
- `initiateValidation` (@ `package/AlertApi.d.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `constructor` (@ `package/WebApi.js`) -> DB Complexity: **38**
  * *Intent:* ; // --------------------------------------------------------------------------- // Factory to return client apis // When new APIs are added, a method...
- `createType3Message` (@ `package/opensource/node-http-ntlm/ntlm.js`) -> DB Complexity: **21**
- `getTreeZip` (@ `package/GitApi.d.ts`) -> DB Complexity: **13**
- `_getTranslatedField` (@ `package/Serialization.js`) -> DB Complexity: **10**
- `getTfvcStatistics` (@ `package/TfvcApi.d.ts`) -> DB Complexity: **9**
- `updateWiki` (@ `package/WikiApi.d.ts`) -> DB Complexity: **9**
- `constructor` (@ `package/ClientApiBases.js`) -> DB Complexity: **9**
- `_getTranslatedEnumValue` (@ `package/Serialization.js`) -> DB Complexity: **9**
- `uploadTaskDefinition` (@ `package/TaskAgentApi.js`) -> DB Complexity: **9**
- `_readTaskLibSecrets` (@ `package/WebApi.js`) -> DB Complexity: **9**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package` | 42 | 3593.29 | 37.71% | 11.47% |
| `package/interfaces` | 31 | 236.48 | 8.2% | 0.52% |
| `package/opensource/node-http-ntlm` | 2 | 213.74 | 28.19% | 0.0% |
| `package/interfaces/common` | 7 | 47.21 | 8.26% | 6.62% |
| `package/handlers` | 8 | 38.97 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/CIXApi.d.ts` -> **100.0%** Exposure
- `package/VsoClient.js` -> **100.0%** Exposure
- `package/WebApi.js` -> **99.9999%** Exposure
- `package/TaskAgentApi.js` -> **85.3656%** Exposure
- `package/interfaces/common/VsoBaseInterfaces.d.ts` -> **46.3301%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/Serialization.js` -> **100.0%** Exposure
- `package/TaskAgentApi.js` -> **100.0%** Exposure
- `package/VsoClient.js` -> **100.0%** Exposure
- `package/WebApi.js` -> **100.0%** Exposure
- `package/opensource/node-http-ntlm/ntlm.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/WebApi.js` -> **31** Orphaned Functions | **2** Duplicates
- `package/CIXApi.d.ts` -> **0** Orphaned Functions | **2** Duplicates
- `package/WorkApi.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/interfaces/common/VsoBaseInterfaces.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/TaskAgentApi.js` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/CoreApi.d.ts`** -> AI Confidence: **99.34%**
2. **`package/GitApi.d.ts`** -> AI Confidence: **99.34%**
3. **`package/WorkItemTrackingApi.d.ts`** -> AI Confidence: **99.34%**
4. **`package/GalleryApi.d.ts`** -> AI Confidence: **99.32%**
5. **`package/WebApi.d.ts`** -> AI Confidence: **99.31%**
6. **`package/WebApi.js`** -> AI Confidence: **99.31%**
7. **`package/TaskAgentApiBase.d.ts`** -> AI Confidence: **99.29%**
8. **`package/TestPlanApi.d.ts`** -> AI Confidence: **99.29%**
9. **`package/TestResultsApi.d.ts`** -> AI Confidence: **99.29%**
10. **`package/TfvcApi.d.ts`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/ClientApiBases.js` -> **100.0%** Exposure
- `package/Serialization.js` -> **100.0%** Exposure
- `package/TaskAgentApi.js` -> **100.0%** Exposure
- `package/VsoClient.js` -> **100.0%** Exposure
- `package/WebApi.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/ClientApiBases.js` -> **100.0%** Exposure
- `package/Serialization.js` -> **100.0%** Exposure
- `package/TaskAgentApi.js` -> **100.0%** Exposure
- `package/VsoClient.js` -> **100.0%** Exposure
- `package/WebApi.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/WebApi.js` (JAVASCRIPT) -> Cumulative Risk: **1002.51**
- **Archetype:** `file_cluster_11` (Distance: 14.343 IQR)
- **Magnitude:** 1202.54 | **LOC:** 497 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 176.1), `_getResourceAreaUrl` (Impact: 48.1), `connect` (Impact: 13.4)

### 2. `package/TaskAgentApi.js` (JAVASCRIPT) -> Cumulative Risk: **906.31**
- **Archetype:** `file_cluster_4` (Distance: 13.081 IQR)
- **Magnitude:** 403.18 | **LOC:** 204 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getTaskContentZip` (Impact: 67.9), `getTaskDefinition` (Impact: 67.9), `getTaskDefinitions` (Impact: 60.9)

### 3. `package/VsoClient.js` (JAVASCRIPT) -> Cumulative Risk: **777.89**
- **Archetype:** `file_cluster_4` (Distance: 12.655 IQR)
- **Magnitude:** 52.32 | **LOC:** 266 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `autoNegotiateApiVersion` (Impact: 17.6), `constructor` (Impact: 2.9), `constructor` (Impact: 2.3)

### 4. `package/Serialization.js` (JAVASCRIPT) -> Cumulative Risk: **730.94**
- **Archetype:** `file_cluster_8` (Distance: 12.671 IQR)
- **Magnitude:** 1124.94 | **LOC:** 273 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_getTranslatedField` (Impact: 614.7), `_getTranslatedEnumValue` (Impact: 114.0), `_getTranslatedArray` (Impact: 95.2)

### 5. `package/ClientApiBases.js` (JAVASCRIPT) -> Cumulative Risk: **615.12**
- **Archetype:** `file_cluster_8` (Distance: 10.055 IQR)
- **Magnitude:** 65.76 | **LOC:** 61 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (94.747%)
- **Heaviest Functions:** `extractRateLimitHeaders` (Impact: 32.4), `createAcceptHeader` (Impact: 5.3), `formatResponse` (Impact: 4.4)

### 6. `package/opensource/node-http-ntlm/ntlm.js` (JAVASCRIPT) -> Cumulative Risk: **447.34**
- **Archetype:** `file_cluster_8` (Distance: 10.848 IQR)
- **Magnitude:** 212.74 | **LOC:** 391 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Verification (80.0%), Cognitive Load (56.3754%)
- **Heaviest Functions:** `createType3Message` (Impact: 13.4), `parseType2Message` (Impact: 12.0), `binaryArray2bytes` (Impact: 8.8)

### 7. `package/interfaces/common/VsoBaseInterfaces.d.ts` (TYPESCRIPT) -> Cumulative Risk: **438.68**
- **Archetype:** `file_cluster_2` (Distance: 10.896 IQR)
- **Magnitude:** 2.96 | **LOC:** 132 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.7527%), Safety Score (53.5294%), Documentation (52.4099%)
- **Heaviest Functions:** `requestRawWithCallback` (Impact: 2.6), `handleAuthentication` (Impact: 2.3)

### 8. `package/WorkApi.d.ts` (TYPESCRIPT) -> Cumulative Risk: **422.8**
- **Archetype:** `file_cluster_2` (Distance: 14.222 IQR)
- **Magnitude:** 16.97 | **LOC:** 504 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Verification (80.0%), Stability (50.0%)
- **Heaviest Functions:** `reorderIterationWorkItems` (Impact: 64.2), `setBoardOptions` (Impact: 1.6), `updateBoardUserSettings` (Impact: 1.6)

### 9. `package/ManagementApi.d.ts` (TYPESCRIPT) -> Cumulative Risk: **419.99**
- **Archetype:** `file_cluster_2` (Distance: 15.013 IQR)
- **Magnitude:** 11.16 | **LOC:** 225 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Verification (80.0%), Stability (50.0%)
- **Heaviest Functions:** `getEstimatedRepoBillableCommittersDetail` (Impact: 58.4)

### 10. `package/CIXApi.d.ts` (TYPESCRIPT) -> Cumulative Risk: **415.8**
- **Archetype:** `file_cluster_2` (Distance: 12.385 IQR)
- **Magnitude:** 1.36 | **LOC:** 50 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9995%), Stability (50.0%)
- **Heaviest Functions:** `createResources` (Impact: 1.6), `createResources` (Impact: 1.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/WebApi.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.343 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.862 IQR)
- **Top Global Matches:** file_cluster_11: 14.343, file_cluster_13: 14.355, file_cluster_6: 14.733
- **Magnitude:** 1202.54 | **LOC:** 497 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (66.2512%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 176.1 | O(N^6) | DB: 38)
    * *Intent:* ; // --------------------------------------------------------------------------- // Factory to retur...
  * `_getResourceAreaUrl` (Impact: 48.1 | O(N^5) | DB: 2)
    * *Intent:* // TODO: Load RESOURCE_AREA_ID correctly.
  * `connect` (Impact: 13.4 | O(N^5) | DB: 3)
  * `_readTaskLibSecrets` (Impact: 12.2 | O(N^3) | DB: 9)
  * `getLocationsApi` (Impact: 10.9 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 99`, `args: 51`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 551`, `dead_code: 1`, `planned_debt: 24`, `duplicate_logic: 2`, `orphaned_logic: 31`
* *Architecture:* `io: 8`, `api: 12`, `concurrency: 8`, `import: 41`
* *Defense:* `safety: 15`, `doc: 9`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CoreApi, WikiApi, SecurityRolesApi, TestPlanApi, ntlm, ManagementApi, ExtensionManagementApi, ProjectAnalysisApi...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/Serialization.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.671 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.36 IQR)
- **Top Global Matches:** file_cluster_8: 12.671, file_cluster_11: 13.054, file_cluster_7: 13.056
- **Magnitude:** 1124.94 | **LOC:** 273 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (65.7757%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_getTranslatedField` (Impact: 614.7 | O(2^N) | DB: 10)
  * `_getTranslatedEnumValue` (Impact: 114.0 | O(N^6) | DB: 9)
  * `_getTranslatedArray` (Impact: 95.2 | O(2^N) | DB: 6)
  * `_getTranslatedObject` (Impact: 55.7 | O(N^6) | DB: 6)
  * `deserialize` (Impact: 47.8 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 53`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 112`
* *Architecture:* `api: 3`
* *Defense:* `safety: 18`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.160163
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/TaskAgentApi.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.081 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.696 IQR)
- **Top Global Matches:** file_cluster_4: 13.081, file_cluster_13: 13.517, file_cluster_15: 13.673
- **Magnitude:** 403.18 | **LOC:** 204 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (49.3766%), Tech Debt (85.3656%)
**Top Internal Functions/Classes:**
  * `getTaskContentZip` (Impact: 67.9 | O(2^N) | DB: 2)
  * `getTaskDefinition` (Impact: 67.9 | O(2^N) | DB: 2)
  * `getTaskDefinitions` (Impact: 60.9 | O(2^N) | DB: 2)
    * *Intent:* /** * @param {string} taskId * @param {string} versionString * @param {string[]} visibility * @param...
  * `deleteTaskDefinition` (Impact: 43.3 | O(2^N) | DB: 2)
    * *Intent:* /**
  * `uploadTaskDefinition` (Impact: 28.1 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 44`, `args: 20`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 58`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `concurrency: 32`, `import: 2`
* *Defense:* `safety: 7`, `doc: 25`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022472
  * `Imports (Out-Degree: 0):` url, TaskAgentApiBase
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/opensource/node-http-ntlm/ntlm.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.848 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.674 IQR)
- **Top Global Matches:** file_cluster_8: 10.848, file_cluster_7: 11.468, file_cluster_13: 11.474
- **Magnitude:** 212.74 | **LOC:** 391 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (56.3754%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createType3Message` (Impact: 13.4 | O(N^1) | DB: 21)
  * `parseType2Message` (Impact: 12.0 | O(N^1) | DB: 3)
  * `binaryArray2bytes` (Impact: 8.8 | O(N^1) | DB: 9)
  * `createType1Message` (Impact: 7.2 | O(N^1) | DB: 7)
  * `insertZerosEvery7Bits` (Impact: 5.8 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 83`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 139`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/GitApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_2` (Drift: 15.798 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.685 IQR)
- **Top Global Matches:** file_cluster_2: 15.798, file_cluster_16: 15.947, file_cluster_4: 16.141
- **Magnitude:** 128.89 | **LOC:** 1605 | **CtrlFlow:** 97.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (42.4996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getTreeZip` (Impact: 1009.8 | O(2^N) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 13`, `args: 247`, `func_start: 247`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 6`
* *Architecture:* `io: 12`, `api: 2`, `concurrency: 266`, `import: 5`
* *Defense:* `safety: 32`, `doc: 495`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CoreInterfaces, VsoBaseInterfaces, VSSInterfaces, ClientApiBases, GitInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/TestResultsApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_2` (Drift: 15.574 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.387 IQR)
- **Top Global Matches:** file_cluster_2: 15.574, file_cluster_16: 15.742, file_cluster_4: 16.12
- **Magnitude:** 107.6 | **LOC:** 1111 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.4989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `queryTestResultWorkItems` (Impact: 827.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 32`, `args: 243`, `func_start: 243`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`
* *Architecture:* `api: 2`, `concurrency: 242`, `import: 4`
* *Defense:* `safety: 24`, `doc: 588`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` VsoBaseInterfaces, VSSInterfaces, ClientApiBases, TestInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/WorkItemTrackingApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_2` (Drift: 14.595 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.452 IQR)
- **Top Global Matches:** file_cluster_2: 14.595, file_cluster_16: 14.746, file_cluster_4: 15.094
- **Magnitude:** 76.38 | **LOC:** 830 | **CtrlFlow:** 90.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.4967%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateWorkItemTypeDefinition` (Impact: 594.6 | O(2^N))
  * `getWorkItemTypeColors` (Impact: 2.8 | O(N^2))
  * `getWorkItemTypeColorAndIcons` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 27`, `args: 159`, `func_start: 159`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 158`, `import: 5`
* *Defense:* `safety: 13`, `doc: 267`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CoreInterfaces, VsoBaseInterfaces, VSSInterfaces, ClientApiBases, WorkItemTrackingInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/GalleryApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_2` (Drift: 15.805 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_2: 15.805, file_cluster_16: 15.917, file_cluster_4: 16.217
- **Magnitude:** 72.89 | **LOC:** 697 | **CtrlFlow:** 94.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.5%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateVSCodeWebExtensionStatistics` (Impact: 537.0 | O(2^N))
  * `updatePublisherAsset` (Impact: 11.2 | O(N^2))
  * `getGalleryUserSettings` (Impact: 5.3 | O(N^2))
  * `setGalleryUserSettings` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 11`, `args: 169`, `func_start: 169`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`
* *Architecture:* `api: 2`, `concurrency: 168`, `import: 3`
* *Defense:* `safety: 46`, `doc: 364`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` VsoBaseInterfaces, GalleryInterfaces, GalleryCompatHttpClientBase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ClientApiBases.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.055 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.897 IQR)
- **Top Global Matches:** file_cluster_8: 10.055, file_cluster_13: 10.066, file_cluster_7: 10.683
- **Magnitude:** 65.76 | **LOC:** 61 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (60.3648%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extractRateLimitHeaders` (Impact: 32.4 | O(N^3))
  * `createAcceptHeader` (Impact: 5.3 | O(N^2))
  * `formatResponse` (Impact: 4.4 | O(N^3) | DB: 2)
  * `constructor` (Impact: 3.7 | O(N^2) | DB: 9)
  * `createRequestOptions` (Impact: 2.8 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 8`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 6`, `import: 4`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 93.27
  * `Choke Point (Betweenness):` 0.006895 | `Ripple Effect (Closeness):` 0.303371
  * `Imports (Out-Degree: 2):` Serialization, RestClient, VsoClient, HttpClient
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `package/VsoClient.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.655 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.647 IQR)
- **Top Global Matches:** file_cluster_4: 12.655, file_cluster_13: 12.81, file_cluster_8: 13.275
- **Magnitude:** 52.32 | **LOC:** 266 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.4294%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `autoNegotiateApiVersion` (Impact: 17.6 | O(N^3) | DB: 4)
  * `constructor` (Impact: 2.9 | O(N^2) | DB: 5)
    * *Intent:* /** * Base class that should be used (derived from) to make requests to VSS REST apis
  * `constructor` (Impact: 2.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `args: 3`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 6`, `import: 2`
* *Defense:* `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.186168
  * `Imports (Out-Degree: 0):` url, path
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/TestPlanApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_2` (Drift: 15.763 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.228 IQR)
- **Top Global Matches:** file_cluster_2: 15.763, file_cluster_16: 15.921, file_cluster_13: 16.247
- **Magnitude:** 29.9 | **LOC:** 452 | **CtrlFlow:** 88.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.498%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateTestVariable` (Impact: 200.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 12`, `args: 95`, `func_start: 95`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 94`, `import: 4`
* *Defense:* `safety: 18`, `doc: 210`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` VsoBaseInterfaces, VSSInterfaces, ClientApiBases, TestPlanInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/TfvcApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.894 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.868 IQR)
- **Top Global Matches:** file_cluster_2: 13.894, file_cluster_16: 14.038, file_cluster_13: 14.324
- **Magnitude:** 29.19 | **LOC:** 255 | **CtrlFlow:** 92.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (42.4935%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getTfvcStatistics` (Impact: 244.8 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 12`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 8`, `api: 2`, `concurrency: 44`, `import: 4`
* *Defense:* `doc: 98`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` VsoBaseInterfaces, TfvcInterfaces, ClientApiBases, VSSInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/ReleaseInterfaces.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.743 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 3.847 IQR)
- **Top Global Matches:** file_cluster_8: 10.743, file_cluster_7: 10.959, file_cluster_1: 11.223
- **Magnitude:** 27.37 | **LOC:** 4544 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.7299%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 811`, `structural_boundaries: 534`, `class_start: 215`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 216`, `import: 3`
* *Defense:* `safety: 2`, `doc: 840`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` VSSInterfaces, DistributedTaskCommonInterfaces, FormInputInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/Serialization.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.364 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 3.573 IQR)
- **Top Global Matches:** file_cluster_8: 8.364, file_cluster_7: 8.734, file_cluster_1: 9.028
- **Magnitude:** 25.05 | **LOC:** 68 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.2046%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `api: 6`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/TaskAgentInterfaces.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.051 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 3.716 IQR)
- **Top Global Matches:** file_cluster_8: 10.051, file_cluster_7: 10.366, file_cluster_1: 10.638
- **Magnitude:** 23.1 | **LOC:** 4223 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.1839%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 557`, `structural_boundaries: 440`, `class_start: 180`
* *Risk/State:* `safety_bypasses: 105`, `state_mutation: 3`
* *Architecture:* `api: 181`, `import: 3`
* *Defense:* `doc: 353`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` VSSInterfaces, DistributedTaskCommonInterfaces, FormInputInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/FileContainerApiBase.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.449 IQR)
- **Local Micro-Species:** `Cluster 3: UI Frameworks & View Layers` (Drift: 6.597 IQR)
- **Top Global Matches:** file_cluster_13: 14.449, file_cluster_16: 14.56, file_cluster_2: 14.571
- **Magnitude:** 22.01 | **LOC:** 54 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.0963%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getItems` (Impact: 209.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 12`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 8`, `import: 4`
* *Defense:* `safety: 2`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` VsoBaseInterfaces, VSSInterfaces, ClientApiBases, FileContainerInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/TaskAgentApiBase.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_2` (Drift: 14.008 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.198 IQR)
- **Top Global Matches:** file_cluster_2: 14.008, file_cluster_16: 14.17, file_cluster_4: 14.449
- **Magnitude:** 21.72 | **LOC:** 1235 | **CtrlFlow:** 92.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.4984%), Tech Debt (12.5501%)
**Top Internal Functions/Classes:**
  * `getYamlSchema` (Impact: 43.0 | O(2^N))
  * `updateAgentUserCapabilities` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 12`, `args: 168`, `func_start: 168`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `concurrency: 167`, `import: 4`
* *Defense:* `safety: 28`, `doc: 32`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` VsoBaseInterfaces, VSSInterfaces, ClientApiBases, TaskAgentInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/common/System.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.723 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.318 IQR)
- **Top Global Matches:** file_cluster_8: 8.723, file_cluster_7: 9.002, file_cluster_1: 9.326
- **Magnitude:** 21.52 | **LOC:** 48 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.8822%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `args: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 5`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011236
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/interfaces/TestInterfaces.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.416 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 3.518 IQR)
- **Top Global Matches:** file_cluster_8: 10.416, file_cluster_7: 10.664, file_cluster_1: 10.934
- **Magnitude:** 20.82 | **LOC:** 6096 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.4965%), Tech Debt (8.206%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 703`, `structural_boundaries: 346`, `class_start: 154`
* *Risk/State:* `safety_bypasses: 141`, `state_mutation: 3`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 155`, `import: 3`
* *Defense:* `safety: 1`, `doc: 606`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SystemDataInterfaces, CoreInterfaces, VSSInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/WikiApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_2` (Drift: 14.375 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 7.043 IQR)
- **Top Global Matches:** file_cluster_2: 14.375, file_cluster_16: 14.49, file_cluster_13: 14.622
- **Magnitude:** 18.56 | **LOC:** 244 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (42.4907%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateWiki` (Impact: 138.5 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 20`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 44`, `import: 6`
* *Defense:* `safety: 2`, `doc: 120`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` WikiInterfaces, CommentsInterfaces, VsoBaseInterfaces, VSSInterfaces, ClientApiBases, GitInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/WorkApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 14.222 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.119 IQR)
- **Top Global Matches:** file_cluster_2: 14.222, file_cluster_16: 14.345, file_cluster_13: 14.777
- **Magnitude:** 16.97 | **LOC:** 504 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.4887%), Tech Debt (32.1778%)
**Top Internal Functions/Classes:**
  * `reorderIterationWorkItems` (Impact: 64.2 | O(2^N))
  * `setBoardOptions` (Impact: 1.6 | O(N^2))
  * `updateBoardUserSettings` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 12`, `args: 99`, `func_start: 99`, `class_start: 2`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 98`, `import: 4`
* *Defense:* `safety: 10`, `doc: 128`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` VsoBaseInterfaces, WorkInterfaces, ClientApiBases, CoreInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/WorkItemTrackingProcessApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_2` (Drift: 15.297 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.109 IQR)
- **Top Global Matches:** file_cluster_2: 15.297, file_cluster_16: 15.4, file_cluster_4: 15.824
- **Magnitude:** 16.85 | **LOC:** 522 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateBehaviorToWorkItemType` (Impact: 50.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 11`, `args: 115`, `func_start: 115`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 114`, `import: 3`
* *Defense:* `safety: 22`, `doc: 227`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` VsoBaseInterfaces, WorkItemTrackingProcessInterfaces, ClientApiBases
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/BuildInterfaces.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.353 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 3.777 IQR)
- **Top Global Matches:** file_cluster_8: 10.353, file_cluster_7: 10.579, file_cluster_1: 10.849
- **Magnitude:** 14.52 | **LOC:** 3621 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.789%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 278`, `class_start: 105`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 106`, `import: 5`
* *Defense:* `safety: 1`, `doc: 438`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` VSSInterfaces, TfvcInterfaces, TestInterfaces, DistributedTaskCommonInterfaces, CoreInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ThirdPartyNotice.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 13.74 | **LOC:** 687 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/CoreApi.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_2` (Drift: 15.07 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.387 IQR)
- **Top Global Matches:** file_cluster_2: 15.07, file_cluster_16: 15.156, file_cluster_13: 15.313
- **Magnitude:** 13.57 | **LOC:** 260 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.4979%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateTeam` (Impact: 78.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 13`, `args: 55`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `api: 2`, `concurrency: 54`, `import: 5`
* *Defense:* `safety: 13`, `doc: 63`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` OperationsInterfaces, CoreInterfaces, VsoBaseInterfaces, VSSInterfaces, ClientApiBases
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/WebApi.js` (JAVASCRIPT) | Magnitude: 1202.54 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 551, indent_spaces: 375, branch: 113, structural_boundaries: 99

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/TaskAgentApi.d.ts` (TYPESCRIPT) | Magnitude: 2.28 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 25, indent_spaces: 12, structural_boundaries: 11, args: 7
- `package/FileContainerApiBase.d.ts` (TYPESCRIPT) | Magnitude: 22.01 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: branch: 32, doc: 24, structural_boundaries: 12, generics: 10
- `package/ClientApiBases.d.ts` (TYPESCRIPT) | Magnitude: 13.18 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, args: 5, func_start: 5
- `package/WebApi.d.ts` (TYPESCRIPT) | Magnitude: 4.53 | Delta: **0.249 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 71, structural_boundaries: 50, indent_spaces: 47, args: 39
- `package/FileContainerApi.d.ts` (TYPESCRIPT) | Magnitude: 4.7 | Delta: **0.262 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 13, branch: 8, args: 6, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/interfaces/GraphInterfaces.d.ts` (TYPESCRIPT) | Magnitude: 5.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 81, indent_spaces: 71, doc: 53, branch: 47
- `package/SecurityRolesApi.d.ts` (TYPESCRIPT) | Magnitude: 2.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 22, args: 13, func_start: 13, indent_spaces: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/GalleryCompatHttpClientBase.d.ts` (TYPESCRIPT) | Magnitude: 2.3 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 11, generics: 10, args: 9
- `package/ProjectAnalysisApi.d.ts` (TYPESCRIPT) | Magnitude: 2.44 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 17, structural_boundaries: 11, generics: 10, indent_spaces: 10
- `package/CIXApi.d.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: branch: 20, doc: 19, indent_spaces: 13, structural_boundaries: 11
- `package/LocationsApi.d.ts` (TYPESCRIPT) | Magnitude: 7.58 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 34, branch: 26, args: 21, func_start: 21
- `package/ProfileApi.d.ts` (TYPESCRIPT) | Magnitude: 10.47 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 56, args: 35, func_start: 35, indent_spaces: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/VsoClient.js` (JAVASCRIPT) | Magnitude: 52.32 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 19, indent_spaces: 17, structural_boundaries: 6, concurrency: 6
- `package/TaskAgentApi.js` (JAVASCRIPT) | Magnitude: 403.18 | Delta: **0.436 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 119, state_mutation: 58, structural_boundaries: 44, branch: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/ClientApiBases.js` (JAVASCRIPT) | Magnitude: 65.76 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 10, branch: 9, structural_boundaries: 8
- `package/VsoClient.d.ts` (TYPESCRIPT) | Magnitude: 2.18 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, encapsulation: 10, args: 8
- `package/interfaces/PolicyInterfaces.d.ts` (TYPESCRIPT) | Magnitude: 2.72 | Delta: **0.127 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 43, doc: 38, structural_boundaries: 23, branch: 21
- `package/interfaces/WikiInterfaces.d.ts` (TYPESCRIPT) | Magnitude: 3.36 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 53, doc: 49, structural_boundaries: 36, branch: 35
- `package/interfaces/FeatureManagementInterfaces.d.ts` (TYPESCRIPT) | Magnitude: 2.63 | Delta: **0.187 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 46, doc: 36, branch: 26, structural_boundaries: 22

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/ClientApiBases.js` -> **Severity: 0.653** (Bridge: 0.0069 * Flux: 94.747%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/VsoClient.js` -> **Severity: 10.807** (Embedded: 0.1862 * Error Risk: 58.0489%)
- `package/Serialization.js` -> **Severity: 4.851** (Embedded: 0.1602 * Error Risk: 30.2894%)
- `package/ClientApiBases.js` -> **Severity: 4.717** (Embedded: 0.3034 * Error Risk: 15.5473%)
- `package/TaskAgentApi.js` -> **Severity: 1.11** (Embedded: 0.0225 * Error Risk: 49.3798%)
- `package/handlers/basiccreds.js` -> **Severity: 0.899** (Embedded: 0.0112 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/ClientApiBases.js` -> **Severity: 7678.555** (Blast Radius: 93.27 * Doc Risk: 82.3261%)
- `package/Serialization.js` -> **Severity: 4708.575** (Blast Radius: 47.116 * Doc Risk: 99.9358%)
- `package/interfaces/common/VsoBaseInterfaces.js` -> **Severity: 2987.881** (Blast Radius: 149.406 * Doc Risk: 19.9984%)
- `package/interfaces/common/System.js` -> **Severity: 1294.084** (Blast Radius: 13.831 * Doc Risk: 93.564%)
- `package/TaskAgentApi.js` -> **Severity: 928.591** (Blast Radius: 10.866 * Doc Risk: 85.4584%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
