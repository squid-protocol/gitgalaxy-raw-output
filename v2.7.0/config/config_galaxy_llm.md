# ARCHITECTURAL_BRIEF: config
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
| Analyzed Artifacts (Scanned) | 12 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 321 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 85.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4 | 272 | 33.3% |
| TYPESCRIPT | 4 | 34 | 33.3% |
| MARKDOWN | 2 | 0 | 16.7% |
| PLAINTEXT | 1 | 0 | 8.3% |
| JSON | 1 | 15 | 8.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9 | 75.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 25.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgz`: 1x Excluded (Explicitly Denied Extension: '.tgz')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 50.0 | 9.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.2 | 52.0 | 63.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 39.3 | 50.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 11.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 34.1 | 8.9 | 5.6 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 77.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 25.0 | 3.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2 | 2 | 1 | `package/async.js` |
| cleanup | 0 | 0 | 0 | - |
| guards | 26 | 2 | 6 | `package/parser.js` |
| danger | 6 | 4 | 2 | `package/async.js` |
| concurrency | 13 | 2 | 4 | `package/async.js` |
| connectivity | 37 | 8 | 5 | `package/types/parser.d.ts` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 1 | 0 | `package/parser.js` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 58 | 7 | 21 | `package/parser.js` |
| debt | 2 | 1 | 0 | `package/parser.js` |
| mutation | 105 | 5 | 16 | `package/parser.js` |
| dead_code | 28 | 5 | 5 | `package/types/parser.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 2 | 1 | 0 | `package/async.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/History.md` (Hits: 0)
- `package/README.md` (Hits: 0)
- `package/async.js` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **defer.js** (`package/defer.js`) — 3 inbound connections
2. **History.md** (`package/History.md`) — 0 inbound connections
3. **README.md** (`package/README.md`) — 0 inbound connections
4. **async.js** (`package/async.js`) — 0 inbound connections
5. **parser.js** (`package/parser.js`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **async.js** (`package/async.js`) — 4 outbound dependencies
2. **defer.js** (`package/defer.js`) — 3 outbound dependencies
3. **parser.js** (`package/parser.js`) — 3 outbound dependencies
4. **async.d.ts** (`package/types/async.d.ts`) — 3 outbound dependencies
5. **defer.d.ts** (`package/types/defer.d.ts`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `tsParser` (@ `package/parser.js`) -> Impact: **13.3** | LOC: 23
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
- `yamlParser` (@ `package/parser.js`) -> Impact: **13.1** | LOC: 20
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object | undefined} */
- `resolveAsyncConfigs` (@ `package/async.js`) -> Impact: **11.2** | LOC: 27
  * *Intent:* /** * Do not use `config.get` before executing this method, it will freeze the config object. * @param {Config} config the main config object, returne...
- `iterate` (@ `package/async.js`) -> Impact: **10.8** | LOC: 19
- `setFilesOrder` (@ `package/parser.js`) -> Impact: **9.3** | LOC: 13
  * *Intent:* /** * @param {string|string[]} name * @param {number=} newIndex * @returns {string[]} */
- `jsParser` (@ `package/parser.js`) -> Impact: **9.1** | LOC: 8
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
- `coffeeParser` (@ `package/parser.js`) -> Impact: **6.7** | LOC: 31
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
- `xmlParser` (@ `package/parser.js`) -> Impact: **5.8** | LOC: 12
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
- `csonParser` (@ `package/parser.js`) -> Impact: **5.7** | LOC: 10
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
- `asyncConfig` (@ `package/async.js`) -> Impact: **5.6** | LOC: 28
  * *Intent:* /** * @template T * @overload * @param {(config: Config, original: any) => Promise<T>} promiseOrFunc * @returns {DeferredConfig} */ /** * @template T ...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package` | 8 | 356.12 | 10.48% | 19.2% |
| `package/types` | 4 | 4.53 | 0.63% | 50.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/types/parser.d.ts` -> **100.0%** Exposure
- `package/parser.js` -> **89.6986%** Exposure
- `package/async.js` -> **63.8804%** Exposure
- `package/types/async.d.ts` -> **50.0%** Exposure
- `package/types/raw.d.ts` -> **50.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/parser.js` -> **100.0%** Exposure
- `package/async.js` -> **99.9982%** Exposure
- `package/defer.js` -> **31.0026%** Exposure
- `package/raw.js` -> **31.0026%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/types/parser.d.ts` -> **20** Orphaned Functions | **0** Duplicates
- `package/parser.js` -> **5** Orphaned Functions | **0** Duplicates
- `package/async.js` -> **1** Orphaned Functions | **0** Duplicates
- `package/types/async.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/types/raw.d.ts` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/async.js` (JAVASCRIPT) -> Cumulative Risk: **576.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 95.84 | **LOC:** 92 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9982%), Safety Score (80.0115%)
- **Heaviest Functions:** `resolveAsyncConfigs` (Impact: 11.2), `iterate` (Impact: 10.8), `asyncConfig` (Impact: 5.6)

### 2. `package/parser.js` (JAVASCRIPT) -> Cumulative Risk: **543.46**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 212.92 | **LOC:** 385 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (89.6986%), Safety Score (85.2437%)
- **Heaviest Functions:** `tsParser` (Impact: 13.3), `yamlParser` (Impact: 13.1), `setFilesOrder` (Impact: 9.3)

### 3. `package/types/async.d.ts` (TYPESCRIPT) -> Cumulative Risk: **359.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.68 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (90.6079%), Safety Score (57.7583%), Tech Debt (50.0%)
- **Heaviest Functions:** `asyncConfig` (Impact: 1.5), `asyncConfig` (Impact: 1.5), `resolveAsyncConfigs` (Impact: 1.5)

### 4. `package/types/parser.d.ts` (TYPESCRIPT) -> Cumulative Risk: **318.06**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2.98 | **LOC:** 133 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Safety Score (50.1071%), Stability (50.0%)
- **Heaviest Functions:** `setFilesOrder` (Impact: 3.5), `getFilesOrder` (Impact: 2.9), `parse` (Impact: 1.8)

### 5. `package/defer.js` (JAVASCRIPT) -> Cumulative Risk: **283.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 6.14 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (65.7332%), Stability (50.0%), Api Exposure (34.0809%)
- **Heaviest Functions:** `deferConfig` (Impact: 2.0)

### 6. `package/types/raw.d.ts` (TYPESCRIPT) -> Cumulative Risk: **271.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.19 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (63.7774%), Tech Debt (50.0%), Stability (50.0%)
- **Heaviest Functions:** `raw` (Impact: 1.6)

### 7. `package/raw.js` (JAVASCRIPT) -> Cumulative Risk: **254.26**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 5.84 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (65.3461%), Stability (50.0%), State Flux (31.0026%)
- **Heaviest Functions:** `raw` (Impact: 1.7)

### 8. `package/types/defer.d.ts` (TYPESCRIPT) -> Cumulative Risk: **57.89**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.68 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Api Exposure (5.5883%), Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/parser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 212.92 | **LOC:** 385 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.8095%), Tech Debt (89.6986%)
**Top Internal Functions/Classes:**
  * `tsParser` (Impact: 13.3)
    * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
  * `yamlParser` (Impact: 13.1)
    * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object | undefined} */
  * `setFilesOrder` (Impact: 9.3)
    * *Intent:* /** * @param {string|string[]} name * @param {number=} newIndex * @returns {string[]} */
  * `jsParser` (Impact: 9.1)
    * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
  * `coffeeParser` (Impact: 6.7)
    * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 38`, `args: 21`, `func_start: 21`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`, `import: 15`
* *Defense:* `safety: 20`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` coffee-script, iced-coffee-script, json5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/async.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 95.84 | **LOC:** 92 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9946%), Tech Debt (63.8804%)
**Top Internal Functions/Classes:**
  * `resolveAsyncConfigs` (Impact: 11.2)
    * *Intent:* /** * Do not use `config.get` before executing this method, it will freeze the config object. * @par...
  * `iterate` (Impact: 10.8)
  * `asyncConfig` (Impact: 5.6)
    * *Intent:* /** * @template T * @overload * @param {(config: Config, original: any) => Promise<T>} promiseOrFunc...
  * `prepare` (Impact: 4.5)
  * `registerRelease` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 16`, `args: 13`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 6`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` defer, config, util.js, config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/History.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 14.22 | **LOC:** 711 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/defer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6.14 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deferConfig` (Impact: 2.0)
    * *Intent:* /** * @deprecated please use the new callback mechanism * @see lib/defer.js * @type {typeof import('...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 243.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.272727
  * `Imports (Out-Degree: 0):` defer, defer.js, util.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/raw.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.84 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `raw` (Impact: 1.7)
    * *Intent:* /** * @param {any} rawObj * @returns {RawConfig & { resolve: () => any }} */
**Contextual Mitigations & Amplifications:**
* *Amplified Sql Injection:* 1 instances
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 3.66 | **LOC:** 183 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/parser.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2.98 | **LOC:** 133 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5108%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `setFilesOrder` (Impact: 3.5)
    * *Intent:* /** * @param {string|string[]} name * @param {number=} newIndex * @returns {string[]} */
  * `getFilesOrder` (Impact: 2.9)
    * *Intent:* /** * @param {string=} name * @returns {string[] | number} */
  * `parse` (Impact: 1.8)
    * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object | undefined} */
  * `xmlParser` (Impact: 1.8)
    * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
  * `jsParser` (Impact: 1.8)
    * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 24`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `unreferenced_by_name: 20`
* *Architecture:* `api: 21`
* *Defense:* `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.2 | **LOC:** 110 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/async.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 0.68 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `asyncConfig` (Impact: 1.5)
    * *Intent:* /** * @template T * @overload * @param {Promise<T>} promiseOrFunc * @returns {Promise<T>} */
  * `asyncConfig` (Impact: 1.5)
    * *Intent:* /** * @template T * @overload * @param {(config: Config, original: any) => Promise<T>} promiseOrFunc...
  * `resolveAsyncConfigs` (Impact: 1.5)
    * *Intent:* /** * Do not use `config.get` before executing this method, it will freeze the config object. * @par...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` defer, config, config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/defer.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 0.68 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` defer, defer.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/raw.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 0.19 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `raw` (Impact: 1.6)
    * *Intent:* /** * @param {any} rawObj * @returns {RawConfig & { resolve: () => any }} */
**Contextual Mitigations & Amplifications:**
* *Amplified Sql Injection:* 2 instances
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/defer.js` -> **Severity: 17.927** (Embedded: 0.2727 * Error Risk: 65.7332%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/async.js` -> **Severity: 1718.225** (Blast Radius: 68.729 * Doc Risk: 25.0%)
- `package/parser.js` -> **Severity: 163.644** (Blast Radius: 68.729 * Doc Risk: 2.381%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
