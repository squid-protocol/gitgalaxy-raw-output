# ARCHITECTURAL_BRIEF: smmap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 13 analyzed artifact(s), 890 LOC.
- **Load-bearing artifact:** `smmap-5.0.3/smmap/mman.py` -- 4 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `smmap-5.0.3/smmap/test/test_mman.py` -- pulls in 8 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `smmap-5.0.3/smmap/mman.py` at magnitude 426.44 (structural weight, not risk).
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
| Total Artifacts | 16 |
| Analyzed Artifacts (Scanned) | 13 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 890 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1955 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.2319 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3182 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 11 | 890 | 84.6% |
| PLAINTEXT | 1 | 0 | 7.7% |
| MARKDOWN | 1 | 0 | 7.7% |

## 4.1 SOURCE ENCODINGS
All 13 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 31%, Large Core Modules (2) 31%, Parameter Forwarders Files 31%, Declarative / Non-Code 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 11 | 84.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 15.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 47.2 | 23.5 | 30.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 77.4 | 47.4 | 50.3 | 51.4 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 10.7 | 1.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 59.5 | 20.0 | 5.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.1 | 60.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7 | 6 | 1 | `smmap-5.0.3/smmap/mman.py` |
| cleanup | 9 | 5 | 2 | `smmap-5.0.3/smmap/test/test_buf.py` |
| guards | 203 | 9 | 34 | `smmap-5.0.3/smmap/test/test_mman.py` |
| danger | 14 | 4 | 2 | `smmap-5.0.3/smmap/mman.py` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 89 | 8 | 23 | `smmap-5.0.3/smmap/mman.py` |
| io | 44 | 8 | 8 | `smmap-5.0.3/smmap/test/test_mman.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 12 | 5 | 3 | `smmap-5.0.3/smmap/test/test_util.py` |
| docs | 68 | 5 | 22 | `smmap-5.0.3/smmap/mman.py` |
| debt | 4 | 3 | 1 | `smmap-5.0.3/smmap/mman.py` |
| mutation | 407 | 10 | 71 | `smmap-5.0.3/smmap/mman.py` |
| dead_code | 9 | 4 | 3 | `smmap-5.0.3/smmap/test/test_util.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.4**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `smmap-5.0.3/smmap/test/test_mman.py` (Hits: 12)
- `smmap-5.0.3/smmap/util.py` (Hits: 8)
- `smmap-5.0.3/smmap/test/test_util.py` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mman.py** (`smmap-5.0.3/smmap/mman.py`) — 4 inbound connections
2. **lib.py** (`smmap-5.0.3/smmap/test/lib.py`) — 4 inbound connections
3. **buf.py** (`smmap-5.0.3/smmap/buf.py`) — 3 inbound connections
4. **util.py** (`smmap-5.0.3/smmap/util.py`) — 3 inbound connections
5. **__init__.py** (`smmap-5.0.3/smmap/__init__.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_mman.py** (`smmap-5.0.3/smmap/test/test_mman.py`) — 8 outbound dependencies
2. **test_buf.py** (`smmap-5.0.3/smmap/test/test_buf.py`) — 7 outbound dependencies
3. **setup.py** (`smmap-5.0.3/setup.py`) — 4 outbound dependencies
4. **test_util.py** (`smmap-5.0.3/smmap/test/test_util.py`) — 4 outbound dependencies
5. **mman.py** (`smmap-5.0.3/smmap/mman.py`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_obtain_region` **(Many-Argument Workhorses)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **55.2** | LOC: 98
  * *Intent:* # bisect to find an existing region. The c++ implementation cannot # do that as it uses a linked list for regions. r = None lo = 0 hi = len(a) while l...
- `test_memman_operation` **(Defensive Guards)** (@ `smmap-5.0.3/smmap/test/test_mman.py`) -> Impact: **27.7** | LOC: 129
  * *Intent:* # END for each manasger type # test more access, force it to actually unmap regions with FileCreator(self.k_window_test_size, "manager_operation_test"...
- `test_basics` **(Defensive Guards)** (@ `smmap-5.0.3/smmap/test/test_buf.py`) -> Impact: **20.7** | LOC: 102
- `use_region` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **19.8** | LOC: 39
  * *Intent:* """Assure we point to a window which allows access to the given offset into the file :param offset: absolute offset in bytes into the file :param size...
- `__getslice__` **(Many-Argument Workhorses)** (@ `smmap-5.0.3/smmap/buf.py`) -> Impact: **19.6** | LOC: 33
- `_collect_lru_region` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **17.6** | LOC: 40
  * *Intent:* # END handle max memory size #{ Internal Methods """Unmap the region which was least-recently used and has no client :param size: size of the region w...
- `begin_access` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/buf.py`) -> Impact: **16.0** | LOC: 27
  * *Intent:* # END fast or slow path #{ Interface """Call this before the first use of this instance. The method was already called by the constructor in case suff...
- `_obtain_region` **(Many-Argument Workhorses)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **15.1** | LOC: 37
  * *Intent:* """Utility to create a new region - for more information on the parameters, see MapCursor.use_region. :param a: A regions (a)rray :return: The newly c...
- `test_window` **(Defensive Guards)** (@ `smmap-5.0.3/smmap/test/test_util.py`) -> Impact: **13.5** | LOC: 43
- `__init__` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **12.8** | LOC: 32
  * *Intent:* """initialize the manager with the given parameters. :param window_size: if -1, a default window size will be chosen depending on the operating system...

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `smmap-5.0.3/smmap` | 4 | 730.68 | 38.24% | 2.67% |
| `smmap-5.0.3/smmap/test` | 6 | 307.58 | 16.12% | 0.0% |
| `smmap-5.0.3` | 3 | 24.64 | 3.09% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `smmap-5.0.3/smmap/mman.py` -> **10.6646%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `smmap-5.0.3/smmap/buf.py` -> **100.0%** Exposure
- `smmap-5.0.3/smmap/mman.py` -> **100.0%** Exposure
- `smmap-5.0.3/smmap/util.py` -> **100.0%** Exposure
- `smmap-5.0.3/smmap/__init__.py` -> **99.8341%** Exposure
- `smmap-5.0.3/setup.py` -> **91.6827%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `smmap-5.0.3/smmap/test/test_util.py` -> **4** Orphaned Functions | **0** Duplicates
- `smmap-5.0.3/smmap/test/test_mman.py` -> **3** Orphaned Functions | **0** Duplicates
- `smmap-5.0.3/smmap/test/test_buf.py` -> **1** Orphaned Functions | **0** Duplicates
- `smmap-5.0.3/smmap/test/test_tutorial.py` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `31` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `smmap-5.0.3/smmap/mman.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.374)
- **Top Global Matches:** file_cluster_12: 6.374, file_cluster_16: 7.794, file_cluster_15: 7.814
- **Magnitude:** 426.44 | **LOC:** 589 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 122.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 13.4328% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_obtain_region` **(Many-Argument Workhorses)** (Impact: 55.2)
    * *Intent:* # bisect to find an existing region. The c++ implementation cannot # do that as it uses a linked lis...
  * `use_region` **(Stateful Encapsulated Methods)** (Impact: 19.8)
    * *Intent:* """Assure we point to a window which allows access to the given offset into the file :param offset: ...
  * `_collect_lru_region` **(Stateful Encapsulated Methods)** (Impact: 17.6)
    * *Intent:* # END handle max memory size #{ Internal Methods """Unmap the region which was least-recently used a...
  * `_obtain_region` **(Many-Argument Workhorses)** (Impact: 15.1)
    * *Intent:* """Utility to create a new region - for more information on the parameters, see MapCursor.use_region...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 12.8)
    * *Intent:* """initialize the manager with the given parameters. :param window_size: if -1, a default window siz...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 87`, `args: 38`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 78`, `planned_debt: 2`
* *Architecture:* `io: 4`, `api: 33`, `import: 3`
* *Defense:* `safety: 7`, `doc: 36`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 122.57
  * `Choke Point (Betweenness):` 0.030303 | `Ripple Effect (Closeness):` 0.347222
  * `Imports (Out-Degree: 1):` .util, functools, sys
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `smmap-5.0.3/smmap/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.645)
- **Top Global Matches:** file_cluster_15: 5.645, file_cluster_16: 6.466, file_cluster_11: 6.782
- **Magnitude:** 141.86 | **LOC:** 223 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 184.87; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.7%), Connectivity (formerly Api Exposure) (53.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 21.7391% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 11.7)
    * *Intent:* #{ Configuration #} END configuration """Initialize a region, allocate the memory map :param path_or...
  * `increment_client_count` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* """Adjust the usage count by the given positive or negative offset. If usage count equals 0, we will...
  * `file_size` **(Encapsulated Accessors)** (Impact: 6.2)
    * *Intent:* """:return: size of file we manager"""
  * `align_to_mmap` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* #{ Utilities """ Align the given integer number to the closest page offset, which usually is 4096 by...
  * `extend_left_to` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* """Adjust the offset to start where the given window on our left ends if possible, but don't make yo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 52`, `args: 24`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `io: 8`, `api: 23`, `import: 4`
* *Defense:* `safety: 6`, `doc: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 184.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.340278
  * `Imports (Out-Degree: 0):` mmap, os, sys
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `smmap-5.0.3/smmap/buf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.538)
- **Top Global Matches:** file_cluster_16: 6.538, file_cluster_15: 6.838, file_cluster_11: 8.9
- **Magnitude:** 137.74 | **LOC:** 144 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 109.188; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__getslice__` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `begin_access` **(Stateful Encapsulated Methods)** (Impact: 16.0)
    * *Intent:* # END fast or slow path #{ Interface """Call this before the first use of this instance. The method ...
  * `__getitem__` **(Defensive Guards)** (Impact: 10.9)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 8.1)
    * *Intent:* """Initialize the instance to operate on the given cursor. :param cursor: if not None, the associate...
  * `end_access` **(Encapsulated Accessors)** (Impact: 3.3)
    * *Intent:* """Call this method once you are done using the instance. It is automatically called on destruction,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 24`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `io: 3`, `api: 11`, `import: 1`
* *Defense:* `safety: 5`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 109.188
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.266667
  * `Imports (Out-Degree: 0):` sys
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `smmap-5.0.3/smmap/test/test_mman.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.804)
- **Top Global Matches:** file_cluster_9: 6.804, file_cluster_15: 9.787, file_cluster_16: 10.207
- **Magnitude:** 120.2 | **LOC:** 225 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 47.23; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (31.6%), Guard Balance (formerly Safety Score) (30.5%), Connectivity (formerly Api Exposure) (5.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_memman_operation` **(Defensive Guards)** (Impact: 27.7)
    * *Intent:* # END for each manasger type # test more access, force it to actually unmap regions with FileCreator...
  * `test_memory_manager` **(Defensive Guards)** (Impact: 10.7)
  * `test_cursor` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 94`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 35`, `unreferenced_by_name: 3`
* *Architecture:* `io: 12`, `api: 4`, `import: 8`
* *Defense:* `safety: 69`, `test: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .lib, copy, os, random, smmap.mman, smmap.util, sys, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/smmap/test/test_buf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.943)
- **Top Global Matches:** file_cluster_9: 6.943, file_cluster_15: 12.629, file_cluster_16: 12.798
- **Magnitude:** 71.46 | **LOC:** 127 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 47.23; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.1%), Complexity Load (formerly Cognitive Load) (30.6%), Connectivity (formerly Api Exposure) (4.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_basics` **(Defensive Guards)** (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 49`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 2`, `import: 7`
* *Defense:* `safety: 24`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .lib, os, random, smmap.buf, smmap.mman, sys, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/smmap/test/test_util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.534)
- **Top Global Matches:** file_cluster_9: 7.534, file_cluster_15: 8.682, file_cluster_16: 9.321
- **Magnitude:** 66.6 | **LOC:** 106 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 47.23; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.5%), Guard Balance (formerly Safety Score) (32.4%), Connectivity (formerly Api Exposure) (7.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_window` **(Defensive Guards)** (Impact: 13.5)
  * `test_region` **(Defensive Guards)** (Impact: 12.6)
  * `test_region_list` **(Defensive Guards)** (Impact: 3.4)
  * `test_util` **(Defensive Guards)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 42`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 4`
* *Architecture:* `io: 7`, `api: 5`, `import: 4`
* *Defense:* `safety: 30`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .lib, os, smmap.util, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/smmap/test/lib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.75)
- **Top Global Matches:** file_cluster_7: 7.75, file_cluster_12: 8.455, file_cluster_5: 9.8
- **Magnitude:** 28.28 | **LOC:** 73 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 110.125; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (59.5%), Guard Balance (formerly Safety Score) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Encapsulated Accessors)** (Impact: 2.5)
  * `__exit__` **(Parameter Forwarders)** (Impact: 2.3)
  * `__del__` **(Defensive Guards)** (Impact: 1.7)
  * `setUpAll` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* #} END configuration #{ Overrides # nothing for now pass # END overrides #{ Interface #} END interfa...
  * `__enter__` **(Parameter Forwarders)** (Impact: 1.5)
    * *Intent:* # END exception handling
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `io: 2`, `api: 9`, `import: 3`
* *Defense:* `safety: 4`, `doc: 3`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 110.125
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.333333
  * `Imports (Out-Degree: 0):` os, tempfile, unittest
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `smmap-5.0.3/smmap/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 5.146)
- **Top Global Matches:** file_cluster_14: 5.146, file_cluster_7: 7.9, file_cluster_5: 11.825
- **Magnitude:** 24.64 | **LOC:** 12 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 95.405; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (61.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (19.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 95.405
  * `Choke Point (Betweenness):` 0.022727 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 2):` .buf, .mman
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `smmap-5.0.3/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.912)
- **Top Global Matches:** file_cluster_2: 2.912, file_cluster_17: 4.754, file_cluster_13: 5.51
- **Magnitude:** 21.96 | **LOC:** 53 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 47.23; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (9.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ez_setup, os, setuptools, smmap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/smmap/test/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/smmap/test/test_tutorial.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.747)
- **Top Global Matches:** file_cluster_15: 7.747, file_cluster_2: 7.904, file_cluster_11: 8.058
- **Magnitude:** 10.52 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 47.23; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (32.2%), Connectivity (formerly Api Exposure) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_example` **(Defensive Guards)** (Impact: 4.9)
    * *Intent:* # Memory Managers ################## import smmap # This instance should be globally available in yo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 14`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .lib, smmap, smmap.test.lib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.68 | **LOC:** 84 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 47.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `smmap-5.0.3/smmap/mman.py` -> **Severity: 3.03** (Bridge: 0.0303 * Flux: 100.0%)
- `smmap-5.0.3/smmap/__init__.py` -> **Severity: 2.269** (Bridge: 0.0227 * Flux: 99.8341%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `smmap-5.0.3/smmap/mman.py` -> **Severity: 26.881** (Embedded: 0.3472 * Error Risk: 77.4178%)
- `smmap-5.0.3/smmap/util.py` -> **Severity: 21.343** (Embedded: 0.3403 * Error Risk: 62.7218%)
- `smmap-5.0.3/smmap/buf.py` -> **Severity: 19.698** (Embedded: 0.2667 * Error Risk: 73.8682%)
- `smmap-5.0.3/smmap/test/lib.py` -> **Severity: 16.762** (Embedded: 0.3333 * Error Risk: 50.2857%)
- `smmap-5.0.3/smmap/__init__.py` -> **Severity: 10.296** (Embedded: 0.1667 * Error Risk: 61.7748%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `smmap-5.0.3/smmap/test/lib.py` -> **Severity: 11012.5** (Blast Radius: 110.125 * Doc Risk: 100.0%)
- `smmap-5.0.3/smmap/buf.py` -> **Severity: 6551.28** (Blast Radius: 109.188 * Doc Risk: 60.0%)
- `smmap-5.0.3/smmap/test/test_buf.py` -> **Severity: 4723.0** (Blast Radius: 47.23 * Doc Risk: 100.0%)
- `smmap-5.0.3/smmap/test/test_mman.py` -> **Severity: 4723.0** (Blast Radius: 47.23 * Doc Risk: 100.0%)
- `smmap-5.0.3/smmap/test/test_tutorial.py` -> **Severity: 4723.0** (Blast Radius: 47.23 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 268 call pairs -- scoped 48.9%, unique 0.0%, ambiguous 12.3%, external 38.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 268 | 48.9% | 0.0% | 12.3% | 38.8% |

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
