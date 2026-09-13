# ARCHITECTURAL_BRIEF: rollup-plugin-node-builtins
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
| Total Artifacts | 33 |
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 4730 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3574 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0342 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.15 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 28 | 4702 | 90.3% |
| JSON | 1 | 28 | 3.2% |
| PLAINTEXT | 1 | 0 | 3.2% |
| MARKDOWN | 1 | 0 | 3.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 29 | 93.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 6.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 67.7 | 89.0 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 68.0 | 79.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 37.2 | 2.7 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 72.6 | 21.7 | 12.2 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 80.4 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 5.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 86.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 82.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 9 | 4 | 1 | `package/src/es6/util.js` |
| cleanup | 12 | 3 | 0 | `package/src/es6/timers.js` |
| guards | 440 | 23 | 45 | `package/src/es6/readable-stream/readable.js` |
| danger | 81 | 16 | 8 | `package/src/es6/zlib.js` |
| concurrency | 44 | 4 | 1 | `package/src/es6/timers.js` |
| connectivity | 184 | 28 | 16 | `package/src/es6/zlib.js` |
| io | 6 | 2 | 0 | `package/src/index.js` |
| crypto | 1 | 1 | 0 | `package/src/index.js` |
| ipc | 8 | 2 | 0 | `package/src/es6/setimmediate.js` |
| time | 32 | 3 | 0 | `package/src/es6/timers.js` |
| serialization | 3 | 1 | 0 | `package/src/es6/util.js` |
| regex | 43 | 8 | 3 | `package/src/es6/url.js` |
| events | 145 | 10 | 12 | `package/src/es6/readable-stream/readable.js` |
| tests | 14 | 1 | 0 | `package/src/es6/assert.js` |
| docs | 23 | 2 | 0 | `package/src/es6/punycode.js` |
| debt | 19 | 8 | 2 | `package/src/es6/readable-stream/readable.js` |
| mutation | 1842 | 25 | 157 | `package/src/es6/url.js` |
| dead_code | 52 | 14 | 5 | `package/src/es6/readable-stream/readable.js` |
| credential | 0 | 0 | 0 | - |
| threat | 190 | 21 | 15 | `package/src/es6/events.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **4.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/index.js` (Hits: 4)
- `package/src/es6/path.js` (Hits: 2)
- `package/.eslintrc` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.js** (`package/src/es6/util.js`) — 9 inbound connections
2. **events.js** (`package/src/es6/events.js`) — 4 inbound connections
3. **duplex.js** (`package/src/es6/readable-stream/duplex.js`) — 4 inbound connections
4. **inherits.js** (`package/src/es6/inherits.js`) — 2 inbound connections
5. **readable.js** (`package/src/es6/readable-stream/readable.js`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **stream.js** (`package/src/es6/stream.js`) — 7 outbound dependencies
2. **readable.js** (`package/src/es6/readable-stream/readable.js`) — 6 outbound dependencies
3. **writable.js** (`package/src/es6/readable-stream/writable.js`) — 5 outbound dependencies
4. **duplex.js** (`package/src/es6/readable-stream/duplex.js`) — 4 outbound dependencies
5. **url.js** (`package/src/es6/url.js`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse` (@ `package/src/es6/url.js`) -> Impact: **178.5** | LOC: 260
- `resolveObject` (@ `package/src/es6/url.js`) -> Impact: **174.6** | LOC: 268
- `_deepEqual` (@ `package/src/es6/assert.js`) -> Impact: **77.0** | LOC: 65
- `readableAddChunk` (@ `package/src/es6/readable-stream/readable.js`) -> Impact: **75.8** | LOC: 47
- `formatValue` (@ `package/src/es6/util.js`) -> Impact: **71.5** | LOC: 111
- `Zlib` (@ `package/src/es6/zlib.js`) -> Impact: **65.5** | LOC: 98
  * *Intent:* // the Zlib class they all inherit from // This thing manages the queue of requests, and returns // true or false if there is anything in the queue wh...
- `formatProperty` (@ `package/src/es6/util.js`) -> Impact: **58.4** | LOC: 57
- `format` (@ `package/src/es6/url.js`) -> Impact: **53.7** | LOC: 55
- `_throws` (@ `package/src/es6/assert.js`) -> Impact: **48.8** | LOC: 37
- `read` (@ `package/src/es6/readable-stream/readable.js`) -> Impact: **47.4** | LOC: 99
  * *Intent:* // you can override either this method, or the async _read(n) below.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src/es6` | 20 | 4576.0 | 70.75% | 17.36% |
| `package/src/es6/readable-stream` | 6 | 1826.68 | 80.16% | 6.18% |
| `package/src` | 1 | 70.32 | 63.31% | 0.0% |
| `package` | 4 | 33.24 | 1.28% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/es6/domain.js` -> **99.9811%** Exposure
- `package/src/es6/timers.js` -> **84.1131%** Exposure
- `package/src/es6/os.js` -> **75.3696%** Exposure
- `package/src/es6/zlib.js` -> **37.2349%** Exposure
- `package/src/es6/string-decoder.js` -> **25.4029%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/es6/events.js` -> **100.0%** Exposure
- `package/src/es6/path.js` -> **100.0%** Exposure
- `package/src/es6/punycode.js` -> **100.0%** Exposure
- `package/src/es6/qs.js` -> **100.0%** Exposure
- `package/src/es6/readable-stream/buffer-list.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/es6/domain.js` -> **7** Orphaned Functions | **0** Duplicates
- `package/src/es6/zlib.js` -> **4** Orphaned Functions | **0** Duplicates
- `package/src/es6/os.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/src/es6/timers.js` -> **2** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `29` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/es6/zlib.js` (JAVASCRIPT) -> Cumulative Risk: **763.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 561.98 | **LOC:** 636 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Cognitive Load (98.7067%)
- **Heaviest Functions:** `Zlib` (Impact: 65.5), `_processChunk` (Impact: 37.2), `params` (Impact: 27.4)

### 2. `package/src/es6/readable-stream/readable.js` (JAVASCRIPT) -> Cumulative Risk: **694.44**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 997.26 | **LOC:** 897 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.2058%)
- **Heaviest Functions:** `readableAddChunk` (Impact: 75.8), `read` (Impact: 47.4), `pipe` (Impact: 44.7)

### 3. `package/src/es6/path.js` (JAVASCRIPT) -> Cumulative Risk: **686.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 198.16 | **LOC:** 235 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.3939%)
- **Heaviest Functions:** `relative` (Impact: 17.6), `normalizeArray` (Impact: 16.8), `resolve` (Impact: 10.4)

### 4. `package/src/es6/readable-stream/writable.js` (JAVASCRIPT) -> Cumulative Risk: **679.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 565.22 | **LOC:** 484 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.6893%)
- **Heaviest Functions:** `clearBuffer` (Impact: 23.6), `writeOrBuffer` (Impact: 23.4), `end` (Impact: 19.1)

### 5. `package/src/es6/url.js` (JAVASCRIPT) -> Cumulative Risk: **679.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1052.04 | **LOC:** 746 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.6519%)
- **Heaviest Functions:** `parse` (Impact: 178.5), `resolveObject` (Impact: 174.6), `format` (Impact: 53.7)

### 6. `package/src/es6/timers.js` (JAVASCRIPT) -> Cumulative Risk: **677.07**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 70.32 | **LOC:** 77 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%), Cognitive Load (97.6507%)
- **Heaviest Functions:** `clearInterval` (Impact: 6.0), `clearTimeout` (Impact: 6.0), `active` (Impact: 4.8)

### 7. `package/src/es6/util.js` (JAVASCRIPT) -> Cumulative Risk: **668.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 507.34 | **LOC:** 599 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Cognitive Load (93.8596%), Documentation (92.7711%)
- **Heaviest Functions:** `formatValue` (Impact: 71.5), `formatProperty` (Impact: 58.4), `format` (Impact: 21.6)

### 8. `package/src/es6/readable-stream/transform.js` (JAVASCRIPT) -> Cumulative Risk: **664.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 125.8 | **LOC:** 175 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.771%)
- **Heaviest Functions:** `afterTransform` (Impact: 13.1), `Transform` (Impact: 11.4), `_write` (Impact: 10.5)

### 9. `package/src/es6/string-decoder.js` (JAVASCRIPT) -> Cumulative Risk: **659.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 168.66 | **LOC:** 221 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.2974%)
- **Heaviest Functions:** `write` (Impact: 17.5), `detectIncompleteChar` (Impact: 14.3), `StringDecoder` (Impact: 12.9)

### 10. `package/src/es6/events.js` (JAVASCRIPT) -> Cumulative Risk: **652.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 560.96 | **LOC:** 476 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.6497%)
- **Heaviest Functions:** `removeListener` (Impact: 44.3), `_addListener` (Impact: 41.2), `emit` (Impact: 31.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/es6/url.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1052.04 | **LOC:** 746 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.2442%), Tech Debt (9.4444%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 178.5)
  * `resolveObject` (Impact: 174.6)
  * `format` (Impact: 53.7)
  * `urlParse` (Impact: 8.3)
  * `parseHost` (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 81`, `args: 14`, `func_start: 13`
* *Risk/State:* `state_mutation: 211`, `dead_code: 9`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.729
  * `Choke Point (Betweenness):` 0.003448 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 2):` punycode, querystring, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/readable-stream/readable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 997.26 | **LOC:** 897 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.0284%), Tech Debt (24.5937%)
**Top Internal Functions/Classes:**
  * `readableAddChunk` (Impact: 75.8)
  * `read` (Impact: 47.4)
    * *Intent:* // you can override either this method, or the async _read(n) below.
  * `pipe` (Impact: 44.7)
  * `wrap` (Impact: 28.4)
    * *Intent:* // wrap an old-style stream as the async data source. // This is *not* part of the readable stream i...
  * `howMuchToRead` (Impact: 21.6)
    * *Intent:* // This function is designed to be inlinable, so please take care when making // changes to the func...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 149 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 117`, `args: 54`, `func_start: 49`
* *Risk/State:* `state_mutation: 163`, `dead_code: 12`, `fragile_debt: 5`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.275
  * `Choke Point (Betweenness):` 0.008621 | `Ripple Effect (Closeness):` 0.109091
  * `Imports (Out-Degree: 4):` buffer-list, duplex, events, process, string_decoder, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/es6/readable-stream/writable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 565.22 | **LOC:** 484 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.1175%), Tech Debt (12.4968%)
**Top Internal Functions/Classes:**
  * `clearBuffer` (Impact: 23.6)
    * *Intent:* // if there's something in the buffer waiting, then process it
  * `writeOrBuffer` (Impact: 23.4)
    * *Intent:* // if we're already writing something, then just put this // in the queue, and wait our turn. Otherw...
  * `end` (Impact: 19.1)
  * `write` (Impact: 19.0)
  * `validChunk` (Impact: 18.8)
    * *Intent:* // If we get something that is not a buffer, string, null, or undefined, // and we're not in objectM...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 51`, `args: 31`, `func_start: 32`
* *Risk/State:* `state_mutation: 116`, `dead_code: 5`, `planned_debt: 2`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.275
  * `Choke Point (Betweenness):` 0.001724 | `Ripple Effect (Closeness):` 0.109091
  * `Imports (Out-Degree: 3):` duplex, buffer, events, process, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/es6/zlib.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 561.98 | **LOC:** 636 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.7067%), Tech Debt (37.2349%)
**Top Internal Functions/Classes:**
  * `Zlib` (Impact: 65.5)
    * *Intent:* // the Zlib class they all inherit from // This thing manages the queue of requests, and returns // ...
  * `_processChunk` (Impact: 37.2)
  * `params` (Impact: 27.4)
  * `flush` (Impact: 22.0)
  * `_transform` (Impact: 21.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 104`, `args: 50`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 78`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 31`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 45`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` binding, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/events.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 560.96 | **LOC:** 476 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.6228%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `removeListener` (Impact: 44.3)
  * `_addListener` (Impact: 41.2)
  * `emit` (Impact: 31.7)
  * `removeAllListeners` (Impact: 25.0)
  * `listeners` (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 82`, `args: 28`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 98`, `dead_code: 1`
* *Architecture:* `api: 2`
* *Defense:* `safety: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.482
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142222
  * `Imports (Out-Degree: 0):` events
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/es6/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 507.34 | **LOC:** 599 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.8596%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `formatValue` (Impact: 71.5)
  * `formatProperty` (Impact: 58.4)
  * `format` (Impact: 21.6)
  * `inspect` (Impact: 20.3)
    * *Intent:* /** * Echos the value of a value. Trys to print the value out * in the best way possible given the d...
  * `deprecate` (Impact: 15.3)
    * *Intent:* // Mark that a method should not be used. // Returns a modified function which warns once by default...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 127`, `args: 45`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 59`
* *Architecture:* `api: 23`, `import: 2`
* *Defense:* `safety: 40`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 117.149
  * `Choke Point (Betweenness):` 0.011494 | `Ripple Effect (Closeness):` 0.30303
  * `Imports (Out-Degree: 1):` inherits, process
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `package/src/es6/assert.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 447.4 | **LOC:** 489 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.0087%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_deepEqual` (Impact: 77.0)
  * `_throws` (Impact: 48.8)
  * `objEquiv` (Impact: 44.5)
  * `AssertionError` (Impact: 13.1)
  * `isView` (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 99`, `args: 34`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 43`, `dead_code: 1`
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* `safety: 59`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` buffer, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/punycode.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 309.28 | **LOC:** 476 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.8641%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `encode` (Impact: 29.3)
    * *Intent:* /** * Converts a string of Unicode symbols (e.g. a domain name label) to a * Punycode string of ASCI...
  * `decode` (Impact: 25.9)
    * *Intent:* /** * Converts a Punycode string of ASCII-only symbols to a string of Unicode * symbols. * @memberOf...
  * `ucs2decode` (Impact: 12.6)
    * *Intent:* /** * Creates an array containing the numeric code points of each Unicode * character in the string....
  * `adapt` (Impact: 6.5)
    * *Intent:* /** * Bias adaptation function as per section 3.4 of RFC 3492. * https://tools.ietf.org/html/rfc3492...
  * `basicToDigit` (Impact: 6.3)
    * *Intent:* /** * Converts a basic code point into a digit/integer. * @see `digitToBasic()` * @private * @param ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 55`, `args: 15`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 71`, `dead_code: 2`
* *Architecture:* `api: 7`
* *Defense:* `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.533
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044444
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/path.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 198.16 | **LOC:** 235 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.1286%), Tech Debt (15.6698%)
**Top Internal Functions/Classes:**
  * `relative` (Impact: 17.6)
    * *Intent:* // path.relative(from, to) // posix version
  * `normalizeArray` (Impact: 16.8)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
  * `resolve` (Impact: 10.4)
    * *Intent:* // path.resolve([from ...], to) // posix version
  * `normalize` (Impact: 9.4)
    * *Intent:* // path.normalize(path) // posix version
  * `trim` (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 61`, `args: 17`, `func_start: 12`
* *Risk/State:* `state_mutation: 32`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 11`, `import: 1`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/string-decoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 168.66 | **LOC:** 221 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.9079%), Tech Debt (25.4029%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 17.5)
    * *Intent:* // write decodes the given buffer and returns it as JS string that is // guaranteed to not contain a...
  * `detectIncompleteChar` (Impact: 14.3)
    * *Intent:* // detectIncompleteChar determines if there is an incomplete UTF-8 character at // the end of the gi...
  * `StringDecoder` (Impact: 12.9)
    * *Intent:* // StringDecoder provides an interface for efficiently splitting a series of // buffers into a serie...
  * `end` (Impact: 6.4)
  * `assertEncoding` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 33`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/setimmediate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 150.06 | **LOC:** 186 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 10.9)
  * `installPostMessageImplementation` (Impact: 7.2)
  * `runIfPresent` (Impact: 6.7)
  * `onGlobalMessage` (Impact: 6.0)
  * `setImmediate` (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 51
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 31`, `args: 20`, `func_start: 19`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 20`
* *Architecture:* `api: 3`, `concurrency: 11`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/qs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 149.04 | **LOC:** 148 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.0101%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 38.3)
  * `stringify` (Impact: 19.1)
  * `stringifyPrimitive` (Impact: 12.1)
  * `map` (Impact: 5.6)
  * `hasOwnProperty` (Impact: 1.9)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 34`, `args: 9`, `func_start: 5`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 4`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/vm.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 134.14 | **LOC:** 203 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.7011%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `runInContext` (Impact: 16.8)
  * `forEach` (Impact: 7.3)
  * `indexOf` (Impact: 7.3)
  * `Object_keys` (Impact: 6.1)
    * *Intent:* */
  * `createContext` (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 52`, `args: 25`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 20`
* *Architecture:* `api: 8`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/readable-stream/transform.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 125.8 | **LOC:** 175 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.7846%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `afterTransform` (Impact: 13.1)
  * `Transform` (Impact: 11.4)
  * `_write` (Impact: 10.5)
  * `_read` (Impact: 7.7)
    * *Intent:* // Doesn't matter what the args are here. // _transform does all the work. // That we got here means...
  * `done` (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 20`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`, `dead_code: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.38
  * `Choke Point (Betweenness):` 0.005747 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 2):` duplex, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/es6/readable-stream/buffer-list.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 89.22 | **LOC:** 60 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.4226%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `concat` (Impact: 6.3)
  * `join` (Impact: 4.6)
  * `push` (Impact: 4.5)
  * `shift` (Impact: 4.3)
  * `unshift` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.090741
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/stream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 76.6 | **LOC:** 111 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.9578%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pipe` (Impact: 26.6)
  * `ondata` (Impact: 6.0)
  * `onclose` (Impact: 3.3)
  * `ondrain` (Impact: 3.2)
  * `onerror` (Impact: 3.1)
    * *Intent:* // don't leave dangling pipes when there are errors.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 14`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 26.751
  * `Choke Point (Betweenness):` 0.008046 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 7):` duplex.js, passthrough.js, readable.js, transform.js, writable.js, events, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/timers.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 70.32 | **LOC:** 77 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.6507%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `clearInterval` (Impact: 6.0)
  * `clearTimeout` (Impact: 6.0)
  * `active` (Impact: 4.8)
  * `clearFn` (Impact: 4.5)
  * `onTimeout` (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 16`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 2`
* *Architecture:* `api: 10`, `concurrency: 13`, `import: 1`
* *Defense:* `safety: 10`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` setimmediate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 70.32 | **LOC:** 74 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.308%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 8`, `args: 1`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/os.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 54.92 | **LOC:** 114 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.3134%), Tech Debt (75.3696%)
**Top Internal Functions/Classes:**
  * `endianness` (Impact: 6.8)
  * `hostname` (Impact: 3.2)
  * `release` (Impact: 2.3)
  * `loadavg` (Impact: 1.1)
  * `uptime` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 37`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 17`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/http.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 53.3 | **LOC:** 168 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.3546%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 25.8)
  * `get` (Impact: 2.0)
  * `Agent` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 19`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` request, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/readable-stream/duplex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 37.76 | **LOC:** 46 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.2312%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Duplex` (Impact: 12.1)
  * `onend` (Impact: 3.5)
    * *Intent:* // the no-half-open enforcer
  * `onEndNT` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 11`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 53.84
  * `Choke Point (Betweenness):` 0.012644 | `Ripple Effect (Closeness):` 0.15
  * `Imports (Out-Degree: 3):` readable, writable, process, util
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/es6/domain.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 35.4 | **LOC:** 101 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.4208%), Tech Debt (99.9811%)
**Top Internal Functions/Classes:**
  * `intercept` (Impact: 5.0)
  * `bind` (Impact: 2.0)
  * `run` (Impact: 1.9)
  * `createEmitError` (Impact: 1.7)
  * `emitError` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 19`, `args: 13`, `func_start: 11`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` inherits, events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/inherits.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 24.96 | **LOC:** 26 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.5532%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `inherits` (Impact: 2.3)
  * `inherits` (Impact: 2.1)
  * `TempCtor` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 3`, `func_start: 5`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 126.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.208696
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/.eslintrc` (JSON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.56 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/rollup.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.64 | **LOC:** 9 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` package.json, rollup-plugin-babel
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

- `package/src/es6/readable-stream/duplex.js` -> **Severity: 1.264** (Bridge: 0.0126 * Flux: 99.9994%)
- `package/src/es6/util.js` -> **Severity: 1.149** (Bridge: 0.0115 * Flux: 99.9997%)
- `package/src/es6/readable-stream/readable.js` -> **Severity: 0.862** (Bridge: 0.0086 * Flux: 100.0%)
- `package/src/es6/stream.js` -> **Severity: 0.805** (Bridge: 0.008 * Flux: 99.9982%)
- `package/src/es6/readable-stream/transform.js` -> **Severity: 0.575** (Bridge: 0.0057 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/es6/util.js` -> **Severity: 24.042** (Embedded: 0.303 * Error Risk: 79.3386%)
- `package/src/es6/inherits.js` -> **Severity: 17.685** (Embedded: 0.2087 * Error Risk: 84.7391%)
- `package/src/es6/events.js` -> **Severity: 13.603** (Embedded: 0.1422 * Error Risk: 95.6497%)
- `package/src/es6/readable-stream/duplex.js` -> **Severity: 11.964** (Embedded: 0.15 * Error Risk: 79.7611%)
- `package/src/es6/readable-stream/writable.js` -> **Severity: 10.766** (Embedded: 0.1091 * Error Risk: 98.6893%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/es6/inherits.js` -> **Severity: 12632.7** (Blast Radius: 126.327 * Doc Risk: 100.0%)
- `package/src/es6/util.js` -> **Severity: 10868.042** (Blast Radius: 117.149 * Doc Risk: 92.7711%)
- `package/src/es6/readable-stream/duplex.js` -> **Severity: 5384.0** (Blast Radius: 53.84 * Doc Risk: 100.0%)
- `package/src/es6/events.js` -> **Severity: 4848.2** (Blast Radius: 48.482 * Doc Risk: 100.0%)
- `package/src/es6/readable-stream/readable.js` -> **Severity: 3727.5** (Blast Radius: 37.275 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
