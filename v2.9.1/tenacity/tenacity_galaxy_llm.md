# ARCHITECTURAL_BRIEF: tenacity
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
- **Scope:** 66 analyzed artifact(s), 3441 LOC.
- **Load-bearing artifact:** `tenacity-9.1.4/tenacity/wait.py` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tenacity-9.1.4/tenacity/__init__.py` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tenacity-9.1.4/tests/test_tenacity.py` at magnitude 975.04 (structural weight, not risk).
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
| Total Artifacts | 81 |
| Analyzed Artifacts (Scanned) | 66 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 15 |
| Total LOC | 3441 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3715 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.58 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| YAML | 45 | 187 | 68.2% |
| PYTHON | 21 | 3254 | 31.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `3.736`
> **Composition Archetype:** `Small Flat Repo` (z +3.74; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 71%, Generic / Templated Code Files 17%, Large Core Modules (3) 6%, Large Core Modules (2) 3%, Declarative / Non-Code 2%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 66 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 15*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 4x Excluded (Unsupported Extension: '.rst')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.4 | 21.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 67.5 | 9.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 23.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 22 | 6 | 0 | `tenacity-9.1.4/tests/test_tenacity.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 258 | 12 | 8 | `tenacity-9.1.4/tests/test_tenacity.py` |
| danger | 209 | 14 | 9 | `tenacity-9.1.4/tests/test_tenacity.py` |
| concurrency | 150 | 12 | 4 | `tenacity-9.1.4/tests/test_asyncio.py` |
| connectivity | 374 | 18 | 9 | `tenacity-9.1.4/tests/test_tenacity.py` |
| io | 11 | 5 | 0 | `tenacity-9.1.4/doc/source/conf.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 14 | 3 | 0 | `tenacity-9.1.4/tests/test_tenacity.py` |
| serialization | 1 | 1 | 0 | `tenacity-9.1.4/tests/test_tenacity.py` |
| regex | 2 | 2 | 0 | `tenacity-9.1.4/tenacity/retry.py` |
| events | 24 | 4 | 0 | `tenacity-9.1.4/tests/test_tenacity.py` |
| tests | 216 | 6 | 0 | `tenacity-9.1.4/tests/test_tenacity.py` |
| docs | 89 | 13 | 2 | `tenacity-9.1.4/tests/test_tenacity.py` |
| debt | 61 | 6 | 0 | `tenacity-9.1.4/tests/test_tenacity.py` |
| mutation | 980 | 20 | 20 | `tenacity-9.1.4/tests/test_tenacity.py` |
| dead_code | 39 | 6 | 0 | `tenacity-9.1.4/tests/test_asyncio.py` |
| credential | 0 | 0 | 0 | - |
| threat | 76 | 12 | 4 | `tenacity-9.1.4/tenacity/retry.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tenacity-9.1.4/doc/source/conf.py` (Hits: 6)
- `tenacity-9.1.4/tenacity/asyncio/__init__.py` (Hits: 2)
- `tenacity-9.1.4/tenacity/__init__.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **wait.py** (`tenacity-9.1.4/tenacity/wait.py`) — 3 inbound connections
2. **stop.py** (`tenacity-9.1.4/tenacity/stop.py`) — 2 inbound connections
3. **test_tenacity.py** (`tenacity-9.1.4/tests/test_tenacity.py`) — 2 inbound connections
4. **after.py** (`tenacity-9.1.4/tenacity/after.py`) — 1 inbound connections
5. **before.py** (`tenacity-9.1.4/tenacity/before.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`tenacity-9.1.4/tenacity/__init__.py`) — 22 outbound dependencies
2. **test_tenacity.py** (`tenacity-9.1.4/tests/test_tenacity.py`) — 14 outbound dependencies
3. **__init__.py** (`tenacity-9.1.4/tenacity/asyncio/__init__.py`) — 12 outbound dependencies
4. **test_asyncio.py** (`tenacity-9.1.4/tests/test_asyncio.py`) — 9 outbound dependencies
5. **_utils.py** (`tenacity-9.1.4/tenacity/_utils.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Generic / Templated Code)** (@ `tenacity-9.1.4/tenacity/retry.py`) -> Impact: **31.5** | LOC: 30
- `retry` **(Defensive Guards)** (@ `tenacity-9.1.4/tenacity/__init__.py`) -> Impact: **22.5** | LOC: 35
  * *Intent:* """Wrap a function with a new `Retrying` object. :param dargs: positional arguments passed to Retrying object :param dkw: keyword arguments passed to ...
- `before_sleep_log` **(Many-Argument Workhorses)** (@ `tenacity-9.1.4/tenacity/before_sleep.py`) -> Impact: **22.3** | LOC: 43
- `__call__` **(Defensive Guards)** (@ `tenacity-9.1.4/tenacity/asyncio/__init__.py`) -> Impact: **19.1** | LOC: 24
- `__call__` **(Defensive Guards)** (@ `tenacity-9.1.4/tenacity/__init__.py`) -> Impact: **14.6** | LOC: 23
- `__call__` **(Defensive Guards)** (@ `tenacity-9.1.4/tenacity/tornadoweb.py`) -> Impact: **14.6** | LOC: 23
- `log_it` **(Compute Cores)** (@ `tenacity-9.1.4/tenacity/before_sleep.py`) -> Impact: **14.4** | LOC: 33
- `wrap` **(Defensive Guards)** (@ `tenacity-9.1.4/tenacity/__init__.py`) -> Impact: **13.8** | LOC: 22
- `make_retry_state` **(Many-Argument Workhorses)** (@ `tenacity-9.1.4/tests/test_tenacity.py`) -> Impact: **12.7** | LOC: 31
- `test_wait_chain` **(Compute Cores)** (@ `tenacity-9.1.4/tests/test_tenacity.py`) -> Impact: **12.2** | LOC: 17

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tenacity-9.1.4/tests` | 7 | 1778.54 | 19.48% | 0.0% |
| `tenacity-9.1.4/tenacity` | 10 | 1001.06 | 38.36% | 29.98% |
| `tenacity-9.1.4/releasenotes/notes` | 44 | 536.2 | 1.66% | 0.41% |
| `tenacity-9.1.4/tenacity/asyncio` | 2 | 330.82 | 75.0% | 49.57% |
| `tenacity-9.1.4` | 2 | 24.16 | 0.0% | 0.0% |
| `tenacity-9.1.4/doc/source` | 1 | 22.26 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tenacity-9.1.4/tenacity/stop.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tenacity/retry.py` -> **99.9934%** Exposure
- `tenacity-9.1.4/tenacity/_utils.py` -> **99.7748%** Exposure
- `tenacity-9.1.4/tenacity/asyncio/retry.py` -> **99.131%** Exposure
- `tenacity-9.1.4/releasenotes/notes/wait_exponential_jitter-6ffc81dddcbaa6d3.yaml` -> **18.2426%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `tenacity-9.1.4/tenacity/before_sleep.py` -> **99.9994%** Exposure
- `tenacity-9.1.4/tenacity/asyncio/__init__.py` -> **99.9979%** Exposure
- `tenacity-9.1.4/tenacity/wait.py` -> **99.9886%** Exposure
- `tenacity-9.1.4/tenacity/__init__.py` -> **99.9792%** Exposure
- `tenacity-9.1.4/tenacity/asyncio/retry.py` -> **99.9704%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tenacity-9.1.4/tests/test_asyncio.py` -> **23** Orphaned Functions | **10** Duplicates
- `tenacity-9.1.4/tests/test_tenacity.py` -> **0** Orphaned Functions | **26** Duplicates
- `tenacity-9.1.4/tenacity/retry.py` -> **0** Orphaned Functions | **8** Duplicates
- `tenacity-9.1.4/tenacity/_utils.py` -> **5** Orphaned Functions | **0** Duplicates
- `tenacity-9.1.4/tests/test_tornado.py` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `97` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tenacity-9.1.4/tests/test_tenacity.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 975.04 | **LOC:** 1807 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 32.781; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (63.4%), Guard Balance (formerly Safety Score) (61.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (20.3%)
- **Documentation Coverage:** 92.7114% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_retry_state` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `test_wait_chain` **(Compute Cores)** (Impact: 12.2)
  * `_make_unset_exception` **(Stateful Encapsulated Methods)** (Impact: 7.3)
  * `test_wait_random_exponential` **(I/O & Config Routines)** (Impact: 7.1)
  * `test_random_sleep` **(Type Conversions)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 310
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 399`, `args: 221`, `func_start: 203`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 204`, `duplicate_logic: 26`
* *Architecture:* `api: 166`, `import: 20`
* *Defense:* `safety: 76`, `doc: 24`, `test: 133`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.781
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030769
  * `Imports (Out-Degree: 0):` contextlib, copy, datetime, fractions, logging, pickle, pytest, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tests/test_asyncio.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 601.2 | **LOC:** 493 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 14.409; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.0%), Complexity Load (formerly Cognitive Load) (47.2%)
- **Documentation Coverage:** 96.0784% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_retry_with_async_result_or` **(Defensive Guards)** (Impact: 7.1)
  * `test_retry_with_async_result_ror` **(Defensive Guards)** (Impact: 7.1)
  * `test_retry_with_async_exc` **(Defensive Guards)** (Impact: 7.0)
  * `test_retry_function_attributes` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* """Test that the wrapped function attributes are exposed as intended. - statistics contains the valu...
  * `test_retry_with_async_result` **(Defensive Guards)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 319
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 170`, `args: 53`, `func_start: 52`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 44`, `duplicate_logic: 10`, `unreferenced_by_name: 23`
* *Architecture:* `api: 58`, `concurrency: 79`, `import: 13`
* *Defense:* `safety: 36`, `doc: 2`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .test_tenacity, asyncio, functools, inspect, pytest, tenacity, tenacity.wait, trio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 434.46 | **LOC:** 751 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 14.409; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.5%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `retry` **(Defensive Guards)** (Impact: 22.5)
    * *Intent:* """Wrap a function with a new `Retrying` object. :param dargs: positional arguments passed to Retryi...
  * `__call__` **(Defensive Guards)** (Impact: 14.6)
  * `wrap` **(Defensive Guards)** (Impact: 13.8)
  * `_post_stop_check_actions` **(Stateful Encapsulated Methods)** (Impact: 10.1)
  * `__exit__` **(Generic / Templated Code)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 210`, `args: 54`, `func_start: 51`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 87`
* *Architecture:* `io: 1`, `api: 39`, `concurrency: 4`, `import: 59`
* *Defense:* `safety: 12`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` , .after, .before, .before_sleep, .nap, .retry, .stop, .wait...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/asyncio/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 223.4 | **LOC:** 211 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 14.409; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Defensive Guards)** (Impact: 19.1)
  * `__anext__` **(Defensive Guards)** (Impact: 9.1)
  * `_run_wait` **(Stateful Encapsulated Methods)** (Impact: 5.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 5.2)
  * `_portable_async_sleep` **(Stateful Encapsulated Methods)** (Impact: 5.0)
    * *Intent:* # If trio is already imported, then importing it is cheap. # If trio isn't already imported, then it...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 94
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 75`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 25`
* *Architecture:* `io: 2`, `api: 14`, `concurrency: 19`, `import: 24`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..retry, .retry, asyncio, functools, overhead, sniffio, sys, tenacity...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/retry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 189.38 | **LOC:** 283 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 14.409; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Generic / Templated Code)** (Impact: 31.5)
  * `__call__` **(Defensive Guards)** (Impact: 9.3)
  * `__call__` **(Generic / Templated Code)** (Impact: 9.2)
  * `__call__` **(Generic / Templated Code)** (Impact: 7.5)
  * `__call__` **(Generic / Templated Code)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 70`, `args: 32`, `func_start: 28`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `duplicate_logic: 8`
* *Architecture:* `api: 16`, `import: 4`
* *Defense:* `safety: 4`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` abc, re, tenacity, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/asyncio/retry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 107.42 | **LOC:** 126 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 14.409; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.1%), Guard Balance (formerly Safety Score) (86.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Generic / Templated Code)** (Impact: 9.2)
  * `__call__` **(Generic / Templated Code)** (Impact: 7.3)
  * `__call__` **(Generic / Templated Code)** (Impact: 7.3)
  * `__call__` **(Generic / Templated Code)** (Impact: 7.3)
  * `__and__` **(Generic / Templated Code)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 43`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `concurrency: 9`, `import: 5`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` abc, tenacity, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tests/test_issue_478.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 107.34 | **LOC:** 118 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 14.409; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_issue` **(Defensive Guards)** (Impact: 10.8)
  * `test_async` **(Defensive Guards)** (Impact: 10.8)
  * `do_retry` **(Defensive Guards)** (Impact: 6.5)
  * `do_retry` **(Defensive Guards)** (Impact: 6.5)
  * `_do_work` **(Encapsulated Accessors)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 44`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 11`, `unreferenced_by_name: 2`
* *Architecture:* `api: 11`, `concurrency: 11`, `import: 5`
* *Defense:* `safety: 10`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` asyncio, functools, tenacity, typing, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/wait.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 97.0 | **LOC:** 274 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 28.407; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.0%), Connectivity (formerly Api Exposure) (58.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Generic / Templated Code)** (Impact: 5.6)
  * `__radd__` **(Generic / Templated Code)** (Impact: 3.7)
    * *Intent:* # make it possible to use multiple waits with the built-in sum function if other == 0: # type: ignor...
  * `__call__` **(Generic / Templated Code)** (Impact: 3.6)
  * `__init__` **(Generic / Templated Code)** (Impact: 3.0)
  * `__init__` **(Generic / Templated Code)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 53`, `args: 21`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 4`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.407
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046154
  * `Imports (Out-Degree: 0):` abc, random, tenacity, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tenacity/_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 65.78 | **LOC:** 114 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 14.409; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (95.4%), Complexity Load (formerly Cognitive Load) (58.6%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_ordinal` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* # See: https://en.wikipedia.org/wiki/English_numerals#Ordinal_numbers if pos_num == 0: return "th" e...
  * `is_coroutine_callable` **(Defensive Guards)** (Impact: 7.5)
  * `get_callback_name` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* """Get a callback fully-qualified name. If no name can be produced ``repr(cb)`` is called and return...
  * `to_seconds` **(Defensive Guards)** (Impact: 4.4)
  * `wrap_to_async_func` **(Generic / Templated Code)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 33`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 8`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 8`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, functools, inspect, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/stop.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 63.42 | **LOC:** 131 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 22.283; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.1%), Concurrency Surface (formerly Concurrency) (96.9%), Guard Balance (formerly Safety Score) (77.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Generic / Templated Code)** (Impact: 3.8)
  * `__call__` **(Generic / Templated Code)** (Impact: 3.7)
  * `__call__` **(Generic / Templated Code)** (Impact: 3.6)
  * `__call__` **(Generic / Templated Code)** (Impact: 3.6)
  * `__call__` **(Generic / Templated Code)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 41`, `args: 16`, `func_start: 16`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `duplicate_logic: 4`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 5`
* *Defense:* `doc: 8`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.283
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030769
  * `Imports (Out-Degree: 0):` abc, tenacity, threading, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tenacity/before_sleep.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 59.96 | **LOC:** 72 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 16.159; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (38.7%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `before_sleep_log` **(Many-Argument Workhorses)** (Impact: 22.3)
  * `log_it` **(Compute Cores)** (Impact: 14.4)
  * `before_sleep_nothing` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """Before sleep strategy that does nothing."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.159
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015385
  * `Imports (Out-Degree: 0):` tenacity, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tests/test_after.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 38.14 | **LOC:** 76 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 14.409; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (15.6%), Connectivity (formerly Api Exposure) (7.4%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_01_default` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* """Test log formatting."""
  * `test_02_custom_sec_format` **(I/O & Config Routines)** (Impact: 5.4)
    * *Intent:* """Test log formatting with custom int format.."""
  * `setUp` **(Generic / Templated Code)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `doc: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , logging, random, tenacity, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/tornadoweb.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 33.82 | **LOC:** 64 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 16.159; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Defensive Guards)** (Impact: 14.6)
  * `__init__` **(Generic / Templated Code)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 17`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 5`
* *Architecture:* `io: 1`, `api: 3`, `import: 8`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.159
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015385
  * `Imports (Out-Degree: 0):` sys, tenacity, tornado, tornado.concurrent, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tests/test_tornado.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 24.68 | **LOC:** 78 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 14.409; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (31.6%), Connectivity (formerly Api Exposure) (6.7%), Complexity Load (formerly Cognitive Load) (6.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_old_tornado` **(Annotated & Test Methods)** (Impact: 2.1)
  * `test_stop_after_attempt` **(Defensive Guards)** (Impact: 1.8)
  * `test_retry` **(Defensive Guards)** (Impact: 1.7)
  * `_retryable_coroutine` **(Encapsulated Accessors)** (Impact: 1.6)
  * `_retryable_coroutine_with_2_attempts` **(Encapsulated Accessors)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 25`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 8`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .test_tenacity, tenacity, tornado, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/after.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 22.74 | **LOC:** 50 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 16.159; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (69.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (40.1%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `after_log` **(Generic / Templated Code)** (Impact: 7.0)
  * `log_it` **(Generic / Templated Code)** (Impact: 4.8)
  * `after_nothing` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """After call strategy that does nothing."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.159
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015385
  * `Imports (Out-Degree: 0):` tenacity, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/doc/source/conf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 22.26 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 14.409; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (72.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `io: 6`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/before.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 21.78 | **LOC:** 47 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 16.159; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (69.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (40.1%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `before_log` **(Generic / Templated Code)** (Impact: 6.1)
  * `log_it` **(Generic / Templated Code)** (Impact: 4.8)
  * `before_nothing` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """Before call strategy that does nothing."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.159
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015385
  * `Imports (Out-Degree: 0):` tenacity, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tests/test_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 21.62 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 14.409; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.6%), Connectivity (formerly Api Exposure) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_is_coroutine_callable` **(Defensive Guards)** (Impact: 2.8)
  * `__call__` **(Generic / Templated Code)** (Impact: 1.5)
  * `__call__` **(Generic / Templated Code)** (Impact: 1.5)
  * `async_func` **(Generic / Templated Code)** (Impact: 1.1)
  * `sync_func` **(Generic / Templated Code)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `args: 6`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` functools, tenacity
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/fix-async-retry-type-overloads-27f3e0c239ed6b.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/add-stop-before-delay-a775f88ac872c923.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 13.64 | **LOC:** 7 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/async-sleep-retrying-32de5866f5d041.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 13.64 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/no-async-iter-6132a42e52348a75.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 13.64 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 13.12 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 14.409; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/fix-retry-wrapper-attributes-f7a3a45b8e90f257.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 13.12 | **LOC:** 7 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/trio-support-retry-22bd544800cd1f36.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 13.12 | **LOC:** 7 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.409
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

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tenacity-9.1.4/tenacity/wait.py` -> **Severity: 3.646** (Embedded: 0.0462 * Error Risk: 78.992%)
- `tenacity-9.1.4/tenacity/stop.py` -> **Severity: 2.373** (Embedded: 0.0308 * Error Risk: 77.1322%)
- `tenacity-9.1.4/tests/test_tenacity.py` -> **Severity: 1.895** (Embedded: 0.0308 * Error Risk: 61.5915%)
- `tenacity-9.1.4/tenacity/tornadoweb.py` -> **Severity: 1.466** (Embedded: 0.0154 * Error Risk: 95.2574%)
- `tenacity-9.1.4/tenacity/before_sleep.py` -> **Severity: 1.33** (Embedded: 0.0154 * Error Risk: 86.4295%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tenacity-9.1.4/tests/test_tenacity.py` -> **Severity: 3039.172** (Blast Radius: 32.781 * Doc Risk: 92.7114%)
- `tenacity-9.1.4/tenacity/wait.py` -> **Severity: 2840.7** (Blast Radius: 28.407 * Doc Risk: 100.0%)
- `tenacity-9.1.4/tenacity/stop.py` -> **Severity: 2228.3** (Blast Radius: 22.283 * Doc Risk: 100.0%)
- `tenacity-9.1.4/tenacity/tornadoweb.py` -> **Severity: 1615.9** (Blast Radius: 16.159 * Doc Risk: 100.0%)
- `tenacity-9.1.4/tenacity/asyncio/__init__.py` -> **Severity: 1440.9** (Blast Radius: 14.409 * Doc Risk: 100.0%)

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
