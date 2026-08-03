# ARCHITECTURAL_BRIEF: root
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/root` |
| **Timestamp** | `2026-08-03T21:28:17.918534+00:00` |
| **Scan Duration** | `61.1s` |
| **Git Branch** | `master` |
| **Git Commit** | `e082dce9bac50cc8ea6f3acb68c306692b712770` |
| **Git Remote** | `https://github.com/root-project/root.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 12154 malicious artifacts.

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
| Total Artifacts | 31167 |
| Analyzed Artifacts (Scanned) | 13910 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17257 |
| Total LOC | 1979479 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 44.6% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0826 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 588 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 9250 | 1458673 | 66.5% |
| C | 1478 | 238792 | 10.6% |
| PLAINTEXT | 1145 | 0 | 8.2% |
| PYTHON | 692 | 65503 | 5.0% |
| MARKDOWN | 291 | 0 | 2.1% |
| HTML | 193 | 23155 | 1.4% |
| MAKEFILE | 167 | 31974 | 1.2% |
| JAVASCRIPT | 136 | 68129 | 1.0% |
| BINARY_THREAT | 122 | 122 | 0.9% |
| TD | 120 | 59536 | 0.9% |
| SHELL | 75 | 3762 | 0.5% |
| XML | 69 | 0 | 0.5% |
| OBJECTIVE-C | 44 | 7941 | 0.3% |
| BATCH | 28 | 535 | 0.2% |
| M4 | 28 | 2641 | 0.2% |
| CSS | 18 | 2064 | 0.1% |
| JSON | 17 | 1183 | 0.1% |
| YAML | 12 | 440 | 0.1% |
| PERL | 11 | 2895 | 0.1% |
| DOCKERFILE | 5 | 129 | 0.0% |
| FORTRAN | 4 | 11212 | 0.0% |
| PROTO | 2 | 118 | 0.0% |
| POWERSHELL | 1 | 6 | 0.0% |
| APEX | 1 | 655 | 0.0% |
| SQLITE | 1 | 14 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.027`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 6897 | 49.6% |
| file_cluster_8 | 4440 | 31.9% |
| file_cluster_7 | 446 | 3.2% |
| file_cluster_9 | 179 | 1.3% |
| Unknown | 122 | 0.9% |
| file_cluster_4 | 105 | 0.8% |
| file_cluster_16 | 86 | 0.6% |
| file_cluster_11 | 81 | 0.6% |
| file_cluster_0 | 41 | 0.3% |
| file_cluster_17 | 24 | 0.2% |
| file_cluster_12 | 19 | 0.1% |
| file_cluster_2 | 16 | 0.1% |
| file_cluster_6 | 12 | 0.1% |
| file_cluster_1 | 4 | 0.0% |
| file_cluster_15 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1436 | 10.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17257*

**Composition by Extension & Reason:**
- `.cpp`: 3805x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1336 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2773 LOC)
- `.h`: 2994x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 33 LOC), 1x Excluded (Embedded Array/Matrix Payload: 8583 commas in 941 LOC)
- `.c`: 1488x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 2720 hex tokens in 994 LOC), 1x Excluded (Embedded Array/Matrix Payload: 17555 commas in 3790 LOC)
- `.rst`: 1316x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 34x Excluded (Unsupported Extension: '.rst')
- `.ref`: 1046x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cxx`: 1020x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3064 LOC), 1x Excluded (Embedded Array/Matrix Payload: 4995 commas in 1165 LOC)
- `.png`: 892x Excluded (Explicitly Denied Extension: '.png')
- `.xml`: 828x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.td`: 543x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2144 LOC), 1x Excluded (Embedded Array/Matrix Payload: 2980 commas in 910 LOC)
- `.xpm`: 357x Excluded (Unsupported Extension: '.xpm'), 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.root`: 309x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Unsupported Extension: '.root')
- `.py`: 263x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 362 LOC), 1x Excluded (Saturation: Line 34 exceeds 500 chars)
- `.txt`: 245x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 9 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1081 LOC)
- `.jpg`: 191x Excluded (Explicitly Denied Extension: '.jpg')
- `.cmake`: 114x Excluded (Unsupported Extension: '.cmake'), 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.cmake)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 29.8 | 29.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 33.3 | 17.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.0 | 15.6 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.1 | 2.4 | 80.0 |
| API Exposure | 0.0 | 18.0 | 3.5 | 1.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 72.8 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 17.0 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 90.0 | 1.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.1 | 12.3 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 37.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.8 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.5 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `interpreter/llvm-project/clang/www/c_dr_status.html` (Hits: 896)
- `interpreter/llvm-project/clang/www/cxx_status.html` (Hits: 562)
- `interpreter/llvm-project/clang/www/c_status.html` (Hits: 424)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TMath.h** (`math/mathcore/inc/TMath.h`) — 572 inbound connections
2. **TROOT.h** (`core/base/inc/TROOT.h`) — 561 inbound connections
3. **TError.h** (`core/foundation/inc/TError.h`) — 402 inbound connections
4. **TString.h** (`core/base/inc/TString.h`) — 370 inbound connections
5. **TCanvas.h** (`graf2d/gpad/inc/TCanvas.h`) — 351 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **converters.h** (`graf2d/win32gdk/gdk/src/iconv/converters.h`) — 146 outbound dependencies
2. **TCling.cxx** (`core/metacling/src/TCling.cxx`) — 134 outbound dependencies
3. **Sema.h** (`interpreter/llvm-project/clang/include/clang/Sema/Sema.h`) — 92 outbound dependencies
4. **DwarfLinkerForBinary.cpp** (`interpreter/llvm-project/llvm/tools/dsymutil/DwarfLinkerForBinary.cpp`) — 90 outbound dependencies
5. **CodeGenPassBuilder.h** (`interpreter/llvm-project/llvm/include/llvm/Passes/CodeGenPassBuilder.h`) — 82 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inheritsFrom` (@ `interpreter/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp`) -> Impact: **12545.9** | LOC: 525
  * *Intent:* /// inheritsFrom - Indicates whether all instructions in one class also belong /// to another class. /// /// @param child - The class that may be the ...
- `printInst` (@ `interpreter/llvm-project/llvm/tools/llvm-objdump/llvm-objdump.cpp`) -> Impact: **10673.7** | LOC: 1540
- `warn` (@ `interpreter/llvm-project/llvm/tools/llvm-nm/llvm-nm.cpp`) -> Impact: **7665.9** | LOC: 1559
- `dav_move_file` (@ `net/http/civetweb/civetweb.c`) -> Impact: **6866.6** | LOC: 2093
- `TranslateCoordinates` (@ `graf2d/cocoa/src/QuartzWindow.mm`) -> Impact: **5889.7** | LOC: 1874
- `writePrettyPrintFunction` (@ `interpreter/llvm-project/clang/utils/TableGen/ClangAttrEmitter.cpp`) -> Impact: **4856.9** | LOC: 1379
- `findUnwindRelocNameAddend` (@ `interpreter/llvm-project/llvm/tools/llvm-objdump/MachODump.cpp`) -> Impact: **4606.6** | LOC: 660
- `TDecompSparse::Factor_sub2` (@ `math/matrix/src/TDecompSparse.cxx`) -> Impact: **4057.1** | LOC: 502
- `TLatex::Analyse` (@ `graf2d/graf/src/TLatex.cxx`) -> Impact: **3710.6** | LOC: 1316
  * *Intent:* /// when the argument is an atom (normal text), it calculates /// the size of it and return it as the result. /// for example : if the operator #%frac...
- `TStreamerInfo::ReadBuffer` (@ `io/io/src/TStreamerInfoReadBuffer.cxx`) -> Impact: **3649.4** | LOC: 749
  * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Deserialize information from buffer b into object at pointer /// ...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_build_ranges` (@ `bindings/distrdf/python/DistRDF/HeadNode.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `bindings/pyroot/cppyy/cppyy/python/cppyy/_cpython_cppyy.py`) -> **O(2^N) [Recursive]**
- `__processGroupContentLine` (@ `bindings/pyroot/pythonizations/python/ROOT/JsMVA/OutputTransformer.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Transform one line of C++ output string to HTML. # @param self object pointer # @param line line to transform
- `GetValue` (@ `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_rdataframe.py`) -> **O(2^N) [Recursive]**
- `getGuardedStlInclude` (@ `cmake/unix/makepchinput.py`) -> **O(2^N) [Recursive]**
  * *Intent:* #------------------------------------------------------------------------------- def getGuardedStlInclude(headerName): return '#if __has_include("%s")...
- `__init__` (@ `interpreter/cling/tools/Jupyter/kernel/clingkernel.py`) -> **O(2^N) [Recursive]**
- `_GetSymbols` (@ `interpreter/llvm-project/clang/tools/include-mapping/cppreference_parser.py`) -> **O(2^N) [Recursive]**
- `main` (@ `interpreter/llvm-project/clang/tools/scan-view/bin/scan-view`) -> **O(2^N) [Recursive]**
- `checkTypeValues` (@ `interpreter/llvm-project/clang/utils/ABITest/ABITestGen.py`) -> **O(2^N) [Recursive]**
- `captureDriverInfo` (@ `interpreter/llvm-project/clang/utils/CmpDriver`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `TH1::Clone` (@ `hist/hist/src/TH1.cxx`) -> DB Complexity: **789**
- `TPad::Close` (@ `graf2d/gpad/src/TPad.cxx`) -> DB Complexity: **786**
- `TLatex::Analyse` (@ `graf2d/graf/src/TLatex.cxx`) -> DB Complexity: **734**
  * *Intent:* /// when the argument is an atom (normal text), it calculates /// the size of it and return it as the result. /// for example : if the operator #%frac...
- `south_gate` (@ `tutorials/visualisation/geom/south_gate.C`) -> DB Complexity: **711**
  * *Intent:* /// Supervisor: Prof. Inkyu Park (icpark@physics.uos.ac.kr) /// /// How to run: `.x south_gate.C` in ROOT terminal, then use OpenGL /// /// This macro...
- `TClass::GetBaseClassOffset` (@ `core/meta/src/TClass.cxx`) -> DB Complexity: **704**
  * *Intent:* // Now we a dot
- `TASImage::ReadImage` (@ `graf2d/asimage/src/TASImage.cxx`) -> DB Complexity: **659**
- `TH2::DoFitSlices` (@ `hist/hist/src/TH2.cxx`) -> DB Complexity: **645**
- `warn` (@ `interpreter/llvm-project/llvm/tools/llvm-nm/llvm-nm.cpp`) -> DB Complexity: **643**
- `inheritsFrom` (@ `interpreter/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp`) -> DB Complexity: **618**
  * *Intent:* /// inheritsFrom - Indicates whether all instructions in one class also belong /// to another class. /// /// @param child - The class that may be the ...
- `TGWin32::UpdateMarkerStyle` (@ `graf2d/win32gdk/src/TGWin32.cxx`) -> DB Complexity: **609**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `builtins/glew/src` | 3 | 131376.76 | 55.37% | 8.17% |
| `hist/hist/src` | 72 | 97830.3 | 38.63% | 80.66% |
| `gui/gui/src` | 92 | 90054.1 | 36.63% | 82.36% |
| `geom/geom/src` | 53 | 83841.3 | 38.94% | 89.45% |
| `tmva/tmva/src` | 159 | 81981.74 | 32.65% | 86.93% |
| `roofit/roofitcore/src` | 223 | 79636.76 | 33.41% | 81.98% |
| `interpreter/llvm-project/llvm/lib/Transforms/Utils` | 91 | 76701.7 | 56.42% | 57.7% |
| `tmva/sofie/test/input_models` | 122 | 61000.0 | 0.0% | 0.0% |
| `io/io/src` | 37 | 53346.14 | 46.87% | 82.17% |
| `interpreter/llvm-project/llvm/utils/TableGen` | 52 | 49475.1 | 48.87% | 49.07% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bindings/distrdf/python/DistRDF/ComputationGraphGenerator.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Proxy.py` -> **100.0%** Exposure
- `bindings/pyroot/cppyy/cppyy/bench/py_functioncalls.py` -> **100.0%** Exposure
- `bindings/pyroot/cppyy/cppyy/python/cppyy/_stdcpp_fix.py` -> **100.0%** Exposure
- `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_pyz_utils.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bindings/pyroot/pythonizations/python/ROOT/_jupyroot/helpers/cppcompleter.py` -> **100.0%** Exposure
- `bindings/pyroot/pythonizations/python/ROOT/_jupyroot/helpers/handlers.py` -> **100.0%** Exposure
- `bindings/pyroot/pythonizations/python/ROOT/_jupyroot/helpers/utils.py` -> **100.0%** Exposure
- `etc/notebook/jupyter_notebook_config.py.in` -> **100.0%** Exposure
- `geom/gdml/writer.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `graf2d/win32gdk/src/TGWin32.cxx` -> **207** Orphaned Functions | **22** Duplicates
- `interpreter/llvm-project/llvm/include/llvm/Transforms/IPO/Attributor.h` -> **55** Orphaned Functions | **141** Duplicates
- `interpreter/llvm-project/clang/include/clang/AST/ExprCXX.h` -> **0** Orphaned Functions | **188** Duplicates
- `io/xml/src/TBufferXML.cxx` -> **81** Orphaned Functions | **101** Duplicates
- `core/metacling/src/TCling.cxx` -> **135** Orphaned Functions | **43** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tutorials/machine_learning/TMVA_CNN_Classification.py`** -> AI Confidence: **99.48%**
2. **`tutorials/machine_learning/TMVA_RNN_Classification.py`** -> AI Confidence: **99.48%**
3. **`core/base/inc/LinkDef.h`** -> AI Confidence: **99.48%**
4. **`core/base/src/TColor.cxx`** -> AI Confidence: **99.48%**
5. **`core/base/src/TErrorDefaultHandler.cxx`** -> AI Confidence: **99.48%**
6. **`core/base/src/TFileCollection.cxx`** -> AI Confidence: **99.48%**
7. **`core/base/src/TPRegexp.cxx`** -> AI Confidence: **99.48%**
8. **`core/base/src/TPluginManager.cxx`** -> AI Confidence: **99.48%**
9. **`core/base/src/TRemoteObject.cxx`** -> AI Confidence: **99.48%**
10. **`core/base/src/TSystem.cxx`** -> AI Confidence: **99.48%**
11. **`core/base/src/TUrl.cxx`** -> AI Confidence: **99.48%**
12. **`core/foundation/src/TClassEdit.cxx`** -> AI Confidence: **99.48%**
13. **`core/gui/src/TContextMenu.cxx`** -> AI Confidence: **99.48%**
14. **`core/meta/src/TDataMember.cxx`** -> AI Confidence: **99.48%**
15. **`core/metacling/src/TClingTypeInfo.cxx`** -> AI Confidence: **99.48%**
16. **`core/multiproc/src/TMPClient.cxx`** -> AI Confidence: **99.48%**
17. **`core/textinput/src/Getline_color.cxx`** -> AI Confidence: **99.48%**
18. **`geom/gdml/src/TGDMLParse.cxx`** -> AI Confidence: **99.48%**
19. **`geom/gdml/src/TGDMLWrite.cxx`** -> AI Confidence: **99.48%**
20. **`geom/geom/src/TGeoSphere.cxx`** -> AI Confidence: **99.48%**
21. **`geom/geom/src/TGeoVoxelFinder.cxx`** -> AI Confidence: **99.48%**
22. **`geom/geombuilder/src/TGeoPgonEditor.cxx`** -> AI Confidence: **99.48%**
23. **`geom/geomchecker/src/TGeoChecker.cxx`** -> AI Confidence: **99.48%**
24. **`graf2d/asimage/src/TASImage.cxx`** -> AI Confidence: **99.48%**
25. **`graf2d/asimage/src/TASPaletteEditor.cxx`** -> AI Confidence: **99.48%**
26. **`graf2d/asimage/src/libAfterImage/afterbase.h.in`** -> AI Confidence: **99.48%**
27. **`graf2d/gpad/src/TClassTree.cxx`** -> AI Confidence: **99.48%**
28. **`graf2d/gpad/src/TCreatePrimitives.cxx`** -> AI Confidence: **99.48%**
29. **`graf2d/gpad/src/TGroupButton.cxx`** -> AI Confidence: **99.48%**
30. **`graf2d/gpad/src/TInspectCanvas.cxx`** -> AI Confidence: **99.48%**
31. **`graf2d/gpad/src/TPad.cxx`** -> AI Confidence: **99.48%**
32. **`graf2d/gpadv7/src/RMenuItems.cxx`** -> AI Confidence: **99.48%**
33. **`graf2d/graf/src/TBox.cxx`** -> AI Confidence: **99.48%**
34. **`graf2d/graf/src/TCandle.cxx`** -> AI Confidence: **99.48%**
35. **`graf2d/graf/src/TDiamond.cxx`** -> AI Confidence: **99.48%**
36. **`graf2d/graf/src/TGraphPolargram.cxx`** -> AI Confidence: **99.48%**
37. **`graf2d/graf/src/TLatex.cxx`** -> AI Confidence: **99.48%**
38. **`graf2d/graf/src/TLegend.cxx`** -> AI Confidence: **99.48%**
39. **`graf2d/graf/src/TText.cxx`** -> AI Confidence: **99.48%**
40. **`graf2d/mathtext/src/mathtextparse.cxx`** -> AI Confidence: **99.48%**
41. **`graf2d/postscript/src/TImageDump.cxx`** -> AI Confidence: **99.48%**
42. **`graf2d/postscript/src/TPDF.cxx`** -> AI Confidence: **99.48%**
43. **`graf2d/postscript/src/TPostScript.cxx`** -> AI Confidence: **99.48%**
44. **`graf2d/postscript/src/TSVG.cxx`** -> AI Confidence: **99.48%**
45. **`graf2d/postscript/src/TTeXDump.cxx`** -> AI Confidence: **99.48%**
46. **`graf2d/x11/src/Rotated.cxx`** -> AI Confidence: **99.48%**
47. **`graf2d/x11/src/TGX11.cxx`** -> AI Confidence: **99.48%**
48. **`graf3d/eve/src/TEveBrowser.cxx`** -> AI Confidence: **99.48%**
49. **`graf3d/eve/src/TEveCalo2DGL.cxx`** -> AI Confidence: **99.48%**
50. **`graf3d/eve/src/TEveCaloLegoGL.cxx`** -> AI Confidence: **99.48%**
51. **`graf3d/eve/src/TEveCaloLegoOverlay.cxx`** -> AI Confidence: **99.48%**
52. **`graf3d/eve/src/TEveLegoEventHandler.cxx`** -> AI Confidence: **99.48%**
53. **`graf3d/eve/src/TEveTextGL.cxx`** -> AI Confidence: **99.48%**
54. **`graf3d/g3d/src/TSPHE.cxx`** -> AI Confidence: **99.48%**
55. **`graf3d/g3d/src/TXTRU.cxx`** -> AI Confidence: **99.48%**
56. **`graf3d/gl/src/TGLAxis.cxx`** -> AI Confidence: **99.48%**
57. **`graf3d/gl/src/TGLAxisPainter.cxx`** -> AI Confidence: **99.48%**
58. **`graf3d/gl/src/TGLBoxPainter.cxx`** -> AI Confidence: **99.48%**
59. **`graf3d/gl/src/TGLCameraOverlay.cxx`** -> AI Confidence: **99.48%**
60. **`graf3d/gl/src/TGLEventHandler.cxx`** -> AI Confidence: **99.48%**
61. **`graf3d/gl/src/TGLFontManager.cxx`** -> AI Confidence: **99.48%**
62. **`graf3d/gl/src/TGLHistPainter.cxx`** -> AI Confidence: **99.48%**
63. **`graf3d/gl/src/TGLLegoPainter.cxx`** -> AI Confidence: **99.48%**
64. **`graf3d/gl/src/TGLPolyMarker.cxx`** -> AI Confidence: **99.48%**
65. **`graf3d/gl/src/TGLSAViewer.cxx`** -> AI Confidence: **99.48%**
66. **`graf3d/gl/src/TGLSurfacePainter.cxx`** -> AI Confidence: **99.48%**
67. **`graf3d/gl/src/TGLText.cxx`** -> AI Confidence: **99.48%**
68. **`graf3d/gl/src/TGLVoxelPainter.cxx`** -> AI Confidence: **99.48%**
69. **`graf3d/gl/src/TH2GL.cxx`** -> AI Confidence: **99.48%**
70. **`gui/fitpanel/src/TFitEditor.cxx`** -> AI Confidence: **99.48%**
71. **`gui/fitpanel/src/TFitParametersDialog.cxx`** -> AI Confidence: **99.48%**
72. **`gui/ged/src/TFunctionParametersDialog.cxx`** -> AI Confidence: **99.48%**
73. **`gui/ged/src/TGedPatternSelect.cxx`** -> AI Confidence: **99.48%**
74. **`gui/ged/src/TGraphEditor.cxx`** -> AI Confidence: **99.48%**
75. **`gui/ged/src/TH1Editor.cxx`** -> AI Confidence: **99.48%**
76. **`gui/ged/src/TStyleDialog.cxx`** -> AI Confidence: **99.48%**
77. **`gui/gui/src/TGApplication.cxx`** -> AI Confidence: **99.48%**
78. **`gui/gui/src/TGButton.cxx`** -> AI Confidence: **99.48%**
79. **`gui/gui/src/TGButtonGroup.cxx`** -> AI Confidence: **99.48%**
80. **`gui/gui/src/TGColorDialog.cxx`** -> AI Confidence: **99.48%**
81. **`gui/gui/src/TGColorSelect.cxx`** -> AI Confidence: **99.48%**
82. **`gui/gui/src/TGCommandPlugin.cxx`** -> AI Confidence: **99.48%**
83. **`gui/gui/src/TGFSComboBox.cxx`** -> AI Confidence: **99.48%**
84. **`gui/gui/src/TGFileBrowser.cxx`** -> AI Confidence: **99.48%**
85. **`gui/gui/src/TGFileDialog.cxx`** -> AI Confidence: **99.48%**
86. **`gui/gui/src/TGFont.cxx`** -> AI Confidence: **99.48%**
87. **`gui/gui/src/TGFontDialog.cxx`** -> AI Confidence: **99.48%**
88. **`gui/gui/src/TGGC.cxx`** -> AI Confidence: **99.48%**
89. **`gui/gui/src/TGLabel.cxx`** -> AI Confidence: **99.48%**
90. **`gui/gui/src/TGListView.cxx`** -> AI Confidence: **99.48%**
91. **`gui/gui/src/TGMsgBox.cxx`** -> AI Confidence: **99.48%**
92. **`gui/gui/src/TGNumberEntry.cxx`** -> AI Confidence: **99.48%**
93. **`gui/gui/src/TGResourcePool.cxx`** -> AI Confidence: **99.48%**
94. **`gui/gui/src/TGSpeedo.cxx`** -> AI Confidence: **99.48%**
95. **`gui/gui/src/TGTextEdit.cxx`** -> AI Confidence: **99.48%**
96. **`gui/gui/src/TGTextEditDialogs.cxx`** -> AI Confidence: **99.48%**
97. **`gui/gui/src/TGTextEditor.cxx`** -> AI Confidence: **99.48%**
98. **`gui/gui/src/TGView.cxx`** -> AI Confidence: **99.48%**
99. **`gui/gui/src/TRootBrowser.cxx`** -> AI Confidence: **99.48%**
100. **`gui/gui/src/TRootCanvas.cxx`** -> AI Confidence: **99.48%**
101. **`gui/gui/src/TRootContextMenu.cxx`** -> AI Confidence: **99.48%**
102. **`gui/gui/src/TRootDialog.cxx`** -> AI Confidence: **99.48%**
103. **`gui/guihtml/src/TGHtmlBrowser.cxx`** -> AI Confidence: **99.48%**
104. **`gui/guihtml/src/TGHtmlForm.cxx`** -> AI Confidence: **99.48%**
105. **`gui/guihtml/src/TGHtmlParse.cxx`** -> AI Confidence: **99.48%**
106. **`gui/guihtml/src/TGHtmlSizer.cxx`** -> AI Confidence: **99.48%**
107. **`hist/hist/src/AnalyticalIntegrals.cxx`** -> AI Confidence: **99.48%**
108. **`hist/hist/src/HFitImpl.cxx`** -> AI Confidence: **99.48%**
109. **`hist/hist/src/HFitInterface.cxx`** -> AI Confidence: **99.48%**
110. **`hist/hist/src/TBinomialEfficiencyFitter.cxx`** -> AI Confidence: **99.48%**
111. **`hist/hist/src/TFormula_v5.cxx`** -> AI Confidence: **99.48%**
112. **`hist/hist/src/TH1Merger.cxx`** -> AI Confidence: **99.48%**
113. **`hist/hist/src/TH3.cxx`** -> AI Confidence: **99.48%**
114. **`hist/hist/src/THnBase.cxx`** -> AI Confidence: **99.48%**
115. **`hist/hist/src/TLimit.cxx`** -> AI Confidence: **99.48%**
116. **`hist/hist/src/TMultiDimFit.cxx`** -> AI Confidence: **99.48%**
117. **`hist/hist/src/TMultiGraph.cxx`** -> AI Confidence: **99.48%**
118. **`hist/hist/src/TPrincipal.cxx`** -> AI Confidence: **99.48%**
119. **`hist/hist/src/TProfile2D.cxx`** -> AI Confidence: **99.48%**
120. **`hist/hist/src/TSpline.cxx`** -> AI Confidence: **99.48%**
121. **`hist/histpainter/src/TGraph2DPainter.cxx`** -> AI Confidence: **99.48%**
122. **`hist/histpainter/src/TGraphPainter.cxx`** -> AI Confidence: **99.48%**
123. **`hist/histpainter/src/THistPainter.cxx`** -> AI Confidence: **99.48%**
124. **`hist/histpainter/src/TPainter3dAlgorithms.cxx`** -> AI Confidence: **99.48%**
125. **`hist/histpainter/src/TPaletteAxis.cxx`** -> AI Confidence: **99.48%**
126. **`hist/spectrumpainter/src/TSpectrum2Painter.cxx`** -> AI Confidence: **99.48%**
127. **`hist/unfold/src/TUnfold.cxx`** -> AI Confidence: **99.48%**
128. **`hist/unfold/src/TUnfoldBinning.cxx`** -> AI Confidence: **99.48%**
129. **`hist/unfold/src/TUnfoldBinningXML.cxx`** -> AI Confidence: **99.48%**
130. **`hist/unfold/src/TUnfoldDensity.cxx`** -> AI Confidence: **99.48%**
131. **`interpreter/cling/lib/Utils/Paths.cpp`** -> AI Confidence: **99.48%**
132. **`interpreter/llvm-project/clang/utils/TableGen/TableGen.cpp`** -> AI Confidence: **99.48%**
133. **`interpreter/llvm-project/llvm/include/llvm-c/DataTypes.h`** -> AI Confidence: **99.48%**
134. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/BuildLibCalls.cpp`** -> AI Confidence: **99.48%**
135. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/DemoteRegToStack.cpp`** -> AI Confidence: **99.48%**
136. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/LoopSimplify.cpp`** -> AI Confidence: **99.48%**
137. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/LoopUnrollRuntime.cpp`** -> AI Confidence: **99.48%**
138. **`interpreter/llvm-project/llvm/tools/bugpoint/OptimizerDriver.cpp`** -> AI Confidence: **99.48%**
139. **`interpreter/llvm-project/llvm/tools/llvm-ar/llvm-ar.cpp`** -> AI Confidence: **99.48%**
140. **`interpreter/llvm-project/llvm/tools/llvm-config/llvm-config.cpp`** -> AI Confidence: **99.48%**
141. **`interpreter/llvm-project/llvm/tools/llvm-mt/llvm-mt.cpp`** -> AI Confidence: **99.48%**
142. **`interpreter/llvm-project/llvm/tools/llvm-objdump/MachODump.cpp`** -> AI Confidence: **99.48%**
143. **`interpreter/llvm-project/llvm/tools/llvm-pdbutil/StreamUtil.cpp`** -> AI Confidence: **99.48%**
144. **`interpreter/llvm-project/llvm/tools/llvm-rc/llvm-rc.cpp`** -> AI Confidence: **99.48%**
145. **`interpreter/llvm-project/llvm/tools/llvm-size/llvm-size.cpp`** -> AI Confidence: **99.48%**
146. **`interpreter/llvm-project/llvm/tools/llvm-xray/xray-stacks.cpp`** -> AI Confidence: **99.48%**
147. **`interpreter/llvm-project/llvm/utils/TableGen/Basic/CodeGenIntrinsics.cpp`** -> AI Confidence: **99.48%**
148. **`interpreter/llvm-project/llvm/utils/TableGen/CodeEmitterGen.cpp`** -> AI Confidence: **99.48%**
149. **`interpreter/llvm-project/llvm/utils/TableGen/Common/CodeGenInstAlias.cpp`** -> AI Confidence: **99.48%**
150. **`interpreter/llvm-project/llvm/utils/TableGen/DAGISelMatcherGen.cpp`** -> AI Confidence: **99.48%**
151. **`interpreter/llvm-project/llvm/utils/TableGen/InstrDocsEmitter.cpp`** -> AI Confidence: **99.48%**
152. **`interpreter/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp`** -> AI Confidence: **99.48%**
153. **`io/io/src/TFileCacheRead.cxx`** -> AI Confidence: **99.48%**
154. **`io/io/src/TGenCollectionStreamer.cxx`** -> AI Confidence: **99.48%**
155. **`io/io/src/TKey.cxx`** -> AI Confidence: **99.48%**
156. **`io/io/src/TMakeProject.cxx`** -> AI Confidence: **99.48%**
157. **`io/io/src/TStreamerInfo.cxx`** -> AI Confidence: **99.48%**
158. **`io/io/src/TStreamerInfoReadBuffer.cxx`** -> AI Confidence: **99.48%**
159. **`io/io/src/TStreamerInfoWriteBuffer.cxx`** -> AI Confidence: **99.48%**
160. **`io/xml/src/TXMLPlayer.cxx`** -> AI Confidence: **99.48%**
161. **`main/src/h2root.cxx`** -> AI Confidence: **99.48%**
162. **`main/src/roots.cxx`** -> AI Confidence: **99.48%**
163. **`math/mathcore/src/RootFinder.cxx`** -> AI Confidence: **99.48%**
164. **`math/minuit/src/TLinearFitter.cxx`** -> AI Confidence: **99.48%**
165. **`math/minuit/src/TMinuit.cxx`** -> AI Confidence: **99.48%**
166. **`math/minuit2/src/FumiliBuilder.cxx`** -> AI Confidence: **99.48%**
167. **`math/minuit2/src/MnLineSearch.cxx`** -> AI Confidence: **99.48%**
168. **`math/minuit2/src/Numerical2PGradientCalculator.cxx`** -> AI Confidence: **99.48%**
169. **`math/minuit2/src/SimplexBuilder.cxx`** -> AI Confidence: **99.48%**
170. **`math/mlp/src/TMultiLayerPerceptron.cxx`** -> AI Confidence: **99.48%**
171. **`math/splot/src/TSPlot.cxx`** -> AI Confidence: **99.48%**
172. **`net/auth/src/TAuthenticate.cxx`** -> AI Confidence: **99.48%**
173. **`net/auth/src/THostAuth.cxx`** -> AI Confidence: **99.48%**
174. **`net/auth/src/TRootSecContext.cxx`** -> AI Confidence: **99.48%**
175. **`net/net/src/TApplicationRemote.cxx`** -> AI Confidence: **99.48%**
176. **`net/net/src/TApplicationServer.cxx`** -> AI Confidence: **99.48%**
177. **`net/net/src/TSQLMonitoring.cxx`** -> AI Confidence: **99.48%**
178. **`net/rpdutils/src/daemon.cxx`** -> AI Confidence: **99.48%**
179. **`net/rpdutils/src/rpdutils.cxx`** -> AI Confidence: **99.48%**
180. **`roofit/multiprocess/src/util.cxx`** -> AI Confidence: **99.48%**
181. **`roofit/roofit/src/RooIntegralMorph.cxx`** -> AI Confidence: **99.48%**
182. **`roofit/roofit/src/RooMomentMorphFuncND.cxx`** -> AI Confidence: **99.48%**
183. **`roofit/roofit/src/RooMultiBinomial.cxx`** -> AI Confidence: **99.48%**
184. **`roofit/roofit/src/RooNDKeysPdf.cxx`** -> AI Confidence: **99.48%**
185. **`roofit/roofitcore/src/RooAbsNumGenerator.cxx`** -> AI Confidence: **99.48%**
186. **`roofit/roofitcore/src/RooAcceptReject.cxx`** -> AI Confidence: **99.48%**
187. **`roofit/roofitcore/src/RooBinnedGenContext.cxx`** -> AI Confidence: **99.48%**
188. **`roofit/roofitcore/src/RooChi2Var.cxx`** -> AI Confidence: **99.48%**
189. **`roofit/roofitcore/src/RooCmdArg.cxx`** -> AI Confidence: **99.48%**
190. **`roofit/roofitcore/src/RooDataProjBinding.cxx`** -> AI Confidence: **99.48%**
191. **`roofit/roofitcore/src/RooDataSet.cxx`** -> AI Confidence: **99.48%**
192. **`roofit/roofitcore/src/RooFirstMoment.cxx`** -> AI Confidence: **99.48%**
193. **`roofit/roofitcore/src/RooGenContext.cxx`** -> AI Confidence: **99.48%**
194. **`roofit/roofitcore/src/RooMoment.cxx`** -> AI Confidence: **99.48%**
195. **`roofit/roofitcore/src/RooRealMPFE.cxx`** -> AI Confidence: **99.48%**
196. **`roofit/roofitcore/src/RooSecondMoment.cxx`** -> AI Confidence: **99.48%**
197. **`roofit/roofitcore/src/RooStreamParser.cxx`** -> AI Confidence: **99.48%**
198. **`roofit/roofitcore/src/RooUnitTest.cxx`** -> AI Confidence: **99.48%**
199. **`roofit/roofitcore/src/TestStatistics/RooBinnedL.cxx`** -> AI Confidence: **99.48%**
200. **`roofit/roostats/src/AsymptoticCalculator.cxx`** -> AI Confidence: **99.48%**
201. **`roofit/roostats/src/HypoTestInverterPlot.cxx`** -> AI Confidence: **99.48%**
202. **`roofit/roostats/src/LikelihoodIntervalPlot.cxx`** -> AI Confidence: **99.48%**
203. **`roofit/roostats/src/ProfileLikelihoodTestStat.cxx`** -> AI Confidence: **99.48%**
204. **`roottest/scripts/analyze_valgrind.cxx`** -> AI Confidence: **99.48%**
205. **`tmva/sofie/inc/TMVA/ROperator_Concat.hxx`** -> AI Confidence: **99.48%**
206. **`tmva/sofie/inc/TMVA/ROperator_Conv.hxx`** -> AI Confidence: **99.48%**
207. **`tmva/sofie/inc/TMVA/ROperator_Gemm.hxx`** -> AI Confidence: **99.48%**
208. **`tmva/sofie/inc/TMVA/ROperator_Pool.hxx`** -> AI Confidence: **99.48%**
209. **`tmva/tmva/src/CCPruner.cxx`** -> AI Confidence: **99.48%**
210. **`tmva/tmva/src/Configurable.cxx`** -> AI Confidence: **99.48%**
211. **`tmva/tmva/src/DataSetFactory.cxx`** -> AI Confidence: **99.48%**
212. **`tmva/tmva/src/DecisionTree.cxx`** -> AI Confidence: **99.48%**
213. **`tmva/tmva/src/GeneticFitter.cxx`** -> AI Confidence: **99.48%**
214. **`tmva/tmva/src/MCFitter.cxx`** -> AI Confidence: **99.48%**
215. **`tmva/tmva/src/MethodBDT.cxx`** -> AI Confidence: **99.48%**
216. **`tmva/tmva/src/MethodCFMlpANN_Utils.cxx`** -> AI Confidence: **99.48%**
217. **`tmva/tmva/src/MethodCuts.cxx`** -> AI Confidence: **99.48%**
218. **`tmva/tmva/src/MethodLikelihood.cxx`** -> AI Confidence: **99.48%**
219. **`tmva/tmva/src/MethodMLP.cxx`** -> AI Confidence: **99.48%**
220. **`tmva/tmva/src/MethodPDEFoam.cxx`** -> AI Confidence: **99.48%**
221. **`tmva/tmva/src/MethodSVM.cxx`** -> AI Confidence: **99.48%**
222. **`tmva/tmva/src/OptimizeConfigParameters.cxx`** -> AI Confidence: **99.48%**
223. **`tmva/tmva/src/PDEFoam.cxx`** -> AI Confidence: **99.48%**
224. **`tmva/tmva/src/PDEFoamDecisionTree.cxx`** -> AI Confidence: **99.48%**
225. **`tmva/tmva/src/PDEFoamDecisionTreeDensity.cxx`** -> AI Confidence: **99.48%**
226. **`tmva/tmva/src/PDEFoamDiscriminant.cxx`** -> AI Confidence: **99.48%**
227. **`tmva/tmva/src/PDEFoamDiscriminantDensity.cxx`** -> AI Confidence: **99.48%**
228. **`tmva/tmva/src/PDEFoamKernelGauss.cxx`** -> AI Confidence: **99.48%**
229. **`tmva/tmva/src/PDEFoamKernelLinN.cxx`** -> AI Confidence: **99.48%**
230. **`tmva/tmva/src/PDEFoamMultiTarget.cxx`** -> AI Confidence: **99.48%**
231. **`tmva/tmva/src/PDF.cxx`** -> AI Confidence: **99.48%**
232. **`tmva/tmva/src/ROCCalc.cxx`** -> AI Confidence: **99.48%**
233. **`tmva/tmva/src/ResultsRegression.cxx`** -> AI Confidence: **99.48%**
234. **`tmva/tmva/src/RuleFitParams.cxx`** -> AI Confidence: **99.48%**
235. **`tmva/tmva/src/SVWorkingSet.cxx`** -> AI Confidence: **99.48%**
236. **`tmva/tmva/src/SimulatedAnnealing.cxx`** -> AI Confidence: **99.48%**
237. **`tmva/tmva/src/VarTransformHandler.cxx`** -> AI Confidence: **99.48%**
238. **`tmva/tmva/src/VariableGaussTransform.cxx`** -> AI Confidence: **99.48%**
239. **`tmva/tmva/src/VariableImportance.cxx`** -> AI Confidence: **99.48%**
240. **`tmva/tmva/src/VariableNormalizeTransform.cxx`** -> AI Confidence: **99.48%**
241. **`tmva/tmva/src/VariablePCATransform.cxx`** -> AI Confidence: **99.48%**
242. **`tmva/tmva/src/VariableTransform.cxx`** -> AI Confidence: **99.48%**
243. **`tmva/tmva/src/VariableTransformBase.cxx`** -> AI Confidence: **99.48%**
244. **`tmva/tmvagui/src/MovieMaker.cxx`** -> AI Confidence: **99.48%**
245. **`tmva/tmvagui/src/PlotFoams.cxx`** -> AI Confidence: **99.48%**
246. **`tmva/tmvagui/src/TMVAGui.cxx`** -> AI Confidence: **99.48%**
247. **`tmva/tmvagui/src/TMVAMultiClassGui.cxx`** -> AI Confidence: **99.48%**
248. **`tmva/tmvagui/src/network.cxx`** -> AI Confidence: **99.48%**
249. **`tmva/tmvagui/src/paracoor.cxx`** -> AI Confidence: **99.48%**
250. **`tmva/tmvagui/src/probas.cxx`** -> AI Confidence: **99.48%**
251. **`tree/tree/src/TBasket.cxx`** -> AI Confidence: **99.48%**
252. **`tree/tree/src/TBranchBrowsable.cxx`** -> AI Confidence: **99.48%**
253. **`tree/tree/src/TBranchClones.cxx`** -> AI Confidence: **99.48%**
254. **`tree/tree/src/TBranchElement.cxx`** -> AI Confidence: **99.48%**
255. **`tree/tree/src/TEntryList.cxx`** -> AI Confidence: **99.48%**
256. **`tree/tree/src/TTreeCache.cxx`** -> AI Confidence: **99.48%**
257. **`tree/tree/src/TTreeCacheUnzip.cxx`** -> AI Confidence: **99.48%**
258. **`tree/tree/src/TTreeCloner.cxx`** -> AI Confidence: **99.48%**
259. **`tree/treeplayer/src/TSelectorDraw.cxx`** -> AI Confidence: **99.48%**
260. **`tree/treeplayer/src/TTreeFormula.cxx`** -> AI Confidence: **99.48%**
261. **`tree/treeplayer/src/TTreeGeneratorBase.cxx`** -> AI Confidence: **99.48%**
262. **`tree/treeplayer/src/TTreePlayer.cxx`** -> AI Confidence: **99.48%**
263. **`tree/treeplayer/src/TTreeProxyGenerator.cxx`** -> AI Confidence: **99.48%**
264. **`tree/treeplayer/src/TTreeReaderGenerator.cxx`** -> AI Confidence: **99.48%**
265. **`tree/treeviewer/src/TParallelCoordRange.cxx`** -> AI Confidence: **99.48%**
266. **`tree/treeviewer/src/TParallelCoordVar.cxx`** -> AI Confidence: **99.48%**
267. **`tree/treeviewer/src/TSpider.cxx`** -> AI Confidence: **99.48%**
268. **`builtins/glew/src/glew.c`** -> AI Confidence: **99.48%**
269. **`graf2d/asimage/src/libAfterImage/afterbase.h`** -> AI Confidence: **99.48%**
270. **`graf2d/asimage/src/libAfterImage/ascmap.c`** -> AI Confidence: **99.48%**
271. **`graf2d/asimage/src/libAfterImage/asfont.c`** -> AI Confidence: **99.48%**
272. **`graf2d/asimage/src/libAfterImage/asimage.c`** -> AI Confidence: **99.48%**
273. **`graf2d/asimage/src/libAfterImage/asstorage.c`** -> AI Confidence: **99.48%**
274. **`graf2d/asimage/src/libAfterImage/asvisual.c`** -> AI Confidence: **99.48%**
275. **`graf2d/asimage/src/libAfterImage/blender.c`** -> AI Confidence: **99.48%**
276. **`graf2d/asimage/src/libAfterImage/bmp.c`** -> AI Confidence: **99.48%**
277. **`graf2d/asimage/src/libAfterImage/draw.c`** -> AI Confidence: **99.48%**
278. **`graf2d/asimage/src/libAfterImage/export.c`** -> AI Confidence: **99.48%**
279. **`graf2d/asimage/src/libAfterImage/imencdec.c`** -> AI Confidence: **99.48%**
280. **`graf2d/asimage/src/libAfterImage/import.c`** -> AI Confidence: **99.48%**
281. **`graf2d/asimage/src/libAfterImage/scanline.c`** -> AI Confidence: **99.48%**
282. **`graf2d/asimage/src/libAfterImage/test_mmx.c`** -> AI Confidence: **99.48%**
283. **`graf2d/asimage/src/libAfterImage/transform.c`** -> AI Confidence: **99.48%**
284. **`graf2d/asimage/src/libAfterImage/ungif.c`** -> AI Confidence: **99.48%**
285. **`graf2d/asimage/src/libAfterImage/xcf.c`** -> AI Confidence: **99.48%**
286. **`graf2d/asimage/src/libAfterImage/ximage.c`** -> AI Confidence: **99.48%**
287. **`graf2d/asimage/src/libAfterImage/xpm.c`** -> AI Confidence: **99.48%**
288. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkdrawable-win32.c`** -> AI Confidence: **99.48%**
289. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkevents-win32.c`** -> AI Confidence: **99.48%**
290. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkgc-win32.c`** -> AI Confidence: **99.48%**
291. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkinput-win32.c`** -> AI Confidence: **99.48%**
292. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkwindow-win32.c`** -> AI Confidence: **99.48%**
293. **`graf2d/win32gdk/gdk/src/glib/gbacktrace.c`** -> AI Confidence: **99.48%**
294. **`graf2d/win32gdk/gdk/src/glib/gconvert.c`** -> AI Confidence: **99.48%**
295. **`graf2d/win32gdk/gdk/src/glib/giochannel.c`** -> AI Confidence: **99.48%**
296. **`graf2d/win32gdk/gdk/src/glib/gmessages.c`** -> AI Confidence: **99.48%**
297. **`graf2d/win32gdk/gdk/src/glib/gscanner.c`** -> AI Confidence: **99.48%**
298. **`graf2d/win32gdk/gdk/src/glib/gspawn-win32.c`** -> AI Confidence: **99.48%**
299. **`graf2d/win32gdk/gdk/src/glib/gspawn.c`** -> AI Confidence: **99.48%**
300. **`graf2d/win32gdk/gdk/src/glib/gutf8.c`** -> AI Confidence: **99.48%**
301. **`graf2d/win32gdk/gdk/src/iconv/localcharset.c`** -> AI Confidence: **99.48%**
302. **`graf3d/eve7/glu/normal.c`** -> AI Confidence: **99.48%**
303. **`graf3d/x3d/src/x3d.c`** -> AI Confidence: **99.48%**
304. **`interpreter/llvm-project/llvm/examples/OrcV2Examples/OrcV2CBindingsLazy/OrcV2CBindingsLazy.c`** -> AI Confidence: **99.48%**
305. **`tutorials/analysis/unfold/testUnfold1.C`** -> AI Confidence: **99.48%**
306. **`tutorials/analysis/unfold/testUnfold3.C`** -> AI Confidence: **99.48%**
307. **`tutorials/analysis/unfold/testUnfold5c.C`** -> AI Confidence: **99.48%**
308. **`tutorials/analysis/unfold/testUnfold5d.C`** -> AI Confidence: **99.48%**
309. **`tutorials/analysis/unfold/testUnfold7b.C`** -> AI Confidence: **99.48%**
310. **`tutorials/analysis/unfold/testUnfold7c.C`** -> AI Confidence: **99.48%**
311. **`tutorials/hist/hist101_TH1_autobinning.C`** -> AI Confidence: **99.48%**
312. **`tutorials/hist/hist103_THnSparse_hist.C`** -> AI Confidence: **99.48%**
313. **`tutorials/http/httpserver.C`** -> AI Confidence: **99.48%**
314. **`tutorials/io/hadd.C`** -> AI Confidence: **99.48%**
315. **`tutorials/legacy/net/parallelMergeClient.C`** -> AI Confidence: **99.48%**
316. **`tutorials/legacy/net/spyserv.C`** -> AI Confidence: **99.48%**
317. **`tutorials/legacy/net/treeClient.C`** -> AI Confidence: **99.48%**
318. **`tutorials/legacy/spectrum/peaks2.C`** -> AI Confidence: **99.48%**
319. **`tutorials/machine_learning/TMVAClassificationApplication.C`** -> AI Confidence: **99.48%**
320. **`tutorials/machine_learning/TMVAClassificationCategoryApplication.C`** -> AI Confidence: **99.48%**
321. **`tutorials/machine_learning/TMVACrossValidation.C`** -> AI Confidence: **99.48%**
322. **`tutorials/machine_learning/TMVACrossValidationApplication.C`** -> AI Confidence: **99.48%**
323. **`tutorials/machine_learning/TMVAMulticlass.C`** -> AI Confidence: **99.48%**
324. **`tutorials/machine_learning/TMVAMulticlassApplication.C`** -> AI Confidence: **99.48%**
325. **`tutorials/machine_learning/TMVAMultipleBackgroundExample.C`** -> AI Confidence: **99.48%**
326. **`tutorials/machine_learning/TMVARegressionApplication.C`** -> AI Confidence: **99.48%**
327. **`tutorials/machine_learning/createData.C`** -> AI Confidence: **99.48%**
328. **`tutorials/math/LegendreAssoc.C`** -> AI Confidence: **99.48%**
329. **`tutorials/math/foam/foam_demo.C`** -> AI Confidence: **99.48%**
330. **`tutorials/math/kdTreeBinning.C`** -> AI Confidence: **99.48%**
331. **`tutorials/math/testrandom.C`** -> AI Confidence: **99.48%**
332. **`tutorials/roofit/roofit/rf708_bphysics.C`** -> AI Confidence: **99.48%**
333. **`tutorials/roofit/roostats/FourBinInstructional.C`** -> AI Confidence: **99.48%**
334. **`tutorials/roofit/roostats/OneSidedFrequentistUpperLimitWithBands.C`** -> AI Confidence: **99.48%**
335. **`tutorials/roofit/roostats/TwoSidedFrequentistUpperLimitWithBands.C`** -> AI Confidence: **99.48%**
336. **`tutorials/roofit/roostats/rs401c_FeldmanCousins.C`** -> AI Confidence: **99.48%**
337. **`tutorials/visualisation/graphs/gr018_time2.C`** -> AI Confidence: **99.48%**
338. **`core/macosx/src/TMacOSXSystem.mm`** -> AI Confidence: **99.48%**
339. **`graf2d/cocoa/src/CocoaPrivate.mm`** -> AI Confidence: **99.48%**
340. **`graf2d/cocoa/src/FontCache.mm`** -> AI Confidence: **99.48%**
341. **`graf2d/cocoa/src/QuartzPixmap.mm`** -> AI Confidence: **99.48%**
342. **`graf2d/cocoa/src/QuartzWindow.mm`** -> AI Confidence: **99.48%**
343. **`graf2d/cocoa/src/TGCocoa.mm`** -> AI Confidence: **99.48%**
344. **`graf2d/cocoa/src/TGOSXGL.mm`** -> AI Confidence: **99.48%**
345. **`graf2d/cocoa/src/TGQuartz.mm`** -> AI Confidence: **99.48%**
346. **`graf2d/cocoa/src/X11Buffer.mm`** -> AI Confidence: **99.48%**
347. **`graf2d/cocoa/src/X11Events.mm`** -> AI Confidence: **99.48%**
348. **`graf2d/quartz/src/QuartzFillArea.mm`** -> AI Confidence: **99.48%**
349. **`graf2d/quartz/src/QuartzLine.mm`** -> AI Confidence: **99.48%**
350. **`graf2d/quartz/src/QuartzText.mm`** -> AI Confidence: **99.48%**
351. **`misc/rootql/ReadFile.m`** -> AI Confidence: **99.48%**
352. **`misc/rootsl/ReadFile.m`** -> AI Confidence: **99.48%**
353. **`js/modules/gui.mjs`** -> AI Confidence: **99.48%**
354. **`js/modules/hist2d/THistPainter.mjs`** -> AI Confidence: **99.48%**
355. **`core/zip/src/Tailor.h`** -> AI Confidence: **99.44%**
356. **`core/foundation/res/TSchemaRuleProcessor.h`** -> AI Confidence: **99.43%**
357. **`roofit/histfactory/src/ConfigParser.cxx`** -> AI Confidence: **99.43%**
358. **`graf2d/asimage/src/libAfterImage/zlib/zutil.h`** -> AI Confidence: **99.43%**
359. **`bindings/pyroot/cppyy/CPyCppyy/src/ProxyWrappers.cxx`** -> AI Confidence: **99.39%**
360. **`bindings/pyroot/cppyy/CPyCppyy/src/TemplateProxy.cxx`** -> AI Confidence: **99.39%**
361. **`bindings/pyroot/pythonizations/src/RPyROOTApplication.cxx`** -> AI Confidence: **99.39%**
362. **`core/base/src/TEnv.cxx`** -> AI Confidence: **99.39%**
363. **`core/base/src/TFileInfo.cxx`** -> AI Confidence: **99.39%**
364. **`core/clingutils/src/RStl.cxx`** -> AI Confidence: **99.39%**
365. **`core/dictgen/src/LinkdefReader.cxx`** -> AI Confidence: **99.39%**
366. **`core/meta/src/TMethod.cxx`** -> AI Confidence: **99.39%**
367. **`core/meta/src/TProtoClass.cxx`** -> AI Confidence: **99.39%**
368. **`core/meta/src/TSchemaRule.cxx`** -> AI Confidence: **99.39%**
369. **`core/meta/src/TStreamerElement.cxx`** -> AI Confidence: **99.39%**
370. **`core/rint/src/TRint.cxx`** -> AI Confidence: **99.39%**
371. **`core/rint/src/TTabCom.cxx`** -> AI Confidence: **99.39%**
372. **`core/unix/src/TUnixSystem.cxx`** -> AI Confidence: **99.39%**
373. **`geom/geom/src/TGeoArb8.cxx`** -> AI Confidence: **99.39%**
374. **`geom/geom/src/TGeoBuilder.cxx`** -> AI Confidence: **99.39%**
375. **`geom/geom/src/TGeoElement.cxx`** -> AI Confidence: **99.39%**
376. **`geom/geom/src/TGeoNavigator.cxx`** -> AI Confidence: **99.39%**
377. **`geom/geom/src/TGeoPcon.cxx`** -> AI Confidence: **99.39%**
378. **`geom/geom/src/TGeoPgon.cxx`** -> AI Confidence: **99.39%**
379. **`geom/geom/src/TGeoShapeAssembly.cxx`** -> AI Confidence: **99.39%**
380. **`geom/geom/src/TGeoTorus.cxx`** -> AI Confidence: **99.39%**
381. **`geom/geom/src/TGeoVolume.cxx`** -> AI Confidence: **99.39%**
382. **`geom/geombuilder/src/TGeoHypeEditor.cxx`** -> AI Confidence: **99.39%**
383. **`geom/geombuilder/src/TGeoSphereEditor.cxx`** -> AI Confidence: **99.39%**
384. **`geom/geompainter/src/TGeoPainter.cxx`** -> AI Confidence: **99.39%**
385. **`geom/geompainter/src/TGeoTrack.cxx`** -> AI Confidence: **99.39%**
386. **`geom/webviewer/src/RGeomViewer.cxx`** -> AI Confidence: **99.39%**
387. **`graf2d/asimage/src/TASPluginGS.cxx`** -> AI Confidence: **99.39%**
388. **`graf2d/gpad/src/TCanvas.cxx`** -> AI Confidence: **99.39%**
389. **`graf2d/gpad/src/TRatioPlot.cxx`** -> AI Confidence: **99.39%**
390. **`graf2d/graf/src/TAttImage.cxx`** -> AI Confidence: **99.39%**
391. **`graf2d/graf/src/TCutG.cxx`** -> AI Confidence: **99.39%**
392. **`graf2d/graf/src/TEllipse.cxx`** -> AI Confidence: **99.39%**
393. **`graf2d/graf/src/TLine.cxx`** -> AI Confidence: **99.39%**
394. **`graf2d/graf/src/TPave.cxx`** -> AI Confidence: **99.39%**
395. **`graf2d/graf/src/TPaveStats.cxx`** -> AI Confidence: **99.39%**
396. **`graf2d/graf/src/TPaveText.cxx`** -> AI Confidence: **99.39%**
397. **`graf2d/graf/src/TPie.cxx`** -> AI Confidence: **99.39%**
398. **`graf2d/graf/src/TPolyLine.cxx`** -> AI Confidence: **99.39%**
399. **`graf2d/win32gdk/src/TGWin32.cxx`** -> AI Confidence: **99.39%**
400. **`graf3d/eve/src/TEveCalo3DGL.cxx`** -> AI Confidence: **99.39%**
401. **`graf3d/eve/src/TEveGeoPolyShape.cxx`** -> AI Confidence: **99.39%**
402. **`graf3d/eve/src/TEveProjectionAxesGL.cxx`** -> AI Confidence: **99.39%**
403. **`graf3d/eve/src/TEveTrackPropagatorEditor.cxx`** -> AI Confidence: **99.39%**
404. **`graf3d/eve7/src/REvePolygonSetProjected.cxx`** -> AI Confidence: **99.39%**
405. **`graf3d/g3d/src/TNode.cxx`** -> AI Confidence: **99.39%**
406. **`graf3d/g3d/src/TPCON.cxx`** -> AI Confidence: **99.39%**
407. **`graf3d/g3d/src/TTUBE.cxx`** -> AI Confidence: **99.39%**
408. **`graf3d/g3d/src/TView3D.cxx`** -> AI Confidence: **99.39%**
409. **`graf3d/gl/src/TGL5DPainter.cxx`** -> AI Confidence: **99.39%**
410. **`graf3d/gl/src/TGLAnnotation.cxx`** -> AI Confidence: **99.39%**
411. **`graf3d/gl/src/TGLOutput.cxx`** -> AI Confidence: **99.39%**
412. **`graf3d/gl/src/TGLPhysicalShape.cxx`** -> AI Confidence: **99.39%**
413. **`graf3d/gl/src/TGLSceneBase.cxx`** -> AI Confidence: **99.39%**
414. **`graf3d/gl/src/TGLScenePad.cxx`** -> AI Confidence: **99.39%**
415. **`graf3d/gl/src/TGLSphere.cxx`** -> AI Confidence: **99.39%**
416. **`graf3d/gl/src/TGLTF3Painter.cxx`** -> AI Confidence: **99.39%**
417. **`graf3d/gl/src/TGLTH3Composition.cxx`** -> AI Confidence: **99.39%**
418. **`graf3d/gl/src/TH3GL.cxx`** -> AI Confidence: **99.39%**
419. **`gui/cefdisplay/src/RCefWebDisplayHandle.cxx`** -> AI Confidence: **99.39%**
420. **`gui/ged/src/TFrameEditor.cxx`** -> AI Confidence: **99.39%**
421. **`gui/ged/src/TGedEditor.cxx`** -> AI Confidence: **99.39%**
422. **`gui/ged/src/TPieEditor.cxx`** -> AI Confidence: **99.39%**
423. **`gui/gui/src/TGCanvas.cxx`** -> AI Confidence: **99.39%**
424. **`gui/gui/src/TGComboBox.cxx`** -> AI Confidence: **99.39%**
425. **`gui/gui/src/TGDockableFrame.cxx`** -> AI Confidence: **99.39%**
426. **`gui/gui/src/TGFSContainer.cxx`** -> AI Confidence: **99.39%**
427. **`gui/gui/src/TGFrame.cxx`** -> AI Confidence: **99.39%**
428. **`gui/gui/src/TGListBox.cxx`** -> AI Confidence: **99.39%**
429. **`gui/gui/src/TGListTree.cxx`** -> AI Confidence: **99.39%**
430. **`gui/gui/src/TGMdiDecorFrame.cxx`** -> AI Confidence: **99.39%**
431. **`gui/gui/src/TGMdiMainFrame.cxx`** -> AI Confidence: **99.39%**
432. **`gui/gui/src/TGMenu.cxx`** -> AI Confidence: **99.39%**
433. **`gui/gui/src/TGRedirectOutputGuard.cxx`** -> AI Confidence: **99.39%**
434. **`gui/gui/src/TGScrollBar.cxx`** -> AI Confidence: **99.39%**
435. **`gui/gui/src/TGTab.cxx`** -> AI Confidence: **99.39%**
436. **`gui/gui/src/TGTableHeader.cxx`** -> AI Confidence: **99.39%**
437. **`gui/gui/src/TGTextEntry.cxx`** -> AI Confidence: **99.39%**
438. **`gui/gui/src/TGTextView.cxx`** -> AI Confidence: **99.39%**
439. **`gui/gui/src/TGToolTip.cxx`** -> AI Confidence: **99.39%**
440. **`gui/gui/src/TRootBrowserLite.cxx`** -> AI Confidence: **99.39%**
441. **`gui/gui/src/TRootEmbeddedCanvas.cxx`** -> AI Confidence: **99.39%**
442. **`gui/guibuilder/src/TGuiBldDragManager.cxx`** -> AI Confidence: **99.39%**
443. **`gui/guibuilder/src/TGuiBldEditor.cxx`** -> AI Confidence: **99.39%**
444. **`gui/guibuilder/src/TGuiBldGeometryFrame.cxx`** -> AI Confidence: **99.39%**
445. **`gui/guibuilder/src/TGuiBldHintsEditor.cxx`** -> AI Confidence: **99.39%**
446. **`gui/guibuilder/src/TGuiBldNameFrame.cxx`** -> AI Confidence: **99.39%**
447. **`gui/guibuilder/src/TRootGuiBuilder.cxx`** -> AI Confidence: **99.39%**
448. **`gui/guihtml/src/TGHtml.cxx`** -> AI Confidence: **99.39%**
449. **`gui/guihtml/src/TGHtmlImage.cxx`** -> AI Confidence: **99.39%**
450. **`gui/qt6webdisplay/rootqt6.cpp`** -> AI Confidence: **99.39%**
451. **`gui/recorder/src/TRecorder.cxx`** -> AI Confidence: **99.39%**
452. **`gui/webdisplay/src/RWebDisplayHandle.cxx`** -> AI Confidence: **99.39%**
453. **`gui/webdisplay/src/RWebWindowsManager.cxx`** -> AI Confidence: **99.39%**
454. **`gui/webgui6/src/TWebCanvas.cxx`** -> AI Confidence: **99.39%**
455. **`hist/hist/src/TEfficiency.cxx`** -> AI Confidence: **99.39%**
456. **`hist/hist/src/TF1.cxx`** -> AI Confidence: **99.39%**
457. **`hist/hist/src/TF1Convolution.cxx`** -> AI Confidence: **99.39%**
458. **`hist/hist/src/TFractionFitter.cxx`** -> AI Confidence: **99.39%**
459. **`hist/hist/src/TGraph.cxx`** -> AI Confidence: **99.39%**
460. **`hist/hist/src/TGraph2DAsymmErrors.cxx`** -> AI Confidence: **99.39%**
461. **`hist/hist/src/TGraph2DErrors.cxx`** -> AI Confidence: **99.39%**
462. **`hist/hist/src/TGraphMultiErrors.cxx`** -> AI Confidence: **99.39%**
463. **`hist/hist/src/TH1.cxx`** -> AI Confidence: **99.39%**
464. **`hist/hist/src/TH2.cxx`** -> AI Confidence: **99.39%**
465. **`hist/hist/src/TH2Poly.cxx`** -> AI Confidence: **99.39%**
466. **`hist/hist/src/TKDE.cxx`** -> AI Confidence: **99.39%**
467. **`hist/hist/src/TProfile.cxx`** -> AI Confidence: **99.39%**
468. **`hist/hist/src/TProfile3D.cxx`** -> AI Confidence: **99.39%**
469. **`hist/unfold/src/TUnfoldSys.cxx`** -> AI Confidence: **99.39%**
470. **`interpreter/llvm-project/clang/include/clang/Sema/SemaOpenACC.h`** -> AI Confidence: **99.39%**
471. **`interpreter/llvm-project/clang/tools/clang-linker-wrapper/ClangLinkerWrapper.cpp`** -> AI Confidence: **99.39%**
472. **`interpreter/llvm-project/clang/tools/libclang/CIndexer.cpp`** -> AI Confidence: **99.39%**
473. **`interpreter/llvm-project/clang/tools/libclang/CXCursor.cpp`** -> AI Confidence: **99.39%**
474. **`interpreter/llvm-project/llvm/examples/BrainF/BrainFDriver.cpp`** -> AI Confidence: **99.39%**
475. **`interpreter/llvm-project/llvm/include/llvm/Analysis/DominanceFrontierImpl.h`** -> AI Confidence: **99.39%**
476. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/CodeExtractor.cpp`** -> AI Confidence: **99.39%**
477. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/GlobalStatus.cpp`** -> AI Confidence: **99.39%**
478. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/LCSSA.cpp`** -> AI Confidence: **99.39%**
479. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/LibCallsShrinkWrap.cpp`** -> AI Confidence: **99.39%**
480. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/LoopRotationUtils.cpp`** -> AI Confidence: **99.39%**
481. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/SSAUpdaterBulk.cpp`** -> AI Confidence: **99.39%**
482. **`interpreter/llvm-project/llvm/tools/bugpoint/ExecutionDriver.cpp`** -> AI Confidence: **99.39%**
483. **`interpreter/llvm-project/llvm/tools/llvm-c-test/echo.cpp`** -> AI Confidence: **99.39%**
484. **`interpreter/llvm-project/llvm/tools/llvm-cfi-verify/llvm-cfi-verify.cpp`** -> AI Confidence: **99.39%**
485. **`interpreter/llvm-project/llvm/tools/llvm-exegesis/lib/X86/Target.cpp`** -> AI Confidence: **99.39%**
486. **`interpreter/llvm-project/llvm/tools/llvm-mc-assemble-fuzzer/llvm-mc-assemble-fuzzer.cpp`** -> AI Confidence: **99.39%**
487. **`interpreter/llvm-project/llvm/tools/llvm-ml/Disassembler.cpp`** -> AI Confidence: **99.39%**
488. **`interpreter/llvm-project/llvm/tools/llvm-nm/llvm-nm.cpp`** -> AI Confidence: **99.39%**
489. **`interpreter/llvm-project/llvm/tools/llvm-objdump/llvm-objdump.cpp`** -> AI Confidence: **99.39%**
490. **`interpreter/llvm-project/llvm/tools/llvm-readobj/llvm-readobj.cpp`** -> AI Confidence: **99.39%**
491. **`interpreter/llvm-project/llvm/tools/llvm-reduce/ReducerWorkItem.cpp`** -> AI Confidence: **99.39%**
492. **`interpreter/llvm-project/llvm/tools/llvm-undname/llvm-undname.cpp`** -> AI Confidence: **99.39%**
493. **`interpreter/llvm-project/llvm/tools/obj2yaml/dwarf2yaml.cpp`** -> AI Confidence: **99.39%**
494. **`interpreter/llvm-project/llvm/tools/opt/optdriver.cpp`** -> AI Confidence: **99.39%**
495. **`interpreter/llvm-project/llvm/utils/TableGen/AsmWriterEmitter.cpp`** -> AI Confidence: **99.39%**
496. **`interpreter/llvm-project/llvm/utils/TableGen/CompressInstEmitter.cpp`** -> AI Confidence: **99.39%**
497. **`interpreter/llvm-project/llvm/utils/split-file/split-file.cpp`** -> AI Confidence: **99.39%**
498. **`interpreter/llvm-project/llvm/utils/yaml-bench/YAMLBench.cpp`** -> AI Confidence: **99.39%**
499. **`io/io/src/TDirectoryFile.cxx`** -> AI Confidence: **99.39%**
500. **`io/io/src/TEmulatedCollectionProxy.cxx`** -> AI Confidence: **99.39%**
501. **`io/io/src/TFile.cxx`** -> AI Confidence: **99.39%**
502. **`io/io/src/TFileMerger.cxx`** -> AI Confidence: **99.39%**
503. **`io/io/src/TMapFile.cxx`** -> AI Confidence: **99.39%**
504. **`io/io/src/TMemFile.cxx`** -> AI Confidence: **99.39%**
505. **`io/xml/src/TXMLFile.cxx`** -> AI Confidence: **99.39%**
506. **`math/fumili/src/TFumili.cxx`** -> AI Confidence: **99.39%**
507. **`math/fumili/src/TFumiliMinimizer.cxx`** -> AI Confidence: **99.39%**
508. **`math/mathcore/inc/Math/LFSR.h`** -> AI Confidence: **99.39%**
509. **`math/mathcore/src/Factory.cxx`** -> AI Confidence: **99.39%**
510. **`math/mathcore/src/FitResult.cxx`** -> AI Confidence: **99.39%**
511. **`math/mathcore/src/GoFTest.cxx`** -> AI Confidence: **99.39%**
512. **`math/mathmore/src/GSLMinimizer.cxx`** -> AI Confidence: **99.39%**
513. **`math/mathmore/src/VavilovFast.cxx`** -> AI Confidence: **99.39%**
514. **`math/minuit2/src/InitialGradientCalculator.cxx`** -> AI Confidence: **99.39%**
515. **`math/minuit2/src/MnContours.cxx`** -> AI Confidence: **99.39%**
516. **`math/minuit2/src/MnHesse.cxx`** -> AI Confidence: **99.39%**
517. **`math/minuit2/src/MnMinos.cxx`** -> AI Confidence: **99.39%**
518. **`math/minuit2/src/VariableMetricBuilder.cxx`** -> AI Confidence: **99.39%**
519. **`math/mlp/src/TMLPAnalyzer.cxx`** -> AI Confidence: **99.39%**
520. **`math/unuran/src/TUnuranContDist.cxx`** -> AI Confidence: **99.39%**
521. **`montecarlo/eg/src/TGenerator.cxx`** -> AI Confidence: **99.39%**
522. **`net/auth/src/TRootAuth.cxx`** -> AI Confidence: **99.39%**
523. **`net/auth/src/rsaaux.cxx`** -> AI Confidence: **99.39%**
524. **`net/auth/src/rsalib.cxx`** -> AI Confidence: **99.39%**
525. **`net/http/src/TFastCgi.cxx`** -> AI Confidence: **99.39%**
526. **`net/http/src/THttpServer.cxx`** -> AI Confidence: **99.39%**
527. **`net/httpsniff/src/TRootSnifferFull.cxx`** -> AI Confidence: **99.39%**
528. **`net/net/src/TFTP.cxx`** -> AI Confidence: **99.39%**
529. **`net/net/src/TFileStager.cxx`** -> AI Confidence: **99.39%**
530. **`net/net/src/TMessage.cxx`** -> AI Confidence: **99.39%**
531. **`net/net/src/TPSocket.cxx`** -> AI Confidence: **99.39%**
532. **`net/net/src/TSecContext.cxx`** -> AI Confidence: **99.39%**
533. **`net/net/src/TSocket.cxx`** -> AI Confidence: **99.39%**
534. **`net/net/src/TWebFile.cxx`** -> AI Confidence: **99.39%**
535. **`net/netxng/src/TNetXNGFile.cxx`** -> AI Confidence: **99.39%**
536. **`roofit/batchcompute/src/ComputeFunctions.cxx`** -> AI Confidence: **99.39%**
537. **`roofit/histfactory/src/HistFactoryModelUtils.cxx`** -> AI Confidence: **99.39%**
538. **`roofit/multiprocess/src/ProcessManager.cxx`** -> AI Confidence: **99.39%**
539. **`roofit/multiprocess/src/worker.cxx`** -> AI Confidence: **99.39%**
540. **`roofit/roofit/src/RooBMixDecay.cxx`** -> AI Confidence: **99.39%**
541. **`roofit/roofit/src/RooKeysPdf.cxx`** -> AI Confidence: **99.39%**
542. **`roofit/roofit/src/RooLagrangianMorphFunc.cxx`** -> AI Confidence: **99.39%**
543. **`roofit/roofit/src/RooMomentMorph.cxx`** -> AI Confidence: **99.39%**
544. **`roofit/roofit/src/RooMomentMorphFunc.cxx`** -> AI Confidence: **99.39%**
545. **`roofit/roofitcore/src/RooAbsData.cxx`** -> AI Confidence: **99.39%**
546. **`roofit/roofitcore/src/RooAbsMinimizerFcn.cxx`** -> AI Confidence: **99.39%**
547. **`roofit/roofitcore/src/RooAbsOptTestStatistic.cxx`** -> AI Confidence: **99.39%**
548. **`roofit/roofitcore/src/RooAbsRealLValue.cxx`** -> AI Confidence: **99.39%**
549. **`roofit/roofitcore/src/RooAbsTestStatistic.cxx`** -> AI Confidence: **99.39%**
550. **`roofit/roofitcore/src/RooAdaptiveIntegratorND.cxx`** -> AI Confidence: **99.39%**
551. **`roofit/roofitcore/src/RooAddHelpers.cxx`** -> AI Confidence: **99.39%**
552. **`roofit/roofitcore/src/RooFactoryWSTool.cxx`** -> AI Confidence: **99.39%**
553. **`roofit/roofitcore/src/RooGrid.cxx`** -> AI Confidence: **99.39%**
554. **`roofit/roofitcore/src/RooHelpers.cxx`** -> AI Confidence: **99.39%**
555. **`roofit/roofitcore/src/RooHist.cxx`** -> AI Confidence: **99.39%**
556. **`roofit/roofitcore/src/RooImproperIntegrator1D.cxx`** -> AI Confidence: **99.39%**
557. **`roofit/roofitcore/src/RooMCIntegrator.cxx`** -> AI Confidence: **99.39%**
558. **`roofit/roofitcore/src/RooMCStudy.cxx`** -> AI Confidence: **99.39%**
559. **`roofit/roofitcore/src/RooNLLVar.cxx`** -> AI Confidence: **99.39%**
560. **`roofit/roofitcore/src/RooNumIntFactory.cxx`** -> AI Confidence: **99.39%**
561. **`roofit/roofitcore/src/RooRandomizeParamMCSModule.cxx`** -> AI Confidence: **99.39%**
562. **`roofit/roofitcore/src/RooRealIntegral.cxx`** -> AI Confidence: **99.39%**
563. **`roofit/roofitcore/src/RooRecursiveFraction.cxx`** -> AI Confidence: **99.39%**
564. **`roofit/roofitcore/src/RooSimWSTool.cxx`** -> AI Confidence: **99.39%**
565. **`roofit/roofitcore/src/TestStatistics/LikelihoodJob.cxx`** -> AI Confidence: **99.39%**
566. **`roofit/roofitmore/src/RooNonCentralChiSquare.cxx`** -> AI Confidence: **99.39%**
567. **`roofit/roostats/src/HybridPlot.cxx`** -> AI Confidence: **99.39%**
568. **`roofit/roostats/src/HypoTestInverter.cxx`** -> AI Confidence: **99.39%**
569. **`roofit/roostats/src/MetropolisHastings.cxx`** -> AI Confidence: **99.39%**
570. **`roofit/roostats/src/NeymanConstruction.cxx`** -> AI Confidence: **99.39%**
571. **`roofit/roostats/src/SamplingDistribution.cxx`** -> AI Confidence: **99.39%**
572. **`roofit/roostats/src/ToyMCSampler.cxx`** -> AI Confidence: **99.39%**
573. **`roofit/xroofit/src/xRooHypoSpace.cxx`** -> AI Confidence: **99.39%**
574. **`roofit/xroofit/src/xRooNLLVar.cxx`** -> AI Confidence: **99.39%**
575. **`tmva/pymva/src/MethodPyGTB.cxx`** -> AI Confidence: **99.39%**
576. **`tmva/pymva/src/MethodPyKeras.cxx`** -> AI Confidence: **99.39%**
577. **`tmva/pymva/src/MethodPyTorch.cxx`** -> AI Confidence: **99.39%**
578. **`tmva/rmva/src/MethodRSVM.cxx`** -> AI Confidence: **99.39%**
579. **`tmva/sofie/inc/TMVA/ROperator_Reduce.hxx`** -> AI Confidence: **99.39%**
580. **`tmva/sofie/inc/TMVA/ROperator_Reshape.hxx`** -> AI Confidence: **99.39%**
581. **`tmva/tmva/src/BinarySearchTree.cxx`** -> AI Confidence: **99.39%**
582. **`tmva/tmva/src/CvSplit.cxx`** -> AI Confidence: **99.39%**
583. **`tmva/tmva/src/ExpectedErrorPruneTool.cxx`** -> AI Confidence: **99.39%**
584. **`tmva/tmva/src/GeneticAlgorithm.cxx`** -> AI Confidence: **99.39%**
585. **`tmva/tmva/src/KDEKernel.cxx`** -> AI Confidence: **99.39%**
586. **`tmva/tmva/src/MethodANNBase.cxx`** -> AI Confidence: **99.39%**
587. **`tmva/tmva/src/MethodBase.cxx`** -> AI Confidence: **99.39%**
588. **`tmva/tmva/src/MethodBoost.cxx`** -> AI Confidence: **99.39%**
589. **`tmva/tmva/src/MethodDL.cxx`** -> AI Confidence: **99.39%**
590. **`tmva/tmva/src/MethodDNN.cxx`** -> AI Confidence: **99.39%**
591. **`tmva/tmva/src/MethodKNN.cxx`** -> AI Confidence: **99.39%**
592. **`tmva/tmva/src/MethodPDERS.cxx`** -> AI Confidence: **99.39%**
593. **`tmva/tmva/src/MinuitFitter.cxx`** -> AI Confidence: **99.39%**
594. **`tmva/tmva/src/PDEFoamDensityBase.cxx`** -> AI Confidence: **99.39%**
595. **`tmva/tmva/src/PDEFoamTarget.cxx`** -> AI Confidence: **99.39%**
596. **`tmva/tmva/src/PDEFoamTargetDensity.cxx`** -> AI Confidence: **99.39%**
597. **`tmva/tmva/src/ResultsMulticlass.cxx`** -> AI Confidence: **99.39%**
598. **`tmva/tmva/src/RuleFit.cxx`** -> AI Confidence: **99.39%**
599. **`tmva/tmva/src/SVKernelMatrix.cxx`** -> AI Confidence: **99.39%**
600. **`tmva/tmva/src/Timer.cxx`** -> AI Confidence: **99.39%**
601. **`tmva/tmva/src/VariableDecorrTransform.cxx`** -> AI Confidence: **99.39%**
602. **`tmva/tmvagui/src/mvaeffs.cxx`** -> AI Confidence: **99.39%**
603. **`tree/dataframe/src/RSqliteDS.cxx`** -> AI Confidence: **99.39%**
604. **`tree/ntuplebrowse/src/RNTupleDrawVisitor.cxx`** -> AI Confidence: **99.39%**
605. **`tree/tree/src/TBranch.cxx`** -> AI Confidence: **99.39%**
606. **`tree/tree/src/TBranchObject.cxx`** -> AI Confidence: **99.39%**
607. **`tree/tree/src/TBranchSTL.cxx`** -> AI Confidence: **99.39%**
608. **`tree/tree/src/TLeaf.cxx`** -> AI Confidence: **99.39%**
609. **`tree/tree/src/TLeafC.cxx`** -> AI Confidence: **99.39%**
610. **`tree/tree/src/TNtuple.cxx`** -> AI Confidence: **99.39%**
611. **`tree/tree/src/TNtupleD.cxx`** -> AI Confidence: **99.39%**
612. **`tree/tree/src/TTree.cxx`** -> AI Confidence: **99.39%**
613. **`tree/treeplayer/src/TBranchProxy.cxx`** -> AI Confidence: **99.39%**
614. **`tree/treeplayer/src/TFileDrawMap.cxx`** -> AI Confidence: **99.39%**
615. **`tree/treeplayer/src/TTreeReader.cxx`** -> AI Confidence: **99.39%**
616. **`tree/treeplayer/src/TTreeReaderValue.cxx`** -> AI Confidence: **99.39%**
617. **`tree/treeplayer/src/TTreeTableInterface.cxx`** -> AI Confidence: **99.39%**
618. **`tree/treeviewer/src/TParallelCoord.cxx`** -> AI Confidence: **99.39%**
619. **`tree/treeviewer/src/TTVLVContainer.cxx`** -> AI Confidence: **99.39%**
620. **`tree/treeviewer/src/TTVSession.cxx`** -> AI Confidence: **99.39%**
621. **`tree/treeviewer/src/TTreeViewer.cxx`** -> AI Confidence: **99.39%**
622. **`tutorials/math/fit/fitEllipseTGraphRMM.cxx`** -> AI Confidence: **99.39%**
623. **`builtins/glew/src/visualinfo.c`** -> AI Confidence: **99.39%**
624. **`etc/html/saveScriptOutput.C`** -> AI Confidence: **99.39%**
625. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkcolor-win32.c`** -> AI Confidence: **99.39%**
626. **`graf2d/win32gdk/gdk/src/glib/giounix.c`** -> AI Confidence: **99.39%**
627. **`graf2d/win32gdk/gdk/src/glib/giowin32.c`** -> AI Confidence: **99.39%**
628. **`graf2d/win32gdk/gdk/src/glib/gmain.c`** -> AI Confidence: **99.39%**
629. **`graf2d/win32gdk/gdk/src/glib/gstrfuncs.c`** -> AI Confidence: **99.39%**
630. **`graf2d/win32gdk/gdk/src/glib/gutils.c`** -> AI Confidence: **99.39%**
631. **`interpreter/llvm-project/clang/tools/c-index-test/c-index-test.c`** -> AI Confidence: **99.39%**
632. **`interpreter/llvm-project/llvm/examples/OrcV2Examples/OrcV2CBindingsVeryLazy/OrcV2CBindingsVeryLazy.c`** -> AI Confidence: **99.39%**
633. **`tutorials/analysis/unfold/testUnfold2.C`** -> AI Confidence: **99.39%**
634. **`tutorials/analysis/unfold/testUnfold4.C`** -> AI Confidence: **99.39%**
635. **`tutorials/hsimple.C`** -> AI Confidence: **99.39%**
636. **`tutorials/io/ntuple/ntpl017_shared_reader.C`** -> AI Confidence: **99.39%**
637. **`tutorials/io/tree/tree143_drawsparse.C`** -> AI Confidence: **99.39%**
638. **`tutorials/legacy/net/fastMergeServer.C`** -> AI Confidence: **99.39%**
639. **`tutorials/legacy/spectrum/peaks.C`** -> AI Confidence: **99.39%**
640. **`tutorials/math/fit/TestBinomial.C`** -> AI Confidence: **99.39%**
641. **`tutorials/math/mathcoreVectorIO.C`** -> AI Confidence: **99.39%**
642. **`tutorials/math/matrix/invertMatrix.C`** -> AI Confidence: **99.39%**
643. **`tutorials/roofit/roostats/StandardFeldmanCousinsDemo.C`** -> AI Confidence: **99.39%**
644. **`tutorials/roofit/roostats/StandardProfileInspectorDemo.C`** -> AI Confidence: **99.39%**
645. **`tutorials/roofit/roostats/StandardProfileLikelihoodDemo.C`** -> AI Confidence: **99.39%**
646. **`tutorials/visualisation/eve/view3ds.C`** -> AI Confidence: **99.39%**
647. **`tutorials/visualisation/graphs/gr017_time.C`** -> AI Confidence: **99.39%**
648. **`tutorials/visualisation/gui/drag_and_drop.C`** -> AI Confidence: **99.39%**
649. **`js/modules/base/ObjectPainter.mjs`** -> AI Confidence: **99.39%**
650. **`js/modules/geom/TGeoPainter.mjs`** -> AI Confidence: **99.39%**
651. **`js/modules/gpad/RAxisPainter.mjs`** -> AI Confidence: **99.39%**
652. **`js/modules/gpad/TCanvasPainter.mjs`** -> AI Confidence: **99.39%**
653. **`js/modules/gpad/TFramePainter.mjs`** -> AI Confidence: **99.39%**
654. **`js/modules/hist/TH3Painter.mjs`** -> AI Confidence: **99.39%**
655. **`js/modules/hist/TPavePainter.mjs`** -> AI Confidence: **99.39%**
656. **`js/modules/hist2d/TGraphPainter.mjs`** -> AI Confidence: **99.39%**
657. **`js/modules/hist2d/TH2Painter.mjs`** -> AI Confidence: **99.39%**
658. **`bindings/pyroot/pythonizations/python/ROOT/_pythonization/_tmva/_sofie/_parser/_keras/parser.py`** -> AI Confidence: **99.35%**
659. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPMethod.cxx`** -> AI Confidence: **99.35%**
660. **`geom/geombuilder/src/TGeoTrapEditor.cxx`** -> AI Confidence: **99.35%**
661. **`graf3d/gl/src/TGLH2PolyPainter.cxx`** -> AI Confidence: **99.35%**
662. **`hist/hist/src/TGraphErrors.cxx`** -> AI Confidence: **99.35%**
663. **`interpreter/llvm-project/clang/tools/libclang/CIndexCodeCompletion.cpp`** -> AI Confidence: **99.35%**
664. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/BasicBlockUtils.cpp`** -> AI Confidence: **99.35%**
665. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/ModuleUtils.cpp`** -> AI Confidence: **99.35%**
666. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/PromoteMemoryToRegister.cpp`** -> AI Confidence: **99.35%**
667. **`interpreter/llvm-project/llvm/tools/bugpoint/ExtractFunction.cpp`** -> AI Confidence: **99.35%**
668. **`interpreter/llvm-project/llvm/tools/llvm-mca/llvm-mca.cpp`** -> AI Confidence: **99.35%**
669. **`interpreter/llvm-project/llvm/tools/llvm-profgen/ProfiledBinary.cpp`** -> AI Confidence: **99.35%**
670. **`interpreter/llvm-project/llvm/tools/llvm-reduce/DeltaManager.cpp`** -> AI Confidence: **99.35%**
671. **`io/sql/src/TSQLStructure.cxx`** -> AI Confidence: **99.35%**
672. **`math/minuit2/src/Minuit2Minimizer.cxx`** -> AI Confidence: **99.35%**
673. **`net/http/src/TRootSniffer.cxx`** -> AI Confidence: **99.35%**
674. **`net/net/src/TUDPSocket.cxx`** -> AI Confidence: **99.35%**
675. **`roofit/histfactory/src/HistFactoryNavigation.cxx`** -> AI Confidence: **99.35%**
676. **`roofit/roofitcore/src/BidirMMapPipe.cxx`** -> AI Confidence: **99.35%**
677. **`roofit/roofitcore/src/RooDataHist.cxx`** -> AI Confidence: **99.35%**
678. **`roofit/roofitcore/src/RooFFTConvPdf.cxx`** -> AI Confidence: **99.35%**
679. **`roofit/roostats/src/BayesianCalculator.cxx`** -> AI Confidence: **99.35%**
680. **`tmva/pymva/src/MethodPyRandomForest.cxx`** -> AI Confidence: **99.35%**
681. **`tmva/tmva/src/CrossValidation.cxx`** -> AI Confidence: **99.35%**
682. **`tmva/tmva/src/MethodCFMlpANN.cxx`** -> AI Confidence: **99.35%**
683. **`tmva/tmva/src/MethodCategory.cxx`** -> AI Confidence: **99.35%**
684. **`tmva/tmva/src/ModulekNN.cxx`** -> AI Confidence: **99.35%**
685. **`tmva/tmva/src/Reader.cxx`** -> AI Confidence: **99.35%**
686. **`tmva/tmva/src/Rule.cxx`** -> AI Confidence: **99.35%**
687. **`tree/dataframe/src/RCsvDS.cxx`** -> AI Confidence: **99.35%**
688. **`tree/treeplayer/src/TFormLeafInfo.cxx`** -> AI Confidence: **99.35%**
689. **`tree/treeplayer/src/TTreeReaderValueFast.cxx`** -> AI Confidence: **99.35%**
690. **`graf2d/win32gdk/gdk/src/glib/gwin32.c`** -> AI Confidence: **99.35%**
691. **`tutorials/math/mathcoreGenVector.C`** -> AI Confidence: **99.35%**
692. **`tutorials/math/quadp/portfolio.C`** -> AI Confidence: **99.35%**
693. **`interpreter/llvm-project/llvm/utils/extract_symbols.py`** -> AI Confidence: **99.34%**
694. **`interpreter/llvm-project/llvm/utils/lit/lit/llvm/config.py`** -> AI Confidence: **99.34%**
695. **`core/base/src/TSystemDirectory.cxx`** -> AI Confidence: **99.34%**
696. **`core/cont/src/TSeqCollection.cxx`** -> AI Confidence: **99.34%**
697. **`core/foundation/inc/ROOT/RConfig.hxx`** -> AI Confidence: **99.34%**
698. **`core/meta/src/TBaseClass.cxx`** -> AI Confidence: **99.34%**
699. **`core/multiproc/src/TMPWorker.cxx`** -> AI Confidence: **99.34%**
700. **`geom/geom/src/TGeoHype.cxx`** -> AI Confidence: **99.34%**
701. **`geom/geom/src/TGeoStateInfo.cxx`** -> AI Confidence: **99.34%**
702. **`graf2d/asimage/src/libAfterImage/win32/StdAfx.h`** -> AI Confidence: **99.34%**
703. **`graf2d/gpad/src/TControlBarButton.cxx`** -> AI Confidence: **99.34%**
704. **`graf2d/gpad/src/TSliderBox.cxx`** -> AI Confidence: **99.34%**
705. **`graf2d/graf/src/TLegendEntry.cxx`** -> AI Confidence: **99.34%**
706. **`graf2d/graf/src/TPaveLabel.cxx`** -> AI Confidence: **99.34%**
707. **`graf2d/mathtext/src/fontembedps.cxx`** -> AI Confidence: **99.34%**
708. **`graf2d/mathtext/src/mathtextencode.cxx`** -> AI Confidence: **99.34%**
709. **`graf2d/win32gdk/gdk/src/gdk/gdki18n.h`** -> AI Confidence: **99.34%**
710. **`graf2d/win32gdk/gdk/src/iconv/aliases2.h`** -> AI Confidence: **99.34%**
711. **`graf3d/eve/src/TEveFrameBoxGL.cxx`** -> AI Confidence: **99.34%**
712. **`graf3d/eve/src/TEveMacro.cxx`** -> AI Confidence: **99.34%**
713. **`graf3d/eve/src/TEvePolygonSetProjected.cxx`** -> AI Confidence: **99.34%**
714. **`graf3d/eve/src/TEveScene.cxx`** -> AI Confidence: **99.34%**
715. **`graf3d/eve/src/TEveStraightLineSetGL.cxx`** -> AI Confidence: **99.34%**
716. **`graf3d/g3d/src/THelix.cxx`** -> AI Confidence: **99.34%**
717. **`graf3d/g3d/src/TTUBS.cxx`** -> AI Confidence: **99.34%**
718. **`graf3d/gl/src/TGLClipSetEditor.cxx`** -> AI Confidence: **99.34%**
719. **`graf3d/gviz3d/src/TStructViewer.cxx`** -> AI Confidence: **99.34%**
720. **`gui/fitpanel/src/TTreeInput.cxx`** -> AI Confidence: **99.34%**
721. **`gui/gui/src/TGDoubleSlider.cxx`** -> AI Confidence: **99.34%**
722. **`gui/gui/src/TGShapedFrame.cxx`** -> AI Confidence: **99.34%**
723. **`gui/gui/src/TGSlider.cxx`** -> AI Confidence: **99.34%**
724. **`gui/gui/src/TGTableContainer.cxx`** -> AI Confidence: **99.34%**
725. **`gui/gui/src/TGTripleSlider.cxx`** -> AI Confidence: **99.34%**
726. **`gui/gui/src/TGXYLayout.cxx`** -> AI Confidence: **99.34%**
727. **`gui/gui/src/TRootApplication.cxx`** -> AI Confidence: **99.34%**
728. **`gui/guihtml/src/TGHtmlDraw.cxx`** -> AI Confidence: **99.34%**
729. **`gui/guihtml/src/TGHtmlIndex.cxx`** -> AI Confidence: **99.34%**
730. **`gui/guihtml/src/TGHtmlTable.cxx`** -> AI Confidence: **99.34%**
731. **`gui/guihtml/src/TGHtmlUri.cxx`** -> AI Confidence: **99.34%**
732. **`gui/qt6webdisplay/rootwebpage.cpp`** -> AI Confidence: **99.34%**
733. **`gui/webgui6/src/TWebMenuItem.cxx`** -> AI Confidence: **99.34%**
734. **`hist/spectrum/src/TSpectrum.cxx`** -> AI Confidence: **99.34%**
735. **`hist/spectrum/src/TSpectrum2.cxx`** -> AI Confidence: **99.34%**
736. **`interpreter/llvm-project/clang/tools/clang-fuzzer/proto-to-cxx/loop_proto_to_cxx_main.cpp`** -> AI Confidence: **99.34%**
737. **`interpreter/llvm-project/clang/tools/clang-fuzzer/proto-to-cxx/proto_to_cxx_main.cpp`** -> AI Confidence: **99.34%**
738. **`interpreter/llvm-project/clang/tools/clang-fuzzer/proto-to-llvm/loop_proto_to_llvm_main.cpp`** -> AI Confidence: **99.34%**
739. **`interpreter/llvm-project/clang/utils/TableGen/ClangBuiltinsEmitter.cpp`** -> AI Confidence: **99.34%**
740. **`interpreter/llvm-project/llvm/include/llvm/Support/Compiler.h`** -> AI Confidence: **99.34%**
741. **`interpreter/llvm-project/llvm/lib/Transforms/Utils/LoopConstrainer.cpp`** -> AI Confidence: **99.34%**
742. **`interpreter/llvm-project/llvm/tools/llvm-reduce/deltas/ReduceInstructionFlags.cpp`** -> AI Confidence: **99.34%**
743. **`interpreter/llvm-project/llvm/tools/llvm-reduce/deltas/ReduceMemoryOperations.cpp`** -> AI Confidence: **99.34%**
744. **`interpreter/llvm-project/llvm/tools/llvm-reduce/deltas/ReduceRegisterDefs.cpp`** -> AI Confidence: **99.34%**
745. **`interpreter/llvm-project/llvm/utils/TableGen/Common/AsmWriterInst.cpp`** -> AI Confidence: **99.34%**
746. **`interpreter/llvm-project/llvm/utils/TableGen/Common/CodeGenInstruction.cpp`** -> AI Confidence: **99.34%**
747. **`interpreter/llvm-project/llvm/utils/TableGen/DAGISelMatcherOpt.cpp`** -> AI Confidence: **99.34%**
748. **`interpreter/llvm-project/llvm/utils/TableGen/OptionRSTEmitter.cpp`** -> AI Confidence: **99.34%**
749. **`io/io/src/TContainerConverters.cxx`** -> AI Confidence: **99.34%**
750. **`main/src/rmain.cxx`** -> AI Confidence: **99.34%**
751. **`math/experimental/genvectorx/src/BitReproducible.cxx`** -> AI Confidence: **99.34%**
752. **`math/mathcore/src/AdaptiveIntegratorMultiDim.cxx`** -> AI Confidence: **99.34%**
753. **`math/mathcore/src/FitConfig.cxx`** -> AI Confidence: **99.34%**
754. **`math/mathmore/src/complex_quartic.h`** -> AI Confidence: **99.34%**
755. **`math/minuit2/src/TMinuit2TraceObject.cxx`** -> AI Confidence: **99.34%**
756. **`math/physics/src/TRobustEstimator.cxx`** -> AI Confidence: **99.34%**
757. **`misc/rmkdepend/mainroot.cxx`** -> AI Confidence: **99.34%**
758. **`net/net/src/TServerSocket.cxx`** -> AI Confidence: **99.34%**
759. **`roofit/histfactory/src/hist2workspace.cxx`** -> AI Confidence: **99.34%**
760. **`roofit/roofit/src/RooBukinPdf.cxx`** -> AI Confidence: **99.34%**
761. **`roofit/roofitcore/src/RooBrentRootFinder.cxx`** -> AI Confidence: **99.34%**
762. **`roofit/roofitcore/src/RooFormulaVar.cxx`** -> AI Confidence: **99.34%**
763. **`roofit/roofitcore/src/TestStatistics/LikelihoodSerial.cxx`** -> AI Confidence: **99.34%**
764. **`roottest/scripts/utils.cc`** -> AI Confidence: **99.34%**
765. **`tmva/sofie/inc/TMVA/ROperator_Gather.hxx`** -> AI Confidence: **99.34%**
766. **`tmva/sofie/inc/TMVA/ROperator_GatherND.hxx`** -> AI Confidence: **99.34%**
767. **`tmva/sofie/inc/TMVA/ROperator_Range.hxx`** -> AI Confidence: **99.34%**
768. **`tmva/sofie/inc/TMVA/ROperator_Slice.hxx`** -> AI Confidence: **99.34%**
769. **`tmva/tmva/src/ClassInfo.cxx`** -> AI Confidence: **99.34%**
770. **`tmva/tmva/src/LDA.cxx`** -> AI Confidence: **99.34%**
771. **`tmva/tmva/src/Node.cxx`** -> AI Confidence: **99.34%**
772. **`tmva/tmva/src/RootFinder.cxx`** -> AI Confidence: **99.34%**
773. **`tmva/tmvagui/src/TMVARegGui.cxx`** -> AI Confidence: **99.34%**
774. **`tmva/tmvagui/src/deviations.cxx`** -> AI Confidence: **99.34%**
775. **`tmva/tmvagui/src/efficiencies.cxx`** -> AI Confidence: **99.34%**
776. **`tmva/tmvagui/src/mvas.cxx`** -> AI Confidence: **99.34%**
777. **`tmva/tmvagui/src/mvasMulticlass.cxx`** -> AI Confidence: **99.34%**
778. **`tmva/tmvagui/src/regression_averagedevs.cxx`** -> AI Confidence: **99.34%**
779. **`tmva/tmvagui/src/training_history.cxx`** -> AI Confidence: **99.34%**
780. **`tree/tree/src/TLeafB.cxx`** -> AI Confidence: **99.34%**
781. **`tree/treeplayer/src/TMPWorkerTree.cxx`** -> AI Confidence: **99.34%**
782. **`tutorials/io/tree/dictionary/writeTree.cxx`** -> AI Confidence: **99.34%**
783. **`config/thisroot.csh`** -> AI Confidence: **99.34%**
784. **`core/clib/src/snprintf.c`** -> AI Confidence: **99.34%**
785. **`graf2d/asimage/src/libAfterImage/zlib/infback.c`** -> AI Confidence: **99.34%**
786. **`graf2d/win32gdk/gdk/src/gdk/gdk.c`** -> AI Confidence: **99.34%**
787. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkfont-win32.c`** -> AI Confidence: **99.34%**
788. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkimage-win32.c`** -> AI Confidence: **99.34%**
789. **`graf2d/win32gdk/gdk/src/glib/gmarkup.c`** -> AI Confidence: **99.34%**
790. **`graf2d/win32gdk/gdk/src/glib/gunidecomp.c`** -> AI Confidence: **99.34%**
791. **`graf2d/win32gdk/gdk/src/glib/guniprop.c`** -> AI Confidence: **99.34%**
792. **`misc/rmkdepend/main.c`** -> AI Confidence: **99.34%**
793. **`tutorials/math/pdf/pdf012_tStudent.C`** -> AI Confidence: **99.34%**
794. **`tutorials/math/quasirandom.C`** -> AI Confidence: **99.34%**
795. **`tutorials/visualisation/gl/glViewerExercise.C`** -> AI Confidence: **99.34%**
796. **`graf2d/cocoa/src/MenuLoader.mm`** -> AI Confidence: **99.34%**
797. **`graf2d/cocoa/src/XLFDParser.mm`** -> AI Confidence: **99.34%**
798. **`misc/rootql/GeneratePreviewForURL.m`** -> AI Confidence: **99.34%**
799. **`js/modules/hist/TF2Painter.mjs`** -> AI Confidence: **99.34%**
800. **`js/modules/hist/TH2Painter.mjs`** -> AI Confidence: **99.34%**
801. **`js/modules/hist/hist3d.mjs`** -> AI Confidence: **99.34%**
802. **`js/modules/hist2d/TH1Painter.mjs`** -> AI Confidence: **99.34%**
803. **`bindings/pyroot/cppyy/CPyCppyy/src/PyException.cxx`** -> AI Confidence: **99.32%**
804. **`core/base/src/TVirtualPS.cxx`** -> AI Confidence: **99.32%**
805. **`graf2d/asimage/src/libAfterImage/zlib/zconf.h`** -> AI Confidence: **99.32%**
806. **`graf2d/mathtext/src/mathtextview.cxx`** -> AI Confidence: **99.32%**
807. **`graf2d/win32gdk/gdk/src/glib/galloca.h`** -> AI Confidence: **99.32%**
808. **`graf3d/eve/src/TEveSecondarySelectable.cxx`** -> AI Confidence: **99.32%**
809. **`graf3d/g3d/src/TMaterial.cxx`** -> AI Confidence: **99.32%**
810. **`graf3d/gl/src/TGLQuadric.cxx`** -> AI Confidence: **99.32%**
811. **`gui/ged/src/TPaveStatsEditor.cxx`** -> AI Confidence: **99.32%**
812. **`gui/gui/src/TGString.cxx`** -> AI Confidence: **99.32%**
813. **`gui/guibuilder/src/TGuiBldHintsButton.cxx`** -> AI Confidence: **99.32%**
814. **`gui/guihtml/src/TGHtmlElement.cxx`** -> AI Confidence: **99.32%**
815. **`gui/guihtml/src/TGHtmlLayout.cxx`** -> AI Confidence: **99.32%**
816. **`hist/hist/src/TF1Data_v5.cxx`** -> AI Confidence: **99.32%**
817. **`hist/hist/src/TGraphDelaunay.cxx`** -> AI Confidence: **99.32%**
818. **`math/experimental/genvectorx/inc/MathX/GenVectorX/AccHeaders.h`** -> AI Confidence: **99.32%**
819. **`math/matrix/src/TDecompBK.cxx`** -> AI Confidence: **99.32%**
820. **`math/minuit2/src/mntplot.cxx`** -> AI Confidence: **99.32%**
821. **`math/physics/src/TRolke.cxx`** -> AI Confidence: **99.32%**
822. **`math/quadp/src/TMehrotraSolver.cxx`** -> AI Confidence: **99.32%**
823. **`roofit/roofitcore/src/RooAbsCache.cxx`** -> AI Confidence: **99.32%**
824. **`roottest/root/meta/genreflex/ROOT-5768/RelationalCool/src/SealBase_sysapi_Windows.h`** -> AI Confidence: **99.32%**
825. **`tmva/rmva/src/RMethodBase.cxx`** -> AI Confidence: **99.32%**
826. **`tmva/sofie_parsers/src/ParseConstant.cxx`** -> AI Confidence: **99.32%**
827. **`tmva/sofie_parsers/src/ParseConv.cxx`** -> AI Confidence: **99.32%**
828. **`tmva/sofie_parsers/src/ParseConvTranspose.cxx`** -> AI Confidence: **99.32%**
829. **`tmva/sofie_parsers/src/ParseFuseConvTransposeAdd.cxx`** -> AI Confidence: **99.32%**
830. **`tmva/sofie_parsers/src/ParseFuseGemmRelu.cxx`** -> AI Confidence: **99.32%**
831. **`tmva/sofie_parsers/src/ParseGRU.cxx`** -> AI Confidence: **99.32%**
832. **`tmva/sofie_parsers/src/ParseGemm.cxx`** -> AI Confidence: **99.32%**
833. **`tmva/sofie_parsers/src/ParseLSTM.cxx`** -> AI Confidence: **99.32%**
834. **`tmva/sofie_parsers/src/ParseLayerNormalization.cxx`** -> AI Confidence: **99.32%**
835. **`tmva/sofie_parsers/src/ParsePool.cxx`** -> AI Confidence: **99.32%**
836. **`tmva/sofie_parsers/src/ParseRNN.cxx`** -> AI Confidence: **99.32%**
837. **`tmva/sofie_parsers/src/ParseRandom.cxx`** -> AI Confidence: **99.32%**
838. **`tmva/sofie_parsers/src/ParseReshape.cxx`** -> AI Confidence: **99.32%**
839. **`tmva/sofie_parsers/src/ParseSlice.cxx`** -> AI Confidence: **99.32%**
840. **`tmva/tmvagui/src/compareanapp.cxx`** -> AI Confidence: **99.32%**
841. **`tmva/tmvagui/src/likelihoodrefs.cxx`** -> AI Confidence: **99.32%**
842. **`core/zip/src/ZTrees.c`** -> AI Confidence: **99.32%**
843. **`graf2d/asimage/src/libAfterImage/libjpeg/jcdctmgr.c`** -> AI Confidence: **99.32%**
844. **`graf2d/asimage/src/libAfterImage/libjpeg/jfdctfst.c`** -> AI Confidence: **99.32%**
845. **`graf2d/asimage/src/libAfterImage/libjpeg/jidctflt.c`** -> AI Confidence: **99.32%**
846. **`graf2d/asimage/src/libAfterImage/libjpeg/jidctfst.c`** -> AI Confidence: **99.32%**
847. **`graf2d/asimage/src/libAfterImage/libpng/pngrtran.c`** -> AI Confidence: **99.32%**
848. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkcursor-win32.c`** -> AI Confidence: **99.32%**
849. **`graf2d/win32gdk/gdk/src/glib/gshell.c`** -> AI Confidence: **99.32%**
850. **`tutorials/io/importCode.C`** -> AI Confidence: **99.32%**
851. **`tutorials/io/sql/sqlselect.C`** -> AI Confidence: **99.32%**
852. **`tutorials/math/fit/fitLinear2.C`** -> AI Confidence: **99.32%**
853. **`gui/cefdisplay/src/gui_handler_mac.mm`** -> AI Confidence: **99.32%**
854. **`misc/rootql/GenerateThumbnailForURL.m`** -> AI Confidence: **99.32%**
855. **`js/modules/base/TAttFillHandler.mjs`** -> AI Confidence: **99.32%**
856. **`js/modules/base/TAttLineHandler.mjs`** -> AI Confidence: **99.32%**
857. **`js/modules/base/TAttMarkerHandler.mjs`** -> AI Confidence: **99.32%**
858. **`bindings/distrdf/python/DistRDF/HeadNode.py`** -> AI Confidence: **99.31%**
859. **`bindings/pyroot/cppyy/cppyy/bench/bench_functioncalls.py`** -> AI Confidence: **99.31%**
860. **`bindings/pyroot/cppyy/cppyy/setup.py`** -> AI Confidence: **99.31%**
861. **`bindings/pyroot/pythonizations/python/ROOT/JsMVA/Factory.py`** -> AI Confidence: **99.31%**
862. **`bindings/pyroot/pythonizations/python/ROOT/_numbadeclare.py`** -> AI Confidence: **99.31%**
863. **`bindings/pyroot/pythonizations/python/ROOT/_pythonization/_rdf_pyz.py`** -> AI Confidence: **99.31%**
864. **`cmake/unix/makeCITATION.py`** -> AI Confidence: **99.31%**
865. **`interpreter/llvm-project/clang/tools/clang-format/clang-format-diff.py`** -> AI Confidence: **99.31%**
866. **`interpreter/llvm-project/clang/tools/clang-format/git-clang-format`** -> AI Confidence: **99.31%**
867. **`interpreter/llvm-project/clang/tools/scan-build-py/lib/libscanbuild/analyze.py`** -> AI Confidence: **99.31%**
868. **`interpreter/llvm-project/clang/tools/scan-build-py/lib/libscanbuild/arguments.py`** -> AI Confidence: **99.31%**
869. **`interpreter/llvm-project/clang/tools/scan-build-py/lib/libscanbuild/report.py`** -> AI Confidence: **99.31%**
870. **`interpreter/llvm-project/clang/tools/scan-build/bin/set-xcode-analyzer`** -> AI Confidence: **99.31%**
871. **`interpreter/llvm-project/clang/tools/scan-view/share/ScanView.py`** -> AI Confidence: **99.31%**
872. **`interpreter/llvm-project/clang/utils/ABITest/ABITestGen.py`** -> AI Confidence: **99.31%**
873. **`interpreter/llvm-project/clang/utils/analyzer/SATest.py`** -> AI Confidence: **99.31%**
874. **`interpreter/llvm-project/clang/utils/analyzer/exploded-graph-rewriter.py`** -> AI Confidence: **99.31%**
875. **`interpreter/llvm-project/clang/utils/check_cfc/check_cfc.py`** -> AI Confidence: **99.31%**
876. **`interpreter/llvm-project/clang/utils/clangdiag.py`** -> AI Confidence: **99.31%**
877. **`interpreter/llvm-project/clang/utils/creduce-clang-crash.py`** -> AI Confidence: **99.31%**
878. **`interpreter/llvm-project/clang/utils/hmaptool/hmaptool`** -> AI Confidence: **99.31%**
879. **`interpreter/llvm-project/clang/utils/perf-training/perf-helper.py`** -> AI Confidence: **99.31%**
880. **`interpreter/llvm-project/clang/utils/token-delta.py`** -> AI Confidence: **99.31%**
881. **`interpreter/llvm-project/llvm/utils/Misc/zkill`** -> AI Confidence: **99.31%**
882. **`interpreter/llvm-project/llvm/utils/Reviewing/find_interesting_reviews.py`** -> AI Confidence: **99.31%**
883. **`interpreter/llvm-project/llvm/utils/UpdateTestChecks/common.py`** -> AI Confidence: **99.31%**
884. **`interpreter/llvm-project/llvm/utils/abtest.py`** -> AI Confidence: **99.31%**
885. **`interpreter/llvm-project/llvm/utils/collect_and_build_with_pgo.py`** -> AI Confidence: **99.31%**
886. **`interpreter/llvm-project/llvm/utils/demangle_tree.py`** -> AI Confidence: **99.31%**
887. **`interpreter/llvm-project/llvm/utils/git/code-format-helper.py`** -> AI Confidence: **99.31%**
888. **`interpreter/llvm-project/llvm/utils/lit/lit/TestRunner.py`** -> AI Confidence: **99.31%**
889. **`interpreter/llvm-project/llvm/utils/lit/lit/builtin_commands/diff.py`** -> AI Confidence: **99.31%**
890. **`interpreter/llvm-project/llvm/utils/lit/lit/cl_arguments.py`** -> AI Confidence: **99.31%**
891. **`interpreter/llvm-project/llvm/utils/lit/lit/formats/googletest.py`** -> AI Confidence: **99.31%**
892. **`interpreter/llvm-project/llvm/utils/lit/lit/main.py`** -> AI Confidence: **99.31%**
893. **`interpreter/llvm-project/llvm/utils/lit/lit/reports.py`** -> AI Confidence: **99.31%**
894. **`interpreter/llvm-project/llvm/utils/lit/lit/util.py`** -> AI Confidence: **99.31%**
895. **`interpreter/llvm-project/llvm/utils/llvm-locstats/llvm-locstats.py`** -> AI Confidence: **99.31%**
896. **`interpreter/llvm-project/llvm/utils/llvm-mca-compare.py`** -> AI Confidence: **99.31%**
897. **`interpreter/llvm-project/llvm/utils/remote-exec.py`** -> AI Confidence: **99.31%**
898. **`interpreter/llvm-project/llvm/utils/revert_checker.py`** -> AI Confidence: **99.31%**
899. **`interpreter/llvm-project/llvm/utils/update_any_test_checks.py`** -> AI Confidence: **99.31%**
900. **`interpreter/llvm-project/llvm/utils/update_cc_test_checks.py`** -> AI Confidence: **99.31%**
901. **`interpreter/llvm-project/llvm/utils/update_mc_test_checks.py`** -> AI Confidence: **99.31%**
902. **`interpreter/llvm-project/llvm/utils/update_mca_test_checks.py`** -> AI Confidence: **99.31%**
903. **`interpreter/llvm-project/llvm/utils/update_mir_test_checks.py`** -> AI Confidence: **99.31%**
904. **`interpreter/llvm-project/llvm/utils/update_test_body.py`** -> AI Confidence: **99.31%**
905. **`bindings/pyroot/cppyy/CPyCppyy/src/API.cxx`** -> AI Confidence: **99.31%**
906. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPConstructor.cxx`** -> AI Confidence: **99.31%**
907. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPDataMember.cxx`** -> AI Confidence: **99.31%**
908. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPInstance.cxx`** -> AI Confidence: **99.31%**
909. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPOverload.cxx`** -> AI Confidence: **99.31%**
910. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPScope.cxx`** -> AI Confidence: **99.31%**
911. **`bindings/pyroot/cppyy/CPyCppyy/src/CPyCppyyModule.cxx`** -> AI Confidence: **99.31%**
912. **`bindings/pyroot/cppyy/CPyCppyy/src/Dispatcher.cxx`** -> AI Confidence: **99.31%**
913. **`bindings/pyroot/cppyy/CPyCppyy/src/LowLevelViews.cxx`** -> AI Confidence: **99.31%**
914. **`bindings/pyroot/cppyy/CPyCppyy/src/MemoryRegulator.cxx`** -> AI Confidence: **99.31%**
915. **`bindings/pyroot/cppyy/CPyCppyy/src/Pythonize.cxx`** -> AI Confidence: **99.31%**
916. **`bindings/pyroot/cppyy/CPyCppyy/src/TPyClassGenerator.cxx`** -> AI Confidence: **99.31%**
917. **`bindings/pyroot/cppyy/CPyCppyy/src/Utility.cxx`** -> AI Confidence: **99.31%**
918. **`bindings/pyroot/cppyy/cppyy-backend/clingwrapper/src/clingwrapper.cxx`** -> AI Confidence: **99.31%**
919. **`bindings/pyroot/pythonizations/src/TTreePyz.cxx`** -> AI Confidence: **99.31%**
920. **`bindings/r/src/TRInterface.cxx`** -> AI Confidence: **99.31%**
921. **`bindings/tpython/src/TPyClassGenerator.cxx`** -> AI Confidence: **99.31%**
922. **`bindings/tpython/src/TPython.cxx`** -> AI Confidence: **99.31%**
923. **`core/base/src/TApplication.cxx`** -> AI Confidence: **99.31%**
924. **`core/base/src/TAttAxis.cxx`** -> AI Confidence: **99.31%**
925. **`core/base/src/TAttLine.cxx`** -> AI Confidence: **99.31%**
926. **`core/base/src/TAttMarker.cxx`** -> AI Confidence: **99.31%**
927. **`core/base/src/TAttText.cxx`** -> AI Confidence: **99.31%**
928. **`core/base/src/TDirectory.cxx`** -> AI Confidence: **99.31%**
929. **`core/base/src/TFolder.cxx`** -> AI Confidence: **99.31%**
930. **`core/base/src/TListOfTypes.cxx`** -> AI Confidence: **99.31%**
931. **`core/base/src/TMD5.cxx`** -> AI Confidence: **99.31%**
932. **`core/base/src/TMacro.cxx`** -> AI Confidence: **99.31%**
933. **`core/base/src/TObject.cxx`** -> AI Confidence: **99.31%**
934. **`core/base/src/TQCommand.cxx`** -> AI Confidence: **99.31%**
935. **`core/base/src/TQObject.cxx`** -> AI Confidence: **99.31%**
936. **`core/base/src/TROOT.cxx`** -> AI Confidence: **99.31%**
937. **`core/base/src/TRef.cxx`** -> AI Confidence: **99.31%**
938. **`core/base/src/TStopwatch.cxx`** -> AI Confidence: **99.31%**
939. **`core/base/src/TStorage.cxx`** -> AI Confidence: **99.31%**
940. **`core/base/src/TString.cxx`** -> AI Confidence: **99.31%**
941. **`core/base/src/TStyle.cxx`** -> AI Confidence: **99.31%**
942. **`core/base/src/TTimeStamp.cxx`** -> AI Confidence: **99.31%**
943. **`core/base/src/TUUID.cxx`** -> AI Confidence: **99.31%**
944. **`core/clingutils/src/TClingUtils.cxx`** -> AI Confidence: **99.31%**
945. **`core/cont/src/TClassTable.cxx`** -> AI Confidence: **99.31%**
946. **`core/cont/src/TClonesArray.cxx`** -> AI Confidence: **99.31%**
947. **`core/cont/src/TCollection.cxx`** -> AI Confidence: **99.31%**
948. **`core/dictgen/src/BaseSelectionRule.cxx`** -> AI Confidence: **99.31%**
949. **`core/dictgen/src/DictSelectionReader.cxx`** -> AI Confidence: **99.31%**
950. **`core/dictgen/src/Scanner.cxx`** -> AI Confidence: **99.31%**
951. **`core/dictgen/src/SelectionRules.cxx`** -> AI Confidence: **99.31%**
952. **`core/dictgen/src/TModuleGenerator.cxx`** -> AI Confidence: **99.31%**
953. **`core/dictgen/src/rootcling_impl.cxx`** -> AI Confidence: **99.31%**
954. **`core/foundation/inc/ROOT/RError.hxx`** -> AI Confidence: **99.31%**
955. **`core/foundation/src/FoundationUtils.cxx`** -> AI Confidence: **99.31%**
956. **`core/foundation/src/RConversionRuleParser.cxx`** -> AI Confidence: **99.31%**
957. **`core/foundation/src/TError.cxx`** -> AI Confidence: **99.31%**
958. **`core/gui/src/TBrowser.cxx`** -> AI Confidence: **99.31%**
959. **`core/gui/src/TGuiFactory.cxx`** -> AI Confidence: **99.31%**
960. **`core/imt/src/RTaskArena.cxx`** -> AI Confidence: **99.31%**
961. **`core/lz4/src/ZipLZ4.cxx`** -> AI Confidence: **99.31%**
962. **`core/meta/src/TCheckHashRecursiveRemoveConsistency.h`** -> AI Confidence: **99.31%**
963. **`core/meta/src/TClass.cxx`** -> AI Confidence: **99.31%**
964. **`core/meta/src/TEnum.cxx`** -> AI Confidence: **99.31%**
965. **`core/meta/src/TFunction.cxx`** -> AI Confidence: **99.31%**
966. **`core/meta/src/TListOfDataMembers.cxx`** -> AI Confidence: **99.31%**
967. **`core/meta/src/TSchemaRuleSet.cxx`** -> AI Confidence: **99.31%**
968. **`core/meta/src/TStatusBitsChecker.cxx`** -> AI Confidence: **99.31%**
969. **`core/meta/src/TVirtualStreamerInfo.cxx`** -> AI Confidence: **99.31%**
970. **`core/metacling/src/TCling.cxx`** -> AI Confidence: **99.31%**
971. **`core/metacling/src/TClingBaseClassInfo.cxx`** -> AI Confidence: **99.31%**
972. **`core/metacling/src/TClingCallFunc.cxx`** -> AI Confidence: **99.31%**
973. **`core/metacling/src/TClingClassInfo.cxx`** -> AI Confidence: **99.31%**
974. **`core/metacling/src/TClingDataMemberInfo.cxx`** -> AI Confidence: **99.31%**
975. **`core/metacling/src/TClingMethodArgInfo.cxx`** -> AI Confidence: **99.31%**
976. **`core/metacling/src/TClingMethodInfo.cxx`** -> AI Confidence: **99.31%**
977. **`core/metacling/src/TClingRdictModuleFileExtension.cxx`** -> AI Confidence: **99.31%**
978. **`core/metacling/src/TClingTypedefInfo.cxx`** -> AI Confidence: **99.31%**
979. **`core/textinput/src/Getline.cxx`** -> AI Confidence: **99.31%**
980. **`core/textinput/src/textinput/Editor.cpp`** -> AI Confidence: **99.31%**
981. **`core/textinput/src/textinput/TerminalDisplay.cpp`** -> AI Confidence: **99.31%**
982. **`core/textinput/src/textinput/TerminalDisplayUnix.cpp`** -> AI Confidence: **99.31%**
983. **`core/textinput/src/textinput/TextInput.cpp`** -> AI Confidence: **99.31%**
984. **`core/thread/src/TThread.cxx`** -> AI Confidence: **99.31%**
985. **`core/winnt/src/TWinNTSystem.cxx`** -> AI Confidence: **99.31%**
986. **`core/winnt/src/Win32Splash.cxx`** -> AI Confidence: **99.31%**
987. **`core/zip/src/RZip.cxx`** -> AI Confidence: **99.31%**
988. **`geom/geom/src/TGeoBBox.cxx`** -> AI Confidence: **99.31%**
989. **`geom/geom/src/TGeoBoolNode.cxx`** -> AI Confidence: **99.31%**
990. **`geom/geom/src/TGeoColorScheme.cxx`** -> AI Confidence: **99.31%**
991. **`geom/geom/src/TGeoCompositeShape.cxx`** -> AI Confidence: **99.31%**
992. **`geom/geom/src/TGeoCone.cxx`** -> AI Confidence: **99.31%**
993. **`geom/geom/src/TGeoEltu.cxx`** -> AI Confidence: **99.31%**
994. **`geom/geom/src/TGeoManager.cxx`** -> AI Confidence: **99.31%**
995. **`geom/geom/src/TGeoMaterial.cxx`** -> AI Confidence: **99.31%**
996. **`geom/geom/src/TGeoNode.cxx`** -> AI Confidence: **99.31%**
997. **`geom/geom/src/TGeoParaboloid.cxx`** -> AI Confidence: **99.31%**
998. **`geom/geom/src/TGeoParallelWorld.cxx`** -> AI Confidence: **99.31%**
999. **`geom/geom/src/TGeoPatternFinder.cxx`** -> AI Confidence: **99.31%**
1000. **`geom/geom/src/TGeoPhysicalNode.cxx`** -> AI Confidence: **99.31%**
1001. **`geom/geom/src/TGeoShape.cxx`** -> AI Confidence: **99.31%**
1002. **`geom/geom/src/TGeoTessellated.cxx`** -> AI Confidence: **99.31%**
1003. **`geom/geom/src/TGeoTube.cxx`** -> AI Confidence: **99.31%**
1004. **`geom/geom/src/TGeoXtru.cxx`** -> AI Confidence: **99.31%**
1005. **`geom/geombuilder/src/TGeoBBoxEditor.cxx`** -> AI Confidence: **99.31%**
1006. **`geom/geombuilder/src/TGeoConeEditor.cxx`** -> AI Confidence: **99.31%**
1007. **`geom/geombuilder/src/TGeoEltuEditor.cxx`** -> AI Confidence: **99.31%**
1008. **`geom/geombuilder/src/TGeoManagerEditor.cxx`** -> AI Confidence: **99.31%**
1009. **`geom/geombuilder/src/TGeoMaterialEditor.cxx`** -> AI Confidence: **99.31%**
1010. **`geom/geombuilder/src/TGeoMatrixEditor.cxx`** -> AI Confidence: **99.31%**
1011. **`geom/geombuilder/src/TGeoMediumEditor.cxx`** -> AI Confidence: **99.31%**
1012. **`geom/geombuilder/src/TGeoNodeEditor.cxx`** -> AI Confidence: **99.31%**
1013. **`geom/geombuilder/src/TGeoParaEditor.cxx`** -> AI Confidence: **99.31%**
1014. **`geom/geombuilder/src/TGeoPconEditor.cxx`** -> AI Confidence: **99.31%**
1015. **`geom/geombuilder/src/TGeoTabManager.cxx`** -> AI Confidence: **99.31%**
1016. **`geom/geombuilder/src/TGeoTorusEditor.cxx`** -> AI Confidence: **99.31%**
1017. **`geom/geombuilder/src/TGeoTrd1Editor.cxx`** -> AI Confidence: **99.31%**
1018. **`geom/geombuilder/src/TGeoTrd2Editor.cxx`** -> AI Confidence: **99.31%**
1019. **`geom/geombuilder/src/TGeoTubeEditor.cxx`** -> AI Confidence: **99.31%**
1020. **`geom/geombuilder/src/TGeoVolumeEditor.cxx`** -> AI Confidence: **99.31%**
1021. **`geom/geomchecker/src/TGeoOverlap.cxx`** -> AI Confidence: **99.31%**
1022. **`geom/vecgeom/src/TGeoVGShape.cxx`** -> AI Confidence: **99.31%**
1023. **`geom/webviewer/src/RGeomData.cxx`** -> AI Confidence: **99.31%**
1024. **`graf2d/fitsio/src/TFITS.cxx`** -> AI Confidence: **99.31%**
1025. **`graf2d/gpad/src/TColorWheel.cxx`** -> AI Confidence: **99.31%**
1026. **`graf2d/gpad/src/TControlBar.cxx`** -> AI Confidence: **99.31%**
1027. **`graf2d/gpad/src/TPadPainter.cxx`** -> AI Confidence: **99.31%**
1028. **`graf2d/gpadv7/src/RAttrAggregation.cxx`** -> AI Confidence: **99.31%**
1029. **`graf2d/gpadv7/src/RAttrMap.cxx`** -> AI Confidence: **99.31%**
1030. **`graf2d/gpadv7/src/RCanvas.cxx`** -> AI Confidence: **99.31%**
1031. **`graf2d/gpadv7/src/TObjectDrawable.cxx`** -> AI Confidence: **99.31%**
1032. **`graf2d/graf/src/TCurlyArc.cxx`** -> AI Confidence: **99.31%**
1033. **`graf2d/graf/src/TMarker.cxx`** -> AI Confidence: **99.31%**
1034. **`graf2d/graf/src/TMathText.cxx`** -> AI Confidence: **99.31%**
1035. **`graf2d/graf/src/TTF.cxx`** -> AI Confidence: **99.31%**
1036. **`graf2d/graf/src/TWbox.cxx`** -> AI Confidence: **99.31%**
1037. **`graf2d/mathtext/src/fontembed.cxx`** -> AI Confidence: **99.31%**
1038. **`graf2d/win32gdk/src/TGWin32ProxyBase.cxx`** -> AI Confidence: **99.31%**
1039. **`graf2d/x11/src/GX11Gui.cxx`** -> AI Confidence: **99.31%**
1040. **`graf2d/x11ttf/src/TGX11TTF.cxx`** -> AI Confidence: **99.31%**
1041. **`graf3d/eve/src/TEveCaloData.cxx`** -> AI Confidence: **99.31%**
1042. **`graf3d/eve/src/TEveCaloVizEditor.cxx`** -> AI Confidence: **99.31%**
1043. **`graf3d/eve/src/TEveDigitSetEditor.cxx`** -> AI Confidence: **99.31%**
1044. **`graf3d/eve/src/TEveElement.cxx`** -> AI Confidence: **99.31%**
1045. **`graf3d/eve/src/TEveElementEditor.cxx`** -> AI Confidence: **99.31%**
1046. **`graf3d/eve/src/TEveGedEditor.cxx`** -> AI Confidence: **99.31%**
1047. **`graf3d/eve/src/TEveGeoNode.cxx`** -> AI Confidence: **99.31%**
1048. **`graf3d/eve/src/TEveGeoShape.cxx`** -> AI Confidence: **99.31%**
1049. **`graf3d/eve/src/TEveManager.cxx`** -> AI Confidence: **99.31%**
1050. **`graf3d/eve/src/TEvePointSet.cxx`** -> AI Confidence: **99.31%**
1051. **`graf3d/eve/src/TEvePolygonSetProjectedGL.cxx`** -> AI Confidence: **99.31%**
1052. **`graf3d/eve/src/TEveProjectionManager.cxx`** -> AI Confidence: **99.31%**
1053. **`graf3d/eve/src/TEveRGBAPaletteEditor.cxx`** -> AI Confidence: **99.31%**
1054. **`graf3d/eve/src/TEveTextEditor.cxx`** -> AI Confidence: **99.31%**
1055. **`graf3d/eve/src/TEveTrack.cxx`** -> AI Confidence: **99.31%**
1056. **`graf3d/eve/src/TEveTrackEditor.cxx`** -> AI Confidence: **99.31%**
1057. **`graf3d/eve/src/TEveTrans.cxx`** -> AI Confidence: **99.31%**
1058. **`graf3d/eve/src/TEveUtil.cxx`** -> AI Confidence: **99.31%**
1059. **`graf3d/eve/src/TEveViewer.cxx`** -> AI Confidence: **99.31%**
1060. **`graf3d/eve/src/TEveWindow.cxx`** -> AI Confidence: **99.31%**
1061. **`graf3d/eve7/src/REveBoxSet.cxx`** -> AI Confidence: **99.31%**
1062. **`graf3d/eve7/src/REveCalo.cxx`** -> AI Confidence: **99.31%**
1063. **`graf3d/eve7/src/REveCaloData.cxx`** -> AI Confidence: **99.31%**
1064. **`graf3d/eve7/src/REveDataCollection.cxx`** -> AI Confidence: **99.31%**
1065. **`graf3d/eve7/src/REveDataSimpleProxyBuilder.cxx`** -> AI Confidence: **99.31%**
1066. **`graf3d/eve7/src/REveElement.cxx`** -> AI Confidence: **99.31%**
1067. **`graf3d/eve7/src/REveGeoPolyShape.cxx`** -> AI Confidence: **99.31%**
1068. **`graf3d/eve7/src/REveGeoTopNode.cxx`** -> AI Confidence: **99.31%**
1069. **`graf3d/eve7/src/REveManager.cxx`** -> AI Confidence: **99.31%**
1070. **`graf3d/eve7/src/REvePointSet.cxx`** -> AI Confidence: **99.31%**
1071. **`graf3d/eve7/src/REveProjectionManager.cxx`** -> AI Confidence: **99.31%**
1072. **`graf3d/eve7/src/REveScene.cxx`** -> AI Confidence: **99.31%**
1073. **`graf3d/eve7/src/REveSelection.cxx`** -> AI Confidence: **99.31%**
1074. **`graf3d/eve7/src/REveTableInfo.cxx`** -> AI Confidence: **99.31%**
1075. **`graf3d/eve7/src/REveTrack.cxx`** -> AI Confidence: **99.31%**
1076. **`graf3d/eve7/src/REveTrans.cxx`** -> AI Confidence: **99.31%**
1077. **`graf3d/eve7/src/REveUtil.cxx`** -> AI Confidence: **99.31%**
1078. **`graf3d/eve7/src/REveViewer.cxx`** -> AI Confidence: **99.31%**
1079. **`graf3d/g3d/src/TAxis3D.cxx`** -> AI Confidence: **99.31%**
1080. **`graf3d/g3d/src/TGeometry.cxx`** -> AI Confidence: **99.31%**
1081. **`graf3d/g3d/src/TMarker3DBox.cxx`** -> AI Confidence: **99.31%**
1082. **`graf3d/g3d/src/TPolyLine3D.cxx`** -> AI Confidence: **99.31%**
1083. **`graf3d/g3d/src/TPolyMarker3D.cxx`** -> AI Confidence: **99.31%**
1084. **`graf3d/g3d/src/TShape.cxx`** -> AI Confidence: **99.31%**
1085. **`graf3d/gl/src/TF2GL.cxx`** -> AI Confidence: **99.31%**
1086. **`graf3d/gl/src/TGL5DDataSetEditor.cxx`** -> AI Confidence: **99.31%**
1087. **`graf3d/gl/src/TGLAutoRotator.cxx`** -> AI Confidence: **99.31%**
1088. **`graf3d/gl/src/TGLCameraGuide.cxx`** -> AI Confidence: **99.31%**
1089. **`graf3d/gl/src/TGLClip.cxx`** -> AI Confidence: **99.31%**
1090. **`graf3d/gl/src/TGLContext.cxx`** -> AI Confidence: **99.31%**
1091. **`graf3d/gl/src/TGLCylinder.cxx`** -> AI Confidence: **99.31%**
1092. **`graf3d/gl/src/TGLFaceSet.cxx`** -> AI Confidence: **99.31%**
1093. **`graf3d/gl/src/TGLFormat.cxx`** -> AI Confidence: **99.31%**
1094. **`graf3d/gl/src/TGLManipSet.cxx`** -> AI Confidence: **99.31%**
1095. **`graf3d/gl/src/TGLObject.cxx`** -> AI Confidence: **99.31%**
1096. **`graf3d/gl/src/TGLOverlayButton.cxx`** -> AI Confidence: **99.31%**
1097. **`graf3d/gl/src/TGLPShapeObjEditor.cxx`** -> AI Confidence: **99.31%**
1098. **`graf3d/gl/src/TGLPadPainter.cxx`** -> AI Confidence: **99.31%**
1099. **`graf3d/gl/src/TGLPadUtils.cxx`** -> AI Confidence: **99.31%**
1100. **`graf3d/gl/src/TGLParametric.cxx`** -> AI Confidence: **99.31%**
1101. **`graf3d/gl/src/TGLPlot3D.cxx`** -> AI Confidence: **99.31%**
1102. **`graf3d/gl/src/TGLPlotPainter.cxx`** -> AI Confidence: **99.31%**
1103. **`graf3d/gl/src/TGLPolyLine.cxx`** -> AI Confidence: **99.31%**
1104. **`graf3d/gl/src/TGLScene.cxx`** -> AI Confidence: **99.31%**
1105. **`graf3d/gl/src/TGLSdfFontMaker.cxx`** -> AI Confidence: **99.31%**
1106. **`graf3d/gl/src/TGLUtil.cxx`** -> AI Confidence: **99.31%**
1107. **`graf3d/gl/src/TGLViewer.cxx`** -> AI Confidence: **99.31%**
1108. **`graf3d/gl/src/TGLViewerBase.cxx`** -> AI Confidence: **99.31%**
1109. **`graf3d/gl/src/TGLViewerEditor.cxx`** -> AI Confidence: **99.31%**
1110. **`graf3d/gl/src/TX11GL.cxx`** -> AI Confidence: **99.31%**
1111. **`graf3d/gl/src/gl2ps.cxx`** -> AI Confidence: **99.31%**
1112. **`graf3d/gviz3d/src/TStructNodeEditor.cxx`** -> AI Confidence: **99.31%**
1113. **`graf3d/gviz3d/src/TStructViewerGUI.cxx`** -> AI Confidence: **99.31%**
1114. **`graf3d/x3d/src/TViewerX3D.cxx`** -> AI Confidence: **99.31%**
1115. **`gui/browsable/src/RSysFile.cxx`** -> AI Confidence: **99.31%**
1116. **`gui/browsable/src/TDirectoryElement.cxx`** -> AI Confidence: **99.31%**
1117. **`gui/browserv7/src/RBrowser.cxx`** -> AI Confidence: **99.31%**
1118. **`gui/browserv7/src/RBrowserData.cxx`** -> AI Confidence: **99.31%**
1119. **`gui/browserv7/src/RBrowserTCanvasWidget.cxx`** -> AI Confidence: **99.31%**
1120. **`gui/browserv7/src/RFileDialog.cxx`** -> AI Confidence: **99.31%**
1121. **`gui/canvaspainter/src/RCanvasPainter.cxx`** -> AI Confidence: **99.31%**
1122. **`gui/cefdisplay/src/gui_handler.cxx`** -> AI Confidence: **99.31%**
1123. **`gui/cefdisplay/src/gui_handler_linux.cxx`** -> AI Confidence: **99.31%**
1124. **`gui/cefdisplay/src/simple_app.cxx`** -> AI Confidence: **99.31%**
1125. **`gui/fitpanel/src/TAdvancedGraphicsDialog.cxx`** -> AI Confidence: **99.31%**
1126. **`gui/fitpanelv7/src/RFitPanel.cxx`** -> AI Confidence: **99.31%**
1127. **`gui/ged/src/TAttFillEditor.cxx`** -> AI Confidence: **99.31%**
1128. **`gui/ged/src/TAttLineEditor.cxx`** -> AI Confidence: **99.31%**
1129. **`gui/ged/src/TAttMarkerEditor.cxx`** -> AI Confidence: **99.31%**
1130. **`gui/ged/src/TAttTextEditor.cxx`** -> AI Confidence: **99.31%**
1131. **`gui/ged/src/TAxisEditor.cxx`** -> AI Confidence: **99.31%**
1132. **`gui/ged/src/TF1Editor.cxx`** -> AI Confidence: **99.31%**
1133. **`gui/ged/src/TGedFrame.cxx`** -> AI Confidence: **99.31%**
1134. **`gui/ged/src/TH2Editor.cxx`** -> AI Confidence: **99.31%**
1135. **`gui/ged/src/TStyleManager.cxx`** -> AI Confidence: **99.31%**
1136. **`gui/gui/src/TGClient.cxx`** -> AI Confidence: **99.31%**
1137. **`gui/gui/src/TGIcon.cxx`** -> AI Confidence: **99.31%**
1138. **`gui/gui/src/TGImageMap.cxx`** -> AI Confidence: **99.31%**
1139. **`gui/gui/src/TGPasswdDialog.cxx`** -> AI Confidence: **99.31%**
1140. **`gui/gui/src/TGPicture.cxx`** -> AI Confidence: **99.31%**
1141. **`gui/gui/src/TGSplitFrame.cxx`** -> AI Confidence: **99.31%**
1142. **`gui/gui/src/TGTable.cxx`** -> AI Confidence: **99.31%**
1143. **`gui/gui/src/TGTableCell.cxx`** -> AI Confidence: **99.31%**
1144. **`gui/gui/src/TGToolBar.cxx`** -> AI Confidence: **99.31%**
1145. **`gui/gui/src/TRootGuiFactory.cxx`** -> AI Confidence: **99.31%**
1146. **`gui/qt6webdisplay/rooturlschemehandler.cpp`** -> AI Confidence: **99.31%**
1147. **`gui/webdisplay/src/RWebWindow.cxx`** -> AI Confidence: **99.31%**
1148. **`gui/webgui6/src/TWebControlBar.cxx`** -> AI Confidence: **99.31%**
1149. **`hist/hbook/src/THbookFile.cxx`** -> AI Confidence: **99.31%**
1150. **`hist/hist/src/TAxis.cxx`** -> AI Confidence: **99.31%**
1151. **`hist/hist/src/TBackCompFitter.cxx`** -> AI Confidence: **99.31%**
1152. **`hist/hist/src/TF1Helper.cxx`** -> AI Confidence: **99.31%**
1153. **`hist/hist/src/TF1NormSum.cxx`** -> AI Confidence: **99.31%**
1154. **`hist/hist/src/TF2.cxx`** -> AI Confidence: **99.31%**
1155. **`hist/hist/src/TF3.cxx`** -> AI Confidence: **99.31%**
1156. **`hist/hist/src/TFormula.cxx`** -> AI Confidence: **99.31%**
1157. **`hist/hist/src/TGraph2D.cxx`** -> AI Confidence: **99.31%**
1158. **`hist/hist/src/TGraphAsymmErrors.cxx`** -> AI Confidence: **99.31%**
1159. **`hist/hist/src/TGraphBentErrors.cxx`** -> AI Confidence: **99.31%**
1160. **`hist/hist/src/TGraphTime.cxx`** -> AI Confidence: **99.31%**
1161. **`hist/hist/src/THStack.cxx`** -> AI Confidence: **99.31%**
1162. **`hist/hist/src/THnChain.cxx`** -> AI Confidence: **99.31%**
1163. **`hist/hist/src/TProfile2Poly.cxx`** -> AI Confidence: **99.31%**
1164. **`hist/histv7/benchmark/hist_benchmark_engine.cxx`** -> AI Confidence: **99.31%**
1165. **`interpreter/CppInterOp/unittests/CppInterOp/Utils.cpp`** -> AI Confidence: **99.31%**
1166. **`interpreter/cling/lib/Utils/AST.cpp`** -> AI Confidence: **99.31%**
1167. **`interpreter/cling/lib/Utils/PlatformPosix.cpp`** -> AI Confidence: **99.31%**
1168. **`interpreter/cling/lib/Utils/PlatformWin.cpp`** -> AI Confidence: **99.31%**
1169. **`interpreter/cling/tools/driver/cling.cpp`** -> AI Confidence: **99.31%**
1170. **`interpreter/llvm-project/clang/include/clang/AST/JSONNodeDumper.h`** -> AI Confidence: **99.31%**
1171. **`interpreter/llvm-project/clang/include/clang/AST/RecursiveASTVisitor.h`** -> AI Confidence: **99.31%**
1172. **`interpreter/llvm-project/clang/include/clang/AST/StmtVisitor.h`** -> AI Confidence: **99.31%**
1173. **`interpreter/llvm-project/clang/include/clang/Basic/ObjCRuntime.h`** -> AI Confidence: **99.31%**
1174. **`interpreter/llvm-project/clang/include/clang/Basic/PartialDiagnostic.h`** -> AI Confidence: **99.31%**
1175. **`interpreter/llvm-project/clang/tools/clang-extdef-mapping/ClangExtDefMapGen.cpp`** -> AI Confidence: **99.31%**
1176. **`interpreter/llvm-project/clang/tools/clang-format/ClangFormat.cpp`** -> AI Confidence: **99.31%**
1177. **`interpreter/llvm-project/clang/tools/clang-fuzzer/handle-llvm/handle_llvm.cpp`** -> AI Confidence: **99.31%**
1178. **`interpreter/llvm-project/clang/tools/clang-installapi/Options.cpp`** -> AI Confidence: **99.31%**
1179. **`interpreter/llvm-project/clang/tools/clang-nvlink-wrapper/ClangNVLinkWrapper.cpp`** -> AI Confidence: **99.31%**
1180. **`interpreter/llvm-project/clang/tools/clang-offload-bundler/ClangOffloadBundler.cpp`** -> AI Confidence: **99.31%**
1181. **`interpreter/llvm-project/clang/tools/clang-offload-packager/ClangOffloadPackager.cpp`** -> AI Confidence: **99.31%**
1182. **`interpreter/llvm-project/clang/tools/clang-refactor/TestSupport.cpp`** -> AI Confidence: **99.31%**
1183. **`interpreter/llvm-project/clang/tools/clang-repl/ClangRepl.cpp`** -> AI Confidence: **99.31%**
1184. **`interpreter/llvm-project/clang/tools/clang-scan-deps/ClangScanDeps.cpp`** -> AI Confidence: **99.31%**
1185. **`interpreter/llvm-project/clang/tools/clang-sycl-linker/ClangSYCLLinker.cpp`** -> AI Confidence: **99.31%**
1186. **`interpreter/llvm-project/clang/tools/diagtool/ShowEnabledWarnings.cpp`** -> AI Confidence: **99.31%**
1187. **`interpreter/llvm-project/clang/tools/diagtool/TreeView.cpp`** -> AI Confidence: **99.31%**
1188. **`interpreter/llvm-project/clang/tools/driver/cc1_main.cpp`** -> AI Confidence: **99.31%**
1189. **`interpreter/llvm-project/clang/tools/driver/cc1as_main.cpp`** -> AI Confidence: **99.31%**
1190. **`interpreter/llvm-project/clang/tools/driver/driver.cpp`** -> AI Confidence: **99.31%**
1191. **`interpreter/llvm-project/clang/tools/libclang/CIndex.cpp`** -> AI Confidence: **99.31%**
1192. **`interpreter/llvm-project/clang/tools/libclang/CIndexDiagnostic.cpp`** -> AI Confidence: **99.31%**
1193. **`interpreter/llvm-project/clang/tools/libclang/CIndexHigh.cpp`** -> AI Confidence: **99.31%**
1194. **`interpreter/llvm-project/clang/tools/libclang/CXIndexDataConsumer.cpp`** -> AI Confidence: **99.31%**
1195. **`interpreter/llvm-project/clang/tools/libclang/CXSourceLocation.cpp`** -> AI Confidence: **99.31%**
1196. **`interpreter/llvm-project/clang/tools/libclang/CXType.cpp`** -> AI Confidence: **99.31%**
1197. **`interpreter/llvm-project/clang/utils/TableGen/ClangAttrEmitter.cpp`** -> AI Confidence: **99.31%**
1198. **`interpreter/llvm-project/clang/utils/TableGen/ClangDiagnosticsEmitter.cpp`** -> AI Confidence: **99.31%**
1199. **`interpreter/llvm-project/clang/utils/TableGen/ClangOptionDocEmitter.cpp`** -> AI Confidence: **99.31%**
1200. **`interpreter/llvm-project/clang/utils/TableGen/ClangSyntaxEmitter.cpp`** -> AI Confidence: **99.31%**
1201. **`interpreter/llvm-project/clang/utils/TableGen/RISCVVEmitter.cpp`** -> AI Confidence: **99.31%**
1202. **`interpreter/llvm-project/llvm/examples/BrainF/BrainF.cpp`** -> AI Confidence: **99.31%**
1203. **`interpreter/llvm-project/llvm/examples/IRTransforms/SimplifyCFG.cpp`** -> AI Confidence: **99.31%**
1204. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/BuildingAJIT/Chapter1/toy.cpp`** -> AI Confidence: **99.31%**
1205. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/BuildingAJIT/Chapter2/toy.cpp`** -> AI Confidence: **99.31%**
1206. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/BuildingAJIT/Chapter3/toy.cpp`** -> AI Confidence: **99.31%**
1207. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/BuildingAJIT/Chapter4/toy.cpp`** -> AI Confidence: **99.31%**
1208. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter2/toy.cpp`** -> AI Confidence: **99.31%**
1209. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter3/toy.cpp`** -> AI Confidence: **99.31%**
1210. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter4/toy.cpp`** -> AI Confidence: **99.31%**
1211. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter5/toy.cpp`** -> AI Confidence: **99.31%**
1212. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter6/toy.cpp`** -> AI Confidence: **99.31%**
1213. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter7/toy.cpp`** -> AI Confidence: **99.31%**
1214. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter8/toy.cpp`** -> AI Confidence: **99.31%**
1215. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter9/toy.cpp`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `interpreter/llvm-project/llvm/include/llvm/BinaryFormat/COFF.h` -> **0.8459%** Exposure
- `js/modules/base/svg2pdf.mjs` -> **0.0483%** Exposure
- `graf2d/mathtext/src/table/adobeglyphlist.h` -> **0.0156%** Exposure
- `graf2d/postscript/src/AdobeGlyphList.h` -> **0.0156%** Exposure
- `math/mathmore/src/VavilovAccurate.cxx` -> **0.0005%** Exposure
### Exploit Generation Surface
- `bindings/distrdf/python/DistRDF/Backends/Base.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Backends/Dask/Backend.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Backends/Utils.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/HeadNode.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Node.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `bindings/pyroot/cppyy/cppyy/bench/support.py` -> **100.0%** Exposure
- `bindings/pyroot/cppyy/cppyy/python/cppyy/ll.py` -> **100.0%** Exposure
- `bindings/pyroot/pythonizations/python/ROOT/_rootcli.py` -> **100.0%** Exposure
- `documentation/primer/macros/runall.py` -> **100.0%** Exposure
- `etc/dictpch/makepch.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `builtins/zstd/common/bitstream.h` -> **10.0%** Exposure
- `core/base/inc/TROOT.h` -> **10.0%** Exposure
- `core/base/inc/TSystem.h` -> **10.0%** Exposure
- `core/base/src/TPluginManager.cxx` -> **10.0%** Exposure
- `core/clingutils/res/TClingUtils.h` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `bindings/distrdf/python/DistRDF/Backends/Base.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Backends/Dask/Backend.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Backends/Spark/Backend.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Backends/Utils.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/HeadNode.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `157` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `65694` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ui5/eve7/controller/Lego.controller.js` (JAVASCRIPT) -> Cumulative Risk: **983.31**
- **Archetype:** `file_cluster_4` (Distance: 14.213 IQR)
- **Magnitude:** 216.98 | **LOC:** 121 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `drawHist` (Impact: 21.6), `onInit` (Impact: 13.7), `onResize` (Impact: 8.8)

### 2. `ui5/canv/controller/CanvasPanel.controller.js` (JAVASCRIPT) -> Cumulative Risk: **960.04**
- **Archetype:** `file_cluster_4` (Distance: 14.988 IQR)
- **Magnitude:** 449.02 | **LOC:** 175 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `onResizeTimeout` (Impact: 83.7), `resizeBrowser` (Impact: 69.9), `setFixedSize` (Impact: 36.8)

### 3. `ui5/eve7/controller/Summary.controller.js` (JAVASCRIPT) -> Cumulative Risk: **959.9**
- **Archetype:** `file_cluster_4` (Distance: 13.576 IQR)
- **Magnitude:** 772.02 | **LOC:** 415 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `processHighlight` (Impact: 127.5), `createSummaryModel` (Impact: 49.0), `BrowseElement` (Impact: 33.6)

### 4. `ui5/eve7/controller/GL.controller.js` (JAVASCRIPT) -> Cumulative Risk: **959.26**
- **Archetype:** `file_cluster_11` (Distance: 14.067 IQR)
- **Magnitude:** 473.62 | **LOC:** 286 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setupManagerAndViewType` (Impact: 37.9), `checkViewReady` (Impact: 32.8), `onEveManagerInit` (Impact: 18.1)

### 5. `ui5/eve7/controller/Main.controller.js` (JAVASCRIPT) -> Cumulative Risk: **953.98**
- **Archetype:** `file_cluster_8` (Distance: 13.075 IQR)
- **Magnitude:** 515.58 | **LOC:** 423 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `removeView` (Impact: 40.6), `makeEveViewController` (Impact: 37.6), `updateViewers` (Impact: 27.3)

### 6. `ui5/geom/controller/GeomViewer.controller.js` (JAVASCRIPT) -> Cumulative Risk: **946.46**
- **Archetype:** `file_cluster_11` (Distance: 15.296 IQR)
- **Magnitude:** 1773.58 | **LOC:** 793 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `onWebsocketMsg` (Impact: 88.9), `checkDrawMsg` (Impact: 85.1), `changeNodeVisibilityOffline` (Impact: 78.2)

### 7. `config/rootssh` (SHELL) -> Cumulative Risk: **936.17**
- **Archetype:** `file_cluster_4` (Distance: 14.558 IQR)
- **Magnitude:** 262.0 | **LOC:** 182 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Algorithmic Dos (99.9993%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 63.6), `Anonymous_Block` (Impact: 45.7), `Anonymous_Block_[Truncated]` (Impact: 27.2)

### 8. `ui5/canv/controller/Canvas.controller.js` (JAVASCRIPT) -> Cumulative Risk: **936.16**
- **Archetype:** `file_cluster_4` (Distance: 14.104 IQR)
- **Magnitude:** 1323.44 | **LOC:** 801 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `onFileMenuAction` (Impact: 161.8), `showLeftArea` (Impact: 138.3), `closeMethodDialog` (Impact: 112.5)

### 9. `js/modules/hist/RPavePainter.mjs` (JAVASCRIPT) -> Cumulative Risk: **932.41**
- **Archetype:** `file_cluster_4` (Distance: 13.897 IQR)
- **Magnitude:** 463.6 | **LOC:** 284 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `drawContent` (Impact: 107.4), `drawPave` (Impact: 59.1), `sizeChanged` (Impact: 41.0)

### 10. `js/modules/draw/TSplinePainter.mjs` (JAVASCRIPT) -> Cumulative Risk: **919.88**
- **Archetype:** `file_cluster_13` (Distance: 13.247 IQR)
- **Magnitude:** 466.38 | **LOC:** 338 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `processTooltipEvent` (Impact: 117.9), `redraw` (Impact: 56.6), `draw` (Impact: 49.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `builtins/glew/src/glew.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.929 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.533 IQR)
- **Top Global Matches:** file_cluster_8: 14.929, file_cluster_7: 15.321, file_cluster_0: 15.412
- **Magnitude:** 128986.48 | **LOC:** 28582 | **CtrlFlow:** 96.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (77.5937%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3594`, `structural_boundaries: 148`, `args: 9`, `func_start: 124`
* *Risk/State:* `state_mutation: 8363`
* *Architecture:* `api: 918`, `import: 3`
* *Defense:* `safety: 6`, `immutability_locks: 1550`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wglew.h, stddef.h, osmesa.h, stdio.h, dlfcn.h, eglew.h, stdlib.h, AvailabilityMacros.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/minicern/src/zebra.f` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.119 IQR)
- **Top Global Matches:** file_cluster_8: 15.119, file_cluster_11: 15.155, file_cluster_0: 15.27
- **Magnitude:** 29761.08 | **LOC:** 7291 | **CtrlFlow:** 93.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 231
- **Risk Profile:** Cognitive Load (99.2376%), Tech Debt (11.6007%)
**Top Internal Functions/Classes:**
  * `MZLIFT` (Impact: 2511.5 | O(2^N) | DB: 104)
  * `MZPUSH` (Impact: 1983.2 | O(2^N) | DB: 116)
  * `MZIOCH` (Impact: 1846.2 | O(2^N) | DB: 139)
  * `RZOPEN` (Impact: 1399.7 | O(2^N) | DB: 231)
  * `RZREAD` (Impact: 1183.1 | O(2^N) | DB: 102)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2063`, `structural_boundaries: 144`, `args: 68`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 249`, `high_risk_execution: 855`, `state_mutation: 7350`, `orphaned_logic: 28`
* *Architecture:* `io: 98`, `api: 66`, `import: 1`
* *Defense:* `safety: 90`, `immutability_locks: 89`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `net/http/civetweb/civetweb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.243 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.335 IQR)
- **Top Global Matches:** file_cluster_8: 15.243, file_cluster_13: 15.374, file_cluster_11: 15.396
- **Magnitude:** 23998.74 | **LOC:** 23203 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 374
- **Risk Profile:** Cognitive Load (93.4368%), Tech Debt (13.3066%)
**Top Internal Functions/Classes:**
  * `dav_move_file` (Impact: 6866.6 | O(2^N) | DB: 374)
  * `mg_start_worker_thread` (Impact: 910.5 | O(2^N) | DB: 70)
  * `connect_socket` (Impact: 668.2 | O(N^5) | DB: 71)
  * `interpret_uri` (Impact: 474.6 | O(N^6) | DB: 50)
  * `read_auth_file` (Impact: 389.9 | O(2^N) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3044`, `structural_boundaries: 1491`, `args: 294`, `func_start: 256`, `class_start: 225`
* *Risk/State:* `safety_bypasses: 89`, `high_risk_execution: 4`, `state_mutation: 6290`, `dead_code: 10`, `planned_debt: 27`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 31`
* *Architecture:* `io: 141`, `api: 1598`, `concurrency: 104`, `import: 86`
* *Defense:* `safety: 169`, `doc: 3`, `sync_locks: 17`, `immutability_locks: 401`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` dh.h, sendfile.h, dlfcn.h, handle_form.inl, inttypes.h, md5.inl, signal.h, prctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `math/matrix/src/TDecompSparse.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.305 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.711 IQR)
- **Top Global Matches:** file_cluster_8: 16.305, file_cluster_7: 16.339, file_cluster_13: 16.532
- **Magnitude:** 18475.32 | **LOC:** 2730 | **CtrlFlow:** 94.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 379
- **Risk Profile:** Cognitive Load (38.8749%), Tech Debt (60.7371%)
**Top Internal Functions/Classes:**
  * `TDecompSparse::Factor_sub2` (Impact: 4057.1 | O(2^N) | DB: 379)
  * `TDecompSparse::Factor` (Impact: 1762.5 | O(2^N) | DB: 99)
  * `TDecompSparse::InitPivot_sub2` (Impact: 1404.5 | O(N^6) | DB: 219)
  * `TDecompSparse::InitPivot_sub1` (Impact: 1073.7 | O(2^N) | DB: 94)
  * `TDecompSparse::InitPivot` (Impact: 1026.8 | O(2^N) | DB: 71)
    * *Intent:* // set initial value of "Treat As Zero" parameter
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 704`, `structural_boundaries: 45`, `args: 54`, `func_start: 28`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 4777`, `fragile_debt: 6`, `duplicate_logic: 7`, `orphaned_logic: 20`
* *Architecture:* `import: 2`
* *Defense:* `doc: 762`, `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TMath.h, TDecompSparse.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `math/minuit/src/TMinuit.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.455 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.054 IQR)
- **Top Global Matches:** file_cluster_7: 16.455, file_cluster_8: 16.48, file_cluster_13: 16.582
- **Magnitude:** 17317.52 | **LOC:** 7899 | **CtrlFlow:** 90.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 200
- **Risk Profile:** Cognitive Load (39.2579%), Tech Debt (47.6182%)
**Top Internal Functions/Classes:**
  * `TMinuit::mnexcm` (Impact: 1526.6 | O(N^6) | DB: 155)
  * `TMinuit::mnset` (Impact: 585.6 | O(N^3) | DB: 91)
  * `TMinuit::mncont` (Impact: 578.3 | O(N^6) | DB: 147)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Transform FCN t...
  * `TMinuit::mnline` (Impact: 488.9 | O(N^4) | DB: 135)
  * `TMinuit::mncros` (Impact: 442.3 | O(N^3) | DB: 200)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1908`, `structural_boundaries: 210`, `args: 102`, `func_start: 76`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 8749`, `dead_code: 22`, `planned_debt: 3`, `fragile_debt: 7`, `duplicate_logic: 5`, `orphaned_logic: 70`
* *Architecture:* `import: 10`
* *Defense:* `safety: 7`, `doc: 2529`, `test: 2`, `immutability_locks: 135`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` TPluginManager.h, atomic, cstdlib, TClass.h, TList.h, cstdio, TMinuit.h, TMath.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.018 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.689 IQR)
- **Top Global Matches:** file_cluster_8: 16.018, file_cluster_13: 16.045, file_cluster_11: 16.089
- **Magnitude:** 17221.04 | **LOC:** 1162 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 618
- **Risk Profile:** Cognitive Load (64.8682%), Tech Debt (23.5221%)
**Top Internal Functions/Classes:**
  * `inheritsFrom` (Impact: 12545.9 | O(2^N) | DB: 618)
    * *Intent:* /// inheritsFrom - Indicates whether all instructions in one class also belong /// to another class....
  * `DisassemblerTables::emitContextTable` (Impact: 994.4 | O(N^4) | DB: 169)
  * `DisassemblerTables::emitModRMDecision` (Impact: 440.7 | O(N^6) | DB: 31)
  * `DisassemblerTables::setTableFields` (Impact: 111.4 | O(N^6) | DB: 12)
  * `getDecisionType` (Impact: 99.0 | O(N^6) | DB: 28)
    * *Intent:* /// getDecisionType - Determines whether a ModRM decision with 255 entries can /// be compacted by e...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 898`, `structural_boundaries: 188`, `args: 84`, `func_start: 14`
* *Risk/State:* `state_mutation: 2737`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `import: 8`
* *Defense:* `safety: 4`, `doc: 45`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ErrorHandling.h, X86ModRMFilters.h, SmallVector.h, Format.h, X86DisassemblerShared.h, X86DisassemblerTables.h, map, raw_ostream.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `roottest/scripts/Rules.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.698 IQR)
- **Top Global Matches:** file_cluster_17: 11.698, file_cluster_8: 12.063, file_cluster_11: 12.066
- **Magnitude:** 16450.92 | **LOC:** 907 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (81.9851%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 136`, `args: 32`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 87`, `dead_code: 8`
* *Architecture:* `io: 102`, `api: 55`, `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Common.mk, Makefile.comp, $(wildcard, FixCling.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graf2d/win32gdk/src/TGWin32.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_7` (Drift: 17.403 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.533 IQR)
- **Top Global Matches:** file_cluster_7: 17.403, file_cluster_13: 17.487, file_cluster_8: 17.515
- **Magnitude:** 15956.98 | **LOC:** 7848 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 609
- **Risk Profile:** Cognitive Load (46.0579%), Tech Debt (98.9255%)
**Top Internal Functions/Classes:**
  * `TGWin32::MapGCValues` (Impact: 835.0 | O(N^6) | DB: 152)
  * `TGWin32::RequestString` (Impact: 606.5 | O(N^6) | DB: 77)
  * `TGWin32::UpdateMarkerStyle` (Impact: 558.6 | O(N^6) | DB: 609)
  * `TGWin32::MapEvent` (Impact: 405.9 | O(N^3) | DB: 214)
  * `TGWin32::RequestLocator` (Impact: 351.6 | O(N^6) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1320`, `structural_boundaries: 432`, `args: 388`, `func_start: 242`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 7192`, `dead_code: 28`, `fragile_debt: 1`, `duplicate_logic: 22`, `orphaned_logic: 207`
* *Architecture:* `io: 7`, `api: 1`, `import: 34`
* *Defense:* `doc: 7155`, `sync_locks: 1`, `immutability_locks: 48`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` TApplication.h, RStipples.h, TGWin32.h, TObjString.h, process.h, TSystem.h, TStyle.h, TEnv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graf2d/asimage/src/TASImage.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.938 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.904 IQR)
- **Top Global Matches:** file_cluster_7: 16.938, file_cluster_8: 17.008, file_cluster_13: 17.027
- **Magnitude:** 13350.7 | **LOC:** 6859 | **CtrlFlow:** 79.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 659
- **Risk Profile:** Cognitive Load (47.0725%), Tech Debt (33.2452%)
**Top Internal Functions/Classes:**
  * `TASImage::ReadImage` (Impact: 2962.2 | O(N^6) | DB: 659)
  * `TASImage::CopyArea` (Impact: 613.8 | O(N^6) | DB: 39)
  * `TASImage::DrawDashZLine` (Impact: 375.3 | O(N^6) | DB: 96)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Return a pointe...
  * `TASImage::DrawDashZTLine` (Impact: 364.7 | O(N^6) | DB: 76)
  * `TASImage::DrawLineInternal` (Impact: 341.2 | O(N^6) | DB: 67)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1197`, `structural_boundaries: 312`, `args: 173`, `func_start: 95`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 12`, `state_mutation: 5369`, `dead_code: 4`, `duplicate_logic: 13`, `orphaned_logic: 42`
* *Architecture:* `io: 10`, `import: 32`
* *Defense:* `safety: 1`, `doc: 3156`, `immutability_locks: 76`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` TArrayL.h, TVirtualPad.h, Xlib.h, Windows4root.h, TPluginManager.h, TFrame.h, TVirtualPS.h, TSystem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `math/mathcore/src/TKDTree.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.839 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.694 IQR)
- **Top Global Matches:** file_cluster_13: 16.839, file_cluster_11: 16.885, file_cluster_7: 16.983
- **Magnitude:** 13288.97 | **LOC:** 1248 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (35.8353%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 103`, `args: 72`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 780`, `dead_code: 15`
* *Architecture:* `import: 5`
* *Defense:* `doc: 635`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` TString.h, cstring, TRandom.h, TKDTree.h, limits
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/spectrum/src/TSpectrum2Fit.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.437 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 3.826 IQR)
- **Top Global Matches:** file_cluster_7: 16.437, file_cluster_8: 16.465, file_cluster_13: 16.598
- **Magnitude:** 13145.3 | **LOC:** 5877 | **CtrlFlow:** 93.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 603
- **Risk Profile:** Cognitive Load (46.3116%), Tech Debt (19.9585%)
**Top Internal Functions/Classes:**
  * `TSpectrum2Fit::FitAwmi` (Impact: 1926.8 | O(N^6) | DB: 603)
    * *Intent:* /// nfound = s->SearchHighRes(source, dest, nbinsx, nbinsy, 2, 2, kTRUE, 100, kFALSE, 3); /// printf...
  * `TSpectrum2Fit::FitStiefel` (Impact: 1788.0 | O(N^6) | DB: 534)
    * *Intent:* /// printf("Found %d candidate peaks\n",nfound); /// Bool_t *FixPosX = new Bool_t[nfound]; /// Bool_...
  * `TSpectrum2Fit::Shape2` (Impact: 340.1 | O(N^6) | DB: 51)
  * `TSpectrum2Fit::Dersigmax` (Impact: 213.2 | O(N^6) | DB: 45)
  * `TSpectrum2Fit::Dersigmay` (Impact: 213.2 | O(N^6) | DB: 45)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1068`, `structural_boundaries: 73`, `args: 205`, `func_start: 51`
* *Risk/State:* `state_mutation: 6987`, `dead_code: 27`, `duplicate_logic: 2`, `orphaned_logic: 48`
* *Architecture:* `import: 2`
* *Defense:* `doc: 2036`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TMath.h, TSpectrum2Fit.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/histpainter/src/THistPainter.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.725 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.322 IQR)
- **Top Global Matches:** file_cluster_13: 16.725, file_cluster_8: 16.752, file_cluster_7: 16.782
- **Magnitude:** 11321.32 | **LOC:** 11904 | **CtrlFlow:** 90.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 323
- **Risk Profile:** Cognitive Load (41.8204%), Tech Debt (17.5301%)
**Top Internal Functions/Classes:**
  * `THistPainter::PaintColorLevelsFast` (Impact: 689.4 | O(2^N) | DB: 84)
  * `THistPainter::PaintContour` (Impact: 681.9 | O(N^5) | DB: 209)
  * `THistPainter::MakeChopt` (Impact: 608.4 | O(N^3) | DB: 323)
  * `THistPainter::ShowProjection3` (Impact: 593.1 | O(N^6) | DB: 261)
  * `THistPainter::Paint` (Impact: 385.4 | O(N^6) | DB: 51)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1230`, `structural_boundaries: 137`, `args: 247`, `func_start: 33`
* *Risk/State:* `high_risk_execution: 58`, `state_mutation: 5462`, `dead_code: 6`, `duplicate_logic: 2`, `orphaned_logic: 30`
* *Architecture:* `import: 55`
* *Defense:* `safety: 3`, `doc: 996`, `immutability_locks: 17`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` cctype, TPluginManager.h, Hoption.h, TFrame.h, TPoints.h, TMultiGraph.h, TPie.h, iostream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tree/treeplayer/src/TTreeFormula.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.824 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.283 IQR)
- **Top Global Matches:** file_cluster_13: 16.824, file_cluster_11: 16.926, file_cluster_7: 16.965
- **Magnitude:** 10939.42 | **LOC:** 5986 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 476
- **Risk Profile:** Cognitive Load (48.9438%), Tech Debt (33.2661%)
**Top Internal Functions/Classes:**
  * `TTreeFormula::GetRealInstance` (Impact: 3460.3 | O(N^6) | DB: 476)
  * `TTreeFormula::LoadCurrentDim` (Impact: 755.7 | O(N^6) | DB: 109)
  * `TTreeFormula::ResetDimensions` (Impact: 411.1 | O(N^3) | DB: 63)
  * `TTreeFormula::RegisterDimensions` (Impact: 286.8 | O(N^6) | DB: 50)
  * `TTreeFormula::DefineAlternate` (Impact: 270.9 | O(N^6) | DB: 44)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1591`, `structural_boundaries: 289`, `args: 122`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4847`, `dead_code: 26`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 9`, `orphaned_logic: 13`
* *Architecture:* `api: 1`, `import: 41`
* *Defense:* `safety: 14`, `doc: 1139`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` cctype, algorithm, TLeafElement.h, TBranchObject.h, TList.h, TArrayI.h, cmath, sstream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/histpainter/src/TPainter3dAlgorithms.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.504 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.561 IQR)
- **Top Global Matches:** file_cluster_7: 16.504, file_cluster_8: 16.52, file_cluster_13: 16.602
- **Magnitude:** 10616.94 | **LOC:** 5780 | **CtrlFlow:** 90.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 182
- **Risk Profile:** Cognitive Load (41.1902%), Tech Debt (27.3676%)
**Top Internal Functions/Classes:**
  * `TPainter3dAlgorithms::IsoSurface` (Impact: 1343.2 | O(N^6) | DB: 154)
  * `TPainter3dAlgorithms::ImplicitFunction` (Impact: 924.9 | O(N^6) | DB: 182)
  * `TPainter3dAlgorithms::MarchingCube` (Impact: 916.7 | O(N^6) | DB: 71)
  * `TPainter3dAlgorithms::ZDepth` (Impact: 842.4 | O(N^6) | DB: 106)
  * `TPainter3dAlgorithms::SurfaceSpherical` (Impact: 521.9 | O(N^6) | DB: 91)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 775`, `structural_boundaries: 84`, `args: 52`, `func_start: 29`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 3738`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 26`
* *Architecture:* `import: 14`
* *Defense:* `doc: 1029`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` TF3.h, TVirtualPad.h, TView.h, TH1.h, Hoption.h, THLimitsFinder.h, cstdlib, TStyle.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graf2d/gpad/src/TPad.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 17.601 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.913 IQR)
- **Top Global Matches:** file_cluster_13: 17.601, file_cluster_7: 17.657, file_cluster_8: 17.781
- **Magnitude:** 10406.68 | **LOC:** 7683 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 786
- **Risk Profile:** Cognitive Load (47.8924%), Tech Debt (30.645%)
**Top Internal Functions/Classes:**
  * `TPad::Close` (Impact: 3438.0 | O(N^6) | DB: 786)
  * `TPad::PaintHatches` (Impact: 886.4 | O(N^6) | DB: 182)
  * `TPad::ClipPolygon` (Impact: 258.3 | O(N^3) | DB: 93)
  * `TPad::PlaceBox` (Impact: 125.0 | O(N^3) | DB: 37)
  * `TPad::FillCollideGridTH1` (Impact: 107.8 | O(N^3) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1040`, `structural_boundaries: 222`, `args: 237`, `func_start: 103`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4656`, `dead_code: 16`, `duplicate_logic: 6`, `orphaned_logic: 37`
* *Architecture:* `import: 51`
* *Defense:* `safety: 1`, `doc: 3548`, `immutability_locks: 72`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` TPaveText.h, TBaseClass.h, TFile.h, TPluginManager.h, TFrame.h, TVirtualPS.h, TMultiGraph.h, TBrowser.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/minicern/src/hbook.f` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.608 IQR)
- **Top Global Matches:** file_cluster_8: 14.608, file_cluster_11: 14.768, file_cluster_0: 14.839
- **Magnitude:** 10171.86 | **LOC:** 4127 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 162
- **Risk Profile:** Cognitive Load (85.607%), Tech Debt (12.0567%)
**Top Internal Functions/Classes:**
  * `HGNT2` (Impact: 969.1 | O(N^6) | DB: 162)
  * `HRIN` (Impact: 794.6 | O(2^N) | DB: 119)
  * `HPATH` (Impact: 560.2 | O(2^N) | DB: 65)
  * `HCDIR` (Impact: 379.9 | O(2^N) | DB: 73)
  * `HCX` (Impact: 285.3 | O(2^N) | DB: 49)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 716`, `structural_boundaries: 449`, `args: 56`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 126`, `state_mutation: 4359`, `orphaned_logic: 17`
* *Architecture:* `io: 20`, `api: 54`
* *Defense:* `safety: 78`, `immutability_locks: 73`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/modules/io.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.28%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.947 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.292 IQR)
- **Top Global Matches:** file_cluster_4: 14.947, file_cluster_11: 15.171, file_cluster_0: 15.228
- **Magnitude:** 10125.18 | **LOC:** 4213 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 106
- **Risk Profile:** Cognitive Load (63.3367%), Tech Debt (59.9117%)
**Top Internal Functions/Classes:**
  * `createMemberStreamer` (Impact: 2103.6 | O(2^N) | DB: 106)
  * `readBuffer` (Impact: 961.2 | O(N^6) | DB: 26)
  * `readTKey` (Impact: 848.9 | O(2^N) | DB: 105)
    * *Intent:* /** @summary read class version from I/O buffer */
  * `zip_inflate_codes` (Impact: 756.5 | O(2^N) | DB: 6)
    * *Intent:* /* Copyright (C) 1999 Masanao Izumo <iz@onicos.co.jp> * Version: 1.0.0.1 * LastModified: Dec 25 1999...
  * `R__unzip` (Impact: 515.1 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1074`, `structural_boundaries: 478`, `args: 248`, `func_start: 258`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1682`, `dead_code: 21`, `planned_debt: 1`, `duplicate_logic: 23`
* *Architecture:* `io: 10`, `api: 21`, `concurrency: 326`, `import: 5`
* *Defense:* `safety: 289`, `doc: 129`, `test: 1`, `immutability_locks: 179`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` zstd-js, zstd.mjs, core, fs, core.mjs, lzma.mjs, io, io.mjs
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `core/meta/src/TClass.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 17.409 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.293 IQR)
- **Top Global Matches:** file_cluster_13: 17.409, file_cluster_11: 17.637, file_cluster_7: 17.652
- **Magnitude:** 10078.36 | **LOC:** 7593 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 704
- **Risk Profile:** Cognitive Load (47.9205%), Tech Debt (91.0277%)
**Top Internal Functions/Classes:**
  * `TClass::GetBaseClassOffset` (Impact: 2594.4 | O(N^6) | DB: 704)
    * *Intent:* // Now we a dot
  * `TClass::Init` (Impact: 2151.2 | O(2^N) | DB: 94)
  * `TDumpMembers::Inspect` (Impact: 370.0 | O(N^4) | DB: 89)
  * `TAutoInspector::Inspect` (Impact: 341.0 | O(N^6) | DB: 58)
    * *Intent:* // The class is not loaded, hence it is 'emulated' and the main source of
  * `TBuildRealData::Inspect` (Impact: 272.1 | O(N^6) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 817`, `structural_boundaries: 410`, `args: 193`, `func_start: 100`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 3`, `state_mutation: 3395`, `dead_code: 24`, `planned_debt: 2`, `duplicate_logic: 19`, `orphaned_logic: 37`
* *Architecture:* `io: 4`, `api: 6`, `import: 74`
* *Defense:* `safety: 24`, `doc: 3378`, `sync_locks: 3`, `immutability_locks: 151`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` string, TVirtualPad.h, cctype, Windows4Root.h, TObjString.h, TBaseClass.h, TClassMenuItem.h, TSpinLockGuard.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/spectrum/src/TSpectrum2Transform.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.374 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 3.963 IQR)
- **Top Global Matches:** file_cluster_7: 16.374, file_cluster_8: 16.392, file_cluster_13: 16.461
- **Magnitude:** 9946.56 | **LOC:** 2788 | **CtrlFlow:** 95.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 332
- **Risk Profile:** Cognitive Load (40.3253%), Tech Debt (18.4165%)
**Top Internal Functions/Classes:**
  * `TSpectrum2Transform::General2` (Impact: 1931.2 | O(N^6) | DB: 332)
  * `TSpectrum2Transform::FourCos2` (Impact: 799.7 | O(N^6) | DB: 136)
  * `TSpectrum2Transform::Transform` (Impact: 721.0 | O(N^5) | DB: 180)
    * *Intent:* /// To execute this example, do /// /// `root > .x Transform2.C` /// /// ~~~ {.cpp} /// void Transfo...
  * `TSpectrum2Transform::FilterZonal` (Impact: 580.4 | O(N^4) | DB: 163)
    * *Intent:* /// `root > .x Filter2.C` /// /// ~~~ {.cpp} /// void Filter2() { /// Int_t i, j; /// Int_t nbinsx =...
  * `TSpectrum2Transform::Enhance` (Impact: 576.1 | O(N^4) | DB: 163)
    * *Intent:* /// \image html spectrum2transform_enhance_image002.jpg Fig. 2 Enhanced spectrum of the data from Fi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 827`, `structural_boundaries: 37`, `args: 22`, `func_start: 21`
* *Risk/State:* `state_mutation: 4124`, `dead_code: 19`, `duplicate_logic: 2`, `orphaned_logic: 18`
* *Architecture:* `import: 2`
* *Defense:* `doc: 864`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TSpectrum2Transform.h, TMath.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/modules/gpad/TFramePainter.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.943 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.685 IQR)
- **Top Global Matches:** file_cluster_4: 15.943, file_cluster_11: 16.001, file_cluster_17: 16.113
- **Magnitude:** 9613.98 | **LOC:** 3345 | **CtrlFlow:** 75.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (56.0218%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `zoom` (Impact: 1110.6 | O(2^N) | DB: 50)
  * `processFrameTooltipEvent` (Impact: 848.5 | O(N^5) | DB: 38)
  * `drawAxes` (Impact: 756.2 | O(2^N) | DB: 28)
  * `fillContextMenu` (Impact: 505.9 | O(N^6) | DB: 49)
  * `showContextMenu` (Impact: 322.7 | O(N^5) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1113`, `structural_boundaries: 370`, `args: 212`, `func_start: 154`, `class_start: 3`
* *Risk/State:* `state_mutation: 2750`, `dead_code: 13`
* *Architecture:* `io: 15`, `api: 16`, `concurrency: 146`, `import: 9`
* *Defense:* `safety: 340`, `doc: 117`, `immutability_locks: 132`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ObjectPainter.mjs, TAttLineHandler.mjs, menu.mjs, BasePainter.mjs, FontHandler.mjs, core.mjs, utils.mjs, d3.mjs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/modules/hist2d/TH2Painter.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.54 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.991 IQR)
- **Top Global Matches:** file_cluster_4: 14.54, file_cluster_8: 14.597, file_cluster_11: 14.671
- **Magnitude:** 9375.42 | **LOC:** 3845 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 87
- **Risk Profile:** Cognitive Load (80.0277%), Tech Debt (7.8146%)
**Top Internal Functions/Classes:**
  * `drawBinsCandle` (Impact: 1023.9 | O(N^6) | DB: 87)
  * `constructor` (Impact: 803.0 | O(N^5) | DB: 37)
  * `processTooltipEvent` (Impact: 768.3 | O(N^6) | DB: 46)
  * `drawPolyBins` (Impact: 549.7 | O(N^5) | DB: 39)
  * `buildHist2dContour` (Impact: 541.6 | O(N^5) | DB: 7)
    * *Intent:* /** @summary Build histogram contour lines
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1352`, `structural_boundaries: 404`, `args: 132`, `func_start: 128`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1867`, `dead_code: 7`, `planned_debt: 1`
* *Architecture:* `io: 35`, `api: 11`, `concurrency: 181`, `import: 7`
* *Defense:* `safety: 275`, `doc: 49`, `immutability_locks: 194`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ObjectPainter.mjs, colors.mjs, menu.mjs, BasePainter.mjs, THistPainter.mjs, core.mjs, d3.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/metacling/src/TCling.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.589 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.311 IQR)
- **Top Global Matches:** file_cluster_13: 16.589, file_cluster_7: 16.726, file_cluster_8: 16.846
- **Magnitude:** 9210.58 | **LOC:** 9765 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 14.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 110
- **Risk Profile:** Cognitive Load (46.912%), Tech Debt (99.972%)
**Top Internal Functions/Classes:**
  * `TCling::RegisterModule` (Impact: 1813.8 | O(2^N) | DB: 110)
  * `TCling::InspectMembers` (Impact: 848.7 | O(N^6) | DB: 103)
  * `GetClassSharedLibsForModule` (Impact: 438.5 | O(2^N) | DB: 16)
  * `TCling::TCling` (Impact: 390.3 | O(N^6) | DB: 78)
  * `TCling::ProcessLine` (Impact: 367.2 | O(N^6) | DB: 60)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Inject the modu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 863`, `structural_boundaries: 614`, `args: 484`, `func_start: 215`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 7`, `state_mutation: 2519`, `dead_code: 11`, `planned_debt: 3`, `fragile_debt: 24`, `duplicate_logic: 43`, `orphaned_logic: 135`
* *Architecture:* `io: 9`, `api: 3`, `import: 131`
* *Defense:* `safety: 32`, `doc: 5188`, `sync_locks: 7`, `immutability_locks: 389`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` TVirtualPad.h, TKey.h, RecordLayout.h, TFile.h, functional, dlfcn.h, TSystem.h, TGlobal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gui/guibuilder/src/TGuiBldDragManager.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.697 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.397 IQR)
- **Top Global Matches:** file_cluster_7: 16.697, file_cluster_13: 16.747, file_cluster_8: 16.808
- **Magnitude:** 8851.18 | **LOC:** 6332 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 552
- **Risk Profile:** Cognitive Load (47.5307%), Tech Debt (24.2339%)
**Top Internal Functions/Classes:**
  * `TGuiBldMenuDialog::Build` (Impact: 3434.3 | O(N^6) | DB: 552)
  * `TGuiBldDragManager::Drop` (Impact: 1341.7 | O(N^6) | DB: 325)
  * `TGuiBldDragManager::PlaceFrame` (Impact: 228.9 | O(N^6) | DB: 21)
  * `TGuiBldDragManager::CheckTargetAtPoint` (Impact: 161.4 | O(N^6) | DB: 26)
    * *Intent:* /// Handling of return/enter key pressing /// /// If on is kFALSE: /// If Return or Enter key was pr...
  * `TGuiBldDragManager::HandleMotion` (Impact: 78.8 | O(N^3) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1025`, `structural_boundaries: 321`, `args: 210`, `func_start: 115`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3122`, `dead_code: 12`, `planned_debt: 2`, `fragile_debt: 4`, `orphaned_logic: 24`
* *Architecture:* `api: 2`, `import: 41`
* *Defense:* `safety: 2`, `doc: 3448`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` TGTextEntry.h, TObjString.h, TBaseClass.h, TClassMenuItem.h, TGProgressBar.h, TGFontDialog.h, TSystem.h, TList.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `roofit/xroofit/src/xRooNode.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 19.028 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 6.445 IQR)
- **Top Global Matches:** file_cluster_11: 19.028, file_cluster_13: 19.087, file_cluster_17: 19.206
- **Magnitude:** 8607.02 | **LOC:** 12616 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 393
- **Risk Profile:** Cognitive Load (48.4343%), Tech Debt (22.2644%)
**Top Internal Functions/Classes:**
  * `xRooNode::_ShowVars_` (Impact: 2855.4 | O(N^6) | DB: 393)
    * *Intent:* //o->SetCall(o,"BlahBlah","Option_t*",-1); l->AddFirst(o);*/
  * `xRooNode::Browse` (Impact: 469.2 | O(N^6) | DB: 73)
  * `xRooNode::Checked` (Impact: 302.7 | O(N^6) | DB: 41)
  * `xRooNode::IntegralAndError` (Impact: 137.3 | O(N^6) | DB: 36)
  * `xRooNode::xRooNode` (Impact: 107.5 | O(N^6) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1470`, `structural_boundaries: 665`, `args: 278`, `func_start: 59`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4198`, `dead_code: 160`, `planned_debt: 10`, `fragile_debt: 3`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `api: 2`, `import: 96`
* *Defense:* `safety: 63`, `doc: 310`, `immutability_locks: 93`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 72):` RooDataSet.h, TPaveText.h, TKey.h, TFile.h, TFrame.h, TMultiGraph.h, coutCapture.h, TSystem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tmva/tmva/inc/TMVA/DNN/Architectures/TCudnn.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.736 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 7.142 IQR)
- **Top Global Matches:** file_cluster_13: 15.736, file_cluster_11: 15.911, file_cluster_8: 16.035
- **Magnitude:** 8483.66 | **LOC:** 1048 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.9729%), Tech Debt (8.8768%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 209`, `args: 156`, `func_start: 50`, `class_start: 4`
* *Risk/State:* `state_mutation: 661`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 2`, `doc: 174`, `immutability_locks: 154`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Functions.h, string, cudnn.h, GRULayer.h, utility, RConfigure.h, RNNLayer.h, CudaBuffers.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `bindings/pyroot/cppyy/cppyy/python/cppyy/_version.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tutorials/io/tree/tree200_temperature.C` (C) | Magnitude: 116.66 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, pointers: 80, state_mutation: 71, api: 19
- `interpreter/llvm-project/llvm/include/llvm/ProfileData/SymbolRemappingReader.h` (CPP) | Magnitude: 18.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 20, doc: 19, structural_boundaries: 8, func_start: 6
- `interpreter/llvm-project/llvm/include/llvm/Analysis/MustExecute.h` (CPP) | Magnitude: 263.1 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: doc: 242, state_mutation: 176, indent_spaces: 168, immutability_locks: 101
- `interpreter/llvm-project/llvm/include/llvm/Analysis/PtrUseVisitor.h` (CPP) | Magnitude: 120.78 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 66, indent_spaces: 65, doc: 48, args: 35
- `builtins/zstd/compress/zstd_fast.c` (C) | Magnitude: 1213.08 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 502, indent_spaces: 353, immutability_locks: 174, api: 160

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `tutorials/visualisation/graphics/triangles.C` (C) | Magnitude: 75.92 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 35, doc: 16, pointers: 16
- `core/cont/src/THashTable.cxx` (CPP) | Magnitude: 489.66 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 824, state_mutation: 319, indent_spaces: 226, pointers: 83
- `tutorials/hist/hist057_TExec_th1.C` (C) | Magnitude: 39.24 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 22, doc: 15, indent_spaces: 14, pointers: 12
- `core/cont/src/TExMap.cxx` (CPP) | Magnitude: 532.34 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 533, state_mutation: 305, indent_spaces: 228, branch: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `graf2d/asimage/src/libAfterImage/zlib/gzio.c` (C) | Magnitude: 2537.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 518, indent_spaces: 400, pointers: 277, branch: 154
- `math/mathcore/inc/Math/IFunction.h` (CPP) | Magnitude: 93.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 52, doc: 46, immutability_locks: 38
- `math/minuit2/src/MnLineSearch.cxx` (CPP) | Magnitude: 2429.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 870, indent_spaces: 532, branch: 138, dead_code: 25
- `math/smatrix/inc/Math/Dsinv.h` (CPP) | Magnitude: 249.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 165, indent_spaces: 76, branch: 20, structural_boundaries: 13
- `tmva/sofie/inc/TMVA/ROperator_Einsum.hxx` (CPP) | Magnitude: 835.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 411, indent_spaces: 234, branch: 71, structural_boundaries: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `config/thisroot.sh` (SHELL) | Magnitude: 640.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 193, state_mutation: 171, branch: 112, safety_bypasses: 39
- `interpreter/llvm-project/clang/utils/bash-autocomplete.sh` (SHELL) | Magnitude: 73.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 36, indent_spaces: 34, state_mutation: 30, safety_bypasses: 16
- `bindings/pyroot/cppyy/cppyy-backend/clingwrapper/src/precommondefs.h` (CPP) | Magnitude: 29.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 18, state_mutation: 12, reflection_metaprogramming: 9, branch: 6
- `builtins/zstd/common/huf.h` (CPP) | Magnitude: 54.06 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 82, structural_boundaries: 56, safety_bypasses: 52, macros: 37
- `interpreter/llvm-project/llvm/utils/crosstool/ARM/build-install-linux.sh` (SHELL) | Magnitude: 103.78 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, reflection_metaprogramming: 85, structural_boundaries: 46, branch: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `graf2d/win32gdk/gdk/src/iconv/gb12345.h` (CPP) | Magnitude: 29.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 15, branch: 5, structural_boundaries: 5
- `graf3d/gl/src/TGL5DDataSetEditor.cxx` (CPP) | Magnitude: 170.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 680, indent_spaces: 165, pointers: 132, structural_boundaries: 33
- `tree/dataframe/src/RJittedFilter.cxx` (CPP) | Magnitude: 55.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, pointers: 27, structural_boundaries: 19, func_start: 18
- `builtins/zstd/compress/zstd_compress_sequences.h` (C) | Magnitude: 44.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 27, immutability_locks: 24, indent_spaces: 23, safety: 12
- `tutorials/visualisation/gui/WorldMap.C` (C) | Magnitude: 95.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, api: 51, pointers: 43, state_mutation: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `graf2d/graf/src/TLatex.cxx` (CPP) | Magnitude: 7481.52 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 2932, indent_spaces: 2061, doc: 845, branch: 699
- `tutorials/visualisation/webcanv/latex_url.cxx` (CPP) | Magnitude: 18.8 | Delta: **0.268 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 16, state_mutation: 12, indent_spaces: 7, pointers: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `interpreter/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/Shared/WrapperFunctionUtils.h` (CPP) | Magnitude: 900.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 419, state_mutation: 356, structural_boundaries: 315, args: 181
- `math/experimental/genvectorx/inc/MathX/GenVectorX/Transform3D.h` (CPP) | Magnitude: 1068.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 641, state_mutation: 609, structural_boundaries: 304, immutability_locks: 178
- `interpreter/llvm-project/llvm/include/llvm/Support/Chrono.h` (CPP) | Magnitude: 112.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 79, indent_spaces: 63, doc: 43, state_mutation: 37
- `math/mathcore/inc/VectorizedTMath.h` (CPP) | Magnitude: 254.98 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 169, structural_boundaries: 137, indent_spaces: 122, doc: 24
- `tmva/tmva/src/DNN/Architectures/Reference/Initialization.hxx` (CPP) | Magnitude: 207.14 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 190, indent_spaces: 65, doc: 55, structural_boundaries: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tmva/tmva/src/DNN/Architectures/Cpu/Regularization.hxx` (CPP) | Magnitude: 142.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 125, indent_spaces: 83, doc: 47, pointers: 32
- `roottest/scripts/FixCling.mk` (MAKEFILE) | Magnitude: 37.82 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 29, state_mutation: 22, structural_boundaries: 17, branch: 6
- `tutorials/roofit/roostats/ModelInspector.py` (PYTHON) | Magnitude: 402.92 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 393, state_mutation: 76, branch: 40, structural_boundaries: 34
- `tutorials/roofit/roostats/StandardBayesianNumericalDemo.py` (PYTHON) | Magnitude: 10.28 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, branch: 20, structural_boundaries: 13, debug_prints: 12
- `ui5/fitpanel/controller/FitPanel.controller.js` (JAVASCRIPT) | Magnitude: 259.1 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 117, state_mutation: 115, branch: 32, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `interpreter/cling/www/use.html` (HTML) | Magnitude: 19.68 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 19, io: 7, ui_framework: 6
- `doc/v524/index.html` (HTML) | Magnitude: 22.0 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 46, structural_boundaries: 28, ui_framework: 19, args: 13
- `doc/v534/index.html` (HTML) | Magnitude: 25.28 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: io: 64, structural_boundaries: 42, ui_framework: 21, args: 18
- `doc/v526/index.html` (HTML) | Magnitude: 25.68 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: io: 64, structural_boundaries: 41, ui_framework: 20, args: 18
- `doc/v530/index.html` (HTML) | Magnitude: 25.42 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: io: 66, structural_boundaries: 43, ui_framework: 21, args: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `interpreter/llvm-project/clang/tools/include-mapping/cppreference_parser.py` (PYTHON) | Magnitude: 0.43 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 39, branch: 37, state_mutation: 24
- `js/modules/hist2d/THistPainter.mjs` (JAVASCRIPT) | Magnitude: 7630.96 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 2296, state_mutation: 2239, branch: 1106, structural_boundaries: 271
- `js/modules/gpad/TAxisPainter.mjs` (JAVASCRIPT) | Magnitude: 6965.62 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1833, indent_spaces: 1210, branch: 648, structural_boundaries: 201
- `js/modules/hist2d/TScatterPainter.mjs` (JAVASCRIPT) | Magnitude: 316.48 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 135, state_mutation: 77, branch: 51, structural_boundaries: 39
- `interpreter/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/MemoryMapper.h` (CPP) | Magnitude: 37.24 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 44, pointers: 26, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `roofit/roostats/inc/RooStats/TestStatistic.h` (CPP) | Magnitude: 19.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 9, doc: 8, immutability_locks: 7
- `roofit/roofitmore/src/RooNonCentralChiSquare.cxx` (CPP) | Magnitude: 119.38 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 55, doc: 54, indent_spaces: 38, branch: 10
- `interpreter/llvm-project/clang/include/clang/Format/Format.h` (CPP) | Magnitude: 403.84 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 1837, indent_spaces: 323, state_mutation: 208, dead_code: 151
- `interpreter/llvm-project/llvm/include/llvm/Support/ExponentialBackoff.h` (CPP) | Magnitude: 11.02 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 13, state_mutation: 5, dead_code: 5
- `interpreter/llvm-project/clang/include/clang/ASTMatchers/ASTMatchers.h` (CPP) | Magnitude: 2349.6 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 3488, indent_spaces: 809, state_mutation: 648, dead_code: 433

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `gui/fitpanelv7/src/RFitPanelModel.cxx` (CPP) | Magnitude: 516.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 287, indent_spaces: 252, doc: 243, branch: 93
- `gui/guibuilder/src/TGuiBldHintsEditor.cxx` (CPP) | Magnitude: 580.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 421, pointers: 316, state_mutation: 310, doc: 297
- `math/mathcore/inc/TRandom1.h` (CPP) | Magnitude: 8.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 154, indent_spaces: 29, structural_boundaries: 14, args: 9
- `tmva/tmva/inc/TMVA/TSynapse.h` (CPP) | Magnitude: 34.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 56, indent_spaces: 32, structural_boundaries: 18, api: 11
- `tmva/tmva/src/MethodDNN.cxx` (CPP) | Magnitude: 2916.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1114, state_mutation: 1018, doc: 757, branch: 253

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `bindings/pyroot/cppyy/cppyy/bench/support.py` (PYTHON) | Magnitude: 20.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, ipc_rpc_bridges: 4, branch: 2
- `ui5/eve7/index.html` (HTML) | Magnitude: 16.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 11, state_mutation: 6, branch: 4
- `interpreter/llvm-project/clang/include/clang/AST/CommentVisitor.h` (CPP) | Magnitude: 15.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 17, args: 14, macros: 14
- `interpreter/llvm-project/clang/tools/libclang/CIndexUSRs.cpp` (CPP) | Magnitude: 0.07 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, args: 29, structural_boundaries: 19, state_mutation: 19
- `interpreter/llvm-project/llvm/include/llvm/Analysis/LastRunTrackingAnalysis.h` (CPP) | Magnitude: 25.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 30, doc: 24, structural_boundaries: 21, args: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `builtins/zstd/compress/zstd_compress_literals.h` (C) | Magnitude: 24.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 10, pointers: 10, api: 9, structural_boundaries: 7
- `gui/guihtml/inc/TGHtmlUri.h` (CPP) | Magnitude: 25.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, pointers: 13, state_mutation: 8, macros: 8
- `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_thistpainter.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, ownership: 1
- `math/mathcore/inc/Math/BasicMinimizer.h` (CPP) | Magnitude: 25.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, doc: 36, immutability_locks: 31, safety: 24
- `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_tscatter.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, ownership: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tree/ntuple/src/RFieldMeta.cxx` -> Churn: **90.01%** | Cog Load: 85.4812% | Debt: 49.8876%
- `tree/dataframe/inc/ROOT/RDF/RInterface.hxx` -> Churn: **88.66%** | Cog Load: 29.5551% | Debt: 99.9973%
- `tree/ntuple/src/RField.cxx` -> Churn: **80.14%** | Cog Load: 57.7005% | Debt: 99.6123%
- `tree/dataframe/inc/ROOT/RDF/InterfaceUtils.hxx` -> Churn: **72.37%** | Cog Load: 37.9629% | Debt: 99.9998%
- `bindings/pyroot/pythonizations/python/ROOT/_facade.py` -> Churn: **68.79%** | Cog Load: 41.7923% | Debt: 88.3013%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `math/matrix/src/TDecompSparse.cxx` -> **mdessole** (100.0% isolated ownership) | Magnitude: 18475.32
- `roottest/scripts/Rules.mk` -> **Jonas Rembser** (100.0% isolated ownership) | Magnitude: 16450.92
- `graf2d/asimage/src/TASImage.cxx` -> **Sergey Linev** (100.0% isolated ownership) | Magnitude: 13350.7
- `math/mathcore/src/TKDTree.cxx` -> **ferdymercury** (100.0% isolated ownership) | Magnitude: 13288.97
- `hist/histpainter/src/TPainter3dAlgorithms.cxx` -> **Sergey Linev** (100.0% isolated ownership) | Magnitude: 10616.94

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/base/inc/Rtypes.h` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 99.9317%)
- `core/base/inc/TQObject.h` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.9873%)
- `gui/gui/inc/TGFrame.h` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 100.0%)
- `core/base/inc/TObject.h` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)
- `roofit/roofitcore/inc/RooAbsPdf.h` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/foundation/inc/DllImport.h` -> **Severity: 1610.953** (Blast Radius: 33.49 * Doc Risk: 48.1025%)
- `core/base/inc/Rtypes.h` -> **Severity: 1001.124** (Blast Radius: 55.99 * Doc Risk: 17.8804%)
- `gui/gui/inc/TGFrame.h` -> **Severity: 480.9** (Blast Radius: 4.809 * Doc Risk: 100.0%)
- `core/foundation/inc/RtypesCore.h` -> **Severity: 420.167** (Blast Radius: 35.248 * Doc Risk: 11.9203%)
- `core/base/inc/TString.h` -> **Severity: 340.943** (Blast Radius: 19.068 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
