# ARCHITECTURAL_BRIEF: runtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dotnet/runtime.git` |
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
- **Scope:** 40931 analyzed artifact(s), 8284258 LOC.
- **Load-bearing artifact:** `src/libraries/Fuzzing/DotnetFuzzing/Assert.cs` -- 6195 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/coreclr/vm/common.h` -- pulls in 104 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/tests/JIT/Regression/JitBlue/DevDiv_255294/DevDiv_255294.cs` at magnitude 190922.02 (structural weight, not risk).
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
| Total Artifacts | 57632 |
| Analyzed Artifacts (Scanned) | 40931 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16701 |
| Total LOC | 8284258 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.0% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.596 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.227 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1055 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 31666 | 6333638 | 77.4% |
| CPP | 3162 | 1256159 | 7.7% |
| C | 1893 | 522327 | 4.6% |
| XML | 1403 | 1994 | 3.4% |
| PLAINTEXT | 847 | 5 | 2.1% |
| MARKDOWN | 416 | 0 | 1.0% |
| ASSEMBLY | 299 | 45847 | 0.7% |
| YAML | 298 | 19028 | 0.7% |
| SHELL | 195 | 19631 | 0.5% |
| TYPESCRIPT | 182 | 28575 | 0.4% |
| JSON | 173 | 6369 | 0.4% |
| POWERSHELL | 67 | 5417 | 0.2% |
| PYTHON | 59 | 14936 | 0.1% |
| MAKEFILE | 59 | 4639 | 0.1% |
| BATCH | 52 | 2475 | 0.1% |
| JAVASCRIPT | 49 | 3539 | 0.1% |
| HTML | 24 | 598 | 0.1% |
| OBJECTIVE-C | 23 | 3013 | 0.1% |
| M4 | 19 | 876 | 0.0% |
| FSHARP | 13 | 1870 | 0.0% |
| DOCKERFILE | 9 | 220 | 0.0% |
| SWIFT | 9 | 9582 | 0.0% |
| PERL | 5 | 894 | 0.0% |
| JAVA | 5 | 345 | 0.0% |
| CSV | 2 | 496 | 0.0% |
| YACC | 1 | 1782 | 0.0% |
| CSS | 1 | 3 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 7 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 37242 |
| utf-8 | bom | 3652 |
| utf-16-le | bom | 23 |
| cp1252 | cp1252-fallback | 6 |
| unknown | unknown | 5 |
| latin-1 | latin-1-fallback | 1 |
| utf-16-be | utf-16-heuristic | 1 |
| utf-16-le | utf-16-heuristic | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 18%, State Mutators Files 15%, Encapsulated Accessors Files 14%, Data / Markup / Trivial 11%, Large Core Modules 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 39659 | 96.9% |
| Unknown | 5 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1258 | 3.1% |
| Static: Minified & Vendor Opaque Mass | 9 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16701*

**Composition by Extension & Reason:**
- `.csproj`: 5699x Unsupported Format (.csproj), 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.csproj')
- `.il`: 3384x Unsupported Format (.il), 219x Excluded: Neighborhood Micro-Mass Limit Exceeded, 169x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ilproj`: 2748x Unsupported Format (.ilproj), 120x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 421x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.props`: 314x Unsupported Format (.props), 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 21x Excluded (Unsupported Extension: '.props')
- `.cs`: 325x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3044 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3417 LOC)
- `.xml`: 260x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Massive Static Asset Blob: 4283 LOC)
- `.targets`: 154x Unsupported Format (.targets), 58x Excluded (Unsupported Extension: '.targets'), 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.slnx`: 236x Unsupported Format (.slnx)
- `.h`: 213x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1569 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1529 LOC)
- `.resx`: 223x Unsupported Format (.resx)
- `.template`: 174x Unsupported Format (.template), 3x Excluded (Unsupported Extension: '.template')
- `.cpp`: 165x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 9362 LOC), 1x Excluded (Embedded Array/Matrix Payload: 2342 commas in 705 LOC)
- `no_extension`: 76x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 72x Unsupported Format (.undeterminable), 2x Excluded (Unsupported Extension: '.globalconfig')
- `.proj`: 104x Unsupported Format (.proj), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Excluded (Unsupported Extension: '.proj')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 19.0 | 6.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 33.7 | 47.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.7 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 19.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 74.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 84762 | 10471 | 4 | `src/libraries/System.Private.CoreLib/src/System/Reflection/Emit/OpCodes.cs` |
| cleanup | 13668 | 3939 | 0 | `src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/CommonTests.cs` |
| guards | 605735 | 28254 | 29 | `src/tests/JIT/Directed/nullabletypes/isinstvaluetype.cs` |
| danger | 148165 | 11601 | 5 | `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` |
| concurrency | 93472 | 4597 | 1 | `src/libraries/System.Net.Http/tests/FunctionalTests/HttpClientHandlerTest.Http2.cs` |
| connectivity | 661491 | 34286 | 26 | `src/tests/JIT/Regression/CLR-x86-JIT/V2.0-Beta2/b399444/Repro.cs` |
| io | 19002 | 1994 | 0 | `src/mono/mono/tests/verifier/make_tests.sh` |
| crypto | 6 | 6 | 0 | `.github/skills/ci-pipeline-monitor/scripts/fetch_helix_logs.py` |
| ipc | 1175 | 274 | 0 | `src/native/libs/System.Native/pal_networking.c` |
| time | 13787 | 1686 | 0 | `src/libraries/System.Runtime/tests/System.Runtime.Tests/System/DateTimeOffsetTests.cs` |
| serialization | 2683 | 314 | 0 | `src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Serialization/Value.ReadTests.cs` |
| regex | 892 | 283 | 0 | `src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/UpgradeToGeneratedRegexAnalyzerTests.cs` |
| events | 239978 | 5787 | 2 | `src/tests/JIT/Directed/cmov/Double_And_Op.cs` |
| tests | 325807 | 11218 | 12 | `src/libraries/System.Runtime/tests/System.Runtime.Tests/System/IntPtrTests.GenericMath.cs` |
| docs | 366761 | 8489 | 10 | `src/libraries/System.Private.CoreLib/src/System/Runtime/Intrinsics/Arm/AdvSimd.cs` |
| debt | 118524 | 8085 | 3 | `src/tests/JIT/jit64/opt/cse/hugeexpr1.cs` |
| mutation | 2334281 | 31688 | 92 | `src/tests/JIT/Regression/CLR-x86-JIT/V2.0-Beta2/b399444/Repro.cs` |
| dead_code | 195037 | 25972 | 11 | `src/libraries/System.Numerics.Vectors/tests/GenericVectorTests.cs` |
| credential | 2493 | 276 | 0 | `src/libraries/System.IO.Hashing/tests/XxHash128Tests.cs` |
| threat | 1174 | 195 | 0 | `src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/RegexPcreTests.cs` |
| ml_ai | 25016 | 2194 | 0 | `src/libraries/System.Runtime.Numerics/tests/ComplexTests.GenericMath.cs` |
| ui | 389 | 104 | 0 | `src/libraries/System.ObjectModel/tests/ObservableCollection/ObservableCollection_MethodsTest.cs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/mono/mono/tests/verifier/make_tests.sh` (Hits: 692)
- `src/coreclr/scripts/superpmi.py` (Hits: 349)
- `src/libraries/Common/tests/System/IO/Compression/FileData.cs` (Hits: 236)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Assert.cs** (`src/libraries/Fuzzing/DotnetFuzzing/Assert.cs`) — 6195 inbound connections
2. **Diagnostics.cs** (`src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/Diagnostics.cs`) — 5779 inbound connections
3. **System.Runtime.InteropServices.cs** (`src/libraries/System.Runtime.InteropServices/ref/System.Runtime.InteropServices.cs`) — 5211 inbound connections
4. **System.Runtime.cs** (`src/libraries/System.Runtime/ref/System.Runtime.cs`) — 4889 inbound connections
5. **Debug.cs** (`src/coreclr/nativeaot/Runtime.Base/src/System/Diagnostics/Debug.cs`) — 4303 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.h** (`src/coreclr/vm/common.h`) — 104 outbound dependencies
2. **mini-runtime.c** (`src/mono/mono/mini/mini-runtime.c`) — 74 outbound dependencies
3. **icall.c** (`src/mono/mono/metadata/icall.c`) — 68 outbound dependencies
4. **ceemain.cpp** (`src/coreclr/vm/ceemain.cpp`) — 65 outbound dependencies
5. **debugger-agent.c** (`src/mono/mono/component/debugger-agent.c`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `func` **(Many-Argument Workhorses)** (@ `src/tests/JIT/jit64/regress/vsw/524070/test2.cs`) -> Impact: **12877.0** | LOC: 10505
- `mono_method_to_ir` **(Many-Argument Workhorses)** (@ `src/mono/mono/mini/method-to-ir.c`) -> Impact: **5106.6** | LOC: 6072
  * *Intent:* * @end_bblock: if not NULL, the ending basic block, used during inlining. * @return_var: if not NULL, the place where the return value is stored, used...
- `process_bb` **(Many-Argument Workhorses)** (@ `src/mono/mono/mini/mini-llvm.c`) -> Impact: **4300.1** | LOC: 6848
- `TestEntryPoint` **(Compute Cores)** (@ `src/tests/JIT/Regression/CLR-x86-JIT/V1-M12-Beta2/b71005/b71005.cs`) -> Impact: **3461.1** | LOC: 1162
- `TestEntryPoint` **(Compute Cores)** (@ `src/tests/JIT/opt/virtualstubdispatch/bigvtbl/bigvtbl.cs`) -> Impact: **3177.9** | LOC: 3039
- `Compiler::impSpecialIntrinsic` **(Many-Argument Workhorses)** (@ `src/coreclr/jit/hwintrinsicxarch.cpp`) -> Impact: **3124.8** | LOC: 4359
  * *Intent:* // mustExpand -- true if the intrinsic must return a GenTree*; otherwise, false // // Return Value: // the expanded intrinsic. // // Assumptions: // F...
- `Test` **(Many-Argument Workhorses)** (@ `src/tests/JIT/Regression/JitBlue/GitHub_17777/GitHub_17777.cs`) -> Impact: **2890.5** | LOC: 249
- `HugeMethod` **(Compute Cores)** (@ `src/tests/JIT/Regression/JitBlue/DevDiv_255294/DevDiv_255294.cs`) -> Impact: **2625.2** | LOC: 2503
- `generate_code` **(Many-Argument Workhorses)** (@ `src/mono/mono/mini/interp/transform.c`) -> Impact: **2441.8** | LOC: 3619
- `InterpExecMethod` **(Many-Argument Workhorses)** (@ `src/coreclr/vm/interpexec.cpp`) -> Impact: **2196.7** | LOC: 3372

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/tests/JIT/Directed/cmov` | 16 | 731582.1 | 94.24% | 0.0% |
| `src/coreclr/jit` | 291 | 333728.54 | 31.46% | 31.16% |
| `src/tests/JIT/Regression/JitBlue/DevDiv_255294` | 1 | 190922.02 | 96.89% | 0.0% |
| `src/coreclr/vm` | 513 | 184540.04 | 20.82% | 34.76% |
| `src/mono/mono/mini` | 158 | 175923.56 | 45.85% | 47.15% |
| `src/tests/JIT/jit64/opt/cse` | 34 | 110452.88 | 75.34% | 0.0% |
| `src/tests/JIT/Regression/VS-ia64-JIT/V1.2-M01/b10827` | 1 | 95064.16 | 97.01% | 0.0% |
| `src/mono/mono/metadata` | 162 | 78827.16 | 25.46% | 37.26% |
| `src/libraries/System.Private.CoreLib/src/System` | 276 | 72927.73 | 22.08% | 28.39% |
| `src/tests/JIT/Regression/CLR-x86-JIT/V2.0-Beta2/b399444` | 1 | 66864.72 | 5.22% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/mono/mono/metadata/metadata-update.c` -> **100.0%** Exposure
- `src/mono/mono/metadata/sysmath.c` -> **100.0%** Exposure
- `src/mono/mono/mini/interp-stubs.c` -> **100.0%** Exposure
- `src/mono/mono/mini/interp/interp-simd.c` -> **100.0%** Exposure
- `src/mono/mono/utils/mono-counters.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `eng/pipelines/common/templates/pipeline-with-resources.yml` -> **100.0%** Exposure
- `eng/build.sh` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.sh` -> **100.0%** Exposure
- `eng/common/build.sh` -> **100.0%** Exposure
- `eng/common/cibuild.sh` -> **100.0%** Exposure
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
- `src/libraries/System.Security.Cryptography/tests/AsymmetricAlgorithmTests.cs` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `162` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `122687` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/tests/JIT/Regression/JitBlue/DevDiv_255294/DevDiv_255294.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.846)
- **Top Global Matches:** file_cluster_3: 10.846, file_cluster_8: 22.347, file_cluster_6: 34.603
- **Magnitude:** 190922.02 | **LOC:** 62379 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.011; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (96.9%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HugeMethod` **(Compute Cores)** (Impact: 2625.2)
  * `TestEntryPoint` **(Annotated & Test Methods)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62348 instances
* *State Mutation (weighted view):* 187045
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62348`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 62349`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` System, System.Runtime.CompilerServices, TestLibrary, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Regression/VS-ia64-JIT/V1.2-M01/b10827/MT_DEATH.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 9.732)
- **Top Global Matches:** file_cluster_1: 9.732, file_cluster_3: 48.009, file_cluster_8: 69.645
- **Magnitude:** 95064.16 | **LOC:** 20866 | **CtrlFlow:** 139.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (97.0%), Concurrency Surface (formerly Concurrency) (12.7%), Connectivity (formerly Api Exposure) (2.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 63.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 21205 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 65459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27685`, `structural_boundaries: 473`, `args: 466`, `func_start: 466`, `class_start: 1`
* *Risk/State:* `state_mutation: 23049`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` System, System.Threading, TestLibrary, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Bool_And_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 9.743)
- **Top Global Matches:** file_cluster_1: 9.743, file_cluster_3: 48.009, file_cluster_8: 69.645
- **Magnitude:** 94055.26 | **LOC:** 20789 | **CtrlFlow:** 139.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (96.9%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 63.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20741 instances
* *State Mutation (weighted view):* 64524
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23042`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Bool_Or_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 9.743)
- **Top Global Matches:** file_cluster_1: 9.743, file_cluster_3: 48.009, file_cluster_8: 69.645
- **Magnitude:** 94055.26 | **LOC:** 20788 | **CtrlFlow:** 139.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (96.9%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 63.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20741 instances
* *State Mutation (weighted view):* 64524
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23042`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Bool_Xor_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 9.743)
- **Top Global Matches:** file_cluster_1: 9.743, file_cluster_3: 48.009, file_cluster_8: 69.645
- **Magnitude:** 94055.26 | **LOC:** 20788 | **CtrlFlow:** 139.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (96.9%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_1` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_2` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_3` **(Compute Cores)** (Impact: 63.2)
  * `Sub_Funclet_4` **(Compute Cores)** (Impact: 63.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20741 instances
* *State Mutation (weighted view):* 64524
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23042`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Regression/CLR-x86-JIT/V2.0-Beta2/b399444/Repro.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.907)
- **Top Global Matches:** file_cluster_2: 7.907, file_cluster_16: 8.547, file_cluster_13: 8.794
- **Magnitude:** 66864.72 | **LOC:** 65618 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.02; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Complexity Load (formerly Cognitive Load) (5.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestEntryPoint` **(Annotated & Test Methods)** (Impact: 2.6)
  * `TestManyFieldsPlusTwo` **(Defensive Guards)** (Impact: 2.0)
  * `TestManyFields` **(Defensive Guards)** (Impact: 1.6)
  * `TestLdManyFields` **(Encapsulated Accessors)** (Impact: 1.2)
  * `TestLdManyFieldsPlusTwo` **(Encapsulated Accessors)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 65544`, `import: 4`
* *Defense:* `safety: 7`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` System, System.Reflection, System.Runtime.CompilerServices, Xunit
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/tests/JIT/jit64/opt/cse/hugeexpr1.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.081)
- **Top Global Matches:** file_cluster_9: 9.081, file_cluster_16: 9.388, file_cluster_2: 9.517
- **Magnitude:** 50572.38 | **LOC:** 89159 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (72.2%), Connectivity (formerly Api Exposure) (1.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestEntryPoint` **(I/O & Config Routines)** (Impact: 9.0)
  * `return_int` **(Stateful Encapsulated Methods)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12513 instances
* *State Mutation (weighted view):* 49023
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12439`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 23997`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 9`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` System, TestLibrary, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_Xor_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47930.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10751 instances
* *State Mutation (weighted view):* 36711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_And_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47870.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10721 instances
* *State Mutation (weighted view):* 36651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_Or_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47870.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10721 instances
* *State Mutation (weighted view):* 36651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_Xor_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47770.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10671 instances
* *State Mutation (weighted view):* 36551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_And_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47752.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10662 instances
* *State Mutation (weighted view):* 36533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_Or_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47752.02 | **LOC:** 22170 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10662 instances
* *State Mutation (weighted view):* 36533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_Xor_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47752.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10662 instances
* *State Mutation (weighted view):* 36533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_And_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47710.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10641 instances
* *State Mutation (weighted view):* 36491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_Or_Op.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_1: 8.644, file_cluster_3: 47.812, file_cluster_8: 69.494
- **Magnitude:** 47710.02 | **LOC:** 22171 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (93.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_1` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_2` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_3` **(I/O & Config Routines)** (Impact: 23.4)
  * `Sub_Funclet_4` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10641 instances
* *State Mutation (weighted view):* 36491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 465`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15209`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/jit64/opt/cse/HugeArray1.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.998)
- **Top Global Matches:** file_cluster_9: 8.998, file_cluster_16: 9.4, file_cluster_2: 9.621
- **Magnitude:** 44498.22 | **LOC:** 85517 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.2%), Complexity Load (formerly Cognitive Load) (72.3%), Connectivity (formerly Api Exposure) (1.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestEntryPoint` **(I/O & Config Routines)** (Impact: 19.5)
  * `return_int` **(Stateful Encapsulated Methods)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10585 instances
* *State Mutation (weighted view):* 43183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10527`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 22013`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 11`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` System, TestLibrary, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.681)
- **Top Global Matches:** file_cluster_0: 8.681, file_cluster_13: 10.608, file_cluster_2: 12.044
- **Magnitude:** 30298.0 | **LOC:** 13502 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **742** in-repo importer(s); it depends on **1**; blast radius 4.285; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (50.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.9%), Connectivity (formerly Api Exposure) (19.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Create` **(Generic / Templated Code)** (Impact: 8.2)
  * `Create` **(Generic / Templated Code)** (Impact: 8.1)
  * `Create` **(Generic / Templated Code)** (Impact: 5.8)
  * `Create` **(Generic / Templated Code)** (Impact: 5.8)
  * `Create` **(Generic / Templated Code)** (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 114`, `args: 10620`, `func_start: 10584`, `class_start: 109`
* *Risk/State:* `state_mutation: 34`, `dead_code: 55`, `duplicate_logic: 1929`, `unreferenced_by_name: 264`
* *Architecture:* `api: 10822`, `import: 1`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.285
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` System.Diagnostics.CodeAnalysis
  * `Imported By (In-Degree: 742):` (Excluded from Brief to save tokens)

### `src/tests/JIT/opt/virtualstubdispatch/bigvtbl/bigvtbl.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 61.477)
- **Top Global Matches:** file_cluster_4: 61.477, file_cluster_16: 61.912, file_cluster_12: 61.994
- **Magnitude:** 28676.46 | **LOC:** 15056 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **2**; blast radius 0.021; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (19.5%), Complexity Load (formerly Cognitive Load) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestEntryPoint` **(Compute Cores)** (Impact: 3177.9)
  * `f1` **(Interface Declarations)** (Impact: 1.1)
  * `f2` **(Interface Declarations)** (Impact: 1.1)
  * `f3` **(Interface Declarations)** (Impact: 1.1)
  * `f4` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3025`, `structural_boundaries: 15029`, `args: 11997`, `func_start: 11997`, `class_start: 5`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 12002`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` System, Xunit
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/coreclr/jit/gentree.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.893)
- **Top Global Matches:** file_cluster_6: 7.893, file_cluster_4: 12.75, file_cluster_8: 14.509
- **Magnitude:** 25038.66 | **LOC:** 35405 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 15.8%
- **Blast Radius:** changing it is visible to **56** in-repo importer(s); it depends on **6**; blast radius 0.083; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 93.2234% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Compiler::gtFoldExprHWIntrinsic` **(Many-Argument Workhorses)** (Impact: 819.7)
    * *Intent:* //------------------------------------------------------------------------ // gtFoldExprHWIntrinsic:...
  * `Compiler::gtSetEvalOrder` **(Many-Argument Workhorses)** (Impact: 652.7)
    * *Intent:* * * Given a tree, figure out the order in which its sub-operands should be * evaluated. If the secon...
  * `GenTreeHWIntrinsic::GetHWIntrinsicIdForBinOp` **(Many-Argument Workhorses)** (Impact: 573.7)
    * *Intent:* // GetHWIntrinsicIdForBinOp: Returns intrinsic ID based on the oper, base type, and simd size // // ...
  * `Compiler::gtDispTree` **(Many-Argument Workhorses)** (Impact: 558.9)
    * *Intent:* /*****************************************************************************/
  * `Compiler::gtSetMultiOpOrder` **(Many-Argument Workhorses)** (Impact: 524.6)
    * *Intent:* #if defined(FEATURE_SIMD) || defined(FEATURE_HW_INTRINSICS) //--------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2713 instances
* *State Mutation (weighted view):* 8494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7368`, `structural_boundaries: 1633`, `args: 1631`, `func_start: 534`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 3068`, `dead_code: 76`, `planned_debt: 14`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 431`
* *Architecture:* `api: 7`, `import: 12`
* *Defense:* `safety: 1143`, `doc: 40`, `immutability_locks: 262`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 47):` gtlist.h, gtstructs.h, handlekinds.h, hwintrinsic.h, jitpch.h, simd.h
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `src/libraries/System.Runtime/ref/System.Runtime.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 11.532)
- **Top Global Matches:** file_cluster_0: 11.532, file_cluster_13: 13.301, file_cluster_16: 13.817
- **Magnitude:** 24834.68 | **LOC:** 17405 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **4889** in-repo importer(s); blast radius 21.245; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (71.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MulticastDelegate` **(Encapsulated Accessors)** (Impact: 5.3)
  * `MulticastDelegate` **(Stateful Encapsulated Methods)** (Impact: 5.2)
  * `Deconstruct` **(Generic / Templated Code)** (Impact: 4.9)
  * `Deconstruct` **(Generic / Templated Code)** (Impact: 4.8)
  * `Deconstruct` **(Generic / Templated Code)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 1438`, `args: 8156`, `func_start: 8599`, `class_start: 886`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 111`, `duplicate_logic: 1962`, `unreferenced_by_name: 881`
* *Architecture:* `io: 1`, `api: 9835`, `concurrency: 641`
* *Defense:* `safety: 247`, `sync_locks: 4`, `immutability_locks: 421`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.245
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4889):` (Excluded from Brief to save tokens)

### `src/coreclr/jit/emitarm64sve.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.588)
- **Top Global Matches:** file_cluster_8: 10.588, file_cluster_3: 15.619, file_cluster_6: 22.35
- **Magnitude:** 24042.8 | **LOC:** 20043 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 0.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.6%)
- **Documentation Coverage:** 7.5949% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitter::getInsSveExecutionCharacteristics` **(Many-Argument Workhorses)** (Impact: 2016.5)
    * *Intent:* #if defined(DEBUG) || defined(LATE_DISASM) //-------------------------------------------------------...
  * `emitter::emitInsSve_R_R_R_R` **(Many-Argument Workhorses)** (Impact: 1828.7)
    * *Intent:* /***************************************************************************** * * Add a SVE instruc...
  * `emitter::emitInsSve_R_R_R` **(Many-Argument Workhorses)** (Impact: 1713.0)
    * *Intent:* /***************************************************************************** * * Add a SVE instruc...
  * `emitter::emitInsSve_R_R_R_I` **(Many-Argument Workhorses)** (Impact: 1611.7)
    * *Intent:* /***************************************************************************** * * Add a SVE instruc...
  * `emitter::emitOutput_InstrSve` **(Many-Argument Workhorses)** (Impact: 1249.9)
    * *Intent:* /***************************************************************************** * * Append the machin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2242 instances
* *State Mutation (weighted view):* 6929
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7619`, `structural_boundaries: 348`, `args: 62`, `func_start: 94`
* *Risk/State:* `state_mutation: 2445`, `planned_debt: 3`, `unreferenced_by_name: 92`
* *Architecture:* `import: 16`
* *Defense:* `safety: 2850`, `doc: 79`, `immutability_locks: 167`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 10):` codegen.h, instr.h, instrsarm64sve.h, jitpch.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/tests/JIT/Methodical/fp/exgen/10w5d.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.422)
- **Top Global Matches:** file_cluster_11: 8.422, file_cluster_15: 8.97, file_cluster_2: 9.374
- **Magnitude:** 19118.14 | **LOC:** 36338 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.1%), Complexity Load (formerly Cognitive Load) (51.6%), Connectivity (formerly Api Exposure) (16.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Func_0_3_5_2_4` **(I/O & Config Routines)** (Impact: 22.4)
  * `Func_0_3_2_6_4` **(I/O & Config Routines)** (Impact: 19.1)
  * `Func_0_5_1_1` **(I/O & Config Routines)** (Impact: 17.7)
  * `Func_0_5_5_3` **(I/O & Config Routines)** (Impact: 16.9)
  * `Func_0_5_3_4_4` **(I/O & Config Routines)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 891 instances
* *State Mutation (weighted view):* 6838
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1858`, `structural_boundaries: 3314`, `args: 2011`, `func_start: 2239`, `class_start: 1370`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5056`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6315`, `import: 2`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` System, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/emitarm64.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.99)
- **Top Global Matches:** file_cluster_8: 8.99, file_cluster_6: 10.799, file_cluster_4: 18.63
- **Magnitude:** 18506.44 | **LOC:** 18013 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 0.017; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.8%)
- **Documentation Coverage:** 27.2401% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitter::emitDispInsHelp` **(Many-Argument Workhorses)** (Impact: 1372.8)
    * *Intent:* // // Arguments: // id - The instruction // isNew - Whether the instruction is newly generated (befo...
  * `emitter::getInsExecutionCharacteristics` **(Many-Argument Workhorses)** (Impact: 1255.5)
    * *Intent:* // // Arguments: // id - The current instruction descriptor to be evaluated // // Return Value: // A...
  * `emitter::emitIns_R_R_R` **(Many-Argument Workhorses)** (Impact: 1068.9)
    * *Intent:* /***************************************************************************** * * Add an instructio...
  * `emitter::emitOutputInstr` **(Many-Argument Workhorses)** (Impact: 731.0)
    * *Intent:* /***************************************************************************** * * Append the machin...
  * `emitter::emitIns_R_R` **(Many-Argument Workhorses)** (Impact: 683.3)
    * *Intent:* /***************************************************************************** * * Add an instructio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2029 instances
* *State Mutation (weighted view):* 6341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5086`, `structural_boundaries: 406`, `args: 272`, `func_start: 198`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2283`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 194`
* *Architecture:* `import: 21`
* *Defense:* `safety: 1635`, `doc: 128`, `immutability_locks: 112`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 20):` codegen.h, emit.h, emitjmps.h, instr.h, instrs.h, instrsarm64sve.h, jitpch.h, register.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/tests/JIT/jit64/regress/vsw/524070/test2.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.397)
- **Top Global Matches:** file_cluster_3: 10.397, file_cluster_8: 22.188, file_cluster_6: 34.548
- **Magnitude:** 17312.28 | **LOC:** 10529 | **CtrlFlow:** 83.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (96.9%), Guard Balance (formerly Safety Score) (68.8%), Connectivity (formerly Api Exposure) (3.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `func` **(Many-Argument Workhorses)** (Impact: 12877.0)
  * `TestEntryPoint` **(Annotated & Test Methods)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1406 instances
* *State Mutation (weighted view):* 4218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8735`, `structural_boundaries: 5`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 1406`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 30`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/libraries/Microsoft.Extensions.Configuration.Binder/tests/SourceGenerationTests/ConfigBindingGenTestDriver.cs` (CSHARP) | Magnitude: 85.14 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 35, core_var_decl: 25, api: 14
- `src/libraries/System.CodeDom/tests/System/CodeDom/CodeNamespaceTests.cs` (CSHARP) | Magnitude: 55.64 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, test: 40, core_var_decl: 28, state_mutation: 22
- `src/libraries/System.Linq/tests/ConcatTests.cs` (CSHARP) | Magnitude: 253.0 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 408, structural_boundaries: 94, core_var_decl: 68, args: 59
- `src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpAuthenticationManager.cs` (CSHARP) | Magnitude: 9.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 4, encapsulation: 4, args: 3
- `src/libraries/System.Formats.Asn1/tests/Reader/AssertHelpers.cs` (CSHARP) | Magnitude: 54.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 52, branch: 8, structural_boundaries: 7, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/libraries/System.ComponentModel.Composition/tests/System/ComponentModel/Composition/Hosting/CompositionTransactionTests.cs` (CSHARP) | Magnitude: 144.06 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 377, structural_boundaries: 108, test: 80, args: 59
- `src/libraries/Microsoft.CSharp/tests/IntegerUnaryOperationTests.cs` (CSHARP) | Magnitude: 43.92 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 92, decorators: 25, structural_boundaries: 24, safety: 22
- `src/libraries/System.CodeDom/tests/System/CodeDom/CodeTypeReferenceCollectionTests.cs` (CSHARP) | Magnitude: 42.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 21, args: 18, func_start: 17
- `src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/CodeSnippets.cs` (CSHARP) | Magnitude: 426.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1258, structural_boundaries: 366, api: 244, decorators: 206
- `src/tests/Loader/classloader/DefaultInterfaceMethods/sharedgenerics/non_virtual_calls_to_instance_methods.cs.template` (CSHARP) | Magnitude: 30.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 20, args: 13, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/tools/illink/test/Mono.Linker.Tests.Cases/Warnings/WarningSuppression/DetectRedundantSuppressionsInAssembly.cs` (CSHARP) | Magnitude: 0.01 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 5, decorators: 4, api: 3
- `src/tools/illink/test/Mono.Linker.Tests.Cases/Warnings/WarningSuppression/DetectRedundantSuppressionsInModule.cs` (CSHARP) | Magnitude: 0.01 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 5, decorators: 4, api: 3
- `src/coreclr/System.Private.CoreLib/src/System/Collections/EmptyReadOnlyDictionaryInternal.cs` (CSHARP) | Magnitude: 42.8 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 77, api: 22, args: 21, structural_boundaries: 19
- `src/coreclr/vm/bundle.cpp` (CPP) | Magnitude: 42.2 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, branch: 8, pointers: 8, state_mutation: 6
- `src/tests/Loader/classloader/DefaultInterfaceMethods/simple/simple.cs.template` (CSHARP) | Magnitude: 34.58 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 20, args: 14, func_start: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchemaPropertyCollection.cs` (CSHARP) | Magnitude: 217.68 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 288, branch: 45, safety: 38, state_mutation: 32
- `src/tests/JIT/Regression/JitBlue/Runtime_76273/Runtime_76273.cs` (CSHARP) | Magnitude: 36.18 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 39, api: 14, structural_boundaries: 10, core_var_decl: 10
- `src/mono/wasi/testassets/Http.cs` (CSHARP) | Magnitude: 72.02 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 21, concurrency: 12, safety: 9
- `src/mono/browser/runtime/loader/logging.ts` (TYPESCRIPT) | Magnitude: 157.76 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 105, branch: 38, core_var_decl: 20, structural_boundaries: 17
- `src/native/public/mono/metadata/details/metadata-functions.h` (CPP) | Magnitude: 16.8 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: pointers: 117, args: 75, immutability_locks: 34, structural_boundaries: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/libraries/Common/src/Interop/Unix/System.Native/Interop.Accept.cs` (CSHARP) | Magnitude: 5.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, api: 3, encapsulation: 3
- `src/libraries/Common/src/Interop/Windows/Kernel32/Interop.WaitForMultipleObjects.cs` (CSHARP) | Magnitude: 5.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, api: 3, encapsulation: 3
- `src/libraries/Common/src/Interop/Windows/Netapi32/Interop.DsEnumerateDomainTrustsW.cs` (CSHARP) | Magnitude: 5.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, api: 3, encapsulation: 3
- `src/libraries/Common/src/Interop/Windows/User32/Interop.LoadString.cs` (CSHARP) | Magnitude: 5.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, api: 3, encapsulation: 3
- `src/tests/CoreMangLib/system/enum/enumiconvertibletouint16.cs` (CSHARP) | Magnitude: 62.06 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 183, core_var_decl: 50, safety: 31, design_camel_case: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `eng/native/version/copy_version_files.sh` (SHELL) | Magnitude: 46.12 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 21, state_mutation: 13, core_var_decl: 13
- `src/mono/browser/runtime/memory.ts` (TYPESCRIPT) | Magnitude: 326.2 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 216, structural_boundaries: 165, args: 83, func_start: 72
- `src/native/public/mono/metadata/details/mono-private-unstable-functions.h` (CPP) | Magnitude: 15.2 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: pointers: 12, args: 7, immutability_locks: 6, structural_boundaries: 5
- `src/native/libs/System.Native/pal_autoreleasepool.m` (OBJECTIVE-C) | Magnitude: 9.36 | Delta: **0.168** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 10, safety_bypasses: 5, macros: 5, memory_alloc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/tests/JIT/Performance/CodeQuality/Math/Functions/Double/AcosDouble.cs` (CSHARP) | Magnitude: 15.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, core_var_decl: 5, state_mutation: 3
- `src/tests/JIT/Performance/CodeQuality/Math/Functions/Double/AsinDouble.cs` (CSHARP) | Magnitude: 15.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, core_var_decl: 5, state_mutation: 3
- `src/tests/JIT/Performance/CodeQuality/Math/Functions/Double/AtanDouble.cs` (CSHARP) | Magnitude: 15.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, core_var_decl: 5, state_mutation: 3
- `src/tests/JIT/Performance/CodeQuality/Math/Functions/Double/CeilingDouble.cs` (CSHARP) | Magnitude: 15.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, core_var_decl: 5, state_mutation: 3
- `src/tests/JIT/Performance/CodeQuality/Math/Functions/Double/CosDouble.cs` (CSHARP) | Magnitude: 15.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, core_var_decl: 5, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/libraries/System.Net.WebProxy/src/System/Net/WebProxy.NonWasm.cs` (CSHARP) | Magnitude: 34.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 12, core_var_decl: 8, branch: 7
- `src/mono/System.Private.CoreLib/src/System/GC.Mono.cs` (CSHARP) | Magnitude: 171.28 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 267, args: 59, func_start: 58, api: 46
- `src/native/external/libunwind/src/mi/Gget_proc_name.c` (C) | Magnitude: 0.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, pointers: 28, branch: 16, structural_boundaries: 15
- `src/libraries/Common/src/System/Security/Cryptography/RSACng.EncryptDecrypt.cs` (CSHARP) | Magnitude: 193.28 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 233, branch: 41, core_var_decl: 41, design_camel_case: 27
- `src/installer/tests/Assets/Projects/Component/Component.cs` (CSHARP) | Magnitude: 25.06 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 9, state_mutation: 7, core_var_decl: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/coreclr/pal/inc/unixasmmacrosriscv64.inc` (ASSEMBLY) | Magnitude: 26.7 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 206, macros: 78, core_var_decl: 17, bitwise_ops: 12
- `src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/Operator.cs` (CSHARP) | Magnitude: 17.4 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 13, api: 9, encapsulation: 5
- `src/coreclr/nativeaot/Runtime/arm64/UniversalTransition.S` (ASSEMBLY) | Magnitude: 19.1 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 53, args: 39, structural_boundaries: 31, bitwise_ops: 9
- `src/native/external/brotli/c/enc/cluster_inc.h` (CPP) | Magnitude: 0.3 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 249, state_mutation: 94, pointers: 74, branch: 62
- `src/mono/mono/tests/reflection-load-with-context.cs` (CSHARP) | Magnitude: 2.44 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 11, safety: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/libraries/Common/tests/System/Net/Http/HuffmanEncoder.cs` (CSHARP) | Magnitude: 41.84 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 294, state_mutation: 6, core_var_decl: 6, bitwise_ops: 5
- `src/libraries/System.Private.CoreLib/src/System/Globalization/GlobalizationExtensions.cs` (CSHARP) | Magnitude: 8.38 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 5, branch: 2, safety: 2
- `src/coreclr/pal/tests/palsuite/miscellaneous/FormatMessageW/test4/test.cpp` (CPP) | Magnitude: 19.66 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 5, args: 4, branch: 3
- `src/libraries/System.Security.Permissions/src/System/Security/Permissions/HostProtectionResource.cs` (CSHARP) | Magnitude: 16.44 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, core_var_decl: 13, design_pascal_case: 12, decorators: 3
- `src/libraries/System.Data.Odbc/src/Common/System/Data/ProviderBase/DbConnectionPoolOptions.cs` (CSHARP) | Magnitude: 30.88 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 8, api: 8, encapsulation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_3
- `src/libraries/System.Private.CoreLib/src/System/Runtime/Intrinsics/Scalar.cs` (CSHARP) | Magnitude: 1408.34 | Delta: **0.452** (centroid distance) | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 1798, branch: 712, structural_boundaries: 362, pointers: 186

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/mono/wasm/host/DevServer/WebAssemblyNetDebugProxyAppBuilderExtensions.cs` (CSHARP) | Magnitude: 391.92 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 412, structural_boundaries: 143, core_var_decl: 84, branch: 66
- `src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/TypeSystem/TypeDefinition.cs` (CSHARP) | Magnitude: 95.32 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 196, structural_boundaries: 42, branch: 24, args: 22
- `src/coreclr/vm/stubmgr.cpp` (CPP) | Magnitude: 789.04 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1285, pointers: 239, branch: 212, structural_boundaries: 165
- `src/coreclr/md/inc/metamodel.h` (CPP) | Magnitude: 1016.62 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1416, pointers: 326, args: 259, branch: 216
- `src/libraries/System.Reflection.MetadataLoadContext/tests/src/Tests/Type/TypeInvariants.cs` (CSHARP) | Magnitude: 220.06 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 482, test: 143, core_var_decl: 97, branch: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.Declarations/Conformance.dynamic.declarations.returnType.methods.cs` (CSHARP) | Magnitude: 91.24 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 236, structural_boundaries: 49, api: 33, safety_bypasses: 25
- `src/mono/sample/wasi/http-p2/Program.cs` (CSHARP) | Magnitude: 69.22 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 21, concurrency: 13, safety: 9
- `src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/BasicSymmetricCipherNCrypt.cs` (CSHARP) | Magnitude: 23.52 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 5, args: 5, func_start: 5
- `src/coreclr/inc/simplerhash.inl` (CPP) | Magnitude: 182.12 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 136, core_var_decl: 44, pointers: 32
- `src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.Declarations/Conformance.dynamic.declarations.backwardscompatible.cs` (CSHARP) | Magnitude: 315.44 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 913, structural_boundaries: 181, safety_bypasses: 157, api: 133

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/libraries/System.Net.NetworkInformation/src/System/Net/NetworkInformation/NetworkAddressChange.Windows.cs` (CSHARP) | Magnitude: 156.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 269, branch: 36, core_var_decl: 31, state_mutation: 21
- `src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DelegateCreationInfo.cs` (CSHARP) | Magnitude: 0.2 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 292, branch: 56, structural_boundaries: 46, core_var_decl: 38
- `src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.cs` (CSHARP) | Magnitude: 121.38 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 154, branch: 31, structural_boundaries: 26, state_mutation: 18
- `src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/ConfigurationElement.cs` (CSHARP) | Magnitude: 1189.68 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1512, branch: 358, core_var_decl: 230, state_mutation: 146
- `src/coreclr/jit/codegencommon.cpp` (CPP) | Magnitude: 3388.72 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 4055, pointers: 1535, branch: 1008, core_var_decl: 661

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.Context/Conformance.dynamic.context.property.autoproperty.regclass.cs` (CSHARP) | Magnitude: 449.42 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 981, structural_boundaries: 145, api: 142, core_var_decl: 122
- `src/mono/browser/runtime/queue.ts` (TYPESCRIPT) | Magnitude: 35.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 11, args: 7, func_start: 7
- `src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/queue.ts` (TYPESCRIPT) | Magnitude: 35.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 11, args: 7, func_start: 7
- `src/mono/mono/utils/mono-hwcap-arm64.c` (C) | Magnitude: 108.98 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 58, state_mutation: 30, core_var_decl: 30, design_snake_case: 30
- `src/mono/mono/mini/llvm-runtime.cpp` (CPP) | Magnitude: 11.06 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 14, indent_tabs: 13, import: 8, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Node/JsonNodeConverter.cs` (CSHARP) | Magnitude: 113.06 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 82, branch: 30, structural_boundaries: 16, state_mutation: 12
- `src/coreclr/utilcode/outstring.cpp` (CPP) | Magnitude: 151.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 108, pointers: 35, state_mutation: 30, branch: 28
- `src/libraries/System.Linq.Expressions/src/System/Dynamic/UpdateDelegates.Generated.cs` (CSHARP) | Magnitude: 1496.98 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1673, core_var_decl: 250, design_snake_case: 230, branch: 210
- `src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Formatter/Utf8Formatter.Integer.cs` (CSHARP) | Magnitude: 246.0 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 171, indent_spaces: 131, branch: 57, structural_boundaries: 25
- `src/tests/GC/Features/HeapExpansion/bestfit-threaded.cs` (CSHARP) | Magnitude: 106.36 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 130, core_var_decl: 31, design_snake_case: 27, branch: 26

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/SOSDacImpl.cs` -> Churn: **89.82%** | Cog Load: 39.1273% | Debt: 68.4428%
- `src/coreclr/jit/codegenwasm.cpp` -> Churn: **87.5%** | Cog Load: 76.8253% | Debt: 92.0172%
- `src/coreclr/jit/gentree.cpp` -> Churn: **83.6%** | Cog Load: 91.0429% | Debt: 54.8885%
- `src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/Dbi/DacDbiImpl.cs` -> Churn: **83.6%** | Cog Load: 36.7542% | Debt: 99.8128%
- `src/coreclr/jit/lower.cpp` -> Churn: **80.66%** | Cog Load: 37.7756% | Debt: 56.9001%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/coreclr/jit/emitarm64sve.cpp` -> **Yat Long Poon** (100.0% isolated ownership) | Magnitude: 24042.8
- `src/mono/mono/component/debugger-agent.c` -> **Thays Grazia** (100.0% isolated ownership) | Magnitude: 9938.5
- `src/coreclr/gc/plan_phase.cpp` -> **Jan Vorlicek** (100.0% isolated ownership) | Magnitude: 7792.02
- `src/coreclr/jit/emitarm.cpp` -> **Michal Strehovský** (100.0% isolated ownership) | Magnitude: 7758.44
- `src/libraries/System.Private.CoreLib/src/System/Runtime/Intrinsics/Arm/AdvSimd.cs` -> **Jan Jones** (100.0% isolated ownership) | Magnitude: 7462.8

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/libraries/System.Runtime.InteropServices/ref/System.Runtime.InteropServices.cs` -> **Severity: 3252.6** (Blast Radius: 32.526 * Doc Risk: 100.0%)
- `src/libraries/Fuzzing/DotnetFuzzing/Assert.cs` -> **Severity: 2350.1** (Blast Radius: 23.501 * Doc Risk: 100.0%)
- `src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/Diagnostics.cs` -> **Severity: 2249.1** (Blast Radius: 22.491 * Doc Risk: 100.0%)
- `src/libraries/System.Runtime/ref/System.Runtime.cs` -> **Severity: 2124.5** (Blast Radius: 21.245 * Doc Risk: 100.0%)
- `src/libraries/System.Console/ref/System.Console.cs` -> **Severity: 2043.5** (Blast Radius: 20.435 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 83275 literal sites + 1305 sites through wrappers = 84580
- **`memory_alloc`:** 5762 literal sites + 2048 sites through wrappers = 7810
- **`panics_and_aborts`:** 102466 literal sites + 1583 sites through wrappers = 104049

- `g_new0` (macro, memory_alloc, primitive): 428 call sites in 99 files -- `src/mono/browser/runtime/driver.c`
- `d` (function, debug_prints, primitive): 278 call sites in 86 files -- `src/tests/JIT/jit64/gc/misc/struct2_5_2.cs`
- `CoreClrAlloc` (function, memory_alloc, primitive): 191 call sites in 25 files -- `src/tests/Common/Platform/platformdefines.h`
- `g_slist_prepend` (function, memory_alloc, via g_new): 124 call sites in 43 files -- `src/mono/mono/eglib/gslist.c`
- `g_new` (macro, memory_alloc, primitive): 69 call sites in 40 files -- `src/mono/browser/runtime/driver.c`
- `ThrowSrgsException` (function, panics_and_aborts, primitive): 64 call sites in 1 files -- `src/libraries/System.Speech/src/Internal/SrgsParser/XmlParser.cs`
- `ep_rt_object_alloc` (macro, memory_alloc, primitive): 57 call sites in 26 files -- `src/coreclr/nativeaot/Runtime/eventpipe/ep-rt-aot.h`
- `ThrowClosed` (function, panics_and_aborts, primitive): 52 call sites in 1 files -- `src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBaseWriter.cs`
- `dn_vector_free` (function, memory_alloc, via dn_vector_custom_free): 48 call sites in 2 files -- `src/native/containers/dn-vector.h`
- `mono_add_unwind_op_def_cfa` (macro, memory_alloc, via g_slist_append): 44 call sites in 21 files -- `src/mono/mono/mini/mini-unwind.h`
- `error` (function, debug_prints, primitive): 43 call sites in 1 files -- `src/mono/mono/tests/generics-sharing.2.cs`
- `_alloca` (macro, memory_alloc, primitive): 42 call sites in 22 files -- `src/coreclr/pal/inc/pal.h`
*(+1265 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1395600 call pairs -- scoped 48.2%, unique 3.8%, ambiguous 32.5%, external 15.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| csharp | 1087460 | 54.2% | 0.6% | 35.0% | 10.1% |
| cpp | 206139 | 28.3% | 10.1% | 31.9% | 29.7% |
| c | 87338 | 21.7% | 28.7% | 6.7% | 42.9% |
| typescript | 5423 | 52.4% | 0.0% | 7.4% | 40.2% |
| python | 3551 | 20.7% | 0.0% | 4.3% | 75.0% |
| shell | 2324 | 11.4% | 0.8% | 0.2% | 87.6% |
| swift | 1131 | 79.0% | 0.0% | 0.4% | 20.5% |
| objective-c | 659 | 9.6% | 13.1% | 12.4% | 64.9% |
| javascript | 522 | 12.8% | 0.0% | 10.0% | 77.2% |
| yacc | 313 | 17.9% | 14.4% | 64.2% | 3.5% |

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
