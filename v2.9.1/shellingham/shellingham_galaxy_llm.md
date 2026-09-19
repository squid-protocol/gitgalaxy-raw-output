# ARCHITECTURAL_BRIEF: shellingham
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
- **Scope:** 10 analyzed artifact(s), 361 LOC.
- **Load-bearing artifact:** `shellingham-1.5.4/src/shellingham/_core.py` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `shellingham-1.5.4/src/shellingham/nt.py` -- pulls in 5 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `shellingham-1.5.4/src/shellingham/nt.py` at magnitude 117.24 (structural weight, not risk).
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
| Total Artifacts | 15 |
| Analyzed Artifacts (Scanned) | 10 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 361 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 9 | 361 | 90.0% |
| PLAINTEXT | 1 | 0 | 10.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Large Core Modules (2) 30%, Encapsulated Accessors Files 20%, Declarative / Non-Code 10%, Type Conversions Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9 | 90.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 10.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 58.9 | 26.9 | 37.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.3 | 71.0 | 72.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 30.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.6 | 2.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 23.9 | 7.1 | 2.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 59.3 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 38.3 | 16.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10 | 5 | 3 | `shellingham-1.5.4/src/shellingham/posix/proc.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 37 | 6 | 8 | `shellingham-1.5.4/src/shellingham/nt.py` |
| danger | 17 | 7 | 3 | `shellingham-1.5.4/src/shellingham/posix/ps.py` |
| concurrency | 4 | 3 | 1 | `shellingham-1.5.4/src/shellingham/nt.py` |
| connectivity | 17 | 7 | 4 | `shellingham-1.5.4/tests/test_posix.py` |
| io | 19 | 5 | 6 | `shellingham-1.5.4/src/shellingham/posix/proc.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 1 | 0 | `shellingham-1.5.4/src/shellingham/posix/ps.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 3 | 2 | 1 | `shellingham-1.5.4/src/shellingham/posix/__init__.py` |
| events | 0 | 0 | 0 | - |
| tests | 8 | 1 | 0 | `shellingham-1.5.4/tests/test_posix.py` |
| docs | 9 | 4 | 2 | `shellingham-1.5.4/src/shellingham/posix/__init__.py` |
| debt | 2 | 2 | 1 | `shellingham-1.5.4/src/shellingham/posix/proc.py` |
| mutation | 177 | 8 | 29 | `shellingham-1.5.4/src/shellingham/nt.py` |
| dead_code | 6 | 5 | 1 | `shellingham-1.5.4/tests/test_posix.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 1 | 1 | 0 | `shellingham-1.5.4/src/shellingham/_core.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.125**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `shellingham-1.5.4/src/shellingham/posix/proc.py` (Hits: 9)
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` (Hits: 6)
- `shellingham-1.5.4/src/shellingham/posix/ps.py` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_core.py** (`shellingham-1.5.4/src/shellingham/_core.py`) — 1 inbound connections
2. **_core.py** (`shellingham-1.5.4/src/shellingham/posix/_core.py`) — 1 inbound connections
3. **MANIFEST.in** (`shellingham-1.5.4/MANIFEST.in`) — 0 inbound connections
4. **setup.py** (`shellingham-1.5.4/setup.py`) — 0 inbound connections
5. **__init__.py** (`shellingham-1.5.4/src/shellingham/__init__.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **nt.py** (`shellingham-1.5.4/src/shellingham/nt.py`) — 5 outbound dependencies
2. **proc.py** (`shellingham-1.5.4/src/shellingham/posix/proc.py`) — 5 outbound dependencies
3. **__init__.py** (`shellingham-1.5.4/src/shellingham/posix/__init__.py`) — 4 outbound dependencies
4. **ps.py** (`shellingham-1.5.4/src/shellingham/posix/ps.py`) — 4 outbound dependencies
5. **test_posix.py** (`shellingham-1.5.4/tests/test_posix.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `iter_process_parents` **(Defensive Guards)** (@ `shellingham-1.5.4/src/shellingham/posix/ps.py`) -> Impact: **15.9** | LOC: 40
  * *Intent:* """Try to look up the process tree via the output of `ps`."""
- `_get_interpreter_shell` **(Stateful Encapsulated Methods)** (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> Impact: **13.0** | LOC: 18
  * *Intent:* """Get shell invoked via an interpreter. Some shells are implemented on, and invoked with an interpreter, e.g. xonsh is commonly executed with an exec...
- `get_shell` **(Defensive Guards)** (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> Impact: **12.0** | LOC: 32
- `_get_shell` **(Stateful Encapsulated Methods)** (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> Impact: **11.2** | LOC: 16
- `detect_shell` **(Defensive Guards)** (@ `shellingham-1.5.4/src/shellingham/__init__.py`) -> Impact: **7.7** | LOC: 15
- `get_shell` **(Type Conversions)** (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> Impact: **7.3** | LOC: 8
  * *Intent:* """Get the shell that the supplied pid or os.getpid() is running in."""
- `check` **(Compute Cores)** (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> Impact: **6.3** | LOC: 7
- `iter_process_parents` **(Stateful Encapsulated Methods)** (@ `shellingham-1.5.4/src/shellingham/posix/proc.py`) -> Impact: **6.0** | LOC: 17
  * *Intent:* """Try to look up the process tree via the /proc interface."""
- `_iter_process_parents` **(Stateful Encapsulated Methods)** (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> Impact: **5.8** | LOC: 13
  * *Intent:* """Select a way to obtain process information from the system. * `/proc` is used if supported. * The system `ps` utility is used as a fallback option....
- `_iter_process_parents` **(Stateful Encapsulated Methods)** (@ `shellingham-1.5.4/src/shellingham/posix/proc.py`) -> Impact: **5.6** | LOC: 8
  * *Intent:* # Inner generator function so we correctly throw an error eagerly if proc # is not supported, rather than on the first call to the iterator. This # al...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Stateful Encapsulated Methods**: n/a
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `shellingham-1.5.4/src/shellingham/posix` | 4 | 201.28 | 31.74% | 63.25% |
| `shellingham-1.5.4/src/shellingham` | 3 | 157.0 | 32.07% | 7.31% |
| `shellingham-1.5.4/tests` | 1 | 44.2 | 18.69% | 0.0% |
| `shellingham-1.5.4` | 2 | 12.04 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **99.8499%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/ps.py` -> **99.8499%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **53.2847%** Exposure
- `shellingham-1.5.4/src/shellingham/nt.py` -> **21.9173%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `shellingham-1.5.4/src/shellingham/nt.py` -> **100.0%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **100.0%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **100.0%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/ps.py` -> **100.0%** Exposure
- `shellingham-1.5.4/src/shellingham/__init__.py` -> **99.9849%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `shellingham-1.5.4/tests/test_posix.py` -> **2** Orphaned Functions | **0** Duplicates
- `shellingham-1.5.4/src/shellingham/nt.py` -> **1** Orphaned Functions | **0** Duplicates
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **1** Orphaned Functions | **0** Duplicates
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **1** Orphaned Functions | **0** Duplicates
- `shellingham-1.5.4/src/shellingham/posix/ps.py` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `22` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `shellingham-1.5.4/src/shellingham/nt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 117.24 | **LOC:** 164 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 85.47; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Complexity Load (formerly Cognitive Load) (58.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_shell` **(Defensive Guards)** (Impact: 12.0)
  * `check` **(Compute Cores)** (Impact: 6.3)
  * `_check_expected` **(Encapsulated Accessors)** (Impact: 4.7)
  * `_get_full_path` **(Encapsulated Accessors)** (Impact: 4.6)
  * `check` **(Parameter Forwarders)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 30`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 41`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 5`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` contextlib, ctypes, ctypes.wintypes, os, shellingham._core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/posix/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 86.04 | **LOC:** 113 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Debt Markers (formerly Tech Debt) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_interpreter_shell` **(Stateful Encapsulated Methods)** (Impact: 13.0)
    * *Intent:* """Get shell invoked via an interpreter. Some shells are implemented on, and invoked with an interpr...
  * `_get_shell` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `get_shell` **(Type Conversions)** (Impact: 7.3)
    * *Intent:* """Get the shell that the supplied pid or os.getpid() is running in."""
  * `_iter_process_parents` **(Stateful Encapsulated Methods)** (Impact: 5.8)
    * *Intent:* """Select a way to obtain process information from the system. * `/proc` is used if supported. * The...
  * `_get_login_shell` **(Encapsulated Accessors)** (Impact: 4.6)
    * *Intent:* """Form shell information from SHELL environ if possible."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 23`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 1`, `import: 4`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , .._core, os, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/posix/proc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 61.58 | **LOC:** 84 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (97.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iter_process_parents` **(Stateful Encapsulated Methods)** (Impact: 6.0)
    * *Intent:* """Try to look up the process tree via the /proc interface."""
  * `_iter_process_parents` **(Stateful Encapsulated Methods)** (Impact: 5.6)
    * *Intent:* # Inner generator function so we correctly throw an error eagerly if proc # is not supported, rather...
  * `_get_ppid` **(Encapsulated Accessors)** (Impact: 3.9)
  * `detect_proc` **(I/O & Config Routines)** (Impact: 3.7)
    * *Intent:* """Detect /proc filesystem style. This checks the /proc/{pid} directory for possible formats. Return...
  * `_get_cmdline` **(Encapsulated Accessors)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 26`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 9`, `api: 3`, `import: 5`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ._core, io, os, re, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/tests/test_posix.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 44.2 | **LOC:** 86 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 85.47; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (72.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (18.7%), Connectivity (formerly Api Exposure) (8.0%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patch` **(Compute Cores)** (Impact: 5.5)
  * `unpatch` **(Defensive Guards)** (Impact: 4.6)
  * `test_get_shell` **(Defensive Guards)** (Impact: 2.4)
  * `environ` **(Parameter Forwarders)** (Impact: 1.7)
    * *Intent:* """Provide environment variable override, and restore on finalize. """
  * `__init__` **(Type Conversions)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 3`, `doc: 1`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, pytest, shellingham, shellingham.posix._core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/posix/ps.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 41.62 | **LOC:** 52 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (80.8%), Complexity Load (formerly Cognitive Load) (50.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iter_process_parents` **(Defensive Guards)** (Impact: 15.9)
    * *Intent:* """Try to look up the process tree via the output of `ps`."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 2`, `import: 4`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ._core, errno, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 23.08 | **LOC:** 24 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `detect_shell` **(Defensive Guards)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 1`, `api: 1`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ._core, importlib, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/_core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 16.68 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 158.12; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (23.9%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 158.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `shellingham-1.5.4/src/shellingham/posix/_core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 12.04 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 158.12; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 158.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` collections
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `shellingham-1.5.4/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
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

- `shellingham-1.5.4/src/shellingham/_core.py` -> **Severity: 7.389** (Embedded: 0.1111 * Error Risk: 66.5013%)
- `shellingham-1.5.4/src/shellingham/posix/_core.py` -> **Severity: 6.728** (Embedded: 0.1111 * Error Risk: 60.5532%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `shellingham-1.5.4/src/shellingham/__init__.py` -> **Severity: 8547.0** (Blast Radius: 85.47 * Doc Risk: 100.0%)
- `shellingham-1.5.4/src/shellingham/nt.py` -> **Severity: 8547.0** (Blast Radius: 85.47 * Doc Risk: 100.0%)
- `shellingham-1.5.4/tests/test_posix.py` -> **Severity: 6647.669** (Blast Radius: 85.47 * Doc Risk: 77.7778%)
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **Severity: 4273.5** (Blast Radius: 85.47 * Doc Risk: 50.0%)
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **Severity: 1424.503** (Blast Radius: 85.47 * Doc Risk: 16.6667%)

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
