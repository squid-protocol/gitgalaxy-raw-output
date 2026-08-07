# ARCHITECTURAL_BRIEF: javascript-algorithms
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/javascript-algorithms` |
| **Timestamp** | `2026-08-07T04:26:22.102851+00:00` |
| **Scan Duration** | `1.19s` |
| **Git Branch** | `master` |
| **Git Commit** | `115e42816808484f76de4e6703caa8280e03ed54` |
| **Git Remote** | `https://github.com/trekhleb/javascript-algorithms.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 359 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 83.7 | 15.6 | 7.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 35.6 | 27.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.4 | 0.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.9 | 3.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 90.6 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 89.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 78.0 | 1.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.9 | 5.5 | 2.4 | 0.0 |
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

- `getPhase` (@ `src/algorithms/math/complex-number/ComplexNumber.js`) -> Impact: **51.5** | LOC: 29
- `describe` (@ `src/data-structures/tree/avl-tree/__test__/AvlTRee.test.js`) -> Impact: **32.6** | LOC: 301
- `kNN` (@ `src/algorithms/ml/knn/kNN.js`) -> Impact: **29.3** | LOC: 48
  * *Intent:* /** * Classifies the point in space based on k-nearest neighbors algorithm. * * @param {number[][]} dataSet - array of data points, i.e. [[0, 1], [3, ...
- `isSafe` (@ `src/algorithms/uncategorized/n-queens/nQueens.js`) -> Impact: **27.6** | LOC: 72
  * *Intent:* /**
- `balance` (@ `src/data-structures/tree/red-black-tree/RedBlackTree.js`) -> Impact: **27.1** | LOC: 62
  * *Intent:* /** * @param {*} value * @return {boolean}
- `solveZeroOneKnapsackProblem` (@ `src/algorithms/sets/knapsack-problem/Knapsack.js`) -> Impact: **27.0** | LOC: 87
  * *Intent:* /** * @var KnapsackItem itemA * @var KnapsackItem itemB */
- `longestCommonSubsequence` (@ `src/algorithms/sets/longest-common-subsequence/longestCommonSubsequence.js`) -> Impact: **27.0** | LOC: 55
  * *Intent:* /**
- `describe` (@ `src/algorithms/math/matrix/__tests__/Matrix.test.js`) -> Impact: **26.9** | LOC: 453
- `shortestCommonSupersequence` (@ `src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js`) -> Impact: **26.9** | LOC: 54
  * *Intent:* /** * @param {string[]} set1
- `describe` (@ `src/data-structures/graph/__test__/Graph.test.js`) -> Impact: **25.9** | LOC: 397

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 27 | 5167.18 | 0.92% | 0.0% |
| `src/data-structures/heap` | 14 | 625.7 | 15.88% | 1.02% |
| `src/data-structures/linked-list` | 12 | 305.64 | 3.45% | 0.0% |
| `src/algorithms/sets/knapsack-problem` | 3 | 247.28 | 22.64% | 32.85% |
| `src/data-structures/heap/__test__` | 5 | 245.22 | 9.88% | 0.0% |
| `src/data-structures/doubly-linked-list` | 10 | 237.1 | 4.97% | 0.0% |
| `src/data-structures/graph` | 9 | 228.86 | 13.4% | 0.0% |
| `src/data-structures/lru-cache` | 4 | 209.74 | 17.72% | 24.66% |
| `src/data-structures/disjoint-set` | 7 | 205.18 | 15.41% | 0.0% |
| `src/data-structures/graph/__test__` | 3 | 203.84 | 4.14% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/algorithms/math/is-power-of-two/isPowerOfTwoBitwise.js` -> **100.0%** Exposure
- `src/algorithms/math/matrix/Matrix.js` -> **100.0%** Exposure
- `src/algorithms/tree/depth-first-search/depthFirstSearch.js` -> **100.0%** Exposure
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/accumulatorBestTimeToBuySellStocks.js` -> **100.0%** Exposure
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/dpBestTimeToBuySellStocks.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/algorithms/cryptography/polynomial-hash/PolynomialHash.js` -> **100.0%** Exposure
- `src/algorithms/linked-list/traversal/traversal.js` -> **100.0%** Exposure
- `src/algorithms/math/bits/bitLength.js` -> **100.0%** Exposure
- `src/algorithms/math/bits/countSetBits.js` -> **100.0%** Exposure
- `src/algorithms/math/complex-number/ComplexNumber.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/data-structures/linked-list/__test__/LinkedList.test.js` -> **1** Orphaned Functions | **21** Duplicates
- `src/data-structures/graph/__test__/Graph.test.js` -> **1** Orphaned Functions | **19** Duplicates
- `src/algorithms/math/complex-number/__test__/ComplexNumber.test.js` -> **1** Orphaned Functions | **18** Duplicates
- `src/data-structures/doubly-linked-list/__test__/DoublyLinkedList.test.js` -> **1** Orphaned Functions | **17** Duplicates
- `src/algorithms/math/matrix/__tests__/Matrix.test.js` -> **1** Orphaned Functions | **14** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/algorithms/sorting/SortTester.js` (JAVASCRIPT) -> Cumulative Risk: **525.61**
- **Archetype:** `file_cluster_8` (Distance: 12.071 IQR)
- **Magnitude:** 67.0 | **LOC:** 73 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9837%), Tech Debt (99.8729%), Documentation (98.9013%)
- **Heaviest Functions:** `testSortWithCustomComparator` (Impact: 6.1), `testSortStability` (Impact: 5.9), `compareCallback` (Impact: 5.5)

### 2. `src/algorithms/sets/knapsack-problem/Knapsack.js` (JAVASCRIPT) -> Cumulative Risk: **460.96**
- **Archetype:** `file_cluster_17` (Distance: 14.132 IQR)
- **Magnitude:** 212.08 | **LOC:** 196 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.5553%), Safety Score (98.3282%)
- **Heaviest Functions:** `solveZeroOneKnapsackProblem` (Impact: 27.0), `solveUnboundedKnapsackProblem` (Impact: 6.8), `compareCallback` (Impact: 5.5)

### 3. `src/data-structures/lru-cache/LRUCache.js` (JAVASCRIPT) -> Cumulative Risk: **444.97**
- **Archetype:** `file_cluster_8` (Distance: 14.729 IQR)
- **Magnitude:** 145.92 | **LOC:** 154 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8968%), Tech Debt (98.6482%)
- **Heaviest Functions:** `evict` (Impact: 8.7), `append` (Impact: 6.9), `set` (Impact: 5.7)

### 4. `src/data-structures/graph/GraphEdge.js` (JAVASCRIPT) -> Cumulative Risk: **444.64**
- **Archetype:** `file_cluster_8` (Distance: 13.466 IQR)
- **Magnitude:** 36.82 | **LOC:** 46 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.6869%), Stability (78.0478%)
- **Heaviest Functions:** `getKey` (Impact: 3.4), `constructor` (Impact: 2.5), `reverse` (Impact: 1.8)

### 5. `src/data-structures/graph/Graph.js` (JAVASCRIPT) -> Cumulative Risk: **440.67**
- **Archetype:** `file_cluster_8` (Distance: 13.401 IQR)
- **Magnitude:** 100.54 | **LOC:** 204 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (90.2173%), Stability (78.0472%)
- **Heaviest Functions:** `addEdge` (Impact: 10.1), `findEdge` (Impact: 3.9), `addVertex` (Impact: 3.4)

### 6. `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/peakvalleyBestTimeToBuySellStocks.js` (JAVASCRIPT) -> Cumulative Risk: **436.56**
- **Archetype:** `file_cluster_15` (Distance: 12.827 IQR)
- **Magnitude:** 22.42 | **LOC:** 36 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (81.9308%)
- **Heaviest Functions:** `visit` (Impact: 7.9), `visit` (Impact: 2.4), `visit` (Impact: 1.8)

### 7. `src/algorithms/sorting/quick-sort/QuickSortInPlace.js` (JAVASCRIPT) -> Cumulative Risk: **430.35**
- **Archetype:** `file_cluster_8` (Distance: 12.487 IQR)
- **Magnitude:** 44.62 | **LOC:** 79 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9997%), State Flux (99.9997%), Safety Score (81.0108%)
- **Heaviest Functions:** `sort` (Impact: 14.7), `partitionArray` (Impact: 6.6), `swap` (Impact: 2.6)

### 8. `src/algorithms/math/matrix/Matrix.js` (JAVASCRIPT) -> Cumulative Risk: **414.29**
- **Archetype:** `file_cluster_15` (Distance: 12.787 IQR)
- **Magnitude:** 87.6 | **LOC:** 310 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.7494%), Safety Score (69.4594%)
- **Heaviest Functions:** `walk` (Impact: 7.8), `recWalk` (Impact: 7.5), `t` (Impact: 5.7)

### 9. `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` (JAVASCRIPT) -> Cumulative Risk: **411.85**
- **Archetype:** `file_cluster_13` (Distance: 11.57 IQR)
- **Magnitude:** 36.96 | **LOC:** 86 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (90.5729%), Tech Debt (90.1764%), Safety Score (46.6352%)
- **Heaviest Functions:** `pixelsDiff` (Impact: 11.1), `describe` (Impact: 3.1), `it` (Impact: 3.0)

### 10. `src/algorithms/uncategorized/hanoi-tower/hanoiTower.js` (JAVASCRIPT) -> Cumulative Risk: **409.98**
- **Archetype:** `file_cluster_8` (Distance: 10.98 IQR)
- **Magnitude:** 26.88 | **LOC:** 85 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.8051%), Safety Score (66.1443%)
- **Heaviest Functions:** `moveCallback` (Impact: 3.0), `hanoiTower` (Impact: 1.8), `hanoiTowerRecursive` (Impact: 1.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Magnitude:** 271.84 | **LOC:** 287 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.8748%), Tech Debt (14.2366%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 15.8)
    * *Intent:* /**
  * `heapifyDown` (Impact: 15.4)
  * `heapifyUp` (Impact: 6.4)
  * `find` (Impact: 5.7)
  * `poll` (Impact: 5.1)
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
- **Magnitude:** 258.42 | **LOC:** 273 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3567%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `insert` (Impact: 20.5)
    * *Intent:* /** * @param {*} value * @return {LinkedList}
  * `delete` (Impact: 14.5)
  * `deleteTail` (Impact: 8.4)
  * `deleteHead` (Impact: 6.5)
  * `reverse` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 34`, `args: 13`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 179`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 5`, `doc: 33`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.628
  * `Choke Point (Betweenness):` 0.000258 | `Ripple Effect (Closeness):` 0.036684
  * `Imports (Out-Degree: 2):` LinkedListNode, Comparator
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/knapsack-problem/Knapsack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.132 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.9 IQR)
- **Top Global Matches:** file_cluster_17: 14.132, file_cluster_11: 14.319, file_cluster_13: 14.324
- **Magnitude:** 212.08 | **LOC:** 196 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.6251%), Tech Debt (98.5553%)
**Top Internal Functions/Classes:**
  * `solveZeroOneKnapsackProblem` (Impact: 27.0)
    * *Intent:* /** * @var KnapsackItem itemA * @var KnapsackItem itemB */
  * `solveUnboundedKnapsackProblem` (Impact: 6.8)
  * `compareCallback` (Impact: 5.5)
  * `compareCallback` (Impact: 5.5)
  * `compareCallback` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 27`, `args: 14`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 135`, `dead_code: 1`, `duplicate_logic: 3`
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
- **Magnitude:** 202.3 | **LOC:** 264 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.7421%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `delete` (Impact: 16.6)
    * *Intent:* /**
  * `deleteHead` (Impact: 6.5)
  * `deleteTail` (Impact: 5.4)
  * `reverse` (Impact: 4.1)
  * `prepend` (Impact: 3.4)
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

### `src/data-structures/tree/BinaryTreeNode.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.199 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 2.971 IQR)
- **Top Global Matches:** file_cluster_13: 14.199, file_cluster_8: 14.242, file_cluster_7: 14.304
- **Magnitude:** 183.06 | **LOC:** 220 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.1032%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `replaceChild` (Impact: 13.0)
  * `removeChild` (Impact: 7.7)
    * *Intent:* /** * @param {*} value * @return {BinaryTreeNode}
  * `traverseInOrder` (Impact: 5.1)
  * `setLeft` (Impact: 5.0)
  * `setRight` (Impact: 5.0)
    * *Intent:* // Check if grand-parent has two children.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 23`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 120`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.575
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.007806
  * `Imports (Out-Degree: 2):` HashTable, Comparator
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/red-black-tree/RedBlackTree.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.899 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.655 IQR)
- **Top Global Matches:** file_cluster_13: 13.899, file_cluster_8: 13.919, file_cluster_7: 13.998
- **Magnitude:** 179.56 | **LOC:** 324 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.3056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `balance` (Impact: 27.1)
    * *Intent:* /** * @param {*} value * @return {boolean}
  * `leftLeftRotation` (Impact: 10.3)
  * `rightRightRotation` (Impact: 10.3)
  * `insert` (Impact: 5.1)
    * *Intent:* /**
  * `isNodeColored` (Impact: 3.0)
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

### `src/data-structures/heap/MinHeapAdhoc.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.217 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.007 IQR)
- **Top Global Matches:** file_cluster_8: 13.217, file_cluster_17: 13.503, file_cluster_13: 13.605
- **Magnitude:** 167.28 | **LOC:** 118 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.7496%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `heapifyDown` (Impact: 17.2)
  * `heapifyUp` (Impact: 6.1)
  * `poll` (Impact: 3.2)
  * `constructor` (Impact: 2.2)
  * `swap` (Impact: 2.0)
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
- **Magnitude:** 167.14 | **LOC:** 116 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.7381%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `heapifyDown` (Impact: 17.1)
  * `heapifyUp` (Impact: 6.1)
  * `poll` (Impact: 3.2)
  * `constructor` (Impact: 2.2)
  * `swap` (Impact: 2.0)
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
- **Risk Profile:** Cognitive Load (32.76%), Tech Debt (98.6482%)
**Top Internal Functions/Classes:**
  * `evict` (Impact: 8.7)
    * *Intent:* /** * Promotes the node to the end of the linked list. * It means that the node is most frequently u...
  * `append` (Impact: 6.9)
  * `set` (Impact: 5.7)
    * *Intent:* /** * Creates a cache instance of a specific capacity.
  * `get` (Impact: 3.1)
    * *Intent:* /** * Implementation of the LRU (Least Recently Used) Cache * based on the HashMap and Doubly Linked...
  * `constructor` (Impact: 2.5)
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

### `src/data-structures/tree/binary-search-tree/BinarySearchTreeNode.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.724 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.425 IQR)
- **Top Global Matches:** file_cluster_13: 13.724, file_cluster_8: 13.835, file_cluster_17: 13.85
- **Magnitude:** 145.92 | **LOC:** 152 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.5696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 23.9)
  * `insert` (Impact: 10.1)
  * `find` (Impact: 9.4)
  * `findMin` (Impact: 3.2)
  * `constructor` (Impact: 2.1)
    * *Intent:* /**
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

### `src/algorithms/math/complex-number/ComplexNumber.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.029 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.345 IQR)
- **Top Global Matches:** file_cluster_13: 15.029, file_cluster_8: 15.23, file_cluster_7: 15.269
- **Magnitude:** 142.04 | **LOC:** 161 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.9468%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getPhase` (Impact: 51.5)
  * `toComplexNumber` (Impact: 3.2)
    * *Intent:* /** * @param {ComplexNumber|number} number
  * `getPolarForm` (Impact: 2.3)
  * `multiply` (Impact: 2.2)
    * *Intent:* // Make sure we're dealing with complex number.
  * `add` (Impact: 1.9)
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

### `src/data-structures/linked-list/__test__/LinkedList.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.827 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 6.373 IQR)
- **Top Global Matches:** file_cluster_8: 9.827, file_cluster_17: 10.25, file_cluster_7: 10.587
- **Magnitude:** 100.66 | **LOC:** 283 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2954%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 20.9)
  * `it` (Impact: 6.4)
  * `comparatorFunction` (Impact: 5.5)
  * `it` (Impact: 4.1)
  * `it` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 36`, `args: 22`, `func_start: 97`
* *Risk/State:* `state_mutation: 13`, `duplicate_logic: 21`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 3`, `test: 94`, `immutability_locks: 29`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LinkedList
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/graph/Graph.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.401 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.612 IQR)
- **Top Global Matches:** file_cluster_8: 13.401, file_cluster_7: 13.485, file_cluster_17: 13.53
- **Magnitude:** 100.54 | **LOC:** 204 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.5331%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addEdge` (Impact: 10.1)
  * `findEdge` (Impact: 3.9)
  * `addVertex` (Impact: 3.4)
  * `getAdjacencyMatrix` (Impact: 2.4)
  * `constructor` (Impact: 2.2)
    * *Intent:* /**
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

### `src/data-structures/graph/__test__/Graph.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.379 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 6.851 IQR)
- **Top Global Matches:** file_cluster_8: 8.379, file_cluster_7: 9.22, file_cluster_1: 9.45
- **Magnitude:** 98.94 | **LOC:** 402 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (2.8786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 25.9)
  * `it` (Impact: 6.2)
  * `it` (Impact: 4.8)
  * `it` (Impact: 4.8)
  * `it` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 26`, `args: 21`, `func_start: 90`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 19`, `orphaned_logic: 1`
* *Architecture:* `import: 3`
* *Defense:* `test: 87`, `immutability_locks: 122`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Graph, GraphVertex, GraphEdge
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/heap/__test__/MinHeap.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.27 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.546 IQR)
- **Top Global Matches:** file_cluster_8: 11.27, file_cluster_13: 11.733, file_cluster_17: 11.734
- **Magnitude:** 93.06 | **LOC:** 195 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.9291%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 14.2)
  * `it` (Impact: 6.2)
  * `expect` (Impact: 4.7)
  * `it` (Impact: 3.4)
  * `it` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 15`, `args: 11`, `func_start: 71`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 43`, `duplicate_logic: 9`, `orphaned_logic: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `test: 71`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MinHeap, Comparator
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/tree/avl-tree/__test__/AvlTRee.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.633 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.214 IQR)
- **Top Global Matches:** file_cluster_8: 8.633, file_cluster_7: 9.495, file_cluster_1: 9.691
- **Magnitude:** 91.32 | **LOC:** 304 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.3797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 32.6)
  * `it` (Impact: 5.6)
  * `it` (Impact: 4.7)
  * `it` (Impact: 4.7)
  * `it` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `args: 14`, `func_start: 114`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 13`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `test: 114`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AvlTree
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algorithms/math/matrix/Matrix.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_15` (Drift: 12.787 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.291 IQR)
- **Top Global Matches:** file_cluster_15: 12.787, file_cluster_8: 12.838, file_cluster_7: 12.933
- **Magnitude:** 87.6 | **LOC:** 310 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.4999%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `walk` (Impact: 7.8)
  * `recWalk` (Impact: 7.5)
  * `t` (Impact: 5.7)
    * *Intent:* /** * @typedef {number} Cell * @typedef {Cell[][]|Cell[][][]} Matrix
  * `updateCellAtIndex` (Impact: 4.5)
  * `getCellAtIndex` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 34`, `args: 14`, `func_start: 27`
* *Risk/State:* `state_mutation: 24`, `duplicate_logic: 7`
* *Architecture:* `api: 8`
* *Defense:* `safety: 1`, `doc: 37`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.345
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00871
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/algorithms/math/matrix/__tests__/Matrix.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.807 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.713 IQR)
- **Top Global Matches:** file_cluster_8: 7.807, file_cluster_7: 8.783, file_cluster_1: 8.887
- **Magnitude:** 86.42 | **LOC:** 456 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.7271%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 26.9)
  * `it` (Impact: 6.0)
  * `it` (Impact: 6.0)
  * `it` (Impact: 4.2)
  * `it` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 35`, `args: 32`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `duplicate_logic: 14`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `test: 86`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Matrix
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/graph/GraphVertex.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.403 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.102 IQR)
- **Top Global Matches:** file_cluster_17: 14.403, file_cluster_13: 14.61, file_cluster_8: 14.733
- **Magnitude:** 85.5 | **LOC:** 139 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.1526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 6.6)
    * *Intent:* /**
  * `edgeComparator` (Impact: 5.5)
  * `findEdge` (Impact: 4.7)
    * *Intent:* /** * @param {GraphEdge} requiredEdge * @returns {boolean}
  * `neighborsConverter` (Impact: 3.6)
    * *Intent:* /** * @param {GraphEdge} edge
  * `edgeFinder` (Impact: 3.6)
    * *Intent:* /** * @param {GraphEdge} requiredEdge * @returns {boolean} */
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

### `src/data-structures/tree/binary-search-tree/__test__/BinarySearchTreeNode.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.586 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 6.059 IQR)
- **Top Global Matches:** file_cluster_8: 8.586, file_cluster_7: 9.477, file_cluster_1: 9.672
- **Magnitude:** 82.56 | **LOC:** 256 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.3632%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 23.0)
  * `it` (Impact: 10.2)
  * `nodeValueComparatorCallback` (Impact: 9.2)
  * `it` (Impact: 3.9)
  * `it` (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 22`, `args: 20`, `func_start: 86`
* *Risk/State:* `safety_bypasses: 3`, `duplicate_logic: 14`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 1`, `test: 84`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BinarySearchTreeNode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/doubly-linked-list/__test__/DoublyLinkedList.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.519 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 6.015 IQR)
- **Top Global Matches:** file_cluster_8: 9.519, file_cluster_17: 10.105, file_cluster_7: 10.323
- **Magnitude:** 82.36 | **LOC:** 281 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.4416%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 19.1)
  * `it` (Impact: 6.4)
  * `comparatorFunction` (Impact: 5.5)
  * `it` (Impact: 4.2)
  * `it` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 30`, `args: 17`, `func_start: 113`
* *Risk/State:* `state_mutation: 10`, `duplicate_logic: 17`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 3`, `test: 111`, `immutability_locks: 25`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DoublyLinkedList
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/heap/__test__/MaxHeap.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.163 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.586 IQR)
- **Top Global Matches:** file_cluster_8: 11.163, file_cluster_17: 11.602, file_cluster_13: 11.611
- **Magnitude:** 80.32 | **LOC:** 173 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 13.6)
  * `it` (Impact: 6.2)
  * `expect` (Impact: 4.7)
  * `it` (Impact: 3.4)
  * `it` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `args: 10`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 34`, `duplicate_logic: 8`, `orphaned_logic: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `test: 67`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MaxHeap, Comparator
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/tree/segment-tree/SegmentTree.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.53 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.896 IQR)
- **Top Global Matches:** file_cluster_8: 12.53, file_cluster_7: 12.654, file_cluster_13: 12.707
- **Magnitude:** 79.68 | **LOC:** 169 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.5896%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rangeQueryRecursive` (Impact: 13.8)
    * *Intent:* /**
  * `initSegmentTree` (Impact: 5.2)
  * `buildTreeRecursively` (Impact: 5.2)
    * *Intent:* /** * Build segment tree.
  * `constructor` (Impact: 2.5)
    * *Intent:* /**
  * `rangeQuery` (Impact: 2.4)
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

### `src/data-structures/bloom-filter/BloomFilter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.99 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.432 IQR)
- **Top Global Matches:** file_cluster_8: 12.99, file_cluster_7: 13.126, file_cluster_1: 13.373
- **Magnitude:** 77.18 | **LOC:** 132 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.3777%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mayContain` (Impact: 4.9)
    * *Intent:* // Set each hashValue index to true.
  * `createStore` (Impact: 3.8)
  * `hash1` (Impact: 3.4)
  * `hash3` (Impact: 3.4)
  * `hash2` (Impact: 3.3)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/algorithms/sets/longest-increasing-subsequence/dpLongestIncreasingSubsequence.js` (JAVASCRIPT) | Magnitude: 28.9 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 12, branch: 7, structural_boundaries: 6
- `src/algorithms/sets/knapsack-problem/KnapsackItem.js` (JAVASCRIPT) | Magnitude: 33.8 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 19, indent_spaces: 18, structural_boundaries: 6, api: 6
- `src/algorithms/math/fourier-transform/discreteFourierTransform.js` (JAVASCRIPT) | Magnitude: 25.12 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 12, branch: 7, structural_boundaries: 7
- `src/algorithms/math/square-root/squareRoot.js` (JAVASCRIPT) | Magnitude: 13.96 | Delta: **0.323 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, branch: 5, structural_boundaries: 5, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js` (JAVASCRIPT) | Magnitude: 56.74 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 27, branch: 14, structural_boundaries: 9
- `src/algorithms/ml/knn/kNN.js` (JAVASCRIPT) | Magnitude: 49.08 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, state_mutation: 18, branch: 11, structural_boundaries: 10
- `src/algorithms/sorting/insertion-sort/InsertionSort.js` (JAVASCRIPT) | Magnitude: 27.9 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, state_mutation: 18, structural_boundaries: 7, branch: 4
- `src/data-structures/tree/red-black-tree/RedBlackTree.js` (JAVASCRIPT) | Magnitude: 179.56 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 127, state_mutation: 105, doc: 38, branch: 30
- `src/algorithms/sorting/bubble-sort/BubbleSort.js` (JAVASCRIPT) | Magnitude: 32.24 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 19, structural_boundaries: 9, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/peakvalleyBestTimeToBuySellStocks.js` (JAVASCRIPT) | Magnitude: 22.42 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 9, structural_boundaries: 8, func_start: 4
- `src/algorithms/math/matrix/Matrix.js` (JAVASCRIPT) | Magnitude: 87.6 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, doc: 37, structural_boundaries: 34, func_start: 27
- `src/algorithms/uncategorized/best-time-to-buy-sell-stocks/accumulatorBestTimeToBuySellStocks.js` (JAVASCRIPT) | Magnitude: 11.4 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, state_mutation: 6, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/algorithms/graph/prim/prim.js` (JAVASCRIPT) | Magnitude: 19.22 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 6, state_mutation: 6, branch: 5
- `src/algorithms/graph/travelling-salesman/bfTravellingSalesman.js` (JAVASCRIPT) | Magnitude: 46.28 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 22, immutability_locks: 18, structural_boundaries: 17
- `src/algorithms/sorting/counting-sort/CountingSort.js` (JAVASCRIPT) | Magnitude: 58.14 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 34, indent_spaces: 34, structural_boundaries: 11, branch: 9
- `src/algorithms/graph/eulerian-path/eulerianPath.js` (JAVASCRIPT) | Magnitude: 21.4 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 6, branch: 5, structural_boundaries: 5
- `src/algorithms/uncategorized/n-queens/nQueens.js` (JAVASCRIPT) | Magnitude: 54.58 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, doc: 15, branch: 11, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/algorithms/image-processing/utils/imageData.js` (JAVASCRIPT) | Magnitude: 7.4 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, immutability_locks: 6, indent_spaces: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/algorithms/math/binary-floating-point/__tests__/bitsToFloat.test.js` (JAVASCRIPT) | Magnitude: 32.68 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, args: 9, func_start: 9
- `src/algorithms/string/z-algorithm/zAlgorithm.js` (JAVASCRIPT) | Magnitude: 38.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 27, state_mutation: 18, branch: 8, structural_boundaries: 7
- `src/algorithms/sets/combination-sum/combinationSum.js` (JAVASCRIPT) | Magnitude: 3.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 2, api: 2, branch: 1
- `src/algorithms/sets/power-set/btPowerSet.js` (JAVASCRIPT) | Magnitude: 3.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 2, api: 2, branch: 1
- `src/data-structures/heap/Heap.js` (JAVASCRIPT) | Magnitude: 271.84 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 183, indent_spaces: 139, doc: 60, structural_boundaries: 27

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/data-structures/graph/Graph.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 100.54
- `src/algorithms/math/matrix/__tests__/Matrix.test.js` -> **trekhleb** (100.0% isolated ownership) | Magnitude: 86.42
- `src/data-structures/graph/GraphVertex.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 85.5
- `src/data-structures/tree/red-black-tree/__test__/RedBlackTree.test.js` -> **trekhleb** (100.0% isolated ownership) | Magnitude: 75.98
- `src/data-structures/graph/__test__/GraphVertex.test.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 70.1

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

- `src/utils/comparator/Comparator.js` -> **Severity: 5.182** (Embedded: 0.0661 * Error Risk: 78.435%)
- `src/data-structures/linked-list/LinkedList.js` -> **Severity: 3.62** (Embedded: 0.0367 * Error Risk: 98.6884%)
- `src/data-structures/graph/GraphEdge.js` -> **Severity: 2.99** (Embedded: 0.0323 * Error Risk: 92.6869%)
- `src/data-structures/graph/Graph.js` -> **Severity: 2.91** (Embedded: 0.0323 * Error Risk: 90.2173%)
- `src/data-structures/linked-list/LinkedListNode.js` -> **Severity: 2.387** (Embedded: 0.0276 * Error Risk: 86.5538%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/algorithms/sorting/SortTester.js` -> **Severity: 631.485** (Blast Radius: 6.385 * Doc Risk: 98.9013%)
- `src/utils/comparator/Comparator.js` -> **Severity: 558.156** (Blast Radius: 46.824 * Doc Risk: 11.9203%)
- `src/algorithms/sorting/Sort.js` -> **Severity: 552.396** (Blast Radius: 17.094 * Doc Risk: 32.3152%)
- `src/data-structures/linked-list/LinkedList.js` -> **Severity: 305.493** (Blast Radius: 25.628 * Doc Risk: 11.9203%)
- `src/data-structures/graph/GraphVertex.js` -> **Severity: 132.547** (Blast Radius: 7.413 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
