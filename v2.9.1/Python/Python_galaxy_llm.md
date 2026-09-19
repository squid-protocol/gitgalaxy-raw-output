# ARCHITECTURAL_BRIEF: Python
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/TheAlgorithms/Python.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1433 analyzed artifact(s), 47344 LOC.
- **Load-bearing artifact:** `maths/greatest_common_divisor.py` -- 10 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `DIRECTORY.md` -- pulls in 1156 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `data_structures/binary_tree/red_black_tree.py` at magnitude 849.08 (structural weight, not risk).
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
| Total Artifacts | 1504 |
| Analyzed Artifacts (Scanned) | 1433 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 71 |
| Total LOC | 47344 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 95.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0943 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6364 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4891 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1363 | 46240 | 95.1% |
| PLAINTEXT | 35 | 4 | 2.4% |
| MARKDOWN | 26 | 0 | 1.8% |
| SHELL | 6 | 76 | 0.4% |
| JSON | 2 | 910 | 0.1% |
| CSV | 1 | 114 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `1.545`
> **Composition Archetype:** `Mid Flat Project` (z +1.54; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 24%, Generic / Templated Code Files 24%, Compute Cores Files 15%, Many-Argument Workhorses Files 14%, Type Conversions Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1372 | 95.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 58 | 4.0% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 71*

**Composition by Extension & Reason:**
- `.py`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 49 LOC), 1x Excluded (Machine-Generated Source Code Signature: 54 LOC)
- `.yml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 5x Unsupported Format (.undeterminable), 1x Excluded (Lexical Monotony: High structural repetition detected in 7194 LOC), 1x Excluded (Embedded Array/Matrix Payload: 5000 commas in 1001 LOC)
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.disabled`: 3x Excluded (Unsupported Extension: '.DISABLED')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 1x Excluded (Static Asset Blob without Intent: 1260 LOC)
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')
- `.py_tf`: 1x Excluded (Unsupported Extension: '.py_tf')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.8 | 22.3 | 20.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 62.4 | 78.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.4 | 2.5 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 67.7 | 24.7 | 20.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 25.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 69.7 | 99.9 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.5 | 1.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 61.3 | 1.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1384 | 556 | 3 | `data_structures/linked_list/singly_linked_list.py` |
| cleanup | 6 | 3 | 0 | `file_transfer/send_file.py` |
| guards | 1550 | 318 | 3 | `data_structures/binary_tree/binary_search_tree_recursive.py` |
| danger | 1772 | 593 | 4 | `graphs/graph_adjacency_matrix.py` |
| concurrency | 220 | 51 | 0 | `data_structures/binary_tree/binary_tree_traversals.py` |
| connectivity | 3824 | 1137 | 6 | `digital_image_processing/index_calculation.py` |
| io | 390 | 114 | 0 | `scripts/validate_solutions.py` |
| crypto | 5 | 5 | 0 | `ciphers/diffie_hellman.py` |
| ipc | 1 | 1 | 0 | `sorts/odd_even_transposition_parallel.py` |
| time | 20 | 9 | 0 | `graphs/bidirectional_a_star.py` |
| serialization | 30 | 7 | 0 | `scripts/close_pull_requests_with_awaiting_changes.sh` |
| regex | 12 | 7 | 0 | `web_programming/download_images_from_google_query.py` |
| events | 48 | 14 | 0 | `machine_learning/mfcc.py` |
| tests | 362 | 55 | 0 | `graphs/graph_adjacency_list.py` |
| docs | 3768 | 1104 | 6 | `digital_image_processing/index_calculation.py` |
| debt | 1929 | 642 | 4 | `machine_learning/linear_discriminant_analysis.py` |
| mutation | 22151 | 1054 | 37 | `graphs/directed_and_undirected_weighted_graph.py` |
| dead_code | 162 | 79 | 0 | `graphs/graph_list.py` |
| credential | 4 | 2 | 0 | `geodesy/lamberts_ellipsoidal_distance.py` |
| threat | 89 | 48 | 0 | `web_programming/instagram_crawler.py` |
| ml_ai | 366 | 146 | 1 | `strings/is_valid_email_address.py` |
| ui | 5 | 1 | 0 | `web_programming/recaptcha_verification.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/validate_solutions.py` (Hits: 13)
- `scripts/close_pull_requests_with_awaiting_changes.sh` (Hits: 12)
- `scripts/close_pull_requests_with_failing_tests.sh` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **greatest_common_divisor.py** (`maths/greatest_common_divisor.py`) — 10 inbound connections
2. **hash_table.py** (`data_structures/hashing/hash_table.py`) — 4 inbound connections
3. **kd_node.py** (`data_structures/kd_tree/kd_node.py`) — 4 inbound connections
4. **stack.py** (`data_structures/stacks/stack.py`) — 4 inbound connections
5. **prime_check.py** (`maths/prime_check.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **DIRECTORY.md** (`DIRECTORY.md`) — 1156 outbound dependencies
2. **sequential_minimum_optimization.py** (`machine_learning/sequential_minimum_optimization.py`) — 10 outbound dependencies
3. **test_digital_image_processing.py** (`digital_image_processing/test_digital_image_processing.py`) — 9 outbound dependencies
4. **automatic_differentiation.py** (`machine_learning/automatic_differentiation.py`) — 8 outbound dependencies
5. **input_data.py** (`neural_network/input_data.py`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `simulated_annealing` **(Many-Argument Workhorses)** (@ `searches/simulated_annealing.py`) -> Impact: **64.0** | LOC: 86
- `search` **(Many-Argument Workhorses)** (@ `graphs/a_star.py`) -> Impact: **58.6** | LOC: 94
  * *Intent:* # function to search the path
- `next_term` **(Many-Argument Workhorses)** (@ `project_euler/problem_551/sol1.py`) -> Impact: **55.8** | LOC: 87
  * *Intent:* """ Calculates and updates a_i in-place to either the n-th term or the smallest term for which c > 10^k when the terms are written in the form: a(i) =...
- `hill_climbing` **(Many-Argument Workhorses)** (@ `searches/hill_climbing.py`) -> Impact: **54.7** | LOC: 74
- `_get_new_alpha` **(Many-Argument Workhorses)** (@ `machine_learning/sequential_minimum_optimization.py`) -> Impact: **51.0** | LOC: 72
  * *Intent:* # Get the new alpha2 and new alpha1
- `_remove_repair` **(Compute Cores)** (@ `data_structures/binary_tree/red_black_tree.py`) -> Impact: **48.9** | LOC: 72
  * *Intent:* """Repair the coloring of the tree that may have been messed up."""
- `hsv_to_rgb` **(Many-Argument Workhorses)** (@ `conversions/rgb_hsv_conversion.py`) -> Impact: **45.4** | LOC: 67
  * *Intent:* """ Conversion from the HSV-representation to the RGB-representation. Expected RGB-values taken from https://www.rapidtables.com/convert/color/hsv-to-...
- `decrypt_caesar_with_chi_squared` **(Many-Argument Workhorses)** (@ `ciphers/decrypt_caesar_with_chi_squared.py`) -> Impact: **45.0** | LOC: 249
- `remove` **(Compute Cores)** (@ `data_structures/binary_tree/red_black_tree.py`) -> Impact: **44.3** | LOC: 54
  * *Intent:* """Remove label from this tree."""
- `suppress_non_maximum` **(Many-Argument Workhorses)** (@ `digital_image_processing/edge_detection/canny.py`) -> Impact: **42.5** | LOC: 50
  * *Intent:* """ Non-maximum suppression. If the edge strength of the current pixel is the largest compared to the other pixels in the mask with the same direction...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `graphs` | 61 | 6724.78 | 42.27% | 3.68% |
| `maths` | 130 | 4648.22 | 20.95% | 1.79% |
| `data_structures/binary_tree` | 34 | 3634.36 | 30.45% | 1.11% |
| `ciphers` | 48 | 2995.96 | 33.68% | 1.58% |
| `machine_learning` | 32 | 2739.62 | 25.53% | 1.01% |
| `dynamic_programming` | 51 | 2358.3 | 30.28% | 0.74% |
| `sorts` | 53 | 2152.66 | 28.78% | 1.89% |
| `other` | 28 | 1955.96 | 27.06% | 0.62% |
| `strings` | 57 | 1933.94 | 25.18% | 0.0% |
| `data_structures/linked_list` | 17 | 1907.38 | 38.55% | 11.69% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `graphs/check_bipatrite.py` -> **99.9972%** Exposure
- `maths/special_numbers/ugly_numbers.py` -> **99.9972%** Exposure
- `graphs/directed_and_undirected_weighted_graph.py` -> **99.9882%** Exposure
- `data_structures/linked_list/__init__.py` -> **99.8499%** Exposure
- `data_structures/linked_list/from_sequence.py` -> **98.9013%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `audio_filters/butterworth_filter.py` -> **100.0%** Exposure
- `audio_filters/iir_filter.py` -> **100.0%** Exposure
- `audio_filters/show_response.py` -> **100.0%** Exposure
- `backtracking/crossword_puzzle_solver.py` -> **100.0%** Exposure
- `backtracking/knight_tour.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `graphs/directed_and_undirected_weighted_graph.py` -> **0** Orphaned Functions | **18** Duplicates
- `data_structures/linked_list/__init__.py` -> **4** Orphaned Functions | **0** Duplicates
- `data_structures/linked_list/from_sequence.py` -> **3** Orphaned Functions | **0** Duplicates
- `maths/fibonacci.py` -> **0** Orphaned Functions | **2** Duplicates
- `web_programming/emails_from_url.py` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `9` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3205` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `data_structures/binary_tree/red_black_tree.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 849.08 | **LOC:** 717 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.8%)
- **Documentation Coverage:** 10.2564% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_remove_repair` **(Compute Cores)** (Impact: 48.9)
    * *Intent:* """Repair the coloring of the tree that may have been messed up."""
  * `remove` **(Compute Cores)** (Impact: 44.3)
    * *Intent:* """Remove label from this tree."""
  * `_insert_repair` **(Stateful Encapsulated Methods)** (Impact: 30.1)
    * *Intent:* """Repair the coloring from inserting into a tree."""
  * `insert` **(Compute Cores)** (Impact: 16.8)
    * *Intent:* """Inserts label into the subtree rooted at self, performs any rotations necessary to maintain balan...
  * `floor` **(Compute Cores)** (Impact: 16.4)
    * *Intent:* """Returns the largest element in this tree which is at most label. This method is guaranteed to run...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 138`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 188`
* *Architecture:* `api: 39`, `import: 3`
* *Defense:* `safety: 8`, `doc: 35`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, collections.abc, pprint
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `graphs/directed_and_undirected_weighted_graph.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 781.88 | **LOC:** 490 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dfs` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* # if no destination is meant the default value is -1
  * `dfs` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* # if no destination is meant the default value is -1
  * `cycle_nodes` **(Compute Cores)** (Impact: 25.2)
  * `has_cycle` **(Compute Cores)** (Impact: 25.2)
  * `cycle_nodes` **(Compute Cores)** (Impact: 25.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 142 instances
* *State Mutation (weighted view):* 456
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 71`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 172`, `dead_code: 6`, `duplicate_logic: 18`
* *Architecture:* `api: 26`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` collections, math, random, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `machine_learning/sequential_minimum_optimization.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 578.78 | **LOC:** 623 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.1%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_new_alpha` **(Many-Argument Workhorses)** (Impact: 51.0)
    * *Intent:* # Get the new alpha2 and new alpha1
  * `_choose_a2` **(Stateful Encapsulated Methods)** (Impact: 24.4)
    * *Intent:* """ Choose the second alpha using a heuristic algorithm Steps: 1: Choose alpha2 that maximizes the s...
  * `fit` **(Stateful Encapsulated Methods)** (Impact: 22.9)
    * *Intent:* # Calculate alphas using SMO algorithm
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 22.4)
  * `_choose_a1` **(Stateful Encapsulated Methods)** (Impact: 18.8)
    * *Intent:* """ Choose first alpha Steps: 1: First loop over all samples 2: Second loop over all non-bound sampl...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 92`, `args: 35`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 135`, `dead_code: 3`
* *Architecture:* `io: 7`, `api: 16`, `import: 9`
* *Defense:* `safety: 3`, `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` matplotlib, numpy, os, pandas, sequential_minimum_optimization, sklearn.datasets, sklearn.preprocessing, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `data_structures/heap/binomial_heap.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 409.56 | **LOC:** 402 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (41.4%)
- **Documentation Coverage:** 21.0526% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `merge_heaps` **(Many-Argument Workhorses)** (Impact: 40.1)
    * *Intent:* """ In-place merge of two binomial heaps. Both of them become the resulting merged heap """
  * `delete_min` **(Compute Cores)** (Impact: 27.7)
    * *Intent:* """ delete min element and return it """
  * `insert` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* """ insert a value in the heap """
  * `merge_trees` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* """ In-place merge of two binomial trees of equal size. Returns the root of the resulting tree """
  * `__traversal` **(Stateful Encapsulated Methods)** (Impact: 7.2)
    * *Intent:* """ Pre-order traversal of nodes """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 29`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 103`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 1`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` doctest, numpy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `maths/primelib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 408.16 | **LOC:** 842 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.675; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.0%), Connectivity (formerly Api Exposure) (48.9%), Complexity Load (formerly Cognitive Load) (42.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `kg_v` **(Many-Argument Workhorses)** (Impact: 38.9)
    * *Intent:* # ---------------------------------------------- """ Least common multiple input: two positive integ...
  * `goldbach` **(Defensive Guards)** (Impact: 21.6)
    * *Intent:* # ------------------------ """ Goldbach's assumption input: a even positive integer 'number' > 2 ret...
  * `get_primes_between` **(Many-Argument Workhorses)** (Impact: 18.5)
    * *Intent:* # --------------------------------------------------- """ input: prime numbers 'pNumber1' and 'pNumb...
  * `prime_factorization` **(Defensive Guards)** (Impact: 16.7)
    * *Intent:* # ----------------------------------------- """ input: positive integer 'number' returns a list of t...
  * `sieve_er` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* # ------------------------------------------ """ input: positive integer 'N' > 2 returns a list of p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 94`, `args: 17`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 61`, `dead_code: 6`
* *Architecture:* `api: 17`, `import: 3`
* *Defense:* `safety: 64`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 1):` doctest, math, maths.greatest_common_divisor
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `neural_network/convolution_neural_network.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 338.08 | **LOC:** 358 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `train` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `convolute` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* # convolution process size_conv = convs[0] num_conv = convs[1] size_data = np.shape(data)[0] # get t...
  * `pooling` **(Many-Argument Workhorses)** (Impact: 14.6)
    * *Intent:* # pooling process size_map = len(featuremaps[0]) size_pooled = int(size_map / size_pooling) featurem...
  * `_calculate_gradient_from_pool` **(Stateful Encapsulated Methods)** (Impact: 11.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 36`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 120`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 12`, `import: 3`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` matplotlib, numpy, pickle
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `graphs/graph_adjacency_matrix.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 332.82 | **LOC:** 610 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Connectivity (formerly Api Exposure) (46.6%), Complexity Load (formerly Cognitive Load) (34.0%)
- **Documentation Coverage:** 73.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_edge` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* """ Creates an edge from source vertex to destination vertex. If any given vertex doesn't exist or t...
  * `remove_edge` **(Many-Argument Workhorses)** (Impact: 15.3)
    * *Intent:* """ Removes the edge between the two vertices. If any given vertex doesn't exist or the edge does no...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 14.8)
  * `test_contains_edge` **(Compute Cores)** (Impact: 11.5)
    * *Intent:* # generate graphs and graph input vertex_count = 20 ( undirected_graph, directed_graph, random_verti...
  * `test_add_and_remove_edges_repeatedly` **(Compute Cores)** (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 74`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 46`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* `safety: 15`, `doc: 9`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, pprint, pytest, random, typing, unittest
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `data_structures/linked_list/skip_list.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 330.4 | **LOC:** 449 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.8%)
- **Documentation Coverage:** 62.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insert` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* """ :param key: Key to insert. :param value: Value associated with given key. >>> skip_list = SkipLi...
  * `_locate_node` **(Stateful Encapsulated Methods)** (Impact: 13.8)
    * *Intent:* """ :param key: Searched key, :return: Tuple with searched node (or None if given key is not present...
  * `delete` **(Compute Cores)** (Impact: 13.4)
    * *Intent:* """ :param key: Key to remove from list. >>> skip_list = SkipList() >>> skip_list.insert(2, "Two") >...
  * `__str__` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* """ :return: Visual representation of SkipList >>> skip_list = SkipList() >>> print(skip_list) SkipL...
  * `random_level` **(Generic / Templated Code)** (Impact: 4.8)
    * *Intent:* """ :return: Random level from [1, self.max_level] interval. Higher values are less likely. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 85`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 92`, `dead_code: 1`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 39`, `doc: 10`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, doctest, itertools, random, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `linear_algebra/src/lib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 324.46 | **LOC:** 445 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.249; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.0%)
- **Documentation Coverage:** 7.4074% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__mul__` **(Defensive Guards)** (Impact: 16.9)
    * *Intent:* """ implements the matrix-vector multiplication. implements the matrix-scalar multiplication """
  * `__mul__` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* """ mul implements the scalar multiplication and the dot-product """
  * `__add__` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* """ implements matrix addition. """
  * `__sub__` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* """ implements matrix subtraction. """
  * `determinant` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* """ returns the determinant of an nxn matrix using Laplace expansion """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 86`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 39`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 19`, `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.249
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001571
  * `Imports (Out-Degree: 0):` __future__, collections.abc, math, random, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `graphs/multi_heuristic_astar.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 318.74 | **LOC:** 313 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multi_a_star` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `expand_state` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `do_something` **(Many-Argument Workhorses)** (Impact: 26.0)
  * `make_common_ground` **(I/O & Config Routines)** (Impact: 11.1)
  * `put` **(Compute Cores)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 34`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 57`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 17`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` heapq, numpy, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `graphs/graph_adjacency_list.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 314.72 | **LOC:** 598 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (78.1%), Connectivity (formerly Api Exposure) (46.8%), Complexity Load (formerly Cognitive Load) (28.8%)
- **Documentation Coverage:** 73.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_edge` **(Many-Argument Workhorses)** (Impact: 15.3)
    * *Intent:* """ Creates an edge from source vertex to destination vertex. If any given vertex doesn't exist or t...
  * `remove_edge` **(Many-Argument Workhorses)** (Impact: 15.3)
    * *Intent:* """ Removes the edge between the two vertices. If any given vertex doesn't exist or the edge does no...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 14.8)
  * `remove_vertex` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* """ Removes the given vertex from the graph and deletes all incoming and outgoing edges from the giv...
  * `test_contains_edge` **(Compute Cores)** (Impact: 11.5)
    * *Intent:* # generate graphs and graph input vertex_count = 20 ( undirected_graph, directed_graph, random_verti...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 74`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 37`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* `safety: 15`, `doc: 9`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, pprint, pytest, random, typing, unittest
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `other/word_search.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 306.14 | **LOC:** 396 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (48.8%)
- **Documentation Coverage:** 18.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insert_northeast` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* """ >>> ws = WordSearch(WORDS, 3, 3) >>> ws.insert_northeast("cat", [2], [0]) >>> ws.board # doctest...
  * `insert_southeast` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* """ >>> ws = WordSearch(WORDS, 3, 3) >>> ws.insert_southeast("cat", [0], [0]) >>> ws.board # doctest...
  * `insert_southwest` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* """ >>> ws = WordSearch(WORDS, 3, 3) >>> ws.insert_southwest("cat", [0], [2]) >>> ws.board # doctest...
  * `insert_northwest` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* """ >>> ws = WordSearch(WORDS, 3, 3) >>> ws.insert_northwest("cat", [2], [2]) >>> ws.board # doctest...
  * `insert_north` **(Many-Argument Workhorses)** (Impact: 19.4)
    * *Intent:* """ >>> ws = WordSearch(WORDS, 3, 3) >>> ws.insert_north("cat", [2], [2]) >>> ws.board # doctest: +N...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 35`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` doctest, random
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cellular_automata/wa_tor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 298.9 | **LOC:** 549 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (48.9%)
- **Documentation Coverage:** 27.3865% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visualise` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* """ Visually displays the Wa-Tor planet using an ascii code in terminal to clear and re-print the Wa...
  * `move_and_reproduce` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `run` **(Many-Argument Workhorses)** (Impact: 16.3)
    * *Intent:* """ Emulate time passing by looping `iteration_count` times >>> wt = WaTor(WIDTH, HEIGHT) >>> wt.run...
  * `balance_predators_and_prey` **(Compute Cores)** (Impact: 14.3)
    * *Intent:* """ Balances predators and preys so that prey can not dominate the predators, blocking up space for ...
  * `get_surrounding_prey` **(Many-Argument Workhorses)** (Impact: 12.4)
    * *Intent:* """ Returns all the prey entities around (N, S, E, W) a predator entity. Subtly different to the `mo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 34`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `safety: 2`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` collections.abc, doctest, os, random, time, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `data_structures/binary_tree/binary_search_tree_recursive.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 298.5 | **LOC:** 642 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (44.8%), Complexity Load (formerly Cognitive Load) (43.3%), Guard Balance (formerly Safety Score) (32.8%)
- **Documentation Coverage:** 31.1321% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `remove` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* """ Removes a node in the tree >>> t = BinarySearchTree() >>> t.put(8) >>> t.put(10) >>> t.remove(8)...
  * `_reassign_nodes` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `_put` **(Stateful Encapsulated Methods)** (Impact: 11.8)
  * `_search` **(Stateful Encapsulated Methods)** (Impact: 8.5)
  * `binary_search_tree_example` **(I/O & Config Routines)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 136`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `state_mutation: 60`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 76`, `doc: 26`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, collections.abc, pytest, unittest
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `other/davis_putnam_logemann_loveland.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 295.26 | **LOC:** 368 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (47.9%)
- **Documentation Coverage:** 27.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dpll_algorithm` **(Many-Argument Workhorses)** (Impact: 29.3)
  * `find_pure_symbols` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `find_unit_clauses` **(Many-Argument Workhorses)** (Impact: 21.5)
  * `evaluate` **(Compute Cores)** (Impact: 13.2)
    * *Intent:* """ Evaluates the clause with the assignments in model. This has the following steps: 1. Return ``Tr...
  * `assign` **(Generic / Templated Code)** (Impact: 11.1)
    * *Intent:* """ Assign values to literals of the clause as given by model. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 42`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 51`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 2`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, collections.abc, doctest, random
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `matrix/matrix_class.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 288.54 | **LOC:** 367 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_column` **(Defensive Guards)** (Impact: 23.0)
  * `__init__` **(Defensive Guards)** (Impact: 20.0)
  * `add_row` **(Defensive Guards)** (Impact: 18.8)
    * *Intent:* # MATRIX MANIPULATION
  * `__mul__` **(Defensive Guards)** (Impact: 18.4)
  * `__pow__` **(Defensive Guards)** (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 69`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`
* *Architecture:* `api: 28`, `import: 2`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, doctest
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `data_structures/binary_tree/avl_tree.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 285.98 | **LOC:** 350 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.0%)
- **Documentation Coverage:** 48.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `del_node` **(Compute Cores)** (Impact: 33.4)
  * `insert_node` **(Defensive Guards)** (Impact: 18.7)
  * `__str__` **(Compute Cores)** (Impact: 13.0)
  * `get_right_most` **(Generic / Templated Code)** (Impact: 4.6)
  * `get_left_most` **(Generic / Templated Code)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 80`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 55`
* *Architecture:* `api: 30`, `import: 5`
* *Defense:* `safety: 8`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, doctest, math, random, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `graphs/basic_graphs.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 281.68 | **LOC:** 410 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (46.4%)
- **Documentation Coverage:** 62.963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `topo` **(Compute Cores)** (Impact: 21.1)
  * `dijk` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* """ dijk({1: [(2, 7), (3, 9), (6, 14)], 2: [(1, 7), (3, 10), (4, 15)], 3: [(1, 9), (2, 10), (4, 11),...
  * `prim` **(Compute Cores)** (Impact: 16.4)
  * `krusk` **(Compute Cores)** (Impact: 13.8)
    * *Intent:* """ Sort edges on the basis of distance """
  * `dfs` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* """ >>> dfs({1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, 1) 1 2 4 5 3 """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 32`, `args: 15`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 44`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` collections, io, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `neural_network/input_data.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 277.1 | **LOC:** 343 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (57.1%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 29.9)
  * `next_batch` **(Stateful Encapsulated Methods)** (Impact: 29.0)
    * *Intent:* """Return the next `batch_size` examples from this data set."""
  * `read_data_sets` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `_extract_labels` **(Stateful Encapsulated Methods)** (Impact: 7.3)
    * *Intent:* """Extract the labels into a 1D uint8 numpy array [index]. Args: f: A file object that can be passed...
  * `_maybe_download` **(Stateful Encapsulated Methods)** (Impact: 7.0)
    * *Intent:* """Download the data from source url, unless it's already here. Args: filename: string, name of the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 62`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `state_mutation: 78`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 8`, `import: 8`
* *Defense:* `safety: 2`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` gzip, numpy, os, tensorflow.python.framework, tensorflow.python.platform, tensorflow.python.util.deprecation, typing, urllib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `divide_and_conquer/convex_hull.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 271.68 | **LOC:** 508 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.7%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convex_hull_bf` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* """ Constructs the convex hull of a set of 2D points using a brute force algorithm. The algorithm ba...
  * `convex_hull_melkman` **(Compute Cores)** (Impact: 20.4)
    * *Intent:* """ Constructs the convex hull of a set of 2D points using the melkman algorithm. The algorithm work...
  * `_construct_hull` **(Many-Argument Workhorses)** (Impact: 15.5)
  * `_construct_points` **(Stateful Encapsulated Methods)** (Impact: 9.3)
  * `convex_hull_recursive` **(I/O & Config Routines)** (Impact: 9.1)
    * *Intent:* """ Constructs the convex hull of a set of 2D points using a divide-and-conquer strategy The algorit...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 52`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 52`, `dead_code: 1`
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* `safety: 6`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, collections.abc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `searches/binary_search.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 266.26 | **LOC:** 435 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (46.6%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `binary_search_with_duplicates` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* """Pure implementation of a binary search algorithm in Python that supports duplicates. Resources us...
  * `binary_search_by_recursion` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `binary_search` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* """Pure implementation of a binary search algorithm in Python Be careful collection must be ascendin...
  * `bisect_left` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `bisect_right` **(Many-Argument Workhorses)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 32`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` bisect, doctest, itertools, timeit
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `searches/tabu_search.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 252.74 | **LOC:** 293 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (45.0%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tabu_search` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `find_neighborhood` **(Many-Argument Workhorses)** (Impact: 16.8)
    * *Intent:* """ Pure implementation of generating the neighborhood (sorted by total distance of each solution fr...
  * `generate_first_solution` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* """ Pure implementation of generating the first solution for the Tabu search to start, with the redu...
  * `generate_neighbours` **(Compute Cores)** (Impact: 10.5)
    * *Intent:* """ Pure implementation of generating a dictionary of neighbors and the cost with each neighbor, giv...
  * `main` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 22`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 59`
* *Architecture:* `io: 2`, `api: 5`, `import: 2`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` argparse, copy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `hashes/hamming_code.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 252.16 | **LOC:** 293 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (40.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `receptor_converter` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* """ >>> receptor_converter(4, "1111010010111111") (['1', '0', '1', '0', '1', '0', '1', '1', '1', '1'...
  * `emitter_converter` **(Many-Argument Workhorses)** (Impact: 36.8)
    * *Intent:* # Functions of hamming code------------------------------------------- """ :param size_par: how many...
  * `text_from_bits` **(Type Conversions)** (Impact: 4.3)
    * *Intent:* """ >>> text_from_bits('011011010111001101100111') 'msg' """
  * `text_to_bits` **(Parameter Forwarders)** (Impact: 2.4)
    * *Intent:* # Functions of binary conversion-------------------------------------- """ >>> text_to_bits("msg") '...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 11`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 54`, `planned_debt: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 4`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` numpy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `computer_vision/mosaic_augmentation.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 251.2 | **LOC:** 187 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (41.0%)
- **Documentation Coverage:** 21.6085% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_image_and_anno` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `get_dataset` **(Type Conversions)** (Impact: 8.3)
    * *Intent:* """ - label_dir <type: str>: Path to label include annotation of images - img_dir <type: str>: Path ...
  * `main` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* """ Get images list and annotations list from input dir. Update new images and annotations. Save ima...
  * `random_chars` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* """ Automatic generate random 32 characters. Get random string code: '7b7ad245cdff75241935e4dd860f3b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 22`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 70`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 4`, `import: 6`
* *Defense:* `safety: 1`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` cv2, glob, numpy, os, random, string
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `project_euler/problem_054/sol1.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 239.42 | **LOC:** 385 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.3%)
- **Documentation Coverage:** 75.7576% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compare_with` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* """ Determines the outcome of comparing self hand with other hand. Returns the output as 'Win', 'Los...
  * `_is_same_kind` **(Stateful Encapsulated Methods)** (Impact: 17.5)
    * *Intent:* # Kind Values for internal use: # 7: Four of a kind # 6: Full house # 3: Three of a kind # 2: Two pa...
  * `hand_name` **(Compute Cores)** (Impact: 14.6)
    * *Intent:* # This function is not part of the problem, I did it just for fun """ Return the name of the hand in...
  * `_get_hand_type` **(Stateful Encapsulated Methods)** (Impact: 12.3)
    * *Intent:* # Number representing the type of hand internally: # 23: Royal flush # 22: Straight flush # 21: Four...
  * `_compare_cards` **(Stateful Encapsulated Methods)** (Impact: 9.0)
    * *Intent:* # Enumerate gives us the index as well as the element of a list for index, card_value in enumerate(s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 65`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 39`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 14`, `import: 2`
* *Defense:* `safety: 6`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000931
  * `Imports (Out-Degree: 0):` __future__, os
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `graphs/graph_adjacency_list.py` -> **michaelmccamy** (100.0% isolated ownership) | Magnitude: 314.72
- `divide_and_conquer/convex_hull.py` -> **pre-commit-ci[bot]** (100.0% isolated ownership) | Magnitude: 271.68
- `data_structures/arrays/sudoku_solver.py` -> **Dylanskyep** (100.0% isolated ownership) | Magnitude: 226.9
- `geometry/tests/test_graham_scan.py` -> **Ali Alimohammadi** (100.0% isolated ownership) | Magnitude: 203.42
- `maths/area.py` -> **Jaime Fernández González** (100.0% isolated ownership) | Magnitude: 160.98

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `maths/greatest_common_divisor.py` -> **Severity: 0.385** (Embedded: 0.007 * Error Risk: 54.7004%)
- `data_structures/hashing/hash_table.py` -> **Severity: 0.285** (Embedded: 0.0029 * Error Risk: 97.9442%)
- `data_structures/kd_tree/nearest_neighbour_search.py` -> **Severity: 0.214** (Embedded: 0.0022 * Error Risk: 95.8399%)
- `digital_image_processing/filters/convolve.py` -> **Severity: 0.214** (Embedded: 0.0022 * Error Risk: 95.63%)
- `maths/prime_factors.py` -> **Severity: 0.211** (Embedded: 0.0022 * Error Risk: 94.5979%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `data_structures/kd_tree/kd_node.py` -> **Severity: 253.7** (Blast Radius: 2.537 * Doc Risk: 100.0%)
- `data_structures/suffix_tree/suffix_tree_node.py` -> **Severity: 222.7** (Blast Radius: 2.227 * Doc Risk: 100.0%)
- `digital_image_processing/filters/convolve.py` -> **Severity: 178.0** (Blast Radius: 1.78 * Doc Risk: 100.0%)
- `maths/prime_check.py` -> **Severity: 159.733** (Blast Radius: 2.396 * Doc Risk: 66.6667%)
- `data_structures/hashing/number_theory/prime_numbers.py` -> **Severity: 137.9** (Blast Radius: 2.758 * Doc Risk: 50.0%)

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
