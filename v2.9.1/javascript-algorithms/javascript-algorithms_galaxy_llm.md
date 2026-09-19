# ARCHITECTURAL_BRIEF: javascript-algorithms
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/trekhleb/javascript-algorithms.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 621 analyzed artifact(s), 15318 LOC.
- **Load-bearing artifact:** `src/algorithms/graph/dijkstra/dijkstra.js` -- 30 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `README.he-IL.md` -- pulls in 128 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 676 |
| Analyzed Artifacts (Scanned) | 621 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 55 |
| Total LOC | 15318 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 91.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7985 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.2233 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7579 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 111 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 359 | 15293 | 57.8% |
| MARKDOWN | 258 | 0 | 41.5% |
| JSON | 2 | 24 | 0.3% |
| PLAINTEXT | 2 | 1 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `5.064`
> **Composition Archetype:** `Small Flat Repo (2)` (z +5.06; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Declarative / Non-Code 22%, Callbacks & Closures Files 7%, Compute Cores Files 6%, Large Core Modules (2) 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 361 | 58.1% |
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.7 | 12.2 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.5 | 39.1 | 41.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 88.1 | 1.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 0.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 90.2 | 14.9 | 14.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 88.1 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.6 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 78.0 | 1.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7 | 6 | 0 | `src/data-structures/trie/Trie.js` |
| cleanup | 0 | 0 | 0 | - |
| guards | 245 | 114 | 1 | `src/algorithms/math/matrix/Matrix.js` |
| danger | 158 | 76 | 1 | `src/algorithms/math/matrix/__tests__/Matrix.test.js` |
| concurrency | 4 | 1 | 0 | `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` |
| connectivity | 421 | 182 | 2 | `src/algorithms/math/matrix/Matrix.js` |
| io | 3 | 1 | 0 | `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 8 | 3 | 0 | `src/algorithms/cryptography/caesar-cipher/caesarCipher.js` |
| events | 70 | 22 | 0 | `src/algorithms/math/liu-hui/__test__/liuHui.test.js` |
| tests | 4025 | 179 | 19 | `src/data-structures/tree/red-black-tree/__test__/RedBlackTree.test.js` |
| docs | 532 | 175 | 2 | `src/data-structures/heap/Heap.js` |
| debt | 9 | 7 | 0 | `src/algorithms/cryptography/hill-cipher/hillCipher.js` |
| mutation | 4269 | 263 | 20 | `src/data-structures/graph/__test__/Graph.test.js` |
| dead_code | 43 | 36 | 0 | `src/algorithms/ml/knn/__test__/knn.test.js` |
| credential | 0 | 0 | 0 | - |
| threat | 2 | 2 | 0 | `src/data-structures/hash-table/HashTable.js` |
| ml_ai | 36 | 9 | 0 | `src/algorithms/math/bits/__test__/multiply.test.js` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` (Hits: 3)
- `.babelrc` (Hits: 0)
- `.eslintrc` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **dijkstra.js** (`src/algorithms/graph/dijkstra/dijkstra.js`) — 30 inbound connections
2. **factorial.js** (`src/algorithms/math/factorial/factorial.js`) — 21 inbound connections
3. **GraphVertex.js** (`src/data-structures/graph/GraphVertex.js`) — 21 inbound connections
4. **kruskal.js** (`src/algorithms/graph/kruskal/kruskal.js`) — 20 inbound connections
5. **prim.js** (`src/algorithms/graph/prim/prim.js`) — 20 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.he-IL.md** (`README.he-IL.md`) — 128 outbound dependencies
2. **README.md** (`README.md`) — 128 outbound dependencies
3. **README.uz-UZ.md** (`README.uz-UZ.md`) — 127 outbound dependencies
4. **README.ru-RU.md** (`README.ru-RU.md`) — 123 outbound dependencies
5. **README.de-DE.md** (`README.de-DE.md`) — 120 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `regularExpressionMatching` **(Many-Argument Workhorses)** (@ `src/algorithms/string/regular-expression-matching/regularExpressionMatching.js`) -> Impact: **37.4** | LOC: 125
  * *Intent:* /** * Dynamic programming approach. * */
- `getPhase` **(Defensive Guards)** (@ `src/algorithms/math/complex-number/ComplexNumber.js`) -> Impact: **36.8** | LOC: 29
  * *Intent:* /** */
- `shortestCommonSupersequence` **(Many-Argument Workhorses)** (@ `src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js`) -> Impact: **30.9** | LOC: 63
  * *Intent:* /** */
- `balance` **(Compute Cores)** (@ `src/data-structures/tree/red-black-tree/RedBlackTree.js`) -> Impact: **30.4** | LOC: 71
  * *Intent:* /** */
- `kNN` **(Many-Argument Workhorses)** (@ `src/algorithms/ml/knn/kNN.js`) -> Impact: **27.0** | LOC: 48
- `longestCommonSubsequence` **(Defensive Guards)** (@ `src/algorithms/sets/longest-common-subsequence/longestCommonSubsequence.js`) -> Impact: **27.0** | LOC: 55
  * *Intent:* /** */
- `findLowEnergySeam` **(Many-Argument Workhorses)** (@ `src/algorithms/image-processing/seam-carving/resizeImageWidth.js`) -> Impact: **26.9** | LOC: 87
  * *Intent:* /** * Finds the seam (the sequence of pixels from top to bottom) that has the * lowest resulting energy using the Dynamic Programming approach. */
- `remove` **(Compute Cores)** (@ `src/data-structures/tree/binary-search-tree/BinarySearchTreeNode.js`) -> Impact: **23.7** | LOC: 50
  * *Intent:* /** */
- `eulerianPath` **(Compute Cores)** (@ `src/algorithms/graph/eulerian-path/eulerianPath.js`) -> Impact: **23.0** | LOC: 93
  * *Intent:* /** * Fleury's algorithm of finding Eulerian Path (visit all graph edges exactly once). * */
- `KMeans` **(Many-Argument Workhorses)** (@ `src/algorithms/ml/k-means/kMeans.js`) -> Impact: **22.8** | LOC: 75
  * *Intent:* /** * Classifies the point in space based on k-Means algorithm. * */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 27 | 5168.18 | 0.22% | 0.0% |
| `src/data-structures/heap` | 14 | 280.76 | 11.83% | 1.18% |
| `src/algorithms/math/bits/__test__` | 16 | 244.64 | 1.41% | 0.0% |
| `src/data-structures/linked-list` | 12 | 240.68 | 3.57% | 0.0% |
| `src/data-structures/doubly-linked-list` | 10 | 194.2 | 4.25% | 0.0% |
| `src/data-structures/heap/__test__` | 5 | 191.82 | 8.6% | 0.0% |
| `src/algorithms/math/matrix` | 2 | 165.34 | 16.59% | 0.0% |
| `src/data-structures/graph` | 9 | 161.44 | 4.59% | 0.0% |
| `src/algorithms/sets/knapsack-problem` | 3 | 159.92 | 14.4% | 0.0% |
| `src/algorithms/image-processing/seam-carving` | 3 | 153.64 | 11.45% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/algorithms/math/is-power-of-two/isPowerOfTwoBitwise.js` -> **88.0797%** Exposure
- `src/algorithms/cryptography/hill-cipher/hillCipher.js` -> **73.1059%** Exposure
- `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` -> **66.4144%** Exposure
- `src/data-structures/queue/Queue.js` -> **50.0%** Exposure
- `src/data-structures/stack/Stack.js` -> **50.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/algorithms/cryptography/polynomial-hash/PolynomialHash.js` -> **100.0%** Exposure
- `src/algorithms/graph/detect-cycle/detectDirectedCycle.js` -> **100.0%** Exposure
- `src/algorithms/graph/eulerian-path/eulerianPath.js` -> **100.0%** Exposure
- `src/algorithms/graph/floyd-warshall/floydWarshall.js` -> **100.0%** Exposure
- `src/algorithms/image-processing/seam-carving/resizeImageWidth.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/algorithms/ml/knn/__test__/knn.test.js` -> **3** Orphaned Functions | **0** Duplicates
- `src/data-structures/linked-list/__test__/LinkedList.test.js` -> **3** Orphaned Functions | **0** Duplicates
- `src/data-structures/doubly-linked-list/__test__/DoublyLinkedList.test.js` -> **2** Orphaned Functions | **0** Duplicates
- `src/algorithms/cryptography/hill-cipher/_test_/hillCipher.test.js` -> **1** Orphaned Functions | **0** Duplicates
- `src/algorithms/graph/breadth-first-search/__test__/breadthFirstSearch.test.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2507` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/linked-list/LinkedList.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 199.46 | **LOC:** 273 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 23.523; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Connectivity (formerly Api Exposure) (60.5%), Complexity Load (formerly Cognitive Load) (35.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insert` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* /** */
  * `delete` **(Compute Cores)** (Impact: 14.5)
    * *Intent:* /** */
  * `find` **(Defensive Guards)** (Impact: 11.0)
    * *Intent:* /** */
  * `deleteTail` **(I/O & Config Routines)** (Impact: 6.3)
    * *Intent:* /** */
  * `deleteHead` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 36`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 5`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.000253 | `Ripple Effect (Closeness):` 0.036684
  * `Imports (Out-Degree: 2):` Comparator, LinkedListNode
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/data-structures/doubly-linked-list/DoublyLinkedList.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 165.4 | **LOC:** 264 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Connectivity (formerly Api Exposure) (48.9%), Complexity Load (formerly Cognitive Load) (33.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `delete` **(Defensive Guards)** (Impact: 16.6)
    * *Intent:* /** */
  * `find` **(Defensive Guards)** (Impact: 11.0)
    * *Intent:* /** */
  * `prepend` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** */
  * `deleteHead` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** */
  * `deleteTail` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 32`, `args: 13`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 5`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 2):` Comparator, DoublyLinkedListNode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/math/matrix/Matrix.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 164.06 | **LOC:** 310 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 8.266; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Connectivity (formerly Api Exposure) (62.4%), Complexity Load (formerly Cognitive Load) (33.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dot` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* /** */
  * `validateSameShape` **(Defensive Guards)** (Impact: 10.0)
    * *Intent:* /** * Validates that matrices are of the same shape. * */
  * `recWalk` **(Defensive Guards)** (Impact: 8.1)
    * *Intent:* /** * Traverses the matrix recursively. * */
  * `shape` **(Defensive Guards)** (Impact: 7.9)
    * *Intent:* /** */ /** * Gets the matrix's shape. * */
  * `validateType` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* /** * Checks if matrix has a correct type. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 61`, `args: 24`, `func_start: 16`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 14`
* *Defense:* `safety: 9`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009488
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/knapsack-problem/Knapsack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 141.92 | **LOC:** 196 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.402; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Connectivity (formerly Api Exposure) (38.6%), Complexity Load (formerly Cognitive Load) (35.8%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `solveZeroOneKnapsackProblem` **(I/O & Config Routines)** (Impact: 20.4)
    * *Intent:* // Solve 0/1 knapsack problem // Dynamic Programming approach.
  * `solveUnboundedKnapsackProblem` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* // Solve unbounded knapsack problem. // Greedy approach.
  * `compareCallback` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* /** */
  * `compareCallback` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* /** */
  * `compareCallback` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 27`, `args: 14`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `dead_code: 2`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 5`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.402
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 1):` MergeSort
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/image-processing/seam-carving/resizeImageWidth.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 133.24 | **LOC:** 254 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (34.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findLowEnergySeam` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* /** * Finds the seam (the sequence of pixels from top to bottom) that has the * lowest resulting ene...
  * `calculateEnergyMap` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /** * Calculates the energy of each pixel of the image. */
  * `getPixelEnergy` **(Many-Argument Workhorses)** (Impact: 7.5)
    * *Intent:* /** * Calculates the energy of a pixel. */
  * `resizeImageWidth` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* /** * Performs the content-aware image width resizing using the seam carving method. */
  * `deleteSeam` **(Callbacks & Closures)** (Impact: 4.8)
    * *Intent:* /** * Deletes the seam from the image data. * We delete the pixel in each row and then shift the res...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 34`, `args: 8`, `func_start: 6`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 1):` imageData
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/Heap.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 127.34 | **LOC:** 287 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 9.914; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.5%), Connectivity (formerly Api Exposure) (49.6%), Complexity Load (formerly Cognitive Load) (40.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `remove` **(Many-Argument Workhorses)** (Impact: 15.8)
    * *Intent:* /** */
  * `heapifyDown` **(Compute Cores)** (Impact: 9.9)
    * *Intent:* /** */
  * `heapifyUp` **(Compute Cores)** (Impact: 6.4)
    * *Intent:* /** */
  * `find` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* /** */
  * `poll` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 28`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `planned_debt: 1`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 5`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.914
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.020015
  * `Imports (Out-Degree: 1):` Comparator
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/red-black-tree/RedBlackTree.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 112.74 | **LOC:** 324 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (32.0%), Connectivity (formerly Api Exposure) (31.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `balance` **(Compute Cores)** (Impact: 30.4)
    * *Intent:* /** */
  * `leftLeftRotation` **(Compute Cores)** (Impact: 10.5)
    * *Intent:* /** * Left Left Case (p is left child of g and x is left child of p) */
  * `rightRightRotation` **(Compute Cores)** (Impact: 10.5)
    * *Intent:* /** * Right Right Case (p is right child of g and x is right child of p) */
  * `insert` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* /** */
  * `isNodeColored` **(Parameter Forwarders)** (Impact: 3.0)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 21`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 3`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 1):` BinarySearchTree
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/BinaryTreeNode.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 111.96 | **LOC:** 220 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 6.039; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.2%), Connectivity (formerly Api Exposure) (53.8%), Complexity Load (formerly Cognitive Load) (35.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `replaceChild` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* /** */
  * `removeChild` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* /** */
  * `uncle` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* /** * Get parent's sibling if it exists. */
  * `setLeft` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* /** */
  * `setRight` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 28`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.039
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.007806
  * `Imports (Out-Degree: 2):` Comparator, HashTable
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/data-structures/lru-cache/LRUCache.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 104.92 | **LOC:** 154 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 2.485; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Connectivity (formerly Api Exposure) (35.1%), Complexity Load (formerly Cognitive Load) (31.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evict` **(Defensive Guards)** (Impact: 8.7)
    * *Intent:* /** * Evicts (removes) the node from cache linked list. */
  * `append` **(I/O & Config Routines)** (Impact: 6.9)
    * *Intent:* /** * Appends a new node to the end of the cache linked list. */
  * `set` **(State Mutators)** (Impact: 5.7)
    * *Intent:* /** * Sets the value to cache by its key. * Time complexity: O(1) in average. */
  * `get` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* /** * Returns the cached value by its key. * Time complexity: O(1) in average. */
  * `constructor` **(State Mutators)** (Impact: 2.5)
    * *Intent:* /** * Creates a doubly-linked list node. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 9`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `api: 3`
* *Defense:* `safety: 5`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.485
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004839
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/algorithms/math/complex-number/ComplexNumber.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 91.98 | **LOC:** 161 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 6.763; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.0%), Connectivity (formerly Api Exposure) (53.1%), Complexity Load (formerly Cognitive Load) (47.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPhase` **(Defensive Guards)** (Impact: 36.8)
    * *Intent:* /** */
  * `toComplexNumber` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* /** * Convert real numbers to complex number. * In case if complex number is provided then lefts it ...
  * `divide` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* /** */
  * `add` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* /** */
  * `subtract` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 14`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 7`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.763
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.010323
  * `Imports (Out-Degree: 1):` radianToDegree
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/algorithms/string/regular-expression-matching/regularExpressionMatching.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 84.36 | **LOC:** 136 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.82; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.2%), Complexity Load (formerly Cognitive Load) (64.7%), Connectivity (formerly Api Exposure) (16.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `regularExpressionMatching` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* /** * Dynamic programming approach. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 8`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 1`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 74.82 | **LOC:** 72 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Complexity Load (formerly Cognitive Load) (62.6%), Connectivity (formerly Api Exposure) (18.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shortestCommonSupersequence` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 1):` longestCommonSubsequence
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/longest-common-subsequence/longestCommonSubsequence.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 73.78 | **LOC:** 61 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 3.367; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Complexity Load (formerly Cognitive Load) (60.3%), Connectivity (formerly Api Exposure) (20.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `longestCommonSubsequence` **(Defensive Guards)** (Impact: 27.0)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 10`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003629
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/algorithms/ml/k-means/kMeans.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 72.82 | **LOC:** 86 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 2.593; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Complexity Load (formerly Cognitive Load) (56.5%), Connectivity (formerly Api Exposure) (18.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `KMeans` **(Many-Argument Workhorses)** (Impact: 22.8)
    * *Intent:* /** * Classifies the point in space based on k-Means algorithm. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.593
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.003226
  * `Imports (Out-Degree: 2):` euclideanDistance, Matrix
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/algorithms/string/z-algorithm/zAlgorithm.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 70.18 | **LOC:** 133 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.82; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Complexity Load (formerly Cognitive Load) (43.4%), Connectivity (formerly Api Exposure) (16.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildZArray` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* /** */
  * `zAlgorithm` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 9`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/graph/GraphVertex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 69.6 | **LOC:** 139 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **1**; blast radius 6.803; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.1%), Connectivity (formerly Api Exposure) (86.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (78.0%), Guard Balance (formerly Safety Score) (39.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* /** */
  * `edgeComparator` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* /** */
  * `findEdge` **(Defensive Guards)** (Impact: 4.7)
    * *Intent:* /** */
  * `edgeFinder` **(Defensive Guards)** (Impact: 4.6)
  * `neighborsConverter` **(Callbacks & Closures)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 25`, `args: 19`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `safety: 8`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.803
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.033871
  * `Imports (Out-Degree: 1):` LinkedList
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/__test__/MinHeap.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 68.96 | **LOC:** 195 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.984; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (43.8%), Complexity Load (formerly Cognitive Load) (22.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 15`, `args: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 47`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `test: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Comparator, MinHeap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/bloom-filter/BloomFilter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 68.58 | **LOC:** 132 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.82; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.8%), Connectivity (formerly Api Exposure) (37.5%), Complexity Load (formerly Cognitive Load) (30.0%)
- **Documentation Coverage:** 7.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mayContain` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* /** */
  * `createStore` **(Parameter Forwarders)** (Impact: 3.8)
    * *Intent:* /** * Creates the data store for our filter. * We use this method to generate the store in order to ...
  * `hash1` **(Compute Cores)** (Impact: 3.4)
    * *Intent:* /** */
  * `hash3` **(Compute Cores)** (Impact: 3.4)
    * *Intent:* /** */
  * `hash2` **(Compute Cores)** (Impact: 3.3)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 19`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 4`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/math/fourier-transform/fastFourierTransform.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 68.54 | **LOC:** 78 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.402; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Complexity Load (formerly Cognitive Load) (42.4%), Connectivity (formerly Api Exposure) (18.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fastFourierTransform` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* /** * Returns the radix-2 fast fourier transform of the given array. * Optionally computes the radix...
  * `reverseBits` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* /** * Returns the number which is the flipped binary representation of input. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 13`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.402
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 2):` bitLength, ComplexNumber
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/string/longest-common-substring/longestCommonSubstring.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 68.2 | **LOC:** 69 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.82; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Complexity Load (formerly Cognitive Load) (55.2%), Connectivity (formerly Api Exposure) (18.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `longestCommonSubstring` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* /** * Longest Common Substring (LCS) (Dynamic Programming Approach). * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 13`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001613
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/MinHeapAdhoc.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 68.06 | **LOC:** 118 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 2.028; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (78.0%), Complexity Load (formerly Cognitive Load) (57.9%), Connectivity (formerly Api Exposure) (49.7%)
- **Documentation Coverage:** 45.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `heapifyDown` **(I/O & Config Routines)** (Impact: 12.6)
  * `heapifyUp` **(Interface Declarations)** (Impact: 3.5)
  * `poll` **(Defensive Guards)** (Impact: 2.4)
  * `swap` **(State Mutators)** (Impact: 2.0)
  * `constructor` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 17`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 6`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003226
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/MaxHeapAdhoc.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 67.92 | **LOC:** 116 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 2.028; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (78.4%), Complexity Load (formerly Cognitive Load) (59.4%), Connectivity (formerly Api Exposure) (49.8%)
- **Documentation Coverage:** 45.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `heapifyDown` **(I/O & Config Routines)** (Impact: 12.5)
  * `heapifyUp` **(Interface Declarations)** (Impact: 3.5)
  * `poll` **(Defensive Guards)** (Impact: 2.4)
  * `swap` **(State Mutators)** (Impact: 2.0)
  * `constructor` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 17`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 6`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003226
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/data-structures/graph/Graph.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 66.72 | **LOC:** 204 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); blast radius 7.446; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (78.0%), Guard Balance (formerly Safety Score) (74.9%), Connectivity (formerly Api Exposure) (58.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addEdge` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* /** */
  * `deleteEdge` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* /** */
  * `findEdge` **(Parameter Forwarders)** (Impact: 3.9)
    * *Intent:* /** */
  * `addVertex` **(Compute Cores)** (Impact: 3.4)
    * *Intent:* /** */
  * `getAdjacencyMatrix` **(Callbacks & Closures)** (Impact: 2.0)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 26`, `args: 20`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 6`
* *Defense:* `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.446
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.042297
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/algorithms/sorting/SortTester.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 65.3 | **LOC:** 73 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); blast radius 5.859; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (90.2%), Guard Balance (formerly Safety Score) (62.8%), Complexity Load (formerly Cognitive Load) (56.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compareCallback` **(Defensive Guards)** (Impact: 6.0)
  * `compareCallback` **(Defensive Guards)** (Impact: 5.8)
  * `testSortWithCustomComparator` **(Callbacks & Closures)** (Impact: 5.1)
  * `testSortStability` **(Defensive Guards)** (Impact: 5.0)
  * `testAlgorithmTimeComplexity` **(State Mutators)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 12`
* *Defense:* `safety: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.859
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019355
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/data-structures/graph/GraphVertex.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 69.6
- `src/data-structures/graph/Graph.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 66.72

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/data-structures/linked-list/LinkedList.js` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 100.0%)
- `src/data-structures/priority-queue/PriorityQueue.js` -> **Severity: 0.024** (Bridge: 0.0003 * Flux: 91.6827%)
- `src/algorithms/graph/dijkstra/dijkstra.js` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 99.9999%)
- `src/algorithms/graph/kruskal/kruskal.js` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 91.6827%)
- `src/data-structures/graph/GraphVertex.js` -> **Severity: 0.014** (Bridge: 0.0002 * Flux: 87.076%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/utils/comparator/Comparator.js` -> **Severity: 4.849** (Embedded: 0.0818 * Error Risk: 59.3184%)
- `src/algorithms/graph/dijkstra/dijkstra.js` -> **Severity: 4.354** (Embedded: 0.0484 * Error Risk: 89.9735%)
- `src/data-structures/linked-list/LinkedList.js` -> **Severity: 3.569** (Embedded: 0.0367 * Error Risk: 97.2874%)
- `src/data-structures/graph/Graph.js` -> **Severity: 3.17** (Embedded: 0.0423 * Error Risk: 74.9367%)
- `src/algorithms/graph/prim/prim.js` -> **Severity: 2.788** (Embedded: 0.0323 * Error Risk: 86.4295%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/data-structures/linked-list/LinkedListNode.js` -> **Severity: 590.2** (Blast Radius: 11.804 * Doc Risk: 50.0%)
- `src/algorithms/sorting/SortTester.js` -> **Severity: 585.9** (Blast Radius: 5.859 * Doc Risk: 100.0%)
- `src/algorithms/sorting/Sort.js` -> **Severity: 464.228** (Blast Radius: 16.248 * Doc Risk: 28.5714%)
- `src/playground/playground.js` -> **Severity: 173.118** (Blast Radius: 1.82 * Doc Risk: 95.12%)
- `src/data-structures/priority-queue/PriorityQueue.js` -> **Severity: 167.738** (Blast Radius: 13.419 * Doc Risk: 12.5%)

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
