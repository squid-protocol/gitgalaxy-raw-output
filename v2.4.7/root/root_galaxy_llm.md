# ARCHITECTURAL_BRIEF: root
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/root` |
| **Timestamp** | `2026-08-07T05:29:23.240513+00:00` |
| **Scan Duration** | `59.82s` |
| **Git Branch** | `master` |
| **Git Commit** | `e082dce9bac50cc8ea6f3acb68c306692b712770` |
| **Git Remote** | `https://github.com/root-project/root.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 12154 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.026`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 6898 | 49.6% |
| file_cluster_8 | 4433 | 31.9% |
| file_cluster_7 | 447 | 3.2% |
| file_cluster_9 | 179 | 1.3% |
| Unknown | 122 | 0.9% |
| file_cluster_4 | 105 | 0.8% |
| file_cluster_16 | 87 | 0.6% |
| file_cluster_11 | 85 | 0.6% |
| file_cluster_0 | 42 | 0.3% |
| file_cluster_17 | 24 | 0.2% |
| file_cluster_12 | 19 | 0.1% |
| file_cluster_2 | 16 | 0.1% |
| file_cluster_6 | 11 | 0.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 29.7 | 29.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 61.9 | 71.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.8 | 18.2 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.7 | 2.4 | 80.0 |
| API Exposure | 0.0 | 18.0 | 3.6 | 1.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 72.8 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 17.0 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 90.0 | 1.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.2 | 11.9 | 11.9 |
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

- `inheritsFrom` (@ `interpreter/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp`) -> Impact: **1814.8** | LOC: 525
  * *Intent:* /// inheritsFrom - Indicates whether all instructions in one class also belong /// to another class. /// /// @param child - The class that may be the ...
- `printInst` (@ `interpreter/llvm-project/llvm/tools/llvm-objdump/llvm-objdump.cpp`) -> Impact: **1590.8** | LOC: 1540
- `TLatex::Analyse` (@ `graf2d/graf/src/TLatex.cxx`) -> Impact: **1280.7** | LOC: 1316
  * *Intent:* /// when the argument is an atom (normal text), it calculates /// the size of it and return it as the result. /// for example : if the operator #%frac...
- `warn` (@ `interpreter/llvm-project/llvm/tools/llvm-nm/llvm-nm.cpp`) -> Impact: **1162.0** | LOC: 1559
- `TH2::DoFitSlices` (@ `hist/hist/src/TH2.cxx`) -> Impact: **1103.0** | LOC: 2770
- `TH1::Clone` (@ `hist/hist/src/TH1.cxx`) -> Impact: **1091.8** | LOC: 2715
- `test` (@ `js/modules/hist/TPavePainter.mjs`) -> Impact: **1078.3** | LOC: 1287
- `dav_move_file` (@ `net/http/civetweb/civetweb.c`) -> Impact: **1070.7** | LOC: 2093
- `TStreamerInfo::ReadBuffer` (@ `io/io/src/TStreamerInfoReadBuffer.cxx`) -> Impact: **1069.5** | LOC: 750
  * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Deserialize information from buffer b into object at pointer
- `TStreamerInfo::WriteBufferAux` (@ `io/io/src/TStreamerInfoWriteBuffer.cxx`) -> Impact: **1058.6** | LOC: 652
  * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// The object at pointer is serialized to the buffer b

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `builtins/glew/src` | 3 | 132697.86 | 55.37% | 17.41% |
| `hist/hist/src` | 72 | 74436.5 | 37.99% | 81.8% |
| `geom/geom/src` | 53 | 64014.0 | 38.0% | 89.45% |
| `tmva/sofie/test/input_models` | 122 | 61000.0 | 0.0% | 0.0% |
| `gui/gui/src` | 92 | 58710.7 | 36.4% | 83.45% |
| `tmva/tmva/src` | 159 | 58505.04 | 32.39% | 88.13% |
| `roofit/roofitcore/src` | 223 | 53068.66 | 33.35% | 83.0% |
| `interpreter/llvm-project/llvm/lib/Transforms/Utils` | 91 | 48632.7 | 56.65% | 65.57% |
| `graf2d/win32gdk/gdk/src/iconv` | 198 | 33016.27 | 52.59% | 1.9% |
| `graf3d/gl/src` | 92 | 32896.02 | 33.63% | 83.25% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bindings/distrdf/python/DistRDF/ComputationGraphGenerator.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Proxy.py` -> **100.0%** Exposure
- `bindings/pyroot/cppyy/cppyy/bench/py_functioncalls.py` -> **100.0%** Exposure
- `bindings/pyroot/cppyy/cppyy/python/cppyy/_pythonization.py` -> **100.0%** Exposure
- `bindings/pyroot/cppyy/cppyy/python/cppyy/_stdcpp_fix.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bindings/pyroot/pythonizations/python/ROOT/_jupyroot/helpers/cppcompleter.py` -> **100.0%** Exposure
- `bindings/pyroot/pythonizations/python/ROOT/_jupyroot/helpers/handlers.py` -> **100.0%** Exposure
- `bindings/pyroot/pythonizations/python/ROOT/_jupyroot/helpers/utils.py` -> **100.0%** Exposure
- `etc/notebook/jupyter_notebook_config.py.in` -> **100.0%** Exposure
- `geom/gdml/writer.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `interpreter/llvm-project/clang/include/clang/AST/ExprCXX.h` -> **0** Orphaned Functions | **332** Duplicates
- `interpreter/llvm-project/clang/include/clang/AST/StmtOpenMP.h` -> **0** Orphaned Functions | **285** Duplicates
- `interpreter/llvm-project/clang/include/clang/AST/Stmt.h` -> **0** Orphaned Functions | **242** Duplicates
- `graf2d/win32gdk/src/TGWin32.cxx` -> **207** Orphaned Functions | **22** Duplicates
- `js/modules/d3.mjs` -> **0** Orphaned Functions | **227** Duplicates

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
842. **`interpreter/llvm-project/llvm/utils/TableGen/tdtags`** -> AI Confidence: **99.32%**
843. **`core/zip/src/ZTrees.c`** -> AI Confidence: **99.32%**
844. **`graf2d/asimage/src/libAfterImage/libjpeg/jcdctmgr.c`** -> AI Confidence: **99.32%**
845. **`graf2d/asimage/src/libAfterImage/libjpeg/jfdctfst.c`** -> AI Confidence: **99.32%**
846. **`graf2d/asimage/src/libAfterImage/libjpeg/jidctflt.c`** -> AI Confidence: **99.32%**
847. **`graf2d/asimage/src/libAfterImage/libjpeg/jidctfst.c`** -> AI Confidence: **99.32%**
848. **`graf2d/asimage/src/libAfterImage/libpng/pngrtran.c`** -> AI Confidence: **99.32%**
849. **`graf2d/win32gdk/gdk/src/gdk/win32/gdkcursor-win32.c`** -> AI Confidence: **99.32%**
850. **`graf2d/win32gdk/gdk/src/glib/gshell.c`** -> AI Confidence: **99.32%**
851. **`tutorials/io/importCode.C`** -> AI Confidence: **99.32%**
852. **`tutorials/io/sql/sqlselect.C`** -> AI Confidence: **99.32%**
853. **`tutorials/math/fit/fitLinear2.C`** -> AI Confidence: **99.32%**
854. **`gui/cefdisplay/src/gui_handler_mac.mm`** -> AI Confidence: **99.32%**
855. **`misc/rootql/GenerateThumbnailForURL.m`** -> AI Confidence: **99.32%**
856. **`js/modules/base/TAttFillHandler.mjs`** -> AI Confidence: **99.32%**
857. **`js/modules/base/TAttLineHandler.mjs`** -> AI Confidence: **99.32%**
858. **`js/modules/base/TAttMarkerHandler.mjs`** -> AI Confidence: **99.32%**
859. **`bindings/distrdf/python/DistRDF/HeadNode.py`** -> AI Confidence: **99.31%**
860. **`bindings/pyroot/cppyy/cppyy/bench/bench_functioncalls.py`** -> AI Confidence: **99.31%**
861. **`bindings/pyroot/cppyy/cppyy/setup.py`** -> AI Confidence: **99.31%**
862. **`bindings/pyroot/pythonizations/python/ROOT/JsMVA/Factory.py`** -> AI Confidence: **99.31%**
863. **`bindings/pyroot/pythonizations/python/ROOT/_numbadeclare.py`** -> AI Confidence: **99.31%**
864. **`bindings/pyroot/pythonizations/python/ROOT/_pythonization/_rdf_pyz.py`** -> AI Confidence: **99.31%**
865. **`cmake/unix/makeCITATION.py`** -> AI Confidence: **99.31%**
866. **`interpreter/llvm-project/clang/tools/clang-format/clang-format-diff.py`** -> AI Confidence: **99.31%**
867. **`interpreter/llvm-project/clang/tools/clang-format/git-clang-format`** -> AI Confidence: **99.31%**
868. **`interpreter/llvm-project/clang/tools/scan-build-py/lib/libscanbuild/analyze.py`** -> AI Confidence: **99.31%**
869. **`interpreter/llvm-project/clang/tools/scan-build-py/lib/libscanbuild/arguments.py`** -> AI Confidence: **99.31%**
870. **`interpreter/llvm-project/clang/tools/scan-build-py/lib/libscanbuild/report.py`** -> AI Confidence: **99.31%**
871. **`interpreter/llvm-project/clang/tools/scan-build/bin/set-xcode-analyzer`** -> AI Confidence: **99.31%**
872. **`interpreter/llvm-project/clang/tools/scan-view/share/ScanView.py`** -> AI Confidence: **99.31%**
873. **`interpreter/llvm-project/clang/utils/ABITest/ABITestGen.py`** -> AI Confidence: **99.31%**
874. **`interpreter/llvm-project/clang/utils/analyzer/SATest.py`** -> AI Confidence: **99.31%**
875. **`interpreter/llvm-project/clang/utils/analyzer/exploded-graph-rewriter.py`** -> AI Confidence: **99.31%**
876. **`interpreter/llvm-project/clang/utils/check_cfc/check_cfc.py`** -> AI Confidence: **99.31%**
877. **`interpreter/llvm-project/clang/utils/clangdiag.py`** -> AI Confidence: **99.31%**
878. **`interpreter/llvm-project/clang/utils/creduce-clang-crash.py`** -> AI Confidence: **99.31%**
879. **`interpreter/llvm-project/clang/utils/hmaptool/hmaptool`** -> AI Confidence: **99.31%**
880. **`interpreter/llvm-project/clang/utils/perf-training/perf-helper.py`** -> AI Confidence: **99.31%**
881. **`interpreter/llvm-project/clang/utils/token-delta.py`** -> AI Confidence: **99.31%**
882. **`interpreter/llvm-project/llvm/utils/Misc/zkill`** -> AI Confidence: **99.31%**
883. **`interpreter/llvm-project/llvm/utils/Reviewing/find_interesting_reviews.py`** -> AI Confidence: **99.31%**
884. **`interpreter/llvm-project/llvm/utils/UpdateTestChecks/common.py`** -> AI Confidence: **99.31%**
885. **`interpreter/llvm-project/llvm/utils/abtest.py`** -> AI Confidence: **99.31%**
886. **`interpreter/llvm-project/llvm/utils/collect_and_build_with_pgo.py`** -> AI Confidence: **99.31%**
887. **`interpreter/llvm-project/llvm/utils/demangle_tree.py`** -> AI Confidence: **99.31%**
888. **`interpreter/llvm-project/llvm/utils/git/code-format-helper.py`** -> AI Confidence: **99.31%**
889. **`interpreter/llvm-project/llvm/utils/lit/lit/TestRunner.py`** -> AI Confidence: **99.31%**
890. **`interpreter/llvm-project/llvm/utils/lit/lit/builtin_commands/diff.py`** -> AI Confidence: **99.31%**
891. **`interpreter/llvm-project/llvm/utils/lit/lit/cl_arguments.py`** -> AI Confidence: **99.31%**
892. **`interpreter/llvm-project/llvm/utils/lit/lit/formats/googletest.py`** -> AI Confidence: **99.31%**
893. **`interpreter/llvm-project/llvm/utils/lit/lit/main.py`** -> AI Confidence: **99.31%**
894. **`interpreter/llvm-project/llvm/utils/lit/lit/reports.py`** -> AI Confidence: **99.31%**
895. **`interpreter/llvm-project/llvm/utils/lit/lit/util.py`** -> AI Confidence: **99.31%**
896. **`interpreter/llvm-project/llvm/utils/llvm-locstats/llvm-locstats.py`** -> AI Confidence: **99.31%**
897. **`interpreter/llvm-project/llvm/utils/llvm-mca-compare.py`** -> AI Confidence: **99.31%**
898. **`interpreter/llvm-project/llvm/utils/remote-exec.py`** -> AI Confidence: **99.31%**
899. **`interpreter/llvm-project/llvm/utils/revert_checker.py`** -> AI Confidence: **99.31%**
900. **`interpreter/llvm-project/llvm/utils/update_any_test_checks.py`** -> AI Confidence: **99.31%**
901. **`interpreter/llvm-project/llvm/utils/update_cc_test_checks.py`** -> AI Confidence: **99.31%**
902. **`interpreter/llvm-project/llvm/utils/update_mc_test_checks.py`** -> AI Confidence: **99.31%**
903. **`interpreter/llvm-project/llvm/utils/update_mca_test_checks.py`** -> AI Confidence: **99.31%**
904. **`interpreter/llvm-project/llvm/utils/update_mir_test_checks.py`** -> AI Confidence: **99.31%**
905. **`interpreter/llvm-project/llvm/utils/update_test_body.py`** -> AI Confidence: **99.31%**
906. **`bindings/pyroot/cppyy/CPyCppyy/src/API.cxx`** -> AI Confidence: **99.31%**
907. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPConstructor.cxx`** -> AI Confidence: **99.31%**
908. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPDataMember.cxx`** -> AI Confidence: **99.31%**
909. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPInstance.cxx`** -> AI Confidence: **99.31%**
910. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPOverload.cxx`** -> AI Confidence: **99.31%**
911. **`bindings/pyroot/cppyy/CPyCppyy/src/CPPScope.cxx`** -> AI Confidence: **99.31%**
912. **`bindings/pyroot/cppyy/CPyCppyy/src/CPyCppyyModule.cxx`** -> AI Confidence: **99.31%**
913. **`bindings/pyroot/cppyy/CPyCppyy/src/Dispatcher.cxx`** -> AI Confidence: **99.31%**
914. **`bindings/pyroot/cppyy/CPyCppyy/src/LowLevelViews.cxx`** -> AI Confidence: **99.31%**
915. **`bindings/pyroot/cppyy/CPyCppyy/src/MemoryRegulator.cxx`** -> AI Confidence: **99.31%**
916. **`bindings/pyroot/cppyy/CPyCppyy/src/Pythonize.cxx`** -> AI Confidence: **99.31%**
917. **`bindings/pyroot/cppyy/CPyCppyy/src/TPyClassGenerator.cxx`** -> AI Confidence: **99.31%**
918. **`bindings/pyroot/cppyy/CPyCppyy/src/Utility.cxx`** -> AI Confidence: **99.31%**
919. **`bindings/pyroot/cppyy/cppyy-backend/clingwrapper/src/clingwrapper.cxx`** -> AI Confidence: **99.31%**
920. **`bindings/pyroot/pythonizations/src/TTreePyz.cxx`** -> AI Confidence: **99.31%**
921. **`bindings/r/src/TRInterface.cxx`** -> AI Confidence: **99.31%**
922. **`bindings/tpython/src/TPyClassGenerator.cxx`** -> AI Confidence: **99.31%**
923. **`bindings/tpython/src/TPython.cxx`** -> AI Confidence: **99.31%**
924. **`core/base/src/TApplication.cxx`** -> AI Confidence: **99.31%**
925. **`core/base/src/TAttAxis.cxx`** -> AI Confidence: **99.31%**
926. **`core/base/src/TAttLine.cxx`** -> AI Confidence: **99.31%**
927. **`core/base/src/TAttMarker.cxx`** -> AI Confidence: **99.31%**
928. **`core/base/src/TAttText.cxx`** -> AI Confidence: **99.31%**
929. **`core/base/src/TDirectory.cxx`** -> AI Confidence: **99.31%**
930. **`core/base/src/TFolder.cxx`** -> AI Confidence: **99.31%**
931. **`core/base/src/TListOfTypes.cxx`** -> AI Confidence: **99.31%**
932. **`core/base/src/TMD5.cxx`** -> AI Confidence: **99.31%**
933. **`core/base/src/TMacro.cxx`** -> AI Confidence: **99.31%**
934. **`core/base/src/TObject.cxx`** -> AI Confidence: **99.31%**
935. **`core/base/src/TQCommand.cxx`** -> AI Confidence: **99.31%**
936. **`core/base/src/TQObject.cxx`** -> AI Confidence: **99.31%**
937. **`core/base/src/TROOT.cxx`** -> AI Confidence: **99.31%**
938. **`core/base/src/TRef.cxx`** -> AI Confidence: **99.31%**
939. **`core/base/src/TStopwatch.cxx`** -> AI Confidence: **99.31%**
940. **`core/base/src/TStorage.cxx`** -> AI Confidence: **99.31%**
941. **`core/base/src/TString.cxx`** -> AI Confidence: **99.31%**
942. **`core/base/src/TStyle.cxx`** -> AI Confidence: **99.31%**
943. **`core/base/src/TTimeStamp.cxx`** -> AI Confidence: **99.31%**
944. **`core/base/src/TUUID.cxx`** -> AI Confidence: **99.31%**
945. **`core/clingutils/src/TClingUtils.cxx`** -> AI Confidence: **99.31%**
946. **`core/cont/src/TClassTable.cxx`** -> AI Confidence: **99.31%**
947. **`core/cont/src/TClonesArray.cxx`** -> AI Confidence: **99.31%**
948. **`core/cont/src/TCollection.cxx`** -> AI Confidence: **99.31%**
949. **`core/dictgen/src/BaseSelectionRule.cxx`** -> AI Confidence: **99.31%**
950. **`core/dictgen/src/DictSelectionReader.cxx`** -> AI Confidence: **99.31%**
951. **`core/dictgen/src/Scanner.cxx`** -> AI Confidence: **99.31%**
952. **`core/dictgen/src/SelectionRules.cxx`** -> AI Confidence: **99.31%**
953. **`core/dictgen/src/TModuleGenerator.cxx`** -> AI Confidence: **99.31%**
954. **`core/dictgen/src/rootcling_impl.cxx`** -> AI Confidence: **99.31%**
955. **`core/foundation/inc/ROOT/RError.hxx`** -> AI Confidence: **99.31%**
956. **`core/foundation/src/FoundationUtils.cxx`** -> AI Confidence: **99.31%**
957. **`core/foundation/src/RConversionRuleParser.cxx`** -> AI Confidence: **99.31%**
958. **`core/foundation/src/TError.cxx`** -> AI Confidence: **99.31%**
959. **`core/gui/src/TBrowser.cxx`** -> AI Confidence: **99.31%**
960. **`core/gui/src/TGuiFactory.cxx`** -> AI Confidence: **99.31%**
961. **`core/imt/src/RTaskArena.cxx`** -> AI Confidence: **99.31%**
962. **`core/lz4/src/ZipLZ4.cxx`** -> AI Confidence: **99.31%**
963. **`core/meta/src/TCheckHashRecursiveRemoveConsistency.h`** -> AI Confidence: **99.31%**
964. **`core/meta/src/TClass.cxx`** -> AI Confidence: **99.31%**
965. **`core/meta/src/TEnum.cxx`** -> AI Confidence: **99.31%**
966. **`core/meta/src/TFunction.cxx`** -> AI Confidence: **99.31%**
967. **`core/meta/src/TListOfDataMembers.cxx`** -> AI Confidence: **99.31%**
968. **`core/meta/src/TSchemaRuleSet.cxx`** -> AI Confidence: **99.31%**
969. **`core/meta/src/TStatusBitsChecker.cxx`** -> AI Confidence: **99.31%**
970. **`core/meta/src/TVirtualStreamerInfo.cxx`** -> AI Confidence: **99.31%**
971. **`core/metacling/src/TCling.cxx`** -> AI Confidence: **99.31%**
972. **`core/metacling/src/TClingBaseClassInfo.cxx`** -> AI Confidence: **99.31%**
973. **`core/metacling/src/TClingCallFunc.cxx`** -> AI Confidence: **99.31%**
974. **`core/metacling/src/TClingClassInfo.cxx`** -> AI Confidence: **99.31%**
975. **`core/metacling/src/TClingDataMemberInfo.cxx`** -> AI Confidence: **99.31%**
976. **`core/metacling/src/TClingMethodArgInfo.cxx`** -> AI Confidence: **99.31%**
977. **`core/metacling/src/TClingMethodInfo.cxx`** -> AI Confidence: **99.31%**
978. **`core/metacling/src/TClingRdictModuleFileExtension.cxx`** -> AI Confidence: **99.31%**
979. **`core/metacling/src/TClingTypedefInfo.cxx`** -> AI Confidence: **99.31%**
980. **`core/textinput/src/Getline.cxx`** -> AI Confidence: **99.31%**
981. **`core/textinput/src/textinput/Editor.cpp`** -> AI Confidence: **99.31%**
982. **`core/textinput/src/textinput/TerminalDisplay.cpp`** -> AI Confidence: **99.31%**
983. **`core/textinput/src/textinput/TerminalDisplayUnix.cpp`** -> AI Confidence: **99.31%**
984. **`core/textinput/src/textinput/TextInput.cpp`** -> AI Confidence: **99.31%**
985. **`core/thread/src/TThread.cxx`** -> AI Confidence: **99.31%**
986. **`core/winnt/src/TWinNTSystem.cxx`** -> AI Confidence: **99.31%**
987. **`core/winnt/src/Win32Splash.cxx`** -> AI Confidence: **99.31%**
988. **`core/zip/src/RZip.cxx`** -> AI Confidence: **99.31%**
989. **`geom/geom/src/TGeoBBox.cxx`** -> AI Confidence: **99.31%**
990. **`geom/geom/src/TGeoBoolNode.cxx`** -> AI Confidence: **99.31%**
991. **`geom/geom/src/TGeoColorScheme.cxx`** -> AI Confidence: **99.31%**
992. **`geom/geom/src/TGeoCompositeShape.cxx`** -> AI Confidence: **99.31%**
993. **`geom/geom/src/TGeoCone.cxx`** -> AI Confidence: **99.31%**
994. **`geom/geom/src/TGeoEltu.cxx`** -> AI Confidence: **99.31%**
995. **`geom/geom/src/TGeoManager.cxx`** -> AI Confidence: **99.31%**
996. **`geom/geom/src/TGeoMaterial.cxx`** -> AI Confidence: **99.31%**
997. **`geom/geom/src/TGeoNode.cxx`** -> AI Confidence: **99.31%**
998. **`geom/geom/src/TGeoParaboloid.cxx`** -> AI Confidence: **99.31%**
999. **`geom/geom/src/TGeoParallelWorld.cxx`** -> AI Confidence: **99.31%**
1000. **`geom/geom/src/TGeoPatternFinder.cxx`** -> AI Confidence: **99.31%**
1001. **`geom/geom/src/TGeoPhysicalNode.cxx`** -> AI Confidence: **99.31%**
1002. **`geom/geom/src/TGeoShape.cxx`** -> AI Confidence: **99.31%**
1003. **`geom/geom/src/TGeoTessellated.cxx`** -> AI Confidence: **99.31%**
1004. **`geom/geom/src/TGeoTube.cxx`** -> AI Confidence: **99.31%**
1005. **`geom/geom/src/TGeoXtru.cxx`** -> AI Confidence: **99.31%**
1006. **`geom/geombuilder/src/TGeoBBoxEditor.cxx`** -> AI Confidence: **99.31%**
1007. **`geom/geombuilder/src/TGeoConeEditor.cxx`** -> AI Confidence: **99.31%**
1008. **`geom/geombuilder/src/TGeoEltuEditor.cxx`** -> AI Confidence: **99.31%**
1009. **`geom/geombuilder/src/TGeoManagerEditor.cxx`** -> AI Confidence: **99.31%**
1010. **`geom/geombuilder/src/TGeoMaterialEditor.cxx`** -> AI Confidence: **99.31%**
1011. **`geom/geombuilder/src/TGeoMatrixEditor.cxx`** -> AI Confidence: **99.31%**
1012. **`geom/geombuilder/src/TGeoMediumEditor.cxx`** -> AI Confidence: **99.31%**
1013. **`geom/geombuilder/src/TGeoNodeEditor.cxx`** -> AI Confidence: **99.31%**
1014. **`geom/geombuilder/src/TGeoParaEditor.cxx`** -> AI Confidence: **99.31%**
1015. **`geom/geombuilder/src/TGeoPconEditor.cxx`** -> AI Confidence: **99.31%**
1016. **`geom/geombuilder/src/TGeoTabManager.cxx`** -> AI Confidence: **99.31%**
1017. **`geom/geombuilder/src/TGeoTorusEditor.cxx`** -> AI Confidence: **99.31%**
1018. **`geom/geombuilder/src/TGeoTrd1Editor.cxx`** -> AI Confidence: **99.31%**
1019. **`geom/geombuilder/src/TGeoTrd2Editor.cxx`** -> AI Confidence: **99.31%**
1020. **`geom/geombuilder/src/TGeoTubeEditor.cxx`** -> AI Confidence: **99.31%**
1021. **`geom/geombuilder/src/TGeoVolumeEditor.cxx`** -> AI Confidence: **99.31%**
1022. **`geom/geomchecker/src/TGeoOverlap.cxx`** -> AI Confidence: **99.31%**
1023. **`geom/vecgeom/src/TGeoVGShape.cxx`** -> AI Confidence: **99.31%**
1024. **`geom/webviewer/src/RGeomData.cxx`** -> AI Confidence: **99.31%**
1025. **`graf2d/fitsio/src/TFITS.cxx`** -> AI Confidence: **99.31%**
1026. **`graf2d/gpad/src/TColorWheel.cxx`** -> AI Confidence: **99.31%**
1027. **`graf2d/gpad/src/TControlBar.cxx`** -> AI Confidence: **99.31%**
1028. **`graf2d/gpad/src/TPadPainter.cxx`** -> AI Confidence: **99.31%**
1029. **`graf2d/gpadv7/src/RAttrAggregation.cxx`** -> AI Confidence: **99.31%**
1030. **`graf2d/gpadv7/src/RAttrMap.cxx`** -> AI Confidence: **99.31%**
1031. **`graf2d/gpadv7/src/RCanvas.cxx`** -> AI Confidence: **99.31%**
1032. **`graf2d/gpadv7/src/TObjectDrawable.cxx`** -> AI Confidence: **99.31%**
1033. **`graf2d/graf/src/TCurlyArc.cxx`** -> AI Confidence: **99.31%**
1034. **`graf2d/graf/src/TMarker.cxx`** -> AI Confidence: **99.31%**
1035. **`graf2d/graf/src/TMathText.cxx`** -> AI Confidence: **99.31%**
1036. **`graf2d/graf/src/TTF.cxx`** -> AI Confidence: **99.31%**
1037. **`graf2d/graf/src/TWbox.cxx`** -> AI Confidence: **99.31%**
1038. **`graf2d/mathtext/src/fontembed.cxx`** -> AI Confidence: **99.31%**
1039. **`graf2d/win32gdk/src/TGWin32ProxyBase.cxx`** -> AI Confidence: **99.31%**
1040. **`graf2d/x11/src/GX11Gui.cxx`** -> AI Confidence: **99.31%**
1041. **`graf2d/x11ttf/src/TGX11TTF.cxx`** -> AI Confidence: **99.31%**
1042. **`graf3d/eve/src/TEveCaloData.cxx`** -> AI Confidence: **99.31%**
1043. **`graf3d/eve/src/TEveCaloVizEditor.cxx`** -> AI Confidence: **99.31%**
1044. **`graf3d/eve/src/TEveDigitSetEditor.cxx`** -> AI Confidence: **99.31%**
1045. **`graf3d/eve/src/TEveElement.cxx`** -> AI Confidence: **99.31%**
1046. **`graf3d/eve/src/TEveElementEditor.cxx`** -> AI Confidence: **99.31%**
1047. **`graf3d/eve/src/TEveGedEditor.cxx`** -> AI Confidence: **99.31%**
1048. **`graf3d/eve/src/TEveGeoNode.cxx`** -> AI Confidence: **99.31%**
1049. **`graf3d/eve/src/TEveGeoShape.cxx`** -> AI Confidence: **99.31%**
1050. **`graf3d/eve/src/TEveManager.cxx`** -> AI Confidence: **99.31%**
1051. **`graf3d/eve/src/TEvePointSet.cxx`** -> AI Confidence: **99.31%**
1052. **`graf3d/eve/src/TEvePolygonSetProjectedGL.cxx`** -> AI Confidence: **99.31%**
1053. **`graf3d/eve/src/TEveProjectionManager.cxx`** -> AI Confidence: **99.31%**
1054. **`graf3d/eve/src/TEveRGBAPaletteEditor.cxx`** -> AI Confidence: **99.31%**
1055. **`graf3d/eve/src/TEveTextEditor.cxx`** -> AI Confidence: **99.31%**
1056. **`graf3d/eve/src/TEveTrack.cxx`** -> AI Confidence: **99.31%**
1057. **`graf3d/eve/src/TEveTrackEditor.cxx`** -> AI Confidence: **99.31%**
1058. **`graf3d/eve/src/TEveTrans.cxx`** -> AI Confidence: **99.31%**
1059. **`graf3d/eve/src/TEveUtil.cxx`** -> AI Confidence: **99.31%**
1060. **`graf3d/eve/src/TEveViewer.cxx`** -> AI Confidence: **99.31%**
1061. **`graf3d/eve/src/TEveWindow.cxx`** -> AI Confidence: **99.31%**
1062. **`graf3d/eve7/src/REveBoxSet.cxx`** -> AI Confidence: **99.31%**
1063. **`graf3d/eve7/src/REveCalo.cxx`** -> AI Confidence: **99.31%**
1064. **`graf3d/eve7/src/REveCaloData.cxx`** -> AI Confidence: **99.31%**
1065. **`graf3d/eve7/src/REveDataCollection.cxx`** -> AI Confidence: **99.31%**
1066. **`graf3d/eve7/src/REveDataSimpleProxyBuilder.cxx`** -> AI Confidence: **99.31%**
1067. **`graf3d/eve7/src/REveElement.cxx`** -> AI Confidence: **99.31%**
1068. **`graf3d/eve7/src/REveGeoPolyShape.cxx`** -> AI Confidence: **99.31%**
1069. **`graf3d/eve7/src/REveGeoTopNode.cxx`** -> AI Confidence: **99.31%**
1070. **`graf3d/eve7/src/REveManager.cxx`** -> AI Confidence: **99.31%**
1071. **`graf3d/eve7/src/REvePointSet.cxx`** -> AI Confidence: **99.31%**
1072. **`graf3d/eve7/src/REveProjectionManager.cxx`** -> AI Confidence: **99.31%**
1073. **`graf3d/eve7/src/REveScene.cxx`** -> AI Confidence: **99.31%**
1074. **`graf3d/eve7/src/REveSelection.cxx`** -> AI Confidence: **99.31%**
1075. **`graf3d/eve7/src/REveTableInfo.cxx`** -> AI Confidence: **99.31%**
1076. **`graf3d/eve7/src/REveTrack.cxx`** -> AI Confidence: **99.31%**
1077. **`graf3d/eve7/src/REveTrans.cxx`** -> AI Confidence: **99.31%**
1078. **`graf3d/eve7/src/REveUtil.cxx`** -> AI Confidence: **99.31%**
1079. **`graf3d/eve7/src/REveViewer.cxx`** -> AI Confidence: **99.31%**
1080. **`graf3d/g3d/src/TAxis3D.cxx`** -> AI Confidence: **99.31%**
1081. **`graf3d/g3d/src/TGeometry.cxx`** -> AI Confidence: **99.31%**
1082. **`graf3d/g3d/src/TMarker3DBox.cxx`** -> AI Confidence: **99.31%**
1083. **`graf3d/g3d/src/TPolyLine3D.cxx`** -> AI Confidence: **99.31%**
1084. **`graf3d/g3d/src/TPolyMarker3D.cxx`** -> AI Confidence: **99.31%**
1085. **`graf3d/g3d/src/TShape.cxx`** -> AI Confidence: **99.31%**
1086. **`graf3d/gl/src/TF2GL.cxx`** -> AI Confidence: **99.31%**
1087. **`graf3d/gl/src/TGL5DDataSetEditor.cxx`** -> AI Confidence: **99.31%**
1088. **`graf3d/gl/src/TGLAutoRotator.cxx`** -> AI Confidence: **99.31%**
1089. **`graf3d/gl/src/TGLCameraGuide.cxx`** -> AI Confidence: **99.31%**
1090. **`graf3d/gl/src/TGLClip.cxx`** -> AI Confidence: **99.31%**
1091. **`graf3d/gl/src/TGLContext.cxx`** -> AI Confidence: **99.31%**
1092. **`graf3d/gl/src/TGLCylinder.cxx`** -> AI Confidence: **99.31%**
1093. **`graf3d/gl/src/TGLFaceSet.cxx`** -> AI Confidence: **99.31%**
1094. **`graf3d/gl/src/TGLFormat.cxx`** -> AI Confidence: **99.31%**
1095. **`graf3d/gl/src/TGLManipSet.cxx`** -> AI Confidence: **99.31%**
1096. **`graf3d/gl/src/TGLObject.cxx`** -> AI Confidence: **99.31%**
1097. **`graf3d/gl/src/TGLOverlayButton.cxx`** -> AI Confidence: **99.31%**
1098. **`graf3d/gl/src/TGLPShapeObjEditor.cxx`** -> AI Confidence: **99.31%**
1099. **`graf3d/gl/src/TGLPadPainter.cxx`** -> AI Confidence: **99.31%**
1100. **`graf3d/gl/src/TGLPadUtils.cxx`** -> AI Confidence: **99.31%**
1101. **`graf3d/gl/src/TGLParametric.cxx`** -> AI Confidence: **99.31%**
1102. **`graf3d/gl/src/TGLPlot3D.cxx`** -> AI Confidence: **99.31%**
1103. **`graf3d/gl/src/TGLPlotPainter.cxx`** -> AI Confidence: **99.31%**
1104. **`graf3d/gl/src/TGLPolyLine.cxx`** -> AI Confidence: **99.31%**
1105. **`graf3d/gl/src/TGLScene.cxx`** -> AI Confidence: **99.31%**
1106. **`graf3d/gl/src/TGLSdfFontMaker.cxx`** -> AI Confidence: **99.31%**
1107. **`graf3d/gl/src/TGLUtil.cxx`** -> AI Confidence: **99.31%**
1108. **`graf3d/gl/src/TGLViewer.cxx`** -> AI Confidence: **99.31%**
1109. **`graf3d/gl/src/TGLViewerBase.cxx`** -> AI Confidence: **99.31%**
1110. **`graf3d/gl/src/TGLViewerEditor.cxx`** -> AI Confidence: **99.31%**
1111. **`graf3d/gl/src/TX11GL.cxx`** -> AI Confidence: **99.31%**
1112. **`graf3d/gl/src/gl2ps.cxx`** -> AI Confidence: **99.31%**
1113. **`graf3d/gviz3d/src/TStructNodeEditor.cxx`** -> AI Confidence: **99.31%**
1114. **`graf3d/gviz3d/src/TStructViewerGUI.cxx`** -> AI Confidence: **99.31%**
1115. **`graf3d/x3d/src/TViewerX3D.cxx`** -> AI Confidence: **99.31%**
1116. **`gui/browsable/src/RSysFile.cxx`** -> AI Confidence: **99.31%**
1117. **`gui/browsable/src/TDirectoryElement.cxx`** -> AI Confidence: **99.31%**
1118. **`gui/browserv7/src/RBrowser.cxx`** -> AI Confidence: **99.31%**
1119. **`gui/browserv7/src/RBrowserData.cxx`** -> AI Confidence: **99.31%**
1120. **`gui/browserv7/src/RBrowserTCanvasWidget.cxx`** -> AI Confidence: **99.31%**
1121. **`gui/browserv7/src/RFileDialog.cxx`** -> AI Confidence: **99.31%**
1122. **`gui/canvaspainter/src/RCanvasPainter.cxx`** -> AI Confidence: **99.31%**
1123. **`gui/cefdisplay/src/gui_handler.cxx`** -> AI Confidence: **99.31%**
1124. **`gui/cefdisplay/src/gui_handler_linux.cxx`** -> AI Confidence: **99.31%**
1125. **`gui/cefdisplay/src/simple_app.cxx`** -> AI Confidence: **99.31%**
1126. **`gui/fitpanel/src/TAdvancedGraphicsDialog.cxx`** -> AI Confidence: **99.31%**
1127. **`gui/fitpanelv7/src/RFitPanel.cxx`** -> AI Confidence: **99.31%**
1128. **`gui/ged/src/TAttFillEditor.cxx`** -> AI Confidence: **99.31%**
1129. **`gui/ged/src/TAttLineEditor.cxx`** -> AI Confidence: **99.31%**
1130. **`gui/ged/src/TAttMarkerEditor.cxx`** -> AI Confidence: **99.31%**
1131. **`gui/ged/src/TAttTextEditor.cxx`** -> AI Confidence: **99.31%**
1132. **`gui/ged/src/TAxisEditor.cxx`** -> AI Confidence: **99.31%**
1133. **`gui/ged/src/TF1Editor.cxx`** -> AI Confidence: **99.31%**
1134. **`gui/ged/src/TGedFrame.cxx`** -> AI Confidence: **99.31%**
1135. **`gui/ged/src/TH2Editor.cxx`** -> AI Confidence: **99.31%**
1136. **`gui/ged/src/TStyleManager.cxx`** -> AI Confidence: **99.31%**
1137. **`gui/gui/src/TGClient.cxx`** -> AI Confidence: **99.31%**
1138. **`gui/gui/src/TGIcon.cxx`** -> AI Confidence: **99.31%**
1139. **`gui/gui/src/TGImageMap.cxx`** -> AI Confidence: **99.31%**
1140. **`gui/gui/src/TGPasswdDialog.cxx`** -> AI Confidence: **99.31%**
1141. **`gui/gui/src/TGPicture.cxx`** -> AI Confidence: **99.31%**
1142. **`gui/gui/src/TGSplitFrame.cxx`** -> AI Confidence: **99.31%**
1143. **`gui/gui/src/TGTable.cxx`** -> AI Confidence: **99.31%**
1144. **`gui/gui/src/TGTableCell.cxx`** -> AI Confidence: **99.31%**
1145. **`gui/gui/src/TGToolBar.cxx`** -> AI Confidence: **99.31%**
1146. **`gui/gui/src/TRootGuiFactory.cxx`** -> AI Confidence: **99.31%**
1147. **`gui/qt6webdisplay/rooturlschemehandler.cpp`** -> AI Confidence: **99.31%**
1148. **`gui/webdisplay/src/RWebWindow.cxx`** -> AI Confidence: **99.31%**
1149. **`gui/webgui6/src/TWebControlBar.cxx`** -> AI Confidence: **99.31%**
1150. **`hist/hbook/src/THbookFile.cxx`** -> AI Confidence: **99.31%**
1151. **`hist/hist/src/TAxis.cxx`** -> AI Confidence: **99.31%**
1152. **`hist/hist/src/TBackCompFitter.cxx`** -> AI Confidence: **99.31%**
1153. **`hist/hist/src/TF1Helper.cxx`** -> AI Confidence: **99.31%**
1154. **`hist/hist/src/TF1NormSum.cxx`** -> AI Confidence: **99.31%**
1155. **`hist/hist/src/TF2.cxx`** -> AI Confidence: **99.31%**
1156. **`hist/hist/src/TF3.cxx`** -> AI Confidence: **99.31%**
1157. **`hist/hist/src/TFormula.cxx`** -> AI Confidence: **99.31%**
1158. **`hist/hist/src/TGraph2D.cxx`** -> AI Confidence: **99.31%**
1159. **`hist/hist/src/TGraphAsymmErrors.cxx`** -> AI Confidence: **99.31%**
1160. **`hist/hist/src/TGraphBentErrors.cxx`** -> AI Confidence: **99.31%**
1161. **`hist/hist/src/TGraphTime.cxx`** -> AI Confidence: **99.31%**
1162. **`hist/hist/src/THStack.cxx`** -> AI Confidence: **99.31%**
1163. **`hist/hist/src/THnChain.cxx`** -> AI Confidence: **99.31%**
1164. **`hist/hist/src/TProfile2Poly.cxx`** -> AI Confidence: **99.31%**
1165. **`hist/histv7/benchmark/hist_benchmark_engine.cxx`** -> AI Confidence: **99.31%**
1166. **`interpreter/CppInterOp/unittests/CppInterOp/Utils.cpp`** -> AI Confidence: **99.31%**
1167. **`interpreter/cling/lib/Utils/AST.cpp`** -> AI Confidence: **99.31%**
1168. **`interpreter/cling/lib/Utils/PlatformPosix.cpp`** -> AI Confidence: **99.31%**
1169. **`interpreter/cling/lib/Utils/PlatformWin.cpp`** -> AI Confidence: **99.31%**
1170. **`interpreter/cling/tools/driver/cling.cpp`** -> AI Confidence: **99.31%**
1171. **`interpreter/llvm-project/clang/include/clang/AST/JSONNodeDumper.h`** -> AI Confidence: **99.31%**
1172. **`interpreter/llvm-project/clang/include/clang/AST/RecursiveASTVisitor.h`** -> AI Confidence: **99.31%**
1173. **`interpreter/llvm-project/clang/include/clang/AST/StmtVisitor.h`** -> AI Confidence: **99.31%**
1174. **`interpreter/llvm-project/clang/include/clang/Basic/ObjCRuntime.h`** -> AI Confidence: **99.31%**
1175. **`interpreter/llvm-project/clang/include/clang/Basic/PartialDiagnostic.h`** -> AI Confidence: **99.31%**
1176. **`interpreter/llvm-project/clang/tools/clang-extdef-mapping/ClangExtDefMapGen.cpp`** -> AI Confidence: **99.31%**
1177. **`interpreter/llvm-project/clang/tools/clang-format/ClangFormat.cpp`** -> AI Confidence: **99.31%**
1178. **`interpreter/llvm-project/clang/tools/clang-fuzzer/handle-llvm/handle_llvm.cpp`** -> AI Confidence: **99.31%**
1179. **`interpreter/llvm-project/clang/tools/clang-installapi/Options.cpp`** -> AI Confidence: **99.31%**
1180. **`interpreter/llvm-project/clang/tools/clang-nvlink-wrapper/ClangNVLinkWrapper.cpp`** -> AI Confidence: **99.31%**
1181. **`interpreter/llvm-project/clang/tools/clang-offload-bundler/ClangOffloadBundler.cpp`** -> AI Confidence: **99.31%**
1182. **`interpreter/llvm-project/clang/tools/clang-offload-packager/ClangOffloadPackager.cpp`** -> AI Confidence: **99.31%**
1183. **`interpreter/llvm-project/clang/tools/clang-refactor/TestSupport.cpp`** -> AI Confidence: **99.31%**
1184. **`interpreter/llvm-project/clang/tools/clang-repl/ClangRepl.cpp`** -> AI Confidence: **99.31%**
1185. **`interpreter/llvm-project/clang/tools/clang-scan-deps/ClangScanDeps.cpp`** -> AI Confidence: **99.31%**
1186. **`interpreter/llvm-project/clang/tools/clang-sycl-linker/ClangSYCLLinker.cpp`** -> AI Confidence: **99.31%**
1187. **`interpreter/llvm-project/clang/tools/diagtool/ShowEnabledWarnings.cpp`** -> AI Confidence: **99.31%**
1188. **`interpreter/llvm-project/clang/tools/diagtool/TreeView.cpp`** -> AI Confidence: **99.31%**
1189. **`interpreter/llvm-project/clang/tools/driver/cc1_main.cpp`** -> AI Confidence: **99.31%**
1190. **`interpreter/llvm-project/clang/tools/driver/cc1as_main.cpp`** -> AI Confidence: **99.31%**
1191. **`interpreter/llvm-project/clang/tools/driver/driver.cpp`** -> AI Confidence: **99.31%**
1192. **`interpreter/llvm-project/clang/tools/libclang/CIndex.cpp`** -> AI Confidence: **99.31%**
1193. **`interpreter/llvm-project/clang/tools/libclang/CIndexDiagnostic.cpp`** -> AI Confidence: **99.31%**
1194. **`interpreter/llvm-project/clang/tools/libclang/CIndexHigh.cpp`** -> AI Confidence: **99.31%**
1195. **`interpreter/llvm-project/clang/tools/libclang/CXIndexDataConsumer.cpp`** -> AI Confidence: **99.31%**
1196. **`interpreter/llvm-project/clang/tools/libclang/CXSourceLocation.cpp`** -> AI Confidence: **99.31%**
1197. **`interpreter/llvm-project/clang/tools/libclang/CXType.cpp`** -> AI Confidence: **99.31%**
1198. **`interpreter/llvm-project/clang/utils/TableGen/ClangAttrEmitter.cpp`** -> AI Confidence: **99.31%**
1199. **`interpreter/llvm-project/clang/utils/TableGen/ClangDiagnosticsEmitter.cpp`** -> AI Confidence: **99.31%**
1200. **`interpreter/llvm-project/clang/utils/TableGen/ClangOptionDocEmitter.cpp`** -> AI Confidence: **99.31%**
1201. **`interpreter/llvm-project/clang/utils/TableGen/ClangSyntaxEmitter.cpp`** -> AI Confidence: **99.31%**
1202. **`interpreter/llvm-project/clang/utils/TableGen/RISCVVEmitter.cpp`** -> AI Confidence: **99.31%**
1203. **`interpreter/llvm-project/llvm/examples/BrainF/BrainF.cpp`** -> AI Confidence: **99.31%**
1204. **`interpreter/llvm-project/llvm/examples/IRTransforms/SimplifyCFG.cpp`** -> AI Confidence: **99.31%**
1205. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/BuildingAJIT/Chapter1/toy.cpp`** -> AI Confidence: **99.31%**
1206. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/BuildingAJIT/Chapter2/toy.cpp`** -> AI Confidence: **99.31%**
1207. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/BuildingAJIT/Chapter3/toy.cpp`** -> AI Confidence: **99.31%**
1208. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/BuildingAJIT/Chapter4/toy.cpp`** -> AI Confidence: **99.31%**
1209. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter2/toy.cpp`** -> AI Confidence: **99.31%**
1210. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter3/toy.cpp`** -> AI Confidence: **99.31%**
1211. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter4/toy.cpp`** -> AI Confidence: **99.31%**
1212. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter5/toy.cpp`** -> AI Confidence: **99.31%**
1213. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter6/toy.cpp`** -> AI Confidence: **99.31%**
1214. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter7/toy.cpp`** -> AI Confidence: **99.31%**
1215. **`interpreter/llvm-project/llvm/examples/Kaleidoscope/Chapter8/toy.cpp`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `157` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `65694` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/modules/draw/TWebPaintingPainter.mjs` (JAVASCRIPT) -> Cumulative Risk: **718.52**
- **Archetype:** `file_cluster_4` (Distance: 12.651 IQR)
- **Magnitude:** 382.66 | **LOC:** 228 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.9977%)
- **Heaviest Functions:** `redraw` (Impact: 94.9), `process` (Impact: 64.2), `check_attributes` (Impact: 21.5)

### 2. `tree/ntuple/src/RClusterPool.cxx` (CPP) -> Cumulative Risk: **702.96**
- **Archetype:** `file_cluster_4` (Distance: 13.559 IQR)
- **Magnitude:** 466.26 | **LOC:** 405 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.8234%), Safety Score (97.4016%)
- **Heaviest Functions:** `ROOT::Internal::RClusterPool::GetCluster` (Impact: 68.2), `ROOT::Internal::RClusterPool::WaitFor` (Impact: 25.2), `ROOT::Internal::RClusterPool::ExecReadCl` (Impact: 14.5)

### 3. `config/rootssh` (SHELL) -> Cumulative Risk: **694.52**
- **Archetype:** `file_cluster_4` (Distance: 14.701 IQR)
- **Magnitude:** 229.2 | **LOC:** 182 | **CtrlFlow:** 90.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9549%), Tech Debt (99.7762%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 46.6), `Anonymous_Block` (Impact: 32.3), `Anonymous_Block_[Truncated]` (Impact: 20.8)

### 4. `js/modules/draw/TTree.mjs` (JAVASCRIPT) -> Cumulative Risk: **694.51**
- **Archetype:** `file_cluster_4` (Distance: 14.539 IQR)
- **Magnitude:** 743.28 | **LOC:** 494 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9954%), Safety Score (90.5031%)
- **Heaviest Functions:** `createTreePlayer` (Impact: 95.1), `drawTree` (Impact: 80.2), `drawTreePlayer` (Impact: 44.9)

### 5. `js/modules/draw/TTextPainter.mjs` (JAVASCRIPT) -> Cumulative Risk: **694.2**
- **Archetype:** `file_cluster_4` (Distance: 14.416 IQR)
- **Magnitude:** 237.32 | **LOC:** 129 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `_redrawText` (Impact: 53.6), `moveEnd` (Impact: 4.9), `draw` (Impact: 2.2)

### 6. `graf2d/asimage/src/libAfterImage/zlib/zutil.c` (C) -> Cumulative Risk: **691.51**
- **Archetype:** `file_cluster_8` (Distance: 13.045 IQR)
- **Magnitude:** 235.62 | **LOC:** 319 | **CtrlFlow:** 76.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8388%)
- **Heaviest Functions:** `zlibCompileFlags` (Impact: 42.1), `zcalloc` (Impact: 7.0), `zcfree` (Impact: 7.0)

### 7. `graf2d/win32gdk/gdk/src/gdk/win32/gdkim-win32.c` (C) -> Cumulative Risk: **690.95**
- **Archetype:** `file_cluster_13` (Distance: 13.673 IQR)
- **Magnitude:** 391.78 | **LOC:** 348 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.5292%)
- **Heaviest Functions:** `gdk_wcstombs` (Impact: 34.0), `gdk_nmbstowcs` (Impact: 22.9), `gdk_nmbstowchar_ts` (Impact: 18.7)

### 8. `js/modules/hist2d/TH2Painter.mjs` (JAVASCRIPT) -> Cumulative Risk: **687.86**
- **Archetype:** `file_cluster_4` (Distance: 14.514 IQR)
- **Magnitude:** 5800.02 | **LOC:** 3845 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (94.1845%), Tech Debt (86.9293%)
- **Heaviest Functions:** `drawBinsCandle` (Impact: 309.8), `constructor` (Impact: 276.9), `processTooltipEvent` (Impact: 230.9)

### 9. `js/modules/gpad/RFramePainter.mjs` (JAVASCRIPT) -> Cumulative Risk: **684.36**
- **Archetype:** `file_cluster_4` (Distance: 15.736 IQR)
- **Magnitude:** 2403.08 | **LOC:** 1303 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9564%), Safety Score (99.4348%)
- **Heaviest Functions:** `zoom` (Impact: 172.8), `fillContextMenu` (Impact: 64.0), `zoomSingle` (Impact: 59.8)

### 10. `ui5/canv/controller/Canvas.controller.js` (JAVASCRIPT) -> Cumulative Risk: **684.28**
- **Archetype:** `file_cluster_4` (Distance: 14.116 IQR)
- **Magnitude:** 880.44 | **LOC:** 801 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9831%), Tech Debt (97.9386%)
- **Heaviest Functions:** `showLeftArea` (Impact: 57.7), `onFileMenuAction` (Impact: 48.7), `closeMethodDialog` (Impact: 46.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `builtins/glew/src/glew.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.929 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.533 IQR)
- **Top Global Matches:** file_cluster_8: 14.929, file_cluster_7: 15.321, file_cluster_0: 15.412
- **Magnitude:** 128986.48 | **LOC:** 28582 | **CtrlFlow:** 96.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5937%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3594`, `structural_boundaries: 148`, `args: 9`, `func_start: 124`
* *Risk/State:* `state_mutation: 8363`
* *Architecture:* `api: 918`, `import: 3`
* *Defense:* `safety: 6`, `immutability_locks: 1550`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eglew.h, stdio.h, wglew.h, stddef.h, dyld.h, AvailabilityMacros.h, string.h, glew.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `roottest/scripts/Rules.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.693 IQR)
- **Top Global Matches:** file_cluster_17: 11.693, file_cluster_8: 12.057, file_cluster_11: 12.063
- **Magnitude:** 15819.02 | **LOC:** 907 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.0033%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 136`, `args: 32`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 87`, `dead_code: 8`
* *Architecture:* `io: 102`, `api: 55`, `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $(wildcard, Makefile.comp, FixCling.mk, Common.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `net/http/civetweb/civetweb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.238 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.336 IQR)
- **Top Global Matches:** file_cluster_8: 15.238, file_cluster_13: 15.369, file_cluster_11: 15.391
- **Magnitude:** 12788.14 | **LOC:** 23203 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.4206%), Tech Debt (12.6401%)
**Top Internal Functions/Classes:**
  * `dav_move_file` (Impact: 1070.7)
  * `connect_socket` (Impact: 232.6)
  * `mg_start_worker_thread` (Impact: 151.9)
  * `interpret_uri` (Impact: 143.0)
  * `mg_get_connection_info` (Impact: 130.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3044`, `structural_boundaries: 1491`, `args: 265`, `func_start: 256`, `class_start: 225`
* *Risk/State:* `safety_bypasses: 89`, `high_risk_execution: 4`, `state_mutation: 6290`, `dead_code: 10`, `planned_debt: 27`, `fragile_debt: 2`, `orphaned_logic: 31`
* *Architecture:* `io: 141`, `api: 1598`, `concurrency: 104`, `import: 86`
* *Defense:* `safety: 169`, `doc: 3`, `sync_locks: 17`, `immutability_locks: 401`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` tcp.h, kernel.h, http2.inl, ctype.h, stdarg.h, inet.h, socket.h, version.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `math/minuit/src/TMinuit.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.439 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.082 IQR)
- **Top Global Matches:** file_cluster_7: 16.439, file_cluster_8: 16.464, file_cluster_13: 16.567
- **Magnitude:** 12749.92 | **LOC:** 7899 | **CtrlFlow:** 90.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.2009%), Tech Debt (47.6182%)
**Top Internal Functions/Classes:**
  * `TMinuit::mnexcm` (Impact: 453.3)
  * `TMinuit::mnset` (Impact: 305.6)
  * `TMinuit::mncros` (Impact: 229.2)
  * `TMinuit::mnhelp` (Impact: 210.8)
  * `TMinuit::mnline` (Impact: 202.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1908`, `structural_boundaries: 210`, `args: 78`, `func_start: 76`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 8749`, `dead_code: 22`, `planned_debt: 3`, `fragile_debt: 7`, `duplicate_logic: 5`, `orphaned_logic: 70`
* *Architecture:* `import: 10`
* *Defense:* `safety: 7`, `doc: 2529`, `test: 2`, `immutability_locks: 135`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` TROOT.h, atomic, TPluginManager.h, TError.h, TMinuit.h, cstdio, TList.h, TMath.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/minicern/src/zebra.f` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.119 IQR)
- **Top Global Matches:** file_cluster_8: 15.119, file_cluster_11: 15.155, file_cluster_0: 15.27
- **Magnitude:** 12040.58 | **LOC:** 7291 | **CtrlFlow:** 93.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3382%), Tech Debt (11.6007%)
**Top Internal Functions/Classes:**
  * `MZLIFT` (Impact: 368.5)
  * `MZPUSH` (Impact: 293.0)
  * `MZIOCH` (Impact: 274.1)
  * `RZOPEN` (Impact: 209.1)
  * `MZRELB` (Impact: 178.4)
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

### `graf2d/win32gdk/src/TGWin32.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_7` (Drift: 17.39 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.539 IQR)
- **Top Global Matches:** file_cluster_7: 17.39, file_cluster_13: 17.475, file_cluster_8: 17.503
- **Magnitude:** 10693.58 | **LOC:** 7848 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.0045%), Tech Debt (98.9255%)
**Top Internal Functions/Classes:**
  * `TGWin32::MapGCValues` (Impact: 248.0)
  * `TGWin32::MapEvent` (Impact: 211.9)
  * `TGWin32::RequestString` (Impact: 181.4)
  * `TGWin32::UpdateMarkerStyle` (Impact: 178.6)
  * `TGWin32::RequestLocator` (Impact: 105.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1320`, `structural_boundaries: 432`, `args: 346`, `func_start: 242`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 7192`, `dead_code: 28`, `fragile_debt: 1`, `duplicate_logic: 22`, `orphaned_logic: 207`
* *Architecture:* `io: 7`, `api: 1`, `import: 34`
* *Defense:* `doc: 7155`, `sync_locks: 1`, `immutability_locks: 48`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` TColor.h, stdio.h, TROOT.h, TObjString.h, gdkkeysyms.h, ctype.h, TString.h, TMath.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `math/mathcore/src/TKDTree.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.764 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.727 IQR)
- **Top Global Matches:** file_cluster_13: 16.764, file_cluster_11: 16.81, file_cluster_7: 16.908
- **Magnitude:** 9794.0 | **LOC:** 1248 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.3922%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 103`, `args: 36`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 780`, `dead_code: 15`
* *Architecture:* `import: 5`
* *Defense:* `doc: 635`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` limits, TRandom.h, cstring, TString.h, TKDTree.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/spectrum/src/TSpectrum2Fit.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.409 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 3.863 IQR)
- **Top Global Matches:** file_cluster_7: 16.409, file_cluster_8: 16.437, file_cluster_13: 16.57
- **Magnitude:** 9117.1 | **LOC:** 5877 | **CtrlFlow:** 93.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.3116%), Tech Debt (19.9585%)
**Top Internal Functions/Classes:**
  * `TSpectrum2Fit::FitAwmi` (Impact: 593.1)
    * *Intent:* /// nfound = s->SearchHighRes(source, dest, nbinsx, nbinsy, 2, 2, kTRUE, 100, kFALSE, 3); /// printf...
  * `TSpectrum2Fit::FitStiefel` (Impact: 553.9)
    * *Intent:* /// printf("Found %d candidate peaks\n",nfound); /// Bool_t *FixPosX = new Bool_t[nfound]; /// Bool_...
  * `TSpectrum2Fit::Shape2` (Impact: 100.4)
  * `TSpectrum2Fit::SetPeakParameters` (Impact: 85.4)
  * `TSpectrum2Fit::SetFitParameters` (Impact: 71.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1068`, `structural_boundaries: 73`, `args: 139`, `func_start: 51`
* *Risk/State:* `state_mutation: 6987`, `dead_code: 27`, `duplicate_logic: 2`, `orphaned_logic: 48`
* *Architecture:* `import: 2`
* *Defense:* `doc: 2036`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TMath.h, TSpectrum2Fit.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graf2d/asimage/src/TASImage.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.911 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.918 IQR)
- **Top Global Matches:** file_cluster_7: 16.911, file_cluster_8: 16.981, file_cluster_13: 17.0
- **Magnitude:** 9096.1 | **LOC:** 6859 | **CtrlFlow:** 79.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.7042%), Tech Debt (55.3877%)
**Top Internal Functions/Classes:**
  * `TASImage::ReadImage` (Impact: 918.4)
  * `TASImage::CopyArea` (Impact: 179.0)
  * `TASImage::Paint` (Impact: 150.2)
  * `TASImage::MapFileTypes` (Impact: 150.0)
  * `TASImage::DrawText` (Impact: 128.9)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Return alpha-bl...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1197`, `structural_boundaries: 312`, `args: 126`, `func_start: 95`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 12`, `state_mutation: 5337`, `dead_code: 4`, `duplicate_logic: 17`, `orphaned_logic: 70`
* *Architecture:* `io: 10`, `import: 32`
* *Defense:* `safety: 1`, `doc: 3156`, `immutability_locks: 76`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` TColor.h, TROOT.h, TVirtualPS.h, RConfigure.h, TPluginManager.h, TVirtualPad.h, TGaxis.h, TMath.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tmva/tmva/inc/TMVA/DNN/Architectures/TCudnn.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.729 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 7.141 IQR)
- **Top Global Matches:** file_cluster_13: 15.729, file_cluster_11: 15.905, file_cluster_8: 16.029
- **Magnitude:** 8362.98 | **LOC:** 1048 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.9729%), Tech Debt (8.8768%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 209`, `args: 151`, `func_start: 50`, `class_start: 4`
* *Risk/State:* `state_mutation: 661`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 2`, `doc: 174`, `immutability_locks: 154`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Functions.h, ConvLayer.h, ContextHandles.h, MaxPoolLayer.h, RConfigure.h, BatchNormLayer.h, cudnn.h, LSTMLayer.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graf2d/gpad/src/TPad.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 17.579 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.913 IQR)
- **Top Global Matches:** file_cluster_13: 17.579, file_cluster_7: 17.635, file_cluster_8: 17.759
- **Magnitude:** 8090.38 | **LOC:** 7683 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (48.0897%), Tech Debt (77.4722%)
**Top Internal Functions/Classes:**
  * `TPad::Close` (Impact: 1047.8)
  * `TPad::ExecuteEvent` (Impact: 534.0)
  * `TPad::PaintHatches` (Impact: 280.2)
  * `TPad::ExecuteEventAxis` (Impact: 256.2)
  * `TPad::ClipPolygon` (Impact: 132.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1040`, `structural_boundaries: 222`, `args: 174`, `func_start: 103`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4622`, `dead_code: 16`, `duplicate_logic: 10`, `orphaned_logic: 91`
* *Architecture:* `import: 51`
* *Defense:* `safety: 1`, `doc: 3548`, `immutability_locks: 72`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` TColor.h, cstring, TROOT.h, TVirtualPS.h, TPluginManager.h, TImage.h, TExec.h, TDataMember.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/hist/src/TH1.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 18.318 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.403 IQR)
- **Top Global Matches:** file_cluster_13: 18.318, file_cluster_7: 18.424, file_cluster_11: 18.496
- **Magnitude:** 8077.82 | **LOC:** 10696 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (47.2601%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `TH1::Clone` (Impact: 1091.8)
  * `TH1::LabelsOption` (Impact: 887.1)
  * `TH1::KolmogorovTest` (Impact: 614.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Copy this histo...
  * `TH1::TransformHisto` (Impact: 99.8)
    * *Intent:* /// /// The status of the fit is obtained converting the TFitResultPtr to an integer /// independent...
  * `TH1::DoIntegral` (Impact: 88.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 804`, `structural_boundaries: 325`, `args: 237`, `func_start: 206`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3617`, `dead_code: 44`, `planned_debt: 1`, `duplicate_logic: 102`, `orphaned_logic: 91`
* *Architecture:* `import: 45`
* *Defense:* `safety: 1`, `doc: 6779`, `immutability_locks: 234`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` cctype, cstring, TROOT.h, DataRange.h, TPluginManager.h, TVirtualPad.h, TH1Merger.h, fstream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/modules/d3.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.275 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.388 IQR)
- **Top Global Matches:** file_cluster_11: 14.275, file_cluster_8: 14.277, file_cluster_17: 14.492
- **Magnitude:** 7949.92 | **LOC:** 6881 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.7023%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `formatLocale$1` (Impact: 110.7)
  * `formatLocale` (Impact: 102.4)
  * `arc` (Impact: 101.4)
  * `newFormat` (Impact: 93.8)
  * `arc` (Impact: 69.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1442`, `structural_boundaries: 1467`, `args: 940`, `func_start: 830`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 109`, `high_risk_execution: 3`, `state_mutation: 2475`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 227`
* *Architecture:* `io: 11`, `api: 44`, `concurrency: 23`
* *Defense:* `safety: 368`, `test: 3`, `immutability_locks: 113`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/histpainter/src/THistPainter.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.657 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.368 IQR)
- **Top Global Matches:** file_cluster_13: 16.657, file_cluster_8: 16.684, file_cluster_7: 16.714
- **Magnitude:** 7858.72 | **LOC:** 11904 | **CtrlFlow:** 90.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (39.466%), Tech Debt (17.5301%)
**Top Internal Functions/Classes:**
  * `THistPainter::MakeChopt` (Impact: 314.0)
  * `THistPainter::PaintContour` (Impact: 238.5)
  * `THistPainter::PaintErrors` (Impact: 199.7)
  * `THistPainter::ShowProjection3` (Impact: 199.0)
  * `THistPainter::DistancetoPrimitive` (Impact: 177.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1230`, `structural_boundaries: 137`, `args: 115`, `func_start: 33`
* *Risk/State:* `high_risk_execution: 58`, `state_mutation: 5462`, `dead_code: 6`, `duplicate_logic: 2`, `orphaned_logic: 30`
* *Architecture:* `import: 55`
* *Defense:* `safety: 3`, `doc: 996`, `immutability_locks: 17`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` cctype, TColor.h, cstring, TROOT.h, TImage.h, TPluginManager.h, TGaxis.h, THStack.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tree/treeplayer/src/TTreeFormula.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.774 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.3 IQR)
- **Top Global Matches:** file_cluster_13: 16.774, file_cluster_11: 16.877, file_cluster_7: 16.917
- **Magnitude:** 7514.12 | **LOC:** 5986 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.9764%), Tech Debt (74.3489%)
**Top Internal Functions/Classes:**
  * `TTreeFormula::GetRealInstance` (Impact: 1039.8)
  * `TTreeFormula::EvalInstance` (Impact: 501.8)
  * `TTreeFormula::LoadCurrentDim` (Impact: 119.7)
  * `TTreeFormula::RegisterDimensions` (Impact: 85.5)
  * `TTreeFormula::ResetDimensions` (Impact: 84.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1591`, `structural_boundaries: 289`, `args: 74`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4847`, `dead_code: 26`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 22`, `orphaned_logic: 21`
* *Architecture:* `api: 1`, `import: 41`
* *Defense:* `safety: 14`, `doc: 1139`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` TLeafElement.h, cctype, TROOT.h, TVirtualCollectionProxy.h, TTreeFormula.h, TLeafB.h, TString.h, strlcpy.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `math/matrix/src/TDecompSparse.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.291 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.736 IQR)
- **Top Global Matches:** file_cluster_8: 16.291, file_cluster_7: 16.325, file_cluster_13: 16.519
- **Magnitude:** 7424.12 | **LOC:** 2730 | **CtrlFlow:** 94.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.213%), Tech Debt (60.7371%)
**Top Internal Functions/Classes:**
  * `TDecompSparse::Factor_sub2` (Impact: 601.1)
  * `TDecompSparse::InitPivot_sub2` (Impact: 412.9)
  * `TDecompSparse::Factor` (Impact: 258.3)
  * `TDecompSparse::InitPivot_sub1` (Impact: 159.2)
  * `TDecompSparse::InitPivot` (Impact: 151.3)
    * *Intent:* // set initial value of "Treat As Zero" parameter
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 704`, `structural_boundaries: 45`, `args: 41`, `func_start: 28`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 4777`, `fragile_debt: 6`, `duplicate_logic: 7`, `orphaned_logic: 20`
* *Architecture:* `import: 2`
* *Defense:* `doc: 762`, `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TMath.h, TDecompSparse.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builtins/nlohmann/json.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.773 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.655 IQR)
- **Top Global Matches:** file_cluster_11: 15.773, file_cluster_13: 15.818, file_cluster_8: 15.836
- **Magnitude:** 7329.8 | **LOC:** 25678 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.9519%), Tech Debt (8.0485%)
**Top Internal Functions/Classes:**
  * `operator<=>` (Impact: 15.1)
    * *Intent:* /*! */
  * `replace_substring` (Impact: 4.5)
    * *Intent:* #endif #if JSON_USE_IMPLICIT_CONVERSIONS #define JSON_EXPLICIT #else #define JSON_EXPLICIT explicit ...
  * `escape` (Impact: 2.1)
    * *Intent:* /////////////////////////// // JSON type enumeration // ///////////////////////////
  * `unescape` (Impact: 2.0)
  * `operator<` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2908`, `structural_boundaries: 2804`, `args: 984`, `func_start: 428`, `class_start: 134`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 7055`, `dead_code: 31`, `planned_debt: 4`, `fragile_debt: 3`
* *Architecture:* `io: 2`, `api: 30`, `import: 136`
* *Defense:* `safety: 166`, `doc: 1559`, `immutability_locks: 700`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cctype, cstring, istream, streambuf, iomanip, map, tuple, optional...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `gui/guibuilder/src/TGuiBldDragManager.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.723 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.363 IQR)
- **Top Global Matches:** file_cluster_7: 16.723, file_cluster_13: 16.77, file_cluster_8: 16.834
- **Magnitude:** 6550.28 | **LOC:** 6332 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.3113%), Tech Debt (96.884%)
**Top Internal Functions/Classes:**
  * `TGuiBldMenuDialog::Build` (Impact: 1057.1)
  * `TGuiBldDragManager::Drop` (Impact: 440.2)
  * `TGuiBldDragManager::HandleKey` (Impact: 150.7)
  * `TGuiBldDragManager::Menu4Frame` (Impact: 98.4)
  * `TGuiBldDragManager::HandleEvent` (Impact: 83.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1025`, `structural_boundaries: 321`, `args: 194`, `func_start: 115`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3108`, `dead_code: 12`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 14`, `orphaned_logic: 95`
* *Architecture:* `api: 2`, `import: 41`
* *Defense:* `safety: 2`, `doc: 3448`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` TColor.h, TROOT.h, TImage.h, TObjString.h, TRootGuiBuilder.h, TToggle.h, TGLabel.h, TDataMember.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `roofit/xroofit/src/xRooNode.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 19.002 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 6.45 IQR)
- **Top Global Matches:** file_cluster_11: 19.002, file_cluster_13: 19.061, file_cluster_17: 19.179
- **Magnitude:** 6408.12 | **LOC:** 12616 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.492%), Tech Debt (25.0844%)
**Top Internal Functions/Classes:**
  * `xRooNode::_ShowVars_` (Impact: 863.5)
    * *Intent:* //o->SetCall(o,"BlahBlah","Option_t*",-1); l->AddFirst(o);*/
  * `xRooNode::Remove` (Impact: 754.3)
  * `xRooNode::Browse` (Impact: 140.1)
  * `xRooNode::Checked` (Impact: 90.6)
  * `xRooNode::IntegralAndError` (Impact: 41.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1470`, `structural_boundaries: 665`, `args: 231`, `func_start: 59`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4192`, `dead_code: 160`, `planned_debt: 10`, `fragile_debt: 3`, `duplicate_logic: 2`, `orphaned_logic: 21`
* *Architecture:* `api: 2`, `import: 96`
* *Defense:* `safety: 63`, `doc: 310`, `immutability_locks: 93`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 72):` RooSimultaneous.h, RooAddition.h, RooUniformBinning.h, RooJSONFactoryWSTool.h, RooBinSamplingPdf.h, TTimeStamp.h, TFrame.h, TStopwatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/minicern/src/hbook.f` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.608 IQR)
- **Top Global Matches:** file_cluster_8: 14.608, file_cluster_11: 14.768, file_cluster_0: 14.839
- **Magnitude:** 6205.96 | **LOC:** 4127 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5501%), Tech Debt (12.0567%)
**Top Internal Functions/Classes:**
  * `HGNT2` (Impact: 289.4)
  * `HRIN` (Impact: 122.6)
  * `HPATH` (Impact: 116.8)
  * `HGNT1` (Impact: 89.6)
  * `HGIVE` (Impact: 70.5)
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

### `hist/spectrum/src/TSpectrum2Transform.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.374 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 3.963 IQR)
- **Top Global Matches:** file_cluster_7: 16.374, file_cluster_8: 16.392, file_cluster_13: 16.461
- **Magnitude:** 6131.66 | **LOC:** 2788 | **CtrlFlow:** 95.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.3253%), Tech Debt (18.4165%)
**Top Internal Functions/Classes:**
  * `TSpectrum2Transform::General2` (Impact: 573.5)
  * `TSpectrum2Transform::Transform` (Impact: 249.9)
    * *Intent:* /// To execute this example, do /// /// `root > .x Transform2.C` /// /// ~~~ {.cpp} /// void Transfo...
  * `TSpectrum2Transform::FilterZonal` (Impact: 240.1)
    * *Intent:* /// `root > .x Filter2.C` /// /// ~~~ {.cpp} /// void Filter2() { /// Int_t i, j; /// Int_t nbinsx =...
  * `TSpectrum2Transform::Enhance` (Impact: 238.4)
    * *Intent:* /// \image html spectrum2transform_enhance_image002.jpg Fig. 2 Enhanced spectrum of the data from Fi...
  * `TSpectrum2Transform::FourCos2` (Impact: 237.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 827`, `structural_boundaries: 37`, `args: 22`, `func_start: 21`
* *Risk/State:* `state_mutation: 4124`, `dead_code: 19`, `duplicate_logic: 2`, `orphaned_logic: 18`
* *Architecture:* `import: 2`
* *Defense:* `doc: 864`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TMath.h, TSpectrum2Transform.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/histpainter/src/TPainter3dAlgorithms.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.474 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.615 IQR)
- **Top Global Matches:** file_cluster_7: 16.474, file_cluster_8: 16.49, file_cluster_13: 16.572
- **Magnitude:** 6003.74 | **LOC:** 5780 | **CtrlFlow:** 90.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.9058%), Tech Debt (27.3676%)
**Top Internal Functions/Classes:**
  * `TPainter3dAlgorithms::IsoSurface` (Impact: 394.5)
  * `TPainter3dAlgorithms::ImplicitFunction` (Impact: 274.3)
  * `TPainter3dAlgorithms::MarchingCube` (Impact: 268.5)
  * `TPainter3dAlgorithms::ZDepth` (Impact: 247.1)
  * `TPainter3dAlgorithms::SurfaceSpherical` (Impact: 154.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 775`, `structural_boundaries: 84`, `args: 29`, `func_start: 29`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 3738`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 26`
* *Architecture:* `import: 14`
* *Defense:* `doc: 1029`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` TColor.h, TROOT.h, TStyle.h, Hparam.h, TH1.h, TVirtualPad.h, TF3.h, Hoption.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/modules/hist2d/TH2Painter.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.514 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.058 IQR)
- **Top Global Matches:** file_cluster_4: 14.514, file_cluster_8: 14.583, file_cluster_11: 14.655
- **Magnitude:** 5800.02 | **LOC:** 3845 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.0277%), Tech Debt (86.9293%)
**Top Internal Functions/Classes:**
  * `drawBinsCandle` (Impact: 309.8)
  * `constructor` (Impact: 276.9)
  * `processTooltipEvent` (Impact: 230.9)
  * `addMainTriangle` (Impact: 208.7)
  * `produceCandlePoint` (Impact: 190.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1352`, `structural_boundaries: 404`, `args: 132`, `func_start: 128`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1851`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 36`
* *Architecture:* `io: 35`, `api: 11`, `concurrency: 181`, `import: 7`
* *Defense:* `safety: 275`, `doc: 49`, `immutability_locks: 194`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.mjs, colors.mjs, d3.mjs, ObjectPainter.mjs, THistPainter.mjs, menu.mjs, BasePainter.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/modules/gpad/TFramePainter.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.918 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.745 IQR)
- **Top Global Matches:** file_cluster_4: 15.918, file_cluster_11: 15.984, file_cluster_17: 16.089
- **Magnitude:** 5689.38 | **LOC:** 3345 | **CtrlFlow:** 75.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (60.0001%), Tech Debt (61.9015%)
**Top Internal Functions/Classes:**
  * `processFrameTooltipEvent` (Impact: 294.2)
  * `makeResizeElements` (Impact: 256.2)
  * `zoom` (Impact: 191.3)
  * `addDragHandler` (Impact: 160.5)
  * `fillContextMenu` (Impact: 150.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1113`, `structural_boundaries: 370`, `args: 212`, `func_start: 154`, `class_start: 3`
* *Risk/State:* `state_mutation: 2734`, `dead_code: 13`, `duplicate_logic: 30`
* *Architecture:* `io: 15`, `api: 16`, `concurrency: 146`, `import: 9`
* *Defense:* `safety: 340`, `doc: 117`, `immutability_locks: 132`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.mjs, TAxisPainter.mjs, d3.mjs, FontHandler.mjs, ObjectPainter.mjs, TAttLineHandler.mjs, menu.mjs, utils.mjs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `geom/geom/src/TGeoTube.cxx` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.714 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.782 IQR)
- **Top Global Matches:** file_cluster_7: 16.714, file_cluster_8: 16.798, file_cluster_13: 16.864
- **Magnitude:** 5688.0 | **LOC:** 3572 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.6419%), Tech Debt (92.3484%)
**Top Internal Functions/Classes:**
  * `TGeoTubeSeg::DistFromOutsideS` (Impact: 345.6)
  * `TGeoCtub::DistFromOutside` (Impact: 137.6)
  * `TGeoTube::DistFromOutsideS` (Impact: 80.7)
  * `TGeoTubeSeg::SafetyS` (Impact: 54.6)
  * `TGeoTubeSeg::DistFromInsideS` (Impact: 53.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 601`, `structural_boundaries: 271`, `args: 123`, `func_start: 103`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 3987`, `dead_code: 6`, `duplicate_logic: 22`, `orphaned_logic: 78`
* *Architecture:* `import: 8`
* *Defense:* `doc: 3051`, `immutability_locks: 177`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` TGeoTube.h, iostream, TGeoVolume.h, TVirtualGeoPainter.h, TBuffer3DTypes.h, TMath.h, TBuffer3D.h, TGeoManager.h
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
- `bindings/pyroot/cppyy/cppyy/python/cppyy/_pythonization.py` (PYTHON) | Magnitude: 562.78 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 224, branch: 86, structural_boundaries: 86, state_mutation: 42
- `interpreter/llvm-project/llvm/include/llvm/ProfileData/SymbolRemappingReader.h` (CPP) | Magnitude: 16.76 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 20, doc: 19, structural_boundaries: 8, func_start: 6
- `interpreter/llvm-project/llvm/include/llvm/Analysis/MustExecute.h` (CPP) | Magnitude: 232.2 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: doc: 242, state_mutation: 176, indent_spaces: 168, immutability_locks: 101
- `builtins/zstd/compress/zstd_fast.c` (C) | Magnitude: 792.68 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 502, indent_spaces: 353, immutability_locks: 174, api: 160

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `tutorials/visualisation/graphics/triangles.C` (C) | Magnitude: 71.52 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 35, doc: 16, pointers: 16
- `core/cont/src/THashTable.cxx` (CPP) | Magnitude: 435.76 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 824, state_mutation: 319, indent_spaces: 226, pointers: 83
- `tutorials/hist/hist057_TExec_th1.C` (C) | Magnitude: 35.34 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 22, doc: 15, indent_spaces: 14, pointers: 12
- `core/cont/src/TExMap.cxx` (CPP) | Magnitude: 473.14 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 533, state_mutation: 305, indent_spaces: 228, branch: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `math/minuit2/src/MnLineSearch.cxx` (CPP) | Magnitude: 1127.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 870, indent_spaces: 532, branch: 138, dead_code: 25
- `math/smatrix/inc/Math/Dsinv.h` (CPP) | Magnitude: 210.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 165, indent_spaces: 76, branch: 20, structural_boundaries: 13
- `js/modules/d3.mjs` (JAVASCRIPT) | Magnitude: 7949.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4430, state_mutation: 2475, structural_boundaries: 1467, branch: 1442
- `ui5/browser/model/BrowserModel.js` (JAVASCRIPT) | Magnitude: 987.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 538, indent_spaces: 417, branch: 162, structural_boundaries: 88
- `tmva/sofie/inc/TMVA/ROperator_Einsum.hxx` (CPP) | Magnitude: 578.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 411, indent_spaces: 234, branch: 71, structural_boundaries: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `bindings/pyroot/cppyy/cppyy-backend/clingwrapper/src/precommondefs.h` (CPP) | Magnitude: 29.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 18, state_mutation: 12, reflection_metaprogramming: 9, branch: 6
- `builtins/zstd/common/huf.h` (CPP) | Magnitude: 54.06 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 82, structural_boundaries: 56, safety_bypasses: 52, args: 37
- `interpreter/llvm-project/clang/utils/bash-autocomplete.sh` (SHELL) | Magnitude: 73.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 36, indent_spaces: 34, state_mutation: 30, safety_bypasses: 16
- `interpreter/llvm-project/llvm/utils/crosstool/ARM/build-install-linux.sh` (SHELL) | Magnitude: 78.98 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, reflection_metaprogramming: 85, structural_boundaries: 46, branch: 42
- `misc/win/ld.sh` (SHELL) | Magnitude: 72.16 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, branch: 33, state_mutation: 27, reflection_metaprogramming: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `interpreter/llvm-project/clang/include/clang/Parse/Parser.h` (CPP) | Magnitude: 802.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1109, state_mutation: 484, doc: 476, pointers: 272
- `interpreter/llvm-project/llvm/include/llvm/DebugInfo/PDB/Native/InfoStreamBuilder.h` (CPP) | Magnitude: 22.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 18, state_mutation: 12, immutability_locks: 8
- `tmva/tmva/inc/TMVA/RuleEnsemble.h` (CPP) | Magnitude: 664.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 360, indent_spaces: 334, structural_boundaries: 155, immutability_locks: 151
- `tree/dataframe/src/RJittedFilter.cxx` (CPP) | Magnitude: 49.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, pointers: 27, structural_boundaries: 19, func_start: 18
- `builtins/zstd/compress/zstd_compress_sequences.h` (C) | Magnitude: 44.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 27, immutability_locks: 24, indent_spaces: 23, safety: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `graf2d/graf/src/TLatex.cxx` (CPP) | Magnitude: 4637.22 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 2932, indent_spaces: 2061, doc: 845, branch: 699
- `tutorials/visualisation/webcanv/latex_url.cxx` (CPP) | Magnitude: 15.8 | Delta: **0.268 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 16, state_mutation: 12, indent_spaces: 7, pointers: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `interpreter/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/Shared/WrapperFunctionUtils.h` (CPP) | Magnitude: 575.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 419, state_mutation: 356, structural_boundaries: 315, args: 181
- `math/experimental/genvectorx/inc/MathX/GenVectorX/Transform3D.h` (CPP) | Magnitude: 891.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 641, state_mutation: 609, structural_boundaries: 304, immutability_locks: 178
- `interpreter/llvm-project/llvm/include/llvm/ADT/ilist.h` (CPP) | Magnitude: 300.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 207, indent_spaces: 163, structural_boundaries: 111, doc: 40
- `interpreter/llvm-project/llvm/include/llvm/Support/Chrono.h` (CPP) | Magnitude: 80.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 79, indent_spaces: 63, doc: 43, state_mutation: 37
- `math/mathcore/inc/VectorizedTMath.h` (CPP) | Magnitude: 219.58 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 169, structural_boundaries: 137, indent_spaces: 122, doc: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tmva/tmva/src/DNN/Architectures/Cpu/Regularization.hxx` (CPP) | Magnitude: 142.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 125, indent_spaces: 83, doc: 47, pointers: 32
- `roottest/scripts/FixCling.mk` (MAKEFILE) | Magnitude: 37.82 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 29, state_mutation: 22, structural_boundaries: 17, branch: 6
- `tutorials/roofit/roostats/ModelInspector.py` (PYTHON) | Magnitude: 213.82 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 393, state_mutation: 76, branch: 40, structural_boundaries: 34
- `tutorials/roofit/roostats/StandardBayesianNumericalDemo.py` (PYTHON) | Magnitude: 9.38 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, branch: 20, structural_boundaries: 13, debug_prints: 12
- `ui5/fitpanel/controller/FitPanel.controller.js` (JAVASCRIPT) | Magnitude: 193.7 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_11`
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
- `interpreter/llvm-project/clang/tools/include-mapping/cppreference_parser.py` (PYTHON) | Magnitude: 0.15 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 39, branch: 37, state_mutation: 24
- `js/modules/hist2d/THistPainter.mjs` (JAVASCRIPT) | Magnitude: 4957.96 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 2296, state_mutation: 2237, branch: 1106, structural_boundaries: 271
- `js/modules/hist2d/TScatterPainter.mjs` (JAVASCRIPT) | Magnitude: 208.38 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 135, state_mutation: 77, branch: 51, structural_boundaries: 39
- `interpreter/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/MemoryMapper.h` (CPP) | Magnitude: 37.24 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 44, pointers: 26, args: 22
- `js/modules/gpad/TAxisPainter.mjs` (JAVASCRIPT) | Magnitude: 4087.62 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1819, indent_spaces: 1210, branch: 648, structural_boundaries: 201

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `math/mathcore/inc/Math/IFunction.h` (CPP) | Magnitude: 73.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 52, doc: 46, immutability_locks: 38
- `roofit/roostats/inc/RooStats/TestStatistic.h` (CPP) | Magnitude: 19.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 9, doc: 8, immutability_locks: 7
- `roofit/roofitmore/src/RooNonCentralChiSquare.cxx` (CPP) | Magnitude: 76.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 55, doc: 54, indent_spaces: 38, branch: 10
- `interpreter/llvm-project/clang/include/clang/Format/Format.h` (CPP) | Magnitude: 321.34 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 1837, indent_spaces: 323, state_mutation: 208, dead_code: 151
- `interpreter/llvm-project/llvm/include/llvm/Support/ExponentialBackoff.h` (CPP) | Magnitude: 8.22 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 13, state_mutation: 5, dead_code: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `graf3d/gl/src/TGL5DDataSetEditor.cxx` (CPP) | Magnitude: 110.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 680, indent_spaces: 165, pointers: 132, structural_boundaries: 33
- `gui/fitpanelv7/src/RFitPanelModel.cxx` (CPP) | Magnitude: 454.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 287, indent_spaces: 252, doc: 243, branch: 93
- `gui/guibuilder/src/TGuiBldHintsEditor.cxx` (CPP) | Magnitude: 453.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 421, pointers: 316, state_mutation: 310, doc: 297
- `hist/hist/src/TH2.cxx` (CPP) | Magnitude: 4542.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4787, state_mutation: 2315, indent_spaces: 1479, pointers: 535
- `math/mathcore/inc/TRandom1.h` (CPP) | Magnitude: 8.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 154, indent_spaces: 29, structural_boundaries: 14, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `bindings/pyroot/cppyy/cppyy/bench/support.py` (PYTHON) | Magnitude: 7.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, ipc_rpc_bridges: 4, branch: 2
- `ui5/eve7/index.html` (HTML) | Magnitude: 14.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 11, state_mutation: 6, branch: 4
- `bindings/pyroot/cppyy/CPyCppyy/src/Pythonize.cxx` (CPP) | Magnitude: 1280.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 860, indent_spaces: 839, branch: 271, structural_boundaries: 147
- `interpreter/llvm-project/clang/include/clang/AST/CommentVisitor.h` (CPP) | Magnitude: 15.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 17, macros: 14, args: 13
- `interpreter/llvm-project/clang/tools/libclang/CIndexUSRs.cpp` (CPP) | Magnitude: 0.05 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, args: 28, structural_boundaries: 19, state_mutation: 19

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

- `tree/ntuple/src/RFieldMeta.cxx` -> Churn: **90.01%** | Cog Load: 86.8128% | Debt: 99.9996%
- `tree/dataframe/inc/ROOT/RDF/RInterface.hxx` -> Churn: **88.66%** | Cog Load: 29.5551% | Debt: 99.9973%
- `tree/ntuple/src/RField.cxx` -> Churn: **80.14%** | Cog Load: 57.7005% | Debt: 99.6123%
- `tree/dataframe/inc/ROOT/RDF/InterfaceUtils.hxx` -> Churn: **72.37%** | Cog Load: 37.9629% | Debt: 99.9998%
- `bindings/pyroot/pythonizations/python/ROOT/_facade.py` -> Churn: **68.79%** | Cog Load: 41.7923% | Debt: 88.3013%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `roottest/scripts/Rules.mk` -> **Jonas Rembser** (100.0% isolated ownership) | Magnitude: 15819.02
- `math/mathcore/src/TKDTree.cxx` -> **ferdymercury** (100.0% isolated ownership) | Magnitude: 9794.0
- `graf2d/asimage/src/TASImage.cxx` -> **Sergey Linev** (100.0% isolated ownership) | Magnitude: 9096.1
- `math/matrix/src/TDecompSparse.cxx` -> **mdessole** (100.0% isolated ownership) | Magnitude: 7424.12
- `hist/histpainter/src/TPainter3dAlgorithms.cxx` -> **Sergey Linev** (100.0% isolated ownership) | Magnitude: 6003.74

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

- `core/base/inc/Rtypes.h` -> **Severity: 1001.124** (Blast Radius: 55.99 * Doc Risk: 17.8804%)
- `core/foundation/inc/DllImport.h` -> **Severity: 808.546** (Blast Radius: 33.49 * Doc Risk: 24.1429%)
- `gui/gui/inc/TGFrame.h` -> **Severity: 480.9** (Blast Radius: 4.809 * Doc Risk: 100.0%)
- `core/foundation/inc/RtypesCore.h` -> **Severity: 420.167** (Blast Radius: 35.248 * Doc Risk: 11.9203%)
- `core/base/inc/TString.h` -> **Severity: 340.943** (Blast Radius: 19.068 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
