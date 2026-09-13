# ARCHITECTURAL_BRIEF: @types_node
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
| Total Artifacts | 88 |
| Analyzed Artifacts (Scanned) | 81 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 12139 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.0% |
| Dominant Lang | TYPESCRIPT |

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
| TYPESCRIPT | 79 | 12139 | 97.5% |
| MARKDOWN | 1 | 0 | 1.2% |
| PLAINTEXT | 1 | 0 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 79 | 97.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `.ts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4066 LOC), 1x Excluded (Machine-Generated Source Code Signature: 151 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 38.3 | 8.6 | 6.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 38.5 | 44.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 72.0 | 99.8 | 100.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 35.8 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 12.4 | 2.9 | 2.8 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 26.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 59.9 | 2.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 89.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 27.0 | 4.5 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 49.4 | 0.6 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6 | 6 | 0 | `node/child_process.d.ts` |
| cleanup | 23 | 14 | 1 | `node/fs.d.ts` |
| guards | 645 | 45 | 28 | `node/quic.d.ts` |
| danger | 892 | 52 | 25 | `node/stream.d.ts` |
| concurrency | 484 | 33 | 15 | `node/fs/promises.d.ts` |
| connectivity | 222 | 68 | 3 | `node/util.d.ts` |
| io | 375 | 21 | 8 | `node/fs.d.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 85 | 6 | 0 | `node/cluster.d.ts` |
| time | 31 | 6 | 0 | `node/timers.d.ts` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 147 | 24 | 4 | `node/events.d.ts` |
| tests | 4 | 4 | 0 | `node/assert.d.ts` |
| docs | 2580 | 59 | 88 | `node/fs.d.ts` |
| debt | 465 | 29 | 12 | `node/http2.d.ts` |
| mutation | 334 | 56 | 12 | `node/http2.d.ts` |
| dead_code | 879 | 63 | 28 | `node/buffer.d.ts` |
| credential | 1 | 1 | 0 | `node/tls.d.ts` |
| threat | 46 | 13 | 2 | `node/stream/web.d.ts` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.122**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `node/fs.d.ts` (Hits: 168)
- `node/https.d.ts` (Hits: 47)
- `node/fs/promises.d.ts` (Hits: 46)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **process.d.ts** (`node/process.d.ts`) — 111 outbound dependencies
2. **worker_threads.d.ts** (`node/worker_threads.d.ts`) — 13 outbound dependencies
3. **child_process.d.ts** (`node/child_process.d.ts`) — 10 outbound dependencies
4. **stream.d.ts** (`node/stream.d.ts`) — 10 outbound dependencies
5. **promises.d.ts** (`node/fs/promises.d.ts`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `finished` (@ `node/stream.d.ts`) -> Impact: **23.1** | LOC: 47
- `__promisify__` (@ `node/fs.d.ts`) -> Impact: **12.7** | LOC: 10
  * *Intent:* /** * Asynchronously writes `buffer` to the file referenced by the supplied file descriptor. * @param fd A file descriptor. * @param offset The part o...
- `compare` (@ `node/buffer.d.ts`) -> Impact: **12.6** | LOC: 7
  * *Intent:* * console.log(buf1.compare(buf2, 0, 6, 4)); * // Prints: -1 * console.log(buf1.compare(buf2, 5, 6, 5)); * // Prints: 1 * ``` * * `ERR_OUT_OF_RANGE` is...
- `listen` (@ `node/net.d.ts`) -> Impact: **11.2** | LOC: 1
  * *Intent:* * after a certain amount of time: * * ```js * server.on('error', (e) => { * if (e.code === 'EADDRINUSE') { * console.error('Address in use, retrying.....
- `stringify` (@ `node/querystring.d.ts`) -> Impact: **11.2** | LOC: 1
  * *Intent:* * By default, characters requiring percent-encoding within the query string will * be encoded as UTF-8\. If an alternative encoding is required, then ...
- `writeFile` (@ `node/fs/promises.d.ts`) -> Impact: **11.1** | LOC: 22
  * *Intent:* * * await promise; * } catch (err) { * // When a request is aborted - err is an AbortError * console.error(err); * } * ``` * * Aborting an ongoing req...
- `send` (@ `node/dgram.d.ts`) -> Impact: **11.0** | LOC: 8
- `traceCallback` (@ `node/diagnostics_channel.d.ts`) -> Impact: **10.1** | LOC: 7
  * *Intent:* * // Then asyncStart can restore from that data it stored previously * channels.asyncStart.bindStore(myStore, (data) => { * return data.span; * }); * ...
- `writeSync` (@ `node/fs.d.ts`) -> Impact: **10.1** | LOC: 7
  * *Intent:* /** * For detailed information, see the documentation of the asynchronous version of * this API: {@link write}. * @since v0.1.21 * @param [offset=0] *...
- `write` (@ `node/fs/promises.d.ts`) -> Impact: **9.4** | LOC: 9
  * *Intent:* * * It is unsafe to use `filehandle.write()` multiple times on the same file * without waiting for the promise to be fulfilled (or rejected). For this...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `node` | 46 | 316.74 | 6.89% | 85.32% |
| `node/fs` | 1 | 19.38 | 23.33% | 99.99% |
| `node/web-globals` | 16 | 11.66 | 11.67% | 38.93% |
| `node/stream` | 3 | 7.48 | 13.26% | 74.16% |
| `node/dns` | 1 | 5.59 | 38.26% | 92.96% |
| `node/ts5.7/compatibility` | 1 | 5.17 | 13.32% | 100.0% |
| `node/ts5.6/compatibility` | 1 | 4.96 | 13.54% | 100.0% |
| `node/util` | 1 | 3.67 | 4.11% | 100.0% |
| `node/ts5.6` | 3 | 3.55 | 1.75% | 33.33% |
| `node/path` | 2 | 1.82 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `node/async_hooks.d.ts` -> **100.0%** Exposure
- `node/buffer.buffer.d.ts` -> **100.0%** Exposure
- `node/buffer.d.ts` -> **100.0%** Exposure
- `node/console.d.ts` -> **100.0%** Exposure
- `node/dgram.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `node/console.d.ts` -> **59.8688%** Exposure
- `node/constants.d.ts` -> **31.0026%** Exposure
- `node/path/posix.d.ts` -> **31.0026%** Exposure
- `node/path/win32.d.ts` -> **31.0026%** Exposure
- `node/assert/strict.d.ts` -> **26.0366%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `node/http2.d.ts` -> **26** Orphaned Functions | **112** Duplicates
- `node/fs.d.ts` -> **39** Orphaned Functions | **70** Duplicates
- `node/buffer.d.ts` -> **82** Orphaned Functions | **0** Duplicates
- `node/stream.d.ts` -> **28** Orphaned Functions | **54** Duplicates
- `node/http.d.ts` -> **28** Orphaned Functions | **50** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `node/tls.d.ts` -> **49.4048%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `349` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `node/stream/web.d.ts` (TYPESCRIPT) -> Cumulative Risk: **625.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 4.44 | **LOC:** 297 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9995%), Concurrency (81.4319%)
- **Heaviest Functions:** `read` (Impact: 3.7), `pipeThrough` (Impact: 3.5), `pipeTo` (Impact: 3.5)

### 2. `node/web-globals/timers.d.ts` (TYPESCRIPT) -> Cumulative Risk: **542.2**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1.35 | **LOC:** 45 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9665%), Concurrency (99.5792%), Documentation (85.7143%)
- **Heaviest Functions:** `setInterval` (Impact: 4.2), `setTimeout` (Impact: 4.2), `setImmediate` (Impact: 1.9)

### 3. `node/worker_threads.d.ts` (TYPESCRIPT) -> Cumulative Risk: **524.58**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 8.9 | **LOC:** 718 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (88.5436%), Verification (80.0%)
- **Heaviest Functions:** `postMessageToThread` (Impact: 4.8), `addEventListener` (Impact: 4.2), `addEventListener` (Impact: 4.2)

### 4. `node/util.d.ts` (TYPESCRIPT) -> Cumulative Risk: **523.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 14.55 | **LOC:** 1688 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9649%), Concurrency (93.7373%), Verification (80.0%)
- **Heaviest Functions:** `inspect` (Impact: 9.0), `deprecate` (Impact: 6.8), `callbackify` (Impact: 6.0)

### 5. `node/ts5.6/compatibility/float16array.d.ts` (TYPESCRIPT) -> Cumulative Risk: **523.54**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 4.96 | **LOC:** 72 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (80.0%)
- **Heaviest Functions:** `fill` (Impact: 6.0), `slice` (Impact: 5.2), `subarray` (Impact: 5.2)

### 6. `node/ts5.7/compatibility/float16array.d.ts` (TYPESCRIPT) -> Cumulative Risk: **523.32**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 5.17 | **LOC:** 73 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (80.0%)
- **Heaviest Functions:** `fill` (Impact: 6.0), `slice` (Impact: 5.2), `subarray` (Impact: 5.2)

### 7. `node/console.d.ts` (TYPESCRIPT) -> Cumulative Risk: **516.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3.02 | **LOC:** 152 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Verification (80.0%), State Flux (59.8688%)
- **Heaviest Functions:** `dir` (Impact: 5.2), `table` (Impact: 5.2), `assert` (Impact: 3.5)

### 8. `node/stream.d.ts` (TYPESCRIPT) -> Cumulative Risk: **515.19**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 24.68 | **LOC:** 1794 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Safety Score (80.0%), Verification (80.0%)
- **Heaviest Functions:** `finished` (Impact: 23.1), `write` (Impact: 8.1), `reduce` (Impact: 6.2)

### 9. `node/fs.d.ts` (TYPESCRIPT) -> Cumulative Risk: **485.07**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 51.73 | **LOC:** 4679 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (83.4218%), Verification (80.0%)
- **Heaviest Functions:** `__promisify__` (Impact: 12.7), `writeSync` (Impact: 10.1), `__promisify__` (Impact: 7.5)

### 10. `node/dns.d.ts` (TYPESCRIPT) -> Cumulative Risk: **478.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 9.44 | **LOC:** 923 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9431%), Concurrency (96.5555%), Verification (80.0%)
- **Heaviest Functions:** `setLocalAddress` (Impact: 5.2), `__promisify__` (Impact: 3.5), `__promisify__` (Impact: 3.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `node/fs.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 51.73 | **LOC:** 4679 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.185%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__promisify__` (Impact: 12.7)
    * *Intent:* /** * Asynchronously writes `buffer` to the file referenced by the supplied file descriptor. * @para...
  * `writeSync` (Impact: 10.1)
    * *Intent:* /** * For detailed information, see the documentation of the asynchronous version of * this API: {@l...
  * `__promisify__` (Impact: 7.5)
    * *Intent:* /** * Asynchronous readdir(3) - read a directory. * @param path A path to a file. If a URL is provid...
  * `readdirSync` (Impact: 7.5)
    * *Intent:* /** * Reads the contents of the directory. * * See the POSIX [`readdir(3)`](http://man7.org/linux/ma...
  * `__promisify__` (Impact: 7.4)
    * *Intent:* /** * Asynchronous readdir(3) - read a directory. * @param path A path to a file. If a URL is provid...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 643`, `args: 365`, `func_start: 343`, `class_start: 57`
* *Risk/State:* `safety_bypasses: 32`, `planned_debt: 7`, `duplicate_logic: 70`, `unreferenced_by_name: 39`
* *Architecture:* `io: 168`, `api: 2`, `concurrency: 72`, `import: 7`
* *Defense:* `doc: 360`, `immutability_locks: 33`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:events, node:fs, promises, node:os, node:path, node:stream, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/http2.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 26.67 | **LOC:** 2481 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1815%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `goaway` (Impact: 8.1)
    * *Intent:* /** * Transmits a `GOAWAY` frame to the connected peer _without_ shutting down the`Http2Session`. * ...
  * `pushStream` (Impact: 6.2)
  * `respondWithFD` (Impact: 6.2)
    * *Intent:* * 'last-modified': stat.mtime.toUTCString(), * 'content-type': 'text/plain; charset=utf-8', * }; * s...
  * `respondWithFile` (Impact: 6.2)
    * *Intent:* * ```js * import http2 from 'node:http2'; * const server = http2.createServer(); * server.on('stream...
  * `connect` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 584`, `args: 256`, `func_start: 223`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 77`, `duplicate_logic: 112`, `unreferenced_by_name: 26`
* *Architecture:* `io: 10`, `api: 2`, `concurrency: 5`, `import: 10`
* *Defense:* `doc: 116`, `immutability_locks: 55`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:events, node:fs, node:http, node:http2, node:net, node:stream, node:tls...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/stream.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 24.68 | **LOC:** 1794 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1503%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `finished` (Impact: 23.1)
  * `write` (Impact: 8.1)
  * `reduce` (Impact: 6.2)
  * `end` (Impact: 6.0)
  * `filter` (Impact: 5.4)
    * *Intent:* /** * This method allows filtering the stream. For each chunk in the stream the *fn* function will b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 435`, `args: 203`, `func_start: 172`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 163`, `state_mutation: 2`, `planned_debt: 5`, `duplicate_logic: 54`, `unreferenced_by_name: 28`
* *Architecture:* `api: 5`, `concurrency: 17`, `import: 5`
* *Defense:* `safety: 1`, `doc: 91`, `immutability_locks: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` old-api-module.js, node:buffer, node:events, node:fs, node:http, node:stream, promises, web...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/fs/promises.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.38 | **LOC:** 1330 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.3272%), Tech Debt (99.9857%)
**Top Internal Functions/Classes:**
  * `writeFile` (Impact: 11.1)
    * *Intent:* * * await promise; * } catch (err) { * // When a request is aborted - err is an AbortError * console...
  * `write` (Impact: 9.4)
    * *Intent:* * * It is unsafe to use `filehandle.write()` multiple times on the same file * without waiting for t...
  * `read` (Impact: 9.2)
    * *Intent:* /** * Reads data from the file and stores that in the given buffer. * * If the file is not modified ...
  * `write` (Impact: 9.0)
  * `readdir` (Impact: 7.4)
    * *Intent:* * ```js * import { readdir } from 'node:fs/promises'; * * try { * const files = await readdir(path);...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 70`, `args: 87`, `func_start: 87`, `class_start: 12`
* *Risk/State:* `planned_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 25`
* *Architecture:* `io: 46`, `api: 1`, `concurrency: 76`, `import: 7`
* *Defense:* `doc: 78`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:events, node:fs, promises, node:os, node:path, node:readline, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/http.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.81 | **LOC:** 2189 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.3571%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `writeHead` (Impact: 6.2)
    * *Intent:* * res.setHeader('X-Foo', 'bar'); * res.writeHead(200, { 'Content-Type': 'text/plain' }); * res.end('...
  * `setTimeout` (Impact: 5.2)
    * *Intent:* /** * Sets the timeout value for sockets, and emits a `'timeout'` event on * the Server object, pass...
  * `setSocketKeepAlive` (Impact: 5.2)
    * *Intent:* /** * Once a socket is assigned to this request and is connected `socket.setKeepAlive()` will be cal...
  * `setGlobalProxyFromEnv` (Impact: 4.3)
    * *Intent:* * As this function resets the global configurations, any previously configured * `http.globalAgent`,...
  * `request` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 332`, `args: 166`, `func_start: 146`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 44`, `duplicate_logic: 50`, `unreferenced_by_name: 28`
* *Architecture:* `io: 9`, `api: 1`, `concurrency: 5`, `import: 10`
* *Defense:* `doc: 124`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:dns, node:events, node:http, node:net, node:stream, node:url, undici-types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/buffer.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.5 | **LOC:** 1811 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.4072%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `compare` (Impact: 12.6)
    * *Intent:* * console.log(buf1.compare(buf2, 0, 6, 4)); * // Prints: -1 * console.log(buf1.compare(buf2, 5, 6, 5...
  * `copy` (Impact: 9.0)
    * *Intent:* * } * * buf.copy(buf, 0, 4, 10); * * console.log(buf.toString()); * // Prints: efghijghijklmnopqrstu...
  * `fill` (Impact: 9.0)
    * *Intent:* * console.log(buf.fill('a')); * // Prints: <Buffer 61 61 61 61 61> * console.log(buf.fill('aazz', 'h...
  * `toString` (Impact: 8.1)
    * *Intent:* * const buf2 = Buffer.from('tést'); * * console.log(buf2.toString('hex')); * // Prints: 74c3a97374 *...
  * `slice` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 58`, `args: 96`, `func_start: 98`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `planned_debt: 1`, `unreferenced_by_name: 82`
* *Architecture:* `api: 24`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 2`, `doc: 88`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/util.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.55 | **LOC:** 1688 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.1947%), Tech Debt (99.9649%)
**Top Internal Functions/Classes:**
  * `inspect` (Impact: 9.0)
    * *Intent:* * // 1_000_000 * console.log(inspect(bigNumber, { numericSeparator: true })); * // 123_456_789n * co...
  * `deprecate` (Impact: 6.8)
    * *Intent:* * * If the `--throw-deprecation` command-line flag is set, or the * `process.throwDeprecation` prope...
  * `callbackify` (Impact: 6.0)
  * `getCallSites` (Impact: 5.2)
    * *Intent:* * // Line Number: 7 * // Column Number: 26 * * // Without sourceMap: * // Function Name: '' * // Scr...
  * `decode` (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 389`, `args: 98`, `func_start: 68`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 21`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 29`
* *Architecture:* `api: 101`, `concurrency: 27`, `import: 2`
* *Defense:* `safety: 1`, `doc: 84`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:assert, node:events, node:fs, node:process, node:util, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/net.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 13.45 | **LOC:** 953 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.0922%), Tech Debt (99.9965%)
**Top Internal Functions/Classes:**
  * `listen` (Impact: 11.2)
    * *Intent:* * after a certain amount of time: * * ```js * server.on('error', (e) => { * if (e.code === 'EADDRINU...
  * `write` (Impact: 8.1)
    * *Intent:* /** * Sends data on the socket, with an explicit encoding for string data. * @see {@link Socket.writ...
  * `listen` (Impact: 8.1)
  * `listen` (Impact: 8.1)
  * `end` (Impact: 6.0)
    * *Intent:* /** * Half-closes the socket, with one final chunk of data. * @see {@link Socket.end} for full detai...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 174`, `args: 97`, `func_start: 91`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 13`, `duplicate_logic: 4`, `unreferenced_by_name: 21`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 1`, `doc: 84`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:dns, node:events, node:net, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/child_process.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 11.0 | **LOC:** 1434 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9528%), Tech Debt (81.9453%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 9.2)
  * `spawn` (Impact: 6.2)
    * *Intent:* // overloads of spawn with 'args'
  * `spawnSync` (Impact: 6.2)
  * `execFileSync` (Impact: 6.2)
  * `send` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 130`, `args: 76`, `func_start: 76`, `class_start: 35`
* *Risk/State:* `high_risk_execution: 4`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 1`, `import: 7`
* *Defense:* `doc: 36`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:assert, node:buffer, node:child_process, node:dgram, node:events, node:fs, node:net, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/zlib.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.96 | **LOC:** 683 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1062%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `flush` (Impact: 5.2)
  * `crc32` (Impact: 3.5)
    * *Intent:* /** * Computes a 32-bit [Cyclic Redundancy Check](https://en.wikipedia.org/wiki/Cyclic_redundancy_ch...
  * `__promisify__` (Impact: 3.5)
  * `brotliCompressSync` (Impact: 3.5)
    * *Intent:* /** * Compress a chunk of data with `BrotliCompress`. * @since v11.7.0, v10.16.0 */
  * `__promisify__` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 108`, `args: 73`, `func_start: 72`, `class_start: 28`
* *Risk/State:* `duplicate_logic: 22`, `unreferenced_by_name: 25`
* *Architecture:* `api: 1`, `concurrency: 11`, `import: 3`
* *Defense:* `doc: 68`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:fs, node:stream, node:util, node:zlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/dns.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9.44 | **LOC:** 923 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.8616%), Tech Debt (99.9431%)
**Top Internal Functions/Classes:**
  * `setLocalAddress` (Impact: 5.2)
    * *Intent:* * The resolver instance will send its requests from the specified IP address. * This allows programs...
  * `__promisify__` (Impact: 3.5)
  * `__promisify__` (Impact: 3.5)
  * `__promisify__` (Impact: 3.5)
  * `__promisify__` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 184`, `args: 73`, `func_start: 73`, `class_start: 27`
* *Risk/State:* `fragile_debt: 1`, `duplicate_logic: 9`, `unreferenced_by_name: 5`
* *Architecture:* `api: 2`, `concurrency: 31`, `import: 2`
* *Defense:* `doc: 38`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:dns, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/tls.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9.44 | **LOC:** 1204 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2747%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `connect` (Impact: 9.2)
  * `connect` (Impact: 6.0)
  * `renegotiate` (Impact: 5.5)
    * *Intent:* * that is either an `Error` (if the request failed) or `null`. * * This method can be used to reques...
  * `getCACertificates` (Impact: 4.3)
    * *Intent:* * * `"system"`: return the CA certificates that are loaded from the system's trusted store, accordin...
  * `listenerCount` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 179`, `args: 101`, `func_start: 86`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 23`, `planned_debt: 3`, `duplicate_logic: 24`, `unreferenced_by_name: 25`
* *Architecture:* `io: 1`, `api: 1`, `import: 5`
* *Defense:* `doc: 119`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:crypto, node:fs, node:net, node:tls, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/worker_threads.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8.9 | **LOC:** 718 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.4894%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `postMessageToThread` (Impact: 4.8)
  * `addEventListener` (Impact: 4.2)
  * `addEventListener` (Impact: 4.2)
  * `removeEventListener` (Impact: 4.2)
  * `removeEventListener` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 133`, `args: 64`, `func_start: 64`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `planned_debt: 1`, `duplicate_logic: 10`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 18`, `import: 10`
* *Defense:* `doc: 38`, `sync_locks: 3`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:assert, node:events, promises, node:perf_hooks, node:stream, web, node:url, node:v8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/process.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8.74 | **LOC:** 2176 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2486%), Tech Debt (93.3551%)
**Top Internal Functions/Classes:**
  * `emitWarning` (Impact: 9.0)
  * `send` (Impact: 7.4)
    * *Intent:* /** * If Node.js is spawned with an IPC channel, the `process.send()` method can be * used to send m...
  * `emitWarning` (Impact: 6.0)
  * `writeReport` (Impact: 5.2)
    * *Intent:* /** * Writes a diagnostic report to a file. If filename is not provided, the default filename * incl...
  * `send` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 299`, `args: 88`, `func_start: 66`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 2`, `unreferenced_by_name: 25`
* *Architecture:* `io: 35`, `api: 3`, `concurrency: 4`, `import: 116`
* *Defense:* `doc: 114`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert, strict, async_hooks, buffer, child_process, cluster, console, constants...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/events.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7.34 | **LOC:** 1048 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.173%), Tech Debt (92.2003%)
**Top Internal Functions/Classes:**
  * `on` (Impact: 4.2)
    * *Intent:* * for await (const event of on(ee, 'foo', { signal: ac.signal })) { * // The execution of this inner...
  * `on` (Impact: 4.2)
  * `once` (Impact: 4.2)
    * *Intent:* * } catch (error) { * if (error.name === 'AbortError') { * console.error('Waiting for the event was ...
  * `once` (Impact: 4.0)
  * `off` (Impact: 4.0)
    * *Intent:* /** * Node.js-specific alias for `eventTarget.removeEventListener()`. * @since v14.5.0 */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 157`, `args: 75`, `func_start: 65`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 2`, `dead_code: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 2`
* *Defense:* `doc: 53`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:assert, node:async_hooks, node:events, node:process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/dgram.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6.04 | **LOC:** 565 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.7256%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 11.0)
  * `send` (Impact: 9.2)
    * *Intent:* * client.connect(41234, 'localhost', (err) => { * client.send(message, (err) => { * client.close(); ...
  * `bind` (Impact: 8.1)
    * *Intent:* * console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`); * }); * * server.on('listen...
  * `send` (Impact: 7.7)
  * `send` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 73`, `args: 37`, `func_start: 36`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `unreferenced_by_name: 20`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 5`
* *Defense:* `doc: 29`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:cluster, node:dgram, node:dns, node:events, node:net
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/dns/promises.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.59 | **LOC:** 504 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.2553%), Tech Debt (92.9648%)
**Top Internal Functions/Classes:**
  * `setLocalAddress` (Impact: 5.2)
    * *Intent:* * The resolver instance will send its requests from the specified IP address. * This allows programs...
  * `constructor` (Impact: 2.9)
    * *Intent:* * * `resolver.resolveAny()` * * `resolver.resolveCaa()` * * `resolver.resolveCname()` * * `resolver....
  * `resolve` (Impact: 2.3)
  * `lookupService` (Impact: 2.1)
    * *Intent:* * If `address` is not a valid IP address, a `TypeError` will be thrown. * The `port` will be coerced...
  * `lookup` (Impact: 1.8)
    * *Intent:* * dnsPromises.lookup('example.com', options).then((result) => { * console.log('address: %j family: I...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 42`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `concurrency: 35`, `import: 2`
* *Defense:* `doc: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:dns, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/assert.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.43 | **LOC:** 956 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.1468%), Tech Debt (21.6461%)
**Top Internal Functions/Classes:**
  * `rejects` (Impact: 4.2)
  * `doesNotReject` (Impact: 4.2)
  * `equal` (Impact: 4.0)
    * *Intent:* * // OK, 1 == '1' * assert.equal(NaN, NaN); * // OK * * assert.equal(1, 2); * // AssertionError: 1 =...
  * `notEqual` (Impact: 4.0)
    * *Intent:* * assert.notEqual(1, 2); * // OK * * assert.notEqual(1, 1); * // AssertionError: 1 != 1 * * assert.n...
  * `deepEqual` (Impact: 4.0)
    * *Intent:* * An alias of {@link deepStrictEqual}. * * **Legacy assertion mode** * * > Stability: 3 - Legacy: Us...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 86`, `args: 26`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 8`, `doc: 37`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:assert, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/perf_hooks.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.24 | **LOC:** 644 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2986%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `markResourceTiming` (Impact: 6.5)
  * `measure` (Impact: 6.0)
  * `eventLoopUtilization` (Impact: 5.4)
    * *Intent:* /** * This is an alias of `perf_hooks.eventLoopUtilization()`. * * _This property is an extension by...
  * `eventLoopUtilization` (Impact: 5.4)
    * *Intent:* * * Although the CPU is mostly idle while running this script, the value of * `utilization` is `1`. ...
  * `addEventListener` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 92`, `args: 40`, `func_start: 39`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 12`, `planned_debt: 2`, `duplicate_logic: 9`, `unreferenced_by_name: 19`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* `doc: 50`, `immutability_locks: 57`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:child_process, node:events, node:perf_hooks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/ts5.7/compatibility/float16array.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.17 | **LOC:** 73 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.3205%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fill` (Impact: 6.0)
  * `slice` (Impact: 5.2)
  * `subarray` (Impact: 5.2)
  * `copyWithin` (Impact: 4.0)
  * `every` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 28`, `args: 38`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `unreferenced_by_name: 30`
* *Architecture:* None
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/ts5.6/compatibility/float16array.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4.96 | **LOC:** 72 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.5382%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fill` (Impact: 6.0)
  * `slice` (Impact: 5.2)
  * `subarray` (Impact: 5.2)
  * `copyWithin` (Impact: 4.0)
  * `findLast` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 28`, `args: 34`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `unreferenced_by_name: 26`
* *Architecture:* None
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/tty.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4.53 | **LOC:** 251 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8424%), Tech Debt (99.8423%)
**Top Internal Functions/Classes:**
  * `cursorTo` (Impact: 6.0)
    * *Intent:* /** * `writeStream.cursorTo()` moves this `WriteStream`'s cursor to the specified * position. * @sin...
  * `moveCursor` (Impact: 4.0)
    * *Intent:* /** * `writeStream.moveCursor()` moves this `WriteStream`'s cursor _relative_ to its * current posit...
  * `listenerCount` (Impact: 3.7)
  * `constructor` (Impact: 3.5)
    * *Intent:* /** * Represents the readable side of a TTY. In normal circumstances `process.stdin` will be the onl...
  * `clearLine` (Impact: 3.5)
    * *Intent:* /** * `writeStream.clearLine()` clears the current line of this `WriteStream` in a * direction ident...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 75`, `args: 42`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:net, node:tty
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/v8.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4.47 | **LOC:** 989 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9511%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `writeHeapSnapshot` (Impact: 5.2)
    * *Intent:* * if (message === 'heapdump') { * // Generate a heapdump for the worker * // and return the filename...
  * `addSerializeCallback` (Impact: 3.5)
    * *Intent:* /** * Add a callback that will be called when the Node.js instance is about to get serialized into a...
  * `addDeserializeCallback` (Impact: 3.5)
    * *Intent:* /** * Add a callback that will be called when the Node.js instance is deserialized from a snapshot. ...
  * `setDeserializeMainFunction` (Impact: 3.5)
    * *Intent:* /** * This sets the entry point of the Node.js application when it is deserialized from a snapshot. ...
  * `getCppHeapStatistics` (Impact: 2.9)
    * *Intent:* * type_names: [], * detail_level: 'brief', * }); * ``` * @since v22.15.0 * @param detailLevel **Defa...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 67`, `args: 54`, `func_start: 48`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 9`, `duplicate_logic: 8`, `unreferenced_by_name: 35`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 3`
* *Defense:* `doc: 68`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:assert, node:buffer, node:fs, node:path, node:stream, node:v8, node:worker_threads, node:zlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/stream/web.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4.44 | **LOC:** 297 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8215%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 3.7)
  * `pipeThrough` (Impact: 3.5)
  * `pipeTo` (Impact: 3.5)
  * `cancel` (Impact: 2.9)
  * `error` (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 137`, `args: 39`, `func_start: 35`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 40`, `duplicate_logic: 14`, `unreferenced_by_name: 8`
* *Architecture:* `api: 1`, `concurrency: 13`, `import: 2`
* *Defense:* `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` web, node:util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/https.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4.32 | **LOC:** 406 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4299%), Tech Debt (66.1871%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 4.2)
  * `get` (Impact: 4.2)
  * `createConnection` (Impact: 3.7)
  * `constructor` (Impact: 3.7)
  * `listenerCount` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 100`, `args: 40`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `unreferenced_by_name: 4`
* *Architecture:* `io: 47`, `api: 1`, `import: 5`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:crypto, node:fs, node:http, node:https, node:stream, node:tls, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `node/assert/strict.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)
- `node/stream/web.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)
- `node/ts5.6/compatibility/float16array.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)
- `node/ts5.7/compatibility/float16array.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)
- `node/web-globals/abortcontroller.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
