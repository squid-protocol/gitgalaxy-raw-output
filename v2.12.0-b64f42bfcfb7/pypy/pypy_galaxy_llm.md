# ARCHITECTURAL_BRIEF: pypy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pypy/pypy.git` |
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
- **Scope:** 4996 analyzed artifact(s), 1026964 LOC.
- **Load-bearing artifact:** `lib-python/2.7/os.py` -- 930 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pypy/module/imp/test/test_import.py` -- pulls in 86 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `rpython/jit/metainterp/test/test_ajit.py` at magnitude 5870.56 (structural weight, not risk).
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
| Total Artifacts | 6000 |
| Analyzed Artifacts (Scanned) | 4996 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1004 |
| Total LOC | 1026964 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5618 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1338 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 7.0115 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 247 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 4405 | 971084 | 88.2% |
| C | 285 | 46323 | 5.7% |
| PLAINTEXT | 174 | 0 | 3.5% |
| CPP | 39 | 4936 | 0.8% |
| SHELL | 24 | 131 | 0.5% |
| MARKDOWN | 20 | 0 | 0.4% |
| XML | 17 | 0 | 0.3% |
| MAKEFILE | 13 | 2198 | 0.3% |
| BATCH | 5 | 391 | 0.1% |
| YAML | 4 | 185 | 0.1% |
| HTML | 3 | 969 | 0.1% |
| JSON | 2 | 2 | 0.0% |
| M4 | 2 | 599 | 0.0% |
| ASSEMBLY | 2 | 97 | 0.0% |
| CSS | 1 | 49 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 37 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 4957 |
| cp1252 | cp1252-fallback | 29 |
| latin-1 | latin-1-fallback | 8 |
| utf-8 | bom | 2 |

> 3 guessed file(s) read as double-byte text that decodes strictly as gbk: if that is the estate's code page, rescan with `--source-encoding gbk` (or the right one of those). E.g. `lib-python/2.7/test/cjkencodings/gb2312.txt`, `lib-python/2.7/test/cjkencodings/gbk.txt`, `lib-python/2.7/test/test_shlex.py`.

> 1 guessed file(s) read as double-byte text that decodes strictly as big5: if that is the estate's code page, rescan with `--source-encoding big5` (or the right one of those). E.g. `lib-python/2.7/test/cjkencodings/big5.txt`.

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `lib-python/2.7/test/cjkencodings/euc_jp.txt`.

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk / euc_kr: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `lib-python/2.7/test/cjkencodings/euc_kr.txt`.

> 1 guessed file(s) read as double-byte text that decodes strictly as shift_jis / gbk: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `lib-python/2.7/test/cjkencodings/shift_jis.txt`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 26%, Large Core Modules (2) 19%, Data / Markup / Trivial 18%, Large Core Modules (3) 16%, Declarative / Non-Code 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4801 | 96.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 194 | 3.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1004*

**Composition by Extension & Reason:**
- `.rst`: 217x Excluded (Unsupported Extension: '.rst'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 183x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Lexical Monotony: High structural repetition detected in 2366 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 2215 LOC)
- `.py`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Excluded: Neighborhood Micro-Mass Limit Exceeded, 12x Excluded (Embedded Hex Payload: 1024 hex tokens in 699 LOC)
- `.dectest`: 143x Excluded (Unsupported Extension: '.decTest')
- `no_extension`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.benchmark_result')
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `.gif`: 11x Excluded (Explicitly Denied Extension: '.gif')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 23 LOC), 1x Excluded (Machine-Generated Source Code Signature: 16 LOC), 1x Excluded (Machine-Generated Source Code Signature: 29 LOC)
- `.dot`: 8x Excluded (Unsupported Extension: '.dot')
- `.0`: 7x Excluded (Unsupported Extension: '.0')
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 98 LOC), 1x Excluded (Embedded Array/Matrix Payload: 55661 commas in 4104 LOC), 1x Excluded (Embedded Array/Matrix Payload: 65036 commas in 2379 LOC)
- `.au`: 6x Excluded (Unsupported Extension: '.au')
- `.pem`: 6x Excluded (Unsupported Extension: '.pem')
- `.graffle`: 6x Excluded (Unsupported Extension: '.graffle')
- `.pdf`: 6x Excluded (Explicitly Denied Extension: '.pdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 31.8 | 29.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.4 | 54.9 | 58.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.6 | 10.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.6 | 9.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 49.4 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 17961 | 2091 | 8 | `extra_tests/cffi_tests/test_c.py` |
| cleanup | 3081 | 646 | 1 | `pypy/module/mmap/test/test_mmap.py` |
| guards | 97985 | 3265 | 48 | `pypy/module/micronumpy/test/test_ndarray.py` |
| danger | 39830 | 3234 | 21 | `extra_tests/cffi_tests/test_c.py` |
| concurrency | 2965 | 512 | 1 | `lib-python/2.7/test/test_multiprocessing.py` |
| connectivity | 95156 | 4155 | 51 | `rpython/annotator/test/test_annrpython.py` |
| io | 20575 | 1798 | 9 | `lib-python/2.7/test/test_socket.py` |
| crypto | 53 | 39 | 0 | `lib-python/2.7/test/test_httplib.py` |
| ipc | 927 | 141 | 0 | `lib-python/2.7/test/test_subprocess.py` |
| time | 1047 | 231 | 0 | `lib-python/2.7/test/test_datetime.py` |
| serialization | 233 | 84 | 0 | `pypy/interpreter/test/test_zzpickle_and_slow.py` |
| regex | 1662 | 275 | 0 | `lib-python/2.7/test/test_re.py` |
| events | 2778 | 335 | 0 | `lib-python/2.7/compiler/pycodegen.py` |
| tests | 34014 | 1730 | 17 | `extra_tests/cffi_tests/test_c.py` |
| docs | 21833 | 2477 | 10 | `rpython/jit/metainterp/optimizeopt/test/test_optimizeopt.py` |
| debt | 9546 | 1622 | 5 | `rpython/annotator/test/test_annrpython.py` |
| mutation | 510935 | 4063 | 269 | `lib-python/2.7/plat-mac/macerrors.py` |
| dead_code | 27211 | 2457 | 14 | `rpython/jit/metainterp/optimizeopt/test/test_optimizeopt.py` |
| credential | 23 | 20 | 0 | `extra_tests/test_string.py` |
| threat | 2966 | 128 | 0 | `rpython/rlib/unicodedata/unicodedb_3_2_0.py` |
| ml_ai | 991 | 86 | 0 | `pypy/module/micronumpy/test/test_ndarray.py` |
| ui | 60 | 24 | 0 | `lib-python/2.7/test/sgml_input.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.8333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib-python/2.7/test/test_socket.py` (Hits: 328)
- `pypy/module/posix/test/test_posix2.py` (Hits: 311)
- `lib-python/2.7/test/test_ssl.py` (Hits: 300)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **os.py** (`lib-python/2.7/os.py`) — 930 inbound connections
2. **__init__.py** (`py/__init__.py`) — 670 inbound connections
3. **__init__.py** (`rpython/rtyper/lltypesystem/__init__.py`) — 668 inbound connections
4. **__init__.py** (`lib-python/2.7/unittest/__init__.py`) — 586 inbound connections
5. **case.py** (`lib-python/2.7/unittest/case.py`) — 525 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_import.py** (`pypy/module/imp/test/test_import.py`) — 86 outbound dependencies
2. **test_sundry.py** (`lib-python/2.7/test/test_sundry.py`) — 65 outbound dependencies
3. **Python.h** (`pypy/module/cpyext/include/Python.h`) — 61 outbound dependencies
4. **api.py** (`pypy/module/cpyext/api.py`) — 52 outbound dependencies
5. **moduledef.py** (`pypy/module/cpyext/moduledef.py`) — 45 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Many-Argument Workhorses)** (@ `lib-python/2.7/test/regrtest.py`) -> Impact: **1147.3** | LOC: 746
- `convertsimple` **(Many-Argument Workhorses)** (@ `pypy/module/cpyext/src/getargs.c`) -> Impact: **655.7** | LOC: 783
  * *Intent:* */
- `__Py_dg_dtoa` **(Many-Argument Workhorses)** (@ `rpython/translator/c/src/dtoa.c`) -> Impact: **504.0** | LOC: 609
  * *Intent:* call to __Py_dg_freedtoa. */
- `__Py_dg_strtod` **(Many-Argument Workhorses)** (@ `rpython/translator/c/src/dtoa.c`) -> Impact: **361.5** | LOC: 753
- `make_formatting_class` **(Stateful Encapsulated Methods)** (@ `pypy/objspace/std/newformat.py`) -> Impact: **360.9** | LOC: 770
- `dispatch_bytecode` **(Many-Argument Workhorses)** (@ `pypy/interpreter/pyopcode.py`) -> Impact: **328.3** | LOC: 306
- `make_timsort_class` **(Many-Argument Workhorses)** (@ `rpython/rlib/listsort.py`) -> Impact: **300.7** | LOC: 625
- `llexternal` **(Many-Argument Workhorses)** (@ `rpython/rtyper/lltypesystem/rffi.py`) -> Impact: **277.1** | LOC: 275
- `__init__` **(Many-Argument Workhorses)** (@ `pypy/module/micronumpy/nditer.py`) -> Impact: **272.0** | LOC: 175
- `_parse` **(Many-Argument Workhorses)** (@ `lib-python/2.7/sre_parse.py`) -> Impact: **267.5** | LOC: 310
  * *Intent:* # parse a simple pattern subpattern = SubPattern(state) # precompute constants into local variables subpatternappend = subpattern.append sourceget = s...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib-python/2.7/test` | 476 | 114190.62 | 21.91% | 0.0% |
| `lib-python/2.7` | 200 | 101962.94 | 48.54% | 20.15% |
| `rpython/rlib` | 84 | 38808.24 | 57.39% | 26.87% |
| `rpython/jit/metainterp/test` | 55 | 28721.56 | 27.3% | 0.0% |
| `pypy/objspace/std` | 40 | 27882.58 | 60.47% | 18.28% |
| `pypy/module/micronumpy` | 27 | 20935.2 | 73.22% | 27.17% |
| `rpython/jit/metainterp` | 28 | 19234.82 | 58.92% | 10.4% |
| `lib-python/2.7/idlelib` | 74 | 17047.34 | 44.45% | 21.51% |
| `rpython/jit/metainterp/optimizeopt` | 26 | 16700.42 | 67.47% | 16.08% |
| `pypy/interpreter` | 30 | 16621.52 | 54.39% | 23.79% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `rpython/rlib/rvmprof/src/shared/libbacktrace/Makefile.am` -> **100.0%** Exposure
- `extra_tests/ctypes_tests/test_commethods.py` -> **100.0%** Exposure
- `extra_tests/test_json.py` -> **100.0%** Exposure
- `extra_tests/test_os.py` -> **100.0%** Exposure
- `extra_tests/test_pyrepl/test_basic.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `_pytest/_argcomplete.py` -> **100.0%** Exposure
- `_pytest/_code/_py2traceback.py` -> **100.0%** Exposure
- `_pytest/_code/code.py` -> **100.0%** Exposure
- `_pytest/_code/source.py` -> **100.0%** Exposure
- `_pytest/assertion/__init__.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `rpython/jit/metainterp/optimizeopt/test/test_optimizeopt.py` -> **416** Orphaned Functions | **6** Duplicates
- `lib-python/2.7/lib2to3/tests/test_fixers.py` -> **263** Orphaned Functions | **114** Duplicates
- `rpython/jit/metainterp/test/test_ajit.py` -> **225** Orphaned Functions | **95** Duplicates
- `pypy/module/micronumpy/test/test_ndarray.py` -> **290** Orphaned Functions | **2** Duplicates
- `extra_tests/cffi_tests/test_c.py` -> **231** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `lib_pypy/_cffi_ssl/_stdssl/certificate.py` -> **49.4048%** Exposure
- `lib-python/2.7/ssl.py` -> **47.9938%** Exposure
- `lib-python/2.7/test/test_smtplib.py` -> **26.5066%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `21` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24430` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `rpython/jit/metainterp/test/test_ajit.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.543)
- **Top Global Matches:** file_cluster_12: 7.543, file_cluster_7: 9.035, file_cluster_5: 9.889
- **Magnitude:** 5870.56 | **LOC:** 5055 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.072; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (73.3%), Complexity Load (formerly Cognitive Load) (30.5%), Connectivity (formerly Api Exposure) (13.7%), Dead Code Surface (formerly Dead Code) (5.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_cmp_fastpaths` **(Defensive Guards)** (Impact: 32.7)
  * `test_nested_retrace` **(Defensive Guards)** (Impact: 27.3)
  * `test_inputarg_reset_bug` **(Compute Cores)** (Impact: 26.2)
    * *Intent:* ## j = 0 ## while j < 100: ## j += 1 ## c = 0 ## j = 0 ## while j < 2: ## j += 1 ## if c == 0:...
  * `test_retrace_ending_up_retracing_another_loop` **(Defensive Guards)** (Impact: 22.8)
  * `make_int` **(Defensive Guards)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 702 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 1733`, `args: 697`, `func_start: 680`, `class_start: 140`
* *Risk/State:* `safety_bypasses: 218`, `high_risk_execution: 1`, `state_mutation: 1176`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 9`, `duplicate_logic: 95`, `unreferenced_by_name: 225`
* *Architecture:* `io: 30`, `api: 376`, `import: 57`
* *Defense:* `safety: 373`, `doc: 1`, `test: 225`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.072
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.0002
  * `Imports (Out-Degree: 20):` gc, math, py, pytest, rpython.jit.codewriter.policy, rpython.jit.metainterp, rpython.jit.metainterp.pyjitpl, rpython.jit.metainterp.test.support...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib-python/2.7/decimal.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.875)
- **Top Global Matches:** file_cluster_4: 4.875, file_cluster_16: 10.117, file_cluster_15: 10.215
- **Magnitude:** 5098.96 | **LOC:** 6222 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 0.127; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (49.9%)
- **Documentation Coverage:** 14.578% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__pow__` **(Many-Argument Workhorses)** (Impact: 122.6)
    * *Intent:* """Return self ** other [ % modulo]. With two arguments, compute self**other. With three arguments, ...
  * `_power_exact` **(Many-Argument Workhorses)** (Impact: 109.8)
    * *Intent:* """Attempt to compute self**other exactly. Given Decimals self and other and an integer p, attempt t...
  * `__new__` **(Stateful Encapsulated Methods)** (Impact: 95.2)
    * *Intent:* # Generally, the value of the Decimal instance is given by # (-1)**_sign * _int * 10**_exp # Special...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 78.1)
  * `quantize` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* """Quantize self so its exponent is the same as that of exp. Similar to self._rescale(exp._exp) but ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 728 instances
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 2306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 935`, `structural_boundaries: 868`, `args: 233`, `func_start: 232`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 850`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 173`, `concurrency: 10`, `import: 9`
* *Defense:* `safety: 39`, `doc: 221`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.001539
  * `Imports (Out-Degree: 6):` collections, doctest, itertools, locale, math, numbers, re, sys...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `rpython/annotator/test/test_annrpython.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.817)
- **Top Global Matches:** file_cluster_12: 6.817, file_cluster_7: 9.049, file_cluster_5: 9.787
- **Magnitude:** 4909.2 | **LOC:** 4842 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **28**; blast radius 0.462; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (87.3%), Guard Balance (formerly Safety Score) (57.5%), Complexity Load (formerly Cognitive Load) (42.2%)
- **Documentation Coverage:** 99.3478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `f` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `f` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `test_nonneg_cleverness` **(Defensive Guards)** (Impact: 15.0)
  * `test_general_nonneg_cleverness` **(Defensive Guards)** (Impact: 15.0)
  * `f` **(Compute Cores)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 382 instances
* *State Mutation (weighted view):* 2023
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 2333`, `args: 858`, `func_start: 854`, `class_start: 197`
* *Risk/State:* `safety_bypasses: 145`, `high_risk_execution: 6`, `state_mutation: 1259`, `fragile_debt: 5`, `duplicate_logic: 114`
* *Architecture:* `io: 2`, `api: 542`, `import: 41`
* *Defense:* `safety: 775`, `doc: 5`, `test: 329`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.462
  * `Choke Point (Betweenness):` 0.009937 | `Ripple Effect (Closeness):` 0.113227
  * `Imports (Out-Degree: 29):` __future__, collections, os, py.test, rpython.annotator, rpython.annotator.annrpython, rpython.annotator.classdesc, rpython.annotator.dictdef...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `rpython/jit/backend/test/runner_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.983)
- **Top Global Matches:** file_cluster_12: 7.983, file_cluster_4: 9.37, file_cluster_7: 10.142
- **Magnitude:** 4658.46 | **LOC:** 5486 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **39**; blast radius 0.184; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (90.5%), Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (34.9%)
- **Documentation Coverage:** 99.5146% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_call_release_gil_variable_function_and_arguments` **(Compute Cores)** (Impact: 61.3)
  * `nan_and_infinity` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `test_nan_and_infinity` **(Compute Cores)** (Impact: 38.6)
  * `test_floats_and_guards` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `test_jump` **(Defensive Guards)** (Impact: 37.1)
    * *Intent:* # this test generates small loops where the JUMP passes many # arguments of various types, shuffling...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 608 instances
* *State Mutation (weighted view):* 2983
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 487`, `structural_boundaries: 965`, `args: 224`, `func_start: 206`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 157`, `state_mutation: 1767`, `fragile_debt: 4`, `duplicate_logic: 6`
* *Architecture:* `io: 30`, `api: 213`, `import: 90`
* *Defense:* `safety: 523`, `doc: 78`, `test: 145`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.184
  * `Choke Point (Betweenness):` 0.000186 | `Ripple Effect (Closeness):` 0.00244
  * `Imports (Out-Degree: 38):` __future__, ctypes, gc, math, operator, os, py, random...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `rpython/rlib/parsing/pypackrat.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.958)
- **Top Global Matches:** file_cluster_6: 7.958, file_cluster_4: 12.504, file_cluster_8: 15.231
- **Magnitude:** 4598.58 | **LOC:** 3135 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 0.147; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.5%), Complexity Load (formerly Cognitive Load) (65.2%), Connectivity (formerly Api Exposure) (7.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_if_` **(Stateful Encapsulated Methods)** (Impact: 47.3)
  * `_enclosed` **(Stateful Encapsulated Methods)** (Impact: 41.6)
  * `_repetition` **(Stateful Encapsulated Methods)** (Impact: 41.0)
  * `_productionargs` **(Stateful Encapsulated Methods)** (Impact: 36.1)
  * `_arguments` **(Stateful Encapsulated Methods)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 862 instances
* *State Mutation (weighted view):* 3551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 466`, `structural_boundaries: 571`, `args: 73`, `func_start: 73`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 1827`
* *Architecture:* `api: 37`, `import: 2`
* *Defense:* `safety: 300`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.147
  * `Choke Point (Betweenness):` 0.000418 | `Ripple Effect (Closeness):` 0.075622
  * `Imports (Out-Degree: 2):` rpython.rlib.parsing.makepackrat, rpython.rlib.parsing.tree
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `rpython/jit/metainterp/pyjitpl.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.748)
- **Top Global Matches:** file_cluster_12: 7.748, file_cluster_15: 8.097, file_cluster_16: 8.177
- **Magnitude:** 4369.84 | **LOC:** 3900 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **31**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%)
- **Documentation Coverage:** 96.4657% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_residual_call` **(Many-Argument Workhorses)** (Impact: 99.9)
  * `_get_opimpl_method` **(Many-Argument Workhorses)** (Impact: 83.1)
    * *Intent:* # ____________________________________________________________
  * `handler` **(Many-Argument Workhorses)** (Impact: 80.8)
    * *Intent:* #
  * `get_list_of_active_boxes` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `_build_allboxes` **(Many-Argument Workhorses)** (Impact: 38.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 571 instances
* *Api Near Db Sink:* 26 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 2094
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 589`, `structural_boundaries: 746`, `args: 268`, `func_start: 268`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 5`, `state_mutation: 952`, `dead_code: 5`, `fragile_debt: 14`
* *Architecture:* `io: 3`, `api: 215`, `import: 49`
* *Defense:* `safety: 177`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.000907 | `Ripple Effect (Closeness):` 0.090301
  * `Imports (Out-Degree: 33):` __future__, py, rpython.config.translationoption, rpython.jit.backend.llsupport.ffisupport, rpython.jit.codewriter, rpython.jit.codewriter.effectinfo, rpython.jit.codewriter.jitcode, rpython.jit.codewriter.liveness...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `rpython/rlib/rbigint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.522)
- **Top Global Matches:** file_cluster_4: 5.522, file_cluster_16: 9.082, file_cluster_15: 9.267
- **Magnitude:** 4194.58 | **LOC:** 3668 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **10**; blast radius 0.898; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.3%)
- **Documentation Coverage:** 77.3852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pow` **(Many-Argument Workhorses)** (Impact: 80.8)
  * `_format_recursive` **(Many-Argument Workhorses)** (Impact: 65.4)
  * `_int_bitwise` **(Many-Argument Workhorses)** (Impact: 62.1)
    * *Intent:* """ Bitwise and/or/xor operations """
  * `_bitwise` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* """ Bitwise and/or/xor operations """
  * `tobytes` **(Many-Argument Workhorses)** (Impact: 61.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 748 instances
* *State Mutation (weighted view):* 2313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 632`, `args: 173`, `func_start: 173`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 817`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 5`, `api: 117`, `import: 17`
* *Defense:* `safety: 93`, `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.898
  * `Choke Point (Betweenness):` 0.000546 | `Ripple Effect (Closeness):` 0.149507
  * `Imports (Out-Degree: 9):` math, rpython.annotator, rpython.rlib, rpython.rlib.debug, rpython.rlib.objectmodel, rpython.rlib.rarithmetic, rpython.rlib.rstring, rpython.rtyper...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `rpython/translator/c/src/dtoa.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.862)
- **Top Global Matches:** file_cluster_6: 5.862, file_cluster_4: 9.744, file_cluster_8: 15.839
- **Magnitude:** 3501.04 | **LOC:** 3024 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.067; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.7%), Guard Balance (formerly Safety Score) (88.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__Py_dg_dtoa` **(Many-Argument Workhorses)** (Impact: 504.0)
    * *Intent:* call to __Py_dg_freedtoa. */
  * `__Py_dg_strtod` **(Many-Argument Workhorses)** (Impact: 361.5)
  * `bigcomp` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* Returns 0 on success, -1 on failure (e.g., due to a failed malloc call). */
  * `mult` **(Many-Argument Workhorses)** (Impact: 44.6)
    * *Intent:* /* multiply two Bigints. Returns a new Bigint, or NULL on failure. Ignores the signs of a and b. */...
  * `quorem` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* bits (28--31) are zero and bit 27 is set. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 701 instances
* *State Mutation (weighted view):* 2134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 560`, `structural_boundaries: 133`, `args: 58`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 732`, `dead_code: 2`, `fragile_debt: 9`, `unreferenced_by_name: 3`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` assert.h, errno.h, float.h, limits.h, asm.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib-python/2.7/test/test_descr.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.568)
- **Top Global Matches:** file_cluster_12: 8.568, file_cluster_7: 8.899, file_cluster_5: 9.833
- **Magnitude:** 3451.9 | **LOC:** 4984 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.11; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.1%), Complexity Load (formerly Cognitive Load) (46.8%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 99.4083% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_rich_comparisons` **(Defensive Guards)** (Impact: 36.5)
    * *Intent:* # Testing rich comparisons... class Z(complex): pass z = Z(1) self.assertEqual(z, 1+0j) self.assertE...
  * `test_basic_inheritance` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* # Testing inheritance from basic types... class hexint(int): def __repr__(self): return hex(self) de...
  * `test_set_class` **(Compute Cores)** (Impact: 26.5)
    * *Intent:* # Testing __class__ assignment... class C(object): pass class D(object): pass class E(object): pass ...
  * `test_metaclass` **(C Struct Operations)** (Impact: 24.4)
    * *Intent:* # Testing __metaclass__... class C: __metaclass__ = type def __init__(self): self.__state = 0 def ge...
  * `test_pickle_slots` **(Defensive Guards)** (Impact: 24.3)
    * *Intent:* # Testing pickling of classes with __slots__ ... import pickle, cPickle # Pickling of classes with _...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 294 instances
* *High Risk Execution (weighted view):* 17
* *State Mutation (weighted view):* 1371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 1602`, `args: 462`, `func_start: 444`, `class_start: 401`
* *Risk/State:* `safety_bypasses: 300`, `high_risk_execution: 23`, `state_mutation: 783`, `fragile_debt: 29`, `duplicate_logic: 54`, `unreferenced_by_name: 131`
* *Architecture:* `io: 19`, `api: 382`, `import: 32`
* *Defense:* `safety: 245`, `doc: 5`, `test: 140`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.0004
  * `Imports (Out-Degree: 19):` __builtin__, _testcapi, abc, binascii, cPickle, cStringIO, copy, copy_reg...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `extra_tests/cffi_tests/test_c.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.505)
- **Top Global Matches:** file_cluster_7: 9.505, file_cluster_12: 10.218, file_cluster_5: 10.899
- **Magnitude:** 3231.58 | **LOC:** 4527 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.067; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Complexity Load (formerly Cognitive Load) (82.7%), Guard Balance (formerly Safety Score) (80.0%)
- **Documentation Coverage:** 99.6303% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_test_bitfield_details` **(Defensive Guards)** (Impact: 33.6)
  * `_test_wchar_variant` **(Defensive Guards)** (Impact: 30.7)
  * `test_buffer` **(Defensive Guards)** (Impact: 23.4)
  * `find_and_load_library` **(Defensive Guards)** (Impact: 18.1)
  * `check` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 317 instances
* *State Mutation (weighted view):* 2069
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 1769`, `args: 276`, `func_start: 273`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 436`, `high_risk_execution: 1`, `state_mutation: 1435`, `fragile_debt: 6`, `duplicate_logic: 6`, `unreferenced_by_name: 231`
* *Architecture:* `io: 44`, `api: 268`, `import: 41`
* *Defense:* `safety: 1185`, `doc: 1`, `test: 539`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __builtin__, _cffi_backend, _weakref, array, builtins, ctypes.util, gc, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/module/_cffi_backend/test/_backend_test_c.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.496)
- **Top Global Matches:** file_cluster_7: 9.496, file_cluster_12: 10.225, file_cluster_5: 10.909
- **Magnitude:** 3212.68 | **LOC:** 4505 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.067; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (41.2%), Connectivity (formerly Api Exposure) (13.1%)
- **Documentation Coverage:** 99.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_test_bitfield_details` **(Defensive Guards)** (Impact: 33.6)
  * `_test_wchar_variant` **(Defensive Guards)** (Impact: 30.7)
  * `test_buffer` **(Defensive Guards)** (Impact: 23.4)
  * `find_and_load_library` **(Defensive Guards)** (Impact: 18.1)
  * `check` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 311 instances
* *State Mutation (weighted view):* 2052
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 1753`, `args: 275`, `func_start: 272`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 434`, `high_risk_execution: 1`, `state_mutation: 1430`, `fragile_debt: 7`, `duplicate_logic: 6`, `unreferenced_by_name: 231`
* *Architecture:* `io: 40`, `api: 268`, `import: 33`
* *Defense:* `safety: 1181`, `doc: 2`, `test: 534`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __builtin__, _cffi_backend, _weakref, array, builtins, contextlib, ctypes.util, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/module/micronumpy/test/test_ndarray.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.612)
- **Top Global Matches:** file_cluster_15: 7.612, file_cluster_12: 8.554, file_cluster_11: 9.046
- **Magnitude:** 3188.24 | **LOC:** 4479 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (41.5%), Guard Balance (formerly Safety Score) (32.4%), Connectivity (formerly Api Exposure) (13.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_fromstring` **(Defensive Guards)** (Impact: 20.8)
  * `test_subarrays` **(Defensive Guards)** (Impact: 17.9)
  * `test_data` **(Defensive Guards)** (Impact: 15.0)
  * `test_fromstring_types` **(Defensive Guards)** (Impact: 13.5)
  * `test_memoryview` **(Defensive Guards)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 288 instances
* *State Mutation (weighted view):* 1841
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 2589`, `args: 323`, `func_start: 320`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 1265`, `fragile_debt: 6`, `duplicate_logic: 2`, `unreferenced_by_name: 290`
* *Architecture:* `io: 40`, `api: 324`, `import: 342`
* *Defense:* `safety: 1521`, `test: 294`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.001568 | `Ripple Effect (Closeness):` 0.074406
  * `Imports (Out-Degree: 16):` _weakref, array, cPickle, math, mmap, numpy, numpy.core.multiarray, operator...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib-python/2.7/lib2to3/tests/test_fixers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.826)
- **Top Global Matches:** file_cluster_15: 8.826, file_cluster_12: 9.992, file_cluster_11: 10.472
- **Magnitude:** 3167.26 | **LOC:** 4545 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 0.067; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.6%), Complexity Load (formerly Cognitive Load) (20.9%), Connectivity (formerly Api Exposure) (14.8%)
- **Documentation Coverage:** 99.5671% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_prefix_preservation` **(Compute Cores)** (Impact: 19.6)
  * `assert_runs_after` **(Compute Cores)** (Impact: 12.8)
  * `test_call` **(Compute Cores)** (Impact: 10.5)
  * `test` **(Compute Cores)** (Impact: 9.2)
  * `test_import_from` **(Compute Cores)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 1615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 832`, `args: 466`, `func_start: 462`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 1347`, `fragile_debt: 4`, `duplicate_logic: 114`, `unreferenced_by_name: 263`
* *Architecture:* `io: 16`, `api: 514`, `import: 13`
* *Defense:* `safety: 7`, `doc: 931`, `test: 442`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` ..fixes.fix_imports, ..fixes.fix_imports2, ..fixes.fix_urllib, .a, .b, .bar, .c, .foo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib-python/2.7/lib-tk/Tkinter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_12: 6.526, file_cluster_7: 8.227, file_cluster_5: 9.108
- **Magnitude:** 3143.22 | **LOC:** 3868 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **83** in-repo importer(s); it depends on **10**; blast radius 2.148; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 10.2167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search` **(Many-Argument Workhorses)** (Impact: 39.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.3)
  * `_options` **(Stateful Encapsulated Methods)** (Impact: 27.3)
    * *Intent:* """Internal function."""
  * `_grid_configure` **(Stateful Encapsulated Methods)** (Impact: 20.6)
    * *Intent:* """Internal function."""
  * `_stringify` **(Stateful Encapsulated Methods)** (Impact: 19.7)
    * *Intent:* """Internal function."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 268 instances
* *State Mutation (weighted view):* 949
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 984`, `args: 516`, `func_start: 515`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 89`, `high_risk_execution: 1`, `state_mutation: 413`, `fragile_debt: 11`, `duplicate_logic: 38`
* *Architecture:* `io: 20`, `api: 482`, `import: 12`
* *Defense:* `safety: 73`, `doc: 504`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.148
  * `Choke Point (Betweenness):` 0.00903 | `Ripple Effect (Closeness):` 0.131264
  * `Imports (Out-Degree: 8):` FixTk, Tkconstants, Tkinter, _tkinter, os, re, sys, traceback...
  * `Imported By (In-Degree: 83):` (Excluded from Brief to save tokens)

### `lib-python/2.7/pydoc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.406)
- **Top Global Matches:** file_cluster_4: 8.406, file_cluster_12: 9.998, file_cluster_7: 11.929
- **Magnitude:** 3086.58 | **LOC:** 2424 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **28**; blast radius 0.168; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.4%), Connectivity (formerly Api Exposure) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 48.7047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `docmodule` **(Many-Argument Workhorses)** (Impact: 111.6)
    * *Intent:* """Produce HTML documentation for a module object."""
  * `docclass` **(Many-Argument Workhorses)** (Impact: 92.4)
  * `docmodule` **(Many-Argument Workhorses)** (Impact: 85.4)
    * *Intent:* """Produce text documentation for a given module object."""
  * `docclass` **(Many-Argument Workhorses)** (Impact: 74.5)
    * *Intent:* """Produce text documentation for a given class object."""
  * `docroutine` **(Many-Argument Workhorses)** (Impact: 71.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 421 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 1370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 468`, `args: 188`, `func_start: 148`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 73`, `high_risk_execution: 8`, `state_mutation: 528`, `fragile_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `io: 88`, `api: 147`, `concurrency: 4`, `import: 24`
* *Defense:* `safety: 119`, `doc: 93`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.168
  * `Choke Point (Betweenness):` 0.003761 | `Ripple Effect (Closeness):` 0.096794
  * `Imports (Out-Degree: 27):` BaseHTTPServer, StringIO, Tkinter, __builtin__, collections, formatter, getopt, imp...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pypy/module/micronumpy/types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.202)
- **Top Global Matches:** file_cluster_12: 7.202, file_cluster_15: 9.067, file_cluster_16: 9.852
- **Magnitude:** 3035.74 | **LOC:** 2770 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **26**; blast radius 0.11; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Complexity Load (formerly Cognitive Load) (88.8%)
- **Documentation Coverage:** 98.9101% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `record_coerce` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `make_integer_min_dtype` **(Type Conversions)** (Impact: 33.2)
  * `_coerce` **(Stateful Encapsulated Methods)** (Impact: 26.7)
    * *Intent:* # TODO: Make sure the shape and the array match from pypy.module.micronumpy.descriptor import W_Dtyp...
  * `floordiv` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `pow` **(Compute Cores)** (Impact: 18.9)
    * *Intent:* #complex mod does not exist in numpy #@simple_binary_op #def mod(self, v1, v2): # return math.fmod(v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 992
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 1055`, `args: 378`, `func_start: 376`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 446`, `dead_code: 20`, `planned_debt: 3`, `fragile_debt: 8`, `duplicate_logic: 54`
* *Architecture:* `api: 381`, `import: 29`
* *Defense:* `safety: 182`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.000323 | `Ripple Effect (Closeness):` 0.074446
  * `Imports (Out-Degree: 26):` .constants, functools, math, pypy.interpreter.baseobjspace, pypy.interpreter.error, pypy.module.micronumpy, pypy.module.micronumpy.base, pypy.module.micronumpy.concrete...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib-python/2.7/lib-tk/turtle.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.583)
- **Top Global Matches:** file_cluster_12: 6.583, file_cluster_16: 7.946, file_cluster_15: 8.533
- **Magnitude:** 2904.9 | **LOC:** 4035 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.079; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (46.0%)
- **Documentation Coverage:** 21.4493% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pen` **(Stateful Encapsulated Methods)** (Impact: 59.7)
    * *Intent:* """Return or set the pen's attributes. Arguments: pen -- a dictionary with some or all of the below ...
  * `_undogoto` **(Stateful Encapsulated Methods)** (Impact: 39.6)
    * *Intent:* """Reverse a _goto. Used for undo() """
  * `_drawturtle` **(Stateful Encapsulated Methods)** (Impact: 32.3)
    * *Intent:* """Manages the correct rendering of the turtle with respect to its shape, resizemode, stretch and ti...
  * `dot` **(Many-Argument Workhorses)** (Impact: 28.5)
    * *Intent:* """Draw a dot with diameter size, using color. Optional arguments: size -- an integer >= 1 (if given...
  * `circle` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* """ Draw a circle with given radius. Arguments: radius -- a number extent (optional) -- a number ste...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 423 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 1432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 372`, `args: 216`, `func_start: 214`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 6`, `state_mutation: 586`, `dead_code: 3`, `fragile_debt: 3`, `duplicate_logic: 3`, `unreferenced_by_name: 9`
* *Architecture:* `io: 3`, `api: 138`, `import: 11`
* *Defense:* `safety: 50`, `doc: 183`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.0002
  * `Imports (Out-Degree: 5):` Tkinter, copy, math, os, os.path, re, time, types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rpython/rtyper/test/test_rpbc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.521)
- **Top Global Matches:** file_cluster_12: 7.521, file_cluster_7: 10.139, file_cluster_15: 10.342
- **Magnitude:** 2877.76 | **LOC:** 2218 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **176** in-repo importer(s); it depends on **13**; blast radius 2.526; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.0%), Complexity Load (formerly Cognitive Load) (43.1%), Connectivity (formerly Api Exposure) (14.3%), Dead Code Surface (formerly Dead Code) (5.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `f` **(Compute Cores)** (Impact: 45.8)
  * `test_call_star_and_keywords_starargs` **(Compute Cores)** (Impact: 41.1)
  * `f` **(Compute Cores)** (Impact: 23.8)
  * `test_call_star_and_keywords` **(Compute Cores)** (Impact: 22.9)
  * `test_call_keywords` **(Compute Cores)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 299 instances
* *State Mutation (weighted view):* 1119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 1165`, `args: 406`, `func_start: 404`, `class_start: 104`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 7`, `state_mutation: 521`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 73`, `unreferenced_by_name: 104`
* *Architecture:* `api: 292`, `import: 48`
* *Defense:* `safety: 187`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.526
  * `Choke Point (Betweenness):` 0.005956 | `Ripple Effect (Closeness):` 0.118249
  * `Imports (Out-Degree: 16):` py, rpython.annotator, rpython.config.translationoption, rpython.rlib.cache, rpython.rlib.nonconst, rpython.rlib.objectmodel, rpython.rtyper, rpython.rtyper.llannotation...
  * `Imported By (In-Degree: 176):` (Excluded from Brief to save tokens)

### `rpython/rlib/rvmprof/src/shared/libbacktrace/dwarf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.054)
- **Top Global Matches:** file_cluster_6: 6.054, file_cluster_4: 11.254, file_cluster_8: 14.419
- **Magnitude:** 2863.64 | **LOC:** 3039 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 0.082; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%), Guard Balance (formerly Safety Score) (74.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_function_entry` **(Many-Argument Workhorses)** (Impact: 228.6)
    * *Intent:* /* Read one entry plus all its children. Add function addresses to VEC. Returns 1 on success, 0 on e...
  * `find_address_ranges` **(Many-Argument Workhorses)** (Impact: 158.9)
    * *Intent:* read, 0 if there is some error. */
  * `read_line_program` **(Many-Argument Workhorses)** (Impact: 118.6)
    * *Intent:* /* Read the line program, adding line mappings to VEC. Return 1 on success, 0 on failure. */
  * `read_attribute` **(Many-Argument Workhorses)** (Impact: 112.4)
    * *Intent:* *IS_VALID to 1. We don't try to store the value of other attribute forms, because we don't care abou...
  * `dwarf_lookup_pc` **(Many-Argument Workhorses)** (Impact: 98.5)
    * *Intent:* 0 if not. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 421 instances
* *State Mutation (weighted view):* 1336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 448`, `structural_boundaries: 545`, `args: 47`, `func_start: 46`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 494`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 70`, `immutability_locks: 129`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0004
  * `Imports (Out-Degree: 8):` backtrace.h, config.h, dwarf2.h, errno.h, filenames.h, internal.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pypy/objspace/std/listobject.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_15: 6.609, file_cluster_16: 6.977, file_cluster_12: 7.081
- **Magnitude:** 2829.58 | **LOC:** 2530 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **24**; blast radius 0.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (93.3%), Debt Markers (formerly Tech Debt) (79.3%), Guard Balance (formerly Safety Score) (73.2%)
- **Documentation Coverage:** 86.7857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setslice` **(Many-Argument Workhorses)** (Impact: 48.3)
  * `descr_sort` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* """ L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*; cmp(x, y) -> -1, 0, 1"""
  * `find_or_count` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `_safe_find_or_count` **(Stateful Encapsulated Methods)** (Impact: 32.9)
  * `get_strategy_from_list_object` **(Compute Cores)** (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 313 instances
* *State Mutation (weighted view):* 1130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 773`, `args: 316`, `func_start: 307`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 504`, `fragile_debt: 7`, `duplicate_logic: 15`
* *Architecture:* `io: 3`, `api: 272`, `import: 29`
* *Defense:* `safety: 103`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 0.007065 | `Ripple Effect (Closeness):` 0.128322
  * `Imports (Out-Degree: 21):` math, operator, pypy.interpreter.baseobjspace, pypy.interpreter.error, pypy.interpreter.gateway, pypy.interpreter.miscutils, pypy.interpreter.signature, pypy.interpreter.typedef...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `rpython/jit/backend/x86/assembler.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.582)
- **Top Global Matches:** file_cluster_12: 6.582, file_cluster_16: 7.566, file_cluster_15: 7.847
- **Magnitude:** 2747.2 | **LOC:** 2782 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **33**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.9%)
- **Documentation Coverage:** 96.2617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_build_wb_slowpath` **(Many-Argument Workhorses)** (Impact: 59.0)
  * `assemble_loop` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `_build_malloc_slowpath` **(Many-Argument Workhorses)** (Impact: 37.7)
    * *Intent:* """ While arriving on slowpath, we have a gcpattern on stack 0. The arguments are passed in ecx and ...
  * `load_from_mem` **(Many-Argument Workhorses)** (Impact: 35.5)
    * *Intent:* # ----------
  * `generate_body` **(Many-Argument Workhorses)** (Impact: 33.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 311 instances
* *State Mutation (weighted view):* 1256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 409`, `args: 177`, `func_start: 177`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 634`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 8`
* *Architecture:* `io: 1`, `api: 143`, `import: 39`
* *Defense:* `safety: 171`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.000834
  * `Imports (Out-Degree: 34):` __future__, itertools, rpython.jit.backend.llsupport, rpython.jit.backend.llsupport.asmmemmgr, rpython.jit.backend.llsupport.assembler, rpython.jit.backend.llsupport.descr, rpython.jit.backend.llsupport.gcmap, rpython.jit.backend.llsupport.regalloc...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `rpython/memory/gc/incminimark.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.303)
- **Top Global Matches:** file_cluster_4: 6.303, file_cluster_16: 7.415, file_cluster_15: 7.551
- **Magnitude:** 2744.94 | **LOC:** 3407 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **15**; blast radius 0.131; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.2%)
- **Documentation Coverage:** 84.375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `major_collection_step` **(Many-Argument Workhorses)** (Impact: 61.2)
    * *Intent:* # Note - minor collections seem fast enough so that one # is done before every major collection step
  * `external_malloc` **(Many-Argument Workhorses)** (Impact: 53.7)
    * *Intent:* # XXX kill alloc_young and make it always True """Allocate a large object using the ArenaCollection ...
  * `writebarrier_before_copy` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `_minor_collection` **(I/O & Config Routines)** (Impact: 44.4)
    * *Intent:* # ---------- # Nursery collection """Perform a minor collection: find the objects from the nursery t...
  * `_trace_drag_out` **(Many-Argument Workhorses)** (Impact: 38.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 419 instances
* *State Mutation (weighted view):* 1470
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 335`, `args: 150`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 632`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 21`
* *Architecture:* `io: 3`, `api: 106`, `import: 25`
* *Defense:* `safety: 10`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.001474
  * `Imports (Out-Degree: 13):` os, rpython.memory.gc, rpython.memory.gc.base, rpython.memory.gc.minimarkpage, rpython.memory.support, rpython.rlib, rpython.rlib.debug, rpython.rlib.objectmodel...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `rpython/rlib/runicode.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.322)
- **Top Global Matches:** file_cluster_6: 5.322, file_cluster_4: 7.425, file_cluster_15: 15.655
- **Magnitude:** 2735.82 | **LOC:** 1901 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **8**; blast radius 0.163; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.8%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.5816% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `str_decode_unicode_escape` **(Many-Argument Workhorses)** (Impact: 109.0)
  * `str_decode_utf_7` **(Many-Argument Workhorses)** (Impact: 96.9)
  * `str_decode_utf_16_helper` **(Many-Argument Workhorses)** (Impact: 95.8)
  * `make_unicode_escape_function` **(Many-Argument Workhorses)** (Impact: 85.9)
  * `str_decode_utf_32_helper` **(Many-Argument Workhorses)** (Impact: 85.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 422 instances
* *State Mutation (weighted view):* 1301
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 269`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 457`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 7`
* *Architecture:* `io: 3`, `api: 65`, `import: 8`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.106653
  * `Imports (Out-Degree: 7):` rpython.rlib, rpython.rlib.objectmodel, rpython.rlib.rarithmetic, rpython.rlib.rstring, rpython.rlib.unicodedata, rpython.rtyper.lltypesystem, rpython.tool.sourcetools, sys
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `lib-python/2.7/tarfile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.272)
- **Top Global Matches:** file_cluster_12: 7.272, file_cluster_4: 7.999, file_cluster_15: 9.419
- **Magnitude:** 2672.44 | **LOC:** 2633 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **20**; blast radius 0.257; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.7%), Connectivity (formerly Api Exposure) (60.5%), Complexity Load (formerly Cognitive Load) (38.5%)
- **Documentation Coverage:** 38.7097% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 121.1)
  * `gettarinfo` **(Many-Argument Workhorses)** (Impact: 67.5)
    * *Intent:* """Create a TarInfo object from the result of os.stat or equivalent on an existing file. The file is...
  * `open` **(Many-Argument Workhorses)** (Impact: 51.4)
    * *Intent:* #-------------------------------------------------------------------------- # Below are the classmet...
  * `add` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* """Add the file `name' to the archive. `name' may be any type of file (directory, fifo, symbolic lin...
  * `_extract_member` **(Stateful Encapsulated Methods)** (Impact: 34.0)
    * *Intent:* """Extract the TarInfo object tarinfo to a physical file called targetpath. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 373 instances
* *State Mutation (weighted view):* 1291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 420`, `args: 146`, `func_start: 144`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 545`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 64`, `api: 115`, `import: 23`
* *Defense:* `safety: 101`, `doc: 116`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.000492 | `Ripple Effect (Closeness):` 0.14995
  * `Imports (Out-Degree: 12):` StringIO, __builtin__, bz2, cStringIO, calendar, copy, errno, grp...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `rpython/rtyper/lltypesystem/lltype.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.778)
- **Top Global Matches:** file_cluster_12: 6.778, file_cluster_16: 8.881, file_cluster_5: 9.639
- **Magnitude:** 2665.52 | **LOC:** 2509 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **74** in-repo importer(s); it depends on **11**; blast radius 1.555; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.9%), Guard Balance (formerly Safety Score) (64.6%), Debt Markers (formerly Tech Debt) (56.7%)
- **Documentation Coverage:** 96.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `malloc` **(Many-Argument Workhorses)** (Impact: 49.2)
  * `ann_malloc` **(Defensive Guards)** (Impact: 34.2)
  * `cast_opaque_ptr` **(Defensive Guards)** (Impact: 33.5)
  * `_cast_whatever` **(Defensive Guards)** (Impact: 32.5)
  * `dissect_ll_instance` **(Defensive Guards)** (Impact: 31.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 304 instances
* *State Mutation (weighted view):* 1016
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 485`, `structural_boundaries: 830`, `args: 286`, `func_start: 285`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 408`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 9`, `duplicate_logic: 9`
* *Architecture:* `api: 127`, `import: 22`
* *Defense:* `safety: 277`, `doc: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.555
  * `Choke Point (Betweenness):` 0.004334 | `Ripple Effect (Closeness):` 0.134796
  * `Imports (Out-Degree: 12):` rpython.annotator.bookkeeper, rpython.annotator.model, rpython.rlib.objectmodel, rpython.rlib.rarithmetic, rpython.rtyper.extregistry, rpython.rtyper.llannotation, rpython.rtyper.lltypesystem, rpython.tool...
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `pypy/objspace/fake/test/test_objspace.py` (PYTHON) | Magnitude: 92.24 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 33, args: 26, state_mutation: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `lib-python/2.7/test/test_sundry.py` (PYTHON) | Magnitude: 15.16 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 70, import: 65, test: 5
- `extra_tests/test_syslog.py` (PYTHON) | Magnitude: 3.18 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 3, test: 3, safety: 2, args: 1
- `pypy/module/__builtin__/test/test_apply.py` (PYTHON) | Magnitude: 17.66 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 13, api: 7, args: 6
- `pypy/module/token/test/apptest_token.py` (PYTHON) | Magnitude: 6.5 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 10, safety: 6, indent_spaces: 6, args: 3
- `lib-python/2.7/test/test_charmapcodec.py` (PYTHON) | Magnitude: 19.46 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 15, test: 8, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `rpython/jit/backend/ppc/test/test_basic.py` (PYTHON) | Magnitude: 35.92 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 23, state_mutation: 6, import: 6
- `rpython/jit/backend/zarch/test/test_basic.py` (PYTHON) | Magnitude: 35.92 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 23, state_mutation: 6, import: 6
- `lib-python/2.7/rfc822.py` (PYTHON) | Magnitude: 1023.86 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 593, state_mutation: 202, branch: 174, structural_boundaries: 158
- `rpython/rtyper/test/test_rstr.py` (PYTHON) | Magnitude: 1458.1 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1080, structural_boundaries: 560, state_mutation: 362, core_var_decl: 362
- `rpython/rlib/rposix_stat.py` (PYTHON) | Magnitude: 828.34 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 624, structural_boundaries: 223, state_mutation: 191, core_var_decl: 188

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pypy/module/cpyext/sysmodule.py` (PYTHON) | Magnitude: 11.82 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 8, core_var_decl: 7, design_snake_case: 7
- `pypy/module/cpyext/boolobject.py` (PYTHON) | Magnitude: 4.84 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 3, import: 2, branch: 1
- `rpython/tool/pytest/test/test_expecttest.py` (PYTHON) | Magnitude: 6.06 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, api: 3, import: 3
- `rpython/jit/backend/aarch64/test/test_instr_builder.py` (PYTHON) | Magnitude: 112.4 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 158, structural_boundaries: 64, core_var_decl: 49, design_snake_case: 49
- `rpython/rlib/test/test_rpath.py` (PYTHON) | Magnitude: 34.72 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 68, indent_spaces: 66, safety: 56, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `rpython/annotator/test/test_description.py` (PYTHON) | Magnitude: 34.44 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 29, state_mutation: 13, class_start: 11
- `extra_tests/ctypes_tests/test_cast.py` (PYTHON) | Magnitude: 36.76 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 17, state_mutation: 15, core_var_decl: 13
- `lib-python/2.7/test/test_opcodes.py` (PYTHON) | Magnitude: 69.24 | Delta: **0.187** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 36, args: 23, safety: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pypy/module/test_lib_pypy/test_curses.py` (PYTHON) | Magnitude: 27.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 25, test: 8, state_mutation: 7
- `lib-python/2.7/os2emxpath.py` (PYTHON) | Magnitude: 150.56 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 63, core_var_decl: 34, design_snake_case: 33, state_mutation: 32
- `pypy/module/cpyext/test/test_fileobject.py` (PYTHON) | Magnitude: 5.08 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, api: 2, import: 2
- `rpython/translator/c/node.py` (PYTHON) | Magnitude: 1283.9 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 796, state_mutation: 262, structural_boundaries: 257, core_var_decl: 194
- `lib-python/2.7/test/test_md5.py` (PYTHON) | Magnitude: 44.16 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 16, structural_boundaries: 15, core_var_decl: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `lib-python/2.7/plat-mac/videoreader.py` (PYTHON) | Magnitude: 328.44 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 227, state_mutation: 89, structural_boundaries: 86, core_var_decl: 68
- `lib-python/2.7/plat-mac/PixMapWrapper.py` (PYTHON) | Magnitude: 172.96 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 149, structural_boundaries: 38, state_mutation: 34, branch: 29
- `rpython/jit/metainterp/optimizeopt/info.py` (PYTHON) | Magnitude: 1091.78 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 670, structural_boundaries: 334, state_mutation: 184, core_var_decl: 137
- `pypy/module/cpyext/src/sysmodule.c` (C) | Magnitude: 71.3 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 57, pointers: 22, branch: 11, state_mutation: 11
- `lib_pypy/_sqlite3_build.py` (PYTHON) | Magnitude: 45.76 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, core_var_decl: 17, design_snake_case: 17, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `rpython/translator/c/src/exception.c` (C) | Magnitude: 8.82 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 8, indent_spaces: 6, macros: 5, indent_tabs: 5
- `rpython/rlib/rvmprof/src/shared/libbacktrace/state.c` (C) | Magnitude: 19.7 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, pointers: 7, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `lib-python/2.7/plat-irix5/IOCTL.py` (PYTHON) | Magnitude: 237.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: core_var_decl: 221, state_mutation: 220, design_upper_case: 211, structural_boundaries: 16
- `lib-python/2.7/plat-irix6/IOCTL.py` (PYTHON) | Magnitude: 237.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: core_var_decl: 221, state_mutation: 220, design_upper_case: 211, structural_boundaries: 16
- `rpython/rlib/test/test_rmd5.py` (PYTHON) | Magnitude: 106.88 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 110, state_mutation: 28, structural_boundaries: 23, core_var_decl: 19
- `pypy/module/_warnings/test/test_warnings.py` (PYTHON) | Magnitude: 7.04 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, state_mutation: 4, core_var_decl: 4, design_snake_case: 4
- `lib-python/2.7/test/double_const.py` (PYTHON) | Magnitude: 15.18 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 6, indent_spaces: 6, core_var_decl: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `lib-python/2.7/Cookie.py` (PYTHON) | Magnitude: 284.98 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 260, structural_boundaries: 80, core_var_decl: 61, state_mutation: 59
- `rpython/rlib/listsort.py` (PYTHON) | Magnitude: 962.62 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 415, branch: 114, state_mutation: 114, structural_boundaries: 102
- `lib-python/2.7/unittest/loader.py` (PYTHON) | Magnitude: 384.32 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 197, core_var_decl: 76, structural_boundaries: 75, state_mutation: 71
- `lib-python/2.7/collections.py` (PYTHON) | Magnitude: 652.88 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 380, structural_boundaries: 157, branch: 118, state_mutation: 107

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `rpython/jit/codewriter/test/test_format.py` (PYTHON) | Magnitude: 80.48 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 46, state_mutation: 44, core_var_decl: 41
- `lib-python/2.7/idlelib/idle_test/test_calltips.py` (PYTHON) | Magnitude: 175.78 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 70, api: 41, args: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `lib-python/2.7/lib2to3/btm_matcher.py` (PYTHON) | Magnitude: 194.88 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 41, branch: 33, structural_boundaries: 31
- `lib-python/2.7/plat-irix5/readcd.py` (PYTHON) | Magnitude: 339.9 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 216, branch: 79, state_mutation: 52, structural_boundaries: 48
- `lib-python/2.7/plat-irix6/readcd.py` (PYTHON) | Magnitude: 339.9 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 216, branch: 79, state_mutation: 52, structural_boundaries: 48
- `rpython/translator/backendopt/storesink.py` (PYTHON) | Magnitude: 235.56 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 108, state_mutation: 44, branch: 40, structural_boundaries: 31
- `pypy/module/_cffi_backend/realize_c_type.py` (PYTHON) | Magnitude: 769.62 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 465, state_mutation: 172, core_var_decl: 138, branch: 135

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `rpython/jit/metainterp/optimizeopt/rawbuffer.py` (PYTHON) | Magnitude: 126.92 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 31, branch: 22, state_mutation: 22
- `lib-python/2.7/idlelib/PathBrowser.py` (PYTHON) | Magnitude: 124.58 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 37, state_mutation: 27, core_var_decl: 21
- `lib-python/2.7/atexit.py` (PYTHON) | Magnitude: 38.7 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 8, state_mutation: 8, core_var_decl: 8
- `lib-python/2.7/ctypes/test/test_repr.py` (PYTHON) | Magnitude: 17.14 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 10, test: 6, safety_bypasses: 4
- `rpython/rlib/rjitlog/test/test_jitlog.py` (PYTHON) | Magnitude: 77.5 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 62, state_mutation: 36, core_var_decl: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `rpython/tool/gcanalyze.py` (PYTHON) | Magnitude: 90.82 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 23, core_var_decl: 23, design_snake_case: 22
- `rpython/jit/tool/jitoutput.py` (PYTHON) | Magnitude: 64.86 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 30, bitwise_ops: 28, core_var_decl: 28
- `pypy/tool/clean_old_branches.py` (PYTHON) | Magnitude: 30.68 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, branch: 13, structural_boundaries: 7, io: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pypy/objspace/std/mapdict.py` -> Churn: **100.0%** | Cog Load: 87.9505% | Debt: 46.3906%
- `rpython/rlib/rbigint.py` -> Churn: **60.86%** | Cog Load: 61.2565% | Debt: 10.238%
- `rpython/rlib/rsignal.py` -> Churn: **60.86%** | Cog Load: 67.6364% | Debt: 42.3061%
- `rpython/rtyper/lltypesystem/ll2ctypes.py` -> Churn: **60.86%** | Cog Load: 89.5228% | Debt: 49.0459%
- `rpython/translator/c/src/signals.c` -> Churn: **60.86%** | Cog Load: 55.1658% | Debt: 96.6932%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rpython/jit/metainterp/pyjitpl.py` -> **CF Bolz-Tereick** (100.0% isolated ownership) | Magnitude: 4369.84
- `rpython/rlib/runicode.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 2735.82
- `rpython/jit/codewriter/jtransform.py` -> **CF Bolz-Tereick** (100.0% isolated ownership) | Magnitude: 2607.16
- `rpython/rtyper/lltypesystem/ll2ctypes.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 2208.8
- `pypy/module/cpyext/api.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 1970.38

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib-python/2.7/subprocess.py` -> **Severity: 2.229** (Bridge: 0.0223 * Flux: 100.0%)
- `lib-python/2.7/os.py` -> **Severity: 2.16** (Bridge: 0.0216 * Flux: 100.0%)
- `lib-python/2.7/threading.py` -> **Severity: 2.113** (Bridge: 0.0211 * Flux: 100.0%)
- `lib-python/2.7/_threading_local.py` -> **Severity: 2.032** (Bridge: 0.0203 * Flux: 99.9999%)
- `pypy/objspace/std/specialisedtupleobject.py` -> **Severity: 2.021** (Bridge: 0.0202 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib-python/2.7/os.py` -> **Severity: 23.116** (Embedded: 0.3377 * Error Risk: 68.4474%)
- `lib-python/2.7/warnings.py` -> **Severity: 22.688** (Embedded: 0.2789 * Error Risk: 81.3347%)
- `lib-python/2.7/types.py` -> **Severity: 21.157** (Embedded: 0.2833 * Error Risk: 74.6774%)
- `lib-python/2.7/re.py` -> **Severity: 20.891** (Embedded: 0.2577 * Error Risk: 81.0603%)
- `lib-python/2.7/traceback.py` -> **Severity: 19.052** (Embedded: 0.2221 * Error Risk: 85.7802%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib-python/2.7/os.py` -> **Severity: 2074.986** (Blast Radius: 43.018 * Doc Risk: 48.2353%)
- `lib-python/2.7/types.py` -> **Severity: 1914.0** (Blast Radius: 19.14 * Doc Risk: 100.0%)
- `lib-python/2.7/encodings/__init__.py` -> **Severity: 1481.073** (Blast Radius: 18.102 * Doc Risk: 81.8182%)
- `lib-python/2.7/warnings.py` -> **Severity: 1287.3** (Blast Radius: 20.842 * Doc Risk: 61.7647%)
- `lib-python/2.7/codecs.py` -> **Severity: 1286.582** (Blast Radius: 23.551 * Doc Risk: 54.6296%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1421 literal sites + 49 sites through wrappers = 1470
- **`memory_alloc`:** 230 literal sites + 90 sites through wrappers = 320
- **`panics_and_aborts`:** 13815 literal sites + 1654 sites through wrappers = 15469

- `chr` (function, panics_and_aborts, primitive): 1144 call sites in 258 files -- `pypy/module/__builtin__/operation.py`
- `PyErr_BadInternalCall` (function, panics_and_aborts, primitive): 35 call sites in 13 files -- `pypy/module/cpyext/pyerrors.py`
- `cppstring_to_cstring` (function, memory_alloc, primitive): 24 call sites in 1 files -- `pypy/module/_cppyy/src/dummy_backend.cxx`
- `raiseWindowsError` (function, panics_and_aborts, primitive): 24 call sites in 1 files -- `pypy/module/_winreg/interp_winreg.py`
- `z` (function, panics_and_aborts, primitive): 17 call sites in 5 files -- `rpython/jit/metainterp/test/test_exception.py`
- `PUBLIC_CPPYY_DATA` (macro, memory_alloc, primitive): 16 call sites in 1 files -- `pypy/module/_cppyy/src/dummy_backend.cxx`
- `_cmperror` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `lib_pypy/datetime.py`
- `lookup_db_flags` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `rpython/rlib/unicodedata/unicodedb_3_2_0.py`
- `_assert_unraisable` (function, panics_and_aborts, primitive): 14 call sites in 2 files -- `pypy/module/_cffi_backend/test/_backend_test_c.py`
- `PyMem_RESIZE` (macro, memory_alloc, via PyMem_REALLOC): 11 call sites in 1 files -- `pypy/module/cpyext/include/pymem.h`
- `letter2tp` (function, panics_and_aborts, primitive): 11 call sites in 5 files -- `pypy/module/_rawffi/interp_rawffi.py`
- `_wrap_close` (function, panics_and_aborts, primitive): 10 call sites in 2 files -- `pypy/module/imp/importing.py`
*(+249 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 291359 call pairs -- scoped 46.0%, unique 0.2%, ambiguous 38.7%, external 15.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 286309 | 46.5% | 0.0% | 39.3% | 14.2% |
| c | 4619 | 18.6% | 11.9% | 2.3% | 67.2% |
| cpp | 310 | 41.3% | 0.6% | 13.9% | 44.2% |
| m4 | 96 | 16.7% | 0.0% | 0.0% | 83.3% |
| shell | 25 | 0.0% | 0.0% | 0.0% | 100.0% |

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
