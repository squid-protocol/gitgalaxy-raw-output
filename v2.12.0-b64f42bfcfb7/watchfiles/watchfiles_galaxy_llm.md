# ARCHITECTURAL_BRIEF: watchfiles
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 34 analyzed artifact(s), 2382 LOC.
- **Load-bearing artifact:** `watchfiles-1.1.1/watchfiles/__init__.py` -- 8 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `watchfiles-1.1.1/src/lib.rs` -- pulls in 28 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `watchfiles-1.1.1/watchfiles/run.py` at magnitude 297.14 (structural weight, not risk).
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
| Total Artifacts | 42 |
| Analyzed Artifacts (Scanned) | 34 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 2382 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2646 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2028 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6479 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 17 | 1985 | 50.0% |
| PLAINTEXT | 13 | 0 | 38.2% |
| MARKDOWN | 2 | 0 | 5.9% |
| MAKEFILE | 1 | 63 | 2.9% |
| RUST | 1 | 334 | 2.9% |

## 4.1 SOURCE ENCODINGS
All 34 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 53%, Large Core Modules (2) 18%, Generic / Templated Code Files 6%, Large Core Modules (3) 6%, Parameter Forwarders Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19 | 55.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 44.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 69.9 | 25.5 | 26.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 68.8 | 44.8 | 51.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 21.4 | 1.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 80.6 | 22.4 | 11.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 27.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 66.1 | 80.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 95 | 10 | 8 | `watchfiles-1.1.1/tests/test_rust_notify.py` |
| cleanup | 19 | 5 | 1 | `watchfiles-1.1.1/Makefile` |
| guards | 220 | 13 | 22 | `watchfiles-1.1.1/tests/test_run_process.py` |
| danger | 93 | 11 | 9 | `watchfiles-1.1.1/watchfiles/run.py` |
| concurrency | 99 | 7 | 15 | `watchfiles-1.1.1/tests/test_watch.py` |
| connectivity | 210 | 16 | 21 | `watchfiles-1.1.1/tests/test_run_process.py` |
| io | 129 | 12 | 8 | `watchfiles-1.1.1/tests/test_cli.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 2 | 0 | `watchfiles-1.1.1/watchfiles/run.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 3 | 3 | 0 | `watchfiles-1.1.1/tests/test_filters.py` |
| events | 35 | 4 | 3 | `watchfiles-1.1.1/watchfiles/run.py` |
| tests | 258 | 9 | 33 | `watchfiles-1.1.1/tests/test_cli.py` |
| docs | 45 | 9 | 6 | `watchfiles-1.1.1/watchfiles/filters.py` |
| debt | 14 | 5 | 1 | `watchfiles-1.1.1/src/lib.rs` |
| mutation | 888 | 16 | 89 | `watchfiles-1.1.1/tests/test_cli.py` |
| dead_code | 111 | 8 | 17 | `watchfiles-1.1.1/tests/test_rust_notify.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `watchfiles-1.1.1/tests/test_cli.py` (Hits: 55)
- `watchfiles-1.1.1/tests/test_run_process.py` (Hits: 28)
- `watchfiles-1.1.1/tests/test_docs.py` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`watchfiles-1.1.1/watchfiles/__init__.py`) — 8 inbound connections
2. **main.py** (`watchfiles-1.1.1/watchfiles/main.py`) — 8 inbound connections
3. **filters.py** (`watchfiles-1.1.1/watchfiles/filters.py`) — 5 inbound connections
4. **run.py** (`watchfiles-1.1.1/watchfiles/run.py`) — 3 inbound connections
5. **cli.py** (`watchfiles-1.1.1/watchfiles/cli.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`watchfiles-1.1.1/src/lib.rs`) — 28 outbound dependencies
2. **run.py** (`watchfiles-1.1.1/watchfiles/run.py`) — 20 outbound dependencies
3. **cli.py** (`watchfiles-1.1.1/watchfiles/cli.py`) — 13 outbound dependencies
4. **main.py** (`watchfiles-1.1.1/watchfiles/main.py`) — 13 outbound dependencies
5. **test_docs.py** (`watchfiles-1.1.1/tests/test_docs.py`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `py_new` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/src/lib.rs`) -> Impact: **76.4** | LOC: 153
- `awatch` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/main.py`) -> Impact: **70.4** | LOC: 136
- `watch` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/src/lib.rs`) -> Impact: **70.1** | LOC: 80
- `watch` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/main.py`) -> Impact: **53.6** | LOC: 99
- `cli` **(Compute Cores)** (@ `watchfiles-1.1.1/watchfiles/cli.py`) -> Impact: **39.0** | LOC: 157
  * *Intent:* """ Watch one or more directories and execute either a shell command or a python function on file changes. Example of watching the current directory a...
- `run_process` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **34.3** | LOC: 126
- `arun_process` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **33.8** | LOC: 78
- `start_process` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **33.5** | LOC: 34
- `build_filter` **(Defensive Guards)** (@ `watchfiles-1.1.1/watchfiles/cli.py`) -> Impact: **23.9** | LOC: 28
- `__call__` **(Compute Cores)** (@ `watchfiles-1.1.1/watchfiles/filters.py`) -> Impact: **17.1** | LOC: 21
  * *Intent:* """ Instances of `BaseFilter` subclasses can be used as callables. Args: change: The type of change that occurred, see [`Change`][watchfiles.Change]. ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `watchfiles-1.1.1/tests` | 9 | 1085.3 | 25.13% | 0.0% |
| `watchfiles-1.1.1/watchfiles` | 8 | 870.82 | 27.05% | 0.0% |
| `watchfiles-1.1.1/src` | 1 | 218.38 | 39.71% | 21.38% |
| `watchfiles-1.1.1` | 2 | 40.64 | 1.03% | 0.0% |
| `watchfiles-1.1.1/tests/test_files/dir_a` | 8 | 8.0 | 0.0% | 0.0% |
| `watchfiles-1.1.1/tests/test_files` | 6 | 6.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `watchfiles-1.1.1/src/lib.rs` -> **21.3762%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **100.0%** Exposure
- `watchfiles-1.1.1/watchfiles/main.py` -> **100.0%** Exposure
- `watchfiles-1.1.1/watchfiles/run.py` -> **99.9981%** Exposure
- `watchfiles-1.1.1/watchfiles/cli.py` -> **99.9894%** Exposure
- `watchfiles-1.1.1/src/lib.rs` -> **91.1375%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `watchfiles-1.1.1/tests/test_rust_notify.py` -> **29** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_run_process.py` -> **21** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_watch.py` -> **21** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_cli.py` -> **17** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_filters.py` -> **10** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `144` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `watchfiles-1.1.1/watchfiles/run.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.378)
- **Top Global Matches:** file_cluster_5: 7.378, file_cluster_12: 10.85, file_cluster_7: 10.88
- **Magnitude:** 297.14 | **LOC:** 439 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **20**; blast radius 55.654; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.9%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_process` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `arun_process` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `start_process` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `stop` **(Defensive Guards)** (Impact: 11.2)
  * `detect_target_type` **(Defensive Guards)** (Impact: 8.6)
    * *Intent:* """ Used by [`run_process`][watchfiles.run_process], [`arun_process`][watchfiles.arun_process] and i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 84`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 3`, `state_mutation: 29`
* *Architecture:* `io: 8`, `api: 19`, `concurrency: 10`, `import: 21`
* *Defense:* `safety: 21`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 55.654
  * `Choke Point (Betweenness):` 0.001263 | `Ripple Effect (Closeness):` 0.204848
  * `Imports (Out-Degree: 2):` .filters, .main, anyio, contextlib, importlib, inspect, json, logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/main.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.509)
- **Top Global Matches:** file_cluster_4: 9.509, file_cluster_0: 11.694, file_cluster_16: 12.769
- **Magnitude:** 289.28 | **LOC:** 374 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **13**; blast radius 238.507; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.6%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `awatch` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `watch` **(Many-Argument Workhorses)** (Impact: 53.6)
  * `_prep_changes` **(Stateful Encapsulated Methods)** (Impact: 9.1)
  * `_log_changes` **(Stateful Encapsulated Methods)** (Impact: 8.9)
  * `_calc_async_timeout` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* """ see https://github.com/samuelcolvin/watchfiles/issues/110 """
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 59`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `io: 6`, `api: 7`, `concurrency: 6`, `import: 14`
* *Defense:* `safety: 1`, `doc: 11`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 238.507
  * `Choke Point (Betweenness):` 0.009785 | `Ripple Effect (Closeness):` 0.256061
  * `Imports (Out-Degree: 2):` ._rust_notify, .filters, anyio, asyncio, enum, logging, os, pathlib...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/test_watch.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.407)
- **Top Global Matches:** file_cluster_12: 7.407, file_cluster_7: 8.414, file_cluster_5: 9.753
- **Magnitude:** 268.06 | **LOC:** 241 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 9.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (48.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_awatch_interrupt_warning` **(Defensive Guards)** (Impact: 5.6)
  * `test_awatch_unexpected_signal` **(Defensive Guards)** (Impact: 4.7)
  * `test_awatch_no_yield` **(Defensive Guards)** (Impact: 4.2)
  * `test_watch_timeout` **(Defensive Guards)** (Impact: 4.2)
  * `test_awatch_timeout` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 92`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 27`, `unreferenced_by_name: 21`
* *Architecture:* `io: 3`, `api: 22`, `concurrency: 20`, `import: 12`
* *Defense:* `safety: 37`, `test: 27`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` anyio, conftest, contextlib, exceptiongroup, pathlib, pytest, sys, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.118)
- **Top Global Matches:** file_cluster_6: 10.118, file_cluster_8: 12.405, file_cluster_4: 16.574
- **Magnitude:** 218.38 | **LOC:** 383 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 9.215; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `py_new` **(Many-Argument Workhorses)** (Impact: 76.4)
  * `watch` **(Many-Argument Workhorses)** (Impact: 70.1)
  * `_rust_notify` **(Generic / Templated Code)** (Impact: 7.8)
  * `map_watch_error` **(Compute Cores)** (Impact: 6.6)
  * `__exit__` **(Generic / Templated Code)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 79`, `args: 15`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 15`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 7`, `doc: 1`, `sync_locks: 16`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` notify, notify::Config, notify::ErrorKind, notify::PollWatcher, notify::RecommendedWatcher, notify::RecursiveMode, notify::Result, notify::Watcher...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_rust_notify.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.777)
- **Top Global Matches:** file_cluster_13: 7.777, file_cluster_11: 7.914, file_cluster_15: 8.086
- **Magnitude:** 195.7 | **LOC:** 343 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 9.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.6%), Complexity Load (formerly Cognitive Load) (26.8%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_move_internal` **(Type Conversions)** (Impact: 5.3)
    * *Intent:* # can't use tmp_path as it causes problems on Windows (different drive), and macOS (delayed events) ...
  * `test_default_ignore_permission_denied` **(Defensive Guards)** (Impact: 4.7)
  * `test_does_not_exist_message` **(Type Conversions)** (Impact: 4.4)
  * `test_does_not_exist_polling` **(Type Conversions)** (Impact: 4.4)
  * `test_wrong_type_event_is_set` **(Type Conversions)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 86`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 53`, `unreferenced_by_name: 29`
* *Architecture:* `io: 5`, `api: 30`, `import: 9`
* *Defense:* `safety: 28`, `test: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .conftest, os, pathlib, pytest, re, sys, typing, watchfiles._rust_notify...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_run_process.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.467)
- **Top Global Matches:** file_cluster_12: 7.467, file_cluster_7: 8.504, file_cluster_5: 9.664
- **Magnitude:** 193.6 | **LOC:** 280 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 9.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (48.4%), Guard Balance (formerly Safety Score) (30.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_alive_terminates` **(Defensive Guards)** (Impact: 6.7)
  * `test_function_string_not_win` **(Defensive Guards)** (Impact: 6.7)
  * `test_command_with_args` **(Defensive Guards)** (Impact: 6.7)
  * `poll` **(Compute Cores)** (Impact: 4.3)
  * `join` **(Parameter Forwarders)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 121`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 3`, `state_mutation: 39`, `unreferenced_by_name: 21`
* *Architecture:* `io: 28`, `api: 30`, `concurrency: 8`, `import: 12`
* *Defense:* `safety: 54`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` conftest, dirty_equals, multiprocessing.context, os, pathlib, pytest, subprocess, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/cli.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.374)
- **Top Global Matches:** file_cluster_8: 10.374, file_cluster_6: 11.769, file_cluster_4: 19.285
- **Magnitude:** 132.44 | **LOC:** 225 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 28.799; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.5%), Complexity Load (formerly Cognitive Load) (51.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cli` **(Compute Cores)** (Impact: 39.0)
    * *Intent:* """ Watch one or more directories and execute either a shell command or a python function on file ch...
  * `build_filter` **(Defensive Guards)** (Impact: 23.9)
  * `resolve_path` **(Generic / Templated Code)** (Impact: 4.5)
  * `import_exit` **(Defensive Guards)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 53`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 18`
* *Architecture:* `io: 6`, `api: 4`, `import: 12`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.799
  * `Choke Point (Betweenness):` 0.01089 | `Ripple Effect (Closeness):` 0.090909
  * `Imports (Out-Degree: 4):` .Change, .filters, .run, .version, argparse, logging, of, os...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/conftest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.86)
- **Top Global Matches:** file_cluster_12: 6.86, file_cluster_5: 8.265, file_cluster_7: 8.722
- **Magnitude:** 128.66 | **LOC:** 205 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 14.438; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.6%), Guard Balance (formerly Safety Score) (58.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (33.7%)
- **Documentation Coverage:** 91.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__exit__` **(Compute Cores)** (Impact: 8.6)
  * `watch` **(Defensive Guards)** (Impact: 5.3)
  * `test_dir` **(I/O & Config Routines)** (Impact: 4.5)
  * `clear` **(Parameter Forwarders)** (Impact: 3.0)
  * `write_soon` **(Interface Declarations)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 56`, `args: 26`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 31`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 21`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 2`, `doc: 3`, `test: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.438
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060606
  * `Imports (Out-Degree: 0):` logging, os, pathlib, pytest, sys, threading, time, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/test_docs.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.021)
- **Top Global Matches:** file_cluster_12: 7.021, file_cluster_15: 9.329, file_cluster_7: 9.964
- **Magnitude:** 110.78 | **LOC:** 123 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 9.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (93.7%), Guard Balance (formerly Safety Score) (61.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (36.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_code_chunks` **(Compute Cores)** (Impact: 9.1)
  * `extract_code_chunks` **(Compute Cores)** (Impact: 8.7)
  * `_import_execute` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `import_execute` **(Stateful Encapsulated Methods)** (Impact: 6.4)
  * `test_docs_examples` **(Many-Argument Workhorses)** (Impact: 5.9)
    * *Intent:* # with pypy we sometimes (???) get a "The loop argument is deprecated since Python 3.8" warning, see...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 37`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `unreferenced_by_name: 2`
* *Architecture:* `io: 9`, `api: 6`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 7`, `doc: 1`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _pytest.assertion.rewrite, collections, conftest, importlib.util, pathlib, pytest, re, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.701)
- **Top Global Matches:** file_cluster_15: 7.701, file_cluster_2: 8.25, file_cluster_11: 8.538
- **Magnitude:** 84.16 | **LOC:** 332 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 9.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.4%), Connectivity (formerly Api Exposure) (10.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_args` **(Defensive Guards)** (Impact: 3.3)
  * `test_ignore_paths` **(I/O & Config Routines)** (Impact: 3.1)
  * `test_filter_all` **(Defensive Guards)** (Impact: 3.0)
  * `test_args_command` **(Type Conversions)** (Impact: 3.0)
  * `test_function` **(Type Conversions)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 51`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 16`, `unreferenced_by_name: 17`
* *Architecture:* `io: 55`, `api: 18`, `import: 7`
* *Defense:* `safety: 15`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dirty_equals, os, pathlib, pytest, sys, watchfiles, watchfiles.cli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/filters.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.587)
- **Top Global Matches:** file_cluster_0: 6.587, file_cluster_16: 9.322, file_cluster_15: 9.699
- **Magnitude:** 83.6 | **LOC:** 150 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 180.674; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.3%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* """ Instances of `BaseFilter` subclasses can be used as callables. Args: change: The type of change ...
  * `__init__` **(Generic / Templated Code)** (Impact: 10.0)
  * `__call__` **(Generic / Templated Code)** (Impact: 4.1)
  * `__init__` **(Encapsulated Accessors)** (Impact: 3.0)
  * `__repr__` **(Generic / Templated Code)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `io: 3`, `api: 5`, `import: 6`
* *Defense:* `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 180.674
  * `Choke Point (Betweenness):` 0.000947 | `Ripple Effect (Closeness):` 0.243867
  * `Imports (Out-Degree: 1):` .main, logging, os, pathlib, re, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/test_force_polling.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.801)
- **Top Global Matches:** file_cluster_7: 6.801, file_cluster_12: 6.808, file_cluster_5: 8.889
- **Magnitude:** 53.2 | **LOC:** 105 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 9.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (17.1%), Connectivity (formerly Api Exposure) (8.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_default_force_polling_wsl` **(Defensive Guards)** (Impact: 5.6)
  * `test_default_force_polling` **(Defensive Guards)** (Impact: 5.2)
  * `test_watch_polling_env` **(Parameter Forwarders)** (Impact: 3.9)
  * `test_watch_polling_env_with_custom_delay` **(Parameter Forwarders)** (Impact: 3.9)
  * `test_watch_polling_not_env` **(Parameter Forwarders)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 32`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 3`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .conftest, __future__, pytest, typing, watchfiles, watchfiles.main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_filters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.754)
- **Top Global Matches:** file_cluster_0: 7.754, file_cluster_13: 8.671, file_cluster_15: 9.019
- **Magnitude:** 40.62 | **LOC:** 101 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 9.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (29.2%), Complexity Load (formerly Cognitive Load) (13.9%), Connectivity (formerly Api Exposure) (10.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Generic / Templated Code)** (Impact: 4.1)
  * `test_web_filter` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* # test case from docs class WebFilter(DefaultFilter): allowed_extensions = '.html', '.css', '.js' de...
  * `test_default_filter` **(Type Conversions)** (Impact: 1.9)
  * `test_simple_function` **(Generic / Templated Code)** (Impact: 1.8)
  * `only_added` **(Generic / Templated Code)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 44`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 11`, `import: 8`
* *Defense:* `safety: 16`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` conftest, dirty_equals, pathlib, pytest, re, sys, typing, watchfiles
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.955)
- **Top Global Matches:** file_cluster_2: 5.955, file_cluster_15: 7.672, file_cluster_17: 7.709
- **Magnitude:** 38.46 | **LOC:** 78 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (13.5%), Test Surface (formerly Verification) (2.4%), Complexity Load (formerly Cognitive Load) (2.1%)
- **Documentation Coverage:** 35.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `.uv` **(I/O & Config Routines)** (Impact: 2.2)
  * `.pre-commit` **(I/O & Config Routines)** (Impact: 2.2)
  * `clean` **(I/O & Config Routines)** (Impact: 1.5)
  * `lint-rust` **(I/O & Config Routines)** (Impact: 1.4)
  * `format` **(I/O & Config Routines)** (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `func_start: 14`
* *Risk/State:* None
* *Architecture:* `api: 18`
* *Defense:* `doc: 3`, `test: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.019)
- **Top Global Matches:** file_cluster_5: 7.019, file_cluster_7: 10.369, file_cluster_12: 11.44
- **Magnitude:** 23.92 | **LOC:** 112 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 11.827; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (64.8%), Guard Balance (formerly Safety Score) (53.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Generic / Templated Code)** (Impact: 3.3)
  * `watch` **(Generic / Templated Code)** (Impact: 2.8)
  * `__exit__` **(Generic / Templated Code)** (Impact: 1.8)
    * *Intent:* """ Calls [`close`][watchfiles._rust_notify.RustNotify.close]. """
  * `is_set` **(Generic / Templated Code)** (Impact: 1.5)
  * `__enter__` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """ Does nothing, but allows `RustNotify` to be used as a context manager. !!! note The watching the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/__init__.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.531)
- **Top Global Matches:** file_cluster_2: 4.531, file_cluster_17: 5.268, file_cluster_13: 5.829
- **Magnitude:** 18.32 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **4**; blast radius 177.457; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (31.0%), Connectivity (formerly Api Exposure) (23.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 177.457
  * `Choke Point (Betweenness):` 0.020676 | `Ripple Effect (Closeness):` 0.284512
  * `Imports (Out-Degree: 4):` .filters, .main, .run, .version
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/version.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.988)
- **Top Global Matches:** file_cluster_2: 3.988, file_cluster_17: 5.168, file_cluster_13: 5.621
- **Magnitude:** 14.56 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 53.043; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (31.0%), Connectivity (formerly Api Exposure) (21.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 53.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.189675
  * `Imports (Out-Degree: 1):` ._rust_notify
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/__main__.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.058)
- **Top Global Matches:** file_cluster_2: 4.058, file_cluster_17: 5.194, file_cluster_13: 5.832
- **Magnitude:** 11.56 | **LOC:** 5 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .cli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 2.18 | **LOC:** 109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/a.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/a_non_recursive.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/b.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/c.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `watchfiles-1.1.1/tests/test_rust_notify.py` (PYTHON) | Magnitude: 195.7 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 178, structural_boundaries: 86, core_var_decl: 57, design_snake_case: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `watchfiles-1.1.1/tests/test_force_polling.py` (PYTHON) | Magnitude: 53.2 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 32, test: 13, args: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `watchfiles-1.1.1/watchfiles/cli.py` -> **Severity: 1.089** (Bridge: 0.0109 * Flux: 99.9894%)
- `watchfiles-1.1.1/watchfiles/main.py` -> **Severity: 0.979** (Bridge: 0.0098 * Flux: 100.0%)
- `watchfiles-1.1.1/watchfiles/__init__.py` -> **Severity: 0.641** (Bridge: 0.0207 * Flux: 31.0026%)
- `watchfiles-1.1.1/watchfiles/run.py` -> **Severity: 0.126** (Bridge: 0.0013 * Flux: 99.9981%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 0.095** (Bridge: 0.0009 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `watchfiles-1.1.1/watchfiles/main.py` -> **Severity: 17.568** (Embedded: 0.2561 * Error Risk: 68.6092%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 16.273** (Embedded: 0.2439 * Error Risk: 66.73%)
- `watchfiles-1.1.1/watchfiles/__init__.py` -> **Severity: 14.632** (Embedded: 0.2845 * Error Risk: 51.4282%)
- `watchfiles-1.1.1/watchfiles/run.py` -> **Severity: 14.092** (Embedded: 0.2048 * Error Risk: 68.7931%)
- `watchfiles-1.1.1/watchfiles/version.py` -> **Severity: 9.755** (Embedded: 0.1897 * Error Risk: 51.4282%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `watchfiles-1.1.1/watchfiles/main.py` -> **Severity: 17888.025** (Blast Radius: 238.507 * Doc Risk: 75.0%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 14782.421** (Blast Radius: 180.674 * Doc Risk: 81.8182%)
- `watchfiles-1.1.1/watchfiles/run.py` -> **Severity: 4174.05** (Blast Radius: 55.654 * Doc Risk: 75.0%)
- `watchfiles-1.1.1/watchfiles/cli.py` -> **Severity: 1919.934** (Blast Radius: 28.799 * Doc Risk: 66.6667%)
- `watchfiles-1.1.1/tests/conftest.py` -> **Severity: 1315.462** (Blast Radius: 14.438 * Doc Risk: 91.1111%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 766 call pairs -- scoped 26.9%, unique 0.0%, ambiguous 5.4%, external 67.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 688 | 29.8% | 0.0% | 6.0% | 64.2% |
| rust | 78 | 1.3% | 0.0% | 0.0% | 98.7% |

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
