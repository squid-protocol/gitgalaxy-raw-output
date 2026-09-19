# ARCHITECTURAL_BRIEF: smmap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 7 analyzed artifact(s), 507 LOC.
- **Load-bearing artifact:** `smmap-5.0.3/smmap/buf.py` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `smmap-5.0.3/smmap/mman.py` -- pulls in 6 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 10 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 507 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.25 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 5 | 507 | 71.4% |
| PLAINTEXT | 1 | 0 | 14.3% |
| MARKDOWN | 1 | 0 | 14.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 43%, Parameter Forwarders Files 43%, Declarative / Non-Code 14%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 5 | 71.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 28.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 9.3 | 47.2 | 32.4 | 40.5 | 9.3 |
| Guard Balance (formerly Error & Exception Exposure) | 62.6 | 97.8 | 85.5 | 85.6 | 62.6 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 12.6 | 2.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 48.9 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 48.1 | 24.9 | 34.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 91.7 | 100.0 | 98.3 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.5 | 3.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 60.0 | 19.0 | 13.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5 | 4 | 1 | `smmap-5.0.3/smmap/mman.py` |
| cleanup | 3 | 2 | 1 | `smmap-5.0.3/smmap/util.py` |
| guards | 60 | 4 | 15 | `smmap-5.0.3/smmap/mman.py` |
| danger | 12 | 3 | 2 | `smmap-5.0.3/smmap/mman.py` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 67 | 3 | 23 | `smmap-5.0.3/smmap/mman.py` |
| io | 17 | 4 | 4 | `smmap-5.0.3/smmap/util.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 65 | 4 | 22 | `smmap-5.0.3/smmap/mman.py` |
| debt | 2 | 1 | 0 | `smmap-5.0.3/smmap/mman.py` |
| mutation | 243 | 5 | 43 | `smmap-5.0.3/smmap/mman.py` |
| dead_code | 2 | 2 | 1 | `smmap-5.0.3/smmap/buf.py` |
| credential | 0 | 0 | 0 | - |
| threat | 6 | 3 | 1 | `smmap-5.0.3/smmap/util.py` |
| ml_ai | 1 | 1 | 0 | `smmap-5.0.3/smmap/__init__.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `smmap-5.0.3/smmap/util.py` (Hits: 8)
- `smmap-5.0.3/smmap/mman.py` (Hits: 4)
- `smmap-5.0.3/smmap/buf.py` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **buf.py** (`smmap-5.0.3/smmap/buf.py`) — 1 inbound connections
2. **mman.py** (`smmap-5.0.3/smmap/mman.py`) — 1 inbound connections
3. **util.py** (`smmap-5.0.3/smmap/util.py`) — 1 inbound connections
4. **MANIFEST.in** (`smmap-5.0.3/MANIFEST.in`) — 0 inbound connections
5. **README.md** (`smmap-5.0.3/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mman.py** (`smmap-5.0.3/smmap/mman.py`) — 6 outbound dependencies
2. **setup.py** (`smmap-5.0.3/setup.py`) — 4 outbound dependencies
3. **util.py** (`smmap-5.0.3/smmap/util.py`) — 3 outbound dependencies
4. **__init__.py** (`smmap-5.0.3/smmap/__init__.py`) — 2 outbound dependencies
5. **buf.py** (`smmap-5.0.3/smmap/buf.py`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_obtain_region` **(Many-Argument Workhorses)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **55.2** | LOC: 98
  * *Intent:* # bisect to find an existing region. The c++ implementation cannot # do that as it uses a linked list for regions. r = None lo = 0 hi = len(a) while l...
- `use_region` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **19.8** | LOC: 39
  * *Intent:* """Assure we point to a window which allows access to the given offset into the file :param offset: absolute offset in bytes into the file :param size...
- `__getslice__` **(Many-Argument Workhorses)** (@ `smmap-5.0.3/smmap/buf.py`) -> Impact: **19.6** | LOC: 33
- `_collect_lru_region` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **17.6** | LOC: 40
  * *Intent:* # END handle max memory size #{ Internal Methods """Unmap the region which was least-recently used and has no client :param size: size of the region w...
- `begin_access` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/buf.py`) -> Impact: **16.0** | LOC: 27
  * *Intent:* # END fast or slow path #{ Interface """Call this before the first use of this instance. The method was already called by the constructor in case suff...
- `_obtain_region` **(Many-Argument Workhorses)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **15.1** | LOC: 37
  * *Intent:* """Utility to create a new region - for more information on the parameters, see MapCursor.use_region. :param a: A regions (a)rray :return: The newly c...
- `__init__` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **12.8** | LOC: 32
  * *Intent:* """initialize the manager with the given parameters. :param window_size: if -1, a default window size will be chosen depending on the operating system...
- `__init__` **(Stateful Encapsulated Methods)** (@ `smmap-5.0.3/smmap/util.py`) -> Impact: **11.7** | LOC: 38
  * *Intent:* #{ Configuration #} END configuration """Initialize a region, allocate the memory map :param path_or_fd: path to the file to map, or the opened file d...
- `__getitem__` **(Defensive Guards)** (@ `smmap-5.0.3/smmap/buf.py`) -> Impact: **10.9** | LOC: 11
- `force_map_handle_removal_win` **(Compute Cores)** (@ `smmap-5.0.3/smmap/mman.py`) -> Impact: **10.0** | LOC: 26
  * *Intent:* #} END interface #{ Special Purpose Interface """ONLY AVAILABLE ON WINDOWS On windows removing files is not allowed if anybody still has it opened. If...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `smmap-5.0.3/smmap` | 4 | 730.68 | 38.24% | 3.15% |
| `smmap-5.0.3` | 3 | 24.64 | 3.09% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `smmap-5.0.3/smmap/mman.py` -> **12.5845%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `smmap-5.0.3/smmap/buf.py` -> **100.0%** Exposure
- `smmap-5.0.3/smmap/mman.py` -> **100.0%** Exposure
- `smmap-5.0.3/smmap/util.py` -> **100.0%** Exposure
- `smmap-5.0.3/smmap/__init__.py` -> **99.8341%** Exposure
- `smmap-5.0.3/setup.py` -> **91.6827%** Exposure

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
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `smmap-5.0.3/smmap/mman.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 426.44 | **LOC:** 589 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 157.263; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 157.263
  * `Choke Point (Betweenness):` 0.033333 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 1):` .util, functools, however, it, its, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `smmap-5.0.3/smmap/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 141.86 | **LOC:** 223 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 244.033; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Risk/State:* `state_mutation: 27`, `dead_code: 1`
* *Architecture:* `io: 8`, `api: 23`, `import: 4`
* *Defense:* `safety: 6`, `doc: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 244.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.222222
  * `Imports (Out-Degree: 0):` mmap, os, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `smmap-5.0.3/smmap/buf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 137.74 | **LOC:** 144 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 157.263; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.7%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Risk/State:* `state_mutation: 21`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 11`, `import: 1`
* *Defense:* `safety: 5`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 157.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `smmap-5.0.3/smmap/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 24.64 | **LOC:** 12 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 110.36; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (85.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (19.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 110.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .buf, .mman
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 21.96 | **LOC:** 53 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 110.36; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (62.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (9.3%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 110.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ez_setup, os, setuptools, smmap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.68 | **LOC:** 84 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 110.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smmap-5.0.3/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 110.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `smmap-5.0.3/smmap/mman.py` -> **Severity: 3.333** (Bridge: 0.0333 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `smmap-5.0.3/smmap/util.py` -> **Severity: 18.908** (Embedded: 0.2222 * Error Risk: 85.0859%)
- `smmap-5.0.3/smmap/mman.py` -> **Severity: 16.295** (Embedded: 0.1667 * Error Risk: 97.7682%)
- `smmap-5.0.3/smmap/buf.py` -> **Severity: 16.117** (Embedded: 0.1667 * Error Risk: 96.7018%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `smmap-5.0.3/smmap/buf.py` -> **Severity: 9435.78** (Blast Radius: 157.263 * Doc Risk: 60.0%)
- `smmap-5.0.3/smmap/util.py` -> **Severity: 5305.058** (Blast Radius: 244.033 * Doc Risk: 21.7391%)
- `smmap-5.0.3/smmap/mman.py` -> **Severity: 2112.482** (Blast Radius: 157.263 * Doc Risk: 13.4328%)

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
