# ARCHITECTURAL_BRIEF: gnucobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/paulsmith/gnucobol.git` |
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
- **Scope:** 217 analyzed artifact(s), 213423 LOC.
- **Load-bearing artifact:** `build_windows/config.h.in` -- 33 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `libcob/common.c` -- pulls in 48 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cobc/typeck.c` at magnitude 12394.6 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 217 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 165 |
| Total LOC | 213423 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 56.8% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5075 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3945 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2219 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| M4 | 80 | 83966 | 36.9% |
| C | 49 | 101307 | 22.6% |
| PLAINTEXT | 38 | 0 | 17.5% |
| SHELL | 12 | 1329 | 5.5% |
| MAKEFILE | 10 | 1654 | 4.6% |
| COBOL | 8 | 1309 | 3.7% |
| BATCH | 6 | 1091 | 2.8% |
| YACC | 4 | 20590 | 1.8% |
| MARKDOWN | 3 | 0 | 1.4% |
| PERL | 3 | 547 | 1.4% |
| POWERSHELL | 1 | 5 | 0.5% |
| CPP | 1 | 217 | 0.5% |
| PHP | 1 | 67 | 0.5% |
| LIVECODE | 1 | 1341 | 0.5% |

## 4.1 SOURCE ENCODINGS
> 3 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 214 |
| cp1252 | cp1252-fallback | 3 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 31%, Data / Markup / Trivial 22%, Large Core Modules 21%, Large Core Modules (3) 10%, Many-Argument Workhorses Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 176 | 81.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 41 | 18.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 165*

**Composition by Extension & Reason:**
- `.vcxproj`: 24x Excluded (Unsupported Extension: '.vcxproj')
- `.filters`: 24x Excluded (Unsupported Extension: '.filters')
- `.conf`: 19x Excluded (Unsupported Extension: '.conf')
- `.user`: 14x Excluded (Unsupported Extension: '.user')
- `.am`: 10x Excluded (Unsupported Extension: '.am')
- `.words`: 10x Excluded (Unsupported Extension: '.words')
- `no_extension`: 6x Unsupported Format (.undeterminable), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sln`: 8x Excluded (Unsupported Extension: '.sln')
- `.po`: 8x Excluded (Unsupported Extension: '.po')
- `.vcproj`: 6x Excluded (Unsupported Extension: '.vcproj')
- `.cpj`: 4x Excluded (Unsupported Extension: '.cpj')
- `.rc`: 4x Excluded (Unsupported Extension: '.rc')
- `.in`: 2x Unsupported Format (.undeterminable), 1x Zero-Density Threshold (LOC: 126, Signals: 0)
- `.cfg`: 2x Excluded (Unsupported Extension: '.cfg')
- `.texi`: 2x Excluded (Unsupported Extension: '.texi')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.2 | 20.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.7 | 29.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.3 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1110 | 44 | 13 | `libcob/common.c` |
| cleanup | 1270 | 58 | 12 | `tests/testsuite.src/run_misc.at` |
| guards | 7363 | 56 | 85 | `libcob/common.c` |
| danger | 1984 | 72 | 23 | `cobc/cobc.c` |
| concurrency | 25 | 11 | 0 | `build_aux/mkinstalldirs` |
| connectivity | 2661 | 82 | 16 | `libcob/common.h` |
| io | 626 | 46 | 5 | `doc/cobcinfo.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 129 | 7 | 0 | `tests/testsuite.src/numeric-dump.cob` |
| time | 43 | 14 | 0 | `tests/cobol85/report.pl` |
| serialization | 4 | 1 | 0 | `po/Makefile.in.in` |
| regex | 45 | 11 | 0 | `build_aux/create_mingw_bindist.sh` |
| events | 458 | 24 | 1 | `configure.ac` |
| tests | 6520 | 43 | 48 | `tests/testsuite.src/run_misc.at` |
| docs | 78 | 16 | 0 | `libcob/common.h` |
| debt | 1741 | 89 | 25 | `libcob/common.c` |
| mutation | 35706 | 130 | 500 | `cobc/parser.y` |
| dead_code | 877 | 77 | 6 | `cobc/typeck.c` |
| credential | 32 | 9 | 0 | `build_windows/set_env_vs_dist.bat` |
| threat | 4 | 1 | 0 | `libcob/fileio.c` |
| ml_ai | 164 | 26 | 1 | `m4/libtool.m4` |
| ui | 5 | 4 | 0 | `ABOUT-NLS` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/cobcinfo.sh` (Hits: 135)
- `libcob/fileio.c` (Hits: 66)
- `build_aux/compile` (Hits: 56)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.h.in** (`build_windows/config.h.in`) — 33 inbound connections
2. **common.c** (`libcob/common.c`) — 24 inbound connections
3. **cobc.h** (`cobc/cobc.h`) — 16 inbound connections
4. **tree.h** (`cobc/tree.h`) — 15 inbound connections
5. **libcob.h** (`libcob.h`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.c** (`libcob/common.c`) — 48 outbound dependencies
2. **cobc.c** (`cobc/cobc.c`) — 34 outbound dependencies
3. **testsuite.at** (`tests/testsuite.at`) — 34 outbound dependencies
4. **screenio.c** (`libcob/screenio.c`) — 21 outbound dependencies
5. **call.c** (`libcob/call.c`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `output_long_integer` **(Many-Argument Workhorses)** (@ `cobc/codegen.c`) -> Impact: **1056.2** | LOC: 2429
- `cob_gettmpdir` **(Compute Cores)** (@ `libcob/common.c`) -> Impact: **731.0** | LOC: 2399
- `cob_set_file_format` **(Many-Argument Workhorses)** (@ `libcob/fileio.c`) -> Impact: **631.1** | LOC: 592
  * *Intent:* /* * Set file format based on IO_filename options */
- `field_accept` **(Many-Argument Workhorses)** (@ `libcob/screenio.c`) -> Impact: **617.9** | LOC: 684
- `cob_decimal_set_display` **(Many-Argument Workhorses)** (@ `libcob/numeric.c`) -> Impact: **520.4** | LOC: 1470
  * *Intent:* /* DISPLAY */
- `cb_build_intrinsic` **(Many-Argument Workhorses)** (@ `cobc/tree.c`) -> Impact: **507.2** | LOC: 485
- `output_internal_function` **(Many-Argument Workhorses)** (@ `cobc/codegen.c`) -> Impact: **503.4** | LOC: 1200
- `cb_build_binary_op` **(Many-Argument Workhorses)** (@ `cobc/tree.c`) -> Impact: **442.4** | LOC: 487
  * *Intent:* /* Expression */
- `process_command_line` **(Many-Argument Workhorses)** (@ `cobc/cobc.c`) -> Impact: **408.9** | LOC: 973
  * *Intent:* /* process command line options */
- `output_call` **(Compute Cores)** (@ `cobc/codegen.c`) -> Impact: **368.9** | LOC: 703

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cobc` | 24 | 65339.62 | 41.3% | 14.54% |
| `libcob` | 31 | 56207.92 | 52.31% | 12.47% |
| `tests/testsuite.src` | 38 | 2185.66 | 0.73% | 0.0% |
| `m4` | 40 | 1706.14 | 2.07% | 46.24% |
| `bin` | 4 | 1065.78 | 33.55% | 10.56% |
| `build_aux` | 8 | 746.26 | 50.82% | 6.13% |
| `__monolith__` | 15 | 672.92 | 4.63% | 1.36% |
| `tests/cobol85` | 21 | 635.58 | 6.13% | 0.0% |
| `po` | 5 | 183.42 | 4.96% | 19.0% |
| `doc` | 2 | 182.42 | 19.32% | 5.88% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `m4/ltsugar.m4` -> **100.0%** Exposure
- `m4/extern-inline.m4` -> **99.9999%** Exposure
- `m4/longlong.m4` -> **99.9985%** Exposure
- `m4/wint_t.m4` -> **99.9925%** Exposure
- `m4/ltoptions.m4` -> **99.6986%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `build_aux/compile` -> **100.0%** Exposure
- `build_aux/ylwrap` -> **100.0%** Exposure
- `bin/gcdiff.c` -> **100.0%** Exposure
- `cobc/cobc.c` -> **100.0%** Exposure
- `cobc/config.c` -> **100.0%** Exposure
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
- **Unknown Dependencies:** `524` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cobc/typeck.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.105)
- **Top Global Matches:** file_cluster_6: 5.105, file_cluster_4: 11.104, file_cluster_8: 13.606
- **Magnitude:** 12394.6 | **LOC:** 13270 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **14**; blast radius 5.49; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.0%), Guard Balance (formerly Safety Score) (70.0%)
- **Documentation Coverage:** 98.6248% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_emit_call` **(Many-Argument Workhorses)** (Impact: 305.9)
  * `validate_move_from_num_lit` **(Many-Argument Workhorses)** (Impact: 250.9)
  * `cb_build_identifier` **(Many-Argument Workhorses)** (Impact: 206.3)
  * `cb_build_move_literal` **(Many-Argument Workhorses)** (Impact: 166.8)
  * `cb_validate_program_environment` **(Compute Cores)** (Impact: 158.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1595 instances
* *State Mutation (weighted view):* 4910
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3361`, `structural_boundaries: 1680`, `args: 777`, `func_start: 327`, `class_start: 177`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 1720`, `planned_debt: 50`, `fragile_debt: 19`, `unreferenced_by_name: 146`
* *Architecture:* `api: 167`, `import: 14`
* *Defense:* `safety: 70`, `doc: 4`, `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.49
  * `Choke Point (Betweenness):` 0.000952 | `Ripple Effect (Closeness):` 0.036916
  * `Imports (Out-Degree: 13):` cobc.h, config.h, ctype.h, system.def, limits.h, locale.h, stddef.h, stdio.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cobc/parser.y` (YACC | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.633)
- **Top Global Matches:** file_cluster_15: 9.633, file_cluster_4: 9.749, file_cluster_16: 10.062
- **Magnitude:** 11967.14 | **LOC:** 18380 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.4%), Guard Balance (formerly Safety Score) (67.6%)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2184`, `planned_debt: 25`, `fragile_debt: 41`
* *Architecture:* `io: 2`, `api: 2`, `import: 5`
* *Defense:* `safety: 22`, `immutability_locks: 115`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` cobc.h, config.h, stdlib.h, string.h, tree.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/codegen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.532)
- **Top Global Matches:** file_cluster_6: 9.532, file_cluster_8: 10.642, file_cluster_4: 16.865
- **Magnitude:** 11915.86 | **LOC:** 12938 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 4.212; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.5%)
- **Documentation Coverage:** 99.1489% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `output_long_integer` **(Many-Argument Workhorses)** (Impact: 1056.2)
  * `output_internal_function` **(Many-Argument Workhorses)** (Impact: 503.4)
  * `output_call` **(Compute Cores)** (Impact: 368.9)
  * `output_stmt` **(Compute Cores)** (Impact: 330.9)
  * `output_param` **(Many-Argument Workhorses)** (Impact: 231.3)
    * *Intent:* /* Parameter */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1487 instances
* *State Mutation (weighted view):* 4577
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3196`, `structural_boundaries: 1296`, `args: 446`, `func_start: 202`, `class_start: 210`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 1603`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 7`, `unreferenced_by_name: 3`
* *Architecture:* `api: 24`, `import: 13`
* *Defense:* `safety: 29`, `doc: 2`, `immutability_locks: 186`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.212
  * `Choke Point (Betweenness):` 0.000609 | `Ripple Effect (Closeness):` 0.033706
  * `Imports (Out-Degree: 12):` cobc.h, config.h, ctype.h, system.def, limits.h, stdarg.h, stddef.h, stdio.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `libcob/fileio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.689)
- **Top Global Matches:** file_cluster_8: 7.689, file_cluster_6: 12.628, file_cluster_4: 21.004
- **Magnitude:** 9230.24 | **LOC:** 7364 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 6.996; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_set_file_format` **(Many-Argument Workhorses)** (Impact: 631.1)
    * *Intent:* /* * Set file format based on IO_filename options */
  * `cob_file_open` **(Many-Argument Workhorses)** (Impact: 201.7)
    * *Intent:* #define dMaxArgs 16
  * `cob_fd_file_open` **(Many-Argument Workhorses)** (Impact: 180.8)
    * *Intent:* /* * Open (record) Sequential and Relative files * with just an 'fd' (No FILE *) */
  * `cob_file_save_status` **(Many-Argument Workhorses)** (Impact: 150.3)
  * `lineseq_write` **(Many-Argument Workhorses)** (Impact: 122.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1529 instances
* *High Risk Execution (weighted view):* 8
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 4678
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1893`, `structural_boundaries: 784`, `args: 209`, `func_start: 129`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 127`, `high_risk_execution: 9`, `state_mutation: 1620`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 47`
* *Architecture:* `io: 66`, `api: 70`, `import: 5`
* *Defense:* `safety: 136`, `doc: 3`, `immutability_locks: 121`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.996
  * `Choke Point (Betweenness):` 0.006884 | `Ripple Effect (Closeness):` 0.077928
  * `Imports (Out-Degree: 14):` defaults.h, dlfcn.h, fileio.h, signal.h, wait.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `libcob/common.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.995)
- **Top Global Matches:** file_cluster_6: 7.995, file_cluster_4: 11.905, file_cluster_8: 15.886
- **Magnitude:** 8745.0 | **LOC:** 8748 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **48**; blast radius 24.118; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.4%)
- **Documentation Coverage:** 99.4413% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_gettmpdir` **(Compute Cores)** (Impact: 731.0)
  * `cob_correct_numeric` **(Compute Cores)** (Impact: 156.6)
  * `get_config_val` **(Many-Argument Workhorses)** (Impact: 151.7)
    * *Intent:* /* Return setting value as a 'string' */
  * `check_current_date` **(I/O & Config Routines)** (Impact: 150.0)
  * `cb_config_entry` **(Many-Argument Workhorses)** (Impact: 145.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1308 instances
* *High Risk Execution (weighted view):* 5
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 4084
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1896`, `structural_boundaries: 980`, `args: 512`, `func_start: 204`, `class_start: 58`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 6`, `state_mutation: 1468`, `planned_debt: 4`, `fragile_debt: 4`, `unreferenced_by_name: 115`
* *Architecture:* `io: 14`, `api: 156`, `import: 49`
* *Defense:* `safety: 215`, `doc: 3`, `immutability_locks: 224`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.118
  * `Choke Point (Betweenness):` 0.015399 | `Ripple Effect (Closeness):` 0.127382
  * `Imports (Out-Degree: 19):` cJSON.h, cJSON.h, coblocal.h, config.h, ctype.h, curses.h, db.h, defaults.h...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `cobc/tree.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.137)
- **Top Global Matches:** file_cluster_6: 6.137, file_cluster_4: 7.616, file_cluster_16: 15.977
- **Magnitude:** 7356.1 | **LOC:** 6804 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **10**; blast radius 8.191; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_build_intrinsic` **(Many-Argument Workhorses)** (Impact: 507.2)
  * `cb_build_binary_op` **(Many-Argument Workhorses)** (Impact: 442.4)
    * *Intent:* /* Expression */
  * `compare_field_literal` **(Many-Argument Workhorses)** (Impact: 321.5)
    * *Intent:* /* Check if comparing field to literal is always TRUE or FALSE */
  * `cb_build_picture` **(Many-Argument Workhorses)** (Impact: 196.7)
  * `finalize_report` **(Many-Argument Workhorses)** (Impact: 156.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1007 instances
* *State Mutation (weighted view):* 3256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1716`, `structural_boundaries: 899`, `args: 301`, `func_start: 156`, `class_start: 157`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 1242`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 13`
* *Architecture:* `api: 172`, `import: 10`
* *Defense:* `safety: 118`, `immutability_locks: 236`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.191
  * `Choke Point (Betweenness):` 0.00053 | `Ripple Effect (Closeness):` 0.045602
  * `Imports (Out-Degree: 9):` cobc.h, config.h, ctype.h, limits.h, parser.h, stddef.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `cobc/cobc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.524)
- **Top Global Matches:** file_cluster_6: 8.524, file_cluster_4: 12.218, file_cluster_8: 16.448
- **Magnitude:** 7292.08 | **LOC:** 8434 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **34**; blast radius 10.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.3%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 99.5215% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_command_line` **(Many-Argument Workhorses)** (Impact: 408.9)
    * *Intent:* /* process command line options */
  * `print_replace_text` **(Many-Argument Workhorses)** (Impact: 156.4)
    * *Intent:* /* TODO: Modularise! */
  * `main` **(Many-Argument Workhorses)** (Impact: 109.1)
    * *Intent:* /* Main function */
  * `process_filename` **(Compute Cores)** (Impact: 105.3)
    * *Intent:* is to be processed, otherwise NULL */
  * `process` **(Compute Cores)** (Impact: 94.7)
    * *Intent:* #ifdef __OS400__
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1238 instances
* *High Risk Execution (weighted view):* 4
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 3841
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1593`, `structural_boundaries: 749`, `args: 350`, `func_start: 155`, `class_start: 90`
* *Risk/State:* `safety_bypasses: 244`, `high_risk_execution: 5`, `state_mutation: 1365`, `planned_debt: 4`, `fragile_debt: 9`
* *Architecture:* `io: 25`, `api: 47`, `import: 41`
* *Defense:* `safety: 171`, `doc: 1`, `immutability_locks: 186`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.603
  * `Choke Point (Betweenness):` 0.006225 | `Ripple Effect (Closeness):` 0.059633
  * `Imports (Out-Degree: 20):` cobc.h, config.def, config.h, ctype.h, db.h, defaults.h, direct.h, fcntl.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `libcob/intrinsic.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.457)
- **Top Global Matches:** file_cluster_4: 7.457, file_cluster_16: 8.706, file_cluster_15: 9.618
- **Magnitude:** 4886.76 | **LOC:** 6809 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **19**; blast radius 7.734; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%)
- **Documentation Coverage:** 98.9899% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_check_numval` **(Many-Argument Workhorses)** (Impact: 230.2)
    * *Intent:* /* TEST-NUMVAL implementation */ /* Validate NUMVAL / NUMVAL-C item */ /* [spaces][+|-][spaces]{digi...
  * `cob_check_numval_f` **(Compute Cores)** (Impact: 93.1)
    * *Intent:* /* Validate NUMVAL-F item */ /* sp = spaces */ /* [sp][+|-][sp]{digits[.[digits]]|.digits}[sp][E[sp]...
  * `cob_intr_locale_date` **(Many-Argument Workhorses)** (Impact: 55.2)
  * `numval` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `cob_intr_numval_f` **(Compute Cores)** (Impact: 51.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 773 instances
* *State Mutation (weighted view):* 2396
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 860`, `structural_boundaries: 577`, `args: 354`, `func_start: 233`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 850`, `fragile_debt: 2`, `unreferenced_by_name: 112`
* *Architecture:* `io: 5`, `api: 124`, `import: 19`
* *Defense:* `safety: 138`, `doc: 2`, `immutability_locks: 281`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.000348 | `Ripple Effect (Closeness):` 0.083846
  * `Imports (Out-Degree: 6):` coblocal.h, config.h, ctype.h, errno.h, gmp.h, langinfo.h, libcob.h, locale.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `libcob/fsqlxfd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.78)
- **Top Global Matches:** file_cluster_8: 12.78, file_cluster_3: 15.698, file_cluster_6: 24.013
- **Magnitude:** 4354.5 | **LOC:** 2449 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 6.667; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.8%), Complexity Load (formerly Cognitive Load) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 83.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_sql_stmt` **(Many-Argument Workhorses)** (Impact: 323.1)
    * *Intent:* /* * Build SQL Statement and return as malloced string */
  * `cob_load_xfd` **(Many-Argument Workhorses)** (Impact: 222.0)
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
* *Structure:* `branch: 816`, `structural_boundaries: 180`, `args: 50`, `func_start: 38`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 115`, `state_mutation: 802`, `unreferenced_by_name: 15`
* *Architecture:* `io: 5`, `api: 20`, `import: 2`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.044455
  * `Imports (Out-Degree: 4):` defaults.h, fileio.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cobc/field.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.583)
- **Top Global Matches:** file_cluster_8: 8.583, file_cluster_6: 9.124, file_cluster_4: 17.339
- **Magnitude:** 3483.98 | **LOC:** 3249 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 5.319; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compute_size` **(Compute Cores)** (Impact: 249.6)
  * `cb_build_field_tree` **(Many-Argument Workhorses)** (Impact: 196.9)
  * `compute_binary_size` **(Compute Cores)** (Impact: 171.5)
  * `validate_pic` **(Compute Cores)** (Impact: 142.1)
  * `cb_evaluate_expr` **(Many-Argument Workhorses)** (Impact: 87.7)
    * *Intent:* /* Evaluate expression and store as new Numeric Literal */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 495 instances
* *State Mutation (weighted view):* 1504
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1068`, `structural_boundaries: 422`, `args: 117`, `func_start: 66`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 514`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 8`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 94`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.319
  * `Choke Point (Betweenness):` 0.000166 | `Ripple Effect (Closeness):` 0.036916
  * `Imports (Out-Degree: 8):` cobc.h, config.h, ctype.h, limits.h, stddef.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `libcob/screenio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.049)
- **Top Global Matches:** file_cluster_4: 5.049, file_cluster_6: 10.083, file_cluster_16: 11.103
- **Magnitude:** 3416.4 | **LOC:** 3613 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 4.778; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `field_accept` **(Many-Argument Workhorses)** (Impact: 617.9)
  * `cob_screen_get_all` **(Many-Argument Workhorses)** (Impact: 223.9)
    * *Intent:* #endif
  * `cob_convert_key` **(Many-Argument Workhorses)** (Impact: 77.3)
  * `mouse_to_exception_code` **(Compute Cores)** (Impact: 74.8)
    * *Intent:* #ifdef NCURSES_MOUSE_VERSION
  * `field_display` **(Many-Argument Workhorses)** (Impact: 64.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 491 instances
* *State Mutation (weighted view):* 1518
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 720`, `structural_boundaries: 286`, `args: 164`, `func_start: 90`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 536`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 13`
* *Architecture:* `io: 2`, `api: 33`, `import: 21`
* *Defense:* `safety: 36`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.778
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.075271
  * `Imports (Out-Degree: 7):` coblocal.h, config.h, ctype.h, curses.h, errno.h, io.h, libcob.h, limits.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `libcob/move.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 4.785)
- **Top Global Matches:** file_cluster_6: 4.785, file_cluster_4: 10.092, file_cluster_8: 14.607
- **Magnitude:** 3152.7 | **LOC:** 2540 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **11**; blast radius 15.283; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%), Complexity Load (formerly Cognitive Load) (78.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_move_display_to_edited` **(Many-Argument Workhorses)** (Impact: 279.7)
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
* *Structure:* `branch: 722`, `structural_boundaries: 269`, `args: 78`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 541`, `unreferenced_by_name: 33`
* *Architecture:* `api: 34`, `import: 11`
* *Defense:* `safety: 56`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.283
  * `Choke Point (Betweenness):` 0.000373 | `Ripple Effect (Closeness):` 0.090738
  * `Imports (Out-Degree: 6):` coblocal.h, config.h, ctype.h, errno.h, libcob.h, locale.h, math.h, stddef.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `libcob/numeric.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.3)
- **Top Global Matches:** file_cluster_4: 6.3, file_cluster_6: 8.204, file_cluster_16: 13.72
- **Magnitude:** 2544.78 | **LOC:** 2689 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **14**; blast radius 10.221; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.8%)
- **Documentation Coverage:** 96.5217% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_decimal_set_display` **(Many-Argument Workhorses)** (Impact: 520.4)
    * *Intent:* /* DISPLAY */
  * `cob_decimal_get_binary` **(Many-Argument Workhorses)** (Impact: 75.1)
  * `cob_decimal_do_round` **(Many-Argument Workhorses)** (Impact: 73.3)
  * `cob_decimal_get_field` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `cob_cmp_packed` **(Many-Argument Workhorses)** (Impact: 41.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 323 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 984
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 224`, `args: 108`, `func_start: 70`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 338`, `fragile_debt: 3`, `unreferenced_by_name: 28`
* *Architecture:* `api: 40`, `import: 14`
* *Defense:* `safety: 36`, `doc: 2`, `immutability_locks: 57`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.221
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.081776
  * `Imports (Out-Degree: 5):` coblocal.h, config.h, ctype.h, errno.h, gmp.h, ieeefp.h, libcob.h, math.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `libcob/fbdb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.483)
- **Top Global Matches:** file_cluster_8: 6.483, file_cluster_6: 11.116, file_cluster_4: 19.743
- **Magnitude:** 2272.7 | **LOC:** 2009 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 3.561; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.3%), Guard Balance (formerly Safety Score) (75.5%)
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
* *Amplified Cascading Flux:* 341 instances
* *State Mutation (weighted view):* 1055
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 185`, `args: 42`, `func_start: 37`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 373`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 3`, `import: 2`
* *Defense:* `safety: 38`, `immutability_locks: 33`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.561
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.054743
  * `Imports (Out-Degree: 3):` db.h, fileio.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobc/sqlxfdgen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.907)
- **Top Global Matches:** file_cluster_3: 11.907, file_cluster_8: 15.327, file_cluster_6: 27.475
- **Magnitude:** 2248.82 | **LOC:** 1440 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 3.999; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Complexity Load (formerly Cognitive Load) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_redefines` **(Many-Argument Workhorses)** (Impact: 157.2)
  * `write_postfix` **(Many-Argument Workhorses)** (Impact: 121.8)
  * `cb_parse_xfd` **(Many-Argument Workhorses)** (Impact: 114.2)
  * `output_xfd_file` **(Compute Cores)** (Impact: 108.9)
    * *Intent:* /* Write out the DDL and XFD files */
  * `write_field` **(Many-Argument Workhorses)** (Impact: 83.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 392 instances
* *State Mutation (weighted view):* 1179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 136`, `args: 30`, `func_start: 23`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 395`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 3`, `import: 12`
* *Defense:* `safety: 6`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.999
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025841
  * `Imports (Out-Degree: 6):` cobc.h, config.h, ctype.h, limits.h, stdarg.h, stddef.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `libcob/fodbc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.298)
- **Top Global Matches:** file_cluster_6: 9.298, file_cluster_8: 9.954, file_cluster_4: 17.128
- **Magnitude:** 2187.76 | **LOC:** 1871 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 3.561; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.1%)
- **Documentation Coverage:** 87.0968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `odbc_open` **(Many-Argument Workhorses)** (Impact: 139.1)
    * *Intent:* /* OPEN INDEXED file */
  * `chkSts` **(Many-Argument Workhorses)** (Impact: 138.2)
    * *Intent:* **************************************************/
  * `join_environment` **(Compute Cores)** (Impact: 114.6)
    * *Intent:* /* INDEXED */
  * `odbc_read_next` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* /* Sequential READ of the INDEXED file */
  * `getOdbcMsg` **(Many-Argument Workhorses)** (Impact: 67.3)
    * *Intent:* #define szErrMsg 512 #define dbStsRetry (EAGAIN * 1000)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 367 instances
* *State Mutation (weighted view):* 1123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 201`, `args: 55`, `func_start: 30`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 389`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 9`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.561
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.054294
  * `Imports (Out-Degree: 4):` fileio.h, sql.h, sqlca.h, sqlcli1.h, sqlext.h, sqludf.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `libcob/fisam.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.13)
- **Top Global Matches:** file_cluster_8: 10.13, file_cluster_6: 19.567, file_cluster_3: 20.103
- **Magnitude:** 2044.36 | **LOC:** 1670 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 7.559; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isam_open` **(Many-Argument Workhorses)** (Impact: 239.8)
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
* *Amplified Cascading Flux:* 345 instances
* *State Mutation (weighted view):* 1057
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 234`, `args: 92`, `func_start: 26`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 367`
* *Architecture:* `io: 1`, `api: 3`, `import: 5`
* *Defense:* `safety: 14`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.559
  * `Choke Point (Betweenness):` 0.001839 | `Ripple Effect (Closeness):` 0.059142
  * `Imports (Out-Degree: 3):` disam.h, fileio.h, isam.h, isconfig.h, vbisam.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `libcob/reportio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.411)
- **Top Global Matches:** file_cluster_6: 7.411, file_cluster_8: 8.883, file_cluster_4: 15.764
- **Magnitude:** 1946.28 | **LOC:** 1836 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 4.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_report_generate` **(Many-Argument Workhorses)** (Impact: 166.4)
    * *Intent:* /* * GENERATE report-line */
  * `reportDumpOneLine` **(Many-Argument Workhorses)** (Impact: 121.7)
    * *Intent:* #endif #ifdef COB_DEBUG_LOG
  * `report_line` **(Many-Argument Workhorses)** (Impact: 110.8)
    * *Intent:* /* * GENERATE one report-line */
  * `dumpFlags` **(Many-Argument Workhorses)** (Impact: 78.7)
    * *Intent:* #ifdef COB_DEBUG_LOG
  * `cob_report_terminate` **(Many-Argument Workhorses)** (Impact: 65.7)
    * *Intent:* /* * TERMINATE report */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 298 instances
* *State Mutation (weighted view):* 912
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 106`, `args: 52`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 316`, `planned_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`, `api: 6`, `import: 9`
* *Defense:* `safety: 6`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074425
  * `Imports (Out-Degree: 7):` coblocal.h, config.h, ctype.h, errno.h, libcob.h, stddef.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `libcob/foci.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.786)
- **Top Global Matches:** file_cluster_6: 8.786, file_cluster_8: 13.364, file_cluster_4: 14.992
- **Magnitude:** 1890.12 | **LOC:** 1664 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 3.561; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.0%)
- **Documentation Coverage:** 87.0968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `oci_open` **(Many-Argument Workhorses)** (Impact: 134.1)
    * *Intent:* /* OPEN INDEXED file */
  * `chkSts` **(Many-Argument Workhorses)** (Impact: 102.2)
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
* *Structure:* `branch: 370`, `structural_boundaries: 179`, `args: 32`, `func_start: 30`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 345`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 18`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.561
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.054294
  * `Imports (Out-Degree: 4):` fileio.h, oci.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `libcob/call.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.865)
- **Top Global Matches:** file_cluster_4: 5.865, file_cluster_12: 10.007, file_cluster_16: 10.873
- **Magnitude:** 1772.72 | **LOC:** 2319 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **19**; blast radius 5.593; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%), Complexity Load (formerly Cognitive Load) (66.4%)
- **Documentation Coverage:** 97.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cob_resolve_internal` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `cob_init_call` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `do_cancel_module` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `cob_call_field` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `cob_encode_program_id` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 319 instances
* *State Mutation (weighted view):* 990
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 298`, `args: 96`, `func_start: 58`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 1`, `state_mutation: 352`, `unreferenced_by_name: 34`
* *Architecture:* `io: 1`, `api: 45`, `import: 19`
* *Defense:* `safety: 44`, `doc: 2`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.593
  * `Choke Point (Betweenness):` 0.000665 | `Ripple Effect (Closeness):` 0.080779
  * `Imports (Out-Degree: 8):` coblocal.h, config.h, ctype.h, defaults.h, dlfcn.h, errno.h, libcob.h, ltdl.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `libcob/fextfh.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.535)
- **Top Global Matches:** file_cluster_6: 6.535, file_cluster_8: 9.991, file_cluster_4: 14.633
- **Magnitude:** 1715.62 | **LOC:** 1336 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 3.561; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EXTFH` **(Many-Argument Workhorses)** (Impact: 225.5)
    * *Intent:* /* * EXTFH: maybe called by user own 'callfh' routine * to call normal fileio routine in fileio.c */...
  * `copy_fcd_to_file` **(Many-Argument Workhorses)** (Impact: 101.7)
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
* *Structure:* `branch: 365`, `structural_boundaries: 111`, `args: 52`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 310`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.054294
  * `Imports (Out-Degree: 4):` fileio.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `libcob/flmdb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.976)
- **Top Global Matches:** file_cluster_6: 5.976, file_cluster_4: 9.747, file_cluster_8: 15.702
- **Magnitude:** 1384.18 | **LOC:** 1563 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 3.561; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lmdb_open` **(Many-Argument Workhorses)** (Impact: 177.0)
  * `lmdb_read_next` **(Many-Argument Workhorses)** (Impact: 153.8)
    * *Intent:* /* Sequential READ of the INDEXED file */
  * `lmdb_start_internal` **(Many-Argument Workhorses)** (Impact: 102.1)
  * `lmdb_write_internal` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `lmdb_delete_internal` **(Many-Argument Workhorses)** (Impact: 40.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 632
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 149`, `args: 52`, `func_start: 37`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 234`, `planned_debt: 15`
* *Architecture:* `io: 3`, `api: 3`, `import: 6`
* *Defense:* `safety: 30`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.561
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.054743
  * `Imports (Out-Degree: 3):` fileio.h, libgen.h, lmdb.h, file.h, stat.h, sysmacros.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobc/pplex.l` (YACC | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.654)
- **Top Global Matches:** file_cluster_1: 6.654, file_cluster_3: 48.326, file_cluster_8: 70.109
- **Magnitude:** 1383.38 | **LOC:** 2165 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%), Complexity Load (formerly Cognitive Load) (73.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` cobc.h, config.h, ctype.h, ppparse.h, string.h, stat.h, types.h, tree.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/scanner.l` (YACC | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.397)
- **Top Global Matches:** file_cluster_3: 8.397, file_cluster_8: 21.537, file_cluster_6: 34.165
- **Magnitude:** 1331.14 | **LOC:** 2489 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%), Complexity Load (formerly Cognitive Load) (69.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` cobc.h, config.h, ctype.h, limits.h, parser.h, tree.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/termio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.558)
- **Top Global Matches:** file_cluster_8: 10.558, file_cluster_3: 15.481, file_cluster_6: 22.343
- **Magnitude:** 1318.1 | **LOC:** 751 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 4.64; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `display_common` **(Many-Argument Workhorses)** (Impact: 361.9)
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
* *Structure:* `branch: 219`, `structural_boundaries: 41`, `args: 20`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 153`, `unreferenced_by_name: 7`
* *Architecture:* `io: 2`, `api: 6`, `import: 12`
* *Defense:* `safety: 6`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.64
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.075271
  * `Imports (Out-Degree: 7):` coblocal.h, config.h, ctype.h, errno.h, libcob.h, stdarg.h, stddef.h, stdio.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `po/Makefile.in.in` (MAKEFILE) | Magnitude: 137.32 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 111, indent_tabs: 94, structural_boundaries: 89, core_var_decl: 82

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `cobc/parser.y` (YACC) | Magnitude: 11967.14 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 5901, indent_spaces: 3835, branch: 3495, args: 2397

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/testsuite.at` (M4) | Magnitude: 15.9 | Delta: **0.211** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 34, test: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `cobc/ppparse.y` (YACC) | Magnitude: 1137.44 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 583, state_mutation: 271, branch: 259, indent_spaces: 241

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `libcob/common.c` -> **Severity: 1.54** (Bridge: 0.0154 * Flux: 100.0%)
- `libcob/fileio.c` -> **Severity: 0.688** (Bridge: 0.0069 * Flux: 100.0%)
- `cobc/cobc.c` -> **Severity: 0.622** (Bridge: 0.0062 * Flux: 100.0%)
- `libcob/fisam.c` -> **Severity: 0.184** (Bridge: 0.0018 * Flux: 100.0%)
- `cobc/typeck.c` -> **Severity: 0.095** (Bridge: 0.001 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `libcob/common.c` -> **Severity: 9.471** (Embedded: 0.1274 * Error Risk: 74.3541%)
- `libcob/move.c` -> **Severity: 7.175** (Embedded: 0.0907 * Error Risk: 79.0713%)
- `libcob/cobgetopt.c` -> **Severity: 7.09** (Embedded: 0.0883 * Error Risk: 80.2828%)
- `libcob/fileio.c` -> **Severity: 6.347** (Embedded: 0.0779 * Error Risk: 81.4491%)
- `libcob/termio.c` -> **Severity: 6.12** (Embedded: 0.0753 * Error Risk: 81.3001%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libcob/common.c` -> **Severity: 2398.325** (Blast Radius: 24.118 * Doc Risk: 99.4413%)
- `lib/gettext.h` -> **Severity: 2143.9** (Blast Radius: 21.439 * Doc Risk: 100.0%)
- `libcob/exception.def` -> **Severity: 2121.5** (Blast Radius: 21.215 * Doc Risk: 100.0%)
- `libcob/coblocal.h` -> **Severity: 1545.4** (Blast Radius: 15.454 * Doc Risk: 100.0%)
- `libcob/move.c` -> **Severity: 1528.3** (Blast Radius: 15.283 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `7` files carry mainframe facts -- `111` call sites, `0` dataset bindings, `540` record items.

### `tests/testsuite.src/numeric-dump.cob` (COBOL)
- **Calls:** `CALL dump`
- **Record layouts (108 items):** `G-1 (3)`, `G-2 (3)`, `G-3 (3)`, `G-4 (3)`, `G-5 (3)`, `G-6 (3)`, `G-7 (3)`, `G-8 (3)`, `G-9 (3)`, `G-10 (3)`, `G-11 (3)`, `G-12 (3)` … (+24 more)
- **Data moves:** 72 (INITIALIZE 36, MOVE 36)

### `copy/xfhfcd3.cpy` (COBOL)
- **Record layouts (221 items):** `FCD-FILE-FORMAT (22)`, `FCD-DEVICE-FLAG (15)`, `FCD-STATUS-TYPE (10)`, `FCD-OTHER-FLAGS (10)`, `FCD-CONFIG-FLAGS2 (10)`, `FCD-LOCK-MODE (10)`, `FCD-FLAGS-1 (9)`, `FCD-TRANS-LOG (9)`, `FCD-MISC-FLAGS (9)`, `FCD-LOCKTYPES (8)`, `FCD-OPEN-MODE (7)`, `FCD-MVS-FLAGS (7)` … (+62 more)

### `tests/testsuite.src/tutorial.cob` (COBOL)
- **Calls:** `CALL EXTFH`
- **Record layouts (58 items):** `EX-KEYDEF (41)`, `OPCODE (11)`, `EX-RECORD (3)`, `FCD (1)`, `EX-FILENAME (1)`, `EX-INDEX-NAME (1)`
- **Data moves:** 48 (ACCEPT 2, ADD 3, MOVE 43); most-fed items `OPCODE`, `FCD-OPEN-MODE`, `FCD-ORGANIZATION`, `FCD-VERSION`, `FCD-ACCESS-MODE`, `FCD-FILE-FORMAT`

### `copy/sqlda.cpy` (COBOL)
- **Record layouts (54 items):** `SQLDA (54)`

### `extras/CBL_OC_DUMP.cob` (COBOL)
- **Calls:** `CALL C$PARAMSIZE`, `CALL CBL_GC_PRINTABLE`
- **Record layouts (39 items):** `DISP-LINE (10)`, `CHAR-SET (4)`, `ARCHITECTURE (3)`, `ENDIAN-ORDER (3)`, `EXTENDED-INFOS (3)`, `WAS-CALLED-BEFORE (2)`, `HEX-TAB-RED (2)`, `ADDR (1)`, `COUNTER (1)`, `BYLINE (1)`, `LEN (1)`, `DOTS (1)` … (+7 more)
- **Data moves:** 13 (ACCEPT 2, MOVE 11); most-fed items `BYTE`, `DOTS`, `HEX-DISP-VAL`, `LEN`, `LEN-DISPLAY`, `OFFSET`

### `tests/testsuite.src/numeric-display.cob` (COBOL)
- **Record layouts (36 items):** `X-P1 (1)`, `X-P2 (1)`, `X-P3 (1)`, `X-P4 (1)`, `X-P5 (1)`, `X-P6 (1)`, `X-P7 (1)`, `X-P8 (1)`, `X-P9 (1)`, `X-P10 (1)`, `X-P11 (1)`, `X-P12 (1)` … (+24 more)

### `copy/sqlca.cpy` (COBOL)
- **Record layouts (24 items):** `SQLCA (24)`

- **Mainframe skeleton completeness:** 45% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: application programs (source or load-module list) (111 gaps); JCL and PROC libraries (4 gaps).

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1102 literal sites + 2 sites through wrappers = 1104
- **`memory_alloc`:** 24 literal sites + 89 sites through wrappers = 113

- `cobc_free` (function, memory_alloc, primitive): 71 call sites in 3 files -- `cobc/cobc.c`
- `cob_gmp_free` (function, memory_alloc, primitive): 8 call sites in 2 files -- `libcob/numeric.c`
- `print_program_listing` (function, memory_alloc, via cobc_free): 5 call sites in 1 files -- `cobc/cobc.c`
- `cleanup_copybook_reference` (function, memory_alloc, via cobc_free): 3 call sites in 1 files -- `cobc/cobc.c`
- `print_list` (function, debug_prints, primitive): 2 call sites in 1 files -- `cobc/debug.c`
- `free_list_skip` (function, memory_alloc, via cobc_free): 1 call sites in 1 files -- `cobc/cobc.c`
- `pretty_print` (function, memory_alloc, primitive): 1 call sites in 1 files -- `cobc/debug.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 16646 call pairs -- scoped 24.4%, unique 19.3%, ambiguous 0.2%, external 56.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 12743 | 30.0% | 18.9% | 0.2% | 50.8% |
| yacc | 1937 | 0.0% | 39.9% | 0.0% | 60.1% |
| m4 | 1067 | 17.2% | 2.0% | 0.0% | 80.8% |
| livecode | 738 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 102 | 17.6% | 0.0% | 0.0% | 82.4% |
| perl | 18 | 0.0% | 0.0% | 0.0% | 100.0% |
| batch | 17 | 100.0% | 0.0% | 0.0% | 0.0% |
| cobol | 12 | 66.7% | 0.0% | 0.0% | 33.3% |
| cpp | 12 | 0.0% | 0.0% | 0.0% | 100.0% |

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
