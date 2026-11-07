# ARCHITECTURAL_BRIEF: networkx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/networkx/networkx.git` |
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
- **Scope:** 708 analyzed artifact(s), 92197 LOC.
- **Load-bearing artifact:** `networkx/__init__.py` -- 597 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `networkx/algorithms/__init__.py` -- pulls in 75 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `networkx/utils/backends.py` at magnitude 2299.88 (structural weight, not risk).
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
| Total Artifacts | 970 |
| Analyzed Artifacts (Scanned) | 708 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 262 |
| Total LOC | 92197 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 73.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3552 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3005 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 34.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3155 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 659 | 90845 | 93.1% |
| YAML | 16 | 600 | 2.3% |
| PLAINTEXT | 15 | 0 | 2.1% |
| MARKDOWN | 8 | 0 | 1.1% |
| JSON | 2 | 75 | 0.3% |
| JAVASCRIPT | 2 | 120 | 0.3% |
| CSS | 2 | 33 | 0.3% |
| MAKEFILE | 1 | 96 | 0.1% |
| XML | 1 | 0 | 0.1% |
| HTML | 1 | 12 | 0.1% |
| CPP | 1 | 416 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 708 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 25%, Many-Argument Workhorses Files 24%, Data / Markup / Trivial 12%, Declarative / Non-Code 11%, Large Core Modules (3) 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 685 | 96.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 23 | 3.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 262*

**Composition by Extension & Reason:**
- `.rst`: 131x Excluded (Unsupported Extension: '.rst'), 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 12 exceeds 500 chars)
- `.png`: 10x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 3x Excluded (Machine-Generated Source Code Signature: 5 LOC), 3x Excluded (Machine-Generated Source Code Signature: 7 LOC), 2x Excluded (Machine-Generated Source Code Signature: 11 LOC)
- `.bz2`: 5x Excluded (Explicitly Denied Extension: '.bz2')
- `.gz`: 4x Excluded (Explicitly Denied Extension: '.gz')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.edgelist`: 2x Excluded (Unsupported Extension: '.edgelist')
- `.zip`: 2x Excluded (Explicitly Denied Extension: '.zip')
- `.geojson`: 2x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.a99`: 2x Excluded (Unsupported Extension: '.A99')
- `.b99`: 2x Excluded (Unsupported Extension: '.B99')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.1 | 27.0 | 29.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.8 | 58.3 | 59.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 80.9 | 16.4 | 11.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 40.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 26.0 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.9 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.7 | 62.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3333 | 418 | 12 | `networkx/algorithms/tests/test_simple_paths.py` |
| cleanup | 34 | 7 | 0 | `networkx/drawing/tests/test_pylab.py` |
| guards | 8886 | 428 | 36 | `networkx/generators/tests/test_classic.py` |
| danger | 2290 | 342 | 10 | `networkx/utils/backends.py` |
| concurrency | 431 | 95 | 1 | `networkx/readwrite/gml.py` |
| connectivity | 6757 | 557 | 25 | `networkx/algorithms/tests/test_distance_measures.py` |
| io | 90 | 32 | 0 | `.circleci/config.yml` |
| crypto | 1 | 1 | 0 | `networkx/algorithms/graph_hashing.py` |
| ipc | 1 | 1 | 0 | `examples/algorithms/plot_parallel_betweenness.py` |
| time | 21 | 4 | 0 | `networkx/algorithms/isomorphism/tests/test_temporalisomorphvf2.py` |
| serialization | 8 | 5 | 0 | `networkx/utils/tests/test_backends.py` |
| regex | 8 | 4 | 0 | `networkx/readwrite/gml.py` |
| events | 20 | 7 | 0 | `examples/external/force/force.js` |
| tests | 6570 | 258 | 31 | `networkx/algorithms/tests/test_distance_measures.py` |
| docs | 2828 | 532 | 10 | `networkx/algorithms/planarity.py` |
| debt | 400 | 119 | 1 | `networkx/algorithms/tests/test_link_prediction.py` |
| mutation | 54368 | 620 | 195 | `networkx/algorithms/isomorphism/tests/test_vf2pp_helpers.py` |
| dead_code | 3684 | 293 | 19 | `networkx/algorithms/tests/test_distance_measures.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 393 | 142 | 1 | `networkx/drawing/layout.py` |
| ui | 28 | 1 | 0 | `examples/graph/plot_morse_trie.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.circleci/config.yml` (Hits: 15)
- `doc/Makefile` (Hits: 8)
- `.github/workflows/weekly-dispatch.yml` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`networkx/__init__.py`) — 597 inbound connections
2. **planarity.py** (`networkx/algorithms/planarity.py`) — 197 inbound connections
3. **__init__.py** (`networkx/utils/__init__.py`) — 177 inbound connections
4. **decorators.py** (`networkx/utils/decorators.py`) — 149 inbound connections
5. **misc.py** (`networkx/utils/misc.py`) — 144 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`networkx/algorithms/__init__.py`) — 75 outbound dependencies
2. **__init__.py** (`networkx/generators/__init__.py`) — 29 outbound dependencies
3. **__init__.py** (`networkx/algorithms/centrality/__init__.py`) — 20 outbound dependencies
4. **backends.py** (`networkx/utils/backends.py`) — 19 outbound dependencies
5. **nx_pylab.py** (`networkx/drawing/nx_pylab.py`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `optimize_edit_paths` **(Many-Argument Workhorses)** (@ `networkx/algorithms/similarity.py`) -> Impact: **722.2** | LOC: 656
- `max_weight_matching` **(Many-Argument Workhorses)** (@ `networkx/algorithms/matching.py`) -> Impact: **395.4** | LOC: 828
  * *Intent:* """Compute a maximum-weighted matching of G. A matching is a subset of edges in which no node occurs more than once. The weight of a matching is the s...
- `display` **(Many-Argument Workhorses)** (@ `networkx/drawing/nx_pylab.py`) -> Impact: **291.6** | LOC: 832
- `_call_if_any_backends_installed` **(Many-Argument Workhorses)** (@ `networkx/utils/backends.py`) -> Impact: **266.1** | LOC: 492
  * *Intent:* # Dispatch to backends based on inputs, `backend=` arg, or configuration """Returns the result of the original function, or the backend function if th...
- `draw_networkx_edges` **(Many-Argument Workhorses)** (@ `networkx/drawing/nx_pylab.py`) -> Impact: **263.1** | LOC: 371
- `_convert_and_call_for_tests` **(Many-Argument Workhorses)** (@ `networkx/utils/backends.py`) -> Impact: **237.6** | LOC: 293
- `__new__` **(Many-Argument Workhorses)** (@ `networkx/utils/backends.py`) -> Impact: **207.8** | LOC: 265
- `preflow_push_impl` **(Many-Argument Workhorses)** (@ `networkx/algorithms/flow/preflowpush.py`) -> Impact: **205.7** | LOC: 267
  * *Intent:* """Implementation of the highest-label preflow-push algorithm."""
- `syntactic_feasibility` **(Many-Argument Workhorses)** (@ `networkx/algorithms/isomorphism/isomorphvf2.py`) -> Impact: **191.1** | LOC: 221
  * *Intent:* """Returns True if adding (G1_node, G2_node) is syntactically feasible. This function returns True if it is adding the candidate pair to the current p...
- `_convert_arguments` **(Many-Argument Workhorses)** (@ `networkx/utils/backends.py`) -> Impact: **190.4** | LOC: 210
  * *Intent:* """Convert graph arguments to the specified backend. Returns ------- args tuple and kwargs dict """

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `networkx/algorithms` | 57 | 15754.36 | 37.9% | 5.53% |
| `networkx/algorithms/tests` | 58 | 9779.44 | 18.47% | 0.0% |
| `networkx/generators` | 30 | 6699.12 | 32.65% | 2.44% |
| `networkx/readwrite` | 13 | 5270.54 | 42.63% | 1.56% |
| `networkx/drawing` | 6 | 4628.74 | 43.05% | 7.93% |
| `networkx/utils` | 10 | 4333.88 | 41.64% | 5.33% |
| `networkx/algorithms/isomorphism` | 9 | 3923.56 | 40.56% | 15.57% |
| `networkx/algorithms/isomorphism/tests` | 11 | 3559.1 | 26.05% | 0.0% |
| `networkx/generators/tests` | 29 | 3355.3 | 15.4% | 0.0% |
| `networkx/algorithms/centrality/tests` | 21 | 3315.7 | 19.08% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmarks/benchmarks/benchmark_classes.py` -> **100.0%** Exposure
- `networkx/algorithms/centrality/reaching.py` -> **99.9998%** Exposure
- `benchmarks/benchmarks/benchmark_neighbors.py` -> **99.999%** Exposure
- `networkx/algorithms/simple_paths.py` -> **99.9971%** Exposure
- `benchmarks/benchmarks/benchmark_algorithms.py` -> **99.9948%** Exposure
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
- **Unknown Dependencies:** `2192` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `networkx/utils/backends.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.893)
- **Top Global Matches:** file_cluster_8: 7.893, file_cluster_6: 11.219, file_cluster_4: 19.551
- **Magnitude:** 2299.88 | **LOC:** 2184 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 33.616; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%)
- **Documentation Coverage:** 48.4848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_call_if_any_backends_installed` **(Many-Argument Workhorses)** (Impact: 266.1)
    * *Intent:* # Dispatch to backends based on inputs, `backend=` arg, or configuration """Returns the result of th...
  * `_convert_and_call_for_tests` **(Many-Argument Workhorses)** (Impact: 237.6)
  * `__new__` **(Many-Argument Workhorses)** (Impact: 207.8)
  * `_convert_arguments` **(Many-Argument Workhorses)** (Impact: 190.4)
    * *Intent:* """Convert graph arguments to the specified backend. Returns ------- args tuple and kwargs dict """
  * `_convert_graph` **(Many-Argument Workhorses)** (Impact: 85.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 833
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 505`, `structural_boundaries: 259`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 293`, `dead_code: 2`, `planned_debt: 8`
* *Architecture:* `api: 8`, `import: 22`
* *Defense:* `safety: 96`, `doc: 22`, `test: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.616
  * `Choke Point (Betweenness):` 0.002032 | `Ripple Effect (Closeness):` 0.434705
  * `Imports (Out-Degree: 5):` .configs, .decorators, collections.abc, copy, functools, importlib.metadata, inspect, io...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `networkx/drawing/nx_pylab.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.377)
- **Top Global Matches:** file_cluster_4: 6.377, file_cluster_6: 7.909, file_cluster_12: 13.506
- **Magnitude:** 2172.74 | **LOC:** 2979 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **51** in-repo importer(s); it depends on **16**; blast radius 10.188; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%), Guard Balance (formerly Safety Score) (74.9%)
- **Documentation Coverage:** 63.0952% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `display` **(Many-Argument Workhorses)** (Impact: 291.6)
  * `draw_networkx_edges` **(Many-Argument Workhorses)** (Impact: 263.1)
  * `draw_networkx_edge_labels` **(Many-Argument Workhorses)** (Impact: 138.7)
  * `draw_networkx_nodes` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 62.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 251 instances
* *State Mutation (weighted view):* 796
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 181`, `args: 46`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 294`, `planned_debt: 1`
* *Architecture:* `api: 45`, `import: 42`
* *Defense:* `safety: 48`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.188
  * `Choke Point (Betweenness):` 0.000345 | `Ripple Effect (Closeness):` 0.307634
  * `Imports (Out-Degree: 3):` collections, collections.abc, inspect, itertools, math, matplotlib, matplotlib.cm, matplotlib.collections...
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `networkx/algorithms/similarity.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.102)
- **Top Global Matches:** file_cluster_6: 8.102, file_cluster_8: 9.672, file_cluster_4: 16.057
- **Magnitude:** 1999.62 | **LOC:** 2108 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.9%), Complexity Load (formerly Cognitive Load) (76.7%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `optimize_edit_paths` **(Many-Argument Workhorses)** (Impact: 722.2)
  * `match_edges` **(Many-Argument Workhorses)** (Impact: 118.5)
    * *Intent:* """ Parameters: u, v: matched vertices, u=None or v=None for deletion/insertion pending_g, pending_h...
  * `get_edit_ops` **(Many-Argument Workhorses)** (Impact: 103.9)
  * `get_edit_paths` **(Many-Argument Workhorses)** (Impact: 100.6)
  * `_simrank_similarity_python` **(Many-Argument Workhorses)** (Impact: 61.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 167 instances
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 99`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 182`, `planned_debt: 1`
* *Architecture:* `api: 22`, `import: 15`
* *Defense:* `safety: 2`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.295777
  * `Imports (Out-Degree: 5):` dataclasses, itertools, math, networkx, networkx.utils, numpy, scipy, time
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/drawing/layout.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.675)
- **Top Global Matches:** file_cluster_4: 6.675, file_cluster_9: 10.621, file_cluster_6: 10.856
- **Magnitude:** 1481.22 | **LOC:** 2041 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 6.079; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.2%)
- **Documentation Coverage:** 65.8537% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spring_layout` **(Many-Argument Workhorses)** (Impact: 138.0)
  * `forceatlas2_layout` **(Many-Argument Workhorses)** (Impact: 133.8)
  * `arf_layout` **(Many-Argument Workhorses)** (Impact: 50.9)
  * `kamada_kawai_layout` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `_sparse_fruchterman_reingold` **(Many-Argument Workhorses)** (Impact: 37.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 217 instances
* *State Mutation (weighted view):* 716
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 143`, `args: 25`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 282`, `planned_debt: 1`
* *Architecture:* `api: 17`, `import: 29`
* *Defense:* `safety: 19`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.079
  * `Choke Point (Betweenness):` 0.000187 | `Ripple Effect (Closeness):` 0.299302
  * `Imports (Out-Degree: 5):` networkx, networkx.utils, numpy, scipy, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `networkx/readwrite/gexf.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.624)
- **Top Global Matches:** file_cluster_4: 8.624, file_cluster_12: 9.549, file_cluster_7: 11.364
- **Magnitude:** 1428.82 | **LOC:** 1085 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 1.47; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.2%)
- **Documentation Coverage:** 87.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_attributes` **(Many-Argument Workhorses)** (Impact: 64.5)
    * *Intent:* # Add attrvalues to node or edge attvalues = Element("attvalues") if len(data) == 0: return data mod...
  * `make_graph` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* # start with empty DiGraph or MultiDiGraph edgedefault = graph_xml.get("defaultedgetype", None) if e...
  * `add_edge` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* # add an edge to the graph # raise error if we find mixed directed and undirected edges edge_directi...
  * `add_edges` **(Type Conversions)** (Impact: 27.4)
  * `indent` **(Compute Cores)** (Impact: 26.8)
    * *Intent:* # in-place prettyprint formatter i = "\n" + " " * level if len(elem): if not elem.text or not elem.t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 277 instances
* *State Mutation (weighted view):* 901
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 97`, `args: 33`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 347`, `fragile_debt: 2`
* *Architecture:* `api: 35`, `import: 6`
* *Defense:* `safety: 29`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.47
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.290795
  * `Imports (Out-Degree: 4):` itertools, networkx, networkx.utils, numpy, time, xml.etree.ElementTree
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/matching.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.042)
- **Top Global Matches:** file_cluster_8: 7.042, file_cluster_6: 12.573, file_cluster_4: 21.164
- **Magnitude:** 1340.7 | **LOC:** 1149 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.583; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.9%)
- **Documentation Coverage:** 64.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `max_weight_matching` **(Many-Argument Workhorses)** (Impact: 395.4)
    * *Intent:* """Compute a maximum-weighted matching of G. A matching is a subset of edges in which no node occurs...
  * `addBlossom` **(Many-Argument Workhorses)** (Impact: 60.6)
    * *Intent:* # Construct a new blossom with given base, through S-vertices v and w. # Label the new blossom as S;...
  * `expandBlossom` **(Many-Argument Workhorses)** (Impact: 52.4)
    * *Intent:* # Expand the given top-level blossom. # This is an obnoxiously complicated recursive function for th...
  * `_recurse` **(Many-Argument Workhorses)** (Impact: 46.2)
    * *Intent:* # This is an obnoxiously complicated recursive function for the sake of # a stack-transformation. So...
  * `is_maximal_matching` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* """Return True if ``matching`` is a maximal matching of ``G`` A *maximal matching* in a graph is a m...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 100`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 196`, `fragile_debt: 2`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 43`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.296252
  * `Imports (Out-Degree: 3):` itertools, networkx, networkx.utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/planarity.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.063)
- **Top Global Matches:** file_cluster_4: 7.063, file_cluster_12: 7.394, file_cluster_15: 8.898
- **Magnitude:** 1235.56 | **LOC:** 1489 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **197** in-repo importer(s); it depends on **3**; blast radius 80.491; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (63.3%)
- **Documentation Coverage:** 11.236% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_constraints` **(Many-Argument Workhorses)** (Impact: 38.1)
  * `add_half_edge` **(Many-Argument Workhorses)** (Impact: 35.5)
    * *Intent:* """Adds a half-edge from `start_node` to `end_node`. If the half-edge is not the first one out of `s...
  * `remove_back_edges` **(Compute Cores)** (Impact: 33.1)
  * `dfs_orientation` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* """Orient the graph by DFS, compute lowpoints and nesting order."""
  * `dfs_testing` **(Compute Cores)** (Impact: 23.2)
    * *Intent:* """Test for LR partition."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 672
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 120`, `args: 61`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 250`
* *Architecture:* `api: 47`, `import: 3`
* *Defense:* `safety: 6`, `doc: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 80.491
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.44414
  * `Imports (Out-Degree: 1):` collections, copy, networkx
  * `Imported By (In-Degree: 197):` (Excluded from Brief to save tokens)

### `networkx/drawing/tests/test_pylab.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.393)
- **Top Global Matches:** file_cluster_12: 6.393, file_cluster_15: 7.786, file_cluster_11: 8.281
- **Magnitude:** 1144.74 | **LOC:** 1583 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.279; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.6%), Complexity Load (formerly Cognitive Load) (24.5%), Connectivity (formerly Api Exposure) (12.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.6%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_display_edge_style` **(Defensive Guards)** (Impact: 21.2)
  * `test_display_edge_position` **(Defensive Guards)** (Impact: 17.0)
  * `test_display_edge_single_color` **(Defensive Guards)** (Impact: 16.9)
  * `test_individualized_font_attributes` **(Defensive Guards)** (Impact: 16.6)
  * `test_display_edge_width` **(Defensive Guards)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 626
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 221`, `args: 81`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 268`, `unreferenced_by_name: 79`
* *Architecture:* `api: 81`, `import: 12`
* *Defense:* `safety: 160`, `doc: 28`, `test: 137`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` itertools, matplotlib.collections, matplotlib.patches, networkx, os, pytest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/cycles.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.706)
- **Top Global Matches:** file_cluster_8: 7.706, file_cluster_6: 10.834, file_cluster_4: 19.244
- **Magnitude:** 1138.62 | **LOC:** 1235 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.494; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (57.6%)
- **Documentation Coverage:** 44.7368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chordless_cycles` **(Many-Argument Workhorses)** (Impact: 105.9)
    * *Intent:* """Find simple chordless cycles of a graph. A `simple cycle` is a closed path where no node appears ...
  * `simple_cycles` **(Many-Argument Workhorses)** (Impact: 60.3)
    * *Intent:* """Find simple cycles (elementary circuits) of a graph. A "simple cycle", or "elementary circuit", i...
  * `find_cycle` **(Many-Argument Workhorses)** (Impact: 53.9)
    * *Intent:* """Returns a cycle found via depth-first traversal. The cycle is a list of edges indicating the cycl...
  * `_chordless_cycle_search` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* """The main loop for chordless cycle enumeration. This algorithm is strongly inspired by that of Dia...
  * `_min_cycle` **(Many-Argument Workhorses)** (Impact: 34.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.494
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.29546
  * `Imports (Out-Degree: 5):` collections, itertools, math, networkx, networkx.utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/ismags.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.105)
- **Top Global Matches:** file_cluster_6: 7.105, file_cluster_4: 9.963, file_cluster_12: 16.65
- **Magnitude:** 1110.56 | **LOC:** 1314 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 0.656; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 40.7407% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_map_nodes` **(Many-Argument Workhorses)** (Impact: 102.7)
    * *Intent:* """ Find all subgraph isomorphisms honoring constraints. The collection `candidate_sets` is stored a...
  * `_process_ordered_pair_partitions` **(Many-Argument Workhorses)** (Impact: 71.1)
  * `create_aligned_partitions` **(Many-Argument Workhorses)** (Impact: 62.8)
    * *Intent:* """Partitions of "things" (nodes or edges) from subgraph and graph based on function `thing_matcher`...
  * `_refine_opp` **(Many-Argument Workhorses)** (Impact: 53.9)
  * `make_partition` **(Many-Argument Workhorses)** (Impact: 41.3)
    * *Intent:* """ Partitions items into sets based on the outcome of ``test(item1, item2)``. Pairs of items for wh...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 110`, `args: 36`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 184`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 6`, `doc: 23`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.222966
  * `Imports (Out-Degree: 2):` collections, functools, itertools, networkx
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `networkx/generators/random_graphs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.677)
- **Top Global Matches:** file_cluster_6: 7.677, file_cluster_4: 8.883, file_cluster_9: 14.725
- **Magnitude:** 1110.56 | **LOC:** 1496 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 0.936; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.5%)
- **Documentation Coverage:** 32.5581% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extended_barabasi_albert_graph` **(Many-Argument Workhorses)** (Impact: 87.5)
    * *Intent:* """Returns an extended Barabási–Albert model graph. An extended Barabási–Albert model graph is a ran...
  * `dual_barabasi_albert_graph` **(Many-Argument Workhorses)** (Impact: 64.4)
  * `random_regular_graph` **(Many-Argument Workhorses)** (Impact: 50.5)
  * `fast_gnp_random_graph` **(Many-Argument Workhorses)** (Impact: 38.1)
    * *Intent:* """Returns a $G_{n,p}$ random graph, also known as an Erdős-Rényi graph or a binomial graph. Paramet...
  * `powerlaw_cluster_graph` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* """Holme and Kim algorithm for growing graphs with powerlaw degree distribution and approximate aver...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 83`, `args: 24`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 178`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.936
  * `Choke Point (Betweenness):` 0.000132 | `Ripple Effect (Closeness):` 0.292643
  * `Imports (Out-Degree: 8):` ..utils.misc, .classic, .degree_seq, collections, itertools, math, networkx, networkx.utils...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/tests/test_vf2pp_helpers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.497)
- **Top Global Matches:** file_cluster_15: 7.497, file_cluster_16: 8.364, file_cluster_2: 8.392
- **Magnitude:** 1076.08 | **LOC:** 1315 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.279; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.3%), Complexity Load (formerly Cognitive Load) (29.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.2%), Connectivity (formerly Api Exposure) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_covered_neighbors_no_labels` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `test_feasible_look_ahead_same_labels` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `test_covered_neighbors_with_labels` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `test_no_covered_neighbors_no_labels` **(Many-Argument Workhorses)** (Impact: 22.7)
  * `test_same_in_out_degrees_no_candidate` **(Type Conversions)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 123`, `args: 23`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `state_mutation: 442`, `unreferenced_by_name: 22`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 88`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` itertools, networkx, networkx.algorithms.isomorphism.vf2pp, operator, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/algorithms/shortest_paths/weighted.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.958)
- **Top Global Matches:** file_cluster_4: 6.958, file_cluster_6: 8.43, file_cluster_12: 12.974
- **Magnitude:** 1050.02 | **LOC:** 2543 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 0.822; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (51.7%)
- **Documentation Coverage:** 23.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_dijkstra_multisource` **(Many-Argument Workhorses)** (Impact: 79.7)
  * `_inner_bellman_ford` **(Many-Argument Workhorses)** (Impact: 67.0)
  * `bidirectional_dijkstra` **(Many-Argument Workhorses)** (Impact: 63.4)
  * `goldberg_radzik` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* """Compute shortest path lengths and predecessors on shortest paths in weighted graphs. The algorith...
  * `_bellman_ford` **(Many-Argument Workhorses)** (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 142 instances
* *State Mutation (weighted view):* 433
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 110`, `args: 37`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 149`, `planned_debt: 1`
* *Architecture:* `api: 31`, `import: 5`
* *Defense:* `safety: 13`, `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.00014 | `Ripple Effect (Closeness):` 0.223961
  * `Imports (Out-Degree: 4):` collections, heapq, itertools, networkx, networkx.algorithms.shortest_paths.generic
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `networkx/algorithms/approximation/traveling_salesman.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.868)
- **Top Global Matches:** file_cluster_8: 7.868, file_cluster_6: 11.945, file_cluster_4: 20.36
- **Magnitude:** 1034.78 | **LOC:** 1509 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.409; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.3%)
- **Documentation Coverage:** 21.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `held_karp_ascent` **(Many-Argument Workhorses)** (Impact: 98.7)
    * *Intent:* """ Minimizes the Held-Karp relaxation of the TSP for `G` Solves the Held-Karp relaxation of the inp...
  * `simulated_annealing_tsp` **(Many-Argument Workhorses)** (Impact: 87.6)
  * `threshold_accepting_tsp` **(Many-Argument Workhorses)** (Impact: 84.4)
  * `asadpour_atsp` **(Many-Argument Workhorses)** (Impact: 63.7)
    * *Intent:* """ Returns an approximate solution to the traveling salesman problem. This approximate solution is ...
  * `traveling_salesman_problem` **(Many-Argument Workhorses)** (Impact: 47.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 76`, `args: 20`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 174`, `planned_debt: 1`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `safety: 3`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.01207
  * `Imports (Out-Degree: 6):` math, networkx, networkx.algorithms.tree.mst, networkx.utils, numpy, scipy
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/threshold.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.364)
- **Top Global Matches:** file_cluster_4: 7.364, file_cluster_12: 10.8, file_cluster_9: 11.152
- **Magnitude:** 1002.04 | **LOC:** 982 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.359; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.1%)
- **Documentation Coverage:** 3.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `creation_sequence` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* """ Determines the creation sequence for the given threshold degree sequence. The creation sequence ...
  * `weights_to_creation_sequence` **(Many-Argument Workhorses)** (Impact: 34.3)
    * *Intent:* # return wseq
  * `shortest_path` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* """ Find the shortest path between u and v in a threshold graph G with the given creation_sequence. ...
  * `shortest_path_length` **(Defensive Guards)** (Impact: 28.2)
    * *Intent:* """ Return the shortest path length from indicated node to every other node for the threshold graph ...
  * `creation_sequence_to_weights` **(Defensive Guards)** (Impact: 24.8)
    * *Intent:* """ Returns a list of node weights which create the threshold graph designated by the creation seque...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 87`, `args: 26`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 214`, `dead_code: 1`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 22`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001414
  * `Imports (Out-Degree: 4):` math, networkx, networkx.utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `networkx/readwrite/gml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.326)
- **Top Global Matches:** file_cluster_8: 7.326, file_cluster_6: 13.778, file_cluster_4: 22.214
- **Magnitude:** 984.6 | **LOC:** 883 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 1.53; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.6%), Complexity Load (formerly Cognitive Load) (62.2%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_gml_lines` **(Many-Argument Workhorses)** (Impact: 175.4)
    * *Intent:* """Parse GML `lines` into a graph."""
  * `stringize` **(Many-Argument Workhorses)** (Impact: 86.5)
  * `generate_gml` **(Many-Argument Workhorses)** (Impact: 83.9)
  * `literal_stringizer` **(Defensive Guards)** (Impact: 46.0)
    * *Intent:* """Convert a `value` to a Python literal in GML representation. Parameters ---------- value : object...
  * `stringize` **(Defensive Guards)** (Impact: 44.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 87`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 121`
* *Architecture:* `api: 27`, `import: 9`
* *Defense:* `safety: 45`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.53
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.291101
  * `Imports (Out-Degree: 4):` ast, collections, enum, html.entities, io, networkx, networkx.utils, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/isomorphvf2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.427)
- **Top Global Matches:** file_cluster_6: 8.427, file_cluster_4: 13.444, file_cluster_8: 14.81
- **Magnitude:** 932.14 | **LOC:** 1263 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 0.83; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.3%)
- **Documentation Coverage:** 4.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `syntactic_feasibility` **(Many-Argument Workhorses)** (Impact: 191.1)
    * *Intent:* """Returns True if adding (G1_node, G2_node) is syntactically feasible. This function returns True i...
  * `syntactic_feasibility` **(Many-Argument Workhorses)** (Impact: 78.1)
    * *Intent:* """Returns True if adding (G1_node, G2_node) is syntactically feasible. This function returns True i...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 69.9)
    * *Intent:* """Initializes DiGMState object. Pass in the DiGraphMatcher to which this DiGMState belongs and the ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 41.1)
    * *Intent:* """Initializes GMState object. Pass in the GraphMatcher to which this GMState belongs and the new no...
  * `candidate_pairs_iter` **(Compute Cores)** (Impact: 29.1)
    * *Intent:* """Iterator over candidate pairs of nodes in G1 and G2."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 96`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 130`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 26`, `import: 2`
* *Defense:* `safety: 6`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.000484 | `Ripple Effect (Closeness):` 0.178287
  * `Imports (Out-Degree: 2):` networkx, sys
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tests/test_cycles.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.556)
- **Top Global Matches:** file_cluster_12: 6.556, file_cluster_15: 7.645, file_cluster_16: 9.628
- **Magnitude:** 929.44 | **LOC:** 983 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.279; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (44.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.8%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 98.6486% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_cycle` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `check_cycle_algorithm` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `test_chordless_cycles_giant_hamiltonian` **(Compute Cores)** (Impact: 20.7)
    * *Intent:* # ... o - e - o - e - o ... # o = odd, e = even # ... ---/ \-----/ \--- ... # <-- "long" edges # # e...
  * `test_simple_cycles_notable_clique_sequences` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* # A000292: Number of labeled graphs on n+3 nodes that are triangles. g_family = [self.K(n) for n in ...
  * `test_chordless_cycles_directed` **(Compute Cores)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 183`, `args: 75`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 229`, `unreferenced_by_name: 55`
* *Architecture:* `api: 78`, `import: 6`
* *Defense:* `safety: 68`, `doc: 1`, `test: 71`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` itertools, math, networkx, networkx.algorithms.traversal.edgedfs, pytest, random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `networkx/readwrite/graphml.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.68)
- **Top Global Matches:** file_cluster_4: 6.68, file_cluster_12: 8.643, file_cluster_15: 10.331
- **Magnitude:** 888.72 | **LOC:** 1054 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 1.53; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.3%)
- **Documentation Coverage:** 57.377% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_graph_element` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* """ Serialize graph G in GraphML to the stream. """
  * `decode_data_elements` **(Many-Argument Workhorses)** (Impact: 36.9)
    * *Intent:* """Use the key information to decode the data XML if present."""
  * `make_graph` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* # set default graph type edgedefault = graph_xml.get("edgedefault", None) if G is None: if edgedefau...
  * `indent` **(Compute Cores)** (Impact: 26.8)
    * *Intent:* # in-place prettyprint formatter i = "\n" + level * " " if len(elem): if not elem.text or not elem.t...
  * `attr_type` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* """Infer the attribute type of data named name. Currently this only supports inference of numeric ty...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 453
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 107`, `args: 33`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 181`, `fragile_debt: 1`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `safety: 11`, `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.53
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.291101
  * `Imports (Out-Degree: 5):` collections, lxml.etree, networkx, networkx.utils, numpy, warnings, xml.etree.ElementTree
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/algorithms/isomorphism/vf2pp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.506)
- **Top Global Matches:** file_cluster_8: 6.506, file_cluster_3: 17.992, file_cluster_6: 18.41
- **Magnitude:** 866.84 | **LOC:** 1066 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 0.699; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%), Complexity Load (formerly Cognitive Load) (58.8%)
- **Documentation Coverage:** 20.6897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_restore_Tinout_Di` **(Many-Argument Workhorses)** (Impact: 91.3)
    * *Intent:* # If the node to remove from the mapping has >=1 covered neighbor, add it to T1. _, _, directed, FG,...
  * `_feasible_look_ahead` **(Many-Argument Workhorses)** (Impact: 81.3)
  * `_feasible_node_pair` **(Many-Argument Workhorses)** (Impact: 80.7)
  * `_all_morphisms` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `_find_candidates_Di` **(Many-Argument Workhorses)** (Impact: 48.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 84`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 115`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 16`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.699
  * `Choke Point (Betweenness):` 0.000101 | `Ripple Effect (Closeness):` 0.29673
  * `Imports (Out-Degree: 3):` collections, networkx, operator
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tree/branchings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.463)
- **Top Global Matches:** file_cluster_4: 7.463, file_cluster_12: 8.757, file_cluster_9: 10.329
- **Magnitude:** 806.56 | **LOC:** 1035 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 0.594; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (45.5%)
- **Documentation Coverage:** 36.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maximum_branching` **(Many-Argument Workhorses)** (Impact: 153.5)
  * `edmonds_step_I2` **(Many-Argument Workhorses)** (Impact: 34.3)
    * *Intent:* """ Perform step I2 from Edmonds' paper First, check if the last step I1 created a cycle. If it did ...
  * `greedy_branching` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* """ Returns a branching obtained through a greedy algorithm. This algorithm is wrong, and cannot giv...
  * `_write_partition` **(Stateful Encapsulated Methods)** (Impact: 22.5)
    * *Intent:* """ Writes the desired partition into the graph to calculate the minimum spanning tree. Also, if one...
  * `maximum_spanning_arborescence` **(Many-Argument Workhorses)** (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 372
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 66`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 140`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 19`, `import: 7`
* *Defense:* `safety: 8`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.594
  * `Choke Point (Betweenness):` 5e-05 | `Ripple Effect (Closeness):` 0.296094
  * `Imports (Out-Degree: 7):` .recognition, dataclasses, networkx, networkx.utils, operator, queue, string
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `networkx/algorithms/tree/mst.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.145)
- **Top Global Matches:** file_cluster_6: 5.145, file_cluster_4: 12.049, file_cluster_8: 12.519
- **Magnitude:** 763.48 | **LOC:** 1323 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 0.64; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.0%)
- **Documentation Coverage:** 30.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prim_mst_edges` **(Many-Argument Workhorses)** (Impact: 103.0)
    * *Intent:* """Iterate over edges of Prim's algorithm min/max spanning tree. Parameters ---------- G : NetworkX ...
  * `kruskal_mst_edges` **(Many-Argument Workhorses)** (Impact: 82.1)
  * `random_spanning_tree` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* """ Sample a random spanning tree using the edges weights of `G`. This function supports two differe...
  * `boruvka_mst_edges` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `number_of_spanning_trees` **(Many-Argument Workhorses)** (Impact: 24.6)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.64
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.297049
  * `Imports (Out-Degree: 6):` dataclasses, enum, heapq, itertools, math, networkx, networkx.utils, numpy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `networkx/algorithms/simple_paths.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.501)
- **Top Global Matches:** file_cluster_4: 7.501, file_cluster_12: 9.35, file_cluster_15: 11.212
- **Magnitude:** 699.18 | **LOC:** 967 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.553; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_bidirectional_dijkstra` **(Many-Argument Workhorses)** (Impact: 113.4)
  * `_bidirectional_pred_succ` **(Many-Argument Workhorses)** (Impact: 88.4)
    * *Intent:* """Bidirectional shortest path helper. Returns (pred,succ,w) where pred is a dictionary of predecess...
  * `shortest_simple_paths` **(Many-Argument Workhorses)** (Impact: 38.7)
    * *Intent:* """Generate all simple paths in the graph G from source to target, starting from shortest ones. A si...
  * `_all_simple_edge_paths` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* # We simulate recursion with a stack, keeping the current path being explored # and the outgoing edg...
  * `all_simple_edge_paths` **(Many-Argument Workhorses)** (Impact: 23.7)
    * *Intent:* """Generate lists of edges for all simple paths in G from source to target. A simple path is a path ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 70`, `args: 31`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 92`, `duplicate_logic: 16`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 4`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.553
  * `Choke Point (Betweenness):` 0.000628 | `Ripple Effect (Closeness):` 0.295777
  * `Imports (Out-Degree: 7):` heapq, itertools, networkx, networkx.algorithms.shortest_paths.weighted, networkx.utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/readwrite/text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.447)
- **Top Global Matches:** file_cluster_8: 12.447, file_cluster_3: 14.432, file_cluster_6: 24.252
- **Magnitude:** 689.1 | **LOC:** 852 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 1.518; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.3%)
- **Documentation Coverage:** 70.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_network_text` **(Many-Argument Workhorses)** (Impact: 173.4)
  * `_parse_network_text` **(Many-Argument Workhorses)** (Impact: 65.4)
    * *Intent:* """Reconstructs a graph from a network text representation. This is mainly used for testing. Network...
  * `write_network_text` **(Many-Argument Workhorses)** (Impact: 26.0)
  * `_find_sources` **(Stateful Encapsulated Methods)** (Impact: 13.1)
    * *Intent:* """ Determine a minimal set of nodes such that the entire graph is reachable """
  * `as_dict` **(Compute Cores)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 38`, `args: 9`, `func_start: 5`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 134`
* *Architecture:* `io: 1`, `api: 14`, `import: 7`
* *Defense:* `safety: 5`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.518
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.291101
  * `Imports (Out-Degree: 4):` collections, itertools, networkx, networkx.utils, sys, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `networkx/convert_matrix.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.246)
- **Top Global Matches:** file_cluster_6: 9.246, file_cluster_8: 10.36, file_cluster_4: 16.811
- **Magnitude:** 681.06 | **LOC:** 1320 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 17.041; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_numpy_array` **(Many-Argument Workhorses)** (Impact: 90.5)
  * `to_numpy_array` **(Many-Argument Workhorses)** (Impact: 79.7)
  * `from_pandas_edgelist` **(Many-Argument Workhorses)** (Impact: 67.0)
  * `to_scipy_sparse_array` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* """Returns the graph adjacency matrix as a SciPy sparse array. Parameters ---------- G : graph The N...
  * `to_pandas_edgelist` **(Many-Argument Workhorses)** (Impact: 44.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 62`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 97`, `dead_code: 4`
* *Architecture:* `api: 9`, `import: 9`
* *Defense:* `safety: 9`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.041
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.433002
  * `Imports (Out-Degree: 2):` collections, itertools, networkx, numpy, pandas, scipy
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `networkx/algorithms/tests/test_smetric.py` (PYTHON) | Magnitude: 3.2 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, test: 2, import: 2, indent_spaces: 2
- `networkx/algorithms/connectivity/tests/test_kcomponents.py` (PYTHON) | Magnitude: 167.52 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 239, core_var_decl: 60, state_mutation: 57, structural_boundaries: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `networkx/algorithms/community/quality.py` (PYTHON) | Magnitude: 268.84 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 87, core_var_decl: 42, state_mutation: 39, branch: 38
- `networkx/algorithms/operators/tests/test_all.py` (PYTHON) | Magnitude: 154.62 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 249, core_var_decl: 108, state_mutation: 94, design_short_vars: 84
- `networkx/algorithms/tests/test_core.py` (PYTHON) | Magnitude: 199.08 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 200, structural_boundaries: 87, core_var_decl: 74, state_mutation: 61
- `networkx/algorithms/traversal/tests/test_dfs.py` (PYTHON) | Magnitude: 146.78 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 271, structural_boundaries: 74, core_var_decl: 50, safety: 48
- `networkx/algorithms/tests/test_clique.py` (PYTHON) | Magnitude: 134.36 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 253, structural_boundaries: 69, core_var_decl: 54, state_mutation: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `networkx/algorithms/bipartite/tests/test_cluster.py` (PYTHON) | Magnitude: 39.22 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 37, core_var_decl: 24, safety: 19
- `networkx/algorithms/tree/recognition.py` (PYTHON) | Magnitude: 52.96 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, branch: 14, structural_boundaries: 10, decorators: 6
- `networkx/algorithms/centrality/current_flow_closeness.py` (PYTHON) | Magnitude: 39.76 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, core_var_decl: 13, state_mutation: 12, structural_boundaries: 8
- `networkx/generators/tests/test_expanders.py` (PYTHON) | Magnitude: 105.34 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 55, test: 55, core_var_decl: 35
- `networkx/algorithms/approximation/dominating_set.py` (PYTHON) | Magnitude: 38.22 | Delta: **0.149** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 15, core_var_decl: 8, design_snake_case: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `networkx/algorithms/tree/tests/test_recognition.py` (PYTHON) | Magnitude: 101.46 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 63, safety: 32, state_mutation: 28
- `networkx/algorithms/tests/test_isolate.py` (PYTHON) | Magnitude: 10.16 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 10, safety: 5, args: 3
- `networkx/algorithms/operators/unary.py` (PYTHON) | Magnitude: 22.82 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, branch: 6, structural_boundaries: 6, api: 3
- `networkx/algorithms/approximation/tests/test_matching.py` (PYTHON) | Magnitude: 3.3 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 6, import: 2, indent_spaces: 2, args: 1
- `networkx/linalg/tests/test_modularity.py` (PYTHON) | Magnitude: 34.04 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 62, state_mutation: 13, core_var_decl: 13, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `networkx/algorithms/tree/distance_measures.py` (PYTHON) | Magnitude: 106.64 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 48, branch: 23, state_mutation: 17, core_var_decl: 15
- `examples/3d_drawing/plot_basic.py` (PYTHON) | Magnitude: 21.86 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, core_var_decl: 8, indent_spaces: 7, design_snake_case: 7
- `networkx/algorithms/reciprocity.py` (PYTHON) | Magnitude: 57.24 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 13, core_var_decl: 11, design_snake_case: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/milestone-merged-prs.yaml` (YAML) | Magnitude: 15.32 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 2, args: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `networkx/algorithms/bipartite/tests/test_spectral_bipartivity.py` (PYTHON) | Magnitude: 26.64 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 24, test: 19, safety: 14
- `networkx/algorithms/tests/test_asteroidal.py` (PYTHON) | Magnitude: 10.3 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, state_mutation: 7, core_var_decl: 7
- `networkx/algorithms/centrality/tests/test_voterank.py` (PYTHON) | Magnitude: 30.96 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 15, state_mutation: 12, core_var_decl: 12
- `networkx/algorithms/tests/test_hybrid.py` (PYTHON) | Magnitude: 8.36 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, safety: 5, core_var_decl: 4
- `networkx/readwrite/tests/test_leda.py` (PYTHON) | Magnitude: 14.52 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 10, state_mutation: 7, core_var_decl: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/test.yml` -> Churn: **100.0%** | Cog Load: 11.419% | Debt: 94.3702%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `networkx/utils/backends.py` -> **Rick Ratzel** (100.0% isolated ownership) | Magnitude: 2299.88
- `networkx/drawing/nx_pylab.py` -> **NaorTIRAM** (100.0% isolated ownership) | Magnitude: 2172.74
- `networkx/drawing/layout.py` -> **Fabio Zanini** (100.0% isolated ownership) | Magnitude: 1481.22
- `networkx/readwrite/gexf.py` -> **Ross Barnowski** (100.0% isolated ownership) | Magnitude: 1428.82
- `networkx/algorithms/planarity.py` -> **Varand Arakelian** (100.0% isolated ownership) | Magnitude: 1235.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `networkx/__init__.py` -> **Severity: 14.156** (Bridge: 0.2831 * Flux: 50.0%)
- `networkx/utils/backends.py` -> **Severity: 0.203** (Bridge: 0.002 * Flux: 100.0%)
- `networkx/generators/intersection.py` -> **Severity: 0.1** (Bridge: 0.001 * Flux: 99.9986%)
- `networkx/utils/misc.py` -> **Severity: 0.072** (Bridge: 0.0007 * Flux: 100.0%)
- `networkx/algorithms/isomorphism/temporalisomorphvf2.py` -> **Severity: 0.071** (Bridge: 0.0007 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `networkx/__init__.py` -> **Severity: 67.585** (Embedded: 0.8448 * Error Risk: 80.0%)
- `networkx/algorithms/__init__.py` -> **Severity: 41.662** (Embedded: 0.4431 * Error Risk: 94.0294%)
- `networkx/utils/__init__.py` -> **Severity: 40.927** (Embedded: 0.5116 * Error Risk: 80.0%)
- `networkx/generators/__init__.py` -> **Severity: 40.143** (Embedded: 0.435 * Error Risk: 92.2728%)
- `networkx/algorithms/planarity.py` -> **Severity: 39.109** (Embedded: 0.4441 * Error Risk: 88.0553%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `networkx/__init__.py` -> **Severity: 23327.8** (Blast Radius: 233.278 * Doc Risk: 100.0%)
- `networkx/exception.py` -> **Severity: 1704.3** (Blast Radius: 17.043 * Doc Risk: 100.0%)
- `networkx/utils/backends.py` -> **Severity: 1629.865** (Blast Radius: 33.616 * Doc Risk: 48.4848%)
- `networkx/utils/misc.py` -> **Severity: 1266.029** (Blast Radius: 25.729 * Doc Risk: 49.2063%)
- `networkx/utils/decorators.py` -> **Severity: 1254.306** (Blast Radius: 40.765 * Doc Risk: 30.7692%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 1052 literal sites + 7 sites through wrappers = 1059

- `pop_attr` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `networkx/readwrite/gml.py`
- `_stub_func` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `networkx/utils/tests/test_backends.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 31230 call pairs -- scoped 15.3%, unique 0.0%, ambiguous 13.2%, external 71.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 31226 | 15.3% | 0.0% | 13.2% | 71.5% |
| javascript | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
