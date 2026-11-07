# ARCHITECTURAL_BRIEF: guzzle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/guzzle/guzzle.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 91 analyzed artifact(s), 10208 LOC.
- **Load-bearing artifact:** `src/Utils.php` -- 16 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/MiddlewareTest.php` -- pulls in 17 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Handler/CurlFactory.php` at magnitude 659.04 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 91 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 23 |
| Total LOC | 10208 |
| Volatility Index | 0.11 |
| % Scanned of codebase = | 79.8% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4695 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0945 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 15.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6132 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 73 | 9604 | 80.2% |
| YAML | 6 | 189 | 6.6% |
| MARKDOWN | 5 | 0 | 5.5% |
| JSON | 4 | 156 | 4.4% |
| DOCKERFILE | 1 | 8 | 1.1% |
| MAKEFILE | 1 | 68 | 1.1% |
| JAVASCRIPT | 1 | 183 | 1.1% |

## 4.1 SOURCE ENCODINGS
All 91 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 26%, Interface Declarations Files 21%, Large Core Modules (3) 15%, Large Core Modules (2) 11%, Declarative / Non-Code 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 86 | 94.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 5.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 23*

**Composition by Extension & Reason:**
- `.rst`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.dist`: 2x Excluded (Unsupported Extension: '.dist')
- `.php`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 1x Excluded (Unsupported Extension: '.neon')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 60.3 | 13.5 | 6.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 78.0 | 42.3 | 53.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.4 | 0.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 56.1 | 5.5 | 4.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 71.6 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 36.0 | 13.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1118 | 47 | 21 | `tests/ClientTest.php` |
| cleanup | 60 | 19 | 2 | `src/Client.php` |
| guards | 501 | 66 | 12 | `src/Handler/StreamHandler.php` |
| danger | 115 | 28 | 4 | `src/Handler/CurlFactory.php` |
| concurrency | 13 | 9 | 0 | `Makefile` |
| connectivity | 895 | 66 | 26 | `tests/ClientTest.php` |
| io | 44 | 16 | 2 | `src/Handler/StreamHandler.php` |
| crypto | 1 | 1 | 0 | `tests/server.js` |
| ipc | 6 | 4 | 0 | `Makefile` |
| time | 33 | 7 | 0 | `tests/Cookie/SetCookieTest.php` |
| serialization | 16 | 7 | 0 | `src/Utils.php` |
| regex | 7 | 5 | 0 | `src/Cookie/SetCookie.php` |
| events | 4 | 2 | 0 | `src/Handler/StreamHandler.php` |
| tests | 600 | 26 | 16 | `tests/Handler/CurlFactoryTest.php` |
| docs | 421 | 65 | 13 | `src/RequestOptions.php` |
| debt | 52 | 9 | 0 | `Makefile` |
| mutation | 1999 | 64 | 53 | `tests/ClientTest.php` |
| dead_code | 555 | 59 | 15 | `tests/Handler/CurlFactoryTest.php` |
| credential | 0 | 0 | 0 | - |
| threat | 6 | 4 | 0 | `src/Cookie/SetCookie.php` |
| ml_ai | 10 | 5 | 0 | `tests/MiddlewareTest.php` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Handler/StreamHandler.php` (Hits: 10)
- `tests/Handler/StreamHandlerTest.php` (Hits: 8)
- `src/Handler/HeaderProcessor.php` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Utils.php** (`src/Utils.php`) — 16 inbound connections
2. **RequestException.php** (`src/Exception/RequestException.php`) — 10 inbound connections
3. **MockHandler.php** (`src/Handler/MockHandler.php`) — 10 inbound connections
4. **InvalidArgumentException.php** (`src/Exception/InvalidArgumentException.php`) — 9 inbound connections
5. **HandlerStack.php** (`src/HandlerStack.php`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **MiddlewareTest.php** (`tests/MiddlewareTest.php`) — 17 outbound dependencies
2. **ClientTest.php** (`tests/ClientTest.php`) — 13 outbound dependencies
3. **StreamHandlerTest.php** (`tests/Handler/StreamHandlerTest.php`) — 13 outbound dependencies
4. **StreamHandler.php** (`src/Handler/StreamHandler.php`) — 12 outbound dependencies
5. **CurlFactoryTest.php** (`tests/Handler/CurlFactoryTest.php`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `format` **(Many-Argument Workhorses)** (@ `src/MessageFormatter.php`) -> Impact: **123.8** | LOC: 115
  * *Intent:* /** * Returns a formatted message string. * * @param RequestInterface $request Request that was sent * @param ResponseInterface|null $response Respons...
- `applyHandlerOptions` **(Many-Argument Workhorses)** (@ `src/Handler/CurlFactory.php`) -> Impact: **120.7** | LOC: 197
- `GuzzleServer` **(Many-Argument Workhorses)** (@ `tests/server.js`) -> Impact: **102.1** | LOC: 206
  * *Intent:* /** * Guzzle node.js server */
- `controlRequest` **(Many-Argument Workhorses)** (@ `tests/server.js`) -> Impact: **67.8** | LOC: 76
- `applyOptions` **(Many-Argument Workhorses)** (@ `src/Client.php`) -> Impact: **60.1** | LOC: 129
  * *Intent:* /** * Applies the array of request options to a request. */
- `createStream` **(Defensive Guards)** (@ `src/Handler/StreamHandler.php`) -> Impact: **37.3** | LOC: 87
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
| `src` | 18 | 1821.48 | 20.86% | 48.85% |
| `tests` | 18 | 1578.1 | 9.72% | 0.0% |
| `src/Handler` | 9 | 1568.16 | 28.36% | 58.8% |
| `tests/Handler` | 7 | 1063.42 | 12.06% | 0.0% |
| `src/Cookie` | 5 | 691.75 | 30.09% | 65.96% |
| `tests/Cookie` | 4 | 322.46 | 6.38% | 0.0% |
| `src/Exception` | 9 | 232.0 | 5.49% | 32.63% |
| `__monolith__` | 7 | 130.52 | 3.65% | 8.69% |
| `tests/Exception` | 3 | 89.32 | 0.0% | 0.0% |
| `.github/workflows` | 3 | 44.56 | 1.15% | 66.65% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/ci.yml` -> **100.0%** Exposure
- `src/functions.php` -> **100.0%** Exposure
- `src/TransferStats.php` -> **99.9998%** Exposure
- `.github/workflows/static.yml` -> **99.9447%** Exposure
- `src/Exception/RequestException.php` -> **99.5741%** Exposure
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
- **Unknown Dependencies:** `339` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Handler/CurlFactory.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.876)
- **Top Global Matches:** file_cluster_4: 5.876, file_cluster_16: 7.961, file_cluster_15: 9.021
- **Magnitude:** 659.04 | **LOC:** 742 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 27.764; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (60.3%), Debt Markers (formerly Tech Debt) (26.5%)
- **Documentation Coverage:** 70.3704% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyHandlerOptions` **(Many-Argument Workhorses)** (Impact: 120.7)
  * `applyBody` **(Stateful Encapsulated Methods)** (Impact: 21.9)
  * `create` **(Defensive Guards)** (Impact: 17.4)
  * `createRejection` **(Many-Argument Workhorses)** (Impact: 16.9)
  * `createHeaderFn` **(Defensive Guards)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 110 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 95`, `args: 25`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 125`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 10`
* *Defense:* `safety: 36`, `doc: 10`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.764
  * `Choke Point (Betweenness):` 0.009176 | `Ripple Effect (Closeness):` 0.121008
  * `Imports (Out-Degree: 7):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Promise, GuzzleHttp\Promise\FulfilledPromise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Psr7\LazyOpenStream, GuzzleHttp\TransferStats, GuzzleHttp\Utils...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Handler/StreamHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.798)
- **Top Global Matches:** file_cluster_4: 6.798, file_cluster_16: 7.783, file_cluster_15: 9.426
- **Magnitude:** 486.48 | **LOC:** 635 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 19.552; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.5%), Complexity Load (formerly Cognitive Load) (44.7%), Debt Markers (formerly Tech Debt) (32.3%)
- **Documentation Coverage:** 27.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createStream` **(Defensive Guards)** (Impact: 37.3)
    * *Intent:* /** * @return resource */
  * `__invoke` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* /** * Sends an HTTP request. * * @param RequestInterface $request Request to send. * @param array $o...
  * `add_proxy` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* /** * @param mixed $value as passed via Request transfer options. */
  * `checkDecode` **(Stateful Encapsulated Methods)** (Impact: 17.5)
    * *Intent:* /** * @param resource $stream */
  * `resolveHost` **(Stateful Encapsulated Methods)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 72 instances
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 102`, `args: 27`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 82`, `unreferenced_by_name: 8`
* *Architecture:* `io: 10`, `api: 1`, `import: 12`
* *Defense:* `safety: 47`, `doc: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.552
  * `Choke Point (Betweenness):` 0.016396 | `Ripple Effect (Closeness):` 0.16
  * `Imports (Out-Degree: 6):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Promise, GuzzleHttp\Promise\FulfilledPromise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Psr7, GuzzleHttp\TransferStats, GuzzleHttp\Utils...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/Handler/CurlFactoryTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.415)
- **Top Global Matches:** file_cluster_11: 7.415, file_cluster_10: 8.264, file_cluster_15: 8.695
- **Magnitude:** 435.66 | **LOC:** 961 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (27.8%), Connectivity (formerly Api Exposure) (11.6%)
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
* *Structure:* `branch: 13`, `structural_boundaries: 257`, `args: 78`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 197`, `unreferenced_by_name: 63`
* *Architecture:* `io: 2`, `api: 63`, `import: 12`
* *Defense:* `safety: 9`, `doc: 4`, `test: 98`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Handler, GuzzleHttp\Handler\CurlFactory, GuzzleHttp\Handler\EasyHandle, GuzzleHttp\Promise, GuzzleHttp\Psr7, GuzzleHttp\Tests\Helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ClientTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.507)
- **Top Global Matches:** file_cluster_11: 6.507, file_cluster_2: 8.279, file_cluster_15: 8.359
- **Magnitude:** 375.06 | **LOC:** 865 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.3%), Connectivity (formerly Api Exposure) (12.3%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` GuzzleHttp\Client, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\HandlerStack, GuzzleHttp\Handler\MockHandler, GuzzleHttp\Middleware, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Psr7, GuzzleHttp\Psr7\Request...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Client.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.397)
- **Top Global Matches:** file_cluster_4: 6.397, file_cluster_16: 9.7, file_cluster_15: 10.059
- **Magnitude:** 347.88 | **LOC:** 484 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 21.264; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.9%), Debt Markers (formerly Tech Debt) (55.9%), Complexity Load (formerly Cognitive Load) (36.8%)
- **Documentation Coverage:** 4.3478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyOptions` **(Many-Argument Workhorses)** (Impact: 60.1)
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
* *Structure:* `branch: 65`, `structural_boundaries: 60`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 75`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `api: 8`, `import: 11`
* *Defense:* `safety: 31`, `doc: 16`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.264
  * `Choke Point (Betweenness):` 0.045104 | `Ripple Effect (Closeness):` 0.101408
  * `Imports (Out-Degree: 6):` ClientTrait, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\Exception\GuzzleException, GuzzleHttp\Exception\InvalidArgumentException, GuzzleHttp\Promise, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/Handler/StreamHandlerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.498)
- **Top Global Matches:** file_cluster_11: 6.498, file_cluster_10: 7.639, file_cluster_15: 8.164
- **Magnitude:** 340.04 | **LOC:** 822 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (54.7%), Complexity Load (formerly Cognitive Load) (22.0%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 97.3214% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testAutomaticallyDecompressGzip` **(Type Conversions)** (Impact: 2.9)
  * `testAutomaticallyDecompressGzipHead` **(I/O & Config Routines)** (Impact: 2.9)
  * `testSuccessfullyCallsOnHeadersBeforeWritingToSink` **(Callbacks & Closures)** (Impact: 2.6)
  * `testAddsProxyByProtocol` **(Interface Declarations)** (Impact: 2.5)
  * `testInvokesOnStatsOnError` **(I/O & Config Routines)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 3 instances
* *Memory Alloc (weighted view):* 67
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 174`, `args: 65`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 167`, `unreferenced_by_name: 55`
* *Architecture:* `io: 8`, `api: 55`, `import: 13`
* *Defense:* `safety: 6`, `doc: 2`, `test: 96`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Handler\StreamHandler, GuzzleHttp\Psr7, GuzzleHttp\Psr7\FnStream, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response, GuzzleHttp\RequestOptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.332)
- **Top Global Matches:** file_cluster_8: 11.332, file_cluster_6: 16.019, file_cluster_4: 23.711
- **Magnitude:** 274.36 | **LOC:** 262 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 5.433; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (22.4%), Concurrency Surface (formerly Concurrency) (16.6%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crypto, http, http-auth, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cookie/SetCookie.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.081)
- **Top Global Matches:** file_cluster_15: 8.081, file_cluster_11: 8.118, file_cluster_4: 8.14
- **Magnitude:** 263.18 | **LOC:** 493 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); blast radius 35.641; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.1%), Guard Balance (formerly Safety Score) (59.7%), Complexity Load (formerly Cognitive Load) (34.1%)
- **Documentation Coverage:** 7.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromString` **(Defensive Guards)** (Impact: 26.3)
    * *Intent:* /** * Create a new SetCookie object from a string. * * @param string $cookie Set-Cookie header strin...
  * `__construct` **(Defensive Guards)** (Impact: 23.9)
    * *Intent:* /** * @param array $data Array of cookie data provided by a Cookie parser */
  * `__toString` **(Defensive Guards)** (Impact: 10.8)
  * `setExpires` **(Type Conversions)** (Impact: 8.9)
    * *Intent:* /** * Set the unix timestamp for which the cookie will expire. * * @param int|string|null $timestamp...
  * `matchesDomain` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* /** * Check if the cookie matches a domain value. * * @param string $domain Domain to check against ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 61`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `unreferenced_by_name: 11`
* *Architecture:* `api: 26`
* *Defense:* `safety: 16`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.100439
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/MessageFormatter.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.652)
- **Top Global Matches:** file_cluster_8: 6.652, file_cluster_6: 17.126, file_cluster_3: 20.078
- **Magnitude:** 236.1 | **LOC:** 200 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 7.393; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.8%), Complexity Load (formerly Cognitive Load) (43.4%), Debt Markers (formerly Tech Debt) (27.7%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 0):` Psr\Http\Message\MessageInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Utils.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.517)
- **Top Global Matches:** file_cluster_15: 6.517, file_cluster_16: 8.121, file_cluster_11: 8.363
- **Magnitude:** 227.1 | **LOC:** 385 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **6**; blast radius 86.865; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.5%), Guard Balance (formerly Safety Score) (70.5%), Complexity Load (formerly Cognitive Load) (36.6%)
- **Documentation Coverage:** 14.8148% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isHostInNoProxy` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* * partial match: (e.g., "foo.com" == "baz.foo.com" and ".foo.com" == * "baz.foo.com", but ".foo.com"...
  * `idnUriConvert` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /** * @throws InvalidArgumentException * * @internal */
  * `chooseHandler` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* /** * Chooses and creates a default handler to use based on the environment. * * The returned handle...
  * `getenv` **(Type Conversions)** (Impact: 9.1)
    * *Intent:* /** * @internal */
  * `defaultCaBundle` **(I/O & Config Routines)** (Impact: 8.8)
    * *Intent:* * Returns the default cacert bundle for the current system. * * First, the openssl.cafile and curl.c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 68`, `args: 22`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`, `unreferenced_by_name: 13`
* *Architecture:* `io: 2`, `api: 13`, `import: 6`
* *Defense:* `safety: 5`, `doc: 16`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 86.865
  * `Choke Point (Betweenness):` 0.076717 | `Ripple Effect (Closeness):` 0.248276
  * `Imports (Out-Degree: 6):` GuzzleHttp\Exception\InvalidArgumentException, GuzzleHttp\Handler\CurlHandler, GuzzleHttp\Handler\CurlMultiHandler, GuzzleHttp\Handler\Proxy, GuzzleHttp\Handler\StreamHandler, Psr\Http\Message\UriInterface
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/Cookie/CookieJar.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.774)
- **Top Global Matches:** file_cluster_4: 6.774, file_cluster_12: 9.505, file_cluster_15: 11.084
- **Magnitude:** 220.1 | **LOC:** 308 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 17.461; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.6%), Guard Balance (formerly Safety Score) (68.4%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.461
  * `Choke Point (Betweenness):` 0.003995 | `Ripple Effect (Closeness):` 0.110651
  * `Imports (Out-Degree: 1):` Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/RedirectMiddlewareTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.11)
- **Top Global Matches:** file_cluster_11: 7.11, file_cluster_10: 7.603, file_cluster_15: 8.34
- **Magnitude:** 197.38 | **LOC:** 547 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.7%), Complexity Load (formerly Cognitive Load) (16.6%), Connectivity (formerly Api Exposure) (10.1%)
- **Documentation Coverage:** 60.8696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testNotRemoveCurlAuthorizationOptionsOnRedirect` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
  * `testRemoveCurlAuthorizationOptionsOnRedirectCrossHost` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
  * `testRemoveCurlAuthorizationOptionsOnRedirectCrossPort` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
  * `testRemoveCurlAuthorizationOptionsOnRedirectCrossScheme` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
  * `testRemoveCurlAuthorizationOptionsOnRedirectCrossSchemeSamePort` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* /** * @testWith ["digest"] * ["ntlm"] */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 163`, `args: 32`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 96`, `unreferenced_by_name: 23`
* *Architecture:* `api: 23`, `import: 11`
* *Defense:* `safety: 14`, `doc: 9`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` GuzzleHttp\Client, GuzzleHttp\Exception\BadResponseException, GuzzleHttp\Exception\TooManyRedirectsException, GuzzleHttp\HandlerStack, GuzzleHttp\Handler\MockHandler, GuzzleHttp\Middleware, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/HandlerStack.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.384)
- **Top Global Matches:** file_cluster_15: 5.384, file_cluster_11: 6.606, file_cluster_16: 6.65
- **Magnitude:** 186.46 | **LOC:** 276 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **3**; blast radius 17.878; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.8%), Guard Balance (formerly Safety Score) (78.0%), Complexity Load (formerly Cognitive Load) (34.3%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.878
  * `Choke Point (Betweenness):` 0.031475 | `Ripple Effect (Closeness):` 0.106667
  * `Imports (Out-Degree: 3):` GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/Handler/MockHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.517)
- **Top Global Matches:** file_cluster_4: 7.517, file_cluster_6: 9.559, file_cluster_15: 13.251
- **Magnitude:** 158.18 | **LOC:** 213 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **9**; blast radius 15.404; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.9%), Guard Balance (formerly Safety Score) (61.0%), Complexity Load (formerly Cognitive Load) (38.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.404
  * `Choke Point (Betweenness):` 0.016057 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 5):` GuzzleHttp\Exception\RequestException, GuzzleHttp\HandlerStack, GuzzleHttp\Promise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\TransferStats, GuzzleHttp\Utils, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/RedirectMiddleware.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.565)
- **Top Global Matches:** file_cluster_16: 7.565, file_cluster_15: 7.682, file_cluster_9: 7.704
- **Magnitude:** 156.88 | **LOC:** 229 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 8.197; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (67.7%), Complexity Load (formerly Cognitive Load) (34.6%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.197
  * `Choke Point (Betweenness):` 0.011542 | `Ripple Effect (Closeness):` 0.077419
  * `Imports (Out-Degree: 4):` GuzzleHttp\Exception\BadResponseException, GuzzleHttp\Exception\TooManyRedirectsException, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface, Psr\Http\Message\UriInterface
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/Cookie/CookieJarTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.61)
- **Top Global Matches:** file_cluster_11: 5.61, file_cluster_15: 6.443, file_cluster_16: 7.726
- **Magnitude:** 155.42 | **LOC:** 508 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.4%), Connectivity (formerly Api Exposure) (9.6%), Complexity Load (formerly Cognitive Load) (7.5%)
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
* *Structure:* `branch: 8`, `structural_boundaries: 96`, `args: 30`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 27`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* `doc: 9`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DateInterval, DateTime, DateTimeImmutable, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\Cookie\SetCookie, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response, PHPUnit\Framework\TestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Handler/CurlMultiHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.729)
- **Top Global Matches:** file_cluster_16: 6.729, file_cluster_12: 7.714, file_cluster_15: 7.971
- **Magnitude:** 143.4 | **LOC:** 288 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 19.124; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.4%), Guard Balance (formerly Safety Score) (65.7%), Complexity Load (formerly Cognitive Load) (37.9%)
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 7`, `doc: 14`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.124
  * `Choke Point (Betweenness):` 0.03608 | `Ripple Effect (Closeness):` 0.16
  * `Imports (Out-Degree: 3):` Closure, GuzzleHttp\Promise, GuzzleHttp\Promise\Promise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Utils, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/Handler/MockHandlerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.037)
- **Top Global Matches:** file_cluster_10: 7.037, file_cluster_11: 7.242, file_cluster_15: 8.941
- **Magnitude:** 137.66 | **LOC:** 263 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.8%), Connectivity (formerly Api Exposure) (11.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` GuzzleHttp\Exception\BadResponseException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Handler\MockHandler, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response, GuzzleHttp\Psr7\Stream, GuzzleHttp\TransferStats, PHPUnit\Framework\TestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cookie/CookieJarInterface.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.047)
- **Top Global Matches:** file_cluster_2: 5.047, file_cluster_17: 5.418, file_cluster_11: 5.647
- **Magnitude:** 127.59 | **LOC:** 81 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 7.537; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (55.4%), Complexity Load (formerly Cognitive Load) (10.5%), Connectivity (formerly Api Exposure) (8.8%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.537
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.078006
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Exception/RequestException.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.908)
- **Top Global Matches:** file_cluster_11: 5.908, file_cluster_15: 6.646, file_cluster_16: 7.382
- **Magnitude:** 117.76 | **LOC:** 151 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **5**; blast radius 22.072; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Guard Balance (formerly Safety Score) (70.9%), Complexity Load (formerly Cognitive Load) (32.7%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.072
  * `Choke Point (Betweenness):` 0.009613 | `Ripple Effect (Closeness):` 0.179787
  * `Imports (Out-Degree: 2):` GuzzleHttp\BodySummarizer, GuzzleHttp\BodySummarizerInterface, Psr\Http\Client\RequestExceptionInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tests/MiddlewareTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.578)
- **Top Global Matches:** file_cluster_11: 6.578, file_cluster_10: 6.892, file_cluster_15: 8.021
- **Magnitude:** 114.76 | **LOC:** 260 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.9%), Connectivity (formerly Api Exposure) (10.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` GuzzleHttp\BodySummarizer, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\Cookie\SetCookie, GuzzleHttp\Exception\ClientException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Exception\ServerException, GuzzleHttp\HandlerStack, GuzzleHttp\Handler\MockHandler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/PoolTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.772)
- **Top Global Matches:** file_cluster_10: 6.772, file_cluster_11: 7.768, file_cluster_16: 8.962
- **Magnitude:** 97.54 | **LOC:** 197 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.1%), Complexity Load (formerly Cognitive Load) (35.3%), Connectivity (formerly Api Exposure) (7.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` GuzzleHttp\Client, GuzzleHttp\Exception\ClientException, GuzzleHttp\HandlerStack, GuzzleHttp\Handler\MockHandler, GuzzleHttp\Pool, GuzzleHttp\Promise\Promise, GuzzleHttp\Psr7\Request, GuzzleHttp\Psr7\Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Cookie/SetCookieTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.307)
- **Top Global Matches:** file_cluster_11: 6.307, file_cluster_15: 6.452, file_cluster_2: 7.8
- **Magnitude:** 94.96 | **LOC:** 493 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.3%), Connectivity (formerly Api Exposure) (9.1%), Complexity Load (formerly Cognitive Load) (4.2%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testParseCookie` **(Many-Argument Workhorses)** (Impact: 15.7)
    * *Intent:* /** * @dataProvider cookieParserDataProvider */
  * `testValidatesCookies` **(Parameter Forwarders)** (Impact: 2.7)
    * *Intent:* /** * @dataProvider cookieValidateProvider */
  * `testHoldsValues` **(I/O & Config Routines)** (Impact: 2.5)
  * `testMatchesDomain` **(I/O & Config Routines)** (Impact: 2.5)
  * `cookieParserDataProvider` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* /** * Provides the parsed information from a cookie * * @return array */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 38`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 16`
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* `safety: 5`, `doc: 7`, `test: 48`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` GuzzleHttp\Cookie\SetCookie, PHPUnit\Framework\TestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Middleware.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.578)
- **Top Global Matches:** file_cluster_10: 6.578, file_cluster_15: 6.77, file_cluster_11: 7.15
- **Magnitude:** 91.68 | **LOC:** 269 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **7**; blast radius 14.85; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (98.2%), Guard Balance (formerly Safety Score) (54.2%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.85
  * `Choke Point (Betweenness):` 0.027896 | `Ripple Effect (Closeness):` 0.091139
  * `Imports (Out-Degree: 6):` GuzzleHttp\Cookie\CookieJarInterface, GuzzleHttp\Exception\RequestException, GuzzleHttp\Promise, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface, Psr\Log\LoggerInterface
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/PrepareBodyMiddleware.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.301)
- **Top Global Matches:** file_cluster_9: 6.301, file_cluster_15: 8.531, file_cluster_16: 8.758
- **Magnitude:** 88.82 | **LOC:** 106 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 7.537; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.0%), Debt Markers (formerly Tech Debt) (68.5%), Complexity Load (formerly Cognitive Load) (40.9%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.537
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.078006
  * `Imports (Out-Degree: 0):` GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/Handler/CurlHandlerTest.php` (PHP) | Magnitude: 39.84 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 38, state_mutation: 21, memory_alloc: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Cookie/SetCookie.php` (PHP) | Magnitude: 263.18 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 264, branch: 71, structural_boundaries: 61, state_mutation: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/RedirectMiddleware.php` (PHP) | Magnitude: 156.88 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 35, state_mutation: 31, branch: 25

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/ci.yml` -> Churn: **100.0%** | Cog Load: 3.4519% | Debt: 100.0%
- `.github/workflows/static.yml` -> Churn: **100.0%** | Cog Load: 0.0% | Debt: 99.9447%
- `src/Cookie/CookieJar.php` -> Churn: **100.0%** | Cog Load: 39.346% | Debt: 85.6401%
- `src/Middleware.php` -> Churn: **100.0%** | Cog Load: 14.4926% | Debt: 98.1899%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/Handler/StreamHandlerTest.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 340.04
- `src/Cookie/CookieJar.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 220.1
- `src/RedirectMiddleware.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 156.88
- `src/Middleware.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 91.68
- `tests/Server.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 84.22

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Utils.php` -> **Severity: 7.672** (Bridge: 0.0767 * Flux: 100.0%)
- `src/Client.php` -> **Severity: 4.51** (Bridge: 0.0451 * Flux: 100.0%)
- `src/Handler/CurlMultiHandler.php` -> **Severity: 3.608** (Bridge: 0.0361 * Flux: 100.0%)
- `src/HandlerStack.php` -> **Severity: 3.148** (Bridge: 0.0315 * Flux: 100.0%)
- `src/Middleware.php` -> **Severity: 2.783** (Bridge: 0.0279 * Flux: 99.7628%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Utils.php` -> **Severity: 17.51** (Embedded: 0.2483 * Error Risk: 70.5278%)
- `src/Exception/RequestException.php` -> **Severity: 12.741** (Embedded: 0.1798 * Error Risk: 70.8661%)
- `src/Handler/CurlMultiHandler.php` -> **Severity: 10.515** (Embedded: 0.16 * Error Risk: 65.7193%)
- `src/Handler/StreamHandler.php` -> **Severity: 10.166** (Embedded: 0.16 * Error Risk: 63.5358%)
- `src/TransferStats.php` -> **Severity: 9.862** (Embedded: 0.1637 * Error Risk: 60.2378%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Handler/CurlFactory.php` -> **Severity: 1953.764** (Blast Radius: 27.764 * Doc Risk: 70.3704%)
- `tests/bootstrap.php` -> **Severity: 1422.3** (Blast Radius: 14.223 * Doc Risk: 100.0%)
- `src/Utils.php` -> **Severity: 1286.888** (Blast Radius: 86.865 * Doc Risk: 14.8148%)
- `src/Handler/CurlHandler.php` -> **Severity: 1161.3** (Blast Radius: 19.355 * Doc Risk: 60.0%)
- `src/Cookie/CookieJar.php` -> **Severity: 940.208** (Blast Radius: 17.461 * Doc Risk: 53.8462%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3694 call pairs -- scoped 33.0%, unique 2.0%, ambiguous 6.1%, external 58.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 3660 | 33.2% | 2.0% | 6.1% | 58.6% |
| javascript | 34 | 11.8% | 0.0% | 0.0% | 88.2% |

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
