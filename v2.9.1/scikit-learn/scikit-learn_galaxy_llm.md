# ARCHITECTURAL_BRIEF: scikit-learn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/scikit-learn/scikit-learn.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1188 analyzed artifact(s), 251700 LOC.
- **Load-bearing artifact:** `asv_benchmarks/benchmarks/datasets.py` -- 400 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 1188 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 600 |
| Total LOC | 251700 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 66.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.329 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1271 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1596 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 60 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1065 | 248530 | 89.6% |
| PLAINTEXT | 49 | 0 | 4.1% |
| SHELL | 24 | 860 | 2.0% |
| MARKDOWN | 10 | 0 | 0.8% |
| CPP | 8 | 299 | 0.7% |
| JAVASCRIPT | 6 | 179 | 0.5% |
| CSS | 6 | 844 | 0.5% |
| MAKEFILE | 4 | 127 | 0.3% |
| JSON | 4 | 43 | 0.3% |
| XML | 4 | 8 | 0.3% |
| CSV | 4 | 372 | 0.3% |
| HTML | 2 | 307 | 0.2% |
| YAML | 1 | 5 | 0.1% |
| BATCH | 1 | 126 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.808`
> **Composition Archetype:** `Hub-Coupled App` (z +2.81; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 22%, Many-Argument Workhorses Files 18%, Data / Markup / Trivial 15%, Large Core Modules (3) 14%, Large Core Modules (2) 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1126 | 94.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 59 | 5.0% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 600*

**Composition by Extension & Reason:**
- `.rst`: 206x Excluded (Unsupported Extension: '.rst')
- `.png`: 96x Excluded (Explicitly Denied Extension: '.png')
- `.gz`: 82x Excluded (Explicitly Denied Extension: '.gz')
- `no_extension`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 25 LOC), 2x Excluded (Machine-Generated Source Code Signature: 31 LOC)
- `.tp`: 20x Excluded (Unsupported Extension: '.tp'), 4x Unsupported Format (.tp)
- `.build`: 20x Excluded (Unsupported Extension: '.build'), 1x Unsupported Format (.build)
- `.lock`: 13x Excluded (Unsupported Extension: '.lock')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1357 LOC), 1x Excluded (Machine-Generated Source Code Signature: 252 LOC)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 47 LOC), 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.template`: 7x Excluded (Unsupported Extension: '.template')
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.cpp`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 19 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 29.4 | 31.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 71.3 | 83.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.4 | 7.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.5 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 8.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 46.0 | 43.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2737 | 460 | 6 | `sklearn/utils/_test_common/instance_generator.py` |
| cleanup | 40 | 23 | 0 | `doc/Makefile` |
| guards | 12468 | 584 | 32 | `sklearn/utils/estimator_checks.py` |
| danger | 3363 | 502 | 8 | `sklearn/utils/estimator_checks.py` |
| concurrency | 365 | 79 | 0 | `sklearn/utils/estimator_checks.py` |
| connectivity | 10579 | 789 | 23 | `sklearn/utils/tests/test_estimator_checks.py` |
| io | 896 | 133 | 1 | `doc/templates/index.html` |
| crypto | 4 | 4 | 0 | `examples/applications/plot_out_of_core_classification.py` |
| ipc | 31 | 19 | 0 | `build_tools/check-meson-openmp-dependencies.py` |
| time | 151 | 43 | 0 | `examples/applications/plot_out_of_core_classification.py` |
| serialization | 55 | 28 | 0 | `sklearn/tests/test_base.py` |
| regex | 165 | 56 | 0 | `build_tools/circle/build_doc.sh` |
| events | 103 | 24 | 0 | `sklearn/decomposition/_dict_learning.py` |
| tests | 12134 | 269 | 32 | `sklearn/metrics/tests/test_classification.py` |
| docs | 5740 | 896 | 14 | `sklearn/gaussian_process/kernels.py` |
| debt | 2701 | 509 | 7 | `sklearn/linear_model/tests/test_logistic.py` |
| mutation | 147250 | 994 | 314 | `sklearn/utils/estimator_checks.py` |
| dead_code | 5460 | 458 | 14 | `sklearn/metrics/tests/test_classification.py` |
| credential | 1 | 1 | 0 | `doc/templates/index.html` |
| threat | 859 | 247 | 2 | `sklearn/gaussian_process/kernels.py` |
| ml_ai | 7799 | 922 | 15 | `sklearn/linear_model/_ridge.py` |
| ui | 118 | 13 | 0 | `doc/templates/index.html` |

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

1. **datasets.py** (`asv_benchmarks/benchmarks/datasets.py`) — 400 inbound connections
2. **model_selection.py** (`asv_benchmarks/benchmarks/model_selection.py`) — 224 inbound connections
3. **linear_model.py** (`asv_benchmarks/benchmarks/linear_model.py`) — 214 inbound connections
4. **base.py** (`sklearn/base.py`) — 211 inbound connections
5. **_testing.py** (`sklearn/utils/_testing.py`) — 180 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_search.py** (`sklearn/model_selection/tests/test_search.py`) — 44 outbound dependencies
2. **instance_generator.py** (`sklearn/utils/_test_common/instance_generator.py`) — 42 outbound dependencies
3. **estimator_checks.py** (`sklearn/utils/estimator_checks.py`) — 41 outbound dependencies
4. **test_validation.py** (`sklearn/model_selection/tests/test_validation.py`) — 38 outbound dependencies
5. **_testing.py** (`sklearn/utils/_testing.py`) — 38 outbound dependencies

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
| `sklearn/utils` | 62 | 17458.28 | 33.49% | 18.7% |
| `sklearn/linear_model` | 18 | 12353.26 | 49.45% | 13.11% |
| `sklearn/linear_model/tests` | 19 | 9552.54 | 30.17% | 0.0% |
| `sklearn/tests` | 27 | 8756.18 | 22.69% | 0.0% |
| `sklearn/utils/tests` | 44 | 8560.94 | 39.7% | 0.0% |
| `sklearn/metrics/tests` | 9 | 7635.86 | 27.57% | 0.0% |
| `sklearn` | 19 | 6828.56 | 40.67% | 30.43% |
| `sklearn/preprocessing/tests` | 9 | 5715.98 | 21.68% | 0.0% |
| `sklearn/cluster` | 20 | 5534.94 | 38.47% | 3.75% |
| `sklearn/preprocessing` | 10 | 5369.04 | 41.07% | 9.18% |

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8760` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `sklearn/utils/estimator_checks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4183.24 | **LOC:** 5485 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **41**; blast radius 0.789; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.9%), Connectivity (formerly Api Exposure) (69.1%)
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
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 2`, `state_mutation: 916`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 1`
* *Architecture:* `api: 115`, `import: 44`
* *Defense:* `safety: 368`, `doc: 43`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.789
  * `Choke Point (Betweenness):` 0.000397 | `Ripple Effect (Closeness):` 0.014482
  * `Imports (Out-Degree: 19):` __future__, contextlib, copy, functools, inspect, joblib, numbers, numpy...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/tests/test_ridge.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2130.7 | **LOC:** 2631 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (91.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.4%), Complexity Load (formerly Cognitive Load) (26.7%), Connectivity (formerly Api Exposure) (9.8%)
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
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 580`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 7`, `unreferenced_by_name: 71`
* *Architecture:* `api: 79`, `import: 20`
* *Defense:* `safety: 106`, `doc: 28`, `test: 253`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` itertools, numpy, pytest, scipy, sklearn, sklearn.base, sklearn.datasets, sklearn.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/utils/validation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2118.86 | **LOC:** 2942 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **179** in-repo importer(s); it depends on **23**; blast radius 38.141; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.3%)
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
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 214`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 33`, `import: 23`
* *Defense:* `safety: 82`, `doc: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.141
  * `Choke Point (Betweenness):` 0.002425 | `Ripple Effect (Closeness):` 0.309944
  * `Imports (Out-Degree: 7):` collections.abc, contextlib, functools, inspect, joblib, numbers, numpy, operator...
  * `Imported By (In-Degree: 179):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/_ridge.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1901.4 | **LOC:** 3052 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **23**; blast radius 0.364; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Complexity Load (formerly Cognitive Load) (65.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.1%)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 339`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 26`, `import: 22`
* *Defense:* `safety: 12`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.003753
  * `Imports (Out-Degree: 14):` abc, functools, numbers, numpy, scipy, scipy.sparse, sklearn.base, sklearn.datasets...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sklearn/preprocessing/tests/test_data.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1886.36 | **LOC:** 2840 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (89.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.7%), Complexity Load (formerly Cognitive Load) (26.7%), Connectivity (formerly Api Exposure) (11.4%)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 729`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 104`
* *Architecture:* `api: 108`, `import: 22`
* *Defense:* `safety: 144`, `doc: 15`, `test: 236`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` numpy, numpy.linalg, pytest, re, scipy, sklearn, sklearn.base, sklearn.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/tree/tests/test_tree.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1839.04 | **LOC:** 3074 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 0.268; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (89.9%), Connectivity (formerly Api Exposure) (67.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.3%), Complexity Load (formerly Cognitive Load) (25.0%)
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
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 5`, `state_mutation: 674`, `dead_code: 3`, `planned_debt: 10`, `fragile_debt: 1`
* *Architecture:* `api: 119`, `import: 33`
* *Defense:* `safety: 99`, `doc: 29`, `test: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.268
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000842
  * `Imports (Out-Degree: 13):` copy, copyreg, io, itertools, joblib, joblib.numpy_pickle, numpy, numpy.testing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_classification.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1779.52 | **LOC:** 3847 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.9%), Complexity Load (formerly Cognitive Load) (23.1%), Connectivity (formerly Api Exposure) (11.7%)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 629`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 116`
* *Architecture:* `api: 122`, `import: 27`
* *Defense:* `safety: 197`, `doc: 43`, `test: 291`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` functools, itertools, numpy, pandas, pytest, re, scipy, scipy.spatial.distance...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/metrics/_classification.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1712.48 | **LOC:** 4046 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (98.8%), Guard Balance (formerly Safety Score) (94.0%), Complexity Load (formerly Cognitive Load) (53.9%)
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 290`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 21`, `import: 15`
* *Defense:* `safety: 16`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.286
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.001685
  * `Imports (Out-Degree: 9):` contextlib, math, numbers, numpy, scipy.sparse, sklearn, sklearn.exceptions, sklearn.metrics...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/neighbors/tests/test_neighbors.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1650.22 | **LOC:** 2510 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (90.8%), Complexity Load (formerly Cognitive Load) (27.4%), Concurrency Surface (formerly Concurrency) (12.4%), Connectivity (formerly Api Exposure) (10.8%)
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
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 545`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 3`, `unreferenced_by_name: 76`
* *Architecture:* `api: 87`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 56`, `doc: 16`, `test: 193`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` itertools, joblib, numpy, pytest, re, scipy.sparse, sklearn, sklearn.base...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/model_selection/tests/test_search.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1626.66 | **LOC:** 2973 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **44**; blast radius 0.299; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (37.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.1%)
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
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 521`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 6`, `duplicate_logic: 9`
* *Architecture:* `io: 3`, `api: 145`, `import: 44`
* *Defense:* `safety: 207`, `doc: 27`, `test: 171`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.299
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.001685
  * `Imports (Out-Degree: 25):` collections.abc, functools, io, itertools, numpy, pandas, pickle, pytest...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/_logistic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1617.66 | **LOC:** 2355 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 41.2%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **27**; blast radius 0.285; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.9%), Complexity Load (formerly Cognitive Load) (82.5%)
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
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 299`, `dead_code: 2`, `planned_debt: 4`
* *Architecture:* `api: 10`, `import: 26`
* *Defense:* `safety: 6`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.285
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.001685
  * `Imports (Out-Degree: 20):` inspect, numbers, numpy, scipy, sklearn._loss.loss, sklearn.base, sklearn.datasets, sklearn.linear_model...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_common.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1520.58 | **LOC:** 2803 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 23.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Connectivity (formerly Api Exposure) (51.7%), Complexity Load (formerly Cognitive Load) (27.9%)
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
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 427`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 5`
* *Architecture:* `api: 59`, `import: 22`
* *Defense:* `safety: 37`, `doc: 10`, `test: 137`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.307
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.000842
  * `Imports (Out-Degree: 11):` functools, inspect, itertools, math, numpy, pytest, re, sklearn._config...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/tests/test_logistic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1510.64 | **LOC:** 2880 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.2%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (26.4%), Connectivity (formerly Api Exposure) (10.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` itertools, numpy, numpy.testing, os, pytest, re, scipy, scipy.linalg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/model_selection/tests/test_validation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1498.06 | **LOC:** 2746 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.1%), Complexity Load (formerly Cognitive Load) (36.5%), Connectivity (formerly Api Exposure) (11.6%)
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
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 465`, `dead_code: 5`, `fragile_debt: 1`, `duplicate_logic: 5`, `unreferenced_by_name: 74`
* *Architecture:* `io: 1`, `api: 115`, `import: 40`
* *Defense:* `safety: 109`, `doc: 19`, `test: 146`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` functools, numpy, os, pandas, pytest, re, scipy.sparse, sklearn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/preprocessing/_data.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1485.32 | **LOC:** 3719 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **17**; blast radius 0.339; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Connectivity (formerly Api Exposure) (44.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.4%)
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
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 308`, `dead_code: 9`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 48`, `import: 15`
* *Defense:* `safety: 8`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.339
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.002696
  * `Imports (Out-Degree: 10):` numbers, numpy, scipy, scipy.special, sklearn.base, sklearn.metrics.pairwise, sklearn.preprocessing, sklearn.preprocessing._encoders...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/_validation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1469.04 | **LOC:** 2493 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **28**; blast radius 0.454; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.4%), Complexity Load (formerly Cognitive Load) (56.3%)
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
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 230`, `dead_code: 1`, `planned_debt: 8`
* *Architecture:* `api: 7`, `import: 24`
* *Defense:* `safety: 33`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.454
  * `Choke Point (Betweenness):` 9.1e-05 | `Ripple Effect (Closeness):` 0.013368
  * `Imports (Out-Degree: 14):` collections, contextlib, functools, joblib, numbers, numpy, scipy.sparse, sklearn...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `sklearn/decomposition/_nmf.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1384.56 | **LOC:** 2403 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.299; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.0%), Complexity Load (formerly Cognitive Load) (47.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.8%)
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
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 254`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 14`, `import: 18`
* *Defense:* `safety: 3`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.299
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.001685
  * `Imports (Out-Degree: 9):` abc, itertools, math, numbers, numpy, scipy, scipy.sparse, sklearn._config...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/_cd_fast.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1377.68 | **LOC:** 1586 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.8%)
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
* *Risk/State:* `state_mutation: 219`, `dead_code: 9`, `planned_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` numpy, sklearn.exceptions, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/linear_model/_coordinate_descent.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1347.48 | **LOC:** 3460 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **24**; blast radius 0.29; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.2%), Debt Markers (formerly Tech Debt) (72.3%), Complexity Load (formerly Cognitive Load) (70.1%)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 299`, `dead_code: 3`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `io: 1`, `api: 22`, `import: 22`
* *Defense:* `safety: 13`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.29
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.001685
  * `Imports (Out-Degree: 14):` abc, functools, joblib, numbers, numpy, scipy, sklearn, sklearn.base...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/tree/_tree.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1296.66 | **LOC:** 1999 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.253; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Complexity Load (formerly Cognitive Load) (59.1%), Connectivity (formerly Api Exposure) (42.0%)
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
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 286`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 2`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy, scipy.sparse, sklearn.utils, struct
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/utils/tests/test_validation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1293.58 | **LOC:** 2383 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (71.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.4%), Guard Balance (formerly Safety Score) (56.0%)
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
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 349`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 98`
* *Architecture:* `api: 118`, `import: 29`
* *Defense:* `safety: 169`, `doc: 33`, `test: 271`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` itertools, numbers, numpy, operator, pandas, pytest, re, scipy.sparse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/linear_model/_stochastic_gradient.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1275.2 | **LOC:** 2681 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 0.398; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.1%)
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
* *Risk/State:* `state_mutation: 246`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 21`, `import: 17`
* *Defense:* `safety: 12`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.398
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.00337
  * `Imports (Out-Degree: 13):` abc, numbers, numpy, sklearn, sklearn._loss._loss, sklearn.base, sklearn.exceptions, sklearn.linear_model...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `sklearn/tests/test_pipeline.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1258.8 | **LOC:** 2551 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.273; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.1%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (29.6%)
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 436`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 2`, `duplicate_logic: 19`
* *Architecture:* `api: 167`, `import: 34`
* *Defense:* `safety: 180`, `doc: 45`, `test: 164`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.000842
  * `Imports (Out-Degree: 20):` itertools, joblib, numpy, pytest, re, shutil, sklearn, sklearn.base...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1252.38 | **LOC:** 2380 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **27**; blast radius 0.315; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.003009
  * `Imports (Out-Degree: 15):` abc, contextlib, functools, itertools, numbers, numpy, sklearn._loss.loss, sklearn.base...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/tests/test_split.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1224.44 | **LOC:** 2133 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.5%), Complexity Load (formerly Cognitive Load) (28.6%), Connectivity (formerly Api Exposure) (11.2%)
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
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 425`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 76`
* *Architecture:* `io: 2`, `api: 79`, `import: 23`
* *Defense:* `safety: 149`, `doc: 4`, `test: 167`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` itertools, numpy, pandas, pytest, re, scipy, scipy.sparse, scipy.special...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `sklearn/metrics/_classification.py` -> Churn: **98.83%** | Cog Load: 53.8713% | Debt: 8.806%
- `sklearn/linear_model/_logistic.py` -> Churn: **87.93%** | Cog Load: 82.5021% | Debt: 9.2848%
- `sklearn/utils/estimator_checks.py` -> Churn: **77.89%** | Cog Load: 67.1192% | Debt: 8.8783%
- `sklearn/utils/validation.py` -> Churn: **72.31%** | Cog Load: 57.7487% | Debt: 17.4563%
- `sklearn/inspection/_plot/decision_boundary.py` -> Churn: **71.31%** | Cog Load: 65.0238% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sklearn/decomposition/_nmf.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1384.56
- `sklearn/neighbors/_base.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1218.32
- `sklearn/gaussian_process/kernels.py` -> **Jérémie du Boisberranger** (100.0% isolated ownership) | Magnitude: 1158.4
- `sklearn/mixture/tests/test_gaussian_mixture.py` -> **Olivier Grisel** (100.0% isolated ownership) | Magnitude: 1073.38
- `sklearn/datasets/_samples_generator.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1036.12

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `asv_benchmarks/benchmarks/datasets.py` -> **Severity: 0.907** (Bridge: 0.0091 * Flux: 99.9967%)
- `sklearn/base.py` -> **Severity: 0.892** (Bridge: 0.0089 * Flux: 100.0%)
- `sklearn/feature_extraction/text.py` -> **Severity: 0.657** (Bridge: 0.0066 * Flux: 100.0%)
- `sklearn/pipeline.py` -> **Severity: 0.45** (Bridge: 0.0045 * Flux: 100.0%)
- `sklearn/metrics/pairwise.py` -> **Severity: 0.371** (Bridge: 0.0037 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `asv_benchmarks/benchmarks/datasets.py` -> **Severity: 32.866** (Embedded: 0.3821 * Error Risk: 86.006%)
- `sklearn/utils/fixes.py` -> **Severity: 31.342** (Embedded: 0.3246 * Error Risk: 96.5628%)
- `asv_benchmarks/benchmarks/model_selection.py` -> **Severity: 27.923** (Embedded: 0.2838 * Error Risk: 98.381%)
- `sklearn/utils/validation.py` -> **Severity: 27.783** (Embedded: 0.3099 * Error Risk: 89.6392%)
- `sklearn/base.py` -> **Severity: 26.238** (Embedded: 0.2913 * Error Risk: 90.0709%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `asv_benchmarks/benchmarks/datasets.py` -> **Severity: 11229.8** (Blast Radius: 112.298 * Doc Risk: 100.0%)
- `sklearn/utils/fixes.py` -> **Severity: 4034.557** (Blast Radius: 52.113 * Doc Risk: 77.4194%)
- `asv_benchmarks/benchmarks/model_selection.py` -> **Severity: 3579.9** (Blast Radius: 35.799 * Doc Risk: 100.0%)
- `asv_benchmarks/benchmarks/decomposition.py` -> **Severity: 2885.1** (Blast Radius: 28.851 * Doc Risk: 100.0%)
- `sklearn/exceptions.py` -> **Severity: 2675.1** (Blast Radius: 26.751 * Doc Risk: 100.0%)

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
