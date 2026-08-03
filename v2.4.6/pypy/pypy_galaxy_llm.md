# ARCHITECTURAL_BRIEF: pypy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/pypy` |
| **Timestamp** | `2026-08-03T19:40:08.727449+00:00` |
| **Scan Duration** | `11.31s` |
| **Git Branch** | `main` |
| **Git Commit** | `e371778f304422ddbb06fdf373c557a7d643c68f` |
| **Git Remote** | `https://github.com/pypy/pypy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1752 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 5994 |
| Analyzed Artifacts (Scanned) | 1788 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4206 |
| Total LOC | 323019 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 29.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6638 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1434 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 19.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2477 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 134 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1458 | 290444 | 81.5% |
| C | 276 | 28498 | 15.4% |
| PLAINTEXT | 23 | 0 | 1.3% |
| MAKEFILE | 9 | 1823 | 0.5% |
| MARKDOWN | 9 | 0 | 0.5% |
| BATCH | 3 | 350 | 0.2% |
| SHELL | 3 | 17 | 0.2% |
| M4 | 2 | 591 | 0.1% |
| ASSEMBLY | 2 | 97 | 0.1% |
| CPP | 1 | 1079 | 0.1% |
| HTML | 1 | 71 | 0.1% |
| CSS | 1 | 49 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.516`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1008 | 56.4% |
| file_cluster_13 | 618 | 34.6% |
| file_cluster_0 | 76 | 4.3% |
| file_cluster_17 | 22 | 1.2% |
| file_cluster_12 | 14 | 0.8% |
| file_cluster_9 | 12 | 0.7% |
| file_cluster_6 | 2 | 0.1% |
| file_cluster_16 | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |
| file_cluster_4 | 1 | 0.1% |
| file_cluster_11 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 32 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4206*

**Composition by Extension & Reason:**
- `.py`: 3073x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 19 LOC), 4x Excluded (Machine-Generated Source Code Signature: 2 LOC)
- `.txt`: 363x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 213x Excluded (Unsupported Extension: '.rst'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dectest`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 12 LOC), 1x Excluded (Unsupported Extension: '.benchmark_result')
- `.c`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 182 LOC), 1x Excluded (Embedded Array/Matrix Payload: 55661 commas in 4104 LOC)
- `.xml`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `.cxx`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 11x Excluded (Explicitly Denied Extension: '.gif')
- `.dot`: 8x Excluded (Unsupported Extension: '.dot')
- `.0`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.au`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.graffle`: 5x Excluded (Unsupported Extension: '.graffle'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 97.6 | 23.3 | 13.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.3 | 19.7 | 5.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 38.6 | 12.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 34.5 | 2.7 | 80.0 |
| API Exposure | 0.0 | 18.4 | 5.4 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 41.3 | 19.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.4 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 74.9 | 99.3 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 58.9 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 48.2 | 20.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 95.2 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pypy/interpreter/app_main.py` (Hits: 130)
- `pypy/module/posix/interp_posix.py` (Hits: 92)
- `py/_path/local.py` (Hits: 73)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **error.py** (`pypy/interpreter/error.py`) — 257 inbound connections
2. **gateway.py** (`pypy/interpreter/gateway.py`) — 158 inbound connections
3. **baseobjspace.py** (`pypy/interpreter/baseobjspace.py`) — 124 inbound connections
4. **typedef.py** (`pypy/interpreter/typedef.py`) — 117 inbound connections
5. **history.py** (`rpython/jit/metainterp/history.py`) — 85 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Python.h** (`pypy/module/cpyext/include/Python.h`) — 61 outbound dependencies
2. **api.py** (`pypy/module/cpyext/api.py`) — 54 outbound dependencies
3. **moduledef.py** (`pypy/module/cpyext/moduledef.py`) — 46 outbound dependencies
4. **baseobjspace.py** (`pypy/interpreter/baseobjspace.py`) — 42 outbound dependencies
5. **warmspot.py** (`rpython/jit/metainterp/warmspot.py`) — 40 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_Cryptography_pem_password_cb` (@ `lib_pypy/_cffi_ssl/_stdssl/__init__.py`) -> Impact: **6083.6** | LOC: 1460
- `_opimpl_assert_green` (@ `rpython/jit/metainterp/pyjitpl.py`) -> Impact: **4615.5** | LOC: 2104
- `_get_printable_location` (@ `pypy/objspace/std/listobject.py`) -> Impact: **4452.9** | LOC: 2258
- `transform_ovfcheck` (@ `rpython/translator/simplify.py`) -> Impact: **3696.7** | LOC: 946
- `_new_copy_contents_fun` (@ `rpython/rtyper/lltypesystem/rstr.py`) -> Impact: **3536.2** | LOC: 1228
- `getfield` (@ `pypy/module/micronumpy/ndarray.py`) -> Impact: **3316.5** | LOC: 1090
- `_put_back_line_directives` (@ `lib_pypy/cffi/cparser.py`) -> Impact: **3279.0** | LOC: 835
- `build_number` (@ `rpython/rtyper/lltypesystem/lltype.py`) -> Impact: **3246.9** | LOC: 1164
- `raiseattrerror` (@ `pypy/objspace/descroperation.py`) -> Impact: **3203.3** | LOC: 830
- `_put_back_line_directives` (@ `rpython/tool/cparser/cparser.py`) -> Impact: **3168.1** | LOC: 801

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `getcolor` (@ `dotviewer/drawgraph.py`) -> **O(2^N) [Recursive]**
- `test_issue1655` (@ `extra_tests/ctypes_tests/test_functions.py`) -> **O(2^N) [Recursive]**
- `_Cryptography_pem_password_cb` (@ `lib_pypy/_cffi_ssl/_stdssl/__init__.py`) -> **O(2^N) [Recursive]**
- `write` (@ `lib_pypy/_cffi_ssl/_stdssl/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # just that no data is currently available. The SSL routines should retry # the read, which we can achieve by calling BIO_set_retry_read(). lib.BIO_se...
- `_get_peer_alt_names` (@ `lib_pypy/_cffi_ssl/_stdssl/certificate.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # this code follows the procedure outlined in # OpenSSL's crypto/x509v3/v3_prn.c:X509v3_EXT_print() # function to extract the STACK_OF(GENERAL_NAME), ...
- `__new__` (@ `lib_pypy/_ctypes/array.py`) -> **O(2^N) [Recursive]**
- `_conv_param` (@ `lib_pypy/_ctypes/function.py`) -> **O(2^N) [Recursive]**
- `_setargtypes` (@ `lib_pypy/_ctypes/function.py`) -> **O(2^N) [Recursive]**
- `__new__` (@ `lib_pypy/_ctypes/primitive.py`) -> **O(2^N) [Recursive]**
- `names_and_fields` (@ `lib_pypy/_ctypes/structure.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # _fields_: list of (name, ctype, [optional_bitfield]) if isinstance(_fields_, tuple): _fields_ = list(_fields_) for f in _fields_: tp = f[1] if not i...

### Highest Data Gravity (Database Complexity)
- `putenv` (@ `pypy/module/posix/interp_posix.py`) -> DB Complexity: **200**
- `sd2b` (@ `rpython/translator/c/src/dtoa.c`) -> DB Complexity: **192**
  * *Intent:* /* count trailing 0 bits in the 32-bit integer y, and shift y right by that number of bits. */
- `convertsimple` (@ `pypy/module/cpyext/src/getargs.c`) -> DB Complexity: **173**
- `_Cryptography_pem_password_cb` (@ `lib_pypy/_cffi_ssl/_stdssl/__init__.py`) -> DB Complexity: **145**
- `_my_getstr` (@ `lib_pypy/pyrepl/unix_console.py`) -> DB Complexity: **140**
- `checkbadchars` (@ `py/_path/svnwc.py`) -> DB Complexity: **139**
- `_opimpl_assert_green` (@ `rpython/jit/metainterp/pyjitpl.py`) -> DB Complexity: **136**
- `print_banner` (@ `pypy/interpreter/app_main.py`) -> DB Complexity: **126**
  * *Intent:* # no. That's the normal path, "pypy stuff.py". # This includes the logic from execfile(), tweaked # to grab the future_flags at the end.
- `__repr__` (@ `py/_path/local.py`) -> DB Complexity: **116**
- `_get_msvc_env` (@ `rpython/translator/platform/windows.py`) -> DB Complexity: **114**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pypy/objspace/std` | 40 | 42585.28 | 20.49% | 28.18% |
| `pypy/module/micronumpy` | 27 | 35947.98 | 37.32% | 43.58% |
| `rpython/jit/metainterp` | 28 | 27674.16 | 31.01% | 42.73% |
| `pypy/interpreter` | 30 | 27053.38 | 24.79% | 44.17% |
| `rpython/rtyper/lltypesystem` | 20 | 26373.4 | 23.88% | 53.74% |
| `rpython/jit/metainterp/optimizeopt` | 26 | 25901.39 | 29.52% | 49.58% |
| `pypy/module/imp` | 4 | 21507.99 | 8.95% | 31.55% |
| `rpython/rtyper` | 33 | 21114.52 | 26.67% | 58.02% |
| `rpython/jit/backend/x86` | 17 | 19445.01 | 22.51% | 46.08% |
| `lib_pypy` | 49 | 18654.86 | 22.23% | 38.25% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `rpython/translator/c/src/stacklet/Makefile` -> **100.0%** Exposure
- `dotviewer/msgstruct.py` -> **100.0%** Exposure
- `dotviewer/strunicode.py` -> **100.0%** Exposure
- `extra_tests/ctypes_tests/test_base.py` -> **100.0%** Exposure
- `extra_tests/ctypes_tests/test_bitfields.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `lib_pypy/_functools.py` -> **100.0%** Exposure
- `lib_pypy/pyrepl/input.py` -> **100.0%** Exposure
- `lib_pypy/pyrepl/unix_console.py` -> **100.0%** Exposure
- `lib_pypy/pyrepl/unix_eventqueue.py` -> **100.0%** Exposure
- `py/_code/assertion.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pypy/module/cpyext/stubs.py` -> **195** Orphaned Functions | **0** Duplicates
- `rpython/annotator/unaryop.py` -> **48** Orphaned Functions | **72** Duplicates
- `rpython/jit/metainterp/optimizeopt/info.py` -> **0** Orphaned Functions | **101** Duplicates
- `extra_tests/cffi_tests/test_c.py` -> **83** Orphaned Functions | **0** Duplicates
- `pypy/module/micronumpy/types.py` -> **0** Orphaned Functions | **82** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`rpython/translator/c/src/dtoa.c`** -> AI Confidence: **99.48%**
2. **`rpython/translator/c/src/ll_strtod.c`** -> AI Confidence: **99.48%**
3. **`rpython/translator/c/src/stacklet/slp_platformselect.h`** -> AI Confidence: **99.48%**
4. **`rpython/rlib/rvmprof/src/shared/_vmprof.h`** -> AI Confidence: **99.43%**
5. **`pypy/module/cpyext/include/Python.h`** -> AI Confidence: **99.42%**
6. **`pypy/module/cpyext/include/pyport.h`** -> AI Confidence: **99.42%**
7. **`pypy/module/_cffi_backend/src/parse_c_type.c`** -> AI Confidence: **99.39%**
8. **`rpython/rlib/rvmprof/src/shared/libbacktrace/fileline.c`** -> AI Confidence: **99.39%**
9. **`pypy/interpreter/pyparser/pytokenizer.py`** -> AI Confidence: **99.34%**
10. **`pypy/module/_multibytecodec/src/cjkcodecs/_codecs_jp.c`** -> AI Confidence: **99.34%**
11. **`rpython/translator/c/src/thread.c`** -> AI Confidence: **99.34%**
12. **`rpython/translator/c/src/asm.h`** -> AI Confidence: **99.32%**
13. **`dotviewer/drawgraph.py`** -> AI Confidence: **99.31%**
14. **`dotviewer/graphdisplay.py`** -> AI Confidence: **99.31%**
15. **`dotviewer/graphparse.py`** -> AI Confidence: **99.31%**
16. **`lib_pypy/_cffi_ssl/_stdssl/__init__.py`** -> AI Confidence: **99.31%**
17. **`lib_pypy/_cffi_ssl/_stdssl/error.py`** -> AI Confidence: **99.31%**
18. **`lib_pypy/_cffi_ssl/tools/make_ssl_data.py`** -> AI Confidence: **99.31%**
19. **`lib_pypy/_ctypes/function.py`** -> AI Confidence: **99.31%**
20. **`lib_pypy/_ctypes/structure.py`** -> AI Confidence: **99.31%**
21. **`lib_pypy/_sqlite3.py`** -> AI Confidence: **99.31%**
22. **`lib_pypy/_tkinter/app.py`** -> AI Confidence: **99.31%**
23. **`lib_pypy/cffi/_pycparser/ply/cpp.py`** -> AI Confidence: **99.31%**
24. **`lib_pypy/cffi/_pycparser/ply/yacc.py`** -> AI Confidence: **99.31%**
25. **`lib_pypy/cffi/api.py`** -> AI Confidence: **99.31%**
26. **`lib_pypy/cffi/cparser.py`** -> AI Confidence: **99.31%**
27. **`lib_pypy/cffi/recompiler.py`** -> AI Confidence: **99.31%**
28. **`lib_pypy/cffi/verifier.py`** -> AI Confidence: **99.31%**
29. **`lib_pypy/pypy_tools/build_cffi_imports.py`** -> AI Confidence: **99.31%**
30. **`lib_pypy/pyrepl/python_reader.py`** -> AI Confidence: **99.31%**
31. **`lib_pypy/pyrepl/unix_console.py`** -> AI Confidence: **99.31%**
32. **`py/_code/source.py`** -> AI Confidence: **99.31%**
33. **`py/_io/terminalwriter.py`** -> AI Confidence: **99.31%**
34. **`py/_path/local.py`** -> AI Confidence: **99.31%**
35. **`py/_path/svnurl.py`** -> AI Confidence: **99.31%**
36. **`py/_path/svnwc.py`** -> AI Confidence: **99.31%**
37. **`pypy/config/pypyoption.py`** -> AI Confidence: **99.31%**
38. **`pypy/interpreter/app_main.py`** -> AI Confidence: **99.31%**
39. **`pypy/interpreter/astcompiler/astbuilder.py`** -> AI Confidence: **99.31%**
40. **`pypy/interpreter/astcompiler/tools/asdl_py.py`** -> AI Confidence: **99.31%**
41. **`pypy/interpreter/executioncontext.py`** -> AI Confidence: **99.31%**
42. **`pypy/interpreter/pyopcode.py`** -> AI Confidence: **99.31%**
43. **`pypy/interpreter/reverse_debugging.py`** -> AI Confidence: **99.31%**
44. **`pypy/interpreter/unicodehelper.py`** -> AI Confidence: **99.31%**
45. **`pypy/module/_cffi_backend/ctypeptr.py`** -> AI Confidence: **99.31%**
46. **`pypy/module/_cffi_backend/newtype.py`** -> AI Confidence: **99.31%**
47. **`pypy/module/_cffi_backend/realize_c_type.py`** -> AI Confidence: **99.31%**
48. **`pypy/module/_csv/interp_reader.py`** -> AI Confidence: **99.31%**
49. **`pypy/module/_file/readinto.py`** -> AI Confidence: **99.31%**
50. **`pypy/module/_io/interp_bufferedio.py`** -> AI Confidence: **99.31%**
51. **`pypy/module/_io/interp_io.py`** -> AI Confidence: **99.31%**
52. **`pypy/module/_io/interp_stringio.py`** -> AI Confidence: **99.31%**
53. **`pypy/module/_io/interp_textio.py`** -> AI Confidence: **99.31%**
54. **`pypy/module/_locale/interp_locale.py`** -> AI Confidence: **99.31%**
55. **`pypy/module/_winreg/interp_winreg.py`** -> AI Confidence: **99.31%**
56. **`pypy/module/array/interp_array.py`** -> AI Confidence: **99.31%**
57. **`pypy/module/cpyext/memoryobject.py`** -> AI Confidence: **99.31%**
58. **`pypy/module/cpyext/pystrtod.py`** -> AI Confidence: **99.31%**
59. **`pypy/module/cpyext/structmember.py`** -> AI Confidence: **99.31%**
60. **`pypy/module/fcntl/interp_fcntl.py`** -> AI Confidence: **99.31%**
61. **`pypy/module/imp/importing.py`** -> AI Confidence: **99.31%**
62. **`pypy/module/micronumpy/arrayops.py`** -> AI Confidence: **99.31%**
63. **`pypy/module/micronumpy/casting.py`** -> AI Confidence: **99.31%**
64. **`pypy/module/micronumpy/ctors.py`** -> AI Confidence: **99.31%**
65. **`pypy/module/micronumpy/descriptor.py`** -> AI Confidence: **99.31%**
66. **`pypy/module/micronumpy/loop.py`** -> AI Confidence: **99.31%**
67. **`pypy/module/micronumpy/nditer.py`** -> AI Confidence: **99.31%**
68. **`pypy/module/micronumpy/selection.py`** -> AI Confidence: **99.31%**
69. **`pypy/module/micronumpy/support.py`** -> AI Confidence: **99.31%**
70. **`pypy/module/micronumpy/ufuncs.py`** -> AI Confidence: **99.31%**
71. **`pypy/module/pypyjit/test_pypy_c/model.py`** -> AI Confidence: **99.31%**
72. **`pypy/module/select/interp_kqueue.py`** -> AI Confidence: **99.31%**
73. **`pypy/module/select/interp_select.py`** -> AI Confidence: **99.31%**
74. **`pypy/module/sys/initpath.py`** -> AI Confidence: **99.31%**
75. **`pypy/module/time/interp_time.py`** -> AI Confidence: **99.31%**
76. **`pypy/objspace/std/floatobject.py`** -> AI Confidence: **99.31%**
77. **`pypy/objspace/std/formatting.py`** -> AI Confidence: **99.31%**
78. **`pypy/objspace/std/newformat.py`** -> AI Confidence: **99.31%**
79. **`pypy/objspace/std/sliceobject.py`** -> AI Confidence: **99.31%**
80. **`pypy/tool/asterisk.py`** -> AI Confidence: **99.31%**
81. **`pypy/tool/bench/htmlreport.py`** -> AI Confidence: **99.31%**
82. **`pypy/tool/compare_last_builds.py`** -> AI Confidence: **99.31%**
83. **`pypy/tool/gcdump.py`** -> AI Confidence: **99.31%**
84. **`pypy/tool/import_graph.py`** -> AI Confidence: **99.31%**
85. **`pypy/tool/importfun.py`** -> AI Confidence: **99.31%**
86. **`rpython/annotator/annrpython.py`** -> AI Confidence: **99.31%**
87. **`rpython/annotator/bookkeeper.py`** -> AI Confidence: **99.31%**
88. **`rpython/annotator/classdesc.py`** -> AI Confidence: **99.31%**
89. **`rpython/jit/backend/aarch64/assembler.py`** -> AI Confidence: **99.31%**
90. **`rpython/jit/backend/aarch64/callbuilder.py`** -> AI Confidence: **99.31%**
91. **`rpython/jit/backend/arm/assembler.py`** -> AI Confidence: **99.31%**
92. **`rpython/jit/backend/arm/callbuilder.py`** -> AI Confidence: **99.31%**
93. **`rpython/jit/backend/llsupport/rewrite.py`** -> AI Confidence: **99.31%**
94. **`rpython/jit/backend/ppc/callbuilder.py`** -> AI Confidence: **99.31%**
95. **`rpython/jit/backend/ppc/tool/viewcode.py`** -> AI Confidence: **99.31%**
96. **`rpython/jit/backend/riscv/assembler.py`** -> AI Confidence: **99.31%**
97. **`rpython/jit/backend/riscv/callbuilder.py`** -> AI Confidence: **99.31%**
98. **`rpython/jit/backend/tool/viewcode.py`** -> AI Confidence: **99.31%**
99. **`rpython/jit/backend/x86/assembler.py`** -> AI Confidence: **99.31%**
100. **`rpython/jit/backend/x86/callbuilder.py`** -> AI Confidence: **99.31%**
101. **`rpython/jit/backend/zarch/callbuilder.py`** -> AI Confidence: **99.31%**
102. **`rpython/jit/backend/zarch/tool/viewcode.py`** -> AI Confidence: **99.31%**
103. **`rpython/jit/codewriter/call.py`** -> AI Confidence: **99.31%**
104. **`rpython/jit/codewriter/format.py`** -> AI Confidence: **99.31%**
105. **`rpython/jit/metainterp/optimizeopt/heap.py`** -> AI Confidence: **99.31%**
106. **`rpython/jit/metainterp/optimizeopt/intbounds.py`** -> AI Confidence: **99.31%**
107. **`rpython/jit/metainterp/optimizeopt/rewrite.py`** -> AI Confidence: **99.31%**
108. **`rpython/jit/metainterp/optimizeopt/vector.py`** -> AI Confidence: **99.31%**
109. **`rpython/jit/metainterp/optimizeopt/virtualstate.py`** -> AI Confidence: **99.31%**
110. **`rpython/jit/tool/oparser.py`** -> AI Confidence: **99.31%**
111. **`rpython/memory/gc/env.py`** -> AI Confidence: **99.31%**
112. **`rpython/memory/gc/incminimark.py`** -> AI Confidence: **99.31%**
113. **`rpython/memory/gc/minimark.py`** -> AI Confidence: **99.31%**
114. **`rpython/memory/gctransform/shadowcolor.py`** -> AI Confidence: **99.31%**
115. **`rpython/rtyper/lltypesystem/ll2ctypes.py`** -> AI Confidence: **99.31%**
116. **`rpython/rtyper/lltypesystem/module/ll_math.py`** -> AI Confidence: **99.31%**
117. **`rpython/rtyper/lltypesystem/rordereddict.py`** -> AI Confidence: **99.31%**
118. **`rpython/rtyper/normalizecalls.py`** -> AI Confidence: **99.31%**
119. **`rpython/tool/ansi_mandelbrot.py`** -> AI Confidence: **99.31%**
120. **`rpython/tool/cparser/cparser.py`** -> AI Confidence: **99.31%**
121. **`rpython/tool/error.py`** -> AI Confidence: **99.31%**
122. **`rpython/tool/logparser.py`** -> AI Confidence: **99.31%**
123. **`rpython/tool/setuptools_msvc.py`** -> AI Confidence: **99.31%**
124. **`rpython/translator/backendopt/all.py`** -> AI Confidence: **99.31%**
125. **`rpython/translator/backendopt/inline.py`** -> AI Confidence: **99.31%**
126. **`rpython/translator/backendopt/malloc.py`** -> AI Confidence: **99.31%**
127. **`rpython/translator/c/database.py`** -> AI Confidence: **99.31%**
128. **`rpython/translator/c/genc.py`** -> AI Confidence: **99.31%**
129. **`rpython/translator/goal/translate.py`** -> AI Confidence: **99.31%**
130. **`rpython/translator/platform/posix.py`** -> AI Confidence: **99.31%**
131. **`rpython/translator/platform/windows.py`** -> AI Confidence: **99.31%**
132. **`rpython/translator/simplify.py`** -> AI Confidence: **99.31%**
133. **`rpython/translator/tool/graphpage.py`** -> AI Confidence: **99.31%**
134. **`rpython/translator/tool/lltracker.py`** -> AI Confidence: **99.31%**
135. **`rpython/translator/tool/make_dot.py`** -> AI Confidence: **99.31%**
136. **`rpython/translator/tool/pdbplus.py`** -> AI Confidence: **99.31%**
137. **`rpython/translator/transform.py`** -> AI Confidence: **99.31%**
138. **`testrunner/runner.py`** -> AI Confidence: **99.31%**
139. **`lib_pypy/_testcapimodule.c`** -> AI Confidence: **99.31%**
140. **`pypy/module/faulthandler/faulthandler.c`** -> AI Confidence: **99.31%**
141. **`rpython/rlib/rjitlog/src/rjitlog.c`** -> AI Confidence: **99.31%**
142. **`rpython/rlib/rvmprof/src/shared/libbacktrace/btest.c`** -> AI Confidence: **99.31%**
143. **`rpython/rlib/rvmprof/src/shared/libbacktrace/dwarf.c`** -> AI Confidence: **99.31%**
144. **`rpython/rlib/rvmprof/src/shared/libbacktrace/elf.c`** -> AI Confidence: **99.31%**
145. **`rpython/rlib/rvmprof/src/shared/symboltable.c`** -> AI Confidence: **99.31%**
146. **`rpython/rlib/rvmprof/src/shared/vmp_stack.c`** -> AI Confidence: **99.31%**
147. **`rpython/rlib/rvmprof/src/shared/vmprof_unix.c`** -> AI Confidence: **99.31%**
148. **`rpython/translator/c/src/debug_print.c`** -> AI Confidence: **99.31%**
149. **`rpython/translator/c/src/entrypoint.c`** -> AI Confidence: **99.31%**
150. **`rpython/translator/c/src/instrument.c`** -> AI Confidence: **99.31%**
151. **`rpython/translator/c/src/signals.c`** -> AI Confidence: **99.31%**
152. **`rpython/translator/c/src/thread_pthread.c`** -> AI Confidence: **99.31%**
153. **`rpython/translator/revdb/src-revdb/revdb.c`** -> AI Confidence: **99.31%**
154. **`pypy/module/_cppyy/src/dummy_backend.cxx`** -> AI Confidence: **99.31%**
155. **`lib_pypy/__init__.py`** -> AI Confidence: **99.29%**
156. **`lib_pypy/_sysconfigdata.py`** -> AI Confidence: **99.29%**
157. **`lib_pypy/pyrepl/copy_code.py`** -> AI Confidence: **99.29%**
158. **`lib_pypy/pyrepl/keymaps.py`** -> AI Confidence: **99.29%**
159. **`pypy/module/posix/moduledef.py`** -> AI Confidence: **99.29%**
160. **`rpython/__init__.py`** -> AI Confidence: **99.29%**
161. **`rpython/jit/backend/riscv/instructions.py`** -> AI Confidence: **99.29%**
162. **`rpython/jit/backend/x86/arch.py`** -> AI Confidence: **99.29%**
163. **`pypy/module/_multibytecodec/src/cjkcodecs/_codecs_hk.c`** -> AI Confidence: **99.29%**
164. **`pypy/module/_multibytecodec/src/cjkcodecs/_codecs_kr.c`** -> AI Confidence: **99.29%**
165. **`pypy/module/cpyext/src/mysnprintf.c`** -> AI Confidence: **99.29%**
166. **`pypy/module/cpyext/src/pyerrors.c`** -> AI Confidence: **99.29%**
167. **`pypy/module/cpyext/src/stringobject.c`** -> AI Confidence: **99.29%**
168. **`pypy/module/cpyext/src/typeobject.c`** -> AI Confidence: **99.29%**
169. **`pypy/module/cpyext/src/unicodeobject.c`** -> AI Confidence: **99.29%**
170. **`rpython/translator/c/src/asm.c`** -> AI Confidence: **99.29%**
171. **`rpython/translator/c/src/int.h`** -> AI Confidence: **99.29%**
172. **`rpython/translator/c/src/support.h`** -> AI Confidence: **99.29%**
173. **`pypy/module/_multibytecodec/src/cjkcodecs/alg_jisx0201.h`** -> AI Confidence: **99.29%**
174. **`pypy/module/_multibytecodec/src/cjkcodecs/emu_jisx0213_2000.h`** -> AI Confidence: **99.29%**
175. **`pypy/module/cpyext/PC/pyconfig.h`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `extra_tests/test_string.py` -> **100.0%** Exposure
- `rpython/jit/backend/x86/rx86.py` -> **100.0%** Exposure
- `pypy/module/pypyjit/test_pypy_c/test_string.py` -> **0.0643%** Exposure
- `rpython/jit/backend/x86/detect_feature.py` -> **0.0019%** Exposure
- `pypy/module/test_lib_pypy/test_marshal_extra.py` -> **0.001%** Exposure
### Exploit Generation Surface
- `dotviewer/drawgraph.py` -> **100.0%** Exposure
- `dotviewer/graphclient.py` -> **100.0%** Exposure
- `dotviewer/graphdisplay.py` -> **100.0%** Exposure
- `dotviewer/graphparse.py` -> **100.0%** Exposure
- `dotviewer/graphserver.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `dotviewer/graphclient.py` -> **100.0%** Exposure
- `dotviewer/graphparse.py` -> **100.0%** Exposure
- `extra_tests/test_pypy_remote_debug.py` -> **100.0%** Exposure
- `extra_tests/test_sqlite3.py` -> **100.0%** Exposure
- `lib_pypy/_cffi_ssl/_cffi_src/utils.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `rpython/rlib/rvmprof/src/shared/libbacktrace/dwarf.c` -> **10.0%** Exposure
- `pypy/module/_cffi_backend/src/parse_c_type.c` -> **9.9999%** Exposure
- `pypy/module/cpyext/src/bufferobject.c` -> **9.9999%** Exposure
- `rpython/translator/c/src/dtoa.c` -> **9.9817%** Exposure
- `rpython/rlib/rvmprof/src/shared/libbacktrace/internal.h` -> **9.974%** Exposure
### Hardcoded Payload Artifacts
- `lib_pypy/_cffi_ssl/_stdssl/certificate.py` -> **95.203%** Exposure
### Algorithmic DoS Exposure
- `dotviewer/dotviewer.py` -> **100.0%** Exposure
- `dotviewer/drawgraph.py` -> **100.0%** Exposure
- `dotviewer/graphclient.py` -> **100.0%** Exposure
- `dotviewer/graphdisplay.py` -> **100.0%** Exposure
- `dotviewer/graphparse.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `13` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `9050` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `dotviewer/graphparse.py` (PYTHON) -> Cumulative Risk: **941.56**
- **Archetype:** `file_cluster_13` (Distance: 10.653 IQR)
- **Magnitude:** 325.46 | **LOC:** 143 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `parse_plain` (Impact: 174.7), `guess_type` (Impact: 53.2), `dot2plain_graphviz` (Impact: 43.1)

### 2. `pypy/module/micronumpy/compile.py` (PYTHON) -> Cumulative Risk: **896.16**
- **Archetype:** `file_cluster_13` (Distance: 14.198 IQR)
- **Magnitude:** 2856.04 | **LOC:** 1124 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__repr__` (Impact: 1374.7), `__repr__` (Impact: 189.7), `__repr__` (Impact: 116.4)

### 3. `lib_pypy/pyrepl/input.py` (PYTHON) -> Cumulative Risk: **895.79**
- **Archetype:** `file_cluster_13` (Distance: 15.243 IQR)
- **Magnitude:** 173.98 | **LOC:** 98 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `push` (Impact: 80.2), `__init__` (Impact: 19.2), `get` (Impact: 10.6)

### 4. `rpython/flowspace/flowcontext.py` (PYTHON) -> Cumulative Risk: **882.19**
- **Archetype:** `file_cluster_8` (Distance: 12.119 IQR)
- **Magnitude:** 2081.56 | **LOC:** 1405 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `unsupportedoperation` (Impact: 1335.7), `guessbool` (Impact: 255.9), `guessexception` (Impact: 15.6)

### 5. `pypy/tool/bench/pypyresult.py` (PYTHON) -> Cumulative Risk: **873.33**
- **Archetype:** `file_cluster_13` (Distance: 12.44 IQR)
- **Magnitude:** 102.52 | **LOC:** 59 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 29.1), `getbenchmarks` (Impact: 17.7), `parsepickle` (Impact: 7.5)

### 6. `py/_code/_assertionold.py` (PYTHON) -> Cumulative Risk: **864.73**
- **Archetype:** `file_cluster_17` (Distance: 12.995 IQR)
- **Magnitude:** 551.36 | **LOC:** 556 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `eval` (Impact: 61.7), `check` (Impact: 59.2), `__matchkey__` (Impact: 35.5)

### 7. `rpython/jit/tl/tlc.py` (PYTHON) -> Cumulative Risk: **851.37**
- **Archetype:** `file_cluster_13` (Distance: 13.107 IQR)
- **Magnitude:** 1263.46 | **LOC:** 484 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `make_interp` (Impact: 800.0), `_nth` (Impact: 21.0), `get` (Impact: 17.7)

### 8. `rpython/jit/backend/ppc/form.py` (PYTHON) -> Cumulative Risk: **849.05**
- **Archetype:** `file_cluster_17` (Distance: 12.636 IQR)
- **Magnitude:** 807.28 | **LOC:** 195 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9997%)
- **Heaviest Functions:** `__call__` (Impact: 665.2), `calc_fields` (Impact: 30.9), `__init__` (Impact: 18.4)

### 9. `rpython/jit/backend/ppc/tool/viewcode.py` (PYTHON) -> Cumulative Risk: **831.37**
- **Archetype:** `file_cluster_13` (Distance: 11.419 IQR)
- **Magnitude:** 651.04 | **LOC:** 431 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `__repr__` (Impact: 299.9), `load_symbols` (Impact: 55.7), `format_code_dump_with_labels` (Impact: 49.1)

### 10. `rpython/jit/backend/zarch/tool/viewcode.py` (PYTHON) -> Cumulative Risk: **829.93**
- **Archetype:** `file_cluster_13` (Distance: 11.432 IQR)
- **Magnitude:** 651.02 | **LOC:** 429 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `__repr__` (Impact: 299.9), `load_symbols` (Impact: 55.7), `format_code_dump_with_labels` (Impact: 49.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pypy/module/imp/importing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.756 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.194 IQR)
- **Top Global Matches:** file_cluster_0: 11.756, file_cluster_8: 11.768, file_cluster_13: 11.784
- **Magnitude:** 21207.29 | **LOC:** 1154 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.1495%), Tech Debt (26.2196%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 227`, `args: 59`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 35`, `dead_code: 5`, `fragile_debt: 8`
* *Architecture:* `io: 45`, `api: 46`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 87`, `doc: 34`, `test: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.582
  * `Choke Point (Betweenness):` 0.000878 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` pypy.interpreter.module, at, rpython.rlib.streamio, pypy.interpreter.typedef, x, lock., stat, hook...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rpython/jit/backend/x86/rx86.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.965 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.574 IQR)
- **Top Global Matches:** file_cluster_8: 9.965, file_cluster_0: 10.347, file_cluster_13: 10.513
- **Magnitude:** 8885.73 | **LOC:** 1057 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.2456%), Tech Debt (16.2903%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 168`, `args: 77`, `func_start: 77`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 25`, `dead_code: 3`, `fragile_debt: 4`
* *Architecture:* `api: 79`, `import: 7`
* *Defense:* `safety: 29`, `doc: 2`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` rpython.rtyper.lltypesystem, rpython.rlib.objectmodel, py, rpython.rlib.rarithmetic, rpython.jit.backend.x86.arch, rpython.rlib.unroll
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rpython/jit/metainterp/pyjitpl.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.466 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.047 IQR)
- **Top Global Matches:** file_cluster_0: 12.466, file_cluster_13: 12.745, file_cluster_8: 12.84
- **Magnitude:** 7619.34 | **LOC:** 3900 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 136
- **Risk Profile:** Cognitive Load (30.652%), Tech Debt (14.2114%)
**Top Internal Functions/Classes:**
  * `_opimpl_assert_green` (Impact: 4615.5 | O(2^N) | DB: 136)
  * `opimpl_jit_merge_point` (Impact: 123.7 | O(N^6) | DB: 2)
  * `_try_tco` (Impact: 111.3 | O(N^6))
  * `_opimpl_recursive_call` (Impact: 105.3 | O(N^6))
  * `get_list_of_active_boxes` (Impact: 94.8 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 743`, `args: 268`, `func_start: 268`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 3`, `state_mutation: 292`, `dead_code: 22`, `fragile_debt: 14`
* *Architecture:* `io: 3`, `api: 291`, `import: 49`
* *Defense:* `safety: 182`, `doc: 32`, `test: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 0.000678 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` rpython.rtyper.lltypesystem, rpython.jit.metainterp.logger, rpython.jit.metainterp.optimizeopt.util, rpython.jit.metainterp.history, rpython.jit.metainterp, rpython.jit.metainterp.support, rpython.rlib, rpython.jit.codewriter.effectinfo...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib_pypy/_cffi_ssl/_stdssl/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.798 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.539 IQR)
- **Top Global Matches:** file_cluster_0: 11.798, file_cluster_8: 11.903, file_cluster_13: 11.954
- **Magnitude:** 6872.22 | **LOC:** 1981 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 145
- **Risk Profile:** Cognitive Load (59.78%), Tech Debt (22.7558%)
**Top Internal Functions/Classes:**
  * `_Cryptography_pem_password_cb` (Impact: 6083.6 | O(2^N) | DB: 145)
  * `write` (Impact: 433.4 | O(2^N) | DB: 13)
    * *Intent:* # just that no data is currently available. The SSL routines should retry # the read, which we can a...
  * `txt2obj` (Impact: 16.5 | O(N^2))
  * `_asn1obj2py` (Impact: 13.7 | O(N^2))
  * `_PySSL_errno` (Impact: 12.4 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 467`, `structural_boundaries: 315`, `args: 105`, `func_start: 105`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 172`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 37`, `api: 84`, `import: 19`
* *Defense:* `safety: 52`, `doc: 16`, `test: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` socket, _pypy_util_cffi, _cffi_ssl._stdssl.error, enum, thread, _cffi_ssl._stdssl.certificate, time, _cffi_ssl._stdssl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/rtyper/lltypesystem/lltype.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.382 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.066 IQR)
- **Top Global Matches:** file_cluster_0: 13.382, file_cluster_13: 13.462, file_cluster_17: 13.47
- **Magnitude:** 6436.28 | **LOC:** 2509 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (56.3417%), Tech Debt (99.3818%)
**Top Internal Functions/Classes:**
  * `build_number` (Impact: 3246.9 | O(2^N) | DB: 20)
  * `__repr__` (Impact: 669.5 | O(2^N) | DB: 14)
    * *Intent:* #self._TYPE = TYPE
  * `__str__` (Impact: 495.7 | O(2^N) | DB: 4)
  * `dissect_ll_instance` (Impact: 151.3 | O(2^N))
  * `malloc` (Impact: 145.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 815`, `args: 286`, `func_start: 285`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 180`, `dead_code: 17`, `planned_debt: 1`, `fragile_debt: 9`, `duplicate_logic: 34`
* *Architecture:* `api: 117`, `import: 22`
* *Defense:* `safety: 301`, `doc: 28`, `test: 63`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.728
  * `Choke Point (Betweenness):` 0.001486 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` types, rpython.tool, rpython.rtyper.lltypesystem, rpython.rlib.objectmodel, rpython.annotator.model, rpython.rtyper.llannotation, rpython.rlib.rarithmetic, rpython.annotator.bookkeeper...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `lib_pypy/cffi/_pycparser/ply/yacc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.81 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.356 IQR)
- **Top Global Matches:** file_cluster_8: 12.81, file_cluster_17: 12.965, file_cluster_13: 13.036
- **Magnitude:** 6160.3 | **LOC:** 3426 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (87.5854%), Tech Debt (93.0125%)
**Top Internal Functions/Classes:**
  * `parse_grammar` (Impact: 1079.6 | O(2^N) | DB: 43)
    * *Intent:* # === INTROSPECTION === # # The following functions and classes are used to implement the PLY # intr...
  * `yacc` (Impact: 680.4 | O(N^4) | DB: 23)
    * *Intent:* # Secondary validation step that looks for p_ definitions that are not functions # or functions that...
  * `parsedebug` (Impact: 507.6 | O(N^6) | DB: 35)
    * *Intent:* # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! # parsedebug(). # # ...
  * `parseopt` (Impact: 468.5 | O(N^6) | DB: 35)
    * *Intent:* #--! parsedebug-end # parseopt(). # # Optimized version of parse() method. DO NOT EDIT THIS CODE DIR...
  * `parseopt_notrack` (Impact: 430.3 | O(N^6) | DB: 35)
    * *Intent:* #--! parseopt-end # parseopt_notrack(). # # Optimized version of parseopt() with line number trackin...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 602`, `structural_boundaries: 347`, `args: 110`, `func_start: 105`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 565`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 22`, `orphaned_logic: 11`
* *Architecture:* `io: 26`, `api: 91`, `import: 10`
* *Defense:* `safety: 107`, `doc: 8`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` types, re, inspect, os.path, warnings, sys, base64, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib_pypy/pyrepl/readline.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.984 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.551 IQR)
- **Top Global Matches:** file_cluster_8: 10.984, file_cluster_13: 11.11, file_cluster_0: 11.31
- **Magnitude:** 5317.94 | **LOC:** 490 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.2606%), Tech Debt (34.7016%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 102`, `args: 41`, `func_start: 41`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 45`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 3`
* *Architecture:* `io: 14`, `api: 37`, `import: 7`
* *Defense:* `safety: 21`, `doc: 4`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.738
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __builtin__, pyrepl.unix_console, pyrepl.historical_reader, warnings, sys, pyrepl, pyrepl.completing_reader, os
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pypy/objspace/std/listobject.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.256 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.889 IQR)
- **Top Global Matches:** file_cluster_8: 12.256, file_cluster_13: 12.319, file_cluster_0: 12.375
- **Magnitude:** 5192.08 | **LOC:** 2530 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (20.2663%), Tech Debt (22.8057%)
**Top Internal Functions/Classes:**
  * `_get_printable_location` (Impact: 4452.9 | O(2^N) | DB: 73)
  * `get_strategy_from_list_object` (Impact: 49.3 | O(N^3))
  * `listrepr` (Impact: 46.5 | O(N^4) | DB: 5)
  * `_get_printable_location` (Impact: 45.0 | O(2^N) | DB: 1)
  * `_get_strategy_from_list_object_int_or_fl` (Impact: 26.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 773`, `args: 316`, `func_start: 307`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 176`, `dead_code: 2`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 273`, `import: 29`
* *Defense:* `safety: 105`, `doc: 90`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.152
  * `Choke Point (Betweenness):` 0.002353 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` pypy.objspace.std.bytesobject, pypy.interpreter.typedef, pypy.objspace.std.sliceobject, pypy.module.cpyext.sequence, rpython.rlib.rarithmetic, rpython.rlib.rstring, rpython.rlib, pypy.interpreter.miscutils...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `rpython/rtyper/lltypesystem/module/ll_math.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.112 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.818 IQR)
- **Top Global Matches:** file_cluster_8: 8.112, file_cluster_13: 8.837, file_cluster_7: 8.964
- **Magnitude:** 5173.96 | **LOC:** 406 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.4978%), Tech Debt (20.8609%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 102`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 1`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 21`, `import: 13`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.384
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rpython.rlib.rfloat, rpython.rtyper.lltypesystem, py, rpython.translator, sys, statement, rpython.translator.tool.cbuild, errno...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pypy/module/micronumpy/types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.022 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.42 IQR)
- **Top Global Matches:** file_cluster_0: 12.022, file_cluster_13: 12.623, file_cluster_8: 12.695
- **Magnitude:** 4982.24 | **LOC:** 2770 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (17.9971%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `unbox` (Impact: 1970.4 | O(2^N))
  * `unbox` (Impact: 320.9 | O(2^N))
  * `_coerce` (Impact: 154.0 | O(2^N))
  * `record_coerce` (Impact: 134.9 | O(N^6))
  * `make_integer_min_dtype` (Impact: 111.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 1037`, `args: 378`, `func_start: 376`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 44`, `dead_code: 24`, `planned_debt: 3`, `fragile_debt: 8`, `duplicate_logic: 82`
* *Architecture:* `api: 382`, `import: 29`
* *Defense:* `safety: 184`, `doc: 10`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.135
  * `Choke Point (Betweenness):` 0.031003 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` rpython.rtyper.lltypesystem, pypy.module.micronumpy.descriptor, functools, rpython.rlib.rarithmetic, rpython.rlib.rstring, rpython.rlib.unroll, rpython.rlib, ...
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `pypy/module/micronumpy/descriptor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.151 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.547 IQR)
- **Top Global Matches:** file_cluster_8: 12.151, file_cluster_13: 12.28, file_cluster_0: 12.384
- **Magnitude:** 4845.14 | **LOC:** 1491 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (43.0785%), Tech Debt (10.6861%)
**Top Internal Functions/Classes:**
  * `byteorder_w` (Impact: 2020.9 | O(2^N) | DB: 68)
  * `make_new_dtype` (Impact: 1429.8 | O(2^N) | DB: 32)
  * `dtype_from_list` (Impact: 440.6 | O(N^6) | DB: 1)
  * `dtype_from_dict` (Impact: 184.8 | O(N^6) | DB: 2)
  * `dtype_from_spec` (Impact: 106.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 315`, `args: 88`, `func_start: 87`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 254`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `api: 82`, `import: 22`
* *Defense:* `safety: 59`, `doc: 6`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.003356 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` .base, pypy.module.micronumpy.hashdescr, rpython.rlib.objectmodel, pypy.interpreter.error, rpython.annotator.model, pypy.objspace.std.dictmultiobject, pypy.module.micronumpy.appbridge, pypy.interpreter.gateway...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pypy/module/micronumpy/ndarray.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.152 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.199 IQR)
- **Top Global Matches:** file_cluster_8: 11.152, file_cluster_13: 11.35, file_cluster_0: 11.413
- **Magnitude:** 4626.8 | **LOC:** 1706 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (26.0091%), Tech Debt (11.1306%)
**Top Internal Functions/Classes:**
  * `getfield` (Impact: 3316.5 | O(2^N) | DB: 17)
  * `descr_getitem` (Impact: 183.5 | O(2^N))
  * `_prepare_array_index` (Impact: 163.5 | O(N^6) | DB: 4)
  * `getitem_filter` (Impact: 157.6 | O(2^N))
  * `setitem_array_int` (Impact: 126.7 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 380`, `args: 132`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 66`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `api: 120`, `import: 26`
* *Defense:* `safety: 64`, `doc: 14`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.517
  * `Choke Point (Betweenness):` 0.000682 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` rpython.rtyper.lltypesystem, pypy.module.micronumpy.descriptor, .flatiter, pypy.module.micronumpy.appbridge, pypy.interpreter.typedef, pypy.module.micronumpy.arrayops, rpython.rlib.rarithmetic, rpython.rlib.rstring...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `rpython/memory/gc/incminimark.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.176 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.038 IQR)
- **Top Global Matches:** file_cluster_13: 13.176, file_cluster_8: 13.201, file_cluster_0: 13.298
- **Magnitude:** 4575.44 | **LOC:** 3407 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (41.2186%), Tech Debt (96.226%)
**Top Internal Functions/Classes:**
  * `major_collection_step` (Impact: 352.2 | O(2^N) | DB: 23)
  * `external_malloc` (Impact: 350.9 | O(2^N) | DB: 6)
    * *Intent:* # Pinned object in front of nursery_top. Try reserving totalsize # by jumping into the next, yet unu...
  * `setup` (Impact: 262.4 | O(2^N) | DB: 42)
    * *Intent:* # # 'large_object' limit how big objects can be in the nursery, so # it gives a lower bound on the a...
  * `writebarrier_before_copy` (Impact: 160.9 | O(N^6) | DB: 5)
    * *Intent:* # which must have an array part; 'index' is the index of the # item that is (or contains) the pointe...
  * `collect_cardrefs_to_nursery` (Impact: 137.1 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 401`, `structural_boundaries: 329`, `args: 150`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 524`, `dead_code: 23`, `planned_debt: 2`, `fragile_debt: 21`, `duplicate_logic: 2`, `orphaned_logic: 34`
* *Architecture:* `io: 4`, `api: 104`, `import: 25`
* *Defense:* `safety: 10`, `doc: 48`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` rpython.rtyper.lltypesystem, rpython.rlib.objectmodel, rpython.memory.gc.base, rpython.memory.gc.minimarkpage, rpython.rlib.debug, rpython.rtyper.lltypesystem.llmemory, rpython.memory.support, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/module/cpyext/src/getargs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.337 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.11 IQR)
- **Top Global Matches:** file_cluster_8: 13.337, file_cluster_0: 13.579, file_cluster_13: 13.593
- **Magnitude:** 4457.94 | **LOC:** 1873 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 173
- **Risk Profile:** Cognitive Load (95.5063%), Tech Debt (16.8487%)
**Top Internal Functions/Classes:**
  * `convertsimple` (Impact: 1564.8 | O(N^6) | DB: 173)
  * `skipitem` (Impact: 762.5 | O(2^N) | DB: 18)
  * `vgetargs1` (Impact: 224.6 | O(N^6) | DB: 33)
  * `vgetargskeywords` (Impact: 147.3 | O(N^6) | DB: 29)
  * `converttuple` (Impact: 91.2 | O(N^6) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 512`, `structural_boundaries: 199`, `args: 11`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 877`, `dead_code: 3`, `fragile_debt: 2`, `orphaned_logic: 6`
* *Architecture:* `io: 10`, `api: 347`, `import: 2`
* *Defense:* `safety: 19`, `test: 11`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Python.h, ctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/module/micronumpy/ufuncs.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.873 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.827 IQR)
- **Top Global Matches:** file_cluster_8: 11.873, file_cluster_13: 12.006, file_cluster_17: 12.141
- **Magnitude:** 4373.62 | **LOC:** 1624 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (62.9404%), Tech Debt (57.6125%)
**Top Internal Functions/Classes:**
  * `_raise_err_msg` (Impact: 1980.0 | O(2^N) | DB: 37)
  * `descr_repr` (Impact: 1432.1 | O(N^6) | DB: 18)
  * `frompyfunc` (Impact: 304.5 | O(N^6))
  * `descr_call` (Impact: 114.8 | O(N^6) | DB: 5)
  * `_ufunc1_dtypes` (Impact: 73.9 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 246`, `args: 57`, `func_start: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 198`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 8`, `duplicate_logic: 3`, `orphaned_logic: 3`
* *Architecture:* `api: 47`, `import: 22`
* *Defense:* `safety: 55`, `doc: 8`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` rpython.rtyper.lltypesystem, pypy.module.micronumpy.descriptor, pypy.interpreter.typedef, pypy.module.micronumpy.support, rpython.rlib.rarithmetic, pypy.module.micronumpy.base, rpython.rlib, .converters...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib_pypy/datetime.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.245 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.166 IQR)
- **Top Global Matches:** file_cluster_0: 12.245, file_cluster_8: 12.306, file_cluster_13: 12.445
- **Magnitude:** 4177.0 | **LOC:** 2106 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (28.691%), Tech Debt (46.1017%)
**Top Internal Functions/Classes:**
  * `fromutc` (Impact: 2162.2 | O(2^N) | DB: 26)
  * `_accum` (Impact: 783.6 | O(2^N) | DB: 6)
  * `_ymd2ord` (Impact: 386.7 | O(2^N) | DB: 3)
  * `_check_tzname` (Impact: 181.2 | O(N^6))
    * *Intent:* # strftime is going to have at this: escape % Zreplace = s.replace('%', '%%') newformat.append(Zrepl...
  * `_normalize_date` (Impact: 63.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 440`, `args: 161`, `func_start: 161`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 84`, `dead_code: 8`, `fragile_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 66`, `import: 6`
* *Defense:* `safety: 111`, `doc: 100`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, __pypy__._pypydatetime, math, time, struct, _strptime
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/interpreter/baseobjspace.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.229 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.5 IQR)
- **Top Global Matches:** file_cluster_13: 12.229, file_cluster_0: 12.292, file_cluster_8: 12.352
- **Magnitude:** 4133.62 | **LOC:** 2294 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (13.8321%), Tech Debt (31.2669%)
**Top Internal Functions/Classes:**
  * `get_printable_location` (Impact: 637.4 | O(2^N) | DB: 2)
  * `_cached_compile` (Impact: 565.3 | O(N^6) | DB: 18)
  * `getbuiltinmodule` (Impact: 430.0 | O(2^N) | DB: 19)
  * `interp_w` (Impact: 160.5 | O(N^6) | DB: 1)
    * *Intent:* # For the reverse debugger: we run compiled watchpoint # expressions in a fast way that will crash i...
  * `exception_match` (Impact: 126.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 646`, `args: 210`, `func_start: 210`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 59`, `dead_code: 5`, `fragile_debt: 18`
* *Architecture:* `io: 19`, `api: 241`, `concurrency: 3`, `import: 53`
* *Defense:* `safety: 157`, `doc: 104`, `test: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.554
  * `Choke Point (Betweenness):` 0.027516 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` pypy.interpreter.module, pypy.interpreter.function, hashlib, pypy.module.__builtin__.interp_classobj, pypy.objspace.std.sliceobject, statement, rpython.rlib.rarithmetic, _warnings...
  * `Imported By (In-Degree: 124):` (Excluded from Brief to save tokens)

### `rpython/translator/c/src/dtoa.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.52 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.252 IQR)
- **Top Global Matches:** file_cluster_8: 14.52, file_cluster_13: 14.626, file_cluster_11: 14.685
- **Magnitude:** 4020.04 | **LOC:** 3024 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 192
- **Risk Profile:** Cognitive Load (94.8202%), Tech Debt (20.2359%)
**Top Internal Functions/Classes:**
  * `sd2b` (Impact: 2529.1 | O(2^N) | DB: 192)
    * *Intent:* /* count trailing 0 bits in the 32-bit integer y, and shift y right by that number of bits. */
  * `mult` (Impact: 67.3 | O(N^4) | DB: 61)
  * `s2b` (Impact: 37.4 | O(N^3) | DB: 16)
    * *Intent:* #else #define Storeinc(a,b,c) (((unsigned short *)a)[0] = (unsigned short)b, \
  * `Balloc` (Impact: 36.0 | O(N^4) | DB: 11)
    * *Intent:* * result in the hard case, we use floating-point * arithmetic to determine the adjustment to within ...
  * `pow5mult` (Impact: 29.7 | O(N^4) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 56`, `args: 15`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1072`, `dead_code: 3`, `fragile_debt: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 124`, `import: 7`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, limits.h, asm.h, string.h, float.h, stdio.h, stdlib.h, assert.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/translator/simplify.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.449 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.534 IQR)
- **Top Global Matches:** file_cluster_8: 12.449, file_cluster_13: 12.482, file_cluster_17: 12.574
- **Magnitude:** 3991.28 | **LOC:** 1089 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (50.5984%), Tech Debt (15.6915%)
**Top Internal Functions/Classes:**
  * `transform_ovfcheck` (Impact: 3696.7 | O(2^N) | DB: 53)
  * `replace_exitswitch_by_constant` (Impact: 37.0 | O(N^5))
  * `eliminate_empty_blocks` (Impact: 26.8 | O(N^4))
    * *Intent:* # ____________________________________________________________ def eliminate_empty_blocks(graph): ""...
  * `get_graph` (Impact: 13.7 | O(N^2))
  * `simplify_graph` (Impact: 8.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 187`, `args: 43`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 145`, `dead_code: 2`, `fragile_debt: 4`
* *Architecture:* `api: 46`, `import: 10`
* *Defense:* `safety: 52`, `doc: 34`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.517
  * `Choke Point (Betweenness):` 0.002444 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` rpython.rtyper.lltypesystem, rpython.flowspace.model, py, rpython.translator, rpython.translator.backendopt.ssa, collections, rpython.rtyper.lltypesystem.lloperation, rpython.tool.algo.unionfind...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `rpython/rtyper/lltypesystem/ll2ctypes.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.89 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.838 IQR)
- **Top Global Matches:** file_cluster_13: 12.89, file_cluster_8: 13.008, file_cluster_0: 13.034
- **Magnitude:** 3940.3 | **LOC:** 1631 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (53.2365%), Tech Debt (64.3733%)
**Top Internal Functions/Classes:**
  * `get_libc_name` (Impact: 1142.0 | O(2^N) | DB: 37)
  * `lltype2ctypes` (Impact: 773.9 | O(2^N) | DB: 9)
  * `build_new_ctypes_type` (Impact: 638.3 | O(N^6) | DB: 15)
  * `build_ctypes_struct` (Impact: 411.4 | O(2^N) | DB: 2)
    * *Intent:* # for unicode strings, do not use ctypes.c_wchar because ctypes # automatically converts arrays into...
  * `ctypes2lltype` (Impact: 342.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 354`, `args: 99`, `func_start: 98`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 90`, `dead_code: 10`, `fragile_debt: 11`, `duplicate_logic: 4`
* *Architecture:* `io: 20`, `api: 68`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 183`, `doc: 22`, `test: 21`, `sync_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.312
  * `Choke Point (Betweenness):` 0.00169 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` rpython.rtyper.lltypesystem, tempfile, array, rpython.rtyper.llannotation, rpython.rlib.rarithmetic, rpython.translator.platform, os, rpython.rlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib_pypy/_sqlite3.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.656 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.439 IQR)
- **Top Global Matches:** file_cluster_0: 12.656, file_cluster_8: 12.749, file_cluster_13: 12.856
- **Magnitude:** 3755.14 | **LOC:** 1407 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (75.2415%), Tech Debt (13.7008%)
**Top Internal Functions/Classes:**
  * `cursor` (Impact: 3118.2 | O(2^N) | DB: 66)
  * `_get_exception` (Impact: 49.2 | O(N^4))
  * `__init__` (Impact: 39.8 | O(N^4) | DB: 32)
  * `__do_all_statements` (Impact: 36.5 | O(N^5))
  * `connect` (Impact: 25.9 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 257`, `args: 100`, `func_start: 97`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 242`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 7`, `api: 59`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 98`, `test: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, functools, datetime, sqlite3.dump, sys, _sqlite3_cffi, __pypy__, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/rtyper/lltypesystem/rstr.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.188 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.745 IQR)
- **Top Global Matches:** file_cluster_0: 10.188, file_cluster_8: 10.352, file_cluster_13: 10.573
- **Magnitude:** 3679.76 | **LOC:** 1322 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (37.6034%), Tech Debt (18.8867%)
**Top Internal Functions/Classes:**
  * `_new_copy_contents_fun` (Impact: 3536.2 | O(2^N) | DB: 7)
  * `ll_striter` (Impact: 11.0 | O(N^2))
  * `new_malloc` (Impact: 10.8 | O(N^3))
  * `ll_strnext` (Impact: 5.5 | O(N^2))
  * `emptystrfun` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 270`, `args: 75`, `func_start: 73`, `class_start: 9`
* *Risk/State:* `state_mutation: 13`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 7`
* *Architecture:* `api: 74`, `import: 23`
* *Defense:* `safety: 37`, `doc: 6`, `test: 16`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.616
  * `Choke Point (Betweenness):` 0.00193 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` rpython.rtyper.lltypesystem, rpython.rtyper.rint, rpython.rlib.rarithmetic, rpython.rtyper.rstr, rpython.rtyper.error, rpython.rlib.rstring, rpython.rlib, rpython.annotator...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `lib_pypy/cffi/cparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.033 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.044 IQR)
- **Top Global Matches:** file_cluster_8: 12.033, file_cluster_13: 12.233, file_cluster_17: 12.365
- **Magnitude:** 3658.82 | **LOC:** 1016 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (45.1773%), Tech Debt (28.1011%)
**Top Internal Functions/Classes:**
  * `_put_back_line_directives` (Impact: 3279.0 | O(2^N) | DB: 34)
  * `_workaround_for_old_pycparser` (Impact: 224.4 | O(N^6) | DB: 13)
    * *Intent:* # Workaround for a pycparser issue (fixed between pycparser 2.10 and # 2.14): "char*const***" gives ...
  * `_get_parser` (Impact: 5.4 | O(N^2) | DB: 1)
  * `_workaround_for_static_import_finders` (Impact: 2.0 | O(N^1))
    * *Intent:* # Issue #392: packaging tools like cx_Freeze can not find these # because pycparser uses exec dynami...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 232`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 122`, `dead_code: 2`, `fragile_debt: 8`
* *Architecture:* `io: 1`, `api: 10`, `import: 13`
* *Defense:* `safety: 77`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .error, re, thread, .commontypes, _thread, warnings, sys, pycparser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/objspace/descroperation.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.664 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.573 IQR)
- **Top Global Matches:** file_cluster_0: 10.664, file_cluster_8: 10.69, file_cluster_13: 10.916
- **Magnitude:** 3580.64 | **LOC:** 997 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (27.1262%), Tech Debt (28.5334%)
**Top Internal Functions/Classes:**
  * `raiseattrerror` (Impact: 3203.3 | O(2^N))
  * `_make_unaryop_impl` (Impact: 269.8 | O(2^N))
  * `object_getattribute` (Impact: 1.9 | O(N^1))
  * `object_setattr` (Impact: 1.9 | O(N^1))
  * `object_delattr` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 276`, `args: 79`, `func_start: 77`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 7`
* *Architecture:* `api: 74`, `import: 11`
* *Defense:* `safety: 22`, `doc: 10`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.968
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` rpython.rlib.objectmodel, pypy.interpreter.error, pypy.interpreter.function, pypy.module.__builtin__.interp_classobj, pypy.interpreter.typedef, pypy.objspace.std.typeobject, pypy.interpreter.argument, rpython.tool.sourcetools...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pypy/objspace/std/unicodeobject.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.583 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.634 IQR)
- **Top Global Matches:** file_cluster_8: 11.583, file_cluster_13: 11.671, file_cluster_0: 11.679
- **Magnitude:** 3516.5 | **LOC:** 1944 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (12.1239%), Tech Debt (63.8051%)
**Top Internal Functions/Classes:**
  * `convert_arg_to_w_unicode` (Impact: 1621.2 | O(2^N) | DB: 9)
  * `unicode_from_encoded_object` (Impact: 305.6 | O(2^N) | DB: 2)
  * `encode_object` (Impact: 156.0 | O(N^5) | DB: 6)
  * `__repr__` (Impact: 100.7 | O(N^6))
  * `descr_splitlines` (Impact: 71.4 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 520`, `args: 195`, `func_start: 194`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 44`, `dead_code: 3`, `fragile_debt: 8`, `duplicate_logic: 6`
* *Architecture:* `io: 5`, `api: 131`, `import: 26`
* *Defense:* `safety: 80`, `doc: 132`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.684
  * `Choke Point (Betweenness):` 0.00275 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` pypy.objspace.std, pypy.interpreter.typedef, .bytearrayobject, pypy.objspace.std.sliceobject, rpython.rlib.rarithmetic, rpython.rlib.buffer, rpython.rlib.rstring, rpython.rlib...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `rpython/rlib/fastutf8/src/utf8.c` (C) | Magnitude: 315.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 116, state_mutation: 110, api: 50, pointers: 37
- `py/_code/code.py` (PYTHON) | Magnitude: 1358.34 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 530, structural_boundaries: 181, branch: 132, state_mutation: 129
- `pypy/objspace/std/mapdict.py` (PYTHON) | Magnitude: 1815.1 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1134, structural_boundaries: 452, encapsulation: 288, branch: 238
- `pypy/module/faulthandler/handler.py` (PYTHON) | Magnitude: 267.4 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 57, args: 29, func_start: 29
- `pypy/module/imp/importing.py` (PYTHON) | Magnitude: 21207.29 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 766, branch: 266, structural_boundaries: 227, safety: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pypy/module/_cppyy/src/dummy_backend.cxx` (CPP) | Magnitude: 2086.38 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 969, indent_spaces: 865, branch: 309, structural_boundaries: 164

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `rpython/rlib/rvmprof/src/shared/libbacktrace/filenames.h` (C) | Magnitude: 23.02 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 31, reflection_metaprogramming: 16, branch: 11, pointers: 10
- `pypy/module/_multibytecodec/src/cjkcodecs/alg_jisx0201.h` (C) | Magnitude: 53.46 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 30, branch: 22, indent_spaces: 17, api: 8
- `rpython/translator/c/src/asm_gcc_x86_64.h` (C) | Magnitude: 24.64 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, macros: 3, indent_spaces: 3, branch: 2
- `rpython/translator/c/src/stack.h` (C) | Magnitude: 26.66 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 20, reflection_metaprogramming: 9, api: 7, branch: 6
- `rpython/translator/c/src/debug_print.h` (C) | Magnitude: 31.78 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 23, reflection_metaprogramming: 11, api: 10, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pypy/interpreter/pyparser/pyparse.py` (PYTHON) | Magnitude: 286.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, branch: 44, structural_boundaries: 36, encapsulation: 19
- `pypy/module/__builtin__/app_inspect.py` (PYTHON) | Magnitude: 229.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 28, encapsulation: 27, branch: 23
- `pypy/module/faulthandler/dumper.py` (PYTHON) | Magnitude: 34.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, encapsulation: 13, branch: 6
- `rpython/jit/backend/ppc/locations.py` (PYTHON) | Magnitude: 146.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 94, args: 40, func_start: 40
- `rpython/translator/backendopt/stat.py` (PYTHON) | Magnitude: 172.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, branch: 18, state_mutation: 12, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `lib_pypy/_structseq.py` (PYTHON) | Magnitude: 305.94 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, encapsulation: 42, branch: 36, structural_boundaries: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `rpython/translator/backendopt/inline.py` (PYTHON) | Magnitude: 1392.48 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 580, branch: 181, structural_boundaries: 136, state_mutation: 73
- `pypy/tool/pydis.py` (PYTHON) | Magnitude: 310.04 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 143, state_mutation: 49, branch: 42, structural_boundaries: 35
- `rpython/memory/gctransform/shadowcolor.py` (PYTHON) | Magnitude: 2818.82 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 551, branch: 232, structural_boundaries: 121, state_mutation: 107
- `lib_pypy/pyrepl/unix_eventqueue.py` (PYTHON) | Magnitude: 143.76 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 42, structural_boundaries: 18, branch: 11
- `rpython/translator/backendopt/constfold.py` (PYTHON) | Magnitude: 830.96 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 303, branch: 119, structural_boundaries: 76, safety: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pypy/tool/watchdog_nt.py` (PYTHON) | Magnitude: 15.3 | Delta: **0.314 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, io: 9, structural_boundaries: 7, concurrency: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `lib_pypy/_cffi_ssl/_cffi_src/openssl/crypto.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 8, dead_code: 6, structural_boundaries: 2, import: 1
- `lib_pypy/_cffi_ssl/_cffi_src/openssl/cryptography.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 8, dead_code: 6, structural_boundaries: 2, import: 1
- `lib_pypy/_cffi_ssl/_cffi_src/openssl/evp.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 9, doc: 8, structural_boundaries: 2, import: 1
- `lib_pypy/_cffi_ssl/_cffi_src/openssl/ocsp.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 8, dead_code: 6, structural_boundaries: 2, import: 1
- `lib_pypy/_cffi_ssl/_cffi_src/openssl/x509.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 8, dead_code: 6, structural_boundaries: 2, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `lib_pypy/pyrepl/console.py` (PYTHON) | Magnitude: 81.42 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 33, api: 32, doc: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `rpython/memory/gc/minimark.py` (PYTHON) | Magnitude: 2804.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1131, state_mutation: 306, branch: 230, structural_boundaries: 197
- `rpython/tool/gcanalyze.py` (PYTHON) | Magnitude: 55.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, branch: 17, io: 12, state_mutation: 12
- `rpython/tool/runsubprocess.py` (PYTHON) | Magnitude: 83.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, branch: 27, structural_boundaries: 21, encapsulation: 19
- `lib_pypy/cffi/_pycparser/_build_tables.py` (PYTHON) | Magnitude: 15.3 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, import: 7, indent_spaces: 3, io: 2
- `rpython/rtyper/extfunc.py` (PYTHON) | Magnitude: 254.46 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 40, branch: 23, api: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `lib_pypy/_cffi_ssl/_cffi_src/openssl/ssl.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 22, doc: 8, structural_boundaries: 2, import: 1
- `lib_pypy/cffi/lock.py` (PYTHON) | Magnitude: 15.22 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: dead_code: 10, structural_boundaries: 9, indent_spaces: 8, import: 5
- `lib_pypy/_cffi_ssl/_cffi_src/openssl/provider.py` (PYTHON) | Magnitude: 12.08 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 8, dead_code: 3
- `rpython/jit/backend/x86/arch.py` (PYTHON) | Magnitude: 15.6 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 22, branch: 9, io: 3, fragile_debt: 3
- `rpython/rlib/rvmprof/src/shared/vmprof_getpc.h` (C) | Magnitude: 5.82 | Delta: **0.239 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 14, import: 7, ownership: 6, pointers: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pypy/objspace/std/mapdict.py` -> Churn: **100.0%** | Cog Load: 36.4498% | Debt: 99.9531%
- `rpython/translator/c/src/thread.h` -> Churn: **76.8%** | Cog Load: 54.612% | Debt: 0.0%
- `rpython/rtyper/lltypesystem/ll2ctypes.py` -> Churn: **60.86%** | Cog Load: 53.2365% | Debt: 64.3733%
- `rpython/translator/c/src/signals.c` -> Churn: **60.86%** | Cog Load: 77.3529% | Debt: 98.9915%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rpython/jit/metainterp/pyjitpl.py` -> **CF Bolz-Tereick** (100.0% isolated ownership) | Magnitude: 7619.34
- `lib_pypy/cffi/_pycparser/ply/yacc.py` -> **Charalampos Stratakis** (100.0% isolated ownership) | Magnitude: 6160.3
- `rpython/rtyper/lltypesystem/ll2ctypes.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 3940.3
- `rpython/jit/codewriter/jtransform.py` -> **CF Bolz-Tereick** (100.0% isolated ownership) | Magnitude: 3309.5
- `pypy/module/cpyext/api.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 2553.3

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rpython/rtyper/annlowlevel.py` -> **Severity: 1.086** (Bridge: 0.0115 * Flux: 94.3643%)
- `rpython/jit/metainterp/history.py` -> **Severity: 0.933** (Bridge: 0.0095 * Flux: 97.8861%)
- `pypy/module/cpyext/api.py` -> **Severity: 0.851** (Bridge: 0.0094 * Flux: 90.1562%)
- `pypy/interpreter/baseobjspace.py` -> **Severity: 0.847** (Bridge: 0.0275 * Flux: 30.7782%)
- `rpython/translator/translator.py` -> **Severity: 0.824** (Bridge: 0.0082 * Flux: 99.9593%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pypy/interpreter/error.py` -> **Severity: 3848.232** (Blast Radius: 38.535 * Doc Risk: 99.8633%)
- `pypy/module/micronumpy/types.py` -> **Severity: 2213.491** (Blast Radius: 22.135 * Doc Risk: 99.9996%)
- `pypy/interpreter/baseobjspace.py` -> **Severity: 2055.207** (Blast Radius: 20.554 * Doc Risk: 99.9906%)
- `rpython/jit/metainterp/optimizeopt/unroll.py` -> **Severity: 1644.1** (Blast Radius: 16.441 * Doc Risk: 100.0%)
- `rpython/tool/ansi_print.py` -> **Severity: 1335.089** (Blast Radius: 13.351 * Doc Risk: 99.9992%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
