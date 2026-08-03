# ARCHITECTURAL_BRIEF: cpython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/cpython` |
| **Timestamp** | `2026-08-03T20:09:55.611750+00:00` |
| **Scan Duration** | `12.89s` |
| **Git Branch** | `main` |
| **Git Commit** | `1fd66eadd258223a0e3446b5b23ff2303294112c` |
| **Git Remote** | `https://github.com/python/cpython` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1397 malicious artifacts.

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
| Total Artifacts | 5595 |
| Analyzed Artifacts (Scanned) | 1596 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3999 |
| Total LOC | 478015 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 28.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5652 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2007 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.1371 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 81 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 1034 | 409904 | 64.8% |
| PYTHON | 246 | 44313 | 15.4% |
| XML | 78 | 8 | 4.9% |
| PLAINTEXT | 53 | 0 | 3.3% |
| SHELL | 49 | 1218 | 3.1% |
| MARKDOWN | 33 | 0 | 2.1% |
| OBJECTIVE-C | 16 | 836 | 1.0% |
| BATCH | 15 | 1040 | 0.9% |
| HTML | 12 | 4374 | 0.8% |
| MAKEFILE | 9 | 3328 | 0.6% |
| YAML | 9 | 340 | 0.6% |
| JAVASCRIPT | 7 | 1366 | 0.4% |
| JSON | 7 | 282 | 0.4% |
| CPP | 7 | 2456 | 0.4% |
| M4 | 6 | 6645 | 0.4% |
| POWERSHELL | 5 | 247 | 0.3% |
| KOTLIN | 3 | 112 | 0.2% |
| CSV | 3 | 995 | 0.2% |
| CSS | 2 | 488 | 0.1% |
| ASSEMBLY | 2 | 63 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.521`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1198 | 75.1% |
| file_cluster_13 | 229 | 14.3% |
| file_cluster_16 | 19 | 1.2% |
| file_cluster_0 | 18 | 1.1% |
| file_cluster_4 | 13 | 0.8% |
| file_cluster_12 | 9 | 0.6% |
| file_cluster_17 | 4 | 0.3% |
| file_cluster_9 | 4 | 0.3% |
| file_cluster_15 | 4 | 0.3% |
| file_cluster_11 | 2 | 0.1% |
| file_cluster_7 | 1 | 0.1% |
| file_cluster_1 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 86 | 5.4% |
| Static: Minified & Vendor Opaque Mass | 8 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3999*

**Composition by Extension & Reason:**
- `.py`: 2021x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2475 LOC)
- `.rst`: 394x Excluded (Unsupported Extension: '.rst'), 393x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dectest`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 117x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 72547 LOC exceeds safe regex boundaries), 1x Excluded (Embedded Hex Payload: 14899 hex tokens in 7516 LOC)
- `.toml`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.toml), 5x Excluded (Unsupported Extension: '.toml')
- `.h`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 113 LOC), 1x Excluded (Machine-Generated Source Code Signature: 949 LOC)
- `.xml`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Monolithic Amalgamation: 30918 LOC exceeds safe regex boundaries)
- `.vcxproj`: 55x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.vcxproj)
- `.png`: 54x Excluded (Explicitly Denied Extension: '.png')
- `.filters`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.wxs`: 44x Unsupported Format (.wxs)
- `.yml`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wixproj`: 30x Unsupported Format (.wixproj)
- `.json`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2435 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 37.8 | 26.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 27.7 | 16.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 25.3 | 2.3 | 80.0 |
| API Exposure | 0.0 | 18.8 | 7.7 | 9.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 53.9 | 80.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 70.0 | 1.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.8 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 69.9 | 99.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 51.9 | 96.7 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 1.6 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Modules/clinic/posixmodule.c.h` (Hits: 108)
- `Modules/_interpchannelsmodule.c` (Hits: 100)
- `Objects/mimalloc/stats.c` (Hits: 64)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Python.h** (`Include/Python.h`) — 312 inbound connections
2. **pycore_modsupport.h** (`Include/internal/pycore_modsupport.h`) — 176 inbound connections
3. **pycore_runtime.h** (`Include/internal/pycore_runtime.h`) — 146 inbound connections
4. **pycore_gc.h** (`Include/internal/pycore_gc.h`) — 112 inbound connections
5. **sys.c** (`Modules/_testlimitedcapi/sys.c`) — 97 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Python.h** (`Include/Python.h`) — 94 outbound dependencies
2. **pylifecycle.c** (`Python/pylifecycle.c`) — 51 outbound dependencies
3. **ceval.h** (`Python/ceval.h`) — 47 outbound dependencies
4. **unicodeobject.c** (`Objects/unicodeobject.c`) — 41 outbound dependencies
5. **_testinternalcapi.c** (`Modules/_testinternalcapi.c`) — 37 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sd2b` (@ `Python/dtoa.c`) -> Impact: **5744.8** | LOC: 1170
- `_PyUnicode_CheckConsistency` (@ `Objects/unicodeobject.c`) -> Impact: **5452.9** | LOC: 1539
  * *Intent:* */
- `refchain_init` (@ `Objects/object.c`) -> Impact: **4337.6** | LOC: 1912
- `_ssl__SSLSocket_context_set_impl` (@ `Modules/_ssl.c`) -> Impact: **4173.2** | LOC: 1893
- `set_inheritable` (@ `Python/fileutils.c`) -> Impact: **4127.4** | LOC: 1156
- `merge_hi` (@ `Objects/listobject.c`) -> Impact: **3286.5** | LOC: 1471
- `PyFrame_GetLineNumber` (@ `Objects/frameobject.c`) -> Impact: **2897.0** | LOC: 1199
- `PyMemoTable_Copy` (@ `Modules/_pickle.c`) -> Impact: **2763.9** | LOC: 1930
- `_PyErr_SetObject` (@ `Python/errors.c`) -> Impact: **2721.9** | LOC: 1574
- `multibytecodec_encode` (@ `Modules/cjkcodecs/multibytecodec.c`) -> Impact: **2653.6** | LOC: 1423

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `gradle_task` (@ `Android/android.py`) -> **O(2^N) [Recursive]**
- `test_format` (@ `Modules/_decimal/tests/deccheck.py`) -> **O(2^N) [Recursive]**
- `function_as_string` (@ `Modules/_decimal/tests/deccheck.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # ====================================================================== # ====================================================================== clas...
- `visit` (@ `Parser/asdl.py`) -> **O(2^N) [Recursive]**
- `package_version` (@ `Platforms/Apple/__main__.py`) -> **O(2^N) [Recursive]**
- `_dump_unresolved` (@ `Tools/c-analyzer/c_analyzer/analyze.py`) -> **O(2^N) [Recursive]**
- `iter_files` (@ `Tools/c-analyzer/c_common/fsutil.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `Tools/c-analyzer/c_parser/info.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `Tools/c-analyzer/c_parser/info.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `Tools/c-analyzer/c_parser/info.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `update` (@ `Modules/_hacl/Hacl_Hash_MD5.c`) -> DB Complexity: **652**
  * *Intent:* * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL T...
- `_channelitem_clear_interpreter` (@ `Modules/_interpchannelsmodule.c`) -> DB Complexity: **520**
- `sd2b` (@ `Python/dtoa.c`) -> DB Complexity: **432**
- `array_del_slice` (@ `Modules/arraymodule.c`) -> DB Complexity: **399**
- `PyMemoTable_Copy` (@ `Modules/_pickle.c`) -> DB Complexity: **392**
- `long_true_divide` (@ `Objects/longobject.c`) -> DB Complexity: **363**
- `_highlightSyntax` (@ `Doc/_static/profiling-sampling-visualization.js`) -> DB Complexity: **353**
- `_PyJit_FinalizeTracing` (@ `Python/optimizer.c`) -> DB Complexity: **339**
- `insertdict` (@ `Objects/dictobject.c`) -> DB Complexity: **322**
- `element_gc_clear` (@ `Modules/_elementtree.c`) -> DB Complexity: **318**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Modules` | 111 | 111073.12 | 59.05% | 39.76% |
| `Python` | 108 | 109971.38 | 62.9% | 38.65% |
| `Objects` | 51 | 81799.54 | 66.34% | 33.04% |
| `Modules/clinic` | 79 | 74742.04 | 68.91% | 0.78% |
| `Modules/_hacl` | 30 | 23544.6 | 34.1% | 10.68% |
| `PC` | 27 | 10254.44 | 35.61% | 26.96% |
| `Modules/expat` | 23 | 10222.04 | 30.87% | 12.99% |
| `Objects/clinic` | 25 | 9953.78 | 62.0% | 0.32% |
| `Modules/_testcapi` | 42 | 9325.5 | 47.14% | 25.56% |
| `Modules/_decimal/libmpdec` | 35 | 9134.08 | 40.96% | 28.71% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Mac/BuildScript/resources/update_shell_profile.command` -> **100.0%** Exposure
- `Mac/BuildScript/scripts/postflight.documentation` -> **100.0%** Exposure
- `Mac/BuildScript/scripts/postflight.patch-profile` -> **100.0%** Exposure
- `Misc/python-config.sh.in` -> **100.0%** Exposure
- `Platforms/Apple/iOS/Resources/bin/arm64-apple-ios-ar` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Android/android-env.sh` -> **100.0%** Exposure
- `Mac/BuildScript/resources/update_shell_profile.command` -> **100.0%** Exposure
- `Mac/BuildScript/scripts/postflight.documentation` -> **100.0%** Exposure
- `Mac/BuildScript/scripts/postflight.patch-profile` -> **100.0%** Exposure
- `Misc/python-config.sh.in` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Modules/_decimal/libmpdec/mpsignal.c` -> **105** Orphaned Functions | **0** Duplicates
- `Modules/_testclinic.c` -> **97** Orphaned Functions | **6** Duplicates
- `Modules/_cursesmodule.c` -> **86** Orphaned Functions | **0** Duplicates
- `Tools/c-analyzer/c_parser/info.py` -> **0** Orphaned Functions | **84** Duplicates
- `Python/sysmodule.c` -> **65** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Android/testbed/app/src/main/java/org/python/testbed/MainActivity.kt`** -> AI Confidence: **99.48%**
2. **`Modules/_decimal/libmpdec/io.c`** -> AI Confidence: **99.48%**
3. **`Modules/_decimal/libmpdec/transpose.c`** -> AI Confidence: **99.48%**
4. **`Modules/_hacl/Hacl_HMAC.c`** -> AI Confidence: **99.48%**
5. **`Modules/_hacl/Lib_Memzero0.c`** -> AI Confidence: **99.48%**
6. **`Modules/_hacl/include/krml/internal/target.h`** -> AI Confidence: **99.48%**
7. **`Modules/_io/_iomodule.c`** -> AI Confidence: **99.48%**
8. **`Modules/_posixsubprocess.c`** -> AI Confidence: **99.48%**
9. **`Modules/_testinternalcapi/testbytecodes.c`** -> AI Confidence: **99.48%**
10. **`Objects/floatobject.c`** -> AI Confidence: **99.48%**
11. **`Objects/mimalloc/static.c`** -> AI Confidence: **99.48%**
12. **`Parser/pegen_errors.c`** -> AI Confidence: **99.48%**
13. **`Python/bytecodes.c`** -> AI Confidence: **99.48%**
14. **`Tools/jit/template.c`** -> AI Confidence: **99.48%**
15. **`Modules/_hacl/libintvector.h`** -> AI Confidence: **99.44%**
16. **`Modules/_multiprocessing/multiprocessing.h`** -> AI Confidence: **99.44%**
17. **`Python/marshal.c`** -> AI Confidence: **99.44%**
18. **`Include/Python.h`** -> AI Confidence: **99.42%**
19. **`Platforms/Apple/testbed/__main__.py`** -> AI Confidence: **99.39%**
20. **`Tools/clinic/libclinic/parse_args.py`** -> AI Confidence: **99.39%**
21. **`Tools/freeze/freeze.py`** -> AI Confidence: **99.39%**
22. **`Tools/unicode/makeunicodedata.py`** -> AI Confidence: **99.39%**
23. **`Mac/Tools/pythonw.c`** -> AI Confidence: **99.39%**
24. **`Modules/_decimal/libmpdec/convolute.c`** -> AI Confidence: **99.39%**
25. **`Modules/_decimal/libmpdec/difradix2.c`** -> AI Confidence: **99.39%**
26. **`Modules/_decimal/libmpdec/mpdecimal.c`** -> AI Confidence: **99.39%**
27. **`Modules/_json.c`** -> AI Confidence: **99.39%**
28. **`Modules/_sqlite/cursor.c`** -> AI Confidence: **99.39%**
29. **`Modules/_sqlite/module.c`** -> AI Confidence: **99.39%**
30. **`Modules/_sre/sre.c`** -> AI Confidence: **99.39%**
31. **`Modules/_ssl.c`** -> AI Confidence: **99.39%**
32. **`Modules/getaddrinfo.c`** -> AI Confidence: **99.39%**
33. **`Modules/getpath.c`** -> AI Confidence: **99.39%**
34. **`Modules/mathmodule.c`** -> AI Confidence: **99.39%**
35. **`Objects/bytes_methods.c`** -> AI Confidence: **99.39%**
36. **`Objects/longobject.c`** -> AI Confidence: **99.39%**
37. **`Objects/sliceobject.c`** -> AI Confidence: **99.39%**
38. **`Objects/unicodeobject.c`** -> AI Confidence: **99.39%**
39. **`Parser/myreadline.c`** -> AI Confidence: **99.39%**
40. **`Parser/string_parser.c`** -> AI Confidence: **99.39%**
41. **`Python/Python-tokenize.c`** -> AI Confidence: **99.39%**
42. **`Python/dynload_win.c`** -> AI Confidence: **99.39%**
43. **`Python/flowgraph.c`** -> AI Confidence: **99.39%**
44. **`Python/getargs.c`** -> AI Confidence: **99.39%**
45. **`Python/pathconfig.c`** -> AI Confidence: **99.39%**
46. **`Modules/_io/winconsoleio.c`** -> AI Confidence: **99.35%**
47. **`Android/testbed/app/src/androidTest/java/org/python/testbed/PythonSuite.kt`** -> AI Confidence: **99.34%**
48. **`Include/internal/mimalloc/mimalloc/track.h`** -> AI Confidence: **99.34%**
49. **`Modules/_decimal/libmpdec/basearith.c`** -> AI Confidence: **99.34%**
50. **`Modules/_decimal/libmpdec/crt.c`** -> AI Confidence: **99.34%**
51. **`Modules/_remote_debugging/clinic/module.c.h`** -> AI Confidence: **99.34%**
52. **`Modules/binascii.c`** -> AI Confidence: **99.34%**
53. **`Modules/cjkcodecs/_codecs_jp.c`** -> AI Confidence: **99.34%**
54. **`Modules/clinic/_hashopenssl.c.h`** -> AI Confidence: **99.34%**
55. **`Modules/clinic/_testclinic.c.h`** -> AI Confidence: **99.34%**
56. **`Modules/clinic/_testclinic_depr.c.h`** -> AI Confidence: **99.34%**
57. **`Modules/clinic/_testclinic_kwds.c.h`** -> AI Confidence: **99.34%**
58. **`Modules/clinic/mmapmodule.c.h`** -> AI Confidence: **99.34%**
59. **`Modules/clinic/posixmodule.c.h`** -> AI Confidence: **99.34%**
60. **`Modules/clinic/selectmodule.c.h`** -> AI Confidence: **99.34%**
61. **`Objects/clinic/bytearrayobject.c.h`** -> AI Confidence: **99.34%**
62. **`Objects/complexobject.c`** -> AI Confidence: **99.34%**
63. **`Objects/unicode_format.c`** -> AI Confidence: **99.34%**
64. **`Objects/unicode_formatter.c`** -> AI Confidence: **99.34%**
65. **`Python/dtoa.c`** -> AI Confidence: **99.34%**
66. **`Python/structmember.c`** -> AI Confidence: **99.34%**
67. **`Python/traceback.c`** -> AI Confidence: **99.34%**
68. **`PC/_wmimodule.cpp`** -> AI Confidence: **99.34%**
69. **`Include/cpython/pyatomic.h`** -> AI Confidence: **99.32%**
70. **`Misc/platform_triplet.c`** -> AI Confidence: **99.32%**
71. **`Modules/_ctypes/clinic/callproc.c.h`** -> AI Confidence: **99.32%**
72. **`Modules/_decimal/libmpdec/constants.c`** -> AI Confidence: **99.32%**
73. **`Modules/_io/clinic/_iomodule.c.h`** -> AI Confidence: **99.32%**
74. **`Modules/_io/clinic/iobase.c.h`** -> AI Confidence: **99.32%**
75. **`Modules/_sqlite/clinic/_sqlite3.connect.c.h`** -> AI Confidence: **99.32%**
76. **`Modules/_sqlite/clinic/connection.c.h`** -> AI Confidence: **99.32%**
77. **`Modules/_sqlite/clinic/module.c.h`** -> AI Confidence: **99.32%**
78. **`Modules/_ssl/clinic/cert.c.h`** -> AI Confidence: **99.32%**
79. **`Modules/_testcapi/clinic/exceptions.c.h`** -> AI Confidence: **99.32%**
80. **`Modules/_zstd/clinic/compressor.c.h`** -> AI Confidence: **99.32%**
81. **`Modules/cjkcodecs/clinic/multibytecodec.c.h`** -> AI Confidence: **99.32%**
82. **`Modules/clinic/_codecsmodule.c.h`** -> AI Confidence: **99.32%**
83. **`Modules/clinic/_cursesmodule.c.h`** -> AI Confidence: **99.32%**
84. **`Modules/clinic/_datetimemodule.c.h`** -> AI Confidence: **99.32%**
85. **`Modules/clinic/_dbmmodule.c.h`** -> AI Confidence: **99.32%**
86. **`Modules/clinic/_gdbmmodule.c.h`** -> AI Confidence: **99.32%**
87. **`Modules/clinic/_opcode.c.h`** -> AI Confidence: **99.32%**
88. **`Modules/clinic/_pickle.c.h`** -> AI Confidence: **99.32%**
89. **`Modules/clinic/_testmultiphase.c.h`** -> AI Confidence: **99.32%**
90. **`Modules/clinic/cmathmodule.c.h`** -> AI Confidence: **99.32%**
91. **`Modules/clinic/mathmodule.c.h`** -> AI Confidence: **99.32%**
92. **`Modules/clinic/sha2module.c.h`** -> AI Confidence: **99.32%**
93. **`Modules/clinic/signalmodule.c.h`** -> AI Confidence: **99.32%**
94. **`Modules/clinic/symtablemodule.c.h`** -> AI Confidence: **99.32%**
95. **`Objects/clinic/codeobject.c.h`** -> AI Confidence: **99.32%**
96. **`Objects/clinic/descrobject.c.h`** -> AI Confidence: **99.32%**
97. **`Objects/clinic/enumobject.c.h`** -> AI Confidence: **99.32%**
98. **`Objects/clinic/interpolationobject.c.h`** -> AI Confidence: **99.32%**
99. **`Objects/clinic/memoryobject.c.h`** -> AI Confidence: **99.32%**
100. **`Objects/clinic/moduleobject.c.h`** -> AI Confidence: **99.32%**
101. **`Objects/clinic/structseq.c.h`** -> AI Confidence: **99.32%**
102. **`Objects/clinic/typevarobject.c.h`** -> AI Confidence: **99.32%**
103. **`PC/clinic/_wmimodule.cpp.h`** -> AI Confidence: **99.32%**
104. **`Python/ceval.h`** -> AI Confidence: **99.32%**
105. **`Python/clinic/Python-tokenize.c.h`** -> AI Confidence: **99.32%**
106. **`Python/clinic/bltinmodule.c.h`** -> AI Confidence: **99.32%**
107. **`Python/clinic/instruction_sequence.c.h`** -> AI Confidence: **99.32%**
108. **`Python/clinic/marshal.c.h`** -> AI Confidence: **99.32%**
109. **`Python/mystrtoul.c`** -> AI Confidence: **99.32%**
110. **`Mac/PythonLauncher/MyDocument.m`** -> AI Confidence: **99.32%**
111. **`Mac/PythonLauncher/doscript.m`** -> AI Confidence: **99.32%**
112. **`Android/android.py`** -> AI Confidence: **99.31%**
113. **`Doc/tools/check-html-ids.py`** -> AI Confidence: **99.31%**
114. **`Doc/tools/check-warnings.py`** -> AI Confidence: **99.31%**
115. **`Modules/_decimal/tests/deccheck.py`** -> AI Confidence: **99.31%**
116. **`Modules/_decimal/tests/formathelper.py`** -> AI Confidence: **99.31%**
117. **`Platforms/Apple/__main__.py`** -> AI Confidence: **99.31%**
118. **`Tools/c-analyzer/c_analyzer/__main__.py`** -> AI Confidence: **99.31%**
119. **`Tools/c-analyzer/c_common/fsutil.py`** -> AI Confidence: **99.31%**
120. **`Tools/c-analyzer/c_common/scriptutil.py`** -> AI Confidence: **99.31%**
121. **`Tools/c-analyzer/c_parser/__main__.py`** -> AI Confidence: **99.31%**
122. **`Tools/c-analyzer/c_parser/info.py`** -> AI Confidence: **99.31%**
123. **`Tools/c-analyzer/c_parser/preprocessor/common.py`** -> AI Confidence: **99.31%**
124. **`Tools/c-analyzer/cpython/__main__.py`** -> AI Confidence: **99.31%**
125. **`Tools/c-analyzer/cpython/_analyzer.py`** -> AI Confidence: **99.31%**
126. **`Tools/c-analyzer/cpython/_builtin_types.py`** -> AI Confidence: **99.31%**
127. **`Tools/c-analyzer/cpython/_capi.py`** -> AI Confidence: **99.31%**
128. **`Tools/c-analyzer/distutils/msvc9compiler.py`** -> AI Confidence: **99.31%**
129. **`Tools/c-analyzer/distutils/util.py`** -> AI Confidence: **99.31%**
130. **`Tools/cases_generator/opcode_metadata_generator.py`** -> AI Confidence: **99.31%**
131. **`Tools/cases_generator/optimizer_generator.py`** -> AI Confidence: **99.31%**
132. **`Tools/cases_generator/parsing.py`** -> AI Confidence: **99.31%**
133. **`Tools/clinic/libclinic/block_parser.py`** -> AI Confidence: **99.31%**
134. **`Tools/clinic/libclinic/clanguage.py`** -> AI Confidence: **99.31%**
135. **`Tools/clinic/libclinic/cli.py`** -> AI Confidence: **99.31%**
136. **`Tools/clinic/libclinic/converter.py`** -> AI Confidence: **99.31%**
137. **`Tools/clinic/libclinic/dsl_parser.py`** -> AI Confidence: **99.31%**
138. **`Tools/freeze/test/freeze.py`** -> AI Confidence: **99.31%**
139. **`Tools/i18n/msgfmt.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `Parser/tokenizer/helpers.c` -> **1.555%** Exposure
- `Objects/bytearrayobject.c` -> **0.0005%** Exposure
- `Python/ceval.c` -> **0.0002%** Exposure
### Exploit Generation Surface
- `Android/android.py` -> **100.0%** Exposure
- `Doc/includes/diff.py` -> **100.0%** Exposure
- `Doc/includes/minidom-example.py` -> **100.0%** Exposure
- `Doc/includes/mp_pool.py` -> **100.0%** Exposure
- `Doc/includes/tzinfo_examples.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Doc/includes/dbpickle.py` -> **100.0%** Exposure
- `Doc/tools/extensions/profiling_trace.py` -> **100.0%** Exposure
- `Modules/_decimal/tests/formathelper.py` -> **100.0%** Exposure
- `Platforms/Apple/testbed/__main__.py` -> **100.0%** Exposure
- `Tools/c-analyzer/c_parser/preprocessor/common.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `Include/internal/pycore_dict.h` -> **10.0%** Exposure
- `Include/internal/pycore_interpframe.h` -> **10.0%** Exposure
- `Include/internal/pycore_optimizer.h` -> **10.0%** Exposure
- `Modules/_bz2module.c` -> **10.0%** Exposure
- `Modules/_codecsmodule.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `Android/android-env.sh` -> **100.0%** Exposure
- `Misc/python-config.sh.in` -> **100.0%** Exposure
- `Modules/_decimal/tests/runall-memorydebugger.sh` -> **100.0%** Exposure
- `Android/android.py` -> **100.0%** Exposure
- `Doc/includes/diff.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `88` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6126` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Parser/action_helpers.c` (C) -> Cumulative Risk: **844.7**
- **Archetype:** `file_cluster_8` (Distance: 13.947 IQR)
- **Magnitude:** 2079.38 | **LOC:** 2014 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_build_concatenated_str` (Impact: 168.3), `_get_resized_exprs` (Impact: 77.7), `_PyPegen_concatenate_strings` (Impact: 76.5)

### 2. `Objects/picklebufobject.c` (C) -> Cumulative Risk: **834.86**
- **Archetype:** `file_cluster_8` (Distance: 11.729 IQR)
- **Magnitude:** 181.28 | **LOC:** 225 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `picklebuf_new` (Impact: 15.2), `PyPickleBuffer_GetBuffer` (Impact: 11.4), `picklebuf_getbuf` (Impact: 7.5)

### 3. `Python/pylifecycle.c` (C) -> Cumulative Risk: **810.0**
- **Archetype:** `file_cluster_13` (Distance: 13.725 IQR)
- **Magnitude:** 3319.14 | **LOC:** 3896 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 16.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `_Py_LegacyLocaleDetected` (Impact: 1115.2), `resolve_final_tstate` (Impact: 1010.7), `finalize_remove_modules` (Impact: 84.5)

### 4. `Python/pystate.c` (C) -> Cumulative Risk: **802.65**
- **Archetype:** `file_cluster_13` (Distance: 14.02 IQR)
- **Magnitude:** 1417.5 | **LOC:** 3289 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 12.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%), Tech Debt (97.8372%)
- **Heaviest Functions:** `stop_the_world` (Impact: 503.2), `_PyInterpreterState_DeleteExceptMain` (Impact: 117.2), `park_detached_threads` (Impact: 50.1)

### 5. `Modules/socketmodule.c` (C) -> Cumulative Risk: **801.07**
- **Archetype:** `file_cluster_8` (Distance: 14.131 IQR)
- **Magnitude:** 3408.78 | **LOC:** 9359 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 26.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.2598%)
- **Heaviest Functions:** `_socket_socket_sendmsg_impl` (Impact: 906.2), `makesockaddr` (Impact: 417.4), `setipaddr` (Impact: 97.3)

### 6. `Tools/ftscalingbench/ftscalingbench.py` (PYTHON) -> Cumulative Risk: **797.15**
- **Archetype:** `file_cluster_0` (Distance: 10.606 IQR)
- **Magnitude:** 0.75 | **LOC:** 452 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `determine_num_threads_and_affinity` (Impact: 417.9), `benchmark` (Impact: 25.3), `load_string_const` (Impact: 14.3)

### 7. `Python/optimizer.c` (C) -> Cumulative Risk: **793.63**
- **Archetype:** `file_cluster_13` (Distance: 15.267 IQR)
- **Magnitude:** 1975.66 | **LOC:** 2127 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 28.6%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_PyJit_FinalizeTracing` (Impact: 803.6), `get_index_for_executor` (Impact: 13.6), `_PyOptimizer_Optimize` (Impact: 11.6)

### 8. `Python/sysmodule.c` (C) -> Cumulative Risk: **791.61**
- **Archetype:** `file_cluster_8` (Distance: 13.561 IQR)
- **Magnitude:** 2238.08 | **LOC:** 4722 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 11.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `sys_set_asyncgen_hooks` (Impact: 79.8), `sys_displayhook_unencodable` (Impact: 65.8), `sys_displayhook` (Impact: 48.5)

### 9. `Modules/_collectionsmodule.c` (C) -> Cumulative Risk: **789.33**
- **Archetype:** `file_cluster_8` (Distance: 13.796 IQR)
- **Magnitude:** 1565.12 | **LOC:** 2900 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 16.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_collections__count_elements_impl` (Impact: 134.6), `deque_index_impl` (Impact: 62.6), `deque_inplace_repeat_lock_held` (Impact: 57.8)

### 10. `Modules/gcmodule.c` (C) -> Cumulative Risk: **783.48**
- **Archetype:** `file_cluster_8` (Distance: 12.108 IQR)
- **Magnitude:** 311.7 | **LOC:** 562 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 28.6%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `gc_get_stats_impl` (Impact: 26.6), `gc_get_objects_impl` (Impact: 15.2), `append_referrents` (Impact: 14.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Modules/clinic/posixmodule.c.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.656 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.051 IQR)
- **Top Global Matches:** file_cluster_8: 14.656, file_cluster_12: 14.886, file_cluster_7: 14.974
- **Magnitude:** 12538.16 | **LOC:** 13615 | **CtrlFlow:** 86.3% | **Authorship Centralization:** 18.2%
- **Algorithmic:** O(N^6) | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (75.3202%), Tech Debt (10.3784%)
**Top Internal Functions/Classes:**
  * `os_statx` (Impact: 130.4 | O(N^4) | DB: 22)
  * `os_sendfile` (Impact: 117.0 | O(N^6) | DB: 27)
  * `os_splice` (Impact: 106.2 | O(N^6) | DB: 26)
  * `os_chflags` (Impact: 90.7 | O(N^4) | DB: 17)
  * `os_copy_file_range` (Impact: 88.2 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2266`, `structural_boundaries: 359`, `args: 8`, `func_start: 189`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 50`, `state_mutation: 5587`, `duplicate_logic: 15`, `orphaned_logic: 1`
* *Architecture:* `io: 108`, `api: 2027`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 358`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pycore_modsupport.h, pycore_long.h, pycore_gc.h, pycore_abstract.h, pycore_runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/unicodeobject.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.941 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.053 IQR)
- **Top Global Matches:** file_cluster_13: 14.941, file_cluster_8: 15.044, file_cluster_11: 15.088
- **Magnitude:** 11422.74 | **LOC:** 14992 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 51.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 283
- **Risk Profile:** Cognitive Load (95.4556%), Tech Debt (13.9724%)
**Top Internal Functions/Classes:**
  * `_PyUnicode_CheckConsistency` (Impact: 5452.9 | O(2^N) | DB: 283)
    * *Intent:* */
  * `_PyUnicode_DecodeUnicodeEscapeInternal2` (Impact: 1618.9 | O(N^6) | DB: 165)
  * `PyUnicode_DecodeUTF32Stateful` (Impact: 401.4 | O(N^6) | DB: 43)
  * `_Py_DecodeUTF8Ex` (Impact: 375.7 | O(N^6) | DB: 28)
  * `_PyUnicode_EncodeUTF32` (Impact: 126.6 | O(N^6) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 892`, `structural_boundaries: 323`, `args: 32`, `func_start: 94`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 2053`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 697`, `import: 76`
* *Defense:* `safety: 86`, `doc: 1`, `test: 71`, `immutability_locks: 146`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` ucs1lib.h, eq.h, Python.h, pycore_pystate.h, pycore_unicodeobject.h, pycore_pyhash.h, stddef.h, replace.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/marshal.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.505 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.998 IQR)
- **Top Global Matches:** file_cluster_8: 13.505, file_cluster_13: 13.671, file_cluster_11: 13.797
- **Magnitude:** 8604.78 | **LOC:** 2158 | **CtrlFlow:** 86.5% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (86.6342%), Tech Debt (10.7369%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 47`, `args: 5`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 568`, `fragile_debt: 2`
* *Architecture:* `io: 10`, `api: 163`, `import: 13`
* *Defense:* `safety: 22`, `test: 19`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` TargetConditionals.h, marshal.h, pycore_call.h, Python.h, pycore_long.h, pycore_pystate.h, pycore_code.h, pycore_setobject.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/dictobject.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.882 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.824 IQR)
- **Top Global Matches:** file_cluster_8: 14.882, file_cluster_11: 15.033, file_cluster_13: 15.037
- **Magnitude:** 8163.56 | **LOC:** 8326 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 52.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 322
- **Risk Profile:** Cognitive Load (92.9154%), Tech Debt (21.8647%)
**Top Internal Functions/Classes:**
  * `insertdict` (Impact: 2463.2 | O(2^N) | DB: 322)
  * `_Py_dict_lookup_threadsafe` (Impact: 251.9 | O(2^N) | DB: 16)
  * `dictiter_iternext_threadsafe` (Impact: 99.8 | O(N^6) | DB: 20)
  * `store_instance_attr_lock_held` (Impact: 88.8 | O(N^6) | DB: 10)
  * `dictreviter_iter_lock_held` (Impact: 81.5 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 957`, `structural_boundaries: 540`, `args: 4`, `func_start: 188`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 130`, `state_mutation: 2529`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 3`, `orphaned_logic: 35`
* *Architecture:* `io: 2`, `api: 1033`, `import: 19`
* *Defense:* `safety: 196`, `doc: 5`, `test: 198`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` eq.h, Python.h, pycore_pystate.h, pycore_unicodeobject.h, pycore_freelist.h, pycore_pyerrors.h, pycore_code.h, pycore_tuple.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/clinic/_testclinic.c.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.37 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.225 IQR)
- **Top Global Matches:** file_cluster_8: 14.37, file_cluster_12: 14.528, file_cluster_7: 14.659
- **Magnitude:** 7930.68 | **LOC:** 4604 | **CtrlFlow:** 88.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (77.3426%), Tech Debt (15.531%)
**Top Internal Functions/Classes:**
  * `char_converter` (Impact: 810.3 | O(2^N) | DB: 44)
  * `unsigned_char_converter` (Impact: 416.2 | O(2^N) | DB: 10)
  * `py_ssize_t_converter` (Impact: 306.4 | O(2^N) | DB: 25)
  * `unsigned_long_long_converter` (Impact: 202.6 | O(2^N) | DB: 6)
  * `unsigned_long_converter` (Impact: 175.8 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 830`, `structural_boundaries: 110`, `args: 10`, `func_start: 75`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 2406`, `fragile_debt: 4`, `duplicate_logic: 6`
* *Architecture:* `api: 937`, `import: 6`
* *Defense:* `safety: 9`, `immutability_locks: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` pycore_modsupport.h, pycore_long.h, pycore_gc.h, pycore_abstract.h, pycore_runtime.h, pycore_tuple.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/dtoa.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.82 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.067 IQR)
- **Top Global Matches:** file_cluster_8: 14.82, file_cluster_11: 14.921, file_cluster_13: 14.976
- **Magnitude:** 7901.16 | **LOC:** 2842 | **CtrlFlow:** 90.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 432
- **Risk Profile:** Cognitive Load (98.0151%), Tech Debt (15.0793%)
**Top Internal Functions/Classes:**
  * `sd2b` (Impact: 5744.8 | O(2^N) | DB: 432)
  * `mult` (Impact: 42.9 | O(N^4) | DB: 38)
  * `s2b` (Impact: 37.4 | O(N^3) | DB: 16)
    * *Intent:* /* Int_max = floor(P*log(FLT_RADIX)/log(10) - 1) */ #define Exp_shift 20 #define Exp_shift1 20 #defi...
  * `Balloc` (Impact: 36.2 | O(N^4) | DB: 12)
    * *Intent:* * * Modifications: * * 1. We only require IEEE, IBM, or VAX double-precision * arithmetic (not IEEE ...
  * `pow5mult` (Impact: 29.7 | O(N^4) | DB: 8)
    * *Intent:* #endif /* !defined(Py_GIL_DISABLED) && !defined(Py_USING_MEMORY_DEBUGGER) */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 547`, `structural_boundaries: 59`, `args: 12`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1695`, `dead_code: 4`, `fragile_debt: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 187`, `import: 5`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` stdlib.h, Python.h, pycore_pystate.h, float.h, pycore_dtoa.h, pycore_interp_structs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/longobject.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.119 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.412 IQR)
- **Top Global Matches:** file_cluster_8: 15.119, file_cluster_11: 15.156, file_cluster_0: 15.188
- **Magnitude:** 7549.78 | **LOC:** 6969 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 21.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 363
- **Risk Profile:** Cognitive Load (95.1135%), Tech Debt (21.381%)
**Top Internal Functions/Classes:**
  * `long_true_divide` (Impact: 2417.1 | O(2^N) | DB: 363)
  * `_PyLong_FromLarge` (Impact: 614.5 | O(N^6) | DB: 144)
  * `long_from_string_base` (Impact: 143.7 | O(N^6) | DB: 20)
  * `long_to_decimal_string_internal` (Impact: 134.3 | O(N^6) | DB: 54)
  * `long_from_binary_base` (Impact: 114.6 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 817`, `structural_boundaries: 324`, `args: 17`, `func_start: 108`
* *Risk/State:* `safety_bypasses: 171`, `high_risk_execution: 2`, `state_mutation: 2725`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 27`
* *Architecture:* `io: 1`, `api: 705`, `import: 15`
* *Defense:* `safety: 151`, `doc: 2`, `test: 116`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` pycore_initconfig.h, pycore_call.h, Python.h, pycore_long.h, pycore_unicodeobject.h, float.h, pycore_structseq.h, stddef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_ssl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.047 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.739 IQR)
- **Top Global Matches:** file_cluster_8: 14.047, file_cluster_7: 14.348, file_cluster_13: 14.366
- **Magnitude:** 7069.98 | **LOC:** 7422 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 17.4%
- **Algorithmic:** O(N^6) | **DB Complexity:** 268
- **Risk Profile:** Cognitive Load (96.3336%), Tech Debt (9.3831%)
**Top Internal Functions/Classes:**
  * `_ssl__SSLSocket_context_set_impl` (Impact: 4173.2 | O(N^6) | DB: 268)
  * `sslmodule_init_constants` (Impact: 114.7 | O(N^6) | DB: 1)
  * `newPySSLSocket` (Impact: 111.8 | O(N^6) | DB: 22)
    * *Intent:* /* Default cipher suites */ #ifndef PY_SSL_DEFAULT_CIPHERS #define PY_SSL_DEFAULT_CIPHERS 1 #endif #...
  * `_ssl_enum_crls_impl` (Impact: 59.5 | O(N^6) | DB: 15)
  * `_ssl__SSLSocket_do_handshake_impl` (Impact: 47.8 | O(N^5) | DB: 14)
    * *Intent:* #ifndef OPENSSL_NO_PSK
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 734`, `structural_boundaries: 291`, `args: 13`, `func_start: 98`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 1346`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 20`, `api: 624`, `import: 4`
* *Defense:* `safety: 16`, `test: 9`, `immutability_locks: 44`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` _ssl.c.h, poll.h, err.h, pem.h, Python.h, rand.h, rsa.h, dh.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/initconfig.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.602 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.261 IQR)
- **Top Global Matches:** file_cluster_8: 14.602, file_cluster_13: 14.757, file_cluster_11: 14.767
- **Magnitude:** 6867.36 | **LOC:** 4859 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 18.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (77.5942%), Tech Debt (21.7418%)
**Top Internal Functions/Classes:**
  * `PyConfig_Set` (Impact: 540.1 | O(2^N) | DB: 16)
  * `config_parse_cmdline` (Impact: 300.6 | O(N^6) | DB: 33)
    * *Intent:* /* Parse the command line arguments */
  * `config_read` (Impact: 121.3 | O(N^6) | DB: 25)
  * `_PyConfig_FromDict` (Impact: 120.2 | O(N^6) | DB: 7)
  * `config_read_env_vars` (Impact: 82.1 | O(N^6) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 937`, `structural_boundaries: 463`, `args: 26`, `func_start: 141`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 2519`, `dead_code: 5`, `fragile_debt: 1`, `orphaned_logic: 32`
* *Architecture:* `io: 8`, `api: 800`, `import: 20`
* *Defense:* `safety: 96`, `test: 75`, `immutability_locks: 197`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Python.h, pycore_pystate.h, pycore_pyhash.h, pycore_sysmodule.h, pycore_pystats.h, stdlib.h, pycore_pyerrors.h, pycore_initconfig.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_decimal/clinic/_decimal.c.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.361 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.268 IQR)
- **Top Global Matches:** file_cluster_8: 14.361, file_cluster_7: 14.683, file_cluster_12: 14.781
- **Magnitude:** 6690.3 | **LOC:** 6984 | **CtrlFlow:** 80.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (64.5928%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_decimal_localcontext` (Impact: 75.5 | O(N^3) | DB: 39)
  * `context_init` (Impact: 65.0 | O(N^3) | DB: 37)
  * `dec_new` (Impact: 26.9 | O(N^3) | DB: 19)
  * `_decimal_Decimal_to_integral_value` (Impact: 26.9 | O(N^3) | DB: 18)
  * `_decimal_Decimal_to_integral` (Impact: 26.9 | O(N^3) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 842`, `structural_boundaries: 202`, `args: 3`, `func_start: 123`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3571`
* *Architecture:* `api: 1010`, `import: 4`
* *Defense:* `immutability_locks: 329`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pycore_abstract.h, pycore_runtime.h, pycore_gc.h, pycore_modsupport.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/expat/xmlparse.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.446 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.53 IQR)
- **Top Global Matches:** file_cluster_8: 14.446, file_cluster_0: 14.605, file_cluster_11: 14.624
- **Magnitude:** 6458.16 | **LOC:** 9225 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 202
- **Risk Profile:** Cognitive Load (95.7501%), Tech Debt (10.3505%)
**Top Internal Functions/Classes:**
  * `getContext` (Impact: 2376.0 | O(N^6) | DB: 202)
  * `XML_SetEncoding` (Impact: 528.7 | O(N^6) | DB: 120)
    * *Intent:* /* do not call if m_parentParser != NULL */
  * `storeAttributeValue` (Impact: 301.6 | O(N^6) | DB: 44)
  * `parserCreate` (Impact: 209.8 | O(N^6) | DB: 59)
    * *Intent:* # define XmlInitUnknownEncodingNS XmlInitUnknownEncoding # undef XmlGetInternalEncodingNS # define X...
  * `getAttributeId` (Impact: 97.5 | O(N^6) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 998`, `structural_boundaries: 584`, `args: 20`, `func_start: 69`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 1980`, `dead_code: 7`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 6`, `api: 561`
* *Defense:* `safety: 52`, `test: 17`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` xmlrole.h, stdio.h, assert.h, stddef.h, expat.h, math.h, errno.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/fileutils.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.089 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.199 IQR)
- **Top Global Matches:** file_cluster_8: 14.089, file_cluster_13: 14.164, file_cluster_11: 14.273
- **Magnitude:** 5964.74 | **LOC:** 3149 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 246
- **Risk Profile:** Cognitive Load (94.5818%), Tech Debt (23.4439%)
**Top Internal Functions/Classes:**
  * `set_inheritable` (Impact: 4127.4 | O(2^N) | DB: 246)
  * `_Py_stat_basic_info_to_stat` (Impact: 111.5 | O(N^6) | DB: 14)
  * `encode_current_locale` (Impact: 85.5 | O(N^5) | DB: 26)
    * *Intent:* /* Workaround FreeBSD and OpenIndiana locale encoding issue with the C locale
  * `_Py_DecodeLocaleEx` (Impact: 66.9 | O(N^6) | DB: 3)
  * `_Py_fstat_noraise` (Impact: 44.4 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 198`, `args: 27`, `func_start: 59`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 868`, `fragile_debt: 2`, `orphaned_logic: 11`
* *Architecture:* `io: 23`, `api: 362`, `import: 17`
* *Defense:* `safety: 65`, `test: 18`, `immutability_locks: 48`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` stdlib.h, pycore_fileutils_windows.h, fcntl.h, Python.h, pycore_pystate.h, pycore_fileutils.h, pycore_unicodeobject.h, ioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/listobject.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.302 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.705 IQR)
- **Top Global Matches:** file_cluster_8: 14.302, file_cluster_13: 14.407, file_cluster_0: 14.507
- **Magnitude:** 5520.28 | **LOC:** 4308 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 258
- **Risk Profile:** Cognitive Load (93.4286%), Tech Debt (16.1505%)
**Top Internal Functions/Classes:**
  * `merge_hi` (Impact: 3286.5 | O(2^N) | DB: 258)
  * `list_extend_set` (Impact: 161.7 | O(N^5) | DB: 45)
  * `count_run` (Impact: 74.4 | O(N^5) | DB: 27)
  * `ensure_shared_on_resize` (Impact: 63.6 | O(2^N) | DB: 13)
    * *Intent:* #endif
  * `list_inplace_repeat_lock_held` (Impact: 29.0 | O(N^5) | DB: 8)
    * *Intent:* /* Do it backwards, for Christian Tismer.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 455`, `structural_boundaries: 224`, `args: 8`, `func_start: 82`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 1224`, `dead_code: 1`, `orphaned_logic: 18`
* *Architecture:* `io: 1`, `api: 403`, `import: 18`
* *Defense:* `safety: 76`, `doc: 2`, `test: 50`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` pycore_ceval.h, pycore_typeobject.h, listobject.c.h, pycore_modsupport.h, Python.h, pycore_long.h, pycore_setobject.h, pycore_list.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/object.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.669 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.424 IQR)
- **Top Global Matches:** file_cluster_13: 13.669, file_cluster_8: 13.67, file_cluster_0: 13.871
- **Magnitude:** 5416.74 | **LOC:** 3503 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 23.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 207
- **Risk Profile:** Cognitive Load (88.856%), Tech Debt (18.7458%)
**Top Internal Functions/Classes:**
  * `refchain_init` (Impact: 4337.6 | O(2^N) | DB: 207)
  * `_PyObject_CheckConsistency` (Impact: 11.6 | O(N^2))
  * `Py_GetConstant` (Impact: 9.6 | O(N^2))
  * `PyRefTracer_SetTracer` (Impact: 6.8 | O(N^3) | DB: 2)
  * `has_own_refchain` (Impact: 6.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 318`, `structural_boundaries: 238`, `args: 14`, `func_start: 101`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 620`, `dead_code: 5`, `fragile_debt: 1`, `orphaned_logic: 11`
* *Architecture:* `io: 3`, `api: 345`, `import: 34`
* *Defense:* `safety: 31`, `doc: 1`, `test: 25`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` pycore_typeobject.h, pycore_context.h, Python.h, pycore_pystate.h, pycore_function.h, pycore_freelist.h, pycore_brc.h, pycore_symtable.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/codeobject.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.523 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.709 IQR)
- **Top Global Matches:** file_cluster_8: 14.523, file_cluster_13: 14.649, file_cluster_11: 14.699
- **Magnitude:** 5371.68 | **LOC:** 3670 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 15.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (75.5083%), Tech Debt (24.5548%)
**Top Internal Functions/Classes:**
  * `PyUnstable_Code_NewWithPosOnlyArgs` (Impact: 556.9 | O(N^6) | DB: 60)
  * `_PyCode_ConstantKey` (Impact: 247.7 | O(2^N) | DB: 39)
  * `intern_constants` (Impact: 222.2 | O(2^N) | DB: 19)
  * `_PyCode_Validate` (Impact: 219.7 | O(N^6) | DB: 1)
  * `code_richcompare` (Impact: 144.4 | O(N^6) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 624`, `structural_boundaries: 324`, `args: 22`, `func_start: 117`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 1816`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 26`
* *Architecture:* `io: 10`, `api: 622`, `import: 21`
* *Defense:* `safety: 84`, `doc: 8`, `test: 87`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Python.h, pycore_pystate.h, pycore_unicodeobject.h, pycore_function.h, pycore_opcode_utils.h, codeobject.c.h, pycore_uniqueid.h, pycore_code.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_pickle.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.258 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.545 IQR)
- **Top Global Matches:** file_cluster_8: 14.258, file_cluster_13: 14.407, file_cluster_11: 14.468
- **Magnitude:** 4769.86 | **LOC:** 8277 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(N^6) | **DB Complexity:** 392
- **Risk Profile:** Cognitive Load (97.027%), Tech Debt (21.8032%)
**Top Internal Functions/Classes:**
  * `PyMemoTable_Copy` (Impact: 2763.9 | O(N^6) | DB: 392)
  * `load_build` (Impact: 92.8 | O(N^6) | DB: 12)
  * `_pickle_Unpickler___init___impl` (Impact: 44.1 | O(N^6) | DB: 10)
  * `_pickle_exec` (Impact: 31.0 | O(N^3) | DB: 5)
  * `do_setitems` (Impact: 29.6 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 539`, `structural_boundaries: 279`, `args: 5`, `func_start: 71`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1280`, `fragile_debt: 3`, `orphaned_logic: 13`
* *Architecture:* `io: 14`, `api: 373`, `import: 16`
* *Defense:* `safety: 39`, `doc: 2`, `test: 18`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` pycore_ceval.h, pycore_symtable.h, stdlib.h, pycore_pyerrors.h, pycore_moduleobject.h, pycore_bytesobject.h, Python.h, pycore_long.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_ctypes/_ctypes.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.636 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.773 IQR)
- **Top Global Matches:** file_cluster_8: 13.636, file_cluster_13: 13.89, file_cluster_7: 13.923
- **Magnitude:** 4651.82 | **LOC:** 6524 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 14.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 241
- **Risk Profile:** Cognitive Load (89.1276%), Tech Debt (11.9329%)
**Top Internal Functions/Classes:**
  * `CDataType_in_dll_impl` (Impact: 1955.6 | O(N^6) | DB: 241)
    * *Intent:* [clinic start generated code]*/
  * `_ctypes_alloc_format_string_for_type` (Impact: 119.7 | O(N^2) | DB: 20)
  * `_ctypes_alloc_format_string_with_shape` (Impact: 64.5 | O(N^6) | DB: 7)
  * `StructUnionType_init` (Impact: 49.0 | O(N^6) | DB: 8)
  * `CDataType_from_buffer_impl` (Impact: 38.4 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 647`, `structural_boundaries: 519`, `args: 15`, `func_start: 119`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 99`, `state_mutation: 1456`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 7`
* *Architecture:* `io: 3`, `api: 705`, `import: 14`
* *Defense:* `safety: 58`, `doc: 16`, `test: 47`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` pycore_ceval.h, pycore_modsupport.h, _ctypes.c.h, pycore_call.h, Python.h, pycore_unicodeobject.h, ctypes.h, pycore_long.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/frameobject.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.14 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.844 IQR)
- **Top Global Matches:** file_cluster_8: 14.14, file_cluster_13: 14.195, file_cluster_11: 14.291
- **Magnitude:** 4573.64 | **LOC:** 2451 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 251
- **Risk Profile:** Cognitive Load (92.5764%), Tech Debt (10.4471%)
**Top Internal Functions/Classes:**
  * `PyFrame_GetLineNumber` (Impact: 2897.0 | O(2^N) | DB: 251)
  * `framelocalsproxy_pop` (Impact: 26.6 | O(N^3) | DB: 9)
  * `framelocalsproxy_new` (Impact: 22.6 | O(N^6) | DB: 4)
  * `framelocalsproxy_merge` (Impact: 20.4 | O(N^3) | DB: 6)
  * `framelocalsproxy_richcompare` (Impact: 19.5 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 211`, `args: 3`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 1022`, `dead_code: 1`, `planned_debt: 5`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 395`, `import: 18`
* *Defense:* `safety: 57`, `test: 55`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` pycore_ceval.h, frameobject.c.h, pycore_genobject.h, frameobject.h, pycore_modsupport.h, Python.h, pycore_unicodeobject.h, pycore_code.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_elementtree.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.692 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.438 IQR)
- **Top Global Matches:** file_cluster_8: 13.692, file_cluster_13: 13.931, file_cluster_11: 13.968
- **Magnitude:** 4522.02 | **LOC:** 4559 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(N^6) | **DB Complexity:** 318
- **Risk Profile:** Cognitive Load (94.6299%), Tech Debt (13.2421%)
**Top Internal Functions/Classes:**
  * `element_gc_clear` (Impact: 1787.6 | O(N^6) | DB: 318)
  * `module_exec` (Impact: 241.2 | O(N^6) | DB: 17)
  * `_elementtree_XMLParser__setevents_impl` (Impact: 89.2 | O(N^6) | DB: 11)
  * `expat_pi_handler` (Impact: 82.5 | O(N^4) | DB: 10)
  * `_elementtree_XMLParser___init___impl` (Impact: 79.5 | O(N^6) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 341`, `args: 18`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1332`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `api: 575`, `import: 8`
* *Defense:* `safety: 20`, `doc: 1`, `test: 15`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Python.h, pycore_pyhash.h, stddef.h, expat.h, pyexpat.h, pycore_weakref.h, pycore_dict.h, _elementtree.c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/arraymodule.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.986 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.618 IQR)
- **Top Global Matches:** file_cluster_8: 13.986, file_cluster_13: 14.115, file_cluster_0: 14.171
- **Magnitude:** 4391.7 | **LOC:** 3509 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 18.2%
- **Algorithmic:** O(N^6) | **DB Complexity:** 399
- **Risk Profile:** Cognitive Load (92.5651%), Tech Debt (40.3439%)
**Top Internal Functions/Classes:**
  * `array_del_slice` (Impact: 2111.2 | O(N^6) | DB: 399)
  * `array_richcompare` (Impact: 197.8 | O(N^6) | DB: 35)
  * `II_setitem` (Impact: 37.1 | O(N^6) | DB: 6)
  * `array_resize` (Impact: 24.4 | O(N^3) | DB: 7)
  * `array_slice` (Impact: 21.2 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 274`, `args: 12`, `func_start: 66`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1310`, `dead_code: 4`, `fragile_debt: 3`, `orphaned_logic: 26`
* *Architecture:* `io: 9`, `api: 490`, `import: 11`
* *Defense:* `safety: 30`, `doc: 4`, `test: 15`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` pycore_ceval.h, pycore_moduleobject.h, pycore_bytesobject.h, pycore_modsupport.h, pycore_call.h, Python.h, stddef.h, stdbool.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_datetimemodule.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.66 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.573 IQR)
- **Top Global Matches:** file_cluster_8: 13.66, file_cluster_13: 13.908, file_cluster_0: 13.942
- **Magnitude:** 4363.72 | **LOC:** 7910 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (76.6211%), Tech Debt (36.1927%)
**Top Internal Functions/Classes:**
  * `datetime_date_strftime_impl` (Impact: 564.0 | O(N^6) | DB: 73)
  * `wrap_strftime` (Impact: 264.4 | O(N^6) | DB: 38)
    * *Intent:* /* ---------------------------------------------------------------------------
  * `utc_to_seconds` (Impact: 168.4 | O(2^N) | DB: 6)
  * `parse_hh_mm_ss_ff` (Impact: 162.5 | O(N^4) | DB: 22)
    * *Intent:* #define DATE_SET_FOLD(o, v) (PyDateTime_DATE_GET_FOLD(o) = (v))
  * `parse_isoformat_date` (Impact: 101.1 | O(N^4) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 286`, `args: 23`, `func_start: 95`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 1270`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 32`
* *Architecture:* `api: 550`, `import: 10`
* *Defense:* `safety: 49`, `test: 33`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` datetime.h, time.h, pycore_initconfig.h, winsock2.h, Python.h, pycore_long.h, pycore_unicodeobject.h, pycore_time.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_cursesmodule.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.078 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.084 IQR)
- **Top Global Matches:** file_cluster_8: 13.078, file_cluster_7: 13.457, file_cluster_13: 13.505
- **Magnitude:** 4341.32 | **LOC:** 5657 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (64.8771%), Tech Debt (60.2641%)
**Top Internal Functions/Classes:**
  * `cursesmodule_exec` (Impact: 134.5 | O(N^6) | DB: 29)
    * *Intent:* #endif /* STRICT_SYSV_CURSES */ #ifdef NCURSES_VERSION
  * `PyCurses_ConvertToChtype` (Impact: 76.7 | O(N^6) | DB: 9)
    * *Intent:* #endif #if defined(_AIX) #define STRICT_SYSV_CURSES #endif #if defined(HAVE_NCURSESW) && NCURSES_EXT...
  * `PyCursesWindow_ChgAt` (Impact: 66.0 | O(N^6) | DB: 17)
    * *Intent:* #ifdef HAVE_NCURSESW
  * `_curses_window_addstr_impl` (Impact: 49.1 | O(N^6) | DB: 20)
    * *Intent:* #define Window_OneArgNoReturnFunction(X, TYPE, PARSESTR) \
  * `_curses_window_addnstr_impl` (Impact: 48.9 | O(N^6) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 532`, `structural_boundaries: 374`, `args: 10`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 1671`, `fragile_debt: 1`, `orphaned_logic: 86`
* *Architecture:* `io: 12`, `api: 964`, `import: 9`
* *Defense:* `safety: 11`, `doc: 2`, `test: 10`, `immutability_locks: 51`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` pycore_capsule.h, Python.h, pycore_long.h, pycore_fileutils.h, py_curses.h, pycore_structseq.h, term.h, _cursesmodule.c.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/cjkcodecs/multibytecodec.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.093 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.231 IQR)
- **Top Global Matches:** file_cluster_8: 13.093, file_cluster_12: 13.409, file_cluster_7: 13.418
- **Magnitude:** 4108.46 | **LOC:** 2147 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 228
- **Risk Profile:** Cognitive Load (96.3181%), Tech Debt (8.2866%)
**Top Internal Functions/Classes:**
  * `multibytecodec_encode` (Impact: 2653.6 | O(2^N) | DB: 228)
  * `multibytecodec_encerror` (Impact: 182.7 | O(N^6) | DB: 27)
  * `multibytecodec_decerror` (Impact: 141.7 | O(N^6) | DB: 15)
  * `internal_error_callback` (Impact: 24.6 | O(N^2))
  * `expand_encodebuffer` (Impact: 15.2 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 168`, `args: 3`, `func_start: 56`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 708`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 336`, `import: 4`
* *Defense:* `safety: 8`, `doc: 2`, `test: 8`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` multibytecodec.c.h, Python.h, stddef.h, multibytecodec.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_hacl/Hacl_Hash_SHA3.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.561 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.078 IQR)
- **Top Global Matches:** file_cluster_8: 14.561, file_cluster_7: 14.82, file_cluster_13: 14.851
- **Magnitude:** 3968.02 | **LOC:** 2458 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 225
- **Risk Profile:** Cognitive Load (55.6967%), Tech Debt (17.0019%)
**Top Internal Functions/Classes:**
  * `Hacl_Hash_SHA3_update` (Impact: 52.1 | O(N^2) | DB: 77)
  * `Hacl_Hash_SHA3_update_last_sha3` (Impact: 31.0 | O(N^2) | DB: 225)
  * `Hacl_Hash_SHA3_copy` (Impact: 28.1 | O(N^3) | DB: 28)
  * `Hacl_Hash_SHA3_malloc` (Impact: 27.8 | O(N^3) | DB: 21)
  * `digest_` (Impact: 24.6 | O(N^2) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 63`, `args: 1`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 2603`, `orphaned_logic: 21`
* *Architecture:* `api: 962`, `import: 3`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Hacl_Streaming_Types.h, Hacl_Streaming_Types.h, Hacl_Hash_SHA3.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/clinic/_cursesmodule.c.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.25 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.935 IQR)
- **Top Global Matches:** file_cluster_8: 13.25, file_cluster_12: 13.577, file_cluster_7: 13.618
- **Magnitude:** 3928.38 | **LOC:** 4454 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (73.5572%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_curses_ungetmouse` (Impact: 179.3 | O(N^6) | DB: 8)
  * `_curses_resizeterm` (Impact: 83.2 | O(N^6) | DB: 6)
  * `_curses_resize_term` (Impact: 83.2 | O(N^6) | DB: 6)
  * `_curses_setupterm` (Impact: 63.9 | O(N^4) | DB: 19)
  * `_curses_window_addnstr` (Impact: 52.3 | O(N^4) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 742`, `structural_boundaries: 137`, `args: 4`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 1398`
* *Architecture:* `io: 2`, `api: 680`, `import: 3`
* *Defense:* `safety: 6`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pycore_runtime.h, pycore_gc.h, pycore_modsupport.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `Misc/mypy/_colorize.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Modules/makexp_aix` (SHELL) | Magnitude: 10.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: io: 21, safety_bypasses: 16, debug_prints: 9, state_mutation: 6
- `Objects/mimalloc/alloc-aligned.c` (C) | Magnitude: 178.7 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 140, pointers: 109, structural_boundaries: 107, safety: 88
- `Objects/floatobject.c` (C) | Magnitude: 534.9 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 253, indent_spaces: 208, branch: 64, pointers: 57
- `Objects/mimalloc/page.c` (C) | Magnitude: 766.06 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 489, state_mutation: 397, pointers: 214, branch: 151
- `Include/internal/mimalloc/mimalloc.h` (C) | Magnitude: 255.2 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 282, api: 193, pointers: 193, indent_spaces: 178

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `Tools/cases_generator/uop_metadata_generator.py` (PYTHON) | Magnitude: 0.24 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 113, branch: 49, events: 42, encapsulation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `PC/launcher2.c` (C) | Magnitude: 2426.66 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 815, state_mutation: 645, branch: 302, pointers: 291
- `Tools/wasm/wasi-env` (SHELL) | Magnitude: 0.08 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 47, indent_spaces: 25, reflection_metaprogramming: 23, debug_prints: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Include/internal/pycore_pyatomic_ft_wrappers.h` (C) | Magnitude: 52.6 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 121, reflection_metaprogramming: 113, pointers: 55, indent_spaces: 52
- `Mac/BuildScript/scripts/postflight.framework` (SHELL) | Magnitude: 5.04 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 22, indent_spaces: 12, structural_boundaries: 5, io: 4
- `Python/ceval_macros.h` (C) | Magnitude: 186.22 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, macros: 164, state_mutation: 125, branch: 104
- `Include/internal/pycore_stats.h` (C) | Magnitude: 96.14 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 67, macros: 57, reflection_metaprogramming: 47, indent_spaces: 34
- `Mac/BuildScript/resources/update_shell_profile.command` (SHELL) | Magnitude: 106.6 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: reflection_metaprogramming: 58, indent_tabs: 58, state_mutation: 51, branch: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Objects/object.c` (C) | Magnitude: 5416.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1369, state_mutation: 620, pointers: 590, api: 345
- `Modules/_decimal/libmpdec/bench_full.c` (C) | Magnitude: 165.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 72, pointers: 27, api: 17
- `Modules/_decimal/libmpdec/basearith.c` (C) | Magnitude: 872.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 482, indent_spaces: 308, branch: 99, api: 92
- `Objects/mimalloc/alloc-posix.c` (C) | Magnitude: 141.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 89, indent_spaces: 79, structural_boundaries: 57, api: 48
- `Tools/c-analyzer/c_analyzer/match.py` (PYTHON) | Magnitude: 0.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 63, branch: 48, encapsulation: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Tools/msi/make_appx.ps1` (POWERSHELL) | Magnitude: 0.04 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, branch: 24, state_mutation: 21, doc: 8
- `Tools/msi/make_cat.ps1` (POWERSHELL) | Magnitude: 0.02 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, branch: 8, doc: 7, explicit_casts: 6
- `Tools/msi/sdktools.psm1` (POWERSHELL) | Magnitude: 0.14 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, branch: 23, state_mutation: 19, api: 11
- `Tools/msi/uploadrelease.ps1` (POWERSHELL) | Magnitude: 0.13 | Delta: **0.279 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 100, state_mutation: 79, branch: 59, api: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Tools/clinic/libclinic/identifiers.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, branch: 4, api: 4
- `Tools/cases_generator/stack.py` (PYTHON) | Magnitude: 2.03 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 621, branch: 208, structural_boundaries: 168, state_mutation: 136
- `Tools/clinic/libclinic/converters.py` (PYTHON) | Magnitude: 1.59 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 666, structural_boundaries: 289, state_mutation: 273, branch: 159
- `Tools/cases_generator/_typing_backports.py` (PYTHON) | Magnitude: 0.0 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, args: 1, func_start: 1
- `Tools/scripts/sortperf.py` (PYTHON) | Magnitude: 0.09 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 41, generics: 27, state_mutation: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Tools/peg_generator/pegen/ast_dump.py` (PYTHON) | Magnitude: 0.31 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 55, branch: 25, encapsulation: 20, structural_boundaries: 15
- `Doc/_static/profiling-sampling-visualization.js` (JAVASCRIPT) | Magnitude: 1304.9 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 928, state_mutation: 780, safety: 391, args: 111
- `Doc/tools/static/rtd_switcher.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.205 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 8, immutability_locks: 7, structural_boundaries: 6
- `Doc/tools/static/changelog_search.js` (JAVASCRIPT) | Magnitude: 0.06 | Delta: **0.24 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 12, branch: 11, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Android/android.py` (PYTHON) | Magnitude: 1732.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 598, branch: 175, structural_boundaries: 144, concurrency: 70
- `Objects/mimalloc/bitmap.c` (C) | Magnitude: 1156.9 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 843, indent_spaces: 279, pointers: 154, api: 128
- `Platforms/emscripten/web_example/python.worker.mjs` (JAVASCRIPT) | Magnitude: 99.38 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 33, concurrency: 15, immutability_locks: 14
- `Objects/mimalloc/init.c` (C) | Magnitude: 282.02 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 253, state_mutation: 124, pointers: 85, structural_boundaries: 80
- `Objects/mimalloc/stats.c` (C) | Magnitude: 376.74 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 304, indent_spaces: 288, state_mutation: 183, branch: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Tools/c-analyzer/distutils/errors.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, structural_boundaries: 14, class_start: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Modules/_testlimitedcapi/threadstate.c` (C) | Magnitude: 16.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, api: 7, pointers: 6, state_mutation: 4
- `Doc/tools/extensions/patchlevel.py` (PYTHON) | Magnitude: 0.07 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 15, branch: 8, io: 4
- `Objects/moduleobject.c` (C) | Magnitude: 923.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 778, state_mutation: 324, pointers: 244, branch: 219
- `Modules/_testinternalcapi/test_critical_sections.c` (C) | Magnitude: 57.4 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, sec_high_risk_execution: 46, state_mutation: 31, pointers: 22
- `Python/import.c` (C) | Magnitude: 2753.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1344, state_mutation: 729, pointers: 463, api: 442

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Python/getcopyright.c` (C) | Magnitude: 9.08 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 6, ownership: 5, structural_boundaries: 2, immutability_locks: 2
- `Include/internal/pycore_lock.h` (C) | Magnitude: 17.26 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 6, structural_boundaries: 5, args: 5, explicit_casts: 5
- `Include/internal/pycore_parking_lot.h` (C) | Magnitude: 23.54 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 15, pointers: 10, args: 9, macros: 6
- `PC/zconf.h` (C) | Magnitude: 30.62 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 56, branch: 24, structural_boundaries: 17, api: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Python/bytecodes.c` -> Churn: **100.0%** | Cog Load: 62.6613% | Debt: 13.8611%
- `Python/optimizer_bytecodes.c` -> Churn: **95.31%** | Cog Load: 73.9089% | Debt: 9.057%
- `Python/ceval.c` -> Churn: **85.47%** | Cog Load: 80.24% | Debt: 14.9988%
- `Python/optimizer.c` -> Churn: **81.99%** | Cog Load: 90.9349% | Debt: 8.6742%
- `Objects/dictobject.c` -> Churn: **79.86%** | Cog Load: 92.9154% | Debt: 21.8647%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Python/dtoa.c` -> **Sergey B Kirpichev** (100.0% isolated ownership) | Magnitude: 7901.16
- `Modules/_decimal/clinic/_decimal.c.h` -> **Sergey B Kirpichev** (100.0% isolated ownership) | Magnitude: 6690.3
- `Modules/expat/xmlparse.c` -> **Stan Ulbrych** (100.0% isolated ownership) | Magnitude: 6458.16
- `Modules/clinic/_cursesmodule.c.h` -> **vict-Yang** (100.0% isolated ownership) | Magnitude: 3928.38
- `Python/getargs.c` -> **Victor Stinner** (100.0% isolated ownership) | Magnitude: 3710.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Include/internal/pycore_gc.h` -> **Severity: 0.138** (Bridge: 0.0014 * Flux: 100.0%)
- `Include/internal/pycore_object.h` -> **Severity: 0.136** (Bridge: 0.0014 * Flux: 98.83%)
- `Include/internal/pycore_unicodeobject.h` -> **Severity: 0.075** (Bridge: 0.0008 * Flux: 100.0%)
- `Include/internal/pycore_pystate.h` -> **Severity: 0.053** (Bridge: 0.001 * Flux: 50.4324%)
- `PC/winreg.c` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 99.9998%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Include/internal/pycore_structs.h` -> **Severity: 2417.8** (Blast Radius: 24.178 * Doc Risk: 100.0%)
- `Include/internal/pycore_context.h` -> **Severity: 2075.5** (Blast Radius: 20.755 * Doc Risk: 100.0%)
- `Include/internal/pycore_modsupport.h` -> **Severity: 1821.5** (Blast Radius: 18.215 * Doc Risk: 100.0%)
- `Modules/_testlimitedcapi/sys.c` -> **Severity: 1794.936** (Blast Radius: 17.953 * Doc Risk: 99.9797%)
- `Include/internal/mimalloc/mimalloc.h` -> **Severity: 1513.3** (Blast Radius: 15.133 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
