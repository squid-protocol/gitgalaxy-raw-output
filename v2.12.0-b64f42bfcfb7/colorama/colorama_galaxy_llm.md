# ARCHITECTURAL_BRIEF: colorama
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
- **Scope:** 26 analyzed artifact(s), 1428 LOC.
- **Load-bearing artifact:** `colorama-0.4.6/colorama/initialise.py` -- 10 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `colorama-0.4.6/colorama/tests/ansitowin32_test.py` -- pulls in 9 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `colorama-0.4.6/colorama/ansitowin32.py` at magnitude 283.24 (structural weight, not risk).
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
| Total Artifacts | 31 |
| Analyzed Artifacts (Scanned) | 26 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 1428 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3336 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.3314 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6907 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 23 | 1406 | 88.5% |
| PLAINTEXT | 1 | 0 | 3.8% |
| BATCH | 1 | 11 | 3.8% |
| SHELL | 1 | 11 | 3.8% |

## 4.1 SOURCE ENCODINGS
All 26 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 31%, Declarative / Non-Code 27%, Data / Markup / Trivial 15%, Large Core Modules (3) 12%, Interface Declarations Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 25 | 96.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 3.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.5 | 19.1 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.5 | 40.4 | 51.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.9 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 76.2 | 17.2 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 51.3 | 90.5 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 17 | 4 | 1 | `colorama-0.4.6/colorama/ansi.py` |
| cleanup | 6 | 3 | 0 | `colorama-0.4.6/colorama/tests/ansitowin32_test.py` |
| guards | 39 | 7 | 5 | `colorama-0.4.6/colorama/winterm.py` |
| danger | 9 | 4 | 2 | `colorama-0.4.6/colorama/win32.py` |
| concurrency | 5 | 2 | 0 | `colorama-0.4.6/colorama/tests/utils.py` |
| connectivity | 155 | 15 | 19 | `colorama-0.4.6/colorama/tests/ansitowin32_test.py` |
| io | 96 | 13 | 6 | `colorama-0.4.6/colorama/tests/initialise_test.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 1 | 0 | `colorama-0.4.6/colorama/ansitowin32.py` |
| events | 0 | 0 | 0 | - |
| tests | 116 | 5 | 10 | `colorama-0.4.6/colorama/tests/ansitowin32_test.py` |
| docs | 9 | 5 | 1 | `colorama-0.4.6/colorama/ansitowin32.py` |
| debt | 33 | 9 | 4 | `colorama-0.4.6/demos/demo06.py` |
| mutation | 734 | 20 | 97 | `colorama-0.4.6/colorama/tests/ansitowin32_test.py` |
| dead_code | 55 | 5 | 7 | `colorama-0.4.6/colorama/tests/ansitowin32_test.py` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `colorama-0.4.6/colorama/tests/ansitowin32_test.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `colorama-0.4.6/colorama/tests/initialise_test.py` (Hits: 34)
- `colorama-0.4.6/colorama/initialise.py` (Hits: 15)
- `colorama-0.4.6/colorama/tests/utils.py` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **initialise.py** (`colorama-0.4.6/colorama/initialise.py`) — 10 inbound connections
2. **__init__.py** (`colorama-0.4.6/colorama/__init__.py`) — 9 inbound connections
3. **fixpath.py** (`colorama-0.4.6/demos/fixpath.py`) — 8 inbound connections
4. **ansitowin32.py** (`colorama-0.4.6/colorama/ansitowin32.py`) — 7 inbound connections
5. **ansi.py** (`colorama-0.4.6/colorama/ansi.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ansitowin32_test.py** (`colorama-0.4.6/colorama/tests/ansitowin32_test.py`) — 9 outbound dependencies
2. **initialise_test.py** (`colorama-0.4.6/colorama/tests/initialise_test.py`) — 7 outbound dependencies
3. **ansitowin32.py** (`colorama-0.4.6/colorama/ansitowin32.py`) — 6 outbound dependencies
4. **winterm_test.py** (`colorama-0.4.6/colorama/tests/winterm_test.py`) — 5 outbound dependencies
5. **demo06.py** (`colorama-0.4.6/demos/demo06.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `extract_params` **(Type Conversions)** (@ `colorama-0.4.6/colorama/ansitowin32.py`) -> Impact: **24.8** | LOC: 16
- `__init__` **(Many-Argument Workhorses)** (@ `colorama-0.4.6/colorama/ansitowin32.py`) -> Impact: **24.0** | LOC: 39
  * *Intent:* # The wrapped stream (normally sys.stdout or sys.stderr) self.wrapped = wrapped # should we reset colors to defaults after every .write() self.autores...
- `init` **(Many-Argument Workhorses)** (@ `colorama-0.4.6/colorama/initialise.py`) -> Impact: **19.2** | LOC: 26
- `call_win32` **(Many-Argument Workhorses)** (@ `colorama-0.4.6/colorama/ansitowin32.py`) -> Impact: **17.0** | LOC: 20
- `erase_screen` **(Many-Argument Workhorses)** (@ `colorama-0.4.6/colorama/winterm.py`) -> Impact: **15.6** | LOC: 31
  * *Intent:* # 0 should clear from the cursor to the end of the screen. # 1 should clear from the cursor to the beginning of the screen. # 2 should clear the entir...
- `convert_osc` **(Compute Cores)** (@ `colorama-0.4.6/colorama/ansitowin32.py`) -> Impact: **14.6** | LOC: 14
- `erase_line` **(Many-Argument Workhorses)** (@ `colorama-0.4.6/colorama/winterm.py`) -> Impact: **13.2** | LOC: 24
  * *Intent:* # 0 should clear from the cursor to the end of the line. # 1 should clear from the cursor to the beginning of the line. # 2 should clear the entire li...
- `testJustFixWindowsConsole` **(I/O & Config Routines)** (@ `colorama-0.4.6/colorama/tests/initialise_test.py`) -> Impact: **11.3** | LOC: 57
- `write_and_convert` **(Compute Cores)** (@ `colorama-0.4.6/colorama/ansitowin32.py`) -> Impact: **9.4** | LOC: 14
  * *Intent:* ''' Write the given text to our wrapped stream, stripping any ANSI sequences from the text, and optionally converting them into win32 calls. '''
- `fore` **(Stateful Encapsulated Methods)** (@ `colorama-0.4.6/colorama/winterm.py`) -> Impact: **9.4** | LOC: 10

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `colorama-0.4.6/colorama` | 6 | 881.98 | 58.92% | 0.0% |
| `colorama-0.4.6/colorama/tests` | 7 | 406.64 | 11.62% | 0.0% |
| `colorama-0.4.6/demos` | 12 | 142.36 | 3.46% | 0.0% |
| `colorama-0.4.6` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `colorama-0.4.6/colorama/ansi.py` -> **100.0%** Exposure
- `colorama-0.4.6/colorama/ansitowin32.py` -> **100.0%** Exposure
- `colorama-0.4.6/colorama/initialise.py` -> **100.0%** Exposure
- `colorama-0.4.6/colorama/win32.py` -> **100.0%** Exposure
- `colorama-0.4.6/colorama/winterm.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `colorama-0.4.6/colorama/tests/ansitowin32_test.py` -> **23** Orphaned Functions | **0** Duplicates
- `colorama-0.4.6/colorama/tests/initialise_test.py` -> **12** Orphaned Functions | **0** Duplicates
- `colorama-0.4.6/colorama/tests/winterm_test.py` -> **8** Orphaned Functions | **0** Duplicates
- `colorama-0.4.6/colorama/tests/isatty_test.py` -> **7** Orphaned Functions | **0** Duplicates
- `colorama-0.4.6/colorama/tests/ansi_test.py` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `63` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `colorama-0.4.6/colorama/ansitowin32.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.446)
- **Top Global Matches:** file_cluster_12: 6.446, file_cluster_15: 6.594, file_cluster_16: 8.025
- **Magnitude:** 283.24 | **LOC:** 278 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 138.344; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.4%), Connectivity (formerly Api Exposure) (69.6%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract_params` **(Type Conversions)** (Impact: 24.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* # The wrapped stream (normally sys.stdout or sys.stderr) self.wrapped = wrapped # should we reset co...
  * `call_win32` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `convert_osc` **(Compute Cores)** (Impact: 14.6)
  * `write_and_convert` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* ''' Write the given text to our wrapped stream, stripping any ANSI sequences from the text, and opti...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 46`, `args: 21`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 42`
* *Architecture:* `io: 4`, `api: 21`, `import: 6`
* *Defense:* `safety: 4`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 138.344
  * `Choke Point (Betweenness):` 0.055833 | `Ripple Effect (Closeness):` 0.391304
  * `Imports (Out-Degree: 3):` .ansi, .win32, .winterm, os, re, sys
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `colorama-0.4.6/colorama/winterm.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.913)
- **Top Global Matches:** file_cluster_16: 5.913, file_cluster_15: 6.333, file_cluster_12: 6.805
- **Magnitude:** 245.56 | **LOC:** 196 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 72.829; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `erase_screen` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* # 0 should clear from the cursor to the end of the screen. # 1 should clear from the cursor to the b...
  * `erase_line` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* # 0 should clear from the cursor to the end of the line. # 1 should clear from the cursor to the beg...
  * `fore` **(Stateful Encapsulated Methods)** (Impact: 9.4)
  * `back` **(Stateful Encapsulated Methods)** (Impact: 9.4)
  * `enable_vt_processing` **(Defensive Guards)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 31`, `args: 16`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 59`
* *Architecture:* `api: 19`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 72.829
  * `Choke Point (Betweenness):` 0.001667 | `Ripple Effect (Closeness):` 0.289
  * `Imports (Out-Degree: 1):` .win32, msvcrt
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `colorama-0.4.6/colorama/tests/ansitowin32_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.319)
- **Top Global Matches:** file_cluster_10: 6.319, file_cluster_15: 6.449, file_cluster_11: 8.217
- **Magnitude:** 157.06 | **LOC:** 295 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (29.6%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testWriteAndConvertStripsAllValidAnsi` **(Compute Cores)** (Impact: 5.5)
  * `testWriteAndConvertCallsWin32WithParamsAndCommand` **(I/O & Config Routines)** (Impact: 3.6)
  * `test_osc_codes` **(Compute Cores)** (Impact: 3.6)
  * `test_native_windows_ansi` **(Callbacks & Closures)** (Impact: 3.6)
  * `testExtractParams` **(Compute Cores)** (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 60`, `args: 36`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `state_mutation: 69`, `unreferenced_by_name: 23`
* *Architecture:* `io: 3`, `api: 26`, `import: 9`
* *Defense:* `safety: 4`, `test: 56`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ..ansitowin32, ..win32, .utils, contextlib, contextlib2, io, mock, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/colorama/initialise.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.154)
- **Top Global Matches:** file_cluster_12: 7.154, file_cluster_15: 8.635, file_cluster_16: 8.78
- **Magnitude:** 132.16 | **LOC:** 122 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **4**; blast radius 82.438; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.9%), Complexity Load (formerly Cognitive Load) (72.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `just_fix_windows_console` **(I/O & Config Routines)** (Impact: 8.1)
  * `wrap_stream` **(Compute Cores)** (Impact: 7.7)
  * `deinit` **(Interface Declarations)** (Impact: 3.2)
  * `reinit` **(Interface Declarations)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 27`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `io: 15`, `api: 7`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 82.438
  * `Choke Point (Betweenness):` 0.0175 | `Ripple Effect (Closeness):` 0.403333
  * `Imports (Out-Degree: 1):` .ansitowin32, atexit, contextlib, sys
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `colorama-0.4.6/colorama/win32.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.376)
- **Top Global Matches:** file_cluster_15: 5.376, file_cluster_12: 6.288, file_cluster_11: 6.515
- **Magnitude:** 123.58 | **LOC:** 181 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 124.431; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (68.5%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SetConsoleCursorPosition` **(Compute Cores)** (Impact: 8.8)
  * `SetConsoleMode` **(Parameter Forwarders)** (Impact: 3.7)
  * `GetConsoleMode` **(Parameter Forwarders)** (Impact: 3.1)
  * `FillConsoleOutputCharacter` **(Parameter Forwarders)** (Impact: 2.7)
  * `FillConsoleOutputAttribute` **(Parameter Forwarders)** (Impact: 2.7)
    * *Intent:* ''' FillConsoleOutputAttribute( hConsole, csbi.wAttributes, dwConSize, coordScreen, &cCharsWritten )...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 30`, `args: 13`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 58`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 124.431
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.316098
  * `Imports (Out-Degree: 0):` ctypes
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `colorama-0.4.6/colorama/tests/initialise_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.385)
- **Top Global Matches:** file_cluster_10: 7.385, file_cluster_15: 7.495, file_cluster_13: 7.993
- **Magnitude:** 89.3 | **LOC:** 190 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.8%), Complexity Load (formerly Cognitive Load) (17.2%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testJustFixWindowsConsole` **(I/O & Config Routines)** (Impact: 11.3)
  * `testAutoResetChangeable` **(Parameter Forwarders)** (Impact: 2.5)
  * `testAutoResetPassedOn` **(Parameter Forwarders)** (Impact: 2.3)
  * `testAtexitRegisteredOnlyOnce` **(Parameter Forwarders)** (Impact: 2.0)
  * `testInitWrapsOnWindows` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 42`, `args: 24`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 12`
* *Architecture:* `io: 34`, `api: 19`, `import: 7`
* *Defense:* `safety: 4`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ..ansitowin32, ..initialise, .utils, mock, sys, unittest, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/colorama/ansi.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.203)
- **Top Global Matches:** file_cluster_15: 6.203, file_cluster_2: 7.613, file_cluster_11: 7.761
- **Magnitude:** 84.36 | **LOC:** 103 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 89.44; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.5%), Connectivity (formerly Api Exposure) (76.2%), Guard Balance (formerly Safety Score) (73.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* # the subclasses declare class attributes which are numbers. # Upon instantiation we define instance...
  * `POS` **(Type Conversions)** (Impact: 2.1)
  * `UP` **(Type Conversions)** (Impact: 1.8)
  * `DOWN` **(Type Conversions)** (Impact: 1.8)
  * `FORWARD` **(Type Conversions)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 24`, `args: 10`, `func_start: 10`, `class_start: 5`
* *Risk/State:* `state_mutation: 46`
* *Architecture:* `api: 15`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 89.44
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.365714
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `colorama-0.4.6/colorama/tests/winterm_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.476)
- **Top Global Matches:** file_cluster_15: 6.476, file_cluster_13: 6.581, file_cluster_2: 7.425
- **Magnitude:** 66.58 | **LOC:** 132 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (25.5%), Connectivity (formerly Api Exposure) (9.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testResetAll` **(Parameter Forwarders)** (Impact: 2.6)
  * `testGetAttrs` **(I/O & Config Routines)** (Impact: 2.4)
  * `testSetConsole` **(Parameter Forwarders)** (Impact: 2.4)
  * `testSetConsoleOnStderr` **(Parameter Forwarders)** (Impact: 2.4)
  * `testInit` **(Parameter Forwarders)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 18`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 8`
* *Architecture:* `io: 4`, `api: 9`, `import: 5`
* *Defense:* `safety: 2`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..winterm, mock, sys, unittest, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/colorama/tests/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.806)
- **Top Global Matches:** file_cluster_11: 6.806, file_cluster_15: 7.18, file_cluster_13: 7.354
- **Magnitude:** 35.42 | **LOC:** 50 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 36.208; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (71.4%), Guard Balance (formerly Safety Score) (61.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `replace_by` **(Parameter Forwarders)** (Impact: 1.8)
  * `replace_original_by` **(Parameter Forwarders)** (Impact: 1.8)
  * `osname` **(Parameter Forwarders)** (Impact: 1.7)
  * `isatty` **(Parameter Forwarders)** (Impact: 1.5)
  * `isatty` **(Parameter Forwarders)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `io: 15`, `api: 8`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.208
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.12
  * `Imports (Out-Degree: 0):` contextlib, io, os, sys
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `colorama-0.4.6/colorama/tests/isatty_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.14)
- **Top Global Matches:** file_cluster_15: 6.14, file_cluster_11: 7.199, file_cluster_13: 7.524
- **Magnitude:** 26.96 | **LOC:** 58 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.7%), Connectivity (formerly Api Exposure) (11.3%), Complexity Load (formerly Cognitive Load) (4.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_TTY` **(Parameter Forwarders)** (Impact: 1.7)
  * `test_nonTTY` **(Parameter Forwarders)** (Impact: 1.7)
  * `test_withPycharmNoneOverride` **(Parameter Forwarders)** (Impact: 1.7)
  * `test_withPycharmStreamWrapped` **(Parameter Forwarders)** (Impact: 1.7)
  * `test_withPycharm` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 7`
* *Architecture:* `io: 4`, `api: 9`, `import: 4`
* *Defense:* `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..ansitowin32, .utils, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/colorama/tests/ansi_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.911)
- **Top Global Matches:** file_cluster_15: 5.911, file_cluster_2: 6.833, file_cluster_11: 6.99
- **Magnitude:** 20.8 | **LOC:** 77 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (8.9%), Complexity Load (formerly Cognitive Load) (4.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testForeAttributes` **(I/O & Config Routines)** (Impact: 2.4)
  * `testBackAttributes` **(I/O & Config Routines)** (Impact: 2.4)
  * `setUp` **(Parameter Forwarders)** (Impact: 1.7)
    * *Intent:* # sanity check: stdout should be a file or StringIO object. # It will only be AnsiToWin32 if init() ...
  * `tearDown` **(Parameter Forwarders)** (Impact: 1.6)
  * `testStyleAttributes` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 5`
* *Architecture:* `io: 6`, `api: 6`, `import: 4`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..ansi, ..ansitowin32, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo01.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.127)
- **Top Global Matches:** file_cluster_2: 5.127, file_cluster_17: 6.234, file_cluster_13: 6.7
- **Magnitude:** 19.56 | **LOC:** 49 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 6`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, colorama, fixpath, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo02.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.615)
- **Top Global Matches:** file_cluster_2: 4.615, file_cluster_17: 5.646, file_cluster_13: 6.271
- **Magnitude:** 15.36 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`
* *Risk/State:* None
* *Architecture:* `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, colorama, fixpath
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo05.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.041)
- **Top Global Matches:** file_cluster_2: 6.041, file_cluster_17: 6.712, file_cluster_13: 7.15
- **Magnitude:** 15.26 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* None
* *Architecture:* `io: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, colorama, fixpath, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo.bat` (BATCH | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.115)
- **Top Global Matches:** file_cluster_2: 2.115, file_cluster_17: 4.936, file_cluster_13: 6.267
- **Magnitude:** 15.22 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo03.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.529)
- **Top Global Matches:** file_cluster_2: 5.529, file_cluster_17: 6.286, file_cluster_13: 6.699
- **Magnitude:** 15.2 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`
* *Risk/State:* None
* *Architecture:* `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, colorama, fixpath
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo04.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.842)
- **Top Global Matches:** file_cluster_2: 5.842, file_cluster_17: 6.64, file_cluster_13: 6.962
- **Magnitude:** 14.68 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* None
* *Architecture:* `io: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, colorama, fixpath, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/fixpath.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.742)
- **Top Global Matches:** file_cluster_2: 5.742, file_cluster_17: 6.745, file_cluster_13: 7.099
- **Magnitude:** 14.08 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **2**; blast radius 56.812; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (31.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 56.812
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.32
  * `Imports (Out-Degree: 0):` os.path, sys
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `colorama-0.4.6/demos/demo06.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.882)
- **Top Global Matches:** file_cluster_10: 6.882, file_cluster_2: 8.219, file_cluster_15: 8.373
- **Magnitude:** 13.22 | **LOC:** 43 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Guard Balance (formerly Safety Score) (55.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (18.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Callbacks & Closures)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, colorama, fixpath, random, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/colorama/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.885)
- **Top Global Matches:** file_cluster_2: 4.885, file_cluster_17: 5.602, file_cluster_13: 5.956
- **Magnitude:** 13.08 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **3**; blast radius 72.265; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 72.265
  * `Choke Point (Betweenness):` 0.036667 | `Ripple Effect (Closeness):` 0.36
  * `Imports (Out-Degree: 3):` .ansi, .ansitowin32, .initialise
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `colorama-0.4.6/colorama/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo09.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.869)
- **Top Global Matches:** file_cluster_10: 6.869, file_cluster_15: 8.03, file_cluster_11: 8.855
- **Magnitude:** 7.56 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (31.0%), Connectivity (formerly Api Exposure) (5.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find` **(Parameter Forwarders)** (Impact: 1.8)
  * `format` **(Callbacks & Closures)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` argparse, colorama
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo07.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.75)
- **Top Global Matches:** file_cluster_11: 5.75, file_cluster_2: 7.221, file_cluster_15: 7.608
- **Magnitude:** 6.9 | **LOC:** 28 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (7.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* """ expected output: 1a2 aba 3a4 """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, colorama, fixpath
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.526)
- **Top Global Matches:** file_cluster_2: 4.526, file_cluster_17: 6.052, file_cluster_13: 6.721
- **Magnitude:** 2.72 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `colorama-0.4.6/demos/demo08.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.895)
- **Top Global Matches:** file_cluster_11: 5.895, file_cluster_2: 7.554, file_cluster_15: 7.798
- **Magnitude:** 2.6 | **LOC:** 16 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 18.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (4.1%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* """automatically reset stdout"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, colorama, fixpath
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `colorama-0.4.6/colorama/tests/initialise_test.py` (PYTHON) | Magnitude: 89.3 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 42, io: 34, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `colorama-0.4.6/colorama/tests/winterm_test.py` (PYTHON) | Magnitude: 66.58 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 92, state_mutation: 38, test: 22, structural_boundaries: 18

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `colorama-0.4.6/colorama/ansitowin32.py` -> **Severity: 5.583** (Bridge: 0.0558 * Flux: 100.0%)
- `colorama-0.4.6/colorama/initialise.py` -> **Severity: 1.75** (Bridge: 0.0175 * Flux: 100.0%)
- `colorama-0.4.6/colorama/__init__.py` -> **Severity: 0.616** (Bridge: 0.0367 * Flux: 16.7982%)
- `colorama-0.4.6/colorama/winterm.py` -> **Severity: 0.167** (Bridge: 0.0017 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `colorama-0.4.6/colorama/initialise.py` -> **Severity: 32.217** (Embedded: 0.4033 * Error Risk: 79.8773%)
- `colorama-0.4.6/colorama/ansitowin32.py` -> **Severity: 28.733** (Embedded: 0.3913 * Error Risk: 73.4276%)
- `colorama-0.4.6/colorama/ansi.py` -> **Severity: 26.936** (Embedded: 0.3657 * Error Risk: 73.652%)
- `colorama-0.4.6/colorama/winterm.py` -> **Severity: 24.124** (Embedded: 0.289 * Error Risk: 83.4744%)
- `colorama-0.4.6/colorama/win32.py` -> **Severity: 22.848** (Embedded: 0.3161 * Error Risk: 72.2829%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `colorama-0.4.6/colorama/ansitowin32.py` -> **Severity: 12576.729** (Blast Radius: 138.344 * Doc Risk: 90.9091%)
- `colorama-0.4.6/colorama/win32.py` -> **Severity: 11258.044** (Blast Radius: 124.431 * Doc Risk: 90.4762%)
- `colorama-0.4.6/colorama/ansi.py` -> **Severity: 8944.0** (Blast Radius: 89.44 * Doc Risk: 100.0%)
- `colorama-0.4.6/colorama/initialise.py` -> **Severity: 8243.8** (Blast Radius: 82.438 * Doc Risk: 100.0%)
- `colorama-0.4.6/colorama/winterm.py` -> **Severity: 7282.9** (Blast Radius: 72.829 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 4 literal sites + 1 sites through wrappers = 5

- `get_osfhandle` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `colorama-0.4.6/colorama/winterm.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 438 call pairs -- scoped 45.2%, unique 0.0%, ambiguous 3.0%, external 51.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 435 | 45.5% | 0.0% | 3.0% | 51.5% |
| shell | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
