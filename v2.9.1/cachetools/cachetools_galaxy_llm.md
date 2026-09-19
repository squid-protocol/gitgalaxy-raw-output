# ARCHITECTURAL_BRIEF: cachetools
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
- **Scope:** 20 analyzed artifact(s), 3401 LOC.
- **Load-bearing artifact:** `cachetools-7.0.5/src/cachetools/keys.py` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `cachetools-7.0.5/src/cachetools/__init__.py` -- pulls in 9 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cachetools-7.0.5/src/cachetools/__init__.py` at magnitude 818.28 (structural weight, not risk).
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
| Total Artifacts | 27 |
| Analyzed Artifacts (Scanned) | 20 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 3401 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 74.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.64 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6667 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 19 | 3401 | 95.0% |
| PLAINTEXT | 1 | 0 | 5.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 45%, Declarative / Non-Code 15%, Large Core Modules (3) 15%, Compute Cores Files 10%, Data / Markup / Trivial 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19 | 95.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 84.5 | 27.0 | 24.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 52.4 | 97.3 | 75.7 | 78.3 | 78.3 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 15.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 3.5 | 56.6 | 18.6 | 10.5 | 56.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 87.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 63 | 8 | 4 | `cachetools-7.0.5/tests/test_tlru.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 188 | 10 | 37 | `cachetools-7.0.5/src/cachetools/_cachedmethod.py` |
| danger | 57 | 8 | 7 | `cachetools-7.0.5/src/cachetools/__init__.py` |
| concurrency | 19 | 4 | 3 | `cachetools-7.0.5/tests/test_threading.py` |
| connectivity | 339 | 19 | 37 | `cachetools-7.0.5/tests/test_cachedmethod.py` |
| io | 1 | 1 | 0 | `cachetools-7.0.5/tests/__init__.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 5 | 2 | 0 | `cachetools-7.0.5/tests/test_ttl.py` |
| serialization | 4 | 2 | 0 | `cachetools-7.0.5/tests/__init__.py` |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 187 | 14 | 18 | `cachetools-7.0.5/tests/test_cachedmethod.py` |
| docs | 48 | 7 | 6 | `cachetools-7.0.5/src/cachetools/__init__.py` |
| debt | 35 | 4 | 6 | `cachetools-7.0.5/src/cachetools/__init__.py` |
| mutation | 1296 | 19 | 135 | `cachetools-7.0.5/src/cachetools/__init__.py` |
| dead_code | 129 | 13 | 17 | `cachetools-7.0.5/tests/test_cachedmethod.py` |
| credential | 0 | 0 | 0 | - |
| threat | 39 | 8 | 4 | `cachetools-7.0.5/src/cachetools/_cachedmethod.py` |
| ml_ai | 3 | 1 | 0 | `cachetools-7.0.5/src/cachetools/_cachedmethod.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cachetools-7.0.5/tests/__init__.py` (Hits: 1)
- `cachetools-7.0.5/MANIFEST.in` (Hits: 0)
- `cachetools-7.0.5/src/cachetools/__init__.py` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **keys.py** (`cachetools-7.0.5/src/cachetools/keys.py`) — 2 inbound connections
2. **_cached.py** (`cachetools-7.0.5/src/cachetools/_cached.py`) — 1 inbound connections
3. **_cachedmethod.py** (`cachetools-7.0.5/src/cachetools/_cachedmethod.py`) — 1 inbound connections
4. **func.py** (`cachetools-7.0.5/src/cachetools/func.py`) — 1 inbound connections
5. **MANIFEST.in** (`cachetools-7.0.5/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`cachetools-7.0.5/src/cachetools/__init__.py`) — 9 outbound dependencies
2. **test_cachedmethod.py** (`cachetools-7.0.5/tests/test_cachedmethod.py`) — 8 outbound dependencies
3. **func.py** (`cachetools-7.0.5/src/cachetools/func.py`) — 6 outbound dependencies
4. **test_cached.py** (`cachetools-7.0.5/tests/test_cached.py`) — 5 outbound dependencies
5. **test_threading.py** (`cachetools-7.0.5/tests/test_threading.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_wrapper` **(Many-Argument Workhorses)** (@ `cachetools-7.0.5/src/cachetools/_cached.py`) -> Impact: **46.5** | LOC: 31
- `_wrapper` **(Stateful Encapsulated Methods)** (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **41.0** | LOC: 27
- `__get__` **(Defensive Guards)** (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **21.9** | LOC: 39
- `__init__` **(Stateful Encapsulated Methods)** (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **17.4** | LOC: 9
- `expire` **(Stateful Encapsulated Methods)** (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **16.7** | LOC: 23
  * *Intent:* """Remove expired items from the cache and return an iterable of the expired `(key, value)` pairs. """
- `cached` **(Defensive Guards)** (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **16.1** | LOC: 29
  * *Intent:* """Decorator to wrap a function with a memoizing callable that saves results in a cache. """
- `cachedmethod` **(Defensive Guards)** (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **15.8** | LOC: 23
  * *Intent:* """Decorator to wrap a method with a memoizing callable that saves results in a cache. """
- `test_missing` **(Compute Cores)** (@ `cachetools-7.0.5/tests/__init__.py`) -> Impact: **15.6** | LOC: 58
- `__setitem__` **(Compute Cores)** (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **14.8** | LOC: 15
- `decorator` **(Defensive Guards)** (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **9.5** | LOC: 20

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cachetools-7.0.5/src/cachetools` | 5 | 1550.66 | 56.71% | 58.81% |
| `cachetools-7.0.5/tests` | 14 | 1300.16 | 16.45% | 0.0% |
| `cachetools-7.0.5` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **99.8275%** Exposure
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **99.415%** Exposure
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **94.8231%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/keys.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **99.9999%** Exposure
- `cachetools-7.0.5/src/cachetools/func.py` -> **99.022%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cachetools-7.0.5/tests/test_cachedmethod.py` -> **32** Orphaned Functions | **6** Duplicates
- `cachetools-7.0.5/tests/__init__.py` -> **20** Orphaned Functions | **0** Duplicates
- `cachetools-7.0.5/tests/test_cached.py` -> **17** Orphaned Functions | **0** Duplicates
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **0** Orphaned Functions | **12** Duplicates
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **0** Orphaned Functions | **11** Duplicates

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
- **Unknown Dependencies:** `61` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cachetools-7.0.5/src/cachetools/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 818.28 | **LOC:** 773 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 42.735; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Debt Markers (formerly Tech Debt) (94.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 76.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expire` **(Stateful Encapsulated Methods)** (Impact: 16.7)
    * *Intent:* """Remove expired items from the cache and return an iterable of the expired `(key, value)` pairs. "...
  * `cached` **(Defensive Guards)** (Impact: 16.1)
    * *Intent:* """Decorator to wrap a function with a memoizing callable that saves results in a cache. """
  * `cachedmethod` **(Defensive Guards)** (Impact: 15.8)
    * *Intent:* """Decorator to wrap a method with a memoizing callable that saves results in a cache. """
  * `__setitem__` **(Compute Cores)** (Impact: 14.8)
  * `decorator` **(Defensive Guards)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 237`, `args: 99`, `func_start: 98`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 180`, `duplicate_logic: 12`
* *Architecture:* `api: 56`, `import: 9`
* *Defense:* `safety: 30`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` , ._cached, ._cachedmethod, collections, collections.abc, functools, heapq, random...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/_cachedmethod.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 364.82 | **LOC:** 420 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 60.897; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Complexity Load (formerly Cognitive Load) (84.5%), Guard Balance (formerly Safety Score) (83.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_wrapper` **(Stateful Encapsulated Methods)** (Impact: 41.0)
  * `__get__` **(Defensive Guards)** (Impact: 21.9)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 17.4)
  * `__set_name__` **(Stateful Encapsulated Methods)** (Impact: 8.4)
  * `_condition_info` **(C Struct Operations)** (Impact: 4.9)
    * *Intent:* # At least for now, the implementation prefers clarity and performance # over ease of maintenance, t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 140`, `args: 53`, `func_start: 51`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 83`, `duplicate_logic: 11`
* *Architecture:* `api: 37`, `import: 3`
* *Defense:* `safety: 32`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.897
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` functools, warnings, weakref
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/test_cachedmethod.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 304.64 | **LOC:** 698 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (17.1%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 98.1308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_decorator_cond_info` **(I/O & Config Routines)** (Impact: 6.7)
  * `test_decorator_lock_cond_info` **(I/O & Config Routines)** (Impact: 6.7)
  * `test_decorator_lock_info` **(I/O & Config Routines)** (Impact: 6.3)
  * `test_decorator_info` **(I/O & Config Routines)** (Impact: 5.5)
  * `test_decorator_immutable_dict` **(Annotated & Test Methods)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 113`, `args: 81`, `func_start: 55`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`, `duplicate_logic: 6`, `unreferenced_by_name: 32`
* *Architecture:* `api: 62`, `import: 8`
* *Defense:* `safety: 4`, `doc: 1`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cachetools, fractions, gc, unittest, unittest.mock, warnings, weakref
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/_cached.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 232.16 | **LOC:** 260 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 60.897; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.4%), Guard Balance (formerly Safety Score) (87.3%), Complexity Load (formerly Cognitive Load) (82.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_wrapper` **(Many-Argument Workhorses)** (Impact: 46.5)
  * `_condition_info` **(Many-Argument Workhorses)** (Impact: 4.7)
    * *Intent:* # At least for now, the implementation prefers clarity and performance # over ease of maintenance, t...
  * `_locked_info` **(Stateful Encapsulated Methods)** (Impact: 4.2)
  * `_condition` **(Stateful Encapsulated Methods)** (Impact: 4.0)
  * `_unlocked_info` **(Stateful Encapsulated Methods)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 85`, `args: 31`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 74`, `duplicate_logic: 6`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `safety: 28`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.897
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` functools
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 191.16 | **LOC:** 384 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (85.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (31.2%), Connectivity (formerly Api Exposure) (10.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_missing` **(Compute Cores)** (Impact: 15.6)
  * `test_pickle` **(Compute Cores)** (Impact: 6.9)
  * `test_insert` **(Compute Cores)** (Impact: 6.5)
  * `test_pickle_maxsize` **(Compute Cores)** (Impact: 4.8)
  * `_test_getsizeof` **(Stateful Encapsulated Methods)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 54`, `args: 29`, `func_start: 26`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 67`, `unreferenced_by_name: 20`
* *Architecture:* `io: 1`, `api: 25`, `import: 4`
* *Defense:* `safety: 4`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pickle, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_cached.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 176.58 | **LOC:** 399 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 42.735; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (17.9%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `func` **(Defensive Guards)** (Impact: 6.3)
  * `test_decorator_typed` **(I/O & Config Routines)** (Impact: 2.9)
  * `test_decorator` **(I/O & Config Routines)** (Impact: 2.7)
  * `test_decorator_lock_condition_info` **(I/O & Config Routines)** (Impact: 2.7)
  * `test_decorator_lock_info` **(I/O & Config Routines)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 45`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `state_mutation: 65`, `unreferenced_by_name: 17`
* *Architecture:* `api: 35`, `import: 5`
* *Defense:* `safety: 1`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , cachetools, cachetools.keys, unittest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_tlru.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 127.04 | **LOC:** 330 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (78.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (27.0%), Connectivity (formerly Api Exposure) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_ttu` **(Type Conversions)** (Impact: 5.2)
  * `test_ttu_heap_cleanup` **(I/O & Config Routines)** (Impact: 4.2)
  * `test_ttu_expire` **(Type Conversions)** (Impact: 3.9)
  * `__call__` **(Parameter Forwarders)** (Impact: 3.0)
  * `test_ttu_lru` **(I/O & Config Routines)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 33`, `args: 23`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `state_mutation: 59`, `unreferenced_by_name: 10`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cachetools, math, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_ttl.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 92.52 | **LOC:** 246 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (24.0%), Connectivity (formerly Api Exposure) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_ttl` **(Type Conversions)** (Impact: 4.2)
  * `test_ttl_expire` **(Type Conversions)** (Impact: 3.9)
  * `__call__` **(Parameter Forwarders)** (Impact: 3.0)
  * `test_ttl_lru` **(I/O & Config Routines)** (Impact: 2.8)
  * `test_ttl_clear` **(I/O & Config Routines)** (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 32`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 46`, `unreferenced_by_name: 9`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cachetools, datetime, math, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_classmethod.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 82.42 | **LOC:** 152 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Guard Balance (formerly Safety Score) (70.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (10.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(Parameter Forwarders)** (Impact: 2.7)
  * `test_typed` **(Parameter Forwarders)** (Impact: 2.6)
  * `test_locked` **(Parameter Forwarders)** (Impact: 2.0)
  * `test_condition` **(Parameter Forwarders)** (Impact: 2.0)
  * `test_clear` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 35`, `args: 17`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 26`, `unreferenced_by_name: 7`
* *Architecture:* `api: 13`, `concurrency: 3`, `import: 4`
* *Defense:* `test: 9`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cachetools, threading, unittest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/func.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 76.44 | **LOC:** 106 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 79.06; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ttl_cache` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* """Decorator to wrap a function with a memoizing callable that saves up to `maxsize` results based o...
  * `rr_cache` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* """Decorator to wrap a function with a memoizing callable that saves up to `maxsize` results based o...
  * `fifo_cache` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* """Decorator to wrap a function with a memoizing callable that saves up to `maxsize` results based o...
  * `lfu_cache` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* """Decorator to wrap a function with a memoizing callable that saves up to `maxsize` results based o...
  * `lru_cache` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* """Decorator to wrap a function with a memoizing callable that saves up to `maxsize` results based o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 40`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 8`
* *Defense:* `doc: 6`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 79.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` , functools, math, random, threading, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/test_threading.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 67.52 | **LOC:** 63 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (78.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_cached_stampede` **(Compute Cores)** (Impact: 6.3)
  * `test_cachedmethod_stampede` **(Compute Cores)** (Impact: 6.3)
  * `func` **(Defensive Guards)** (Impact: 3.4)
  * `meth` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `concurrency: 5`, `import: 5`
* *Defense:* `safety: 1`, `test: 6`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cachetools, os, threading, time, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/keys.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 58.96 | **LOC:** 67 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 115.385; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (46.2%)
- **Documentation Coverage:** 46.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `typedkey` **(Type Conversions)** (Impact: 9.2)
    * *Intent:* """Return a typed cache key for the specified hashable arguments."""
  * `hashkey` **(Type Conversions)** (Impact: 5.5)
    * *Intent:* """Return a cache key for the specified hashable arguments."""
  * `__hash__` **(Encapsulated Accessors)** (Impact: 3.7)
  * `__add__` **(Parameter Forwarders)** (Impact: 2.1)
  * `__radd__` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 20`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 8`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 115.385
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.105263
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/test_func.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 57.72 | **LOC:** 125 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 42.735; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (12.4%), Connectivity (formerly Api Exposure) (10.7%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_decorator_needs_rlock` **(C Struct Operations)** (Impact: 4.2)
    * *Intent:* """This will deadlock on a cache that uses a regular lock. https://github.com/python/cpython/blob/3....
  * `__eq__` **(Parameter Forwarders)** (Impact: 3.8)
  * `decorator` **(Parameter Forwarders)** (Impact: 2.1)
  * `test_decorator_typed` **(Callbacks & Closures)** (Impact: 2.0)
  * `test_decorator` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 23`, `args: 18`, `func_start: 11`, `class_start: 7`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 10`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `doc: 1`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cachetools.func, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_lfu.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 45.7 | **LOC:** 91 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.2%), Connectivity (formerly Api Exposure) (7.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_lfu` **(I/O & Config Routines)** (Impact: 5.3)
  * `test_lfu_clear` **(I/O & Config Routines)** (Impact: 2.6)
  * `test_lfu_getsizeof` **(Callbacks & Closures)** (Impact: 2.5)
  * `test_lfu_update_existing` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 11`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 4`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cachetools, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_rr.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 42.64 | **LOC:** 89 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (9.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_rr` **(I/O & Config Routines)** (Impact: 2.6)
  * `test_rr_getsizeof` **(Callbacks & Closures)** (Impact: 2.5)
  * `test_rr_bad_choice` **(Parameter Forwarders)** (Impact: 2.1)
  * `test_rr_update_existing` **(Parameter Forwarders)** (Impact: 2.0)
  * `test_rr_default_choice` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cachetools, random, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_lru.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 39.8 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (81.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_lru` **(I/O & Config Routines)** (Impact: 2.6)
  * `test_lru_getsizeof` **(Callbacks & Closures)** (Impact: 2.5)
  * `test_lru_clear` **(I/O & Config Routines)** (Impact: 2.4)
  * `test_lru_update_existing` **(Parameter Forwarders)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 4`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cachetools, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_fifo.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 29.1 | **LOC:** 69 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (78.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_fifo` **(I/O & Config Routines)** (Impact: 2.6)
  * `test_fifo_getsizeof` **(Callbacks & Closures)** (Impact: 2.5)
  * `test_fifo_update_existing` **(Parameter Forwarders)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cachetools, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_keys.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 28.72 | **LOC:** 93 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 42.735; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.5%), Connectivity (formerly Api Exposure) (9.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pickle` **(Compute Cores)** (Impact: 4.1)
  * `test_methodkey` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* # similar to hashkey(), but ignores its first positional argument self.assertEqual(key("x"), key("y"...
  * `test_hashkey` **(Parameter Forwarders)** (Impact: 2.5)
  * `test_typedkey` **(Parameter Forwarders)** (Impact: 2.5)
  * `test_typedmethodkey` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* # similar to typedkey(), but ignores its first positional argument self.assertEqual(key("x"), key("y...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 17`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cachetools.keys, pickle, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 14.6 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 42.735; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cachetools, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
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

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cachetools-7.0.5/src/cachetools/keys.py` -> **Severity: 9.404** (Embedded: 0.1053 * Error Risk: 89.3377%)
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **Severity: 4.597** (Embedded: 0.0526 * Error Risk: 87.3453%)
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **Severity: 4.387** (Embedded: 0.0526 * Error Risk: 83.3511%)
- `cachetools-7.0.5/src/cachetools/func.py` -> **Severity: 3.845** (Embedded: 0.0526 * Error Risk: 73.0548%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cachetools-7.0.5/src/cachetools/_cached.py` -> **Severity: 6089.7** (Blast Radius: 60.897 * Doc Risk: 100.0%)
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **Severity: 6089.7** (Blast Radius: 60.897 * Doc Risk: 100.0%)
- `cachetools-7.0.5/src/cachetools/keys.py` -> **Severity: 5384.637** (Blast Radius: 115.385 * Doc Risk: 46.6667%)
- `cachetools-7.0.5/tests/__init__.py` -> **Severity: 4273.5** (Blast Radius: 42.735 * Doc Risk: 100.0%)
- `cachetools-7.0.5/tests/test_cached.py` -> **Severity: 4273.5** (Blast Radius: 42.735 * Doc Risk: 100.0%)

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
