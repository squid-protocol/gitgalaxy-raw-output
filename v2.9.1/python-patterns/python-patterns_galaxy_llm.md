# ARCHITECTURAL_BRIEF: python-patterns
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/faif/python-patterns.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 78 analyzed artifact(s), 2272 LOC.
- **Load-bearing artifact:** `patterns/behavioral/catalog.py` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `README.md` -- pulls in 40 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `patterns/other/graph_search.py` at magnitude 148.68 (structural weight, not risk).
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
| Total Artifacts | 123 |
| Analyzed Artifacts (Scanned) | 78 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 45 |
| Total LOC | 2272 |
| Volatility Index | 0.013 |
| % Scanned of codebase = | 63.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4242 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4237 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 26 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 73 | 2204 | 93.6% |
| PLAINTEXT | 2 | 0 | 2.6% |
| MAKEFILE | 1 | 55 | 1.3% |
| MARKDOWN | 1 | 0 | 1.3% |
| SHELL | 1 | 13 | 1.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `0.977`
> **Composition Archetype:** `Small Flat Repo` (z +0.98; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 42%, Parameter Forwarders Files 18%, Large Core Modules (2) 17%, Data / Markup / Trivial 14%, Encapsulated Accessors Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 75 | 96.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 3.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 45*

**Composition by Extension & Reason:**
- `.png`: 35x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 59.7 | 12.7 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 56.1 | 62.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.7 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 75.7 | 32.2 | 41.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.6 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.9 | 1.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 56.8 | 8.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.4 | 81.8 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 16 | 6 | 0 | `patterns/structural/mvc.py` |
| cleanup | 1 | 1 | 0 | `tests/structural/test_proxy.py` |
| guards | 146 | 32 | 5 | `patterns/other/hsm/hsm.py` |
| danger | 92 | 28 | 4 | `patterns/structural/mvc.py` |
| concurrency | 2 | 2 | 0 | `patterns/behavioral/iterator.py` |
| connectivity | 531 | 66 | 13 | `patterns/other/hsm/hsm.py` |
| io | 12 | 3 | 0 | `Makefile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1 | 1 | 0 | `patterns/dependency_injection.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 18 | 4 | 0 | `tests/behavioral/test_publish_subscribe.py` |
| tests | 196 | 25 | 8 | `tests/test_hsm.py` |
| docs | 183 | 44 | 6 | `patterns/structural/mvc.py` |
| debt | 105 | 29 | 4 | `Makefile` |
| mutation | 677 | 66 | 19 | `tests/structural/test_adapter.py` |
| dead_code | 105 | 28 | 4 | `tests/test_hsm.py` |
| credential | 0 | 0 | 0 | - |
| threat | 65 | 22 | 3 | `patterns/structural/flyweight_with_metaclass.py` |
| ml_ai | 1 | 1 | 0 | `patterns/behavioral/catalog.py` |
| ui | 12 | 3 | 0 | `patterns/structural/decorator.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 5)
- `lint.sh` (Hits: 4)
- `tests/structural/test_proxy.py` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **catalog.py** (`patterns/behavioral/catalog.py`) — 2 inbound connections
2. **mediator.py** (`patterns/behavioral/mediator.py`) — 2 inbound connections
3. **memento.py** (`patterns/behavioral/memento.py`) — 2 inbound connections
4. **observer.py** (`patterns/behavioral/observer.py`) — 2 inbound connections
5. **publish_subscribe.py** (`patterns/behavioral/publish_subscribe.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`README.md`) — 40 outbound dependencies
2. **memento.py** (`patterns/behavioral/memento.py`) — 5 outbound dependencies
3. **mvc.py** (`patterns/structural/mvc.py`) — 5 outbound dependencies
4. **pool.py** (`patterns/creational/pool.py`) — 4 outbound dependencies
5. **blackboard.py** (`patterns/other/blackboard.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `find_shortest_path_dfs` **(Generic / Templated Code)** (@ `patterns/other/graph_search.py`) -> Impact: **18.7** | LOC: 16
- `find_shortest_path_bfs` **(Many-Argument Workhorses)** (@ `patterns/other/graph_search.py`) -> Impact: **15.8** | LOC: 37
  * *Intent:* """ Finds the shortest path between two nodes in a graph using breadth-first search. :param start: The node to start from. :type start: str or int :pa...
- `find_path_dfs` **(Generic / Templated Code)** (@ `patterns/other/graph_search.py`) -> Impact: **14.1** | LOC: 13
- `find_all_paths_dfs` **(Generic / Templated Code)** (@ `patterns/other/graph_search.py`) -> Impact: **11.8** | LOC: 13
- `template_function` **(Compute Cores)** (@ `patterns/behavioral/template.py`) -> Impact: **10.7** | LOC: 13
- `visit` **(Generic / Templated Code)** (@ `patterns/behavioral/visitor.py`) -> Impact: **9.5** | LOC: 11
- `do_the_job` **(Generic / Templated Code)** (@ `patterns/structural/proxy.py`) -> Impact: **9.2** | LOC: 11
  * *Intent:* """ logging and controlling access are some examples of proxy usages. """
- `__set__` **(Generic / Templated Code)** (@ `patterns/behavioral/strategy.py`) -> Impact: **8.2** | LOC: 5
- `__init__` **(Stateful Encapsulated Methods)** (@ `patterns/behavioral/catalog.py`) -> Impact: **7.6** | LOC: 14
  * *Intent:* # dictionary that will be used to determine which static method is # to be executed but that will be also used to store possible param # value self._s...
- `dispatch` **(Generic / Templated Code)** (@ `patterns/structural/front_controller.py`) -> Impact: **7.6** | LOC: 13
  * *Intent:* """ This function is used to dispatch the request based on the type of device. If it is a mobile, then mobile view will be called and if it is a table...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `patterns/behavioral` | 18 | 676.54 | 22.81% | 18.76% |
| `patterns/structural` | 12 | 431.7 | 16.46% | 19.72% |
| `patterns/creational` | 8 | 242.68 | 17.99% | 17.22% |
| `patterns/other` | 3 | 216.92 | 22.3% | 33.33% |
| `tests/structural` | 7 | 182.7 | 6.29% | 0.0% |
| `tests/behavioral` | 9 | 146.12 | 0.96% | 0.0% |
| `tests/creational` | 7 | 132.88 | 3.84% | 0.0% |
| `patterns/other/hsm` | 2 | 118.18 | 8.29% | 50.0% |
| `tests` | 2 | 58.04 | 0.0% | 0.0% |
| `patterns` | 2 | 46.94 | 5.27% | 18.88% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `patterns/behavioral/specification.py` -> **100.0%** Exposure
- `patterns/creational/builder.py` -> **100.0%** Exposure
- `patterns/behavioral/catalog.py` -> **99.9979%** Exposure
- `patterns/other/hsm/hsm.py` -> **99.9976%** Exposure
- `patterns/other/blackboard.py` -> **99.9844%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `patterns/other/graph_search.py` -> **100.0%** Exposure
- `patterns/structural/flyweight_with_metaclass.py` -> **100.0%** Exposure
- `patterns/structural/front_controller.py` -> **99.9999%** Exposure
- `patterns/behavioral/catalog.py` -> **99.9995%** Exposure
- `patterns/behavioral/memento.py` -> **99.9932%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_hsm.py` -> **12** Orphaned Functions | **2** Duplicates
- `tests/structural/test_adapter.py` -> **11** Orphaned Functions | **0** Duplicates
- `patterns/other/hsm/hsm.py` -> **0** Orphaned Functions | **6** Duplicates
- `tests/creational/test_lazy.py` -> **6** Orphaned Functions | **0** Duplicates
- `tests/creational/test_prototype.py` -> **6** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `189` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `patterns/other/graph_search.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 148.68 | **LOC:** 160 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 10.208; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (46.6%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_shortest_path_dfs` **(Generic / Templated Code)** (Impact: 18.7)
  * `find_shortest_path_bfs` **(Many-Argument Workhorses)** (Impact: 15.8)
    * *Intent:* """ Finds the shortest path between two nodes in a graph using breadth-first search. :param start: T...
  * `find_path_dfs` **(Generic / Templated Code)** (Impact: 14.1)
  * `find_all_paths_dfs` **(Generic / Templated Code)** (Impact: 11.8)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 18`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.208
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012987
  * `Imports (Out-Degree: 0):` doctest, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `patterns/other/hsm/hsm.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 107.66 | **LOC:** 178 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (93.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_message` **(Compute Cores)** (Impact: 5.4)
  * `__init__` **(Encapsulated Accessors)** (Impact: 2.4)
  * `_next_state` **(Encapsulated Accessors)** (Impact: 2.0)
  * `__init__` **(Parameter Forwarders)** (Impact: 1.8)
  * `__init__` **(Encapsulated Accessors)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 59`, `args: 34`, `func_start: 34`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 15`, `duplicate_logic: 6`
* *Architecture:* `api: 31`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/structural/mvc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 93.4 | **LOC:** 217 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Guard Balance (formerly Safety Score) (86.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.0%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve` **(Generic / Templated Code)** (Impact: 7.2)
  * `show_item_information` **(Type Conversions)** (Impact: 5.0)
  * `show_item_list` **(Generic / Templated Code)** (Impact: 4.2)
  * `show_item_information` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* """ Show information about a {item_type} item. :param str item_name: the name of the {item_type} ite...
  * `register` **(Generic / Templated Code)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 51`, `args: 20`, `func_start: 20`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 10`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 4`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` abc, doctest, inspect, sys, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/behavioral/catalog.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 87.28 | **LOC:** 176 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 54.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* # dictionary that will be used to determine which static method is # to be executed but that will be...
  * `__init__` **(Generic / Templated Code)** (Impact: 7.3)
  * `__init__` **(Generic / Templated Code)** (Impact: 7.2)
    * *Intent:* # simple test to validate param value if param in self._class_method_choices: self.param = param els...
  * `__init__` **(Generic / Templated Code)** (Impact: 7.2)
    * *Intent:* # simple test to validate param value if param in self._static_method_choices: self.param = param el...
  * `main_method` **(Generic / Templated Code)** (Impact: 1.8)
    * *Intent:* """will execute either _static_method_1 or _static_method_2 depending on self.param value """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 34`, `args: 17`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `state_mutation: 13`, `duplicate_logic: 4`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` doctest
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/structural/test_adapter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 66.48 | **LOC:** 75 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.99; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (85.2%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_car_adapter_shall_make_very_loud_noise` **(Parameter Forwarders)** (Impact: 1.8)
  * `setUp` **(Parameter Forwarders)** (Impact: 1.7)
  * `test_dog_adapter_shall_make_noise` **(Parameter Forwarders)** (Impact: 1.7)
  * `test_cat_adapter_shall_make_noise` **(Parameter Forwarders)** (Impact: 1.7)
  * `test_human_adapter_shall_make_noise` **(Parameter Forwarders)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 34`, `unreferenced_by_name: 11`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.99
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` patterns.structural.adapter, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patterns/behavioral/memento.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 60.54 | **LOC:** 146 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Connectivity (formerly Api Exposure) (64.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.8%)
- **Documentation Coverage:** 80.6452% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `memento` **(Generic / Templated Code)** (Impact: 5.6)
  * `rollback` **(Generic / Templated Code)** (Impact: 3.0)
  * `commit` **(Generic / Templated Code)** (Impact: 2.9)
  * `Transactional` **(Generic / Templated Code)** (Impact: 2.7)
    * *Intent:* """Adds transactional semantics to methods. Methods decorated with @Transactional will roll back to ...
  * `__get__` **(Generic / Templated Code)** (Impact: 2.7)
    * *Intent:* """ A decorator that makes a function transactional. :param method: The function to be decorated. ""...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 26`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 11`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `safety: 1`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` copy, doctest, sys, traceback, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/behavioral/specification.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 59.66 | **LOC:** 111 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.208; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (75.7%), Guard Balance (formerly Safety Score) (66.0%), Mutation Surface (formerly State Flux) (15.3%)
- **Documentation Coverage:** 93.9394% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_satisfied_by` **(Generic / Templated Code)** (Impact: 3.7)
  * `is_satisfied_by` **(Type Conversions)** (Impact: 3.7)
  * `__init__` **(Generic / Templated Code)** (Impact: 2.1)
  * `__init__` **(Generic / Templated Code)** (Impact: 2.1)
  * `and_specification` **(Parameter Forwarders)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 41`, `args: 18`, `func_start: 18`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 22`, `import: 3`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.208
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012987
  * `Imports (Out-Degree: 0):` abc, doctest, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `patterns/other/blackboard.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 57.72 | **LOC:** 143 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 10.208; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (66.2%), Guard Balance (formerly Safety Score) (65.0%), Mutation Surface (formerly State Flux) (46.3%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_loop` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* """ This function is a loop that runs until the progress reaches 100. It checks if an expert is eage...
  * `is_eager_to_contribute` **(Generic / Templated Code)** (Impact: 4.3)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.8)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.8)
  * `add_expert` **(Generic / Templated Code)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 31`, `args: 17`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 17`, `import: 3`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.208
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012987
  * `Imports (Out-Degree: 0):` abc, doctest, pprint, random
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `patterns/structural/front_controller.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 57.72 | **LOC:** 96 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.208; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.6%), Connectivity (formerly Api Exposure) (59.7%), Complexity Load (formerly Cognitive Load) (32.7%)
- **Documentation Coverage:** 53.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatch` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* """ This function is used to dispatch the request based on the type of device. If it is a mobile, th...
  * `dispatch_request` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* """ This function takes a request object and sends it to the dispatcher. """
  * `__init__` **(Compute Cores)** (Impact: 5.5)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.6)
  * `show_index_page` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 23`, `args: 8`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.208
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012987
  * `Imports (Out-Degree: 0):` __future__, doctest, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `patterns/behavioral/strategy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 53.42 | **LOC:** 93 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (69.5%), Connectivity (formerly Api Exposure) (68.9%), Complexity Load (formerly Cognitive Load) (56.5%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__set__` **(Generic / Templated Code)** (Impact: 8.2)
  * `validate` **(Defensive Guards)** (Impact: 5.7)
  * `apply_discount` **(Generic / Templated Code)** (Impact: 4.6)
  * `__set_name__` **(Generic / Templated Code)** (Impact: 2.1)
  * `__get__` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 27`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` __future__, doctest, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/behavioral/observer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 48.94 | **LOC:** 136 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (83.1%), Connectivity (formerly Api Exposure) (55.3%), Complexity Load (formerly Cognitive Load) (29.7%)
- **Documentation Coverage:** 45.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `attach` **(Generic / Templated Code)** (Impact: 3.9)
    * *Intent:* """ Attach an observer to the subject. Args: observer (Observer): The observer instance to attach. "...
  * `notify` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* """ Notify all attached observers by calling their update method. """
  * `detach` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* """ Detach an observer from the subject. Args: observer (Observer): The observer instance to detach....
  * `update` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* """ Receive update from the subject. Args: subject (Subject): The subject instance sending the updat...
  * `__init__` **(Encapsulated Accessors)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 24`, `args: 11`, `func_start: 11`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`
* *Architecture:* `api: 14`, `import: 3`
* *Defense:* `safety: 2`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` __future__, doctest, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/behavioral/publish_subscribe.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 48.0 | **LOC:** 96 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (88.3%), Connectivity (formerly Api Exposure) (68.4%), Complexity Load (formerly Cognitive Load) (28.8%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Generic / Templated Code)** (Impact: 4.5)
  * `subscribe` **(Generic / Templated Code)** (Impact: 2.1)
  * `unsubscribe` **(Generic / Templated Code)** (Impact: 2.1)
  * `__init__` **(Generic / Templated Code)** (Impact: 2.1)
  * `notify` **(Generic / Templated Code)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 18`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` __future__, doctest
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/test_hsm.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 47.52 | **LOC:** 99 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.99; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (17.0%), Connectivity (formerly Api Exposure) (12.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.9%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_given_standby_on_message_switchover_shall_call_hsm_methods` **(Parameter Forwarders)** (Impact: 2.1)
  * `test_calling_next_state_shall_change_current_state` **(Defensive Guards)** (Impact: 1.7)
  * `test_method_perform_switchover_shall_return_specifically` **(Parameter Forwarders)** (Impact: 1.7)
    * *Intent:* """Exemplary HierachicalStateMachine method test. (here: _perform_switchover()). Add additional test...
  * `test_given_standby_on_message_diagnostics_failed_shall_raise_exception_and_keep_in_state` **(Defensive Guards)** (Impact: 1.7)
  * `test_given_standby_on_message_diagnostics_passed_shall_raise_exception_and_keep_in_state` **(Defensive Guards)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 31`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `safety: 7`, `doc: 2`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.99
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` patterns.other.hsm.hsm, unittest, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patterns/creational/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 46.54 | **LOC:** 113 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (74.6%), Connectivity (formerly Api Exposure) (73.0%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_size` **(Generic / Templated Code)** (Impact: 2.9)
  * `construct_building` **(Generic / Templated Code)** (Impact: 1.7)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.6)
  * `build_floor` **(Parameter Forwarders)** (Impact: 1.5)
  * `build_size` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 22`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `state_mutation: 7`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` doctest
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/behavioral/state.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 45.86 | **LOC:** 90 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (86.6%), Mutation Surface (formerly State Flux) (85.0%), Connectivity (formerly Api Exposure) (64.8%), Complexity Load (formerly Cognitive Load) (41.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scan` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* """Scan the dial to the next station"""
  * `__init__` **(Generic / Templated Code)** (Impact: 2.0)
  * `__init__` **(Generic / Templated Code)** (Impact: 2.0)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.7)
    * *Intent:* """We have an AM state and an FM state"""
  * `toggle_amfm` **(Generic / Templated Code)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 16`, `args: 9`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` __future__, doctest
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/structural/flyweight_with_metaclass.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 45.62 | **LOC:** 64 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.99; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.9%), Guard Balance (formerly Safety Score) (90.0%), Complexity Load (formerly Cognitive Load) (59.7%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Parameter Forwarders)** (Impact: 4.5)
  * `__new__` **(Parameter Forwarders)** (Impact: 2.8)
    * *Intent:* """ Set up object pool :param name: class name :param parents: class parents :param dct: dict: inclu...
  * `_serialize_params` **(Stateful Encapsulated Methods)** (Impact: 2.5)
    * *Intent:* """ Serialize input parameters to a key. Simple implementation is just to serialize it as a string "...
  * `__init__` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* # print('Init {}: {}'.format(self.__class__, (args, kwargs))) pass if __name__ == "__main__": instan...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 21`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `unreferenced_by_name: 3`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.99
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` weakref
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patterns/behavioral/chain_of_responsibility.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 43.98 | **LOC:** 124 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.208; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Connectivity (formerly Api Exposure) (63.9%), Guard Balance (formerly Safety Score) (63.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.1%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle` **(Generic / Templated Code)** (Impact: 5.7)
    * *Intent:* """ Handle request and stop. If can't - call next handler in chain. As an alternative you might even...
  * `check_range` **(Generic / Templated Code)** (Impact: 3.8)
  * `check_range` **(Generic / Templated Code)** (Impact: 3.7)
  * `check_range` **(Generic / Templated Code)** (Impact: 3.1)
  * `check_range` **(Generic / Templated Code)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 27`, `args: 9`, `func_start: 9`, `class_start: 5`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 14`, `import: 3`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.208
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012987
  * `Imports (Out-Degree: 0):` abc, doctest, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `patterns/creational/lazy_evaluation.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 42.44 | **LOC:** 113 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.9%), Connectivity (formerly Api Exposure) (46.9%), Complexity Load (formerly Cognitive Load) (38.1%)
- **Documentation Coverage:** 63.1579% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__get__` **(Generic / Templated Code)** (Impact: 4.3)
  * `lazy_property2` **(Stateful Encapsulated Methods)** (Impact: 3.6)
    * *Intent:* """ A lazy property decorator. The function decorated is called the first time to retrieve the resul...
  * `_lazy_property` **(Encapsulated Accessors)** (Impact: 3.0)
  * `parents` **(Generic / Templated Code)** (Impact: 3.0)
  * `__init__` **(Generic / Templated Code)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 20`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 1`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` doctest, functools, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/behavioral/servant.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 39.88 | **LOC:** 132 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Connectivity (formerly Api Exposure) (54.8%), Guard Balance (formerly Safety Score) (54.7%), Complexity Load (formerly Cognitive Load) (37.8%)
- **Documentation Coverage:** 27.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `calculate_area` **(Defensive Guards)** (Impact: 6.6)
    * *Intent:* """ Calculate the area of a given shape. Args: shape: The geometric shape whose area is to be calcul...
  * `calculate_perimeter` **(Defensive Guards)** (Impact: 6.6)
    * *Intent:* """ Calculate the perimeter of a given shape. Args: shape: The geometric shape whose perimeter is to...
  * `__init__` **(Parameter Forwarders)** (Impact: 2.4)
  * `move_to` **(Parameter Forwarders)** (Impact: 2.2)
    * *Intent:* """ Move a given shape to a new position. Args: shape: The geometric shape to be moved. new_position...
  * `__init__` **(Parameter Forwarders)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 19`, `args: 7`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 4`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` doctest, math
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/creational/pool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 39.76 | **LOC:** 95 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.1%), Connectivity (formerly Api Exposure) (44.6%), Complexity Load (formerly Cognitive Load) (34.2%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Encapsulated Accessors)** (Impact: 6.2)
  * `__exit__` **(Generic / Templated Code)** (Impact: 4.9)
  * `__enter__` **(Generic / Templated Code)** (Impact: 3.0)
  * `__del__` **(Generic / Templated Code)** (Impact: 3.0)
  * `main` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* """ >>> import queue >>> def test_object(queue): ... pool = ObjectPool(queue, True) ... print('Insid...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` doctest, queue, types, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `patterns/structural/adapter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 38.78 | **LOC:** 126 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (86.6%), Connectivity (formerly Api Exposure) (64.6%), Complexity Load (formerly Cognitive Load) (22.5%)
- **Documentation Coverage:** 52.1739% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Generic / Templated Code)** (Impact: 2.2)
    * *Intent:* """We set the adapted methods in the object's dict."""
  * `__getattr__` **(Generic / Templated Code)** (Impact: 1.9)
    * *Intent:* """All non-adapted calls are passed to the object."""
  * `make_noise` **(Generic / Templated Code)** (Impact: 1.8)
  * `original_dict` **(Generic / Templated Code)** (Impact: 1.6)
    * *Intent:* """Print original object dict."""
  * `__init__` **(Generic / Templated Code)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 26`, `args: 12`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 7`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` doctest, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/structural/test_mvc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 38.56 | **LOC:** 68 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.99; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (39.4%), Guard Balance (formerly Safety Score) (31.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.1%), Connectivity (formerly Api Exposure) (8.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_consoleview_capitalizer_and_list_and_info` **(Defensive Guards)** (Impact: 3.8)
  * `test_show_item_information_missing_calls_item_not_found` **(Defensive Guards)** (Impact: 1.8)
  * `test_productmodel_iteration_and_price_str` **(Type Conversions)** (Impact: 1.4)
  * `test_router_register_resolve_and_unknown` **(Defensive Guards)** (Impact: 1.4)
  * `test_productmodel_get_raises_keyerror` **(Type Conversions)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 24`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 5`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 14`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.99
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` patterns.structural.mvc, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/creational/test_prototype.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 36.74 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.99; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.6%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setUp` **(Parameter Forwarders)** (Impact: 1.9)
  * `test_extended_property_values_cloning` **(Callbacks & Closures)** (Impact: 1.7)
  * `test_cloning_propperty_innate_values` **(Parameter Forwarders)** (Impact: 1.6)
  * `test_cloning_propperty_assigned_values` **(Parameter Forwarders)** (Impact: 1.6)
  * `test_particular_properties_retrieving` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 13`, `args: 9`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 13`, `unreferenced_by_name: 6`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.99
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` patterns.creational.prototype, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patterns/dependency_injection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 36.42 | **LOC:** 117 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.208; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (83.6%), Connectivity (formerly Api Exposure) (57.2%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 64.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_current_time_as_html_fragment` **(Generic / Templated Code)** (Impact: 2.0)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.8)
  * `set_time_provider` **(Parameter Forwarders)** (Impact: 1.8)
  * `get_current_time_as_html_fragment` **(Generic / Templated Code)** (Impact: 1.7)
  * `get_current_time_as_html_fragment` **(Parameter Forwarders)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 27`, `args: 10`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.208
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012987
  * `Imports (Out-Degree: 0):` datetime, doctest, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `patterns/creational/abstract_factory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 34.46 | **LOC:** 100 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 18.699; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (73.7%), Connectivity (formerly Api Exposure) (60.9%), Complexity Load (formerly Cognitive Load) (9.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buy_pet` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* """Creates and shows a pet using the abstract factory"""
  * `__init__` **(Generic / Templated Code)** (Impact: 1.9)
    * *Intent:* """pet_factory is our abstract factory. We can set it at will."""
  * `__init__` **(Generic / Templated Code)** (Impact: 1.8)
  * `speak` **(Generic / Templated Code)** (Impact: 1.5)
  * `__str__` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 21`, `args: 10`, `func_start: 10`, `class_start: 4`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025974
  * `Imports (Out-Degree: 0):` doctest, random, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `patterns/other/graph_search.py` -> **Debakar Roy** (100.0% isolated ownership) | Magnitude: 148.68
- `patterns/behavioral/specification.py` -> **Debakar Roy** (100.0% isolated ownership) | Magnitude: 59.66
- `patterns/other/blackboard.py` -> **justpraveen** (100.0% isolated ownership) | Magnitude: 57.72

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `patterns/behavioral/memento.py` -> **Severity: 2.464** (Embedded: 0.026 * Error Risk: 94.8548%)
- `patterns/behavioral/visitor.py` -> **Severity: 2.374** (Embedded: 0.026 * Error Risk: 91.4175%)
- `patterns/behavioral/publish_subscribe.py` -> **Severity: 2.294** (Embedded: 0.026 * Error Risk: 88.3176%)
- `patterns/structural/mvc.py` -> **Severity: 2.258** (Embedded: 0.026 * Error Risk: 86.9243%)
- `patterns/behavioral/catalog.py` -> **Severity: 2.253** (Embedded: 0.026 * Error Risk: 86.7472%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `patterns/fundamental/delegation_pattern.py` -> **Severity: 1869.9** (Blast Radius: 18.699 * Doc Risk: 100.0%)
- `patterns/other/hsm/hsm.py` -> **Severity: 1869.9** (Blast Radius: 18.699 * Doc Risk: 100.0%)
- `patterns/behavioral/strategy.py` -> **Severity: 1714.076** (Blast Radius: 18.699 * Doc Risk: 91.6667%)
- `patterns/creational/builder.py` -> **Severity: 1714.076** (Blast Radius: 18.699 * Doc Risk: 91.6667%)
- `patterns/behavioral/publish_subscribe.py` -> **Severity: 1691.814** (Blast Radius: 18.699 * Doc Risk: 90.4762%)

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
