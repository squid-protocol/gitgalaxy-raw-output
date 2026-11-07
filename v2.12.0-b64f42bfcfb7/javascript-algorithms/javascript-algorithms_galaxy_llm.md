# ARCHITECTURAL_BRIEF: javascript-algorithms
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/trekhleb/javascript-algorithms.git` |
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
- **Scope:** 622 analyzed artifact(s), 15345 LOC.
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
| Analyzed Artifacts (Scanned) | 622 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 54 |
| Total LOC | 15345 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 92.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7998 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.2307 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7248 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 110 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 359 | 15293 | 57.7% |
| MARKDOWN | 258 | 0 | 41.5% |
| JSON | 2 | 24 | 0.3% |
| PLAINTEXT | 2 | 1 | 0.3% |
| YAML | 1 | 27 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 621 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Declarative / Non-Code 22%, Callbacks & Closures Files 7%, Large Core Modules (2) 7%, Compute Cores Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 362 | 58.2% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 259 | 41.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 54*

**Composition by Extension & Reason:**
- `.png`: 27x Excluded (Explicitly Denied Extension: '.png')
- `.jpeg`: 12x Excluded (Explicitly Denied Extension: '.jpeg')
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Massive Static Asset Blob: 9728 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.7 | 11.2 | 4.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 77.4 | 31.9 | 44.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.7 | 1.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 0.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 90.2 | 14.6 | 8.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 88.1 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.2 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.0 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 78.0 | 1.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 13.8 | 0.0 | 0.0 |
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
| concurrency | 5 | 2 | 0 | `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` |
| connectivity | 406 | 183 | 2 | `src/algorithms/math/matrix/Matrix.js` |
| io | 3 | 1 | 0 | `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 8 | 3 | 0 | `src/algorithms/cryptography/caesar-cipher/caesarCipher.js` |
| events | 70 | 22 | 0 | `src/algorithms/math/liu-hui/__test__/liuHui.test.js` |
| tests | 4025 | 179 | 19 | `src/data-structures/tree/red-black-tree/__test__/RedBlackTree.test.js` |
| docs | 533 | 176 | 2 | `src/data-structures/heap/Heap.js` |
| debt | 13 | 9 | 0 | `src/algorithms/cryptography/hill-cipher/hillCipher.js` |
| mutation | 4269 | 263 | 20 | `src/data-structures/graph/__test__/Graph.test.js` |
| dead_code | 13 | 10 | 0 | `src/algorithms/linked-list/reverse-traversal/__test__/reverseTraversal.test.js` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
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
- `findLowEnergySeam` **(Many-Argument Workhorses)** (@ `src/algorithms/image-processing/seam-carving/resizeImageWidth.js`) -> Impact: **26.4** | LOC: 78
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
| `__monolith__` | 27 | 5168.18 | 0.0% | 0.0% |
| `src/data-structures/heap` | 14 | 278.96 | 11.83% | 0.75% |
| `src/algorithms/math/bits/__test__` | 16 | 244.64 | 0.0% | 0.0% |
| `src/data-structures/linked-list` | 12 | 240.68 | 3.57% | 0.0% |
| `src/data-structures/doubly-linked-list` | 10 | 194.2 | 4.25% | 0.0% |
| `src/data-structures/heap/__test__` | 5 | 191.62 | 8.6% | 0.0% |
| `src/algorithms/sets/knapsack-problem` | 3 | 159.62 | 14.4% | 0.0% |
| `src/data-structures/graph` | 9 | 155.94 | 4.59% | 0.0% |
| `src/algorithms/math/matrix` | 2 | 155.84 | 16.45% | 0.0% |
| `src/algorithms/image-processing/seam-carving` | 3 | 147.84 | 11.45% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/algorithms/sorting/SortTester.js` -> **99.708%** Exposure
- `src/algorithms/graph/strongly-connected-components/stronglyConnectedComponents.js` -> **99.6654%** Exposure
- `src/algorithms/math/is-power-of-two/isPowerOfTwoBitwise.js` -> **62.2459%** Exposure
- `src/algorithms/cryptography/hill-cipher/hillCipher.js` -> **37.7541%** Exposure
- `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` -> **33.5856%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/algorithms/cryptography/polynomial-hash/PolynomialHash.js` -> **100.0%** Exposure
- `src/algorithms/graph/detect-cycle/detectDirectedCycle.js` -> **100.0%** Exposure
- `src/algorithms/graph/eulerian-path/eulerianPath.js` -> **100.0%** Exposure
- `src/algorithms/graph/floyd-warshall/floydWarshall.js` -> **100.0%** Exposure
- `src/algorithms/image-processing/seam-carving/resizeImageWidth.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/algorithms/graph/strongly-connected-components/stronglyConnectedComponents.js` -> **0** Orphaned Functions | **2** Duplicates
- `src/algorithms/sorting/SortTester.js` -> **0** Orphaned Functions | **2** Duplicates
- `src/algorithms/graph/breadth-first-search/__test__/breadthFirstSearch.test.js` -> **1** Orphaned Functions | **0** Duplicates
- `src/algorithms/graph/depth-first-search/__test__/depthFirstSearch.test.js` -> **1** Orphaned Functions | **0** Duplicates
- `src/algorithms/image-processing/seam-carving/__tests__/resizeImageWidth.node.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2510` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/linked-list/LinkedList.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.434)
- **Top Global Matches:** file_cluster_15: 5.434, file_cluster_11: 7.142, file_cluster_16: 7.97
- **Magnitude:** 199.46 | **LOC:** 273 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 22.556; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.5%), Connectivity (formerly Api Exposure) (60.5%), Complexity Load (formerly Cognitive Load) (35.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.556
  * `Choke Point (Betweenness):` 0.000252 | `Ripple Effect (Closeness):` 0.036625
  * `Imports (Out-Degree: 2):` Comparator, LinkedListNode
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/data-structures/doubly-linked-list/DoublyLinkedList.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.227)
- **Top Global Matches:** file_cluster_15: 5.227, file_cluster_11: 6.789, file_cluster_16: 7.894
- **Magnitude:** 165.4 | **LOC:** 264 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.9%), Connectivity (formerly Api Exposure) (48.9%), Complexity Load (formerly Cognitive Load) (33.9%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 2):` Comparator, DoublyLinkedListNode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/math/matrix/Matrix.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.488)
- **Top Global Matches:** file_cluster_10: 5.488, file_cluster_15: 8.32, file_cluster_2: 8.707
- **Magnitude:** 154.56 | **LOC:** 310 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 8.217; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.8%), Connectivity (formerly Api Exposure) (59.1%), Complexity Load (formerly Cognitive Load) (32.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dot` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* /** */
  * `validateSameShape` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* /** * Validates that matrices are of the same shape. * */
  * `shape` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* /** */ /** * Gets the matrix's shape. * */
  * `recWalk` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* /** * Traverses the matrix recursively. * */
  * `validateType` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* /** * Checks if matrix has a correct type. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 61`, `args: 24`, `func_start: 16`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 12`
* *Defense:* `safety: 9`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009472
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/knapsack-problem/Knapsack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.89)
- **Top Global Matches:** file_cluster_4: 7.89, file_cluster_10: 11.122, file_cluster_6: 11.617
- **Magnitude:** 141.62 | **LOC:** 196 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.9%), Connectivity (formerly Api Exposure) (38.6%), Complexity Load (formerly Cognitive Load) (35.8%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `solveZeroOneKnapsackProblem` **(I/O & Config Routines)** (Impact: 20.4)
    * *Intent:* // Solve 0/1 knapsack problem // Dynamic Programming approach.
  * `solveUnboundedKnapsackProblem` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* // Solve unbounded knapsack problem. // Greedy approach.
  * `compareCallback` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* /** */
  * `compareCallback` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* /** */
  * `compareCallback` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 27`, `args: 14`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 5`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 1):` MergeSort
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/image-processing/seam-carving/resizeImageWidth.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.456)
- **Top Global Matches:** file_cluster_10: 6.456, file_cluster_15: 7.32, file_cluster_16: 8.195
- **Magnitude:** 127.44 | **LOC:** 254 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.3%), Complexity Load (formerly Cognitive Load) (34.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findLowEnergySeam` **(Many-Argument Workhorses)** (Impact: 26.4)
    * *Intent:* /** * Finds the seam (the sequence of pixels from top to bottom) that has the * lowest resulting ene...
  * `calculateEnergyMap` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* /** * Calculates the energy of each pixel of the image. */
  * `getPixelEnergy` **(Many-Argument Workhorses)** (Impact: 7.0)
    * *Intent:* /** * Calculates the energy of a pixel. */
  * `resizeImageWidth` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* /** * Performs the content-aware image width resizing using the seam carving method. */
  * `deleteSeam` **(Callbacks & Closures)** (Impact: 4.4)
    * *Intent:* /** * Deletes the seam from the image data. * We delete the pixel in each row and then shift the res...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 34`, `args: 8`, `func_start: 6`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 1):` imageData
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/Heap.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.555)
- **Top Global Matches:** file_cluster_15: 4.555, file_cluster_11: 6.477, file_cluster_16: 7.666
- **Magnitude:** 125.54 | **LOC:** 287 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 12.017; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.3%), Connectivity (formerly Api Exposure) (49.6%), Complexity Load (formerly Cognitive Load) (40.1%)
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
* *Structure:* `branch: 22`, `structural_boundaries: 28`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `planned_debt: 1`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 5`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.017
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.026118
  * `Imports (Out-Degree: 1):` Comparator
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/red-black-tree/RedBlackTree.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.135)
- **Top Global Matches:** file_cluster_4: 6.135, file_cluster_15: 9.257, file_cluster_16: 10.862
- **Magnitude:** 112.74 | **LOC:** 324 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (56.7%), Complexity Load (formerly Cognitive Load) (32.0%), Connectivity (formerly Api Exposure) (31.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 1):` BinarySearchTree
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/tree/BinaryTreeNode.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.301)
- **Top Global Matches:** file_cluster_15: 5.301, file_cluster_11: 5.652, file_cluster_2: 7.589
- **Magnitude:** 111.96 | **LOC:** 220 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 5.172; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.7%), Connectivity (formerly Api Exposure) (53.8%), Complexity Load (formerly Cognitive Load) (35.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.172
  * `Choke Point (Betweenness):` 9.1e-05 | `Ripple Effect (Closeness):` 0.007794
  * `Imports (Out-Degree: 2):` Comparator, HashTable
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/data-structures/lru-cache/LRUCache.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.555)
- **Top Global Matches:** file_cluster_15: 6.555, file_cluster_2: 6.63, file_cluster_13: 7.353
- **Magnitude:** 104.92 | **LOC:** 154 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 2.47; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.0%), Connectivity (formerly Api Exposure) (35.1%), Complexity Load (formerly Cognitive Load) (31.6%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004831
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/algorithms/math/complex-number/ComplexNumber.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.269)
- **Top Global Matches:** file_cluster_4: 7.269, file_cluster_6: 10.727, file_cluster_15: 11.34
- **Magnitude:** 91.98 | **LOC:** 161 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 6.722; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (56.7%), Connectivity (formerly Api Exposure) (53.1%), Complexity Load (formerly Cognitive Load) (47.4%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.722
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.010306
  * `Imports (Out-Degree: 1):` radianToDegree
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/algorithms/string/regular-expression-matching/regularExpressionMatching.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.646)
- **Top Global Matches:** file_cluster_1: 4.646, file_cluster_3: 48.135, file_cluster_8: 69.998
- **Magnitude:** 84.36 | **LOC:** 136 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.808; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.5%), Complexity Load (formerly Cognitive Load) (64.7%), Connectivity (formerly Api Exposure) (16.0%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/shortest-common-supersequence/shortestCommonSupersequence.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 3.909)
- **Top Global Matches:** file_cluster_1: 3.909, file_cluster_3: 48.076, file_cluster_8: 69.959
- **Magnitude:** 74.82 | **LOC:** 72 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.4%), Complexity Load (formerly Cognitive Load) (62.6%), Connectivity (formerly Api Exposure) (18.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 1):` longestCommonSubsequence
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/sets/longest-common-subsequence/longestCommonSubsequence.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.936)
- **Top Global Matches:** file_cluster_9: 5.936, file_cluster_15: 12.387, file_cluster_16: 12.441
- **Magnitude:** 73.78 | **LOC:** 61 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 3.346; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.2%), Complexity Load (formerly Cognitive Load) (60.3%), Connectivity (formerly Api Exposure) (20.5%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003623
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/algorithms/ml/k-means/kMeans.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.195)
- **Top Global Matches:** file_cluster_9: 5.195, file_cluster_16: 11.907, file_cluster_15: 12.008
- **Magnitude:** 72.82 | **LOC:** 86 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 2.577; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.4%), Complexity Load (formerly Cognitive Load) (56.5%), Connectivity (formerly Api Exposure) (18.9%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.577
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.003221
  * `Imports (Out-Degree: 2):` euclideanDistance, Matrix
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/algorithms/string/z-algorithm/zAlgorithm.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.931)
- **Top Global Matches:** file_cluster_9: 5.931, file_cluster_15: 7.451, file_cluster_16: 8.207
- **Magnitude:** 70.18 | **LOC:** 133 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.808; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (43.4%), Connectivity (formerly Api Exposure) (16.1%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/__test__/MinHeap.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.613)
- **Top Global Matches:** file_cluster_12: 6.613, file_cluster_10: 6.995, file_cluster_7: 7.808
- **Magnitude:** 68.96 | **LOC:** 195 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.978; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (46.1%), Complexity Load (formerly Cognitive Load) (22.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Comparator, MinHeap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data-structures/bloom-filter/BloomFilter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.642)
- **Top Global Matches:** file_cluster_15: 4.642, file_cluster_2: 7.062, file_cluster_11: 7.159
- **Magnitude:** 68.58 | **LOC:** 132 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.808; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.4%), Connectivity (formerly Api Exposure) (37.5%), Complexity Load (formerly Cognitive Load) (30.0%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/math/fourier-transform/fastFourierTransform.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.933)
- **Top Global Matches:** file_cluster_9: 5.933, file_cluster_15: 7.369, file_cluster_16: 8.365
- **Magnitude:** 68.54 | **LOC:** 78 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.1%), Complexity Load (formerly Cognitive Load) (42.4%), Connectivity (formerly Api Exposure) (18.1%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 2):` bitLength, ComplexNumber
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algorithms/string/longest-common-substring/longestCommonSubstring.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.479)
- **Top Global Matches:** file_cluster_9: 5.479, file_cluster_16: 12.089, file_cluster_15: 12.221
- **Magnitude:** 68.2 | **LOC:** 69 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.808; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.8%), Complexity Load (formerly Cognitive Load) (55.2%), Connectivity (formerly Api Exposure) (18.6%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00161
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/MinHeapAdhoc.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.408)
- **Top Global Matches:** file_cluster_15: 5.408, file_cluster_11: 5.835, file_cluster_2: 7.63
- **Magnitude:** 68.06 | **LOC:** 118 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 2.016; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (57.9%), Guard Balance (formerly Safety Score) (57.8%), Connectivity (formerly Api Exposure) (49.7%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003221
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/data-structures/heap/MaxHeapAdhoc.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.414)
- **Top Global Matches:** file_cluster_15: 5.414, file_cluster_11: 5.841, file_cluster_2: 7.645
- **Magnitude:** 67.92 | **LOC:** 116 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 2.016; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (59.4%), Guard Balance (formerly Safety Score) (58.0%), Connectivity (formerly Api Exposure) (49.8%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003221
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/data-structures/graph/Graph.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.576)
- **Top Global Matches:** file_cluster_10: 6.576, file_cluster_15: 6.65, file_cluster_11: 7.195
- **Magnitude:** 66.72 | **LOC:** 204 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); blast radius 7.263; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (78.0%), Connectivity (formerly Api Exposure) (58.8%), Guard Balance (formerly Safety Score) (56.7%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.042229
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/algorithms/sorting/SortTester.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.273)
- **Top Global Matches:** file_cluster_10: 6.273, file_cluster_15: 7.969, file_cluster_13: 8.082
- **Magnitude:** 64.5 | **LOC:** 73 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); blast radius 5.824; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Connectivity (formerly Api Exposure) (90.2%), Complexity Load (formerly Cognitive Load) (56.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compareCallback` **(Defensive Guards)** (Impact: 5.5)
  * `compareCallback` **(Defensive Guards)** (Impact: 5.5)
  * `testSortWithCustomComparator` **(Callbacks & Closures)** (Impact: 5.1)
  * `testSortStability` **(Defensive Guards)** (Impact: 5.0)
  * `testAlgorithmTimeComplexity` **(State Mutators)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `duplicate_logic: 2`
* *Architecture:* `api: 12`
* *Defense:* `safety: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.824
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019324
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/data-structures/graph/GraphVertex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.753)
- **Top Global Matches:** file_cluster_11: 6.753, file_cluster_10: 6.843, file_cluster_15: 6.854
- **Magnitude:** 64.1 | **LOC:** 139 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **1**; blast radius 6.624; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.1%), Connectivity (formerly Api Exposure) (78.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (78.0%), Guard Balance (formerly Safety Score) (43.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* /** */
  * `edgeComparator` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* /** */
  * `findEdge` **(Defensive Guards)** (Impact: 4.7)
    * *Intent:* /** */
  * `hasNeighbor` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* /** */
  * `neighborsConverter` **(Defensive Guards)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 25`, `args: 19`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 8`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.624
  * `Choke Point (Betweenness):` 0.000161 | `Ripple Effect (Closeness):` 0.033816
  * `Imports (Out-Degree: 1):` LinkedList
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/data-structures/linked-list/__test__/LinkedList.test.js` (JAVASCRIPT) | Magnitude: 24.56 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 200, test: 94, structural_boundaries: 36, core_var_decl: 31
- `src/data-structures/graph/Graph.js` (JAVASCRIPT) | Magnitude: 66.72 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 26, args: 20, doc: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/data-structures/graph/GraphVertex.js` (JAVASCRIPT) | Magnitude: 64.1 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 25, args: 19, func_start: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/algorithms/math/fast-powering/fastPowering.js` (JAVASCRIPT) | Magnitude: 7.42 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 4, branch: 3, safety: 2
- `src/algorithms/math/is-power-of-two/isPowerOfTwoBitwise.js` (JAVASCRIPT) | Magnitude: 5.02 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, branch: 2, args: 1
- `src/algorithms/uncategorized/jump-game/greedyJumpGame.js` (JAVASCRIPT) | Magnitude: 12.5 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, core_var_decl: 4, design_camel_case: 4
- `src/algorithms/uncategorized/recursive-staircase/recursiveStaircaseBF.js` (JAVASCRIPT) | Magnitude: 7.94 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, branch: 4, safety: 2
- `src/algorithms/math/bits/isEven.js` (JAVASCRIPT) | Magnitude: 2.66 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/algorithms/string/palindrome/isPalindrome.js` (JAVASCRIPT) | Magnitude: 12.14 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, branch: 3, state_mutation: 2
- `src/algorithms/graph/eulerian-path/__test__/eulerianPath.test.js` (JAVASCRIPT) | Magnitude: 3.84 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 111, core_var_decl: 51, design_camel_case: 48, test: 28
- `src/algorithms/graph/bellman-ford/__test__/bellmanFord.test.js` (JAVASCRIPT) | Magnitude: 17.1 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 99, core_var_decl: 37, design_camel_case: 35, test: 18
- `src/algorithms/graph/dijkstra/__test__/dijkstra.test.js` (JAVASCRIPT) | Magnitude: 17.1 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 99, core_var_decl: 37, design_camel_case: 35, test: 18
- `src/algorithms/math/fibonacci/fibonacciNth.js` (JAVASCRIPT) | Magnitude: 15.48 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, core_var_decl: 4, design_camel_case: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/algorithms/sets/knapsack-problem/__test__/Knapsack.test.js` (JAVASCRIPT) | Magnitude: 17.54 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 123, test: 49, core_var_decl: 21, design_camel_case: 14
- `src/data-structures/disjoint-set/__test__/DisjointSetItem.test.js` (JAVASCRIPT) | Magnitude: 3.32 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, test: 65, core_var_decl: 9, design_camel_case: 9
- `src/data-structures/graph/__test__/GraphEdge.test.js` (JAVASCRIPT) | Magnitude: 3.1 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 46, test: 25, core_var_decl: 13, structural_boundaries: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/data-structures/graph/Graph.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 66.72
- `src/data-structures/graph/GraphVertex.js` -> **Alex Rock Ancelet** (100.0% isolated ownership) | Magnitude: 64.1

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

- `src/utils/comparator/Comparator.js` -> **Severity: 3.988** (Embedded: 0.0816 * Error Risk: 48.8573%)
- `src/algorithms/graph/dijkstra/dijkstra.js` -> **Severity: 3.075** (Embedded: 0.0483 * Error Risk: 63.6453%)
- `src/data-structures/linked-list/LinkedList.js` -> **Severity: 2.765** (Embedded: 0.0366 * Error Risk: 75.5071%)
- `src/data-structures/graph/Graph.js` -> **Severity: 2.395** (Embedded: 0.0422 * Error Risk: 56.7054%)
- `src/algorithms/graph/prim/prim.js` -> **Severity: 1.963** (Embedded: 0.0322 * Error Risk: 60.962%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/algorithms/sorting/SortTester.js` -> **Severity: 582.4** (Blast Radius: 5.824 * Doc Risk: 100.0%)
- `src/data-structures/linked-list/LinkedListNode.js` -> **Severity: 569.35** (Blast Radius: 11.387 * Doc Risk: 50.0%)
- `src/algorithms/sorting/Sort.js` -> **Severity: 538.333** (Blast Radius: 16.15 * Doc Risk: 33.3333%)
- `src/playground/playground.js` -> **Severity: 171.977** (Blast Radius: 1.808 * Doc Risk: 95.12%)
- `src/data-structures/priority-queue/PriorityQueue.js` -> **Severity: 166.7** (Blast Radius: 13.336 * Doc Risk: 12.5%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1187 call pairs -- scoped 44.2%, unique 0.0%, ambiguous 19.5%, external 36.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 1187 | 44.2% | 0.0% | 19.5% | 36.3% |

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
