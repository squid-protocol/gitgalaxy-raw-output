# ARCHITECTURAL_BRIEF: propcache
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
- **Scope:** 29 analyzed artifact(s), 1040 LOC.
- **Load-bearing artifact:** `propcache-0.4.1/src/propcache/api.py` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `propcache-0.4.1/packaging/pep517_backend/_backend.py` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `propcache-0.4.1/packaging/pep517_backend/_backend.py` at magnitude 139.02 (structural weight, not risk).
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
| Total Artifacts | 43 |
| Analyzed Artifacts (Scanned) | 29 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 14 |
| Total LOC | 1040 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5237 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1623 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7586 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 19 | 1040 | 65.5% |
| PLAINTEXT | 9 | 0 | 31.0% |
| MARKDOWN | 1 | 0 | 3.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 48%, Generic / Templated Code Files 24%, Declarative / Non-Code 7%, Large Core Modules (2) 7%, Compute Cores Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19 | 65.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 34.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 14*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 57.9 | 18.0 | 16.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.8 | 63.6 | 73.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 34.1 | 13.7 | 10.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.6 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 26.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3 | 3 | 0 | `propcache-0.4.1/packaging/pep517_backend/_transformers.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 104 | 14 | 7 | `propcache-0.4.1/tests/test_under_cached_property.py` |
| danger | 39 | 11 | 3 | `propcache-0.4.1/tests/test_under_cached_property.py` |
| concurrency | 21 | 4 | 3 | `propcache-0.4.1/packaging/pep517_backend/_backend.py` |
| connectivity | 98 | 16 | 9 | `propcache-0.4.1/tests/test_under_cached_property.py` |
| io | 33 | 9 | 2 | `propcache-0.4.1/tests/test_under_cached_property.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 64 | 6 | 9 | `propcache-0.4.1/tests/conftest.py` |
| docs | 107 | 17 | 12 | `propcache-0.4.1/tests/test_cached_property.py` |
| debt | 46 | 4 | 7 | `propcache-0.4.1/tests/test_under_cached_property.py` |
| mutation | 407 | 15 | 47 | `propcache-0.4.1/packaging/pep517_backend/_backend.py` |
| dead_code | 33 | 6 | 5 | `propcache-0.4.1/tests/test_cached_property.py` |
| credential | 0 | 0 | 0 | - |
| threat | 9 | 4 | 1 | `propcache-0.4.1/src/propcache/_helpers_c.pyx` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `propcache-0.4.1/tests/test_under_cached_property.py` (Hits: 11)
- `propcache-0.4.1/tests/test_cached_property.py` (Hits: 8)
- `propcache-0.4.1/packaging/pep517_backend/_compat.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **api.py** (`propcache-0.4.1/src/propcache/api.py`) — 3 inbound connections
2. **_compat.py** (`propcache-0.4.1/packaging/pep517_backend/_compat.py`) — 2 inbound connections
3. **_cython_configuration.py** (`propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py`) — 2 inbound connections
4. **_transformers.py** (`propcache-0.4.1/packaging/pep517_backend/_transformers.py`) — 2 inbound connections
5. **_backend.py** (`propcache-0.4.1/packaging/pep517_backend/_backend.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_backend.py** (`propcache-0.4.1/packaging/pep517_backend/_backend.py`) — 19 outbound dependencies
2. **_cython_configuration.py** (`propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py`) — 10 outbound dependencies
3. **cli.py** (`propcache-0.4.1/packaging/pep517_backend/cli.py`) — 8 outbound dependencies
4. **_compat.py** (`propcache-0.4.1/packaging/pep517_backend/_compat.py`) — 7 outbound dependencies
5. **test_cached_property.py** (`propcache-0.4.1/tests/test_cached_property.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `maybe_prebuild_c_extensions` **(Many-Argument Workhorses)** (@ `propcache-0.4.1/packaging/pep517_backend/_backend.py`) -> Impact: **19.1** | LOC: 62
- `pytest_collection_modifyitems` **(Generic / Templated Code)** (@ `propcache-0.4.1/tests/conftest.py`) -> Impact: **11.1** | LOC: 22
- `get_requires_for_build_wheel` **(Compute Cores)** (@ `propcache-0.4.1/packaging/pep517_backend/_backend.py`) -> Impact: **9.8** | LOC: 27
- `_exclude_dir_path` **(Stateful Encapsulated Methods)** (@ `propcache-0.4.1/packaging/pep517_backend/_backend.py`) -> Impact: **9.1** | LOC: 21
- `__get__` **(Compute Cores)** (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> Impact: **8.7** | LOC: 14
- `__set_name__` **(Compute Cores)** (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> Impact: **8.4** | LOC: 8
- `test_under_cached_property_no_refcount_leak` **(Defensive Guards)** (@ `propcache-0.4.1/tests/test_under_cached_property.py`) -> Impact: **8.1** | LOC: 78
  * *Intent:* """Test that under_cached_property does not leak references."""
- `test_cached_property_no_refcount_leak` **(Defensive Guards)** (@ `propcache-0.4.1/tests/test_cached_property.py`) -> Impact: **8.0** | LOC: 75
  * *Intent:* """Test that cached_property does not leak references."""
- `_get_setting_value` **(Stateful Encapsulated Methods)** (@ `propcache-0.4.1/packaging/pep517_backend/_backend.py`) -> Impact: **7.7** | LOC: 19
- `__get__` **(Compute Cores)** (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> Impact: **6.5** | LOC: 10

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `propcache-0.4.1/tests` | 6 | 413.8 | 10.57% | 0.0% |
| `propcache-0.4.1/packaging/pep517_backend` | 8 | 299.4 | 13.21% | 0.0% |
| `propcache-0.4.1/src/propcache` | 5 | 158.92 | 34.58% | 0.0% |
| `propcache-0.4.1/requirements` | 7 | 7.0 | 0.0% | 0.0% |
| `propcache-0.4.1` | 2 | 2.0 | 0.0% | 0.0% |
| `propcache-0.4.1/packaging` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **100.0%** Exposure
- `propcache-0.4.1/packaging/pep517_backend/_transformers.py` -> **100.0%** Exposure
- `propcache-0.4.1/src/propcache/_helpers.py` -> **100.0%** Exposure
- `propcache-0.4.1/src/propcache/_helpers_py.py` -> **99.9997%** Exposure
- `propcache-0.4.1/src/propcache/_helpers_c.pyx` -> **99.8921%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `propcache-0.4.1/tests/test_under_cached_property.py` -> **9** Orphaned Functions | **18** Duplicates
- `propcache-0.4.1/tests/test_cached_property.py` -> **9** Orphaned Functions | **13** Duplicates
- `propcache-0.4.1/tests/test_benchmarks.py` -> **4** Orphaned Functions | **8** Duplicates
- `propcache-0.4.1/tests/conftest.py` -> **5** Orphaned Functions | **0** Duplicates
- `propcache-0.4.1/tests/test_init.py` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `80` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `propcache-0.4.1/packaging/pep517_backend/_backend.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 139.02 | **LOC:** 392 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 42.752; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 73.913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybe_prebuild_c_extensions` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `get_requires_for_build_wheel` **(Compute Cores)** (Impact: 9.8)
  * `_exclude_dir_path` **(Stateful Encapsulated Methods)** (Impact: 9.1)
  * `_get_setting_value` **(Stateful Encapsulated Methods)** (Impact: 7.7)
  * `build_wheel` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 107`, `args: 16`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 38`
* *Architecture:* `io: 2`, `api: 9`, `import: 26`
* *Defense:* `safety: 9`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 42.752
  * `Choke Point (Betweenness):` 0.003968 | `Ripple Effect (Closeness):` 0.035714
  * `Imports (Out-Degree: 3):` ._compat, ._cython_configuration, ._transformers, Cython.Build.Cythonize, __future__, collections.abc, contextlib, distutils.command.install...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/tests/test_cached_property.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 132.0 | **LOC:** 227 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 23.109; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.8%), Complexity Load (formerly Cognitive Load) (20.9%), Connectivity (formerly Api Exposure) (10.9%)
- **Documentation Coverage:** 32.6087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_cached_property_no_refcount_leak` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* """Test that cached_property does not leak references."""
  * `test_set_name` **(Annotated & Test Methods)** (Impact: 6.4)
    * *Intent:* """Test that the __set_name__ method is called and checked."""
  * `test_get_without_set_name` **(Generic / Templated Code)** (Impact: 6.2)
    * *Intent:* """Test that get without __set_name__ fails."""
  * `test_cached_property_class_docstring` **(Defensive Guards)** (Impact: 4.9)
  * `test_cached_property` **(Generic / Templated Code)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 81`, `args: 26`, `func_start: 26`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 27`, `duplicate_logic: 13`, `unreferenced_by_name: 9`
* *Architecture:* `io: 8`, `api: 21`, `import: 8`
* *Defense:* `safety: 22`, `doc: 20`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections.abc, gc, operator, propcache.api, pytest, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/tests/test_under_cached_property.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 129.4 | **LOC:** 253 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 23.109; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.0%), Connectivity (formerly Api Exposure) (10.7%)
- **Documentation Coverage:** 49.0566% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_under_cached_property_no_refcount_leak` **(Defensive Guards)** (Impact: 8.1)
    * *Intent:* """Test that under_cached_property does not leak references."""
  * `test_under_cached_property_typeddict` **(C Struct Operations)** (Impact: 5.5)
    * *Intent:* """Test static typing passes with TypedDict."""
  * `test_under_cached_property` **(Generic / Templated Code)** (Impact: 5.2)
  * `test_under_cached_property_class_docstring` **(Defensive Guards)** (Impact: 5.1)
  * `count_sentinels` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* """Count the number of UnderCachedPropertySentinel instances in gc."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 88`, `args: 31`, `func_start: 31`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 24`, `duplicate_logic: 18`, `unreferenced_by_name: 9`
* *Architecture:* `io: 11`, `api: 24`, `import: 7`
* *Defense:* `safety: 24`, `doc: 17`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections.abc, gc, propcache.api, pytest, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/tests/test_benchmarks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 74.52 | **LOC:** 93 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 23.109; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (85.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (18.3%), Connectivity (formerly Api Exposure) (8.0%)
- **Documentation Coverage:** 30.7692% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_under_cached_property_cache_miss` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* """Benchmark for under_cached_property cache miss."""
  * `test_under_cached_property_cache_hit` **(Encapsulated Accessors)** (Impact: 3.7)
    * *Intent:* """Benchmark for under_cached_property cache hit."""
  * `test_cached_property_cache_hit` **(Generic / Templated Code)** (Impact: 3.7)
    * *Intent:* """Benchmark for cached_property cache hit."""
  * `test_cached_property_cache_miss` **(C Struct Operations)** (Impact: 3.7)
    * *Intent:* """Benchmark for cached_property cache miss."""
  * `_run` **(Encapsulated Accessors)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 26`, `args: 15`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `duplicate_logic: 8`, `unreferenced_by_name: 4`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 2`, `doc: 9`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` propcache, pytest, pytest_codspeed
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 57.5 | **LOC:** 116 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 23.109; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (10.2%), Connectivity (formerly Api Exposure) (9.2%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pytest_collection_modifyitems` **(Generic / Templated Code)** (Impact: 11.1)
  * `tag` **(Generic / Templated Code)** (Impact: 4.4)
    * *Intent:* """Return a text representation of the pure-python attribute."""
  * `imported_module` **(Generic / Templated Code)** (Impact: 4.4)
    * *Intent:* """Return a loaded importable containing a propcache variant."""
  * `pytest_addoption` **(Generic / Templated Code)** (Impact: 2.6)
  * `propcache_module` **(Generic / Templated Code)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 26`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `unreferenced_by_name: 5`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `doc: 10`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, dataclasses, functools, importlib, pytest, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/_transformers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 52.9 | **LOC:** 112 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 58.54; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (29.2%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_emit_opt_pairs` **(Stateful Encapsulated Methods)** (Impact: 6.1)
  * `sanitize_rst_roles` **(I/O & Config Routines)** (Impact: 5.3)
    * *Intent:* """Replace RST roles with inline highlighting."""
  * `get_enabled_cli_flags_from_config` **(Generic / Templated Code)** (Impact: 4.4)
    * *Intent:* """Make a list of enabled boolean flags from config."""
  * `get_cli_kwargs_from_config` **(Generic / Templated Code)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 17`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.54
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.095238
  * `Imports (Out-Degree: 0):` collections.abc, itertools, re, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/src/propcache/_helpers_c.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 49.8 | **LOC:** 104 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 62.565; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (76.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__get__` **(Compute Cores)** (Impact: 8.7)
  * `__set_name__` **(Compute Cores)** (Impact: 8.4)
  * `__get__` **(Compute Cores)** (Impact: 6.5)
  * `__set__` **(Parameter Forwarders)** (Impact: 2.1)
  * `__init__` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074405
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 46.94 | **LOC:** 128 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 54.865; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (32.3%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patched_env` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* """Temporary set given env vars. :param env: tmp env vars to set :type env: dict :yields: None """
  * `_configure_cython_line_tracing` **(Stateful Encapsulated Methods)** (Impact: 3.9)
    * *Intent:* """Configure Cython line tracing directives if requested."""
  * `get_local_cython_config` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* """Grab optional build dependencies from pyproject.toml config. :returns: config section from ``pypr...
  * `make_cythonize_cli_args_from_config` **(Generic / Templated Code)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 28`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 2`, `api: 4`, `import: 10`
* *Defense:* `safety: 4`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 54.865
  * `Choke Point (Betweenness):` 0.002646 | `Ripple Effect (Closeness):` 0.080357
  * `Imports (Out-Degree: 2):` ._compat, ._transformers, __future__, collections.abc, contextlib, expandvars, os, pathlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/src/propcache/_helpers.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 41.56 | **LOC:** 40 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 92.841; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.5%), Complexity Load (formerly Cognitive Load) (57.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 28`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 1`, `api: 1`, `import: 11`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 92.841
  * `Choke Point (Betweenness):` 0.010582 | `Ripple Effect (Closeness):` 0.081633
  * `Imports (Out-Degree: 2):` ._helpers_c, ._helpers_py, os, sys, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/src/propcache/_helpers_py.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 36.34 | **LOC:** 63 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 62.565; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__get__` **(Generic / Templated Code)** (Impact: 4.5)
  * `__get__` **(Generic / Templated Code)** (Impact: 2.1)
  * `__set__` **(Generic / Templated Code)** (Impact: 2.1)
  * `__get__` **(Generic / Templated Code)** (Impact: 2.0)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 4`, `import: 5`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074405
  * `Imports (Out-Degree: 0):` collections.abc, functools, sys, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/tests/test_init.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 17.96 | **LOC:** 44 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 23.109; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (21.4%), Connectivity (formerly Api Exposure) (9.1%), Complexity Load (formerly Cognitive Load) (3.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_importing_invalid_attr_raises` **(Generic / Templated Code)** (Impact: 4.2)
    * *Intent:* """Verify importing an invalid attribute raises an AttributeError."""
  * `test_public_api_is_discoverable_in_dir` **(Generic / Templated Code)** (Impact: 1.6)
    * *Intent:* """Verify the public API is discoverable programmatically."""
  * `test_api_at_top_level` **(Defensive Guards)** (Impact: 1.3)
    * *Intent:* """Verify the public API is accessible at top-level."""
  * `test_import_error_invalid_attr` **(Generic / Templated Code)** (Impact: 1.3)
    * *Intent:* """Verify importing an invalid attribute raises an ImportError."""
  * `test_no_wildcard_imports` **(Generic / Templated Code)** (Impact: 1.1)
    * *Intent:* """Verify wildcard imports are prohibited."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 19`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 6`, `doc: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` propcache, pytest, system
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/src/propcache/__init__.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 16.62 | **LOC:** 33 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 23.109; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (77.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (26.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_import_facade` **(Encapsulated Accessors)** (Impact: 3.2)
    * *Intent:* """Import the public API from the `api` module."""
  * `_dir_facade` **(Encapsulated Accessors)** (Impact: 1.1)
    * *Intent:* """Include the public API in the module's dir() output."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , .api, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 16.48 | **LOC:** 55 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 23.109; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (85.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (16.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_main_program` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* """Invoke ``translate-cython`` or fail."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 29`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`
* *Architecture:* `io: 2`, `api: 1`, `import: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ._cython_configuration, Cython.Compiler.CmdLine, Cython.Compiler.Main, __future__, collections.abc, itertools, pathlib, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/hooks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 15.28 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 23.109; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ._backend, contextlib, setuptools.build_meta
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/src/propcache/api.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 14.6 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 82.038; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 82.038
  * `Choke Point (Betweenness):` 0.011905 | `Ripple Effect (Closeness):` 0.107143
  * `Imports (Out-Degree: 1):` ._helpers
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/packaging/pep517_backend/__main__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 12.08 | **LOC:** 7 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 23.109; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (73.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/_compat.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 6.18 | **LOC:** 29 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 58.54; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (34.1%), Mutation Surface (formerly State Flux) (31.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chdir_cm` **(Defensive Guards)** (Impact: 1.8)
    * *Intent:* """Temporarily change the current directory, recovering on exit."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 18`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 5`, `api: 2`, `import: 8`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.54
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.095238
  * `Imports (Out-Degree: 0):` collections.abc, contextlib, os, pathlib, sys, tomli, tomllib
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/tests/test_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2.42 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 23.109; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_api` **(Defensive Guards)** (Impact: 1.3)
    * *Intent:* """Verify the public API is accessible."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 4`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` propcache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/NOTICE` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/codspeed.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/cython.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/dev.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/doc-spelling.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.109
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

- `propcache-0.4.1/src/propcache/_helpers.py` -> **Severity: 1.058** (Bridge: 0.0106 * Flux: 100.0%)
- `propcache-0.4.1/packaging/pep517_backend/_backend.py` -> **Severity: 0.396** (Bridge: 0.004 * Flux: 99.7579%)
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **Severity: 0.265** (Bridge: 0.0026 * Flux: 100.0%)
- `propcache-0.4.1/src/propcache/api.py` -> **Severity: 0.2** (Bridge: 0.0119 * Flux: 16.7982%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `propcache-0.4.1/packaging/pep517_backend/_transformers.py` -> **Severity: 8.428** (Embedded: 0.0952 * Error Risk: 88.4933%)
- `propcache-0.4.1/src/propcache/_helpers.py` -> **Severity: 7.306** (Embedded: 0.0816 * Error Risk: 89.4999%)
- `propcache-0.4.1/src/propcache/_helpers_py.py` -> **Severity: 7.199** (Embedded: 0.0744 * Error Risk: 96.7525%)
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **Severity: 7.008** (Embedded: 0.0804 * Error Risk: 87.2138%)
- `propcache-0.4.1/src/propcache/api.py` -> **Severity: 6.444** (Embedded: 0.1071 * Error Risk: 60.143%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `propcache-0.4.1/src/propcache/_helpers_c.pyx` -> **Severity: 6256.5** (Blast Radius: 62.565 * Doc Risk: 100.0%)
- `propcache-0.4.1/src/propcache/_helpers_py.py` -> **Severity: 6256.5** (Blast Radius: 62.565 * Doc Risk: 100.0%)
- `propcache-0.4.1/packaging/pep517_backend/_backend.py` -> **Severity: 3159.929** (Blast Radius: 42.752 * Doc Risk: 73.913%)
- `propcache-0.4.1/packaging/pep517_backend/_transformers.py` -> **Severity: 2508.855** (Blast Radius: 58.54 * Doc Risk: 42.8571%)
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **Severity: 1567.57** (Blast Radius: 54.865 * Doc Risk: 28.5714%)

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
