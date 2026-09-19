# ARCHITECTURAL_BRIEF: sqlite
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sqlite/sqlite.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 568 analyzed artifact(s), 312327 LOC.
- **Load-bearing artifact:** `src/sqliteInt.h` -- 107 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `autosetup/jimsh0.c` -- pulls in 38 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `autosetup/jimsh0.c` at magnitude 21433.94 (structural weight, not risk).
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
| Total Artifacts | 2200 |
| Analyzed Artifacts (Scanned) | 568 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1632 |
| Total LOC | 312327 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 25.8% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6968 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.302 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8622 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 40 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 314 | 267384 | 55.3% |
| TCL | 60 | 12775 | 10.6% |
| JAVA | 58 | 8157 | 10.2% |
| JAVASCRIPT | 37 | 16442 | 6.5% |
| MARKDOWN | 26 | 0 | 4.6% |
| HTML | 18 | 2239 | 3.2% |
| SHELL | 14 | 2245 | 2.5% |
| PLAINTEXT | 13 | 0 | 2.3% |
| SQLITE | 11 | 826 | 1.9% |
| MAKEFILE | 7 | 1450 | 1.2% |
| CSS | 2 | 122 | 0.4% |
| BATCH | 2 | 246 | 0.4% |
| M4 | 2 | 20 | 0.4% |
| CSHARP | 2 | 307 | 0.4% |
| XML | 1 | 0 | 0.2% |
| YACC | 1 | 114 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.604`
> **Composition Archetype:** `Hub-Coupled App` (z +2.60; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 18%, Data / Markup / Trivial 17%, Encapsulated Accessors Files 17%, Declarative / Non-Code 15%, Many-Argument Workhorses Files 13%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 529 | 93.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 39 | 6.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1632*

**Composition by Extension & Reason:**
- `.test`: 1466x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.test)
- `.tcl`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 167 LOC), 1x Excluded (Machine-Generated Source Code Signature: 466 LOC)
- `.c`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 6204 LOC), 1x Excluded (Machine-Generated Source Code Signature: 384 LOC)
- `.db`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.linux-generic'), 1x Excluded (Lexical Monotony: High structural repetition detected in 2205 LOC)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 24429 LOC), 1x Unsupported Format (.undeterminable)
- `.in`: 1x Excluded (Machine-Generated Source Code Signature: 560 LOC), 1x Excluded (Machine-Generated Source Code Signature: 51 LOC), 1x Excluded (Machine-Generated Source Code Signature: 41 LOC)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1297 LOC)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.msc`: 2x Excluded (Unsupported Extension: '.msc')
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.def`: 2x Unsupported Format (.undeterminable)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 162 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2472 LOC)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 49.5 | 64.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 69.8 | 90.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.3 | 11.7 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 35.5 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.3 | 2.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 71.2 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.5 | 1.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.0 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 106200 | 330 | 434 | `autosetup/jimsh0.c` |
| cleanup | 554 | 123 | 2 | `ext/wasm/tester1.c-pp.js` |
| guards | 28303 | 427 | 116 | `autosetup/jimsh0.c` |
| danger | 5809 | 341 | 24 | `autosetup/autosetup` |
| concurrency | 589 | 66 | 1 | `ext/wasm/api/sqlite3-vfs-opfs.c-pp.js` |
| connectivity | 7750 | 404 | 27 | `src/sqliteInt.h` |
| io | 1128 | 147 | 5 | `autosetup/autosetup` |
| crypto | 0 | 0 | 0 | - |
| ipc | 114 | 36 | 0 | `autosetup/jimsh0.c` |
| time | 109 | 36 | 0 | `ext/wasm/api/sqlite3-vfs-opfs.c-pp.js` |
| serialization | 32 | 15 | 0 | `ext/wasm/GNUmakefile` |
| regex | 99 | 33 | 0 | `ext/wasm/GNUmakefile` |
| events | 271 | 54 | 0 | `contrib/sqlitecon.tcl` |
| tests | 121 | 27 | 0 | `test/modeA.sql` |
| docs | 1616 | 168 | 3 | `tool/GetFile.cs` |
| debt | 2549 | 272 | 10 | `tool/lemon.c` |
| mutation | 92478 | 438 | 374 | `autosetup/jimsh0.c` |
| dead_code | 2187 | 342 | 10 | `ext/jni/src/org/sqlite/jni/wrapper1/Sqlite.java` |
| credential | 4 | 4 | 0 | `ext/misc/base64.c` |
| threat | 3378 | 223 | 13 | `src/sqliteInt.h` |
| ml_ai | 483 | 78 | 1 | `ext/fts3/unicode/mkunicode.tcl` |
| ui | 138 | 31 | 0 | `contrib/sqlitecon.tcl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `autosetup/autosetup` (Hits: 91)
- `ext/wasm/index.html` (Hits: 78)
- `tool/mkvsix.tcl` (Hits: 50)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sqliteInt.h** (`src/sqliteInt.h`) — 107 inbound connections
2. **sqlite3ext.h** (`src/sqlite3ext.h`) — 61 inbound connections
3. **tclsqlite.h** (`src/tclsqlite.h`) — 43 inbound connections
4. **vdbeInt.h** (`src/vdbeInt.h`) — 15 inbound connections
5. **testing.css** (`ext/wasm/common/testing.css`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **jimsh0.c** (`autosetup/jimsh0.c`) — 38 outbound dependencies
2. **sqliteInt.h** (`src/sqliteInt.h`) — 26 outbound dependencies
3. **shell.c.in** (`src/shell.c.in`) — 24 outbound dependencies
4. **os_unix.c** (`src/os_unix.c`) — 21 outbound dependencies
5. **fileio.c** (`ext/misc/fileio.c`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `do_meta_command` **(Many-Argument Workhorses)** (@ `src/shell.c.in`) -> Impact: **1227.5** | LOC: 1686
  * *Intent:* /* ** If an input line begins with "." then invoke this routine to ** process that line. ** ** Return 1 on error, 2 to exit, and 0 otherwise. */
- `DbObjCmd` **(Many-Argument Workhorses)** (@ `src/tclsqlite.c`) -> Impact: **1139.7** | LOC: 1775
  * *Intent:* /* ** The "sqlite" command below creates a new Tcl command for each ** connection it opens to an SQLite database. This routine is invoked ** whenever ...
- `winRead` **(Many-Argument Workhorses)** (@ `src/os_win.c`) -> Impact: **948.9** | LOC: 2162
  * *Intent:* /* ** Read data from a file into a buffer. Return SQLITE_OK if all ** bytes were read successfully and SQLITE_IOERR if anything goes ** wrong. */
- `winWrite` **(Many-Argument Workhorses)** (@ `src/os_win.c`) -> Impact: **942.2** | LOC: 2208
  * *Intent:* /* ** Write data from a buffer into a file. Return SQLITE_OK on success ** or some other error code on failure. */
- `sqlite3VdbeExec` **(Many-Argument Workhorses)** (@ `src/vdbe.c`) -> Impact: **895.9** | LOC: 2899
  * *Intent:* /* ** Execute as much of a VDBE program as we can. ** This is the core of sqlite3_step(). */
- `sqlite3ApiBootstrap` **(Many-Argument Workhorses)** (@ `ext/wasm/api/sqlite3-api-prologue.js`) -> Impact: **807.6** | LOC: 1971
- `sqlite3WhereCodeOneLoopStart` **(Many-Argument Workhorses)** (@ `src/wherecode.c`) -> Impact: **782.5** | LOC: 1363
  * *Intent:* /* ** Generate code for the start of the iLevel-th loop in the WHERE clause ** implementation described by pWInfo. */
- `sqlite3GenerateConstraintChecks` **(Many-Argument Workhorses)** (@ `src/insert.c`) -> Impact: **748.6** | LOC: 829
  * *Intent:* ** NOT NULL REPLACE The NULL value is replace by the default ** value for that column. If the default value ** is NULL, the action is the same as ABOR...
- `sqlite3Update` **(Many-Argument Workhorses)** (@ `src/update.c`) -> Impact: **719.0** | LOC: 879
  * *Intent:* /* ** Process an UPDATE statement. ** ** UPDATE OR IGNORE tbl SET a=b, c=d FROM tbl2... WHERE e<5 AND f NOT NULL; ** \_______/ \_/ \______/ \_____/ \_...
- `sqlite3_str_vappendf` **(Many-Argument Workhorses)** (@ `src/printf.c`) -> Impact: **648.6** | LOC: 813
  * *Intent:* # define SQLITE_PRINT_BUF_SIZE 70 #endif #define etBUFSIZE SQLITE_PRINT_BUF_SIZE /* Size of the output buffer */ /* ** Hard limit on the precision of ...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 149 | 162736.82 | 60.06% | 25.6% |
| `ext/misc` | 62 | 26240.16 | 66.8% | 23.43% |
| `autosetup` | 12 | 25844.64 | 43.96% | 36.87% |
| `tool` | 75 | 24615.8 | 54.53% | 14.81% |
| `ext/fts5` | 17 | 21036.38 | 57.81% | 17.52% |
| `ext/fts3` | 17 | 11463.42 | 55.8% | 16.16% |
| `ext/session` | 6 | 10010.62 | 64.03% | 27.72% |
| `ext/wasm/api` | 20 | 9574.78 | 36.75% | 55.71% |
| `ext/wasm` | 29 | 6667.42 | 35.85% | 15.72% |
| `ext/rtree` | 9 | 6551.82 | 48.7% | 11.56% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ext/jni/src/org/sqlite/jni/fts5/Fts5ExtensionApi.java` -> **100.0%** Exposure
- `ext/jni/src/org/sqlite/jni/wrapper1/SqlFunction.java` -> **100.0%** Exposure
- `ext/jni/src/org/sqlite/jni/capi/OutputPointer.java` -> **99.9839%** Exposure
- `tool/winmain.c` -> **99.9665%** Exposure
- `src/os.c` -> **99.9623%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ext/wasm/mkdist.sh` -> **100.0%** Exposure
- `tool/mkautoconfamal.sh` -> **100.0%** Exposure
- `autosetup/cc.tcl` -> **100.0%** Exposure
- `autosetup/pkg-config.tcl` -> **100.0%** Exposure
- `autosetup/proj.tcl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ext/jni/src/org/sqlite/jni/wrapper1/Sqlite.java` -> **94** Orphaned Functions | **4** Duplicates
- `src/vdbeapi.c` -> **89** Orphaned Functions | **0** Duplicates
- `src/main.c` -> **82** Orphaned Functions | **0** Duplicates
- `src/vdbeaux.c` -> **73** Orphaned Functions | **0** Duplicates
- `src/btree.c` -> **66** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1328` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `autosetup/jimsh0.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 21433.94 | **LOC:** 24509 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 1.144; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Complexity Load (formerly Cognitive Load) (93.6%), Debt Markers (formerly Tech Debt) (7.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JimCreatePipeline` **(Many-Argument Workhorses)** (Impact: 350.8)
  * `Jim_StringCoreCommand` **(Many-Argument Workhorses)** (Impact: 243.6)
  * `Jim_FormatString` **(Many-Argument Workhorses)** (Impact: 222.5)
    * *Intent:* #include <ctype.h> #include <string.h> #include <stdio.h> #define JIM_INTEGER_SPACE 24 #define MAX_F...
  * `Jim_InfoCoreCommand` **(Many-Argument Workhorses)** (Impact: 211.2)
    * *Intent:* #endif
  * `JimCatchTryHelper` **(Many-Argument Workhorses)** (Impact: 186.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 3014 instances
* *High Risk Execution (weighted view):* 17
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 9437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4774`, `structural_boundaries: 2713`, `args: 1227`, `func_start: 689`, `class_start: 178`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 18`, `state_mutation: 3409`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 18`, `api: 442`, `import: 111`
* *Defense:* `safety: 52`, `immutability_locks: 770`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inet.h, assert.h, crt_externs.h, ctype.h, direct.h, dirent.h, errno.h, execinfo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shell.c.in` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 13128.1 | **LOC:** 13720 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 93.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 1.144; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (97.2%), Complexity Load (formerly Cognitive Load) (96.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_meta_command` **(Many-Argument Workhorses)** (Impact: 1227.5)
    * *Intent:* /* ** If an input line begins with "." then invoke this routine to ** process that line. ** ** Retur...
  * `main` **(Many-Argument Workhorses)** (Impact: 621.6)
    * *Intent:* #endif /* WIN32 */ /* ** This is the main entry point for the process. Everything starts here. ** **...
  * `dotCmdMode` **(Compute Cores)** (Impact: 340.7)
    * *Intent:* ** how to encode them. ARG can be "off", "on", ** "sql", "csv", "html", "tcl", or "json". ** --title...
  * `dotCmdImport` **(Compute Cores)** (Impact: 209.3)
    * *Intent:* ** ** Options: ** --ascii Do not use RFC-4180 quoting. Use \037 and \036 ** as column and row separa...
  * `lintFkeyIndexes` **(Many-Argument Workhorses)** (Impact: 144.6)
    * *Intent:* /* ** The implementation of dot-command ".lint fkey-indexes". */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 51 instances
* *Amplified Cascading Flux:* 2154 instances
* *High Risk Execution (weighted view):* 11
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 6567
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3894`, `structural_boundaries: 781`, `args: 492`, `func_start: 202`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 14`, `state_mutation: 2259`, `planned_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `io: 20`, `api: 57`, `import: 25`
* *Defense:* `safety: 54`, `doc: 9`, `immutability_locks: 385`, `cleanup: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, ctype.h, dirent.h, readline.h, fcntl.h, io.h, linenoise.h, math.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/btree.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9617.44 | **LOC:** 11569 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `balance_nonroot` **(Many-Argument Workhorses)** (Impact: 433.5)
    * *Intent:* ** be rolled back. ** ** The third argument to this function, aOvflSpace, is a pointer to a ** buffe...
  * `sqlite3BtreeOpen` **(Many-Argument Workhorses)** (Impact: 218.4)
    * *Intent:* ** when sqlite3BtreeClose() is called. ** ** If zFilename is ":memory:" then an in-memory database i...
  * `allocateBtreePage` **(Many-Argument Workhorses)** (Impact: 206.5)
    * *Intent:* ** SQLITE_OK is returned on success. Any other return value indicates ** an error. *ppPage is set to...
  * `sqlite3BtreeInsert` **(Many-Argument Workhorses)** (Impact: 189.5)
    * *Intent:* ** sqlite3BtreeIndexMoveto() to seek cursor pCur to (pKey,nKey) has already ** been performed. In ot...
  * `btreeBeginTrans` **(Many-Argument Workhorses)** (Impact: 126.3)
    * *Intent:* ** If an initial attempt to acquire the lock fails because of lock contention ** and the database wa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1588 instances
* *State Mutation (weighted view):* 4849
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1876`, `structural_boundaries: 595`, `args: 306`, `func_start: 220`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 1673`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 66`
* *Architecture:* `api: 90`, `import: 1`
* *Defense:* `safety: 704`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` btreeInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/lemon.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8108.94 | **LOC:** 6076 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.144; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (89.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.5%)
- **Documentation Coverage:** 49.5763% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ReportTable` **(Many-Argument Workhorses)** (Impact: 419.2)
    * *Intent:* /* Generate C source code for the parser */
  * `parseonetoken` **(Compute Cores)** (Impact: 333.9)
    * *Intent:* /* Parse a single token */
  * `Parse` **(Compute Cores)** (Impact: 119.4)
    * *Intent:* /* In spite of its name, this function is really a scanner. It read ** in the entire input file (all...
  * `translate_code` **(Many-Argument Workhorses)** (Impact: 117.0)
    * *Intent:* /* ** Write and transform the rp->code string so that symbols are expanded. ** Populate the rp->code...
  * `print_stack_union` **(Many-Argument Workhorses)** (Impact: 84.0)
    * *Intent:* /* ** Print the definition of the union used for the parser's data stack. ** This union contains fie...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1629 instances
* *High Risk Execution (weighted view):* 23
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 4999
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1443`, `structural_boundaries: 886`, `args: 216`, `func_start: 132`, `class_start: 253`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 27`, `state_mutation: 1741`, `dead_code: 6`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 192`, `import: 7`
* *Defense:* `safety: 35`, `doc: 23`, `test: 1`, `immutability_locks: 107`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, ctype.h, stdarg.h, stdio.h, stdlib.h, string.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/where.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 7950.88 | **LOC:** 7884 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 78.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3WhereBegin` **(Many-Argument Workhorses)** (Impact: 528.2)
    * *Intent:* ** ** pOrderBy is a pointer to the ORDER BY clause (or the GROUP BY clause ** if the WHERE_GROUPBY f...
  * `wherePathSatisfiesOrderBy` **(Many-Argument Workhorses)** (Impact: 310.8)
    * *Intent:* ** (or GROUP BY) without requiring a separate sort operation. Return N: ** ** N>0: N terms of the OR...
  * `whereLoopAddBtreeIndex` **(Many-Argument Workhorses)** (Impact: 263.2)
    * *Intent:* #endif /* ** We have so far matched pBuilder->pNew->u.btree.nEq terms of the ** index pIndex. Try to...
  * `wherePathSolver` **(Many-Argument Workhorses)** (Impact: 215.2)
    * *Intent:* /* ** Given the list of WhereLoop objects at pWInfo->pLoops, this routine ** attempts to find the lo...
  * `whereLoopAddBtree` **(Many-Argument Workhorses)** (Impact: 150.2)
    * *Intent:* ** cost = nSeek * (log(nRow) + (K+3.0) * nVisit) // non-covering index ** ** Normally, nSeek is 1. n...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1285 instances
* *State Mutation (weighted view):* 3996
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1556`, `structural_boundaries: 395`, `args: 178`, `func_start: 107`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1426`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 32`, `import: 2`
* *Defense:* `safety: 233`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sqliteInt.h, whereInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/fts5/fts5_index.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7896.88 | **LOC:** 9546 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 99.3031% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fts5DoSecureDelete` **(Many-Argument Workhorses)** (Impact: 121.9)
    * *Intent:* /* ** Completely remove the entry that pSeg currently points to from ** the database. */
  * `fts5DecodeFunction` **(Many-Argument Workhorses)** (Impact: 119.5)
    * *Intent:* #endif /* SQLITE_TEST || SQLITE_FTS5_DEBUG */ #if defined(SQLITE_TEST) || defined(SQLITE_FTS5_DEBUG)...
  * `fts5FlushOneHash` **(Many-Argument Workhorses)** (Impact: 92.3)
    * *Intent:* /* ** Flush the contents of in-memory hash table iHash to a new level-0 ** segment on disk. Also upd...
  * `fts5SetupTokendataIter` **(Many-Argument Workhorses)** (Impact: 82.9)
    * *Intent:* /* ** This function sets up an iterator to use for a non-prefix query on a ** tokendata=1 table. */
  * `fts5LeafSeek` **(Many-Argument Workhorses)** (Impact: 77.3)
    * *Intent:* /* ** The iterator object passed as the second argument currently contains ** no valid values except...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1227 instances
* *State Mutation (weighted view):* 3797
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1550`, `structural_boundaries: 517`, `args: 283`, `func_start: 238`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 1343`, `planned_debt: 6`, `unreferenced_by_name: 29`
* *Architecture:* `api: 84`, `import: 1`
* *Defense:* `safety: 190`, `doc: 2`, `test: 8`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fts5Int.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/select.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7695.98 | **LOC:** 8983 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 72.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3Select` **(Many-Argument Workhorses)** (Impact: 615.4)
    * *Intent:* ** * DISTINCT ORDER BY -> GROUP BY optimization tag-select-0500 ** * Set up for ORDER BY tag-select-...
  * `selectInnerLoop` **(Many-Argument Workhorses)** (Impact: 268.4)
    * *Intent:* #endif /* ** This routine generates the code for the inside of the inner loop ** of a SELECT. ** ** ...
  * `selectExpander` **(Many-Argument Workhorses)** (Impact: 248.0)
    * *Intent:* ** that implements the view. A copy is made of the view's SELECT ** statement so that we can freely ...
  * `flattenSubquery` **(Many-Argument Workhorses)** (Impact: 213.9)
    * *Intent:* ** (28) The subquery is not a MATERIALIZED CTE. (This is handled ** in the caller before ever reachi...
  * `generateSortTail` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* #else /* No-op versions of the explainXXX() functions and macros. */ # define explainTempTable(y,z) ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1205 instances
* *State Mutation (weighted view):* 3779
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1553`, `structural_boundaries: 440`, `args: 190`, `func_start: 106`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 1369`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `safety: 349`, `doc: 3`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/session/sqlite3session.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6565.8 | **LOC:** 6791 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sessionChangeMerge` **(Many-Argument Workhorses)** (Impact: 189.1)
    * *Intent:* /* ** This function is called to merge two changes to the same row together as ** part of an sqlite3...
  * `sessionChangesetApply` **(Many-Argument Workhorses)** (Impact: 175.7)
    * *Intent:* /* ** Argument pIter is a changeset iterator that has been initialized, but ** not yet passed to sql...
  * `sessionChangesetNextOne` **(Many-Argument Workhorses)** (Impact: 156.1)
    * *Intent:* /* ** Advance the changeset iterator to the next change. The differences between ** this function an...
  * `sessionTableInfo` **(Many-Argument Workhorses)** (Impact: 137.5)
    * *Intent:* ** ** CREATE TABLE tbl1(w, x DEFAULT 'abc', y, z, PRIMARY KEY(w, z)); ** ** Then the five output var...
  * `sessionGenerateChangeset` **(Many-Argument Workhorses)** (Impact: 101.3)
    * *Intent:* /* ** Generate either a changeset (if argument bPatchset is zero) or a patchset ** (if it is non-zer...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 970 instances
* *State Mutation (weighted view):* 2962
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1174`, `structural_boundaries: 512`, `args: 179`, `func_start: 158`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 1022`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 35`
* *Architecture:* `api: 73`, `import: 5`
* *Defense:* `safety: 97`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` assert.h, sqlite3session.h, sqliteInt.h, string.h, vdbeInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/expr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6515.56 | **LOC:** 7703 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 88.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3ExprCodeTarget` **(Many-Argument Workhorses)** (Impact: 415.4)
    * *Intent:* /* ** Generate code into the current Vdbe to evaluate the given ** expression. Attempt to store the ...
  * `sqlite3FindInIndex` **(Many-Argument Workhorses)** (Impact: 164.6)
    * *Intent:* ** NULL values. ** ** If the aiMap parameter is not NULL, it must point to an array containing ** on...
  * `sqlite3ExprIfFalse` **(Many-Argument Workhorses)** (Impact: 148.1)
    * *Intent:* /* ** Generate code for a boolean expression such that a jump is made ** to the label "dest" if the ...
  * `sqlite3ExprCodeIN` **(Many-Argument Workhorses)** (Impact: 127.2)
    * *Intent:* ** ** The IN operator is true if the LHS value is contained within the RHS. ** The result is false i...
  * `sqlite3ExprIfTrue` **(Many-Argument Workhorses)** (Impact: 126.3)
    * *Intent:* /* ** Generate code for a boolean expression such that a jump is made ** to the label "dest" if the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 815 instances
* *State Mutation (weighted view):* 2560
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1547`, `structural_boundaries: 581`, `args: 292`, `func_start: 176`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 930`, `planned_debt: 8`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `api: 119`, `import: 1`
* *Defense:* `safety: 415`, `doc: 1`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/os_win.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5867.52 | **LOC:** 6500 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.6%), Guard Balance (formerly Safety Score) (91.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 49.6835% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `winRead` **(Many-Argument Workhorses)** (Impact: 948.9)
    * *Intent:* /* ** Read data from a file into a buffer. Return SQLITE_OK if all ** bytes were read successfully a...
  * `winWrite` **(Many-Argument Workhorses)** (Impact: 942.2)
    * *Intent:* /* ** Write data from a buffer into a file. Return SQLITE_OK on success ** or some other error code ...
  * `winOpen` **(Many-Argument Workhorses)** (Impact: 224.6)
    * *Intent:* /* ** The Windows version of xAccess() accepts an extra bit in the flags ** parameter that prevents ...
  * `winFullPathnameNoMutex` **(Many-Argument Workhorses)** (Impact: 149.5)
    * *Intent:* #endif /* __CYGWIN__ */ /* ** Turn a relative pathname into a full pathname. Write the full ** pathn...
  * `winShmLock` **(Many-Argument Workhorses)** (Impact: 121.4)
    * *Intent:* /* ** Change the lock state for a shared-memory segment. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 599 instances
* *State Mutation (weighted view):* 1845
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1080`, `structural_boundaries: 415`, `args: 415`, `func_start: 113`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 647`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 15`
* *Architecture:* `api: 39`, `import: 4`
* *Defense:* `safety: 124`, `doc: 6`, `test: 4`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` os_common.h, os_win.h, sqliteInt.h, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5657.92 | **LOC:** 5635 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.0%), Complexity Load (formerly Cognitive Load) (93.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 49.3976% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jsonTranslateTextToBlob` **(Many-Argument Workhorses)** (Impact: 366.1)
    * *Intent:* ** its equivalent binary JSONB representation. Append the translation into ** pParse->aBlob[] beginn...
  * `jsonbValidityCheck` **(Many-Argument Workhorses)** (Impact: 231.0)
    * *Intent:* /* ** Check a single element of the JSONB in pParse for validity. ** ** The element to be checked st...
  * `jsonLookupStep` **(Many-Argument Workhorses)** (Impact: 180.0)
    * *Intent:* ** ** If the value found by this routine is the value half of label/value pair ** within an object, ...
  * `jsonTranslateBlobToText` **(Many-Argument Workhorses)** (Impact: 158.8)
    * *Intent:* /* ** Translate the binary JSONB representation of JSON beginning at ** pParse->aBlob[i] into a JSON...
  * `jsonReturnFromBlob` **(Many-Argument Workhorses)** (Impact: 135.9)
    * *Intent:* ** Return the value of the BLOB node at index i. ** ** If the value is a primitive, return it as an ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 859 instances
* *State Mutation (weighted view):* 2617
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1291`, `structural_boundaries: 571`, `args: 126`, `func_start: 107`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 899`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 84`, `doc: 10`, `immutability_locks: 114`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/os_unix.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5634.84 | **LOC:** 8590 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 94.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%)
- **Documentation Coverage:** 49.4565% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unixOpen` **(Many-Argument Workhorses)** (Impact: 249.6)
    * *Intent:* ** sqlite3OsOpenExclusive(); ** ** These calls correspond to the following combinations of flags: **...
  * `unixShmLock` **(Many-Argument Workhorses)** (Impact: 132.6)
    * *Intent:* #endif /* !defined(SQLITE_WASI) && !defined(SQLITE_OMIT_WAL) */ /* ** Change the lock state for a sh...
  * `unixFileControl` **(Many-Argument Workhorses)** (Impact: 124.0)
    * *Intent:* #endif /* ** Information and control of an open file handle. */
  * `fillInUnixFile` **(Many-Argument Workhorses)** (Impact: 114.2)
    * *Intent:* /**************************************************************************** **********************...
  * `proxyTakeConch` **(Many-Argument Workhorses)** (Impact: 95.8)
    * *Intent:* /* Takes the conch by taking a shared lock and read the contents conch, if ** lockPath is non-NULL, ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 861 instances
* *State Mutation (weighted view):* 2630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1400`, `structural_boundaries: 492`, `args: 341`, `func_start: 137`, `class_start: 69`
* *Risk/State:* `safety_bypasses: 124`, `state_mutation: 908`, `dead_code: 13`, `planned_debt: 5`, `fragile_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 24`, `import: 23`
* *Defense:* `safety: 232`, `doc: 16`, `test: 4`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dlfcn.h, errno.h, fcntl.h, limits.h, os_common.h, pthread.h, semaphore.h, sqliteInt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vdbe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5306.22 | **LOC:** 9319 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.9%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 49.0654% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3VdbeExec` **(Many-Argument Workhorses)** (Impact: 895.9)
    * *Intent:* /* ** Execute as much of a VDBE program as we can. ** This is the core of sqlite3_step(). */
  * `vdbeColumnFromOverflow` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* /* ** For OP_Column, factor out the case where content is loaded from ** overflow pages, so that the...
  * `sqlite3VdbeMemPrettyPrint` **(Many-Argument Workhorses)** (Impact: 51.3)
    * *Intent:* #ifdef SQLITE_DEBUG /* ** Write a nice string representation of the contents of cell pMem ** into bu...
  * `applyAffinity` **(Stateful Encapsulated Methods)** (Impact: 29.6)
    * *Intent:* ** always preferred, even if the affinity is REAL, because ** an integer representation is more spac...
  * `allocateCursor` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* /* Return true if the cursor was opened using the OP_OpenSorter opcode. */ #define isSorter(x) ((x)-...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1305 instances
* *State Mutation (weighted view):* 3988
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1563`, `structural_boundaries: 235`, `args: 109`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 1`, `state_mutation: 1378`, `planned_debt: 5`, `unreferenced_by_name: 4`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 696`, `doc: 4`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hwtime.h, sqliteInt.h, vdbeInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/fts3/fts3_write.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5222.28 | **LOC:** 5857 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.1%)
- **Documentation Coverage:** 96.35% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fts3SqlStmt` **(Many-Argument Workhorses)** (Impact: 157.0)
    * *Intent:* /* ** This function is used to obtain an SQLite prepared statement handle ** for the statement ident...
  * `sqlite3Fts3SegReaderStep` **(Many-Argument Workhorses)** (Impact: 100.5)
  * `sqlite3Fts3Incrmerge` **(Many-Argument Workhorses)** (Impact: 98.3)
    * *Intent:* /* ** Attempt an incremental merge that writes nMerge leaf blocks. ** ** Incremental merges happen n...
  * `fts3IncrmergeLoad` **(Many-Argument Workhorses)** (Impact: 86.5)
    * *Intent:* ** This function is called when initializing an incremental-merge operation. ** It checks if the exi...
  * `fts3SpecialInsert` **(Compute Cores)** (Impact: 73.2)
    * *Intent:* /* ** Handle a 'special' INSERT of the form: ** ** "INSERT INTO tbl(tbl) VALUES(<expr>)" ** ** Argum...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 875 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 2657
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 948`, `structural_boundaries: 265`, `args: 134`, `func_start: 118`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 907`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 16`
* *Architecture:* `api: 44`, `import: 5`
* *Defense:* `safety: 102`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, fts3Int.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vdbeaux.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4651.08 | **LOC:** 5585 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3VdbeRecordCompareWithSkip` **(Many-Argument Workhorses)** (Impact: 185.5)
    * *Intent:* ** sqlite3VdbeParseRecord. ** ** If argument bSkip is non-zero, it is assumed that the caller has al...
  * `sqlite3VdbeHalt` **(Many-Argument Workhorses)** (Impact: 93.6)
    * *Intent:* /* ** This routine is called the when a VDBE tries to halt. If the VDBE ** has made changes and is i...
  * `vdbeCommit` **(Many-Argument Workhorses)** (Impact: 92.5)
    * *Intent:* /* ** A read or write transaction may or may not be active on database handle ** db. If a transactio...
  * `sqlite3VdbeNextOpcode` **(Many-Argument Workhorses)** (Impact: 74.0)
    * *Intent:* #if defined(SQLITE_ENABLE_BYTECODE_VTAB) || !defined(SQLITE_OMIT_EXPLAIN) /* ** Locate the next opco...
  * `sqlite3VdbeDisplayComment` **(Many-Argument Workhorses)** (Impact: 72.2)
    * *Intent:* /* ** Compute a string for the "comment" field of a VDBE opcode listing. ** ** The Synopsis: field i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 690 instances
* *State Mutation (weighted view):* 2150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 977`, `structural_boundaries: 425`, `args: 229`, `func_start: 163`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 770`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 73`
* *Architecture:* `io: 1`, `api: 125`, `import: 2`
* *Defense:* `safety: 236`, `immutability_locks: 91`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sqliteInt.h, vdbeInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pager.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4392.42 | **LOC:** 7835 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.8%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3PagerOpen` **(Many-Argument Workhorses)** (Impact: 156.0)
    * *Intent:* ** The flags argument is used to specify properties that affect the ** operation of the pager. It sh...
  * `pager_playback_one_page` **(Many-Argument Workhorses)** (Impact: 125.3)
    * *Intent:* ** is successfully read from the (sub-)journal file but appears to be ** corrupted, SQLITE_DONE is r...
  * `sqlite3PagerCommitPhaseOne` **(Many-Argument Workhorses)** (Impact: 119.0)
    * *Intent:* ** * the database file synced. ** ** The only thing that remains to commit the transaction is to fin...
  * `pager_end_transaction` **(Many-Argument Workhorses)** (Impact: 88.5)
    * *Intent:* ** ** After the journal is finalized, the pager moves to PAGER_READER state. ** If running in non-ex...
  * `pager_playback` **(Many-Argument Workhorses)** (Impact: 70.9)
    * *Intent:* ** back (or no pages if the journal header is corrupted). The journal file ** is then deleted and SQ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 619 instances
* *State Mutation (weighted view):* 1912
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1062`, `structural_boundaries: 294`, `args: 192`, `func_start: 149`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 674`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 61`
* *Architecture:* `api: 83`, `import: 2`
* *Defense:* `safety: 378`, `doc: 2`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sqliteInt.h, wal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/rbu/sqlite3rbu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4295.58 | **LOC:** 5448 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.1%)
- **Documentation Coverage:** 99.3007% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rbuObjIterPrepareAll` **(Many-Argument Workhorses)** (Impact: 112.8)
    * *Intent:* /* ** Ensure that the SQLite statement handles required to update the ** target database object curr...
  * `openRbuHandle` **(Many-Argument Workhorses)** (Impact: 102.0)
  * `rbuOpenDatabase` **(Many-Argument Workhorses)** (Impact: 96.0)
    * *Intent:* /* ** Open the database handle and attach the RBU database as "rbu". If an ** error occurs, leave an...
  * `rbuObjIterGetIndexWhere` **(Many-Argument Workhorses)** (Impact: 86.1)
  * `rbuObjIterGetIndexCols` **(Many-Argument Workhorses)** (Impact: 65.9)
    * *Intent:* ** CREATE INDEX i1 ON t1(c, b COLLATE nocase); ** ** and "t1" is a table with an explicit INTEGER PR...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 673 instances
* *State Mutation (weighted view):* 2073
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 927`, `structural_boundaries: 267`, `args: 153`, `func_start: 123`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 727`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 11`
* *Architecture:* `io: 1`, `api: 34`, `import: 6`
* *Defense:* `safety: 90`, `doc: 4`, `immutability_locks: 148`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, sqlite3.h, sqlite3rbu.h, stdio.h, string.h, windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tclsqlite.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4093.94 | **LOC:** 4600 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 2.117; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Guard Balance (formerly Safety Score) (95.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DbObjCmd` **(Many-Argument Workhorses)** (Impact: 1139.7)
    * *Intent:* /* ** The "sqlite" command below creates a new Tcl command for each ** connection it opens to an SQL...
  * `dbQrf` **(Many-Argument Workhorses)** (Impact: 206.9)
    * *Intent:* ** -titlealign eTitleAlign ** -border bBorder ** -wrap nWrap ** -screenwidth nScreenWidth ** -lineli...
  * `auth_callback` **(Many-Argument Workhorses)** (Impact: 144.2)
    * *Intent:* #ifndef SQLITE_OMIT_AUTHORIZATION /* ** This is the authentication function. It appends the authenti...
  * `DbMain` **(Many-Argument Workhorses)** (Impact: 139.9)
    * *Intent:* ** ?-create BOOLEAN? ?-nomutex BOOLEAN? ** ?-nofollow BOOLEAN? ** ** This is the main Tcl command. W...
  * `dbPrepareAndBind` **(Many-Argument Workhorses)** (Impact: 133.8)
    * *Intent:* ** Search the cache for a prepared-statement object that implements the ** first SQL statement in th...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 530 instances
* *Api Near Db Sink:* 2 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1609
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1012`, `structural_boundaries: 392`, `args: 124`, `func_start: 68`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 549`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 28`, `import: 15`
* *Defense:* `safety: 30`, `doc: 2`, `immutability_locks: 99`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.117
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.001764
  * `Imports (Out-Degree: 2):` assert.h, ctype.h, errno.h, io.h, msvc.h, qrf.h, signal.h, sqlite3.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4062.52 | **LOC:** 5190 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 45.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Complexity Load (formerly Cognitive Load) (91.7%), Debt Markers (formerly Tech Debt) (80.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3ParseUri` **(Many-Argument Workhorses)** (Impact: 204.7)
    * *Intent:* ** ** If successful, SQLITE_OK is returned. In this case *ppVfs is set to point to ** the VFS that s...
  * `openDatabase` **(Many-Argument Workhorses)** (Impact: 183.3)
    * *Intent:* /* ** This routine does the work of opening a database on behalf of ** sqlite3_open() and sqlite3_op...
  * `sqlite3_test_control` **(Many-Argument Workhorses)** (Impact: 142.8)
    * *Intent:* /* ** Interface to the testing logic. */
  * `sqlite3ErrName` **(Compute Cores)** (Impact: 137.0)
    * *Intent:* /* ** Return a static string containing the name corresponding to the error code ** specified in the...
  * `sqlite3_config` **(Many-Argument Workhorses)** (Impact: 127.6)
    * *Intent:* /* ** This API allows applications to modify the global configuration of ** the SQLite library at ru...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 582 instances
* *State Mutation (weighted view):* 1790
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 856`, `structural_boundaries: 607`, `args: 200`, `func_start: 125`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 626`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 82`
* *Architecture:* `api: 113`, `import: 4`
* *Defense:* `safety: 73`, `doc: 4`, `immutability_locks: 143`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` fts3.h, rtree.h, sqliteInt.h, sqliteicu.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/rtree/rtree.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3927.24 | **LOC:** 4486 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rtreeSqlInit` **(Many-Argument Workhorses)** (Impact: 101.8)
  * `rtreeFilter` **(Many-Argument Workhorses)** (Impact: 99.7)
    * *Intent:* /* ** Rtree virtual table module xFilter method. */
  * `rtreeInit` **(Many-Argument Workhorses)** (Impact: 88.2)
    * *Intent:* /* ** This function is the implementation of both the xConnect and xCreate ** methods of the r-tree ...
  * `rtreeCallbackConstraint` **(Many-Argument Workhorses)** (Impact: 77.6)
    * *Intent:* #endif /* ** Check the RTree node or entry given by pCellData and p against the MATCH ** constraint ...
  * `SplitNode` **(Many-Argument Workhorses)** (Impact: 67.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 663 instances
* *State Mutation (weighted view):* 2032
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 749`, `structural_boundaries: 265`, `args: 177`, `func_start: 110`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 706`, `unreferenced_by_name: 3`
* *Architecture:* `api: 32`, `import: 11`
* *Defense:* `safety: 56`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` assert.h, cmnintrin.h, geopoly.c, intrin.h, sqlite3.h, sqlite3ext.h, sqlite3rtree.h, stddef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/qrf/qrf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3328.4 | **LOC:** 2984 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `qrfColumnar` **(Compute Cores)** (Impact: 191.4)
    * *Intent:* /* ** Columnar modes require that the entire query be evaluated first, with ** results written into ...
  * `qrfInitialize` **(Many-Argument Workhorses)** (Impact: 144.4)
    * *Intent:* /* ** Initialize the internal Qrf object. */
  * `qrfEncodeText` **(Many-Argument Workhorses)** (Impact: 107.0)
    * *Intent:* /* ** Encode text appropriately and append it to pOut. */
  * `qrfRenderValue` **(Many-Argument Workhorses)** (Impact: 103.9)
    * *Intent:* /* ** Render value pVal into pOut */
  * `qrfWrapLine` **(Many-Argument Workhorses)** (Impact: 94.5)
    * *Intent:* /* ** (*pz)[] is a line of text that is to be displayed the box or table or ** similar tabular forma...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 578 instances
* *State Mutation (weighted view):* 1742
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 744`, `structural_boundaries: 268`, `args: 51`, `func_start: 49`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 586`, `unreferenced_by_name: 1`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `safety: 12`, `immutability_locks: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, qrf.h, stdint.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/fts5/fts5_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3328.06 | **LOC:** 3876 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fts5FilterMethod` **(Many-Argument Workhorses)** (Impact: 149.7)
    * *Intent:* /* ** This is the xFilter interface for the virtual table. See ** the virtual table xFilter method d...
  * `fts5UpdateMethod` **(Many-Argument Workhorses)** (Impact: 109.2)
    * *Intent:* /* ** This function is the implementation of the xUpdate callback used by ** FTS3 virtual tables. It...
  * `fts5BestIndexMethod` **(Many-Argument Workhorses)** (Impact: 105.9)
    * *Intent:* ** * No other constraints: cost=1000.0 ** * One rowid range constraint: cost=750.0 ** * Both rowid r...
  * `fts5SpecialInsert` **(Many-Argument Workhorses)** (Impact: 55.5)
    * *Intent:* ** This function is called to handle an FTS INSERT command. In other words, ** an INSERT statement o...
  * `fts5InitVtab` **(Many-Argument Workhorses)** (Impact: 54.4)
    * *Intent:* /* ** This function is the implementation of both the xConnect and xCreate ** methods of the FTS3 vi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 551 instances
* *State Mutation (weighted view):* 1689
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 601`, `structural_boundaries: 253`, `args: 127`, `func_start: 113`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 587`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 29`, `import: 1`
* *Defense:* `safety: 87`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fts5Int.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/insert.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3235.1 | **LOC:** 3394 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.8%), Guard Balance (formerly Safety Score) (94.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3GenerateConstraintChecks` **(Many-Argument Workhorses)** (Impact: 748.6)
    * *Intent:* ** NOT NULL REPLACE The NULL value is replace by the default ** value for that column. If the defaul...
  * `sqlite3Insert` **(Many-Argument Workhorses)** (Impact: 440.6)
    * *Intent:* ** end loop ** cleanup after the SELECT ** end co-routine R ** B: open temp table ** L: yield X, at ...
  * `xferOptimization` **(Many-Argument Workhorses)** (Impact: 254.2)
    * *Intent:* ** embedded in the code for details. ** ** This routine returns TRUE if the optimization is guarante...
  * `sqlite3CompleteInsertion` **(Many-Argument Workhorses)** (Impact: 66.5)
    * *Intent:* #else # define codeWithoutRowidPreupdate(a,b,c,d) #endif /* ** This routine generates code to finish...
  * `sqlite3MultiValues` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* ** of a schema item like a VIEW or TRIGGER). In this case there is no VM ** being generated when par...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 414 instances
* *State Mutation (weighted view):* 1277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 606`, `structural_boundaries: 137`, `args: 41`, `func_start: 29`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 449`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `safety: 114`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/wal.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3140.1 | **LOC:** 4622 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `walFrames` **(Many-Argument Workhorses)** (Impact: 141.1)
    * *Intent:* /* ** Write a set of frames to the log. The caller must hold the write-lock ** on the log file (obta...
  * `walTryBeginRead` **(Many-Argument Workhorses)** (Impact: 131.2)
    * *Intent:* ** Or if pWal->readLock==0, then the reader will ignore the WAL ** completely and get all content di...
  * `walCheckpoint` **(Many-Argument Workhorses)** (Impact: 122.3)
    * *Intent:* ** Fsync is also called on the database file if (and only if) the entire ** WAL content is copied in...
  * `sqlite3WalCheckpoint` **(Many-Argument Workhorses)** (Impact: 109.4)
    * *Intent:* /* ** This routine is called to implement sqlite3_wal_checkpoint() and ** related interfaces. ** ** ...
  * `walIndexRecover` **(Many-Argument Workhorses)** (Impact: 65.0)
    * *Intent:* /* ** Recover the wal-index by reading the write-ahead log file. ** ** This routine first tries to e...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 520 instances
* *State Mutation (weighted view):* 1603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 564`, `structural_boundaries: 238`, `args: 119`, `func_start: 81`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 563`, `planned_debt: 4`, `unreferenced_by_name: 25`
* *Architecture:* `api: 40`, `import: 2`
* *Defense:* `safety: 157`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Windows.h, wal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/func.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2840.88 | **LOC:** 3464 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 87.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patternCompare` **(Many-Argument Workhorses)** (Impact: 129.4)
    * *Intent:* ** ** Like matching rules: ** ** '%' Matches any sequence of zero or more characters ** *** '_' Matc...
  * `substrFunc` **(Many-Argument Workhorses)** (Impact: 74.5)
    * *Intent:* /* ** Implementation of the substr() function. ** ** substr(x,p1,p2) returns p2 characters of x[] be...
  * `percentStep` **(Many-Argument Workhorses)** (Impact: 60.6)
    * *Intent:* /* ** The "step" function for percentile(Y,P) is called once for each ** input row. */
  * `trimFunc` **(Stateful Encapsulated Methods)** (Impact: 54.0)
    * *Intent:* /* ** Implementation of the TRIM(), LTRIM(), and RTRIM() functions. ** The userdata is 0x1 for left ...
  * `groupConcatStep` **(Many-Argument Workhorses)** (Impact: 47.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 443 instances
* *State Mutation (weighted view):* 1346
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 592`, `structural_boundaries: 252`, `args: 128`, `func_start: 94`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 460`, `planned_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `safety: 86`, `doc: 4`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, math.h, sqliteInt.h, stdlib.h, vdbeInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/shell.c.in` -> Churn: **100.0%** | Cog Load: 96.2715% | Debt: 8.7402%
- `ext/qrf/qrf.c` -> Churn: **87.59%** | Cog Load: 77.8774% | Debt: 8.0245%
- `ext/wasm/GNUmakefile` -> Churn: **83.69%** | Cog Load: 92.9662% | Debt: 62.1965%
- `ext/wasm/api/sqlite3-vfs-kvvfs.c-pp.js` -> Churn: **82.89%** | Cog Load: 45.9832% | Debt: 91.637%
- `src/select.c` -> Churn: **67.79%** | Cog Load: 75.4994% | Debt: 10.6361%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `autosetup/jimsh0.c` -> **drh** (100.0% isolated ownership) | Magnitude: 21433.94
- `src/shell.c.in` -> **drh** (93.3% isolated ownership) | Magnitude: 13128.1
- `src/expr.c` -> **drh** (88.9% isolated ownership) | Magnitude: 6515.56
- `src/json.c` -> **drh** (100.0% isolated ownership) | Magnitude: 5657.92
- `src/os_unix.c` -> **drh** (94.4% isolated ownership) | Magnitude: 5634.84

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/tclsqlite.c` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/sqliteInt.h` -> **Severity: 9.816** (Embedded: 0.189 * Error Risk: 51.9483%)
- `src/sqlite3ext.h` -> **Severity: 6.004** (Embedded: 0.1163 * Error Risk: 51.6223%)
- `src/vdbe.h` -> **Severity: 5.198** (Embedded: 0.0975 * Error Risk: 53.339%)
- `src/vdbeInt.h` -> **Severity: 1.408** (Embedded: 0.0265 * Error Risk: 53.2352%)
- `ext/fts3/fts3Int.h` -> **Severity: 1.018** (Embedded: 0.0212 * Error Risk: 48.0877%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `autosetup/teaish/tester.tcl` -> **Severity: 481.25** (Blast Radius: 5.034 * Doc Risk: 95.6%)
- `ext/wasm/SQLTester/SQLTester.mjs` -> **Severity: 204.349** (Blast Radius: 2.117 * Doc Risk: 96.5278%)
- `ext/jni/src/org/sqlite/jni/capi/sqlite3_value.java` -> **Severity: 195.4** (Blast Radius: 1.954 * Doc Risk: 100.0%)
- `ext/jni/src/org/sqlite/jni/capi/CApi.java` -> **Severity: 194.632** (Blast Radius: 3.089 * Doc Risk: 63.0081%)
- `ext/jni/src/org/sqlite/jni/capi/Tester1.java` -> **Severity: 192.91** (Blast Radius: 2.117 * Doc Risk: 91.1243%)

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
