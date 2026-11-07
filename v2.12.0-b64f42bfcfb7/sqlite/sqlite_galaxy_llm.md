# ARCHITECTURAL_BRIEF: sqlite
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sqlite/sqlite.git` |
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
- **Scope:** 642 analyzed artifact(s), 326420 LOC.
- **Load-bearing artifact:** `src/malloc.c` -- 221 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/sqliteInt.h` -- pulls in 26 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/shell.c.in` at magnitude 13483.5 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 642 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1558 |
| Total LOC | 326420 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 29.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3514 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2951 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6518 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 30 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 351 | 274715 | 54.7% |
| TCL | 83 | 17636 | 12.9% |
| JAVA | 58 | 8157 | 9.0% |
| JAVASCRIPT | 39 | 16657 | 6.1% |
| MARKDOWN | 28 | 0 | 4.4% |
| HTML | 21 | 3490 | 3.3% |
| SHELL | 16 | 581 | 2.5% |
| PLAINTEXT | 15 | 0 | 2.3% |
| SQLITE | 11 | 826 | 1.7% |
| MAKEFILE | 7 | 1491 | 1.1% |
| YACC | 3 | 1793 | 0.5% |
| BATCH | 3 | 625 | 0.5% |
| CSS | 2 | 122 | 0.3% |
| M4 | 2 | 20 | 0.3% |
| CSHARP | 2 | 307 | 0.3% |
| XML | 1 | 0 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 642 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Encapsulated Accessors Files 17%, Large Core Modules (3) 17%, Data / Markup / Trivial 16%, Declarative / Non-Code 16%, Many-Argument Workhorses Files 13%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 599 | 93.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 43 | 6.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1558*

**Composition by Extension & Reason:**
- `.test`: 1466x Excluded (Unsupported Extension: '.test'), 3x Unsupported Format (.test)
- `.tcl`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 290 LOC), 1x Excluded (Machine-Generated Source Code Signature: 446 LOC)
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.linux-generic'), 1x Excluded (Lexical Monotony: High structural repetition detected in 2205 LOC)
- `.db`: 10x Excluded (Unsupported Extension: '.db')
- `.c`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 6204 LOC), 1x Excluded (Machine-Generated Source Code Signature: 384 LOC)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 24429 LOC), 1x Unsupported Format (.undeterminable)
- `.def`: 2x Unsupported Format (.undeterminable), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.in`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.msc`: 2x Excluded (Unsupported Extension: '.msc')
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.explain`: 2x Excluded (Unsupported Extension: '.explain')
- `.eps`: 1x Excluded (Explicitly Denied Extension: '.eps')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.fallback`: 1x Excluded (Unsupported Extension: '.fallback')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 45.8 | 58.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.7 | 56.4 | 68.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.9 | 9.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 31.2 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.9 | 2.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 63.6 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.5 | 2.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.3 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3031 | 282 | 12 | `src/parse.y` |
| cleanup | 686 | 155 | 2 | `ext/wasm/tester1.c-pp.js` |
| guards | 28753 | 480 | 105 | `ext/wasm/tester1.c-pp.js` |
| danger | 5707 | 391 | 24 | `src/test1.c` |
| concurrency | 655 | 77 | 1 | `ext/wasm/api/sqlite3-vfs-opfs.c-pp.js` |
| connectivity | 7745 | 448 | 25 | `src/sqliteInt.h` |
| io | 1464 | 183 | 5 | `doc/lemon.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 107 | 41 | 0 | `src/shell.c.in` |
| time | 109 | 37 | 0 | `ext/wasm/api/sqlite3-vfs-opfs.c-pp.js` |
| serialization | 33 | 16 | 0 | `ext/wasm/GNUmakefile` |
| regex | 100 | 34 | 0 | `ext/wasm/GNUmakefile` |
| events | 282 | 62 | 0 | `contrib/sqlitecon.tcl` |
| tests | 219 | 48 | 0 | `test/tester.tcl` |
| docs | 1639 | 182 | 3 | `tool/GetFile.cs` |
| debt | 3352 | 319 | 14 | `tool/lemon.c` |
| mutation | 97280 | 503 | 374 | `src/shell.c.in` |
| dead_code | 2543 | 381 | 9 | `ext/jni/src/org/sqlite/jni/wrapper1/Sqlite.java` |
| credential | 4 | 4 | 0 | `ext/misc/base64.c` |
| threat | 3 | 2 | 0 | `ext/wasm/SQLTester/SQLTester.mjs` |
| ml_ai | 673 | 89 | 1 | `test/tester.tcl` |
| ui | 255 | 43 | 0 | `test/malloctraceviewer.tcl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.1973**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/lemon.html` (Hits: 220)
- `ext/wasm/index.html` (Hits: 78)
- `test/testrunner.tcl` (Hits: 54)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **malloc.c** (`src/malloc.c`) — 221 inbound connections
2. **printf.c** (`src/printf.c`) — 183 inbound connections
3. **main.c** (`src/main.c`) — 176 inbound connections
4. **vdbeapi.c** (`src/vdbeapi.c`) — 154 inbound connections
5. **util.c** (`src/util.c`) — 118 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sqliteInt.h** (`src/sqliteInt.h`) — 26 outbound dependencies
2. **shell.c.in** (`src/shell.c.in`) — 24 outbound dependencies
3. **os_unix.c** (`src/os_unix.c`) — 21 outbound dependencies
4. **threadtest3.c** (`test/threadtest3.c`) — 20 outbound dependencies
5. **fileio.c** (`ext/misc/fileio.c`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sqlite3VdbeExec` **(Many-Argument Workhorses)** (@ `src/vdbe.c`) -> Impact: **2410.6** | LOC: 8473
  * *Intent:* /* ** Execute as much of a VDBE program as we can. ** This is the core of sqlite3_step(). */
- `do_meta_command` **(Many-Argument Workhorses)** (@ `src/shell.c.in`) -> Impact: **1983.9** | LOC: 3028
  * *Intent:* /* ** If an input line begins with "." then invoke this routine to ** process that line. ** ** Return 1 on error, 2 to exit, and 0 otherwise. */
- `DbObjCmd` **(Many-Argument Workhorses)** (@ `src/tclsqlite.c`) -> Impact: **980.9** | LOC: 1775
  * *Intent:* /* ** The "sqlite" command below creates a new Tcl command for each ** connection it opens to an SQLite database. This routine is invoked ** whenever ...
- `winWrite` **(Many-Argument Workhorses)** (@ `src/os_win.c`) -> Impact: **805.8** | LOC: 2208
  * *Intent:* /* ** Write data from a buffer into a file. Return SQLITE_OK on success ** or some other error code on failure. */
- `winRead` **(Many-Argument Workhorses)** (@ `src/os_win.c`) -> Impact: **799.0** | LOC: 2162
  * *Intent:* /* ** Read data from a file into a buffer. Return SQLITE_OK if all ** bytes were read successfully and SQLITE_IOERR if anything goes ** wrong. */
- `sqlite3ApiBootstrap` **(Many-Argument Workhorses)** (@ `ext/wasm/api/sqlite3-api-prologue.js`) -> Impact: **778.5** | LOC: 1971
- `sqlite3WhereCodeOneLoopStart` **(Many-Argument Workhorses)** (@ `src/wherecode.c`) -> Impact: **771.9** | LOC: 1363
  * *Intent:* /* ** Generate code for the start of the iLevel-th loop in the WHERE clause ** implementation described by pWInfo. */
- `sqlite3GenerateConstraintChecks` **(Many-Argument Workhorses)** (@ `src/insert.c`) -> Impact: **741.1** | LOC: 829
  * *Intent:* ** NOT NULL REPLACE The NULL value is replace by the default ** value for that column. If the default value ** is NULL, the action is the same as ABOR...
- `sqlite3Update` **(Many-Argument Workhorses)** (@ `src/update.c`) -> Impact: **701.0** | LOC: 879
  * *Intent:* /* ** Process an UPDATE statement. ** ** UPDATE OR IGNORE tbl SET a=b, c=d FROM tbl2... WHERE e<5 AND f NOT NULL; ** \_______/ \_/ \______/ \_____/ \_...
- `sqlite3_str_vappendf` **(Many-Argument Workhorses)** (@ `src/printf.c`) -> Impact: **638.6** | LOC: 813
  * *Intent:* # define SQLITE_PRINT_BUF_SIZE 70 #endif #define etBUFSIZE SQLITE_PRINT_BUF_SIZE /* Size of the output buffer */ /* ** Hard limit on the precision of ...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 152 | 174416.06 | 56.99% | 23.75% |
| `ext/misc` | 63 | 26580.28 | 66.18% | 18.27% |
| `tool` | 86 | 25626.22 | 53.88% | 11.57% |
| `ext/fts5` | 19 | 24708.2 | 58.67% | 16.17% |
| `test` | 68 | 18379.38 | 20.01% | 0.0% |
| `ext/fts3` | 19 | 11832.08 | 52.03% | 14.83% |
| `ext/session` | 7 | 10125.32 | 63.12% | 23.05% |
| `ext/wasm/api` | 20 | 9064.58 | 37.5% | 52.04% |
| `ext/rtree` | 9 | 6381.82 | 47.87% | 10.67% |
| `ext/wasm` | 33 | 6255.75 | 34.65% | 11.3% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ext/jni/src/org/sqlite/jni/fts5/Fts5ExtensionApi.java` -> **100.0%** Exposure
- `ext/jni/src/org/sqlite/jni/wrapper1/SqlFunction.java` -> **100.0%** Exposure
- `ext/jni/src/org/sqlite/jni/capi/OutputPointer.java` -> **99.9839%** Exposure
- `src/os.c` -> **99.9558%** Exposure
- `src/hwtime.h` -> **99.9447%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ext/wasm/mkdist.sh` -> **100.0%** Exposure
- `tool/emcc.sh.in` -> **100.0%** Exposure
- `tool/mkautoconfamal.sh` -> **100.0%** Exposure
- `contrib/sqlitecon.tcl` -> **100.0%** Exposure
- `ext/fts3/fts3speed.tcl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ext/jni/src/org/sqlite/jni/wrapper1/Sqlite.java` -> **94** Orphaned Functions | **2** Duplicates
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
- **Unknown Dependencies:** `1513` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/shell.c.in` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.229)
- **Top Global Matches:** file_cluster_6: 9.229, file_cluster_8: 12.099, file_cluster_4: 15.786
- **Magnitude:** 13483.5 | **LOC:** 13720 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 95.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.529; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (95.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_meta_command` **(Many-Argument Workhorses)** (Impact: 1983.9)
    * *Intent:* /* ** If an input line begins with "." then invoke this routine to ** process that line. ** ** Retur...
  * `main` **(Many-Argument Workhorses)** (Impact: 574.8)
    * *Intent:* #endif /* WIN32 */ /* ** This is the main entry point for the process. Everything starts here. ** **...
  * `dotCmdMode` **(Compute Cores)** (Impact: 336.5)
    * *Intent:* ** how to encode them. ARG can be "off", "on", ** "sql", "csv", "html", "tcl", or "json". ** --title...
  * `dotCmdImport` **(Compute Cores)** (Impact: 203.6)
    * *Intent:* ** ** Options: ** --ascii Do not use RFC-4180 quoting. Use \037 and \036 ** as column and row separa...
  * `shellFormatSchema` **(Many-Argument Workhorses)** (Impact: 141.7)
    * *Intent:* /* ** SQL Function: shell_format_schema(SQL,FLAGS) ** ** This function is internally by the CLI to a...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 51 instances
* *Amplified Cascading Flux:* 2094 instances
* *High Risk Execution (weighted view):* 11
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 6447
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3416`, `structural_boundaries: 781`, `args: 492`, `func_start: 202`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 14`, `state_mutation: 2259`, `dead_code: 4`, `planned_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `io: 20`, `api: 57`, `import: 25`
* *Defense:* `safety: 54`, `doc: 9`, `immutability_locks: 385`, `cleanup: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.529
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 43):` assert.h, ctype.h, dirent.h, readline.h, fcntl.h, io.h, linenoise.h, math.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/btree.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.252)
- **Top Global Matches:** file_cluster_6: 6.252, file_cluster_4: 10.193, file_cluster_8: 15.604
- **Magnitude:** 9566.34 | **LOC:** 11569 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **1**; blast radius 8.814; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%), Guard Balance (formerly Safety Score) (72.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `balance_nonroot` **(Many-Argument Workhorses)** (Impact: 431.1)
    * *Intent:* ** be rolled back. ** ** The third argument to this function, aOvflSpace, is a pointer to a ** buffe...
  * `allocateBtreePage` **(Many-Argument Workhorses)** (Impact: 206.5)
    * *Intent:* ** SQLITE_OK is returned on success. Any other return value indicates ** an error. *ppPage is set to...
  * `sqlite3BtreeOpen` **(Many-Argument Workhorses)** (Impact: 194.6)
    * *Intent:* ** when sqlite3BtreeClose() is called. ** ** If zFilename is ":memory:" then an in-memory database i...
  * `sqlite3BtreeInsert` **(Many-Argument Workhorses)** (Impact: 189.5)
    * *Intent:* ** sqlite3BtreeIndexMoveto() to seek cursor pCur to (pKey,nKey) has already ** been performed. In ot...
  * `btreeBeginTrans` **(Many-Argument Workhorses)** (Impact: 124.3)
    * *Intent:* ** If an initial attempt to acquire the lock fails because of lock contention ** and the database wa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1585 instances
* *State Mutation (weighted view):* 4843
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1837`, `structural_boundaries: 595`, `args: 306`, `func_start: 220`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 1673`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 66`
* *Architecture:* `api: 90`, `import: 1`
* *Defense:* `safety: 704`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.814
  * `Choke Point (Betweenness):` 0.003398 | `Ripple Effect (Closeness):` 0.215013
  * `Imports (Out-Degree: 19):` btreeInt.h
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `tool/lemon.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.503)
- **Top Global Matches:** file_cluster_6: 6.503, file_cluster_4: 8.497, file_cluster_16: 16.714
- **Magnitude:** 8038.64 | **LOC:** 6076 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.529; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Guard Balance (formerly Safety Score) (89.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.4%)
- **Documentation Coverage:** 49.5763% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ReportTable` **(Many-Argument Workhorses)** (Impact: 399.2)
    * *Intent:* /* Generate C source code for the parser */
  * `parseonetoken` **(Compute Cores)** (Impact: 328.3)
    * *Intent:* /* Parse a single token */
  * `Parse` **(Compute Cores)** (Impact: 118.0)
    * *Intent:* /* In spite of its name, this function is really a scanner. It read ** in the entire input file (all...
  * `translate_code` **(Many-Argument Workhorses)** (Impact: 111.8)
    * *Intent:* /* ** Write and transform the rp->code string so that symbols are expanded. ** Populate the rp->code...
  * `print_stack_union` **(Many-Argument Workhorses)** (Impact: 81.8)
    * *Intent:* /* ** Print the definition of the union used for the parser's data stack. ** This union contains fie...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1627 instances
* *High Risk Execution (weighted view):* 23
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 4995
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1396`, `structural_boundaries: 886`, `args: 216`, `func_start: 132`, `class_start: 253`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 27`, `state_mutation: 1741`, `dead_code: 8`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 192`, `import: 7`
* *Defense:* `safety: 35`, `doc: 23`, `test: 1`, `immutability_locks: 107`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.529
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, ctype.h, stdarg.h, stdio.h, stdlib.h, string.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/where.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.998)
- **Top Global Matches:** file_cluster_8: 5.998, file_cluster_6: 11.91, file_cluster_4: 20.551
- **Magnitude:** 7885.98 | **LOC:** 7884 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **2**; blast radius 1.694; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%), Complexity Load (formerly Cognitive Load) (77.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3WhereBegin` **(Many-Argument Workhorses)** (Impact: 519.2)
    * *Intent:* ** ** pOrderBy is a pointer to the ORDER BY clause (or the GROUP BY clause ** if the WHERE_GROUPBY f...
  * `wherePathSatisfiesOrderBy` **(Many-Argument Workhorses)** (Impact: 310.8)
    * *Intent:* ** (or GROUP BY) without requiring a separate sort operation. Return N: ** ** N>0: N terms of the OR...
  * `whereLoopAddBtreeIndex` **(Many-Argument Workhorses)** (Impact: 261.0)
    * *Intent:* #endif /* ** We have so far matched pBuilder->pNew->u.btree.nEq terms of the ** index pIndex. Try to...
  * `wherePathSolver` **(Many-Argument Workhorses)** (Impact: 203.1)
    * *Intent:* /* ** Given the list of WhereLoop objects at pWInfo->pLoops, this routine ** attempts to find the lo...
  * `whereLoopAddBtree` **(Many-Argument Workhorses)** (Impact: 148.5)
    * *Intent:* ** cost = nSeek * (log(nRow) + (K+3.0) * nVisit) // non-covering index ** ** Normally, nSeek is 1. n...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1278 instances
* *State Mutation (weighted view):* 3982
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1522`, `structural_boundaries: 395`, `args: 178`, `func_start: 107`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1426`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 32`, `import: 2`
* *Defense:* `safety: 233`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.694
  * `Choke Point (Betweenness):` 0.002292 | `Ripple Effect (Closeness):` 0.150379
  * `Imports (Out-Degree: 20):` sqliteInt.h, whereInt.h
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `ext/fts5/fts5_index.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.327)
- **Top Global Matches:** file_cluster_4: 5.327, file_cluster_6: 9.936, file_cluster_16: 11.288
- **Magnitude:** 7847.98 | **LOC:** 9546 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 0.707; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%), Complexity Load (formerly Cognitive Load) (73.3%)
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
* *Amplified Cascading Flux:* 1222 instances
* *State Mutation (weighted view):* 3787
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1493`, `structural_boundaries: 517`, `args: 283`, `func_start: 238`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 1343`, `dead_code: 2`, `planned_debt: 6`, `unreferenced_by_name: 29`
* *Architecture:* `api: 84`, `import: 1`
* *Defense:* `safety: 190`, `doc: 2`, `test: 8`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.707
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.00702
  * `Imports (Out-Degree: 14):` fts5Int.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/select.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.586)
- **Top Global Matches:** file_cluster_6: 8.586, file_cluster_8: 9.202, file_cluster_4: 16.575
- **Magnitude:** 7570.68 | **LOC:** 8983 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 71.4%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **1**; blast radius 3.93; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%), Guard Balance (formerly Safety Score) (74.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3Select` **(Many-Argument Workhorses)** (Impact: 571.4)
    * *Intent:* ** * DISTINCT ORDER BY -> GROUP BY optimization tag-select-0500 ** * Set up for ORDER BY tag-select-...
  * `selectInnerLoop` **(Many-Argument Workhorses)** (Impact: 259.4)
    * *Intent:* #endif /* ** This routine generates the code for the inside of the inner loop ** of a SELECT. ** ** ...
  * `selectExpander` **(Many-Argument Workhorses)** (Impact: 242.8)
    * *Intent:* ** that implements the view. A copy is made of the view's SELECT ** statement so that we can freely ...
  * `flattenSubquery` **(Many-Argument Workhorses)** (Impact: 211.7)
    * *Intent:* ** (28) The subquery is not a MATERIALIZED CTE. (This is handled ** in the caller before ever reachi...
  * `generateSortTail` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* #else /* No-op versions of the explainXXX() functions and macros. */ # define explainTempTable(y,z) ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1194 instances
* *State Mutation (weighted view):* 3757
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1487`, `structural_boundaries: 440`, `args: 190`, `func_start: 106`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 1369`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `safety: 349`, `doc: 3`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.93
  * `Choke Point (Betweenness):` 0.001838 | `Ripple Effect (Closeness):` 0.205742
  * `Imports (Out-Degree: 19):` sqliteInt.h
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/vdbe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.608)
- **Top Global Matches:** file_cluster_6: 6.608, file_cluster_4: 10.895, file_cluster_8: 15.366
- **Magnitude:** 6820.92 | **LOC:** 9319 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **3**; blast radius 3.594; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.0%), Guard Balance (formerly Safety Score) (72.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.6%)
- **Documentation Coverage:** 49.6241% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3VdbeExec` **(Many-Argument Workhorses)** (Impact: 2410.6)
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
* *Structure:* `branch: 1531`, `structural_boundaries: 235`, `args: 109`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 1`, `state_mutation: 1378`, `planned_debt: 5`, `unreferenced_by_name: 4`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 696`, `doc: 4`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.594
  * `Choke Point (Betweenness):` 0.003345 | `Ripple Effect (Closeness):` 0.184617
  * `Imports (Out-Degree: 29):` hwtime.h, sqliteInt.h, vdbeInt.h
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/expr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.29)
- **Top Global Matches:** file_cluster_6: 6.29, file_cluster_4: 10.253, file_cluster_8: 15.575
- **Magnitude:** 6488.76 | **LOC:** 7703 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 81.8%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **1**; blast radius 4.64; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%), Guard Balance (formerly Safety Score) (65.9%)
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
* *Structure:* `branch: 1525`, `structural_boundaries: 581`, `args: 292`, `func_start: 176`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 930`, `planned_debt: 8`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `api: 119`, `import: 1`
* *Defense:* `safety: 415`, `doc: 1`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.64
  * `Choke Point (Betweenness):` 0.001555 | `Ripple Effect (Closeness):` 0.207116
  * `Imports (Out-Degree: 18):` sqliteInt.h
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `ext/session/sqlite3session.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.581)
- **Top Global Matches:** file_cluster_6: 5.581, file_cluster_4: 9.37, file_cluster_8: 15.887
- **Magnitude:** 6483.7 | **LOC:** 6791 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 0.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sessionChangeMerge` **(Many-Argument Workhorses)** (Impact: 189.1)
    * *Intent:* /* ** This function is called to merge two changes to the same row together as ** part of an sqlite3...
  * `sessionChangesetApply` **(Many-Argument Workhorses)** (Impact: 172.6)
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
* *Structure:* `branch: 1137`, `structural_boundaries: 512`, `args: 179`, `func_start: 158`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 1022`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 35`
* *Architecture:* `api: 73`, `import: 5`
* *Defense:* `safety: 97`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.808
  * `Choke Point (Betweenness):` 0.000224 | `Ripple Effect (Closeness):` 0.010985
  * `Imports (Out-Degree: 14):` assert.h, sqlite3session.h, sqliteInt.h, string.h, vdbeInt.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/test1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.337)
- **Top Global Matches:** file_cluster_4: 8.337, file_cluster_12: 9.696, file_cluster_16: 10.059
- **Magnitude:** 6036.5 | **LOC:** 9453 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **16**; blast radius 1.034; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (53.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_carray_bind` **(Many-Argument Workhorses)** (Impact: 227.7)
    * *Intent:* ** Options: ** -malloc ** -transient ** -static ** -v2 ** -int32 ** -int64 ** -double ** -text ** -b...
  * `fpnum_compare` **(Many-Argument Workhorses)** (Impact: 188.7)
    * *Intent:* ** taking rounding into consideration. ** ** D. An exponent on a floating point of the form "e+NN" w...
  * `test_create_function_v2` **(Many-Argument Workhorses)** (Impact: 60.2)
  * `test_stmt_scanstatus` **(Many-Argument Workhorses)** (Impact: 56.8)
    * *Intent:* #ifdef SQLITE_ENABLE_STMT_SCANSTATUS /* ** Usage: sqlite3_stmt_scanstatus ?-flags FLAGS? STMT IDX */...
  * `test_test_control` **(Many-Argument Workhorses)** (Impact: 56.5)
    * *Intent:* /* ** sqlite3_test_control VERB ARGS... */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 709 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 2182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1231`, `structural_boundaries: 1251`, `args: 328`, `func_start: 261`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 159`, `high_risk_execution: 1`, `state_mutation: 764`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 72`, `import: 16`
* *Defense:* `safety: 58`, `immutability_locks: 174`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.034
  * `Choke Point (Betweenness):` 0.025841 | `Ripple Effect (Closeness):` 0.089318
  * `Imports (Out-Degree: 58):` ctype.h, os_win.h, process.h, sqliteInt.h, stdlib.h, string.h, param.h, resource.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/json.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.742)
- **Top Global Matches:** file_cluster_6: 7.742, file_cluster_8: 10.186, file_cluster_4: 15.43
- **Magnitude:** 5652.72 | **LOC:** 5635 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.866; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 49.3976% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jsonTranslateTextToBlob` **(Many-Argument Workhorses)** (Impact: 364.4)
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
* *Structure:* `branch: 1283`, `structural_boundaries: 571`, `args: 126`, `func_start: 107`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 899`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 84`, `doc: 10`, `immutability_locks: 114`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.866
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.147518
  * `Imports (Out-Degree: 11):` sqliteInt.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/build.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.776)
- **Top Global Matches:** file_cluster_4: 6.776, file_cluster_6: 8.0, file_cluster_16: 14.519
- **Magnitude:** 5411.24 | **LOC:** 5821 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **1**; blast radius 7.505; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3CreateIndex` **(Many-Argument Workhorses)** (Impact: 469.5)
    * *Intent:* /* ** Create a new index for an SQL table. pName1.pName2 is the name of the index ** and pTblList is...
  * `sqlite3EndTable` **(Many-Argument Workhorses)** (Impact: 174.2)
    * *Intent:* ** occurred. ** ** An entry for the table is made in the schema table on disk, unless ** this is a t...
  * `sqlite3StartTable` **(Many-Argument Workhorses)** (Impact: 122.6)
    * *Intent:* ** the first of several action routines that get called in response ** to a CREATE TABLE statement. ...
  * `sqlite3DropTable` **(Many-Argument Workhorses)** (Impact: 74.6)
    * *Intent:* /* ** This routine is called to do the work of a DROP TABLE statement. ** pName is the name of the t...
  * `sqlite3CreateForeignKey` **(Many-Argument Workhorses)** (Impact: 72.3)
    * *Intent:* ** currently under construction. pFromCol determines which columns ** in the current table point to ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 816 instances
* *State Mutation (weighted view):* 2535
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1007`, `structural_boundaries: 305`, `args: 165`, `func_start: 129`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 903`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 43`
* *Architecture:* `api: 99`, `import: 1`
* *Defense:* `safety: 273`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.505
  * `Choke Point (Betweenness):` 0.004979 | `Ripple Effect (Closeness):` 0.213166
  * `Imports (Out-Degree: 27):` sqliteInt.h
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `src/os_win.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.376)
- **Top Global Matches:** file_cluster_6: 7.376, file_cluster_4: 7.846, file_cluster_16: 15.312
- **Magnitude:** 5355.62 | **LOC:** 6500 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 0.833; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 49.6835% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `winWrite` **(Many-Argument Workhorses)** (Impact: 805.8)
    * *Intent:* /* ** Write data from a buffer into a file. Return SQLITE_OK on success ** or some other error code ...
  * `winRead` **(Many-Argument Workhorses)** (Impact: 799.0)
    * *Intent:* /* ** Read data from a file into a buffer. Return SQLITE_OK if all ** bytes were read successfully a...
  * `winOpen` **(Many-Argument Workhorses)** (Impact: 205.0)
    * *Intent:* /* ** The Windows version of xAccess() accepts an extra bit in the flags ** parameter that prevents ...
  * `winFullPathnameNoMutex` **(Many-Argument Workhorses)** (Impact: 133.8)
    * *Intent:* #endif /* __CYGWIN__ */ /* ** Turn a relative pathname into a full pathname. Write the full ** pathn...
  * `winShmLock` **(Many-Argument Workhorses)** (Impact: 116.9)
    * *Intent:* /* ** Change the lock state for a shared-memory segment. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 575 instances
* *State Mutation (weighted view):* 1797
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 771`, `structural_boundaries: 415`, `args: 415`, `func_start: 113`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 647`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 15`
* *Architecture:* `api: 39`, `import: 4`
* *Defense:* `safety: 124`, `doc: 6`, `test: 4`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.833
  * `Choke Point (Betweenness):` 0.00092 | `Ripple Effect (Closeness):` 0.108163
  * `Imports (Out-Degree: 12):` os_common.h, os_win.h, sqliteInt.h, time.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/os_unix.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.573)
- **Top Global Matches:** file_cluster_6: 7.573, file_cluster_4: 10.045, file_cluster_12: 17.14
- **Magnitude:** 5334.44 | **LOC:** 8590 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.529; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 49.4565% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unixOpen` **(Many-Argument Workhorses)** (Impact: 222.7)
    * *Intent:* ** sqlite3OsOpenExclusive(); ** ** These calls correspond to the following combinations of flags: **...
  * `unixShmLock` **(Many-Argument Workhorses)** (Impact: 123.7)
    * *Intent:* #endif /* !defined(SQLITE_WASI) && !defined(SQLITE_OMIT_WAL) */ /* ** Change the lock state for a sh...
  * `unixFileControl` **(Many-Argument Workhorses)** (Impact: 98.0)
    * *Intent:* #endif /* ** Information and control of an open file handle. */
  * `proxyTakeConch` **(Many-Argument Workhorses)** (Impact: 92.9)
    * *Intent:* /* Takes the conch by taking a shared lock and read the contents conch, if ** lockPath is non-NULL, ...
  * `fillInUnixFile` **(Many-Argument Workhorses)** (Impact: 92.2)
    * *Intent:* /**************************************************************************** **********************...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 848 instances
* *State Mutation (weighted view):* 2604
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1111`, `structural_boundaries: 492`, `args: 341`, `func_start: 137`, `class_start: 69`
* *Risk/State:* `safety_bypasses: 124`, `state_mutation: 908`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 24`, `import: 23`
* *Defense:* `safety: 232`, `doc: 16`, `test: 4`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.529
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` dlfcn.h, errno.h, fcntl.h, limits.h, os_common.h, pthread.h, semaphore.h, sqliteInt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/fts3/fts3_write.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.4)
- **Top Global Matches:** file_cluster_6: 6.4, file_cluster_4: 6.791, file_cluster_16: 14.597
- **Magnitude:** 5093.98 | **LOC:** 5857 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.744; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 96.35% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3Fts3SegReaderStep` **(Many-Argument Workhorses)** (Impact: 100.5)
  * `sqlite3Fts3Incrmerge` **(Many-Argument Workhorses)** (Impact: 98.3)
    * *Intent:* /* ** Attempt an incremental merge that writes nMerge leaf blocks. ** ** Incremental merges happen n...
  * `fts3IncrmergeLoad` **(Many-Argument Workhorses)** (Impact: 86.5)
    * *Intent:* ** This function is called when initializing an incremental-merge operation. ** It checks if the exi...
  * `sqlite3Fts3UpdateMethod` **(Many-Argument Workhorses)** (Impact: 71.7)
    * *Intent:* /* ** This function does the work for the xUpdate method of FTS3 virtual ** tables. The schema of th...
  * `fts3SpecialInsert` **(Compute Cores)** (Impact: 69.7)
    * *Intent:* /* ** Handle a 'special' INSERT of the form: ** ** "INSERT INTO tbl(tbl) VALUES(<expr>)" ** ** Argum...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 873 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 2653
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 888`, `structural_boundaries: 265`, `args: 134`, `func_start: 118`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 907`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 16`
* *Architecture:* `api: 44`, `import: 5`
* *Defense:* `safety: 102`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.744
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.00468
  * `Imports (Out-Degree: 11):` assert.h, fts3Int.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vdbeaux.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.721)
- **Top Global Matches:** file_cluster_4: 5.721, file_cluster_6: 8.285, file_cluster_16: 13.263
- **Magnitude:** 4597.28 | **LOC:** 5585 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **37** in-repo importer(s); it depends on **2**; blast radius 8.384; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.5%), Guard Balance (formerly Safety Score) (71.4%)
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
  * `sqlite3VdbeDisplayComment` **(Many-Argument Workhorses)** (Impact: 70.2)
    * *Intent:* /* ** Compute a string for the "comment" field of a VDBE opcode listing. ** ** The Synopsis: field i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 679 instances
* *State Mutation (weighted view):* 2128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 933`, `structural_boundaries: 425`, `args: 229`, `func_start: 163`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 770`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 73`
* *Architecture:* `io: 1`, `api: 125`, `import: 2`
* *Defense:* `safety: 236`, `immutability_locks: 91`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.384
  * `Choke Point (Betweenness):` 0.003982 | `Ripple Effect (Closeness):` 0.216514
  * `Imports (Out-Degree: 22):` sqliteInt.h, vdbeInt.h
  * `Imported By (In-Degree: 37):` (Excluded from Brief to save tokens)

### `src/pager.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.367)
- **Top Global Matches:** file_cluster_6: 5.367, file_cluster_4: 9.865, file_cluster_8: 15.195
- **Magnitude:** 4362.02 | **LOC:** 7835 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **2**; blast radius 7.059; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3PagerOpen` **(Many-Argument Workhorses)** (Impact: 156.0)
    * *Intent:* ** The flags argument is used to specify properties that affect the ** operation of the pager. It sh...
  * `pager_playback_one_page` **(Many-Argument Workhorses)** (Impact: 125.3)
    * *Intent:* ** is successfully read from the (sub-)journal file but appears to be ** corrupted, SQLITE_DONE is r...
  * `sqlite3PagerCommitPhaseOne` **(Many-Argument Workhorses)** (Impact: 115.0)
    * *Intent:* ** * the database file synced. ** ** The only thing that remains to commit the transaction is to fin...
  * `pager_end_transaction` **(Many-Argument Workhorses)** (Impact: 88.5)
    * *Intent:* ** ** After the journal is finalized, the pager moves to PAGER_READER state. ** If running in non-ex...
  * `pager_playback` **(Many-Argument Workhorses)** (Impact: 70.9)
    * *Intent:* ** back (or no pages if the journal header is corrupted). The journal file ** is then deleted and SQ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 618 instances
* *State Mutation (weighted view):* 1910
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 294`, `args: 192`, `func_start: 149`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 674`, `dead_code: 17`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 61`
* *Architecture:* `api: 83`, `import: 2`
* *Defense:* `safety: 378`, `doc: 2`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.059
  * `Choke Point (Betweenness):` 0.033804 | `Ripple Effect (Closeness):` 0.212436
  * `Imports (Out-Degree: 18):` sqliteInt.h, wal.h
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `ext/rbu/sqlite3rbu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.614)
- **Top Global Matches:** file_cluster_6: 6.614, file_cluster_4: 8.287, file_cluster_16: 15.869
- **Magnitude:** 4226.98 | **LOC:** 5448 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.632; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%), Complexity Load (formerly Cognitive Load) (73.3%)
- **Documentation Coverage:** 99.3007% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rbuObjIterPrepareAll` **(Many-Argument Workhorses)** (Impact: 112.8)
    * *Intent:* /* ** Ensure that the SQLite statement handles required to update the ** target database object curr...
  * `openRbuHandle` **(Many-Argument Workhorses)** (Impact: 102.0)
  * `rbuOpenDatabase` **(Many-Argument Workhorses)** (Impact: 86.0)
    * *Intent:* /* ** Open the database handle and attach the RBU database as "rbu". If an ** error occurs, leave an...
  * `rbuObjIterGetIndexWhere` **(Many-Argument Workhorses)** (Impact: 84.4)
  * `rbuObjIterGetIndexCols` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* ** CREATE INDEX i1 ON t1(c, b COLLATE nocase); ** ** and "t1" is a table with an explicit INTEGER PR...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 668 instances
* *State Mutation (weighted view):* 2063
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 888`, `structural_boundaries: 267`, `args: 153`, `func_start: 123`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 727`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 11`
* *Architecture:* `io: 1`, `api: 34`, `import: 6`
* *Defense:* `safety: 90`, `doc: 4`, `immutability_locks: 148`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.632
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.00351
  * `Imports (Out-Degree: 11):` assert.h, sqlite3.h, sqlite3rbu.h, stdio.h, string.h, windows.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.05)
- **Top Global Matches:** file_cluster_4: 5.05, file_cluster_6: 9.386, file_cluster_15: 12.12
- **Magnitude:** 3915.72 | **LOC:** 5190 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **176** in-repo importer(s); it depends on **4**; blast radius 40.731; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3ParseUri` **(Many-Argument Workhorses)** (Impact: 194.2)
    * *Intent:* ** ** If successful, SQLITE_OK is returned. In this case *ppVfs is set to point to ** the VFS that s...
  * `sqlite3ErrName` **(Compute Cores)** (Impact: 137.0)
    * *Intent:* /* ** Return a static string containing the name corresponding to the error code ** specified in the...
  * `sqlite3_test_control` **(Many-Argument Workhorses)** (Impact: 130.6)
    * *Intent:* /* ** Interface to the testing logic. */
  * `openDatabase` **(Many-Argument Workhorses)** (Impact: 125.2)
    * *Intent:* /* ** This routine does the work of opening a database on behalf of ** sqlite3_open() and sqlite3_op...
  * `sqlite3CreateFunc` **(Many-Argument Workhorses)** (Impact: 113.7)
    * *Intent:* /* ** This function is exactly the same as sqlite3_create_function(), except ** that it is designed ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 578 instances
* *State Mutation (weighted view):* 1782
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 762`, `structural_boundaries: 607`, `args: 200`, `func_start: 125`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 626`, `dead_code: 12`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 82`
* *Architecture:* `api: 113`, `import: 4`
* *Defense:* `safety: 73`, `doc: 4`, `immutability_locks: 143`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.731
  * `Choke Point (Betweenness):` 0.03649 | `Ripple Effect (Closeness):` 0.318926
  * `Imports (Out-Degree: 38):` fts3.h, rtree.h, sqliteInt.h, sqliteicu.h
  * `Imported By (In-Degree: 176):` (Excluded from Brief to save tokens)

### `src/tclsqlite.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.066)
- **Top Global Matches:** file_cluster_6: 8.066, file_cluster_4: 8.368, file_cluster_12: 15.315
- **Magnitude:** 3861.64 | **LOC:** 4600 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 1.038; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DbObjCmd` **(Many-Argument Workhorses)** (Impact: 980.9)
    * *Intent:* /* ** The "sqlite" command below creates a new Tcl command for each ** connection it opens to an SQL...
  * `dbQrf` **(Many-Argument Workhorses)** (Impact: 202.9)
    * *Intent:* ** -titlealign eTitleAlign ** -border bBorder ** -wrap nWrap ** -screenwidth nScreenWidth ** -lineli...
  * `DbMain` **(Many-Argument Workhorses)** (Impact: 137.6)
    * *Intent:* ** ?-create BOOLEAN? ?-nomutex BOOLEAN? ** ?-nofollow BOOLEAN? ** ** This is the main Tcl command. W...
  * `dbPrepareAndBind` **(Many-Argument Workhorses)** (Impact: 133.8)
    * *Intent:* ** Search the cache for a prepared-statement object that implements the ** first SQL statement in th...
  * `auth_callback` **(Many-Argument Workhorses)** (Impact: 133.6)
    * *Intent:* #ifndef SQLITE_OMIT_AUTHORIZATION /* ** This is the authentication function. It appends the authenti...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 527 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 860`, `structural_boundaries: 392`, `args: 124`, `func_start: 68`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 549`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 28`, `import: 15`
* *Defense:* `safety: 30`, `doc: 2`, `immutability_locks: 99`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.038
  * `Choke Point (Betweenness):` 0.002356 | `Ripple Effect (Closeness):` 0.088238
  * `Imports (Out-Degree: 17):` assert.h, ctype.h, errno.h, io.h, msvc.h, qrf.h, signal.h, sqlite3.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ext/rtree/rtree.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.745)
- **Top Global Matches:** file_cluster_6: 6.745, file_cluster_4: 8.037, file_cluster_16: 15.178
- **Magnitude:** 3765.04 | **LOC:** 4486 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 0.77; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%), Complexity Load (formerly Cognitive Load) (74.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rtreeFilter` **(Many-Argument Workhorses)** (Impact: 94.8)
    * *Intent:* /* ** Rtree virtual table module xFilter method. */
  * `rtreeInit` **(Many-Argument Workhorses)** (Impact: 79.7)
    * *Intent:* /* ** This function is the implementation of both the xConnect and xCreate ** methods of the r-tree ...
  * `rtreeCallbackConstraint` **(Many-Argument Workhorses)** (Impact: 77.6)
    * *Intent:* #endif /* ** Check the RTree node or entry given by pCellData and p against the MATCH ** constraint ...
  * `SplitNode` **(Many-Argument Workhorses)** (Impact: 67.2)
  * `rtreeUpdate` **(Many-Argument Workhorses)** (Impact: 65.3)
    * *Intent:* /* ** The xUpdate method for rtree module virtual tables. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 631 instances
* *State Mutation (weighted view):* 1968
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 635`, `structural_boundaries: 265`, `args: 177`, `func_start: 110`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 706`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 32`, `import: 11`
* *Defense:* `safety: 56`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.77
  * `Choke Point (Betweenness):` 9.6e-05 | `Ripple Effect (Closeness):` 0.0065
  * `Imports (Out-Degree: 14):` assert.h, cmnintrin.h, geopoly.c, intrin.h, sqlite3.h, sqlite3ext.h, sqlite3rtree.h, stddef.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ext/fts5/fts5_expr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 4.754)
- **Top Global Matches:** file_cluster_6: 4.754, file_cluster_4: 11.555, file_cluster_8: 12.949
- **Magnitude:** 3597.86 | **LOC:** 3287 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.708; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (77.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3Fts5ParseNode` **(Many-Argument Workhorses)** (Impact: 92.8)
    * *Intent:* /* ** Allocate and return a new expression object. If anything goes wrong (i.e. ** OOM error), leave...
  * `fts5ExprPrint` **(Many-Argument Workhorses)** (Impact: 70.1)
  * `fts5ExprPrintTcl` **(Many-Argument Workhorses)** (Impact: 64.1)
    * *Intent:* /* ** Compose a tcl-readable representation of expression pExpr. Return a ** pointer to a buffer con...
  * `fts5ExprGetToken` **(Many-Argument Workhorses)** (Impact: 59.1)
    * *Intent:* /* ** Read the first token from the nul-terminated string at *pz. */
  * `sqlite3Fts5ExprClonePhrase` **(Many-Argument Workhorses)** (Impact: 58.6)
    * *Intent:* /* ** Create a new FTS5 expression by cloning phrase iPhrase of the ** expression passed as the seco...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 578 instances
* *State Mutation (weighted view):* 1748
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 707`, `structural_boundaries: 238`, `args: 113`, `func_start: 92`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 592`, `planned_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `api: 56`, `import: 3`
* *Defense:* `safety: 71`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.708
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.005106
  * `Imports (Out-Degree: 9):` fts5Int.h, fts5parse.h, stdio.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ext/fts5/fts5_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.805)
- **Top Global Matches:** file_cluster_4: 7.805, file_cluster_6: 11.451, file_cluster_12: 11.504
- **Magnitude:** 3320.06 | **LOC:** 3876 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 0.675; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.5%), Complexity Load (formerly Cognitive Load) (72.1%)
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
* *Structure:* `branch: 595`, `structural_boundaries: 253`, `args: 127`, `func_start: 113`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 587`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 29`, `import: 1`
* *Defense:* `safety: 87`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.000103 | `Ripple Effect (Closeness):` 0.005616
  * `Imports (Out-Degree: 20):` fts5Int.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ext/qrf/qrf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.876)
- **Top Global Matches:** file_cluster_8: 5.876, file_cluster_6: 16.319, file_cluster_3: 20.501
- **Magnitude:** 3312.8 | **LOC:** 2984 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.592; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.4%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `qrfColumnar` **(Compute Cores)** (Impact: 191.4)
    * *Intent:* /* ** Columnar modes require that the entire query be evaluated first, with ** results written into ...
  * `qrfInitialize` **(Many-Argument Workhorses)** (Impact: 144.4)
    * *Intent:* /* ** Initialize the internal Qrf object. */
  * `qrfEncodeText` **(Many-Argument Workhorses)** (Impact: 107.0)
    * *Intent:* /* ** Encode text appropriately and append it to pOut. */
  * `qrfRenderValue` **(Many-Argument Workhorses)** (Impact: 99.9)
    * *Intent:* /* ** Render value pVal into pOut */
  * `qrfWrapLine` **(Many-Argument Workhorses)** (Impact: 94.5)
    * *Intent:* /* ** (*pz)[] is a line of text that is to be displayed the box or table or ** similar tabular forma...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 578 instances
* *State Mutation (weighted view):* 1742
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 731`, `structural_boundaries: 268`, `args: 51`, `func_start: 49`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 586`, `unreferenced_by_name: 1`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `safety: 12`, `immutability_locks: 98`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.592
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.073935
  * `Imports (Out-Degree: 7):` assert.h, qrf.h, stdint.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/insert.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.888)
- **Top Global Matches:** file_cluster_8: 7.888, file_cluster_6: 8.36, file_cluster_4: 16.862
- **Magnitude:** 3213.0 | **LOC:** 3394 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **1**; blast radius 1.704; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqlite3GenerateConstraintChecks` **(Many-Argument Workhorses)** (Impact: 741.1)
    * *Intent:* ** NOT NULL REPLACE The NULL value is replace by the default ** value for that column. If the defaul...
  * `sqlite3Insert` **(Many-Argument Workhorses)** (Impact: 430.0)
    * *Intent:* ** end loop ** cleanup after the SELECT ** end co-routine R ** B: open temp table ** L: yield X, at ...
  * `xferOptimization` **(Many-Argument Workhorses)** (Impact: 254.2)
    * *Intent:* ** embedded in the code for details. ** ** This routine returns TRUE if the optimization is guarante...
  * `sqlite3CompleteInsertion` **(Many-Argument Workhorses)** (Impact: 66.5)
    * *Intent:* #else # define codeWithoutRowidPreupdate(a,b,c,d) #endif /* ** This routine generates code to finish...
  * `sqlite3MultiValues` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* ** of a schema item like a VIEW or TRIGGER). In this case there is no VM ** being generated when par...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 412 instances
* *State Mutation (weighted view):* 1273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 598`, `structural_boundaries: 137`, `args: 41`, `func_start: 29`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 449`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `safety: 114`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.704
  * `Choke Point (Betweenness):` 0.000279 | `Ripple Effect (Closeness):` 0.147518
  * `Imports (Out-Degree: 20):` sqliteInt.h
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `ext/misc/vtshim.c` (C) | Magnitude: 570.62 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: pointers: 406, indent_spaces: 403, state_mutation: 100, branch: 89
- `ext/wasm/common/testing.css` (CSS) | Magnitude: 0.85 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 50, class_start: 27, ui_framework: 5, immutability_locks: 4
- `ext/misc/templatevtab.c` (C) | Magnitude: 67.96 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 97, pointers: 45, structural_boundaries: 22, args: 12
- `src/mutex_noop.c` (C) | Magnitude: 81.44 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 76, pointers: 40, structural_boundaries: 36, args: 20
- `ext/wasm/fiddle/index.c-pp.html` (HTML) | Magnitude: 42.36 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 339, core_var_decl: 67, design_snake_case: 67, class_start: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ext/jni/src/org/sqlite/jni/fts5/XTokenizeCallback.java` (JAVA) | Magnitude: 3.38 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1
- `ext/jni/src/org/sqlite/jni/capi/CommitHookCallback.java` (JAVA) | Magnitude: 2.18 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 2, args: 1, func_start: 1
- `ext/jni/src/org/sqlite/jni/capi/ProgressHandlerCallback.java` (JAVA) | Magnitude: 2.18 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tool/mksqlite3internalh.tcl` (TCL) | Magnitude: 61.28 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 67, state_mutation: 16, branch: 14, io: 6
- `tool/mksqlite3h.tcl` (TCL) | Magnitude: 128.38 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 86, state_mutation: 46, branch: 22, io: 15
- `ext/wasm/api/sqlite3-vfs-opfs.c-pp.js` (JAVASCRIPT) | Magnitude: 1278.56 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 867, state_mutation: 212, core_var_decl: 162, branch: 144
- `ext/wasm/SQLTester/index.html` (HTML) | Magnitude: 60.9 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 25, core_var_decl: 25, branch: 19
- `ext/jni/src/org/sqlite/jni/capi/ResultCode.java` (JAVA) | Magnitude: 13.92 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 7, args: 4, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `ext/fts5/fts5_varint.c` (C) | Magnitude: 370.86 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 182, state_mutation: 108, bitwise_ops: 78, core_var_decl: 33
- `src/test_tclsh.c` (C) | Magnitude: 69.06 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 122, args: 58, api: 47, macros: 14
- `test/ossfuzz.c` (C) | Magnitude: 104.84 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 89, pointers: 30, branch: 20, structural_boundaries: 20
- `ext/misc/uuid.c` (C) | Magnitude: 147.94 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 28, branch: 24, structural_boundaries: 19
- `ext/misc/appendvfs.c` (C) | Magnitude: 308.66 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 270, pointers: 198, structural_boundaries: 89, encapsulation: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/lemon-test01.y` (YACC) | Magnitude: 22.48 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 54, pointers: 15, bitwise_ops: 15, state_mutation: 7
- `autoconf/Makefile.in` (MAKEFILE) | Magnitude: 81.76 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 68, indent_tabs: 64, func_start: 34, core_var_decl: 26
- `ext/fts5/fts5parse.y` (YACC) | Magnitude: 39.18 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 29, indent_spaces: 29, explicit_casts: 20, core_var_decl: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `ext/rtree/test_rtreedoc.c` (C) | Magnitude: 246.74 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 224, pointers: 105, state_mutation: 44, branch: 40
- `ext/jni/src/c/sqlite3-jni.c` (C) | Magnitude: 2563.16 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 3609, pointers: 1183, branch: 795, core_var_decl: 659
- `src/mem3.c` (C) | Magnitude: 411.44 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 361, state_mutation: 101, branch: 67, structural_boundaries: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `ext/jni/src/org/sqlite/jni/capi/Tester1.java` (JAVA) | Magnitude: 1164.06 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1897, core_var_decl: 459, design_snake_case: 331, structural_boundaries: 268

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ext/intck/sqlite3intck.c` (C) | Magnitude: 581.14 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 606, pointers: 213, branch: 121, state_mutation: 104

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ext/fts3/fts3_term.c` (C) | Magnitude: 226.62 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 221, pointers: 142, state_mutation: 50, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tool/mkpragmatab.tcl` (TCL) | Magnitude: 279.06 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 433, state_mutation: 88, branch: 68, debug_prints: 35
- `tool/Replace.cs` (CSHARP) | Magnitude: 28.06 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 74, doc: 49, structural_boundaries: 15, core_var_decl: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/shell.c.in` -> Churn: **100.0%** | Cog Load: 95.7589% | Debt: 8.6869%
- `ext/wasm/api/sqlite3-vfs-kvvfs.c-pp.js` -> Churn: **87.49%** | Cog Load: 46.17% | Debt: 89.8056%
- `ext/qrf/qrf.c` -> Churn: **85.42%** | Cog Load: 77.5111% | Debt: 7.8758%
- `src/select.c` -> Churn: **70.84%** | Cog Load: 74.6689% | Debt: 10.515%
- `src/util.c` -> Churn: **67.71%** | Cog Load: 75.5465% | Debt: 56.2909%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/shell.c.in` -> **drh** (95.7% isolated ownership) | Magnitude: 13483.5
- `src/vdbe.c` -> **drh** (100.0% isolated ownership) | Magnitude: 6820.92
- `src/expr.c` -> **drh** (81.8% isolated ownership) | Magnitude: 6488.76
- `ext/session/sqlite3session.c` -> **dan** (100.0% isolated ownership) | Magnitude: 6483.7
- `src/json.c` -> **drh** (100.0% isolated ownership) | Magnitude: 5652.72

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/main.c` -> **Severity: 3.649** (Bridge: 0.0365 * Flux: 100.0%)
- `src/pager.c` -> **Severity: 3.38** (Bridge: 0.0338 * Flux: 100.0%)
- `src/wal.c` -> **Severity: 2.958** (Bridge: 0.0296 * Flux: 100.0%)
- `src/test_thread.c` -> **Severity: 2.901** (Bridge: 0.0291 * Flux: 99.8568%)
- `src/test1.c` -> **Severity: 2.584** (Bridge: 0.0258 * Flux: 99.9906%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/printf.c` -> **Severity: 25.71** (Embedded: 0.3117 * Error Risk: 82.479%)
- `src/main.c` -> **Severity: 23.07** (Embedded: 0.3189 * Error Risk: 72.3363%)
- `src/util.c` -> **Severity: 22.908** (Embedded: 0.2745 * Error Risk: 83.4625%)
- `src/malloc.c` -> **Severity: 22.111** (Embedded: 0.3617 * Error Risk: 61.1312%)
- `src/vdbeapi.c` -> **Severity: 19.788** (Embedded: 0.2839 * Error Risk: 69.7014%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/tester.tcl` -> **Severity: 4373.754** (Blast Radius: 76.231 * Doc Risk: 57.375%)
- `src/malloc.c` -> **Severity: 2150.75** (Blast Radius: 43.015 * Doc Risk: 50.0%)
- `ext/fts3/fts3speed.tcl` -> **Severity: 2144.077** (Blast Radius: 22.253 * Doc Risk: 96.35%)
- `src/main.c` -> **Severity: 2036.55** (Blast Radius: 40.731 * Doc Risk: 50.0%)
- `src/printf.c` -> **Severity: 1374.55** (Blast Radius: 27.491 * Doc Risk: 50.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2931 literal sites + 133 sites through wrappers = 3064
- **`memory_alloc`:** 203 literal sites + 58 sites through wrappers = 261
- **`panics_and_aborts`:** 864 literal sites + 276 sites through wrappers = 1140

- `toss3` (function, panics_and_aborts, primitive): 94 call sites in 4 files -- `ext/wasm/api/sqlite3-api-oo1.c-pp.js`
- `toss` (function, panics_and_aborts, primitive): 67 call sites in 1 files -- `ext/wasm/jaccwabyt/jaccwabyt.js`
- `ErrorMsg` (function, debug_prints, primitive): 49 call sites in 1 files -- `tool/lemon.c`
- `fatal_error` (function, panics_and_aborts, primitive): 24 call sites in 1 files -- `test/wordcount.c`
- `modeSetStr` (function, memory_alloc, primitive): 17 call sites in 1 files -- `src/shell.c.in`
- `fatalError` (function, debug_prints, primitive): 12 call sites in 1 files -- `test/dbfuzz.c`
- `fatalError` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `test/dbfuzz.c`
- `toss` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `ext/wasm/api/sqlite3-opfs-async-proxy.js`
- `abort_due_to_error` (function, debug_prints, primitive): 9 call sites in 1 files -- `ext/session/session_speed_test.c`
- `abort_due_to_error` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `ext/session/session_speed_test.c`
- `modeFree` (function, memory_alloc, primitive): 9 call sites in 1 files -- `src/shell.c.in`
- `stats_line` (function, debug_prints, primitive): 9 call sites in 1 files -- `tool/lemon.c`
*(+64 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 50803 call pairs -- scoped 24.2%, unique 29.6%, ambiguous 1.3%, external 44.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 40298 | 24.2% | 36.6% | 0.1% | 39.2% |
| javascript | 3778 | 24.4% | 0.0% | 4.8% | 70.8% |
| tcl | 3720 | 14.3% | 3.5% | 0.7% | 81.5% |
| java | 2071 | 49.9% | 0.9% | 19.1% | 30.1% |
| yacc | 548 | 0.0% | 33.0% | 0.4% | 66.6% |
| html | 185 | 22.2% | 0.0% | 1.1% | 76.8% |
| shell | 138 | 8.0% | 0.0% | 0.0% | 92.0% |
| csharp | 39 | 12.8% | 0.0% | 0.0% | 87.2% |
| makefile | 20 | 0.0% | 0.0% | 0.0% | 100.0% |
| batch | 6 | 100.0% | 0.0% | 0.0% | 0.0% |

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
