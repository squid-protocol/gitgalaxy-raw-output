# ARCHITECTURAL_BRIEF: pn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/pn` |
| **Timestamp** | `2026-08-07T05:16:22.486794+00:00` |
| **Scan Duration** | `0.1s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 36 malicious artifacts.

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
| Total Artifacts | 40 |
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 522 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.5% |
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
| JAVASCRIPT | 36 | 522 | 97.3% |
| PLAINTEXT | 1 | 0 | 2.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.034`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 28 | 75.7% |
| file_cluster_8 | 5 | 13.5% |
| file_cluster_4 | 3 | 8.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 2.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 149 LOC)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 100.0 | 22.9 | 5.0 | 5.0 |
| Error & Exception Exposure | 58.1 | 92.0 | 75.2 | 73.6 | 73.6 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 0.3 | 3.1 | 1.3 | 1.1 | 0.3 |
| API Exposure | 3.1 | 9.2 | 5.3 | 5.8 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| State Flux Exposure | 87.1 | 100.0 | 99.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 53.3 | 40.0 | 13.3 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 1.6 | 11.9 | 6.4 | 4.8 | 1.6 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/fs.js` (Hits: 155)
- `package/http.js` (Hits: 21)
- `package/child_process.js` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_promise.js** (`package/_promise.js`) — 0 inbound connections
2. **_promisify.js** (`package/_promisify.js`) — 0 inbound connections
3. **assert.js** (`package/assert.js`) — 0 inbound connections
4. **async_hooks.js** (`package/async_hooks.js`) — 0 inbound connections
5. **buffer.js** (`package/buffer.js`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **child_process.js** (`package/child_process.js`) — 2 outbound dependencies
2. **cluster.js** (`package/cluster.js`) — 2 outbound dependencies
3. **crypto.js** (`package/crypto.js`) — 2 outbound dependencies
4. **dgram.js** (`package/dgram.js`) — 2 outbound dependencies
5. **dns.js** (`package/dns.js`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `deferred` (@ `package/_promisify.js`) -> Impact: **16.5** | LOC: 19
  * *Intent:* // deferred gets its own scope to prevent inadvertent capture in the closure
- `resolve` (@ `package/_promisify.js`) -> Impact: **7.1** | LOC: 4
- `exports` (@ `package/_promisify.js`) -> Impact: **7.1** | LOC: 7
- `getOrSetPromise` (@ `package/_promise.js`) -> Impact: **3.7** | LOC: 4
- `bind` (@ `package/child_process.js`) -> Impact: **3.5** | LOC: 1
- `bind` (@ `package/cluster.js`) -> Impact: **3.5** | LOC: 1
- `bind` (@ `package/crypto.js`) -> Impact: **3.5** | LOC: 1
- `bind` (@ `package/dgram.js`) -> Impact: **3.5** | LOC: 1
- `bind` (@ `package/dns.js`) -> Impact: **3.5** | LOC: 1
- `bind` (@ `package/domain.js`) -> Impact: **3.5** | LOC: 1

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package` | 37 | 563.84 | 22.27% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest State Flux (Mutation/Volatility)
- `package/_promise.js` -> **100.0%** Exposure
- `package/_promisify.js` -> **100.0%** Exposure
- `package/assert.js` -> **100.0%** Exposure
- `package/async_hooks.js` -> **100.0%** Exposure
- `package/buffer.js` -> **100.0%** Exposure

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/async_hooks.js`** -> AI Confidence: **99.06%**
2. **`package/inspector.js`** -> AI Confidence: **99.06%**
3. **`package/perf_hooks.js`** -> AI Confidence: **99.06%**
4. **`package/punycode.js`** -> AI Confidence: **99.06%**
5. **`package/v8.js`** -> AI Confidence: **99.06%**
6. **`package/_promisify.js`** -> AI Confidence: **98.96%**
7. **`package/_promise.js`** -> AI Confidence: **98.85%**
8. **`package/http2.js`** -> AI Confidence: **98.85%**
9. **`package/assert.js`** -> AI Confidence: **98.84%**
10. **`package/buffer.js`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `33` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/_promisify.js` (JAVASCRIPT) -> Cumulative Risk: **563.74**
- **Archetype:** `file_cluster_4` (Distance: 12.54 IQR)
- **Magnitude:** 68.26 | **LOC:** 59 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9613%)
- **Heaviest Functions:** `deferred` (Impact: 16.5), `resolve` (Impact: 7.1), `exports` (Impact: 7.1)

### 2. `package/cluster.js` (JAVASCRIPT) -> Cumulative Risk: **536.02**
- **Archetype:** `file_cluster_13` (Distance: 13.574 IQR)
- **Magnitude:** 15.84 | **LOC:** 20 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (96.4226%), Concurrency (87.756%)
- **Heaviest Functions:** `bind` (Impact: 3.5)

### 3. `package/timers.js` (JAVASCRIPT) -> Cumulative Risk: **451.58**
- **Archetype:** `file_cluster_4` (Distance: 12.799 IQR)
- **Magnitude:** 19.78 | **LOC:** 15 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Concurrency (99.9972%), Spec Match (93.3333%), Safety Score (84.8205%)
- **Heaviest Functions:** `bind` (Impact: 3.5)

### 4. `package/readline.js` (JAVASCRIPT) -> Cumulative Risk: **440.88**
- **Archetype:** `file_cluster_13` (Distance: 11.29 IQR)
- **Magnitude:** 13.82 | **LOC:** 16 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (88.0797%), Safety Score (83.5484%)
- **Heaviest Functions:** `bind` (Impact: 3.5)

### 5. `package/http2.js` (JAVASCRIPT) -> Cumulative Risk: **437.69**
- **Archetype:** `file_cluster_13` (Distance: 13.248 IQR)
- **Magnitude:** 13.8 | **LOC:** 15 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (93.5031%), Safety Score (74.8113%)
- **Heaviest Functions:** `bind` (Impact: 3.5)

### 6. `package/http.js` (JAVASCRIPT) -> Cumulative Risk: **435.0**
- **Archetype:** `file_cluster_13` (Distance: 11.424 IQR)
- **Magnitude:** 13.88 | **LOC:** 20 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (84.3461%), Safety Score (81.7574%)
- **Heaviest Functions:** `bind` (Impact: 3.5)

### 7. `package/tls.js` (JAVASCRIPT) -> Cumulative Risk: **429.92**
- **Archetype:** `file_cluster_13` (Distance: 10.657 IQR)
- **Magnitude:** 13.94 | **LOC:** 22 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (81.0697%), Safety Score (80.1048%)
- **Heaviest Functions:** `bind` (Impact: 3.5)

### 8. `package/util.js` (JAVASCRIPT) -> Cumulative Risk: **384.65**
- **Archetype:** `file_cluster_8` (Distance: 9.459 IQR)
- **Magnitude:** 14.26 | **LOC:** 41 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9249%), Safety Score (73.275%), Stability (50.0%)
- **Heaviest Functions:** `bind` (Impact: 3.5)

### 9. `package/_promise.js` (JAVASCRIPT) -> Cumulative Risk: **380.31**
- **Archetype:** `file_cluster_4` (Distance: 11.883 IQR)
- **Magnitude:** 14.8 | **LOC:** 7 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Concurrency (99.9999%), Safety Score (77.9026%), Stability (50.0%)
- **Heaviest Functions:** `getOrSetPromise` (Impact: 3.7)

### 10. `package/crypto.js` (JAVASCRIPT) -> Cumulative Risk: **380.3**
- **Archetype:** `file_cluster_8` (Distance: 9.392 IQR)
- **Magnitude:** 14.54 | **LOC:** 53 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.0464%), Safety Score (69.2642%), Stability (50.0%)
- **Heaviest Functions:** `bind` (Impact: 3.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/_promisify.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.54 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.063 IQR)
- **Top Global Matches:** file_cluster_4: 12.54, file_cluster_13: 13.106, file_cluster_11: 13.184
- **Magnitude:** 68.26 | **LOC:** 59 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9613%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deferred` (Impact: 16.5)
    * *Intent:* // deferred gets its own scope to prevent inadvertent capture in the closure
  * `resolve` (Impact: 7.1)
  * `exports` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 14`, `args: 5`, `func_start: 3`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promise.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/timers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.799 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 7.379 IQR)
- **Top Global Matches:** file_cluster_4: 12.799, file_cluster_13: 12.963, file_cluster_8: 13.308
- **Magnitude:** 19.78 | **LOC:** 15 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `concurrency: 6`, `import: 2`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` timers, _promisify.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dns.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.288 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.051 IQR)
- **Top Global Matches:** file_cluster_8: 9.288, file_cluster_13: 9.699, file_cluster_7: 10.041
- **Magnitude:** 16.48 | **LOC:** 49 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5628%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, dns
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cluster.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.574 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 7.261 IQR)
- **Top Global Matches:** file_cluster_13: 13.574, file_cluster_4: 13.7, file_cluster_15: 13.701
- **Magnitude:** 15.84 | **LOC:** 20 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.4226%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 10`, `args: 13`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, cluster
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/async_hooks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.093 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_13: 15.093, file_cluster_17: 15.72, file_cluster_11: 15.732
- **Magnitude:** 15.56 | **LOC:** 3 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` async_hooks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/inspector.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.093 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_13: 15.093, file_cluster_17: 15.72, file_cluster_11: 15.732
- **Magnitude:** 15.56 | **LOC:** 3 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspector
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/perf_hooks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.093 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_13: 15.093, file_cluster_17: 15.72, file_cluster_11: 15.732
- **Magnitude:** 15.56 | **LOC:** 3 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` perf_hooks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/punycode.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.093 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_13: 15.093, file_cluster_17: 15.72, file_cluster_11: 15.732
- **Magnitude:** 15.56 | **LOC:** 3 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` punycode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/v8.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.093 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_13: 15.093, file_cluster_17: 15.72, file_cluster_11: 15.732
- **Magnitude:** 15.56 | **LOC:** 3 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v8
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/fs.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.591 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.385 IQR)
- **Top Global Matches:** file_cluster_8: 8.591, file_cluster_13: 9.195, file_cluster_7: 9.43
- **Magnitude:** 15.22 | **LOC:** 87 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.2987%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 155`, `api: 1`, `import: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/_promise.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.883 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.73 IQR)
- **Top Global Matches:** file_cluster_4: 11.883, file_cluster_8: 12.82, file_cluster_7: 13.248
- **Magnitude:** 14.8 | **LOC:** 7 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getOrSetPromise` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `concurrency: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/crypto.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.392 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.27 IQR)
- **Top Global Matches:** file_cluster_8: 9.392, file_cluster_13: 9.871, file_cluster_7: 10.191
- **Magnitude:** 14.54 | **LOC:** 53 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.2562%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 5`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/util.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.459 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.829 IQR)
- **Top Global Matches:** file_cluster_8: 9.459, file_cluster_13: 9.78, file_cluster_7: 10.235
- **Magnitude:** 14.26 | **LOC:** 41 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.4588%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.657 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.267 IQR)
- **Top Global Matches:** file_cluster_13: 10.657, file_cluster_8: 10.688, file_cluster_11: 11.309
- **Magnitude:** 13.94 | **LOC:** 22 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.0697%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, tls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/http.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.424 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.298 IQR)
- **Top Global Matches:** file_cluster_13: 11.424, file_cluster_8: 11.688, file_cluster_11: 11.811
- **Magnitude:** 13.88 | **LOC:** 20 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.3461%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 21`, `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http, _promisify.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/readline.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.29 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.596 IQR)
- **Top Global Matches:** file_cluster_13: 11.29, file_cluster_8: 11.502, file_cluster_11: 11.886
- **Magnitude:** 13.82 | **LOC:** 16 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, readline
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/http2.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.248 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.705 IQR)
- **Top Global Matches:** file_cluster_13: 13.248, file_cluster_11: 13.495, file_cluster_8: 13.638
- **Magnitude:** 13.8 | **LOC:** 15 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.5031%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 5`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, http2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/net.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.584 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.747 IQR)
- **Top Global Matches:** file_cluster_13: 11.584, file_cluster_8: 11.867, file_cluster_11: 12.154
- **Magnitude:** 13.78 | **LOC:** 17 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, net
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/child_process.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.723 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.426 IQR)
- **Top Global Matches:** file_cluster_13: 12.723, file_cluster_11: 13.117, file_cluster_8: 13.175
- **Magnitude:** 13.76 | **LOC:** 14 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 17`, `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/https.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.664 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.949 IQR)
- **Top Global Matches:** file_cluster_13: 12.664, file_cluster_11: 12.972, file_cluster_8: 13.183
- **Magnitude:** 13.72 | **LOC:** 11 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 12`, `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, https
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/stream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.112 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.036 IQR)
- **Top Global Matches:** file_cluster_13: 12.112, file_cluster_8: 12.512, file_cluster_11: 12.646
- **Magnitude:** 13.72 | **LOC:** 14 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/domain.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.092 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.956 IQR)
- **Top Global Matches:** file_cluster_13: 13.092, file_cluster_11: 13.466, file_cluster_8: 13.579
- **Magnitude:** 13.68 | **LOC:** 10 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, domain
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dgram.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.2 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_13: 13.2, file_cluster_11: 13.665, file_cluster_8: 13.795
- **Magnitude:** 13.64 | **LOC:** 8 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _promisify.js, dgram
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/assert.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.458 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.308 IQR)
- **Top Global Matches:** file_cluster_13: 11.458, file_cluster_8: 12.136, file_cluster_7: 12.662
- **Magnitude:** 13.04 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/buffer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.633 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.384 IQR)
- **Top Global Matches:** file_cluster_13: 10.633, file_cluster_8: 11.361, file_cluster_7: 11.92
- **Magnitude:** 13.04 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/tls.js` (JAVASCRIPT) | Magnitude: 13.94 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, state_mutation: 9, structural_boundaries: 4, import: 2
- `package/cluster.js` (JAVASCRIPT) | Magnitude: 15.84 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: ipc_rpc_bridges: 25, args: 13, closures: 13, indent_spaces: 12
- `package/readline.js` (JAVASCRIPT) | Magnitude: 13.82 | Delta: **0.212 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 9, structural_boundaries: 4, import: 2
- `package/http2.js` (JAVASCRIPT) | Magnitude: 13.8 | Delta: **0.247 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 9, structural_boundaries: 5, branch: 3
- `package/http.js` (JAVASCRIPT) | Magnitude: 13.88 | Delta: **0.264 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 21, indent_spaces: 14, state_mutation: 9, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/timers.js` (JAVASCRIPT) | Magnitude: 19.78 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 9, time_date_logic: 8, concurrency: 6
- `package/_promisify.js` (JAVASCRIPT) | Magnitude: 68.26 | Delta: **0.566 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 22, indent_spaces: 22, structural_boundaries: 14, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/process.js` (JAVASCRIPT) | Magnitude: 11.64 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 53, args: 45, closures: 45, structural_boundaries: 25
- `package/util.js` (JAVASCRIPT) | Magnitude: 14.26 | Delta: **0.321 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 9, structural_boundaries: 4, import: 2
- `package/dns.js` (JAVASCRIPT) | Magnitude: 16.48 | Delta: **0.411 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 11, structural_boundaries: 4, import: 2
- `package/crypto.js` (JAVASCRIPT) | Magnitude: 14.54 | Delta: **0.479 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, state_mutation: 9, structural_boundaries: 6, args: 5
- `package/fs.js` (JAVASCRIPT) | Magnitude: 15.22 | Delta: **0.604 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: io: 155, indent_spaces: 81, state_mutation: 9, structural_boundaries: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/_promisify.js` -> **Severity: 322.17** (Blast Radius: 27.027 * Doc Risk: 11.9203%)
- `package/cluster.js` -> **Severity: 322.17** (Blast Radius: 27.027 * Doc Risk: 11.9203%)
- `package/crypto.js` -> **Severity: 322.17** (Blast Radius: 27.027 * Doc Risk: 11.9203%)
- `package/dns.js` -> **Severity: 322.17** (Blast Radius: 27.027 * Doc Risk: 11.9203%)
- `package/fs.js` -> **Severity: 322.17** (Blast Radius: 27.027 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
