# ARCHITECTURAL_BRIEF: guzzle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/guzzle/guzzle.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 83 analyzed artifact(s), 10019 LOC.
- **Load-bearing artifact:** `src/Utils.php` -- 12 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/ClientTest.php` -- pulls in 21 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Handler/CurlFactory.php` at magnitude 670.24 (structural weight, not risk).
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
| Total Artifacts | 114 |
| Analyzed Artifacts (Scanned) | 83 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 31 |
| Total LOC | 10019 |
| Volatility Index | 0.084 |
| % Scanned of codebase = | 72.8% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5116 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.071 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2027 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 73 | 9604 | 88.0% |
| JSON | 4 | 156 | 4.8% |
| MARKDOWN | 3 | 0 | 3.6% |
| DOCKERFILE | 1 | 8 | 1.2% |
| MAKEFILE | 1 | 68 | 1.2% |
| JAVASCRIPT | 1 | 183 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `1.324`
> **Composition Archetype:** `Small Flat Repo (2)` (z +1.32; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 23%, Data / Markup / Trivial 19%, Large Core Modules (3) 16%, Large Core Modules (2) 13%, Declarative / Non-Code 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 80 | 96.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 31*

**Composition by Extension & Reason:**
- `.rst`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dist`: 2x Excluded (Unsupported Extension: '.dist')
- `.php`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 1x Excluded (Unsupported Extension: '.neon')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 61.0 | 14.4 | 8.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.1 | 57.5 | 68.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.5 | 0.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 56.1 | 5.8 | 5.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 71.6 | 2.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.1 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 36.4 | 27.5 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1118 | 47 | 29 | `tests/ClientTest.php` |
| cleanup | 60 | 19 | 2 | `src/Client.php` |
| guards | 498 | 63 | 14 | `src/Handler/StreamHandler.php` |
| danger | 115 | 28 | 4 | `src/Handler/CurlFactory.php` |
| concurrency | 13 | 9 | 1 | `Makefile` |
| connectivity | 892 | 63 | 28 | `tests/ClientTest.php` |
| io | 44 | 16 | 2 | `src/Handler/StreamHandler.php` |
| crypto | 1 | 1 | 0 | `tests/server.js` |
| ipc | 6 | 4 | 0 | `Makefile` |
| time | 33 | 7 | 0 | `tests/Cookie/SetCookieTest.php` |
| serialization | 16 | 7 | 0 | `src/Utils.php` |
| regex | 7 | 5 | 0 | `src/Cookie/SetCookie.php` |
| events | 4 | 2 | 0 | `src/Handler/StreamHandler.php` |
| tests | 600 | 26 | 17 | `tests/Handler/CurlFactoryTest.php` |
| docs | 412 | 62 | 14 | `src/RequestOptions.php` |
| debt | 39 | 7 | 0 | `Makefile` |
| mutation | 1996 | 63 | 69 | `tests/ClientTest.php` |
| dead_code | 559 | 59 | 16 | `tests/Handler/CurlFactoryTest.php` |
| credential | 0 | 0 | 0 | - |
| threat | 19 | 16 | 1 | `src/Handler/CurlMultiHandler.php` |
| ml_ai | 10 | 5 | 0 | `tests/MiddlewareTest.php` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Handler/StreamHandler.php` (Hits: 10)
- `tests/Handler/StreamHandlerTest.php` (Hits: 8)
- `src/Handler/HeaderProcessor.php` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Utils.php** (`src/Utils.php`) — 12 inbound connections
2. **RequestException.php** (`src/Exception/RequestException.php`) — 10 inbound connections
3. **MockHandler.php** (`src/Handler/MockHandler.php`) — 9 inbound connections
4. **HandlerStack.php** (`src/HandlerStack.php`) — 8 inbound connections
5. **Client.php** (`src/Client.php`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ClientTest.php** (`tests/ClientTest.php`) — 21 outbound dependencies
2. **Client.php** (`src/Client.php`) — 18 outbound dependencies
3. **MiddlewareTest.php** (`tests/MiddlewareTest.php`) — 17 outbound dependencies
4. **StreamHandler.php** (`src/Handler/StreamHandler.php`) — 14 outbound dependencies
5. **StreamHandlerTest.php** (`tests/Handler/StreamHandlerTest.php`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `format` **(Many-Argument Workhorses)** (@ `src/MessageFormatter.php`) -> Impact: **123.8** | LOC: 115
  * *Intent:* /** * Returns a formatted message string. * * @param RequestInterface $request Request that was sent * @param ResponseInterface|null $response Respons...
- `applyHandlerOptions` **(Many-Argument Workhorses)** (@ `src/Handler/CurlFactory.php`) -> Impact: **122.4** | LOC: 197
- `GuzzleServer` **(Many-Argument Workhorses)** (@ `tests/server.js`) -> Impact: **102.1** | LOC: 206
  * *Intent:* /** * Guzzle node.js server */
- `controlRequest` **(Many-Argument Workhorses)** (@ `tests/server.js`) -> Impact: **67.8** | LOC: 76
- `applyOptions` **(Many-Argument Workhorses)** (@ `src/Client.php`) -> Impact: **61.9** | LOC: 129
  * *Intent:* /** * Applies the array of request options to a request. */
- `createStream` **(Defensive Guards)** (@ `src/Handler/StreamHandler.php`) -> Impact: **39.0** | LOC: 87
  * *Intent:* /** * @return resource */
- `__invoke` **(Defensive Guards)** (@ `src/Handler/MockHandler.php`) -> Impact: **31.0** | LOC: 66
- `setCookie` **(Compute Cores)** (@ `src/Cookie/CookieJar.php`) -> Impact: **27.0** | LOC: 59
- `create` **(Many-Argument Workhorses)** (@ `src/Exception/RequestException.php`) -> Impact: **27.0** | LOC: 50
  * *Intent:* /** * Factory method to create a new exception with a normalized error message * * @param RequestInterface $request Request sent * @param ResponseInte...
- `modifyRequest` **(Many-Argument Workhorses)** (@ `src/RedirectMiddleware.php`) -> Impact: **26.4** | LOC: 48

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 18 | 1822.68 | 20.87% | 53.24% |
| `tests` | 18 | 1688.9 | 10.07% | 0.0% |
| `src/Handler` | 9 | 1589.06 | 28.5% | 66.12% |
| `tests/Handler` | 7 | 1078.52 | 12.22% | 0.0% |
| `src/Cookie` | 5 | 692.75 | 30.13% | 71.44% |
| `tests/Cookie` | 4 | 324.46 | 5.86% | 0.0% |
| `src/Exception` | 9 | 232.0 | 5.49% | 33.06% |
| `__monolith__` | 7 | 130.52 | 3.65% | 11.77% |
| `tests/Exception` | 3 | 89.32 | 0.0% | 0.0% |
| `tests/Handler/Network` | 1 | 19.7 | 6.87% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/functions.php` -> **100.0%** Exposure
- `src/TransferStats.php` -> **99.9999%** Exposure
- `src/Exception/RequestException.php` -> **99.7583%** Exposure
- `src/Exception/BadResponseException.php` -> **98.9013%** Exposure
- `src/Exception/ConnectException.php` -> **98.9013%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/Client.php` -> **100.0%** Exposure
- `src/Cookie/FileCookieJar.php` -> **100.0%** Exposure
- `src/Exception/RequestException.php` -> **100.0%** Exposure
- `src/Handler/CurlFactory.php` -> **100.0%** Exposure
- `src/Handler/CurlMultiHandler.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/Handler/CurlFactoryTest.php` -> **63** Orphaned Functions | **0** Duplicates
- `tests/ClientTest.php` -> **62** Orphaned Functions | **0** Duplicates
- `tests/Handler/StreamHandlerTest.php` -> **55** Orphaned Functions | **0** Duplicates
- `tests/Cookie/CookieJarTest.php` -> **27** Orphaned Functions | **0** Duplicates
- `tests/RedirectMiddlewareTest.php` -> **23** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `386` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Handler/CurlFactory.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 670.24 | **LOC:** 742 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 7.619; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Complexity Load (formerly Cognitive Load) (61.0%), Debt Markers (formerly Tech Debt) (29.2%)
- **Documentation Coverage:** 70.3704% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyHandlerOptions` **(Many-Argument Workhorses)** (Impact: 122.4)
  * `applyBody` **(Stateful Encapsulated Methods)** (Impact: 21.9)
  * `createRejection` **(Many-Argument Workhorses)** (Impact: 20.4)
  * `retryFailedRewind` **(Stateful Encapsulated Methods)** (Impact: 17.8)
    * *Intent:* /** * This function ensures that a response was set on a transaction. If one * was not set, then the...
  * `create` **(Defensive Guards)** (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 110 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 95`, `args: 25`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 125`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 10`
* *Defense:* `safety: 36`, `doc: 10`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.619
  * `Choke Point (Betweenness):` 0.000502 | `Ripple Effect (Closeness):` 0.012195
  * `Imports (Out-Degree: 4):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Promise, GuzzleHttp\Promise\FulfilledPromise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Psr7\LazyOpenStream, GuzzleHttp\TransferStats, GuzzleHttp\Utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Handler/StreamHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 496.18 | **LOC:** 635 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 21.823; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Complexity Load (formerly Cognitive Load) (45.2%), Debt Markers (formerly Tech Debt) (34.8%)
- **Documentation Coverage:** 27.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createStream` **(Defensive Guards)** (Impact: 39.0)
    * *Intent:* /** * @return resource */
  * `__invoke` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* /** * Sends an HTTP request. * * @param RequestInterface $request Request to send. * @param array $o...
  * `add_proxy` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* /** * @param mixed $value as passed via Request transfer options. */
  * `resolveHost` **(Stateful Encapsulated Methods)** (Impact: 20.3)
  * `createResponse` **(Many-Argument Workhorses)** (Impact: 18.1)
    * *Intent:* /** * @param resource $stream */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 72 instances
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 102`, `args: 27`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 82`, `dead_code: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 10`, `api: 1`, `import: 12`
* *Defense:* `safety: 47`, `doc: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.823
  * `Choke Point (Betweenness):` 0.01084 | `Ripple Effect (Closeness):` 0.129186
  * `Imports (Out-Degree: 4):` 'close', GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Promise, GuzzleHttp\Promise\FulfilledPromise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Psr7, GuzzleHttp\TransferStats...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/Handler/CurlFactoryTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 438.76 | **LOC:** 961 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.5%), Complexity Load (formerly Cognitive Load) (27.5%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 93.7984% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testCreatesCurlHandle` **(I/O & Config Routines)** (Impact: 8.0)
  * `checkNoProxyForHost` **(Stateful Encapsulated Methods)** (Impact: 6.8)
  * `addDecodeResponse` **(Stateful Encapsulated Methods)** (Impact: 3.5)
  * `testBodyEofOnWindows` **(I/O & Config Routines)** (Impact: 3.2)
    * *Intent:* /** * https://github.com/guzzle/guzzle/issues/2735 */
  * `testCreatesConnectException` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 17 instances
* *Memory Alloc (weighted view):* 140
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 257`, `args: 78`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 197`, `unreferenced_by_name: 63`
* *Architecture:* `io: 2`, `api: 63`, `import: 12`
* *Defense:* `safety: 9`, `doc: 4`, `test: 98`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Handler, GuzzleHttp\Handler\CurlFactory, GuzzleHttp\Handler\EasyHandle, GuzzleHttp\Promise, GuzzleHttp\Psr7, GuzzleHttp\Tests\Helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ClientTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 375.06 | **LOC:** 865 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.5%), Connectivity (formerly Api Exposure) (12.3%)
- **Documentation Coverage:** 93.5484% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testCanSendMultipartWithExplicitBody` **(I/O & Config Routines)** (Impact: 3.2)
  * `testCanSendMultipart` **(I/O & Config Routines)** (Impact: 2.9)
  * `testUsesProxyEnvironmentVariables` **(I/O & Config Routines)** (Impact: 2.7)
  * `testIdnWithRedirect` **(Type Conversions)** (Impact: 2.4)
    * *Intent:* /** * @requires extension idn */
  * `testCanMergeOnBaseUriWithRequest` **(Type Conversions)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Memory Alloc (weighted view):* 206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 289`, `args: 63`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `state_mutation: 198`, `unreferenced_by_name: 62`
* *Architecture:* `io: 2`, `api: 62`, `import: 14`
* *Defense:* `safety: 6`, `doc: 4`, `test: 73`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` GuzzleHttp\Client, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\HandlerStack, GuzzleHttp\Handler\MockHandler, GuzzleHttp\Middleware, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Psr7, GuzzleHttp\Psr7\Request...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Handler/StreamHandlerTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 352.04 | **LOC:** 822 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (23.5%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 97.3214% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testStreamAttributeKeepsStreamOpen` **(I/O & Config Routines)** (Impact: 4.3)
  * `testAutomaticallyDecompressGzip` **(Type Conversions)** (Impact: 2.9)
  * `testAutomaticallyDecompressGzipHead` **(I/O & Config Routines)** (Impact: 2.9)
  * `testHandlesGarbageHttpServerGracefully` **(Defensive Guards)** (Impact: 2.9)
  * `testHandlesInvalidStatusCodeGracefully` **(Interface Declarations)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 7 instances
* *Memory Alloc (weighted view):* 67
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 174`, `args: 65`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 167`, `unreferenced_by_name: 55`
* *Architecture:* `io: 8`, `api: 55`, `import: 13`
* *Defense:* `safety: 6`, `doc: 2`, `test: 96`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Handler\StreamHandler, GuzzleHttp\Psr7, GuzzleHttp\Psr7\FnStream, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response, GuzzleHttp\RequestOptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Client.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 349.68 | **LOC:** 484 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **18**; blast radius 29.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.1%), Debt Markers (formerly Tech Debt) (62.5%), Complexity Load (formerly Cognitive Load) (36.9%)
- **Documentation Coverage:** 4.3478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyOptions` **(Many-Argument Workhorses)** (Impact: 61.9)
    * *Intent:* /** * Applies the array of request options to a request. */
  * `configureDefaults` **(Stateful Encapsulated Methods)** (Impact: 18.0)
    * *Intent:* /** * Configures the default options for a client. */
  * `buildUri` **(Stateful Encapsulated Methods)** (Impact: 12.8)
  * `prepareDefaults` **(Stateful Encapsulated Methods)** (Impact: 11.6)
    * *Intent:* /** * Merges default options into the array. * * @param array $options Options to modify by referenc...
  * `requestAsync` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* /** * Create and send an asynchronous HTTP request. * * Use an absolute path to override the base pa...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 57 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 60`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 75`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `api: 8`, `import: 11`
* *Defense:* `safety: 31`, `doc: 16`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.808
  * `Choke Point (Betweenness):` 0.006449 | `Ripple Effect (Closeness):` 0.1033
  * `Imports (Out-Degree: 4):`  Allows default headers to be unset.
            if ($options['headers'] === null) 
                $defaults['_conditional'] = [], ClientTrait, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\Exception\GuzzleException, GuzzleHttp\Exception\InvalidArgumentException, GuzzleHttp\Promise, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/RedirectMiddlewareTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 307.18 | **LOC:** 547 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (83.6%), Complexity Load (formerly Cognitive Load) (22.7%), Connectivity (formerly Api Exposure) (10.1%)
- **Documentation Coverage:** 60.8696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testRemoveCurlAuthorizationOptionsOnRedirectCrossScheme` **(Defensive Guards)** (Impact: 8.3)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
  * `testRemoveCurlAuthorizationOptionsOnRedirectCrossSchemeSamePort` **(Defensive Guards)** (Impact: 8.3)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
  * `testNotRemoveCurlAuthorizationOptionsOnRedirect` **(Defensive Guards)** (Impact: 8.3)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
  * `testRemoveCurlAuthorizationOptionsOnRedirectCrossHost` **(Defensive Guards)** (Impact: 6.9)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
  * `testRemoveCurlAuthorizationOptionsOnRedirectCrossPort` **(Defensive Guards)** (Impact: 6.9)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 163`, `args: 32`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 96`, `unreferenced_by_name: 23`
* *Architecture:* `api: 23`, `import: 11`
* *Defense:* `safety: 14`, `doc: 9`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` GuzzleHttp\Client, GuzzleHttp\Exception\BadResponseException, GuzzleHttp\Exception\TooManyRedirectsException, GuzzleHttp\HandlerStack, GuzzleHttp\Handler\MockHandler, GuzzleHttp\Middleware, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 274.36 | **LOC:** 262 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 6.794; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (92.1%), Complexity Load (formerly Cognitive Load) (22.4%), Concurrency Surface (formerly Concurrency) (16.6%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GuzzleServer` **(Many-Argument Workhorses)** (Impact: 102.1)
    * *Intent:* /** * Guzzle node.js server */
  * `controlRequest` **(Many-Argument Workhorses)** (Impact: 67.8)
  * `loadAuthentifier` **(Defensive Guards)** (Impact: 20.7)
    * *Intent:* /** * Provides authentication handlers (Basic, Digest). */
  * `receivedRequest` **(Defensive Guards)** (Impact: 14.8)
  * `firewallRequest` **(Many-Argument Workhorses)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 26`, `args: 13`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 21`
* *Architecture:* `io: 2`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 4`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crypto, http, http-auth, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cookie/SetCookie.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 264.18 | **LOC:** 493 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 21.81; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.5%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (34.3%)
- **Documentation Coverage:** 7.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromString` **(Defensive Guards)** (Impact: 26.3)
    * *Intent:* /** * Create a new SetCookie object from a string. * * @param string $cookie Set-Cookie header strin...
  * `__construct` **(Defensive Guards)** (Impact: 23.9)
    * *Intent:* /** * @param array $data Array of cookie data provided by a Cookie parser */
  * `__toString` **(Defensive Guards)** (Impact: 10.8)
  * `setExpires` **(Type Conversions)** (Impact: 8.9)
    * *Intent:* /** * Set the unix timestamp for which the cookie will expire. * * @param int|string|null $timestamp...
  * `validate` **(Defensive Guards)** (Impact: 8.7)
    * *Intent:* /** * Check if the cookie is valid according to RFC 6265. * * @return bool|string Returns true if va...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 61`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `unreferenced_by_name: 11`
* *Architecture:* `api: 26`
* *Defense:* `safety: 16`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.81
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060976
  * `Imports (Out-Degree: 0):` '=') === false) 
            return new self($data, ', \strlen($cookiePath), an equal sign.
        if (!isset($pieces[0]) || \strpos($pieces[0], "
        return \substr($requestPath, 
    public function matchesPath(string $requestPath): bool
    
        $cookiePath = $this->getPath(
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/MessageFormatter.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 236.1 | **LOC:** 200 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 10.259; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Complexity Load (formerly Cognitive Load) (43.4%), Debt Markers (formerly Tech Debt) (36.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* /** * Returns a formatted message string. * * @param RequestInterface $request Request that was sent...
  * `__construct` **(Compute Cores)** (Impact: 4.4)
    * *Intent:* /** * @param string $template Log message template */
  * `headers` **(Encapsulated Accessors)** (Impact: 3.3)
    * *Intent:* /** * Get headers from message as string */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 16`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 3`, `doc: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02439
  * `Imports (Out-Degree: 0):` Psr\Http\Message\MessageInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Utils.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 226.5 | **LOC:** 385 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **9**; blast radius 75.045; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Guard Balance (formerly Safety Score) (93.9%), Complexity Load (formerly Cognitive Load) (36.6%)
- **Documentation Coverage:** 30.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isHostInNoProxy` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* /** * Returns true if the provided host matches any of the no proxy areas. * * This method will stri...
  * `idnUriConvert` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /** * Wrapper for the hrtime() or microtime() functions * (depending on the PHP version, one of the ...
  * `chooseHandler` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* /** * Chooses and creates a default handler to use based on the environment. * * The returned handle...
  * `getenv` **(Type Conversions)** (Impact: 9.1)
  * `idnToAsci` **(Stateful Encapsulated Methods)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 68`, `args: 22`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`, `unreferenced_by_name: 13`
* *Architecture:* `io: 2`, `api: 13`, `import: 6`
* *Defense:* `safety: 5`, `doc: 16`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 75.045
  * `Choke Point (Betweenness):` 0.028857 | `Ripple Effect (Closeness):` 0.200578
  * `Imports (Out-Degree: 5):` GuzzleHttp\Exception\InvalidArgumentException, GuzzleHttp\Handler\CurlHandler, GuzzleHttp\Handler\CurlMultiHandler, GuzzleHttp\Handler\Proxy, GuzzleHttp\Handler\StreamHandler, Psr\Http\Message\UriInterface, or a custom HTTP handler.', s cURL...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/Cookie/CookieJar.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 220.1 | **LOC:** 308 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **2**; blast radius 19.481; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.9%), Debt Markers (formerly Tech Debt) (88.3%)
- **Documentation Coverage:** 53.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setCookie` **(Compute Cores)** (Impact: 27.0)
  * `clear` **(Compute Cores)** (Impact: 23.6)
  * `withCookieHeader` **(Compute Cores)** (Impact: 13.9)
  * `extractCookies` **(Compute Cores)** (Impact: 13.1)
  * `getCookiePathFromRequest` **(Stateful Encapsulated Methods)** (Impact: 9.4)
    * *Intent:* /** * Computes cookie path following RFC 6265 section 5.1.4 * * @see https://datatracker.ietf.org/do...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 62`, `args: 19`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 29`, `unreferenced_by_name: 9`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 1`, `doc: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.097561
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/HandlerStack.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 186.46 | **LOC:** 276 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **3**; blast radius 19.641; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.4%), Guard Balance (formerly Safety Score) (98.1%), Complexity Load (formerly Cognitive Load) (34.3%)
- **Documentation Coverage:** 3.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `splice` **(Stateful Encapsulated Methods)** (Impact: 14.4)
    * *Intent:* /** * Splices a function into the middleware list at a specific position. */
  * `remove` **(Callbacks & Closures)** (Impact: 6.4)
    * *Intent:* /** * Remove a middleware by instance or name from the stack. * * @param callable|string $remove Mid...
  * `debugCallable` **(Stateful Encapsulated Methods)** (Impact: 6.4)
    * *Intent:* /** * Provides a debug string for a given callable. * * @param callable|string $fn Function to write...
  * `__toString` **(I/O & Config Routines)** (Impact: 5.2)
    * *Intent:* /** * Dumps a string representation of the stack. * * @return string */
  * `resolve` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** * Compose the middleware and handler into a single callable function. * * @return callable(Reque...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 39`, `args: 16`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`, `unreferenced_by_name: 9`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.105401
  * `Imports (Out-Degree: 0):` GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/Handler/MockHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 158.18 | **LOC:** 213 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **10**; blast radius 18.977; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.5%), Guard Balance (formerly Safety Score) (81.8%), Complexity Load (formerly Cognitive Load) (38.0%)
- **Documentation Coverage:** 27.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__invoke` **(Defensive Guards)** (Impact: 31.0)
  * `append` **(Defensive Guards)** (Impact: 10.6)
    * *Intent:* /** * Adds one or more variadic requests, exceptions, callables, or promises * to the queue. * * @pa...
  * `__construct` **(Compute Cores)** (Impact: 10.5)
    * *Intent:* /** * The passed in value must be an array of * {@see ResponseInterface} objects, Exceptions, * call...
  * `invokeStats` **(Stateful Encapsulated Methods)** (Impact: 9.5)
    * *Intent:* /** * @param mixed $reason Promise or reason. */
  * `createWithMiddleware` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** * Creates a new MockHandler that uses the default handler stack list of * middlewares. * * @para...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 40`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`, `unreferenced_by_name: 7`
* *Architecture:* `io: 2`, `api: 8`, `import: 9`
* *Defense:* `safety: 18`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.977
  * `Choke Point (Betweenness):` 0.013701 | `Ripple Effect (Closeness):` 0.109756
  * `Imports (Out-Degree: 4):` GuzzleHttp\Exception\RequestException, GuzzleHttp\HandlerStack, GuzzleHttp\Promise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\TransferStats, GuzzleHttp\Utils, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/RedirectMiddleware.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 156.88 | **LOC:** 229 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 7.619; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (91.4%), Complexity Load (formerly Cognitive Load) (34.6%)
- **Documentation Coverage:** 41.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `modifyRequest` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `checkRedirect` **(Many-Argument Workhorses)** (Impact: 16.0)
    * *Intent:* /** * @return ResponseInterface|PromiseInterface */
  * `__invoke` **(Defensive Guards)** (Impact: 11.7)
  * `guardMax` **(Stateful Encapsulated Methods)** (Impact: 6.5)
    * *Intent:* /** * Check for too many redirects. * * @throws TooManyRedirectsException Too many redirects. */
  * `redirectUri` **(Stateful Encapsulated Methods)** (Impact: 4.8)
    * *Intent:* /** * Set the appropriate URL on the request based on the location header. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 35`, `args: 9`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 8`, `doc: 8`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.619
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012195
  * `Imports (Out-Degree: 2):` GuzzleHttp\Exception\BadResponseException, GuzzleHttp\Exception\TooManyRedirectsException, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface, Psr\Http\Message\UriInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Cookie/CookieJarTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 156.42 | **LOC:** 508 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.4%), Connectivity (formerly Api Exposure) (9.6%), Dead Code Surface (formerly Dead Code) (5.6%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testReturnsCookiesMatchingRequests` **(Compute Cores)** (Impact: 6.0)
    * *Intent:* /** * @dataProvider getMatchingCookiesDataProvider */
  * `testIgnoresCookiesForMismatchingDomains` **(Parameter Forwarders)** (Impact: 4.7)
    * *Intent:* /** * @dataProvider getDomainMatchesProvider */
  * `testDeletesCookiesByName` **(Callbacks & Closures)** (Impact: 3.1)
  * `testRemovesSelectively` **(I/O & Config Routines)** (Impact: 3.0)
  * `testOverwritesCookiesThatAreOlderOrDiscardable` **(I/O & Config Routines)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 96`, `args: 30`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `dead_code: 1`, `unreferenced_by_name: 27`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* `doc: 9`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DateInterval, DateTime, DateTimeImmutable, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\Cookie\SetCookie, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response, PHPUnit\Framework\TestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Handler/CurlMultiHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 143.4 | **LOC:** 288 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 20.709; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.0%), Guard Balance (formerly Safety Score) (88.9%), Complexity Load (formerly Cognitive Load) (37.9%)
- **Documentation Coverage:** 45.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* /** * This handler accepts the following options: * * - handle_factory: An optional factory used to ...
  * `tick` **(I/O & Config Routines)** (Impact: 8.8)
    * *Intent:* /** * Ticks the curl event loop. */
  * `processMessages` **(Stateful Encapsulated Methods)** (Impact: 7.2)
  * `__get` **(Compute Cores)** (Impact: 6.7)
    * *Intent:* /** * @param string $name * * @return resource|\CurlMultiHandle * * @throws \BadMethodCallException ...
  * `cancel` **(Stateful Encapsulated Methods)** (Impact: 6.7)
    * *Intent:* /** * Cancels a handle from sending and removes references to it. * * @param int $id Handle ID to ca...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 22 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 36`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 7`, `doc: 14`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.709
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.12495
  * `Imports (Out-Degree: 1):` Closure, GuzzleHttp\Promise, GuzzleHttp\Promise\Promise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Utils, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/Handler/MockHandlerTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 137.66 | **LOC:** 263 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.0%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testInvokesOnStatsFunctionForError` **(Callbacks & Closures)** (Impact: 2.0)
  * `testRejectsPromiseWhenOnHeadersFails` **(Callbacks & Closures)** (Impact: 1.8)
  * `testInvokesOnStatsFunctionForResponse` **(Callbacks & Closures)** (Impact: 1.8)
  * `testTransferTime` **(Callbacks & Closures)** (Impact: 1.8)
  * `testSinkFilename` **(Interface Declarations)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 107`, `args: 30`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 80`, `unreferenced_by_name: 21`
* *Architecture:* `api: 21`, `import: 8`
* *Defense:* `safety: 10`, `doc: 3`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` GuzzleHttp\Exception\BadResponseException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Handler\MockHandler, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response, GuzzleHttp\Psr7\Stream, GuzzleHttp\TransferStats, PHPUnit\Framework\TestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cookie/CookieJarInterface.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 127.59 | **LOC:** 81 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 12.119; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (73.0%), Complexity Load (formerly Cognitive Load) (10.5%), Connectivity (formerly Api Exposure) (8.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039911
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Exception/RequestException.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 117.76 | **LOC:** 151 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **5**; blast radius 30.891; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (94.7%), Complexity Load (formerly Cognitive Load) (32.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 27.0)
    * *Intent:* /** * Factory method to create a new exception with a normalized error message * * @param RequestInt...
  * `__construct` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `wrapException` **(Defensive Guards)** (Impact: 3.7)
    * *Intent:* /** * Wrap non-RequestExceptions with a RequestException */
  * `getResponse` **(Interface Declarations)** (Impact: 2.2)
    * *Intent:* /** * Get the associated response */
  * `getRequest` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* /** * Get the request that caused the exception */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 6`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.891
  * `Choke Point (Betweenness):` 0.008582 | `Ripple Effect (Closeness):` 0.170935
  * `Imports (Out-Degree: 2):` GuzzleHttp\BodySummarizer, GuzzleHttp\BodySummarizerInterface, Psr\Http\Client\RequestExceptionInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tests/MiddlewareTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 114.76 | **LOC:** 260 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.4%), Connectivity (formerly Api Exposure) (10.0%)
- **Documentation Coverage:** 86.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testTapsBeforeAndAfter` **(Callbacks & Closures)** (Impact: 2.5)
  * `testTracksHistory` **(Parameter Forwarders)** (Impact: 2.3)
    * *Intent:* /** * @dataProvider getHistoryUseCases */
  * `testAddsCookiesToRequests` **(Callbacks & Closures)** (Impact: 2.0)
  * `testMapsRequest` **(Callbacks & Closures)** (Impact: 1.9)
  * `testLogsRequestsAndErrors` **(Interface Declarations)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 114`, `args: 23`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `unreferenced_by_name: 15`
* *Architecture:* `api: 15`, `import: 17`
* *Defense:* `safety: 3`, `doc: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` GuzzleHttp\BodySummarizer, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\Cookie\SetCookie, GuzzleHttp\Exception\ClientException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Exception\ServerException, GuzzleHttp\HandlerStack, GuzzleHttp\Handler\MockHandler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/PoolTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 97.54 | **LOC:** 197 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (85.0%), Complexity Load (formerly Cognitive Load) (35.3%), Connectivity (formerly Api Exposure) (7.8%)
- **Documentation Coverage:** 78.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getClient` **(Encapsulated Accessors)** (Impact: 3.3)
  * `testUsesYieldedKeyInFulfilledCallback` **(Callbacks & Closures)** (Impact: 2.5)
  * `testCanProvideCallablesThatReturnResponses` **(Callbacks & Closures)** (Impact: 2.2)
  * `testBatchesResults` **(Callbacks & Closures)** (Impact: 2.1)
  * `testExecutesPendingWhenWaiting` **(Callbacks & Closures)** (Impact: 2.0)
    * *Intent:* /** * @doesNotPerformAssertions */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 108`, `args: 23`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 53`, `unreferenced_by_name: 9`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `safety: 1`, `doc: 2`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` GuzzleHttp\Client, GuzzleHttp\Exception\ClientException, GuzzleHttp\HandlerStack, GuzzleHttp\Handler\MockHandler, GuzzleHttp\Pool, GuzzleHttp\Promise\Promise, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Cookie/SetCookieTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 95.96 | **LOC:** 493 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 6.794; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (40.4%), Connectivity (formerly Api Exposure) (9.1%), Complexity Load (formerly Cognitive Load) (4.2%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testParseCookie` **(Many-Argument Workhorses)** (Impact: 15.7)
    * *Intent:* /** * @dataProvider cookieParserDataProvider */
  * `testValidatesCookies` **(Parameter Forwarders)** (Impact: 2.7)
    * *Intent:* /** * @dataProvider cookieValidateProvider */
  * `cookieValidateProvider` **(Defensive Guards)** (Impact: 2.6)
  * `testHoldsValues` **(I/O & Config Routines)** (Impact: 2.5)
  * `testMatchesDomain` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 38`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 16`
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* `safety: 5`, `doc: 7`, `test: 48`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` GuzzleHttp\Cookie\SetCookie, PHPUnit\Framework\TestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Middleware.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 91.68 | **LOC:** 269 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 12.528; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (98.7%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tap` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* /** * Middleware that invokes a callback before and after sending a request. * * The provided listen...
  * `log` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * Middleware that logs requests, responses, and errors using a message * formatter. * * @param L...
  * `httpErrors` **(Callbacks & Closures)** (Impact: 6.7)
    * *Intent:* /** * Middleware that throws exceptions for 4xx or 5xx responses when the * "http_errors" request op...
  * `history` **(Callbacks & Closures)** (Impact: 5.9)
    * *Intent:* /** * Middleware that pushes history data to an ArrayAccess container. * * @param array|\ArrayAccess...
  * `cookies` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* /** * Middleware that adds cookies to requests. * * The options array must be set to a CookieJarInte...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 104`, `args: 33`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 10`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 8`, `doc: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.528
  * `Choke Point (Betweenness):` 0.001656 | `Ripple Effect (Closeness):` 0.060976
  * `Imports (Out-Degree: 2):` GuzzleHttp\Cookie\CookieJarInterface, GuzzleHttp\Exception\RequestException, GuzzleHttp\Promise, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface, Psr\Log\LoggerInterface
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/PrepareBodyMiddleware.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 88.82 | **LOC:** 106 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 6.794; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.4%), Debt Markers (formerly Tech Debt) (83.2%), Complexity Load (formerly Cognitive Load) (40.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addExpectHeader` **(Stateful Encapsulated Methods)** (Impact: 21.8)
    * *Intent:* /** * Add expect header */
  * `__invoke` **(Compute Cores)** (Impact: 19.2)
  * `__construct` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * @param callable(RequestInterface, array): PromiseInterface $nextHandler Next handler to invoke...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 12`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.794
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Cookie/CookieJar.php` -> Churn: **100.0%** | Cog Load: 39.346% | Debt: 88.3274%
- `src/Middleware.php` -> Churn: **100.0%** | Cog Load: 14.4926% | Debt: 98.6851%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/Handler/StreamHandlerTest.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 352.04
- `src/Cookie/CookieJar.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 220.1
- `src/RedirectMiddleware.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 156.88
- `src/Middleware.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 91.68
- `tests/Server.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 85.22

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Utils.php` -> **Severity: 2.886** (Bridge: 0.0289 * Flux: 100.0%)
- `src/Handler/MockHandler.php` -> **Severity: 1.37** (Bridge: 0.0137 * Flux: 100.0%)
- `src/Handler/StreamHandler.php` -> **Severity: 1.084** (Bridge: 0.0108 * Flux: 100.0%)
- `src/Exception/RequestException.php` -> **Severity: 0.858** (Bridge: 0.0086 * Flux: 100.0%)
- `src/Client.php` -> **Severity: 0.645** (Bridge: 0.0064 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Utils.php` -> **Severity: 18.829** (Embedded: 0.2006 * Error Risk: 93.8734%)
- `src/Exception/RequestException.php` -> **Severity: 16.193** (Embedded: 0.1709 * Error Risk: 94.7294%)
- `src/TransferStats.php` -> **Severity: 12.438** (Embedded: 0.1507 * Error Risk: 82.5469%)
- `src/Handler/CurlMultiHandler.php` -> **Severity: 11.11** (Embedded: 0.125 * Error Risk: 88.9157%)
- `src/Handler/StreamHandler.php` -> **Severity: 10.951** (Embedded: 0.1292 * Error Risk: 84.7672%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Utils.php` -> **Severity: 2251.35** (Blast Radius: 75.045 * Doc Risk: 30.0%)
- `src/Handler/CurlHandler.php` -> **Severity: 1259.88** (Blast Radius: 20.998 * Doc Risk: 60.0%)
- `src/Cookie/CookieJar.php` -> **Severity: 1048.978** (Blast Radius: 19.481 * Doc Risk: 53.8462%)
- `src/Handler/CurlMultiHandler.php` -> **Severity: 931.905** (Blast Radius: 20.709 * Doc Risk: 45.0%)
- `tests/Helpers.php` -> **Severity: 877.4** (Blast Radius: 8.774 * Doc Risk: 100.0%)

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
