# ARCHITECTURAL_BRIEF: networkx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/networkx` |
| **Timestamp** | `2026-08-03T19:39:18.480266+00:00` |
| **Scan Duration** | `2.92s` |
| **Git Branch** | `main` |
| **Git Commit** | `6628a781503211153d16f2a2ef184e75daba69e5` |
| **Git Remote** | `https://github.com/networkx/networkx.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 649 malicious artifacts.

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
| Total Artifacts | 970 |
| Analyzed Artifacts (Scanned) | 674 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 296 |
| Total LOC | 89089 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 69.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8346 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2835 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.3616 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 69 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 646 | 88768 | 95.8% |
| PLAINTEXT | 14 | 0 | 2.1% |
| MARKDOWN | 5 | 0 | 0.7% |
| JSON | 2 | 75 | 0.3% |
| JAVASCRIPT | 2 | 105 | 0.3% |
| CSS | 2 | 33 | 0.3% |
| MAKEFILE | 1 | 96 | 0.1% |
| XML | 1 | 0 | 0.1% |
| HTML | 1 | 12 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.966`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 459 | 68.1% |
| file_cluster_13 | 128 | 19.0% |
| file_cluster_0 | 51 | 7.6% |
| file_cluster_7 | 8 | 1.2% |
| file_cluster_17 | 6 | 0.9% |
| file_cluster_2 | 1 | 0.1% |
| file_cluster_6 | 1 | 0.1% |
| file_cluster_16 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 296*

**Composition by Extension & Reason:**
- `.rst`: 131x Excluded (Unsupported Extension: '.rst'), 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 156 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1071 LOC)
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 7 LOC), 2x Excluded (Machine-Generated Source Code Signature: 5 LOC)
- `.png`: 10x Excluded (Explicitly Denied Extension: '.png')
- `.bz2`: 5x Excluded (Explicitly Denied Extension: '.bz2')
- `.gz`: 4x Excluded (Explicitly Denied Extension: '.gz')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 40 LOC)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.edgelist`: 1x Excluded (Unsupported Extension: '.edgelist'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 2x Excluded (Explicitly Denied Extension: '.zip')
- `.geojson`: 2x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.a99`: 2x Excluded (Unsupported Extension: '.A99')
- `.b99`: 2x Excluded (Unsupported Extension: '.B99')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.7 | 9.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 10.3 | 0.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.7 | 5.1 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 32.5 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 76.4 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 93.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.2 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 79.6 | 7.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 59.5 | 94.4 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 46.1 | 1.2 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `networkx/utils/backends.py` (Hits: 7)
- `doc/Makefile` (Hits: 7)
- `networkx/readwrite/tests/test_gml.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **decorators.py** (`networkx/utils/decorators.py`) — 18 inbound connections
2. **generators.py** (`networkx/algorithms/bipartite/generators.py`) — 9 inbound connections
3. **classic.py** (`networkx/generators/classic.py`) — 8 inbound connections
4. **community.py** (`networkx/generators/community.py`) — 7 inbound connections
5. **weighted.py** (`networkx/algorithms/shortest_paths/weighted.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`networkx/algorithms/__init__.py`) — 75 outbound dependencies
2. **__init__.py** (`networkx/generators/__init__.py`) — 29 outbound dependencies
3. **backends.py** (`networkx/utils/backends.py`) — 22 outbound dependencies
4. **__init__.py** (`networkx/algorithms/centrality/__init__.py`) — 20 outbound dependencies
5. **lazy_imports.py** (`networkx/lazy_imports.py`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_call_if_any_backends_installed` (@ `networkx/utils/backends.py`) -> Impact: **4234.7** | LOC: 1019
- `escape` (@ `networkx/readwrite/gml.py`) -> Impact: **2246.2** | LOC: 549
- `draw_networkx_nodes` (@ `networkx/drawing/nx_pylab.py`) -> Impact: **2174.7** | LOC: 779
- `max_weight_matching` (@ `networkx/algorithms/matching.py`) -> Impact: **1277.7** | LOC: 774
- `procedure_P` (@ `networkx/algorithms/coloring/equitable_coloring.py`) -> Impact: **1146.3** | LOC: 247
- `test_display_edge_multiple_colors` (@ `networkx/drawing/tests/test_pylab.py`) -> Impact: **760.8** | LOC: 1360
- `lukes_partitioning` (@ `networkx/algorithms/community/lukes.py`) -> Impact: **712.2** | LOC: 157
- `syntactic_feasibility` (@ `networkx/algorithms/isomorphism/isomorphvf2.py`) -> Impact: **640.8** | LOC: 216
- `preflow_push_impl` (@ `networkx/algorithms/flow/preflowpush.py`) -> Impact: **599.0** | LOC: 270
- `boykov_kolmogorov_impl` (@ `networkx/algorithms/flow/boykovkolmogorov.py`) -> Impact: **490.9** | LOC: 188

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `k_components` (@ `networkx/algorithms/approximation/kcomponents.py`) -> **O(2^N) [Recursive]**
- `spanning_tree_distribution` (@ `networkx/algorithms/approximation/traveling_salesman.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Test to see if the ascent method found an integer solution or a fractional # solution. If it is integral then z_star is a nx.Graph, otherwise it is ...
- `color` (@ `networkx/algorithms/bipartite/basic.py`) -> **O(2^N) [Recursive]**
- `procedure_P` (@ `networkx/algorithms/coloring/equitable_coloring.py`) -> **O(2^N) [Recursive]**
- `lukes_partitioning` (@ `networkx/algorithms/community/lukes.py`) -> **O(2^N) [Recursive]**
- `match` (@ `networkx/algorithms/isomorphism/isomorphvf2.py`) -> **O(2^N) [Recursive]**
- `dfs_testing_recursive` (@ `networkx/algorithms/planarity.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # determine nesting graph
- `_select_starting_cell` (@ `networkx/generators/line.py`) -> **O(2^N) [Recursive]**
- `set_customers` (@ `networkx/generators/tests/test_internet_as_graphs.py`) -> **O(2^N) [Recursive]**
- `set_providers` (@ `networkx/generators/tests/test_internet_as_graphs.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `max_weight_matching` (@ `networkx/algorithms/matching.py`) -> DB Complexity: **27**
- `setup_class` (@ `networkx/readwrite/tests/test_graphml.py`) -> DB Complexity: **27**
- `draw_networkx_nodes` (@ `networkx/drawing/nx_pylab.py`) -> DB Complexity: **25**
- `_set_configs_from_environment` (@ `networkx/utils/backends.py`) -> DB Complexity: **22**
  * *Intent:* # Note: "networkx" is in `backend_info` but ignored in `backends` and `config.backends`. # It is valid to use "networkx" as a backend argument and in ...
- `lr_planarity` (@ `networkx/algorithms/planarity.py`) -> DB Complexity: **18**
- `__init__` (@ `networkx/algorithms/planarity.py`) -> DB Complexity: **18**
- `setup_class` (@ `networkx/algorithms/approximation/tests/test_traveling_salesman.py`) -> DB Complexity: **16**
- `__init__` (@ `networkx/generators/internet_as_graphs.py`) -> DB Complexity: **14**
  * *Intent:* """ if len(degs) == 0: return None s = sum(degs.values()) if s == 0: return seed.choice(list(degs.keys())) v = seed.random() * s
- `extended_barabasi_albert_graph` (@ `networkx/generators/random_graphs.py`) -> DB Complexity: **14**
- `setup_class` (@ `networkx/algorithms/centrality/tests/test_load_centrality.py`) -> DB Complexity: **13**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `networkx/algorithms` | 56 | 16933.08 | 14.37% | 8.06% |
| `networkx/algorithms/tests` | 58 | 9403.54 | 3.64% | 0.0% |
| `networkx/utils` | 10 | 7558.98 | 25.07% | 33.97% |
| `networkx/generators` | 29 | 6536.0 | 11.6% | 5.94% |
| `networkx/algorithms/isomorphism` | 9 | 6146.56 | 26.29% | 40.82% |
| `networkx/readwrite` | 13 | 5326.24 | 16.6% | 8.54% |
| `networkx/algorithms/flow` | 12 | 3635.02 | 16.51% | 15.74% |
| `networkx/generators/tests` | 29 | 3534.1 | 3.79% | 0.0% |
| `networkx/drawing` | 5 | 3494.52 | 12.79% | 11.03% |
| `networkx/algorithms/community` | 14 | 2970.54 | 15.25% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `benchmarks/benchmarks/benchmark_chordal.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_classes.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_harmonic_centrality.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_neighbors.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_regular.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `networkx/algorithms/components/biconnected.py` -> **100.0%** Exposure
- `networkx/algorithms/components/connected.py` -> **100.0%** Exposure
- `networkx/algorithms/components/strongly_connected.py` -> **100.0%** Exposure
- `networkx/algorithms/components/weakly_connected.py` -> **100.0%** Exposure
- `networkx/generators/random_clustered.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `networkx/algorithms/tests/test_distance_measures.py` -> **93** Orphaned Functions | **8** Duplicates
- `networkx/algorithms/tests/test_link_prediction.py` -> **8** Orphaned Functions | **81** Duplicates
- `networkx/algorithms/tests/test_simple_paths.py` -> **64** Orphaned Functions | **15** Duplicates
- `networkx/algorithms/tests/test_dag.py` -> **59** Orphaned Functions | **8** Duplicates
- `networkx/algorithms/tests/test_similarity.py` -> **61** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`networkx/algorithms/similarity.py`** -> AI Confidence: **99.39%**
2. **`networkx/generators/lattice.py`** -> AI Confidence: **99.39%**
3. **`networkx/algorithms/connectivity/cuts.py`** -> AI Confidence: **99.34%**
4. **`networkx/algorithms/bipartite/projection.py`** -> AI Confidence: **99.32%**
5. **`examples/drawing/plot_knuth_miles.py`** -> AI Confidence: **99.31%**
6. **`networkx/algorithms/approximation/traveling_salesman.py`** -> AI Confidence: **99.31%**
7. **`networkx/algorithms/bipartite/matching.py`** -> AI Confidence: **99.31%**
8. **`networkx/algorithms/centrality/betweenness.py`** -> AI Confidence: **99.31%**
9. **`networkx/algorithms/connectivity/connectivity.py`** -> AI Confidence: **99.31%**
10. **`networkx/algorithms/connectivity/tests/test_edge_augmentation.py`** -> AI Confidence: **99.31%**
11. **`networkx/algorithms/dag.py`** -> AI Confidence: **99.31%**
12. **`networkx/algorithms/flow/preflowpush.py`** -> AI Confidence: **99.31%**
13. **`networkx/algorithms/tree/branchings.py`** -> AI Confidence: **99.31%**
14. **`networkx/algorithms/tree/mst.py`** -> AI Confidence: **99.31%**
15. **`networkx/drawing/nx_pylab.py`** -> AI Confidence: **99.31%**
16. **`networkx/generators/geometric.py`** -> AI Confidence: **99.31%**
17. **`networkx/generators/random_graphs.py`** -> AI Confidence: **99.31%**
18. **`networkx/readwrite/gml.py`** -> AI Confidence: **99.31%**
19. **`networkx/readwrite/graphml.py`** -> AI Confidence: **99.31%**
20. **`networkx/utils/backends.py`** -> AI Confidence: **99.31%**
21. **`networkx/utils/decorators.py`** -> AI Confidence: **99.31%**
22. **`networkx/algorithms/assortativity/connectivity.py`** -> AI Confidence: **99.29%**
23. **`networkx/algorithms/assortativity/neighbor_degree.py`** -> AI Confidence: **99.29%**
24. **`networkx/algorithms/flow/capacityscaling.py`** -> AI Confidence: **99.29%**
25. **`networkx/algorithms/shortest_paths/generic.py`** -> AI Confidence: **99.29%**
26. **`networkx/algorithms/summarization.py`** -> AI Confidence: **99.29%**
27. **`networkx/drawing/nx_latex.py`** -> AI Confidence: **99.29%**
28. **`networkx/relabel.py`** -> AI Confidence: **99.29%**
29. **`networkx/generators/atlas.py`** -> AI Confidence: **99.24%**
30. **`networkx/lazy_imports.py`** -> AI Confidence: **99.24%**
31. **`networkx/algorithms/approximation/kcomponents.py`** -> AI Confidence: **99.23%**
32. **`networkx/algorithms/community/bipartitions.py`** -> AI Confidence: **99.23%**
33. **`networkx/algorithms/cycles.py`** -> AI Confidence: **99.23%**
34. **`networkx/drawing/tests/test_pylab.py`** -> AI Confidence: **99.23%**
35. **`networkx/readwrite/json_graph/node_link.py`** -> AI Confidence: **99.23%**
36. **`networkx/utils/misc.py`** -> AI Confidence: **99.23%**
37. **`networkx/algorithms/centrality/group.py`** -> AI Confidence: **99.22%**
38. **`networkx/algorithms/community/modularity_max.py`** -> AI Confidence: **99.22%**
39. **`networkx/readwrite/text.py`** -> AI Confidence: **99.22%**
40. **`examples/drawing/plot_chess_masters.py`** -> AI Confidence: **99.2%**
41. **`networkx/algorithms/isomorphism/isomorphvf2.py`** -> AI Confidence: **99.2%**
42. **`networkx/algorithms/isomorphism/vf2pp.py`** -> AI Confidence: **99.2%**
43. **`networkx/algorithms/operators/product.py`** -> AI Confidence: **99.2%**
44. **`networkx/algorithms/sparsifiers.py`** -> AI Confidence: **99.2%**
45. **`networkx/algorithms/time_dependent.py`** -> AI Confidence: **99.2%**
46. **`networkx/readwrite/json_graph/adjacency.py`** -> AI Confidence: **99.2%**
47. **`doc/conf.py`** -> AI Confidence: **99.18%**
48. **`networkx/readwrite/tests/test_gml.py`** -> AI Confidence: **99.18%**
49. **`examples/algorithms/plot_subgraphs.py`** -> AI Confidence: **99.17%**
50. **`networkx/algorithms/assortativity/pairs.py`** -> AI Confidence: **99.17%**
51. **`networkx/algorithms/bipartite/extendability.py`** -> AI Confidence: **99.17%**
52. **`networkx/algorithms/centrality/closeness.py`** -> AI Confidence: **99.17%**
53. **`networkx/algorithms/centrality/voterank_alg.py`** -> AI Confidence: **99.17%**
54. **`networkx/algorithms/coloring/equitable_coloring.py`** -> AI Confidence: **99.17%**
55. **`networkx/algorithms/community/local.py`** -> AI Confidence: **99.17%**
56. **`networkx/algorithms/d_separation.py`** -> AI Confidence: **99.17%**
57. **`networkx/algorithms/distance_measures.py`** -> AI Confidence: **99.17%**
58. **`networkx/algorithms/flow/networksimplex.py`** -> AI Confidence: **99.17%**
59. **`networkx/algorithms/planar_drawing.py`** -> AI Confidence: **99.17%**
60. **`networkx/algorithms/regular.py`** -> AI Confidence: **99.17%**
61. **`networkx/generators/joint_degree_seq.py`** -> AI Confidence: **99.17%**
62. **`networkx/generators/sudoku.py`** -> AI Confidence: **99.17%**
63. **`networkx/readwrite/json_graph/cytoscape.py`** -> AI Confidence: **99.17%**
64. **`networkx/readwrite/pajek.py`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `benchmarks/benchmarks/benchmark_algorithms.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_shortest_path.py` -> **100.0%** Exposure
- `examples/algorithms/plot_iterated_dynamical_systems.py` -> **100.0%** Exposure
- `examples/subclass/plot_printgraph.py` -> **100.0%** Exposure
- `networkx/algorithms/approximation/connectivity.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `benchmarks/benchmarks/benchmark_algorithms.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_chordal.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_classes.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_neighbors.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_shortest_path.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2214` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `networkx/algorithms/isomorphism/isomorphvf2.py` (PYTHON) -> Cumulative Risk: **782.66**
- **Archetype:** `file_cluster_17` (Distance: 12.206 IQR)
- **Magnitude:** 1950.04 | **LOC:** 1263 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `syntactic_feasibility` (Impact: 640.8), `syntactic_feasibility` (Impact: 257.9), `__init__` (Impact: 231.9)

### 2. `networkx/algorithms/centrality/flow_matrix.py` (PYTHON) -> Cumulative Risk: **774.29**
- **Archetype:** `file_cluster_13` (Distance: 10.77 IQR)
- **Magnitude:** 132.9 | **LOC:** 131 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 14.1), `width` (Impact: 13.5), `flow_matrix_row` (Impact: 11.3)

### 3. `networkx/utils/misc.py` (PYTHON) -> Cumulative Risk: **767.34**
- **Archetype:** `file_cluster_13` (Distance: 14.268 IQR)
- **Magnitude:** 623.38 | **LOC:** 717 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `check_create_using` (Impact: 89.3), `flatten` (Impact: 56.1), `create_py_random_state` (Impact: 53.5)

### 4. `networkx/algorithms/flow/utils.py` (PYTHON) -> Cumulative Risk: **750.5**
- **Archetype:** `file_cluster_13` (Distance: 11.912 IQR)
- **Magnitude:** 225.82 | **LOC:** 232 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `build_residual_network` (Impact: 71.9), `detect_unboundedness` (Impact: 42.8), `build_flow_dict` (Impact: 17.8)

### 5. `networkx/algorithms/planarity.py` (PYTHON) -> Cumulative Risk: **742.79**
- **Archetype:** `file_cluster_8` (Distance: 11.923 IQR)
- **Magnitude:** 1704.06 | **LOC:** 1489 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `dfs_testing_recursive` (Impact: 122.6), `dfs_orientation_recursive` (Impact: 116.0), `add_constraints` (Impact: 110.2)

### 6. `networkx/algorithms/isomorphism/vf2userfunc.py` (PYTHON) -> Cumulative Risk: **741.14**
- **Archetype:** `file_cluster_8` (Distance: 11.691 IQR)
- **Magnitude:** 115.34 | **LOC:** 193 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9956%)
- **Heaviest Functions:** `_semantic_feasibility` (Impact: 67.7), `semantic_feasibility` (Impact: 8.8), `__init__` (Impact: 7.9)

### 7. `networkx/algorithms/isomorphism/temporalisomorphvf2.py` (PYTHON) -> Cumulative Risk: **728.62**
- **Archetype:** `file_cluster_8` (Distance: 11.826 IQR)
- **Magnitude:** 407.58 | **LOC:** 309 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `one_hop` (Impact: 61.1), `get_pred_dates` (Impact: 44.8), `get_succ_dates` (Impact: 44.8)

### 8. `networkx/utils/heaps.py` (PYTHON) -> Cumulative Risk: **724.55**
- **Archetype:** `file_cluster_13` (Distance: 12.689 IQR)
- **Magnitude:** 353.5 | **LOC:** 339 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `insert` (Impact: 75.5), `insert` (Impact: 34.4), `_merge_children` (Impact: 33.0)

### 9. `networkx/readwrite/graphml.py` (PYTHON) -> Cumulative Risk: **710.87**
- **Archetype:** `file_cluster_8` (Distance: 11.091 IQR)
- **Magnitude:** 1175.02 | **LOC:** 1054 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.644%)
- **Heaviest Functions:** `add_graph_element` (Impact: 133.3), `indent` (Impact: 130.8), `decode_data_elements` (Impact: 128.9)

### 10. `networkx/algorithms/approximation/kcomponents.py` (PYTHON) -> Cumulative Risk: **706.6**
- **Archetype:** `file_cluster_13` (Distance: 10.592 IQR)
- **Magnitude:** 436.7 | **LOC:** 369 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `k_components` (Impact: 184.6), `_cliques_heuristic` (Impact: 102.1), `subgraph` (Impact: 21.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `networkx/utils/backends.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.392 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.203 IQR)
- **Top Global Matches:** file_cluster_8: 12.392, file_cluster_13: 12.469, file_cluster_17: 12.483
- **Magnitude:** 4692.28 | **LOC:** 2184 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (61.9296%), Tech Debt (17.5638%)
**Top Internal Functions/Classes:**
  * `_call_if_any_backends_installed` (Impact: 4234.7 | O(2^N) | DB: 13)
  * `_set_configs_from_environment` (Impact: 55.1 | O(N^4) | DB: 22)
    * *Intent:* # Note: "networkx" is in `backend_info` but ignored in `backends` and `config.backends`. # It is val...
  * `_get_backends` (Impact: 49.5 | O(N^5) | DB: 1)
    * *Intent:* """ Retrieve NetworkX ``backends`` and ``backend_info`` from the entry points. Parameters ----------...
  * `__signature__` (Impact: 32.1 | O(N^6) | DB: 1)
  * `_call_if_no_backends_installed` (Impact: 25.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 514`, `structural_boundaries: 233`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 226`, `dead_code: 4`, `planned_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 5`, `import: 22`
* *Defense:* `safety: 109`, `doc: 44`, `test: 16`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.371
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 2):` finishes., of, .decorators, importlib.metadata, .configs, typing, time, warnings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/drawing/nx_pylab.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.126 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.599 IQR)
- **Top Global Matches:** file_cluster_8: 11.126, file_cluster_13: 11.267, file_cluster_17: 11.491
- **Magnitude:** 2963.14 | **LOC:** 2979 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (19.9821%), Tech Debt (13.8018%)
**Top Internal Functions/Classes:**
  * `draw_networkx_nodes` (Impact: 2174.7 | O(N^6) | DB: 25)
  * `_update_text_pos_angle` (Impact: 106.9 | O(N^6) | DB: 2)
    * *Intent:* *args,
  * `node_property_sequence` (Impact: 63.7 | O(N^5))
  * `edge_property_sequence` (Impact: 63.5 | O(N^5))
  * `apply_alpha` (Impact: 61.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 179`, `args: 44`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 84`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 44`, `import: 42`
* *Defense:* `safety: 48`, `doc: 50`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.766
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` numbers, collections, matplotlib.pyplot, itertools, collections.abc, matplotlib.patches, matplotlib.path, matplotlib.colors...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/readwrite/gml.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.407 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.385 IQR)
- **Top Global Matches:** file_cluster_13: 11.407, file_cluster_8: 11.48, file_cluster_7: 11.518
- **Magnitude:** 2309.6 | **LOC:** 883 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (15.6585%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `escape` (Impact: 2246.2 | O(2^N) | DB: 7)
  * `write_gml` (Impact: 6.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 87`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 21`
* *Architecture:* `api: 27`, `import: 9`
* *Defense:* `safety: 47`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` enum, collections, io, typing, networkx.utils, ast, html.entities, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/isomorphvf2.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.206 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.65 IQR)
- **Top Global Matches:** file_cluster_17: 12.206, file_cluster_7: 12.213, file_cluster_8: 12.215
- **Magnitude:** 1950.04 | **LOC:** 1263 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (47.7751%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `syntactic_feasibility` (Impact: 640.8 | O(N^6) | DB: 9)
  * `syntactic_feasibility` (Impact: 257.9 | O(N^6) | DB: 4)
    * *Intent:* # TODO: # Currently, we use recursion and set the recursion level higher. # It would be nice to rest...
  * `__init__` (Impact: 231.9 | O(N^6) | DB: 11)
    * *Intent:* # Users might be comparing DiGraph instances with MultiDiGraph # instances. So the generic DiGraphMa...
  * `candidate_pairs_iter` (Impact: 117.4 | O(N^6))
  * `__init__` (Impact: 116.9 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 96`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 144`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 3`, `api: 28`, `import: 2`
* *Defense:* `safety: 6`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001978
  * `Imports (Out-Degree: 0):` sys, networkx, networkx.algorithms
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/planarity.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.824 IQR)
- **Top Global Matches:** file_cluster_8: 11.923, file_cluster_7: 12.033, file_cluster_13: 12.157
- **Magnitude:** 1704.06 | **LOC:** 1489 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (26.5698%), Tech Debt (45.521%)
**Top Internal Functions/Classes:**
  * `dfs_testing_recursive` (Impact: 122.6 | O(2^N) | DB: 1)
    * *Intent:* # determine nesting graph
  * `dfs_orientation_recursive` (Impact: 116.0 | O(2^N))
    * *Intent:* """Recursive version of :meth:`lr_planarity`."""
  * `add_constraints` (Impact: 110.2 | O(N^5) | DB: 3)
  * `add_half_edge` (Impact: 105.4 | O(N^5) | DB: 1)
  * `check_structure` (Impact: 87.0 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 120`, `args: 51`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 157`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 58`, `import: 3`
* *Defense:* `safety: 6`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.31
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` copy, networkx, collections
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/ismags.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.041 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.435 IQR)
- **Top Global Matches:** file_cluster_8: 11.041, file_cluster_7: 11.117, file_cluster_17: 11.123
- **Magnitude:** 1599.26 | **LOC:** 1314 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (22.6348%), Tech Debt (35.8026%)
**Top Internal Functions/Classes:**
  * `_map_nodes` (Impact: 341.0 | O(N^6) | DB: 2)
  * `create_aligned_partitions` (Impact: 207.8 | O(N^6))
  * `_refine_opp` (Impact: 182.5 | O(N^6) | DB: 5)
    * *Intent:* ------
  * `_largest_common_subgraph` (Impact: 150.8 | O(2^N))
    * *Intent:* # Note: isinstance(G.edges(), OutEdgeDataView) is only true for multi(di)graph sg_multiedge = isinst...
  * `make_partition` (Impact: 106.8 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 108`, `args: 36`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 72`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 6`, `doc: 46`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` functools, itertools, networkx, collections
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/cycles.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.96 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.574 IQR)
- **Top Global Matches:** file_cluster_0: 11.96, file_cluster_13: 11.991, file_cluster_17: 12.014
- **Magnitude:** 1593.52 | **LOC:** 1235 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (41.4163%), Tech Debt (9.1779%)
**Top Internal Functions/Classes:**
  * `chordless_cycles` (Impact: 339.7 | O(N^6) | DB: 2)
  * `find_cycle` (Impact: 172.7 | O(N^6) | DB: 5)
  * `simple_cycles` (Impact: 163.3 | O(N^5))
    * *Intent:* ----------
  * `_chordless_cycle_search` (Impact: 111.1 | O(N^6) | DB: 4)
  * `recursive_simple_cycles` (Impact: 102.0 | O(N^5) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 81`, `args: 24`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 163`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `safety: 3`, `doc: 32`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` collections, itertools, networkx.utils, math, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/matching.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.739 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.594 IQR)
- **Top Global Matches:** file_cluster_0: 11.739, file_cluster_8: 11.772, file_cluster_13: 11.922
- **Magnitude:** 1591.0 | **LOC:** 1149 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (48.6948%), Tech Debt (13.2964%)
**Top Internal Functions/Classes:**
  * `max_weight_matching` (Impact: 1277.7 | O(N^6) | DB: 27)
  * `is_maximal_matching` (Impact: 70.9 | O(N^4) | DB: 1)
  * `is_matching` (Impact: 39.2 | O(N^3) | DB: 1)
    * *Intent:* # If the edge isn't covered, add it to the matching
  * `is_perfect_matching` (Impact: 39.2 | O(N^3) | DB: 1)
  * `maximal_matching` (Impact: 18.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 87`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 43`, `doc: 20`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` itertools, networkx.utils, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/coloring/equitable_coloring.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.576 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.702 IQR)
- **Top Global Matches:** file_cluster_8: 10.576, file_cluster_7: 10.889, file_cluster_17: 10.891
- **Magnitude:** 1466.56 | **LOC:** 506 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (21.1452%), Tech Debt (10.4072%)
**Top Internal Functions/Classes:**
  * `procedure_P` (Impact: 1146.3 | O(2^N) | DB: 9)
  * `equitable_color` (Impact: 97.5 | O(N^5) | DB: 2)
  * `is_equitable` (Impact: 56.5 | O(N^4))
    * *Intent:* """Determines if the coloring is valid and equitable for the graph G."""
  * `change_color` (Impact: 43.5 | O(N^3) | DB: 2)
  * `move_witnesses` (Impact: 18.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 36`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 42`, `planned_debt: 1`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 4`, `doc: 16`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.766
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` networkx, collections
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/generators/random_graphs.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.246 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.468 IQR)
- **Top Global Matches:** file_cluster_0: 11.246, file_cluster_8: 11.391, file_cluster_13: 11.411
- **Magnitude:** 1364.96 | **LOC:** 1496 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (16.8013%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extended_barabasi_albert_graph` (Impact: 302.6 | O(N^6) | DB: 14)
  * `random_regular_graph` (Impact: 150.6 | O(N^5))
  * `watts_strogatz_graph` (Impact: 112.9 | O(N^6))
  * `powerlaw_cluster_graph` (Impact: 105.3 | O(N^5) | DB: 6)
  * `newman_watts_strogatz_graph` (Impact: 96.9 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 83`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 64`, `dead_code: 3`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.277
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 3):` .degree_seq, ..utils.misc, collections, itertools, networkx.utils, scipy, math, .classic...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/vf2pp.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.97 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_17: 11.97, file_cluster_0: 12.234, file_cluster_13: 12.448
- **Magnitude:** 1357.94 | **LOC:** 1066 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (15.4077%), Tech Debt (9.1057%)
**Top Internal Functions/Classes:**
  * `_restore_Tinout_Di` (Impact: 265.7 | O(N^5))
  * `_feasible_look_ahead` (Impact: 237.8 | O(N^5))
  * `_feasible_node_pair` (Impact: 198.1 | O(N^4))
    * *Intent:* # Calculate the optimal node ordering
  * `_all_morphisms` (Impact: 127.8 | O(N^4) | DB: 4)
  * `_find_candidates_Di` (Impact: 117.3 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 84`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 29`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 16`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004451
  * `Imports (Out-Degree: 0):` operator, networkx, collections
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `networkx/readwrite/graphml.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.091 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.899 IQR)
- **Top Global Matches:** file_cluster_8: 11.091, file_cluster_13: 11.196, file_cluster_7: 11.329
- **Magnitude:** 1175.02 | **LOC:** 1054 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (14.0949%), Tech Debt (99.4995%)
**Top Internal Functions/Classes:**
  * `add_graph_element` (Impact: 133.3 | O(N^5) | DB: 1)
  * `indent` (Impact: 130.8 | O(2^N))
  * `decode_data_elements` (Impact: 128.9 | O(N^6))
  * `make_graph` (Impact: 87.8 | O(N^4) | DB: 3)
  * `add_edges` (Impact: 78.5 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 106`, `args: 33`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 84`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 34`, `import: 11`
* *Defense:* `safety: 12`, `doc: 40`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` numpy, xml.etree.ElementTree, collections, networkx.utils, warnings, lxml.etree, networkx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/distance_measures.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.574 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.444 IQR)
- **Top Global Matches:** file_cluster_0: 10.574, file_cluster_13: 10.684, file_cluster_8: 10.689
- **Magnitude:** 997.86 | **LOC:** 1121 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (11.7565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_extrema_bounding` (Impact: 283.5 | O(N^5) | DB: 1)
  * `resistance_distance` (Impact: 165.0 | O(N^5))
  * `eccentricity` (Impact: 136.3 | O(2^N))
  * `barycenter` (Impact: 85.4 | O(N^4) | DB: 1)
  * `center` (Impact: 74.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 57`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`, `dead_code: 4`
* *Architecture:* `api: 11`, `import: 7`
* *Defense:* `safety: 4`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.31
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` networkx.utils, scipy, math, numpy, networkx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/drawing/tests/test_pylab.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.662 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.734 IQR)
- **Top Global Matches:** file_cluster_8: 11.662, file_cluster_0: 11.87, file_cluster_17: 12.002
- **Magnitude:** 893.54 | **LOC:** 1583 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.0211%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_display_edge_multiple_colors` (Impact: 760.8 | O(N^4) | DB: 1)
  * `test_display_line_collection` (Impact: 16.3 | O(N^2))
  * `test_display_arg_handling_node_alpha` (Impact: 5.6 | O(N^2))
  * `test_display_node_position` (Impact: 5.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 213`, `args: 81`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 81`, `import: 12`
* *Defense:* `safety: 160`, `doc: 56`, `test: 251`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` itertools, matplotlib.patches, os, warnings, matplotlib.collections, pytest, networkx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/tests/test_cycles.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.352 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.8 IQR)
- **Top Global Matches:** file_cluster_8: 11.352, file_cluster_17: 11.548, file_cluster_0: 11.703
- **Magnitude:** 870.44 | **LOC:** 983 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (9.7528%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_cycle` (Impact: 124.5 | O(N^5) | DB: 1)
  * `test_simple_cycles_notable_clique_sequen` (Impact: 47.2 | O(N^3))
  * `test_chordless_cycles_giant_hamiltonian` (Impact: 41.3 | O(N^4))
    * *Intent:* # ... ---/ \-----/ \--- ... # <-- "long" edges # # each long edge belongs to exactly one triangle, a...
  * `test_simple_cycles_bound_error` (Impact: 40.0 | O(N^4))
  * `test_simple_cycles_bounded` (Impact: 35.9 | O(N^4) | DB: 2)
    * *Intent:* # there should be one cycle of every length d = nx.DiGraph() expected = [] for n in range(10): nx.ad...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 177`, `args: 75`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 29`, `duplicate_logic: 3`, `orphaned_logic: 55`
* *Architecture:* `api: 78`, `import: 6`
* *Defense:* `safety: 68`, `doc: 2`, `test: 138`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` random, itertools, math, networkx.algorithms.traversal.edgedfs, pytest, networkx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/threshold.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.502 IQR)
- **Top Global Matches:** file_cluster_0: 12.923, file_cluster_17: 12.969, file_cluster_13: 13.048
- **Magnitude:** 848.74 | **LOC:** 982 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (28.045%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `creation_sequence` (Impact: 81.6 | O(N^4) | DB: 5)
  * `shortest_path` (Impact: 57.9 | O(N^3) | DB: 1)
  * `creation_sequence_to_weights` (Impact: 57.4 | O(N^3))
  * `shortest_path_length` (Impact: 53.7 | O(N^3))
    * *Intent:* # Properties of Threshold Graphs def triangles(creation_sequence): """
  * `find_alternating_4_cycle` (Impact: 49.0 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 87`, `args: 26`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 115`, `dead_code: 5`
* *Architecture:* `api: 43`, `import: 3`
* *Defense:* `safety: 22`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.293
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` math, networkx.algorithms.threshold, networkx.utils, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/connectivity/edge_augmentation.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.649 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.076 IQR)
- **Top Global Matches:** file_cluster_0: 10.649, file_cluster_7: 10.816, file_cluster_8: 10.836
- **Magnitude:** 794.8 | **LOC:** 1271 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (13.6607%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `k_edge_augmentation` (Impact: 112.3 | O(N^5))
    * *Intent:* # First try to quickly determine if G is not k-edge-connected if G.number_of_nodes() < k + 1: return...
  * `greedy_k_edge_augmentation` (Impact: 106.9 | O(N^4) | DB: 3)
  * `unconstrained_bridge_augmentation` (Impact: 103.5 | O(N^4) | DB: 1)
    * *Intent:* """Finds augmentation that k-edge-connects as much of the graph as possible. When a k-edge-augmentat...
  * `weighted_bridge_augmentation` (Impact: 73.3 | O(N^3))
  * `partial_k_edge_augmentation` (Impact: 69.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 62`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 24`
* *Architecture:* `api: 14`, `import: 5`
* *Defense:* `safety: 12`, `doc: 40`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` collections, networkx.algorithms.connectivity, itertools, networkx.utils, math, networkx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tree/mst.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.282 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.198 IQR)
- **Top Global Matches:** file_cluster_8: 10.282, file_cluster_7: 10.318, file_cluster_13: 10.33
- **Magnitude:** 780.18 | **LOC:** 1323 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (15.7211%), Tech Debt (10.3557%)
**Top Internal Functions/Classes:**
  * `prim_mst_edges` (Impact: 346.5 | O(N^6) | DB: 1)
    * *Intent:* """ subtrees = UnionFind() if G.is_multigraph(): edges = G.edges(keys=True, data=True) else: edges =...
  * `random_spanning_tree` (Impact: 186.7 | O(N^6) | DB: 1)
  * `number_of_spanning_trees` (Impact: 41.8 | O(N^3))
  * `_partition` (Impact: 37.3 | O(N^5))
  * `best_edge` (Impact: 37.2 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 91`, `args: 21`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 24`, `planned_debt: 2`
* *Architecture:* `api: 19`, `import: 10`
* *Defense:* `safety: 6`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005299
  * `Imports (Out-Degree: 0):` numpy, enum, networkx.algorithms, dataclasses, itertools, networkx.utils, math, operator...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `networkx/algorithms/shortest_paths/weighted.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.244 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.742 IQR)
- **Top Global Matches:** file_cluster_0: 11.244, file_cluster_8: 11.368, file_cluster_7: 11.433
- **Magnitude:** 768.42 | **LOC:** 2543 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (23.6624%), Tech Debt (9.0458%)
**Top Internal Functions/Classes:**
  * `bidirectional_dijkstra` (Impact: 199.5 | O(N^6) | DB: 1)
  * `goldberg_radzik` (Impact: 173.2 | O(N^6) | DB: 4)
  * `find_negative_cycle` (Impact: 68.0 | O(N^5) | DB: 6)
  * `multi_source_dijkstra` (Impact: 40.2 | O(N^3))
  * `negative_edge_cycle` (Impact: 25.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 110`, `args: 37`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 57`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 31`, `import: 5`
* *Defense:* `safety: 13`, `doc: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.594
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.01056
  * `Imports (Out-Degree: 1):` collections, itertools, networkx.algorithms.shortest_paths.generic, heapq, networkx
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `networkx/algorithms/dag.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.465 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.165 IQR)
- **Top Global Matches:** file_cluster_0: 11.465, file_cluster_13: 11.746, file_cluster_17: 11.856
- **Magnitude:** 763.24 | **LOC:** 1388 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (20.7079%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `transitive_reduction` (Impact: 105.1 | O(2^N))
    * *Intent:* ----------
  * `all_topological_sorts` (Impact: 102.4 | O(N^5) | DB: 7)
    * *Intent:* -------- """ return G.is_directed() and not has_cycle(G) @nx._dispatchable def topological_generatio...
  * `lexicographical_topological_sort` (Impact: 99.3 | O(N^6))
  * `topological_generations` (Impact: 84.6 | O(N^5) | DB: 1)
  * `dag_longest_path` (Impact: 82.4 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 64`, `args: 25`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 39`, `dead_code: 1`
* *Architecture:* `api: 23`, `import: 6`
* *Defense:* `safety: 12`, `doc: 40`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` collections, itertools, networkx.utils, math, operator, heapq, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/community/lukes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.768 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.336 IQR)
- **Top Global Matches:** file_cluster_13: 9.768, file_cluster_17: 9.799, file_cluster_0: 9.819
- **Magnitude:** 725.16 | **LOC:** 228 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (15.7855%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lukes_partitioning` (Impact: 712.2 | O(2^N) | DB: 1)
  * `_split_n_from` (Impact: 5.5 | O(N^2))
    * *Intent:* # the second argument assert n >= min_size_of_first_part for p1 in range(min_size_of_first_part, n +...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 31`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 4`, `doc: 4`, `test: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` functools, random, networkx.utils, copy, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/approximation/traveling_salesman.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.901 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.872 IQR)
- **Top Global Matches:** file_cluster_8: 9.901, file_cluster_13: 10.202, file_cluster_7: 10.218
- **Magnitude:** 716.18 | **LOC:** 1509 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (17.99%), Tech Debt (9.1852%)
**Top Internal Functions/Classes:**
  * `held_karp_ascent` (Impact: 261.1 | O(N^5) | DB: 1)
  * `asadpour_atsp` (Impact: 171.9 | O(N^5))
    * *Intent:* ----------
  * `spanning_tree_distribution` (Impact: 161.0 | O(2^N))
    * *Intent:* # Test to see if the ascent method found an integer solution or a fractional # solution. If it is in...
  * `christofides` (Impact: 28.4 | O(N^2))
  * `greedy_tsp` (Impact: 19.4 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 76`, `args: 19`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 28`, `planned_debt: 1`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `safety: 3`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 1):` networkx.algorithms, networkx.utils, networkx.algorithms.approximation, math, scipy, networkx.algorithms.tree.mst, numpy, networkx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/centrality/group.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.997 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.151 IQR)
- **Top Global Matches:** file_cluster_8: 9.997, file_cluster_13: 10.121, file_cluster_0: 10.141
- **Magnitude:** 702.7 | **LOC:** 788 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.0065%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `group_betweenness_centrality` (Impact: 270.0 | O(N^6) | DB: 1)
  * `_heuristic` (Impact: 161.7 | O(N^6) | DB: 3)
  * `_dfbnb` (Impact: 115.9 | O(2^N))
  * `_group_preprocessing` (Impact: 99.8 | O(N^6))
  * `group_closeness_centrality` (Impact: 21.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 36`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 12`, `dead_code: 3`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 4`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 2):` networkx.algorithms.centrality.betweenness, networkx.utils.decorators, copy, pandas, numpy, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/flow/networksimplex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.76 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.779 IQR)
- **Top Global Matches:** file_cluster_8: 11.76, file_cluster_7: 11.883, file_cluster_13: 11.919
- **Magnitude:** 702.7 | **LOC:** 663 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (31.0401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `network_simplex` (Impact: 304.9 | O(N^4) | DB: 6)
  * `find_entering_edges` (Impact: 48.8 | O(N^5) | DB: 1)
  * `find_apex` (Impact: 43.0 | O(N^5))
  * `augment_flow` (Impact: 22.8 | O(N^4))
  * `initialize_spanning_tree` (Impact: 21.1 | O(N^3) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 36`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 103`
* *Architecture:* `api: 18`, `import: 4`
* *Defense:* `safety: 2`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.345
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` math, itertools, networkx.utils, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/simple_paths.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.391 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.196 IQR)
- **Top Global Matches:** file_cluster_13: 10.391, file_cluster_8: 10.455, file_cluster_0: 10.472
- **Magnitude:** 694.38 | **LOC:** 967 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (19.2423%), Tech Debt (32.7379%)
**Top Internal Functions/Classes:**
  * `_bidirectional_pred_succ` (Impact: 296.5 | O(N^6) | DB: 2)
  * `shortest_simple_paths` (Impact: 120.4 | O(N^6) | DB: 2)
    * *Intent:* -------
  * `_all_simple_edge_paths` (Impact: 46.7 | O(N^3) | DB: 2)
    * *Intent:* # The empty list is not a valid path. Could also return
  * `all_simple_edge_paths` (Impact: 41.1 | O(N^3))
  * `filter_iter` (Impact: 24.6 | O(N^6))
    * *Intent:* # We simulate recursion with a stack, keeping the current path being explored # and the outgoing edg...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 70`, `args: 31`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 28`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 4`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.31
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 1):` functools, itertools, networkx.utils, networkx.algorithms.shortest_paths.weighted, heapq, networkx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `networkx/algorithms/wiener.py` (PYTHON) | Magnitude: 56.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 16, branch: 15, doc: 10
- `networkx/algorithms/lowest_common_ancestors.py` (PYTHON) | Magnitude: 266.68 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, branch: 40, structural_boundaries: 21, doc: 8
- `networkx/algorithms/approximation/connectivity.py` (PYTHON) | Magnitude: 322.2 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 117, branch: 50, structural_boundaries: 24, state_mutation: 15
- `networkx/utils/tests/test_backends.py` (PYTHON) | Magnitude: 142.72 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 75, test: 52, safety: 46
- `networkx/algorithms/minors/tests/test_contraction.py` (PYTHON) | Magnitude: 273.46 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 347, test: 154, structural_boundaries: 146, safety: 103

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `networkx/generators/tests/test_internet_as_graphs.py` (PYTHON) | Magnitude: 419.18 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 75, branch: 47, test: 44
- `networkx/algorithms/flow/maxflow.py` (PYTHON) | Magnitude: 107.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 24, encapsulation: 22, branch: 12
- `examples/subclass/plot_printgraph.py` (PYTHON) | Magnitude: 110.68 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, args: 10, func_start: 10
- `networkx/algorithms/approximation/clustering_coefficient.py` (PYTHON) | Magnitude: 23.08 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, branch: 4, decorators: 3
- `networkx/algorithms/community/label_propagation.py` (PYTHON) | Magnitude: 320.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 96, branch: 46, structural_boundaries: 23, doc: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tools/generate_requirements.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, generics: 3, encapsulation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `networkx/algorithms/isomorphism/isomorphvf2.py` (PYTHON) | Magnitude: 1950.04 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 475, branch: 236, state_mutation: 144, structural_boundaries: 96
- `networkx/algorithms/components/tests/test_attracting.py` (PYTHON) | Magnitude: 38.16 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 28, test: 25, safety: 17
- `doc/_static/copybutton.js` (JAVASCRIPT) | Magnitude: 41.66 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 26, structural_boundaries: 12, comprehensions: 4
- `networkx/algorithms/bipartite/matching.py` (PYTHON) | Magnitude: 463.98 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 145, branch: 62, structural_boundaries: 39, state_mutation: 30
- `networkx/generators/tests/test_small.py` (PYTHON) | Magnitude: 140.92 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 172, test: 121, structural_boundaries: 118, safety: 111

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/graph/plot_morse_trie.py` (PYTHON) | Magnitude: 12.88 | Delta: **0.539 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, ui_framework: 28, branch: 9, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `networkx/generators/joint_degree_seq.py` (PYTHON) | Magnitude: 535.8 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 246, branch: 81, structural_boundaries: 31, state_mutation: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `networkx/algorithms/shortest_paths/unweighted.py` (PYTHON) | Magnitude: 464.86 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 160, branch: 63, structural_boundaries: 34, state_mutation: 24
- `networkx/algorithms/euler.py` (PYTHON) | Magnitude: 431.02 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 160, branch: 76, structural_boundaries: 36, encapsulation: 19
- `networkx/algorithms/traversal/depth_first_search.py` (PYTHON) | Magnitude: 328.36 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 105, branch: 35, structural_boundaries: 20, doc: 16
- `networkx/algorithms/operators/product.py` (PYTHON) | Magnitude: 495.0 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 179, branch: 95, encapsulation: 59, structural_boundaries: 34
- `networkx/algorithms/connectivity/edge_kcomponents.py` (PYTHON) | Magnitude: 372.4 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, branch: 53, structural_boundaries: 37, doc: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `networkx/algorithms/approximation/dominating_set.py` (PYTHON) | Magnitude: 28.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 15, doc: 8, branch: 5
- `networkx/algorithms/components/tests/test_connected.py` (PYTHON) | Magnitude: 106.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 30, test: 25, state_mutation: 17
- `networkx/generators/time_series.py` (PYTHON) | Magnitude: 17.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 5, doc: 4, branch: 3
- `networkx/algorithms/isomorphism/tests/test_tree_isomorphism.py` (PYTHON) | Magnitude: 93.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 125, test: 27, structural_boundaries: 25, branch: 16
- `networkx/algorithms/centrality/percolation.py` (PYTHON) | Magnitude: 61.92 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 12, branch: 9, encapsulation: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `networkx/utils/misc.py` -> Churn: **71.67%** | Cog Load: 19.0532% | Debt: 77.9618%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `networkx/drawing/nx_pylab.py` -> **NaorTIRAM** (100.0% isolated ownership) | Magnitude: 2963.14
- `networkx/readwrite/gml.py` -> **Ross Barnowski** (100.0% isolated ownership) | Magnitude: 2309.6
- `networkx/algorithms/isomorphism/ismags.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1599.26
- `networkx/algorithms/isomorphism/vf2pp.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1357.94
- `networkx/algorithms/tests/test_cycles.py` -> **Ross Barnowski** (100.0% isolated ownership) | Magnitude: 870.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `networkx/algorithms/centrality/betweenness.py` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 95.4357%)
- `networkx/algorithms/shortest_paths/weighted.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 89.0533%)
- `networkx/generators/atlas.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 81.3057%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `networkx/algorithms/centrality/betweenness.py` -> **Severity: 0.31** (Embedded: 0.0059 * Error Risk: 52.1675%)
- `networkx/utils/decorators.py` -> **Severity: 0.253** (Embedded: 0.0312 * Error Risk: 8.1237%)
- `networkx/algorithms/communicability_alg.py` -> **Severity: 0.227** (Embedded: 0.003 * Error Risk: 76.5116%)
- `networkx/convert.py` -> **Severity: 0.227** (Embedded: 0.003 * Error Risk: 76.5686%)
- `networkx/algorithms/bipartite/matching.py` -> **Severity: 0.215** (Embedded: 0.0045 * Error Risk: 48.2927%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `networkx/algorithms/flow/utils.py` -> **Severity: 841.2** (Blast Radius: 8.412 * Doc Risk: 100.0%)
- `networkx/algorithms/bipartite/generators.py` -> **Severity: 715.569** (Blast Radius: 7.291 * Doc Risk: 98.1441%)
- `networkx/algorithms/traversal/edgedfs.py` -> **Severity: 460.296** (Blast Radius: 4.611 * Doc Risk: 99.8257%)
- `networkx/algorithms/assortativity/pairs.py` -> **Severity: 459.1** (Blast Radius: 4.651 * Doc Risk: 98.7099%)
- `networkx/algorithms/centrality/flow_matrix.py` -> **Severity: 453.5** (Blast Radius: 4.535 * Doc Risk: 99.9999%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
