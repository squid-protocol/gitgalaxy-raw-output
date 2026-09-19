# ARCHITECTURAL_BRIEF: sse-starlette
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
- **Scope:** 15 analyzed artifact(s), 1338 LOC.
- **Load-bearing artifact:** `sse_starlette-3.3.4/sse_starlette/sse.py` -- 7 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `sse_starlette-3.3.4/sse_starlette/sse.py` -- pulls in 15 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `sse_starlette-3.3.4/tests/test_multi_loop.py` at magnitude 474.1 (structural weight, not risk).
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
| Total Artifacts | 20 |
| Analyzed Artifacts (Scanned) | 15 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 1338 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 75.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2917 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2281 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 12 | 1338 | 80.0% |
| PLAINTEXT | 2 | 0 | 13.3% |
| MARKDOWN | 1 | 0 | 6.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 47%, Data / Markup / Trivial 33%, Large Core Modules (3) 20%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 12 | 80.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 20.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 49.9 | 23.2 | 25.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.1 | 57.9 | 60.8 | 62.6 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 35.9 | 15.5 | 11.1 | 20.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 58.3 | 100.0 | 100.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 1.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 58.3 | 62.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 31 | 6 | 5 | `sse_starlette-3.3.4/tests/test_event.py` |
| cleanup | 4 | 2 | 1 | `sse_starlette-3.3.4/tests/test_multi_loop.py` |
| guards | 149 | 10 | 28 | `sse_starlette-3.3.4/tests/test_multi_loop.py` |
| danger | 42 | 9 | 9 | `sse_starlette-3.3.4/sse_starlette/sse.py` |
| concurrency | 331 | 8 | 76 | `sse_starlette-3.3.4/tests/test_multi_loop.py` |
| connectivity | 134 | 11 | 27 | `sse_starlette-3.3.4/tests/test_sse.py` |
| io | 6 | 2 | 1 | `sse_starlette-3.3.4/tests/conftest.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `sse_starlette-3.3.4/sse_starlette/event.py` |
| events | 26 | 3 | 7 | `sse_starlette-3.3.4/sse_starlette/sse.py` |
| tests | 128 | 7 | 29 | `sse_starlette-3.3.4/tests/test_sse.py` |
| docs | 60 | 8 | 12 | `sse_starlette-3.3.4/sse_starlette/sse.py` |
| debt | 31 | 6 | 5 | `sse_starlette-3.3.4/tests/test_issue167.py` |
| mutation | 473 | 11 | 79 | `sse_starlette-3.3.4/sse_starlette/sse.py` |
| dead_code | 51 | 8 | 9 | `sse_starlette-3.3.4/tests/test_sse.py` |
| credential | 0 | 0 | 0 | - |
| threat | 8 | 1 | 0 | `sse_starlette-3.3.4/sse_starlette/sse.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.9**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `sse_starlette-3.3.4/tests/conftest.py` (Hits: 5)
- `sse_starlette-3.3.4/tests/anyio_compat.py` (Hits: 1)
- `sse_starlette-3.3.4/AUTHORS` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sse.py** (`sse_starlette-3.3.4/sse_starlette/sse.py`) — 7 inbound connections
2. **event.py** (`sse_starlette-3.3.4/sse_starlette/event.py`) — 3 inbound connections
3. **anyio_compat.py** (`sse_starlette-3.3.4/tests/anyio_compat.py`) — 2 inbound connections
4. **AUTHORS** (`sse_starlette-3.3.4/AUTHORS`) — 0 inbound connections
5. **MANIFEST.in** (`sse_starlette-3.3.4/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sse.py** (`sse_starlette-3.3.4/sse_starlette/sse.py`) — 15 outbound dependencies
2. **conftest.py** (`sse_starlette-3.3.4/tests/conftest.py`) — 13 outbound dependencies
3. **test_sse.py** (`sse_starlette-3.3.4/tests/test_sse.py`) — 11 outbound dependencies
4. **test_multi_loop.py** (`sse_starlette-3.3.4/tests/test_multi_loop.py`) — 6 outbound dependencies
5. **test_issue132.py** (`sse_starlette-3.3.4/tests/test_issue132.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `sse_starlette-3.3.4/sse_starlette/sse.py`) -> Impact: **46.2** | LOC: 72
- `encode` **(Defensive Guards)** (@ `sse_starlette-3.3.4/sse_starlette/event.py`) -> Impact: **14.1** | LOC: 28
- `test_response_send_whenValidInput_thenGeneratesExpectedOutput` **(Many-Argument Workhorses)** (@ `sse_starlette-3.3.4/tests/test_sse.py`) -> Impact: **13.8** | LOC: 32
- `test_shutdownGracePeriod_whenGeneratorExitsInTime_thenCleanShutdown` **(Defensive Guards)** (@ `sse_starlette-3.3.4/tests/test_issue167.py`) -> Impact: **13.0** | LOC: 63
  * *Intent:* """Generator that sees shutdown_event and exits within grace period should complete without CancelledError."""
- `test_eventSourceResponse_whenUsingMemoryChannel_thenHandlesAsyncQueueCorrectly` **(Many-Argument Workhorses)** (@ `sse_starlette-3.3.4/tests/test_sse.py`) -> Impact: **12.8** | LOC: 56
- `app` **(Many-Argument Workhorses)** (@ `sse_starlette-3.3.4/tests/test_sse.py`) -> Impact: **11.6** | LOC: 32
  * *Intent:* # Arrange # Create bounded memory channel for producer-consumer communication send_chan, recv_chan = anyio.create_memory_object_stream( max_buffer_siz...
- `app` **(Type Conversions)** (@ `sse_starlette-3.3.4/tests/test_sse.py`) -> Impact: **10.8** | LOC: 16
  * *Intent:* # Arrange
- `stream_numbers` **(Type Conversions)** (@ `sse_starlette-3.3.4/tests/test_sse.py`) -> Impact: **10.8** | LOC: 15
  * *Intent:* # Producer function that writes to the channel
- `mock_send` **(Defensive Guards)** (@ `sse_starlette-3.3.4/tests/test_issue167.py`) -> Impact: **10.7** | LOC: 6
- `_stream_response` **(Stateful Encapsulated Methods)** (@ `sse_starlette-3.3.4/sse_starlette/sse.py`) -> Impact: **10.0** | LOC: 27
  * *Intent:* """Send out SSE data to the client as it becomes available in the iterator."""

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `sse_starlette-3.3.4/tests` | 9 | 1723.16 | 20.46% | 0.0% |
| `sse_starlette-3.3.4/sse_starlette` | 3 | 470.62 | 31.61% | 0.0% |
| `sse_starlette-3.3.4` | 3 | 10.88 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **100.0%** Exposure
- `sse_starlette-3.3.4/sse_starlette/event.py` -> **99.9982%** Exposure
- `sse_starlette-3.3.4/sse_starlette/__init__.py` -> **31.0026%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sse_starlette-3.3.4/tests/test_issue167.py` -> **6** Orphaned Functions | **17** Duplicates
- `sse_starlette-3.3.4/tests/test_sse.py` -> **14** Orphaned Functions | **0** Duplicates
- `sse_starlette-3.3.4/tests/test_multi_loop.py` -> **7** Orphaned Functions | **5** Duplicates
- `sse_starlette-3.3.4/tests/test_issue132.py` -> **9** Orphaned Functions | **2** Duplicates
- `sse_starlette-3.3.4/tests/test_issue152.py` -> **5** Orphaned Functions | **2** Duplicates

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
- **Unknown Dependencies:** `71` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `sse_starlette-3.3.4/tests/test_multi_loop.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 474.1 | **LOC:** 280 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 37.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (59.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 46.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_thread_isolation` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* """Test that shutdown state is isolated between different threads."""
  * `test_handle_exit_wakes_multiple_waiting_tasks` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* """Test that handle_exit() wakes ALL waiting tasks."""
  * `test_all_tasks_share_same_shutdown_state` **(Type Conversions)** (Impact: 5.3)
    * *Intent:* """ Verify that all tasks created with asyncio.create_task() in the same thread share the same _Shut...
  * `test_uvicorn_should_exit_ignored_when_disabled` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* """ Test that uvicorn's should_exit flag is ignored when automatic draining is disabled. The _shutdo...
  * `test_handle_exit_wakes_waiting_task` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* """ Test that handle_exit() wakes a task waiting on _listen_for_exit_signal. The watcher polls shoul...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 55 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 350
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 63`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 41`, `duplicate_logic: 5`, `unreferenced_by_name: 7`
* *Architecture:* `api: 18`, `concurrency: 75`, `import: 6`
* *Defense:* `safety: 30`, `doc: 12`, `test: 18`, `sync_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` asyncio, pytest, sse_starlette.sse, threading, typing, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/sse_starlette/sse.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 387.6 | **LOC:** 438 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **15**; blast radius 213.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `_stream_response` **(Stateful Encapsulated Methods)** (Impact: 10.0)
    * *Intent:* """Send out SSE data to the client as it becomes available in the iterator."""
  * `_ping` **(Stateful Encapsulated Methods)** (Impact: 10.0)
    * *Intent:* """Periodically send ping messages to keep the connection alive on proxies. - frequenccy ca every 15...
  * `_shutdown_watcher` **(Stateful Encapsulated Methods)** (Impact: 8.7)
    * *Intent:* """ Poll for shutdown and broadcast to all events in this context. One watcher runs per thread (even...
  * `__call__` **(Generic / Templated Code)** (Impact: 8.2)
    * *Intent:* """Entrypoint for Starlette's ASGI contract. We spin up tasks: - _stream_response to push events - _...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 101
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 84`, `args: 21`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 57`
* *Architecture:* `api: 12`, `concurrency: 31`, `import: 15`
* *Defense:* `safety: 13`, `doc: 15`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 213.154
  * `Choke Point (Betweenness):` 0.032967 | `Ripple Effect (Closeness):` 0.5
  * `Imports (Out-Degree: 1):` anyio, asyncio, dataclasses, datetime, logging, signal, sse_starlette.event, starlette.background...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `sse_starlette-3.3.4/tests/test_issue167.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 385.9 | **LOC:** 286 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 37.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (71.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (29.5%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_shutdownGracePeriod_whenGeneratorExitsInTime_thenCleanShutdown` **(Defensive Guards)** (Impact: 13.0)
    * *Intent:* """Generator that sees shutdown_event and exits within grace period should complete without Cancelle...
  * `mock_send` **(Defensive Guards)** (Impact: 10.7)
  * `test_shutdownGracePeriod_whenGeneratorIgnoresEvent_thenForceCancelAfterTimeout` **(Defensive Guards)** (Impact: 6.9)
  * `test_shutdownEvent_whenGracePeriodZero_thenEventSetButImmediateCancel` **(Defensive Guards)** (Impact: 5.2)
  * `test_noShutdownEvent_whenShutdownDetected_thenImmediateCancel` **(Defensive Guards)** (Impact: 4.9)
    * *Intent:* """Without shutdown_event, behavior is identical to pre-#167: immediate cancel."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 210
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 109`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 36`, `duplicate_logic: 17`, `unreferenced_by_name: 6`
* *Architecture:* `api: 27`, `concurrency: 60`, `import: 4`
* *Defense:* `safety: 19`, `doc: 8`, `test: 13`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` anyio, pytest, sse_starlette.sse, tests.anyio_compat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/test_sse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 338.44 | **LOC:** 335 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 37.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_response_send_whenValidInput_thenGeneratesExpectedOutput` **(Many-Argument Workhorses)** (Impact: 13.8)
  * `test_eventSourceResponse_whenUsingMemoryChannel_thenHandlesAsyncQueueCorrectly` **(Many-Argument Workhorses)** (Impact: 12.8)
  * `app` **(Many-Argument Workhorses)** (Impact: 11.6)
    * *Intent:* # Arrange # Create bounded memory channel for producer-consumer communication send_chan, recv_chan =...
  * `app` **(Type Conversions)** (Impact: 10.8)
    * *Intent:* # Arrange
  * `stream_numbers` **(Type Conversions)** (Impact: 10.8)
    * *Intent:* # Producer function that writes to the channel
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 106
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 114`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 38`, `unreferenced_by_name: 14`
* *Architecture:* `api: 32`, `concurrency: 41`, `import: 12`
* *Defense:* `safety: 22`, `doc: 1`, `test: 31`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` anyio, anyio.lowlevel, asyncio, functools, logging, math, pytest, sse_starlette.sse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/test_issue152.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 222.78 | **LOC:** 212 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 37.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (69.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_watcher_broadcasts_to_all_events` **(Defensive Guards)** (Impact: 8.7)
    * *Intent:* """Verify that one watcher can signal multiple events. This test also serves as coverage for test_is...
  * `test_single_watcher_per_thread` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* """ Issue #152 regression: Only one watcher should be started per thread. In real ASGI apps: - Each ...
  * `test_event_removal_during_broadcast_is_safe` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* """Removing an event from the set during broadcast doesn't crash. The watcher iterates over list(sta...
  * `test_watcher_cleanup_allows_restart` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* """After watcher exits, a new connection can start a new watcher. The watcher's finally block resets...
  * `test_rapid_ensure_calls_spawn_single_watcher` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* """Multiple rapid calls to _ensure_watcher_started don't spawn multiple watchers."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 125
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 47`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 28`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 9`, `concurrency: 30`, `import: 13`
* *Defense:* `safety: 17`, `doc: 8`, `test: 11`, `sync_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` anyio, asyncio, pytest, sse_starlette.sse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/test_issue132.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 154.92 | **LOC:** 171 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 37.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.5%), Connectivity (formerly Api Exposure) (10.5%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_detects_uvicorn_server_should_exit` **(Defensive Guards)** (Impact: 2.7)
    * *Intent:* """Should detect when uvicorn Server.should_exit is set (Issue #132)."""
  * `test_detects_appstatus_should_exit` **(Defensive Guards)** (Impact: 2.4)
    * *Intent:* """Should detect when AppStatus.should_exit is set (monkey-patch worked)."""
  * `test_fallback_when_no_uvicorn_server` **(Defensive Guards)** (Impact: 2.4)
    * *Intent:* """Should work when _get_uvicorn_server returns None."""
  * `test_returns_server_when_handler_is_bound_method` **(Defensive Guards)** (Impact: 2.0)
    * *Intent:* """Should extract Server from bound method handler."""
  * `test_returns_none_when_self_lacks_should_exit` **(Defensive Guards)** (Impact: 2.0)
    * *Intent:* """Should return None when __self__ doesn't have should_exit attribute."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Concurrency (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 58`, `args: 13`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 14`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 9`, `doc: 12`, `test: 23`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` anyio, pytest, signal, sse_starlette.sse, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/conftest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 89.98 | **LOC:** 114 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 37.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (56.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.1%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reset_shutdown_state` **(Defensive Guards)** (Impact: 4.0)
    * *Intent:* """Reset shutdown state before/after each test. It ensures clean state for tests involving AppStatus...
  * `app` **(Interface Declarations)** (Impact: 3.9)
  * `endless` **(Defensive Guards)** (Impact: 3.6)
  * `event_publisher` **(Defensive Guards)** (Impact: 2.6)
  * `httpx_client` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 46`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `api: 9`, `concurrency: 13`, `import: 14`
* *Defense:* `safety: 4`, `doc: 2`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` asgi_lifespan, asyncio, contextlib, httpx, logging, pytest, sse_starlette, sse_starlette.sse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/sse_starlette/event.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 67.94 | **LOC:** 97 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 266.631; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode` **(Defensive Guards)** (Impact: 14.1)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 9.3)
  * `__init__` **(Generic / Templated Code)** (Impact: 7.7)
  * `ensure_bytes` **(Defensive Guards)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 10`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 266.631
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.385714
  * `Imports (Out-Degree: 0):` io, json, re, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sse_starlette-3.3.4/tests/test_event.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 27.64 | **LOC:** 132 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 37.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (27.6%), Connectivity (formerly Api Exposure) (8.0%), Complexity Load (formerly Cognitive Load) (4.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_server_sent_event` **(Defensive Guards)** (Impact: 5.5)
  * `test_multiline_data` **(Defensive Guards)** (Impact: 2.2)
  * `test_json_server_sent_event` **(Defensive Guards)** (Impact: 1.8)
  * `test_ensure_bytes` **(Defensive Guards)** (Impact: 1.8)
  * `test_custom_sep` **(Defensive Guards)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 19`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 6`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 9`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, sse_starlette.event
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/anyio_compat.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 18.88 | **LOC:** 33 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 69.487; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (72.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (34.1%), Dead Code Surface (formerly Dead Code) (23.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `collapse_excgroups` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.487
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142857
  * `Imports (Out-Degree: 0):` contextlib, exceptiongroup, sys, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sse_starlette-3.3.4/sse_starlette/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 15.08 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 37.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (31.0%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sse_starlette.event, sse_starlette.sse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 8.88 | **LOC:** 444 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 37.561; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ARCHITECTURE.md
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/AUTHORS` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 37.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **Severity: 3.297** (Bridge: 0.033 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **Severity: 47.036** (Embedded: 0.5 * Error Risk: 94.0715%)
- `sse_starlette-3.3.4/sse_starlette/event.py` -> **Severity: 34.214** (Embedded: 0.3857 * Error Risk: 88.7041%)
- `sse_starlette-3.3.4/tests/anyio_compat.py` -> **Severity: 10.281** (Embedded: 0.1429 * Error Risk: 71.9676%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sse_starlette-3.3.4/sse_starlette/event.py` -> **Severity: 26663.1** (Blast Radius: 266.631 * Doc Risk: 100.0%)
- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **Severity: 8526.16** (Blast Radius: 213.154 * Doc Risk: 40.0%)
- `sse_starlette-3.3.4/tests/anyio_compat.py` -> **Severity: 6948.7** (Blast Radius: 69.487 * Doc Risk: 100.0%)
- `sse_starlette-3.3.4/tests/test_event.py` -> **Severity: 3756.1** (Blast Radius: 37.561 * Doc Risk: 100.0%)
- `sse_starlette-3.3.4/tests/test_sse.py` -> **Severity: 3756.1** (Blast Radius: 37.561 * Doc Risk: 100.0%)

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
