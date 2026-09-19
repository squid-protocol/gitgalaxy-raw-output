# ARCHITECTURAL_BRIEF: gnucobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/paulsmith/gnucobol.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 204 analyzed artifact(s), 210331 LOC.
- **Load-bearing artifact:** `build_windows/config.h.in` -- 33 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `libcob/common.c` -- pulls in 48 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cobc/typeck.c` at magnitude 12535.6 (structural weight, not risk).
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
| Total Artifacts | 382 |
| Analyzed Artifacts (Scanned) | 204 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 178 |
| Total LOC | 210331 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 53.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5284 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5153 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8225 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| M4 | 76 | 82998 | 37.3% |
| C | 48 | 101302 | 23.5% |
| PLAINTEXT | 36 | 0 | 17.6% |
| MAKEFILE | 10 | 1654 | 4.9% |
| COBOL | 9 | 1461 | 4.4% |
| SHELL | 8 | 752 | 3.9% |
| BATCH | 5 | 955 | 2.5% |
| YACC | 4 | 20590 | 2.0% |
| MARKDOWN | 3 | 0 | 1.5% |
| PERL | 3 | 547 | 1.5% |
| POWERSHELL | 1 | 5 | 0.5% |
| PHP | 1 | 67 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.862`
> **Composition Archetype:** `Mid Flat Project` (z +2.86; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 34%, Data / Markup / Trivial 22%, Large Core Modules 19%, Large Core Modules (3) 11%, Many-Argument Workhorses Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 165 | 80.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 39 | 19.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 178*

**Composition by Extension & Reason:**
- `.vcxproj`: 24x Excluded (Unsupported Extension: '.vcxproj')
- `.filters`: 24x Excluded (Unsupported Extension: '.filters')
- `.conf`: 19x Excluded (Unsupported Extension: '.conf')
- `no_extension`: 7x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 349 LOC)
- `.user`: 14x Excluded (Unsupported Extension: '.user')
- `.am`: 9x Excluded (Unsupported Extension: '.am'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.words`: 10x Excluded (Unsupported Extension: '.words')
- `.sln`: 8x Excluded (Unsupported Extension: '.sln')
- `.po`: 8x Excluded (Unsupported Extension: '.po')
- `.vcproj`: 6x Excluded (Unsupported Extension: '.vcproj')
- `.cpj`: 4x Excluded (Unsupported Extension: '.cpj')
- `.rc`: 4x Excluded (Unsupported Extension: '.rc')
- `.m4`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 276 LOC)
- `.in`: 2x Unsupported Format (.undeterminable), 1x Zero-Density Threshold (LOC: 126, Signals: 0)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.4 | 21.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 53.5 | 97.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 33560 | 49 | 562 | `cobc/codegen.c` |
| cleanup | 1248 | 53 | 13 | `tests/testsuite.src/run_misc.at` |
| guards | 7334 | 54 | 113 | `libcob/common.c` |
| danger | 1827 | 64 | 21 | `cobc/cobc.c` |
| concurrency | 22 | 9 | 0 | `build_aux/mkinstalldirs` |
| connectivity | 2642 | 77 | 24 | `libcob/common.h` |
| io | 517 | 43 | 4 | `doc/cobcinfo.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 131 | 7 | 0 | `tests/testsuite.src/numeric-dump.cob` |
| time | 41 | 12 | 0 | `tests/cobol85/report.pl` |
| serialization | 4 | 1 | 0 | `po/Makefile.in.in` |
| regex | 33 | 8 | 0 | `build_aux/create_mingw_bindist.sh` |
| events | 443 | 20 | 0 | `configure.ac` |
| tests | 6518 | 41 | 60 | `tests/testsuite.src/run_misc.at` |
| docs | 78 | 16 | 0 | `libcob/common.h` |
| debt | 1770 | 84 | 29 | `libcob/common.c` |
| mutation | 35227 | 119 | 531 | `cobc/parser.y` |
| dead_code | 907 | 83 | 8 | `cobc/typeck.c` |
| credential | 22 | 6 | 0 | `build_windows/set_env_vs_dist_x64.bat` |
| threat | 799 | 43 | 7 | `libcob/common.h` |
| ml_ai | 135 | 23 | 1 | `m4/libtool.m4` |
| ui | 3 | 3 | 0 | `libcob/common.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/cobcinfo.sh` (Hits: 135)
- `libcob/fileio.c` (Hits: 66)
- `build_aux/create_mingw_bindist.sh` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.h.in** (`build_windows/config.h.in`) — 33 inbound connections
2. **cobc.h** (`cobc/cobc.h`) — 16 inbound connections
3. **tree.h** (`cobc/tree.h`) — 15 inbound connections
4. **libcob.h** (`libcob.h`) — 15 inbound connections
5. **coblocal.h** (`libcob/coblocal.h`) — 11 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.c** (`libcob/common.c`) — 48 outbound dependencies
2. **cobc.c** (`cobc/cobc.c`) — 34 outbound dependencies
3. **testsuite.at** (`tests/testsuite.at`) — 34 outbound dependencies
4. **screenio.c** (`libcob/screenio.c`) — 21 outbound dependencies
5. **call.c** (`libcob/call.c`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `output_long_integer` **(Many-Argument Workhorses)** (@ `cobc/codegen.c`) -> Impact: **1091.6** | LOC: 2429
- `cob_gettmpdir` **(Compute Cores)** (@ `libcob/common.c`) -> Impact: **756.0** | LOC: 2399
- `cob_set_file_format` **(Many-Argument Workhorses)** (@ `libcob/fileio.c`) -> Impact: **640.0** | LOC: 592
  * *Intent:* /* * Set file format based on IO_filename options */
- `field_accept` **(Many-Argument Workhorses)** (@ `libcob/screenio.c`) -> Impact: **631.2** | LOC: 684
- `output_internal_function` **(Many-Argument Workhorses)** (@ `cobc/codegen.c`) -> Impact: **564.0** | LOC: 1200
- `cob_decimal_set_display` **(Many-Argument Workhorses)** (@ `libcob/numeric.c`) -> Impact: **544.6** | LOC: 1470
  * *Intent:* /* DISPLAY */
- `cb_build_intrinsic` **(Many-Argument Workhorses)** (@ `cobc/tree.c`) -> Impact: **511.7** | LOC: 485
- `process_command_line` **(Many-Argument Workhorses)** (@ `cobc/cobc.c`) -> Impact: **455.7** | LOC: 973
  * *Intent:* /* process command line options */
- `cb_build_binary_op` **(Many-Argument Workhorses)** (@ `cobc/tree.c`) -> Impact: **442.4** | LOC: 487
  * *Intent:* /* Expression */
- `cob_gen_optim` **(Many-Argument Workhorses)** (@ `cobc/codeoptim.c`) -> Impact: **421.7** | LOC: 1532

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cobc` | 24 | 66522.52 | 42.85% | 15.39% |
| `libcob` | 31 | 57330.62 | 54.97% | 12.78% |
| `tests/testsuite.src` | 38 | 2207.36 | 0.73% | 0.0% |
| `m4` | 36 | 1583.18 | 1.62% | 69.1% |
| `bin` | 4 | 1101.28 | 34.77% | 12.21% |
| `tests/cobol85` | 21 | 635.58 | 6.26% | 0.0% |
| `__monolith__` | 13 | 313.0 | 4.9% | 1.64% |
| `build_aux` | 4 | 232.62 | 43.73% | 0.0% |
| `po` | 5 | 183.42 | 4.96% | 19.17% |
| `doc` | 2 | 182.42 | 19.32% | 7.27% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `m4/extern-inline.m4` -> **100.0%** Exposure
- `m4/ltsugar.m4` -> **100.0%** Exposure
- `m4/longlong.m4` -> **99.9997%** Exposure
- `m4/wint_t.m4` -> **99.9992%** Exposure
- `m4/printf-posix.m4` -> **99.929%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/gcdiff.c` -> **100.0%** Exposure
- `cobc/cobc.c` -> **100.0%** Exposure
- `cobc/config.c` -> **100.0%** Exposure
- `cobc/field.c` -> **100.0%** Exposure
- `cobc/sqlxfdgen.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cobc/typeck.c` -> **146** Orphaned Functions | **0** Duplicates
- `libcob/common.c` -> **115** Orphaned Functions | **0** Duplicates
- `libcob/intrinsic.c` -> **112** Orphaned Functions | **0** Duplicates
- `libcob/fileio.c` -> **47** Orphaned Functions | **0** Duplicates
- `libcob/call.c` -> **34** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `521` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cobc/typeck.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 12535.6 | **LOC:** 13270 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.5%)
- **Documentation Coverage:** 98.6248% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_emit_call` **(Many-Argument Workhorses)** (Impact: 315.4)
  * `validate_move_from_num_lit` **(Many-Argument Workhorses)** (Impact: 250.9)
  * `cb_build_identifier` **(Many-Argument Workhorses)** (Impact: 209.7)
  * `cb_build_move_literal` **(Many-Argument Workhorses)** (Impact: 173.7)
  * `cb_validate_program_environment` **(Compute Cores)** (Impact: 161.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1601 instances
* *State Mutation (weighted view):* 4922
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3442`, `structural_boundaries: 1680`, `args: 777`, `func_start: 327`, `class_start: 177`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 1720`, `dead_code: 4`, `planned_debt: 50`, `fragile_debt: 19`, `unreferenced_by_name: 146`
* *Architecture:* `api: 167`, `import: 14`
* *Defense:* `safety: 70`, `doc: 4`, `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cobc.h, config.h, ctype.h, system.def, limits.h, locale.h, stddef.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/codegen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 12285.36 | **LOC:** 12938 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Guard Balance (formerly Safety Score) (92.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.1489% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `output_long_integer` **(Many-Argument Workhorses)** (Impact: 1091.6)
  * `output_internal_function` **(Many-Argument Workhorses)** (Impact: 564.0)
  * `output_call` **(Compute Cores)** (Impact: 385.9)
  * `output_stmt` **(Compute Cores)** (Impact: 342.2)
  * `output_param` **(Many-Argument Workhorses)** (Impact: 239.9)
    * *Intent:* /* Parameter */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1508 instances
* *State Mutation (weighted view):* 4619
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3379`, `structural_boundaries: 1296`, `args: 446`, `func_start: 202`, `class_start: 210`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 1603`, `planned_debt: 4`, `fragile_debt: 7`, `unreferenced_by_name: 3`
* *Architecture:* `api: 24`, `import: 13`
* *Defense:* `safety: 29`, `doc: 2`, `immutability_locks: 186`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cobc.h, config.h, ctype.h, system.def, limits.h, stdarg.h, stddef.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/parser.y` (YACC | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 11967.14 | **LOC:** 18380 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `usage` **(Many-Argument Workhorses)** (Impact: 91.3)
    * *Intent:* ;
  * `screen_option` **(Compute Cores)** (Impact: 88.8)
    * *Intent:* ;
  * `statement` **(I/O & Config Routines)** (Impact: 71.4)
    * *Intent:* ;
  * `accp_attr` **(I/O & Config Routines)** (Impact: 67.0)
    * *Intent:* ;
  * `accept_body` **(Compute Cores)** (Impact: 57.7)
    * *Intent:* ;
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1820 instances
* *State Mutation (weighted view):* 5824
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3495`, `structural_boundaries: 1166`, `args: 2397`, `func_start: 1148`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2184`, `dead_code: 3`, `planned_debt: 25`, `fragile_debt: 41`
* *Architecture:* `io: 2`, `api: 2`, `import: 5`
* *Defense:* `safety: 22`, `immutability_locks: 115`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, config.h, stdlib.h, string.h, tree.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fileio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 9313.04 | **LOC:** 7364 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_set_file_format` **(Many-Argument Workhorses)** (Impact: 640.0)
    * *Intent:* /* * Set file format based on IO_filename options */
  * `cob_file_open` **(Many-Argument Workhorses)** (Impact: 209.1)
    * *Intent:* #define dMaxArgs 16
  * `cob_fd_file_open` **(Many-Argument Workhorses)** (Impact: 180.8)
    * *Intent:* /* * Open (record) Sequential and Relative files * with just an 'fd' (No FILE *) */
  * `cob_file_save_status` **(Many-Argument Workhorses)** (Impact: 150.3)
  * `lineseq_write` **(Many-Argument Workhorses)** (Impact: 122.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1532 instances
* *High Risk Execution (weighted view):* 8
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 4684
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1959`, `structural_boundaries: 784`, `args: 209`, `func_start: 129`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 127`, `high_risk_execution: 9`, `state_mutation: 1620`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 47`
* *Architecture:* `io: 66`, `api: 70`, `import: 5`
* *Defense:* `safety: 136`, `doc: 3`, `immutability_locks: 121`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` defaults.h, dlfcn.h, fileio.h, signal.h, wait.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/common.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9105.0 | **LOC:** 8748 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.3%), Complexity Load (formerly Cognitive Load) (93.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.4413% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_gettmpdir` **(Compute Cores)** (Impact: 756.0)
  * `cob_correct_numeric` **(Compute Cores)** (Impact: 156.6)
  * `get_config_val` **(Many-Argument Workhorses)** (Impact: 151.7)
    * *Intent:* /* Return setting value as a 'string' */
  * `check_current_date` **(I/O & Config Routines)** (Impact: 150.0)
  * `cb_config_entry` **(Many-Argument Workhorses)** (Impact: 145.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1347 instances
* *High Risk Execution (weighted view):* 5
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 4162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2090`, `structural_boundaries: 980`, `args: 512`, `func_start: 204`, `class_start: 58`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 6`, `state_mutation: 1468`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 4`, `unreferenced_by_name: 115`
* *Architecture:* `io: 14`, `api: 156`, `import: 49`
* *Defense:* `safety: 215`, `doc: 3`, `immutability_locks: 224`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` cJSON.h, cJSON.h, coblocal.h, config.h, ctype.h, curses.h, db.h, defaults.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/cobc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7554.88 | **LOC:** 8434 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.5%)
- **Documentation Coverage:** 99.5215% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_command_line` **(Many-Argument Workhorses)** (Impact: 455.7)
    * *Intent:* /* process command line options */
  * `print_replace_text` **(Many-Argument Workhorses)** (Impact: 156.4)
    * *Intent:* /* TODO: Modularise! */
  * `process_filename` **(Compute Cores)** (Impact: 116.6)
    * *Intent:* is to be processed, otherwise NULL */
  * `main` **(Many-Argument Workhorses)** (Impact: 109.1)
    * *Intent:* /* Main function */
  * `process` **(Compute Cores)** (Impact: 94.7)
    * *Intent:* #ifdef __OS400__
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1255 instances
* *High Risk Execution (weighted view):* 4
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 3875
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1782`, `structural_boundaries: 749`, `args: 350`, `func_start: 155`, `class_start: 90`
* *Risk/State:* `safety_bypasses: 244`, `high_risk_execution: 5`, `state_mutation: 1365`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 9`
* *Architecture:* `io: 25`, `api: 47`, `import: 41`
* *Defense:* `safety: 171`, `doc: 1`, `immutability_locks: 186`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` cobc.h, config.def, config.h, ctype.h, db.h, defaults.h, direct.h, fcntl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/tree.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7422.9 | **LOC:** 6804 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_build_intrinsic` **(Many-Argument Workhorses)** (Impact: 511.7)
  * `cb_build_binary_op` **(Many-Argument Workhorses)** (Impact: 442.4)
    * *Intent:* /* Expression */
  * `compare_field_literal` **(Many-Argument Workhorses)** (Impact: 324.0)
    * *Intent:* /* Check if comparing field to literal is always TRUE or FALSE */
  * `cb_build_picture` **(Many-Argument Workhorses)** (Impact: 202.4)
  * `finalize_report` **(Many-Argument Workhorses)** (Impact: 156.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1011 instances
* *State Mutation (weighted view):* 3264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1757`, `structural_boundaries: 899`, `args: 301`, `func_start: 156`, `class_start: 157`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 1242`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 13`
* *Architecture:* `api: 172`, `import: 10`
* *Defense:* `safety: 118`, `immutability_locks: 236`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, config.h, ctype.h, limits.h, parser.h, stddef.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/intrinsic.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4947.76 | **LOC:** 6809 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Complexity Load (formerly Cognitive Load) (89.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.9899% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_check_numval` **(Many-Argument Workhorses)** (Impact: 230.2)
    * *Intent:* /* TEST-NUMVAL implementation */ /* Validate NUMVAL / NUMVAL-C item */ /* [spaces][+|-][spaces]{digi...
  * `cob_check_numval_f` **(Compute Cores)** (Impact: 93.1)
    * *Intent:* /* Validate NUMVAL-F item */ /* sp = spaces */ /* [sp][+|-][sp]{digits[.[digits]]|.digits}[sp][E[sp]...
  * `cob_intr_locale_date` **(Many-Argument Workhorses)** (Impact: 73.1)
  * `numval` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `cob_intr_numval_f` **(Compute Cores)** (Impact: 51.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 776 instances
* *State Mutation (weighted view):* 2402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 903`, `structural_boundaries: 577`, `args: 354`, `func_start: 233`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 850`, `fragile_debt: 2`, `unreferenced_by_name: 112`
* *Architecture:* `io: 5`, `api: 124`, `import: 19`
* *Defense:* `safety: 138`, `doc: 2`, `immutability_locks: 281`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` coblocal.h, config.h, ctype.h, errno.h, gmp.h, langinfo.h, libcob.h, locale.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fsqlxfd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 4387.1 | **LOC:** 2449 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (81.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 83.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_sql_stmt` **(Many-Argument Workhorses)** (Impact: 333.7)
    * *Intent:* /* * Build SQL Statement and return as malloced string */
  * `cob_load_xfd` **(Many-Argument Workhorses)** (Impact: 226.0)
    * *Intent:* /* * Read the 'file.xd' and create table of fields, etc * 'indsize' is the size of the SQL Indicator...
  * `convert_to_date` **(Many-Argument Workhorses)** (Impact: 214.8)
    * *Intent:* */
  * `convert_from_date` **(Many-Argument Workhorses)** (Impact: 108.9)
    * *Intent:* */
  * `cob_xfd_to_ddl` **(Many-Argument Workhorses)** (Impact: 95.8)
    * *Intent:* /* * Create DDL from XFD */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 767 instances
* *State Mutation (weighted view):* 2336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 839`, `structural_boundaries: 180`, `args: 50`, `func_start: 38`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 115`, `state_mutation: 802`, `unreferenced_by_name: 15`
* *Architecture:* `io: 5`, `api: 20`, `import: 2`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` defaults.h, fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/screenio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3517.4 | **LOC:** 3613 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.5%), Complexity Load (formerly Cognitive Load) (94.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `field_accept` **(Many-Argument Workhorses)** (Impact: 631.2)
  * `cob_screen_get_all` **(Many-Argument Workhorses)** (Impact: 225.6)
    * *Intent:* #endif
  * `cob_convert_key` **(Many-Argument Workhorses)** (Impact: 82.5)
  * `mouse_to_exception_code` **(Compute Cores)** (Impact: 79.0)
    * *Intent:* #ifdef NCURSES_MOUSE_VERSION
  * `field_display` **(Many-Argument Workhorses)** (Impact: 64.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 514 instances
* *State Mutation (weighted view):* 1564
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 761`, `structural_boundaries: 286`, `args: 164`, `func_start: 90`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 536`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 13`
* *Architecture:* `io: 2`, `api: 33`, `import: 21`
* *Defense:* `safety: 36`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` coblocal.h, config.h, ctype.h, curses.h, errno.h, io.h, libcob.h, limits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/field.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3517.18 | **LOC:** 3249 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compute_size` **(Compute Cores)** (Impact: 252.4)
  * `cb_build_field_tree` **(Many-Argument Workhorses)** (Impact: 199.6)
  * `compute_binary_size` **(Compute Cores)** (Impact: 173.2)
  * `validate_pic` **(Compute Cores)** (Impact: 142.1)
  * `create_implicit_picture` **(Compute Cores)** (Impact: 93.6)
    * *Intent:* /* create an implicit picture for items that miss it but need one, return 1 if not possible */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 495 instances
* *State Mutation (weighted view):* 1504
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1091`, `structural_boundaries: 422`, `args: 117`, `func_start: 66`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 514`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 8`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, config.h, ctype.h, limits.h, stddef.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/move.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3194.4 | **LOC:** 2540 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_move_display_to_edited` **(Many-Argument Workhorses)** (Impact: 281.4)
    * *Intent:* /* Edited */
  * `cob_move` **(Many-Argument Workhorses)** (Impact: 269.6)
  * `cob_get_s64_pic9` **(Compute Cores)** (Impact: 65.0)
  * `cob_alloc_move` **(Many-Argument Workhorses)** (Impact: 62.9)
    * *Intent:* /* * Allocate storage as required and move data to dst field * The storage for these LINKAGE fields ...
  * `cob_move_edited_to_display` **(Many-Argument Workhorses)** (Impact: 61.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 519 instances
* *State Mutation (weighted view):* 1579
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 746`, `structural_boundaries: 269`, `args: 78`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 541`, `unreferenced_by_name: 33`
* *Architecture:* `api: 34`, `import: 11`
* *Defense:* `safety: 56`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` coblocal.h, config.h, ctype.h, errno.h, libcob.h, locale.h, math.h, stddef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/numeric.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2641.88 | **LOC:** 2689 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.8%), Complexity Load (formerly Cognitive Load) (90.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.5217% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_decimal_set_display` **(Many-Argument Workhorses)** (Impact: 544.6)
    * *Intent:* /* DISPLAY */
  * `cob_decimal_get_binary` **(Many-Argument Workhorses)** (Impact: 83.1)
  * `cob_decimal_do_round` **(Many-Argument Workhorses)** (Impact: 73.3)
  * `cob_decimal_get_field` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `cob_decimal_get_packed` **(Many-Argument Workhorses)** (Impact: 51.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 329 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 996
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 454`, `structural_boundaries: 224`, `args: 108`, `func_start: 70`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 338`, `fragile_debt: 3`, `unreferenced_by_name: 28`
* *Architecture:* `api: 40`, `import: 14`
* *Defense:* `safety: 36`, `doc: 2`, `immutability_locks: 57`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` coblocal.h, config.h, ctype.h, errno.h, gmp.h, ieeefp.h, libcob.h, math.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fbdb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2307.9 | **LOC:** 2009 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ix_bdb_read_next` **(Many-Argument Workhorses)** (Impact: 217.7)
    * *Intent:* /* Sequential READ of the INDEXED file */
  * `ix_bdb_open` **(Many-Argument Workhorses)** (Impact: 193.6)
    * *Intent:* /* OPEN INDEXED file */
  * `ix_bdb_start_internal` **(Many-Argument Workhorses)** (Impact: 119.8)
  * `bdb_lock_record` **(Many-Argument Workhorses)** (Impact: 66.8)
    * *Intent:* /* Impose lock on record and table it */
  * `bdb_test_record_lock` **(Many-Argument Workhorses)** (Impact: 60.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 344 instances
* *State Mutation (weighted view):* 1061
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 185`, `args: 42`, `func_start: 37`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 373`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 3`, `import: 2`
* *Defense:* `safety: 38`, `immutability_locks: 33`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` db.h, fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/sqlxfdgen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 2274.02 | **LOC:** 1440 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_redefines` **(Many-Argument Workhorses)** (Impact: 157.2)
  * `write_postfix` **(Many-Argument Workhorses)** (Impact: 139.8)
  * `cb_parse_xfd` **(Many-Argument Workhorses)** (Impact: 114.2)
  * `output_xfd_file` **(Compute Cores)** (Impact: 108.9)
    * *Intent:* /* Write out the DDL and XFD files */
  * `write_field` **(Many-Argument Workhorses)** (Impact: 83.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 394 instances
* *State Mutation (weighted view):* 1183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 530`, `structural_boundaries: 136`, `args: 30`, `func_start: 23`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 395`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 3`, `import: 12`
* *Defense:* `safety: 6`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, config.h, ctype.h, limits.h, stdarg.h, stddef.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fodbc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2196.16 | **LOC:** 1871 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 87.0968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chkSts` **(Many-Argument Workhorses)** (Impact: 142.7)
    * *Intent:* **************************************************/
  * `odbc_open` **(Many-Argument Workhorses)** (Impact: 141.6)
    * *Intent:* /* OPEN INDEXED file */
  * `join_environment` **(Compute Cores)** (Impact: 116.0)
    * *Intent:* /* INDEXED */
  * `odbc_read_next` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* /* Sequential READ of the INDEXED file */
  * `getOdbcMsg` **(Many-Argument Workhorses)** (Impact: 67.3)
    * *Intent:* #define szErrMsg 512 #define dbStsRetry (EAGAIN * 1000)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 367 instances
* *State Mutation (weighted view):* 1123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 448`, `structural_boundaries: 201`, `args: 55`, `func_start: 30`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 389`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 9`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fileio.h, sql.h, sqlca.h, sqlcli1.h, sqlext.h, sqludf.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fisam.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2075.46 | **LOC:** 1670 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 8.506; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isam_open` **(Many-Argument Workhorses)** (Impact: 244.7)
    * *Intent:* /* OPEN INDEXED file */
  * `isam_read_next` **(Many-Argument Workhorses)** (Impact: 211.2)
    * *Intent:* /* Sequential READ of the INDEXED file */
  * `isam_rewrite` **(Many-Argument Workhorses)** (Impact: 69.2)
    * *Intent:* /* REWRITE record to the INDEXED file */
  * `isam_read` **(Many-Argument Workhorses)** (Impact: 50.7)
    * *Intent:* /* Random READ of the INDEXED file */
  * `isam_start` **(Many-Argument Workhorses)** (Impact: 49.4)
    * *Intent:* /* START INDEXED file with positioning */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 351 instances
* *State Mutation (weighted view):* 1069
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 234`, `args: 92`, `func_start: 26`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 367`
* *Architecture:* `io: 1`, `api: 3`, `import: 5`
* *Defense:* `safety: 14`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.506
  * `Choke Point (Betweenness):` 0.000435 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 1):` disam.h, fileio.h, isam.h, isconfig.h, vbisam.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `libcob/reportio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1990.78 | **LOC:** 1836 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Complexity Load (formerly Cognitive Load) (81.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_report_generate` **(Many-Argument Workhorses)** (Impact: 180.4)
    * *Intent:* /* * GENERATE report-line */
  * `reportDumpOneLine` **(Many-Argument Workhorses)** (Impact: 121.7)
    * *Intent:* #endif #ifdef COB_DEBUG_LOG
  * `report_line` **(Many-Argument Workhorses)** (Impact: 112.5)
    * *Intent:* /* * GENERATE one report-line */
  * `dumpFlags` **(Many-Argument Workhorses)** (Impact: 78.7)
    * *Intent:* #ifdef COB_DEBUG_LOG
  * `cob_report_terminate` **(Many-Argument Workhorses)** (Impact: 76.1)
    * *Intent:* /* * TERMINATE report */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 301 instances
* *State Mutation (weighted view):* 918
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 486`, `structural_boundaries: 106`, `args: 52`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 316`, `planned_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`, `api: 6`, `import: 9`
* *Defense:* `safety: 6`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` coblocal.h, config.h, ctype.h, errno.h, libcob.h, stddef.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/foci.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1898.62 | **LOC:** 1664 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.2%)
- **Documentation Coverage:** 87.0968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `oci_open` **(Many-Argument Workhorses)** (Impact: 136.6)
    * *Intent:* /* OPEN INDEXED file */
  * `chkSts` **(Many-Argument Workhorses)** (Impact: 108.2)
    * *Intent:* **************************************************/
  * `oci_read_next` **(Many-Argument Workhorses)** (Impact: 85.3)
    * *Intent:* /* Sequential READ of the INDEXED file */
  * `join_environment` **(Compute Cores)** (Impact: 74.0)
    * *Intent:* /* INDEXED */
  * `oci_setup_stmt` **(Many-Argument Workhorses)** (Impact: 55.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 324 instances
* *State Mutation (weighted view):* 993
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 179`, `args: 32`, `func_start: 30`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 345`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 18`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fileio.h, oci.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/call.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1870.92 | **LOC:** 2319 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.8%)
- **Documentation Coverage:** 97.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_resolve_internal` **(Many-Argument Workhorses)** (Impact: 75.0)
  * `cob_call` **(Many-Argument Workhorses)** (Impact: 45.8)
  * `cob_init_call` **(Many-Argument Workhorses)** (Impact: 45.8)
  * `do_cancel_module` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `cob_call_field` **(Many-Argument Workhorses)** (Impact: 37.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 998
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 344`, `structural_boundaries: 298`, `args: 96`, `func_start: 58`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 1`, `state_mutation: 352`, `unreferenced_by_name: 34`
* *Architecture:* `io: 1`, `api: 45`, `import: 19`
* *Defense:* `safety: 44`, `doc: 2`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` coblocal.h, config.h, ctype.h, defaults.h, dlfcn.h, errno.h, libcob.h, ltdl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fextfh.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1727.72 | **LOC:** 1336 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EXTFH` **(Many-Argument Workhorses)** (Impact: 230.7)
    * *Intent:* /* * EXTFH: maybe called by user own 'callfh' routine * to call normal fileio routine in fileio.c */...
  * `copy_fcd_to_file` **(Many-Argument Workhorses)** (Impact: 105.2)
    * *Intent:* /* * Copy 'FCD' to 'cob_file' based information */
  * `copy_file_to_fcd` **(Many-Argument Workhorses)** (Impact: 97.1)
    * *Intent:* /* * Copy 'cob_file' to FCD based information */
  * `update_fcd_to_file` **(Many-Argument Workhorses)** (Impact: 63.5)
    * *Intent:* /* * Update 'cob_file' from 'FCD' information */
  * `update_file_to_fcd` **(Many-Argument Workhorses)** (Impact: 52.6)
    * *Intent:* /* * Update FCD from cob_file */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 290 instances
* *State Mutation (weighted view):* 890
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 111`, `args: 52`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 310`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/flmdb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1402.18 | **LOC:** 1563 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Guard Balance (formerly Safety Score) (93.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lmdb_open` **(Many-Argument Workhorses)** (Impact: 177.0)
  * `lmdb_read_next` **(Many-Argument Workhorses)** (Impact: 159.8)
    * *Intent:* /* Sequential READ of the INDEXED file */
  * `lmdb_start_internal` **(Many-Argument Workhorses)** (Impact: 104.6)
  * `lmdb_write_internal` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `lmdb_delete_internal` **(Many-Argument Workhorses)** (Impact: 43.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 202 instances
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 149`, `args: 52`, `func_start: 37`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 234`, `planned_debt: 15`
* *Architecture:* `io: 3`, `api: 3`, `import: 6`
* *Defense:* `safety: 30`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fileio.h, libgen.h, lmdb.h, file.h, stat.h, sysmacros.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/pplex.l` (YACC | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 1383.38 | **LOC:** 2165 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(I/O & Config Routines)** (Impact: 263.4)
  * `err_handling` **(I/O & Config Routines)** (Impact: 63.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 325 instances
* *State Mutation (weighted view):* 1022
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 397`, `structural_boundaries: 187`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 372`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `import: 9`
* *Defense:* `immutability_locks: 38`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, config.h, ctype.h, ppparse.h, string.h, stat.h, types.h, tree.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/scanner.l` (YACC | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1331.14 | **LOC:** 2489 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `error` **(I/O & Config Routines)** (Impact: 89.2)
  * `freevar` **(I/O & Config Routines)** (Impact: 47.2)
  * `error` **(I/O & Config Routines)** (Impact: 21.6)
  * `error` **(I/O & Config Routines)** (Impact: 18.9)
  * `error` **(I/O & Config Routines)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 352 instances
* *State Mutation (weighted view):* 1092
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 59`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 388`, `planned_debt: 4`, `fragile_debt: 7`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, config.h, ctype.h, limits.h, parser.h, tree.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/termio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1323.3 | **LOC:** 751 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 3.739; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `display_common` **(Many-Argument Workhorses)** (Impact: 367.1)
  * `display_alnum_dump` **(Many-Argument Workhorses)** (Impact: 147.4)
  * `cob_display` **(Many-Argument Workhorses)** (Impact: 104.8)
  * `cob_dump_field` **(Many-Argument Workhorses)** (Impact: 102.7)
    * *Intent:* /* Display field for DUMP purposes */
  * `cob_accept` **(Compute Cores)** (Impact: 31.4)
    * *Intent:* /* ACCEPT */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 455
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 41`, `args: 20`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 153`, `unreferenced_by_name: 7`
* *Architecture:* `io: 2`, `api: 6`, `import: 12`
* *Defense:* `safety: 6`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` coblocal.h, config.h, ctype.h, errno.h, libcob.h, stdarg.h, stddef.h, stdio.h...
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

- `libcob/fisam.c` -> **Severity: 0.043** (Bridge: 0.0004 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `libcob/sysdefines.h` -> **Severity: 4.793** (Embedded: 0.0872 * Error Risk: 54.9834%)
- `libcob/coblocal.h` -> **Severity: 4.644** (Embedded: 0.0682 * Error Risk: 68.0492%)
- `libcob/common.h` -> **Severity: 4.227** (Embedded: 0.0818 * Error Risk: 51.6705%)
- `cobc/tree.h` -> **Severity: 3.618** (Embedded: 0.0735 * Error Risk: 49.2035%)
- `libcob/fisam.c` -> **Severity: 1.461** (Embedded: 0.0147 * Error Risk: 99.3667%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libcob/exception.def` -> **Severity: 2632.5** (Blast Radius: 26.325 * Doc Risk: 100.0%)
- `libcob/coblocal.h` -> **Severity: 1999.1** (Blast Radius: 19.991 * Doc Risk: 100.0%)
- `libcob/fisam.c` -> **Severity: 850.6** (Blast Radius: 8.506 * Doc Risk: 100.0%)
- `cobc/config.def` -> **Severity: 790.1** (Blast Radius: 7.901 * Doc Risk: 100.0%)
- `cobc/flag.def` -> **Severity: 726.6** (Blast Radius: 7.266 * Doc Risk: 100.0%)

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
