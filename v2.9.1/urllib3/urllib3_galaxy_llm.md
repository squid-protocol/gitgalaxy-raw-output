# ARCHITECTURAL_BRIEF: urllib3
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
- **Scope:** 45 analyzed artifact(s), 8201 LOC.
- **Load-bearing artifact:** `urllib3-2.6.3/src/urllib3/exceptions.py` -- 17 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `urllib3-2.6.3/src/urllib3/connection.py` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `urllib3-2.6.3/src/urllib3/response.py` at magnitude 1266.04 (structural weight, not risk).
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
| Total Artifacts | 52 |
| Analyzed Artifacts (Scanned) | 45 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 8201 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2659 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2648 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 28.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6329 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 42 | 8109 | 93.3% |
| PLAINTEXT | 1 | 0 | 2.2% |
| MARKDOWN | 1 | 0 | 2.2% |
| JAVASCRIPT | 1 | 92 | 2.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.693`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.69; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 44%, Large Core Modules (2) 16%, Large Core Modules (3) 11%, Data / Markup / Trivial 9%, Many-Argument Workhorses Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 43 | 95.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 4.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 47.1 | 46.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.6 | 79.0 | 90.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.8 | 14.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 42.2 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 88.7 | 33.0 | 32.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 17.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 86.1 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 45.6 | 4.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 66.4 | 75.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 98 | 22 | 8 | `urllib3-2.6.3/src/urllib3/response.py` |
| cleanup | 47 | 11 | 5 | `urllib3-2.6.3/src/urllib3/response.py` |
| guards | 667 | 35 | 41 | `urllib3-2.6.3/src/urllib3/response.py` |
| danger | 364 | 33 | 22 | `urllib3-2.6.3/src/urllib3/response.py` |
| concurrency | 220 | 16 | 12 | `urllib3-2.6.3/dummyserver/app.py` |
| connectivity | 519 | 40 | 28 | `urllib3-2.6.3/src/urllib3/response.py` |
| io | 187 | 23 | 16 | `urllib3-2.6.3/dummyserver/socketserver.py` |
| crypto | 23 | 13 | 1 | `urllib3-2.6.3/src/urllib3/contrib/pyopenssl.py` |
| ipc | 2 | 2 | 0 | `urllib3-2.6.3/dummyserver/testcase.py` |
| time | 9 | 2 | 0 | `urllib3-2.6.3/dummyserver/app.py` |
| serialization | 1 | 1 | 0 | `urllib3-2.6.3/src/urllib3/contrib/emscripten/emscripten_fetch_worker.js` |
| regex | 16 | 5 | 1 | `urllib3-2.6.3/src/urllib3/util/url.py` |
| events | 31 | 9 | 3 | `urllib3-2.6.3/dummyserver/asgi_proxy.py` |
| tests | 5 | 2 | 0 | `urllib3-2.6.3/dummyserver/testcase.py` |
| docs | 250 | 32 | 14 | `urllib3-2.6.3/src/urllib3/exceptions.py` |
| debt | 55 | 17 | 5 | `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py` |
| mutation | 3540 | 41 | 199 | `urllib3-2.6.3/src/urllib3/connection.py` |
| dead_code | 29 | 15 | 2 | `urllib3-2.6.3/dummyserver/testcase.py` |
| credential | 2 | 1 | 0 | `urllib3-2.6.3/src/urllib3/util/url.py` |
| threat | 98 | 18 | 9 | `urllib3-2.6.3/src/urllib3/response.py` |
| ml_ai | 1 | 1 | 0 | `urllib3-2.6.3/src/urllib3/__init__.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.2**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `urllib3-2.6.3/dummyserver/socketserver.py` (Hits: 27)
- `urllib3-2.6.3/src/urllib3/connection.py` (Hits: 27)
- `urllib3-2.6.3/dummyserver/hypercornserver.py` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **exceptions.py** (`urllib3-2.6.3/src/urllib3/exceptions.py`) — 17 inbound connections
2. **_base_connection.py** (`urllib3-2.6.3/src/urllib3/_base_connection.py`) — 10 inbound connections
3. **url.py** (`urllib3-2.6.3/src/urllib3/util/url.py`) — 10 inbound connections
4. **connectionpool.py** (`urllib3-2.6.3/src/urllib3/connectionpool.py`) — 8 inbound connections
5. **timeout.py** (`urllib3-2.6.3/src/urllib3/util/timeout.py`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **connection.py** (`urllib3-2.6.3/src/urllib3/connection.py`) — 29 outbound dependencies
2. **connectionpool.py** (`urllib3-2.6.3/src/urllib3/connectionpool.py`) — 26 outbound dependencies
3. **response.py** (`urllib3-2.6.3/src/urllib3/response.py`) — 25 outbound dependencies
4. **poolmanager.py** (`urllib3-2.6.3/src/urllib3/poolmanager.py`) — 21 outbound dependencies
5. **__init__.py** (`urllib3-2.6.3/src/urllib3/__init__.py`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `urlopen` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/connectionpool.py`) -> Impact: **142.1** | LOC: 369
- `_ssl_wrap_socket_and_match_hostname` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> Impact: **109.2** | LOC: 123
- `increment` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/util/retry.py`) -> Impact: **81.2** | LOC: 96
- `create_urllib3_context` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/util/ssl_.py`) -> Impact: **78.2** | LOC: 150
- `request` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> Impact: **74.4** | LOC: 96
  * *Intent:* # `request` method's signature intentionally violates LSP. # urllib3's API is different from `http.client.HTTPConnection` and the subclassing is only ...
- `match_hostname` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/util/ssl_match_hostname.py`) -> Impact: **55.2** | LOC: 65
- `ssl_wrap_socket` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/util/ssl_.py`) -> Impact: **52.2** | LOC: 72
- `read` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/response.py`) -> Impact: **51.7** | LOC: 95
- `_make_request` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/connectionpool.py`) -> Impact: **46.4** | LOC: 180
- `read1` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/response.py`) -> Impact: **45.5** | LOC: 69

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `urllib3-2.6.3/src/urllib3` | 12 | 4051.9 | 39.55% | 16.34% |
| `urllib3-2.6.3/src/urllib3/util` | 13 | 2049.74 | 39.83% | 9.12% |
| `urllib3-2.6.3/dummyserver` | 6 | 1492.68 | 68.29% | 14.67% |
| `urllib3-2.6.3/src/urllib3/http2` | 3 | 413.16 | 57.4% | 36.21% |
| `urllib3-2.6.3/src/urllib3/contrib/emscripten` | 6 | 9.9 | 56.58% | 16.3% |
| `urllib3-2.6.3/src/urllib3/contrib` | 3 | 4.37 | 36.71% | 0.0% |
| `urllib3-2.6.3` | 2 | 3.46 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py` -> **97.8154%** Exposure
- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **97.6035%** Exposure
- `urllib3-2.6.3/src/urllib3/util/response.py` -> **81.7574%** Exposure
- `urllib3-2.6.3/dummyserver/testcase.py` -> **71.198%** Exposure
- `urllib3-2.6.3/src/urllib3/http2/probe.py` -> **50.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `urllib3-2.6.3/dummyserver/app.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/hypercornserver.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/socketserver.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/_collections.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/connection.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py` -> **0** Orphaned Functions | **12** Duplicates
- `urllib3-2.6.3/dummyserver/testcase.py` -> **4** Orphaned Functions | **2** Duplicates
- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **0** Orphaned Functions | **2** Duplicates
- `urllib3-2.6.3/src/urllib3/response.py` -> **0** Orphaned Functions | **2** Duplicates
- `urllib3-2.6.3/src/urllib3/http2/probe.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `286` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `urllib3-2.6.3/src/urllib3/response.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1266.04 | **LOC:** 1481 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 7.639; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 89.2617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(Many-Argument Workhorses)** (Impact: 51.7)
  * `read1` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `read_chunked` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `_fp_read` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `_raw_read` **(Many-Argument Workhorses)** (Impact: 34.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 154 instances
* *State Mutation (weighted view):* 491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 270`, `args: 82`, `func_start: 82`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 183`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 73`, `import: 27`
* *Defense:* `safety: 45`, `doc: 20`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.639
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` , ._base_connection, ._collections, .connection, .connectionpool, .exceptions, .util.response, .util.retry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/dummyserver/app.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 790.14 | **LOC:** 484 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 12.428; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Complexity Load (formerly Cognitive Load) (86.0%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pyodide_upload` **(Compute Cores)** (Impact: 10.0)
  * `encodingrequest` **(I/O & Config Routines)** (Impact: 7.0)
  * `upload` **(Type Conversions)** (Impact: 6.4)
  * `_get_pyodide_template` **(Stateful Encapsulated Methods)** (Impact: 5.6)
    * *Intent:* # serve code to run pyodide in a webworker, or html template # these are included in pytest_pyodide,...
  * `successful_retry` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* """First return an error and then success It's not currently very flexible as the number of retries ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 62 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 404
* *State Mutation (weighted view):* 232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 188`, `args: 42`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 96`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 39`, `concurrency: 94`, `import: 15`
* *Defense:* `safety: 4`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.428
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.045455
  * `Imports (Out-Degree: 0):` __future__, collections, collections.abc, contextlib, datetime, email.utils, gzip, io...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/connection.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 780.7 | **LOC:** 1100 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 11.968; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.5%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_ssl_wrap_socket_and_match_hostname` **(Many-Argument Workhorses)** (Impact: 109.2)
  * `request` **(Many-Argument Workhorses)** (Impact: 74.4)
    * *Intent:* # `request` method's signature intentionally violates LSP. # urllib3's API is different from `http.c...
  * `connect` **(I/O & Config Routines)** (Impact: 33.7)
    * *Intent:* # Today we don't need to be doing this step before the /actual/ socket # connection, however in the ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `set_cert` **(Many-Argument Workhorses)** (Impact: 25.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 140`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 143`, `dead_code: 2`, `planned_debt: 4`
* *Architecture:* `io: 27`, `api: 24`, `concurrency: 3`, `import: 37`
* *Defense:* `safety: 21`, `doc: 17`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.968
  * `Choke Point (Betweenness):` 0.01154 | `Ripple Effect (Closeness):` 0.045455
  * `Imports (Out-Degree: 13):` ._base_connection, ._collections, ._version, .exceptions, .http2, .response, .util, .util.request...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/connectionpool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 614.58 | **LOC:** 1179 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **26**; blast radius 106.876; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.9%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `urlopen` **(Many-Argument Workhorses)** (Impact: 142.1)
  * `_make_request` **(Many-Argument Workhorses)** (Impact: 46.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `is_same_host` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* """ Check if the given ``url`` is a member of the same host as this connection pool. """
  * `_get_conn` **(Stateful Encapsulated Methods)** (Impact: 14.0)
    * *Intent:* """ Get a connection. Will return a pooled connection if one is available. If no connections are ava...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 130`, `args: 27`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 100`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 12`, `import: 30`
* *Defense:* `safety: 32`, `doc: 21`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 106.876
  * `Choke Point (Betweenness):` 0.143605 | `Ripple Effect (Closeness):` 0.3126
  * `Imports (Out-Degree: 12):` ._base_connection, ._collections, ._request_methods, .connection, .exceptions, .response, .util.connection, .util.proxy...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/poolmanager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 420.1 | **LOC:** 652 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 9.984; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 89.6552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `urlopen` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `_default_key_normalizer` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `_new_pool` **(Many-Argument Workhorses)** (Impact: 16.5)
  * `connection_from_host` **(Many-Argument Workhorses)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 84`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 87`, `dead_code: 1`
* *Architecture:* `api: 15`, `import: 20`
* *Defense:* `safety: 7`, `doc: 14`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.003013 | `Ripple Effect (Closeness):` 0.045455
  * `Imports (Out-Degree: 9):` ._collections, ._request_methods, .connection, .connectionpool, .exceptions, .response, .util.connection, .util.proxy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/retry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 382.84 | **LOC:** 550 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **14**; blast radius 85.133; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 60.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `increment` **(Many-Argument Workhorses)** (Impact: 81.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 28.5)
  * `is_retry` **(Many-Argument Workhorses)** (Impact: 16.7)
  * `from_int` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `parse_retry_after` **(Compute Cores)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 69`, `args: 17`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 63`
* *Architecture:* `api: 14`, `import: 14`
* *Defense:* `safety: 4`, `doc: 11`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 85.133
  * `Choke Point (Betweenness):` 0.010897 | `Ripple Effect (Closeness):` 0.30721
  * `Imports (Out-Degree: 3):` ..connectionpool, ..exceptions, ..response, .util, __future__, email, itertools, logging...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/_collections.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 372.22 | **LOC:** 488 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 25.424; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.0%)
- **Documentation Coverage:** 84.127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extend` **(Defensive Guards)** (Impact: 29.6)
    * *Intent:* """Generic import function for any type of header-like object. Adapted version of MutableMapping.upd...
  * `add` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* """Adds a (name, value) pair, doesn't overwrite the value if it already exists. If this is called wi...
  * `ensure_can_construct_http_header_dict` **(Defensive Guards)** (Impact: 10.8)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 10.5)
  * `__setitem__` **(Defensive Guards)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 110`, `args: 42`, `func_start: 42`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 63`, `dead_code: 1`
* *Architecture:* `api: 26`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 28`, `doc: 9`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.261831
  * `Imports (Out-Degree: 0):` Protocol, __future__, collections, enum, function, threading, typing, typing_extensions
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/ssl_.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 358.6 | **LOC:** 528 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 30.953; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 48.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_urllib3_context` **(Many-Argument Workhorses)** (Impact: 78.2)
  * `ssl_wrap_socket` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `assert_fingerprint` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* """ Checks if given fingerprint matches the supplied certificate. :param cert: Certificate as bytes ...
  * `_is_bpo_43522_fixed` **(Stateful Encapsulated Methods)** (Impact: 13.2)
  * `_ssl_wrap_socket_impl` **(Stateful Encapsulated Methods)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`, `dead_code: 2`
* *Architecture:* `io: 16`, `api: 8`, `import: 17`
* *Defense:* `safety: 12`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.953
  * `Choke Point (Betweenness):` 0.020921 | `Ripple Effect (Closeness):` 0.189555
  * `Imports (Out-Degree: 3):` ..exceptions, .ssltransport, .url, __future__, binascii, hashlib, hmac, os...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/url.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 352.26 | **LOC:** 470 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 59.158; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_url` **(Compute Cores)** (Impact: 41.9)
    * *Intent:* """ Given a url, return a parsed :class:`.Url` namedtuple. Best-effort is performed to parse incompl...
  * `_normalize_host` **(Stateful Encapsulated Methods)** (Impact: 29.1)
  * `_encode_invalid_chars` **(Stateful Encapsulated Methods)** (Impact: 17.3)
  * `_remove_path_dot_segments` **(Stateful Encapsulated Methods)** (Impact: 14.1)
    * *Intent:* # See http://tools.ietf.org/html/rfc3986#section-5.2.4 for pseudo-code segments = path.split("/") # ...
  * `url` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* """ Convert self into a url This function should more or less round-trip with :func:`.parse_url`. Th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 55`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `safety: 5`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.158
  * `Choke Point (Betweenness):` 0.026559 | `Ripple Effect (Closeness):` 0.356364
  * `Imports (Out-Degree: 2):` ..exceptions, .util, __future__, idna, re, typing, urllib3
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/http2/connection.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 306.84 | **LOC:** 357 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 7.639; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.3%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `send` **(Defensive Guards)** (Impact: 28.2)
    * *Intent:* """Send data to the server. `data` can be: `str`, `bytes`, an iterable, or file-like objects that su...
  * `putrequest` **(Stateful Encapsulated Methods)** (Impact: 19.4)
  * `getresponse` **(Defensive Guards)** (Impact: 17.6)
  * `putheader` **(Defensive Guards)** (Impact: 16.6)
    * *Intent:* # TODO SKIPPABLE_HEADERS from urllib3 are ignored. header = header.encode() if isinstance(header, st...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 73`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 48`, `planned_debt: 5`
* *Architecture:* `api: 16`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 13`, `doc: 6`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.639
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .._base_connection, .._collections, ..connection, ..exceptions, ..response, __future__, h2.config, h2.connection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/dummyserver/testcase.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 286.78 | **LOC:** 354 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 7.639; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Complexity Load (formerly Cognitive Load) (83.1%)
- **Documentation Coverage:** 86.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start_response_handler` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `assert_header_received` **(Defensive Guards)** (Impact: 14.3)
  * `socket_handler` **(Defensive Guards)** (Impact: 12.6)
  * `consume_socket` **(Defensive Guards)** (Impact: 10.9)
  * `consume_request` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* """ Consume a socket until after the HTTP request is sent. """
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 74`, `args: 19`, `func_start: 19`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 50`, `duplicate_logic: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 15`, `api: 24`, `concurrency: 13`, `import: 14`
* *Defense:* `safety: 8`, `doc: 4`, `test: 4`, `sync_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.639
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, contextlib, dummyserver.app, dummyserver.asgi_proxy, dummyserver.hypercornserver, dummyserver.socketserver, pytest, socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/util/ssltransport.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 257.06 | **LOC:** 272 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 18.218; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 96.2264% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makefile` **(Many-Argument Workhorses)** (Impact: 42.2)
  * `_ssl_io_loop` **(Stateful Encapsulated Methods)** (Impact: 26.4)
  * `_wrap_ssl_read` **(Stateful Encapsulated Methods)** (Impact: 8.4)
  * `recv_into` **(Generic / Templated Code)** (Impact: 7.3)
  * `sendall` **(Type Conversions)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 68`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`, `planned_debt: 1`
* *Architecture:* `io: 16`, `api: 25`, `import: 8`
* *Defense:* `safety: 7`, `doc: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.218
  * `Choke Point (Betweenness):` 0.001498 | `Ripple Effect (Closeness):` 0.152292
  * `Imports (Out-Degree: 2):` ..exceptions, .ssl_, __future__, io, socket, ssl, typing, typing_extensions
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/fields.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 186.24 | **LOC:** 342 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 18.636; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.5%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 45.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 14.6)
  * `format_header_param_rfc2231` **(Many-Argument Workhorses)** (Impact: 14.4)
    * *Intent:* """ Helper function to format and quote a single header parameter using the strategy defined in RFC ...
  * `from_tuples` **(Many-Argument Workhorses)** (Impact: 13.3)
  * `_render_parts` **(Stateful Encapsulated Methods)** (Impact: 10.2)
  * `render_headers` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* """ Renders the headers for this request field. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 33`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 32`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 5`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.636
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.149303
  * `Imports (Out-Degree: 0):` __future__, email.utils, mimetypes, typing, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/request.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 180.84 | **LOC:** 264 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 16.657; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (58.1%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_headers` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `body_to_chunks` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `rewind_body` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* """ Attempt to rewind body to a certain position. Primarily used for request redirects and retries. ...
  * `set_file_position` **(Defensive Guards)** (Impact: 6.1)
  * `chunk_readable` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 44`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 32`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 6`, `import: 13`
* *Defense:* `safety: 20`, `doc: 4`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.657
  * `Choke Point (Betweenness):` 0.000282 | `Ripple Effect (Closeness):` 0.228438
  * `Imports (Out-Degree: 2):` ..exceptions, .util, __future__, backports, base64, brotli, brotlicffi, compression...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/asgi_proxy.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 157.3 | **LOC:** 115 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 8.721; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Guard Balance (formerly Safety Score) (90.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `absolute_uri` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `__call__` **(Defensive Guards)** (Impact: 9.4)
  * `connect` **(Type Conversions)** (Impact: 7.2)
  * `_read_body` **(Stateful Encapsulated Methods)** (Impact: 6.2)
  * `start_forward` **(Defensive Guards)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 66
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 45`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 21`, `import: 6`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.721
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022727
  * `Imports (Out-Degree: 0):` __future__, httpx, hypercorn.typing, ssl, trio, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/socketserver.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 142.62 | **LOC:** 191 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 8.721; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.8%), Guard Balance (formerly Safety Score) (96.3%), Complexity Load (formerly Cognitive Load) (54.4%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ssl_options_to_context` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `_start_server` **(Stateful Encapsulated Methods)** (Impact: 8.1)
  * `_has_ipv6` **(Stateful Encapsulated Methods)** (Impact: 5.3)
    * *Intent:* """Returns True if the system can bind an IPv6 address."""
  * `_resolves_to_ipv6` **(Stateful Encapsulated Methods)** (Impact: 4.8)
    * *Intent:* """Returns True if the system resolves host to an IPv6 address by default."""
  * `__init__` **(Generic / Templated Code)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 39`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 30`
* *Architecture:* `io: 27`, `api: 7`, `concurrency: 4`, `import: 15`
* *Defense:* `safety: 3`, `doc: 5`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.721
  * `Choke Point (Betweenness):` 0.001498 | `Ripple Effect (Closeness):` 0.022727
  * `Imports (Out-Degree: 2):` __future__, cryptography.hazmat.backends, cryptography.hazmat.primitives, logging, os, socket, ssl, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/ssl_match_hostname.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 139.02 | **LOC:** 160 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 15.936; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match_hostname` **(Many-Argument Workhorses)** (Impact: 55.2)
  * `_dnsname_match` **(Many-Argument Workhorses)** (Impact: 22.7)
  * `_ipaddress_match` **(Stateful Encapsulated Methods)** (Impact: 2.4)
    * *Intent:* """Exact matching of IP addresses. RFC 9110 section 4.3.5: "A reference identity of IP-ID contains t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 22`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 19`
* *Architecture:* `io: 1`, `api: 2`, `import: 6`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.936
  * `Choke Point (Betweenness):` 0.023256 | `Ripple Effect (Closeness):` 0.228438
  * `Imports (Out-Degree: 1):` .ssl_, __future__, ipaddress, re, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 133.5 | **LOC:** 336 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **11**; blast radius 151.183; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.6%), Connectivity (formerly Api Exposure) (88.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* # TODO(t-8ch): Stop inheriting from AssertionError in v2.0. # 'localhost' is here because our URL pa...
  * `__init__` **(Generic / Templated Code)** (Impact: 4.2)
  * `pool` **(Generic / Templated Code)** (Impact: 3.3)
  * `__init__` **(Generic / Templated Code)** (Impact: 2.6)
  * `__init__` **(Generic / Templated Code)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 88`, `args: 21`, `func_start: 21`, `class_start: 38`
* *Risk/State:* `state_mutation: 29`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 39`, `import: 10`
* *Defense:* `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 151.183
  * `Choke Point (Betweenness):` 0.114341 | `Ripple Effect (Closeness):` 0.43459
  * `Imports (Out-Degree: 2):` .connection, .connectionpool, .response, .util.retry, __future__, a, email.errors, http.client...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/_request_methods.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 127.02 | **LOC:** 279 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 16.152; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.3%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 36.9)
  * `request_encode_body` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `request_encode_url` **(Many-Argument Workhorses)** (Impact: 9.7)
  * `urlopen` **(Generic / Templated Code)** (Impact: 3.7)
  * `__init__` **(Generic / Templated Code)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 26`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `planned_debt: 2`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.152
  * `Choke Point (Betweenness):` 0.028717 | `Ripple Effect (Closeness):` 0.222727
  * `Imports (Out-Degree: 3):` ._base_connection, ._collections, .filepost, .response, __future__, json, typing, urllib.parse
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/hypercornserver.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 105.32 | **LOC:** 147 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 8.721; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (95.3%), Guard Balance (formerly Safety Score) (92.5%), Complexity Load (formerly Cognitive Load) (86.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_hypercorn_in_thread` **(Defensive Guards)** (Impact: 11.4)
  * `_create_urllib3_sockets` **(Stateful Encapsulated Methods)** (Impact: 8.2)
  * `_retry_create_urllib3_sockets` **(Stateful Encapsulated Methods)** (Impact: 6.2)
    * *Intent:* # When we request a socket with host localhost and port zero, Hypercorn # only binds to IPv4. But we...
  * `create_sockets` **(Defensive Guards)** (Impact: 4.7)
  * `_start_server` **(Stateful Encapsulated Methods)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 41`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 23`, `planned_debt: 1`
* *Architecture:* `io: 20`, `api: 4`, `concurrency: 3`, `import: 17`
* *Defense:* `safety: 6`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.721
  * `Choke Point (Betweenness):` 0.000264 | `Ripple Effect (Closeness):` 0.022727
  * `Imports (Out-Degree: 2):` .app, __future__, anyio.abc, anyio.to_thread, contextlib, errno, functools, hypercorn...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/connection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 90.9 | **LOC:** 138 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 28.005; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (35.6%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_connection` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* # This function is copied from socket.py in the Python 2.7 standard # library test suite. Added to i...
  * `_set_socket_options` **(Stateful Encapsulated Methods)** (Impact: 5.6)
  * `_has_ipv6` **(Stateful Encapsulated Methods)** (Impact: 5.3)
    * *Intent:* """Returns True if the system can bind an IPv6 address."""
  * `allowed_gai_family` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* """This function is designed to work in the context of getaddrinfo, where family=socket.AF_UNSPEC is...
  * `is_connection_dropped` **(Generic / Templated Code)** (Impact: 1.7)
    * *Intent:* """ Returns True if the connection is dropped and should be closed. :param conn: :class:`urllib3.con...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 23`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`
* *Architecture:* `io: 16`, `api: 3`, `import: 6`
* *Defense:* `safety: 7`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.005
  * `Choke Point (Betweenness):` 0.005814 | `Ripple Effect (Closeness):` 0.262032
  * `Imports (Out-Degree: 3):` .._base_connection, ..exceptions, .timeout, __future__, socket, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/wait.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 90.72 | **LOC:** 125 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 9.664; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%), Complexity Load (formerly Cognitive Load) (51.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `select_wait_for_socket` **(Many-Argument Workhorses)** (Impact: 16.8)
    * *Intent:* # # Now, how do we choose between select() and poll()? On traditional Unixes, # select() has a stran...
  * `poll_wait_for_socket` **(Generic / Templated Code)** (Impact: 14.6)
  * `wait_for_socket` **(Defensive Guards)** (Impact: 7.5)
  * `do_poll` **(Generic / Templated Code)** (Impact: 3.0)
    * *Intent:* # For some reason, poll() takes timeout in milliseconds
  * `_have_working_poll` **(Stateful Encapsulated Methods)** (Impact: 2.5)
    * *Intent:* # Apparently some systems have a select.poll that fails as soon as you try # to use it, either due t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 22`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `io: 11`, `api: 7`, `import: 4`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060606
  * `Imports (Out-Degree: 0):` __future__, but, functools, select, socket, time
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/timeout.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 85.84 | **LOC:** 276 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **7**; blast radius 39.984; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 27.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_validate_timeout` **(Stateful Encapsulated Methods)** (Impact: 20.0)
    * *Intent:* """Check that a timeout attribute is valid. :param value: The timeout value to validate :param name:...
  * `read_timeout` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* """Get the value for the read timeout. This assumes some time has elapsed in the connection timeout ...
  * `connect_timeout` **(Generic / Templated Code)** (Impact: 6.5)
    * *Intent:* """Get the value to use when setting a connection timeout. This will be a positive float or integer,...
  * `get_connect_duration` **(Generic / Templated Code)** (Impact: 4.9)
    * *Intent:* """Gets the time elapsed since the call to :meth:`start_connect`. :return: Elapsed time in seconds. ...
  * `resolve_default_timeout` **(Generic / Templated Code)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 42`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 9`, `import: 7`
* *Defense:* `safety: 4`, `doc: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.984
  * `Choke Point (Betweenness):` 0.005876 | `Ripple Effect (Closeness):` 0.29697
  * `Imports (Out-Degree: 1):` ..exceptions, __future__, enum, socket, time, typing, urllib3
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/http2/probe.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 83.7 | **LOC:** 88 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.639; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Complexity Load (formerly Cognitive Load) (66.3%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_and_release` **(Generic / Templated Code)** (Impact: 9.6)
  * `acquire_and_get` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* # By the end of this block we know that # _cache_[values,locks] is available. value = None with self...
  * `_values` **(Encapsulated Accessors)** (Impact: 3.0)
    * *Intent:* """This function is for testing purposes only. Gets the current state of the probe cache"""
  * `_reset` **(Encapsulated Accessors)** (Impact: 1.7)
    * *Intent:* """This function is for testing purposes only. Reset the cache values"""
  * `__init__` **(Encapsulated Accessors)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 20`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 5`, `doc: 2`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.639
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, threading
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/filepost.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 50.96 | **LOC:** 90 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 12.937; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.5%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode_multipart_formdata` **(Many-Argument Workhorses)** (Impact: 12.3)
  * `iter_field_objects` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* """ Iterate over fields. Supports list of (k, v) tuples and dicts, and lists of :class:`~urllib3.fie...
  * `choose_boundary` **(Generic / Templated Code)** (Impact: 1.2)
    * *Intent:* """ Our embarrassingly-simple replacement for mimetools.choose_boundary. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 3`, `import: 7`
* *Defense:* `safety: 4`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.937
  * `Choke Point (Betweenness):` 0.015328 | `Ripple Effect (Closeness):` 0.178632
  * `Imports (Out-Degree: 1):` .fields, __future__, binascii, codecs, io, os, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `urllib3-2.6.3/src/urllib3/connectionpool.py` -> **Severity: 14.36** (Bridge: 0.1436 * Flux: 99.9995%)
- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **Severity: 11.429** (Bridge: 0.1143 * Flux: 99.9593%)
- `urllib3-2.6.3/src/urllib3/_request_methods.py` -> **Severity: 2.872** (Bridge: 0.0287 * Flux: 99.9937%)
- `urllib3-2.6.3/src/urllib3/util/url.py` -> **Severity: 2.656** (Bridge: 0.0266 * Flux: 100.0%)
- `urllib3-2.6.3/src/urllib3/util/ssl_match_hostname.py` -> **Severity: 2.326** (Bridge: 0.0233 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `urllib3-2.6.3/src/urllib3/util/url.py` -> **Severity: 34.265** (Embedded: 0.3564 * Error Risk: 96.1513%)
- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **Severity: 33.511** (Embedded: 0.4346 * Error Risk: 77.1102%)
- `urllib3-2.6.3/src/urllib3/util/retry.py` -> **Severity: 29.535** (Embedded: 0.3072 * Error Risk: 96.1379%)
- `urllib3-2.6.3/src/urllib3/connectionpool.py` -> **Severity: 27.478** (Embedded: 0.3126 * Error Risk: 87.9001%)
- `urllib3-2.6.3/src/urllib3/util/connection.py` -> **Severity: 24.596** (Embedded: 0.262 * Error Risk: 93.8683%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **Severity: 15118.3** (Blast Radius: 151.183 * Doc Risk: 100.0%)
- `urllib3-2.6.3/src/urllib3/util/util.py` -> **Severity: 7995.7** (Blast Radius: 79.957 * Doc Risk: 100.0%)
- `urllib3-2.6.3/src/urllib3/connectionpool.py` -> **Severity: 5343.8** (Blast Radius: 106.876 * Doc Risk: 50.0%)
- `urllib3-2.6.3/src/urllib3/util/retry.py` -> **Severity: 5168.791** (Blast Radius: 85.133 * Doc Risk: 60.7143%)
- `urllib3-2.6.3/src/urllib3/util/url.py` -> **Severity: 2957.9** (Blast Radius: 59.158 * Doc Risk: 50.0%)

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
