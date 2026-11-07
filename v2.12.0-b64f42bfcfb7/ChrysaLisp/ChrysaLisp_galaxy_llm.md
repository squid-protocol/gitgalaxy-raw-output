# ARCHITECTURAL_BRIEF: ChrysaLisp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/vygr/ChrysaLisp.git` |
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
- **Scope:** 445 analyzed artifact(s), 48939 LOC.
- **Load-bearing artifact:** `funcs.ps1` -- 7 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `LLM.md` -- pulls in 52 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/host/gui_fb.c` at magnitude 1008.76 (structural weight, not risk).
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
| Total Artifacts | 1054 |
| Analyzed Artifacts (Scanned) | 445 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 609 |
| Total LOC | 48939 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 42.2% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7136 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4584 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2188 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 272 | 17935 | 61.1% |
| GLSL | 129 | 26969 | 29.0% |
| CPP | 10 | 2358 | 2.2% |
| POWERSHELL | 9 | 259 | 2.0% |
| SHELL | 9 | 288 | 2.0% |
| XML | 6 | 0 | 1.3% |
| BATCH | 5 | 119 | 1.1% |
| MARKDOWN | 3 | 0 | 0.7% |
| MAKEFILE | 1 | 98 | 0.2% |
| C | 1 | 913 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 445 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 81%, Data / Markup / Trivial 14%, Large Core Modules 1%, Large Core Modules (3) 1%, Interface Declarations Files 0%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 442 | 99.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 609*

**Composition by Extension & Reason:**
- `.md`: 199x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3032 LOC)
- `.cpm`: 160x Excluded (Unsupported Extension: '.cpm')
- `.lisp`: 142x Excluded (Unsupported Extension: '.lisp'), 5x Unsupported Format (.lisp), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 47 exceeds 500 chars), 1x Zero-Density Threshold (LOC: 58, Signals: 0)
- `.sdf`: 19x Excluded (Unsupported Extension: '.sdf')
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `.ctf`: 6x Excluded (Unsupported Extension: '.ctf')
- `.tga`: 4x Excluded (Unsupported Extension: '.tga')
- `.vp`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.flm`: 3x Excluded (Unsupported Extension: '.flm')
- `.lst`: 3x Excluded (Unsupported Extension: '.lst')
- `.svg`: 1x Excluded (Static Asset Blob without Intent: 1654 LOC), 1x Excluded (Massive Static Asset Blob: 49421 LOC), 1x Excluded (Embedded Array/Matrix Payload: 5355 commas in 726 LOC)
- `.pcb`: 3x Excluded (Unsupported Extension: '.pcb')
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 3.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.5 | 6.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 93.8 | 0.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 50.4 | 0.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 36.7 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.3 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 176 | 10 | 0 | `src/host/pii_linux.cpp` |
| cleanup | 25 | 8 | 0 | `src/host/gui_fb.c` |
| guards | 123 | 10 | 0 | `src/host/gui_fb.c` |
| danger | 453 | 30 | 0 | `funcs.sh` |
| concurrency | 29 | 7 | 0 | `service/lock/app.inc` |
| connectivity | 32 | 4 | 0 | `src/host/gui_fb.c` |
| io | 40 | 12 | 0 | `src/host/gui_fb.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 22 | 5 | 0 | `Makefile` |
| time | 0 | 0 | 0 | - |
| serialization | 1 | 1 | 0 | `Makefile` |
| regex | 6 | 1 | 0 | `Makefile` |
| events | 52 | 4 | 0 | `lib/trans/arm64.inc` |
| tests | 3 | 2 | 0 | `funcs.sh` |
| docs | 69 | 3 | 0 | `src/host/sdl_dummy.h` |
| debt | 42 | 9 | 0 | `src/host/gui_fb.c` |
| mutation | 1122 | 37 | 0 | `src/host/gui_fb.c` |
| dead_code | 13 | 8 | 0 | `funcs.ps1` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 21 | 6 | 0 | `lib/asm/cscript.inc` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/host/gui_fb.c` (Hits: 7)
- `run_cube.sh` (Hits: 6)
- `Makefile` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **funcs.ps1** (`funcs.ps1`) — 7 inbound connections
2. **funcs.sh** (`funcs.sh`) — 7 inbound connections
3. **pii.h** (`src/host/pii.h`) — 5 inbound connections
4. **pii_windows.cpp** (`src/host/pii_windows.cpp`) — 2 inbound connections
5. **CONTRIBUTIONS.md** (`CONTRIBUTIONS.md`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **LLM.md** (`LLM.md`) — 52 outbound dependencies
2. **gui_fb.c** (`src/host/gui_fb.c`) — 17 outbound dependencies
3. **pii_windows.cpp** (`src/host/pii_windows.cpp`) — 15 outbound dependencies
4. **pii_darwin.cpp** (`src/host/pii_darwin.cpp`) — 14 outbound dependencies
5. **pii_linux.cpp** (`src/host/pii_linux.cpp`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `host_gui_blit` **(Many-Argument Workhorses)** (@ `src/host/gui_raw.cpp`) -> Impact: **79.5** | LOC: 151
- `get_event_timeout` **(Many-Argument Workhorses)** (@ `src/host/gui_fb.c`) -> Impact: **51.3** | LOC: 90
  * *Intent:* /* msec timeout 0 to poll, timeout -1 to block */
- `host_gui_create_texture` **(Many-Argument Workhorses)** (@ `src/host/gui_fb.c`) -> Impact: **49.2** | LOC: 53
  * *Intent:* /* allocate drawable for passed data and return a handle to it */
- `host_gui_create_texture` **(Many-Argument Workhorses)** (@ `src/host/gui_raw.cpp`) -> Impact: **49.1** | LOC: 51
  * *Intent:* //////////////////// // texture functions ////////////////////
- `host_gui_filled_box` **(Compute Cores)** (@ `src/host/gui_raw.cpp`) -> Impact: **33.6** | LOC: 50
- `main` **(Many-Argument Workhorses)** (@ `src/host/main.cpp`) -> Impact: **29.8** | LOC: 77
  * *Intent:* #endif
- `open_framebuffer` **(I/O & Config Routines)** (@ `src/host/gui_fb.c`) -> Impact: **25.9** | LOC: 98
  * *Intent:* /* open linux framebuffer*/
- `last_op` **(I/O & Config Routines)** (@ `lib/asm/vp.inc`) -> Impact: **22.9** | LOC: 198
- `pii_mprotect` **(Compute Cores)** (@ `src/host/pii_windows.cpp`) -> Impact: **22.9** | LOC: 18
- `read_mouse` **(Stateful Encapsulated Methods)** (@ `src/host/gui_fb.c`) -> Impact: **21.8** | LOC: 33
  * *Intent:* * --------+-----+-----+-----+-----+-----+-----+-----+----- * Byte 0 | 0 0 Neg-Y Neg-X 1 Mid Right Left * Byte 1 | X X X X X X X X * Byte 2 | Y Y Y Y Y...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/host` | 11 | 2462.42 | 41.35% | 3.16% |
| `__monolith__` | 27 | 938.98 | 31.74% | 3.47% |
| `class/lisp` | 31 | 527.22 | 0.0% | 0.0% |
| `gui/path` | 16 | 263.48 | 0.0% | 0.0% |
| `lib/text` | 12 | 219.4 | 0.0% | 0.0% |
| `lib/asm` | 11 | 202.0 | 1.83% | 2.25% |
| `lib/collections` | 10 | 162.92 | 0.0% | 0.0% |
| `apps/science/pcb` | 8 | 137.02 | 0.0% | 1.13% |
| `gui/canvas` | 7 | 131.56 | 0.0% | 0.0% |
| `apps/system/terminal` | 8 | 123.92 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `funcs.ps1` -> **93.7517%** Exposure
- `apps/desktop/todo/config.inc` -> **62.2459%** Exposure
- `apps/desktop/todo/widgets.inc` -> **62.2459%** Exposure
- `lib/task/global.inc` -> **37.7541%** Exposure
- `src/host/main.cpp` -> **15.1253%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `funcs.ps1` -> **100.0%** Exposure
- `run_cube.ps1` -> **100.0%** Exposure
- `run_mesh.ps1` -> **100.0%** Exposure
- `run_tree.ps1` -> **100.0%** Exposure
- `funcs.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `funcs.ps1` -> **5** Orphaned Functions | **0** Duplicates
- `apps/science/pcb/router.inc` -> **1** Orphaned Functions | **0** Duplicates
- `lib/asm/asm.inc` -> **1** Orphaned Functions | **0** Duplicates
- `lib/asm/vp.inc` -> **1** Orphaned Functions | **0** Duplicates
- `lib/task/global.inc` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `158` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/host/gui_fb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.716)
- **Top Global Matches:** file_cluster_4: 8.716, file_cluster_12: 11.608, file_cluster_6: 12.095
- **Magnitude:** 1008.76 | **LOC:** 1064 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_event_timeout` **(Many-Argument Workhorses)** (Impact: 51.3)
    * *Intent:* /* msec timeout 0 to poll, timeout -1 to block */
  * `host_gui_create_texture` **(Many-Argument Workhorses)** (Impact: 49.2)
    * *Intent:* /* allocate drawable for passed data and return a handle to it */
  * `open_framebuffer` **(I/O & Config Routines)** (Impact: 25.9)
    * *Intent:* /* open linux framebuffer*/
  * `read_mouse` **(Stateful Encapsulated Methods)** (Impact: 21.8)
    * *Intent:* * --------+-----+-----+-----+-----+-----+-----+-----+----- * Byte 0 | 0 0 Neg-Y Neg-X 1 Mid Right Le...
  * `host_gui_filled_box` **(Compute Cores)** (Impact: 20.1)
    * *Intent:* /* fill rectangle with current color */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 186 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 599
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 117`, `args: 49`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 4`, `state_mutation: 227`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 23`, `import: 17`
* *Defense:* `immutability_locks: 26`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, fcntl.h, inttypes.h, fb.h, kd.h, keyboard.h, vt.h, poll.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/gui_raw.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.323)
- **Top Global Matches:** file_cluster_6: 9.323, file_cluster_4: 12.609, file_cluster_8: 16.957
- **Magnitude:** 458.68 | **LOC:** 488 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.097; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.7%)
- **Documentation Coverage:** 72.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `host_gui_blit` **(Many-Argument Workhorses)** (Impact: 79.5)
  * `host_gui_create_texture` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* //////////////////// // texture functions ////////////////////
  * `host_gui_filled_box` **(Compute Cores)** (Impact: 33.6)
  * `host_gui_flush` **(Compute Cores)** (Impact: 11.3)
  * `host_gui_box` **(Compute Cores)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 73 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 63`, `args: 34`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 96`
* *Architecture:* `import: 4`
* *Defense:* `doc: 10`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL.h, iostream, memory, stdint.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/pii_windows.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.129)
- **Top Global Matches:** file_cluster_7: 8.129, file_cluster_12: 8.563, file_cluster_5: 10.174
- **Magnitude:** 274.78 | **LOC:** 400 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 3.88; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%), Complexity Load (formerly Cognitive Load) (64.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pii_mprotect` **(Compute Cores)** (Impact: 22.9)
  * `pii_munmap` **(Compute Cores)** (Impact: 18.8)
  * `pii_dirlist` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `walk_directory` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* */ #define FOLDER_PRE 0 #define FOLDER_POST 1
  * `pii_open` **(Compute Cores)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 32 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 79`, `args: 34`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 38`
* *Architecture:* `import: 15`
* *Defense:* `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004435
  * `Imports (Out-Degree: 1):` conio.h, direct.h, fcntl.h, io.h, iostream, pii.h, random, stdio.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/host/pii_darwin.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.085)
- **Top Global Matches:** file_cluster_7: 8.085, file_cluster_12: 8.862, file_cluster_5: 10.207
- **Magnitude:** 214.3 | **LOC:** 359 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%), Complexity Load (formerly Cognitive Load) (46.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `walk_directory` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* */ #define FOLDER_PRE 0 #define FOLDER_POST 1
  * `pii_open` **(Compute Cores)** (Impact: 17.2)
  * `pii_open_shared` **(Compute Cores)** (Impact: 13.0)
  * `pii_mprotect` **(Compute Cores)** (Impact: 12.7)
  * `pii_mmap` **(Type Conversions)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 76`, `args: 30`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 23`
* *Architecture:* `import: 14`
* *Defense:* `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dirent.h, fcntl.h, iostream, OSCacheControl.h, pii.h, random, stdio.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/pii_linux.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.092)
- **Top Global Matches:** file_cluster_7: 8.092, file_cluster_12: 8.889, file_cluster_5: 10.214
- **Magnitude:** 214.28 | **LOC:** 358 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%), Complexity Load (formerly Cognitive Load) (46.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `walk_directory` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* */ #define FOLDER_PRE 0 #define FOLDER_POST 1
  * `pii_open` **(Compute Cores)** (Impact: 17.2)
  * `pii_open_shared` **(Compute Cores)** (Impact: 13.0)
  * `pii_mprotect` **(Compute Cores)** (Impact: 12.7)
  * `pii_mmap` **(Type Conversions)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 76`, `args: 30`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 23`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dirent.h, fcntl.h, iostream, pii.h, random, stdio.h, string.h, mman.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `funcs.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.061)
- **Top Global Matches:** file_cluster_10: 9.061, file_cluster_9: 10.024, file_cluster_15: 11.367
- **Magnitude:** 209.82 | **LOC:** 112 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 14.574; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.4%), Debt Markers (formerly Tech Debt) (93.8%), Complexity Load (formerly Cognitive Load) (81.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `boot_cpu_gui` **(Callbacks & Closures)** (Impact: 19.0)
  * `boot_cpu_tui` **(Callbacks & Closures)** (Impact: 19.0)
  * `add_link` **(Callbacks & Closures)** (Impact: 10.5)
  * `main` **(Callbacks & Closures)** (Impact: 7.6)
  * `zero_pad` **(Callbacks & Closures)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 8`, `args: 5`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 52`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.574
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.015521
  * `Imports (Out-Degree: 1):` $NHROOT\stop.ps1
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `funcs.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 6.642)
- **Top Global Matches:** file_cluster_14: 6.642, file_cluster_7: 12.635, file_cluster_5: 15.555
- **Magnitude:** 142.7 | **LOC:** 153 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); blast radius 14.574; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 11.6)
  * `boot_cpu_gui` **(Compute Cores)** (Impact: 11.4)
  * `boot_cpu_tui` **(Compute Cores)** (Impact: 11.3)
  * `add_link` **(Compute Cores)** (Impact: 9.6)
  * `zero_pad` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 62`, `args: 23`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 27`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 3`
* *Defense:* `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.574
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015521
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/host/vp64.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 7.027)
- **Top Global Matches:** file_cluster_17: 7.027, file_cluster_2: 7.736, file_cluster_15: 8.252
- **Magnitude:** 105.22 | **LOC:** 490 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 2.988; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (99.9%), Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (59.1%), Debt Markers (formerly Tech Debt) (9.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vp64` **(Many-Argument Workhorses)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 7`, `args: 3`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `state_mutation: 70`, `unreferenced_by_name: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002217
  * `Imports (Out-Degree: 1):` atomic, cmath, immintrin.h, intrin.h, iostream, pii.h, types.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `run_cube.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.284)
- **Top Global Matches:** file_cluster_10: 5.284, file_cluster_2: 5.362, file_cluster_17: 7.014
- **Magnitude:** 75.64 | **LOC:** 37 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.7%), Complexity Load (formerly Cognitive Load) (65.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_mesh.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.209)
- **Top Global Matches:** file_cluster_2: 5.209, file_cluster_10: 5.244, file_cluster_17: 6.894
- **Magnitude:** 57.52 | **LOC:** 31 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (61.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/main.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.023)
- **Top Global Matches:** file_cluster_7: 7.023, file_cluster_12: 8.43, file_cluster_5: 9.621
- **Magnitude:** 56.48 | **LOC:** 145 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.6%), Guard Balance (formerly Safety Score) (72.6%), Complexity Load (formerly Cognitive Load) (37.2%), Debt Markers (formerly Tech Debt) (15.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 29.8)
    * *Intent:* #endif
  * `enableRawMode` **(Interface Declarations)** (Impact: 1.4)
  * `enableRawMode` **(Interface Declarations)** (Impact: 1.4)
  * `disableRawMode` **(Interface Declarations)** (Impact: 1.2)
  * `disableRawMode` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 22`, `args: 14`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fcntl.h, io.h, iostream, pii.h, stdint.h, string.h, stat.h, termios.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/audio_sdl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.792)
- **Top Global Matches:** file_cluster_12: 6.792, file_cluster_7: 7.239, file_cluster_5: 9.411
- **Magnitude:** 54.46 | **LOC:** 140 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.097; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.0%), Mutation Surface (formerly State Flux) (56.3%), Complexity Load (formerly Cognitive Load) (15.1%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `host_audio_change_sfx` **(Compute Cores)** (Impact: 20.5)
  * `host_audio_add_sfx` **(Compute Cores)** (Impact: 5.1)
  * `host_audio_init` **(I/O & Config Routines)** (Impact: 3.8)
  * `host_audio_remove_sfx` **(Compute Cores)** (Impact: 3.4)
  * `host_audio_play_sfx` **(Parameter Forwarders)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 5`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL.h, SDL_mixer.h, SDL_rwops.h, iostream, stdint.h, string, unordered_map
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_tree.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.179)
- **Top Global Matches:** file_cluster_10: 5.179, file_cluster_2: 5.181, file_cluster_17: 6.868
- **Magnitude:** 42.5 | **LOC:** 34 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (59.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/gui_sdl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.275)
- **Top Global Matches:** file_cluster_7: 8.275, file_cluster_14: 8.801, file_cluster_12: 11.053
- **Magnitude:** 41.14 | **LOC:** 155 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Mutation Surface (formerly State Flux) (9.5%), Complexity Load (formerly Cognitive Load) (6.9%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `host_gui_init` **(Compute Cores)** (Impact: 4.3)
  * `host_gui_create_texture` **(Parameter Forwarders)** (Impact: 2.9)
  * `host_gui_set_texture_color` **(Parameter Forwarders)** (Impact: 2.5)
  * `host_gui_set_color` **(Parameter Forwarders)** (Impact: 2.4)
  * `host_gui_blit` **(Parameter Forwarders)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 48`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 4`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_ring.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.029)
- **Top Global Matches:** file_cluster_2: 5.029, file_cluster_10: 5.199, file_cluster_17: 6.751
- **Magnitude:** 36.38 | **LOC:** 24 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.6%), Complexity Load (formerly Cognitive Load) (57.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_cube.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 7.005)
- **Top Global Matches:** file_cluster_14: 7.005, file_cluster_7: 14.821, file_cluster_5: 18.098
- **Magnitude:** 35.96 | **LOC:** 39 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Complexity Load (formerly Cognitive Load) (63.6%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 17`, `args: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 8`
* *Architecture:* `io: 6`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` funcs.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/text/buffer.inc` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.253)
- **Top Global Matches:** file_cluster_2: 3.253, file_cluster_17: 4.58, file_cluster_13: 5.666
- **Magnitude:** 34.6 | **LOC:** 1351 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.3%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 83`, `args: 376`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/str/class.vp` (GLSL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.569)
- **Top Global Matches:** file_cluster_2: 2.569, file_cluster_17: 5.133, file_cluster_13: 6.459
- **Magnitude:** 33.6 | **LOC:** 1097 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.4%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gui/region/class.vp` (GLSL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.568)
- **Top Global Matches:** file_cluster_2: 2.568, file_cluster_17: 5.133, file_cluster_13: 6.459
- **Magnitude:** 33.54 | **LOC:** 1065 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.116)
- **Top Global Matches:** file_cluster_2: 5.116, file_cluster_10: 5.212, file_cluster_17: 6.817
- **Magnitude:** 33.36 | **LOC:** 23 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.6%), Complexity Load (formerly Cognitive Load) (55.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_tui.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.116)
- **Top Global Matches:** file_cluster_2: 5.116, file_cluster_10: 5.212, file_cluster_17: 6.817
- **Magnitude:** 33.36 | **LOC:** 23 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.6%), Complexity Load (formerly Cognitive Load) (55.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_star.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.017)
- **Top Global Matches:** file_cluster_2: 5.017, file_cluster_10: 5.134, file_cluster_17: 6.74
- **Magnitude:** 30.36 | **LOC:** 23 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.097; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (60.6%), Complexity Load (formerly Cognitive Load) (41.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/stream/lisp.vp` (GLSL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.505)
- **Top Global Matches:** file_cluster_2: 2.505, file_cluster_17: 5.102, file_cluster_13: 6.433
- **Magnitude:** 30.32 | **LOC:** 950 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.3%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/reals/class.vp` (GLSL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.457)
- **Top Global Matches:** file_cluster_2: 2.457, file_cluster_17: 5.094, file_cluster_13: 6.41
- **Magnitude:** 29.92 | **LOC:** 924 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.2%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/lisp/root.inc` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.385)
- **Top Global Matches:** file_cluster_2: 2.385, file_cluster_17: 4.564, file_cluster_13: 5.61
- **Magnitude:** 29.74 | **LOC:** 1430 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.8%), Guard Balance (formerly Safety Score) (50.5%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 112`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* None
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `run_tree.ps1` (POWERSHELL) | Magnitude: 42.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 9, branch: 5, closures: 3
- `run_cube.ps1` (POWERSHELL) | Magnitude: 75.64 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, state_mutation: 20, branch: 8, closures: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `run_mesh.ps1` (POWERSHELL) | Magnitude: 57.52 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 21, state_mutation: 14, branch: 6, closures: 3
- `run.ps1` (POWERSHELL) | Magnitude: 33.36 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 6, branch: 4, closures: 2
- `run_tui.ps1` (POWERSHELL) | Magnitude: 33.36 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 6, branch: 4, closures: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/host/gui_fb.c` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 1008.76
- `src/host/gui_raw.cpp` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 458.68
- `funcs.ps1` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 209.82
- `run_cube.ps1` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 75.64
- `run_mesh.ps1` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 57.52

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `funcs.ps1` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `funcs.sh` -> **Severity: 1.526** (Embedded: 0.0155 * Error Risk: 98.3496%)
- `funcs.ps1` -> **Severity: 1.496** (Embedded: 0.0155 * Error Risk: 96.3591%)
- `stop.ps1` -> **Severity: 0.757** (Embedded: 0.0095 * Error Risk: 80.0%)
- `src/host/pii_windows.cpp` -> **Severity: 0.327** (Embedded: 0.0044 * Error Risk: 73.7671%)
- `src/host/vp64.cpp` -> **Severity: 0.131** (Embedded: 0.0022 * Error Risk: 59.0727%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `funcs.ps1` -> **Severity: 728.7** (Blast Radius: 14.574 * Doc Risk: 50.0%)
- `funcs.sh` -> **Severity: 728.7** (Blast Radius: 14.574 * Doc Risk: 50.0%)
- `src/host/pii_windows.cpp` -> **Severity: 388.0** (Blast Radius: 3.88 * Doc Risk: 100.0%)
- `src/host/vp64.cpp` -> **Severity: 298.8** (Blast Radius: 2.988 * Doc Risk: 100.0%)
- `apps/games/chess/ui.inc` -> **Severity: 209.7** (Blast Radius: 2.097 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 34 literal sites + 9 sites through wrappers = 43
- **`memory_alloc`:** 17 literal sites + 12 sites through wrappers = 29

- `logSDLError` (function, debug_prints, primitive): 9 call sites in 1 files -- `src/host/audio_sdl.cpp`
- `unassert` (macro, memory_alloc, via unassert_handler): 8 call sites in 1 files -- `src/host/gui_fb.c`
- `host_gui_deinit` (function, memory_alloc, primitive): 3 call sites in 1 files -- `src/host/gui_fb.c`
- `host_gui_resize` (function, memory_alloc, primitive): 1 call sites in 1 files -- `src/host/gui_raw.cpp`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 381 call pairs -- scoped 15.7%, unique 0.8%, ambiguous 2.1%, external 81.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 281 | 5.3% | 1.1% | 2.8% | 90.7% |
| c | 67 | 29.9% | 0.0% | 0.0% | 70.1% |
| shell | 29 | 86.2% | 0.0% | 0.0% | 13.8% |
| powershell | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
