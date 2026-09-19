# ARCHITECTURAL_BRIEF: root
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/root-project/root.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 22504 analyzed artifact(s), 4903428 LOC.
- **Load-bearing artifact:** `interpreter/llvm-project/clang/lib/Headers/llvm_libc_wrappers/string.h` -- 1805 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `interpreter/llvm-project/llvm/lib/Passes/PassBuilder.cpp` -- pulls in 332 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `builtins/glew/src/glew.c` at magnitude 29666.36 (structural weight, not risk).
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
| Total Artifacts | 31167 |
| Analyzed Artifacts (Scanned) | 22504 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8663 |
| Total LOC | 4903428 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 72.2% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6619 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0733 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2352 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 948 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 14719 | 4090586 | 65.4% |
| C | 3229 | 429065 | 14.3% |
| PLAINTEXT | 1184 | 0 | 5.3% |
| XML | 936 | 0 | 4.2% |
| PYTHON | 930 | 97011 | 4.1% |
| MARKDOWN | 308 | 0 | 1.4% |
| HTML | 197 | 23814 | 0.9% |
| MAKEFILE | 196 | 33303 | 0.9% |
| JAVASCRIPT | 150 | 90394 | 0.7% |
| TD | 129 | 87206 | 0.6% |
| OBJECTIVE-C | 122 | 17534 | 0.5% |
| BINARY_THREAT | 122 | 122 | 0.5% |
| SHELL | 117 | 4457 | 0.5% |
| M4 | 38 | 3228 | 0.2% |
| BATCH | 29 | 544 | 0.1% |
| JSON | 28 | 1651 | 0.1% |
| CSS | 20 | 2249 | 0.1% |
| YAML | 13 | 303 | 0.1% |
| PERL | 11 | 2896 | 0.0% |
| CSV | 9 | 150 | 0.0% |
| DOCKERFILE | 5 | 129 | 0.0% |
| FORTRAN | 4 | 12570 | 0.0% |
| ASSEMBLY | 3 | 5423 | 0.0% |
| PROTO | 2 | 118 | 0.0% |
| POWERSHELL | 1 | 6 | 0.0% |
| APEX | 1 | 655 | 0.0% |
| SQLITE | 1 | 14 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `4.163`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +4.16; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 19%, Large Core Modules (3) 18%, Declarative / Non-Code 15%, Parameter Forwarders Files 8%, Large Core Modules 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 20890 | 92.8% |
| Unknown | 122 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1492 | 6.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8663*

**Composition by Extension & Reason:**
- `.rst`: 1316x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 34x Excluded (Unsupported Extension: '.rst')
- `.cpp`: 1129x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1636 LOC), 1x Excluded (Machine-Generated Source Code Signature: 188 LOC)
- `.h`: 759x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 34x Excluded (Machine-Generated Source Code Signature: 30 LOC), 28x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `.ref`: 1046x Excluded (Unsupported Extension: '.ref')
- `.png`: 892x Excluded (Explicitly Denied Extension: '.png')
- `.td`: 529x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 9029 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2144 LOC)
- `.xpm`: 396x Excluded (Unsupported Extension: '.xpm')
- `.root`: 323x Excluded (Unsupported Extension: '.root')
- `.txt`: 207x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 9 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1081 LOC)
- `.jpg`: 191x Excluded (Explicitly Denied Extension: '.jpg')
- `.cmake`: 128x Excluded (Unsupported Extension: '.cmake'), 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.cmake)
- `.tex`: 96x Excluded (Unsupported Extension: '.tex')
- `no_extension`: 55x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 23x Unsupported Format (.undeterminable), 2x Unresolved Ambiguity (No Retainable Structure)
- `.gif`: 86x Excluded (Explicitly Denied Extension: '.gif')
- `.pdf`: 50x Excluded (Explicitly Denied Extension: '.pdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 18.1 | 5.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 43.5 | 54.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.6 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.2 | 1.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 17.0 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 90.0 | 1.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 51.8 | 57.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1390277 | 15446 | 123 | `interpreter/llvm-project/llvm/lib/Transforms/Vectorize/SLPVectorizer.cpp` |
| cleanup | 4646 | 1509 | 0 | `interpreter/llvm-project/clang/lib/Parse/ParsePragma.cpp` |
| guards | 529974 | 14413 | 54 | `builtins/glew/src/glew.c` |
| danger | 28794 | 4018 | 2 | `misc/minicern/src/zebra.f` |
| concurrency | 5295 | 660 | 0 | `gui/webdisplay/src/RWebWindow.cxx` |
| connectivity | 87910 | 11204 | 9 | `interpreter/llvm-project/clang/lib/Headers/avx512vlintrin.h` |
| io | 10660 | 1152 | 0 | `interpreter/llvm-project/clang/www/c_dr_status.html` |
| crypto | 4 | 4 | 0 | `bindings/distrdf/python/DistRDF/Backends/Base.py` |
| ipc | 1159 | 269 | 0 | `roofit/roofitcore/src/BidirMMapPipe.cxx` |
| time | 512 | 148 | 0 | `net/http/civetweb/civetweb.c` |
| serialization | 394 | 96 | 0 | `misc/minicern/src/zebra.f` |
| regex | 1399 | 242 | 0 | `interpreter/llvm-project/clang/tools/scan-build/bin/scan-build` |
| events | 4679 | 802 | 0 | `net/http/civetweb/civetweb.c` |
| tests | 20576 | 674 | 0 | `tree/ntuple/test/ntuple_types.cxx` |
| docs | 459365 | 11570 | 42 | `interpreter/llvm-project/clang/include/clang/ASTMatchers/ASTMatchers.h` |
| debt | 43371 | 5961 | 4 | `interpreter/llvm-project/clang/include/clang/AST/OpenMPClause.h` |
| mutation | 1208253 | 15710 | 113 | `builtins/glew/src/glew.c` |
| dead_code | 120526 | 10582 | 12 | `interpreter/llvm-project/clang/include/clang/ASTMatchers/ASTMatchers.h` |
| credential | 160 | 55 | 0 | `roottest/cling/template/typedef/cmspb_orig.C` |
| threat | 32379 | 9271 | 1 | `graf2d/win32gdk/gdk/src/gdk/gdkkeysyms.h` |
| ml_ai | 7110 | 591 | 0 | `interpreter/llvm-project/clang/lib/Headers/avx512fintrin.h` |
| ui | 1201 | 153 | 0 | `graf2d/cocoa/src/X11Events.mm` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `interpreter/llvm-project/clang/www/c_dr_status.html` (Hits: 896)
- `interpreter/llvm-project/clang/www/cxx_status.html` (Hits: 766)
- `interpreter/llvm-project/clang/www/c_status.html` (Hits: 424)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **string.h** (`interpreter/llvm-project/clang/lib/Headers/llvm_libc_wrappers/string.h`) — 1805 inbound connections
2. **memory.py** (`bindings/pyroot/pythonizations/test/memory.py`) — 1135 inbound connections
3. **raw_ostream.h** (`interpreter/llvm-project/llvm/include/llvm/Support/raw_ostream.h`) — 1068 inbound connections
4. **StringRef.h** (`interpreter/llvm-project/llvm/include/llvm/ADT/StringRef.h`) — 986 inbound connections
5. **SmallVector.h** (`interpreter/llvm-project/llvm/include/llvm/ADT/SmallVector.h`) — 876 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **PassBuilder.cpp** (`interpreter/llvm-project/llvm/lib/Passes/PassBuilder.cpp`) — 332 outbound dependencies
2. **atlasFlushedProjectHeaders.h** (`roottest/root/io/prefetching/atlasFlushed/atlasFlushedProjectHeaders.h`) — 255 outbound dependencies
3. **ASTReader.cpp** (`interpreter/llvm-project/clang/lib/Serialization/ASTReader.cpp`) — 153 outbound dependencies
4. **converters.h** (`graf2d/win32gdk/gdk/src/iconv/converters.h`) — 146 outbound dependencies
5. **TCling.cxx** (`core/metacling/src/TCling.cxx`) — 134 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inheritsFrom` **(Many-Argument Workhorses)** (@ `interpreter/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp`) -> Impact: **1814.8** | LOC: 525
  * *Intent:* /// inheritsFrom - Indicates whether all instructions in one class also belong /// to another class. /// /// @param child - The class that may be the ...
- `GIMatchTableExecutor::executeMatchTable` **(Many-Argument Workhorses)** (@ `interpreter/llvm-project/llvm/include/llvm/CodeGen/GlobalISel/GIMatchTableExecutorImpl.h`) -> Impact: **1538.2** | LOC: 1319
- `Sema::ActOnTag` **(Many-Argument Workhorses)** (@ `interpreter/llvm-project/clang/lib/Sema/SemaDecl.cpp`) -> Impact: **1448.1** | LOC: 1009
- `connect_socket` **(Many-Argument Workhorses)** (@ `net/http/civetweb/civetweb.c`) -> Impact: **1446.6** | LOC: 2514
- `TSpectrum3::SearchHighRes` **(Many-Argument Workhorses)** (@ `hist/spectrum/src/TSpectrum3.cxx`) -> Impact: **1439.0** | LOC: 1205
  * *Intent:* /// } /// } /// Double_t *PosX = new Double_t[nfound]; /// Double_t *PosY = new Double_t[nfound]; /// Double_t *PosZ = new Double_t[nfound]; /// PosX ...
- `TargetLowering::SimplifyDemandedBits` **(Many-Argument Workhorses)** (@ `interpreter/llvm-project/llvm/lib/CodeGen/SelectionDAG/TargetLowering.cpp`) -> Impact: **1413.6** | LOC: 1515
  * *Intent:* /// Look at Op. At this point, we know that only the OriginalDemandedBits of the /// result of Op are ever used downstream. If we can use this informa...
- `TFormula::Analyze` **(Many-Argument Workhorses)** (@ `hist/hist/src/TFormula_v5.cxx`) -> Impact: **1409.5** | LOC: 1150
  * *Intent:* /// /// and write your own constructor /// /// ~~~ {.cpp} /// MyClass::MyClass(const char *name,const char *expression) : TFormula() /// ~~~ /// /// w...
- `CodeGenFunction::EmitBuiltinExpr` **(Many-Argument Workhorses)** (@ `interpreter/llvm-project/clang/lib/CodeGen/CGBuiltin.cpp`) -> Impact: **1385.4** | LOC: 1368
- `SemaRISCV::CheckBuiltinFunctionCall` **(Many-Argument Workhorses)** (@ `interpreter/llvm-project/clang/lib/Sema/SemaRISCV.cpp`) -> Impact: **1363.0** | LOC: 819
- `upgradeX86IntrinsicCall` **(Many-Argument Workhorses)** (@ `interpreter/llvm-project/llvm/lib/IR/AutoUpgrade.cpp`) -> Impact: **1349.4** | LOC: 1140

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `interpreter/llvm-project/clang/lib/Sema` | 88 | 234868.92 | 45.79% | 70.46% |
| `interpreter/llvm-project/clang/lib/CodeGen` | 100 | 106369.12 | 29.68% | 58.89% |
| `interpreter/llvm-project/llvm/lib/CodeGen` | 243 | 105779.0 | 38.98% | 79.78% |
| `interpreter/llvm-project/clang/lib/AST` | 89 | 95516.74 | 42.18% | 81.01% |
| `interpreter/llvm-project/llvm/lib/CodeGen/SelectionDAG` | 33 | 91089.76 | 48.57% | 67.83% |
| `interpreter/llvm-project/llvm/lib/Analysis` | 120 | 77198.32 | 39.8% | 83.54% |
| `hist/hist/src` | 72 | 74268.58 | 37.46% | 67.87% |
| `tmva/sofie/test/input_models` | 122 | 61000.0 | 0.0% | 0.0% |
| `interpreter/llvm-project/llvm/lib/Transforms/Scalar` | 81 | 58111.14 | 39.55% | 61.4% |
| `geom/geom/src` | 53 | 55905.78 | 34.89% | 84.88% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_roofit/_roodecays.py` -> **100.0%** Exposure
- `geom/gdml/writer.py` -> **100.0%** Exposure
- `interpreter/llvm-project/clang/tools/scan-build-py/lib/libscanbuild/report.py` -> **100.0%** Exposure
- `roottest/python/pythonizations/PyROOT_smartptrtest.py` -> **100.0%** Exposure
- `roottest/python/regression/PyROOT_regressiontests.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bindings/distrdf/python/DistRDF/Backends/Base.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Backends/Utils.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/ComputationGraphGenerator.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/HeadNode.py` -> **100.0%** Exposure
- `bindings/distrdf/python/DistRDF/Ranges.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `interpreter/llvm-project/llvm/lib/IR/Core.cpp` -> **637** Orphaned Functions | **0** Duplicates
- `interpreter/llvm-project/clang/lib/Headers/lasxintrin.h` -> **537** Orphaned Functions | **0** Duplicates
- `interpreter/llvm-project/clang/tools/libclang/CIndex.cpp` -> **517** Orphaned Functions | **4** Duplicates
- `interpreter/llvm-project/clang/lib/Headers/lsxintrin.h` -> **519** Orphaned Functions | **0** Duplicates
- `interpreter/llvm-project/clang/include/clang/AST/OpenMPClause.h` -> **0** Orphaned Functions | **492** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `176` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `119433` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `builtins/glew/src/glew.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 29666.36 | **LOC:** 28582 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (90.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `glewContextInit` **(Compute Cores)** (Impact: 700.6)
  * `glewIsSupported` **(Many-Argument Workhorses)** (Impact: 442.0)
    * *Intent:* #endif
  * `eglewIsSupported` **(Many-Argument Workhorses)** (Impact: 254.5)
    * *Intent:* #elif defined(GLEW_EGL)
  * `_glewInit_GL_EXT_direct_state_access` **(Compute Cores)** (Impact: 226.1)
    * *Intent:* #endif /* GL_EXT_depth_bounds_test */ #ifdef GL_EXT_direct_state_access
  * `eglewInit` **(Many-Argument Workhorses)** (Impact: 182.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 7632 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 23109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5319`, `structural_boundaries: 1620`, `args: 95`, `func_start: 496`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7845`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 12`
* *Architecture:* `api: 23`, `import: 14`
* *Defense:* `safety: 7`, `immutability_locks: 4218`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` AvailabilityMacros.h, eglew.h, glew.h, glxew.h, osmesa.h, wglew.h, dlfcn.h, dyld.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/Sema/SemaOpenMP.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 23440.42 | **LOC:** 24325 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 76.4095% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SemaOpenMP::ActOnOpenMPExecutableDirective` **(Many-Argument Workhorses)** (Impact: 1118.4)
  * `actOnOMPReductionKindClause` **(Many-Argument Workhorses)** (Impact: 1118.2)
  * `checkOpenMPLoop` **(Many-Argument Workhorses)** (Impact: 374.2)
    * *Intent:* /// Called on a for stmt to check itself and nested loops (if any). /// \return Returns 0 if one of ...
  * `SemaOpenMP::ActOnOpenMPAtomicDirective` **(Many-Argument Workhorses)** (Impact: 364.2)
  * `SemaOpenMP::ActOnOpenMPSingleExprWithArgClause` **(Many-Argument Workhorses)** (Impact: 319.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1888 instances
* *State Mutation (weighted view):* 5932
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6392`, `structural_boundaries: 2477`, `args: 5075`, `func_start: 674`, `class_start: 40`
* *Risk/State:* `state_mutation: 2156`, `dead_code: 53`, `planned_debt: 15`, `fragile_debt: 3`, `duplicate_logic: 6`, `unreferenced_by_name: 324`
* *Architecture:* `api: 24`, `import: 35`
* *Defense:* `safety: 317`, `doc: 515`, `immutability_locks: 783`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` TreeTransform.h, ASTContext.h, ASTMutationListener.h, CXXInheritance.h, Decl.h, DeclCXX.h, DeclOpenMP.h, DynamicRecursiveASTVisitor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/llvm/lib/CodeGen/SelectionDAG/DAGCombiner.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 20213.32 | **LOC:** 29254 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **62**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%), Debt Markers (formerly Tech Debt) (72.1%)
- **Documentation Coverage:** 70.9751% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DAGCombiner::visitVECTOR_SHUFFLE` **(Compute Cores)** (Impact: 344.2)
  * `DAGCombiner::visit` **(Compute Cores)** (Impact: 241.9)
  * `DAGCombiner::tryStoreMergeOfLoads` **(Many-Argument Workhorses)** (Impact: 221.0)
  * `DAGCombiner::visitAND` **(Compute Cores)** (Impact: 213.0)
  * `DAGCombiner::visitTRUNCATE` **(Compute Cores)** (Impact: 203.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1265 instances
* *State Mutation (weighted view):* 3872
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8160`, `structural_boundaries: 3414`, `args: 7037`, `func_start: 439`, `class_start: 9`
* *Risk/State:* `state_mutation: 1342`, `dead_code: 46`, `planned_debt: 158`, `fragile_debt: 67`, `unreferenced_by_name: 271`
* *Architecture:* `api: 4`, `import: 62`
* *Defense:* `safety: 239`, `doc: 617`, `immutability_locks: 370`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 54):` MatchContext.h, algorithm, cassert, cstdint, functional, iterator, APFloat.h, APInt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/llvm/lib/Transforms/Vectorize/SLPVectorizer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 19958.28 | **LOC:** 22018 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **82**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.2%)
- **Documentation Coverage:** 43.9206% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BoUpSLP::vectorizeTree` **(Many-Argument Workhorses)** (Impact: 666.4)
  * `BoUpSLP::buildTree_rec` **(Many-Argument Workhorses)** (Impact: 640.8)
  * `BoUpSLP::getEntryCost` **(Many-Argument Workhorses)** (Impact: 597.0)
  * `tryToReduce` **(Many-Argument Workhorses)** (Impact: 534.2)
    * *Intent:* /// Attempt to vectorize the tree found by matchAssociativeReduction.
  * `BoUpSLP::isGatherShuffledSingleRegisterEntry` **(Many-Argument Workhorses)** (Impact: 513.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1953 instances
* *State Mutation (weighted view):* 6005
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6498`, `structural_boundaries: 2725`, `args: 5920`, `func_start: 401`, `class_start: 36`
* *Risk/State:* `state_mutation: 2099`, `dead_code: 27`, `planned_debt: 37`, `fragile_debt: 13`, `duplicate_logic: 2`, `unreferenced_by_name: 96`
* *Architecture:* `api: 14`, `import: 82`
* *Defense:* `safety: 482`, `doc: 1150`, `immutability_locks: 794`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 73):` algorithm, cassert, cstdint, iterator, DenseMap.h, DenseSet.h, PriorityQueue.h, STLExtras.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `net/http/civetweb/civetweb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 19748.38 | **LOC:** 23203 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **77**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.0%), Guard Balance (formerly Safety Score) (90.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `connect_socket` **(Many-Argument Workhorses)** (Impact: 1446.6)
  * `gmt_time_string` **(Many-Argument Workhorses)** (Impact: 969.0)
    * *Intent:* /* Convert time_t to a string. According to RFC2616, Sec 14.18, this must be * included in all respo...
  * `handle_request` **(Many-Argument Workhorses)** (Impact: 723.1)
    * *Intent:* /* This is the heart of the Civetweb's logic. * This function is called when the request is read, pa...
  * `mg_start_worker_thread` **(Many-Argument Workhorses)** (Impact: 561.9)
  * `uninitialize_openssl` **(I/O & Config Routines)** (Impact: 454.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 2147 instances
* *Concurrency (weighted view):* 114
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 6596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3994`, `structural_boundaries: 2235`, `args: 1351`, `func_start: 370`, `class_start: 295`
* *Risk/State:* `safety_bypasses: 121`, `high_risk_execution: 11`, `state_mutation: 2302`, `dead_code: 15`, `planned_debt: 50`, `fragile_debt: 3`, `unreferenced_by_name: 38`
* *Architecture:* `io: 59`, `api: 154`, `concurrency: 29`, `import: 92`
* *Defense:* `safety: 233`, `doc: 6`, `sync_locks: 27`, `immutability_locks: 545`, `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` inet.h, civetweb.h, ctype.h, direct.h, dirent.h, dlfcn.h, errno.h, external_log_access.inl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/Sema/SemaExpr.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 19448.22 | **LOC:** 21235 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **67**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (82.4%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 75.2033% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sema::CheckCompareOperands` **(Many-Argument Workhorses)** (Impact: 502.9)
    * *Intent:* // C99 6.5.8, C++ [expr.rel]
  * `Sema::CheckVectorOperands` **(Many-Argument Workhorses)** (Impact: 337.4)
  * `Sema::DiagnoseAssignmentResult` **(Many-Argument Workhorses)** (Impact: 333.8)
  * `Sema::CreateBuiltinBinOp` **(Many-Argument Workhorses)** (Impact: 307.0)
  * `Sema::BuildResolvedCallExpr` **(Many-Argument Workhorses)** (Impact: 306.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1359 instances
* *State Mutation (weighted view):* 4137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5879`, `structural_boundaries: 2245`, `args: 3775`, `func_start: 463`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1419`, `dead_code: 46`, `planned_debt: 7`, `fragile_debt: 100`, `duplicate_logic: 18`, `unreferenced_by_name: 208`
* *Architecture:* `api: 10`, `concurrency: 2`, `import: 76`
* *Defense:* `safety: 226`, `doc: 408`, `immutability_locks: 487`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 63):` CheckExprLifetime.h, TreeTransform.h, UsedDeclVisitor.h, ASTConsumer.h, ASTContext.h, ASTLambda.h, ASTMutationListener.h, BuiltinTypes.def...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/CodeGen/CGBuiltin.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 18702.88 | **LOC:** 23478 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **72**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.4%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 62.0191% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CodeGenFunction::EmitBuiltinExpr` **(Many-Argument Workhorses)** (Impact: 1385.4)
  * `CodeGenFunction::EmitX86BuiltinExpr` **(Many-Argument Workhorses)** (Impact: 1294.1)
  * `CodeGenFunction::EmitCommonNeonBuiltinExpr` **(Many-Argument Workhorses)** (Impact: 1026.4)
  * `CodeGenFunction::EmitAArch64BuiltinExpr` **(Many-Argument Workhorses)** (Impact: 998.0)
  * `CodeGenFunction::EmitAMDGPUBuiltinExpr` **(Many-Argument Workhorses)** (Impact: 732.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1853 instances
* *State Mutation (weighted view):* 5787
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7557`, `structural_boundaries: 2439`, `args: 5450`, `func_start: 224`, `class_start: 11`
* *Risk/State:* `state_mutation: 2081`, `dead_code: 31`, `planned_debt: 17`, `fragile_debt: 22`, `unreferenced_by_name: 85`
* *Architecture:* `import: 76`
* *Defense:* `safety: 172`, `doc: 101`, `sync_locks: 1`, `immutability_locks: 293`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` ABIInfo.h, CGCUDARuntime.h, CGCXXABI.h, CGHLSLRuntime.h, CGObjCRuntime.h, CGOpenCLRuntime.h, CGRecordLayout.h, CGValue.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/Sema/SemaDecl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 18185.84 | **LOC:** 20452 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **57**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.7%), Debt Markers (formerly Tech Debt) (74.6%)
- **Documentation Coverage:** 83.815% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sema::ActOnTag` **(Many-Argument Workhorses)** (Impact: 1448.1)
  * `Sema::ActOnFunctionDeclarator` **(Many-Argument Workhorses)** (Impact: 1123.2)
  * `Sema::ActOnVariableDeclarator` **(Many-Argument Workhorses)** (Impact: 850.4)
  * `Sema::ActOnFields` **(Many-Argument Workhorses)** (Impact: 534.5)
  * `Sema::MergeFunctionDecl` **(Many-Argument Workhorses)** (Impact: 464.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 947 instances
* *State Mutation (weighted view):* 2893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5739`, `structural_boundaries: 1761`, `args: 3771`, `func_start: 344`, `class_start: 14`
* *Risk/State:* `state_mutation: 999`, `dead_code: 107`, `planned_debt: 22`, `fragile_debt: 95`, `duplicate_logic: 3`, `unreferenced_by_name: 172`
* *Architecture:* `api: 4`, `import: 57`
* *Defense:* `safety: 159`, `doc: 254`, `immutability_locks: 592`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 53):` TypeLocBuilder.h, algorithm, ASTConsumer.h, ASTContext.h, ASTLambda.h, CXXInheritance.h, CharUnits.h, Decl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/AST/ExprConstant.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 13625.16 | **LOC:** 18052 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.5%), Debt Markers (formerly Tech Debt) (88.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.9%)
- **Documentation Coverage:** 77.6262% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IntExprEvaluator::VisitBuiltinCallExpr` **(Many-Argument Workhorses)** (Impact: 860.1)
  * `EvaluateStmt` **(Many-Argument Workhorses)** (Impact: 437.2)
    * *Intent:* // Evaluate a statement.
  * `CheckICE` **(Many-Argument Workhorses)** (Impact: 425.3)
  * `EvaluateComparisonBinaryOperator` **(Many-Argument Workhorses)** (Impact: 332.9)
  * `PointerExprEvaluator::VisitBuiltinCallExpr` **(Many-Argument Workhorses)** (Impact: 234.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 792 instances
* *State Mutation (weighted view):* 2502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4702`, `structural_boundaries: 2663`, `args: 3907`, `func_start: 709`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 918`, `dead_code: 20`, `planned_debt: 11`, `fragile_debt: 109`, `duplicate_logic: 18`, `unreferenced_by_name: 191`
* *Architecture:* `api: 30`, `import: 46`
* *Defense:* `safety: 318`, `doc: 509`, `immutability_locks: 1334`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 40):` Context.h, Frame.h, State.h, ExprConstShared.h, APValue.h, ASTContext.h, ASTLambda.h, Attr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/Sema/SemaOverload.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 13619.84 | **LOC:** 16512 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (66.5%)
- **Documentation Coverage:** 71.1039% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IsStandardConversion` **(Many-Argument Workhorses)** (Impact: 371.4)
    * *Intent:* /// IsStandardConversion - Determines whether there is a standard /// conversion sequence (C++ [conv...
  * `Sema::CreateOverloadedBinOp` **(Many-Argument Workhorses)** (Impact: 332.4)
  * `clang::isBetterOverloadCandidate` **(Many-Argument Workhorses)** (Impact: 263.0)
    * *Intent:* /// isBetterOverloadCandidate - Determines whether the first overload /// candidate is a better cand...
  * `IsOverloadOrOverrideImpl` **(Many-Argument Workhorses)** (Impact: 248.2)
  * `Sema::AddOverloadCandidate` **(Many-Argument Workhorses)** (Impact: 237.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1059 instances
* *State Mutation (weighted view):* 3345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3782`, `structural_boundaries: 1528`, `args: 2383`, `func_start: 308`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1227`, `dead_code: 53`, `planned_debt: 17`, `fragile_debt: 80`, `unreferenced_by_name: 113`
* *Architecture:* `api: 6`, `import: 35`
* *Defense:* `safety: 162`, `doc: 434`, `immutability_locks: 360`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` CheckExprLifetime.h, algorithm, cassert, ASTContext.h, CXXInheritance.h, Decl.h, DeclCXX.h, DeclObjC.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/Sema/SemaDeclCXX.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 13504.94 | **LOC:** 19172 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **47**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Debt Markers (formerly Tech Debt) (83.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%)
- **Documentation Coverage:** 82.3266% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sema::ActOnCXXMemberDeclarator` **(Many-Argument Workhorses)** (Impact: 277.6)
  * `Sema::CheckCompletedCXXClass` **(Many-Argument Workhorses)** (Impact: 227.7)
  * `Sema::BuildUsingDeclaration` **(Many-Argument Workhorses)** (Impact: 199.9)
  * `CheckConstexprFunctionBody` **(Many-Argument Workhorses)** (Impact: 180.3)
    * *Intent:* /// Check the body for the given constexpr function declaration only contains /// the permitted type...
  * `CheckConstexprFunctionStmt` **(Many-Argument Workhorses)** (Impact: 178.8)
    * *Intent:* /// Check the provided statement is allowed in a constexpr function /// definition.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 862 instances
* *Memory Alloc (weighted view):* 30
* *State Mutation (weighted view):* 2661
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4316`, `structural_boundaries: 1779`, `args: 3561`, `func_start: 443`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 937`, `dead_code: 81`, `planned_debt: 11`, `fragile_debt: 91`, `duplicate_logic: 2`, `unreferenced_by_name: 223`
* *Architecture:* `api: 21`, `import: 47`
* *Defense:* `safety: 230`, `doc: 286`, `immutability_locks: 457`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` ASTConsumer.h, ASTContext.h, ASTMutationListener.h, CXXInheritance.h, CharUnits.h, ComparisonCategories.h, DeclCXX.h, DeclTemplate.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/llvm/lib/CodeGen/SelectionDAG/SelectionDAG.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 13034.54 | **LOC:** 13772 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **74**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (86.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%)
- **Documentation Coverage:** 79.8246% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SelectionDAG::computeKnownBits` **(Many-Argument Workhorses)** (Impact: 880.4)
    * *Intent:* /// Determine which bits of Op are known to be either zero or one and return /// them in Known. The ...
  * `SelectionDAG::getNode` **(Many-Argument Workhorses)** (Impact: 762.1)
  * `SelectionDAG::getNode` **(Many-Argument Workhorses)** (Impact: 539.0)
  * `SelectionDAG::ComputeNumSignBits` **(Many-Argument Workhorses)** (Impact: 529.2)
  * `SelectionDAG::FoldConstantArithmetic` **(Many-Argument Workhorses)** (Impact: 398.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 826 instances
* *State Mutation (weighted view):* 2574
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3964`, `structural_boundaries: 1571`, `args: 3587`, `func_start: 442`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 63`, `high_risk_execution: 1`, `state_mutation: 922`, `dead_code: 14`, `planned_debt: 45`, `fragile_debt: 30`, `unreferenced_by_name: 245`
* *Architecture:* `api: 2`, `import: 79`
* *Defense:* `safety: 432`, `doc: 260`, `sync_locks: 1`, `immutability_locks: 550`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 65):` SDNodeDbgValue.h, algorithm, cassert, cstdint, cstdlib, deque, limits, APFloat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/Sema/SemaChecking.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 12250.74 | **LOC:** 15088 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **101**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%), Complexity Load (formerly Cognitive Load) (65.4%)
- **Documentation Coverage:** 81.1083% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sema::CheckBuiltinFunctionCall` **(Many-Argument Workhorses)** (Impact: 1062.8)
  * `Sema::BuildAtomicExpr` **(Many-Argument Workhorses)** (Impact: 741.9)
  * `Sema::CheckImplicitConversion` **(Many-Argument Workhorses)** (Impact: 376.8)
  * `checkFormatStringExpr` **(Many-Argument Workhorses)** (Impact: 347.3)
    * *Intent:* // Determine if an expression is a string literal or constant string. // If this function returns fa...
  * `CheckPrintfHandler::checkFormatExpr` **(Many-Argument Workhorses)** (Impact: 263.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 743 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 2275
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4053`, `structural_boundaries: 1823`, `args: 2733`, `func_start: 394`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 789`, `dead_code: 28`, `planned_debt: 17`, `fragile_debt: 39`, `duplicate_logic: 6`, `unreferenced_by_name: 152`
* *Architecture:* `api: 11`, `import: 101`
* *Defense:* `safety: 137`, `doc: 267`, `immutability_locks: 846`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 91):` CheckExprLifetime.h, algorithm, cassert, cctype, APValue.h, ASTContext.h, Attr.h, AttrIterator.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/llvm/lib/Analysis/ScalarEvolution.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 12148.56 | **LOC:** 15980 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **74**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (89.5%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 85.0427% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ScalarEvolution::LoopGuards::collectFromBlock` **(Many-Argument Workhorses)** (Impact: 363.8)
  * `ScalarEvolution::getAddExpr` **(Many-Argument Workhorses)** (Impact: 272.8)
    * *Intent:* /// Get a canonical add expression, or something simpler if possible.
  * `ScalarEvolution::createSCEV` **(Compute Cores)** (Impact: 227.4)
  * `ScalarEvolution::howManyLessThans` **(Many-Argument Workhorses)** (Impact: 212.5)
  * `ScalarEvolution::isImpliedCondBalancedTypes` **(Many-Argument Workhorses)** (Impact: 208.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1017 instances
* *High Risk Execution (weighted view):* 12
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 3138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3665`, `structural_boundaries: 2185`, `args: 4312`, `func_start: 468`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 16`, `state_mutation: 1104`, `dead_code: 39`, `planned_debt: 34`, `fragile_debt: 16`, `duplicate_logic: 9`, `unreferenced_by_name: 276`
* *Architecture:* `api: 8`, `import: 74`
* *Defense:* `safety: 268`, `doc: 283`, `immutability_locks: 1887`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 62):` algorithm, cassert, climits, cstdint, cstdlib, APInt.h, ArrayRef.h, DenseMap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/spectrumpainter/src/TSpectrum2Painter.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 11856.46 | **LOC:** 7820 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TSpectrum2Painter::Paint` **(Many-Argument Workhorses)** (Impact: 446.0)
    * *Intent:* /// ~~~ /// root > .x VisA.C /// ~~~ /// ~~~ {.cpp} /// #include "TSpectrum2Painter.h" /// /// void ...
  * `TSpectrum2Painter::ColorModel` **(Many-Argument Workhorses)** (Impact: 205.9)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// This function c...
  * `TSpectrum2Painter::ColorCalculation` **(Many-Argument Workhorses)** (Impact: 190.2)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Calculates and ...
  * `TSpectrum2Painter::PaintSpectrum` **(Many-Argument Workhorses)** (Impact: 105.4)
    * *Intent:* /// - 7 = Triangle. /// /// cg(enable,color) channel grid. /// In addition to the surface drawn usin...
  * `TSpectrum2Painter::Envelope` **(Many-Argument Workhorses)** (Impact: 97.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Ensures hidden ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2955 instances
* *State Mutation (weighted view):* 10201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1959`, `structural_boundaries: 86`, `args: 43`, `func_start: 44`
* *Risk/State:* `state_mutation: 4291`, `dead_code: 5`, `unreferenced_by_name: 44`
* *Architecture:* `import: 14`
* *Defense:* `doc: 807`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` TBox.h, TColor.h, TEllipse.h, TF1.h, TGaxis.h, TH2.h, THLimitsFinder.h, TLine.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/llvm/lib/CodeGen/SelectionDAG/TargetLowering.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 11808.4 | **LOC:** 12117 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.8%), Complexity Load (formerly Cognitive Load) (85.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 74.3421% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TargetLowering::SimplifyDemandedBits` **(Many-Argument Workhorses)** (Impact: 1413.6)
    * *Intent:* /// Look at Op. At this point, we know that only the OriginalDemandedBits of the /// result of Op ar...
  * `TargetLowering::SimplifySetCC` **(Many-Argument Workhorses)** (Impact: 1259.4)
    * *Intent:* /// Try to simplify a setcc built with the specified operands and cc. If it is /// unable to simplif...
  * `TargetLowering::SimplifyDemandedVectorElts` **(Many-Argument Workhorses)** (Impact: 676.8)
  * `TargetLowering::softenSetCCOperands` **(Many-Argument Workhorses)** (Impact: 292.2)
  * `TargetLowering::LegalizeSetCCCondCode` **(Many-Argument Workhorses)** (Impact: 283.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 929 instances
* *State Mutation (weighted view):* 3015
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3154`, `structural_boundaries: 959`, `args: 2938`, `func_start: 152`
* *Risk/State:* `state_mutation: 1157`, `dead_code: 26`, `planned_debt: 61`, `fragile_debt: 28`, `unreferenced_by_name: 125`
* *Architecture:* `import: 24`
* *Defense:* `safety: 154`, `doc: 147`, `immutability_locks: 312`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` cctype, STLExtras.h, ValueTracking.h, VectorUtils.h, CallingConvLower.h, CodeGenCommonISel.h, MachineFrameInfo.h, MachineFunction.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/AST/ASTContext.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 11607.84 | **LOC:** 14749 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **98**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (98.3%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 71.0884% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DecodeTypeFromStr` **(Many-Argument Workhorses)** (Impact: 524.5)
    * *Intent:* //===----------------------------------------------------------------------===// // Builtin Type Com...
  * `ASTContext::mergeTypes` **(Many-Argument Workhorses)** (Impact: 370.7)
  * `ASTContext::getTypeInfoImpl` **(Compute Cores)** (Impact: 350.4)
    * *Intent:* /// getTypeInfoImpl - Return the size of the specified type, in bits. This /// method does not work ...
  * `ASTContext::getObjCEncodingForTypeImpl` **(Many-Argument Workhorses)** (Impact: 282.5)
    * *Intent:* // FIXME: Use SmallString for accumulating string.
  * `ASTContext::mergeFunctionTypes` **(Many-Argument Workhorses)** (Impact: 180.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 1047 instances
* *Memory Alloc (weighted view):* 101
* *State Mutation (weighted view):* 3292
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3597`, `structural_boundaries: 2254`, `args: 3083`, `func_start: 489`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 1198`, `dead_code: 43`, `planned_debt: 11`, `fragile_debt: 74`, `unreferenced_by_name: 368`
* *Architecture:* `import: 136`
* *Defense:* `safety: 329`, `doc: 386`, `immutability_locks: 1112`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 87):` Context.h, CXXABI.h, algorithm, cassert, APValue.h, ASTConcept.h, ASTContext.h, ASTMutationListener.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/histpainter/src/TPainter3dAlgorithms.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 11034.86 | **LOC:** 5780 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TPainter3dAlgorithms::IsoSurface` **(Many-Argument Workhorses)** (Impact: 334.4)
    * *Intent:* /// /// \param[in] ns number of iso-surfaces /// \param[in] s iso-surface values /// \param[in] nx n...
  * `TPainter3dAlgorithms::ImplicitFunction` **(Many-Argument Workhorses)** (Impact: 217.7)
    * *Intent:* /// Draw implicit function FUN(X,Y,Z) = 0 in cartesian coordinates using /// hidden surface removal ...
  * `TPainter3dAlgorithms::LegoSpherical` **(Many-Argument Workhorses)** (Impact: 213.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Draw stack of l...
  * `TPainter3dAlgorithms::MarchingCube` **(Many-Argument Workhorses)** (Impact: 202.0)
    * *Intent:* /// Topological decider for "Marching Cubes" algorithm Find set of triangles /// approximating the i...
  * `TPainter3dAlgorithms::ZDepth` **(Many-Argument Workhorses)** (Impact: 183.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Z-depth algorit...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2265 instances
* *State Mutation (weighted view):* 7018
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1441`, `structural_boundaries: 386`, `args: 76`, `func_start: 67`
* *Risk/State:* `state_mutation: 2488`, `dead_code: 1`, `unreferenced_by_name: 65`
* *Architecture:* `import: 14`
* *Defense:* `doc: 446`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` Hoption.h, Hparam.h, TColor.h, TF3.h, TH1.h, THLimitsFinder.h, THistPainter.h, TMath.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `math/minuit/src/TMinuit.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 10986.22 | **LOC:** 7899 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (41.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TMinuit::mnexcm` **(Many-Argument Workhorses)** (Impact: 316.9)
    * *Intent:* /// IERFLG is now (94.5) defined the same as ICONDN in MNCOMD = /// - 0: command executed normally /...
  * `TMinuit::mnline` **(Many-Argument Workhorses)** (Impact: 202.3)
    * *Intent:* /// Perform a line search from position START /// /// along direction STEP, where the length of vect...
  * `TMinuit::mncros` **(Many-Argument Workhorses)** (Impact: 179.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Find point wher...
  * `TMinuit::mnhelp` **(Many-Argument Workhorses)** (Impact: 141.8)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// HELP routine fo...
  * `TMinuit::mnset` **(I/O & Config Routines)** (Impact: 138.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Interprets the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2507 instances
* *State Mutation (weighted view):* 7857
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1473`, `structural_boundaries: 645`, `args: 78`, `func_start: 78`
* *Risk/State:* `state_mutation: 2843`, `dead_code: 22`, `planned_debt: 3`, `fragile_debt: 7`, `unreferenced_by_name: 73`
* *Architecture:* `import: 10`
* *Defense:* `safety: 7`, `doc: 579`, `test: 2`, `immutability_locks: 135`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` TClass.h, TError.h, TList.h, TMath.h, TMinuit.h, TPluginManager.h, TROOT.h, atomic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/Serialization/ASTReader.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 10808.76 | **LOC:** 12884 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **153**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Guard Balance (formerly Safety Score) (91.6%), Complexity Load (formerly Cognitive Load) (91.2%)
- **Documentation Coverage:** 90.0192% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ASTReader::ReadASTBlock` **(Many-Argument Workhorses)** (Impact: 545.5)
  * `ASTReader::ReadControlBlock` **(Many-Argument Workhorses)** (Impact: 300.7)
  * `ASTReader::readASTFileControlBlock` **(Many-Argument Workhorses)** (Impact: 272.8)
  * `ASTReader::GetType` **(Compute Cores)** (Impact: 265.4)
  * `OMPClauseReader::readClause` **(Compute Cores)** (Impact: 219.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1409 instances
* *State Mutation (weighted view):* 4432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2865`, `structural_boundaries: 1362`, `args: 2626`, `func_start: 495`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1614`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 87`, `unreferenced_by_name: 409`
* *Architecture:* `api: 9`, `import: 155`
* *Defense:* `safety: 163`, `doc: 130`, `immutability_locks: 272`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 138):` ASTCommon.h, ASTReaderInternals.h, TemplateArgumentHasher.h, algorithm, cassert, ASTConsumer.h, ASTContext.h, ASTMutationListener.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/llvm/lib/Analysis/ValueTracking.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 10658.14 | **LOC:** 10305 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **67**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%), Complexity Load (formerly Cognitive Load) (75.5%)
- **Documentation Coverage:** 76.6169% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `computeKnownFPClass` **(Many-Argument Workhorses)** (Impact: 1174.8)
  * `computeKnownBitsFromOperator` **(Many-Argument Workhorses)** (Impact: 846.4)
  * `isKnownNonZeroFromOperator` **(Many-Argument Workhorses)** (Impact: 389.5)
  * `llvm::fcmpImpliesClass` **(Many-Argument Workhorses)** (Impact: 317.4)
  * `ComputeNumSignBitsImpl` **(Many-Argument Workhorses)** (Impact: 245.5)
    * *Intent:* /// Return the number of times the sign bit of the register is replicated into /// the other bits. W...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 563 instances
* *State Mutation (weighted view):* 1701
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3475`, `structural_boundaries: 1273`, `args: 2344`, `func_start: 201`, `class_start: 1`
* *Risk/State:* `state_mutation: 575`, `dead_code: 19`, `planned_debt: 42`, `fragile_debt: 12`, `unreferenced_by_name: 78`
* *Architecture:* `import: 67`
* *Defense:* `safety: 106`, `doc: 167`, `immutability_locks: 736`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 58):` algorithm, cassert, cstdint, APFloat.h, APInt.h, ArrayRef.h, STLExtras.h, ScopeExit.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `interpreter/llvm-project/clang/lib/Driver/ToolChains/Clang.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 10279.54 | **LOC:** 9383 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **60**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 86.5979% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Clang::ConstructJob` **(Many-Argument Workhorses)** (Impact: 1342.7)
  * `RenderFloatingPointOptions` **(Many-Argument Workhorses)** (Impact: 682.5)
  * `renderDebugOptions` **(Many-Argument Workhorses)** (Impact: 385.7)
  * `CollectArgsForIntegratedAssembler` **(Many-Argument Workhorses)** (Impact: 323.9)
  * `Clang::AddPreprocessingOptions` **(Many-Argument Workhorses)** (Impact: 263.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1344 instances
* *State Mutation (weighted view):* 4113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2710`, `structural_boundaries: 350`, `args: 1359`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `state_mutation: 1425`, `dead_code: 7`, `planned_debt: 11`, `fragile_debt: 29`, `unreferenced_by_name: 35`
* *Architecture:* `import: 60`
* *Defense:* `safety: 42`, `doc: 31`, `immutability_locks: 462`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 53):` AMDGPU.h, AArch64.h, ARM.h, CSKY.h, LoongArch.h, M68k.h, Mips.h, PPC.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/histpainter/src/THistPainter.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 10271.76 | **LOC:** 11904 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.2%)
- **Documentation Coverage:** 1.4085% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THistPainter::MakeChopt` **(Compute Cores)** (Impact: 260.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Decode string `...
  * `THistPainter::ShowProjection3` **(Many-Argument Workhorses)** (Impact: 199.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Show projection...
  * `THistPainter::PaintContour` **(Compute Cores)** (Impact: 196.4)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Control functi...
  * `THistPainter::PaintSurface` **(Compute Cores)** (Impact: 190.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Control functi...
  * `THistPainter::PaintErrors` **(Compute Cores)** (Impact: 173.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Draw 1D histog...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1893 instances
* *State Mutation (weighted view):* 5936
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2513`, `structural_boundaries: 259`, `args: 231`, `func_start: 71`
* *Risk/State:* `state_mutation: 2150`, `dead_code: 17`, `fragile_debt: 1`, `unreferenced_by_name: 69`
* *Architecture:* `import: 55`
* *Defense:* `safety: 3`, `doc: 225`, `immutability_locks: 39`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` Hoption.h, Hparam.h, TArrow.h, TCandle.h, TCanvas.h, TColor.h, TCrown.h, TCutG.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/spectrum/src/TSpectrum3.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 10222.96 | **LOC:** 4422 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TSpectrum3::SearchHighRes` **(Many-Argument Workhorses)** (Impact: 1439.0)
    * *Intent:* /// } /// } /// Double_t *PosX = new Double_t[nfound]; /// Double_t *PosY = new Double_t[nfound]; //...
  * `TSpectrum3::SearchFast` **(Many-Argument Workhorses)** (Impact: 1221.9)
    * *Intent:* /// - source-pointer to the matrix of source spectrum /// - ssizex-x length of source spectrum /// -...
  * `TSpectrum3::SmoothMarkov` **(Many-Argument Workhorses)** (Impact: 368.0)
    * *Intent:* /// } /// } /// s->SmoothMarkov(source,nbinsx,nbinsy,nbinsz,3); /// for (i = 0; i < nbinsx; i++){ //...
  * `TSpectrum3::Background` **(Many-Argument Workhorses)** (Impact: 325.9)
    * *Intent:* /// } /// } /// strcpy(PATH,"spectra3/back_peaks_5ds.spe"); /// out=fopen(PATH,"wb"); /// for(i=0;i<...
  * `TSpectrum3::Deconvolution` **(Many-Argument Workhorses)** (Impact: 250.4)
    * *Intent:* /// } /// } /// s->Deconvolution(source,resp,nbinsx,nbinsy,nbinsz,10,10,2); /// for (i = 0; i < nbin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2054 instances
* *State Mutation (weighted view):* 6468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1105`, `structural_boundaries: 37`, `args: 11`, `func_start: 13`
* *Risk/State:* `state_mutation: 2360`, `dead_code: 69`, `unreferenced_by_name: 9`
* *Architecture:* `import: 4`
* *Defense:* `doc: 645`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` TH3.h, TMath.h, TSpectrum3.h, TVirtualPad.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `roofit/xroofit/src/xRooNode.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 9940.36 | **LOC:** 12616 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **80**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.8%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 91.5033% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xRooNode::BuildHistogram` **(Many-Argument Workhorses)** (Impact: 1160.7)
  * `xRooNode::Draw` **(Many-Argument Workhorses)** (Impact: 615.2)
  * `xRooNode::Add` **(Many-Argument Workhorses)** (Impact: 545.1)
  * `xRooNode::Multiply` **(Many-Argument Workhorses)** (Impact: 327.9)
  * `xRooNode::SetBinContent` **(Many-Argument Workhorses)** (Impact: 202.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 971 instances
* *Memory Alloc (weighted view):* 73
* *State Mutation (weighted view):* 2954
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3673`, `structural_boundaries: 1649`, `args: 589`, `func_start: 159`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1012`, `dead_code: 349`, `planned_debt: 32`, `fragile_debt: 4`, `duplicate_logic: 6`, `unreferenced_by_name: 99`
* *Architecture:* `api: 7`, `import: 96`
* *Defense:* `safety: 183`, `doc: 38`, `immutability_locks: 224`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 79):` RVersion.h, RooAbsArg.h, RooAbsData.h, RooAddPdf.h, RooAddition.h, RooBinSamplingPdf.h, RooBinning.h, RooCategory.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tree/ntuple/src/RFieldMeta.cxx` -> Churn: **90.01%** | Cog Load: 69.5039% | Debt: 99.9114%
- `tree/ntuple/src/RField.cxx` -> Churn: **80.14%** | Cog Load: 20.0226% | Debt: 98.1797%
- `bindings/pyroot/pythonizations/python/ROOT/_facade.py` -> Churn: **68.79%** | Cog Load: 78.5192% | Debt: 10.4763%
- `graf2d/gpad/src/TPad.cxx` -> Churn: **67.52%** | Cog Load: 47.8031% | Debt: 63.2027%
- `interpreter/cling/lib/Interpreter/CIFactory.cpp` -> Churn: **67.05%** | Cog Load: 70.8303% | Debt: 74.7435%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `interpreter/llvm-project/clang/lib/Sema/SemaOpenMP.cpp` -> **Devajith Valaparambil Sreeramaswamy** (100.0% isolated ownership) | Magnitude: 23440.42
- `interpreter/llvm-project/clang/lib/Sema/SemaExpr.cpp` -> **Devajith Valaparambil Sreeramaswamy** (100.0% isolated ownership) | Magnitude: 19448.22
- `interpreter/llvm-project/clang/lib/CodeGen/CGBuiltin.cpp` -> **Devajith Valaparambil Sreeramaswamy** (100.0% isolated ownership) | Magnitude: 18702.88
- `interpreter/llvm-project/clang/lib/Sema/SemaDecl.cpp` -> **Devajith Valaparambil Sreeramaswamy** (100.0% isolated ownership) | Magnitude: 18185.84
- `interpreter/llvm-project/clang/lib/AST/ExprConstant.cpp` -> **Devajith Valaparambil Sreeramaswamy** (100.0% isolated ownership) | Magnitude: 13625.16

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `interpreter/llvm-project/llvm/include/llvm/ADT/DenseMap.h` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 98.5688%)
- `interpreter/llvm-project/llvm/include/llvm/ADT/SmallVector.h` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 78.5102%)
- `io/io/inc/TFile.h` -> **Severity: 0.006** (Bridge: 0.0005 * Flux: 11.6431%)
- `core/base/inc/TObject.h` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 38.9651%)
- `core/base/inc/Bytes.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `interpreter/llvm-project/clang/lib/Headers/llvm_libc_wrappers/string.h` -> **Severity: 26.767** (Embedded: 0.275 * Error Risk: 97.3403%)
- `bindings/pyroot/pythonizations/test/memory.py` -> **Severity: 13.179** (Embedded: 0.2028 * Error Risk: 64.9934%)
- `core/base/inc/Rtypes.h` -> **Severity: 12.198** (Embedded: 0.1544 * Error Risk: 79.0109%)
- `core/base/inc/TObject.h` -> **Severity: 11.402** (Embedded: 0.1328 * Error Risk: 85.8697%)
- `core/base/inc/TStorage.h` -> **Severity: 10.733** (Embedded: 0.1076 * Error Risk: 99.7395%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/base/inc/Rtypes.h` -> **Severity: 1768.6** (Blast Radius: 17.686 * Doc Risk: 100.0%)
- `core/base/inc/TString.h` -> **Severity: 1043.341** (Blast Radius: 10.667 * Doc Risk: 97.8102%)
- `interpreter/llvm-project/llvm/include/llvm/ADT/iterator.h` -> **Severity: 863.6** (Blast Radius: 8.636 * Doc Risk: 100.0%)
- `roottest/root/io/simple/cstring.C` -> **Severity: 798.8** (Blast Radius: 7.988 * Doc Risk: 100.0%)
- `core/base/inc/TNamed.h` -> **Severity: 647.3** (Blast Radius: 6.473 * Doc Risk: 100.0%)

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
