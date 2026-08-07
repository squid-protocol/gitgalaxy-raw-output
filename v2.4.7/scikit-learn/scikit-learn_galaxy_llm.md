# ARCHITECTURAL_BRIEF: scikit-learn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/scikit-learn` |
| **Timestamp** | `2026-08-07T04:02:06.059524+00:00` |
| **Scan Duration** | `7.83s` |
| **Git Branch** | `main` |
| **Git Commit** | `94af1dff678e8a7a6fc627b85a5489980c063331` |
| **Git Remote** | `https://github.com/scikit-learn/scikit-learn.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1072 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Volatility Index | 0.006 |
| % Scanned of codebase = | 64.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3301 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 9.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 23.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.2 | 2.5 | 1.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.3 | 0.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 11.8 | 0.0 | 0.0 |
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

- `check_consistent_length` (@ `sklearn/utils/validation.py`) -> Impact: **773.3** | LOC: 1436
  * *Intent:* ----------
- `test_check_array_links_to_imputer_doc_on` (@ `sklearn/utils/tests/test_validation.py`) -> Impact: **644.7** | LOC: 2120
- `_initialize_nmf` (@ `sklearn/decomposition/_nmf.py`) -> Impact: **472.0** | LOC: 1210
- `test_logistic_regression_path_convergenc` (@ `sklearn/linear_model/tests/test_logistic.py`) -> Impact: **460.8** | LOC: 2495
- `libsvm_sparse_train` (@ `sklearn/svm/_libsvm_sparse.pyx`) -> Impact: **401.3** | LOC: 427
- `_validate_steps` (@ `sklearn/pipeline.py`) -> Impact: **387.8** | LOC: 1071
- `_check_length_scale` (@ `sklearn/gaussian_process/kernels.py`) -> Impact: **366.1** | LOC: 1156
- `_score` (@ `sklearn/model_selection/_validation.py`) -> Impact: **344.4** | LOC: 697
- `check_sample_weight_invariance` (@ `sklearn/metrics/tests/test_common.py`) -> Impact: **341.4** | LOC: 1146
- `test_check_estimator_sparse_data` (@ `sklearn/utils/tests/test_estimator_checks.py`) -> Impact: **334.3** | LOC: 1040

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sklearn/utils` | 62 | 8701.52 | 13.0% | 21.22% |
| `sklearn/utils/tests` | 44 | 5641.8 | 9.38% | 0.0% |
| `sklearn/tests` | 25 | 4657.84 | 4.65% | 0.0% |
| `sklearn/metrics/tests` | 9 | 4163.32 | 3.83% | 0.0% |
| `sklearn/linear_model/tests` | 19 | 3750.94 | 3.7% | 0.0% |
| `sklearn` | 18 | 3734.52 | 16.08% | 41.11% |
| `sklearn/linear_model` | 18 | 3463.84 | 16.21% | 41.49% |
| `sklearn/model_selection/tests` | 8 | 2971.46 | 3.8% | 0.0% |
| `sklearn/preprocessing/tests` | 9 | 2424.68 | 3.12% | 0.0% |
| `sklearn/preprocessing` | 10 | 2421.12 | 15.9% | 25.29% |

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
- `sklearn/compose/tests/test_column_transformer.py` -> **87** Orphaned Functions | **25** Duplicates
- `sklearn/preprocessing/tests/test_data.py` -> **101** Orphaned Functions | **0** Duplicates
- `sklearn/preprocessing/tests/test_encoders.py` -> **81** Orphaned Functions | **14** Duplicates
- `sklearn/metrics/tests/test_ranking.py` -> **80** Orphaned Functions | **5** Duplicates
- `sklearn/metrics/tests/test_classification.py` -> **68** Orphaned Functions | **15** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8625` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `build_tools/linting.sh` (SHELL) -> Cumulative Risk: **716.98**
- **Archetype:** `file_cluster_4` (Distance: 12.146 IQR)
- **Magnitude:** 150.04 | **LOC:** 124 | **CtrlFlow:** 93.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (99.996%)
- **Heaviest Functions:** `__global_context__` (Impact: 37.6), `Anonymous_Block` (Impact: 7.5), `Anonymous_Block` (Impact: 7.4)

### 2. `build_tools/circle/build_doc.sh` (SHELL) -> Cumulative Risk: **680.7**
- **Archetype:** `file_cluster_11` (Distance: 12.514 IQR)
- **Magnitude:** 281.78 | **LOC:** 284 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.2956%), Safety Score (98.8967%)
- **Heaviest Functions:** `get_build_type_[Truncated]` (Impact: 143.9), `Anonymous_Block` (Impact: 12.8), `Anonymous_Block` (Impact: 7.2)

### 3. `build_tools/wheels/build_wheels.sh` (SHELL) -> Cumulative Risk: **640.57**
- **Archetype:** `file_cluster_0` (Distance: 14.323 IQR)
- **Magnitude:** 38.34 | **LOC:** 58 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9987%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 15.6), `__global_context__` (Impact: 2.2)

### 4. `sklearn/externals/_packaging/version.py` (PYTHON) -> Cumulative Risk: **624.99**
- **Archetype:** `file_cluster_0` (Distance: 11.45 IQR)
- **Magnitude:** 294.78 | **LOC:** 536 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (98.163%)
- **Heaviest Functions:** `__init__` (Impact: 34.3), `_legacy_cmpkey` (Impact: 17.2), `__str__` (Impact: 15.2)

### 5. `maint_tools/whats_missing.sh` (SHELL) -> Cumulative Risk: **621.42**
- **Archetype:** `file_cluster_4` (Distance: 10.461 IQR)
- **Magnitude:** 46.12 | **LOC:** 62 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9333%), Cognitive Load (99.6415%)
- **Heaviest Functions:** `__global_context__` (Impact: 6.9), `Anonymous_Block` (Impact: 5.2), `logged_prs` (Impact: 3.0)

### 6. `sklearn/svm/src/newrand/newrand.h` (CPP) -> Cumulative Risk: **599.78**
- **Archetype:** `file_cluster_13` (Distance: 19.185 IQR)
- **Magnitude:** 37.96 | **LOC:** 60 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9357%), Safety Score (93.2898%)
- **Heaviest Functions:** `bounded_rand_int` (Impact: 13.2), `set_seed` (Impact: 2.1)

### 7. `build_tools/shared.sh` (SHELL) -> Cumulative Risk: **596.17**
- **Archetype:** `file_cluster_8` (Distance: 11.852 IQR)
- **Magnitude:** 81.82 | **LOC:** 71 | **CtrlFlow:** 95.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9819%), Cognitive Load (99.3766%)
- **Heaviest Functions:** `get_dep` (Impact: 65.7)

### 8. `build_tools/wheels/test_wheels.sh` (SHELL) -> Cumulative Risk: **575.41**
- **Archetype:** `file_cluster_8` (Distance: 11.226 IQR)
- **Magnitude:** 20.56 | **LOC:** 31 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Safety Score (94.7324%)
- **Heaviest Functions:** `__global_context__` (Impact: 6.9), `Anonymous_Block` (Impact: 5.3)

### 9. `maint_tools/vendor_array_api_extra.sh` (SHELL) -> Cumulative Risk: **553.28**
- **Archetype:** `file_cluster_8` (Distance: 8.953 IQR)
- **Magnitude:** 5.54 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9978%), Safety Score (99.9744%), State Flux (99.3028%)
- **Heaviest Functions:** `__global_context__` (Impact: 2.2)

### 10. `maint_tools/vendor_array_api_compat.sh` (SHELL) -> Cumulative Risk: **549.2**
- **Archetype:** `file_cluster_8` (Distance: 8.951 IQR)
- **Magnitude:** 5.54 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9978%), Safety Score (99.9744%), State Flux (99.3028%)
- **Heaviest Functions:** `__global_context__` (Impact: 2.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `sklearn/utils/estimator_checks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.083 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.867 IQR)
- **Top Global Matches:** file_cluster_8: 12.083, file_cluster_0: 12.264, file_cluster_7: 12.296
- **Magnitude:** 1913.34 | **LOC:** 5485 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 21.4%
- **Risk Profile:** Cognitive Load (11.3074%), Tech Debt (12.5128%)
**Top Internal Functions/Classes:**
  * `check_dict_unchanged` (Impact: 185.3)
  * `check_classifiers_predictions` (Impact: 111.4)
  * `check_param_validation` (Impact: 69.7)
  * `check_dataframe_column_names_consistency` (Impact: 69.3)
  * `check_parameters_default_constructible` (Impact: 47.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 818`, `structural_boundaries: 561`, `args: 150`, `func_start: 146`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 24`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 137`, `import: 44`
* *Defense:* `safety: 413`, `doc: 86`, `test: 166`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.8
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.014961
  * `Imports (Out-Degree: 19):` sklearn.utils._test_common.instance_generator, sklearn.metrics.pairwise, pickle, sklearn.utils.validation, typing, re, contextlib, pandas...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_classification.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.519 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.109 IQR)
- **Top Global Matches:** file_cluster_8: 11.519, file_cluster_0: 11.849, file_cluster_7: 11.916
- **Magnitude:** 1098.82 | **LOC:** 3847 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (3.5944%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test__check_targets` (Impact: 248.6)
  * `test_prf_warnings` (Impact: 64.0)
    * *Intent:* # if zero_division = nan, check that all metrics are nan and exit if np.isnan(zero_division): for me...
  * `test_multilabel_jaccard_score` (Impact: 29.7)
  * `test_multilabel_confusion_matrix_errors` (Impact: 25.6)
    * *Intent:* # test support for labels with samplewise cm = multilabel_confusion_matrix(y_true, y_pred, labels=[2...
  * `test_matthews_corrcoef_against_jurman` (Impact: 22.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 393`, `args: 122`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 27`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 15`, `orphaned_logic: 68`
* *Architecture:* `api: 122`, `import: 27`
* *Defense:* `safety: 197`, `doc: 86`, `test: 477`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` sklearn.utils.validation, sklearn.metrics._classification, re, sklearn.calibration, pandas, some, scipy, sklearn.base...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/model_selection/tests/test_search.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.667 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.378 IQR)
- **Top Global Matches:** file_cluster_8: 11.667, file_cluster_13: 11.956, file_cluster_0: 11.996
- **Magnitude:** 1003.76 | **LOC:** 2973 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (4.3842%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_SearchCV_with_fit_params` (Impact: 138.9)
  * `test_grid_search_failing_classifier` (Impact: 44.5)
  * `test_grid_search_cv_splits_consistency` (Impact: 37.4)
  * `get_cand_scores` (Impact: 35.5)
  * `test_grid_search_cv_results` (Impact: 28.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 460`, `args: 149`, `func_start: 147`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 27`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 6`, `duplicate_logic: 28`
* *Architecture:* `io: 3`, `api: 203`, `import: 44`
* *Defense:* `safety: 218`, `doc: 54`, `test: 333`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001741
  * `Imports (Out-Degree: 25):` sklearn.metrics.pairwise, pickle, sklearn.utils.validation, re, io, pandas, sklearn.svm, sklearn.tests.metadata_routing_common...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/tree/tests/test_tree.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.966 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.519 IQR)
- **Top Global Matches:** file_cluster_8: 10.966, file_cluster_0: 11.171, file_cluster_13: 11.368
- **Magnitude:** 981.94 | **LOC:** 3074 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (2.9505%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_error` (Impact: 30.9)
  * `test_check_node_ndarray` (Impact: 23.3)
  * `check_min_weight_fraction_leaf` (Impact: 22.9)
    * *Intent:* """Test if leaves contain at least min_weight_fraction_leaf of the training set"""
  * `test_sparse_parameters` (Impact: 20.4)
  * `check_sparse_input` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 288`, `args: 119`, `func_start: 119`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 13`, `dead_code: 3`, `planned_debt: 10`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 217`, `import: 33`
* *Defense:* `safety: 103`, `doc: 58`, `test: 319`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00087
  * `Imports (Out-Degree: 13):` pickle, sklearn.utils.validation, joblib.numpy_pickle, re, io, sklearn.utils.stats, joblib, sklearn.utils._testing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/utils/tests/test_estimator_checks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.236 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.2 IQR)
- **Top Global Matches:** file_cluster_13: 12.236, file_cluster_8: 12.302, file_cluster_0: 12.445
- **Magnitude:** 968.26 | **LOC:** 1788 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (23.7592%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_check_estimator_sparse_data` (Impact: 334.3)
  * `fit` (Impact: 17.2)
  * `fit` (Impact: 16.7)
  * `test_check_set_params` (Impact: 14.6)
    * *Intent:* """Check set_params doesn't fail and sets the right values."""
  * `test_check_dont_overwrite_parameters` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 419`, `args: 155`, `func_start: 153`, `class_start: 53`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 116`, `dead_code: 3`, `fragile_debt: 3`, `duplicate_logic: 63`, `orphaned_logic: 16`
* *Architecture:* `io: 3`, `api: 169`, `import: 37`
* *Defense:* `safety: 68`, `doc: 42`, `test: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` sklearn.utils._test_common.instance_generator, importlib, sklearn.utils.validation, scipy.sparse, re, pandas, joblib, sklearn.svm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `maint_tools/update_tracking_issue.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.544 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.771 IQR)
- **Top Global Matches:** file_cluster_8: 8.544, file_cluster_13: 8.92, file_cluster_7: 9.296
- **Magnitude:** 920.24 | **LOC:** 190 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.4083%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 21`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `io: 7`, `api: 3`, `import: 7`
* *Defense:* `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, datetime, pathlib, defusedxml.ElementTree, github, warnings, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/gaussian_process/kernels.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.237 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.006 IQR)
- **Top Global Matches:** file_cluster_8: 12.237, file_cluster_13: 12.274, file_cluster_0: 12.289
- **Magnitude:** 911.46 | **LOC:** 2408 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.1575%), Tech Debt (13.8521%)
**Top Internal Functions/Classes:**
  * `_check_length_scale` (Impact: 366.1)
  * `theta` (Impact: 299.1)
  * `set_params` (Impact: 17.1)
  * `theta` (Impact: 9.3)
    * *Intent:* -------
  * `hyperparameters` (Impact: 5.6)
    * *Intent:* """Get parameters of this kernel. Parameters ---------- deep : bool, default=True If True, will retu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 283`, `args: 106`, `func_start: 106`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 122`, `duplicate_logic: 2`
* *Architecture:* `api: 72`, `import: 12`
* *Defense:* `safety: 8`, `doc: 156`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.814
  * `Choke Point (Betweenness):` 0.000429 | `Ripple Effect (Closeness):` 0.15908
  * `Imports (Out-Degree: 5):` sklearn.metrics.pairwise, numpy, sklearn.gaussian_process.kernels, scipy.spatial.distance, sklearn.utils.validation, sklearn.gaussian_process, collections, math...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `sklearn/utils/validation.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.399 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.991 IQR)
- **Top Global Matches:** file_cluster_8: 11.399, file_cluster_7: 11.72, file_cluster_13: 11.776
- **Magnitude:** 875.6 | **LOC:** 2942 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (20.5884%), Tech Debt (9.4247%)
**Top Internal Functions/Classes:**
  * `check_consistent_length` (Impact: 773.3)
    * *Intent:* ----------
  * `_deprecate_positional_args` (Impact: 16.2)
  * `_inner_deprecate_positional_args` (Impact: 12.1)
    * *Intent:* * will issue a warning when passed as a positional argument.
  * `check_memory` (Impact: 9.3)
  * `inner_f` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 494`, `structural_boundaries: 220`, `args: 54`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 8`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 23`, `import: 23`
* *Defense:* `safety: 95`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.585
  * `Choke Point (Betweenness):` 0.002307 | `Ripple Effect (Closeness):` 0.319326
  * `Imports (Out-Degree: 7):` sklearn.utils.validation, scipy.sparse, sklearn.utils._isfinite, contextlib, pandas, joblib, sklearn.svm, numbers...
  * `Imported By (In-Degree: 179):` (Excluded from Brief to save tokens)

### `sklearn/utils/tests/test_validation.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.749 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.844 IQR)
- **Top Global Matches:** file_cluster_8: 11.749, file_cluster_0: 11.876, file_cluster_13: 12.023
- **Magnitude:** 850.28 | **LOC:** 2383 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (9.7734%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_check_array_links_to_imputer_doc_on` (Impact: 644.7)
  * `test_ordering` (Impact: 7.8)
    * *Intent:* # We need to check each validation utility, because a 'copy' without # 'order=K' will kill the order...
  * `test_as_float_array` (Impact: 7.2)
  * `test_check_array_allow_nd_errors` (Impact: 6.2)
  * `test_memmap` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 323`, `structural_boundaries: 384`, `args: 115`, `func_start: 114`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 13`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 118`, `import: 29`
* *Defense:* `safety: 169`, `doc: 66`, `test: 418`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` sklearn.utils.validation, scipy.sparse, tempfile, sklearn.metrics.tests.test_score_objects, re, pandas, sklearn.svm, sklearn.utils._testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/preprocessing/_data.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.903 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.71 IQR)
- **Top Global Matches:** file_cluster_8: 11.903, file_cluster_13: 12.005, file_cluster_7: 12.047
- **Magnitude:** 830.9 | **LOC:** 3719 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (17.5613%), Tech Debt (96.0747%)
**Top Internal Functions/Classes:**
  * `fit` (Impact: 320.7)
  * `scale` (Impact: 71.8)
    * *Intent:* # New array to avoid side-effects scale = xp.asarray(scale, copy=True) scale[constant_mask] = 1.0 re...
  * `partial_fit` (Impact: 64.0)
  * `transform` (Impact: 23.6)
  * `inverse_transform` (Impact: 23.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 189`, `args: 70`, `func_start: 70`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 154`, `dead_code: 9`, `planned_debt: 2`, `duplicate_logic: 19`
* *Architecture:* `api: 47`, `import: 15`
* *Defense:* `safety: 8`, `doc: 122`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.343
  * `Choke Point (Betweenness):` 9e-05 | `Ripple Effect (Closeness):` 0.002785
  * `Imports (Out-Degree: 10):` sklearn.utils._sparse, numpy, sklearn.utils.sparsefuncs_fast, sklearn.metrics.pairwise, sklearn.utils.validation, sklearn.utils._array_api, sklearn.utils._param_validation, sklearn.utils.extmath...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/tests/test_validation.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.343 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.354 IQR)
- **Top Global Matches:** file_cluster_8: 11.343, file_cluster_13: 11.611, file_cluster_0: 11.655
- **Magnitude:** 810.16 | **LOC:** 2746 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (4.9894%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `partial_fit` (Impact: 310.3)
  * `test_validation_curve` (Impact: 180.8)
  * `test_passed_unrequested_metadata` (Impact: 19.1)
  * `test_validation_functions_routing` (Impact: 14.9)
  * `test_learning_curve_some_failing_fits_wa` (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 316`, `args: 128`, `func_start: 116`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 58`, `dead_code: 5`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 115`, `import: 40`
* *Defense:* `safety: 113`, `doc: 38`, `test: 225`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` time, sklearn.utils.validation, scipy.sparse, tempfile, re, sklearn.metrics._scorer, pandas, sklearn.svm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/tests/test_pipeline.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.038 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.129 IQR)
- **Top Global Matches:** file_cluster_8: 12.038, file_cluster_13: 12.212, file_cluster_0: 12.213
- **Magnitude:** 777.1 | **LOC:** 2551 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (3.3234%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_step_name_validation` (Impact: 200.5)
  * `test_pipeline_invalid_parameters` (Impact: 24.9)
    * *Intent:* # Test the various init parameters of the pipeline in fit # method
  * `test_pipeline_raise_set_params_error` (Impact: 16.8)
  * `test_set_pipeline_steps` (Impact: 11.9)
  * `test_set_pipeline_step_passthrough` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 462`, `args: 167`, `func_start: 153`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 37`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 2`, `duplicate_logic: 25`
* *Architecture:* `api: 210`, `import: 34`
* *Defense:* `safety: 195`, `doc: 90`, `test: 312`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00087
  * `Imports (Out-Degree: 20):` time, sklearn.utils.validation, sklearn.kernel_approximation, tempfile, re, joblib, sklearn.svm, sklearn.tests.metadata_routing_common...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_common.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.347 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.337 IQR)
- **Top Global Matches:** file_cluster_8: 10.347, file_cluster_7: 10.844, file_cluster_0: 10.913
- **Magnitude:** 773.34 | **LOC:** 2803 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (3.9691%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_sample_weight_invariance` (Impact: 341.4)
  * `test_sample_order_invariance` (Impact: 49.5)
    * *Intent:* # test_not_symmetric_metric passes on a not symmetric metric # but fails on a symmetric metric
  * `test_classification_with_invalid_sample_` (Impact: 24.0)
  * `test_classification_inf_nan_input` (Impact: 23.0)
    * *Intent:* # non-regression test for: # https://github.com/scikit-learn/scikit-learn/issues/6809 [ ([np.nan, 1,...
  * `test_multioutput_regression_invariance_t` (Impact: 20.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 136`, `args: 69`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 7`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 5`
* *Architecture:* `api: 83`, `import: 22`
* *Defense:* `safety: 38`, `doc: 20`, `test: 151`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00087
  * `Imports (Out-Degree: 11):` sklearn.metrics.pairwise, sklearn.utils.validation, typing, re, sklearn.utils._testing, itertools, sklearn.exceptions, sklearn.preprocessing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `benchmarks/bench_hist_gradient_boosting_threading.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.051 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.692 IQR)
- **Top Global Matches:** file_cluster_8: 8.051, file_cluster_13: 8.723, file_cluster_7: 9.039
- **Magnitude:** 768.14 | **LOC:** 348 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2475%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 42`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 6`
* *Architecture:* `io: 1`, `api: 2`, `import: 16`
* *Defense:* `safety: 3`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` argparse, time, os, threadpoolctl, numpy, matplotlib, xgboost, catboost...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/preprocessing/tests/test_data.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.092 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.711 IQR)
- **Top Global Matches:** file_cluster_8: 11.092, file_cluster_0: 11.351, file_cluster_7: 11.588
- **Magnitude:** 767.66 | **LOC:** 2840 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (3.0774%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_quantile_transform_check_error` (Impact: 27.0)
  * `test_power_transformer_boxcox_strictly_p` (Impact: 23.8)
    * *Intent:* # method is boxcox pt = PowerTransformer(method="box-cox") pt.fit(np.abs(X_2d)) X_with_negatives = X...
  * `test_normalize` (Impact: 22.9)
  * `test_standard_scaler_numerical_stability` (Impact: 17.4)
    * *Intent:* # Test numerical stability of scaling # np.log(1e-5) is taken because of its floating point represen...
  * `test_robust_scaler_attributes` (Impact: 14.8)
    * *Intent:* # check consistent type of attributes if with_centering and sparse.issparse(X): pytest.skip("RobustS...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 294`, `args: 112`, `func_start: 112`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 101`
* *Architecture:* `api: 108`, `import: 22`
* *Defense:* `safety: 144`, `doc: 30`, `test: 369`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` sklearn.metrics.pairwise, re, sklearn.svm, sklearn.utils._testing, scipy, sklearn.base, sklearn.pipeline, sklearn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/neighbors/_base.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.389 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.347 IQR)
- **Top Global Matches:** file_cluster_13: 12.389, file_cluster_8: 12.456, file_cluster_7: 12.72
- **Magnitude:** 749.38 | **LOC:** 1399 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.4798%), Tech Debt (14.2037%)
**Top Internal Functions/Classes:**
  * `kneighbors` (Impact: 210.2)
  * `_check_algorithm_metric` (Impact: 161.1)
  * `sort_graph_by_row_values` (Impact: 26.6)
  * `_get_weights` (Impact: 20.5)
  * `_kneighbors_from_graph` (Impact: 19.5)
    * *Intent:* ----------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 234`, `dead_code: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 22`
* *Defense:* `safety: 14`, `doc: 32`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.655
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008776
  * `Imports (Out-Degree: 10):` sklearn.metrics.pairwise, sklearn.utils.validation, scipy.sparse, joblib, sklearn.base, numbers, itertools, sklearn.exceptions...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `sklearn/metrics/tests/test_ranking.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.669 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.389 IQR)
- **Top Global Matches:** file_cluster_8: 10.669, file_cluster_0: 11.13, file_cluster_7: 11.137
- **Magnitude:** 720.14 | **LOC:** 2613 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (3.2124%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_precision_recall_curve_toydata` (Impact: 47.9)
  * `test_roc_curve_toydata` (Impact: 38.5)
  * `check_lrap_error_raised` (Impact: 18.5)
  * `test_confusion_matrix_at_thresholds_impl` (Impact: 16.7)
  * `test_auc_score_non_binary_class` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 272`, `args: 102`, `func_start: 102`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 14`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 5`, `orphaned_logic: 80`
* *Architecture:* `api: 91`, `import: 18`
* *Defense:* `safety: 109`, `doc: 54`, `test: 338`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` sklearn.utils.validation, re, some, sklearn.utils._testing, scipy, sklearn.metrics._ranking, sklearn, sklearn.utils.extmath...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/decomposition/_nmf.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.009 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.324 IQR)
- **Top Global Matches:** file_cluster_8: 11.009, file_cluster_7: 11.248, file_cluster_13: 11.298
- **Magnitude:** 716.02 | **LOC:** 2403 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.3052%), Tech Debt (8.3203%)
**Top Internal Functions/Classes:**
  * `_initialize_nmf` (Impact: 472.0)
  * `_beta_divergence` (Impact: 45.7)
  * `_check_init` (Impact: 16.8)
    * *Intent:* """Trace of np.dot(X, Y.T). Parameters ---------- X : array-like First matrix. Y : array-like Second...
  * `_special_sparse_dot` (Impact: 9.0)
  * `_beta_loss_to_float` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 118`, `args: 35`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 133`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 12`, `import: 18`
* *Defense:* `safety: 3`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001741
  * `Imports (Out-Degree: 9):` time, sklearn.utils.validation, scipy.sparse, scipy, sklearn.base, numbers, sklearn.utils._sparse, sklearn.utils.extmath...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sklearn/model_selection/tests/test_split.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.338 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.891 IQR)
- **Top Global Matches:** file_cluster_8: 11.338, file_cluster_0: 11.672, file_cluster_13: 11.791
- **Magnitude:** 710.54 | **LOC:** 2133 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (4.0765%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_kfold_valueerrors` (Impact: 48.6)
  * `test_group_kfold` (Impact: 38.2)
  * `test_leave_one_p_group_out` (Impact: 23.4)
  * `test_leave_one_p_group_out_error_on_fewe` (Impact: 22.4)
  * `test_cross_validator_with_default_params` (Impact: 16.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 270`, `args: 82`, `func_start: 82`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 19`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 74`
* *Architecture:* `io: 2`, `api: 79`, `import: 23`
* *Defense:* `safety: 149`, `doc: 8`, `test: 301`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` sklearn.utils.validation, scipy.sparse, re, pandas, sklearn.tests.metadata_routing_common, sklearn.utils._testing, sklearn.svm, scipy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/applications/wikipedia_principal_eigenvector.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.27 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.556 IQR)
- **Top Global Matches:** file_cluster_8: 9.27, file_cluster_13: 9.466, file_cluster_7: 9.734
- **Magnitude:** 709.35 | **LOC:** 229 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.3072%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 35`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 5`, `import: 9`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` time, os, datetime, numpy, urllib.request, sklearn.decomposition, pprint, scipy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/model_selection/_search.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.779 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.553 IQR)
- **Top Global Matches:** file_cluster_13: 11.779, file_cluster_8: 11.947, file_cluster_0: 12.086
- **Magnitude:** 697.44 | **LOC:** 2041 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 11.1%
- **Risk Profile:** Cognitive Load (17.6986%), Tech Debt (98.12%)
**Top Internal Functions/Classes:**
  * `_yield_masked_array_for_each_param` (Impact: 183.9)
  * `fit` (Impact: 59.4)
  * `_format_results` (Impact: 41.1)
  * `__init__` (Impact: 33.1)
  * `__init__` (Impact: 28.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 148`, `args: 41`, `func_start: 41`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 74`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `api: 23`, `import: 31`
* *Defense:* `safety: 32`, `doc: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.337
  * `Choke Point (Betweenness):` 0.000129 | `Ripple Effect (Closeness):` 0.003481
  * `Imports (Out-Degree: 18):` time, sklearn.utils.validation, re, sklearn.metrics._scorer, sklearn.base, numbers, sklearn, sklearn.model_selection._validation...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sklearn/linear_model/tests/test_logistic.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.235 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.751 IQR)
- **Top Global Matches:** file_cluster_8: 11.235, file_cluster_0: 11.489, file_cluster_7: 11.647
- **Magnitude:** 677.14 | **LOC:** 2880 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 45.0%
- **Risk Profile:** Cognitive Load (3.8458%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_logistic_regression_path_convergenc` (Impact: 460.8)
  * `test_check_solver_option` (Impact: 38.6)
    * *Intent:* # only 'liblinear' solver for solver in ["liblinear"]: msg = f"The '{solver}' solver does not suppor...
  * `test_consistency_path` (Impact: 13.5)
    * *Intent:* # Test that the path algorithm is consistent
  * `test_inconsistent_input` (Impact: 11.4)
    * *Intent:* # Test that an exception is raised on inconsistent input
  * `test_nan` (Impact: 5.6)
    * *Intent:* # Test proper NaN handling.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 250`, `args: 82`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 49`, `fragile_debt: 16`, `orphaned_logic: 11`
* *Architecture:* `io: 1`, `api: 79`, `import: 26`
* *Defense:* `safety: 122`, `doc: 48`, `test: 320`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` re, sklearn.svm, scipy, sklearn.base, sklearn.utils._testing, sklearn, itertools, sklearn.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/compose/tests/test_column_transformer.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.276 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.143 IQR)
- **Top Global Matches:** file_cluster_8: 11.276, file_cluster_0: 11.613, file_cluster_7: 11.752
- **Magnitude:** 659.68 | **LOC:** 2892 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (2.5797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_column_transformer_invalid_columns` (Impact: 20.7)
  * `test_column_transformer_dataframe` (Impact: 20.2)
  * `test_column_transformer_error_msg_1D` (Impact: 14.6)
  * `test_metadata_routing_error_for_column_t` (Impact: 13.0)
  * `test_column_transformer_empty_columns` (Impact: 12.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 382`, `args: 131`, `func_start: 116`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 25`, `orphaned_logic: 87`
* *Architecture:* `api: 120`, `import: 19`
* *Defense:* `safety: 247`, `doc: 66`, `test: 402`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` pickle, re, joblib, sklearn.tests.metadata_routing_common, sklearn.utils._testing, scipy, sklearn.base, sklearn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/datasets/tests/test_openml.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.283 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.7 IQR)
- **Top Global Matches:** file_cluster_8: 10.283, file_cluster_0: 10.685, file_cluster_7: 10.708
- **Magnitude:** 658.92 | **LOC:** 1637 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (2.7586%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_monkey_patch_webbased_functions` (Impact: 252.1)
    * *Intent:* # in combination with a regular cache directory, as the files that are # stored as cache should not ...
  * `_mock_urlopen` (Impact: 223.2)
  * `test_fetch_openml_verify_checksum` (Impact: 24.6)
    * *Intent:* # create a temporary modified arff file original_data_module = OPENML_TEST_DATA_MODULE + "." + f"id_...
  * `_mock_urlopen_shared` (Impact: 14.2)
  * `_mock_urlopen_data_list` (Impact: 13.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 220`, `args: 61`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 11`
* *Architecture:* `io: 14`, `api: 44`, `import: 18`
* *Defense:* `safety: 87`, `doc: 52`, `test: 191`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` os, importlib, numpy, sklearn.datasets._openml, scipy.sparse, sklearn.utils._optional_dependencies, functools, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sklearn/model_selection/_split.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.626 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.443 IQR)
- **Top Global Matches:** file_cluster_13: 11.626, file_cluster_7: 11.679, file_cluster_8: 11.691
- **Magnitude:** 626.36 | **LOC:** 3072 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (14.3491%), Tech Debt (99.9992%)
**Top Internal Functions/Classes:**
  * `_validate_shuffle_split` (Impact: 95.2)
  * `_iter_test_masks` (Impact: 86.5)
  * `_make_test_folds` (Impact: 49.0)
  * `check_cv` (Impact: 35.6)
  * `_build_repr` (Impact: 24.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 170`, `args: 69`, `func_start: 69`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 59`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 31`
* *Architecture:* `api: 47`, `import: 17`
* *Defense:* `safety: 14`, `doc: 116`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 9.7e-05 | `Ripple Effect (Closeness):` 0.017802
  * `Imports (Out-Degree: 7):` sklearn.utils.validation, numbers, sklearn, sklearn.utils.extmath, collections.abc, itertools, warnings, numpy...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `sklearn/tests/test_common.py` (PYTHON) | Magnitude: 155.66 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 238, encapsulation: 75, structural_boundaries: 73, branch: 58
- `sklearn/linear_model/_passive_aggressive.py` (PYTHON) | Magnitude: 79.9 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 168, encapsulation: 25, structural_boundaries: 24, state_mutation: 24
- `sklearn/utils/_tags.py` (PYTHON) | Magnitude: 24.88 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 16, doc: 14, safety: 10
- `sklearn/tests/test_metadata_routing.py` (PYTHON) | Magnitude: 445.18 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 734, structural_boundaries: 228, test: 116, api: 100
- `sklearn/utils/deprecation.py` (PYTHON) | Magnitude: 54.0 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 26, encapsulation: 19, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `build_tools/circle/build_doc.sh` (SHELL) | Magnitude: 281.78 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: branch: 148, indent_spaces: 131, io: 115, state_mutation: 101

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `build_tools/circle/checkout_merge_commit.sh` (SHELL) | Magnitude: 30.6 | Delta: **0.247 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 16, reflection_metaprogramming: 12, io: 9, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `sklearn/utils/_available_if.py` (PYTHON) | Magnitude: 28.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, encapsulation: 9, args: 6
- `sklearn/cluster/tests/test_feature_agglomeration.py` (PYTHON) | Magnitude: 10.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 22, test: 12, safety: 10
- `examples/linear_model/plot_logistic_path.py` (PYTHON) | Magnitude: 18.84 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 13, import: 7, ml_traditional: 5
- `examples/linear_model/plot_sgd_iris.py` (PYTHON) | Magnitude: 6.86 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 14, import: 5, ml_traditional: 3
- `sklearn/preprocessing/_target_encoder.py` (PYTHON) | Magnitude: 195.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 273, state_mutation: 61, structural_boundaries: 54, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `sklearn/externals/array_api_compat/torch/_aliases.py` (PYTHON) | Magnitude: 472.68 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 476, structural_boundaries: 185, branch: 134, encapsulation: 111
- `sklearn/externals/_packaging/_structures.py` (PYTHON) | Magnitude: 35.8 | Delta: **0.346 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 36, encapsulation: 22, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `doc/js/scripts/api-search.js` (JAVASCRIPT) | Magnitude: 13.64 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, args: 1, doc: 1, ui_framework: 1
- `doc/js/scripts/sg_plotly_resize.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.607 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 2, structural_boundaries: 1, args: 1, ui_framework: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `build_tools/linting.sh` (SHELL) | Magnitude: 150.04 | Delta: **0.271 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 57, branch: 56, indent_spaces: 36, debug_prints: 33
- `maint_tools/whats_missing.sh` (SHELL) | Magnitude: 46.12 | Delta: **0.43 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 47, structural_boundaries: 23, indent_tabs: 23, concurrency: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `sklearn/externals/_arff.py` (PYTHON) | Magnitude: 470.34 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 451, branch: 165, structural_boundaries: 136, encapsulation: 115

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/text/plot_hashing_vs_dict_vectorizer.py` (PYTHON) | Magnitude: 32.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 28, state_mutation: 18, indent_spaces: 16, debug_prints: 15
- `sklearn/utils/_param_validation.py` (PYTHON) | Magnitude: 540.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 415, structural_boundaries: 232, branch: 173, encapsulation: 141
- `sklearn/utils/_arpack.py` (PYTHON) | Magnitude: 3.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, doc: 2, args: 1
- `sklearn/cluster/_bicluster.py` (PYTHON) | Magnitude: 185.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 269, state_mutation: 66, structural_boundaries: 59, encapsulation: 47
- `sklearn/metrics/tests/test_dist_metrics.py` (PYTHON) | Magnitude: 151.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 226, test: 62, structural_boundaries: 61, api: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sklearn/svm/src/libsvm/svm.h` (CPP) | Magnitude: 17.38 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 83, structural_boundaries: 69, indent_tabs: 53, immutability_locks: 38
- `sklearn/svm/_libsvm.pxi` (PYTHON) | Magnitude: 16.22 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 57, dead_code: 9, structural_boundaries: 4, encapsulation: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `sklearn/linear_model/_base.py` -> Churn: **71.17%** | Cog Load: 19.6561% | Debt: 99.1221%
- `sklearn/calibration.py` -> Churn: **70.75%** | Cog Load: 11.6612% | Debt: 99.6311%
- `sklearn/model_selection/_split.py` -> Churn: **70.75%** | Cog Load: 14.3491% | Debt: 99.9992%
- `sklearn/model_selection/_search.py` -> Churn: **68.3%** | Cog Load: 17.6986% | Debt: 98.12%
- `sklearn/utils/_test_common/instance_generator.py` -> Churn: **68.3%** | Cog Load: 5.4658% | Debt: 82.5342%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `maint_tools/update_tracking_issue.py` -> **François Paugam** (100.0% isolated ownership) | Magnitude: 920.24
- `sklearn/gaussian_process/kernels.py` -> **Jérémie du Boisberranger** (100.0% isolated ownership) | Magnitude: 911.46
- `sklearn/neighbors/_base.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 749.38
- `sklearn/decomposition/_nmf.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 716.02
- `examples/applications/wikipedia_principal_eigenvector.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 709.35

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

- `asv_benchmarks/benchmarks/model_selection.py` -> **Severity: 19.961** (Embedded: 0.2924 * Error Risk: 68.2759%)
- `sklearn/exceptions.py` -> **Severity: 17.966** (Embedded: 0.2964 * Error Risk: 60.62%)
- `asv_benchmarks/benchmarks/metrics.py` -> **Severity: 16.569** (Embedded: 0.2672 * Error Risk: 61.9968%)
- `sklearn/feature_extraction/text.py` -> **Severity: 14.539** (Embedded: 0.251 * Error Risk: 57.9341%)
- `sklearn/utils/fixes.py` -> **Severity: 14.189** (Embedded: 0.334 * Error Risk: 42.479%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `asv_benchmarks/benchmarks/datasets.py` -> **Severity: 11354.9** (Blast Radius: 113.549 * Doc Risk: 100.0%)
- `asv_benchmarks/benchmarks/model_selection.py` -> **Severity: 3514.271** (Blast Radius: 36.224 * Doc Risk: 97.015%)
- `asv_benchmarks/benchmarks/decomposition.py` -> **Severity: 2901.24** (Blast Radius: 29.183 * Doc Risk: 99.4154%)
- `asv_benchmarks/benchmarks/ensemble.py` -> **Severity: 2064.865** (Blast Radius: 21.133 * Doc Risk: 97.7081%)
- `asv_benchmarks/benchmarks/linear_model.py` -> **Severity: 1718.3** (Blast Radius: 17.183 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
