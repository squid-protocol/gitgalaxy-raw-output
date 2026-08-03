# ARCHITECTURAL_BRIEF: runtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/runtime` |
| **Timestamp** | `2026-08-03T21:34:37.142872+00:00` |
| **Scan Duration** | `219.42s` |
| **Git Branch** | `main` |
| **Git Commit** | `aba46e33ea5ddd45d90e5c6a8b46bba6744ddc9a` |
| **Git Remote** | `https://github.com/dotnet/runtime.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 37810 malicious artifacts.

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
| Total Artifacts | 57632 |
| Analyzed Artifacts (Scanned) | 41256 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16376 |
| Total LOC | 6379237 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.6% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2238 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 733 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 31742 | 5045137 | 76.9% |
| CPP | 3376 | 805344 | 8.2% |
| C | 1953 | 371359 | 4.7% |
| XML | 1556 | 1994 | 3.8% |
| PLAINTEXT | 812 | 5 | 2.0% |
| MARKDOWN | 368 | 0 | 0.9% |
| ASSEMBLY | 304 | 48835 | 0.7% |
| SHELL | 183 | 18395 | 0.4% |
| TYPESCRIPT | 181 | 20774 | 0.4% |
| YAML | 180 | 11747 | 0.4% |
| JSON | 166 | 5987 | 0.4% |
| MAKEFILE | 82 | 7942 | 0.2% |
| PYTHON | 59 | 15001 | 0.1% |
| HTML | 52 | 1236 | 0.1% |
| POWERSHELL | 51 | 2820 | 0.1% |
| BATCH | 49 | 2580 | 0.1% |
| JAVASCRIPT | 49 | 3095 | 0.1% |
| M4 | 38 | 1534 | 0.1% |
| OBJECTIVE-C | 24 | 2150 | 0.1% |
| SWIFT | 10 | 9609 | 0.0% |
| DOCKERFILE | 7 | 171 | 0.0% |
| PERL | 5 | 894 | 0.0% |
| JAVA | 5 | 345 | 0.0% |
| CSV | 2 | 498 | 0.0% |
| YACC | 1 | 1782 | 0.0% |
| CSS | 1 | 3 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.555`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 26420 | 64.0% |
| file_cluster_13 | 6524 | 15.8% |
| file_cluster_0 | 3551 | 8.6% |
| file_cluster_16 | 1899 | 4.6% |
| file_cluster_4 | 917 | 2.2% |
| file_cluster_7 | 259 | 0.6% |
| file_cluster_15 | 116 | 0.3% |
| file_cluster_11 | 108 | 0.3% |
| file_cluster_9 | 102 | 0.2% |
| file_cluster_12 | 68 | 0.2% |
| file_cluster_17 | 52 | 0.1% |
| file_cluster_6 | 27 | 0.1% |
| file_cluster_1 | 27 | 0.1% |
| Unknown | 5 | 0.0% |
| file_cluster_2 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1175 | 2.8% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16376*

**Composition by Extension & Reason:**
- `.csproj`: 5717x Unsupported Format (.csproj), 123x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.csproj')
- `.il`: 3378x Unsupported Format (.il), 219x Excluded: Neighborhood Micro-Mass Limit Exceeded, 169x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ilproj`: 2748x Unsupported Format (.ilproj), 120x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 469x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.props`: 326x Unsupported Format (.props), 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Excluded (Unsupported Extension: '.props')
- `.cs`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Saturation: Line 15 exceeds 500 chars), 6x Excluded (Saturation: Line 22 exceeds 500 chars)
- `.targets`: 159x Unsupported Format (.targets), 51x Excluded (Unsupported Extension: '.targets'), 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.slnx`: 236x Unsupported Format (.slnx)
- `.resx`: 223x Unsupported Format (.resx)
- `.template`: 174x Unsupported Format (.template), 3x Excluded (Unsupported Extension: '.template')
- `.cpp`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 3188 commas in 635 LOC), 1x Excluded (Embedded Array/Matrix Payload: 30245 commas in 9163 LOC)
- `no_extension`: 78x Unsupported Format (.undeterminable), 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.yml`: 130x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 197 LOC), 1x Excluded (Static Asset Blob without Intent: 2078 LOC)
- `.proj`: 116x Unsupported Format (.proj), 8x Excluded (Unsupported Extension: '.proj'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Excluded (Binary Format Detected), 1x Excluded (Massive Static Asset Blob: 4283 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 25.1 | 11.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 34.3 | 35.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 20.3 | 6.0 | 5.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 31.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 19.4 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.2 | 0.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 60.1 | 99.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 43.5 | 2.8 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/mono/mono/tests/verifier/make_tests.sh` (Hits: 692)
- `src/native/external/zlib-ng/configure` (Hits: 666)
- `src/coreclr/scripts/superpmi.py` (Hits: 375)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Diagnostics.cs** (`src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/Diagnostics.cs`) — 5770 inbound connections
2. **System.Runtime.InteropServices.cs** (`src/libraries/System.Runtime.InteropServices/ref/System.Runtime.InteropServices.cs`) — 5015 inbound connections
3. **System.IO.cs** (`src/libraries/shims/System.IO/src/System.IO.cs`) — 3085 inbound connections
4. **System.Threading.cs** (`src/libraries/System.Threading/ref/System.Threading.cs`) — 2915 inbound connections
5. **System.Linq.cs** (`src/libraries/System.Linq/ref/System.Linq.cs`) — 2621 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.h** (`src/coreclr/vm/common.h`) — 104 outbound dependencies
2. **mini-runtime.c** (`src/mono/mono/mini/mini-runtime.c`) — 74 outbound dependencies
3. **icall.c** (`src/mono/mono/metadata/icall.c`) — 68 outbound dependencies
4. **ceemain.cpp** (`src/coreclr/vm/ceemain.cpp`) — 65 outbound dependencies
5. **debugger-agent.c** (`src/mono/mono/component/debugger-agent.c`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `func` (@ `src/tests/JIT/jit64/regress/vsw/524070/test2.cs`) -> Impact: **16780.7** | LOC: 1278
- `add_float` (@ `src/mono/mono/mini/mini-arm.c`) -> Impact: **7140.2** | LOC: 1919
- `OriginalString_AbsoluteUri_ToString_Test` (@ `src/libraries/System.Private.Uri/tests/FunctionalTests/UriCreateStringTests.cs`) -> Impact: **6480.3** | LOC: 629
- `emitter::emitInsWritesToLclVarStackLoc` (@ `src/coreclr/jit/emitloongarch64.cpp`) -> Impact: **6464.8** | LOC: 1884
- `TryScanMethod` (@ `src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/TypePreinit.cs`) -> Impact: **6325.6** | LOC: 1001
- `TestEntryPoint` (@ `src/tests/JIT/Regression/CLR-x86-JIT/V1-M12-Beta2/b71005/b71005.cs`) -> Impact: **5915.5** | LOC: 521
- `QuoteSnippetStringCStyle` (@ `src/libraries/System.CodeDom/src/Microsoft/CSharp/CSharpCodeGenerator.cs`) -> Impact: **5617.3** | LOC: 1526
- `ReadAsync` (@ `src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextReaderImplAsync.cs`) -> Impact: **5045.7** | LOC: 1364
  * *Intent:* // Reads next node from the input data
- `Log1P` (@ `src/libraries/System.Runtime.Numerics/src/System/Numerics/Complex.cs`) -> Impact: **4817.4** | LOC: 1357
  * *Intent:* // IEEE prohibit optimizations which are value changing // so we make sure that behaviour for the simplified version exactly match
- `emitter::emitIns_R_R_I` (@ `src/coreclr/jit/emitarm64.cpp`) -> Impact: **4658.4** | LOC: 1747

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `generateDummyProvider` (@ `src/coreclr/scripts/genDummyProvider.py`) -> **O(2^N) [Recursive]**
- `genEtwMacroHeader` (@ `src/coreclr/scripts/genEtwProvider.py`) -> **O(2^N) [Recursive]**
- `main` (@ `src/coreclr/scripts/jitformat.py`) -> **O(2^N) [Recursive]**
- `download_with_progress_urlretrieve` (@ `src/coreclr/scripts/jitutil.py`) -> **O(2^N) [Recursive]**
- `__exit__` (@ `src/coreclr/scripts/jitutil.py`) -> **O(2^N) [Recursive]**
- `format_pct` (@ `src/coreclr/scripts/superpmi.py`) -> **O(2^N) [Recursive]**
- `print_superpmi_error_result` (@ `src/coreclr/scripts/superpmi.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ logging.info("Merging MC files") pattern = os.path.join(self.temp_location, "*.mc") command = [self.mcs_path, "-merge", self.base_mch_file, patter...
- `setup_benchmark` (@ `src/coreclr/scripts/superpmi_collect_setup.py`) -> **O(2^N) [Recursive]**
- `append_diff_file` (@ `src/coreclr/scripts/superpmi_diffs_summarize.py`) -> **O(2^N) [Recursive]**
- `parse_mini_ops` (@ `src/mono/mono/mini/genmdesc.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `main_[Truncated]` (@ `src/native/external/zlib-ng/configure`) -> DB Complexity: **1437**
- `Compiler::getPrimitiveTypeForStruct` (@ `src/coreclr/jit/compiler.cpp`) -> DB Complexity: **927**
- `print_results_[Truncated]` (@ `src/tests/Common/scripts/bringup_runtest.sh`) -> DB Complexity: **714**
- `And` (@ `src/tests/JIT/Regression/VS-ia64-JIT/V2.0-Beta2/b311420/b311420.cs`) -> DB Complexity: **697**
  * *Intent:* // Logical & |
- `FileData` (@ `src/libraries/Common/tests/System/IO/Compression/FileData.cs`) -> DB Complexity: **667**
- `main_[Truncated]` (@ `src/native/external/zlib-ng/configure`) -> DB Complexity: **657**
- `Compiler::fgMorphInit` (@ `src/coreclr/jit/morph.cpp`) -> DB Complexity: **619**
  * *Intent:* */ #include "jitpch.h" #ifdef _MSC_VER #pragma hdrstop #endif #include "allocacheck.h" // for alloca
- `CodeGen::genBuildRegPairsStack` (@ `src/coreclr/jit/codegenarm64.cpp`) -> DB Complexity: **607**
- `emitter::emitInsWritesToLclVarStackLoc` (@ `src/coreclr/jit/emitloongarch64.cpp`) -> DB Complexity: **596**
- `add_float` (@ `src/mono/mono/mini/mini-arm.c`) -> DB Complexity: **583**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/coreclr/jit` | 290 | 351667.32 | 51.35% | 39.88% |
| `src/tests/JIT/Directed/cmov` | 16 | 326435.5 | 42.77% | 0.0% |
| `src/coreclr/vm` | 512 | 250960.58 | 42.9% | 47.24% |
| `src/tests/JIT/Directed/nullabletypes` | 21 | 144362.44 | 19.1% | 0.0% |
| `src/mono/mono/mini` | 159 | 136634.96 | 51.18% | 47.43% |
| `src/libraries/System.Private.CoreLib/src/System` | 276 | 120829.59 | 27.55% | 63.82% |
| `src/libraries/System.Private.Xml/src/System/Xml/Schema` | 104 | 73232.23 | 37.38% | 45.57% |
| `src/libraries/System.Runtime/tests/System.Runtime.Tests/System` | 124 | 73208.86 | 19.49% | 0.0% |
| `src/libraries/System.Private.Xml/src/System/Xml/Core` | 71 | 70844.06 | 42.02% | 50.21% |
| `src/libraries/System.Private.Xml/src/System/Xml/Serialization` | 76 | 66398.78 | 38.73% | 58.22% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/native/external/libunwind/.github/workflows/CI-unix.yml` -> **100.0%** Exposure
- `src/native/external/zstd/.cirrus.yml` -> **100.0%** Exposure
- `.devcontainer/scripts/postCreateCommand.sh` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.sh` -> **100.0%** Exposure
- `eng/common/dotnet-install.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `eng/pipelines/common/templates/pipeline-with-resources.yml` -> **100.0%** Exposure
- `dotnet.sh` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.sh` -> **100.0%** Exposure
- `eng/common/cross/tizen-fetch.sh` -> **100.0%** Exposure
- `eng/common/darc-init.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/libraries/System.Linq.Expressions/tests/Convert/ConvertCheckedTests.cs` -> **237** Orphaned Functions | **13** Duplicates
- `src/libraries/System.Linq.Expressions/tests/Convert/ConvertTests.cs` -> **250** Orphaned Functions | **0** Duplicates
- `src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/TensorOperation.cs` -> **1** Orphaned Functions | **249** Duplicates
- `src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector128Tests.cs` -> **233** Orphaned Functions | **17** Duplicates
- `src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector256Tests.cs` -> **198** Orphaned Functions | **52** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`.github/skills/ci-pipeline-monitor/scripts/validate_results.py`** -> AI Confidence: **99.48%**
2. **`src/mono/mono/component/debugger-agent.c`** -> AI Confidence: **99.48%**
3. **`src/mono/mono/eglib/test/test.c`** -> AI Confidence: **99.48%**
4. **`src/mono/mono/metadata/callspec.c`** -> AI Confidence: **99.48%**
5. **`src/mono/mono/metadata/class-init.c`** -> AI Confidence: **99.48%**
6. **`src/mono/mono/metadata/class-setup-vtable.c`** -> AI Confidence: **99.48%**
7. **`src/mono/mono/metadata/debug-helpers.c`** -> AI Confidence: **99.48%**
8. **`src/mono/mono/metadata/marshal-lightweight.c`** -> AI Confidence: **99.48%**
9. **`src/mono/mono/metadata/mono-basic-block.c`** -> AI Confidence: **99.48%**
10. **`src/mono/mono/metadata/sgen-mono-ilgen.c`** -> AI Confidence: **99.48%**
11. **`src/mono/mono/metadata/sre-encode.c`** -> AI Confidence: **99.48%**
12. **`src/mono/mono/mini/abcremoval.c`** -> AI Confidence: **99.48%**
13. **`src/mono/mono/mini/aot-compiler.c`** -> AI Confidence: **99.48%**
14. **`src/mono/mono/mini/calls.c`** -> AI Confidence: **99.48%**
15. **`src/mono/mono/mini/decompose.c`** -> AI Confidence: **99.48%**
16. **`src/mono/mono/mini/driver.c`** -> AI Confidence: **99.48%**
17. **`src/mono/mono/mini/dwarfwriter.c`** -> AI Confidence: **99.48%**
18. **`src/mono/mono/mini/interp/transform-simd.c`** -> AI Confidence: **99.48%**
19. **`src/mono/mono/mini/interp/transform.c`** -> AI Confidence: **99.48%**
20. **`src/mono/mono/mini/intrinsics.c`** -> AI Confidence: **99.48%**
21. **`src/mono/mono/mini/local-propagation.c`** -> AI Confidence: **99.48%**
22. **`src/mono/mono/mini/memory-access.c`** -> AI Confidence: **99.48%**
23. **`src/mono/mono/mini/method-to-ir.c`** -> AI Confidence: **99.48%**
24. **`src/mono/mono/mini/mini-amd64.c`** -> AI Confidence: **99.48%**
25. **`src/mono/mono/mini/mini-arm-gsharedvt.c`** -> AI Confidence: **99.48%**
26. **`src/mono/mono/mini/mini-arm.c`** -> AI Confidence: **99.48%**
27. **`src/mono/mono/mini/mini-arm64.c`** -> AI Confidence: **99.48%**
28. **`src/mono/mono/mini/mini-codegen.c`** -> AI Confidence: **99.48%**
29. **`src/mono/mono/mini/mini-gc.c`** -> AI Confidence: **99.48%**
30. **`src/mono/mono/mini/mini-llvm.c`** -> AI Confidence: **99.48%**
31. **`src/mono/mono/mini/mini-riscv.c`** -> AI Confidence: **99.48%**
32. **`src/mono/mono/mini/mini-s390x.c`** -> AI Confidence: **99.48%**
33. **`src/mono/mono/mini/mini-x86.c`** -> AI Confidence: **99.48%**
34. **`src/mono/mono/mini/ssa.c`** -> AI Confidence: **99.48%**
35. **`src/mono/mono/mini/trace.c`** -> AI Confidence: **99.48%**
36. **`src/mono/mono/mini/tramp-amd64-gsharedvt.c`** -> AI Confidence: **99.48%**
37. **`src/mono/mono/mini/tramp-arm-gsharedvt.c`** -> AI Confidence: **99.48%**
38. **`src/mono/mono/mini/tramp-ppc.c`** -> AI Confidence: **99.48%**
39. **`src/mono/mono/mini/tramp-s390x.c`** -> AI Confidence: **99.48%**
40. **`src/mono/mono/mini/tramp-x86.c`** -> AI Confidence: **99.48%**
41. **`src/mono/mono/mini/unwind.c`** -> AI Confidence: **99.48%**
42. **`src/mono/mono/unit-tests/test-mono-callspec.c`** -> AI Confidence: **99.48%**
43. **`src/mono/mono/utils/lock-free-alloc.c`** -> AI Confidence: **99.48%**
44. **`src/mono/mono/utils/mono-hwcap-arm.c`** -> AI Confidence: **99.48%**
45. **`src/mono/mono/utils/mono-os-wait-win32.c`** -> AI Confidence: **99.48%**
46. **`src/mono/mono/utils/mono-path.c`** -> AI Confidence: **99.48%**
47. **`src/native/external/brotli/c/enc/bit_cost.c`** -> AI Confidence: **99.48%**
48. **`src/native/external/brotli/c/enc/compress_fragment.c`** -> AI Confidence: **99.48%**
49. **`src/native/external/brotli/c/enc/compress_fragment_two_pass.c`** -> AI Confidence: **99.48%**
50. **`src/native/external/libunwind/src/dwarf/Gfind_unwind_table.c`** -> AI Confidence: **99.48%**
51. **`src/native/external/libunwind/src/nto/unw_nto_access_reg.c`** -> AI Confidence: **99.48%**
52. **`src/native/external/libunwind/src/x86/Gos-freebsd.c`** -> AI Confidence: **99.48%**
53. **`src/native/external/libunwind/tests/Gtest-trace.c`** -> AI Confidence: **99.48%**
54. **`src/native/external/libunwind/tests/ppc64-test-altivec.c`** -> AI Confidence: **99.48%**
55. **`src/native/external/libunwind/tests/test-async-sig.c`** -> AI Confidence: **99.48%**
56. **`src/native/external/libunwind/tests/test-ptrace.c`** -> AI Confidence: **99.48%**
57. **`src/native/external/zlib-ng/inflate.c`** -> AI Confidence: **99.48%**
58. **`src/coreclr/ilasm/prebuilt/asmparse.cpp`** -> AI Confidence: **99.48%**
59. **`src/coreclr/ildasm/dasm.cpp`** -> AI Confidence: **99.48%**
60. **`src/coreclr/ildasm/dis.cpp`** -> AI Confidence: **99.48%**
61. **`src/coreclr/ildasm/dres.cpp`** -> AI Confidence: **99.48%**
62. **`src/coreclr/interpreter/compiler.cpp`** -> AI Confidence: **99.48%**
63. **`src/coreclr/jit/codegenarm64.cpp`** -> AI Confidence: **99.48%**
64. **`src/coreclr/jit/codegencommon.cpp`** -> AI Confidence: **99.48%**
65. **`src/coreclr/jit/codegenloongarch64.cpp`** -> AI Confidence: **99.48%**
66. **`src/coreclr/jit/codegenriscv64.cpp`** -> AI Confidence: **99.48%**
67. **`src/coreclr/jit/codegenxarch.cpp`** -> AI Confidence: **99.48%**
68. **`src/coreclr/jit/compiler.cpp`** -> AI Confidence: **99.48%**
69. **`src/coreclr/jit/emit.cpp`** -> AI Confidence: **99.48%**
70. **`src/coreclr/jit/emitarm64.cpp`** -> AI Confidence: **99.48%**
71. **`src/coreclr/jit/emitloongarch64.cpp`** -> AI Confidence: **99.48%**
72. **`src/coreclr/jit/emitriscv64.cpp`** -> AI Confidence: **99.48%**
73. **`src/coreclr/jit/emitxarch.cpp`** -> AI Confidence: **99.48%**
74. **`src/coreclr/jit/gcencode.cpp`** -> AI Confidence: **99.48%**
75. **`src/coreclr/jit/hwintrinsiccodegenxarch.cpp`** -> AI Confidence: **99.48%**
76. **`src/coreclr/jit/jit.h`** -> AI Confidence: **99.48%**
77. **`src/coreclr/jit/utils.cpp`** -> AI Confidence: **99.48%**
78. **`src/coreclr/md/compiler/custattr_emit.cpp`** -> AI Confidence: **99.48%**
79. **`src/coreclr/md/compiler/custattr_import.cpp`** -> AI Confidence: **99.48%**
80. **`src/coreclr/md/compiler/import.cpp`** -> AI Confidence: **99.48%**
81. **`src/coreclr/md/compiler/importhelper.cpp`** -> AI Confidence: **99.48%**
82. **`src/coreclr/md/compiler/regmeta_emit.cpp`** -> AI Confidence: **99.48%**
83. **`src/coreclr/md/enc/metamodelenc.cpp`** -> AI Confidence: **99.48%**
84. **`src/coreclr/md/runtime/mdinternalro.cpp`** -> AI Confidence: **99.48%**
85. **`src/coreclr/nativeaot/Runtime/MethodTable.cpp`** -> AI Confidence: **99.48%**
86. **`src/coreclr/nativeaot/Runtime/rhassert.cpp`** -> AI Confidence: **99.48%**
87. **`src/coreclr/nativeaot/Runtime/unix/PalCreateDump.cpp`** -> AI Confidence: **99.48%**
88. **`src/coreclr/pal/src/cruntime/wchar.cpp`** -> AI Confidence: **99.48%**
89. **`src/coreclr/pal/src/exception/seh-unwind.cpp`** -> AI Confidence: **99.48%**
90. **`src/coreclr/pal/src/file/directory.cpp`** -> AI Confidence: **99.48%**
91. **`src/coreclr/pal/src/file/file.cpp`** -> AI Confidence: **99.48%**
92. **`src/coreclr/pal/src/locale/unicode.cpp`** -> AI Confidence: **99.48%**
93. **`src/coreclr/pal/src/misc/dbgmsg.cpp`** -> AI Confidence: **99.48%**
94. **`src/coreclr/pal/src/misc/fmtmessage.cpp`** -> AI Confidence: **99.48%**
95. **`src/coreclr/pal/src/misc/sysinfo.cpp`** -> AI Confidence: **99.48%**
96. **`src/coreclr/pal/src/synchmgr/synchcontrollers.cpp`** -> AI Confidence: **99.48%**
97. **`src/coreclr/pal/src/synchmgr/wait.cpp`** -> AI Confidence: **99.48%**
98. **`src/coreclr/pal/src/thread/threadsusp.cpp`** -> AI Confidence: **99.48%**
99. **`src/coreclr/tools/metainfo/mdinfo.cpp`** -> AI Confidence: **99.48%**
100. **`src/coreclr/tools/superpmi/mcs/mcs.cpp`** -> AI Confidence: **99.48%**
101. **`src/coreclr/tools/superpmi/mcs/removedup.cpp`** -> AI Confidence: **99.48%**
102. **`src/coreclr/tools/superpmi/mcs/verbdumpmap.cpp`** -> AI Confidence: **99.48%**
103. **`src/coreclr/tools/superpmi/mcs/verbmerge.cpp`** -> AI Confidence: **99.48%**
104. **`src/coreclr/tools/superpmi/superpmi/parallelsuperpmi.cpp`** -> AI Confidence: **99.48%**
105. **`src/coreclr/tools/superpmi/superpmi/superpmi.cpp`** -> AI Confidence: **99.48%**
106. **`src/coreclr/vm/array.cpp`** -> AI Confidence: **99.48%**
107. **`src/coreclr/vm/assemblyspec.cpp`** -> AI Confidence: **99.48%**
108. **`src/coreclr/vm/classcompat.cpp`** -> AI Confidence: **99.48%**
109. **`src/coreclr/vm/clsload.cpp`** -> AI Confidence: **99.48%**
110. **`src/coreclr/vm/cominterfacemarshaler.cpp`** -> AI Confidence: **99.48%**
111. **`src/coreclr/vm/coreassemblyspec.cpp`** -> AI Confidence: **99.48%**
112. **`src/coreclr/vm/customattribute.cpp`** -> AI Confidence: **99.48%**
113. **`src/coreclr/vm/dllimport.cpp`** -> AI Confidence: **99.48%**
114. **`src/coreclr/vm/eepolicy.cpp`** -> AI Confidence: **99.48%**
115. **`src/coreclr/vm/eventreporter.cpp`** -> AI Confidence: **99.48%**
116. **`src/coreclr/vm/eventtrace.cpp`** -> AI Confidence: **99.48%**
117. **`src/coreclr/vm/gccover.cpp`** -> AI Confidence: **99.48%**
118. **`src/coreclr/vm/genericdict.cpp`** -> AI Confidence: **99.48%**
119. **`src/coreclr/vm/generics.cpp`** -> AI Confidence: **99.48%**
120. **`src/coreclr/vm/genmeth.cpp`** -> AI Confidence: **99.48%**
121. **`src/coreclr/vm/i386/stublinkerx86.cpp`** -> AI Confidence: **99.48%**
122. **`src/coreclr/vm/interopconverter.cpp`** -> AI Confidence: **99.48%**
123. **`src/coreclr/vm/invokeutil.cpp`** -> AI Confidence: **99.48%**
124. **`src/coreclr/vm/jitinterface.cpp`** -> AI Confidence: **99.48%**
125. **`src/coreclr/vm/jitinterfacegen.cpp`** -> AI Confidence: **99.48%**
126. **`src/coreclr/vm/memberload.cpp`** -> AI Confidence: **99.48%**
127. **`src/coreclr/vm/methodtablebuilder.cpp`** -> AI Confidence: **99.48%**
128. **`src/coreclr/vm/mlinfo.cpp`** -> AI Confidence: **99.48%**
129. **`src/coreclr/vm/olevariant.cpp`** -> AI Confidence: **99.48%**
130. **`src/coreclr/vm/prestub.cpp`** -> AI Confidence: **99.48%**
131. **`src/coreclr/vm/qcallentrypoints.cpp`** -> AI Confidence: **99.48%**
132. **`src/coreclr/vm/runtimecallablewrapper.cpp`** -> AI Confidence: **99.48%**
133. **`src/coreclr/vm/siginfo.cpp`** -> AI Confidence: **99.48%**
134. **`src/coreclr/vm/stackwalk.cpp`** -> AI Confidence: **99.48%**
135. **`src/mono/mono/metadata/gc_wrapper.h`** -> AI Confidence: **99.48%**
136. **`src/mono/mono/tests/tailcall/split-fsharp.cpp`** -> AI Confidence: **99.48%**
137. **`src/mono/mono/utils/mono-sigcontext.h`** -> AI Confidence: **99.48%**
138. **`src/native/external/libunwind/include/libunwind.h.in`** -> AI Confidence: **99.48%**
139. **`src/tests/profiler/native/classfactory.cpp`** -> AI Confidence: **99.48%**
140. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/ReadyToRunSignature.cs`** -> AI Confidence: **99.48%**
141. **`src/coreclr/tools/r2rdump/Extensions.cs`** -> AI Confidence: **99.48%**
142. **`src/libraries/Microsoft.CSharp/tests/ImplicitConversionTests.cs`** -> AI Confidence: **99.48%**
143. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/Parser/KnownTypeSymbols.cs`** -> AI Confidence: **99.48%**
144. **`src/libraries/Microsoft.Extensions.DependencyModel/src/DependencyContextJsonReader.cs`** -> AI Confidence: **99.48%**
145. **`src/libraries/Microsoft.Win32.SystemEvents/src/Microsoft/Win32/SystemEvents.cs`** -> AI Confidence: **99.48%**
146. **`src/libraries/System.CodeDom/src/Microsoft/CSharp/CSharpCodeGenerator.cs`** -> AI Confidence: **99.48%**
147. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/CompositionContainer.cs`** -> AI Confidence: **99.48%**
148. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/BaseConfigurationRecord.cs`** -> AI Confidence: **99.48%**
149. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/ConfigurationElement.cs`** -> AI Confidence: **99.48%**
150. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/MgmtConfigurationRecord.cs`** -> AI Confidence: **99.48%**
151. **`src/libraries/System.Data.Common/src/System/Data/DataRelation.cs`** -> AI Confidence: **99.48%**
152. **`src/libraries/System.Data.Common/src/System/Data/DataSet.cs`** -> AI Confidence: **99.48%**
153. **`src/libraries/System.Data.Common/src/System/Data/XMLSchema.cs`** -> AI Confidence: **99.48%**
154. **`src/libraries/System.Data.Common/src/System/Data/XmlDataLoader.cs`** -> AI Confidence: **99.48%**
155. **`src/libraries/System.Data.Common/src/System/Xml/XmlDataDocument.cs`** -> AI Confidence: **99.48%**
156. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcConnection.cs`** -> AI Confidence: **99.48%**
157. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcParameter.cs`** -> AI Confidence: **99.48%**
158. **`src/libraries/System.Data.OleDb/src/ColumnBinding.cs`** -> AI Confidence: **99.48%**
159. **`src/libraries/System.Data.OleDb/src/OleDbDataReader.cs`** -> AI Confidence: **99.48%**
160. **`src/libraries/System.Data.OleDb/src/OleDbMetaDataFactory.cs`** -> AI Confidence: **99.48%**
161. **`src/libraries/System.Data.OleDb/src/System/Data/ProviderBase/DbConnectionPool.cs`** -> AI Confidence: **99.48%**
162. **`src/libraries/System.DirectoryServices.Protocols/src/System/DirectoryServices/Protocols/ldap/LdapConnection.cs`** -> AI Confidence: **99.48%**
163. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchemaClass.cs`** -> AI Confidence: **99.48%**
164. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/Domain.cs`** -> AI Confidence: **99.48%**
165. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/Utils.cs`** -> AI Confidence: **99.48%**
166. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarHeader.Read.cs`** -> AI Confidence: **99.48%**
167. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/NamedPipeServerStream.Windows.cs`** -> AI Confidence: **99.48%**
168. **`src/libraries/System.IO.Ports/src/System/IO/Ports/SerialStream.Windows.cs`** -> AI Confidence: **99.48%**
169. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/ExpressionStringBuilder.cs`** -> AI Confidence: **99.48%**
170. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Interpreter/LightCompiler.cs`** -> AI Confidence: **99.48%**
171. **`src/libraries/System.Management/src/System/Management/WMIGenerator.cs`** -> AI Confidence: **99.48%**
172. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiHttpWorld.wit.imports.wasi.http.v0_2_0.OutgoingHandlerInterop.cs`** -> AI Confidence: **99.48%**
173. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiHttpWorld.wit.imports.wasi.http.v0_2_0.TypesInterop.cs`** -> AI Confidence: **99.48%**
174. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/MsQuicConfiguration.cs`** -> AI Confidence: **99.48%**
175. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncEventArgs.cs`** -> AI Confidence: **99.48%**
176. **`src/libraries/System.Private.CoreLib/src/System/Array.cs`** -> AI Confidence: **99.48%**
177. **`src/libraries/System.Private.CoreLib/src/System/Reflection/MethodBaseInvoker.cs`** -> AI Confidence: **99.48%**
178. **`src/libraries/System.Private.CoreLib/src/System/Reflection/MethodInvoker.cs`** -> AI Confidence: **99.48%**
179. **`src/libraries/System.Private.CoreLib/src/System/Text/Ascii.Utility.cs`** -> AI Confidence: **99.48%**
180. **`src/libraries/System.Private.CoreLib/src/System/Text/Unicode/Utf8Utility.Transcoding.cs`** -> AI Confidence: **99.48%**
181. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonFormatReaderGenerator.cs`** -> AI Confidence: **99.48%**
182. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonFormatWriterGenerator.cs`** -> AI Confidence: **99.48%**
183. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/XmlJsonReader.cs`** -> AI Confidence: **99.48%**
184. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/XmlJsonWriter.cs`** -> AI Confidence: **99.48%**
185. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/SchemaImporter.cs`** -> AI Confidence: **99.48%**
186. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlFormatWriterGenerator.cs`** -> AI Confidence: **99.48%**
187. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBaseWriter.cs`** -> AI Confidence: **99.48%**
188. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBinaryWriter.cs`** -> AI Confidence: **99.48%**
189. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlDictionaryWriter.cs`** -> AI Confidence: **99.48%**
190. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlUTF8TextReader.cs`** -> AI Confidence: **99.48%**
191. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/XContainer.cs`** -> AI Confidence: **99.48%**
192. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Schema/XNodeValidator.cs`** -> AI Confidence: **99.48%**
193. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/LoadFromReader.cs`** -> AI Confidence: **99.48%**
194. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/InputSpace.cs`** -> AI Confidence: **99.48%**
195. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/XmlFactoryWriterTests.cs`** -> AI Confidence: **99.48%**
196. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlCharCheckingWriter.cs`** -> AI Confidence: **99.48%**
197. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextReaderImpl.cs`** -> AI Confidence: **99.48%**
198. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextWriter.cs`** -> AI Confidence: **99.48%**
199. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWellFormedWriter.cs`** -> AI Confidence: **99.48%**
200. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/DocumentSchemaValidator.cs`** -> AI Confidence: **99.48%**
201. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/DtdParser.cs`** -> AI Confidence: **99.48%**
202. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/Parser.cs`** -> AI Confidence: **99.48%**
203. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/Preprocessor.cs`** -> AI Confidence: **99.48%**
204. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/SchemaSetCompiler.cs`** -> AI Confidence: **99.48%**
205. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XdrBuilder.cs`** -> AI Confidence: **99.48%**
206. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XdrValidator.cs`** -> AI Confidence: **99.48%**
207. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchemaException.cs`** -> AI Confidence: **99.48%**
208. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchemaValidator.cs`** -> AI Confidence: **99.48%**
209. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XsdValidator.cs`** -> AI Confidence: **99.48%**
210. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/SchemaObjectWriter.cs`** -> AI Confidence: **99.48%**
211. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSchemaExporter.cs`** -> AI Confidence: **99.48%**
212. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationReader.cs`** -> AI Confidence: **99.48%**
213. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationReaderILGen.cs`** -> AI Confidence: **99.48%**
214. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationWriter.cs`** -> AI Confidence: **99.48%**
215. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationWriterILGen.cs`** -> AI Confidence: **99.48%**
216. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/GenerateHelper.cs`** -> AI Confidence: **99.48%**
217. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ContainerAction.cs`** -> AI Confidence: **99.48%**
218. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/NumberAction.cs`** -> AI Confidence: **99.48%**
219. **`src/libraries/System.Private.Xml/tests/Xslt/XslTransformApi/CXslTArgumentList.cs`** -> AI Confidence: **99.48%**
220. **`src/libraries/System.Reflection.DispatchProxy/src/System/Reflection/DispatchProxyGenerator.cs`** -> AI Confidence: **99.48%**
221. **`src/libraries/System.Runtime/tests/System.IO.FileSystem.Tests/Directory/ReparsePoints_MountVolume.cs`** -> AI Confidence: **99.48%**
222. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/CommonObjectSecurity.cs`** -> AI Confidence: **99.48%**
223. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/NativeObjectSecurity.cs`** -> AI Confidence: **99.48%**
224. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/Win32.cs`** -> AI Confidence: **99.48%**
225. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/CmsSigner.cs`** -> AI Confidence: **99.48%**
226. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/EccKeyFormatHelper.cs`** -> AI Confidence: **99.48%**
227. **`src/libraries/System.ServiceModel.Syndication/src/System/ServiceModel/Syndication/Atom10FeedFormatter.cs`** -> AI Confidence: **99.48%**
228. **`src/libraries/System.ServiceModel.Syndication/src/System/ServiceModel/Syndication/Rss20FeedFormatter.cs`** -> AI Confidence: **99.48%**
229. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/Arc.cs`** -> AI Confidence: **99.48%**
230. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/BackEnd.cs`** -> AI Confidence: **99.48%**
231. **`src/libraries/System.Speech/src/Internal/Synthesis/SSmlParser.cs`** -> AI Confidence: **99.48%**
232. **`src/libraries/System.Speech/src/Internal/Synthesis/VoiceSynthesis.cs`** -> AI Confidence: **99.48%**
233. **`src/libraries/System.Speech/src/Recognition/RecognizerBase.cs`** -> AI Confidence: **99.48%**
234. **`src/libraries/System.Speech/src/Result/RecognizedPhrase.cs`** -> AI Confidence: **99.48%**
235. **`src/libraries/System.Speech/src/Synthesis/PromptBuilder.cs`** -> AI Confidence: **99.48%**
236. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/DBCSCodePageEncoding.cs`** -> AI Confidence: **99.48%**
237. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/GB18030Encoding.cs`** -> AI Confidence: **99.48%**
238. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/ISO2022Encoding.cs`** -> AI Confidence: **99.48%**
239. **`src/libraries/System.Text.Json/gen/JsonSourceGenerator.Parser.cs`** -> AI Confidence: **99.48%**
240. **`src/libraries/System.Text.Json/src/System/Text/Json/ThrowHelper.Serialization.cs`** -> AI Confidence: **99.48%**
241. **`src/libraries/System.Text.Json/tests/System.Text.Json.SourceGeneration.Tests/Serialization/NumberHandlingTests.cs`** -> AI Confidence: **99.48%**
242. **`src/libraries/System.Transactions.Local/src/System/Transactions/TransactionsEtwProvider.cs`** -> AI Confidence: **99.48%**
243. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataMethodInstance.cs`** -> AI Confidence: **99.48%**
244. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/SOSDacImpl.cs`** -> AI Confidence: **99.48%**
245. **`src/tests/GC/Features/PartialCompaction/partialcompactionwloh.cs`** -> AI Confidence: **99.48%**
246. **`src/tests/GC/Stress/Framework/ReliabilityFramework.cs`** -> AI Confidence: **99.48%**
247. **`src/mono/browser/runtime/marshal-to-cs.ts`** -> AI Confidence: **99.48%**
248. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/marshal-to-cs.ts`** -> AI Confidence: **99.48%**
249. **`src/native/libs/System.Globalization.Native/pal_locale.m`** -> AI Confidence: **99.48%**
250. **`src/tasks/AppleAppBuilder/Templates/runtime-librarymode.m`** -> AI Confidence: **99.48%**
251. **`src/tasks/AppleAppBuilder/Templates/runtime.m`** -> AI Confidence: **99.48%**
252. **`src/coreclr/ilasm/ilasmpch.h`** -> AI Confidence: **99.44%**
253. **`src/native/external/libunwind/include/tdep/jmpbuf.h`** -> AI Confidence: **99.44%**
254. **`src/native/external/rapidjson/rapidjson.h`** -> AI Confidence: **99.44%**
255. **`src/native/external/zlib-ng/arch_functions.h`** -> AI Confidence: **99.44%**
256. **`src/native/libs/System.Globalization.Native/pal_icushim_internal.h`** -> AI Confidence: **99.44%**
257. **`src/native/external/brotli/c/enc/backward_references.h`** -> AI Confidence: **99.43%**
258. **`src/native/external/brotli/c/enc/histogram.h`** -> AI Confidence: **99.43%**
259. **`src/native/external/libunwind/src/ia64/Gfind_unwind_table.c`** -> AI Confidence: **99.43%**
260. **`src/coreclr/pal/src/file/path.cpp`** -> AI Confidence: **99.43%**
261. **`src/mono/mono/utils/mono-compiler.h`** -> AI Confidence: **99.43%**
262. **`src/native/external/llvm-libunwind/src/DwarfInstructions.hpp`** -> AI Confidence: **99.43%**
263. **`src/mono/mono/mini/mini-arch.h`** -> AI Confidence: **99.42%**
264. **`src/native/external/libunwind/include/tdep/dwarf-config.h`** -> AI Confidence: **99.42%**
265. **`src/native/external/libunwind/include/tdep/libunwind_i.h.in`** -> AI Confidence: **99.42%**
266. **`src/native/external/zlib-ng/zbuild.h`** -> AI Confidence: **99.42%**
267. **`src/native/external/zstd/lib/common/compiler.h`** -> AI Confidence: **99.42%**
268. **`src/native/external/zstd/lib/common/zstd_deps.h`** -> AI Confidence: **99.42%**
269. **`src/coreclr/scripts/superpmi.py`** -> AI Confidence: **99.39%**
270. **`src/mono/mono/eglib/gfile-posix.c`** -> AI Confidence: **99.39%**
271. **`src/mono/mono/eglib/gfile-unix.c`** -> AI Confidence: **99.39%**
272. **`src/mono/mono/eglib/gmisc-win32.c`** -> AI Confidence: **99.39%**
273. **`src/mono/mono/metadata/assembly.c`** -> AI Confidence: **99.39%**
274. **`src/mono/mono/metadata/class.c`** -> AI Confidence: **99.39%**
275. **`src/mono/mono/metadata/custom-attrs.c`** -> AI Confidence: **99.39%**
276. **`src/mono/mono/metadata/icall.c`** -> AI Confidence: **99.39%**
277. **`src/mono/mono/metadata/marshal.c`** -> AI Confidence: **99.39%**
278. **`src/mono/mono/metadata/native-library.c`** -> AI Confidence: **99.39%**
279. **`src/mono/mono/metadata/reflection.c`** -> AI Confidence: **99.39%**
280. **`src/mono/mono/metadata/sgen-new-bridge.c`** -> AI Confidence: **99.39%**
281. **`src/mono/mono/metadata/sre.c`** -> AI Confidence: **99.39%**
282. **`src/mono/mono/metadata/unsafe-accessor.c`** -> AI Confidence: **99.39%**
283. **`src/mono/mono/metadata/weak-hash.c`** -> AI Confidence: **99.39%**
284. **`src/mono/mono/mini/debug-mini.c`** -> AI Confidence: **99.39%**
285. **`src/mono/mono/mini/interp/interp.c`** -> AI Confidence: **99.39%**
286. **`src/mono/mono/mini/mini-exceptions.c`** -> AI Confidence: **99.39%**
287. **`src/mono/mono/mini/mini-generic-sharing.c`** -> AI Confidence: **99.39%**
288. **`src/mono/mono/mini/mini-ppc.c`** -> AI Confidence: **99.39%**
289. **`src/mono/mono/mini/mini-runtime.c`** -> AI Confidence: **99.39%**
290. **`src/mono/mono/mini/mini-trampolines.c`** -> AI Confidence: **99.39%**
291. **`src/mono/mono/mini/mini.c`** -> AI Confidence: **99.39%**
292. **`src/mono/mono/mini/monovm.c`** -> AI Confidence: **99.39%**
293. **`src/mono/mono/mini/simd-intrinsics.c`** -> AI Confidence: **99.39%**
294. **`src/mono/mono/mini/tramp-amd64.c`** -> AI Confidence: **99.39%**
295. **`src/mono/mono/mini/tramp-arm64.c`** -> AI Confidence: **99.39%**
296. **`src/mono/mono/profiler/aot.c`** -> AI Confidence: **99.39%**
297. **`src/mono/mono/profiler/mprof-report.c`** -> AI Confidence: **99.39%**
298. **`src/mono/mono/sgen/sgen-gc.c`** -> AI Confidence: **99.39%**
299. **`src/mono/mono/utils/lock-free-array-queue.c`** -> AI Confidence: **99.39%**
300. **`src/mono/mono/utils/mono-threads-state-machine.c`** -> AI Confidence: **99.39%**
301. **`src/mono/mono/utils/parse.c`** -> AI Confidence: **99.39%**
302. **`src/native/external/brotli/c/dec/decode.c`** -> AI Confidence: **99.39%**
303. **`src/native/external/brotli/c/enc/backward_references_hq.c`** -> AI Confidence: **99.39%**
304. **`src/native/external/brotli/c/enc/brotli_bit_stream.c`** -> AI Confidence: **99.39%**
305. **`src/native/external/brotli/c/enc/metablock.c`** -> AI Confidence: **99.39%**
306. **`src/native/external/libunwind/src/coredump/_UCD_create.c`** -> AI Confidence: **99.39%**
307. **`src/native/external/libunwind/src/nto/unw_nto_find_proc_info.c`** -> AI Confidence: **99.39%**
308. **`src/native/external/libunwind/src/setjmp/longjmp.c`** -> AI Confidence: **99.39%**
309. **`src/native/external/libunwind/tests/Garm64-test-sve-signal.c`** -> AI Confidence: **99.39%**
310. **`src/native/external/libunwind/tests/Gia64-test-nat.c`** -> AI Confidence: **99.39%**
311. **`src/native/external/libunwind/tests/Gtest-bt.c`** -> AI Confidence: **99.39%**
312. **`src/native/external/libunwind/tests/crasher.c`** -> AI Confidence: **99.39%**
313. **`src/native/external/libunwind/tests/test-setjmp.c`** -> AI Confidence: **99.39%**
314. **`src/native/external/zlib-ng/arch/x86/x86_features.c`** -> AI Confidence: **99.39%**
315. **`src/native/external/zstd/lib/compress/fse_compress.c`** -> AI Confidence: **99.39%**
316. **`src/native/libs/System.Native/pal_runtimeinformation.c`** -> AI Confidence: **99.39%**
317. **`src/native/libs/System.Security.Cryptography.Native/opensslshim.c`** -> AI Confidence: **99.39%**
318. **`src/native/minipal/random.c`** -> AI Confidence: **99.39%**
319. **`src/coreclr/binder/applicationcontext.cpp`** -> AI Confidence: **99.39%**
320. **`src/coreclr/binder/assemblybindercommon.cpp`** -> AI Confidence: **99.39%**
321. **`src/coreclr/binder/assemblyname.cpp`** -> AI Confidence: **99.39%**
322. **`src/coreclr/gc/objecthandle.cpp`** -> AI Confidence: **99.39%**
323. **`src/coreclr/gcinfo/gcinfoencoder.cpp`** -> AI Confidence: **99.39%**
324. **`src/coreclr/ildasm/dman.cpp`** -> AI Confidence: **99.39%**
325. **`src/coreclr/jit/ee_il_dll.cpp`** -> AI Confidence: **99.39%**
326. **`src/coreclr/md/compiler/disp.cpp`** -> AI Confidence: **99.39%**
327. **`src/coreclr/md/compiler/mdutil.cpp`** -> AI Confidence: **99.39%**
328. **`src/coreclr/md/compiler/regmeta.cpp`** -> AI Confidence: **99.39%**
329. **`src/coreclr/md/compiler/regmeta_import.cpp`** -> AI Confidence: **99.39%**
330. **`src/coreclr/md/compiler/regmeta_vm.cpp`** -> AI Confidence: **99.39%**
331. **`src/coreclr/md/enc/liteweightstgdbrw.cpp`** -> AI Confidence: **99.39%**
332. **`src/coreclr/md/enc/mdinternalrw.cpp`** -> AI Confidence: **99.39%**
333. **`src/coreclr/md/enc/metamodelrw.cpp`** -> AI Confidence: **99.39%**
334. **`src/coreclr/nativeaot/Runtime/eventtrace.cpp`** -> AI Confidence: **99.39%**
335. **`src/coreclr/nativeaot/Runtime/unix/HardwareExceptions.cpp`** -> AI Confidence: **99.39%**
336. **`src/coreclr/nativeaot/Runtime/unix/UnixNativeCodeManager.cpp`** -> AI Confidence: **99.39%**
337. **`src/coreclr/nativeaot/Runtime/unix/cgroupcpu.cpp`** -> AI Confidence: **99.39%**
338. **`src/coreclr/pal/src/misc/cgroup.cpp`** -> AI Confidence: **99.39%**
339. **`src/coreclr/pal/src/safecrt/vsprintf.cpp`** -> AI Confidence: **99.39%**
340. **`src/coreclr/pal/src/synchmgr/synchmanager.cpp`** -> AI Confidence: **99.39%**
341. **`src/coreclr/pal/src/thread/context.cpp`** -> AI Confidence: **99.39%**
342. **`src/coreclr/pal/src/thread/process.cpp`** -> AI Confidence: **99.39%**
343. **`src/coreclr/pal/src/thread/thread.cpp`** -> AI Confidence: **99.39%**
344. **`src/coreclr/tools/superpmi/superpmi-shared/callutils.cpp`** -> AI Confidence: **99.39%**
345. **`src/coreclr/tools/superpmi/superpmi/commandline.cpp`** -> AI Confidence: **99.39%**
346. **`src/coreclr/tools/superpmi/superpmi/streamingsuperpmi.cpp`** -> AI Confidence: **99.39%**
347. **`src/coreclr/utilcode/util.cpp`** -> AI Confidence: **99.39%**
348. **`src/coreclr/vm/assembly.cpp`** -> AI Confidence: **99.39%**
349. **`src/coreclr/vm/binder.cpp`** -> AI Confidence: **99.39%**
350. **`src/coreclr/vm/cdacstress.cpp`** -> AI Confidence: **99.39%**
351. **`src/coreclr/vm/class.cpp`** -> AI Confidence: **99.39%**
352. **`src/coreclr/vm/comcallablewrapper.cpp`** -> AI Confidence: **99.39%**
353. **`src/coreclr/vm/comdelegate.cpp`** -> AI Confidence: **99.39%**
354. **`src/coreclr/vm/commodule.cpp`** -> AI Confidence: **99.39%**
355. **`src/coreclr/vm/comtoclrcall.cpp`** -> AI Confidence: **99.39%**
356. **`src/coreclr/vm/crst.cpp`** -> AI Confidence: **99.39%**
357. **`src/coreclr/vm/debugdebugger.cpp`** -> AI Confidence: **99.39%**
358. **`src/coreclr/vm/dispatchinfo.cpp`** -> AI Confidence: **99.39%**
359. **`src/coreclr/vm/eeconfig.cpp`** -> AI Confidence: **99.39%**
360. **`src/coreclr/vm/eventtrace_bulktype.cpp`** -> AI Confidence: **99.39%**
361. **`src/coreclr/vm/exceptionhandling.cpp`** -> AI Confidence: **99.39%**
362. **`src/coreclr/vm/finalizerthread.cpp`** -> AI Confidence: **99.39%**
363. **`src/coreclr/vm/gcenv.ee.cpp`** -> AI Confidence: **99.39%**
364. **`src/coreclr/vm/gchelpers.cpp`** -> AI Confidence: **99.39%**
365. **`src/coreclr/vm/ilstubcache.cpp`** -> AI Confidence: **99.39%**
366. **`src/coreclr/vm/methodtable.cpp`** -> AI Confidence: **99.39%**
367. **`src/coreclr/vm/reflectioninvocation.cpp`** -> AI Confidence: **99.39%**
368. **`src/coreclr/vm/stublink.cpp`** -> AI Confidence: **99.39%**
369. **`src/coreclr/vm/threadsuspend.cpp`** -> AI Confidence: **99.39%**
370. **`src/coreclr/vm/typestring.cpp`** -> AI Confidence: **99.39%**
371. **`src/coreclr/vm/util.cpp`** -> AI Confidence: **99.39%**
372. **`src/native/corehost/bundle/extractor.cpp`** -> AI Confidence: **99.39%**
373. **`src/native/corehost/hostpolicy/deps_resolver.cpp`** -> AI Confidence: **99.39%**
374. **`src/native/corehost/test/nativehost/nativehost.cpp`** -> AI Confidence: **99.39%**
375. **`src/native/external/libunwind/include/libunwind_i.h`** -> AI Confidence: **99.39%**
376. **`src/native/external/llvm-libunwind/src/Unwind-EHABI.cpp`** -> AI Confidence: **99.39%**
377. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/TypeNameResolver.CoreCLR.cs`** -> AI Confidence: **99.39%**
378. **`src/coreclr/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncHelpers.CoreCLR.cs`** -> AI Confidence: **99.39%**
379. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Extensions/NonPortable/CustomAttributeInstantiator.cs`** -> AI Confidence: **99.39%**
380. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/Eabi/EabiUnwindConverter.cs`** -> AI Confidence: **99.39%**
381. **`src/coreclr/tools/aot/ILCompiler.Compiler/IL/ILImporter.Scanner.cs`** -> AI Confidence: **99.39%**
382. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/DebugInfoTableNode.cs`** -> AI Confidence: **99.39%**
383. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/IBC/IBCProfileParser.cs`** -> AI Confidence: **99.39%**
384. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/JitInterface/CorInfoImpl.ReadyToRun.cs`** -> AI Confidence: **99.39%**
385. **`src/coreclr/tools/r2rtest/BuildFolderSet.cs`** -> AI Confidence: **99.39%**
386. **`src/coreclr/tools/runincontext/runincontext.cs`** -> AI Confidence: **99.39%**
387. **`src/installer/tests/HostActivation.Tests/NativeHosting/HostContext.cs`** -> AI Confidence: **99.39%**
388. **`src/libraries/Common/src/Interop/Unix/System.Native/Interop.ForkAndExecProcess.cs`** -> AI Confidence: **99.39%**
389. **`src/libraries/Common/src/Interop/Unix/System.Security.Cryptography.Native/Interop.OpenSsl.cs`** -> AI Confidence: **99.39%**
390. **`src/libraries/Common/src/System/Diagnostics/NetFrameworkUtils.cs`** -> AI Confidence: **99.39%**
391. **`src/libraries/Common/src/System/Security/Cryptography/X509Certificates/X509CertificateLoader.Pkcs12.cs`** -> AI Confidence: **99.39%**
392. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Semantics/Conversion.cs`** -> AI Confidence: **99.39%**
393. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/SymbolTable.cs`** -> AI Confidence: **99.39%**
394. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/Emitter/CoreBindingHelpers.cs`** -> AI Confidence: **99.39%**
395. **`src/libraries/Microsoft.Extensions.DependencyInjection.Abstractions/src/ActivatorUtilities.cs`** -> AI Confidence: **99.39%**
396. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/DependencyInjectionEventSource.cs`** -> AI Confidence: **99.39%**
397. **`src/libraries/Microsoft.Extensions.DependencyModel/src/DependencyContextWriter.cs`** -> AI Confidence: **99.39%**
398. **`src/libraries/Microsoft.Extensions.Logging.EventSource/src/LoggingEventSource.cs`** -> AI Confidence: **99.39%**
399. **`src/libraries/Microsoft.Win32.Registry/src/Microsoft/Win32/RegistryKey.cs`** -> AI Confidence: **99.39%**
400. **`src/libraries/Microsoft.XmlSerializer.Generator/src/Sgen.cs`** -> AI Confidence: **99.39%**
401. **`src/libraries/System.CodeDom/src/Microsoft/VisualBasic/VBCodeGenerator.cs`** -> AI Confidence: **99.39%**
402. **`src/libraries/System.ComponentModel.Composition/src/Microsoft/Internal/GenerationServices.cs`** -> AI Confidence: **99.39%**
403. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/ImportingMember.cs`** -> AI Confidence: **99.39%**
404. **`src/libraries/System.ComponentModel.TypeConverter/src/MS/Internal/Xml/Linq/ComponentModel/XComponentModel.cs`** -> AI Confidence: **99.39%**
405. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/LicenseManager.cs`** -> AI Confidence: **99.39%**
406. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/TypeDescriptor.cs`** -> AI Confidence: **99.39%**
407. **`src/libraries/System.Data.Common/src/System/Data/DataColumn.cs`** -> AI Confidence: **99.39%**
408. **`src/libraries/System.Data.Common/src/System/Data/DataTable.cs`** -> AI Confidence: **99.39%**
409. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcDataReader.cs`** -> AI Confidence: **99.39%**
410. **`src/libraries/System.Data.OleDb/src/OleDbCommand.cs`** -> AI Confidence: **99.39%**
411. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/EventLog.cs`** -> AI Confidence: **99.39%**
412. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/EventLogInternal.cs`** -> AI Confidence: **99.39%**
413. **`src/libraries/System.Diagnostics.Process/src/Microsoft/Win32/SafeHandles/SafeProcessHandle.Windows.cs`** -> AI Confidence: **99.39%**
414. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/PerformanceCounterLib.cs`** -> AI Confidence: **99.39%**
415. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/ProcessManager.Windows.cs`** -> AI Confidence: **99.39%**
416. **`src/libraries/System.Diagnostics.TextWriterTraceListener/src/System/Diagnostics/XmlWriterTraceListener.cs`** -> AI Confidence: **99.39%**
417. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADStoreCtx.cs`** -> AI Confidence: **99.39%**
418. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADStoreCtx_LoadStore.cs`** -> AI Confidence: **99.39%**
419. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADStoreCtx_Query.cs`** -> AI Confidence: **99.39%**
420. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/SDSUtils.cs`** -> AI Confidence: **99.39%**
421. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/DirectoryContext.cs`** -> AI Confidence: **99.39%**
422. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/DirectoryEntry.cs`** -> AI Confidence: **99.39%**
423. **`src/libraries/System.IO.Compression/src/System/IO/Compression/ZipArchive.cs`** -> AI Confidence: **99.39%**
424. **`src/libraries/System.IO.FileSystem.Watcher/src/System/IO/FileSystemWatcher.Windows.cs`** -> AI Confidence: **99.39%**
425. **`src/libraries/System.IO.Hashing/src/System/IO/Hashing/XxHashShared.cs`** -> AI Confidence: **99.39%**
426. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/XmlCompatibilityReader.cs`** -> AI Confidence: **99.39%**
427. **`src/libraries/System.IO.Pipelines/src/System/IO/Pipelines/Pipe.cs`** -> AI Confidence: **99.39%**
428. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/NamedPipeServerStream.Unix.cs`** -> AI Confidence: **99.39%**
429. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Expressions.cs`** -> AI Confidence: **99.39%**
430. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/DebugViewWriter.cs`** -> AI Confidence: **99.39%**
431. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/IndexExpression.cs`** -> AI Confidence: **99.39%**
432. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/HttpConnectionPool.Http3.cs`** -> AI Confidence: **99.39%**
433. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/Http3Connection.cs`** -> AI Confidence: **99.39%**
434. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpConnection.cs`** -> AI Confidence: **99.39%**
435. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpConnectionBase.cs`** -> AI Confidence: **99.39%**
436. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpWindowsProxy.cs`** -> AI Confidence: **99.39%**
437. **`src/libraries/System.Net.HttpListener/src/System/Net/Managed/HttpResponseStream.Managed.cs`** -> AI Confidence: **99.39%**
438. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpListener.Windows.cs`** -> AI Confidence: **99.39%**
439. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpListenerRequest.Windows.cs`** -> AI Confidence: **99.39%**
440. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpListenerResponse.Windows.cs`** -> AI Confidence: **99.39%**
441. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/WebSockets/WebSocketBase.cs`** -> AI Confidence: **99.39%**
442. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpReplyReaderFactory.cs`** -> AI Confidence: **99.39%**
443. **`src/libraries/System.Net.NetworkInformation/src/System/Net/NetworkInformation/NetworkAddressChange.Unix.cs`** -> AI Confidence: **99.39%**
444. **`src/libraries/System.Net.Quic/src/System/Net/Quic/QuicConnection.SslConnectionOptions.cs`** -> AI Confidence: **99.39%**
445. **`src/libraries/System.Net.Requests/src/System/Net/FtpWebRequest.cs`** -> AI Confidence: **99.39%**
446. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStream.Protocol.cs`** -> AI Confidence: **99.39%**
447. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStreamCertificateContext.Linux.cs`** -> AI Confidence: **99.39%**
448. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/Socket.cs`** -> AI Confidence: **99.39%**
449. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncEventArgs.Windows.cs`** -> AI Confidence: **99.39%**
450. **`src/libraries/System.Net.WebSockets/src/System/Net/WebSockets/ManagedWebSocket.cs`** -> AI Confidence: **99.39%**
451. **`src/libraries/System.Private.CoreLib/gen/NativeRuntimeEventSourceGenerator.cs`** -> AI Confidence: **99.39%**
452. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Base64Helper/Base64DecoderHelper.cs`** -> AI Confidence: **99.39%**
453. **`src/libraries/System.Private.CoreLib/src/System/Collections/Generic/Dictionary.cs`** -> AI Confidence: **99.39%**
454. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/EventSource.cs`** -> AI Confidence: **99.39%**
455. **`src/libraries/System.Private.CoreLib/src/System/Environment.Windows.cs`** -> AI Confidence: **99.39%**
456. **`src/libraries/System.Private.CoreLib/src/System/Globalization/DateTimeFormat.cs`** -> AI Confidence: **99.39%**
457. **`src/libraries/System.Private.CoreLib/src/System/Reflection/ConstructorInvoker.cs`** -> AI Confidence: **99.39%**
458. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.Unix.cs`** -> AI Confidence: **99.39%**
459. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/DataContractSerializer.cs`** -> AI Confidence: **99.39%**
460. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/DataContractSet.cs`** -> AI Confidence: **99.39%**
461. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ExtensionDataReader.cs`** -> AI Confidence: **99.39%**
462. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/ReflectionJsonFormatWriter.cs`** -> AI Confidence: **99.39%**
463. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ReflectionXmlFormatWriter.cs`** -> AI Confidence: **99.39%**
464. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/SchemaExporter.cs`** -> AI Confidence: **99.39%**
465. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlFormatReaderGenerator.cs`** -> AI Confidence: **99.39%**
466. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializerReadContext.cs`** -> AI Confidence: **99.39%**
467. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializerWriteContext.cs`** -> AI Confidence: **99.39%**
468. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlCanonicalWriter.cs`** -> AI Confidence: **99.39%**
469. **`src/libraries/System.Private.Uri/src/System/Uri.cs`** -> AI Confidence: **99.39%**
470. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/XNodeSequenceRemove.cs`** -> AI Confidence: **99.39%**
471. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/CommonTests.cs`** -> AI Confidence: **99.39%**
472. **`src/libraries/System.Private.Xml/src/System/Xml/Cache/XPathDocumentBuilder.cs`** -> AI Confidence: **99.39%**
473. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlAutoDetectWriter.cs`** -> AI Confidence: **99.39%**
474. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextReaderImplAsync.cs`** -> AI Confidence: **99.39%**
475. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XsdValidatingReader.cs`** -> AI Confidence: **99.39%**
476. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlNode.cs`** -> AI Confidence: **99.39%**
477. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/DtdValidator.cs`** -> AI Confidence: **99.39%**
478. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/FacetChecker.cs`** -> AI Confidence: **99.39%**
479. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchemaValidationException.cs`** -> AI Confidence: **99.39%**
480. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/CodeGenerator.cs`** -> AI Confidence: **99.39%**
481. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/ImportContext.cs`** -> AI Confidence: **99.39%**
482. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/ReflectionXmlSerializationReader.cs`** -> AI Confidence: **99.39%**
483. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/ReflectionXmlSerializationWriter.cs`** -> AI Confidence: **99.39%**
484. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/SoapReflectionImporter.cs`** -> AI Confidence: **99.39%**
485. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlReflectionImporter.cs`** -> AI Confidence: **99.39%**
486. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSchemaImporter.cs`** -> AI Confidence: **99.39%**
487. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSchemas.cs`** -> AI Confidence: **99.39%**
488. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializer.cs`** -> AI Confidence: **99.39%**
489. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/XPathNavigator.cs`** -> AI Confidence: **99.39%**
490. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlILConstructAnalyzer.cs`** -> AI Confidence: **99.39%**
491. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlCollation.cs`** -> AI Confidence: **99.39%**
492. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XmlQueryTypeFactory.cs`** -> AI Confidence: **99.39%**
493. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/Processor.cs`** -> AI Confidence: **99.39%**
494. **`src/libraries/System.Private.Xml/src/System/Xml/Xslt/XslCompiledTransform.cs`** -> AI Confidence: **99.39%**
495. **`src/libraries/System.Private.Xml/src/System/Xml/Xslt/XslTransform.cs`** -> AI Confidence: **99.39%**
496. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/XsltArgumentList.cs`** -> AI Confidence: **99.39%**
497. **`src/libraries/System.Private.Xml/tests/Xslt/XslTransformApi/CXslTransform.cs`** -> AI Confidence: **99.39%**
498. **`src/libraries/System.Private.Xml/tests/Xslt/XslTransformApi/XSLTransform.cs`** -> AI Confidence: **99.39%**
499. **`src/libraries/System.Resources.Extensions/tests/BinaryFormatTests/Legacy/EqualityExtensions.cs`** -> AI Confidence: **99.39%**
500. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/CacheUsage.cs`** -> AI Confidence: **99.39%**
501. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/Interop/JavaScriptExports.Mono.cs`** -> AI Confidence: **99.39%**
502. **`src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector512Tests.cs`** -> AI Confidence: **99.39%**
503. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryFormatterWriter.cs`** -> AI Confidence: **99.39%**
504. **`src/libraries/System.Runtime.Serialization.Xml/tests/SerializationTestTypes/ComparisonHelper.cs`** -> AI Confidence: **99.39%**
505. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/Reflection/TypeTests.GetMember.cs`** -> AI Confidence: **99.39%**
506. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskCancelWaitTest.cs`** -> AI Confidence: **99.39%**
507. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/Privilege.cs`** -> AI Confidence: **99.39%**
508. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/SecurityDescriptor.cs`** -> AI Confidence: **99.39%**
509. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/SignedCms.cs`** -> AI Confidence: **99.39%**
510. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/SignerInfo.cs`** -> AI Confidence: **99.39%**
511. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/CryptoConfig.cs`** -> AI Confidence: **99.39%**
512. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/HashProviderDispenser.Windows.cs`** -> AI Confidence: **99.39%**
513. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslCrlCache.cs`** -> AI Confidence: **99.39%**
514. **`src/libraries/System.Security.Principal.Windows/src/System/Security/Principal/NTAccount.cs`** -> AI Confidence: **99.39%**
515. **`src/libraries/System.ServiceProcess.ServiceController/src/System/ServiceProcess/ServiceBase.cs`** -> AI Confidence: **99.39%**
516. **`src/libraries/System.Speech/src/Internal/GrammarBuilding/BuilderElements.cs`** -> AI Confidence: **99.39%**
517. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/SRGSCompiler.cs`** -> AI Confidence: **99.39%**
518. **`src/libraries/System.Speech/src/Recognition/Grammar.cs`** -> AI Confidence: **99.39%**
519. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/SBCSCodePageEncoding.cs`** -> AI Confidence: **99.39%**
520. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Collection/IEnumerableConverterFactory.cs`** -> AI Confidence: **99.39%**
521. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/FSharp/FSharpUnionConverter.cs`** -> AI Confidence: **99.39%**
522. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Metadata/DefaultJsonTypeInfoResolver.Helpers.cs`** -> AI Confidence: **99.39%**
523. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/WriteStack.cs`** -> AI Confidence: **99.39%**
524. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.cs`** -> AI Confidence: **99.39%**
525. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Utf8JsonReaderTests.TryGet.cs`** -> AI Confidence: **99.39%**
526. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Utf8JsonReaderTests.cs`** -> AI Confidence: **99.39%**
527. **`src/libraries/System.Threading.Tasks.Parallel/src/System/Threading/Tasks/Parallel.cs`** -> AI Confidence: **99.39%**
528. **`src/libraries/System.Web.HttpUtility/src/System/Web/Util/HttpEncoder.cs`** -> AI Confidence: **99.39%**
529. **`src/mono/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeTypeBuilder.Mono.cs`** -> AI Confidence: **99.39%**
530. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/Context/AMD64/AMD64Unwinder.cs`** -> AI Confidence: **99.39%**
531. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataMethodDefinition.cs`** -> AI Confidence: **99.39%**
532. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataModule.cs`** -> AI Confidence: **99.39%**
533. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/Dbi/DacDbiImpl.cs`** -> AI Confidence: **99.39%**
534. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/SOSDacImpl.IXCLRDataProcess.cs`** -> AI Confidence: **99.39%**
535. **`src/tasks/AndroidAppBuilder/ApkBuilder.cs`** -> AI Confidence: **99.39%**
536. **`src/tasks/AppleAppBuilder/AppleAppBuilder.cs`** -> AI Confidence: **99.39%**
537. **`src/tests/baseservices/exceptions/StackTracePreserve/StackTracePreserveTests.cs`** -> AI Confidence: **99.39%**
538. **`src/tests/baseservices/exceptions/unhandled/unhandledTester.cs`** -> AI Confidence: **99.39%**
539. **`src/tools/illink/src/ILLink.Shared/TrimAnalysis/HandleCallAction.cs`** -> AI Confidence: **99.39%**
540. **`src/tools/illink/src/linker/Linker.Steps/SweepStep.cs`** -> AI Confidence: **99.39%**
541. **`src/tools/illink/test/Mono.Linker.Tests.Cases/DataFlow/FeatureCheckDataFlow.cs`** -> AI Confidence: **99.39%**
542. **`src/mono/browser/runtime/gc-handles.ts`** -> AI Confidence: **99.39%**
543. **`src/mono/browser/runtime/loader/config.ts`** -> AI Confidence: **99.39%**
544. **`src/mono/browser/runtime/managed-exports.ts`** -> AI Confidence: **99.39%**
545. **`src/tasks/AppleAppBuilder/Templates/runtime-coreclr.m`** -> AI Confidence: **99.39%**
546. **`src/mono/mono/mini/exceptions-amd64.c`** -> AI Confidence: **99.35%**
547. **`src/native/external/brotli/c/tools/brotli.c`** -> AI Confidence: **99.35%**
548. **`src/coreclr/vm/amd64/excepamd64.cpp`** -> AI Confidence: **99.35%**
549. **`src/coreclr/vm/eetwain.cpp`** -> AI Confidence: **99.35%**
550. **`src/coreclr/vm/excep.cpp`** -> AI Confidence: **99.35%**
551. **`src/coreclr/vm/profilinghelper.cpp`** -> AI Confidence: **99.35%**
552. **`src/coreclr/tools/ILTrim.Core/DependencyAnalysis/MethodBodyNode.cs`** -> AI Confidence: **99.35%**
553. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/HttpConnectionPool.Http2.cs`** -> AI Confidence: **99.35%**
554. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/HttpConnectionPool.cs`** -> AI Confidence: **99.35%**
555. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlDocument.cs`** -> AI Confidence: **99.35%**
556. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/Compilation.cs`** -> AI Confidence: **99.35%**
557. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/XslCompiledTransform.cs`** -> AI Confidence: **99.35%**
558. **`src/libraries/System.Runtime.Serialization.Schema/src/System/Runtime/Serialization/Schema/CodeExporter.cs`** -> AI Confidence: **99.35%**
559. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Metadata/JsonTypeInfo.cs`** -> AI Confidence: **99.35%**
560. **`src/mono/wasi/Wasi.Build.Tests/BuildTestBase.cs`** -> AI Confidence: **99.35%**
561. **`src/mono/browser/runtime/invoke-cs.ts`** -> AI Confidence: **99.35%**
562. **`.github/skills/ci-pipeline-monitor/scripts/generate_report.py`** -> AI Confidence: **99.34%**
563. **`src/coreclr/scripts/fuzzlyn_summarize.py`** -> AI Confidence: **99.34%**
564. **`src/mono/mono/eglib/gpath.c`** -> AI Confidence: **99.34%**
565. **`src/mono/mono/eglib/test/driver.c`** -> AI Confidence: **99.34%**
566. **`src/mono/mono/mini/alias-analysis.c`** -> AI Confidence: **99.34%**
567. **`src/mono/mono/mini/dominators.c`** -> AI Confidence: **99.34%**
568. **`src/mono/mono/mini/graph.c`** -> AI Confidence: **99.34%**
569. **`src/mono/mono/mini/helpers.c`** -> AI Confidence: **99.34%**
570. **`src/mono/mono/mini/main.c`** -> AI Confidence: **99.34%**
571. **`src/mono/mono/mini/tramp-arm64-gsharedvt.c`** -> AI Confidence: **99.34%**
572. **`src/mono/mono/mini/type-checking.c`** -> AI Confidence: **99.34%**
573. **`src/mono/mono/profiler/log-args.c`** -> AI Confidence: **99.34%**
574. **`src/mono/mono/unit-tests/test-path.c`** -> AI Confidence: **99.34%**
575. **`src/native/eventpipe/ep-json-file.c`** -> AI Confidence: **99.34%**
576. **`src/native/external/brotli/c/dec/huffman.c`** -> AI Confidence: **99.34%**
577. **`src/native/external/brotli/c/enc/entropy_encode.c`** -> AI Confidence: **99.34%**
578. **`src/native/external/brotli/c/enc/literal_cost.c`** -> AI Confidence: **99.34%**
579. **`src/native/external/brotli/c/enc/static_dict.c`** -> AI Confidence: **99.34%**
580. **`src/native/external/libunwind/src/ptrace/_UPT_access_reg.c`** -> AI Confidence: **99.34%**
581. **`src/native/external/libunwind/src/ptrace/_UPT_reg_offset.c`** -> AI Confidence: **99.34%**
582. **`src/native/external/libunwind/tests/Gia64-test-rbs.c`** -> AI Confidence: **99.34%**
583. **`src/native/external/libunwind/tests/Gtest-concurrent.c`** -> AI Confidence: **99.34%**
584. **`src/native/external/libunwind/tests/Gx64-test-dwarf-expressions.c`** -> AI Confidence: **99.34%**
585. **`src/native/external/zlib-ng/deflate.c`** -> AI Confidence: **99.34%**
586. **`src/native/external/zlib-ng/deflate_quick.c`** -> AI Confidence: **99.34%**
587. **`src/native/external/zlib-ng/deflate_rle.c`** -> AI Confidence: **99.34%**
588. **`src/native/external/zlib-ng/trees.c`** -> AI Confidence: **99.34%**
589. **`src/native/external/zstd/lib/dictBuilder/divsufsort.c`** -> AI Confidence: **99.34%**
590. **`src/native/libs/System.Globalization.Native/pal_localeNumberData.c`** -> AI Confidence: **99.34%**
591. **`src/native/libs/System.Security.Cryptography.Native.Android/pal_ecc_import_export.c`** -> AI Confidence: **99.34%**
592. **`src/coreclr/hosts/corerun/dotenv.cpp`** -> AI Confidence: **99.34%**
593. **`src/coreclr/ildasm/dasm_sz.cpp`** -> AI Confidence: **99.34%**
594. **`src/coreclr/ildasm/windasm.cpp`** -> AI Confidence: **99.34%**
595. **`src/coreclr/jit/codegenarm.cpp`** -> AI Confidence: **99.34%**
596. **`src/coreclr/jit/codegenarmarch.cpp`** -> AI Confidence: **99.34%**
597. **`src/coreclr/jit/emitarm.cpp`** -> AI Confidence: **99.34%**
598. **`src/coreclr/jit/lowerarmarch.cpp`** -> AI Confidence: **99.34%**
599. **`src/coreclr/jit/lsra.cpp`** -> AI Confidence: **99.34%**
600. **`src/coreclr/jit/lsraarm.cpp`** -> AI Confidence: **99.34%**
601. **`src/coreclr/jit/lsraarm64.cpp`** -> AI Confidence: **99.34%**
602. **`src/coreclr/jit/lsraarmarch.cpp`** -> AI Confidence: **99.34%**
603. **`src/coreclr/jit/lsraloongarch64.cpp`** -> AI Confidence: **99.34%**
604. **`src/coreclr/jit/lsrariscv64.cpp`** -> AI Confidence: **99.34%**
605. **`src/coreclr/md/compiler/assemblymd.cpp`** -> AI Confidence: **99.34%**
606. **`src/coreclr/minipal/Unix/dn-stdio.cpp`** -> AI Confidence: **99.34%**
607. **`src/coreclr/pal/src/arch/i386/signalhandlerhelper.cpp`** -> AI Confidence: **99.34%**
608. **`src/coreclr/pal/src/exception/machmessage.cpp`** -> AI Confidence: **99.34%**
609. **`src/coreclr/pal/src/map/map.cpp`** -> AI Confidence: **99.34%**
610. **`src/coreclr/pal/src/misc/environ.cpp`** -> AI Confidence: **99.34%**
611. **`src/coreclr/tools/superpmi/mcs/verbildump.cpp`** -> AI Confidence: **99.34%**
612. **`src/coreclr/tools/superpmi/mcs/verbjitflags.cpp`** -> AI Confidence: **99.34%**
613. **`src/coreclr/tools/superpmi/superpmi-shared/logging.cpp`** -> AI Confidence: **99.34%**
614. **`src/coreclr/tools/superpmi/superpmi/jitinstance.cpp`** -> AI Confidence: **99.34%**
615. **`src/coreclr/utilcode/ilformatter.cpp`** -> AI Confidence: **99.34%**
616. **`src/coreclr/utilcode/opinfo.cpp`** -> AI Confidence: **99.34%**
617. **`src/coreclr/utilcode/posterror.cpp`** -> AI Confidence: **99.34%**
618. **`src/coreclr/utilcode/prettyprintsig.cpp`** -> AI Confidence: **99.34%**
619. **`src/coreclr/utilcode/sbuffer.cpp`** -> AI Confidence: **99.34%**
620. **`src/coreclr/utilcode/stacktrace.cpp`** -> AI Confidence: **99.34%**
621. **`src/coreclr/utilcode/utsem.cpp`** -> AI Confidence: **99.34%**
622. **`src/coreclr/vm/arm64/stubs.cpp`** -> AI Confidence: **99.34%**
623. **`src/coreclr/vm/comdatetime.cpp`** -> AI Confidence: **99.34%**
624. **`src/coreclr/vm/commtmemberinfomap.cpp`** -> AI Confidence: **99.34%**
625. **`src/coreclr/vm/exinfo.cpp`** -> AI Confidence: **99.34%**
626. **`src/coreclr/vm/pgo.cpp`** -> AI Confidence: **99.34%**
627. **`src/coreclr/vm/zapsig.cpp`** -> AI Confidence: **99.34%**
628. **`src/mono/mono/tests/split-tailcall-interface-conservestack.cpp`** -> AI Confidence: **99.34%**
629. **`src/native/corehost/fxr/standalone/hostpolicy_resolver.cpp`** -> AI Confidence: **99.34%**
630. **`src/native/external/llvm-libunwind/src/config.h`** -> AI Confidence: **99.34%**
631. **`src/native/external/zlib-ng/gzguts.h`** -> AI Confidence: **99.34%**
632. **`src/native/external/zlib-ng/win32/depcheck.cpp`** -> AI Confidence: **99.34%**
633. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeILGenerator.cs`** -> AI Confidence: **99.34%**
634. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeMethodBuilder.cs`** -> AI Confidence: **99.34%**
635. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/SignatureHelper.cs`** -> AI Confidence: **99.34%**
636. **`src/coreclr/nativeaot/Runtime.Base/src/System/Runtime/ExceptionHandling.cs`** -> AI Confidence: **99.34%**
637. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/InvokeUtils.cs`** -> AI Confidence: **99.34%**
638. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/DynamicInvokeInfo.cs`** -> AI Confidence: **99.34%**
639. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/TypeInfos/RuntimeTypeInfo.InvokeMember.cs`** -> AI Confidence: **99.34%**
640. **`src/coreclr/tools/Common/Compiler/DependencyAnalysis/ObjectDataBuilder.cs`** -> AI Confidence: **99.34%**
641. **`src/coreclr/tools/Common/JitInterface/SystemVStructClassificator.cs`** -> AI Confidence: **99.34%**
642. **`src/coreclr/tools/GCLogParser/parse-hb-log.cs`** -> AI Confidence: **99.34%**
643. **`src/coreclr/tools/ILTrim.Core/DependencyAnalysis/EcmaSignatureRewriter.cs`** -> AI Confidence: **99.34%**
644. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_ARM/ARMReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
645. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_ARM64/ARM64ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
646. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_LoongArch64/LoongArch64ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
647. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_RiscV64/RiscV64ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
648. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_X64/X64ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
649. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_X86/X86ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
650. **`src/coreclr/tools/dotnet-pgo/SPGO/FlowSmoothing.cs`** -> AI Confidence: **99.34%**
651. **`src/libraries/Common/src/System/Data/Common/DbConnectionOptions.Common.cs`** -> AI Confidence: **99.34%**
652. **`src/libraries/Common/src/System/Data/ProviderBase/DbConnectionFactory.cs`** -> AI Confidence: **99.34%**
653. **`src/libraries/Common/src/System/Net/Http/aspnetcore/Http3/QPack/QPackDecoder.cs`** -> AI Confidence: **99.34%**
654. **`src/libraries/Common/src/System/Number.Formatting.Common.cs`** -> AI Confidence: **99.34%**
655. **`src/libraries/Common/src/System/Security/Cryptography/X509Certificates/X509CertificateLoader.cs`** -> AI Confidence: **99.34%**
656. **`src/libraries/Common/tests/System/Xml/XmlCoreTest/ManagedNodeWriter.cs`** -> AI Confidence: **99.34%**
657. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Errors/UserStringBuilder.cs`** -> AI Confidence: **99.34%**
658. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Semantics/Operators.cs`** -> AI Confidence: **99.34%**
659. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/MaskedTextProvider.cs`** -> AI Confidence: **99.34%**
660. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/ReflectPropertyDescriptor.cs`** -> AI Confidence: **99.34%**
661. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/XmlUtil.cs`** -> AI Confidence: **99.34%**
662. **`src/libraries/System.Console/tests/TermInfo.Unix.cs`** -> AI Confidence: **99.34%**
663. **`src/libraries/System.Data.Common/src/System/Data/Common/DBCommandBuilder.cs`** -> AI Confidence: **99.34%**
664. **`src/libraries/System.Data.Common/src/System/Data/Common/DbDataAdapter.cs`** -> AI Confidence: **99.34%**
665. **`src/libraries/System.Data.Common/src/System/Data/ProviderBase/SchemaMapping.cs`** -> AI Confidence: **99.34%**
666. **`src/libraries/System.Data.Common/src/System/Data/XMLDiffLoader.cs`** -> AI Confidence: **99.34%**
667. **`src/libraries/System.Data.Odbc/src/Common/System/Data/Common/DBConnectionString.cs`** -> AI Confidence: **99.34%**
668. **`src/libraries/System.Data.Odbc/src/Common/System/Data/Common/DbConnectionOptions.cs`** -> AI Confidence: **99.34%**
669. **`src/libraries/System.Data.Odbc/src/Common/System/Data/ProviderBase/DbConnectionPool.cs`** -> AI Confidence: **99.34%**
670. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcCommand.cs`** -> AI Confidence: **99.34%**
671. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcMetaDataFactory.cs`** -> AI Confidence: **99.34%**
672. **`src/libraries/System.Data.OleDb/src/OleDbConnectionString.cs`** -> AI Confidence: **99.34%**
673. **`src/libraries/System.Data.OleDb/src/OleDbConnectionStringBuilder.cs`** -> AI Confidence: **99.34%**
674. **`src/libraries/System.Data.OleDb/src/RowBinding.cs`** -> AI Confidence: **99.34%**
675. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/DsesFilterAndTransform.cs`** -> AI Confidence: **99.34%**
676. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/ProcessStartInfo.cs`** -> AI Confidence: **99.34%**
677. **`src/libraries/System.Diagnostics.TraceSource/src/System/Diagnostics/TraceInternal.cs`** -> AI Confidence: **99.34%**
678. **`src/libraries/System.Diagnostics.TraceSource/src/System/Diagnostics/TraceListener.cs`** -> AI Confidence: **99.34%**
679. **`src/libraries/System.Diagnostics.TraceSource/src/System/Diagnostics/TraceSource.cs`** -> AI Confidence: **99.34%**
680. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySite.cs`** -> AI Confidence: **99.34%**
681. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySiteLink.cs`** -> AI Confidence: **99.34%**
682. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySiteLinkBridge.cs`** -> AI Confidence: **99.34%**
683. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ApplicationPartition.cs`** -> AI Confidence: **99.34%**
684. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/Forest.cs`** -> AI Confidence: **99.34%**
685. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/ZipPackage.cs`** -> AI Confidence: **99.34%**
686. **`src/libraries/System.IO.Ports/tests/SerialPort/Handshake.cs`** -> AI Confidence: **99.34%**
687. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/ILGen.cs`** -> AI Confidence: **99.34%**
688. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Binary.cs`** -> AI Confidence: **99.34%**
689. **`src/libraries/System.Linq.Expressions/tests/SequenceTests/SequenceTests.cs`** -> AI Confidence: **99.34%**
690. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpRequestState.cs`** -> AI Confidence: **99.34%**
691. **`src/libraries/System.Net.Http/src/System/Net/Http/Headers/HeaderDescriptor.cs`** -> AI Confidence: **99.34%**
692. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpResponseStream.Windows.cs`** -> AI Confidence: **99.34%**
693. **`src/libraries/System.Net.NetworkInformation/src/System/Net/NetworkInformation/NetworkAddressChange.Windows.cs`** -> AI Confidence: **99.34%**
694. **`src/libraries/System.Net.Requests/src/System/Net/FtpControlStream.cs`** -> AI Confidence: **99.34%**
695. **`src/libraries/System.Net.Security/src/System/Net/Security/SslAuthenticationOptions.cs`** -> AI Confidence: **99.34%**
696. **`src/libraries/System.Private.CoreLib/src/System/DefaultBinder.cs`** -> AI Confidence: **99.34%**
697. **`src/libraries/System.Private.CoreLib/src/System/HashCode.cs`** -> AI Confidence: **99.34%**
698. **`src/libraries/System.Private.CoreLib/src/System/SpanHelpers.Byte.cs`** -> AI Confidence: **99.34%**
699. **`src/libraries/System.Private.CoreLib/src/System/Text/Latin1Utility.cs`** -> AI Confidence: **99.34%**
700. **`src/libraries/System.Private.CoreLib/src/System/Text/StringBuilder.cs`** -> AI Confidence: **99.34%**
701. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XsdDataContractExporter.cs`** -> AI Confidence: **99.34%**
702. **`src/libraries/System.Private.Xml.Linq/tests/Properties/ImplicitConversionsRoundTrip.cs`** -> AI Confidence: **99.34%**
703. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/EventsHelper.cs`** -> AI Confidence: **99.34%**
704. **`src/libraries/System.Private.Xml.Linq/tests/misc/XLinqErrata4.cs`** -> AI Confidence: **99.34%**
705. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/EndOfLineHandlingTests.cs`** -> AI Confidence: **99.34%**
706. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/WriterSettings.cs`** -> AI Confidence: **99.34%**
707. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/ErrorConditions.cs`** -> AI Confidence: **99.34%**
708. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlEventCache.cs`** -> AI Confidence: **99.34%**
709. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWellFormedWriterHelpers.cs`** -> AI Confidence: **99.34%**
710. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWriter.cs`** -> AI Confidence: **99.34%**
711. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/DocumentXPathNavigator.cs`** -> AI Confidence: **99.34%**
712. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/DocumentXmlWriter.cs`** -> AI Confidence: **99.34%**
713. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlLoader.cs`** -> AI Confidence: **99.34%**
714. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/Inference/Infer.cs`** -> AI Confidence: **99.34%**
715. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/SchemaCollectionCompiler.cs`** -> AI Confidence: **99.34%**
716. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/SchemaCollectionpreProcessor.cs`** -> AI Confidence: **99.34%**
717. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchemaSet.cs`** -> AI Confidence: **99.34%**
718. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XsdBuilder.cs`** -> AI Confidence: **99.34%**
719. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/SourceInfo.cs`** -> AI Confidence: **99.34%**
720. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/QueryBuilder.cs`** -> AI Confidence: **99.34%**
721. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XslNumber.cs`** -> AI Confidence: **99.34%**
722. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ApplyTemplatesAction.cs`** -> AI Confidence: **99.34%**
723. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/TemplateLookupAction.cs`** -> AI Confidence: **99.34%**
724. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/EndOfLineHandlingTests.cs`** -> AI Confidence: **99.34%**
725. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/ErrorCondition.cs`** -> AI Confidence: **99.34%**
726. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCCloseOutput.cs`** -> AI Confidence: **99.34%**
727. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/XsltApiV2.cs`** -> AI Confidence: **99.34%**
728. **`src/libraries/System.Runtime.Numerics/src/System/Number.BigInteger.cs`** -> AI Confidence: **99.34%**
729. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/BigIntegerToStringTests.cs`** -> AI Confidence: **99.34%**
730. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryObjectReader.cs`** -> AI Confidence: **99.34%**
731. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/Runtime/JitInfoTests.cs`** -> AI Confidence: **99.34%**
732. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskCreateTest.cs`** -> AI Confidence: **99.34%**
733. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskFromAsyncTest.cs`** -> AI Confidence: **99.34%**
734. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/CertificateRequest.Load.cs`** -> AI Confidence: **99.34%**
735. **`src/libraries/System.ServiceModel.Syndication/src/System/ServiceModel/Syndication/AtomPub10ServiceDocumentFormatter.cs`** -> AI Confidence: **99.34%**
736. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/Graph.cs`** -> AI Confidence: **99.34%**
737. **`src/libraries/System.Speech/src/Internal/SrgsParser/XmlParser.cs`** -> AI Confidence: **99.34%**
738. **`src/libraries/System.Speech/src/Internal/Synthesis/TextWriterEngine.cs`** -> AI Confidence: **99.34%**
739. **`src/libraries/System.Text.Json/src/System/Text/Json/Reader/JsonReaderHelper.Unescaping.cs`** -> AI Confidence: **99.34%**
740. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Metadata/JsonPropertyInfo.cs`** -> AI Confidence: **99.34%**
741. **`src/libraries/System.Text.Json/tests/Common/TestClasses/TestClasses.SimpleTestClass.cs`** -> AI Confidence: **99.34%**
742. **`src/libraries/System.Text.Json/tests/Common/TestClasses/TestClasses.SimpleTestClassWithObject.cs`** -> AI Confidence: **99.34%**
743. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexNode.cs`** -> AI Confidence: **99.34%**
744. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexParser.cs`** -> AI Confidence: **99.34%**
745. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/Symbolic/RegexNodeConverter.cs`** -> AI Confidence: **99.34%**
746. **`src/libraries/System.Transactions.Local/src/System/Transactions/Oletx/OletxResourceManager.cs`** -> AI Confidence: **99.34%**
747. **`src/mono/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeILGenerator.Mono.cs`** -> AI Confidence: **99.34%**
748. **`src/mono/System.Private.CoreLib/src/System/Reflection/TypeNameResolver.Mono.cs`** -> AI Confidence: **99.34%**
749. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/Context/X86/X86Unwinder.cs`** -> AI Confidence: **99.34%**
750. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataStackWalk.cs`** -> AI Confidence: **99.34%**
751. **`src/tests/GC/Features/PartialCompaction/partialcompactiontest.cs`** -> AI Confidence: **99.34%**
752. **`src/tests/GC/Scenarios/LeakWheel/leakwheel.cs`** -> AI Confidence: **99.34%**
753. **`src/tests/GC/Stress/Framework/RFLogging.cs`** -> AI Confidence: **99.34%**
754. **`src/tests/JIT/SIMD/VectorGet.cs`** -> AI Confidence: **99.34%**
755. **`src/tests/Regressions/coreclr/0582/csgen.1.cs`** -> AI Confidence: **99.34%**
756. **`src/tools/illink/src/ILLink.Tasks/CreateRuntimeRootDescriptorFile.cs`** -> AI Confidence: **99.34%**
757. **`src/tools/illink/src/linker/Linker.Steps/UnreachableBlocksOptimizer.cs`** -> AI Confidence: **99.34%**
758. **`src/native/libs/System.Native/pal_environment.m`** -> AI Confidence: **99.34%**
759. **`src/mono/mono/mini/genmdesc.py`** -> AI Confidence: **99.32%**
760. **`src/tests/Common/scripts/migrate-tags.py`** -> AI Confidence: **99.32%**
761. **`src/mono/mono/eglib/gutf8.c`** -> AI Confidence: **99.32%**
762. **`src/mono/mono/mini/cfold.c`** -> AI Confidence: **99.32%**
763. **`src/mono/mono/mini/interp/transform-opt.c`** -> AI Confidence: **99.32%**
764. **`src/mono/mono/mini/linear-scan.c`** -> AI Confidence: **99.32%**
765. **`src/mono/mono/mini/liveness.c`** -> AI Confidence: **99.32%**
766. **`src/mono/mono/mini/seq-points.c`** -> AI Confidence: **99.32%**
767. **`src/mono/mono/utils/mono-hwcap-arm64.c`** -> AI Confidence: **99.32%**
768. **`src/mono/mono/utils/mono-hwcap-x86.c`** -> AI Confidence: **99.32%**
769. **`src/native/external/libunwind/src/ia64/Gregs.c`** -> AI Confidence: **99.32%**
770. **`src/native/external/libunwind/src/s390x/Lglobal.c`** -> AI Confidence: **99.32%**
771. **`src/native/external/libunwind/src/x86/Gos-linux.c`** -> AI Confidence: **99.32%**
772. **`src/native/external/libunwind/src/x86_64/Lglobal.c`** -> AI Confidence: **99.32%**
773. **`src/native/external/zlib-ng/arch/generic/crc32_braid_c.c`** -> AI Confidence: **99.32%**
774. **`src/native/external/zlib-ng/inftrees.c`** -> AI Confidence: **99.32%**
775. **`src/native/external/zstd/lib/compress/zstd_lazy.c`** -> AI Confidence: **99.32%**
776. **`src/native/libs/System.Security.Cryptography.Native.Apple/pal_seckey_macos.c`** -> AI Confidence: **99.32%**
777. **`src/coreclr/binder/defaultassemblybinder.cpp`** -> AI Confidence: **99.32%**
778. **`src/coreclr/binder/textualidentityparser.cpp`** -> AI Confidence: **99.32%**
779. **`src/coreclr/dlls/mscorpe/ceefilegenwritertokens.cpp`** -> AI Confidence: **99.32%**
780. **`src/coreclr/ilasm/assem.cpp`** -> AI Confidence: **99.32%**
781. **`src/coreclr/ildasm/util.hpp`** -> AI Confidence: **99.32%**
782. **`src/coreclr/inc/corhlprpriv.cpp`** -> AI Confidence: **99.32%**
783. **`src/coreclr/interpreter/compileropt.cpp`** -> AI Confidence: **99.32%**
784. **`src/coreclr/jit/assertionprop.cpp`** -> AI Confidence: **99.32%**
785. **`src/coreclr/jit/codegenlinear.cpp`** -> AI Confidence: **99.32%**
786. **`src/coreclr/jit/error.h`** -> AI Confidence: **99.32%**
787. **`src/coreclr/jit/fgdiagnostic.cpp`** -> AI Confidence: **99.32%**
788. **`src/coreclr/jit/inlinepolicy.cpp`** -> AI Confidence: **99.32%**
789. **`src/coreclr/jit/lower.cpp`** -> AI Confidence: **99.32%**
790. **`src/coreclr/jit/objectalloc.cpp`** -> AI Confidence: **99.32%**
791. **`src/coreclr/jit/promotiondecomposition.cpp`** -> AI Confidence: **99.32%**
792. **`src/coreclr/jit/scopeinfo.cpp`** -> AI Confidence: **99.32%**
793. **`src/coreclr/nativeaot/Runtime/arm64/AsmMacros_Shared.h`** -> AI Confidence: **99.32%**
794. **`src/coreclr/tools/superpmi/superpmi-shared/standardpch.h`** -> AI Confidence: **99.32%**
795. **`src/coreclr/tools/superpmi/superpmi/methodstatsemitter.cpp`** -> AI Confidence: **99.32%**
796. **`src/coreclr/unwinder/arm/unwinder.cpp`** -> AI Confidence: **99.32%**
797. **`src/coreclr/utilcode/sigparser.cpp`** -> AI Confidence: **99.32%**
798. **`src/coreclr/utilcode/splitpath.cpp`** -> AI Confidence: **99.32%**
799. **`src/coreclr/vm/gcenv.ee.common.cpp`** -> AI Confidence: **99.32%**
800. **`src/coreclr/vm/genanalysis.cpp`** -> AI Confidence: **99.32%**
801. **`src/coreclr/vm/unsafeaccessors.cpp`** -> AI Confidence: **99.32%**
802. **`src/native/public/mono/utils/details/mono-publib-types.h`** -> AI Confidence: **99.32%**
803. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Associates.cs`** -> AI Confidence: **99.32%**
804. **`src/coreclr/System.Private.CoreLib/src/System/Runtime/InteropServices/IDispatchHelpers.cs`** -> AI Confidence: **99.32%**
805. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaSignatureTranslator.cs`** -> AI Confidence: **99.32%**
806. **`src/coreclr/tools/Common/TypeSystem/IL/ILImporter.cs`** -> AI Confidence: **99.32%**
807. **`src/coreclr/tools/Common/TypeSystem/IL/ILStackHelper.cs`** -> AI Confidence: **99.32%**
808. **`src/coreclr/tools/Common/TypeSystem/IL/ILTokenReplacer.cs`** -> AI Confidence: **99.32%**
809. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/Amd64/UnwindInfo.cs`** -> AI Confidence: **99.32%**
810. **`src/coreclr/tools/aot/ILCompiler.TypeSystem.Tests/InstanceFieldLayoutTests.cs`** -> AI Confidence: **99.32%**
811. **`src/libraries/Common/src/System/Data/ProviderBase/DbReferenceCollection.cs`** -> AI Confidence: **99.32%**
812. **`src/libraries/Common/src/System/Security/Cryptography/Asn1/DirectoryStringAsn.xml.cs`** -> AI Confidence: **99.32%**
813. **`src/libraries/Common/src/System/Security/Cryptography/Asn1/GeneralNameAsn.xml.cs`** -> AI Confidence: **99.32%**
814. **`src/libraries/Common/src/System/Security/Cryptography/Asn1/Pkcs7/CertificateChoiceAsn.xml.cs`** -> AI Confidence: **99.32%**
815. **`src/libraries/Common/tests/System/Xml/ModuleCore/cparser.cs`** -> AI Confidence: **99.32%**
816. **`src/libraries/Microsoft.Extensions.Configuration.EnvironmentVariables/src/EnvironmentVariablesConfigurationProvider.cs`** -> AI Confidence: **99.32%**
817. **`src/libraries/Microsoft.Extensions.DependencyModel/src/CompilationOptions.cs`** -> AI Confidence: **99.32%**
818. **`src/libraries/System.CodeDom/src/System/CodeDom/Compiler/CodeGenerator.cs`** -> AI Confidence: **99.32%**
819. **`src/libraries/System.Collections.Immutable/tests/ImmutableCollectionsMarshal.cs`** -> AI Confidence: **99.32%**
820. **`src/libraries/System.Console/src/System/TermInfo.cs`** -> AI Confidence: **99.32%**
821. **`src/libraries/System.Data.Common/src/System/Data/DataTableExtensions.cs`** -> AI Confidence: **99.32%**
822. **`src/libraries/System.Data.Common/src/System/Data/Filter/AggregateNode.cs`** -> AI Confidence: **99.32%**
823. **`src/libraries/System.Data.Common/src/System/Data/Filter/ExpressionParser.cs`** -> AI Confidence: **99.32%**
824. **`src/libraries/System.Data.Common/tests/System/Data/DataTableReaderTest.cs`** -> AI Confidence: **99.32%**
825. **`src/libraries/System.Data.OleDb/src/System/Data/ProviderBase/DbReferenceCollection.cs`** -> AI Confidence: **99.32%**
826. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/LegacyPropagator.cs`** -> AI Confidence: **99.32%**
827. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/Reader/EventLogException.cs`** -> AI Confidence: **99.32%**
828. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/Reader/EventLogWatcher.cs`** -> AI Confidence: **99.32%**
829. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/Reader/EventRecord.cs`** -> AI Confidence: **99.32%**
830. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/DirectoryEntryManager.cs`** -> AI Confidence: **99.32%**
831. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/Locator.cs`** -> AI Confidence: **99.32%**
832. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ReplicationConnection.cs`** -> AI Confidence: **99.32%**
833. **`src/libraries/System.Formats.Asn1/src/System/Formats/Asn1/AsnWriter.Integer.cs`** -> AI Confidence: **99.32%**
834. **`src/libraries/System.Formats.Cbor/tests/Writer/CborWriterTests.Helpers.cs`** -> AI Confidence: **99.32%**
835. **`src/libraries/System.Linq.Expressions/tests/Convert/ConvertTests.cs`** -> AI Confidence: **99.32%**
836. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryDecrementNullableTests.cs`** -> AI Confidence: **99.32%**
837. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryIncrementNullableTests.cs`** -> AI Confidence: **99.32%**
838. **`src/libraries/System.Linq.Parallel/src/System/Linq/Parallel/QueryOperators/Inlined/NullableDoubleMinMaxAggregationOperator.cs`** -> AI Confidence: **99.32%**
839. **`src/libraries/System.Linq.Parallel/src/System/Linq/Parallel/QueryOperators/Inlined/NullableFloatMinMaxAggregationOperator.cs`** -> AI Confidence: **99.32%**
840. **`src/libraries/System.Management/src/System/Management/ManagementObject.cs`** -> AI Confidence: **99.32%**
841. **`src/libraries/System.Management/src/System/Management/Property.cs`** -> AI Confidence: **99.32%**
842. **`src/libraries/System.Memory/tests/Span/IndexOfAny.char.cs`** -> AI Confidence: **99.32%**
843. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/ConnectionSetupDistributedTracing.cs`** -> AI Confidence: **99.32%**
844. **`src/libraries/System.Net.Requests/src/System/Net/CommandStream.cs`** -> AI Confidence: **99.32%**
845. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/CounterGroup.cs`** -> AI Confidence: **99.32%**
846. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/TraceLogging/FieldMetadata.cs`** -> AI Confidence: **99.32%**
847. **`src/libraries/System.Private.CoreLib/src/System/Number.Dragon4.cs`** -> AI Confidence: **99.32%**
848. **`src/libraries/System.Private.CoreLib/src/System/Reflection/Emit/TypeNameBuilder.cs`** -> AI Confidence: **99.32%**
849. **`src/libraries/System.Private.CoreLib/src/System/Reflection/InvokerEmitUtil.cs`** -> AI Confidence: **99.32%**
850. **`src/libraries/System.Private.CoreLib/src/System/Text/UTF32Encoding.cs`** -> AI Confidence: **99.32%**
851. **`src/libraries/System.Private.CoreLib/src/System/Text/Unicode/TextSegmentationUtility.cs`** -> AI Confidence: **99.32%**
852. **`src/libraries/System.Private.CoreLib/src/System/Text/ValueStringBuilder.AppendFormat.cs`** -> AI Confidence: **99.32%**
853. **`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Sources/ManualResetValueTaskSourceCore.cs`** -> AI Confidence: **99.32%**
854. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlWriterDelegator.cs`** -> AI Confidence: **99.32%**
855. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Test.ModuleCore/testparser.cs`** -> AI Confidence: **99.32%**
856. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/CXMLReaderAttrTest.cs`** -> AI Confidence: **99.32%**
857. **`src/libraries/System.Private.Xml/src/System/Xml/Core/HtmlEncodedRawTextWriter.cs`** -> AI Confidence: **99.32%**
858. **`src/libraries/System.Private.Xml/src/System/Xml/Core/HtmlUtf8RawTextWriter.cs`** -> AI Confidence: **99.32%**
859. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/OptimizerPatterns.cs`** -> AI Confidence: **99.32%**
860. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/TailCallAnalyzer.cs`** -> AI Confidence: **99.32%**
861. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/DecimalFormatter.cs`** -> AI Confidence: **99.32%**
862. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XPath/XPathParser.cs`** -> AI Confidence: **99.32%**
863. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCCheckChars.cs`** -> AI Confidence: **99.32%**
864. **`src/libraries/System.Private.Xml/tests/XmlReader/Tests/ReadCharsTests.cs`** -> AI Confidence: **99.32%**
865. **`src/libraries/System.Private.Xml/tests/XmlReaderLib/ErrorCondition.cs`** -> AI Confidence: **99.32%**
866. **`src/libraries/System.Reflection.Emit/src/System/Reflection/Emit/PseudoCustomAttributesData.cs`** -> AI Confidence: **99.32%**
867. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryObjectWriter.cs`** -> AI Confidence: **99.32%**
868. **`src/libraries/System.Runtime.Serialization.Xml/tests/Canonicalization/CryptoCanonicalization/CanonicalEncoder.cs`** -> AI Confidence: **99.32%**
869. **`src/libraries/System.Security.Claims/src/System/Security/Claims/Claim.cs`** -> AI Confidence: **99.32%**
870. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/CmsRecipient.cs`** -> AI Confidence: **99.32%**
871. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/CanonicalXmlElement.cs`** -> AI Confidence: **99.32%**
872. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslX509ChainEventSource.cs`** -> AI Confidence: **99.32%**
873. **`src/libraries/System.Speech/src/Internal/Synthesis/ConvertTextFrag.cs`** -> AI Confidence: **99.32%**
874. **`src/libraries/System.Text.Json/src/System/Text/Json/Reader/Utf8JsonReader.MultiSegment.cs`** -> AI Confidence: **99.32%**
875. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Bytes.cs`** -> AI Confidence: **99.32%**
876. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.DateTime.cs`** -> AI Confidence: **99.32%**
877. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.DateTimeOffset.cs`** -> AI Confidence: **99.32%**
878. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Decimal.cs`** -> AI Confidence: **99.32%**
879. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Double.cs`** -> AI Confidence: **99.32%**
880. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Float.cs`** -> AI Confidence: **99.32%**
881. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Guid.cs`** -> AI Confidence: **99.32%**
882. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.String.cs`** -> AI Confidence: **99.32%**
883. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteValues.StringSegment.cs`** -> AI Confidence: **99.32%**
884. **`src/libraries/System.Text.Json/tests/Common/JsonNumberTestData.cs`** -> AI Confidence: **99.32%**
885. **`src/libraries/System.Text.Json/tests/Common/TestClasses/TestClasses.SimpleTestStruct.cs`** -> AI Confidence: **99.32%**
886. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexInterpreter.cs`** -> AI Confidence: **99.32%**
887. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexTree.cs`** -> AI Confidence: **99.32%**
888. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexWriter.cs`** -> AI Confidence: **99.32%**
889. **`src/libraries/System.Text.RegularExpressions/tests/UnitTests/RegexFindOptimizationsTests.cs`** -> AI Confidence: **99.32%**
890. **`src/libraries/System.Threading.Channels/src/System/Threading/Channels/ChannelUtilities.cs`** -> AI Confidence: **99.32%**
891. **`src/libraries/System.Transactions.Local/src/System/Transactions/TransactionScope.cs`** -> AI Confidence: **99.32%**
892. **`src/native/managed/cdac/tests/DumpTests/StackReferenceDumpTests.cs`** -> AI Confidence: **99.32%**
893. **`src/tests/JIT/Directed/ConstantFolding/value_numbering_unordered_comparisons_of_constants.cs`** -> AI Confidence: **99.32%**
894. **`src/tests/JIT/Directed/nullabletypes/isinst.cs`** -> AI Confidence: **99.32%**
895. **`src/tests/JIT/Directed/nullabletypes/isinst2.cs`** -> AI Confidence: **99.32%**
896. **`src/tests/JIT/Directed/nullabletypes/isinstboxed.cs`** -> AI Confidence: **99.32%**
897. **`src/tests/JIT/Directed/nullabletypes/isinstenum.cs`** -> AI Confidence: **99.32%**
898. **`src/tests/JIT/Directed/nullabletypes/isinstgenerics.cs`** -> AI Confidence: **99.32%**
899. **`src/tests/JIT/Directed/nullabletypes/isinstinterface.cs`** -> AI Confidence: **99.32%**
900. **`src/tests/JIT/Methodical/stringintern/test2.cs`** -> AI Confidence: **99.32%**
901. **`src/tests/JIT/Methodical/stringintern/test4.cs`** -> AI Confidence: **99.32%**
902. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M09.5-PDC/b25882/b25882.cs`** -> AI Confidence: **99.32%**
903. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M10/b02352/b02352.cs`** -> AI Confidence: **99.32%**
904. **`src/tests/JIT/Regression/CLR-x86-JIT/V1.2-Beta1/b210352/csharptester.cs`** -> AI Confidence: **99.32%**
905. **`src/tests/JIT/Regression/CLR-x86-JIT/v2.1/DDB/b202743/b202743.cs`** -> AI Confidence: **99.32%**
906. **`src/tests/JIT/Regression/JitBlue/GitHub_17777/GitHub_17777.cs`** -> AI Confidence: **99.32%**
907. **`src/tests/JIT/Regression/JitBlue/GitHub_9692/GitHub_9692.cs`** -> AI Confidence: **99.32%**
908. **`src/tests/JIT/Regression/JitBlue/Runtime_110958/Runtime_110985.cs`** -> AI Confidence: **99.32%**
909. **`src/tests/JIT/Regression/JitBlue/Runtime_66089/Runtime_66089.cs`** -> AI Confidence: **99.32%**
910. **`src/tests/JIT/SIMD/VectorArrayInit.cs`** -> AI Confidence: **99.32%**
911. **`src/tests/JIT/SIMD/VectorCopyToArray.cs`** -> AI Confidence: **99.32%**
912. **`src/tests/JIT/SIMD/VectorRelOp.cs`** -> AI Confidence: **99.32%**
913. **`src/tests/JIT/SIMD/VectorSet.cs`** -> AI Confidence: **99.32%**
914. **`src/tests/JIT/jit64/hfa/main/testA/hfa_testA.cs`** -> AI Confidence: **99.32%**
915. **`src/tests/JIT/jit64/hfa/main/testB/hfa_testB.cs`** -> AI Confidence: **99.32%**
916. **`src/tests/JIT/jit64/hfa/main/testC/hfa_testC.cs`** -> AI Confidence: **99.32%**
917. **`src/tests/JIT/jit64/hfa/main/testG/hfa_testG.cs`** -> AI Confidence: **99.32%**
918. **`src/tests/JIT/jit64/opt/rngchk/RngchkStress2.cs`** -> AI Confidence: **99.32%**
919. **`src/tests/JIT/opt/Compares/conditionalIncrements.cs`** -> AI Confidence: **99.32%**
920. **`src/tests/JIT/opt/Compares/conditionalSimpleOps.cs`** -> AI Confidence: **99.32%**
921. **`src/tests/Loader/binding/assemblies/assemblyversion/embedstringversions.cs`** -> AI Confidence: **99.32%**
922. **`src/tests/baseservices/compilerservices/dynamicobjectproperties/dev10_535767.cs`** -> AI Confidence: **99.32%**
923. **`src/tests/baseservices/exceptions/regressions/V1/SEH/VJ/NestedEx1.cs`** -> AI Confidence: **99.32%**
924. **`src/tests/baseservices/exceptions/regressions/V1/SEH/VJ/NestedEx2.cs`** -> AI Confidence: **99.32%**
925. **`src/tests/baseservices/exceptions/unittests/EHPatternTests.cs`** -> AI Confidence: **99.32%**
926. **`src/tests/baseservices/exceptions/unittests/StrSwitchFinally.cs`** -> AI Confidence: **99.32%**
927. **`src/tools/illink/test/Mono.Linker.Tests.Cases/DataFlow/ExceptionalDataFlow.cs`** -> AI Confidence: **99.32%**
928. **`src/native/libs/System.Native/pal_autoreleasepool.m`** -> AI Confidence: **99.32%**
929. **`src/native/libs/System.Native/pal_iossupportversion.m`** -> AI Confidence: **99.32%**
930. **`eng/common/SetupNugetSources.sh`** -> AI Confidence: **99.31%**
931. **`.github/skills/ci-pipeline-monitor/scripts/extract_failed_tests.py`** -> AI Confidence: **99.31%**
932. **`.github/skills/ci-pipeline-monitor/scripts/fetch_helix_logs.py`** -> AI Confidence: **99.31%**
933. **`eng/common/cross/install-debs.py`** -> AI Confidence: **99.31%**
934. **`src/coreclr/scripts/genEtwProvider.py`** -> AI Confidence: **99.31%**
935. **`src/coreclr/scripts/genEventingTests.py`** -> AI Confidence: **99.31%**
936. **`src/coreclr/scripts/jitrollingbuild.py`** -> AI Confidence: **99.31%**
937. **`src/coreclr/scripts/superpmi_aspnet.py`** -> AI Confidence: **99.31%**
938. **`src/coreclr/scripts/superpmi_aspnet2.py`** -> AI Confidence: **99.31%**
939. **`src/coreclr/scripts/superpmi_benchmarks.py`** -> AI Confidence: **99.31%**
940. **`src/coreclr/scripts/superpmi_diffs.py`** -> AI Confidence: **99.31%**
941. **`src/coreclr/scripts/superpmi_diffs_setup.py`** -> AI Confidence: **99.31%**
942. **`src/tests/run.py`** -> AI Confidence: **99.31%**
943. **`src/libraries/Common/tests/System/Net/EnterpriseTests/setup/apacheweb/mod_auth_ntlm_winbind/mod_auth_ntlm_winbind.c`** -> AI Confidence: **99.31%**
944. **`src/mono/mono/component/debugger-engine.c`** -> AI Confidence: **99.31%**
945. **`src/mono/mono/component/debugger-networking.c`** -> AI Confidence: **99.31%**
946. **`src/mono/mono/component/debugger-state-machine.c`** -> AI Confidence: **99.31%**
947. **`src/mono/mono/component/hot_reload.c`** -> AI Confidence: **99.31%**
948. **`src/mono/mono/component/marshal-ilgen.c`** -> AI Confidence: **99.31%**
949. **`src/mono/mono/component/mini-wasm-debugger.c`** -> AI Confidence: **99.31%**
950. **`src/mono/mono/eglib/gfile-win32.c`** -> AI Confidence: **99.31%**
951. **`src/mono/mono/eglib/giconv.c`** -> AI Confidence: **99.31%**
952. **`src/mono/mono/eglib/gmodule-aix.c`** -> AI Confidence: **99.31%**
953. **`src/mono/mono/eglib/gstr.c`** -> AI Confidence: **99.31%**
954. **`src/mono/mono/eglib/test/file.c`** -> AI Confidence: **99.31%**
955. **`src/mono/mono/eglib/test/path.c`** -> AI Confidence: **99.31%**
956. **`src/mono/mono/eventpipe/ep-rt-mono-profiler-provider.c`** -> AI Confidence: **99.31%**
957. **`src/mono/mono/eventpipe/ep-rt-mono-runtime-provider.c`** -> AI Confidence: **99.31%**
958. **`src/mono/mono/metadata/appdomain.c`** -> AI Confidence: **99.31%**
959. **`src/mono/mono/metadata/assembly-load-context.c`** -> AI Confidence: **99.31%**
960. **`src/mono/mono/metadata/class-accessors.c`** -> AI Confidence: **99.31%**
961. **`src/mono/mono/metadata/components.c`** -> AI Confidence: **99.31%**
962. **`src/mono/mono/metadata/debug-mono-ppdb.c`** -> AI Confidence: **99.31%**
963. **`src/mono/mono/metadata/dynamic-image.c`** -> AI Confidence: **99.31%**
964. **`src/mono/mono/metadata/exception.c`** -> AI Confidence: **99.31%**
965. **`src/mono/mono/metadata/gc.c`** -> AI Confidence: **99.31%**
966. **`src/mono/mono/metadata/handle.c`** -> AI Confidence: **99.31%**
967. **`src/mono/mono/metadata/image.c`** -> AI Confidence: **99.31%**
968. **`src/mono/mono/metadata/jit-info.c`** -> AI Confidence: **99.31%**
969. **`src/mono/mono/metadata/loader.c`** -> AI Confidence: **99.31%**
970. **`src/mono/mono/metadata/marshal-shared.c`** -> AI Confidence: **99.31%**
971. **`src/mono/mono/metadata/memory-manager.c`** -> AI Confidence: **99.31%**
972. **`src/mono/mono/metadata/mempool.c`** -> AI Confidence: **99.31%**
973. **`src/mono/mono/metadata/metadata.c`** -> AI Confidence: **99.31%**
974. **`src/mono/mono/metadata/method-builder-ilgen.c`** -> AI Confidence: **99.31%**
975. **`src/mono/mono/metadata/monitor.c`** -> AI Confidence: **99.31%**
976. **`src/mono/mono/metadata/mono-conc-hash.c`** -> AI Confidence: **99.31%**
977. **`src/mono/mono/metadata/mono-debug.c`** -> AI Confidence: **99.31%**
978. **`src/mono/mono/metadata/mono-hash.c`** -> AI Confidence: **99.31%**
979. **`src/mono/mono/metadata/object.c`** -> AI Confidence: **99.31%**
980. **`src/mono/mono/metadata/profiler.c`** -> AI Confidence: **99.31%**
981. **`src/mono/mono/metadata/sgen-bridge.c`** -> AI Confidence: **99.31%**
982. **`src/mono/mono/metadata/sgen-mono.c`** -> AI Confidence: **99.31%**
983. **`src/mono/mono/metadata/sgen-stw.c`** -> AI Confidence: **99.31%**
984. **`src/mono/mono/metadata/sgen-tarjan-bridge.c`** -> AI Confidence: **99.31%**
985. **`src/mono/mono/metadata/threads.c`** -> AI Confidence: **99.31%**
986. **`src/mono/mono/metadata/verify.c`** -> AI Confidence: **99.31%**
987. **`src/mono/mono/metadata/w32handle.c`** -> AI Confidence: **99.31%**
988. **`src/mono/mono/mini/aot-runtime.c`** -> AI Confidence: **99.31%**
989. **`src/mono/mono/mini/cfgdump.c`** -> AI Confidence: **99.31%**
990. **`src/mono/mono/mini/exceptions-arm.c`** -> AI Confidence: **99.31%**
991. **`src/mono/mono/mini/exceptions-arm64.c`** -> AI Confidence: **99.31%**
992. **`src/mono/mono/mini/exceptions-ppc.c`** -> AI Confidence: **99.31%**
993. **`src/mono/mono/mini/exceptions-s390x.c`** -> AI Confidence: **99.31%**
994. **`src/mono/mono/mini/image-writer.c`** -> AI Confidence: **99.31%**
995. **`src/mono/mono/mini/interp/interp-pgo.c`** -> AI Confidence: **99.31%**
996. **`src/mono/mono/mini/interp/jiterpreter.c`** -> AI Confidence: **99.31%**
997. **`src/mono/mono/mini/interp/whitebox.c`** -> AI Confidence: **99.31%**
998. **`src/mono/mono/mini/jit-icalls.c`** -> AI Confidence: **99.31%**
999. **`src/mono/mono/mini/mini-amd64-gsharedvt.c`** -> AI Confidence: **99.31%**
1000. **`src/mono/mono/mini/mini-darwin.c`** -> AI Confidence: **99.31%**
1001. **`src/mono/mono/mini/mini-posix.c`** -> AI Confidence: **99.31%**
1002. **`src/mono/mono/mini/mini-profiler.c`** -> AI Confidence: **99.31%**
1003. **`src/mono/mono/mini/mini-wasm.c`** -> AI Confidence: **99.31%**
1004. **`src/mono/mono/mini/mini-windows-dlldac.c`** -> AI Confidence: **99.31%**
1005. **`src/mono/mono/mini/mini-windows.c`** -> AI Confidence: **99.31%**
1006. **`src/mono/mono/mini/tramp-arm.c`** -> AI Confidence: **99.31%**
1007. **`src/mono/mono/profiler/browser.c`** -> AI Confidence: **99.31%**
1008. **`src/mono/mono/profiler/coverage.c`** -> AI Confidence: **99.31%**
1009. **`src/mono/mono/profiler/helper.c`** -> AI Confidence: **99.31%**
1010. **`src/mono/mono/profiler/log.c`** -> AI Confidence: **99.31%**
1011. **`src/mono/mono/profiler/vtune.c`** -> AI Confidence: **99.31%**
1012. **`src/mono/mono/sgen/sgen-alloc.c`** -> AI Confidence: **99.31%**
1013. **`src/mono/mono/sgen/sgen-cardtable.c`** -> AI Confidence: **99.31%**
1014. **`src/mono/mono/sgen/sgen-debug.c`** -> AI Confidence: **99.31%**
1015. **`src/mono/mono/sgen/sgen-descriptor.c`** -> AI Confidence: **99.31%**
1016. **`src/mono/mono/sgen/sgen-fin-weak-hash.c`** -> AI Confidence: **99.31%**
1017. **`src/mono/mono/sgen/sgen-internal.c`** -> AI Confidence: **99.31%**
1018. **`src/mono/mono/sgen/sgen-los.c`** -> AI Confidence: **99.31%**
1019. **`src/mono/mono/sgen/sgen-marksweep.c`** -> AI Confidence: **99.31%**
1020. **`src/mono/mono/sgen/sgen-memory-governor.c`** -> AI Confidence: **99.31%**
1021. **`src/mono/mono/sgen/sgen-protocol.c`** -> AI Confidence: **99.31%**
1022. **`src/mono/mono/tests/metadata-verifier/gen-md-tests.c`** -> AI Confidence: **99.31%**
1023. **`src/mono/mono/unit-tests/test-conc-hashtable.c`** -> AI Confidence: **99.31%**
1024. **`src/mono/mono/unit-tests/test-mono-linked-list-set.c`** -> AI Confidence: **99.31%**
1025. **`src/mono/mono/utils/checked-build.c`** -> AI Confidence: **99.31%**
1026. **`src/mono/mono/utils/dlmalloc.c`** -> AI Confidence: **99.31%**
1027. **`src/mono/mono/utils/hazard-pointer.c`** -> AI Confidence: **99.31%**
1028. **`src/mono/mono/utils/memfuncs.c`** -> AI Confidence: **99.31%**
1029. **`src/mono/mono/utils/mono-cgroup.c`** -> AI Confidence: **99.31%**
1030. **`src/mono/mono/utils/mono-codeman.c`** -> AI Confidence: **99.31%**
1031. **`src/mono/mono/utils/mono-context.c`** -> AI Confidence: **99.31%**
1032. **`src/mono/mono/utils/mono-dl-posix.c`** -> AI Confidence: **99.31%**
1033. **`src/mono/mono/utils/mono-dl-windows.c`** -> AI Confidence: **99.31%**
1034. **`src/mono/mono/utils/mono-error.c`** -> AI Confidence: **99.31%**
1035. **`src/mono/mono/utils/mono-log-common.c`** -> AI Confidence: **99.31%**
1036. **`src/mono/mono/utils/mono-logger.c`** -> AI Confidence: **99.31%**
1037. **`src/mono/mono/utils/mono-mmap-windows.c`** -> AI Confidence: **99.31%**
1038. **`src/mono/mono/utils/mono-mmap.c`** -> AI Confidence: **99.31%**
1039. **`src/mono/mono/utils/mono-proclib.c`** -> AI Confidence: **99.31%**
1040. **`src/mono/mono/utils/mono-threads-android.c`** -> AI Confidence: **99.31%**
1041. **`src/mono/mono/utils/mono-threads-coop.c`** -> AI Confidence: **99.31%**
1042. **`src/mono/mono/utils/mono-threads-mach.c`** -> AI Confidence: **99.31%**
1043. **`src/mono/mono/utils/mono-threads-posix.c`** -> AI Confidence: **99.31%**
1044. **`src/mono/mono/utils/mono-threads.c`** -> AI Confidence: **99.31%**
1045. **`src/mono/mono/utils/mono-time.c`** -> AI Confidence: **99.31%**
1046. **`src/native/containers/dn-simdhash-test.c`** -> AI Confidence: **99.31%**
1047. **`src/native/containers/simdhash-benchmark/benchmark.c`** -> AI Confidence: **99.31%**
1048. **`src/native/eventpipe/ds-ipc-pal-socket.c`** -> AI Confidence: **99.31%**
1049. **`src/native/eventpipe/ds-ipc.c`** -> AI Confidence: **99.31%**
1050. **`src/native/eventpipe/ep-buffer-manager.c`** -> AI Confidence: **99.31%**
1051. **`src/native/eventpipe/ep-buffer.c`** -> AI Confidence: **99.31%**
1052. **`src/native/eventpipe/ep-event-instance.c`** -> AI Confidence: **99.31%**
1053. **`src/native/eventpipe/ep-event-source.c`** -> AI Confidence: **99.31%**
1054. **`src/native/external/brotli/c/common/shared_dictionary.c`** -> AI Confidence: **99.31%**
1055. **`src/native/external/brotli/c/enc/backward_references.c`** -> AI Confidence: **99.31%**
1056. **`src/native/external/brotli/c/enc/block_splitter.c`** -> AI Confidence: **99.31%**
1057. **`src/native/external/brotli/c/enc/cluster.c`** -> AI Confidence: **99.31%**
1058. **`src/native/external/brotli/c/enc/encode.c`** -> AI Confidence: **99.31%**
1059. **`src/native/external/brotli/c/enc/encoder_dict.c`** -> AI Confidence: **99.31%**
1060. **`src/native/external/libunwind/src/coredump/ucd_file_table.c`** -> AI Confidence: **99.31%**
1061. **`src/native/external/libunwind/src/dwarf/Gfind_proc_info-lsb.c`** -> AI Confidence: **99.31%**
1062. **`src/native/external/libunwind/src/ia64/Gtables.c`** -> AI Confidence: **99.31%**
1063. **`src/native/external/libunwind/src/nto/unw_nto_create.c`** -> AI Confidence: **99.31%**
1064. **`src/native/external/libunwind/src/os-freebsd.c`** -> AI Confidence: **99.31%**
1065. **`src/native/external/libunwind/src/os-linux.c`** -> AI Confidence: **99.31%**
1066. **`src/native/external/libunwind/src/os-qnx.c`** -> AI Confidence: **99.31%**
1067. **`src/native/external/libunwind/tests/Gperf-simple.c`** -> AI Confidence: **99.31%**
1068. **`src/native/external/libunwind/tests/Gperf-trace.c`** -> AI Confidence: **99.31%**
1069. **`src/native/external/libunwind/tests/Gtest-dyn1.c`** -> AI Confidence: **99.31%**
1070. **`src/native/external/libunwind/tests/Gtest-exc.c`** -> AI Confidence: **99.31%**
1071. **`src/native/external/libunwind/tests/Ltest-init-local-signal.c`** -> AI Confidence: **99.31%**
1072. **`src/native/external/libunwind/tests/Ltest-mem-validate.c`** -> AI Confidence: **99.31%**
1073. **`src/native/external/libunwind/tests/test-coredump-unwind.c`** -> AI Confidence: **99.31%**
1074. **`src/native/external/libunwind/tests/test-mem.c`** -> AI Confidence: **99.31%**
1075. **`src/native/external/libunwind/tests/test-ptrace-misc.c`** -> AI Confidence: **99.31%**
1076. **`src/native/external/libunwind/tests/x64-unwind-badjmp-signal-frame.c`** -> AI Confidence: **99.31%**
1077. **`src/native/external/zlib-ng/arch/arm/arm_features.c`** -> AI Confidence: **99.31%**
1078. **`src/native/external/zlib-ng/arch/riscv/riscv_features.c`** -> AI Confidence: **99.31%**
1079. **`src/native/external/zlib-ng/arch/x86/adler32_avx512_vnni.c`** -> AI Confidence: **99.31%**
1080. **`src/native/external/zlib-ng/arch/x86/compare256_avx2.c`** -> AI Confidence: **99.31%**
1081. **`src/native/external/zstd/lib/common/fse_decompress.c`** -> AI Confidence: **99.31%**
1082. **`src/native/external/zstd/lib/compress/huf_compress.c`** -> AI Confidence: **99.31%**
1083. **`src/native/external/zstd/lib/compress/zstd_compress.c`** -> AI Confidence: **99.31%**
1084. **`src/native/external/zstd/lib/compress/zstdmt_compress.c`** -> AI Confidence: **99.31%**
1085. **`src/native/external/zstd/lib/decompress/huf_decompress.c`** -> AI Confidence: **99.31%**
1086. **`src/native/external/zstd/lib/decompress/zstd_decompress.c`** -> AI Confidence: **99.31%**
1087. **`src/native/external/zstd/lib/decompress/zstd_decompress_block.c`** -> AI Confidence: **99.31%**
1088. **`src/native/external/zstd/lib/dictBuilder/cover.c`** -> AI Confidence: **99.31%**
1089. **`src/native/external/zstd/lib/dictBuilder/fastcover.c`** -> AI Confidence: **99.31%**
1090. **`src/native/external/zstd/lib/dictBuilder/zdict.c`** -> AI Confidence: **99.31%**
1091. **`src/native/external/zstd/lib/legacy/zstd_v01.c`** -> AI Confidence: **99.31%**
1092. **`src/native/external/zstd/lib/legacy/zstd_v02.c`** -> AI Confidence: **99.31%**
1093. **`src/native/external/zstd/lib/legacy/zstd_v03.c`** -> AI Confidence: **99.31%**
1094. **`src/native/external/zstd/lib/legacy/zstd_v05.c`** -> AI Confidence: **99.31%**
1095. **`src/native/external/zstd/lib/legacy/zstd_v06.c`** -> AI Confidence: **99.31%**
1096. **`src/native/libs/System.Globalization.Native/pal_calendarData.c`** -> AI Confidence: **99.31%**
1097. **`src/native/libs/System.Globalization.Native/pal_collation.c`** -> AI Confidence: **99.31%**
1098. **`src/native/libs/System.Globalization.Native/pal_icushim.c`** -> AI Confidence: **99.31%**
1099. **`src/native/libs/System.Globalization.Native/pal_icushim_static.c`** -> AI Confidence: **99.31%**
1100. **`src/native/libs/System.Globalization.Native/pal_locale.c`** -> AI Confidence: **99.31%**
1101. **`src/native/libs/System.IO.Compression.Native/entrypoints.c`** -> AI Confidence: **99.31%**
1102. **`src/native/libs/System.IO.Ports.Native/pal_termios.c`** -> AI Confidence: **99.31%**
1103. **`src/native/libs/System.Native/pal_datetime_time_zone_data.c`** -> AI Confidence: **99.31%**
1104. **`src/native/libs/System.Native/pal_interfaceaddresses.c`** -> AI Confidence: **99.31%**
1105. **`src/native/libs/System.Native/pal_io.c`** -> AI Confidence: **99.31%**
1106. **`src/native/libs/System.Native/pal_maphardwaretype.c`** -> AI Confidence: **99.31%**
1107. **`src/native/libs/System.Native/pal_mount.c`** -> AI Confidence: **99.31%**
1108. **`src/native/libs/System.Native/pal_networkchange.c`** -> AI Confidence: **99.31%**
1109. **`src/native/libs/System.Native/pal_networking.c`** -> AI Confidence: **99.31%**
1110. **`src/native/libs/System.Native/pal_process.c`** -> AI Confidence: **99.31%**
1111. **`src/native/libs/System.Native/pal_time.c`** -> AI Confidence: **99.31%**
1112. **`src/native/libs/System.Native/pal_uid.c`** -> AI Confidence: **99.31%**
1113. **`src/native/libs/System.Net.Security.Native/pal_gssapi.c`** -> AI Confidence: **99.31%**
1114. **`src/native/libs/System.Security.Cryptography.Native.Android/pal_x509.c`** -> AI Confidence: **99.31%**
1115. **`src/native/libs/System.Security.Cryptography.Native.Android/pal_x509store.c`** -> AI Confidence: **99.31%**
1116. **`src/native/libs/System.Security.Cryptography.Native/openssl.c`** -> AI Confidence: **99.31%**
1117. **`src/native/libs/System.Security.Cryptography.Native/pal_ssl.c`** -> AI Confidence: **99.31%**
1118. **`src/native/libs/System.Security.Cryptography.Native/pal_x509.c`** -> AI Confidence: **99.31%**
1119. **`src/native/minipal/cpufeatures.c`** -> AI Confidence: **99.31%**
1120. **`src/native/minipal/log.c`** -> AI Confidence: **99.31%**
1121. **`src/native/minipal/memorybarrierprocesswide.c`** -> AI Confidence: **99.31%**
1122. **`src/tasks/LibraryBuilder/Templates/autoinit.c`** -> AI Confidence: **99.31%**
1123. **`src/tests/Interop/MonoAPI/Native/mono-embedding-api-test/mono-embedding-api-test.c`** -> AI Confidence: **99.31%**
1124. **`src/coreclr/dlls/mscoree/exports.cpp`** -> AI Confidence: **99.31%**
1125. **`src/coreclr/gc/sample/gcenv.h`** -> AI Confidence: **99.31%**
1126. **`src/coreclr/gc/unix/cgroup.cpp`** -> AI Confidence: **99.31%**
1127. **`src/coreclr/gc/unix/events.cpp`** -> AI Confidence: **99.31%**
1128. **`src/coreclr/gc/unix/gcenv.unix.cpp`** -> AI Confidence: **99.31%**
1129. **`src/coreclr/gc/unix/numasupport.cpp`** -> AI Confidence: **99.31%**
1130. **`src/coreclr/gc/windows/gcenv.windows.cpp`** -> AI Confidence: **99.31%**
1131. **`src/coreclr/hosts/corerun/corerun.cpp`** -> AI Confidence: **99.31%**
1132. **`src/coreclr/interpreter/eeinterp.cpp`** -> AI Confidence: **99.31%**
1133. **`src/coreclr/jit/simdcodegenxarch.cpp`** -> AI Confidence: **99.31%**
1134. **`src/coreclr/md/enc/stgtiggerstorage.cpp`** -> AI Confidence: **99.31%**
1135. **`src/coreclr/md/runtime/mdinternaldisp.cpp`** -> AI Confidence: **99.31%**
1136. **`src/coreclr/md/runtime/stgpool.cpp`** -> AI Confidence: **99.31%**
1137. **`src/coreclr/minipal/Unix/doublemapping.cpp`** -> AI Confidence: **99.31%**
1138. **`src/coreclr/nativeaot/Runtime/AsmOffsetsVerify.cpp`** -> AI Confidence: **99.31%**
1139. **`src/coreclr/nativeaot/Runtime/Crst.cpp`** -> AI Confidence: **99.31%**
1140. **`src/coreclr/nativeaot/Runtime/FinalizerHelpers.cpp`** -> AI Confidence: **99.31%**
1141. **`src/coreclr/nativeaot/Runtime/GcEnum.cpp`** -> AI Confidence: **99.31%**
1142. **`src/coreclr/nativeaot/Runtime/GcStressControl.cpp`** -> AI Confidence: **99.31%**
1143. **`src/coreclr/nativeaot/Runtime/RestrictedCallouts.cpp`** -> AI Confidence: **99.31%**
1144. **`src/coreclr/nativeaot/Runtime/RhConfig.cpp`** -> AI Confidence: **99.31%**
1145. **`src/coreclr/nativeaot/Runtime/StackFrameIterator.cpp`** -> AI Confidence: **99.31%**
1146. **`src/coreclr/nativeaot/Runtime/clrgc.enabled.cpp`** -> AI Confidence: **99.31%**
1147. **`src/coreclr/nativeaot/Runtime/eventpipe/ds-rt-aot.cpp`** -> AI Confidence: **99.31%**
1148. **`src/coreclr/nativeaot/Runtime/eventpipe/ds-rt-aot.h`** -> AI Confidence: **99.31%**
1149. **`src/coreclr/nativeaot/Runtime/eventpipeinternal.cpp`** -> AI Confidence: **99.31%**
1150. **`src/coreclr/nativeaot/Runtime/eventtrace_bulktype.cpp`** -> AI Confidence: **99.31%**
1151. **`src/coreclr/nativeaot/Runtime/eventtrace_gcheap.cpp`** -> AI Confidence: **99.31%**
1152. **`src/coreclr/nativeaot/Runtime/startup.cpp`** -> AI Confidence: **99.31%**
1153. **`src/coreclr/nativeaot/Runtime/stressLog.cpp`** -> AI Confidence: **99.31%**
1154. **`src/coreclr/nativeaot/Runtime/thread.cpp`** -> AI Confidence: **99.31%**
1155. **`src/coreclr/nativeaot/Runtime/threadstore.cpp`** -> AI Confidence: **99.31%**
1156. **`src/coreclr/nativeaot/Runtime/unix/PalUnix.cpp`** -> AI Confidence: **99.31%**
1157. **`src/coreclr/nativeaot/Runtime/unix/UnwindHelpers.cpp`** -> AI Confidence: **99.31%**
1158. **`src/coreclr/nativeaot/Runtime/windows/PalCommon.cpp`** -> AI Confidence: **99.31%**
1159. **`src/coreclr/pal/src/eventprovider/lttngprovider/eventproviderhelpers.cpp`** -> AI Confidence: **99.31%**
1160. **`src/coreclr/pal/src/exception/machexception.cpp`** -> AI Confidence: **99.31%**
1161. **`src/coreclr/pal/src/exception/remote-unwind.cpp`** -> AI Confidence: **99.31%**
1162. **`src/coreclr/pal/src/init/pal.cpp`** -> AI Confidence: **99.31%**
1163. **`src/coreclr/pal/src/init/sxs.cpp`** -> AI Confidence: **99.31%**
1164. **`src/coreclr/pal/src/map/virtual.cpp`** -> AI Confidence: **99.31%**
1165. **`src/coreclr/pal/src/misc/perfjitdump.cpp`** -> AI Confidence: **99.31%**
1166. **`src/coreclr/pal/src/misc/time.cpp`** -> AI Confidence: **99.31%**
1167. **`src/coreclr/pal/src/misc/tracepointprovider.cpp`** -> AI Confidence: **99.31%**
1168. **`src/coreclr/pal/src/misc/utils.cpp`** -> AI Confidence: **99.31%**
1169. **`src/coreclr/tools/superpmi/mcs/verbasmdump.cpp`** -> AI Confidence: **99.31%**
1170. **`src/coreclr/tools/superpmi/mcs/verbfracture.cpp`** -> AI Confidence: **99.31%**
1171. **`src/coreclr/tools/superpmi/mcs/verbstrip.cpp`** -> AI Confidence: **99.31%**
1172. **`src/coreclr/tools/superpmi/superpmi-shared/methodcontextreader.cpp`** -> AI Confidence: **99.31%**
1173. **`src/coreclr/tools/superpmi/superpmi-shared/spmiutil.cpp`** -> AI Confidence: **99.31%**
1174. **`src/coreclr/tools/superpmi/superpmi-shim-collector/superpmi-shim-collector.cpp`** -> AI Confidence: **99.31%**
1175. **`src/coreclr/utilcode/cycletimer.cpp`** -> AI Confidence: **99.31%**
1176. **`src/coreclr/utilcode/debug.cpp`** -> AI Confidence: **99.31%**
1177. **`src/coreclr/utilcode/stresslog.cpp`** -> AI Confidence: **99.31%**
1178. **`src/coreclr/vm/amd64/cgenamd64.cpp`** -> AI Confidence: **99.31%**
1179. **`src/coreclr/vm/appdomain.cpp`** -> AI Confidence: **99.31%**
1180. **`src/coreclr/vm/arm/stubs.cpp`** -> AI Confidence: **99.31%**
1181. **`src/coreclr/vm/assemblynative.cpp`** -> AI Confidence: **99.31%**
1182. **`src/coreclr/vm/ceeload.cpp`** -> AI Confidence: **99.31%**
1183. **`src/coreclr/vm/ceemain.cpp`** -> AI Confidence: **99.31%**
1184. **`src/coreclr/vm/clrex.cpp`** -> AI Confidence: **99.31%**
1185. **`src/coreclr/vm/clrtocomcall.cpp`** -> AI Confidence: **99.31%**
1186. **`src/coreclr/vm/codeman.cpp`** -> AI Confidence: **99.31%**
1187. **`src/coreclr/vm/codeversion.cpp`** -> AI Confidence: **99.31%**
1188. **`src/coreclr/vm/comdynamic.cpp`** -> AI Confidence: **99.31%**
1189. **`src/coreclr/vm/comsynchronizable.cpp`** -> AI Confidence: **99.31%**
1190. **`src/coreclr/vm/comutilnative.cpp`** -> AI Confidence: **99.31%**
1191. **`src/coreclr/vm/corhost.cpp`** -> AI Confidence: **99.31%**
1192. **`src/coreclr/vm/dllimportcallback.cpp`** -> AI Confidence: **99.31%**
1193. **`src/coreclr/vm/dwreport.cpp`** -> AI Confidence: **99.31%**
1194. **`src/coreclr/vm/dynamicmethod.cpp`** -> AI Confidence: **99.31%**
1195. **`src/coreclr/vm/encee.cpp`** -> AI Confidence: **99.31%**
1196. **`src/coreclr/vm/eventtrace_gcheap.cpp`** -> AI Confidence: **99.31%**
1197. **`src/coreclr/vm/fcall.cpp`** -> AI Confidence: **99.31%**
1198. **`src/coreclr/vm/fieldmarshaler.cpp`** -> AI Confidence: **99.31%**
1199. **`src/coreclr/vm/frames.cpp`** -> AI Confidence: **99.31%**
1200. **`src/coreclr/vm/gcheaputilities.cpp`** -> AI Confidence: **99.31%**
1201. **`src/coreclr/vm/i386/cgenx86.cpp`** -> AI Confidence: **99.31%**
1202. **`src/coreclr/vm/i386/excepx86.cpp`** -> AI Confidence: **99.31%**
1203. **`src/coreclr/vm/i386/jitinterfacex86.cpp`** -> AI Confidence: **99.31%**
1204. **`src/coreclr/vm/ilmarshalers.cpp`** -> AI Confidence: **99.31%**
1205. **`src/coreclr/vm/instmethhash.cpp`** -> AI Confidence: **99.31%**
1206. **`src/coreclr/vm/interoputil.cpp`** -> AI Confidence: **99.31%**
1207. **`src/coreclr/vm/interpexec.cpp`** -> AI Confidence: **99.31%**
1208. **`src/coreclr/vm/jithelpers.cpp`** -> AI Confidence: **99.31%**
1209. **`src/coreclr/vm/loaderallocator.cpp`** -> AI Confidence: **99.31%**
1210. **`src/coreclr/vm/loongarch64/stubs.cpp`** -> AI Confidence: **99.31%**
1211. **`src/coreclr/vm/marshalnative.cpp`** -> AI Confidence: **99.31%**
1212. **`src/coreclr/vm/method.cpp`** -> AI Confidence: **99.31%**
1213. **`src/coreclr/vm/multicorejit.cpp`** -> AI Confidence: **99.31%**
1214. **`src/coreclr/vm/multicorejitplayer.cpp`** -> AI Confidence: **99.31%**
1215. **`src/coreclr/vm/object.cpp`** -> AI Confidence: **99.31%**
1216. **`src/coreclr/vm/peassembly.cpp`** -> AI Confidence: **99.31%**
1217. **`src/coreclr/vm/proftoeeinterfaceimpl.cpp`** -> AI Confidence: **99.31%**
1218. **`src/coreclr/vm/readytoruninfo.cpp`** -> AI Confidence: **99.31%**
1219. **`src/coreclr/vm/rejit.cpp`** -> AI Confidence: **99.31%**
1220. **`src/coreclr/vm/riscv64/stubs.cpp`** -> AI Confidence: **99.31%**
1221. **`src/coreclr/vm/runtimehandles.cpp`** -> AI Confidence: **99.31%**
1222. **`src/coreclr/vm/stdinterfaces.cpp`** -> AI Confidence: **99.31%**
1223. **`src/coreclr/vm/stubgen.cpp`** -> AI Confidence: **99.31%**
1224. **`src/coreclr/vm/stubmgr.cpp`** -> AI Confidence: **99.31%**
1225. **`src/coreclr/vm/syncblk.cpp`** -> AI Confidence: **99.31%**
1226. **`src/coreclr/vm/tailcallhelp.cpp`** -> AI Confidence: **99.31%**
1227. **`src/coreclr/vm/threads.cpp`** -> AI Confidence: **99.31%**
1228. **`src/coreclr/vm/typehandle.cpp`** -> AI Confidence: **99.31%**
1229. **`src/coreclr/vm/typehash.cpp`** -> AI Confidence: **99.31%**
1230. **`src/coreclr/vm/virtualcallstub.cpp`** -> AI Confidence: **99.31%**
1231. **`src/coreclr/vm/writebarriermanager.cpp`** -> AI Confidence: **99.31%**
1232. **`src/mono/mono/metadata/reflection-cache.h`** -> AI Confidence: **99.31%**
1233. **`src/native/corehost/apphost/apphost.windows.cpp`** -> AI Confidence: **99.31%**
1234. **`src/native/corehost/comhost/comhost.cpp`** -> AI Confidence: **99.31%**
1235. **`src/native/corehost/corehost.cpp`** -> AI Confidence: **99.31%**
1236. **`src/native/corehost/fxr/command_line.cpp`** -> AI Confidence: **99.31%**
1237. **`src/native/corehost/fxr/fx_muxer.cpp`** -> AI Confidence: **99.31%**
1238. **`src/native/corehost/fxr/hostfxr.cpp`** -> AI Confidence: **99.31%**
1239. **`src/native/corehost/hostmisc/pal.unix.cpp`** -> AI Confidence: **99.31%**
1240. **`src/native/corehost/hostpolicy/deps_format.cpp`** -> AI Confidence: **99.31%**
1241. **`src/native/corehost/hostpolicy/hostpolicy.cpp`** -> AI Confidence: **99.31%**
1242. **`src/native/corehost/hostpolicy/hostpolicy_context.cpp`** -> AI Confidence: **99.31%**
1243. **`src/native/corehost/ijwhost/ijwhost.cpp`** -> AI Confidence: **99.31%**
1244. **`src/native/corehost/ijwhost/ijwthunk.cpp`** -> AI Confidence: **99.31%**
1245. **`src/native/corehost/runtime_config.cpp`** -> AI Confidence: **99.31%**
1246. **`src/native/corehost/test/nativehost/host_context_test.cpp`** -> AI Confidence: **99.31%**
1247. **`src/native/external/zstd/lib/legacy/zstd_legacy.h`** -> AI Confidence: **99.31%**
1248. **`src/native/watchdog/watchdog.cpp`** -> AI Confidence: **99.31%**
1249. **`src/tests/Interop/COM/RuntimeAsync/RuntimeAsyncNative.cpp`** -> AI Confidence: **99.31%**
1250. **`src/tests/Interop/IJW/NativeVarargs/IjwNativeVarargs.cpp`** -> AI Confidence: **99.31%**
1251. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128B.cpp`** -> AI Confidence: **99.31%**
1252. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128C.cpp`** -> AI Confidence: **99.31%**
1253. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128D.cpp`** -> AI Confidence: **99.31%**
1254. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128F.cpp`** -> AI Confidence: **99.31%**
1255. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128L.cpp`** -> AI Confidence: **99.31%**
1256. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128U.cpp`** -> AI Confidence: **99.31%**
1257. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64B.cpp`** -> AI Confidence: **99.31%**
1258. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64C.cpp`** -> AI Confidence: **99.31%**
1259. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64D.cpp`** -> AI Confidence: **99.31%**
1260. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64F.cpp`** -> AI Confidence: **99.31%**
1261. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64L.cpp`** -> AI Confidence: **99.31%**
1262. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64U.cpp`** -> AI Confidence: **99.31%**
1263. **`src/coreclr/System.Private.CoreLib/src/Internal/Runtime/InteropServices/ComActivator.cs`** -> AI Confidence: **99.31%**
1264. **`src/coreclr/System.Private.CoreLib/src/System/Array.CoreCLR.cs`** -> AI Confidence: **99.31%**
1265. **`src/coreclr/System.Private.CoreLib/src/System/Exception.CoreCLR.cs`** -> AI Confidence: **99.31%**
1266. **`src/coreclr/System.Private.CoreLib/src/System/GC.CoreCLR.cs`** -> AI Confidence: **99.31%**
1267. **`src/coreclr/System.Private.CoreLib/src/System/MulticastDelegate.CoreCLR.cs`** -> AI Confidence: **99.31%**
1268. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/DynamicMethod.CoreCLR.cs`** -> AI Confidence: **99.31%**
1269. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/RuntimeCustomAttributeData.cs`** -> AI Confidence: **99.31%**
1270. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/RuntimeMethodInfo.CoreCLR.cs`** -> AI Confidence: **99.31%**
1271. **`src/coreclr/System.Private.CoreLib/src/System/Runtime/InteropServices/Marshal.CoreCLR.cs`** -> AI Confidence: **99.31%**
1272. **`src/coreclr/System.Private.CoreLib/src/System/RuntimeType.CoreCLR.cs`** -> AI Confidence: **99.31%**
1273. **`src/coreclr/System.Private.CoreLib/src/System/Threading/Thread.CoreCLR.cs`** -> AI Confidence: **99.31%**
1274. **`src/coreclr/System.Private.CoreLib/src/System/Variant.cs`** -> AI Confidence: **99.31%**
1275. **`src/coreclr/System.Private.CoreLib/src/System/__ComObject.cs`** -> AI Confidence: **99.31%**
1276. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Core/Execution/ExecutionDomain.cs`** -> AI Confidence: **99.31%**
1277. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Core/Execution/MethodBaseInvoker.cs`** -> AI Confidence: **99.31%**
1278. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Extensions/NonPortable/CustomAttributeSearcher.cs`** -> AI Confidence: **99.31%**
1279. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Activator.NativeAot.cs`** -> AI Confidence: **99.31%**
1280. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/ActivatorImplementation.cs`** -> AI Confidence: **99.31%**
1281. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Array.NativeAot.cs`** -> AI Confidence: **99.31%**
1282. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Delegate.cs`** -> AI Confidence: **99.31%**
1283. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Exception.NativeAot.cs`** -> AI Confidence: **99.31%**
1284. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/CustomAttributes/NativeFormat/NativeFormatCustomAttributeData.cs`** -> AI Confidence: **99.31%**
1285. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/General/MetadataReaderExtensions.NativeFormat.cs`** -> AI Confidence: **99.31%**
1286. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/MethodInfos/OpenMethodInvoker.cs`** -> AI Confidence: **99.31%**
1287. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/TypeInfos/NativeFormat/NativeFormatRuntimeTypeInfo.CoreGetDeclared.cs`** -> AI Confidence: **99.31%**
1288. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/TypeInfos/RuntimeTypeInfo.cs`** -> AI Confidence: **99.31%**
1289. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/CompilerServices/ClassConstructorRunner.cs`** -> AI Confidence: **99.31%**
1290. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/InteropServices/Marshal.NativeAot.cs`** -> AI Confidence: **99.31%**
1291. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/InteropServices/PInvokeMarshal.cs`** -> AI Confidence: **99.31%**
1292. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/RuntimeExceptionHelpers.cs`** -> AI Confidence: **99.31%**
1293. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Threading/Thread.NativeAot.cs`** -> AI Confidence: **99.31%**
1294. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Type.NativeAot.cs`** -> AI Confidence: **99.31%**
1295. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/GenericDictionaryCell.cs`** -> AI Confidence: **99.31%**
1296. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeBuilder.cs`** -> AI Confidence: **99.31%**
1297. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.FieldAccess.cs`** -> AI Confidence: **99.31%**
1298. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.GVMResolution.cs`** -> AI Confidence: **99.31%**
1299. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.Metadata.cs`** -> AI Confidence: **99.31%**
1300. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/TypeSystem/TypeDesc.Runtime.cs`** -> AI Confidence: **99.31%**
1301. **`src/coreclr/tools/Common/CommandLineHelpers.cs`** -> AI Confidence: **99.31%**
1302. **`src/coreclr/tools/Common/Compiler/CompilerTypeSystemContext.cs`** -> AI Confidence: **99.31%**
1303. **`src/coreclr/tools/Common/Compiler/GenericCycleDetection/GraphBuilder.cs`** -> AI Confidence: **99.31%**
1304. **`src/coreclr/tools/Common/Compiler/GenericCycleDetection/ModuleCycleInfo.cs`** -> AI Confidence: **99.31%**
1305. **`src/coreclr/tools/Common/Compiler/NativeAotNameMangler.cs`** -> AI Confidence: **99.31%**
1306. **`src/coreclr/tools/Common/Compiler/ObjectWriter/ElfObjectWriter.cs`** -> AI Confidence: **99.31%**
1307. **`src/coreclr/tools/Common/Compiler/ObjectWriter/ObjectWriter.cs`** -> AI Confidence: **99.31%**
1308. **`src/coreclr/tools/Common/Compiler/ObjectWriter/PEObjectWriter.cs`** -> AI Confidence: **99.31%**
1309. **`src/coreclr/tools/Common/Compiler/ObjectWriter/StringTableBuilder.cs`** -> AI Confidence: **99.31%**
1310. **`src/coreclr/tools/Common/Compiler/ObjectWriter/WasmObjectWriter.cs`** -> AI Confidence: **99.31%**
1311. **`src/coreclr/tools/Common/Compiler/TypeMapMetadata.cs`** -> AI Confidence: **99.31%**
1312. **`src/coreclr/tools/Common/Compiler/Win32Resources/ResourceData.cs`** -> AI Confidence: **99.31%**
1313. **`src/coreclr/tools/Common/InstructionSetHelpers.cs`** -> AI Confidence: **99.31%**
1314. **`src/coreclr/tools/Common/Internal/NativeFormat/NativeFormatWriter.cs`** -> AI Confidence: **99.31%**
1315. **`src/coreclr/tools/Common/JitInterface/CorInfoImpl.cs`** -> AI Confidence: **99.31%**
1316. **`src/coreclr/tools/Common/JitInterface/ThunkGenerator/InstructionSetGenerator.cs`** -> AI Confidence: **99.31%**
1317. **`src/coreclr/tools/Common/JitInterface/ThunkGenerator/Program.cs`** -> AI Confidence: **99.31%**
1318. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaMethod.cs`** -> AI Confidence: **99.31%**
1319. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaModule.cs`** -> AI Confidence: **99.31%**
1320. **`src/coreclr/tools/Common/TypeSystem/IL/FlowGraph.cs`** -> AI Confidence: **99.31%**
1321. **`src/coreclr/tools/Common/TypeSystem/IL/Stubs/StructMarshallingThunk.cs`** -> AI Confidence: **99.31%**
1322. **`src/coreclr/tools/Common/TypeSystem/IL/UnsafeAccessors.cs`** -> AI Confidence: **99.31%**
1323. **`src/coreclr/tools/Common/TypeSystem/Interop/UnmanagedCallingConventions.cs`** -> AI Confidence: **99.31%**
1324. **`src/coreclr/tools/Common/TypeSystem/MetadataEmitter/TypeSystemMetadataEmitter.cs`** -> AI Confidence: **99.31%**
1325. **`src/coreclr/tools/ILTrim.Core/DependencyAnalysis/TokenBased/MethodDefinitionNode.cs`** -> AI Confidence: **99.31%**
1326. **`src/coreclr/tools/ILVerification/AccessVerificationHelpers.cs`** -> AI Confidence: **99.31%**
1327. **`src/coreclr/tools/ILVerification/TypeVerifier.cs`** -> AI Confidence: **99.31%**
1328. **`src/coreclr/tools/ILVerification/Verifier.cs`** -> AI Confidence: **99.31%**
1329. **`src/coreclr/tools/ILVerify/Program.cs`** -> AI Confidence: **99.31%**
1330. **`src/coreclr/tools/aot/DependencyGraphViewer/Program.cs`** -> AI Confidence: **99.31%**
1331. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/BodySubstitutionParser.cs`** -> AI Confidence: **99.31%**
1332. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/CompilerTypeSystemContext.Aot.cs`** -> AI Confidence: **99.31%**
1333. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/CompilerGeneratedState.cs`** -> AI Confidence: **99.31%**
1334. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/FlowAnnotations.cs`** -> AI Confidence: **99.31%**
1335. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/HandleCallAction.cs`** -> AI Confidence: **99.31%**
1336. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/MethodBodyScanner.cs`** -> AI Confidence: **99.31%**
1337. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/ReflectionMarker.cs`** -> AI Confidence: **99.31%**
1338. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/DynamicDependencyAttributesOnEntityNode.cs`** -> AI Confidence: **99.31%**
1339. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/EETypeNode.cs`** -> AI Confidence: **99.31%**
1340. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/ReadyToRunGenericHelperNode.cs`** -> AI Confidence: **99.31%**
1341. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DescriptorMarker.cs`** -> AI Confidence: **99.31%**
1342. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ILScanner.cs`** -> AI Confidence: **99.31%**
1343. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Logger.cs`** -> AI Confidence: **99.31%**
1344. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Logging/DocumentationSignatureParser.cs`** -> AI Confidence: **99.31%**
1345. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Logging/UnconditionalSuppressMessageAttributeState.cs`** -> AI Confidence: **99.31%**
1346. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/CoffObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1347. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/Dwarf/DwarfBuilder.cs`** -> AI Confidence: **99.31%**
1348. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/Dwarf/DwarfInfo.cs`** -> AI Confidence: **99.31%**
1349. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/ElfObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1350. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/MachObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1351. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/ObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1352. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/UnixObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1353. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/SourceLinkWriter.cs`** -> AI Confidence: **99.31%**
1354. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/SubstitutedILProvider.cs`** -> AI Confidence: **99.31%**
1355. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/TypePreinit.cs`** -> AI Confidence: **99.31%**
1356. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/UsageBasedMetadataManager.cs`** -> AI Confidence: **99.31%**
1357. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/UserDefinedTypeDescriptor.cs`** -> AI Confidence: **99.31%**
1358. **`src/coreclr/tools/aot/ILCompiler.Diagnostics/PdbWriter.cs`** -> AI Confidence: **99.31%**
1359. **`src/coreclr/tools/aot/ILCompiler.MetadataTransform/ILCompiler/Metadata/Transform.Type.cs`** -> AI Confidence: **99.31%**
1360. **`src/coreclr/tools/aot/ILCompiler.MetadataTransform/Internal/Metadata/NativeFormat/Writer/MdBinaryWriterGen.cs`** -> AI Confidence: **99.31%**
1361. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun.Tests/TestCasesRunner/R2RResultChecker.cs`** -> AI Confidence: **99.31%**
1362. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/CallChainProfile.cs`** -> AI Confidence: **99.31%**
1363. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/ArgIterator.cs`** -> AI Confidence: **99.31%**
1364. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/AttributePresenceFilterNode.cs`** -> AI Confidence: **99.31%**
1365. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/GenericLookupSignature.cs`** -> AI Confidence: **99.31%**
1366. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/InliningInfoNode.cs`** -> AI Confidence: **99.31%**
1367. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/InstrumentationDataTableNode.cs`** -> AI Confidence: **99.31%**
1368. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/ManifestMetadataTableNode.cs`** -> AI Confidence: **99.31%**
1369. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/MethodFixupSignature.cs`** -> AI Confidence: **99.31%**
1370. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/SignatureBuilder.cs`** -> AI Confidence: **99.31%**
1371. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/TypeFixupSignature.cs`** -> AI Confidence: **99.31%**
1372. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/TypeGenericInfoMapNode.cs`** -> AI Confidence: **99.31%**
1373. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/TypeValidationChecker.cs`** -> AI Confidence: **99.31%**
1374. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/WasmImportThunk.cs`** -> AI Confidence: **99.31%**
1375. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/FileLayoutOptimizer.cs`** -> AI Confidence: **99.31%**
1376. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ProfileDataManager.cs`** -> AI Confidence: **99.31%**
1377. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunCodegenCompilation.cs`** -> AI Confidence: **99.31%**
1378. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunMetadataFieldLayoutAlgorithm.cs`** -> AI Confidence: **99.31%**
1379. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunProfilingRootProvider.cs`** -> AI Confidence: **99.31%**
1380. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/IL/ReadyToRunILProvider.cs`** -> AI Confidence: **99.31%**
1381. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/EHInfo.cs`** -> AI Confidence: **99.31%**
1382. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/MachO/MachOImageReader.cs`** -> AI Confidence: **99.31%**
1383. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/ReadyToRunMethod.cs`** -> AI Confidence: **99.31%**
1384. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/ReadyToRunReader.cs`** -> AI Confidence: **99.31%**
1385. **`src/coreclr/tools/aot/ILCompiler.RyuJit/JitInterface/CorInfoImpl.RyuJit.cs`** -> AI Confidence: **99.31%**
1386. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/AssemblyChecker.cs`** -> AI Confidence: **99.31%**
1387. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/ResultChecker.cs`** -> AI Confidence: **99.31%**
1388. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/TrimmingDriver.cs`** -> AI Confidence: **99.31%**
1389. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/Tests/DocumentationSignatureParserTests.cs`** -> AI Confidence: **99.31%**
1390. **`src/coreclr/tools/aot/ILCompiler/ILCompilerRootCommand.cs`** -> AI Confidence: **99.31%**
1391. **`src/coreclr/tools/aot/ILCompiler/RdXmlRootProvider.cs`** -> AI Confidence: **99.31%**
1392. **`src/coreclr/tools/aot/crossgen2/Program.cs`** -> AI Confidence: **99.31%**
1393. **`src/coreclr/tools/dotnet-pgo/Program.cs`** -> AI Confidence: **99.31%**
1394. **`src/coreclr/tools/dotnet-pgo/R2RSignatureTypeProvider.cs`** -> AI Confidence: **99.31%**
1395. **`src/coreclr/tools/dotnet-pgo/SPGO/SampleCorrelator.cs`** -> AI Confidence: **99.31%**
1396. **`src/coreclr/tools/dotnet-pgo/TraceRuntimeDescToTypeSystemDesc.cs`** -> AI Confidence: **99.31%**
1397. **`src/coreclr/tools/r2rdump/CoreDisTools.cs`** -> AI Confidence: **99.31%**
1398. **`src/coreclr/tools/r2rdump/Program.cs`** -> AI Confidence: **99.31%**
1399. **`src/coreclr/tools/r2rdump/R2RDiff.cs`** -> AI Confidence: **99.31%**
1400. **`src/coreclr/tools/r2rdump/TextDumper.cs`** -> AI Confidence: **99.31%**
1401. **`src/coreclr/tools/r2rtest/Commands/CompileSubtreeCommand.cs`** -> AI Confidence: **99.31%**
1402. **`src/coreclr/tools/r2rtest/ParallelRunner.cs`** -> AI Confidence: **99.31%**
1403. **`src/coreclr/tools/r2rtest/ProcessRunner.cs`** -> AI Confidence: **99.31%**
1404. **`src/installer/managed/Microsoft.NET.HostModel/AppHost/HostWriter.cs`** -> AI Confidence: **99.31%**
1405. **`src/installer/managed/Microsoft.NET.HostModel/Bundle/Bundler.cs`** -> AI Confidence: **99.31%**
1406. **`src/installer/managed/Microsoft.NET.HostModel/Bundle/Manifest.cs`** -> AI Confidence: **99.31%**
1407. **`src/installer/tests/TestUtils/Command.cs`** -> AI Confidence: **99.31%**
1408. **`src/installer/tests/TestUtils/RuntimeConfig.cs`** -> AI Confidence: **99.31%**
1409. **`src/libraries/Common/src/Internal/Cryptography/PkcsHelpers.cs`** -> AI Confidence: **99.31%**
1410. **`src/libraries/Common/src/Interop/Interop.Odbc.cs`** -> AI Confidence: **99.31%**
1411. **`src/libraries/Common/src/Interop/Linux/procfs/Interop.ProcFsStat.ParseMapModules.cs`** -> AI Confidence: **99.31%**
1412. **`src/libraries/Common/src/Interop/Linux/procfs/Interop.ProcFsStat.TryReadStatusFile.cs`** -> AI Confidence: **99.31%**
1413. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.Keychain.macOS.cs`** -> AI Confidence: **99.31%**
1414. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.SecKeyRef.macOS.cs`** -> AI Confidence: **99.31%**
1415. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.Ssl.cs`** -> AI Confidence: **99.31%**
1416. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.X509.iOS.cs`** -> AI Confidence: **99.31%**
1417. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.X509.macOS.cs`** -> AI Confidence: **99.31%**
1418. **`src/libraries/Common/src/Interop/Windows/HttpApi/Interop.HttpApi.cs`** -> AI Confidence: **99.31%**
1419. **`src/libraries/Common/src/System/HexConverter.cs`** -> AI Confidence: **99.31%**
1420. **`src/libraries/Common/src/System/IO/FileSystem.Attributes.Windows.cs`** -> AI Confidence: **99.31%**
1421. **`src/libraries/Common/src/System/Net/Http/X509ResourceClient.cs`** -> AI Confidence: **99.31%**
1422. **`src/libraries/Common/src/System/Security/Cryptography/CompositeMLDsaManaged.ECDsa.cs`** -> AI Confidence: **99.31%**
1423. **`src/libraries/Common/src/System/Security/Cryptography/Helpers.cs`** -> AI Confidence: **99.31%**
1424. **`src/libraries/Common/src/System/Security/Cryptography/MLKemCng.Windows.cs`** -> AI Confidence: **99.31%**
1425. **`src/libraries/Common/src/System/Security/Cryptography/PasswordBasedEncryption.cs`** -> AI Confidence: **99.31%**
1426. **`src/libraries/Common/src/System/Security/Cryptography/Pkcs/Pkcs12SafeContents.cs`** -> AI Confidence: **99.31%**
1427. **`src/libraries/Common/src/System/Security/Cryptography/PqcBlobHelpers.cs`** -> AI Confidence: **99.31%**
1428. **`src/libraries/Common/src/System/Security/Cryptography/RSAAndroid.cs`** -> AI Confidence: **99.31%**
1429. **`src/libraries/Common/src/System/Security/Cryptography/RSAAppleCrypto.cs`** -> AI Confidence: **99.31%**
1430. **`src/libraries/Common/src/System/Security/Cryptography/X509Certificates/CertificateHelpers.Windows.cs`** -> AI Confidence: **99.31%**
1431. **`src/libraries/Common/tests/AndroidTestRunner/AndroidTestRunner.cs`** -> AI Confidence: **99.31%**
1432. **`src/libraries/Common/tests/AppleTestRunner/AppleTestRunner.cs`** -> AI Confidence: **99.31%**
1433. **`src/libraries/Common/tests/SourceGenerators/RoslynTestUtils.cs`** -> AI Confidence: **99.31%**
1434. **`src/libraries/Common/tests/StaticTestGenerator/Program.cs`** -> AI Confidence: **99.31%**
1435. **`src/libraries/Common/tests/System/Net/Http/Http3LoopbackStream.cs`** -> AI Confidence: **99.31%**
1436. **`src/libraries/Common/tests/System/Net/Prerequisites/RemoteLoopServer/Handlers/RemoteLoopHandler.cs`** -> AI Confidence: **99.31%**
1437. **`src/libraries/Common/tests/System/Net/Security/FakeNegotiateServer.cs`** -> AI Confidence: **99.31%**
1438. **`src/libraries/Common/tests/System/Net/Security/FakeNtlmServer.cs`** -> AI Confidence: **99.31%**
1439. **`src/libraries/Common/tests/System/Runtime/Serialization/Utils.cs`** -> AI Confidence: **99.31%**
1440. **`src/libraries/Common/tests/System/Security/Cryptography/X509Certificates/RevocationResponder.cs`** -> AI Confidence: **99.31%**
1441. **`src/libraries/Common/tests/System/Xml/XmlCoreTest/AsyncUtil.cs`** -> AI Confidence: **99.31%**
1442. **`src/libraries/Common/tests/System/Xml/XmlCoreTest/ReaderUtil.cs`** -> AI Confidence: **99.31%**
1443. **`src/libraries/Common/tests/System/Xml/XmlCoreTest/WriterFactory.cs`** -> AI Confidence: **99.31%**
1444. **`src/libraries/Common/tests/System/Xml/XmlDiff/XmlDiffDocument.cs`** -> AI Confidence: **99.31%**
1445. **`src/libraries/Common/tests/TestUtilities/System/AssertExtensions.cs`** -> AI Confidence: **99.31%**
1446. **`src/libraries/Common/tests/WasmTestRunner/WasmTestRunner.cs`** -> AI Confidence: **99.31%**
1447. **`src/libraries/Fuzzing/DotnetFuzzing/Fuzzers/Utf8JsonReaderFuzzer.cs`** -> AI Confidence: **99.31%**
1448. **`src/libraries/Fuzzing/DotnetFuzzing/Program.cs`** -> AI Confidence: **99.31%**
1449. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ComInterop/ComRuntimeHelpers.cs`** -> AI Confidence: **99.31%**
1450. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ComInterop/DynamicVariantExtensions.cs`** -> AI Confidence: **99.31%**
1451. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ComInterop/IDispatchComObject.cs`** -> AI Confidence: **99.31%**
1452. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ExpressionTreeCallRewriter.cs`** -> AI Confidence: **99.31%**
1453. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/RuntimeBinder.cs`** -> AI Confidence: **99.31%**
1454. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Semantics/Types/TypeManager.cs`** -> AI Confidence: **99.31%**
1455. **`src/libraries/Microsoft.Extensions.Caching.Abstractions/src/Hybrid/HybridCache.cs`** -> AI Confidence: **99.31%**
1456. **`src/libraries/Microsoft.Extensions.Caching.Memory/src/CacheEntry.CacheEntryTokens.cs`** -> AI Confidence: **99.31%**
1457. **`src/libraries/Microsoft.Extensions.Caching.Memory/src/CacheEntry.cs`** -> AI Confidence: **99.31%**
1458. **`src/libraries/Microsoft.Extensions.Caching.Memory/src/MemoryCache.cs`** -> AI Confidence: **99.31%**
1459. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/ConfigurationBindingGenerator.Parser.cs`** -> AI Confidence: **99.31%**
1460. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/ConfigurationBindingGenerator.Suppressor.cs`** -> AI Confidence: **99.31%**
1461. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/ConfigurationBindingGenerator.cs`** -> AI Confidence: **99.31%**
1462. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/Specs/InterceptorInfo.cs`** -> AI Confidence: **99.31%**
1463. **`src/libraries/Microsoft.Extensions.Configuration.Binder/src/ConfigurationBinder.cs`** -> AI Confidence: **99.31%**
1464. **`src/libraries/Microsoft.Extensions.Configuration.FileExtensions/src/FileConfigurationProvider.cs`** -> AI Confidence: **99.31%**
1465. **`src/libraries/Microsoft.Extensions.Configuration.Xml/src/XmlStreamConfigurationProvider.cs`** -> AI Confidence: **99.31%**
1466. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/ServiceLookup/CallSiteFactory.cs`** -> AI Confidence: **99.31%**
1467. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/ServiceLookup/CallSiteRuntimeResolver.cs`** -> AI Confidence: **99.31%**
1468. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/ServiceLookup/ILEmit/ILEmitResolverBuilder.cs`** -> AI Confidence: **99.31%**
1469. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/ServiceProvider.cs`** -> AI Confidence: **99.31%**
1470. **`src/libraries/Microsoft.Extensions.Diagnostics/tests/DefaultMetricsFactoryTests.cs`** -> AI Confidence: **99.31%**
1471. **`src/libraries/Microsoft.Extensions.FileProviders.Physical/src/PhysicalFileProvider.cs`** -> AI Confidence: **99.31%**
1472. **`src/libraries/Microsoft.Extensions.FileProviders.Physical/src/PhysicalFilesWatcher.cs`** -> AI Confidence: **99.31%**
1473. **`src/libraries/Microsoft.Extensions.FileProviders.Physical/src/PollingWildCardChangeToken.cs`** -> AI Confidence: **99.31%**
1474. **`src/libraries/Microsoft.Extensions.FileSystemGlobbing/src/Internal/MatcherContext.cs`** -> AI Confidence: **99.31%**
1475. **`src/libraries/Microsoft.Extensions.HostFactoryResolver/src/HostFactoryResolver.cs`** -> AI Confidence: **99.31%**
1476. **`src/libraries/Microsoft.Extensions.Hosting/src/HostApplicationBuilder.cs`** -> AI Confidence: **99.31%**
1477. **`src/libraries/Microsoft.Extensions.Hosting/src/Internal/Host.cs`** -> AI Confidence: **99.31%**
1478. **`src/libraries/Microsoft.Extensions.Hosting/tests/FunctionalTests/IntegrationTesting/src/Deployers/ApplicationDeployer.cs`** -> AI Confidence: **99.31%**
1479. **`src/libraries/Microsoft.Extensions.Http/src/DefaultHttpClientFactory.cs`** -> AI Confidence: **99.31%**
1480. **`src/libraries/Microsoft.Extensions.Http/tests/Microsoft.Extensions.Http.Tests/Logging/LoggingUriOutputTests.cs`** -> AI Confidence: **99.31%**
1481. **`src/libraries/Microsoft.Extensions.Logging.Abstractions/gen/LoggerMessageGenerator.Parser.cs`** -> AI Confidence: **99.31%**
1482. **`src/libraries/Microsoft.Extensions.Logging.Abstractions/gen/LoggerMessageGenerator.Roslyn4.0.cs`** -> AI Confidence: **99.31%**
1483. **`src/libraries/Microsoft.Extensions.Logging.Console/src/ConsoleLoggerProcessor.cs`** -> AI Confidence: **99.31%**
1484. **`src/libraries/Microsoft.Extensions.Logging.Console/src/ConsoleLoggerProvider.cs`** -> AI Confidence: **99.31%**
1485. **`src/libraries/Microsoft.Extensions.Logging.Console/src/JsonConsoleFormatter.cs`** -> AI Confidence: **99.31%**
1486. **`src/libraries/Microsoft.Extensions.Logging.EventSource/src/EventSourceLogger.cs`** -> AI Confidence: **99.31%**
1487. **`src/libraries/Microsoft.Extensions.Logging/src/LoggerFactory.cs`** -> AI Confidence: **99.31%**
1488. **`src/libraries/Microsoft.Extensions.Options/gen/Emitter.cs`** -> AI Confidence: **99.31%**
1489. **`src/libraries/Microsoft.Extensions.Options/gen/Parser.cs`** -> AI Confidence: **99.31%**
1490. **`src/libraries/Microsoft.Extensions.Primitives/src/StringValues.cs`** -> AI Confidence: **99.31%**
1491. **`src/libraries/System.Collections.Immutable/src/System/Collections/Frozen/FrozenDictionary.cs`** -> AI Confidence: **99.31%**
1492. **`src/libraries/System.Collections.Immutable/tests/ImmutableSortedDictionaryTest.cs`** -> AI Confidence: **99.31%**
1493. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/AttributedModel/AttributedPartCreationInfo.cs`** -> AI Confidence: **99.31%**
1494. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/CompositionException.cs`** -> AI Confidence: **99.31%**
1495. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ExportServices.cs`** -> AI Confidence: **99.31%**
1496. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/AggregateExportProvider.cs`** -> AI Confidence: **99.31%**
1497. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/CatalogExportProvider.cs`** -> AI Confidence: **99.31%**
1498. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/ComposablePartExportProvider.cs`** -> AI Confidence: **99.31%**
1499. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/CompositionServices.cs`** -> AI Confidence: **99.31%**
1500. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/DirectoryCatalog.cs`** -> AI Confidence: **99.31%**
1501. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/ExportProvider.GetExportOverrides.cs`** -> AI Confidence: **99.31%**
1502. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/FilteredCatalog.cs`** -> AI Confidence: **99.31%**
1503. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/ImportEngine.cs`** -> AI Confidence: **99.31%**
1504. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/TypeCatalog.cs`** -> AI Confidence: **99.31%**
1505. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Primitives/ContractBasedImportDefinition.cs`** -> AI Confidence: **99.31%**
1506. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/GenericSpecializationPartCreationInfo.cs`** -> AI Confidence: **99.31%**
1507. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/ReflectionComposablePart.cs`** -> AI Confidence: **99.31%**
1508. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/ReflectionComposablePartDefinition.cs`** -> AI Confidence: **99.31%**
1509. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/ReflectionModelServices.cs`** -> AI Confidence: **99.31%**
1510. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/CultureInfoConverter.cs`** -> AI Confidence: **99.31%**
1511. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/EnumConverter.cs`** -> AI Confidence: **99.31%**
1512. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/ReflectTypeDescriptionProvider.cs`** -> AI Confidence: **99.31%**
1513. **`src/libraries/System.ComponentModel.TypeConverter/src/System/Drawing/ColorConverter.cs`** -> AI Confidence: **99.31%**
1514. **`src/libraries/System.ComponentModel.TypeConverter/src/System/Security/Authentication/ExtendedProtection/ExtendedProtectionPolicyTypeConverter.cs`** -> AI Confidence: **99.31%**
1515. **`src/libraries/System.ComponentModel.TypeConverter/tests/TypeConverterTestBase.cs`** -> AI Confidence: **99.31%**
1516. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/ClientConfigPaths.cs`** -> AI Confidence: **99.31%**
1517. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/SettingsPropertyValue.cs`** -> AI Confidence: **99.31%**
1518. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Diagnostics/TraceUtils.cs`** -> AI Confidence: **99.31%**
1519. **`src/libraries/System.Console/src/System/Console.cs`** -> AI Confidence: **99.31%**
1520. **`src/libraries/System.Console/tests/Color.cs`** -> AI Confidence: **99.31%**
1521. **`src/libraries/System.Data.Common/src/System/Data/Common/DbProviderFactories.cs`** -> AI Confidence: **99.31%**
1522. **`src/libraries/System.Data.Common/src/System/Data/Common/ObjectStorage.cs`** -> AI Confidence: **99.31%**
1523. **`src/libraries/System.Data.Common/src/System/Data/Common/SqlUDTStorage.cs`** -> AI Confidence: **99.31%**
1524. **`src/libraries/System.Data.Common/src/System/Data/DataView.cs`** -> AI Confidence: **99.31%**
1525. **`src/libraries/System.Data.Common/src/System/Data/DataViewManager.cs`** -> AI Confidence: **99.31%**
1526. **`src/libraries/System.Data.Common/src/System/Data/LinqDataView.cs`** -> AI Confidence: **99.31%**
1527. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLBinary.cs`** -> AI Confidence: **99.31%**
1528. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLBytes.cs`** -> AI Confidence: **99.31%**
1529. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLChars.cs`** -> AI Confidence: **99.31%**
1530. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLDecimal.cs`** -> AI Confidence: **99.31%**
1531. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLInt64.cs`** -> AI Confidence: **99.31%**
1532. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SqlXml.cs`** -> AI Confidence: **99.31%**
1533. **`src/libraries/System.Data.Common/src/System/Data/TypeLimiter.cs`** -> AI Confidence: **99.31%**
1534. **`src/libraries/System.Data.Common/src/System/Data/xmlsaver.cs`** -> AI Confidence: **99.31%**
1535. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcConnectionStringbuilder.cs`** -> AI Confidence: **99.31%**
1536. **`src/libraries/System.Data.OleDb/src/OleDbConnection.cs`** -> AI Confidence: **99.31%**
1537. **`src/libraries/System.Data.OleDb/src/OleDbConnectionFactory.cs`** -> AI Confidence: **99.31%**
1538. **`src/libraries/System.Data.OleDb/src/OleDbConnectionInternal.cs`** -> AI Confidence: **99.31%**
1539. **`src/libraries/System.Data.OleDb/src/OleDbException.cs`** -> AI Confidence: **99.31%**
1540. **`src/libraries/System.Data.OleDb/src/OleDb_Util.cs`** -> AI Confidence: **99.31%**
1541. **`src/libraries/System.Data.OleDb/src/System/Data/ProviderBase/DbConnectionPoolCounters.cs`** -> AI Confidence: **99.31%**
1542. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Activity.cs`** -> AI Confidence: **99.31%**
1543. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/AggregationManager.cs`** -> AI Confidence: **99.31%**
1544. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/MetricsEventSource.cs`** -> AI Confidence: **99.31%**
1545. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/TagList.netcore.cs`** -> AI Confidence: **99.31%**
1546. **`src/libraries/System.Diagnostics.DiagnosticSource/tests/MetricOuterLoopTests/Common.cs`** -> AI Confidence: **99.31%**
1547. **`src/libraries/System.Diagnostics.DiagnosticSource/tests/MetricsTests.cs`** -> AI Confidence: **99.31%**
1548. **`src/libraries/System.Diagnostics.DiagnosticSource/tests/RuntimeMetricsTests.cs`** -> AI Confidence: **99.31%**
1549. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/EventLogEntry.cs`** -> AI Confidence: **99.31%**
1550. **`src/libraries/System.Diagnostics.EventLog/tests/System/Diagnostics/Reader/ProviderMetadataTests.cs`** -> AI Confidence: **99.31%**
1551. **`src/libraries/System.Diagnostics.PerformanceCounter/src/System/Diagnostics/PerformanceCounterLib.cs`** -> AI Confidence: **99.31%**
1552. **`src/libraries/System.Diagnostics.PerformanceCounter/src/System/Diagnostics/SharedPerformanceCounter.cs`** -> AI Confidence: **99.31%**
1553. **`src/libraries/System.Diagnostics.Process/src/Microsoft/Win32/SafeHandles/SafeProcessHandle.Unix.cs`** -> AI Confidence: **99.31%**
1554. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Linux.cs`** -> AI Confidence: **99.31%**
1555. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Multiplexing.cs`** -> AI Confidence: **99.31%**
1556. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Unix.cs`** -> AI Confidence: **99.31%**
1557. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Windows.cs`** -> AI Confidence: **99.31%**
1558. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.cs`** -> AI Confidence: **99.31%**
1559. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/ProcessUtils.Unix.cs`** -> AI Confidence: **99.31%**
1560. **`src/libraries/System.Diagnostics.Process/tests/Helpers.cs`** -> AI Confidence: **99.31%**
1561. **`src/libraries/System.Diagnostics.TraceSource/src/System/Diagnostics/Switch.cs`** -> AI Confidence: **99.31%**
1562. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADAMStoreCtx.cs`** -> AI Confidence: **99.31%**
1563. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADUtils.cs`** -> AI Confidence: **99.31%**
1564. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/SDSCache.cs`** -> AI Confidence: **99.31%**
1565. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AuthZSet.cs`** -> AI Confidence: **99.31%**
1566. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/Context.cs`** -> AI Confidence: **99.31%**
1567. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/Principal.cs`** -> AI Confidence: **99.31%**
1568. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMMembersSet.cs`** -> AI Confidence: **99.31%**
1569. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMQuerySet.cs`** -> AI Confidence: **99.31%**
1570. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMStoreCtx_LoadStore.cs`** -> AI Confidence: **99.31%**
1571. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMStoreCtx_Query.cs`** -> AI Confidence: **99.31%**
1572. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMUtils.cs`** -> AI Confidence: **99.31%**
1573. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/exceptions.cs`** -> AI Confidence: **99.31%**
1574. **`src/libraries/System.DirectoryServices.Protocols/src/System/DirectoryServices/Protocols/ldap/LdapSessionOptions.cs`** -> AI Confidence: **99.31%**
1575. **`src/libraries/System.DirectoryServices.Protocols/tests/TestServer/LdapTestServer.Protocol.cs`** -> AI Confidence: **99.31%**
1576. **`src/libraries/System.DirectoryServices.Protocols/tests/TestServer/LdapTestServer.cs`** -> AI Confidence: **99.31%**
1577. **`src/libraries/System.Formats.Nrbf/src/System/Formats/Nrbf/ArraySinglePrimitiveRecord.cs`** -> AI Confidence: **99.31%**
1578. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarHeader.Write.cs`** -> AI Confidence: **99.31%**
1579. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarWriter.Windows.cs`** -> AI Confidence: **99.31%**
1580. **`src/libraries/System.IO.Compression/src/System/IO/Compression/DeflateZLib/DeflateStream.cs`** -> AI Confidence: **99.31%**
1581. **`src/libraries/System.IO.Compression/src/System/IO/Compression/ZipArchiveEntry.cs`** -> AI Confidence: **99.31%**
1582. **`src/libraries/System.IO.Compression/src/System/IO/Compression/ZipBlocks.cs`** -> AI Confidence: **99.31%**
1583. **`src/libraries/System.IO.FileSystem.Watcher/src/System/IO/FileSystemWatcher.Linux.cs`** -> AI Confidence: **99.31%**
1584. **`src/libraries/System.IO.FileSystem.Watcher/src/System/IO/FileSystemWatcher.OSX.cs`** -> AI Confidence: **99.31%**
1585. **`src/libraries/System.IO.FileSystem.Watcher/src/System/IO/FileSystemWatcher.cs`** -> AI Confidence: **99.31%**
1586. **`src/libraries/System.IO.Hashing/src/System/IO/Hashing/Adler32.cs`** -> AI Confidence: **99.31%**
1587. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/Package.cs`** -> AI Confidence: **99.31%**
1588. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/PartBasedPackageProperties.cs`** -> AI Confidence: **99.31%**
1589. **`src/libraries/System.IO.Pipes/src/Microsoft/Win32/SafeHandles/SafePipeHandle.Unix.cs`** -> AI Confidence: **99.31%**
1590. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/NamedPipeClientStream.Unix.cs`** -> AI Confidence: **99.31%**
1591. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/NamedPipeClientStream.cs`** -> AI Confidence: **99.31%**
1592. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/PipeStream.Unix.cs`** -> AI Confidence: **99.31%**
1593. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/PipeStream.Windows.cs`** -> AI Confidence: **99.31%**
1594. **`src/libraries/System.IO.Ports/src/System/IO/Ports/SerialStream.Unix.cs`** -> AI Confidence: **99.31%**
1595. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadByte.cs`** -> AI Confidence: **99.31%**
1596. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadChar.cs`** -> AI Confidence: **99.31%**
1597. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadTo.cs`** -> AI Confidence: **99.31%**
1598. **`src/libraries/System.IO.Ports/tests/SerialPort/Read_byte_int_int.cs`** -> AI Confidence: **99.31%**
1599. **`src/libraries/System.IO.Ports/tests/SerialPort/Read_char_int_int.cs`** -> AI Confidence: **99.31%**
1600. **`src/libraries/System.IO.Ports/tests/Support/PortHelper.cs`** -> AI Confidence: **99.31%**
1601. **`src/libraries/System.IO.Ports/tests/Support/SerialPortConnection.cs`** -> AI Confidence: **99.31%**
1602. **`src/libraries/System.IO.Ports/tests/Support/TCSupport.cs`** -> AI Confidence: **99.31%**
1603. **`src/libraries/System.Linq.Expressions/src/System/Dynamic/ExpandoObject.cs`** -> AI Confidence: **99.31%**
1604. **`src/libraries/System.Linq.Expressions/src/System/Dynamic/Utils/DelegateHelpers.cs`** -> AI Confidence: **99.31%**
1605. **`src/libraries/System.Linq.Expressions/src/System/Dynamic/Utils/ExpressionUtils.cs`** -> AI Confidence: **99.31%**
1606. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/BoundConstants.cs`** -> AI Confidence: **99.31%**
1607. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/CompilerScope.cs`** -> AI Confidence: **99.31%**
1608. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Statements.cs`** -> AI Confidence: **99.31%**
1609. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Expression.cs`** -> AI Confidence: **99.31%**
1610. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Interpreter/CallInstruction.Generated.cs`** -> AI Confidence: **99.31%**
1611. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Interpreter/LightLambda.cs`** -> AI Confidence: **99.31%**
1612. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/LambdaExpression.cs`** -> AI Confidence: **99.31%**
1613. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/NewExpression.cs`** -> AI Confidence: **99.31%**
1614. **`src/libraries/System.Linq.Parallel/src/System/Linq/Parallel/Scheduling/OrderPreservingPipeliningSpoolingTask.cs`** -> AI Confidence: **99.31%**
1615. **`src/libraries/System.Linq.Parallel/src/System/Linq/ParallelEnumerable.cs`** -> AI Confidence: **99.31%**
1616. **`src/libraries/System.Linq.Queryable/src/System/Linq/EnumerableRewriter.cs`** -> AI Confidence: **99.31%**
1617. **`src/libraries/System.Management/src/System/Management/ManagementPath.cs`** -> AI Confidence: **99.31%**
1618. **`src/libraries/System.Memory.Data/src/System/BinaryData.cs`** -> AI Confidence: **99.31%**
1619. **`src/libraries/System.Memory/tests/Span/EnumerateLines.cs`** -> AI Confidence: **99.31%**
1620. **`src/libraries/System.Memory/tests/Span/StringSearchValues.cs`** -> AI Confidence: **99.31%**
1621. **`src/libraries/System.Net.Http.Json/src/System/Net/Http/Json/HttpClientJsonExtensions.Get.AsyncEnumerable.cs`** -> AI Confidence: **99.31%**
1622. **`src/libraries/System.Net.Http.Json/src/System/Net/Http/Json/HttpClientJsonExtensions.cs`** -> AI Confidence: **99.31%**
1623. **`src/libraries/System.Net.Http.Json/src/System/Net/Http/Json/JsonContent.cs`** -> AI Confidence: **99.31%**
1624. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpHandler.cs`** -> AI Confidence: **99.31%**
1625. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpRequestCallback.cs`** -> AI Confidence: **99.31%**
1626. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpResponseParser.cs`** -> AI Confidence: **99.31%**
1627. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpResponseStream.cs`** -> AI Confidence: **99.31%**
1628. **`src/libraries/System.Net.Http/src/System/Net/Http/Headers/CacheControlHeaderValue.cs`** -> AI Confidence: **99.31%**
1629. **`src/libraries/System.Net.Http/src/System/Net/Http/Headers/HttpHeaders.cs`** -> AI Confidence: **99.31%**
1630. **`src/libraries/System.Net.Http/src/System/Net/Http/HttpClient.cs`** -> AI Confidence: **99.31%**
1631. **`src/libraries/System.Net.Http/src/System/Net/Http/HttpClientHandler.AnyMobile.cs`** -> AI Confidence: **99.31%**
1632. **`src/libraries/System.Net.Http/src/System/Net/Http/HttpContent.cs`** -> AI Confidence: **99.31%**
1633. **`src/libraries/System.Net.Http/src/System/Net/Http/MultipartContent.cs`** -> AI Confidence: **99.31%**
1634. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/AuthenticationHelper.Digest.cs`** -> AI Confidence: **99.31%**
1635. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/AuthenticationHelper.NtAuth.cs`** -> AI Confidence: **99.31%**
1636. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectHelper.cs`** -> AI Confidence: **99.31%**
1637. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/HttpConnectionPool.Http1.cs`** -> AI Confidence: **99.31%**
1638. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/Http2Connection.cs`** -> AI Confidence: **99.31%**
1639. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/Http2Stream.cs`** -> AI Confidence: **99.31%**
1640. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/Http3RequestStream.cs`** -> AI Confidence: **99.31%**
1641. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpConnectionPoolManager.cs`** -> AI Confidence: **99.31%**
1642. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpConnectionSettings.cs`** -> AI Confidence: **99.31%**
1643. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/SocketsHttpHandler.cs`** -> AI Confidence: **99.31%**
1644. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/SocksHelper.cs`** -> AI Confidence: **99.31%**
1645. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiHttpInterop.cs`** -> AI Confidence: **99.31%**
1646. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/Program.cs`** -> AI Confidence: **99.31%**
1647. **`src/libraries/System.Net.Http/tests/UnitTests/Headers/CacheControlHeaderValueTest.cs`** -> AI Confidence: **99.31%**
1648. **`src/libraries/System.Net.HttpListener/src/System/Net/HttpListener.cs`** -> AI Confidence: **99.31%**
1649. **`src/libraries/System.Net.HttpListener/src/System/Net/HttpListenerRequest.cs`** -> AI Confidence: **99.31%**
1650. **`src/libraries/System.Net.HttpListener/src/System/Net/Managed/HttpConnection.cs`** -> AI Confidence: **99.31%**
1651. **`src/libraries/System.Net.HttpListener/src/System/Net/Managed/HttpListenerRequest.Managed.cs`** -> AI Confidence: **99.31%**
1652. **`src/libraries/System.Net.HttpListener/src/System/Net/Managed/HttpRequestStream.Managed.cs`** -> AI Confidence: **99.31%**
1653. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpListenerContext.Windows.cs`** -> AI Confidence: **99.31%**
1654. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/WebSockets/WebSocketHttpListenerDuplexStream.cs`** -> AI Confidence: **99.31%**
1655. **`src/libraries/System.Net.HttpListener/tests/TrimmingTests/CookieExtensionsTest.Helper.cs`** -> AI Confidence: **99.31%**
1656. **`src/libraries/System.Net.Mail/src/System/Net/Base64Stream.cs`** -> AI Confidence: **99.31%**
1657. **`src/libraries/System.Net.Mail/src/System/Net/Mail/MailMessage.cs`** -> AI Confidence: **99.31%**
1658. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpClient.cs`** -> AI Confidence: **99.31%**
1659. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpCommands.cs`** -> AI Confidence: **99.31%**
1660. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpConnection.cs`** -> AI Confidence: **99.31%**
1661. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpTransport.cs`** -> AI Confidence: **99.31%**
1662. **`src/libraries/System.Net.Mail/src/System/Net/Mime/MimePart.cs`** -> AI Confidence: **99.31%**
1663. **`src/libraries/System.Net.Mail/tests/Functional/LoopbackServerTestBase.cs`** -> AI Confidence: **99.31%**
1664. **`src/libraries/System.Net.Mail/tests/Functional/LoopbackSmtpServer.cs`** -> AI Confidence: **99.31%**
1665. **`src/libraries/System.Net.NameResolution/src/System/Net/Dns.cs`** -> AI Confidence: **99.31%**
1666. **`src/libraries/System.Net.NameResolution/src/System/Net/NameResolutionPal.Unix.cs`** -> AI Confidence: **99.31%**
1667. **`src/libraries/System.Net.NameResolution/src/System/Net/NameResolutionPal.Windows.cs`** -> AI Confidence: **99.31%**
1668. **`src/libraries/System.Net.NameResolution/tests/PalTests/NameResolutionPalTests.cs`** -> AI Confidence: **99.31%**
1669. **`src/libraries/System.Net.NetworkInformation/src/System/Net/NetworkInformation/NetworkAddressChange.OSX.cs`** -> AI Confidence: **99.31%**
1670. **`src/libraries/System.Net.Ping/src/System/Net/NetworkInformation/Ping.PingUtility.cs`** -> AI Confidence: **99.31%**
1671. **`src/libraries/System.Net.Ping/src/System/Net/NetworkInformation/Ping.RawSocket.cs`** -> AI Confidence: **99.31%**
1672. **`src/libraries/System.Net.Ping/src/System/Net/NetworkInformation/Ping.Windows.cs`** -> AI Confidence: **99.31%**
1673. **`src/libraries/System.Net.Primitives/src/System/Net/IPAddress.cs`** -> AI Confidence: **99.31%**
1674. **`src/libraries/System.Net.Primitives/src/System/Net/IPAddressParser.cs`** -> AI Confidence: **99.31%**
1675. **`src/libraries/System.Net.Primitives/src/System/Net/IPEndPoint.cs`** -> AI Confidence: **99.31%**
1676. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/MsQuicApi.cs`** -> AI Confidence: **99.31%**
1677. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/ResettableValueTaskSource.cs`** -> AI Confidence: **99.31%**
1678. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/ThrowHelper.cs`** -> AI Confidence: **99.31%**
1679. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/ValueTaskSource.cs`** -> AI Confidence: **99.31%**
1680. **`src/libraries/System.Net.Quic/src/System/Net/Quic/QuicConnection.cs`** -> AI Confidence: **99.31%**
1681. **`src/libraries/System.Net.Quic/src/System/Net/Quic/QuicStream.cs`** -> AI Confidence: **99.31%**
1682. **`src/libraries/System.Net.Requests/src/System/Net/HttpWebRequest.cs`** -> AI Confidence: **99.31%**
1683. **`src/libraries/System.Net.Security/src/System/Net/CertificateValidationPal.Windows.cs`** -> AI Confidence: **99.31%**
1684. **`src/libraries/System.Net.Security/src/System/Net/NegotiateAuthenticationPal.ManagedSpnego.cs`** -> AI Confidence: **99.31%**
1685. **`src/libraries/System.Net.Security/src/System/Net/NegotiateAuthenticationPal.Unix.cs`** -> AI Confidence: **99.31%**
1686. **`src/libraries/System.Net.Security/src/System/Net/NegotiateAuthenticationPal.Windows.cs`** -> AI Confidence: **99.31%**
1687. **`src/libraries/System.Net.Security/src/System/Net/Security/CipherSuitesPolicyPal.Linux.cs`** -> AI Confidence: **99.31%**
1688. **`src/libraries/System.Net.Security/src/System/Net/Security/NegotiateStream.cs`** -> AI Confidence: **99.31%**
1689. **`src/libraries/System.Net.Security/src/System/Net/Security/Pal.Android/SafeDeleteSslContext.cs`** -> AI Confidence: **99.31%**
1690. **`src/libraries/System.Net.Security/src/System/Net/Security/Pal.OSX/SafeDeleteNwContext.cs`** -> AI Confidence: **99.31%**
1691. **`src/libraries/System.Net.Security/src/System/Net/Security/Pal.OSX/SafeDeleteSslContext.cs`** -> AI Confidence: **99.31%**
1692. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStream.IO.cs`** -> AI Confidence: **99.31%**
1693. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStream.cs`** -> AI Confidence: **99.31%**
1694. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStreamPal.OSX.cs`** -> AI Confidence: **99.31%**
1695. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStreamPal.Windows.cs`** -> AI Confidence: **99.31%**
1696. **`src/libraries/System.Net.Security/tests/StressTests/SslStress/Program.cs`** -> AI Confidence: **99.31%**
1697. **`src/libraries/System.Net.ServerSentEvents/src/System/Net/ServerSentEvents/SseParser_1.cs`** -> AI Confidence: **99.31%**
1698. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/Socket.Tasks.cs`** -> AI Confidence: **99.31%**
1699. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/Socket.Unix.cs`** -> AI Confidence: **99.31%**
1700. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/Socket.Windows.cs`** -> AI Confidence: **99.31%**
1701. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncContext.Unix.cs`** -> AI Confidence: **99.31%**
1702. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncEngine.Wasi.cs`** -> AI Confidence: **99.31%**
1703. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketPal.Unix.cs`** -> AI Confidence: **99.31%**
1704. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketPal.Windows.cs`** -> AI Confidence: **99.31%**
1705. **`src/libraries/System.Net.WebClient/src/System/Net/WebClient.cs`** -> AI Confidence: **99.31%**
1706. **`src/libraries/System.Net.WebHeaderCollection/src/System/Net/WebHeaderCollection.cs`** -> AI Confidence: **99.31%**
1707. **`src/libraries/System.Net.WebProxy/src/System/Net/WebProxy.cs`** -> AI Confidence: **99.31%**
1708. **`src/libraries/System.Net.WebSockets.Client/src/System/Net/WebSockets/ClientWebSocketOptions.cs`** -> AI Confidence: **99.31%**
1709. **`src/libraries/System.Net.WebSockets.Client/src/System/Net/WebSockets/WebSocketHandle.Managed.cs`** -> AI Confidence: **99.31%**
1710. **`src/libraries/System.Net.WebSockets.Client/tests/LoopbackServer/WebSocketHandshakeHelper.cs`** -> AI Confidence: **99.31%**
1711. **`src/libraries/System.Private.CoreLib/gen/IntrinsicsInSystemPrivateCoreLibAnalyzer.cs`** -> AI Confidence: **99.31%**
1712. **`src/libraries/System.Private.CoreLib/src/Internal/Runtime/InteropServices/ComponentActivator.cs`** -> AI Confidence: **99.31%**
1713. **`src/libraries/System.Private.CoreLib/src/Internal/Win32/RegistryKey.cs`** -> AI Confidence: **99.31%**
1714. **`src/libraries/System.Private.CoreLib/src/Microsoft/Win32/SafeHandles/SafeFileHandle.OverlappedValueTaskSource.Windows.cs`** -> AI Confidence: **99.31%**
1715. **`src/libraries/System.Private.CoreLib/src/Microsoft/Win32/SafeHandles/SafeFileHandle.ThreadPoolValueTaskSource.cs`** -> AI Confidence: **99.31%**
1716. **`src/libraries/System.Private.CoreLib/src/System/AppContext.cs`** -> AI Confidence: **99.31%**
1717. **`src/libraries/System.Private.CoreLib/src/System/AppDomain.cs`** -> AI Confidence: **99.31%**
1718. **`src/libraries/System.Private.CoreLib/src/System/Collections/BitArray.cs`** -> AI Confidence: **99.31%**
1719. **`src/libraries/System.Private.CoreLib/src/System/DateTime.cs`** -> AI Confidence: **99.31%**
1720. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/StackTrace.cs`** -> AI Confidence: **99.31%**
1721. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/EventProvider.cs`** -> AI Confidence: **99.31%**
1722. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/ManifestBuilder.cs`** -> AI Confidence: **99.31%**
1723. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/TraceLogging/TraceLoggingEventSource.cs`** -> AI Confidence: **99.31%**
1724. **`src/libraries/System.Private.CoreLib/src/System/Double.cs`** -> AI Confidence: **99.31%**
1725. **`src/libraries/System.Private.CoreLib/src/System/Enum.cs`** -> AI Confidence: **99.31%**
1726. **`src/libraries/System.Private.CoreLib/src/System/Environment.GetFolderPathCore.Unix.cs`** -> AI Confidence: **99.31%**
1727. **`src/libraries/System.Private.CoreLib/src/System/Exception.cs`** -> AI Confidence: **99.31%**
1728. **`src/libraries/System.Private.CoreLib/src/System/Globalization/CompareInfo.cs`** -> AI Confidence: **99.31%**
1729. **`src/libraries/System.Private.CoreLib/src/System/Globalization/CompareInfo.iOS.cs`** -> AI Confidence: **99.31%**
1730. **`src/libraries/System.Private.CoreLib/src/System/Globalization/Ordinal.Utf8.cs`** -> AI Confidence: **99.31%**
1731. **`src/libraries/System.Private.CoreLib/src/System/Globalization/Ordinal.cs`** -> AI Confidence: **99.31%**
1732. **`src/libraries/System.Private.CoreLib/src/System/IO/Enumeration/FileSystemEnumerator.Windows.cs`** -> AI Confidence: **99.31%**
1733. **`src/libraries/System.Private.CoreLib/src/System/IO/RandomAccess.Unix.cs`** -> AI Confidence: **99.31%**
1734. **`src/libraries/System.Private.CoreLib/src/System/IO/RandomAccess.Windows.cs`** -> AI Confidence: **99.31%**
1735. **`src/libraries/System.Private.CoreLib/src/System/IO/SharedMemoryManager.Unix.cs`** -> AI Confidence: **99.31%**
1736. **`src/libraries/System.Private.CoreLib/src/System/IO/Strategies/FileStreamHelpers.Windows.cs`** -> AI Confidence: **99.31%**
1737. **`src/libraries/System.Private.CoreLib/src/System/IO/Stream.cs`** -> AI Confidence: **99.31%**
1738. **`src/libraries/System.Private.CoreLib/src/System/IO/StreamReader.cs`** -> AI Confidence: **99.31%**
1739. **`src/libraries/System.Private.CoreLib/src/System/IO/StreamWriter.cs`** -> AI Confidence: **99.31%**
1740. **`src/libraries/System.Private.CoreLib/src/System/Int128.cs`** -> AI Confidence: **99.31%**
1741. **`src/libraries/System.Private.CoreLib/src/System/Int16.cs`** -> AI Confidence: **99.31%**
1742. **`src/libraries/System.Private.CoreLib/src/System/Int32.cs`** -> AI Confidence: **99.31%**
1743. **`src/libraries/System.Private.CoreLib/src/System/Int64.cs`** -> AI Confidence: **99.31%**
1744. **`src/libraries/System.Private.CoreLib/src/System/IntPtr.cs`** -> AI Confidence: **99.31%**
1745. **`src/libraries/System.Private.CoreLib/src/System/Math.cs`** -> AI Confidence: **99.31%**
1746. **`src/libraries/System.Private.CoreLib/src/System/MathF.cs`** -> AI Confidence: **99.31%**
1747. **`src/libraries/System.Private.CoreLib/src/System/Memory.cs`** -> AI Confidence: **99.31%**
1748. **`src/libraries/System.Private.CoreLib/src/System/MemoryExtensions.cs`** -> AI Confidence: **99.31%**
1749. **`src/libraries/System.Private.CoreLib/src/System/Number.Formatting.cs`** -> AI Confidence: **99.31%**
1750. **`src/libraries/System.Private.CoreLib/src/System/Number.Parsing.cs`** -> AI Confidence: **99.31%**
1751. **`src/libraries/System.Private.CoreLib/src/System/ReadOnlyMemory.cs`** -> AI Confidence: **99.31%**
1752. **`src/libraries/System.Private.CoreLib/src/System/ReadOnlySpan.cs`** -> AI Confidence: **99.31%**
1753. **`src/libraries/System.Private.CoreLib/src/System/Reflection/Assembly.cs`** -> AI Confidence: **99.31%**
1754. **`src/libraries/System.Private.CoreLib/src/System/Reflection/AssemblyName.cs`** -> AI Confidence: **99.31%**
1755. **`src/libraries/System.Private.CoreLib/src/System/Resources/ResourceReader.cs`** -> AI Confidence: **99.31%**
1756. **`src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncMethodBuilderCore.cs`** -> AI Confidence: **99.31%**
1757. **`src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/ConditionalWeakTable.cs`** -> AI Confidence: **99.31%**
1758. **`src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/PoolingAsyncValueTaskMethodBuilderT.cs`** -> AI Confidence: **99.31%**
1759. **`src/libraries/System.Private.CoreLib/src/System/Runtime/InteropServices/ComWrappers.cs`** -> AI Confidence: **99.31%**
1760. **`src/libraries/System.Private.CoreLib/src/System/Runtime/InteropServices/Marshal.cs`** -> AI Confidence: **99.31%**
1761. **`src/libraries/System.Private.CoreLib/src/System/Runtime/InteropServices/NFloat.cs`** -> AI Confidence: **99.31%**
1762. **`src/libraries/System.Private.CoreLib/src/System/Runtime/InteropServices/TypeMapLazyDictionary.cs`** -> AI Confidence: **99.31%**
1763. **`src/libraries/System.Private.CoreLib/src/System/Runtime/Loader/AssemblyLoadContext.cs`** -> AI Confidence: **99.31%**
1764. **`src/libraries/System.Private.CoreLib/src/System/SByte.cs`** -> AI Confidence: **99.31%**
1765. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/ProbabilisticMap.cs`** -> AI Confidence: **99.31%**
1766. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/Strings/AsciiStringSearchValuesTeddyBase.cs`** -> AI Confidence: **99.31%**
1767. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/Strings/SingleStringSearchValuesThreeChars.cs`** -> AI Confidence: **99.31%**
1768. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/Strings/StringSearchValues.cs`** -> AI Confidence: **99.31%**
1769. **`src/libraries/System.Private.CoreLib/src/System/Single.cs`** -> AI Confidence: **99.31%**
1770. **`src/libraries/System.Private.CoreLib/src/System/StartupHookProvider.cs`** -> AI Confidence: **99.31%**
1771. **`src/libraries/System.Private.CoreLib/src/System/String.Comparison.cs`** -> AI Confidence: **99.31%**
1772. **`src/libraries/System.Private.CoreLib/src/System/String.Manipulation.cs`** -> AI Confidence: **99.31%**
1773. **`src/libraries/System.Private.CoreLib/src/System/Text/TranscodingStream.cs`** -> AI Confidence: **99.31%**
1774. **`src/libraries/System.Private.CoreLib/src/System/Threading/RegisteredWaitHandle.WindowsThreadPool.cs`** -> AI Confidence: **99.31%**
1775. **`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs`** -> AI Confidence: **99.31%**
1776. **`src/libraries/System.Private.CoreLib/src/System/Threading/Thread.Windows.cs`** -> AI Confidence: **99.31%**
1777. **`src/libraries/System.Private.CoreLib/src/System/Threading/Thread.cs`** -> AI Confidence: **99.31%**
1778. **`src/libraries/System.Private.CoreLib/src/System/Threading/ThreadPoolBoundHandle.WindowsThreadPool.cs`** -> AI Confidence: **99.31%**
1779. **`src/libraries/System.Private.CoreLib/src/System/Threading/ThreadPoolWorkQueue.cs`** -> AI Confidence: **99.31%**
1780. **`src/libraries/System.Private.CoreLib/src/System/ThrowHelper.cs`** -> AI Confidence: **99.31%**
1781. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.Unix.Android.cs`** -> AI Confidence: **99.31%**
1782. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.Unix.NonAndroid.cs`** -> AI Confidence: **99.31%**
1783. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.cs`** -> AI Confidence: **99.31%**
1784. **`src/libraries/System.Private.CoreLib/src/System/Type.cs`** -> AI Confidence: **99.31%**
1785. **`src/libraries/System.Private.CoreLib/src/System/UInt128.cs`** -> AI Confidence: **99.31%**
1786. **`src/libraries/System.Private.CoreLib/src/System/UInt16.cs`** -> AI Confidence: **99.31%**
1787. **`src/libraries/System.Private.CoreLib/src/System/UInt32.cs`** -> AI Confidence: **99.31%**
1788. **`src/libraries/System.Private.CoreLib/src/System/UInt64.cs`** -> AI Confidence: **99.31%**
1789. **`src/libraries/System.Private.CoreLib/src/System/UIntPtr.cs`** -> AI Confidence: **99.31%**
1790. **`src/libraries/System.Private.CoreLib/src/System/Version.cs`** -> AI Confidence: **99.31%**
1791. **`src/libraries/System.Private.CoreLib/src/System/WeakReference.T.cs`** -> AI Confidence: **99.31%**
1792. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ClassDataContract.cs`** -> AI Confidence: **99.31%**
1793. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/CodeGenerator.cs`** -> AI Confidence: **99.31%**
1794. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/CollectionDataContract.cs`** -> AI Confidence: **99.31%**
1795. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ContextAware.cs`** -> AI Confidence: **99.31%**
1796. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/DataContract.cs`** -> AI Confidence: **99.31%**
1797. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/EnumDataContract.cs`** -> AI Confidence: **99.31%**
1798. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/DataContractJsonSerializer.cs`** -> AI Confidence: **99.31%**
1799. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonClassDataContract.cs`** -> AI Confidence: **99.31%**
1800. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonCollectionDataContract.cs`** -> AI Confidence: **99.31%**
1801. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonDataContract.cs`** -> AI Confidence: **99.31%**
1802. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonFormatGeneratorStatics.cs`** -> AI Confidence: **99.31%**
1803. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonXmlDataContract.cs`** -> AI Confidence: **99.31%**
1804. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/XmlObjectSerializerReadContextComplexJson.cs`** -> AI Confidence: **99.31%**
1805. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/XmlObjectSerializerWriteContextComplexJson.cs`** -> AI Confidence: **99.31%**
1806. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/PrimitiveDataContract.cs`** -> AI Confidence: **99.31%**
1807. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ReflectionClassWriter.cs`** -> AI Confidence: **99.31%**
1808. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ReflectionReader.cs`** -> AI Confidence: **99.31%**
1809. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlDataContract.cs`** -> AI Confidence: **99.31%**
1810. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializer.cs`** -> AI Confidence: **99.31%**
1811. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializerContext.cs`** -> AI Confidence: **99.31%**
1812. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializerWriteContextComplex.cs`** -> AI Confidence: **99.31%**
1813. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBaseReader.cs`** -> AI Confidence: **99.31%**
1814. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBinaryWriterSession.cs`** -> AI Confidence: **99.31%**
1815. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBufferReader.cs`** -> AI Confidence: **99.31%**
1816. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlConverter.cs`** -> AI Confidence: **99.31%**
1817. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlDictionaryAsyncCheckWriter.cs`** -> AI Confidence: **99.31%**
1818. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlDictionaryReader.cs`** -> AI Confidence: **99.31%**
1819. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlNodeWriter.cs`** -> AI Confidence: **99.31%**
1820. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlStreamNodeWriter.cs`** -> AI Confidence: **99.31%**
1821. **`src/libraries/System.Private.Uri/src/System/UriExt.cs`** -> AI Confidence: **99.31%**
1822. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/XElement.cs`** -> AI Confidence: **99.31%**
1823. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/XNode.cs`** -> AI Confidence: **99.31%**
1824. **`src/libraries/System.Private.Xml.Linq/tests/Properties/XElement_Value.cs`** -> AI Confidence: **99.31%**
1825. **`src/libraries/System.Private.Xml.Linq/tests/Schema/ExtensionTests.cs`** -> AI Confidence: **99.31%**
1826. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/AddFirstAddFirstIntoDocument.cs`** -> AI Confidence: **99.31%**
1827. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/ParamsObjectsCreation.cs`** -> AI Confidence: **99.31%**
1828. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/XAttributeEnumRemove.cs`** -> AI Confidence: **99.31%**
1829. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/XContainerAddIntoDocument.cs`** -> AI Confidence: **99.31%**
1830. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/HelperExtensionMethods.cs`** -> AI Confidence: **99.31%**
1831. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/FunctionalTests.cs`** -> AI Confidence: **99.31%**
1832. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/OmitDuplicatesAnnotation.cs`** -> AI Confidence: **99.31%**
1833. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/SaveOptions_OmitDuplicateNamespace.cs`** -> AI Confidence: **99.31%**
1834. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/XmlReaderDiff.cs`** -> AI Confidence: **99.31%**
1835. **`src/libraries/System.Private.Xml/src/System/Xml/BinaryXml/SqlUtils.cs`** -> AI Confidence: **99.31%**
1836. **`src/libraries/System.Private.Xml/src/System/Xml/BinaryXml/XmlBinaryReader.cs`** -> AI Confidence: **99.31%**
1837. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlCharCheckingWriterAsync.cs`** -> AI Confidence: **99.31%**
1838. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlSubtreeReaderAsync.cs`** -> AI Confidence: **99.31%**
1839. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlValidatingReaderImpl.cs`** -> AI Confidence: **99.31%**
1840. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWellFormedWriterAsync.cs`** -> AI Confidence: **99.31%**
1841. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWriterSettings.cs`** -> AI Confidence: **99.31%**
1842. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XsdCachingReader.cs`** -> AI Confidence: **99.31%**
1843. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XsdCachingReaderAsync.cs`** -> AI Confidence: **99.31%**
1844. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XsdValidatingReaderAsync.cs`** -> AI Confidence: **99.31%**
1845. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlElement.cs`** -> AI Confidence: **99.31%**
1846. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlNodeReader.cs`** -> AI Confidence: **99.31%**
1847. **`src/libraries/System.Private.Xml/src/System/Xml/Resolvers/XmlPreloadedResolver.cs`** -> AI Confidence: **99.31%**
1848. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/Asttree.cs`** -> AI Confidence: **99.31%**
1849. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/ConstraintStruct.cs`** -> AI Confidence: **99.31%**
1850. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/DataTypeImplementation.cs`** -> AI Confidence: **99.31%**
1851. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/DtdParserAsync.cs`** -> AI Confidence: **99.31%**
1852. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchema.cs`** -> AI Confidence: **99.31%**
1853. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/Compiler.cs`** -> AI Confidence: **99.31%**
1854. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/Mappings.cs`** -> AI Confidence: **99.31%**
1855. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/SchemaImporter.cs`** -> AI Confidence: **99.31%**
1856. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/Types.cs`** -> AI Confidence: **99.31%**
1857. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlAttributeOverrides.cs`** -> AI Confidence: **99.31%**
1858. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationGeneratedCode.cs`** -> AI Confidence: **99.31%**
1859. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationILGen.cs`** -> AI Confidence: **99.31%**
1860. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/Xmlcustomformatter.cs`** -> AI Confidence: **99.31%**
1861. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/CompiledXPathExpr.cs`** -> AI Confidence: **99.31%**
1862. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/Query.cs`** -> AI Confidence: **99.31%**
1863. **`src/libraries/System.Private.Xml/src/System/Xml/XmlConvert.cs`** -> AI Confidence: **99.31%**
1864. **`src/libraries/System.Private.Xml/src/System/Xml/XmlResolver.cs`** -> AI Confidence: **99.31%**
1865. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/IteratorDescriptor.cs`** -> AI Confidence: **99.31%**
1866. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/StaticDataManager.cs`** -> AI Confidence: **99.31%**
1867. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlILModule.cs`** -> AI Confidence: **99.31%**
1868. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlILOptimizerVisitor.cs`** -> AI Confidence: **99.31%**
1869. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlILTrace.cs`** -> AI Confidence: **99.31%**
1870. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlIlVisitor.cs`** -> AI Confidence: **99.31%**
1871. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/QIL/QilXmlWriter.cs`** -> AI Confidence: **99.31%**
1872. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/SetIterators.cs`** -> AI Confidence: **99.31%**
1873. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/WhitespaceRuleLookup.cs`** -> AI Confidence: **99.31%**
1874. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlExtensionFunction.cs`** -> AI Confidence: **99.31%**
1875. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlQueryContext.cs`** -> AI Confidence: **99.31%**
1876. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlQueryRuntime.cs`** -> AI Confidence: **99.31%**
1877. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XsltLibrary.cs`** -> AI Confidence: **99.31%**
1878. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XPath/XPathBuilder.cs`** -> AI Confidence: **99.31%**
1879. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XmlIlGenerator.cs`** -> AI Confidence: **99.31%**
1880. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XslException.cs`** -> AI Confidence: **99.31%**
1881. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/MatcherBuilder.cs`** -> AI Confidence: **99.31%**
1882. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/QilGenerator.cs`** -> AI Confidence: **99.31%**
1883. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/QilGeneratorEnv.cs`** -> AI Confidence: **99.31%**
1884. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/XPathPatternParser.cs`** -> AI Confidence: **99.31%**
1885. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/XslAst.cs`** -> AI Confidence: **99.31%**
1886. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/XslAstAnalyzer.cs`** -> AI Confidence: **99.31%**
1887. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/XsltLoader.cs`** -> AI Confidence: **99.31%**
1888. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ActionFrame.cs`** -> AI Confidence: **99.31%**
1889. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/BuilderInfo.cs`** -> AI Confidence: **99.31%**
1890. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/RootAction.cs`** -> AI Confidence: **99.31%**
1891. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/TemplateAction.cs`** -> AI Confidence: **99.31%**
1892. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/XsltCompileContext.cs`** -> AI Confidence: **99.31%**
1893. **`src/libraries/System.Private.Xml/tests/ExceptionVerifier.cs`** -> AI Confidence: **99.31%**
1894. **`src/libraries/System.Private.Xml/tests/Writers/RwFactory/CXmlDriverEngine.cs`** -> AI Confidence: **99.31%**
1895. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCFullEndElement.cs`** -> AI Confidence: **99.31%**
1896. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/Errata4.cs`** -> AI Confidence: **99.31%**
1897. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/XsltSettings.cs`** -> AI Confidence: **99.31%**
1898. **`src/libraries/System.Reflection.Emit/src/System/Reflection/Emit/MethodBuilderImpl.cs`** -> AI Confidence: **99.31%**
1899. **`src/libraries/System.Reflection.Emit/src/System/Reflection/Emit/ModuleBuilderImpl.cs`** -> AI Confidence: **99.31%**
1900. **`src/libraries/System.Reflection.Emit/tests/PersistedAssemblyBuilder/AssemblySaveCustomAttributeTests.cs`** -> AI Confidence: **99.31%**
1901. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/PortableExecutable/PEReader.EmbeddedPortablePdb.cs`** -> AI Confidence: **99.31%**
1902. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/PortableExecutable/PEReader.cs`** -> AI Confidence: **99.31%**
1903. **`src/libraries/System.Reflection.Metadata/tests/Metadata/TypeNameParserSamples.cs`** -> AI Confidence: **99.31%**
1904. **`src/libraries/System.Reflection.MetadataLoadContext/src/System/Reflection/TypeLoading/Assemblies/RoAssembly.cs`** -> AI Confidence: **99.31%**
1905. **`src/libraries/System.Reflection.MetadataLoadContext/tests/src/Tests/CustomAttributes/CustomAttributeTests.cs`** -> AI Confidence: **99.31%**
1906. **`src/libraries/System.Resources.Extensions/src/System/Resources/Extensions/BinaryFormat/BinaryFormattedObject.TypeResolver.cs`** -> AI Confidence: **99.31%**
1907. **`src/libraries/System.Resources.Extensions/src/System/Resources/Extensions/BinaryFormat/BinaryFormattedObject.cs`** -> AI Confidence: **99.31%**
1908. **`src/libraries/System.Resources.Extensions/tests/BinaryFormatTests/Legacy/BinaryFormatterTests.cs`** -> AI Confidence: **99.31%**
1909. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/CacheExpires.cs`** -> AI Confidence: **99.31%**
1910. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/HostFileChangeMonitor.cs`** -> AI Confidence: **99.31%**
1911. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCache.cs`** -> AI Confidence: **99.31%**
1912. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCacheEntry.cs`** -> AI Confidence: **99.31%**
1913. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCacheEntryChangeMonitor.cs`** -> AI Confidence: **99.31%**
1914. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCacheStatistics.cs`** -> AI Confidence: **99.31%**
1915. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCacheStore.cs`** -> AI Confidence: **99.31%**
1916. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/Interop/JavaScriptExports.CoreCLR.cs`** -> AI Confidence: **99.31%**
1917. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/JSHostImplementation.cs`** -> AI Confidence: **99.31%**
1918. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/Marshaling/JSMarshalerArgument.Task.cs`** -> AI Confidence: **99.31%**
1919. **`src/libraries/System.Runtime.InteropServices.JavaScript/tests/JSImportGenerator.UnitTest/Fails.cs`** -> AI Confidence: **99.31%**
1920. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/Analyzers/ComInterfaceGeneratorDiagnosticsAnalyzer.cs`** -> AI Confidence: **99.31%**
1921. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/Analyzers/RuntimeComApiUsageWithSourceGeneratedComAnalyzer.cs`** -> AI Confidence: **99.31%**
1922. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/Analyzers/VtableIndexStubDiagnosticsAnalyzer.cs`** -> AI Confidence: **99.31%**
1923. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/ComMethodInfo.cs`** -> AI Confidence: **99.31%**
1924. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/VtableIndexStubGenerator.cs`** -> AI Confidence: **99.31%**
1925. **`src/libraries/System.Runtime.InteropServices/gen/DownlevelLibraryImportGenerator/DownlevelLibraryImportDiagnosticsAnalyzer.cs`** -> AI Confidence: **99.31%**
1926. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/ConvertToLibraryImportFixer.cs`** -> AI Confidence: **99.31%**
1927. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/CustomMarshallerAttributeAnalyzer.cs`** -> AI Confidence: **99.31%**
1928. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/CustomMarshallerAttributeFixer.cs`** -> AI Confidence: **99.31%**
1929. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/LibraryImportDiagnosticsAnalyzer.cs`** -> AI Confidence: **99.31%**
1930. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/ShapeBreakingDiagnosticSuppressor.cs`** -> AI Confidence: **99.31%**
1931. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/ContainingSyntaxContext.cs`** -> AI Confidence: **99.31%**
1932. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/ManagedToNativeStubGenerator.cs`** -> AI Confidence: **99.31%**
1933. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/ManualTypeMarshallingHelper.cs`** -> AI Confidence: **99.31%**
1934. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/MarshalAsParser.cs`** -> AI Confidence: **99.31%**
1935. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/Marshalling/BoolMarshaller.cs`** -> AI Confidence: **99.31%**
1936. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/Marshalling/CharMarshaller.cs`** -> AI Confidence: **99.31%**
1937. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/Marshalling/MarshallerHelpers.cs`** -> AI Confidence: **99.31%**
1938. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/SyntaxExtensions.cs`** -> AI Confidence: **99.31%**
1939. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/TypeSymbolExtensions.cs`** -> AI Confidence: **99.31%**
1940. **`src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/CompileFails.cs`** -> AI Confidence: **99.31%**
1941. **`src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector128Tests.cs`** -> AI Confidence: **99.31%**
1942. **`src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector256Tests.cs`** -> AI Confidence: **99.31%**
1943. **`src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector64Tests.cs`** -> AI Confidence: **99.31%**
1944. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/BigInteger.cs`** -> AI Confidence: **99.31%**
1945. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/Complex.cs`** -> AI Confidence: **99.31%**
1946. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/FormatterServices.cs`** -> AI Confidence: **99.31%**
1947. **`src/libraries/System.Runtime.Serialization.Formatters/tests/EqualityExtensions.cs`** -> AI Confidence: **99.31%**
1948. **`src/libraries/System.Runtime.Serialization.Schema/src/System/Runtime/Serialization/Schema/ContractCodeDomInfo.cs`** -> AI Confidence: **99.31%**
1949. **`src/libraries/System.Runtime.Serialization.Schema/src/System/Runtime/Serialization/Schema/XsdDataContractImporter.cs`** -> AI Confidence: **99.31%**
1950. **`src/libraries/System.Runtime.Serialization.Xml/tests/SerializationTestTypes/DataContract.cs`** -> AI Confidence: **99.31%**
1951. **`src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.Context/Conformance.dynamic.context.method.regmethod.regclass.cs`** -> AI Confidence: **99.31%**
1952. **`src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.DynamicType/Conformance.dynamic.dynamicType.conversions.cs`** -> AI Confidence: **99.31%**
1953. **`src/libraries/System.Runtime/tests/System.Globalization.Tests/System/Globalization/GraphemeBreakTest.cs`** -> AI Confidence: **99.31%**
1954. **`src/libraries/System.Runtime/tests/System.IO.FileSystem.Tests/PortedCommon/CommonUtilities.cs`** -> AI Confidence: **99.31%**
1955. **`src/libraries/System.Runtime/tests/System.IO.FileSystem.Tests/PortedCommon/IOServices.cs`** -> AI Confidence: **99.31%**
1956. **`src/libraries/System.Runtime/tests/System.Runtime.InteropServices.RuntimeInformation.Tests/DescriptionNameTests.cs`** -> AI Confidence: **99.31%**
1957. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/Reflection/NullabilityInfoContextTests.cs`** -> AI Confidence: **99.31%**
1958. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/TimeZoneInfoTests.Common.cs`** -> AI Confidence: **99.31%**
1959. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/TimeZoneInfoTests.cs`** -> AI Confidence: **99.31%**
1960. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskRtTests_Core.cs`** -> AI Confidence: **99.31%**
1961. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskRunSyncTests.cs`** -> AI Confidence: **99.31%**
1962. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/TaskScheduler/TaskSchedulerTests.cs`** -> AI Confidence: **99.31%**
1963. **`src/libraries/System.Security.Claims/src/System/Security/Claims/ClaimsPrincipal.cs`** -> AI Confidence: **99.31%**
1964. **`src/libraries/System.Security.Cryptography.Cose/src/System/Security/Cryptography/Cose/CoseHelpers.cs`** -> AI Confidence: **99.31%**
1965. **`src/libraries/System.Security.Cryptography.Cose/src/System/Security/Cryptography/Cose/CoseMessage.cs`** -> AI Confidence: **99.31%**
1966. **`src/libraries/System.Security.Cryptography.Cose/src/System/Security/Cryptography/Cose/CoseMultiSignMessage.cs`** -> AI Confidence: **99.31%**
1967. **`src/libraries/System.Security.Cryptography.Cose/tests/CoseTestHelpers.cs`** -> AI Confidence: **99.31%**
1968. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/AsnHelpers.cs`** -> AI Confidence: **99.31%**
1969. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.Decrypt.cs`** -> AI Confidence: **99.31%**
1970. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.KeyTrans.cs`** -> AI Confidence: **99.31%**
1971. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/Windows/DecryptorPalWindows.Decrypt.cs`** -> AI Confidence: **99.31%**
1972. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/Windows/HelpersWindows.cs`** -> AI Confidence: **99.31%**
1973. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/Windows/PkcsPalWindows.Encrypt.cs`** -> AI Confidence: **99.31%**
1974. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/PkcsHelpers.cs`** -> AI Confidence: **99.31%**
1975. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/CmsSignature.RSA.cs`** -> AI Confidence: **99.31%**
1976. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/CmsSignature.cs`** -> AI Confidence: **99.31%**
1977. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/Rfc3161TimestampRequest.cs`** -> AI Confidence: **99.31%**
1978. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/Rfc3161TimestampToken.cs`** -> AI Confidence: **99.31%**
1979. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/Rfc3161TimestampTokenInfo.cs`** -> AI Confidence: **99.31%**
1980. **`src/libraries/System.Security.Cryptography.Pkcs/tests/Pkcs12/Pkcs12BuilderTests.cs`** -> AI Confidence: **99.31%**
1981. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/EncryptedXml.cs`** -> AI Confidence: **99.31%**
1982. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/SignedXml.cs`** -> AI Confidence: **99.31%**
1983. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/SignedXmlDebugLog.cs`** -> AI Confidence: **99.31%**
1984. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/CapiHelper.Windows.cs`** -> AI Confidence: **99.31%**
1985. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/CngHelpers.cs`** -> AI Confidence: **99.31%**
1986. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/CryptoStream.cs`** -> AI Confidence: **99.31%**
1987. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/HKDF.Windows.cs`** -> AI Confidence: **99.31%**
1988. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/Helpers.cs`** -> AI Confidence: **99.31%**
1989. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/Rfc2898DeriveBytes.cs`** -> AI Confidence: **99.31%**
1990. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/CertificateRequest.cs`** -> AI Confidence: **99.31%**
1991. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/ChainPal.Android.cs`** -> AI Confidence: **99.31%**
1992. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslCertificateAssetDownloader.cs`** -> AI Confidence: **99.31%**
1993. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslX509CertificateReader.cs`** -> AI Confidence: **99.31%**
1994. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslX509ChainProcessor.cs`** -> AI Confidence: **99.31%**
1995. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/PublicKey.cs`** -> AI Confidence: **99.31%**
1996. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/UnixExportProvider.cs`** -> AI Confidence: **99.31%**
1997. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509Certificate.cs`** -> AI Confidence: **99.31%**
1998. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509Certificate2.cs`** -> AI Confidence: **99.31%**
1999. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509Certificate2Collection.cs`** -> AI Confidence: **99.31%**
2000. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509CertificateLoader.macOS.cs`** -> AI Confidence: **99.31%**
2001. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509Pal.Windows.PublicKey.cs`** -> AI Confidence: **99.31%**
2002. **`src/libraries/System.Security.Principal.Windows/src/System/Security/Principal/SID.cs`** -> AI Confidence: **99.31%**
2003. **`src/libraries/System.Security.Principal.Windows/src/System/Security/Principal/WindowsIdentity.cs`** -> AI Confidence: **99.31%**
2004. **`src/libraries/System.ServiceModel.Syndication/tests/Utils/XmlDiff.cs`** -> AI Confidence: **99.31%**
2005. **`src/libraries/System.ServiceModel.Syndication/tests/Utils/XmlDiffDocument.cs`** -> AI Confidence: **99.31%**
2006. **`src/libraries/System.ServiceProcess.ServiceController/src/System/ServiceProcess/ServiceController.cs`** -> AI Confidence: **99.31%**
2007. **`src/libraries/System.Speech/src/Internal/ObjectToken/ObjectToken.cs`** -> AI Confidence: **99.31%**
2008. **`src/libraries/System.Speech/src/Internal/ObjectToken/RegistryDataKey.cs`** -> AI Confidence: **99.31%**
2009. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/CustomGrammar.cs`** -> AI Confidence: **99.31%**
2010. **`src/libraries/System.Speech/src/Internal/Synthesis/EngineSite.cs`** -> AI Confidence: **99.31%**
2011. **`src/libraries/System.Speech/src/Internal/Synthesis/TextFragmentEngine.cs`** -> AI Confidence: **99.31%**
2012. **`src/libraries/System.Speech/src/Recognition/GrammarBuilder.cs`** -> AI Confidence: **99.31%**
2013. **`src/libraries/System.Speech/src/Recognition/SpeechRecognitionEngine.cs`** -> AI Confidence: **99.31%**
2014. **`src/libraries/System.Speech/src/Recognition/SrgsGrammar/SrgsItem.cs`** -> AI Confidence: **99.31%**
2015. **`src/libraries/System.Speech/src/Recognition/SrgsGrammar/SrgsNameValueTag.cs`** -> AI Confidence: **99.31%**
2016. **`src/libraries/System.Speech/src/Recognition/SrgsGrammar/SrgsRule.cs`** -> AI Confidence: **99.31%**
2017. **`src/libraries/System.Speech/src/Result/RecognitionResult.cs`** -> AI Confidence: **99.31%**
2018. **`src/libraries/System.Speech/src/Synthesis/SpeechSynthesizer.cs`** -> AI Confidence: **99.31%**
2019. **`src/libraries/System.Speech/src/Synthesis/VoiceInfo.cs`** -> AI Confidence: **99.31%**
2020. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/BaseCodePageEncoding.cs`** -> AI Confidence: **99.31%**
2021. **`src/libraries/System.Text.Encodings.Web/src/System/Text/Encodings/Web/TextEncoder.cs`** -> AI Confidence: **99.31%**
2022. **`src/libraries/System.Text.Encodings.Web/tests/JavaScriptEncoderTests.cs`** -> AI Confidence: **99.31%**
2023. **`src/libraries/System.Text.Encodings.Web/tools/GenUnicodeRanges/Program.cs`** -> AI Confidence: **99.31%**
2024. **`src/libraries/System.Text.Json/gen/Helpers/KnownTypeSymbols.cs`** -> AI Confidence: **99.31%**
2025. **`src/libraries/System.Text.Json/gen/Helpers/RoslynExtensions.cs`** -> AI Confidence: **99.31%**
2026. **`src/libraries/System.Text.Json/gen/JsonSourceGenerator.Emitter.cs`** -> AI Confidence: **99.31%**
2027. **`src/libraries/System.Text.Json/gen/JsonSourceGenerator.Roslyn3.11.cs`** -> AI Confidence: **99.31%**
2028. **`src/libraries/System.Text.Json/src/System/Text/Json/JsonHelpers.cs`** -> AI Confidence: **99.31%**
2029. **`src/libraries/System.Text.Json/src/System/Text/Json/Schema/JsonSchemaExporter.cs`** -> AI Confidence: **99.31%**
2030. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Object/ObjectConverterFactory.cs`** -> AI Confidence: **99.31%**
2031. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Object/ObjectWithParameterizedConstructorConverter.cs`** -> AI Confidence: **99.31%**
2032. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Value/EnumConverter.cs`** -> AI Confidence: **99.31%**
2033. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonSerializer.Read.Pipe.cs`** -> AI Confidence: **99.31%**
2034. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonSerializer.Read.Stream.cs`** -> AI Confidence: **99.31%**
2035. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonSerializerOptions.Caching.cs`** -> AI Confidence: **99.31%**
2036. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonSerializerOptions.cs`** -> AI Confidence: **99.31%**
2037. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/ReadStackFrame.cs`** -> AI Confidence: **99.31%**
2038. **`src/libraries/System.Text.Json/tests/Common/JsonTestHelper.cs`** -> AI Confidence: **99.31%**
2039. **`src/libraries/System.Text.Json/tests/System.Text.Json.SourceGeneration.Tests/Serialization/CollectionTests.cs`** -> AI Confidence: **99.31%**
2040. **`src/libraries/System.Text.Json/tests/System.Text.Json.SourceGeneration.Tests/Serialization/JsonCreationHandlingTests.cs`** -> AI Confidence: **99.31%**
2041. **`src/libraries/System.Text.Json/tests/System.Text.Json.SourceGeneration.Tests/Serialization/JsonSchemaExporterTests.cs`** -> AI Confidence: **99.31%**
2042. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/JsonTestHelper.cs`** -> AI Confidence: **99.31%**
2043. **`src/libraries/System.Text.RegularExpressions/gen/RegexGenerator.Emitter.cs`** -> AI Confidence: **99.31%**
2044. **`src/libraries/System.Text.RegularExpressions/gen/RegexGenerator.Parser.cs`** -> AI Confidence: **99.31%**
2045. **`src/libraries/System.Text.RegularExpressions/gen/RegexGenerator.cs`** -> AI Confidence: **99.31%**
2046. **`src/libraries/System.Text.RegularExpressions/gen/UpgradeToGeneratedRegexCodeFixer.cs`** -> AI Confidence: **99.31%**
2047. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/Regex.cs`** -> AI Confidence: **99.31%**
2048. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexCompiler.cs`** -> AI Confidence: **99.31%**
2049. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/Regex.KnownPattern.Tests.cs`** -> AI Confidence: **99.31%**
2050. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/Regex.Match.Tests.cs`** -> AI Confidence: **99.31%**
2051. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/RegexExperiment.cs`** -> AI Confidence: **99.31%**
2052. **`src/libraries/System.Transactions.Local/src/System/Transactions/TransactionManager.cs`** -> AI Confidence: **99.31%**
2053. **`src/libraries/System.Transactions.Local/tests/AsyncTransactionScopeTests.cs`** -> AI Confidence: **99.31%**
2054. **`src/libraries/System.Windows.Extensions/src/System/Media/SoundPlayer.cs`** -> AI Confidence: **99.31%**
2055. **`src/mono/System.Private.CoreLib/src/System/Exception.Mono.cs`** -> AI Confidence: **99.31%**
2056. **`src/mono/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeAssemblyBuilder.Mono.cs`** -> AI Confidence: **99.31%**
2057. **`src/mono/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeModuleBuilder.Mono.cs`** -> AI Confidence: **99.31%**
2058. **`src/mono/System.Private.CoreLib/src/System/Reflection/RuntimeAssembly.cs`** -> AI Confidence: **99.31%**
2059. **`src/mono/System.Private.CoreLib/src/System/Reflection/RuntimeMethodInfo.Mono.cs`** -> AI Confidence: **99.31%**
2060. **`src/mono/System.Private.CoreLib/src/System/Reflection/RuntimePropertyInfo.cs`** -> AI Confidence: **99.31%**
2061. **`src/mono/System.Private.CoreLib/src/System/Runtime/Loader/AssemblyLoadContext.Mono.cs`** -> AI Confidence: **99.31%**
2062. **`src/mono/System.Private.CoreLib/src/System/RuntimeType.Mono.cs`** -> AI Confidence: **99.31%**
2063. **`src/mono/browser/debugger/BrowserDebugProxy/DebugStore.cs`** -> AI Confidence: **99.31%**
2064. **`src/mono/browser/debugger/BrowserDebugProxy/EvaluateExpression.cs`** -> AI Confidence: **99.31%**
2065. **`src/mono/browser/debugger/BrowserDebugProxy/JObjectValueCreator.cs`** -> AI Confidence: **99.31%**
2066. **`src/mono/browser/debugger/BrowserDebugProxy/MemberReferenceResolver.cs`** -> AI Confidence: **99.31%**
2067. **`src/mono/browser/debugger/BrowserDebugProxy/MetadataDebugSummary.cs`** -> AI Confidence: **99.31%**
2068. **`src/mono/browser/debugger/BrowserDebugProxy/MonoProxy.cs`** -> AI Confidence: **99.31%**
2069. **`src/mono/mono/tests/merp-crash-test.cs`** -> AI Confidence: **99.31%**
2070. **`src/mono/mono/tests/test-runner.cs`** -> AI Confidence: **99.31%**
2071. **`src/mono/mono/tests/verifier/AssemblyRunner.cs`** -> AI Confidence: **99.31%**
2072. **`src/mono/sample/wasm/simple-server/Program.cs`** -> AI Confidence: **99.31%**
2073. **`src/mono/wasm/Wasm.Build.Tests/AppSettingsTests.cs`** -> AI Confidence: **99.31%**
2074. **`src/mono/wasm/Wasm.Build.Tests/Blazor/BlazorWasmTestBase.cs`** -> AI Confidence: **99.31%**
2075. **`src/mono/wasm/Wasm.Build.Tests/BrowserRunner.cs`** -> AI Confidence: **99.31%**
2076. **`src/mono/wasm/Wasm.Build.Tests/Common/TestUtils.cs`** -> AI Confidence: **99.31%**
2077. **`src/mono/wasm/Wasm.Build.Tests/Common/Utils.cs`** -> AI Confidence: **99.31%**
2078. **`src/mono/wasm/Wasm.Build.Tests/IcuTestsBase.cs`** -> AI Confidence: **99.31%**
2079. **`src/mono/wasm/Wasm.Build.Tests/PInvokeTableGeneratorTests.cs`** -> AI Confidence: **99.31%**
2080. **`src/mono/wasm/Wasm.Build.Tests/ProjectProviderBase.cs`** -> AI Confidence: **99.31%**
2081. **`src/mono/wasm/Wasm.Build.Tests/Templates/WasmTemplateTests.cs`** -> AI Confidence: **99.31%**
2082. **`src/mono/wasm/Wasm.Build.Tests/WasmSdkBasedProjectProvider.cs`** -> AI Confidence: **99.31%**
2083. **`src/mono/wasm/host/Options.cs`** -> AI Confidence: **99.31%**
2084. **`src/mono/wasm/host/wasi/WasiEngineHost.cs`** -> AI Confidence: **99.31%**
2085. **`src/mono/wasm/symbolicator/WasmSymbolicator.cs`** -> AI Confidence: **99.31%**
2086. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/EcmaMetadata_1.cs`** -> AI Confidence: **99.31%**
2087. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/Loader_1.cs`** -> AI Confidence: **99.31%**
2088. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/StackWalk_1.cs`** -> AI Confidence: **99.31%**
2089. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataFrame.cs`** -> AI Confidence: **99.31%**
2090. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader/ContractDescriptorParser.cs`** -> AI Confidence: **99.31%**
2091. **`src/native/managed/cdac/tests/DumpTests/DumpTestBase.cs`** -> AI Confidence: **99.31%**
2092. **`src/native/managed/cdac/tests/DumpTests/StackWalkDumpTests.cs`** -> AI Confidence: **99.31%**
2093. **`src/native/managed/cdac/tests/MethodTableTests.cs`** -> AI Confidence: **99.31%**
2094. **`src/native/managed/cdac/tests/MockMemorySpace.cs`** -> AI Confidence: **99.31%**
2095. **`src/tasks/AotCompilerTask/MonoAOTCompiler.cs`** -> AI Confidence: **99.31%**
2096. **`src/tasks/AppleAppBuilder/Xcode.cs`** -> AI Confidence: **99.31%**
2097. **`src/tasks/AssemblyStripper/AssemblyStripper.cs`** -> AI Confidence: **99.31%**
2098. **`src/tasks/Common/FileCache.cs`** -> AI Confidence: **99.31%**
2099. **`src/tasks/LibraryBuilder/LibraryBuilder.cs`** -> AI Confidence: **99.31%**
2100. **`src/tasks/Microsoft.NET.Sdk.WebAssembly.Pack.Tasks/ComputeWasmBuildAssets.cs`** -> AI Confidence: **99.31%**
2101. **`src/tasks/Microsoft.NET.Sdk.WebAssembly.Pack.Tasks/GenerateWasmBootJson.cs`** -> AI Confidence: **99.31%**
2102. **`src/tasks/Microsoft.NET.WebAssembly.Webcil/WebcilReader.cs`** -> AI Confidence: **99.31%**
2103. **`src/tasks/MonoTargetsTasks/EmitBundleTask/EmitBundleBase.cs`** -> AI Confidence: **99.31%**
2104. **`src/tasks/MonoTargetsTasks/ILStrip/ILStrip.cs`** -> AI Confidence: **99.31%**
2105. **`src/tasks/WasmAppBuilder/EmccCompile.cs`** -> AI Confidence: **99.31%**
2106. **`src/tasks/WasmAppBuilder/IcallTableGenerator.cs`** -> AI Confidence: **99.31%**
2107. **`src/tasks/WasmAppBuilder/WasmAppBuilderBaseTask.cs`** -> AI Confidence: **99.31%**
2108. **`src/tasks/WasmAppBuilder/coreclr/ManagedToNativeGenerator.cs`** -> AI Confidence: **99.31%**
2109. **`src/tasks/WasmAppBuilder/coreclr/PInvokeCollector.cs`** -> AI Confidence: **99.31%**
2110. **`src/tasks/WasmAppBuilder/mono/ManagedToNativeGenerator.cs`** -> AI Confidence: **99.31%**
2111. **`src/tasks/WasmAppBuilder/mono/PInvokeCollector.cs`** -> AI Confidence: **99.31%**
2112. **`src/tasks/WasmBuildTasks/GenerateAOTProps.cs`** -> AI Confidence: **99.31%**
2113. **`src/tasks/WasmBuildTasks/UpdateChromeVersions.cs`** -> AI Confidence: **99.31%**
2114. **`src/tasks/WorkloadBuildTasks/PatchNuGetConfig.cs`** -> AI Confidence: **99.31%**
2115. **`src/tests/Common/CoreCLRTestLibrary/CoreclrTestWrapperLib.cs`** -> AI Confidence: **99.31%**
2116. **`src/tests/Common/CoreCLRTestLibrary/OutOfProcessTest.cs`** -> AI Confidence: **99.31%**
2117. **`src/tests/Common/XUnitLogChecker/XUnitLogChecker.cs`** -> AI Confidence: **99.31%**
2118. **`src/tests/Common/XUnitWrapperGenerator/ITestInfo.cs`** -> AI Confidence: **99.31%**
2119. **`src/tests/Common/XUnitWrapperGenerator/XUnitWrapperGenerator.cs`** -> AI Confidence: **99.31%**
2120. **`src/tests/GC/API/GC/GetTotalAllocatedBytes.cs`** -> AI Confidence: **99.31%**
2121. **`src/tests/Interop/MarshalAPI/IUnknown/IUnknownTest.cs`** -> AI Confidence: **99.31%**
2122. **`src/tests/Interop/NativeLibrary/API/GetMainProgramHandleTests.cs`** -> AI Confidence: **99.31%**
2123. **`src/tests/Interop/NativeLibrary/Callback/CallbackStressTest.cs`** -> AI Confidence: **99.31%**
2124. **`src/tests/Interop/SimpleStruct/SimpleStructManaged.cs`** -> AI Confidence: **99.31%**
2125. **`src/tests/Interop/StructMarshalling/ReversePInvoke/Helper.cs`** -> AI Confidence: **99.31%**
2126. **`src/tests/Interop/Swift/SwiftErrorHandling/SwiftErrorHandling.cs`** -> AI Confidence: **99.31%**
2127. **`src/tests/Interop/TypeMap/TypeMapApp.cs`** -> AI Confidence: **99.31%**
2128. **`src/tests/JIT/Directed/Convert/out_of_range_fp_to_int_conversions.cs`** -> AI Confidence: **99.31%**
2129. **`src/tests/JIT/HardwareIntrinsics/X86/General/VectorArray.cs`** -> AI Confidence: **99.31%**
2130. **`src/tests/JIT/HardwareIntrinsics/X86/Sse2.X64/StoreNonTemporal.cs`** -> AI Confidence: **99.31%**
2131. **`src/tests/JIT/HardwareIntrinsics/X86/Sse41/LoadAlignedVector128NonTemporal.cs`** -> AI Confidence: **99.31%**
2132. **`src/tests/JIT/HardwareIntrinsics/X86_Avx/Avx2/GatherMaskVector128.cs`** -> AI Confidence: **99.31%**
2133. **`src/tests/JIT/HardwareIntrinsics/X86_Avx/Avx2/GatherMaskVector256.cs`** -> AI Confidence: **99.31%**
2134. **`src/tests/JIT/HardwareIntrinsics/X86_Avx/Avx2/GatherVector128.cs`** -> AI Confidence: **99.31%**
2135. **`src/tests/JIT/HardwareIntrinsics/X86_Avx/Avx2/GatherVector256.cs`** -> AI Confidence: **99.31%**
2136. **`src/tests/JIT/IL_Conformance/Convert/TestConvertFromIntegral.cs`** -> AI Confidence: **99.31%**
2137. **`src/tests/JIT/Regression/CLR-x86-JIT/V2.0-Beta2/b425314/b425314.cs`** -> AI Confidence: **99.31%**
2138. **`src/tests/JIT/Regression/JitBlue/GitHub_23159/GitHub_23159.cs`** -> AI Confidence: **99.31%**
2139. **`src/tests/JIT/SIMD/CircleInConvex.cs`** -> AI Confidence: **99.31%**
2140. **`src/tests/JIT/SIMD/ShiftOperations.cs`** -> AI Confidence: **99.31%**
2141. **`src/tests/JIT/Stress/ABI/Gen.cs`** -> AI Confidence: **99.31%**
2142. **`src/tests/JIT/Stress/ABI/Program.cs`** -> AI Confidence: **99.31%**
2143. **`src/tests/JIT/Stress/ABI/Stubs.cs`** -> AI Confidence: **99.31%**
2144. **`src/tests/JIT/opt/SVE/ChangeMaskUse.cs`** -> AI Confidence: **99.31%**
2145. **`src/tests/JIT/opt/Structs/structcopies.cs`** -> AI Confidence: **99.31%**
2146. **`src/tests/Loader/CollectibleAssemblies/ResolvedFromDifferentContext/ResolvedFromDifferentContext.cs`** -> AI Confidence: **99.31%**
2147. **`src/tests/Loader/binding/tracing/BinderEventListener.cs`** -> AI Confidence: **99.31%**
2148. **`src/tests/Loader/binding/tracing/Helpers.cs`** -> AI Confidence: **99.31%**
2149. **`src/tests/Loader/classloader/DictionaryExpansion/DictionaryExpansion.cs`** -> AI Confidence: **99.31%**
2150. **`src/tests/Loader/classloader/generics/ByRefLike/Validate.cs`** -> AI Confidence: **99.31%**
2151. **`src/tests/async/eh-microbench/eh-microbench.cs`** -> AI Confidence: **99.31%**
2152. **`src/tests/baseservices/exceptions/exceptionstacktrace/exceptionstacktrace.cs`** -> AI Confidence: **99.31%**
2153. **`src/tests/baseservices/exceptions/stackoverflow/stackoverflowtester.cs`** -> AI Confidence: **99.31%**
2154. **`src/tests/readytorun/coreroot_determinism/Program.cs`** -> AI Confidence: **99.31%**
2155. **`src/tests/readytorun/tests/test.cs`** -> AI Confidence: **99.31%**
2156. **`src/tests/tracing/eventcounter/gh53564.cs`** -> AI Confidence: **99.31%**
2157. **`src/tests/tracing/eventcounter/regression-25709.cs`** -> AI Confidence: **99.31%**
2158. **`src/tests/tracing/eventcounter/runtimecounters.cs`** -> AI Confidence: **99.31%**
2159. **`src/tests/tracing/eventpipe/common/Microsoft.Diagnostics.NETCore.Client/DiagnosticsServerRouter/DiagnosticsServerRouterFactory.cs`** -> AI Confidence: **99.31%**
2160. **`src/tests/tracing/eventpipe/common/Reverse.cs`** -> AI Confidence: **99.31%**
2161. **`src/tests/tracing/eventpipe/randomizedallocationsampling/manual/AllocationProfiler/Program.cs`** -> AI Confidence: **99.31%**
2162. **`src/tests/tracing/runtimeeventsource/NativeRuntimeEventSourceTest.cs`** -> AI Confidence: **99.31%**
2163. **`src/tests/tracing/userevents/common/UserEventsTestRunner.cs`** -> AI Confidence: **99.31%**
2164. **`src/tools/StressLogAnalyzer/src/Program.cs`** -> AI Confidence: **99.31%**
2165. **`src/tools/ilasm/src/ILAssembler/GrammarVisitor.cs`** -> AI Confidence: **99.31%**
2166. **`src/tools/ilasm/src/ILAssembler/VTableExportPEBuilder.cs`** -> AI Confidence: **99.31%**
2167. **`src/tools/ilasm/src/ilasm/Program.cs`** -> AI Confidence: **99.31%**
2168. **`src/tools/illink/external/Mono.Options/Options.cs`** -> AI Confidence: **99.31%**
2169. **`src/tools/illink/src/ILLink.RoslynAnalyzer/DataFlow/ControlFlowGraphProxy.cs`** -> AI Confidence: **99.31%**
2170. **`src/tools/illink/src/ILLink.RoslynAnalyzer/DataFlow/FeatureChecksVisitor.cs`** -> AI Confidence: **99.31%**
2171. **`src/tools/illink/src/ILLink.RoslynAnalyzer/DataFlow/LocalDataFlowVisitor.cs`** -> AI Confidence: **99.31%**
2172. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/HandleCallAction.cs`** -> AI Confidence: **99.31%**
2173. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/ReflectionAccessAnalyzer.cs`** -> AI Confidence: **99.31%**
2174. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/TrimDataFlowAnalysis.cs`** -> AI Confidence: **99.31%**
2175. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/TypeNameResolver.cs`** -> AI Confidence: **99.31%**
2176. **`src/tools/illink/src/linker/Linker.Dataflow/CompilerGeneratedState.cs`** -> AI Confidence: **99.31%**
2177. **`src/tools/illink/src/linker/Linker.Dataflow/FlowAnnotations.cs`** -> AI Confidence: **99.31%**
2178. **`src/tools/illink/src/linker/Linker.Dataflow/HandleCallAction.cs`** -> AI Confidence: **99.31%**
2179. **`src/tools/illink/src/linker/Linker.Dataflow/MethodBodyScanner.cs`** -> AI Confidence: **99.31%**
2180. **`src/tools/illink/src/linker/Linker.Dataflow/ReflectionMarker.cs`** -> AI Confidence: **99.31%**
2181. **`src/tools/illink/src/linker/Linker.Steps/BodySubstitutionParser.cs`** -> AI Confidence: **99.31%**
2182. **`src/tools/illink/src/linker/Linker.Steps/DescriptorMarker.cs`** -> AI Confidence: **99.31%**
2183. **`src/tools/illink/src/linker/Linker.Steps/LinkAttributesParser.cs`** -> AI Confidence: **99.31%**
2184. **`src/tools/illink/src/linker/Linker.Steps/MarkStep.cs`** -> AI Confidence: **99.31%**
2185. **`src/tools/illink/src/linker/Linker.Steps/ProcessLinkerXmlBase.cs`** -> AI Confidence: **99.31%**
2186. **`src/tools/illink/src/linker/Linker/DocumentationSignatureParser.cs`** -> AI Confidence: **99.31%**
2187. **`src/tools/illink/src/linker/Linker/Driver.cs`** -> AI Confidence: **99.31%**
2188. **`src/tools/illink/src/linker/Linker/LinkContext.cs`** -> AI Confidence: **99.31%**
2189. **`src/tools/illink/src/linker/Linker/LinkerAttributesInformation.cs`** -> AI Confidence: **99.31%**
2190. **`src/tools/illink/src/linker/Linker/MessageContainer.cs`** -> AI Confidence: **99.31%**
2191. **`src/tools/illink/src/linker/Linker/TypeNameResolver.cs`** -> AI Confidence: **99.31%**
2192. **`src/tools/illink/src/linker/Linker/TypeReferenceExtensions.cs`** -> AI Confidence: **99.31%**
2193. **`src/tools/illink/test/ILLink.RoslynAnalyzer.Tests/CompilationExtensions.cs`** -> AI Confidence: **99.31%**
2194. **`src/tools/illink/test/Mono.Linker.Tests.Cases/RequiresCapability/RequiresAccessedThrough.cs`** -> AI Confidence: **99.31%**
2195. **`src/tools/illink/test/Mono.Linker.Tests/TestCasesRunner/MemberAssertionsCollector.cs`** -> AI Confidence: **99.31%**
2196. **`src/tools/illink/test/Mono.Linker.Tests/TestCasesRunner/ResultChecker.cs`** -> AI Confidence: **99.31%**
2197. **`src/mono/browser/runtime/assets.ts`** -> AI Confidence: **99.31%**
2198. **`src/mono/browser/runtime/diagnostics/diagnostics-js.ts`** -> AI Confidence: **99.31%**
2199. **`src/mono/browser/runtime/http.ts`** -> AI Confidence: **99.31%**
2200. **`src/mono/browser/runtime/invoke-js.ts`** -> AI Confidence: **99.31%**
2201. **`src/mono/browser/runtime/jiterpreter-interp-entry.ts`** -> AI Confidence: **99.31%**
2202. **`src/mono/browser/runtime/jiterpreter-jit-call.ts`** -> AI Confidence: **99.31%**
2203. **`src/mono/browser/runtime/jiterpreter-support.ts`** -> AI Confidence: **99.31%**
2204. **`src/mono/browser/runtime/jiterpreter.ts`** -> AI Confidence: **99.31%**
2205. **`src/mono/browser/runtime/loader/assets.ts`** -> AI Confidence: **99.31%**
2206. **`src/mono/browser/runtime/loader/run.ts`** -> AI Confidence: **99.31%**
2207. **`src/mono/browser/runtime/marshal-to-js.ts`** -> AI Confidence: **99.31%**
2208. **`src/mono/browser/runtime/pthreads/shared.ts`** -> AI Confidence: **99.31%**
2209. **`src/mono/browser/runtime/run.ts`** -> AI Confidence: **99.31%**
2210. **`src/mono/browser/runtime/web-socket.ts`** -> AI Confidence: **99.31%**
2211. **`src/native/libs/Common/JavaScript/loader/assets.ts`** -> AI Confidence: **99.31%**
2212. **`src/native/libs/System.Native.Browser/diagnostics/diagnostic-server-js.ts`** -> AI Confidence: **99.31%**
2213. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/http.ts`** -> AI Confidence: **99.31%**
2214. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/invoke-cs.ts`** -> AI Confidence: **99.31%**
2215. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/marshal-to-js.ts`** -> AI Confidence: **99.31%**
2216. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/web-socket.ts`** -> AI Confidence: **99.31%**
2217. **`.devcontainer/scripts/onCreateCommand.sh`** -> AI Confidence: **99.29%**
2218. **`.devcontainer/scripts/postCreateCommand.sh`** -> AI Confidence: **99.29%**
2219. **`eng/common/init-tools-native.sh`** -> AI Confidence: **99.29%**
2220. **`eng/native/genmoduleindex.sh`** -> AI Confidence: **99.29%**
2221. **`eng/testing/AndroidRunnerTemplate.sh`** -> AI Confidence: **99.29%**
2222. **`eng/testing/AppleRunnerTemplate.sh`** -> AI Confidence: **99.29%**
2223. **`eng/testing/WasiRunnerTemplate.sh`** -> AI Confidence: **99.29%**
2224. **`eng/testing/WasmRunnerTemplate.sh`** -> AI Confidence: **99.29%**
2225. **`src/coreclr/generateredefinesfile.sh`** -> AI Confidence: **99.29%**
2226. **`src/coreclr/nativeresources/processrc.sh`** -> AI Confidence: **99.29%**
2227. **`src/coreclr/pal/tools/gen-dactable-rva.sh`** -> AI Confidence: **99.29%**
2228. **`src/coreclr/pal/tools/setup-ubuntuvm.sh`** -> AI Confidence: **99.29%**
2229. **`src/coreclr/pal/tools/smarty.sh`** -> AI Confidence: **99.29%**
2230. **`src/libraries/Common/tests/System/Net/EnterpriseTests/setup/apacheweb/run.sh`** -> AI Confidence: **99.29%**
2231. **`src/libraries/System.Security.Cryptography/tests/osslplugins/build.sh`** -> AI Confidence: **99.29%**
2232. **`src/mono/mono/arch/arm/dpiops.sh`** -> AI Confidence: **99.29%**
2233. **`src/mono/mono/arch/arm/vfpops.sh`** -> AI Confidence: **99.29%**
2234. **`src/mono/mono/tests/verifier/make_access_test.sh`** -> AI Confidence: **99.29%**
2235. **`src/mono/mono/tests/verifier/make_bad_op_test.sh`** -> AI Confidence: **99.29%**
2236. **`src/mono/mono/tests/verifier/make_boxed_genarg_test.sh`** -> AI Confidence: **99.29%**
2237. **`src/mono/mono/tests/verifier/make_branch_test.sh`** -> AI Confidence: **99.29%**
2238. **`src/mono/mono/tests/verifier/make_call_test.sh`** -> AI Confidence: **99.29%**
2239. **`src/mono/mono/tests/verifier/make_cast_test.sh`** -> AI Confidence: **99.29%**
2240. **`src/mono/mono/tests/verifier/make_constrained_test.sh`** -> AI Confidence: **99.29%**
2241. **`src/mono/mono/tests/verifier/make_cross_nested_access_test.sh`** -> AI Confidence: **99.29%**
2242. **`src/mono/mono/tests/verifier/make_ctor_test.sh`** -> AI Confidence: **99.29%**
2243. **`src/mono/mono/tests/verifier/make_delegate_compat_test.sh`** -> AI Confidence: **99.29%**
2244. **`src/mono/mono/tests/verifier/make_double_nesting_test.sh`** -> AI Confidence: **99.29%**
2245. **`src/mono/mono/tests/verifier/make_exception_branch_test.sh`** -> AI Confidence: **99.29%**
2246. **`src/mono/mono/tests/verifier/make_exception_overlap_test.sh`** -> AI Confidence: **99.29%**
2247. **`src/mono/mono/tests/verifier/make_field_store_test.sh`** -> AI Confidence: **99.29%**
2248. **`src/mono/mono/tests/verifier/make_field_valuetype_test.sh`** -> AI Confidence: **99.29%**
2249. **`src/mono/mono/tests/verifier/make_generic_argument_constraints_test.sh`** -> AI Confidence: **99.29%**
2250. **`src/mono/mono/tests/verifier/make_il_overflow_test.sh`** -> AI Confidence: **99.29%**
2251. **`src/mono/mono/tests/verifier/make_invalid_ret_type.sh`** -> AI Confidence: **99.29%**
2252. **`src/mono/mono/tests/verifier/make_ldelem_test.sh`** -> AI Confidence: **99.29%**
2253. **`src/mono/mono/tests/verifier/make_ldelema_test.sh`** -> AI Confidence: **99.29%**
2254. **`src/mono/mono/tests/verifier/make_ldlen_test.sh`** -> AI Confidence: **99.29%**
2255. **`src/mono/mono/tests/verifier/make_load_indirect_test.sh`** -> AI Confidence: **99.29%**
2256. **`src/mono/mono/tests/verifier/make_localloc_test.sh`** -> AI Confidence: **99.29%**
2257. **`src/mono/mono/tests/verifier/make_method_constraint_test.sh`** -> AI Confidence: **99.29%**
2258. **`src/mono/mono/tests/verifier/make_nested_access_test.sh`** -> AI Confidence: **99.29%**
2259. **`src/mono/mono/tests/verifier/make_newobj_test.sh`** -> AI Confidence: **99.29%**
2260. **`src/mono/mono/tests/verifier/make_self_nested_test.sh`** -> AI Confidence: **99.29%**
2261. **`src/mono/mono/tests/verifier/make_stelem_test.sh`** -> AI Confidence: **99.29%**
2262. **`src/mono/mono/tests/verifier/make_tail_call_test.sh`** -> AI Confidence: **99.29%**
2263. **`src/mono/mono/tests/verifier/make_tests.sh`** -> AI Confidence: **99.29%**
2264. **`src/mono/mono/tests/verifier/make_throw_test.sh`** -> AI Confidence: **99.29%**
2265. **`src/mono/mono/tests/verifier/make_type_constraint_test.sh`** -> AI Confidence: **99.29%**
2266. **`src/mono/mono/tests/verifier/make_type_visibility_test.sh`** -> AI Confidence: **99.29%**
2267. **`src/mono/mono/tests/verifier/make_unbox_test.sh`** -> AI Confidence: **99.29%**
2268. **`src/native/external/libunwind/scripts/qemu-test-driver`** -> AI Confidence: **99.29%**
2269. **`src/native/external/libunwind/tests/check-namespace.sh.in`** -> AI Confidence: **99.29%**
2270. **`src/native/libs/build-native.sh`** -> AI Confidence: **99.29%**
2271. **`src/native/libs/verify-entrypoints.sh`** -> AI Confidence: **99.29%**
2272. **`src/native/libs/verify-so.sh`** -> AI Confidence: **99.29%**
2273. **`eng/collect_vsinfo.ps1`** -> AI Confidence: **99.29%**
2274. **`eng/common/dotnet-install.ps1`** -> AI Confidence: **99.29%**
2275. **`eng/common/dotnet.ps1`** -> AI Confidence: **99.29%**
2276. **`eng/common/generate-locproject.ps1`** -> AI Confidence: **99.29%**
2277. **`eng/common/internal-feed-operations.ps1`** -> AI Confidence: **99.29%**
2278. **`eng/common/pipeline-logging-functions.ps1`** -> AI Confidence: **99.29%**
2279. **`eng/common/sdk-task.ps1`** -> AI Confidence: **99.29%**
2280. **`eng/common/vmr-sync.ps1`** -> AI Confidence: **99.29%**
2281. **`eng/download-wasi-sdk.ps1`** -> AI Confidence: **99.29%**
2282. **`eng/extract-for-crossdac.ps1`** -> AI Confidence: **99.29%**
2283. **`eng/native/generateversionscript.ps1`** -> AI Confidence: **99.29%**
2284. **`eng/native/ijw/getRefPackFolderFromArtifacts.ps1`** -> AI Confidence: **99.29%**
2285. **`eng/native/sign-with-dac-certificate.ps1`** -> AI Confidence: **99.29%**
2286. **`eng/native/version/copy_version_files.ps1`** -> AI Confidence: **99.29%**
2287. **`eng/pipelines/mono/update-machine-certs.ps1`** -> AI Confidence: **99.29%**
2288. **`src/libraries/Common/tests/Scripts/Tools/ParallelTestExecution.ps1`** -> AI Confidence: **99.29%**
2289. **`src/libraries/Common/tests/System/Net/StressTests/build-local.ps1`** -> AI Confidence: **99.29%**
2290. **`src/coreclr/inc/log.h`** -> AI Confidence: **99.29%**
2291. **`src/mono/mono/metadata/gc-stats.c`** -> AI Confidence: **99.29%**
2292. **`src/mono/mono/mini/branch-opts.c`** -> AI Confidence: **99.29%**
2293. **`src/mono/mono/mini/mini-arm64-gsharedvt.c`** -> AI Confidence: **99.29%**
2294. **`src/mono/mono/mini/mini-x86-gsharedvt.c`** -> AI Confidence: **99.29%**
2295. **`src/mono/mono/mini/tramp-x86-gsharedvt.c`** -> AI Confidence: **99.29%**
2296. **`src/mono/mono/sgen/sgen-qsort.h`** -> AI Confidence: **99.29%**
2297. **`src/mono/mono/utils/mono-hwcap-ppc.c`** -> AI Confidence: **99.29%**
2298. **`src/mono/mono/utils/mono-log-android.c`** -> AI Confidence: **99.29%**
2299. **`src/mono/mono/utils/mono-os-semaphore-win32.c`** -> AI Confidence: **99.29%**
2300. **`src/native/eventpipe/ds-portable-rid.c`** -> AI Confidence: **99.29%**
2301. **`src/native/external/brotli/c/enc/command.c`** -> AI Confidence: **99.29%**
2302. **`src/native/external/brotli/c/enc/fast_log.c`** -> AI Confidence: **99.29%**
2303. **`src/native/external/brotli/c/enc/utf8_util.c`** -> AI Confidence: **99.29%**
2304. **`src/native/external/libunwind/src/aarch64/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2305. **`src/native/external/libunwind/src/aarch64/Gregs.c`** -> AI Confidence: **99.29%**
2306. **`src/native/external/libunwind/src/aarch64/Gstash_frame.c`** -> AI Confidence: **99.29%**
2307. **`src/native/external/libunwind/src/aarch64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2308. **`src/native/external/libunwind/src/aarch64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2309. **`src/native/external/libunwind/src/aarch64/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2310. **`src/native/external/libunwind/src/aarch64/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2311. **`src/native/external/libunwind/src/aarch64/Lglobal.c`** -> AI Confidence: **99.29%**
2312. **`src/native/external/libunwind/src/aarch64/Linit.c`** -> AI Confidence: **99.29%**
2313. **`src/native/external/libunwind/src/aarch64/Linit_local.c`** -> AI Confidence: **99.29%**
2314. **`src/native/external/libunwind/src/aarch64/Linit_remote.c`** -> AI Confidence: **99.29%**
2315. **`src/native/external/libunwind/src/aarch64/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2316. **`src/native/external/libunwind/src/aarch64/Los-freebsd.c`** -> AI Confidence: **99.29%**
2317. **`src/native/external/libunwind/src/aarch64/Los-linux.c`** -> AI Confidence: **99.29%**
2318. **`src/native/external/libunwind/src/aarch64/Los-qnx.c`** -> AI Confidence: **99.29%**
2319. **`src/native/external/libunwind/src/aarch64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2320. **`src/native/external/libunwind/src/aarch64/Lregs.c`** -> AI Confidence: **99.29%**
2321. **`src/native/external/libunwind/src/aarch64/Lresume.c`** -> AI Confidence: **99.29%**
2322. **`src/native/external/libunwind/src/aarch64/Lstash_frame.c`** -> AI Confidence: **99.29%**
2323. **`src/native/external/libunwind/src/aarch64/Lstep.c`** -> AI Confidence: **99.29%**
2324. **`src/native/external/libunwind/src/aarch64/Ltrace.c`** -> AI Confidence: **99.29%**
2325. **`src/native/external/libunwind/src/aarch64/ucontext_i.h`** -> AI Confidence: **99.29%**
2326. **`src/native/external/libunwind/src/arm/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2327. **`src/native/external/libunwind/src/arm/Gregs.c`** -> AI Confidence: **99.29%**
2328. **`src/native/external/libunwind/src/arm/Gstash_frame.c`** -> AI Confidence: **99.29%**
2329. **`src/native/external/libunwind/src/arm/Gtrace.c`** -> AI Confidence: **99.29%**
2330. **`src/native/external/libunwind/src/arm/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2331. **`src/native/external/libunwind/src/arm/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2332. **`src/native/external/libunwind/src/arm/Lex_tables.c`** -> AI Confidence: **99.29%**
2333. **`src/native/external/libunwind/src/arm/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2334. **`src/native/external/libunwind/src/arm/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2335. **`src/native/external/libunwind/src/arm/Lglobal.c`** -> AI Confidence: **99.29%**
2336. **`src/native/external/libunwind/src/arm/Linit.c`** -> AI Confidence: **99.29%**
2337. **`src/native/external/libunwind/src/arm/Linit_local.c`** -> AI Confidence: **99.29%**
2338. **`src/native/external/libunwind/src/arm/Linit_remote.c`** -> AI Confidence: **99.29%**
2339. **`src/native/external/libunwind/src/arm/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2340. **`src/native/external/libunwind/src/arm/Los-freebsd.c`** -> AI Confidence: **99.29%**
2341. **`src/native/external/libunwind/src/arm/Los-linux.c`** -> AI Confidence: **99.29%**
2342. **`src/native/external/libunwind/src/arm/Los-other.c`** -> AI Confidence: **99.29%**
2343. **`src/native/external/libunwind/src/arm/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2344. **`src/native/external/libunwind/src/arm/Lregs.c`** -> AI Confidence: **99.29%**
2345. **`src/native/external/libunwind/src/arm/Lresume.c`** -> AI Confidence: **99.29%**
2346. **`src/native/external/libunwind/src/arm/Lstash_frame.c`** -> AI Confidence: **99.29%**
2347. **`src/native/external/libunwind/src/arm/Lstep.c`** -> AI Confidence: **99.29%**
2348. **`src/native/external/libunwind/src/arm/Ltrace.c`** -> AI Confidence: **99.29%**
2349. **`src/native/external/libunwind/src/arm/is_fpreg.c`** -> AI Confidence: **99.29%**
2350. **`src/native/external/libunwind/src/coredump/_UCD_access_reg_freebsd.c`** -> AI Confidence: **99.29%**
2351. **`src/native/external/libunwind/src/coredump/_UCD_access_reg_qnx.c`** -> AI Confidence: **99.29%**
2352. **`src/native/external/libunwind/src/dwarf/Gexpr.c`** -> AI Confidence: **99.29%**
2353. **`src/native/external/libunwind/src/dwarf/Lexpr.c`** -> AI Confidence: **99.29%**
2354. **`src/native/external/libunwind/src/dwarf/Lfde.c`** -> AI Confidence: **99.29%**
2355. **`src/native/external/libunwind/src/dwarf/Lfind_proc_info-lsb.c`** -> AI Confidence: **99.29%**
2356. **`src/native/external/libunwind/src/dwarf/Lfind_unwind_table.c`** -> AI Confidence: **99.29%**
2357. **`src/native/external/libunwind/src/dwarf/Lget_proc_info_in_range.c`** -> AI Confidence: **99.29%**
2358. **`src/native/external/libunwind/src/dwarf/Lparser.c`** -> AI Confidence: **99.29%**
2359. **`src/native/external/libunwind/src/dwarf/Lpe.c`** -> AI Confidence: **99.29%**
2360. **`src/native/external/libunwind/src/hppa/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2361. **`src/native/external/libunwind/src/hppa/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2362. **`src/native/external/libunwind/src/hppa/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2363. **`src/native/external/libunwind/src/hppa/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2364. **`src/native/external/libunwind/src/hppa/Lglobal.c`** -> AI Confidence: **99.29%**
2365. **`src/native/external/libunwind/src/hppa/Linit.c`** -> AI Confidence: **99.29%**
2366. **`src/native/external/libunwind/src/hppa/Linit_local.c`** -> AI Confidence: **99.29%**
2367. **`src/native/external/libunwind/src/hppa/Linit_remote.c`** -> AI Confidence: **99.29%**
2368. **`src/native/external/libunwind/src/hppa/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2369. **`src/native/external/libunwind/src/hppa/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2370. **`src/native/external/libunwind/src/hppa/Lregs.c`** -> AI Confidence: **99.29%**
2371. **`src/native/external/libunwind/src/hppa/Lresume.c`** -> AI Confidence: **99.29%**
2372. **`src/native/external/libunwind/src/hppa/Lstep.c`** -> AI Confidence: **99.29%**
2373. **`src/native/external/libunwind/src/ia64/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2374. **`src/native/external/libunwind/src/ia64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2375. **`src/native/external/libunwind/src/ia64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2376. **`src/native/external/libunwind/src/ia64/Lfind_unwind_table.c`** -> AI Confidence: **99.29%**
2377. **`src/native/external/libunwind/src/ia64/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2378. **`src/native/external/libunwind/src/ia64/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2379. **`src/native/external/libunwind/src/ia64/Lglobal.c`** -> AI Confidence: **99.29%**
2380. **`src/native/external/libunwind/src/ia64/Linit.c`** -> AI Confidence: **99.29%**
2381. **`src/native/external/libunwind/src/ia64/Linit_local.c`** -> AI Confidence: **99.29%**
2382. **`src/native/external/libunwind/src/ia64/Linit_remote.c`** -> AI Confidence: **99.29%**
2383. **`src/native/external/libunwind/src/ia64/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2384. **`src/native/external/libunwind/src/ia64/Lparser.c`** -> AI Confidence: **99.29%**
2385. **`src/native/external/libunwind/src/ia64/Lrbs.c`** -> AI Confidence: **99.29%**
2386. **`src/native/external/libunwind/src/ia64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2387. **`src/native/external/libunwind/src/ia64/Lregs.c`** -> AI Confidence: **99.29%**
2388. **`src/native/external/libunwind/src/ia64/Lresume.c`** -> AI Confidence: **99.29%**
2389. **`src/native/external/libunwind/src/ia64/Lscript.c`** -> AI Confidence: **99.29%**
2390. **`src/native/external/libunwind/src/ia64/Lstep.c`** -> AI Confidence: **99.29%**
2391. **`src/native/external/libunwind/src/ia64/Ltables.c`** -> AI Confidence: **99.29%**
2392. **`src/native/external/libunwind/src/loongarch64/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2393. **`src/native/external/libunwind/src/loongarch64/Gregs.c`** -> AI Confidence: **99.29%**
2394. **`src/native/external/libunwind/src/loongarch64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2395. **`src/native/external/libunwind/src/loongarch64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2396. **`src/native/external/libunwind/src/loongarch64/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2397. **`src/native/external/libunwind/src/loongarch64/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2398. **`src/native/external/libunwind/src/loongarch64/Lglobal.c`** -> AI Confidence: **99.29%**
2399. **`src/native/external/libunwind/src/loongarch64/Linit.c`** -> AI Confidence: **99.29%**
2400. **`src/native/external/libunwind/src/loongarch64/Linit_local.c`** -> AI Confidence: **99.29%**
2401. **`src/native/external/libunwind/src/loongarch64/Linit_remote.c`** -> AI Confidence: **99.29%**
2402. **`src/native/external/libunwind/src/loongarch64/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2403. **`src/native/external/libunwind/src/loongarch64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2404. **`src/native/external/libunwind/src/loongarch64/Lregs.c`** -> AI Confidence: **99.29%**
2405. **`src/native/external/libunwind/src/loongarch64/Lresume.c`** -> AI Confidence: **99.29%**
2406. **`src/native/external/libunwind/src/loongarch64/Lstep.c`** -> AI Confidence: **99.29%**
2407. **`src/native/external/libunwind/src/mi/Gput_dynamic_unwind_info.c`** -> AI Confidence: **99.29%**
2408. **`src/native/external/libunwind/src/mi/Gset_iterate_phdr_function.c`** -> AI Confidence: **99.29%**
2409. **`src/native/external/libunwind/src/mi/Laddress_validator.c`** -> AI Confidence: **99.29%**
2410. **`src/native/external/libunwind/src/mi/Ldestroy_addr_space.c`** -> AI Confidence: **99.29%**
2411. **`src/native/external/libunwind/src/mi/Ldyn-extract.c`** -> AI Confidence: **99.29%**
2412. **`src/native/external/libunwind/src/mi/Ldyn-remote.c`** -> AI Confidence: **99.29%**
2413. **`src/native/external/libunwind/src/mi/Lfind_dynamic_proc_info.c`** -> AI Confidence: **99.29%**
2414. **`src/native/external/libunwind/src/mi/Lget_accessors.c`** -> AI Confidence: **99.29%**
2415. **`src/native/external/libunwind/src/mi/Lget_elf_filename.c`** -> AI Confidence: **99.29%**
2416. **`src/native/external/libunwind/src/mi/Lget_fpreg.c`** -> AI Confidence: **99.29%**
2417. **`src/native/external/libunwind/src/mi/Lget_proc_info_by_ip.c`** -> AI Confidence: **99.29%**
2418. **`src/native/external/libunwind/src/mi/Lget_proc_name.c`** -> AI Confidence: **99.29%**
2419. **`src/native/external/libunwind/src/mi/Lget_reg.c`** -> AI Confidence: **99.29%**
2420. **`src/native/external/libunwind/src/mi/Lput_dynamic_unwind_info.c`** -> AI Confidence: **99.29%**
2421. **`src/native/external/libunwind/src/mi/Lset_cache_size.c`** -> AI Confidence: **99.29%**
2422. **`src/native/external/libunwind/src/mi/Lset_caching_policy.c`** -> AI Confidence: **99.29%**
2423. **`src/native/external/libunwind/src/mi/Lset_fpreg.c`** -> AI Confidence: **99.29%**
2424. **`src/native/external/libunwind/src/mi/Lset_iterate_phdr_function.c`** -> AI Confidence: **99.29%**
2425. **`src/native/external/libunwind/src/mi/Lset_reg.c`** -> AI Confidence: **99.29%**
2426. **`src/native/external/libunwind/src/mi/_ReadSLEB.c`** -> AI Confidence: **99.29%**
2427. **`src/native/external/libunwind/src/mi/strerror.c`** -> AI Confidence: **99.29%**
2428. **`src/native/external/libunwind/src/mips/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2429. **`src/native/external/libunwind/src/mips/Gregs.c`** -> AI Confidence: **99.29%**
2430. **`src/native/external/libunwind/src/mips/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2431. **`src/native/external/libunwind/src/mips/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2432. **`src/native/external/libunwind/src/mips/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2433. **`src/native/external/libunwind/src/mips/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2434. **`src/native/external/libunwind/src/mips/Lglobal.c`** -> AI Confidence: **99.29%**
2435. **`src/native/external/libunwind/src/mips/Linit.c`** -> AI Confidence: **99.29%**
2436. **`src/native/external/libunwind/src/mips/Linit_local.c`** -> AI Confidence: **99.29%**
2437. **`src/native/external/libunwind/src/mips/Linit_remote.c`** -> AI Confidence: **99.29%**
2438. **`src/native/external/libunwind/src/mips/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2439. **`src/native/external/libunwind/src/mips/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2440. **`src/native/external/libunwind/src/mips/Lregs.c`** -> AI Confidence: **99.29%**
2441. **`src/native/external/libunwind/src/mips/Lresume.c`** -> AI Confidence: **99.29%**
2442. **`src/native/external/libunwind/src/mips/Lstep.c`** -> AI Confidence: **99.29%**
2443. **`src/native/external/libunwind/src/mips/offsets.h`** -> AI Confidence: **99.29%**
2444. **`src/native/external/libunwind/src/ppc/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2445. **`src/native/external/libunwind/src/ppc/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2446. **`src/native/external/libunwind/src/ppc/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2447. **`src/native/external/libunwind/src/ppc/Linit_local.c`** -> AI Confidence: **99.29%**
2448. **`src/native/external/libunwind/src/ppc/Linit_remote.c`** -> AI Confidence: **99.29%**
2449. **`src/native/external/libunwind/src/ppc/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2450. **`src/native/external/libunwind/src/ppc/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2451. **`src/native/external/libunwind/src/ppc32/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2452. **`src/native/external/libunwind/src/ppc32/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2453. **`src/native/external/libunwind/src/ppc32/Lglobal.c`** -> AI Confidence: **99.29%**
2454. **`src/native/external/libunwind/src/ppc32/Linit.c`** -> AI Confidence: **99.29%**
2455. **`src/native/external/libunwind/src/ppc32/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2456. **`src/native/external/libunwind/src/ppc32/Lregs.c`** -> AI Confidence: **99.29%**
2457. **`src/native/external/libunwind/src/ppc32/Lresume.c`** -> AI Confidence: **99.29%**
2458. **`src/native/external/libunwind/src/ppc32/Lstep.c`** -> AI Confidence: **99.29%**
2459. **`src/native/external/libunwind/src/ppc64/Gregs.c`** -> AI Confidence: **99.29%**
2460. **`src/native/external/libunwind/src/ppc64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2461. **`src/native/external/libunwind/src/ppc64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2462. **`src/native/external/libunwind/src/ppc64/Lglobal.c`** -> AI Confidence: **99.29%**
2463. **`src/native/external/libunwind/src/ppc64/Linit.c`** -> AI Confidence: **99.29%**
2464. **`src/native/external/libunwind/src/ppc64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2465. **`src/native/external/libunwind/src/ppc64/Lregs.c`** -> AI Confidence: **99.29%**
2466. **`src/native/external/libunwind/src/ppc64/Lresume.c`** -> AI Confidence: **99.29%**
2467. **`src/native/external/libunwind/src/ppc64/Lstep.c`** -> AI Confidence: **99.29%**
2468. **`src/native/external/libunwind/src/riscv/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2469. **`src/native/external/libunwind/src/riscv/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2470. **`src/native/external/libunwind/src/riscv/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2471. **`src/native/external/libunwind/src/riscv/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2472. **`src/native/external/libunwind/src/riscv/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2473. **`src/native/external/libunwind/src/riscv/Lglobal.c`** -> AI Confidence: **99.29%**
2474. **`src/native/external/libunwind/src/riscv/Linit.c`** -> AI Confidence: **99.29%**
2475. **`src/native/external/libunwind/src/riscv/Linit_local.c`** -> AI Confidence: **99.29%**
2476. **`src/native/external/libunwind/src/riscv/Linit_remote.c`** -> AI Confidence: **99.29%**
2477. **`src/native/external/libunwind/src/riscv/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2478. **`src/native/external/libunwind/src/riscv/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2479. **`src/native/external/libunwind/src/riscv/Lregs.c`** -> AI Confidence: **99.29%**
2480. **`src/native/external/libunwind/src/riscv/Lresume.c`** -> AI Confidence: **99.29%**
2481. **`src/native/external/libunwind/src/riscv/Lstep.c`** -> AI Confidence: **99.29%**
2482. **`src/native/external/libunwind/src/riscv/asm.h`** -> AI Confidence: **99.29%**
2483. **`src/native/external/libunwind/src/riscv/offsets.h`** -> AI Confidence: **99.29%**
2484. **`src/native/external/libunwind/src/s390x/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2485. **`src/native/external/libunwind/src/s390x/Gregs.c`** -> AI Confidence: **99.29%**
2486. **`src/native/external/libunwind/src/s390x/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2487. **`src/native/external/libunwind/src/s390x/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2488. **`src/native/external/libunwind/src/s390x/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2489. **`src/native/external/libunwind/src/s390x/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2490. **`src/native/external/libunwind/src/s390x/Linit.c`** -> AI Confidence: **99.29%**
2491. **`src/native/external/libunwind/src/s390x/Linit_local.c`** -> AI Confidence: **99.29%**
2492. **`src/native/external/libunwind/src/s390x/Linit_remote.c`** -> AI Confidence: **99.29%**
2493. **`src/native/external/libunwind/src/s390x/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2494. **`src/native/external/libunwind/src/s390x/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2495. **`src/native/external/libunwind/src/s390x/Lregs.c`** -> AI Confidence: **99.29%**
2496. **`src/native/external/libunwind/src/s390x/Lresume.c`** -> AI Confidence: **99.29%**
2497. **`src/native/external/libunwind/src/s390x/Lstep.c`** -> AI Confidence: **99.29%**
2498. **`src/native/external/libunwind/src/setjmp/siglongjmp.c`** -> AI Confidence: **99.29%**
2499. **`src/native/external/libunwind/src/sh/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2500. **`src/native/external/libunwind/src/sh/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2501. **`src/native/external/libunwind/src/sh/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2502. **`src/native/external/libunwind/src/sh/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2503. **`src/native/external/libunwind/src/sh/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2504. **`src/native/external/libunwind/src/sh/Lglobal.c`** -> AI Confidence: **99.29%**
2505. **`src/native/external/libunwind/src/sh/Linit.c`** -> AI Confidence: **99.29%**
2506. **`src/native/external/libunwind/src/sh/Linit_local.c`** -> AI Confidence: **99.29%**
2507. **`src/native/external/libunwind/src/sh/Linit_remote.c`** -> AI Confidence: **99.29%**
2508. **`src/native/external/libunwind/src/sh/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2509. **`src/native/external/libunwind/src/sh/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2510. **`src/native/external/libunwind/src/sh/Lregs.c`** -> AI Confidence: **99.29%**
2511. **`src/native/external/libunwind/src/sh/Lresume.c`** -> AI Confidence: **99.29%**
2512. **`src/native/external/libunwind/src/sh/Lstep.c`** -> AI Confidence: **99.29%**
2513. **`src/native/external/libunwind/src/x86/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2514. **`src/native/external/libunwind/src/x86/Gregs.c`** -> AI Confidence: **99.29%**
2515. **`src/native/external/libunwind/src/x86/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2516. **`src/native/external/libunwind/src/x86/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2517. **`src/native/external/libunwind/src/x86/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2518. **`src/native/external/libunwind/src/x86/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2519. **`src/native/external/libunwind/src/x86/Lglobal.c`** -> AI Confidence: **99.29%**
2520. **`src/native/external/libunwind/src/x86/Linit.c`** -> AI Confidence: **99.29%**
2521. **`src/native/external/libunwind/src/x86/Linit_local.c`** -> AI Confidence: **99.29%**
2522. **`src/native/external/libunwind/src/x86/Linit_remote.c`** -> AI Confidence: **99.29%**
2523. **`src/native/external/libunwind/src/x86/Los-freebsd.c`** -> AI Confidence: **99.29%**
2524. **`src/native/external/libunwind/src/x86/Los-linux.c`** -> AI Confidence: **99.29%**
2525. **`src/native/external/libunwind/src/x86/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2526. **`src/native/external/libunwind/src/x86/Lregs.c`** -> AI Confidence: **99.29%**
2527. **`src/native/external/libunwind/src/x86/Lresume.c`** -> AI Confidence: **99.29%**
2528. **`src/native/external/libunwind/src/x86/Lstep.c`** -> AI Confidence: **99.29%**
2529. **`src/native/external/libunwind/src/x86/is_fpreg.c`** -> AI Confidence: **99.29%**
2530. **`src/native/external/libunwind/src/x86_64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2531. **`src/native/external/libunwind/src/x86_64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2532. **`src/native/external/libunwind/src/x86_64/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2533. **`src/native/external/libunwind/src/x86_64/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2534. **`src/native/external/libunwind/src/x86_64/Linit.c`** -> AI Confidence: **99.29%**
2535. **`src/native/external/libunwind/src/x86_64/Linit_local.c`** -> AI Confidence: **99.29%**
2536. **`src/native/external/libunwind/src/x86_64/Linit_remote.c`** -> AI Confidence: **99.29%**
2537. **`src/native/external/libunwind/src/x86_64/Los-freebsd.c`** -> AI Confidence: **99.29%**
2538. **`src/native/external/libunwind/src/x86_64/Los-linux.c`** -> AI Confidence: **99.29%**
2539. **`src/native/external/libunwind/src/x86_64/Los-qnx.c`** -> AI Confidence: **99.29%**
2540. **`src/native/external/libunwind/src/x86_64/Los-solaris.c`** -> AI Confidence: **99.29%**
2541. **`src/native/external/libunwind/src/x86_64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2542. **`src/native/external/libunwind/src/x86_64/Lregs.c`** -> AI Confidence: **99.29%**
2543. **`src/native/external/libunwind/src/x86_64/Lresume.c`** -> AI Confidence: **99.29%**
2544. **`src/native/external/libunwind/src/x86_64/Lstash_frame.c`** -> AI Confidence: **99.29%**
2545. **`src/native/external/libunwind/src/x86_64/Lstep.c`** -> AI Confidence: **99.29%**
2546. **`src/native/external/libunwind/src/x86_64/Ltrace.c`** -> AI Confidence: **99.29%**
2547. **`src/native/external/libunwind/tests/Gia64-test-stack.c`** -> AI Confidence: **99.29%**
2548. **`src/native/external/libunwind/tests/Larm64-test-sve-signal.c`** -> AI Confidence: **99.29%**
2549. **`src/native/external/libunwind/tests/Lia64-test-nat.c`** -> AI Confidence: **99.29%**
2550. **`src/native/external/libunwind/tests/Lia64-test-rbs.c`** -> AI Confidence: **99.29%**
2551. **`src/native/external/libunwind/tests/Lia64-test-readonly.c`** -> AI Confidence: **99.29%**
2552. **`src/native/external/libunwind/tests/Lia64-test-stack.c`** -> AI Confidence: **99.29%**
2553. **`src/native/external/libunwind/tests/Lperf-simple.c`** -> AI Confidence: **99.29%**
2554. **`src/native/external/libunwind/tests/Lperf-trace.c`** -> AI Confidence: **99.29%**
2555. **`src/native/external/libunwind/tests/Ltest-bt.c`** -> AI Confidence: **99.29%**
2556. **`src/native/external/libunwind/tests/Ltest-concurrent.c`** -> AI Confidence: **99.29%**
2557. **`src/native/external/libunwind/tests/Ltest-dyn1.c`** -> AI Confidence: **99.29%**
2558. **`src/native/external/libunwind/tests/Ltest-exc.c`** -> AI Confidence: **99.29%**
2559. **`src/native/external/libunwind/tests/Ltest-nomalloc.c`** -> AI Confidence: **99.29%**
2560. **`src/native/external/libunwind/tests/Ltest-resume-sig-rt.c`** -> AI Confidence: **99.29%**
2561. **`src/native/external/libunwind/tests/Ltest-resume-sig.c`** -> AI Confidence: **99.29%**
2562. **`src/native/external/libunwind/tests/Ltest-trace.c`** -> AI Confidence: **99.29%**
2563. **`src/native/external/libunwind/tests/Lx64-test-dwarf-expressions.c`** -> AI Confidence: **99.29%**
2564. **`src/native/external/llvm-libunwind/src/assembly.h`** -> AI Confidence: **99.29%**
2565. **`src/native/external/zlib-ng/arch/arm/crc32_acle.c`** -> AI Confidence: **99.29%**
2566. **`src/native/external/zlib-ng/arch/riscv/chunkset_rvv.c`** -> AI Confidence: **99.29%**
2567. **`src/native/external/zlib-ng/cmake/detect-arch.c`** -> AI Confidence: **99.29%**
2568. **`src/native/external/zlib-ng/deflate_fast.c`** -> AI Confidence: **99.29%**
2569. **`src/native/external/zlib-ng/deflate_slow.c`** -> AI Confidence: **99.29%**
2570. **`src/native/external/zlib-ng/deflate_stored.c`** -> AI Confidence: **99.29%**
2571. **`src/native/external/zlib-ng/uncompr.c`** -> AI Confidence: **99.29%**
2572. **`src/native/external/zstd/lib/common/debug.c`** -> AI Confidence: **99.29%**
2573. **`src/native/external/zstd/lib/compress/zstd_double_fast.c`** -> AI Confidence: **99.29%**
2574. **`src/native/external/zstd/lib/compress/zstd_fast.c`** -> AI Confidence: **99.29%**
2575. **`src/native/libs/System.Security.Cryptography.Native.Android/pal_pbkdf2.c`** -> AI Confidence: **99.29%**
2576. **`src/native/libs/System.Security.Cryptography.Native.Apple/pal_ecc.c`** -> AI Confidence: **99.29%**
2577. **`src/native/libs/System.Security.Cryptography.Native/pal_ecc_import_export.c`** -> AI Confidence: **99.29%**
2578. **`src/coreclr/dlls/mscorrc/resource.h`** -> AI Confidence: **99.29%**
2579. **`src/coreclr/gc/gceesvr.cpp`** -> AI Confidence: **99.29%**
2580. **`src/coreclr/gc/memory.cpp`** -> AI Confidence: **99.29%**
2581. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.AVX2.int32_t.generated.cpp`** -> AI Confidence: **99.29%**
2582. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.AVX2.int64_t.generated.cpp`** -> AI Confidence: **99.29%**
2583. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.AVX512.int32_t.generated.cpp`** -> AI Confidence: **99.29%**
2584. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.AVX512.int64_t.generated.cpp`** -> AI Confidence: **99.29%**
2585. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.NEON.uint32_t.generated.cpp`** -> AI Confidence: **99.29%**
2586. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.scalar.uint64_t.generated.cpp`** -> AI Confidence: **99.29%**
2587. **`src/coreclr/gcdump/gcdump.cpp`** -> AI Confidence: **99.29%**
2588. **`src/coreclr/gcdump/i386/gcdumpx86.cpp`** -> AI Confidence: **99.29%**
2589. **`src/coreclr/gcinfo/gcinfodumper.cpp`** -> AI Confidence: **99.29%**
2590. **`src/coreclr/ilasm/assembler.cpp`** -> AI Confidence: **99.29%**
2591. **`src/coreclr/ilasm/grammar_after.cpp`** -> AI Confidence: **99.29%**
2592. **`src/coreclr/ilasm/main.cpp`** -> AI Confidence: **99.29%**
2593. **`src/coreclr/ilasm/writer.cpp`** -> AI Confidence: **99.29%**
2594. **`src/coreclr/inc/dacvars.h`** -> AI Confidence: **99.29%**
2595. **`src/coreclr/inc/formattype.cpp`** -> AI Confidence: **99.29%**
2596. **`src/coreclr/inc/vptr_list.h`** -> AI Confidence: **99.29%**
2597. **`src/coreclr/jit/buildstring.cpp`** -> AI Confidence: **99.29%**
2598. **`src/coreclr/jit/codegenwasm.cpp`** -> AI Confidence: **99.29%**
2599. **`src/coreclr/jit/debuginfo.cpp`** -> AI Confidence: **99.29%**
2600. **`src/coreclr/jit/decomposelongs.cpp`** -> AI Confidence: **99.29%**
2601. **`src/coreclr/jit/disasm.cpp`** -> AI Confidence: **99.29%**
2602. **`src/coreclr/jit/earlyprop.cpp`** -> AI Confidence: **99.29%**
2603. **`src/coreclr/jit/emitarm64sve.cpp`** -> AI Confidence: **99.29%**
2604. **`src/coreclr/jit/fgbasic.cpp`** -> AI Confidence: **99.29%**
2605. **`src/coreclr/jit/fgehopt.cpp`** -> AI Confidence: **99.29%**
2606. **`src/coreclr/jit/fgflow.cpp`** -> AI Confidence: **99.29%**
2607. **`src/coreclr/jit/fginline.cpp`** -> AI Confidence: **99.29%**
2608. **`src/coreclr/jit/fgopt.cpp`** -> AI Confidence: **99.29%**
2609. **`src/coreclr/jit/fgprofilesynthesis.cpp`** -> AI Confidence: **99.29%**
2610. **`src/coreclr/jit/gschecks.cpp`** -> AI Confidence: **99.29%**
2611. **`src/coreclr/jit/hwintrinsic.cpp`** -> AI Confidence: **99.29%**
2612. **`src/coreclr/jit/hwintrinsicarm64.cpp`** -> AI Confidence: **99.29%**
2613. **`src/coreclr/jit/hwintrinsiccodegenarm64.cpp`** -> AI Confidence: **99.29%**
2614. **`src/coreclr/jit/hwintrinsicxarch.cpp`** -> AI Confidence: **99.29%**
2615. **`src/coreclr/jit/importer.cpp`** -> AI Confidence: **99.29%**
2616. **`src/coreclr/jit/importercalls.cpp`** -> AI Confidence: **99.29%**
2617. **`src/coreclr/jit/jithashtable.cpp`** -> AI Confidence: **99.29%**
2618. **`src/coreclr/jit/jitmetadatalist.h`** -> AI Confidence: **99.29%**
2619. **`src/coreclr/jit/lclmorph.cpp`** -> AI Confidence: **99.29%**
2620. **`src/coreclr/jit/lowerxarch.cpp`** -> AI Confidence: **99.29%**
2621. **`src/coreclr/jit/lsrabuild.cpp`** -> AI Confidence: **99.29%**
2622. **`src/coreclr/jit/lsraxarch.cpp`** -> AI Confidence: **99.29%**
2623. **`src/coreclr/jit/morph.cpp`** -> AI Confidence: **99.29%**
2624. **`src/coreclr/jit/optimizer.cpp`** -> AI Confidence: **99.29%**
2625. **`src/coreclr/jit/phase.cpp`** -> AI Confidence: **99.29%**
2626. **`src/coreclr/jit/promotionliveness.cpp`** -> AI Confidence: **99.29%**
2627. **`src/coreclr/jit/rangecheck.cpp`** -> AI Confidence: **99.29%**
2628. **`src/coreclr/jit/rationalize.cpp`** -> AI Confidence: **99.29%**
2629. **`src/coreclr/jit/smcommon.cpp`** -> AI Confidence: **99.29%**
2630. **`src/coreclr/jit/stacklevelsetter.cpp`** -> AI Confidence: **99.29%**
2631. **`src/coreclr/jit/targetamd64.cpp`** -> AI Confidence: **99.29%**
2632. **`src/coreclr/jit/targetarm.cpp`** -> AI Confidence: **99.29%**
2633. **`src/coreclr/jit/targetarm64.cpp`** -> AI Confidence: **99.29%**
2634. **`src/coreclr/jit/targetloongarch64.cpp`** -> AI Confidence: **99.29%**
2635. **`src/coreclr/jit/targetx86.cpp`** -> AI Confidence: **99.29%**
2636. **`src/coreclr/jit/unwind.cpp`** -> AI Confidence: **99.29%**
2637. **`src/coreclr/jit/unwindamd64.cpp`** -> AI Confidence: **99.29%**
2638. **`src/coreclr/jit/unwindarm64.cpp`** -> AI Confidence: **99.29%**
2639. **`src/coreclr/jit/unwindarmarch.cpp`** -> AI Confidence: **99.29%**
2640. **`src/coreclr/jit/unwindloongarch64.cpp`** -> AI Confidence: **99.29%**
2641. **`src/coreclr/jitshared/histogram.cpp`** -> AI Confidence: **99.29%**
2642. **`src/coreclr/md/compiler/filtermanager.cpp`** -> AI Confidence: **99.29%**
2643. **`src/coreclr/md/runtime/metamodelcolumndefs.h`** -> AI Confidence: **99.29%**
2644. **`src/coreclr/minipal/Windows/dn-stdio.cpp`** -> AI Confidence: **99.29%**
2645. **`src/coreclr/nativeaot/Runtime/amd64/AsmOffsetsCpu.h`** -> AI Confidence: **99.29%**
2646. **`src/coreclr/nativeaot/Runtime/windows/AsmOffsets.cpp`** -> AI Confidence: **99.29%**
2647. **`src/coreclr/pal/inc/rt/imagehlp.h`** -> AI Confidence: **99.29%**
2648. **`src/coreclr/pal/src/arch/amd64/asmconstants.h`** -> AI Confidence: **99.29%**
2649. **`src/coreclr/pal/src/map/common.cpp`** -> AI Confidence: **99.29%**
2650. **`src/coreclr/pal/src/safecrt/tmakepath_s.inl`** -> AI Confidence: **99.29%**
2651. **`src/coreclr/pal/tests/palsuite/c_runtime/isdigit/test1/test1.cpp`** -> AI Confidence: **99.29%**
2652. **`src/coreclr/pal/tests/palsuite/c_runtime/iswprint/test1/test1.cpp`** -> AI Confidence: **99.29%**
2653. **`src/coreclr/pal/tests/palsuite/c_runtime/isxdigit/test1/test1.cpp`** -> AI Confidence: **99.29%**
2654. **`src/coreclr/pal/tests/palsuite/c_runtime/strcmp/test1/test1.cpp`** -> AI Confidence: **99.29%**
2655. **`src/coreclr/pal/tests/palsuite/c_runtime/strncmp/test1/test1.cpp`** -> AI Confidence: **99.29%**
2656. **`src/coreclr/pal/tests/palsuite/c_runtime/wcsstr/test1/test1.cpp`** -> AI Confidence: **99.29%**
2657. **`src/coreclr/pal/tests/palsuite/composite/object_management/event/nonshared/main.cpp`** -> AI Confidence: **99.29%**
2658. **`src/coreclr/pal/tests/palsuite/composite/object_management/event/shared/main.cpp`** -> AI Confidence: **99.29%**
2659. **`src/coreclr/pal/tests/palsuite/composite/object_management/semaphore/nonshared/main.cpp`** -> AI Confidence: **99.29%**
2660. **`src/coreclr/pal/tests/palsuite/composite/object_management/semaphore/shared/main.cpp`** -> AI Confidence: **99.29%**
2661. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test1/commonconsts.h`** -> AI Confidence: **99.29%**
2662. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test1/test1.cpp`** -> AI Confidence: **99.29%**
2663. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test3/commonconsts.h`** -> AI Confidence: **99.29%**
2664. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test3/test3.cpp`** -> AI Confidence: **99.29%**
2665. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test4/test4.cpp`** -> AI Confidence: **99.29%**
2666. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER/test1/PAL_EXCEPT_FILTER.cpp`** -> AI Confidence: **99.29%**
2667. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER/test2/pal_except_filter.cpp`** -> AI Confidence: **99.29%**
2668. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER_EX/test1/PAL_EXCEPT_FILTER_EX.cpp`** -> AI Confidence: **99.29%**
2669. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER_EX/test2/pal_except_filter_ex.cpp`** -> AI Confidence: **99.29%**
2670. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER_EX/test3/pal_except_filter.cpp`** -> AI Confidence: **99.29%**
2671. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_TRY_EXCEPT_EX/test1/PAL_TRY_EXCEPT_EX.cpp`** -> AI Confidence: **99.29%**
2672. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_TRY_EXCEPT_EX/test2/PAL_TRY_EXCEPT_EX.cpp`** -> AI Confidence: **99.29%**
2673. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_TRY_EXCEPT_EX/test3/PAL_TRY_EXCEPT_EX.cpp`** -> AI Confidence: **99.29%**
2674. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_TRY_LEAVE_FINALLY/test1/PAL_TRY_LEAVE_FINALLY.cpp`** -> AI Confidence: **99.29%**
2675. **`src/coreclr/pal/tests/palsuite/exception_handling/RaiseException/test1/test1.cpp`** -> AI Confidence: **99.29%**
2676. **`src/coreclr/pal/tests/palsuite/exception_handling/RaiseException/test2/test2.cpp`** -> AI Confidence: **99.29%**
2677. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test2/test2.cpp`** -> AI Confidence: **99.29%**
2678. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test3/test3.cpp`** -> AI Confidence: **99.29%**
2679. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test4/test4.cpp`** -> AI Confidence: **99.29%**
2680. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test5/test5.cpp`** -> AI Confidence: **99.29%**
2681. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test6/test6.cpp`** -> AI Confidence: **99.29%**
2682. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_finally/test1/pal_finally.cpp`** -> AI Confidence: **99.29%**
2683. **`src/coreclr/pal/tests/palsuite/file_io/FlushFileBuffers/test1/FlushFileBuffers.cpp`** -> AI Confidence: **99.29%**
2684. **`src/coreclr/pal/tests/palsuite/file_io/GetFileSize/test1/GetFileSize.cpp`** -> AI Confidence: **99.29%**
2685. **`src/coreclr/pal/tests/palsuite/file_io/GetFileSizeEx/test1/GetFileSizeEx.cpp`** -> AI Confidence: **99.29%**
2686. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameA/test1/GetFullPathNameA.cpp`** -> AI Confidence: **99.29%**
2687. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameA/test2/test2.cpp`** -> AI Confidence: **99.29%**
2688. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameA/test3/test3.cpp`** -> AI Confidence: **99.29%**
2689. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameA/test4/test4.cpp`** -> AI Confidence: **99.29%**
2690. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameW/test2/test2.cpp`** -> AI Confidence: **99.29%**
2691. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameW/test3/test3.cpp`** -> AI Confidence: **99.29%**
2692. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameW/test4/test4.cpp`** -> AI Confidence: **99.29%**
2693. **`src/coreclr/pal/tests/palsuite/file_io/GetStdHandle/test1/GetStdHandle.cpp`** -> AI Confidence: **99.29%**
2694. **`src/coreclr/pal/tests/palsuite/file_io/GetStdHandle/test2/GetStdHandle.cpp`** -> AI Confidence: **99.29%**
2695. **`src/coreclr/pal/tests/palsuite/file_io/ReadFile/test4/readfile.cpp`** -> AI Confidence: **99.29%**
2696. **`src/coreclr/pal/tests/palsuite/file_io/WriteFile/test4/writefile.cpp`** -> AI Confidence: **99.29%**
2697. **`src/coreclr/pal/tests/palsuite/file_io/errorpathnotfound/test1/test1.cpp`** -> AI Confidence: **99.29%**
2698. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/CreateFileMapping_neg1/CreateFileMapping_neg.cpp`** -> AI Confidence: **99.29%**
2699. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test1/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2700. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test2/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2701. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test3/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2702. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test4/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2703. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test5/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2704. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test6/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2705. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test7/createfilemapping.cpp`** -> AI Confidence: **99.29%**
2706. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/GetModuleFileNameA/test1/GetModuleFileNameA.cpp`** -> AI Confidence: **99.29%**
2707. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/GetModuleFileNameW/test1/GetModuleFileNameW.cpp`** -> AI Confidence: **99.29%**
2708. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/GetProcAddress/test1/test1.cpp`** -> AI Confidence: **99.29%**
2709. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/GetProcAddress/test2/test2.cpp`** -> AI Confidence: **99.29%**
2710. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/MapViewOfFile/test1/MapViewOfFile.cpp`** -> AI Confidence: **99.29%**
2711. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/MapViewOfFile/test2/MapViewOfFile.cpp`** -> AI Confidence: **99.29%**
2712. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/MapViewOfFile/test3/MapViewOfFile.cpp`** -> AI Confidence: **99.29%**
2713. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/MapViewOfFile/test4/mapviewoffile.cpp`** -> AI Confidence: **99.29%**
2714. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/UnmapViewOfFile/test1/UnmapViewOfFile.cpp`** -> AI Confidence: **99.29%**
2715. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualAlloc/test20/virtualalloc.cpp`** -> AI Confidence: **99.29%**
2716. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualAlloc/test21/virtualalloc.cpp`** -> AI Confidence: **99.29%**
2717. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test1/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2718. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test2/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2719. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test3/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2720. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test4/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2721. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test6/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2722. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test7/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2723. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualQuery/test1/VirtualQuery.cpp`** -> AI Confidence: **99.29%**
2724. **`src/coreclr/pal/tests/palsuite/loader/LoadLibraryA/test1/LoadLibraryA.cpp`** -> AI Confidence: **99.29%**
2725. **`src/coreclr/pal/tests/palsuite/loader/LoadLibraryW/test1/LoadLibraryW.cpp`** -> AI Confidence: **99.29%**
2726. **`src/coreclr/pal/tests/palsuite/miscellaneous/GetSystemInfo/test1/test.cpp`** -> AI Confidence: **99.29%**
2727. **`src/coreclr/pal/tests/palsuite/miscellaneous/InterLockedExchangeAdd/test1/test.cpp`** -> AI Confidence: **99.29%**
2728. **`src/coreclr/pal/tests/palsuite/miscellaneous/IsBadReadPtr/test1/test.cpp`** -> AI Confidence: **99.29%**
2729. **`src/coreclr/pal/tests/palsuite/miscellaneous/SetEnvironmentVariableA/test1/test1.cpp`** -> AI Confidence: **99.29%**
2730. **`src/coreclr/pal/tests/palsuite/miscellaneous/SetEnvironmentVariableW/test1/test.cpp`** -> AI Confidence: **99.29%**
2731. **`src/coreclr/pal/tests/palsuite/threading/CreateProcessW/test1/childProcess.cpp`** -> AI Confidence: **99.29%**
2732. **`src/coreclr/pal/tests/palsuite/threading/CreateProcessW/test1/parentProcess.cpp`** -> AI Confidence: **99.29%**
2733. **`src/coreclr/pal/tests/palsuite/threading/CreateProcessW/test2/parentprocess.cpp`** -> AI Confidence: **99.29%**
2734. **`src/coreclr/pal/tests/palsuite/threading/DisableThreadLibraryCalls/test2/test2.cpp`** -> AI Confidence: **99.29%**
2735. **`src/coreclr/pal/tests/palsuite/threading/DuplicateHandle/test1/test1.cpp`** -> AI Confidence: **99.29%**
2736. **`src/coreclr/pal/tests/palsuite/threading/DuplicateHandle/test10/test10.cpp`** -> AI Confidence: **99.29%**
2737. **`src/coreclr/pal/tests/palsuite/threading/DuplicateHandle/test12/test12.cpp`** -> AI Confidence: **99.29%**
2738. **`src/coreclr/pal/tests/palsuite/threading/GetCurrentThread/test1/thread.cpp`** -> AI Confidence: **99.29%**
2739. **`src/coreclr/pal/tests/palsuite/threading/OpenEventW/test1/test1.cpp`** -> AI Confidence: **99.29%**
2740. **`src/coreclr/pal/tests/palsuite/threading/OpenEventW/test2/test2.cpp`** -> AI Confidence: **99.29%**
2741. **`src/coreclr/pal/tests/palsuite/threading/OpenEventW/test3/test3.cpp`** -> AI Confidence: **99.29%**
2742. **`src/coreclr/pal/tests/palsuite/threading/OpenEventW/test5/test5.cpp`** -> AI Confidence: **99.29%**
2743. **`src/coreclr/pal/tests/palsuite/threading/OpenProcess/test1/test1.cpp`** -> AI Confidence: **99.29%**
2744. **`src/coreclr/pal/tests/palsuite/threading/QueryThreadCycleTime/test1/test1.cpp`** -> AI Confidence: **99.29%**
2745. **`src/coreclr/pal/tests/palsuite/threading/ResetEvent/test1/test1.cpp`** -> AI Confidence: **99.29%**
2746. **`src/coreclr/pal/tests/palsuite/threading/ResetEvent/test4/test4.cpp`** -> AI Confidence: **99.29%**
2747. **`src/coreclr/pal/tests/palsuite/threading/SetEvent/test1/test1.cpp`** -> AI Confidence: **99.29%**
2748. **`src/coreclr/pal/tests/palsuite/threading/SetEvent/test2/test2.cpp`** -> AI Confidence: **99.29%**
2749. **`src/coreclr/pal/tests/palsuite/threading/SetEvent/test4/test4.cpp`** -> AI Confidence: **99.29%**
2750. **`src/coreclr/pal/tests/palsuite/threading/Sleep/test1/Sleep.cpp`** -> AI Confidence: **99.29%**
2751. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjects/test1/test1.cpp`** -> AI Confidence: **99.29%**
2752. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjectsEx/test1/test1.cpp`** -> AI Confidence: **99.29%**
2753. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjectsEx/test5/helper.cpp`** -> AI Confidence: **99.29%**
2754. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjectsEx/test5/test5.cpp`** -> AI Confidence: **99.29%**
2755. **`src/coreclr/pal/tests/palsuite/threading/WaitForSingleObject/test1/test1.cpp`** -> AI Confidence: **99.29%**
2756. **`src/coreclr/tools/cdac-build-tool/sample/sample.data.h`** -> AI Confidence: **99.29%**
2757. **`src/coreclr/tools/metainfo/mdobj.cpp`** -> AI Confidence: **99.29%**
2758. **`src/coreclr/unwinder/amd64/dbs_stack_x64.cpp`** -> AI Confidence: **99.29%**
2759. **`src/coreclr/unwinder/amd64/unwinder.cpp`** -> AI Confidence: **99.29%**
2760. **`src/coreclr/unwinder/loongarch64/unwinder.cpp`** -> AI Confidence: **99.29%**
2761. **`src/coreclr/unwinder/riscv64/unwinder.cpp`** -> AI Confidence: **99.29%**
2762. **`src/coreclr/utilcode/log.cpp`** -> AI Confidence: **99.29%**
2763. **`src/coreclr/utilcode/sstring_com.cpp`** -> AI Confidence: **99.29%**
2764. **`src/coreclr/vm/arm/asmconstants.h`** -> AI Confidence: **99.29%**
2765. **`src/coreclr/vm/arm/asmmacros.h`** -> AI Confidence: **99.29%**
2766. **`src/coreclr/vm/arm/singlestepper.cpp`** -> AI Confidence: **99.29%**
2767. **`src/coreclr/vm/arm64/AsmMacros_Shared.h`** -> AI Confidence: **99.29%**
2768. **`src/coreclr/vm/arm64/asmconstants.h`** -> AI Confidence: **99.29%**
2769. **`src/coreclr/vm/arm64/asmmacros.h`** -> AI Confidence: **99.29%**
2770. **`src/coreclr/vm/arm64/patchedcodeconstants.h`** -> AI Confidence: **99.29%**
2771. **`src/coreclr/vm/arm64/singlestepper.cpp`** -> AI Confidence: **99.29%**
2772. **`src/coreclr/vm/asyncthunks.cpp`** -> AI Confidence: **99.29%**
2773. **`src/coreclr/vm/callhelpers.cpp`** -> AI Confidence: **99.29%**
2774. **`src/coreclr/vm/classlayoutinfo.cpp`** -> AI Confidence: **99.29%**
2775. **`src/coreclr/vm/clrvarargs.cpp`** -> AI Confidence: **99.29%**
2776. **`src/coreclr/vm/eecontract.cpp`** -> AI Confidence: **99.29%**
2777. **`src/coreclr/vm/gc_unwind_x86.inl`** -> AI Confidence: **99.29%**
2778. **`src/coreclr/vm/gcdecode.cpp`** -> AI Confidence: **99.29%**
2779. **`src/coreclr/vm/ildump.h`** -> AI Confidence: **99.29%**
2780. **`src/coreclr/vm/loongarch64/asmconstants.h`** -> AI Confidence: **99.29%**
2781. **`src/coreclr/vm/loongarch64/singlestepper.cpp`** -> AI Confidence: **99.29%**
2782. **`src/coreclr/vm/methodimpl.cpp`** -> AI Confidence: **99.29%**
2783. **`src/coreclr/vm/rcwrefcache.cpp`** -> AI Confidence: **99.29%**
2784. **`src/coreclr/vm/readytorunstandalonemethodmetadata.cpp`** -> AI Confidence: **99.29%**
2785. **`src/coreclr/vm/riscv64/asmconstants.h`** -> AI Confidence: **99.29%**
2786. **`src/coreclr/vm/riscv64/singlestepper.cpp`** -> AI Confidence: **99.29%**
2787. **`src/coreclr/vm/sigformat.cpp`** -> AI Confidence: **99.29%**
2788. **`src/libraries/System.Diagnostics.FileVersionInfo/tests/NativeLibrary/dllmain.cpp`** -> AI Confidence: **99.29%**
2789. **`src/libraries/System.Diagnostics.FileVersionInfo/tests/SecondNativeLibrary/dllmain.cpp`** -> AI Confidence: **99.29%**
2790. **`src/mono/cmake/config.h.in`** -> AI Confidence: **99.29%**
2791. **`src/mono/mono/arch/amd64/amd64-codegen.h`** -> AI Confidence: **99.29%**
2792. **`src/mono/mono/arch/x86/x86-codegen.h`** -> AI Confidence: **99.29%**
2793. **`src/mono/mono/metadata/verify-internals.h`** -> AI Confidence: **99.29%**
2794. **`src/mono/mono/mini/interp/jiterpreter-opcode-values.h`** -> AI Confidence: **99.29%**
2795. **`src/mono/mono/offsets/aarch64-apple-darwin10.h`** -> AI Confidence: **99.29%**
2796. **`src/mono/mono/offsets/aarch64-apple-maccatalyst.h`** -> AI Confidence: **99.29%**
2797. **`src/mono/mono/offsets/aarch64-v8a-linux-android.h`** -> AI Confidence: **99.29%**
2798. **`src/mono/mono/offsets/armv7-none-linux-androideabi.h`** -> AI Confidence: **99.29%**
2799. **`src/mono/mono/offsets/i686-none-linux-android.h`** -> AI Confidence: **99.29%**
2800. **`src/mono/mono/offsets/wasm32-unknown-none.h`** -> AI Confidence: **99.29%**
2801. **`src/mono/mono/offsets/wasm32-unknown-wasip2.h`** -> AI Confidence: **99.29%**
2802. **`src/mono/mono/offsets/x86_64-apple-darwin10.h`** -> AI Confidence: **99.29%**
2803. **`src/mono/mono/offsets/x86_64-apple-maccatalyst.h`** -> AI Confidence: **99.29%**
2804. **`src/mono/mono/offsets/x86_64-none-linux-android.h`** -> AI Confidence: **99.29%**
2805. **`src/mono/mono/sgen/sgen-archdep.h`** -> AI Confidence: **99.29%**
2806. **`src/mono/mono/sgen/sgen-major-copy-object.h`** -> AI Confidence: **99.29%**
2807. **`src/mono/mono/utils/dtrace.h`** -> AI Confidence: **99.29%**
2808. **`src/mono/mono/utils/ftnptr.h`** -> AI Confidence: **99.29%**
2809. **`src/mono/mono/utils/mono-hwcap-vars.h`** -> AI Confidence: **99.29%**
2810. **`src/mono/mono/utils/w32subset.h`** -> AI Confidence: **99.29%**
2811. **`src/mono/mono/utils/ward.h`** -> AI Confidence: **99.29%**
2812. **`src/native/containers/dn-vector-ptr.h`** -> AI Confidence: **99.29%**
2813. **`src/native/corehost/test/nativehost/get_native_search_directories_test.cpp`** -> AI Confidence: **99.29%**
2814. **`src/native/corehost/test/nativehost/hostfxr_exports.cpp`** -> AI Confidence: **99.29%**
2815. **`src/native/corehost/test/nativehost/hostpolicy_exports.cpp`** -> AI Confidence: **99.29%**
2816. **`src/native/external/brotli/c/enc/backward_references_inc.h`** -> AI Confidence: **99.29%**
2817. **`src/native/external/brotli/c/enc/block_splitter_inc.h`** -> AI Confidence: **99.29%**
2818. **`src/native/external/brotli/c/include/brotli/port.h`** -> AI Confidence: **99.29%**
2819. **`src/native/external/libunwind/include/compiler.h`** -> AI Confidence: **99.29%**
2820. **`src/native/external/libunwind/include/tdep-aarch64/jmpbuf.h`** -> AI Confidence: **99.29%**
2821. **`src/native/external/libunwind/include/tdep-riscv/jmpbuf.h`** -> AI Confidence: **99.29%**
2822. **`src/native/external/libunwind/include/tdep-s390x/jmpbuf.h`** -> AI Confidence: **99.29%**
2823. **`src/native/external/libunwind/include/tdep-x86/jmpbuf.h`** -> AI Confidence: **99.29%**
2824. **`src/native/external/libunwind/include/tdep-x86_64/jmpbuf.h`** -> AI Confidence: **99.29%**
2825. **`src/native/external/libunwind/tests/Ltest-init.cxx`** -> AI Confidence: **99.29%**
2826. **`src/native/external/rapidjson/internal/itoa.h`** -> AI Confidence: **99.29%**
2827. **`src/native/external/zlib-ng/arch/s390/s390_functions.h`** -> AI Confidence: **99.29%**
2828. **`src/native/libs/System.Native/ios/netinet/tcp_fsm.h`** -> AI Confidence: **99.29%**
2829. **`src/tests/Interop/COM/NativeClients/Dispatch/ClientTests.h`** -> AI Confidence: **99.29%**
2830. **`src/tests/JIT/jit64/mcc/interop/native_i3s.cpp`** -> AI Confidence: **99.29%**
2831. **`src/tests/JIT/jit64/mcc/interop/native_i5s.cpp`** -> AI Confidence: **99.29%**
2832. **`src/tests/JIT/jit64/mcc/interop/native_i6s.cpp`** -> AI Confidence: **99.29%**
2833. **`src/tests/JIT/jit64/mcc/interop/native_i7s.cpp`** -> AI Confidence: **99.29%**
2834. **`src/tests/JIT/jit64/mcc/interop/native_i8s.cpp`** -> AI Confidence: **99.29%**
2835. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/CustomAttributeBuilder.cs`** -> AI Confidence: **99.29%**
2836. **`src/coreclr/System.Private.CoreLib/src/System/Runtime/ExceptionServices/AsmOffsets.cs`** -> AI Confidence: **99.29%**
2837. **`src/coreclr/System.Private.CoreLib/src/System/TypeLoadException.CoreCLR.cs`** -> AI Confidence: **99.29%**
2838. **`src/coreclr/tools/Common/Compiler/DependencyAnalysis/Target_X64/X64Emitter.cs`** -> AI Confidence: **99.29%**
2839. **`src/coreclr/tools/Common/Compiler/DependencyAnalysis/Target_X86/X86Emitter.cs`** -> AI Confidence: **99.29%**
2840. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaSignatureEncoder.cs`** -> AI Confidence: **99.29%**
2841. **`src/coreclr/tools/Common/TypeSystem/Ecma/PrimitiveTypeProvider.cs`** -> AI Confidence: **99.29%**
2842. **`src/coreclr/tools/Common/TypeSystem/IL/MethodILDebugView.cs`** -> AI Confidence: **99.29%**
2843. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/ScannerExtensions.cs`** -> AI Confidence: **99.29%**
2844. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_X86/X86ReadyToRunGenericHelperNode.cs`** -> AI Confidence: **99.29%**
2845. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/JitHelper.cs`** -> AI Confidence: **99.29%**
2846. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/StringExtensions.cs`** -> AI Confidence: **99.29%**
2847. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/x86/GcInfo.cs`** -> AI Confidence: **99.29%**
2848. **`src/installer/tests/Assets/Projects/CoreDump.cs`** -> AI Confidence: **99.29%**
2849. **`src/libraries/Common/src/Interop/Unix/System.Native/Interop.MountPoints.FormatInfo.cs`** -> AI Confidence: **99.29%**
2850. **`src/libraries/Common/src/System/Composition/Diagnostics/CompositionTrace.cs`** -> AI Confidence: **99.29%**
2851. **`src/libraries/Common/src/System/Data/Common/MultipartIdentifier.cs`** -> AI Confidence: **99.29%**
2852. **`src/libraries/Common/src/System/Data/ProviderBase/DbMetaDataFactory.cs`** -> AI Confidence: **99.29%**
2853. **`src/libraries/Common/src/System/Net/Http/aspnetcore/Http2/Hpack/HPackDecoder.cs`** -> AI Confidence: **99.29%**
2854. **`src/libraries/Common/src/System/Net/HttpValidationHelpers.cs`** -> AI Confidence: **99.29%**
2855. **`src/libraries/Common/src/System/Number.Parsing.Common.cs`** -> AI Confidence: **99.29%**
2856. **`src/libraries/Common/src/System/Obsoletions.cs`** -> AI Confidence: **99.29%**
2857. **`src/libraries/Common/src/System/Reflection/AssemblyNameFormatter.cs`** -> AI Confidence: **99.29%**
2858. **`src/libraries/Common/src/System/Resources/ResourceWriter.cs`** -> AI Confidence: **99.29%**
2859. **`src/libraries/Microsoft.Bcl.Cryptography/src/Microsoft.Bcl.Cryptography.Forwards.cs`** -> AI Confidence: **99.29%**
2860. **`src/libraries/Microsoft.Bcl.Memory/src/Microsoft.Bcl.Memory.Forwards.cs`** -> AI Confidence: **99.29%**
2861. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Errors/ErrorFacts.cs`** -> AI Confidence: **99.29%**
2862. **`src/libraries/Microsoft.Extensions.Configuration.Binder/ref/Microsoft.Extensions.Configuration.Binder.cs`** -> AI Confidence: **99.29%**
2863. **`src/libraries/Microsoft.Extensions.Logging.Abstractions/src/LoggerExtensions.cs`** -> AI Confidence: **99.29%**
2864. **`src/libraries/Microsoft.VisualBasic.Core/ref/Microsoft.VisualBasic.Core.cs`** -> AI Confidence: **99.29%**
2865. **`src/libraries/Microsoft.Win32.Primitives/ref/Microsoft.Win32.Primitives.cs`** -> AI Confidence: **99.29%**
2866. **`src/libraries/System.CodeDom/src/System/CodeDom/Compiler/CodeValidator.cs`** -> AI Confidence: **99.29%**
2867. **`src/libraries/System.Collections.NonGeneric/ref/System.Collections.NonGeneric.cs`** -> AI Confidence: **99.29%**
2868. **`src/libraries/System.Collections/tests/Generic/LinkedList/LinkedList.Generic.Tests.Find.cs`** -> AI Confidence: **99.29%**
2869. **`src/libraries/System.Collections/tests/Generic/LinkedList/LinkedList.Generic.Tests.FindLast.cs`** -> AI Confidence: **99.29%**
2870. **`src/libraries/System.ComponentModel.Annotations/src/System/ComponentModel/DataAnnotations/ValidationContext.cs`** -> AI Confidence: **99.29%**
2871. **`src/libraries/System.ComponentModel.Primitives/src/System/ComponentModel/EventHandlerList.cs`** -> AI Confidence: **99.29%**
2872. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/Design/ComponentChangedEventArgs.cs`** -> AI Confidence: **99.29%**
2873. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/Design/Serialization/InstanceDescriptor.cs`** -> AI Confidence: **99.29%**
2874. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Diagnostics/TraceConfiguration.cs`** -> AI Confidence: **99.29%**
2875. **`src/libraries/System.Configuration.ConfigurationManager/tests/System/Configuration/TestData.cs`** -> AI Confidence: **99.29%**
2876. **`src/libraries/System.Data.Common/src/System/Data/DataViewListener.cs`** -> AI Confidence: **99.29%**
2877. **`src/libraries/System.Data.Common/src/System/Data/Merger.cs`** -> AI Confidence: **99.29%**
2878. **`src/libraries/System.Data.Odbc/src/Common/System/Data/Common/NameValuePermission.cs`** -> AI Confidence: **99.29%**
2879. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcUtils.cs`** -> AI Confidence: **99.29%**
2880. **`src/libraries/System.Data.OleDb/ref/System.Data.OleDb.cs`** -> AI Confidence: **99.29%**
2881. **`src/libraries/System.Data.OleDb/src/OleDbCommandBuilder.cs`** -> AI Confidence: **99.29%**
2882. **`src/libraries/System.Data.OleDb/src/System/Data/ProviderBase/DbMetaDataFactory.cs`** -> AI Confidence: **99.29%**
2883. **`src/libraries/System.Diagnostics.DiagnosticSource/ref/System.Diagnostics.DiagnosticSource.cs`** -> AI Confidence: **99.29%**
2884. **`src/libraries/System.Diagnostics.DiagnosticSource/ref/System.Diagnostics.DiagnosticSourceActivity.cs`** -> AI Confidence: **99.29%**
2885. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/Instrument.netfx.cs`** -> AI Confidence: **99.29%**
2886. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/ObservableCounter.cs`** -> AI Confidence: **99.29%**
2887. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/ObservableGauge.cs`** -> AI Confidence: **99.29%**
2888. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/ObservableUpDownCounter.cs`** -> AI Confidence: **99.29%**
2889. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/PassThroughPropagator.cs`** -> AI Confidence: **99.29%**
2890. **`src/libraries/System.Diagnostics.EventLog/ref/System.Diagnostics.EventLog.cs`** -> AI Confidence: **99.29%**
2891. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/Reader/EventLogInformation.cs`** -> AI Confidence: **99.29%**
2892. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/Reader/EventLogQuery.cs`** -> AI Confidence: **99.29%**
2893. **`src/libraries/System.Diagnostics.FileVersionInfo/ref/System.Diagnostics.FileVersionInfo.cs`** -> AI Confidence: **99.29%**
2894. **`src/libraries/System.Diagnostics.PerformanceCounter/src/System/Diagnostics/CounterSampleCalculator.cs`** -> AI Confidence: **99.29%**
2895. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/ProcessWaitState.Unix.cs`** -> AI Confidence: **99.29%**
2896. **`src/libraries/System.Diagnostics.StackTrace/src/System/Diagnostics/SymbolStore/ISymbolMethod.cs`** -> AI Confidence: **99.29%**
2897. **`src/libraries/System.Diagnostics.TextWriterTraceListener/ref/System.Diagnostics.TextWriterTraceListener.cs`** -> AI Confidence: **99.29%**
2898. **`src/libraries/System.Diagnostics.TextWriterTraceListener/src/System/Diagnostics/TextWriterTraceListener.cs`** -> AI Confidence: **99.29%**
2899. **`src/libraries/System.DirectoryServices.Protocols/src/System/DirectoryServices/Protocols/common/BerConverter.cs`** -> AI Confidence: **99.29%**
2900. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ADAMInstance.cs`** -> AI Confidence: **99.29%**
2901. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectoryInterSiteTransport.cs`** -> AI Confidence: **99.29%**
2902. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchedule.cs`** -> AI Confidence: **99.29%**
2903. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchemaClassCollection.cs`** -> AI Confidence: **99.29%**
2904. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchemaProperty.cs`** -> AI Confidence: **99.29%**
2905. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySiteLinkCollection.cs`** -> AI Confidence: **99.29%**
2906. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySubnet.cs`** -> AI Confidence: **99.29%**
2907. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/DirectoryServer.cs`** -> AI Confidence: **99.29%**
2908. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/DirectoryServerCollection.cs`** -> AI Confidence: **99.29%**
2909. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/TrustHelper.cs`** -> AI Confidence: **99.29%**
2910. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/PropertyValueCollection.cs`** -> AI Confidence: **99.29%**
2911. **`src/libraries/System.Formats.Asn1/src/System/Formats/Asn1/AsnWriter.Enumerated.cs`** -> AI Confidence: **99.29%**
2912. **`src/libraries/System.Formats.Cbor/src/System/Formats/Cbor/Reader/CborReader.SkipValue.cs`** -> AI Confidence: **99.29%**
2913. **`src/libraries/System.Formats.Cbor/src/System/Formats/Cbor/Reader/CborReader.cs`** -> AI Confidence: **99.29%**
2914. **`src/libraries/System.Formats.Cbor/tests/Reader/CborReaderTests.Helpers.cs`** -> AI Confidence: **99.29%**
2915. **`src/libraries/System.IO.Compression.ZipFile/ref/System.IO.Compression.ZipFile.cs`** -> AI Confidence: **99.29%**
2916. **`src/libraries/System.IO.FileSystem.AccessControl/src/System/Security/AccessControl/DirectoryObjectSecurity.cs`** -> AI Confidence: **99.29%**
2917. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/FileFormatException.cs`** -> AI Confidence: **99.29%**
2918. **`src/libraries/System.IO.Pipes.AccessControl/ref/System.IO.Pipes.AccessControl.cs`** -> AI Confidence: **99.29%**
2919. **`src/libraries/System.Linq.Expressions/src/System/Dynamic/Utils/ExpressionVisitorUtils.cs`** -> AI Confidence: **99.29%**
2920. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Generated.cs`** -> AI Confidence: **99.29%**
2921. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Lambda.cs`** -> AI Confidence: **99.29%**
2922. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Logical.cs`** -> AI Confidence: **99.29%**
2923. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/StackSpiller.Generated.cs`** -> AI Confidence: **99.29%**
2924. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/TryExpression.cs`** -> AI Confidence: **99.29%**
2925. **`src/libraries/System.Linq.Expressions/tests/Array/NewArrayListTests.cs`** -> AI Confidence: **99.29%**
2926. **`src/libraries/System.Linq.Expressions/tests/Array/NullableArrayIndexTests.cs`** -> AI Confidence: **99.29%**
2927. **`src/libraries/System.Linq.Expressions/tests/Array/NullableNewArrayListTests.cs`** -> AI Confidence: **99.29%**
2928. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Arithmetic/BinaryNullableAddTests.cs`** -> AI Confidence: **99.29%**
2929. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Arithmetic/BinaryNullableDivideTests.cs`** -> AI Confidence: **99.29%**
2930. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Arithmetic/BinaryNullableModuloTests.cs`** -> AI Confidence: **99.29%**
2931. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Arithmetic/BinaryNullableMultiplyTests.cs`** -> AI Confidence: **99.29%**
2932. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Arithmetic/BinaryNullablePowerTests.cs`** -> AI Confidence: **99.29%**
2933. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Arithmetic/BinaryNullableSubtractTests.cs`** -> AI Confidence: **99.29%**
2934. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Arithmetic/BinaryShiftTests.cs`** -> AI Confidence: **99.29%**
2935. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Bitwise/BinaryNullableAndTests.cs`** -> AI Confidence: **99.29%**
2936. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Bitwise/BinaryNullableExclusiveOrTests.cs`** -> AI Confidence: **99.29%**
2937. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Bitwise/BinaryNullableOrTests.cs`** -> AI Confidence: **99.29%**
2938. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Logical/BinaryNullableLogicalTests.cs`** -> AI Confidence: **99.29%**
2939. **`src/libraries/System.Linq.Expressions/tests/Cast/AsNullable.cs`** -> AI Confidence: **99.29%**
2940. **`src/libraries/System.Linq.Expressions/tests/Cast/CastNullableTests.cs`** -> AI Confidence: **99.29%**
2941. **`src/libraries/System.Linq.Expressions/tests/Cast/IsNullableTests.cs`** -> AI Confidence: **99.29%**
2942. **`src/libraries/System.Linq.Expressions/tests/Cast/IsTests.cs`** -> AI Confidence: **99.29%**
2943. **`src/libraries/System.Linq.Expressions/tests/Constant/ConstantNullableTests.cs`** -> AI Confidence: **99.29%**
2944. **`src/libraries/System.Linq.Expressions/tests/Convert/ConvertCheckedTests.cs`** -> AI Confidence: **99.29%**
2945. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaAddNullableTests.cs`** -> AI Confidence: **99.29%**
2946. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaAddTests.cs`** -> AI Confidence: **99.29%**
2947. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaDivideNullableTests.cs`** -> AI Confidence: **99.29%**
2948. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaIdentityNullableTests.cs`** -> AI Confidence: **99.29%**
2949. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaModuloNullableTests.cs`** -> AI Confidence: **99.29%**
2950. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaMultiplyNullableTests.cs`** -> AI Confidence: **99.29%**
2951. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaMultiplyTests.cs`** -> AI Confidence: **99.29%**
2952. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaSubtractNullableTests.cs`** -> AI Confidence: **99.29%**
2953. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaSubtractTests.cs`** -> AI Confidence: **99.29%**
2954. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaUnaryNotNullableTests.cs`** -> AI Confidence: **99.29%**
2955. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedAddCheckedNullableTests.cs`** -> AI Confidence: **99.29%**
2956. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedAddNullableTests.cs`** -> AI Confidence: **99.29%**
2957. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedBitwiseAndNullableTests.cs`** -> AI Confidence: **99.29%**
2958. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedBitwiseExclusiveOrNullableTests.cs`** -> AI Confidence: **99.29%**
2959. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedBitwiseOrNullableTests.cs`** -> AI Confidence: **99.29%**
2960. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2961. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonGreaterThanNullableTests.cs`** -> AI Confidence: **99.29%**
2962. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonGreaterThanOrEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2963. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonLessThanNullableTests.cs`** -> AI Confidence: **99.29%**
2964. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonLessThanOrEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2965. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonNotEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2966. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedDivideNullableTests.cs`** -> AI Confidence: **99.29%**
2967. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedModuloNullableTests.cs`** -> AI Confidence: **99.29%**
2968. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedMultiplyCheckedNullableTests.cs`** -> AI Confidence: **99.29%**
2969. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedMultiplyNullableTests.cs`** -> AI Confidence: **99.29%**
2970. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedNullableTests.cs`** -> AI Confidence: **99.29%**
2971. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedSubtractCheckedNullableTests.cs`** -> AI Confidence: **99.29%**
2972. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedSubtractNullableTests.cs`** -> AI Confidence: **99.29%**
2973. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2974. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonGreaterThanNullableTests.cs`** -> AI Confidence: **99.29%**
2975. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonGreaterThanOrEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2976. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonLessThanNullableTests.cs`** -> AI Confidence: **99.29%**
2977. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonLessThanOrEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2978. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonNotEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2979. **`src/libraries/System.Linq.Expressions/tests/New/NewWithParameterTests.cs`** -> AI Confidence: **99.29%**
2980. **`src/libraries/System.Linq.Expressions/tests/Ternary/TernaryArrayNullableTests.cs`** -> AI Confidence: **99.29%**
2981. **`src/libraries/System.Linq.Expressions/tests/Ternary/TernaryArrayTests.cs`** -> AI Confidence: **99.29%**
2982. **`src/libraries/System.Linq.Expressions/tests/Ternary/TernaryNullableTests.cs`** -> AI Confidence: **99.29%**
2983. **`src/libraries/System.Linq.Expressions/tests/Ternary/TernaryTests.cs`** -> AI Confidence: **99.29%**
2984. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryArithmeticNegateCheckedNullableTests.cs`** -> AI Confidence: **99.29%**
2985. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryArithmeticNegateNullableTests.cs`** -> AI Confidence: **99.29%**
2986. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryBitwiseNotNullableTests.cs`** -> AI Confidence: **99.29%**
2987. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryIsFalseNullableTests.cs`** -> AI Confidence: **99.29%**
2988. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryIsTrueNullableTests.cs`** -> AI Confidence: **99.29%**
2989. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryOnesComplementNullableTests.cs`** -> AI Confidence: **99.29%**
2990. **`src/libraries/System.Linq.Expressions/tests/Unary/UnaryUnaryPlusNullableTests.cs`** -> AI Confidence: **99.29%**
2991. **`src/libraries/System.Linq.Parallel/src/System/Linq/Parallel/Utils/Sorting.cs`** -> AI Confidence: **99.29%**
2992. **`src/libraries/System.Management/src/System/Management/ManagementDateTime.cs`** -> AI Confidence: **99.29%**
2993. **`src/libraries/System.Management/src/System/Management/ManagementObjectSearcher.cs`** -> AI Confidence: **99.29%**
2994. **`src/libraries/System.Management/src/System/Management/MethodSet.cs`** -> AI Confidence: **99.29%**
2995. **`src/libraries/System.Memory.Data/ref/System.Memory.Data.cs`** -> AI Confidence: **99.29%**
2996. **`src/libraries/System.Memory/ref/System.Memory.cs`** -> AI Confidence: **99.29%**
2997. **`src/libraries/System.Memory/tests/ReadOnlySpan/IndexOfAny.byte.cs`** -> AI Confidence: **99.29%**
2998. **`src/libraries/System.Memory/tests/ReadOnlySpan/IndexOfAny.char.cs`** -> AI Confidence: **99.29%**
2999. **`src/libraries/System.Memory/tests/SequenceReader/SpanLiteralExtensions.cs`** -> AI Confidence: **99.29%**
3000. **`src/libraries/System.Memory/tests/Span/EnumerateRunes.cs`** -> AI Confidence: **99.29%**
3001. **`src/libraries/System.Memory/tests/Span/LastIndexOf.T.cs`** -> AI Confidence: **99.29%**
3002. **`src/libraries/System.Net.Http.Json/ref/System.Net.Http.Json.cs`** -> AI Confidence: **99.29%**
3003. **`src/libraries/System.Net.Http/src/System/Net/Http/HttpRequestException.cs`** -> AI Confidence: **99.29%**
3004. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpEnvironmentProxy.cs`** -> AI Confidence: **99.29%**
3005. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpRequestStream.Windows.cs`** -> AI Confidence: **99.29%**
3006. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpResponseStreamAsyncResult.cs`** -> AI Confidence: **99.29%**
3007. **`src/libraries/System.Net.Mail/tests/Unit/ByteEncodingTest.cs`** -> AI Confidence: **99.29%**
3008. **`src/libraries/System.Net.Mail/tests/Unit/MessageTests/MessageHeaderBehaviorTest.cs`** -> AI Confidence: **99.29%**
3009. **`src/libraries/System.Net.NameResolution/ref/System.Net.NameResolution.cs`** -> AI Confidence: **99.29%**
3010. **`src/libraries/System.Net.Ping/ref/System.Net.Ping.cs`** -> AI Confidence: **99.29%**
3011. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Interop/msquic_generated_windows.cs`** -> AI Confidence: **99.29%**
3012. **`src/libraries/System.Net.Requests/ref/System.Net.Requests.cs`** -> AI Confidence: **99.29%**
3013. **`src/libraries/System.Net.Requests/src/System/Net/NetRes.cs`** -> AI Confidence: **99.29%**
3014. **`src/libraries/System.Net.WebClient/tests/AssemblyInfo.cs`** -> AI Confidence: **99.29%**
3015. **`src/libraries/System.Net.WebHeaderCollection/ref/System.Net.WebHeaderCollection.cs`** -> AI Confidence: **99.29%**
3016. **`src/libraries/System.Net.WebProxy/ref/System.Net.WebProxy.cs`** -> AI Confidence: **99.29%**
3017. **`src/libraries/System.Net.WebSockets.Client/ref/System.Net.WebSockets.Client.cs`** -> AI Confidence: **99.29%**
3018. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.IAggregationOperator.cs`** -> AI Confidence: **99.29%**
3019. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.IBinaryOperator.cs`** -> AI Confidence: **99.29%**
3020. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.IStatefulUnaryOperator.cs`** -> AI Confidence: **99.29%**
3021. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.ITernaryOperator.cs`** -> AI Confidence: **99.29%**
3022. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.IUnaryOperator.cs`** -> AI Confidence: **99.29%**
3023. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Formatter/Utf8Formatter.Boolean.cs`** -> AI Confidence: **99.29%**
3024. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Formatter/Utf8Formatter.Guid.cs`** -> AI Confidence: **99.29%**
3025. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Date.R.cs`** -> AI Confidence: **99.29%**
3026. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Integer.Signed.D.cs`** -> AI Confidence: **99.29%**
3027. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Integer.Signed.N.cs`** -> AI Confidence: **99.29%**
3028. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Integer.Unsigned.D.cs`** -> AI Confidence: **99.29%**
3029. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Integer.Unsigned.N.cs`** -> AI Confidence: **99.29%**
3030. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.TimeSpan.C.cs`** -> AI Confidence: **99.29%**
3031. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.TimeSpan.LittleG.cs`** -> AI Confidence: **99.29%**
3032. **`src/libraries/System.Private.CoreLib/src/System/Collections/ObjectModel/CollectionHelpers.cs`** -> AI Confidence: **99.29%**
3033. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/EventListener.cs`** -> AI Confidence: **99.29%**
3034. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/EventPipePayloadDecoder.cs`** -> AI Confidence: **99.29%**
3035. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/TraceLogging/ConcurrentSet.cs`** -> AI Confidence: **99.29%**
3036. **`src/libraries/System.Private.CoreLib/src/System/Globalization/DateTimeFormatInfoScanner.cs`** -> AI Confidence: **99.29%**
3037. **`src/libraries/System.Private.CoreLib/src/System/IConvertible.cs`** -> AI Confidence: **99.29%**
3038. **`src/libraries/System.Private.CoreLib/src/System/IO/Strategies/FileStreamHelpers.cs`** -> AI Confidence: **99.29%**
3039. **`src/libraries/System.Private.CoreLib/src/System/ParseNumbers.cs`** -> AI Confidence: **99.29%**
3040. **`src/libraries/System.Private.CoreLib/src/System/Reflection/Binder.cs`** -> AI Confidence: **99.29%**
3041. **`src/libraries/System.Private.CoreLib/src/System/Reflection/IReflect.cs`** -> AI Confidence: **99.29%**
3042. **`src/libraries/System.Private.CoreLib/src/System/Reflection/InvokeUtils.cs`** -> AI Confidence: **99.29%**
3043. **`src/libraries/System.Private.CoreLib/src/System/Security/SecurityException.cs`** -> AI Confidence: **99.29%**
3044. **`src/libraries/System.Private.CoreLib/src/System/SpanHelpers.cs`** -> AI Confidence: **99.29%**
3045. **`src/libraries/System.Private.CoreLib/src/System/Text/CompositeFormat.cs`** -> AI Confidence: **99.29%**
3046. **`src/libraries/System.Private.CoreLib/src/System/Text/UnicodeEncoding.cs`** -> AI Confidence: **99.29%**
3047. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.StringSerializer.cs`** -> AI Confidence: **99.29%**
3048. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Attributes.cs`** -> AI Confidence: **99.29%**
3049. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonWriterDelegator.cs`** -> AI Confidence: **99.29%**
3050. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlSigningNodeWriter.cs`** -> AI Confidence: **99.29%**
3051. **`src/libraries/System.Private.Uri/src/System/PercentEncodingHelper.cs`** -> AI Confidence: **99.29%**
3052. **`src/libraries/System.Private.Uri/src/System/UriBuilder.cs`** -> AI Confidence: **99.29%**
3053. **`src/libraries/System.Private.Uri/tests/FunctionalTests/IriEncodingDecodingTests.cs`** -> AI Confidence: **99.29%**
3054. **`src/libraries/System.Private.Uri/tests/FunctionalTests/UriIsWellFormedUriStringTest.cs`** -> AI Confidence: **99.29%**
3055. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/XNodeBuilder.cs`** -> AI Confidence: **99.29%**
3056. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/XNodeReplaceOnElement.cs`** -> AI Confidence: **99.29%**
3057. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/ManagedNodeWriter.cs`** -> AI Confidence: **99.29%**
3058. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/CXMLGeneralTest.cs`** -> AI Confidence: **99.29%**
3059. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/ReadSubTree.cs`** -> AI Confidence: **99.29%**
3060. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/ReadToDescendant.cs`** -> AI Confidence: **99.29%**
3061. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/ReadToNextSibling.cs`** -> AI Confidence: **99.29%**
3062. **`src/libraries/System.Private.Xml/src/System/Xml/Core/QueryOutputWriterV1.cs`** -> AI Confidence: **99.29%**
3063. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextEncoder.cs`** -> AI Confidence: **99.29%**
3064. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/PrimitiveXmlSerializers.cs`** -> AI Confidence: **99.29%**
3065. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/AttributeAction.cs`** -> AI Confidence: **99.29%**
3066. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/CallTemplateAction.cs`** -> AI Confidence: **99.29%**
3067. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ChooseAction.cs`** -> AI Confidence: **99.29%**
3068. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ElementAction.cs`** -> AI Confidence: **99.29%**
3069. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/RecordBuilder.cs`** -> AI Confidence: **99.29%**
3070. **`src/libraries/System.Private.Xml/tests/Readers/NameTable/TCRecordNameTableAdd.cs`** -> AI Confidence: **99.29%**
3071. **`src/libraries/System.Private.Xml/tests/Readers/NameTable/TestFiles.cs`** -> AI Confidence: **99.29%**
3072. **`src/libraries/System.Private.Xml/tests/Readers/ReaderSettings/TCMaxSettings.cs`** -> AI Confidence: **99.29%**
3073. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCWriteBuffer.cs`** -> AI Confidence: **99.29%**
3074. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests1.cs`** -> AI Confidence: **99.29%**
3075. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests2.cs`** -> AI Confidence: **99.29%**
3076. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests3.cs`** -> AI Confidence: **99.29%**
3077. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests4.cs`** -> AI Confidence: **99.29%**
3078. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests5.cs`** -> AI Confidence: **99.29%**
3079. **`src/libraries/System.Private.Xml/tests/XmlReaderLib/TCLinePos.cs`** -> AI Confidence: **99.29%**
3080. **`src/libraries/System.Private.Xml/tests/XmlReaderLib/TCReadValue.cs`** -> AI Confidence: **99.29%**
3081. **`src/libraries/System.Reflection.Context/ref/System.Reflection.Context.cs`** -> AI Confidence: **99.29%**
3082. **`src/libraries/System.Reflection.Emit.ILGeneration/ref/System.Reflection.Emit.ILGeneration.cs`** -> AI Confidence: **99.29%**
3083. **`src/libraries/System.Reflection.Emit.Lightweight/ref/System.Reflection.Emit.Lightweight.cs`** -> AI Confidence: **99.29%**
3084. **`src/libraries/System.Reflection.Emit/src/System/Reflection/Emit/SignatureHelper.cs`** -> AI Confidence: **99.29%**
3085. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/BlobWriterImpl.cs`** -> AI Confidence: **99.29%**
3086. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/Ecma335/CustomAttributeDecoder.cs`** -> AI Confidence: **99.29%**
3087. **`src/libraries/System.Reflection.MetadataLoadContext/tests/src/Tests/Type/TypeTests.GetMember.cs`** -> AI Confidence: **99.29%**
3088. **`src/libraries/System.Reflection.TypeExtensions/tests/ConstructorInfo/ConstructorInfoInvokeArrayTests.cs`** -> AI Confidence: **99.29%**
3089. **`src/libraries/System.Resources.Extensions/tests/BinaryFormatTests/Common/EventOrderTests.cs`** -> AI Confidence: **99.29%**
3090. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/Marshaling/JSMarshalerArgument.Object.cs`** -> AI Confidence: **99.29%**
3091. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/Marshaling/JSMarshalerArgument.String.cs`** -> AI Confidence: **99.29%**
3092. **`src/libraries/System.Runtime.InteropServices/src/System/Runtime/InteropServices/HandleCollector.cs`** -> AI Confidence: **99.29%**
3093. **`src/libraries/System.Runtime.InteropServices/tests/Common/ComInterfaces/INullArrayCases.cs`** -> AI Confidence: **99.29%**
3094. **`src/libraries/System.Runtime.InteropServices/tests/System.Runtime.InteropServices.UnitTests/System/Runtime/InteropServices/Marshal/StringMarshalingTests.cs`** -> AI Confidence: **99.29%**
3095. **`src/libraries/System.Runtime.InteropServices/tests/System.Runtime.InteropServices.UnitTests/System/Runtime/InteropServices/NFloatTests.GenericMath.cs`** -> AI Confidence: **99.29%**
3096. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/BigIntegerCalculator.AddSub.cs`** -> AI Confidence: **99.29%**
3097. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/BigIntegerCalculator.DivRem.cs`** -> AI Confidence: **99.29%**
3098. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/BigIntegerCalculator.SquMul.cs`** -> AI Confidence: **99.29%**
3099. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/Driver.cs`** -> AI Confidence: **99.29%**
3100. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/cast_to.cs`** -> AI Confidence: **99.29%**
3101. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/ctor.cs`** -> AI Confidence: **99.29%**
3102. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/op_multiply.cs`** -> AI Confidence: **99.29%**
3103. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatter.cs`** -> AI Confidence: **99.29%**
3104. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryArray.cs`** -> AI Confidence: **99.29%**
3105. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryObjectWithMapTyped.cs`** -> AI Confidence: **99.29%**
3106. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryTypeConverter.cs`** -> AI Confidence: **99.29%**
3107. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryUtilClasses.cs`** -> AI Confidence: **99.29%**
3108. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/ObjectNull.cs`** -> AI Confidence: **99.29%**
3109. **`src/libraries/System.Runtime.Serialization.Xml/tests/Canonicalization/CryptoCanonicalization/CanonicalWriter.cs`** -> AI Confidence: **99.29%**
3110. **`src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.Context/Common.cs`** -> AI Confidence: **99.29%**
3111. **`src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.Statements/Conformance.dynamic.statements.foreach.cs`** -> AI Confidence: **99.29%**
3112. **`src/libraries/System.Runtime/tests/System.IO.FileSystem.Tests/Enumeration/MatchTypesTests.cs`** -> AI Confidence: **99.29%**
3113. **`src/libraries/System.Runtime/tests/System.Runtime.InteropServices.RuntimeInformation.Tests/CheckArchitectureTests.cs`** -> AI Confidence: **99.29%**
3114. **`src/libraries/System.Runtime/tests/System.Text.Encoding.Tests/Ascii/TrimTests.cs`** -> AI Confidence: **99.29%**
3115. **`src/libraries/System.Runtime/tests/System.Text.Encoding.Tests/EncodingTestHelpers.cs`** -> AI Confidence: **99.29%**
3116. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskContinueWithAllAnyTests.cs`** -> AI Confidence: **99.29%**
3117. **`src/libraries/System.Security.Cryptography.Cose/tests/CoseHeaderLabelTests.cs`** -> AI Confidence: **99.29%**
3118. **`src/libraries/System.Security.Cryptography.Pkcs/ref/System.Security.Cryptography.Pkcs.netstandard21.cs`** -> AI Confidence: **99.29%**
3119. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/EnvelopedCms.cs`** -> AI Confidence: **99.29%**
3120. **`src/libraries/System.Security.Cryptography.Pkcs/tests/Rfc3161/TimestampRequestTests.cs`** -> AI Confidence: **99.29%**
3121. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/C14NAncestralNamespaceContextManager.cs`** -> AI Confidence: **99.29%**
3122. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/Reference.cs`** -> AI Confidence: **99.29%**
3123. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/ECDiffieHellmanCng.Key.cs`** -> AI Confidence: **99.29%**
3124. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/ECDsaCng.Key.cs`** -> AI Confidence: **99.29%**
3125. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/ECParameters.cs`** -> AI Confidence: **99.29%**
3126. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/HKDF.OpenSsl.cs`** -> AI Confidence: **99.29%**
3127. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/Asn1/TbsCertificateAsn.xml.cs`** -> AI Confidence: **99.29%**
3128. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/ChainPal.OpenSsl.cs`** -> AI Confidence: **99.29%**
3129. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X500DirectoryStringHelper.cs`** -> AI Confidence: **99.29%**
3130. **`src/libraries/System.Security.Cryptography/tests/X509Certificates/ExtensionsTests/SubjectAlternativeNameTests.cs`** -> AI Confidence: **99.29%**
3131. **`src/libraries/System.Security.Permissions/ref/System.Security.Permissions.Forwards.cs`** -> AI Confidence: **99.29%**
3132. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/Item.cs`** -> AI Confidence: **99.29%**
3133. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/ParseElementCollection.cs`** -> AI Confidence: **99.29%**
3134. **`src/libraries/System.Speech/src/Internal/SrgsParser/SrgsDocumentParser.cs`** -> AI Confidence: **99.29%**
3135. **`src/libraries/System.Speech/src/Internal/Synthesis/AudioFormatConverter.cs`** -> AI Confidence: **99.29%**
3136. **`src/libraries/System.Speech/src/Internal/Synthesis/PcmConverter.cs`** -> AI Confidence: **99.29%**
3137. **`src/libraries/System.Text.Encodings.Web/src/System/Text/Encodings/Web/OptimizedInboxTextEncoder.cs`** -> AI Confidence: **99.29%**
3138. **`src/libraries/System.Text.Encodings.Web/tests/JavaScriptEncoderTests.Relaxed.cs`** -> AI Confidence: **99.29%**
3139. **`src/libraries/System.Text.Json/Common/JsonSourceGenerationOptionsAttribute.cs`** -> AI Confidence: **99.29%**
3140. **`src/libraries/System.Text.Json/src/System/Text/Json/JsonException.cs`** -> AI Confidence: **99.29%**
3141. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonConverter.MetadataHandling.cs`** -> AI Confidence: **99.29%**
3142. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonConverterOfT.WriteCore.cs`** -> AI Confidence: **99.29%**
3143. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonConverterOfT.cs`** -> AI Confidence: **99.29%**
3144. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Metadata/PolymorphicTypeResolver.cs`** -> AI Confidence: **99.29%**
3145. **`src/libraries/System.Text.Json/src/System/Text/Json/ThrowHelper.cs`** -> AI Confidence: **99.29%**
3146. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Literal.cs`** -> AI Confidence: **99.29%**
3147. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteValues.Comment.cs`** -> AI Confidence: **99.29%**
3148. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteValues.Literal.cs`** -> AI Confidence: **99.29%**
3149. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteValues.String.cs`** -> AI Confidence: **99.29%**
3150. **`src/libraries/System.Text.Json/tests/Common/TestClasses/TestClasses.SimpleTestClassWithNullables.cs`** -> AI Confidence: **99.29%**
3151. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/BitStackTests.cs`** -> AI Confidence: **99.29%**
3152. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/JsonNode/JsonNodeOperatorTests.cs`** -> AI Confidence: **99.29%**
3153. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Serialization/NullableTests.cs`** -> AI Confidence: **99.29%**
3154. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Utf8JsonReaderTests.ValueTextEquals.cs`** -> AI Confidence: **99.29%**
3155. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexInterpreterCode.cs`** -> AI Confidence: **99.29%**
3156. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/RegexParserTests.cs`** -> AI Confidence: **99.29%**
3157. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/RegexParserTests.netcoreapp.cs`** -> AI Confidence: **99.29%**
3158. **`src/libraries/System.Text.RegularExpressions/tests/UnitTests/RegexPrefixAnalyzerTests.cs`** -> AI Confidence: **99.29%**
3159. **`src/libraries/System.Text.RegularExpressions/tests/UnitTests/RegexReductionTests.cs`** -> AI Confidence: **99.29%**
3160. **`src/libraries/System.Threading.AccessControl/ref/System.Threading.AccessControl.cs`** -> AI Confidence: **99.29%**
3161. **`src/libraries/System.Threading.Overlapped/ref/System.Threading.Overlapped.cs`** -> AI Confidence: **99.29%**
3162. **`src/libraries/System.Threading.Tasks.Parallel/tests/ParallelForTest.cs`** -> AI Confidence: **99.29%**
3163. **`src/libraries/System.Threading.Tasks.Parallel/tests/ParallelStateTest.cs`** -> AI Confidence: **99.29%**
3164. **`src/libraries/System.Threading.Thread/ref/System.Threading.Thread.cs`** -> AI Confidence: **99.29%**
3165. **`src/libraries/System.Threading.ThreadPool/ref/System.Threading.ThreadPool.cs`** -> AI Confidence: **99.29%**
3166. **`src/libraries/System.Transactions.Local/src/System/Transactions/EnlistmentState.cs`** -> AI Confidence: **99.29%**
3167. **`src/libraries/System.Transactions.Local/src/System/Transactions/Oletx/OletxEnlistment.cs`** -> AI Confidence: **99.29%**
3168. **`src/libraries/System.Transactions.Local/src/System/Transactions/PreparingEnlistment.cs`** -> AI Confidence: **99.29%**
3169. **`src/libraries/System.Transactions.Local/src/System/Transactions/SinglePhaseEnlistment.cs`** -> AI Confidence: **99.29%**
3170. **`src/libraries/System.Xml.XmlSerializer/ref/System.Xml.XmlSerializer.cs`** -> AI Confidence: **99.29%**
3171. **`src/mono/mono/mini/test.cs`** -> AI Confidence: **99.29%**
3172. **`src/mono/mono/tests/abort-try-holes.cs`** -> AI Confidence: **99.29%**
3173. **`src/mono/mono/tests/bug-30085.cs`** -> AI Confidence: **99.29%**
3174. **`src/mono/mono/tests/exception9.cs`** -> AI Confidence: **99.29%**
3175. **`src/mono/mono/tests/gchandle-stress.cs`** -> AI Confidence: **99.29%**
3176. **`src/mono/mono/tests/main-returns-abort-resetabort.cs`** -> AI Confidence: **99.29%**
3177. **`src/mono/mono/tests/main-returns-background-abort-resetabort.cs`** -> AI Confidence: **99.29%**
3178. **`src/mono/mono/tests/main-returns-background-resetabort.cs`** -> AI Confidence: **99.29%**
3179. **`src/mono/mono/tests/many-locals.cs`** -> AI Confidence: **99.29%**
3180. **`src/mono/mono/tests/monitor-stress.cs`** -> AI Confidence: **99.29%**
3181. **`src/mono/wasm/Wasm.Build.Tests/Common/EnvironmentVariables.cs`** -> AI Confidence: **99.29%**
3182. **`src/mono/wasm/host/WasmTestMessagesProcessor.cs`** -> AI Confidence: **99.29%**
3183. **`src/mono/wasm/testassets/BlazorBasicTestApp/App/Pages/Home.razor`** -> AI Confidence: **99.29%**
3184. **`src/mono/wasm/testassets/BlazorWebWasm/BlazorWebWasm/Components/Pages/NotFound.razor`** -> AI Confidence: **99.29%**
3185. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/GC/GCHeapWKS.cs`** -> AI Confidence: **99.29%**
3186. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/Context/X86/GCInfoDecoding/GCArgTable.cs`** -> AI Confidence: **99.29%**
3187. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataExceptionState.cs`** -> AI Confidence: **99.29%**
3188. **`src/tasks/Crossgen2Tasks/CommonFilePulledFromSdkRepo/LogAdapter.cs`** -> AI Confidence: **99.29%**
3189. **`src/tests/Common/GenerateHWIntrinsicTests/Arm/Templates.cs`** -> AI Confidence: **99.29%**
3190. **`src/tests/GC/API/NoGCRegion/Callback.cs`** -> AI Confidence: **99.29%**
3191. **`src/tests/GC/API/NoGCRegion/NoGC.cs`** -> AI Confidence: **99.29%**
3192. **`src/tests/GC/Performance/Tests/GCLarge.cs`** -> AI Confidence: **99.29%**
3193. **`src/tests/GC/Performance/Tests/GCPerf.cs`** -> AI Confidence: **99.29%**
3194. **`src/tests/GC/Performance/Tests/WeakReferenceTest.cs`** -> AI Confidence: **99.29%**
3195. **`src/tests/GC/Scenarios/Boxing/gcvariant2.cs`** -> AI Confidence: **99.29%**
3196. **`src/tests/GC/Scenarios/Boxing/gcvariant3.cs`** -> AI Confidence: **99.29%**
3197. **`src/tests/GC/Scenarios/Boxing/gcvariant4.cs`** -> AI Confidence: **99.29%**
3198. **`src/tests/GC/Scenarios/ServerModel/server.cs`** -> AI Confidence: **99.29%**
3199. **`src/tests/GC/Scenarios/muldimjagary/muldimjagary.cs`** -> AI Confidence: **99.29%**
3200. **`src/tests/GC/Stress/Tests/DirectedGraph.cs`** -> AI Confidence: **99.29%**
3201. **`src/tests/GC/Stress/Tests/MulDimJagAry.cs`** -> AI Confidence: **99.29%**
3202. **`src/tests/GC/Stress/Tests/StressAllocator.cs`** -> AI Confidence: **99.29%**
3203. **`src/tests/Interop/StructMarshalling/PInvoke/MarshalStructAsLayoutExp.cs`** -> AI Confidence: **99.29%**
3204. **`src/tests/Interop/StructMarshalling/PInvoke/MarshalStructAsLayoutSeq.cs`** -> AI Confidence: **99.29%**
3205. **`src/tests/JIT/Directed/Convert/value_numbering_checked_casts_of_constants_double.cs`** -> AI Confidence: **99.29%**
3206. **`src/tests/JIT/Directed/Convert/value_numbering_checked_casts_of_constants_float.cs`** -> AI Confidence: **99.29%**
3207. **`src/tests/JIT/Directed/Convert/value_numbering_checked_casts_of_constants_long.cs`** -> AI Confidence: **99.29%**
3208. **`src/tests/JIT/Directed/Misc/gettype/gettypetypeofmatrix.cs`** -> AI Confidence: **99.29%**
3209. **`src/tests/JIT/Directed/UnrollLoop/loop4.cs`** -> AI Confidence: **99.29%**
3210. **`src/tests/JIT/Directed/UnrollLoop/loop6.cs`** -> AI Confidence: **99.29%**
3211. **`src/tests/JIT/Directed/cmov/Bool_And_Op.cs`** -> AI Confidence: **99.29%**
3212. **`src/tests/JIT/Directed/cmov/Bool_No_Op.cs`** -> AI Confidence: **99.29%**
3213. **`src/tests/JIT/Directed/cmov/Bool_Or_Op.cs`** -> AI Confidence: **99.29%**
3214. **`src/tests/JIT/Directed/cmov/Bool_Xor_Op.cs`** -> AI Confidence: **99.29%**
3215. **`src/tests/JIT/Directed/cmov/Double_And_Op.cs`** -> AI Confidence: **99.29%**
3216. **`src/tests/JIT/Directed/cmov/Double_No_Op.cs`** -> AI Confidence: **99.29%**
3217. **`src/tests/JIT/Directed/cmov/Double_Or_Op.cs`** -> AI Confidence: **99.29%**
3218. **`src/tests/JIT/Directed/cmov/Double_Xor_Op.cs`** -> AI Confidence: **99.29%**
3219. **`src/tests/JIT/Directed/cmov/Float_And_Op.cs`** -> AI Confidence: **99.29%**
3220. **`src/tests/JIT/Directed/cmov/Float_No_Op.cs`** -> AI Confidence: **99.29%**
3221. **`src/tests/JIT/Directed/cmov/Float_Or_Op.cs`** -> AI Confidence: **99.29%**
3222. **`src/tests/JIT/Directed/cmov/Float_Xor_Op.cs`** -> AI Confidence: **99.29%**
3223. **`src/tests/JIT/Directed/cmov/Int_And_Op.cs`** -> AI Confidence: **99.29%**
3224. **`src/tests/JIT/Directed/cmov/Int_No_Op.cs`** -> AI Confidence: **99.29%**
3225. **`src/tests/JIT/Directed/cmov/Int_Or_Op.cs`** -> AI Confidence: **99.29%**
3226. **`src/tests/JIT/Directed/cmov/Int_Xor_Op.cs`** -> AI Confidence: **99.29%**
3227. **`src/tests/JIT/Directed/gettypetypeof/gettypetypeofmatrix.cs`** -> AI Confidence: **99.29%**
3228. **`src/tests/JIT/Directed/intrinsic/interlocked/IntrinsicTest_Overflow.cs`** -> AI Confidence: **99.29%**
3229. **`src/tests/JIT/Directed/nullabletypes/isinstvaluetype.cs`** -> AI Confidence: **99.29%**
3230. **`src/tests/JIT/Generics/Exceptions/specific_class_instance02.cs`** -> AI Confidence: **99.29%**
3231. **`src/tests/JIT/Generics/Exceptions/specific_class_static02.cs`** -> AI Confidence: **99.29%**
3232. **`src/tests/JIT/Generics/Exceptions/specific_struct_instance02.cs`** -> AI Confidence: **99.29%**
3233. **`src/tests/JIT/Generics/Exceptions/specific_struct_static02.cs`** -> AI Confidence: **99.29%**
3234. **`src/tests/JIT/Generics/Typeof/dynamicTypes.cs`** -> AI Confidence: **99.29%**
3235. **`src/tests/JIT/Generics/Typeof/objectBoxing.cs`** -> AI Confidence: **99.29%**
3236. **`src/tests/JIT/Generics/Typeof/refTypesdynamic.cs`** -> AI Confidence: **99.29%**
3237. **`src/tests/JIT/Methodical/AsgOp/i4/i4flat.cs`** -> AI Confidence: **99.29%**
3238. **`src/tests/JIT/Methodical/AsgOp/i8/i8flat.cs`** -> AI Confidence: **99.29%**
3239. **`src/tests/JIT/Methodical/AsgOp/r4/r4flat.cs`** -> AI Confidence: **99.29%**
3240. **`src/tests/JIT/Methodical/AsgOp/r8/r8flat.cs`** -> AI Confidence: **99.29%**
3241. **`src/tests/JIT/Methodical/MDArray/DataTypes/bool.cs`** -> AI Confidence: **99.29%**
3242. **`src/tests/JIT/Methodical/MDArray/DataTypes/byte.cs`** -> AI Confidence: **99.29%**
3243. **`src/tests/JIT/Methodical/MDArray/DataTypes/char.cs`** -> AI Confidence: **99.29%**
3244. **`src/tests/JIT/Methodical/MDArray/DataTypes/decimal.cs`** -> AI Confidence: **99.29%**
3245. **`src/tests/JIT/Methodical/MDArray/DataTypes/double.cs`** -> AI Confidence: **99.29%**
3246. **`src/tests/JIT/Methodical/MDArray/DataTypes/float.cs`** -> AI Confidence: **99.29%**
3247. **`src/tests/JIT/Methodical/MDArray/DataTypes/long.cs`** -> AI Confidence: **99.29%**
3248. **`src/tests/JIT/Methodical/MDArray/DataTypes/sbyte.cs`** -> AI Confidence: **99.29%**
3249. **`src/tests/JIT/Methodical/MDArray/DataTypes/short.cs`** -> AI Confidence: **99.29%**
3250. **`src/tests/JIT/Methodical/MDArray/DataTypes/uint.cs`** -> AI Confidence: **99.29%**
3251. **`src/tests/JIT/Methodical/MDArray/DataTypes/ulong.cs`** -> AI Confidence: **99.29%**
3252. **`src/tests/JIT/Methodical/MDArray/DataTypes/ushort.cs`** -> AI Confidence: **99.29%**
3253. **`src/tests/JIT/Methodical/MDArray/GaussJordan/classarr.cs`** -> AI Confidence: **99.29%**
3254. **`src/tests/JIT/Methodical/MDArray/GaussJordan/jaggedarr.cs`** -> AI Confidence: **99.29%**
3255. **`src/tests/JIT/Methodical/MDArray/GaussJordan/plainarr.cs`** -> AI Confidence: **99.29%**
3256. **`src/tests/JIT/Methodical/MDArray/GaussJordan/structarr.cs`** -> AI Confidence: **99.29%**
3257. **`src/tests/JIT/Methodical/MDArray/basics/classarr.cs`** -> AI Confidence: **99.29%**
3258. **`src/tests/JIT/Methodical/MDArray/basics/doublearr.cs`** -> AI Confidence: **99.29%**
3259. **`src/tests/JIT/Methodical/MDArray/basics/jaggedarr.cs`** -> AI Confidence: **99.29%**
3260. **`src/tests/JIT/Methodical/MDArray/basics/stringarr.cs`** -> AI Confidence: **99.29%**
3261. **`src/tests/JIT/Methodical/MDArray/basics/structarr.cs`** -> AI Confidence: **99.29%**
3262. **`src/tests/JIT/Methodical/NaN/arithm32.cs`** -> AI Confidence: **99.29%**
3263. **`src/tests/JIT/Methodical/NaN/arithm64.cs`** -> AI Confidence: **99.29%**
3264. **`src/tests/JIT/Methodical/NaN/r4NaNadd.cs`** -> AI Confidence: **99.29%**
3265. **`src/tests/JIT/Methodical/NaN/r4NaNdiv.cs`** -> AI Confidence: **99.29%**
3266. **`src/tests/JIT/Methodical/NaN/r4NaNmul.cs`** -> AI Confidence: **99.29%**
3267. **`src/tests/JIT/Methodical/NaN/r4NaNrem.cs`** -> AI Confidence: **99.29%**
3268. **`src/tests/JIT/Methodical/NaN/r4NaNsub.cs`** -> AI Confidence: **99.29%**
3269. **`src/tests/JIT/Methodical/NaN/r8NaNadd.cs`** -> AI Confidence: **99.29%**
3270. **`src/tests/JIT/Methodical/NaN/r8NaNdiv.cs`** -> AI Confidence: **99.29%**
3271. **`src/tests/JIT/Methodical/NaN/r8NaNmul.cs`** -> AI Confidence: **99.29%**
3272. **`src/tests/JIT/Methodical/NaN/r8NaNrem.cs`** -> AI Confidence: **99.29%**
3273. **`src/tests/JIT/Methodical/NaN/r8NaNsub.cs`** -> AI Confidence: **99.29%**
3274. **`src/tests/JIT/Methodical/divrem/div/decimaldiv.cs`** -> AI Confidence: **99.29%**
3275. **`src/tests/JIT/Methodical/divrem/div/i4div.cs`** -> AI Confidence: **99.29%**
3276. **`src/tests/JIT/Methodical/divrem/div/i8div.cs`** -> AI Confidence: **99.29%**
3277. **`src/tests/JIT/Methodical/divrem/div/r4div.cs`** -> AI Confidence: **99.29%**
3278. **`src/tests/JIT/Methodical/divrem/div/r8div.cs`** -> AI Confidence: **99.29%**
3279. **`src/tests/JIT/Methodical/divrem/div/u4div.cs`** -> AI Confidence: **99.29%**
3280. **`src/tests/JIT/Methodical/divrem/div/u8div.cs`** -> AI Confidence: **99.29%**
3281. **`src/tests/JIT/Methodical/divrem/rem/decimalrem.cs`** -> AI Confidence: **99.29%**
3282. **`src/tests/JIT/Methodical/divrem/rem/i4rem.cs`** -> AI Confidence: **99.29%**
3283. **`src/tests/JIT/Methodical/divrem/rem/i8rem.cs`** -> AI Confidence: **99.29%**
3284. **`src/tests/JIT/Methodical/divrem/rem/r4rem.cs`** -> AI Confidence: **99.29%**
3285. **`src/tests/JIT/Methodical/divrem/rem/r8rem.cs`** -> AI Confidence: **99.29%**
3286. **`src/tests/JIT/Methodical/divrem/rem/u4rem.cs`** -> AI Confidence: **99.29%**
3287. **`src/tests/JIT/Methodical/divrem/rem/u8rem.cs`** -> AI Confidence: **99.29%**
3288. **`src/tests/JIT/Methodical/eh/deadcode/loopstrswitchgoto.cs`** -> AI Confidence: **99.29%**
3289. **`src/tests/JIT/Methodical/eh/finallyexec/localgotoinahandler.cs`** -> AI Confidence: **99.29%**
3290. **`src/tests/JIT/Methodical/eh/finallyexec/switchincatch.cs`** -> AI Confidence: **99.29%**
3291. **`src/tests/JIT/Methodical/eh/finallyexec/tryCatchFinallyThrow_nonlocalexit1.cs`** -> AI Confidence: **99.29%**
3292. **`src/tests/JIT/Methodical/eh/finallyexec/tryCatchFinallyThrow_nonlocalexit2.cs`** -> AI Confidence: **99.29%**
3293. **`src/tests/JIT/Methodical/eh/finallyexec/tryCatchFinallyThrow_nonlocalexit3.cs`** -> AI Confidence: **99.29%**
3294. **`src/tests/JIT/Methodical/eh/finallyexec/tryCatchFinallyThrow_nonlocalexit4.cs`** -> AI Confidence: **99.29%**
3295. **`src/tests/JIT/Methodical/eh/interactions/strswitchfinal.cs`** -> AI Confidence: **99.29%**
3296. **`src/tests/JIT/Methodical/eh/nested/general/cascadedcatch.cs`** -> AI Confidence: **99.29%**
3297. **`src/tests/JIT/Methodical/eh/nested/general/rethrowincatchnestedinfinally.cs`** -> AI Confidence: **99.29%**
3298. **`src/tests/JIT/Methodical/eh/nested/general/throwinfinallynestedintry.cs`** -> AI Confidence: **99.29%**
3299. **`src/tests/JIT/Methodical/eh/nested/general/throwinnestedfinally.cs`** -> AI Confidence: **99.29%**
3300. **`src/tests/JIT/Methodical/eh/nested/nonlocalexit/throwinfinally_50.cs`** -> AI Confidence: **99.29%**
3301. **`src/tests/JIT/Methodical/eh/nested/nonlocalexit/throwinfinallynestedintry_30.cs`** -> AI Confidence: **99.29%**
3302. **`src/tests/JIT/Methodical/eh/nested/nonlocalexit/throwinfinallyrecursive_20.cs`** -> AI Confidence: **99.29%**
3303. **`src/tests/JIT/Methodical/eh/regress/asurt/140713/innerFinally.cs`** -> AI Confidence: **99.29%**
3304. **`src/tests/JIT/Methodical/eh/regress/asurt/141358/uncaughtException.cs`** -> AI Confidence: **99.29%**
3305. **`src/tests/JIT/Methodical/explicit/misc/explicit1.cs`** -> AI Confidence: **99.29%**
3306. **`src/tests/JIT/Methodical/explicit/misc/explicit2.cs`** -> AI Confidence: **99.29%**
3307. **`src/tests/JIT/Methodical/explicit/misc/explicit3.cs`** -> AI Confidence: **99.29%**
3308. **`src/tests/JIT/Methodical/explicit/misc/explicit4.cs`** -> AI Confidence: **99.29%**
3309. **`src/tests/JIT/Methodical/explicit/misc/explicit5.cs`** -> AI Confidence: **99.29%**
3310. **`src/tests/JIT/Methodical/explicit/misc/explicit6.cs`** -> AI Confidence: **99.29%**
3311. **`src/tests/JIT/Methodical/explicit/misc/explicit7.cs`** -> AI Confidence: **99.29%**
3312. **`src/tests/JIT/Methodical/explicit/misc/explicit8.cs`** -> AI Confidence: **99.29%**
3313. **`src/tests/JIT/Methodical/int64/unsigned/implicit_promotion.cs`** -> AI Confidence: **99.29%**
3314. **`src/tests/JIT/Methodical/refany/format.cs`** -> AI Confidence: **99.29%**
3315. **`src/tests/JIT/Performance/CodeQuality/Benchstones/BenchF/LLoops/LLoops.cs`** -> AI Confidence: **99.29%**
3316. **`src/tests/JIT/Performance/CodeQuality/Benchstones/BenchF/MatInv4/MatInv4.cs`** -> AI Confidence: **99.29%**
3317. **`src/tests/JIT/Performance/CodeQuality/Benchstones/BenchI/Puzzle/Puzzle.cs`** -> AI Confidence: **99.29%**
3318. **`src/tests/JIT/Performance/CodeQuality/Benchstones/MDBenchF/MDLLoops/MDLLoops.cs`** -> AI Confidence: **99.29%**
3319. **`src/tests/JIT/Performance/CodeQuality/Benchstones/MDBenchI/MDPuzzle/MDPuzzle.cs`** -> AI Confidence: **99.29%**
3320. **`src/tests/JIT/Performance/CodeQuality/Bytemark/Huffman.cs`** -> AI Confidence: **99.29%**
3321. **`src/tests/JIT/Performance/CodeQuality/Bytemark/assign_jagged.cs`** -> AI Confidence: **99.29%**
3322. **`src/tests/JIT/Performance/CodeQuality/Bytemark/assign_rect.cs`** -> AI Confidence: **99.29%**
3323. **`src/tests/JIT/Performance/CodeQuality/Bytemark/bitops.cs`** -> AI Confidence: **99.29%**
3324. **`src/tests/JIT/Performance/CodeQuality/Bytemark/emfloat.cs`** -> AI Confidence: **99.29%**
3325. **`src/tests/JIT/Performance/CodeQuality/Bytemark/emfloatclass.cs`** -> AI Confidence: **99.29%**
3326. **`src/tests/JIT/Performance/CodeQuality/Bytemark/ludecomp.cs`** -> AI Confidence: **99.29%**
3327. **`src/tests/JIT/Performance/CodeQuality/Bytemark/numericsort.cs`** -> AI Confidence: **99.29%**
3328. **`src/tests/JIT/Performance/CodeQuality/SciMark/Random.cs`** -> AI Confidence: **99.29%**
3329. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M09.5-PDC/b31912/b31912.cs`** -> AI Confidence: **99.29%**
3330. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M11-Beta1/b41470/b41470.cs`** -> AI Confidence: **99.29%**
3331. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M12-Beta2/b71005/b71005.cs`** -> AI Confidence: **99.29%**
3332. **`src/tests/JIT/Regression/CLR-x86-JIT/V2.0-RTM/b369916/b369916.cs`** -> AI Confidence: **99.29%**
3333. **`src/tests/JIT/Regression/CLR-x86-JIT/v2.1/b569942/b569942.cs`** -> AI Confidence: **99.29%**
3334. **`src/tests/JIT/Regression/CLR-x86-JIT/v2.1/b608198/b608198.cs`** -> AI Confidence: **99.29%**
3335. **`src/tests/JIT/Regression/JitBlue/GitHub_18056/Bool_And_Op.cs`** -> AI Confidence: **99.29%**
3336. **`src/tests/JIT/Regression/JitBlue/GitHub_20838/GitHub_20838.cs`** -> AI Confidence: **99.29%**
3337. **`src/tests/JIT/Regression/JitBlue/Runtime_93342/Runtime_93342.cs`** -> AI Confidence: **99.29%**
3338. **`src/tests/JIT/Regression/VS-ia64-JIT/M00/b111192/strswitch2.cs`** -> AI Confidence: **99.29%**
3339. **`src/tests/JIT/Regression/VS-ia64-JIT/M00/b141358/test.cs`** -> AI Confidence: **99.29%**
3340. **`src/tests/JIT/Regression/VS-ia64-JIT/V1.2-M01/b10827/MT_DEATH.cs`** -> AI Confidence: **99.29%**
3341. **`src/tests/JIT/Regression/VS-ia64-JIT/V1.2-M02/b26496/_1d6bgof.cs`** -> AI Confidence: **99.29%**
3342. **`src/tests/JIT/Regression/VS-ia64-JIT/V2.0-Beta2/b184799/b184799.cs`** -> AI Confidence: **99.29%**
3343. **`src/tests/JIT/Regression/VS-ia64-JIT/V2.0-Beta2/b311420/b311420.cs`** -> AI Confidence: **99.29%**
3344. **`src/tests/JIT/Regression/VS-ia64-JIT/V2.0-RTM/b539509/b539509.cs`** -> AI Confidence: **99.29%**
3345. **`src/tests/JIT/jit64/eh/FinallyExec/nestedTryRegionsWithSameOffset1.cs`** -> AI Confidence: **99.29%**
3346. **`src/tests/JIT/jit64/eh/FinallyExec/nestedTryRegionsWithSameOffset3.cs`** -> AI Confidence: **99.29%**
3347. **`src/tests/JIT/jit64/opt/cse/arrayexpr1.cs`** -> AI Confidence: **99.29%**
3348. **`src/tests/JIT/jit64/opt/cse/arrayexpr2.cs`** -> AI Confidence: **99.29%**
3349. **`src/tests/JIT/jit64/opt/cse/fieldExprUnchecked1.cs`** -> AI Confidence: **99.29%**
3350. **`src/tests/JIT/jit64/opt/cse/fieldexpr1.cs`** -> AI Confidence: **99.29%**
3351. **`src/tests/JIT/jit64/opt/cse/fieldexpr1_1.cs`** -> AI Confidence: **99.29%**
3352. **`src/tests/JIT/jit64/opt/cse/fieldexpr2.cs`** -> AI Confidence: **99.29%**
3353. **`src/tests/JIT/jit64/opt/cse/mixedexpr1.cs`** -> AI Confidence: **99.29%**
3354. **`src/tests/JIT/jit64/opt/cse/simpleexpr1.cs`** -> AI Confidence: **99.29%**
3355. **`src/tests/JIT/jit64/opt/cse/simpleexpr1_1.cs`** -> AI Confidence: **99.29%**
3356. **`src/tests/JIT/jit64/opt/cse/simpleexpr2.cs`** -> AI Confidence: **99.29%**
3357. **`src/tests/JIT/jit64/opt/cse/simpleexpr3.cs`** -> AI Confidence: **99.29%**
3358. **`src/tests/JIT/jit64/opt/cse/simpleexpr4.cs`** -> AI Confidence: **99.29%**
3359. **`src/tests/JIT/jit64/opt/cse/staticFieldExpr1.cs`** -> AI Confidence: **99.29%**
3360. **`src/tests/JIT/jit64/opt/cse/staticFieldExpr1_1.cs`** -> AI Confidence: **99.29%**
3361. **`src/tests/JIT/jit64/opt/cse/staticFieldExprUnchecked1.cs`** -> AI Confidence: **99.29%**
3362. **`src/tests/JIT/jit64/opt/cse/volatilefield.cs`** -> AI Confidence: **99.29%**
3363. **`src/tests/JIT/jit64/opt/cse/volatilestaticfield.cs`** -> AI Confidence: **99.29%**
3364. **`src/tests/JIT/jit64/opt/lur/lur_02.cs`** -> AI Confidence: **99.29%**
3365. **`src/tests/JIT/jit64/regress/vsw/524070/test1.cs`** -> AI Confidence: **99.29%**
3366. **`src/tests/JIT/jit64/regress/vsw/524070/test2.cs`** -> AI Confidence: **99.29%**
3367. **`src/tests/JIT/jit64/regress/vsw/539509/test1.cs`** -> AI Confidence: **99.29%**
3368. **`src/tests/Loader/classloader/explicitlayout/misc/case10.cs`** -> AI Confidence: **99.29%**
3369. **`src/tests/Loader/classloader/explicitlayout/objrefandnonobjrefoverlap/case9.cs`** -> AI Confidence: **99.29%**
3370. **`src/tests/baseservices/exceptions/generics/GenericExceptions.cs`** -> AI Confidence: **99.29%**
3371. **`src/tests/baseservices/exceptions/regressions/V1/SEH/VJ/TryCatch.cs`** -> AI Confidence: **99.29%**
3372. **`src/tests/nativeaot/SmokeTests/FrameworkStrings/Program.cs`** -> AI Confidence: **99.29%**
3373. **`src/tests/tracing/common/Assert.cs`** -> AI Confidence: **99.29%**
3374. **`src/tools/ilasm/src/ILAssembler/StringHelpers.cs`** -> AI Confidence: **99.29%**
3375. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Assertions/KeptBaseOnTypeInAssemblyAttribute.cs`** -> AI Confidence: **99.29%**
3376. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Assertions/KeptInterfaceOnTypeInAssemblyAttribute.cs`** -> AI Confidence: **99.29%**
3377. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Assertions/RemovedInterfaceOnTypeInAssemblyAttribute.cs`** -> AI Confidence: **99.29%**
3378. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Metadata/SetupCompileAfterAttribute.cs`** -> AI Confidence: **99.29%**
3379. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Metadata/SetupCompileBeforeAttribute.cs`** -> AI Confidence: **99.29%**
3380. **`src/tools/illink/test/Mono.Linker.Tests.Cases/RequiresCapability/Dependencies/RequiresInCopyAssembly.cs`** -> AI Confidence: **99.29%**
3381. **`src/native/external/libunwind/configure.ac`** -> AI Confidence: **99.29%**
3382. **`src/coreclr/inc/CrstTypes.def`** -> AI Confidence: **99.29%**
3383. **`src/coreclr/inc/llvm/Dwarf.def`** -> AI Confidence: **99.29%**
3384. **`src/coreclr/jit/smopcodemap.def`** -> AI Confidence: **99.29%**
3385. **`src/native/external/libunwind/Makefile.am`** -> AI Confidence: **99.29%**
3386. **`src/mono/browser/runtime/es6/dotnet.es6.pre.js`** -> AI Confidence: **99.29%**
3387. **`src/coreclr/ilasm/asmparse.y`** -> AI Confidence: **99.29%**
3388. **`src/libraries/Common/tests/System/Net/EnterpriseTests/setup/apacheweb/Dockerfile`** -> AI Confidence: **99.29%**
3389. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/Dockerfile`** -> AI Confidence: **99.29%**
3390. **`src/native/libs/Common/JavaScript/loader/config.ts`** -> AI Confidence: **99.29%**
3391. **`src/native/libs/System.Globalization.Native/pal_calendarData.m`** -> AI Confidence: **99.29%**
3392. **`src/native/libs/System.Globalization.Native/pal_casing.m`** -> AI Confidence: **99.29%**
3393. **`src/native/libs/System.Globalization.Native/pal_collation.m`** -> AI Confidence: **99.29%**
3394. **`src/native/libs/System.Globalization.Native/pal_normalization.m`** -> AI Confidence: **99.29%**
3395. **`src/native/libs/System.Globalization.Native/pal_timeZoneInfo.m`** -> AI Confidence: **99.29%**
3396. **`src/native/libs/System.Native/pal_datetime.m`** -> AI Confidence: **99.29%**
3397. **`src/native/libs/System.Native/pal_log.m`** -> AI Confidence: **99.29%**
3398. **`src/native/libs/System.Native/pal_searchpath.m`** -> AI Confidence: **99.29%**
3399. **`src/native/libs/System.Security.Cryptography.Native.Apple/pal_networkframework.m`** -> AI Confidence: **99.29%**
3400. **`src/tasks/AppleAppBuilder/Templates/util.m`** -> AI Confidence: **99.29%**
3401. **`src/native/external/libunwind/src/x86_64/Gtrace.c`** -> AI Confidence: **99.28%**
3402. **`src/coreclr/inc/winwrap.h`** -> AI Confidence: **99.27%**
3403. **`src/coreclr/jit/emitdef.h`** -> AI Confidence: **99.27%**
3404. **`src/coreclr/jit/emitfmts.h`** -> AI Confidence: **99.27%**
3405. **`src/coreclr/jit/instrs.h`** -> AI Confidence: **99.27%**
3406. **`src/coreclr/jit/register.h`** -> AI Confidence: **99.27%**
3407. **`src/native/external/zlib-ng/zendian.h`** -> AI Confidence: **99.27%**
3408. **`src/coreclr/pal/inc/strsafe.h`** -> AI Confidence: **99.26%**
3409. **`src/mono/mono/utils/mono-threads-debug.h`** -> AI Confidence: **99.26%**
3410. **`src/native/external/zlib-ng/inflate_p.h`** -> AI Confidence: **99.26%**
3411. **`src/coreclr/scripts/jitutil.py`** -> AI Confidence: **99.25%**
3412. **`src/mono/mono/metadata/handle.h`** -> AI Confidence: **99.25%**
3413. **`src/mono/mono/utils/mono-os-mutex.h`** -> AI Confidence: **99.25%**
3414. **`src/native/external/brotli/c/common/platform.h`** -> AI Confidence: **99.25%**
3415. **`src/native/external/libunwind/src/x86_64/Gos-freebsd.c`** -> AI Confidence: **99.25%**
3416. **`src/native/external/libunwind/tests/Gtest-resume-sig.c`** -> AI Confidence: **99.25%**
3417. **`src/native/external/zstd/lib/common/xxhash.h`** -> AI Confidence: **99.25%**
3418. **`src/coreclr/gc/gc.cpp`** -> AI Confidence: **99.25%**
3419. **`src/coreclr/gc/gcee.cpp`** -> AI Confidence: **99.25%**
3420. **`src/coreclr/gc/vxsort/vxsort.h`** -> AI Confidence: **99.25%**
3421. **`src/coreclr/inc/stresslog.h`** -> AI Confidence: **99.25%**
3422. **`src/mono/mono/utils/mono-os-semaphore.h`** -> AI Confidence: **99.25%**
3423. **`src/native/external/llvm-libunwind/src/AddressSpace.hpp`** -> AI Confidence: **99.25%**
3424. **`src/native/external/llvm-libunwind/src/DwarfParser.hpp`** -> AI Confidence: **99.25%**
3425. **`src/native/external/rapidjson/reader.h`** -> AI Confidence: **99.25%**
3426. **`src/native/external/zlib-ng/inffast_tpl.h`** -> AI Confidence: **99.25%**
3427. **`src/native/libs/Common/pal_error_common.h`** -> AI Confidence: **99.25%**
3428. **`src/native/minipal/thread.h`** -> AI Confidence: **99.25%**
3429. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiHttpWorld.wit.imports.wasi.io.v0_2_0.IStreams.cs`** -> AI Confidence: **99.25%**
3430. **`src/tests/Common/scripts/crossgen2_comparison.py`** -> AI Confidence: **99.24%**
3431. **`src/coreclr/pal/src/include/pal/context.h`** -> AI Confidence: **99.24%**
3432. **`src/mono/mono/eglib/glib.h`** -> AI Confidence: **99.24%**
3433. **`src/mono/mono/eglib/test/module.c`** -> AI Confidence: **99.24%**
3434. **`src/mono/mono/eventpipe/ds-rt-mono.c`** -> AI Confidence: **99.24%**
3435. **`src/mono/mono/eventpipe/ep-rt-mono.c`** -> AI Confidence: **99.24%**
3436. **`src/mono/mono/eventpipe/test/ep-buffer-tests.c`** -> AI Confidence: **99.24%**
3437. **`src/mono/mono/metadata/dynamic-stream.c`** -> AI Confidence: **99.24%**
3438. **`src/mono/mono/metadata/environment.c`** -> AI Confidence: **99.24%**
3439. **`src/mono/mono/metadata/icall-table.c`** -> AI Confidence: **99.24%**
3440. **`src/mono/mono/metadata/mono-config.c`** -> AI Confidence: **99.24%**
3441. **`src/mono/mono/mini/exceptions-x86.c`** -> AI Confidence: **99.24%**
3442. **`src/mono/mono/mini/mini-cross-helpers.c`** -> AI Confidence: **99.24%**
3443. **`src/mono/mono/mini/mini-s390x.h`** -> AI Confidence: **99.24%**
3444. **`src/mono/mono/mini/mini.h`** -> AI Confidence: **99.24%**
3445. **`src/mono/mono/sgen/sgen-nursery-allocator.c`** -> AI Confidence: **99.24%**
3446. **`src/mono/mono/utils/mono-dl.c`** -> AI Confidence: **99.24%**
3447. **`src/mono/mono/utils/mono-log-posix.c`** -> AI Confidence: **99.24%**
3448. **`src/mono/mono/utils/mono-log-windows.c`** -> AI Confidence: **99.24%**
3449. **`src/mono/mono/utils/mono-mmap-wasm.c`** -> AI Confidence: **99.24%**
3450. **`src/mono/mono/utils/mono-threads-posix-signals.c`** -> AI Confidence: **99.24%**
3451. **`src/mono/mono/utils/mono-threads-windows.c`** -> AI Confidence: **99.24%**
3452. **`src/native/eventpipe/ep-file.c`** -> AI Confidence: **99.24%**
3453. **`src/native/eventpipe/ep-provider.c`** -> AI Confidence: **99.24%**
3454. **`src/native/external/libunwind/src/s390x/Ginit.c`** -> AI Confidence: **99.24%**
3455. **`src/native/external/libunwind/tests/ia64-test-dyn1.c`** -> AI Confidence: **99.24%**
3456. **`src/native/external/libunwind/tests/ia64-test-setjmp.c`** -> AI Confidence: **99.24%**
3457. **`src/native/external/llvm-libunwind/src/UnwindLevel1.c`** -> AI Confidence: **99.24%**
3458. **`src/native/external/zlib-ng/arch/x86/chunkset_avx512.c`** -> AI Confidence: **99.24%**
3459. **`src/native/external/zstd/lib/legacy/zstd_v04.c`** -> AI Confidence: **99.24%**
3460. **`src/native/external/zstd/lib/legacy/zstd_v07.c`** -> AI Confidence: **99.24%**
3461. **`src/native/libs/System.Native/entrypoints.c`** -> AI Confidence: **99.24%**
3462. **`src/native/libs/System.Native/pal_console.c`** -> AI Confidence: **99.24%**
3463. **`src/native/libs/System.Native/pal_datetime.c`** -> AI Confidence: **99.24%**
3464. **`src/native/libs/System.Native/pal_networkstatistics.c`** -> AI Confidence: **99.24%**
3465. **`src/native/libs/System.Native/pal_signal.c`** -> AI Confidence: **99.24%**
3466. **`src/native/libs/System.Native/pal_threading.c`** -> AI Confidence: **99.24%**
3467. **`src/native/libs/System.Security.Cryptography.Native/opensslshim.h`** -> AI Confidence: **99.24%**
3468. **`src/tasks/AndroidAppBuilder/Templates/monodroid-coreclr.c`** -> AI Confidence: **99.24%**
3469. **`src/tasks/AndroidAppBuilder/Templates/monodroid.c`** -> AI Confidence: **99.24%**
3470. **`src/coreclr/gc/vxsort/standalone/simple_bench/demo.cpp`** -> AI Confidence: **99.24%**
3471. **`src/coreclr/inc/palclr.h`** -> AI Confidence: **99.24%**
3472. **`src/coreclr/md/compiler/regmeta_compilersupport.cpp`** -> AI Confidence: **99.24%**
3473. **`src/coreclr/nativeaot/Runtime/ThunksMapping.cpp`** -> AI Confidence: **99.24%**
3474. **`src/coreclr/nativeaot/Runtime/event.cpp`** -> AI Confidence: **99.24%**
3475. **`src/coreclr/nativeaot/Runtime/windows/CoffNativeCodeManager.cpp`** -> AI Confidence: **99.24%**
3476. **`src/coreclr/nativeaot/Runtime/windows/PalMinWin.cpp`** -> AI Confidence: **99.24%**
3477. **`src/coreclr/pal/src/exception/seh.cpp`** -> AI Confidence: **99.24%**
3478. **`src/coreclr/pal/src/exception/signal.cpp`** -> AI Confidence: **99.24%**
3479. **`src/coreclr/pal/src/loader/module.cpp`** -> AI Confidence: **99.24%**
3480. **`src/coreclr/utilcode/safewrap.cpp`** -> AI Confidence: **99.24%**
3481. **`src/mono/mono/mini/mini-llvm-cpp.cpp`** -> AI Confidence: **99.24%**
3482. **`src/native/corehost/comhost/clsidmap.cpp`** -> AI Confidence: **99.24%**
3483. **`src/native/corehost/hostmisc/pal.windows.cpp`** -> AI Confidence: **99.24%**
3484. **`src/native/eventpipe/ep-rt-config.h`** -> AI Confidence: **99.24%**
3485. **`src/native/external/brotli/c/enc/hash.h`** -> AI Confidence: **99.24%**
3486. **`src/native/external/brotli/c/enc/quality.h`** -> AI Confidence: **99.24%**
3487. **`src/native/external/libunwind/include/tdep-mips/libunwind_i.h`** -> AI Confidence: **99.24%**
3488. **`src/native/external/llvm-libunwind/src/Unwind-seh.cpp`** -> AI Confidence: **99.24%**
3489. **`src/native/external/rapidjson/writer.h`** -> AI Confidence: **99.24%**
3490. **`src/native/external/zstd/lib/common/zstd_internal.h`** -> AI Confidence: **99.24%**
3491. **`src/native/minipal/getexepath.h`** -> AI Confidence: **99.24%**
3492. **`src/tests/nativeaot/SmokeTests/PInvoke/PInvokeNative.cpp`** -> AI Confidence: **99.24%**
3493. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/RuntimeAssembly.cs`** -> AI Confidence: **99.24%**
3494. **`src/coreclr/System.Private.CoreLib/src/System/RuntimeHandles.cs`** -> AI Confidence: **99.24%**
3495. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Augments/ReflectionAugments.cs`** -> AI Confidence: **99.24%**
3496. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/GC.NativeAot.cs`** -> AI Confidence: **99.24%**
3497. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/General/Helpers.cs`** -> AI Confidence: **99.24%**
3498. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/MethodInfos/RuntimeMethodInfo.cs`** -> AI Confidence: **99.24%**
3499. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/CompilerServices/RuntimeHelpers.NativeAot.cs`** -> AI Confidence: **99.24%**
3500. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/RuntimeType.NativeAot.cs`** -> AI Confidence: **99.24%**
3501. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/NativeLayoutInfoLoadContext.cs`** -> AI Confidence: **99.24%**
3502. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.ConstructedGenericMethodsLookup.cs`** -> AI Confidence: **99.24%**
3503. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.ConstructedGenericTypesLookup.cs`** -> AI Confidence: **99.24%**
3504. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/TypeSystem/RuntimeNoMetadataType.cs`** -> AI Confidence: **99.24%**
3505. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/TypeSystem/TypeSystemContext.Runtime.cs`** -> AI Confidence: **99.24%**
3506. **`src/coreclr/tools/ILTrim.Core/ModuleWriter.cs`** -> AI Confidence: **99.24%**
3507. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/GenericArgumentDataFlow.cs`** -> AI Confidence: **99.24%**
3508. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/InterfaceGenericVirtualMethodTableNode.cs`** -> AI Confidence: **99.24%**
3509. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/MstatObjectDumper.cs`** -> AI Confidence: **99.24%**
3510. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/SubstitutionProvider.cs`** -> AI Confidence: **99.24%**
3511. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun.Tests/TestCasesRunner/R2RTestCaseCompiler.cs`** -> AI Confidence: **99.24%**
3512. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun.Tests/TestCasesRunner/R2RTestRunner.cs`** -> AI Confidence: **99.24%**
3513. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunCompilationModuleGroupBase.cs`** -> AI Confidence: **99.24%**
3514. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunTableManager.cs`** -> AI Confidence: **99.24%**
3515. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/MemberAssertionsCollector.cs`** -> AI Confidence: **99.24%**
3516. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/TestCaseCollector.cs`** -> AI Confidence: **99.24%**
3517. **`src/coreclr/tools/cdac-build-tool/DataDescriptorModel.cs`** -> AI Confidence: **99.24%**
3518. **`src/coreclr/tools/dotnet-pgo/MethodMemoryMap.cs`** -> AI Confidence: **99.24%**
3519. **`src/coreclr/tools/dotnet-pgo/MibcEmitter.cs`** -> AI Confidence: **99.24%**
3520. **`src/coreclr/tools/dotnet-pgo/PgoRootCommand.cs`** -> AI Confidence: **99.24%**
3521. **`src/coreclr/tools/dotnet-pgo/TraceTypeSystemContext.cs`** -> AI Confidence: **99.24%**
3522. **`src/coreclr/tools/dotnet-pgo/TypeRefTypeSystem/TypeRefTypeSystemContext.cs`** -> AI Confidence: **99.24%**
3523. **`src/coreclr/tools/dotnet-pgo/TypeRefTypeSystem/TypeRefTypeSystemType.cs`** -> AI Confidence: **99.24%**
3524. **`src/installer/managed/Microsoft.NET.HostModel/ComHost/ClsidMap.cs`** -> AI Confidence: **99.24%**
3525. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.Aead.cs`** -> AI Confidence: **99.24%**
3526. **`src/libraries/Common/src/Interop/Unix/System.Security.Cryptography.Native/Interop.Ssl.cs`** -> AI Confidence: **99.24%**
3527. **`src/libraries/Common/src/Roslyn/SyntaxValueProvider_ForAttributeWithMetadataName.cs`** -> AI Confidence: **99.24%**
3528. **`src/libraries/Common/src/System/Security/Cryptography/CompositeMLDsaManaged.cs`** -> AI Confidence: **99.24%**
3529. **`src/libraries/Common/tests/System/Net/Http/Http2LoopbackConnection.cs`** -> AI Confidence: **99.24%**
3530. **`src/libraries/Common/tests/System/Net/Http/HttpClientHandlerTest.Decompression.cs`** -> AI Confidence: **99.24%**
3531. **`src/libraries/Common/tests/System/Net/Http/LoopbackProxyServer.cs`** -> AI Confidence: **99.24%**
3532. **`src/libraries/Common/tests/System/Net/Http/LoopbackServer.cs`** -> AI Confidence: **99.24%**
3533. **`src/libraries/Common/tests/TestUtilities/System/PlatformDetection.cs`** -> AI Confidence: **99.24%**
3534. **`src/libraries/Common/tests/Tests/System/Net/aspnetcore/Http2/DynamicTableTest.cs`** -> AI Confidence: **99.24%**
3535. **`src/libraries/Common/tests/Tests/System/Net/aspnetcore/Http3/QPackDecoderTest.cs`** -> AI Confidence: **99.24%**
3536. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/ServiceLookup/Expressions/ExpressionResolverBuilder.cs`** -> AI Confidence: **99.24%**
3537. **`src/libraries/Microsoft.Extensions.Logging.Abstractions/tests/Microsoft.Extensions.Logging.Generators.Tests/LoggerMessageGeneratedCodeTests.cs`** -> AI Confidence: **99.24%**
3538. **`src/libraries/Microsoft.Win32.SystemEvents/tests/SystemEvents.CreateTimer.cs`** -> AI Confidence: **99.24%**
3539. **`src/libraries/System.Collections.Concurrent/tests/ProducerConsumerCollectionTests.cs`** -> AI Confidence: **99.24%**
3540. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Primitives/ComposablePartCatalog.cs`** -> AI Confidence: **99.24%**
3541. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Diagnostics/ListenerElementsCollection.cs`** -> AI Confidence: **99.24%**
3542. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLDateTime.cs`** -> AI Confidence: **99.24%**
3543. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLDouble.cs`** -> AI Confidence: **99.24%**
3544. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLGuid.cs`** -> AI Confidence: **99.24%**
3545. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLSingle.cs`** -> AI Confidence: **99.24%**
3546. **`src/libraries/System.Data.Common/tests/System/Data/DataSetTest.cs`** -> AI Confidence: **99.24%**
3547. **`src/libraries/System.Data.Common/tests/System/Data/DataSetTypedDataSetTest.cs`** -> AI Confidence: **99.24%**
3548. **`src/libraries/System.Data.Odbc/src/Common/System/Data/Common/AdapterUtil.Odbc.cs`** -> AI Confidence: **99.24%**
3549. **`src/libraries/System.Data.OleDb/src/System/Data/Common/AdapterUtil.cs`** -> AI Confidence: **99.24%**
3550. **`src/libraries/System.Diagnostics.Process/tests/ProcessStartInfoTests.cs`** -> AI Confidence: **99.24%**
3551. **`src/libraries/System.Diagnostics.Process/tests/ProcessTests.Windows.cs`** -> AI Confidence: **99.24%**
3552. **`src/libraries/System.Diagnostics.Process/tests/ProcessTests.cs`** -> AI Confidence: **99.24%**
3553. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/TokenGroupsSet.cs`** -> AI Confidence: **99.24%**
3554. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarHelpers.cs`** -> AI Confidence: **99.24%**
3555. **`src/libraries/System.IO.Compression/tests/CompressionStreamUnitTests.ZLib.cs`** -> AI Confidence: **99.24%**
3556. **`src/libraries/System.IO.Ports/tests/SerialPort/GetPortNames.cs`** -> AI Confidence: **99.24%**
3557. **`src/libraries/System.IO.Ports/tests/SerialStream/WriteTimeout.cs`** -> AI Confidence: **99.24%**
3558. **`src/libraries/System.Linq.Expressions/src/System/Dynamic/DynamicObject.cs`** -> AI Confidence: **99.24%**
3559. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/DelegateHelpers.cs`** -> AI Confidence: **99.24%**
3560. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/StackSpiller.cs`** -> AI Confidence: **99.24%**
3561. **`src/libraries/System.Linq.Expressions/src/System/Runtime/CompilerServices/CallSite.cs`** -> AI Confidence: **99.24%**
3562. **`src/libraries/System.Management/src/System/Management/InteropClasses/WMIInterop.cs`** -> AI Confidence: **99.24%**
3563. **`src/libraries/System.Net.Http.Json/src/System/Net/Http/Json/HttpContentJsonExtensions.AsyncEnumerable.cs`** -> AI Confidence: **99.24%**
3564. **`src/libraries/System.Net.Http.WinHttpHandler/tests/UnitTests/FakeInterop.cs`** -> AI Confidence: **99.24%**
3565. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/DecompressionHandler.cs`** -> AI Confidence: **99.24%**
3566. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiInputStream.cs`** -> AI Confidence: **99.24%**
3567. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/Configuration.cs`** -> AI Confidence: **99.24%**
3568. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/LogHttpEventListener.cs`** -> AI Confidence: **99.24%**
3569. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/StressClient.cs`** -> AI Confidence: **99.24%**
3570. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/StressServer.cs`** -> AI Confidence: **99.24%**
3571. **`src/libraries/System.Net.Http/tests/UnitTests/HPack/HPackRoundtripTests.cs`** -> AI Confidence: **99.24%**
3572. **`src/libraries/System.Net.Http/tests/UnitTests/HttpWindowsProxyTest.cs`** -> AI Confidence: **99.24%**
3573. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/MsQuicConfiguration.Cache.cs`** -> AI Confidence: **99.24%**
3574. **`src/libraries/System.Net.Quic/src/System/Net/Quic/QuicListener.cs`** -> AI Confidence: **99.24%**
3575. **`src/libraries/System.Net.Quic/tests/FunctionalTests/QuicTestCollection.cs`** -> AI Confidence: **99.24%**
3576. **`src/libraries/System.Net.Security/src/System/Net/NegotiateAuthenticationPal.ManagedNtlm.cs`** -> AI Confidence: **99.24%**
3577. **`src/libraries/System.Net.Security/tests/FunctionalTests/CertificateValidationRemoteServer.cs`** -> AI Confidence: **99.24%**
3578. **`src/libraries/System.Net.Security/tests/FunctionalTests/SslStreamSystemDefaultsTest.cs`** -> AI Confidence: **99.24%**
3579. **`src/libraries/System.Net.Security/tests/FunctionalTests/TestHelper.cs`** -> AI Confidence: **99.24%**
3580. **`src/libraries/System.Net.Security/tests/StressTests/SslStress/StressOperations.cs`** -> AI Confidence: **99.24%**
3581. **`src/libraries/System.Net.Security/tests/UnitTests/NegotiateAuthenticationTests.cs`** -> AI Confidence: **99.24%**
3582. **`src/libraries/System.Net.WebSockets.Client/tests/LoopbackServer/ReadAheadWebSocket.cs`** -> AI Confidence: **99.24%**
3583. **`src/libraries/System.Net.WebSockets.Client/tests/wasm/BrowserTimerThrottlingTest.cs`** -> AI Confidence: **99.24%**
3584. **`src/libraries/System.Private.CoreLib/src/System/Globalization/TextInfo.cs`** -> AI Confidence: **99.24%**
3585. **`src/libraries/System.Private.CoreLib/src/System/RuntimeType.cs`** -> AI Confidence: **99.24%**
3586. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/SearchValues.cs`** -> AI Confidence: **99.24%**
3587. **`src/libraries/System.Private.CoreLib/src/System/Span.cs`** -> AI Confidence: **99.24%**
3588. **`src/libraries/System.Private.CoreLib/src/System/Text/Encoding.cs`** -> AI Confidence: **99.24%**
3589. **`src/libraries/System.Private.CoreLib/src/System/Threading/ThreadPool.Browser.cs`** -> AI Confidence: **99.24%**
3590. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/ReflectionJsonFormatReader.cs`** -> AI Confidence: **99.24%**
3591. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ReflectionXmlFormatReader.cs`** -> AI Confidence: **99.24%**
3592. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XPathQueryGenerator.cs`** -> AI Confidence: **99.24%**
3593. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlDictionary.cs`** -> AI Confidence: **99.24%**
3594. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/BridgeHelpers.cs`** -> AI Confidence: **99.24%**
3595. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/FunctionalTests.cs`** -> AI Confidence: **99.24%**
3596. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlValidatingReaderImplAsync.cs`** -> AI Confidence: **99.24%**
3597. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchemaDataType.cs`** -> AI Confidence: **99.24%**
3598. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlQuerySequence.cs`** -> AI Confidence: **99.24%**
3599. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XsltFunctions.cs`** -> AI Confidence: **99.24%**
3600. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/Avt.cs`** -> AI Confidence: **99.24%**
3601. **`src/libraries/System.Private.Xml/tests/XmlSerializer/XmlSerializerTests.RuntimeOnly.cs`** -> AI Confidence: **99.24%**
3602. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/ComInterfaceInfo.cs`** -> AI Confidence: **99.24%**
3603. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/VirtualMethodPointerStubGenerator.cs`** -> AI Confidence: **99.24%**
3604. **`src/libraries/System.Runtime.InteropServices/gen/DownlevelLibraryImportGenerator/DownlevelLibraryImportGenerator.cs`** -> AI Confidence: **99.24%**
3605. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/BoundGenerators.cs`** -> AI Confidence: **99.24%**
3606. **`src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.Context/Conformance.dynamic.context.property.regproperty.regclass.cs`** -> AI Confidence: **99.24%**
3607. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/GCTests.cs`** -> AI Confidence: **99.24%**
3608. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/CESchedulerPairTests.cs`** -> AI Confidence: **99.24%**
3609. **`src/libraries/System.Security.AccessControl/src/System/Security/Principal/Win32.cs`** -> AI Confidence: **99.24%**
3610. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.Decode.cs`** -> AI Confidence: **99.24%**
3611. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.Encrypt.cs`** -> AI Confidence: **99.24%**
3612. **`src/libraries/System.Security.Cryptography.Pkcs/tests/SignedCms/SignerInfoTests.cs`** -> AI Confidence: **99.24%**
3613. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/DSA.cs`** -> AI Confidence: **99.24%**
3614. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/RSA.cs`** -> AI Confidence: **99.24%**
3615. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/AndroidCertificatePal.cs`** -> AI Confidence: **99.24%**
3616. **`src/libraries/System.Security.Cryptography/tests/X509Certificates/DynamicChainTests.cs`** -> AI Confidence: **99.24%**
3617. **`src/libraries/System.Security.Cryptography/tests/X509Certificates/X509FilesystemTests.Windows.cs`** -> AI Confidence: **99.24%**
3618. **`src/libraries/System.Text.Json/tests/Common/JsonSchemaExporterTests.TestTypes.cs`** -> AI Confidence: **99.24%**
3619. **`src/libraries/System.Text.Json/tests/Common/JsonSchemaExporterTests.cs`** -> AI Confidence: **99.24%**
3620. **`src/libraries/System.Text.Json/tests/System.Text.Json.SourceGeneration.Tests/Serialization/JsonSerializerWrapper.SourceGen.cs`** -> AI Confidence: **99.24%**
3621. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Serialization/JsonSerializerWrapper.Reflection.cs`** -> AI Confidence: **99.24%**
3622. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Utf8JsonWriterTests.cs`** -> AI Confidence: **99.24%**
3623. **`src/libraries/System.Text.RegularExpressions/gen/UpgradeToGeneratedRegexAnalyzer.cs`** -> AI Confidence: **99.24%**
3624. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/Regex.Tests.Common.cs`** -> AI Confidence: **99.24%**
3625. **`src/libraries/System.Threading.Tasks.Dataflow/src/Internal/SpscTargetCore.cs`** -> AI Confidence: **99.24%**
3626. **`src/libraries/System.Transactions.Local/tests/TransactionTracingEventListener.cs`** -> AI Confidence: **99.24%**
3627. **`src/mono/browser/debugger/BrowserDebugProxy/Common/FirefoxDebuggerConnection.cs`** -> AI Confidence: **99.24%**
3628. **`src/mono/browser/debugger/BrowserDebugProxy/DevToolsProxy.cs`** -> AI Confidence: **99.24%**
3629. **`src/mono/browser/debugger/BrowserDebugProxy/Firefox/FirefoxMonoProxy.cs`** -> AI Confidence: **99.24%**
3630. **`src/mono/browser/debugger/BrowserDebugProxy/MemberObjectsExplorer.cs`** -> AI Confidence: **99.24%**
3631. **`src/mono/browser/debugger/BrowserDebugProxy/ValueTypeClass.cs`** -> AI Confidence: **99.24%**
3632. **`src/mono/mono/tests/assembly-load-stress.cs`** -> AI Confidence: **99.24%**
3633. **`src/mono/mono/tests/remoting4.cs`** -> AI Confidence: **99.24%**
3634. **`src/mono/wasm/Wasm.Build.Tests/Blazor/CleanTests.cs`** -> AI Confidence: **99.24%**
3635. **`src/mono/wasm/Wasm.Build.Tests/Blazor/WorkloadRequiredTests.cs`** -> AI Confidence: **99.24%**
3636. **`src/mono/wasm/Wasm.Build.Tests/NativeRebuildTests/NativeRebuildTestsBase.cs`** -> AI Confidence: **99.24%**
3637. **`src/mono/wasm/Wasm.Build.Tests/Templates/WasmTemplateTestsBase.cs`** -> AI Confidence: **99.24%**
3638. **`src/mono/wasm/host/BrowserHost.cs`** -> AI Confidence: **99.24%**
3639. **`src/mono/wasm/host/CommonConfiguration.cs`** -> AI Confidence: **99.24%**
3640. **`src/mono/wasm/host/DevServer/DebugProxyLauncher.cs`** -> AI Confidence: **99.24%**
3641. **`src/mono/wasm/host/DevServer/WebAssemblyNetDebugProxyAppBuilderExtensions.cs`** -> AI Confidence: **99.24%**
3642. **`src/mono/wasm/host/WebServer.cs`** -> AI Confidence: **99.24%**
3643. **`src/tasks/MonoTargetsTasks/MarshalingPInvokeScanner/MarshalingPInvokeScanner.cs`** -> AI Confidence: **99.24%**
3644. **`src/tasks/WasmAppBuilder/coreclr/PInvokeTableGenerator.cs`** -> AI Confidence: **99.24%**
3645. **`src/tasks/WasmAppBuilder/mono/PInvokeTableGenerator.cs`** -> AI Confidence: **99.24%**
3646. **`src/tasks/WorkloadBuildTasks/InstallWorkloadFromArtifacts.cs`** -> AI Confidence: **99.24%**
3647. **`src/tests/GC/LargeMemory/memcheck.cs`** -> AI Confidence: **99.24%**
3648. **`src/tests/GC/Performance/Tests/LowLatencyTest.cs`** -> AI Confidence: **99.24%**
3649. **`src/tests/Interop/COM/Reflection/Reflection.cs`** -> AI Confidence: **99.24%**
3650. **`src/tests/JIT/Performance/CodeQuality/BenchmarksGame/fasta/fasta-1.cs`** -> AI Confidence: **99.24%**
3651. **`src/tests/JIT/Performance/CodeQuality/SIMD/RayTracer/RayTracerBench.cs`** -> AI Confidence: **99.24%**
3652. **`src/tests/JIT/Regression/JitBlue/Runtime_34587/Runtime_34587.cs`** -> AI Confidence: **99.24%**
3653. **`src/tests/Regressions/coreclr/GitHub_116953/test116953.cs`** -> AI Confidence: **99.24%**
3654. **`src/tests/Regressions/coreclr/GitHub_45929/test45929.cs`** -> AI Confidence: **99.24%**
3655. **`src/tests/nativeaot/SmokeTests/DynamicGenerics/B282745.cs`** -> AI Confidence: **99.24%**
3656. **`src/tests/nativeaot/SmokeTests/DynamicGenerics/GenericVirtualMethods.cs`** -> AI Confidence: **99.24%**
3657. **`src/tests/nativeaot/SmokeTests/DynamicGenerics/fieldreflection.cs`** -> AI Confidence: **99.24%**
3658. **`src/tests/profiler/eventpipe/eventpipe.cs`** -> AI Confidence: **99.24%**
3659. **`src/tests/tracing/eventcounter/regression-46938.cs`** -> AI Confidence: **99.24%**
3660. **`src/tests/tracing/eventpipe/common/IpcTraceTest.cs`** -> AI Confidence: **99.24%**
3661. **`src/tests/tracing/eventpipe/common/Microsoft.Diagnostics.NETCore.Client/DiagnosticsClient/DiagnosticsClient.cs`** -> AI Confidence: **99.24%**
3662. **`src/tests/tracing/eventpipe/processinfo3/processinfo3.cs`** -> AI Confidence: **99.24%**
3663. **`src/tools/StressLogAnalyzer/src/StressLogAnalyzer.cs`** -> AI Confidence: **99.24%**
3664. **`src/tools/illink/src/ILLink.CodeFix/BaseAttributeCodeFixProvider.cs`** -> AI Confidence: **99.24%**
3665. **`src/tools/illink/src/ILLink.CodeFix/RequiresUnsafeCodeFixProvider.cs`** -> AI Confidence: **99.24%**
3666. **`src/tools/illink/src/ILLink.RoslynAnalyzer/RequiresDynamicCodeAnalyzer.cs`** -> AI Confidence: **99.24%**
3667. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/TrimAnalysisVisitor.cs`** -> AI Confidence: **99.24%**
3668. **`src/tools/illink/src/linker/Linker/TypeNameResolver.WithDiagnostics.cs`** -> AI Confidence: **99.24%**
3669. **`src/tools/illink/test/ILLink.RoslynAnalyzer.Tests/TestChecker.cs`** -> AI Confidence: **99.24%**
3670. **`src/tools/illink/test/ILLink.RoslynAnalyzer.Tests/Verifiers/CSharpAnalyzerVerifier`1.cs`** -> AI Confidence: **99.24%**
3671. **`src/tools/illink/test/Mono.Linker.Tests/TestCasesRunner/TestCaseCollector.cs`** -> AI Confidence: **99.24%**
3672. **`src/mono/browser/runtime/rollup.config.js`** -> AI Confidence: **99.24%**
3673. **`src/mono/browser/runtime/cancelable-promise.ts`** -> AI Confidence: **99.24%**
3674. **`src/mono/browser/runtime/interp-pgo.ts`** -> AI Confidence: **99.24%**
3675. **`src/mono/browser/runtime/pthreads/worker-thread.ts`** -> AI Confidence: **99.24%**
3676. **`src/mono/browser/runtime/roots.ts`** -> AI Confidence: **99.24%**
3677. **`src/mono/browser/runtime/startup.ts`** -> AI Confidence: **99.24%**
3678. **`src/native/libs/Common/JavaScript/loader/run.ts`** -> AI Confidence: **99.24%**
3679. **`src/coreclr/scripts/antigen_run.py`** -> AI Confidence: **99.23%**
3680. **`src/coreclr/scripts/fuzzlyn_run.py`** -> AI Confidence: **99.23%**
3681. **`src/coreclr/scripts/pgocheck.py`** -> AI Confidence: **99.23%**
3682. **`src/native/external/brotli/setup.py`** -> AI Confidence: **99.23%**
3683. **`src/mono/mono/eglib/test/timer.c`** -> AI Confidence: **99.23%**
3684. **`src/mono/mono/metadata/w32event-unix.c`** -> AI Confidence: **99.23%**
3685. **`src/mono/mono/mini/interp/mintops.h`** -> AI Confidence: **99.23%**
3686. **`src/mono/mono/mini/llvm-intrinsics.h`** -> AI Confidence: **99.23%**
3687. **`src/mono/mono/utils/atomic.h`** -> AI Confidence: **99.23%**
3688. **`src/native/external/brotli/c/enc/bit_cost.h`** -> AI Confidence: **99.23%**
3689. **`src/native/external/brotli/c/enc/dictionary_hash.h`** -> AI Confidence: **99.23%**
3690. **`src/native/external/brotli/c/enc/literal_cost.h`** -> AI Confidence: **99.23%**
3691. **`src/native/external/brotli/c/enc/utf8_util.h`** -> AI Confidence: **99.23%**
3692. **`src/native/external/libunwind/src/aarch64/Gos-freebsd.c`** -> AI Confidence: **99.23%**
3693. **`src/native/external/libunwind/src/dwarf/Gparser.c`** -> AI Confidence: **99.23%**
3694. **`src/native/external/libunwind/src/ia64/unwind_decoder.h`** -> AI Confidence: **99.23%**
3695. **`src/native/external/libunwind/src/nto/unw_nto_destroy.c`** -> AI Confidence: **99.23%**
3696. **`src/native/external/libunwind/src/x86_64/Gget_save_loc.c`** -> AI Confidence: **99.23%**
3697. **`src/native/external/libunwind/src/x86_64/Gstash_frame.c`** -> AI Confidence: **99.23%**
3698. **`src/native/external/libunwind/tests/test-reg-state.c`** -> AI Confidence: **99.23%**
3699. **`src/native/external/zlib-ng/arch/arm/neon_intrins.h`** -> AI Confidence: **99.23%**
3700. **`src/native/external/zlib-ng/arch/power/power_features.c`** -> AI Confidence: **99.23%**
3701. **`src/native/external/zlib-ng/arch/x86/crc32_fold_pclmulqdq_tpl.h`** -> AI Confidence: **99.23%**
3702. **`src/native/external/zlib-ng/arch/x86/x86_intrins.h`** -> AI Confidence: **99.23%**
3703. **`src/native/external/zstd/lib/decompress/zstd_ddict.c`** -> AI Confidence: **99.23%**
3704. **`src/native/libs/System.Security.Cryptography.Native.Apple/pal_x509_macos.c`** -> AI Confidence: **99.23%**
3705. **`src/coreclr/dlls/mscorpe/ceefilegenwriter.cpp`** -> AI Confidence: **99.23%**
3706. **`src/coreclr/gc/allocation.cpp`** -> AI Confidence: **99.23%**
3707. **`src/coreclr/gc/background.cpp`** -> AI Confidence: **99.23%**
3708. **`src/coreclr/gc/card_table.cpp`** -> AI Confidence: **99.23%**
3709. **`src/coreclr/gc/collect.cpp`** -> AI Confidence: **99.23%**
3710. **`src/coreclr/gc/dac_gcheap_fields.h`** -> AI Confidence: **99.23%**
3711. **`src/coreclr/gc/dac_generation_fields.h`** -> AI Confidence: **99.23%**
3712. **`src/coreclr/gc/diagnostics.cpp`** -> AI Confidence: **99.23%**
3713. **`src/coreclr/gc/dynamic_heap_count.cpp`** -> AI Confidence: **99.23%**
3714. **`src/coreclr/gc/dynamic_tuning.cpp`** -> AI Confidence: **99.23%**
3715. **`src/coreclr/gc/gcenv.inl`** -> AI Confidence: **99.23%**
3716. **`src/coreclr/gc/handletableconstants.h`** -> AI Confidence: **99.23%**
3717. **`src/coreclr/gc/handletablecore.cpp`** -> AI Confidence: **99.23%**
3718. **`src/coreclr/gc/no_gc.cpp`** -> AI Confidence: **99.23%**
3719. **`src/coreclr/gc/plan_phase.cpp`** -> AI Confidence: **99.23%**
3720. **`src/coreclr/gc/region_allocator.cpp`** -> AI Confidence: **99.23%**
3721. **`src/coreclr/gc/regions_segments.cpp`** -> AI Confidence: **99.23%**
3722. **`src/coreclr/gc/relocate_compact.cpp`** -> AI Confidence: **99.23%**
3723. **`src/coreclr/gc/softwarewritewatch.cpp`** -> AI Confidence: **99.23%**
3724. **`src/coreclr/gc/sweep.cpp`** -> AI Confidence: **99.23%**
3725. **`src/coreclr/gc/vxsort/vxsort_targets_disable.h`** -> AI Confidence: **99.23%**
3726. **`src/coreclr/gc/vxsort/vxsort_targets_enable_avx2.h`** -> AI Confidence: **99.23%**
3727. **`src/coreclr/gc/vxsort/vxsort_targets_enable_avx512.h`** -> AI Confidence: **99.23%**
3728. **`src/coreclr/ilasm/asmman.cpp`** -> AI Confidence: **99.23%**
3729. **`src/coreclr/ildasm/resource.h`** -> AI Confidence: **99.23%**
3730. **`src/coreclr/inc/dlwrap.h`** -> AI Confidence: **99.23%**
3731. **`src/coreclr/inc/optsmallperfcritical.h`** -> AI Confidence: **99.23%**
3732. **`src/coreclr/interpreter/interpconfigvalues.h`** -> AI Confidence: **99.23%**
3733. **`src/coreclr/interpreter/intops.cpp`** -> AI Confidence: **99.23%**
3734. **`src/coreclr/jit/fgwasm.h`** -> AI Confidence: **99.23%**
3735. **`src/coreclr/jit/opcode.h`** -> AI Confidence: **99.23%**
3736. **`src/coreclr/jit/target.h`** -> AI Confidence: **99.23%**
3737. **`src/coreclr/jit/valuenum.cpp`** -> AI Confidence: **99.23%**
3738. **`src/coreclr/jit/valuenumfuncs.h`** -> AI Confidence: **99.23%**
3739. **`src/coreclr/md/debug_metadata.h`** -> AI Confidence: **99.23%**
3740. **`src/coreclr/md/enc/rwutil.cpp`** -> AI Confidence: **99.23%**
3741. **`src/coreclr/md/inc/mdlog.h`** -> AI Confidence: **99.23%**
3742. **`src/coreclr/md/inc/metamodel.h`** -> AI Confidence: **99.23%**
3743. **`src/coreclr/nativeaot/Runtime/GCMemoryHelpers.inl`** -> AI Confidence: **99.23%**
3744. **`src/coreclr/nativeaot/Runtime/eventtrace_etw.h`** -> AI Confidence: **99.23%**
3745. **`src/coreclr/nativeaot/Runtime/profheapwalkhelper.cpp`** -> AI Confidence: **99.23%**
3746. **`src/coreclr/pal/inc/rt/guiddef.h`** -> AI Confidence: **99.23%**
3747. **`src/coreclr/pal/src/safecrt/input.inl`** -> AI Confidence: **99.23%**
3748. **`src/coreclr/pal/src/safecrt/internal_securecrt.h`** -> AI Confidence: **99.23%**
3749. **`src/coreclr/pal/src/safecrt/tcscat_s.inl`** -> AI Confidence: **99.23%**
3750. **`src/coreclr/pal/src/safecrt/tcscpy_s.inl`** -> AI Confidence: **99.23%**
3751. **`src/coreclr/pal/src/safecrt/tcsncat_s.inl`** -> AI Confidence: **99.23%**
3752. **`src/coreclr/pal/src/safecrt/tcsncpy_s.inl`** -> AI Confidence: **99.23%**
3753. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjectsEx/test5/commonconsts.h`** -> AI Confidence: **99.23%**
3754. **`src/coreclr/runtime/MiscNativeHelpers.h`** -> AI Confidence: **99.23%**
3755. **`src/coreclr/tools/aot/jitinterface/dllexport.h`** -> AI Confidence: **99.23%**
3756. **`src/coreclr/utilcode/ex.cpp`** -> AI Confidence: **99.23%**
3757. **`src/coreclr/utilcode/loaderheap_shared.cpp`** -> AI Confidence: **99.23%**
3758. **`src/coreclr/utilcode/sstring.cpp`** -> AI Confidence: **99.23%**
3759. **`src/coreclr/vm/appdomainnative.cpp`** -> AI Confidence: **99.23%**
3760. **`src/coreclr/vm/classhash.cpp`** -> AI Confidence: **99.23%**
3761. **`src/coreclr/vm/eehash.cpp`** -> AI Confidence: **99.23%**
3762. **`src/coreclr/vm/gchelpers.inl`** -> AI Confidence: **99.23%**
3763. **`src/coreclr/vm/peimagelayout.cpp`** -> AI Confidence: **99.23%**
3764. **`src/coreclr/vm/perfmap.cpp`** -> AI Confidence: **99.23%**
3765. **`src/coreclr/vm/rtlfunctions.h`** -> AI Confidence: **99.23%**
3766. **`src/coreclr/vm/syncclean.cpp`** -> AI Confidence: **99.23%**
3767. **`src/mono/mono/metadata/object-offsets.h`** -> AI Confidence: **99.23%**
3768. **`src/mono/mono/sgen/sgen-protocol-def.h`** -> AI Confidence: **99.23%**
3769. **`src/mono/mono/sgen/sgen-scan-object.h`** -> AI Confidence: **99.23%**
3770. **`src/mono/mono/utils/options-def.h`** -> AI Confidence: **99.23%**
3771. **`src/native/corehost/bundle/runner.cpp`** -> AI Confidence: **99.23%**
3772. **`src/native/corehost/fxr_resolver.cpp`** -> AI Confidence: **99.23%**
3773. **`src/native/corehost/json_parser.cpp`** -> AI Confidence: **99.23%**
3774. **`src/native/eventpipe/ds-getter-setter.h`** -> AI Confidence: **99.23%**
3775. **`src/native/eventpipe/ds-rt-config.h`** -> AI Confidence: **99.23%**
3776. **`src/native/external/brotli/c/common/version.h`** -> AI Confidence: **99.23%**
3777. **`src/native/external/brotli/c/enc/cluster_inc.h`** -> AI Confidence: **99.23%**
3778. **`src/native/external/llvm-libunwind/src/libunwind.cpp`** -> AI Confidence: **99.23%**
3779. **`src/native/external/llvm-libunwind/src/shadow_stack_unwind.h`** -> AI Confidence: **99.23%**
3780. **`src/native/external/zlib-ng/crc32_braid_p.h`** -> AI Confidence: **99.23%**
3781. **`src/native/external/zlib-ng/match_tpl.h`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/libraries/Microsoft.Bcl.Cryptography/src/CompatibilitySuppressions.xml` -> **100.0%** Exposure
- `src/libraries/System.Configuration.ConfigurationManager/src/CompatibilitySuppressions.xml` -> **100.0%** Exposure
- `src/libraries/System.Numerics.Tensors/src/CompatibilitySuppressions.xml` -> **100.0%** Exposure
- `src/libraries/System.Reflection.Context/src/ILLink/ILLink.Suppressions.xml` -> **100.0%** Exposure
- `src/libraries/System.Reflection.MetadataLoadContext/src/ILLink/ILLink.Suppressions.xml` -> **100.0%** Exposure
### Exploit Generation Surface
- `.github/skills/ci-pipeline-monitor/scripts/extract_failed_tests.py` -> **100.0%** Exposure
- `.github/skills/ci-pipeline-monitor/scripts/fetch_helix_logs.py` -> **100.0%** Exposure
- `.github/skills/ci-pipeline-monitor/scripts/generate_report.py` -> **100.0%** Exposure
- `.github/skills/ci-pipeline-monitor/scripts/setup_and_fetch_builds.py` -> **100.0%** Exposure
- `.github/skills/ci-pipeline-monitor/scripts/validate_results.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `eng/testing/WasmBatchRunner.sh` -> **100.0%** Exposure
- `src/libraries/System.Security.Cryptography/tests/osslplugins/install-engine.sh` -> **100.0%** Exposure
- `src/tests/Common/scripts/bringup_runtest.sh` -> **100.0%** Exposure
- `.github/skills/ci-pipeline-monitor/scripts/extract_failed_tests.py` -> **100.0%** Exposure
- `.github/skills/ci-pipeline-monitor/scripts/fetch_helix_logs.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `src/mono/browser/runtime/driver.c` -> **100.0%** Exposure
- `src/mono/browser/runtime/runtime.c` -> **100.0%** Exposure
- `src/libraries/Common/tests/System/Net/EnterpriseTests/setup/apacheweb/mod_auth_ntlm_winbind/mod_auth_ntlm_winbind.c` -> **10.0%** Exposure
- `src/mono/mono/component/debugger-agent.c` -> **10.0%** Exposure
- `src/mono/mono/component/debugger-engine.c` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/DSA/DSAKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/EC/ECKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/RSA/RSAKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/System.Security.Cryptography/tests/ECPemExportTests.cs` -> **99.9997%** Exposure
- `src/libraries/System.Security.Cryptography/tests/X509Certificates/X509Certificate2PemTests.cs` -> **99.9977%** Exposure
### Algorithmic DoS Exposure
- `src/native/external/libunwind/.github/workflows/CI-unix.yml` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.sh` -> **100.0%** Exposure
- `eng/common/cross/tizen-fetch.sh` -> **100.0%** Exposure
- `eng/common/init-tools-native.sh` -> **100.0%** Exposure
- `eng/common/native/init-compiler.sh` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `139` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `122719` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncContext.Unix.cs` (CSHARP) -> Cumulative Risk: **1088.84**
- **Archetype:** `file_cluster_8` (Distance: 13.45 IQR)
- **Magnitude:** 3807.04 | **LOC:** 2332 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `StartAsyncOperation` (Impact: 2345.6), `ProcessCancellation` (Impact: 72.9), `TryComplete` (Impact: 72.3)

### 2. `src/libraries/System.Private.CoreLib/src/Microsoft/Win32/SafeHandles/SafeFileHandle.ThreadPoolValueTaskSource.cs` (CSHARP) -> Cumulative Risk: **1040.55**
- **Archetype:** `file_cluster_4` (Distance: 12.418 IQR)
- **Magnitude:** 384.9 | **LOC:** 236 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ExecuteInternal` (Impact: 185.6), `GetResult` (Impact: 40.8), `IThreadPoolWorkItem.Execute` (Impact: 16.1)

### 3. `src/tasks/WasmAppBuilder/WasmAppBuilderBaseTask.cs` (CSHARP) -> Cumulative Risk: **999.78**
- **Archetype:** `file_cluster_0` (Distance: 13.277 IQR)
- **Magnitude:** 288.06 | **LOC:** 191 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `UpdateRuntimeConfigJson` (Impact: 137.9), `ProcessSatelliteAssemblies` (Impact: 26.8), `FileCopyChecked` (Impact: 25.1)

### 4. `src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/marshaled-types.ts` (TYPESCRIPT) -> Cumulative Risk: **995.4**
- **Archetype:** `file_cluster_13` (Distance: 13.98 IQR)
- **Magnitude:** 50.93 | **LOC:** 265 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `cancel` (Impact: 51.0), `set` (Impact: 26.3), `slice` (Impact: 26.3)

### 5. `src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/Thread_1.cs` (CSHARP) -> Cumulative Risk: **994.85**
- **Archetype:** `file_cluster_4` (Distance: 11.819 IQR)
- **Magnitude:** 281.62 | **LOC:** 273 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `IThread.GetThreadLocalStaticBase` (Impact: 53.9), `IThread.GetWatsonBuckets` (Impact: 28.9), `IThread.GetThreadData` (Impact: 26.0)

### 6. `src/coreclr/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncHelpers.CoreCLR.cs` (CSHARP) -> Cumulative Risk: **993.57**
- **Archetype:** `file_cluster_8` (Distance: 11.578 IQR)
- **Magnitude:** 504.62 | **LOC:** 1245 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `HandleSuspended` (Impact: 37.1), `RestoreContextsOnSuspension` (Impact: 36.8), `UnwindRuntimeAsyncMethodUnhandledExcepti` (Impact: 26.2)

### 7. `src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpRequestState.cs` (CSHARP) -> Cumulative Risk: **987.21**
- **Archetype:** `file_cluster_4` (Distance: 13.072 IQR)
- **Magnitude:** 487.32 | **LOC:** 236 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Dispose` (Impact: 149.5), `FromIntPtr` (Impact: 29.6), `ClearSendRequestState` (Impact: 21.2)

### 8. `src/mono/wasm/Wasm.Build.Tests/Common/ToolCommand.cs` (CSHARP) -> Cumulative Risk: **985.45**
- **Archetype:** `file_cluster_8` (Distance: 10.957 IQR)
- **Magnitude:** 284.18 | **LOC:** 239 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Dispose` (Impact: 45.3), `ExecuteAsyncInternal` (Impact: 39.3), `WithEnvironmentVariables` (Impact: 21.3)

### 9. `src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/AggregatorStore.cs` (CSHARP) -> Cumulative Risk: **978.42**
- **Archetype:** `file_cluster_4` (Distance: 12.919 IQR)
- **Magnitude:** 1292.36 | **LOC:** 517 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Collect` (Impact: 202.8), `Collect` (Impact: 173.5), `GetAggregator` (Impact: 114.0)

### 10. `src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/DsesFilterAndTransform.cs` (CSHARP) -> Cumulative Risk: **977.83**
- **Archetype:** `file_cluster_13` (Distance: 12.693 IQR)
- **Magnitude:** 864.0 | **LOC:** 1055 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `CreateActivitySourceTransform` (Impact: 202.4), `Fetch` (Impact: 147.7), `TransformSpec` (Impact: 89.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/tests/JIT/Directed/cmov/Bool_And_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.833 IQR)
- **Top Global Matches:** file_cluster_8: 12.833, file_cluster_7: 13.343, file_cluster_1: 13.355
- **Magnitude:** 49380.16 | **LOC:** 20789 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (63.1895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 185.2 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3227`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Bool_Or_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.833 IQR)
- **Top Global Matches:** file_cluster_8: 12.833, file_cluster_7: 13.343, file_cluster_1: 13.355
- **Magnitude:** 49380.16 | **LOC:** 20788 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (63.1895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 185.2 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3227`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Bool_Xor_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.401 IQR)
- **Top Global Matches:** file_cluster_8: 13.401, file_cluster_7: 13.89, file_cluster_1: 13.901
- **Magnitude:** 49380.16 | **LOC:** 20788 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (63.1895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 185.2 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 185.2 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3227`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Regression/VS-ia64-JIT/V1.2-M01/b10827/MT_DEATH.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.917 IQR)
- **Top Global Matches:** file_cluster_8: 12.917, file_cluster_7: 13.423, file_cluster_1: 13.436
- **Magnitude:** 43336.66 | **LOC:** 20866 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (63.1652%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 160.7 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 160.7 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 160.7 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 160.7 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 160.7 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27685`, `structural_boundaries: 473`, `args: 466`, `func_start: 930`, `class_start: 1`
* *Risk/State:* `state_mutation: 3230`
* *Architecture:* `api: 4`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` TestLibrary, Xunit, System, System.Threading
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/nullabletypes/isinstvaluetype.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.579 IQR)
- **Top Global Matches:** file_cluster_8: 16.579, file_cluster_16: 16.804, file_cluster_7: 17.087
- **Magnitude:** 33489.16 | **LOC:** 19758 | **CtrlFlow:** 99.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.2124%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestCase0001` (Impact: 972.6 | O(N^3))
  * `TestCase0002` (Impact: 972.6 | O(N^3))
  * `TestCase0003` (Impact: 972.6 | O(N^3))
  * `TestCase0004` (Impact: 972.6 | O(N^3))
  * `TestCase0005` (Impact: 972.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7144`, `structural_boundaries: 7`, `args: 36`, `func_start: 19249`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 19179`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Runtime.InteropServices, TestLibrary, Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/nullabletypes/isinst2.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.531 IQR)
- **Top Global Matches:** file_cluster_8: 16.531, file_cluster_16: 16.752, file_cluster_7: 17.034
- **Magnitude:** 29637.58 | **LOC:** 17298 | **CtrlFlow:** 99.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.5283%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestCase0019` (Impact: 1625.8 | O(N^3))
  * `TestCase0020` (Impact: 1625.8 | O(N^3))
  * `TestCase0021` (Impact: 1625.8 | O(N^3))
  * `TestCase0022` (Impact: 1625.8 | O(N^3))
  * `TestCase0023` (Impact: 1625.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6340`, `structural_boundaries: 6`, `args: 20`, `func_start: 16961`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 16922`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Runtime.InteropServices, Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/nullabletypes/isinst.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.466 IQR)
- **Top Global Matches:** file_cluster_8: 16.466, file_cluster_16: 16.681, file_cluster_7: 16.971
- **Magnitude:** 26350.72 | **LOC:** 15380 | **CtrlFlow:** 99.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.5256%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestCase0001` (Impact: 1626.4 | O(N^3))
  * `TestCase0002` (Impact: 1626.4 | O(N^3))
  * `TestCase0003` (Impact: 1626.4 | O(N^3))
  * `TestCase0006` (Impact: 1626.4 | O(N^3))
  * `TestCase0004` (Impact: 1626.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5636`, `structural_boundaries: 6`, `args: 18`, `func_start: 15077`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 15042`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Runtime.InteropServices, Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/emitarm64.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.835 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.516 IQR)
- **Top Global Matches:** file_cluster_8: 15.835, file_cluster_11: 16.062, file_cluster_13: 16.11
- **Magnitude:** 26192.26 | **LOC:** 18013 | **CtrlFlow:** 94.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 550
- **Risk Profile:** Cognitive Load (90.7304%), Tech Debt (26.314%)
**Top Internal Functions/Classes:**
  * `emitter::emitIns_R_R_I` (Impact: 4658.4 | O(N^6) | DB: 253)
  * `emitter::emitInsTernary` (Impact: 4160.4 | O(N^6) | DB: 330)
  * `emitter::emitDispInsHelp` (Impact: 2714.0 | O(N^6) | DB: 146)
  * `emitter::emitIns_R_S` (Impact: 2654.3 | O(N^6) | DB: 550)
  * `emitter::emitInsCode` (Impact: 892.5 | O(N^6) | DB: 201)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3734`, `structural_boundaries: 236`, `args: 160`, `func_start: 123`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6604`, `dead_code: 3`, `planned_debt: 10`, `orphaned_logic: 90`
* *Architecture:* `import: 21`
* *Defense:* `safety: 958`, `doc: 83`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` codegen.h, instrs.h, emitjmps.h, instrsarm64sve.h, jitpch.h, instr.h, emit.h, register.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/nullabletypes/isinstboxed.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.42 IQR)
- **Top Global Matches:** file_cluster_8: 16.42, file_cluster_16: 16.637, file_cluster_7: 16.927
- **Magnitude:** 24709.92 | **LOC:** 14496 | **CtrlFlow:** 99.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.4039%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestCase0001` (Impact: 1626.6 | O(N^3))
  * `TestCase0002` (Impact: 1626.6 | O(N^3))
  * `TestCase0006` (Impact: 1626.6 | O(N^3))
  * `TestCase0003` (Impact: 1626.5 | O(N^3))
  * `TestCase0004` (Impact: 1626.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5284`, `structural_boundaries: 6`, `args: 17`, `func_start: 14135`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 14102`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Runtime.InteropServices, Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/emitarm64sve.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.789 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.86 IQR)
- **Top Global Matches:** file_cluster_8: 15.789, file_cluster_11: 16.063, file_cluster_13: 16.119
- **Magnitude:** 24630.44 | **LOC:** 20043 | **CtrlFlow:** 98.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 577
- **Risk Profile:** Cognitive Load (96.2822%), Tech Debt (14.8263%)
**Top Internal Functions/Classes:**
  * `emitter::emitInsSve_R_R_R` (Impact: 3783.7 | O(N^6) | DB: 577)
    * *Intent:* /*****************************************************************************
  * `emitter::emitInsPairSanityCheck` (Impact: 3100.3 | O(N^5) | DB: 2)
  * `emitter::emitDispInsSveHelp` (Impact: 2663.0 | O(N^6) | DB: 52)
  * `emitter::getInsSveExecutionCharacteristi` (Impact: 2421.3 | O(N^5) | DB: 381)
  * `emitter::emitInsSveSanityCheck` (Impact: 1628.2 | O(N^5) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4594`, `structural_boundaries: 73`, `args: 20`, `func_start: 42`
* *Risk/State:* `state_mutation: 5941`, `planned_debt: 10`, `duplicate_logic: 2`, `orphaned_logic: 40`
* *Architecture:* `import: 16`
* *Defense:* `safety: 1297`, `doc: 27`, `immutability_locks: 159`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` instr.h, codegen.h, instrsarm64sve.h, jitpch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/jit64/regress/vsw/524070/test2.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.541 IQR)
- **Top Global Matches:** file_cluster_8: 13.541, file_cluster_7: 13.988, file_cluster_13: 14.175
- **Magnitude:** 21227.58 | **LOC:** 10529 | **CtrlFlow:** 99.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 170
- **Risk Profile:** Cognitive Load (96.8877%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `func` (Impact: 16780.7 | O(2^N) | DB: 170)
  * `TestEntryPoint` (Impact: 15.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8765`, `structural_boundaries: 5`, `args: 2`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 4218`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 30`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libraries/Microsoft.VisualBasic.Core/tests/OperatorsTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.163 IQR)
- **Top Global Matches:** file_cluster_8: 10.163, file_cluster_0: 10.706, file_cluster_7: 10.833
- **Magnitude:** 19516.04 | **LOC:** 5479 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.8462%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `OrObject_TestData` (Impact: 2249.5 | O(N^3))
  * `AndObject_TestData` (Impact: 2213.3 | O(N^3))
  * `XorObject_TestData` (Impact: 2213.3 | O(N^3))
  * `ModObject_TestData` (Impact: 1774.2 | O(N^3))
  * `ConcatenateObject_TestData` (Impact: 1182.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4119`, `structural_boundaries: 8376`, `args: 211`, `func_start: 213`, `class_start: 33`
* *Risk/State:* `fragile_debt: 1`, `duplicate_logic: 24`, `orphaned_logic: 67`
* *Architecture:* `api: 195`, `import: 8`
* *Defense:* `safety: 52`, `test: 142`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Reflection, System.Linq, Microsoft.VisualBasic.CompilerServices, System, Xunit, System.Runtime.CompilerServices, System.Globalization, System.Collections.Generic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/nativeaot/Runtime/StackFrameIterator.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.439 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.428 IQR)
- **Top Global Matches:** file_cluster_8: 14.439, file_cluster_13: 14.568, file_cluster_11: 14.682
- **Magnitude:** 18258.61 | **LOC:** 2433 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (65.5301%), Tech Debt (26.2048%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 61`, `args: 184`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1006`, `dead_code: 3`, `planned_debt: 13`, `fragile_debt: 5`
* *Architecture:* `api: 8`, `import: 24`
* *Defense:* `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` threadstore.inl, rhassert.h, Pal.h, slist.h, PalLimitedContext.h, gcenv.h, event.h, RuntimeInstance.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_Xor_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.135 IQR)
- **Top Global Matches:** file_cluster_8: 13.135, file_cluster_1: 13.142, file_cluster_7: 13.591
- **Magnitude:** 18244.52 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (38.1825%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1679`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_And_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.546 IQR)
- **Top Global Matches:** file_cluster_8: 12.546, file_cluster_1: 12.554, file_cluster_7: 13.024
- **Magnitude:** 18184.52 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (37.6212%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1619`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_Or_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.546 IQR)
- **Top Global Matches:** file_cluster_8: 12.546, file_cluster_1: 12.554, file_cluster_7: 13.024
- **Magnitude:** 18184.52 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (37.6212%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1619`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_Xor_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.06 IQR)
- **Top Global Matches:** file_cluster_8: 13.06, file_cluster_1: 13.068, file_cluster_7: 13.521
- **Magnitude:** 18084.52 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.6945%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1519`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_And_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.489 IQR)
- **Top Global Matches:** file_cluster_8: 12.489, file_cluster_1: 12.496, file_cluster_7: 12.97
- **Magnitude:** 18066.52 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.5289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1501`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_Or_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.489 IQR)
- **Top Global Matches:** file_cluster_8: 12.489, file_cluster_1: 12.496, file_cluster_7: 12.97
- **Magnitude:** 18066.52 | **LOC:** 22170 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.5289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1501`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_Xor_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.052 IQR)
- **Top Global Matches:** file_cluster_8: 13.052, file_cluster_1: 13.059, file_cluster_7: 13.513
- **Magnitude:** 18066.52 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.5289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1501`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_And_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.467 IQR)
- **Top Global Matches:** file_cluster_8: 12.467, file_cluster_1: 12.475, file_cluster_7: 12.95
- **Magnitude:** 18024.52 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.1439%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1459`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Float_Or_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.467 IQR)
- **Top Global Matches:** file_cluster_8: 12.467, file_cluster_1: 12.475, file_cluster_7: 12.95
- **Magnitude:** 18024.52 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.1439%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_1` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_2` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_3` (Impact: 65.3 | O(N^2) | DB: 3)
  * `Sub_Funclet_4` (Impact: 65.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1459`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libraries/System.Runtime/ref/System.Runtime.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.278 IQR)
- **Top Global Matches:** file_cluster_0: 15.278, file_cluster_16: 15.405, file_cluster_11: 15.482
- **Magnitude:** 16628.18 | **LOC:** 17405 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (75.3522%), Tech Debt (59.5146%)
**Top Internal Functions/Classes:**
  * `AppendPrivatePath` (Impact: 43.4 | O(2^N))
  * `SetCachePath` (Impact: 43.4 | O(2^N))
  * `SetDynamicBase` (Impact: 43.4 | O(2^N))
  * `SetShadowCopyPath` (Impact: 43.4 | O(2^N))
  * `CreateInstanceAndUnwrap` (Impact: 40.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4127`, `structural_boundaries: 1438`, `args: 5545`, `func_start: 8371`, `class_start: 808`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3972`, `duplicate_logic: 184`, `orphaned_logic: 41`
* *Architecture:* `io: 1`, `api: 10227`, `concurrency: 746`
* *Defense:* `safety: 247`, `sync_locks: 4`, `immutability_locks: 421`, `cleanup: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.781
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 137):` (Excluded from Brief to save tokens)

### `src/coreclr/ildasm/dasm.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.397 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.705 IQR)
- **Top Global Matches:** file_cluster_8: 15.397, file_cluster_13: 15.666, file_cluster_11: 15.699
- **Magnitude:** 16019.36 | **LOC:** 7636 | **CtrlFlow:** 82.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 474
- **Risk Profile:** Cognitive Load (93.4225%), Tech Debt (15.761%)
**Top Internal Functions/Classes:**
  * `UnderlyingTypeOfEnumTypeDef` (Impact: 3100.1 | O(N^6) | DB: 474)
  * `DumpClass` (Impact: 1346.2 | O(2^N) | DB: 130)
  * `DumpMethod` (Impact: 817.1 | O(N^6) | DB: 184)
  * `DumpEvent` (Impact: 523.8 | O(N^6) | DB: 54)
  * `DumpProp` (Impact: 513.0 | O(N^6) | DB: 57)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1491`, `structural_boundaries: 313`, `args: 911`, `func_start: 74`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 18`, `state_mutation: 5616`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 23`
* *Architecture:* `io: 3`, `import: 20`
* *Defense:* `safety: 2`, `test: 1`, `sync_locks: 1`, `immutability_locks: 66`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` corsym.h, metamodelpub.h, dynamicarray.h, readytorun.h, mdinfo.h, clrversion.h, ceeload.h, resource.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mono/mono/mini/interp/transform.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.244 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.184 IQR)
- **Top Global Matches:** file_cluster_8: 15.244, file_cluster_13: 15.437, file_cluster_11: 15.455
- **Magnitude:** 16002.42 | **LOC:** 10168 | **CtrlFlow:** 92.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 384
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (16.8108%)
**Top Internal Functions/Classes:**
  * `push_type_explicit` (Impact: 4114.3 | O(2^N) | DB: 351)
  * `generate_code` (Impact: 3842.8 | O(N^6) | DB: 384)
  * `emit_compacted_instruction` (Impact: 112.9 | O(N^1) | DB: 168)
  * `generate` (Impact: 94.7 | O(N^1) | DB: 104)
  * `interp_mark_ref_slots_for_vt` (Impact: 86.7 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2899`, `structural_boundaries: 246`, `args: 17`, `func_start: 86`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 5673`, `dead_code: 6`, `planned_debt: 8`, `fragile_debt: 21`, `orphaned_logic: 8`
* *Architecture:* `io: 4`, `api: 1304`, `import: 28`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` interp-pgo.h, transform-simd.c, interp.h, appdomain.h, mono-basic-block.h, interp-internals.h, class-internals.h, abi-details.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/libraries/System.Linq.Queryable/tests/ConcatTests.cs` (CSHARP) | Magnitude: 48.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, func_start: 10, test: 8, args: 7
- `src/libraries/System.Net.Mail/tests/Functional/MailMessageTest.cs` (CSHARP) | Magnitude: 152.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 177, func_start: 59, test: 52, sec_high_risk_execution: 52
- `src/libraries/System.Runtime.InteropServices/tests/System.Runtime.InteropServices.UnitTests/System/Runtime/InteropServices/Marshal/PInvokeErrorMessageTests.cs` (CSHARP) | Magnitude: 79.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 29, func_start: 13, test: 11
- `src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Serialization/PropertyNameTests.cs` (CSHARP) | Magnitude: 125.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 35, concurrency: 28, func_start: 24
- `src/tools/illink/test/Mono.Linker.Tests.Cases/Inheritance.Interfaces/InterfaceVariants.cs` (CSHARP) | Magnitude: 0.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 230, func_start: 67, decorators: 62, api: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/tests/JIT/Regression/JitBlue/Runtime_60957/Runtime_60957.cs` (CSHARP) | Magnitude: 140.24 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 116, doc: 44, func_start: 29, debug_prints: 19
- `src/libraries/System.IO.Compression/src/System/IO/Compression/DeflateManaged/InputBuffer.cs` (CSHARP) | Magnitude: 203.3 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 126, doc: 38, func_start: 26, state_mutation: 17
- `src/tools/ilasm/src/ILAssembler/StringHelpers.cs` (CSHARP) | Magnitude: 0.41 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, branch: 45, func_start: 22, events: 16
- `src/mono/mono/mini/test.cs` (CSHARP) | Magnitude: 772.76 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 396, indent_tabs: 307, branch: 140, events: 127
- `src/tests/JIT/Regression/JitBlue/Runtime_93342/Runtime_93342.cs` (CSHARP) | Magnitude: 184.96 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, events: 38, listeners: 38, branch: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/libraries/System.Runtime.Loader/tests/ApplyUpdateUtil.cs` (CSHARP) | Magnitude: 222.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 36, structural_boundaries: 27, func_start: 25
- `eng/common/generate-sbom-prep.sh` (SHELL) | Magnitude: 43.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 24, structural_boundaries: 18, branch: 12, safety_bypasses: 9
- `src/libraries/System.Composition.Hosting/tests/System/Composition/Hosting/Core/ExportDescriptorPromiseTests.cs` (CSHARP) | Magnitude: 159.06 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 206, func_start: 94, structural_boundaries: 77, test: 75
- `src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/EventSource.cs` (CSHARP) | Magnitude: 2856.06 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 973, branch: 295, state_mutation: 263, doc: 157
- `src/libraries/System.Resources.Extensions/src/System/Resources/Extensions/BinaryFormat/SerializationEvents.cs` (CSHARP) | Magnitude: 153.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 74, branch: 29, generics: 20, func_start: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `.devcontainer/scripts/postCreateCommand.sh` (SHELL) | Magnitude: 0.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, reflection_metaprogramming: 3, branch: 2, indent_spaces: 2
- `src/libraries/System.Linq.Expressions/src/System/Dynamic/Utils/CachedReflectionInfo.cs` (CSHARP) | Magnitude: 34.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, branch: 34, safety: 33, reflection_metaprogramming: 33
- `src/native/eventpipe/ep-rt-config.h` (CPP) | Magnitude: 46.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 41, state_mutation: 30, reflection_metaprogramming: 21, args: 12
- `src/mono/mono/arch/s390x/s390x-codegen.h` (CPP) | Magnitude: 608.48 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 682, reflection_metaprogramming: 681, indent_tabs: 651, state_mutation: 562
- `src/mono/mono/sgen/sgen-conf.h` (CPP) | Magnitude: 20.32 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 55, reflection_metaprogramming: 36, branch: 10, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/libraries/System.Collections.Immutable/src/System/Collections/Frozen/ItemsFrozenSet.cs` (CSHARP) | Magnitude: 27.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, encapsulation: 12, structural_boundaries: 9, generics: 5
- `src/mono/mono/utils/mono-context.c` (C) | Magnitude: 400.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 437, state_mutation: 335, indent_tabs: 290, macros: 70
- `src/native/libs/System.Security.Cryptography.Native.Apple/pal_symmetric.c` (C) | Magnitude: 145.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 27, api: 26, branch: 24
- `src/coreclr/tools/Common/Compiler/ObjectWriter/ElfObjectWriter.cs` (CSHARP) | Magnitude: 1.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 661, state_mutation: 258, func_start: 135, structural_boundaries: 113
- `src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/VTableSliceNode.cs` (CSHARP) | Magnitude: 0.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, sec_high_risk_execution: 15, branch: 13, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/Regex.Match.cs` (CSHARP) | Magnitude: 139.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 531, indent_spaces: 67, func_start: 37, sec_high_risk_execution: 24
- `eng/common/pipeline-logging-functions.ps1` (POWERSHELL) | Magnitude: 43.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 26, indent_spaces: 20, sec_high_risk_execution: 10, closures: 6
- `src/libraries/System.Data.Common/src/System/Data/DataRowCollection.cs` (CSHARP) | Magnitude: 263.42 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 127, func_start: 44, doc: 35, branch: 29
- `src/libraries/System.Private.CoreLib/src/System/Int32.cs` (CSHARP) | Magnitude: 1718.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 930, state_mutation: 392, branch: 245, structural_boundaries: 229
- `src/libraries/System.Private.CoreLib/src/System/Int64.cs` (CSHARP) | Magnitude: 1685.3 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 933, state_mutation: 395, branch: 246, structural_boundaries: 230

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/libraries/System.Collections.Immutable/src/System/Collections/Immutable/ImmutableList_1.Builder.cs` (CSHARP) | Magnitude: 703.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 699, indent_spaces: 366, func_start: 115, state_mutation: 76
- `src/libraries/System.Collections.Immutable/tests/EverythingEqual.cs` (CSHARP) | Magnitude: 19.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 8, func_start: 5, generics: 5
- `src/libraries/System.Collections.Immutable/tests/ImmutableSetTest.cs` (CSHARP) | Magnitude: 74.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 94, indent_spaces: 88, func_start: 36, test: 24
- `src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/INotifyComposablePartCatalogChanged.cs` (CSHARP) | Magnitude: 15.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, doc: 3, branch: 2
- `src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Metadata/PropertyRef.cs` (CSHARP) | Magnitude: 128.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, bitwise_ops: 22, structural_boundaries: 19, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/mono/browser/runtime/queue.ts` (TYPESCRIPT) | Magnitude: 9.89 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 55, indent_spaces: 34, args: 11, structural_boundaries: 8
- `eng/common/vmr-sync.sh` (SHELL) | Magnitude: 300.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 89, indent_spaces: 83, branch: 74, structural_boundaries: 38
- `src/coreclr/vm/ebr.h` (CPP) | Magnitude: 112.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 94, indent_spaces: 43, structural_boundaries: 13, args: 10
- `src/libraries/System.Linq/src/System/Linq/OfType.SpeedOpt.cs` (CSHARP) | Magnitude: 532.68 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 144, branch: 41, state_mutation: 39, structural_boundaries: 24
- `src/libraries/Microsoft.Extensions.Configuration.Binder/gen/ConfigurationBindingGenerator.Parser.cs` (CSHARP) | Magnitude: 1911.04 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 544, state_mutation: 215, branch: 187, structural_boundaries: 85

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/libraries/System.ObjectModel/tests/ReadOnlyObservableCollection/ReadOnlyObservableCollection_EventsTests.cs` (CSHARP) | Magnitude: 607.76 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 417, func_start: 91, state_mutation: 86, doc: 84
- `src/libraries/System.ObjectModel/tests/ObservableCollection/ObservableCollection_MethodsTest.cs` (CSHARP) | Magnitude: 825.04 | Delta: **0.217 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 545, func_start: 146, state_mutation: 114, doc: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/libraries/System.Linq.AsyncEnumerable/src/System/Linq/ToArrayAsync.cs` (CSHARP) | Magnitude: 49.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 13, concurrency: 12, func_start: 8
- `src/libraries/System.Private.Xml/tests/Xslt/XslTransformApi/CXsltArgumentListMultith.cs` (CSHARP) | Magnitude: 266.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 206, doc: 168, func_start: 72, state_mutation: 52
- `src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Multiplexing.cs` (CSHARP) | Magnitude: 496.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 254, doc: 128, state_mutation: 89, branch: 57
- `src/mono/mono/tests/appdomain-thread-abort.cs` (CSHARP) | Magnitude: 213.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 190, func_start: 55, structural_boundaries: 43, branch: 37
- `src/tests/JIT/Regression/CLR-x86-JIT/V1.2-M01/b08046cs/SyncGCHole.cs` (CSHARP) | Magnitude: 148.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, branch: 13, func_start: 12, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/coreclr/tools/Common/Compiler/DependencyAnalysis/AssemblyStubNode.cs` (CSHARP) | Magnitude: 0.09 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 70, func_start: 37, structural_boundaries: 17, state_mutation: 16
- `src/libraries/System.Management/src/System/Management/ManagementEventWatcher.cs` (CSHARP) | Magnitude: 418.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 301, doc: 147, state_mutation: 93, branch: 47
- `src/libraries/Microsoft.Win32.SystemEvents/src/Microsoft/Win32/UserPreferenceCategories.cs` (CSHARP) | Magnitude: 30.4 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 72, indent_spaces: 17, state_mutation: 14, sec_high_risk_execution: 7
- `src/coreclr/vm/amd64/virtualcallstubcpu.hpp` (CPP) | Magnitude: 528.84 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 392, state_mutation: 282, structural_boundaries: 140, args: 89
- `src/libraries/System.Text.Encoding.CodePages/src/System/Text/EncoderFallbackBufferHelper.cs` (CSHARP) | Magnitude: 70.18 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 32, func_start: 8, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/tests/Interop/PInvoke/Array/MarshalArray.h` (CPP) | Magnitude: 349.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 235, indent_spaces: 211, state_mutation: 155, structural_boundaries: 45
- `src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/RefreshEventArgs.cs` (CSHARP) | Magnitude: 34.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 17, indent_spaces: 14, state_mutation: 9, branch: 5
- `src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/ECDsa.cs` (CSHARP) | Magnitude: 555.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 450, indent_spaces: 401, func_start: 130, state_mutation: 62
- `src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/PortablePdb/PortablePdbVersions.cs` (CSHARP) | Magnitude: 19.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 18, indent_spaces: 14, api: 12, encapsulation: 12
- `src/installer/managed/Microsoft.NET.HostModel/MachO/BinaryFormat/Blobs/IBlob.cs` (CSHARP) | Magnitude: 18.78 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, indent_spaces: 3, structural_boundaries: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/native/external/libunwind/src/hppa/Gglobal.c` (C) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, api: 6, pointers: 5, state_mutation: 3
- `src/coreclr/jit/alloc.h` (CPP) | Magnitude: 41.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 24, macros: 16, globals: 14
- `src/coreclr/nativeaot/Runtime/eventtrace_gcheap.cpp` (CPP) | Magnitude: 136.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 137, state_mutation: 69, pointers: 40, import: 15
- `src/coreclr/nativeaot/System.Private.CoreLib/src/System/Diagnostics/DiagnosticMethodInfo.NativeAot.cs` (CSHARP) | Magnitude: 49.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 9, func_start: 7, api: 7
- `src/coreclr/tools/r2rdump/CoreDisTools.cs` (CSHARP) | Magnitude: 0.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 248, state_mutation: 71, doc: 59, branch: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/CreationPolicy.cs` (CSHARP) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 18, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `src/native/external/libunwind/src/riscv/Gapply_reg_state.c` (C) | Magnitude: 0.01 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 5, pointers: 5, structural_boundaries: 4, ownership: 4
- `src/libraries/System.Private.CoreLib/src/System/Numerics/DivisionRounding.cs` (CSHARP) | Magnitude: 21.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 20, indent_spaces: 8, state_mutation: 5, structural_boundaries: 2
- `src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/LineInfoAnnotation.cs` (CSHARP) | Magnitude: 9.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 10, doc: 8, api: 4, dead_code: 3
- `src/native/external/libunwind/src/loongarch64/regname.c` (C) | Magnitude: 0.01 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, branch: 5, ownership: 4, api: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/coreclr/jit/compiler.h` -> Churn: **95.83%** | Cog Load: 57.4041% | Debt: 54.6602%
- `src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/SOSDacImpl.cs` -> Churn: **89.82%** | Cog Load: 34.0172% | Debt: 92.0941%
- `src/coreclr/jit/codegenwasm.cpp` -> Churn: **87.5%** | Cog Load: 96.1732% | Debt: 69.376%
- `src/coreclr/jit/lower.cpp` -> Churn: **80.66%** | Cog Load: 94.998% | Debt: 64.8077%
- `src/coreclr/jit/morph.cpp` -> Churn: **79.06%** | Cog Load: 78.8892% | Debt: 15.6463%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/coreclr/jit/emitarm64sve.cpp` -> **Yat Long Poon** (100.0% isolated ownership) | Magnitude: 24630.44
- `src/coreclr/nativeaot/Runtime/StackFrameIterator.cpp` -> **Copilot** (100.0% isolated ownership) | Magnitude: 18258.61
- `src/coreclr/jit/lsra.cpp` -> **Jakob Botsch Nielsen** (100.0% isolated ownership) | Magnitude: 11311.18
- `src/coreclr/gc/plan_phase.cpp` -> **Jan Vorlicek** (100.0% isolated ownership) | Magnitude: 8646.84
- `src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextReaderImpl.cs` -> **Christopher Haugen** (100.0% isolated ownership) | Magnitude: 7857.48

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/coreclr/inc/utilcode.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `src/coreclr/vm/frames.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 95.9524%)
- `src/coreclr/inc/caparser.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.954%)
- `src/coreclr/inc/sigparser.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `src/coreclr/vm/appdomain.hpp` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 87.8774%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/libraries/System.Runtime.InteropServices/ref/System.Runtime.InteropServices.cs` -> **Severity: 5126.0** (Blast Radius: 51.26 * Doc Risk: 100.0%)
- `src/libraries/System.Linq/ref/System.Linq.cs` -> **Severity: 2351.2** (Blast Radius: 23.512 * Doc Risk: 100.0%)
- `src/libraries/System.Threading/ref/System.Threading.cs` -> **Severity: 1794.6** (Blast Radius: 17.946 * Doc Risk: 100.0%)
- `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` -> **Severity: 571.8** (Blast Radius: 5.718 * Doc Risk: 100.0%)
- `src/libraries/System.ComponentModel/ref/System.ComponentModel.cs` -> **Severity: 560.468** (Blast Radius: 5.607 * Doc Risk: 99.9586%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
