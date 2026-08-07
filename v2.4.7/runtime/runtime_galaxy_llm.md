# ARCHITECTURAL_BRIEF: runtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/runtime` |
| **Timestamp** | `2026-08-07T05:35:06.122945+00:00` |
| **Scan Duration** | `197.75s` |
| **Git Branch** | `main` |
| **Git Commit** | `aba46e33ea5ddd45d90e5c6a8b46bba6744ddc9a` |
| **Git Remote** | `https://github.com/dotnet/runtime.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 37810 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.62`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 26770 | 64.9% |
| file_cluster_13 | 6336 | 15.4% |
| file_cluster_0 | 3428 | 8.3% |
| file_cluster_16 | 1914 | 4.6% |
| file_cluster_4 | 899 | 2.2% |
| file_cluster_7 | 256 | 0.6% |
| file_cluster_9 | 110 | 0.3% |
| file_cluster_15 | 95 | 0.2% |
| file_cluster_11 | 89 | 0.2% |
| file_cluster_12 | 65 | 0.2% |
| file_cluster_17 | 52 | 0.1% |
| file_cluster_6 | 28 | 0.1% |
| file_cluster_1 | 28 | 0.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 23.7 | 10.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 38.0 | 44.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 20.3 | 6.0 | 5.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 31.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 19.4 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
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

- `TestEntryPoint` (@ `src/tests/JIT/Regression/CLR-x86-JIT/V1-M12-Beta2/b71005/b71005.cs`) -> Impact: **3952.3** | LOC: 521
- `func` (@ `src/tests/JIT/jit64/regress/vsw/524070/test2.cs`) -> Impact: **2452.0** | LOC: 1278
- `emitter::emitInsWritesToLclVarStackLoc` (@ `src/coreclr/jit/emitloongarch64.cpp`) -> Impact: **1914.4** | LOC: 1884
- `Sub_Funclet_0` (@ `src/tests/JIT/Directed/cmov/Bool_No_Op.cs`) -> Impact: **1552.0** | LOC: 280
- `Sub_Funclet_1` (@ `src/tests/JIT/Directed/cmov/Bool_No_Op.cs`) -> Impact: **1552.0** | LOC: 280
- `Sub_Funclet_2` (@ `src/tests/JIT/Directed/cmov/Bool_No_Op.cs`) -> Impact: **1552.0** | LOC: 280
- `Class1` (@ `src/tests/JIT/Methodical/eh/nested/nonlocalexit/throwinfinallyrecursive_20.cs`) -> Impact: **1526.5** | LOC: 877
- `emitter::emitIns_R_ARX` (@ `src/coreclr/jit/emitxarch.cpp`) -> Impact: **1440.1** | LOC: 1956
- `push_type_explicit` (@ `src/mono/mono/mini/interp/transform.c`) -> Impact: **1422.7** | LOC: 1538
- `emitter::emitIns_R_R_I` (@ `src/coreclr/jit/emitarm64.cpp`) -> Impact: **1393.3** | LOC: 1747

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/tests/JIT/Directed/cmov` | 16 | 395230.0 | 42.77% | 0.0% |
| `src/coreclr/jit` | 290 | 259266.52 | 51.63% | 47.93% |
| `src/coreclr/vm` | 512 | 174222.49 | 42.96% | 52.66% |
| `src/mono/mono/mini` | 159 | 132462.16 | 51.12% | 50.37% |
| `src/mono/mono/metadata` | 162 | 63474.06 | 36.05% | 42.74% |
| `src/libraries/System.Private.CoreLib/src/System` | 276 | 53545.24 | 24.53% | 65.57% |
| `src/tests/JIT/Regression/VS-ia64-JIT/V1.2-M01/b10827` | 1 | 53460.66 | 63.17% | 0.0% |
| `src/tests/JIT/Directed/Convert` | 12 | 49594.28 | 22.87% | 0.0% |
| `src/tests/JIT/opt/virtualstubdispatch/bigvtbl` | 1 | 41768.56 | 15.69% | 0.0% |
| `src/mono/mono/tests` | 626 | 41695.96 | 15.72% | 0.0% |

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
- `src/tests/JIT/opt/virtualstubdispatch/bigvtbl/bigvtbl.cs` -> **1** Orphaned Functions | **11996** Duplicates
- `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` -> **0** Orphaned Functions | **10423** Duplicates
- `src/libraries/System.Runtime/ref/System.Runtime.cs` -> **585** Orphaned Functions | **7228** Duplicates
- `src/libraries/System.Private.CoreLib/src/System/Runtime/Intrinsics/Arm/AdvSimd.PlatformNotSupported.cs` -> **44** Orphaned Functions | **2584** Duplicates
- `src/libraries/System.Private.CoreLib/src/System/Runtime/Intrinsics/Arm/AdvSimd.cs` -> **8** Orphaned Functions | **2584** Duplicates

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
142. **`src/libraries/System.CodeDom/src/Microsoft/CSharp/CSharpCodeGenerator.cs`** -> AI Confidence: **99.48%**
143. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/ConfigurationElement.cs`** -> AI Confidence: **99.48%**
144. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/MgmtConfigurationRecord.cs`** -> AI Confidence: **99.48%**
145. **`src/libraries/System.Data.Common/src/System/Data/XMLSchema.cs`** -> AI Confidence: **99.48%**
146. **`src/libraries/System.Data.Common/src/System/Data/XmlDataLoader.cs`** -> AI Confidence: **99.48%**
147. **`src/libraries/System.Data.Common/src/System/Xml/XmlDataDocument.cs`** -> AI Confidence: **99.48%**
148. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcConnection.cs`** -> AI Confidence: **99.48%**
149. **`src/libraries/System.Data.OleDb/src/ColumnBinding.cs`** -> AI Confidence: **99.48%**
150. **`src/libraries/System.Data.OleDb/src/OleDbDataReader.cs`** -> AI Confidence: **99.48%**
151. **`src/libraries/System.Data.OleDb/src/OleDbMetaDataFactory.cs`** -> AI Confidence: **99.48%**
152. **`src/libraries/System.DirectoryServices.Protocols/src/System/DirectoryServices/Protocols/ldap/LdapConnection.cs`** -> AI Confidence: **99.48%**
153. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchemaClass.cs`** -> AI Confidence: **99.48%**
154. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/Domain.cs`** -> AI Confidence: **99.48%**
155. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarHeader.Read.cs`** -> AI Confidence: **99.48%**
156. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/NamedPipeServerStream.Windows.cs`** -> AI Confidence: **99.48%**
157. **`src/libraries/System.IO.Ports/src/System/IO/Ports/SerialStream.Windows.cs`** -> AI Confidence: **99.48%**
158. **`src/libraries/System.Management/src/System/Management/WMIGenerator.cs`** -> AI Confidence: **99.48%**
159. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiHttpWorld.wit.imports.wasi.http.v0_2_0.OutgoingHandlerInterop.cs`** -> AI Confidence: **99.48%**
160. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiHttpWorld.wit.imports.wasi.http.v0_2_0.TypesInterop.cs`** -> AI Confidence: **99.48%**
161. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/MsQuicConfiguration.cs`** -> AI Confidence: **99.48%**
162. **`src/libraries/System.Private.CoreLib/src/System/Text/Ascii.Utility.cs`** -> AI Confidence: **99.48%**
163. **`src/libraries/System.Private.CoreLib/src/System/Text/Unicode/Utf8Utility.Transcoding.cs`** -> AI Confidence: **99.48%**
164. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonFormatReaderGenerator.cs`** -> AI Confidence: **99.48%**
165. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonFormatWriterGenerator.cs`** -> AI Confidence: **99.48%**
166. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/XmlJsonReader.cs`** -> AI Confidence: **99.48%**
167. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBaseWriter.cs`** -> AI Confidence: **99.48%**
168. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBinaryWriter.cs`** -> AI Confidence: **99.48%**
169. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlUTF8TextReader.cs`** -> AI Confidence: **99.48%**
170. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/LoadFromReader.cs`** -> AI Confidence: **99.48%**
171. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/InputSpace.cs`** -> AI Confidence: **99.48%**
172. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/XmlFactoryWriterTests.cs`** -> AI Confidence: **99.48%**
173. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlCharCheckingWriter.cs`** -> AI Confidence: **99.48%**
174. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextWriter.cs`** -> AI Confidence: **99.48%**
175. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWellFormedWriter.cs`** -> AI Confidence: **99.48%**
176. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/DocumentSchemaValidator.cs`** -> AI Confidence: **99.48%**
177. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/DtdParser.cs`** -> AI Confidence: **99.48%**
178. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/Parser.cs`** -> AI Confidence: **99.48%**
179. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/Preprocessor.cs`** -> AI Confidence: **99.48%**
180. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/SchemaSetCompiler.cs`** -> AI Confidence: **99.48%**
181. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XdrBuilder.cs`** -> AI Confidence: **99.48%**
182. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XdrValidator.cs`** -> AI Confidence: **99.48%**
183. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchemaValidator.cs`** -> AI Confidence: **99.48%**
184. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XsdValidator.cs`** -> AI Confidence: **99.48%**
185. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationReaderILGen.cs`** -> AI Confidence: **99.48%**
186. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationWriter.cs`** -> AI Confidence: **99.48%**
187. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationWriterILGen.cs`** -> AI Confidence: **99.48%**
188. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/GenerateHelper.cs`** -> AI Confidence: **99.48%**
189. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ContainerAction.cs`** -> AI Confidence: **99.48%**
190. **`src/libraries/System.Runtime/tests/System.IO.FileSystem.Tests/Directory/ReparsePoints_MountVolume.cs`** -> AI Confidence: **99.48%**
191. **`src/libraries/System.ServiceModel.Syndication/src/System/ServiceModel/Syndication/Atom10FeedFormatter.cs`** -> AI Confidence: **99.48%**
192. **`src/libraries/System.ServiceModel.Syndication/src/System/ServiceModel/Syndication/Rss20FeedFormatter.cs`** -> AI Confidence: **99.48%**
193. **`src/libraries/System.Speech/src/Internal/Synthesis/SSmlParser.cs`** -> AI Confidence: **99.48%**
194. **`src/libraries/System.Speech/src/Synthesis/PromptBuilder.cs`** -> AI Confidence: **99.48%**
195. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/DBCSCodePageEncoding.cs`** -> AI Confidence: **99.48%**
196. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/GB18030Encoding.cs`** -> AI Confidence: **99.48%**
197. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/ISO2022Encoding.cs`** -> AI Confidence: **99.48%**
198. **`src/libraries/System.Transactions.Local/src/System/Transactions/TransactionsEtwProvider.cs`** -> AI Confidence: **99.48%**
199. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/SOSDacImpl.cs`** -> AI Confidence: **99.48%**
200. **`src/tests/GC/Features/PartialCompaction/partialcompactionwloh.cs`** -> AI Confidence: **99.48%**
201. **`src/tests/GC/Stress/Framework/ReliabilityFramework.cs`** -> AI Confidence: **99.48%**
202. **`src/mono/browser/runtime/marshal-to-cs.ts`** -> AI Confidence: **99.48%**
203. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/marshal-to-cs.ts`** -> AI Confidence: **99.48%**
204. **`src/native/libs/System.Globalization.Native/pal_locale.m`** -> AI Confidence: **99.48%**
205. **`src/tasks/AppleAppBuilder/Templates/runtime-librarymode.m`** -> AI Confidence: **99.48%**
206. **`src/tasks/AppleAppBuilder/Templates/runtime.m`** -> AI Confidence: **99.48%**
207. **`src/coreclr/ilasm/ilasmpch.h`** -> AI Confidence: **99.44%**
208. **`src/native/external/libunwind/include/tdep/jmpbuf.h`** -> AI Confidence: **99.44%**
209. **`src/native/external/rapidjson/rapidjson.h`** -> AI Confidence: **99.44%**
210. **`src/native/external/zlib-ng/arch_functions.h`** -> AI Confidence: **99.44%**
211. **`src/native/libs/System.Globalization.Native/pal_icushim_internal.h`** -> AI Confidence: **99.44%**
212. **`src/native/external/brotli/c/enc/backward_references.h`** -> AI Confidence: **99.43%**
213. **`src/native/external/brotli/c/enc/histogram.h`** -> AI Confidence: **99.43%**
214. **`src/native/external/libunwind/src/ia64/Gfind_unwind_table.c`** -> AI Confidence: **99.43%**
215. **`src/coreclr/pal/src/file/path.cpp`** -> AI Confidence: **99.43%**
216. **`src/mono/mono/utils/mono-compiler.h`** -> AI Confidence: **99.43%**
217. **`src/native/external/llvm-libunwind/src/DwarfInstructions.hpp`** -> AI Confidence: **99.43%**
218. **`src/mono/mono/mini/mini-arch.h`** -> AI Confidence: **99.42%**
219. **`src/native/external/libunwind/include/tdep/dwarf-config.h`** -> AI Confidence: **99.42%**
220. **`src/native/external/libunwind/include/tdep/libunwind_i.h.in`** -> AI Confidence: **99.42%**
221. **`src/native/external/zlib-ng/zbuild.h`** -> AI Confidence: **99.42%**
222. **`src/native/external/zstd/lib/common/compiler.h`** -> AI Confidence: **99.42%**
223. **`src/native/external/zstd/lib/common/zstd_deps.h`** -> AI Confidence: **99.42%**
224. **`src/coreclr/scripts/superpmi.py`** -> AI Confidence: **99.39%**
225. **`src/mono/mono/eglib/gfile-posix.c`** -> AI Confidence: **99.39%**
226. **`src/mono/mono/eglib/gfile-unix.c`** -> AI Confidence: **99.39%**
227. **`src/mono/mono/eglib/gmisc-win32.c`** -> AI Confidence: **99.39%**
228. **`src/mono/mono/metadata/assembly.c`** -> AI Confidence: **99.39%**
229. **`src/mono/mono/metadata/class.c`** -> AI Confidence: **99.39%**
230. **`src/mono/mono/metadata/custom-attrs.c`** -> AI Confidence: **99.39%**
231. **`src/mono/mono/metadata/icall.c`** -> AI Confidence: **99.39%**
232. **`src/mono/mono/metadata/marshal.c`** -> AI Confidence: **99.39%**
233. **`src/mono/mono/metadata/native-library.c`** -> AI Confidence: **99.39%**
234. **`src/mono/mono/metadata/reflection.c`** -> AI Confidence: **99.39%**
235. **`src/mono/mono/metadata/sgen-new-bridge.c`** -> AI Confidence: **99.39%**
236. **`src/mono/mono/metadata/sre.c`** -> AI Confidence: **99.39%**
237. **`src/mono/mono/metadata/unsafe-accessor.c`** -> AI Confidence: **99.39%**
238. **`src/mono/mono/metadata/weak-hash.c`** -> AI Confidence: **99.39%**
239. **`src/mono/mono/mini/debug-mini.c`** -> AI Confidence: **99.39%**
240. **`src/mono/mono/mini/interp/interp.c`** -> AI Confidence: **99.39%**
241. **`src/mono/mono/mini/mini-exceptions.c`** -> AI Confidence: **99.39%**
242. **`src/mono/mono/mini/mini-generic-sharing.c`** -> AI Confidence: **99.39%**
243. **`src/mono/mono/mini/mini-ppc.c`** -> AI Confidence: **99.39%**
244. **`src/mono/mono/mini/mini-runtime.c`** -> AI Confidence: **99.39%**
245. **`src/mono/mono/mini/mini-trampolines.c`** -> AI Confidence: **99.39%**
246. **`src/mono/mono/mini/mini.c`** -> AI Confidence: **99.39%**
247. **`src/mono/mono/mini/monovm.c`** -> AI Confidence: **99.39%**
248. **`src/mono/mono/mini/simd-intrinsics.c`** -> AI Confidence: **99.39%**
249. **`src/mono/mono/mini/tramp-amd64.c`** -> AI Confidence: **99.39%**
250. **`src/mono/mono/mini/tramp-arm64.c`** -> AI Confidence: **99.39%**
251. **`src/mono/mono/profiler/aot.c`** -> AI Confidence: **99.39%**
252. **`src/mono/mono/profiler/mprof-report.c`** -> AI Confidence: **99.39%**
253. **`src/mono/mono/sgen/sgen-gc.c`** -> AI Confidence: **99.39%**
254. **`src/mono/mono/utils/lock-free-array-queue.c`** -> AI Confidence: **99.39%**
255. **`src/mono/mono/utils/mono-threads-state-machine.c`** -> AI Confidence: **99.39%**
256. **`src/mono/mono/utils/parse.c`** -> AI Confidence: **99.39%**
257. **`src/native/external/brotli/c/dec/decode.c`** -> AI Confidence: **99.39%**
258. **`src/native/external/brotli/c/enc/backward_references_hq.c`** -> AI Confidence: **99.39%**
259. **`src/native/external/brotli/c/enc/brotli_bit_stream.c`** -> AI Confidence: **99.39%**
260. **`src/native/external/brotli/c/enc/metablock.c`** -> AI Confidence: **99.39%**
261. **`src/native/external/libunwind/src/coredump/_UCD_create.c`** -> AI Confidence: **99.39%**
262. **`src/native/external/libunwind/src/nto/unw_nto_find_proc_info.c`** -> AI Confidence: **99.39%**
263. **`src/native/external/libunwind/src/setjmp/longjmp.c`** -> AI Confidence: **99.39%**
264. **`src/native/external/libunwind/tests/Garm64-test-sve-signal.c`** -> AI Confidence: **99.39%**
265. **`src/native/external/libunwind/tests/Gia64-test-nat.c`** -> AI Confidence: **99.39%**
266. **`src/native/external/libunwind/tests/Gtest-bt.c`** -> AI Confidence: **99.39%**
267. **`src/native/external/libunwind/tests/crasher.c`** -> AI Confidence: **99.39%**
268. **`src/native/external/libunwind/tests/test-setjmp.c`** -> AI Confidence: **99.39%**
269. **`src/native/external/zlib-ng/arch/x86/x86_features.c`** -> AI Confidence: **99.39%**
270. **`src/native/external/zstd/lib/compress/fse_compress.c`** -> AI Confidence: **99.39%**
271. **`src/native/libs/System.Native/pal_runtimeinformation.c`** -> AI Confidence: **99.39%**
272. **`src/native/libs/System.Security.Cryptography.Native/opensslshim.c`** -> AI Confidence: **99.39%**
273. **`src/native/minipal/random.c`** -> AI Confidence: **99.39%**
274. **`src/coreclr/binder/applicationcontext.cpp`** -> AI Confidence: **99.39%**
275. **`src/coreclr/binder/assemblybindercommon.cpp`** -> AI Confidence: **99.39%**
276. **`src/coreclr/binder/assemblyname.cpp`** -> AI Confidence: **99.39%**
277. **`src/coreclr/gc/objecthandle.cpp`** -> AI Confidence: **99.39%**
278. **`src/coreclr/gcinfo/gcinfoencoder.cpp`** -> AI Confidence: **99.39%**
279. **`src/coreclr/ildasm/dman.cpp`** -> AI Confidence: **99.39%**
280. **`src/coreclr/jit/ee_il_dll.cpp`** -> AI Confidence: **99.39%**
281. **`src/coreclr/md/compiler/disp.cpp`** -> AI Confidence: **99.39%**
282. **`src/coreclr/md/compiler/mdutil.cpp`** -> AI Confidence: **99.39%**
283. **`src/coreclr/md/compiler/regmeta.cpp`** -> AI Confidence: **99.39%**
284. **`src/coreclr/md/compiler/regmeta_import.cpp`** -> AI Confidence: **99.39%**
285. **`src/coreclr/md/compiler/regmeta_vm.cpp`** -> AI Confidence: **99.39%**
286. **`src/coreclr/md/enc/liteweightstgdbrw.cpp`** -> AI Confidence: **99.39%**
287. **`src/coreclr/md/enc/mdinternalrw.cpp`** -> AI Confidence: **99.39%**
288. **`src/coreclr/md/enc/metamodelrw.cpp`** -> AI Confidence: **99.39%**
289. **`src/coreclr/nativeaot/Runtime/eventtrace.cpp`** -> AI Confidence: **99.39%**
290. **`src/coreclr/nativeaot/Runtime/unix/HardwareExceptions.cpp`** -> AI Confidence: **99.39%**
291. **`src/coreclr/nativeaot/Runtime/unix/UnixNativeCodeManager.cpp`** -> AI Confidence: **99.39%**
292. **`src/coreclr/nativeaot/Runtime/unix/cgroupcpu.cpp`** -> AI Confidence: **99.39%**
293. **`src/coreclr/pal/src/misc/cgroup.cpp`** -> AI Confidence: **99.39%**
294. **`src/coreclr/pal/src/safecrt/vsprintf.cpp`** -> AI Confidence: **99.39%**
295. **`src/coreclr/pal/src/synchmgr/synchmanager.cpp`** -> AI Confidence: **99.39%**
296. **`src/coreclr/pal/src/thread/context.cpp`** -> AI Confidence: **99.39%**
297. **`src/coreclr/pal/src/thread/process.cpp`** -> AI Confidence: **99.39%**
298. **`src/coreclr/pal/src/thread/thread.cpp`** -> AI Confidence: **99.39%**
299. **`src/coreclr/tools/superpmi/superpmi-shared/callutils.cpp`** -> AI Confidence: **99.39%**
300. **`src/coreclr/tools/superpmi/superpmi/commandline.cpp`** -> AI Confidence: **99.39%**
301. **`src/coreclr/tools/superpmi/superpmi/streamingsuperpmi.cpp`** -> AI Confidence: **99.39%**
302. **`src/coreclr/utilcode/util.cpp`** -> AI Confidence: **99.39%**
303. **`src/coreclr/vm/assembly.cpp`** -> AI Confidence: **99.39%**
304. **`src/coreclr/vm/binder.cpp`** -> AI Confidence: **99.39%**
305. **`src/coreclr/vm/cdacstress.cpp`** -> AI Confidence: **99.39%**
306. **`src/coreclr/vm/class.cpp`** -> AI Confidence: **99.39%**
307. **`src/coreclr/vm/comcallablewrapper.cpp`** -> AI Confidence: **99.39%**
308. **`src/coreclr/vm/comdelegate.cpp`** -> AI Confidence: **99.39%**
309. **`src/coreclr/vm/commodule.cpp`** -> AI Confidence: **99.39%**
310. **`src/coreclr/vm/comtoclrcall.cpp`** -> AI Confidence: **99.39%**
311. **`src/coreclr/vm/crst.cpp`** -> AI Confidence: **99.39%**
312. **`src/coreclr/vm/debugdebugger.cpp`** -> AI Confidence: **99.39%**
313. **`src/coreclr/vm/dispatchinfo.cpp`** -> AI Confidence: **99.39%**
314. **`src/coreclr/vm/eeconfig.cpp`** -> AI Confidence: **99.39%**
315. **`src/coreclr/vm/eventtrace_bulktype.cpp`** -> AI Confidence: **99.39%**
316. **`src/coreclr/vm/exceptionhandling.cpp`** -> AI Confidence: **99.39%**
317. **`src/coreclr/vm/finalizerthread.cpp`** -> AI Confidence: **99.39%**
318. **`src/coreclr/vm/gcenv.ee.cpp`** -> AI Confidence: **99.39%**
319. **`src/coreclr/vm/gchelpers.cpp`** -> AI Confidence: **99.39%**
320. **`src/coreclr/vm/ilstubcache.cpp`** -> AI Confidence: **99.39%**
321. **`src/coreclr/vm/methodtable.cpp`** -> AI Confidence: **99.39%**
322. **`src/coreclr/vm/reflectioninvocation.cpp`** -> AI Confidence: **99.39%**
323. **`src/coreclr/vm/stublink.cpp`** -> AI Confidence: **99.39%**
324. **`src/coreclr/vm/threadsuspend.cpp`** -> AI Confidence: **99.39%**
325. **`src/coreclr/vm/typestring.cpp`** -> AI Confidence: **99.39%**
326. **`src/coreclr/vm/util.cpp`** -> AI Confidence: **99.39%**
327. **`src/native/corehost/bundle/extractor.cpp`** -> AI Confidence: **99.39%**
328. **`src/native/corehost/hostpolicy/deps_resolver.cpp`** -> AI Confidence: **99.39%**
329. **`src/native/corehost/test/nativehost/nativehost.cpp`** -> AI Confidence: **99.39%**
330. **`src/native/external/libunwind/include/libunwind_i.h`** -> AI Confidence: **99.39%**
331. **`src/native/external/llvm-libunwind/src/Unwind-EHABI.cpp`** -> AI Confidence: **99.39%**
332. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/Eabi/EabiUnwindConverter.cs`** -> AI Confidence: **99.39%**
333. **`src/coreclr/tools/aot/ILCompiler.Compiler/IL/ILImporter.Scanner.cs`** -> AI Confidence: **99.39%**
334. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/DebugInfoTableNode.cs`** -> AI Confidence: **99.39%**
335. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/IBC/IBCProfileParser.cs`** -> AI Confidence: **99.39%**
336. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/JitInterface/CorInfoImpl.ReadyToRun.cs`** -> AI Confidence: **99.39%**
337. **`src/coreclr/tools/r2rtest/BuildFolderSet.cs`** -> AI Confidence: **99.39%**
338. **`src/coreclr/tools/runincontext/runincontext.cs`** -> AI Confidence: **99.39%**
339. **`src/installer/tests/HostActivation.Tests/NativeHosting/HostContext.cs`** -> AI Confidence: **99.39%**
340. **`src/libraries/Common/src/System/Diagnostics/NetFrameworkUtils.cs`** -> AI Confidence: **99.39%**
341. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Semantics/Conversion.cs`** -> AI Confidence: **99.39%**
342. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/SymbolTable.cs`** -> AI Confidence: **99.39%**
343. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/Emitter/CoreBindingHelpers.cs`** -> AI Confidence: **99.39%**
344. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/DependencyInjectionEventSource.cs`** -> AI Confidence: **99.39%**
345. **`src/libraries/Microsoft.Extensions.DependencyModel/src/DependencyContextJsonReader.cs`** -> AI Confidence: **99.39%**
346. **`src/libraries/Microsoft.Extensions.DependencyModel/src/DependencyContextWriter.cs`** -> AI Confidence: **99.39%**
347. **`src/libraries/Microsoft.Win32.Registry/src/Microsoft/Win32/RegistryKey.cs`** -> AI Confidence: **99.39%**
348. **`src/libraries/Microsoft.Win32.SystemEvents/src/Microsoft/Win32/SystemEvents.cs`** -> AI Confidence: **99.39%**
349. **`src/libraries/Microsoft.XmlSerializer.Generator/src/Sgen.cs`** -> AI Confidence: **99.39%**
350. **`src/libraries/System.CodeDom/src/Microsoft/VisualBasic/VBCodeGenerator.cs`** -> AI Confidence: **99.39%**
351. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/CompositionContainer.cs`** -> AI Confidence: **99.39%**
352. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/BaseConfigurationRecord.cs`** -> AI Confidence: **99.39%**
353. **`src/libraries/System.Data.Common/src/System/Data/DataRelation.cs`** -> AI Confidence: **99.39%**
354. **`src/libraries/System.Data.Common/src/System/Data/DataSet.cs`** -> AI Confidence: **99.39%**
355. **`src/libraries/System.Data.Common/src/System/Data/DataTable.cs`** -> AI Confidence: **99.39%**
356. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcParameter.cs`** -> AI Confidence: **99.39%**
357. **`src/libraries/System.Data.OleDb/src/OleDbCommand.cs`** -> AI Confidence: **99.39%**
358. **`src/libraries/System.Data.OleDb/src/System/Data/ProviderBase/DbConnectionPool.cs`** -> AI Confidence: **99.39%**
359. **`src/libraries/System.Diagnostics.Process/src/Microsoft/Win32/SafeHandles/SafeProcessHandle.Windows.cs`** -> AI Confidence: **99.39%**
360. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/ProcessManager.Windows.cs`** -> AI Confidence: **99.39%**
361. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADStoreCtx.cs`** -> AI Confidence: **99.39%**
362. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADStoreCtx_LoadStore.cs`** -> AI Confidence: **99.39%**
363. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADStoreCtx_Query.cs`** -> AI Confidence: **99.39%**
364. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/SDSUtils.cs`** -> AI Confidence: **99.39%**
365. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/Utils.cs`** -> AI Confidence: **99.39%**
366. **`src/libraries/System.IO.Compression/src/System/IO/Compression/ZipArchive.cs`** -> AI Confidence: **99.39%**
367. **`src/libraries/System.IO.Hashing/src/System/IO/Hashing/XxHashShared.cs`** -> AI Confidence: **99.39%**
368. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Expressions.cs`** -> AI Confidence: **99.39%**
369. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/DebugViewWriter.cs`** -> AI Confidence: **99.39%**
370. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/ExpressionStringBuilder.cs`** -> AI Confidence: **99.39%**
371. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Interpreter/LightCompiler.cs`** -> AI Confidence: **99.39%**
372. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/HttpConnectionPool.Http3.cs`** -> AI Confidence: **99.39%**
373. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpListener.Windows.cs`** -> AI Confidence: **99.39%**
374. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpListenerResponse.Windows.cs`** -> AI Confidence: **99.39%**
375. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpReplyReaderFactory.cs`** -> AI Confidence: **99.39%**
376. **`src/libraries/System.Net.Quic/src/System/Net/Quic/QuicConnection.SslConnectionOptions.cs`** -> AI Confidence: **99.39%**
377. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStream.Protocol.cs`** -> AI Confidence: **99.39%**
378. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/Socket.cs`** -> AI Confidence: **99.39%**
379. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncEventArgs.Windows.cs`** -> AI Confidence: **99.39%**
380. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncEventArgs.cs`** -> AI Confidence: **99.39%**
381. **`src/libraries/System.Private.CoreLib/src/System/Array.cs`** -> AI Confidence: **99.39%**
382. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Base64Helper/Base64DecoderHelper.cs`** -> AI Confidence: **99.39%**
383. **`src/libraries/System.Private.CoreLib/src/System/Environment.Windows.cs`** -> AI Confidence: **99.39%**
384. **`src/libraries/System.Private.CoreLib/src/System/Globalization/DateTimeFormat.cs`** -> AI Confidence: **99.39%**
385. **`src/libraries/System.Private.CoreLib/src/System/Reflection/MethodBaseInvoker.cs`** -> AI Confidence: **99.39%**
386. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ExtensionDataReader.cs`** -> AI Confidence: **99.39%**
387. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/ReflectionJsonFormatWriter.cs`** -> AI Confidence: **99.39%**
388. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/SchemaImporter.cs`** -> AI Confidence: **99.39%**
389. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlFormatReaderGenerator.cs`** -> AI Confidence: **99.39%**
390. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlFormatWriterGenerator.cs`** -> AI Confidence: **99.39%**
391. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlDictionaryWriter.cs`** -> AI Confidence: **99.39%**
392. **`src/libraries/System.Private.Uri/src/System/Uri.cs`** -> AI Confidence: **99.39%**
393. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/XContainer.cs`** -> AI Confidence: **99.39%**
394. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Schema/XNodeValidator.cs`** -> AI Confidence: **99.39%**
395. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/XNodeSequenceRemove.cs`** -> AI Confidence: **99.39%**
396. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/CommonTests.cs`** -> AI Confidence: **99.39%**
397. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextReaderImpl.cs`** -> AI Confidence: **99.39%**
398. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextReaderImplAsync.cs`** -> AI Confidence: **99.39%**
399. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/DtdValidator.cs`** -> AI Confidence: **99.39%**
400. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/SchemaObjectWriter.cs`** -> AI Confidence: **99.39%**
401. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSchemaExporter.cs`** -> AI Confidence: **99.39%**
402. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSchemaImporter.cs`** -> AI Confidence: **99.39%**
403. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationReader.cs`** -> AI Confidence: **99.39%**
404. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XmlQueryTypeFactory.cs`** -> AI Confidence: **99.39%**
405. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/NumberAction.cs`** -> AI Confidence: **99.39%**
406. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/XsltArgumentList.cs`** -> AI Confidence: **99.39%**
407. **`src/libraries/System.Private.Xml/tests/Xslt/XslTransformApi/CXslTArgumentList.cs`** -> AI Confidence: **99.39%**
408. **`src/libraries/System.Private.Xml/tests/Xslt/XslTransformApi/XSLTransform.cs`** -> AI Confidence: **99.39%**
409. **`src/libraries/System.Reflection.DispatchProxy/src/System/Reflection/DispatchProxyGenerator.cs`** -> AI Confidence: **99.39%**
410. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/CacheUsage.cs`** -> AI Confidence: **99.39%**
411. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/Interop/JavaScriptExports.Mono.cs`** -> AI Confidence: **99.39%**
412. **`src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector512Tests.cs`** -> AI Confidence: **99.39%**
413. **`src/libraries/System.Runtime.Serialization.Xml/tests/SerializationTestTypes/ComparisonHelper.cs`** -> AI Confidence: **99.39%**
414. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/Reflection/TypeTests.GetMember.cs`** -> AI Confidence: **99.39%**
415. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskCancelWaitTest.cs`** -> AI Confidence: **99.39%**
416. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/CommonObjectSecurity.cs`** -> AI Confidence: **99.39%**
417. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/NativeObjectSecurity.cs`** -> AI Confidence: **99.39%**
418. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/Privilege.cs`** -> AI Confidence: **99.39%**
419. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/Win32.cs`** -> AI Confidence: **99.39%**
420. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/CmsSigner.cs`** -> AI Confidence: **99.39%**
421. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/SignedCms.cs`** -> AI Confidence: **99.39%**
422. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/CryptoConfig.cs`** -> AI Confidence: **99.39%**
423. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/EccKeyFormatHelper.cs`** -> AI Confidence: **99.39%**
424. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/HashProviderDispenser.Windows.cs`** -> AI Confidence: **99.39%**
425. **`src/libraries/System.ServiceProcess.ServiceController/src/System/ServiceProcess/ServiceBase.cs`** -> AI Confidence: **99.39%**
426. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/Arc.cs`** -> AI Confidence: **99.39%**
427. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/BackEnd.cs`** -> AI Confidence: **99.39%**
428. **`src/libraries/System.Speech/src/Internal/Synthesis/VoiceSynthesis.cs`** -> AI Confidence: **99.39%**
429. **`src/libraries/System.Speech/src/Recognition/RecognizerBase.cs`** -> AI Confidence: **99.39%**
430. **`src/libraries/System.Speech/src/Result/RecognizedPhrase.cs`** -> AI Confidence: **99.39%**
431. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/SBCSCodePageEncoding.cs`** -> AI Confidence: **99.39%**
432. **`src/libraries/System.Text.Json/gen/JsonSourceGenerator.Parser.cs`** -> AI Confidence: **99.39%**
433. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Collection/IEnumerableConverterFactory.cs`** -> AI Confidence: **99.39%**
434. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/FSharp/FSharpUnionConverter.cs`** -> AI Confidence: **99.39%**
435. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Metadata/DefaultJsonTypeInfoResolver.Helpers.cs`** -> AI Confidence: **99.39%**
436. **`src/libraries/System.Text.Json/src/System/Text/Json/ThrowHelper.Serialization.cs`** -> AI Confidence: **99.39%**
437. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.cs`** -> AI Confidence: **99.39%**
438. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Utf8JsonReaderTests.TryGet.cs`** -> AI Confidence: **99.39%**
439. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Utf8JsonReaderTests.cs`** -> AI Confidence: **99.39%**
440. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/Context/AMD64/AMD64Unwinder.cs`** -> AI Confidence: **99.39%**
441. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataMethodDefinition.cs`** -> AI Confidence: **99.39%**
442. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataMethodInstance.cs`** -> AI Confidence: **99.39%**
443. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataModule.cs`** -> AI Confidence: **99.39%**
444. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/Dbi/DacDbiImpl.cs`** -> AI Confidence: **99.39%**
445. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/SOSDacImpl.IXCLRDataProcess.cs`** -> AI Confidence: **99.39%**
446. **`src/tasks/AppleAppBuilder/AppleAppBuilder.cs`** -> AI Confidence: **99.39%**
447. **`src/tests/baseservices/exceptions/StackTracePreserve/StackTracePreserveTests.cs`** -> AI Confidence: **99.39%**
448. **`src/tests/baseservices/exceptions/unhandled/unhandledTester.cs`** -> AI Confidence: **99.39%**
449. **`src/tools/illink/test/Mono.Linker.Tests.Cases/DataFlow/FeatureCheckDataFlow.cs`** -> AI Confidence: **99.39%**
450. **`src/mono/browser/runtime/gc-handles.ts`** -> AI Confidence: **99.39%**
451. **`src/mono/browser/runtime/loader/config.ts`** -> AI Confidence: **99.39%**
452. **`src/mono/browser/runtime/managed-exports.ts`** -> AI Confidence: **99.39%**
453. **`src/tasks/AppleAppBuilder/Templates/runtime-coreclr.m`** -> AI Confidence: **99.39%**
454. **`src/mono/mono/mini/exceptions-amd64.c`** -> AI Confidence: **99.35%**
455. **`src/native/external/brotli/c/tools/brotli.c`** -> AI Confidence: **99.35%**
456. **`src/coreclr/vm/amd64/excepamd64.cpp`** -> AI Confidence: **99.35%**
457. **`src/coreclr/vm/eetwain.cpp`** -> AI Confidence: **99.35%**
458. **`src/coreclr/vm/excep.cpp`** -> AI Confidence: **99.35%**
459. **`src/coreclr/vm/profilinghelper.cpp`** -> AI Confidence: **99.35%**
460. **`src/coreclr/tools/ILTrim.Core/DependencyAnalysis/MethodBodyNode.cs`** -> AI Confidence: **99.35%**
461. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/Http3Connection.cs`** -> AI Confidence: **99.35%**
462. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpConnection.cs`** -> AI Confidence: **99.35%**
463. **`src/libraries/System.Net.WebSockets/src/System/Net/WebSockets/ManagedWebSocket.cs`** -> AI Confidence: **99.35%**
464. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/EventSource.cs`** -> AI Confidence: **99.35%**
465. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/FacetChecker.cs`** -> AI Confidence: **99.35%**
466. **`src/mono/browser/runtime/invoke-cs.ts`** -> AI Confidence: **99.35%**
467. **`.github/skills/ci-pipeline-monitor/scripts/generate_report.py`** -> AI Confidence: **99.34%**
468. **`src/coreclr/scripts/fuzzlyn_summarize.py`** -> AI Confidence: **99.34%**
469. **`src/mono/mono/eglib/gpath.c`** -> AI Confidence: **99.34%**
470. **`src/mono/mono/eglib/test/driver.c`** -> AI Confidence: **99.34%**
471. **`src/mono/mono/mini/alias-analysis.c`** -> AI Confidence: **99.34%**
472. **`src/mono/mono/mini/dominators.c`** -> AI Confidence: **99.34%**
473. **`src/mono/mono/mini/graph.c`** -> AI Confidence: **99.34%**
474. **`src/mono/mono/mini/helpers.c`** -> AI Confidence: **99.34%**
475. **`src/mono/mono/mini/main.c`** -> AI Confidence: **99.34%**
476. **`src/mono/mono/mini/tramp-arm64-gsharedvt.c`** -> AI Confidence: **99.34%**
477. **`src/mono/mono/mini/type-checking.c`** -> AI Confidence: **99.34%**
478. **`src/mono/mono/profiler/log-args.c`** -> AI Confidence: **99.34%**
479. **`src/mono/mono/unit-tests/test-path.c`** -> AI Confidence: **99.34%**
480. **`src/native/eventpipe/ep-json-file.c`** -> AI Confidence: **99.34%**
481. **`src/native/external/brotli/c/dec/huffman.c`** -> AI Confidence: **99.34%**
482. **`src/native/external/brotli/c/enc/entropy_encode.c`** -> AI Confidence: **99.34%**
483. **`src/native/external/brotli/c/enc/literal_cost.c`** -> AI Confidence: **99.34%**
484. **`src/native/external/brotli/c/enc/static_dict.c`** -> AI Confidence: **99.34%**
485. **`src/native/external/libunwind/src/ptrace/_UPT_access_reg.c`** -> AI Confidence: **99.34%**
486. **`src/native/external/libunwind/src/ptrace/_UPT_reg_offset.c`** -> AI Confidence: **99.34%**
487. **`src/native/external/libunwind/tests/Gia64-test-rbs.c`** -> AI Confidence: **99.34%**
488. **`src/native/external/libunwind/tests/Gtest-concurrent.c`** -> AI Confidence: **99.34%**
489. **`src/native/external/libunwind/tests/Gx64-test-dwarf-expressions.c`** -> AI Confidence: **99.34%**
490. **`src/native/external/zlib-ng/deflate.c`** -> AI Confidence: **99.34%**
491. **`src/native/external/zlib-ng/deflate_quick.c`** -> AI Confidence: **99.34%**
492. **`src/native/external/zlib-ng/deflate_rle.c`** -> AI Confidence: **99.34%**
493. **`src/native/external/zlib-ng/trees.c`** -> AI Confidence: **99.34%**
494. **`src/native/external/zstd/lib/dictBuilder/divsufsort.c`** -> AI Confidence: **99.34%**
495. **`src/native/libs/System.Globalization.Native/pal_localeNumberData.c`** -> AI Confidence: **99.34%**
496. **`src/native/libs/System.Security.Cryptography.Native.Android/pal_ecc_import_export.c`** -> AI Confidence: **99.34%**
497. **`src/coreclr/hosts/corerun/dotenv.cpp`** -> AI Confidence: **99.34%**
498. **`src/coreclr/ildasm/dasm_sz.cpp`** -> AI Confidence: **99.34%**
499. **`src/coreclr/ildasm/windasm.cpp`** -> AI Confidence: **99.34%**
500. **`src/coreclr/jit/codegenarm.cpp`** -> AI Confidence: **99.34%**
501. **`src/coreclr/jit/codegenarmarch.cpp`** -> AI Confidence: **99.34%**
502. **`src/coreclr/jit/emitarm.cpp`** -> AI Confidence: **99.34%**
503. **`src/coreclr/jit/lowerarmarch.cpp`** -> AI Confidence: **99.34%**
504. **`src/coreclr/jit/lsra.cpp`** -> AI Confidence: **99.34%**
505. **`src/coreclr/jit/lsraarm.cpp`** -> AI Confidence: **99.34%**
506. **`src/coreclr/jit/lsraarm64.cpp`** -> AI Confidence: **99.34%**
507. **`src/coreclr/jit/lsraarmarch.cpp`** -> AI Confidence: **99.34%**
508. **`src/coreclr/jit/lsraloongarch64.cpp`** -> AI Confidence: **99.34%**
509. **`src/coreclr/jit/lsrariscv64.cpp`** -> AI Confidence: **99.34%**
510. **`src/coreclr/md/compiler/assemblymd.cpp`** -> AI Confidence: **99.34%**
511. **`src/coreclr/minipal/Unix/dn-stdio.cpp`** -> AI Confidence: **99.34%**
512. **`src/coreclr/pal/src/arch/i386/signalhandlerhelper.cpp`** -> AI Confidence: **99.34%**
513. **`src/coreclr/pal/src/exception/machmessage.cpp`** -> AI Confidence: **99.34%**
514. **`src/coreclr/pal/src/map/map.cpp`** -> AI Confidence: **99.34%**
515. **`src/coreclr/pal/src/misc/environ.cpp`** -> AI Confidence: **99.34%**
516. **`src/coreclr/tools/superpmi/mcs/verbildump.cpp`** -> AI Confidence: **99.34%**
517. **`src/coreclr/tools/superpmi/mcs/verbjitflags.cpp`** -> AI Confidence: **99.34%**
518. **`src/coreclr/tools/superpmi/superpmi-shared/logging.cpp`** -> AI Confidence: **99.34%**
519. **`src/coreclr/tools/superpmi/superpmi/jitinstance.cpp`** -> AI Confidence: **99.34%**
520. **`src/coreclr/utilcode/ilformatter.cpp`** -> AI Confidence: **99.34%**
521. **`src/coreclr/utilcode/opinfo.cpp`** -> AI Confidence: **99.34%**
522. **`src/coreclr/utilcode/posterror.cpp`** -> AI Confidence: **99.34%**
523. **`src/coreclr/utilcode/prettyprintsig.cpp`** -> AI Confidence: **99.34%**
524. **`src/coreclr/utilcode/sbuffer.cpp`** -> AI Confidence: **99.34%**
525. **`src/coreclr/utilcode/stacktrace.cpp`** -> AI Confidence: **99.34%**
526. **`src/coreclr/utilcode/utsem.cpp`** -> AI Confidence: **99.34%**
527. **`src/coreclr/vm/arm64/stubs.cpp`** -> AI Confidence: **99.34%**
528. **`src/coreclr/vm/comdatetime.cpp`** -> AI Confidence: **99.34%**
529. **`src/coreclr/vm/commtmemberinfomap.cpp`** -> AI Confidence: **99.34%**
530. **`src/coreclr/vm/exinfo.cpp`** -> AI Confidence: **99.34%**
531. **`src/coreclr/vm/pgo.cpp`** -> AI Confidence: **99.34%**
532. **`src/coreclr/vm/zapsig.cpp`** -> AI Confidence: **99.34%**
533. **`src/mono/mono/tests/split-tailcall-interface-conservestack.cpp`** -> AI Confidence: **99.34%**
534. **`src/native/corehost/fxr/standalone/hostpolicy_resolver.cpp`** -> AI Confidence: **99.34%**
535. **`src/native/external/llvm-libunwind/src/config.h`** -> AI Confidence: **99.34%**
536. **`src/native/external/zlib-ng/gzguts.h`** -> AI Confidence: **99.34%**
537. **`src/native/external/zlib-ng/win32/depcheck.cpp`** -> AI Confidence: **99.34%**
538. **`src/coreclr/nativeaot/Runtime.Base/src/System/Runtime/ExceptionHandling.cs`** -> AI Confidence: **99.34%**
539. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/InvokeUtils.cs`** -> AI Confidence: **99.34%**
540. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/DynamicInvokeInfo.cs`** -> AI Confidence: **99.34%**
541. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/TypeInfos/RuntimeTypeInfo.InvokeMember.cs`** -> AI Confidence: **99.34%**
542. **`src/coreclr/tools/Common/Compiler/DependencyAnalysis/ObjectDataBuilder.cs`** -> AI Confidence: **99.34%**
543. **`src/coreclr/tools/Common/JitInterface/SystemVStructClassificator.cs`** -> AI Confidence: **99.34%**
544. **`src/coreclr/tools/GCLogParser/parse-hb-log.cs`** -> AI Confidence: **99.34%**
545. **`src/coreclr/tools/ILTrim.Core/DependencyAnalysis/EcmaSignatureRewriter.cs`** -> AI Confidence: **99.34%**
546. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_ARM/ARMReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
547. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_ARM64/ARM64ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
548. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_LoongArch64/LoongArch64ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
549. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_RiscV64/RiscV64ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
550. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_X64/X64ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
551. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_X86/X86ReadyToRunHelperNode.cs`** -> AI Confidence: **99.34%**
552. **`src/coreclr/tools/dotnet-pgo/SPGO/FlowSmoothing.cs`** -> AI Confidence: **99.34%**
553. **`src/libraries/Common/src/System/Data/Common/DbConnectionOptions.Common.cs`** -> AI Confidence: **99.34%**
554. **`src/libraries/Common/src/System/Net/Http/aspnetcore/Http3/QPack/QPackDecoder.cs`** -> AI Confidence: **99.34%**
555. **`src/libraries/Common/src/System/Number.Formatting.Common.cs`** -> AI Confidence: **99.34%**
556. **`src/libraries/Common/tests/System/Xml/XmlCoreTest/ManagedNodeWriter.cs`** -> AI Confidence: **99.34%**
557. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Errors/UserStringBuilder.cs`** -> AI Confidence: **99.34%**
558. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Semantics/Operators.cs`** -> AI Confidence: **99.34%**
559. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/MaskedTextProvider.cs`** -> AI Confidence: **99.34%**
560. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/XmlUtil.cs`** -> AI Confidence: **99.34%**
561. **`src/libraries/System.Data.Common/src/System/Data/Common/DBCommandBuilder.cs`** -> AI Confidence: **99.34%**
562. **`src/libraries/System.Data.Common/src/System/Data/Common/DbDataAdapter.cs`** -> AI Confidence: **99.34%**
563. **`src/libraries/System.Data.Common/src/System/Data/ProviderBase/SchemaMapping.cs`** -> AI Confidence: **99.34%**
564. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcMetaDataFactory.cs`** -> AI Confidence: **99.34%**
565. **`src/libraries/System.Data.OleDb/src/RowBinding.cs`** -> AI Confidence: **99.34%**
566. **`src/libraries/System.Diagnostics.TraceSource/src/System/Diagnostics/TraceInternal.cs`** -> AI Confidence: **99.34%**
567. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySite.cs`** -> AI Confidence: **99.34%**
568. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySiteLink.cs`** -> AI Confidence: **99.34%**
569. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ApplicationPartition.cs`** -> AI Confidence: **99.34%**
570. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/ZipPackage.cs`** -> AI Confidence: **99.34%**
571. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/NamedPipeServerStream.Unix.cs`** -> AI Confidence: **99.34%**
572. **`src/libraries/System.IO.Ports/tests/SerialPort/Handshake.cs`** -> AI Confidence: **99.34%**
573. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/ILGen.cs`** -> AI Confidence: **99.34%**
574. **`src/libraries/System.Net.Http/src/System/Net/Http/Headers/HeaderDescriptor.cs`** -> AI Confidence: **99.34%**
575. **`src/libraries/System.Net.NetworkInformation/src/System/Net/NetworkInformation/NetworkAddressChange.Unix.cs`** -> AI Confidence: **99.34%**
576. **`src/libraries/System.Net.Security/src/System/Net/Security/SslAuthenticationOptions.cs`** -> AI Confidence: **99.34%**
577. **`src/libraries/System.Private.CoreLib/src/System/Collections/Generic/Dictionary.cs`** -> AI Confidence: **99.34%**
578. **`src/libraries/System.Private.CoreLib/src/System/DefaultBinder.cs`** -> AI Confidence: **99.34%**
579. **`src/libraries/System.Private.CoreLib/src/System/HashCode.cs`** -> AI Confidence: **99.34%**
580. **`src/libraries/System.Private.CoreLib/src/System/SpanHelpers.Byte.cs`** -> AI Confidence: **99.34%**
581. **`src/libraries/System.Private.CoreLib/src/System/Text/Latin1Utility.cs`** -> AI Confidence: **99.34%**
582. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/EventsHelper.cs`** -> AI Confidence: **99.34%**
583. **`src/libraries/System.Private.Xml.Linq/tests/misc/XLinqErrata4.cs`** -> AI Confidence: **99.34%**
584. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/EndOfLineHandlingTests.cs`** -> AI Confidence: **99.34%**
585. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/WriterSettings.cs`** -> AI Confidence: **99.34%**
586. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/ErrorConditions.cs`** -> AI Confidence: **99.34%**
587. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWriter.cs`** -> AI Confidence: **99.34%**
588. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XsdValidatingReader.cs`** -> AI Confidence: **99.34%**
589. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlLoader.cs`** -> AI Confidence: **99.34%**
590. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/SchemaCollectionCompiler.cs`** -> AI Confidence: **99.34%**
591. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/SchemaCollectionpreProcessor.cs`** -> AI Confidence: **99.34%**
592. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XsdBuilder.cs`** -> AI Confidence: **99.34%**
593. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/ReflectionXmlSerializationWriter.cs`** -> AI Confidence: **99.34%**
594. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlCollation.cs`** -> AI Confidence: **99.34%**
595. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ApplyTemplatesAction.cs`** -> AI Confidence: **99.34%**
596. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/ErrorCondition.cs`** -> AI Confidence: **99.34%**
597. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCCloseOutput.cs`** -> AI Confidence: **99.34%**
598. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/XsltApiV2.cs`** -> AI Confidence: **99.34%**
599. **`src/libraries/System.Private.Xml/tests/Xslt/XslTransformApi/CXslTransform.cs`** -> AI Confidence: **99.34%**
600. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/BigIntegerToStringTests.cs`** -> AI Confidence: **99.34%**
601. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryFormatterWriter.cs`** -> AI Confidence: **99.34%**
602. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryObjectReader.cs`** -> AI Confidence: **99.34%**
603. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/Runtime/JitInfoTests.cs`** -> AI Confidence: **99.34%**
604. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskCreateTest.cs`** -> AI Confidence: **99.34%**
605. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskFromAsyncTest.cs`** -> AI Confidence: **99.34%**
606. **`src/libraries/System.ServiceModel.Syndication/src/System/ServiceModel/Syndication/AtomPub10ServiceDocumentFormatter.cs`** -> AI Confidence: **99.34%**
607. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/Graph.cs`** -> AI Confidence: **99.34%**
608. **`src/libraries/System.Speech/src/Internal/SrgsParser/XmlParser.cs`** -> AI Confidence: **99.34%**
609. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexNode.cs`** -> AI Confidence: **99.34%**
610. **`src/libraries/System.Threading.Tasks.Parallel/src/System/Threading/Tasks/Parallel.cs`** -> AI Confidence: **99.34%**
611. **`src/libraries/System.Transactions.Local/src/System/Transactions/Oletx/OletxResourceManager.cs`** -> AI Confidence: **99.34%**
612. **`src/mono/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeILGenerator.Mono.cs`** -> AI Confidence: **99.34%**
613. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/Context/X86/X86Unwinder.cs`** -> AI Confidence: **99.34%**
614. **`src/tests/GC/Features/PartialCompaction/partialcompactiontest.cs`** -> AI Confidence: **99.34%**
615. **`src/tests/GC/Scenarios/LeakWheel/leakwheel.cs`** -> AI Confidence: **99.34%**
616. **`src/tests/GC/Stress/Framework/RFLogging.cs`** -> AI Confidence: **99.34%**
617. **`src/tests/JIT/SIMD/VectorGet.cs`** -> AI Confidence: **99.34%**
618. **`src/tests/Regressions/coreclr/0582/csgen.1.cs`** -> AI Confidence: **99.34%**
619. **`src/tools/illink/src/linker/Linker.Steps/SweepStep.cs`** -> AI Confidence: **99.34%**
620. **`src/native/libs/System.Native/pal_environment.m`** -> AI Confidence: **99.34%**
621. **`src/mono/mono/mini/genmdesc.py`** -> AI Confidence: **99.32%**
622. **`src/tests/Common/scripts/migrate-tags.py`** -> AI Confidence: **99.32%**
623. **`src/mono/mono/eglib/gutf8.c`** -> AI Confidence: **99.32%**
624. **`src/mono/mono/mini/cfold.c`** -> AI Confidence: **99.32%**
625. **`src/mono/mono/mini/interp/transform-opt.c`** -> AI Confidence: **99.32%**
626. **`src/mono/mono/mini/linear-scan.c`** -> AI Confidence: **99.32%**
627. **`src/mono/mono/mini/liveness.c`** -> AI Confidence: **99.32%**
628. **`src/mono/mono/mini/seq-points.c`** -> AI Confidence: **99.32%**
629. **`src/mono/mono/utils/mono-hwcap-arm64.c`** -> AI Confidence: **99.32%**
630. **`src/mono/mono/utils/mono-hwcap-x86.c`** -> AI Confidence: **99.32%**
631. **`src/native/external/libunwind/src/ia64/Gregs.c`** -> AI Confidence: **99.32%**
632. **`src/native/external/libunwind/src/s390x/Lglobal.c`** -> AI Confidence: **99.32%**
633. **`src/native/external/libunwind/src/x86/Gos-linux.c`** -> AI Confidence: **99.32%**
634. **`src/native/external/libunwind/src/x86_64/Lglobal.c`** -> AI Confidence: **99.32%**
635. **`src/native/external/zlib-ng/arch/generic/crc32_braid_c.c`** -> AI Confidence: **99.32%**
636. **`src/native/external/zlib-ng/inftrees.c`** -> AI Confidence: **99.32%**
637. **`src/native/external/zstd/lib/compress/zstd_lazy.c`** -> AI Confidence: **99.32%**
638. **`src/native/libs/System.Security.Cryptography.Native.Apple/pal_seckey_macos.c`** -> AI Confidence: **99.32%**
639. **`src/coreclr/binder/defaultassemblybinder.cpp`** -> AI Confidence: **99.32%**
640. **`src/coreclr/binder/textualidentityparser.cpp`** -> AI Confidence: **99.32%**
641. **`src/coreclr/dlls/mscorpe/ceefilegenwritertokens.cpp`** -> AI Confidence: **99.32%**
642. **`src/coreclr/ilasm/assem.cpp`** -> AI Confidence: **99.32%**
643. **`src/coreclr/ildasm/util.hpp`** -> AI Confidence: **99.32%**
644. **`src/coreclr/inc/corhlprpriv.cpp`** -> AI Confidence: **99.32%**
645. **`src/coreclr/interpreter/compileropt.cpp`** -> AI Confidence: **99.32%**
646. **`src/coreclr/jit/assertionprop.cpp`** -> AI Confidence: **99.32%**
647. **`src/coreclr/jit/codegenlinear.cpp`** -> AI Confidence: **99.32%**
648. **`src/coreclr/jit/error.h`** -> AI Confidence: **99.32%**
649. **`src/coreclr/jit/fgdiagnostic.cpp`** -> AI Confidence: **99.32%**
650. **`src/coreclr/jit/inlinepolicy.cpp`** -> AI Confidence: **99.32%**
651. **`src/coreclr/jit/lower.cpp`** -> AI Confidence: **99.32%**
652. **`src/coreclr/jit/objectalloc.cpp`** -> AI Confidence: **99.32%**
653. **`src/coreclr/jit/promotiondecomposition.cpp`** -> AI Confidence: **99.32%**
654. **`src/coreclr/jit/scopeinfo.cpp`** -> AI Confidence: **99.32%**
655. **`src/coreclr/nativeaot/Runtime/arm64/AsmMacros_Shared.h`** -> AI Confidence: **99.32%**
656. **`src/coreclr/tools/superpmi/superpmi-shared/standardpch.h`** -> AI Confidence: **99.32%**
657. **`src/coreclr/tools/superpmi/superpmi/methodstatsemitter.cpp`** -> AI Confidence: **99.32%**
658. **`src/coreclr/unwinder/arm/unwinder.cpp`** -> AI Confidence: **99.32%**
659. **`src/coreclr/utilcode/sigparser.cpp`** -> AI Confidence: **99.32%**
660. **`src/coreclr/utilcode/splitpath.cpp`** -> AI Confidence: **99.32%**
661. **`src/coreclr/vm/gcenv.ee.common.cpp`** -> AI Confidence: **99.32%**
662. **`src/coreclr/vm/genanalysis.cpp`** -> AI Confidence: **99.32%**
663. **`src/coreclr/vm/unsafeaccessors.cpp`** -> AI Confidence: **99.32%**
664. **`src/native/public/mono/utils/details/mono-publib-types.h`** -> AI Confidence: **99.32%**
665. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaSignatureTranslator.cs`** -> AI Confidence: **99.32%**
666. **`src/coreclr/tools/Common/TypeSystem/IL/ILImporter.cs`** -> AI Confidence: **99.32%**
667. **`src/coreclr/tools/Common/TypeSystem/IL/ILStackHelper.cs`** -> AI Confidence: **99.32%**
668. **`src/coreclr/tools/Common/TypeSystem/IL/ILTokenReplacer.cs`** -> AI Confidence: **99.32%**
669. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/Amd64/UnwindInfo.cs`** -> AI Confidence: **99.32%**
670. **`src/coreclr/tools/aot/ILCompiler.TypeSystem.Tests/InstanceFieldLayoutTests.cs`** -> AI Confidence: **99.32%**
671. **`src/libraries/Common/src/System/Security/Cryptography/Asn1/DirectoryStringAsn.xml.cs`** -> AI Confidence: **99.32%**
672. **`src/libraries/Common/src/System/Security/Cryptography/Asn1/GeneralNameAsn.xml.cs`** -> AI Confidence: **99.32%**
673. **`src/libraries/Common/src/System/Security/Cryptography/Asn1/Pkcs7/CertificateChoiceAsn.xml.cs`** -> AI Confidence: **99.32%**
674. **`src/libraries/Common/tests/System/Xml/ModuleCore/cparser.cs`** -> AI Confidence: **99.32%**
675. **`src/libraries/System.CodeDom/src/System/CodeDom/Compiler/CodeGenerator.cs`** -> AI Confidence: **99.32%**
676. **`src/libraries/System.Data.Common/src/System/Data/Filter/ExpressionParser.cs`** -> AI Confidence: **99.32%**
677. **`src/libraries/System.Data.Common/tests/System/Data/DataTableReaderTest.cs`** -> AI Confidence: **99.32%**
678. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/DirectoryEntryManager.cs`** -> AI Confidence: **99.32%**
679. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ReplicationConnection.cs`** -> AI Confidence: **99.32%**
680. **`src/libraries/System.Formats.Asn1/src/System/Formats/Asn1/AsnWriter.Integer.cs`** -> AI Confidence: **99.32%**
681. **`src/libraries/System.Formats.Cbor/tests/Writer/CborWriterTests.Helpers.cs`** -> AI Confidence: **99.32%**
682. **`src/libraries/System.Management/src/System/Management/ManagementObject.cs`** -> AI Confidence: **99.32%**
683. **`src/libraries/System.Management/src/System/Management/Property.cs`** -> AI Confidence: **99.32%**
684. **`src/libraries/System.Memory/tests/Span/IndexOfAny.char.cs`** -> AI Confidence: **99.32%**
685. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/CounterGroup.cs`** -> AI Confidence: **99.32%**
686. **`src/libraries/System.Private.CoreLib/src/System/Number.Dragon4.cs`** -> AI Confidence: **99.32%**
687. **`src/libraries/System.Private.CoreLib/src/System/Reflection/Emit/TypeNameBuilder.cs`** -> AI Confidence: **99.32%**
688. **`src/libraries/System.Private.CoreLib/src/System/Text/UTF32Encoding.cs`** -> AI Confidence: **99.32%**
689. **`src/libraries/System.Private.CoreLib/src/System/Text/Unicode/TextSegmentationUtility.cs`** -> AI Confidence: **99.32%**
690. **`src/libraries/System.Private.CoreLib/src/System/Text/ValueStringBuilder.AppendFormat.cs`** -> AI Confidence: **99.32%**
691. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlWriterDelegator.cs`** -> AI Confidence: **99.32%**
692. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Test.ModuleCore/testparser.cs`** -> AI Confidence: **99.32%**
693. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/CXMLReaderAttrTest.cs`** -> AI Confidence: **99.32%**
694. **`src/libraries/System.Private.Xml/src/System/Xml/Core/HtmlEncodedRawTextWriter.cs`** -> AI Confidence: **99.32%**
695. **`src/libraries/System.Private.Xml/src/System/Xml/Core/HtmlUtf8RawTextWriter.cs`** -> AI Confidence: **99.32%**
696. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/OptimizerPatterns.cs`** -> AI Confidence: **99.32%**
697. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/TailCallAnalyzer.cs`** -> AI Confidence: **99.32%**
698. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/DecimalFormatter.cs`** -> AI Confidence: **99.32%**
699. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCCheckChars.cs`** -> AI Confidence: **99.32%**
700. **`src/libraries/System.Private.Xml/tests/XmlReaderLib/ErrorCondition.cs`** -> AI Confidence: **99.32%**
701. **`src/libraries/System.Reflection.Emit/src/System/Reflection/Emit/PseudoCustomAttributesData.cs`** -> AI Confidence: **99.32%**
702. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryObjectWriter.cs`** -> AI Confidence: **99.32%**
703. **`src/libraries/System.Runtime.Serialization.Xml/tests/Canonicalization/CryptoCanonicalization/CanonicalEncoder.cs`** -> AI Confidence: **99.32%**
704. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/CmsRecipient.cs`** -> AI Confidence: **99.32%**
705. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/CanonicalXmlElement.cs`** -> AI Confidence: **99.32%**
706. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslX509ChainEventSource.cs`** -> AI Confidence: **99.32%**
707. **`src/libraries/System.Speech/src/Internal/Synthesis/ConvertTextFrag.cs`** -> AI Confidence: **99.32%**
708. **`src/libraries/System.Text.Json/src/System/Text/Json/Reader/Utf8JsonReader.MultiSegment.cs`** -> AI Confidence: **99.32%**
709. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Bytes.cs`** -> AI Confidence: **99.32%**
710. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.DateTime.cs`** -> AI Confidence: **99.32%**
711. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.DateTimeOffset.cs`** -> AI Confidence: **99.32%**
712. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Decimal.cs`** -> AI Confidence: **99.32%**
713. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Double.cs`** -> AI Confidence: **99.32%**
714. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Float.cs`** -> AI Confidence: **99.32%**
715. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Guid.cs`** -> AI Confidence: **99.32%**
716. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.String.cs`** -> AI Confidence: **99.32%**
717. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteValues.StringSegment.cs`** -> AI Confidence: **99.32%**
718. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexInterpreter.cs`** -> AI Confidence: **99.32%**
719. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexWriter.cs`** -> AI Confidence: **99.32%**
720. **`src/libraries/System.Threading.Channels/src/System/Threading/Channels/ChannelUtilities.cs`** -> AI Confidence: **99.32%**
721. **`src/libraries/System.Transactions.Local/src/System/Transactions/TransactionScope.cs`** -> AI Confidence: **99.32%**
722. **`src/native/managed/cdac/tests/DumpTests/StackReferenceDumpTests.cs`** -> AI Confidence: **99.32%**
723. **`src/tests/JIT/Directed/ConstantFolding/value_numbering_unordered_comparisons_of_constants.cs`** -> AI Confidence: **99.32%**
724. **`src/tests/JIT/Directed/nullabletypes/isinst.cs`** -> AI Confidence: **99.32%**
725. **`src/tests/JIT/Directed/nullabletypes/isinst2.cs`** -> AI Confidence: **99.32%**
726. **`src/tests/JIT/Directed/nullabletypes/isinstboxed.cs`** -> AI Confidence: **99.32%**
727. **`src/tests/JIT/Directed/nullabletypes/isinstgenerics.cs`** -> AI Confidence: **99.32%**
728. **`src/tests/JIT/Directed/nullabletypes/isinstinterface.cs`** -> AI Confidence: **99.32%**
729. **`src/tests/JIT/Methodical/stringintern/test2.cs`** -> AI Confidence: **99.32%**
730. **`src/tests/JIT/Methodical/stringintern/test4.cs`** -> AI Confidence: **99.32%**
731. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M09.5-PDC/b25882/b25882.cs`** -> AI Confidence: **99.32%**
732. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M10/b02352/b02352.cs`** -> AI Confidence: **99.32%**
733. **`src/tests/JIT/Regression/CLR-x86-JIT/V1.2-Beta1/b210352/csharptester.cs`** -> AI Confidence: **99.32%**
734. **`src/tests/JIT/Regression/CLR-x86-JIT/v2.1/DDB/b202743/b202743.cs`** -> AI Confidence: **99.32%**
735. **`src/tests/JIT/Regression/JitBlue/GitHub_17777/GitHub_17777.cs`** -> AI Confidence: **99.32%**
736. **`src/tests/JIT/Regression/JitBlue/GitHub_9692/GitHub_9692.cs`** -> AI Confidence: **99.32%**
737. **`src/tests/JIT/Regression/JitBlue/Runtime_110958/Runtime_110985.cs`** -> AI Confidence: **99.32%**
738. **`src/tests/JIT/Regression/JitBlue/Runtime_66089/Runtime_66089.cs`** -> AI Confidence: **99.32%**
739. **`src/tests/JIT/SIMD/VectorArrayInit.cs`** -> AI Confidence: **99.32%**
740. **`src/tests/JIT/SIMD/VectorCopyToArray.cs`** -> AI Confidence: **99.32%**
741. **`src/tests/JIT/SIMD/VectorRelOp.cs`** -> AI Confidence: **99.32%**
742. **`src/tests/JIT/SIMD/VectorSet.cs`** -> AI Confidence: **99.32%**
743. **`src/tests/JIT/jit64/hfa/main/testA/hfa_testA.cs`** -> AI Confidence: **99.32%**
744. **`src/tests/JIT/jit64/hfa/main/testB/hfa_testB.cs`** -> AI Confidence: **99.32%**
745. **`src/tests/JIT/jit64/hfa/main/testC/hfa_testC.cs`** -> AI Confidence: **99.32%**
746. **`src/tests/JIT/jit64/hfa/main/testG/hfa_testG.cs`** -> AI Confidence: **99.32%**
747. **`src/tests/JIT/jit64/opt/rngchk/RngchkStress2.cs`** -> AI Confidence: **99.32%**
748. **`src/tests/JIT/opt/Compares/conditionalIncrements.cs`** -> AI Confidence: **99.32%**
749. **`src/tests/JIT/opt/Compares/conditionalSimpleOps.cs`** -> AI Confidence: **99.32%**
750. **`src/tests/Loader/binding/assemblies/assemblyversion/embedstringversions.cs`** -> AI Confidence: **99.32%**
751. **`src/tests/baseservices/compilerservices/dynamicobjectproperties/dev10_535767.cs`** -> AI Confidence: **99.32%**
752. **`src/tests/baseservices/exceptions/regressions/V1/SEH/VJ/NestedEx1.cs`** -> AI Confidence: **99.32%**
753. **`src/tests/baseservices/exceptions/regressions/V1/SEH/VJ/NestedEx2.cs`** -> AI Confidence: **99.32%**
754. **`src/tests/baseservices/exceptions/unittests/EHPatternTests.cs`** -> AI Confidence: **99.32%**
755. **`src/tests/baseservices/exceptions/unittests/StrSwitchFinally.cs`** -> AI Confidence: **99.32%**
756. **`src/tools/illink/test/Mono.Linker.Tests.Cases/DataFlow/ExceptionalDataFlow.cs`** -> AI Confidence: **99.32%**
757. **`src/native/libs/System.Native/pal_autoreleasepool.m`** -> AI Confidence: **99.32%**
758. **`src/native/libs/System.Native/pal_iossupportversion.m`** -> AI Confidence: **99.32%**
759. **`eng/common/SetupNugetSources.sh`** -> AI Confidence: **99.31%**
760. **`.github/skills/ci-pipeline-monitor/scripts/extract_failed_tests.py`** -> AI Confidence: **99.31%**
761. **`.github/skills/ci-pipeline-monitor/scripts/fetch_helix_logs.py`** -> AI Confidence: **99.31%**
762. **`eng/common/cross/install-debs.py`** -> AI Confidence: **99.31%**
763. **`src/coreclr/scripts/genEtwProvider.py`** -> AI Confidence: **99.31%**
764. **`src/coreclr/scripts/genEventingTests.py`** -> AI Confidence: **99.31%**
765. **`src/coreclr/scripts/jitrollingbuild.py`** -> AI Confidence: **99.31%**
766. **`src/coreclr/scripts/superpmi_aspnet.py`** -> AI Confidence: **99.31%**
767. **`src/coreclr/scripts/superpmi_aspnet2.py`** -> AI Confidence: **99.31%**
768. **`src/coreclr/scripts/superpmi_benchmarks.py`** -> AI Confidence: **99.31%**
769. **`src/coreclr/scripts/superpmi_diffs.py`** -> AI Confidence: **99.31%**
770. **`src/coreclr/scripts/superpmi_diffs_setup.py`** -> AI Confidence: **99.31%**
771. **`src/tests/run.py`** -> AI Confidence: **99.31%**
772. **`src/libraries/Common/tests/System/Net/EnterpriseTests/setup/apacheweb/mod_auth_ntlm_winbind/mod_auth_ntlm_winbind.c`** -> AI Confidence: **99.31%**
773. **`src/mono/mono/component/debugger-engine.c`** -> AI Confidence: **99.31%**
774. **`src/mono/mono/component/debugger-networking.c`** -> AI Confidence: **99.31%**
775. **`src/mono/mono/component/debugger-state-machine.c`** -> AI Confidence: **99.31%**
776. **`src/mono/mono/component/hot_reload.c`** -> AI Confidence: **99.31%**
777. **`src/mono/mono/component/marshal-ilgen.c`** -> AI Confidence: **99.31%**
778. **`src/mono/mono/component/mini-wasm-debugger.c`** -> AI Confidence: **99.31%**
779. **`src/mono/mono/eglib/gfile-win32.c`** -> AI Confidence: **99.31%**
780. **`src/mono/mono/eglib/giconv.c`** -> AI Confidence: **99.31%**
781. **`src/mono/mono/eglib/gmodule-aix.c`** -> AI Confidence: **99.31%**
782. **`src/mono/mono/eglib/gstr.c`** -> AI Confidence: **99.31%**
783. **`src/mono/mono/eglib/test/file.c`** -> AI Confidence: **99.31%**
784. **`src/mono/mono/eglib/test/path.c`** -> AI Confidence: **99.31%**
785. **`src/mono/mono/eventpipe/ep-rt-mono-profiler-provider.c`** -> AI Confidence: **99.31%**
786. **`src/mono/mono/eventpipe/ep-rt-mono-runtime-provider.c`** -> AI Confidence: **99.31%**
787. **`src/mono/mono/metadata/appdomain.c`** -> AI Confidence: **99.31%**
788. **`src/mono/mono/metadata/assembly-load-context.c`** -> AI Confidence: **99.31%**
789. **`src/mono/mono/metadata/class-accessors.c`** -> AI Confidence: **99.31%**
790. **`src/mono/mono/metadata/components.c`** -> AI Confidence: **99.31%**
791. **`src/mono/mono/metadata/debug-mono-ppdb.c`** -> AI Confidence: **99.31%**
792. **`src/mono/mono/metadata/dynamic-image.c`** -> AI Confidence: **99.31%**
793. **`src/mono/mono/metadata/exception.c`** -> AI Confidence: **99.31%**
794. **`src/mono/mono/metadata/gc.c`** -> AI Confidence: **99.31%**
795. **`src/mono/mono/metadata/handle.c`** -> AI Confidence: **99.31%**
796. **`src/mono/mono/metadata/image.c`** -> AI Confidence: **99.31%**
797. **`src/mono/mono/metadata/jit-info.c`** -> AI Confidence: **99.31%**
798. **`src/mono/mono/metadata/loader.c`** -> AI Confidence: **99.31%**
799. **`src/mono/mono/metadata/marshal-shared.c`** -> AI Confidence: **99.31%**
800. **`src/mono/mono/metadata/memory-manager.c`** -> AI Confidence: **99.31%**
801. **`src/mono/mono/metadata/mempool.c`** -> AI Confidence: **99.31%**
802. **`src/mono/mono/metadata/metadata.c`** -> AI Confidence: **99.31%**
803. **`src/mono/mono/metadata/method-builder-ilgen.c`** -> AI Confidence: **99.31%**
804. **`src/mono/mono/metadata/monitor.c`** -> AI Confidence: **99.31%**
805. **`src/mono/mono/metadata/mono-conc-hash.c`** -> AI Confidence: **99.31%**
806. **`src/mono/mono/metadata/mono-debug.c`** -> AI Confidence: **99.31%**
807. **`src/mono/mono/metadata/mono-hash.c`** -> AI Confidence: **99.31%**
808. **`src/mono/mono/metadata/object.c`** -> AI Confidence: **99.31%**
809. **`src/mono/mono/metadata/profiler.c`** -> AI Confidence: **99.31%**
810. **`src/mono/mono/metadata/sgen-bridge.c`** -> AI Confidence: **99.31%**
811. **`src/mono/mono/metadata/sgen-mono.c`** -> AI Confidence: **99.31%**
812. **`src/mono/mono/metadata/sgen-stw.c`** -> AI Confidence: **99.31%**
813. **`src/mono/mono/metadata/sgen-tarjan-bridge.c`** -> AI Confidence: **99.31%**
814. **`src/mono/mono/metadata/threads.c`** -> AI Confidence: **99.31%**
815. **`src/mono/mono/metadata/verify.c`** -> AI Confidence: **99.31%**
816. **`src/mono/mono/metadata/w32handle.c`** -> AI Confidence: **99.31%**
817. **`src/mono/mono/mini/aot-runtime.c`** -> AI Confidence: **99.31%**
818. **`src/mono/mono/mini/cfgdump.c`** -> AI Confidence: **99.31%**
819. **`src/mono/mono/mini/exceptions-arm.c`** -> AI Confidence: **99.31%**
820. **`src/mono/mono/mini/exceptions-arm64.c`** -> AI Confidence: **99.31%**
821. **`src/mono/mono/mini/exceptions-ppc.c`** -> AI Confidence: **99.31%**
822. **`src/mono/mono/mini/exceptions-s390x.c`** -> AI Confidence: **99.31%**
823. **`src/mono/mono/mini/image-writer.c`** -> AI Confidence: **99.31%**
824. **`src/mono/mono/mini/interp/interp-pgo.c`** -> AI Confidence: **99.31%**
825. **`src/mono/mono/mini/interp/jiterpreter.c`** -> AI Confidence: **99.31%**
826. **`src/mono/mono/mini/interp/whitebox.c`** -> AI Confidence: **99.31%**
827. **`src/mono/mono/mini/jit-icalls.c`** -> AI Confidence: **99.31%**
828. **`src/mono/mono/mini/mini-amd64-gsharedvt.c`** -> AI Confidence: **99.31%**
829. **`src/mono/mono/mini/mini-darwin.c`** -> AI Confidence: **99.31%**
830. **`src/mono/mono/mini/mini-posix.c`** -> AI Confidence: **99.31%**
831. **`src/mono/mono/mini/mini-profiler.c`** -> AI Confidence: **99.31%**
832. **`src/mono/mono/mini/mini-wasm.c`** -> AI Confidence: **99.31%**
833. **`src/mono/mono/mini/mini-windows-dlldac.c`** -> AI Confidence: **99.31%**
834. **`src/mono/mono/mini/mini-windows.c`** -> AI Confidence: **99.31%**
835. **`src/mono/mono/mini/tramp-arm.c`** -> AI Confidence: **99.31%**
836. **`src/mono/mono/profiler/browser.c`** -> AI Confidence: **99.31%**
837. **`src/mono/mono/profiler/coverage.c`** -> AI Confidence: **99.31%**
838. **`src/mono/mono/profiler/helper.c`** -> AI Confidence: **99.31%**
839. **`src/mono/mono/profiler/log.c`** -> AI Confidence: **99.31%**
840. **`src/mono/mono/profiler/vtune.c`** -> AI Confidence: **99.31%**
841. **`src/mono/mono/sgen/sgen-alloc.c`** -> AI Confidence: **99.31%**
842. **`src/mono/mono/sgen/sgen-cardtable.c`** -> AI Confidence: **99.31%**
843. **`src/mono/mono/sgen/sgen-debug.c`** -> AI Confidence: **99.31%**
844. **`src/mono/mono/sgen/sgen-descriptor.c`** -> AI Confidence: **99.31%**
845. **`src/mono/mono/sgen/sgen-fin-weak-hash.c`** -> AI Confidence: **99.31%**
846. **`src/mono/mono/sgen/sgen-internal.c`** -> AI Confidence: **99.31%**
847. **`src/mono/mono/sgen/sgen-los.c`** -> AI Confidence: **99.31%**
848. **`src/mono/mono/sgen/sgen-marksweep.c`** -> AI Confidence: **99.31%**
849. **`src/mono/mono/sgen/sgen-memory-governor.c`** -> AI Confidence: **99.31%**
850. **`src/mono/mono/sgen/sgen-protocol.c`** -> AI Confidence: **99.31%**
851. **`src/mono/mono/tests/metadata-verifier/gen-md-tests.c`** -> AI Confidence: **99.31%**
852. **`src/mono/mono/unit-tests/test-conc-hashtable.c`** -> AI Confidence: **99.31%**
853. **`src/mono/mono/unit-tests/test-mono-linked-list-set.c`** -> AI Confidence: **99.31%**
854. **`src/mono/mono/utils/checked-build.c`** -> AI Confidence: **99.31%**
855. **`src/mono/mono/utils/dlmalloc.c`** -> AI Confidence: **99.31%**
856. **`src/mono/mono/utils/hazard-pointer.c`** -> AI Confidence: **99.31%**
857. **`src/mono/mono/utils/memfuncs.c`** -> AI Confidence: **99.31%**
858. **`src/mono/mono/utils/mono-cgroup.c`** -> AI Confidence: **99.31%**
859. **`src/mono/mono/utils/mono-codeman.c`** -> AI Confidence: **99.31%**
860. **`src/mono/mono/utils/mono-context.c`** -> AI Confidence: **99.31%**
861. **`src/mono/mono/utils/mono-dl-posix.c`** -> AI Confidence: **99.31%**
862. **`src/mono/mono/utils/mono-dl-windows.c`** -> AI Confidence: **99.31%**
863. **`src/mono/mono/utils/mono-error.c`** -> AI Confidence: **99.31%**
864. **`src/mono/mono/utils/mono-log-common.c`** -> AI Confidence: **99.31%**
865. **`src/mono/mono/utils/mono-logger.c`** -> AI Confidence: **99.31%**
866. **`src/mono/mono/utils/mono-mmap-windows.c`** -> AI Confidence: **99.31%**
867. **`src/mono/mono/utils/mono-mmap.c`** -> AI Confidence: **99.31%**
868. **`src/mono/mono/utils/mono-proclib.c`** -> AI Confidence: **99.31%**
869. **`src/mono/mono/utils/mono-threads-android.c`** -> AI Confidence: **99.31%**
870. **`src/mono/mono/utils/mono-threads-coop.c`** -> AI Confidence: **99.31%**
871. **`src/mono/mono/utils/mono-threads-mach.c`** -> AI Confidence: **99.31%**
872. **`src/mono/mono/utils/mono-threads-posix.c`** -> AI Confidence: **99.31%**
873. **`src/mono/mono/utils/mono-threads.c`** -> AI Confidence: **99.31%**
874. **`src/mono/mono/utils/mono-time.c`** -> AI Confidence: **99.31%**
875. **`src/native/containers/dn-simdhash-test.c`** -> AI Confidence: **99.31%**
876. **`src/native/containers/simdhash-benchmark/benchmark.c`** -> AI Confidence: **99.31%**
877. **`src/native/eventpipe/ds-ipc-pal-socket.c`** -> AI Confidence: **99.31%**
878. **`src/native/eventpipe/ds-ipc.c`** -> AI Confidence: **99.31%**
879. **`src/native/eventpipe/ep-buffer-manager.c`** -> AI Confidence: **99.31%**
880. **`src/native/eventpipe/ep-buffer.c`** -> AI Confidence: **99.31%**
881. **`src/native/eventpipe/ep-event-instance.c`** -> AI Confidence: **99.31%**
882. **`src/native/eventpipe/ep-event-source.c`** -> AI Confidence: **99.31%**
883. **`src/native/external/brotli/c/common/shared_dictionary.c`** -> AI Confidence: **99.31%**
884. **`src/native/external/brotli/c/enc/backward_references.c`** -> AI Confidence: **99.31%**
885. **`src/native/external/brotli/c/enc/block_splitter.c`** -> AI Confidence: **99.31%**
886. **`src/native/external/brotli/c/enc/cluster.c`** -> AI Confidence: **99.31%**
887. **`src/native/external/brotli/c/enc/encode.c`** -> AI Confidence: **99.31%**
888. **`src/native/external/brotli/c/enc/encoder_dict.c`** -> AI Confidence: **99.31%**
889. **`src/native/external/libunwind/src/coredump/ucd_file_table.c`** -> AI Confidence: **99.31%**
890. **`src/native/external/libunwind/src/dwarf/Gfind_proc_info-lsb.c`** -> AI Confidence: **99.31%**
891. **`src/native/external/libunwind/src/ia64/Gtables.c`** -> AI Confidence: **99.31%**
892. **`src/native/external/libunwind/src/nto/unw_nto_create.c`** -> AI Confidence: **99.31%**
893. **`src/native/external/libunwind/src/os-freebsd.c`** -> AI Confidence: **99.31%**
894. **`src/native/external/libunwind/src/os-linux.c`** -> AI Confidence: **99.31%**
895. **`src/native/external/libunwind/src/os-qnx.c`** -> AI Confidence: **99.31%**
896. **`src/native/external/libunwind/tests/Gperf-simple.c`** -> AI Confidence: **99.31%**
897. **`src/native/external/libunwind/tests/Gperf-trace.c`** -> AI Confidence: **99.31%**
898. **`src/native/external/libunwind/tests/Gtest-dyn1.c`** -> AI Confidence: **99.31%**
899. **`src/native/external/libunwind/tests/Gtest-exc.c`** -> AI Confidence: **99.31%**
900. **`src/native/external/libunwind/tests/Ltest-init-local-signal.c`** -> AI Confidence: **99.31%**
901. **`src/native/external/libunwind/tests/Ltest-mem-validate.c`** -> AI Confidence: **99.31%**
902. **`src/native/external/libunwind/tests/test-coredump-unwind.c`** -> AI Confidence: **99.31%**
903. **`src/native/external/libunwind/tests/test-mem.c`** -> AI Confidence: **99.31%**
904. **`src/native/external/libunwind/tests/test-ptrace-misc.c`** -> AI Confidence: **99.31%**
905. **`src/native/external/libunwind/tests/x64-unwind-badjmp-signal-frame.c`** -> AI Confidence: **99.31%**
906. **`src/native/external/zlib-ng/arch/arm/arm_features.c`** -> AI Confidence: **99.31%**
907. **`src/native/external/zlib-ng/arch/riscv/riscv_features.c`** -> AI Confidence: **99.31%**
908. **`src/native/external/zlib-ng/arch/x86/adler32_avx512_vnni.c`** -> AI Confidence: **99.31%**
909. **`src/native/external/zlib-ng/arch/x86/compare256_avx2.c`** -> AI Confidence: **99.31%**
910. **`src/native/external/zstd/lib/common/fse_decompress.c`** -> AI Confidence: **99.31%**
911. **`src/native/external/zstd/lib/compress/huf_compress.c`** -> AI Confidence: **99.31%**
912. **`src/native/external/zstd/lib/compress/zstd_compress.c`** -> AI Confidence: **99.31%**
913. **`src/native/external/zstd/lib/compress/zstdmt_compress.c`** -> AI Confidence: **99.31%**
914. **`src/native/external/zstd/lib/decompress/huf_decompress.c`** -> AI Confidence: **99.31%**
915. **`src/native/external/zstd/lib/decompress/zstd_decompress.c`** -> AI Confidence: **99.31%**
916. **`src/native/external/zstd/lib/decompress/zstd_decompress_block.c`** -> AI Confidence: **99.31%**
917. **`src/native/external/zstd/lib/dictBuilder/cover.c`** -> AI Confidence: **99.31%**
918. **`src/native/external/zstd/lib/dictBuilder/fastcover.c`** -> AI Confidence: **99.31%**
919. **`src/native/external/zstd/lib/dictBuilder/zdict.c`** -> AI Confidence: **99.31%**
920. **`src/native/external/zstd/lib/legacy/zstd_v01.c`** -> AI Confidence: **99.31%**
921. **`src/native/external/zstd/lib/legacy/zstd_v02.c`** -> AI Confidence: **99.31%**
922. **`src/native/external/zstd/lib/legacy/zstd_v03.c`** -> AI Confidence: **99.31%**
923. **`src/native/external/zstd/lib/legacy/zstd_v05.c`** -> AI Confidence: **99.31%**
924. **`src/native/external/zstd/lib/legacy/zstd_v06.c`** -> AI Confidence: **99.31%**
925. **`src/native/libs/System.Globalization.Native/pal_calendarData.c`** -> AI Confidence: **99.31%**
926. **`src/native/libs/System.Globalization.Native/pal_collation.c`** -> AI Confidence: **99.31%**
927. **`src/native/libs/System.Globalization.Native/pal_icushim.c`** -> AI Confidence: **99.31%**
928. **`src/native/libs/System.Globalization.Native/pal_icushim_static.c`** -> AI Confidence: **99.31%**
929. **`src/native/libs/System.Globalization.Native/pal_locale.c`** -> AI Confidence: **99.31%**
930. **`src/native/libs/System.IO.Compression.Native/entrypoints.c`** -> AI Confidence: **99.31%**
931. **`src/native/libs/System.IO.Ports.Native/pal_termios.c`** -> AI Confidence: **99.31%**
932. **`src/native/libs/System.Native/pal_datetime_time_zone_data.c`** -> AI Confidence: **99.31%**
933. **`src/native/libs/System.Native/pal_interfaceaddresses.c`** -> AI Confidence: **99.31%**
934. **`src/native/libs/System.Native/pal_io.c`** -> AI Confidence: **99.31%**
935. **`src/native/libs/System.Native/pal_maphardwaretype.c`** -> AI Confidence: **99.31%**
936. **`src/native/libs/System.Native/pal_mount.c`** -> AI Confidence: **99.31%**
937. **`src/native/libs/System.Native/pal_networkchange.c`** -> AI Confidence: **99.31%**
938. **`src/native/libs/System.Native/pal_networking.c`** -> AI Confidence: **99.31%**
939. **`src/native/libs/System.Native/pal_process.c`** -> AI Confidence: **99.31%**
940. **`src/native/libs/System.Native/pal_time.c`** -> AI Confidence: **99.31%**
941. **`src/native/libs/System.Native/pal_uid.c`** -> AI Confidence: **99.31%**
942. **`src/native/libs/System.Net.Security.Native/pal_gssapi.c`** -> AI Confidence: **99.31%**
943. **`src/native/libs/System.Security.Cryptography.Native.Android/pal_x509.c`** -> AI Confidence: **99.31%**
944. **`src/native/libs/System.Security.Cryptography.Native.Android/pal_x509store.c`** -> AI Confidence: **99.31%**
945. **`src/native/libs/System.Security.Cryptography.Native/openssl.c`** -> AI Confidence: **99.31%**
946. **`src/native/libs/System.Security.Cryptography.Native/pal_ssl.c`** -> AI Confidence: **99.31%**
947. **`src/native/libs/System.Security.Cryptography.Native/pal_x509.c`** -> AI Confidence: **99.31%**
948. **`src/native/minipal/cpufeatures.c`** -> AI Confidence: **99.31%**
949. **`src/native/minipal/log.c`** -> AI Confidence: **99.31%**
950. **`src/native/minipal/memorybarrierprocesswide.c`** -> AI Confidence: **99.31%**
951. **`src/tasks/LibraryBuilder/Templates/autoinit.c`** -> AI Confidence: **99.31%**
952. **`src/tests/Interop/MonoAPI/Native/mono-embedding-api-test/mono-embedding-api-test.c`** -> AI Confidence: **99.31%**
953. **`src/coreclr/dlls/mscoree/exports.cpp`** -> AI Confidence: **99.31%**
954. **`src/coreclr/gc/sample/gcenv.h`** -> AI Confidence: **99.31%**
955. **`src/coreclr/gc/unix/cgroup.cpp`** -> AI Confidence: **99.31%**
956. **`src/coreclr/gc/unix/events.cpp`** -> AI Confidence: **99.31%**
957. **`src/coreclr/gc/unix/gcenv.unix.cpp`** -> AI Confidence: **99.31%**
958. **`src/coreclr/gc/unix/numasupport.cpp`** -> AI Confidence: **99.31%**
959. **`src/coreclr/gc/windows/gcenv.windows.cpp`** -> AI Confidence: **99.31%**
960. **`src/coreclr/hosts/corerun/corerun.cpp`** -> AI Confidence: **99.31%**
961. **`src/coreclr/interpreter/eeinterp.cpp`** -> AI Confidence: **99.31%**
962. **`src/coreclr/jit/simdcodegenxarch.cpp`** -> AI Confidence: **99.31%**
963. **`src/coreclr/md/enc/stgtiggerstorage.cpp`** -> AI Confidence: **99.31%**
964. **`src/coreclr/md/runtime/mdinternaldisp.cpp`** -> AI Confidence: **99.31%**
965. **`src/coreclr/md/runtime/stgpool.cpp`** -> AI Confidence: **99.31%**
966. **`src/coreclr/minipal/Unix/doublemapping.cpp`** -> AI Confidence: **99.31%**
967. **`src/coreclr/nativeaot/Runtime/AsmOffsetsVerify.cpp`** -> AI Confidence: **99.31%**
968. **`src/coreclr/nativeaot/Runtime/Crst.cpp`** -> AI Confidence: **99.31%**
969. **`src/coreclr/nativeaot/Runtime/FinalizerHelpers.cpp`** -> AI Confidence: **99.31%**
970. **`src/coreclr/nativeaot/Runtime/GcEnum.cpp`** -> AI Confidence: **99.31%**
971. **`src/coreclr/nativeaot/Runtime/GcStressControl.cpp`** -> AI Confidence: **99.31%**
972. **`src/coreclr/nativeaot/Runtime/RestrictedCallouts.cpp`** -> AI Confidence: **99.31%**
973. **`src/coreclr/nativeaot/Runtime/RhConfig.cpp`** -> AI Confidence: **99.31%**
974. **`src/coreclr/nativeaot/Runtime/StackFrameIterator.cpp`** -> AI Confidence: **99.31%**
975. **`src/coreclr/nativeaot/Runtime/clrgc.enabled.cpp`** -> AI Confidence: **99.31%**
976. **`src/coreclr/nativeaot/Runtime/eventpipe/ds-rt-aot.cpp`** -> AI Confidence: **99.31%**
977. **`src/coreclr/nativeaot/Runtime/eventpipe/ds-rt-aot.h`** -> AI Confidence: **99.31%**
978. **`src/coreclr/nativeaot/Runtime/eventpipeinternal.cpp`** -> AI Confidence: **99.31%**
979. **`src/coreclr/nativeaot/Runtime/eventtrace_bulktype.cpp`** -> AI Confidence: **99.31%**
980. **`src/coreclr/nativeaot/Runtime/eventtrace_gcheap.cpp`** -> AI Confidence: **99.31%**
981. **`src/coreclr/nativeaot/Runtime/startup.cpp`** -> AI Confidence: **99.31%**
982. **`src/coreclr/nativeaot/Runtime/stressLog.cpp`** -> AI Confidence: **99.31%**
983. **`src/coreclr/nativeaot/Runtime/thread.cpp`** -> AI Confidence: **99.31%**
984. **`src/coreclr/nativeaot/Runtime/threadstore.cpp`** -> AI Confidence: **99.31%**
985. **`src/coreclr/nativeaot/Runtime/unix/PalUnix.cpp`** -> AI Confidence: **99.31%**
986. **`src/coreclr/nativeaot/Runtime/unix/UnwindHelpers.cpp`** -> AI Confidence: **99.31%**
987. **`src/coreclr/nativeaot/Runtime/windows/PalCommon.cpp`** -> AI Confidence: **99.31%**
988. **`src/coreclr/pal/src/eventprovider/lttngprovider/eventproviderhelpers.cpp`** -> AI Confidence: **99.31%**
989. **`src/coreclr/pal/src/exception/machexception.cpp`** -> AI Confidence: **99.31%**
990. **`src/coreclr/pal/src/exception/remote-unwind.cpp`** -> AI Confidence: **99.31%**
991. **`src/coreclr/pal/src/init/pal.cpp`** -> AI Confidence: **99.31%**
992. **`src/coreclr/pal/src/init/sxs.cpp`** -> AI Confidence: **99.31%**
993. **`src/coreclr/pal/src/map/virtual.cpp`** -> AI Confidence: **99.31%**
994. **`src/coreclr/pal/src/misc/perfjitdump.cpp`** -> AI Confidence: **99.31%**
995. **`src/coreclr/pal/src/misc/time.cpp`** -> AI Confidence: **99.31%**
996. **`src/coreclr/pal/src/misc/tracepointprovider.cpp`** -> AI Confidence: **99.31%**
997. **`src/coreclr/pal/src/misc/utils.cpp`** -> AI Confidence: **99.31%**
998. **`src/coreclr/tools/superpmi/mcs/verbasmdump.cpp`** -> AI Confidence: **99.31%**
999. **`src/coreclr/tools/superpmi/mcs/verbfracture.cpp`** -> AI Confidence: **99.31%**
1000. **`src/coreclr/tools/superpmi/mcs/verbstrip.cpp`** -> AI Confidence: **99.31%**
1001. **`src/coreclr/tools/superpmi/superpmi-shared/methodcontextreader.cpp`** -> AI Confidence: **99.31%**
1002. **`src/coreclr/tools/superpmi/superpmi-shared/spmiutil.cpp`** -> AI Confidence: **99.31%**
1003. **`src/coreclr/tools/superpmi/superpmi-shim-collector/superpmi-shim-collector.cpp`** -> AI Confidence: **99.31%**
1004. **`src/coreclr/utilcode/cycletimer.cpp`** -> AI Confidence: **99.31%**
1005. **`src/coreclr/utilcode/debug.cpp`** -> AI Confidence: **99.31%**
1006. **`src/coreclr/utilcode/stresslog.cpp`** -> AI Confidence: **99.31%**
1007. **`src/coreclr/vm/amd64/cgenamd64.cpp`** -> AI Confidence: **99.31%**
1008. **`src/coreclr/vm/appdomain.cpp`** -> AI Confidence: **99.31%**
1009. **`src/coreclr/vm/arm/stubs.cpp`** -> AI Confidence: **99.31%**
1010. **`src/coreclr/vm/assemblynative.cpp`** -> AI Confidence: **99.31%**
1011. **`src/coreclr/vm/ceeload.cpp`** -> AI Confidence: **99.31%**
1012. **`src/coreclr/vm/ceemain.cpp`** -> AI Confidence: **99.31%**
1013. **`src/coreclr/vm/clrex.cpp`** -> AI Confidence: **99.31%**
1014. **`src/coreclr/vm/clrtocomcall.cpp`** -> AI Confidence: **99.31%**
1015. **`src/coreclr/vm/codeman.cpp`** -> AI Confidence: **99.31%**
1016. **`src/coreclr/vm/codeversion.cpp`** -> AI Confidence: **99.31%**
1017. **`src/coreclr/vm/comdynamic.cpp`** -> AI Confidence: **99.31%**
1018. **`src/coreclr/vm/comsynchronizable.cpp`** -> AI Confidence: **99.31%**
1019. **`src/coreclr/vm/comutilnative.cpp`** -> AI Confidence: **99.31%**
1020. **`src/coreclr/vm/corhost.cpp`** -> AI Confidence: **99.31%**
1021. **`src/coreclr/vm/dllimportcallback.cpp`** -> AI Confidence: **99.31%**
1022. **`src/coreclr/vm/dwreport.cpp`** -> AI Confidence: **99.31%**
1023. **`src/coreclr/vm/dynamicmethod.cpp`** -> AI Confidence: **99.31%**
1024. **`src/coreclr/vm/encee.cpp`** -> AI Confidence: **99.31%**
1025. **`src/coreclr/vm/eventtrace_gcheap.cpp`** -> AI Confidence: **99.31%**
1026. **`src/coreclr/vm/fcall.cpp`** -> AI Confidence: **99.31%**
1027. **`src/coreclr/vm/fieldmarshaler.cpp`** -> AI Confidence: **99.31%**
1028. **`src/coreclr/vm/frames.cpp`** -> AI Confidence: **99.31%**
1029. **`src/coreclr/vm/gcheaputilities.cpp`** -> AI Confidence: **99.31%**
1030. **`src/coreclr/vm/i386/cgenx86.cpp`** -> AI Confidence: **99.31%**
1031. **`src/coreclr/vm/i386/excepx86.cpp`** -> AI Confidence: **99.31%**
1032. **`src/coreclr/vm/i386/jitinterfacex86.cpp`** -> AI Confidence: **99.31%**
1033. **`src/coreclr/vm/ilmarshalers.cpp`** -> AI Confidence: **99.31%**
1034. **`src/coreclr/vm/instmethhash.cpp`** -> AI Confidence: **99.31%**
1035. **`src/coreclr/vm/interoputil.cpp`** -> AI Confidence: **99.31%**
1036. **`src/coreclr/vm/interpexec.cpp`** -> AI Confidence: **99.31%**
1037. **`src/coreclr/vm/jithelpers.cpp`** -> AI Confidence: **99.31%**
1038. **`src/coreclr/vm/loaderallocator.cpp`** -> AI Confidence: **99.31%**
1039. **`src/coreclr/vm/loongarch64/stubs.cpp`** -> AI Confidence: **99.31%**
1040. **`src/coreclr/vm/marshalnative.cpp`** -> AI Confidence: **99.31%**
1041. **`src/coreclr/vm/method.cpp`** -> AI Confidence: **99.31%**
1042. **`src/coreclr/vm/multicorejit.cpp`** -> AI Confidence: **99.31%**
1043. **`src/coreclr/vm/multicorejitplayer.cpp`** -> AI Confidence: **99.31%**
1044. **`src/coreclr/vm/object.cpp`** -> AI Confidence: **99.31%**
1045. **`src/coreclr/vm/peassembly.cpp`** -> AI Confidence: **99.31%**
1046. **`src/coreclr/vm/proftoeeinterfaceimpl.cpp`** -> AI Confidence: **99.31%**
1047. **`src/coreclr/vm/readytoruninfo.cpp`** -> AI Confidence: **99.31%**
1048. **`src/coreclr/vm/rejit.cpp`** -> AI Confidence: **99.31%**
1049. **`src/coreclr/vm/riscv64/stubs.cpp`** -> AI Confidence: **99.31%**
1050. **`src/coreclr/vm/runtimehandles.cpp`** -> AI Confidence: **99.31%**
1051. **`src/coreclr/vm/stdinterfaces.cpp`** -> AI Confidence: **99.31%**
1052. **`src/coreclr/vm/stubgen.cpp`** -> AI Confidence: **99.31%**
1053. **`src/coreclr/vm/stubmgr.cpp`** -> AI Confidence: **99.31%**
1054. **`src/coreclr/vm/syncblk.cpp`** -> AI Confidence: **99.31%**
1055. **`src/coreclr/vm/tailcallhelp.cpp`** -> AI Confidence: **99.31%**
1056. **`src/coreclr/vm/threads.cpp`** -> AI Confidence: **99.31%**
1057. **`src/coreclr/vm/typehandle.cpp`** -> AI Confidence: **99.31%**
1058. **`src/coreclr/vm/typehash.cpp`** -> AI Confidence: **99.31%**
1059. **`src/coreclr/vm/virtualcallstub.cpp`** -> AI Confidence: **99.31%**
1060. **`src/coreclr/vm/writebarriermanager.cpp`** -> AI Confidence: **99.31%**
1061. **`src/mono/mono/metadata/reflection-cache.h`** -> AI Confidence: **99.31%**
1062. **`src/native/corehost/apphost/apphost.windows.cpp`** -> AI Confidence: **99.31%**
1063. **`src/native/corehost/comhost/comhost.cpp`** -> AI Confidence: **99.31%**
1064. **`src/native/corehost/corehost.cpp`** -> AI Confidence: **99.31%**
1065. **`src/native/corehost/fxr/command_line.cpp`** -> AI Confidence: **99.31%**
1066. **`src/native/corehost/fxr/fx_muxer.cpp`** -> AI Confidence: **99.31%**
1067. **`src/native/corehost/fxr/hostfxr.cpp`** -> AI Confidence: **99.31%**
1068. **`src/native/corehost/hostmisc/pal.unix.cpp`** -> AI Confidence: **99.31%**
1069. **`src/native/corehost/hostpolicy/deps_format.cpp`** -> AI Confidence: **99.31%**
1070. **`src/native/corehost/hostpolicy/hostpolicy.cpp`** -> AI Confidence: **99.31%**
1071. **`src/native/corehost/hostpolicy/hostpolicy_context.cpp`** -> AI Confidence: **99.31%**
1072. **`src/native/corehost/ijwhost/ijwhost.cpp`** -> AI Confidence: **99.31%**
1073. **`src/native/corehost/ijwhost/ijwthunk.cpp`** -> AI Confidence: **99.31%**
1074. **`src/native/corehost/runtime_config.cpp`** -> AI Confidence: **99.31%**
1075. **`src/native/corehost/test/nativehost/host_context_test.cpp`** -> AI Confidence: **99.31%**
1076. **`src/native/external/zstd/lib/legacy/zstd_legacy.h`** -> AI Confidence: **99.31%**
1077. **`src/native/watchdog/watchdog.cpp`** -> AI Confidence: **99.31%**
1078. **`src/tests/Interop/COM/RuntimeAsync/RuntimeAsyncNative.cpp`** -> AI Confidence: **99.31%**
1079. **`src/tests/Interop/IJW/NativeVarargs/IjwNativeVarargs.cpp`** -> AI Confidence: **99.31%**
1080. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128B.cpp`** -> AI Confidence: **99.31%**
1081. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128C.cpp`** -> AI Confidence: **99.31%**
1082. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128D.cpp`** -> AI Confidence: **99.31%**
1083. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128F.cpp`** -> AI Confidence: **99.31%**
1084. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128L.cpp`** -> AI Confidence: **99.31%**
1085. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector128U.cpp`** -> AI Confidence: **99.31%**
1086. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64B.cpp`** -> AI Confidence: **99.31%**
1087. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64C.cpp`** -> AI Confidence: **99.31%**
1088. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64D.cpp`** -> AI Confidence: **99.31%**
1089. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64F.cpp`** -> AI Confidence: **99.31%**
1090. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64L.cpp`** -> AI Confidence: **99.31%**
1091. **`src/tests/Interop/PInvoke/Generics/GenericsNative.Vector64U.cpp`** -> AI Confidence: **99.31%**
1092. **`src/coreclr/System.Private.CoreLib/src/System/Exception.CoreCLR.cs`** -> AI Confidence: **99.31%**
1093. **`src/coreclr/System.Private.CoreLib/src/System/GC.CoreCLR.cs`** -> AI Confidence: **99.31%**
1094. **`src/coreclr/System.Private.CoreLib/src/System/MulticastDelegate.CoreCLR.cs`** -> AI Confidence: **99.31%**
1095. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeMethodBuilder.cs`** -> AI Confidence: **99.31%**
1096. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/RuntimeCustomAttributeData.cs`** -> AI Confidence: **99.31%**
1097. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/TypeNameResolver.CoreCLR.cs`** -> AI Confidence: **99.31%**
1098. **`src/coreclr/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncHelpers.CoreCLR.cs`** -> AI Confidence: **99.31%**
1099. **`src/coreclr/System.Private.CoreLib/src/System/Runtime/InteropServices/Marshal.CoreCLR.cs`** -> AI Confidence: **99.31%**
1100. **`src/coreclr/System.Private.CoreLib/src/System/RuntimeType.CoreCLR.cs`** -> AI Confidence: **99.31%**
1101. **`src/coreclr/System.Private.CoreLib/src/System/Threading/Thread.CoreCLR.cs`** -> AI Confidence: **99.31%**
1102. **`src/coreclr/System.Private.CoreLib/src/System/Variant.cs`** -> AI Confidence: **99.31%**
1103. **`src/coreclr/System.Private.CoreLib/src/System/__ComObject.cs`** -> AI Confidence: **99.31%**
1104. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Core/Execution/ExecutionDomain.cs`** -> AI Confidence: **99.31%**
1105. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Extensions/NonPortable/CustomAttributeInstantiator.cs`** -> AI Confidence: **99.31%**
1106. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Extensions/NonPortable/CustomAttributeSearcher.cs`** -> AI Confidence: **99.31%**
1107. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/ActivatorImplementation.cs`** -> AI Confidence: **99.31%**
1108. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Array.NativeAot.cs`** -> AI Confidence: **99.31%**
1109. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Delegate.cs`** -> AI Confidence: **99.31%**
1110. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/CustomAttributes/NativeFormat/NativeFormatCustomAttributeData.cs`** -> AI Confidence: **99.31%**
1111. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/General/MetadataReaderExtensions.NativeFormat.cs`** -> AI Confidence: **99.31%**
1112. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/TypeInfos/NativeFormat/NativeFormatRuntimeTypeInfo.CoreGetDeclared.cs`** -> AI Confidence: **99.31%**
1113. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/TypeInfos/RuntimeTypeInfo.cs`** -> AI Confidence: **99.31%**
1114. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/CompilerServices/ClassConstructorRunner.cs`** -> AI Confidence: **99.31%**
1115. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/InteropServices/Marshal.NativeAot.cs`** -> AI Confidence: **99.31%**
1116. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/InteropServices/PInvokeMarshal.cs`** -> AI Confidence: **99.31%**
1117. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/RuntimeExceptionHelpers.cs`** -> AI Confidence: **99.31%**
1118. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Threading/Thread.NativeAot.cs`** -> AI Confidence: **99.31%**
1119. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/GenericDictionaryCell.cs`** -> AI Confidence: **99.31%**
1120. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeBuilder.cs`** -> AI Confidence: **99.31%**
1121. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.FieldAccess.cs`** -> AI Confidence: **99.31%**
1122. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.GVMResolution.cs`** -> AI Confidence: **99.31%**
1123. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.Metadata.cs`** -> AI Confidence: **99.31%**
1124. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/TypeSystem/TypeDesc.Runtime.cs`** -> AI Confidence: **99.31%**
1125. **`src/coreclr/tools/Common/CommandLineHelpers.cs`** -> AI Confidence: **99.31%**
1126. **`src/coreclr/tools/Common/Compiler/GenericCycleDetection/GraphBuilder.cs`** -> AI Confidence: **99.31%**
1127. **`src/coreclr/tools/Common/Compiler/GenericCycleDetection/ModuleCycleInfo.cs`** -> AI Confidence: **99.31%**
1128. **`src/coreclr/tools/Common/Compiler/NativeAotNameMangler.cs`** -> AI Confidence: **99.31%**
1129. **`src/coreclr/tools/Common/Compiler/ObjectWriter/ElfObjectWriter.cs`** -> AI Confidence: **99.31%**
1130. **`src/coreclr/tools/Common/Compiler/ObjectWriter/ObjectWriter.cs`** -> AI Confidence: **99.31%**
1131. **`src/coreclr/tools/Common/Compiler/ObjectWriter/PEObjectWriter.cs`** -> AI Confidence: **99.31%**
1132. **`src/coreclr/tools/Common/Compiler/ObjectWriter/StringTableBuilder.cs`** -> AI Confidence: **99.31%**
1133. **`src/coreclr/tools/Common/Compiler/ObjectWriter/WasmObjectWriter.cs`** -> AI Confidence: **99.31%**
1134. **`src/coreclr/tools/Common/Compiler/TypeMapMetadata.cs`** -> AI Confidence: **99.31%**
1135. **`src/coreclr/tools/Common/Compiler/Win32Resources/ResourceData.cs`** -> AI Confidence: **99.31%**
1136. **`src/coreclr/tools/Common/InstructionSetHelpers.cs`** -> AI Confidence: **99.31%**
1137. **`src/coreclr/tools/Common/Internal/NativeFormat/NativeFormatWriter.cs`** -> AI Confidence: **99.31%**
1138. **`src/coreclr/tools/Common/JitInterface/CorInfoImpl.cs`** -> AI Confidence: **99.31%**
1139. **`src/coreclr/tools/Common/JitInterface/ThunkGenerator/InstructionSetGenerator.cs`** -> AI Confidence: **99.31%**
1140. **`src/coreclr/tools/Common/JitInterface/ThunkGenerator/Program.cs`** -> AI Confidence: **99.31%**
1141. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaMethod.cs`** -> AI Confidence: **99.31%**
1142. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaModule.cs`** -> AI Confidence: **99.31%**
1143. **`src/coreclr/tools/Common/TypeSystem/IL/FlowGraph.cs`** -> AI Confidence: **99.31%**
1144. **`src/coreclr/tools/Common/TypeSystem/IL/Stubs/StructMarshallingThunk.cs`** -> AI Confidence: **99.31%**
1145. **`src/coreclr/tools/Common/TypeSystem/IL/UnsafeAccessors.cs`** -> AI Confidence: **99.31%**
1146. **`src/coreclr/tools/Common/TypeSystem/Interop/UnmanagedCallingConventions.cs`** -> AI Confidence: **99.31%**
1147. **`src/coreclr/tools/Common/TypeSystem/MetadataEmitter/TypeSystemMetadataEmitter.cs`** -> AI Confidence: **99.31%**
1148. **`src/coreclr/tools/ILTrim.Core/DependencyAnalysis/TokenBased/MethodDefinitionNode.cs`** -> AI Confidence: **99.31%**
1149. **`src/coreclr/tools/ILVerification/AccessVerificationHelpers.cs`** -> AI Confidence: **99.31%**
1150. **`src/coreclr/tools/ILVerification/TypeVerifier.cs`** -> AI Confidence: **99.31%**
1151. **`src/coreclr/tools/ILVerification/Verifier.cs`** -> AI Confidence: **99.31%**
1152. **`src/coreclr/tools/ILVerify/Program.cs`** -> AI Confidence: **99.31%**
1153. **`src/coreclr/tools/aot/DependencyGraphViewer/Program.cs`** -> AI Confidence: **99.31%**
1154. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/BodySubstitutionParser.cs`** -> AI Confidence: **99.31%**
1155. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/CompilerTypeSystemContext.Aot.cs`** -> AI Confidence: **99.31%**
1156. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/CompilerGeneratedState.cs`** -> AI Confidence: **99.31%**
1157. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/FlowAnnotations.cs`** -> AI Confidence: **99.31%**
1158. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/HandleCallAction.cs`** -> AI Confidence: **99.31%**
1159. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/MethodBodyScanner.cs`** -> AI Confidence: **99.31%**
1160. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/ReflectionMarker.cs`** -> AI Confidence: **99.31%**
1161. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/DynamicDependencyAttributesOnEntityNode.cs`** -> AI Confidence: **99.31%**
1162. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/EETypeNode.cs`** -> AI Confidence: **99.31%**
1163. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/ReadyToRunGenericHelperNode.cs`** -> AI Confidence: **99.31%**
1164. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DescriptorMarker.cs`** -> AI Confidence: **99.31%**
1165. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ILScanner.cs`** -> AI Confidence: **99.31%**
1166. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Logging/DocumentationSignatureParser.cs`** -> AI Confidence: **99.31%**
1167. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Logging/UnconditionalSuppressMessageAttributeState.cs`** -> AI Confidence: **99.31%**
1168. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/CoffObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1169. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/Dwarf/DwarfBuilder.cs`** -> AI Confidence: **99.31%**
1170. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/Dwarf/DwarfInfo.cs`** -> AI Confidence: **99.31%**
1171. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/ElfObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1172. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/MachObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1173. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/ObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1174. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/ObjectWriter/UnixObjectWriter.Aot.cs`** -> AI Confidence: **99.31%**
1175. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/SourceLinkWriter.cs`** -> AI Confidence: **99.31%**
1176. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/SubstitutedILProvider.cs`** -> AI Confidence: **99.31%**
1177. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/TypePreinit.cs`** -> AI Confidence: **99.31%**
1178. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/UsageBasedMetadataManager.cs`** -> AI Confidence: **99.31%**
1179. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/UserDefinedTypeDescriptor.cs`** -> AI Confidence: **99.31%**
1180. **`src/coreclr/tools/aot/ILCompiler.Diagnostics/PdbWriter.cs`** -> AI Confidence: **99.31%**
1181. **`src/coreclr/tools/aot/ILCompiler.MetadataTransform/ILCompiler/Metadata/Transform.Type.cs`** -> AI Confidence: **99.31%**
1182. **`src/coreclr/tools/aot/ILCompiler.MetadataTransform/Internal/Metadata/NativeFormat/Writer/MdBinaryWriterGen.cs`** -> AI Confidence: **99.31%**
1183. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/CallChainProfile.cs`** -> AI Confidence: **99.31%**
1184. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/ArgIterator.cs`** -> AI Confidence: **99.31%**
1185. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/AttributePresenceFilterNode.cs`** -> AI Confidence: **99.31%**
1186. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/GenericLookupSignature.cs`** -> AI Confidence: **99.31%**
1187. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/InliningInfoNode.cs`** -> AI Confidence: **99.31%**
1188. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/InstrumentationDataTableNode.cs`** -> AI Confidence: **99.31%**
1189. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/ManifestMetadataTableNode.cs`** -> AI Confidence: **99.31%**
1190. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/MethodFixupSignature.cs`** -> AI Confidence: **99.31%**
1191. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/SignatureBuilder.cs`** -> AI Confidence: **99.31%**
1192. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/TypeFixupSignature.cs`** -> AI Confidence: **99.31%**
1193. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/TypeGenericInfoMapNode.cs`** -> AI Confidence: **99.31%**
1194. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/TypeValidationChecker.cs`** -> AI Confidence: **99.31%**
1195. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/WasmImportThunk.cs`** -> AI Confidence: **99.31%**
1196. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/FileLayoutOptimizer.cs`** -> AI Confidence: **99.31%**
1197. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ProfileDataManager.cs`** -> AI Confidence: **99.31%**
1198. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunCodegenCompilation.cs`** -> AI Confidence: **99.31%**
1199. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunMetadataFieldLayoutAlgorithm.cs`** -> AI Confidence: **99.31%**
1200. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunProfilingRootProvider.cs`** -> AI Confidence: **99.31%**
1201. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/IL/ReadyToRunILProvider.cs`** -> AI Confidence: **99.31%**
1202. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/EHInfo.cs`** -> AI Confidence: **99.31%**
1203. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/MachO/MachOImageReader.cs`** -> AI Confidence: **99.31%**
1204. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/ReadyToRunMethod.cs`** -> AI Confidence: **99.31%**
1205. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/ReadyToRunReader.cs`** -> AI Confidence: **99.31%**
1206. **`src/coreclr/tools/aot/ILCompiler.RyuJit/JitInterface/CorInfoImpl.RyuJit.cs`** -> AI Confidence: **99.31%**
1207. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/ResultChecker.cs`** -> AI Confidence: **99.31%**
1208. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/TrimmingDriver.cs`** -> AI Confidence: **99.31%**
1209. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/Tests/DocumentationSignatureParserTests.cs`** -> AI Confidence: **99.31%**
1210. **`src/coreclr/tools/aot/ILCompiler/ILCompilerRootCommand.cs`** -> AI Confidence: **99.31%**
1211. **`src/coreclr/tools/aot/ILCompiler/RdXmlRootProvider.cs`** -> AI Confidence: **99.31%**
1212. **`src/coreclr/tools/aot/crossgen2/Program.cs`** -> AI Confidence: **99.31%**
1213. **`src/coreclr/tools/dotnet-pgo/Program.cs`** -> AI Confidence: **99.31%**
1214. **`src/coreclr/tools/dotnet-pgo/R2RSignatureTypeProvider.cs`** -> AI Confidence: **99.31%**
1215. **`src/coreclr/tools/dotnet-pgo/SPGO/SampleCorrelator.cs`** -> AI Confidence: **99.31%**
1216. **`src/coreclr/tools/dotnet-pgo/TraceRuntimeDescToTypeSystemDesc.cs`** -> AI Confidence: **99.31%**
1217. **`src/coreclr/tools/r2rdump/CoreDisTools.cs`** -> AI Confidence: **99.31%**
1218. **`src/coreclr/tools/r2rdump/Program.cs`** -> AI Confidence: **99.31%**
1219. **`src/coreclr/tools/r2rdump/R2RDiff.cs`** -> AI Confidence: **99.31%**
1220. **`src/coreclr/tools/r2rdump/TextDumper.cs`** -> AI Confidence: **99.31%**
1221. **`src/coreclr/tools/r2rtest/Commands/CompileSubtreeCommand.cs`** -> AI Confidence: **99.31%**
1222. **`src/coreclr/tools/r2rtest/ParallelRunner.cs`** -> AI Confidence: **99.31%**
1223. **`src/coreclr/tools/r2rtest/ProcessRunner.cs`** -> AI Confidence: **99.31%**
1224. **`src/installer/managed/Microsoft.NET.HostModel/AppHost/HostWriter.cs`** -> AI Confidence: **99.31%**
1225. **`src/installer/managed/Microsoft.NET.HostModel/Bundle/Bundler.cs`** -> AI Confidence: **99.31%**
1226. **`src/installer/managed/Microsoft.NET.HostModel/Bundle/Manifest.cs`** -> AI Confidence: **99.31%**
1227. **`src/libraries/Common/src/Internal/Cryptography/PkcsHelpers.cs`** -> AI Confidence: **99.31%**
1228. **`src/libraries/Common/src/Interop/Linux/procfs/Interop.ProcFsStat.ParseMapModules.cs`** -> AI Confidence: **99.31%**
1229. **`src/libraries/Common/src/Interop/Linux/procfs/Interop.ProcFsStat.TryReadStatusFile.cs`** -> AI Confidence: **99.31%**
1230. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.Keychain.macOS.cs`** -> AI Confidence: **99.31%**
1231. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.Ssl.cs`** -> AI Confidence: **99.31%**
1232. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.X509.iOS.cs`** -> AI Confidence: **99.31%**
1233. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.X509.macOS.cs`** -> AI Confidence: **99.31%**
1234. **`src/libraries/Common/src/Interop/Unix/System.Native/Interop.ForkAndExecProcess.cs`** -> AI Confidence: **99.31%**
1235. **`src/libraries/Common/src/Interop/Unix/System.Security.Cryptography.Native/Interop.OpenSsl.cs`** -> AI Confidence: **99.31%**
1236. **`src/libraries/Common/src/System/HexConverter.cs`** -> AI Confidence: **99.31%**
1237. **`src/libraries/Common/src/System/IO/FileSystem.Attributes.Windows.cs`** -> AI Confidence: **99.31%**
1238. **`src/libraries/Common/src/System/Security/Cryptography/CompositeMLDsaManaged.ECDsa.cs`** -> AI Confidence: **99.31%**
1239. **`src/libraries/Common/src/System/Security/Cryptography/Helpers.cs`** -> AI Confidence: **99.31%**
1240. **`src/libraries/Common/src/System/Security/Cryptography/MLKemCng.Windows.cs`** -> AI Confidence: **99.31%**
1241. **`src/libraries/Common/src/System/Security/Cryptography/PasswordBasedEncryption.cs`** -> AI Confidence: **99.31%**
1242. **`src/libraries/Common/src/System/Security/Cryptography/Pkcs/Pkcs12SafeContents.cs`** -> AI Confidence: **99.31%**
1243. **`src/libraries/Common/src/System/Security/Cryptography/PqcBlobHelpers.cs`** -> AI Confidence: **99.31%**
1244. **`src/libraries/Common/src/System/Security/Cryptography/RSAAndroid.cs`** -> AI Confidence: **99.31%**
1245. **`src/libraries/Common/src/System/Security/Cryptography/RSAAppleCrypto.cs`** -> AI Confidence: **99.31%**
1246. **`src/libraries/Common/src/System/Security/Cryptography/X509Certificates/CertificateHelpers.Windows.cs`** -> AI Confidence: **99.31%**
1247. **`src/libraries/Common/src/System/Security/Cryptography/X509Certificates/X509CertificateLoader.Pkcs12.cs`** -> AI Confidence: **99.31%**
1248. **`src/libraries/Common/src/System/Security/Cryptography/X509Certificates/X509CertificateLoader.cs`** -> AI Confidence: **99.31%**
1249. **`src/libraries/Common/tests/StaticTestGenerator/Program.cs`** -> AI Confidence: **99.31%**
1250. **`src/libraries/Common/tests/System/Net/Http/Http3LoopbackStream.cs`** -> AI Confidence: **99.31%**
1251. **`src/libraries/Common/tests/System/Net/Prerequisites/RemoteLoopServer/Handlers/RemoteLoopHandler.cs`** -> AI Confidence: **99.31%**
1252. **`src/libraries/Common/tests/System/Net/Security/FakeNegotiateServer.cs`** -> AI Confidence: **99.31%**
1253. **`src/libraries/Common/tests/System/Net/Security/FakeNtlmServer.cs`** -> AI Confidence: **99.31%**
1254. **`src/libraries/Common/tests/System/Runtime/Serialization/Utils.cs`** -> AI Confidence: **99.31%**
1255. **`src/libraries/Common/tests/System/Security/Cryptography/X509Certificates/RevocationResponder.cs`** -> AI Confidence: **99.31%**
1256. **`src/libraries/Common/tests/System/Xml/XmlCoreTest/AsyncUtil.cs`** -> AI Confidence: **99.31%**
1257. **`src/libraries/Common/tests/System/Xml/XmlCoreTest/ReaderUtil.cs`** -> AI Confidence: **99.31%**
1258. **`src/libraries/Common/tests/System/Xml/XmlCoreTest/WriterFactory.cs`** -> AI Confidence: **99.31%**
1259. **`src/libraries/Common/tests/System/Xml/XmlDiff/XmlDiffDocument.cs`** -> AI Confidence: **99.31%**
1260. **`src/libraries/Common/tests/TestUtilities/System/AssertExtensions.cs`** -> AI Confidence: **99.31%**
1261. **`src/libraries/Common/tests/WasmTestRunner/WasmTestRunner.cs`** -> AI Confidence: **99.31%**
1262. **`src/libraries/Fuzzing/DotnetFuzzing/Program.cs`** -> AI Confidence: **99.31%**
1263. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ComInterop/ComRuntimeHelpers.cs`** -> AI Confidence: **99.31%**
1264. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ComInterop/DynamicVariantExtensions.cs`** -> AI Confidence: **99.31%**
1265. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ComInterop/IDispatchComObject.cs`** -> AI Confidence: **99.31%**
1266. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ExpressionTreeCallRewriter.cs`** -> AI Confidence: **99.31%**
1267. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/RuntimeBinder.cs`** -> AI Confidence: **99.31%**
1268. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Semantics/Types/TypeManager.cs`** -> AI Confidence: **99.31%**
1269. **`src/libraries/Microsoft.Extensions.Caching.Memory/src/CacheEntry.CacheEntryTokens.cs`** -> AI Confidence: **99.31%**
1270. **`src/libraries/Microsoft.Extensions.Caching.Memory/src/MemoryCache.cs`** -> AI Confidence: **99.31%**
1271. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/ConfigurationBindingGenerator.Parser.cs`** -> AI Confidence: **99.31%**
1272. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/ConfigurationBindingGenerator.Suppressor.cs`** -> AI Confidence: **99.31%**
1273. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/ConfigurationBindingGenerator.cs`** -> AI Confidence: **99.31%**
1274. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/Parser/KnownTypeSymbols.cs`** -> AI Confidence: **99.31%**
1275. **`src/libraries/Microsoft.Extensions.Configuration.Binder/gen/Specs/InterceptorInfo.cs`** -> AI Confidence: **99.31%**
1276. **`src/libraries/Microsoft.Extensions.Configuration.Binder/src/ConfigurationBinder.cs`** -> AI Confidence: **99.31%**
1277. **`src/libraries/Microsoft.Extensions.Configuration.FileExtensions/src/FileConfigurationProvider.cs`** -> AI Confidence: **99.31%**
1278. **`src/libraries/Microsoft.Extensions.DependencyInjection.Abstractions/src/ActivatorUtilities.cs`** -> AI Confidence: **99.31%**
1279. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/ServiceLookup/CallSiteFactory.cs`** -> AI Confidence: **99.31%**
1280. **`src/libraries/Microsoft.Extensions.FileProviders.Physical/src/PhysicalFilesWatcher.cs`** -> AI Confidence: **99.31%**
1281. **`src/libraries/Microsoft.Extensions.FileSystemGlobbing/src/Internal/MatcherContext.cs`** -> AI Confidence: **99.31%**
1282. **`src/libraries/Microsoft.Extensions.Hosting/src/Internal/Host.cs`** -> AI Confidence: **99.31%**
1283. **`src/libraries/Microsoft.Extensions.Hosting/tests/FunctionalTests/IntegrationTesting/src/Deployers/ApplicationDeployer.cs`** -> AI Confidence: **99.31%**
1284. **`src/libraries/Microsoft.Extensions.Http/src/DefaultHttpClientFactory.cs`** -> AI Confidence: **99.31%**
1285. **`src/libraries/Microsoft.Extensions.Logging.Abstractions/gen/LoggerMessageGenerator.Parser.cs`** -> AI Confidence: **99.31%**
1286. **`src/libraries/Microsoft.Extensions.Logging.Abstractions/gen/LoggerMessageGenerator.Roslyn4.0.cs`** -> AI Confidence: **99.31%**
1287. **`src/libraries/Microsoft.Extensions.Logging.Console/src/ConsoleLoggerProcessor.cs`** -> AI Confidence: **99.31%**
1288. **`src/libraries/Microsoft.Extensions.Logging.Console/src/ConsoleLoggerProvider.cs`** -> AI Confidence: **99.31%**
1289. **`src/libraries/Microsoft.Extensions.Logging.Console/src/JsonConsoleFormatter.cs`** -> AI Confidence: **99.31%**
1290. **`src/libraries/Microsoft.Extensions.Logging.EventSource/src/LoggingEventSource.cs`** -> AI Confidence: **99.31%**
1291. **`src/libraries/Microsoft.Extensions.Logging/src/LoggerFactory.cs`** -> AI Confidence: **99.31%**
1292. **`src/libraries/Microsoft.Extensions.Options/gen/Emitter.cs`** -> AI Confidence: **99.31%**
1293. **`src/libraries/Microsoft.Extensions.Options/gen/Parser.cs`** -> AI Confidence: **99.31%**
1294. **`src/libraries/System.Collections.Immutable/tests/ImmutableSortedDictionaryTest.cs`** -> AI Confidence: **99.31%**
1295. **`src/libraries/System.ComponentModel.Composition/src/Microsoft/Internal/GenerationServices.cs`** -> AI Confidence: **99.31%**
1296. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/AttributedModel/AttributedPartCreationInfo.cs`** -> AI Confidence: **99.31%**
1297. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/CompositionException.cs`** -> AI Confidence: **99.31%**
1298. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/AggregateExportProvider.cs`** -> AI Confidence: **99.31%**
1299. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/CatalogExportProvider.cs`** -> AI Confidence: **99.31%**
1300. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/ComposablePartExportProvider.cs`** -> AI Confidence: **99.31%**
1301. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/CompositionServices.cs`** -> AI Confidence: **99.31%**
1302. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/FilteredCatalog.cs`** -> AI Confidence: **99.31%**
1303. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/ImportEngine.cs`** -> AI Confidence: **99.31%**
1304. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/ImportingMember.cs`** -> AI Confidence: **99.31%**
1305. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/ReflectionComposablePartDefinition.cs`** -> AI Confidence: **99.31%**
1306. **`src/libraries/System.ComponentModel.TypeConverter/src/MS/Internal/Xml/Linq/ComponentModel/XComponentModel.cs`** -> AI Confidence: **99.31%**
1307. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/CultureInfoConverter.cs`** -> AI Confidence: **99.31%**
1308. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/EnumConverter.cs`** -> AI Confidence: **99.31%**
1309. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/LicenseManager.cs`** -> AI Confidence: **99.31%**
1310. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/ReflectTypeDescriptionProvider.cs`** -> AI Confidence: **99.31%**
1311. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/TypeDescriptor.cs`** -> AI Confidence: **99.31%**
1312. **`src/libraries/System.ComponentModel.TypeConverter/src/System/Drawing/ColorConverter.cs`** -> AI Confidence: **99.31%**
1313. **`src/libraries/System.ComponentModel.TypeConverter/tests/TypeConverterTestBase.cs`** -> AI Confidence: **99.31%**
1314. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/ClientConfigPaths.cs`** -> AI Confidence: **99.31%**
1315. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/SettingsPropertyValue.cs`** -> AI Confidence: **99.31%**
1316. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Diagnostics/TraceUtils.cs`** -> AI Confidence: **99.31%**
1317. **`src/libraries/System.Console/tests/TermInfo.Unix.cs`** -> AI Confidence: **99.31%**
1318. **`src/libraries/System.Data.Common/src/System/Data/Common/ObjectStorage.cs`** -> AI Confidence: **99.31%**
1319. **`src/libraries/System.Data.Common/src/System/Data/DataColumn.cs`** -> AI Confidence: **99.31%**
1320. **`src/libraries/System.Data.Common/src/System/Data/DataView.cs`** -> AI Confidence: **99.31%**
1321. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLBytes.cs`** -> AI Confidence: **99.31%**
1322. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLChars.cs`** -> AI Confidence: **99.31%**
1323. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLDecimal.cs`** -> AI Confidence: **99.31%**
1324. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SqlXml.cs`** -> AI Confidence: **99.31%**
1325. **`src/libraries/System.Data.Common/src/System/Data/xmlsaver.cs`** -> AI Confidence: **99.31%**
1326. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcConnectionStringbuilder.cs`** -> AI Confidence: **99.31%**
1327. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcDataReader.cs`** -> AI Confidence: **99.31%**
1328. **`src/libraries/System.Data.OleDb/src/OleDbConnection.cs`** -> AI Confidence: **99.31%**
1329. **`src/libraries/System.Data.OleDb/src/OleDbConnectionInternal.cs`** -> AI Confidence: **99.31%**
1330. **`src/libraries/System.Data.OleDb/src/OleDbConnectionString.cs`** -> AI Confidence: **99.31%**
1331. **`src/libraries/System.Data.OleDb/src/OleDbConnectionStringBuilder.cs`** -> AI Confidence: **99.31%**
1332. **`src/libraries/System.Data.OleDb/src/OleDb_Util.cs`** -> AI Confidence: **99.31%**
1333. **`src/libraries/System.Data.OleDb/src/System/Data/ProviderBase/DbConnectionPoolCounters.cs`** -> AI Confidence: **99.31%**
1334. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Activity.cs`** -> AI Confidence: **99.31%**
1335. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/DsesFilterAndTransform.cs`** -> AI Confidence: **99.31%**
1336. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/AggregationManager.cs`** -> AI Confidence: **99.31%**
1337. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/MetricsEventSource.cs`** -> AI Confidence: **99.31%**
1338. **`src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Metrics/TagList.netcore.cs`** -> AI Confidence: **99.31%**
1339. **`src/libraries/System.Diagnostics.DiagnosticSource/tests/RuntimeMetricsTests.cs`** -> AI Confidence: **99.31%**
1340. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/EventLog.cs`** -> AI Confidence: **99.31%**
1341. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/EventLogEntry.cs`** -> AI Confidence: **99.31%**
1342. **`src/libraries/System.Diagnostics.EventLog/src/System/Diagnostics/EventLogInternal.cs`** -> AI Confidence: **99.31%**
1343. **`src/libraries/System.Diagnostics.EventLog/tests/System/Diagnostics/Reader/ProviderMetadataTests.cs`** -> AI Confidence: **99.31%**
1344. **`src/libraries/System.Diagnostics.PerformanceCounter/src/System/Diagnostics/PerformanceCounterLib.cs`** -> AI Confidence: **99.31%**
1345. **`src/libraries/System.Diagnostics.PerformanceCounter/src/System/Diagnostics/SharedPerformanceCounter.cs`** -> AI Confidence: **99.31%**
1346. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/PerformanceCounterLib.cs`** -> AI Confidence: **99.31%**
1347. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Linux.cs`** -> AI Confidence: **99.31%**
1348. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Multiplexing.cs`** -> AI Confidence: **99.31%**
1349. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Unix.cs`** -> AI Confidence: **99.31%**
1350. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Windows.cs`** -> AI Confidence: **99.31%**
1351. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/ProcessStartInfo.cs`** -> AI Confidence: **99.31%**
1352. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/ProcessUtils.Unix.cs`** -> AI Confidence: **99.31%**
1353. **`src/libraries/System.Diagnostics.Process/tests/Helpers.cs`** -> AI Confidence: **99.31%**
1354. **`src/libraries/System.Diagnostics.TextWriterTraceListener/src/System/Diagnostics/XmlWriterTraceListener.cs`** -> AI Confidence: **99.31%**
1355. **`src/libraries/System.Diagnostics.TraceSource/src/System/Diagnostics/TraceListener.cs`** -> AI Confidence: **99.31%**
1356. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADAMStoreCtx.cs`** -> AI Confidence: **99.31%**
1357. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADUtils.cs`** -> AI Confidence: **99.31%**
1358. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/SDSCache.cs`** -> AI Confidence: **99.31%**
1359. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AuthZSet.cs`** -> AI Confidence: **99.31%**
1360. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/Context.cs`** -> AI Confidence: **99.31%**
1361. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/Principal.cs`** -> AI Confidence: **99.31%**
1362. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMMembersSet.cs`** -> AI Confidence: **99.31%**
1363. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMQuerySet.cs`** -> AI Confidence: **99.31%**
1364. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMStoreCtx_LoadStore.cs`** -> AI Confidence: **99.31%**
1365. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMStoreCtx_Query.cs`** -> AI Confidence: **99.31%**
1366. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMUtils.cs`** -> AI Confidence: **99.31%**
1367. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/exceptions.cs`** -> AI Confidence: **99.31%**
1368. **`src/libraries/System.DirectoryServices.Protocols/src/System/DirectoryServices/Protocols/ldap/LdapSessionOptions.cs`** -> AI Confidence: **99.31%**
1369. **`src/libraries/System.DirectoryServices.Protocols/tests/TestServer/LdapTestServer.Protocol.cs`** -> AI Confidence: **99.31%**
1370. **`src/libraries/System.DirectoryServices.Protocols/tests/TestServer/LdapTestServer.cs`** -> AI Confidence: **99.31%**
1371. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/DirectoryContext.cs`** -> AI Confidence: **99.31%**
1372. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/DirectoryEntry.cs`** -> AI Confidence: **99.31%**
1373. **`src/libraries/System.Formats.Nrbf/src/System/Formats/Nrbf/ArraySinglePrimitiveRecord.cs`** -> AI Confidence: **99.31%**
1374. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarHeader.Write.cs`** -> AI Confidence: **99.31%**
1375. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarWriter.Windows.cs`** -> AI Confidence: **99.31%**
1376. **`src/libraries/System.IO.Compression/src/System/IO/Compression/DeflateZLib/DeflateStream.cs`** -> AI Confidence: **99.31%**
1377. **`src/libraries/System.IO.Compression/src/System/IO/Compression/ZipArchiveEntry.cs`** -> AI Confidence: **99.31%**
1378. **`src/libraries/System.IO.FileSystem.Watcher/src/System/IO/FileSystemWatcher.Linux.cs`** -> AI Confidence: **99.31%**
1379. **`src/libraries/System.IO.FileSystem.Watcher/src/System/IO/FileSystemWatcher.OSX.cs`** -> AI Confidence: **99.31%**
1380. **`src/libraries/System.IO.FileSystem.Watcher/src/System/IO/FileSystemWatcher.Windows.cs`** -> AI Confidence: **99.31%**
1381. **`src/libraries/System.IO.FileSystem.Watcher/src/System/IO/FileSystemWatcher.cs`** -> AI Confidence: **99.31%**
1382. **`src/libraries/System.IO.Hashing/src/System/IO/Hashing/Adler32.cs`** -> AI Confidence: **99.31%**
1383. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/Package.cs`** -> AI Confidence: **99.31%**
1384. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/XmlCompatibilityReader.cs`** -> AI Confidence: **99.31%**
1385. **`src/libraries/System.IO.Pipelines/src/System/IO/Pipelines/Pipe.cs`** -> AI Confidence: **99.31%**
1386. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/NamedPipeClientStream.Unix.cs`** -> AI Confidence: **99.31%**
1387. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/NamedPipeClientStream.cs`** -> AI Confidence: **99.31%**
1388. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/PipeStream.Unix.cs`** -> AI Confidence: **99.31%**
1389. **`src/libraries/System.IO.Pipes/src/System/IO/Pipes/PipeStream.Windows.cs`** -> AI Confidence: **99.31%**
1390. **`src/libraries/System.IO.Ports/src/System/IO/Ports/SerialStream.Unix.cs`** -> AI Confidence: **99.31%**
1391. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadByte.cs`** -> AI Confidence: **99.31%**
1392. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadChar.cs`** -> AI Confidence: **99.31%**
1393. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadTo.cs`** -> AI Confidence: **99.31%**
1394. **`src/libraries/System.IO.Ports/tests/SerialPort/Read_byte_int_int.cs`** -> AI Confidence: **99.31%**
1395. **`src/libraries/System.IO.Ports/tests/SerialPort/Read_char_int_int.cs`** -> AI Confidence: **99.31%**
1396. **`src/libraries/System.IO.Ports/tests/Support/PortHelper.cs`** -> AI Confidence: **99.31%**
1397. **`src/libraries/System.IO.Ports/tests/Support/SerialPortConnection.cs`** -> AI Confidence: **99.31%**
1398. **`src/libraries/System.IO.Ports/tests/Support/TCSupport.cs`** -> AI Confidence: **99.31%**
1399. **`src/libraries/System.Linq.Expressions/src/System/Dynamic/Utils/DelegateHelpers.cs`** -> AI Confidence: **99.31%**
1400. **`src/libraries/System.Linq.Expressions/src/System/Dynamic/Utils/ExpressionUtils.cs`** -> AI Confidence: **99.31%**
1401. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/BoundConstants.cs`** -> AI Confidence: **99.31%**
1402. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/CompilerScope.cs`** -> AI Confidence: **99.31%**
1403. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Statements.cs`** -> AI Confidence: **99.31%**
1404. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/IndexExpression.cs`** -> AI Confidence: **99.31%**
1405. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Interpreter/CallInstruction.Generated.cs`** -> AI Confidence: **99.31%**
1406. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Interpreter/LightLambda.cs`** -> AI Confidence: **99.31%**
1407. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/NewExpression.cs`** -> AI Confidence: **99.31%**
1408. **`src/libraries/System.Linq.Parallel/src/System/Linq/Parallel/Scheduling/OrderPreservingPipeliningSpoolingTask.cs`** -> AI Confidence: **99.31%**
1409. **`src/libraries/System.Linq.Queryable/src/System/Linq/EnumerableRewriter.cs`** -> AI Confidence: **99.31%**
1410. **`src/libraries/System.Management/src/System/Management/ManagementPath.cs`** -> AI Confidence: **99.31%**
1411. **`src/libraries/System.Memory/tests/Span/EnumerateLines.cs`** -> AI Confidence: **99.31%**
1412. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpHandler.cs`** -> AI Confidence: **99.31%**
1413. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpRequestCallback.cs`** -> AI Confidence: **99.31%**
1414. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpRequestState.cs`** -> AI Confidence: **99.31%**
1415. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpResponseParser.cs`** -> AI Confidence: **99.31%**
1416. **`src/libraries/System.Net.Http/src/System/Net/Http/Headers/CacheControlHeaderValue.cs`** -> AI Confidence: **99.31%**
1417. **`src/libraries/System.Net.Http/src/System/Net/Http/Headers/HttpHeaders.cs`** -> AI Confidence: **99.31%**
1418. **`src/libraries/System.Net.Http/src/System/Net/Http/HttpContent.cs`** -> AI Confidence: **99.31%**
1419. **`src/libraries/System.Net.Http/src/System/Net/Http/MultipartContent.cs`** -> AI Confidence: **99.31%**
1420. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/AuthenticationHelper.Digest.cs`** -> AI Confidence: **99.31%**
1421. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/AuthenticationHelper.NtAuth.cs`** -> AI Confidence: **99.31%**
1422. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/HttpConnectionPool.Http1.cs`** -> AI Confidence: **99.31%**
1423. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/HttpConnectionPool.Http2.cs`** -> AI Confidence: **99.31%**
1424. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/ConnectionPool/HttpConnectionPool.cs`** -> AI Confidence: **99.31%**
1425. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/Http2Connection.cs`** -> AI Confidence: **99.31%**
1426. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/Http2Stream.cs`** -> AI Confidence: **99.31%**
1427. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/Http3RequestStream.cs`** -> AI Confidence: **99.31%**
1428. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpConnectionBase.cs`** -> AI Confidence: **99.31%**
1429. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpWindowsProxy.cs`** -> AI Confidence: **99.31%**
1430. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/SocksHelper.cs`** -> AI Confidence: **99.31%**
1431. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiHttpInterop.cs`** -> AI Confidence: **99.31%**
1432. **`src/libraries/System.Net.Http/tests/UnitTests/Headers/CacheControlHeaderValueTest.cs`** -> AI Confidence: **99.31%**
1433. **`src/libraries/System.Net.HttpListener/src/System/Net/HttpListener.cs`** -> AI Confidence: **99.31%**
1434. **`src/libraries/System.Net.HttpListener/src/System/Net/HttpListenerRequest.cs`** -> AI Confidence: **99.31%**
1435. **`src/libraries/System.Net.HttpListener/src/System/Net/Managed/HttpConnection.cs`** -> AI Confidence: **99.31%**
1436. **`src/libraries/System.Net.HttpListener/src/System/Net/Managed/HttpListenerRequest.Managed.cs`** -> AI Confidence: **99.31%**
1437. **`src/libraries/System.Net.HttpListener/src/System/Net/Managed/HttpRequestStream.Managed.cs`** -> AI Confidence: **99.31%**
1438. **`src/libraries/System.Net.HttpListener/src/System/Net/Managed/HttpResponseStream.Managed.cs`** -> AI Confidence: **99.31%**
1439. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpListenerRequest.Windows.cs`** -> AI Confidence: **99.31%**
1440. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/WebSockets/WebSocketBase.cs`** -> AI Confidence: **99.31%**
1441. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/WebSockets/WebSocketHttpListenerDuplexStream.cs`** -> AI Confidence: **99.31%**
1442. **`src/libraries/System.Net.HttpListener/tests/TrimmingTests/CookieExtensionsTest.Helper.cs`** -> AI Confidence: **99.31%**
1443. **`src/libraries/System.Net.Mail/src/System/Net/Base64Stream.cs`** -> AI Confidence: **99.31%**
1444. **`src/libraries/System.Net.Mail/src/System/Net/Mail/MailMessage.cs`** -> AI Confidence: **99.31%**
1445. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpClient.cs`** -> AI Confidence: **99.31%**
1446. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpCommands.cs`** -> AI Confidence: **99.31%**
1447. **`src/libraries/System.Net.Mail/src/System/Net/Mime/MimePart.cs`** -> AI Confidence: **99.31%**
1448. **`src/libraries/System.Net.Mail/tests/Functional/LoopbackSmtpServer.cs`** -> AI Confidence: **99.31%**
1449. **`src/libraries/System.Net.NameResolution/src/System/Net/Dns.cs`** -> AI Confidence: **99.31%**
1450. **`src/libraries/System.Net.NameResolution/src/System/Net/NameResolutionPal.Windows.cs`** -> AI Confidence: **99.31%**
1451. **`src/libraries/System.Net.NameResolution/tests/PalTests/NameResolutionPalTests.cs`** -> AI Confidence: **99.31%**
1452. **`src/libraries/System.Net.NetworkInformation/src/System/Net/NetworkInformation/NetworkAddressChange.OSX.cs`** -> AI Confidence: **99.31%**
1453. **`src/libraries/System.Net.Ping/src/System/Net/NetworkInformation/Ping.RawSocket.cs`** -> AI Confidence: **99.31%**
1454. **`src/libraries/System.Net.Ping/src/System/Net/NetworkInformation/Ping.Windows.cs`** -> AI Confidence: **99.31%**
1455. **`src/libraries/System.Net.Primitives/src/System/Net/IPAddressParser.cs`** -> AI Confidence: **99.31%**
1456. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/MsQuicApi.cs`** -> AI Confidence: **99.31%**
1457. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/ResettableValueTaskSource.cs`** -> AI Confidence: **99.31%**
1458. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/ThrowHelper.cs`** -> AI Confidence: **99.31%**
1459. **`src/libraries/System.Net.Quic/src/System/Net/Quic/QuicConnection.cs`** -> AI Confidence: **99.31%**
1460. **`src/libraries/System.Net.Quic/src/System/Net/Quic/QuicStream.cs`** -> AI Confidence: **99.31%**
1461. **`src/libraries/System.Net.Requests/src/System/Net/FtpControlStream.cs`** -> AI Confidence: **99.31%**
1462. **`src/libraries/System.Net.Requests/src/System/Net/FtpWebRequest.cs`** -> AI Confidence: **99.31%**
1463. **`src/libraries/System.Net.Requests/src/System/Net/HttpWebRequest.cs`** -> AI Confidence: **99.31%**
1464. **`src/libraries/System.Net.Security/src/System/Net/CertificateValidationPal.Windows.cs`** -> AI Confidence: **99.31%**
1465. **`src/libraries/System.Net.Security/src/System/Net/NegotiateAuthenticationPal.ManagedSpnego.cs`** -> AI Confidence: **99.31%**
1466. **`src/libraries/System.Net.Security/src/System/Net/NegotiateAuthenticationPal.Unix.cs`** -> AI Confidence: **99.31%**
1467. **`src/libraries/System.Net.Security/src/System/Net/NegotiateAuthenticationPal.Windows.cs`** -> AI Confidence: **99.31%**
1468. **`src/libraries/System.Net.Security/src/System/Net/Security/Pal.Android/SafeDeleteSslContext.cs`** -> AI Confidence: **99.31%**
1469. **`src/libraries/System.Net.Security/src/System/Net/Security/Pal.OSX/SafeDeleteNwContext.cs`** -> AI Confidence: **99.31%**
1470. **`src/libraries/System.Net.Security/src/System/Net/Security/Pal.OSX/SafeDeleteSslContext.cs`** -> AI Confidence: **99.31%**
1471. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStream.IO.cs`** -> AI Confidence: **99.31%**
1472. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStreamCertificateContext.Linux.cs`** -> AI Confidence: **99.31%**
1473. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStreamPal.OSX.cs`** -> AI Confidence: **99.31%**
1474. **`src/libraries/System.Net.Security/src/System/Net/Security/SslStreamPal.Windows.cs`** -> AI Confidence: **99.31%**
1475. **`src/libraries/System.Net.ServerSentEvents/src/System/Net/ServerSentEvents/SseParser_1.cs`** -> AI Confidence: **99.31%**
1476. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/Socket.Tasks.cs`** -> AI Confidence: **99.31%**
1477. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/Socket.Unix.cs`** -> AI Confidence: **99.31%**
1478. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/Socket.Windows.cs`** -> AI Confidence: **99.31%**
1479. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncContext.Unix.cs`** -> AI Confidence: **99.31%**
1480. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketAsyncEngine.Wasi.cs`** -> AI Confidence: **99.31%**
1481. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketPal.Unix.cs`** -> AI Confidence: **99.31%**
1482. **`src/libraries/System.Net.Sockets/src/System/Net/Sockets/SocketPal.Windows.cs`** -> AI Confidence: **99.31%**
1483. **`src/libraries/System.Net.WebProxy/src/System/Net/WebProxy.cs`** -> AI Confidence: **99.31%**
1484. **`src/libraries/System.Net.WebSockets.Client/src/System/Net/WebSockets/WebSocketHandle.Managed.cs`** -> AI Confidence: **99.31%**
1485. **`src/libraries/System.Private.CoreLib/gen/IntrinsicsInSystemPrivateCoreLibAnalyzer.cs`** -> AI Confidence: **99.31%**
1486. **`src/libraries/System.Private.CoreLib/gen/NativeRuntimeEventSourceGenerator.cs`** -> AI Confidence: **99.31%**
1487. **`src/libraries/System.Private.CoreLib/src/Internal/Runtime/InteropServices/ComponentActivator.cs`** -> AI Confidence: **99.31%**
1488. **`src/libraries/System.Private.CoreLib/src/Internal/Win32/RegistryKey.cs`** -> AI Confidence: **99.31%**
1489. **`src/libraries/System.Private.CoreLib/src/Microsoft/Win32/SafeHandles/SafeFileHandle.OverlappedValueTaskSource.Windows.cs`** -> AI Confidence: **99.31%**
1490. **`src/libraries/System.Private.CoreLib/src/Microsoft/Win32/SafeHandles/SafeFileHandle.ThreadPoolValueTaskSource.cs`** -> AI Confidence: **99.31%**
1491. **`src/libraries/System.Private.CoreLib/src/System/AppContext.cs`** -> AI Confidence: **99.31%**
1492. **`src/libraries/System.Private.CoreLib/src/System/Collections/BitArray.cs`** -> AI Confidence: **99.31%**
1493. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/StackTrace.cs`** -> AI Confidence: **99.31%**
1494. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/EventProvider.cs`** -> AI Confidence: **99.31%**
1495. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/ManifestBuilder.cs`** -> AI Confidence: **99.31%**
1496. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/TraceLogging/TraceLoggingEventSource.cs`** -> AI Confidence: **99.31%**
1497. **`src/libraries/System.Private.CoreLib/src/System/Double.cs`** -> AI Confidence: **99.31%**
1498. **`src/libraries/System.Private.CoreLib/src/System/Enum.cs`** -> AI Confidence: **99.31%**
1499. **`src/libraries/System.Private.CoreLib/src/System/Environment.GetFolderPathCore.Unix.cs`** -> AI Confidence: **99.31%**
1500. **`src/libraries/System.Private.CoreLib/src/System/Globalization/CompareInfo.cs`** -> AI Confidence: **99.31%**
1501. **`src/libraries/System.Private.CoreLib/src/System/Globalization/CompareInfo.iOS.cs`** -> AI Confidence: **99.31%**
1502. **`src/libraries/System.Private.CoreLib/src/System/Globalization/Ordinal.Utf8.cs`** -> AI Confidence: **99.31%**
1503. **`src/libraries/System.Private.CoreLib/src/System/Globalization/Ordinal.cs`** -> AI Confidence: **99.31%**
1504. **`src/libraries/System.Private.CoreLib/src/System/IO/Enumeration/FileSystemEnumerator.Windows.cs`** -> AI Confidence: **99.31%**
1505. **`src/libraries/System.Private.CoreLib/src/System/IO/RandomAccess.Unix.cs`** -> AI Confidence: **99.31%**
1506. **`src/libraries/System.Private.CoreLib/src/System/IO/RandomAccess.Windows.cs`** -> AI Confidence: **99.31%**
1507. **`src/libraries/System.Private.CoreLib/src/System/IO/SharedMemoryManager.Unix.cs`** -> AI Confidence: **99.31%**
1508. **`src/libraries/System.Private.CoreLib/src/System/IO/Strategies/FileStreamHelpers.Windows.cs`** -> AI Confidence: **99.31%**
1509. **`src/libraries/System.Private.CoreLib/src/System/IO/StreamReader.cs`** -> AI Confidence: **99.31%**
1510. **`src/libraries/System.Private.CoreLib/src/System/IO/StreamWriter.cs`** -> AI Confidence: **99.31%**
1511. **`src/libraries/System.Private.CoreLib/src/System/Int128.cs`** -> AI Confidence: **99.31%**
1512. **`src/libraries/System.Private.CoreLib/src/System/Int32.cs`** -> AI Confidence: **99.31%**
1513. **`src/libraries/System.Private.CoreLib/src/System/Int64.cs`** -> AI Confidence: **99.31%**
1514. **`src/libraries/System.Private.CoreLib/src/System/IntPtr.cs`** -> AI Confidence: **99.31%**
1515. **`src/libraries/System.Private.CoreLib/src/System/Math.cs`** -> AI Confidence: **99.31%**
1516. **`src/libraries/System.Private.CoreLib/src/System/MathF.cs`** -> AI Confidence: **99.31%**
1517. **`src/libraries/System.Private.CoreLib/src/System/Memory.cs`** -> AI Confidence: **99.31%**
1518. **`src/libraries/System.Private.CoreLib/src/System/MemoryExtensions.cs`** -> AI Confidence: **99.31%**
1519. **`src/libraries/System.Private.CoreLib/src/System/Number.Formatting.cs`** -> AI Confidence: **99.31%**
1520. **`src/libraries/System.Private.CoreLib/src/System/Number.Parsing.cs`** -> AI Confidence: **99.31%**
1521. **`src/libraries/System.Private.CoreLib/src/System/ReadOnlyMemory.cs`** -> AI Confidence: **99.31%**
1522. **`src/libraries/System.Private.CoreLib/src/System/Reflection/AssemblyName.cs`** -> AI Confidence: **99.31%**
1523. **`src/libraries/System.Private.CoreLib/src/System/Reflection/ConstructorInvoker.cs`** -> AI Confidence: **99.31%**
1524. **`src/libraries/System.Private.CoreLib/src/System/Reflection/MethodInvoker.cs`** -> AI Confidence: **99.31%**
1525. **`src/libraries/System.Private.CoreLib/src/System/Resources/ResourceReader.cs`** -> AI Confidence: **99.31%**
1526. **`src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/ConditionalWeakTable.cs`** -> AI Confidence: **99.31%**
1527. **`src/libraries/System.Private.CoreLib/src/System/Runtime/InteropServices/ComWrappers.cs`** -> AI Confidence: **99.31%**
1528. **`src/libraries/System.Private.CoreLib/src/System/Runtime/InteropServices/Marshal.cs`** -> AI Confidence: **99.31%**
1529. **`src/libraries/System.Private.CoreLib/src/System/Runtime/Loader/AssemblyLoadContext.cs`** -> AI Confidence: **99.31%**
1530. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/ProbabilisticMap.cs`** -> AI Confidence: **99.31%**
1531. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/Strings/AsciiStringSearchValuesTeddyBase.cs`** -> AI Confidence: **99.31%**
1532. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/Strings/SingleStringSearchValuesThreeChars.cs`** -> AI Confidence: **99.31%**
1533. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/Strings/StringSearchValues.cs`** -> AI Confidence: **99.31%**
1534. **`src/libraries/System.Private.CoreLib/src/System/Single.cs`** -> AI Confidence: **99.31%**
1535. **`src/libraries/System.Private.CoreLib/src/System/StartupHookProvider.cs`** -> AI Confidence: **99.31%**
1536. **`src/libraries/System.Private.CoreLib/src/System/String.Comparison.cs`** -> AI Confidence: **99.31%**
1537. **`src/libraries/System.Private.CoreLib/src/System/String.Manipulation.cs`** -> AI Confidence: **99.31%**
1538. **`src/libraries/System.Private.CoreLib/src/System/Text/StringBuilder.cs`** -> AI Confidence: **99.31%**
1539. **`src/libraries/System.Private.CoreLib/src/System/Text/TranscodingStream.cs`** -> AI Confidence: **99.31%**
1540. **`src/libraries/System.Private.CoreLib/src/System/Threading/RegisteredWaitHandle.WindowsThreadPool.cs`** -> AI Confidence: **99.31%**
1541. **`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs`** -> AI Confidence: **99.31%**
1542. **`src/libraries/System.Private.CoreLib/src/System/Threading/Thread.Windows.cs`** -> AI Confidence: **99.31%**
1543. **`src/libraries/System.Private.CoreLib/src/System/Threading/ThreadPoolBoundHandle.WindowsThreadPool.cs`** -> AI Confidence: **99.31%**
1544. **`src/libraries/System.Private.CoreLib/src/System/Threading/ThreadPoolWorkQueue.cs`** -> AI Confidence: **99.31%**
1545. **`src/libraries/System.Private.CoreLib/src/System/ThrowHelper.cs`** -> AI Confidence: **99.31%**
1546. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.Unix.Android.cs`** -> AI Confidence: **99.31%**
1547. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.Unix.NonAndroid.cs`** -> AI Confidence: **99.31%**
1548. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.Unix.cs`** -> AI Confidence: **99.31%**
1549. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.cs`** -> AI Confidence: **99.31%**
1550. **`src/libraries/System.Private.CoreLib/src/System/UInt128.cs`** -> AI Confidence: **99.31%**
1551. **`src/libraries/System.Private.CoreLib/src/System/WeakReference.T.cs`** -> AI Confidence: **99.31%**
1552. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ClassDataContract.cs`** -> AI Confidence: **99.31%**
1553. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/CodeGenerator.cs`** -> AI Confidence: **99.31%**
1554. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/CollectionDataContract.cs`** -> AI Confidence: **99.31%**
1555. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/DataContract.cs`** -> AI Confidence: **99.31%**
1556. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/DataContractSerializer.cs`** -> AI Confidence: **99.31%**
1557. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/DataContractSet.cs`** -> AI Confidence: **99.31%**
1558. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/DataContractJsonSerializer.cs`** -> AI Confidence: **99.31%**
1559. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonDataContract.cs`** -> AI Confidence: **99.31%**
1560. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonXmlDataContract.cs`** -> AI Confidence: **99.31%**
1561. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/XmlJsonWriter.cs`** -> AI Confidence: **99.31%**
1562. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/XmlObjectSerializerReadContextComplexJson.cs`** -> AI Confidence: **99.31%**
1563. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/XmlObjectSerializerWriteContextComplexJson.cs`** -> AI Confidence: **99.31%**
1564. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ReflectionClassWriter.cs`** -> AI Confidence: **99.31%**
1565. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ReflectionReader.cs`** -> AI Confidence: **99.31%**
1566. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/ReflectionXmlFormatWriter.cs`** -> AI Confidence: **99.31%**
1567. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/SchemaExporter.cs`** -> AI Confidence: **99.31%**
1568. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializerReadContext.cs`** -> AI Confidence: **99.31%**
1569. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializerWriteContext.cs`** -> AI Confidence: **99.31%**
1570. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializerWriteContextComplex.cs`** -> AI Confidence: **99.31%**
1571. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XsdDataContractExporter.cs`** -> AI Confidence: **99.31%**
1572. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBaseReader.cs`** -> AI Confidence: **99.31%**
1573. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBufferReader.cs`** -> AI Confidence: **99.31%**
1574. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlCanonicalWriter.cs`** -> AI Confidence: **99.31%**
1575. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlConverter.cs`** -> AI Confidence: **99.31%**
1576. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlDictionaryReader.cs`** -> AI Confidence: **99.31%**
1577. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlStreamNodeWriter.cs`** -> AI Confidence: **99.31%**
1578. **`src/libraries/System.Private.Uri/src/System/UriExt.cs`** -> AI Confidence: **99.31%**
1579. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/XNode.cs`** -> AI Confidence: **99.31%**
1580. **`src/libraries/System.Private.Xml.Linq/tests/Properties/ImplicitConversionsRoundTrip.cs`** -> AI Confidence: **99.31%**
1581. **`src/libraries/System.Private.Xml.Linq/tests/Properties/XElement_Value.cs`** -> AI Confidence: **99.31%**
1582. **`src/libraries/System.Private.Xml.Linq/tests/Schema/ExtensionTests.cs`** -> AI Confidence: **99.31%**
1583. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/AddFirstAddFirstIntoDocument.cs`** -> AI Confidence: **99.31%**
1584. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/ParamsObjectsCreation.cs`** -> AI Confidence: **99.31%**
1585. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/XAttributeEnumRemove.cs`** -> AI Confidence: **99.31%**
1586. **`src/libraries/System.Private.Xml.Linq/tests/TreeManipulation/XContainerAddIntoDocument.cs`** -> AI Confidence: **99.31%**
1587. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/HelperExtensionMethods.cs`** -> AI Confidence: **99.31%**
1588. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/FunctionalTests.cs`** -> AI Confidence: **99.31%**
1589. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/OmitDuplicatesAnnotation.cs`** -> AI Confidence: **99.31%**
1590. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/SaveOptions_OmitDuplicateNamespace.cs`** -> AI Confidence: **99.31%**
1591. **`src/libraries/System.Private.Xml.Linq/tests/xNodeBuilder/XmlReaderDiff.cs`** -> AI Confidence: **99.31%**
1592. **`src/libraries/System.Private.Xml/src/System/Xml/BinaryXml/SqlUtils.cs`** -> AI Confidence: **99.31%**
1593. **`src/libraries/System.Private.Xml/src/System/Xml/BinaryXml/XmlBinaryReader.cs`** -> AI Confidence: **99.31%**
1594. **`src/libraries/System.Private.Xml/src/System/Xml/Cache/XPathDocumentBuilder.cs`** -> AI Confidence: **99.31%**
1595. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlAutoDetectWriter.cs`** -> AI Confidence: **99.31%**
1596. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlCharCheckingWriterAsync.cs`** -> AI Confidence: **99.31%**
1597. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlSubtreeReaderAsync.cs`** -> AI Confidence: **99.31%**
1598. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlValidatingReaderImpl.cs`** -> AI Confidence: **99.31%**
1599. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWellFormedWriterAsync.cs`** -> AI Confidence: **99.31%**
1600. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWriterSettings.cs`** -> AI Confidence: **99.31%**
1601. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XsdCachingReader.cs`** -> AI Confidence: **99.31%**
1602. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XsdCachingReaderAsync.cs`** -> AI Confidence: **99.31%**
1603. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XsdValidatingReaderAsync.cs`** -> AI Confidence: **99.31%**
1604. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/DocumentXPathNavigator.cs`** -> AI Confidence: **99.31%**
1605. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlDocument.cs`** -> AI Confidence: **99.31%**
1606. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlElement.cs`** -> AI Confidence: **99.31%**
1607. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlNode.cs`** -> AI Confidence: **99.31%**
1608. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/Asttree.cs`** -> AI Confidence: **99.31%**
1609. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/ConstraintStruct.cs`** -> AI Confidence: **99.31%**
1610. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/DtdParserAsync.cs`** -> AI Confidence: **99.31%**
1611. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/CodeGenerator.cs`** -> AI Confidence: **99.31%**
1612. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/Compilation.cs`** -> AI Confidence: **99.31%**
1613. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/ImportContext.cs`** -> AI Confidence: **99.31%**
1614. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/ReflectionXmlSerializationReader.cs`** -> AI Confidence: **99.31%**
1615. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/SoapReflectionImporter.cs`** -> AI Confidence: **99.31%**
1616. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/SourceInfo.cs`** -> AI Confidence: **99.31%**
1617. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/Types.cs`** -> AI Confidence: **99.31%**
1618. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlReflectionImporter.cs`** -> AI Confidence: **99.31%**
1619. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSchemas.cs`** -> AI Confidence: **99.31%**
1620. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationGeneratedCode.cs`** -> AI Confidence: **99.31%**
1621. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializationILGen.cs`** -> AI Confidence: **99.31%**
1622. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/XmlSerializer.cs`** -> AI Confidence: **99.31%**
1623. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/CompiledXPathExpr.cs`** -> AI Confidence: **99.31%**
1624. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/Query.cs`** -> AI Confidence: **99.31%**
1625. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/XPathNavigator.cs`** -> AI Confidence: **99.31%**
1626. **`src/libraries/System.Private.Xml/src/System/Xml/XmlConvert.cs`** -> AI Confidence: **99.31%**
1627. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/IteratorDescriptor.cs`** -> AI Confidence: **99.31%**
1628. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlILConstructAnalyzer.cs`** -> AI Confidence: **99.31%**
1629. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlILOptimizerVisitor.cs`** -> AI Confidence: **99.31%**
1630. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlILTrace.cs`** -> AI Confidence: **99.31%**
1631. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlIlVisitor.cs`** -> AI Confidence: **99.31%**
1632. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/QIL/QilXmlWriter.cs`** -> AI Confidence: **99.31%**
1633. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/SetIterators.cs`** -> AI Confidence: **99.31%**
1634. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlExtensionFunction.cs`** -> AI Confidence: **99.31%**
1635. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlQueryContext.cs`** -> AI Confidence: **99.31%**
1636. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XsltLibrary.cs`** -> AI Confidence: **99.31%**
1637. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XPath/XPathBuilder.cs`** -> AI Confidence: **99.31%**
1638. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XmlIlGenerator.cs`** -> AI Confidence: **99.31%**
1639. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XslException.cs`** -> AI Confidence: **99.31%**
1640. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/MatcherBuilder.cs`** -> AI Confidence: **99.31%**
1641. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/QilGenerator.cs`** -> AI Confidence: **99.31%**
1642. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/QilGeneratorEnv.cs`** -> AI Confidence: **99.31%**
1643. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/XPathPatternParser.cs`** -> AI Confidence: **99.31%**
1644. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/XslAstAnalyzer.cs`** -> AI Confidence: **99.31%**
1645. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Xslt/XsltLoader.cs`** -> AI Confidence: **99.31%**
1646. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/BuilderInfo.cs`** -> AI Confidence: **99.31%**
1647. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/Processor.cs`** -> AI Confidence: **99.31%**
1648. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/TemplateAction.cs`** -> AI Confidence: **99.31%**
1649. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/XsltCompileContext.cs`** -> AI Confidence: **99.31%**
1650. **`src/libraries/System.Private.Xml/tests/ExceptionVerifier.cs`** -> AI Confidence: **99.31%**
1651. **`src/libraries/System.Private.Xml/tests/Writers/RwFactory/CXmlDriverEngine.cs`** -> AI Confidence: **99.31%**
1652. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/Errata4.cs`** -> AI Confidence: **99.31%**
1653. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/XslCompiledTransform.cs`** -> AI Confidence: **99.31%**
1654. **`src/libraries/System.Private.Xml/tests/Xslt/XslCompiledTransformApi/XsltSettings.cs`** -> AI Confidence: **99.31%**
1655. **`src/libraries/System.Reflection.Emit/src/System/Reflection/Emit/ModuleBuilderImpl.cs`** -> AI Confidence: **99.31%**
1656. **`src/libraries/System.Reflection.Emit/tests/PersistedAssemblyBuilder/AssemblySaveCustomAttributeTests.cs`** -> AI Confidence: **99.31%**
1657. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/PortableExecutable/PEReader.EmbeddedPortablePdb.cs`** -> AI Confidence: **99.31%**
1658. **`src/libraries/System.Reflection.Metadata/tests/Metadata/TypeNameParserSamples.cs`** -> AI Confidence: **99.31%**
1659. **`src/libraries/System.Reflection.MetadataLoadContext/tests/src/Tests/CustomAttributes/CustomAttributeTests.cs`** -> AI Confidence: **99.31%**
1660. **`src/libraries/System.Resources.Extensions/src/System/Resources/Extensions/BinaryFormat/BinaryFormattedObject.TypeResolver.cs`** -> AI Confidence: **99.31%**
1661. **`src/libraries/System.Resources.Extensions/src/System/Resources/Extensions/BinaryFormat/BinaryFormattedObject.cs`** -> AI Confidence: **99.31%**
1662. **`src/libraries/System.Resources.Extensions/tests/BinaryFormatTests/Legacy/BinaryFormatterTests.cs`** -> AI Confidence: **99.31%**
1663. **`src/libraries/System.Resources.Extensions/tests/BinaryFormatTests/Legacy/EqualityExtensions.cs`** -> AI Confidence: **99.31%**
1664. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/CacheExpires.cs`** -> AI Confidence: **99.31%**
1665. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/HostFileChangeMonitor.cs`** -> AI Confidence: **99.31%**
1666. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCache.cs`** -> AI Confidence: **99.31%**
1667. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCacheEntry.cs`** -> AI Confidence: **99.31%**
1668. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCacheEntryChangeMonitor.cs`** -> AI Confidence: **99.31%**
1669. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCacheStatistics.cs`** -> AI Confidence: **99.31%**
1670. **`src/libraries/System.Runtime.Caching/src/System/Runtime/Caching/MemoryCacheStore.cs`** -> AI Confidence: **99.31%**
1671. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/Interop/JavaScriptExports.CoreCLR.cs`** -> AI Confidence: **99.31%**
1672. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/JSHostImplementation.cs`** -> AI Confidence: **99.31%**
1673. **`src/libraries/System.Runtime.InteropServices.JavaScript/src/System/Runtime/InteropServices/JavaScript/Marshaling/JSMarshalerArgument.Task.cs`** -> AI Confidence: **99.31%**
1674. **`src/libraries/System.Runtime.InteropServices.JavaScript/tests/JSImportGenerator.UnitTest/Fails.cs`** -> AI Confidence: **99.31%**
1675. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/Analyzers/ComInterfaceGeneratorDiagnosticsAnalyzer.cs`** -> AI Confidence: **99.31%**
1676. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/Analyzers/VtableIndexStubDiagnosticsAnalyzer.cs`** -> AI Confidence: **99.31%**
1677. **`src/libraries/System.Runtime.InteropServices/gen/DownlevelLibraryImportGenerator/DownlevelLibraryImportDiagnosticsAnalyzer.cs`** -> AI Confidence: **99.31%**
1678. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/CustomMarshallerAttributeAnalyzer.cs`** -> AI Confidence: **99.31%**
1679. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/CustomMarshallerAttributeFixer.cs`** -> AI Confidence: **99.31%**
1680. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/LibraryImportDiagnosticsAnalyzer.cs`** -> AI Confidence: **99.31%**
1681. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/ContainingSyntaxContext.cs`** -> AI Confidence: **99.31%**
1682. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/ManagedToNativeStubGenerator.cs`** -> AI Confidence: **99.31%**
1683. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/ManualTypeMarshallingHelper.cs`** -> AI Confidence: **99.31%**
1684. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/MarshalAsParser.cs`** -> AI Confidence: **99.31%**
1685. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/Marshalling/BoolMarshaller.cs`** -> AI Confidence: **99.31%**
1686. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/Marshalling/CharMarshaller.cs`** -> AI Confidence: **99.31%**
1687. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/Marshalling/MarshallerHelpers.cs`** -> AI Confidence: **99.31%**
1688. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/TypeSymbolExtensions.cs`** -> AI Confidence: **99.31%**
1689. **`src/libraries/System.Runtime.InteropServices/tests/LibraryImportGenerator.UnitTests/CompileFails.cs`** -> AI Confidence: **99.31%**
1690. **`src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector128Tests.cs`** -> AI Confidence: **99.31%**
1691. **`src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector256Tests.cs`** -> AI Confidence: **99.31%**
1692. **`src/libraries/System.Runtime.Intrinsics/tests/Vectors/Vector64Tests.cs`** -> AI Confidence: **99.31%**
1693. **`src/libraries/System.Runtime.Numerics/src/System/Number.BigInteger.cs`** -> AI Confidence: **99.31%**
1694. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/BigInteger.cs`** -> AI Confidence: **99.31%**
1695. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/Complex.cs`** -> AI Confidence: **99.31%**
1696. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/FormatterServices.cs`** -> AI Confidence: **99.31%**
1697. **`src/libraries/System.Runtime.Serialization.Formatters/tests/EqualityExtensions.cs`** -> AI Confidence: **99.31%**
1698. **`src/libraries/System.Runtime.Serialization.Schema/src/System/Runtime/Serialization/Schema/CodeExporter.cs`** -> AI Confidence: **99.31%**
1699. **`src/libraries/System.Runtime.Serialization.Schema/src/System/Runtime/Serialization/Schema/XsdDataContractImporter.cs`** -> AI Confidence: **99.31%**
1700. **`src/libraries/System.Runtime.Serialization.Xml/tests/SerializationTestTypes/DataContract.cs`** -> AI Confidence: **99.31%**
1701. **`src/libraries/System.Runtime/tests/System.Globalization.Tests/System/Globalization/GraphemeBreakTest.cs`** -> AI Confidence: **99.31%**
1702. **`src/libraries/System.Runtime/tests/System.IO.FileSystem.Tests/PortedCommon/CommonUtilities.cs`** -> AI Confidence: **99.31%**
1703. **`src/libraries/System.Runtime/tests/System.IO.FileSystem.Tests/PortedCommon/IOServices.cs`** -> AI Confidence: **99.31%**
1704. **`src/libraries/System.Runtime/tests/System.Runtime.InteropServices.RuntimeInformation.Tests/DescriptionNameTests.cs`** -> AI Confidence: **99.31%**
1705. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/TimeZoneInfoTests.Common.cs`** -> AI Confidence: **99.31%**
1706. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/TimeZoneInfoTests.cs`** -> AI Confidence: **99.31%**
1707. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskRtTests_Core.cs`** -> AI Confidence: **99.31%**
1708. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskRunSyncTests.cs`** -> AI Confidence: **99.31%**
1709. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/TaskScheduler/TaskSchedulerTests.cs`** -> AI Confidence: **99.31%**
1710. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/SecurityDescriptor.cs`** -> AI Confidence: **99.31%**
1711. **`src/libraries/System.Security.Cryptography.Cose/src/System/Security/Cryptography/Cose/CoseHelpers.cs`** -> AI Confidence: **99.31%**
1712. **`src/libraries/System.Security.Cryptography.Cose/src/System/Security/Cryptography/Cose/CoseMessage.cs`** -> AI Confidence: **99.31%**
1713. **`src/libraries/System.Security.Cryptography.Cose/src/System/Security/Cryptography/Cose/CoseMultiSignMessage.cs`** -> AI Confidence: **99.31%**
1714. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/AsnHelpers.cs`** -> AI Confidence: **99.31%**
1715. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.KeyTrans.cs`** -> AI Confidence: **99.31%**
1716. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/Windows/DecryptorPalWindows.Decrypt.cs`** -> AI Confidence: **99.31%**
1717. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/Windows/HelpersWindows.cs`** -> AI Confidence: **99.31%**
1718. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/Windows/PkcsPalWindows.Encrypt.cs`** -> AI Confidence: **99.31%**
1719. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/PkcsHelpers.cs`** -> AI Confidence: **99.31%**
1720. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/CmsSignature.RSA.cs`** -> AI Confidence: **99.31%**
1721. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/CmsSignature.cs`** -> AI Confidence: **99.31%**
1722. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/Rfc3161TimestampToken.cs`** -> AI Confidence: **99.31%**
1723. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/Rfc3161TimestampTokenInfo.cs`** -> AI Confidence: **99.31%**
1724. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/SignerInfo.cs`** -> AI Confidence: **99.31%**
1725. **`src/libraries/System.Security.Cryptography.Pkcs/tests/Pkcs12/Pkcs12BuilderTests.cs`** -> AI Confidence: **99.31%**
1726. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/EncryptedXml.cs`** -> AI Confidence: **99.31%**
1727. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/SignedXml.cs`** -> AI Confidence: **99.31%**
1728. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/CapiHelper.Windows.cs`** -> AI Confidence: **99.31%**
1729. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/CngHelpers.cs`** -> AI Confidence: **99.31%**
1730. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/CryptoStream.cs`** -> AI Confidence: **99.31%**
1731. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/HKDF.Windows.cs`** -> AI Confidence: **99.31%**
1732. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/Rfc2898DeriveBytes.cs`** -> AI Confidence: **99.31%**
1733. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/CertificateRequest.cs`** -> AI Confidence: **99.31%**
1734. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/ChainPal.Android.cs`** -> AI Confidence: **99.31%**
1735. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslCertificateAssetDownloader.cs`** -> AI Confidence: **99.31%**
1736. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslCrlCache.cs`** -> AI Confidence: **99.31%**
1737. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslX509ChainProcessor.cs`** -> AI Confidence: **99.31%**
1738. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/PublicKey.cs`** -> AI Confidence: **99.31%**
1739. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/UnixExportProvider.cs`** -> AI Confidence: **99.31%**
1740. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509Certificate2.cs`** -> AI Confidence: **99.31%**
1741. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509Certificate2Collection.cs`** -> AI Confidence: **99.31%**
1742. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509CertificateLoader.macOS.cs`** -> AI Confidence: **99.31%**
1743. **`src/libraries/System.Security.Principal.Windows/src/System/Security/Principal/NTAccount.cs`** -> AI Confidence: **99.31%**
1744. **`src/libraries/System.Security.Principal.Windows/src/System/Security/Principal/SID.cs`** -> AI Confidence: **99.31%**
1745. **`src/libraries/System.Security.Principal.Windows/src/System/Security/Principal/WindowsIdentity.cs`** -> AI Confidence: **99.31%**
1746. **`src/libraries/System.ServiceModel.Syndication/tests/Utils/XmlDiff.cs`** -> AI Confidence: **99.31%**
1747. **`src/libraries/System.ServiceModel.Syndication/tests/Utils/XmlDiffDocument.cs`** -> AI Confidence: **99.31%**
1748. **`src/libraries/System.ServiceProcess.ServiceController/src/System/ServiceProcess/ServiceController.cs`** -> AI Confidence: **99.31%**
1749. **`src/libraries/System.Speech/src/Internal/GrammarBuilding/BuilderElements.cs`** -> AI Confidence: **99.31%**
1750. **`src/libraries/System.Speech/src/Internal/ObjectToken/ObjectToken.cs`** -> AI Confidence: **99.31%**
1751. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/CustomGrammar.cs`** -> AI Confidence: **99.31%**
1752. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/SRGSCompiler.cs`** -> AI Confidence: **99.31%**
1753. **`src/libraries/System.Speech/src/Internal/Synthesis/EngineSite.cs`** -> AI Confidence: **99.31%**
1754. **`src/libraries/System.Speech/src/Recognition/Grammar.cs`** -> AI Confidence: **99.31%**
1755. **`src/libraries/System.Speech/src/Recognition/SpeechRecognitionEngine.cs`** -> AI Confidence: **99.31%**
1756. **`src/libraries/System.Speech/src/Recognition/SrgsGrammar/SrgsItem.cs`** -> AI Confidence: **99.31%**
1757. **`src/libraries/System.Speech/src/Recognition/SrgsGrammar/SrgsNameValueTag.cs`** -> AI Confidence: **99.31%**
1758. **`src/libraries/System.Speech/src/Recognition/SrgsGrammar/SrgsRule.cs`** -> AI Confidence: **99.31%**
1759. **`src/libraries/System.Speech/src/Result/RecognitionResult.cs`** -> AI Confidence: **99.31%**
1760. **`src/libraries/System.Text.Encoding.CodePages/src/System/Text/BaseCodePageEncoding.cs`** -> AI Confidence: **99.31%**
1761. **`src/libraries/System.Text.Encodings.Web/src/System/Text/Encodings/Web/TextEncoder.cs`** -> AI Confidence: **99.31%**
1762. **`src/libraries/System.Text.Encodings.Web/tests/JavaScriptEncoderTests.cs`** -> AI Confidence: **99.31%**
1763. **`src/libraries/System.Text.Encodings.Web/tools/GenUnicodeRanges/Program.cs`** -> AI Confidence: **99.31%**
1764. **`src/libraries/System.Text.Json/gen/JsonSourceGenerator.Emitter.cs`** -> AI Confidence: **99.31%**
1765. **`src/libraries/System.Text.Json/gen/JsonSourceGenerator.Roslyn3.11.cs`** -> AI Confidence: **99.31%**
1766. **`src/libraries/System.Text.Json/src/System/Text/Json/JsonHelpers.cs`** -> AI Confidence: **99.31%**
1767. **`src/libraries/System.Text.Json/src/System/Text/Json/Schema/JsonSchemaExporter.cs`** -> AI Confidence: **99.31%**
1768. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Object/ObjectConverterFactory.cs`** -> AI Confidence: **99.31%**
1769. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Object/ObjectWithParameterizedConstructorConverter.cs`** -> AI Confidence: **99.31%**
1770. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Value/EnumConverter.cs`** -> AI Confidence: **99.31%**
1771. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonSerializerOptions.Caching.cs`** -> AI Confidence: **99.31%**
1772. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonSerializerOptions.cs`** -> AI Confidence: **99.31%**
1773. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Metadata/JsonTypeInfo.cs`** -> AI Confidence: **99.31%**
1774. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/ReadStackFrame.cs`** -> AI Confidence: **99.31%**
1775. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/WriteStack.cs`** -> AI Confidence: **99.31%**
1776. **`src/libraries/System.Text.Json/tests/Common/JsonTestHelper.cs`** -> AI Confidence: **99.31%**
1777. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/JsonTestHelper.cs`** -> AI Confidence: **99.31%**
1778. **`src/libraries/System.Text.RegularExpressions/gen/RegexGenerator.Emitter.cs`** -> AI Confidence: **99.31%**
1779. **`src/libraries/System.Text.RegularExpressions/gen/RegexGenerator.Parser.cs`** -> AI Confidence: **99.31%**
1780. **`src/libraries/System.Text.RegularExpressions/gen/RegexGenerator.cs`** -> AI Confidence: **99.31%**
1781. **`src/libraries/System.Text.RegularExpressions/gen/UpgradeToGeneratedRegexCodeFixer.cs`** -> AI Confidence: **99.31%**
1782. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexCompiler.cs`** -> AI Confidence: **99.31%**
1783. **`src/libraries/System.Transactions.Local/src/System/Transactions/TransactionManager.cs`** -> AI Confidence: **99.31%**
1784. **`src/libraries/System.Transactions.Local/tests/AsyncTransactionScopeTests.cs`** -> AI Confidence: **99.31%**
1785. **`src/libraries/System.Web.HttpUtility/src/System/Web/Util/HttpEncoder.cs`** -> AI Confidence: **99.31%**
1786. **`src/libraries/System.Windows.Extensions/src/System/Media/SoundPlayer.cs`** -> AI Confidence: **99.31%**
1787. **`src/mono/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeTypeBuilder.Mono.cs`** -> AI Confidence: **99.31%**
1788. **`src/mono/System.Private.CoreLib/src/System/Reflection/TypeNameResolver.Mono.cs`** -> AI Confidence: **99.31%**
1789. **`src/mono/System.Private.CoreLib/src/System/RuntimeType.Mono.cs`** -> AI Confidence: **99.31%**
1790. **`src/mono/browser/debugger/BrowserDebugProxy/EvaluateExpression.cs`** -> AI Confidence: **99.31%**
1791. **`src/mono/browser/debugger/BrowserDebugProxy/JObjectValueCreator.cs`** -> AI Confidence: **99.31%**
1792. **`src/mono/browser/debugger/BrowserDebugProxy/MemberReferenceResolver.cs`** -> AI Confidence: **99.31%**
1793. **`src/mono/browser/debugger/BrowserDebugProxy/MonoProxy.cs`** -> AI Confidence: **99.31%**
1794. **`src/mono/mono/tests/merp-crash-test.cs`** -> AI Confidence: **99.31%**
1795. **`src/mono/mono/tests/test-runner.cs`** -> AI Confidence: **99.31%**
1796. **`src/mono/mono/tests/verifier/AssemblyRunner.cs`** -> AI Confidence: **99.31%**
1797. **`src/mono/sample/wasm/simple-server/Program.cs`** -> AI Confidence: **99.31%**
1798. **`src/mono/wasi/Wasi.Build.Tests/BuildTestBase.cs`** -> AI Confidence: **99.31%**
1799. **`src/mono/wasm/Wasm.Build.Tests/BrowserRunner.cs`** -> AI Confidence: **99.31%**
1800. **`src/mono/wasm/Wasm.Build.Tests/Common/TestUtils.cs`** -> AI Confidence: **99.31%**
1801. **`src/mono/wasm/Wasm.Build.Tests/Common/Utils.cs`** -> AI Confidence: **99.31%**
1802. **`src/mono/wasm/Wasm.Build.Tests/Templates/WasmTemplateTests.cs`** -> AI Confidence: **99.31%**
1803. **`src/mono/wasm/Wasm.Build.Tests/WasmSdkBasedProjectProvider.cs`** -> AI Confidence: **99.31%**
1804. **`src/mono/wasm/host/Options.cs`** -> AI Confidence: **99.31%**
1805. **`src/mono/wasm/symbolicator/WasmSymbolicator.cs`** -> AI Confidence: **99.31%**
1806. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/EcmaMetadata_1.cs`** -> AI Confidence: **99.31%**
1807. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/Loader_1.cs`** -> AI Confidence: **99.31%**
1808. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/StackWalk_1.cs`** -> AI Confidence: **99.31%**
1809. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataFrame.cs`** -> AI Confidence: **99.31%**
1810. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataStackWalk.cs`** -> AI Confidence: **99.31%**
1811. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader/ContractDescriptorParser.cs`** -> AI Confidence: **99.31%**
1812. **`src/native/managed/cdac/tests/DumpTests/DumpTestBase.cs`** -> AI Confidence: **99.31%**
1813. **`src/native/managed/cdac/tests/DumpTests/StackWalkDumpTests.cs`** -> AI Confidence: **99.31%**
1814. **`src/native/managed/cdac/tests/MethodTableTests.cs`** -> AI Confidence: **99.31%**
1815. **`src/native/managed/cdac/tests/MockMemorySpace.cs`** -> AI Confidence: **99.31%**
1816. **`src/tasks/AndroidAppBuilder/ApkBuilder.cs`** -> AI Confidence: **99.31%**
1817. **`src/tasks/AotCompilerTask/MonoAOTCompiler.cs`** -> AI Confidence: **99.31%**
1818. **`src/tasks/AppleAppBuilder/Xcode.cs`** -> AI Confidence: **99.31%**
1819. **`src/tasks/AssemblyStripper/AssemblyStripper.cs`** -> AI Confidence: **99.31%**
1820. **`src/tasks/LibraryBuilder/LibraryBuilder.cs`** -> AI Confidence: **99.31%**
1821. **`src/tasks/Microsoft.NET.Sdk.WebAssembly.Pack.Tasks/ComputeWasmBuildAssets.cs`** -> AI Confidence: **99.31%**
1822. **`src/tasks/Microsoft.NET.Sdk.WebAssembly.Pack.Tasks/GenerateWasmBootJson.cs`** -> AI Confidence: **99.31%**
1823. **`src/tasks/MonoTargetsTasks/EmitBundleTask/EmitBundleBase.cs`** -> AI Confidence: **99.31%**
1824. **`src/tasks/MonoTargetsTasks/ILStrip/ILStrip.cs`** -> AI Confidence: **99.31%**
1825. **`src/tasks/WasmAppBuilder/EmccCompile.cs`** -> AI Confidence: **99.31%**
1826. **`src/tasks/WasmAppBuilder/WasmAppBuilderBaseTask.cs`** -> AI Confidence: **99.31%**
1827. **`src/tasks/WasmAppBuilder/coreclr/PInvokeCollector.cs`** -> AI Confidence: **99.31%**
1828. **`src/tasks/WasmBuildTasks/UpdateChromeVersions.cs`** -> AI Confidence: **99.31%**
1829. **`src/tasks/WorkloadBuildTasks/PatchNuGetConfig.cs`** -> AI Confidence: **99.31%**
1830. **`src/tests/Common/CoreCLRTestLibrary/CoreclrTestWrapperLib.cs`** -> AI Confidence: **99.31%**
1831. **`src/tests/Common/CoreCLRTestLibrary/OutOfProcessTest.cs`** -> AI Confidence: **99.31%**
1832. **`src/tests/Common/XUnitLogChecker/XUnitLogChecker.cs`** -> AI Confidence: **99.31%**
1833. **`src/tests/Common/XUnitWrapperGenerator/ITestInfo.cs`** -> AI Confidence: **99.31%**
1834. **`src/tests/Common/XUnitWrapperGenerator/XUnitWrapperGenerator.cs`** -> AI Confidence: **99.31%**
1835. **`src/tests/GC/API/GC/GetTotalAllocatedBytes.cs`** -> AI Confidence: **99.31%**
1836. **`src/tests/Interop/MarshalAPI/IUnknown/IUnknownTest.cs`** -> AI Confidence: **99.31%**
1837. **`src/tests/Interop/NativeLibrary/API/GetMainProgramHandleTests.cs`** -> AI Confidence: **99.31%**
1838. **`src/tests/Interop/NativeLibrary/Callback/CallbackStressTest.cs`** -> AI Confidence: **99.31%**
1839. **`src/tests/Interop/SimpleStruct/SimpleStructManaged.cs`** -> AI Confidence: **99.31%**
1840. **`src/tests/Interop/StructMarshalling/ReversePInvoke/Helper.cs`** -> AI Confidence: **99.31%**
1841. **`src/tests/Interop/Swift/SwiftErrorHandling/SwiftErrorHandling.cs`** -> AI Confidence: **99.31%**
1842. **`src/tests/JIT/Directed/Convert/out_of_range_fp_to_int_conversions.cs`** -> AI Confidence: **99.31%**
1843. **`src/tests/JIT/HardwareIntrinsics/X86/General/VectorArray.cs`** -> AI Confidence: **99.31%**
1844. **`src/tests/JIT/HardwareIntrinsics/X86/Sse2.X64/StoreNonTemporal.cs`** -> AI Confidence: **99.31%**
1845. **`src/tests/JIT/HardwareIntrinsics/X86/Sse41/LoadAlignedVector128NonTemporal.cs`** -> AI Confidence: **99.31%**
1846. **`src/tests/JIT/HardwareIntrinsics/X86_Avx/Avx2/GatherMaskVector128.cs`** -> AI Confidence: **99.31%**
1847. **`src/tests/JIT/HardwareIntrinsics/X86_Avx/Avx2/GatherMaskVector256.cs`** -> AI Confidence: **99.31%**
1848. **`src/tests/JIT/HardwareIntrinsics/X86_Avx/Avx2/GatherVector128.cs`** -> AI Confidence: **99.31%**
1849. **`src/tests/JIT/HardwareIntrinsics/X86_Avx/Avx2/GatherVector256.cs`** -> AI Confidence: **99.31%**
1850. **`src/tests/JIT/IL_Conformance/Convert/TestConvertFromIntegral.cs`** -> AI Confidence: **99.31%**
1851. **`src/tests/JIT/Regression/CLR-x86-JIT/V2.0-Beta2/b425314/b425314.cs`** -> AI Confidence: **99.31%**
1852. **`src/tests/JIT/Regression/JitBlue/GitHub_23159/GitHub_23159.cs`** -> AI Confidence: **99.31%**
1853. **`src/tests/JIT/SIMD/CircleInConvex.cs`** -> AI Confidence: **99.31%**
1854. **`src/tests/JIT/SIMD/ShiftOperations.cs`** -> AI Confidence: **99.31%**
1855. **`src/tests/JIT/Stress/ABI/Gen.cs`** -> AI Confidence: **99.31%**
1856. **`src/tests/JIT/Stress/ABI/Program.cs`** -> AI Confidence: **99.31%**
1857. **`src/tests/JIT/Stress/ABI/Stubs.cs`** -> AI Confidence: **99.31%**
1858. **`src/tests/JIT/opt/SVE/ChangeMaskUse.cs`** -> AI Confidence: **99.31%**
1859. **`src/tests/JIT/opt/Structs/structcopies.cs`** -> AI Confidence: **99.31%**
1860. **`src/tests/Loader/CollectibleAssemblies/ResolvedFromDifferentContext/ResolvedFromDifferentContext.cs`** -> AI Confidence: **99.31%**
1861. **`src/tests/Loader/binding/tracing/BinderEventListener.cs`** -> AI Confidence: **99.31%**
1862. **`src/tests/Loader/binding/tracing/Helpers.cs`** -> AI Confidence: **99.31%**
1863. **`src/tests/Loader/classloader/DictionaryExpansion/DictionaryExpansion.cs`** -> AI Confidence: **99.31%**
1864. **`src/tests/Loader/classloader/generics/ByRefLike/Validate.cs`** -> AI Confidence: **99.31%**
1865. **`src/tests/async/eh-microbench/eh-microbench.cs`** -> AI Confidence: **99.31%**
1866. **`src/tests/baseservices/exceptions/exceptionstacktrace/exceptionstacktrace.cs`** -> AI Confidence: **99.31%**
1867. **`src/tests/baseservices/exceptions/stackoverflow/stackoverflowtester.cs`** -> AI Confidence: **99.31%**
1868. **`src/tests/readytorun/coreroot_determinism/Program.cs`** -> AI Confidence: **99.31%**
1869. **`src/tests/readytorun/tests/test.cs`** -> AI Confidence: **99.31%**
1870. **`src/tests/tracing/eventcounter/gh53564.cs`** -> AI Confidence: **99.31%**
1871. **`src/tests/tracing/eventcounter/regression-25709.cs`** -> AI Confidence: **99.31%**
1872. **`src/tests/tracing/eventcounter/runtimecounters.cs`** -> AI Confidence: **99.31%**
1873. **`src/tests/tracing/eventpipe/common/Microsoft.Diagnostics.NETCore.Client/DiagnosticsServerRouter/DiagnosticsServerRouterFactory.cs`** -> AI Confidence: **99.31%**
1874. **`src/tests/tracing/eventpipe/common/Reverse.cs`** -> AI Confidence: **99.31%**
1875. **`src/tests/tracing/eventpipe/randomizedallocationsampling/manual/AllocationProfiler/Program.cs`** -> AI Confidence: **99.31%**
1876. **`src/tests/tracing/runtimeeventsource/NativeRuntimeEventSourceTest.cs`** -> AI Confidence: **99.31%**
1877. **`src/tools/StressLogAnalyzer/src/Program.cs`** -> AI Confidence: **99.31%**
1878. **`src/tools/ilasm/src/ILAssembler/GrammarVisitor.cs`** -> AI Confidence: **99.31%**
1879. **`src/tools/ilasm/src/ILAssembler/VTableExportPEBuilder.cs`** -> AI Confidence: **99.31%**
1880. **`src/tools/ilasm/src/ilasm/Program.cs`** -> AI Confidence: **99.31%**
1881. **`src/tools/illink/external/Mono.Options/Options.cs`** -> AI Confidence: **99.31%**
1882. **`src/tools/illink/src/ILLink.RoslynAnalyzer/DataFlow/ControlFlowGraphProxy.cs`** -> AI Confidence: **99.31%**
1883. **`src/tools/illink/src/ILLink.RoslynAnalyzer/DataFlow/LocalDataFlowVisitor.cs`** -> AI Confidence: **99.31%**
1884. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/HandleCallAction.cs`** -> AI Confidence: **99.31%**
1885. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/ReflectionAccessAnalyzer.cs`** -> AI Confidence: **99.31%**
1886. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/TrimDataFlowAnalysis.cs`** -> AI Confidence: **99.31%**
1887. **`src/tools/illink/src/ILLink.Shared/TrimAnalysis/HandleCallAction.cs`** -> AI Confidence: **99.31%**
1888. **`src/tools/illink/src/ILLink.Tasks/CreateRuntimeRootDescriptorFile.cs`** -> AI Confidence: **99.31%**
1889. **`src/tools/illink/src/linker/Linker.Dataflow/FlowAnnotations.cs`** -> AI Confidence: **99.31%**
1890. **`src/tools/illink/src/linker/Linker.Dataflow/HandleCallAction.cs`** -> AI Confidence: **99.31%**
1891. **`src/tools/illink/src/linker/Linker.Dataflow/MethodBodyScanner.cs`** -> AI Confidence: **99.31%**
1892. **`src/tools/illink/src/linker/Linker.Dataflow/ReflectionMarker.cs`** -> AI Confidence: **99.31%**
1893. **`src/tools/illink/src/linker/Linker.Steps/DescriptorMarker.cs`** -> AI Confidence: **99.31%**
1894. **`src/tools/illink/src/linker/Linker.Steps/LinkAttributesParser.cs`** -> AI Confidence: **99.31%**
1895. **`src/tools/illink/src/linker/Linker.Steps/MarkStep.cs`** -> AI Confidence: **99.31%**
1896. **`src/tools/illink/src/linker/Linker.Steps/ProcessLinkerXmlBase.cs`** -> AI Confidence: **99.31%**
1897. **`src/tools/illink/src/linker/Linker.Steps/UnreachableBlocksOptimizer.cs`** -> AI Confidence: **99.31%**
1898. **`src/tools/illink/src/linker/Linker/DocumentationSignatureParser.cs`** -> AI Confidence: **99.31%**
1899. **`src/tools/illink/src/linker/Linker/Driver.cs`** -> AI Confidence: **99.31%**
1900. **`src/tools/illink/src/linker/Linker/LinkerAttributesInformation.cs`** -> AI Confidence: **99.31%**
1901. **`src/tools/illink/src/linker/Linker/MessageContainer.cs`** -> AI Confidence: **99.31%**
1902. **`src/tools/illink/src/linker/Linker/TypeReferenceExtensions.cs`** -> AI Confidence: **99.31%**
1903. **`src/tools/illink/test/Mono.Linker.Tests.Cases/RequiresCapability/RequiresAccessedThrough.cs`** -> AI Confidence: **99.31%**
1904. **`src/tools/illink/test/Mono.Linker.Tests/TestCasesRunner/MemberAssertionsCollector.cs`** -> AI Confidence: **99.31%**
1905. **`src/tools/illink/test/Mono.Linker.Tests/TestCasesRunner/ResultChecker.cs`** -> AI Confidence: **99.31%**
1906. **`src/mono/browser/runtime/assets.ts`** -> AI Confidence: **99.31%**
1907. **`src/mono/browser/runtime/diagnostics/diagnostics-js.ts`** -> AI Confidence: **99.31%**
1908. **`src/mono/browser/runtime/http.ts`** -> AI Confidence: **99.31%**
1909. **`src/mono/browser/runtime/invoke-js.ts`** -> AI Confidence: **99.31%**
1910. **`src/mono/browser/runtime/jiterpreter-interp-entry.ts`** -> AI Confidence: **99.31%**
1911. **`src/mono/browser/runtime/jiterpreter-jit-call.ts`** -> AI Confidence: **99.31%**
1912. **`src/mono/browser/runtime/jiterpreter-support.ts`** -> AI Confidence: **99.31%**
1913. **`src/mono/browser/runtime/jiterpreter.ts`** -> AI Confidence: **99.31%**
1914. **`src/mono/browser/runtime/loader/assets.ts`** -> AI Confidence: **99.31%**
1915. **`src/mono/browser/runtime/loader/run.ts`** -> AI Confidence: **99.31%**
1916. **`src/mono/browser/runtime/marshal-to-js.ts`** -> AI Confidence: **99.31%**
1917. **`src/mono/browser/runtime/pthreads/shared.ts`** -> AI Confidence: **99.31%**
1918. **`src/mono/browser/runtime/run.ts`** -> AI Confidence: **99.31%**
1919. **`src/mono/browser/runtime/web-socket.ts`** -> AI Confidence: **99.31%**
1920. **`src/native/libs/Common/JavaScript/loader/assets.ts`** -> AI Confidence: **99.31%**
1921. **`src/native/libs/System.Native.Browser/diagnostics/diagnostic-server-js.ts`** -> AI Confidence: **99.31%**
1922. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/http.ts`** -> AI Confidence: **99.31%**
1923. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/invoke-cs.ts`** -> AI Confidence: **99.31%**
1924. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/marshal-to-js.ts`** -> AI Confidence: **99.31%**
1925. **`src/native/libs/System.Runtime.InteropServices.JavaScript.Native/interop/web-socket.ts`** -> AI Confidence: **99.31%**
1926. **`.devcontainer/scripts/onCreateCommand.sh`** -> AI Confidence: **99.29%**
1927. **`.devcontainer/scripts/postCreateCommand.sh`** -> AI Confidence: **99.29%**
1928. **`eng/common/init-tools-native.sh`** -> AI Confidence: **99.29%**
1929. **`eng/common/native/init-compiler.sh`** -> AI Confidence: **99.29%**
1930. **`eng/common/native/init-distro-rid.sh`** -> AI Confidence: **99.29%**
1931. **`eng/native/genmoduleindex.sh`** -> AI Confidence: **99.29%**
1932. **`eng/testing/AndroidRunnerTemplate.sh`** -> AI Confidence: **99.29%**
1933. **`eng/testing/AppleRunnerTemplate.sh`** -> AI Confidence: **99.29%**
1934. **`eng/testing/BionicRunnerTemplate.sh`** -> AI Confidence: **99.29%**
1935. **`eng/testing/RunnerTemplate.sh`** -> AI Confidence: **99.29%**
1936. **`eng/testing/WasiRunnerTemplate.sh`** -> AI Confidence: **99.29%**
1937. **`eng/testing/WasmRunnerTemplate.sh`** -> AI Confidence: **99.29%**
1938. **`src/coreclr/enablesanitizers.sh`** -> AI Confidence: **99.29%**
1939. **`src/coreclr/generateredefinesfile.sh`** -> AI Confidence: **99.29%**
1940. **`src/coreclr/nativeresources/processrc.sh`** -> AI Confidence: **99.29%**
1941. **`src/coreclr/pal/tools/gen-dactable-rva.sh`** -> AI Confidence: **99.29%**
1942. **`src/coreclr/pal/tools/setup-ubuntuvm.sh`** -> AI Confidence: **99.29%**
1943. **`src/coreclr/pal/tools/smarty.sh`** -> AI Confidence: **99.29%**
1944. **`src/coreclr/run-cppcheck.sh`** -> AI Confidence: **99.29%**
1945. **`src/libraries/Common/tests/System/Net/EnterpriseTests/setup/apacheweb/run.sh`** -> AI Confidence: **99.29%**
1946. **`src/libraries/Common/tests/System/Net/StressTests/build-local.sh`** -> AI Confidence: **99.29%**
1947. **`src/libraries/System.Security.Cryptography/tests/osslplugins/build.sh`** -> AI Confidence: **99.29%**
1948. **`src/mono/mono/arch/arm/dpiops.sh`** -> AI Confidence: **99.29%**
1949. **`src/mono/mono/arch/arm/vfpops.sh`** -> AI Confidence: **99.29%**
1950. **`src/mono/mono/eglib/test/test-both`** -> AI Confidence: **99.29%**
1951. **`src/mono/mono/eglib/test/whats-implemented`** -> AI Confidence: **99.29%**
1952. **`src/mono/mono/tests/verifier/make_access_test.sh`** -> AI Confidence: **99.29%**
1953. **`src/mono/mono/tests/verifier/make_bad_op_test.sh`** -> AI Confidence: **99.29%**
1954. **`src/mono/mono/tests/verifier/make_bin_test.sh`** -> AI Confidence: **99.29%**
1955. **`src/mono/mono/tests/verifier/make_bool_branch_test.sh`** -> AI Confidence: **99.29%**
1956. **`src/mono/mono/tests/verifier/make_boxed_genarg_test.sh`** -> AI Confidence: **99.29%**
1957. **`src/mono/mono/tests/verifier/make_branch_test.sh`** -> AI Confidence: **99.29%**
1958. **`src/mono/mono/tests/verifier/make_call_test.sh`** -> AI Confidence: **99.29%**
1959. **`src/mono/mono/tests/verifier/make_cast_test.sh`** -> AI Confidence: **99.29%**
1960. **`src/mono/mono/tests/verifier/make_cmmp_test.sh`** -> AI Confidence: **99.29%**
1961. **`src/mono/mono/tests/verifier/make_constrained_test.sh`** -> AI Confidence: **99.29%**
1962. **`src/mono/mono/tests/verifier/make_cross_nested_access_test.sh`** -> AI Confidence: **99.29%**
1963. **`src/mono/mono/tests/verifier/make_ctor_test.sh`** -> AI Confidence: **99.29%**
1964. **`src/mono/mono/tests/verifier/make_delegate_compat_test.sh`** -> AI Confidence: **99.29%**
1965. **`src/mono/mono/tests/verifier/make_delegate_test.sh`** -> AI Confidence: **99.29%**
1966. **`src/mono/mono/tests/verifier/make_double_nesting_test.sh`** -> AI Confidence: **99.29%**
1967. **`src/mono/mono/tests/verifier/make_endfinally_test.sh`** -> AI Confidence: **99.29%**
1968. **`src/mono/mono/tests/verifier/make_exception_branch_test.sh`** -> AI Confidence: **99.29%**
1969. **`src/mono/mono/tests/verifier/make_exception_overlap_test.sh`** -> AI Confidence: **99.29%**
1970. **`src/mono/mono/tests/verifier/make_field_store_test.sh`** -> AI Confidence: **99.29%**
1971. **`src/mono/mono/tests/verifier/make_field_valuetype_test.sh`** -> AI Confidence: **99.29%**
1972. **`src/mono/mono/tests/verifier/make_generic_argument_constraints_test.sh`** -> AI Confidence: **99.29%**
1973. **`src/mono/mono/tests/verifier/make_il_overflow_test.sh`** -> AI Confidence: **99.29%**
1974. **`src/mono/mono/tests/verifier/make_invalid_ret_type.sh`** -> AI Confidence: **99.29%**
1975. **`src/mono/mono/tests/verifier/make_ldelem_test.sh`** -> AI Confidence: **99.29%**
1976. **`src/mono/mono/tests/verifier/make_ldelema_test.sh`** -> AI Confidence: **99.29%**
1977. **`src/mono/mono/tests/verifier/make_ldlen_test.sh`** -> AI Confidence: **99.29%**
1978. **`src/mono/mono/tests/verifier/make_load_indirect_test.sh`** -> AI Confidence: **99.29%**
1979. **`src/mono/mono/tests/verifier/make_localloc_test.sh`** -> AI Confidence: **99.29%**
1980. **`src/mono/mono/tests/verifier/make_method_constraint_test.sh`** -> AI Confidence: **99.29%**
1981. **`src/mono/mono/tests/verifier/make_mkrefany.sh`** -> AI Confidence: **99.29%**
1982. **`src/mono/mono/tests/verifier/make_nested_access_test.sh`** -> AI Confidence: **99.29%**
1983. **`src/mono/mono/tests/verifier/make_newarr_test.sh`** -> AI Confidence: **99.29%**
1984. **`src/mono/mono/tests/verifier/make_newobj_test.sh`** -> AI Confidence: **99.29%**
1985. **`src/mono/mono/tests/verifier/make_obj_store_test.sh`** -> AI Confidence: **99.29%**
1986. **`src/mono/mono/tests/verifier/make_overlapped_test.sh`** -> AI Confidence: **99.29%**
1987. **`src/mono/mono/tests/verifier/make_prefix_test.sh`** -> AI Confidence: **99.29%**
1988. **`src/mono/mono/tests/verifier/make_rethrow_test.sh`** -> AI Confidence: **99.29%**
1989. **`src/mono/mono/tests/verifier/make_self_nested_test.sh`** -> AI Confidence: **99.29%**
1990. **`src/mono/mono/tests/verifier/make_stelem_test.sh`** -> AI Confidence: **99.29%**
1991. **`src/mono/mono/tests/verifier/make_store_indirect_test.sh`** -> AI Confidence: **99.29%**
1992. **`src/mono/mono/tests/verifier/make_switch_test.sh`** -> AI Confidence: **99.29%**
1993. **`src/mono/mono/tests/verifier/make_tail_call_test.sh`** -> AI Confidence: **99.29%**
1994. **`src/mono/mono/tests/verifier/make_tests.sh`** -> AI Confidence: **99.29%**
1995. **`src/mono/mono/tests/verifier/make_throw_test.sh`** -> AI Confidence: **99.29%**
1996. **`src/mono/mono/tests/verifier/make_type_constraint_test.sh`** -> AI Confidence: **99.29%**
1997. **`src/mono/mono/tests/verifier/make_type_visibility_test.sh`** -> AI Confidence: **99.29%**
1998. **`src/mono/mono/tests/verifier/make_unbox_any_test.sh`** -> AI Confidence: **99.29%**
1999. **`src/mono/mono/tests/verifier/make_unbox_test.sh`** -> AI Confidence: **99.29%**
2000. **`src/mono/sample/HelloWorld/aot_helloWorld_app.sh`** -> AI Confidence: **99.29%**
2001. **`src/native/external/libunwind/scripts/qemu-test-driver`** -> AI Confidence: **99.29%**
2002. **`src/native/external/libunwind/tests/check-namespace.sh.in`** -> AI Confidence: **99.29%**
2003. **`src/native/libs/build-native.sh`** -> AI Confidence: **99.29%**
2004. **`src/native/libs/verify-entrypoints.sh`** -> AI Confidence: **99.29%**
2005. **`src/native/libs/verify-so.sh`** -> AI Confidence: **99.29%**
2006. **`eng/collect_vsinfo.ps1`** -> AI Confidence: **99.29%**
2007. **`eng/common/dotnet-install.ps1`** -> AI Confidence: **99.29%**
2008. **`eng/common/dotnet.ps1`** -> AI Confidence: **99.29%**
2009. **`eng/common/generate-locproject.ps1`** -> AI Confidence: **99.29%**
2010. **`eng/common/init-tools-native.ps1`** -> AI Confidence: **99.29%**
2011. **`eng/common/internal-feed-operations.ps1`** -> AI Confidence: **99.29%**
2012. **`eng/common/pipeline-logging-functions.ps1`** -> AI Confidence: **99.29%**
2013. **`eng/common/sdk-task.ps1`** -> AI Confidence: **99.29%**
2014. **`eng/common/tools.ps1`** -> AI Confidence: **99.29%**
2015. **`eng/common/vmr-sync.ps1`** -> AI Confidence: **99.29%**
2016. **`eng/download-wasi-sdk.ps1`** -> AI Confidence: **99.29%**
2017. **`eng/extract-for-crossdac.ps1`** -> AI Confidence: **99.29%**
2018. **`eng/native/generateversionscript.ps1`** -> AI Confidence: **99.29%**
2019. **`eng/native/sign-with-dac-certificate.ps1`** -> AI Confidence: **99.29%**
2020. **`eng/native/version/copy_version_files.ps1`** -> AI Confidence: **99.29%**
2021. **`eng/pipelines/mono/update-machine-certs.ps1`** -> AI Confidence: **99.29%**
2022. **`src/libraries/Common/tests/Scripts/Tools/ParallelTestExecution.ps1`** -> AI Confidence: **99.29%**
2023. **`src/libraries/Common/tests/System/Net/StressTests/build-local.ps1`** -> AI Confidence: **99.29%**
2024. **`src/libraries/Common/tests/System/Net/StressTests/run-docker-compose.ps1`** -> AI Confidence: **99.29%**
2025. **`src/libraries/Fuzzing/DotnetFuzzing/collect-coverage.ps1`** -> AI Confidence: **99.29%**
2026. **`src/libraries/GenerateLibrariesSln.ps1`** -> AI Confidence: **99.29%**
2027. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/entrypoint.ps1`** -> AI Confidence: **99.29%**
2028. **`src/libraries/System.Net.Security/tests/StressTests/SslStress/entrypoint.ps1`** -> AI Confidence: **99.29%**
2029. **`src/native/managed/cdac/scripts/cdac-dump-inspect.ps1`** -> AI Confidence: **99.29%**
2030. **`src/native/managed/cdac/tests/StressTests/RunStressTests.ps1`** -> AI Confidence: **99.29%**
2031. **`src/coreclr/inc/log.h`** -> AI Confidence: **99.29%**
2032. **`src/mono/mono/metadata/gc-stats.c`** -> AI Confidence: **99.29%**
2033. **`src/mono/mono/mini/branch-opts.c`** -> AI Confidence: **99.29%**
2034. **`src/mono/mono/mini/mini-arm64-gsharedvt.c`** -> AI Confidence: **99.29%**
2035. **`src/mono/mono/mini/mini-x86-gsharedvt.c`** -> AI Confidence: **99.29%**
2036. **`src/mono/mono/mini/tramp-x86-gsharedvt.c`** -> AI Confidence: **99.29%**
2037. **`src/mono/mono/sgen/sgen-qsort.h`** -> AI Confidence: **99.29%**
2038. **`src/mono/mono/utils/mono-hwcap-ppc.c`** -> AI Confidence: **99.29%**
2039. **`src/mono/mono/utils/mono-log-android.c`** -> AI Confidence: **99.29%**
2040. **`src/mono/mono/utils/mono-os-semaphore-win32.c`** -> AI Confidence: **99.29%**
2041. **`src/native/eventpipe/ds-portable-rid.c`** -> AI Confidence: **99.29%**
2042. **`src/native/external/brotli/c/enc/command.c`** -> AI Confidence: **99.29%**
2043. **`src/native/external/brotli/c/enc/fast_log.c`** -> AI Confidence: **99.29%**
2044. **`src/native/external/brotli/c/enc/utf8_util.c`** -> AI Confidence: **99.29%**
2045. **`src/native/external/libunwind/src/aarch64/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2046. **`src/native/external/libunwind/src/aarch64/Gregs.c`** -> AI Confidence: **99.29%**
2047. **`src/native/external/libunwind/src/aarch64/Gstash_frame.c`** -> AI Confidence: **99.29%**
2048. **`src/native/external/libunwind/src/aarch64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2049. **`src/native/external/libunwind/src/aarch64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2050. **`src/native/external/libunwind/src/aarch64/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2051. **`src/native/external/libunwind/src/aarch64/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2052. **`src/native/external/libunwind/src/aarch64/Lglobal.c`** -> AI Confidence: **99.29%**
2053. **`src/native/external/libunwind/src/aarch64/Linit.c`** -> AI Confidence: **99.29%**
2054. **`src/native/external/libunwind/src/aarch64/Linit_local.c`** -> AI Confidence: **99.29%**
2055. **`src/native/external/libunwind/src/aarch64/Linit_remote.c`** -> AI Confidence: **99.29%**
2056. **`src/native/external/libunwind/src/aarch64/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2057. **`src/native/external/libunwind/src/aarch64/Los-freebsd.c`** -> AI Confidence: **99.29%**
2058. **`src/native/external/libunwind/src/aarch64/Los-linux.c`** -> AI Confidence: **99.29%**
2059. **`src/native/external/libunwind/src/aarch64/Los-qnx.c`** -> AI Confidence: **99.29%**
2060. **`src/native/external/libunwind/src/aarch64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2061. **`src/native/external/libunwind/src/aarch64/Lregs.c`** -> AI Confidence: **99.29%**
2062. **`src/native/external/libunwind/src/aarch64/Lresume.c`** -> AI Confidence: **99.29%**
2063. **`src/native/external/libunwind/src/aarch64/Lstash_frame.c`** -> AI Confidence: **99.29%**
2064. **`src/native/external/libunwind/src/aarch64/Lstep.c`** -> AI Confidence: **99.29%**
2065. **`src/native/external/libunwind/src/aarch64/Ltrace.c`** -> AI Confidence: **99.29%**
2066. **`src/native/external/libunwind/src/aarch64/ucontext_i.h`** -> AI Confidence: **99.29%**
2067. **`src/native/external/libunwind/src/arm/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2068. **`src/native/external/libunwind/src/arm/Gregs.c`** -> AI Confidence: **99.29%**
2069. **`src/native/external/libunwind/src/arm/Gstash_frame.c`** -> AI Confidence: **99.29%**
2070. **`src/native/external/libunwind/src/arm/Gtrace.c`** -> AI Confidence: **99.29%**
2071. **`src/native/external/libunwind/src/arm/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2072. **`src/native/external/libunwind/src/arm/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2073. **`src/native/external/libunwind/src/arm/Lex_tables.c`** -> AI Confidence: **99.29%**
2074. **`src/native/external/libunwind/src/arm/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2075. **`src/native/external/libunwind/src/arm/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2076. **`src/native/external/libunwind/src/arm/Lglobal.c`** -> AI Confidence: **99.29%**
2077. **`src/native/external/libunwind/src/arm/Linit.c`** -> AI Confidence: **99.29%**
2078. **`src/native/external/libunwind/src/arm/Linit_local.c`** -> AI Confidence: **99.29%**
2079. **`src/native/external/libunwind/src/arm/Linit_remote.c`** -> AI Confidence: **99.29%**
2080. **`src/native/external/libunwind/src/arm/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2081. **`src/native/external/libunwind/src/arm/Los-freebsd.c`** -> AI Confidence: **99.29%**
2082. **`src/native/external/libunwind/src/arm/Los-linux.c`** -> AI Confidence: **99.29%**
2083. **`src/native/external/libunwind/src/arm/Los-other.c`** -> AI Confidence: **99.29%**
2084. **`src/native/external/libunwind/src/arm/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2085. **`src/native/external/libunwind/src/arm/Lregs.c`** -> AI Confidence: **99.29%**
2086. **`src/native/external/libunwind/src/arm/Lresume.c`** -> AI Confidence: **99.29%**
2087. **`src/native/external/libunwind/src/arm/Lstash_frame.c`** -> AI Confidence: **99.29%**
2088. **`src/native/external/libunwind/src/arm/Lstep.c`** -> AI Confidence: **99.29%**
2089. **`src/native/external/libunwind/src/arm/Ltrace.c`** -> AI Confidence: **99.29%**
2090. **`src/native/external/libunwind/src/arm/is_fpreg.c`** -> AI Confidence: **99.29%**
2091. **`src/native/external/libunwind/src/coredump/_UCD_access_reg_freebsd.c`** -> AI Confidence: **99.29%**
2092. **`src/native/external/libunwind/src/coredump/_UCD_access_reg_qnx.c`** -> AI Confidence: **99.29%**
2093. **`src/native/external/libunwind/src/dwarf/Gexpr.c`** -> AI Confidence: **99.29%**
2094. **`src/native/external/libunwind/src/dwarf/Lexpr.c`** -> AI Confidence: **99.29%**
2095. **`src/native/external/libunwind/src/dwarf/Lfde.c`** -> AI Confidence: **99.29%**
2096. **`src/native/external/libunwind/src/dwarf/Lfind_proc_info-lsb.c`** -> AI Confidence: **99.29%**
2097. **`src/native/external/libunwind/src/dwarf/Lfind_unwind_table.c`** -> AI Confidence: **99.29%**
2098. **`src/native/external/libunwind/src/dwarf/Lget_proc_info_in_range.c`** -> AI Confidence: **99.29%**
2099. **`src/native/external/libunwind/src/dwarf/Lparser.c`** -> AI Confidence: **99.29%**
2100. **`src/native/external/libunwind/src/dwarf/Lpe.c`** -> AI Confidence: **99.29%**
2101. **`src/native/external/libunwind/src/hppa/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2102. **`src/native/external/libunwind/src/hppa/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2103. **`src/native/external/libunwind/src/hppa/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2104. **`src/native/external/libunwind/src/hppa/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2105. **`src/native/external/libunwind/src/hppa/Lglobal.c`** -> AI Confidence: **99.29%**
2106. **`src/native/external/libunwind/src/hppa/Linit.c`** -> AI Confidence: **99.29%**
2107. **`src/native/external/libunwind/src/hppa/Linit_local.c`** -> AI Confidence: **99.29%**
2108. **`src/native/external/libunwind/src/hppa/Linit_remote.c`** -> AI Confidence: **99.29%**
2109. **`src/native/external/libunwind/src/hppa/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2110. **`src/native/external/libunwind/src/hppa/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2111. **`src/native/external/libunwind/src/hppa/Lregs.c`** -> AI Confidence: **99.29%**
2112. **`src/native/external/libunwind/src/hppa/Lresume.c`** -> AI Confidence: **99.29%**
2113. **`src/native/external/libunwind/src/hppa/Lstep.c`** -> AI Confidence: **99.29%**
2114. **`src/native/external/libunwind/src/ia64/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2115. **`src/native/external/libunwind/src/ia64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2116. **`src/native/external/libunwind/src/ia64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2117. **`src/native/external/libunwind/src/ia64/Lfind_unwind_table.c`** -> AI Confidence: **99.29%**
2118. **`src/native/external/libunwind/src/ia64/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2119. **`src/native/external/libunwind/src/ia64/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2120. **`src/native/external/libunwind/src/ia64/Lglobal.c`** -> AI Confidence: **99.29%**
2121. **`src/native/external/libunwind/src/ia64/Linit.c`** -> AI Confidence: **99.29%**
2122. **`src/native/external/libunwind/src/ia64/Linit_local.c`** -> AI Confidence: **99.29%**
2123. **`src/native/external/libunwind/src/ia64/Linit_remote.c`** -> AI Confidence: **99.29%**
2124. **`src/native/external/libunwind/src/ia64/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2125. **`src/native/external/libunwind/src/ia64/Lparser.c`** -> AI Confidence: **99.29%**
2126. **`src/native/external/libunwind/src/ia64/Lrbs.c`** -> AI Confidence: **99.29%**
2127. **`src/native/external/libunwind/src/ia64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2128. **`src/native/external/libunwind/src/ia64/Lregs.c`** -> AI Confidence: **99.29%**
2129. **`src/native/external/libunwind/src/ia64/Lresume.c`** -> AI Confidence: **99.29%**
2130. **`src/native/external/libunwind/src/ia64/Lscript.c`** -> AI Confidence: **99.29%**
2131. **`src/native/external/libunwind/src/ia64/Lstep.c`** -> AI Confidence: **99.29%**
2132. **`src/native/external/libunwind/src/ia64/Ltables.c`** -> AI Confidence: **99.29%**
2133. **`src/native/external/libunwind/src/loongarch64/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2134. **`src/native/external/libunwind/src/loongarch64/Gregs.c`** -> AI Confidence: **99.29%**
2135. **`src/native/external/libunwind/src/loongarch64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2136. **`src/native/external/libunwind/src/loongarch64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2137. **`src/native/external/libunwind/src/loongarch64/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2138. **`src/native/external/libunwind/src/loongarch64/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2139. **`src/native/external/libunwind/src/loongarch64/Lglobal.c`** -> AI Confidence: **99.29%**
2140. **`src/native/external/libunwind/src/loongarch64/Linit.c`** -> AI Confidence: **99.29%**
2141. **`src/native/external/libunwind/src/loongarch64/Linit_local.c`** -> AI Confidence: **99.29%**
2142. **`src/native/external/libunwind/src/loongarch64/Linit_remote.c`** -> AI Confidence: **99.29%**
2143. **`src/native/external/libunwind/src/loongarch64/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2144. **`src/native/external/libunwind/src/loongarch64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2145. **`src/native/external/libunwind/src/loongarch64/Lregs.c`** -> AI Confidence: **99.29%**
2146. **`src/native/external/libunwind/src/loongarch64/Lresume.c`** -> AI Confidence: **99.29%**
2147. **`src/native/external/libunwind/src/loongarch64/Lstep.c`** -> AI Confidence: **99.29%**
2148. **`src/native/external/libunwind/src/mi/Gput_dynamic_unwind_info.c`** -> AI Confidence: **99.29%**
2149. **`src/native/external/libunwind/src/mi/Gset_iterate_phdr_function.c`** -> AI Confidence: **99.29%**
2150. **`src/native/external/libunwind/src/mi/Laddress_validator.c`** -> AI Confidence: **99.29%**
2151. **`src/native/external/libunwind/src/mi/Ldestroy_addr_space.c`** -> AI Confidence: **99.29%**
2152. **`src/native/external/libunwind/src/mi/Ldyn-extract.c`** -> AI Confidence: **99.29%**
2153. **`src/native/external/libunwind/src/mi/Ldyn-remote.c`** -> AI Confidence: **99.29%**
2154. **`src/native/external/libunwind/src/mi/Lfind_dynamic_proc_info.c`** -> AI Confidence: **99.29%**
2155. **`src/native/external/libunwind/src/mi/Lget_accessors.c`** -> AI Confidence: **99.29%**
2156. **`src/native/external/libunwind/src/mi/Lget_elf_filename.c`** -> AI Confidence: **99.29%**
2157. **`src/native/external/libunwind/src/mi/Lget_fpreg.c`** -> AI Confidence: **99.29%**
2158. **`src/native/external/libunwind/src/mi/Lget_proc_info_by_ip.c`** -> AI Confidence: **99.29%**
2159. **`src/native/external/libunwind/src/mi/Lget_proc_name.c`** -> AI Confidence: **99.29%**
2160. **`src/native/external/libunwind/src/mi/Lget_reg.c`** -> AI Confidence: **99.29%**
2161. **`src/native/external/libunwind/src/mi/Lput_dynamic_unwind_info.c`** -> AI Confidence: **99.29%**
2162. **`src/native/external/libunwind/src/mi/Lset_cache_size.c`** -> AI Confidence: **99.29%**
2163. **`src/native/external/libunwind/src/mi/Lset_caching_policy.c`** -> AI Confidence: **99.29%**
2164. **`src/native/external/libunwind/src/mi/Lset_fpreg.c`** -> AI Confidence: **99.29%**
2165. **`src/native/external/libunwind/src/mi/Lset_iterate_phdr_function.c`** -> AI Confidence: **99.29%**
2166. **`src/native/external/libunwind/src/mi/Lset_reg.c`** -> AI Confidence: **99.29%**
2167. **`src/native/external/libunwind/src/mi/_ReadSLEB.c`** -> AI Confidence: **99.29%**
2168. **`src/native/external/libunwind/src/mi/strerror.c`** -> AI Confidence: **99.29%**
2169. **`src/native/external/libunwind/src/mips/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2170. **`src/native/external/libunwind/src/mips/Gregs.c`** -> AI Confidence: **99.29%**
2171. **`src/native/external/libunwind/src/mips/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2172. **`src/native/external/libunwind/src/mips/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2173. **`src/native/external/libunwind/src/mips/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2174. **`src/native/external/libunwind/src/mips/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2175. **`src/native/external/libunwind/src/mips/Lglobal.c`** -> AI Confidence: **99.29%**
2176. **`src/native/external/libunwind/src/mips/Linit.c`** -> AI Confidence: **99.29%**
2177. **`src/native/external/libunwind/src/mips/Linit_local.c`** -> AI Confidence: **99.29%**
2178. **`src/native/external/libunwind/src/mips/Linit_remote.c`** -> AI Confidence: **99.29%**
2179. **`src/native/external/libunwind/src/mips/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2180. **`src/native/external/libunwind/src/mips/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2181. **`src/native/external/libunwind/src/mips/Lregs.c`** -> AI Confidence: **99.29%**
2182. **`src/native/external/libunwind/src/mips/Lresume.c`** -> AI Confidence: **99.29%**
2183. **`src/native/external/libunwind/src/mips/Lstep.c`** -> AI Confidence: **99.29%**
2184. **`src/native/external/libunwind/src/mips/offsets.h`** -> AI Confidence: **99.29%**
2185. **`src/native/external/libunwind/src/ppc/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2186. **`src/native/external/libunwind/src/ppc/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2187. **`src/native/external/libunwind/src/ppc/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2188. **`src/native/external/libunwind/src/ppc/Linit_local.c`** -> AI Confidence: **99.29%**
2189. **`src/native/external/libunwind/src/ppc/Linit_remote.c`** -> AI Confidence: **99.29%**
2190. **`src/native/external/libunwind/src/ppc/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2191. **`src/native/external/libunwind/src/ppc/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2192. **`src/native/external/libunwind/src/ppc32/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2193. **`src/native/external/libunwind/src/ppc32/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2194. **`src/native/external/libunwind/src/ppc32/Lglobal.c`** -> AI Confidence: **99.29%**
2195. **`src/native/external/libunwind/src/ppc32/Linit.c`** -> AI Confidence: **99.29%**
2196. **`src/native/external/libunwind/src/ppc32/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2197. **`src/native/external/libunwind/src/ppc32/Lregs.c`** -> AI Confidence: **99.29%**
2198. **`src/native/external/libunwind/src/ppc32/Lresume.c`** -> AI Confidence: **99.29%**
2199. **`src/native/external/libunwind/src/ppc32/Lstep.c`** -> AI Confidence: **99.29%**
2200. **`src/native/external/libunwind/src/ppc64/Gregs.c`** -> AI Confidence: **99.29%**
2201. **`src/native/external/libunwind/src/ppc64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2202. **`src/native/external/libunwind/src/ppc64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2203. **`src/native/external/libunwind/src/ppc64/Lglobal.c`** -> AI Confidence: **99.29%**
2204. **`src/native/external/libunwind/src/ppc64/Linit.c`** -> AI Confidence: **99.29%**
2205. **`src/native/external/libunwind/src/ppc64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2206. **`src/native/external/libunwind/src/ppc64/Lregs.c`** -> AI Confidence: **99.29%**
2207. **`src/native/external/libunwind/src/ppc64/Lresume.c`** -> AI Confidence: **99.29%**
2208. **`src/native/external/libunwind/src/ppc64/Lstep.c`** -> AI Confidence: **99.29%**
2209. **`src/native/external/libunwind/src/riscv/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2210. **`src/native/external/libunwind/src/riscv/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2211. **`src/native/external/libunwind/src/riscv/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2212. **`src/native/external/libunwind/src/riscv/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2213. **`src/native/external/libunwind/src/riscv/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2214. **`src/native/external/libunwind/src/riscv/Lglobal.c`** -> AI Confidence: **99.29%**
2215. **`src/native/external/libunwind/src/riscv/Linit.c`** -> AI Confidence: **99.29%**
2216. **`src/native/external/libunwind/src/riscv/Linit_local.c`** -> AI Confidence: **99.29%**
2217. **`src/native/external/libunwind/src/riscv/Linit_remote.c`** -> AI Confidence: **99.29%**
2218. **`src/native/external/libunwind/src/riscv/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2219. **`src/native/external/libunwind/src/riscv/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2220. **`src/native/external/libunwind/src/riscv/Lregs.c`** -> AI Confidence: **99.29%**
2221. **`src/native/external/libunwind/src/riscv/Lresume.c`** -> AI Confidence: **99.29%**
2222. **`src/native/external/libunwind/src/riscv/Lstep.c`** -> AI Confidence: **99.29%**
2223. **`src/native/external/libunwind/src/riscv/asm.h`** -> AI Confidence: **99.29%**
2224. **`src/native/external/libunwind/src/riscv/offsets.h`** -> AI Confidence: **99.29%**
2225. **`src/native/external/libunwind/src/s390x/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2226. **`src/native/external/libunwind/src/s390x/Gregs.c`** -> AI Confidence: **99.29%**
2227. **`src/native/external/libunwind/src/s390x/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2228. **`src/native/external/libunwind/src/s390x/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2229. **`src/native/external/libunwind/src/s390x/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2230. **`src/native/external/libunwind/src/s390x/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2231. **`src/native/external/libunwind/src/s390x/Linit.c`** -> AI Confidence: **99.29%**
2232. **`src/native/external/libunwind/src/s390x/Linit_local.c`** -> AI Confidence: **99.29%**
2233. **`src/native/external/libunwind/src/s390x/Linit_remote.c`** -> AI Confidence: **99.29%**
2234. **`src/native/external/libunwind/src/s390x/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2235. **`src/native/external/libunwind/src/s390x/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2236. **`src/native/external/libunwind/src/s390x/Lregs.c`** -> AI Confidence: **99.29%**
2237. **`src/native/external/libunwind/src/s390x/Lresume.c`** -> AI Confidence: **99.29%**
2238. **`src/native/external/libunwind/src/s390x/Lstep.c`** -> AI Confidence: **99.29%**
2239. **`src/native/external/libunwind/src/setjmp/siglongjmp.c`** -> AI Confidence: **99.29%**
2240. **`src/native/external/libunwind/src/sh/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2241. **`src/native/external/libunwind/src/sh/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2242. **`src/native/external/libunwind/src/sh/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2243. **`src/native/external/libunwind/src/sh/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2244. **`src/native/external/libunwind/src/sh/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2245. **`src/native/external/libunwind/src/sh/Lglobal.c`** -> AI Confidence: **99.29%**
2246. **`src/native/external/libunwind/src/sh/Linit.c`** -> AI Confidence: **99.29%**
2247. **`src/native/external/libunwind/src/sh/Linit_local.c`** -> AI Confidence: **99.29%**
2248. **`src/native/external/libunwind/src/sh/Linit_remote.c`** -> AI Confidence: **99.29%**
2249. **`src/native/external/libunwind/src/sh/Lis_signal_frame.c`** -> AI Confidence: **99.29%**
2250. **`src/native/external/libunwind/src/sh/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2251. **`src/native/external/libunwind/src/sh/Lregs.c`** -> AI Confidence: **99.29%**
2252. **`src/native/external/libunwind/src/sh/Lresume.c`** -> AI Confidence: **99.29%**
2253. **`src/native/external/libunwind/src/sh/Lstep.c`** -> AI Confidence: **99.29%**
2254. **`src/native/external/libunwind/src/x86/Gget_save_loc.c`** -> AI Confidence: **99.29%**
2255. **`src/native/external/libunwind/src/x86/Gregs.c`** -> AI Confidence: **99.29%**
2256. **`src/native/external/libunwind/src/x86/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2257. **`src/native/external/libunwind/src/x86/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2258. **`src/native/external/libunwind/src/x86/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2259. **`src/native/external/libunwind/src/x86/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2260. **`src/native/external/libunwind/src/x86/Lglobal.c`** -> AI Confidence: **99.29%**
2261. **`src/native/external/libunwind/src/x86/Linit.c`** -> AI Confidence: **99.29%**
2262. **`src/native/external/libunwind/src/x86/Linit_local.c`** -> AI Confidence: **99.29%**
2263. **`src/native/external/libunwind/src/x86/Linit_remote.c`** -> AI Confidence: **99.29%**
2264. **`src/native/external/libunwind/src/x86/Los-freebsd.c`** -> AI Confidence: **99.29%**
2265. **`src/native/external/libunwind/src/x86/Los-linux.c`** -> AI Confidence: **99.29%**
2266. **`src/native/external/libunwind/src/x86/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2267. **`src/native/external/libunwind/src/x86/Lregs.c`** -> AI Confidence: **99.29%**
2268. **`src/native/external/libunwind/src/x86/Lresume.c`** -> AI Confidence: **99.29%**
2269. **`src/native/external/libunwind/src/x86/Lstep.c`** -> AI Confidence: **99.29%**
2270. **`src/native/external/libunwind/src/x86/is_fpreg.c`** -> AI Confidence: **99.29%**
2271. **`src/native/external/libunwind/src/x86_64/Lapply_reg_state.c`** -> AI Confidence: **99.29%**
2272. **`src/native/external/libunwind/src/x86_64/Lcreate_addr_space.c`** -> AI Confidence: **99.29%**
2273. **`src/native/external/libunwind/src/x86_64/Lget_proc_info.c`** -> AI Confidence: **99.29%**
2274. **`src/native/external/libunwind/src/x86_64/Lget_save_loc.c`** -> AI Confidence: **99.29%**
2275. **`src/native/external/libunwind/src/x86_64/Linit.c`** -> AI Confidence: **99.29%**
2276. **`src/native/external/libunwind/src/x86_64/Linit_local.c`** -> AI Confidence: **99.29%**
2277. **`src/native/external/libunwind/src/x86_64/Linit_remote.c`** -> AI Confidence: **99.29%**
2278. **`src/native/external/libunwind/src/x86_64/Los-freebsd.c`** -> AI Confidence: **99.29%**
2279. **`src/native/external/libunwind/src/x86_64/Los-linux.c`** -> AI Confidence: **99.29%**
2280. **`src/native/external/libunwind/src/x86_64/Los-qnx.c`** -> AI Confidence: **99.29%**
2281. **`src/native/external/libunwind/src/x86_64/Los-solaris.c`** -> AI Confidence: **99.29%**
2282. **`src/native/external/libunwind/src/x86_64/Lreg_states_iterate.c`** -> AI Confidence: **99.29%**
2283. **`src/native/external/libunwind/src/x86_64/Lregs.c`** -> AI Confidence: **99.29%**
2284. **`src/native/external/libunwind/src/x86_64/Lresume.c`** -> AI Confidence: **99.29%**
2285. **`src/native/external/libunwind/src/x86_64/Lstash_frame.c`** -> AI Confidence: **99.29%**
2286. **`src/native/external/libunwind/src/x86_64/Lstep.c`** -> AI Confidence: **99.29%**
2287. **`src/native/external/libunwind/src/x86_64/Ltrace.c`** -> AI Confidence: **99.29%**
2288. **`src/native/external/libunwind/tests/Gia64-test-stack.c`** -> AI Confidence: **99.29%**
2289. **`src/native/external/libunwind/tests/Larm64-test-sve-signal.c`** -> AI Confidence: **99.29%**
2290. **`src/native/external/libunwind/tests/Lia64-test-nat.c`** -> AI Confidence: **99.29%**
2291. **`src/native/external/libunwind/tests/Lia64-test-rbs.c`** -> AI Confidence: **99.29%**
2292. **`src/native/external/libunwind/tests/Lia64-test-readonly.c`** -> AI Confidence: **99.29%**
2293. **`src/native/external/libunwind/tests/Lia64-test-stack.c`** -> AI Confidence: **99.29%**
2294. **`src/native/external/libunwind/tests/Lperf-simple.c`** -> AI Confidence: **99.29%**
2295. **`src/native/external/libunwind/tests/Lperf-trace.c`** -> AI Confidence: **99.29%**
2296. **`src/native/external/libunwind/tests/Ltest-bt.c`** -> AI Confidence: **99.29%**
2297. **`src/native/external/libunwind/tests/Ltest-concurrent.c`** -> AI Confidence: **99.29%**
2298. **`src/native/external/libunwind/tests/Ltest-dyn1.c`** -> AI Confidence: **99.29%**
2299. **`src/native/external/libunwind/tests/Ltest-exc.c`** -> AI Confidence: **99.29%**
2300. **`src/native/external/libunwind/tests/Ltest-nomalloc.c`** -> AI Confidence: **99.29%**
2301. **`src/native/external/libunwind/tests/Ltest-resume-sig-rt.c`** -> AI Confidence: **99.29%**
2302. **`src/native/external/libunwind/tests/Ltest-resume-sig.c`** -> AI Confidence: **99.29%**
2303. **`src/native/external/libunwind/tests/Ltest-trace.c`** -> AI Confidence: **99.29%**
2304. **`src/native/external/libunwind/tests/Lx64-test-dwarf-expressions.c`** -> AI Confidence: **99.29%**
2305. **`src/native/external/llvm-libunwind/src/assembly.h`** -> AI Confidence: **99.29%**
2306. **`src/native/external/zlib-ng/arch/arm/crc32_acle.c`** -> AI Confidence: **99.29%**
2307. **`src/native/external/zlib-ng/arch/riscv/chunkset_rvv.c`** -> AI Confidence: **99.29%**
2308. **`src/native/external/zlib-ng/cmake/detect-arch.c`** -> AI Confidence: **99.29%**
2309. **`src/native/external/zlib-ng/deflate_fast.c`** -> AI Confidence: **99.29%**
2310. **`src/native/external/zlib-ng/deflate_slow.c`** -> AI Confidence: **99.29%**
2311. **`src/native/external/zlib-ng/deflate_stored.c`** -> AI Confidence: **99.29%**
2312. **`src/native/external/zlib-ng/uncompr.c`** -> AI Confidence: **99.29%**
2313. **`src/native/external/zstd/lib/common/debug.c`** -> AI Confidence: **99.29%**
2314. **`src/native/external/zstd/lib/compress/zstd_double_fast.c`** -> AI Confidence: **99.29%**
2315. **`src/native/external/zstd/lib/compress/zstd_fast.c`** -> AI Confidence: **99.29%**
2316. **`src/native/libs/System.Security.Cryptography.Native.Android/pal_pbkdf2.c`** -> AI Confidence: **99.29%**
2317. **`src/native/libs/System.Security.Cryptography.Native.Apple/pal_ecc.c`** -> AI Confidence: **99.29%**
2318. **`src/native/libs/System.Security.Cryptography.Native/pal_ecc_import_export.c`** -> AI Confidence: **99.29%**
2319. **`src/coreclr/dlls/mscorrc/resource.h`** -> AI Confidence: **99.29%**
2320. **`src/coreclr/gc/gceesvr.cpp`** -> AI Confidence: **99.29%**
2321. **`src/coreclr/gc/memory.cpp`** -> AI Confidence: **99.29%**
2322. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.AVX2.int32_t.generated.cpp`** -> AI Confidence: **99.29%**
2323. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.AVX2.int64_t.generated.cpp`** -> AI Confidence: **99.29%**
2324. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.AVX512.int32_t.generated.cpp`** -> AI Confidence: **99.29%**
2325. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.AVX512.int64_t.generated.cpp`** -> AI Confidence: **99.29%**
2326. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.NEON.uint32_t.generated.cpp`** -> AI Confidence: **99.29%**
2327. **`src/coreclr/gc/vxsort/smallsort/bitonic_sort.scalar.uint64_t.generated.cpp`** -> AI Confidence: **99.29%**
2328. **`src/coreclr/gcdump/gcdump.cpp`** -> AI Confidence: **99.29%**
2329. **`src/coreclr/gcdump/i386/gcdumpx86.cpp`** -> AI Confidence: **99.29%**
2330. **`src/coreclr/gcinfo/gcinfodumper.cpp`** -> AI Confidence: **99.29%**
2331. **`src/coreclr/ilasm/assembler.cpp`** -> AI Confidence: **99.29%**
2332. **`src/coreclr/ilasm/grammar_after.cpp`** -> AI Confidence: **99.29%**
2333. **`src/coreclr/ilasm/main.cpp`** -> AI Confidence: **99.29%**
2334. **`src/coreclr/ilasm/writer.cpp`** -> AI Confidence: **99.29%**
2335. **`src/coreclr/inc/dacvars.h`** -> AI Confidence: **99.29%**
2336. **`src/coreclr/inc/formattype.cpp`** -> AI Confidence: **99.29%**
2337. **`src/coreclr/inc/vptr_list.h`** -> AI Confidence: **99.29%**
2338. **`src/coreclr/jit/buildstring.cpp`** -> AI Confidence: **99.29%**
2339. **`src/coreclr/jit/codegenwasm.cpp`** -> AI Confidence: **99.29%**
2340. **`src/coreclr/jit/debuginfo.cpp`** -> AI Confidence: **99.29%**
2341. **`src/coreclr/jit/decomposelongs.cpp`** -> AI Confidence: **99.29%**
2342. **`src/coreclr/jit/disasm.cpp`** -> AI Confidence: **99.29%**
2343. **`src/coreclr/jit/earlyprop.cpp`** -> AI Confidence: **99.29%**
2344. **`src/coreclr/jit/emitarm64sve.cpp`** -> AI Confidence: **99.29%**
2345. **`src/coreclr/jit/fgbasic.cpp`** -> AI Confidence: **99.29%**
2346. **`src/coreclr/jit/fgehopt.cpp`** -> AI Confidence: **99.29%**
2347. **`src/coreclr/jit/fgflow.cpp`** -> AI Confidence: **99.29%**
2348. **`src/coreclr/jit/fginline.cpp`** -> AI Confidence: **99.29%**
2349. **`src/coreclr/jit/fgopt.cpp`** -> AI Confidence: **99.29%**
2350. **`src/coreclr/jit/fgprofilesynthesis.cpp`** -> AI Confidence: **99.29%**
2351. **`src/coreclr/jit/gschecks.cpp`** -> AI Confidence: **99.29%**
2352. **`src/coreclr/jit/hwintrinsic.cpp`** -> AI Confidence: **99.29%**
2353. **`src/coreclr/jit/hwintrinsicarm64.cpp`** -> AI Confidence: **99.29%**
2354. **`src/coreclr/jit/hwintrinsiccodegenarm64.cpp`** -> AI Confidence: **99.29%**
2355. **`src/coreclr/jit/hwintrinsicxarch.cpp`** -> AI Confidence: **99.29%**
2356. **`src/coreclr/jit/importer.cpp`** -> AI Confidence: **99.29%**
2357. **`src/coreclr/jit/importercalls.cpp`** -> AI Confidence: **99.29%**
2358. **`src/coreclr/jit/jithashtable.cpp`** -> AI Confidence: **99.29%**
2359. **`src/coreclr/jit/jitmetadatalist.h`** -> AI Confidence: **99.29%**
2360. **`src/coreclr/jit/lclmorph.cpp`** -> AI Confidence: **99.29%**
2361. **`src/coreclr/jit/lowerxarch.cpp`** -> AI Confidence: **99.29%**
2362. **`src/coreclr/jit/lsrabuild.cpp`** -> AI Confidence: **99.29%**
2363. **`src/coreclr/jit/lsraxarch.cpp`** -> AI Confidence: **99.29%**
2364. **`src/coreclr/jit/morph.cpp`** -> AI Confidence: **99.29%**
2365. **`src/coreclr/jit/optimizer.cpp`** -> AI Confidence: **99.29%**
2366. **`src/coreclr/jit/phase.cpp`** -> AI Confidence: **99.29%**
2367. **`src/coreclr/jit/promotionliveness.cpp`** -> AI Confidence: **99.29%**
2368. **`src/coreclr/jit/rangecheck.cpp`** -> AI Confidence: **99.29%**
2369. **`src/coreclr/jit/rationalize.cpp`** -> AI Confidence: **99.29%**
2370. **`src/coreclr/jit/smcommon.cpp`** -> AI Confidence: **99.29%**
2371. **`src/coreclr/jit/stacklevelsetter.cpp`** -> AI Confidence: **99.29%**
2372. **`src/coreclr/jit/targetamd64.cpp`** -> AI Confidence: **99.29%**
2373. **`src/coreclr/jit/targetarm.cpp`** -> AI Confidence: **99.29%**
2374. **`src/coreclr/jit/targetarm64.cpp`** -> AI Confidence: **99.29%**
2375. **`src/coreclr/jit/targetloongarch64.cpp`** -> AI Confidence: **99.29%**
2376. **`src/coreclr/jit/targetx86.cpp`** -> AI Confidence: **99.29%**
2377. **`src/coreclr/jit/unwind.cpp`** -> AI Confidence: **99.29%**
2378. **`src/coreclr/jit/unwindamd64.cpp`** -> AI Confidence: **99.29%**
2379. **`src/coreclr/jit/unwindarm64.cpp`** -> AI Confidence: **99.29%**
2380. **`src/coreclr/jit/unwindarmarch.cpp`** -> AI Confidence: **99.29%**
2381. **`src/coreclr/jit/unwindloongarch64.cpp`** -> AI Confidence: **99.29%**
2382. **`src/coreclr/jitshared/histogram.cpp`** -> AI Confidence: **99.29%**
2383. **`src/coreclr/md/compiler/filtermanager.cpp`** -> AI Confidence: **99.29%**
2384. **`src/coreclr/md/runtime/metamodelcolumndefs.h`** -> AI Confidence: **99.29%**
2385. **`src/coreclr/minipal/Windows/dn-stdio.cpp`** -> AI Confidence: **99.29%**
2386. **`src/coreclr/nativeaot/Runtime/amd64/AsmOffsetsCpu.h`** -> AI Confidence: **99.29%**
2387. **`src/coreclr/nativeaot/Runtime/windows/AsmOffsets.cpp`** -> AI Confidence: **99.29%**
2388. **`src/coreclr/pal/inc/rt/imagehlp.h`** -> AI Confidence: **99.29%**
2389. **`src/coreclr/pal/src/arch/amd64/asmconstants.h`** -> AI Confidence: **99.29%**
2390. **`src/coreclr/pal/src/map/common.cpp`** -> AI Confidence: **99.29%**
2391. **`src/coreclr/pal/src/safecrt/tmakepath_s.inl`** -> AI Confidence: **99.29%**
2392. **`src/coreclr/pal/tests/palsuite/c_runtime/isdigit/test1/test1.cpp`** -> AI Confidence: **99.29%**
2393. **`src/coreclr/pal/tests/palsuite/c_runtime/iswprint/test1/test1.cpp`** -> AI Confidence: **99.29%**
2394. **`src/coreclr/pal/tests/palsuite/c_runtime/isxdigit/test1/test1.cpp`** -> AI Confidence: **99.29%**
2395. **`src/coreclr/pal/tests/palsuite/c_runtime/strcmp/test1/test1.cpp`** -> AI Confidence: **99.29%**
2396. **`src/coreclr/pal/tests/palsuite/c_runtime/strncmp/test1/test1.cpp`** -> AI Confidence: **99.29%**
2397. **`src/coreclr/pal/tests/palsuite/c_runtime/wcsstr/test1/test1.cpp`** -> AI Confidence: **99.29%**
2398. **`src/coreclr/pal/tests/palsuite/composite/object_management/event/nonshared/main.cpp`** -> AI Confidence: **99.29%**
2399. **`src/coreclr/pal/tests/palsuite/composite/object_management/event/shared/main.cpp`** -> AI Confidence: **99.29%**
2400. **`src/coreclr/pal/tests/palsuite/composite/object_management/semaphore/nonshared/main.cpp`** -> AI Confidence: **99.29%**
2401. **`src/coreclr/pal/tests/palsuite/composite/object_management/semaphore/shared/main.cpp`** -> AI Confidence: **99.29%**
2402. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test1/commonconsts.h`** -> AI Confidence: **99.29%**
2403. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test1/test1.cpp`** -> AI Confidence: **99.29%**
2404. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test3/commonconsts.h`** -> AI Confidence: **99.29%**
2405. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test3/test3.cpp`** -> AI Confidence: **99.29%**
2406. **`src/coreclr/pal/tests/palsuite/debug_api/WriteProcessMemory/test4/test4.cpp`** -> AI Confidence: **99.29%**
2407. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER/test1/PAL_EXCEPT_FILTER.cpp`** -> AI Confidence: **99.29%**
2408. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER/test2/pal_except_filter.cpp`** -> AI Confidence: **99.29%**
2409. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER_EX/test1/PAL_EXCEPT_FILTER_EX.cpp`** -> AI Confidence: **99.29%**
2410. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER_EX/test2/pal_except_filter_ex.cpp`** -> AI Confidence: **99.29%**
2411. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_EXCEPT_FILTER_EX/test3/pal_except_filter.cpp`** -> AI Confidence: **99.29%**
2412. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_TRY_EXCEPT_EX/test1/PAL_TRY_EXCEPT_EX.cpp`** -> AI Confidence: **99.29%**
2413. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_TRY_EXCEPT_EX/test2/PAL_TRY_EXCEPT_EX.cpp`** -> AI Confidence: **99.29%**
2414. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_TRY_EXCEPT_EX/test3/PAL_TRY_EXCEPT_EX.cpp`** -> AI Confidence: **99.29%**
2415. **`src/coreclr/pal/tests/palsuite/exception_handling/PAL_TRY_LEAVE_FINALLY/test1/PAL_TRY_LEAVE_FINALLY.cpp`** -> AI Confidence: **99.29%**
2416. **`src/coreclr/pal/tests/palsuite/exception_handling/RaiseException/test1/test1.cpp`** -> AI Confidence: **99.29%**
2417. **`src/coreclr/pal/tests/palsuite/exception_handling/RaiseException/test2/test2.cpp`** -> AI Confidence: **99.29%**
2418. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test2/test2.cpp`** -> AI Confidence: **99.29%**
2419. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test3/test3.cpp`** -> AI Confidence: **99.29%**
2420. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test4/test4.cpp`** -> AI Confidence: **99.29%**
2421. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test5/test5.cpp`** -> AI Confidence: **99.29%**
2422. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_except/test6/test6.cpp`** -> AI Confidence: **99.29%**
2423. **`src/coreclr/pal/tests/palsuite/exception_handling/pal_finally/test1/pal_finally.cpp`** -> AI Confidence: **99.29%**
2424. **`src/coreclr/pal/tests/palsuite/file_io/FlushFileBuffers/test1/FlushFileBuffers.cpp`** -> AI Confidence: **99.29%**
2425. **`src/coreclr/pal/tests/palsuite/file_io/GetFileSize/test1/GetFileSize.cpp`** -> AI Confidence: **99.29%**
2426. **`src/coreclr/pal/tests/palsuite/file_io/GetFileSizeEx/test1/GetFileSizeEx.cpp`** -> AI Confidence: **99.29%**
2427. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameA/test1/GetFullPathNameA.cpp`** -> AI Confidence: **99.29%**
2428. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameA/test2/test2.cpp`** -> AI Confidence: **99.29%**
2429. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameA/test3/test3.cpp`** -> AI Confidence: **99.29%**
2430. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameA/test4/test4.cpp`** -> AI Confidence: **99.29%**
2431. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameW/test2/test2.cpp`** -> AI Confidence: **99.29%**
2432. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameW/test3/test3.cpp`** -> AI Confidence: **99.29%**
2433. **`src/coreclr/pal/tests/palsuite/file_io/GetFullPathNameW/test4/test4.cpp`** -> AI Confidence: **99.29%**
2434. **`src/coreclr/pal/tests/palsuite/file_io/GetStdHandle/test1/GetStdHandle.cpp`** -> AI Confidence: **99.29%**
2435. **`src/coreclr/pal/tests/palsuite/file_io/GetStdHandle/test2/GetStdHandle.cpp`** -> AI Confidence: **99.29%**
2436. **`src/coreclr/pal/tests/palsuite/file_io/ReadFile/test4/readfile.cpp`** -> AI Confidence: **99.29%**
2437. **`src/coreclr/pal/tests/palsuite/file_io/WriteFile/test4/writefile.cpp`** -> AI Confidence: **99.29%**
2438. **`src/coreclr/pal/tests/palsuite/file_io/errorpathnotfound/test1/test1.cpp`** -> AI Confidence: **99.29%**
2439. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/CreateFileMapping_neg1/CreateFileMapping_neg.cpp`** -> AI Confidence: **99.29%**
2440. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test1/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2441. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test2/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2442. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test3/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2443. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test4/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2444. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test5/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2445. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test6/CreateFileMappingW.cpp`** -> AI Confidence: **99.29%**
2446. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/CreateFileMappingW/test7/createfilemapping.cpp`** -> AI Confidence: **99.29%**
2447. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/GetModuleFileNameA/test1/GetModuleFileNameA.cpp`** -> AI Confidence: **99.29%**
2448. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/GetModuleFileNameW/test1/GetModuleFileNameW.cpp`** -> AI Confidence: **99.29%**
2449. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/GetProcAddress/test1/test1.cpp`** -> AI Confidence: **99.29%**
2450. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/GetProcAddress/test2/test2.cpp`** -> AI Confidence: **99.29%**
2451. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/MapViewOfFile/test1/MapViewOfFile.cpp`** -> AI Confidence: **99.29%**
2452. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/MapViewOfFile/test2/MapViewOfFile.cpp`** -> AI Confidence: **99.29%**
2453. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/MapViewOfFile/test3/MapViewOfFile.cpp`** -> AI Confidence: **99.29%**
2454. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/MapViewOfFile/test4/mapviewoffile.cpp`** -> AI Confidence: **99.29%**
2455. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/UnmapViewOfFile/test1/UnmapViewOfFile.cpp`** -> AI Confidence: **99.29%**
2456. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualAlloc/test20/virtualalloc.cpp`** -> AI Confidence: **99.29%**
2457. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualAlloc/test21/virtualalloc.cpp`** -> AI Confidence: **99.29%**
2458. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test1/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2459. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test2/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2460. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test3/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2461. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test4/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2462. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test6/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2463. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualProtect/test7/VirtualProtect.cpp`** -> AI Confidence: **99.29%**
2464. **`src/coreclr/pal/tests/palsuite/filemapping_memmgt/VirtualQuery/test1/VirtualQuery.cpp`** -> AI Confidence: **99.29%**
2465. **`src/coreclr/pal/tests/palsuite/loader/LoadLibraryA/test1/LoadLibraryA.cpp`** -> AI Confidence: **99.29%**
2466. **`src/coreclr/pal/tests/palsuite/loader/LoadLibraryW/test1/LoadLibraryW.cpp`** -> AI Confidence: **99.29%**
2467. **`src/coreclr/pal/tests/palsuite/miscellaneous/GetSystemInfo/test1/test.cpp`** -> AI Confidence: **99.29%**
2468. **`src/coreclr/pal/tests/palsuite/miscellaneous/InterLockedExchangeAdd/test1/test.cpp`** -> AI Confidence: **99.29%**
2469. **`src/coreclr/pal/tests/palsuite/miscellaneous/IsBadReadPtr/test1/test.cpp`** -> AI Confidence: **99.29%**
2470. **`src/coreclr/pal/tests/palsuite/miscellaneous/SetEnvironmentVariableA/test1/test1.cpp`** -> AI Confidence: **99.29%**
2471. **`src/coreclr/pal/tests/palsuite/miscellaneous/SetEnvironmentVariableW/test1/test.cpp`** -> AI Confidence: **99.29%**
2472. **`src/coreclr/pal/tests/palsuite/threading/CreateProcessW/test1/childProcess.cpp`** -> AI Confidence: **99.29%**
2473. **`src/coreclr/pal/tests/palsuite/threading/CreateProcessW/test1/parentProcess.cpp`** -> AI Confidence: **99.29%**
2474. **`src/coreclr/pal/tests/palsuite/threading/CreateProcessW/test2/parentprocess.cpp`** -> AI Confidence: **99.29%**
2475. **`src/coreclr/pal/tests/palsuite/threading/DisableThreadLibraryCalls/test2/test2.cpp`** -> AI Confidence: **99.29%**
2476. **`src/coreclr/pal/tests/palsuite/threading/DuplicateHandle/test1/test1.cpp`** -> AI Confidence: **99.29%**
2477. **`src/coreclr/pal/tests/palsuite/threading/DuplicateHandle/test10/test10.cpp`** -> AI Confidence: **99.29%**
2478. **`src/coreclr/pal/tests/palsuite/threading/DuplicateHandle/test12/test12.cpp`** -> AI Confidence: **99.29%**
2479. **`src/coreclr/pal/tests/palsuite/threading/GetCurrentThread/test1/thread.cpp`** -> AI Confidence: **99.29%**
2480. **`src/coreclr/pal/tests/palsuite/threading/OpenEventW/test1/test1.cpp`** -> AI Confidence: **99.29%**
2481. **`src/coreclr/pal/tests/palsuite/threading/OpenEventW/test2/test2.cpp`** -> AI Confidence: **99.29%**
2482. **`src/coreclr/pal/tests/palsuite/threading/OpenEventW/test3/test3.cpp`** -> AI Confidence: **99.29%**
2483. **`src/coreclr/pal/tests/palsuite/threading/OpenEventW/test5/test5.cpp`** -> AI Confidence: **99.29%**
2484. **`src/coreclr/pal/tests/palsuite/threading/OpenProcess/test1/test1.cpp`** -> AI Confidence: **99.29%**
2485. **`src/coreclr/pal/tests/palsuite/threading/QueryThreadCycleTime/test1/test1.cpp`** -> AI Confidence: **99.29%**
2486. **`src/coreclr/pal/tests/palsuite/threading/ResetEvent/test1/test1.cpp`** -> AI Confidence: **99.29%**
2487. **`src/coreclr/pal/tests/palsuite/threading/ResetEvent/test4/test4.cpp`** -> AI Confidence: **99.29%**
2488. **`src/coreclr/pal/tests/palsuite/threading/SetEvent/test1/test1.cpp`** -> AI Confidence: **99.29%**
2489. **`src/coreclr/pal/tests/palsuite/threading/SetEvent/test2/test2.cpp`** -> AI Confidence: **99.29%**
2490. **`src/coreclr/pal/tests/palsuite/threading/SetEvent/test4/test4.cpp`** -> AI Confidence: **99.29%**
2491. **`src/coreclr/pal/tests/palsuite/threading/Sleep/test1/Sleep.cpp`** -> AI Confidence: **99.29%**
2492. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjects/test1/test1.cpp`** -> AI Confidence: **99.29%**
2493. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjectsEx/test1/test1.cpp`** -> AI Confidence: **99.29%**
2494. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjectsEx/test5/helper.cpp`** -> AI Confidence: **99.29%**
2495. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjectsEx/test5/test5.cpp`** -> AI Confidence: **99.29%**
2496. **`src/coreclr/pal/tests/palsuite/threading/WaitForSingleObject/test1/test1.cpp`** -> AI Confidence: **99.29%**
2497. **`src/coreclr/tools/cdac-build-tool/sample/sample.data.h`** -> AI Confidence: **99.29%**
2498. **`src/coreclr/tools/metainfo/mdobj.cpp`** -> AI Confidence: **99.29%**
2499. **`src/coreclr/unwinder/amd64/dbs_stack_x64.cpp`** -> AI Confidence: **99.29%**
2500. **`src/coreclr/unwinder/amd64/unwinder.cpp`** -> AI Confidence: **99.29%**
2501. **`src/coreclr/unwinder/loongarch64/unwinder.cpp`** -> AI Confidence: **99.29%**
2502. **`src/coreclr/unwinder/riscv64/unwinder.cpp`** -> AI Confidence: **99.29%**
2503. **`src/coreclr/utilcode/log.cpp`** -> AI Confidence: **99.29%**
2504. **`src/coreclr/utilcode/sstring_com.cpp`** -> AI Confidence: **99.29%**
2505. **`src/coreclr/vm/arm/asmconstants.h`** -> AI Confidence: **99.29%**
2506. **`src/coreclr/vm/arm/asmmacros.h`** -> AI Confidence: **99.29%**
2507. **`src/coreclr/vm/arm/singlestepper.cpp`** -> AI Confidence: **99.29%**
2508. **`src/coreclr/vm/arm64/AsmMacros_Shared.h`** -> AI Confidence: **99.29%**
2509. **`src/coreclr/vm/arm64/asmconstants.h`** -> AI Confidence: **99.29%**
2510. **`src/coreclr/vm/arm64/asmmacros.h`** -> AI Confidence: **99.29%**
2511. **`src/coreclr/vm/arm64/patchedcodeconstants.h`** -> AI Confidence: **99.29%**
2512. **`src/coreclr/vm/arm64/singlestepper.cpp`** -> AI Confidence: **99.29%**
2513. **`src/coreclr/vm/asyncthunks.cpp`** -> AI Confidence: **99.29%**
2514. **`src/coreclr/vm/callhelpers.cpp`** -> AI Confidence: **99.29%**
2515. **`src/coreclr/vm/classlayoutinfo.cpp`** -> AI Confidence: **99.29%**
2516. **`src/coreclr/vm/clrvarargs.cpp`** -> AI Confidence: **99.29%**
2517. **`src/coreclr/vm/eecontract.cpp`** -> AI Confidence: **99.29%**
2518. **`src/coreclr/vm/gc_unwind_x86.inl`** -> AI Confidence: **99.29%**
2519. **`src/coreclr/vm/gcdecode.cpp`** -> AI Confidence: **99.29%**
2520. **`src/coreclr/vm/ildump.h`** -> AI Confidence: **99.29%**
2521. **`src/coreclr/vm/loongarch64/asmconstants.h`** -> AI Confidence: **99.29%**
2522. **`src/coreclr/vm/loongarch64/singlestepper.cpp`** -> AI Confidence: **99.29%**
2523. **`src/coreclr/vm/methodimpl.cpp`** -> AI Confidence: **99.29%**
2524. **`src/coreclr/vm/rcwrefcache.cpp`** -> AI Confidence: **99.29%**
2525. **`src/coreclr/vm/readytorunstandalonemethodmetadata.cpp`** -> AI Confidence: **99.29%**
2526. **`src/coreclr/vm/riscv64/asmconstants.h`** -> AI Confidence: **99.29%**
2527. **`src/coreclr/vm/riscv64/singlestepper.cpp`** -> AI Confidence: **99.29%**
2528. **`src/coreclr/vm/sigformat.cpp`** -> AI Confidence: **99.29%**
2529. **`src/libraries/System.Diagnostics.FileVersionInfo/tests/NativeLibrary/dllmain.cpp`** -> AI Confidence: **99.29%**
2530. **`src/libraries/System.Diagnostics.FileVersionInfo/tests/SecondNativeLibrary/dllmain.cpp`** -> AI Confidence: **99.29%**
2531. **`src/mono/cmake/config.h.in`** -> AI Confidence: **99.29%**
2532. **`src/mono/mono/arch/amd64/amd64-codegen.h`** -> AI Confidence: **99.29%**
2533. **`src/mono/mono/arch/x86/x86-codegen.h`** -> AI Confidence: **99.29%**
2534. **`src/mono/mono/metadata/verify-internals.h`** -> AI Confidence: **99.29%**
2535. **`src/mono/mono/mini/interp/jiterpreter-opcode-values.h`** -> AI Confidence: **99.29%**
2536. **`src/mono/mono/offsets/aarch64-apple-darwin10.h`** -> AI Confidence: **99.29%**
2537. **`src/mono/mono/offsets/aarch64-apple-maccatalyst.h`** -> AI Confidence: **99.29%**
2538. **`src/mono/mono/offsets/aarch64-v8a-linux-android.h`** -> AI Confidence: **99.29%**
2539. **`src/mono/mono/offsets/armv7-none-linux-androideabi.h`** -> AI Confidence: **99.29%**
2540. **`src/mono/mono/offsets/i686-none-linux-android.h`** -> AI Confidence: **99.29%**
2541. **`src/mono/mono/offsets/wasm32-unknown-none.h`** -> AI Confidence: **99.29%**
2542. **`src/mono/mono/offsets/wasm32-unknown-wasip2.h`** -> AI Confidence: **99.29%**
2543. **`src/mono/mono/offsets/x86_64-apple-darwin10.h`** -> AI Confidence: **99.29%**
2544. **`src/mono/mono/offsets/x86_64-apple-maccatalyst.h`** -> AI Confidence: **99.29%**
2545. **`src/mono/mono/offsets/x86_64-none-linux-android.h`** -> AI Confidence: **99.29%**
2546. **`src/mono/mono/sgen/sgen-archdep.h`** -> AI Confidence: **99.29%**
2547. **`src/mono/mono/sgen/sgen-major-copy-object.h`** -> AI Confidence: **99.29%**
2548. **`src/mono/mono/utils/dtrace.h`** -> AI Confidence: **99.29%**
2549. **`src/mono/mono/utils/ftnptr.h`** -> AI Confidence: **99.29%**
2550. **`src/mono/mono/utils/mono-hwcap-vars.h`** -> AI Confidence: **99.29%**
2551. **`src/mono/mono/utils/w32subset.h`** -> AI Confidence: **99.29%**
2552. **`src/mono/mono/utils/ward.h`** -> AI Confidence: **99.29%**
2553. **`src/native/containers/dn-vector-ptr.h`** -> AI Confidence: **99.29%**
2554. **`src/native/corehost/test/nativehost/get_native_search_directories_test.cpp`** -> AI Confidence: **99.29%**
2555. **`src/native/corehost/test/nativehost/hostfxr_exports.cpp`** -> AI Confidence: **99.29%**
2556. **`src/native/corehost/test/nativehost/hostpolicy_exports.cpp`** -> AI Confidence: **99.29%**
2557. **`src/native/external/brotli/c/enc/backward_references_inc.h`** -> AI Confidence: **99.29%**
2558. **`src/native/external/brotli/c/enc/block_splitter_inc.h`** -> AI Confidence: **99.29%**
2559. **`src/native/external/brotli/c/include/brotli/port.h`** -> AI Confidence: **99.29%**
2560. **`src/native/external/libunwind/include/compiler.h`** -> AI Confidence: **99.29%**
2561. **`src/native/external/libunwind/include/tdep-aarch64/jmpbuf.h`** -> AI Confidence: **99.29%**
2562. **`src/native/external/libunwind/include/tdep-riscv/jmpbuf.h`** -> AI Confidence: **99.29%**
2563. **`src/native/external/libunwind/include/tdep-s390x/jmpbuf.h`** -> AI Confidence: **99.29%**
2564. **`src/native/external/libunwind/include/tdep-x86/jmpbuf.h`** -> AI Confidence: **99.29%**
2565. **`src/native/external/libunwind/include/tdep-x86_64/jmpbuf.h`** -> AI Confidence: **99.29%**
2566. **`src/native/external/libunwind/tests/Ltest-init.cxx`** -> AI Confidence: **99.29%**
2567. **`src/native/external/rapidjson/internal/itoa.h`** -> AI Confidence: **99.29%**
2568. **`src/native/external/zlib-ng/arch/s390/s390_functions.h`** -> AI Confidence: **99.29%**
2569. **`src/native/libs/System.Native/ios/netinet/tcp_fsm.h`** -> AI Confidence: **99.29%**
2570. **`src/tests/Interop/COM/NativeClients/Dispatch/ClientTests.h`** -> AI Confidence: **99.29%**
2571. **`src/tests/JIT/jit64/mcc/interop/native_i3s.cpp`** -> AI Confidence: **99.29%**
2572. **`src/tests/JIT/jit64/mcc/interop/native_i5s.cpp`** -> AI Confidence: **99.29%**
2573. **`src/tests/JIT/jit64/mcc/interop/native_i6s.cpp`** -> AI Confidence: **99.29%**
2574. **`src/tests/JIT/jit64/mcc/interop/native_i7s.cpp`** -> AI Confidence: **99.29%**
2575. **`src/tests/JIT/jit64/mcc/interop/native_i8s.cpp`** -> AI Confidence: **99.29%**
2576. **`src/coreclr/System.Private.CoreLib/src/System/Runtime/ExceptionServices/AsmOffsets.cs`** -> AI Confidence: **99.29%**
2577. **`src/coreclr/tools/Common/Compiler/DependencyAnalysis/Target_X64/X64Emitter.cs`** -> AI Confidence: **99.29%**
2578. **`src/coreclr/tools/Common/Compiler/DependencyAnalysis/Target_X86/X86Emitter.cs`** -> AI Confidence: **99.29%**
2579. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaSignatureEncoder.cs`** -> AI Confidence: **99.29%**
2580. **`src/coreclr/tools/Common/TypeSystem/Ecma/PrimitiveTypeProvider.cs`** -> AI Confidence: **99.29%**
2581. **`src/coreclr/tools/Common/TypeSystem/IL/MethodILDebugView.cs`** -> AI Confidence: **99.29%**
2582. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/ScannerExtensions.cs`** -> AI Confidence: **99.29%**
2583. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/Target_X86/X86ReadyToRunGenericHelperNode.cs`** -> AI Confidence: **99.29%**
2584. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/JitHelper.cs`** -> AI Confidence: **99.29%**
2585. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/StringExtensions.cs`** -> AI Confidence: **99.29%**
2586. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/x86/GcInfo.cs`** -> AI Confidence: **99.29%**
2587. **`src/libraries/Common/src/Interop/Unix/System.Native/Interop.MountPoints.FormatInfo.cs`** -> AI Confidence: **99.29%**
2588. **`src/libraries/Common/src/System/Composition/Diagnostics/CompositionTrace.cs`** -> AI Confidence: **99.29%**
2589. **`src/libraries/Common/src/System/Data/Common/MultipartIdentifier.cs`** -> AI Confidence: **99.29%**
2590. **`src/libraries/Common/src/System/Data/ProviderBase/DbMetaDataFactory.cs`** -> AI Confidence: **99.29%**
2591. **`src/libraries/Common/src/System/Net/Http/aspnetcore/Http2/Hpack/HPackDecoder.cs`** -> AI Confidence: **99.29%**
2592. **`src/libraries/Common/src/System/Net/HttpValidationHelpers.cs`** -> AI Confidence: **99.29%**
2593. **`src/libraries/Common/src/System/Number.Parsing.Common.cs`** -> AI Confidence: **99.29%**
2594. **`src/libraries/Common/src/System/Obsoletions.cs`** -> AI Confidence: **99.29%**
2595. **`src/libraries/Common/src/System/Reflection/AssemblyNameFormatter.cs`** -> AI Confidence: **99.29%**
2596. **`src/libraries/Microsoft.Bcl.Cryptography/src/Microsoft.Bcl.Cryptography.Forwards.cs`** -> AI Confidence: **99.29%**
2597. **`src/libraries/Microsoft.Bcl.Memory/src/Microsoft.Bcl.Memory.Forwards.cs`** -> AI Confidence: **99.29%**
2598. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/Errors/ErrorFacts.cs`** -> AI Confidence: **99.29%**
2599. **`src/libraries/System.CodeDom/src/System/CodeDom/Compiler/CodeValidator.cs`** -> AI Confidence: **99.29%**
2600. **`src/libraries/System.Collections/tests/Generic/LinkedList/LinkedList.Generic.Tests.Find.cs`** -> AI Confidence: **99.29%**
2601. **`src/libraries/System.Collections/tests/Generic/LinkedList/LinkedList.Generic.Tests.FindLast.cs`** -> AI Confidence: **99.29%**
2602. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Diagnostics/TraceConfiguration.cs`** -> AI Confidence: **99.29%**
2603. **`src/libraries/System.Data.Common/src/System/Data/Merger.cs`** -> AI Confidence: **99.29%**
2604. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcUtils.cs`** -> AI Confidence: **99.29%**
2605. **`src/libraries/System.Data.OleDb/src/OleDbCommandBuilder.cs`** -> AI Confidence: **99.29%**
2606. **`src/libraries/System.Data.OleDb/src/System/Data/ProviderBase/DbMetaDataFactory.cs`** -> AI Confidence: **99.29%**
2607. **`src/libraries/System.Diagnostics.PerformanceCounter/src/System/Diagnostics/CounterSampleCalculator.cs`** -> AI Confidence: **99.29%**
2608. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/ProcessWaitState.Unix.cs`** -> AI Confidence: **99.29%**
2609. **`src/libraries/System.DirectoryServices.Protocols/src/System/DirectoryServices/Protocols/common/BerConverter.cs`** -> AI Confidence: **99.29%**
2610. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectoryInterSiteTransport.cs`** -> AI Confidence: **99.29%**
2611. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchedule.cs`** -> AI Confidence: **99.29%**
2612. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchemaClassCollection.cs`** -> AI Confidence: **99.29%**
2613. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySchemaProperty.cs`** -> AI Confidence: **99.29%**
2614. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySiteLinkCollection.cs`** -> AI Confidence: **99.29%**
2615. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySubnet.cs`** -> AI Confidence: **99.29%**
2616. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/DirectoryServerCollection.cs`** -> AI Confidence: **99.29%**
2617. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/TrustHelper.cs`** -> AI Confidence: **99.29%**
2618. **`src/libraries/System.Formats.Cbor/src/System/Formats/Cbor/Reader/CborReader.SkipValue.cs`** -> AI Confidence: **99.29%**
2619. **`src/libraries/System.Formats.Cbor/tests/Reader/CborReaderTests.Helpers.cs`** -> AI Confidence: **99.29%**
2620. **`src/libraries/System.IO.Compression.ZipFile/ref/System.IO.Compression.ZipFile.cs`** -> AI Confidence: **99.29%**
2621. **`src/libraries/System.IO.FileSystem.AccessControl/src/System/Security/AccessControl/DirectoryObjectSecurity.cs`** -> AI Confidence: **99.29%**
2622. **`src/libraries/System.IO.Pipes.AccessControl/ref/System.IO.Pipes.AccessControl.cs`** -> AI Confidence: **99.29%**
2623. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Generated.cs`** -> AI Confidence: **99.29%**
2624. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Lambda.cs`** -> AI Confidence: **99.29%**
2625. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Logical.cs`** -> AI Confidence: **99.29%**
2626. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/StackSpiller.Generated.cs`** -> AI Confidence: **99.29%**
2627. **`src/libraries/System.Linq.Expressions/tests/Array/NewArrayListTests.cs`** -> AI Confidence: **99.29%**
2628. **`src/libraries/System.Linq.Expressions/tests/Array/NullableNewArrayListTests.cs`** -> AI Confidence: **99.29%**
2629. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Bitwise/BinaryNullableAndTests.cs`** -> AI Confidence: **99.29%**
2630. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Bitwise/BinaryNullableExclusiveOrTests.cs`** -> AI Confidence: **99.29%**
2631. **`src/libraries/System.Linq.Expressions/tests/BinaryOperators/Bitwise/BinaryNullableOrTests.cs`** -> AI Confidence: **99.29%**
2632. **`src/libraries/System.Linq.Expressions/tests/Cast/IsTests.cs`** -> AI Confidence: **99.29%**
2633. **`src/libraries/System.Linq.Expressions/tests/Constant/ConstantNullableTests.cs`** -> AI Confidence: **99.29%**
2634. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaAddNullableTests.cs`** -> AI Confidence: **99.29%**
2635. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaAddTests.cs`** -> AI Confidence: **99.29%**
2636. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaIdentityNullableTests.cs`** -> AI Confidence: **99.29%**
2637. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaMultiplyNullableTests.cs`** -> AI Confidence: **99.29%**
2638. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaMultiplyTests.cs`** -> AI Confidence: **99.29%**
2639. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaSubtractNullableTests.cs`** -> AI Confidence: **99.29%**
2640. **`src/libraries/System.Linq.Expressions/tests/Lambda/LambdaSubtractTests.cs`** -> AI Confidence: **99.29%**
2641. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2642. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonGreaterThanNullableTests.cs`** -> AI Confidence: **99.29%**
2643. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonGreaterThanOrEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2644. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonLessThanNullableTests.cs`** -> AI Confidence: **99.29%**
2645. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonLessThanOrEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2646. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedComparisonNotEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2647. **`src/libraries/System.Linq.Expressions/tests/Lifted/LiftedNullableTests.cs`** -> AI Confidence: **99.29%**
2648. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2649. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonGreaterThanNullableTests.cs`** -> AI Confidence: **99.29%**
2650. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonGreaterThanOrEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2651. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonLessThanNullableTests.cs`** -> AI Confidence: **99.29%**
2652. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonLessThanOrEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2653. **`src/libraries/System.Linq.Expressions/tests/Lifted/NonLiftedComparisonNotEqualNullableTests.cs`** -> AI Confidence: **99.29%**
2654. **`src/libraries/System.Linq.Expressions/tests/Ternary/TernaryArrayNullableTests.cs`** -> AI Confidence: **99.29%**
2655. **`src/libraries/System.Linq.Expressions/tests/Ternary/TernaryArrayTests.cs`** -> AI Confidence: **99.29%**
2656. **`src/libraries/System.Linq.Expressions/tests/Ternary/TernaryNullableTests.cs`** -> AI Confidence: **99.29%**
2657. **`src/libraries/System.Linq.Expressions/tests/Ternary/TernaryTests.cs`** -> AI Confidence: **99.29%**
2658. **`src/libraries/System.Linq.Parallel/src/System/Linq/Parallel/Utils/Sorting.cs`** -> AI Confidence: **99.29%**
2659. **`src/libraries/System.Management/src/System/Management/ManagementDateTime.cs`** -> AI Confidence: **99.29%**
2660. **`src/libraries/System.Management/src/System/Management/ManagementObjectSearcher.cs`** -> AI Confidence: **99.29%**
2661. **`src/libraries/System.Management/src/System/Management/MethodSet.cs`** -> AI Confidence: **99.29%**
2662. **`src/libraries/System.Memory/tests/ReadOnlySpan/IndexOfAny.byte.cs`** -> AI Confidence: **99.29%**
2663. **`src/libraries/System.Memory/tests/ReadOnlySpan/IndexOfAny.char.cs`** -> AI Confidence: **99.29%**
2664. **`src/libraries/System.Memory/tests/SequenceReader/SpanLiteralExtensions.cs`** -> AI Confidence: **99.29%**
2665. **`src/libraries/System.Memory/tests/Span/EnumerateRunes.cs`** -> AI Confidence: **99.29%**
2666. **`src/libraries/System.Memory/tests/Span/LastIndexOf.T.cs`** -> AI Confidence: **99.29%**
2667. **`src/libraries/System.Net.Http.Json/ref/System.Net.Http.Json.cs`** -> AI Confidence: **99.29%**
2668. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpResponseStreamAsyncResult.cs`** -> AI Confidence: **99.29%**
2669. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Interop/msquic_generated_windows.cs`** -> AI Confidence: **99.29%**
2670. **`src/libraries/System.Net.Requests/src/System/Net/NetRes.cs`** -> AI Confidence: **99.29%**
2671. **`src/libraries/System.Net.WebClient/tests/AssemblyInfo.cs`** -> AI Confidence: **99.29%**
2672. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.IAggregationOperator.cs`** -> AI Confidence: **99.29%**
2673. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.IBinaryOperator.cs`** -> AI Confidence: **99.29%**
2674. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.IStatefulUnaryOperator.cs`** -> AI Confidence: **99.29%**
2675. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.ITernaryOperator.cs`** -> AI Confidence: **99.29%**
2676. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/Common/TensorPrimitives.IUnaryOperator.cs`** -> AI Confidence: **99.29%**
2677. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Formatter/Utf8Formatter.Boolean.cs`** -> AI Confidence: **99.29%**
2678. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Formatter/Utf8Formatter.Guid.cs`** -> AI Confidence: **99.29%**
2679. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Date.R.cs`** -> AI Confidence: **99.29%**
2680. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Integer.Signed.D.cs`** -> AI Confidence: **99.29%**
2681. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Integer.Signed.N.cs`** -> AI Confidence: **99.29%**
2682. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Integer.Unsigned.D.cs`** -> AI Confidence: **99.29%**
2683. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.Integer.Unsigned.N.cs`** -> AI Confidence: **99.29%**
2684. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.TimeSpan.C.cs`** -> AI Confidence: **99.29%**
2685. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Utf8Parser/Utf8Parser.TimeSpan.LittleG.cs`** -> AI Confidence: **99.29%**
2686. **`src/libraries/System.Private.CoreLib/src/System/Collections/ObjectModel/CollectionHelpers.cs`** -> AI Confidence: **99.29%**
2687. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/EventPipePayloadDecoder.cs`** -> AI Confidence: **99.29%**
2688. **`src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/TraceLogging/ConcurrentSet.cs`** -> AI Confidence: **99.29%**
2689. **`src/libraries/System.Private.CoreLib/src/System/Globalization/DateTimeFormatInfoScanner.cs`** -> AI Confidence: **99.29%**
2690. **`src/libraries/System.Private.CoreLib/src/System/IO/Strategies/FileStreamHelpers.cs`** -> AI Confidence: **99.29%**
2691. **`src/libraries/System.Private.CoreLib/src/System/ParseNumbers.cs`** -> AI Confidence: **99.29%**
2692. **`src/libraries/System.Private.CoreLib/src/System/Reflection/InvokeUtils.cs`** -> AI Confidence: **99.29%**
2693. **`src/libraries/System.Private.CoreLib/src/System/SpanHelpers.cs`** -> AI Confidence: **99.29%**
2694. **`src/libraries/System.Private.CoreLib/src/System/Text/CompositeFormat.cs`** -> AI Confidence: **99.29%**
2695. **`src/libraries/System.Private.CoreLib/src/System/Text/UnicodeEncoding.cs`** -> AI Confidence: **99.29%**
2696. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.StringSerializer.cs`** -> AI Confidence: **99.29%**
2697. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Attributes.cs`** -> AI Confidence: **99.29%**
2698. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonWriterDelegator.cs`** -> AI Confidence: **99.29%**
2699. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlSigningNodeWriter.cs`** -> AI Confidence: **99.29%**
2700. **`src/libraries/System.Private.Uri/src/System/PercentEncodingHelper.cs`** -> AI Confidence: **99.29%**
2701. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/XNodeBuilder.cs`** -> AI Confidence: **99.29%**
2702. **`src/libraries/System.Private.Xml.Linq/tests/XDocument.Common/ManagedNodeWriter.cs`** -> AI Confidence: **99.29%**
2703. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/CXMLGeneralTest.cs`** -> AI Confidence: **99.29%**
2704. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/ReadSubTree.cs`** -> AI Confidence: **99.29%**
2705. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/ReadToDescendant.cs`** -> AI Confidence: **99.29%**
2706. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlTextEncoder.cs`** -> AI Confidence: **99.29%**
2707. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/AttributeAction.cs`** -> AI Confidence: **99.29%**
2708. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/CallTemplateAction.cs`** -> AI Confidence: **99.29%**
2709. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ElementAction.cs`** -> AI Confidence: **99.29%**
2710. **`src/libraries/System.Private.Xml/tests/Readers/NameTable/TCRecordNameTableAdd.cs`** -> AI Confidence: **99.29%**
2711. **`src/libraries/System.Private.Xml/tests/Readers/ReaderSettings/TCMaxSettings.cs`** -> AI Confidence: **99.29%**
2712. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCWriteBuffer.cs`** -> AI Confidence: **99.29%**
2713. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests1.cs`** -> AI Confidence: **99.29%**
2714. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests2.cs`** -> AI Confidence: **99.29%**
2715. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests3.cs`** -> AI Confidence: **99.29%**
2716. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests4.cs`** -> AI Confidence: **99.29%**
2717. **`src/libraries/System.Private.Xml/tests/XmlConvert/VerifyNameTests5.cs`** -> AI Confidence: **99.29%**
2718. **`src/libraries/System.Private.Xml/tests/XmlReaderLib/TCLinePos.cs`** -> AI Confidence: **99.29%**
2719. **`src/libraries/System.Private.Xml/tests/XmlReaderLib/TCReadValue.cs`** -> AI Confidence: **99.29%**
2720. **`src/libraries/System.Reflection.Emit/src/System/Reflection/Emit/SignatureHelper.cs`** -> AI Confidence: **99.29%**
2721. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/BlobWriterImpl.cs`** -> AI Confidence: **99.29%**
2722. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/Ecma335/CustomAttributeDecoder.cs`** -> AI Confidence: **99.29%**
2723. **`src/libraries/System.Reflection.MetadataLoadContext/tests/src/Tests/Type/TypeTests.GetMember.cs`** -> AI Confidence: **99.29%**
2724. **`src/libraries/System.Reflection.TypeExtensions/tests/ConstructorInfo/ConstructorInfoInvokeArrayTests.cs`** -> AI Confidence: **99.29%**
2725. **`src/libraries/System.Resources.Extensions/tests/BinaryFormatTests/Common/EventOrderTests.cs`** -> AI Confidence: **99.29%**
2726. **`src/libraries/System.Runtime.InteropServices/tests/System.Runtime.InteropServices.UnitTests/System/Runtime/InteropServices/Marshal/StringMarshalingTests.cs`** -> AI Confidence: **99.29%**
2727. **`src/libraries/System.Runtime.InteropServices/tests/System.Runtime.InteropServices.UnitTests/System/Runtime/InteropServices/NFloatTests.GenericMath.cs`** -> AI Confidence: **99.29%**
2728. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/BigIntegerCalculator.AddSub.cs`** -> AI Confidence: **99.29%**
2729. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/BigIntegerCalculator.DivRem.cs`** -> AI Confidence: **99.29%**
2730. **`src/libraries/System.Runtime.Numerics/src/System/Numerics/BigIntegerCalculator.SquMul.cs`** -> AI Confidence: **99.29%**
2731. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/Driver.cs`** -> AI Confidence: **99.29%**
2732. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/cast_to.cs`** -> AI Confidence: **99.29%**
2733. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/ctor.cs`** -> AI Confidence: **99.29%**
2734. **`src/libraries/System.Runtime.Numerics/tests/BigInteger/op_multiply.cs`** -> AI Confidence: **99.29%**
2735. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryArray.cs`** -> AI Confidence: **99.29%**
2736. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryObjectWithMapTyped.cs`** -> AI Confidence: **99.29%**
2737. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/BinaryTypeConverter.cs`** -> AI Confidence: **99.29%**
2738. **`src/libraries/System.Runtime.Serialization.Formatters/src/System/Runtime/Serialization/Formatters/Binary/ObjectNull.cs`** -> AI Confidence: **99.29%**
2739. **`src/libraries/System.Runtime.Serialization.Xml/tests/Canonicalization/CryptoCanonicalization/CanonicalWriter.cs`** -> AI Confidence: **99.29%**
2740. **`src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.Statements/Conformance.dynamic.statements.foreach.cs`** -> AI Confidence: **99.29%**
2741. **`src/libraries/System.Runtime/tests/System.IO.FileSystem.Tests/Enumeration/MatchTypesTests.cs`** -> AI Confidence: **99.29%**
2742. **`src/libraries/System.Runtime/tests/System.Runtime.InteropServices.RuntimeInformation.Tests/CheckArchitectureTests.cs`** -> AI Confidence: **99.29%**
2743. **`src/libraries/System.Runtime/tests/System.Text.Encoding.Tests/Ascii/TrimTests.cs`** -> AI Confidence: **99.29%**
2744. **`src/libraries/System.Runtime/tests/System.Text.Encoding.Tests/EncodingTestHelpers.cs`** -> AI Confidence: **99.29%**
2745. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/TaskContinueWithAllAnyTests.cs`** -> AI Confidence: **99.29%**
2746. **`src/libraries/System.Security.Cryptography.Cose/tests/CoseHeaderLabelTests.cs`** -> AI Confidence: **99.29%**
2747. **`src/libraries/System.Security.Cryptography.Pkcs/tests/Rfc3161/TimestampRequestTests.cs`** -> AI Confidence: **99.29%**
2748. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/Reference.cs`** -> AI Confidence: **99.29%**
2749. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/ECDiffieHellmanCng.Key.cs`** -> AI Confidence: **99.29%**
2750. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/ECDsaCng.Key.cs`** -> AI Confidence: **99.29%**
2751. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/HKDF.OpenSsl.cs`** -> AI Confidence: **99.29%**
2752. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X500DirectoryStringHelper.cs`** -> AI Confidence: **99.29%**
2753. **`src/libraries/System.Security.Cryptography/tests/X509Certificates/ExtensionsTests/SubjectAlternativeNameTests.cs`** -> AI Confidence: **99.29%**
2754. **`src/libraries/System.Security.Permissions/ref/System.Security.Permissions.Forwards.cs`** -> AI Confidence: **99.29%**
2755. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/Item.cs`** -> AI Confidence: **99.29%**
2756. **`src/libraries/System.Speech/src/Internal/SrgsParser/SrgsDocumentParser.cs`** -> AI Confidence: **99.29%**
2757. **`src/libraries/System.Speech/src/Internal/Synthesis/AudioFormatConverter.cs`** -> AI Confidence: **99.29%**
2758. **`src/libraries/System.Text.Encodings.Web/src/System/Text/Encodings/Web/OptimizedInboxTextEncoder.cs`** -> AI Confidence: **99.29%**
2759. **`src/libraries/System.Text.Encodings.Web/tests/JavaScriptEncoderTests.Relaxed.cs`** -> AI Confidence: **99.29%**
2760. **`src/libraries/System.Text.Json/Common/JsonSourceGenerationOptionsAttribute.cs`** -> AI Confidence: **99.29%**
2761. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonConverter.MetadataHandling.cs`** -> AI Confidence: **99.29%**
2762. **`src/libraries/System.Text.Json/src/System/Text/Json/ThrowHelper.cs`** -> AI Confidence: **99.29%**
2763. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Literal.cs`** -> AI Confidence: **99.29%**
2764. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteValues.Comment.cs`** -> AI Confidence: **99.29%**
2765. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteValues.Literal.cs`** -> AI Confidence: **99.29%**
2766. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteValues.String.cs`** -> AI Confidence: **99.29%**
2767. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/BitStackTests.cs`** -> AI Confidence: **99.29%**
2768. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Utf8JsonReaderTests.ValueTextEquals.cs`** -> AI Confidence: **99.29%**
2769. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexInterpreterCode.cs`** -> AI Confidence: **99.29%**
2770. **`src/libraries/System.Text.RegularExpressions/tests/UnitTests/RegexReductionTests.cs`** -> AI Confidence: **99.29%**
2771. **`src/libraries/System.Threading.AccessControl/ref/System.Threading.AccessControl.cs`** -> AI Confidence: **99.29%**
2772. **`src/libraries/System.Threading.Tasks.Parallel/tests/ParallelForTest.cs`** -> AI Confidence: **99.29%**
2773. **`src/libraries/System.Threading.Thread/ref/System.Threading.Thread.cs`** -> AI Confidence: **99.29%**
2774. **`src/libraries/System.Transactions.Local/src/System/Transactions/EnlistmentState.cs`** -> AI Confidence: **99.29%**
2775. **`src/libraries/System.Transactions.Local/src/System/Transactions/Oletx/OletxEnlistment.cs`** -> AI Confidence: **99.29%**
2776. **`src/libraries/System.Transactions.Local/src/System/Transactions/SinglePhaseEnlistment.cs`** -> AI Confidence: **99.29%**
2777. **`src/mono/mono/mini/test.cs`** -> AI Confidence: **99.29%**
2778. **`src/mono/mono/tests/abort-try-holes.cs`** -> AI Confidence: **99.29%**
2779. **`src/mono/mono/tests/bug-30085.cs`** -> AI Confidence: **99.29%**
2780. **`src/mono/mono/tests/exception9.cs`** -> AI Confidence: **99.29%**
2781. **`src/mono/mono/tests/gchandle-stress.cs`** -> AI Confidence: **99.29%**
2782. **`src/mono/mono/tests/main-returns-abort-resetabort.cs`** -> AI Confidence: **99.29%**
2783. **`src/mono/mono/tests/main-returns-background-abort-resetabort.cs`** -> AI Confidence: **99.29%**
2784. **`src/mono/mono/tests/main-returns-background-resetabort.cs`** -> AI Confidence: **99.29%**
2785. **`src/mono/mono/tests/many-locals.cs`** -> AI Confidence: **99.29%**
2786. **`src/mono/mono/tests/monitor-stress.cs`** -> AI Confidence: **99.29%**
2787. **`src/mono/wasm/testassets/BlazorBasicTestApp/App/Pages/Home.razor`** -> AI Confidence: **99.29%**
2788. **`src/mono/wasm/testassets/BlazorWebWasm/BlazorWebWasm/Components/Pages/NotFound.razor`** -> AI Confidence: **99.29%**
2789. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/Context/X86/GCInfoDecoding/GCArgTable.cs`** -> AI Confidence: **99.29%**
2790. **`src/tasks/Crossgen2Tasks/CommonFilePulledFromSdkRepo/LogAdapter.cs`** -> AI Confidence: **99.29%**
2791. **`src/tests/Common/GenerateHWIntrinsicTests/Arm/Templates.cs`** -> AI Confidence: **99.29%**
2792. **`src/tests/GC/API/NoGCRegion/Callback.cs`** -> AI Confidence: **99.29%**
2793. **`src/tests/GC/API/NoGCRegion/NoGC.cs`** -> AI Confidence: **99.29%**
2794. **`src/tests/GC/Performance/Tests/GCLarge.cs`** -> AI Confidence: **99.29%**
2795. **`src/tests/GC/Performance/Tests/GCPerf.cs`** -> AI Confidence: **99.29%**
2796. **`src/tests/GC/Performance/Tests/WeakReferenceTest.cs`** -> AI Confidence: **99.29%**
2797. **`src/tests/GC/Scenarios/Boxing/gcvariant2.cs`** -> AI Confidence: **99.29%**
2798. **`src/tests/GC/Scenarios/Boxing/gcvariant3.cs`** -> AI Confidence: **99.29%**
2799. **`src/tests/GC/Scenarios/Boxing/gcvariant4.cs`** -> AI Confidence: **99.29%**
2800. **`src/tests/GC/Scenarios/ServerModel/server.cs`** -> AI Confidence: **99.29%**
2801. **`src/tests/GC/Scenarios/muldimjagary/muldimjagary.cs`** -> AI Confidence: **99.29%**
2802. **`src/tests/GC/Stress/Tests/DirectedGraph.cs`** -> AI Confidence: **99.29%**
2803. **`src/tests/GC/Stress/Tests/MulDimJagAry.cs`** -> AI Confidence: **99.29%**
2804. **`src/tests/GC/Stress/Tests/StressAllocator.cs`** -> AI Confidence: **99.29%**
2805. **`src/tests/Interop/StructMarshalling/PInvoke/MarshalStructAsLayoutExp.cs`** -> AI Confidence: **99.29%**
2806. **`src/tests/Interop/StructMarshalling/PInvoke/MarshalStructAsLayoutSeq.cs`** -> AI Confidence: **99.29%**
2807. **`src/tests/JIT/Directed/Convert/value_numbering_checked_casts_of_constants_double.cs`** -> AI Confidence: **99.29%**
2808. **`src/tests/JIT/Directed/Convert/value_numbering_checked_casts_of_constants_float.cs`** -> AI Confidence: **99.29%**
2809. **`src/tests/JIT/Directed/Convert/value_numbering_checked_casts_of_constants_long.cs`** -> AI Confidence: **99.29%**
2810. **`src/tests/JIT/Directed/Misc/gettype/gettypetypeofmatrix.cs`** -> AI Confidence: **99.29%**
2811. **`src/tests/JIT/Directed/UnrollLoop/loop4.cs`** -> AI Confidence: **99.29%**
2812. **`src/tests/JIT/Directed/UnrollLoop/loop6.cs`** -> AI Confidence: **99.29%**
2813. **`src/tests/JIT/Directed/cmov/Bool_And_Op.cs`** -> AI Confidence: **99.29%**
2814. **`src/tests/JIT/Directed/cmov/Bool_No_Op.cs`** -> AI Confidence: **99.29%**
2815. **`src/tests/JIT/Directed/cmov/Bool_Or_Op.cs`** -> AI Confidence: **99.29%**
2816. **`src/tests/JIT/Directed/cmov/Bool_Xor_Op.cs`** -> AI Confidence: **99.29%**
2817. **`src/tests/JIT/Directed/cmov/Double_And_Op.cs`** -> AI Confidence: **99.29%**
2818. **`src/tests/JIT/Directed/cmov/Double_No_Op.cs`** -> AI Confidence: **99.29%**
2819. **`src/tests/JIT/Directed/cmov/Double_Or_Op.cs`** -> AI Confidence: **99.29%**
2820. **`src/tests/JIT/Directed/cmov/Double_Xor_Op.cs`** -> AI Confidence: **99.29%**
2821. **`src/tests/JIT/Directed/cmov/Float_And_Op.cs`** -> AI Confidence: **99.29%**
2822. **`src/tests/JIT/Directed/cmov/Float_No_Op.cs`** -> AI Confidence: **99.29%**
2823. **`src/tests/JIT/Directed/cmov/Float_Or_Op.cs`** -> AI Confidence: **99.29%**
2824. **`src/tests/JIT/Directed/cmov/Float_Xor_Op.cs`** -> AI Confidence: **99.29%**
2825. **`src/tests/JIT/Directed/cmov/Int_And_Op.cs`** -> AI Confidence: **99.29%**
2826. **`src/tests/JIT/Directed/cmov/Int_No_Op.cs`** -> AI Confidence: **99.29%**
2827. **`src/tests/JIT/Directed/cmov/Int_Or_Op.cs`** -> AI Confidence: **99.29%**
2828. **`src/tests/JIT/Directed/cmov/Int_Xor_Op.cs`** -> AI Confidence: **99.29%**
2829. **`src/tests/JIT/Directed/gettypetypeof/gettypetypeofmatrix.cs`** -> AI Confidence: **99.29%**
2830. **`src/tests/JIT/Directed/intrinsic/interlocked/IntrinsicTest_Overflow.cs`** -> AI Confidence: **99.29%**
2831. **`src/tests/JIT/Directed/nullabletypes/isinstvaluetype.cs`** -> AI Confidence: **99.29%**
2832. **`src/tests/JIT/Generics/Exceptions/specific_class_instance02.cs`** -> AI Confidence: **99.29%**
2833. **`src/tests/JIT/Generics/Exceptions/specific_class_static02.cs`** -> AI Confidence: **99.29%**
2834. **`src/tests/JIT/Generics/Exceptions/specific_struct_instance02.cs`** -> AI Confidence: **99.29%**
2835. **`src/tests/JIT/Generics/Exceptions/specific_struct_static02.cs`** -> AI Confidence: **99.29%**
2836. **`src/tests/JIT/Generics/Typeof/dynamicTypes.cs`** -> AI Confidence: **99.29%**
2837. **`src/tests/JIT/Generics/Typeof/objectBoxing.cs`** -> AI Confidence: **99.29%**
2838. **`src/tests/JIT/Generics/Typeof/refTypesdynamic.cs`** -> AI Confidence: **99.29%**
2839. **`src/tests/JIT/Methodical/AsgOp/i4/i4flat.cs`** -> AI Confidence: **99.29%**
2840. **`src/tests/JIT/Methodical/AsgOp/i8/i8flat.cs`** -> AI Confidence: **99.29%**
2841. **`src/tests/JIT/Methodical/AsgOp/r4/r4flat.cs`** -> AI Confidence: **99.29%**
2842. **`src/tests/JIT/Methodical/AsgOp/r8/r8flat.cs`** -> AI Confidence: **99.29%**
2843. **`src/tests/JIT/Methodical/MDArray/DataTypes/bool.cs`** -> AI Confidence: **99.29%**
2844. **`src/tests/JIT/Methodical/MDArray/DataTypes/byte.cs`** -> AI Confidence: **99.29%**
2845. **`src/tests/JIT/Methodical/MDArray/DataTypes/char.cs`** -> AI Confidence: **99.29%**
2846. **`src/tests/JIT/Methodical/MDArray/DataTypes/decimal.cs`** -> AI Confidence: **99.29%**
2847. **`src/tests/JIT/Methodical/MDArray/DataTypes/double.cs`** -> AI Confidence: **99.29%**
2848. **`src/tests/JIT/Methodical/MDArray/DataTypes/float.cs`** -> AI Confidence: **99.29%**
2849. **`src/tests/JIT/Methodical/MDArray/DataTypes/long.cs`** -> AI Confidence: **99.29%**
2850. **`src/tests/JIT/Methodical/MDArray/DataTypes/sbyte.cs`** -> AI Confidence: **99.29%**
2851. **`src/tests/JIT/Methodical/MDArray/DataTypes/short.cs`** -> AI Confidence: **99.29%**
2852. **`src/tests/JIT/Methodical/MDArray/DataTypes/uint.cs`** -> AI Confidence: **99.29%**
2853. **`src/tests/JIT/Methodical/MDArray/DataTypes/ulong.cs`** -> AI Confidence: **99.29%**
2854. **`src/tests/JIT/Methodical/MDArray/DataTypes/ushort.cs`** -> AI Confidence: **99.29%**
2855. **`src/tests/JIT/Methodical/MDArray/GaussJordan/classarr.cs`** -> AI Confidence: **99.29%**
2856. **`src/tests/JIT/Methodical/MDArray/GaussJordan/jaggedarr.cs`** -> AI Confidence: **99.29%**
2857. **`src/tests/JIT/Methodical/MDArray/GaussJordan/plainarr.cs`** -> AI Confidence: **99.29%**
2858. **`src/tests/JIT/Methodical/MDArray/GaussJordan/structarr.cs`** -> AI Confidence: **99.29%**
2859. **`src/tests/JIT/Methodical/MDArray/basics/classarr.cs`** -> AI Confidence: **99.29%**
2860. **`src/tests/JIT/Methodical/MDArray/basics/doublearr.cs`** -> AI Confidence: **99.29%**
2861. **`src/tests/JIT/Methodical/MDArray/basics/jaggedarr.cs`** -> AI Confidence: **99.29%**
2862. **`src/tests/JIT/Methodical/MDArray/basics/stringarr.cs`** -> AI Confidence: **99.29%**
2863. **`src/tests/JIT/Methodical/MDArray/basics/structarr.cs`** -> AI Confidence: **99.29%**
2864. **`src/tests/JIT/Methodical/NaN/arithm32.cs`** -> AI Confidence: **99.29%**
2865. **`src/tests/JIT/Methodical/NaN/arithm64.cs`** -> AI Confidence: **99.29%**
2866. **`src/tests/JIT/Methodical/NaN/r4NaNadd.cs`** -> AI Confidence: **99.29%**
2867. **`src/tests/JIT/Methodical/NaN/r4NaNdiv.cs`** -> AI Confidence: **99.29%**
2868. **`src/tests/JIT/Methodical/NaN/r4NaNmul.cs`** -> AI Confidence: **99.29%**
2869. **`src/tests/JIT/Methodical/NaN/r4NaNrem.cs`** -> AI Confidence: **99.29%**
2870. **`src/tests/JIT/Methodical/NaN/r4NaNsub.cs`** -> AI Confidence: **99.29%**
2871. **`src/tests/JIT/Methodical/NaN/r8NaNadd.cs`** -> AI Confidence: **99.29%**
2872. **`src/tests/JIT/Methodical/NaN/r8NaNdiv.cs`** -> AI Confidence: **99.29%**
2873. **`src/tests/JIT/Methodical/NaN/r8NaNmul.cs`** -> AI Confidence: **99.29%**
2874. **`src/tests/JIT/Methodical/NaN/r8NaNrem.cs`** -> AI Confidence: **99.29%**
2875. **`src/tests/JIT/Methodical/NaN/r8NaNsub.cs`** -> AI Confidence: **99.29%**
2876. **`src/tests/JIT/Methodical/divrem/div/decimaldiv.cs`** -> AI Confidence: **99.29%**
2877. **`src/tests/JIT/Methodical/divrem/div/i4div.cs`** -> AI Confidence: **99.29%**
2878. **`src/tests/JIT/Methodical/divrem/div/i8div.cs`** -> AI Confidence: **99.29%**
2879. **`src/tests/JIT/Methodical/divrem/div/r4div.cs`** -> AI Confidence: **99.29%**
2880. **`src/tests/JIT/Methodical/divrem/div/r8div.cs`** -> AI Confidence: **99.29%**
2881. **`src/tests/JIT/Methodical/divrem/div/u4div.cs`** -> AI Confidence: **99.29%**
2882. **`src/tests/JIT/Methodical/divrem/div/u8div.cs`** -> AI Confidence: **99.29%**
2883. **`src/tests/JIT/Methodical/divrem/rem/decimalrem.cs`** -> AI Confidence: **99.29%**
2884. **`src/tests/JIT/Methodical/divrem/rem/i4rem.cs`** -> AI Confidence: **99.29%**
2885. **`src/tests/JIT/Methodical/divrem/rem/i8rem.cs`** -> AI Confidence: **99.29%**
2886. **`src/tests/JIT/Methodical/divrem/rem/r4rem.cs`** -> AI Confidence: **99.29%**
2887. **`src/tests/JIT/Methodical/divrem/rem/r8rem.cs`** -> AI Confidence: **99.29%**
2888. **`src/tests/JIT/Methodical/divrem/rem/u4rem.cs`** -> AI Confidence: **99.29%**
2889. **`src/tests/JIT/Methodical/divrem/rem/u8rem.cs`** -> AI Confidence: **99.29%**
2890. **`src/tests/JIT/Methodical/eh/deadcode/loopstrswitchgoto.cs`** -> AI Confidence: **99.29%**
2891. **`src/tests/JIT/Methodical/eh/finallyexec/localgotoinahandler.cs`** -> AI Confidence: **99.29%**
2892. **`src/tests/JIT/Methodical/eh/finallyexec/switchincatch.cs`** -> AI Confidence: **99.29%**
2893. **`src/tests/JIT/Methodical/eh/finallyexec/tryCatchFinallyThrow_nonlocalexit1.cs`** -> AI Confidence: **99.29%**
2894. **`src/tests/JIT/Methodical/eh/finallyexec/tryCatchFinallyThrow_nonlocalexit2.cs`** -> AI Confidence: **99.29%**
2895. **`src/tests/JIT/Methodical/eh/finallyexec/tryCatchFinallyThrow_nonlocalexit3.cs`** -> AI Confidence: **99.29%**
2896. **`src/tests/JIT/Methodical/eh/finallyexec/tryCatchFinallyThrow_nonlocalexit4.cs`** -> AI Confidence: **99.29%**
2897. **`src/tests/JIT/Methodical/eh/interactions/strswitchfinal.cs`** -> AI Confidence: **99.29%**
2898. **`src/tests/JIT/Methodical/eh/nested/general/cascadedcatch.cs`** -> AI Confidence: **99.29%**
2899. **`src/tests/JIT/Methodical/eh/nested/general/rethrowincatchnestedinfinally.cs`** -> AI Confidence: **99.29%**
2900. **`src/tests/JIT/Methodical/eh/nested/general/throwinfinallynestedintry.cs`** -> AI Confidence: **99.29%**
2901. **`src/tests/JIT/Methodical/eh/nested/general/throwinnestedfinally.cs`** -> AI Confidence: **99.29%**
2902. **`src/tests/JIT/Methodical/eh/nested/nonlocalexit/throwinfinally_50.cs`** -> AI Confidence: **99.29%**
2903. **`src/tests/JIT/Methodical/eh/nested/nonlocalexit/throwinfinallynestedintry_30.cs`** -> AI Confidence: **99.29%**
2904. **`src/tests/JIT/Methodical/eh/nested/nonlocalexit/throwinfinallyrecursive_20.cs`** -> AI Confidence: **99.29%**
2905. **`src/tests/JIT/Methodical/eh/regress/asurt/140713/innerFinally.cs`** -> AI Confidence: **99.29%**
2906. **`src/tests/JIT/Methodical/eh/regress/asurt/141358/uncaughtException.cs`** -> AI Confidence: **99.29%**
2907. **`src/tests/JIT/Methodical/explicit/misc/explicit1.cs`** -> AI Confidence: **99.29%**
2908. **`src/tests/JIT/Methodical/explicit/misc/explicit2.cs`** -> AI Confidence: **99.29%**
2909. **`src/tests/JIT/Methodical/explicit/misc/explicit3.cs`** -> AI Confidence: **99.29%**
2910. **`src/tests/JIT/Methodical/explicit/misc/explicit4.cs`** -> AI Confidence: **99.29%**
2911. **`src/tests/JIT/Methodical/explicit/misc/explicit5.cs`** -> AI Confidence: **99.29%**
2912. **`src/tests/JIT/Methodical/explicit/misc/explicit6.cs`** -> AI Confidence: **99.29%**
2913. **`src/tests/JIT/Methodical/explicit/misc/explicit7.cs`** -> AI Confidence: **99.29%**
2914. **`src/tests/JIT/Methodical/explicit/misc/explicit8.cs`** -> AI Confidence: **99.29%**
2915. **`src/tests/JIT/Methodical/int64/unsigned/implicit_promotion.cs`** -> AI Confidence: **99.29%**
2916. **`src/tests/JIT/Methodical/refany/format.cs`** -> AI Confidence: **99.29%**
2917. **`src/tests/JIT/Performance/CodeQuality/Benchstones/BenchF/LLoops/LLoops.cs`** -> AI Confidence: **99.29%**
2918. **`src/tests/JIT/Performance/CodeQuality/Benchstones/BenchF/MatInv4/MatInv4.cs`** -> AI Confidence: **99.29%**
2919. **`src/tests/JIT/Performance/CodeQuality/Benchstones/BenchI/Puzzle/Puzzle.cs`** -> AI Confidence: **99.29%**
2920. **`src/tests/JIT/Performance/CodeQuality/Benchstones/MDBenchF/MDLLoops/MDLLoops.cs`** -> AI Confidence: **99.29%**
2921. **`src/tests/JIT/Performance/CodeQuality/Benchstones/MDBenchI/MDPuzzle/MDPuzzle.cs`** -> AI Confidence: **99.29%**
2922. **`src/tests/JIT/Performance/CodeQuality/Bytemark/Huffman.cs`** -> AI Confidence: **99.29%**
2923. **`src/tests/JIT/Performance/CodeQuality/Bytemark/assign_jagged.cs`** -> AI Confidence: **99.29%**
2924. **`src/tests/JIT/Performance/CodeQuality/Bytemark/assign_rect.cs`** -> AI Confidence: **99.29%**
2925. **`src/tests/JIT/Performance/CodeQuality/Bytemark/bitops.cs`** -> AI Confidence: **99.29%**
2926. **`src/tests/JIT/Performance/CodeQuality/Bytemark/emfloat.cs`** -> AI Confidence: **99.29%**
2927. **`src/tests/JIT/Performance/CodeQuality/Bytemark/emfloatclass.cs`** -> AI Confidence: **99.29%**
2928. **`src/tests/JIT/Performance/CodeQuality/Bytemark/ludecomp.cs`** -> AI Confidence: **99.29%**
2929. **`src/tests/JIT/Performance/CodeQuality/Bytemark/numericsort.cs`** -> AI Confidence: **99.29%**
2930. **`src/tests/JIT/Performance/CodeQuality/SciMark/Random.cs`** -> AI Confidence: **99.29%**
2931. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M09.5-PDC/b31912/b31912.cs`** -> AI Confidence: **99.29%**
2932. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M11-Beta1/b41470/b41470.cs`** -> AI Confidence: **99.29%**
2933. **`src/tests/JIT/Regression/CLR-x86-JIT/V1-M12-Beta2/b71005/b71005.cs`** -> AI Confidence: **99.29%**
2934. **`src/tests/JIT/Regression/CLR-x86-JIT/V2.0-RTM/b369916/b369916.cs`** -> AI Confidence: **99.29%**
2935. **`src/tests/JIT/Regression/CLR-x86-JIT/v2.1/b569942/b569942.cs`** -> AI Confidence: **99.29%**
2936. **`src/tests/JIT/Regression/CLR-x86-JIT/v2.1/b608198/b608198.cs`** -> AI Confidence: **99.29%**
2937. **`src/tests/JIT/Regression/JitBlue/GitHub_18056/Bool_And_Op.cs`** -> AI Confidence: **99.29%**
2938. **`src/tests/JIT/Regression/JitBlue/GitHub_20838/GitHub_20838.cs`** -> AI Confidence: **99.29%**
2939. **`src/tests/JIT/Regression/JitBlue/Runtime_93342/Runtime_93342.cs`** -> AI Confidence: **99.29%**
2940. **`src/tests/JIT/Regression/VS-ia64-JIT/M00/b111192/strswitch2.cs`** -> AI Confidence: **99.29%**
2941. **`src/tests/JIT/Regression/VS-ia64-JIT/M00/b141358/test.cs`** -> AI Confidence: **99.29%**
2942. **`src/tests/JIT/Regression/VS-ia64-JIT/V1.2-M01/b10827/MT_DEATH.cs`** -> AI Confidence: **99.29%**
2943. **`src/tests/JIT/Regression/VS-ia64-JIT/V1.2-M02/b26496/_1d6bgof.cs`** -> AI Confidence: **99.29%**
2944. **`src/tests/JIT/Regression/VS-ia64-JIT/V2.0-Beta2/b184799/b184799.cs`** -> AI Confidence: **99.29%**
2945. **`src/tests/JIT/Regression/VS-ia64-JIT/V2.0-RTM/b539509/b539509.cs`** -> AI Confidence: **99.29%**
2946. **`src/tests/JIT/jit64/eh/FinallyExec/nestedTryRegionsWithSameOffset1.cs`** -> AI Confidence: **99.29%**
2947. **`src/tests/JIT/jit64/eh/FinallyExec/nestedTryRegionsWithSameOffset3.cs`** -> AI Confidence: **99.29%**
2948. **`src/tests/JIT/jit64/opt/cse/arrayexpr1.cs`** -> AI Confidence: **99.29%**
2949. **`src/tests/JIT/jit64/opt/cse/arrayexpr2.cs`** -> AI Confidence: **99.29%**
2950. **`src/tests/JIT/jit64/opt/cse/fieldExprUnchecked1.cs`** -> AI Confidence: **99.29%**
2951. **`src/tests/JIT/jit64/opt/cse/fieldexpr1.cs`** -> AI Confidence: **99.29%**
2952. **`src/tests/JIT/jit64/opt/cse/fieldexpr1_1.cs`** -> AI Confidence: **99.29%**
2953. **`src/tests/JIT/jit64/opt/cse/fieldexpr2.cs`** -> AI Confidence: **99.29%**
2954. **`src/tests/JIT/jit64/opt/cse/mixedexpr1.cs`** -> AI Confidence: **99.29%**
2955. **`src/tests/JIT/jit64/opt/cse/simpleexpr1.cs`** -> AI Confidence: **99.29%**
2956. **`src/tests/JIT/jit64/opt/cse/simpleexpr1_1.cs`** -> AI Confidence: **99.29%**
2957. **`src/tests/JIT/jit64/opt/cse/simpleexpr2.cs`** -> AI Confidence: **99.29%**
2958. **`src/tests/JIT/jit64/opt/cse/simpleexpr3.cs`** -> AI Confidence: **99.29%**
2959. **`src/tests/JIT/jit64/opt/cse/simpleexpr4.cs`** -> AI Confidence: **99.29%**
2960. **`src/tests/JIT/jit64/opt/cse/staticFieldExpr1.cs`** -> AI Confidence: **99.29%**
2961. **`src/tests/JIT/jit64/opt/cse/staticFieldExpr1_1.cs`** -> AI Confidence: **99.29%**
2962. **`src/tests/JIT/jit64/opt/cse/staticFieldExprUnchecked1.cs`** -> AI Confidence: **99.29%**
2963. **`src/tests/JIT/jit64/opt/cse/volatilefield.cs`** -> AI Confidence: **99.29%**
2964. **`src/tests/JIT/jit64/opt/cse/volatilestaticfield.cs`** -> AI Confidence: **99.29%**
2965. **`src/tests/JIT/jit64/opt/lur/lur_02.cs`** -> AI Confidence: **99.29%**
2966. **`src/tests/JIT/jit64/regress/vsw/524070/test1.cs`** -> AI Confidence: **99.29%**
2967. **`src/tests/JIT/jit64/regress/vsw/524070/test2.cs`** -> AI Confidence: **99.29%**
2968. **`src/tests/JIT/jit64/regress/vsw/539509/test1.cs`** -> AI Confidence: **99.29%**
2969. **`src/tests/Loader/classloader/explicitlayout/misc/case10.cs`** -> AI Confidence: **99.29%**
2970. **`src/tests/Loader/classloader/explicitlayout/objrefandnonobjrefoverlap/case9.cs`** -> AI Confidence: **99.29%**
2971. **`src/tests/baseservices/exceptions/generics/GenericExceptions.cs`** -> AI Confidence: **99.29%**
2972. **`src/tests/baseservices/exceptions/regressions/V1/SEH/VJ/TryCatch.cs`** -> AI Confidence: **99.29%**
2973. **`src/tests/nativeaot/SmokeTests/FrameworkStrings/Program.cs`** -> AI Confidence: **99.29%**
2974. **`src/tests/tracing/common/Assert.cs`** -> AI Confidence: **99.29%**
2975. **`src/tools/ilasm/src/ILAssembler/StringHelpers.cs`** -> AI Confidence: **99.29%**
2976. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Assertions/KeptBaseOnTypeInAssemblyAttribute.cs`** -> AI Confidence: **99.29%**
2977. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Assertions/KeptInterfaceOnTypeInAssemblyAttribute.cs`** -> AI Confidence: **99.29%**
2978. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Assertions/RemovedInterfaceOnTypeInAssemblyAttribute.cs`** -> AI Confidence: **99.29%**
2979. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Metadata/SetupCompileAfterAttribute.cs`** -> AI Confidence: **99.29%**
2980. **`src/tools/illink/test/Mono.Linker.Tests.Cases.Expectations/Metadata/SetupCompileBeforeAttribute.cs`** -> AI Confidence: **99.29%**
2981. **`src/tools/illink/test/Mono.Linker.Tests.Cases/RequiresCapability/Dependencies/RequiresInCopyAssembly.cs`** -> AI Confidence: **99.29%**
2982. **`src/native/external/libunwind/configure.ac`** -> AI Confidence: **99.29%**
2983. **`src/coreclr/inc/llvm/Dwarf.def`** -> AI Confidence: **99.29%**
2984. **`src/native/external/libunwind/Makefile.am`** -> AI Confidence: **99.29%**
2985. **`src/mono/browser/runtime/es6/dotnet.es6.pre.js`** -> AI Confidence: **99.29%**
2986. **`src/coreclr/ilasm/asmparse.y`** -> AI Confidence: **99.29%**
2987. **`src/libraries/Common/tests/System/Net/EnterpriseTests/setup/apacheweb/Dockerfile`** -> AI Confidence: **99.29%**
2988. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/Dockerfile`** -> AI Confidence: **99.29%**
2989. **`src/native/libs/Common/JavaScript/loader/config.ts`** -> AI Confidence: **99.29%**
2990. **`src/native/libs/System.Globalization.Native/pal_calendarData.m`** -> AI Confidence: **99.29%**
2991. **`src/native/libs/System.Globalization.Native/pal_casing.m`** -> AI Confidence: **99.29%**
2992. **`src/native/libs/System.Globalization.Native/pal_collation.m`** -> AI Confidence: **99.29%**
2993. **`src/native/libs/System.Globalization.Native/pal_normalization.m`** -> AI Confidence: **99.29%**
2994. **`src/native/libs/System.Globalization.Native/pal_timeZoneInfo.m`** -> AI Confidence: **99.29%**
2995. **`src/native/libs/System.Native/pal_datetime.m`** -> AI Confidence: **99.29%**
2996. **`src/native/libs/System.Native/pal_log.m`** -> AI Confidence: **99.29%**
2997. **`src/native/libs/System.Native/pal_searchpath.m`** -> AI Confidence: **99.29%**
2998. **`src/native/libs/System.Security.Cryptography.Native.Apple/pal_networkframework.m`** -> AI Confidence: **99.29%**
2999. **`src/tasks/AppleAppBuilder/Templates/util.m`** -> AI Confidence: **99.29%**
3000. **`src/native/external/libunwind/src/x86_64/Gtrace.c`** -> AI Confidence: **99.28%**
3001. **`src/coreclr/inc/winwrap.h`** -> AI Confidence: **99.27%**
3002. **`src/coreclr/jit/emitdef.h`** -> AI Confidence: **99.27%**
3003. **`src/coreclr/jit/emitfmts.h`** -> AI Confidence: **99.27%**
3004. **`src/coreclr/jit/instrs.h`** -> AI Confidence: **99.27%**
3005. **`src/coreclr/jit/register.h`** -> AI Confidence: **99.27%**
3006. **`src/native/external/zlib-ng/zendian.h`** -> AI Confidence: **99.27%**
3007. **`src/coreclr/pal/inc/strsafe.h`** -> AI Confidence: **99.26%**
3008. **`src/mono/mono/utils/mono-threads-debug.h`** -> AI Confidence: **99.26%**
3009. **`src/native/external/zlib-ng/inflate_p.h`** -> AI Confidence: **99.26%**
3010. **`src/coreclr/scripts/jitutil.py`** -> AI Confidence: **99.25%**
3011. **`src/mono/mono/metadata/handle.h`** -> AI Confidence: **99.25%**
3012. **`src/mono/mono/utils/mono-os-mutex.h`** -> AI Confidence: **99.25%**
3013. **`src/native/external/brotli/c/common/platform.h`** -> AI Confidence: **99.25%**
3014. **`src/native/external/libunwind/src/x86_64/Gos-freebsd.c`** -> AI Confidence: **99.25%**
3015. **`src/native/external/libunwind/tests/Gtest-resume-sig.c`** -> AI Confidence: **99.25%**
3016. **`src/native/external/zstd/lib/common/xxhash.h`** -> AI Confidence: **99.25%**
3017. **`src/coreclr/gc/gc.cpp`** -> AI Confidence: **99.25%**
3018. **`src/coreclr/gc/gcee.cpp`** -> AI Confidence: **99.25%**
3019. **`src/coreclr/gc/vxsort/vxsort.h`** -> AI Confidence: **99.25%**
3020. **`src/coreclr/inc/stresslog.h`** -> AI Confidence: **99.25%**
3021. **`src/mono/mono/utils/mono-os-semaphore.h`** -> AI Confidence: **99.25%**
3022. **`src/native/external/llvm-libunwind/src/AddressSpace.hpp`** -> AI Confidence: **99.25%**
3023. **`src/native/external/llvm-libunwind/src/DwarfParser.hpp`** -> AI Confidence: **99.25%**
3024. **`src/native/external/rapidjson/reader.h`** -> AI Confidence: **99.25%**
3025. **`src/native/external/zlib-ng/inffast_tpl.h`** -> AI Confidence: **99.25%**
3026. **`src/native/libs/Common/pal_error_common.h`** -> AI Confidence: **99.25%**
3027. **`src/native/minipal/thread.h`** -> AI Confidence: **99.25%**
3028. **`src/libraries/System.Net.Http/src/System/Net/Http/WasiHttpHandler/WasiHttpWorld.wit.imports.wasi.io.v0_2_0.IStreams.cs`** -> AI Confidence: **99.25%**
3029. **`src/tests/Common/scripts/crossgen2_comparison.py`** -> AI Confidence: **99.24%**
3030. **`src/coreclr/pal/src/include/pal/context.h`** -> AI Confidence: **99.24%**
3031. **`src/mono/mono/eglib/glib.h`** -> AI Confidence: **99.24%**
3032. **`src/mono/mono/eglib/test/module.c`** -> AI Confidence: **99.24%**
3033. **`src/mono/mono/eventpipe/ds-rt-mono.c`** -> AI Confidence: **99.24%**
3034. **`src/mono/mono/eventpipe/ep-rt-mono.c`** -> AI Confidence: **99.24%**
3035. **`src/mono/mono/eventpipe/test/ep-buffer-tests.c`** -> AI Confidence: **99.24%**
3036. **`src/mono/mono/metadata/dynamic-stream.c`** -> AI Confidence: **99.24%**
3037. **`src/mono/mono/metadata/environment.c`** -> AI Confidence: **99.24%**
3038. **`src/mono/mono/metadata/icall-table.c`** -> AI Confidence: **99.24%**
3039. **`src/mono/mono/metadata/mono-config.c`** -> AI Confidence: **99.24%**
3040. **`src/mono/mono/mini/exceptions-x86.c`** -> AI Confidence: **99.24%**
3041. **`src/mono/mono/mini/mini-cross-helpers.c`** -> AI Confidence: **99.24%**
3042. **`src/mono/mono/mini/mini-s390x.h`** -> AI Confidence: **99.24%**
3043. **`src/mono/mono/mini/mini.h`** -> AI Confidence: **99.24%**
3044. **`src/mono/mono/sgen/sgen-nursery-allocator.c`** -> AI Confidence: **99.24%**
3045. **`src/mono/mono/utils/mono-dl.c`** -> AI Confidence: **99.24%**
3046. **`src/mono/mono/utils/mono-log-posix.c`** -> AI Confidence: **99.24%**
3047. **`src/mono/mono/utils/mono-log-windows.c`** -> AI Confidence: **99.24%**
3048. **`src/mono/mono/utils/mono-mmap-wasm.c`** -> AI Confidence: **99.24%**
3049. **`src/mono/mono/utils/mono-threads-posix-signals.c`** -> AI Confidence: **99.24%**
3050. **`src/mono/mono/utils/mono-threads-windows.c`** -> AI Confidence: **99.24%**
3051. **`src/native/eventpipe/ep-file.c`** -> AI Confidence: **99.24%**
3052. **`src/native/eventpipe/ep-provider.c`** -> AI Confidence: **99.24%**
3053. **`src/native/external/libunwind/src/s390x/Ginit.c`** -> AI Confidence: **99.24%**
3054. **`src/native/external/libunwind/tests/ia64-test-dyn1.c`** -> AI Confidence: **99.24%**
3055. **`src/native/external/libunwind/tests/ia64-test-setjmp.c`** -> AI Confidence: **99.24%**
3056. **`src/native/external/llvm-libunwind/src/UnwindLevel1.c`** -> AI Confidence: **99.24%**
3057. **`src/native/external/zlib-ng/arch/x86/chunkset_avx512.c`** -> AI Confidence: **99.24%**
3058. **`src/native/external/zstd/lib/legacy/zstd_v04.c`** -> AI Confidence: **99.24%**
3059. **`src/native/external/zstd/lib/legacy/zstd_v07.c`** -> AI Confidence: **99.24%**
3060. **`src/native/libs/System.Native/entrypoints.c`** -> AI Confidence: **99.24%**
3061. **`src/native/libs/System.Native/pal_console.c`** -> AI Confidence: **99.24%**
3062. **`src/native/libs/System.Native/pal_datetime.c`** -> AI Confidence: **99.24%**
3063. **`src/native/libs/System.Native/pal_networkstatistics.c`** -> AI Confidence: **99.24%**
3064. **`src/native/libs/System.Native/pal_signal.c`** -> AI Confidence: **99.24%**
3065. **`src/native/libs/System.Native/pal_threading.c`** -> AI Confidence: **99.24%**
3066. **`src/native/libs/System.Security.Cryptography.Native/opensslshim.h`** -> AI Confidence: **99.24%**
3067. **`src/tasks/AndroidAppBuilder/Templates/monodroid-coreclr.c`** -> AI Confidence: **99.24%**
3068. **`src/tasks/AndroidAppBuilder/Templates/monodroid.c`** -> AI Confidence: **99.24%**
3069. **`src/coreclr/gc/vxsort/standalone/simple_bench/demo.cpp`** -> AI Confidence: **99.24%**
3070. **`src/coreclr/inc/palclr.h`** -> AI Confidence: **99.24%**
3071. **`src/coreclr/md/compiler/regmeta_compilersupport.cpp`** -> AI Confidence: **99.24%**
3072. **`src/coreclr/nativeaot/Runtime/ThunksMapping.cpp`** -> AI Confidence: **99.24%**
3073. **`src/coreclr/nativeaot/Runtime/event.cpp`** -> AI Confidence: **99.24%**
3074. **`src/coreclr/nativeaot/Runtime/windows/CoffNativeCodeManager.cpp`** -> AI Confidence: **99.24%**
3075. **`src/coreclr/nativeaot/Runtime/windows/PalMinWin.cpp`** -> AI Confidence: **99.24%**
3076. **`src/coreclr/pal/src/exception/seh.cpp`** -> AI Confidence: **99.24%**
3077. **`src/coreclr/pal/src/exception/signal.cpp`** -> AI Confidence: **99.24%**
3078. **`src/coreclr/pal/src/loader/module.cpp`** -> AI Confidence: **99.24%**
3079. **`src/coreclr/utilcode/safewrap.cpp`** -> AI Confidence: **99.24%**
3080. **`src/mono/mono/mini/mini-llvm-cpp.cpp`** -> AI Confidence: **99.24%**
3081. **`src/native/corehost/comhost/clsidmap.cpp`** -> AI Confidence: **99.24%**
3082. **`src/native/corehost/hostmisc/pal.windows.cpp`** -> AI Confidence: **99.24%**
3083. **`src/native/eventpipe/ep-rt-config.h`** -> AI Confidence: **99.24%**
3084. **`src/native/external/brotli/c/enc/hash.h`** -> AI Confidence: **99.24%**
3085. **`src/native/external/brotli/c/enc/quality.h`** -> AI Confidence: **99.24%**
3086. **`src/native/external/libunwind/include/tdep-mips/libunwind_i.h`** -> AI Confidence: **99.24%**
3087. **`src/native/external/llvm-libunwind/src/Unwind-seh.cpp`** -> AI Confidence: **99.24%**
3088. **`src/native/external/rapidjson/writer.h`** -> AI Confidence: **99.24%**
3089. **`src/native/external/zstd/lib/common/zstd_internal.h`** -> AI Confidence: **99.24%**
3090. **`src/native/minipal/getexepath.h`** -> AI Confidence: **99.24%**
3091. **`src/tests/nativeaot/SmokeTests/PInvoke/PInvokeNative.cpp`** -> AI Confidence: **99.24%**
3092. **`src/coreclr/System.Private.CoreLib/src/Internal/Runtime/InteropServices/ComActivator.cs`** -> AI Confidence: **99.24%**
3093. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/DynamicMethod.CoreCLR.cs`** -> AI Confidence: **99.24%**
3094. **`src/coreclr/nativeaot/System.Private.CoreLib/src/Internal/Reflection/Augments/ReflectionAugments.cs`** -> AI Confidence: **99.24%**
3095. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/GC.NativeAot.cs`** -> AI Confidence: **99.24%**
3096. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/MethodInfos/RuntimeMethodInfo.cs`** -> AI Confidence: **99.24%**
3097. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/CompilerServices/RuntimeHelpers.NativeAot.cs`** -> AI Confidence: **99.24%**
3098. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/NativeLayoutInfoLoadContext.cs`** -> AI Confidence: **99.24%**
3099. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.ConstructedGenericMethodsLookup.cs`** -> AI Confidence: **99.24%**
3100. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Runtime/TypeLoader/TypeLoaderEnvironment.ConstructedGenericTypesLookup.cs`** -> AI Confidence: **99.24%**
3101. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/TypeSystem/RuntimeNoMetadataType.cs`** -> AI Confidence: **99.24%**
3102. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/TypeSystem/TypeSystemContext.Runtime.cs`** -> AI Confidence: **99.24%**
3103. **`src/coreclr/tools/ILTrim.Core/ModuleWriter.cs`** -> AI Confidence: **99.24%**
3104. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Dataflow/GenericArgumentDataFlow.cs`** -> AI Confidence: **99.24%**
3105. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/InterfaceGenericVirtualMethodTableNode.cs`** -> AI Confidence: **99.24%**
3106. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/Logger.cs`** -> AI Confidence: **99.24%**
3107. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/MstatObjectDumper.cs`** -> AI Confidence: **99.24%**
3108. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/SubstitutionProvider.cs`** -> AI Confidence: **99.24%**
3109. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun.Tests/TestCasesRunner/R2RResultChecker.cs`** -> AI Confidence: **99.24%**
3110. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunCompilationModuleGroupBase.cs`** -> AI Confidence: **99.24%**
3111. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunTableManager.cs`** -> AI Confidence: **99.24%**
3112. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/AssemblyChecker.cs`** -> AI Confidence: **99.24%**
3113. **`src/coreclr/tools/aot/ILCompiler.Trimming.Tests/TestCasesRunner/MemberAssertionsCollector.cs`** -> AI Confidence: **99.24%**
3114. **`src/coreclr/tools/dotnet-pgo/MethodMemoryMap.cs`** -> AI Confidence: **99.24%**
3115. **`src/coreclr/tools/dotnet-pgo/MibcEmitter.cs`** -> AI Confidence: **99.24%**
3116. **`src/coreclr/tools/dotnet-pgo/PgoRootCommand.cs`** -> AI Confidence: **99.24%**
3117. **`src/coreclr/tools/dotnet-pgo/TraceTypeSystemContext.cs`** -> AI Confidence: **99.24%**
3118. **`src/coreclr/tools/dotnet-pgo/TypeRefTypeSystem/TypeRefTypeSystemContext.cs`** -> AI Confidence: **99.24%**
3119. **`src/coreclr/tools/dotnet-pgo/TypeRefTypeSystem/TypeRefTypeSystemType.cs`** -> AI Confidence: **99.24%**
3120. **`src/installer/managed/Microsoft.NET.HostModel/ComHost/ClsidMap.cs`** -> AI Confidence: **99.24%**
3121. **`src/installer/tests/TestUtils/Command.cs`** -> AI Confidence: **99.24%**
3122. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.Aead.cs`** -> AI Confidence: **99.24%**
3123. **`src/libraries/Common/src/Interop/Unix/System.Native/Interop.MountPoints.cs`** -> AI Confidence: **99.24%**
3124. **`src/libraries/Common/src/System/Net/Http/X509ResourceClient.cs`** -> AI Confidence: **99.24%**
3125. **`src/libraries/Common/src/System/Net/Security/CertificateValidation.Windows.cs`** -> AI Confidence: **99.24%**
3126. **`src/libraries/Common/src/System/Security/Cryptography/CompositeMLDsaManaged.cs`** -> AI Confidence: **99.24%**
3127. **`src/libraries/Common/src/System/Security/Cryptography/RSACng.SignVerify.cs`** -> AI Confidence: **99.24%**
3128. **`src/libraries/Common/tests/SourceGenerators/RoslynTestUtils.cs`** -> AI Confidence: **99.24%**
3129. **`src/libraries/Common/tests/System/Net/Configuration.Certificates.cs`** -> AI Confidence: **99.24%**
3130. **`src/libraries/Common/tests/System/Net/Http/Http2LoopbackConnection.cs`** -> AI Confidence: **99.24%**
3131. **`src/libraries/Common/tests/System/Net/Http/HttpClientHandlerTest.Decompression.cs`** -> AI Confidence: **99.24%**
3132. **`src/libraries/Common/tests/System/Net/Http/LoopbackProxyServer.cs`** -> AI Confidence: **99.24%**
3133. **`src/libraries/Common/tests/System/Net/Http/LoopbackServer.cs`** -> AI Confidence: **99.24%**
3134. **`src/libraries/Common/tests/TestUtilities/System/IO/FileCleanupTestBase.cs`** -> AI Confidence: **99.24%**
3135. **`src/libraries/Common/tests/Tests/System/Net/aspnetcore/Http2/DynamicTableTest.cs`** -> AI Confidence: **99.24%**
3136. **`src/libraries/Fuzzing/DotnetFuzzing/Fuzzers/Utf8JsonReaderFuzzer.cs`** -> AI Confidence: **99.24%**
3137. **`src/libraries/Microsoft.Extensions.Caching.Abstractions/src/Hybrid/HybridCache.cs`** -> AI Confidence: **99.24%**
3138. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/ServiceLookup/CallSiteRuntimeResolver.cs`** -> AI Confidence: **99.24%**
3139. **`src/libraries/Microsoft.Extensions.FileProviders.Physical/src/PollingWildCardChangeToken.cs`** -> AI Confidence: **99.24%**
3140. **`src/libraries/Microsoft.Extensions.Hosting/src/HostApplicationBuilder.cs`** -> AI Confidence: **99.24%**
3141. **`src/libraries/Microsoft.Extensions.Logging.EventSource/src/EventSourceLogger.cs`** -> AI Confidence: **99.24%**
3142. **`src/libraries/Microsoft.Win32.SystemEvents/tests/SystemEvents.CreateTimer.cs`** -> AI Confidence: **99.24%**
3143. **`src/libraries/System.Collections.Concurrent/tests/ProducerConsumerCollectionTests.cs`** -> AI Confidence: **99.24%**
3144. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/DirectoryCatalog.cs`** -> AI Confidence: **99.24%**
3145. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Hosting/TypeCatalog.cs`** -> AI Confidence: **99.24%**
3146. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/Primitives/ContractBasedImportDefinition.cs`** -> AI Confidence: **99.24%**
3147. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/ReflectionModelServices.cs`** -> AI Confidence: **99.24%**
3148. **`src/libraries/System.Data.Common/src/System/Data/Common/DbProviderFactories.cs`** -> AI Confidence: **99.24%**
3149. **`src/libraries/System.Data.Common/src/System/Data/Common/SqlUDTStorage.cs`** -> AI Confidence: **99.24%**
3150. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLBoolean.cs`** -> AI Confidence: **99.24%**
3151. **`src/libraries/System.Data.OleDb/src/OleDbConnectionFactory.cs`** -> AI Confidence: **99.24%**
3152. **`src/libraries/System.Diagnostics.DiagnosticSource/tests/MetricOuterLoopTests/Common.cs`** -> AI Confidence: **99.24%**
3153. **`src/libraries/System.Diagnostics.Process/tests/ProcessStartInfoTests.cs`** -> AI Confidence: **99.24%**
3154. **`src/libraries/System.Diagnostics.Process/tests/ProcessTests.cs`** -> AI Confidence: **99.24%**
3155. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/TokenGroupsSet.cs`** -> AI Confidence: **99.24%**
3156. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarHelpers.cs`** -> AI Confidence: **99.24%**
3157. **`src/libraries/System.IO.Compression/tests/CompressionStreamUnitTests.ZLib.cs`** -> AI Confidence: **99.24%**
3158. **`src/libraries/System.IO.Ports/tests/SerialPort/GetPortNames.cs`** -> AI Confidence: **99.24%**
3159. **`src/libraries/System.IO.Ports/tests/SerialStream/WriteTimeout.cs`** -> AI Confidence: **99.24%**
3160. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/DelegateHelpers.cs`** -> AI Confidence: **99.24%**
3161. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Expression.cs`** -> AI Confidence: **99.24%**
3162. **`src/libraries/System.Linq.Parallel/src/System/Linq/Parallel/QueryOperators/PartitionerQueryOperator.cs`** -> AI Confidence: **99.24%**
3163. **`src/libraries/System.Management/src/System/Management/InteropClasses/WMIInterop.cs`** -> AI Confidence: **99.24%**
3164. **`src/libraries/System.Memory.Data/src/System/BinaryData.cs`** -> AI Confidence: **99.24%**
3165. **`src/libraries/System.Memory/tests/Span/StringSearchValues.cs`** -> AI Confidence: **99.24%**
3166. **`src/libraries/System.Net.Http.WinHttpHandler/tests/UnitTests/FakeInterop.cs`** -> AI Confidence: **99.24%**
3167. **`src/libraries/System.Net.Http/src/System/Net/Http/HttpClientHandler.AnyMobile.cs`** -> AI Confidence: **99.24%**
3168. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/Program.cs`** -> AI Confidence: **99.24%**
3169. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/StressClient.cs`** -> AI Confidence: **99.24%**
3170. **`src/libraries/System.Net.Http/tests/StressTests/HttpStress/StressServer.cs`** -> AI Confidence: **99.24%**
3171. **`src/libraries/System.Net.Http/tests/UnitTests/HttpWindowsProxyTest.cs`** -> AI Confidence: **99.24%**
3172. **`src/libraries/System.Net.Mail/tests/Functional/LoopbackServerTestBase.cs`** -> AI Confidence: **99.24%**
3173. **`src/libraries/System.Net.Primitives/src/System/Net/IPAddress.cs`** -> AI Confidence: **99.24%**
3174. **`src/libraries/System.Net.Quic/src/System/Net/Quic/QuicListener.cs`** -> AI Confidence: **99.24%**
3175. **`src/libraries/System.Net.Security/tests/FunctionalTests/TestHelper.cs`** -> AI Confidence: **99.24%**
3176. **`src/libraries/System.Net.Security/tests/StressTests/SslStress/Program.cs`** -> AI Confidence: **99.24%**
3177. **`src/libraries/System.Net.Security/tests/StressTests/SslStress/StressOperations.cs`** -> AI Confidence: **99.24%**
3178. **`src/libraries/System.Net.WebClient/src/System/Net/WebClient.cs`** -> AI Confidence: **99.24%**
3179. **`src/libraries/System.Net.WebHeaderCollection/src/System/Net/WebHeaderCollection.cs`** -> AI Confidence: **99.24%**
3180. **`src/libraries/System.Private.CoreLib/src/System/AppDomain.cs`** -> AI Confidence: **99.24%**
3181. **`src/libraries/System.Private.CoreLib/src/System/Decimal.cs`** -> AI Confidence: **99.24%**
3182. **`src/libraries/System.Private.CoreLib/src/System/Globalization/TextInfo.cs`** -> AI Confidence: **99.24%**
3183. **`src/libraries/System.Private.CoreLib/src/System/IO/Stream.cs`** -> AI Confidence: **99.24%**
3184. **`src/libraries/System.Private.CoreLib/src/System/ReadOnlySpan.cs`** -> AI Confidence: **99.24%**
3185. **`src/libraries/System.Private.CoreLib/src/System/Reflection/Assembly.cs`** -> AI Confidence: **99.24%**
3186. **`src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/PoolingAsyncValueTaskMethodBuilderT.cs`** -> AI Confidence: **99.24%**
3187. **`src/libraries/System.Private.CoreLib/src/System/Runtime/InteropServices/NFloat.cs`** -> AI Confidence: **99.24%**
3188. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/SearchValues.cs`** -> AI Confidence: **99.24%**
3189. **`src/libraries/System.Private.CoreLib/src/System/Span.cs`** -> AI Confidence: **99.24%**
3190. **`src/libraries/System.Private.CoreLib/src/System/Threading/Thread.cs`** -> AI Confidence: **99.24%**
3191. **`src/libraries/System.Private.CoreLib/src/System/UInt16.cs`** -> AI Confidence: **99.24%**
3192. **`src/libraries/System.Private.CoreLib/src/System/UInt64.cs`** -> AI Confidence: **99.24%**
3193. **`src/libraries/System.Private.CoreLib/src/System/UIntPtr.cs`** -> AI Confidence: **99.24%**
3194. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/EnumDataContract.cs`** -> AI Confidence: **99.24%**
3195. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonClassDataContract.cs`** -> AI Confidence: **99.24%**
3196. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlDataContract.cs`** -> AI Confidence: **99.24%**
3197. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializer.cs`** -> AI Confidence: **99.24%**
3198. **`src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/XElement.cs`** -> AI Confidence: **99.24%**
3199. **`src/libraries/System.Private.Xml.Linq/tests/TrimmingTests/XElementCtor.cs`** -> AI Confidence: **99.24%**
3200. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/FunctionalTests.cs`** -> AI Confidence: **99.24%**
3201. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlValidatingReaderImplAsync.cs`** -> AI Confidence: **99.24%**
3202. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/DataTypeImplementation.cs`** -> AI Confidence: **99.24%**
3203. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/Compiler.cs`** -> AI Confidence: **99.24%**
3204. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/WhitespaceRuleLookup.cs`** -> AI Confidence: **99.24%**
3205. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlQueryRuntime.cs`** -> AI Confidence: **99.24%**
3206. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XsltFunctions.cs`** -> AI Confidence: **99.24%**
3207. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ActionFrame.cs`** -> AI Confidence: **99.24%**
3208. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/RootAction.cs`** -> AI Confidence: **99.24%**
3209. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/MetadataReader.cs`** -> AI Confidence: **99.24%**
3210. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/PortableExecutable/PEReader.cs`** -> AI Confidence: **99.24%**
3211. **`src/libraries/System.Reflection.MetadataLoadContext/src/System/Reflection/TypeLoading/Assemblies/RoAssembly.cs`** -> AI Confidence: **99.24%**
3212. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/Analyzers/RuntimeComApiUsageWithSourceGeneratedComAnalyzer.cs`** -> AI Confidence: **99.24%**
3213. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/VtableIndexStubGenerator.cs`** -> AI Confidence: **99.24%**
3214. **`src/libraries/System.Runtime.InteropServices/gen/DownlevelLibraryImportGenerator/DownlevelLibraryImportGenerator.cs`** -> AI Confidence: **99.24%**
3215. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/ConvertToLibraryImportFixer.cs`** -> AI Confidence: **99.24%**
3216. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/BoundGenerators.cs`** -> AI Confidence: **99.24%**
3217. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/UnmanagedToManagedStubGenerator.cs`** -> AI Confidence: **99.24%**
3218. **`src/libraries/System.Runtime.Serialization.Schema/src/System/Runtime/Serialization/Schema/ContractCodeDomInfo.cs`** -> AI Confidence: **99.24%**
3219. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/GCTests.cs`** -> AI Confidence: **99.24%**
3220. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/CESchedulerPairTests.cs`** -> AI Confidence: **99.24%**
3221. **`src/libraries/System.Security.Cryptography.Cose/tests/CoseTestHelpers.cs`** -> AI Confidence: **99.24%**
3222. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.Decode.cs`** -> AI Confidence: **99.24%**
3223. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.Encrypt.cs`** -> AI Confidence: **99.24%**
3224. **`src/libraries/System.Security.Cryptography.Pkcs/tests/SignedCms/SignerInfoTests.cs`** -> AI Confidence: **99.24%**
3225. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/Helpers.cs`** -> AI Confidence: **99.24%**
3226. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/Pbkdf2Implementation.Windows.cs`** -> AI Confidence: **99.24%**
3227. **`src/libraries/System.Security.Cryptography/tests/X509Certificates/DynamicChainTests.cs`** -> AI Confidence: **99.24%**
3228. **`src/libraries/System.Speech/src/Recognition/GrammarBuilder.cs`** -> AI Confidence: **99.24%**
3229. **`src/libraries/System.Speech/src/Recognition/SrgsGrammar/SrgsDocument.cs`** -> AI Confidence: **99.24%**
3230. **`src/libraries/System.Speech/src/Synthesis/SpeechSynthesizer.cs`** -> AI Confidence: **99.24%**
3231. **`src/libraries/System.Speech/src/Synthesis/VoiceInfo.cs`** -> AI Confidence: **99.24%**
3232. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Serialization/MetadataTests/DefaultJsonTypeInfoResolverTests.JsonPropertyInfo.cs`** -> AI Confidence: **99.24%**
3233. **`src/libraries/System.Text.Json/tests/System.Text.Json.Tests/Utf8JsonWriterTests.cs`** -> AI Confidence: **99.24%**
3234. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/Regex.KnownPattern.Tests.cs`** -> AI Confidence: **99.24%**
3235. **`src/libraries/System.Transactions.Local/tests/TransactionTracingEventListener.cs`** -> AI Confidence: **99.24%**
3236. **`src/mono/System.Private.CoreLib/src/System/Reflection/RuntimeMethodInfo.Mono.cs`** -> AI Confidence: **99.24%**
3237. **`src/mono/browser/debugger/BrowserDebugProxy/DebugStore.cs`** -> AI Confidence: **99.24%**
3238. **`src/mono/browser/debugger/BrowserDebugProxy/DevToolsProxy.cs`** -> AI Confidence: **99.24%**
3239. **`src/mono/browser/debugger/BrowserDebugProxy/Firefox/FirefoxMonoProxy.cs`** -> AI Confidence: **99.24%**
3240. **`src/mono/browser/debugger/BrowserDebugProxy/MemberObjectsExplorer.cs`** -> AI Confidence: **99.24%**
3241. **`src/mono/browser/debugger/BrowserDebugProxy/ValueTypeClass.cs`** -> AI Confidence: **99.24%**
3242. **`src/mono/mono/tests/assembly-load-stress.cs`** -> AI Confidence: **99.24%**
3243. **`src/mono/mono/tests/remoting4.cs`** -> AI Confidence: **99.24%**
3244. **`src/mono/wasm/Wasm.Build.Tests/Blazor/BlazorWasmTestBase.cs`** -> AI Confidence: **99.24%**
3245. **`src/mono/wasm/Wasm.Build.Tests/Blazor/CleanTests.cs`** -> AI Confidence: **99.24%**
3246. **`src/mono/wasm/Wasm.Build.Tests/Blazor/WorkloadRequiredTests.cs`** -> AI Confidence: **99.24%**
3247. **`src/mono/wasm/Wasm.Build.Tests/ProjectProviderBase.cs`** -> AI Confidence: **99.24%**
3248. **`src/mono/wasm/host/DevServer/WebAssemblyNetDebugProxyAppBuilderExtensions.cs`** -> AI Confidence: **99.24%**
3249. **`src/native/managed/cdac/tests/TestPlaceholderTarget.cs`** -> AI Confidence: **99.24%**
3250. **`src/tasks/Common/FileCache.cs`** -> AI Confidence: **99.24%**
3251. **`src/tasks/MonoTargetsTasks/MarshalingPInvokeScanner/MarshalingPInvokeScanner.cs`** -> AI Confidence: **99.24%**
3252. **`src/tasks/WasmAppBuilder/IcallTableGenerator.cs`** -> AI Confidence: **99.24%**
3253. **`src/tasks/WasmAppBuilder/WasmLoadAssembliesAndReferences.cs`** -> AI Confidence: **99.24%**
3254. **`src/tasks/WasmAppBuilder/coreclr/ManagedToNativeGenerator.cs`** -> AI Confidence: **99.24%**
3255. **`src/tasks/WasmAppBuilder/coreclr/PInvokeTableGenerator.cs`** -> AI Confidence: **99.24%**
3256. **`src/tasks/WasmAppBuilder/mono/PInvokeTableGenerator.cs`** -> AI Confidence: **99.24%**
3257. **`src/tests/GC/Performance/Tests/LowLatencyTest.cs`** -> AI Confidence: **99.24%**
3258. **`src/tests/Interop/COM/Reflection/Reflection.cs`** -> AI Confidence: **99.24%**
3259. **`src/tests/JIT/Performance/CodeQuality/BenchmarksGame/fasta/fasta-1.cs`** -> AI Confidence: **99.24%**
3260. **`src/tests/JIT/Performance/CodeQuality/SIMD/RayTracer/RayTracerBench.cs`** -> AI Confidence: **99.24%**
3261. **`src/tests/JIT/Regression/JitBlue/Runtime_34587/Runtime_34587.cs`** -> AI Confidence: **99.24%**
3262. **`src/tests/Regressions/coreclr/GitHub_45929/test45929.cs`** -> AI Confidence: **99.24%**
3263. **`src/tests/nativeaot/SmokeTests/DynamicGenerics/B282745.cs`** -> AI Confidence: **99.24%**
3264. **`src/tests/nativeaot/SmokeTests/DynamicGenerics/GenericVirtualMethods.cs`** -> AI Confidence: **99.24%**
3265. **`src/tests/nativeaot/SmokeTests/DynamicGenerics/fieldreflection.cs`** -> AI Confidence: **99.24%**
3266. **`src/tests/profiler/eventpipe/eventpipe.cs`** -> AI Confidence: **99.24%**
3267. **`src/tests/tracing/eventcounter/regression-46938.cs`** -> AI Confidence: **99.24%**
3268. **`src/tests/tracing/eventpipe/common/Microsoft.Diagnostics.NETCore.Client/DiagnosticsClient/DiagnosticsClient.cs`** -> AI Confidence: **99.24%**
3269. **`src/tests/tracing/eventpipe/processinfo3/processinfo3.cs`** -> AI Confidence: **99.24%**
3270. **`src/tests/tracing/userevents/common/UserEventsTestRunner.cs`** -> AI Confidence: **99.24%**
3271. **`src/tools/StressLogAnalyzer/src/StressLogAnalyzer.cs`** -> AI Confidence: **99.24%**
3272. **`src/tools/illink/src/ILLink.CodeFix/BaseAttributeCodeFixProvider.cs`** -> AI Confidence: **99.24%**
3273. **`src/tools/illink/src/ILLink.CodeFix/RequiresUnsafeCodeFixProvider.cs`** -> AI Confidence: **99.24%**
3274. **`src/tools/illink/src/ILLink.RoslynAnalyzer/DataFlow/FeatureChecksVisitor.cs`** -> AI Confidence: **99.24%**
3275. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/TrimAnalysisVisitor.cs`** -> AI Confidence: **99.24%**
3276. **`src/tools/illink/src/linker/Linker/LinkContext.cs`** -> AI Confidence: **99.24%**
3277. **`src/tools/illink/src/linker/Linker/TypeNameResolver.cs`** -> AI Confidence: **99.24%**
3278. **`src/tools/illink/test/ILLink.RoslynAnalyzer.Tests/TestChecker.cs`** -> AI Confidence: **99.24%**
3279. **`src/tools/illink/test/Mono.Linker.Tests/TestCasesRunner/TestCaseCollector.cs`** -> AI Confidence: **99.24%**
3280. **`src/mono/browser/runtime/rollup.config.js`** -> AI Confidence: **99.24%**
3281. **`src/mono/browser/runtime/cancelable-promise.ts`** -> AI Confidence: **99.24%**
3282. **`src/mono/browser/runtime/interp-pgo.ts`** -> AI Confidence: **99.24%**
3283. **`src/mono/browser/runtime/pthreads/worker-thread.ts`** -> AI Confidence: **99.24%**
3284. **`src/mono/browser/runtime/roots.ts`** -> AI Confidence: **99.24%**
3285. **`src/mono/browser/runtime/startup.ts`** -> AI Confidence: **99.24%**
3286. **`src/native/libs/Common/JavaScript/loader/run.ts`** -> AI Confidence: **99.24%**
3287. **`src/coreclr/scripts/antigen_run.py`** -> AI Confidence: **99.23%**
3288. **`src/coreclr/scripts/fuzzlyn_run.py`** -> AI Confidence: **99.23%**
3289. **`src/coreclr/scripts/pgocheck.py`** -> AI Confidence: **99.23%**
3290. **`src/native/external/brotli/setup.py`** -> AI Confidence: **99.23%**
3291. **`src/mono/mono/eglib/test/timer.c`** -> AI Confidence: **99.23%**
3292. **`src/mono/mono/metadata/w32event-unix.c`** -> AI Confidence: **99.23%**
3293. **`src/mono/mono/mini/interp/mintops.h`** -> AI Confidence: **99.23%**
3294. **`src/mono/mono/mini/llvm-intrinsics.h`** -> AI Confidence: **99.23%**
3295. **`src/mono/mono/utils/atomic.h`** -> AI Confidence: **99.23%**
3296. **`src/native/external/brotli/c/enc/bit_cost.h`** -> AI Confidence: **99.23%**
3297. **`src/native/external/brotli/c/enc/dictionary_hash.h`** -> AI Confidence: **99.23%**
3298. **`src/native/external/brotli/c/enc/literal_cost.h`** -> AI Confidence: **99.23%**
3299. **`src/native/external/brotli/c/enc/utf8_util.h`** -> AI Confidence: **99.23%**
3300. **`src/native/external/libunwind/src/aarch64/Gos-freebsd.c`** -> AI Confidence: **99.23%**
3301. **`src/native/external/libunwind/src/dwarf/Gparser.c`** -> AI Confidence: **99.23%**
3302. **`src/native/external/libunwind/src/ia64/unwind_decoder.h`** -> AI Confidence: **99.23%**
3303. **`src/native/external/libunwind/src/nto/unw_nto_destroy.c`** -> AI Confidence: **99.23%**
3304. **`src/native/external/libunwind/src/x86_64/Gget_save_loc.c`** -> AI Confidence: **99.23%**
3305. **`src/native/external/libunwind/src/x86_64/Gstash_frame.c`** -> AI Confidence: **99.23%**
3306. **`src/native/external/libunwind/tests/test-reg-state.c`** -> AI Confidence: **99.23%**
3307. **`src/native/external/zlib-ng/arch/arm/neon_intrins.h`** -> AI Confidence: **99.23%**
3308. **`src/native/external/zlib-ng/arch/power/power_features.c`** -> AI Confidence: **99.23%**
3309. **`src/native/external/zlib-ng/arch/x86/crc32_fold_pclmulqdq_tpl.h`** -> AI Confidence: **99.23%**
3310. **`src/native/external/zstd/lib/decompress/zstd_ddict.c`** -> AI Confidence: **99.23%**
3311. **`src/native/libs/System.Security.Cryptography.Native.Apple/pal_x509_macos.c`** -> AI Confidence: **99.23%**
3312. **`src/coreclr/dlls/mscorpe/ceefilegenwriter.cpp`** -> AI Confidence: **99.23%**
3313. **`src/coreclr/gc/allocation.cpp`** -> AI Confidence: **99.23%**
3314. **`src/coreclr/gc/background.cpp`** -> AI Confidence: **99.23%**
3315. **`src/coreclr/gc/card_table.cpp`** -> AI Confidence: **99.23%**
3316. **`src/coreclr/gc/collect.cpp`** -> AI Confidence: **99.23%**
3317. **`src/coreclr/gc/dac_gcheap_fields.h`** -> AI Confidence: **99.23%**
3318. **`src/coreclr/gc/dac_generation_fields.h`** -> AI Confidence: **99.23%**
3319. **`src/coreclr/gc/diagnostics.cpp`** -> AI Confidence: **99.23%**
3320. **`src/coreclr/gc/dynamic_heap_count.cpp`** -> AI Confidence: **99.23%**
3321. **`src/coreclr/gc/dynamic_tuning.cpp`** -> AI Confidence: **99.23%**
3322. **`src/coreclr/gc/gcenv.inl`** -> AI Confidence: **99.23%**
3323. **`src/coreclr/gc/handletableconstants.h`** -> AI Confidence: **99.23%**
3324. **`src/coreclr/gc/handletablecore.cpp`** -> AI Confidence: **99.23%**
3325. **`src/coreclr/gc/no_gc.cpp`** -> AI Confidence: **99.23%**
3326. **`src/coreclr/gc/plan_phase.cpp`** -> AI Confidence: **99.23%**
3327. **`src/coreclr/gc/region_allocator.cpp`** -> AI Confidence: **99.23%**
3328. **`src/coreclr/gc/regions_segments.cpp`** -> AI Confidence: **99.23%**
3329. **`src/coreclr/gc/relocate_compact.cpp`** -> AI Confidence: **99.23%**
3330. **`src/coreclr/gc/softwarewritewatch.cpp`** -> AI Confidence: **99.23%**
3331. **`src/coreclr/gc/sweep.cpp`** -> AI Confidence: **99.23%**
3332. **`src/coreclr/gc/vxsort/vxsort_targets_disable.h`** -> AI Confidence: **99.23%**
3333. **`src/coreclr/gc/vxsort/vxsort_targets_enable_avx2.h`** -> AI Confidence: **99.23%**
3334. **`src/coreclr/gc/vxsort/vxsort_targets_enable_avx512.h`** -> AI Confidence: **99.23%**
3335. **`src/coreclr/ilasm/asmman.cpp`** -> AI Confidence: **99.23%**
3336. **`src/coreclr/ildasm/resource.h`** -> AI Confidence: **99.23%**
3337. **`src/coreclr/inc/dlwrap.h`** -> AI Confidence: **99.23%**
3338. **`src/coreclr/inc/optsmallperfcritical.h`** -> AI Confidence: **99.23%**
3339. **`src/coreclr/interpreter/interpconfigvalues.h`** -> AI Confidence: **99.23%**
3340. **`src/coreclr/interpreter/intops.cpp`** -> AI Confidence: **99.23%**
3341. **`src/coreclr/jit/fgwasm.h`** -> AI Confidence: **99.23%**
3342. **`src/coreclr/jit/opcode.h`** -> AI Confidence: **99.23%**
3343. **`src/coreclr/jit/target.h`** -> AI Confidence: **99.23%**
3344. **`src/coreclr/jit/valuenum.cpp`** -> AI Confidence: **99.23%**
3345. **`src/coreclr/jit/valuenumfuncs.h`** -> AI Confidence: **99.23%**
3346. **`src/coreclr/md/debug_metadata.h`** -> AI Confidence: **99.23%**
3347. **`src/coreclr/md/enc/rwutil.cpp`** -> AI Confidence: **99.23%**
3348. **`src/coreclr/md/inc/mdlog.h`** -> AI Confidence: **99.23%**
3349. **`src/coreclr/md/inc/metamodel.h`** -> AI Confidence: **99.23%**
3350. **`src/coreclr/nativeaot/Runtime/GCMemoryHelpers.inl`** -> AI Confidence: **99.23%**
3351. **`src/coreclr/nativeaot/Runtime/eventtrace_etw.h`** -> AI Confidence: **99.23%**
3352. **`src/coreclr/nativeaot/Runtime/profheapwalkhelper.cpp`** -> AI Confidence: **99.23%**
3353. **`src/coreclr/pal/inc/rt/guiddef.h`** -> AI Confidence: **99.23%**
3354. **`src/coreclr/pal/src/safecrt/input.inl`** -> AI Confidence: **99.23%**
3355. **`src/coreclr/pal/src/safecrt/internal_securecrt.h`** -> AI Confidence: **99.23%**
3356. **`src/coreclr/pal/src/safecrt/tcscat_s.inl`** -> AI Confidence: **99.23%**
3357. **`src/coreclr/pal/src/safecrt/tcscpy_s.inl`** -> AI Confidence: **99.23%**
3358. **`src/coreclr/pal/src/safecrt/tcsncat_s.inl`** -> AI Confidence: **99.23%**
3359. **`src/coreclr/pal/src/safecrt/tcsncpy_s.inl`** -> AI Confidence: **99.23%**
3360. **`src/coreclr/pal/tests/palsuite/threading/WaitForMultipleObjectsEx/test5/commonconsts.h`** -> AI Confidence: **99.23%**
3361. **`src/coreclr/runtime/MiscNativeHelpers.h`** -> AI Confidence: **99.23%**
3362. **`src/coreclr/tools/aot/jitinterface/dllexport.h`** -> AI Confidence: **99.23%**
3363. **`src/coreclr/utilcode/ex.cpp`** -> AI Confidence: **99.23%**
3364. **`src/coreclr/utilcode/loaderheap_shared.cpp`** -> AI Confidence: **99.23%**
3365. **`src/coreclr/utilcode/sstring.cpp`** -> AI Confidence: **99.23%**
3366. **`src/coreclr/vm/appdomainnative.cpp`** -> AI Confidence: **99.23%**
3367. **`src/coreclr/vm/classhash.cpp`** -> AI Confidence: **99.23%**
3368. **`src/coreclr/vm/eehash.cpp`** -> AI Confidence: **99.23%**
3369. **`src/coreclr/vm/gchelpers.inl`** -> AI Confidence: **99.23%**
3370. **`src/coreclr/vm/peimagelayout.cpp`** -> AI Confidence: **99.23%**
3371. **`src/coreclr/vm/perfmap.cpp`** -> AI Confidence: **99.23%**
3372. **`src/coreclr/vm/rtlfunctions.h`** -> AI Confidence: **99.23%**
3373. **`src/coreclr/vm/syncclean.cpp`** -> AI Confidence: **99.23%**
3374. **`src/mono/mono/metadata/object-offsets.h`** -> AI Confidence: **99.23%**
3375. **`src/mono/mono/sgen/sgen-protocol-def.h`** -> AI Confidence: **99.23%**
3376. **`src/mono/mono/sgen/sgen-scan-object.h`** -> AI Confidence: **99.23%**
3377. **`src/mono/mono/utils/options-def.h`** -> AI Confidence: **99.23%**
3378. **`src/native/corehost/bundle/runner.cpp`** -> AI Confidence: **99.23%**
3379. **`src/native/corehost/fxr_resolver.cpp`** -> AI Confidence: **99.23%**
3380. **`src/native/corehost/json_parser.cpp`** -> AI Confidence: **99.23%**
3381. **`src/native/eventpipe/ds-getter-setter.h`** -> AI Confidence: **99.23%**
3382. **`src/native/eventpipe/ds-rt-config.h`** -> AI Confidence: **99.23%**
3383. **`src/native/external/brotli/c/common/version.h`** -> AI Confidence: **99.23%**
3384. **`src/native/external/brotli/c/enc/cluster_inc.h`** -> AI Confidence: **99.23%**
3385. **`src/native/external/llvm-libunwind/src/libunwind.cpp`** -> AI Confidence: **99.23%**
3386. **`src/native/external/llvm-libunwind/src/shadow_stack_unwind.h`** -> AI Confidence: **99.23%**
3387. **`src/native/external/zlib-ng/crc32_braid_p.h`** -> AI Confidence: **99.23%**
3388. **`src/native/external/zlib-ng/match_tpl.h`** -> AI Confidence: **99.23%**
3389. **`src/native/external/zstd/lib/zstd_errors.h`** -> AI Confidence: **99.23%**
3390. **`src/tests/profiler/native/eltprofiler/slowpatheltprofiler.cpp`** -> AI Confidence: **99.23%**
3391. **`src/tests/profiler/native/metadatagetdispenser/metadatagetdispenser.cpp`** -> AI Confidence: **99.23%**
3392. **`src/coreclr/System.Private.CoreLib/src/System/Array.CoreCLR.cs`** -> AI Confidence: **99.23%**
3393. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/SignatureHelper.cs`** -> AI Confidence: **99.23%**
3394. **`src/coreclr/nativeaot/Common/src/Internal/Runtime/CompilerHelpers/StartupCodeHelpers.cs`** -> AI Confidence: **99.23%**
3395. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Diagnostics/StackFrame.NativeAot.cs`** -> AI Confidence: **99.23%**
3396. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Exception.NativeAot.cs`** -> AI Confidence: **99.23%**
3397. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Reflection/Runtime/General/ThunkedApis.cs`** -> AI Confidence: **99.23%**
3398. **`src/coreclr/nativeaot/System.Private.Reflection.Execution/src/Internal/Reflection/Execution/ExecutionEnvironmentImplementation.ManifestResources.cs`** -> AI Confidence: **99.23%**
3399. **`src/coreclr/nativeaot/System.Private.TypeLoader/src/Internal/Reflection/Execution/AssemblyBinderImplementation.cs`** -> AI Confidence: **99.23%**
3400. **`src/coreclr/tools/Common/Compiler/CompilerTypeSystemContext.cs`** -> AI Confidence: **99.23%**
3401. **`src/coreclr/tools/Common/Pgo/PgoFormat.cs`** -> AI Confidence: **99.23%**
3402. **`src/coreclr/tools/Common/TypeSystem/Common/Utilities/LockFreeReaderHashtableOfPointers.cs`** -> AI Confidence: **99.23%**
3403. **`src/coreclr/tools/Common/TypeSystem/Ecma/EcmaType.cs`** -> AI Confidence: **99.23%**
3404. **`src/coreclr/tools/Common/TypeSystem/IL/ILDisassembler.cs`** -> AI Confidence: **99.23%**
3405. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/DehydratedDataNode.cs`** -> AI Confidence: **99.23%**
3406. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/NativeLayoutVertexNode.cs`** -> AI Confidence: **99.23%**
3407. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/ReflectionVirtualInvokeMapNode.cs`** -> AI Confidence: **99.23%**
3408. **`src/coreclr/tools/aot/ILCompiler.Compiler/Compiler/DependencyAnalysis/StackTraceLineNumbersNode.cs`** -> AI Confidence: **99.23%**
3409. **`src/coreclr/tools/aot/ILCompiler.MetadataTransform/ILCompiler/Metadata/Transform.CustomAttribute.cs`** -> AI Confidence: **99.23%**
3410. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/CryptographicHashProvider.cs`** -> AI Confidence: **99.23%**
3411. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/DebugDirectoryNode.cs`** -> AI Confidence: **99.23%**
3412. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/MethodWithGCInfo.cs`** -> AI Confidence: **99.23%**
3413. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/ReadyToRunInstructionSetSupportSignature.cs`** -> AI Confidence: **99.23%**
3414. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/ReadyToRunStandaloneMethodMetadata.cs`** -> AI Confidence: **99.23%**
3415. **`src/coreclr/tools/aot/ILCompiler.RyuJit/Compiler/DependencyAnalysis/MethodCodeNode.cs`** -> AI Confidence: **99.23%**
3416. **`src/coreclr/tools/dotnet-pgo/Microsoft.Diagnostics.JitTrace/JitTraceRuntime.cs`** -> AI Confidence: **99.23%**
3417. **`src/installer/tests/HostActivation.Tests/HostCommands.cs`** -> AI Confidence: **99.23%**
3418. **`src/installer/tests/HostActivation.Tests/RegisteredInstallLocationOverride.cs`** -> AI Confidence: **99.23%**
3419. **`src/libraries/Common/src/Interop/OSX/System.Security.Cryptography.Native.Apple/Interop.SecKeyRef.macOS.cs`** -> AI Confidence: **99.23%**
3420. **`src/libraries/Common/src/System/Security/Cryptography/RSAOpenSsl.cs`** -> AI Confidence: **99.23%**
3421. **`src/libraries/Common/tests/System/IO/Compression/EncoderDecoderTestBase.cs`** -> AI Confidence: **99.23%**
3422. **`src/libraries/Common/tests/System/Net/Http/LoopbackServer.AuthenticationHelpers.cs`** -> AI Confidence: **99.23%**
3423. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ComInterop/ComInvokeBinder.cs`** -> AI Confidence: **99.23%**
3424. **`src/libraries/Microsoft.CSharp/src/Microsoft/CSharp/RuntimeBinder/ComInterop/ComTypeLibDesc.cs`** -> AI Confidence: **99.23%**
3425. **`src/libraries/Microsoft.Extensions.Caching.Memory/src/CacheEntry.cs`** -> AI Confidence: **99.23%**
3426. **`src/libraries/Microsoft.Extensions.Configuration.Xml/src/XmlStreamConfigurationProvider.cs`** -> AI Confidence: **99.23%**
3427. **`src/libraries/Microsoft.Extensions.DependencyInjection/src/ServiceProvider.cs`** -> AI Confidence: **99.23%**
3428. **`src/libraries/Microsoft.Extensions.FileProviders.Physical/src/PhysicalFileProvider.cs`** -> AI Confidence: **99.23%**
3429. **`src/libraries/Microsoft.Extensions.HostFactoryResolver/src/HostFactoryResolver.cs`** -> AI Confidence: **99.23%**
3430. **`src/libraries/System.CodeDom/tests/System/CodeDom/Compiler/CodeGenerationTests.cs`** -> AI Confidence: **99.23%**
3431. **`src/libraries/System.Collections.Concurrent/tests/BlockingCollectionTests.cs`** -> AI Confidence: **99.23%**
3432. **`src/libraries/System.Collections.Immutable/src/System/Collections/Frozen/FrozenDictionary.cs`** -> AI Confidence: **99.23%**
3433. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ExportServices.cs`** -> AI Confidence: **99.23%**
3434. **`src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/ReflectionModel/GenericSpecializationPartCreationInfo.cs`** -> AI Confidence: **99.23%**
3435. **`src/libraries/System.Composition.TypedParts/src/System/Composition/TypedParts/Discovery/TypeInspector.cs`** -> AI Confidence: **99.23%**
3436. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/ConfigurationErrorsException.cs`** -> AI Confidence: **99.23%**
3437. **`src/libraries/System.Console/tests/Color.cs`** -> AI Confidence: **99.23%**
3438. **`src/libraries/System.Data.Common/src/System/Data/Common/DbDataReader.cs`** -> AI Confidence: **99.23%**
3439. **`src/libraries/System.Data.Common/src/System/Data/Common/SQLTypes/SQLStringStorage.cs`** -> AI Confidence: **99.23%**
3440. **`src/libraries/System.Data.Common/src/System/Data/DataViewManager.cs`** -> AI Confidence: **99.23%**
3441. **`src/libraries/System.Data.Common/src/System/Data/LinqDataView.cs`** -> AI Confidence: **99.23%**
3442. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLBinary.cs`** -> AI Confidence: **99.23%**
3443. **`src/libraries/System.Data.Common/src/System/Data/SQLTypes/SQLInt64.cs`** -> AI Confidence: **99.23%**
3444. **`src/libraries/System.Data.Common/src/System/Data/XMLDiffLoader.cs`** -> AI Confidence: **99.23%**
3445. **`src/libraries/System.Data.Common/tests/System/Data/SqlTypes/SqlStringSortingTest.cs`** -> AI Confidence: **99.23%**
3446. **`src/libraries/System.Data.Odbc/src/Common/System/Data/Common/DBConnectionString.cs`** -> AI Confidence: **99.23%**
3447. **`src/libraries/System.Data.Odbc/src/System/Data/Odbc/OdbcCommand.cs`** -> AI Confidence: **99.23%**
3448. **`src/libraries/System.Data.OleDb/src/DbPropSet.cs`** -> AI Confidence: **99.23%**
3449. **`src/libraries/System.Data.OleDb/src/OleDbException.cs`** -> AI Confidence: **99.23%**
3450. **`src/libraries/System.Diagnostics.Process/src/System/Diagnostics/Process.Multiplexing.Windows.cs`** -> AI Confidence: **99.23%**
3451. **`src/libraries/System.Diagnostics.Process/tests/ProcessMultiplexingTests.cs`** -> AI Confidence: **99.23%**
3452. **`src/libraries/System.Diagnostics.Process/tests/ProcessThreadTests.cs`** -> AI Confidence: **99.23%**
3453. **`src/libraries/System.Diagnostics.TraceSource/src/System/Diagnostics/Switch.cs`** -> AI Confidence: **99.23%**
3454. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/SAM/SAMStoreCtx.cs`** -> AI Confidence: **99.23%**
3455. **`src/libraries/System.DirectoryServices.Protocols/src/System/DirectoryServices/Protocols/ldap/LdapPartialResultsProcessor.cs`** -> AI Confidence: **99.23%**
3456. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/ActiveDirectorySiteLinkBridge.cs`** -> AI Confidence: **99.23%**
3457. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarEntry.cs`** -> AI Confidence: **99.23%**
3458. **`src/libraries/System.Formats.Tar/src/System/Formats/Tar/TarFile.cs`** -> AI Confidence: **99.23%**
3459. **`src/libraries/System.Formats.Tar/tests/TarTestsBase.cs`** -> AI Confidence: **99.23%**
3460. **`src/libraries/System.IO.Compression/src/System/IO/Compression/ZipBlocks.cs`** -> AI Confidence: **99.23%**
3461. **`src/libraries/System.IO.Packaging/src/System/IO/Packaging/ZipStreamManager.cs`** -> AI Confidence: **99.23%**
3462. **`src/libraries/System.IO.Pipes/src/Microsoft/Win32/SafeHandles/SafePipeHandle.Unix.cs`** -> AI Confidence: **99.23%**
3463. **`src/libraries/System.IO.Ports/tests/SerialPort/BaudRate.cs`** -> AI Confidence: **99.23%**
3464. **`src/libraries/System.IO.Ports/tests/SerialPort/Parity.cs`** -> AI Confidence: **99.23%**
3465. **`src/libraries/System.IO.Ports/tests/SerialPort/PortName.cs`** -> AI Confidence: **99.23%**
3466. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadByte_Generic.cs`** -> AI Confidence: **99.23%**
3467. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadLine.cs`** -> AI Confidence: **99.23%**
3468. **`src/libraries/System.IO.Ports/tests/SerialPort/Read_char_int_int_Generic.cs`** -> AI Confidence: **99.23%**
3469. **`src/libraries/System.IO.Ports/tests/SerialPort/StopBits.cs`** -> AI Confidence: **99.23%**
3470. **`src/libraries/System.IO.Ports/tests/SerialStream/ReadByte_Generic.cs`** -> AI Confidence: **99.23%**
3471. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Unary.cs`** -> AI Confidence: **99.23%**
3472. **`src/libraries/System.Management/src/System/Management/ManagementQuery.cs`** -> AI Confidence: **99.23%**
3473. **`src/libraries/System.Net.Http.Json/src/System/Net/Http/Json/HttpClientJsonExtensions.cs`** -> AI Confidence: **99.23%**
3474. **`src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpResponseStream.cs`** -> AI Confidence: **99.23%**
3475. **`src/libraries/System.Net.Http/src/System/Net/Http/HttpClient.cs`** -> AI Confidence: **99.23%**
3476. **`src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/HttpConnectionPoolManager.cs`** -> AI Confidence: **99.23%**
3477. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpListenerContext.Windows.cs`** -> AI Confidence: **99.23%**
3478. **`src/libraries/System.Net.HttpListener/src/System/Net/Windows/HttpResponseStream.Windows.cs`** -> AI Confidence: **99.23%**
3479. **`src/libraries/System.Net.Mail/src/System/Net/Mail/SmtpTransport.cs`** -> AI Confidence: **99.23%**
3480. **`src/libraries/System.Net.NameResolution/src/System/Net/NameResolutionPal.Unix.cs`** -> AI Confidence: **99.23%**
3481. **`src/libraries/System.Net.NetworkInformation/src/System/Net/NetworkInformation/NetworkAddressChange.Windows.cs`** -> AI Confidence: **99.23%**
3482. **`src/libraries/System.Net.Ping/src/System/Net/NetworkInformation/Ping.PingUtility.cs`** -> AI Confidence: **99.23%**
3483. **`src/libraries/System.Net.Quic/src/System/Net/Quic/Internal/ValueTaskSource.cs`** -> AI Confidence: **99.23%**
3484. **`src/libraries/System.Net.Security/src/System/Net/Security/CipherSuitesPolicyPal.Linux.cs`** -> AI Confidence: **99.23%**
3485. **`src/libraries/System.Net.WebSockets.Client/tests/LoopbackServer/WebSocketHandshakeHelper.cs`** -> AI Confidence: **99.23%**
3486. **`src/libraries/System.Numerics.Tensors/src/System/Numerics/Tensors/netcore/TensorPrimitives.HammingDistance.cs`** -> AI Confidence: **99.23%**
3487. **`src/libraries/System.Private.CoreLib/src/Microsoft/Win32/SafeHandles/SafeFileHandle.Windows.cs`** -> AI Confidence: **99.23%**
3488. **`src/libraries/System.Private.CoreLib/src/System/Buffer.cs`** -> AI Confidence: **99.23%**
3489. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Binary/BinaryPrimitives.ReverseEndianness.cs`** -> AI Confidence: **99.23%**
3490. **`src/libraries/System.Private.CoreLib/src/System/Buffers/Text/Base64Url/Base64UrlDecoder.cs`** -> AI Confidence: **99.23%**
3491. **`src/libraries/System.Private.CoreLib/src/System/Char.cs`** -> AI Confidence: **99.23%**
3492. **`src/libraries/System.Private.CoreLib/src/System/Exception.cs`** -> AI Confidence: **99.23%**
3493. **`src/libraries/System.Private.CoreLib/src/System/Globalization/HebrewNumber.cs`** -> AI Confidence: **99.23%**
3494. **`src/libraries/System.Private.CoreLib/src/System/IO/TextWriter.CreateBroadcasting.cs`** -> AI Confidence: **99.23%**
3495. **`src/libraries/System.Private.CoreLib/src/System/Int16.cs`** -> AI Confidence: **99.23%**
3496. **`src/libraries/System.Private.CoreLib/src/System/Resources/ResourceReader.Core.cs`** -> AI Confidence: **99.23%**
3497. **`src/libraries/System.Private.CoreLib/src/System/SByte.cs`** -> AI Confidence: **99.23%**
3498. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/IndexOfAnyAsciiSearcher.cs`** -> AI Confidence: **99.23%**
3499. **`src/libraries/System.Private.CoreLib/src/System/SearchValues/Strings/Helpers/AhoCorasick.cs`** -> AI Confidence: **99.23%**
3500. **`src/libraries/System.Private.CoreLib/src/System/SpanHelpers.ByteMemOps.cs`** -> AI Confidence: **99.23%**
3501. **`src/libraries/System.Private.CoreLib/src/System/Text/Ascii.Equality.cs`** -> AI Confidence: **99.23%**
3502. **`src/libraries/System.Private.CoreLib/src/System/Text/Encoding.Internal.cs`** -> AI Confidence: **99.23%**
3503. **`src/libraries/System.Private.CoreLib/src/System/Threading/CancellationTokenSource.cs`** -> AI Confidence: **99.23%**
3504. **`src/libraries/System.Private.CoreLib/src/System/TimeZoneInfo.Cache.cs`** -> AI Confidence: **99.23%**
3505. **`src/libraries/System.Private.CoreLib/src/System/UInt32.cs`** -> AI Confidence: **99.23%**
3506. **`src/libraries/System.Private.CoreLib/src/System/Version.cs`** -> AI Confidence: **99.23%**
3507. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonCollectionDataContract.cs`** -> AI Confidence: **99.23%**
3508. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/Json/JsonFormatGeneratorStatics.cs`** -> AI Confidence: **99.23%**
3509. **`src/libraries/System.Private.DataContractSerialization/src/System/Runtime/Serialization/XmlObjectSerializerContext.cs`** -> AI Confidence: **99.23%**
3510. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBinaryReader.cs`** -> AI Confidence: **99.23%**
3511. **`src/libraries/System.Private.DataContractSerialization/src/System/Xml/XmlBinaryWriterSession.cs`** -> AI Confidence: **99.23%**
3512. **`src/libraries/System.Private.Uri/src/System/UriHelper.cs`** -> AI Confidence: **99.23%**
3513. **`src/libraries/System.Private.Xml.Linq/tests/xNodeReader/ReadValue.cs`** -> AI Confidence: **99.23%**
3514. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlCharCheckingReader.cs`** -> AI Confidence: **99.23%**
3515. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlEventCache.cs`** -> AI Confidence: **99.23%**
3516. **`src/libraries/System.Private.Xml/src/System/Xml/Core/XmlWellFormedWriterHelpers.cs`** -> AI Confidence: **99.23%**
3517. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/DocumentXmlWriter.cs`** -> AI Confidence: **99.23%**
3518. **`src/libraries/System.Private.Xml/src/System/Xml/Dom/XmlNodeReader.cs`** -> AI Confidence: **99.23%**
3519. **`src/libraries/System.Private.Xml/src/System/Xml/Resolvers/XmlPreloadedResolver.cs`** -> AI Confidence: **99.23%**
3520. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchema.cs`** -> AI Confidence: **99.23%**
3521. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XsdDateTime.cs`** -> AI Confidence: **99.23%**
3522. **`src/libraries/System.Private.Xml/src/System/Xml/Serialization/SchemaImporter.cs`** -> AI Confidence: **99.23%**
3523. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/StringFunctions.cs`** -> AI Confidence: **99.23%**
3524. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/XPathParser.cs`** -> AI Confidence: **99.23%**
3525. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/XPathDocument.cs`** -> AI Confidence: **99.23%**
3526. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/IlGen/XmlILModule.cs`** -> AI Confidence: **99.23%**
3527. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XslNumber.cs`** -> AI Confidence: **99.23%**
3528. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/ForEachAction.cs`** -> AI Confidence: **99.23%**
3529. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/XsltOld/TemplateLookupAction.cs`** -> AI Confidence: **99.23%**
3530. **`src/libraries/System.Private.Xml/src/System/Xml/Xslt/XslCompiledTransform.cs`** -> AI Confidence: **99.23%**
3531. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/EndOfLineHandlingTests.cs`** -> AI Confidence: **99.23%**
3532. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCFlushClose.cs`** -> AI Confidence: **99.23%**
3533. **`src/libraries/System.Private.Xml/tests/Writers/XmlWriterApi/TCFullEndElement.cs`** -> AI Confidence: **99.23%**
3534. **`src/libraries/System.Private.Xml/tests/XmlSchema/XmlSchemaValidatorApi/Initialize_EndValidation.cs`** -> AI Confidence: **99.23%**
3535. **`src/libraries/System.Reflection.Emit/src/System/Reflection/Emit/MethodBuilderImpl.cs`** -> AI Confidence: **99.23%**
3536. **`src/libraries/System.Reflection.MetadataLoadContext/src/System/Reflection/TypeLoading/CustomAttributes/Ecma/EcmaCustomAttributeHelpers.cs`** -> AI Confidence: **99.23%**
3537. **`src/libraries/System.Runtime.InteropServices.JavaScript/tests/System.Runtime.InteropServices.JavaScript.UnitTests/System/Runtime/InteropServices/JavaScript/WebWorkerTestHelper.cs`** -> AI Confidence: **99.23%**
3538. **`src/libraries/System.Runtime.InteropServices/gen/ComInterfaceGenerator/ComMethodInfo.cs`** -> AI Confidence: **99.23%**
3539. **`src/libraries/System.Runtime.InteropServices/gen/LibraryImportGenerator/Analyzers/ShapeBreakingDiagnosticSuppressor.cs`** -> AI Confidence: **99.23%**
3540. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/Marshalling/StatelessMarshallingStrategy.cs`** -> AI Confidence: **99.23%**
3541. **`src/libraries/System.Runtime.InteropServices/gen/Microsoft.Interop.SourceGeneration/SyntaxExtensions.cs`** -> AI Confidence: **99.23%**
3542. **`src/libraries/System.Runtime/tests/System.Dynamic.Runtime.Tests/Dynamic.DynamicType/Conformance.dynamic.dynamicType.conversions.cs`** -> AI Confidence: **99.23%**
3543. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/PseudoCustomAttributeTests.cs`** -> AI Confidence: **99.23%**
3544. **`src/libraries/System.Runtime/tests/System.Runtime.Tests/System/UIntPtrTests.cs`** -> AI Confidence: **99.23%**
3545. **`src/libraries/System.Runtime/tests/System.Threading.Tasks.Extensions.Tests/ValueTaskTests.cs`** -> AI Confidence: **99.23%**
3546. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/ObjectSecurity.cs`** -> AI Confidence: **99.23%**
3547. **`src/libraries/System.Security.AccessControl/tests/RawAcl/RawAcl_GetBinaryForm.cs`** -> AI Confidence: **99.23%**
3548. **`src/libraries/System.Security.AccessControl/tests/Utils.cs`** -> AI Confidence: **99.23%**
3549. **`src/libraries/System.Security.Claims/src/System/Security/Claims/ClaimsPrincipal.cs`** -> AI Confidence: **99.23%**
3550. **`src/libraries/System.Security.Cryptography.Pkcs/src/Internal/Cryptography/Pal/AnyOS/ManagedPal.Decrypt.cs`** -> AI Confidence: **99.23%**
3551. **`src/libraries/System.Security.Cryptography.Pkcs/src/System/Security/Cryptography/Pkcs/Rfc3161TimestampRequest.cs`** -> AI Confidence: **99.23%**
3552. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/KeyInfoX509Data.cs`** -> AI Confidence: **99.23%**
3553. **`src/libraries/System.Security.Cryptography.Xml/src/System/Security/Cryptography/Xml/SignedXmlDebugLog.cs`** -> AI Confidence: **99.23%**
3554. **`src/libraries/System.Security.Cryptography.Xml/tests/TestHelpers.cs`** -> AI Confidence: **99.23%**
3555. **`src/libraries/System.Security.Cryptography.Xml/tests/XmlLicenseEncryptedRef.cs`** -> AI Confidence: **99.23%**
3556. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/AppleCCCryptorLite.cs`** -> AI Confidence: **99.23%**
3557. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/CertificatePal.Windows.cs`** -> AI Confidence: **99.23%**
3558. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/OpenSslX509CertificateReader.cs`** -> AI Confidence: **99.23%**
3559. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/StorePal.Windows.Export.cs`** -> AI Confidence: **99.23%**
3560. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/X509Pal.Windows.PublicKey.cs`** -> AI Confidence: **99.23%**
3561. **`src/libraries/System.Security.Cryptography/tests/RandomNumberGeneratorTests.cs`** -> AI Confidence: **99.23%**
3562. **`src/libraries/System.ServiceModel.Syndication/tests/BasicScenarioTests.cs`** -> AI Confidence: **99.23%**
3563. **`src/libraries/System.Speech/src/Internal/SrgsCompiler/State.cs`** -> AI Confidence: **99.23%**
3564. **`src/libraries/System.Speech/src/Internal/Synthesis/TextFragmentEngine.cs`** -> AI Confidence: **99.23%**
3565. **`src/libraries/System.Speech/src/Internal/Synthesis/TextWriterEngine.cs`** -> AI Confidence: **99.23%**
3566. **`src/libraries/System.Text.Json/gen/Helpers/RoslynExtensions.cs`** -> AI Confidence: **99.23%**
3567. **`src/libraries/System.Text.Json/src/System/Text/Json/Reader/JsonReaderHelper.Unescaping.cs`** -> AI Confidence: **99.23%**
3568. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Object/ObjectDefaultConverter.cs`** -> AI Confidence: **99.23%**
3569. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonSerializer.Read.Pipe.cs`** -> AI Confidence: **99.23%**
3570. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Metadata/JsonPropertyInfo.cs`** -> AI Confidence: **99.23%**
3571. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/JsonWriterHelper.Escaping.cs`** -> AI Confidence: **99.23%**
3572. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/JsonWriterHelper.cs`** -> AI Confidence: **99.23%**
3573. **`src/libraries/System.Text.Json/src/System/Text/Json/Writer/Utf8JsonWriter.WriteProperties.Helpers.cs`** -> AI Confidence: **99.23%**
3574. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/RegexParser.cs`** -> AI Confidence: **99.23%**
3575. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/Symbolic/SymbolicRegexNode.cs`** -> AI Confidence: **99.23%**
3576. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/PrecompiledRegexScenarioTest.cs`** -> AI Confidence: **99.23%**
3577. **`src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/RegexExperiment.cs`** -> AI Confidence: **99.23%**
3578. **`src/libraries/System.Threading/src/System/Threading/Barrier.cs`** -> AI Confidence: **99.23%**
3579. **`src/libraries/System.Threading/tests/SemaphoreTests.cs`** -> AI Confidence: **99.23%**
3580. **`src/mono/System.Private.CoreLib/src/System/Delegate.Mono.cs`** -> AI Confidence: **99.23%**
3581. **`src/mono/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeModuleBuilder.Mono.cs`** -> AI Confidence: **99.23%**
3582. **`src/mono/System.Private.CoreLib/src/System/Reflection/RuntimePropertyInfo.cs`** -> AI Confidence: **99.23%**
3583. **`src/mono/browser/debugger/BrowserDebugProxy/MetadataDebugSummary.cs`** -> AI Confidence: **99.23%**
3584. **`src/mono/mono/tests/finally_guard.cs`** -> AI Confidence: **99.23%**
3585. **`src/mono/sample/wasm/browser-eventpipe/Program.cs`** -> AI Confidence: **99.23%**
3586. **`src/mono/wasm/Wasm.Build.Tests/IcuTestsBase.cs`** -> AI Confidence: **99.23%**
3587. **`src/mono/wasm/Wasm.Build.Tests/PInvokeTableGeneratorTests.cs`** -> AI Confidence: **99.23%**
3588. **`src/mono/wasm/host/wasi/WasiEngineHost.cs`** -> AI Confidence: **99.23%**
3589. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/RuntimeTypeSystem_1.cs`** -> AI Confidence: **99.23%**
3590. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/Contracts/StackWalk/Context/X86/GCInfoDecoding/GCInfo.cs`** -> AI Confidence: **99.23%**
3591. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Contracts/PrintfStressMessageFormatter.cs`** -> AI Confidence: **99.23%**
3592. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/ClrDataAppDomain.cs`** -> AI Confidence: **99.23%**
3593. **`src/tasks/Microsoft.NET.WebAssembly.Webcil/WebcilReader.cs`** -> AI Confidence: **99.23%**
3594. **`src/tasks/MobileBuildTasks/Apple/AppleProject.cs`** -> AI Confidence: **99.23%**
3595. **`src/tasks/WasmAppBuilder/mono/ManagedToNativeGenerator.cs`** -> AI Confidence: **99.23%**
3596. **`src/tasks/WasmAppBuilder/mono/PInvokeCollector.cs`** -> AI Confidence: **99.23%**
3597. **`src/tasks/WasmBuildTasks/GenerateAOTProps.cs`** -> AI Confidence: **99.23%**
3598. **`src/tasks/WorkloadBuildTasks/PackageInstaller.cs`** -> AI Confidence: **99.23%**
3599. **`src/tests/GC/Performance/Tests/GCSimulator.cs`** -> AI Confidence: **99.23%**
3600. **`src/tests/GC/Scenarios/GCSimulator/GCSimulator.cs`** -> AI Confidence: **99.23%**
3601. **`src/tests/JIT/Directed/StructPromote/Unsafe/ReadDoubleFromIntOffset.cs`** -> AI Confidence: **99.23%**
3602. **`src/tests/JIT/HardwareIntrinsics/X86/Regression/GitHub_17073/GitHub_17073_gen.csx`** -> AI Confidence: **99.23%**
3603. **`src/tests/JIT/HardwareIntrinsics/X86/Sse41/MultipleSumAbsoluteDifferences.cs`** -> AI Confidence: **99.23%**
3604. **`src/tests/JIT/Methodical/MDArray/DataTypes/int.cs`** -> AI Confidence: **99.23%**
3605. **`src/tests/JIT/Performance/CodeQuality/BenchmarksGame/reverse-complement/reverse-complement-6.cs`** -> AI Confidence: **99.23%**
3606. **`src/tests/JIT/Regression/VS-ia64-JIT/M00/b113493/bad.cs`** -> AI Confidence: **99.23%**
3607. **`src/tests/JIT/SIMD/VectorArray.cs`** -> AI Confidence: **99.23%**
3608. **`src/tests/JIT/SIMD/VectorSum.cs`** -> AI Confidence: **99.23%**
3609. **`src/tests/Loader/binding/assemblies/generics/arilistienum/methods/exceptions.cs`** -> AI Confidence: **99.23%**
3610. **`src/tests/Loader/classloader/TypeInitialization/CctorsWithSideEffects/CctorThrowInlinedStatic.cs`** -> AI Confidence: **99.23%**
3611. **`src/tests/async/varying-yields/varying-yields.cs`** -> AI Confidence: **99.23%**
3612. **`src/tests/baseservices/exceptions/simple/ParallelCrash.cs`** -> AI Confidence: **99.23%**
3613. **`src/tests/tracing/eventpipe/common/Microsoft.Diagnostics.NETCore.Client/ReversedServer/ReversedDiagnosticsServer.cs`** -> AI Confidence: **99.23%**
3614. **`src/tests/tracing/userevents/multithread/multithread.cs`** -> AI Confidence: **99.23%**
3615. **`src/tools/StressLogAnalyzer/src/Filters/ValueRangeFilter.cs`** -> AI Confidence: **99.23%**
3616. **`src/tools/StressLogAnalyzer/src/GCThreadMap.cs`** -> AI Confidence: **99.23%**
3617. **`src/tools/illink/src/ILLink.RoslynAnalyzer/COMAnalyzer.cs`** -> AI Confidence: **99.23%**
3618. **`src/tools/illink/src/ILLink.RoslynAnalyzer/ISymbolExtensions.cs`** -> AI Confidence: **99.23%**
3619. **`src/tools/illink/src/ILLink.RoslynAnalyzer/TrimAnalysis/TypeNameResolver.cs`** -> AI Confidence: **99.23%**
3620. **`src/tools/illink/src/linker/Linker.Dataflow/CompilerGeneratedState.cs`** -> AI Confidence: **99.23%**
3621. **`src/tools/illink/src/linker/Linker.Steps/BodySubstitutionParser.cs`** -> AI Confidence: **99.23%**
3622. **`src/tools/illink/src/linker/Linker.Steps/OutputStep.cs`** -> AI Confidence: **99.23%**
3623. **`src/tools/illink/src/tlens/TLens/Driver.cs`** -> AI Confidence: **99.23%**
3624. **`src/mono/browser/runtime/debug.ts`** -> AI Confidence: **99.23%**
3625. **`src/mono/browser/runtime/strings.ts`** -> AI Confidence: **99.23%**
3626. **`src/coreclr/scripts/superpmi_collect_setup.py`** -> AI Confidence: **99.22%**
3627. **`src/tests/Common/scripts/lst_creator.py`** -> AI Confidence: **99.22%**
3628. **`src/mono/mono/component/debugger-poll.c`** -> AI Confidence: **99.22%**
3629. **`src/mono/mono/eglib/gdate-unix.c`** -> AI Confidence: **99.22%**
3630. **`src/mono/mono/mini/aot-runtime-wasm.c`** -> AI Confidence: **99.22%**
3631. **`src/mono/mono/mini/optflags-def.h`** -> AI Confidence: **99.22%**
3632. **`src/mono/mono/mini/patch-info.h`** -> AI Confidence: **99.22%**
3633. **`src/native/external/libunwind/src/ptrace/_UPT_find_proc_info.c`** -> AI Confidence: **99.22%**
3634. **`src/native/external/libunwind/src/x86_64/ucontext_i.h`** -> AI Confidence: **99.22%**
3635. **`src/native/external/libunwind/tests/forker.c`** -> AI Confidence: **99.22%**
3636. **`src/native/external/zlib-ng/arch/power/compare256_power9.c`** -> AI Confidence: **99.22%**
3637. **`src/native/external/zlib-ng/arch/power/crc32_power8.c`** -> AI Confidence: **99.22%**
3638. **`src/native/external/zstd/lib/common/debug.h`** -> AI Confidence: **99.22%**
3639. **`src/native/external/zstd/lib/compress/zstd_ldm.c`** -> AI Confidence: **99.22%**
3640. **`src/native/libs/System.Globalization.Native/pal_localeStringData.c`** -> AI Confidence: **99.22%**
3641. **`src/native/minipal/utf8.c`** -> AI Confidence: **99.22%**
3642. **`src/native/public/mono/metadata/metadata.h`** -> AI Confidence: **99.22%**
3643. **`src/coreclr/inc/clrconfigvalues.h`** -> AI Confidence: **99.22%**
3644. **`src/coreclr/inc/debugmacrosext.h`** -> AI Confidence: **99.22%**
3645. **`src/coreclr/inc/jithelpers.h`** -> AI Confidence: **99.22%**
3646. **`src/coreclr/inc/staticcontract.h`** -> AI Confidence: **99.22%**
3647. **`src/coreclr/inc/switches.h`** -> AI Confidence: **99.22%**
3648. **`src/coreclr/jit/emitfmtsarm64sve.h`** -> AI Confidence: **99.22%**
3649. **`src/coreclr/jit/emitjmps.h`** -> AI Confidence: **99.22%**
3650. **`src/coreclr/jit/gtstructs.h`** -> AI Confidence: **99.22%**
3651. **`src/coreclr/jit/instr.cpp`** -> AI Confidence: **99.22%**
3652. **`src/coreclr/jit/instrsarm.h`** -> AI Confidence: **99.22%**
3653. **`src/coreclr/jit/instrsarm64.h`** -> AI Confidence: **99.22%**
3654. **`src/coreclr/jit/instrsarm64sve.h`** -> AI Confidence: **99.22%**
3655. **`src/coreclr/jit/instrsriscv64.h`** -> AI Confidence: **99.22%**
3656. **`src/coreclr/jit/jitconfigvalues.h`** -> AI Confidence: **99.22%**
3657. **`src/coreclr/jit/lowerriscv64.cpp`** -> AI Confidence: **99.22%**
3658. **`src/coreclr/jit/lsra_stats.h`** -> AI Confidence: **99.22%**
3659. **`src/coreclr/jit/regallocimpl.h`** -> AI Confidence: **99.22%**
3660. **`src/coreclr/jit/registerarm64.h`** -> AI Confidence: **99.22%**
3661. **`src/coreclr/jit/targetamd64.h`** -> AI Confidence: **99.22%**
3662. **`src/coreclr/jit/targetarm.h`** -> AI Confidence: **99.22%**
3663. **`src/coreclr/jit/targetarm64.h`** -> AI Confidence: **99.22%**
3664. **`src/coreclr/jit/targetloongarch64.h`** -> AI Confidence: **99.22%**
3665. **`src/coreclr/jit/targetriscv64.h`** -> AI Confidence: **99.22%**
3666. **`src/coreclr/jit/targetwasm.h`** -> AI Confidence: **99.22%**
3667. **`src/coreclr/jit/targetx86.h`** -> AI Confidence: **99.22%**
3668. **`src/coreclr/jitshared/jitshared.h`** -> AI Confidence: **99.22%**
3669. **`src/coreclr/md/compiler/assemblymd_emit.cpp`** -> AI Confidence: **99.22%**
3670. **`src/coreclr/md/compiler/emit.cpp`** -> AI Confidence: **99.22%**
3671. **`src/coreclr/md/enc/stgio.cpp`** -> AI Confidence: **99.22%**
3672. **`src/coreclr/md/inc/portablepdbmdi.h`** -> AI Confidence: **99.22%**
3673. **`src/coreclr/pal/inc/pal_assert.h`** -> AI Confidence: **99.22%**
3674. **`src/coreclr/pal/inc/rt/poppack.h`** -> AI Confidence: **99.22%**
3675. **`src/coreclr/pal/inc/rt/pshpack1.h`** -> AI Confidence: **99.22%**
3676. **`src/coreclr/pal/inc/rt/pshpack2.h`** -> AI Confidence: **99.22%**
3677. **`src/coreclr/pal/inc/rt/pshpack4.h`** -> AI Confidence: **99.22%**
3678. **`src/coreclr/pal/inc/rt/pshpack8.h`** -> AI Confidence: **99.22%**
3679. **`src/coreclr/pal/src/handlemgr/handleapi.cpp`** -> AI Confidence: **99.22%**
3680. **`src/coreclr/pal/src/objmgr/listedobjectmanager.cpp`** -> AI Confidence: **99.22%**
3681. **`src/coreclr/utilcode/clrhost_nodependencies.cpp`** -> AI Confidence: **99.22%**
3682. **`src/coreclr/utilcode/namespaceutil.cpp`** -> AI Confidence: **99.22%**
3683. **`src/coreclr/utilcode/pedecoder.cpp`** -> AI Confidence: **99.22%**
3684. **`src/coreclr/vm/FrameTypes.h`** -> AI Confidence: **99.22%**
3685. **`src/coreclr/vm/metasig.h`** -> AI Confidence: **99.22%**
3686. **`src/coreclr/vm/mtypes.h`** -> AI Confidence: **99.22%**
3687. **`src/coreclr/vm/peimage.cpp`** -> AI Confidence: **99.22%**
3688. **`src/coreclr/vm/tieredcompilation.cpp`** -> AI Confidence: **99.22%**
3689. **`src/coreclr/vm/wellknownattributes.h`** -> AI Confidence: **99.22%**
3690. **`src/native/corehost/configure.h.in`** -> AI Confidence: **99.22%**
3691. **`src/native/eventpipe/ep-rt-types.h`** -> AI Confidence: **99.22%**
3692. **`src/native/eventpipe/ep-shared-config.h.in`** -> AI Confidence: **99.22%**
3693. **`src/native/external/brotli/c/enc/find_match_length.h`** -> AI Confidence: **99.22%**
3694. **`src/native/external/llvm-libunwind/include/__libunwind_config.h`** -> AI Confidence: **99.22%**
3695. **`src/native/external/zstd/lib/common/portability_macros.h`** -> AI Confidence: **99.22%**
3696. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Emit/RuntimeILGenerator.cs`** -> AI Confidence: **99.22%**
3697. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Runtime/InteropServices/Marshal.Com.cs`** -> AI Confidence: **99.22%**
3698. **`src/coreclr/tools/Common/TypeSystem/IL/Stubs/ILEmitter.cs`** -> AI Confidence: **99.22%**
3699. **`src/coreclr/tools/aot/ILCompiler.ReadyToRun/Compiler/DependencyAnalysis/ReadyToRun/GCRefMapBuilder.cs`** -> AI Confidence: **99.22%**
3700. **`src/coreclr/tools/aot/ILCompiler.Reflection.ReadyToRun/Amd64/GcInfo.cs`** -> AI Confidence: **99.22%**
3701. **`src/libraries/Fuzzing/DotnetFuzzing/Fuzzers/NrbfDecoderFuzzer.cs`** -> AI Confidence: **99.22%**
3702. **`src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/ReflectPropertyDescriptor.cs`** -> AI Confidence: **99.22%**
3703. **`src/libraries/System.Configuration.ConfigurationManager/src/System/Configuration/LocalFileSettingsProvider.cs`** -> AI Confidence: **99.22%**
3704. **`src/libraries/System.Data.Common/src/System/Data/DataColumnCollection.cs`** -> AI Confidence: **99.22%**
3705. **`src/libraries/System.Data.Common/src/System/Data/XDRSchema.cs`** -> AI Confidence: **99.22%**
3706. **`src/libraries/System.Data.Odbc/src/Common/System/Data/Common/DbConnectionOptions.cs`** -> AI Confidence: **99.22%**
3707. **`src/libraries/System.Data.Odbc/src/Common/System/Data/ProviderBase/DbConnectionPool.cs`** -> AI Confidence: **99.22%**
3708. **`src/libraries/System.Diagnostics.TraceSource/src/System/Diagnostics/TraceSource.cs`** -> AI Confidence: **99.22%**
3709. **`src/libraries/System.DirectoryServices.AccountManagement/src/System/DirectoryServices/AccountManagement/AD/ADDNLinkedAttrSet.cs`** -> AI Confidence: **99.22%**
3710. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/DomainController.cs`** -> AI Confidence: **99.22%**
3711. **`src/libraries/System.DirectoryServices/src/System/DirectoryServices/ActiveDirectory/Forest.cs`** -> AI Confidence: **99.22%**
3712. **`src/libraries/System.Formats.Asn1/ref/System.Formats.Asn1.cs`** -> AI Confidence: **99.22%**
3713. **`src/libraries/System.IO.Pipes/ref/System.IO.Pipes.cs`** -> AI Confidence: **99.22%**
3714. **`src/libraries/System.IO.Ports/tests/SerialPort/ReadTimeout.cs`** -> AI Confidence: **99.22%**
3715. **`src/libraries/System.IO.Ports/tests/SerialPort/WriteTimeout.cs`** -> AI Confidence: **99.22%**
3716. **`src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/Compiler/LambdaCompiler.Binary.cs`** -> AI Confidence: **99.22%**
3717. **`src/libraries/System.Net.Primitives/src/System/Net/Cookie.cs`** -> AI Confidence: **99.22%**
3718. **`src/libraries/System.Private.CoreLib/src/System/Decimal.DecCalc.cs`** -> AI Confidence: **99.22%**
3719. **`src/libraries/System.Private.CoreLib/src/System/Globalization/CompareInfo.Icu.cs`** -> AI Confidence: **99.22%**
3720. **`src/libraries/System.Private.CoreLib/src/System/Globalization/DateTimeParse.cs`** -> AI Confidence: **99.22%**
3721. **`src/libraries/System.Private.CoreLib/src/System/Runtime/Intrinsics/VectorMath.cs`** -> AI Confidence: **99.22%**
3722. **`src/libraries/System.Private.CoreLib/src/System/SpanHelpers.Char.cs`** -> AI Confidence: **99.22%**
3723. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/Inference/Infer.cs`** -> AI Confidence: **99.22%**
3724. **`src/libraries/System.Private.Xml/src/System/Xml/Schema/XmlSchemaSet.cs`** -> AI Confidence: **99.22%**
3725. **`src/libraries/System.Private.Xml/src/System/Xml/XPath/Internal/QueryBuilder.cs`** -> AI Confidence: **99.22%**
3726. **`src/libraries/System.Private.Xml/src/System/Xml/Xsl/Runtime/XmlSequenceWriter.cs`** -> AI Confidence: **99.22%**
3727. **`src/libraries/System.Private.Xml/tests/Xslt/XslTransformApi/CXmlCache.cs`** -> AI Confidence: **99.22%**
3728. **`src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/TypeName.cs`** -> AI Confidence: **99.22%**
3729. **`src/libraries/System.Reflection.MetadataLoadContext/tests/src/Tests/Type/TypeInvariants.cs`** -> AI Confidence: **99.22%**
3730. **`src/libraries/System.Runtime.InteropServices/tests/System.Runtime.InteropServices.UnitTests/System/Runtime/InteropServices/NFloatTests.cs`** -> AI Confidence: **99.22%**
3731. **`src/libraries/System.Runtime.Serialization.Xml/tests/Canonicalization/XmlCanonicalizationTest.cs`** -> AI Confidence: **99.22%**
3732. **`src/libraries/System.Security.AccessControl/src/System/Security/AccessControl/ACL.cs`** -> AI Confidence: **99.22%**
3733. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/CertificateData.ManagedDecode.cs`** -> AI Confidence: **99.22%**
3734. **`src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/X509Certificates/CertificateRequest.Load.cs`** -> AI Confidence: **99.22%**
3735. **`src/libraries/System.Text.Json/src/System/Text/Json/Serialization/JsonSerializer.Read.HandleMetadata.cs`** -> AI Confidence: **99.22%**
3736. **`src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/Symbolic/RegexNodeConverter.cs`** -> AI Confidence: **99.22%**
3737. **`src/libraries/System.Transactions.Local/src/System/Transactions/Oletx/OletxVolatileEnlistment.cs`** -> AI Confidence: **99.22%**
3738. **`src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/TypeNameBuilder.cs`** -> AI Confidence: **99.22%**
3739. **`src/tests/GC/Features/PartialCompaction/eco1.cs`** -> AI Confidence: **99.22%**
3740. **`src/tests/GC/Stress/Framework/ReliabilityConfiguration.cs`** -> AI Confidence: **99.22%**
3741. **`src/tests/GC/Stress/Tests/allocationwithpins.cs`** -> AI Confidence: **99.22%**
3742. **`src/tools/ilasm/src/ILAssembler/BlobBuilderExtensions.cs`** -> AI Confidence: **99.22%**
3743. **`src/native/external/brotli/c/enc/static_dict.h`** -> AI Confidence: **99.21%**
3744. **`src/coreclr/inc/debugmacros.h`** -> AI Confidence: **99.21%**
3745. **`src/coreclr/inc/sstring.h`** -> AI Confidence: **99.21%**
3746. **`src/mono/mono/metadata/lock-tracer.h`** -> AI Confidence: **99.2%**
3747. **`src/mono/mono/mini/mini-windows-tls-callback.c`** -> AI Confidence: **99.2%**
3748. **`src/native/external/libunwind/src/coredump/_UCD_get_threadinfo_prstatus.c`** -> AI Confidence: **99.2%**
3749. **`src/native/external/libunwind/src/mi/Gdyn-remote.c`** -> AI Confidence: **99.2%**
3750. **`src/native/external/libunwind/src/nto/unw_nto_get_proc_name.c`** -> AI Confidence: **99.2%**
3751. **`src/native/external/zlib-ng/arch/arm/adler32_neon.c`** -> AI Confidence: **99.2%**
3752. **`src/native/external/zstd/lib/compress/zstd_opt.c`** -> AI Confidence: **99.2%**
3753. **`src/native/libs/System.Globalization.Native/pal_idna.c`** -> AI Confidence: **99.2%**
3754. **`src/coreclr/ildasm/dasm_formattype.cpp`** -> AI Confidence: **99.2%**
3755. **`src/coreclr/jit/async.cpp`** -> AI Confidence: **99.2%**
3756. **`src/coreclr/jit/copyprop.cpp`** -> AI Confidence: **99.2%**
3757. **`src/coreclr/jit/error.cpp`** -> AI Confidence: **99.2%**
3758. **`src/coreclr/jit/inline.cpp`** -> AI Confidence: **99.2%**
3759. **`src/coreclr/jit/promotion.cpp`** -> AI Confidence: **99.2%**
3760. **`src/coreclr/jit/regallocwasm.cpp`** -> AI Confidence: **99.2%**
3761. **`src/coreclr/jit/regset.cpp`** -> AI Confidence: **99.2%**
3762. **`src/coreclr/jit/ssarenamestate.cpp`** -> AI Confidence: **99.2%**
3763. **`src/coreclr/pal/src/synchobj/event.cpp`** -> AI Confidence: **99.2%**
3764. **`src/coreclr/pal/src/synchobj/semaphore.cpp`** -> AI Confidence: **99.2%**
3765. **`src/coreclr/pal/tests/palsuite/composite/object_management/event/nonshared/event.cpp`** -> AI Confidence: **99.2%**
3766. **`src/coreclr/pal/tests/palsuite/composite/object_management/event/shared/event.cpp`** -> AI Confidence: **99.2%**
3767. **`src/coreclr/pal/tests/palsuite/composite/object_management/semaphore/nonshared/semaphore.cpp`** -> AI Confidence: **99.2%**
3768. **`src/coreclr/pal/tests/palsuite/composite/object_management/semaphore/shared/semaphore.cpp`** -> AI Confidence: **99.2%**
3769. **`src/coreclr/tools/superpmi/superpmi-shared/mclist.cpp`** -> AI Confidence: **99.2%**
3770. **`src/coreclr/utilcode/format1.cpp`** -> AI Confidence: **99.2%**
3771. **`src/coreclr/utilcode/sha1.cpp`** -> AI Confidence: **99.2%**
3772. **`src/coreclr/utilcode/util_nodependencies.cpp`** -> AI Confidence: **99.2%**
3773. **`src/coreclr/vm/weakreferencenative.cpp`** -> AI Confidence: **99.2%**
3774. **`src/native/corehost/fxr/fx_resolver.cpp`** -> AI Confidence: **99.2%**
3775. **`src/native/corehost/hostpolicy/hostpolicy_init.cpp`** -> AI Confidence: **99.2%**
3776. **`src/tests/Interop/PInvoke/Primitives/Int/PInvokeIntNative.cpp`** -> AI Confidence: **99.2%**
3777. **`src/coreclr/System.Private.CoreLib/src/System/Reflection/Associates.cs`** -> AI Confidence: **99.2%**
3778. **`src/coreclr/System.Private.CoreLib/src/System/Runtime/InteropServices/IDispatchHelpers.cs`** -> AI Confidence: **99.2%**
3779. **`src/coreclr/nativeaot/System.Private.CoreLib/src/System/Diagnostics/StackTrace.NativeAot.cs`** -> AI Confidence: **99.2%**
3780. **`src/coreclr/tools/Common/Compiler/DependencyAnalysis/Relocation.cs`** -> AI Confidence: **99.2%**
3781. **`src/coreclr/tools/Common/TypeSystem/IL/Stubs/RuntimeHelpersIntrinsics.cs`** -> AI Confidence: **99.2%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/DSA/DSAKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/EC/ECKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/Common/tests/System/Security/Cryptography/AlgorithmImplementations/RSA/RSAKeyPemTests.cs` -> **100.0%** Exposure
- `src/libraries/System.Security.Cryptography/tests/ECPemExportTests.cs` -> **99.9997%** Exposure
- `src/libraries/System.Security.Cryptography/tests/X509Certificates/X509Certificate2PemTests.cs` -> **99.9977%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `139` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `122719` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/libraries/System.Net.Http.WinHttpHandler/src/System/Net/Http/WinHttpRequestState.cs` (CSHARP) -> Cumulative Risk: **784.34**
- **Archetype:** `file_cluster_4` (Distance: 12.6 IQR)
- **Magnitude:** 240.22 | **LOC:** 236 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Dispose` (Impact: 26.5), `ClearSendRequestState` (Impact: 9.2), `PinReceiveBuffer` (Impact: 7.3)

### 2. `src/libraries/System.Formats.Tar/ref/System.Formats.Tar.cs` (CSHARP) -> Cumulative Risk: **781.67**
- **Archetype:** `file_cluster_8` (Distance: 12.545 IQR)
- **Magnitude:** 290.2 | **LOC:** 157 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9849%)
- **Heaviest Functions:** `CreateFromDirectoryAsync` (Impact: 4.9), `CreateFromDirectoryAsync` (Impact: 4.9), `CreateFromDirectoryAsync` (Impact: 4.9)

### 3. `src/libraries/System.Runtime/ref/System.Runtime.cs` (CSHARP) -> Cumulative Risk: **780.17**
- **Archetype:** `file_cluster_0` (Distance: 14.098 IQR)
- **Magnitude:** 31974.78 | **LOC:** 17405 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 44.4%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (97.7725%)
- **Heaviest Functions:** `GetValues` (Impact: 16.5), `GetEnumValues` (Impact: 15.7), `EscapeString` (Impact: 14.2)

### 4. `src/libraries/Microsoft.Extensions.Caching.Abstractions/ref/Microsoft.Extensions.Caching.Abstractions.cs` (CSHARP) -> Cumulative Risk: **779.34**
- **Archetype:** `file_cluster_4` (Distance: 12.445 IQR)
- **Magnitude:** 280.42 | **LOC:** 219 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9986%)
- **Heaviest Functions:** `GetOrCreateAsync` (Impact: 5.0), `SetStringAsync` (Impact: 4.9), `SetAsync` (Impact: 4.5)

### 5. `src/libraries/System.Net.Security/ref/System.Net.Security.cs` (CSHARP) -> Cumulative Risk: **767.7**
- **Archetype:** `file_cluster_8` (Distance: 13.625 IQR)
- **Magnitude:** 1154.06 | **LOC:** 750 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.9998%)
- **Heaviest Functions:** `SslStream` (Impact: 7.4), `SslStream` (Impact: 6.8), `NegotiateClientCertificateAsync` (Impact: 6.8)

### 6. `src/libraries/System.Threading.Channels/ref/System.Threading.Channels.cs` (CSHARP) -> Cumulative Risk: **766.08**
- **Archetype:** `file_cluster_16` (Distance: 12.224 IQR)
- **Magnitude:** 140.42 | **LOC:** 83 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `ReadAsync` (Impact: 5.7), `ReadAllAsync` (Impact: 5.7), `WriteAsync` (Impact: 3.5)

### 7. `src/libraries/System.Net.Ping/ref/System.Net.Ping.cs` (CSHARP) -> Cumulative Risk: **765.75**
- **Archetype:** `file_cluster_8` (Distance: 12.464 IQR)
- **Magnitude:** 186.12 | **LOC:** 103 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9783%)
- **Heaviest Functions:** `PingCompletedEventArgs` (Impact: 7.0), `PingException` (Impact: 6.2), `SendPingAsync` (Impact: 4.9)

### 8. `src/libraries/System.Threading.Thread/ref/System.Threading.Thread.cs` (CSHARP) -> Cumulative Risk: **763.45**
- **Archetype:** `file_cluster_0` (Distance: 12.834 IQR)
- **Magnitude:** 570.18 | **LOC:** 261 | **CtrlFlow:** 81.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `GetObjectData` (Impact: 6.2), `VolatileRead` (Impact: 6.2), `VolatileRead` (Impact: 6.2)

### 9. `src/mono/browser/runtime/cancelable-promise.ts` (TYPESCRIPT) -> Cumulative Risk: **758.87**
- **Archetype:** `file_cluster_13` (Distance: 13.719 IQR)
- **Magnitude:** 25.97 | **LOC:** 188 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.2394%), Tech Debt (99.1392%)
- **Heaviest Functions:** `reject` (Impact: 13.3), `cancel` (Impact: 11.8), `complete_task` (Impact: 11.6)

### 10. `src/libraries/System.Private.CoreLib/src/System/IO/Strategies/OSFileStreamStrategy.cs` (CSHARP) -> Cumulative Risk: **758.24**
- **Archetype:** `file_cluster_4` (Distance: 12.032 IQR)
- **Magnitude:** 258.36 | **LOC:** 294 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9894%), Concurrency (99.9635%), Tech Debt (98.9463%)
- **Heaviest Functions:** `OSFileStreamStrategy` (Impact: 15.5), `SetLengthCore` (Impact: 11.8), `Read` (Impact: 11.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/tests/JIT/Directed/cmov/Bool_And_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.833 IQR)
- **Top Global Matches:** file_cluster_8: 12.833, file_cluster_7: 13.343, file_cluster_1: 13.355
- **Magnitude:** 60877.06 | **LOC:** 20789 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.1895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 124.2)
  * `Sub_Funclet_1` (Impact: 124.2)
  * `Sub_Funclet_2` (Impact: 124.2)
  * `Sub_Funclet_3` (Impact: 124.2)
  * `Sub_Funclet_4` (Impact: 124.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3227`, `orphaned_logic: 1`
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
- **Magnitude:** 60877.06 | **LOC:** 20788 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.1895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 124.2)
  * `Sub_Funclet_1` (Impact: 124.2)
  * `Sub_Funclet_2` (Impact: 124.2)
  * `Sub_Funclet_3` (Impact: 124.2)
  * `Sub_Funclet_4` (Impact: 124.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3227`, `orphaned_logic: 1`
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
- **Magnitude:** 60877.06 | **LOC:** 20788 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.1895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 124.2)
  * `Sub_Funclet_1` (Impact: 124.2)
  * `Sub_Funclet_2` (Impact: 124.2)
  * `Sub_Funclet_3` (Impact: 124.2)
  * `Sub_Funclet_4` (Impact: 124.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27650`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3227`, `orphaned_logic: 1`
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
- **Magnitude:** 53460.66 | **LOC:** 20866 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.1652%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 107.9)
  * `Sub_Funclet_1` (Impact: 107.9)
  * `Sub_Funclet_2` (Impact: 107.9)
  * `Sub_Funclet_3` (Impact: 107.9)
  * `Sub_Funclet_4` (Impact: 107.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27685`, `structural_boundaries: 473`, `args: 466`, `func_start: 930`, `class_start: 1`
* *Risk/State:* `state_mutation: 3230`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Xunit, System.Threading, System, TestLibrary
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/opt/virtualstubdispatch/bigvtbl/bigvtbl.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.377 IQR)
- **Top Global Matches:** file_cluster_8: 12.377, file_cluster_7: 12.839, file_cluster_1: 13.093
- **Magnitude:** 41768.56 | **LOC:** 15056 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.6856%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestEntryPoint` (Impact: 1275.0)
  * `f1` (Impact: 2.5)
  * `f2` (Impact: 2.5)
  * `f3` (Impact: 2.5)
  * `f4` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3025`, `structural_boundaries: 15029`, `args: 11997`, `func_start: 11998`, `class_start: 5`
* *Risk/State:* `duplicate_logic: 11996`, `orphaned_logic: 1`
* *Architecture:* `api: 12002`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libraries/System.Runtime.Intrinsics/ref/System.Runtime.Intrinsics.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.7%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.007 IQR)
- **Top Global Matches:** file_cluster_0: 13.007, file_cluster_8: 13.085, file_cluster_16: 13.098
- **Magnitude:** 32525.0 | **LOC:** 13502 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (4.7669%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Create` (Impact: 8.1)
  * `Create` (Impact: 5.8)
  * `Create` (Impact: 5.8)
  * `Create` (Impact: 4.2)
  * `Create` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 114`, `args: 10143`, `func_start: 10632`, `class_start: 105`
* *Risk/State:* `dead_code: 55`, `duplicate_logic: 10423`
* *Architecture:* `api: 11066`, `import: 1`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Diagnostics.CodeAnalysis
  * `Imported By (In-Degree: 722):` (Excluded from Brief to save tokens)

### `src/libraries/System.Runtime/ref/System.Runtime.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.73%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.098 IQR)
- **Top Global Matches:** file_cluster_0: 14.098, file_cluster_16: 14.222, file_cluster_8: 14.383
- **Magnitude:** 31974.78 | **LOC:** 17405 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (75.8317%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `GetValues` (Impact: 16.5)
  * `GetEnumValues` (Impact: 15.7)
  * `EscapeString` (Impact: 14.2)
  * `Unescape` (Impact: 14.2)
  * `Copy` (Impact: 13.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 1438`, `args: 7690`, `func_start: 8598`, `class_start: 808`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2894`, `duplicate_logic: 7228`, `orphaned_logic: 585`
* *Architecture:* `io: 1`, `api: 10227`, `concurrency: 726`
* *Defense:* `safety: 247`, `sync_locks: 4`, `immutability_locks: 421`, `cleanup: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.781
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 137):` (Excluded from Brief to save tokens)

### `src/tests/JIT/Directed/cmov/Int_Xor_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.135 IQR)
- **Top Global Matches:** file_cluster_8: 13.135, file_cluster_1: 13.142, file_cluster_7: 13.591
- **Magnitude:** 22584.82 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.1825%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1679`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_And_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.547 IQR)
- **Top Global Matches:** file_cluster_8: 12.547, file_cluster_1: 12.554, file_cluster_7: 13.024
- **Magnitude:** 22524.82 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.6212%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1619`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Int_Or_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.547 IQR)
- **Top Global Matches:** file_cluster_8: 12.547, file_cluster_1: 12.554, file_cluster_7: 13.024
- **Magnitude:** 22524.82 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.6212%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1619`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/cmov/Double_Xor_Op.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.061 IQR)
- **Top Global Matches:** file_cluster_8: 13.061, file_cluster_1: 13.068, file_cluster_7: 13.521
- **Magnitude:** 22424.82 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.6945%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1519`, `orphaned_logic: 1`
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
- **Magnitude:** 22406.82 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1501`, `orphaned_logic: 1`
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
- **Magnitude:** 22406.82 | **LOC:** 22170 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1501`, `orphaned_logic: 1`
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
- **Magnitude:** 22406.82 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1501`, `orphaned_logic: 1`
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
- **Magnitude:** 22364.82 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.1439%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1459`, `orphaned_logic: 1`
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
- **Magnitude:** 22364.82 | **LOC:** 22171 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.1439%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sub_Funclet_0` (Impact: 44.4)
  * `Sub_Funclet_1` (Impact: 44.4)
  * `Sub_Funclet_2` (Impact: 44.4)
  * `Sub_Funclet_3` (Impact: 44.4)
  * `Sub_Funclet_4` (Impact: 44.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9218`, `structural_boundaries: 469`, `args: 465`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1459`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/jit64/opt/cg/cgstress/CgStress1.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.672 IQR)
- **Top Global Matches:** file_cluster_8: 9.672, file_cluster_7: 10.4, file_cluster_1: 10.643
- **Magnitude:** 18943.8 | **LOC:** 28898 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.3244%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestEntryPoint` (Impact: 5.4)
  * `foo0` (Impact: 2.5)
    * *Intent:* #pragma warning disable xUnit1013
  * `foo1` (Impact: 2.5)
  * `foo2` (Impact: 2.5)
  * `foo3` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4102`, `args: 4098`, `func_start: 8196`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4100`, `orphaned_logic: 1`
* *Architecture:* `api: 4100`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xunit, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/nativeaot/Runtime/StackFrameIterator.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.431 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.424 IQR)
- **Top Global Matches:** file_cluster_8: 14.431, file_cluster_13: 14.56, file_cluster_11: 14.673
- **Magnitude:** 17892.89 | **LOC:** 2433 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (65.5301%), Tech Debt (26.2048%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 61`, `args: 176`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1006`, `dead_code: 3`, `planned_debt: 13`, `fragile_debt: 5`
* *Architecture:* `api: 8`, `import: 24`
* *Defense:* `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` StackFrameIterator.h, threadstore.h, thread.h, daccess.h, slist.h, gcenv.h, CommonMacros.inl, Pal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/emitarm64.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.837 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.515 IQR)
- **Top Global Matches:** file_cluster_8: 15.837, file_cluster_11: 16.063, file_cluster_13: 16.112
- **Magnitude:** 15669.16 | **LOC:** 18013 | **CtrlFlow:** 94.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (90.7082%), Tech Debt (37.2465%)
**Top Internal Functions/Classes:**
  * `emitter::emitIns_R_R_I` (Impact: 1393.3)
  * `emitter::emitInsTernary` (Impact: 1241.9)
  * `emitter::emitIns_R_R_R` (Impact: 930.6)
  * `emitter::emitIns_R_R_S_S` (Impact: 834.4)
  * `emitter::emitIns_R_S` (Impact: 824.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3734`, `structural_boundaries: 236`, `args: 155`, `func_start: 123`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6598`, `dead_code: 3`, `planned_debt: 10`, `orphaned_logic: 123`
* *Architecture:* `import: 21`
* *Defense:* `safety: 958`, `doc: 83`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` codegen.h, emit.h, instr.h, emitjmps.h, register.h, instrsarm64sve.h, jitpch.h, instrs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/emitxarch.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.299 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.303 IQR)
- **Top Global Matches:** file_cluster_8: 15.299, file_cluster_11: 15.515, file_cluster_13: 15.591
- **Magnitude:** 15165.58 | **LOC:** 21365 | **CtrlFlow:** 86.3% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (90.9557%), Tech Debt (69.4019%)
**Top Internal Functions/Classes:**
  * `emitter::emitIns_R_ARX` (Impact: 1440.1)
  * `emitter::emitIns_SIMD_R_R_S_R` (Impact: 1253.0)
  * `emitter::emitDispAddrMode` (Impact: 1082.8)
  * `emitter::emitIns_SIMD_R_R_R_R` (Impact: 906.6)
  * `emitter::emitRegName` (Impact: 902.3)
    * *Intent:* //------------------------------------------------------------------------ // emitInsLoadInd: Emits ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2836`, `structural_boundaries: 451`, `args: 251`, `func_start: 179`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 5453`, `dead_code: 9`, `planned_debt: 30`, `fragile_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 159`
* *Architecture:* `import: 13`
* *Defense:* `safety: 447`, `doc: 61`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` codegen.h, emit.h, instr.h, emitjmps.h, register.h, jitpch.h, instrs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mono/mono/mini/mini-llvm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.664 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.127 IQR)
- **Top Global Matches:** file_cluster_8: 15.664, file_cluster_13: 15.815, file_cluster_11: 15.838
- **Magnitude:** 14764.78 | **LOC:** 15450 | **CtrlFlow:** 90.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.1377%), Tech Debt (19.3561%)
**Top Internal Functions/Classes:**
  * `emit_throw` (Impact: 1084.6)
    * *Intent:* /* * Differences between the LLVM/non-LLVM throw corlib exception trampoline:
  * `sig_to_llvm_sig_full` (Impact: 426.7)
  * `get_callee_llvmonly` (Impact: 411.4)
  * `mono_llvm_create_vars` (Impact: 258.3)
  * `get_most_deep_clause` (Impact: 249.2)
    * *Intent:* #endif
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2959`, `structural_boundaries: 299`, `args: 28`, `func_start: 123`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 8125`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 22`, `orphaned_logic: 20`
* *Architecture:* `api: 2779`, `import: 29`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 72`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` mono-dl.h, mini-llvm.h, debug-internals.h, mini-ops.h, freebsd-dwarf.h, mini-runtime.h, BitWriter.h, mono-tls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mono/mono/mini/interp/transform.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.243 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.185 IQR)
- **Top Global Matches:** file_cluster_8: 15.243, file_cluster_13: 15.436, file_cluster_11: 15.454
- **Magnitude:** 13796.92 | **LOC:** 10168 | **CtrlFlow:** 92.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (17.3912%)
**Top Internal Functions/Classes:**
  * `push_type_explicit` (Impact: 1422.7)
  * `interp_handle_intrinsics` (Impact: 1391.1)
  * `interp_method_check_inlining` (Impact: 951.3)
  * `create_call_args` (Impact: 894.5)
  * `generate_code` (Impact: 699.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2899`, `structural_boundaries: 246`, `args: 7`, `func_start: 86`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 5673`, `dead_code: 6`, `planned_debt: 8`, `fragile_debt: 21`, `orphaned_logic: 10`
* *Architecture:* `io: 4`, `api: 1304`, `import: 28`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` exception.h, string.h, mintops.h, tabledefs.h, mini.h, class-internals.h, jiterpreter.h, mono-memory-model.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/Convert/value_numbering_checked_casts_of_constants_double.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.594 IQR)
- **Top Global Matches:** file_cluster_0: 14.594, file_cluster_8: 14.641, file_cluster_11: 15.087
- **Magnitude:** 12627.6 | **LOC:** 10024 | **CtrlFlow:** 85.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.4878%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestCastingDoubleToSByte` (Impact: 747.8)
  * `TestCastingDoubleToByte` (Impact: 747.8)
  * `TestCastingDoubleToUInt16` (Impact: 664.2)
  * `TestCastingDoubleToInt16` (Impact: 626.2)
  * `TestCastingDoubleToUInt32` (Impact: 585.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2050`, `structural_boundaries: 354`, `args: 696`, `func_start: 2072`, `class_start: 1`
* *Risk/State:* `state_mutation: 1011`, `duplicate_logic: 552`, `orphaned_logic: 118`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1699`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Runtime.CompilerServices, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/JIT/Directed/Convert/value_numbering_checked_casts_of_constants_float.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.615 IQR)
- **Top Global Matches:** file_cluster_0: 14.615, file_cluster_8: 14.665, file_cluster_11: 15.107
- **Magnitude:** 12584.24 | **LOC:** 9784 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.9847%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestCastingSingleToSByte` (Impact: 728.5)
  * `TestCastingSingleToByte` (Impact: 728.5)
  * `TestCastingSingleToUInt16` (Impact: 666.6)
  * `TestCastingSingleToInt16` (Impact: 635.6)
  * `TestCastingSingleToUInt32` (Impact: 624.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2018`, `structural_boundaries: 338`, `args: 680`, `func_start: 2024`, `class_start: 1`
* *Risk/State:* `state_mutation: 1011`, `duplicate_logic: 520`, `orphaned_logic: 133`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1683`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Runtime.CompilerServices, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/coreclr/jit/emitarm64sve.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.784 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.863 IQR)
- **Top Global Matches:** file_cluster_8: 15.784, file_cluster_11: 16.059, file_cluster_13: 16.114
- **Magnitude:** 11761.54 | **LOC:** 20043 | **CtrlFlow:** 98.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.2822%), Tech Debt (14.8263%)
**Top Internal Functions/Classes:**
  * `emitter::emitInsSve_R_R_R` (Impact: 1126.0)
    * *Intent:* /*****************************************************************************
  * `emitter::getInsSveExecutionCharacteristi` (Impact: 855.3)
  * `emitter::emitDispInsSveHelp` (Impact: 809.7)
  * `emitter::emitInsPairSanityCheck` (Impact: 633.0)
  * `emitter::emitInsSveSanityCheck` (Impact: 586.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4594`, `structural_boundaries: 73`, `args: 17`, `func_start: 42`
* *Risk/State:* `state_mutation: 5941`, `planned_debt: 10`, `duplicate_logic: 2`, `orphaned_logic: 40`
* *Architecture:* `import: 16`
* *Defense:* `safety: 1297`, `doc: 27`, `immutability_locks: 159`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` instr.h, codegen.h, instrsarm64sve.h, jitpch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/coreclr/System.Private.CoreLib/src/System/Enum.CoreCLR.cs` (CSHARP) | Magnitude: 50.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 97, func_start: 22, structural_boundaries: 18, explicit_casts: 16
- `src/libraries/Common/src/System/Security/Cryptography/RSAOpenSsl.cs` (CSHARP) | Magnitude: 366.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 495, state_mutation: 148, func_start: 118, structural_boundaries: 54
- `src/libraries/System.IO.FileSystem.Watcher/tests/FileSystemWatcher.File.Move.cs` (CSHARP) | Magnitude: 116.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 250, func_start: 55, structural_boundaries: 52, args: 51
- `src/libraries/System.Net.Sockets/tests/FunctionalTests/SendFile.cs` (CSHARP) | Magnitude: 258.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 338, structural_boundaries: 110, concurrency: 82, func_start: 79
- `src/libraries/System.Private.CoreLib/src/System/IndexOutOfRangeException.cs` (CSHARP) | Magnitude: 23.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, state_mutation: 7, structural_boundaries: 4, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/tests/JIT/Regression/JitBlue/Runtime_60957/Runtime_60957.cs` (CSHARP) | Magnitude: 53.64 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 116, doc: 44, func_start: 29, debug_prints: 19
- `src/tools/ilasm/src/ILAssembler/StringHelpers.cs` (CSHARP) | Magnitude: 0.12 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, branch: 43, func_start: 22, events: 16
- `src/libraries/System.IO.Compression/src/System/IO/Compression/DeflateManaged/InputBuffer.cs` (CSHARP) | Magnitude: 89.4 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 126, doc: 38, func_start: 26, state_mutation: 17
- `src/mono/mono/mini/test.cs` (CSHARP) | Magnitude: 765.46 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 396, indent_tabs: 307, branch: 139, events: 127
- `src/tests/JIT/Regression/JitBlue/Runtime_93342/Runtime_93342.cs` (CSHARP) | Magnitude: 98.76 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, events: 38, listeners: 38, branch: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/libraries/System.Reflection.Metadata/src/System/Reflection/Metadata/Ecma335/Encoding/ControlFlowBuilder.cs` (CSHARP) | Magnitude: 355.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 255, func_start: 61, state_mutation: 53, branch: 45
- `src/libraries/System.Runtime.Loader/tests/ApplyUpdateUtil.cs` (CSHARP) | Magnitude: 113.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 36, structural_boundaries: 27, func_start: 25
- `src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/DefaultInterpolatedStringHandler.cs` (CSHARP) | Magnitude: 130.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 47, doc: 42, branch: 23
- `src/coreclr/tools/Common/CommandLineHelpers.cs` (CSHARP) | Magnitude: 0.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 382, state_mutation: 122, branch: 92, structural_boundaries: 63
- `src/libraries/System.Composition.Hosting/tests/System/Composition/Hosting/Core/ExportDescriptorPromiseTests.cs` (CSHARP) | Magnitude: 101.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 206, func_start: 94, structural_boundaries: 77, test: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `.devcontainer/scripts/postCreateCommand.sh` (SHELL) | Magnitude: 0.83 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, reflection_metaprogramming: 3, branch: 2, indent_spaces: 2
- `src/mono/mono/tests/verifier/make_il_overflow_test.sh` (SHELL) | Magnitude: 82.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 45, branch: 24, safety_bypasses: 17, indent_tabs: 17
- `src/native/eventpipe/ep-rt-config.h` (CPP) | Magnitude: 46.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 41, state_mutation: 30, reflection_metaprogramming: 21, args: 12
- `src/mono/mono/arch/s390x/s390x-codegen.h` (CPP) | Magnitude: 608.48 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 682, reflection_metaprogramming: 681, indent_tabs: 651, state_mutation: 562
- `src/mono/mono/sgen/sgen-conf.h` (CPP) | Magnitude: 20.32 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 55, reflection_metaprogramming: 36, branch: 10, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/libraries/Microsoft.Extensions.Caching.Abstractions/src/MemoryCacheEntryOptions.cs` (CSHARP) | Magnitude: 44.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 73, doc: 26, state_mutation: 18, structural_boundaries: 13
- `src/libraries/System.Collections.Immutable/src/System/Collections/Frozen/ItemsFrozenSet.cs` (CSHARP) | Magnitude: 16.72 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, encapsulation: 12, structural_boundaries: 9, generics: 5
- `src/libraries/System.Private.Xml/tests/Readers/ReaderSettings/TCRSGeneric.cs` (CSHARP) | Magnitude: 14.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 21, func_start: 6, dead_code: 5, duplicate_logic: 5
- `src/native/libs/System.Security.Cryptography.Native.Apple/pal_symmetric.c` (C) | Magnitude: 87.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 27, api: 26, branch: 24
- `src/coreclr/tools/Common/Compiler/ObjectWriter/ElfObjectWriter.cs` (CSHARP) | Magnitude: 0.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 661, state_mutation: 258, func_start: 135, structural_boundaries: 113

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `eng/common/pipeline-logging-functions.ps1` (POWERSHELL) | Magnitude: 43.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 26, indent_spaces: 20, sec_high_risk_execution: 10, closures: 6
- `src/libraries/System.Text.RegularExpressions/src/System/Text/RegularExpressions/Regex.Match.cs` (CSHARP) | Magnitude: 60.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 531, indent_spaces: 67, func_start: 37, sec_high_risk_execution: 24
- `src/libraries/System.Private.CoreLib/src/System/Int32.cs` (CSHARP) | Magnitude: 779.68 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 930, state_mutation: 372, structural_boundaries: 229, branch: 207
- `src/libraries/System.Net.Http/src/System/Net/Http/Headers/HeaderStringValues.cs` (CSHARP) | Magnitude: 81.02 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 36, doc: 27, structural_boundaries: 23
- `src/libraries/System.Private.CoreLib/src/System/Diagnostics/Tracing/TraceLogging/Statics.cs` (CSHARP) | Magnitude: 448.92 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 450, state_mutation: 157, branch: 125, structural_boundaries: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/coreclr/tools/dotnet-pgo/SPGO/FlowSmoothing.cs` (CSHARP) | Magnitude: 0.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 310, state_mutation: 98, func_start: 59, branch: 58
- `src/libraries/System.Collections.Immutable/tests/EverythingEqual.cs` (CSHARP) | Magnitude: 13.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 8, func_start: 5, generics: 5
- `src/libraries/System.Collections.Immutable/tests/ImmutableSetTest.cs` (CSHARP) | Magnitude: 49.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 94, indent_spaces: 88, func_start: 36, test: 24
- `src/libraries/System.Text.Json/src/System/Text/Json/Serialization/Converters/Object/ObjectWithParameterizedConstructorConverter.Small.cs` (CSHARP) | Magnitude: 138.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, state_mutation: 71, branch: 29, structural_boundaries: 14
- `src/libraries/System.Linq.Expressions/src/System/Linq/Expressions/ExpressionVisitor.cs` (CSHARP) | Magnitude: 241.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 330, doc: 261, func_start: 80, structural_boundaries: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `eng/common/vmr-sync.sh` (SHELL) | Magnitude: 208.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 89, indent_spaces: 83, branch: 74, structural_boundaries: 35
- `src/mono/browser/runtime/queue.ts` (TYPESCRIPT) | Magnitude: 8.41 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 55, indent_spaces: 34, structural_boundaries: 8, args: 8
- `src/coreclr/vm/ebr.h` (CPP) | Magnitude: 105.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 94, indent_spaces: 43, structural_boundaries: 13, args: 11
- `src/libraries/System.Linq/tests/AnyTests.cs` (CSHARP) | Magnitude: 104.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 54, func_start: 28, args: 27
- `src/libraries/System.Linq/src/System/Linq/OfType.SpeedOpt.cs` (CSHARP) | Magnitude: 151.48 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 144, state_mutation: 39, branch: 32, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/libraries/System.ObjectModel/tests/ReadOnlyObservableCollection/ReadOnlyObservableCollection_EventsTests.cs` (CSHARP) | Magnitude: 304.96 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 417, func_start: 91, state_mutation: 86, doc: 84
- `src/libraries/System.ObjectModel/tests/ObservableCollection/ObservableCollection_MethodsTest.cs` (CSHARP) | Magnitude: 417.54 | Delta: **0.217 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 545, func_start: 146, state_mutation: 114, doc: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/mono/mono/tests/appdomain-thread-abort.cs` (CSHARP) | Magnitude: 202.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 190, func_start: 55, structural_boundaries: 43, branch: 37
- `src/libraries/System.Private.CoreLib/src/System/IO/UnmanagedMemoryStreamWrapper.cs` (CSHARP) | Magnitude: 123.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 125, func_start: 47, args: 29, api: 27
- `src/tests/JIT/Regression/CLR-x86-JIT/V1.2-M01/b08046cs/SyncGCHole.cs` (CSHARP) | Magnitude: 69.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, branch: 13, func_start: 12, structural_boundaries: 10
- `src/mono/sample/wasm/browser/wwwroot/main.js` (JAVASCRIPT) | Magnitude: 18.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 8, concurrency: 7, func_start: 5
- `src/coreclr/System.Private.CoreLib/src/System/Diagnostics/StackFrameHelper.cs` (CSHARP) | Magnitude: 73.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 17, func_start: 13, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/coreclr/tools/Common/Compiler/DependencyAnalysis/AssemblyStubNode.cs` (CSHARP) | Magnitude: 0.05 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 70, func_start: 37, structural_boundaries: 17, state_mutation: 16
- `src/libraries/System.Management/src/System/Management/ManagementEventWatcher.cs` (CSHARP) | Magnitude: 225.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 301, doc: 147, state_mutation: 93, branch: 47
- `src/libraries/Microsoft.Win32.SystemEvents/src/Microsoft/Win32/UserPreferenceCategories.cs` (CSHARP) | Magnitude: 30.4 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 72, indent_spaces: 17, state_mutation: 14, sec_high_risk_execution: 7
- `src/coreclr/vm/amd64/virtualcallstubcpu.hpp` (CPP) | Magnitude: 442.54 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 392, state_mutation: 282, structural_boundaries: 140, args: 89
- `src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/MetadataViewImplementationAttribute.cs` (CSHARP) | Magnitude: 6.44 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 25, indent_spaces: 9, api: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/libraries/System.ComponentModel.TypeConverter/src/System/ComponentModel/AddingNewEventArgs.cs` (CSHARP) | Magnitude: 10.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 17, indent_spaces: 11, api: 4, sec_high_risk_execution: 3
- `src/libraries/System.Private.CoreLib/src/System/Diagnostics/CodeAnalysis/RequiresAssemblyFilesAttribute.cs` (CSHARP) | Magnitude: 18.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 21, indent_spaces: 18, state_mutation: 8, api: 6
- `src/libraries/System.Security.Cryptography/src/System/Security/Cryptography/ECDsa.cs` (CSHARP) | Magnitude: 303.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 450, indent_spaces: 401, func_start: 130, state_mutation: 62
- `src/libraries/System.Collections.Immutable/src/System/Collections/Immutable/IImmutableArray.cs` (CSHARP) | Magnitude: 14.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, indent_spaces: 4, structural_boundaries: 2, class_start: 1
- `src/tests/Interop/PInvoke/Array/MarshalArray.h` (CPP) | Magnitude: 271.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 235, indent_spaces: 211, state_mutation: 155, structural_boundaries: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/mono/mono/utils/mono-context.c` (C) | Magnitude: 400.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 437, state_mutation: 335, indent_tabs: 290, macros: 70
- `src/native/external/libunwind/src/hppa/Gglobal.c` (C) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, api: 6, pointers: 5, state_mutation: 3
- `src/coreclr/jit/lir.cpp` (CPP) | Magnitude: 910.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 491, state_mutation: 444, pointers: 184, sec_high_risk_execution: 161
- `src/coreclr/nativeaot/Runtime/eventtrace_gcheap.cpp` (CPP) | Magnitude: 109.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 137, state_mutation: 69, pointers: 40, import: 15
- `src/native/external/brotli/c/enc/find_match_length.h` (CPP) | Magnitude: 0.09 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 78, indent_spaces: 35, branch: 16, pointers: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/libraries/System.ComponentModel.Composition/src/System/ComponentModel/Composition/CreationPolicy.cs` (CSHARP) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 18, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `src/native/external/libunwind/src/riscv/Gapply_reg_state.c` (C) | Magnitude: 0.01 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 5, pointers: 5, structural_boundaries: 4, ownership: 4
- `src/libraries/System.Private.CoreLib/src/System/Numerics/DivisionRounding.cs` (CSHARP) | Magnitude: 21.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 20, indent_spaces: 8, state_mutation: 5, structural_boundaries: 2
- `src/libraries/System.Private.Xml/tests/XmlReaderLib/TCErrorCondition.cs` (CSHARP) | Magnitude: 229.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 222, func_start: 183, duplicate_logic: 182, dead_code: 17
- `src/libraries/System.Private.Xml.Linq/src/System/Xml/Linq/LineInfoAnnotation.cs` (CSHARP) | Magnitude: 8.26 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 10, doc: 8, api: 4, dead_code: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/coreclr/jit/compiler.h` -> Churn: **95.83%** | Cog Load: 56.9917% | Debt: 54.6602%
- `src/native/managed/cdac/Microsoft.Diagnostics.DataContractReader.Legacy/SOSDacImpl.cs` -> Churn: **89.82%** | Cog Load: 32.0479% | Debt: 97.9547%
- `src/coreclr/jit/codegenwasm.cpp` -> Churn: **87.5%** | Cog Load: 95.5393% | Debt: 95.1074%
- `src/coreclr/jit/lower.cpp` -> Churn: **80.66%** | Cog Load: 93.8575% | Debt: 91.2033%
- `src/coreclr/jit/morph.cpp` -> Churn: **79.06%** | Cog Load: 78.5981% | Debt: 31.6103%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/coreclr/nativeaot/Runtime/StackFrameIterator.cpp` -> **Copilot** (100.0% isolated ownership) | Magnitude: 17892.89
- `src/coreclr/jit/emitarm64sve.cpp` -> **Yat Long Poon** (100.0% isolated ownership) | Magnitude: 11761.54
- `src/coreclr/jit/lsra.cpp` -> **Jakob Botsch Nielsen** (100.0% isolated ownership) | Magnitude: 10658.68
- `src/libraries/System.Security.Cryptography/ref/System.Security.Cryptography.cs` -> **Kevin Jones** (83.3% isolated ownership) | Magnitude: 8946.68
- `src/libraries/System.Private.CoreLib/src/System/Runtime/Intrinsics/Arm/AdvSimd.cs` -> **Jan Jones** (100.0% isolated ownership) | Magnitude: 8363.5

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
- `src/libraries/System.ComponentModel/ref/System.ComponentModel.cs` -> **Severity: 550.118** (Blast Radius: 5.607 * Doc Risk: 98.1127%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
