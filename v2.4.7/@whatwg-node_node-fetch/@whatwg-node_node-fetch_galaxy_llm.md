# ARCHITECTURAL_BRIEF: @whatwg-node_node-fetch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@whatwg-node_node-fetch` |
| **Timestamp** | `2026-08-07T05:14:01.349006+00:00` |
| **Scan Duration** | `0.22s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 92 malicious artifacts.

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
| Total Artifacts | 94 |
| Analyzed Artifacts (Scanned) | 94 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 4892 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 46 | 4092 | 48.9% |
| TYPESCRIPT | 46 | 800 | 48.9% |
| PLAINTEXT | 2 | 0 | 2.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.601`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 40 | 42.6% |
| file_cluster_8 | 30 | 31.9% |
| file_cluster_16 | 12 | 12.8% |
| file_cluster_4 | 4 | 4.3% |
| file_cluster_2 | 4 | 4.3% |
| file_cluster_0 | 2 | 2.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 4.0 | 100.0 | 34.5 | 20.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.6 | 51.4 | 64.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.7 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 18.9 | 2.4 | 80.0 |
| API Exposure | 2.1 | 19.7 | 7.5 | 6.8 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.1 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 83.8 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 5.7 | 100.0 | 49.7 | 51.7 | 8.7 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/cjs/Request.js` (Hits: 5)
- `package/cjs/fetch.js` (Hits: 5)
- `package/esm/Request.js` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AbortError.js** (`package/cjs/AbortError.js`) — 0 inbound connections
2. **Blob.js** (`package/cjs/Blob.js`) — 0 inbound connections
3. **Body.js** (`package/cjs/Body.js`) — 0 inbound connections
4. **CompressionStream.js** (`package/cjs/CompressionStream.js`) — 0 inbound connections
5. **DecompressionStream.js** (`package/cjs/DecompressionStream.js`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/cjs/index.js`) — 18 outbound dependencies
2. **index.js** (`package/esm/index.js`) — 18 outbound dependencies
3. **index.d.cts** (`package/typings/index.d.cts`) — 18 outbound dependencies
4. **index.d.ts** (`package/typings/index.d.ts`) — 18 outbound dependencies
5. **fetchNodeHttp.js** (`package/cjs/fetchNodeHttp.js`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `fetchNodeHttp` (@ `package/cjs/fetchNodeHttp.js`) -> Impact: **101.9** | LOC: 133
- `constructor` (@ `package/cjs/Request.js`) -> Impact: **96.7** | LOC: 64
- `constructor` (@ `package/esm/Request.js`) -> Impact: **96.7** | LOC: 64
- `fetchNodeHttp` (@ `package/esm/fetchNodeHttp.js`) -> Impact: **91.5** | LOC: 133
- `fetchCurl` (@ `package/cjs/fetchCurl.js`) -> Impact: **77.7** | LOC: 134
- `fetchCurl` (@ `package/esm/fetchCurl.js`) -> Impact: **77.7** | LOC: 134
- `json` (@ `package/cjs/Response.js`) -> Impact: **49.5** | LOC: 55
- `json` (@ `package/esm/Response.js`) -> Impact: **49.5** | LOC: 55
- `getMap` (@ `package/cjs/Headers.js`) -> Impact: **41.3** | LOC: 62
  * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
- `getMap` (@ `package/esm/Headers.js`) -> Impact: **41.3** | LOC: 62
  * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/esm` | 23 | 2653.68 | 52.07% | 34.54% |
| `package/cjs` | 24 | 2652.76 | 61.43% | 32.88% |
| `package/typings` | 46 | 193.7 | 11.01% | 34.96% |
| `package` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/cjs/TextEncoderDecoderStream.js` -> **100.0%** Exposure
- `package/cjs/TransformStream.js` -> **100.0%** Exposure
- `package/cjs/WritableStream.js` -> **100.0%** Exposure
- `package/esm/TextEncoderDecoderStream.js` -> **100.0%** Exposure
- `package/esm/TransformStream.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/cjs/Body.js` -> **100.0%** Exposure
- `package/cjs/Headers.js` -> **100.0%** Exposure
- `package/cjs/IteratorObject.js` -> **100.0%** Exposure
- `package/cjs/Request.js` -> **100.0%** Exposure
- `package/cjs/URL.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/cjs/WritableStream.js` -> **0** Orphaned Functions | **12** Duplicates
- `package/esm/WritableStream.js` -> **0** Orphaned Functions | **12** Duplicates
- `package/typings/Blob.d.cts` -> **8** Orphaned Functions | **0** Duplicates
- `package/typings/Blob.d.ts` -> **8** Orphaned Functions | **0** Duplicates
- `package/cjs/TransformStream.js` -> **0** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/cjs/fetchNodeHttp.js`** -> AI Confidence: **99.39%**
2. **`package/cjs/Request.js`** -> AI Confidence: **99.34%**
3. **`package/cjs/fetchCurl.js`** -> AI Confidence: **99.34%**
4. **`package/cjs/Response.js`** -> AI Confidence: **99.32%**
5. **`package/cjs/Body.js`** -> AI Confidence: **99.31%**
6. **`package/cjs/fetch.js`** -> AI Confidence: **99.31%**
7. **`package/esm/fetchNodeHttp.js`** -> AI Confidence: **99.31%**
8. **`package/esm/Body.js`** -> AI Confidence: **99.23%**
9. **`package/esm/Request.js`** -> AI Confidence: **99.23%**
10. **`package/esm/Response.js`** -> AI Confidence: **99.2%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/cjs/WritableStream.js` (JAVASCRIPT) -> Cumulative Risk: **755.77**
- **Archetype:** `file_cluster_4` (Distance: 12.015 IQR)
- **Magnitude:** 134.58 | **LOC:** 116 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.3735%), State Flux (97.5515%)
- **Heaviest Functions:** `constructor` (Impact: 21.0), `write` (Impact: 12.9), `getWriter` (Impact: 8.9)

### 2. `package/esm/WritableStream.js` (JAVASCRIPT) -> Cumulative Risk: **753.03**
- **Archetype:** `file_cluster_4` (Distance: 12.168 IQR)
- **Magnitude:** 135.5 | **LOC:** 112 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.5304%), Concurrency (99.4888%)
- **Heaviest Functions:** `constructor` (Impact: 21.0), `write` (Impact: 12.9), `getWriter` (Impact: 8.9)

### 3. `package/cjs/ReadableStream.js` (JAVASCRIPT) -> Cumulative Risk: **733.05**
- **Archetype:** `file_cluster_4` (Distance: 12.941 IQR)
- **Magnitude:** 309.48 | **LOC:** 246 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9986%), Concurrency (99.7954%), Tech Debt (97.9214%)
- **Heaviest Functions:** `constructor` (Impact: 34.6), `createController` (Impact: 15.9), `destroy` (Impact: 13.1)

### 4. `package/esm/ReadableStream.js` (JAVASCRIPT) -> Cumulative Risk: **732.82**
- **Archetype:** `file_cluster_4` (Distance: 12.952 IQR)
- **Magnitude:** 331.8 | **LOC:** 242 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Concurrency (99.9911%), Tech Debt (98.1263%)
- **Heaviest Functions:** `constructor` (Impact: 34.6), `createController` (Impact: 15.9), `once` (Impact: 13.4)

### 5. `package/esm/TransformStream.js` (JAVASCRIPT) -> Cumulative Risk: **675.21**
- **Archetype:** `file_cluster_13` (Distance: 12.492 IQR)
- **Magnitude:** 105.0 | **LOC:** 76 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9136%), Documentation (90.1191%)
- **Heaviest Functions:** `constructor` (Impact: 24.5), `write` (Impact: 12.9), `final` (Impact: 9.4)

### 6. `package/cjs/TransformStream.js` (JAVASCRIPT) -> Cumulative Risk: **673.23**
- **Archetype:** `file_cluster_13` (Distance: 12.289 IQR)
- **Magnitude:** 104.08 | **LOC:** 80 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (98.9599%), Documentation (92.0154%)
- **Heaviest Functions:** `constructor` (Impact: 24.5), `write` (Impact: 12.9), `final` (Impact: 9.4)

### 7. `package/cjs/Body.js` (JAVASCRIPT) -> Cumulative Risk: **620.13**
- **Archetype:** `file_cluster_13` (Distance: 14.025 IQR)
- **Magnitude:** 360.3 | **LOC:** 530 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.5962%), Concurrency (89.66%)
- **Heaviest Functions:** `handleContentLengthHeader` (Impact: 21.2), `formData` (Impact: 14.2), `blob` (Impact: 12.8)

### 8. `package/esm/Body.js` (JAVASCRIPT) -> Cumulative Risk: **619.83**
- **Archetype:** `file_cluster_13` (Distance: 14.036 IQR)
- **Magnitude:** 362.24 | **LOC:** 526 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.6446%), Concurrency (90.12%)
- **Heaviest Functions:** `handleContentLengthHeader` (Impact: 21.2), `formData` (Impact: 14.2), `blob` (Impact: 12.8)

### 9. `package/esm/utils.js` (JAVASCRIPT) -> Cumulative Risk: **613.26**
- **Archetype:** `file_cluster_0` (Distance: 13.616 IQR)
- **Magnitude:** 110.0 | **LOC:** 111 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.6439%), Tech Debt (96.4066%), Safety Score (80.0%)
- **Heaviest Functions:** `getHeadersObj` (Impact: 10.9), `getSupportedFormats` (Impact: 10.9), `cleanup` (Impact: 9.0)

### 10. `package/cjs/TextEncoderDecoder.js` (JAVASCRIPT) -> Cumulative Risk: **607.19**
- **Archetype:** `file_cluster_8` (Distance: 10.917 IQR)
- **Magnitude:** 44.68 | **LOC:** 50 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9953%), Tech Debt (99.9837%), Documentation (93.3248%)
- **Heaviest Functions:** `constructor` (Impact: 7.3), `decode` (Impact: 4.7), `constructor` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/esm/Body.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.036 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.732 IQR)
- **Top Global Matches:** file_cluster_13: 14.036, file_cluster_4: 14.072, file_cluster_11: 14.15
- **Magnitude:** 362.24 | **LOC:** 526 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.5059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleContentLengthHeader` (Impact: 21.2)
  * `formData` (Impact: 14.2)
  * `blob` (Impact: 12.8)
  * `_doCollectChunksFromReadableJob` (Impact: 11.9)
  * `body` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 54`, `args: 24`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 234`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 14`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, Blob.js, utils.js, busboy, promise-helpers, File.js, FormData.js, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Body.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.025 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.908 IQR)
- **Top Global Matches:** file_cluster_13: 14.025, file_cluster_4: 14.074, file_cluster_11: 14.128
- **Magnitude:** 360.3 | **LOC:** 530 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.3208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleContentLengthHeader` (Impact: 21.2)
  * `formData` (Impact: 14.2)
  * `blob` (Impact: 12.8)
  * `_doCollectChunksFromReadableJob` (Impact: 11.9)
  * `body` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 44`, `args: 24`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 232`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 14`, `doc: 1`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, Blob.js, utils.js, busboy, promise-helpers, File.js, FormData.js, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/ReadableStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.952 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.917 IQR)
- **Top Global Matches:** file_cluster_4: 12.952, file_cluster_13: 13.241, file_cluster_8: 13.306
- **Magnitude:** 331.8 | **LOC:** 242 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.7027%), Tech Debt (98.1263%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 34.6)
  * `createController` (Impact: 15.9)
  * `once` (Impact: 13.4)
  * `destroy` (Impact: 13.1)
  * `handleStart` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 78`, `args: 44`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 92`, `duplicate_logic: 6`
* *Architecture:* `api: 6`, `concurrency: 37`, `import: 6`
* *Defense:* `safety: 20`, `immutability_locks: 14`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, node:events, promises, promise-helpers, node:stream, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/ReadableStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.941 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_4: 12.941, file_cluster_13: 13.14, file_cluster_8: 13.204
- **Magnitude:** 309.48 | **LOC:** 246 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.4296%), Tech Debt (97.9214%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 34.6)
  * `createController` (Impact: 15.9)
  * `destroy` (Impact: 13.1)
  * `handleStart` (Impact: 9.4)
  * `getReader` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 71`, `args: 44`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 92`, `duplicate_logic: 6`
* *Architecture:* `api: 7`, `concurrency: 27`, `import: 6`
* *Defense:* `safety: 20`, `immutability_locks: 20`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, node:events, promises, promise-helpers, node:stream, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Request.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.424 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.978 IQR)
- **Top Global Matches:** file_cluster_13: 14.424, file_cluster_11: 14.641, file_cluster_8: 14.698
- **Magnitude:** 280.16 | **LOC:** 129 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.1783%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 96.7)
  * `super` (Impact: 32.1)
  * `url` (Impact: 7.5)
  * `parsedUrl` (Impact: 7.5)
  * `signal` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 13`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 117`
* *Architecture:* `io: 5`, `api: 6`, `import: 5`
* *Defense:* `safety: 26`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, URL.js, Body.js, Headers.js, node:https
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Request.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.482 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.657 IQR)
- **Top Global Matches:** file_cluster_13: 14.482, file_cluster_11: 14.73, file_cluster_17: 14.739
- **Magnitude:** 279.08 | **LOC:** 125 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.9379%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 96.7)
  * `super` (Impact: 32.1)
  * `url` (Impact: 7.5)
  * `parsedUrl` (Impact: 7.5)
  * `signal` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 19`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 117`
* *Architecture:* `io: 5`, `api: 5`, `import: 5`
* *Defense:* `safety: 26`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, URL.js, Body.js, Headers.js, node:https
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Headers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.128 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.174 IQR)
- **Top Global Matches:** file_cluster_13: 14.128, file_cluster_17: 14.183, file_cluster_8: 14.2
- **Magnitude:** 199.5 | **LOC:** 310 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.1607%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getMap` (Impact: 41.3)
    * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
  * `append` (Impact: 7.5)
  * `isHeadersLike` (Impact: 7.1)
  * `has` (Impact: 4.6)
  * `get` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 11`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 127`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IteratorObject.js, node:util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Headers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.207 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.103 IQR)
- **Top Global Matches:** file_cluster_13: 14.207, file_cluster_17: 14.239, file_cluster_8: 14.288
- **Magnitude:** 198.4 | **LOC:** 305 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.3691%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getMap` (Impact: 41.3)
    * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
  * `append` (Impact: 7.5)
  * `isHeadersLike` (Impact: 7.1)
  * `has` (Impact: 4.6)
  * `get` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 15`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 127`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IteratorObject.js, node:util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/FormData.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.95 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.072 IQR)
- **Top Global Matches:** file_cluster_13: 11.95, file_cluster_8: 11.968, file_cluster_11: 12.134
- **Magnitude:** 183.78 | **LOC:** 151 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.5748%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getStreamFromFormData` (Impact: 32.6)
  * `handleNextEntry` (Impact: 15.3)
  * `pull` (Impact: 11.4)
  * `cancel` (Impact: 8.9)
  * `append` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 34`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 52`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 7`, `immutability_locks: 14`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IteratorObject.js, node:buffer, ReadableStream.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/FormData.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.988 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.001 IQR)
- **Top Global Matches:** file_cluster_13: 11.988, file_cluster_8: 12.016, file_cluster_11: 12.193
- **Magnitude:** 183.68 | **LOC:** 146 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.5562%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getStreamFromFormData` (Impact: 32.6)
  * `handleNextEntry` (Impact: 15.3)
  * `pull` (Impact: 11.4)
  * `cancel` (Impact: 8.9)
  * `append` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 39`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 7`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IteratorObject.js, node:buffer, ReadableStream.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/fetchNodeHttp.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.048 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.149 IQR)
- **Top Global Matches:** file_cluster_13: 10.048, file_cluster_8: 10.189, file_cluster_0: 10.554
- **Magnitude:** 164.9 | **LOC:** 152 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8646%), Tech Debt (99.9604%)
**Top Internal Functions/Classes:**
  * `fetchNodeHttp` (Impact: 91.5)
  * `handleMaybePromise` (Impact: 11.1)
  * `getRequestFnForProtocol` (Impact: 9.1)
  * `reject` (Impact: 5.9)
  * `onError` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 28`, `args: 10`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `duplicate_logic: 6`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 6`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, utils.js, URL.js, node:zlib, promise-helpers, Request.js, Response.js, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/fetchCurl.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.881 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.777 IQR)
- **Top Global Matches:** file_cluster_8: 10.881, file_cluster_13: 10.9, file_cluster_0: 11.187
- **Magnitude:** 151.88 | **LOC:** 140 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.3787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchCurl` (Impact: 77.7)
  * `streamListener` (Impact: 21.6)
  * `errorListener` (Impact: 14.7)
  * `onAbort` (Impact: 7.4)
  * `endListener` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 17`, `args: 10`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 16`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, promise-helpers, Response.js, node:stream, node:tls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/fetchNodeHttp.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.022 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.273 IQR)
- **Top Global Matches:** file_cluster_13: 10.022, file_cluster_8: 10.178, file_cluster_11: 10.52
- **Magnitude:** 151.58 | **LOC:** 156 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.1497%), Tech Debt (98.6851%)
**Top Internal Functions/Classes:**
  * `fetchNodeHttp` (Impact: 101.9)
  * `getRequestFnForProtocol` (Impact: 9.1)
  * `reject` (Impact: 5.9)
  * `onError` (Impact: 5.6)
  * `reject` (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 18`, `args: 10`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `duplicate_logic: 4`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 6`, `immutability_locks: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, utils.js, URL.js, node:zlib, promise-helpers, Request.js, tslib, Response.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/fetchCurl.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.844 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.939 IQR)
- **Top Global Matches:** file_cluster_8: 10.844, file_cluster_13: 10.889, file_cluster_0: 11.181
- **Magnitude:** 148.54 | **LOC:** 143 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.2654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchCurl` (Impact: 77.7)
  * `streamListener` (Impact: 21.6)
  * `errorListener` (Impact: 14.7)
  * `onAbort` (Impact: 7.4)
  * `endListener` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 11`, `args: 10`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `api: 5`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 16`, `immutability_locks: 15`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, promise-helpers, Response.js, node:stream, node:tls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Response.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.66 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.012 IQR)
- **Top Global Matches:** file_cluster_13: 12.66, file_cluster_8: 12.739, file_cluster_11: 12.931
- **Magnitude:** 144.36 | **LOC:** 109 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.6853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `json` (Impact: 49.5)
  * `constructor` (Impact: 31.8)
  * `redirect` (Impact: 5.7)
  * `ok` (Impact: 3.6)
  * `error` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 10`, `args: 6`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 42`
* *Architecture:* `io: 1`, `api: 6`, `import: 3`
* *Defense:* `safety: 14`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Body.js, node:http, Headers.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Response.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.718 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.817 IQR)
- **Top Global Matches:** file_cluster_13: 12.718, file_cluster_8: 12.801, file_cluster_0: 13.016
- **Magnitude:** 143.28 | **LOC:** 105 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.3675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `json` (Impact: 49.5)
  * `constructor` (Impact: 31.8)
  * `redirect` (Impact: 5.7)
  * `ok` (Impact: 3.6)
  * `error` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 14`, `args: 6`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 42`
* *Architecture:* `io: 1`, `api: 5`, `import: 3`
* *Defense:* `safety: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Body.js, node:http, Headers.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/IteratorObject.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.767 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.023 IQR)
- **Top Global Matches:** file_cluster_13: 11.767, file_cluster_8: 11.844, file_cluster_0: 11.986
- **Magnitude:** 141.08 | **LOC:** 135 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.6136%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `flatMap` (Impact: 9.4)
  * `take` (Impact: 6.2)
  * `filter` (Impact: 4.7)
  * `drop` (Impact: 4.7)
  * `some` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 38`, `args: 16`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 72`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, node:util, disposablestack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/IteratorObject.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.802 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.966 IQR)
- **Top Global Matches:** file_cluster_13: 11.802, file_cluster_8: 11.875, file_cluster_17: 12.021
- **Magnitude:** 140.0 | **LOC:** 131 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.9974%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `flatMap` (Impact: 9.4)
  * `take` (Impact: 6.2)
  * `filter` (Impact: 4.7)
  * `drop` (Impact: 4.7)
  * `some` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 42`, `args: 16`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, node:util, disposablestack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/WritableStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.168 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.553 IQR)
- **Top Global Matches:** file_cluster_4: 12.168, file_cluster_13: 12.267, file_cluster_8: 12.396
- **Magnitude:** 135.5 | **LOC:** 112 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.78%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 21.0)
  * `write` (Impact: 12.9)
  * `getWriter` (Impact: 8.9)
  * `final` (Impact: 6.3)
  * `close` (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 29`, `args: 23`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `duplicate_logic: 12`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 8`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:events, utils.js, node:stream, promise-helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/WritableStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.015 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.591 IQR)
- **Top Global Matches:** file_cluster_4: 12.015, file_cluster_13: 12.095, file_cluster_8: 12.209
- **Magnitude:** 134.58 | **LOC:** 116 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.5596%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 21.0)
  * `write` (Impact: 12.9)
  * `getWriter` (Impact: 8.9)
  * `final` (Impact: 6.3)
  * `close` (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 24`, `args: 23`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `duplicate_logic: 12`
* *Architecture:* `api: 8`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 12`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:events, utils.js, node:stream, promise-helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.616 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.259 IQR)
- **Top Global Matches:** file_cluster_0: 13.616, file_cluster_13: 13.7, file_cluster_17: 13.709
- **Magnitude:** 110.0 | **LOC:** 111 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.1539%), Tech Debt (96.4066%)
**Top Internal Functions/Classes:**
  * `getHeadersObj` (Impact: 10.9)
  * `getSupportedFormats` (Impact: 10.9)
  * `cleanup` (Impact: 9.0)
  * `shouldRedirect` (Impact: 8.8)
  * `isArrayBufferView` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 32`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 8`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 22`, `import: 3`
* *Defense:* `safety: 16`, `immutability_locks: 6`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:events, node:signal, node:zlib, promise-helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.205 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.115 IQR)
- **Top Global Matches:** file_cluster_0: 13.205, file_cluster_13: 13.209, file_cluster_11: 13.261
- **Magnitude:** 105.7 | **LOC:** 126 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.1813%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `getSupportedFormats` (Impact: 12.6)
  * `getHeadersObj` (Impact: 10.9)
  * `cleanup` (Impact: 9.0)
  * `shouldRedirect` (Impact: 8.8)
  * `isArrayBufferView` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 20`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `safety: 16`, `immutability_locks: 8`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:signal, node:events, node:zlib, promise-helpers, tslib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/TransformStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.492 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.09 IQR)
- **Top Global Matches:** file_cluster_13: 12.492, file_cluster_4: 12.608, file_cluster_8: 12.694
- **Magnitude:** 105.0 | **LOC:** 76 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.9279%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 24.5)
  * `write` (Impact: 12.9)
  * `final` (Impact: 9.4)
  * `callback` (Impact: 2.5)
  * `callback` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 11`, `args: 12`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `duplicate_logic: 7`
* *Architecture:* `api: 9`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 9`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, WritableStream.js, utils.js, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/TransformStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.289 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.203 IQR)
- **Top Global Matches:** file_cluster_13: 12.289, file_cluster_4: 12.452, file_cluster_8: 12.463
- **Magnitude:** 104.08 | **LOC:** 80 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.8489%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 24.5)
  * `write` (Impact: 12.9)
  * `final` (Impact: 9.4)
  * `callback` (Impact: 2.5)
  * `callback` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 6`, `args: 12`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `duplicate_logic: 7`
* *Architecture:* `api: 10`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 9`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, WritableStream.js, utils.js, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Blob.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.911 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.794 IQR)
- **Top Global Matches:** file_cluster_13: 11.911, file_cluster_8: 11.95, file_cluster_7: 12.384
- **Magnitude:** 69.66 | **LOC:** 280 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.8204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBlobPartAsBuffer` (Impact: 12.8)
  * `hasBufferMethod` (Impact: 5.3)
  * `hasArrayBufferMethod` (Impact: 5.3)
  * `hasBytesMethod` (Impact: 5.3)
  * `hasTextMethod` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 23`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 15`
* *Architecture:* `api: 17`, `import: 3`
* *Defense:* `safety: 15`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, node:buffer, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/cjs/utils.js` (JAVASCRIPT) | Magnitude: 105.7 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, branch: 32, structural_boundaries: 20, args: 18
- `package/esm/utils.js` (JAVASCRIPT) | Magnitude: 110.0 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 32, branch: 31, api: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/cjs/FormData.js` (JAVASCRIPT) | Magnitude: 183.78 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, state_mutation: 52, structural_boundaries: 34, branch: 29
- `package/esm/FormData.js` (JAVASCRIPT) | Magnitude: 183.68 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, state_mutation: 52, structural_boundaries: 39, branch: 29
- `package/esm/Headers.js` (JAVASCRIPT) | Magnitude: 198.4 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 127, indent_spaces: 99, branch: 35, structural_boundaries: 15
- `package/esm/Body.js` (JAVASCRIPT) | Magnitude: 362.24 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 234, indent_spaces: 194, structural_boundaries: 54, branch: 43
- `package/esm/Blob.js` (JAVASCRIPT) | Magnitude: 69.66 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 23, indent_spaces: 21, branch: 20, api: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/typings/AbortError.d.cts` (TYPESCRIPT) | Magnitude: 3.77 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, func_start: 2, indent_spaces: 2
- `package/typings/AbortError.d.ts` (TYPESCRIPT) | Magnitude: 3.77 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, func_start: 2, indent_spaces: 2
- `package/typings/Response.d.cts` (TYPESCRIPT) | Magnitude: 25.21 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, branch: 8, generics: 7
- `package/typings/Response.d.ts` (TYPESCRIPT) | Magnitude: 25.21 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, branch: 8, generics: 7
- `package/typings/TransformStream.d.cts` (TYPESCRIPT) | Magnitude: 3.4 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, generics: 5, indent_spaces: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/typings/Body.d.cts` (TYPESCRIPT) | Magnitude: 1.53 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, ui_framework: 19, structural_boundaries: 16, branch: 15
- `package/typings/Body.d.ts` (TYPESCRIPT) | Magnitude: 1.53 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, ui_framework: 19, structural_boundaries: 16, branch: 15
- `package/typings/Blob.d.cts` (TYPESCRIPT) | Magnitude: 4.82 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 27, args: 23, func_start: 23
- `package/typings/Blob.d.ts` (TYPESCRIPT) | Magnitude: 4.82 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 27, args: 23, func_start: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/cjs/WritableStream.js` (JAVASCRIPT) | Magnitude: 134.58 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 24, args: 23, state_mutation: 23
- `package/esm/WritableStream.js` (JAVASCRIPT) | Magnitude: 135.5 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 29, state_mutation: 25, args: 23
- `package/cjs/ReadableStream.js` (JAVASCRIPT) | Magnitude: 309.48 | Delta: **0.199 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 222, state_mutation: 92, structural_boundaries: 71, branch: 49
- `package/esm/ReadableStream.js` (JAVASCRIPT) | Magnitude: 331.8 | Delta: **0.289 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 222, state_mutation: 92, structural_boundaries: 78, branch: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/esm/fetchCurl.js` (JAVASCRIPT) | Magnitude: 151.88 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, branch: 40, structural_boundaries: 17, safety: 16
- `package/typings/URLSearchParams.d.cts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, branch: 1, api: 1
- `package/typings/URLSearchParams.d.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, branch: 1, api: 1
- `package/cjs/fetchCurl.js` (JAVASCRIPT) | Magnitude: 148.54 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, branch: 40, safety: 16, immutability_locks: 15
- `package/typings/CompressionStream.d.cts` (TYPESCRIPT) | Magnitude: 1.93 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, api: 2, indent_spaces: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/esm/index.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/typings/index.d.cts` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/typings/index.d.ts` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/cjs/index.js` -> **Severity: 1063.795** (Blast Radius: 10.638 * Doc Risk: 99.9995%)
- `package/typings/utils.d.cts` -> **Severity: 1063.735** (Blast Radius: 10.638 * Doc Risk: 99.9939%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
