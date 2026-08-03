# ARCHITECTURAL_BRIEF: Python
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/Python` |
| **Timestamp** | `2026-08-03T19:34:06.871113+00:00` |
| **Scan Duration** | `2.84s` |
| **Git Branch** | `master` |
| **Git Commit** | `840ca00ad389a947205a4a928171499f2228cbb7` |
| **Git Remote** | `https://github.com/TheAlgorithms/Python.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1366 malicious artifacts.

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
| Total Artifacts | 1504 |
| Analyzed Artifacts (Scanned) | 1428 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 76 |
| Total LOC | 47029 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 94.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9269 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1385 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7778 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1360 | 45925 | 95.2% |
| PLAINTEXT | 33 | 4 | 2.3% |
| MARKDOWN | 26 | 0 | 1.8% |
| SHELL | 6 | 76 | 0.4% |
| JSON | 2 | 910 | 0.1% |
| CSV | 1 | 114 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.015`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 737 | 51.6% |
| file_cluster_16 | 369 | 25.8% |
| file_cluster_13 | 234 | 16.4% |
| file_cluster_17 | 8 | 0.6% |
| file_cluster_12 | 6 | 0.4% |
| file_cluster_6 | 5 | 0.4% |
| file_cluster_0 | 4 | 0.3% |
| file_cluster_7 | 2 | 0.1% |
| file_cluster_9 | 2 | 0.1% |
| file_cluster_11 | 1 | 0.1% |
| file_cluster_15 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 56 | 3.9% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 76*

**Composition by Extension & Reason:**
- `.py`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 49 LOC), 1x Excluded (Machine-Generated Source Code Signature: 54 LOC)
- `.yml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 5x Unsupported Format (.undeterminable), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 7194 LOC)
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.disabled`: 3x Excluded (Unsupported Extension: '.DISABLED')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 1x Excluded (Static Asset Blob without Intent: 1260 LOC)
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py_tf`: 1x Excluded (Unsupported Extension: '.py_tf')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 91.1 | 11.9 | 7.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 89.8 | 10.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.9 | 2.8 | 80.0 |
| API Exposure | 0.0 | 11.9 | 2.2 | 1.3 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 98.5 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 79.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.2 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 54.6 | 1.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 43.4 | 14.8 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 40.3 | 14.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 19.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/validate_solutions.py` (Hits: 17)
- `scripts/close_pull_requests_with_awaiting_changes.sh` (Hits: 12)
- `scripts/close_pull_requests_with_failing_tests.sh` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **greatest_common_divisor.py** (`maths/greatest_common_divisor.py`) — 8 inbound connections
2. **hash_table.py** (`data_structures/hashing/hash_table.py`) — 3 inbound connections
3. **kd_node.py** (`data_structures/kd_tree/kd_node.py`) — 3 inbound connections
4. **stack.py** (`data_structures/stacks/stack.py`) — 3 inbound connections
5. **prime_check.py** (`maths/prime_check.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sequential_minimum_optimization.py** (`machine_learning/sequential_minimum_optimization.py`) — 10 outbound dependencies
2. **test_digital_image_processing.py** (`digital_image_processing/test_digital_image_processing.py`) — 9 outbound dependencies
3. **automatic_differentiation.py** (`machine_learning/automatic_differentiation.py`) — 8 outbound dependencies
4. **input_data.py** (`neural_network/input_data.py`) — 8 outbound dependencies
5. **validate_solutions.py** (`scripts/validate_solutions.py`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `next_term` (@ `project_euler/problem_551/sol1.py`) -> Impact: **312.0** | LOC: 68
- `remove` (@ `data_structures/binary_tree/red_black_tree.py`) -> Impact: **293.7** | LOC: 55
- `_remove_repair` (@ `data_structures/binary_tree/red_black_tree.py`) -> Impact: **280.8** | LOC: 73
- `_insert_repair` (@ `data_structures/binary_tree/red_black_tree.py`) -> Impact: **244.4** | LOC: 38
- `solve_all` (@ `data_structures/arrays/sudoku_solver.py`) -> Impact: **224.2** | LOC: 83
- `visualise` (@ `cellular_automata/wa_tor.py`) -> Impact: **205.9** | LOC: 48
- `solve_simultaneous` (@ `maths/simultaneous_linear_equation_solver.py`) -> Impact: **202.6** | LOC: 51
- `infix_2_postfix` (@ `data_structures/stacks/infix_to_prefix_conversion.py`) -> Impact: **194.4** | LOC: 88
- `__str__` (@ `matrix/sherman_morrison.py`) -> Impact: **177.1** | LOC: 148
- `train` (@ `machine_learning/decision_tree.py`) -> Impact: **170.8** | LOC: 55

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `solve_crossword` (@ `backtracking/crossword_puzzle_solver.py`) -> **O(2^N) [Recursive]**
- `visualise` (@ `cellular_automata/wa_tor.py`) -> **O(2^N) [Recursive]**
- `remove` (@ `data_structures/binary_tree/red_black_tree.py`) -> **O(2^N) [Recursive]**
- `_insert_repair` (@ `data_structures/binary_tree/red_black_tree.py`) -> **O(2^N) [Recursive]**
- `delete` (@ `data_structures/trie/radix_tree.py`) -> **O(2^N) [Recursive]**
- `decrypt` (@ `ciphers/brute_force_caesar_cipher.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ >>> decrypt('TMDETUX PMDVU') Decryption using Key #0: TMDETUX PMDVU Decryption using Key #1: SLCDSTW OLCUT Decryption using Key #2: RKBCRSV NKBTS ...
- `floor` (@ `data_structures/binary_tree/red_black_tree.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # There are issues with coloring below children nodes return None if left != right: # The two children have unequal depths return None # Return the bl...
- `ceil` (@ `data_structures/binary_tree/red_black_tree.py`) -> **O(2^N) [Recursive]**
- `_query_range` (@ `data_structures/binary_tree/segment_tree_other.py`) -> **O(2^N) [Recursive]**
- `insert` (@ `data_structures/trie/radix_tree.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block` (@ `scripts/close_pull_requests_with_awaiting_changes.sh`) -> DB Complexity: **50**
  * *Intent:* # Loop through each pull request
- `Anonymous_Block` (@ `scripts/close_pull_requests_with_failing_tests.sh`) -> DB Complexity: **50**
  * *Intent:* # Loop through each pull request
- `Anonymous_Block` (@ `scripts/close_pull_requests_with_require_descriptive_names.sh`) -> DB Complexity: **50**
  * *Intent:* # Loop through each pull request
- `Anonymous_Block` (@ `scripts/close_pull_requests_with_require_tests.sh`) -> DB Complexity: **50**
  * *Intent:* # Loop through each pull request
- `Anonymous_Block` (@ `scripts/close_pull_requests_with_require_type_hints.sh`) -> DB Complexity: **50**
  * *Intent:* # Loop through each pull request
- `Anonymous_Block` (@ `scripts/find_git_conflicts.sh`) -> DB Complexity: **29**
  * *Intent:* # Process each conflicting PR
- `main` (@ `ciphers/transposition_cipher_encrypt_decrypt_file.py`) -> DB Complexity: **21**
- `test_cancer_data` (@ `machine_learning/sequential_minimum_optimization.py`) -> DB Complexity: **21**
- `main` (@ `data_compression/peak_signal_to_noise_ratio.py`) -> DB Complexity: **18**
- `delete_min` (@ `data_structures/heap/binomial_heap.py`) -> DB Complexity: **18**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `graphs` | 61 | 7817.88 | 26.2% | 54.36% |
| `data_structures/binary_tree` | 34 | 5531.56 | 14.34% | 68.93% |
| `maths` | 127 | 5068.18 | 10.99% | 43.01% |
| `dynamic_programming` | 51 | 2840.0 | 14.66% | 55.16% |
| `sorts` | 53 | 2604.26 | 13.52% | 18.39% |
| `ciphers` | 48 | 2574.14 | 11.26% | 31.08% |
| `machine_learning` | 32 | 2489.32 | 11.45% | 43.46% |
| `strings` | 57 | 2471.42 | 11.29% | 49.34% |
| `matrix` | 22 | 2469.06 | 14.42% | 40.25% |
| `other` | 28 | 2238.16 | 19.41% | 54.07% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bit_manipulation/binary_coded_decimal.py` -> **100.0%** Exposure
- `bit_manipulation/excess_3_code.py` -> **100.0%** Exposure
- `bit_manipulation/is_even.py` -> **100.0%** Exposure
- `bit_manipulation/is_power_of_two.py` -> **100.0%** Exposure
- `bit_manipulation/numbers_different_signs.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `backtracking/all_subsequences.py` -> **100.0%** Exposure
- `backtracking/generate_parentheses_iterative.py` -> **100.0%** Exposure
- `data_structures/arrays/permutations.py` -> **100.0%** Exposure
- `data_structures/heap/binomial_heap.py` -> **100.0%** Exposure
- `data_structures/queues/circular_queue.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `graphs/directed_and_undirected_weighted_graph.py` -> **4** Orphaned Functions | **22** Duplicates
- `linear_algebra/src/test_linear_algebra.py` -> **22** Orphaned Functions | **0** Duplicates
- `graphs/graph_adjacency_list.py` -> **18** Orphaned Functions | **0** Duplicates
- `graphs/graph_adjacency_matrix.py` -> **18** Orphaned Functions | **0** Duplicates
- `geometry/tests/test_graham_scan.py` -> **17** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`machine_learning/sequential_minimum_optimization.py`** -> AI Confidence: **99.31%**
2. **`ciphers/autokey.py`** -> AI Confidence: **99.29%**
3. **`conversions/rgb_hsv_conversion.py`** -> AI Confidence: **99.29%**
4. **`dynamic_programming/longest_common_subsequence.py`** -> AI Confidence: **99.29%**
5. **`dynamic_programming/palindrome_partitioning.py`** -> AI Confidence: **99.29%**
6. **`financial/straight_line_depreciation.py`** -> AI Confidence: **99.29%**
7. **`graphs/a_star.py`** -> AI Confidence: **99.29%**
8. **`graphs/dijkstra_2.py`** -> AI Confidence: **99.29%**
9. **`graphs/graphs_floyd_warshall.py`** -> AI Confidence: **99.29%**
10. **`graphs/kahns_algorithm_long.py`** -> AI Confidence: **99.29%**
11. **`greedy_methods/minimum_coin_change.py`** -> AI Confidence: **99.29%**
12. **`hashes/hamming_code.py`** -> AI Confidence: **99.29%**
13. **`knapsack/greedy_knapsack.py`** -> AI Confidence: **99.29%**
14. **`linear_algebra/src/polynom_for_points.py`** -> AI Confidence: **99.29%**
15. **`maths/jaccard_similarity.py`** -> AI Confidence: **99.29%**
16. **`maths/three_sum.py`** -> AI Confidence: **99.29%**
17. **`project_euler/problem_003/sol2.py`** -> AI Confidence: **99.29%**
18. **`project_euler/problem_017/sol1.py`** -> AI Confidence: **99.29%**
19. **`project_euler/problem_019/sol1.py`** -> AI Confidence: **99.29%**
20. **`sorts/binary_insertion_sort.py`** -> AI Confidence: **99.29%**
21. **`strings/manacher.py`** -> AI Confidence: **99.29%**
22. **`strings/wildcard_pattern_matching.py`** -> AI Confidence: **99.29%**
23. **`backtracking/crossword_puzzle_solver.py`** -> AI Confidence: **99.17%**
24. **`boolean_algebra/karnaugh_map_simplification.py`** -> AI Confidence: **99.17%**
25. **`cellular_automata/conways_game_of_life.py`** -> AI Confidence: **99.17%**
26. **`ciphers/base64_cipher.py`** -> AI Confidence: **99.17%**
27. **`ciphers/decrypt_caesar_with_chi_squared.py`** -> AI Confidence: **99.17%**
28. **`ciphers/mixed_keyword_cypher.py`** -> AI Confidence: **99.17%**
29. **`conversions/time_conversions.py`** -> AI Confidence: **99.17%**
30. **`data_structures/stacks/infix_to_prefix_conversion.py`** -> AI Confidence: **99.17%**
31. **`dynamic_programming/abbreviation.py`** -> AI Confidence: **99.17%**
32. **`dynamic_programming/catalan_numbers.py`** -> AI Confidence: **99.17%**
33. **`dynamic_programming/integer_partition.py`** -> AI Confidence: **99.17%**
34. **`dynamic_programming/longest_common_substring.py`** -> AI Confidence: **99.17%**
35. **`dynamic_programming/longest_palindromic_subsequence.py`** -> AI Confidence: **99.17%**
36. **`dynamic_programming/optimal_binary_search_tree.py`** -> AI Confidence: **99.17%**
37. **`dynamic_programming/smith_waterman.py`** -> AI Confidence: **99.17%**
38. **`dynamic_programming/sum_of_subset.py`** -> AI Confidence: **99.17%**
39. **`dynamic_programming/wildcard_matching.py`** -> AI Confidence: **99.17%**
40. **`graphs/articulation_points.py`** -> AI Confidence: **99.17%**
41. **`linear_algebra/src/rank_of_matrix.py`** -> AI Confidence: **99.17%**
42. **`maths/segmented_sieve.py`** -> AI Confidence: **99.17%**
43. **`maths/simultaneous_linear_equation_solver.py`** -> AI Confidence: **99.17%**
44. **`maths/special_numbers/hamming_numbers.py`** -> AI Confidence: **99.17%**
45. **`matrix/spiral_print.py`** -> AI Confidence: **99.17%**
46. **`networking_flow/minimum_cut.py`** -> AI Confidence: **99.17%**
47. **`other/alternative_list_arrange.py`** -> AI Confidence: **99.17%**
48. **`project_euler/problem_003/sol3.py`** -> AI Confidence: **99.17%**
49. **`project_euler/problem_004/sol1.py`** -> AI Confidence: **99.17%**
50. **`project_euler/problem_004/sol2.py`** -> AI Confidence: **99.17%**
51. **`project_euler/problem_005/sol1.py`** -> AI Confidence: **99.17%**
52. **`project_euler/problem_010/sol3.py`** -> AI Confidence: **99.17%**
53. **`project_euler/problem_011/sol2.py`** -> AI Confidence: **99.17%**
54. **`project_euler/problem_014/sol1.py`** -> AI Confidence: **99.17%**
55. **`project_euler/problem_015/sol2.py`** -> AI Confidence: **99.17%**
56. **`project_euler/problem_018/solution.py`** -> AI Confidence: **99.17%**
57. **`project_euler/problem_023/sol1.py`** -> AI Confidence: **99.17%**
58. **`project_euler/problem_067/sol1.py`** -> AI Confidence: **99.17%**
59. **`project_euler/problem_069/sol1.py`** -> AI Confidence: **99.17%**
60. **`project_euler/problem_074/sol2.py`** -> AI Confidence: **99.17%**
61. **`project_euler/problem_076/sol1.py`** -> AI Confidence: **99.17%**
62. **`project_euler/problem_081/sol1.py`** -> AI Confidence: **99.17%**
63. **`project_euler/problem_082/sol1.py`** -> AI Confidence: **99.17%**
64. **`project_euler/problem_116/sol1.py`** -> AI Confidence: **99.17%**
65. **`project_euler/problem_135/sol1.py`** -> AI Confidence: **99.17%**
66. **`project_euler/problem_551/sol1.py`** -> AI Confidence: **99.17%**
67. **`sorts/exchange_sort.py`** -> AI Confidence: **99.17%**
68. **`sorts/heap_sort.py`** -> AI Confidence: **99.17%**
69. **`sorts/odd_even_sort.py`** -> AI Confidence: **99.17%**
70. **`sorts/recursive_mergesort_array.py`** -> AI Confidence: **99.17%**
71. **`sorts/selection_sort.py`** -> AI Confidence: **99.17%**
72. **`sorts/topological_sort.py`** -> AI Confidence: **99.17%**
73. **`strings/alternative_string_arrange.py`** -> AI Confidence: **99.17%**
74. **`strings/damerau_levenshtein_distance.py`** -> AI Confidence: **99.17%**
75. **`strings/is_isogram.py`** -> AI Confidence: **99.17%**
76. **`strings/min_cost_string_conversion.py`** -> AI Confidence: **99.17%**
77. **`machine_learning/automatic_differentiation.py`** -> AI Confidence: **99.15%**
78. **`neural_network/input_data.py`** -> AI Confidence: **99.15%**
79. **`scripts/validate_solutions.py`** -> AI Confidence: **99.15%**
80. **`web_programming/download_images_from_google_query.py`** -> AI Confidence: **99.15%**
81. **`cellular_automata/game_of_life.py`** -> AI Confidence: **99.13%**
82. **`cellular_automata/wa_tor.py`** -> AI Confidence: **99.13%**
83. **`ciphers/affine_cipher.py`** -> AI Confidence: **99.13%**
84. **`computer_vision/flip_augmentation.py`** -> AI Confidence: **99.13%**
85. **`computer_vision/mosaic_augmentation.py`** -> AI Confidence: **99.13%**
86. **`graphs/graph_adjacency_list.py`** -> AI Confidence: **99.13%**
87. **`graphs/graph_adjacency_matrix.py`** -> AI Confidence: **99.13%**
88. **`hashes/md5.py`** -> AI Confidence: **99.13%**
89. **`matrix/tests/test_matrix_operation.py`** -> AI Confidence: **99.13%**
90. **`searches/simulated_annealing.py`** -> AI Confidence: **99.13%**
91. **`sorts/bubble_sort.py`** -> AI Confidence: **99.13%**
92. **`backtracking/rat_in_maze.py`** -> AI Confidence: **99.11%**
93. **`boolean_algebra/multiplexer.py`** -> AI Confidence: **99.11%**
94. **`conversions/binary_to_hexadecimal.py`** -> AI Confidence: **99.11%**
95. **`conversions/binary_to_octal.py`** -> AI Confidence: **99.11%**
96. **`conversions/hex_to_bin.py`** -> AI Confidence: **99.11%**
97. **`conversions/hexadecimal_to_decimal.py`** -> AI Confidence: **99.11%**
98. **`dynamic_programming/all_construct.py`** -> AI Confidence: **99.11%**
99. **`dynamic_programming/fizz_buzz.py`** -> AI Confidence: **99.11%**
100. **`graphs/g_topological_sort.py`** -> AI Confidence: **99.11%**
101. **`graphs/kahns_algorithm_topo.py`** -> AI Confidence: **99.11%**
102. **`maths/geometric_mean.py`** -> AI Confidence: **99.11%**
103. **`maths/hardy_ramanujanalgo.py`** -> AI Confidence: **99.11%**
104. **`maths/prime_sieve_eratosthenes.py`** -> AI Confidence: **99.11%**
105. **`matrix/cramers_rule_2x2.py`** -> AI Confidence: **99.11%**
106. **`physics/rainfall_intensity.py`** -> AI Confidence: **99.11%**
107. **`sorts/gnome_sort.py`** -> AI Confidence: **99.11%**
108. **`cellular_automata/one_dimensional.py`** -> AI Confidence: **99.09%**
109. **`ciphers/atbash.py`** -> AI Confidence: **99.09%**
110. **`ciphers/rsa_cipher.py`** -> AI Confidence: **99.09%**
111. **`conversions/convert_number_to_words.py`** -> AI Confidence: **99.09%**
112. **`data_compression/lempel_ziv.py`** -> AI Confidence: **99.09%**
113. **`data_structures/binary_tree/red_black_tree.py`** -> AI Confidence: **99.09%**
114. **`data_structures/hashing/hash_table.py`** -> AI Confidence: **99.09%**
115. **`data_structures/linked_list/is_palindrome.py`** -> AI Confidence: **99.09%**
116. **`digital_image_processing/filters/gabor_filter.py`** -> AI Confidence: **99.09%**
117. **`divide_and_conquer/mergesort.py`** -> AI Confidence: **99.09%**
118. **`dynamic_programming/k_means_clustering_tensorflow.py`** -> AI Confidence: **99.09%**
119. **`dynamic_programming/longest_increasing_subsequence_iterative.py`** -> AI Confidence: **99.09%**
120. **`dynamic_programming/minimum_squares_to_represent_a_number.py`** -> AI Confidence: **99.09%**
121. **`dynamic_programming/word_break.py`** -> AI Confidence: **99.09%**
122. **`electronics/builtin_voltage.py`** -> AI Confidence: **99.09%**
123. **`electronics/ind_reactance.py`** -> AI Confidence: **99.09%**
124. **`graphics/vector3_for_2d_rendering.py`** -> AI Confidence: **99.09%**
125. **`graphs/basic_graphs.py`** -> AI Confidence: **99.09%**
126. **`graphs/boruvka.py`** -> AI Confidence: **99.09%**
127. **`graphs/dijkstra_algorithm.py`** -> AI Confidence: **99.09%**
128. **`graphs/dijkstra_binary_grid.py`** -> AI Confidence: **99.09%**
129. **`graphs/graph_list.py`** -> AI Confidence: **99.09%**
130. **`graphs/multi_heuristic_astar.py`** -> AI Confidence: **99.09%**
131. **`greedy_methods/fractional_knapsack.py`** -> AI Confidence: **99.09%**
132. **`machine_learning/apriori_algorithm.py`** -> AI Confidence: **99.09%**
133. **`machine_learning/frequent_pattern_growth.py`** -> AI Confidence: **99.09%**
134. **`maths/numerical_analysis/weierstrass_method.py`** -> AI Confidence: **99.09%**
135. **`maths/radix2_fft.py`** -> AI Confidence: **99.09%**
136. **`maths/zellers_congruence.py`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `backtracking/crossword_puzzle_solver.py` -> **100.0%** Exposure
- `boolean_algebra/quine_mc_cluskey.py` -> **100.0%** Exposure
- `cellular_automata/conways_game_of_life.py` -> **100.0%** Exposure
- `cellular_automata/wa_tor.py` -> **100.0%** Exposure
- `ciphers/deterministic_miller_rabin.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `data_structures/binary_tree/maximum_fenwick_tree.py` -> **100.0%** Exposure
- `data_structures/binary_tree/non_recursive_segment_tree.py` -> **100.0%** Exposure
- `data_structures/binary_tree/segment_tree.py` -> **100.0%** Exposure
- `graphs/edmonds_karp_multiple_source_and_sink.py` -> **100.0%** Exposure
- `neural_network/convolution_neural_network.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `audio_filters/iir_filter.py` -> **100.0%** Exposure
- `backtracking/crossword_puzzle_solver.py` -> **100.0%** Exposure
- `backtracking/generate_parentheses_iterative.py` -> **100.0%** Exposure
- `backtracking/sudoku.py` -> **100.0%** Exposure
- `boolean_algebra/quine_mc_cluskey.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2041` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `graphs/edmonds_karp_multiple_source_and_sink.py` (PYTHON) -> Cumulative Risk: **908.54**
- **Archetype:** `file_cluster_8` (Distance: 12.743 IQR)
- **Magnitude:** 279.86 | **LOC:** 194 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_normalize_graph` (Impact: 61.7), `_algorithm` (Impact: 31.9), `process_vertex` (Impact: 26.6)

### 2. `graphs/directed_and_undirected_weighted_graph.py` (PYTHON) -> Cumulative Risk: **843.05**
- **Archetype:** `file_cluster_13` (Distance: 13.111 IQR)
- **Magnitude:** 1145.28 | **LOC:** 490 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `cycle_nodes` (Impact: 99.6), `cycle_nodes` (Impact: 99.6), `has_cycle` (Impact: 99.5)

### 3. `neural_network/convolution_neural_network.py` (PYTHON) -> Cumulative Risk: **819.59**
- **Archetype:** `file_cluster_8` (Distance: 10.715 IQR)
- **Magnitude:** 227.98 | **LOC:** 358 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `convolute` (Impact: 49.4), `pooling` (Impact: 48.1), `predict` (Impact: 14.2)

### 4. `dynamic_programming/bitmask.py` (PYTHON) -> Cumulative Risk: **804.39**
- **Archetype:** `file_cluster_17` (Distance: 19.241 IQR)
- **Magnitude:** 130.44 | **LOC:** 90 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `count_ways_until` (Impact: 85.6), `count_no_of_ways` (Impact: 13.4), `__init__` (Impact: 12.7)

### 5. `data_structures/queues/double_ended_queue.py` (PYTHON) -> Cumulative Risk: **803.61**
- **Archetype:** `file_cluster_13` (Distance: 15.761 IQR)
- **Magnitude:** 210.22 | **LOC:** 464 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__eq__` (Impact: 27.1), `__init__` (Impact: 13.4), `pop` (Impact: 11.4)

### 6. `machine_learning/automatic_differentiation.py` (PYTHON) -> Cumulative Risk: **792.08**
- **Archetype:** `file_cluster_13` (Distance: 15.104 IQR)
- **Magnitude:** 295.12 | **LOC:** 329 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9932%)
- **Heaviest Functions:** `derivative` (Impact: 66.7), `gradient` (Impact: 31.1), `__pow__` (Impact: 16.2)

### 7. `data_structures/linked_list/__init__.py` (PYTHON) -> Cumulative Risk: **788.84**
- **Archetype:** `file_cluster_16` (Distance: 11.425 IQR)
- **Magnitude:** 101.18 | **LOC:** 134 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9992%)
- **Heaviest Functions:** `add` (Impact: 42.9), `__str__` (Impact: 18.1), `remove` (Impact: 10.9)

### 8. `machine_learning/astar.py` (PYTHON) -> Cumulative Risk: **779.76**
- **Archetype:** `file_cluster_8` (Distance: 11.511 IQR)
- **Magnitude:** 136.14 | **LOC:** 149 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9989%)
- **Heaviest Functions:** `astar` (Impact: 67.7), `get_neighbours` (Impact: 18.6), `__init__` (Impact: 3.2)

### 9. `maths/dual_number_automatic_differentiation.py` (PYTHON) -> Cumulative Risk: **779.5**
- **Archetype:** `file_cluster_8` (Distance: 12.423 IQR)
- **Magnitude:** 210.72 | **LOC:** 140 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `differentiate` (Impact: 48.7), `__mul__` (Impact: 31.1), `__pow__` (Impact: 21.3)

### 10. `data_structures/heap/binomial_heap.py` (PYTHON) -> Cumulative Risk: **777.51**
- **Archetype:** `file_cluster_8` (Distance: 12.587 IQR)
- **Magnitude:** 476.96 | **LOC:** 402 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `merge_heaps` (Impact: 112.7), `delete_min` (Impact: 88.2), `__traversal` (Impact: 54.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `data_structures/binary_tree/red_black_tree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.655 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.541 IQR)
- **Top Global Matches:** file_cluster_16: 12.655, file_cluster_8: 12.813, file_cluster_7: 12.821
- **Magnitude:** 1894.18 | **LOC:** 717 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (40.8273%), Tech Debt (30.3633%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 293.7 | O(2^N) | DB: 10)
  * `_remove_repair` (Impact: 280.8 | O(2^N))
  * `_insert_repair` (Impact: 244.4 | O(2^N) | DB: 2)
  * `floor` (Impact: 94.3 | O(2^N) | DB: 1)
    * *Intent:* # There are issues with coloring below children nodes return None if left != right: # The two childr...
  * `ceil` (Impact: 94.3 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 138`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 213`, `orphaned_logic: 8`
* *Architecture:* `api: 33`, `import: 3`
* *Defense:* `safety: 8`, `doc: 70`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, pprint, collections.abc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graphs/directed_and_undirected_weighted_graph.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.111 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.239 IQR)
- **Top Global Matches:** file_cluster_13: 13.111, file_cluster_8: 13.116, file_cluster_0: 13.177
- **Magnitude:** 1145.28 | **LOC:** 490 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (79.747%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `cycle_nodes` (Impact: 99.6 | O(N^6) | DB: 6)
  * `cycle_nodes` (Impact: 99.6 | O(N^6) | DB: 6)
  * `has_cycle` (Impact: 99.5 | O(N^6) | DB: 6)
  * `has_cycle` (Impact: 99.5 | O(N^6) | DB: 6)
  * `dfs` (Impact: 92.8 | O(N^6) | DB: 6)
    * *Intent:* # if no destination is meant the default value is -1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 71`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 154`, `dead_code: 6`, `duplicate_logic: 22`, `orphaned_logic: 4`
* *Architecture:* `api: 26`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, random, math, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `machine_learning/sequential_minimum_optimization.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.996 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.967 IQR)
- **Top Global Matches:** file_cluster_13: 10.996, file_cluster_8: 11.065, file_cluster_0: 11.194
- **Magnitude:** 663.28 | **LOC:** 623 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (41.3653%), Tech Debt (22.0757%)
**Top Internal Functions/Classes:**
  * `_get_new_alpha` (Impact: 122.1 | O(N^4) | DB: 1)
  * `fit` (Impact: 81.1 | O(N^5) | DB: 2)
  * `_choose_a1` (Impact: 63.8 | O(N^5))
    * *Intent:* # Calculate kernel matrix of all possible i1, i2, saving time
  * `test_cancer_data` (Impact: 63.8 | O(2^N) | DB: 21)
  * `_choose_a2` (Impact: 57.8 | O(N^4) | DB: 1)
    * *Intent:* """ Choose first alpha Steps: 1: First loop over all samples 2: Second loop over all non-bound sampl...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 91`, `args: 35`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 74`, `dead_code: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 16`, `import: 9`
* *Defense:* `safety: 3`, `doc: 12`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sequential_minimum_optimization, matplotlib, sklearn.datasets, numpy, time, os, pandas, sklearn.preprocessing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `other/word_search.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.213 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.917 IQR)
- **Top Global Matches:** file_cluster_16: 10.213, file_cluster_8: 10.482, file_cluster_7: 10.747
- **Magnitude:** 583.44 | **LOC:** 396 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.5688%), Tech Debt (18.0471%)
**Top Internal Functions/Classes:**
  * `insert_northeast` (Impact: 71.7 | O(N^6))
  * `insert_southeast` (Impact: 71.7 | O(N^6))
    * *Intent:* # Check if there are existing letters # to the right of the column that will be overwritten
  * `insert_southwest` (Impact: 71.7 | O(N^6))
  * `insert_northwest` (Impact: 71.7 | O(N^6))
  * `insert_north` (Impact: 63.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 35`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` random, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matrix/matrix_class.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.445 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.516 IQR)
- **Top Global Matches:** file_cluster_16: 11.445, file_cluster_8: 11.574, file_cluster_0: 11.635
- **Magnitude:** 571.34 | **LOC:** 367 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (51.027%), Tech Debt (96.9146%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 67.6 | O(N^6) | DB: 2)
  * `add_column` (Impact: 56.0 | O(N^4) | DB: 2)
  * `__mul__` (Impact: 53.0 | O(N^5))
  * `add_row` (Impact: 45.8 | O(N^4) | DB: 2)
  * `determinant` (Impact: 31.2 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 68`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `orphaned_logic: 13`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `safety: 9`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graphs/graph_adjacency_list.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.849 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.149 IQR)
- **Top Global Matches:** file_cluster_16: 10.849, file_cluster_8: 10.943, file_cluster_13: 11.199
- **Magnitude:** 526.92 | **LOC:** 598 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.0913%), Tech Debt (88.0925%)
**Top Internal Functions/Classes:**
  * `test_remove_edge_exception_check` (Impact: 47.9 | O(N^5) | DB: 1)
  * `test_contains_edge` (Impact: 38.0 | O(N^5) | DB: 2)
  * `test_add_and_remove_edges_repeatedly` (Impact: 38.0 | O(N^5) | DB: 1)
  * `remove_vertex` (Impact: 37.4 | O(N^5) | DB: 3)
    * *Intent:* """ if self.contains_vertex(vertex): msg = f"Incorrect input: {vertex} is already in the graph." rai...
  * `add_edge` (Impact: 36.2 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 62`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 40`, `orphaned_logic: 18`
* *Architecture:* `api: 23`, `import: 6`
* *Defense:* `safety: 15`, `doc: 18`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, unittest, typing, random, __future__, pprint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graphs/graph_adjacency_matrix.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.598 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.086 IQR)
- **Top Global Matches:** file_cluster_16: 10.598, file_cluster_8: 10.667, file_cluster_13: 10.977
- **Magnitude:** 514.12 | **LOC:** 610 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.5068%), Tech Debt (86.327%)
**Top Internal Functions/Classes:**
  * `test_remove_edge_exception_check` (Impact: 47.9 | O(N^5) | DB: 1)
  * `test_contains_edge` (Impact: 38.0 | O(N^5) | DB: 2)
  * `test_add_and_remove_edges_repeatedly` (Impact: 38.0 | O(N^5) | DB: 1)
  * `add_edge` (Impact: 36.2 | O(N^4))
  * `remove_edge` (Impact: 36.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 62`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 33`, `orphaned_logic: 18`
* *Architecture:* `api: 23`, `import: 6`
* *Defense:* `safety: 15`, `doc: 18`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, unittest, typing, random, __future__, pprint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linear_algebra/src/lib.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.732 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.444 IQR)
- **Top Global Matches:** file_cluster_16: 12.732, file_cluster_13: 12.921, file_cluster_0: 13.074
- **Magnitude:** 497.06 | **LOC:** 445 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.6516%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__mul__` (Impact: 55.8 | O(N^6))
  * `change_component` (Impact: 36.1 | O(2^N))
  * `__add__` (Impact: 31.9 | O(N^5) | DB: 3)
  * `__sub__` (Impact: 31.9 | O(N^5) | DB: 3)
    * *Intent:* """ returns a zero-vector of size 'dimension' """
  * `determinant` (Impact: 31.3 | O(N^4) | DB: 2)
    * *Intent:* """ if self.__width == other.width() and self.__height == other.height(): matrix = [] for i in range...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 86`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 30`, `duplicate_logic: 14`
* *Architecture:* `api: 29`, `import: 5`
* *Defense:* `safety: 19`, `doc: 66`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.255
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000701
  * `Imports (Out-Degree: 0):` collections.abc, typing, random, math, __future__
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `data_structures/heap/binomial_heap.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.587 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.427 IQR)
- **Top Global Matches:** file_cluster_8: 12.587, file_cluster_7: 12.775, file_cluster_13: 12.867
- **Magnitude:** 476.96 | **LOC:** 402 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (37.7703%), Tech Debt (88.3013%)
**Top Internal Functions/Classes:**
  * `merge_heaps` (Impact: 112.7 | O(N^5) | DB: 9)
  * `delete_min` (Impact: 88.2 | O(N^5) | DB: 18)
  * `__traversal` (Impact: 54.8 | O(2^N) | DB: 2)
  * `insert` (Impact: 38.3 | O(N^5) | DB: 7)
  * `merge_trees` (Impact: 22.7 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 29`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 128`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 1`, `doc: 22`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data_structures/arrays/sudoku_solver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.571 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_8: 10.571, file_cluster_17: 10.829, file_cluster_7: 10.834
- **Magnitude:** 472.68 | **LOC:** 260 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (14.8554%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `solve_all` (Impact: 224.2 | O(2^N) | DB: 4)
  * `eliminate` (Impact: 97.1 | O(2^N))
    * *Intent:* """ Convert grid into a dict of {square: char} with '0' or '.' for empties. """
  * `search` (Impact: 36.9 | O(2^N))
  * `display` (Impact: 31.0 | O(N^4))
    * *Intent:* """ if d not in values[s]: return values ## Already eliminated values[s] = values[s].replace(d, "") ...
  * `parse_grid` (Impact: 14.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 54`, `args: 17`, `func_start: 17`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 17`, `import: 2`
* *Defense:* `safety: 7`, `doc: 30`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` random, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cellular_automata/wa_tor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.317 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.738 IQR)
- **Top Global Matches:** file_cluster_16: 11.317, file_cluster_13: 11.509, file_cluster_8: 11.551
- **Magnitude:** 471.0 | **LOC:** 549 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (23.5018%), Tech Debt (67.9179%)
**Top Internal Functions/Classes:**
  * `visualise` (Impact: 205.9 | O(2^N))
  * `run` (Impact: 58.0 | O(N^6) | DB: 1)
  * `balance_predators_and_prey` (Impact: 39.9 | O(N^4))
  * `__init__` (Impact: 22.9 | O(N^3) | DB: 5)
  * `get_surrounding_prey` (Impact: 21.7 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 34`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 39`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 13`, `import: 6`
* *Defense:* `safety: 2`, `doc: 32`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time, os, typing, random, collections.abc, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data_structures/trie/radix_tree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.922 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.712 IQR)
- **Top Global Matches:** file_cluster_16: 11.922, file_cluster_8: 12.078, file_cluster_7: 12.314
- **Magnitude:** 433.98 | **LOC:** 230 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (26.4891%), Tech Debt (44.8577%)
**Top Internal Functions/Classes:**
  * `delete` (Impact: 159.6 | O(2^N) | DB: 2)
  * `insert` (Impact: 105.9 | O(2^N) | DB: 4)
  * `find` (Impact: 61.6 | O(2^N))
    * *Intent:* # Case 2: The node has no edges that have a prefix to the word # Solution: We create an edge from th...
  * `print_tree` (Impact: 35.0 | O(2^N))
  * `match` (Impact: 17.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 31`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `orphaned_logic: 2`
* *Architecture:* `api: 10`
* *Defense:* `safety: 7`, `doc: 16`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `project_euler/problem_551/sol1.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.205 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.073 IQR)
- **Top Global Matches:** file_cluster_8: 9.205, file_cluster_7: 9.541, file_cluster_16: 9.841
- **Magnitude:** 423.4 | **LOC:** 201 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (17.2839%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `next_term` (Impact: 312.0 | O(2^N) | DB: 1)
  * `compute` (Impact: 51.0 | O(N^3) | DB: 1)
  * `add` (Impact: 24.9 | O(N^3) | DB: 1)
    * *Intent:* # note: a_i -> b * 10^k + c # ds_b -> digitsum(b) # ds_c -> digitsum(c) start_i = i ds_b, ds_c, diff...
  * `solution` (Impact: 20.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `api: 4`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data_structures/binary_tree/binary_search_tree_recursive.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.295 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.581 IQR)
- **Top Global Matches:** file_cluster_16: 13.295, file_cluster_13: 13.423, file_cluster_8: 13.506
- **Magnitude:** 402.9 | **LOC:** 642 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (8.9731%), Tech Debt (95.2574%)
**Top Internal Functions/Classes:**
  * `_put` (Impact: 54.3 | O(2^N))
  * `_search` (Impact: 40.5 | O(2^N))
  * `remove` (Impact: 39.9 | O(N^4))
  * `_reassign_nodes` (Impact: 30.6 | O(N^4) | DB: 1)
    * *Intent:* """ Searches a node in the tree >>> t = BinarySearchTree() >>> t.put(8) >>> t.put(10) >>> node = t.s...
  * `_get_lowest_node` (Impact: 21.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 130`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `state_mutation: 31`, `duplicate_logic: 2`, `orphaned_logic: 11`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 76`, `doc: 52`, `test: 93`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, pytest, unittest, collections.abc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graphs/basic_graphs.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.001 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.234 IQR)
- **Top Global Matches:** file_cluster_8: 12.001, file_cluster_16: 12.094, file_cluster_7: 12.153
- **Magnitude:** 400.98 | **LOC:** 410 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (32.7654%), Tech Debt (84.4217%)
**Top Internal Functions/Classes:**
  * `topo` (Impact: 101.0 | O(2^N) | DB: 2)
  * `dijk` (Impact: 48.6 | O(N^4))
  * `krusk` (Impact: 47.8 | O(N^5) | DB: 3)
  * `prim` (Impact: 39.8 | O(N^4))
  * `floy` (Impact: 31.7 | O(N^5))
    * *Intent:* """ -------------------------------------------------------------------------------- Topological Sor...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 32`, `args: 15`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 48`, `orphaned_logic: 7`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` io, collections, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data_structures/binary_tree/avl_tree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.597 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.964 IQR)
- **Top Global Matches:** file_cluster_16: 10.597, file_cluster_8: 10.742, file_cluster_13: 10.85
- **Magnitude:** 394.28 | **LOC:** 350 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (17.8628%), Tech Debt (99.9654%)
**Top Internal Functions/Classes:**
  * `del_node` (Impact: 127.0 | O(2^N))
  * `insert_node` (Impact: 88.0 | O(2^N))
  * `get_height` (Impact: 14.9 | O(2^N))
  * `del_node` (Impact: 14.2 | O(2^N) | DB: 1)
  * `get_right_most` (Impact: 12.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 80`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 19`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `api: 29`, `import: 5`
* *Defense:* `safety: 8`, `doc: 10`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, random, math, __future__, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graphs/multi_heuristic_astar.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.396 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.734 IQR)
- **Top Global Matches:** file_cluster_8: 10.396, file_cluster_13: 10.884, file_cluster_7: 10.984
- **Magnitude:** 384.54 | **LOC:** 313 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (55.3662%), Tech Debt (54.4525%)
**Top Internal Functions/Classes:**
  * `multi_a_star` (Impact: 136.7 | O(N^6) | DB: 4)
  * `do_something` (Impact: 62.0 | O(N^4) | DB: 3)
  * `make_common_ground` (Impact: 35.7 | O(N^3) | DB: 5)
  * `put` (Impact: 25.8 | O(N^4) | DB: 2)
  * `remove_element` (Impact: 17.8 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 34`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 42`, `fragile_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 16`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` heapq, numpy, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data_structures/binary_tree/binary_search_tree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.057 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.799 IQR)
- **Top Global Matches:** file_cluster_13: 11.057, file_cluster_16: 11.107, file_cluster_0: 11.28
- **Magnitude:** 378.74 | **LOC:** 357 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (14.9681%), Tech Debt (99.9918%)
**Top Internal Functions/Classes:**
  * `__insert` (Impact: 61.8 | O(N^6) | DB: 1)
  * `remove` (Impact: 61.7 | O(2^N) | DB: 1)
  * `search` (Impact: 30.9 | O(N^4))
  * `__reassign_nodes` (Impact: 30.5 | O(N^4) | DB: 1)
  * `get_max` (Impact: 22.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 58`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 12`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 7`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 3`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, collections.abc, __future__, pprint, dataclasses, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `strings/autocomplete_using_trie.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.585 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.238 IQR)
- **Top Global Matches:** file_cluster_16: 9.585, file_cluster_8: 9.752, file_cluster_13: 9.783
- **Magnitude:** 372.23 | **LOC:** 66 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.7465%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 14`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `project_euler/problem_054/sol1.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.459 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.539 IQR)
- **Top Global Matches:** file_cluster_16: 11.459, file_cluster_13: 11.499, file_cluster_8: 11.536
- **Magnitude:** 366.02 | **LOC:** 385 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (24.9269%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_is_same_kind` (Impact: 59.1 | O(N^5) | DB: 2)
    * *Intent:* # Breaking the tie works on the following order of precedence: # 1. First pair (default 0) # 2. Seco...
  * `compare_with` (Impact: 44.6 | O(N^4) | DB: 2)
  * `_get_hand_type` (Impact: 35.6 | O(N^4))
    * *Intent:* """ if not isinstance(hand, str): msg = f"Hand should be of type 'str': {hand!r}" raise TypeError(ms...
  * `hand_name` (Impact: 32.1 | O(N^3) | DB: 2)
  * `_compare_cards` (Impact: 22.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 64`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 14`, `import: 2`
* *Defense:* `safety: 6`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data_structures/linked_list/skip_list.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.785 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.5 IQR)
- **Top Global Matches:** file_cluster_13: 13.785, file_cluster_0: 13.949, file_cluster_11: 14.022
- **Magnitude:** 364.3 | **LOC:** 449 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (33.2241%), Tech Debt (90.8185%)
**Top Internal Functions/Classes:**
  * `insert` (Impact: 55.4 | O(N^5) | DB: 4)
  * `delete` (Impact: 43.1 | O(N^6))
  * `__str__` (Impact: 31.9 | O(N^4) | DB: 5)
  * `_locate_node` (Impact: 31.8 | O(N^4) | DB: 1)
  * `random_level` (Impact: 10.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 85`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 88`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 20`, `import: 5`
* *Defense:* `safety: 39`, `doc: 31`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` itertools, typing, random, __future__, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `maths/area.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.456 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.977 IQR)
- **Top Global Matches:** file_cluster_16: 10.456, file_cluster_8: 10.544, file_cluster_7: 10.785
- **Magnitude:** 356.18 | **LOC:** 584 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.766%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `area_triangle_three_sides` (Impact: 42.8 | O(2^N))
  * `area_reg_polygon` (Impact: 35.3 | O(2^N))
  * `surface_area_torus` (Impact: 35.1 | O(2^N))
  * `surface_area_cuboid` (Impact: 24.3 | O(2^N))
  * `area_trapezium` (Impact: 24.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 41`, `args: 18`, `func_start: 18`
* *Risk/State:* None
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `safety: 1`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `maths/simultaneous_linear_equation_solver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.661 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.735 IQR)
- **Top Global Matches:** file_cluster_8: 11.661, file_cluster_16: 11.801, file_cluster_13: 11.857
- **Magnitude:** 353.48 | **LOC:** 143 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (39.452%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `solve_simultaneous` (Impact: 202.6 | O(2^N) | DB: 8)
  * `simplify` (Impact: 102.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 45`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `strings/is_valid_email_address.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.481 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.443 IQR)
- **Top Global Matches:** file_cluster_8: 7.481, file_cluster_7: 8.06, file_cluster_13: 8.065
- **Magnitude:** 340.73 | **LOC:** 116 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.4805%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 4`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hashes/hamming_code.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.848 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.936 IQR)
- **Top Global Matches:** file_cluster_8: 12.848, file_cluster_13: 12.914, file_cluster_17: 12.955
- **Magnitude:** 305.76 | **LOC:** 293 | **CtrlFlow:** 81.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (42.0565%), Tech Debt (98.8393%)
**Top Internal Functions/Classes:**
  * `receptor_converter` (Impact: 123.8 | O(N^5) | DB: 11)
    * *Intent:* # parity bit counter # counter position of data bits cont_data = 0 for x in range(1, size_par + len(...
  * `emitter_converter` (Impact: 112.4 | O(N^5) | DB: 8)
  * `text_from_bits` (Impact: 4.2 | O(N^1))
    * *Intent:* * the implemented code consists of: * a function responsible for encoding the message (emitterConver...
  * `text_to_bits` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 10`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 57`, `planned_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 4`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `divide_and_conquer/inversions.py` (PYTHON) | Magnitude: 73.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 12, branch: 11, structural_boundaries: 11
- `data_compression/lz77.py` (PYTHON) | Magnitude: 87.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 20, doc: 16, branch: 13
- `web_programming/instagram_crawler.py` (PYTHON) | Magnitude: 92.24 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 59, args: 17, func_start: 17
- `maths/test_factorial.py` (PYTHON) | Magnitude: 21.56 | Delta: **0.325 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 19, structural_boundaries: 13, indent_spaces: 10, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `data_structures/stacks/infix_to_prefix_conversion.py` (PYTHON) | Magnitude: 230.74 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 33, branch: 18, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/find_git_conflicts.sh` (SHELL) | Magnitude: 1.89 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 12, io: 10, structural_boundaries: 7, debug_prints: 6
- `scripts/close_pull_requests_with_require_descriptive_names.sh` (SHELL) | Magnitude: 2.64 | Delta: **0.182 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 15, io: 12, indent_spaces: 9, branch: 8
- `scripts/close_pull_requests_with_require_tests.sh` (SHELL) | Magnitude: 2.65 | Delta: **0.182 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 15, io: 12, indent_spaces: 9, branch: 8
- `scripts/close_pull_requests_with_require_type_hints.sh` (SHELL) | Magnitude: 2.64 | Delta: **0.182 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 15, io: 12, indent_spaces: 9, branch: 8
- `scripts/close_pull_requests_with_awaiting_changes.sh` (SHELL) | Magnitude: 2.65 | Delta: **0.19 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 15, io: 12, indent_spaces: 10, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `data_compression/run_length_encoding.py` (PYTHON) | Magnitude: 30.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, branch: 6, structural_boundaries: 6, doc: 4
- `machine_learning/apriori_algorithm.py` (PYTHON) | Magnitude: 100.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 35, branch: 17, structural_boundaries: 12, doc: 10
- `data_structures/heap/skew_heap.py` (PYTHON) | Magnitude: 98.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 27, doc: 22, encapsulation: 20
- `dynamic_programming/min_distance_up_bottom.py` (PYTHON) | Magnitude: 13.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, doc: 4, branch: 3
- `neural_network/input_data.py` (PYTHON) | Magnitude: 177.8 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 192, encapsulation: 69, structural_boundaries: 55, branch: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `data_structures/stacks/prefix_evaluation.py` (PYTHON) | Magnitude: 49.02 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 16, doc: 8, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `backtracking/all_combinations.py` (PYTHON) | Magnitude: 26.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, branch: 10, state_mutation: 9
- `maths/spearman_rank_correlation_coefficient.py` (PYTHON) | Magnitude: 13.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 9, structural_boundaries: 7, branch: 5
- `strings/naive_string_search.py` (PYTHON) | Magnitude: 26.7 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, branch: 5, structural_boundaries: 4, doc: 4
- `project_euler/problem_016/sol2.py` (PYTHON) | Magnitude: 8.86 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, doc: 4, branch: 2, structural_boundaries: 2
- `maths/perfect_square.py` (PYTHON) | Magnitude: 25.26 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, doc: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `strings/manacher.py` (PYTHON) | Magnitude: 56.26 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, branch: 13, doc: 4, structural_boundaries: 3
- `maths/gcd_of_n_numbers.py` (PYTHON) | Magnitude: 22.84 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, branch: 16, structural_boundaries: 11, doc: 6
- `graphs/random_graph_generator.py` (PYTHON) | Magnitude: 21.86 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 18, branch: 11, structural_boundaries: 8, state_mutation: 6
- `machine_learning/linear_discriminant_analysis.py` (PYTHON) | Magnitude: 151.9 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, doc: 46, branch: 35, debug_prints: 32
- `ciphers/xor_cipher.py` (PYTHON) | Magnitude: 121.68 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 36, safety: 28, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `project_euler/problem_004/sol1.py` (PYTHON) | Magnitude: 38.94 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 10, branch: 5, doc: 4, structural_boundaries: 2
- `project_euler/problem_191/sol1.py` (PYTHON) | Magnitude: 36.18 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, encapsulation: 7, doc: 6
- `sorts/topological_sort.py` (PYTHON) | Magnitude: 68.48 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, branch: 6, state_mutation: 6, generics: 6
- `data_structures/binary_tree/inorder_tree_traversal_2022.py` (PYTHON) | Magnitude: 57.98 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 11, doc: 8, branch: 6
- `maths/bailey_borwein_plouffe.py` (PYTHON) | Magnitude: 16.58 | Delta: **0.361 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 25, branch: 8, encapsulation: 7, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `maths/trapezoidal_rule.py` (PYTHON) | Magnitude: 19.78 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, doc: 18, structural_boundaries: 7, args: 4
- `financial/exponential_moving_average.py` (PYTHON) | Magnitude: 2.56 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, branch: 7, doc: 7, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `data_structures/arrays/kth_largest_element.py` (PYTHON) | Magnitude: 50.92 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 28, branch: 12, structural_boundaries: 8, doc: 6
- `strings/is_pangram.py` (PYTHON) | Magnitude: 10.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 12, doc: 10, branch: 8
- `maths/signum.py` (PYTHON) | Magnitude: 16.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 13, test: 10, safety: 9
- `matrix/searching_in_sorted_matrix.py` (PYTHON) | Magnitude: 31.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 17, branch: 6, structural_boundaries: 6, debug_prints: 4
- `graphs/dijkstra_binary_grid.py` (PYTHON) | Magnitude: 9.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, branch: 11, structural_boundaries: 9, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `graphs/graph_list.py` (PYTHON) | Magnitude: 28.96 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 19, structural_boundaries: 12, branch: 11
- `graphs/greedy_min_vertex_cover.py` (PYTHON) | Magnitude: 38.36 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, branch: 7, structural_boundaries: 6, dead_code: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `graphs/graph_adjacency_matrix.py` -> **Christian Clauss** (100.0% isolated ownership) | Magnitude: 514.12
- `data_structures/trie/radix_tree.py` -> **Christian Clauss** (100.0% isolated ownership) | Magnitude: 433.98
- `project_euler/problem_551/sol1.py` -> **Christian Clauss** (100.0% isolated ownership) | Magnitude: 423.4
- `maths/area.py` -> **Jaime Fernández González** (100.0% isolated ownership) | Magnitude: 356.18
- `machine_learning/decision_tree.py` -> **Harsh Pathak** (100.0% isolated ownership) | Magnitude: 285.1

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `data_structures/hashing/hash_table.py` -> **Severity: 0.107** (Embedded: 0.0021 * Error Risk: 51.1268%)
- `maths/prime_factors.py` -> **Severity: 0.092** (Embedded: 0.0014 * Error Risk: 65.7143%)
- `data_structures/suffix_tree/suffix_tree_node.py` -> **Severity: 0.069** (Embedded: 0.0013 * Error Risk: 54.9551%)
- `web_programming/fetch_github_info.py` -> **Severity: 0.056** (Embedded: 0.0007 * Error Risk: 80.0%)
- `graphs/minimum_spanning_tree_kruskal.py` -> **Severity: 0.048** (Embedded: 0.0007 * Error Risk: 68.4615%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `maths/greatest_common_divisor.py` -> **Severity: 529.2** (Blast Radius: 5.292 * Doc Risk: 100.0%)
- `maths/prime_check.py` -> **Severity: 240.895** (Blast Radius: 2.409 * Doc Risk: 99.9981%)
- `data_structures/stacks/stack.py` -> **Severity: 236.433** (Blast Radius: 2.366 * Doc Risk: 99.9293%)
- `data_structures/hashing/hash_table.py` -> **Severity: 211.994** (Blast Radius: 2.12 * Doc Risk: 99.9973%)
- `data_structures/suffix_tree/suffix_tree.py` -> **Severity: 183.2** (Blast Radius: 1.832 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
