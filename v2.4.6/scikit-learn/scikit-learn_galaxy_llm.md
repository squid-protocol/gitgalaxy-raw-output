# ARCHITECTURAL_BRIEF: scikit-learn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/scikit-learn` |
| **Timestamp** | `2026-08-03T19:40:54.494507+00:00` |
| **Scan Duration** | `8.46s` |
| **Git Branch** | `main` |
| **Git Commit** | `94af1dff678e8a7a6fc627b85a5489980c063331` |
| **Git Remote** | `https://github.com/scikit-learn/scikit-learn.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1072 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1788 |
| Analyzed Artifacts (Scanned) | 1150 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 638 |
| Total LOC | 247802 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 64.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3363 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1317 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7934 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 60 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1042 | 244984 | 90.6% |
| PLAINTEXT | 49 | 0 | 4.3% |
| SHELL | 11 | 550 | 1.0% |
| MARKDOWN | 10 | 0 | 0.9% |
| CPP | 8 | 299 | 0.7% |
| JAVASCRIPT | 6 | 162 | 0.5% |
| CSS | 6 | 844 | 0.5% |
| MAKEFILE | 4 | 127 | 0.3% |
| JSON | 4 | 35 | 0.3% |
| CSV | 4 | 372 | 0.3% |
| XML | 3 | 6 | 0.3% |
| HTML | 2 | 307 | 0.2% |
| BATCH | 1 | 116 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.618`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 868 | 75.5% |
| file_cluster_13 | 198 | 17.2% |
| file_cluster_0 | 12 | 1.0% |
| file_cluster_16 | 2 | 0.2% |
| file_cluster_9 | 2 | 0.2% |
| file_cluster_4 | 2 | 0.2% |
| file_cluster_2 | 2 | 0.2% |
| file_cluster_7 | 1 | 0.1% |
| file_cluster_11 | 1 | 0.1% |
| file_cluster_12 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 59 | 5.1% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 638*

**Composition by Extension & Reason:**
- `.rst`: 205x Excluded (Unsupported Extension: '.rst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 96x Excluded (Explicitly Denied Extension: '.png')
- `.gz`: 82x Excluded (Explicitly Denied Extension: '.gz')
- `no_extension`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 45 LOC), 1x Excluded (Machine-Generated Source Code Signature: 43 LOC)
- `.py`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1357 LOC), 1x Excluded (Machine-Generated Source Code Signature: 252 LOC)
- `.tp`: 20x Excluded (Unsupported Extension: '.tp'), 4x Unsupported Format (.tp)
- `.build`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.build)
- `.sh`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.lock')
- `.txt`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 81 LOC)
- `.template`: 7x Excluded (Unsupported Extension: '.template')
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.cpp`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 1x Excluded (Machine-Generated Source Code Signature: 240 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 9.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.2 | 2.5 | 1.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.4 | 0.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.1 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 41.2 | 7.9 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 32.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/templates/index.html` (Hits: 198)
- `build_tools/circle/build_doc.sh` (Hits: 115)
- `maint_tools/whats_missing.sh` (Hits: 47)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **datasets.py** (`asv_benchmarks/benchmarks/datasets.py`) — 398 inbound connections
2. **model_selection.py** (`asv_benchmarks/benchmarks/model_selection.py`) — 224 inbound connections
3. **linear_model.py** (`asv_benchmarks/benchmarks/linear_model.py`) — 214 inbound connections
4. **base.py** (`sklearn/base.py`) — 211 inbound connections
5. **metrics.py** (`asv_benchmarks/benchmarks/metrics.py`) — 179 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_search.py** (`sklearn/model_selection/tests/test_search.py`) — 44 outbound dependencies
2. **instance_generator.py** (`sklearn/utils/_test_common/instance_generator.py`) — 42 outbound dependencies
3. **estimator_checks.py** (`sklearn/utils/estimator_checks.py`) — 41 outbound dependencies
4. **test_validation.py** (`sklearn/model_selection/tests/test_validation.py`) — 38 outbound dependencies
5. **_testing.py** (`sklearn/utils/_testing.py`) — 38 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `check_consistent_length` (@ `sklearn/utils/validation.py`) -> Impact: **4982.2** | LOC: 1436
  * *Intent:* ----------
- `_initialize_nmf` (@ `sklearn/decomposition/_nmf.py`) -> Impact: **2941.1** | LOC: 1210
- `_validate_steps` (@ `sklearn/pipeline.py`) -> Impact: **2393.6** | LOC: 1071
- `_check_length_scale` (@ `sklearn/gaussian_process/kernels.py`) -> Impact: **2215.9** | LOC: 1156
- `fit` (@ `sklearn/preprocessing/_data.py`) -> Impact: **1964.7** | LOC: 934
- `get_feature_names_out` (@ `sklearn/preprocessing/_polynomial.py`) -> Impact: **1808.0** | LOC: 756
- `check_sample_weight_invariance` (@ `sklearn/metrics/tests/test_common.py`) -> Impact: **1762.1** | LOC: 1146
- `_grid_from_X` (@ `sklearn/inspection/_partial_dependence.py`) -> Impact: **1648.3** | LOC: 388
- `fit` (@ `sklearn/linear_model/_logistic.py`) -> Impact: **1528.5** | LOC: 392
- `test_check_array_links_to_imputer_doc_on` (@ `sklearn/utils/tests/test_validation.py`) -> Impact: **1452.7** | LOC: 2120

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `make_node` (@ `doc/sphinxext/sphinx_issues.py`) -> **O(2^N) [Recursive]**
- `_clone_parametrized` (@ `sklearn/base.py`) -> **O(2^N) [Recursive]**
- `fit` (@ `sklearn/calibration.py`) -> **O(2^N) [Recursive]**
- `fit` (@ `sklearn/covariance/_graph_lasso.py`) -> **O(2^N) [Recursive]**
  * *Intent:* ----------
- `fit` (@ `sklearn/decomposition/_lda.py`) -> **O(2^N) [Recursive]**
- `_initialize_nmf` (@ `sklearn/decomposition/_nmf.py`) -> **O(2^N) [Recursive]**
- `_cov` (@ `sklearn/discriminant_analysis.py`) -> **O(2^N) [Recursive]**
- `fit` (@ `sklearn/dummy.py`) -> **O(2^N) [Recursive]**
- `fit` (@ `sklearn/ensemble/_gb.py`) -> **O(2^N) [Recursive]**
- `fit` (@ `sklearn/ensemble/_stacking.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `get_build_type_[Truncated]` (@ `build_tools/circle/build_doc.sh`) -> DB Complexity: **385**
- `logged_prs` (@ `maint_tools/whats_missing.sh`) -> DB Complexity: **68**
- `_cov` (@ `sklearn/discriminant_analysis.py`) -> DB Complexity: **65**
- `_initialize_nmf` (@ `sklearn/decomposition/_nmf.py`) -> DB Complexity: **63**
- `_check_algorithm_metric` (@ `sklearn/neighbors/_base.py`) -> DB Complexity: **61**
- `_check_length_scale` (@ `sklearn/gaussian_process/kernels.py`) -> DB Complexity: **56**
- `init` (@ `sklearn/ensemble/_gb.py`) -> DB Complexity: **54**
  * *Intent:* # we take advantage that: y - prob = neg_gradient neg_g = neg_gradient.take(indices, axis=0) prob = y_ - neg_g K = loss.n_classes # numerator = negati...
- `fit` (@ `sklearn/dummy.py`) -> DB Complexity: **44**
- `get_feature_names_out` (@ `sklearn/preprocessing/_polynomial.py`) -> DB Complexity: **40**
- `fit` (@ `sklearn/linear_model/_logistic.py`) -> DB Complexity: **35**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sklearn/utils` | 62 | 22210.22 | 12.97% | 19.61% |
| `sklearn` | 18 | 11627.42 | 16.1% | 41.08% |
| `sklearn/utils/tests` | 44 | 9216.2 | 9.43% | 0.0% |
| `sklearn/linear_model` | 18 | 8190.94 | 15.77% | 39.42% |
| `sklearn/preprocessing` | 10 | 8051.02 | 15.88% | 24.79% |
| `sklearn/metrics/tests` | 9 | 7847.72 | 3.91% | 0.0% |
| `sklearn/tests` | 25 | 7375.64 | 4.64% | 0.0% |
| `sklearn/decomposition` | 14 | 6481.56 | 18.53% | 19.14% |
| `sklearn/linear_model/tests` | 19 | 5573.24 | 3.62% | 0.0% |
| `sklearn/model_selection` | 7 | 5398.02 | 18.46% | 75.97% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `asv_benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/decomposition.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/ensemble.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/linear_model.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/manifold.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `sklearn/dummy.py` -> **100.0%** Exposure
- `sklearn/neural_network/_stochastic_optimizers.py` -> **100.0%** Exposure
- `sklearn/utils/_encode.py` -> **100.0%** Exposure
- `sklearn/utils/_mocking.py` -> **100.0%** Exposure
- `sklearn/utils/_repr_html/common.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sklearn/compose/tests/test_column_transformer.py` -> **86** Orphaned Functions | **17** Duplicates
- `sklearn/preprocessing/tests/test_data.py` -> **101** Orphaned Functions | **0** Duplicates
- `sklearn/preprocessing/tests/test_encoders.py` -> **81** Orphaned Functions | **14** Duplicates
- `sklearn/metrics/tests/test_ranking.py` -> **80** Orphaned Functions | **5** Duplicates
- `sklearn/metrics/tests/test_classification.py` -> **68** Orphaned Functions | **12** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`sklearn/inspection/_plot/partial_dependence.py`** -> AI Confidence: **99.39%**
2. **`sklearn/linear_model/_logistic.py`** -> AI Confidence: **99.39%**
3. **`sklearn/neighbors/_base.py`** -> AI Confidence: **99.35%**
4. **`sklearn/utils/validation.py`** -> AI Confidence: **99.35%**
5. **`sklearn/utils/class_weight.py`** -> AI Confidence: **99.34%**
6. **`sklearn/linear_model/_cd_fast.pyx`** -> AI Confidence: **99.32%**
7. **`benchmarks/bench_pca_solvers.py`** -> AI Confidence: **99.31%**
8. **`benchmarks/bench_plot_randomized_svd.py`** -> AI Confidence: **99.31%**
9. **`benchmarks/bench_saga.py`** -> AI Confidence: **99.31%**
10. **`maint_tools/bump-dependencies-versions.py`** -> AI Confidence: **99.31%**
11. **`maint_tools/update_tracking_issue.py`** -> AI Confidence: **99.31%**
12. **`sklearn/cluster/_agglomerative.py`** -> AI Confidence: **99.31%**
13. **`sklearn/cluster/_hdbscan/hdbscan.py`** -> AI Confidence: **99.31%**
14. **`sklearn/cluster/_kmeans.py`** -> AI Confidence: **99.31%**
15. **`sklearn/cluster/_optics.py`** -> AI Confidence: **99.31%**
16. **`sklearn/compose/_target.py`** -> AI Confidence: **99.31%**
17. **`sklearn/covariance/_graph_lasso.py`** -> AI Confidence: **99.31%**
18. **`sklearn/covariance/_robust_covariance.py`** -> AI Confidence: **99.31%**
19. **`sklearn/datasets/_arff_parser.py`** -> AI Confidence: **99.31%**
20. **`sklearn/datasets/_lfw.py`** -> AI Confidence: **99.31%**
21. **`sklearn/datasets/_openml.py`** -> AI Confidence: **99.31%**
22. **`sklearn/datasets/_samples_generator.py`** -> AI Confidence: **99.31%**
23. **`sklearn/datasets/_svmlight_format_io.py`** -> AI Confidence: **99.31%**
24. **`sklearn/decomposition/_dict_learning.py`** -> AI Confidence: **99.31%**
25. **`sklearn/decomposition/_incremental_pca.py`** -> AI Confidence: **99.31%**
26. **`sklearn/decomposition/_lda.py`** -> AI Confidence: **99.31%**
27. **`sklearn/decomposition/_nmf.py`** -> AI Confidence: **99.31%**
28. **`sklearn/decomposition/_pca.py`** -> AI Confidence: **99.31%**
29. **`sklearn/decomposition/tests/test_fastica.py`** -> AI Confidence: **99.31%**
30. **`sklearn/discriminant_analysis.py`** -> AI Confidence: **99.31%**
31. **`sklearn/dummy.py`** -> AI Confidence: **99.31%**
32. **`sklearn/ensemble/_bagging.py`** -> AI Confidence: **99.31%**
33. **`sklearn/ensemble/_forest.py`** -> AI Confidence: **99.31%**
34. **`sklearn/ensemble/_gb.py`** -> AI Confidence: **99.31%**
35. **`sklearn/ensemble/_hist_gradient_boosting/binning.py`** -> AI Confidence: **99.31%**
36. **`sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py`** -> AI Confidence: **99.31%**
37. **`sklearn/ensemble/_hist_gradient_boosting/grower.py`** -> AI Confidence: **99.31%**
38. **`sklearn/externals/_numpydoc/docscrape.py`** -> AI Confidence: **99.31%**
39. **`sklearn/feature_extraction/_dict_vectorizer.py`** -> AI Confidence: **99.31%**
40. **`sklearn/feature_extraction/text.py`** -> AI Confidence: **99.31%**
41. **`sklearn/feature_selection/_from_model.py`** -> AI Confidence: **99.31%**
42. **`sklearn/gaussian_process/_gpc.py`** -> AI Confidence: **99.31%**
43. **`sklearn/gaussian_process/_gpr.py`** -> AI Confidence: **99.31%**
44. **`sklearn/impute/_base.py`** -> AI Confidence: **99.31%**
45. **`sklearn/impute/_iterative.py`** -> AI Confidence: **99.31%**
46. **`sklearn/inspection/_partial_dependence.py`** -> AI Confidence: **99.31%**
47. **`sklearn/inspection/_plot/decision_boundary.py`** -> AI Confidence: **99.31%**
48. **`sklearn/linear_model/_base.py`** -> AI Confidence: **99.31%**
49. **`sklearn/linear_model/_coordinate_descent.py`** -> AI Confidence: **99.31%**
50. **`sklearn/linear_model/_glm/_newton_solver.py`** -> AI Confidence: **99.31%**
51. **`sklearn/linear_model/_glm/tests/test_glm.py`** -> AI Confidence: **99.31%**
52. **`sklearn/linear_model/_least_angle.py`** -> AI Confidence: **99.31%**
53. **`sklearn/linear_model/_omp.py`** -> AI Confidence: **99.31%**
54. **`sklearn/linear_model/_ransac.py`** -> AI Confidence: **99.31%**
55. **`sklearn/linear_model/_ridge.py`** -> AI Confidence: **99.31%**
56. **`sklearn/linear_model/_sag.py`** -> AI Confidence: **99.31%**
57. **`sklearn/linear_model/_stochastic_gradient.py`** -> AI Confidence: **99.31%**
58. **`sklearn/linear_model/tests/test_logistic.py`** -> AI Confidence: **99.31%**
59. **`sklearn/linear_model/tests/test_ridge.py`** -> AI Confidence: **99.31%**
60. **`sklearn/linear_model/tests/test_sag.py`** -> AI Confidence: **99.31%**
61. **`sklearn/manifold/_locally_linear.py`** -> AI Confidence: **99.31%**
62. **`sklearn/manifold/_mds.py`** -> AI Confidence: **99.31%**
63. **`sklearn/manifold/_spectral_embedding.py`** -> AI Confidence: **99.31%**
64. **`sklearn/manifold/_t_sne.py`** -> AI Confidence: **99.31%**
65. **`sklearn/metrics/_classification.py`** -> AI Confidence: **99.31%**
66. **`sklearn/metrics/_plot/precision_recall_curve.py`** -> AI Confidence: **99.31%**
67. **`sklearn/metrics/_plot/tests/test_common_curve_display.py`** -> AI Confidence: **99.31%**
68. **`sklearn/metrics/_ranking.py`** -> AI Confidence: **99.31%**
69. **`sklearn/metrics/_regression.py`** -> AI Confidence: **99.31%**
70. **`sklearn/metrics/pairwise.py`** -> AI Confidence: **99.31%**
71. **`sklearn/metrics/tests/test_common.py`** -> AI Confidence: **99.31%**
72. **`sklearn/metrics/tests/test_pairwise_distances_reduction.py`** -> AI Confidence: **99.31%**
73. **`sklearn/metrics/tests/test_regression.py`** -> AI Confidence: **99.31%**
74. **`sklearn/mixture/_gaussian_mixture.py`** -> AI Confidence: **99.31%**
75. **`sklearn/model_selection/_plot.py`** -> AI Confidence: **99.31%**
76. **`sklearn/model_selection/_search.py`** -> AI Confidence: **99.31%**
77. **`sklearn/model_selection/_split.py`** -> AI Confidence: **99.31%**
78. **`sklearn/model_selection/_validation.py`** -> AI Confidence: **99.31%**
79. **`sklearn/neighbors/_classification.py`** -> AI Confidence: **99.31%**
80. **`sklearn/neighbors/tests/test_neighbors.py`** -> AI Confidence: **99.31%**
81. **`sklearn/neural_network/_multilayer_perceptron.py`** -> AI Confidence: **99.31%**
82. **`sklearn/pipeline.py`** -> AI Confidence: **99.31%**
83. **`sklearn/preprocessing/_data.py`** -> AI Confidence: **99.31%**
84. **`sklearn/preprocessing/_discretization.py`** -> AI Confidence: **99.31%**
85. **`sklearn/preprocessing/_encoders.py`** -> AI Confidence: **99.31%**
86. **`sklearn/preprocessing/_function_transformer.py`** -> AI Confidence: **99.31%**
87. **`sklearn/preprocessing/_label.py`** -> AI Confidence: **99.31%**
88. **`sklearn/preprocessing/_polynomial.py`** -> AI Confidence: **99.31%**
89. **`sklearn/preprocessing/_target_encoder.py`** -> AI Confidence: **99.31%**
90. **`sklearn/preprocessing/tests/test_discretization.py`** -> AI Confidence: **99.31%**
91. **`sklearn/preprocessing/tests/test_label.py`** -> AI Confidence: **99.31%**
92. **`sklearn/svm/_base.py`** -> AI Confidence: **99.31%**
93. **`sklearn/tests/test_docstring_parameters.py`** -> AI Confidence: **99.31%**
94. **`sklearn/tests/test_docstrings.py`** -> AI Confidence: **99.31%**
95. **`sklearn/tests/test_metaestimators_metadata_routing.py`** -> AI Confidence: **99.31%**
96. **`sklearn/tests/test_min_dependencies_readme.py`** -> AI Confidence: **99.31%**
97. **`sklearn/tree/_classes.py`** -> AI Confidence: **99.31%**
98. **`sklearn/tree/_export.py`** -> AI Confidence: **99.31%**
99. **`sklearn/tree/tests/test_monotonic_tree.py`** -> AI Confidence: **99.31%**
100. **`sklearn/utils/_array_api.py`** -> AI Confidence: **99.31%**
101. **`sklearn/utils/_indexing.py`** -> AI Confidence: **99.31%**
102. **`sklearn/utils/_metadata_requests.py`** -> AI Confidence: **99.31%**
103. **`sklearn/utils/_plotting.py`** -> AI Confidence: **99.31%**
104. **`sklearn/utils/_repr_html/estimator.py`** -> AI Confidence: **99.31%**
105. **`sklearn/utils/_testing.py`** -> AI Confidence: **99.31%**
106. **`sklearn/utils/discovery.py`** -> AI Confidence: **99.31%**
107. **`sklearn/utils/estimator_checks.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `sklearn/tests/test_naive_bayes.py` -> **0.0024%** Exposure
### Exploit Generation Surface
- `asv_benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/decomposition.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/ensemble.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/linear_model.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `asv_benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `doc/sphinxext/sphinx_issues.py` -> **100.0%** Exposure
- `sklearn/datasets/_twenty_newsgroups.py` -> **100.0%** Exposure
- `sklearn/neighbors/tests/test_ball_tree.py` -> **100.0%** Exposure
- `build_tools/circle/build_doc.sh` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `asv_benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/ensemble.py` -> **100.0%** Exposure
- `asv_benchmarks/benchmarks/linear_model.py` -> **100.0%** Exposure
- `benchmarks/bench_glmnet.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8625` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `build_tools/circle/build_doc.sh` (SHELL) -> Cumulative Risk: **925.48**
- **Archetype:** `file_cluster_11` (Distance: 12.452 IQR)
- **Magnitude:** 374.78 | **LOC:** 284 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `get_build_type_[Truncated]` (Impact: 239.9), `Anonymous_Block` (Impact: 12.8), `Anonymous_Block` (Impact: 7.2)

### 2. `asv_benchmarks/benchmarks/common.py` (PYTHON) -> Cumulative Risk: **798.92**
- **Archetype:** `file_cluster_13` (Distance: 9.859 IQR)
- **Magnitude:** 198.58 | **LOC:** 257 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `get_from_config` (Impact: 25.6), `setup_cache` (Impact: 18.5), `setup` (Impact: 11.3)

### 3. `maint_tools/whats_missing.sh` (SHELL) -> Cumulative Risk: **777.26**
- **Archetype:** `file_cluster_4` (Distance: 10.452 IQR)
- **Magnitude:** 48.62 | **LOC:** 62 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9333%)
- **Heaviest Functions:** `__global_context__` (Impact: 6.9), `logged_prs` (Impact: 6.5), `Anonymous_Block` (Impact: 4.2)

### 4. `sklearn/externals/_packaging/version.py` (PYTHON) -> Cumulative Risk: **772.19**
- **Archetype:** `file_cluster_0` (Distance: 11.45 IQR)
- **Magnitude:** 521.28 | **LOC:** 536 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 83.7), `_legacy_cmpkey` (Impact: 49.2), `__str__` (Impact: 29.1)

### 5. `sklearn/svm/src/newrand/newrand.h` (CPP) -> Cumulative Risk: **740.88**
- **Archetype:** `file_cluster_13` (Distance: 19.185 IQR)
- **Magnitude:** 55.96 | **LOC:** 60 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9762%)
- **Heaviest Functions:** `bounded_rand_int` (Impact: 31.2), `set_seed` (Impact: 2.1)

### 6. `sklearn/multioutput.py` (PYTHON) -> Cumulative Risk: **739.65**
- **Archetype:** `file_cluster_13` (Distance: 11.709 IQR)
- **Magnitude:** 1308.9 | **LOC:** 1326 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `fit` (Impact: 353.7), `partial_fit` (Impact: 304.4), `fit` (Impact: 208.3)

### 7. `sklearn/_loss/loss.py` (PYTHON) -> Cumulative Risk: **737.83**
- **Archetype:** `file_cluster_8` (Distance: 11.372 IQR)
- **Magnitude:** 643.06 | **LOC:** 1715 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `constant_to_optimal_zero` (Impact: 61.0), `__init__` (Impact: 59.7), `init_gradient_and_hessian` (Impact: 46.0)

### 8. `build_tools/wheels/build_wheels.sh` (SHELL) -> Cumulative Risk: **725.01**
- **Archetype:** `file_cluster_0` (Distance: 14.323 IQR)
- **Magnitude:** 52.34 | **LOC:** 58 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 29.6), `__global_context__` (Impact: 2.2)

### 9. `sklearn/utils/_metadata_requests.py` (PYTHON) -> Cumulative Risk: **722.88**
- **Archetype:** `file_cluster_13` (Distance: 12.287 IQR)
- **Magnitude:** 1387.1 | **LOC:** 1752 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_route_params` (Impact: 144.5), `_route_params` (Impact: 136.4), `_get_param_names` (Impact: 103.9)

### 10. `sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py` (PYTHON) -> Cumulative Risk: **710.48**
- **Archetype:** `file_cluster_8` (Distance: 11.2 IQR)
- **Magnitude:** 1102.48 | **LOC:** 2380 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (97.9586%)
- **Heaviest Functions:** `_check_categorical_features` (Impact: 193.3), `_check_interaction_cst` (Impact: 86.7), `_print_iteration_stats` (Impact: 59.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `sklearn/utils/validation.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.416 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.992 IQR)
- **Top Global Matches:** file_cluster_8: 11.416, file_cluster_7: 11.734, file_cluster_13: 11.78
- **Magnitude:** 5104.8 | **LOC:** 2942 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (20.2864%), Tech Debt (9.4247%)
**Top Internal Functions/Classes:**
  * `check_consistent_length` (Impact: 4982.2 | O(2^N) | DB: 1)
    * *Intent:* ----------
  * `_deprecate_positional_args` (Impact: 44.2 | O(N^5) | DB: 3)
  * `check_memory` (Impact: 17.9 | O(N^3))
  * `_assert_all_finite` (Impact: 1.1 | O(N^1))
  * `_assert_all_finite_element_wise` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 494`, `structural_boundaries: 220`, `args: 54`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 10`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 23`, `import: 23`
* *Defense:* `safety: 95`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.585
  * `Choke Point (Betweenness):` 0.002307 | `Ripple Effect (Closeness):` 0.319326
  * `Imports (Out-Degree: 7):` sklearn.utils._isfinite, operator, numbers, contextlib, sklearn.utils._tags, sklearn.utils._array_api, warnings, sklearn.utils.fixes...
  * `Imported By (In-Degree: 179):` (Excluded from Brief to save tokens)

### `sklearn/utils/estimator_checks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.083 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.867 IQR)
- **Top Global Matches:** file_cluster_8: 12.083, file_cluster_0: 12.264, file_cluster_7: 12.296
- **Magnitude:** 4336.64 | **LOC:** 5485 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 21.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (11.3074%), Tech Debt (12.5128%)
**Top Internal Functions/Classes:**
  * `check_classifiers_predictions` (Impact: 592.2 | O(2^N) | DB: 1)
  * `check_dict_unchanged` (Impact: 500.5 | O(N^5) | DB: 1)
  * `check_param_validation` (Impact: 229.9 | O(N^6))
  * `check_dataframe_column_names_consistency` (Impact: 162.8 | O(N^4) | DB: 1)
  * `check_parameters_default_constructible` (Impact: 131.0 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 818`, `structural_boundaries: 561`, `args: 150`, `func_start: 146`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 24`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 137`, `import: 44`
* *Defense:* `safety: 413`, `doc: 86`, `test: 166`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.8
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.014961
  * `Imports (Out-Degree: 19):` sklearn.linear_model._base, scipy.stats, sklearn.utils._testing, copy, contextlib, numbers, sklearn.metrics, sklearn.utils._tags...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `sklearn/decomposition/_nmf.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.009 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.324 IQR)
- **Top Global Matches:** file_cluster_8: 11.009, file_cluster_7: 11.248, file_cluster_13: 11.298
- **Magnitude:** 3277.32 | **LOC:** 2403 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (20.3052%), Tech Debt (8.3203%)
**Top Internal Functions/Classes:**
  * `_initialize_nmf` (Impact: 2941.1 | O(2^N) | DB: 63)
  * `_beta_divergence` (Impact: 108.2 | O(N^4))
  * `_check_init` (Impact: 32.8 | O(N^3))
    * *Intent:* """Trace of np.dot(X, Y.T). Parameters ---------- X : array-like First matrix. Y : array-like Second...
  * `_special_sparse_dot` (Impact: 21.0 | O(N^4))
  * `_beta_loss_to_float` (Impact: 5.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 118`, `args: 35`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 133`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 12`, `import: 18`
* *Defense:* `safety: 3`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001741
  * `Imports (Out-Degree: 9):` math, numbers, sklearn.utils._param_validation, time, sklearn._config, warnings, scipy, sklearn.exceptions...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/preprocessing/_data.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.91 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.712 IQR)
- **Top Global Matches:** file_cluster_8: 11.91, file_cluster_13: 12.013, file_cluster_7: 12.054
- **Magnitude:** 3140.2 | **LOC:** 3719 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (17.3812%), Tech Debt (91.0974%)
**Top Internal Functions/Classes:**
  * `fit` (Impact: 1964.7 | O(2^N) | DB: 33)
  * `scale` (Impact: 436.9 | O(2^N) | DB: 9)
    * *Intent:* # New array to avoid side-effects scale = xp.asarray(scale, copy=True) scale[constant_mask] = 1.0 re...
  * `partial_fit` (Impact: 209.4 | O(N^6) | DB: 17)
  * `transform` (Impact: 67.6 | O(N^5))
  * `inverse_transform` (Impact: 67.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 189`, `args: 70`, `func_start: 70`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 154`, `dead_code: 9`, `planned_debt: 2`, `duplicate_logic: 16`
* *Architecture:* `api: 47`, `import: 15`
* *Defense:* `safety: 8`, `doc: 122`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.343
  * `Choke Point (Betweenness):` 9e-05 | `Ripple Effect (Closeness):` 0.002785
  * `Imports (Out-Degree: 10):` sklearn.base, scipy.special, sklearn.utils, sklearn.utils.validation, sklearn.utils.sparsefuncs, sklearn.utils._sparse, numbers, scipy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sklearn/neighbors/_base.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.39 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.347 IQR)
- **Top Global Matches:** file_cluster_13: 12.39, file_cluster_8: 12.456, file_cluster_7: 12.72
- **Magnitude:** 2787.98 | **LOC:** 1399 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (56.3585%), Tech Debt (14.2037%)
**Top Internal Functions/Classes:**
  * `kneighbors` (Impact: 1171.7 | O(2^N) | DB: 13)
  * `_check_algorithm_metric` (Impact: 1044.5 | O(2^N) | DB: 61)
  * `sort_graph_by_row_values` (Impact: 122.5 | O(2^N))
  * `_get_weights` (Impact: 58.6 | O(N^5))
  * `_kneighbors_from_graph` (Impact: 37.5 | O(N^3))
    * *Intent:* ----------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 234`, `dead_code: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 22`
* *Defense:* `safety: 14`, `doc: 32`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.655
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008776
  * `Imports (Out-Degree: 10):` numbers, sklearn.metrics, sklearn.utils._param_validation, warnings, sklearn.utils.fixes, sklearn.neighbors._ball_tree, sklearn.metrics.pairwise, sklearn.exceptions...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `sklearn/pipeline.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.333 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.539 IQR)
- **Top Global Matches:** file_cluster_8: 11.333, file_cluster_13: 11.364, file_cluster_0: 11.444
- **Magnitude:** 2490.66 | **LOC:** 2173 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (13.0527%), Tech Debt (12.349%)
**Top Internal Functions/Classes:**
  * `_validate_steps` (Impact: 2393.6 | O(2^N) | DB: 10)
  * `set_output` (Impact: 8.3 | O(N^3))
  * `__init__` (Impact: 4.2 | O(N^2) | DB: 4)
  * `_final_estimator_has` (Impact: 3.1 | O(N^2))
  * `get_params` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 216`, `args: 70`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 20`, `dead_code: 2`, `planned_debt: 8`
* *Architecture:* `api: 37`, `import: 20`
* *Defense:* `safety: 44`, `doc: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.36
  * `Choke Point (Betweenness):` 0.004648 | `Ripple Effect (Closeness):` 0.220657
  * `Imports (Out-Degree: 16):` sklearn.utils._repr_html.estimator, copy, sklearn.utils._tags, sklearn.utils._param_validation, sklearn.utils._array_api, scipy, sklearn.exceptions, sklearn.svm...
  * `Imported By (In-Degree: 128):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_common.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.358 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.337 IQR)
- **Top Global Matches:** file_cluster_8: 10.358, file_cluster_7: 10.854, file_cluster_0: 10.923
- **Magnitude:** 2461.54 | **LOC:** 2803 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 24.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.9691%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_sample_weight_invariance` (Impact: 1762.1 | O(2^N) | DB: 1)
  * `test_sample_order_invariance` (Impact: 129.2 | O(N^5))
    * *Intent:* # test_not_symmetric_metric passes on a not symmetric metric # but fails on a symmetric metric
  * `test_classification_inf_nan_input` (Impact: 45.0 | O(N^3))
    * *Intent:* # non-regression test for: # https://github.com/scikit-learn/scikit-learn/issues/6809 [ ([np.nan, 1,...
  * `test_multioutput_regression_invariance_t` (Impact: 43.6 | O(N^4))
  * `test_continuous_classification_invarianc` (Impact: 38.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 136`, `args: 69`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 7`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 5`
* *Architecture:* `api: 83`, `import: 22`
* *Defense:* `safety: 38`, `doc: 20`, `test: 151`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00087
  * `Imports (Out-Degree: 11):` math, sklearn.utils._testing, sklearn.metrics, sklearn._config, sklearn.utils._array_api, sklearn.utils.fixes, sklearn.metrics.pairwise, sklearn.exceptions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/gaussian_process/kernels.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.239 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.022 IQR)
- **Top Global Matches:** file_cluster_8: 12.239, file_cluster_13: 12.279, file_cluster_0: 12.294
- **Magnitude:** 2426.26 | **LOC:** 2408 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (27.1038%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_length_scale` (Impact: 2215.9 | O(2^N) | DB: 56)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 283`, `args: 106`, `func_start: 106`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 122`
* *Architecture:* `api: 72`, `import: 12`
* *Defense:* `safety: 8`, `doc: 156`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.814
  * `Choke Point (Betweenness):` 0.000429 | `Ripple Effect (Closeness):` 0.15908
  * `Imports (Out-Degree: 5):` sklearn.base, scipy.special, sklearn.utils.validation, scipy.spatial.distance, math, sklearn.gaussian_process, numpy, collections...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `sklearn/externals/_arff.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_7` (Drift: 12.039 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.287 IQR)
- **Top Global Matches:** file_cluster_7: 12.039, file_cluster_8: 12.103, file_cluster_13: 12.125
- **Magnitude:** 2277.74 | **LOC:** 1108 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (15.5751%), Tech Debt (38.0246%)
**Top Internal Functions/Classes:**
  * `encode_data` (Impact: 566.9 | O(2^N) | DB: 4)
    * *Intent:* # ============================================================================= # INTERNAL =========...
  * `_decode_attribute` (Impact: 469.4 | O(2^N) | DB: 3)
  * `__init__` (Impact: 427.7 | O(2^N) | DB: 9)
    * *Intent:* '''.format(value_re=value_re)) # This captures (key, value) groups and will have an empty key/value ...
  * `_build_re_values` (Impact: 317.8 | O(2^N) | DB: 3)
  * `_encode_attribute` (Impact: 297.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 136`, `args: 46`, `func_start: 45`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 53`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 42`, `import: 5`
* *Defense:* `safety: 31`, `doc: 109`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.349
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001978
  * `Imports (Out-Degree: 0):` re, typing, typing_extensions, csv
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/feature_extraction/text.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.573 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.128 IQR)
- **Top Global Matches:** file_cluster_8: 11.573, file_cluster_13: 11.656, file_cluster_7: 11.789
- **Magnitude:** 2176.06 | **LOC:** 2143 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (19.9853%), Tech Debt (90.4473%)
**Top Internal Functions/Classes:**
  * `_check_stop_list` (Impact: 974.1 | O(2^N) | DB: 15)
  * `_count_vocab` (Impact: 789.0 | O(2^N) | DB: 16)
  * `_limit_features` (Impact: 87.6 | O(N^4))
  * `transform` (Impact: 44.2 | O(2^N))
  * `fit` (Impact: 20.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 152`, `args: 50`, `func_start: 50`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 103`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 1`, `api: 30`, `import: 21`
* *Defense:* `safety: 22`, `doc: 84`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.181
  * `Choke Point (Betweenness):` 0.0054 | `Ripple Effect (Closeness):` 0.250954
  * `Imports (Out-Degree: 9):` operator, array, numbers, sklearn.utils._param_validation, sklearn.feature_extraction._hash, warnings, sklearn.utils.fixes, sklearn.feature_extraction.text...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_classification.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.534 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.114 IQR)
- **Top Global Matches:** file_cluster_8: 11.534, file_cluster_0: 11.864, file_cluster_7: 11.93
- **Magnitude:** 2000.02 | **LOC:** 3847 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 30.8%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (3.5924%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test__check_targets` (Impact: 707.6 | O(N^6) | DB: 1)
  * `test_prf_warnings` (Impact: 122.9 | O(N^3) | DB: 3)
    * *Intent:* # if zero_division = nan, check that all metrics are nan and exit if np.isnan(zero_division): for me...
  * `test_multilabel_jaccard_score` (Impact: 68.7 | O(N^4))
  * `test_multilabel_confusion_matrix_errors` (Impact: 49.9 | O(N^3))
    * *Intent:* # test support for labels with samplewise cm = multilabel_confusion_matrix(y_true, y_pred, labels=[2...
  * `test_matthews_corrcoef_against_jurman` (Impact: 43.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 393`, `args: 122`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 27`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 12`, `orphaned_logic: 68`
* *Architecture:* `api: 122`, `import: 27`
* *Defense:* `safety: 197`, `doc: 86`, `test: 477`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` scipy.stats, sklearn.utils._mocking, sklearn.utils._testing, sklearn.metrics, warnings, sklearn.utils._array_api, sklearn.utils.fixes, pandas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/preprocessing/_polynomial.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.014 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.002 IQR)
- **Top Global Matches:** file_cluster_8: 11.014, file_cluster_13: 11.134, file_cluster_7: 11.318
- **Magnitude:** 1971.78 | **LOC:** 1258 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (38.3247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_feature_names_out` (Impact: 1808.0 | O(2^N) | DB: 40)
  * `_create_expansion` (Impact: 21.8 | O(N^3))
  * `powers_` (Impact: 7.7 | O(N^3))
  * `__init__` (Impact: 1.6 | O(N^2))
  * `_combinations` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 76`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 106`, `dead_code: 2`
* *Architecture:* `api: 10`, `import: 16`
* *Defense:* `safety: 7`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.288
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00087
  * `Imports (Out-Degree: 7):` itertools, scipy.special, sklearn.base, sklearn.utils, sklearn.utils._mask, sklearn.utils.validation, numbers, scipy...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/utils/tests/test_estimator_checks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.235 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.199 IQR)
- **Top Global Matches:** file_cluster_13: 12.235, file_cluster_8: 12.301, file_cluster_0: 12.444
- **Magnitude:** 1905.16 | **LOC:** 1788 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (23.7423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_check_estimator_sparse_data` (Impact: 899.0 | O(N^5) | DB: 18)
  * `fit` (Impact: 49.2 | O(N^5) | DB: 2)
  * `fit` (Impact: 40.2 | O(N^4) | DB: 3)
  * `set_params` (Impact: 26.4 | O(2^N) | DB: 4)
  * `set_params` (Impact: 26.3 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 419`, `args: 154`, `func_start: 153`, `class_start: 53`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 116`, `dead_code: 3`, `fragile_debt: 3`, `duplicate_logic: 62`, `orphaned_logic: 16`
* *Architecture:* `io: 3`, `api: 169`, `import: 37`
* *Defense:* `safety: 68`, `doc: 42`, `test: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` sklearn.utils._testing, numbers, sklearn.utils._param_validation, warnings, sklearn.utils._test_common.instance_generator, sklearn.utils.fixes, pandas, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/linear_model/_logistic.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.65 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.853 IQR)
- **Top Global Matches:** file_cluster_8: 11.65, file_cluster_13: 11.889, file_cluster_7: 12.029
- **Magnitude:** 1870.46 | **LOC:** 2355 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (44.8521%), Tech Debt (18.1375%)
**Top Internal Functions/Classes:**
  * `fit` (Impact: 1528.5 | O(2^N) | DB: 35)
  * `score` (Impact: 50.2 | O(2^N))
  * `predict_proba` (Impact: 21.4 | O(2^N))
  * `__sklearn_tags__` (Impact: 14.3 | O(2^N) | DB: 2)
  * `_get_scorer` (Impact: 10.7 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 93`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 193`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 26`
* *Defense:* `safety: 8`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.289
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001741
  * `Imports (Out-Degree: 20):` sklearn.linear_model._base, numbers, sklearn.svm._base, sklearn.metrics, sklearn.utils._param_validation, sklearn.utils._array_api, warnings, sklearn.utils.fixes...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/tests/test_validation.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.342 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.354 IQR)
- **Top Global Matches:** file_cluster_8: 11.342, file_cluster_13: 11.61, file_cluster_0: 11.654
- **Magnitude:** 1835.46 | **LOC:** 2746 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (4.971%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `partial_fit` (Impact: 908.5 | O(N^6) | DB: 21)
  * `test_validation_curve` (Impact: 540.2 | O(N^6) | DB: 6)
  * `test_passed_unrequested_metadata` (Impact: 36.4 | O(N^3))
  * `test_validation_functions_routing` (Impact: 25.3 | O(N^3) | DB: 1)
  * `test_learning_curve_some_failing_fits_wa` (Impact: 18.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 316`, `args: 128`, `func_start: 116`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 58`, `dead_code: 5`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 115`, `import: 40`
* *Defense:* `safety: 113`, `doc: 38`, `test: 225`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` sklearn.multiclass, sklearn.utils._mocking, sklearn.utils._testing, sklearn.metrics, time, warnings, sklearn.utils._array_api, sklearn.utils.fixes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/utils/tests/test_validation.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.749 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.844 IQR)
- **Top Global Matches:** file_cluster_8: 11.749, file_cluster_0: 11.876, file_cluster_13: 12.023
- **Magnitude:** 1681.18 | **LOC:** 2383 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (9.7734%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_check_array_links_to_imputer_doc_on` (Impact: 1452.7 | O(N^4) | DB: 5)
  * `test_ordering` (Impact: 18.2 | O(N^4))
    * *Intent:* # We need to check each validation utility, because a 'copy' without # 'order=K' will kill the order...
  * `test_memmap` (Impact: 11.1 | O(N^3))
  * `test_as_float_array` (Impact: 9.8 | O(N^2))
  * `test_check_array_allow_nd_errors` (Impact: 9.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 323`, `structural_boundaries: 384`, `args: 115`, `func_start: 114`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 13`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 118`, `import: 29`
* *Defense:* `safety: 169`, `doc: 66`, `test: 418`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` operator, sklearn.utils._mocking, sklearn.utils._testing, numbers, sklearn._config, warnings, sklearn.utils._array_api, sklearn.utils.fixes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/inspection/_partial_dependence.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.325 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.853 IQR)
- **Top Global Matches:** file_cluster_8: 9.325, file_cluster_13: 9.662, file_cluster_7: 9.868
- **Magnitude:** 1659.68 | **LOC:** 780 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.1309%), Tech Debt (11.6111%)
**Top Internal Functions/Classes:**
  * `_grid_from_X` (Impact: 1648.3 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 49`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 18`
* *Defense:* `safety: 10`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001741
  * `Imports (Out-Degree: 11):` scipy.stats.mstats, sklearn.base, sklearn.utils, sklearn.utils.validation, sklearn.ensemble._gb, scipy, collections.abc, numpy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/impute/_base.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.496 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.426 IQR)
- **Top Global Matches:** file_cluster_13: 11.496, file_cluster_8: 11.536, file_cluster_7: 11.771
- **Magnitude:** 1656.98 | **LOC:** 1150 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (17.1162%), Tech Debt (34.9407%)
**Top Internal Functions/Classes:**
  * `transform` (Impact: 691.3 | O(2^N) | DB: 14)
  * `_validate_input` (Impact: 277.9 | O(N^6) | DB: 3)
  * `_dense_fit` (Impact: 175.1 | O(N^6))
  * `_sparse_fit` (Impact: 174.3 | O(N^6))
  * `_most_frequent` (Impact: 73.8 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 107`, `args: 28`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 76`, `dead_code: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 10`, `import: 16`
* *Defense:* `safety: 13`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.486
  * `Choke Point (Betweenness):` 0.000127 | `Ripple Effect (Closeness):` 0.004476
  * `Imports (Out-Degree: 8):` sklearn.base, sklearn.utils._mask, sklearn.utils.validation, sklearn.utils.sparsefuncs, sklearn.utils._sparse, numbers, scipy, numpy...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `sklearn/ensemble/_gb.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.011 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.095 IQR)
- **Top Global Matches:** file_cluster_13: 12.011, file_cluster_8: 12.058, file_cluster_7: 12.214
- **Magnitude:** 1623.56 | **LOC:** 2214 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (25.4712%), Tech Debt (66.2335%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 579.5 | O(2^N) | DB: 54)
    * *Intent:* # we take advantage that: y - prob = neg_gradient neg_g = neg_gradient.take(indices, axis=0) prob = ...
  * `fit` (Impact: 454.4 | O(2^N) | DB: 9)
  * `_compute_partial_dependence_recursion` (Impact: 90.9 | O(N^5) | DB: 3)
  * `_get_loss` (Impact: 42.4 | O(N^5) | DB: 3)
  * `_safe_divide` (Impact: 28.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 142`, `args: 47`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `state_mutation: 162`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 30`, `import: 22`
* *Defense:* `safety: 27`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003108
  * `Imports (Out-Degree: 13):` math, numbers, sklearn.utils._param_validation, time, sklearn.utils.stats, warnings, sklearn.exceptions, sklearn.dummy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/_search.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.768 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.556 IQR)
- **Top Global Matches:** file_cluster_13: 11.768, file_cluster_8: 11.931, file_cluster_0: 12.078
- **Magnitude:** 1615.44 | **LOC:** 2041 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 11.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (17.8075%), Tech Debt (96.901%)
**Top Internal Functions/Classes:**
  * `_yield_masked_array_for_each_param` (Impact: 1098.4 | O(2^N) | DB: 26)
  * `__init__` (Impact: 111.0 | O(N^6) | DB: 1)
  * `__init__` (Impact: 95.8 | O(N^6) | DB: 3)
  * `__iter__` (Impact: 56.3 | O(N^6))
    * *Intent:* # Reverse so most frequent cycling parameter comes first
  * `__getitem__` (Impact: 48.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 148`, `args: 41`, `func_start: 41`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 74`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `api: 21`, `import: 31`
* *Defense:* `safety: 32`, `doc: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.337
  * `Choke Point (Betweenness):` 0.000129 | `Ripple Effect (Closeness):` 0.003481
  * `Imports (Out-Degree: 18):` operator, scipy.stats, sklearn.utils._repr_html.estimator, numbers, copy, sklearn.utils._tags, sklearn.metrics, sklearn.utils._param_validation...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/_split.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.626 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.443 IQR)
- **Top Global Matches:** file_cluster_13: 11.626, file_cluster_7: 11.679, file_cluster_8: 11.691
- **Magnitude:** 1614.56 | **LOC:** 3072 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 30.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (14.3491%), Tech Debt (99.9992%)
**Top Internal Functions/Classes:**
  * `_iter_test_masks` (Impact: 363.8 | O(2^N) | DB: 15)
  * `_make_test_folds` (Impact: 248.9 | O(2^N))
  * `_validate_shuffle_split` (Impact: 186.9 | O(N^3))
  * `check_cv` (Impact: 87.2 | O(N^4))
  * `__init__` (Impact: 67.6 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 170`, `args: 69`, `func_start: 69`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 59`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 31`
* *Architecture:* `api: 47`, `import: 17`
* *Defense:* `safety: 14`, `doc: 116`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 9.7e-05 | `Ripple Effect (Closeness):` 0.017802
  * `Imports (Out-Degree: 7):` scipy.special, math, numbers, sklearn.utils._param_validation, sklearn.utils._array_api, warnings, abc, sklearn.utils...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/tests/test_search.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.666 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.397 IQR)
- **Top Global Matches:** file_cluster_8: 11.666, file_cluster_13: 11.961, file_cluster_0: 12.001
- **Magnitude:** 1541.96 | **LOC:** 2973 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (4.4138%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_SearchCV_with_fit_params` (Impact: 297.3 | O(N^4) | DB: 3)
  * `test_grid_search_cv_splits_consistency` (Impact: 111.0 | O(N^6) | DB: 1)
  * `test_grid_search_failing_classifier` (Impact: 80.8 | O(N^3))
  * `test_grid_search_cv_results` (Impact: 65.0 | O(N^4))
  * `test_search_cv_sample_weight_equivalence` (Impact: 55.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 460`, `args: 149`, `func_start: 147`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 27`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 6`, `duplicate_logic: 10`
* *Architecture:* `io: 3`, `api: 203`, `import: 44`
* *Defense:* `safety: 218`, `doc: 54`, `test: 333`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001741
  * `Imports (Out-Degree: 25):` scipy.stats, sklearn.utils._mocking, sklearn.utils._testing, sklearn.metrics, sklearn.compose, sklearn.model_selection._search, warnings, sklearn.utils._array_api...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/_coordinate_descent.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.481 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.582 IQR)
- **Top Global Matches:** file_cluster_8: 11.481, file_cluster_13: 11.672, file_cluster_7: 11.785
- **Magnitude:** 1486.36 | **LOC:** 3460 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 56.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (25.6797%), Tech Debt (98.7422%)
**Top Internal Functions/Classes:**
  * `fit` (Impact: 837.4 | O(2^N) | DB: 19)
  * `fit` (Impact: 192.0 | O(N^5) | DB: 8)
  * `fit` (Impact: 80.0 | O(2^N) | DB: 30)
  * `_set_order` (Impact: 45.0 | O(N^3))
    * *Intent:* """Change the order of X and y if necessary. Parameters ---------- X : {array-like, sparse matrix} o...
  * `_decision_function` (Impact: 21.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 134`, `args: 40`, `func_start: 40`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 181`, `dead_code: 3`, `planned_debt: 5`, `duplicate_logic: 21`
* *Architecture:* `io: 1`, `api: 23`, `import: 22`
* *Defense:* `safety: 15`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001741
  * `Imports (Out-Degree: 14):` sklearn.linear_model._base, numbers, sklearn.metrics, sklearn.utils._param_validation, warnings, sklearn.utils.sparsefuncs, scipy, functools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/base.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.423 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.736 IQR)
- **Top Global Matches:** file_cluster_13: 11.423, file_cluster_8: 11.524, file_cluster_7: 11.712
- **Magnitude:** 1461.46 | **LOC:** 1390 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (12.337%), Tech Debt (13.8196%)
**Top Internal Functions/Classes:**
  * `_clone_parametrized` (Impact: 1391.2 | O(2^N) | DB: 6)
  * `clone` (Impact: 9.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 171`, `args: 42`, `func_start: 42`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `planned_debt: 5`
* *Architecture:* `api: 34`, `import: 26`
* *Defense:* `safety: 20`, `doc: 80`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.666
  * `Choke Point (Betweenness):` 0.009163 | `Ripple Effect (Closeness):` 0.300424
  * `Imports (Out-Degree: 16):` sklearn.utils._repr_html.estimator, copy, numbers, sklearn.utils._tags, sklearn.metrics, sklearn.utils._pprint, sklearn.utils._param_validation, sklearn._config...
  * `Imported By (In-Degree: 211):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/tests/test_logistic.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.235 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.751 IQR)
- **Top Global Matches:** file_cluster_8: 11.235, file_cluster_0: 11.489, file_cluster_7: 11.647
- **Magnitude:** 1413.24 | **LOC:** 2880 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 45.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (3.8458%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_logistic_regression_path_convergenc` (Impact: 1132.8 | O(N^5) | DB: 8)
  * `test_check_solver_option` (Impact: 74.9 | O(N^3))
    * *Intent:* # only 'liblinear' solver for solver in ["liblinear"]: msg = f"The '{solver}' solver does not suppor...
  * `test_consistency_path` (Impact: 29.1 | O(N^4))
    * *Intent:* # Test that the path algorithm is consistent
  * `test_inconsistent_input` (Impact: 16.6 | O(N^2))
    * *Intent:* # Test that an exception is raised on inconsistent input
  * `test_nan` (Impact: 8.2 | O(N^2))
    * *Intent:* # Test proper NaN handling.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 250`, `args: 82`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 49`, `fragile_debt: 16`, `orphaned_logic: 11`
* *Architecture:* `io: 1`, `api: 79`, `import: 26`
* *Defense:* `safety: 122`, `doc: 48`, `test: 320`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` sklearn.multiclass, sklearn.utils._testing, sklearn.metrics, sklearn.linear_model._logistic, warnings, sklearn.utils._array_api, sklearn.utils.fixes, scipy.linalg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `sklearn/utils/_available_if.py` (PYTHON) | Magnitude: 42.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, encapsulation: 9, args: 6
- `sklearn/tests/test_common.py` (PYTHON) | Magnitude: 278.66 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 238, encapsulation: 75, structural_boundaries: 73, branch: 58
- `sklearn/tests/test_metadata_routing.py` (PYTHON) | Magnitude: 533.48 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 734, structural_boundaries: 228, test: 116, api: 100
- `sklearn/linear_model/_passive_aggressive.py` (PYTHON) | Magnitude: 181.7 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 168, encapsulation: 25, structural_boundaries: 24, state_mutation: 24
- `sklearn/utils/_tags.py` (PYTHON) | Magnitude: 45.68 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 16, doc: 14, safety: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `build_tools/circle/build_doc.sh` (SHELL) | Magnitude: 374.78 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 131, branch: 126, io: 115, state_mutation: 98

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `build_tools/circle/checkout_merge_commit.sh` (SHELL) | Magnitude: 34.1 | Delta: **0.248 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 16, reflection_metaprogramming: 12, io: 9, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `sklearn/linear_model/_base.py` (PYTHON) | Magnitude: 489.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 351, branch: 88, structural_boundaries: 76, state_mutation: 45
- `sklearn/cluster/tests/test_feature_agglomeration.py` (PYTHON) | Magnitude: 11.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 22, test: 12, safety: 10
- `examples/linear_model/plot_logistic_path.py` (PYTHON) | Magnitude: 18.84 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 13, import: 7, ml_traditional: 5
- `examples/linear_model/plot_sgd_iris.py` (PYTHON) | Magnitude: 5.86 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 14, import: 5, ml_traditional: 3
- `sklearn/preprocessing/_target_encoder.py` (PYTHON) | Magnitude: 539.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 273, state_mutation: 61, structural_boundaries: 54, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `sklearn/externals/array_api_compat/torch/_aliases.py` (PYTHON) | Magnitude: 1115.38 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 476, structural_boundaries: 185, branch: 134, encapsulation: 111
- `sklearn/externals/_packaging/_structures.py` (PYTHON) | Magnitude: 52.2 | Delta: **0.346 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 36, encapsulation: 22, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `doc/js/scripts/api-search.js` (JAVASCRIPT) | Magnitude: 13.64 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, args: 1, doc: 1, ui_framework: 1
- `doc/js/scripts/sg_plotly_resize.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.607 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 2, structural_boundaries: 1, args: 1, ui_framework: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `build_tools/linting.sh` (SHELL) | Magnitude: 142.04 | Delta: **0.263 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 57, branch: 48, indent_spaces: 36, debug_prints: 33
- `maint_tools/whats_missing.sh` (SHELL) | Magnitude: 48.62 | Delta: **0.421 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 47, structural_boundaries: 23, indent_tabs: 23, concurrency: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `sklearn/externals/_arff.py` (PYTHON) | Magnitude: 2277.74 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 451, branch: 165, structural_boundaries: 136, encapsulation: 115

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/text/plot_hashing_vs_dict_vectorizer.py` (PYTHON) | Magnitude: 34.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 28, state_mutation: 18, indent_spaces: 16, debug_prints: 15
- `sklearn/utils/_param_validation.py` (PYTHON) | Magnitude: 1113.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 415, structural_boundaries: 232, branch: 173, encapsulation: 141
- `sklearn/utils/_arpack.py` (PYTHON) | Magnitude: 3.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, doc: 2, args: 1
- `build_tools/shared.sh` (SHELL) | Magnitude: 234.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, branch: 37, safety_bypasses: 16, state_mutation: 15
- `sklearn/cluster/_bicluster.py` (PYTHON) | Magnitude: 307.16 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 269, state_mutation: 66, structural_boundaries: 59, encapsulation: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sklearn/svm/src/libsvm/svm.h` (CPP) | Magnitude: 17.38 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 83, structural_boundaries: 69, indent_tabs: 53, immutability_locks: 38
- `sklearn/svm/_libsvm.pxi` (PYTHON) | Magnitude: 16.22 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 57, dead_code: 9, structural_boundaries: 4, encapsulation: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `sklearn/linear_model/_base.py` -> Churn: **73.04%** | Cog Load: 12.2543% | Debt: 69.4303%
- `sklearn/calibration.py` -> Churn: **70.03%** | Cog Load: 11.6149% | Debt: 99.6311%
- `sklearn/model_selection/_split.py` -> Churn: **70.03%** | Cog Load: 14.3491% | Debt: 99.9992%
- `sklearn/linear_model/_coordinate_descent.py` -> Churn: **69.05%** | Cog Load: 25.6797% | Debt: 98.7422%
- `sklearn/model_selection/_search.py` -> Churn: **67.6%** | Cog Load: 17.8075% | Debt: 96.901%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sklearn/decomposition/_nmf.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 3277.32
- `sklearn/neighbors/_base.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 2787.98
- `sklearn/gaussian_process/kernels.py` -> **Jérémie du Boisberranger** (100.0% isolated ownership) | Magnitude: 2426.26
- `sklearn/externals/_numpydoc/docscrape.py` -> **Dea María Léon** (100.0% isolated ownership) | Magnitude: 1242.52
- `sklearn/dummy.py` -> **Arthur Lacote** (100.0% isolated ownership) | Magnitude: 1205.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `sklearn/feature_extraction/text.py` -> **Severity: 0.5** (Bridge: 0.0054 * Flux: 92.5983%)
- `sklearn/base.py` -> **Severity: 0.3** (Bridge: 0.0092 * Flux: 32.7944%)
- `sklearn/utils/_testing.py` -> **Severity: 0.295** (Bridge: 0.0031 * Flux: 95.8765%)
- `asv_benchmarks/benchmarks/metrics.py` -> **Severity: 0.233** (Bridge: 0.0041 * Flux: 57.46%)
- `sklearn/utils/_array_api.py` -> **Severity: 0.176** (Bridge: 0.004 * Flux: 44.2259%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `sklearn/utils/_unique.py` -> **Severity: 15.486** (Embedded: 0.1976 * Error Risk: 78.3871%)
- `sklearn/utils/_bunch.py` -> **Severity: 11.319** (Embedded: 0.1653 * Error Risk: 68.4615%)
- `sklearn/externals/array_api_extra/testing.py` -> **Severity: 8.79** (Embedded: 0.1184 * Error Risk: 74.2177%)
- `sklearn/utils/_available_if.py` -> **Severity: 7.791** (Embedded: 0.167 * Error Risk: 46.6667%)
- `sklearn/externals/array_api_compat/common/_helpers.py` -> **Severity: 4.617** (Embedded: 0.0769 * Error Risk: 60.0481%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `asv_benchmarks/benchmarks/datasets.py` -> **Severity: 11354.9** (Blast Radius: 113.549 * Doc Risk: 100.0%)
- `sklearn/utils/fixes.py` -> **Severity: 5261.2** (Blast Radius: 52.612 * Doc Risk: 100.0%)
- `sklearn/utils/_array_api.py` -> **Severity: 4345.4** (Blast Radius: 43.454 * Doc Risk: 100.0%)
- `asv_benchmarks/benchmarks/model_selection.py` -> **Severity: 3621.987** (Blast Radius: 36.224 * Doc Risk: 99.9886%)
- `asv_benchmarks/benchmarks/decomposition.py` -> **Severity: 2918.291** (Blast Radius: 29.183 * Doc Risk: 99.9997%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
