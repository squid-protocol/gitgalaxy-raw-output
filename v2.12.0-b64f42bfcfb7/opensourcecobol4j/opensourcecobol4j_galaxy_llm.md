# ARCHITECTURAL_BRIEF: opensourcecobol4j
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
- **Scope:** 19275 analyzed artifact(s), 1417360 LOC.
- **Load-bearing artifact:** `_scan/i18n_utf8_gitgalaxy_java_spring_20260928_094925/ai_agent_jobs/126-zenkaku-spc-delims-in-record-def__prog_port_ticket.md` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `_scan2/cobol_utf8_gitgalaxy_java_spring_20260929_104118/migration_worklist.md` -- pulls in 128 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `_oracle/classify.py` at magnitude 736.76 (structural weight, not risk).
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
| Total Artifacts | 26864 |
| Analyzed Artifacts (Scanned) | 19275 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7589 |
| Total LOC | 1417360 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.8% |
| Dominant Lang | JSON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9698 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 8171 | 1348956 | 42.4% |
| COBOL | 2613 | 32374 | 13.6% |
| JAVA | 2109 | 27577 | 10.9% |
| MARKDOWN | 2094 | 0 | 10.9% |
| PLAINTEXT | 1998 | 0 | 10.4% |
| SHELL | 1308 | 4224 | 6.8% |
| POSTGRESQL | 654 | 1962 | 3.4% |
| SQLITE | 195 | 585 | 1.0% |
| C | 90 | 270 | 0.5% |
| XML | 17 | 0 | 0.1% |
| YAML | 17 | 391 | 0.1% |
| PYTHON | 7 | 1017 | 0.0% |
| DOCKERFILE | 2 | 4 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 585 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 18690 |
| cp1252 | cp1252-fallback | 298 |
| latin-1 | latin-1-fallback | 287 |

> 76 guessed file(s) read as double-byte text that decodes strictly as shift_jis / gbk: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `_oracle/work/results/i18n_sjis/004-field-lookup/1.err`, `_scan/i18n_sjis/002-field-name/prog.cob`, `_scan/i18n_sjis/004-field-lookup/prog.cob`, `_scan/i18n_sjis/012-nihongo-field-name-in-numeric-test-msg/prog.cob`, `_scan/i18n_sjis/013-nihongo-field-name-in-based-test-msg/prog.cob` and 71 more.

> 4 guessed file(s) read as double-byte text that decodes strictly as gbk: if that is the estate's code page, rescan with `--source-encoding gbk` (or the right one of those). E.g. `_oracle/work/results/cobol_utf8/012-nihongo-field-name-in-odo-test-msg/4.out`, `_oracle/work/results/cobol_utf8/013-nihongo-field-name-in-subscript-test-msg/4.out`, `_oracle/work/results/cobol_utf8/039-string-by-size/4.out`, `_oracle/work/results/cobol_utf8/062-pic-n-string-by-size/4.out`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 77%, Interface Declarations Files 19%, Large Core Modules 2%, Declarative / Non-Code 1%, Large Core Modules (2) 0%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 15183 | 78.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4092 | 21.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7589*

**Composition by Extension & Reason:**
- `.lst`: 2074x Excluded (Unsupported Extension: '.lst')
- `.jcl`: 1852x Excluded (Machine-Generated Source Code Signature: 13 LOC), 89x Excluded (Machine-Generated Source Code Signature: 17 LOC), 61x Excluded (Machine-Generated Source Code Signature: 19 LOC)
- `.java`: 838x Statistical Anomaly (Z-Score: -24867.93 < -4.55), 347x Statistical Anomaly (Z-Score: -29528.11 < -4.55), 132x Statistical Anomaly (Z-Score: -33189.68 < -4.55)
- `.rc`: 957x Excluded (Unsupported Extension: '.rc')
- `.sql`: 323x Statistical Anomaly (Z-Score: -5620.83 < -4.75), 126x Statistical Anomaly (Z-Score: -8993.33 < -4.75), 69x Statistical Anomaly (Z-Score: -11241.67 < -4.75)
- `.json`: 5x Excluded (Static Asset Blob without Intent: 1108 LOC), 5x Excluded (Static Asset Blob without Intent: 1119 LOC), 5x Excluded (Static Asset Blob without Intent: 2044 LOC)
- `.cpy`: 35x Statistical Anomaly (Z-Score: -6.07 < -4.55)
- `.conf`: 30x Excluded (Unsupported Extension: '.conf')
- `no_extension`: 24x Unsupported Format (.undeterminable)
- `.javastep`: 22x Excluded (Unsupported Extension: '.javastep')
- `.db`: 17x Excluded (Unsupported Extension: '.db')
- `.out`: 5x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Binary Format Detected)
- `.testsuite`: 4x Excluded (Unsupported Extension: '.testsuite')
- `.err`: 4x Excluded: Neighborhood Micro-Mass Limit Exceeded

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 88.2 | 0.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.0 | 8.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 36.7 | 1.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 64 | 43 | 0 | `_oracle/classify.py` |
| cleanup | 412 | 273 | 0 | `_scan/cobol_utf8/009-nihongo-filename/prog.cob` |
| guards | 4260 | 2105 | 2 | `_scan/cobol_utf8/125-type-mismatch/a.java` |
| danger | 4584 | 2361 | 1 | `_oracle/classify.py` |
| concurrency | 797 | 386 | 0 | `_oracle/work/cases/jp-compat/068-joining-in-recursive-copy.sh` |
| connectivity | 7133 | 2573 | 3 | `_oracle/classify.py` |
| io | 4314 | 839 | 0 | `_oracle/work/cases/cobol_utf8/115-japanese-word-section-variable.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 124 | 55 | 0 | `_oracle/work/cases/cobol_utf8/106-nc-literal-no-zenakaku-conversion.sh` |
| time | 227 | 68 | 0 | `_oracle/work/cases/jp-compat/086-cob-date-func-current-date-of-time.sh` |
| serialization | 115 | 115 | 0 | `_scan/cobol_utf8/039-string-by-size/prog.cob` |
| regex | 359 | 196 | 0 | `_oracle/classify.py` |
| events | 2106 | 2053 | 1 | `_oracle/work/cases/jp-compat/064-userfh-read-lock-so.sh` |
| tests | 90 | 54 | 0 | `_scan/jp-compat/069-joined-in-redefines-clause/copy.inc` |
| docs | 30 | 24 | 0 | `_oracle/classify.py` |
| debt | 8290 | 4481 | 2 | `_oracle/work/cases/jp-compat/064-userfh-read-lock-so.sh` |
| mutation | 8518 | 5795 | 1 | `_oracle/classify.py` |
| dead_code | 2044 | 1987 | 1 | `_scan/cobol_utf8/115-japanese-word-section-variable/prog.cbl` |
| credential | 134 | 124 | 0 | `_scan/scan_findings.json` |
| threat | 1493 | 975 | 0 | `_scan2/cobol_utf8_gitgalaxy_clean_20260929_104118/06_skeleton/009-nihongo-filename__prog_skeleton.json` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `_oracle/work/cases/cobol_utf8/115-japanese-word-section-variable.sh` (Hits: 46)
- `_oracle/work/cases/cobol_utf8/106-nc-literal-no-zenakaku-conversion.sh` (Hits: 32)
- `_oracle/work/cases/i18n_sjis/010-nihongo-field-name-with-sjis-hyphens.sh` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **126-zenkaku-spc-delims-in-record-def__prog_port_ticket.md** (`_scan/i18n_utf8_gitgalaxy_java_spring_20260928_094925/ai_agent_jobs/126-zenkaku-spc-delims-in-record-def__prog_port_ticket.md`) — 2 inbound connections
2. **inc.cpy** (`_scan/cobol_utf8/111-zenkaku-spc-delims-in-copy-stmt/inc.cpy`) — 1 inbound connections
3. **inc.cpy** (`_scan/i18n_utf8/127-zenkaku-spc-delims-in-copy-stmt/inc.cpy`) — 1 inbound connections
4. **inc2.cpy** (`_scan/jp-compat/092-cobol68-copy-nested-w-normal/inc2.cpy`) — 1 inbound connections
5. **inc2.cpy** (`_scan/jp-compat/093-cobol68-copy-nested-w-normal-2/inc2.cpy`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **migration_worklist.md** (`_scan2/cobol_utf8_gitgalaxy_java_spring_20260929_104118/migration_worklist.md`) — 128 outbound dependencies
2. **migration_worklist.md** (`_scan3/cobol_utf8_gitgalaxy_java_spring_20260929_130951/migration_worklist.md`) — 128 outbound dependencies
3. **migration_worklist.md** (`_scan_3991/cobol_utf8_gitgalaxy_java_spring_20260929_120516/migration_worklist.md`) — 128 outbound dependencies
4. **port_order.md** (`_scan2/cobol_utf8_gitgalaxy_java_spring_20260929_104118/ai_agent_jobs/port_order.md`) — 127 outbound dependencies
5. **port_order.md** (`_scan3/cobol_utf8_gitgalaxy_java_spring_20260929_130951/ai_agent_jobs/port_order.md`) — 127 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `classify_static` **(Many-Argument Workhorses)** (@ `_oracle/classify.py`) -> Impact: **141.6** | LOC: 71
  * *Intent:* """(out-of-scope reasons, notes). No reasons -> a runtime candidate."""
- `write_md` **(Compute Cores)** (@ `_oracle/classify.py`) -> Impact: **62.3** | LOC: 68
- `main` **(Compute Cores)** (@ `_scan/analyze.py`) -> Impact: **50.0** | LOC: 81
- `main` **(Compute Cores)** (@ `_scan2/analyze.py`) -> Impact: **50.0** | LOC: 81
- `main` **(Compute Cores)** (@ `_scan3/analyze.py`) -> Impact: **50.0** | LOC: 81
- `main` **(Compute Cores)** (@ `_scan_3991/analyze.py`) -> Impact: **50.0** | LOC: 81
- `main` **(Compute Cores)** (@ `_scan_3992/analyze.py`) -> Impact: **50.0** | LOC: 81
- `main` **(Compute Cores)** (@ `_oracle/validate_extract.py`) -> Impact: **48.1** | LOC: 63
- `main` **(I/O & Config Routines)** (@ `_oracle/classify.py`) -> Impact: **44.2** | LOC: 65
- `mismatch_cause` **(Compute Cores)** (@ `_oracle/classify.py`) -> Impact: **30.5** | LOC: 21
  * *Intent:* """A reading of GnuCOBOL's first disagreement with opensourcecobol4j's expected output."""

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `_scan/jp-compat_gitgalaxy_clean_20260928_094930/06_skeleton` | 124 | 2964.94 | 0.0% | 0.0% |
| `_scan2/jp-compat_gitgalaxy_clean_20260929_104212/06_skeleton` | 124 | 2964.94 | 0.0% | 0.0% |
| `_scan3/jp-compat_gitgalaxy_clean_20260929_131048/06_skeleton` | 124 | 2964.94 | 0.0% | 0.0% |
| `_scan_3991/jp-compat_gitgalaxy_clean_20260929_120621/06_skeleton` | 124 | 2964.94 | 0.0% | 0.0% |
| `_scan_3992/jp-compat_gitgalaxy_clean_20260929_115604/06_skeleton` | 124 | 2964.94 | 0.0% | 0.0% |
| `_scan3/cobol_utf8_gitgalaxy_clean_20260929_130951/06_skeleton` | 128 | 2878.22 | 0.0% | 0.0% |
| `_scan_3991/cobol_utf8_gitgalaxy_clean_20260929_120516/06_skeleton` | 128 | 2878.22 | 0.0% | 0.0% |
| `_scan2/cobol_utf8_gitgalaxy_clean_20260929_104118/06_skeleton` | 128 | 2876.82 | 0.0% | 0.0% |
| `_scan3/i18n_utf8_gitgalaxy_clean_20260929_131029/06_skeleton` | 126 | 2804.56 | 0.0% | 0.0% |
| `_scan_3991/i18n_utf8_gitgalaxy_clean_20260929_120558/06_skeleton` | 126 | 2804.56 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `_scan/cobol_utf8/021-nihongo-label-name-in-ambiguous-error-msg/prog.cob` -> **100.0%** Exposure
- `_scan/i18n_utf8/020-nihongo-label-name-in-ambiguous-error-msg/prog.cob` -> **100.0%** Exposure
- `_scan2/cobol_utf8/021-nihongo-label-name-in-ambiguous-error-msg/prog.cob` -> **100.0%** Exposure
- `_scan2/i18n_utf8/020-nihongo-label-name-in-ambiguous-error-msg/prog.cob` -> **100.0%** Exposure
- `_scan3/cobol_utf8/021-nihongo-label-name-in-ambiguous-error-msg/prog.cob` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `_oracle/classify.py` -> **100.0%** Exposure
- `_oracle/validate_extract.py` -> **100.0%** Exposure
- `_scan/analyze.py` -> **100.0%** Exposure
- `_scan2/analyze.py` -> **100.0%** Exposure
- `_scan3/analyze.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `_scan/cobol_utf8/021-nihongo-label-name-in-ambiguous-error-msg/prog.cob` -> **0** Orphaned Functions | **4** Duplicates
- `_scan/cobol_utf8/115-japanese-word-section-variable/prog.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `_scan/i18n_utf8/020-nihongo-label-name-in-ambiguous-error-msg/prog.cob` -> **0** Orphaned Functions | **4** Duplicates
- `_scan/jp-compat/031-sort-status-break-in-section-with-thru/prog.cob` -> **4** Orphaned Functions | **0** Duplicates
- `_scan2/cobol_utf8/021-nihongo-label-name-in-ambiguous-error-msg/prog.cob` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `276` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `16701` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `_oracle/classify.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.115)
- **Top Global Matches:** file_cluster_8: 10.115, file_cluster_6: 11.455, file_cluster_4: 19.063
- **Magnitude:** 736.76 | **LOC:** 454 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.046; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.6%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `classify_static` **(Many-Argument Workhorses)** (Impact: 141.6)
    * *Intent:* """(out-of-scope reasons, notes). No reasons -> a runtime candidate."""
  * `write_md` **(Compute Cores)** (Impact: 62.3)
  * `main` **(I/O & Config Routines)** (Impact: 44.2)
  * `mismatch_cause` **(Compute Cores)** (Impact: 30.5)
    * *Intent:* """A reading of GnuCOBOL's first disagreement with opensourcecobol4j's expected output."""
  * `judge` **(Many-Argument Workhorses)** (Impact: 27.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 85`, `args: 17`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 116`
* *Architecture:* `io: 2`, `api: 14`, `import: 9`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, base64, collections, json, pathlib, re, shutil, subprocess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_oracle/validate_extract.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.244)
- **Top Global Matches:** file_cluster_6: 9.244, file_cluster_8: 13.659, file_cluster_4: 14.993
- **Magnitude:** 170.28 | **LOC:** 128 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.046; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 48.1)
  * `unescape` **(Type Conversions)** (Impact: 9.0)
  * `dq_string` **(Generic / Templated Code)** (Impact: 7.4)
    * *Intent:* """The double-quoted shell string starting at block[start] == '"'."""
  * `expected_output` **(Generic / Templated Code)** (Impact: 5.7)
  * `groups` **(Type Conversions)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 32`
* *Architecture:* `io: 2`, `api: 5`, `import: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, base64, json, pathlib, re, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/analyze.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.163)
- **Top Global Matches:** file_cluster_6: 10.163, file_cluster_8: 14.572, file_cluster_4: 15.363
- **Magnitude:** 142.18 | **LOC:** 131 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.046; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 50.0)
  * `split_divisions` **(Generic / Templated Code)** (Impact: 4.4)
  * `_has` **(Encapsulated Accessors)** (Impact: 4.1)
  * `ex` **(Generic / Templated Code)** (Impact: 3.7)
  * `nonascii` **(Generic / Templated Code)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 30`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 29`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections, json, pathlib, re, sqlite3, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan2/analyze.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.163)
- **Top Global Matches:** file_cluster_6: 10.163, file_cluster_8: 14.572, file_cluster_4: 15.363
- **Magnitude:** 142.18 | **LOC:** 131 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.046; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 50.0)
  * `split_divisions` **(Generic / Templated Code)** (Impact: 4.4)
  * `_has` **(Encapsulated Accessors)** (Impact: 4.1)
  * `ex` **(Generic / Templated Code)** (Impact: 3.7)
  * `nonascii` **(Generic / Templated Code)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 30`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 29`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections, json, pathlib, re, sqlite3, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan3/analyze.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.163)
- **Top Global Matches:** file_cluster_6: 10.163, file_cluster_8: 14.572, file_cluster_4: 15.363
- **Magnitude:** 142.18 | **LOC:** 131 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.046; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 50.0)
  * `split_divisions` **(Generic / Templated Code)** (Impact: 4.4)
  * `_has` **(Encapsulated Accessors)** (Impact: 4.1)
  * `ex` **(Generic / Templated Code)** (Impact: 3.7)
  * `nonascii` **(Generic / Templated Code)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 30`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 29`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections, json, pathlib, re, sqlite3, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan_3991/analyze.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.163)
- **Top Global Matches:** file_cluster_6: 10.163, file_cluster_8: 14.572, file_cluster_4: 15.363
- **Magnitude:** 142.18 | **LOC:** 131 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.046; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 50.0)
  * `split_divisions` **(Generic / Templated Code)** (Impact: 4.4)
  * `_has` **(Encapsulated Accessors)** (Impact: 4.1)
  * `ex` **(Generic / Templated Code)** (Impact: 3.7)
  * `nonascii` **(Generic / Templated Code)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 30`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 29`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections, json, pathlib, re, sqlite3, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan_3992/analyze.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.163)
- **Top Global Matches:** file_cluster_6: 10.163, file_cluster_8: 14.572, file_cluster_4: 15.363
- **Magnitude:** 142.18 | **LOC:** 131 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.046; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 50.0)
  * `split_divisions` **(Generic / Templated Code)** (Impact: 4.4)
  * `_has` **(Encapsulated Accessors)** (Impact: 4.1)
  * `ex` **(Generic / Templated Code)** (Impact: 3.7)
  * `nonascii` **(Generic / Templated Code)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 30`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 29`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections, json, pathlib, re, sqlite3, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jp-compat/suite.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.593)
- **Top Global Matches:** file_cluster_2: 2.593, file_cluster_17: 5.145, file_cluster_13: 6.469
- **Magnitude:** 34.94 | **LOC:** 998 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/i18n_sjis_gitgalaxy_java_spring_20260928_094908/ai_agent_jobs/port_order.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.579)
- **Top Global Matches:** file_cluster_2: 2.579, file_cluster_17: 5.138, file_cluster_13: 6.463
- **Magnitude:** 34.12 | **LOC:** 957 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/cobol_utf8_gitgalaxy_clean_20260928_094928/06_skeleton/127-comp-3-integer-min-value__b_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.573)
- **Top Global Matches:** file_cluster_2: 2.573, file_cluster_17: 5.135, file_cluster_13: 6.461
- **Magnitude:** 33.8 | **LOC:** 940 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan2/cobol_utf8_gitgalaxy_clean_20260929_104118/06_skeleton/127-comp-3-integer-min-value__b_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.573)
- **Top Global Matches:** file_cluster_2: 2.573, file_cluster_17: 5.135, file_cluster_13: 6.461
- **Magnitude:** 33.8 | **LOC:** 940 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan3/cobol_utf8_gitgalaxy_clean_20260929_130951/06_skeleton/127-comp-3-integer-min-value__b_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.573)
- **Top Global Matches:** file_cluster_2: 2.573, file_cluster_17: 5.135, file_cluster_13: 6.461
- **Magnitude:** 33.8 | **LOC:** 940 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan_3991/cobol_utf8_gitgalaxy_clean_20260929_120516/06_skeleton/127-comp-3-integer-min-value__b_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.573)
- **Top Global Matches:** file_cluster_2: 2.573, file_cluster_17: 5.135, file_cluster_13: 6.461
- **Magnitude:** 33.8 | **LOC:** 940 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/jp-compat_gitgalaxy_clean_20260928_094930/06_skeleton/003-split-keys-record-key__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/jp-compat_gitgalaxy_clean_20260928_094930/06_skeleton/004-split-keys-record-key-not-yet__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/jp-compat_gitgalaxy_clean_20260928_094930/06_skeleton/005-split-keys-start-syntax-equal__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/jp-compat_gitgalaxy_clean_20260928_094930/06_skeleton/006-split-keys-start-syntax-equal-not-yet__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/jp-compat_gitgalaxy_clean_20260928_094930/06_skeleton/007-split-keys-start-syntax-greater-than__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/jp-compat_gitgalaxy_clean_20260928_094930/06_skeleton/008-split-keys-start-syntax-greater-than-not-yet__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan/jp-compat_gitgalaxy_clean_20260928_094930/06_skeleton/009-split-keys-key-unmatch__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan2/jp-compat_gitgalaxy_clean_20260929_104212/06_skeleton/003-split-keys-record-key__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan2/jp-compat_gitgalaxy_clean_20260929_104212/06_skeleton/004-split-keys-record-key-not-yet__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan2/jp-compat_gitgalaxy_clean_20260929_104212/06_skeleton/005-split-keys-start-syntax-equal__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan2/jp-compat_gitgalaxy_clean_20260929_104212/06_skeleton/006-split-keys-start-syntax-equal-not-yet__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_scan2/jp-compat_gitgalaxy_clean_20260929_104212/06_skeleton/007-split-keys-start-syntax-greater-than__prog_skeleton.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.567)
- **Top Global Matches:** file_cluster_2: 2.567, file_cluster_17: 5.132, file_cluster_13: 6.458
- **Magnitude:** 33.46 | **LOC:** 923 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `_scan/jp-compat/024-allow-empty-evaluate-semantics/prog.cob` (COBOL) | Magnitude: 5.66 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, branch: 4, class_start: 1
- `_scan/jp-compat/026-allow-empty-evaluate-semantics-3/prog.cob` (COBOL) | Magnitude: 5.66 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, branch: 4, class_start: 1
- `_scan2/jp-compat/024-allow-empty-evaluate-semantics/prog.cob` (COBOL) | Magnitude: 5.66 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, branch: 4, class_start: 1
- `_scan2/jp-compat/026-allow-empty-evaluate-semantics-3/prog.cob` (COBOL) | Magnitude: 5.66 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, branch: 4, class_start: 1
- `_scan3/jp-compat/024-allow-empty-evaluate-semantics/prog.cob` (COBOL) | Magnitude: 5.66 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, branch: 4, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `_scan/jp-compat/064-userfh-read-lock-so/hoge.c` (C) | Magnitude: 8.34 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 9, indent_tabs: 4, import: 3, indent_spaces: 2
- `_scan/jp-compat/065-userfh-read-lock-dll/hoge.c` (C) | Magnitude: 8.34 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 9, indent_tabs: 4, import: 3, indent_spaces: 2
- `_scan2/jp-compat/064-userfh-read-lock-so/hoge.c` (C) | Magnitude: 8.34 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 9, indent_tabs: 4, import: 3, indent_spaces: 2
- `_scan2/jp-compat/065-userfh-read-lock-dll/hoge.c` (C) | Magnitude: 8.34 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 9, indent_tabs: 4, import: 3, indent_spaces: 2
- `_scan3/jp-compat/064-userfh-read-lock-so/hoge.c` (C) | Magnitude: 8.34 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 9, indent_tabs: 4, import: 3, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `_scan/cobol_utf8/021-nihongo-label-name-in-ambiguous-error-msg/prog.cob` (COBOL) | Magnitude: 6.84 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, func_start: 6, panics_and_aborts: 4
- `_scan/i18n_utf8/020-nihongo-label-name-in-ambiguous-error-msg/prog.cob` (COBOL) | Magnitude: 6.84 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, func_start: 6, panics_and_aborts: 4
- `_scan2/cobol_utf8/021-nihongo-label-name-in-ambiguous-error-msg/prog.cob` (COBOL) | Magnitude: 6.84 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, func_start: 6, panics_and_aborts: 4
- `_scan2/i18n_utf8/020-nihongo-label-name-in-ambiguous-error-msg/prog.cob` (COBOL) | Magnitude: 6.84 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, func_start: 6, panics_and_aborts: 4
- `_scan3/cobol_utf8/021-nihongo-label-name-in-ambiguous-error-msg/prog.cob` (COBOL) | Magnitude: 6.84 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, func_start: 6, panics_and_aborts: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `_scan/jp-compat/113-call-c-calledby/callee.cob` -> **Severity: 8.6** (Blast Radius: 0.086 * Doc Risk: 100.0%)
- `_scan2/jp-compat/113-call-c-calledby/callee.cob` -> **Severity: 8.6** (Blast Radius: 0.086 * Doc Risk: 100.0%)
- `_scan3/jp-compat/113-call-c-calledby/callee.cob` -> **Severity: 8.6** (Blast Radius: 0.086 * Doc Risk: 100.0%)
- `_scan_3991/jp-compat/113-call-c-calledby/callee.cob` -> **Severity: 8.6** (Blast Radius: 0.086 * Doc Risk: 100.0%)
- `_scan_3992/jp-compat/113-call-c-calledby/callee.cob` -> **Severity: 8.6** (Blast Radius: 0.086 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `2240` files carry mainframe facts -- `74` call sites, `404` dataset bindings, `4998` record items.

### `_scan/jp-compat/086-cob-date-func-current-date-of-time/prog.cob` (COBOL)
- **Calls:** `CALL SYSTEM`
- **Record layouts (26 items):** `CMDLN (18)`, `CURR-DATE (8)`
- **Data moves:** 7 (MOVE 7); most-fed items `CMDLN-DD`, `CMDLN-H`, `CMDLN-M`, `CMDLN-MM`, `CMDLN-S`, `CMDLN-YYYY`

### `_scan2/jp-compat/086-cob-date-func-current-date-of-time/prog.cob` (COBOL)
- **Calls:** `CALL SYSTEM`
- **Record layouts (26 items):** `CMDLN (18)`, `CURR-DATE (8)`
- **Data moves:** 7 (MOVE 7); most-fed items `CMDLN-DD`, `CMDLN-H`, `CMDLN-M`, `CMDLN-MM`, `CMDLN-S`, `CMDLN-YYYY`

### `_scan3/jp-compat/086-cob-date-func-current-date-of-time/prog.cob` (COBOL)
- **Calls:** `CALL SYSTEM`
- **Record layouts (26 items):** `CMDLN (18)`, `CURR-DATE (8)`
- **Data moves:** 7 (MOVE 7); most-fed items `CMDLN-DD`, `CMDLN-H`, `CMDLN-M`, `CMDLN-MM`, `CMDLN-S`, `CMDLN-YYYY`

### `_scan_3991/jp-compat/086-cob-date-func-current-date-of-time/prog.cob` (COBOL)
- **Calls:** `CALL SYSTEM`
- **Record layouts (26 items):** `CMDLN (18)`, `CURR-DATE (8)`
- **Data moves:** 7 (MOVE 7); most-fed items `CMDLN-DD`, `CMDLN-H`, `CMDLN-M`, `CMDLN-MM`, `CMDLN-S`, `CMDLN-YYYY`

### `_scan_3992/jp-compat/086-cob-date-func-current-date-of-time/prog.cob` (COBOL)
- **Calls:** `CALL SYSTEM`
- **Record layouts (26 items):** `CMDLN (18)`, `CURR-DATE (8)`
- **Data moves:** 7 (MOVE 7); most-fed items `CMDLN-DD`, `CMDLN-H`, `CMDLN-M`, `CMDLN-MM`, `CMDLN-S`, `CMDLN-YYYY`

### `jp-compat/086-cob-date-func-current-date-of-time/prog.cob` (COBOL)
- **Calls:** `CALL SYSTEM`
- **Record layouts (26 items):** `CMDLN (18)`, `CURR-DATE (8)`
- **Data moves:** 7 (MOVE 7); most-fed items `CMDLN-DD`, `CMDLN-H`, `CMDLN-M`, `CMDLN-MM`, `CMDLN-S`, `CMDLN-YYYY`

### `_scan/jp-compat/003-split-keys-record-key/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/RANDOM key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan/jp-compat/004-split-keys-record-key-not-yet/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/RANDOM key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan/jp-compat/005-split-keys-start-syntax-equal/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan/jp-compat/006-split-keys-start-syntax-equal-not-yet/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan/jp-compat/007-split-keys-start-syntax-greater-than/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan/jp-compat/008-split-keys-start-syntax-greater-than-not-yet/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan/jp-compat/009-split-keys-key-unmatch/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan2/jp-compat/003-split-keys-record-key/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/RANDOM key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan2/jp-compat/004-split-keys-record-key-not-yet/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/RANDOM key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan2/jp-compat/005-split-keys-start-syntax-equal/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan2/jp-compat/006-split-keys-start-syntax-equal-not-yet/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan2/jp-compat/007-split-keys-start-syntax-greater-than/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan2/jp-compat/008-split-keys-start-syntax-greater-than-not-yet/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

### `_scan2/jp-compat/009-split-keys-key-unmatch/prog.cob` (COBOL)
- **Datasets:** `./TEST-FILE(INPUT/OUTPUT)`
- **Record layouts (4 items):** `TEST-REC⟵TEST-FILE (4)`
- **Keyed files:** `TEST-FILE INDEXED/SEQUENTIAL key TEST-KEY1`
- **Data moves:** 20 (MOVE 20)

*(+2220 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 46% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (2528 gaps); application programs (source or load-module list) (53 gaps); copybook libraries (24 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5301 call pairs -- scoped 3.3%, unique 0.0%, ambiguous 0.1%, external 96.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 2711 | 2.1% | 0.0% | 0.0% | 97.9% |
| shell | 2083 | 0.0% | 0.0% | 0.0% | 100.0% |
| python | 365 | 12.1% | 0.0% | 0.0% | 87.9% |
| cobol | 126 | 59.5% | 0.0% | 4.8% | 35.7% |
| c | 12 | 0.0% | 0.0% | 0.0% | 100.0% |
| postgresql | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
