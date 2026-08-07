# ARCHITECTURAL_BRIEF: networkx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/networkx` |
| **Timestamp** | `2026-08-07T04:00:38.093550+00:00` |
| **Scan Duration** | `2.83s` |
| **Git Branch** | `main` |
| **Git Commit** | `6628a781503211153d16f2a2ef184e75daba69e5` |
| **Git Remote** | `https://github.com/networkx/networkx.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 649 malicious artifacts.

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
| Total Artifacts | 970 |
| Analyzed Artifacts (Scanned) | 674 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 296 |
| Total LOC | 89089 |
| Volatility Index | 0.006 |
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
> **Architectural Drift Z-Score:** `5.954`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 458 | 68.0% |
| file_cluster_13 | 128 | 19.0% |
| file_cluster_0 | 52 | 7.7% |
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
| Error & Exception Exposure | 0.0 | 100.0 | 26.6 | 4.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.7 | 5.1 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 32.5 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 76.4 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 93.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.1 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 84.5 | 7.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
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

- `_call_if_any_backends_installed` (@ `networkx/utils/backends.py`) -> Impact: **648.6** | LOC: 1019
- `draw_networkx_nodes` (@ `networkx/drawing/nx_pylab.py`) -> Impact: **401.5** | LOC: 779
- `max_weight_matching` (@ `networkx/algorithms/matching.py`) -> Impact: **392.7** | LOC: 774
- `test_display_edge_multiple_colors` (@ `networkx/drawing/tests/test_pylab.py`) -> Impact: **345.1** | LOC: 1360
- `escape` (@ `networkx/readwrite/gml.py`) -> Impact: **344.4** | LOC: 549
- `fixup` (@ `networkx/readwrite/gml.py`) -> Impact: **326.6** | LOC: 505
- `preflow_push_impl` (@ `networkx/algorithms/flow/preflowpush.py`) -> Impact: **208.7** | LOC: 270
- `syntactic_feasibility` (@ `networkx/algorithms/isomorphism/isomorphvf2.py`) -> Impact: **190.8** | LOC: 216
- `procedure_P` (@ `networkx/algorithms/coloring/equitable_coloring.py`) -> Impact: **174.3** | LOC: 247
- `boykov_kolmogorov_impl` (@ `networkx/algorithms/flow/boykovkolmogorov.py`) -> Impact: **147.0** | LOC: 188

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `networkx/algorithms` | 56 | 7948.48 | 14.07% | 14.57% |
| `networkx/algorithms/tests` | 58 | 6529.54 | 3.64% | 0.0% |
| `networkx/generators` | 29 | 2983.1 | 11.6% | 7.88% |
| `networkx/algorithms/isomorphism` | 9 | 2670.76 | 26.29% | 58.75% |
| `networkx/readwrite` | 13 | 2314.24 | 16.6% | 8.54% |
| `networkx/utils` | 10 | 2286.18 | 25.07% | 33.97% |
| `networkx/generators/tests` | 29 | 2233.8 | 3.82% | 0.0% |
| `networkx/algorithms/flow` | 12 | 1776.32 | 17.2% | 15.74% |
| `networkx/algorithms/centrality/tests` | 21 | 1770.9 | 2.95% | 0.0% |
| `networkx/algorithms/isomorphism/tests` | 11 | 1647.2 | 5.29% | 0.0% |

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
- `networkx/algorithms/tests/test_simple_paths.py` -> **64** Orphaned Functions | **20** Duplicates
- `networkx/algorithms/tests/test_dag.py` -> **61** Orphaned Functions | **8** Duplicates
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2214` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `networkx/algorithms/flow/utils.py` (PYTHON) -> Cumulative Risk: **604.88**
- **Archetype:** `file_cluster_13` (Distance: 11.912 IQR)
- **Magnitude:** 126.82 | **LOC:** 232 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8288%), Tech Debt (99.1051%)
- **Heaviest Functions:** `build_residual_network` (Impact: 30.3), `detect_unboundedness` (Impact: 12.8), `build_flow_dict` (Impact: 9.2)

### 2. `networkx/algorithms/centrality/flow_matrix.py` (PYTHON) -> Cumulative Risk: **553.4**
- **Archetype:** `file_cluster_13` (Distance: 10.77 IQR)
- **Magnitude:** 99.6 | **LOC:** 131 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9738%), Documentation (99.7824%)
- **Heaviest Functions:** `flow_matrix_row` (Impact: 7.9), `__init__` (Impact: 7.4), `width` (Impact: 5.7)

### 3. `networkx/algorithms/cycles.py` (PYTHON) -> Cumulative Risk: **545.71**
- **Archetype:** `file_cluster_0` (Distance: 11.944 IQR)
- **Magnitude:** 694.12 | **LOC:** 1235 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9987%), Tech Debt (84.6834%), Safety Score (83.287%)
- **Heaviest Functions:** `chordless_cycles` (Impact: 101.6), `simple_cycles` (Impact: 55.9), `find_cycle` (Impact: 52.6)

### 4. `networkx/algorithms/isomorphism/isomorphvf2.py` (PYTHON) -> Cumulative Risk: **534.85**
- **Archetype:** `file_cluster_17` (Distance: 12.206 IQR)
- **Magnitude:** 738.24 | **LOC:** 1263 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9937%), Safety Score (83.4894%)
- **Heaviest Functions:** `syntactic_feasibility` (Impact: 190.8), `syntactic_feasibility` (Impact: 77.8), `__init__` (Impact: 69.7)

### 5. `networkx/utils/configs.py` (PYTHON) -> Cumulative Risk: **529.9**
- **Archetype:** `file_cluster_13` (Distance: 12.392 IQR)
- **Magnitude:** 217.22 | **LOC:** 397 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (95.6575%), Verification (80.0%)
- **Heaviest Functions:** `_on_setattr` (Impact: 52.5), `__enter__` (Impact: 27.1), `__new__` (Impact: 8.1)

### 6. `benchmarks/benchmarks/benchmark_algorithms.py` (PYTHON) -> Cumulative Risk: **526.73**
- **Archetype:** `file_cluster_8` (Distance: 9.02 IQR)
- **Magnitude:** 101.24 | **LOC:** 247 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9997%), Verification (80.0%)
- **Heaviest Functions:** `_make_weighted_benchmark_graphs` (Impact: 15.6), `dijkstra_relaxation_worst_case` (Impact: 5.6), `_make_tournament_benchmark_graphs` (Impact: 3.8)

### 7. `benchmarks/benchmarks/benchmark_classes.py` (PYTHON) -> Cumulative Risk: **526.15**
- **Archetype:** `file_cluster_13` (Distance: 12.228 IQR)
- **Magnitude:** 37.62 | **LOC:** 46 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.9724%), State Flux (98.4807%)
- **Heaviest Functions:** `setup` (Impact: 2.0), `time_graph_create` (Impact: 1.8), `time_add_nodes_from` (Impact: 1.8)

### 8. `networkx/algorithms/isomorphism/ismags.py` (PYTHON) -> Cumulative Risk: **524.37**
- **Archetype:** `file_cluster_8` (Distance: 11.035 IQR)
- **Magnitude:** 620.76 | **LOC:** 1314 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.1304%), State Flux (92.4213%), Verification (80.0%)
- **Heaviest Functions:** `_map_nodes` (Impact: 102.2), `create_aligned_partitions` (Impact: 62.4), `_refine_opp` (Impact: 53.9)

### 9. `networkx/algorithms/planarity.py` (PYTHON) -> Cumulative Risk: **518.22**
- **Archetype:** `file_cluster_8` (Distance: 11.953 IQR)
- **Magnitude:** 738.76 | **LOC:** 1489 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9193%), Verification (80.0%), Safety Score (74.4426%)
- **Heaviest Functions:** `add_constraints` (Impact: 38.1), `add_half_edge` (Impact: 36.6), `remove_back_edges` (Impact: 33.1)

### 10. `benchmarks/benchmarks/benchmark_chordal.py` (PYTHON) -> Cumulative Risk: **517.63**
- **Archetype:** `file_cluster_13` (Distance: 12.834 IQR)
- **Magnitude:** 23.9 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9556%)
- **Heaviest Functions:** `setup` (Impact: 2.0), `time_is_chordal_complete` (Impact: 1.9), `time_is_chordal_star` (Impact: 1.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `networkx/utils/backends.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.392 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.203 IQR)
- **Top Global Matches:** file_cluster_8: 12.392, file_cluster_13: 12.469, file_cluster_17: 12.483
- **Magnitude:** 997.18 | **LOC:** 2184 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (61.9296%), Tech Debt (17.5638%)
**Top Internal Functions/Classes:**
  * `_call_if_any_backends_installed` (Impact: 648.6)
  * `_set_configs_from_environment` (Impact: 23.9)
    * *Intent:* # Note: "networkx" is in `backend_info` but ignored in `backends` and `config.backends`. # It is val...
  * `_get_backends` (Impact: 17.6)
    * *Intent:* """ Retrieve NetworkX ``backends`` and ``backend_info`` from the entry points. Parameters ----------...
  * `__signature__` (Impact: 10.4)
  * `_call_if_no_backends_installed` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 514`, `structural_boundaries: 233`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 226`, `dead_code: 4`, `planned_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 5`, `import: 22`
* *Defense:* `safety: 109`, `doc: 44`, `test: 16`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.371
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 2):` .configs, itertools, networkx, os, numpy, functools, logging, finishes....
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/matching.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.733 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.57 IQR)
- **Top Global Matches:** file_cluster_0: 11.733, file_cluster_8: 11.77, file_cluster_13: 11.916
- **Magnitude:** 900.1 | **LOC:** 1149 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.0911%), Tech Debt (44.4427%)
**Top Internal Functions/Classes:**
  * `max_weight_matching` (Impact: 392.7)
  * `addBlossom` (Impact: 60.6)
  * `expandBlossom` (Impact: 52.4)
    * *Intent:* # If b is a top-level blossom, # label.get(b) is None if b is unlabeled (free), # 1 if b is an S-blo...
  * `_recurse` (Impact: 46.2)
    * *Intent:* # labeledge[b] = (v, w) is the edge through which b obtained its label # such that w is a vertex in ...
  * `verifyOptimum` (Impact: 35.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 87`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 43`, `doc: 20`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` networkx.utils, itertools, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/drawing/nx_pylab.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.12 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.599 IQR)
- **Top Global Matches:** file_cluster_8: 11.12, file_cluster_13: 11.262, file_cluster_17: 11.486
- **Magnitude:** 838.74 | **LOC:** 2979 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.9103%), Tech Debt (13.8018%)
**Top Internal Functions/Classes:**
  * `draw_networkx_nodes` (Impact: 401.5)
  * `draw_networkx` (Impact: 33.8)
  * `_update_text_pos_angle` (Impact: 33.3)
    * *Intent:* *args,
  * `apply_alpha` (Impact: 25.9)
  * `node_property_sequence` (Impact: 22.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 179`, `args: 46`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 84`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 44`, `import: 42`
* *Defense:* `safety: 48`, `doc: 50`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.766
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` matplotlib.colors, itertools, matplotlib, matplotlib.patches, networkx, inspect, matplotlib.collections, matplotlib.path...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/planarity.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.953 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.832 IQR)
- **Top Global Matches:** file_cluster_8: 11.953, file_cluster_7: 12.063, file_cluster_13: 12.187
- **Magnitude:** 738.76 | **LOC:** 1489 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (26.5698%), Tech Debt (45.521%)
**Top Internal Functions/Classes:**
  * `add_constraints` (Impact: 38.1)
  * `add_half_edge` (Impact: 36.6)
  * `remove_back_edges` (Impact: 33.1)
  * `check_structure` (Impact: 26.4)
  * `lr_planarity` (Impact: 26.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 120`, `args: 61`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 157`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 58`, `import: 3`
* *Defense:* `safety: 6`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.31
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` copy, collections, networkx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/isomorphvf2.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.206 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.65 IQR)
- **Top Global Matches:** file_cluster_17: 12.206, file_cluster_7: 12.213, file_cluster_8: 12.215
- **Magnitude:** 738.24 | **LOC:** 1263 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.7751%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `syntactic_feasibility` (Impact: 190.8)
  * `syntactic_feasibility` (Impact: 77.8)
    * *Intent:* # TODO: # Currently, we use recursion and set the recursion level higher. # It would be nice to rest...
  * `__init__` (Impact: 69.7)
    * *Intent:* # Users might be comparing DiGraph instances with MultiDiGraph # instances. So the generic DiGraphMa...
  * `__init__` (Impact: 40.9)
  * `candidate_pairs_iter` (Impact: 35.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 96`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 144`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 3`, `api: 28`, `import: 2`
* *Defense:* `safety: 6`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001978
  * `Imports (Out-Degree: 0):` networkx, networkx.algorithms, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/readwrite/gml.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.402 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.385 IQR)
- **Top Global Matches:** file_cluster_13: 11.402, file_cluster_8: 11.475, file_cluster_7: 11.513
- **Magnitude:** 732.4 | **LOC:** 883 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.6585%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `escape` (Impact: 344.4)
  * `fixup` (Impact: 326.6)
  * `write_gml` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 87`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 21`
* *Architecture:* `api: 27`, `import: 9`
* *Defense:* `safety: 47`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` enum, html.entities, networkx, collections, ast, io, re, networkx.utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/cycles.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.944 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.541 IQR)
- **Top Global Matches:** file_cluster_0: 11.944, file_cluster_13: 11.977, file_cluster_17: 11.994
- **Magnitude:** 694.12 | **LOC:** 1235 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (41.4163%), Tech Debt (84.6834%)
**Top Internal Functions/Classes:**
  * `chordless_cycles` (Impact: 101.6)
  * `simple_cycles` (Impact: 55.9)
    * *Intent:* ----------
  * `find_cycle` (Impact: 52.6)
  * `recursive_simple_cycles` (Impact: 36.2)
  * `_min_cycle` (Impact: 34.4)
    * *Intent:* # If we're given a multigraph, we have a few cases to consider with parallel # edges. # # 1. If we h...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 81`, `args: 24`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 163`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `safety: 3`, `doc: 32`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` itertools, networkx, collections, networkx.utils, math
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/ismags.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.035 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.417 IQR)
- **Top Global Matches:** file_cluster_8: 11.035, file_cluster_17: 11.105, file_cluster_7: 11.11
- **Magnitude:** 620.76 | **LOC:** 1314 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.6348%), Tech Debt (97.1304%)
**Top Internal Functions/Classes:**
  * `_map_nodes` (Impact: 102.2)
  * `create_aligned_partitions` (Impact: 62.4)
  * `_refine_opp` (Impact: 53.9)
    * *Intent:* ------
  * `make_partition` (Impact: 43.9)
  * `_largest_common_subgraph` (Impact: 27.8)
    * *Intent:* # Note: isinstance(G.edges(), OutEdgeDataView) is only true for multi(di)graph sg_multiedge = isinst...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 108`, `args: 36`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 72`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 8`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 6`, `doc: 46`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` functools, collections, itertools, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/generators/random_graphs.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.242 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.469 IQR)
- **Top Global Matches:** file_cluster_0: 11.242, file_cluster_8: 11.386, file_cluster_13: 11.407
- **Magnitude:** 607.76 | **LOC:** 1496 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (16.8013%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extended_barabasi_albert_graph` (Impact: 90.5)
  * `random_regular_graph` (Impact: 52.6)
  * `fast_gnp_random_graph` (Impact: 39.0)
  * `powerlaw_cluster_graph` (Impact: 36.5)
  * `watts_strogatz_graph` (Impact: 33.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 83`, `args: 24`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 64`, `dead_code: 3`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.277
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 3):` .classic, ..utils.misc, itertools, networkx, .degree_seq, scipy, collections, networkx.utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/vf2pp.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.97 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_17: 11.97, file_cluster_0: 12.234, file_cluster_13: 12.448
- **Magnitude:** 593.84 | **LOC:** 1066 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.4077%), Tech Debt (9.1057%)
**Top Internal Functions/Classes:**
  * `_restore_Tinout_Di` (Impact: 91.3)
  * `_feasible_look_ahead` (Impact: 81.3)
  * `_feasible_node_pair` (Impact: 80.7)
    * *Intent:* # Calculate the optimal node ordering
  * `_all_morphisms` (Impact: 54.3)
  * `_find_candidates_Di` (Impact: 48.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 84`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 29`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 16`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004451
  * `Imports (Out-Degree: 0):` operator, collections, networkx
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tests/test_cycles.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.352 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.8 IQR)
- **Top Global Matches:** file_cluster_8: 11.352, file_cluster_17: 11.547, file_cluster_0: 11.703
- **Magnitude:** 526.54 | **LOC:** 983 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.703%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_cycle` (Impact: 42.3)
  * `test_simple_cycles_notable_clique_sequen` (Impact: 24.7)
  * `test_chordless_cycles_giant_hamiltonian` (Impact: 17.9)
    * *Intent:* # ... ---/ \-----/ \--- ... # <-- "long" edges # # each long edge belongs to exactly one triangle, a...
  * `test_chordless_cycles_directed` (Impact: 17.1)
  * `test_simple_cycles_bound_error` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 177`, `args: 75`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 29`, `duplicate_logic: 3`, `orphaned_logic: 55`
* *Architecture:* `api: 78`, `import: 6`
* *Defense:* `safety: 68`, `doc: 2`, `test: 138`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` itertools, networkx.algorithms.traversal.edgedfs, random, pytest, networkx, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/threshold.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.502 IQR)
- **Top Global Matches:** file_cluster_0: 12.923, file_cluster_17: 12.969, file_cluster_13: 13.048
- **Magnitude:** 502.24 | **LOC:** 982 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.045%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `creation_sequence` (Impact: 33.6)
  * `shortest_path` (Impact: 29.9)
  * `creation_sequence_to_weights` (Impact: 29.7)
  * `shortest_path_length` (Impact: 27.7)
    * *Intent:* # Properties of Threshold Graphs def triangles(creation_sequence): """
  * `threshold_graph` (Impact: 17.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 87`, `args: 26`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 115`, `dead_code: 5`
* *Architecture:* `api: 43`, `import: 3`
* *Defense:* `safety: 22`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.293
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` networkx, networkx.utils, networkx.algorithms.threshold, math
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/readwrite/graphml.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.091 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.899 IQR)
- **Top Global Matches:** file_cluster_8: 11.091, file_cluster_13: 11.196, file_cluster_7: 11.329
- **Magnitude:** 497.22 | **LOC:** 1054 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0949%), Tech Debt (99.4995%)
**Top Internal Functions/Classes:**
  * `add_graph_element` (Impact: 46.7)
  * `decode_data_elements` (Impact: 39.0)
  * `make_graph` (Impact: 36.3)
  * `indent` (Impact: 26.8)
  * `add_edge` (Impact: 24.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 106`, `args: 33`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 84`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 34`, `import: 11`
* *Defense:* `safety: 12`, `doc: 40`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` lxml.etree, networkx, warnings, collections, numpy, xml.etree.ElementTree, networkx.utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/drawing/tests/test_pylab.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.662 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.734 IQR)
- **Top Global Matches:** file_cluster_8: 11.662, file_cluster_0: 11.87, file_cluster_17: 12.002
- **Magnitude:** 469.24 | **LOC:** 1583 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.0211%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_display_edge_multiple_colors` (Impact: 345.1)
  * `test_display_line_collection` (Impact: 11.1)
  * `test_display_arg_handling_node_alpha` (Impact: 3.9)
  * `test_display_node_position` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 213`, `args: 81`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 81`, `import: 12`
* *Defense:* `safety: 160`, `doc: 56`, `test: 251`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` itertools, pytest, networkx, warnings, matplotlib.collections, matplotlib.patches, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/tests/test_similarity.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.042 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.272 IQR)
- **Top Global Matches:** file_cluster_8: 11.042, file_cluster_0: 11.576, file_cluster_7: 11.581
- **Magnitude:** 418.5 | **LOC:** 1159 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (2.8349%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_graph_edit_distance_edge_cost` (Impact: 22.6)
  * `test_graph_edit_distance_node_cost` (Impact: 20.9)
  * `test_generate_random_paths_with_isolated` (Impact: 13.2)
  * `test_graph_edit_distance_edge_match` (Impact: 11.1)
  * `test_graph_edit_distance_node_match` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 254`, `args: 77`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 61`
* *Architecture:* `api: 75`, `import: 4`
* *Defense:* `safety: 156`, `doc: 24`, `test: 252`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` networkx.generators.classic, networkx.algorithms.similarity, pytest, networkx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/tests/test_distance_measures.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.739 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.009 IQR)
- **Top Global Matches:** file_cluster_8: 11.739, file_cluster_0: 12.078, file_cluster_13: 12.221
- **Magnitude:** 417.06 | **LOC:** 838 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (3.7585%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_use_bounds_on_off_consistency` (Impact: 9.9)
    * *Intent:* """Test for consistency of distance metrics when using usebounds=True. We validate consistency for `...
  * `test_this_one_specific_tree` (Impact: 9.1)
  * `test_diameter_radius_empty_graph` (Impact: 9.0)
  * `test_trees` (Impact: 7.5)
  * `test_harmonic_diameter_weighted_paths` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 242`, `args: 103`, `func_start: 102`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `duplicate_logic: 8`, `orphaned_logic: 93`
* *Architecture:* `api: 108`, `import: 7`
* *Defense:* `safety: 121`, `doc: 10`, `test: 262`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` itertools, random, pytest, networkx, networkx.algorithms.distance_measures, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/shortest_paths/weighted.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.24 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.742 IQR)
- **Top Global Matches:** file_cluster_0: 11.24, file_cluster_8: 11.364, file_cluster_7: 11.43
- **Magnitude:** 416.82 | **LOC:** 2543 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (23.4267%), Tech Debt (9.0458%)
**Top Internal Functions/Classes:**
  * `bidirectional_dijkstra` (Impact: 59.7)
  * `goldberg_radzik` (Impact: 53.1)
  * `find_negative_cycle` (Impact: 24.0)
  * `multi_source_dijkstra` (Impact: 20.6)
  * `topo_sort` (Impact: 19.8)
    * *Intent:* --------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 110`, `args: 37`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 57`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 31`, `import: 5`
* *Defense:* `safety: 13`, `doc: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.594
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.01056
  * `Imports (Out-Degree: 1):` itertools, networkx, networkx.algorithms.shortest_paths.generic, collections, heapq
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tests/test_simple_paths.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.68 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.053 IQR)
- **Top Global Matches:** file_cluster_8: 11.68, file_cluster_17: 11.962, file_cluster_7: 12.189
- **Magnitude:** 415.04 | **LOC:** 804 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0389%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_all_simple_paths_on_non_trivial_gra` (Impact: 8.2)
  * `test_all_simple_edge_paths_on_non_trivia` (Impact: 8.2)
  * `cost` (Impact: 8.2)
  * `test_directed_weighted_shortest_simple_p` (Impact: 7.6)
  * `test_weighted_shortest_simple_path` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 210`, `args: 88`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `duplicate_logic: 20`, `orphaned_logic: 64`
* *Architecture:* `api: 89`, `import: 8`
* *Defense:* `safety: 101`, `doc: 12`, `test: 200`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` itertools, networkx.algorithms.simple_paths, random, pytest, networkx, networkx.utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/connectivity/edge_augmentation.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.647 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.076 IQR)
- **Top Global Matches:** file_cluster_0: 10.647, file_cluster_7: 10.814, file_cluster_8: 10.835
- **Magnitude:** 399.5 | **LOC:** 1271 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.6607%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `greedy_k_edge_augmentation` (Impact: 44.4)
  * `unconstrained_bridge_augmentation` (Impact: 43.8)
    * *Intent:* """Finds augmentation that k-edge-connects as much of the graph as possible. When a k-edge-augmentat...
  * `weighted_bridge_augmentation` (Impact: 39.4)
  * `k_edge_augmentation` (Impact: 38.8)
    * *Intent:* # First try to quickly determine if G is not k-edge-connected if G.number_of_nodes() < k + 1: return...
  * `partial_k_edge_augmentation` (Impact: 29.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 62`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 24`
* *Architecture:* `api: 14`, `import: 5`
* *Defense:* `safety: 12`, `doc: 40`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` itertools, networkx.algorithms.connectivity, networkx, collections, networkx.utils, math
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tests/test_dag.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.708 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.169 IQR)
- **Top Global Matches:** file_cluster_8: 11.708, file_cluster_17: 11.973, file_cluster_0: 12.036
- **Magnitude:** 381.34 | **LOC:** 866 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (2.9252%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_reflexive_transitive_closure` (Impact: 15.5)
  * `test_topological_sort6` (Impact: 15.4)
  * `test_transitive_closure` (Impact: 12.5)
  * `test_topological_sort3` (Impact: 11.2)
  * `test_transitive_closure_dag` (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 207`, `args: 82`, `func_start: 80`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 5`, `dead_code: 2`, `duplicate_logic: 8`, `orphaned_logic: 61`
* *Architecture:* `api: 80`, `import: 5`
* *Defense:* `safety: 108`, `doc: 24`, `test: 207`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` itertools, pytest, networkx, collections, networkx.utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/flow/networksimplex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.759 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.779 IQR)
- **Top Global Matches:** file_cluster_8: 11.759, file_cluster_7: 11.882, file_cluster_13: 11.918
- **Magnitude:** 380.3 | **LOC:** 663 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.0401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `network_simplex` (Impact: 127.2)
  * `find_entering_edges` (Impact: 17.6)
  * `find_apex` (Impact: 15.0)
  * `initialize_spanning_tree` (Impact: 11.1)
  * `update_potentials` (Impact: 9.4)
    * *Intent:* # Insert the subtree rooted at q into the depth-first thread.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 36`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 103`
* *Architecture:* `api: 18`, `import: 4`
* *Defense:* `safety: 2`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.345
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` networkx, networkx.utils, itertools, math
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/simple_paths.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.369 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.207 IQR)
- **Top Global Matches:** file_cluster_13: 10.369, file_cluster_0: 10.446, file_cluster_8: 10.45
- **Magnitude:** 361.68 | **LOC:** 967 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.2423%), Tech Debt (99.9975%)
**Top Internal Functions/Classes:**
  * `_bidirectional_pred_succ` (Impact: 88.3)
  * `shortest_simple_paths` (Impact: 36.5)
    * *Intent:* -------
  * `_all_simple_edge_paths` (Impact: 24.4)
    * *Intent:* # The empty list is not a valid path. Could also return
  * `all_simple_edge_paths` (Impact: 21.0)
  * `is_simple_path` (Impact: 13.3)
    * *Intent:* """Returns True if and only if `nodes` form a simple path in `G`. A *simple path* in a graph is a no...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 70`, `args: 31`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 28`, `dead_code: 1`, `duplicate_logic: 16`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 4`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.31
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 1):` itertools, networkx, networkx.algorithms.shortest_paths.weighted, networkx.utils, functools, heapq
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/coloring/equitable_coloring.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.576 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.702 IQR)
- **Top Global Matches:** file_cluster_8: 10.576, file_cluster_7: 10.889, file_cluster_17: 10.891
- **Magnitude:** 359.06 | **LOC:** 506 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.1452%), Tech Debt (10.4072%)
**Top Internal Functions/Classes:**
  * `procedure_P` (Impact: 174.3)
  * `equitable_color` (Impact: 35.1)
  * `is_equitable` (Impact: 23.4)
    * *Intent:* """Determines if the coloring is valid and equitable for the graph G."""
  * `change_color` (Impact: 22.4)
  * `move_witnesses` (Impact: 12.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 36`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 42`, `planned_debt: 1`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 4`, `doc: 16`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.766
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001484
  * `Imports (Out-Degree: 0):` collections, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tests/test_link_prediction.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.365 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.296 IQR)
- **Top Global Matches:** file_cluster_8: 9.365, file_cluster_0: 9.866, file_cluster_7: 10.065
- **Magnitude:** 358.76 | **LOC:** 616 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6622%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test_func` (Impact: 10.2)
  * `test_invalid_delta` (Impact: 5.5)
  * `test_node_not_found` (Impact: 3.9)
  * `test_insufficient_community_information` (Impact: 3.9)
  * `test_node_not_found` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 106`, `args: 90`, `func_start: 90`, `class_start: 8`
* *Risk/State:* `state_mutation: 17`, `duplicate_logic: 81`, `orphaned_logic: 8`
* *Architecture:* `api: 97`, `import: 4`
* *Defense:* `safety: 2`, `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` networkx, functools, pytest, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/distance_measures.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.574 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.444 IQR)
- **Top Global Matches:** file_cluster_0: 10.574, file_cluster_13: 10.684, file_cluster_8: 10.689
- **Magnitude:** 356.66 | **LOC:** 1121 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (11.7565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_extrema_bounding` (Impact: 99.5)
  * `resistance_distance` (Impact: 57.2)
  * `barycenter` (Impact: 35.1)
  * `center` (Impact: 25.2)
  * `eccentricity` (Impact: 24.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 57`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`, `dead_code: 4`
* *Architecture:* `api: 11`, `import: 7`
* *Defense:* `safety: 4`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.31
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 0):` networkx, scipy, numpy, networkx.utils, math
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `networkx/algorithms/wiener.py` (PYTHON) | Magnitude: 40.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 16, branch: 15, doc: 10
- `networkx/algorithms/lowest_common_ancestors.py` (PYTHON) | Magnitude: 112.18 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, branch: 40, structural_boundaries: 21, doc: 8
- `networkx/algorithms/approximation/connectivity.py` (PYTHON) | Magnitude: 149.9 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 117, branch: 50, structural_boundaries: 24, state_mutation: 15
- `networkx/utils/tests/test_backends.py` (PYTHON) | Magnitude: 102.72 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 75, test: 52, safety: 46
- `networkx/algorithms/link_prediction.py` (PYTHON) | Magnitude: 138.48 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 49, encapsulation: 28, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `networkx/generators/tests/test_internet_as_graphs.py` (PYTHON) | Magnitude: 155.88 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 75, branch: 47, test: 44
- `networkx/algorithms/flow/maxflow.py` (PYTHON) | Magnitude: 51.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 24, encapsulation: 22, branch: 12
- `examples/subclass/plot_printgraph.py` (PYTHON) | Magnitude: 52.98 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, args: 10, func_start: 10
- `networkx/algorithms/approximation/clustering_coefficient.py` (PYTHON) | Magnitude: 13.08 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, branch: 4, decorators: 3
- `networkx/algorithms/community/label_propagation.py` (PYTHON) | Magnitude: 133.4 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 96, branch: 46, structural_boundaries: 23, doc: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tools/generate_requirements.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, generics: 3, encapsulation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `networkx/algorithms/isomorphism/isomorphvf2.py` (PYTHON) | Magnitude: 738.24 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 475, branch: 236, state_mutation: 144, structural_boundaries: 96
- `networkx/algorithms/components/tests/test_attracting.py` (PYTHON) | Magnitude: 27.96 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 28, test: 25, safety: 17
- `doc/_static/copybutton.js` (JAVASCRIPT) | Magnitude: 41.66 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 26, structural_boundaries: 12, comprehensions: 4
- `networkx/algorithms/bipartite/matching.py` (PYTHON) | Magnitude: 233.98 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 145, branch: 62, structural_boundaries: 39, state_mutation: 28
- `networkx/generators/tests/test_small.py` (PYTHON) | Magnitude: 81.22 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 172, test: 121, structural_boundaries: 118, safety: 111

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/graph/plot_morse_trie.py` (PYTHON) | Magnitude: 5.98 | Delta: **0.539 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, ui_framework: 28, branch: 9, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `networkx/generators/joint_degree_seq.py` (PYTHON) | Magnitude: 201.5 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 246, branch: 81, structural_boundaries: 31, state_mutation: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `networkx/algorithms/shortest_paths/unweighted.py` (PYTHON) | Magnitude: 207.86 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 160, branch: 63, structural_boundaries: 34, state_mutation: 24
- `networkx/algorithms/euler.py` (PYTHON) | Magnitude: 187.92 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 160, branch: 76, structural_boundaries: 36, encapsulation: 19
- `networkx/algorithms/connectivity/edge_kcomponents.py` (PYTHON) | Magnitude: 153.5 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, branch: 53, structural_boundaries: 37, doc: 24
- `networkx/algorithms/traversal/depth_first_search.py` (PYTHON) | Magnitude: 134.66 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 105, branch: 35, structural_boundaries: 20, doc: 16
- `networkx/algorithms/operators/product.py` (PYTHON) | Magnitude: 220.7 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 179, branch: 95, encapsulation: 59, structural_boundaries: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `networkx/algorithms/approximation/dominating_set.py` (PYTHON) | Magnitude: 22.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 15, doc: 8, branch: 5
- `networkx/algorithms/components/tests/test_connected.py` (PYTHON) | Magnitude: 70.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 30, test: 25, state_mutation: 17
- `networkx/generators/time_series.py` (PYTHON) | Magnitude: 10.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 5, doc: 4, branch: 3
- `networkx/algorithms/isomorphism/tests/test_tree_isomorphism.py` (PYTHON) | Magnitude: 67.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 125, test: 27, structural_boundaries: 25, branch: 16
- `networkx/algorithms/centrality/percolation.py` (PYTHON) | Magnitude: 35.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 12, branch: 9, encapsulation: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `networkx/utils/misc.py` -> Churn: **76.03%** | Cog Load: 19.0532% | Debt: 77.9618%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `networkx/drawing/nx_pylab.py` -> **NaorTIRAM** (100.0% isolated ownership) | Magnitude: 838.74
- `networkx/readwrite/gml.py` -> **Ross Barnowski** (100.0% isolated ownership) | Magnitude: 732.4
- `networkx/algorithms/isomorphism/ismags.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 620.76
- `networkx/algorithms/isomorphism/vf2pp.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 593.84
- `networkx/algorithms/tests/test_cycles.py` -> **Ross Barnowski** (100.0% isolated ownership) | Magnitude: 526.54

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `networkx/algorithms/centrality/betweenness.py` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 95.4357%)
- `networkx/algorithms/shortest_paths/weighted.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 89.0533%)
- `networkx/generators/atlas.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 81.3057%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `networkx/utils/decorators.py` -> **Severity: 1.776** (Embedded: 0.0312 * Error Risk: 56.9428%)
- `networkx/algorithms/bipartite/generators.py` -> **Severity: 0.8** (Embedded: 0.0134 * Error Risk: 59.9163%)
- `networkx/algorithms/shortest_paths/weighted.py` -> **Severity: 0.616** (Embedded: 0.0106 * Error Risk: 58.358%)
- `networkx/generators/community.py` -> **Severity: 0.578** (Embedded: 0.0106 * Error Risk: 54.7587%)
- `networkx/generators/classic.py` -> **Severity: 0.537** (Embedded: 0.012 * Error Risk: 44.6938%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `networkx/algorithms/flow/utils.py` -> **Severity: 841.2** (Blast Radius: 8.412 * Doc Risk: 100.0%)
- `networkx/algorithms/centrality/flow_matrix.py` -> **Severity: 452.513** (Blast Radius: 4.535 * Doc Risk: 99.7824%)
- `networkx/algorithms/traversal/edgedfs.py` -> **Severity: 373.765** (Blast Radius: 4.611 * Doc Risk: 81.0595%)
- `networkx/utils/configs.py` -> **Severity: 287.738** (Blast Radius: 3.008 * Doc Risk: 95.6575%)
- `networkx/utils/decorators.py` -> **Severity: 233.042** (Blast Radius: 19.55 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
