# ARCHITECTURAL_BRIEF: scikit-learn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/scikit-learn/scikit-learn.git` |
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
- **Scope:** 1169 analyzed artifact(s), 249700 LOC.
- **Load-bearing artifact:** `sklearn/datasets/__init__.py` -- 312 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `sklearn/model_selection/tests/test_search.py` -- pulls in 44 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `sklearn/utils/estimator_checks.py` at magnitude 4183.24 (structural weight, not risk).
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
| Total Artifacts | 1788 |
| Analyzed Artifacts (Scanned) | 1169 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 619 |
| Total LOC | 249700 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 65.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2821 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0608 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.5837 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 34 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1022 | 244959 | 87.4% |
| PLAINTEXT | 47 | 0 | 4.0% |
| YAML | 29 | 1586 | 2.5% |
| SHELL | 22 | 810 | 1.9% |
| MARKDOWN | 9 | 0 | 0.8% |
| CPP | 8 | 299 | 0.7% |
| CSS | 7 | 884 | 0.6% |
| JAVASCRIPT | 6 | 179 | 0.5% |
| MAKEFILE | 4 | 127 | 0.3% |
| JSON | 4 | 43 | 0.3% |
| XML | 4 | 8 | 0.3% |
| CSV | 4 | 372 | 0.3% |
| HTML | 2 | 307 | 0.2% |
| BATCH | 1 | 126 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1169 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 22%, Many-Argument Workhorses Files 18%, Data / Markup / Trivial 17%, Large Core Modules (3) 14%, Large Core Modules (2) 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1110 | 95.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 56 | 4.8% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 619*

**Composition by Extension & Reason:**
- `.rst`: 206x Excluded (Unsupported Extension: '.rst')
- `.png`: 96x Excluded (Explicitly Denied Extension: '.png')
- `.gz`: 82x Excluded (Explicitly Denied Extension: '.gz')
- `no_extension`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1102 LOC), 1x Excluded (Machine-Generated Source Code Signature: 184 LOC)
- `.tp`: 20x Excluded (Unsupported Extension: '.tp'), 4x Unsupported Format (.tp)
- `.build`: 20x Excluded (Unsupported Extension: '.build'), 1x Unsupported Format (.build)
- `.yml`: 3x Excluded (Machine-Generated Source Code Signature: 25 LOC), 2x Excluded (Machine-Generated Source Code Signature: 31 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 13x Excluded (Unsupported Extension: '.lock')
- `.txt`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 47 LOC), 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.template`: 7x Excluded (Unsupported Extension: '.template')
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.cpp`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 28.9 | 30.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.6 | 54.8 | 61.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.6 | 11.9 | 6.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 94.9 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.6 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.3 | 40.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2515 | 436 | 6 | `sklearn/utils/_test_common/instance_generator.py` |
| cleanup | 40 | 23 | 0 | `doc/Makefile` |
| guards | 12342 | 571 | 32 | `sklearn/utils/estimator_checks.py` |
| danger | 3167 | 470 | 8 | `sklearn/utils/estimator_checks.py` |
| concurrency | 360 | 81 | 0 | `sklearn/utils/estimator_checks.py` |
| connectivity | 10181 | 756 | 23 | `sklearn/utils/tests/test_estimator_checks.py` |
| io | 870 | 140 | 1 | `doc/templates/index.html` |
| crypto | 4 | 4 | 0 | `examples/applications/plot_out_of_core_classification.py` |
| ipc | 31 | 19 | 0 | `build_tools/check-meson-openmp-dependencies.py` |
| time | 157 | 44 | 0 | `examples/applications/plot_out_of_core_classification.py` |
| serialization | 54 | 27 | 0 | `sklearn/tests/test_base.py` |
| regex | 162 | 55 | 0 | `build_tools/circle/build_doc.sh` |
| events | 117 | 31 | 0 | `sklearn/decomposition/_dict_learning.py` |
| tests | 12134 | 272 | 32 | `sklearn/metrics/tests/test_classification.py` |
| docs | 5682 | 899 | 14 | `sklearn/gaussian_process/kernels.py` |
| debt | 2700 | 504 | 7 | `sklearn/linear_model/tests/test_logistic.py` |
| mutation | 145245 | 965 | 318 | `sklearn/utils/estimator_checks.py` |
| dead_code | 5063 | 315 | 14 | `sklearn/metrics/tests/test_classification.py` |
| credential | 3 | 2 | 0 | `build_tools/github/upload_anaconda.sh` |
| threat | 2 | 2 | 0 | `sklearn/datasets/tests/test_svmlight_format.py` |
| ml_ai | 7628 | 877 | 15 | `sklearn/linear_model/_ridge.py` |
| ui | 115 | 12 | 0 | `doc/templates/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/templates/index.html` (Hits: 198)
- `build_tools/circle/build_doc.sh` (Hits: 115)
- `maint_tools/whats_missing.sh` (Hits: 51)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`sklearn/datasets/__init__.py`) — 312 inbound connections
2. **validation.py** (`sklearn/utils/validation.py`) — 234 inbound connections
3. **base.py** (`sklearn/base.py`) — 227 inbound connections
4. **__init__.py** (`sklearn/utils/__init__.py`) — 217 inbound connections
5. **__init__.py** (`sklearn/model_selection/__init__.py`) — 209 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_search.py** (`sklearn/model_selection/tests/test_search.py`) — 44 outbound dependencies
2. **instance_generator.py** (`sklearn/utils/_test_common/instance_generator.py`) — 42 outbound dependencies
3. **test_validation.py** (`sklearn/model_selection/tests/test_validation.py`) — 38 outbound dependencies
4. **estimator_checks.py** (`sklearn/utils/estimator_checks.py`) — 38 outbound dependencies
5. **_testing.py** (`sklearn/utils/_testing.py`) — 37 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `from_estimator` **(Many-Argument Workhorses)** (@ `sklearn/inspection/_plot/partial_dependence.py`) -> Impact: **429.8** | LOC: 540
- `_lars_path_solver` **(Many-Argument Workhorses)** (@ `sklearn/linear_model/_least_angle.py`) -> Impact: **417.1** | LOC: 503
- `check_array` **(Many-Argument Workhorses)** (@ `sklearn/utils/validation.py`) -> Impact: **401.1** | LOC: 421
- `_logistic_regression_path` **(Many-Argument Workhorses)** (@ `sklearn/linear_model/_logistic.py`) -> Impact: **311.7** | LOC: 460
- `_ridge_regression` **(Many-Argument Workhorses)** (@ `sklearn/linear_model/_ridge.py`) -> Impact: **236.4** | LOC: 230
- `fit` **(Many-Argument Workhorses)** (@ `sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py`) -> Impact: **231.8** | LOC: 563
- `fit` **(Many-Argument Workhorses)** (@ `sklearn/linear_model/_logistic.py`) -> Impact: **231.4** | LOC: 415
  * *Intent:* """Fit the model according to the given training data. Parameters ---------- X : {array-like, sparse matrix} of shape (n_samples, n_features) Training...
- `partial_dependence` **(Many-Argument Workhorses)** (@ `sklearn/inspection/_partial_dependence.py`) -> Impact: **226.0** | LOC: 409
- `plot` **(Many-Argument Workhorses)** (@ `sklearn/inspection/_plot/partial_dependence.py`) -> Impact: **222.3** | LOC: 358
- `sparse_enet_coordinate_descent` **(Many-Argument Workhorses)** (@ `sklearn/linear_model/_cd_fast.pyx`) -> Impact: **213.5** | LOC: 350

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `sklearn/utils` | 62 | 17458.28 | 33.49% | 14.76% |
| `sklearn/linear_model` | 18 | 12353.26 | 49.45% | 12.37% |
| `sklearn/linear_model/tests` | 19 | 9552.54 | 30.17% | 0.0% |
| `sklearn/tests` | 27 | 8756.18 | 22.69% | 0.0% |
| `sklearn/utils/tests` | 44 | 8560.94 | 39.7% | 0.0% |
| `sklearn/metrics/tests` | 9 | 7635.86 | 27.57% | 0.0% |
| `sklearn` | 19 | 6828.56 | 40.67% | 28.17% |
| `sklearn/preprocessing/tests` | 9 | 5715.98 | 21.68% | 0.0% |
| `sklearn/cluster` | 20 | 5534.94 | 38.47% | 3.31% |
| `sklearn/preprocessing` | 10 | 5369.04 | 41.07% | 7.64% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `asv_benchmarks/benchmarks/decomposition.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/ensemble.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/linear_model.py` -> **100.0%** Exposure
- `sklearn/_loss/_loss.pxd` -> **100.0%** Exposure
- `sklearn/externals/_packaging/_structures.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `asv_benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/linear_model.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/model_selection.py` -> **100.0%** Exposure
- `benchmarks/bench_feature_expansions.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sklearn/metrics/tests/test_classification.py` -> **116** Orphaned Functions | **0** Duplicates
- `sklearn/preprocessing/tests/test_data.py` -> **104** Orphaned Functions | **0** Duplicates
- `sklearn/utils/tests/test_validation.py` -> **98** Orphaned Functions | **2** Duplicates
- `sklearn/compose/tests/test_column_transformer.py` -> **89** Orphaned Functions | **6** Duplicates
- `sklearn/preprocessing/tests/test_encoders.py` -> **95** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `build_tools/github/upload_anaconda.sh` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8203` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `sklearn/utils/estimator_checks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.356)
- **Top Global Matches:** file_cluster_4: 5.356, file_cluster_15: 9.59, file_cluster_16: 9.838
- **Magnitude:** 4183.24 | **LOC:** 5485 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **38**; blast radius 0.619; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.8%), Connectivity (formerly Api Exposure) (68.6%), Guard Balance (formerly Safety Score) (67.7%)
- **Documentation Coverage:** 79.402% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_array_api_input` **(Many-Argument Workhorses)** (Impact: 94.2)
  * `check_param_validation` **(Many-Argument Workhorses)** (Impact: 64.5)
    * *Intent:* # Check that an informative error is raised when the value of a constructor # parameter does not hav...
  * `check_classifiers_train` **(Many-Argument Workhorses)** (Impact: 60.5)
  * `check_dataframe_column_names_consistency` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `_check_transformer` **(Many-Argument Workhorses)** (Impact: 51.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 597 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 700`, `structural_boundaries: 654`, `args: 150`, `func_start: 146`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 2`, `state_mutation: 916`, `planned_debt: 9`, `fragile_debt: 1`
* *Architecture:* `api: 115`, `import: 44`
* *Defense:* `safety: 368`, `doc: 43`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.619
  * `Choke Point (Betweenness):` 0.001185 | `Ripple Effect (Closeness):` 0.014705
  * `Imports (Out-Degree: 27):` __future__, contextlib, copy, functools, inspect, joblib, numbers, numpy...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/tests/test_ridge.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.179)
- **Top Global Matches:** file_cluster_15: 7.179, file_cluster_16: 7.859, file_cluster_11: 8.652
- **Magnitude:** 2130.7 | **LOC:** 2631 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.7%), Complexity Load (formerly Cognitive Load) (26.7%), Connectivity (formerly Api Exposure) (9.8%)
- **Documentation Coverage:** 78.6982% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_ridge_sample_weight_consistency` **(Many-Argument Workhorses)** (Impact: 51.2)
  * `test_regularization_limits_ridge_classifier_gcv` **(Many-Argument Workhorses)** (Impact: 33.9)
  * `test_ridge_regression_sample_weights` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `test_ridge_gcv_sample_weights` **(Many-Argument Workhorses)** (Impact: 29.6)
  * `test_regularization_limits_ridge_gcv` **(Many-Argument Workhorses)** (Impact: 25.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 332 instances
* *State Mutation (weighted view):* 1244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 275`, `args: 90`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 580`, `planned_debt: 4`, `fragile_debt: 7`, `unreferenced_by_name: 71`
* *Architecture:* `api: 79`, `import: 20`
* *Defense:* `safety: 106`, `doc: 28`, `test: 253`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` itertools, numpy, pytest, scipy, sklearn, sklearn.base, sklearn.datasets, sklearn.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/utils/validation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.463)
- **Top Global Matches:** file_cluster_6: 5.463, file_cluster_4: 10.706, file_cluster_8: 14.54
- **Magnitude:** 2118.86 | **LOC:** 2942 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 12.5%
- **Blast Radius:** changing it is visible to **234** in-repo importer(s); it depends on **20**; blast radius 43.141; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.8%), Guard Balance (formerly Safety Score) (67.1%)
- **Documentation Coverage:** 34.6535% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_array` **(Many-Argument Workhorses)** (Impact: 401.1)
  * `validate_data` **(Many-Argument Workhorses)** (Impact: 80.2)
  * `check_scalar` **(Many-Argument Workhorses)** (Impact: 75.1)
  * `_ensure_sparse_format` **(Many-Argument Workhorses)** (Impact: 73.0)
  * `_assert_all_finite_element_wise` **(Many-Argument Workhorses)** (Impact: 68.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 471`, `structural_boundaries: 245`, `args: 54`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 214`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 33`, `import: 23`
* *Defense:* `safety: 82`, `doc: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 43.141
  * `Choke Point (Betweenness):` 0.003394 | `Ripple Effect (Closeness):` 0.388025
  * `Imports (Out-Degree: 8):` collections.abc, contextlib, functools, inspect, joblib, numbers, numpy, operator...
  * `Imported By (In-Degree: 234):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/_ridge.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.404)
- **Top Global Matches:** file_cluster_4: 5.404, file_cluster_16: 7.953, file_cluster_15: 8.738
- **Magnitude:** 1901.4 | **LOC:** 3052 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **21**; blast radius 1.582; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.5%), Complexity Load (formerly Cognitive Load) (65.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.6%)
- **Documentation Coverage:** 64.5833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_ridge_regression` **(Many-Argument Workhorses)** (Impact: 236.4)
  * `fit` **(Many-Argument Workhorses)** (Impact: 117.3)
    * *Intent:* """Fit Ridge regression model with gcv. Parameters ---------- X : {ndarray, sparse matrix} of shape ...
  * `fit` **(Many-Argument Workhorses)** (Impact: 74.4)
  * `fit` **(Many-Argument Workhorses)** (Impact: 73.2)
    * *Intent:* """Fit Ridge regression model with cv. Parameters ---------- X : ndarray of shape (n_samples, n_feat...
  * `_solve_sparse_cg` **(Many-Argument Workhorses)** (Impact: 47.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 248 instances
* *State Mutation (weighted view):* 835
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 211`, `args: 71`, `func_start: 71`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 339`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 26`, `import: 22`
* *Defense:* `safety: 12`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.582
  * `Choke Point (Betweenness):` 0.001964 | `Ripple Effect (Closeness):` 0.105284
  * `Imports (Out-Degree: 19):` abc, functools, numbers, numpy, scipy, scipy.sparse, sklearn.base, sklearn.exceptions...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `sklearn/preprocessing/tests/test_data.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.507)
- **Top Global Matches:** file_cluster_15: 6.507, file_cluster_11: 7.357, file_cluster_12: 8.11
- **Magnitude:** 1886.36 | **LOC:** 2840 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.8%), Complexity Load (formerly Cognitive Load) (26.7%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 86.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_standard_scaler_constant_features` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `test_normalize` **(Compute Cores)** (Impact: 17.7)
    * *Intent:* # Test normalize function # Only tests functionality not used by the tests for Normalizer. X = np.ra...
  * `test_robust_scaler_attributes` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* # check consistent type of attributes if with_centering and sparse.issparse(X): pytest.skip("RobustS...
  * `test_quantile_transform_check_error` **(Compute Cores)** (Impact: 14.1)
  * `test_standard_scaler_dtype` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* # Ensure scaling does not affect dtype rng = np.random.RandomState(0) n_samples = 10 n_features = 3 ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 260 instances
* *State Mutation (weighted view):* 1249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 345`, `args: 112`, `func_start: 112`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 729`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 104`
* *Architecture:* `api: 108`, `import: 22`
* *Defense:* `safety: 144`, `doc: 15`, `test: 236`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` numpy, numpy.linalg, pytest, re, scipy, sklearn, sklearn.base, sklearn.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/tree/tests/test_tree.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.314)
- **Top Global Matches:** file_cluster_15: 6.314, file_cluster_11: 7.347, file_cluster_12: 8.127
- **Magnitude:** 1839.04 | **LOC:** 3074 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 0.262; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.4%), Connectivity (formerly Api Exposure) (67.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.2%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 77.5934% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_min_weight_fraction_leaf` **(Many-Argument Workhorses)** (Impact: 18.9)
    * *Intent:* """Test if leaves contain at least min_weight_fraction_leaf of the training set"""
  * `check_min_weight_fraction_leaf_with_min_samples_leaf` **(Many-Argument Workhorses)** (Impact: 18.9)
  * `check_sparse_input` **(Many-Argument Workhorses)** (Impact: 15.9)
  * `test_absolute_errors_precomputation_function` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* """ Test the main bit of logic of the MAE(RegressionCriterion) class (used by DecisionTreeRegressor(...
  * `test_explicit_sparse_zeros` **(Many-Argument Workhorses)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 249 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 1172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 361`, `args: 119`, `func_start: 119`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 5`, `state_mutation: 674`, `planned_debt: 10`, `fragile_debt: 1`
* *Architecture:* `api: 119`, `import: 33`
* *Defense:* `safety: 99`, `doc: 29`, `test: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.262
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000855
  * `Imports (Out-Degree: 24):` copy, copyreg, io, itertools, joblib, joblib.numpy_pickle, numpy, numpy.testing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_classification.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.795)
- **Top Global Matches:** file_cluster_15: 6.795, file_cluster_11: 8.027, file_cluster_12: 8.581
- **Magnitude:** 1779.52 | **LOC:** 3847 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 37.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.0%), Guard Balance (formerly Safety Score) (55.7%), Complexity Load (formerly Cognitive Load) (23.1%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 74.5902% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_prf_warnings` **(I/O & Config Routines)** (Impact: 26.1)
    * *Intent:* # average of per-label scores f, w = precision_recall_fscore_support, UndefinedMetricWarning for ave...
  * `test_probabilistic_metrics_array_api` **(Many-Argument Workhorses)** (Impact: 24.3)
  * `test_matthews_corrcoef_against_jurman` **(Compute Cores)** (Impact: 18.8)
    * *Intent:* # Check that the multiclass matthews_corrcoef agrees with the definition # presented in Jurman, Ricc...
  * `test__check_targets` **(I/O & Config Routines)** (Impact: 18.8)
    * *Intent:* # Check that _check_targets correctly merges target types, squeezes # output and fails if input leng...
  * `test_multilabel_jaccard_score` **(Defensive Guards)** (Impact: 16.5)
    * *Intent:* # Dense label indicator matrix format y1 = np.array([[0, 1, 1], [1, 0, 1]]) y2 = np.array([[0, 0, 1]...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 188 instances
* *State Mutation (weighted view):* 1005
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 515`, `args: 122`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 629`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 116`
* *Architecture:* `api: 122`, `import: 27`
* *Defense:* `safety: 197`, `doc: 43`, `test: 291`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` functools, itertools, numpy, pandas, pytest, re, scipy, scipy.spatial.distance...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/metrics/_classification.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.721)
- **Top Global Matches:** file_cluster_6: 5.721, file_cluster_4: 10.209, file_cluster_8: 15.198
- **Magnitude:** 1712.48 | **LOC:** 4046 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 29.4%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **15**; blast radius 4.118; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.3%), Guard Balance (formerly Safety Score) (71.3%), Complexity Load (formerly Cognitive Load) (53.9%)
- **Documentation Coverage:** 63.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `class_likelihood_ratios` **(Many-Argument Workhorses)** (Impact: 127.3)
  * `classification_report` **(Many-Argument Workhorses)** (Impact: 116.3)
  * `multilabel_confusion_matrix` **(Many-Argument Workhorses)** (Impact: 85.3)
  * `confusion_matrix` **(Many-Argument Workhorses)** (Impact: 78.4)
  * `_check_targets` **(Many-Argument Workhorses)** (Impact: 43.3)
    * *Intent:* """Check that y_true and y_pred belong to the same classification task. This converts multiclass or ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 744
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 138`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 290`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 21`, `import: 15`
* *Defense:* `safety: 16`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.118
  * `Choke Point (Betweenness):` 0.009074 | `Ripple Effect (Closeness):` 0.27867
  * `Imports (Out-Degree: 11):` contextlib, math, numbers, numpy, scipy.sparse, sklearn.exceptions, sklearn.preprocessing, sklearn.utils...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `sklearn/neighbors/tests/test_neighbors.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.963)
- **Top Global Matches:** file_cluster_15: 6.963, file_cluster_12: 7.518, file_cluster_16: 7.924
- **Magnitude:** 1650.22 | **LOC:** 2510 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (27.4%), Concurrency Surface (formerly Concurrency) (12.4%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 80.6452% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_neighbors_metrics` **(Many-Argument Workhorses)** (Impact: 49.1)
  * `test_neigh_predictions_algorithm_agnosticity` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `test_unsupervised_kneighbors` **(Many-Argument Workhorses)** (Impact: 32.0)
  * `test_valid_brute_metric_for_auto_algorithm` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `test_radius_neighbors_regressor` **(Many-Argument Workhorses)** (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 977
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 248`, `args: 93`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 545`, `planned_debt: 6`, `fragile_debt: 3`, `unreferenced_by_name: 76`
* *Architecture:* `api: 87`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 56`, `doc: 16`, `test: 193`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` itertools, joblib, numpy, pytest, re, scipy.sparse, sklearn, sklearn.base...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/model_selection/tests/test_search.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.113)
- **Top Global Matches:** file_cluster_15: 6.113, file_cluster_11: 7.544, file_cluster_12: 7.664
- **Magnitude:** 1626.66 | **LOC:** 2973 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **44**; blast radius 0.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.0%), Guard Balance (formerly Safety Score) (56.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.1%), Complexity Load (formerly Cognitive Load) (37.5%)
- **Documentation Coverage:** 84.2466% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_cv_results_array_types` **(Defensive Guards)** (Impact: 21.1)
  * `test_grid_search_cv_results` **(I/O & Config Routines)** (Impact: 18.4)
  * `compare_cv_results_multimetric_with_single` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* """Compare multi-metric cv_results with the ensemble of multiple single metric cv_results from singl...
  * `test_search_cv_sample_weight_equivalence` **(Compute Cores)** (Impact: 17.3)
  * `test_grid_search_failing_classifier` **(I/O & Config Routines)** (Impact: 14.9)
    * *Intent:* # GridSearchCV with on_error != 'raise' # Ensures that a warning is raised and score reset where app...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 849
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 508`, `args: 149`, `func_start: 147`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 521`, `planned_debt: 5`, `fragile_debt: 6`, `duplicate_logic: 9`
* *Architecture:* `io: 3`, `api: 145`, `import: 44`
* *Defense:* `safety: 207`, `doc: 27`, `test: 171`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.282
  * `Choke Point (Betweenness):` 0.000169 | `Ripple Effect (Closeness):` 0.001711
  * `Imports (Out-Degree: 54):` collections.abc, functools, io, itertools, numpy, pandas, pickle, pytest...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/_logistic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.1)
- **Top Global Matches:** file_cluster_6: 5.1, file_cluster_4: 11.633, file_cluster_8: 12.886
- **Magnitude:** 1617.66 | **LOC:** 2355 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 41.2%
- **Blast Radius:** changing it is visible to **88** in-repo importer(s); it depends on **25**; blast radius 1.825; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.8%), Complexity Load (formerly Cognitive Load) (82.5%), Guard Balance (formerly Safety Score) (79.3%)
- **Documentation Coverage:** 48.1481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_logistic_regression_path` **(Many-Argument Workhorses)** (Impact: 311.7)
  * `fit` **(Many-Argument Workhorses)** (Impact: 231.4)
    * *Intent:* """Fit the model according to the given training data. Parameters ---------- X : {array-like, sparse...
  * `fit` **(Many-Argument Workhorses)** (Impact: 118.1)
    * *Intent:* """ Fit the model according to the given training data. Parameters ---------- X : {array-like, spars...
  * `_log_reg_scoring_path` **(Many-Argument Workhorses)** (Impact: 82.8)
    * *Intent:* # helper function for LogisticCV
  * `_check_solver` **(Stateful Encapsulated Methods)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 235 instances
* *State Mutation (weighted view):* 769
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 96`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 299`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 10`, `import: 26`
* *Defense:* `safety: 6`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.825
  * `Choke Point (Betweenness):` 0.006603 | `Ripple Effect (Closeness):` 0.096309
  * `Imports (Out-Degree: 26):` inspect, numbers, numpy, scipy, sklearn._loss.loss, sklearn.base, sklearn.linear_model._base, sklearn.linear_model._glm.glm...
  * `Imported By (In-Degree: 88):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_common.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.51)
- **Top Global Matches:** file_cluster_15: 6.51, file_cluster_16: 7.248, file_cluster_12: 7.696
- **Magnitude:** 1520.58 | **LOC:** 2803 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 26.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.31; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.8%), Guard Balance (formerly Safety Score) (65.1%), Connectivity (formerly Api Exposure) (51.7%), Complexity Load (formerly Cognitive Load) (27.9%)
- **Documentation Coverage:** 89.6825% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_sample_weight_invariance` **(Many-Argument Workhorses)** (Impact: 44.3)
  * `check_array_api_metric` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `test_mixed_array_api_namespace_input_compliance` **(Many-Argument Workhorses)** (Impact: 29.9)
  * `test_format_invariance_with_1d_vectors` **(Compute Cores)** (Impact: 23.2)
  * `test_array_api_classification_mixed_string_numeric_input` **(Many-Argument Workhorses)** (Impact: 22.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 875
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 196`, `args: 69`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 427`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 5`
* *Architecture:* `api: 59`, `import: 22`
* *Defense:* `safety: 37`, `doc: 10`, `test: 137`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.31
  * `Choke Point (Betweenness):` 9.8e-05 | `Ripple Effect (Closeness):` 0.000855
  * `Imports (Out-Degree: 18):` functools, inspect, itertools, math, numpy, pytest, re, sklearn._config...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/tests/test_logistic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.945)
- **Top Global Matches:** file_cluster_15: 6.945, file_cluster_11: 8.216, file_cluster_16: 8.722
- **Magnitude:** 1510.64 | **LOC:** 2880 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.1%), Guard Balance (formerly Safety Score) (59.7%), Complexity Load (formerly Cognitive Load) (26.4%), Connectivity (formerly Api Exposure) (10.9%)
- **Documentation Coverage:** 73.0539% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_logistic_regression_array_api_compliance` **(Many-Argument Workhorses)** (Impact: 54.2)
  * `test_logistic_regression_solvers_multiclass_unpenalized` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `test_check_solver_option` **(Compute Cores)** (Impact: 26.2)
    * *Intent:* # TODO(1.11): remove filterwarnings with change of default scoring # TODO(1.10): remove filterwarnin...
  * `test_multinomial_cv_iris` **(Defensive Guards)** (Impact: 25.2)
    * *Intent:* # TODO(1.12): remove deprecated use_legacy_attributes # Test that multinomial LogisticRegressionCV i...
  * `test_logistic_regression_solvers_multiclass` **(Compute Cores)** (Impact: 23.1)
    * *Intent:* # FIXME: the random state is fixed in the following test because SAG fails # to converge to the same...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 864
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 310`, `args: 82`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `state_mutation: 474`, `planned_debt: 49`, `fragile_debt: 16`, `unreferenced_by_name: 78`
* *Architecture:* `io: 1`, `api: 79`, `import: 26`
* *Defense:* `safety: 117`, `doc: 24`, `test: 207`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` itertools, numpy, numpy.testing, os, pytest, re, scipy, scipy.linalg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/model_selection/tests/test_validation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.462)
- **Top Global Matches:** file_cluster_15: 6.462, file_cluster_12: 6.637, file_cluster_11: 7.716
- **Magnitude:** 1498.06 | **LOC:** 2746 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.1%), Complexity Load (formerly Cognitive Load) (36.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.4%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 88.9868% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fit` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `check_cross_val_predict_multilabel` **(Many-Argument Workhorses)** (Impact: 29.3)
    * *Intent:* """Check the output of cross_val_predict for 2D targets using Estimators which provide a predictions...
  * `test_cross_validate_failing_scorer` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `check_cross_validate_single_metric` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `check_cross_validate_multi_metric` **(Many-Argument Workhorses)** (Impact: 20.7)
    * *Intent:* # Test multimetric evaluation when scoring is a list / dict ( train_mse_scores, test_mse_scores, tra...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 767
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 373`, `args: 128`, `func_start: 116`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 465`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 5`, `unreferenced_by_name: 74`
* *Architecture:* `io: 1`, `api: 115`, `import: 40`
* *Defense:* `safety: 109`, `doc: 19`, `test: 146`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 47):` functools, numpy, os, pandas, pytest, re, scipy.sparse, sklearn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/preprocessing/_data.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.098)
- **Top Global Matches:** file_cluster_4: 6.098, file_cluster_15: 7.358, file_cluster_16: 7.593
- **Magnitude:** 1485.32 | **LOC:** 3719 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **129** in-repo importer(s); it depends on **15**; blast radius 4.341; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.5%), Connectivity (formerly Api Exposure) (44.6%), Complexity Load (formerly Cognitive Load) (35.1%)
- **Documentation Coverage:** 20.3704% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `partial_fit` **(Many-Argument Workhorses)** (Impact: 65.5)
    * *Intent:* """Online computation of mean and std on X for later scaling. All of X is processed as a single batc...
  * `normalize` **(Many-Argument Workhorses)** (Impact: 52.1)
    * *Intent:* """Scale input vectors individually to unit norm (vector length). Read more in the :ref:`User Guide ...
  * `scale` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* """Standardize a dataset along any axis. Center to the mean and component wise scale to unit varianc...
  * `fit` **(Many-Argument Workhorses)** (Impact: 29.3)
    * *Intent:* """Compute the median and quantiles to be used for scaling. Parameters ---------- X : {array-like, s...
  * `_fit` **(Stateful Encapsulated Methods)** (Impact: 26.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 692
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 201`, `args: 70`, `func_start: 70`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 308`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 48`, `import: 15`
* *Defense:* `safety: 8`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.341
  * `Choke Point (Betweenness):` 0.000898 | `Ripple Effect (Closeness):` 0.251513
  * `Imports (Out-Degree: 10):` numbers, numpy, scipy, scipy.special, sklearn.base, sklearn.preprocessing._encoders, sklearn.utils, sklearn.utils._array_api...
  * `Imported By (In-Degree: 129):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/_validation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.745)
- **Top Global Matches:** file_cluster_6: 7.745, file_cluster_8: 12.46, file_cluster_4: 14.485
- **Magnitude:** 1469.04 | **LOC:** 2493 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **62** in-repo importer(s); it depends on **23**; blast radius 2.261; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.3%), Complexity Load (formerly Cognitive Load) (56.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.6%)
- **Documentation Coverage:** 62.963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_fit_and_score` **(Many-Argument Workhorses)** (Impact: 207.9)
  * `learning_curve` **(Many-Argument Workhorses)** (Impact: 99.1)
  * `cross_val_predict` **(Many-Argument Workhorses)** (Impact: 92.2)
  * `cross_validate` **(Many-Argument Workhorses)** (Impact: 65.3)
  * `_score` **(Many-Argument Workhorses)** (Impact: 64.3)
    * *Intent:* """Compute the score(s) of an estimator on a given test set. Will return a dict of floats if `scorer...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 618
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 104`, `args: 20`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 230`, `planned_debt: 8`
* *Architecture:* `api: 7`, `import: 24`
* *Defense:* `safety: 33`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.261
  * `Choke Point (Betweenness):` 0.001871 | `Ripple Effect (Closeness):` 0.17091
  * `Imports (Out-Degree: 16):` collections, contextlib, functools, joblib, numbers, numpy, scipy.sparse, sklearn.base...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `sklearn/decomposition/_nmf.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.199)
- **Top Global Matches:** file_cluster_4: 6.199, file_cluster_6: 7.775, file_cluster_16: 12.947
- **Magnitude:** 1384.56 | **LOC:** 2403 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **18**; blast radius 0.534; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.3%), Complexity Load (formerly Cognitive Load) (47.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.6%)
- **Documentation Coverage:** 34.0426% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_multiplicative_update_w` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `_multiplicative_update_h` **(Many-Argument Workhorses)** (Impact: 84.3)
  * `_fit_multiplicative_update` **(Many-Argument Workhorses)** (Impact: 62.2)
  * `_check_w_h` **(Stateful Encapsulated Methods)** (Impact: 49.5)
    * *Intent:* """Check W and H, or initialize them."""
  * `_minibatch_convergence` **(Stateful Encapsulated Methods)** (Impact: 48.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 654
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 125`, `args: 35`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 254`, `planned_debt: 1`
* *Architecture:* `api: 14`, `import: 18`
* *Defense:* `safety: 3`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.534
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.089435
  * `Imports (Out-Degree: 9):` abc, itertools, math, numbers, numpy, scipy, scipy.sparse, sklearn._config...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/_cd_fast.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.951)
- **Top Global Matches:** file_cluster_8: 5.951, file_cluster_6: 16.912, file_cluster_3: 19.814
- **Magnitude:** 1377.68 | **LOC:** 1586 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%), Complexity Load (formerly Cognitive Load) (60.8%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sparse_enet_coordinate_descent` **(Many-Argument Workhorses)** (Impact: 213.5)
  * `enet_coordinate_descent_multi_task` **(Many-Argument Workhorses)** (Impact: 148.2)
  * `enet_coordinate_descent_gram` **(Many-Argument Workhorses)** (Impact: 139.8)
  * `enet_coordinate_descent` **(Many-Argument Workhorses)** (Impact: 131.0)
  * `R_plus_wj_Xj` **(Many-Argument Workhorses)** (Impact: 32.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 649
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 75`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 219`, `dead_code: 1`, `planned_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` numpy, sklearn.exceptions, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/linear_model/_coordinate_descent.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.689)
- **Top Global Matches:** file_cluster_4: 5.689, file_cluster_6: 9.457, file_cluster_16: 11.501
- **Magnitude:** 1347.48 | **LOC:** 3460 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **21**; blast radius 1.345; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.0%), Debt Markers (formerly Tech Debt) (71.1%), Complexity Load (formerly Cognitive Load) (70.1%)
- **Documentation Coverage:** 50.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `enet_path` **(Many-Argument Workhorses)** (Impact: 161.1)
  * `fit` **(Many-Argument Workhorses)** (Impact: 153.3)
    * *Intent:* """Fit linear model with coordinate descent. Fit is on grid of alphas and best alpha estimated by cr...
  * `_alpha_grid` **(Many-Argument Workhorses)** (Impact: 75.1)
    * *Intent:* ############################################################################### # Paths functions
  * `fit` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* """Fit model with coordinate descent. Parameters ---------- X : {ndarray, sparse matrix, sparse arra...
  * `_path_residuals` **(Many-Argument Workhorses)** (Impact: 53.9)
    * *Intent:* ############################################################################### # Functions for CV w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 168 instances
* *State Mutation (weighted view):* 635
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 135`, `args: 40`, `func_start: 40`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 299`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `io: 1`, `api: 22`, `import: 22`
* *Defense:* `safety: 13`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.345
  * `Choke Point (Betweenness):` 0.000407 | `Ripple Effect (Closeness):` 0.102896
  * `Imports (Out-Degree: 15):` abc, functools, joblib, numbers, numpy, scipy, sklearn.base, sklearn.linear_model...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `sklearn/tree/_tree.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.621)
- **Top Global Matches:** file_cluster_4: 5.621, file_cluster_15: 7.905, file_cluster_16: 8.43
- **Magnitude:** 1296.66 | **LOC:** 1999 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (59.1%), Connectivity (formerly Api Exposure) (42.0%)
- **Documentation Coverage:** 60.9756% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 70.8)
  * `_add_split_node` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `build` **(Many-Argument Workhorses)** (Impact: 50.7)
  * `_cost_complexity_prune` **(Many-Argument Workhorses)** (Impact: 43.8)
  * `compute_partial_dependence` **(Many-Argument Workhorses)** (Impact: 32.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 149`, `args: 60`, `func_start: 60`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 286`, `planned_debt: 1`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 2`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` numpy, scipy.sparse, sklearn.utils, struct
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/utils/tests/test_validation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.542)
- **Top Global Matches:** file_cluster_15: 7.542, file_cluster_12: 7.579, file_cluster_11: 8.592
- **Magnitude:** 1293.58 | **LOC:** 2383 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (71.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.7%), Guard Balance (formerly Safety Score) (51.9%)
- **Documentation Coverage:** 73.7557% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_check_array` **(Defensive Guards)** (Impact: 35.5)
    * *Intent:* # accept_sparse == False # raise error on sparse inputs X = [[1, 2], [3, 4]] X_csr = sp.csr_array(X)...
  * `test_check_array_links_to_imputer_doc_only_for_X` **(Defensive Guards)** (Impact: 17.5)
  * `test_check_array_min_samples_and_features_messages` **(I/O & Config Routines)** (Impact: 17.1)
    * *Intent:* # empty list is considered 2D by default: msg = r"0 feature\(s\) \(shape=\(1, 0\)\) while a minimum ...
  * `test_check_array_dia_to_int32_indexed_csr_csc_coo` **(Defensive Guards)** (Impact: 14.9)
    * *Intent:* """Check the consistency of the indices dtype with sparse matrices/arrays."""
  * `test_num_features_errors_1d_containers` **(Defensive Guards)** (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 509`, `args: 115`, `func_start: 114`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 349`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 98`
* *Architecture:* `api: 118`, `import: 29`
* *Defense:* `safety: 169`, `doc: 33`, `test: 271`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` itertools, numbers, numpy, operator, pandas, pytest, re, scipy.sparse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/linear_model/_stochastic_gradient.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.397)
- **Top Global Matches:** file_cluster_16: 6.397, file_cluster_15: 7.339, file_cluster_4: 8.205
- **Magnitude:** 1275.2 | **LOC:** 2681 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **17**; blast radius 1.534; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.9%), Complexity Load (formerly Cognitive Load) (68.1%)
- **Documentation Coverage:** 51.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_allocate_parameter_mem` **(Stateful Encapsulated Methods)** (Impact: 80.2)
  * `_fit` **(Stateful Encapsulated Methods)** (Impact: 48.0)
  * `_fit` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `_fit` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `_partial_fit` **(Many-Argument Workhorses)** (Impact: 35.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 169 instances
* *State Mutation (weighted view):* 584
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 132`, `args: 47`, `func_start: 47`, `class_start: 7`
* *Risk/State:* `state_mutation: 246`, `planned_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 21`, `import: 17`
* *Defense:* `safety: 12`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.534
  * `Choke Point (Betweenness):` 0.000532 | `Ripple Effect (Closeness):` 0.094816
  * `Imports (Out-Degree: 12):` abc, numbers, numpy, sklearn._loss._loss, sklearn.base, sklearn.exceptions, sklearn.linear_model._base, sklearn.linear_model._sgd_fast...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `sklearn/tests/test_pipeline.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.347)
- **Top Global Matches:** file_cluster_15: 6.347, file_cluster_11: 7.083, file_cluster_10: 7.991
- **Magnitude:** 1258.8 | **LOC:** 2551 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.265; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.8%), Guard Balance (formerly Safety Score) (52.2%), Complexity Load (formerly Cognitive Load) (29.6%)
- **Documentation Coverage:** 72.8707% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pipeline_invalid_parameters` **(I/O & Config Routines)** (Impact: 12.1)
    * *Intent:* # Test the various init parameters of the pipeline in fit # method pipeline = Pipeline([(1, 1)]) wit...
  * `test_metadata_routing_for_pipeline` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* # split and partial_fit not relevant for pipelines """Test that metadata is routed correctly for pip...
  * `test_step_name_validation` **(I/O & Config Routines)** (Impact: 9.8)
  * `test_feature_union_array_api_compliance` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* """Test that FeatureUnion with Array API-compatible transformers works."""
  * `test_feature_union_metadata_routing_error` **(I/O & Config Routines)** (Impact: 8.9)
    * *Intent:* """Test that the right error is raised when metadata is not requested."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 513`, `args: 167`, `func_start: 153`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 436`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 2`, `duplicate_logic: 19`
* *Architecture:* `api: 167`, `import: 34`
* *Defense:* `safety: 180`, `doc: 45`, `test: 164`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.000855
  * `Imports (Out-Degree: 47):` itertools, joblib, numpy, pytest, re, shutil, sklearn, sklearn.base...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.311)
- **Top Global Matches:** file_cluster_4: 6.311, file_cluster_16: 7.373, file_cluster_15: 8.54
- **Magnitude:** 1252.38 | **LOC:** 2380 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **25**; blast radius 1.027; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (63.2%)
- **Documentation Coverage:** 33.871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fit` **(Many-Argument Workhorses)** (Impact: 231.8)
  * `_check_categorical_features` **(Many-Argument Workhorses)** (Impact: 57.9)
    * *Intent:* """Check and validate categorical features in X Parameters ---------- X : {array-like, pandas DataFr...
  * `_check_interaction_cst` **(Stateful Encapsulated Methods)** (Impact: 24.3)
    * *Intent:* """Check and validation for interaction constraints."""
  * `_print_iteration_stats` **(Stateful Encapsulated Methods)** (Impact: 21.2)
    * *Intent:* """Print info about the current fitting iteration."""
  * `_get_small_trainset` **(Many-Argument Workhorses)** (Impact: 18.8)
    * *Intent:* """Compute the indices of the subsample set and return this set. For efficiency, we need to subsampl...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 591
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 159`, `args: 46`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 249`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `import: 25`
* *Defense:* `safety: 13`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.001302 | `Ripple Effect (Closeness):` 0.060073
  * `Imports (Out-Degree: 22):` abc, contextlib, functools, itertools, numbers, numpy, sklearn._loss.loss, sklearn.base...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/tests/test_split.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.113)
- **Top Global Matches:** file_cluster_15: 7.113, file_cluster_12: 7.503, file_cluster_11: 7.946
- **Magnitude:** 1224.44 | **LOC:** 2133 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.7%), Guard Balance (formerly Safety Score) (59.6%), Complexity Load (formerly Cognitive Load) (28.6%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 96.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_group_kfold` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `test_stratified_kfold_label_invariance` **(Type Conversions)** (Impact: 11.4)
    * *Intent:* # Check that stratified kfold gives the same indices regardless of labels n_samples = 100 y = np.arr...
  * `test_leave_one_p_group_out` **(Defensive Guards)** (Impact: 10.7)
  * `test_kfold_valueerrors` **(I/O & Config Routines)** (Impact: 10.6)
  * `test_array_api_train_test_split` **(Many-Argument Workhorses)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 745
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 331`, `args: 82`, `func_start: 82`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 425`, `fragile_debt: 1`, `unreferenced_by_name: 76`
* *Architecture:* `io: 2`, `api: 79`, `import: 23`
* *Defense:* `safety: 149`, `doc: 4`, `test: 167`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` itertools, numpy, pandas, pytest, re, scipy, scipy.sparse, scipy.special...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `asv_benchmarks/benchmarks/manifold.py` (PYTHON) | Magnitude: 23.98 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 13, args: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `sklearn/linear_model/tests/test_least_angle.py` (PYTHON) | Magnitude: 499.04 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 508, core_var_decl: 240, state_mutation: 188, design_snake_case: 187
- `sklearn/utils/tests/test_parallel.py` (PYTHON) | Magnitude: 126.98 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 68, core_var_decl: 28, design_snake_case: 28
- `sklearn/_loss/tests/test_link.py` (PYTHON) | Magnitude: 107.06 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 87, core_var_decl: 33, design_snake_case: 32, structural_boundaries: 23
- `sklearn/feature_selection/tests/test_sequential.py` (PYTHON) | Magnitude: 125.36 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 181, core_var_decl: 101, design_snake_case: 95, structural_boundaries: 61
- `sklearn/utils/tests/test_metaestimators.py` (PYTHON) | Magnitude: 27.26 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 19, safety: 8, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `sklearn/cluster/_birch.py` (PYTHON) | Magnitude: 396.18 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 303, state_mutation: 118, core_var_decl: 103, design_snake_case: 94
- `benchmarks/bench_glmnet.py` (PYTHON) | Magnitude: 64.92 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 83, core_var_decl: 44, design_snake_case: 36, state_mutation: 32
- `maint_tools/update_tracking_issue.py` (PYTHON) | Magnitude: 129.64 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 90, core_var_decl: 46, design_snake_case: 46, branch: 41
- `sklearn/feature_extraction/text.py` (PYTHON) | Magnitude: 910.98 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 813, core_var_decl: 267, design_snake_case: 249, state_mutation: 189
- `examples/miscellaneous/plot_kernel_approximation.py` (PYTHON) | Magnitude: 76.78 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 63, core_var_decl: 60, design_snake_case: 57, state_mutation: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `sklearn/ensemble/_hist_gradient_boosting/tests/test_bitset.py` (PYTHON) | Magnitude: 36.22 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 15, branch: 8, core_var_decl: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `build_tools/github/test_windows_wheels.sh` (SHELL) | Magnitude: 16.36 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, core_var_decl: 6, design_upper_case: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `examples/calibration/plot_compare_calibration.py` (PYTHON) | Magnitude: 47.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 49, core_var_decl: 42, design_snake_case: 41, structural_boundaries: 24
- `sklearn/ensemble/_hist_gradient_boosting/tests/test_binning.py` (PYTHON) | Magnitude: 288.74 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 348, core_var_decl: 149, state_mutation: 128, design_snake_case: 123
- `sklearn/decomposition/_sparse_pca.py` (PYTHON) | Magnitude: 116.26 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 194, core_var_decl: 106, design_snake_case: 98, state_mutation: 41
- `sklearn/manifold/tests/test_spectral_embedding.py` (PYTHON) | Magnitude: 317.9 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 320, core_var_decl: 182, design_snake_case: 172, state_mutation: 116
- `sklearn/metrics/cluster/tests/test_bicluster.py` (PYTHON) | Magnitude: 18.94 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 23, safety: 12, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `sklearn/ensemble/_weight_boosting.py` (PYTHON) | Magnitude: 374.6 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 343, core_var_decl: 120, design_snake_case: 113, structural_boundaries: 80
- `sklearn/cluster/_bisect_k_means.py` (PYTHON) | Magnitude: 243.84 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 203, core_var_decl: 74, design_snake_case: 69, state_mutation: 63
- `sklearn/mixture/tests/test_gaussian_mixture.py` (PYTHON) | Magnitude: 1073.38 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1188, core_var_decl: 621, design_snake_case: 567, state_mutation: 378
- `sklearn/inspection/_permutation_importance.py` (PYTHON) | Magnitude: 142.34 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 120, core_var_decl: 37, design_snake_case: 34, structural_boundaries: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/miscellaneous/plot_pipeline_display.py` (PYTHON) | Magnitude: 32.96 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 46, indent_spaces: 40, import: 23, ml_traditional: 21
- `examples/svm/plot_svm_anova.py` (PYTHON) | Magnitude: 34.66 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, state_mutation: 9, indent_spaces: 9, core_var_decl: 9
- `sklearn/utils/__init__.py` (PYTHON) | Magnitude: 18.42 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 32, import: 16, ml_traditional: 16
- `examples/frozen/plot_frozen_examples.py` (PYTHON) | Magnitude: 26.74 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, core_var_decl: 11, design_snake_case: 11, indent_spaces: 10
- `examples/release_highlights/plot_release_highlights_1_2_0.py` (PYTHON) | Magnitude: 30.36 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 30, structural_boundaries: 26, indent_spaces: 25, design_snake_case: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/feature_selection/plot_feature_selection_pipeline.py` (PYTHON) | Magnitude: 19.46 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, core_var_decl: 12, design_snake_case: 12, import: 6
- `sklearn/ensemble/_hist_gradient_boosting/histogram.pyx` (PYTHON) | Magnitude: 221.04 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 294, core_var_decl: 72, design_snake_case: 71, state_mutation: 41
- `examples/compose/plot_feature_union.py` (PYTHON) | Magnitude: 24.46 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: core_var_decl: 13, structural_boundaries: 12, design_snake_case: 11, state_mutation: 9
- `examples/classification/plot_classifier_comparison.py` (PYTHON) | Magnitude: 44.24 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 34, core_var_decl: 32, design_snake_case: 32
- `benchmarks/bench_plot_svd.py` (PYTHON) | Magnitude: 43.74 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 48, core_var_decl: 24, design_snake_case: 21, structural_boundaries: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `build_tools/github/repair_windows_wheels.sh` (SHELL) | Magnitude: 5.72 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: state_mutation: 3, core_var_decl: 3, design_upper_case: 3, structural_boundaries: 2
- `build_tools/circle/download_documentation.sh` (SHELL) | Magnitude: 1.52 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 1, safety: 1, safety_bypasses: 1, io: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sklearn/inspection/_pd_utils.py` (PYTHON) | Magnitude: 35.4 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 23, branch: 10, structural_boundaries: 8, safety: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/unit-tests.yml` -> Churn: **100.0%** | Cog Load: 9.4567% | Debt: 54.334%
- `sklearn/linear_model/_logistic.py` -> Churn: **92.82%** | Cog Load: 82.5021% | Debt: 8.9197%
- `sklearn/metrics/_classification.py` -> Churn: **92.35%** | Cog Load: 53.8713% | Debt: 8.5486%
- `sklearn/utils/estimator_checks.py` -> Churn: **76.78%** | Cog Load: 67.1192% | Debt: 8.7722%
- `sklearn/inspection/_plot/decision_boundary.py` -> Churn: **75.27%** | Cog Load: 65.0238% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sklearn/tree/tests/test_tree.py` -> **Arthur Lacote** (85.7% isolated ownership) | Magnitude: 1839.04
- `sklearn/model_selection/tests/test_validation.py` -> **Olivier Grisel** (100.0% isolated ownership) | Magnitude: 1498.06
- `sklearn/decomposition/_nmf.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1384.56
- `sklearn/tree/_tree.pyx` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1296.66
- `sklearn/neighbors/_base.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1218.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `sklearn/preprocessing/_discretization.py` -> **Severity: 2.778** (Bridge: 0.0278 * Flux: 100.0%)
- `sklearn/neighbors/_nca.py` -> **Severity: 1.71** (Bridge: 0.0171 * Flux: 100.0%)
- `sklearn/base.py` -> **Severity: 1.673** (Bridge: 0.0167 * Flux: 100.0%)
- `sklearn/metrics/_classification.py` -> **Severity: 0.907** (Bridge: 0.0091 * Flux: 100.0%)
- `sklearn/linear_model/_logistic.py` -> **Severity: 0.66** (Bridge: 0.0066 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `sklearn/utils/validation.py` -> **Severity: 26.039** (Embedded: 0.388 * Error Risk: 67.1073%)
- `sklearn/utils/fixes.py` -> **Severity: 25.318** (Embedded: 0.3383 * Error Risk: 74.8345%)
- `sklearn/base.py` -> **Severity: 24.962** (Embedded: 0.3714 * Error Risk: 67.2155%)
- `sklearn/utils/extmath.py` -> **Severity: 24.357** (Embedded: 0.3095 * Error Risk: 78.7039%)
- `sklearn/utils/_array_api.py` -> **Severity: 23.818** (Embedded: 0.3241 * Error Risk: 73.4903%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sklearn/utils/_array_api.py` -> **Severity: 3087.635** (Blast Radius: 68.878 * Doc Risk: 44.8276%)
- `sklearn/_config.py` -> **Severity: 2882.402** (Blast Radius: 50.442 * Doc Risk: 57.1429%)
- `sklearn/utils/fixes.py` -> **Severity: 2400.388** (Blast Radius: 31.005 * Doc Risk: 77.4194%)
- `sklearn/utils/_param_validation.py` -> **Severity: 1841.814** (Blast Radius: 22.689 * Doc Risk: 81.1765%)
- `sklearn/__init__.py` -> **Severity: 1740.675** (Blast Radius: 23.209 * Doc Risk: 75.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1422 literal sites + 3 sites through wrappers = 1425
- **`panics_and_aborts`:** 1784 literal sites + 9 sites through wrappers = 1793

- `analyzer` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `sklearn/feature_extraction/tests/test_text.py`
- `_get_git_revision` (function, debug_prints, primitive): 1 call sites in 1 files -- `doc/sphinxext/github_link.py`
- `check_estimator_cloneable` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `sklearn/utils/estimator_checks.py`
- `check_estimator_repr` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `sklearn/utils/estimator_checks.py`
- `get_loss` (function, debug_prints, primitive): 1 call sites in 1 files -- `benchmarks/bench_rcv1_logreg_convergence.py`
- `json_urlread` (function, debug_prints, primitive): 1 call sites in 1 files -- `build_tools/circle/list_versions.py`
- `json_urlread` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `build_tools/circle/list_versions.py`
- `setup_compose` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `doc/conftest.py`
- `setup_grid_search` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `doc/conftest.py`
- `setup_impute` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `doc/conftest.py`
- `setup_preprocessing` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `doc/conftest.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 68185 call pairs -- scoped 35.2%, unique 0.0%, ambiguous 9.7%, external 55.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 67985 | 35.3% | 0.0% | 9.7% | 55.0% |
| shell | 169 | 14.2% | 0.0% | 0.0% | 85.8% |
| javascript | 27 | 3.7% | 0.0% | 0.0% | 96.3% |
| cpp | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
