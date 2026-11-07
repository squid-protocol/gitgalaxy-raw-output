# ARCHITECTURAL_BRIEF: python-discovery
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
- **Scope:** 34 analyzed artifact(s), 4546 LOC.
- **Load-bearing artifact:** `python_discovery-1.2.1/src/python_discovery/_py_info.py` -- 13 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `python_discovery-1.2.1/src/python_discovery/_py_info.py` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `python_discovery-1.2.1/src/python_discovery/_py_info.py` at magnitude 922.5 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 34 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 4546 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 79.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3058 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0428 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9545 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 26 | 4429 | 76.5% |
| YAML | 5 | 117 | 14.7% |
| MARKDOWN | 3 | 0 | 8.8% |

## 4.1 SOURCE ENCODINGS
All 34 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 29%, Data / Markup / Trivial 24%, Large Core Modules (2) 12%, Large Core Modules (3) 12%, Declarative / Non-Code 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 31 | 91.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 8.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.4 | 24.7 | 29.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.6 | 47.5 | 50.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 9.9 | 0.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 75.9 | 18.4 | 12.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 65.2 | 3.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 74.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 212 | 18 | 18 | `python_discovery-1.2.1/tests/test_discovery.py` |
| cleanup | 1 | 1 | 0 | `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` |
| guards | 606 | 24 | 46 | `python_discovery-1.2.1/tests/test_py_info_extra.py` |
| danger | 68 | 17 | 4 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| concurrency | 65 | 11 | 5 | `python_discovery-1.2.1/src/python_discovery/_discovery.py` |
| connectivity | 390 | 27 | 31 | `python_discovery-1.2.1/tests/test_py_info_extra.py` |
| io | 174 | 19 | 17 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| crypto | 2 | 2 | 0 | `python_discovery-1.2.1/src/python_discovery/_cache.py` |
| ipc | 12 | 3 | 0 | `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 10 | 4 | 1 | `python_discovery-1.2.1/src/python_discovery/_py_spec.py` |
| events | 3 | 2 | 0 | `python_discovery-1.2.1/.github/workflows/check.yaml` |
| tests | 592 | 14 | 69 | `python_discovery-1.2.1/tests/test_py_info_extra.py` |
| docs | 95 | 16 | 10 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| debt | 3 | 2 | 0 | `python_discovery-1.2.1/tests/test_cached_py_info.py` |
| mutation | 2123 | 28 | 179 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| dead_code | 270 | 14 | 28 | `python_discovery-1.2.1/tests/test_py_info_extra.py` |
| credential | 1 | 1 | 0 | `python_discovery-1.2.1/tests/windows/test_windows_pep514.py` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.7647**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` (Hits: 49)
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` (Hits: 21)
- `python_discovery-1.2.1/tests/test_discovery.py` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_py_info.py`) — 13 inbound connections
2. **__init__.py** (`python_discovery-1.2.1/src/python_discovery/__init__.py`) — 10 inbound connections
3. **_py_spec.py** (`python_discovery-1.2.1/src/python_discovery/_py_spec.py`) — 10 inbound connections
4. **_cache.py** (`python_discovery-1.2.1/src/python_discovery/_cache.py`) — 8 inbound connections
5. **_discovery.py** (`python_discovery-1.2.1/src/python_discovery/_discovery.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_py_info.py`) — 22 outbound dependencies
2. **_cached_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`) — 18 outbound dependencies
3. **test_py_info.py** (`python_discovery-1.2.1/tests/py_info/test_py_info.py`) — 16 outbound dependencies
4. **_discovery.py** (`python_discovery-1.2.1/src/python_discovery/_discovery.py`) — 14 outbound dependencies
5. **test_discovery.py** (`python_discovery-1.2.1/tests/test_discovery.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_discovery_via_path` **(Many-Argument Workhorses)** (@ `python_discovery-1.2.1/tests/test_discovery.py`) -> Impact: **52.3** | LOC: 40
- `_get_via_file_cache` **(Many-Argument Workhorses)** (@ `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`) -> Impact: **41.8** | LOC: 52
- `_mock_pyinfo` **(Stateful Encapsulated Methods)** (@ `python_discovery-1.2.1/tests/windows/conftest.py`) -> Impact: **35.6** | LOC: 26
- `satisfies` **(Compute Cores)** (@ `python_discovery-1.2.1/src/python_discovery/_py_spec.py`) -> Impact: **34.2** | LOC: 26
  * *Intent:* """ Check if this spec is compatible with the given *spec* (e.g. PEP-514 on Windows). :param spec: the requirement to check against. """
- `satisfies` **(Compute Cores)** (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **33.1** | LOC: 23
  * *Intent:* """ Check if a given specification can be satisfied by this python interpreter instance. :param spec: the specification to check against. :param impl_...
- `from_string` **(Compute Cores)** (@ `python_discovery-1.2.1/src/python_discovery/_specifier.py`) -> Impact: **32.3** | LOC: 22
  * *Intent:* """ Parse a PEP 440 version string (e.g. ``3.12.1``). :param version_str: the version string to parse. """
- `discover_exe` **(Many-Argument Workhorses)** (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **31.3** | LOC: 39
- `_run_subprocess` **(Many-Argument Workhorses)** (@ `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`) -> Impact: **30.8** | LOC: 56
- `_check_exe` **(Many-Argument Workhorses)** (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **29.8** | LOC: 30
- `_find_interpreter` **(Stateful Encapsulated Methods)** (@ `python_discovery-1.2.1/src/python_discovery/_discovery.py`) -> Impact: **25.7** | LOC: 25

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `python_discovery-1.2.1/src/python_discovery` | 8 | 2232.42 | 32.0% | 0.0% |
| `python_discovery-1.2.1/tests` | 9 | 1517.86 | 31.91% | 0.0% |
| `python_discovery-1.2.1/tests/py_info` | 2 | 390.14 | 31.24% | 0.0% |
| `python_discovery-1.2.1/tests/windows` | 4 | 272.3 | 10.1% | 0.0% |
| `python_discovery-1.2.1/src/python_discovery/_windows` | 3 | 257.26 | 37.1% | 3.3% |
| `python_discovery-1.2.1/.github` | 4 | 38.28 | 0.0% | 0.0% |
| `python_discovery-1.2.1/.github/workflows` | 2 | 14.66 | 3.73% | 0.0% |
| `python_discovery-1.2.1` | 2 | 2.22 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` -> **9.907%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_py_spec.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_specifier.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `python_discovery-1.2.1/tests/test_py_info_extra.py` -> **59** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/test_specifier.py` -> **39** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/py_info/test_py_info.py` -> **29** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/test_discovery_extra.py` -> **28** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/test_discovery.py` -> **24** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `218` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `python_discovery-1.2.1/src/python_discovery/_py_info.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.146)
- **Top Global Matches:** file_cluster_5: 9.146, file_cluster_0: 9.571, file_cluster_12: 9.588
- **Magnitude:** 922.5 | **LOC:** 814 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **22**; blast radius 123.252; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (47.4%)
- **Documentation Coverage:** 51.0417% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `satisfies` **(Compute Cores)** (Impact: 33.1)
    * *Intent:* """ Check if a given specification can be satisfied by this python interpreter instance. :param spec...
  * `discover_exe` **(Many-Argument Workhorses)** (Impact: 31.3)
  * `_check_exe` **(Many-Argument Workhorses)** (Impact: 29.8)
  * `_init_sysconfig` **(Stateful Encapsulated Methods)** (Impact: 22.8)
  * `_satisfies_version_specifier` **(Stateful Encapsulated Methods)** (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 142 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 163`, `args: 47`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 177`
* *Architecture:* `io: 49`, `api: 31`, `import: 23`
* *Defense:* `safety: 17`, `doc: 30`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 123.252
  * `Choke Point (Betweenness):` 0.035038 | `Ripple Effect (Closeness):` 0.409091
  * `Imports (Out-Degree: 4):` ._cache, ._cached_py_info, ._compat, ._py_spec, __future__, collections, collections.abc, distutils...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/test_discovery.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.895)
- **Top Global Matches:** file_cluster_0: 8.895, file_cluster_4: 10.47, file_cluster_10: 10.499
- **Magnitude:** 403.48 | **LOC:** 447 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.2%), Connectivity (formerly Api Exposure) (10.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_discovery_via_path` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `test_shim_resolved_to_real_binary` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `test_discovery_absolute_path_with_try_first` **(Type Conversions)** (Impact: 9.8)
  * `test_uv_python` **(Type Conversions)** (Impact: 8.9)
  * `_create_versioned_binary` **(Stateful Encapsulated Methods)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 122`, `args: 32`, `func_start: 28`
* *Risk/State:* `state_mutation: 95`, `unreferenced_by_name: 24`
* *Architecture:* `io: 18`, `api: 26`, `import: 14`
* *Defense:* `safety: 44`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, logging, os, pathlib, pytest, pytest_mock, python_discovery, python_discovery._discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_py_info_extra.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.741)
- **Top Global Matches:** file_cluster_0: 7.741, file_cluster_5: 10.478, file_cluster_12: 10.638
- **Magnitude:** 400.32 | **LOC:** 517 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.1%), Complexity Load (formerly Cognitive Load) (41.2%), Connectivity (formerly Api Exposure) (13.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_possible_base_case_sensitive` **(Defensive Guards)** (Impact: 7.6)
  * `test_check_exe_mismatch_not_exact` **(Type Conversions)** (Impact: 5.7)
  * `test_check_exe_mismatch_exact` **(Type Conversions)** (Impact: 5.7)
  * `test_resolve_to_system_circle` **(Generic / Templated Code)** (Impact: 4.5)
  * `test_resolve_to_system_single_prefix_self_link` **(Defensive Guards)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 216
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 157`, `args: 60`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 166`, `unreferenced_by_name: 59`
* *Architecture:* `io: 12`, `api: 59`, `import: 13`
* *Defense:* `safety: 86`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, copy, logging, os, pathlib, pytest, pytest_mock, python_discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_discovery.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.699)
- **Top Global Matches:** file_cluster_9: 9.699, file_cluster_0: 10.15, file_cluster_5: 11.087
- **Magnitude:** 379.34 | **LOC:** 336 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **14**; blast radius 37.239; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.4%), Complexity Load (formerly Cognitive Load) (50.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 72.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_find_interpreter` **(Stateful Encapsulated Methods)** (Impact: 25.7)
  * `_read_python_version_file` **(Stateful Encapsulated Methods)** (Impact: 19.8)
    * *Intent:* """Read a ``.python-version`` file, optionally searching parent directories."""
  * `propose_interpreters` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `get_interpreter` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `_propose_explicit` **(Stateful Encapsulated Methods)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 86`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 53`
* *Architecture:* `io: 21`, `api: 10`, `import: 14`
* *Defense:* `safety: 6`, `doc: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.239
  * `Choke Point (Betweenness):` 0.035038 | `Ripple Effect (Closeness):` 0.215686
  * `Imports (Out-Degree: 5):` ._cache, ._compat, ._py_info, ._py_spec, ._windows, __future__, collections.abc, contextlib...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/py_info/test_py_info.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.805)
- **Top Global Matches:** file_cluster_0: 7.805, file_cluster_5: 8.601, file_cluster_12: 8.878
- **Magnitude:** 313.4 | **LOC:** 455 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (29.6%), Connectivity (formerly Api Exposure) (10.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_system_executable_no_exact_match` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `test_bad_exe_py_info_no_raise` **(Defensive Guards)** (Impact: 7.7)
  * `test_select_most_likely_prefers_machine_match` **(Generic / Templated Code)** (Impact: 6.6)
  * `_generate_not_match_current_interpreter_version` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `test_py_info_cache_clear` **(Defensive Guards)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 128`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 83`, `unreferenced_by_name: 29`
* *Architecture:* `io: 12`, `api: 31`, `import: 17`
* *Defense:* `safety: 64`, `doc: 1`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, copy, itertools, json, logging, os, pathlib, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.246)
- **Top Global Matches:** file_cluster_4: 8.246, file_cluster_6: 11.551, file_cluster_0: 11.964
- **Magnitude:** 269.88 | **LOC:** 265 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 49.689; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.7%), Complexity Load (formerly Cognitive Load) (64.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_via_file_cache` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `_run_subprocess` **(Many-Argument Workhorses)** (Impact: 30.8)
  * `from_exe` **(Many-Argument Workhorses)** (Impact: 14.1)
  * `_get_from_cache` **(Stateful Encapsulated Methods)** (Impact: 13.1)
  * `_extract_between_cookies` **(Stateful Encapsulated Methods)** (Impact: 10.7)
    * *Intent:* """Extract payload between reversed cookie markers, forwarding any surrounding output to stdout."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 68`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`
* *Architecture:* `io: 6`, `api: 7`, `import: 20`
* *Defense:* `safety: 15`, `doc: 2`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 49.689
  * `Choke Point (Betweenness):` 0.000473 | `Ripple Effect (Closeness):` 0.251748
  * `Imports (Out-Degree: 2):` ._cache, ._py_info, __future__, collections, collections.abc, contextlib, hashlib, json...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_specifier.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.723)
- **Top Global Matches:** file_cluster_0: 7.723, file_cluster_4: 9.853, file_cluster_5: 10.238
- **Magnitude:** 267.42 | **LOC:** 312 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 77.865; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.8%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_string` **(Compute Cores)** (Impact: 32.3)
    * *Intent:* """ Parse a PEP 440 version string (e.g. ``3.12.1``). :param version_str: the version string to pars...
  * `__lt__` **(Defensive Guards)** (Impact: 18.0)
  * `from_string` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* """ Parse a single PEP 440 specifier (e.g. ``>=3.10``). :param spec_str: the specifier string to par...
  * `_check_standard` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `contains` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* """ Check if a version string satisfies this specifier. :param version_str: the version string to te...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 90`, `args: 25`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`
* *Architecture:* `io: 1`, `api: 14`, `import: 8`
* *Defense:* `safety: 10`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 77.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.30303
  * `Imports (Out-Degree: 0):` __future__, collections.abc, contextlib, dataclasses, operator, re, sys, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_py_spec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.511)
- **Top Global Matches:** file_cluster_4: 7.511, file_cluster_6: 11.499, file_cluster_16: 12.026
- **Magnitude:** 261.6 | **LOC:** 263 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 83.636; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (30.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `satisfies` **(Compute Cores)** (Impact: 34.2)
    * *Intent:* """ Check if this spec is compatible with the given *spec* (e.g. PEP-514 on Windows). :param spec: t...
  * `generate_re` **(Compute Cores)** (Impact: 23.4)
    * *Intent:* """ Generate a regular expression for matching interpreter filenames. :param windows: if ``True``, r...
  * `_check_version_specifier` **(Stateful Encapsulated Methods)** (Impact: 18.4)
    * *Intent:* """Check if version specifier is satisfied."""
  * `_parse_spec_pattern` **(Stateful Encapsulated Methods)** (Impact: 12.3)
  * `_parse_version_parts` **(Stateful Encapsulated Methods)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 61`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 48`
* *Architecture:* `io: 3`, `api: 8`, `import: 7`
* *Defense:* `safety: 4`, `doc: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 83.636
  * `Choke Point (Betweenness):` 0.011048 | `Ripple Effect (Closeness):` 0.363636
  * `Imports (Out-Degree: 2):` ._py_info, ._specifier, __future__, contextlib, pathlib, re, typing
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/windows/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.641)
- **Top Global Matches:** file_cluster_0: 8.641, file_cluster_5: 9.991, file_cluster_16: 10.052
- **Magnitude:** 207.96 | **LOC:** 176 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (35.4%), Connectivity (formerly Api Exposure) (0.2%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mock_pyinfo` **(Stateful Encapsulated Methods)** (Impact: 35.6)
  * `satisfies` **(Compute Cores)** (Impact: 17.8)
  * `_make_open_key_ex` **(Stateful Encapsulated Methods)** (Impact: 16.4)
  * `_open_key_ex` **(Stateful Encapsulated Methods)** (Impact: 13.4)
  * `_mock_registry` **(Stateful Encapsulated Methods)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 59`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 34`, `unreferenced_by_name: 5`
* *Architecture:* `io: 5`, `api: 1`, `import: 14`
* *Defense:* `safety: 8`, `doc: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, collections.abc, contextlib, os, pathlib, pytest, python_discovery._cached_py_info, python_discovery._py_info...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.237)
- **Top Global Matches:** file_cluster_5: 7.237, file_cluster_12: 9.877, file_cluster_7: 10.099
- **Magnitude:** 195.72 | **LOC:** 223 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 38.867; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%), Connectivity (formerly Api Exposure) (57.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_version` **(Defensive Guards)** (Impact: 19.0)
  * `load_exe` **(Defensive Guards)** (Impact: 18.8)
  * `load_threaded` **(Defensive Guards)** (Impact: 13.9)
  * `process_tag` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `parse_arch` **(Defensive Guards)** (Impact: 10.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 59`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 23`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 13`, `import: 9`
* *Defense:* `safety: 15`, `doc: 4`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.867
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.158562
  * `Imports (Out-Degree: 0):` __future__, collections.abc, logging, os, re, sys, typing, winreg
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/test_discovery_extra.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.45)
- **Top Global Matches:** file_cluster_5: 8.45, file_cluster_0: 9.707, file_cluster_12: 9.79
- **Magnitude:** 182.88 | **LOC:** 242 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (41.7%), Connectivity (formerly Api Exposure) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_propose_interpreters_relative_path` **(Type Conversions)** (Impact: 6.7)
  * `test_propose_interpreters_try_first_with_duplicate` **(Type Conversions)** (Impact: 6.1)
  * `test_propose_interpreters_relative_spec_is_abs` **(Type Conversions)** (Impact: 5.5)
  * `test_propose_interpreters_try_first_with_missing` **(Type Conversions)** (Impact: 3.3)
  * `test_active_versions_global_version_file` **(Type Conversions)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 81`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`, `unreferenced_by_name: 28`
* *Architecture:* `io: 12`, `api: 28`, `import: 12`
* *Defense:* `safety: 31`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, os, pathlib, pytest, pytest_mock, python_discovery, python_discovery._discovery, python_discovery._py_spec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_py_spec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.173)
- **Top Global Matches:** file_cluster_0: 7.173, file_cluster_13: 10.237, file_cluster_15: 10.645
- **Magnitude:** 131.56 | **LOC:** 238 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (65.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.1%), Guard Balance (formerly Safety Score) (32.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_version_satisfies_pairs` **(Stateful Encapsulated Methods)** (Impact: 9.8)
  * `_version_not_satisfies_pairs` **(Stateful Encapsulated Methods)** (Impact: 9.8)
  * `test_bad_py_spec` **(Defensive Guards)** (Impact: 2.5)
  * `test_spec_parse_arch_and_machine_together` **(Generic / Templated Code)** (Impact: 2.2)
  * `test_spec_satisfies_machine` **(Generic / Templated Code)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 73`, `args: 21`, `func_start: 21`
* *Risk/State:* `state_mutation: 34`, `unreferenced_by_name: 19`
* *Architecture:* `io: 6`, `api: 19`, `concurrency: 2`, `import: 8`
* *Defense:* `safety: 31`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, pathlib, pytest, python_discovery, python_discovery._py_info, python_discovery._specifier, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_cached_py_info.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.396)
- **Top Global Matches:** file_cluster_0: 8.396, file_cluster_12: 10.507, file_cluster_5: 10.884
- **Magnitude:** 124.48 | **LOC:** 241 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.1%), Guard Balance (formerly Safety Score) (29.5%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_from_exe_retry_on_first_failure` **(Defensive Guards)** (Impact: 4.7)
  * `test_resolve_py_info_script_pkgutil_returns_none` **(Generic / Templated Code)** (Impact: 3.1)
  * `test_run_subprocess_with_cookies` **(Defensive Guards)** (Impact: 2.3)
  * `test_get_via_file_cache_stale_hash` **(Defensive Guards)** (Impact: 2.2)
  * `test_get_via_file_cache_py_info_none` **(Defensive Guards)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 94`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 58`, `unreferenced_by_name: 22`
* *Architecture:* `io: 17`, `api: 22`, `import: 13`
* *Defense:* `safety: 54`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, json, logging, os, pathlib, pytest, pytest_mock, python_discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_specifier.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.697)
- **Top Global Matches:** file_cluster_0: 6.697, file_cluster_13: 10.488, file_cluster_15: 10.913
- **Magnitude:** 115.72 | **LOC:** 300 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (19.9%), Connectivity (formerly Api Exposure) (12.9%), Complexity Load (formerly Cognitive Load) (10.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_version_parse` **(Generic / Templated Code)** (Impact: 2.7)
  * `test_version_invalid_raises` **(Generic / Templated Code)** (Impact: 2.1)
  * `test_version_lt` **(Generic / Templated Code)** (Impact: 2.1)
  * `test_specifier_invalid_raises` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* # --- SimpleSpecifier ---
  * `test_specifier_contains` **(Generic / Templated Code)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 92`, `args: 39`, `func_start: 39`
* *Risk/State:* `state_mutation: 21`, `unreferenced_by_name: 39`
* *Architecture:* `api: 39`, `import: 3`
* *Defense:* `safety: 45`, `test: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pytest, python_discovery._specifier
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.436)
- **Top Global Matches:** file_cluster_5: 6.436, file_cluster_0: 8.922, file_cluster_12: 9.729
- **Magnitude:** 96.38 | **LOC:** 186 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **9**; blast radius 101.703; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.7%), Connectivity (formerly Api Exposure) (75.9%), Guard Balance (formerly Safety Score) (56.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 60.8696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `py_info_clear` **(Generic / Templated Code)** (Impact: 6.1)
    * *Intent:* """Remove all cached interpreter information."""
  * `read` **(Defensive Guards)** (Impact: 5.0)
  * `write` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* """ Persist *content* to the store. :param content: interpreter metadata to cache. """
  * `py_info` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* """ Return the content store for the interpreter at *path*. :param path: absolute path to a Python e...
  * `__init__` **(Encapsulated Accessors)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 64`, `args: 25`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 28`, `import: 9`
* *Defense:* `safety: 3`, `doc: 16`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 101.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.367309
  * `Imports (Out-Degree: 0):` __future__, collections.abc, contextlib, filelock, hashlib, json, logging, pathlib...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/py_info/test_py_info_exe_based_of.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.501)
- **Top Global Matches:** file_cluster_5: 8.501, file_cluster_0: 9.128, file_cluster_12: 9.263
- **Magnitude:** 76.74 | **LOC:** 83 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (32.9%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_discover_ok` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `_discover_base_folders` **(Encapsulated Accessors)** (Impact: 3.5)
  * `test_discover_empty_folder` **(Generic / Templated Code)** (Impact: 1.9)
  * `_fs_supports_symlink` **(Encapsulated Accessors)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 25`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 8`
* *Defense:* `safety: 3`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, logging, pathlib, pytest, python_discovery, python_discovery._compat, python_discovery._discovery, python_discovery._py_info
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_py_spec_extra.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.844)
- **Top Global Matches:** file_cluster_0: 7.844, file_cluster_5: 9.125, file_cluster_12: 10.129
- **Magnitude:** 74.08 | **LOC:** 131 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.5%), Guard Balance (formerly Safety Score) (35.7%), Connectivity (formerly Api Exposure) (12.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_specifier_with_invalid_inner` **(Defensive Guards)** (Impact: 3.1)
  * `test_get_required_precision_none` **(Interface Declarations)** (Impact: 1.6)
  * `test_get_required_precision_attribute_error` **(Defensive Guards)** (Impact: 1.6)
  * `test_specifier_parse_failure_fallback` **(Defensive Guards)** (Impact: 1.2)
  * `test_version_specifier_satisfies_micro` **(Generic / Templated Code)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 53`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `unreferenced_by_name: 18`
* *Architecture:* `api: 18`, `import: 6`
* *Defense:* `safety: 23`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, python_discovery, python_discovery._specifier, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.033)
- **Top Global Matches:** file_cluster_0: 8.033, file_cluster_5: 9.037, file_cluster_12: 10.365
- **Magnitude:** 70.34 | **LOC:** 116 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (35.0%), Complexity Load (formerly Cognitive Load) (32.2%), Connectivity (formerly Api Exposure) (12.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_disk_cache_py_info_clear_skips_non_json` **(Defensive Guards)** (Impact: 3.3)
  * `test_disk_cache_py_info_clear` **(Defensive Guards)** (Impact: 1.8)
  * `test_disk_content_store_read_valid_json` **(Generic / Templated Code)** (Impact: 1.7)
  * `test_disk_content_store_read_invalid_json` **(Defensive Guards)** (Impact: 1.7)
  * `test_disk_content_store_remove` **(Defensive Guards)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 44`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 18`, `import: 3`
* *Defense:* `safety: 19`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pathlib, python_discovery._cache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_windows/_propose.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.124)
- **Top Global Matches:** file_cluster_9: 8.124, file_cluster_0: 13.625, file_cluster_16: 13.879
- **Magnitude:** 44.86 | **LOC:** 54 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 27.026; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.4%), Complexity Load (formerly Cognitive Load) (54.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `propose_interpreters` **(Many-Argument Workhorses)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 16`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.026
  * `Choke Point (Betweenness):` 0.011364 | `Ripple Effect (Closeness):` 0.138125
  * `Imports (Out-Degree: 4):` ._pep514, __future__, collections.abc, python_discovery._cache, python_discovery._py_info, python_discovery._py_spec, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/windows/test_windows_pep514.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.31)
- **Top Global Matches:** file_cluster_13: 7.31, file_cluster_0: 7.513, file_cluster_15: 7.891
- **Magnitude:** 36.38 | **LOC:** 157 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.4%), Connectivity (formerly Api Exposure) (6.4%), Complexity Load (formerly Cognitive Load) (5.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pep514_run` **(Defensive Guards)** (Impact: 7.0)
  * `test_pep514_parse_functions` **(Defensive Guards)** (Impact: 5.8)
  * `test_pep514` **(I/O & Config Routines)** (Impact: 3.5)
  * `test_pep514_discovers_interpreters` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 36`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 4`, `import: 8`
* *Defense:* `safety: 13`, `doc: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, pytest, python_discovery._windows, python_discovery._windows._pep514, sys, textwrap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/windows/winreg_mock_values.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.574)
- **Top Global Matches:** file_cluster_2: 1.574, file_cluster_17: 4.62, file_cluster_13: 5.886
- **Magnitude:** 22.38 | **LOC:** 171 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 14.349; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.327)
- **Top Global Matches:** file_cluster_2: 5.327, file_cluster_17: 5.807, file_cluster_13: 6.287
- **Magnitude:** 18.42 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 50.94; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (31.0%), Connectivity (formerly Api Exposure) (26.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 50.94
  * `Choke Point (Betweenness):` 0.036774 | `Ripple Effect (Closeness):` 0.30303
  * `Imports (Out-Degree: 5):` ._cache, ._discovery, ._py_info, ._py_spec, ._specifier, __future__, importlib.metadata
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_compat.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.456)
- **Top Global Matches:** file_cluster_0: 6.456, file_cluster_13: 9.253, file_cluster_15: 9.933
- **Magnitude:** 16.88 | **LOC:** 30 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 49.921; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (45.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fs_path_id` **(Generic / Templated Code)** (Impact: 4.3)
  * `fs_is_case_sensitive` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 3`, `import: 6`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 49.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.280497
  * `Imports (Out-Degree: 0):` __future__, functools, logging, pathlib, tempfile, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_windows/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.726)
- **Top Global Matches:** file_cluster_2: 3.726, file_cluster_17: 4.794, file_cluster_13: 5.362
- **Magnitude:** 16.68 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 29.828; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.828
  * `Choke Point (Betweenness):` 0.029356 | `Ripple Effect (Closeness):` 0.176594
  * `Imports (Out-Degree: 2):` ._pep514, ._propose, __future__
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.627)
- **Top Global Matches:** file_cluster_0: 7.627, file_cluster_13: 9.873, file_cluster_16: 10.706
- **Magnitude:** 15.0 | **LOC:** 31 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 14.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (7.1%), Connectivity (formerly Api Exposure) (1.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_skip_if_test_in_system` **(Encapsulated Accessors)** (Impact: 4.5)
  * `_ensure_py_info_cache_empty` **(Encapsulated Accessors)** (Impact: 1.6)
  * `session_cache` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, collections.abc, pytest, python_discovery, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **Severity: 3.504** (Bridge: 0.035 * Flux: 100.0%)
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 3.504** (Bridge: 0.035 * Flux: 100.0%)
- `python_discovery-1.2.1/src/python_discovery/__init__.py` -> **Severity: 1.14** (Bridge: 0.0368 * Flux: 31.0026%)
- `python_discovery-1.2.1/src/python_discovery/_windows/_propose.py` -> **Severity: 1.136** (Bridge: 0.0114 * Flux: 99.9994%)
- `python_discovery-1.2.1/src/python_discovery/_py_spec.py` -> **Severity: 1.105** (Bridge: 0.011 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 32.971** (Embedded: 0.4091 * Error Risk: 80.5965%)
- `python_discovery-1.2.1/src/python_discovery/_py_spec.py` -> **Severity: 26.72** (Embedded: 0.3636 * Error Risk: 73.4787%)
- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **Severity: 20.604** (Embedded: 0.3673 * Error Risk: 56.0936%)
- `python_discovery-1.2.1/src/python_discovery/_specifier.py` -> **Severity: 20.23** (Embedded: 0.303 * Error Risk: 66.7599%)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **Severity: 17.283** (Embedded: 0.2517 * Error Risk: 68.6528%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 6290.992** (Blast Radius: 123.252 * Doc Risk: 51.0417%)
- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **Severity: 6190.621** (Blast Radius: 101.703 * Doc Risk: 60.8696%)
- `python_discovery-1.2.1/src/python_discovery/_specifier.py` -> **Severity: 5561.788** (Blast Radius: 77.865 * Doc Risk: 71.4286%)
- `python_discovery-1.2.1/src/python_discovery/_compat.py` -> **Severity: 4992.1** (Blast Radius: 49.921 * Doc Risk: 100.0%)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **Severity: 4658.344** (Blast Radius: 49.689 * Doc Risk: 93.75%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1521 call pairs -- scoped 32.6%, unique 0.0%, ambiguous 5.1%, external 62.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 1521 | 32.6% | 0.0% | 5.1% | 62.3% |

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
