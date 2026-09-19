# ARCHITECTURAL_BRIEF: @types_node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 81 analyzed artifact(s), 12139 LOC.
- **Load-bearing artifact:** none identifiable. No file in this repository is imported by another that GitGalaxy could resolve, so there is no dependency hierarchy to report. That is itself a finding: either this is a collection of independent scripts/documents rather than a coupled system, or the import style is one the engine does not resolve for these languages.
- **Top orchestrator:** `node/process.d.ts` -- pulls in 111 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `node/fs.d.ts` at magnitude 51.73 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

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
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 79 | 12139 | 97.5% |
| MARKDOWN | 1 | 0 | 1.2% |
| PLAINTEXT | 1 | 0 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `1.412`
> **Composition Archetype:** `Small Flat Repo` (z +1.41; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 33%, State Mutators Files 17%, Declarative / Non-Code 15%, Generic / Templated Code Files 12%, Compute Cores Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

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
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 37.6 | 44.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 72.0 | 99.8 | 100.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 35.8 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 12.4 | 2.9 | 2.8 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 26.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 59.9 | 2.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 27.0 | 4.5 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 49.4 | 0.6 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

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

- `finished` **(Generic / Templated Code)** (@ `node/stream.d.ts`) -> Impact: **23.1** | LOC: 47
- `__promisify__` **(Generic / Templated Code)** (@ `node/fs.d.ts`) -> Impact: **12.7** | LOC: 10
  * *Intent:* /** * Asynchronously writes `buffer` to the file referenced by the supplied file descriptor. */
- `compare` **(Many-Argument Workhorses)** (@ `node/buffer.d.ts`) -> Impact: **12.6** | LOC: 7
  * *Intent:* * console.log(buf1.compare(buf2, 0, 6, 4)); * // Prints: -1 * console.log(buf1.compare(buf2, 5, 6, 5)); * // Prints: 1 * ``` * * `ERR_OUT_OF_RANGE` is...
- `listen` **(Compute Cores)** (@ `node/net.d.ts`) -> Impact: **11.2** | LOC: 1
  * *Intent:* * after a certain amount of time: * * ```js * server.on('error', (e) => { * if (e.code === 'EADDRINUSE') { * console.error('Address in use, retrying.....
- `stringify` **(Compute Cores)** (@ `node/querystring.d.ts`) -> Impact: **11.2** | LOC: 1
  * *Intent:* * By default, characters requiring percent-encoding within the query string will * be encoded as UTF-8\. If an alternative encoding is required, then ...
- `writeFile` **(Many-Argument Workhorses)** (@ `node/fs/promises.d.ts`) -> Impact: **11.1** | LOC: 22
  * *Intent:* * * await promise; * } catch (err) { * // When a request is aborted - err is an AbortError * console.error(err); * } * ``` * * Aborting an ongoing req...
- `send` **(Many-Argument Workhorses)** (@ `node/dgram.d.ts`) -> Impact: **11.0** | LOC: 8
- `traceCallback` **(Generic / Templated Code)** (@ `node/diagnostics_channel.d.ts`) -> Impact: **10.1** | LOC: 7
  * *Intent:* * // Then asyncStart can restore from that data it stored previously * channels.asyncStart.bindStore(myStore, (data) => { * return data.span; * }); * ...
- `writeSync` **(Many-Argument Workhorses)** (@ `node/fs.d.ts`) -> Impact: **10.1** | LOC: 7
  * *Intent:* /** * For detailed information, see the documentation of the asynchronous version of */
- `write` **(Generic / Templated Code)** (@ `node/fs/promises.d.ts`) -> Impact: **9.4** | LOC: 9
  * *Intent:* * * It is unsafe to use `filehandle.write()` multiple times on the same file * without waiting for the promise to be fulfilled (or rejected). For this...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

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

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `node/fs.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 51.73 | **LOC:** 4679 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (83.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 18.0322% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__promisify__` **(Generic / Templated Code)** (Impact: 12.7)
    * *Intent:* /** * Asynchronously writes `buffer` to the file referenced by the supplied file descriptor. */
  * `writeSync` **(Many-Argument Workhorses)** (Impact: 10.1)
    * *Intent:* /** * For detailed information, see the documentation of the asynchronous version of */
  * `__promisify__` **(State Mutators)** (Impact: 7.5)
    * *Intent:* /** * Asynchronous readdir(3) - read a directory. */
  * `readdirSync` **(State Mutators)** (Impact: 7.5)
    * *Intent:* /** * Reads the contents of the directory. * * See the POSIX [`readdir(3)`](http://man7.org/linux/ma...
  * `__promisify__` **(State Mutators)** (Impact: 7.4)
    * *Intent:* /** * Asynchronous readdir(3) - read a directory. */
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 26.67 | **LOC:** 2481 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.4%)
- **Documentation Coverage:** 48.5373% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `goaway` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /** * Transmits a `GOAWAY` frame to the connected peer _without_ shutting down the`Http2Session`. */
  * `pushStream` **(Generic / Templated Code)** (Impact: 6.2)
  * `respondWithFD` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* * 'last-modified': stat.mtime.toUTCString(), * 'content-type': 'text/plain; charset=utf-8', * }; * s...
  * `respondWithFile` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* * ```js * import http2 from 'node:http2'; * const server = http2.createServer(); * server.on('stream...
  * `connect` **(Compute Cores)** (Impact: 6.2)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 24.68 | **LOC:** 1794 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (53.2%)
- **Documentation Coverage:** 38.0537% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finished` **(Generic / Templated Code)** (Impact: 23.1)
  * `write` **(Compute Cores)** (Impact: 8.1)
  * `reduce` **(Generic / Templated Code)** (Impact: 6.2)
  * `end` **(Compute Cores)** (Impact: 6.0)
  * `filter` **(Compute Cores)** (Impact: 5.4)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 19.38 | **LOC:** 1330 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 17.2414% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeFile` **(Many-Argument Workhorses)** (Impact: 11.1)
    * *Intent:* * * await promise; * } catch (err) { * // When a request is aborted - err is an AbortError * console...
  * `write` **(Generic / Templated Code)** (Impact: 9.4)
    * *Intent:* * * It is unsafe to use `filehandle.write()` multiple times on the same file * without waiting for t...
  * `read` **(Generic / Templated Code)** (Impact: 9.2)
    * *Intent:* /** * Reads data from the file and stores that in the given buffer. * * If the file is not modified ...
  * `write` **(Generic / Templated Code)** (Impact: 9.0)
  * `readdir` **(State Mutators)** (Impact: 7.4)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 16.81 | **LOC:** 2189 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.9%)
- **Documentation Coverage:** 41.4807% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeHead` **(State Mutators)** (Impact: 6.2)
    * *Intent:* * res.setHeader('X-Foo', 'bar'); * res.writeHead(200, { 'Content-Type': 'text/plain' }); * res.end('...
  * `setTimeout` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Sets the timeout value for sockets, and emits a `'timeout'` event on * the Server object, pass...
  * `setSocketKeepAlive` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Once a socket is assigned to this request and is connected `socket.setKeepAlive()` will be cal...
  * `setGlobalProxyFromEnv` **(Callbacks & Closures)** (Impact: 4.3)
    * *Intent:* * As this function resets the global configurations, any previously configured * `http.globalAgent`,...
  * `request` **(Parameter Forwarders)** (Impact: 4.2)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 16.5 | **LOC:** 1811 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (35.4%)
- **Documentation Coverage:** 3.1582% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compare` **(Many-Argument Workhorses)** (Impact: 12.6)
    * *Intent:* * console.log(buf1.compare(buf2, 0, 6, 4)); * // Prints: -1 * console.log(buf1.compare(buf2, 5, 6, 5...
  * `copy` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* * } * * buf.copy(buf, 0, 4, 10); * * console.log(buf.toString()); * // Prints: efghijghijklmnopqrstu...
  * `fill` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* * console.log(buf.fill('a')); * // Prints: <Buffer 61 61 61 61 61> * console.log(buf.fill('aazz', 'h...
  * `toString` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* * const buf2 = Buffer.from('tést'); * * console.log(buf2.toString('hex')); * // Prints: 74c3a97374 *...
  * `slice` **(Compute Cores)** (Impact: 8.1)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 14.55 | **LOC:** 1688 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (93.7%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.558% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspect` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* * // 1_000_000 * console.log(inspect(bigNumber, { numericSeparator: true })); * // 123_456_789n * co...
  * `deprecate` **(Generic / Templated Code)** (Impact: 6.8)
    * *Intent:* * * If the `--throw-deprecation` command-line flag is set, or the * `process.throwDeprecation` prope...
  * `callbackify` **(Generic / Templated Code)** (Impact: 6.0)
  * `getCallSites` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* * // Line Number: 7 * // Column Number: 26 * * // Without sourceMap: * // Function Name: '' * // Scr...
  * `decode` **(Compute Cores)** (Impact: 5.2)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 13.45 | **LOC:** 953 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.6%)
- **Documentation Coverage:** 17.6999% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listen` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* * after a certain amount of time: * * ```js * server.on('error', (e) => { * if (e.code === 'EADDRINU...
  * `write` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /** * Sends data on the socket, with an explicit encoding for string data. */
  * `listen` **(Compute Cores)** (Impact: 8.1)
  * `listen` **(Compute Cores)** (Impact: 8.1)
  * `end` **(Compute Cores)** (Impact: 6.0)
    * *Intent:* /** * Half-closes the socket, with one final chunk of data. */
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 11.0 | **LOC:** 1434 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.9%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.5%)
- **Documentation Coverage:** 40.6911% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Compute Cores)** (Impact: 9.2)
  * `spawn` **(State Mutators)** (Impact: 6.2)
    * *Intent:* // overloads of spawn with 'args'
  * `spawnSync` **(State Mutators)** (Impact: 6.2)
  * `execFileSync` **(State Mutators)** (Impact: 6.2)
  * `send` **(Compute Cores)** (Impact: 6.0)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 10.96 | **LOC:** 683 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (58.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 4.4741% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flush` **(Callbacks & Closures)** (Impact: 5.2)
  * `crc32` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Computes a 32-bit [Cyclic Redundancy Check](https://en.wikipedia.org/wiki/Cyclic_redundancy_ch...
  * `__promisify__` **(Generic / Templated Code)** (Impact: 3.5)
  * `brotliCompressSync` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Compress a chunk of data with `BrotliCompress`. */
  * `__promisify__` **(Generic / Templated Code)** (Impact: 3.5)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 9.44 | **LOC:** 923 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Concurrency Surface (formerly Concurrency) (96.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 40.5982% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setLocalAddress` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* * The resolver instance will send its requests from the specified IP address. * This allows programs...
  * `__promisify__` **(Generic / Templated Code)** (Impact: 3.5)
  * `__promisify__` **(Compute Cores)** (Impact: 3.5)
  * `__promisify__` **(Compute Cores)** (Impact: 3.5)
  * `__promisify__` **(Compute Cores)** (Impact: 3.5)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 9.44 | **LOC:** 1204 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Credential Material (formerly Secrets Risk) (49.4%)
- **Documentation Coverage:** 33.7121% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `connect` **(Compute Cores)** (Impact: 9.2)
  * `connect` **(Compute Cores)** (Impact: 6.0)
  * `renegotiate` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* * that is either an `Error` (if the request failed) or `null`. * * This method can be used to reques...
  * `getCACertificates` **(Compute Cores)** (Impact: 4.3)
    * *Intent:* * * `"system"`: return the CA certificates that are loaded from the system's trusted store, accordin...
  * `listenerCount` **(Generic / Templated Code)** (Impact: 3.7)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 8.9 | **LOC:** 718 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (88.5%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 44.2939% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `postMessageToThread` **(Parameter Forwarders)** (Impact: 4.8)
  * `addEventListener` **(Generic / Templated Code)** (Impact: 4.2)
  * `addEventListener` **(Parameter Forwarders)** (Impact: 4.2)
  * `removeEventListener` **(Generic / Templated Code)** (Impact: 4.2)
  * `removeEventListener` **(Parameter Forwarders)** (Impact: 4.2)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 8.74 | **LOC:** 2176 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **111**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (93.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.2%)
- **Documentation Coverage:** 24.4044% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitWarning` **(Compute Cores)** (Impact: 9.0)
  * `send` **(Compute Cores)** (Impact: 7.4)
    * *Intent:* /** * If Node.js is spawned with an IPC channel, the `process.send()` method can be * used to send m...
  * `emitWarning` **(Compute Cores)** (Impact: 6.0)
  * `writeReport` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Writes a diagnostic report to a file. If filename is not provided, the default filename * incl...
  * `send` **(Compute Cores)** (Impact: 4.5)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 7.34 | **LOC:** 1048 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (92.2%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.7%)
- **Documentation Coverage:** 22.7974% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on` **(State Mutators)** (Impact: 4.2)
    * *Intent:* * for await (const event of on(ee, 'foo', { signal: ac.signal })) { * // The execution of this inner...
  * `on` **(State Mutators)** (Impact: 4.2)
  * `once` **(State Mutators)** (Impact: 4.2)
    * *Intent:* * } catch (error) { * if (error.name === 'AbortError') { * console.error('Waiting for the event was ...
  * `once` **(Compute Cores)** (Impact: 4.0)
  * `off` **(Compute Cores)** (Impact: 4.0)
    * *Intent:* /** * Node.js-specific alias for `eventTarget.removeEventListener()`. */
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
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 6.04 | **LOC:** 565 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.2%)
- **Documentation Coverage:** 8.9483% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `send` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* * client.connect(41234, 'localhost', (err) => { * client.send(message, (err) => { * client.close(); ...
  * `bind` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* * console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`); * }); * * server.on('listen...
  * `send` **(Parameter Forwarders)** (Impact: 7.7)
  * `send` **(Compute Cores)** (Impact: 6.2)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 5.59 | **LOC:** 504 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (93.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setLocalAddress` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* * The resolver instance will send its requests from the specified IP address. * This allows programs...
  * `constructor` **(Compute Cores)** (Impact: 2.9)
    * *Intent:* * * `resolver.resolveAny()` * * `resolver.resolveCaa()` * * `resolver.resolveCname()` * * `resolver....
  * `resolve` **(State Mutators)** (Impact: 2.3)
  * `lookupService` **(State Mutators)** (Impact: 2.1)
    * *Intent:* * If `address` is not a valid IP address, a `TypeError` will be thrown. * The `port` will be coerced...
  * `lookup` **(Generic / Templated Code)** (Impact: 1.8)
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
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 5.43 | **LOC:** 956 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (23.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rejects` **(Callbacks & Closures)** (Impact: 4.2)
  * `doesNotReject` **(Callbacks & Closures)** (Impact: 4.2)
  * `equal` **(Compute Cores)** (Impact: 4.0)
    * *Intent:* * // OK, 1 == '1' * assert.equal(NaN, NaN); * // OK * * assert.equal(1, 2); * // AssertionError: 1 =...
  * `notEqual` **(Compute Cores)** (Impact: 4.0)
    * *Intent:* * assert.notEqual(1, 2); * // OK * * assert.notEqual(1, 1); * // AssertionError: 1 != 1 * * assert.n...
  * `deepEqual` **(Compute Cores)** (Impact: 4.0)
    * *Intent:* * * **Legacy assertion mode** * * * Tests for deep equality between the `actual` and `expected` para...
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 5.24 | **LOC:** 644 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.9%)
- **Documentation Coverage:** 41.2997% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `markResourceTiming` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `measure` **(Compute Cores)** (Impact: 6.0)
  * `eventLoopUtilization` **(State Mutators)** (Impact: 5.4)
    * *Intent:* /** * This is an alias of `perf_hooks.eventLoopUtilization()`. * * _This property is an extension by...
  * `eventLoopUtilization` **(State Mutators)** (Impact: 5.4)
    * *Intent:* * * Although the CPU is mostly idle while running this script, the value of * `utilization` is `1`. ...
  * `addEventListener` **(Generic / Templated Code)** (Impact: 4.2)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 5.17 | **LOC:** 73 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fill` **(Compute Cores)** (Impact: 6.0)
  * `slice` **(Generic / Templated Code)** (Impact: 5.2)
  * `subarray` **(Generic / Templated Code)** (Impact: 5.2)
  * `copyWithin` **(Compute Cores)** (Impact: 4.0)
  * `every` **(Compute Cores)** (Impact: 3.5)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 4.96 | **LOC:** 72 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fill` **(Compute Cores)** (Impact: 6.0)
  * `slice` **(Compute Cores)** (Impact: 5.2)
  * `subarray` **(Compute Cores)** (Impact: 5.2)
  * `copyWithin` **(Compute Cores)** (Impact: 4.0)
  * `findLast` **(Parameter Forwarders)** (Impact: 3.7)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 4.53 | **LOC:** 251 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.3%)
- **Documentation Coverage:** 38.9956% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cursorTo` **(Compute Cores)** (Impact: 6.0)
    * *Intent:* /** * `writeStream.cursorTo()` moves this `WriteStream`'s cursor to the specified * position. */
  * `moveCursor` **(Callbacks & Closures)** (Impact: 4.0)
    * *Intent:* /** * `writeStream.moveCursor()` moves this `WriteStream`'s cursor _relative_ to its * current posit...
  * `listenerCount` **(Generic / Templated Code)** (Impact: 3.7)
  * `constructor` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Represents the readable side of a TTY. In normal circumstances `process.stdin` will be the onl...
  * `clearLine` **(Callbacks & Closures)** (Impact: 3.5)
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
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4.47 | **LOC:** 989 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (84.7%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeHeapSnapshot` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* * if (message === 'heapdump') { * // Generate a heapdump for the worker * // and return the filename...
  * `addSerializeCallback` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Add a callback that will be called when the Node.js instance is about to get serialized into a...
  * `addDeserializeCallback` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Add a callback that will be called when the Node.js instance is deserialized from a snapshot. ...
  * `setDeserializeMainFunction` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * This sets the entry point of the Node.js application when it is deserialized from a snapshot. ...
  * `getCppHeapStatistics` **(Compute Cores)** (Impact: 2.9)
    * *Intent:* * type_names: [], * detail_level: 'brief', * }); * ``` * Accepted values are: * * `'brief'`: Brief s...
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 4.44 | **LOC:** 297 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (81.4%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(Generic / Templated Code)** (Impact: 3.7)
  * `pipeThrough` **(Generic / Templated Code)** (Impact: 3.5)
  * `pipeTo` **(Generic / Templated Code)** (Impact: 3.5)
  * `cancel` **(Compute Cores)** (Impact: 2.9)
  * `error` **(Compute Cores)** (Impact: 2.9)
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
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 4.32 | **LOC:** 406 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 12.346; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.0%), Debt Markers (formerly Tech Debt) (66.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 46.0196% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Parameter Forwarders)** (Impact: 4.2)
  * `get` **(Parameter Forwarders)** (Impact: 4.2)
  * `createConnection` **(Parameter Forwarders)** (Impact: 3.7)
  * `constructor` **(Generic / Templated Code)** (Impact: 3.7)
  * `listenerCount` **(Generic / Templated Code)** (Impact: 3.7)
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

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `node/assert/strict.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)
- `node/stream/web.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)
- `node/ts5.6/compatibility/float16array.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)
- `node/ts5.7/compatibility/float16array.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)
- `node/web-globals/abortcontroller.d.ts` -> **Severity: 1234.6** (Blast Radius: 12.346 * Doc Risk: 100.0%)

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
