# ARCHITECTURAL_BRIEF: opensourcecobol4j-src
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/opensourcecobol/opensourcecobol4j` |
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
- **Scope:** 938 analyzed artifact(s), 400886 LOC.
- **Load-bearing artifact:** `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolDataStorage.java` -- 54 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/misc.at` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cobj/typeck.c` at magnitude 7665.06 (structural weight, not risk).
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
| Total Artifacts | 1128 |
| Analyzed Artifacts (Scanned) | 938 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 190 |
| Total LOC | 400886 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 83.2% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7634 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.338 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7244 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 43 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 422 | 284556 | 45.0% |
| M4 | 264 | 47599 | 28.1% |
| JAVA | 102 | 26190 | 10.9% |
| YAML | 26 | 1700 | 2.8% |
| MARKDOWN | 24 | 0 | 2.6% |
| PLAINTEXT | 23 | 0 | 2.5% |
| C | 22 | 23210 | 2.3% |
| SHELL | 21 | 690 | 2.2% |
| MAKEFILE | 14 | 6527 | 1.5% |
| YACC | 6 | 9232 | 0.6% |
| XML | 3 | 0 | 0.3% |
| PERL | 3 | 255 | 0.3% |
| KOTLIN | 2 | 136 | 0.2% |
| POWERSHELL | 2 | 19 | 0.2% |
| DOCKERFILE | 1 | 24 | 0.1% |
| JSON | 1 | 18 | 0.1% |
| BATCH | 1 | 69 | 0.1% |
| LIVECODE | 1 | 661 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 35 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 902 |
| latin-1 | latin-1-fallback | 28 |
| cp1252 | cp1252-fallback | 7 |
| utf-8 | bom | 1 |

> 7 guessed file(s) read as double-byte text that decodes strictly as shift_jis / gbk: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `tests/i18n_sjis.src/data/out-sjis.txt`, `tests/esql-cobol-data.src/japanese.at`, `tests/esql-misc.src/long-sql.at`, `tests/i18n_sjis.src/pic-x.at`, `tests/i18n_sjis.src/program-id.at` and 2 more.

> 2 guessed file(s) read as double-byte text that decodes strictly as shift_jis: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `tests/i18n_sjis.src/national.at`, `tests/i18n_sjis.src/pic-n.at`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 32%, Interface Declarations Files 29%, Large Core Modules (3) 13%, Data / Markup / Trivial 11%, Large Core Modules 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 891 | 95.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 47 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 190*

**Composition by Extension & Reason:**
- `no_extension`: 52x Unsupported Format (.undeterminable), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 26047 LOC)
- `.sub`: 44x Excluded (Unsupported Extension: '.SUB'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `.conf`: 14x Excluded (Unsupported Extension: '.conf')
- `.am`: 8x Excluded (Unsupported Extension: '.am')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 1824 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3913 LOC), 1x Excluded (Machine-Generated Source Code Signature: 13617 LOC)
- `.txt`: 6x Excluded (Binary Format Detected)
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 121 LOC), 1x Excluded (Machine-Generated Source Code Signature: 522 LOC)
- `.dat`: 2x Excluded (Unsupported Extension: '.dat'), 2x Excluded (Unsupported Extension: '.DAT')
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.def`: 1x Zero-Density Threshold (LOC: 82, Signals: 0), 1x Zero-Density Threshold (LOC: 315, Signals: 0), 1x Zero-Density Threshold (LOC: 66, Signals: 0)
- `.in`: 1x Unsupported Format (.undeterminable), 1x Zero-Density Threshold (LOC: 64, Signals: 0)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lib`: 1x Excluded (Explicitly Denied Extension: '.LIB')
- `.guess`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.2 | 21.8 | 9.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.1 | 45.5 | 57.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 87.5 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 86.4 | 2.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 12.8 | 1.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4479 | 405 | 11 | `cobj/codegen.c` |
| cleanup | 2378 | 645 | 6 | `tests/run.src/functions.at` |
| guards | 3361 | 243 | 3 | `cobj/codegen.c` |
| danger | 22911 | 525 | 69 | `tests/cobol85/NC/NC218A.CBL` |
| concurrency | 48 | 12 | 0 | `.github/workflows/pull-request.yml` |
| connectivity | 2686 | 181 | 2 | `cobj/tree.h` |
| io | 5689 | 438 | 16 | `tests/cobol85/IX/IX215A.CBL` |
| crypto | 0 | 0 | 0 | - |
| ipc | 325 | 45 | 0 | `tests/data-rep.src/numeric-dump.cob` |
| time | 106 | 22 | 0 | `tests/cobol85/IF/IF108A.CBL` |
| serialization | 124 | 16 | 0 | `tests/cobol85/NC/NC218A.CBL` |
| regex | 403 | 44 | 0 | `tests/cobol85/NC/NC216A.CBL` |
| events | 115 | 13 | 0 | `cobj/codegen.c` |
| tests | 8053 | 278 | 16 | `tests/run.src/extensions.at` |
| docs | 2064 | 159 | 2 | `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolDataStorage.java` |
| debt | 3140 | 499 | 5 | `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/file/CobolFile.java` |
| mutation | 103616 | 646 | 283 | `cobj/codegen.c` |
| dead_code | 18564 | 508 | 49 | `tests/cobol85/NC/NC105A.CBL` |
| credential | 1 | 1 | 0 | `tests/esql-misc.src/compile.at` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 915 | 62 | 0 | `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/common/CobolIntrinsic.java` |
| ui | 2 | 1 | 0 | `ABOUT-NLS` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0909**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/cobol85/IX/IX215A.CBL` (Hits: 394)
- `libcobj/app/src/test/java/jp/osscons/opensourcecobol/libcobj/sql/CobolDataConverterTest.java` (Hits: 136)
- `tests/cobol85/IX/IX209A.CBL` (Hits: 132)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CobolDataStorage.java** (`libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolDataStorage.java`) — 54 inbound connections
2. **AbstractCobolField.java** (`libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/AbstractCobolField.java`) — 45 inbound connections
3. **CobolFieldAttribute.java** (`libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolFieldAttribute.java`) — 25 inbound connections
4. **CobolRuntimeException.java** (`libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/exceptions/CobolRuntimeException.java`) — 23 inbound connections
5. **CobolStopRunException.java** (`libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/exceptions/CobolStopRunException.java`) — 18 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **misc.at** (`tests/misc.at`) — 42 outbound dependencies
2. **command-line-options.at** (`tests/command-line-options.at`) — 36 outbound dependencies
3. **IndexedFileUtilMain.java** (`libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/user_util/indexed_file/IndexedFileUtilMain.java`) — 32 outbound dependencies
4. **jp-compat.at** (`tests/jp-compat.at`) — 29 outbound dependencies
5. **cobj.c** (`cobj/cobj.c`) — 26 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `validate_move` **(Many-Argument Workhorses)** (@ `cobj/typeck.c`) -> Impact: **552.5** | LOC: 649
- `_getopt_internal` **(Many-Argument Workhorses)** (@ `lib/getopt.c`) -> Impact: **430.9** | LOC: 680
  * *Intent:* long-named options. */
- `cb_validate_string` **(Many-Argument Workhorses)** (@ `cobj/typeck.c`) -> Impact: **353.5** | LOC: 384
  * *Intent:* /* * STRING statement */
- `han2zen` **(Many-Argument Workhorses)** (@ `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolNationalField.java`) -> Impact: **343.7** | LOC: 847
  * *Intent:* /** * 半角文字のバイト列をシフトJISの全角文字のバイト列へ変換する. * * @param str 変換対象の半角文字のバイト列 * @param size 変換対象のバイト数 * @return 全角へ変換したバイト列.変換後のサイズは{@link #workReturnSize}に格納さ...
- `cb_validate_unstring` **(Many-Argument Workhorses)** (@ `cobj/typeck.c`) -> Impact: **253.7** | LOC: 313
  * *Intent:* /* * UNSTRING statement */
- `cb_build_intrinsic` **(Many-Argument Workhorses)** (@ `cobj/tree.c`) -> Impact: **239.4** | LOC: 189
- `joutput_call` **(Compute Cores)** (@ `cobj/codegen.c`) -> Impact: **238.3** | LOC: 439
  * *Intent:* /* * CALL */
- `joutput_stmt` **(Many-Argument Workhorses)** (@ `cobj/codegen.c`) -> Impact: **227.7** | LOC: 398
- `validate_field_1` **(Compute Cores)** (@ `cobj/field.c`) -> Impact: **223.6** | LOC: 400
- `cb_load_conf` **(Many-Argument Workhorses)** (@ `cobj/config.c`) -> Impact: **210.8** | LOC: 257

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/cobol85/NC` | 95 | 85742.46 | 39.6% | 0.0% |
| `tests/cobol85/SQ` | 84 | 36739.14 | 39.92% | 0.0% |
| `cobj` | 29 | 30438.9 | 38.69% | 11.73% |
| `tests/cobol85/IF` | 45 | 22069.76 | 43.32% | 0.0% |
| `tests/cobol85/IX` | 29 | 21482.38 | 36.26% | 0.0% |
| `tests/cobol85/RL` | 26 | 11366.0 | 37.09% | 0.0% |
| `tests/cobol85/ST` | 25 | 10824.6 | 43.27% | 0.0% |
| `tests/cobol85/IC` | 25 | 9140.62 | 41.78% | 0.0% |
| `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data` | 18 | 7908.12 | 46.46% | 35.77% |
| `tests/cobol85/SG` | 13 | 6690.46 | 31.67% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolAlphanumericEditedField.java` -> **100.0%** Exposure
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/file/CobolItem.java` -> **100.0%** Exposure
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/file/CobolSequentialFile.java` -> **100.0%** Exposure
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/file/CobolSort.java` -> **100.0%** Exposure
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/file/FileIO.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compile` -> **100.0%** Exposure
- `libcobj/gradlew` -> **100.0%** Exposure
- `cobj/cobj.c` -> **100.0%** Exposure
- `cobj/codegen.c` -> **100.0%** Exposure
- `cobj/config.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/cobol85/NC/NC105A.CBL` -> **513** Orphaned Functions | **0** Duplicates
- `tests/cobol85/NC/NC104A.CBL` -> **327** Orphaned Functions | **0** Duplicates
- `tests/cobol85/NC/NC218A.CBL` -> **264** Orphaned Functions | **0** Duplicates
- `tests/cobol85/SG/SG101A.CBL` -> **260** Orphaned Functions | **0** Duplicates
- `tests/cobol85/NC/NC124A.CBL` -> **220** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/esql-misc.src/compile.at` -> **99.9571%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1054` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cobj/typeck.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.488)
- **Top Global Matches:** file_cluster_6: 6.488, file_cluster_4: 11.332, file_cluster_8: 14.856
- **Magnitude:** 7665.06 | **LOC:** 7413 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 1.397; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_move` **(Many-Argument Workhorses)** (Impact: 552.5)
  * `cb_validate_string` **(Many-Argument Workhorses)** (Impact: 353.5)
    * *Intent:* /* * STRING statement */
  * `cb_validate_unstring` **(Many-Argument Workhorses)** (Impact: 253.7)
    * *Intent:* /* * UNSTRING statement */
  * `cb_build_move_literal` **(Many-Argument Workhorses)** (Impact: 150.5)
  * `cb_emit_call` **(Many-Argument Workhorses)** (Impact: 129.6)
    * *Intent:* /* * CALL statement */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 857 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 2615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2290`, `structural_boundaries: 990`, `args: 488`, `func_start: 201`, `class_start: 84`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 901`, `dead_code: 5`, `planned_debt: 7`, `fragile_debt: 1`, `unreferenced_by_name: 107`
* *Architecture:* `api: 130`, `import: 12`
* *Defense:* `safety: 33`, `immutability_locks: 72`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.397
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.008155
  * `Imports (Out-Degree: 9):` cobj.h, config.h, ctype.h, locale.h, stdio.h, stdlib.h, string.h, time.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cobj/codegen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.855)
- **Top Global Matches:** file_cluster_8: 6.855, file_cluster_6: 11.695, file_cluster_4: 20.211
- **Magnitude:** 5802.12 | **LOC:** 7481 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 65.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.913; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.0%)
- **Documentation Coverage:** 91.3793% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `joutput_call` **(Compute Cores)** (Impact: 238.3)
    * *Intent:* /* * CALL */
  * `joutput_stmt` **(Many-Argument Workhorses)** (Impact: 227.7)
  * `joutput_param` **(Many-Argument Workhorses)** (Impact: 178.8)
    * *Intent:* /* * Parameter */
  * `codegen` **(Many-Argument Workhorses)** (Impact: 150.1)
  * `joutput_initialize_one` **(Many-Argument Workhorses)** (Impact: 124.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 34 instances
* *Amplified Cascading Flux:* 837 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 2628
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1552`, `structural_boundaries: 804`, `args: 270`, `func_start: 113`, `class_start: 165`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 2`, `state_mutation: 954`, `dead_code: 148`, `planned_debt: 6`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 12`, `import: 10`
* *Defense:* `safety: 24`, `doc: 13`, `immutability_locks: 69`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.006407
  * `Imports (Out-Degree: 8):` cobj.h, config.h, ctype.h, stdarg.h, stdio.h, stdlib.h, string.h, system.def...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cobj/parser.y` (YACC | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.629)
- **Top Global Matches:** file_cluster_15: 8.629, file_cluster_16: 9.227, file_cluster_4: 9.656
- **Magnitude:** 5746.86 | **LOC:** 7364 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.747; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Complexity Load (formerly Cognitive Load) (69.2%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `currency_sign_clause` **(Compute Cores)** (Impact: 72.4)
    * *Intent:* ; /* CURRENCY SIGN clause */
  * `size_optional` **(Compute Cores)** (Impact: 59.0)
    * *Intent:* ;
  * `statement` **(I/O & Config Routines)** (Impact: 55.3)
    * *Intent:* ;
  * `mnemonic_name_clause` **(Compute Cores)** (Impact: 45.4)
    * *Intent:* ; /* Mnemonic name clause */
  * `accp_attr` **(Compute Cores)** (Impact: 45.4)
    * *Intent:* ;
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 935 instances
* *State Mutation (weighted view):* 2950
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1404`, `structural_boundaries: 479`, `args: 1334`, `func_start: 598`
* *Risk/State:* `state_mutation: 1080`, `dead_code: 2`, `fragile_debt: 4`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 11`, `doc: 25`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` cobj.h, config.h, stdlib.h, string.h, tree.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobj/tree.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.901)
- **Top Global Matches:** file_cluster_6: 6.901, file_cluster_4: 8.197, file_cluster_12: 15.524
- **Magnitude:** 3112.06 | **LOC:** 2955 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **8**; blast radius 2.126; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_build_intrinsic` **(Many-Argument Workhorses)** (Impact: 239.4)
  * `cb_build_picture` **(Compute Cores)** (Impact: 186.3)
  * `cb_name_1` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `cb_concat_literals` **(Compute Cores)** (Impact: 69.7)
  * `finalize_file` **(Many-Argument Workhorses)** (Impact: 68.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 436 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1532
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 448`, `args: 192`, `func_start: 99`, `class_start: 105`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 660`, `fragile_debt: 3`
* *Architecture:* `api: 87`, `import: 8`
* *Defense:* `safety: 47`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.126
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.010553
  * `Imports (Out-Degree: 8):` cobj.h, config.h, ctype.h, limits.h, stdio.h, stdlib.h, string.h, tree.h
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `tests/cobol85/IX/IX215A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.174)
- **Top Global Matches:** file_cluster_7: 11.174, file_cluster_12: 12.215, file_cluster_14: 12.752
- **Magnitude:** 2541.46 | **LOC:** 2806 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (86.6%), Complexity Load (formerly Cognitive Load) (46.4%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `START-TEST-GF-27` **(I/O & Config Routines)** (Impact: 25.0)
  * `START-TEST-GF-09` **(I/O & Config Routines)** (Impact: 24.9)
  * `START-TEST-GF-18` **(I/O & Config Routines)** (Impact: 24.9)
  * `START-TEST-GF-06` **(I/O & Config Routines)** (Impact: 19.7)
  * `START-TEST-GF-25` **(I/O & Config Routines)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 379 instances
* *State Mutation (weighted view):* 1711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 460`, `structural_boundaries: 316`, `func_start: 217`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 254`, `high_risk_execution: 1`, `state_mutation: 953`, `dead_code: 1`, `fragile_debt: 6`, `unreferenced_by_name: 55`
* *Architecture:* `io: 394`
* *Defense:* `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC103A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.229)
- **Top Global Matches:** file_cluster_7: 7.229, file_cluster_12: 8.479, file_cluster_5: 10.066
- **Magnitude:** 2476.06 | **LOC:** 2140 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.1%), Complexity Load (formerly Cognitive Load) (41.9%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IF--TEST-GF-97` **(I/O & Config Routines)** (Impact: 7.6)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `IF--TEST-GF-87` **(I/O & Config Routines)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 1116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 789`, `structural_boundaries: 461`, `func_start: 448`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 163`, `high_risk_execution: 1`, `state_mutation: 556`, `dead_code: 1`, `fragile_debt: 6`, `unreferenced_by_name: 215`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC250A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.389)
- **Top Global Matches:** file_cluster_7: 7.389, file_cluster_12: 8.571, file_cluster_5: 10.117
- **Magnitude:** 2197.5 | **LOC:** 1972 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.5%), Complexity Load (formerly Cognitive Load) (43.8%), Dead Code Surface (formerly Dead Code) (5.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IF--TEST-71` **(I/O & Config Routines)** (Impact: 9.8)
  * `IF--TEST-120` **(Compute Cores)** (Impact: 9.8)
  * `IF--TEST-121` **(I/O & Config Routines)** (Impact: 9.8)
  * `IF--TEST-114` **(I/O & Config Routines)** (Impact: 6.5)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 250 instances
* *State Mutation (weighted view):* 841
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 851`, `structural_boundaries: 542`, `func_start: 409`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 147`, `high_risk_execution: 1`, `state_mutation: 341`, `dead_code: 1`, `fragile_debt: 28`, `unreferenced_by_name: 155`
* *Architecture:* `io: 3`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC106A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_7: 6.609, file_cluster_12: 7.913, file_cluster_5: 9.561
- **Magnitude:** 2188.0 | **LOC:** 2534 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.8%), Complexity Load (formerly Cognitive Load) (32.2%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `SUB-TEST-F1-20` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 297 instances
* *State Mutation (weighted view):* 1412
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 585`, `func_start: 349`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 1`, `state_mutation: 818`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 166`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC218A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.414)
- **Top Global Matches:** file_cluster_7: 7.414, file_cluster_14: 8.265, file_cluster_12: 10.415
- **Magnitude:** 2180.84 | **LOC:** 3078 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (83.9%), Complexity Load (formerly Cognitive Load) (43.1%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `FAIL-ROUTINE` **(I/O & Config Routines)** (Impact: 4.4)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 170 instances
* *State Mutation (weighted view):* 1118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 591`, `func_start: 597`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 420`, `high_risk_execution: 1`, `state_mutation: 778`, `dead_code: 1`, `fragile_debt: 8`, `unreferenced_by_name: 264`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobj/cobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.587)
- **Top Global Matches:** file_cluster_6: 8.587, file_cluster_4: 13.144, file_cluster_8: 15.549
- **Magnitude:** 2116.78 | **LOC:** 2507 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **26**; blast radius 2.42; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_command_line` **(Many-Argument Workhorses)** (Impact: 183.7)
  * `main` **(Many-Argument Workhorses)** (Impact: 155.3)
  * `process_filename` **(Compute Cores)** (Impact: 69.5)
  * `preprocess` **(Compute Cores)** (Impact: 53.9)
    * *Intent:* /* Preprocess source */
  * `utf8_national_length` **(Compute Cores)** (Impact: 40.3)
    * *Intent:* #endif /*I18N_UTF8*/ #ifdef I18N_UTF8
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 368 instances
* *High Risk Execution (weighted view):* 23
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 489`, `structural_boundaries: 209`, `args: 81`, `func_start: 45`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 85`, `high_risk_execution: 30`, `state_mutation: 389`
* *Architecture:* `io: 12`, `api: 24`, `import: 31`
* *Defense:* `safety: 28`, `immutability_locks: 62`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.42
  * `Choke Point (Betweenness):` 0.000164 | `Ripple Effect (Closeness):` 0.010553
  * `Imports (Out-Degree: 17):` cobj.h, config.h, defaults.h, errno.h, exception.def, flag-help.def, flag.def, getopt.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tests/cobol85/NC/NC105A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.918)
- **Top Global Matches:** file_cluster_7: 8.918, file_cluster_14: 10.397, file_cluster_12: 10.801
- **Magnitude:** 2106.56 | **LOC:** 3118 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (37.7%), Dead Code Surface (formerly Dead Code) (5.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MOVE-TEST-F1-33-1` **(I/O & Config Routines)** (Impact: 8.7)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `MOVE-TEST-F1-32-1` **(I/O & Config Routines)** (Impact: 5.9)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 952
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 603`, `func_start: 765`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 365`, `high_risk_execution: 1`, `state_mutation: 818`, `dead_code: 7`, `fragile_debt: 4`, `unreferenced_by_name: 513`
* *Architecture:* `io: 8`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC176A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.597)
- **Top Global Matches:** file_cluster_7: 6.597, file_cluster_12: 7.842, file_cluster_5: 9.537
- **Magnitude:** 2086.26 | **LOC:** 2418 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.5%), Complexity Load (formerly Cognitive Load) (32.2%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `ADD-TEST-F1-19` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 291 instances
* *State Mutation (weighted view):* 1336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 577`, `func_start: 330`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `high_risk_execution: 1`, `state_mutation: 754`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 162`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/IX/IX209A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.606)
- **Top Global Matches:** file_cluster_7: 6.606, file_cluster_12: 8.116, file_cluster_5: 9.69
- **Magnitude:** 2036.46 | **LOC:** 2860 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (85.5%), Complexity Load (formerly Cognitive Load) (32.7%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `START-TEST-GF-42` **(I/O & Config Routines)** (Impact: 7.9)
  * `START-TEST-GF-06` **(I/O & Config Routines)** (Impact: 7.7)
  * `START-TEST-GF-24` **(I/O & Config Routines)** (Impact: 7.7)
  * `START-TEST-GF-41` **(I/O & Config Routines)** (Impact: 7.6)
  * `START-TEST-GF-05` **(I/O & Config Routines)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 310 instances
* *State Mutation (weighted view):* 1379
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 319`, `func_start: 243`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 158`, `high_risk_execution: 1`, `state_mutation: 759`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 72`
* *Architecture:* `io: 132`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC124A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.574)
- **Top Global Matches:** file_cluster_12: 6.574, file_cluster_7: 7.309, file_cluster_11: 9.472
- **Magnitude:** 2012.56 | **LOC:** 2355 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.2%), Complexity Load (formerly Cognitive Load) (33.6%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PICTURE-TEST-26-C` **(I/O & Config Routines)** (Impact: 5.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 209 instances
* *State Mutation (weighted view):* 1178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 775`, `func_start: 311`
* *Risk/State:* `safety_bypasses: 83`, `high_risk_execution: 1`, `state_mutation: 760`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 220`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC177A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_7: 6.609, file_cluster_12: 7.494, file_cluster_5: 9.448
- **Magnitude:** 1986.8 | **LOC:** 2138 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (83.7%), Complexity Load (formerly Cognitive Load) (32.8%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `ADD-TEST-F2-34-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 298 instances
* *State Mutation (weighted view):* 1317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 508`, `func_start: 282`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 125`, `high_risk_execution: 1`, `state_mutation: 721`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 146`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolNationalField.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.842)
- **Top Global Matches:** file_cluster_4: 6.842, file_cluster_12: 9.358, file_cluster_16: 9.545
- **Magnitude:** 1975.74 | **LOC:** 1080 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 4.752; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Guard Balance (formerly Safety Score) (93.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `han2zen` **(Many-Argument Workhorses)** (Impact: 343.7)
    * *Intent:* /** * 半角文字のバイト列をシフトJISの全角文字のバイト列へ変換する. * * @param str 変換対象の半角文字のバイト列 * @param size 変換対象のバイト数 * @retu...
  * `cob_move_from_alphanum` **(Stateful Encapsulated Methods)** (Impact: 17.8)
    * *Intent:* /** * CobolAlphanumericFieldからthisへの代入を行う * * @param field 代入元のデータ(AbstractCobolField型) */
  * `moveFrom` **(Compute Cores)** (Impact: 16.2)
  * `judge_hankakujpn_exist` **(Compute Cores)** (Impact: 4.8)
    * *Intent:* /** * 転記元データが存在する場合に,全角へ変換したバイト列を返す. * * @param src 変換対象の英数字項目 * @return 全角へ変換したバイト列.変換対象が空または先頭バイトが...
  * `CobolNationalField` **(State Mutators)** (Impact: 2.2)
    * *Intent:* /** * コンストラクタ * * @param size データを格納するバイト配列の長さ * @param dataStorage データを格納するバイト配列を扱うオブジェクト * @param ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 508 instances
* *State Mutation (weighted view):* 1533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 197`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 517`, `planned_debt: 3`
* *Architecture:* `api: 19`, `import: 2`
* *Defense:* `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.752
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.030913
  * `Imports (Out-Degree: 6):` java.math.BigDecimal, jp.osscons.opensourcecobol.libcobj.exceptions.CobolRuntimeException
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/cobol85/SQ/SQ106A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.027)
- **Top Global Matches:** file_cluster_7: 7.027, file_cluster_14: 8.287, file_cluster_12: 9.85
- **Magnitude:** 1959.72 | **LOC:** 2661 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (86.9%), Complexity Load (formerly Cognitive Load) (32.4%), Dead Code Surface (formerly Dead Code) (5.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.8)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.8)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `FAIL-ROUTINE` **(I/O & Config Routines)** (Impact: 4.5)
  * `SEQ-TEST-RD-15-04` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 236 instances
* *State Mutation (weighted view):* 1210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 275`, `func_start: 336`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 273`, `high_risk_execution: 1`, `state_mutation: 738`, `dead_code: 6`, `fragile_debt: 3`, `unreferenced_by_name: 49`
* *Architecture:* `io: 77`
* *Defense:* `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC173A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.654)
- **Top Global Matches:** file_cluster_12: 6.654, file_cluster_7: 7.133, file_cluster_5: 9.482
- **Magnitude:** 1920.78 | **LOC:** 2219 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.5%), Complexity Load (formerly Cognitive Load) (33.0%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `DIV-TEST-F3-27-2` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 254 instances
* *State Mutation (weighted view):* 1264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 494`, `func_start: 248`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 1`, `state_mutation: 756`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 160`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/SG/SG101A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.705)
- **Top Global Matches:** file_cluster_7: 7.705, file_cluster_14: 9.785, file_cluster_12: 9.803
- **Magnitude:** 1881.46 | **LOC:** 2850 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (33.7%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `FAIL-ROUTINE` **(I/O & Config Routines)** (Impact: 4.3)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 4.2)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 846
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 900`, `func_start: 672`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 312`, `high_risk_execution: 1`, `state_mutation: 770`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 260`
* *Architecture:* `io: 3`
* *Defense:* `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC171A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.856)
- **Top Global Matches:** file_cluster_12: 6.856, file_cluster_7: 6.976, file_cluster_5: 9.455
- **Magnitude:** 1869.32 | **LOC:** 2269 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.4%), Complexity Load (formerly Cognitive Load) (33.0%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `DIV-TEST-F1-15-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 1184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 514`, `func_start: 266`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 1`, `state_mutation: 746`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 162`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC172A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.83)
- **Top Global Matches:** file_cluster_12: 6.83, file_cluster_7: 6.958, file_cluster_5: 9.443
- **Magnitude:** 1867.06 | **LOC:** 2216 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.2%), Complexity Load (formerly Cognitive Load) (32.9%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `DIV-TEST-F2-26-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 234 instances
* *State Mutation (weighted view):* 1210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 486`, `func_start: 255`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 92`, `high_risk_execution: 1`, `state_mutation: 742`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 154`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/common/CobolIntrinsic.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.2)
- **Top Global Matches:** file_cluster_12: 8.2, file_cluster_7: 9.203, file_cluster_5: 9.881
- **Magnitude:** 1850.52 | **LOC:** 3067 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 1.755; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (89.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `funcNumvalC` **(Many-Argument Workhorses)** (Impact: 44.8)
    * *Intent:* // libcob/intrinsicのcob_intr_numval_cの実装 /** * COBOLの組み込み関数FUNCTION NUMVAL-Cに対応する。<br> * 通貨記号やカンマを含む...
  * `funcLocaleDate` **(Many-Argument Workhorses)** (Impact: 41.9)
    * *Intent:* /** * COBOLの組み込み関数FUNCTION LOCALE-DATEに対応する。<br> * 「YYYYMMDD」形式の日付を、指定されたロケール(省略時は既定のロケール)の書式に従って整形し...
  * `funcLocaleTime` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* /** * COBOLの組み込み関数FUNCTION LOCALE-TIMEに対応する。<br> * 「hhmmss」形式の時刻を、指定されたロケール(省略時は既定のロケール)の書式に従って整形した ...
  * `funcNumval` **(Compute Cores)** (Impact: 28.0)
    * *Intent:* // libcob/intrinsicのcob_intr_numvalの実装 /** * COBOLの組み込み関数FUNCTION NUMVALに対応する。<br> * 数字を表す文字列(符号、小数点...
  * `funcSubstituteCase` **(Many-Argument Workhorses)** (Impact: 27.3)
    * *Intent:* /** * COBOLの組み込み関数FUNCTION SUBSTITUTE-CASEに対応する。<br> * 先頭の引数を対象文字列とし、続く引数を(検索文字列, 置換文字列)の組として、 * 対象文...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 326 instances
* *State Mutation (weighted view):* 1021
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 332`, `args: 85`, `func_start: 84`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 128`, `state_mutation: 369`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 59`
* *Architecture:* `api: 74`, `import: 19`
* *Defense:* `safety: 32`, `doc: 98`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.755
  * `Choke Point (Betweenness):` 5.5e-05 | `Ripple Effect (Closeness):` 0.023769
  * `Imports (Out-Degree: 12):` java.math.BigDecimal, java.text.DateFormat, java.time.LocalDateTime, java.time.LocalTime, java.time.format.DateTimeFormatter, java.util.Arrays, java.util.Calendar, java.util.Locale...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/cobol85/NC/NC101A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.698)
- **Top Global Matches:** file_cluster_7: 6.698, file_cluster_12: 7.234, file_cluster_5: 9.431
- **Magnitude:** 1839.64 | **LOC:** 1868 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.6%), Complexity Load (formerly Cognitive Load) (34.1%), Dead Code Surface (formerly Dead Code) (5.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `MPY-TEST-F1-14-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 283 instances
* *State Mutation (weighted view):* 1225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 448`, `func_start: 245`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 1`, `state_mutation: 659`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 143`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC175A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.576)
- **Top Global Matches:** file_cluster_7: 6.576, file_cluster_12: 7.559, file_cluster_5: 9.455
- **Magnitude:** 1819.62 | **LOC:** 2080 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.6%), Complexity Load (formerly Cognitive Load) (32.4%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `SUB-TEST-F2-34-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 1194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 462`, `func_start: 267`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 126`, `high_risk_execution: 1`, `state_mutation: 682`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 128`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cobol85/NC/NC170A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.871)
- **Top Global Matches:** file_cluster_7: 6.871, file_cluster_12: 7.05, file_cluster_5: 9.446
- **Magnitude:** 1773.12 | **LOC:** 2016 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (81.5%), Complexity Load (formerly Cognitive Load) (33.1%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `END-ROUTINE-13` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `MPY-TEST-F2-17-2` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 230 instances
* *State Mutation (weighted view):* 1147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 464`, `func_start: 263`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 1`, `state_mutation: 687`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 160`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.747
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/cobol85/CM/CM401M.CBL` (COBOL) | Magnitude: 9.6 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 9, func_start: 8, unreferenced_by_name: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/cobol85/IC/IC106A.CBL` (COBOL) | Magnitude: 406.94 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 482, state_mutation: 150, structural_boundaries: 88, func_start: 79
- `tests/cobol85/NC/NC138A.CBL` (COBOL) | Magnitude: 461.2 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 585, state_mutation: 181, structural_boundaries: 116, func_start: 103
- `tests/cobol85/NC/NC136A.CBL` (COBOL) | Magnitude: 368.62 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 431, state_mutation: 128, structural_boundaries: 72, func_start: 49
- `tests/cobol85/OB/lib/OBIC2A.CBL` (COBOL) | Magnitude: 171.94 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 242, state_mutation: 71, structural_boundaries: 31, func_start: 23
- `tests/cobol85/NC/NC113M.CBL` (COBOL) | Magnitude: 113.98 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 239, state_mutation: 56, structural_boundaries: 38, func_start: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `.github/workflows/db-settings/embed_db_info_postgresql_15.sh` (SHELL) | Magnitude: 8.56 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 27, structural_boundaries: 16, state_mutation: 6, core_var_decl: 6
- `.github/workflows/db-settings/embed_db_info_postgresql_9.6.sh` (SHELL) | Magnitude: 8.56 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 27, structural_boundaries: 16, state_mutation: 6, core_var_decl: 6
- `tests/embed_db_info.sh` (SHELL) | Magnitude: 8.36 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 27, structural_boundaries: 16, state_mutation: 6, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/file/CobolSequentialFile.java` (JAVA) | Magnitude: 68.7 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 39, planned_debt: 27, branch: 16
- `cobj/ppparse.y` (YACC) | Magnitude: 368.44 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 104, args: 103, state_mutation: 76, indent_spaces: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/misc.at` (M4) | Magnitude: 15.86 | Delta: **0.198** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 42, test: 1
- `tests/command-line-options.at` (M4) | Magnitude: 15.74 | Delta: **0.2** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 36, test: 1
- `tests/jp-compat.at` (M4) | Magnitude: 15.6 | Delta: **0.23** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 29, test: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/syntax.at` (M4) | Magnitude: 15.34 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 16, test: 1
- `.github/workflows/pull-request.yml` (YAML) | Magnitude: 30.96 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 193, structural_boundaries: 48, args: 25, import: 23
- `.github/workflows/push.yml` (YAML) | Magnitude: 28.98 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 48, args: 25, import: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/file/IndexedCursor.java` (JAVA) | Magnitude: 330.92 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 482, branch: 86, core_var_decl: 77, state_mutation: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/user_util/indexed_file/RecordReader.java` (JAVA) | Magnitude: 18.96 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 13, branch: 6, doc: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/cobol85/CM/CM101M.CBL` (COBOL) | Magnitude: 328.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 667, state_mutation: 167, structural_boundaries: 94, func_start: 65
- `tests/cobol85/CM/CM202M.CBL` (COBOL) | Magnitude: 313.6 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 640, state_mutation: 166, structural_boundaries: 87, func_start: 64
- `libcobj/app/src/test/java/jp/osscons/opensourcecobol/libcobj/sql/CobolEsqlBackendFactoryTest.java` (JAVA) | Magnitude: 6.82 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 15, test: 10, args: 6
- `tests/cobol85/NC/NC302M.CBL` (COBOL) | Magnitude: 6.08 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 8, func_start: 5, high_risk_execution: 2
- `tests/cobol85/RW/RW101A.CBL` (COBOL) | Magnitude: 320.14 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 437, state_mutation: 115, structural_boundaries: 71, func_start: 67

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `cobj/codegen.c` -> Churn: **85.84%** | Cog Load: 72.0128% | Debt: 9.1813%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cobj/cobj.c` -> **yutaro-sakamoto** (83.3% isolated ownership) | Magnitude: 2116.78
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolNationalField.java` -> **Takuto Hashimoto** (100.0% isolated ownership) | Magnitude: 1975.74
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/common/CobolIntrinsic.java` -> **Takuto Hashimoto** (100.0% isolated ownership) | Magnitude: 1850.52
- `cobj/field.c` -> **yutaro-sakamoto** (100.0% isolated ownership) | Magnitude: 1264.76
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolDataStorage.java` -> **Takuto Hashimoto** (100.0% isolated ownership) | Magnitude: 1104.42

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/AbstractCobolField.java` -> **Severity: 0.149** (Bridge: 0.0015 * Flux: 100.0%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/common/CobolModule.java` -> **Severity: 0.049** (Bridge: 0.0005 * Flux: 100.0%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/common/CobolUtil.java` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 100.0%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolDataStorage.java` -> **Severity: 0.041** (Bridge: 0.0004 * Flux: 99.4788%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/exceptions/CobolRuntimeException.java` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 95.6223%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolDataStorage.java` -> **Severity: 3.344** (Embedded: 0.0602 * Error Risk: 55.5693%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/AbstractCobolField.java` -> **Severity: 3.334** (Embedded: 0.0488 * Error Risk: 68.3604%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolNationalField.java` -> **Severity: 2.879** (Embedded: 0.0309 * Error Risk: 93.1381%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/common/CobolModule.java` -> **Severity: 2.564** (Embedded: 0.0398 * Error Risk: 64.3515%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/common/CobolUtil.java` -> **Severity: 2.499** (Embedded: 0.0341 * Error Risk: 73.3354%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolNumericField.java` -> **Severity: 418.986** (Blast Radius: 5.554 * Doc Risk: 75.4386%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolNationalField.java` -> **Severity: 380.16** (Blast Radius: 4.752 * Doc Risk: 80.0%)
- `libcobj/app/src/main/java/jp/osscons/opensourcecobol/libcobj/data/CobolAlphanumericField.java` -> **Severity: 297.0** (Blast Radius: 3.96 * Doc Risk: 75.0%)
- `cobj/cobj.c` -> **Severity: 242.0** (Blast Radius: 2.42 * Doc Risk: 100.0%)
- `tests/cobol85/IC/lib/IC111A.CBL` -> **Severity: 238.2** (Blast Radius: 2.382 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `412` files carry mainframe facts -- `230` call sites, `662` dataset bindings, `63319` record items.

- **DB2 table access:** `61` embedded SQL statements touching `4` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

### `tests/cobol85/NC/NC106A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (308 items):** `42-DATANAMES (43)`, `TEST-CORRECT (14)`, `MINUS-NAMES (13)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `SUBTRACT-DATA (11)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)` … (+140 more)
- **Data moves:** 1507 (ADD 70, MOVE 755, SUBTRACT 682); most-fed items `COMPUTED-N`, `DNAME22`, `COMPUTED-18V0`, `COMPUTED-X`, `DUMMY-RECORD`, `DNAME23`

### `tests/cobol85/NC/NC176A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (282 items):** `42-DATANAMES (43)`, `TEST-CORRECT (14)`, `MINUS-NAMES (13)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `SUBTRACT-DATA (11)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)` … (+114 more)
- **Data moves:** 1412 (ADD 705, MOVE 707); most-fed items `COMPUTED-N`, `DNAME22`, `COMPUTED-18V0`, `COMPUTED-X`, `DUMMY-RECORD`, `DNAME23`

### `tests/cobol85/IX/IX215A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`, `XXXXX024(I-O/INPUT/OUTPUT)`, `XXXXX025(I-O/INPUT/OUTPUT)`, `XXXXX026(I-O/INPUT/OUTPUT)`
- **Record layouts (390 items):** `RECORD-KEY-CONTENT (76)`, `IX-FD1R1-F-G-240⟵IX-FD1 (49)`, `IX-FD2R1-F-G-241⟵IX-FD2 (49)`, `FILE-RECORD-INFORMATION-REC (45)`, `IX-FD3R1-F-G-242⟵IX-FD3 (17)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `WRK-FDW-ALTKEY1 (8)`, `WRK-FDW-ALTKEY2 (8)`, `XXINFO (8)`, `CCVS-H-2B (7)` … (+36 more)
- **Keyed files:** `IX-FD1 INDEXED/DYNAMIC key IX-FD1-KEY`, `IX-FD2 INDEXED/DYNAMIC key IX-FD2-KEY`, `IX-FD3 INDEXED/DYNAMIC key IX-FD3-KEY`
- **Data moves:** 959 (ADD 47, MOVE 900, READ 3, SUBTRACT 9); most-fed items `COMPUTED-18V0`, `FILE-RECORD-INFO`, `COMPUTED-A`, `DUMMY-RECORD`, `IX-REC-KEY-AREA`, `WRK-FDW-ALTKEY2`

### `tests/cobol85/NC/NC175A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (259 items):** `TEST-CORRECT (14)`, `MINUS-NAMES (13)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `SUBTRACT-DATA (11)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)`, `CCVS-E-1 (5)` … (+133 more)
- **Data moves:** 921 (ADD 59, MOVE 583, SUBTRACT 279); most-fed items `COMPUTED-N`, `COMPUTED-X`, `DUMMY-RECORD`, `WRK-DS-2V1-1`, `WRK-DS-2V2-2`, `WRK-NE-4`

### `tests/cobol85/NC/NC177A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (238 items):** `TEST-CORRECT (14)`, `MINUS-NAMES (13)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `SUBTRACT-DATA (11)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)`, `CCVS-E-1 (5)` … (+112 more)
- **Data moves:** 930 (ADD 321, MOVE 609); most-fed items `COMPUTED-N`, `COMPUTED-X`, `DUMMY-RECORD`, `WRK-DS-06V06`, `WRK-DU-2V0-1`, `WRK-DU-2V0-2`

### `tests/cobol85/NC/NC124A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (187 items):** `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)`, `CCVS-E-1 (5)`, `CCVS-E-4 (5)`, `CCVS-H-1 (4)` … (+86 more)
- **Data moves:** 895 (ADD 144, MOVE 751); most-fed items `COMPUTED-A`, `DUMMY-RECORD`, `EDIT-AREA-1`, `EDIT-AREA-2`, `EDIT-AREA-3`, `EDIT-AREA-4`

### `tests/cobol85/NC/NC173A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (223 items):** `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `DIVIDE-DATA (9)`, `XXINFO (8)`, `MULTIPLY-DATA (7)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)`, `CCVS-E-1 (5)` … (+105 more)
- **Data moves:** 856 (ADD 79, DIVIDE 132, MOVE 645); most-fed items `COMPUTED-N`, `DUMMY-RECORD`, `COMPUTED-X`, `WRK-DS-09V09`, `WRK-DU-2V0-1`, `WRK-DU-2V0-2`

### `tests/cobol85/NC/NC105A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (276 items):** `GRP-MOVE-RECEIVING-FIELDS (16)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `MOVE42 (10)`, `GRP-MOVE-CONSTANTS (9)`, `GRP-RECEIVING (9)`, `XXINFO (8)`, `SEND-BREAKDOWN (7)`, `RECEIVE-BREAKDOWN (7)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)` … (+97 more)
- **Data moves:** 801 (ADD 9, MOVE 788, SUBTRACT 4); most-fed items `COMPUTED-A`, `DUMMY-RECORD`, `RECEIVE-BREAKDOWN`, `COMPUTED-N`, `CORRECT-A`, `COMPUTED-18V0`

### `tests/cobol85/IX/IX209A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`, `XXXXX024(INPUT/OUTPUT)`
- **Record layouts (307 items):** `RECORD-KEY-CONTENT (76)`, `FILE-RECORD-INFORMATION-REC (45)`, `IX-FS1R1-F-G-240⟵IX-FS1 (30)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `WRK-FS1-ALTKEY1 (8)`, `WRK-FS1-ALTKEY2 (8)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)` … (+35 more)
- **Keyed files:** `IX-FS1 INDEXED/SEQUENTIAL key IX-FS1-KEY`
- **Data moves:** 761 (ADD 22, MOVE 735, READ 1, SUBTRACT 3); most-fed items `FILESTATUS`, `COMPUTED-A`, `FILE-RECORD-INFO`, `IX-ALT-KEY1-AREA`, `IX-ALT-KEY2-AREA`, `IX-REC-KEY-AREA`

### `tests/cobol85/NC/NC172A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (223 items):** `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `DIVIDE-DATA (9)`, `XXINFO (8)`, `MULTIPLY-DATA (7)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)`, `CCVS-E-1 (5)` … (+105 more)
- **Data moves:** 840 (ADD 74, DIVIDE 130, MOVE 636); most-fed items `COMPUTED-N`, `DUMMY-RECORD`, `COMPUTED-X`, `WRK-DS-09V09`, `WRK-DU-2V0-1`, `WRK-DU-2V0-2`

### `tests/cobol85/NC/NC207A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (385 items):** `SECOND-GROUP (54)`, `FIRST-GROUP (53)`, `TABLE-LEVEL-5A (47)`, `TABLE-LEVEL-5B (47)`, `TABLE-LEVEL-5C (47)`, `TABLE-5B-INIT (17)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)` … (+25 more)
- **Data moves:** 672 (ADD 34, DIVIDE 34, MOVE 536, MULTIPLY 34, SUBTRACT 34); most-fed items `COMPUTED-N`, `ACCUMULATOR2`, `ACCUMULATOR1`, `DUMMY-RECORD`, `ERROR-HOLD`, `ERROR-TOTAL`

### `tests/cobol85/NC/NC171A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (223 items):** `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `DIVIDE-DATA (9)`, `XXINFO (8)`, `MULTIPLY-DATA (7)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)`, `CCVS-E-1 (5)` … (+105 more)
- **Data moves:** 788 (ADD 80, DIVIDE 72, MOVE 636); most-fed items `COMPUTED-N`, `DUMMY-RECORD`, `COMPUTED-18V0`, `COMPUTED-X`, `WRK-DS-09V09`, `WRK-DU-1V3-2`

### `tests/cobol85/NC/NC201A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (409 items):** `GRP-FOR-2N058 (34)`, `IF-D35 (14)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `CHARACTER-BREAKDOWN-S (11)`, `CHARACTER-BREAKDOWN-R (11)`, `GRP-MOVE-CONSTANTS (10)`, `PERFORM-SEVEN-LEVEL-TABLE (9)`, `TABLE-86 (9)`, `IF-D32 (8)`, `FIGCON-DATA (8)` … (+147 more)
- **Data moves:** 594 (ADD 80, DIVIDE 4, INITIALIZE 1, MOVE 488, MULTIPLY 14, SUBTRACT 7); most-fed items `COMPUTED-N`, `COMPUTED-A`, `DUMMY-RECORD`, `COMPUTED-18V0`, `ERROR-HOLD`, `PERFORM14`

### `tests/cobol85/NC/NC170A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (223 items):** `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `DIVIDE-DATA (9)`, `XXINFO (8)`, `MULTIPLY-DATA (7)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)`, `CCVS-E-1 (5)` … (+105 more)
- **Data moves:** 774 (ADD 67, MOVE 587, MULTIPLY 120); most-fed items `COMPUTED-N`, `DUMMY-RECORD`, `COMPUTED-A`, `COMPUTED-X`, `WRK-DS-10V00`, `COMPUTED-18V0`

### `tests/cobol85/NC/NC126A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (340 items):** `TEST-GROUP-1 (96)`, `TABLE-GROUP (96)`, `BREAKDOWN-RECORD (24)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `LITERAL-98 (6)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)` … (+21 more)
- **Data moves:** 656 (ADD 9, MOVE 647); most-fed items `COMPUTED-A`, `COMPUTED-BREAKDOWN`, `DUMMY-RECORD`, `CORRECT-A`, `ERROR-HOLD`, `ERROR-TOTAL`

### `tests/cobol85/NC/NC218A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (164 items):** `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)`, `GRP4-XN-10 (5)`, `CCVS-E-1 (5)`, `CCVS-E-4 (5)` … (+54 more)
- **Data moves:** 797 (ADD 108, MOVE 640, UNSTRING 49); most-fed items `COMPUTED-N`, `COMPUTED-A`, `DUMMY-RECORD`, `ID4A-XXXXX`, `ID4B-X`, `ID4-X`

### `tests/cobol85/NC/NC104A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (227 items):** `42-DATANAMES (43)`, `AN-DATANAMES (22)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `MOVE47A (6)`, `CCVS-C-2 (6)`, `CCVS-H-2A (6)`, `CCVS-E-3 (6)` … (+56 more)
- **Data moves:** 729 (ADD 10, MOVE 719); most-fed items `COMPUTED-A`, `COMPUTED-18V0`, `DUMMY-RECORD`, `COMPUTED-N`, `MOVE20`, `MOVE21`

### `tests/cobol85/SQ/SQ106A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`, `XXXXX001(INPUT/OUTPUT)`
- **Record layouts (200 items):** `FILE-RECORD-INFORMATION-REC (45)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `CCVS-C-1 (9)`, `SQ-VS6R2-M-G-151⟵SQ-VS6 (8)`, `BUFFER-COPY (8)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `DELETE-SW (6)`, `CCVS-C-2 (6)` … (+27 more)
- **Data moves:** 744 (ADD 100, MOVE 638, WRITE 6); most-fed items `COMPUTED-A`, `DUMMY-RECORD`, `CORRECT-A`, `FILE-RECORD-INFO-P1-120`, `BUFFER-COPY-120`, `SQ-VS6R2-FIRST`

### `tests/cobol85/NC/NC202A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`
- **Record layouts (344 items):** `42-DATANAMES (43)`, `SUBTRACT-DATA (20)`, `GRP-FOR-ADD-CORR-2 (14)`, `TEST-CORRECT (14)`, `GRP-FOR-ADD-CORR-1 (13)`, `TEST-COMPUTED (13)`, `GRP-FOR-ADD-CORR-R (12)`, `TEST-RESULTS (12)`, `CORR-DATA-5 (8)`, `XXINFO (8)`, `GRP-FOR-ADD-CORR-A (7)`, `CORR-DATA-1 (7)` … (+87 more)
- **Data moves:** 590 (ADD 54, MOVE 536); most-fed items `COMPUTED-N`, `DUMMY-RECORD`, `COMPUTED-A`, `CORRECT-X`, `ERROR-HOLD`, `ERROR-TOTAL`

### `tests/cobol85/IX/IX210A.CBL` (COBOL)
- **Datasets:** `REPORT.LOG(OUTPUT)`, `XXXXX024(I-O/INPUT/OUTPUT)`
- **Record layouts (314 items):** `RECORD-KEY-CONTENT (76)`, `FILE-RECORD-INFORMATION-REC (45)`, `IX-FS1R1-F-G-240⟵IX-FS1 (37)`, `TEST-CORRECT (14)`, `TEST-COMPUTED (13)`, `TEST-RESULTS (12)`, `WRK-FS1-ALTKEY1 (8)`, `WRK-FS1-ALTKEY2 (8)`, `XXINFO (8)`, `CCVS-H-2B (7)`, `CCVS-E-2 (7)`, `CCVS-C-2 (6)` … (+35 more)
- **Keyed files:** `IX-FS1 INDEXED/SEQUENTIAL key IX-FS1-KEY`
- **Data moves:** 616 (ADD 26, MOVE 586, READ 1, SUBTRACT 3); most-fed items `FILESTATUS`, `COMPUTED-A`, `DUMMY-RECORD`, `FILE-RECORD-INFO`, `IX-REC-KEY-AREA`, `IX-ALT-KEY1-AREA`

*(+392 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 38% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (384 gaps); application programs (source or load-module list) (112 gaps); copybook libraries (9 gaps).

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 833 literal sites + 16 sites through wrappers = 849
- **`memory_alloc`:** 93 literal sites + 1693 sites through wrappers = 1786
- **`panics_and_aborts`:** 796 literal sites + 5 sites through wrappers = 801

- `CB_VALUE` (macro, memory_alloc, via CB_LIST): 269 call sites in 5 files -- `cobj/tree.h`
- `CB_CHAIN` (macro, memory_alloc, via CB_LIST): 154 call sites in 5 files -- `cobj/tree.h`
- `cb_field` (function, memory_alloc, via CB_FIELD): 143 call sites in 5 files -- `cobj/tree.c`
- `CB_FIELD` (macro, memory_alloc, via CB_TREE_CAST): 120 call sites in 6 files -- `cobj/tree.h`
- `CB_LITERAL` (macro, memory_alloc, via CB_TREE_CAST): 91 call sites in 4 files -- `cobj/tree.h`
- `CB_REFERENCE` (macro, memory_alloc, via CB_TREE_CAST): 86 call sites in 6 files -- `cobj/tree.h`
- `CB_PAIR_Y` (macro, memory_alloc, via CB_VALUE): 73 call sites in 3 files -- `cobj/tree.h`
- `CB_PAIR_X` (macro, memory_alloc, via CB_PURPOSE): 69 call sites in 3 files -- `cobj/tree.h`
- `CB_FILE` (macro, memory_alloc, via CB_TREE_CAST): 65 call sites in 3 files -- `cobj/tree.h`
- `cobc_malloc` (function, memory_alloc, primitive): 55 call sites in 7 files -- `cobj/cobj.c`
- `make_tree` (function, memory_alloc, via cobc_malloc): 42 call sites in 2 files -- `cobj/tree.c`
- `CB_FUNCALL` (macro, memory_alloc, via CB_TREE_CAST): 41 call sites in 3 files -- `cobj/tree.h`
*(+97 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 47255 call pairs -- scoped 84.9%, unique 2.8%, ambiguous 2.3%, external 10.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 35804 | 99.7% | 0.1% | 0.0% | 0.2% |
| java | 6746 | 52.4% | 1.5% | 16.2% | 29.9% |
| c | 3312 | 25.8% | 22.9% | 0.0% | 51.3% |
| yacc | 919 | 0.2% | 45.5% | 0.0% | 54.3% |
| livecode | 198 | 0.0% | 0.0% | 0.0% | 100.0% |
| m4 | 174 | 14.9% | 0.0% | 0.0% | 85.1% |
| shell | 102 | 12.7% | 0.0% | 0.0% | 87.3% |

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
