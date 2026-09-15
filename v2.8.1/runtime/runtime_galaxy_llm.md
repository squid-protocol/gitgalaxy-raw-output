# ARCHITECTURAL_BRIEF: runtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dotnet/runtime.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 57632 |
| Analyzed Artifacts (Scanned) | 41176 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16456 |
| Total LOC | 7662011 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.4% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6477 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2853 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1112 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 715 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 31685 | 5678786 | 77.0% |
| CPP | 3376 | 1266003 | 8.2% |
| C | 1952 | 553660 | 4.7% |
| XML | 1557 | 1994 | 3.8% |
| PLAINTEXT | 812 | 5 | 2.0% |
| MARKDOWN | 368 | 0 | 0.9% |
| ASSEMBLY | 304 | 48375 | 0.7% |
| YAML | 185 | 11798 | 0.4% |
| SHELL | 185 | 18842 | 0.4% |
| TYPESCRIPT | 181 | 28465 | 0.4% |
| JSON | 166 | 5987 | 0.4% |
| MAKEFILE | 73 | 6733 | 0.2% |
| PYTHON | 59 | 15005 | 0.1% |
| POWERSHELL | 53 | 3815 | 0.1% |
| BATCH | 50 | 2366 | 0.1% |
| JAVASCRIPT | 49 | 3539 | 0.1% |
| HTML | 34 | 928 | 0.1% |
| M4 | 33 | 1175 | 0.1% |
| OBJECTIVE-C | 24 | 3017 | 0.1% |
| SWIFT | 10 | 9609 | 0.0% |
| DOCKERFILE | 7 | 171 | 0.0% |
| PERL | 5 | 894 | 0.0% |
| JAVA | 5 | 345 | 0.0% |
| CSV | 2 | 496 | 0.0% |
| CSS | 1 | 3 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.80; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 16%, Large Core Modules 15%, Tests & Verification Files 13%, Declarative / Non-Code 11%, Data / Markup / Trivial 11%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 39992 | 97.1% |
| Unknown | 5 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1175 | 2.9% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16456*

**Composition by Extension & Reason:**
- `.csproj`: 5719x Unsupported Format (.csproj), 123x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.csproj')
- `.il`: 3378x Unsupported Format (.il), 219x Excluded: Neighborhood Micro-Mass Limit Exceeded, 169x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ilproj`: 2748x Unsupported Format (.ilproj), 120x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 469x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.props`: 326x Unsupported Format (.props), 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Excluded (Unsupported Extension: '.props')
- `.cs`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Saturation: Line 15 exceeds 500 chars), 6x Excluded (Saturation: Line 22 exceeds 500 chars)
- `.targets`: 159x Unsupported Format (.targets), 54x Excluded (Unsupported Extension: '.targets'), 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.slnx`: 236x Unsupported Format (.slnx)
- `.resx`: 223x Unsupported Format (.resx)
- `.template`: 174x Unsupported Format (.template), 3x Excluded (Unsupported Extension: '.template')
- `.cpp`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 3188 commas in 635 LOC), 1x Excluded (Embedded Array/Matrix Payload: 30245 commas in 9163 LOC)
- `no_extension`: 78x Unsupported Format (.undeterminable), 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.proj`: 116x Unsupported Format (.proj), 9x Excluded (Unsupported Extension: '.proj'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 122x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 197 LOC), 1x Excluded (Static Asset Blob without Intent: 2078 LOC)
- `.xml`: 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Excluded (Binary Format Detected), 1x Excluded (Massive Static Asset Blob: 4283 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 20.0 | 7.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 38.2 | 45.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 20.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.7 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 89.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 19.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 73.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 557495 | 14867 | 12 | `src/coreclr/pal/prebuilt/inc/corprof.h` |
| cleanup | 13761 | 3931 | 0 | `src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/CommonTests.cs` |
| guards | 619363 | 28381 | 29 | `src/tests/JIT/Directed/nullabletypes/isinstvaluetype.cs` |
| danger | 141964 | 11655 | 5 | `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` |
| concurrency | 91473 | 4583 | 1 | `src/libraries/System.Net.Http/tests/FunctionalTests/HttpClientHandlerTest.Http2.cs` |
| connectivity | 563948 | 34414 | 26 | `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` |
| io | 19464 | 1990 | 0 | `src/native/external/zlib-ng/configure` |
| crypto | 5 | 5 | 0 | `.github/skills/ci-pipeline-monitor/scripts/fetch_helix_logs.py` |
| ipc | 1135 | 269 | 0 | `src/native/libs/System.Native/pal_networking.c` |
| time | 13638 | 1670 | 0 | `src/libraries/System.Runtime/tests/System.Runtime.Tests/System/DateTimeOffsetTests.cs` |
| serialization | 2458 | 319 | 0 | `src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Serialization/Value.ReadTests.cs` |
| regex | 927 | 278 | 0 | `src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/UpgradeToGeneratedRegexAnalyzerTests.cs` |
| events | 233931 | 5729 | 2 | `src/tests/JIT/Directed/cmov/Double_And_Op.cs` |
| tests | 304641 | 11088 | 12 | `src/libraries/Common/tests/Tests/System/StringTests.cs` |
| docs | 372266 | 8685 | 11 | `src/libraries/System.Private.CoreLib/src/System/Runtime/Intrinsics/Arm/AdvSimd.cs` |
| debt | 91023 | 8108 | 3 | `src/libraries/System.Runtime/ref/System.Runtime.cs` |
| mutation | 1895720 | 31816 | 92 | `src/tests/JIT/Directed/cmov/Double_And_Op.cs` |
| dead_code | 195715 | 26645 | 11 | `src/libraries/System.Numerics.Vectors/tests/GenericVectorTests.cs` |
| credential | 1359 | 262 | 0 | `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/RSA/RSAXml.cs` |
| threat | 72285 | 8714 | 2 | `src/coreclr/pal/prebuilt/inc/corprof.h` |
| ml_ai | 21423 | 2184 | 0 | `src/libraries/System.Runtime.Numerics/tests/ComplexTests.GenericMath.cs` |
| ui | 386 | 102 | 0 | `src/libraries/System.ObjectModel/tests/ObservableCollection/ObservableCollection_MethodsTest.cs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/native/external/zlib-ng/configure` (Hits: 779)
- `src/mono/mono/tests/verifier/make_tests.sh` (Hits: 692)
- `src/coreclr/scripts/superpmi.py` (Hits: 349)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Diagnostics.cs** (`src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/Diagnostics.cs`) — 5789 inbound connections
2. **System.Runtime.InteropServices.cs** (`src/libraries/System.Runtime.InteropServices/ref/System.Runtime.InteropServices.cs`) — 5029 inbound connections
3. **System.IO.cs** (`src/libraries/shims/System.IO/src/System.IO.cs`) — 3088 inbound connections
4. **System.Threading.cs** (`src/libraries/System.Threading/ref/System.Threading.cs`) — 2915 inbound connections
5. **System.Threading.Tasks.cs** (`src/libraries/shims/System.Threading.Tasks/src/System.Threading.Tasks.cs`) — 2426 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.h** (`src/coreclr/vm/common.h`) — 104 outbound dependencies
2. **mini-runtime.c** (`src/mono/mono/mini/mini-runtime.c`) — 74 outbound dependencies
3. **icall.c** (`src/mono/mono/metadata/icall.c`) — 68 outbound dependencies
4. **ceemain.cpp** (`src/coreclr/vm/ceemain.cpp`) — 65 outbound dependencies
5. **debugger-agent.c** (`src/mono/mono/component/debugger-agent.c`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Test` **(Many-Argument Workhorses)** (@ `src/tests/JIT/Regression/JitBlue/GitHub_17777/GitHub_17777.cs`) -> Impact: **2890.5** | LOC: 249
- `MarshalInfo::MarshalInfo` **(Many-Argument Workhorses)** (@ `src/coreclr/vm/mlinfo.cpp`) -> Impact: **1955.0** | LOC: 1351
  * *Intent:* //========================================================================== // Constructs MarshalInfo. //============================================...
- `emitter::emitInsSve_R_R_R_R` **(Many-Argument Workhorses)** (@ `src/coreclr/jit/emitarm64sve.cpp`) -> Impact: **1841.3** | LOC: 1346
  * *Intent:* /***************************************************************************** * * Add a SVE instruction referencing four registers. */
- `mini_emit_inst_for_method` **(Many-Argument Workhorses)** (@ `src/mono/mono/mini/intrinsics.c`) -> Impact: **1789.3** | LOC: 1494
- `emitter::emitInsSve_R_R_R_I` **(Many-Argument Workhorses)** (@ `src/coreclr/jit/emitarm64sve.cpp`) -> Impact: **1614.9** | LOC: 1370
  * *Intent:* /***************************************************************************** * * Add a SVE instruction referencing three registers and a constant. *...
- `emitter::emitInsSve_R_R_R` **(Many-Argument Workhorses)** (@ `src/coreclr/jit/emitarm64sve.cpp`) -> Impact: **1591.5** | LOC: 1470
  * *Intent:* /***************************************************************************** * * Add a SVE instruction referencing three registers. */
- `func` **(Compute Cores)** (@ `src/tests/JIT/jit64/regress/vsw/524070/test2.cs`) -> Impact: **1564.4** | LOC: 1278
- `emitter::emitDispIns` **(Many-Argument Workhorses)** (@ `src/coreclr/jit/emitxarch.cpp`) -> Impact: **1454.5** | LOC: 1370
  * *Intent:* // // Arguments: // id - The instruction // isNew - Whether the instruction is newly generated (before encoding). // doffs - If true, always display t...
- `mono_method_to_ir` **(Many-Argument Workhorses)** (@ `src/mono/mono/mini/method-to-ir.c`) -> Impact: **1430.1** | LOC: 1782
  * *Intent:* * @end_bblock: if not NULL, the ending basic block, used during inlining. * @return_var: if not NULL, the place where the return value is stored, used...
- `emitter::getInsSveExecutionCharacteristics` **(Many-Argument Workhorses)** (@ `src/coreclr/jit/emitarm64sve.cpp`) -> Impact: **1428.5** | LOC: 1446
  * *Intent:* #if defined(DEBUG) || defined(LATE_DISASM) //---------------------------------------------------------------------------------------- // getInsSveExec...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/tests/JIT/Directed/cmov` | 12 | 442351.74 | 93.36% | 0.0% |
| `src/coreclr/jit` | 288 | 305908.98 | 36.38% | 32.14% |
| `src/coreclr/vm` | 512 | 186371.42 | 22.72% | 36.57% |
| `src/mono/mono/mini` | 157 | 168552.1 | 48.16% | 48.41% |
| `src/mono/mono/metadata` | 162 | 78711.53 | 30.0% | 39.16% |
| `src/libraries/System.Private.CoreLib/src/System` | 276 | 73278.03 | 22.18% | 30.29% |
| `src/coreclr/gc` | 66 | 48925.5 | 37.88% | 16.91% |
| `src/mono/mono/tests` | 626 | 45842.46 | 14.99% | 0.0% |
| `src/libraries/System.Private.Xml/src/System/Xml/Schema` | 104 | 31119.64 | 27.11% | 29.5% |
| `src/libraries/System.Runtime.Intrinsics/ref` | 1 | 30298.0 | 4.86% | 100.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/mono/mono/metadata/metadata-update.c` -> **100.0%** Exposure
- `src/mono/mono/metadata/sysmath.c` -> **100.0%** Exposure
- `src/mono/mono/mini/interp-stubs.c` -> **100.0%** Exposure
- `src/mono/mono/mini/interp/interp-simd.c` -> **100.0%** Exposure
- `src/mono/mono/utils/mono-counters.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `eng/pipelines/common/templates/pipeline-with-resources.yml` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.sh` -> **100.0%** Exposure
- `eng/common/cibuild.sh` -> **100.0%** Exposure
- `eng/common/cross/tizen-fetch.sh` -> **100.0%** Exposure
- `eng/common/darc-init.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/libraries/System.Runtime/ref/System.Runtime.cs` -> **881** Orphaned Functions | **1962** Duplicates
- `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` -> **264** Orphaned Functions | **1929** Duplicates
- `src/libraries/System.Security.Cryptography/ref/System.Security.Cryptography.cs` -> **201** Orphaned Functions | **1033** Duplicates
- `src/libraries/System.Numerics.Vectors/tests/GenericVectorTests.cs` -> **1199** Orphaned Functions | **0** Duplicates
- `src/tests/JIT/opt/Vectorization/UnrollEqualsStartsWith_Tests.cs` -> **0** Orphaned Functions | **924** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/DSA/DSAKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/EC/ECKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/RSA/RSAKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/Common/tests/System/Security/Cryptography/X509Certificates/MLKemCertTests.cs` -> **100.0%** Exposure
- `src/libraries/System.Security.Cryptography/tests/ECPemExportTests.cs` -> **99.9997%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `89` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `123141` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/Thread_1.cs` (CSHARP) -> Cumulative Risk: **798.45**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.55)
- **Magnitude:** 201.02 | **LOC:** 273 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9986%)
- **Heaviest Functions:** `IThread.GetThreadLocalStaticBase` (I/O & Config Routines, Impact: 19.9), `IThread.GetThreadData` (Defensive Guards, Impact: 13.3), `IThread.GetWatsonBuckets` (I/O & Config Routines, Impact: 10.9)

### 2. `src/native/libs/Common/JavaScript/loader/assets.ts` (TYPESCRIPT) -> Cumulative Risk: **789.46**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.81)
- **Magnitude:** 942.16 | **LOC:** 710 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `prefetchUrl` (Many-Argument Workhorses, Impact: 46.3), `prefetchAllResources` (Compute Cores, Impact: 38.4), `fetchLazyAssembly` (Compute Cores, Impact: 31.3)

### 3. `src/libraries/System.Private.CoreLib/src/System/Threading/WaitHandle.Windows.cs` (CSHARP) -> Cumulative Risk: **768.92**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.75)
- **Magnitude:** 195.6 | **LOC:** 238 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9924%), State Flux (99.978%)
- **Heaviest Functions:** `WaitForMultipleObjectsIgnoringSyncContext` (Many-Argument Workhorses, Impact: 64.1), `SignalAndWaitCore` (Many-Argument Workhorses, Impact: 16.2), `ThrowWaitFailedException` (Compute Cores, Impact: 16.0)

### 4. `src/libraries/System.Private.CoreLib/src/System/Threading/Wasi/WasiEventLoop.cs` (CSHARP) -> Cumulative Risk: **766.4**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.55)
- **Magnitude:** 206.24 | **LOC:** 292 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9989%)
- **Heaviest Functions:** `CheckPollables` (Compute Cores, Impact: 28.5), `PollWasiEventLoopUntilResolved` (Defensive Guards, Impact: 6.8), `PollWasiEventLoopUntilResolvedVoid` (Defensive Guards, Impact: 6.7)

### 5. `src/mono/wasm/Wasm.Build.Tests/Templates/WasmTemplateTestsBase.cs` (CSHARP) -> Cumulative Risk: **765.34**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.40)
- **Magnitude:** 480.54 | **LOC:** 609 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.999%), State Flux (99.9243%), Documentation (98.0392%)
- **Heaviest Functions:** `BrowserRun` (Defensive Guards, Impact: 54.8), `BuildProjectCore` (Many-Argument Workhorses, Impact: 22.1), `EnsureWasmTemplatesInstalled` (I/O & Config Routines, Impact: 16.2)

### 6. `src/libraries/System.Net.Security/ref/System.Net.Security.cs` (CSHARP) -> Cumulative Risk: **764.26**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.11)
- **Magnitude:** 988.66 | **LOC:** 750 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9998%)
- **Heaviest Functions:** `SslStream` (Compute Cores, Impact: 7.4), `SslStream` (Compute Cores, Impact: 6.8), `SslStream` (Compute Cores, Impact: 6.0)

### 7. `src/mono/browser/runtime/loader/assets.ts` (TYPESCRIPT) -> Cumulative Risk: **761.76**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.89)
- **Magnitude:** 844.9 | **LOC:** 803 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `addAsset` (Many-Argument Workhorses, Impact: 67.3), `prepareAssets` (Compute Cores, Impact: 51.2), `start_asset_download_sources` (Compute Cores, Impact: 35.0)

### 8. `src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/marshaled-types.ts` (TYPESCRIPT) -> Cumulative Risk: **759.63**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.09)
- **Magnitude:** 156.1 | **LOC:** 265 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9997%), State Flux (88.7466%)
- **Heaviest Functions:** `_unsafe_create_view` (Compute Cores, Impact: 9.8), `copyTo` (Callbacks & Closures, Impact: 9.1), `set` (Callbacks & Closures, Impact: 9.0)

### 9. `src/libraries/System.Data.Odbc/src/Common/System/Data/ProviderBase/DbConnectionFactory.cs` (CSHARP) -> Cumulative Risk: **759.42**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -1.20)
- **Magnitude:** 122.8 | **LOC:** 179 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (98.7192%)
- **Heaviest Functions:** `TryGetConnection` (Many-Argument Workhorses, Impact: 69.4)

### 10. `src/coreclr/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncHelpers.CoreCLR.cs` (CSHARP) -> Cumulative Risk: **756.78**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.02)
- **Magnitude:** 700.32 | **LOC:** 1245 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9661%), State Flux (99.5304%), Documentation (99.0741%)
- **Heaviest Functions:** `HandleSuspended` (Compute Cores, Impact: 22.0), `InstrumentedDispatchContinuations` (Compute Cores, Impact: 20.7), `DispatchContinuations` (I/O & Config Routines, Impact: 19.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/tests/JIT/Directed/cmov/Int_Xor_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47930.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10751 instances
* *State Mutation (weighted view):* 36711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_And_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47870.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10721 instances
* *State Mutation (weighted view):* 36651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_Or_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47870.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10721 instances
* *State Mutation (weighted view):* 36651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_Xor_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47770.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10671 instances
* *State Mutation (weighted view):* 36551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_And_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47752.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10662 instances
* *State Mutation (weighted view):* 36533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_Or_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47752.02 | **LOC:** 22170 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10662 instances
* *State Mutation (weighted view):* 36533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_Xor_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47752.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10662 instances
* *State Mutation (weighted view):* 36533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_And_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47710.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10641 instances
* *State Mutation (weighted view):* 36491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_Or_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 47710.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 23.4)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10641 instances
* *State Mutation (weighted view):* 36491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 30298.0 | **LOC:** 13502 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (4.8598%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Create` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `Create` **(Generic / Templated Code)** (Impact: 8.1)
  * `Create` **(Generic / Templated Code)** (Impact: 5.8)
  * `Create` **(Generic / Templated Code)** (Impact: 5.8)
  * `Create` **(Generic / Templated Code)** (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 114`, `args: 10620`, `func_start: 10584`, `class_start: 109`
* *Risk/State:* `state_mutation: 34`, `dead_code: 55`, `duplicate_logic: 1929`, `unreferenced_by_name: 264`
* *Architecture:* `api: 10822`, `import: 1`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.017523
  * `Imports (Out-Degree: 0):` System.Diagnostics.CodeAnalysis
  * `Imported By (In-Degree: 722):` (Excluded from Brief to save tokens)

### `src/libraries/System.Runtime/ref/System.Runtime.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 25413.18 | **LOC:** 17405 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (30.0464%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `ExecuteAssembly` **(Defensive Guards)** (Impact: 9.1)
  * `FileStream` **(Annotated Framework Methods)** (Impact: 7.5)
  * `FileStream` **(Annotated Framework Methods)** (Impact: 6.9)
  * `FileStream` **(Annotated Framework Methods)** (Impact: 6.2)
  * `SerializationInfo` **(Defensive Guards)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 1438`, `args: 8156`, `func_start: 8599`, `class_start: 886`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 111`, `duplicate_logic: 1962`, `unreferenced_by_name: 881`
* *Architecture:* `io: 1`, `api: 9835`, `concurrency: 641`
* *Defense:* `safety: 247`, `sync_locks: 4`, `immutability_locks: 421`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.765
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003322
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 137):` (Excluded from Brief to save tokens)

### `src/coreclr/jit/emitarm64sve.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 22167.6 | **LOC:** 20043 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.6186%), Tech Debt (16.0752%)
**Top Internal Functions/Classes:**
  * `emitter::emitInsSve_R_R_R_R` **(Many-Argument Workhorses)** (Impact: 1841.3)
    * *Intent:* /***************************************************************************** * * Add a SVE instruc...
  * `emitter::emitInsSve_R_R_R_I` **(Many-Argument Workhorses)** (Impact: 1614.9)
    * *Intent:* /***************************************************************************** * * Add a SVE instruc...
  * `emitter::emitInsSve_R_R_R` **(Many-Argument Workhorses)** (Impact: 1591.5)
    * *Intent:* /***************************************************************************** * * Add a SVE instruc...
  * `emitter::getInsSveExecutionCharacteristics` **(Many-Argument Workhorses)** (Impact: 1428.5)
    * *Intent:* #if defined(DEBUG) || defined(LATE_DISASM) //-------------------------------------------------------...
  * `emitter::emitInsPairSanityCheck` **(Many-Argument Workhorses)** (Impact: 1063.5)
    * *Intent:* #endif // defined(DEBUG) || defined(LATE_DISASM) #ifdef DEBUG /*************************************...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2241 instances
* *State Mutation (weighted view):* 6927
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7647`, `structural_boundaries: 348`, `args: 62`, `func_start: 94`
* *Risk/State:* `state_mutation: 2445`, `planned_debt: 3`, `unreferenced_by_name: 92`
* *Architecture:* `import: 16`
* *Defense:* `safety: 2850`, `doc: 79`, `immutability_locks: 167`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` codegen.h, instr.h, instrsarm64sve.h, jitpch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/emitarm64.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 18318.14 | **LOC:** 18013 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (88.1236%), Tech Debt (41.3625%)
**Top Internal Functions/Classes:**
  * `emitter::emitDispInsHelp` **(Many-Argument Workhorses)** (Impact: 1375.8)
    * *Intent:* // // Arguments: // id - The instruction // isNew - Whether the instruction is newly generated (befo...
  * `emitter::emitIns_R_R_R` **(Many-Argument Workhorses)** (Impact: 1068.9)
    * *Intent:* /***************************************************************************** * * Add an instructio...
  * `emitter::getInsExecutionCharacteristics` **(Compute Cores)** (Impact: 1021.1)
    * *Intent:* // // Arguments: // id - The current instruction descriptor to be evaluated // // Return Value: // A...
  * `emitter::emitIns_R_R` **(Many-Argument Workhorses)** (Impact: 683.3)
    * *Intent:* /***************************************************************************** * * Add an instructio...
  * `emitter::emitOutputInstr` **(Many-Argument Workhorses)** (Impact: 682.2)
    * *Intent:* /***************************************************************************** * * Append the machin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2052 instances
* *State Mutation (weighted view):* 6387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5117`, `structural_boundaries: 406`, `args: 272`, `func_start: 198`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2283`, `dead_code: 6`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 194`
* *Architecture:* `import: 21`
* *Defense:* `safety: 1635`, `doc: 128`, `immutability_locks: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` codegen.h, emit.h, emitjmps.h, instr.h, instrs.h, instrsarm64sve.h, jitpch.h, register.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/emitxarch.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 16623.66 | **LOC:** 21365 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (88.5819%), Tech Debt (52.8657%)
**Top Internal Functions/Classes:**
  * `emitter::emitDispIns` **(Many-Argument Workhorses)** (Impact: 1454.5)
    * *Intent:* // // Arguments: // id - The instruction // isNew - Whether the instruction is newly generated (befo...
  * `emitter::emitOutputInstr` **(Many-Argument Workhorses)** (Impact: 948.8)
    * *Intent:* /***************************************************************************** * * Append the machin...
  * `emitter::emitOutputAM` **(Many-Argument Workhorses)** (Impact: 751.1)
    * *Intent:* #endif /***************************************************************************** * * Output an ...
  * `emitter::getInsExecutionCharacteristics` **(Compute Cores)** (Impact: 620.2)
    * *Intent:* // Returns the current instruction execution characteristics // // Arguments: // id - The current in...
  * `emitter::emitOutputSV` **(Many-Argument Workhorses)** (Impact: 390.6)
    * *Intent:* /***************************************************************************** * * Output an instruc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1677 instances
* *State Mutation (weighted view):* 5204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4814`, `structural_boundaries: 736`, `args: 462`, `func_start: 298`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 1850`, `dead_code: 15`, `fragile_debt: 3`, `unreferenced_by_name: 254`
* *Architecture:* `import: 20`
* *Defense:* `safety: 866`, `doc: 97`, `immutability_locks: 123`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` codegen.h, emit.h, emitjmps.h, instr.h, instrs.h, jitpch.h, register.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/jit64/opt/cg/cgstress/CgStress1.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 13613.8 | **LOC:** 28898 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.3244%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestEntryPoint` **(I/O & Config Routines)** (Impact: 1.5)
  * `foo0` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* #pragma warning disable xUnit1013
  * `foo1` **(Interface Declarations)** (Impact: 1.2)
  * `foo2` **(Interface Declarations)** (Impact: 1.2)
  * `foo3` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4102`, `args: 4098`, `func_start: 4098`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4098`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4100`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mono/mono/mini/aot-compiler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 12454.62 | **LOC:** 15922 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.312%), Tech Debt (24.2123%)
**Top Internal Functions/Classes:**
  * `mono_aot_parse_options` **(Compute Cores)** (Impact: 350.0)
  * `aot_assembly` **(Many-Argument Workhorses)** (Impact: 264.1)
  * `encode_method_ref` **(Many-Argument Workhorses)** (Impact: 233.7)
  * `compile_method` **(Many-Argument Workhorses)** (Impact: 231.8)
    * *Intent:* /* * compile_method: * * AOT compile a given method. * This function might be called by multiple thr...
  * `emit_and_reloc_code` **(Many-Argument Workhorses)** (Impact: 216.0)
    * *Intent:* /* * emit_and_reloc_code: * * Emit the native code in CODE, handling relocations along the way. If G...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 1720 instances
* *High Risk Execution (weighted view):* 19
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 5580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3033`, `structural_boundaries: 953`, `args: 620`, `func_start: 316`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 233`, `high_risk_execution: 20`, `state_mutation: 2140`, `dead_code: 17`, `planned_debt: 3`, `fragile_debt: 61`, `unreferenced_by_name: 14`
* *Architecture:* `io: 7`, `api: 56`, `import: 54`
* *Defense:* `safety: 22`, `doc: 7`, `immutability_locks: 188`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` aot-compiler.h, aot-runtime.h, config.h, ctype.h, dwarfwriter.h, errno.h, fcntl.h, image-writer.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mono/mono/mini/method-to-ir.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 12155.46 | **LOC:** 14009 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.2417%), Tech Debt (58.5466%)
**Top Internal Functions/Classes:**
  * `mono_method_to_ir` **(Many-Argument Workhorses)** (Impact: 1430.1)
    * *Intent:* * @end_bblock: if not NULL, the ending basic block, used during inlining. * @return_var: if not NULL...
  * `type_from_op` **(Many-Argument Workhorses)** (Impact: 330.4)
    * *Intent:* /* * Sets ins->type (the type on the eval stack) according to the * type of the opcode and the argum...
  * `mono_spill_global_vars` **(Many-Argument Workhorses)** (Impact: 292.5)
    * *Intent:* /** * mono_spill_global_vars: * * Generate spill code for variables which are not allocated to regis...
  * `handle_constrained_call` **(Many-Argument Workhorses)** (Impact: 167.2)
    * *Intent:* /* * handle_constrained_call: * * Handle constrained calls. Return a MonoInst* representing the call...
  * `inline_method` **(Many-Argument Workhorses)** (Impact: 157.4)
    * *Intent:* /* * inline_method: * * Return the cost of inlining CMETHOD, or zero if it should not be inlined. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1874 instances
* *State Mutation (weighted view):* 5908
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3585`, `structural_boundaries: 867`, `args: 309`, `func_start: 170`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 79`, `high_risk_execution: 1`, `state_mutation: 2160`, `dead_code: 15`, `planned_debt: 10`, `fragile_debt: 113`, `unreferenced_by_name: 21`
* *Architecture:* `api: 60`, `import: 57`
* *Defense:* `safety: 3`, `doc: 11`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` alloca.h, aot-compiler.h, config.h, ctype.h, glib.h, ir-emit.h, jit-icalls.h, llvmonly-runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mono/mono/mini/interp/transform.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10453.96 | **LOC:** 10168 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (15.9732%)
**Top Internal Functions/Classes:**
  * `interp_handle_intrinsics` **(Many-Argument Workhorses)** (Impact: 1427.7)
    * *Intent:* /* Return TRUE if call transformation is finished */
  * `generate_code` **(Many-Argument Workhorses)** (Impact: 1228.1)
  * `interp_transform_call` **(Many-Argument Workhorses)** (Impact: 680.0)
    * *Intent:* /* Return FALSE if error, including inline failure */
  * `emit_compacted_instruction` **(Many-Argument Workhorses)** (Impact: 191.9)
  * `generate` **(Many-Argument Workhorses)** (Impact: 136.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1320 instances
* *State Mutation (weighted view):* 4173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2867`, `structural_boundaries: 856`, `args: 199`, `func_start: 159`
* *Risk/State:* `safety_bypasses: 121`, `state_mutation: 1533`, `dead_code: 7`, `planned_debt: 9`, `fragile_debt: 23`, `unreferenced_by_name: 9`
* *Architecture:* `api: 31`, `import: 28`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` config.h, interp-internals.h, interp-pgo.h, interp.h, jiterpreter.h, mintops.h, abi-details.h, appdomain.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mono/mono/mini/mini-llvm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10231.16 | **LOC:** 15450 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.4554%), Tech Debt (21.5163%)
**Top Internal Functions/Classes:**
  * `process_bb` **(Many-Argument Workhorses)** (Impact: 1127.6)
  * `process_call` **(Many-Argument Workhorses)** (Impact: 351.0)
  * `emit_method_inner` **(Compute Cores)** (Impact: 304.6)
  * `sig_to_llvm_sig_full` **(Many-Argument Workhorses)** (Impact: 221.1)
    * *Intent:* /* * sig_to_llvm_sig_full: * * Return the LLVM signature corresponding to the mono signature SIG usi...
  * `emit_entry_bb` **(Many-Argument Workhorses)** (Impact: 213.5)
    * *Intent:* #endif /* * emit_entry_bb: * * Emit code to load/convert arguments. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1630 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 5264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3901`, `structural_boundaries: 1391`, `args: 879`, `func_start: 201`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 2004`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 55`, `unreferenced_by_name: 16`
* *Architecture:* `api: 29`, `import: 30`
* *Defense:* `safety: 15`, `doc: 1`, `immutability_locks: 109`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` aot-compiler.h, config.h, Analysis.h, BitWriter.h, Core.h, IPO.h, InstCombine.h, Scalar.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/valuenum.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10101.34 | **LOC:** 15890 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (71.7787%), Tech Debt (61.3671%)
**Top Internal Functions/Classes:**
  * `ValueNumStore::EvalHWIntrinsicFunBinary` **(Many-Argument Workhorses)** (Impact: 588.6)
  * `ValueNumStore::EvalUsingMathIdentity` **(Many-Argument Workhorses)** (Impact: 581.0)
    * *Intent:* //---------------------------------------------------------------------------------------- // EvalUs...
  * `ValueNumStore::EvalMathFuncUnary` **(Many-Argument Workhorses)** (Impact: 462.5)
    * *Intent:* #endif // FEATURE_HW_INTRINSICS
  * `Compiler::fgValueNumberTree` **(Compute Cores)** (Impact: 259.5)
  * `Compiler::fgValueNumberJitHelperMethodVNFunc` **(Compute Cores)** (Impact: 254.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 740 instances
* *State Mutation (weighted view):* 2334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3408`, `structural_boundaries: 967`, `args: 1047`, `func_start: 280`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 854`, `dead_code: 20`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 221`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 497`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` gtlist.h, jitpch.h, ssaconfig.h, valuenum.h, valuenumfuncs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mono/mono/component/debugger-agent.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10058.3 | **LOC:** 11340 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.3881%), Tech Debt (38.5138%)
**Top Internal Functions/Classes:**
  * `type_commands_internal` **(Many-Argument Workhorses)** (Impact: 434.8)
  * `method_commands_internal` **(Many-Argument Workhorses)** (Impact: 383.3)
  * `decode_value_internal` **(Many-Argument Workhorses)** (Impact: 313.1)
  * `buffer_add_value_full` **(Many-Argument Workhorses)** (Impact: 303.8)
    * *Intent:* /* * buffer_add_value_full: * * Add the encoding of the value at ADDR described by T to the buffer. ...
  * `mono_do_invoke_method` **(Many-Argument Workhorses)** (Impact: 274.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 4 instances
* *Amplified Cascading Flux:* 1237 instances
* *High Risk Execution (weighted view):* 18
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 3896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2226`, `structural_boundaries: 1068`, `args: 422`, `func_start: 234`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 297`, `high_risk_execution: 19`, `state_mutation: 1422`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 71`, `unreferenced_by_name: 14`
* *Architecture:* `io: 13`, `api: 38`, `import: 64`
* *Defense:* `safety: 3`, `doc: 11`, `immutability_locks: 40`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 47):` config.h, errno.h, fcntl.h, glib.h, in.h, tcp.h, debugger-agent.h, debugger-engine.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libraries/Microsoft.XmlSerializer.Generator/tests/Expected.SerializableAssembly.XmlSerializers.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 9419.6 | **LOC:** 19291 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (29.0612%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Write1_Object` **(Many-Argument Workhorses)** (Impact: 477.5)
  * `CanSerialize` **(Compute Cores)** (Impact: 189.0)
  * `GetSerializer` **(Compute Cores)** (Impact: 189.0)
  * `Write55_TypeWithArraylikeMembers` **(Many-Argument Workhorses)** (Impact: 66.4)
  * `Write89_XmlSerializerAttributes` **(Many-Argument Workhorses)** (Impact: 56.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 590 instances
* *State Mutation (weighted view):* 2849
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5261`, `structural_boundaries: 1720`, `args: 1137`, `func_start: 770`, `class_start: 131`
* *Risk/State:* `state_mutation: 1669`, `duplicate_logic: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 522`
* *Defense:* `safety: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/importercalls.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9180.6 | **LOC:** 12169 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (90.1976%), Tech Debt (22.2828%)
**Top Internal Functions/Classes:**
  * `Compiler::impIntrinsic` **(Many-Argument Workhorses)** (Impact: 1352.2)
    * *Intent:* // sequence. If it is a call, then the intrinsic processing here is responsible // for handling all ...
  * `Compiler::impImportCall` **(Many-Argument Workhorses)** (Impact: 898.0)
    * *Intent:* // callInfo - EE supplied info for the call // rawILOffset - IL offset of the opcode // // Returns: ...
  * `Compiler::lookupNamedIntrinsic` **(Compute Cores)** (Impact: 686.6)
    * *Intent:* //------------------------------------------------------------------------ // lookupNamedIntrinsic: ...
  * `Compiler::impPrimitiveNamedIntrinsic` **(Many-Argument Workhorses)** (Impact: 408.8)
    * *Intent:* //------------------------------------------------------------------------ // impPrimitiveNamedIntri...
  * `Compiler::impDevirtualizeCall` **(Many-Argument Workhorses)** (Impact: 380.9)
    * *Intent:* // // If devirtualization succeeds and the call's this object is a // (boxed) value type, the jit wi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 853 instances
* *State Mutation (weighted view):* 2747
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2637`, `structural_boundaries: 369`, `args: 486`, `func_start: 56`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1041`, `dead_code: 32`, `planned_debt: 40`, `unreferenced_by_name: 50`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 345`, `doc: 3`, `sync_locks: 1`, `immutability_locks: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jitpch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/vm/jitinterface.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 8661.04 | **LOC:** 15735 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (67.6089%), Tech Debt (80.6108%)
**Top Internal Functions/Classes:**
  * `LoadDynamicInfoEntry` **(Many-Argument Workhorses)** (Impact: 377.6)
  * `CEEInfo::getCallInfo` **(Many-Argument Workhorses)** (Impact: 372.9)
    * *Intent:* /***********************************************************************/ // return the address of a...
  * `CEEInfo::ComputeRuntimeLookupForSharedGenericToken` **(Many-Argument Workhorses)** (Impact: 217.7)
  * `CEEInfo::resolveToken` **(Compute Cores)** (Impact: 135.8)
    * *Intent:* /*********************************************************************/
  * `getILIntrinsicImplementationForUnsafe` **(Many-Argument Workhorses)** (Impact: 134.2)
    * *Intent:* *********************************************************************/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 939 instances
* *State Mutation (weighted view):* 3157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2053`, `structural_boundaries: 661`, `args: 841`, `func_start: 347`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 1279`, `dead_code: 36`, `planned_debt: 51`, `unreferenced_by_name: 273`
* *Architecture:* `api: 3`, `import: 46`
* *Defense:* `safety: 18`, `doc: 109`, `test: 1`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` array.h, callconvbuilder.hpp, class.h, codeman.h, comdelegate.h, common.h, corjit.h, corprof.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/morph.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8385.62 | **LOC:** 15984 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 18.8%
- **Risk Profile:** Cognitive Load (60.6514%), Tech Debt (44.1822%)
**Top Internal Functions/Classes:**
  * `Compiler::fgMorphSmpOp` **(Many-Argument Workhorses)** (Impact: 826.6)
    * *Intent:* //------------------------------------------------------------------------ // fgMorphSmpOp: morph a ...
  * `Compiler::fgOptimizeHWIntrinsic` **(Compute Cores)** (Impact: 341.7)
    * *Intent:* // fgOptimizeHWIntrinsic: optimize a HW intrinsic node // // Arguments: // node - HWIntrinsic node t...
  * `Compiler::fgMorphPotentialTailCall` **(Compute Cores)** (Impact: 198.6)
    * *Intent:* // call - The call to morph. // // Return Value: // Returns a node to use if the call was morphed in...
  * `CallArgs::ArgsComplete` **(Many-Argument Workhorses)** (Impact: 171.8)
    * *Intent:* #endif //------------------------------------------------------------------------ // ArgsComplete: M...
  * `Compiler::fgMorphSmpOpOptional` **(Many-Argument Workhorses)** (Impact: 128.5)
    * *Intent:* //------------------------------------------------------------- // fgMorphSmpOpOptional: optional po...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 914 instances
* *State Mutation (weighted view):* 2880
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2693`, `structural_boundaries: 522`, `args: 770`, `func_start: 140`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1052`, `dead_code: 38`, `planned_debt: 34`, `fragile_debt: 2`, `duplicate_logic: 3`, `unreferenced_by_name: 120`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 250`, `doc: 8`, `test: 5`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` allocacheck.h, jitpch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/SOSDacImpl.cs` -> Churn: **89.82%** | Cog Load: 39.0946% | Debt: 68.5751%
- `src/coreclr/jit/codegenwasm.cpp` -> Churn: **87.5%** | Cog Load: 77.0176% | Debt: 92.2576%
- `src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/Dbi/DacDbiImpl.cs` -> Churn: **83.6%** | Cog Load: 36.8789% | Debt: 99.827%
- `src/coreclr/jit/lower.cpp` -> Churn: **80.66%** | Cog Load: 40.4494% | Debt: 57.1309%
- `src/coreclr/jit/morph.cpp` -> Churn: **79.06%** | Cog Load: 60.6514% | Debt: 44.1822%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/coreclr/jit/emitarm64sve.cpp` -> **Yat Long Poon** (100.0% isolated ownership) | Magnitude: 22167.6
- `src/mono/mono/component/debugger-agent.c` -> **Thays Grazia** (100.0% isolated ownership) | Magnitude: 10058.3
- `src/coreclr/gc/plan_phase.cpp` -> **Jan Vorlicek** (100.0% isolated ownership) | Magnitude: 7916.62
- `src/coreclr/jit/emitarm.cpp` -> **Michal Strehovský** (100.0% isolated ownership) | Magnitude: 7815.34
- `src/mono/mono/mini/simd-intrinsics.c` -> **Pavel Savara** (100.0% isolated ownership) | Magnitude: 7782.28

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/coreclr/inc/utilcode.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.6759%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/libraries/System.Runtime.InteropServices/ref/System.Runtime.InteropServices.cs` -> **Severity: 8.111** (Embedded: 0.1592 * Error Risk: 50.9475%)
- `src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/Diagnostics.cs` -> **Severity: 4.448** (Embedded: 0.1404 * Error Risk: 31.6866%)
- `src/libraries/System.Diagnostics.Process/tests/Interop.cs` -> **Severity: 4.352** (Embedded: 0.0725 * Error Risk: 60.0647%)
- `src/libraries/System.Runtime.InteropServices/tests/Common/Verifiers/CSharpAnalyzerVerifier.cs` -> **Severity: 4.08** (Embedded: 0.0718 * Error Risk: 56.8145%)
- `src/libraries/System.Runtime.Serialization.Xml/tests/SerializationTestTypes/Collections.cs` -> **Severity: 3.255** (Embedded: 0.0378 * Error Risk: 86.0512%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/libraries/System.Runtime.InteropServices/ref/System.Runtime.InteropServices.cs` -> **Severity: 5046.9** (Blast Radius: 50.469 * Doc Risk: 100.0%)
- `src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/Diagnostics.cs` -> **Severity: 3899.0** (Blast Radius: 38.99 * Doc Risk: 100.0%)
- `src/libraries/System.Threading/ref/System.Threading.cs` -> **Severity: 1757.9** (Blast Radius: 17.579 * Doc Risk: 100.0%)
- `src/libraries/System.Runtime.Serialization.Xml/tests/SerializationTestTypes/Collections.cs` -> **Severity: 881.3** (Blast Radius: 8.813 * Doc Risk: 100.0%)
- `src/libraries/System.Diagnostics.Process/tests/Interop.cs` -> **Severity: 723.6** (Blast Radius: 7.236 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
