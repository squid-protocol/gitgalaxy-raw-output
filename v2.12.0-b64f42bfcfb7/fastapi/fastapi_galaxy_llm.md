# ARCHITECTURAL_BRIEF: fastapi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tiangolo/fastapi.git` |
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
- **Scope:** 1185 analyzed artifact(s), 86322 LOC.
- **Load-bearing artifact:** `fastapi/__init__.py` -- 573 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `fastapi/routing.py` -- pulls in 34 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `fastapi/routing.py` at magnitude 2034.8 (structural weight, not risk).
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
| Total Artifacts | 2984 |
| Analyzed Artifacts (Scanned) | 1185 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1799 |
| Total LOC | 86322 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 39.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3282 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2071 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5419 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 33 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1117 | 84843 | 94.3% |
| MARKDOWN | 32 | 0 | 2.7% |
| YAML | 26 | 1405 | 2.2% |
| SHELL | 6 | 30 | 0.5% |
| JAVASCRIPT | 1 | 32 | 0.1% |
| CSS | 1 | 3 | 0.1% |
| HTML | 1 | 9 | 0.1% |
| PLAINTEXT | 1 | 0 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1185 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 31%, Data / Markup / Trivial 31%, Parameter Forwarders Files 17%, Generic / Templated Code Files 9%, Interface Declarations Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1152 | 97.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 33 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1799*

**Composition by Extension & Reason:**
- `.md`: 1523x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 180x Excluded (Explicitly Denied Extension: '.png')
- `.svg`: 51x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 4x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 96 exceeds 500 chars), 1x Excluded (Saturation: Line 53 exceeds 500 chars)
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.3 | 38.6 | 46.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.1 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 78.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.7 | 0.7 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 215 | 74 | 0 | `scripts/translate.py` |
| cleanup | 57 | 30 | 0 | `tests/test_ws_router.py` |
| guards | 5537 | 663 | 10 | `tests/test_path.py` |
| danger | 1242 | 215 | 1 | `fastapi/routing.py` |
| concurrency | 1552 | 465 | 3 | `tests/test_dependency_wrapped.py` |
| connectivity | 6445 | 917 | 11 | `tests/test_response_model_as_return_annotation.py` |
| io | 203 | 91 | 0 | `tests/test_dependency_yield_scope.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 67 | 19 | 0 | `scripts/contributors.py` |
| time | 45 | 23 | 0 | `scripts/people.py` |
| serialization | 3 | 2 | 0 | `docs_src/generate_clients/tutorial004.js` |
| regex | 30 | 6 | 0 | `scripts/doc_parsing_utils.py` |
| events | 218 | 46 | 0 | `fastapi/routing.py` |
| tests | 3892 | 506 | 10 | `tests/test_path.py` |
| docs | 1046 | 92 | 0 | `fastapi/applications.py` |
| debt | 281 | 80 | 0 | `scripts/translate.py` |
| mutation | 17602 | 920 | 28 | `fastapi/routing.py` |
| dead_code | 3386 | 735 | 6 | `tests/test_path.py` |
| credential | 24 | 8 | 0 | `tests/test_tutorial/test_security/test_tutorial004.py` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 1 | 1 | 0 | `scripts/translate.py` |
| ui | 20 | 9 | 0 | `docs_src/websockets_/tutorial002_an_py310.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_dependency_yield_scope.py` (Hits: 15)
- `tests/test_dependency_yield_scope_websockets.py` (Hits: 15)
- `scripts/docs.py` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`fastapi/__init__.py`) — 573 inbound connections
2. **applications.py** (`fastapi/applications.py`) — 549 inbound connections
3. **testclient.py** (`fastapi/testclient.py`) — 443 inbound connections
4. **param_functions.py** (`fastapi/param_functions.py`) — 301 inbound connections
5. **utils.py** (`tests/utils.py`) — 111 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **routing.py** (`fastapi/routing.py`) — 34 outbound dependencies
2. **utils.py** (`fastapi/dependencies/utils.py`) — 30 outbound dependencies
3. **applications.py** (`fastapi/applications.py`) — 27 outbound dependencies
4. **utils.py** (`fastapi/openapi/utils.py`) — 23 outbound dependencies
5. **encoders.py** (`fastapi/encoders.py`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `get_request_handler` **(Many-Argument Workhorses)** (@ `fastapi/routing.py`) -> Impact: **254.0** | LOC: 379
- `__init__` **(Many-Argument Workhorses)** (@ `fastapi/routing.py`) -> Impact: **191.3** | LOC: 165
- `analyze_param` **(Many-Argument Workhorses)** (@ `fastapi/dependencies/utils.py`) -> Impact: **126.9** | LOC: 167
- `get_openapi_path` **(Many-Argument Workhorses)** (@ `fastapi/openapi/utils.py`) -> Impact: **121.2** | LOC: 219
- `get_openapi` **(Many-Argument Workhorses)** (@ `fastapi/openapi/utils.py`) -> Impact: **117.0** | LOC: 93
- `jsonable_encoder` **(Many-Argument Workhorses)** (@ `fastapi/encoders.py`) -> Impact: **116.2** | LOC: 236
- `include_router` **(Many-Argument Workhorses)** (@ `fastapi/routing.py`) -> Impact: **113.1** | LOC: 252
- `__init__` **(Many-Argument Workhorses)** (@ `fastapi/applications.py`) -> Impact: **110.7** | LOC: 960
- `test_openapi` **(I/O & Config Routines)** (@ `tests/test_include_router_defaults_overrides.py`) -> Impact: **98.5** | LOC: 6866
- `app` **(Stateful Encapsulated Methods)** (@ `fastapi/routing.py`) -> Impact: **90.8** | LOC: 346

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests` | 206 | 10022.16 | 4.88% | 0.0% |
| `fastapi` | 23 | 3843.8 | 15.38% | 6.42% |
| `scripts` | 19 | 2863.88 | 38.59% | 9.17% |
| `fastapi/dependencies` | 3 | 1331.2 | 62.12% | 2.66% |
| `fastapi/openapi` | 5 | 883.32 | 19.55% | 1.64% |
| `docs_src/security` | 15 | 782.24 | 38.52% | 48.87% |
| `tests/test_request_params/test_body` | 6 | 603.0 | 7.86% | 0.0% |
| `docs_src/dependencies` | 32 | 600.96 | 20.66% | 50.69% |
| `tests/test_request_params/test_file` | 6 | 565.32 | 4.93% | 0.0% |
| `fastapi/_compat` | 3 | 509.62 | 44.48% | 8.83% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `docs_src/stream_data/tutorial001_py310.py` -> **99.9999%** Exposure
- `docs_src/app_testing/app_b_an_py310/test_main.py` -> **99.9905%** Exposure
- `docs_src/app_testing/app_b_py310/test_main.py` -> **99.9905%** Exposure
- `docs_src/dependency_testing/tutorial001_an_py310.py` -> **99.9447%** Exposure
- `docs_src/dependency_testing/tutorial001_py310.py` -> **99.9447%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `docs_src/security/tutorial004_an_py310.py` -> **100.0%** Exposure
- `docs_src/security/tutorial004_py310.py` -> **100.0%** Exposure
- `docs_src/security/tutorial005_an_py310.py` -> **100.0%** Exposure
- `docs_src/security/tutorial005_py310.py` -> **100.0%** Exposure
- `fastapi/dependencies/utils.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_path.py` -> **75** Orphaned Functions | **0** Duplicates
- `tests/test_response_model_as_return_annotation.py` -> **75** Orphaned Functions | **0** Duplicates
- `tests/test_dependency_wrapped.py` -> **30** Orphaned Functions | **12** Duplicates
- `tests/benchmarks/test_general_performance.py` -> **40** Orphaned Functions | **0** Duplicates
- `tests/test_dependency_contextmanager.py` -> **40** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `docs_src/security/tutorial003_py310.py` -> **99.7127%** Exposure
- `docs_src/security/tutorial003_an_py310.py` -> **99.5825%** Exposure
- `tests/test_tutorial/test_security/test_tutorial004.py` -> **99.257%** Exposure
- `tests/test_tutorial/test_security/test_tutorial005.py` -> **98.5886%** Exposure
- `docs_src/security/tutorial004_py310.py` -> **97.0502%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3296` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `fastapi/routing.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.071)
- **Top Global Matches:** file_cluster_5: 9.071, file_cluster_4: 10.28, file_cluster_12: 10.473
- **Magnitude:** 2034.8 | **LOC:** 4957 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **44** in-repo importer(s); it depends on **34**; blast radius 16.528; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Concurrency Surface (formerly Concurrency) (98.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 93.8596% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_request_handler` **(Many-Argument Workhorses)** (Impact: 254.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 191.3)
  * `include_router` **(Many-Argument Workhorses)** (Impact: 113.1)
  * `app` **(Stateful Encapsulated Methods)** (Impact: 90.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 81.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 157 instances
* *Concurrency (weighted view):* 193
* *State Mutation (weighted view):* 526
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 284`, `args: 65`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 212`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 43`, `concurrency: 63`, `import: 36`
* *Defense:* `safety: 46`, `doc: 237`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.528
  * `Choke Point (Betweenness):` 0.002999 | `Ripple Effect (Closeness):` 0.270415
  * `Imports (Out-Degree: 12):` annotated_doc, anyio, anyio.abc, collections.abc, contextlib, email.message, enum, fastapi...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `fastapi/dependencies/utils.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.362)
- **Top Global Matches:** file_cluster_4: 12.362, file_cluster_6: 12.783, file_cluster_5: 14.001
- **Magnitude:** 1162.32 | **LOC:** 1058 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **30**; blast radius 2.171; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (94.9%), Complexity Load (formerly Cognitive Load) (88.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.1014% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyze_param` **(Many-Argument Workhorses)** (Impact: 126.9)
  * `solve_dependencies` **(Many-Argument Workhorses)** (Impact: 89.1)
  * `get_dependant` **(Many-Argument Workhorses)** (Impact: 46.1)
  * `request_params_to_args` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `get_body_field` **(Many-Argument Workhorses)** (Impact: 30.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 164 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 522
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 194`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 68`, `state_mutation: 194`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 21`, `concurrency: 13`, `import: 32`
* *Defense:* `safety: 79`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.171
  * `Choke Point (Betweenness):` 0.001417 | `Ripple Effect (Closeness):` 0.185061
  * `Imports (Out-Degree: 12):` annotationlib, collections.abc, contextlib, copy, dataclasses, fastapi, fastapi._compat, fastapi.background...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `fastapi/openapi/utils.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 14.057)
- **Top Global Matches:** file_cluster_6: 14.057, file_cluster_8: 15.363, file_cluster_4: 19.779
- **Magnitude:** 700.02 | **LOC:** 607 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 5.099; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_openapi_path` **(Many-Argument Workhorses)** (Impact: 121.2)
  * `get_openapi` **(Many-Argument Workhorses)** (Impact: 117.0)
  * `_get_openapi_operation_parameters` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `get_openapi_operation_metadata` **(Generic / Templated Code)** (Impact: 17.1)
  * `get_fields_from_routes` **(Defensive Guards)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 85`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 129`, `planned_debt: 1`
* *Architecture:* `api: 8`, `import: 23`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.099
  * `Choke Point (Betweenness):` 0.00173 | `Ripple Effect (Closeness):` 0.254847
  * `Imports (Out-Degree: 16):` collections.abc, copy, fastapi, fastapi._compat, fastapi.datastructures, fastapi.dependencies.models, fastapi.dependencies.utils, fastapi.encoders...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/doc_parsing_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.709)
- **Top Global Matches:** file_cluster_5: 8.709, file_cluster_12: 9.755, file_cluster_9: 10.482
- **Magnitude:** 640.0 | **LOC:** 734 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 3.509; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.2%), Complexity Load (formerly Cognitive Load) (50.8%), Connectivity (formerly Api Exposure) (46.1%)
- **Documentation Coverage:** 32.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_translation` **(Many-Argument Workhorses)** (Impact: 29.8)
    * *Intent:* # All checks # -------------------------------------------------------------------------------------...
  * `extract_header_permalinks` **(Compute Cores)** (Impact: 23.7)
    * *Intent:* # Header permalinks # ------------------------------------------------------------------------------...
  * `replace_multiline_code_block` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `extract_multiline_code_blocks` **(Compute Cores)** (Impact: 21.8)
  * `replace_header_permalinks` **(Generic / Templated Code)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 69`, `args: 20`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 146`
* *Architecture:* `api: 21`, `import: 2`
* *Defense:* `safety: 12`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.509
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005528
  * `Imports (Out-Degree: 0):` re, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/docs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.844)
- **Top Global Matches:** file_cluster_4: 8.844, file_cluster_12: 10.436, file_cluster_5: 10.519
- **Magnitude:** 613.98 | **LOC:** 742 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.353; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Complexity Load (formerly Cognitive Load) (59.1%), Debt Markers (formerly Tech Debt) (43.7%)
- **Documentation Coverage:** 26.2712% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_permalinks_page` **(Compute Cores)** (Impact: 51.5)
    * *Intent:* """ Add or update header permalinks in specific page of En docs. """
  * `remove_unused_docs_src` **(I/O & Config Routines)** (Impact: 38.4)
    * *Intent:* """ Delete .py files in docs_src that are not included in any .md file under docs/. """
  * `generate_docs_src_versions_for_file` **(Compute Cores)** (Impact: 21.3)
  * `remove_header_permalinks` **(Compute Cores)** (Impact: 10.3)
  * `ensure_non_translated` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* """ Ensure there are no files in the non translatable pages. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 97`, `args: 31`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 4`, `state_mutation: 143`, `unreferenced_by_name: 12`
* *Architecture:* `io: 9`, `api: 30`, `concurrency: 1`, `import: 17`
* *Defense:* `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` html.parser, http.server, jinja2, json, logging, mkdocs.utils, multiprocessing, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fastapi/applications.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.277)
- **Top Global Matches:** file_cluster_5: 7.277, file_cluster_12: 8.377, file_cluster_0: 9.875
- **Magnitude:** 571.96 | **LOC:** 4750 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **549** in-repo importer(s); it depends on **27**; blast radius 64.933; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.0%), Guard Balance (formerly Safety Score) (55.5%), Connectivity (formerly Api Exposure) (47.4%)
- **Documentation Coverage:** 96.9697% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 110.7)
  * `setup` **(Generic / Templated Code)** (Impact: 19.7)
  * `get` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `put` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `post` **(Many-Argument Workhorses)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 129`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 42`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 33`, `concurrency: 6`, `import: 27`
* *Defense:* `safety: 2`, `doc: 261`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 64.933
  * `Choke Point (Betweenness):` 0.007799 | `Ripple Effect (Closeness):` 0.454434
  * `Imports (Out-Degree: 12):` annotated_doc, collections.abc, enum, fastapi, fastapi.datastructures, fastapi.exception_handlers, fastapi.exceptions, fastapi.logger...
  * `Imported By (In-Degree: 549):` (Excluded from Brief to save tokens)

### `tests/test_include_router_defaults_overrides.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.918)
- **Top Global Matches:** file_cluster_15: 5.918, file_cluster_2: 7.051, file_cluster_11: 7.945
- **Magnitude:** 497.84 | **LOC:** 7305 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Concurrency Surface (formerly Concurrency) (19.4%), Connectivity (formerly Api Exposure) (8.8%), Complexity Load (formerly Cognitive Load) (3.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_openapi` **(I/O & Config Routines)** (Impact: 98.5)
  * `test_paths_level5` **(Defensive Guards)** (Impact: 31.0)
  * `test_paths_level3` **(Defensive Guards)** (Impact: 17.2)
  * `dep0` **(Parameter Forwarders)** (Impact: 1.5)
  * `dep1` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 52
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 286`, `args: 27`, `func_start: 27`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 42`, `unreferenced_by_name: 15`
* *Architecture:* `api: 49`, `concurrency: 22`, `import: 6`
* *Defense:* `safety: 34`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` fastapi, fastapi.responses, fastapi.testclient, inline_snapshot, pytest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_dependency_wrapped.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.558)
- **Top Global Matches:** file_cluster_0: 8.558, file_cluster_15: 8.644, file_cluster_13: 8.837
- **Magnitude:** 366.42 | **LOC:** 450 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (53.1%), Complexity Load (formerly Cognitive Load) (50.0%), Connectivity (formerly Api Exposure) (14.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `noop_wrap_async` **(Compute Cores)** (Impact: 14.3)
  * `wrapper` **(Compute Cores)** (Impact: 9.1)
  * `gen_wrapper` **(Parameter Forwarders)** (Impact: 3.6)
  * `async_gen_wrapper` **(Parameter Forwarders)** (Impact: 3.6)
  * `wrapper` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 143
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 171`, `args: 56`, `func_start: 56`, `class_start: 13`
* *Risk/State:* `state_mutation: 25`, `duplicate_logic: 12`, `unreferenced_by_name: 30`
* *Architecture:* `io: 1`, `api: 84`, `concurrency: 98`, `import: 10`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` asyncio, collections.abc, fastapi, fastapi.concurrency, fastapi.testclient, functools, inspect, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/translate.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.073)
- **Top Global Matches:** file_cluster_5: 8.073, file_cluster_12: 8.655, file_cluster_0: 8.701
- **Magnitude:** 358.94 | **LOC:** 455 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.3%), Complexity Load (formerly Cognitive Load) (64.4%), Debt Markers (formerly Tech Debt) (38.1%)
- **Documentation Coverage:** 47.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_pr` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `translate_page` **(Many-Argument Workhorses)** (Impact: 30.3)
  * `translate_lang` **(Generic / Templated Code)** (Impact: 11.2)
  * `update_and_add` **(Generic / Templated Code)** (Impact: 9.1)
  * `commands_json` **(Compute Cores)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 77`, `args: 21`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 6`, `state_mutation: 74`, `unreferenced_by_name: 8`
* *Architecture:* `io: 1`, `api: 21`, `import: 15`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections.abc, doc_parsing_utils, functools, git, github, json, os, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fastapi/params.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.658)
- **Top Global Matches:** file_cluster_5: 7.658, file_cluster_7: 8.749, file_cluster_12: 9.446
- **Magnitude:** 340.56 | **LOC:** 755 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 5.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%), Connectivity (formerly Api Exposure) (49.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 75.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 73.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 15.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 15.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 47`, `args: 10`, `func_start: 10`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 36`, `duplicate_logic: 4`
* *Architecture:* `api: 11`, `import: 12`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.603
  * `Choke Point (Betweenness):` 0.000139 | `Ripple Effect (Closeness):` 0.256173
  * `Imports (Out-Degree: 4):` ._compat, .datastructures, collections.abc, dataclasses, enum, fastapi.exceptions, fastapi.openapi.models, pydantic...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `fastapi/_compat/v2.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.1)
- **Top Global Matches:** file_cluster_5: 6.1, file_cluster_7: 9.787, file_cluster_12: 9.967
- **Magnitude:** 320.36 | **LOC:** 481 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **20**; blast radius 32.434; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.4%), Complexity Load (formerly Cognitive Load) (66.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_schema_from_model_field` **(Many-Argument Workhorses)** (Impact: 26.0)
  * `get_flat_models_from_annotation` **(Defensive Guards)** (Impact: 12.8)
  * `serialize_sequence_value` **(Defensive Guards)** (Impact: 12.7)
  * `get_flat_models_from_field` **(Defensive Guards)** (Impact: 9.4)
  * `get_model_fields` **(Defensive Guards)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 139`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 57`, `planned_debt: 5`
* *Architecture:* `api: 29`, `import: 26`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 32.434
  * `Choke Point (Betweenness):` 0.000334 | `Ripple Effect (Closeness):` 0.190335
  * `Imports (Out-Degree: 6):` collections.abc, copy, dataclasses, enum, fastapi, fastapi._compat, fastapi.openapi.constants, fastapi.types...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/test_dependency_contextmanager.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.033)
- **Top Global Matches:** file_cluster_12: 8.033, file_cluster_15: 9.404, file_cluster_13: 9.435
- **Magnitude:** 314.44 | **LOC:** 400 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (26.4%), Connectivity (formerly Api Exposure) (14.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_sync_context_b_bg` **(Parameter Forwarders)** (Impact: 2.2)
  * `get_context_b_bg` **(Parameter Forwarders)** (Impact: 2.0)
  * `asyncgen_state_try` **(Defensive Guards)** (Impact: 1.9)
  * `generator_state_try` **(Defensive Guards)** (Impact: 1.9)
  * `middleware` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Concurrency (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 175`, `args: 50`, `func_start: 50`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 50`, `unreferenced_by_name: 40`
* *Architecture:* `api: 71`, `concurrency: 28`, `import: 5`
* *Defense:* `safety: 93`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` fastapi, fastapi.responses, fastapi.testclient, json, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_path.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.121)
- **Top Global Matches:** file_cluster_15: 7.121, file_cluster_2: 7.395, file_cluster_11: 7.536
- **Magnitude:** 275.06 | **LOC:** 781 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (28.6%), Connectivity (formerly Api Exposure) (13.0%), Complexity Load (formerly Cognitive Load) (8.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_path_param_ge_2` **(Defensive Guards)** (Impact: 2.7)
  * `test_path_param_le_42` **(Defensive Guards)** (Impact: 2.7)
  * `test_path_param_le_ge_4` **(Defensive Guards)** (Impact: 2.7)
  * `test_path_param_le_int_42` **(Defensive Guards)** (Impact: 2.7)
  * `test_path_param_ge_int_2` **(Defensive Guards)** (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 273`, `args: 75`, `func_start: 75`
* *Risk/State:* `state_mutation: 76`, `unreferenced_by_name: 75`
* *Architecture:* `api: 75`, `import: 2`
* *Defense:* `safety: 149`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .main, fastapi.testclient
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/people.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.507)
- **Top Global Matches:** file_cluster_5: 10.507, file_cluster_4: 10.924, file_cluster_12: 11.811
- **Magnitude:** 267.28 | **LOC:** 484 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.353; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.8%), Complexity Load (formerly Cognitive Load) (57.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_discussions_experts` **(Compute Cores)** (Impact: 26.0)
  * `get_top_users` **(Generic / Templated Code)** (Impact: 10.0)
  * `get_graphql_response` **(Many-Argument Workhorses)** (Impact: 8.1)
  * `__enter__` **(Compute Cores)** (Impact: 7.0)
  * `get_users_to_write` **(Generic / Templated Code)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 63`, `args: 13`, `func_start: 12`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 6`, `state_mutation: 80`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 23`, `import: 15`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, collections.abc, datetime, github, httpx, logging, math, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_response_model_as_return_annotation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.642)
- **Top Global Matches:** file_cluster_0: 6.642, file_cluster_11: 7.417, file_cluster_13: 7.599
- **Magnitude:** 263.98 | **LOC:** 1122 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (42.0%), Connectivity (formerly Api Exposure) (13.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_openapi_schema` **(I/O & Config Routines)** (Impact: 7.5)
  * `test_response_model_none_annotation_return_submodel_with_extra_data` **(Defensive Guards)** (Impact: 1.5)
  * `test_invalid_response_model_field` **(Annotated & Test Methods)** (Impact: 1.5)
  * `test_response_model_none_annotation_return_dict_with_extra_data` **(Defensive Guards)** (Impact: 1.4)
  * `test_response_model_list_of_model_no_annotation` **(Defensive Guards)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 223`, `args: 75`, `func_start: 75`, `class_start: 4`
* *Risk/State:* `state_mutation: 34`, `unreferenced_by_name: 75`
* *Architecture:* `api: 116`, `import: 7`
* *Defense:* `safety: 73`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` fastapi, fastapi.exceptions, fastapi.responses, fastapi.testclient, inline_snapshot, pydantic, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_generate_unique_id_function.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.326)
- **Top Global Matches:** file_cluster_15: 6.326, file_cluster_2: 7.409, file_cluster_13: 7.473
- **Magnitude:** 251.08 | **LOC:** 1700 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.9%), Connectivity (formerly Api Exposure) (10.7%), Complexity Load (formerly Cognitive Load) (3.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_callback_override_generate_unique_id` **(I/O & Config Routines)** (Impact: 15.7)
  * `test_subrouter_top_level_include_overrides_generate_unique_id` **(I/O & Config Routines)** (Impact: 15.2)
  * `test_app_path_operation_overrides_generate_unique_id` **(I/O & Config Routines)** (Impact: 11.8)
  * `test_router_path_operation_overrides_generate_unique_id` **(I/O & Config Routines)** (Impact: 11.6)
  * `test_top_level_generate_unique_id` **(I/O & Config Routines)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 246`, `args: 31`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `state_mutation: 32`, `duplicate_logic: 13`, `unreferenced_by_name: 12`
* *Architecture:* `api: 52`, `import: 6`
* *Defense:* `safety: 14`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` fastapi, fastapi.routing, fastapi.testclient, inline_snapshot, pydantic, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fastapi/param_functions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.848)
- **Top Global Matches:** file_cluster_12: 7.848, file_cluster_7: 8.382, file_cluster_5: 8.585
- **Magnitude:** 235.88 | **LOC:** 2461 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **301** in-repo importer(s); it depends on **9**; blast radius 32.079; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.2%), Connectivity (formerly Api Exposure) (37.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Body` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `Path` **(Many-Argument Workhorses)** (Impact: 27.5)
  * `Query` **(Many-Argument Workhorses)** (Impact: 27.5)
  * `Header` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `Form` **(Many-Argument Workhorses)** (Impact: 26.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 36`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 54`
* *Architecture:* `api: 9`, `import: 9`
* *Defense:* `doc: 217`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.079
  * `Choke Point (Betweenness):` 0.00075 | `Ripple Effect (Closeness):` 0.329978
  * `Imports (Out-Degree: 4):` annotated_doc, collections.abc, fastapi, fastapi._compat, fastapi.datastructures, fastapi.openapi.models, pydantic, typing...
  * `Imported By (In-Degree: 301):` (Excluded from Brief to save tokens)

### `tests/test_router_events.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.509)
- **Top Global Matches:** file_cluster_0: 6.509, file_cluster_13: 9.693, file_cluster_10: 11.173
- **Magnitude:** 226.76 | **LOC:** 379 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (27.0%), Connectivity (formerly Api Exposure) (13.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.8%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_router_events` **(Defensive Guards)** (Impact: 4.4)
  * `test_router_nested_lifespan_state` **(Defensive Guards)** (Impact: 4.3)
  * `test_startup_shutdown_handlers_as_parameters` **(Defensive Guards)** (Impact: 4.3)
    * *Intent:* """Test that startup/shutdown handlers passed as parameters to FastAPI are called correctly."""
  * `test_router_sync_generator_lifespan` **(Defensive Guards)** (Impact: 2.7)
    * *Intent:* """Test that a sync generator lifespan works via _wrap_gen_lifespan_context."""
  * `test_app_lifespan_state` **(Defensive Guards)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Concurrency (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 180`, `args: 44`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `state_mutation: 52`, `duplicate_logic: 22`, `unreferenced_by_name: 10`
* *Architecture:* `api: 52`, `concurrency: 13`, `import: 7`
* *Defense:* `safety: 96`, `doc: 4`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` collections.abc, contextlib, fastapi, fastapi.testclient, pydantic, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_sse.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.848)
- **Top Global Matches:** file_cluster_11: 7.848, file_cluster_13: 8.101, file_cluster_0: 8.154
- **Magnitude:** 221.3 | **LOC:** 319 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Guard Balance (formerly Safety Score) (33.0%), Complexity Load (formerly Cognitive Load) (30.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.7%)
- **Documentation Coverage:** 84.8485% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_async_generator_with_model` **(Defensive Guards)** (Impact: 9.4)
  * `test_sync_generator_with_model` **(Defensive Guards)** (Impact: 4.7)
  * `test_async_generator_no_annotation` **(Defensive Guards)** (Impact: 4.7)
  * `test_sync_generator_no_annotation` **(Defensive Guards)** (Impact: 4.7)
  * `test_post_method_sse` **(Defensive Guards)** (Impact: 4.7)
    * *Intent:* """SSE should work with POST (needed for MCP compatibility)."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 125`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 32`
* *Architecture:* `api: 46`, `concurrency: 15`, `import: 10`
* *Defense:* `safety: 59`, `doc: 5`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` asyncio, collections.abc, fastapi, fastapi.responses, fastapi.routing, fastapi.sse, fastapi.testclient, pydantic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/mkdocs_hooks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.525)
- **Top Global Matches:** file_cluster_5: 6.525, file_cluster_12: 8.763, file_cluster_7: 10.014
- **Magnitude:** 210.7 | **LOC:** 183 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.353; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.7%), Debt Markers (formerly Tech Debt) (72.1%), Complexity Load (formerly Cognitive Load) (70.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_page_markdown` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `resolve_files` **(Defensive Guards)** (Impact: 16.8)
  * `generate_renamed_section_items` **(Defensive Guards)** (Impact: 13.3)
  * `on_config` **(Generic / Templated Code)** (Impact: 9.1)
  * `on_files` **(Generic / Templated Code)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 42`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 41`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 12`, `import: 8`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` functools, material, mkdocs.config.defaults, mkdocs.structure.files, mkdocs.structure.nav, mkdocs.structure.pages, pathlib, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_ws_router.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.457)
- **Top Global Matches:** file_cluster_7: 8.457, file_cluster_12: 8.57, file_cluster_5: 8.839
- **Magnitude:** 206.44 | **LOC:** 272 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (63.0%), Complexity Load (formerly Cognitive Load) (36.1%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 84.8485% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrapped_app` **(Parameter Forwarders)** (Impact: 4.5)
  * `make_app` **(Parameter Forwarders)** (Impact: 3.8)
  * `websocket_middleware` **(Parameter Forwarders)** (Impact: 3.8)
    * *Intent:* """ Helper to create a Starlette pure websocket middleware """
  * `middleware_constructor` **(Annotated & Test Methods)** (Impact: 3.5)
  * `routerindexparams` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 67
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 139`, `args: 34`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 32`, `unreferenced_by_name: 22`
* *Architecture:* `api: 41`, `concurrency: 47`, `import: 5`
* *Defense:* `safety: 18`, `doc: 5`, `test: 17`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` fastapi, fastapi.middleware, fastapi.testclient, functools, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/notify_translations.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.207)
- **Top Global Matches:** file_cluster_6: 10.207, file_cluster_4: 11.517, file_cluster_5: 15.942
- **Magnitude:** 205.26 | **LOC:** 433 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.353; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (72.3%), Guard Balance (formerly Safety Score) (62.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 44.1)
  * `get_graphql_response` **(Many-Argument Workhorses)** (Impact: 10.9)
  * `get_graphql_translation_discussion_comments` **(Generic / Templated Code)** (Impact: 6.1)
  * `get_graphql_translation_discussion_comments_edges` **(Generic / Templated Code)** (Impact: 2.5)
  * `create_comment` **(Generic / Templated Code)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 55`, `args: 7`, `func_start: 7`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 50`
* *Architecture:* `io: 5`, `api: 31`, `import: 10`
* *Defense:* `safety: 24`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` github, httpx, logging, pathlib, pydantic, pydantic_settings, random, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/benchmarks/test_general_performance.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.324)
- **Top Global Matches:** file_cluster_5: 7.324, file_cluster_12: 9.115, file_cluster_0: 9.966
- **Magnitude:** 190.66 | **LOC:** 400 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Guard Balance (formerly Safety Score) (36.4%), Connectivity (formerly Api Exposure) (13.6%), Complexity Load (formerly Cognitive Load) (8.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_bench_post_json` **(Stateful Encapsulated Methods)** (Impact: 2.8)
  * `_bench_get` **(Encapsulated Accessors)** (Impact: 2.5)
  * `test_sync_receiving_validated_pydantic_model` **(Defensive Guards)** (Impact: 2.2)
  * `test_sync_receiving_large_payload` **(Defensive Guards)** (Impact: 2.2)
  * `test_async_receiving_large_payload` **(Defensive Guards)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 153`, `args: 48`, `func_start: 48`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 5`, `unreferenced_by_name: 40`
* *Architecture:* `api: 69`, `concurrency: 30`, `import: 8`
* *Defense:* `safety: 47`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` collections.abc, fastapi, fastapi.testclient, json, pydantic, pytest, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fastapi/encoders.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.93)
- **Top Global Matches:** file_cluster_8: 13.93, file_cluster_6: 14.724, file_cluster_4: 21.125
- **Magnitude:** 180.94 | **LOC:** 348 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **21**; blast radius 8.356; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (74.7%), Connectivity (formerly Api Exposure) (40.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.7%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jsonable_encoder` **(Many-Argument Workhorses)** (Impact: 116.2)
  * `decimal_encoder` **(Type Conversions)** (Impact: 6.8)
    * *Intent:* # Adapted from Pydantic v1 # TODO: pv2 should this return strings instead? """ Encodes a Decimal as ...
  * `generate_encoders_by_class_tuples` **(Generic / Templated Code)** (Impact: 3.3)
  * `isoformat` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* # Taken from Pydantic v1 as is
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 72`, `args: 8`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 18`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 21`
* *Defense:* `safety: 19`, `doc: 11`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.356
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.188244
  * `Imports (Out-Degree: 4):` ._compat, annotated_doc, collections, collections.abc, dataclasses, datetime, decimal, enum...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `fastapi/security/http.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.866)
- **Top Global Matches:** file_cluster_0: 7.866, file_cluster_9: 8.394, file_cluster_15: 8.677
- **Magnitude:** 178.74 | **LOC:** 418 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **11**; blast radius 1.908; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Compute Cores)** (Impact: 16.3)
  * `__call__` **(Compute Cores)** (Impact: 16.3)
  * `__call__` **(Defensive Guards)** (Impact: 11.3)
  * `__call__` **(Generic / Templated Code)** (Impact: 10.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 58`, `args: 11`, `func_start: 11`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 4`, `import: 12`
* *Defense:* `safety: 4`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.908
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.026868
  * `Imports (Out-Degree: 4):` annotated_doc, base64, binascii, fastapi.exceptions, fastapi.openapi.models, fastapi.security.base, fastapi.security.utils, pydantic...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `docs_src/dataclasses_/tutorial002_py310.py` (PYTHON) | Magnitude: 7.76 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, core_var_decl: 4, api: 3
- `docs_src/generate_clients/tutorial001_py310.py` (PYTHON) | Magnitude: 12.04 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, api: 6, safety: 3
- `tests/test_dependency_wrapped.py` (PYTHON) | Magnitude: 366.42 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 171, indent_spaces: 154, concurrency: 98, api: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/test_tutorial/test_python_types/test_tutorial004.py` (PYTHON) | Magnitude: 2.16 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, safety: 1
- `tests/test_tutorial/test_python_types/test_tutorial010.py` (PYTHON) | Magnitude: 2.16 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, safety: 1
- `tests/test_tutorial/test_python_types/test_tutorial013.py` (PYTHON) | Magnitude: 2.16 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, safety: 1
- `tests/test_custom_route_class.py` (PYTHON) | Magnitude: 40.82 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 31, api: 12, state_mutation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/test_union_body_discriminator.py` (PYTHON) | Magnitude: 27.44 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 47, safety: 9, import: 7
- `fastapi/sse.py` (PYTHON) | Magnitude: 68.84 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 21, branch: 15, doc: 14
- `.github/workflows/pre-commit.yml` (YAML) | Magnitude: 16.96 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 74, branch: 10, args: 9, structural_boundaries: 8
- `docs_src/dependencies/tutorial008c_py310.py` (PYTHON) | Magnitude: 12.3 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, api: 4, panics_and_aborts: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `docs_src/cookie_param_models/tutorial001_an_py310.py` (PYTHON) | Magnitude: 6.72 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 4, api: 3, import: 3
- `docs_src/handling_errors/tutorial005_py310.py` (PYTHON) | Magnitude: 10.86 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 7, import: 5, api: 4
- `tests/test_tutorial/test_custom_docs_ui/test_tutorial001.py` (PYTHON) | Magnitude: 17.6 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 20, safety: 9, test: 7
- `tests/test_tutorial/test_custom_docs_ui/test_tutorial002.py` (PYTHON) | Magnitude: 17.6 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 20, safety: 9, test: 7
- `docs_src/request_form_models/tutorial002_py310.py` (PYTHON) | Magnitude: 7.7 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, api: 3, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `docs_src/app_testing/app_a_py310/test_main.py` (PYTHON) | Magnitude: 4.34 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 3, safety: 2, state_mutation: 2
- `docs_src/body/tutorial001_py310.py` (PYTHON) | Magnitude: 6.72 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 5, api: 3, core_var_decl: 3
- `docs_src/request_form_models/tutorial002_an_py310.py` (PYTHON) | Magnitude: 7.72 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 4, api: 3, import: 3
- `docs_src/app_testing/app_b_an_py310/test_main.py` (PYTHON) | Magnitude: 22.42 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 22, core_var_decl: 13, design_snake_case: 13
- `docs_src/app_testing/app_b_py310/test_main.py` (PYTHON) | Magnitude: 22.42 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 22, core_var_decl: 13, design_snake_case: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `fastapi/__init__.py` (PYTHON) | Magnitude: 16.42 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 60, import: 20, dependency_injection: 2, io: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/test_tutorial/test_advanced_middleware/test_tutorial002.py` (PYTHON) | Magnitude: 8.74 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, state_mutation: 6, core_var_decl: 6
- `tests/test_tutorial/test_middleware/test_tutorial001.py` (PYTHON) | Magnitude: 8.22 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 12, safety: 4, state_mutation: 3
- `tests/test_tutorial/test_metadata/test_tutorial003.py` (PYTHON) | Magnitude: 18.78 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 19, safety: 8, state_mutation: 6
- `tests/test_tutorial/test_path_params/test_tutorial005.py` (PYTHON) | Magnitude: 25.52 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 34, safety: 10, state_mutation: 6
- `tests/test_tutorial/test_path_params_numeric_validations/test_tutorial005.py` (PYTHON) | Magnitude: 38.54 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 177, structural_boundaries: 44, test: 13, safety: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/test_stringified_annotation_dependency.py` (PYTHON) | Magnitude: 43.92 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 32, api: 9, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `docs_src/extra_models/tutorial002_py310.py` (PYTHON) | Magnitude: 23.28 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 13, api: 8, core_var_decl: 6
- `tests/test_ws_router.py` (PYTHON) | Magnitude: 206.44 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 139, indent_spaces: 131, concurrency: 47, api: 41

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/test.yml` -> Churn: **82.7%** | Cog Load: 16.7637% | Debt: 99.3054%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `fastapi/routing.py` -> **Sebastián Ramírez** (83.3% isolated ownership) | Magnitude: 2034.8
- `scripts/docs.py` -> **Sebastián Ramírez** (100.0% isolated ownership) | Magnitude: 613.98
- `scripts/translate.py` -> **Motov Yurii** (100.0% isolated ownership) | Magnitude: 358.94
- `fastapi/params.py` -> **Sofie Van Landeghem** (100.0% isolated ownership) | Magnitude: 340.56
- `tests/test_response_model_as_return_annotation.py` -> **Sebastián Ramírez** (100.0% isolated ownership) | Magnitude: 263.98

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `fastapi/applications.py` -> **Severity: 0.304** (Bridge: 0.0078 * Flux: 39.0154%)
- `fastapi/routing.py` -> **Severity: 0.299** (Bridge: 0.003 * Flux: 99.7525%)
- `fastapi/openapi/utils.py` -> **Severity: 0.173** (Bridge: 0.0017 * Flux: 100.0%)
- `fastapi/dependencies/utils.py` -> **Severity: 0.142** (Bridge: 0.0014 * Flux: 100.0%)
- `fastapi/__init__.py` -> **Severity: 0.079** (Bridge: 0.0047 * Flux: 16.7982%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `fastapi/applications.py` -> **Severity: 25.222** (Embedded: 0.4544 * Error Risk: 55.501%)
- `fastapi/__init__.py` -> **Severity: 24.239** (Embedded: 0.4793 * Error Risk: 50.5714%)
- `fastapi/openapi/utils.py` -> **Severity: 21.302** (Embedded: 0.2548 * Error Risk: 83.5861%)
- `fastapi/datastructures.py` -> **Severity: 21.182** (Embedded: 0.2648 * Error Risk: 80.0%)
- `fastapi/exceptions.py` -> **Severity: 20.23** (Embedded: 0.2868 * Error Risk: 70.5405%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `fastapi/applications.py` -> **Severity: 6296.534** (Blast Radius: 64.933 * Doc Risk: 96.9697%)
- `fastapi/exceptions.py` -> **Severity: 3498.7** (Blast Radius: 34.987 * Doc Risk: 100.0%)
- `fastapi/_compat/v2.py` -> **Severity: 3243.4** (Blast Radius: 32.434 * Doc Risk: 100.0%)
- `fastapi/param_functions.py` -> **Severity: 3207.9** (Blast Radius: 32.079 * Doc Risk: 100.0%)
- `fastapi/_compat/shared.py` -> **Severity: 1947.3** (Blast Radius: 19.473 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 136 literal sites + 2 sites through wrappers = 138
- **`panics_and_aborts`:** 237 literal sites + 1 sites through wrappers = 238

- `fake_save_user` (function, debug_prints, primitive): 1 call sites in 1 files -- `docs_src/extra_models/tutorial001_py310.py`
- `fake_save_user` (function, debug_prints, primitive): 1 call sites in 1 files -- `docs_src/extra_models/tutorial002_py310.py`
- `raise_value_error` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `tests/test_exception_handlers.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 11668 call pairs -- scoped 28.9%, unique 0.0%, ambiguous 17.8%, external 53.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 11651 | 29.0% | 0.0% | 17.8% | 53.2% |
| javascript | 9 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 8 | 0.0% | 0.0% | 0.0% | 100.0% |

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
