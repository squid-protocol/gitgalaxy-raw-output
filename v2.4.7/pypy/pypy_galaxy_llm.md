# ARCHITECTURAL_BRIEF: pypy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/pypy` |
| **Timestamp** | `2026-08-07T04:01:24.475588+00:00` |
| **Scan Duration** | `10.67s` |
| **Git Branch** | `main` |
| **Git Commit** | `e371778f304422ddbb06fdf373c557a7d643c68f` |
| **Git Remote** | `https://github.com/pypy/pypy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1752 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
> **Architectural Drift Z-Score:** `5.512`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1005 | 56.2% |
| file_cluster_13 | 621 | 34.7% |
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
| Cognitive Load Exposure | 0.0 | 97.6 | 23.3 | 13.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 40.5 | 47.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 40.0 | 15.9 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 25.2 | 2.5 | 80.0 |
| API Exposure | 0.0 | 18.4 | 5.4 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 41.3 | 19.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.4 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 58.5 | 66.4 | 3.2 |
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

- `_Cryptography_pem_password_cb` (@ `lib_pypy/_cffi_ssl/_stdssl/__init__.py`) -> Impact: **931.7** | LOC: 1460
- `_opimpl_assert_green` (@ `rpython/jit/metainterp/pyjitpl.py`) -> Impact: **749.5** | LOC: 2104
- `_get_printable_location` (@ `pypy/objspace/std/listobject.py`) -> Impact: **732.9** | LOC: 2258
- `str_decode_unicode_escape` (@ `pypy/interpreter/unicodehelper.py`) -> Impact: **681.2** | LOC: 1132
- `_assemble_loop` (@ `rpython/jit/backend/riscv/assembler.py`) -> Impact: **664.3** | LOC: 1713
- `transform_ovfcheck` (@ `rpython/translator/simplify.py`) -> Impact: **568.6** | LOC: 946
- `_new_copy_contents_fun` (@ `rpython/rtyper/lltypesystem/rstr.py`) -> Impact: **557.8** | LOC: 1228
- `__new__` (@ `rpython/rtyper/lltypesystem/lltype.py`) -> Impact: **542.8** | LOC: 1056
- `getfield` (@ `pypy/module/micronumpy/ndarray.py`) -> Impact: **520.5** | LOC: 1090
- `optimize_vector` (@ `rpython/jit/metainterp/optimizeopt/vector.py`) -> Impact: **518.5** | LOC: 754

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pypy/module/imp` | 4 | 21316.59 | 8.88% | 31.55% |
| `pypy/objspace/std` | 40 | 14619.38 | 20.25% | 32.62% |
| `rpython/jit/backend/x86` | 17 | 12892.71 | 22.47% | 46.08% |
| `pypy/module/micronumpy` | 27 | 12330.48 | 37.99% | 44.83% |
| `rpython/jit/metainterp` | 28 | 11366.86 | 30.95% | 46.8% |
| `rpython/jit/metainterp/optimizeopt` | 26 | 10664.59 | 29.42% | 53.23% |
| `pypy/interpreter` | 30 | 10178.98 | 24.63% | 45.84% |
| `rpython/rtyper/lltypesystem` | 20 | 8447.4 | 24.14% | 55.95% |
| `rpython/rtyper` | 33 | 8305.92 | 26.0% | 58.02% |
| `lib_pypy/pyrepl` | 23 | 8150.18 | 31.27% | 61.23% |

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
- `pypy/module/micronumpy/types.py` -> **0** Orphaned Functions | **99** Duplicates
- `extra_tests/cffi_tests/test_c.py` -> **83** Orphaned Functions | **0** Duplicates

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

### Hardcoded Payload Artifacts
- `lib_pypy/_cffi_ssl/_stdssl/certificate.py` -> **95.203%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `13` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `9050` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `rpython/translator/c/src/signals.c` (C) -> Cumulative Risk: **727.66**
- **Archetype:** `file_cluster_13` (Distance: 12.904 IQR)
- **Magnitude:** 159.24 | **LOC:** 273 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.9915%)
- **Heaviest Functions:** `signal_setflag_handler` (Impact: 24.3), `pypysig_poll` (Impact: 9.4), `pypysig_siginterrupt` (Impact: 9.4)

### 2. `rpython/translator/c/src/thread_pthread.c` (C) -> Cumulative Risk: **704.29**
- **Archetype:** `file_cluster_13` (Distance: 13.402 IQR)
- **Magnitude:** 365.9 | **LOC:** 617 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (89.3105%)
- **Heaviest Functions:** `RPyThreadAcquireLockTimed` (Impact: 46.2), `RPyThreadSetStackSize` (Impact: 12.8), `RPyThreadReleaseLock` (Impact: 4.8)

### 3. `rpython/jit/tl/tlc.py` (PYTHON) -> Cumulative Risk: **678.23**
- **Archetype:** `file_cluster_13` (Distance: 13.108 IQR)
- **Magnitude:** 661.26 | **LOC:** 484 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (98.9371%)
- **Heaviest Functions:** `interp` (Impact: 154.8), `make_interp` (Impact: 124.5), `get` (Impact: 7.3)

### 4. `rpython/jit/backend/ppc/form.py` (PYTHON) -> Cumulative Risk: **671.66**
- **Archetype:** `file_cluster_17` (Distance: 12.636 IQR)
- **Magnitude:** 206.58 | **LOC:** 195 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Tech Debt (98.0207%), Cognitive Load (97.0527%)
- **Heaviest Functions:** `__call__` (Impact: 101.2), `calc_fields` (Impact: 12.8), `__init__` (Impact: 5.4)

### 5. `pypy/module/_multibytecodec/src/cjkcodecs/_codecs_jp.c` (C) -> Cumulative Risk: **666.52**
- **Archetype:** `file_cluster_8` (Distance: 11.841 IQR)
- **Magnitude:** 417.3 | **LOC:** 732 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (99.531%), Cognitive Load (94.2382%)
- **Heaviest Functions:** `TRYMAP_ENC` (Impact: 12.6), `TRYMAP_ENC` (Impact: 12.6), `TRYMAP_ENC` (Impact: 6.6)

### 6. `pypy/module/cpyext/src/abstract.c` (C) -> Cumulative Risk: **665.13**
- **Archetype:** `file_cluster_8` (Distance: 12.702 IQR)
- **Magnitude:** 500.22 | **LOC:** 536 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.7734%), Tech Debt (97.4961%)
- **Heaviest Functions:** `PyBuffer_ToContiguous` (Impact: 20.3), `PyObject_CallMethod` (Impact: 10.9), `_PyObject_CallMethod_SizeT` (Impact: 10.9)

### 7. `rpython/rlib/rvmprof/src/shared/vmprof_win.c` (C) -> Cumulative Risk: **658.66**
- **Archetype:** `file_cluster_13` (Distance: 12.068 IQR)
- **Magnitude:** 158.88 | **LOC:** 258 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.5138%), Cognitive Load (89.5336%)
- **Heaviest Functions:** `vmprof_snapshot_thread` (Impact: 42.1), `vmp_write_all` (Impact: 8.2), `prepare_concurrent_bufs` (Impact: 3.1)

### 8. `pypy/module/_multibytecodec/src/cjkcodecs/multibytecodec.c` (C) -> Cumulative Risk: **656.37**
- **Archetype:** `file_cluster_8` (Distance: 13.092 IQR)
- **Magnitude:** 320.06 | **LOC:** 266 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9725%), Tech Debt (99.8804%)
- **Heaviest Functions:** `pypy_cjk_enc_chunk` (Impact: 11.3), `pypy_cjk_dec_chunk` (Impact: 10.9), `pypy_cjk_enc_reset` (Impact: 10.8)

### 9. `rpython/translator/gensupp.py` (PYTHON) -> Cumulative Risk: **655.62**
- **Archetype:** `file_cluster_17` (Distance: 15.917 IQR)
- **Magnitude:** 135.86 | **LOC:** 119 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.5186%), Documentation (91.2153%)
- **Heaviest Functions:** `uniquemodulename` (Impact: 52.4), `make_reserved_names` (Impact: 38.8)

### 10. `rpython/rlib/rvmprof/src/shared/vmprof_common.c` (C) -> Cumulative Risk: **646.71**
- **Archetype:** `file_cluster_13` (Distance: 13.064 IQR)
- **Magnitude:** 313.64 | **LOC:** 301 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.92%), Documentation (99.7976%)
- **Heaviest Functions:** `vmprof_init` (Impact: 35.7), `opened_profile` (Impact: 19.8), `vmprof_get_traceback` (Impact: 12.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pypy/module/imp/importing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.756 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.194 IQR)
- **Top Global Matches:** file_cluster_0: 11.756, file_cluster_8: 11.768, file_cluster_13: 11.784
- **Magnitude:** 21207.29 | **LOC:** 1154 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.8534%), Tech Debt (26.2196%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 227`, `args: 59`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 35`, `dead_code: 5`, `fragile_debt: 8`
* *Architecture:* `io: 45`, `api: 46`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 87`, `doc: 34`, `test: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.582
  * `Choke Point (Betweenness):` 0.000878 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` lock., lock, x, pypy.interpreter.pycode, for, pypy.module.cpyext.api, rpython.rlib, parent...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rpython/jit/backend/x86/rx86.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.965 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.574 IQR)
- **Top Global Matches:** file_cluster_8: 9.965, file_cluster_0: 10.347, file_cluster_13: 10.513
- **Magnitude:** 8885.73 | **LOC:** 1057 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2456%), Tech Debt (16.2903%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 168`, `args: 77`, `func_start: 77`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 25`, `dead_code: 3`, `fragile_debt: 4`
* *Architecture:* `api: 79`, `import: 7`
* *Defense:* `safety: 29`, `doc: 2`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` py, rpython.rtyper.lltypesystem, rpython.rlib.rarithmetic, rpython.rlib.objectmodel, rpython.jit.backend.x86.arch, rpython.rlib.unroll
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib_pypy/pyrepl/readline.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.984 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.551 IQR)
- **Top Global Matches:** file_cluster_8: 10.984, file_cluster_13: 11.11, file_cluster_0: 11.31
- **Magnitude:** 5317.94 | **LOC:** 490 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.2606%), Tech Debt (34.7016%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 102`, `args: 41`, `func_start: 41`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 45`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 3`
* *Architecture:* `io: 14`, `api: 37`, `import: 7`
* *Defense:* `safety: 21`, `doc: 4`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.738
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sys, pyrepl.completing_reader, pyrepl.unix_console, warnings, os, __builtin__, pyrepl, pyrepl.historical_reader
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rpython/rtyper/lltypesystem/module/ll_math.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.112 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.818 IQR)
- **Top Global Matches:** file_cluster_8: 8.112, file_cluster_13: 8.837, file_cluster_7: 8.964
- **Magnitude:** 5173.96 | **LOC:** 406 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.4978%), Tech Debt (20.8609%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 102`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 1`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 21`, `import: 13`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.384
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rpython.rlib.rfloat, rpython.rlib, sys, py, math, rpython.tool.sourcetools, rpython.rtyper.lltypesystem, statement...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib_pypy/cffi/_pycparser/ply/yacc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.793 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.354 IQR)
- **Top Global Matches:** file_cluster_8: 12.793, file_cluster_17: 12.95, file_cluster_13: 13.021
- **Magnitude:** 2475.7 | **LOC:** 3426 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (87.2622%), Tech Debt (93.0125%)
**Top Internal Functions/Classes:**
  * `yacc` (Impact: 280.2)
    * *Intent:* # Secondary validation step that looks for p_ definitions that are not functions # or functions that...
  * `parse_grammar` (Impact: 167.6)
    * *Intent:* # === INTROSPECTION === # # The following functions and classes are used to implement the PLY # intr...
  * `parsedebug` (Impact: 157.0)
    * *Intent:* # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! # parsedebug(). # # ...
  * `parseopt` (Impact: 144.4)
    * *Intent:* #--! parsedebug-end # parseopt(). # # Optimized version of parse() method. DO NOT EDIT THIS CODE DIR...
  * `parseopt_notrack` (Impact: 132.6)
    * *Intent:* #--! parseopt-end # parseopt_notrack(). # # Optimized version of parseopt() with line number trackin...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 602`, `structural_boundaries: 347`, `args: 110`, `func_start: 105`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 559`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 22`, `orphaned_logic: 11`
* *Architecture:* `io: 26`, `api: 91`, `import: 10`
* *Defense:* `safety: 107`, `doc: 8`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` types, sys, , warnings, inspect, re, base64, os.path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/jit/metainterp/pyjitpl.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.464 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.042 IQR)
- **Top Global Matches:** file_cluster_0: 12.464, file_cluster_13: 12.743, file_cluster_8: 12.839
- **Magnitude:** 2291.04 | **LOC:** 3900 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.0984%), Tech Debt (23.115%)
**Top Internal Functions/Classes:**
  * `_opimpl_assert_green` (Impact: 749.5)
  * `get_list_of_active_boxes` (Impact: 39.6)
  * `opimpl_jit_merge_point` (Impact: 37.7)
  * `_try_tco` (Impact: 33.4)
  * `_opimpl_recursive_call` (Impact: 31.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 743`, `args: 268`, `func_start: 268`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 3`, `state_mutation: 292`, `dead_code: 22`, `fragile_debt: 14`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 291`, `import: 49`
* *Defense:* `safety: 182`, `doc: 32`, `test: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 0.000678 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` rpython.jit.metainterp.warmstate, rpython.jit.backend.llsupport.ffisupport, rpython.jit.metainterp.support, rpython.rtyper.annlowlevel, rpython.jit.metainterp.jitprof, rpython.rlib.debug, rpython.rlib.rvmprof, rpython.rlib...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rpython/rlib/rvmprof/src/shared/libbacktrace/dwarf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.027 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.379 IQR)
- **Top Global Matches:** file_cluster_8: 14.027, file_cluster_13: 14.185, file_cluster_0: 14.273
- **Magnitude:** 2289.06 | **LOC:** 3039 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.2777%), Tech Debt (12.5251%)
**Top Internal Functions/Classes:**
  * `read_referenced_name` (Impact: 238.7)
  * `find_address_ranges` (Impact: 184.1)
  * `dwarf_lookup_pc` (Impact: 93.1)
  * `build_address_map` (Impact: 83.6)
  * `read_abbrevs` (Impact: 69.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 320`, `args: 24`, `func_start: 25`, `class_start: 58`
* *Risk/State:* `state_mutation: 906`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 309`, `import: 9`
* *Defense:* `safety: 38`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` backtrace.h, filenames.h, config.h, dwarf2.h, internal.h, errno.h, string.h, types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/rtyper/lltypesystem/lltype.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.379 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.066 IQR)
- **Top Global Matches:** file_cluster_0: 13.379, file_cluster_13: 13.461, file_cluster_17: 13.467
- **Magnitude:** 2150.28 | **LOC:** 2509 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.0301%), Tech Debt (99.8363%)
**Top Internal Functions/Classes:**
  * `__new__` (Impact: 542.8)
  * `build_number` (Impact: 513.7)
  * `__repr__` (Impact: 108.3)
    * *Intent:* #self._TYPE = TYPE
  * `__str__` (Impact: 80.0)
  * `malloc` (Impact: 49.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 815`, `args: 286`, `func_start: 285`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 180`, `dead_code: 17`, `planned_debt: 1`, `fragile_debt: 9`, `duplicate_logic: 41`
* *Architecture:* `api: 119`, `import: 22`
* *Defense:* `safety: 301`, `doc: 28`, `test: 63`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.728
  * `Choke Point (Betweenness):` 0.001486 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` types, weakref, rpython.rtyper.extregistry, rpython.rlib.rarithmetic, rpython.rtyper.lltypesystem, rpython.tool, rpython.annotator.model, rpython.rlib.objectmodel...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `pypy/module/cpyext/src/getargs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.337 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.11 IQR)
- **Top Global Matches:** file_cluster_8: 13.337, file_cluster_0: 13.579, file_cluster_13: 13.593
- **Magnitude:** 2138.34 | **LOC:** 1873 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.5063%), Tech Debt (16.8487%)
**Top Internal Functions/Classes:**
  * `convertsimple` (Impact: 473.6)
  * `skipitem` (Impact: 114.5)
  * `vgetargs1` (Impact: 69.6)
  * `vgetargskeywords` (Impact: 47.4)
  * `converttuple` (Impact: 28.6)
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

### `rpython/translator/c/src/dtoa.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.516 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.246 IQR)
- **Top Global Matches:** file_cluster_8: 14.516, file_cluster_13: 14.621, file_cluster_11: 14.679
- **Magnitude:** 2095.54 | **LOC:** 3024 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.0869%), Tech Debt (28.4905%)
**Top Internal Functions/Classes:**
  * `sd2b` (Impact: 388.3)
    * *Intent:* /* count trailing 0 bits in the 32-bit integer y, and shift y right by that number of bits. */
  * `__Py_dg_strtod` (Impact: 319.3)
  * `bigcomp` (Impact: 35.1)
  * `mult` (Impact: 29.8)
  * `s2b` (Impact: 19.5)
    * *Intent:* #else #define Storeinc(a,b,c) (((unsigned short *)a)[0] = (unsigned short)b, \
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 56`, `args: 8`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1072`, `dead_code: 3`, `fragile_debt: 4`, `orphaned_logic: 4`
* *Architecture:* `api: 124`, `import: 7`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, limits.h, asm.h, errno.h, assert.h, string.h, stdlib.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/memory/gc/incminimark.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.176 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.038 IQR)
- **Top Global Matches:** file_cluster_13: 13.176, file_cluster_8: 13.2, file_cluster_0: 13.298
- **Magnitude:** 1867.04 | **LOC:** 3407 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.2186%), Tech Debt (96.226%)
**Top Internal Functions/Classes:**
  * `major_collection_step` (Impact: 61.2)
  * `external_malloc` (Impact: 55.7)
    * *Intent:* # Pinned object in front of nursery_top. Try reserving totalsize # by jumping into the next, yet unu...
  * `_minor_collection` (Impact: 52.1)
    * *Intent:* # NB: if we are marking, we must not inspect the state of the # GCFLAG_TRACK_YOUNG_PTRS of source_ad...
  * `writebarrier_before_copy` (Impact: 48.4)
    * *Intent:* # which must have an array part; 'index' is the index of the # item that is (or contains) the pointe...
  * `setup` (Impact: 44.2)
    * *Intent:* # # 'large_object' limit how big objects can be in the nursery, so # it gives a lower bound on the a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 401`, `structural_boundaries: 329`, `args: 150`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 524`, `dead_code: 23`, `planned_debt: 2`, `fragile_debt: 21`, `duplicate_logic: 2`, `orphaned_logic: 34`
* *Architecture:* `io: 4`, `api: 104`, `import: 25`
* *Defense:* `safety: 10`, `doc: 48`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` rpython.rlib, sys, rpython.memory.support, rpython.memory.gc.base, rpython.rtyper.lltypesystem, rpython.rlib.rarithmetic, os, rpython.rtyper.lltypesystem.llmemory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/module/micronumpy/types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.019 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.426 IQR)
- **Top Global Matches:** file_cluster_0: 12.019, file_cluster_13: 12.62, file_cluster_8: 12.693
- **Magnitude:** 1816.64 | **LOC:** 2770 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.0108%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `unbox` (Impact: 328.4)
  * `unbox` (Impact: 61.1)
  * `record_coerce` (Impact: 39.9)
  * `make_integer_min_dtype` (Impact: 33.2)
  * `_coerce` (Impact: 26.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 1037`, `args: 378`, `func_start: 376`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 44`, `dead_code: 24`, `planned_debt: 3`, `fragile_debt: 8`, `duplicate_logic: 99`
* *Architecture:* `api: 382`, `import: 29`
* *Defense:* `safety: 184`, `doc: 10`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.135
  * `Choke Point (Betweenness):` 0.031003 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` rpython.rlib.rstruct.ieee, rpython.rlib.rstring, rpython.rtyper.annlowlevel, pypy.objspace.std.floatobject, rpython.rlib, pypy.module.micronumpy.descriptor, pypy.interpreter.error, rpython.rtyper.lltypesystem...
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `pypy/module/_cppyy/src/dummy_backend.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.28 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.93 IQR)
- **Top Global Matches:** file_cluster_11: 16.28, file_cluster_17: 16.356, file_cluster_13: 16.374
- **Magnitude:** 1800.38 | **LOC:** 1315 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3016%), Tech Debt (92.7639%)
**Top Internal Functions/Classes:**
  * `cppyy_call_v` (Impact: 249.5)
    * *Intent:* /* method/function dispatching -------------------------------------------- */
  * `cppyy_call_i` (Impact: 71.4)
  * `cppyy_call_l` (Impact: 43.8)
  * `cppyy_call_d` (Impact: 43.8)
  * `cppyy_constructor` (Impact: 39.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 164`, `args: 123`, `func_start: 82`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 969`, `dead_code: 19`, `duplicate_logic: 2`, `orphaned_logic: 49`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 105`, `immutability_locks: 37`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` vector, cwchar, memory, types.h, map, string, example01.cxx, datatypes.cxx...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib_pypy/_cffi_ssl/_stdssl/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.789 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.517 IQR)
- **Top Global Matches:** file_cluster_0: 11.789, file_cluster_8: 11.91, file_cluster_13: 11.949
- **Magnitude:** 1681.02 | **LOC:** 1981 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.9811%), Tech Debt (77.4737%)
**Top Internal Functions/Classes:**
  * `_Cryptography_pem_password_cb` (Impact: 931.7)
  * `write` (Impact: 69.7)
    * *Intent:* # just that no data is currently available. The SSL routines should retry # the read, which we can a...
  * `set_ecdh_curve` (Impact: 69.1)
  * `_add_ca_certs` (Impact: 56.3)
  * `load_verify_locations` (Impact: 53.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 467`, `structural_boundaries: 315`, `args: 105`, `func_start: 105`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 172`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 12`
* *Architecture:* `io: 37`, `api: 94`, `import: 19`
* *Defense:* `safety: 52`, `doc: 16`, `test: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __pypy__, weakref, sys, thread, _pypy_openssl, _cffi_ssl._stdssl.win32_extra, _cffi_ssl._stdssl.utility, _cffi_ssl._stdssl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/objspace/std/newformat.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.503 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.206 IQR)
- **Top Global Matches:** file_cluster_8: 11.503, file_cluster_13: 11.736, file_cluster_0: 11.743
- **Magnitude:** 1677.74 | **LOC:** 1190 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.2649%), Tech Debt (37.6626%)
**Top Internal Functions/Classes:**
  * `make_formatting_class` (Impact: 436.6)
  * `_format_int_or_long` (Impact: 220.8)
  * `make_template_formatting_class` (Impact: 175.6)
  * `_parse_spec` (Impact: 80.1)
  * `_calc_num_width` (Impact: 59.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 150`, `args: 49`, `func_start: 48`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 195`, `dead_code: 4`, `duplicate_logic: 8`
* *Architecture:* `io: 1`, `api: 26`, `import: 9`
* *Defense:* `safety: 15`, `doc: 16`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.343
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rpython.rlib.rfloat, rpython.rlib, sys, math, string, rpython.rlib.rarithmetic, rpython.rlib.objectmodel, pypy.interpreter.signature...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pypy/module/micronumpy/ufuncs.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.881 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.82 IQR)
- **Top Global Matches:** file_cluster_8: 11.881, file_cluster_13: 12.012, file_cluster_17: 12.146
- **Magnitude:** 1574.22 | **LOC:** 1624 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.9007%), Tech Debt (70.4384%)
**Top Internal Functions/Classes:**
  * `descr_repr` (Impact: 431.9)
  * `_raise_err_msg` (Impact: 303.0)
  * `call` (Impact: 128.7)
  * `frompyfunc` (Impact: 88.9)
  * `type_resolver` (Impact: 74.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 246`, `args: 57`, `func_start: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 198`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 8`, `duplicate_logic: 5`, `orphaned_logic: 3`
* *Architecture:* `api: 47`, `import: 22`
* *Defense:* `safety: 55`, `doc: 8`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` pypy.module.micronumpy.support, pypy.module.micronumpy.ndarray, rpython.rlib, pypy.module.micronumpy.ctors, pypy.module.micronumpy.descriptor, .casting, pypy.interpreter.gateway, rpython.rtyper.lltypesystem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/interpreter/baseobjspace.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.231 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.501 IQR)
- **Top Global Matches:** file_cluster_13: 12.231, file_cluster_0: 12.294, file_cluster_8: 12.354
- **Magnitude:** 1555.02 | **LOC:** 2294 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8442%), Tech Debt (31.2669%)
**Top Internal Functions/Classes:**
  * `_cached_compile` (Impact: 169.3)
  * `get_printable_location` (Impact: 107.4)
  * `getrepr` (Impact: 92.8)
  * `getbuiltinmodule` (Impact: 67.8)
  * `interp_w` (Impact: 48.7)
    * *Intent:* # For the reverse debugger: we run compiled watchpoint # expressions in a fast way that will crash i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 646`, `args: 210`, `func_start: 210`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 59`, `dead_code: 5`, `fragile_debt: 18`
* *Architecture:* `io: 19`, `api: 245`, `concurrency: 3`, `import: 53`
* *Defense:* `safety: 157`, `doc: 104`, `test: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.554
  * `Choke Point (Betweenness):` 0.027516 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` rpython.rlib.signature, pypy.interpreter.reverse_debugging, pypy.config.pypyoption, rpython.rlib.debug, pypy.interpreter.pycode, pypy.objspace.std.sliceobject, rpython.rlib, pypy.module.exceptions.moduledef...
  * `Imported By (In-Degree: 124):` (Excluded from Brief to save tokens)

### `extra_tests/cffi_tests/test_c.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.985 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.557 IQR)
- **Top Global Matches:** file_cluster_8: 12.985, file_cluster_13: 13.434, file_cluster_0: 13.461
- **Magnitude:** 1401.78 | **LOC:** 4527 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.6088%), Tech Debt (71.9863%)
**Top Internal Functions/Classes:**
  * `test_FILE` (Impact: 351.5)
  * `test_cannot_call_with_a_autocompleted_st` (Impact: 315.0)
  * `test_array_instance` (Impact: 31.6)
  * `test_struct_instance` (Impact: 27.1)
  * `test_cast_to_signed_char` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 1640`, `args: 276`, `func_start: 273`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 436`, `high_risk_execution: 1`, `state_mutation: 14`, `dead_code: 2`, `fragile_debt: 6`, `orphaned_logic: 83`
* *Architecture:* `io: 44`, `api: 268`, `import: 42`
* *Defense:* `safety: 1190`, `doc: 2`, `test: 1686`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` posix, _cffi_backend, ctypes.util, nt, sys, packaging.tags, gc, platform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/tool/ansi_mandelbrot.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.904 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.857 IQR)
- **Top Global Matches:** file_cluster_13: 11.904, file_cluster_8: 12.095, file_cluster_7: 12.342
- **Magnitude:** 1382.59 | **LOC:** 188 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.6603%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 27`, `args: 13`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 64`
* *Architecture:* `io: 4`, `api: 10`, `import: 7`
* *Defense:* `safety: 2`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.559
  * `Choke Point (Betweenness):` 0.000252 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` py.io, sys, __future__, os, ansiramp, time, random
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib_pypy/cffi/cparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.05 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.044 IQR)
- **Top Global Matches:** file_cluster_8: 12.05, file_cluster_13: 12.248, file_cluster_17: 12.38
- **Magnitude:** 1343.42 | **LOC:** 1016 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.1773%), Tech Debt (28.1011%)
**Top Internal Functions/Classes:**
  * `_put_back_line_directives` (Impact: 504.2)
  * `_get_type_and_quals` (Impact: 353.3)
  * `replace` (Impact: 138.9)
  * `_process_macros` (Impact: 83.1)
  * `_workaround_for_old_pycparser` (Impact: 68.5)
    * *Intent:* # Workaround for a pycparser issue (fixed between pycparser 2.10 and # 2.14): "char*const***" gives ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 232`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 122`, `dead_code: 2`, `fragile_debt: 8`
* *Architecture:* `io: 1`, `api: 10`, `import: 13`
* *Defense:* `safety: 77`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` weakref, sys, thread, pycparser, warnings, .commontypes, re, pycparser.lextab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/objspace/std/listobject.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.256 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.889 IQR)
- **Top Global Matches:** file_cluster_8: 12.256, file_cluster_13: 12.319, file_cluster_0: 12.375
- **Magnitude:** 1332.28 | **LOC:** 2530 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.2663%), Tech Debt (22.8057%)
**Top Internal Functions/Classes:**
  * `_get_printable_location` (Impact: 732.9)
  * `get_strategy_from_list_object` (Impact: 25.3)
  * `listrepr` (Impact: 19.6)
  * `make_range_list` (Impact: 11.7)
  * `_get_strategy_from_list_object_int_or_fl` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 773`, `args: 316`, `func_start: 307`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 176`, `dead_code: 2`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 273`, `import: 29`
* *Defense:* `safety: 105`, `doc: 90`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.152
  * `Choke Point (Betweenness):` 0.002353 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` pypy.objspace.std.bytesobject, rpython.rlib.rstring, pypy.objspace.std.floatobject, pypy.objspace.std.iterobject, pypy.objspace.std.sliceobject, rpython.rlib, pypy.objspace.std.unicodeobject, pypy.interpreter.gateway...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `rpython/jit/codewriter/jtransform.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.806 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.71 IQR)
- **Top Global Matches:** file_cluster_8: 11.806, file_cluster_13: 12.036, file_cluster_0: 12.122
- **Magnitude:** 1276.4 | **LOC:** 2291 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.4895%), Tech Debt (26.1684%)
**Top Internal Functions/Classes:**
  * `handle_recursive_call` (Impact: 250.1)
    * *Intent:* # If the resulting op1 is still a direct_call, turn it into a # residual_call.
  * `rewrite_op_gc_store_indexed` (Impact: 210.9)
  * `_check_no_vable_array` (Impact: 103.3)
  * `_handle_libffi_call` (Impact: 47.5)
  * `_handle_stroruni_call` (Impact: 37.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 428`, `structural_boundaries: 510`, `args: 153`, `func_start: 153`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 1`, `state_mutation: 103`, `dead_code: 11`, `fragile_debt: 18`
* *Architecture:* `api: 138`, `import: 18`
* *Defense:* `safety: 147`, `doc: 22`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.618
  * `Choke Point (Betweenness):` 0.00016 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` rpython.rlib.jit, rpython.flowspace.model, rpython.translator.unsimplify, rpython.rlib, py, rpython.jit.metainterp, rpython.jit.metainterp.blackhole, rpython.jit.codewriter.policy...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rpython/jit/backend/x86/assembler.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.642 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.715 IQR)
- **Top Global Matches:** file_cluster_8: 12.642, file_cluster_13: 12.662, file_cluster_0: 12.809
- **Magnitude:** 1274.4 | **LOC:** 2782 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.6334%), Tech Debt (25.5132%)
**Top Internal Functions/Classes:**
  * `dump` (Impact: 504.8)
    * *Intent:* # some minimal sanity checking old_nbargs = oldlooptoken.compiled_loop_token._debug_nbargs new_nbarg...
  * `_build_wb_slowpath` (Impact: 59.0)
    * *Intent:* # # patch the JNZ above # From now on this function is basically "merged" with # its caller and so c...
  * `assemble_loop` (Impact: 40.6)
  * `_build_malloc_slowpath` (Impact: 37.2)
  * `assemble_bridge` (Impact: 27.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 388`, `structural_boundaries: 408`, `args: 177`, `func_start: 177`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 170`, `dead_code: 16`, `planned_debt: 5`, `fragile_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `api: 141`, `import: 39`
* *Defense:* `safety: 179`, `doc: 20`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.258
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` rpython.rlib.rvmprof.rvmprof, rpython.jit.backend.x86.jump, rpython.jit.backend.llsupport.asmmemmgr, rpython.jit.backend.x86, rpython.jit.backend.llsupport, rpython.rtyper.annlowlevel, rpython.jit.metainterp.compile, rpython.rlib.debug...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pypy/module/micronumpy/descriptor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.151 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.547 IQR)
- **Top Global Matches:** file_cluster_8: 12.151, file_cluster_13: 12.28, file_cluster_0: 12.383
- **Magnitude:** 1272.24 | **LOC:** 1491 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.0785%), Tech Debt (10.6861%)
**Top Internal Functions/Classes:**
  * `byteorder_w` (Impact: 316.6)
  * `make_new_dtype` (Impact: 224.9)
  * `dtype_from_list` (Impact: 129.8)
  * `dtype_from_dict` (Impact: 54.8)
  * `dtype_from_spec` (Impact: 31.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 315`, `args: 88`, `func_start: 87`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 254`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `api: 82`, `import: 22`
* *Defense:* `safety: 59`, `doc: 6`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.003356 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` rpython.rlib, pypy.module.micronumpy.appbridge, pypy.module.micronumpy.converters, pypy.interpreter.baseobjspace, .base, pypy.module.micronumpy, pypy.interpreter.argument, string...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `py/_path/svnwc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.152 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.41 IQR)
- **Top Global Matches:** file_cluster_13: 14.152, file_cluster_0: 14.188, file_cluster_17: 14.188
- **Magnitude:** 1263.6 | **LOC:** 1241 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.5448%), Tech Debt (79.5295%)
**Top Internal Functions/Classes:**
  * `checkbadchars` (Impact: 471.8)
  * `commit` (Impact: 289.5)
  * `_getbyspec` (Impact: 41.2)
  * `status` (Impact: 22.0)
  * `__str__` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 238`, `args: 98`, `func_start: 96`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 254`, `dead_code: 12`, `fragile_debt: 12`, `orphaned_logic: 4`
* *Architecture:* `io: 20`, `api: 72`, `import: 6`
* *Defense:* `safety: 48`, `doc: 108`, `test: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` calendar, sys, py, xml.parsers.expat, subprocess, xml.dom, re, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `rpython/rlib/fastutf8/src/utf8.c` (C) | Magnitude: 236.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 116, state_mutation: 110, api: 50, pointers: 37
- `py/_code/code.py` (PYTHON) | Magnitude: 543.04 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 530, structural_boundaries: 181, branch: 132, state_mutation: 129
- `pypy/objspace/std/mapdict.py` (PYTHON) | Magnitude: 688.7 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1134, structural_boundaries: 452, encapsulation: 288, branch: 238
- `pypy/module/faulthandler/handler.py` (PYTHON) | Magnitude: 127.9 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 57, args: 29, func_start: 29
- `pypy/module/imp/importing.py` (PYTHON) | Magnitude: 21207.29 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 766, branch: 266, structural_boundaries: 227, safety: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pypy/module/_cppyy/src/dummy_backend.cxx` (CPP) | Magnitude: 1800.38 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_17`
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
- `pypy/interpreter/pyparser/pyparse.py` (PYTHON) | Magnitude: 113.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, branch: 44, structural_boundaries: 36, encapsulation: 19
- `pypy/module/__builtin__/app_inspect.py` (PYTHON) | Magnitude: 70.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 28, encapsulation: 27, branch: 23
- `pypy/module/faulthandler/dumper.py` (PYTHON) | Magnitude: 22.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, encapsulation: 13, branch: 6
- `rpython/jit/backend/ppc/locations.py` (PYTHON) | Magnitude: 110.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 94, args: 40, func_start: 40
- `pypy/module/cpyext/src/typeobject.c` (C) | Magnitude: 24.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 12, pointers: 11, macros: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `lib_pypy/_structseq.py` (PYTHON) | Magnitude: 103.74 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, encapsulation: 42, branch: 36, structural_boundaries: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `rpython/translator/backendopt/inline.py` (PYTHON) | Magnitude: 588.28 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 580, branch: 181, structural_boundaries: 136, state_mutation: 73
- `pypy/tool/pydis.py` (PYTHON) | Magnitude: 170.14 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 143, state_mutation: 49, branch: 42, structural_boundaries: 35
- `rpython/memory/gctransform/shadowcolor.py` (PYTHON) | Magnitude: 604.72 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 551, branch: 232, structural_boundaries: 121, state_mutation: 107
- `lib_pypy/pyrepl/unix_eventqueue.py` (PYTHON) | Magnitude: 77.86 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 42, structural_boundaries: 18, branch: 11
- `rpython/translator/backendopt/constfold.py` (PYTHON) | Magnitude: 323.36 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
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
- `lib_pypy/pyrepl/console.py` (PYTHON) | Magnitude: 66.52 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 33, api: 32, doc: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `rpython/memory/gc/minimark.py` (PYTHON) | Magnitude: 1126.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1131, state_mutation: 306, branch: 230, structural_boundaries: 197
- `rpython/tool/gcanalyze.py` (PYTHON) | Magnitude: 36.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, branch: 17, io: 12, state_mutation: 12
- `rpython/tool/runsubprocess.py` (PYTHON) | Magnitude: 43.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, branch: 27, structural_boundaries: 21, encapsulation: 19
- `lib_pypy/cffi/_pycparser/_build_tables.py` (PYTHON) | Magnitude: 15.3 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, import: 7, indent_spaces: 3, io: 2
- `rpython/rtyper/extfunc.py` (PYTHON) | Magnitude: 97.66 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
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
- `rpython/rlib/rvmprof/src/shared/vmprof_getpc.h` (C) | Magnitude: 4.82 | Delta: **0.239 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 14, import: 7, ownership: 6, pointers: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pypy/objspace/std/mapdict.py` -> Churn: **100.0%** | Cog Load: 36.4498% | Debt: 99.9531%
- `rpython/translator/c/src/thread.h` -> Churn: **76.8%** | Cog Load: 54.612% | Debt: 0.0%
- `rpython/rtyper/lltypesystem/ll2ctypes.py` -> Churn: **60.86%** | Cog Load: 53.1204% | Debt: 76.2081%
- `rpython/translator/c/src/signals.c` -> Churn: **60.86%** | Cog Load: 77.3529% | Debt: 98.9915%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib_pypy/cffi/_pycparser/ply/yacc.py` -> **Charalampos Stratakis** (100.0% isolated ownership) | Magnitude: 2475.7
- `rpython/jit/metainterp/pyjitpl.py` -> **CF Bolz-Tereick** (100.0% isolated ownership) | Magnitude: 2291.04
- `rpython/jit/codewriter/jtransform.py` -> **CF Bolz-Tereick** (100.0% isolated ownership) | Magnitude: 1276.4
- `lib_pypy/cffi/_pycparser/c_parser.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 1089.7
- `rpython/rtyper/lltypesystem/ll2ctypes.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 1082.4

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

- `pypy/interpreter/error.py` -> **Severity: 3040.026** (Blast Radius: 38.535 * Doc Risk: 78.89%)
- `pypy/module/micronumpy/types.py` -> **Severity: 2195.812** (Blast Radius: 22.135 * Doc Risk: 99.2009%)
- `pypy/interpreter/baseobjspace.py` -> **Severity: 1982.865** (Blast Radius: 20.554 * Doc Risk: 96.471%)
- `pypy/module/cpyext/include/traceback.h` -> **Severity: 1269.255** (Blast Radius: 12.709 * Doc Risk: 99.8706%)
- `pypy/interpreter/mixedmodule.py` -> **Severity: 1196.914** (Blast Radius: 17.01 * Doc Risk: 70.3653%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
