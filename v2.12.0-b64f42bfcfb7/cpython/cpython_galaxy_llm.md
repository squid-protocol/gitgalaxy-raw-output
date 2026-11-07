# ARCHITECTURAL_BRIEF: cpython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/python/cpython` |
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
- **Scope:** 3819 analyzed artifact(s), 1398111 LOC.
- **Load-bearing artifact:** `Lib/unittest/__init__.py` -- 990 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Modules/posixmodule.c` -- pulls in 98 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Python/Python-ast.c` at magnitude 17876.62 (structural weight, not risk).
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
| Total Artifacts | 5603 |
| Analyzed Artifacts (Scanned) | 3819 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1784 |
| Total LOC | 1398111 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 68.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5461 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2076 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 25.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3336 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 148 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 2175 | 722256 | 57.0% |
| C | 1055 | 646963 | 27.6% |
| PLAINTEXT | 171 | 0 | 4.5% |
| XML | 134 | 8 | 3.5% |
| MARKDOWN | 59 | 0 | 1.5% |
| SHELL | 49 | 1090 | 1.3% |
| YAML | 40 | 2606 | 1.0% |
| JSON | 30 | 729 | 0.8% |
| BATCH | 29 | 1649 | 0.8% |
| OBJECTIVE-C | 15 | 904 | 0.4% |
| MAKEFILE | 11 | 3496 | 0.3% |
| CPP | 10 | 3918 | 0.3% |
| JAVASCRIPT | 8 | 1905 | 0.2% |
| POWERSHELL | 6 | 249 | 0.2% |
| KOTLIN | 5 | 332 | 0.1% |
| CSS | 5 | 2550 | 0.1% |
| M4 | 5 | 6743 | 0.1% |
| HTML | 4 | 1616 | 0.1% |
| CSV | 4 | 999 | 0.1% |
| ASSEMBLY | 2 | 63 | 0.1% |
| TYPESCRIPT | 2 | 35 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 18 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3790 |
| utf-8 | bom | 11 |
| cp1252 | cp1252-fallback | 10 |
| latin-1 | latin-1-fallback | 8 |

> 2 guessed file(s) read as double-byte text that decodes strictly as gbk: if that is the estate's code page, rescan with `--source-encoding gbk` (or the right one of those). E.g. `Lib/test/cjkencodings/gb2312.txt`, `Lib/test/cjkencodings/gbk.txt`.

> 1 guessed file(s) read as double-byte text that decodes strictly as big5: if that is the estate's code page, rescan with `--source-encoding big5` (or the right one of those). E.g. `Lib/test/cjkencodings/big5.txt`.

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `Lib/test/cjkencodings/euc_jp.txt`.

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk / euc_kr: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `Lib/test/cjkencodings/euc_kr.txt`.

> 1 guessed file(s) read as double-byte text that decodes strictly as shift_jis / gbk: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `Lib/test/cjkencodings/shift_jis.txt`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 23%, Data / Markup / Trivial 21%, Large Core Modules (3) 16%, Declarative / Non-Code 12%, Encapsulated Accessors Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3581 | 93.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 230 | 6.0% |
| Static: Minified & Vendor Opaque Mass | 8 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1784*

**Composition by Extension & Reason:**
- `.rst`: 555x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 232x Excluded (Unsupported Extension: '.rst')
- `.dectest`: 143x Excluded (Unsupported Extension: '.decTest')
- `.py`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Excluded (Embedded Hex Payload: 1024 hex tokens in 699 LOC), 1x Excluded (Machine-Generated Source Code Signature: 376 LOC)
- `.toml`: 69x Excluded (Unsupported Extension: '.toml'), 8x Unsupported Format (.toml), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vcxproj`: 55x Excluded (Unsupported Extension: '.vcxproj'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 54x Excluded (Explicitly Denied Extension: '.png')
- `.filters`: 52x Excluded (Unsupported Extension: '.filters')
- `no_extension`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.undeterminable), 4x Excluded (Binary Format Detected)
- `.h`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2140 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2438 LOC)
- `.wxs`: 44x Unsupported Format (.wxs)
- `.wixproj`: 30x Unsupported Format (.wixproj)
- `.icns`: 18x Excluded (Unsupported Extension: '.icns')
- `.c`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2090 LOC), 1x Excluded (Machine-Generated Source Code Signature: 958 LOC)
- `.html`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 63 exceeds 500 chars), 1x Excluded (Saturation: Line 27 exceeds 500 chars)
- `.gif`: 13x Excluded (Explicitly Denied Extension: '.gif')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 26.7 | 22.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 49.1 | 57.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.8 | 9.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 94.2 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 62.9 | 90.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 25.3 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 17591 | 1616 | 11 | `Lib/test/test_itertools.py` |
| cleanup | 3317 | 478 | 1 | `Lib/test/_test_multiprocessing.py` |
| guards | 83377 | 2287 | 57 | `Include/internal/pycore_unicodeobject_generated.h` |
| danger | 47516 | 2330 | 31 | `Python/Python-ast.c` |
| concurrency | 13685 | 695 | 4 | `Lib/test/test_asyncio/test_locks.py` |
| connectivity | 84665 | 2869 | 57 | `Lib/test/test_typing.py` |
| io | 25746 | 1219 | 12 | `Lib/test/test_socket.py` |
| crypto | 64 | 48 | 0 | `Lib/test/test_httplib.py` |
| ipc | 2468 | 240 | 0 | `Lib/test/test_subprocess.py` |
| time | 1432 | 193 | 0 | `Lib/test/datetimetester.py` |
| serialization | 463 | 124 | 0 | `Lib/test/test_ast/test_ast.py` |
| regex | 1609 | 257 | 0 | `Lib/test/test_re.py` |
| events | 4531 | 338 | 0 | `configure.ac` |
| tests | 47227 | 1059 | 28 | `Lib/test/test_unittest/testmock/testmock.py` |
| docs | 17758 | 1562 | 11 | `Lib/tkinter/__init__.py` |
| debt | 10810 | 1234 | 7 | `Tools/peg_generator/pegen/c_generator.py` |
| mutation | 429624 | 2795 | 303 | `Python/Python-ast.c` |
| dead_code | 32954 | 1570 | 22 | `Lib/test/test_typing.py` |
| credential | 166 | 31 | 0 | `Lib/test/test_zoneinfo/data/zoneinfo_data.json` |
| threat | 2286 | 172 | 0 | `Lib/test/test_lzma.py` |
| ml_ai | 1103 | 123 | 0 | `Modules/_decimal/libmpdec/mpdecimal.c` |
| ui | 410 | 37 | 0 | `Lib/profiling/sampling/_heatmap_assets/heatmap.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5556**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Lib/test/test_socket.py` (Hits: 1839)
- `Lib/test/test_os/test_os.py` (Hits: 1270)
- `Lib/test/test_shutil.py` (Hits: 865)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`Lib/unittest/__init__.py`) — 990 inbound connections
2. **case.py** (`Lib/unittest/case.py`) — 880 inbound connections
3. **__init__.py** (`Lib/test/support/__init__.py`) — 624 inbound connections
4. **os.py** (`Lib/os.py`) — 588 inbound connections
5. **errors.c** (`Python/errors.c`) — 447 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **posixmodule.c** (`Modules/posixmodule.c`) — 98 outbound dependencies
2. **Python.h** (`Include/Python.h`) — 94 outbound dependencies
3. **__init__.py** (`Lib/test/test_import/__init__.py`) — 93 outbound dependencies
4. **test_pyrepl.py** (`Lib/test/test_pyrepl/test_pyrepl.py`) — 78 outbound dependencies
5. **test_inspect.py** (`Lib/test/test_inspect/test_inspect.py`) — 66 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `obj2ast_stmt` **(Many-Argument Workhorses)** (@ `Python/Python-ast.c`) -> Impact: **1659.6** | LOC: 2692
- `dummy_func` **(Many-Argument Workhorses)** (@ `Python/bytecodes.c`) -> Impact: **1547.0** | LOC: 6187
- `obj2ast_expr` **(Many-Argument Workhorses)** (@ `Python/Python-ast.c`) -> Impact: **1209.1** | LOC: 1911
- `add_ast_annotations` **(Many-Argument Workhorses)** (@ `Python/Python-ast.c`) -> Impact: **1144.8** | LOC: 4341
- `sock_initobj_impl` **(Many-Argument Workhorses)** (@ `Modules/socketmodule.c`) -> Impact: **712.1** | LOC: 2044
- `_socket_socket_sendmsg_impl` **(Many-Argument Workhorses)** (@ `Modules/socketmodule.c`) -> Impact: **710.5** | LOC: 2012
- `tok_get_normal_mode` **(Many-Argument Workhorses)** (@ `Parser/lexer/lexer.c`) -> Impact: **652.5** | LOC: 891
- `convertsimple` **(Many-Argument Workhorses)** (@ `Python/getargs.c`) -> Impact: **531.4** | LOC: 671
  * *Intent:* */
- `_Py_dg_dtoa` **(Many-Argument Workhorses)** (@ `Python/dtoa.c`) -> Impact: **504.0** | LOC: 609
  * *Intent:* call to _Py_dg_freedtoa. */
- `dummy_func` **(I/O & Config Routines)** (@ `Python/optimizer_bytecodes.c`) -> Impact: **462.4** | LOC: 2028

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Lib/test` | 439 | 258992.85 | 25.04% | 0.0% |
| `Lib` | 146 | 112966.42 | 48.57% | 17.61% |
| `Python` | 115 | 97743.3 | 43.87% | 29.21% |
| `Modules` | 120 | 93607.34 | 38.06% | 35.1% |
| `Objects` | 55 | 72608.74 | 46.7% | 29.39% |
| `Lib/test/test_asyncio` | 42 | 39827.7 | 40.7% | 0.0% |
| `Modules/clinic` | 79 | 31772.34 | 43.12% | 0.34% |
| `Lib/idlelib` | 75 | 17888.56 | 39.84% | 19.14% |
| `Lib/asyncio` | 35 | 13992.14 | 56.53% | 17.22% |
| `Modules/_decimal/libmpdec` | 35 | 13805.0 | 33.56% | 21.69% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Lib/asyncio/protocols.py` -> **100.0%** Exposure
- `Lib/codecs.py` -> **100.0%** Exposure
- `Lib/multiprocessing/dummy/connection.py` -> **100.0%** Exposure
- `Lib/queue.py` -> **100.0%** Exposure
- `Lib/idlelib/idle_test/test_calltip.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Android/android-env.sh` -> **100.0%** Exposure
- `Mac/BuildScript/scripts/postflight.patch-profile` -> **100.0%** Exposure
- `Misc/python-config.sh.in` -> **100.0%** Exposure
- `Modules/makesetup` -> **100.0%** Exposure
- `Tools/wasm/wasi-env` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Lib/test/test_typing.py` -> **546** Orphaned Functions | **123** Duplicates
- `Lib/test/test_email/test_email.py` -> **473** Orphaned Functions | **0** Duplicates
- `Lib/test/test_inspect/test_inspect.py` -> **334** Orphaned Functions | **128** Duplicates
- `Lib/test/test_socket.py` -> **415** Orphaned Functions | **39** Duplicates
- `Lib/test/test_email/test__header_value_parser.py` -> **367** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `Lib/ssl.py` -> **25.2695%** Exposure
- `Lib/test/test_ssl.py` -> **7.0836%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `64` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `18076` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Python/Python-ast.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.47)
- **Top Global Matches:** file_cluster_6: 7.47, file_cluster_8: 11.006, file_cluster_4: 14.793
- **Magnitude:** 17876.62 | **LOC:** 18576 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **11**; blast radius 0.141; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `obj2ast_stmt` **(Many-Argument Workhorses)** (Impact: 1659.6)
  * `obj2ast_expr` **(Many-Argument Workhorses)** (Impact: 1209.1)
  * `add_ast_annotations` **(Many-Argument Workhorses)** (Impact: 1144.8)
  * `ast2obj_stmt` **(Many-Argument Workhorses)** (Impact: 425.6)
  * `init_types` **(Compute Cores)** (Impact: 376.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2766 instances
* *State Mutation (weighted view):* 8527
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3951`, `structural_boundaries: 2390`, `args: 1478`, `func_start: 152`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 209`, `state_mutation: 2995`
* *Architecture:* `api: 127`, `import: 11`
* *Defense:* `safety: 5`, `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.062714
  * `Imports (Out-Degree: 37):` Python.h, pycore_ast.h, pycore_ast_state.h, pycore_ceval.h, pycore_lock.h, pycore_modsupport.h, pycore_pystate.h, pycore_runtime.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `Objects/unicodeobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.886)
- **Top Global Matches:** file_cluster_6: 6.886, file_cluster_4: 8.949, file_cluster_16: 16.991
- **Magnitude:** 11936.8 | **LOC:** 14992 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 15.4%
- **Blast Radius:** changing it is visible to **267** in-repo importer(s); it depends on **41**; blast radius 2.32; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.4%), Guard Balance (formerly Safety Score) (68.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unicode_fromformat_arg` **(Many-Argument Workhorses)** (Impact: 272.7)
    * *Intent:* #define F_LONG 1 #define F_LONGLONG 2 #define F_SIZE 3 #define F_PTRDIFF 4 #define F_INTMAX 5
  * `_PyUnicode_DecodeUnicodeEscapeInternal2` **(Many-Argument Workhorses)** (Impact: 187.1)
    * *Intent:* /* --- Unicode Escape Codec ----------------------------------------------- */
  * `replace` **(Many-Argument Workhorses)** (Impact: 157.0)
  * `PyUnicode_DecodeUTF7Stateful` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* /* The decoder. The only state we preserve is our read position, * i.e. how many characters we have ...
  * `unicode_decode_utf8_impl` **(Many-Argument Workhorses)** (Impact: 105.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1589 instances
* *State Mutation (weighted view):* 4893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2540`, `structural_boundaries: 1463`, `args: 747`, `func_start: 354`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 108`, `state_mutation: 1715`, `planned_debt: 2`, `fragile_debt: 6`
* *Architecture:* `api: 275`, `import: 77`
* *Defense:* `safety: 296`, `doc: 1`, `immutability_locks: 479`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.003304 | `Ripple Effect (Closeness):` 0.102973
  * `Imports (Out-Degree: 85):` Python.h, unicodeobject.c.h, pycore_abstract.h, pycore_bytes_methods.h, pycore_bytesobject.h, pycore_ceval.h, pycore_codecs.h, pycore_critical_section.h...
  * `Imported By (In-Degree: 267):` (Excluded from Brief to save tokens)

### `Modules/posixmodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.983)
- **Top Global Matches:** file_cluster_4: 8.983, file_cluster_16: 12.593, file_cluster_6: 13.502
- **Magnitude:** 8316.24 | **LOC:** 18842 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 15.4%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **98**; blast radius 0.142; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all_ins` **(Compute Cores)** (Impact: 362.6)
  * `os_sendfile_impl` **(Many-Argument Workhorses)** (Impact: 136.8)
  * `win32_xstat_slow_impl` **(Many-Argument Workhorses)** (Impact: 123.3)
  * `py_posix_spawn` **(Many-Argument Workhorses)** (Impact: 111.7)
  * `os_utime_impl` **(Many-Argument Workhorses)** (Impact: 110.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 879 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 2729
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2081`, `structural_boundaries: 1384`, `args: 1067`, `func_start: 367`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 63`, `high_risk_execution: 9`, `state_mutation: 971`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 8`, `unreferenced_by_name: 220`
* *Architecture:* `io: 5`, `api: 32`, `import: 105`
* *Defense:* `safety: 58`, `immutability_locks: 89`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.000378 | `Ripple Effect (Closeness):` 0.067931
  * `Imports (Out-Degree: 69):` ProcessSnapshot.h, Python.h, aclapi.h, posixmodule.c.h, copyfile.h, crt_externs.h, limits.h, direct.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `Lib/test/test_calendar.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.379)
- **Top Global Matches:** file_cluster_2: 5.379, file_cluster_13: 5.867, file_cluster_17: 6.211
- **Magnitude:** 7528.83 | **LOC:** 1314 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.0%), Complexity Load (formerly Cognitive Load) (15.9%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 232`, `args: 102`, `func_start: 102`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 129`, `fragile_debt: 1`
* *Architecture:* `io: 15`, `api: 115`, `import: 12`
* *Defense:* `safety: 21`, `doc: 6`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` calendar, contextlib, datetime, io, locale, os, platform, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/typeobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.212)
- **Top Global Matches:** file_cluster_4: 8.212, file_cluster_12: 9.8, file_cluster_16: 10.403
- **Magnitude:** 7202.5 | **LOC:** 12874 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 38.1%
- **Blast Radius:** changing it is visible to **157** in-repo importer(s); it depends on **30**; blast radius 3.4; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.8%), Guard Balance (formerly Safety Score) (61.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyType_FromMetaclass` **(Many-Argument Workhorses)** (Impact: 191.3)
  * `update_one_slot` **(Many-Argument Workhorses)** (Impact: 99.3)
    * *Intent:* * There are some further special cases for specific slots, like supporting * __hash__ = None for tp_...
  * `inherit_slots` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `subtype_dealloc` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `object_getstate_default` **(Many-Argument Workhorses)** (Impact: 51.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 768 instances
* *State Mutation (weighted view):* 2444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1793`, `structural_boundaries: 1311`, `args: 847`, `func_start: 418`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 193`, `state_mutation: 908`, `planned_debt: 4`, `fragile_debt: 15`, `unreferenced_by_name: 60`
* *Architecture:* `api: 96`, `import: 30`
* *Defense:* `safety: 280`, `doc: 1`, `test: 32`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.001664 | `Ripple Effect (Closeness):` 0.094092
  * `Imports (Out-Degree: 73):` Python.h, typeobject.c.h, opcode.h, pycore_abstract.h, pycore_call.h, pycore_cell.h, pycore_code.h, pycore_descrobject.h...
  * `Imported By (In-Degree: 157):` (Excluded from Brief to save tokens)

### `Modules/_decimal/libmpdec/mpdecimal.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.17)
- **Top Global Matches:** file_cluster_4: 5.17, file_cluster_6: 10.111, file_cluster_16: 11.072
- **Magnitude:** 7191.28 | **LOC:** 9016 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **16**; blast radius 0.306; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.6%), Guard Balance (formerly Safety Score) (69.3%)
- **Documentation Coverage:** 48.1848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mpd_qdivmod` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* /* Internal function. */
  * `_mpd_qdiv` **(Many-Argument Workhorses)** (Impact: 90.7)
    * *Intent:* /* Divide a by b. */
  * `mpd_qpowmod` **(Many-Argument Workhorses)** (Impact: 85.9)
    * *Intent:* /* The powmod function: (base**exp) % mod */
  * `mpd_qpow` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* /* The power function: base**exp */
  * `_mpd_base_ndivmod` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* * Internal function for large numbers: * * q, r = divmod(coeff(a), coeff(b)) * * Strategy: Multiply ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 916 instances
* *High Risk Execution (weighted view):* 8
* *State Mutation (weighted view):* 2896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1312`, `structural_boundaries: 738`, `args: 367`, `func_start: 304`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 12`, `state_mutation: 1064`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 73`
* *Architecture:* `api: 198`, `import: 16`
* *Defense:* `safety: 115`, `doc: 32`, `immutability_locks: 454`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.306
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.003847
  * `Imports (Out-Degree: 13):` assert.h, basearith.h, bits.h, constants.h, convolute.h, crt.h, fenv.h, float.h...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `Lib/test/_test_multiprocessing.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.217)
- **Top Global Matches:** file_cluster_12: 8.217, file_cluster_15: 9.34, file_cluster_16: 9.516
- **Magnitude:** 6728.34 | **LOC:** 7490 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **49**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (77.2%), Guard Balance (formerly Safety Score) (67.8%), Complexity Load (formerly Cognitive Load) (46.7%)
- **Documentation Coverage:** 97.0427% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `install_tests_in_module_dict` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* # # Functions used to create test cases from the base ones in this module #
  * `_test_dict` **(Stateful Encapsulated Methods)** (Impact: 41.4)
  * `_test_set_operator_symbols` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `_test_list` **(Stateful Encapsulated Methods)** (Impact: 34.4)
  * `_test_set_operator_methods` **(Stateful Encapsulated Methods)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 260 instances
* *Amplified Cascading Flux:* 605 instances
* *Concurrency (weighted view):* 1609
* *State Mutation (weighted view):* 2549
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 578`, `structural_boundaries: 1063`, `args: 522`, `func_start: 507`, `class_start: 92`
* *Risk/State:* `safety_bypasses: 60`, `high_risk_execution: 14`, `state_mutation: 1339`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `io: 163`, `api: 434`, `concurrency: 309`, `import: 77`
* *Defense:* `safety: 206`, `doc: 36`, `test: 397`, `sync_locks: 130`, `cleanup: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.00023 | `Ripple Effect (Closeness):` 0.003141
  * `Imports (Out-Degree: 60):` array, atexit, collections.abc, ctypes, errno, functools, gc, glob...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `Modules/_pickle.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.842)
- **Top Global Matches:** file_cluster_4: 5.842, file_cluster_6: 10.433, file_cluster_16: 10.881
- **Magnitude:** 5494.3 | **LOC:** 8277 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.1%), Guard Balance (formerly Safety Score) (66.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.5%)
- **Documentation Coverage:** 99.2806% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_reduce` **(Many-Argument Workhorses)** (Impact: 187.5)
    * *Intent:* /* We're saving obj, and args is the 2-thru-5 tuple returned by the * appropriate __reduce__ method ...
  * `save` **(Many-Argument Workhorses)** (Impact: 142.9)
  * `save_global` **(Many-Argument Workhorses)** (Impact: 141.2)
  * `batch_dict` **(Many-Argument Workhorses)** (Impact: 82.9)
    * *Intent:* /* iter is an iterator giving (key, value) pairs, and we batch up chunks of * MARK key value ... key...
  * `save_long` **(Many-Argument Workhorses)** (Impact: 68.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 722 instances
* *State Mutation (weighted view):* 2235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1227`, `structural_boundaries: 808`, `args: 400`, `func_start: 208`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 791`, `planned_debt: 6`, `fragile_debt: 12`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 10`, `import: 16`
* *Defense:* `safety: 102`, `doc: 6`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000262
  * `Imports (Out-Degree: 56):` Python.h, _pickle.c.h, pycore_bytesobject.h, pycore_ceval.h, pycore_critical_section.h, pycore_long.h, pycore_moduleobject.h, pycore_object.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Lib/test/test_typing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.705)
- **Top Global Matches:** file_cluster_5: 7.705, file_cluster_12: 10.282, file_cluster_7: 11.186
- **Magnitude:** 5493.2 | **LOC:** 11170 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Complexity Load (formerly Cognitive Load) (17.7%), Connectivity (formerly Api Exposure) (15.5%)
- **Documentation Coverage:** 99.7083% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `template_replace` **(Many-Argument Workhorses)** (Impact: 17.2)
    * *Intent:* """Renders templates with possible combinations of replacements. Example 1: Suppose that: templates ...
  * `test_inheritance_pep563` **(Stateful Encapsulated Methods)** (Impact: 14.2)
  * `test_all_exported_names` **(Compute Cores)** (Impact: 13.8)
    * *Intent:* # ensure all dynamically created objects are actualised for name in typing.__all__: getattr(typing, ...
  * `test_pickle` **(Generic / Templated Code)** (Impact: 13.7)
  * `test_all_repr_eq_any` **(Defensive Guards)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 170 instances
* *High Risk Execution (weighted view):* 46
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 1488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 3365`, `args: 1070`, `func_start: 1062`, `class_start: 870`
* *Risk/State:* `safety_bypasses: 518`, `high_risk_execution: 47`, `state_mutation: 1148`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 123`, `unreferenced_by_name: 546`
* *Architecture:* `io: 5`, `api: 1430`, `concurrency: 11`, `import: 60`
* *Defense:* `safety: 158`, `doc: 15`, `test: 700`, `immutability_locks: 171`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` __future__, abc, annotationlib, collections, collections.abc, contextlib, copy, dataclasses...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/socketmodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.43)
- **Top Global Matches:** file_cluster_4: 6.43, file_cluster_6: 9.578, file_cluster_16: 12.042
- **Magnitude:** 5407.14 | **LOC:** 9359 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 12.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **35**; blast radius 0.075; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.6%), Guard Balance (formerly Safety Score) (60.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sock_initobj_impl` **(Many-Argument Workhorses)** (Impact: 712.1)
  * `_socket_socket_sendmsg_impl` **(Many-Argument Workhorses)** (Impact: 710.5)
  * `getsockaddrarg` **(Many-Argument Workhorses)** (Impact: 376.7)
    * *Intent:* through len_ret. */
  * `makesockaddr` **(Many-Argument Workhorses)** (Impact: 140.3)
    * *Intent:* to determine what kind of address it really is. */ /*ARGSUSED*/
  * `sock_call_ex` **(Many-Argument Workhorses)** (Impact: 88.4)
    * *Intent:* called with the GIL released. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 512 instances
* *State Mutation (weighted view):* 1667
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 871`, `structural_boundaries: 814`, `args: 498`, `func_start: 128`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 643`, `dead_code: 4`, `fragile_debt: 6`, `unreferenced_by_name: 14`
* *Architecture:* `io: 23`, `api: 36`, `import: 39`
* *Defense:* `safety: 63`, `doc: 1`, `immutability_locks: 38`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.000589
  * `Imports (Out-Degree: 43):` AvailabilityMacros.h, Python.h, Rpc.h, addrinfo.h, inet.h, socketmodule.c.h, fcntl.h, getaddrinfo.c...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Objects/longobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.691)
- **Top Global Matches:** file_cluster_4: 8.691, file_cluster_6: 10.736, file_cluster_12: 12.833
- **Magnitude:** 5378.62 | **LOC:** 6969 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **319** in-repo importer(s); it depends on **15**; blast radius 2.343; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (74.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyLong_AsNativeBytes` **(Many-Argument Workhorses)** (Impact: 150.0)
  * `long_pow` **(Many-Argument Workhorses)** (Impact: 112.0)
    * *Intent:* /* pow(v, w, x) */
  * `long_format_binary` **(Many-Argument Workhorses)** (Impact: 101.6)
    * *Intent:* if alternate is nonzero. */
  * `_PyLong_AsByteArray` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `PyLong_FromString` **(Many-Argument Workhorses)** (Impact: 87.2)
    * *Intent:* /* Parses an int from a bytestring. Leading and trailing whitespace will be * ignored. * * If succes...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 879 instances
* *State Mutation (weighted view):* 2747
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 960`, `structural_boundaries: 478`, `args: 338`, `func_start: 170`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 222`, `state_mutation: 989`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `api: 115`, `import: 15`
* *Defense:* `safety: 203`, `doc: 2`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.343
  * `Choke Point (Betweenness):` 0.001204 | `Ripple Effect (Closeness):` 0.10151
  * `Imports (Out-Degree: 38):` Python.h, longobject.c.h, float.h, pycore_bitutils.h, pycore_call.h, pycore_freelist.h, pycore_initconfig.h, pycore_long.h...
  * `Imported By (In-Degree: 319):` (Excluded from Brief to save tokens)

### `Lib/_pydecimal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.019)
- **Top Global Matches:** file_cluster_4: 5.019, file_cluster_16: 10.03, file_cluster_15: 10.144
- **Magnitude:** 5322.86 | **LOC:** 6413 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 0.45; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.9%)
- **Documentation Coverage:** 15.8537% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__pow__` **(Many-Argument Workhorses)** (Impact: 122.6)
    * *Intent:* """Return self ** other [ % modulo]. With two arguments, compute self**other. With three arguments, ...
  * `_power_exact` **(Many-Argument Workhorses)** (Impact: 106.3)
    * *Intent:* """Attempt to compute self**other exactly. Given Decimals self and other and an integer p, attempt t...
  * `__new__` **(Stateful Encapsulated Methods)** (Impact: 101.5)
    * *Intent:* # Generally, the value of the Decimal instance is given by # (-1)**_sign * _int * 10**_exp # Special...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 78.0)
  * `__format__` **(Many-Argument Workhorses)** (Impact: 73.6)
    * *Intent:* # PEP 3101 support. the _localeconv keyword argument should be # considered private: it's provided f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 750 instances
* *State Mutation (weighted view):* 2385
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1019`, `structural_boundaries: 896`, `args: 241`, `func_start: 240`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 885`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 4`, `api: 177`, `import: 9`
* *Defense:* `safety: 43`, `doc: 226`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.45
  * `Choke Point (Betweenness):` 0.000111 | `Ripple Effect (Closeness):` 0.087401
  * `Imports (Out-Degree: 8):` collections, contextvars, itertools, locale, math, numbers, re, sys...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `Objects/dictobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.022)
- **Top Global Matches:** file_cluster_4: 10.022, file_cluster_12: 11.436, file_cluster_16: 12.467
- **Magnitude:** 5318.76 | **LOC:** 8326 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 61.1%
- **Blast Radius:** changing it is visible to **125** in-repo importer(s); it depends on **19**; blast radius 1.241; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.1%)
- **Documentation Coverage:** 49.5807% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dictiter_iternextitem` **(Stateful Encapsulated Methods)** (Impact: 429.6)
  * `_PyDict_FromKeys` **(Many-Argument Workhorses)** (Impact: 74.8)
    * *Intent:* /* Internal version of dict.from_keys(). It is subclass-friendly. */
  * `dict_setdefault_ref_lock_held` **(Many-Argument Workhorses)** (Impact: 73.6)
  * `dictresize` **(Many-Argument Workhorses)** (Impact: 63.5)
    * *Intent:* */
  * `store_instance_attr_lock_held` **(Many-Argument Workhorses)** (Impact: 56.3)
    * *Intent:* // Called with either the object's lock or the dict's lock held // depending on whether or not a dic...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 575 instances
* *State Mutation (weighted view):* 1793
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1061`, `structural_boundaries: 708`, `args: 466`, `func_start: 282`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `state_mutation: 643`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 4`, `unreferenced_by_name: 70`
* *Architecture:* `api: 97`, `import: 19`
* *Defense:* `safety: 278`, `doc: 5`, `test: 60`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.241
  * `Choke Point (Betweenness):` 0.000374 | `Ripple Effect (Closeness):` 0.089665
  * `Imports (Out-Degree: 47):` Python.h, dictobject.c.h, pycore_bitutils.h, pycore_call.h, pycore_ceval.h, pycore_code.h, pycore_critical_section.h, pycore_dict.h...
  * `Imported By (In-Degree: 125):` (Excluded from Brief to save tokens)

### `Lib/test/test_asyncio/test_locks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.665)
- **Top Global Matches:** file_cluster_12: 7.665, file_cluster_7: 9.859, file_cluster_15: 10.525
- **Magnitude:** 5305.64 | **LOC:** 1826 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (49.6%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_repr` **(Compute Cores)** (Impact: 16.6)
  * `test_repr` **(Compute Cores)** (Impact: 9.5)
  * `test_repr` **(Compute Cores)** (Impact: 9.1)
  * `test_wait` **(Compute Cores)** (Impact: 8.8)
  * `test_acquire` **(Compute Cores)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 679 instances
* *Amplified Cascading Flux:* 90 instances
* *Concurrency (weighted view):* 4183
* *State Mutation (weighted view):* 502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 506`, `args: 152`, `func_start: 142`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 322`, `duplicate_logic: 16`, `unreferenced_by_name: 57`
* *Architecture:* `api: 145`, `concurrency: 788`, `import: 5`
* *Defense:* `safety: 31`, `doc: 1`, `test: 88`, `sync_locks: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` asyncio, collections, re, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Lib/http/server.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.637)
- **Top Global Matches:** file_cluster_12: 5.637, file_cluster_2: 5.711, file_cluster_17: 6.426
- **Magnitude:** 5276.76 | **LOC:** 1092 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **19**; blast radius 0.111; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.7%), Connectivity (formerly Api Exposure) (50.9%), Debt Markers (formerly Tech Debt) (36.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 98`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 41`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 17`, `api: 18`, `import: 19`
* *Defense:* `safety: 15`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.000242 | `Ripple Effect (Closeness):` 0.076117
  * `Imports (Out-Degree: 16):` argparse, contextlib, datetime, email.utils, html, http, http.client, io...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `Modules/clinic/posixmodule.c.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.338)
- **Top Global Matches:** file_cluster_16: 7.338, file_cluster_4: 8.318, file_cluster_17: 9.899
- **Magnitude:** 5225.86 | **LOC:** 13615 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.5%), Complexity Load (formerly Cognitive Load) (41.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `os_posix_spawn` **(Many-Argument Workhorses)** (Impact: 47.9)
  * `os_posix_spawnp` **(Many-Argument Workhorses)** (Impact: 47.9)
  * `os_sendfile` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `os_timerfd_settime` **(Stateful Encapsulated Methods)** (Impact: 47.0)
  * `os_startfile` **(Many-Argument Workhorses)** (Impact: 45.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 624 instances
* *State Mutation (weighted view):* 2062
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 962`, `structural_boundaries: 359`, `args: 932`, `func_start: 229`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 12`, `state_mutation: 814`
* *Architecture:* `io: 12`, `api: 1`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 358`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.050291
  * `Imports (Out-Degree: 22):` pycore_abstract.h, pycore_gc.h, pycore_long.h, pycore_modsupport.h, pycore_runtime.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Lib/test/test_asyncio/test_tasks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.5)
- **Top Global Matches:** file_cluster_12: 7.5, file_cluster_15: 8.799, file_cluster_11: 9.02
- **Magnitude:** 5118.28 | **LOC:** 3753 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (47.8%), Connectivity (formerly Api Exposure) (14.7%)
- **Documentation Coverage:** 97.8261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_as_completed_resume_iterator` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* # Test that as_completed returns an iterator that can be resumed # the next time iteration is perfor...
  * `format_coroutine` **(Many-Argument Workhorses)** (Impact: 12.8)
  * `test_as_completed` **(Compute Cores)** (Impact: 12.2)
  * `test_uncancel_structured_blocks` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* # This test recreates the following high-level structure using uncancel():: # # async def make_reque...
  * `make_request_with_timeout` **(Defensive Guards)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 418 instances
* *Amplified Cascading Flux:* 100 instances
* *Concurrency (weighted view):* 2785
* *State Mutation (weighted view):* 897
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 876`, `args: 425`, `func_start: 417`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 697`, `dead_code: 1`, `duplicate_logic: 60`, `unreferenced_by_name: 171`
* *Architecture:* `io: 2`, `api: 444`, `concurrency: 695`, `import: 24`
* *Defense:* `safety: 90`, `doc: 12`, `test: 228`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` _asyncio, _functools, _json, _pickle, asyncio, asyncio.coroutines, collections, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Lib/test/test_capi/test_opt.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.473)
- **Top Global Matches:** file_cluster_12: 6.473, file_cluster_15: 6.926, file_cluster_11: 8.721
- **Magnitude:** 4825.8 | **LOC:** 4774 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 24.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (97.5%), Guard Balance (formerly Safety Score) (75.0%), Complexity Load (formerly Cognitive Load) (29.5%), Connectivity (formerly Api Exposure) (14.6%)
- **Documentation Coverage:** 98.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_invalidate_object` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* # Generate a new set of functions at each call ns = {} func_src = "\n".join( f"""
  * `test_143092` **(Compute Cores)** (Impact: 14.8)
  * `test_executor_side_exits_create_another_executor` **(Compute Cores)** (Impact: 14.4)
  * `test_combine_stack_space_checks_large_framesize` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* # Create a function with a large framesize. This ensures _CHECK_STACK_SPACE is # actually doing its ...
  * `test_int_type_propagation_through_frame` **(Compute Cores)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 616 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 2085
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 885`, `args: 539`, `func_start: 539`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 8`, `state_mutation: 853`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 40`, `unreferenced_by_name: 237`
* *Architecture:* `io: 9`, `api: 503`, `import: 12`
* *Defense:* `safety: 21`, `doc: 25`, `test: 254`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` _opcode, _testinternalcapi, contextlib, gc, itertools, math, os, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Lib/test/datetimetester.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.099)
- **Top Global Matches:** file_cluster_15: 7.099, file_cluster_12: 7.393, file_cluster_10: 8.765
- **Magnitude:** 4732.02 | **LOC:** 7510 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **27**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.1%), Complexity Load (formerly Cognitive Load) (41.2%), Connectivity (formerly Api Exposure) (13.7%)
- **Documentation Coverage:** 98.138% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dst` **(Defensive Guards)** (Impact: 27.5)
  * `test_aware_compare` **(Compute Cores)** (Impact: 24.9)
  * `test_aware_subtract` **(Compute Cores)** (Impact: 21.9)
  * `stats` **(Compute Cores)** (Impact: 21.4)
  * `checkinside` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* # Check a time that's inside DST.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 484 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 2361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 473`, `structural_boundaries: 1004`, `args: 554`, `func_start: 456`, `class_start: 106`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 8`, `state_mutation: 1393`, `planned_debt: 1`, `fragile_debt: 10`, `duplicate_logic: 50`, `unreferenced_by_name: 186`
* *Architecture:* `io: 11`, `api: 504`, `import: 44`
* *Defense:* `safety: 64`, `doc: 17`, `test: 345`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000262
  * `Imports (Out-Degree: 30):` _datetime, _interpreters, _pydatetime, _strptime, _testcapi, array, bisect, contextlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Lib/test/test_enum.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.82)
- **Top Global Matches:** file_cluster_12: 7.82, file_cluster_15: 8.843, file_cluster_16: 9.453
- **Magnitude:** 4538.56 | **LOC:** 5574 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (44.5%), Connectivity (formerly Api Exposure) (14.5%), Concurrency Surface (formerly Concurrency) (14.4%)
- **Documentation Coverage:** 98.4694% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setUp` **(C Struct Operations)** (Impact: 35.1)
  * `test_basics` **(Defensive Guards)** (Impact: 18.8)
  * `test_inspect_classify_class_attrs` **(Compute Cores)** (Impact: 17.3)
    * *Intent:* # indirectly test __objclass__ from inspect import Attribute values = [ Attribute(name='__class__', ...
  * `member_dir` **(Defensive Guards)** (Impact: 16.4)
  * `__new__` **(Defensive Guards)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 342 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 2124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 1377`, `args: 476`, `func_start: 467`, `class_start: 434`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 2`, `state_mutation: 1440`, `dead_code: 1`, `duplicate_logic: 113`, `unreferenced_by_name: 209`
* *Architecture:* `io: 9`, `api: 743`, `concurrency: 3`, `import: 35`
* *Defense:* `safety: 75`, `doc: 14`, `test: 357`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` builtins, collections, copy, dataclasses, datetime, doctest, enum, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Lib/test/test_patma.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.611)
- **Top Global Matches:** file_cluster_12: 6.611, file_cluster_15: 6.907, file_cluster_11: 8.737
- **Magnitude:** 4491.54 | **LOC:** 3560 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.071; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.8%), Complexity Load (formerly Cognitive Load) (31.5%), Connectivity (formerly Api Exposure) (14.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_patma_protocol_with_match_args` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* # Runtime-checkable protocol with `__match_args__` from typing import Protocol, runtime_checkable # ...
  * `test_patma_174` **(Compute Cores)** (Impact: 18.1)
  * `test_patma_182` **(Compute Cores)** (Impact: 16.6)
  * `test_patma_177` **(Compute Cores)** (Impact: 13.8)
  * `http_error` **(Compute Cores)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 642 instances
* *State Mutation (weighted view):* 1953
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 796`, `structural_boundaries: 709`, `args: 399`, `func_start: 399`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 3`, `state_mutation: 669`, `fragile_debt: 8`, `duplicate_logic: 7`, `unreferenced_by_name: 330`
* *Architecture:* `io: 4`, `api: 397`, `import: 15`
* *Defense:* `safety: 4`, `doc: 49`, `test: 345`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000349
  * `Imports (Out-Degree: 10):` array, collections, dataclasses, dis, enum, inspect, pyperf, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Modules/_ssl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.806)
- **Top Global Matches:** file_cluster_4: 5.806, file_cluster_6: 8.481, file_cluster_16: 12.102
- **Magnitude:** 4240.8 | **LOC:** 7422 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 36.4%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (73.6%), Guard Balance (formerly Safety Score) (66.2%), Debt Markers (formerly Tech Debt) (57.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fill_and_set_sslerror` **(Many-Argument Workhorses)** (Impact: 129.3)
  * `_get_peer_alt_names` **(Many-Argument Workhorses)** (Impact: 110.0)
  * `newPySSLSocket` **(Many-Argument Workhorses)** (Impact: 91.1)
  * `_ssl__SSLSocket_read_impl` **(Many-Argument Workhorses)** (Impact: 84.7)
  * `_ssl__SSLContext_load_verify_locations_impl` **(Many-Argument Workhorses)** (Impact: 79.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 582 instances
* *State Mutation (weighted view):* 1805
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 915`, `structural_boundaries: 540`, `args: 435`, `func_start: 159`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 641`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 94`
* *Architecture:* `io: 1`, `api: 21`, `import: 28`
* *Defense:* `safety: 32`, `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000589
  * `Imports (Out-Degree: 48):` Python.h, _ssl.h, cert.c, debughelpers.c, misc.c, _ssl_data_111.h, _ssl_data_300.h, _ssl_data_340.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Lib/test/test_buffer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.378)
- **Top Global Matches:** file_cluster_12: 7.378, file_cluster_4: 9.324, file_cluster_15: 10.064
- **Magnitude:** 4237.16 | **LOC:** 4873 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.4%), Complexity Load (formerly Cognitive Load) (39.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.8%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 77.6204% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify` **(Many-Argument Workhorses)** (Impact: 215.7)
  * `verify_getbuf` **(Many-Argument Workhorses)** (Impact: 100.3)
  * `rand_structure` **(Many-Argument Workhorses)** (Impact: 79.0)
    * *Intent:* """Return random structure: (memlen, itemsize, ndim, shape, strides, offset) If 'valid' is true, the...
  * `test_py_buffer_to_contiguous` **(Many-Argument Workhorses)** (Impact: 65.7)
    * *Intent:* # The requests are used in _testbuffer.c:py_buffer_to_contiguous # to generate buffers without full ...
  * `test_ndarray_getbuf` **(Compute Cores)** (Impact: 53.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 560 instances
* *State Mutation (weighted view):* 2402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 579`, `structural_boundaries: 517`, `args: 196`, `func_start: 192`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 102`, `high_risk_execution: 4`, `state_mutation: 1282`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 14`, `unreferenced_by_name: 101`
* *Architecture:* `io: 14`, `api: 167`, `import: 18`
* *Defense:* `safety: 55`, `doc: 41`, `test: 111`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` _testbuffer, _testcapi, array, contextlib, ctypes, decimal, fractions, inspect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Lib/test/test_descr.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.6)
- **Top Global Matches:** file_cluster_12: 8.6, file_cluster_7: 8.955, file_cluster_5: 9.813
- **Magnitude:** 4161.38 | **LOC:** 6277 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.4%), Complexity Load (formerly Cognitive Load) (45.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.1%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 97.3975% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_reduce` **(Compute Cores)** (Impact: 40.0)
  * `_check_reduce` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `test_rich_comparisons` **(Defensive Guards)** (Impact: 36.3)
    * *Intent:* # Testing rich comparisons... class Z(complex): pass z = Z(1) self.assertEqual(z, 1+0j) self.assertE...
  * `test_classic_comparisons` **(Defensive Guards)** (Impact: 35.7)
    * *Intent:* # Testing classic comparisons... class classic: pass for base in (classic, int, object): class C(bas...
  * `test_metaclass` **(C Struct Operations)** (Impact: 32.6)
    * *Intent:* # Testing metaclasses... class C(metaclass=type): def __init__(self): self.__state = 0 def getstate(...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 290 instances
* *High Risk Execution (weighted view):* 17
* *State Mutation (weighted view):* 1576
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 2163`, `args: 560`, `func_start: 543`, `class_start: 545`
* *Risk/State:* `safety_bypasses: 365`, `high_risk_execution: 25`, `state_mutation: 996`, `dead_code: 8`, `fragile_debt: 23`, `duplicate_logic: 59`, `unreferenced_by_name: 165`
* *Architecture:* `io: 24`, `api: 515`, `import: 37`
* *Defense:* `safety: 198`, `doc: 18`, `test: 199`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000262
  * `Imports (Out-Degree: 24):` _io, _testcapi, abc, binascii, builtins, collections, contextlib, copy...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Modules/_datetimemodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.858)
- **Top Global Matches:** file_cluster_4: 7.858, file_cluster_16: 8.791, file_cluster_12: 8.975
- **Magnitude:** 4094.6 | **LOC:** 7910 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.086; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.0%), Complexity Load (formerly Cognitive Load) (59.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap_strftime` **(Many-Argument Workhorses)** (Impact: 123.2)
    * *Intent:* /* I sure don't want to reproduce the strftime code from the time module, * so this imports the modu...
  * `datetime_richcompare` **(Many-Argument Workhorses)** (Impact: 62.0)
  * `parse_hh_mm_ss_ff` **(Many-Argument Workhorses)** (Impact: 56.5)
  * `parse_isoformat_time` **(Many-Argument Workhorses)** (Impact: 54.5)
  * `datetime_datetime_fromisoformat_impl` **(Many-Argument Workhorses)** (Impact: 49.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 484 instances
* *State Mutation (weighted view):* 1493
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 903`, `structural_boundaries: 617`, `args: 461`, `func_start: 249`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 525`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 6`, `unreferenced_by_name: 35`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 102`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.086
  * `Choke Point (Betweenness):` 0.000106 | `Ripple Effect (Closeness):` 0.059902
  * `Imports (Out-Degree: 40):` Python.h, _datetimemodule.c.h, datetime.h, pycore_initconfig.h, pycore_long.h, pycore_object.h, pycore_pyatomic_ft_wrappers.h, pycore_time.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Tools/jit/_llvm.py` (PYTHON) | Magnitude: 0.26 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 46, core_var_decl: 38, design_snake_case: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `Lib/test/test_free_threading/test_frame.py` (PYTHON) | Magnitude: 159.48 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 42, args: 40, api: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Modules/_decimal/tests/bench.py` (PYTHON) | Magnitude: 121.1 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 95, core_var_decl: 38, design_snake_case: 34, state_mutation: 32
- `Lib/test/support/_hypothesis_stubs/strategies.py` (PYTHON) | Magnitude: 37.74 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 22, api: 10, args: 9
- `Lib/test/test_concurrent_futures/test_wait.py` (PYTHON) | Magnitude: 87.96 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 154, core_var_decl: 44, design_snake_case: 44, structural_boundaries: 28
- `Lib/encodings/charmap.py` (PYTHON) | Magnitude: 35.66 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 20, core_var_decl: 13, design_snake_case: 13
- `Lib/test/test_gdb/test_misc.py` (PYTHON) | Magnitude: 73.42 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 43, core_var_decl: 31, test: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Lib/test/test_interpreters/test_queues.py` (PYTHON) | Magnitude: 435.72 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 449, state_mutation: 139, core_var_decl: 121, structural_boundaries: 120
- `Modules/_io/_iomodule.h` (C) | Magnitude: 41.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: pointers: 49, macros: 36, api: 34, indent_spaces: 32
- `Lib/test/test_sqlite3/test_dbapi.py` (PYTHON) | Magnitude: 1130.92 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1526, structural_boundaries: 551, args: 267, state_mutation: 248
- `Lib/test/test_site.py` (PYTHON) | Magnitude: 645.06 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 658, structural_boundaries: 189, state_mutation: 181, core_var_decl: 178
- `Include/cpython/pyerrors.h` (C) | Magnitude: 28.98 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 59, pointers: 42, structural_boundaries: 27, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Lib/test/test_atexit.py` (PYTHON) | Magnitude: 60.68 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 33, core_var_decl: 26, design_snake_case: 26
- `Lib/idlelib/idle_test/test_autocomplete_w.py` (PYTHON) | Magnitude: 12.36 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 13, test: 5, api: 4
- `Lib/idlelib/idle_test/test_calltip_w.py` (PYTHON) | Magnitude: 12.24 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 12, test: 5, api: 4
- `Lib/importlib/metadata/_collections.py` (PYTHON) | Magnitude: 11.36 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, api: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `Lib/test/test_inspect/inspect_stock_annotations.py` (PYTHON) | Magnitude: 29.78 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 11, args: 6, func_start: 6
- `Lib/test/test_opcodes.py` (PYTHON) | Magnitude: 79.1 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 48, args: 26, state_mutation: 25
- `Lib/test/test_ctypes/test_cast.py` (PYTHON) | Magnitude: 68.92 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 20, core_var_decl: 16, design_snake_case: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Modules/_testcapi/run.c` (C) | Magnitude: 60.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 75, pointers: 32, branch: 14, core_var_decl: 12
- `Modules/tkappinit.c` (C) | Magnitude: 22.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 35, args: 11, api: 8, structural_boundaries: 7
- `Lib/turtledemo/fractalcurves.py` (PYTHON) | Magnitude: 38.86 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 14, core_var_decl: 9, design_snake_case: 9
- `Modules/_testinternalcapi/tuple.c` (C) | Magnitude: 11.3 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 14, pointers: 13, structural_boundaries: 5, args: 4
- `Lib/idlelib/idle_test/test_debugger.py` (PYTHON) | Magnitude: 158.12 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 183, structural_boundaries: 68, state_mutation: 57, test: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Lib/asyncio/subprocess.py` (PYTHON) | Magnitude: 327.64 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 173, state_mutation: 60, structural_boundaries: 54, core_var_decl: 51
- `Modules/_testcapi/float.c` (C) | Magnitude: 68.72 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 20, branch: 16, args: 12
- `Modules/clinic/timemodule.c.h` (C) | Magnitude: 15.44 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 18, macros: 10, pointers: 10, args: 7
- `Lib/symtable.py` (PYTHON) | Magnitude: 431.84 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 246, structural_boundaries: 147, state_mutation: 74, branch: 65
- `PC/clinic/_wmimodule.cpp.h` (C) | Magnitude: 18.42 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 40, pointers: 15, macros: 11, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Include/sliceobject.h` (C) | Magnitude: 16.88 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 17, args: 16, macros: 16, indent_spaces: 12
- `Platforms/emscripten/web_example_pyrepl_jspi/index.html` (HTML) | Magnitude: 16.62 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 28, class_start: 8, structural_boundaries: 4, immutability_locks: 4
- `Python/mysnprintf.c` (C) | Magnitude: 26.68 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, safety: 6, pointers: 6, state_mutation: 5
- `Include/cpython/listobject.h` (C) | Magnitude: 6.82 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: pointers: 12, indent_spaces: 12, args: 10, macros: 8
- `Include/internal/pycore_weakref.h` (C) | Magnitude: 31.96 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, macros: 25, pointers: 22, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Lib/test/test_flufl.py` (PYTHON) | Magnitude: 18.06 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 25, high_risk_execution: 8, test: 8
- `Lib/test/test_import/data/double_const.py` (PYTHON) | Magnitude: 15.18 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 6, indent_spaces: 6, core_var_decl: 6, structural_boundaries: 5
- `Lib/test/test_lazy_import/data/global_filter.py` (PYTHON) | Magnitude: 3.34 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 3, safety: 2, args: 1
- `Lib/test/test_lazy_import/data/global_filter_from.py` (PYTHON) | Magnitude: 3.36 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 4, safety: 3, args: 1
- `Modules/_decimal/libmpdec/examples/sqrt.c` (C) | Magnitude: 19.1 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 26, pointers: 8, state_mutation: 6, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Lib/xml/etree/ElementTree.py` (PYTHON) | Magnitude: 2080.16 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1159, branch: 367, state_mutation: 323, structural_boundaries: 300
- `Platforms/Apple/__main__.py` (PYTHON) | Magnitude: 618.62 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 711, core_var_decl: 156, branch: 149, design_snake_case: 141
- `Lib/test/test_profiling/test_sampling_profiler/test_profiler.py` (PYTHON) | Magnitude: 279.24 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 491, structural_boundaries: 112, core_var_decl: 105, design_snake_case: 105
- `Lib/_pyio.py` (PYTHON) | Magnitude: 2513.6 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1607, structural_boundaries: 480, branch: 455, state_mutation: 360
- `Tools/cases_generator/generators_common.py` (PYTHON) | Magnitude: 0.67 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 694, structural_boundaries: 135, branch: 109, state_mutation: 96

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `Lib/_pyrepl/windows_console.py` (PYTHON) | Magnitude: 590.22 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 444, state_mutation: 149, core_var_decl: 109, structural_boundaries: 108
- `Lib/test/libregrtest/logger.py` (PYTHON) | Magnitude: 97.34 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 28, state_mutation: 20, core_var_decl: 19
- `Lib/test/test_tomllib/burntsushi.py` (PYTHON) | Magnitude: 115.22 | Delta: **0.16** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 38, branch: 35, core_var_decl: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `Python/modsupport.c` (C) | Magnitude: 593.78 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 571, branch: 160, pointers: 140, structural_boundaries: 108
- `Lib/fnmatch.py` (PYTHON) | Magnitude: 268.86 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 116, branch: 53, state_mutation: 51, core_var_decl: 47
- `Tools/peg_generator/pegen/grammar_parser.py` (PYTHON) | Magnitude: 0.9 | Delta: **0.149** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 642, state_mutation: 189, branch: 165, structural_boundaries: 135

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Lib/idlelib/pathbrowser.py` (PYTHON) | Magnitude: 122.18 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 34, state_mutation: 28, core_var_decl: 19
- `Lib/test/test_unittest/testmock/testcallable.py` (PYTHON) | Magnitude: 70.42 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 35, test: 26, state_mutation: 20
- `Mac/PythonLauncher/MyDocument.m` (OBJECTIVE-C) | Magnitude: 107.3 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 68, explicit_casts: 36, func_start: 26, state_mutation: 24
- `Makefile.pre.in` (MAKEFILE) | Magnitude: 643.0 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 1886, structural_boundaries: 336, core_var_decl: 328, design_upper_case: 268
- `Modules/clinic/_randommodule.c.h` (C) | Magnitude: 33.42 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 42, pointers: 30, args: 10, encapsulation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Modules/_zstd/clinic/decompressor.c.h` (C) | Magnitude: 77.4 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 110, pointers: 49, macros: 32, core_var_decl: 19
- `Tools/cases_generator/parser.py` (PYTHON) | Magnitude: 0.06 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 14, structural_boundaries: 13, branch: 10
- `Modules/clinic/overlapped.c.h` (C) | Magnitude: 639.78 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 632, pointers: 214, branch: 148, panics_and_aborts: 124

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Python/optimizer_bytecodes.c` -> Churn: **96.06%** | Cog Load: 72.1594% | Debt: 7.9832%
- `Python/ceval.c` -> Churn: **82.31%** | Cog Load: 79.7832% | Debt: 8.9655%
- `Python/optimizer.c` -> Churn: **79.33%** | Cog Load: 65.632% | Debt: 8.4029%
- `Objects/dictobject.c` -> Churn: **78.07%** | Cog Load: 79.2414% | Debt: 32.9913%
- `Python/optimizer_analysis.c` -> Churn: **72.81%** | Cog Load: 55.8044% | Debt: 10.1514%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Lib/http/server.py` -> **Hugo van Kemenade** (100.0% isolated ownership) | Magnitude: 5276.76
- `Lib/test/test_enum.py` -> **Ethan Furman** (100.0% isolated ownership) | Magnitude: 4538.56
- `Lib/test/test_decimal.py` -> **Sergey B Kirpichev** (100.0% isolated ownership) | Magnitude: 3627.42
- `Python/dtoa.c` -> **Sergey B Kirpichev** (100.0% isolated ownership) | Magnitude: 3360.56
- `Lib/turtle.py` -> **Victor Stinner** (100.0% isolated ownership) | Magnitude: 2994.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Lib/importlib/_bootstrap_external.py` -> **Severity: 0.621** (Bridge: 0.0062 * Flux: 100.0%)
- `Lib/doctest.py` -> **Severity: 0.555** (Bridge: 0.0056 * Flux: 100.0%)
- `Lib/traceback.py` -> **Severity: 0.529** (Bridge: 0.0053 * Flux: 100.0%)
- `Lib/heapq.py` -> **Severity: 0.525** (Bridge: 0.0053 * Flux: 100.0%)
- `Objects/object.c` -> **Severity: 0.495** (Bridge: 0.005 * Flux: 98.1861%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Lib/os.py` -> **Severity: 18.198** (Embedded: 0.2447 * Error Risk: 74.382%)
- `Lib/re/__init__.py` -> **Severity: 17.776** (Embedded: 0.2335 * Error Risk: 76.1204%)
- `Lib/functools.py` -> **Severity: 17.389** (Embedded: 0.2223 * Error Risk: 78.2299%)
- `Lib/types.py` -> **Severity: 17.083** (Embedded: 0.2265 * Error Risk: 75.4109%)
- `Lib/inspect.py` -> **Severity: 16.718** (Embedded: 0.2032 * Error Risk: 82.2606%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Lib/warnings.py` -> **Severity: 3360.6** (Blast Radius: 33.606 * Doc Risk: 100.0%)
- `Lib/functools.py` -> **Severity: 2712.462** (Blast Radius: 35.025 * Doc Risk: 77.4436%)
- `Lib/types.py` -> **Severity: 2557.801** (Blast Radius: 32.364 * Doc Risk: 79.0323%)
- `Lib/_py_warnings.py` -> **Severity: 2351.916** (Blast Radius: 28.559 * Doc Risk: 82.3529%)
- `Lib/_collections_abc.py` -> **Severity: 1745.789** (Blast Radius: 24.075 * Doc Risk: 72.5146%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 3846 literal sites + 81 sites through wrappers = 3927
- **`memory_alloc`:** 241 literal sites + 2161 sites through wrappers = 2402
- **`panics_and_aborts`:** 22168 literal sites + 235 sites through wrappers = 22403

- `PyMem_Free` (function, memory_alloc, primitive): 792 call sites in 141 files -- `Objects/obmalloc.c`
- `PyMem_Malloc` (function, memory_alloc, primitive): 245 call sites in 92 files -- `Objects/obmalloc.c`
- `PyMem_RawFree` (function, memory_alloc, primitive): 205 call sites in 45 files -- `Objects/obmalloc.c`
- `path_cleanup` (function, memory_alloc, via PyMem_Free): 68 call sites in 2 files -- `Modules/posixmodule.c`
- `PyMem_New` (macro, memory_alloc, via PyMem_Malloc): 62 call sites in 23 files -- `Include/pymem.h`
- `PyMem_Realloc` (function, memory_alloc, primitive): 44 call sites in 35 files -- `Objects/obmalloc.c`
- `PyMem_Calloc` (function, memory_alloc, primitive): 41 call sites in 24 files -- `Objects/obmalloc.c`
- `PyObject_New` (macro, memory_alloc, via _PyObject_New): 37 call sites in 21 files -- `Include/objimpl.h`
- `PyMem_NEW` (macro, memory_alloc, via PyMem_New): 35 call sites in 16 files -- `Include/pymem.h`
- `PyObject_Free` (function, memory_alloc, primitive): 35 call sites in 20 files -- `Objects/obmalloc.c`
- `CLEAR` (macro, memory_alloc, via PyMem_RawFree): 34 call sites in 3 files -- `Programs/_bootstrap_python.c`
- `PyMem_RawCalloc` (function, memory_alloc, primitive): 24 call sites in 12 files -- `Objects/obmalloc.c`
*(+258 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 342415 call pairs -- scoped 44.9%, unique 14.3%, ambiguous 16.1%, external 24.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 236237 | 56.3% | 0.0% | 22.9% | 20.8% |
| c | 104418 | 19.5% | 46.9% | 0.9% | 32.6% |
| javascript | 504 | 19.0% | 0.0% | 2.8% | 78.2% |
| cpp | 334 | 8.7% | 21.0% | 1.5% | 68.9% |
| m4 | 249 | 7.2% | 1.2% | 0.0% | 91.6% |
| objective-c | 249 | 29.7% | 10.0% | 5.2% | 55.0% |
| shell | 228 | 5.7% | 0.0% | 0.0% | 94.3% |
| html | 149 | 0.7% | 0.0% | 0.0% | 99.3% |
| kotlin | 45 | 15.6% | 2.2% | 0.0% | 82.2% |
| powershell | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
