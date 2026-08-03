# ARCHITECTURAL_BRIEF: javascript-algorithms
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/javascript-algorithms` |
| **Timestamp** | `2026-08-03T20:05:33.500904+00:00` |
| **Scan Duration** | `1.24s` |
| **Git Branch** | `master` |
| **Git Commit** | `115e42816808484f76de4e6703caa8280e03ed54` |
| **Git Remote** | `https://github.com/trekhleb/javascript-algorithms.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 359 malicious artifacts.

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
| Total Artifacts | 676 |
| Analyzed Artifacts (Scanned) | 621 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 55 |
| Total LOC | 14633 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 91.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8662 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.628 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.5013 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 76 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 359 | 14608 | 57.8% |
| MARKDOWN | 258 | 0 | 41.5% |
| JSON | 2 | 24 | 0.3% |
| PLAINTEXT | 2 | 1 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.893`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 292 | 47.0% |
| file_cluster_13 | 46 | 7.4% |
| file_cluster_17 | 15 | 2.4% |
| file_cluster_0 | 4 | 0.6% |
| file_cluster_15 | 3 | 0.5% |
| file_cluster_7 | 1 | 0.2% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 259 | 41.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 55*

**Composition by Extension & Reason:**
- `.png`: 27x Excluded (Explicitly Denied Extension: '.png')
- `.jpeg`: 12x Excluded (Explicitly Denied Extension: '.jpeg')
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Massive Static Asset Blob: 9728 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 83.7 | 15.4 | 7.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.7 | 13.2 | 2.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.5 | 0.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.9 | 3.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 99.8 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 89.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 78.0 | 1.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.9 | 5.8 | 2.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 10.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/algorithms/graph/travelling-salesman/bfTravellingSalesman.js` (Hits: 5)
- `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` (Hits: 5)
- `src/algorithms/math/fourier-transform/discreteFourierTransform.js` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **GraphVertex.js** (`src/data-structures/graph/GraphVertex.js`) — 21 inbound connections
2. **Graph.js** (`src/data-structures/graph/Graph.js`) — 20 inbound connections
3. **GraphEdge.js** (`src/data-structures/graph/GraphEdge.js`) — 20 inbound connections
4. **Comparator.js** (`src/utils/comparator/Comparator.js`) — 13 inbound connections
5. **SortTester.js** (`src/algorithms/sorting/SortTester.js`) — 12 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **articulationPoints.test.js** (`src/algorithms/graph/articulation-points/__test__/articulationPoints.test.js`) — 4 outbound dependencies
2. **bellmanFord.test.js** (`src/algorithms/graph/bellman-ford/__test__/bellmanFord.test.js`) — 4 outbound dependencies
3. **breadthFirstSearch.test.js** (`src/algorithms/graph/breadth-first-search/__test__/breadthFirstSearch.test.js`) — 4 outbound dependencies
4. **graphBridges.test.js** (`src/algorithms/graph/bridges/__test__/graphBridges.test.js`) — 4 outbound dependencies
5. **depthFirstSearch.test.js** (`src/algorithms/graph/depth-first-search/__test__/depthFirstSearch.test.js`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `balance` (@ `src/data-structures/tree/red-black-tree/RedBlackTree.js`) -> Impact: **99.3** | LOC: 62
  * *Intent:* /** * @param {*} value * @return {boolean}
- `isSafe` (@ `src/algorithms/uncategorized/n-queens/nQueens.js`) -> Impact: **75.6** | LOC: 72
  * *Intent:* /**
- `remove` (@ `src/data-structures/tree/binary-search-tree/BinarySearchTreeNode.js`) -> Impact: **66.3** | LOC: 53
- `getPhase` (@ `src/algorithms/math/complex-number/ComplexNumber.js`) -> Impact: **51.5** | LOC: 29
- `buildZArray` (@ `src/algorithms/string/z-algorithm/zAlgorithm.js`) -> Impact: **50.8** | LOC: 81
  * *Intent:* /**
- `solveZeroOneKnapsackProblem` (@ `src/algorithms/sets/knapsack-problem/Knapsack.js`) -> Impact: **49.6** | LOC: 87
  * *Intent:* /** * @var KnapsackItem itemA * @var KnapsackItem itemB */
- `KMeans` (@ `src/algorithms/ml/k-means/kMeans.js`) -> Impact: **47.8** | LOC: 75
  * *Intent:* /**
- `sort` (@ `src/algorithms/sorting/quick-sort/QuickSortInPlace.js`) -> Impact: **39.2** | LOC: 49
  * *Intent:* /** Sorting in place avoids unnecessary use of additional memory, but modifies input array.
- `longestCommonSubsequence` (@ `src/algorithms/sets/longest-common-subsequence/longestCommonSubsequence.js`) -> Impact: **39.1** | LOC: 55
  * *Intent:* /**
- `shortestCommonSupersequence` (@ `src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js`) -> Impact: **39.1** | LOC: 54
  * *Intent:* /** * @param {string[]} set1

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `balance` (@ `src/data-structures/tree/red-black-tree/RedBlackTree.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @param {*} value * @return {boolean}
- `sort` (@ `src/algorithms/sorting/quick-sort/QuickSort.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `sort` (@ `src/algorithms/sorting/quick-sort/QuickSortInPlace.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** Sorting in place avoids unnecessary use of additional memory, but modifies input array.
- `buildZArray` (@ `src/algorithms/string/z-algorithm/zAlgorithm.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `knightTourRecursive` (@ `src/algorithms/uncategorized/knight-tour/knightTour.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `isSafe` (@ `src/algorithms/uncategorized/n-queens/nQueens.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `set` (@ `src/data-structures/lru-cache/LRUCacheOnMap.js`) -> **O(2^N) [Recursive]**
- `remove` (@ `src/data-structures/tree/binary-search-tree/BinarySearchTreeNode.js`) -> **O(2^N) [Recursive]**
- `insert` (@ `src/data-structures/tree/binary-search-tree/BinarySearchTreeNode.js`) -> **O(2^N) [Recursive]**
- `hash` (@ `src/algorithms/cryptography/polynomial-hash/PolynomialHash.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `src/data-structures/heap/__test__/MinHeap.test.js`) -> DB Complexity: **43**
- `describe` (@ `src/data-structures/heap/__test__/MaxHeap.test.js`) -> DB Complexity: **34**
- `describe` (@ `src/data-structures/priority-queue/__test__/PriorityQueue.test.js`) -> DB Complexity: **28**
- `solveZeroOneKnapsackProblem` (@ `src/algorithms/sets/knapsack-problem/Knapsack.js`) -> DB Complexity: **27**
  * *Intent:* /** * @var KnapsackItem itemA * @var KnapsackItem itemB */
- `describe` (@ `src/data-structures/stack/__test__/Stack.test.js`) -> DB Complexity: **20**
- `balance` (@ `src/data-structures/tree/red-black-tree/RedBlackTree.js`) -> DB Complexity: **20**
  * *Intent:* /** * @param {*} value * @return {boolean}
- `getPhase` (@ `src/algorithms/math/complex-number/ComplexNumber.js`) -> DB Complexity: **19**
- `remove` (@ `src/data-structures/heap/Heap.js`) -> DB Complexity: **17**
  * *Intent:* /**
- `heapifyDown` (@ `src/data-structures/heap/MaxHeapAdhoc.js`) -> DB Complexity: **17**
- `heapifyDown` (@ `src/data-structures/heap/MinHeapAdhoc.js`) -> DB Complexity: **17**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 27 | 5167.18 | 0.92% | 0.0% |
| `src/data-structures/heap` | 14 | 665.9 | 15.88% | 1.02% |
| `src/data-structures/linked-list` | 12 | 326.44 | 3.45% | 0.0% |
| `src/data-structures/tree/red-black-tree` | 3 | 269.76 | 15.44% | 0.0% |
| `src/algorithms/sets/knapsack-problem` | 3 | 266.38 | 22.64% | 0.0% |
| `src/data-structures/doubly-linked-list` | 10 | 252.6 | 4.97% | 0.0% |
| `src/data-structures/tree/binary-search-tree` | 4 | 244.9 | 17.9% | 0.0% |
| `src/data-structures/graph` | 9 | 242.96 | 13.4% | 0.0% |
| `src/data-structures/lru-cache` | 4 | 226.44 | 17.72% | 24.66% |
| `src/data-structures/disjoint-set` | 7 | 206.98 | 15.41% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/algorithms/math/is-power-of-two/isPowerOfTwoBitwise.js` -> **100.0%** Exposure
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/accumulatorBestTimeToBuySellStocks.js` -> **100.0%** Exposure
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/dpBestTimeToBuySellStocks.js` -> **100.0%** Exposure
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/peakvalleyBestTimeToBuySellStocks.js` -> **100.0%** Exposure
- `src/algorithms/uncategorized/hanoi-tower/hanoiTower.js` -> **99.9541%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/algorithms/cryptography/polynomial-hash/PolynomialHash.js` -> **100.0%** Exposure
- `src/algorithms/linked-list/traversal/traversal.js` -> **100.0%** Exposure
- `src/algorithms/math/bits/bitLength.js` -> **100.0%** Exposure
- `src/algorithms/math/bits/countSetBits.js` -> **100.0%** Exposure
- `src/algorithms/math/complex-number/ComplexNumber.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/algorithms/math/binary-floating-point/__tests__/bitsToFloat.test.js` -> **0** Orphaned Functions | **3** Duplicates
- `src/algorithms/graph/hamiltonian-cycle/hamiltonianCycle.js` -> **0** Orphaned Functions | **2** Duplicates
- `src/algorithms/math/binary-floating-point/__tests__/floatAsBinaryString.test.js` -> **0** Orphaned Functions | **2** Duplicates
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/accumulatorBestTimeToBuySellStocks.js` -> **0** Orphaned Functions | **2** Duplicates
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/dpBestTimeToBuySellStocks.js` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`jest.config.js`** -> AI Confidence: **99.29%**
2. **`src/algorithms/math/complex-number/ComplexNumber.js`** -> AI Confidence: **99.17%**
3. **`src/algorithms/graph/dijkstra/dijkstra.js`** -> AI Confidence: **99.06%**
4. **`src/algorithms/graph/eulerian-path/eulerianPath.js`** -> AI Confidence: **99.06%**
5. **`src/algorithms/linked-list/reverse-traversal/reverseTraversal.js`** -> AI Confidence: **99.06%**
6. **`src/algorithms/linked-list/traversal/traversal.js`** -> AI Confidence: **99.06%**
7. **`src/algorithms/math/bits/updateBit.js`** -> AI Confidence: **99.06%**
8. **`src/algorithms/math/euclidean-algorithm/euclideanAlgorithm.js`** -> AI Confidence: **99.06%**
9. **`src/algorithms/math/euclidean-algorithm/euclideanAlgorithmIterative.js`** -> AI Confidence: **99.06%**
10. **`src/algorithms/math/factorial/factorialRecursive.js`** -> AI Confidence: **99.06%**
11. **`src/algorithms/math/fibonacci/fibonacciNthClosedForm.js`** -> AI Confidence: **99.06%**
12. **`src/algorithms/math/fourier-transform/discreteFourierTransform.js`** -> AI Confidence: **99.06%**
13. **`src/algorithms/math/least-common-multiple/leastCommonMultiple.js`** -> AI Confidence: **99.06%**
14. **`src/algorithms/math/pascal-triangle/pascalTriangleRecursive.js`** -> AI Confidence: **99.06%**
15. **`src/algorithms/math/primality-test/trialDivision.js`** -> AI Confidence: **99.06%**
16. **`src/algorithms/math/sieve-of-eratosthenes/sieveOfEratosthenes.js`** -> AI Confidence: **99.06%**
17. **`src/algorithms/math/square-root/squareRoot.js`** -> AI Confidence: **99.06%**
18. **`src/algorithms/ml/k-means/kMeans.js`** -> AI Confidence: **99.06%**
19. **`src/algorithms/ml/knn/kNN.js`** -> AI Confidence: **99.06%**
20. **`src/algorithms/search/binary-search/binarySearch.js`** -> AI Confidence: **99.06%**
21. **`src/algorithms/search/interpolation-search/interpolationSearch.js`** -> AI Confidence: **99.06%**
22. **`src/algorithms/sets/knapsack-problem/Knapsack.js`** -> AI Confidence: **99.06%**
23. **`src/algorithms/sets/longest-common-subsequence/longestCommonSubsequence.js`** -> AI Confidence: **99.06%**
24. **`src/algorithms/sets/longest-increasing-subsequence/dpLongestIncreasingSubsequence.js`** -> AI Confidence: **99.06%**
25. **`src/algorithms/sets/maximum-subarray/dcMaximumSubarraySum.js`** -> AI Confidence: **99.06%**
26. **`src/algorithms/sets/power-set/bwPowerSet.js`** -> AI Confidence: **99.06%**
27. **`src/algorithms/sets/power-set/caPowerSet.js`** -> AI Confidence: **99.06%**
28. **`src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js`** -> AI Confidence: **99.06%**
29. **`src/algorithms/sorting/quick-sort/QuickSort.js`** -> AI Confidence: **99.06%**
30. **`src/algorithms/stack/valid-parentheses/validParentheses.js`** -> AI Confidence: **99.06%**
31. **`src/algorithms/statistics/weighted-random/weightedRandom.js`** -> AI Confidence: **99.06%**
32. **`src/algorithms/string/hamming-distance/hammingDistance.js`** -> AI Confidence: **99.06%**
33. **`src/algorithms/string/knuth-morris-pratt/knuthMorrisPratt.js`** -> AI Confidence: **99.06%**
34. **`src/algorithms/string/regular-expression-matching/regularExpressionMatching.js`** -> AI Confidence: **99.06%**
35. **`src/algorithms/string/z-algorithm/zAlgorithm.js`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/algorithms/sets/knapsack-problem/Knapsack.js` -> **100.0%** Exposure
- `src/algorithms/sorting/shell-sort/ShellSort.js` -> **100.0%** Exposure
- `src/data-structures/doubly-linked-list/DoublyLinkedList.js` -> **100.0%** Exposure
- `src/data-structures/heap/Heap.js` -> **100.0%** Exposure
- `src/data-structures/tree/red-black-tree/RedBlackTree.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `src/algorithms/math/fourier-transform/fastFourierTransform.js` -> **100.0%** Exposure
- `src/algorithms/ml/k-means/kMeans.js` -> **100.0%** Exposure
- `src/algorithms/sets/knapsack-problem/Knapsack.js` -> **100.0%** Exposure
- `src/algorithms/sorting/bubble-sort/BubbleSort.js` -> **100.0%** Exposure
- `src/algorithms/sorting/counting-sort/CountingSort.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/data-structures/heap/Heap.js` (JAVASCRIPT) -> Cumulative Risk: **574.11**
- **Archetype:** `file_cluster_8` (Distance: 14.927 IQR)
- **Magnitude:** 296.64 | **LOC:** 287 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `remove` (Impact: 29.6), `heapifyDown` (Impact: 22.4), `find` (Impact: 8.3)

### 2. `src/algorithms/sets/knapsack-problem/Knapsack.js` (JAVASCRIPT) -> Cumulative Risk: **557.0**
- **Archetype:** `file_cluster_17` (Distance: 14.152 IQR)
- **Magnitude:** 231.18 | **LOC:** 196 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `solveZeroOneKnapsackProblem` (Impact: 49.6), `solveUnboundedKnapsackProblem` (Impact: 9.6), `sortPossibleItemsByWeight` (Impact: 7.0)

### 3. `src/data-structures/doubly-linked-list/DoublyLinkedList.js` (JAVASCRIPT) -> Cumulative Risk: **555.99**
- **Archetype:** `file_cluster_13` (Distance: 14.166 IQR)
- **Magnitude:** 217.8 | **LOC:** 264 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `delete` (Impact: 30.7), `deleteHead` (Impact: 6.5), `deleteTail` (Impact: 5.4)

### 4. `src/algorithms/sorting/shell-sort/ShellSort.js` (JAVASCRIPT) -> Cumulative Risk: **551.42**
- **Archetype:** `file_cluster_8` (Distance: 11.837 IQR)
- **Magnitude:** 39.5 | **LOC:** 42 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `sort` (Impact: 16.0)

### 5. `src/data-structures/tree/red-black-tree/RedBlackTree.js` (JAVASCRIPT) -> Cumulative Risk: **541.73**
- **Archetype:** `file_cluster_13` (Distance: 13.899 IQR)
- **Magnitude:** 265.96 | **LOC:** 324 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `balance` (Impact: 99.3), `leftLeftRotation` (Impact: 14.6), `rightRightRotation` (Impact: 14.6)

### 6. `src/data-structures/heap/MaxHeapAdhoc.js` (JAVASCRIPT) -> Cumulative Risk: **497.62**
- **Archetype:** `file_cluster_8` (Distance: 13.262 IQR)
- **Magnitude:** 174.84 | **LOC:** 116 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (93.7869%)
- **Heaviest Functions:** `heapifyDown` (Impact: 24.8), `heapifyUp` (Impact: 6.1), `poll` (Impact: 3.2)

### 7. `src/data-structures/heap/MinHeapAdhoc.js` (JAVASCRIPT) -> Cumulative Risk: **497.02**
- **Archetype:** `file_cluster_8` (Distance: 13.217 IQR)
- **Magnitude:** 174.98 | **LOC:** 118 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (93.2031%)
- **Heaviest Functions:** `heapifyDown` (Impact: 24.9), `heapifyUp` (Impact: 6.1), `poll` (Impact: 3.2)

### 8. `src/algorithms/sorting/SortTester.js` (JAVASCRIPT) -> Cumulative Risk: **478.69**
- **Archetype:** `file_cluster_8` (Distance: 12.076 IQR)
- **Magnitude:** 61.2 | **LOC:** 73 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9837%), Documentation (99.8729%), Algorithmic Dos (96.1368%)
- **Heaviest Functions:** `testSortWithCustomComparator` (Impact: 8.7), `testSortStability` (Impact: 8.5), `testAlgorithmTimeComplexity` (Impact: 2.5)

### 9. `src/data-structures/graph/Graph.js` (JAVASCRIPT) -> Cumulative Risk: **463.35**
- **Archetype:** `file_cluster_8` (Distance: 13.401 IQR)
- **Magnitude:** 117.44 | **LOC:** 204 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (78.0472%), Algorithmic Dos (61.27%)
- **Heaviest Functions:** `addEdge` (Impact: 18.6), `findEdge` (Impact: 7.4), `reverse` (Impact: 3.6)

### 10. `src/algorithms/sorting/selection-sort/SelectionSort.js` (JAVASCRIPT) -> Cumulative Risk: **460.47**
- **Archetype:** `file_cluster_13` (Distance: 12.835 IQR)
- **Magnitude:** 35.4 | **LOC:** 33 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9727%), Cognitive Load (80.2184%)
- **Heaviest Functions:** `sort` (Impact: 12.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/heap/Heap.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.927 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.548 IQR)
- **Top Global Matches:** file_cluster_8: 14.927, file_cluster_13: 14.942, file_cluster_7: 14.989
- **Magnitude:** 296.64 | **LOC:** 287 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (44.8748%), Tech Debt (14.2366%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 29.6 | O(N^3) | DB: 17)
    * *Intent:* /**
  * `heapifyDown` (Impact: 22.4 | O(N^2) | DB: 13)
  * `find` (Impact: 8.3 | O(N^2) | DB: 5)
  * `heapifyUp` (Impact: 6.4 | O(N^1) | DB: 9)
  * `poll` (Impact: 5.1 | O(N^1) | DB: 9)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 27`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 183`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 5`, `doc: 60`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.445
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.008793
  * `Imports (Out-Degree: 1):` Comparator
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/data-structures/linked-list/LinkedList.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.214 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.551 IQR)
- **Top Global Matches:** file_cluster_13: 14.214, file_cluster_8: 14.272, file_cluster_17: 14.378
- **Magnitude:** 279.22 | **LOC:** 273 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (36.3567%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `insert` (Impact: 30.0 | O(N^2) | DB: 9)
    * *Intent:* /** * @param {*} value * @return {LinkedList}
  * `delete` (Impact: 20.8 | O(N^2) | DB: 14)
  * `deleteTail` (Impact: 12.0 | O(N^2) | DB: 8)
  * `deleteHead` (Impact: 6.5 | O(N^1) | DB: 7)
  * `reverse` (Impact: 4.0 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 34`, `args: 13`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 179`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 5`, `doc: 33`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.628
  * `Choke Point (Betweenness):` 0.000258 | `Ripple Effect (Closeness):` 0.036684
  * `Imports (Out-Degree: 2):` Comparator, LinkedListNode
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/red-black-tree/RedBlackTree.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.899 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.655 IQR)
- **Top Global Matches:** file_cluster_13: 13.899, file_cluster_8: 13.919, file_cluster_7: 13.998
- **Magnitude:** 265.96 | **LOC:** 324 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (46.3056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `balance` (Impact: 99.3 | O(2^N) | DB: 20)
    * *Intent:* /** * @param {*} value * @return {boolean}
  * `leftLeftRotation` (Impact: 14.6 | O(N^2) | DB: 3)
  * `rightRightRotation` (Impact: 14.6 | O(N^2) | DB: 3)
  * `insert` (Impact: 9.3 | O(2^N) | DB: 5)
    * *Intent:* /**
  * `remove` (Impact: 3.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 21`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 105`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 2`, `doc: 38`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 1):` BinarySearchTree
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/knapsack-problem/Knapsack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.152 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.748 IQR)
- **Top Global Matches:** file_cluster_17: 14.152, file_cluster_11: 14.325, file_cluster_13: 14.336
- **Magnitude:** 231.18 | **LOC:** 196 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (35.6251%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `solveZeroOneKnapsackProblem` (Impact: 49.6 | O(N^3) | DB: 27)
    * *Intent:* /** * @var KnapsackItem itemA * @var KnapsackItem itemB */
  * `solveUnboundedKnapsackProblem` (Impact: 9.6 | O(N^2) | DB: 11)
  * `sortPossibleItemsByWeight` (Impact: 7.0 | O(N^2) | DB: 3)
  * `sortPossibleItemsByValue` (Impact: 7.0 | O(N^2) | DB: 3)
  * `sortPossibleItemsByValuePerWeightRatio` (Impact: 7.0 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 27`, `args: 14`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 135`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 5`, `doc: 8`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.527
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 1):` MergeSort
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/doubly-linked-list/DoublyLinkedList.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.166 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.785 IQR)
- **Top Global Matches:** file_cluster_13: 14.166, file_cluster_8: 14.259, file_cluster_17: 14.33
- **Magnitude:** 217.8 | **LOC:** 264 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (44.7421%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `delete` (Impact: 30.7 | O(N^3) | DB: 14)
    * *Intent:* /**
  * `deleteHead` (Impact: 6.5 | O(N^1) | DB: 8)
  * `deleteTail` (Impact: 5.4 | O(N^1) | DB: 10)
  * `reverse` (Impact: 4.1 | O(N^1) | DB: 8)
  * `prepend` (Impact: 3.4 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 31`, `args: 13`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 143`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 5`, `doc: 32`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 2):` Comparator, DoublyLinkedListNode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/binary-search-tree/BinarySearchTreeNode.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.724 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.425 IQR)
- **Top Global Matches:** file_cluster_13: 13.724, file_cluster_8: 13.836, file_cluster_17: 13.851
- **Magnitude:** 210.62 | **LOC:** 152 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (39.5696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 66.3 | O(2^N) | DB: 5)
  * `insert` (Impact: 27.1 | O(2^N) | DB: 15)
  * `find` (Impact: 17.9 | O(2^N) | DB: 10)
  * `constructor` (Impact: 2.1 | O(N^1) | DB: 2)
    * *Intent:* /**
  * `contains` (Impact: 1.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 20`, `args: 6`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 91`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `doc: 18`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.534
  * `Choke Point (Betweenness):` 8.1e-05 | `Ripple Effect (Closeness):` 0.005645
  * `Imports (Out-Degree: 2):` BinaryTreeNode, Comparator
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/BinaryTreeNode.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.199 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 2.971 IQR)
- **Top Global Matches:** file_cluster_13: 14.199, file_cluster_8: 14.242, file_cluster_7: 14.304
- **Magnitude:** 188.76 | **LOC:** 220 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (35.1032%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `replaceChild` (Impact: 13.0 | O(N^1) | DB: 8)
  * `traverseInOrder` (Impact: 9.4 | O(2^N) | DB: 7)
  * `removeChild` (Impact: 7.7 | O(N^1) | DB: 8)
    * *Intent:* /** * @param {*} value * @return {BinaryTreeNode}
  * `setLeft` (Impact: 5.0 | O(N^1) | DB: 5)
  * `setRight` (Impact: 5.0 | O(N^1) | DB: 4)
    * *Intent:* // Check if grand-parent has two children.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 23`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 120`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.575
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.007806
  * `Imports (Out-Degree: 2):` Comparator, HashTable
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/MinHeapAdhoc.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.217 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.007 IQR)
- **Top Global Matches:** file_cluster_8: 13.217, file_cluster_17: 13.503, file_cluster_13: 13.605
- **Magnitude:** 174.98 | **LOC:** 118 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (83.7496%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `heapifyDown` (Impact: 24.9 | O(N^2) | DB: 17)
  * `heapifyUp` (Impact: 6.1 | O(N^1) | DB: 6)
  * `poll` (Impact: 3.2 | O(N^1) | DB: 8)
  * `constructor` (Impact: 2.2 | O(N^1) | DB: 2)
  * `swap` (Impact: 2.0 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 16`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 111`
* *Architecture:* `api: 6`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/MaxHeapAdhoc.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.262 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.028 IQR)
- **Top Global Matches:** file_cluster_8: 13.262, file_cluster_17: 13.537, file_cluster_13: 13.643
- **Magnitude:** 174.84 | **LOC:** 116 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (83.7381%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `heapifyDown` (Impact: 24.8 | O(N^2) | DB: 17)
  * `heapifyUp` (Impact: 6.1 | O(N^1) | DB: 6)
  * `poll` (Impact: 3.2 | O(N^1) | DB: 8)
  * `constructor` (Impact: 2.2 | O(N^1) | DB: 2)
  * `swap` (Impact: 2.0 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 16`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 111`
* *Architecture:* `api: 6`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/lru-cache/LRUCache.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.729 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.079 IQR)
- **Top Global Matches:** file_cluster_8: 14.729, file_cluster_7: 14.862, file_cluster_13: 14.923
- **Magnitude:** 145.92 | **LOC:** 154 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (32.76%), Tech Debt (98.6482%)
**Top Internal Functions/Classes:**
  * `evict` (Impact: 8.7 | O(N^1) | DB: 13)
    * *Intent:* /** * Promotes the node to the end of the linked list. * It means that the node is most frequently u...
  * `append` (Impact: 6.9 | O(N^1) | DB: 14)
  * `set` (Impact: 5.7 | O(N^1) | DB: 4)
    * *Intent:* /** * Creates a cache instance of a specific capacity.
  * `get` (Impact: 3.1 | O(N^1) | DB: 3)
    * *Intent:* /** * Implementation of the LRU (Least Recently Used) Cache * based on the HashMap and Doubly Linked...
  * `constructor` (Impact: 2.5 | O(N^1) | DB: 4)
    * *Intent:* /* eslint-disable no-param-reassign, max-classes-per-file */ /** * Simple implementation of the Doub...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 9`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 113`, `duplicate_logic: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 5`, `doc: 21`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/math/complex-number/ComplexNumber.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.029 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.345 IQR)
- **Top Global Matches:** file_cluster_13: 15.029, file_cluster_8: 15.23, file_cluster_7: 15.269
- **Magnitude:** 142.04 | **LOC:** 161 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (48.9468%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getPhase` (Impact: 51.5 | O(N^1) | DB: 19)
  * `toComplexNumber` (Impact: 3.2 | O(N^1))
    * *Intent:* /** * @param {ComplexNumber|number} number
  * `getPolarForm` (Impact: 2.3 | O(N^1) | DB: 2)
  * `multiply` (Impact: 2.2 | O(N^1) | DB: 3)
    * *Intent:* // Make sure we're dealing with complex number.
  * `add` (Impact: 1.9 | O(N^1) | DB: 3)
    * *Intent:* /** * z = re + im * i * z = radius * e^(i * phase) * * @param {number} [re] * @param {number} [im] *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 11`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 73`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 7`, `doc: 20`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.369
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.010323
  * `Imports (Out-Degree: 1):` radianToDegree
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/data-structures/graph/Graph.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.401 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.612 IQR)
- **Top Global Matches:** file_cluster_8: 13.401, file_cluster_7: 13.485, file_cluster_17: 13.53
- **Magnitude:** 117.44 | **LOC:** 204 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (43.5331%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addEdge` (Impact: 18.6 | O(2^N) | DB: 11)
  * `findEdge` (Impact: 7.4 | O(2^N) | DB: 1)
  * `reverse` (Impact: 3.6 | O(2^N) | DB: 5)
  * `addVertex` (Impact: 3.4 | O(N^1) | DB: 2)
  * `getAdjacencyMatrix` (Impact: 3.1 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 24`, `args: 19`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 59`
* *Architecture:* `api: 4`
* *Defense:* `doc: 34`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.318
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.032258
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/segment-tree/SegmentTree.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.53 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.896 IQR)
- **Top Global Matches:** file_cluster_8: 12.53, file_cluster_7: 12.654, file_cluster_13: 12.707
- **Magnitude:** 95.98 | **LOC:** 169 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (42.5896%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rangeQueryRecursive` (Impact: 26.1 | O(2^N) | DB: 7)
    * *Intent:* /**
  * `buildTreeRecursively` (Impact: 9.2 | O(2^N) | DB: 12)
    * *Intent:* /** * Build segment tree.
  * `initSegmentTree` (Impact: 5.2 | O(N^1) | DB: 1)
  * `constructor` (Impact: 2.5 | O(N^1) | DB: 7)
    * *Intent:* /**
  * `rangeQuery` (Impact: 2.4 | O(N^1) | DB: 2)
    * *Intent:* // Split input array on two halves and process them recursively.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 12`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 1`, `doc: 29`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` isPowerOfTwo
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/uncategorized/n-queens/nQueens.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.553 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.211 IQR)
- **Top Global Matches:** file_cluster_17: 14.553, file_cluster_13: 14.659, file_cluster_11: 14.865
- **Magnitude:** 83.38 | **LOC:** 104 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (19.6359%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isSafe` (Impact: 75.6 | O(2^N) | DB: 2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 9`, `args: 4`, `func_start: 5`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 5`, `doc: 15`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 1):` QueenPosition
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/sorting/radix-sort/RadixSort.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.291 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.869 IQR)
- **Top Global Matches:** file_cluster_8: 13.291, file_cluster_17: 13.38, file_cluster_7: 13.381
- **Magnitude:** 79.62 | **LOC:** 153 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (32.5077%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `placeElementsInNumberBuckets` (Impact: 8.7 | O(N^2) | DB: 4)
  * `sort` (Impact: 7.4 | O(N^2) | DB: 7)
    * *Intent:* /**
  * `getCharCodeOfElementAtIndex` (Impact: 6.5 | O(N^1))
    * *Intent:* /** * @param {*[]} array * @param {number} index
  * `getLengthOfLongestElement` (Impact: 4.7 | O(N^1) | DB: 1)
    * *Intent:* /** * @param {string} element * @param {number} index
  * `placeElementsInCharacterBuckets` (Impact: 2.5 | O(N^1) | DB: 4)
    * *Intent:* /** * Say we have element of 1,052 and are currently on index 1 (starting from 0). This means * we w...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 24`, `args: 14`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 33`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003629
  * `Imports (Out-Degree: 1):` Sort
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/data-structures/graph/GraphVertex.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.396 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.209 IQR)
- **Top Global Matches:** file_cluster_17: 14.396, file_cluster_13: 14.6, file_cluster_8: 14.736
- **Magnitude:** 78.4 | **LOC:** 139 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (33.1526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 9.4 | O(N^2) | DB: 2)
    * *Intent:* /**
  * `toString` (Impact: 5.8 | O(2^N) | DB: 2)
    * *Intent:* /** * @param {GraphVertex} vertex
  * `findEdge` (Impact: 4.7 | O(N^1) | DB: 1)
    * *Intent:* /** * @param {GraphEdge} requiredEdge * @returns {boolean}
  * `getNeighbors` (Impact: 3.4 | O(N^1) | DB: 1)
  * `hasNeighbor` (Impact: 3.2 | O(N^1) | DB: 1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 25`, `args: 19`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 8`, `doc: 34`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.033871
  * `Imports (Out-Degree: 1):` LinkedList
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/data-structures/lru-cache/LRUCacheOnMap.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.041 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.586 IQR)
- **Top Global Matches:** file_cluster_8: 15.041, file_cluster_7: 15.072, file_cluster_13: 15.167
- **Magnitude:** 78.38 | **LOC:** 54 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (38.1271%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `set` (Impact: 21.3 | O(2^N) | DB: 9)
  * `get` (Impact: 6.0 | O(2^N) | DB: 6)
  * `constructor` (Impact: 1.6 | O(N^1) | DB: 2)
    * *Intent:* /* eslint-disable no-restricted-syntax, no-unreachable-loop */ /** * Implementation of the LRU (Leas...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 7`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 2`
* *Defense:* `doc: 9`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/bloom-filter/BloomFilter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.992 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.432 IQR)
- **Top Global Matches:** file_cluster_8: 12.992, file_cluster_7: 13.128, file_cluster_1: 13.375
- **Magnitude:** 77.48 | **LOC:** 132 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (31.3777%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mayContain` (Impact: 7.0 | O(N^2) | DB: 3)
    * *Intent:* // Set each hashValue index to true.
  * `createStore` (Impact: 5.2 | O(N^2) | DB: 2)
  * `hash1` (Impact: 3.4 | O(N^1) | DB: 3)
  * `hash3` (Impact: 3.4 | O(N^1) | DB: 3)
  * `hash2` (Impact: 3.3 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 19`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `api: 4`
* *Defense:* `doc: 22`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/trie/TrieNode.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.977 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.923 IQR)
- **Top Global Matches:** file_cluster_13: 13.977, file_cluster_8: 14.141, file_cluster_7: 14.176
- **Magnitude:** 75.4 | **LOC:** 95 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (35.433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toString` (Impact: 8.8 | O(2^N) | DB: 4)
    * *Intent:* /** * @param {string} character * @return {boolean}
  * `removeChild` (Impact: 6.5 | O(N^1) | DB: 3)
  * `addChild` (Impact: 5.8 | O(N^1) | DB: 4)
    * *Intent:* /** * @param {string} character * @return {TrieNode}
  * `constructor` (Impact: 2.0 | O(N^1) | DB: 3)
    * *Intent:* /**
  * `getChild` (Impact: 1.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 12`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 1`, `doc: 22`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.668
  * `Choke Point (Betweenness):` 0.000129 | `Ripple Effect (Closeness):` 0.003629
  * `Imports (Out-Degree: 1):` HashTable
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/algorithms/ml/k-means/kMeans.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.776 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.617 IQR)
- **Top Global Matches:** file_cluster_13: 11.776, file_cluster_8: 11.888, file_cluster_7: 12.186
- **Magnitude:** 74.82 | **LOC:** 86 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (36.7448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `KMeans` (Impact: 47.8 | O(N^3) | DB: 8)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 2`, `doc: 4`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 2):` euclideanDistance, Matrix
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/disjoint-set/DisjointSetAdhoc.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.67 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.333 IQR)
- **Top Global Matches:** file_cluster_17: 15.67, file_cluster_13: 16.259, file_cluster_8: 16.27
- **Magnitude:** 74.36 | **LOC:** 79 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (39.171%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 11.1 | O(N^1) | DB: 10)
    * *Intent:* /** * Initializes the set of specified size. * @param {number} size
  * `find` (Impact: 5.9 | O(2^N) | DB: 5)
    * *Intent:* * The minimalistic (ad hoc) version of a DisjointSet (or a UnionFind) data structure * that doesn't ...
  * `constructor` (Impact: 1.9 | O(N^1) | DB: 2)
    * *Intent:* /** * The minimalistic (ad hoc) version of a DisjointSet (or a UnionFind) data structure * that does...
  * `connected` (Impact: 1.9 | O(N^1) | DB: 2)
    * *Intent:* /** * Finds the root of node `a` * @param {number} a * @returns {number} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 7`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `api: 4`
* *Defense:* `safety: 3`, `doc: 13`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/sorting/quick-sort/QuickSort.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.22 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.825 IQR)
- **Top Global Matches:** file_cluster_13: 13.22, file_cluster_8: 13.321, file_cluster_7: 13.531
- **Magnitude:** 70.24 | **LOC:** 49 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (39.5696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sort` (Impact: 31.7 | O(2^N) | DB: 13)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 3`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.199
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.005161
  * `Imports (Out-Degree: 1):` Sort
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/algorithms/string/z-algorithm/zAlgorithm.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.664 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.132 IQR)
- **Top Global Matches:** file_cluster_8: 12.664, file_cluster_17: 12.671, file_cluster_7: 12.967
- **Magnitude:** 69.4 | **LOC:** 133 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (39.5696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildZArray` (Impact: 50.8 | O(2^N) | DB: 6)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 7`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* None
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.45 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.499 IQR)
- **Top Global Matches:** file_cluster_13: 12.45, file_cluster_8: 12.458, file_cluster_7: 12.739
- **Magnitude:** 68.94 | **LOC:** 72 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (41.0549%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `shortestCommonSupersequence` (Impact: 39.1 | O(N^2) | DB: 9)
    * *Intent:* /** * @param {string[]} set1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 1):` longestCommonSubsequence
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/algorithms/sets/longest-increasing-subsequence/dpLongestIncreasingSubsequence.js` (JAVASCRIPT) | Magnitude: 35.0 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 12, branch: 7, structural_boundaries: 6
- `src/algorithms/sets/knapsack-problem/KnapsackItem.js` (JAVASCRIPT) | Magnitude: 33.8 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 19, indent_spaces: 18, structural_boundaries: 6, api: 6
- `src/algorithms/math/fourier-transform/discreteFourierTransform.js` (JAVASCRIPT) | Magnitude: 29.42 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 12, branch: 7, structural_boundaries: 7
- `src/algorithms/math/square-root/squareRoot.js` (JAVASCRIPT) | Magnitude: 13.96 | Delta: **0.323 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, branch: 5, structural_boundaries: 5, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js` (JAVASCRIPT) | Magnitude: 68.94 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 27, branch: 14, structural_boundaries: 9
- `src/algorithms/ml/knn/kNN.js` (JAVASCRIPT) | Magnitude: 49.08 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, state_mutation: 18, branch: 11, structural_boundaries: 10
- `src/algorithms/sorting/insertion-sort/InsertionSort.js` (JAVASCRIPT) | Magnitude: 30.7 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, state_mutation: 18, structural_boundaries: 7, branch: 4
- `src/data-structures/tree/red-black-tree/RedBlackTree.js` (JAVASCRIPT) | Magnitude: 265.96 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 127, state_mutation: 105, doc: 38, branch: 30
- `src/algorithms/sorting/bubble-sort/BubbleSort.js` (JAVASCRIPT) | Magnitude: 35.74 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 19, structural_boundaries: 9, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/peakvalleyBestTimeToBuySellStocks.js` (JAVASCRIPT) | Magnitude: 27.02 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 9, structural_boundaries: 8, func_start: 4
- `src/algorithms/math/matrix/Matrix.js` (JAVASCRIPT) | Magnitude: 65.4 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, doc: 37, structural_boundaries: 34, func_start: 27
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/accumulatorBestTimeToBuySellStocks.js` (JAVASCRIPT) | Magnitude: 13.3 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, state_mutation: 6, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/algorithms/graph/prim/prim.js` (JAVASCRIPT) | Magnitude: 23.52 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 6, state_mutation: 6, branch: 5
- `src/algorithms/graph/travelling-salesman/bfTravellingSalesman.js` (JAVASCRIPT) | Magnitude: 52.28 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 22, immutability_locks: 18, structural_boundaries: 17
- `src/algorithms/sorting/counting-sort/CountingSort.js` (JAVASCRIPT) | Magnitude: 67.14 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 34, indent_spaces: 34, structural_boundaries: 11, branch: 9
- `src/algorithms/graph/eulerian-path/eulerianPath.js` (JAVASCRIPT) | Magnitude: 21.4 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 6, branch: 5, structural_boundaries: 5
- `src/algorithms/uncategorized/n-queens/nQueens.js` (JAVASCRIPT) | Magnitude: 83.38 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, doc: 15, branch: 11, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/algorithms/image-processing/utils/imageData.js` (JAVASCRIPT) | Magnitude: 7.4 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, immutability_locks: 6, indent_spaces: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/algorithms/string/z-algorithm/zAlgorithm.js` (JAVASCRIPT) | Magnitude: 69.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 27, state_mutation: 18, branch: 8, structural_boundaries: 7
- `src/algorithms/sets/combination-sum/combinationSum.js` (JAVASCRIPT) | Magnitude: 3.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 2, api: 2, branch: 1
- `src/algorithms/sets/power-set/btPowerSet.js` (JAVASCRIPT) | Magnitude: 3.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 2, api: 2, branch: 1
- `src/data-structures/heap/Heap.js` (JAVASCRIPT) | Magnitude: 296.64 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 183, indent_spaces: 139, doc: 60, structural_boundaries: 27
- `src/algorithms/math/binary-floating-point/__tests__/bitsToFloat.test.js` (JAVASCRIPT) | Magnitude: 21.28 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, args: 9, func_start: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/data-structures/graph/Graph.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 117.44
- `src/data-structures/graph/GraphVertex.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 78.4

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/data-structures/linked-list/LinkedList.js` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 100.0%)
- `src/data-structures/graph/GraphVertex.js` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 99.9999%)
- `src/data-structures/hash-table/HashTable.js` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 99.9995%)
- `src/data-structures/trie/TrieNode.js` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 100.0%)
- `src/data-structures/tree/binary-search-tree/BinarySearchTree.js` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.9996%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/data-structures/linked-list/LinkedList.js` -> **Severity: 3.482** (Embedded: 0.0367 * Error Risk: 94.9115%)
- `src/data-structures/graph/GraphEdge.js` -> **Severity: 1.972** (Embedded: 0.0323 * Error Risk: 61.1259%)
- `src/utils/comparator/Comparator.js` -> **Severity: 1.831** (Embedded: 0.0661 * Error Risk: 27.7119%)
- `src/data-structures/graph/Graph.js` -> **Severity: 1.666** (Embedded: 0.0323 * Error Risk: 51.6333%)
- `src/data-structures/linked-list/LinkedListNode.js` -> **Severity: 1.03** (Embedded: 0.0276 * Error Risk: 37.3498%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/algorithms/sorting/Sort.js` -> **Severity: 1158.684** (Blast Radius: 17.094 * Doc Risk: 67.7831%)
- `src/algorithms/sorting/SortTester.js` -> **Severity: 637.688** (Blast Radius: 6.385 * Doc Risk: 99.8729%)
- `src/utils/comparator/Comparator.js` -> **Severity: 558.156** (Blast Radius: 46.824 * Doc Risk: 11.9203%)
- `src/data-structures/linked-list/LinkedList.js` -> **Severity: 305.493** (Blast Radius: 25.628 * Doc Risk: 11.9203%)
- `src/data-structures/graph/GraphVertex.js` -> **Severity: 132.547** (Blast Radius: 7.413 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
