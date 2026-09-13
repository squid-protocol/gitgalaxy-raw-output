# ARCHITECTURAL_BRIEF: networkx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/networkx/networkx.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 970 |
| Analyzed Artifacts (Scanned) | 684 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 286 |
| Total LOC | 90318 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 70.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8375 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2806 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.3616 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 72 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 654 | 89566 | 95.6% |
| PLAINTEXT | 15 | 0 | 2.2% |
| MARKDOWN | 5 | 0 | 0.7% |
| JSON | 2 | 75 | 0.3% |
| JAVASCRIPT | 2 | 120 | 0.3% |
| CSS | 2 | 33 | 0.3% |
| MAKEFILE | 1 | 96 | 0.1% |
| XML | 1 | 0 | 0.1% |
| HTML | 1 | 12 | 0.1% |
| PHP | 1 | 416 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 664 | 97.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 20 | 2.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 286*

**Composition by Extension & Reason:**
- `.rst`: 131x Excluded (Unsupported Extension: '.rst'), 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 81 LOC), 1x Excluded (Machine-Generated Source Code Signature: 156 LOC)
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 10x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 3x Excluded (Machine-Generated Source Code Signature: 5 LOC), 3x Excluded (Machine-Generated Source Code Signature: 7 LOC), 2x Excluded (Machine-Generated Source Code Signature: 11 LOC)
- `.bz2`: 5x Excluded (Explicitly Denied Extension: '.bz2')
- `.gz`: 4x Excluded (Explicitly Denied Extension: '.gz')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 40 LOC)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.edgelist`: 2x Excluded (Unsupported Extension: '.edgelist')
- `.zip`: 2x Excluded (Explicitly Denied Extension: '.zip')
- `.geojson`: 2x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.a99`: 2x Excluded (Unsupported Extension: '.A99')
- `.b99`: 2x Excluded (Unsupported Extension: '.B99')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.1 | 27.5 | 29.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 70.5 | 80.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 80.9 | 16.7 | 11.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 76.4 | 1.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 83.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.6 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 84.5 | 6.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 52.7 | 61.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3296 | 415 | 13 | `networkx/algorithms/tests/test_simple_paths.py` |
| cleanup | 34 | 7 | 0 | `networkx/drawing/tests/test_pylab.py` |
| guards | 8838 | 422 | 38 | `networkx/generators/tests/test_classic.py` |
| danger | 2239 | 336 | 10 | `networkx/utils/backends.py` |
| concurrency | 421 | 90 | 1 | `networkx/readwrite/gml.py` |
| connectivity | 6721 | 548 | 25 | `networkx/algorithms/tests/test_distance_measures.py` |
| io | 62 | 28 | 0 | `doc/Makefile` |
| crypto | 1 | 1 | 0 | `networkx/algorithms/graph_hashing.py` |
| ipc | 1 | 1 | 0 | `examples/algorithms/plot_parallel_betweenness.py` |
| time | 21 | 4 | 0 | `networkx/algorithms/isomorphism/tests/test_temporalisomorphvf2.py` |
| serialization | 8 | 5 | 0 | `networkx/utils/tests/test_backends.py` |
| regex | 8 | 4 | 0 | `networkx/readwrite/gml.py` |
| events | 8 | 1 | 0 | `examples/external/force/force.js` |
| tests | 6565 | 255 | 32 | `networkx/algorithms/tests/test_distance_measures.py` |
| docs | 2754 | 514 | 10 | `networkx/algorithms/planarity.py` |
| debt | 391 | 115 | 1 | `networkx/algorithms/tests/test_link_prediction.py` |
| mutation | 53420 | 612 | 201 | `networkx/algorithms/isomorphism/tests/test_vf2pp_helpers.py` |
| dead_code | 3796 | 334 | 19 | `networkx/algorithms/tests/test_distance_measures.py` |
| credential | 0 | 0 | 0 | - |
| threat | 204 | 83 | 1 | `networkx/utils/backends.py` |
| ml_ai | 349 | 139 | 1 | `networkx/drawing/nx_pylab.py` |
| ui | 28 | 1 | 0 | `examples/graph/plot_morse_trie.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5336**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/Makefile` (Hits: 8)
- `networkx/readwrite/tests/test_gml.py` (Hits: 6)
- `networkx/utils/decorators.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **decorators.py** (`networkx/utils/decorators.py`) — 18 inbound connections
2. **generators.py** (`networkx/algorithms/bipartite/generators.py`) — 9 inbound connections
3. **classic.py** (`networkx/generators/classic.py`) — 8 inbound connections
4. **community.py** (`networkx/generators/community.py`) — 7 inbound connections
5. **weighted.py** (`networkx/algorithms/shortest_paths/weighted.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`networkx/generators/__init__.py`) — 29 outbound dependencies
2. **backends.py** (`networkx/utils/backends.py`) — 22 outbound dependencies
3. **__init__.py** (`networkx/algorithms/centrality/__init__.py`) — 20 outbound dependencies
4. **lazy_imports.py** (`networkx/lazy_imports.py`) — 18 outbound dependencies
5. **__init__.py** (`networkx/algorithms/approximation/__init__.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `optimize_edit_paths` (@ `networkx/algorithms/similarity.py`) -> Impact: **722.2** | LOC: 656
- `max_weight_matching` (@ `networkx/algorithms/matching.py`) -> Impact: **395.4** | LOC: 828
  * *Intent:* """Compute a maximum-weighted matching of G. A matching is a subset of edges in which no node occurs more than once. The weight of a matching is the s...
- `display` (@ `networkx/drawing/nx_pylab.py`) -> Impact: **291.6** | LOC: 832
- `_call_if_any_backends_installed` (@ `networkx/utils/backends.py`) -> Impact: **266.1** | LOC: 492
  * *Intent:* # Dispatch to backends based on inputs, `backend=` arg, or configuration """Returns the result of the original function, or the backend function if th...
- `draw_networkx_edges` (@ `networkx/drawing/nx_pylab.py`) -> Impact: **263.1** | LOC: 371
- `_convert_and_call_for_tests` (@ `networkx/utils/backends.py`) -> Impact: **237.6** | LOC: 293
- `__new__` (@ `networkx/utils/backends.py`) -> Impact: **207.8** | LOC: 265
- `preflow_push_impl` (@ `networkx/algorithms/flow/preflowpush.py`) -> Impact: **205.7** | LOC: 267
  * *Intent:* """Implementation of the highest-label preflow-push algorithm."""
- `syntactic_feasibility` (@ `networkx/algorithms/isomorphism/isomorphvf2.py`) -> Impact: **191.1** | LOC: 221
  * *Intent:* """Returns True if adding (G1_node, G2_node) is syntactically feasible. This function returns True if it is adding the candidate pair to the current p...
- `_convert_arguments` (@ `networkx/utils/backends.py`) -> Impact: **190.4** | LOC: 210
  * *Intent:* """Convert graph arguments to the specified backend. Returns ------- args tuple and kwargs dict """

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `networkx/algorithms` | 55 | 15686.12 | 38.57% | 7.26% |
| `networkx/algorithms/tests` | 58 | 9779.44 | 18.47% | 0.0% |
| `networkx/generators` | 29 | 6290.0 | 32.54% | 2.88% |
| `networkx/readwrite` | 13 | 5270.54 | 42.63% | 1.67% |
| `networkx/utils` | 10 | 4333.88 | 41.64% | 5.96% |
| `networkx/algorithms/isomorphism` | 9 | 3923.56 | 40.56% | 17.77% |
| `networkx/algorithms/isomorphism/tests` | 11 | 3559.1 | 26.05% | 0.0% |
| `networkx/generators/tests` | 29 | 3355.3 | 15.4% | 0.0% |
| `networkx/algorithms/centrality/tests` | 21 | 3315.7 | 19.08% | 0.0% |
| `networkx/algorithms/centrality` | 22 | 3210.74 | 43.28% | 7.91% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmarks/benchmarks/benchmark_classes.py` -> **100.0%** Exposure
- `networkx/algorithms/centrality/reaching.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_neighbors.py` -> **99.9996%** Exposure
- `networkx/algorithms/simple_paths.py` -> **99.9975%** Exposure
- `benchmarks/benchmarks/benchmark_chordal.py` -> **99.9972%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmarks/benchmarks/benchmark_algorithms.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_harmonic_centrality.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/benchmark_regular.py` -> **100.0%** Exposure
- `doc/conf.py` -> **100.0%** Exposure
- `networkx/algorithms/approximation/clique.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `networkx/algorithms/tests/test_distance_measures.py` -> **93** Orphaned Functions | **3** Duplicates
- `networkx/algorithms/tests/test_simple_paths.py` -> **79** Orphaned Functions | **4** Duplicates
- `networkx/drawing/tests/test_pylab.py` -> **79** Orphaned Functions | **0** Duplicates
- `networkx/algorithms/tests/test_similarity.py` -> **63** Orphaned Functions | **0** Duplicates
- `networkx/algorithms/tests/test_dag.py` -> **61** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `2170` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `networkx/algorithms/simple_paths.py` (PYTHON) -> Cumulative Risk: **696.24**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 699.18 | **LOC:** 967 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9975%), Safety Score (99.2597%)
- **Heaviest Functions:** `_bidirectional_dijkstra` (Impact: 113.4), `_bidirectional_pred_succ` (Impact: 88.4), `shortest_simple_paths` (Impact: 38.7)

### 2. `benchmarks/benchmarks/benchmark_algorithms.py` (PYTHON) -> Cumulative Risk: **677.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 168.54 | **LOC:** 247 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.996%), Documentation (95.4545%)
- **Heaviest Functions:** `_make_weighted_benchmark_graphs` (Impact: 13.6), `dijkstra_relaxation_worst_case` (Impact: 5.2), `_make_tournament_benchmark_graphs` (Impact: 3.2)

### 3. `networkx/algorithms/centrality/closeness.py` (PYTHON) -> Cumulative Risk: **649.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 199.92 | **LOC:** 307 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.7959%)
- **Heaviest Functions:** `incremental_closeness_centrality` (Impact: 48.7), `closeness_centrality` (Impact: 46.5)

### 4. `networkx/algorithms/link_analysis/pagerank_alg.py` (PYTHON) -> Cumulative Risk: **636.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 299.48 | **LOC:** 502 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.2339%)
- **Heaviest Functions:** `_pagerank_python` (Impact: 59.9), `_pagerank_scipy` (Impact: 49.2), `google_matrix` (Impact: 31.1)

### 5. `networkx/readwrite/gexf.py` (PYTHON) -> Cumulative Risk: **627.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1428.82 | **LOC:** 1085 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9212%), Documentation (87.6923%)
- **Heaviest Functions:** `add_attributes` (Impact: 64.5), `make_graph` (Impact: 38.5), `add_edge` (Impact: 33.9)

### 6. `networkx/conftest.py` (PYTHON) -> Cumulative Risk: **611.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 120.2 | **LOC:** 265 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Tech Debt (90.5175%)
- **Heaviest Functions:** `pytest_collection_modifyitems` (Impact: 13.2), `pytest_configure` (Impact: 11.5), `pytest_addoption` (Impact: 3.7)

### 7. `networkx/algorithms/similarity.py` (PYTHON) -> Cumulative Risk: **607.5**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1999.62 | **LOC:** 2108 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.1799%), Documentation (95.2381%)
- **Heaviest Functions:** `optimize_edit_paths` (Impact: 722.2), `match_edges` (Impact: 118.5), `get_edit_ops` (Impact: 103.9)

### 8. `networkx/algorithms/centrality/betweenness.py` (PYTHON) -> Cumulative Risk: **601.33**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 462.66 | **LOC:** 597 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.9137%)
- **Heaviest Functions:** `_rescale` (Impact: 74.3), `betweenness_centrality` (Impact: 38.6), `edge_betweenness_centrality` (Impact: 31.9)

### 9. `networkx/drawing/nx_pylab.py` (PYTHON) -> Cumulative Risk: **595.49**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2172.74 | **LOC:** 2979 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.4149%), Verification (80.0%)
- **Heaviest Functions:** `display` (Impact: 291.6), `draw_networkx_edges` (Impact: 263.1), `draw_networkx_edge_labels` (Impact: 138.7)

### 10. `networkx/algorithms/centrality/reaching.py` (PYTHON) -> Cumulative Risk: **595.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 122.44 | **LOC:** 210 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (97.883%)
- **Heaviest Functions:** `local_reaching_centrality` (Impact: 38.7), `global_reaching_centrality` (Impact: 18.2), `_average_weight` (Impact: 9.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `networkx/utils/backends.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2299.88 | **LOC:** 2184 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (86.8552%), Tech Debt (9.9859%)
**Top Internal Functions/Classes:**
  * `_call_if_any_backends_installed` (Impact: 266.1)
    * *Intent:* # Dispatch to backends based on inputs, `backend=` arg, or configuration """Returns the result of th...
  * `_convert_and_call_for_tests` (Impact: 237.6)
  * `__new__` (Impact: 207.8)
  * `_convert_arguments` (Impact: 190.4)
    * *Intent:* """Convert graph arguments to the specified backend. Returns ------- args tuple and kwargs dict """
  * `_convert_graph` (Impact: 85.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 833
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 505`, `structural_boundaries: 259`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 293`, `dead_code: 4`, `planned_debt: 8`
* *Architecture:* `api: 8`, `import: 22`
* *Defense:* `safety: 96`, `doc: 22`, `test: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.351
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001462
  * `Imports (Out-Degree: 2):` .configs, .decorators, collections.abc, copy, finishes., functools, importlib.metadata, inspect...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/drawing/nx_pylab.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2172.74 | **LOC:** 2979 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.8941%), Tech Debt (8.1229%)
**Top Internal Functions/Classes:**
  * `display` (Impact: 291.6)
  * `draw_networkx_edges` (Impact: 263.1)
  * `draw_networkx_edge_labels` (Impact: 138.7)
  * `draw_networkx_nodes` (Impact: 70.3)
  * `__call__` (Impact: 62.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 251 instances
* *State Mutation (weighted view):* 796
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 181`, `args: 46`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 294`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 45`, `import: 42`
* *Defense:* `safety: 48`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001462
  * `Imports (Out-Degree: 0):` collections, collections.abc, inspect, itertools, math, matplotlib, matplotlib.cm, matplotlib.collections...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/similarity.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1999.62 | **LOC:** 2108 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.6731%), Tech Debt (8.5027%)
**Top Internal Functions/Classes:**
  * `optimize_edit_paths` (Impact: 722.2)
  * `match_edges` (Impact: 118.5)
    * *Intent:* """ Parameters: u, v: matched vertices, u=None or v=None for deletion/insertion pending_g, pending_h...
  * `get_edit_ops` (Impact: 103.9)
  * `get_edit_paths` (Impact: 100.6)
  * `_simrank_similarity_python` (Impact: 61.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 167 instances
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 99`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 182`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 22`, `import: 15`
* *Defense:* `safety: 2`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 0):` dataclasses, itertools, math, networkx, networkx.utils, numpy, pprint, scipy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/readwrite/gexf.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1428.82 | **LOC:** 1085 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.2016%), Tech Debt (11.5059%)
**Top Internal Functions/Classes:**
  * `add_attributes` (Impact: 64.5)
    * *Intent:* # Add attrvalues to node or edge attvalues = Element("attvalues") if len(data) == 0: return data mod...
  * `make_graph` (Impact: 38.5)
    * *Intent:* # start with empty DiGraph or MultiDiGraph edgedefault = graph_xml.get("defaultedgetype", None) if e...
  * `add_edge` (Impact: 33.9)
    * *Intent:* # add an edge to the graph # raise error if we find mixed directed and undirected edges edge_directi...
  * `add_edges` (Impact: 27.4)
  * `indent` (Impact: 26.8)
    * *Intent:* # in-place prettyprint formatter i = "\n" + " " * level if len(elem): if not elem.text or not elem.t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 277 instances
* *State Mutation (weighted view):* 901
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 97`, `args: 33`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 347`, `dead_code: 6`, `fragile_debt: 2`
* *Architecture:* `api: 35`, `import: 6`
* *Defense:* `safety: 29`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001462
  * `Imports (Out-Degree: 0):` itertools, networkx, networkx.utils, numpy, time, xml.etree.ElementTree
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/matching.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1340.7 | **LOC:** 1149 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.9295%), Tech Debt (13.2964%)
**Top Internal Functions/Classes:**
  * `max_weight_matching` (Impact: 395.4)
    * *Intent:* """Compute a maximum-weighted matching of G. A matching is a subset of edges in which no node occurs...
  * `addBlossom` (Impact: 60.6)
    * *Intent:* # Construct a new blossom with given base, through S-vertices v and w. # Label the new blossom as S;...
  * `expandBlossom` (Impact: 52.4)
    * *Intent:* # Expand the given top-level blossom. # This is an obnoxiously complicated recursive function for th...
  * `_recurse` (Impact: 46.2)
    * *Intent:* # This is an obnoxiously complicated recursive function for the sake of # a stack-transformation. So...
  * `is_maximal_matching` (Impact: 28.9)
    * *Intent:* """Return True if ``matching`` is a maximal matching of ``G`` A *maximal matching* in a graph is a m...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 100`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 196`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 43`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001462
  * `Imports (Out-Degree: 0):` itertools, networkx, networkx.utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/planarity.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1235.56 | **LOC:** 1489 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.5641%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `add_constraints` (Impact: 38.1)
  * `add_half_edge` (Impact: 35.5)
    * *Intent:* """Adds a half-edge from `start_node` to `end_node`. If the half-edge is not the first one out of `s...
  * `remove_back_edges` (Impact: 33.1)
  * `dfs_orientation` (Impact: 25.1)
    * *Intent:* """Orient the graph by DFS, compute lowpoints and nesting order."""
  * `dfs_testing` (Impact: 23.2)
    * *Intent:* """Test for LR partition."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 672
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 120`, `args: 61`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 250`, `dead_code: 1`
* *Architecture:* `api: 47`, `import: 3`
* *Defense:* `safety: 6`, `doc: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 0):` collections, copy, networkx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/drawing/tests/test_pylab.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1144.74 | **LOC:** 1583 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.5247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_display_edge_style` (Impact: 21.2)
  * `test_display_edge_position` (Impact: 17.0)
  * `test_display_edge_single_color` (Impact: 16.9)
  * `test_individualized_font_attributes` (Impact: 16.6)
  * `test_display_edge_width` (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 626
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 221`, `args: 81`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 268`, `unreferenced_by_name: 79`
* *Architecture:* `api: 81`, `import: 12`
* *Defense:* `safety: 160`, `doc: 28`, `test: 137`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` itertools, matplotlib.collections, matplotlib.patches, networkx, os, pytest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/cycles.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1138.62 | **LOC:** 1235 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (57.5726%), Tech Debt (9.1779%)
**Top Internal Functions/Classes:**
  * `chordless_cycles` (Impact: 105.9)
    * *Intent:* """Find simple chordless cycles of a graph. A `simple cycle` is a closed path where no node appears ...
  * `simple_cycles` (Impact: 60.3)
    * *Intent:* """Find simple cycles (elementary circuits) of a graph. A "simple cycle", or "elementary circuit", i...
  * `find_cycle` (Impact: 53.9)
    * *Intent:* """Returns a cycle found via depth-first traversal. The cycle is a list of edges indicating the cycl...
  * `_chordless_cycle_search` (Impact: 35.1)
    * *Intent:* """The main loop for chordless cycle enumeration. This algorithm is strongly inspired by that of Dia...
  * `_min_cycle` (Impact: 34.5)
    * *Intent:* """ Computes the minimum weight cycle in G, orthogonal to the vector orth as per [p. 338, 1] Use (u,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 593
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 81`, `args: 24`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 201`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `safety: 3`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001462
  * `Imports (Out-Degree: 0):` collections, itertools, math, networkx, networkx.utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/ismags.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1110.56 | **LOC:** 1314 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.1813%), Tech Debt (35.8026%)
**Top Internal Functions/Classes:**
  * `_map_nodes` (Impact: 102.7)
    * *Intent:* """ Find all subgraph isomorphisms honoring constraints. The collection `candidate_sets` is stored a...
  * `_process_ordered_pair_partitions` (Impact: 71.1)
  * `create_aligned_partitions` (Impact: 62.8)
    * *Intent:* """Partitions of "things" (nodes or edges) from subgraph and graph based on function `thing_matcher`...
  * `_refine_opp` (Impact: 53.9)
  * `make_partition` (Impact: 41.3)
    * *Intent:* """ Partitions items into sets based on the outcome of ``test(item1, item2)``. Pairs of items for wh...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 110`, `args: 36`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 184`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 6`, `doc: 23`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001462
  * `Imports (Out-Degree: 0):` collections, functools, itertools, networkx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/generators/random_graphs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1110.56 | **LOC:** 1496 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (49.5463%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extended_barabasi_albert_graph` (Impact: 87.5)
    * *Intent:* """Returns an extended Barabási–Albert model graph. An extended Barabási–Albert model graph is a ran...
  * `dual_barabasi_albert_graph` (Impact: 64.4)
  * `random_regular_graph` (Impact: 50.5)
  * `fast_gnp_random_graph` (Impact: 38.1)
    * *Intent:* """Returns a $G_{n,p}$ random graph, also known as an Erdős-Rényi graph or a binomial graph. Paramet...
  * `powerlaw_cluster_graph` (Impact: 36.3)
    * *Intent:* """Holme and Kim algorithm for growing graphs with powerlaw degree distribution and approximate aver...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 83`, `args: 24`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 178`, `dead_code: 3`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.258
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001462
  * `Imports (Out-Degree: 3):` ..utils.misc, .classic, .degree_seq, collections, itertools, math, networkx, networkx.utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/tests/test_vf2pp_helpers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1076.08 | **LOC:** 1315 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.1876%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_covered_neighbors_no_labels` (Impact: 28.9)
  * `test_feasible_look_ahead_same_labels` (Impact: 28.4)
  * `test_covered_neighbors_with_labels` (Impact: 27.9)
  * `test_no_covered_neighbors_no_labels` (Impact: 22.7)
  * `test_same_in_out_degrees_no_candidate` (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 123`, `args: 23`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `state_mutation: 442`, `unreferenced_by_name: 22`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 88`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` itertools, networkx, networkx.algorithms.isomorphism.vf2pp, operator, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/shortest_paths/weighted.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1050.02 | **LOC:** 2543 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.0604%), Tech Debt (9.0458%)
**Top Internal Functions/Classes:**
  * `_dijkstra_multisource` (Impact: 79.7)
  * `_inner_bellman_ford` (Impact: 67.0)
  * `bidirectional_dijkstra` (Impact: 63.4)
  * `goldberg_radzik` (Impact: 55.0)
    * *Intent:* """Compute shortest path lengths and predecessors on shortest paths in weighted graphs. The algorith...
  * `_bellman_ford` (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 142 instances
* *State Mutation (weighted view):* 433
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 110`, `args: 37`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 149`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 31`, `import: 5`
* *Defense:* `safety: 13`, `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.482
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.010406
  * `Imports (Out-Degree: 1):` collections, heapq, itertools, networkx, networkx.algorithms.shortest_paths.generic
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `networkx/algorithms/approximation/traveling_salesman.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1034.78 | **LOC:** 1509 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.271%), Tech Debt (9.1852%)
**Top Internal Functions/Classes:**
  * `held_karp_ascent` (Impact: 98.7)
    * *Intent:* """ Minimizes the Held-Karp relaxation of the TSP for `G` Solves the Held-Karp relaxation of the inp...
  * `simulated_annealing_tsp` (Impact: 87.6)
  * `threshold_accepting_tsp` (Impact: 84.4)
  * `asadpour_atsp` (Impact: 63.7)
    * *Intent:* """ Returns an approximate solution to the traveling salesman problem. This approximate solution is ...
  * `traveling_salesman_problem` (Impact: 47.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 76`, `args: 20`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 174`, `planned_debt: 1`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `safety: 3`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.334
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 1):` math, networkx, networkx.algorithms, networkx.algorithms.approximation, networkx.algorithms.tree.mst, networkx.utils, numpy, scipy
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/threshold.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1002.04 | **LOC:** 982 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4549%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `creation_sequence` (Impact: 34.9)
    * *Intent:* """ Determines the creation sequence for the given threshold degree sequence. The creation sequence ...
  * `weights_to_creation_sequence` (Impact: 34.3)
    * *Intent:* # return wseq
  * `shortest_path` (Impact: 30.6)
    * *Intent:* """ Find the shortest path between u and v in a threshold graph G with the given creation_sequence. ...
  * `shortest_path_length` (Impact: 28.2)
    * *Intent:* """ Return the shortest path length from indicated node to every other node for the threshold graph ...
  * `creation_sequence_to_weights` (Impact: 24.8)
    * *Intent:* """ Returns a list of node weights which create the threshold graph designated by the creation seque...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 87`, `args: 26`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 214`, `dead_code: 5`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 22`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001462
  * `Imports (Out-Degree: 0):` math, networkx, networkx.algorithms.threshold, networkx.utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/readwrite/gml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 984.6 | **LOC:** 883 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.1573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_gml_lines` (Impact: 175.4)
    * *Intent:* """Parse GML `lines` into a graph."""
  * `stringize` (Impact: 86.5)
  * `generate_gml` (Impact: 83.9)
  * `literal_stringizer` (Impact: 46.0)
    * *Intent:* """Convert a `value` to a Python literal in GML representation. Parameters ---------- value : object...
  * `stringize` (Impact: 44.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 87`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 121`
* *Architecture:* `api: 27`, `import: 9`
* *Defense:* `safety: 45`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 0):` ast, collections, enum, html.entities, io, networkx, networkx.utils, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/isomorphvf2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 932.14 | **LOC:** 1263 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.99%), Tech Debt (9.1743%)
**Top Internal Functions/Classes:**
  * `syntactic_feasibility` (Impact: 191.1)
    * *Intent:* """Returns True if adding (G1_node, G2_node) is syntactically feasible. This function returns True i...
  * `syntactic_feasibility` (Impact: 78.1)
    * *Intent:* """Returns True if adding (G1_node, G2_node) is syntactically feasible. This function returns True i...
  * `__init__` (Impact: 69.9)
    * *Intent:* """Initializes DiGMState object. Pass in the DiGraphMatcher to which this DiGMState belongs and the ...
  * `__init__` (Impact: 41.1)
    * *Intent:* """Initializes GMState object. Pass in the GraphMatcher to which this GMState belongs and the new no...
  * `candidate_pairs_iter` (Impact: 29.1)
    * *Intent:* """Iterator over candidate pairs of nodes in G1 and G2."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 96`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 130`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 26`, `import: 2`
* *Defense:* `safety: 6`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.385
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 0):` networkx, networkx.algorithms, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tests/test_cycles.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 929.44 | **LOC:** 983 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.5956%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_cycle` (Impact: 42.3)
  * `check_cycle_algorithm` (Impact: 37.1)
  * `test_chordless_cycles_giant_hamiltonian` (Impact: 20.7)
    * *Intent:* # ... o - e - o - e - o ... # o = odd, e = even # ... ---/ \-----/ \--- ... # <-- "long" edges # # e...
  * `test_simple_cycles_notable_clique_sequences` (Impact: 20.6)
    * *Intent:* # A000292: Number of labeled graphs on n+3 nodes that are triangles. g_family = [self.K(n) for n in ...
  * `test_chordless_cycles_directed` (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 183`, `args: 75`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 229`, `unreferenced_by_name: 55`
* *Architecture:* `api: 78`, `import: 6`
* *Defense:* `safety: 68`, `doc: 1`, `test: 71`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` itertools, math, networkx, networkx.algorithms.traversal.edgedfs, pytest, random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/readwrite/graphml.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 888.72 | **LOC:** 1054 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.2277%), Tech Debt (10.1988%)
**Top Internal Functions/Classes:**
  * `add_graph_element` (Impact: 45.0)
    * *Intent:* """ Serialize graph G in GraphML to the stream. """
  * `decode_data_elements` (Impact: 36.9)
    * *Intent:* """Use the key information to decode the data XML if present."""
  * `make_graph` (Impact: 36.3)
    * *Intent:* # set default graph type edgedefault = graph_xml.get("edgedefault", None) if G is None: if edgedefau...
  * `indent` (Impact: 26.8)
    * *Intent:* # in-place prettyprint formatter i = "\n" + level * " " if len(elem): if not elem.text or not elem.t...
  * `attr_type` (Impact: 23.6)
    * *Intent:* """Infer the attribute type of data named name. Currently this only supports inference of numeric ty...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 453
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 107`, `args: 33`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 181`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `safety: 11`, `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 0):` collections, lxml.etree, networkx, networkx.utils, numpy, warnings, xml.etree.ElementTree
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/vf2pp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 866.84 | **LOC:** 1066 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (58.817%), Tech Debt (9.1057%)
**Top Internal Functions/Classes:**
  * `_restore_Tinout_Di` (Impact: 91.3)
    * *Intent:* # If the node to remove from the mapping has >=1 covered neighbor, add it to T1. _, _, directed, FG,...
  * `_feasible_look_ahead` (Impact: 81.3)
  * `_feasible_node_pair` (Impact: 80.7)
  * `_all_morphisms` (Impact: 49.4)
  * `_find_candidates_Di` (Impact: 48.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 84`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 115`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 16`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.425
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004386
  * `Imports (Out-Degree: 0):` collections, networkx, operator
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tree/branchings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 806.56 | **LOC:** 1035 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (40.708%), Tech Debt (10.2581%)
**Top Internal Functions/Classes:**
  * `maximum_branching` (Impact: 153.5)
  * `edmonds_step_I2` (Impact: 34.3)
    * *Intent:* """ Perform step I2 from Edmonds' paper First, check if the last step I1 created a cycle. If it did ...
  * `greedy_branching` (Impact: 33.2)
    * *Intent:* """ Returns a branching obtained through a greedy algorithm. This algorithm is wrong, and cannot giv...
  * `_write_partition` (Impact: 22.5)
    * *Intent:* """ Writes the desired partition into the graph to calculate the minimum spanning tree. Also, if one...
  * `maximum_spanning_arborescence` (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 372
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 66`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 140`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 19`, `import: 7`
* *Defense:* `safety: 8`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 1):` .recognition, dataclasses, networkx, networkx.utils, operator, queue, string
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tree/mst.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 763.48 | **LOC:** 1323 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (37.7905%), Tech Debt (10.3557%)
**Top Internal Functions/Classes:**
  * `prim_mst_edges` (Impact: 103.0)
    * *Intent:* """Iterate over edges of Prim's algorithm min/max spanning tree. Parameters ---------- G : NetworkX ...
  * `kruskal_mst_edges` (Impact: 82.1)
  * `random_spanning_tree` (Impact: 58.2)
    * *Intent:* """ Sample a random spanning tree using the edges weights of `G`. This function supports two differe...
  * `boruvka_mst_edges` (Impact: 52.3)
  * `number_of_spanning_trees` (Impact: 24.6)
    * *Intent:* """Returns the number of spanning trees in `G`. A spanning tree for an undirected graph is a tree th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 91`, `args: 21`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 119`, `planned_debt: 2`
* *Architecture:* `api: 19`, `import: 10`
* *Defense:* `safety: 4`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005221
  * `Imports (Out-Degree: 0):` dataclasses, enum, heapq, itertools, math, networkx, networkx.algorithms, networkx.utils...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `networkx/algorithms/simple_paths.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 699.18 | **LOC:** 967 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.4937%), Tech Debt (99.9975%)
**Top Internal Functions/Classes:**
  * `_bidirectional_dijkstra` (Impact: 113.4)
  * `_bidirectional_pred_succ` (Impact: 88.4)
    * *Intent:* """Bidirectional shortest path helper. Returns (pred,succ,w) where pred is a dictionary of predecess...
  * `shortest_simple_paths` (Impact: 38.7)
    * *Intent:* """Generate all simple paths in the graph G from source to target, starting from shortest ones. A si...
  * `_all_simple_edge_paths` (Impact: 24.4)
    * *Intent:* # We simulate recursion with a stack, keeping the current path being explored # and the outgoing edg...
  * `all_simple_edge_paths` (Impact: 23.7)
    * *Intent:* """Generate lists of edges for all simple paths in G from source to target. A simple path is a path ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 70`, `args: 31`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 92`, `dead_code: 1`, `duplicate_logic: 16`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 4`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.276
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 1):` functools, heapq, itertools, networkx, networkx.algorithms.shortest_paths.weighted, networkx.utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/readwrite/text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 689.1 | **LOC:** 852 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.305%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate_network_text` (Impact: 173.4)
  * `_parse_network_text` (Impact: 65.4)
    * *Intent:* """Reconstructs a graph from a network text representation. This is mainly used for testing. Network...
  * `write_network_text` (Impact: 26.0)
  * `_find_sources` (Impact: 13.1)
    * *Intent:* """ Determine a minimal set of nodes such that the entire graph is reachable """
  * `as_dict` (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 38`, `args: 9`, `func_start: 5`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 134`
* *Architecture:* `io: 1`, `api: 14`, `import: 7`
* *Defense:* `safety: 5`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 0):` collections, itertools, networkx, networkx.utils, sys, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/convert_matrix.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 681.06 | **LOC:** 1320 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.2656%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `from_numpy_array` (Impact: 90.5)
  * `to_numpy_array` (Impact: 79.7)
  * `from_pandas_edgelist` (Impact: 67.0)
  * `to_scipy_sparse_array` (Impact: 47.9)
    * *Intent:* """Returns the graph adjacency matrix as a SciPy sparse array. Parameters ---------- G : graph The N...
  * `to_pandas_edgelist` (Impact: 44.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 62`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 97`, `dead_code: 4`
* *Architecture:* `api: 9`, `import: 9`
* *Defense:* `safety: 9`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004386
  * `Imports (Out-Degree: 0):` collections, itertools, networkx, numpy, pandas, scipy
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/connectivity/edge_augmentation.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 676.1 | **LOC:** 1271 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.0662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `greedy_k_edge_augmentation` (Impact: 44.6)
    * *Intent:* """Greedy algorithm for finding a k-edge-augmentation Parameters ---------- G : NetworkX graph An un...
  * `k_edge_augmentation` (Impact: 39.2)
    * *Intent:* """Finds set of edges to k-edge-connect G. Adding edges from the augmentation to G make it impossibl...
  * `unconstrained_bridge_augmentation` (Impact: 38.7)
    * *Intent:* """Finds an optimal 2-edge-augmentation of G using the fewest edges. This is an implementation of th...
  * `weighted_bridge_augmentation` (Impact: 38.4)
    * *Intent:* """Finds an approximate min-weight 2-edge-augmentation of G. This is an implementation of the approx...
  * `partial_k_edge_augmentation` (Impact: 31.7)
    * *Intent:* """Finds augmentation that k-edge-connects as much of the graph as possible. When a k-edge-augmentat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 96 instances
* *State Mutation (weighted view):* 298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 65`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 106`
* *Architecture:* `api: 14`, `import: 5`
* *Defense:* `safety: 12`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.467
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002924
  * `Imports (Out-Degree: 0):` collections, itertools, math, networkx, networkx.algorithms.connectivity, networkx.utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `networkx/conftest.py` -> Churn: **70.01%** | Cog Load: 61.5222% | Debt: 90.5175%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `networkx/drawing/nx_pylab.py` -> **NaorTIRAM** (100.0% isolated ownership) | Magnitude: 2172.74
- `networkx/readwrite/gexf.py` -> **Ross Barnowski** (100.0% isolated ownership) | Magnitude: 1428.82
- `networkx/algorithms/planarity.py` -> **Varand Arakelian** (100.0% isolated ownership) | Magnitude: 1235.56
- `networkx/drawing/tests/test_pylab.py` -> **NaorTIRAM** (100.0% isolated ownership) | Magnitude: 1144.74
- `networkx/algorithms/isomorphism/ismags.py` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1110.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `networkx/algorithms/centrality/betweenness.py` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)
- `networkx/algorithms/shortest_paths/weighted.py` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)
- `networkx/algorithms/community/quality.py` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `networkx/algorithms/simple_paths.py` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `networkx/algorithms/flow/edmondskarp.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `networkx/utils/decorators.py` -> **Severity: 3.054** (Embedded: 0.0307 * Error Risk: 99.3488%)
- `networkx/algorithms/bipartite/generators.py` -> **Severity: 1.313** (Embedded: 0.0132 * Error Risk: 99.7842%)
- `networkx/generators/classic.py` -> **Severity: 1.089** (Embedded: 0.0118 * Error Risk: 91.9196%)
- `networkx/algorithms/shortest_paths/weighted.py` -> **Severity: 1.032** (Embedded: 0.0104 * Error Risk: 99.1433%)
- `networkx/generators/community.py` -> **Severity: 1.019** (Embedded: 0.0104 * Error Risk: 98.0126%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `networkx/algorithms/flow/utils.py` -> **Severity: 596.808** (Blast Radius: 8.289 * Doc Risk: 72.0%)
- `networkx/utils/decorators.py` -> **Severity: 592.707** (Blast Radius: 19.263 * Doc Risk: 30.7692%)
- `networkx/algorithms/centrality/flow_matrix.py` -> **Severity: 446.8** (Blast Radius: 4.468 * Doc Risk: 100.0%)
- `networkx/algorithms/centrality/betweenness.py` -> **Severity: 397.9** (Blast Radius: 3.979 * Doc Risk: 100.0%)
- `networkx/algorithms/traversal/edgedfs.py` -> **Severity: 389.4** (Blast Radius: 4.543 * Doc Risk: 85.7143%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
