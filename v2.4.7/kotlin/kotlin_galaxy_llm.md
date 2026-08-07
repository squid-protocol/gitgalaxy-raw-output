# ARCHITECTURAL_BRIEF: kotlin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/kotlin` |
| **Timestamp** | `2026-08-07T05:06:10.456994+00:00` |
| **Scan Duration** | `148.9s` |
| **Git Branch** | `master` |
| **Git Commit** | `bcdc78880f23dd07f10607332e8a89a5e72d4e9a` |
| **Git Remote** | `https://github.com/JetBrains/kotlin` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 51718 malicious artifacts.

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
| Total Artifacts | 119907 |
| Analyzed Artifacts (Scanned) | 83578 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 36329 |
| Total LOC | 1928386 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.7% |
| Dominant Lang | KOTLIN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1111 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 825 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| KOTLIN | 45936 | 1614900 | 55.0% |
| PLAINTEXT | 31137 | 5 | 37.3% |
| JAVA | 2836 | 152335 | 3.4% |
| MAKEFILE | 748 | 5746 | 0.9% |
| CPP | 528 | 46080 | 0.6% |
| XML | 443 | 0 | 0.5% |
| GROOVY | 372 | 5294 | 0.4% |
| OBJECTIVE-C | 316 | 11620 | 0.4% |
| JAVASCRIPT | 303 | 5172 | 0.4% |
| SWIFT | 272 | 18826 | 0.3% |
| MARKDOWN | 165 | 0 | 0.2% |
| TYPESCRIPT | 159 | 7405 | 0.2% |
| JSON | 98 | 3502 | 0.1% |
| C | 80 | 6339 | 0.1% |
| PHP | 62 | 45685 | 0.1% |
| SHELL | 40 | 1383 | 0.0% |
| PROTO | 17 | 1234 | 0.0% |
| BATCH | 17 | 750 | 0.0% |
| RUBY | 13 | 179 | 0.0% |
| M4 | 7 | 9 | 0.0% |
| HTML | 6 | 61 | 0.0% |
| CSS | 5 | 231 | 0.0% |
| PYTHON | 5 | 1249 | 0.0% |
| DOCKERFILE | 5 | 158 | 0.0% |
| YAML | 4 | 187 | 0.0% |
| CSV | 2 | 22 | 0.0% |
| SCALA | 1 | 5 | 0.0% |
| YACC | 1 | 9 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.722`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 36471 | 43.6% |
| file_cluster_13 | 7928 | 9.5% |
| file_cluster_16 | 4827 | 5.8% |
| file_cluster_0 | 2358 | 2.8% |
| file_cluster_9 | 182 | 0.2% |
| file_cluster_2 | 129 | 0.2% |
| file_cluster_17 | 125 | 0.1% |
| file_cluster_4 | 98 | 0.1% |
| file_cluster_11 | 73 | 0.1% |
| file_cluster_6 | 39 | 0.0% |
| file_cluster_12 | 36 | 0.0% |
| file_cluster_7 | 9 | 0.0% |
| file_cluster_15 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 31301 | 37.5% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 36329*

**Composition by Extension & Reason:**
- `.kt`: 22532x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 124x Excluded: Neighborhood Micro-Mass Limit Exceeded, 8x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.txt`: 4420x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 726x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.java`: 1728x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 6 exceeds 500 chars), 3x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.info`: 603x Excluded (Unsupported Extension: '.info'), 438x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kts`: 692x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.out`: 560x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 222x Unsupported Format (.undeterminable), 139x Excluded (Unsupported Extension: '.instructions'), 82x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.log`: 478x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.args`: 441x Excluded (Unsupported Extension: '.args'), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.disabled`: 373x Unsupported Format (.disabled)
- `.new`: 191x Excluded (Unsupported Extension: '.new'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.new)
- `.pom`: 192x Unsupported Format (.pom)
- `.json`: 165x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 6753 LOC), 1x Excluded (Massive Static Asset Blob: 17658 LOC)
- `.values`: 137x Excluded (Unsupported Extension: '.values'), 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 138x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 122 LOC), 1x Excluded (Machine-Generated Source Code Signature: 174 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 15.5 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.6 | 0.7 | 0.0 |
| API Exposure | 0.0 | 19.1 | 1.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 69.1 | 80.0 | 100.0 |
| Instability Exposure | 0.0 | 23.1 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 18.4 | 11.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 21.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `settings.gradle` (Hits: 232)
- `libraries/tools/kotlin-maven-plugin-test/src/test/resources/maven-wrapper/mvnw` (Hits: 86)
- `libraries/scripting/jvm/src/kotlin/script/experimental/jvm/util/jvmClasspathUtil.kt` (Hits: 63)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Name.java** (`core/compiler.common/src/org/jetbrains/kotlin/name/Name.java`) — 1254 inbound connections
2. **File.kt** (`compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt`) — 1156 inbound connections
3. **FqName.kt** (`core/compiler.common/src/org/jetbrains/kotlin/name/FqName.kt`) — 814 inbound connections
4. **Project.kt** (`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/Project.kt`) — 808 inbound connections
5. **NotNull.java** (`analysis/symbol-light-classes/testData/additionalFiles/NotNull.java`) — 759 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **FirErrorsDefaultMessages.kt** (`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrorsDefaultMessages.kt`) — 934 outbound dependencies
2. **loadInterpreter.kt** (`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/loadInterpreter.kt`) — 328 outbound dependencies
3. **FirJvmErrorsDefaultMessages.kt** (`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/diagnostics/jvm/FirJvmErrorsDefaultMessages.kt`) — 124 outbound dependencies
4. **KaFirCompilerFacility.kt** (`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompilerFacility.kt`) — 110 outbound dependencies
5. **IrFileSerializer.kt** (`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrFileSerializer.kt`) — 107 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `toKaResolutionAttempt` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt`) -> Impact: **669.0** | LOC: 1082
- `transformQualifiedAccessExpression` (@ `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt`) -> Impact: **666.9** | LOC: 1114
- `build_address_map` (@ `kotlin-native/runtime/src/libbacktrace/c/dwarf.c`) -> Impact: **635.5** | LOC: 883
  * *Intent:* /* The name of the function. */
- `transformErrorReference` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt`) -> Impact: **624.1** | LOC: 1082
- `toKaSymbolResolutionAttempt` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt`) -> Impact: **596.1** | LOC: 1083
- `buildSmartCastStatement` (@ `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirDataFlowAnalyzer.kt`) -> Impact: **595.4** | LOC: 907
- `importFromBlock` (@ `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java`) -> Impact: **554.4** | LOC: 176
- `visitFunctionInScope` (@ `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt`) -> Impact: **537.2** | LOC: 1465
  * *Intent:* * 123, * $composer, * (0b110 and $dirty) or // 1st param has same state that our 1st param does * 0b11000 // 2nd parameter is "static" * ) * } * * Rec...
- `singleExpressionImpl` (@ `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java`) -> Impact: **510.2** | LOC: 724
- `doInline` (@ `compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MethodInliner.kt`) -> Impact: **507.3** | LOC: 740

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/proto` | 171 | 34462.81 | 7.53% | 45.79% |
| `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated` | 6 | 28823.09 | 13.77% | 33.33% |
| `kotlin-native/runtime/src/main/cpp` | 131 | 13568.1 | 46.81% | 69.04% |
| `compiler/psi/psi-api/src/org/jetbrains/kotlin/psi` | 195 | 10269.28 | 11.69% | 57.3% |
| `compiler/frontend/src/org/jetbrains/kotlin/resolve` | 89 | 9899.77 | 21.89% | 48.06% |
| `compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower` | 90 | 8526.7 | 56.88% | 41.31% |
| `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration` | 132 | 8269.68 | 74.26% | 73.84% |
| `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower` | 29 | 7745.6 | 47.1% | 39.12% |
| `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components` | 32 | 7452.14 | 25.7% | 52.79% |
| `kotlin-native/runtime/src/libbacktrace/c` | 13 | 6925.74 | 70.31% | 21.8% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/KaFe10SessionProvider.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10OriginalPsiProvider.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/modification/KaFe10SourceModificationService.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/scopes/KaFe10FileScope.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/scopes/KaFe10ScopeResolution.kt` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/KaFe10Session.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SignatureSubstitutor.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirExpressionInformationProvider.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/compilation/CodeFragmentContextDeclarationCache.kt` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` -> **0** Orphaned Functions | **1987** Duplicates
- `analysis/stubs/testData/builtins/stubs/kotlin.kotlin_builtins.decompiled.text.kt` -> **14** Orphaned Functions | **422** Duplicates
- `native/swift/swift-export-standalone-integration-tests/external/testData/generation/kotlinx-serialization-core/golden_result/KotlinSerialization/KotlinSerialization.swift` -> **41** Orphaned Functions | **289** Duplicates
- `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParserBaseListener.java` -> **324** Orphaned Functions | **0** Duplicates
- `compiler/testData/diagnostics/tests/overload/noConflictingOverloadsWithDeprecatedHidden/FunctionsInMemberScope.latestLV.kt` -> **0** Orphaned Functions | **268** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`kotlin-native/runtime/src/main/cpp/ObjCExport.mm`** -> AI Confidence: **99.48%**
2. **`kotlin-native/runtime/src/main/cpp/ObjCExportCollectionUtils.mm`** -> AI Confidence: **99.48%**
3. **`kotlin-native/runtime/src/main/cpp/ObjCExportErrors.mm`** -> AI Confidence: **99.48%**
4. **`kotlin-native/runtime/src/main/cpp/ObjCInterop.mm`** -> AI Confidence: **99.48%**
5. **`kotlin-native/runtime/src/main/cpp/ObjCInteropUtils.mm`** -> AI Confidence: **99.48%**
6. **`kotlin-native/runtime/src/main/cpp/objc_support/ObjectPtrTest.mm`** -> AI Confidence: **99.48%**
7. **`kotlin-native/runtime/src/main/cpp/swiftExportRuntime/SwiftExport.mm`** -> AI Confidence: **99.48%**
8. **`native/objcexport-header-generator/testData/headers/inlineClassWithNestedClass/!inlineClassWithNestedClass.h`** -> AI Confidence: **99.48%**
9. **`kotlin-native/runtime/src/main/cpp/Random.cpp`** -> AI Confidence: **99.48%**
10. **`kotlin-native/runtime/src/main/cpp/dtoa/dblparse.cpp`** -> AI Confidence: **99.48%**
11. **`kotlin-native/runtime/src/main/cpp/dtoa/fltparse.cpp`** -> AI Confidence: **99.48%**
12. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/temporaryVals/TemporaryVariablesEliminationTransformer.kt`** -> AI Confidence: **99.39%**
13. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirRenderer.kt`** -> AI Confidence: **99.39%**
14. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DeclarationsChecker.kt`** -> AI Confidence: **99.39%**
15. **`core/compiler.common/src/org/jetbrains/kotlin/stats/StatsCalculator.kt`** -> AI Confidence: **99.39%**
16. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/util/jvmClassLoaderUtil.kt`** -> AI Confidence: **99.39%**
17. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/common/OptimizationBasicInterpreter.java`** -> AI Confidence: **99.39%**
18. **`kotlin-native/runtime/src/libbacktrace/c/elf.c`** -> AI Confidence: **99.39%**
19. **`kotlin-native/runtime/src/objc/cpp/ObjCExportClasses.mm`** -> AI Confidence: **99.39%**
20. **`kotlin-native/tools/minidump-analyzer/src/main/cpp/main.cc`** -> AI Confidence: **99.39%**
21. **`compiler/fir/raw-fir/psi2fir/tests/org/jetbrains/kotlin/fir/builder/RawFirBuilderTotalKotlinTestCase.kt`** -> AI Confidence: **99.35%**
22. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/LogicSystem.kt`** -> AI Confidence: **99.34%**
23. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/ConstantEvaluator.kt`** -> AI Confidence: **99.34%**
24. **`kotlin-native/runtime/src/compiler_interface/cpp/CompilerObjCInterface.mm`** -> AI Confidence: **99.34%**
25. **`kotlin-native/runtime/src/main/cpp/ObjCExportCoroutines.mm`** -> AI Confidence: **99.34%**
26. **`kotlin-native/runtime/src/mm/cpp/AppStateTrackingUIKit.mm`** -> AI Confidence: **99.34%**
27. **`native/native.tests/testData/interop/objc/finalizerLoopGCRace/cinterop.m`** -> AI Confidence: **99.34%**
28. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/commonizeCurlInterop/libs/include/curl/system.h`** -> AI Confidence: **99.34%**
29. **`native/swift/swift-export-standalone-integration-tests/simple/testData/execution/referenceTypes/referenceTypes.swift`** -> AI Confidence: **99.34%**
30. **`compiler/backend/src/org/jetbrains/kotlin/codegen/state/JvmBackendConfig.kt`** -> AI Confidence: **99.32%**
31. **`native/swift/swift-export-standalone-integration-tests/simple/testData/execution/null_type/null_type.swift`** -> AI Confidence: **99.32%**
32. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ExpressionTypeProvider.kt`** -> AI Confidence: **99.31%**
33. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10Resolver.kt`** -> AI Confidence: **99.31%**
34. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolInformationProvider.kt`** -> AI Confidence: **99.31%**
35. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeProvider.kt`** -> AI Confidence: **99.31%**
36. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/base/fe10DescUtils.kt`** -> AI Confidence: **99.31%**
37. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/base/KaFe10PsiSymbolUtils.kt`** -> AI Confidence: **99.31%**
38. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/KaFe10JvmTypeMapperContext.kt`** -> AI Confidence: **99.31%**
39. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirDataFlowProvider.kt`** -> AI Confidence: **99.31%**
40. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirExpressionInformationProvider.kt`** -> AI Confidence: **99.31%**
41. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirExpressionTypeProvider.kt`** -> AI Confidence: **99.31%**
42. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt`** -> AI Confidence: **99.31%**
43. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSymbolRelationProvider.kt`** -> AI Confidence: **99.31%**
44. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/inlineStackDataUtils.kt`** -> AI Confidence: **99.31%**
45. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/evaluate/FirAnnotationValueConverter.kt`** -> AI Confidence: **99.31%**
46. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/evaluate/FirCompileTimeConstantEvaluator.kt`** -> AI Confidence: **99.31%**
47. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/psiUtils.kt`** -> AI Confidence: **99.31%**
48. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/ClassicKDocReferenceResolver.kt`** -> AI Confidence: **99.31%**
49. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/FirReferenceResolveHelper.kt`** -> AI Confidence: **99.31%**
50. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KDocReferenceResolver.kt`** -> AI Confidence: **99.31%**
51. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirBasePropertyAccessorSymbol.kt`** -> AI Confidence: **99.31%**
52. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirKotlinPropertySymbol.kt`** -> AI Confidence: **99.31%**
53. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirNamedClassSymbol.kt`** -> AI Confidence: **99.31%**
54. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirNamedFunctionSymbol.kt`** -> AI Confidence: **99.31%**
55. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSymbolProvider.kt`** -> AI Confidence: **99.31%**
56. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/references/KaBaseSimpleNameReference.kt`** -> AI Confidence: **99.31%**
57. **`analysis/analysis-api-standalone/analysis-api-fir-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/services/LLStandaloneFirElementByPsiElementChooser.kt`** -> AI Confidence: **99.31%**
58. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/modifiers/renderers/KaRendererOtherModifiersProvider.kt`** -> AI Confidence: **99.31%**
59. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/renderers/KaFlexibleTypeRenderer.kt`** -> AI Confidence: **99.31%**
60. **`analysis/analysis-test-framework/testFixtures/org/jetbrains/kotlin/analysis/test/framework/utils/commonTestUtils.kt`** -> AI Confidence: **99.31%**
61. **`analysis/decompiled/decompiler-native/src/org/jetbrains/kotlin/analysis/decompiler/konan/NearFileClassDataFinder.kt`** -> AI Confidence: **99.31%**
62. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/text/decompiledTextBuilder.kt`** -> AI Confidence: **99.31%**
63. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/TypeClsStubBuilder.kt`** -> AI Confidence: **99.31%**
64. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtReference.kt`** -> AI Confidence: **99.31%**
65. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/ReadWriteAccessChecker.kt`** -> AI Confidence: **99.31%**
66. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/referenceUtils.kt`** -> AI Confidence: **99.31%**
67. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/LightClassUtil.kt`** -> AI Confidence: **99.31%**
68. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/elements/KotlinLightMethodUtils.kt`** -> AI Confidence: **99.31%**
69. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/elements/KtLightAnnotationsValues.kt`** -> AI Confidence: **99.31%**
70. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/lightClassUtils.kt`** -> AI Confidence: **99.31%**
71. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/LLFirDiagnosticReporter.kt`** -> AI Confidence: **99.31%**
72. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/element/builder/FirElementBuilder.kt`** -> AI Confidence: **99.31%**
73. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/builder/LLFirLockProvider.kt`** -> AI Confidence: **99.31%**
74. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/FileStructureElement.kt`** -> AI Confidence: **99.31%**
75. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/FirElementsRecorder.kt`** -> AI Confidence: **99.31%**
76. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/LLElementMapper.kt`** -> AI Confidence: **99.31%**
77. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/inBlockModification.kt`** -> AI Confidence: **99.31%**
78. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLSubstitutionScopeKeyFactory.kt`** -> AI Confidence: **99.31%**
79. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirBodyLazyResolver.kt`** -> AI Confidence: **99.31%**
80. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/LLContainingClassCalculator.kt`** -> AI Confidence: **99.31%**
81. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/containingFileUtils.kt`** -> AI Confidence: **99.31%**
82. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/declarationUtils.kt`** -> AI Confidence: **99.31%**
83. **`build-common/src/org/jetbrains/kotlin/compilerRunner/argumentsToStrings.kt`** -> AI Confidence: **99.31%**
84. **`build-common/src/org/jetbrains/kotlin/incremental/ChangesCollector.kt`** -> AI Confidence: **99.31%**
85. **`build-common/src/org/jetbrains/kotlin/incremental/LookupStorage.kt`** -> AI Confidence: **99.31%**
86. **`compiler/android-tests/tests/org/jetbrains/kotlin/android/tests/AndroidTestGenerator.kt`** -> AI Confidence: **99.31%**
87. **`compiler/android-tests/tests/org/jetbrains/kotlin/android/tests/CodegenTestsOnAndroidRunner.kt`** -> AI Confidence: **99.31%**
88. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/CommonCompilerArguments.kt`** -> AI Confidence: **99.31%**
89. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/NativeCompilerArguments.kt`** -> AI Confidence: **99.31%**
90. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/WasmCompilerArguments.kt`** -> AI Confidence: **99.31%**
91. **`compiler/backend.common.jvm/src/org/jetbrains/kotlin/types/AbstractTypeMapper.kt`** -> AI Confidence: **99.31%**
92. **`compiler/backend/src/org/jetbrains/kotlin/codegen/StringConcatGenerator.kt`** -> AI Confidence: **99.31%**
93. **`compiler/backend/src/org/jetbrains/kotlin/codegen/codegenUtil.kt`** -> AI Confidence: **99.31%**
94. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/CoroutineTransformerMethodVisitor.kt`** -> AI Confidence: **99.31%**
95. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/SpilledVariableFieldTypesAnalysis.kt`** -> AI Confidence: **99.31%**
96. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/TailCallOptimization.kt`** -> AI Confidence: **99.31%**
97. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/processUninitializedStores.kt`** -> AI Confidence: **99.31%**
98. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/LocalVarRemapper.kt`** -> AI Confidence: **99.31%**
99. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MethodInliner.kt`** -> AI Confidence: **99.31%**
100. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/RegeneratedLambdaFieldRemapper.kt`** -> AI Confidence: **99.31%**
101. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/ReifiedTypeInliner.kt`** -> AI Confidence: **99.31%**
102. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/defaultMethodUtil.kt`** -> AI Confidence: **99.31%**
103. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/inlineCodegenUtils.kt`** -> AI Confidence: **99.31%**
104. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/typeOf.kt`** -> AI Confidence: **99.31%**
105. **`compiler/backend/src/org/jetbrains/kotlin/codegen/intrinsics/TypeIntrinsics.kt`** -> AI Confidence: **99.31%**
106. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/CapturedVarsOptimizationMethodTransformer.kt`** -> AI Confidence: **99.31%**
107. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/ConstantConditionEliminationMethodTransformer.kt`** -> AI Confidence: **99.31%**
108. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/DeadCodeEliminationMethodTransformer.kt`** -> AI Confidence: **99.31%**
109. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/RedundantCheckCastElimination.kt`** -> AI Confidence: **99.31%**
110. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/RedundantNopsCleanupMethodTransformer.kt`** -> AI Confidence: **99.31%**
111. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/BoxingInterpreter.kt`** -> AI Confidence: **99.31%**
112. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/PopBackwardPropagationTransformer.kt`** -> AI Confidence: **99.31%**
113. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/RedundantBoxingMethodTransformer.kt`** -> AI Confidence: **99.31%**
114. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/StackPeepholeOptimizationsTransformer.kt`** -> AI Confidence: **99.31%**
115. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/common/FastAnalyzer.kt`** -> AI Confidence: **99.31%**
116. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/common/Util.kt`** -> AI Confidence: **99.31%**
117. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/FixStackMethodTransformer.kt`** -> AI Confidence: **99.31%**
118. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/nullCheck/NullabilityInterpreter.kt`** -> AI Confidence: **99.31%**
119. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/nullCheck/RedundantNullCheckMethodTransformer.kt`** -> AI Confidence: **99.31%**
120. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/temporaryVals/TemporaryVals.kt`** -> AI Confidence: **99.31%**
121. **`compiler/backend/src/org/jetbrains/kotlin/codegen/serialization/JvmSerializerExtension.kt`** -> AI Confidence: **99.31%**
122. **`compiler/backend/src/org/jetbrains/kotlin/codegen/state/KotlinTypeMapper.kt`** -> AI Confidence: **99.31%**
123. **`compiler/backend/src/org/jetbrains/kotlin/codegen/state/inlineClassManglingUtils.kt`** -> AI Confidence: **99.31%**
124. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/BaseArgumentTest.kt`** -> AI Confidence: **99.31%**
125. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/internal/wrappers/KotlinWrapperPre2_4_0.kt`** -> AI Confidence: **99.31%**
126. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/arguments/CompilerArgumentValueAdapter.kt`** -> AI Confidence: **99.31%**
127. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/daemonAdapters.kt`** -> AI Confidence: **99.31%**
128. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/BtaApiGenerator.kt`** -> AI Confidence: **99.31%**
129. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/BtaImplGenerator.kt`** -> AI Confidence: **99.31%**
130. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/Main.kt`** -> AI Confidence: **99.31%**
131. **`compiler/cli/cli-arguments-generator/src/org/jetbrains/kotlin/cli/arguments/generator/Main.kt`** -> AI Confidence: **99.31%**
132. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/jarfs/FastJarHandler.kt`** -> AI Confidence: **99.31%**
133. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/index/JvmDependenciesIndexImpl.kt`** -> AI Confidence: **99.31%**
134. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/index/SingleJavaFileRootsIndex.kt`** -> AI Confidence: **99.31%**
135. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/modules/CliJavaModuleFinder.kt`** -> AI Confidence: **99.31%**
136. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/Helpers.kt`** -> AI Confidence: **99.31%**
137. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/wasm/KotlinIr2WasmIrCompilerIC.kt`** -> AI Confidence: **99.31%**
138. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/CLICompiler.kt`** -> AI Confidence: **99.31%**
139. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/klibArguments.kt`** -> AI Confidence: **99.31%**
140. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/messages/PlainTextMessageRenderer.kt`** -> AI Confidence: **99.31%**
141. **`compiler/cli/src/org/jetbrains/kotlin/cli/jvm/compiler/IncrementalCompilationContextUtils.kt`** -> AI Confidence: **99.31%**
142. **`compiler/container/src/org/jetbrains/kotlin/container/Storage.kt`** -> AI Confidence: **99.31%**
143. **`compiler/daemon/daemon-client/src/main/kotlin/KotlinCompilerClient.kt`** -> AI Confidence: **99.31%**
144. **`compiler/daemon/daemon-common/src/org/jetbrains/kotlin/daemon/common/DaemonParams.kt`** -> AI Confidence: **99.31%**
145. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/LazyClasspathWatcher.kt`** -> AI Confidence: **99.31%**
146. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/report/getICReporter.kt`** -> AI Confidence: **99.31%**
147. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/Main.kt`** -> AI Confidence: **99.31%**
148. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExportDeclarationChecker.kt`** -> AI Confidence: **99.31%**
149. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNameChecker.kt`** -> AI Confidence: **99.31%**
150. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNameClashClassMembersChecker.kt`** -> AI Confidence: **99.31%**
151. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsDynamicCallChecker.kt`** -> AI Confidence: **99.31%**
152. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmExposeBoxedChecker.kt`** -> AI Confidence: **99.31%**
153. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmRecordChecker.kt`** -> AI Confidence: **99.31%**
154. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmStaticChecker.kt`** -> AI Confidence: **99.31%**
155. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmExternalInheritanceChecker.kt`** -> AI Confidence: **99.31%**
156. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmJsInteropTypesChecker.kt`** -> AI Confidence: **99.31%**
157. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirWebCommonExternalChecker.kt`** -> AI Confidence: **99.31%**
158. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/FirCallsEffectAnalyzer.kt`** -> AI Confidence: **99.31%**
159. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/VariableInitializationCheckProcessor.kt`** -> AI Confidence: **99.31%**
160. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/ConeTypeCompatibilityChecker.kt`** -> AI Confidence: **99.31%**
161. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirCastDiagnosticsHelpers.kt`** -> AI Confidence: **99.31%**
162. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirConflictsHelpers.kt`** -> AI Confidence: **99.31%**
163. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirHelpers.kt`** -> AI Confidence: **99.31%**
164. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirInconsistentTypeParameterHelpers.kt`** -> AI Confidence: **99.31%**
165. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirUpperBoundViolatedHelpers.kt`** -> AI Confidence: **99.31%**
166. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirActualTypeAliasChecker.kt`** -> AI Confidence: **99.31%**
167. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnnotationChecker.kt`** -> AI Confidence: **99.31%**
168. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnnotationClassDeclarationChecker.kt`** -> AI Confidence: **99.31%**
169. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirClassVarianceChecker.kt`** -> AI Confidence: **99.31%**
170. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirContextParametersDeclarationChecker.kt`** -> AI Confidence: **99.31%**
171. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDestructuringDeclarationChecker.kt`** -> AI Confidence: **99.31%**
172. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExpectActualDeclarationChecker.kt`** -> AI Confidence: **99.31%**
173. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExpectConsistencyChecker.kt`** -> AI Confidence: **99.31%**
174. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExposedVisibilityDeclarationChecker.kt`** -> AI Confidence: **99.31%**
175. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExtensionShadowedByMemberChecker.kt`** -> AI Confidence: **99.31%**
176. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFunInterfaceDeclarationChecker.kt`** -> AI Confidence: **99.31%**
177. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFunctionParameterChecker.kt`** -> AI Confidence: **99.31%**
178. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirImplementationMismatchChecker.kt`** -> AI Confidence: **99.31%**
179. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInapplicableLateinitChecker.kt`** -> AI Confidence: **99.31%**
180. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirKClassWithIncorrectTypeArgumentChecker.kt`** -> AI Confidence: **99.31%**
181. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMemberFunctionsChecker.kt`** -> AI Confidence: **99.31%**
182. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirModifierChecker.kt`** -> AI Confidence: **99.31%**
183. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNestedClassChecker.kt`** -> AI Confidence: **99.31%**
184. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptInMarkedDeclarationChecker.kt`** -> AI Confidence: **99.31%**
185. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOverrideChecker.kt`** -> AI Confidence: **99.31%**
186. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPropertyAccessorsTypesChecker.kt`** -> AI Confidence: **99.31%**
187. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPropertyFieldTypeChecker.kt`** -> AI Confidence: **99.31%**
188. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirReservedUnderscoreDeclarationChecker.kt`** -> AI Confidence: **99.31%**
189. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirSealedSupertypeChecker.kt`** -> AI Confidence: **99.31%**
190. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirSupertypesChecker.kt`** -> AI Confidence: **99.31%**
191. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirThrowableSubclassChecker.kt`** -> AI Confidence: **99.31%**
192. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTopLevelPropertiesChecker.kt`** -> AI Confidence: **99.31%**
193. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTypeParameterBoundsChecker.kt`** -> AI Confidence: **99.31%**
194. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirUnusedCheckerBase.kt`** -> AI Confidence: **99.31%**
195. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirValueClassDeclarationChecker.kt`** -> AI Confidence: **99.31%**
196. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/crv/FirUnusedReturnValueChecker.kt`** -> AI Confidence: **99.31%**
197. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/declarationUtils.kt`** -> AI Confidence: **99.31%**
198. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirAnnotationExpressionChecker.kt`** -> AI Confidence: **99.31%**
199. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCastOperatorsChecker.kt`** -> AI Confidence: **99.31%**
200. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirClassLiteralChecker.kt`** -> AI Confidence: **99.31%**
201. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDeprecationChecker.kt`** -> AI Confidence: **99.31%**
202. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirEqualityCompatibilityChecker.kt`** -> AI Confidence: **99.31%**
203. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirExhaustiveWhenChecker.kt`** -> AI Confidence: **99.31%**
204. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirExpressionWithErrorTypeChecker.kt`** -> AI Confidence: **99.31%**
205. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirFunctionReturnTypeMismatchChecker.kt`** -> AI Confidence: **99.31%**
206. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineBodyResolvableExpressionChecker.kt`** -> AI Confidence: **99.31%**
207. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirMissingDependencyClassChecker.kt`** -> AI Confidence: **99.31%**
208. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirNamedVarargChecker.kt`** -> AI Confidence: **99.31%**
209. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptInUsageBaseChecker.kt`** -> AI Confidence: **99.31%**
210. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirReassignmentAndInvisibleSetterChecker.kt`** -> AI Confidence: **99.31%**
211. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirReifiedChecker.kt`** -> AI Confidence: **99.31%**
212. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirReturnSyntaxAndLabelChecker.kt`** -> AI Confidence: **99.31%**
213. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSuspendCallChecker.kt`** -> AI Confidence: **99.31%**
214. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTypeArgumentsNotAllowedExpressionChecker.kt`** -> AI Confidence: **99.31%**
215. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirWhenConditionChecker.kt`** -> AI Confidence: **99.31%**
216. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantVisibilityModifierSyntaxChecker.kt`** -> AI Confidence: **99.31%**
217. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/UnreachableCodeChecker.kt`** -> AI Confidence: **99.31%**
218. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/UnusedVariableAssignmentChecker.kt`** -> AI Confidence: **99.31%**
219. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirExplicitApiDeclarationChecker.kt`** -> AI Confidence: **99.31%**
220. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirUnderscoredTypeArgumentSyntaxChecker.kt`** -> AI Confidence: **99.31%**
221. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/components/ErrorNodeDiagnosticCollectorComponent.kt`** -> AI Confidence: **99.31%**
222. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/coneDiagnosticToFirDiagnostic.kt`** -> AI Confidence: **99.31%**
223. **`compiler/fir/cones/src/org/jetbrains/kotlin/fir/renderer/ConeTypeRenderer.kt`** -> AI Confidence: **99.31%**
224. **`compiler/fir/cones/src/org/jetbrains/kotlin/fir/types/ConeAttributes.kt`** -> AI Confidence: **99.31%**
225. **`compiler/fir/diagnostic-renderers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirAdaptiveTypeRenderingKey.kt`** -> AI Confidence: **99.31%**
226. **`compiler/fir/diagnostic-renderers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirDiagnosticRenderers.kt`** -> AI Confidence: **99.31%**
227. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/backend/Fir2IrFakeOverrideStrategy.kt`** -> AI Confidence: **99.31%**
228. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirConstDeserializer.kt`** -> AI Confidence: **99.31%**
229. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/FirJavaFacade.kt`** -> AI Confidence: **99.31%**
230. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JavaTypeConversion.kt`** -> AI Confidence: **99.31%**
231. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/JvmBinaryAnnotationDeserializer.kt`** -> AI Confidence: **99.31%**
232. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/enhancement/javaTypeUtils.kt`** -> AI Confidence: **99.31%**
233. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/resolve/calls/jvm/JvmPlatformOverloadsConflictResolver.kt`** -> AI Confidence: **99.31%**
234. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirElementSerializer.kt`** -> AI Confidence: **99.31%**
235. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmSerializerExtension.kt`** -> AI Confidence: **99.31%**
236. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrConversionScope.kt`** -> AI Confidence: **99.31%**
237. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrIrGeneratedDeclarationsRegistrar.kt`** -> AI Confidence: **99.31%**
238. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrTypeConverter.kt`** -> AI Confidence: **99.31%**
239. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrVisitor.kt`** -> AI Confidence: **99.31%**
240. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/AdapterGenerator.kt`** -> AI Confidence: **99.31%**
241. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/CallAndReferenceGenerator.kt`** -> AI Confidence: **99.31%**
242. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/ClassMemberGenerator.kt`** -> AI Confidence: **99.31%**
243. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/OperatorExpressionGenerator.kt`** -> AI Confidence: **99.31%**
244. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/OffsetUtils.kt`** -> AI Confidence: **99.31%**
245. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/OriginUtils.kt`** -> AI Confidence: **99.31%**
246. **`compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/moduleData.kt`** -> AI Confidence: **99.31%**
247. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/CopyUtils.kt`** -> AI Confidence: **99.31%**
248. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/FirVisibilityChecker.kt`** -> AI Confidence: **99.31%**
249. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/ValueClassesUtils.kt`** -> AI Confidence: **99.31%**
250. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/expressions/FirConstChecks.kt`** -> AI Confidence: **99.31%**
251. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/expressions/FirExpressionEvaluator.kt`** -> AI Confidence: **99.31%**
252. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/calls/Synthetics.kt`** -> AI Confidence: **99.31%**
253. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/FirOverrideService.kt`** -> AI Confidence: **99.31%**
254. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirAbstractImportingScope.kt`** -> AI Confidence: **99.31%**
255. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirClassSubstitutionScope.kt`** -> AI Confidence: **99.31%**
256. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirStandardOverrideChecker.kt`** -> AI Confidence: **99.31%**
257. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/TypeUtils.kt`** -> AI Confidence: **99.31%**
258. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/AbstractLightTreeRawFirBuilder.kt`** -> AI Confidence: **99.31%**
259. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/ConverterUtil.kt`** -> AI Confidence: **99.31%**
260. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirDeclarationBuilder.kt`** -> AI Confidence: **99.31%**
261. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirExpressionBuilder.kt`** -> AI Confidence: **99.31%**
262. **`compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiRawFirBuilder.kt`** -> AI Confidence: **99.31%**
263. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/AbstractRawFirBuilder.kt`** -> AI Confidence: **99.31%**
264. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/ConversionUtils.kt`** -> AI Confidence: **99.31%**
265. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirDoubleColonExpressionResolver.kt`** -> AI Confidence: **99.31%**
266. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/QualifiedNameResolution.kt`** -> AI Confidence: **99.31%**
267. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/CandidateFactory.kt`** -> AI Confidence: **99.31%**
268. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/CheckArguments.kt`** -> AI Confidence: **99.31%**
269. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/CheckCallableReferenceExpectedType.kt`** -> AI Confidence: **99.31%**
270. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/CollectTypeVariableUsagesInfo.kt`** -> AI Confidence: **99.31%**
271. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/CreateFreshTypeVariableSubstitutorStage.kt`** -> AI Confidence: **99.31%**
272. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/FirArgumentsToParametersMapper.kt`** -> AI Confidence: **99.31%**
273. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/FirTowerResolveTask.kt`** -> AI Confidence: **99.31%**
274. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/TowerLevels.kt`** -> AI Confidence: **99.31%**
275. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirDataFlowAnalyzer.kt`** -> AI Confidence: **99.31%**
276. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/cfg/ControlFlowGraphBuilder.kt`** -> AI Confidence: **99.31%**
277. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/CompletionModeCalculator.kt`** -> AI Confidence: **99.31%**
278. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/ConstraintSystemCompleter.kt`** -> AI Confidence: **99.31%**
279. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/InferenceUtils.kt`** -> AI Confidence: **99.31%**
280. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/optimization/FirReachabilityAnalyzer.kt`** -> AI Confidence: **99.31%**
281. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirTypeResolverImpl.kt`** -> AI Confidence: **99.31%**
282. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirStatusResolver.kt`** -> AI Confidence: **99.31%**
283. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirSupertypesResolution.kt`** -> AI Confidence: **99.31%**
284. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirWhenExhaustivenessComputer.kt`** -> AI Confidence: **99.31%**
285. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/LambdaArgumentEffectsTransformer.kt`** -> AI Confidence: **99.31%**
286. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/TransformUtils.kt`** -> AI Confidence: **99.31%**
287. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirDeclarationsResolveTransformer.kt`** -> AI Confidence: **99.31%**
288. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt`** -> AI Confidence: **99.31%**
289. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/bareTypes.kt`** -> AI Confidence: **99.31%**
290. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/setUnnamedContextParameterNames.kt`** -> AI Confidence: **99.31%**
291. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/contracts/ConeEffectExtractor.kt`** -> AI Confidence: **99.31%**
292. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/mpp/annotationCompareUtils.kt`** -> AI Confidence: **99.31%**
293. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/PrivateToThisUtils.kt`** -> AI Confidence: **99.31%**
294. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/declarations/FirMustUseReturnValueStatusComponent.kt`** -> AI Confidence: **99.31%**
295. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/mainFunctionDetection.kt`** -> AI Confidence: **99.31%**
296. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/DeclarationUtils.kt`** -> AI Confidence: **99.31%**
297. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/VariableStorage.kt`** -> AI Confidence: **99.31%**
298. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/cfg/CFGNodeRenderer.kt`** -> AI Confidence: **99.31%**
299. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/cfg/ControlFlowGraphRenderer.kt`** -> AI Confidence: **99.31%**
300. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/contracts.kt`** -> AI Confidence: **99.31%**
301. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirDeclarationRenderer.kt`** -> AI Confidence: **99.31%**
302. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/ConeIntegerLiteralTypeImpl.kt`** -> AI Confidence: **99.31%**
303. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/FirTree.kt`** -> AI Confidence: **99.31%**
304. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/printer/ImplementationPrinter.kt`** -> AI Confidence: **99.31%**
305. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/LightTreePositioningStrategies.kt`** -> AI Confidence: **99.31%**
306. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PositioningStrategies.kt`** -> AI Confidence: **99.31%**
307. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/BinaryClassSignatureParser.kt`** -> AI Confidence: **99.31%**
308. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/BinaryJavaClass.kt`** -> AI Confidence: **99.31%**
309. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/Methods.kt`** -> AI Confidence: **99.31%**
310. **`compiler/frontend.common/src/org/jetbrains/kotlin/diagnostics/KtDiagnosticFactory.kt`** -> AI Confidence: **99.31%**
311. **`compiler/frontend.common/src/org/jetbrains/kotlin/diagnostics/impl/PendingDiagnosticsReporterImpl.kt`** -> AI Confidence: **99.31%**
312. **`compiler/frontend.common/src/org/jetbrains/kotlin/util/AnalysisExceptions.kt`** -> AI Confidence: **99.31%**
313. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ApiVersionIsAtLeastArgumentsChecker.kt`** -> AI Confidence: **99.31%**
314. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ExternalFunChecker.kt`** -> AI Confidence: **99.31%**
315. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/FileClassAnnotationsChecker.kt`** -> AI Confidence: **99.31%**
316. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaNullabilityChecker.kt`** -> AI Confidence: **99.31%**
317. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmAnnotationsTargetNonExistentAccessorChecker.kt`** -> AI Confidence: **99.31%**
318. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmArrayVariableInLoopAssignmentChecker.kt`** -> AI Confidence: **99.31%**
319. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmFieldApplicabilityChecker.kt`** -> AI Confidence: **99.31%**
320. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmPropertyVsFieldAmbiguityCallChecker.kt`** -> AI Confidence: **99.31%**
321. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmRecordApplicabilityChecker.kt`** -> AI Confidence: **99.31%**
322. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmSyntheticAssignmentChecker.kt`** -> AI Confidence: **99.31%**
323. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SuspensionPointInsideMutexLockChecker.kt`** -> AI Confidence: **99.31%**
324. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/declarationCheckers.kt`** -> AI Confidence: **99.31%**
325. **`compiler/frontend.java/src/org/jetbrains/kotlin/synthetic/JavaSyntheticPropertiesScope.kt`** -> AI Confidence: **99.31%**
326. **`compiler/frontend.java/src/org/jetbrains/kotlin/synthetic/SamAdapterFunctionsScope.kt`** -> AI Confidence: **99.31%**
327. **`compiler/frontend.java/src/org/jetbrains/kotlin/synthetic/syntheticExtensionsUtils.kt`** -> AI Confidence: **99.31%**
328. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/ConstructorConsistencyChecker.kt`** -> AI Confidence: **99.31%**
329. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/ControlFlowInformationProviderImpl.kt`** -> AI Confidence: **99.31%**
330. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/ControlFlowProcessor.kt`** -> AI Confidence: **99.31%**
331. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/PseudocodeTraverser.kt`** -> AI Confidence: **99.31%**
332. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/PseudocodeImpl.kt`** -> AI Confidence: **99.31%**
333. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/pseudocodeUtils.kt`** -> AI Confidence: **99.31%**
334. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/variable/PseudocodeVariablesData.kt`** -> AI Confidence: **99.31%**
335. **`compiler/frontend/src/org/jetbrains/kotlin/cfg/WhenChecker.kt`** -> AI Confidence: **99.31%**
336. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/diagnostics/TextDiagnostic.kt`** -> AI Confidence: **99.31%**
337. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/utils/CheckerTestUtil.kt`** -> AI Confidence: **99.31%**
338. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/utils/DebugInfoUtil.kt`** -> AI Confidence: **99.31%**
339. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/ContractDeserializerImpl.kt`** -> AI Confidence: **99.31%**
340. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/PsiConditionParser.kt`** -> AI Confidence: **99.31%**
341. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/PsiContractParserDispatcher.kt`** -> AI Confidence: **99.31%**
342. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/diagnosticUtils.kt`** -> AI Confidence: **99.31%**
343. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/Renderers.kt`** -> AI Confidence: **99.31%**
344. **`compiler/frontend/src/org/jetbrains/kotlin/idea/MainFunctionDetector.kt`** -> AI Confidence: **99.31%**
345. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AllUnderImportScope.kt`** -> AI Confidence: **99.31%**
346. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnnotationChecker.kt`** -> AI Confidence: **99.31%**
347. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnnotationUseSiteTargetChecker.kt`** -> AI Confidence: **99.31%**
348. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DelegatedPropertyResolver.kt`** -> AI Confidence: **99.31%**
349. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DescriptorToSourceUtils.kt`** -> AI Confidence: **99.31%**
350. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ExposedVisibilityChecker.kt`** -> AI Confidence: **99.31%**
351. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/FunctionDescriptorResolver.kt`** -> AI Confidence: **99.31%**
352. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/LateinitModifierApplicabilityChecker.kt`** -> AI Confidence: **99.31%**
353. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ModifiersChecker.kt`** -> AI Confidence: **99.31%**
354. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/OverloadChecker.kt`** -> AI Confidence: **99.31%**
355. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/OverloadResolver.kt`** -> AI Confidence: **99.31%**
356. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/QualifiedExpressionResolveUtil.kt`** -> AI Confidence: **99.31%**
357. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/QualifiedExpressionResolver.kt`** -> AI Confidence: **99.31%**
358. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ShadowedExtensionChecker.kt`** -> AI Confidence: **99.31%**
359. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/TypeBinding.kt`** -> AI Confidence: **99.31%**
360. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/TypeResolver.kt`** -> AI Confidence: **99.31%**
361. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/bindingContextUtil/BindingContextUtils.kt`** -> AI Confidence: **99.31%**
362. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/CallCompleter.kt`** -> AI Confidence: **99.31%**
363. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/CallExpressionResolver.kt`** -> AI Confidence: **99.31%**
364. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/DiagnosticReporterByTrackingStrategy.kt`** -> AI Confidence: **99.31%**
365. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/AssigningNamedArgumentToVarargChecker.kt`** -> AI Confidence: **99.31%**
366. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/BuilderInferenceAssignmentChecker.kt`** -> AI Confidence: **99.31%**
367. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CallableReferenceCompatibilityChecker.kt`** -> AI Confidence: **99.31%**
368. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CapturingInClosureChecker.kt`** -> AI Confidence: **99.31%**
369. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CompanionLHSRelatedCheckers.kt`** -> AI Confidence: **99.31%**
370. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ContractNotAllowedCallChecker.kt`** -> AI Confidence: **99.31%**
371. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CustomEnumEntriesMigrationCallChecker.kt`** -> AI Confidence: **99.31%**
372. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/DslScopeViolationCallChecker.kt`** -> AI Confidence: **99.31%**
373. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/EqualityCallChecker.kt`** -> AI Confidence: **99.31%**
374. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ImplicitNothingAsTypeParameterCallChecker.kt`** -> AI Confidence: **99.31%**
375. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/IncorrectCapturedApproximationCallChecker.kt`** -> AI Confidence: **99.31%**
376. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/InlineChecker.kt`** -> AI Confidence: **99.31%**
377. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/LambdaWithSuspendModifierCallChecker.kt`** -> AI Confidence: **99.31%**
378. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/LateinitIntrinsicApplicabilityChecker.kt`** -> AI Confidence: **99.31%**
379. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/NewSchemeOfIntegerOperatorResolutionChecker.kt`** -> AI Confidence: **99.31%**
380. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/NullableVarargArgumentCallChecker.kt`** -> AI Confidence: **99.31%**
381. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/OperatorCallChecker.kt`** -> AI Confidence: **99.31%**
382. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ResultTypeWithNullableOperatorsChecker.kt`** -> AI Confidence: **99.31%**
383. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/coroutineCallChecker.kt`** -> AI Confidence: **99.31%**
384. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/ConstraintSystemBuilderImpl.kt`** -> AI Confidence: **99.31%**
385. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/TypeBoundsImpl.kt`** -> AI Confidence: **99.31%**
386. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/DataFlowInfoImpl.kt`** -> AI Confidence: **99.31%**
387. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/DataFlowUtils.kt`** -> AI Confidence: **99.31%**
388. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/DataFlowValueKindUtils.kt`** -> AI Confidence: **99.31%**
389. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/SmartCastManager.kt`** -> AI Confidence: **99.31%**
390. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/KotlinResolutionCallbacksImpl.kt`** -> AI Confidence: **99.31%**
391. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/KotlinToResolvedCallTransformer.kt`** -> AI Confidence: **99.31%**
392. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewAbstractResolvedCall.kt`** -> AI Confidence: **99.31%**
393. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/ResolvedAtomCompleter.kt`** -> AI Confidence: **99.31%**
394. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/util/CallResolverUtil.kt`** -> AI Confidence: **99.31%**
395. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ActualClassifierMustHasTheSameMembersAsNonFinalExpectClassifierChecker.kt`** -> AI Confidence: **99.31%**
396. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ConstModifierChecker.kt`** -> AI Confidence: **99.31%**
397. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/CyclicAnnotationsChecker.kt`** -> AI Confidence: **99.31%**
398. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/EnumCompanionInEnumConstructorCallChecker.kt`** -> AI Confidence: **99.31%**
399. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ExpectActualInTheSameModuleChecker.kt`** -> AI Confidence: **99.31%**
400. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ExpectedActualDeclarationChecker.kt`** -> AI Confidence: **99.31%**
401. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ExplicitApiDeclarationChecker.kt`** -> AI Confidence: **99.31%**
402. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/FunInterfaceDeclarationChecker.kt`** -> AI Confidence: **99.31%**
403. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/KClassWithIncorrectTypeArgumentChecker.kt`** -> AI Confidence: **99.31%**
404. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/OptInMarkerDeclarationAnnotationChecker.kt`** -> AI Confidence: **99.31%**
405. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/OptInUsageChecker.kt`** -> AI Confidence: **99.31%**
406. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/PassingProgressionAsCollectionCallChecker.kt`** -> AI Confidence: **99.31%**
407. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/PrimitiveNumericComparisonCallChecker.kt`** -> AI Confidence: **99.31%**
408. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ResultClassInReturnTypeChecker.kt`** -> AI Confidence: **99.31%**
409. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SealedInheritorInSameModuleChecker.kt`** -> AI Confidence: **99.31%**
410. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SealedInheritorInSamePackageChecker.kt`** -> AI Confidence: **99.31%**
411. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/UnderscoreChecker.kt`** -> AI Confidence: **99.31%**
412. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ValueClassDeclarationChecker.kt`** -> AI Confidence: **99.31%**
413. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/codegen/CodegenUtil.kt`** -> AI Confidence: **99.31%**
414. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/constants/evaluate/ConstantExpressionEvaluator.kt`** -> AI Confidence: **99.31%**
415. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/deprecation/Deprecation.kt`** -> AI Confidence: **99.31%**
416. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/inline/InlineAnalyzerExtension.kt`** -> AI Confidence: **99.31%**
417. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyClassMemberScope.kt`** -> AI Confidence: **99.31%**
418. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/sinceKotlinUtil.kt`** -> AI Confidence: **99.31%**
419. **`compiler/frontend/src/org/jetbrains/kotlin/types/CastDiagnosticsUtil.kt`** -> AI Confidence: **99.31%**
420. **`compiler/frontend/src/org/jetbrains/kotlin/types/enumCompatibilityChecker.kt`** -> AI Confidence: **99.31%**
421. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/DoubleColonExpressionResolver.kt`** -> AI Confidence: **99.31%**
422. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/FunctionsTypingVisitor.kt`** -> AI Confidence: **99.31%**
423. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/LabelResolver.kt`** -> AI Confidence: **99.31%**
424. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/PatternMatchingTypingVisitor.kt`** -> AI Confidence: **99.31%**
425. **`compiler/frontend/src/org/jetbrains/kotlin/util/IncrementalTrackerUtil.kt`** -> AI Confidence: **99.31%**
426. **`compiler/frontend/src/org/jetbrains/kotlin/util/declarationUtil.kt`** -> AI Confidence: **99.31%**
427. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalCompilerRunner.kt`** -> AI Confidence: **99.31%**
428. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/impl/ClassListSnapshotter.kt`** -> AI Confidence: **99.31%**
429. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/dirtyFiles/changesDetectionUtils.kt`** -> AI Confidence: **99.31%**
430. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ClosureAnnotator.kt`** -> AI Confidence: **99.31%**
431. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/DefaultArgumentFunctionFactory.kt`** -> AI Confidence: **99.31%**
432. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/EnumWhenLowering.kt`** -> AI Confidence: **99.31%**
433. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/FlattenStringConcatenationLowering.kt`** -> AI Confidence: **99.31%**
434. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/IfNullExpressionsFusionLowering.kt`** -> AI Confidence: **99.31%**
435. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/RangeContainsLowering.kt`** -> AI Confidence: **99.31%**
436. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ReturnableBlockTransformer.kt`** -> AI Confidence: **99.31%**
437. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/UpgradeCallableReferences.kt`** -> AI Confidence: **99.31%**
438. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/VersionOverloadsLowering.kt`** -> AI Confidence: **99.31%**
439. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/JavaLikeCounterLoopBuilder.kt`** -> AI Confidence: **99.31%**
440. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/NumericForLoopHeader.kt`** -> AI Confidence: **99.31%**
441. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/ProgressionLoopHeader.kt`** -> AI Confidence: **99.31%**
442. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/Utils.kt`** -> AI Confidence: **99.31%**
443. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/DownToHandler.kt`** -> AI Confidence: **99.31%**
444. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/RangeToHandler.kt`** -> AI Confidence: **99.31%**
445. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/optimizations/PropertyAccessorInlineLowering.kt`** -> AI Confidence: **99.31%**
446. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/JsUsefulDeclarationProcessor.kt`** -> AI Confidence: **99.31%**
447. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/UsefulDeclarationProcessor.kt`** -> AI Confidence: **99.31%**
448. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/CacheUpdater.kt`** -> AI Confidence: **99.31%**
449. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/IncrementalCache.kt`** -> AI Confidence: **99.31%**
450. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ir/exportUtils.kt`** -> AI Confidence: **99.31%**
451. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/jsexport/ExportModelGenerator.kt`** -> AI Confidence: **99.31%**
452. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/jsexport/ExportModelToJsStatements.kt`** -> AI Confidence: **99.31%**
453. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/AutoboxingTransformer.kt`** -> AI Confidence: **99.31%**
454. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/BlockDecomposerLowering.kt`** -> AI Confidence: **99.31%**
455. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ImplicitlyExportedDeclarationsMarkingLowering.kt`** -> AI Confidence: **99.31%**
456. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/MoveBodilessDeclarationsToSeparatePlace.kt`** -> AI Confidence: **99.31%**
457. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PurifyObjectInstanceGettersLowering.kt`** -> AI Confidence: **99.31%**
458. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/StaticMembersLowering.kt`** -> AI Confidence: **99.31%**
459. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/TestGenerator.kt`** -> AI Confidence: **99.31%**
460. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ThrowableLowering.kt`** -> AI Confidence: **99.31%**
461. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/TypeOperatorLowering.kt`** -> AI Confidence: **99.31%**
462. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/VarargLowering.kt`** -> AI Confidence: **99.31%**
463. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/BoxedLongCallsTransformer.kt`** -> AI Confidence: **99.31%**
464. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/EqualityAndComparisonCallsTransformer.kt`** -> AI Confidence: **99.31%**
465. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/MethodsOfAnyCallsTransformer.kt`** -> AI Confidence: **99.31%**
466. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/NumberOperatorCallsTransformer.kt`** -> AI Confidence: **99.31%**
467. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/StateMachineBuilder.kt`** -> AI Confidence: **99.31%**
468. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/IrElementToJsExpressionTransformer.kt`** -> AI Confidence: **99.31%**
469. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsCallTransformer.kt`** -> AI Confidence: **99.31%**
470. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsNameLinkingNamer.kt`** -> AI Confidence: **99.31%**
471. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/Merger.kt`** -> AI Confidence: **99.31%**
472. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/jsAstUtils.kt`** -> AI Confidence: **99.31%**
473. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/tsexport/ExportModelGenerator.kt`** -> AI Confidence: **99.31%**
474. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/NameTables.kt`** -> AI Confidence: **99.31%**
475. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/AnnotationCodegen.kt`** -> AI Confidence: **99.31%**
476. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/ClassCodegen.kt`** -> AI Confidence: **99.31%**
477. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/CoroutineCodegen.kt`** -> AI Confidence: **99.31%**
478. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/ExpressionCodegen.kt`** -> AI Confidence: **99.31%**
479. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/FunctionCodegen.kt`** -> AI Confidence: **99.31%**
480. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/SwitchGenerator.kt`** -> AI Confidence: **99.31%**
481. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/irCodegenUtils.kt`** -> AI Confidence: **99.31%**
482. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/Equals.kt`** -> AI Confidence: **99.31%**
483. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/HashCode.kt`** -> AI Confidence: **99.31%**
484. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/AddContinuationLowering.kt`** -> AI Confidence: **99.31%**
485. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/BridgeLowering.kt`** -> AI Confidence: **99.31%**
486. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FunctionReferenceLowering.kt`** -> AI Confidence: **99.31%**
487. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/GenerateMultifileFacades.kt`** -> AI Confidence: **99.31%**
488. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InheritedDefaultMethodsOnClassesLowering.kt`** -> AI Confidence: **99.31%**
489. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InterfaceLowering.kt`** -> AI Confidence: **99.31%**
490. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmInlineClassLowering.kt`** -> AI Confidence: **99.31%**
491. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmInlineMultiFieldValueClassLowering.kt`** -> AI Confidence: **99.31%**
492. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmIrLowerUtils.kt`** -> AI Confidence: **99.31%**
493. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmOptimizationLowering.kt`** -> AI Confidence: **99.31%**
494. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmSafeCallChainFoldingLowering.kt`** -> AI Confidence: **99.31%**
495. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmStringConcatenationLowering.kt`** -> AI Confidence: **99.31%**
496. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PropertyReferenceDelegationLowering.kt`** -> AI Confidence: **99.31%**
497. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/TailCallOptimizationLowering.kt`** -> AI Confidence: **99.31%**
498. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/indy/LambdaMetafactoryArguments.kt`** -> AI Confidence: **99.31%**
499. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/InlineClassAbi.kt`** -> AI Confidence: **99.31%**
500. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmCachedDeclarations.kt`** -> AI Confidence: **99.31%**
501. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmSyntheticAccessorGenerator.kt`** -> AI Confidence: **99.31%**
502. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MemoizedMultiFieldValueClassReplacements.kt`** -> AI Confidence: **99.31%**
503. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MfvcNodeFactory.kt`** -> AI Confidence: **99.31%**
504. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/IrArrayBuilder.kt`** -> AI Confidence: **99.31%**
505. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmDefaultUtils.kt`** -> AI Confidence: **99.31%**
506. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmIrCoroutineUtils.kt`** -> AI Confidence: **99.31%**
507. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmIrInlineUtils.kt`** -> AI Confidence: **99.31%**
508. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmIrUtils.kt`** -> AI Confidence: **99.31%**
509. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/mapping/MethodSignatureMapper.kt`** -> AI Confidence: **99.31%**
510. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/checkers/EscapeAnalysisChecker.kt`** -> AI Confidence: **99.31%**
511. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/SpecialBackendChecksTraversal.kt`** -> AI Confidence: **99.31%**
512. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/dce/WasmUsefulDeclarationProcessor.kt`** -> AI Confidence: **99.31%**
513. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/export/ExportModelGenerator.kt`** -> AI Confidence: **99.31%**
514. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/ClassInfo.kt`** -> AI Confidence: **99.31%**
515. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/WasmCompiledModuleFragment.kt`** -> AI Confidence: **99.31%**
516. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/BodyGenerator.kt`** -> AI Confidence: **99.31%**
517. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/OptimisedWhenGenerator.kt`** -> AI Confidence: **99.31%**
518. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/BuiltInsLowering.kt`** -> AI Confidence: **99.31%**
519. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/ComplexExternalDeclarationsToTopLevelFunctionsLowering.kt`** -> AI Confidence: **99.31%**
520. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/JsCodeCallsLowering.kt`** -> AI Confidence: **99.31%**
521. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/JsInteropFunctionsLowering.kt`** -> AI Confidence: **99.31%**
522. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/UnitToVoidLowering.kt`** -> AI Confidence: **99.31%**
523. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmStringSwitchOptimizerLowering.kt`** -> AI Confidence: **99.31%**
524. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmTypeOperatorLowering.kt`** -> AI Confidence: **99.31%**
525. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmVarargExpressionLowering.kt`** -> AI Confidence: **99.31%**
526. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WhenBranchOptimiserLowering.kt`** -> AI Confidence: **99.31%**
527. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/SourceMapGenerator.kt`** -> AI Confidence: **99.31%**
528. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/Utils.kt`** -> AI Confidence: **99.31%**
529. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/wasmCompiler.kt`** -> AI Confidence: **99.31%**
530. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrExpectActualMatchingContext.kt`** -> AI Confidence: **99.31%**
531. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/IrAnnotationConflictingDefaultArgumentValueKmpChecker.kt`** -> AI Confidence: **99.31%**
532. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/IrJavaDirectActualizationDefaultParametersInActualKmpChecker.kt`** -> AI Confidence: **99.31%**
533. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/IrKotlinActualAnnotationOnJavaKmpChecker.kt`** -> AI Confidence: **99.31%**
534. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/IrInterpreter.kt`** -> AI Confidence: **99.31%**
535. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/Utils.kt`** -> AI Confidence: **99.31%**
536. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/checker/IrInterpreterCommonChecker.kt`** -> AI Confidence: **99.31%**
537. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/preprocessor/IrInterpreterKCallableNamePreprocessor.kt`** -> AI Confidence: **99.31%**
538. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/CommonProxy.kt`** -> AI Confidence: **99.31%**
539. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/reflection/KFunctionProxy.kt`** -> AI Confidence: **99.31%**
540. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/ExceptionState.kt`** -> AI Confidence: **99.31%**
541. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/State.kt`** -> AI Confidence: **99.31%**
542. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/ReflectionState.kt`** -> AI Confidence: **99.31%**
543. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstAnnotationTransformer.kt`** -> AI Confidence: **99.31%**
544. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ArgumentsGenerationUtils.kt`** -> AI Confidence: **99.31%**
545. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/AssignmentGenerator.kt`** -> AI Confidence: **99.31%**
546. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/BranchingExpressionGenerator.kt`** -> AI Confidence: **99.31%**
547. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/CallGenerator.kt`** -> AI Confidence: **99.31%**
548. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DeclarationStubGeneratorImpl.kt`** -> AI Confidence: **99.31%**
549. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/FunctionGenerator.kt`** -> AI Confidence: **99.31%**
550. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/LoopExpressionGenerator.kt`** -> AI Confidence: **99.31%**
551. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/OperatorExpressionGenerator.kt`** -> AI Confidence: **99.31%**
552. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/PropertyGenerator.kt`** -> AI Confidence: **99.31%**
553. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ReflectionReferencesGenerator.kt`** -> AI Confidence: **99.31%**
554. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/transformations/InsertImplicitCasts.kt`** -> AI Confidence: **99.31%**
555. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/declarations/IrFunction.kt`** -> AI Confidence: **99.31%**
556. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/expressions/IrMemberAccessExpression.kt`** -> AI Confidence: **99.31%**
557. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/IrFakeOverrideBuilder.kt`** -> AI Confidence: **99.31%**
558. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/IrOverrideChecker.kt`** -> AI Confidence: **99.31%**
559. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/irTypes.kt`** -> AI Confidence: **99.31%**
560. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/AdditionalIrUtils.kt`** -> AI Confidence: **99.31%**
561. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DumpIrTree.kt`** -> AI Confidence: **99.31%**
562. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrTypeErasureUtils.kt`** -> AI Confidence: **99.31%**
563. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrUtils.kt`** -> AI Confidence: **99.31%**
564. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/dumpKotlinLike.kt`** -> AI Confidence: **99.31%**
565. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/DeepCopyIrTreeWithSymbolsPrinter.kt`** -> AI Confidence: **99.31%**
566. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TypeVisitorPrinter.kt`** -> AI Confidence: **99.31%**
567. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/CheckerUtils.kt`** -> AI Confidence: **99.31%**
568. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/KlibLoaderExtensions.kt`** -> AI Confidence: **99.31%**
569. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageErrorMessages.kt`** -> AI Confidence: **99.31%**
570. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartiallyLinkedIrTreePatcher.kt`** -> AI Confidence: **99.31%**
571. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/DescriptorByIdSignatureFinderImpl.kt`** -> AI Confidence: **99.31%**
572. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/symbols/symbolBasedTypes.kt`** -> AI Confidence: **99.31%**
573. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedField.kt`** -> AI Confidence: **99.31%**
574. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/treeBasedTypes.kt`** -> AI Confidence: **99.31%**
575. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightModifierListDescriptorBased.kt`** -> AI Confidence: **99.31%**
576. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/lightAnnotations.kt`** -> AI Confidence: **99.31%**
577. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/utils.kt`** -> AI Confidence: **99.31%**
578. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/KDocParser.kt`** -> AI Confidence: **99.31%**
579. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/KotlinExpressionParsing.kt`** -> AI Confidence: **99.31%**
580. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/KotlinParsing.kt`** -> AI Confidence: **99.31%**
581. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/SemanticWhitespaceAwareSyntaxBuilders.kt`** -> AI Confidence: **99.31%**
582. **`compiler/psi/parser/src/org/jetbrains/kotlin/kdoc/parser/KDocLinkParser.kt`** -> AI Confidence: **99.31%**
583. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/kdoc/psi/impl/KDocTag.kt`** -> AI Confidence: **99.31%**
584. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtCommonFile.kt`** -> AI Confidence: **99.31%**
585. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/TypeRefHelpers.kt`** -> AI Confidence: **99.31%**
586. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/addRemoveModifier.kt`** -> AI Confidence: **99.31%**
587. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/createByPattern.kt`** -> AI Confidence: **99.31%**
588. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/psiUtil/ClassIdCalculator.kt`** -> AI Confidence: **99.31%**
589. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/psiUtil/ktPsiUtil.kt`** -> AI Confidence: **99.31%**
590. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/utils/ConstantExpressionUtils.kt`** -> AI Confidence: **99.31%**
591. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/BlockExpressionElementType.kt`** -> AI Confidence: **99.31%**
592. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/ConstraintIncorporator.kt`** -> AI Confidence: **99.31%**
593. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/ConstraintInjector.kt`** -> AI Confidence: **99.31%**
594. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/PostponedArgumentInputTypesResolver.kt`** -> AI Confidence: **99.31%**
595. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/ResultTypeResolver.kt`** -> AI Confidence: **99.31%**
596. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/TypeCheckerStateForConstraintSystem.kt`** -> AI Confidence: **99.31%**
597. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/TypeVariableDependencyInformationProvider.kt`** -> AI Confidence: **99.31%**
598. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/VariableFixationFinder.kt`** -> AI Confidence: **99.31%**
599. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/model/MutableConstraintStorage.kt`** -> AI Confidence: **99.31%**
600. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/mpp/AbstractExpectActualAnnotationMatchChecker.kt`** -> AI Confidence: **99.31%**
601. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/mpp/AbstractExpectActualChecker.kt`** -> AI Confidence: **99.31%**
602. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/mpp/AbstractExpectActualMatcher.kt`** -> AI Confidence: **99.31%**
603. **`compiler/resolution.common/src/org/jetbrains/kotlin/types/AbstractTypeApproximator.kt`** -> AI Confidence: **99.31%**
604. **`compiler/resolution/src/org/jetbrains/kotlin/contracts/model/functors/SubstitutingFunctor.kt`** -> AI Confidence: **99.31%**
605. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/KotlinCallResolver.kt`** -> AI Confidence: **99.31%**
606. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/AdditionalDiagnosticReporter.kt`** -> AI Confidence: **99.31%**
607. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/ArgumentsToParametersMapper.kt`** -> AI Confidence: **99.31%**
608. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/ArgumentsUtils.kt`** -> AI Confidence: **99.31%**
609. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/CompletionModeCalculator.kt`** -> AI Confidence: **99.31%**
610. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/KotlinCallCompleter.kt`** -> AI Confidence: **99.31%**
611. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/PostponeArgumentsChecks.kt`** -> AI Confidence: **99.31%**
612. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/PostponedArgumentsAnalyzer.kt`** -> AI Confidence: **99.31%**
613. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/ResolutionParts.kt`** -> AI Confidence: **99.31%**
614. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/SamTypeConversions.kt`** -> AI Confidence: **99.31%**
615. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/SimpleArgumentsChecks.kt`** -> AI Confidence: **99.31%**
616. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/candidate/ResolutionCandidate.kt`** -> AI Confidence: **99.31%**
617. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/components/KotlinConstraintSystemCompleter.kt`** -> AI Confidence: **99.31%**
618. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/components/NewTypeSubstitutor.kt`** -> AI Confidence: **99.31%**
619. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/results/OverloadingConflictResolver.kt`** -> AI Confidence: **99.31%**
620. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tasks/synthesizedInvokes.kt`** -> AI Confidence: **99.31%**
621. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/InvokeProcessors.kt`** -> AI Confidence: **99.31%**
622. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/TowerLevels.kt`** -> AI Confidence: **99.31%**
623. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/TowerResolver.kt`** -> AI Confidence: **99.31%**
624. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/util/isFromStdlibJre7Or8.kt`** -> AI Confidence: **99.31%**
625. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/multiplatform/K1AbstractExpectActualAnnotationMatchChecker.kt`** -> AI Confidence: **99.31%**
626. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/multiplatform/K1AbstractExpectActualCompatibilityChecker.kt`** -> AI Confidence: **99.31%**
627. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/DescriptorSerializer.kt`** -> AI Confidence: **99.31%**
628. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/elvis.kt`** -> AI Confidence: **99.31%**
629. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/localInference.fir.kt`** -> AI Confidence: **99.31%**
630. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/localInference.kt`** -> AI Confidence: **99.31%**
631. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/equalsOnNonNull.fir.kt`** -> AI Confidence: **99.31%**
632. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/equalsOnNonNull.kt`** -> AI Confidence: **99.31%**
633. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/FirErrorsDefaultMessagesHelper.kt`** -> AI Confidence: **99.31%**
634. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/SteppingTestUtils.kt`** -> AI Confidence: **99.31%**
635. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/inferencelogs/MarkdownInferenceLogsDumper.kt`** -> AI Confidence: **99.31%**
636. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/asJava/PsiClassRenderer.kt`** -> AI Confidence: **99.31%**
637. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/cfg/pseudocodeUtils.kt`** -> AI Confidence: **99.31%**
638. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/checkers/CompilerTestLanguageVersionSettings.kt`** -> AI Confidence: **99.31%**
639. **`compiler/util-klib/src/org/jetbrains/kotlin/library/KotlinLibrary.kt`** -> AI Confidence: **99.31%**
640. **`compiler/util-klib/src/org/jetbrains/kotlin/library/SearchPathResolver.kt`** -> AI Confidence: **99.31%**
641. **`compiler/util/src/org/jetbrains/kotlin/utils/LibraryUtils.kt`** -> AI Confidence: **99.31%**
642. **`compiler/util/src/org/jetbrains/kotlin/utils/kapt/MemoryLeakDetector.kt`** -> AI Confidence: **99.31%**
643. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/load/java/AbstractAnnotationTypeQualifierResolver.kt`** -> AI Confidence: **99.31%**
644. **`core/compiler.common/src/org/jetbrains/kotlin/stats/MarkdownReportRenderer.kt`** -> AI Confidence: **99.31%**
645. **`core/compiler.common/src/org/jetbrains/kotlin/types/AbstractTypeChecker.kt`** -> AI Confidence: **99.31%**
646. **`core/compiler.common/src/org/jetbrains/kotlin/util/PerformanceManager.kt`** -> AI Confidence: **99.31%**
647. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/JavaIncompatibilityRulesOverridabilityCondition.kt`** -> AI Confidence: **99.31%**
648. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/types/JavaTypeResolver.kt`** -> AI Confidence: **99.31%**
649. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/types/RawSubstitution.kt`** -> AI Confidence: **99.31%**
650. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/specialBuiltinMembers.kt`** -> AI Confidence: **99.31%**
651. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/typeEnhancement/signatureEnhancement.kt`** -> AI Confidence: **99.31%**
652. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/typeEnhancement/typeEnhancement.kt`** -> AI Confidence: **99.31%**
653. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/DeserializedDescriptorResolver.kt`** -> AI Confidence: **99.31%**
654. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/methodSignatureMapping.kt`** -> AI Confidence: **99.31%**
655. **`core/descriptors/src/org/jetbrains/kotlin/builtins/ReflectionTypes.kt`** -> AI Confidence: **99.31%**
656. **`core/descriptors/src/org/jetbrains/kotlin/builtins/functionTypes.kt`** -> AI Confidence: **99.31%**
657. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/descriptorUtil.kt`** -> AI Confidence: **99.31%**
658. **`core/descriptors/src/org/jetbrains/kotlin/renderer/DescriptorRendererImpl.kt`** -> AI Confidence: **99.31%**
659. **`core/descriptors/src/org/jetbrains/kotlin/resolve/DescriptorUtils.kt`** -> AI Confidence: **99.31%**
660. **`core/descriptors/src/org/jetbrains/kotlin/resolve/SealedClassInheritorsProvider.kt`** -> AI Confidence: **99.31%**
661. **`core/descriptors/src/org/jetbrains/kotlin/resolve/inlineClassesUtils.kt`** -> AI Confidence: **99.31%**
662. **`core/descriptors/src/org/jetbrains/kotlin/resolve/sam/SamConversionResolverImpl.kt`** -> AI Confidence: **99.31%**
663. **`core/descriptors/src/org/jetbrains/kotlin/types/CapturedTypeApproximation.kt`** -> AI Confidence: **99.31%**
664. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeAliasExpander.kt`** -> AI Confidence: **99.31%**
665. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeParameterUpperBoundEraser.kt`** -> AI Confidence: **99.31%**
666. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeUtils.kt`** -> AI Confidence: **99.31%**
667. **`core/deserialization.common.jvm/src/org/jetbrains/kotlin/load/kotlin/AbstractBinaryClassAnnotationLoader.kt`** -> AI Confidence: **99.31%**
668. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/MemberDeserializer.kt`** -> AI Confidence: **99.31%**
669. **`core/metadata.jvm/src/org/jetbrains/kotlin/metadata/jvm/deserialization/JvmProtoBufUtil.kt`** -> AI Confidence: **99.31%**
670. **`core/metadata.jvm/src/org/jetbrains/kotlin/metadata/jvm/deserialization/ModuleMapping.kt`** -> AI Confidence: **99.31%**
671. **`core/metadata.jvm/src/org/jetbrains/kotlin/metadata/jvm/serialization/JvmStringTable.kt`** -> AI Confidence: **99.31%**
672. **`core/reflection.jvm/src/kotlin/reflect/full/KClasses.kt`** -> AI Confidence: **99.31%**
673. **`core/reflection.jvm/src/kotlin/reflect/jvm/KTypesJvm.kt`** -> AI Confidence: **99.31%**
674. **`core/reflection.jvm/src/kotlin/reflect/jvm/ReflectJvmMapping.kt`** -> AI Confidence: **99.31%**
675. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ConvertFromJava.kt`** -> AI Confidence: **99.31%**
676. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ConvertFromMetadata.kt`** -> AI Confidence: **99.31%**
677. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/DescriptorKFunction.kt`** -> AI Confidence: **99.31%**
678. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/DescriptorKParameter.kt`** -> AI Confidence: **99.31%**
679. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/DescriptorKProperty.kt`** -> AI Confidence: **99.31%**
680. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/JavaKFunction.kt`** -> AI Confidence: **99.31%**
681. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KClassImpl.kt`** -> AI Confidence: **99.31%**
682. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KDeclarationContainerImpl.kt`** -> AI Confidence: **99.31%**
683. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KotlinKFunction.kt`** -> AI Confidence: **99.31%**
684. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectKCallable.kt`** -> AI Confidence: **99.31%**
685. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectKProperty.kt`** -> AI Confidence: **99.31%**
686. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectionObjectRenderer.kt`** -> AI Confidence: **99.31%**
687. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/calls/ValueClassAwareCaller.kt`** -> AI Confidence: **99.31%**
688. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/fakeOverrides.kt`** -> AI Confidence: **99.31%**
689. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/DescriptorKType.kt`** -> AI Confidence: **99.31%**
690. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/KTypeSubstitutor.kt`** -> AI Confidence: **99.31%**
691. **`core/util.runtime/src/org/jetbrains/kotlin/utils/addToStdlib.kt`** -> AI Confidence: **99.31%**
692. **`generators/builtins/unsignedTypes.kt`** -> AI Confidence: **99.31%**
693. **`generators/evaluate/GenerateOperationsMap.kt`** -> AI Confidence: **99.31%**
694. **`generators/ide-iml-to-gradle-generator/src/org/jetbrains/kotlin/generators/imltogradle/Main.kt`** -> AI Confidence: **99.31%**
695. **`generators/tree-generator-common/src/org/jetbrains/kotlin/generators/tree/printer/printUtils.kt`** -> AI Confidence: **99.31%**
696. **`jps/jps-common/src/org/jetbrains/kotlin/config/facetSerialization.kt`** -> AI Confidence: **99.31%**
697. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/model/ModuleSettings.kt`** -> AI Confidence: **99.31%**
698. **`js/js.config/src/org/jetbrains/kotlin/utils/JsLibraryUtils.kt`** -> AI Confidence: **99.31%**
699. **`js/js.frontend/src/org/jetbrains/kotlin/js/naming/NameSuggestion.kt`** -> AI Confidence: **99.31%**
700. **`js/js.frontend/src/org/jetbrains/kotlin/js/naming/encodeSignature.kt`** -> AI Confidence: **99.31%**
701. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExportDeclarationChecker.kt`** -> AI Confidence: **99.31%**
702. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExternalArgumentCallChecker.kt`** -> AI Confidence: **99.31%**
703. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExternalChecker.kt`** -> AI Confidence: **99.31%**
704. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsInheritanceChecker.kt`** -> AI Confidence: **99.31%**
705. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsModuleCheckUtil.kt`** -> AI Confidence: **99.31%**
706. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsNameChecker.kt`** -> AI Confidence: **99.31%**
707. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsNameClashChecker.kt`** -> AI Confidence: **99.31%**
708. **`js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/JsAstExtensions.kt`** -> AI Confidence: **99.31%**
709. **`js/js.translator/src/org/jetbrains/kotlin/js/inline/clean/RedundantStatementElimination.kt`** -> AI Confidence: **99.31%**
710. **`js/js.translator/src/org/jetbrains/kotlin/js/inline/clean/TemporaryVariableElimination.kt`** -> AI Confidence: **99.31%**
711. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/ExportModelGenerator.kt`** -> AI Confidence: **99.31%**
712. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/TypeExporter.kt`** -> AI Confidence: **99.31%**
713. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/TypeParameterScope.kt`** -> AI Confidence: **99.31%**
714. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/exportModelUtils.kt`** -> AI Confidence: **99.31%**
715. **`kotlin-native/Interop/Indexer/src/main/kotlin/org/jetbrains/kotlin/native/interop/indexer/ModuleSupport.kt`** -> AI Confidence: **99.31%**
716. **`kotlin-native/Interop/Indexer/src/main/kotlin/org/jetbrains/kotlin/native/interop/indexer/Utils.kt`** -> AI Confidence: **99.31%**
717. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/StubIrDriver.kt`** -> AI Confidence: **99.31%**
718. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CacheBuilder.kt`** -> AI Confidence: **99.31%**
719. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CacheSupport.kt`** -> AI Confidence: **99.31%**
720. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CompilerOutput.kt`** -> AI Confidence: **99.31%**
721. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/Linker.kt`** -> AI Confidence: **99.31%**
722. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/NativeSecondStageCompilationConfig.kt`** -> AI Confidence: **99.31%**
723. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/OptimizationPipeline.kt`** -> AI Confidence: **99.31%**
724. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/SetupConfiguration.kt`** -> AI Confidence: **99.31%**
725. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cexport/CAdapterApiExporter.kt`** -> AI Confidence: **99.31%**
726. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cexport/CAdapterGenerator.kt`** -> AI Confidence: **99.31%**
727. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/IrToBitcode.kt`** -> AI Confidence: **99.31%**
728. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/LlvmDeclarations.kt`** -> AI Confidence: **99.31%**
729. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/RTTIGenerator.kt`** -> AI Confidence: **99.31%**
730. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/objc/linkObjC.kt`** -> AI Confidence: **99.31%**
731. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/objcexport/ObjCExportCodeGenerator.kt`** -> AI Confidence: **99.31%**
732. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/Autoboxing.kt`** -> AI Confidence: **99.31%**
733. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/BuiltinOperatorLowering.kt`** -> AI Confidence: **99.31%**
734. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/CachesAbiLowering.kt`** -> AI Confidence: **99.31%**
735. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeSuspendFunctionLowering.kt`** -> AI Confidence: **99.31%**
736. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ObjectClassLowering.kt`** -> AI Confidence: **99.31%**
737. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TestsDumper.kt`** -> AI Confidence: **99.31%**
738. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/VolatileFieldsLowering.kt`** -> AI Confidence: **99.31%**
739. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/objcexport/InfoPListBuilder.kt`** -> AI Confidence: **99.31%**
740. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportCodeSpec.kt`** -> AI Confidence: **99.31%**
741. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/CastsOptimization.kt`** -> AI Confidence: **99.31%**
742. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DCE.kt`** -> AI Confidence: **99.31%**
743. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DFGBuilder.kt`** -> AI Confidence: **99.31%**
744. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DevirtualizationAnalysis.kt`** -> AI Confidence: **99.31%**
745. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/EscapeAnalysis.kt`** -> AI Confidence: **99.31%**
746. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/KonanBCEForLoopBodyTransformer.kt`** -> AI Confidence: **99.31%**
747. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/PreCodegenInliner.kt`** -> AI Confidence: **99.31%**
748. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/StaticInitializersOptimization.kt`** -> AI Confidence: **99.31%**
749. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/ProtoUtils.kt`** -> AI Confidence: **99.31%**
750. **`kotlin-native/performance/benchmarksAnalyzer/src/commonMain/kotlin/org/jetbrains/analyzer/Statistics.kt`** -> AI Confidence: **99.31%**
751. **`kotlin-native/performance/benchmarksAnalyzer/src/commonMain/kotlin/org/jetbrains/analyzer/SummaryBenchmarksReport.kt`** -> AI Confidence: **99.31%**
752. **`kotlin-native/utilities/cli-runner/src/org/jetbrains/kotlin/cli/utilities/InteropCompiler.kt`** -> AI Confidence: **99.31%**
753. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/Readers.kt`** -> AI Confidence: **99.31%**
754. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/Writers.kt`** -> AI Confidence: **99.31%**
755. **`libraries/scripting/dependencies-maven/src/kotlin/script/experimental/dependencies/maven/MavenDependenciesResolver.kt`** -> AI Confidence: **99.31%**
756. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/jvmScriptSaving.kt`** -> AI Confidence: **99.31%**
757. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/jvmScriptingHostConfiguration.kt`** -> AI Confidence: **99.31%**
758. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/util/jvmClasspathUtil.kt`** -> AI Confidence: **99.31%**
759. **`libraries/stdlib/jdk8/src/kotlin/internal/jdk8/JDK8PlatformImplementations.kt`** -> AI Confidence: **99.31%**
760. **`libraries/stdlib/jvm/src/kotlin/io/encoding/Base64IOStream.kt`** -> AI Confidence: **99.31%**
761. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/reports/ClassReport.kt`** -> AI Confidence: **99.31%**
762. **`libraries/tools/abi-validation/abi-tools/src/main/kotlin/org/jetbrains/kotlin/abi/tools/impl/jvm/KotlinSignaturesLoading.kt`** -> AI Confidence: **99.31%**
763. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/testDsl.kt`** -> AI Confidence: **99.31%**
764. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/testHelpers.kt`** -> AI Confidence: **99.31%**
765. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/android-databinding/app/src/main/java/com/example/databinding/EnumAdapter.kt`** -> AI Confidence: **99.31%**
766. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleKotlinCompilerWork.kt`** -> AI Confidence: **99.31%**
767. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/ProcessedFilesCache.kt`** -> AI Confidence: **99.31%**
768. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/exec.kt`** -> AI Confidence: **99.31%**
769. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/KaptTask.kt`** -> AI Confidence: **99.31%**
770. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/stdlibDependencyManagement.kt`** -> AI Confidence: **99.31%**
771. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinPluginLifecycleImpl.kt`** -> AI Confidence: **99.31%**
772. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/KotlinSourceSetTreeDependsOnMismatchChecker.kt`** -> AI Confidence: **99.31%**
773. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/GranularMetadataTransformation.kt`** -> AI Confidence: **99.31%**
774. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/GenerateSyntheticLinkageImportProject.kt`** -> AI Confidence: **99.31%**
775. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/xcodeIntegrations.kt`** -> AI Confidence: **99.31%**
776. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/DefaultPomDependenciesRewriter.kt`** -> AI Confidence: **99.31%**
777. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/DefaultLanguageSettingsBuilder.kt`** -> AI Confidence: **99.31%**
778. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/kotlinBuildStatisticsUtils.kt`** -> AI Confidence: **99.31%**
779. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/reportDataUtil.kt`** -> AI Confidence: **99.31%**
780. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/CreateTargetConfigurationsSideEffect.kt`** -> AI Confidence: **99.31%**
781. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/internal/RewriteSourceMapFilterReader.kt`** -> AI Confidence: **99.31%**
782. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/AbstractPodInstallTask.kt`** -> AI Confidence: **99.31%**
783. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/PodGenTask.kt`** -> AI Confidence: **99.31%**
784. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/PodInstallSyntheticTask.kt`** -> AI Confidence: **99.31%**
785. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/PodspecTask.kt`** -> AI Confidence: **99.31%**
786. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/KotlinCompile.kt`** -> AI Confidence: **99.31%**
787. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/abi/KotlinAbiCheckTaskImpl.kt`** -> AI Confidence: **99.31%**
788. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/fileUtils.kt`** -> AI Confidence: **99.31%**
789. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/LazyResolvedConfigurationTest.kt`** -> AI Confidence: **99.31%**
790. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeSourceSetConstraintTest.kt`** -> AI Confidence: **99.31%**
791. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinCompilationArchiveTasksTest.kt`** -> AI Confidence: **99.31%**
792. **`libraries/tools/kotlin-gradle-statistics/src/main/kotlin/org/jetbrains/kotlin/statistics/fileloggers/MetricsContainer.kt`** -> AI Confidence: **99.31%**
793. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/mappings/string/StringLowercaseGenerator.kt`** -> AI Confidence: **99.31%**
794. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/AbstractFunctionOrPropertyCommonizer.kt`** -> AI Confidence: **99.31%**
795. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/AnnotationsCommonizer.kt`** -> AI Confidence: **99.31%**
796. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/CallableValueParametersCommonizer.kt`** -> AI Confidence: **99.31%**
797. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/ClassOrTypeAliasTypeCommonizer.kt`** -> AI Confidence: **99.31%**
798. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/transformer/ReApproximationCirNodeTransformer.kt`** -> AI Confidence: **99.31%**
799. **`native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/XcodeSimulatorExecutor.kt`** -> AI Confidence: **99.31%**
800. **`native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/cli/cli.kt`** -> AI Confidence: **99.31%**
801. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCNameChecker.kt`** -> AI Confidence: **99.31%**
802. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCRefinementAnnotationChecker.kt`** -> AI Confidence: **99.31%**
803. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCRefinementChecker.kt`** -> AI Confidence: **99.31%**
804. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCRefinementOverridesChecker.kt`** -> AI Confidence: **99.31%**
805. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/getInlineTargetTypeOrNull.kt`** -> AI Confidence: **99.31%**
806. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/getMethodBridge.kt`** -> AI Confidence: **99.31%**
807. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/isVisibleInObjC.kt`** -> AI Confidence: **99.31%**
808. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCClass.kt`** -> AI Confidence: **99.31%**
809. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCMethod.kt`** -> AI Confidence: **99.31%**
810. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCParameters.kt`** -> AI Confidence: **99.31%**
811. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCType.kt`** -> AI Confidence: **99.31%**
812. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/valueParametersAssociated.kt`** -> AI Confidence: **99.31%**
813. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportMapper.kt`** -> AI Confidence: **99.31%**
814. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportNamer.kt`** -> AI Confidence: **99.31%**
815. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/SirDeclarationFromKtSymbolProvider.kt`** -> AI Confidence: **99.31%**
816. **`native/swift/sir-printer/src/org/jetbrains/sir/printer/impl/SirAsSwiftSourcesPrinter.kt`** -> AI Confidence: **99.31%**
817. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/BridgeProvider/SirBridgeProviderImpl.kt`** -> AI Confidence: **99.31%**
818. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirTypeProviderImpl.kt`** -> AI Confidence: **99.31%**
819. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirVisibilityCheckerImpl.kt`** -> AI Confidence: **99.31%**
820. **`native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/KotlinxCoroutinesCore/KotlinxCoroutinesCore.kt`** -> AI Confidence: **99.31%**
821. **`native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/main/main.kt`** -> AI Confidence: **99.31%**
822. **`native/swift/swift-export-standalone/resources/swift/KotlinCoroutineSupport.kt`** -> AI Confidence: **99.31%**
823. **`native/utils/src/org/jetbrains/kotlin/konan/util/DependencyDownloader.kt`** -> AI Confidence: **99.31%**
824. **`native/utils/src/org/jetbrains/kotlin/konan/util/DependencyProcessor.kt`** -> AI Confidence: **99.31%**
825. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/common/AbstractAtomicfuTransformer.kt`** -> AI Confidence: **99.31%**
826. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/js/TransformerUtil.kt`** -> AI Confidence: **99.31%**
827. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/jvm/AtomicfuJvmIrTransformer.kt`** -> AI Confidence: **99.31%**
828. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/native/AtomicfuNativeIrTransformer.kt`** -> AI Confidence: **99.31%**
829. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/native/NativeAtomicfuIrBuilder.kt`** -> AI Confidence: **99.31%**
830. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractIrTransformTest.kt`** -> AI Confidence: **99.31%**
831. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/ComposeIrGenerationExtension.kt`** -> AI Confidence: **99.31%**
832. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/ComposePlugin.kt`** -> AI Confidence: **99.31%**
833. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/analysis/Stability.kt`** -> AI Confidence: **99.31%**
834. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposableCallChecker.kt`** -> AI Confidence: **99.31%**
835. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposableDeclarationChecker.kt`** -> AI Confidence: **99.31%**
836. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposeDiagnosticSuppressor.kt`** -> AI Confidence: **99.31%**
837. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposableCallChecker.kt`** -> AI Confidence: **99.31%**
838. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposableFunctionChecker.kt`** -> AI Confidence: **99.31%**
839. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/AbstractComposeLowering.kt`** -> AI Confidence: **99.31%**
840. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ClassStabilityTransformer.kt`** -> AI Confidence: **99.31%**
841. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableDefaultParamLowering.kt`** -> AI Confidence: **99.31%**
842. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt`** -> AI Confidence: **99.31%**
843. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableTargetAnnotationsTransformer.kt`** -> AI Confidence: **99.31%**
844. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableTypeRemapper.kt`** -> AI Confidence: **99.31%**
845. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposerLambdaMemoization.kt`** -> AI Confidence: **99.31%**
846. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposerParamTransformer.kt`** -> AI Confidence: **99.31%**
847. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/IrSourcePrinter.kt`** -> AI Confidence: **99.31%**
848. **`plugins/compose/group-mapping/src/main/kotlin/androidx/compose/compiler/mapping/group/GroupAnalysis.kt`** -> AI Confidence: **99.31%**
849. **`plugins/jvm-abi-gen/src/org/jetbrains/kotlin/jvm/abi/JvmAbiClassBuilderInterceptor.kt`** -> AI Confidence: **99.31%**
850. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/KaptContext.kt`** -> AI Confidence: **99.31%**
851. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/ProcessorLoader.kt`** -> AI Confidence: **99.31%**
852. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/stubs/KaptStubLineInformation.kt`** -> AI Confidence: **99.31%**
853. **`plugins/kapt/kapt-cli/src/KaptCli.kt`** -> AI Confidence: **99.31%**
854. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/FirKaptAnalysisHandlerExtension.kt`** -> AI Confidence: **99.31%**
855. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/ErrorTypeCorrector.kt`** -> AI Confidence: **99.31%**
856. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptStubConverter.kt`** -> AI Confidence: **99.31%**
857. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/parseParameters.kt`** -> AI Confidence: **99.31%**
858. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/PluginDataFrameSchemaParser.kt`** -> AI Confidence: **99.31%**
859. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/interpret.kt`** -> AI Confidence: **99.31%**
860. **`plugins/kotlin-dataframe/testFixturesResources/testUtils.kt`** -> AI Confidence: **99.31%**
861. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/BaseIrGenerator.kt`** -> AI Confidence: **99.31%**
862. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/Instantiator.kt`** -> AI Confidence: **99.31%**
863. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrPredicates.kt`** -> AI Confidence: **99.31%**
864. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializableIrGenerator.kt`** -> AI Confidence: **99.31%**
865. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializationJvmIrIntrinsicSupport.kt`** -> AI Confidence: **99.31%**
866. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializerSearchUtil.kt`** -> AI Confidence: **99.31%**
867. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/SerializationPluginDeclarationChecker.kt`** -> AI Confidence: **99.31%**
868. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/TypeUtil.kt`** -> AI Confidence: **99.31%**
869. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/extensions/SerializationResolveExtension.kt`** -> AI Confidence: **99.31%**
870. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/resolve/KSerializationUtil.kt`** -> AI Confidence: **99.31%**
871. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/resolve/SerializableProperties.kt`** -> AI Confidence: **99.31%**
872. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/SerializationFirResolveExtension.kt`** -> AI Confidence: **99.31%**
873. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/checkers/FirSerializationCompanionClassChecker.kt`** -> AI Confidence: **99.31%**
874. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/checkers/FirSerializationPluginClassChecker.kt`** -> AI Confidence: **99.31%**
875. **`plugins/kotlinx-serialization/testFixtures/org/jetbrains/kotlinx/serialization/matrix/cases/EnumsTestMatrix.kt`** -> AI Confidence: **99.31%**
876. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/AccessorGenerator.kt`** -> AI Confidence: **99.31%**
877. **`plugins/parcelize/parcelize-compiler/parcelize.backend/src/org/jetbrains/kotlin/parcelize/IrParcelSerializerFactory.kt`** -> AI Confidence: **99.31%**
878. **`plugins/parcelize/parcelize-compiler/parcelize.backend/src/org/jetbrains/kotlin/parcelize/ParcelizeIrTransformerBase.kt`** -> AI Confidence: **99.31%**
879. **`plugins/parcelize/parcelize-compiler/parcelize.k1/src/org/jetbrains/kotlin/parcelize/ParcelizeAnnotationChecker.kt`** -> AI Confidence: **99.31%**
880. **`plugins/parcelize/parcelize-compiler/parcelize.k1/src/org/jetbrains/kotlin/parcelize/ParcelizeDeclarationChecker.kt`** -> AI Confidence: **99.31%**
881. **`plugins/parcelize/parcelize-compiler/parcelize.k2/src/org/jetbrains/kotlin/parcelize/fir/diagnostics/FirParcelizePropertyChecker.kt`** -> AI Confidence: **99.31%**
882. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/PowerAssertCallTransformer.kt`** -> AI Confidence: **99.31%**
883. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/builder/parameter/StringParameterBuilder.kt`** -> AI Confidence: **99.31%**
884. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/diagram/DiagramBuilder.kt`** -> AI Confidence: **99.31%**
885. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/diagram/ExpressionTree.kt`** -> AI Confidence: **99.31%**
886. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/diagram/offsets.kt`** -> AI Confidence: **99.31%**
887. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/definitions/ScriptiDefinitionsFromClasspathDiscoverySource.kt`** -> AI Confidence: **99.31%**
888. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/resolve/refineCompilationConfiguration.kt`** -> AI Confidence: **99.31%**
889. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/ScriptingCommandLineProcessor.kt`** -> AI Confidence: **99.31%**
890. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/definitions/ScriptRefinedCompilationConfigurationCache.kt`** -> AI Confidence: **99.31%**
891. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/definitions/ScriptRefinedCompilationConfigurationCacheImpl.kt`** -> AI Confidence: **99.31%**
892. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/dependencies/ScriptsCompilationDependencies.kt`** -> AI Confidence: **99.31%**
893. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/errorReporting.kt`** -> AI Confidence: **99.31%**
894. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/k2ScriptAnnotationResolution.kt`** -> AI Confidence: **99.31%**
895. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/irLowerings/scriptingLoweringVisitors.kt`** -> AI Confidence: **99.31%**
896. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/ReplFromTerminal.kt`** -> AI Confidence: **99.31%**
897. **`plugins/scripting/scripting-compiler/tests/org/jetbrains/kotlin/scripting/compiler/plugin/testUtil.kt`** -> AI Confidence: **99.31%**
898. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/codeInsight/ReferenceVariantsHelper.kt`** -> AI Confidence: **99.31%**
899. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/FuzzyType.kt`** -> AI Confidence: **99.31%**
900. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/ImportsUtils.kt`** -> AI Confidence: **99.31%**
901. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/TypeUtils.kt`** -> AI Confidence: **99.31%**
902. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/Utils.kt`** -> AI Confidence: **99.31%**
903. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/implicitReceiversUtils.kt`** -> AI Confidence: **99.31%**
904. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/util/descriptorUtils.kt`** -> AI Confidence: **99.31%**
905. **`plugins/scripting/scripting-ide-services/src/org/jetbrains/kotlin/scripting/ide_services/compiler/impl/KJvmReplCompleter.kt`** -> AI Confidence: **99.31%**
906. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/common-configuration.gradle.kts`** -> AI Confidence: **99.31%**
907. **`repo/gradle-build-conventions/project-tests-convention/src/main/kotlin/generalTestTask.kt`** -> AI Confidence: **99.31%**
908. **`repo/gradle-build-conventions/utilities/src/main/kotlin/repoDependencies.kt`** -> AI Confidence: **99.31%**
909. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/WasmJsCodeCallsChecker.kt`** -> AI Confidence: **99.31%**
910. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/WasmJsInteropTypesChecker.kt`** -> AI Confidence: **99.31%**
911. **`wasm/wasm.ir/src/org/jetbrains/kotlin/wasm/ir/convertors/WasmIrToText.kt`** -> AI Confidence: **99.31%**
912. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/util/JdkClassFinder.java`** -> AI Confidence: **99.31%**
913. **`compiler/android-tests/tests/org/jetbrains/kotlin/android/tests/emulator/Emulator.java`** -> AI Confidence: **99.31%**
914. **`compiler/backend/src/org/jetbrains/kotlin/codegen/StackValue.java`** -> AI Confidence: **99.31%**
915. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/InternalFinallyBlockInliner.java`** -> AI Confidence: **99.31%**
916. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/diagnostics/DefaultErrorMessagesJvm.java`** -> AI Confidence: **99.31%**
917. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/kotlinSignature/SignaturesPropagationData.java`** -> AI Confidence: **99.31%**
918. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/DefaultErrorMessages.java`** -> AI Confidence: **99.31%**
919. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/BodyResolver.java`** -> AI Confidence: **99.31%**
920. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ControlFlowAnalyzer.java`** -> AI Confidence: **99.31%**
921. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/ValueArgumentsToParametersMapper.java`** -> AI Confidence: **99.31%**
922. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/ConstraintsUtil.java`** -> AI Confidence: **99.31%**
923. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/ForceResolveUtil.java`** -> AI Confidence: **99.31%**
924. **`compiler/frontend/src/org/jetbrains/kotlin/types/CommonSupertypes.java`** -> AI Confidence: **99.31%**
925. **`compiler/frontend/src/org/jetbrains/kotlin/types/TypeIntersector.java`** -> AI Confidence: **99.31%**
926. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/BasicExpressionTypingVisitor.java`** -> AI Confidence: **99.31%**
927. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/ControlStructureTypingVisitor.java`** -> AI Confidence: **99.31%**
928. **`compiler/frontend/src/org/jetbrains/kotlin/util/slicedMap/SlicedMapImpl.java`** -> AI Confidence: **99.31%**
929. **`compiler/preloader/instrumentation/src/org/jetbrains/kotlin/preloading/instrumentation/InterceptionInstrumenter.java`** -> AI Confidence: **99.31%**
930. **`compiler/preloader/src/org/jetbrains/kotlin/preloading/ClassPreloadingUtils.java`** -> AI Confidence: **99.31%**
931. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/AbstractKotlinParsing.java`** -> AI Confidence: **99.31%**
932. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinExpressionParsing.java`** -> AI Confidence: **99.31%**
933. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinParsing.java`** -> AI Confidence: **99.31%**
934. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtPsiUtil.java`** -> AI Confidence: **99.31%**
935. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/resolve/ExpectedResolveData.java`** -> AI Confidence: **99.31%**
936. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/resolve/ExpectedResolveDataUtil.java`** -> AI Confidence: **99.31%**
937. **`compiler/tests/org/jetbrains/kotlin/generators/tests/GenerateRangesCodegenTestData.java`** -> AI Confidence: **99.31%**
938. **`compiler/util/src/org/jetbrains/kotlin/config/MavenComparableVersion.java`** -> AI Confidence: **99.31%**
939. **`compiler/util/src/org/jetbrains/kotlin/utils/JavaSdkUtil.java`** -> AI Confidence: **99.31%**
940. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/VariableDescriptorWithInitializerImpl.java`** -> AI Confidence: **99.31%**
941. **`core/descriptors/src/org/jetbrains/kotlin/resolve/MemberComparator.java`** -> AI Confidence: **99.31%**
942. **`core/descriptors/src/org/jetbrains/kotlin/resolve/OverridingUtil.java`** -> AI Confidence: **99.31%**
943. **`dependencies/protobuf/protobuf-patches/src/main/java/com/google/protobuf/CodedInputStream.java`** -> AI Confidence: **99.31%**
944. **`js/js.ast/src/org/jetbrains/kotlin/js/backend/JsToStringGenerationVisitor.java`** -> AI Confidence: **99.31%**
945. **`js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptLexer.java`** -> AI Confidence: **99.31%**
946. **`js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java`** -> AI Confidence: **99.31%**
947. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/KotlinCompileMojoBase.java`** -> AI Confidence: **99.31%**
948. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/MavenPluginLogMessageCollector.java`** -> AI Confidence: **99.31%**
949. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/incremental/MavenICReporter.java`** -> AI Confidence: **99.31%**
950. **`kotlin-native/runtime/src/libbacktrace/c/dwarf.c`** -> AI Confidence: **99.31%**
951. **`kotlin-native/runtime/src/libbacktrace/c/fileline.c`** -> AI Confidence: **99.31%**
952. **`kotlin-native/runtime/src/libbacktrace/c/macho.c`** -> AI Confidence: **99.31%**
953. **`kotlin-native/runtime/src/libbacktrace/c/mmap.c`** -> AI Confidence: **99.31%**
954. **`kotlin-native/runtime/src/objc/cpp/ObjCExportCollections.mm`** -> AI Confidence: **99.31%**
955. **`native/native.tests/testData/interop/objc/kt56402/kt56402.m`** -> AI Confidence: **99.31%**
956. **`kotlin-native/libclangext/src/main/cpp/ClangExt.cpp`** -> AI Confidence: **99.31%**
957. **`kotlin-native/runtime/src/alloc/custom/cpp/FixedBlockPageTest.cpp`** -> AI Confidence: **99.31%**
958. **`kotlin-native/runtime/src/alloc/custom/cpp/GCApi.cpp`** -> AI Confidence: **99.31%**
959. **`kotlin-native/runtime/src/alloc/custom/cpp/NextFitPageTest.cpp`** -> AI Confidence: **99.31%**
960. **`kotlin-native/runtime/src/gc/cms/cpp/GCImplTest.cpp`** -> AI Confidence: **99.31%**
961. **`kotlin-native/runtime/src/gcScheduler/common/cpp/MutatorAssistsTest.cpp`** -> AI Confidence: **99.31%**
962. **`kotlin-native/runtime/src/main/cpp/BoundedQueueTest.cpp`** -> AI Confidence: **99.31%**
963. **`kotlin-native/runtime/src/main/cpp/ConditionVariableTest.cpp`** -> AI Confidence: **99.31%**
964. **`kotlin-native/runtime/src/main/cpp/Console.cpp`** -> AI Confidence: **99.31%**
965. **`kotlin-native/runtime/src/main/cpp/ExecFormat.cpp`** -> AI Confidence: **99.31%**
966. **`kotlin-native/runtime/src/main/cpp/SingleLockListTest.cpp`** -> AI Confidence: **99.31%**
967. **`kotlin-native/runtime/src/main/cpp/StackTrace.cpp`** -> AI Confidence: **99.31%**
968. **`kotlin-native/runtime/src/main/cpp/ToString.cpp`** -> AI Confidence: **99.31%**
969. **`kotlin-native/runtime/src/mm/cpp/ExceptionObjHolderTest.cpp`** -> AI Confidence: **99.31%**
970. **`kotlin-native/tools/llvm_builder/package.py`** -> AI Confidence: **99.31%**
971. **`libraries/tools/required-reason-finder/required_reason_finder.py`** -> AI Confidence: **99.31%**
972. **`native/swift/swift-export-standalone-integration-tests/simple/testData/execution/functional_type/functional_type.swift`** -> AI Confidence: **99.31%**
973. **`analysis/analysis-api/testData/components/compileTimeConstantProvider/evaluate/backingFieldAccessInPropertySetter.kt`** -> AI Confidence: **99.29%**
974. **`analysis/analysis-api/testData/components/dataFlowInfoProvider/exitPointSnapshot/controlFlow/breakContinue2.kt`** -> AI Confidence: **99.29%**
975. **`analysis/analysis-api/testData/components/dataFlowInfoProvider/exitPointSnapshot/controlFlow/conditionalJumps/break.kt`** -> AI Confidence: **99.29%**
976. **`analysis/analysis-api/testData/components/dataFlowInfoProvider/exitPointSnapshot/controlFlow/exitPointEquivalence/breakContinueAndDefault.kt`** -> AI Confidence: **99.29%**
977. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/break.kt`** -> AI Confidence: **99.29%**
978. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/continue.kt`** -> AI Confidence: **99.29%**
979. **`analysis/analysis-api/testData/components/resolver/allByPsi/contextSensitiveResolution/otherExpectedTypePositions/equalityOperator.kt`** -> AI Confidence: **99.29%**
980. **`analysis/analysis-api/testData/components/resolver/allByPsi/contextSensitiveResolution/otherExpectedTypePositions/equalityOperatorOnBoundedEnumTypeParameter.kt`** -> AI Confidence: **99.29%**
981. **`analysis/analysis-api/testData/components/resolver/allByPsi/contextSensitiveResolution/otherExpectedTypePositions/equalityOperatorOnBoundedSealedTypeParameter.kt`** -> AI Confidence: **99.29%**
982. **`analysis/analysis-api/testData/components/resolver/allByPsi/contextSensitiveResolution/otherExpectedTypePositions/whenIfLastStatementEnum.kt`** -> AI Confidence: **99.29%**
983. **`analysis/analysis-api/testData/components/resolver/allByPsi/destructuring/nameBasedDestructuringFullFormErrors.kt`** -> AI Confidence: **99.29%**
984. **`analysis/analysis-api/testData/components/resolver/allByPsi/destructuring/nameBasedDestructuringShortFormErrorsAfter.kt`** -> AI Confidence: **99.29%**
985. **`analysis/analysis-api/testData/components/resolver/singleByPsi/annotationOnExpression_if.kt`** -> AI Confidence: **99.29%**
986. **`analysis/analysis-api/testData/components/typeInfoProvider/isDenotable/smartcast.descriptors.kt`** -> AI Confidence: **99.29%**
987. **`analysis/analysis-api/testData/components/typeInfoProvider/isDenotable/smartcast.kt`** -> AI Confidence: **99.29%**
988. **`analysis/low-level-api-fir/testData/nonLocalDeclarationAnchors/topLevelFor.kts`** -> AI Confidence: **99.29%**
989. **`compiler/fir/analysis-tests/testData/resolve/catchParameter.kt`** -> AI Confidence: **99.29%**
990. **`compiler/fir/analysis-tests/testData/resolve/cfa/comparisonWithChangingTryBlock.kt`** -> AI Confidence: **99.29%**
991. **`compiler/fir/analysis-tests/testData/resolve/cfg/tryCatch.kt`** -> AI Confidence: **99.29%**
992. **`compiler/fir/analysis-tests/testData/resolve/collectionLiterals/stdlibTypes/fallbackInWhen.kt`** -> AI Confidence: **99.29%**
993. **`compiler/fir/analysis-tests/testData/resolve/collectionLiterals/stdlibTypes/trickyCases/upperAndLower.kt`** -> AI Confidence: **99.29%**
994. **`compiler/fir/analysis-tests/testData/resolve/collectionLiterals/stdlibTypes/withElvis.kt`** -> AI Confidence: **99.29%**
995. **`compiler/fir/analysis-tests/testData/resolve/collectionLiterals/stdlibTypes/withTry.kt`** -> AI Confidence: **99.29%**
996. **`compiler/fir/analysis-tests/testData/resolve/contextSensitiveResolutionUsingExpectedType/otherExpectedTypePositions/equalityOperator.kt`** -> AI Confidence: **99.29%**
997. **`compiler/fir/analysis-tests/testData/resolve/contextSensitiveResolutionUsingExpectedType/otherExpectedTypePositions/equalityOperatorOnBoundedEnumTypeParameter.kt`** -> AI Confidence: **99.29%**
998. **`compiler/fir/analysis-tests/testData/resolve/contextSensitiveResolutionUsingExpectedType/otherExpectedTypePositions/equalityOperatorOnBoundedSealedTypeParameter.kt`** -> AI Confidence: **99.29%**
999. **`compiler/fir/analysis-tests/testData/resolve/contextSensitiveResolutionUsingExpectedType/otherExpectedTypePositions/whenIfLastStatementEnum.kt`** -> AI Confidence: **99.29%**
1000. **`compiler/fir/analysis-tests/testData/resolve/destructuring/deprecationOfParensShortFormOfMapEntry.kt`** -> AI Confidence: **99.29%**
1001. **`compiler/fir/analysis-tests/testData/resolve/destructuring/deprecationOfParensShortFormOfNonDataClass.kt`** -> AI Confidence: **99.29%**
1002. **`compiler/fir/analysis-tests/testData/resolve/destructuring/deprecationOfParensShortFormWithNameMismatch.kt`** -> AI Confidence: **99.29%**
1003. **`compiler/fir/analysis-tests/testData/resolve/destructuring/nameBasedDestructuringFullFormErrors.kt`** -> AI Confidence: **99.29%**
1004. **`compiler/fir/analysis-tests/testData/resolve/destructuring/nameBasedDestructuringShortFormErrorsAfter.kt`** -> AI Confidence: **99.29%**
1005. **`compiler/fir/analysis-tests/testData/resolve/extraCheckers/emptyRangeChecker/NoWarning.kt`** -> AI Confidence: **99.29%**
1006. **`compiler/fir/analysis-tests/testData/resolve/extraCheckers/emptyRangeChecker/Warning.kt`** -> AI Confidence: **99.29%**
1007. **`compiler/fir/analysis-tests/testData/resolve/extraCheckers/unused/manyLocalVariables.kt`** -> AI Confidence: **99.29%**
1008. **`compiler/fir/raw-fir/light-tree2fir/testFixtures/org/jetbrains/kotlin/fir/lightTree/PathWalker.kt`** -> AI Confidence: **99.29%**
1009. **`compiler/fir/raw-fir/psi2fir/testData/rawBuilder/expressions/cascadeIf.kt`** -> AI Confidence: **99.29%**
1010. **`compiler/fir/raw-fir/psi2fir/testData/rawBuilder/expressions/try.kt`** -> AI Confidence: **99.29%**
1011. **`compiler/fir/raw-fir/psi2fir/testData/rawBuilder/expressions/whenGuards.kt`** -> AI Confidence: **99.29%**
1012. **`compiler/fir/raw-fir/psi2fir/testData/rawBuilder/expressions/while.kt`** -> AI Confidence: **99.29%**
1013. **`compiler/psi/psi-impl/testData/psi/CommentsBindingInStatementBlock.kt`** -> AI Confidence: **99.29%**
1014. **`compiler/psi/psi-impl/testData/psi/ControlStructures.kt`** -> AI Confidence: **99.29%**
1015. **`compiler/psi/psi-impl/testData/psi/ForWithMultiDecl.kt`** -> AI Confidence: **99.29%**
1016. **`compiler/psi/psi-impl/testData/psi/IfWithPropery.kt`** -> AI Confidence: **99.29%**
1017. **`compiler/psi/psi-impl/testData/psi/Precedence.kt`** -> AI Confidence: **99.29%**
1018. **`compiler/psi/psi-impl/testData/psi/TryRecovery.kt`** -> AI Confidence: **99.29%**
1019. **`compiler/psi/psi-impl/testData/psi/WhenWithSubjectVariable.kt`** -> AI Confidence: **99.29%**
1020. **`compiler/psi/psi-impl/testData/psi/WhenWithSubjectVariable_SoftModifierName.kt`** -> AI Confidence: **99.29%**
1021. **`compiler/psi/psi-impl/testData/psi/When_ERR.kt`** -> AI Confidence: **99.29%**
1022. **`compiler/psi/psi-impl/testData/psi/annotation/at/blockLevelExpressions.kt`** -> AI Confidence: **99.29%**
1023. **`compiler/psi/psi-impl/testData/psi/annotation/at/blockLevelExpressionsNoNewLine.kt`** -> AI Confidence: **99.29%**
1024. **`compiler/psi/psi-impl/testData/psi/annotation/forParameters.kt`** -> AI Confidence: **99.29%**
1025. **`compiler/psi/psi-impl/testData/psi/annotation/functionalTypes/regressionForSimilarSyntax/forDestructuring.kt`** -> AI Confidence: **99.29%**
1026. **`compiler/psi/psi-impl/testData/psi/destructuring/fullPositionBasedDestructuringErrors.kt`** -> AI Confidence: **99.29%**
1027. **`compiler/psi/psi-impl/testData/psi/operators/untilOperatorWithWhitespace.kt`** -> AI Confidence: **99.29%**
1028. **`compiler/psi/psi-impl/testData/psi/recovery/binaryExpression/IsExpressionComplex.kt`** -> AI Confidence: **99.29%**
1029. **`compiler/testData/asJava/lightClasses/lightClassByPsi/deprecatedHiddenProperty_accessors.kt`** -> AI Confidence: **99.29%**
1030. **`compiler/testData/cfg-variables/bugs/doWhileNotDefined.kt`** -> AI Confidence: **99.29%**
1031. **`compiler/testData/cfg/controlStructures/breakContinueInTryFinally.kt`** -> AI Confidence: **99.29%**
1032. **`compiler/testData/cfg/controlStructures/continueInDoWhile.kt`** -> AI Confidence: **99.29%**
1033. **`compiler/testData/cfg/controlStructures/continueInFor.kt`** -> AI Confidence: **99.29%**
1034. **`compiler/testData/cfg/controlStructures/continueInWhile.kt`** -> AI Confidence: **99.29%**
1035. **`compiler/testData/cfg/expressions/LazyBooleans.kt`** -> AI Confidence: **99.29%**
1036. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/fromPlatformTypes/conditions.fir.kt`** -> AI Confidence: **99.29%**
1037. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/fromPlatformTypes/conditions.kt`** -> AI Confidence: **99.29%**
1038. **`compiler/testData/diagnostics/tests/BreakContinue.fir.kt`** -> AI Confidence: **99.29%**
1039. **`compiler/testData/diagnostics/tests/BreakContinue.kt`** -> AI Confidence: **99.29%**
1040. **`compiler/testData/diagnostics/tests/BreakContinueInWhen_after.fir.kt`** -> AI Confidence: **99.29%**
1041. **`compiler/testData/diagnostics/tests/BreakContinueInWhen_after.kt`** -> AI Confidence: **99.29%**
1042. **`compiler/testData/diagnostics/tests/IdentityComparisonWithPrimitives.fir.kt`** -> AI Confidence: **99.29%**
1043. **`compiler/testData/diagnostics/tests/IdentityComparisonWithPrimitives.kt`** -> AI Confidence: **99.29%**
1044. **`compiler/testData/diagnostics/tests/Nullability.fir.kt`** -> AI Confidence: **99.29%**
1045. **`compiler/testData/diagnostics/tests/Nullability.kt`** -> AI Confidence: **99.29%**
1046. **`compiler/testData/diagnostics/tests/checkArguments/booleanExpressions.fir.kt`** -> AI Confidence: **99.29%**
1047. **`compiler/testData/diagnostics/tests/checkArguments/booleanExpressions.kt`** -> AI Confidence: **99.29%**
1048. **`compiler/testData/diagnostics/tests/constructorConsistency/backing.fir.kt`** -> AI Confidence: **99.29%**
1049. **`compiler/testData/diagnostics/tests/constructorConsistency/backing.kt`** -> AI Confidence: **99.29%**
1050. **`compiler/testData/diagnostics/tests/constructorConsistency/getset.fir.kt`** -> AI Confidence: **99.29%**
1051. **`compiler/testData/diagnostics/tests/constructorConsistency/getset.kt`** -> AI Confidence: **99.29%**
1052. **`compiler/testData/diagnostics/tests/constructorConsistency/initwithgetter.fir.kt`** -> AI Confidence: **99.29%**
1053. **`compiler/testData/diagnostics/tests/constructorConsistency/initwithgetter.kt`** -> AI Confidence: **99.29%**
1054. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/breakContinueInTryFinally.fir.kt`** -> AI Confidence: **99.29%**
1055. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/breakContinueInTryFinally.kt`** -> AI Confidence: **99.29%**
1056. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/breakContinueInTryFinallyInLoop.fir.kt`** -> AI Confidence: **99.29%**
1057. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/breakContinueInTryFinallyInLoop.kt`** -> AI Confidence: **99.29%**
1058. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/breakOrContinueInLoopCondition.fir.kt`** -> AI Confidence: **99.29%**
1059. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/breakOrContinueInLoopCondition.kt`** -> AI Confidence: **99.29%**
1060. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/cfgOfFullyIncorrectCode.fir.kt`** -> AI Confidence: **99.29%**
1061. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/cfgOfFullyIncorrectCode.kt`** -> AI Confidence: **99.29%**
1062. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/deadCode/deadCodeInWhileFromBreak.fir.kt`** -> AI Confidence: **99.29%**
1063. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/deadCode/deadCodeInWhileFromBreak.kt`** -> AI Confidence: **99.29%**
1064. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/doWhileNotDefined.kt`** -> AI Confidence: **99.29%**
1065. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/elvisNotProcessed.fir.kt`** -> AI Confidence: **99.29%**
1066. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/elvisNotProcessed.kt`** -> AI Confidence: **99.29%**
1067. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/kt10805.kt`** -> AI Confidence: **99.29%**
1068. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/reassignmenGraphLoop.fir.kt`** -> AI Confidence: **99.29%**
1069. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/reassignmenGraphLoop.kt`** -> AI Confidence: **99.29%**
1070. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/tryCatchFinallyIfs.kt`** -> AI Confidence: **99.29%**
1071. **`compiler/testData/diagnostics/tests/controlStructures/breakToLabel.fir.kt`** -> AI Confidence: **99.29%**
1072. **`compiler/testData/diagnostics/tests/controlStructures/breakToLabel.kt`** -> AI Confidence: **99.29%**
1073. **`compiler/testData/diagnostics/tests/controlStructures/catchOfTypeNothing.fir.kt`** -> AI Confidence: **99.29%**
1074. **`compiler/testData/diagnostics/tests/controlStructures/catchOfTypeNothing.kt`** -> AI Confidence: **99.29%**
1075. **`compiler/testData/diagnostics/tests/controlStructures/ifInResultOfLambda.kt`** -> AI Confidence: **99.29%**
1076. **`compiler/testData/diagnostics/tests/controlStructures/improperElseInExpression.fir.kt`** -> AI Confidence: **99.29%**
1077. **`compiler/testData/diagnostics/tests/controlStructures/improperElseInExpression.kt`** -> AI Confidence: **99.29%**
1078. **`compiler/testData/diagnostics/tests/controlStructures/kt10706.fir.kt`** -> AI Confidence: **99.29%**
1079. **`compiler/testData/diagnostics/tests/controlStructures/kt10706.kt`** -> AI Confidence: **99.29%**
1080. **`compiler/testData/diagnostics/tests/controlStructures/nonExhaustiveIfInElvis_after.kt`** -> AI Confidence: **99.29%**
1081. **`compiler/testData/diagnostics/tests/controlStructures/nonExhaustiveIfInElvis_before.fir.kt`** -> AI Confidence: **99.29%**
1082. **`compiler/testData/diagnostics/tests/controlStructures/nonExhaustiveIfInElvis_before.kt`** -> AI Confidence: **99.29%**
1083. **`compiler/testData/diagnostics/tests/controlStructures/specialConstructsAndPlatformTypes.fir.kt`** -> AI Confidence: **99.29%**
1084. **`compiler/testData/diagnostics/tests/controlStructures/specialConstructsAndPlatformTypes.kt`** -> AI Confidence: **99.29%**
1085. **`compiler/testData/diagnostics/tests/controlStructures/specialConstructsWithNullableExpectedType.kt`** -> AI Confidence: **99.29%**
1086. **`compiler/testData/diagnostics/tests/controlStructures/valVarCatchParameter.kt`** -> AI Confidence: **99.29%**
1087. **`compiler/testData/diagnostics/tests/controlStructures/whenInResultOfLambda.kt`** -> AI Confidence: **99.29%**
1088. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/ContinueOuterLoop.fir.kt`** -> AI Confidence: **99.29%**
1089. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/ContinueOuterLoop.kt`** -> AI Confidence: **99.29%**
1090. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/DeepIf.fir.kt`** -> AI Confidence: **99.29%**
1091. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/DeepIf.kt`** -> AI Confidence: **99.29%**
1092. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/For.fir.kt`** -> AI Confidence: **99.29%**
1093. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/For.kt`** -> AI Confidence: **99.29%**
1094. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/ManyIfs.fir.kt`** -> AI Confidence: **99.29%**
1095. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/ManyIfs.kt`** -> AI Confidence: **99.29%**
1096. **`compiler/testData/diagnostics/tests/generics/nullability/functionalBound.fir.kt`** -> AI Confidence: **99.29%**
1097. **`compiler/testData/diagnostics/tests/generics/nullability/functionalBound.kt`** -> AI Confidence: **99.29%**
1098. **`compiler/testData/diagnostics/tests/inference/completion/postponedArgumentsAnalysis/lambdasInTryCatch.fir.kt`** -> AI Confidence: **99.29%**
1099. **`compiler/testData/diagnostics/tests/inference/completion/postponedArgumentsAnalysis/lambdasInTryCatch.kt`** -> AI Confidence: **99.29%**
1100. **`compiler/testData/diagnostics/tests/inference/extensionLambdasAndArrow.fir.kt`** -> AI Confidence: **99.29%**
1101. **`compiler/testData/diagnostics/tests/inference/extensionLambdasAndArrow.kt`** -> AI Confidence: **99.29%**
1102. **`compiler/testData/diagnostics/tests/inference/kt28598.fir.kt`** -> AI Confidence: **99.29%**
1103. **`compiler/testData/diagnostics/tests/inference/kt28598.kt`** -> AI Confidence: **99.29%**
1104. **`compiler/testData/diagnostics/tests/inference/pcla/stubTypes/memberScope.fir.kt`** -> AI Confidence: **99.29%**
1105. **`compiler/testData/diagnostics/tests/inference/pcla/stubTypes/memberScope.kt`** -> AI Confidence: **99.29%**
1106. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/baseFeatureInteractions.fir.kt`** -> AI Confidence: **99.29%**
1107. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/baseFeatureInteractions.kt`** -> AI Confidence: **99.29%**
1108. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/defaultLambdaInline.kt`** -> AI Confidence: **99.29%**
1109. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/withGuards.fir.kt`** -> AI Confidence: **99.29%**
1110. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/withGuards.kt`** -> AI Confidence: **99.29%**
1111. **`compiler/testData/diagnostics/tests/modifiers/const/binaryLogic.fir.kt`** -> AI Confidence: **99.29%**
1112. **`compiler/testData/diagnostics/tests/modifiers/const/binaryLogic.kt`** -> AI Confidence: **99.29%**
1113. **`compiler/testData/diagnostics/tests/modifiers/const/complexBooleanInStringConcat_after.fir.kt`** -> AI Confidence: **99.29%**
1114. **`compiler/testData/diagnostics/tests/modifiers/const/complexBooleanInStringConcat_after.kt`** -> AI Confidence: **99.29%**
1115. **`compiler/testData/diagnostics/tests/modifiers/const/complexBooleanInStringConcat_before.kt`** -> AI Confidence: **99.29%**
1116. **`compiler/testData/diagnostics/tests/modifiers/const/ifConstVal.kt`** -> AI Confidence: **99.29%**
1117. **`compiler/testData/diagnostics/tests/nullabilityAndSmartCasts/AssertNotNull.fir.kt`** -> AI Confidence: **99.29%**
1118. **`compiler/testData/diagnostics/tests/nullabilityAndSmartCasts/AssertNotNull.kt`** -> AI Confidence: **99.29%**
1119. **`compiler/testData/diagnostics/tests/nullabilityAndSmartCasts/senslessComparisonWithNullOnTypeParameters.kt`** -> AI Confidence: **99.29%**
1120. **`compiler/testData/diagnostics/tests/nullabilityAndSmartCasts/smartCastsAndBooleanExpressions.fir.kt`** -> AI Confidence: **99.29%**
1121. **`compiler/testData/diagnostics/tests/nullabilityAndSmartCasts/smartCastsAndBooleanExpressions.kt`** -> AI Confidence: **99.29%**
1122. **`compiler/testData/diagnostics/tests/platformTypes/nullabilityWarnings/conditions.fir.kt`** -> AI Confidence: **99.29%**
1123. **`compiler/testData/diagnostics/tests/platformTypes/nullabilityWarnings/conditions.kt`** -> AI Confidence: **99.29%**
1124. **`compiler/testData/diagnostics/tests/platformTypes/nullabilityWarnings/senselessComparisonEquals.fir.kt`** -> AI Confidence: **99.29%**
1125. **`compiler/testData/diagnostics/tests/platformTypes/nullabilityWarnings/senselessComparisonEquals.kt`** -> AI Confidence: **99.29%**
1126. **`compiler/testData/diagnostics/tests/platformTypes/nullabilityWarnings/senselessComparisonIdentityEquals.fir.kt`** -> AI Confidence: **99.29%**
1127. **`compiler/testData/diagnostics/tests/platformTypes/nullabilityWarnings/senselessComparisonIdentityEquals.kt`** -> AI Confidence: **99.29%**
1128. **`compiler/testData/diagnostics/tests/regressions/AssignmentsUnderOperators.kt`** -> AI Confidence: **99.29%**
1129. **`compiler/testData/diagnostics/tests/regressions/kt353.fir.kt`** -> AI Confidence: **99.29%**
1130. **`compiler/testData/diagnostics/tests/regressions/kt353.kt`** -> AI Confidence: **99.29%**
1131. **`compiler/testData/diagnostics/tests/script/scriptScopes.kts`** -> AI Confidence: **99.29%**
1132. **`compiler/testData/diagnostics/tests/smartCasts/comparisonUnderAnd.fir.kt`** -> AI Confidence: **99.29%**
1133. **`compiler/testData/diagnostics/tests/smartCasts/comparisonUnderAnd.kt`** -> AI Confidence: **99.29%**
1134. **`compiler/testData/diagnostics/tests/smartCasts/complexComparison.fir.kt`** -> AI Confidence: **99.29%**
1135. **`compiler/testData/diagnostics/tests/smartCasts/complexComparison.kt`** -> AI Confidence: **99.29%**
1136. **`compiler/testData/diagnostics/tests/smartCasts/complexConditionsWithExcl.fir.kt`** -> AI Confidence: **99.29%**
1137. **`compiler/testData/diagnostics/tests/smartCasts/complexConditionsWithExcl.kt`** -> AI Confidence: **99.29%**
1138. **`compiler/testData/diagnostics/tests/smartCasts/exclUnderAnd.fir.kt`** -> AI Confidence: **99.29%**
1139. **`compiler/testData/diagnostics/tests/smartCasts/exclUnderAnd.kt`** -> AI Confidence: **99.29%**
1140. **`compiler/testData/diagnostics/tests/smartCasts/loops/WhileTrueWithBreakInIfCondition.fir.kt`** -> AI Confidence: **99.29%**
1141. **`compiler/testData/diagnostics/tests/smartCasts/loops/WhileTrueWithBreakInIfCondition.kt`** -> AI Confidence: **99.29%**
1142. **`compiler/testData/diagnostics/tests/smartCasts/smartCastWithAndTrue.fir.kt`** -> AI Confidence: **99.29%**
1143. **`compiler/testData/diagnostics/tests/smartCasts/smartCastWithAndTrue.kt`** -> AI Confidence: **99.29%**
1144. **`compiler/testData/diagnostics/tests/smartCasts/smartCastWithOrFalse.fir.kt`** -> AI Confidence: **99.29%**
1145. **`compiler/testData/diagnostics/tests/smartCasts/smartCastWithOrFalse.kt`** -> AI Confidence: **99.29%**
1146. **`compiler/testData/diagnostics/tests/smartCasts/smartCastWithOrFalse_InferMoreImplicationsFromBooleanExpressions.fir.kt`** -> AI Confidence: **99.29%**
1147. **`compiler/testData/diagnostics/tests/smartCasts/smartCastWithOrFalse_InferMoreImplicationsFromBooleanExpressions.kt`** -> AI Confidence: **99.29%**
1148. **`compiler/testData/diagnostics/tests/smartCasts/unstableToStable.kt`** -> AI Confidence: **99.29%**
1149. **`compiler/testData/diagnostics/tests/smartCasts/variables/aliasing.fir.kt`** -> AI Confidence: **99.29%**
1150. **`compiler/testData/diagnostics/tests/smartCasts/variables/aliasing.kt`** -> AI Confidence: **99.29%**
1151. **`compiler/testData/diagnostics/tests/smartCasts/variables/reassignment.fir.kt`** -> AI Confidence: **99.29%**
1152. **`compiler/testData/diagnostics/tests/smartCasts/variables/reassignment.kt`** -> AI Confidence: **99.29%**
1153. **`compiler/testData/diagnostics/tests/smartCasts/varnotnull/boundInitializer.fir.kt`** -> AI Confidence: **99.29%**
1154. **`compiler/testData/diagnostics/tests/smartCasts/varnotnull/boundInitializer.kt`** -> AI Confidence: **99.29%**
1155. **`compiler/testData/diagnostics/tests/suppress/oneWarning/onBlockStatement.fir.kt`** -> AI Confidence: **99.29%**
1156. **`compiler/testData/diagnostics/tests/suppress/oneWarning/onBlockStatement.kt`** -> AI Confidence: **99.29%**
1157. **`compiler/testData/diagnostics/tests/tailRecInTry.kt`** -> AI Confidence: **99.29%**
1158. **`compiler/testData/diagnostics/tests/unsignedTypes/forbiddenEqualsOnUnsignedTypes.fir.kt`** -> AI Confidence: **99.29%**
1159. **`compiler/testData/diagnostics/tests/unsignedTypes/forbiddenEqualsOnUnsignedTypes.kt`** -> AI Confidence: **99.29%**
1160. **`compiler/testData/diagnostics/tests/when/ExhaustiveSelftype.fir.kt`** -> AI Confidence: **99.29%**
1161. **`compiler/testData/diagnostics/tests/when/ExhaustiveSelftype.kt`** -> AI Confidence: **99.29%**
1162. **`compiler/testData/diagnostics/tests/when/ReservedExhaustiveWhen.fir.kt`** -> AI Confidence: **99.29%**
1163. **`compiler/testData/diagnostics/tests/when/ReservedExhaustiveWhen.kt`** -> AI Confidence: **99.29%**
1164. **`compiler/testData/diagnostics/tests/when/guard/diverseBooleanExpression.fir.kt`** -> AI Confidence: **99.29%**
1165. **`compiler/testData/diagnostics/tests/when/guard/diverseBooleanExpression.kt`** -> AI Confidence: **99.29%**
1166. **`compiler/testData/diagnostics/tests/when/guard/earlyJumps.fir.kt`** -> AI Confidence: **99.29%**
1167. **`compiler/testData/diagnostics/tests/when/guard/earlyJumps.kt`** -> AI Confidence: **99.29%**
1168. **`compiler/testData/diagnostics/tests/when/guard/elvisOperator.fir.kt`** -> AI Confidence: **99.29%**
1169. **`compiler/testData/diagnostics/tests/when/guard/elvisOperator.kt`** -> AI Confidence: **99.29%**
1170. **`compiler/testData/diagnostics/tests/when/guard/ifElseExpressions.fir.kt`** -> AI Confidence: **99.29%**
1171. **`compiler/testData/diagnostics/tests/when/guard/ifElseExpressions.kt`** -> AI Confidence: **99.29%**
1172. **`compiler/testData/diagnostics/tests/when/guard/lambda.fir.kt`** -> AI Confidence: **99.29%**
1173. **`compiler/testData/diagnostics/tests/when/guard/lambda.kt`** -> AI Confidence: **99.29%**
1174. **`compiler/testData/diagnostics/tests/when/guard/whenWithGuardSyntax.fir.kt`** -> AI Confidence: **99.29%**
1175. **`compiler/testData/diagnostics/tests/when/guard/whenWithGuardSyntax.kt`** -> AI Confidence: **99.29%**
1176. **`compiler/testData/diagnostics/tests/when/kt9929.fir.kt`** -> AI Confidence: **99.29%**
1177. **`compiler/testData/diagnostics/tests/when/kt9929.kt`** -> AI Confidence: **99.29%**
1178. **`compiler/testData/diagnostics/tests/when/whenAndLambdaWithExpectedType.fir.kt`** -> AI Confidence: **99.29%**
1179. **`compiler/testData/diagnostics/tests/when/whenAndLambdaWithExpectedType.kt`** -> AI Confidence: **99.29%**
1180. **`compiler/testData/diagnostics/tests/when/whenWithNothingAndLambdas.kt`** -> AI Confidence: **99.29%**
1181. **`compiler/testData/diagnostics/tests/when/withSubjectVariable/jumpoutInInitializer.fir.kt`** -> AI Confidence: **99.29%**
1182. **`compiler/testData/diagnostics/tests/when/withSubjectVariable/jumpoutInInitializer.kt`** -> AI Confidence: **99.29%**
1183. **`compiler/testData/diagnostics/tests/whileConditionExpectedType.fir.kt`** -> AI Confidence: **99.29%**
1184. **`compiler/testData/diagnostics/tests/whileConditionExpectedType.kt`** -> AI Confidence: **99.29%**
1185. **`compiler/testData/integration/smoke/scriptDashedArgs/script.kts`** -> AI Confidence: **99.29%**
1186. **`compiler/testData/integration/smoke/simpleScript/script.kts`** -> AI Confidence: **99.29%**
1187. **`compiler/testData/ir/interpreter/exceptions/arithmeticExceptionThrow.kt`** -> AI Confidence: **99.29%**
1188. **`compiler/testData/ir/interpreter/exceptions/divideByZero.kt`** -> AI Confidence: **99.29%**
1189. **`compiler/testData/ir/irText/declarations/catchParameterInTopLevelProperty.kt`** -> AI Confidence: **99.29%**
1190. **`compiler/testData/ir/irText/expressions/breakContinue.kt`** -> AI Confidence: **99.29%**
1191. **`compiler/testData/ir/irText/expressions/breakContinueInLoopHeader.kt`** -> AI Confidence: **99.29%**
1192. **`compiler/testData/ir/irText/expressions/forWithBreakContinue.kt`** -> AI Confidence: **99.29%**
1193. **`compiler/testData/ir/irText/expressions/ifWithArrayOperation.kt`** -> AI Confidence: **99.29%**
1194. **`compiler/testData/ir/irText/expressions/ifWithAssignment.kt`** -> AI Confidence: **99.29%**
1195. **`compiler/testData/ir/irText/expressions/ifWithLoop.kt`** -> AI Confidence: **99.29%**
1196. **`compiler/testData/ir/irText/expressions/kt30796.kt`** -> AI Confidence: **99.29%**
1197. **`compiler/testData/ir/irText/expressions/kt48806.kt`** -> AI Confidence: **99.29%**
1198. **`compiler/testData/ir/irText/expressions/whenUnusedExpression.kt`** -> AI Confidence: **99.29%**
1199. **`compiler/testData/ir/irText/expressions/whileDoWhile.kt`** -> AI Confidence: **99.29%**
1200. **`compiler/testData/ir/irText/firProblems/emptyWhen.kt`** -> AI Confidence: **99.29%**
1201. **`compiler/testData/ir/irText/firProblems/typeOfNonExhaustiveWhen.kt`** -> AI Confidence: **99.29%**
1202. **`compiler/testData/ir/sourceRanges/kt63779.kt`** -> AI Confidence: **99.29%**
1203. **`compiler/testData/ir/sourceRanges/kt63779_3.kt`** -> AI Confidence: **99.29%**
1204. **`compiler/util-klib/src/org/jetbrains/kotlin/library/encodings/WobblyTF8.kt`** -> AI Confidence: **99.29%**
1205. **`core/descriptors/src/org/jetbrains/kotlin/types/error/ErrorTypeKind.kt`** -> AI Confidence: **99.29%**
1206. **`js/js.translator/testData/box/coercion/unitNullCheck.kt`** -> AI Confidence: **99.29%**
1207. **`js/js.translator/testData/box/expression/evaluationOrder/andAndWithBreakContinueReturn.kt`** -> AI Confidence: **99.29%**
1208. **`js/js.translator/testData/box/expression/evaluationOrder/andAndWithSideEffect.kt`** -> AI Confidence: **99.29%**
1209. **`js/js.translator/testData/box/expression/evaluationOrder/compareToIntrinsicWithSideEffect.kt`** -> AI Confidence: **99.29%**
1210. **`js/js.translator/testData/box/expression/evaluationOrder/elvisWithBreakContinueReturn.kt`** -> AI Confidence: **99.29%**
1211. **`js/js.translator/testData/box/expression/evaluationOrder/equalsIntrinsicWithSideEffect.kt`** -> AI Confidence: **99.29%**
1212. **`js/js.translator/testData/box/expression/evaluationOrder/ifWithComplex.kt`** -> AI Confidence: **99.29%**
1213. **`js/js.translator/testData/box/expression/evaluationOrder/intrinsicWithBreakContinueReturn.kt`** -> AI Confidence: **99.29%**
1214. **`js/js.translator/testData/box/expression/evaluationOrder/orOrWithBreakContinueReturn.kt`** -> AI Confidence: **99.29%**
1215. **`js/js.translator/testData/box/expression/evaluationOrder/orOrWithSideEffect.kt`** -> AI Confidence: **99.29%**
1216. **`js/js.translator/testData/box/expression/evaluationOrder/whenWithComplexConditions.kt`** -> AI Confidence: **99.29%**
1217. **`js/js.translator/testData/box/expression/for/forIteratesOverLiteralRange.kt`** -> AI Confidence: **99.29%**
1218. **`js/js.translator/testData/box/expression/for/labeledForWithWhile.kt`** -> AI Confidence: **99.29%**
1219. **`js/js.translator/testData/box/expression/try/tryCatchExpr.kt`** -> AI Confidence: **99.29%**
1220. **`js/js.translator/testData/box/expression/try/tryCatchExpressionWithMessage.kt`** -> AI Confidence: **99.29%**
1221. **`js/js.translator/testData/box/expression/when/constantsInWhen.kt`** -> AI Confidence: **99.29%**
1222. **`js/js.translator/testData/box/expression/while/doWhileWithComplexCondition.kt`** -> AI Confidence: **99.29%**
1223. **`js/js.translator/testData/box/expression/while/doWhileWithComplexConditionAndContinue.kt`** -> AI Confidence: **99.29%**
1224. **`js/js.translator/testData/box/expression/while/whileWithComplexCondition.kt`** -> AI Confidence: **99.29%**
1225. **`js/js.translator/testData/box/expression/while/whileWithComplexConditionAndContinue.kt`** -> AI Confidence: **99.29%**
1226. **`js/js.translator/testData/lineNumbers/doWhileWithComplexCondition.kt`** -> AI Confidence: **99.29%**
1227. **`js/js.translator/testData/lineNumbers/for.kt`** -> AI Confidence: **99.29%**
1228. **`js/js.translator/testData/lineNumbers/whileWithComplexCondition.kt`** -> AI Confidence: **99.29%**
1229. **`kotlin-native/backend.native/tests/samples/settings.gradle.kts`** -> AI Confidence: **99.29%**
1230. **`kotlin-native/performance/settings.gradle.kts`** -> AI Confidence: **99.29%**
1231. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/internal/FloatingPointParser.kt`** -> AI Confidence: **99.29%**
1232. **`libraries/stdlib/js/src/generated/_WhitespaceChars.kt`** -> AI Confidence: **99.29%**
1233. **`libraries/stdlib/native-wasm/src/generated/_WhitespaceChars.kt`** -> AI Confidence: **99.29%**
1234. **`libraries/stdlib/native-wasm/src/kotlin/text/regex/Pattern.kt`** -> AI Confidence: **99.29%**
1235. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/e_fmod.kt`** -> AI Confidence: **99.29%**
1236. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/e_fmodf.kt`** -> AI Confidence: **99.29%**
1237. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/e_pow.kt`** -> AI Confidence: **99.29%**
1238. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/k_rem_pio2.kt`** -> AI Confidence: **99.29%**
1239. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/s_nextafter.kt`** -> AI Confidence: **99.29%**
1240. **`libraries/stdlib/wasm/src/kotlin/text/FloatingPointConverter.kt`** -> AI Confidence: **99.29%**
1241. **`libraries/tools/abi-validation/abi-tools-api/build.gradle.kts`** -> AI Confidence: **99.29%**
1242. **`libraries/tools/abi-validation/kgp-integration-tests/build.gradle.kts`** -> AI Confidence: **99.29%**
1243. **`libraries/tools/binary-compatibility-validator/build.gradle.kts`** -> AI Confidence: **99.29%**
1244. **`libraries/tools/gradle/documentation/build.gradle.kts`** -> AI Confidence: **99.29%**
1245. **`libraries/tools/gradle/regression-benchmark-templates/build.gradle.kts`** -> AI Confidence: **99.29%**
1246. **`libraries/tools/kotlin-gradle-compiler-types/build.gradle.kts`** -> AI Confidence: **99.29%**
1247. **`libraries/tools/kotlin-gradle-plugin-annotations/build.gradle.kts`** -> AI Confidence: **99.29%**
1248. **`libraries/tools/kotlin-gradle-plugin-idea-for-compatibility-tests/build.gradle.kts`** -> AI Confidence: **99.29%**
1249. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/cinteropImport/settings.gradle.kts`** -> AI Confidence: **99.29%**
1250. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/common-klib-lib-and-app/build.gradle.kts`** -> AI Confidence: **99.29%**
1251. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/commonize-kt-50847-cinterop-missing-in-supported-target/build.gradle.kts`** -> AI Confidence: **99.29%**
1252. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-dependant-pods/build.gradle.kts`** -> AI Confidence: **99.29%**
1253. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/new-mpp-lib-and-app/sample-lib-gradle-kotlin-dsl/build.gradle.kts`** -> AI Confidence: **99.29%**
1254. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/transitive-sources-dependencies/settings.gradle.kts`** -> AI Confidence: **99.29%**
1255. **`libraries/tools/kotlin-gradle-plugin-tcs-android/build.gradle.kts`** -> AI Confidence: **99.29%**
1256. **`libraries/tools/kotlin-gradle-plugin-test-utils-embeddable/build.gradle.kts`** -> AI Confidence: **99.29%**
1257. **`libraries/tools/kotlin-stdlib-docs/settings.gradle.kts`** -> AI Confidence: **99.29%**
1258. **`libraries/tools/kotlin-tooling-core/build.gradle.kts`** -> AI Confidence: **99.29%**
1259. **`libraries/tools/kotlin-tooling-metadata/build.gradle.kts`** -> AI Confidence: **99.29%**
1260. **`native/native.tests/testData/lldb/kt33364.kt`** -> AI Confidence: **99.29%**
1261. **`native/swift/sir/src/org/jetbrains/kotlin/sir/util/MiscValidation.kt`** -> AI Confidence: **99.29%**
1262. **`native/swift/sir/src/org/jetbrains/kotlin/sir/util/SirExtensions.kt`** -> AI Confidence: **99.29%**
1263. **`native/utils/build.gradle.kts`** -> AI Confidence: **99.29%**
1264. **`plugins/scripting/scripting-compiler/testData/compiler/explain/explainWithDeadNonExhaustiveIf.kts`** -> AI Confidence: **99.29%**
1265. **`plugins/scripting/scripting-compiler/testData/compiler/explain/explainWithDeadNonExhaustiveIf2.kts`** -> AI Confidence: **99.29%**
1266. **`plugins/scripting/scripting-compiler/testData/compiler/explain/explainWithExhaustiveIf.kts`** -> AI Confidence: **99.29%**
1267. **`plugins/scripting/scripting-compiler/testData/compiler/explain/explainWithLoops.kts`** -> AI Confidence: **99.29%**
1268. **`plugins/scripting/scripting-compiler/testData/compiler/explain/explainWithNonExhaustiveIf.kts`** -> AI Confidence: **99.29%**
1269. **`plugins/scripting/scripting-compiler/testData/compiler/explain/explainWithReducedList.kts`** -> AI Confidence: **99.29%**
1270. **`plugins/scripting/scripting-compiler/testData/compiler/explain/forLoop.kts`** -> AI Confidence: **99.29%**
1271. **`plugins/scripting/scripting-compiler/testData/integration/exceptionWithCause.kts`** -> AI Confidence: **99.29%**
1272. **`plugins/scripting/scripting-tests/testData/diagnostics/repl/unsafe_cast_in_loop.kts`** -> AI Confidence: **99.29%**
1273. **`repo/gradle-build-conventions/project-tests-convention/src/main/kotlin/test-inputs-check.gradle.kts`** -> AI Confidence: **99.29%**
1274. **`repo/gradle-build-conventions/test-data-manager-convention/src/main/kotlin/test-data-manager.gradle.kts`** -> AI Confidence: **99.29%**
1275. **`repo/gradle-build-conventions/utilities/src/main/kotlin/BuildPropertiesExt.kt`** -> AI Confidence: **99.29%**
1276. **`repo/gradle-settings-conventions/develocity/src/main/kotlin/develocity.settings.gradle.kts`** -> AI Confidence: **99.29%**
1277. **`repo/gradle-settings-conventions/settings.gradle.kts`** -> AI Confidence: **99.29%**
1278. **`compiler/testData/asJava/lightClasses/lightClassByFqName/AnnotationClass.descriptors.java`** -> AI Confidence: **99.29%**
1279. **`compiler/testData/asJava/lightClasses/lightClassByFqName/AnnotationClass.java`** -> AI Confidence: **99.29%**
1280. **`compiler/testData/asJava/lightClasses/lightClassByFqName/compilationErrors/localClassApproximation.java`** -> AI Confidence: **99.29%**
1281. **`compiler/testData/diagnostics/nativeTests/specialBackendChecks/runtests.sh`** -> AI Confidence: **99.29%**
1282. **`kotlin-native/backend.native/tests/samples/gradlew`** -> AI Confidence: **99.29%**
1283. **`kotlin-native/backend.native/tests/samples/tensorflow/downloadTensorflow.sh`** -> AI Confidence: **99.29%**
1284. **`kotlin-native/tools/libffi/build_for_macos.sh`** -> AI Confidence: **99.29%**
1285. **`kotlin-native/tools/scripts/update_apple_frameworks.sh`** -> AI Confidence: **99.29%**
1286. **`libraries/tools/kotlin-maven-plugin-test/src/test/resources/maven-wrapper/mvnw`** -> AI Confidence: **99.29%**
1287. **`libraries/tools/kotlin-stdlib-docs-legacy/gradlew`** -> AI Confidence: **99.29%**
1288. **`libraries/tools/kotlin-stdlib-docs/gradlew`** -> AI Confidence: **99.29%**
1289. **`scripts/update-verification-metadata.sh`** -> AI Confidence: **99.29%**
1290. **`js/js.translator/testData/box/jsAstOptimizations/logicalOperators.js`** -> AI Confidence: **99.29%**
1291. **`js/js.translator/testData/js-name-resolution/labels.expected.js`** -> AI Confidence: **99.29%**
1292. **`js/js.translator/testData/js-name-resolution/labels.original.js`** -> AI Confidence: **99.29%**
1293. **`js/js.translator/testData/js-optimizer/empty-statement-elimination/emptyBlockEliminated.original.js`** -> AI Confidence: **99.29%**
1294. **`js/js.translator/testData/js-optimizer/empty-statement-elimination/switchElimination.optimized.js`** -> AI Confidence: **99.29%**
1295. **`js/js.translator/testData/js-optimizer/empty-statement-elimination/switchElimination.original.js`** -> AI Confidence: **99.29%**
1296. **`kotlin-native/gradle/kotlinGradlePlugin.gradle`** -> AI Confidence: **99.29%**
1297. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/compilerPlugins/incrementalChangeInPlugin/plugin/build.gradle`** -> AI Confidence: **99.29%**
1298. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/differentClassloaders/jvm-app/build.gradle`** -> AI Confidence: **99.29%**
1299. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kt-27059-pom-rewriting/js-app/build.gradle`** -> AI Confidence: **99.29%**
1300. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kt-27059-pom-rewriting/jvm-app/build.gradle`** -> AI Confidence: **99.29%**
1301. **`libraries/tools/kotlin-stdlib-docs-legacy/ant/build.gradle`** -> AI Confidence: **99.29%**
1302. **`libraries/tools/kotlin-stdlib-docs-legacy/kotlin_native/build.gradle`** -> AI Confidence: **99.29%**
1303. **`libraries/tools/kotlin-stdlib-docs/plugins/dokka-version-filter-plugin/build.gradle`** -> AI Confidence: **99.29%**
1304. **`settings.gradle`** -> AI Confidence: **99.29%**
1305. **`js/js.translator/testData/typescript-export/wasm/jsPrimitives/jsPrimitives__main.ts`** -> AI Confidence: **99.29%**
1306. **`js/js.translator/testData/typescript-export/wasm/nullableJsPrimitives/nullableJsPrimitives__main.ts`** -> AI Confidence: **99.29%**
1307. **`js/js.translator/testData/typescript-export/wasm/nullablePrimitives/nullablePrimitives__main.ts`** -> AI Confidence: **99.29%**
1308. **`js/js.translator/testData/typescript-export/wasm/nullableUnsigned/nullableUnsinged__main.ts`** -> AI Confidence: **99.29%**
1309. **`js/js.translator/testData/typescript-export/wasm/primitives/primitives__main.ts`** -> AI Confidence: **99.29%**
1310. **`js/js.translator/testData/typescript-export/wasm/unsigned/unsinged__main.ts`** -> AI Confidence: **99.29%**
1311. **`kotlin-native/performance/numerical/src/nativeInterop/cinterop/pi.c`** -> AI Confidence: **99.29%**
1312. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/cinterop-lib/src/mylib.h`** -> AI Confidence: **99.29%**
1313. **`native/native.tests/testData/CInterop/KT-55578/userSetupHint.h`** -> AI Confidence: **99.29%**
1314. **`kotlin-native/performance/cinterop/src/nativeInterop/cinterop/types.def`** -> AI Confidence: **99.29%**
1315. **`kotlin-native/performance/objcinterop/src/nativeInterop/cinterop/complexNumbers.m`** -> AI Confidence: **99.29%**
1316. **`kotlin-native/runtime/src/main/cpp/ObjCExportExceptionDetails.mm`** -> AI Confidence: **99.29%**
1317. **`kotlin-native/runtime/src/main/cpp/WritableTypeInfo.mm`** -> AI Confidence: **99.29%**
1318. **`kotlin-native/runtime/src/main/cpp/objc_support/NSNotificationSubscription.mm`** -> AI Confidence: **99.29%**
1319. **`kotlin-native/runtime/src/main/cpp/objc_support/ObjectPtr.mm`** -> AI Confidence: **99.29%**
1320. **`kotlin-native/runtime/src/test_support/cpp/CompilerGeneratedObjC.mm`** -> AI Confidence: **99.29%**
1321. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-multiple/pod_dependency/src/foo.m`** -> AI Confidence: **99.29%**
1322. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-multiple/subspec_dependency/src/baz.m`** -> AI Confidence: **99.29%**
1323. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-single/subspec_dependency/src/baz.m`** -> AI Confidence: **99.29%**
1324. **`native/executors/src/main/resources/xcode-project/test-ios-launch/test-ios-launch/main.m`** -> AI Confidence: **99.29%**
1325. **`native/native.tests/testData/CInterop/KT-39120/pod1.framework/Headers/pod1-umbrella.h`** -> AI Confidence: **99.29%**
1326. **`native/native.tests/testData/CInterop/KT-39120/pod2.framework/Headers/pod2-umbrella.h`** -> AI Confidence: **99.29%**
1327. **`native/native.tests/testData/framework/gh3343/gh3343.h`** -> AI Confidence: **99.29%**
1328. **`native/native.tests/testData/interop/objc/tests/weakRefs.h`** -> AI Confidence: **99.29%**
1329. **`kotlin-native/runtime/src/libbacktrace/c/include/config.h`** -> AI Confidence: **99.29%**
1330. **`kotlin-native/runtime/src/libbacktrace/c/include/filenames.h`** -> AI Confidence: **99.29%**
1331. **`kotlin-native/runtime/src/main/cpp/dtoa/cbigint.cpp`** -> AI Confidence: **99.29%**
1332. **`kotlin-native/runtime/src/main/cpp/polyhash/PolyHashTest.cpp`** -> AI Confidence: **99.29%**
1333. **`native/native.tests/testData/CExport/InterfaceV1/unhandledException/main.cpp`** -> AI Confidence: **99.29%**
1334. **`native/native.tests/testData/framework/objcexport/functionalTypes.swift`** -> AI Confidence: **99.29%**
1335. **`native/native.tests/testData/framework/objcexport/kotlinPrivateOverride.swift`** -> AI Confidence: **99.29%**
1336. **`native/native.tests/testData/framework/values_generics/values_generics.swift`** -> AI Confidence: **99.29%**
1337. **`native/swift/swift-export-standalone-integration-tests/simple/testData/execution/properties/properties.swift`** -> AI Confidence: **99.29%**
1338. **`native/swift/swift-export-standalone-integration-tests/simple/testData/execution/smokes/smoke0.swift`** -> AI Confidence: **99.29%**
1339. **`kotlin-native/tools/qemu/Dockerfile`** -> AI Confidence: **99.29%**
1340. **`kotlin-native/tools/toolchain_builder/Dockerfile`** -> AI Confidence: **99.29%**
1341. **`scripts/kotlin-build-env.dockerfile`** -> AI Confidence: **99.29%**
1342. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-dependant-pods/pod1/pod1.podspec`** -> AI Confidence: **99.29%**
1343. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-dependant-pods/pod2/pod2.podspec`** -> AI Confidence: **99.29%**
1344. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-dependant-pods/pod3/pod3.podspec`** -> AI Confidence: **99.29%**
1345. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-dependant-pods/pod4/pod4.podspec`** -> AI Confidence: **99.29%**
1346. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-multiple/pod_dependency/pod_dependency.podspec`** -> AI Confidence: **99.29%**
1347. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-multiple/subspec_dependency/subspec_dependency.podspec`** -> AI Confidence: **99.29%**
1348. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-outdated-repo/cocoapodsLibrary/0.1.0/cocoapodsLibrary.podspec`** -> AI Confidence: **99.29%**
1349. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-outdated-repo/cocoapodsLibrary/0.2.0/cocoapodsLibrary.podspec`** -> AI Confidence: **99.29%**
1350. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-outdated-repo/ios-app/Podfile`** -> AI Confidence: **99.29%**
1351. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-single/ios-app/Podfile`** -> AI Confidence: **99.29%**
1352. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-single/pod_dependency/pod_dependency.podspec`** -> AI Confidence: **99.29%**
1353. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-single/subspec_dependency/subspec_dependency.podspec`** -> AI Confidence: **99.29%**
1354. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-template/ios-app/Podfile`** -> AI Confidence: **99.29%**
1355. **`kotlin-native/runtime/src/main/cpp/ObjCExportCollections.h`** -> AI Confidence: **99.28%**
1356. **`kotlin-native/runtime/src/main/cpp/ObjCExportPrivate.h`** -> AI Confidence: **99.28%**
1357. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/commonizeSQLiteAndCurlInterop/libs/include/curl/system.h`** -> AI Confidence: **99.28%**
1358. **`kotlin-native/runtime/src/main/cpp/ObjCInteropUtilsPrivate.h`** -> AI Confidence: **99.26%**
1359. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/annotations/KaFe10AnnotationsList.kt`** -> AI Confidence: **99.24%**
1360. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10DataFlowProvider.kt`** -> AI Confidence: **99.24%**
1361. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolDeclarationOverridesProvider.kt`** -> AI Confidence: **99.24%**
1362. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolProvider.kt`** -> AI Confidence: **99.24%**
1363. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolRelationProvider.kt`** -> AI Confidence: **99.24%**
1364. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/typeCreation/KaFe10TypeCreator.kt`** -> AI Confidence: **99.24%**
1365. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/KaFe10TypeSystemCommonBackendContextForTypeMapping.kt`** -> AI Confidence: **99.24%**
1366. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10SimpleNameReference.kt`** -> AI Confidence: **99.24%**
1367. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompilerFacility.kt`** -> AI Confidence: **99.24%**
1368. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirReferenceShortener.kt`** -> AI Confidence: **99.24%**
1369. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSubstitutorProvider.kt`** -> AI Confidence: **99.24%**
1370. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSymbolDeclarationOverridesProvider.kt`** -> AI Confidence: **99.24%**
1371. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirVisibilityChecker.kt`** -> AI Confidence: **99.24%**
1372. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirSimpleNameReference.kt`** -> AI Confidence: **99.24%**
1373. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPsiSymbol.kt`** -> AI Confidence: **99.24%**
1374. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirValueParameterSymbol.kt`** -> AI Confidence: **99.24%**
1375. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/ConeTypePointer.kt`** -> AI Confidence: **99.24%**
1376. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/KaFirCacheCleaner.kt`** -> AI Confidence: **99.24%**
1377. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/firUtils.kt`** -> AI Confidence: **99.24%**
1378. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseKDocProvider.kt`** -> AI Confidence: **99.24%**
1379. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/projectStructure/KaDanglingFileModuleImpl.kt`** -> AI Confidence: **99.24%**
1380. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/projectStructure/KotlinProjectStructureProviderBase.kt`** -> AI Confidence: **99.24%**
1381. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneAnnotationsResolver.kt`** -> AI Confidence: **99.24%**
1382. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/packages/KotlinStandalonePackageProvider.kt`** -> AI Confidence: **99.24%**
1383. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/projectStructure/danglingFiles.kt`** -> AI Confidence: **99.24%**
1384. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaDebugSymbolRenderer.kt`** -> AI Confidence: **99.24%**
1385. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/ClsClassFinder.kt`** -> AI Confidence: **99.24%**
1386. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/ClsKotlinBinaryClassCache.kt`** -> AI Confidence: **99.24%**
1387. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/ClassClsStubBuilder.kt`** -> AI Confidence: **99.24%**
1388. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/clsStubBuilding.kt`** -> AI Confidence: **99.24%**
1389. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/SyntheticPropertyAccessorReference.kt`** -> AI Confidence: **99.24%**
1390. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/finder/JavaElementFinder.kt`** -> AI Confidence: **99.24%**
1391. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/FirDesignation.kt`** -> AI Confidence: **99.24%**
1392. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/compile/CodeFragmentCapturedValueAnalyzer.kt`** -> AI Confidence: **99.24%**
1393. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/compile/CompilationPeerCollector.kt`** -> AI Confidence: **99.24%**
1394. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/LLFirDeclarationModificationService.kt`** -> AI Confidence: **99.24%**
1395. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/LLFirModuleLazyDeclarationResolver.kt`** -> AI Confidence: **99.24%**
1396. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/RawFirNonLocalDeclarationBuilder.kt`** -> AI Confidence: **99.24%**
1397. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/FirCallableSignature.kt`** -> AI Confidence: **99.24%**
1398. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/services/LLFirJavaAnnotationProvider.kt`** -> AI Confidence: **99.24%**
1399. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/structure/LLSessionStatisticsCalculator.kt`** -> AI Confidence: **99.24%**
1400. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedClassDeserialization.kt`** -> AI Confidence: **99.24%**
1401. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedFirTypeDeserializer.kt`** -> AI Confidence: **99.24%**
1402. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLDanglingFileDependenciesSymbolProvider.kt`** -> AI Confidence: **99.24%**
1403. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirContractsLazyResolver.kt`** -> AI Confidence: **99.24%**
1404. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/ContextCollector.kt`** -> AI Confidence: **99.24%**
1405. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/FirDeclarationForCompiledElementSearcher.kt`** -> AI Confidence: **99.24%**
1406. **`analysis/stubs/testFixtures/org/jetbrains/kotlin/analysis/stubs/additionalStubInfoExtractor.kt`** -> AI Confidence: **99.24%**
1407. **`build-common/src/org/jetbrains/kotlin/incremental/buildUtil.kt`** -> AI Confidence: **99.24%**
1408. **`compiler/android-tests/tests/org/jetbrains/kotlin/android/tests/CodegenTestsOnAndroidGenerator.kt`** -> AI Confidence: **99.24%**
1409. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/CommonKlibBasedCompilerArguments.kt`** -> AI Confidence: **99.24%**
1410. **`compiler/backend/src/org/jetbrains/kotlin/codegen/TransformationMethodVisitor.kt`** -> AI Confidence: **99.24%**
1411. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/RedundantLocalsEliminationMethodTransformer.kt`** -> AI Confidence: **99.24%**
1412. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/resumePointDependentAnalysis.kt`** -> AI Confidence: **99.24%**
1413. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/AnonymousObjectTransformer.kt`** -> AI Confidence: **99.24%**
1414. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MethodInlinerUtil.kt`** -> AI Confidence: **99.24%**
1415. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/coroutines/CoroutineTransformer.kt`** -> AI Confidence: **99.24%**
1416. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/RedundantBoxingInterpreter.kt`** -> AI Confidence: **99.24%**
1417. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/AnalyzeTryCatchBlocks.kt`** -> AI Confidence: **99.24%**
1418. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/BaseCompilationTest.kt`** -> AI Confidence: **99.24%**
1419. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/AbstractModule.kt`** -> AI Confidence: **99.24%**
1420. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/arguments/argumentUtils.kt`** -> AI Confidence: **99.24%**
1421. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/arguments/parseCommandLineArguments.kt`** -> AI Confidence: **99.24%**
1422. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/moduleVisibilityImpl.kt`** -> AI Confidence: **99.24%**
1423. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/ClasspathRootsResolver.kt`** -> AI Confidence: **99.24%**
1424. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/coreEnvironmentUtils.kt`** -> AI Confidence: **99.24%**
1425. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/modules/CliJavaModuleResolver.kt`** -> AI Confidence: **99.24%**
1426. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/js/JsConfigurationUpdater.kt`** -> AI Confidence: **99.24%**
1427. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/K2JVMCompiler.kt`** -> AI Confidence: **99.24%**
1428. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/KotlinToJVMBytecodeCompiler.kt`** -> AI Confidence: **99.24%**
1429. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/cliCompilerUtils.kt`** -> AI Confidence: **99.24%**
1430. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/firFindMainClass.kt`** -> AI Confidence: **99.24%**
1431. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFrontendPipelinePhase.kt`** -> AI Confidence: **99.24%**
1432. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmScriptPipelineStep.kt`** -> AI Confidence: **99.24%**
1433. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeKlibCliPipeline.kt`** -> AI Confidence: **99.24%**
1434. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/GroupedKtSources.kt`** -> AI Confidence: **99.24%**
1435. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/output/outputUtils.kt`** -> AI Confidence: **99.24%**
1436. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/AbstractCliPipeline.kt`** -> AI Confidence: **99.24%**
1437. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/AbstractConfigurationPhase.kt`** -> AI Confidence: **99.24%**
1438. **`compiler/daemon/daemon-common/src/org/jetbrains/kotlin/daemon/common/NetworkUtils.kt`** -> AI Confidence: **99.24%**
1439. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/CompileServiceImpl.kt`** -> AI Confidence: **99.24%**
1440. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/Generator.kt`** -> AI Confidence: **99.24%**
1441. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/FirJsHelpers.kt`** -> AI Confidence: **99.24%**
1442. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/FirJsModuleCheckUtils.kt`** -> AI Confidence: **99.24%**
1443. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsBuiltinNameClashChecker.kt`** -> AI Confidence: **99.24%**
1444. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsInheritanceClassChecker.kt`** -> AI Confidence: **99.24%**
1445. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsStaticChecker.kt`** -> AI Confidence: **99.24%**
1446. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsModuleQualifiedAccessChecker.kt`** -> AI Confidence: **99.24%**
1447. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmExternalDeclarationChecker.kt`** -> AI Confidence: **99.24%**
1448. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmFieldApplicabilityChecker.kt`** -> AI Confidence: **99.24%**
1449. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmNameChecker.kt`** -> AI Confidence: **99.24%**
1450. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirPropertyHidesJavaFieldChecker.kt`** -> AI Confidence: **99.24%**
1451. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirExpressionJavaNullabilityWarningCheckers.kt`** -> AI Confidence: **99.24%**
1452. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirFieldAccessShadowedByInvisibleKotlinProperty.kt`** -> AI Confidence: **99.24%**
1453. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaSamConstructorNullabilityChecker.kt`** -> AI Confidence: **99.24%**
1454. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmInlineTargetQualifiedAccessChecker.kt`** -> AI Confidence: **99.24%**
1455. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmProtectedInSuperClassCompanionCallChecker.kt`** -> AI Confidence: **99.24%**
1456. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmSuspensionPointInsideMutexLockChecker.kt`** -> AI Confidence: **99.24%**
1457. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/firJavaValueBasedClassUtils.kt`** -> AI Confidence: **99.24%**
1458. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeForwardDeclarationReifiedChecker.kt`** -> AI Confidence: **99.24%**
1459. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCNameChecker.kt`** -> AI Confidence: **99.24%**
1460. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCRefinementAnnotationChecker.kt`** -> AI Confidence: **99.24%**
1461. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCRefinementChecker.kt`** -> AI Confidence: **99.24%**
1462. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCRefinementOverridesChecker.kt`** -> AI Confidence: **99.24%**
1463. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeThrowsChecker.kt`** -> AI Confidence: **99.24%**
1464. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeVariadicSpreadChecker.kt`** -> AI Confidence: **99.24%**
1465. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/FirWasmJsEqualityChecker.kt`** -> AI Confidence: **99.24%**
1466. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/expression/FirWasmJsCodeCallChecker.kt`** -> AI Confidence: **99.24%**
1467. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/declarations/utils/FirWebCommonHelpers.kt`** -> AI Confidence: **99.24%**
1468. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/util/PropertyInitializationInfoCollector.kt`** -> AI Confidence: **99.24%**
1469. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirAnnotationHelpers.kt`** -> AI Confidence: **99.24%**
1470. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/ModifiersCompatibilityUtils.kt`** -> AI Confidence: **99.24%**
1471. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/ProjectionRelationCheckerImpl.kt`** -> AI Confidence: **99.24%**
1472. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAmbiguousAnonymousTypeChecker.kt`** -> AI Confidence: **99.24%**
1473. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCommonConstructorDelegationIssuesChecker.kt`** -> AI Confidence: **99.24%**
1474. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirConflictsDeclarationChecker.kt`** -> AI Confidence: **99.24%**
1475. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirConstPropertyChecker.kt`** -> AI Confidence: **99.24%**
1476. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirContractChecker.kt`** -> AI Confidence: **99.24%**
1477. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCyclicTypeBoundsChecker.kt`** -> AI Confidence: **99.24%**
1478. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDataClassConsistentDataCopyAnnotationChecker.kt`** -> AI Confidence: **99.24%**
1479. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDelegateUsesExtensionPropertyTypeParameterChecker.kt`** -> AI Confidence: **99.24%**
1480. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirEnumCompanionInEnumConstructorCallChecker.kt`** -> AI Confidence: **99.24%**
1481. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExpectRefinementChecker.kt`** -> AI Confidence: **99.24%**
1482. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFiniteBoundRestrictionChecker.kt`** -> AI Confidence: **99.24%**
1483. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirImplicitNothingReturnTypeChecker.kt`** -> AI Confidence: **99.24%**
1484. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirImportsChecker.kt`** -> AI Confidence: **99.24%**
1485. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInfixFunctionDeclarationChecker.kt`** -> AI Confidence: **99.24%**
1486. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlineDeclarationChecker.kt`** -> AI Confidence: **99.24%**
1487. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlinedLambdaNonSourceAnnotationsChecker.kt`** -> AI Confidence: **99.24%**
1488. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMemberPropertiesChecker.kt`** -> AI Confidence: **99.24%**
1489. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMethodOfAnyImplementedInInterfaceChecker.kt`** -> AI Confidence: **99.24%**
1490. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNonExpansiveInheritanceRestrictionChecker.kt`** -> AI Confidence: **99.24%**
1491. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNotImplementedOverrideChecker.kt`** -> AI Confidence: **99.24%**
1492. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOpenMemberChecker.kt`** -> AI Confidence: **99.24%**
1493. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOperatorOfChecker.kt`** -> AI Confidence: **99.24%**
1494. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOuterClassArgumentsRequiredChecker.kt`** -> AI Confidence: **99.24%**
1495. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPackageConflictsWithClassifierChecker.kt`** -> AI Confidence: **99.24%**
1496. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirReifiedTypeParameterChecker.kt`** -> AI Confidence: **99.24%**
1497. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirVersionOverloadsChecker.kt`** -> AI Confidence: **99.24%**
1498. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/AbstractFirReflectionApiCallChecker.kt`** -> AI Confidence: **99.24%**
1499. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirConflictsExpressionChecker.kt`** -> AI Confidence: **99.24%**
1500. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirContextSensitiveResolutionAmbiguityChecker.kt`** -> AI Confidence: **99.24%**
1501. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirConventionFunctionCallChecker.kt`** -> AI Confidence: **99.24%**
1502. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDataClassCopyUsageWillBecomeInaccessibleChecker.kt`** -> AI Confidence: **99.24%**
1503. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirForLoopChecker.kt`** -> AI Confidence: **99.24%**
1504. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirForLoopStatementAssignmentChecker.kt`** -> AI Confidence: **99.24%**
1505. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirLateinitIntrinsicApplicabilityChecker.kt`** -> AI Confidence: **99.24%**
1506. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptInAnnotationCallChecker.kt`** -> AI Confidence: **99.24%**
1507. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptInUsageAccessChecker.kt`** -> AI Confidence: **99.24%**
1508. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirParenthesizedLhsSetOperatorChecker.kt`** -> AI Confidence: **99.24%**
1509. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirStandaloneQualifierChecker.kt`** -> AI Confidence: **99.24%**
1510. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTypeArgumentsOfQualifierOfCallableReferenceChecker.kt`** -> AI Confidence: **99.24%**
1511. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUpperBoundViolatedQualifiedAccessExpressionChecker.kt`** -> AI Confidence: **99.24%**
1512. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/CanBeValChecker.kt`** -> AI Confidence: **99.24%**
1513. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirAnnotatedBinaryExpressionChecker.kt`** -> AI Confidence: **99.24%**
1514. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirConfusingWhenBranchSyntaxChecker.kt`** -> AI Confidence: **99.24%**
1515. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirOptInUsageTypeRefChecker.kt`** -> AI Confidence: **99.24%**
1516. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirStarProjectionModifierChecker.kt`** -> AI Confidence: **99.24%**
1517. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirTypeAnnotationChecker.kt`** -> AI Confidence: **99.24%**
1518. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/TypeArgumentsInPackagesTypeRefChecker.kt`** -> AI Confidence: **99.24%**
1519. **`compiler/fir/cones/src/org/jetbrains/kotlin/fir/renderer/ConeTypeRendererForReadability.kt`** -> AI Confidence: **99.24%**
1520. **`compiler/fir/cones/src/org/jetbrains/kotlin/fir/types/ConeTypeUtils.kt`** -> AI Confidence: **99.24%**
1521. **`compiler/fir/dump/src/org/jetbrains/kotlin/fir/dump/HtmlFirDump.kt`** -> AI Confidence: **99.24%**
1522. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/IrCommonToPlatformDependencyActualizerMapContributor.kt`** -> AI Confidence: **99.24%**
1523. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/ClassDeserialization.kt`** -> AI Confidence: **99.24%**
1524. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirTypeDeserializer.kt`** -> AI Confidence: **99.24%**
1525. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/FirJavaElementFinder.kt`** -> AI Confidence: **99.24%**
1526. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/FirJavaVisibilityChecker.kt`** -> AI Confidence: **99.24%**
1527. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JavaUtils.kt`** -> AI Confidence: **99.24%**
1528. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/JvmClassFileBasedSymbolProvider.kt`** -> AI Confidence: **99.24%**
1529. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/javaAnnotationsMapping.kt`** -> AI Confidence: **99.24%**
1530. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaClassStaticUseSiteScope.kt`** -> AI Confidence: **99.24%**
1531. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaScopeUtils.kt`** -> AI Confidence: **99.24%**
1532. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/scopes/jvm/SignatureUtils.kt`** -> AI Confidence: **99.24%**
1533. **`compiler/fir/fir-native/src/org/jetbrains/kotlin/fir/backend/native/interop/FirObjCInterop.kt`** -> AI Confidence: **99.24%**
1534. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirContractSerializer.kt`** -> AI Confidence: **99.24%**
1535. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/constant/FirToConstantValueTransformer.kt`** -> AI Confidence: **99.24%**
1536. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/serializationUtil.kt`** -> AI Confidence: **99.24%**
1537. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrCallableDeclarationsGenerator.kt`** -> AI Confidence: **99.24%**
1538. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrLazyFakeOverrideGenerator.kt`** -> AI Confidence: **99.24%**
1539. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/ImplicitConversionUtils.kt`** -> AI Confidence: **99.24%**
1540. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/SymbolConversionUtils.kt`** -> AI Confidence: **99.24%**
1541. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/VariousUtils.kt`** -> AI Confidence: **99.24%**
1542. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/FirAnnotationUtils.kt`** -> AI Confidence: **99.24%**
1543. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/OperatorFunctionChecks.kt`** -> AI Confidence: **99.24%**
1544. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/declarationUtils.kt`** -> AI Confidence: **99.24%**
1545. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/deprecationUtils.kt`** -> AI Confidence: **99.24%**
1546. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/ScopeUtils.kt`** -> AI Confidence: **99.24%**
1547. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/SupertypeUtils.kt`** -> AI Confidence: **99.24%**
1548. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/TypeExpansionUtils.kt`** -> AI Confidence: **99.24%**
1549. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/calls/ImplicitValue.kt`** -> AI Confidence: **99.24%**
1550. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/AbstractFirUseSiteMemberScope.kt`** -> AI Confidence: **99.24%**
1551. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirClassDeclaredMemberScope.kt`** -> AI Confidence: **99.24%**
1552. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirClassUseSiteMemberScope.kt`** -> AI Confidence: **99.24%**
1553. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirDelegatedMemberScope.kt`** -> AI Confidence: **99.24%**
1554. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirGeneratedScopes.kt`** -> AI Confidence: **99.24%**
1555. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirScriptDeclarationsScope.kt`** -> AI Confidence: **99.24%**
1556. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirTypeIntersectionScope.kt`** -> AI Confidence: **99.24%**
1557. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirTypeIntersectionScopeContext.kt`** -> AI Confidence: **99.24%**
1558. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/ConeInferenceContext.kt`** -> AI Confidence: **99.24%**
1559. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/ConeTypeContext.kt`** -> AI Confidence: **99.24%**
1560. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/FirCorrespondingSupertypesCache.kt`** -> AI Confidence: **99.24%**
1561. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/FirFunctionTypeKindServiceImpl.kt`** -> AI Confidence: **99.24%**
1562. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/FunctionalTypeUtils.kt`** -> AI Confidence: **99.24%**
1563. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/InferenceUtils.kt`** -> AI Confidence: **99.24%**
1564. **`compiler/fir/raw-fir/psi2fir/testFixtures/org/jetbrains/kotlin/fir/builder/AbstractRawFirBuilderTestCase.kt`** -> AI Confidence: **99.24%**
1565. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/generatedDeclarationsUtils.kt`** -> AI Confidence: **99.24%**
1566. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/ContextSensitiveResolutionUtils.kt`** -> AI Confidence: **99.24%**
1567. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirSamResolver.kt`** -> AI Confidence: **99.24%**
1568. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/ArgumentUtils.kt`** -> AI Confidence: **99.24%**
1569. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/FirCallResolver.kt`** -> AI Confidence: **99.24%**
1570. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/SuperCalls.kt`** -> AI Confidence: **99.24%**
1571. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/VisibilityUtils.kt`** -> AI Confidence: **99.24%**
1572. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/Candidate.kt`** -> AI Confidence: **99.24%**
1573. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/ConeOverloadConflictResolver.kt`** -> AI Confidence: **99.24%**
1574. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/EagerLambdaResolution.kt`** -> AI Confidence: **99.24%**
1575. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/FirDeclarationOverloadabilityHelperImpl.kt`** -> AI Confidence: **99.24%**
1576. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/FirOverloadByLambdaReturnTypeResolver.kt`** -> AI Confidence: **99.24%**
1577. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/ResolutionStages.kt`** -> AI Confidence: **99.24%**
1578. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/FirInvokeResolveTowerExtension.kt`** -> AI Confidence: **99.24%**
1579. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirLocalVariableAssignmentAnalyzer.kt`** -> AI Confidence: **99.24%**
1580. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/CollectionLiteralBoundsCollector.kt`** -> AI Confidence: **99.24%**
1581. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/ConeConstraintSystemUtilContext.kt`** -> AI Confidence: **99.24%**
1582. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirCallCompleter.kt`** -> AI Confidence: **99.24%**
1583. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirDelegatedPropertyInferenceSession.kt`** -> AI Confidence: **99.24%**
1584. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirInferenceLogger.kt`** -> AI Confidence: **99.24%**
1585. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirPCLAInferenceSession.kt`** -> AI Confidence: **99.24%**
1586. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirTypeCandidateCollector.kt`** -> AI Confidence: **99.24%**
1587. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirCallCompletionResultsWriterTransformer.kt`** -> AI Confidence: **99.24%**
1588. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirSpecificTypeResolverTransformer.kt`** -> AI Confidence: **99.24%**
1589. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirTypeResolveTransformer.kt`** -> AI Confidence: **99.24%**
1590. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/BodyResolveContext.kt`** -> AI Confidence: **99.24%**
1591. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/DeclarationApproximationUtils.kt`** -> AI Confidence: **99.24%**
1592. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirControlFlowStatementsResolveTransformer.kt`** -> AI Confidence: **99.24%**
1593. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/contracts/FirAbstractContractResolveTransformerDispatcher.kt`** -> AI Confidence: **99.24%**
1594. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/mpp/FirExpectActualMatchingContextImpl.kt`** -> AI Confidence: **99.24%**
1595. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/FirEqualsOverrideHelpers.kt`** -> AI Confidence: **99.24%**
1596. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/ScopeUtils.kt`** -> AI Confidence: **99.24%**
1597. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/CallableIdUtils.kt`** -> AI Confidence: **99.24%**
1598. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/Utils.kt`** -> AI Confidence: **99.24%**
1599. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/utils/declarationAttributes.kt`** -> AI Confidence: **99.24%**
1600. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/FirExpressionUtil.kt`** -> AI Confidence: **99.24%**
1601. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/FirCallableSymbol.kt`** -> AI Confidence: **99.24%**
1602. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/FirTypeUtils.kt`** -> AI Confidence: **99.24%**
1603. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/cfg/UnreachableCode.kt`** -> AI Confidence: **99.24%**
1604. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PositioningStrategy.kt`** -> AI Confidence: **99.24%**
1605. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/fileClasses/JvmFileClassUtil.kt`** -> AI Confidence: **99.24%**
1606. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaClassImpl.kt`** -> AI Confidence: **99.24%**
1607. **`compiler/frontend.java/src/org/jetbrains/kotlin/inline/inlineUtil.kt`** -> AI Confidence: **99.24%**
1608. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/kotlin/moduleVisibilityUtils.kt`** -> AI Confidence: **99.24%**
1609. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/RuntimeAssertions.kt`** -> AI Confidence: **99.24%**
1610. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/InconsistentOperatorFromJavaCallChecker.kt`** -> AI Confidence: **99.24%**
1611. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/InlinePlatformCompatibilityChecker.kt`** -> AI Confidence: **99.24%**
1612. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/InterfaceDefaultMethodCallChecker.kt`** -> AI Confidence: **99.24%**
1613. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaOverrideWithWrongNullabilityOverrideChecker.kt`** -> AI Confidence: **99.24%**
1614. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaTypeAccessibilityChecker.kt`** -> AI Confidence: **99.24%**
1615. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmMultifileClassStateChecker.kt`** -> AI Confidence: **99.24%**
1616. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ProtectedInSuperClassCompanionCallChecker.kt`** -> AI Confidence: **99.24%**
1617. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ProtectedSyntheticExtensionCallChecker.kt`** -> AI Confidence: **99.24%**
1618. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/RepeatableAnnotationChecker.kt`** -> AI Confidence: **99.24%**
1619. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SuspendInFunInterfaceChecker.kt`** -> AI Confidence: **99.24%**
1620. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/jvmConstants.kt`** -> AI Confidence: **99.24%**
1621. **`compiler/frontend/src/org/jetbrains/kotlin/analyzer/AbstractResolverForProject.kt`** -> AI Confidence: **99.24%**
1622. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/ContextInfoToDataFlowInfo.kt`** -> AI Confidence: **99.24%**
1623. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/EffectSystem.kt`** -> AI Confidence: **99.24%**
1624. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/EffectsExtractingVisitor.kt`** -> AI Confidence: **99.24%**
1625. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/effects/PsiCallsEffectParser.kt`** -> AI Confidence: **99.24%**
1626. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/ClassicPositioningStrategies.kt`** -> AI Confidence: **99.24%**
1627. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DeclarationResolver.kt`** -> AI Confidence: **99.24%**
1628. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DelegatingBindingTrace.kt`** -> AI Confidence: **99.24%**
1629. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DelegationResolver.kt`** -> AI Confidence: **99.24%**
1630. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/LazyExplicitImportScope.kt`** -> AI Confidence: **99.24%**
1631. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/LocalVariableResolver.kt`** -> AI Confidence: **99.24%**
1632. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/NonExpansiveInheritanceRestrictionChecker.kt`** -> AI Confidence: **99.24%**
1633. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/OverrideResolver.kt`** -> AI Confidence: **99.24%**
1634. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/UpperBoundChecker.kt`** -> AI Confidence: **99.24%**
1635. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/VarianceChecker.kt`** -> AI Confidence: **99.24%**
1636. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/CandidateResolver.kt`** -> AI Confidence: **99.24%**
1637. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/AbstractReflectionApiCallChecker.kt`** -> AI Confidence: **99.24%**
1638. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/DeprecatedCallChecker.kt`** -> AI Confidence: **99.24%**
1639. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ProtectedConstructorCallChecker.kt`** -> AI Confidence: **99.24%**
1640. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/SynchronizedByValueChecker.kt`** -> AI Confidence: **99.24%**
1641. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/UselessElvisCallChecker.kt`** -> AI Confidence: **99.24%**
1642. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/BuilderInferenceSession.kt`** -> AI Confidence: **99.24%**
1643. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/BuilderInferenceUtil.kt`** -> AI Confidence: **99.24%**
1644. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/ConstraintSystemImpl.kt`** -> AI Confidence: **99.24%**
1645. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tasks/dynamicCalls.kt`** -> AI Confidence: **99.24%**
1646. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewResolutionOldInference.kt`** -> AI Confidence: **99.24%**
1647. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/util/callUtil.kt`** -> AI Confidence: **99.24%**
1648. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/util/resolvedCallUtil.kt`** -> AI Confidence: **99.24%**
1649. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ContextualDeclarationChecker.kt`** -> AI Confidence: **99.24%**
1650. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DataObjectContentChecker.kt`** -> AI Confidence: **99.24%**
1651. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DeprecatedSinceKotlinAnnotationChecker.kt`** -> AI Confidence: **99.24%**
1652. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ExpectActualClassifiersAreInBetaChecker.kt`** -> AI Confidence: **99.24%**
1653. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/InlineParameterChecker.kt`** -> AI Confidence: **99.24%**
1654. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/NullableExtensionOperatorWithSafeCallChecker.kt`** -> AI Confidence: **99.24%**
1655. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/PublishedApiUsageChecker.kt`** -> AI Confidence: **99.24%**
1656. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ResolutionWithStubTypesChecker.kt`** -> AI Confidence: **99.24%**
1657. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SuspendFunctionAsSupertypeChecker.kt`** -> AI Confidence: **99.24%**
1658. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/VolatileAnnotationChecker.kt`** -> AI Confidence: **99.24%**
1659. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/deprecation/DeprecationResolver.kt`** -> AI Confidence: **99.24%**
1660. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/deprecation/deprecationUtil.kt`** -> AI Confidence: **99.24%**
1661. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/FileScopeFactory.kt`** -> AI Confidence: **99.24%**
1662. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/LazyDeclarationResolver.kt`** -> AI Confidence: **99.24%**
1663. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/AbstractLazyMemberScope.kt`** -> AI Confidence: **99.24%**
1664. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/ClassResolutionScopesSupport.kt`** -> AI Confidence: **99.24%**
1665. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/unqualifiedSuper/unqualifiedSuper.kt`** -> AI Confidence: **99.24%**
1666. **`compiler/incremental-compilation-impl/testFixtures/org/jetbrains/kotlin/incremental/AbstractIncrementalCompilerRunnerTestBase.kt`** -> AI Confidence: **99.24%**
1667. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/ExpectSymbolTransformer.kt`** -> AI Confidence: **99.24%**
1668. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/IrInlineUtils.kt`** -> AI Confidence: **99.24%**
1669. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/DefaultArgumentStubGenerator.kt`** -> AI Confidence: **99.24%**
1670. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ExpectDeclarationRemover.kt`** -> AI Confidence: **99.24%**
1671. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InlineClassDeclarationLowering.kt`** -> AI Confidence: **99.24%**
1672. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InnerClassesLowering.kt`** -> AI Confidence: **99.24%**
1673. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InventNamesForLocalClasses.kt`** -> AI Confidence: **99.24%**
1674. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InventNamesForLocalFunctions.kt`** -> AI Confidence: **99.24%**
1675. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/LateinitLowering.kt`** -> AI Confidence: **99.24%**
1676. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/LocalDeclarationPopupLowering.kt`** -> AI Confidence: **99.24%**
1677. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/SharedVariablesLowering.kt`** -> AI Confidence: **99.24%**
1678. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/ForLoopsLowering.kt`** -> AI Confidence: **99.24%**
1679. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/WithIndexLoopHeader.kt`** -> AI Confidence: **99.24%**
1680. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/StepHandler.kt`** -> AI Confidence: **99.24%**
1681. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/phaser/DumperVerifier.kt`** -> AI Confidence: **99.24%**
1682. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/IdSignatureHashCalculator.kt`** -> AI Confidence: **99.24%**
1683. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/BooleanPropertyInExternalLowering.kt`** -> AI Confidence: **99.24%**
1684. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/BridgesConstruction.kt`** -> AI Confidence: **99.24%**
1685. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/CollectClassDefaultConstructorsLowering.kt`** -> AI Confidence: **99.24%**
1686. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6AddBoxParameterLowering.kt`** -> AI Confidence: **99.24%**
1687. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6ConstructorBoxParameterOptimizationLowering.kt`** -> AI Confidence: **99.24%**
1688. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6ConstructorCallLowering.kt`** -> AI Confidence: **99.24%**
1689. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6ConstructorLowering.kt`** -> AI Confidence: **99.24%**
1690. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6PrimaryConstructorOptimizationLowering.kt`** -> AI Confidence: **99.24%**
1691. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/EscapedIdentifiersLowering.kt`** -> AI Confidence: **99.24%**
1692. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ExternalPropertyOverridingLowering.kt`** -> AI Confidence: **99.24%**
1693. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsDefaultArgumentStubGenerator.kt`** -> AI Confidence: **99.24%**
1694. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsStringConcatenationLowering.kt`** -> AI Confidence: **99.24%**
1695. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/MultipleCatchesLowering.kt`** -> AI Confidence: **99.24%**
1696. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PropertyLazyInitLowering.kt`** -> AI Confidence: **99.24%**
1697. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/SuspendLoweringUtils.kt`** -> AI Confidence: **99.24%**
1698. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/IrElementToJsStatementTransformer.kt`** -> AI Confidence: **99.24%**
1699. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/IrModuleToJsTransformer.kt`** -> AI Confidence: **99.24%**
1700. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsIrProgramFragment.kt`** -> AI Confidence: **99.24%**
1701. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsPolyfills.kt`** -> AI Confidence: **99.24%**
1702. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/tsexport/TransitiveExportCollector.kt`** -> AI Confidence: **99.24%**
1703. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/IrJsUtils.kt`** -> AI Confidence: **99.24%**
1704. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/IrTypeUtils.kt`** -> AI Confidence: **99.24%**
1705. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/JsInlineClassesUtils.kt`** -> AI Confidence: **99.24%**
1706. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/misc.kt`** -> AI Confidence: **99.24%**
1707. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/serialization/JsIrAstDeserializer.kt`** -> AI Confidence: **99.24%**
1708. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrInlineCodegen.kt`** -> AI Confidence: **99.24%**
1709. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrSourceCompilerForInline.kt`** -> AI Confidence: **99.24%**
1710. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/GetJavaPrimitiveType.kt`** -> AI Confidence: **99.24%**
1711. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/JvmInvokeDynamic.kt`** -> AI Confidence: **99.24%**
1712. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/JvmIrCodegenFactory.kt`** -> AI Confidence: **99.24%**
1713. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/SymbolTableWithBuiltInsDeduplication.kt`** -> AI Confidence: **99.24%**
1714. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/AdditionalClassAnnotationLowering.kt`** -> AI Confidence: **99.24%**
1715. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/CollectionStubMethodLowering.kt`** -> AI Confidence: **99.24%**
1716. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FileClassLowering.kt`** -> AI Confidence: **99.24%**
1717. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FunctionNVarargBridgeLowering.kt`** -> AI Confidence: **99.24%**
1718. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InterfaceObjectCallsLowering.kt`** -> AI Confidence: **99.24%**
1719. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmPropertiesLowering.kt`** -> AI Confidence: **99.24%**
1720. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmStaticAnnotationLowering.kt`** -> AI Confidence: **99.24%**
1721. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/MainMethodGenerationLowering.kt`** -> AI Confidence: **99.24%**
1722. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PolymorphicSignatureLowering.kt`** -> AI Confidence: **99.24%**
1723. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ProcessOptionalAnnotations.kt`** -> AI Confidence: **99.24%**
1724. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/TypeOperatorLowering.kt`** -> AI Confidence: **99.24%**
1725. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/VarargLowering.kt`** -> AI Confidence: **99.24%**
1726. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MemoizedInlineClassReplacements.kt`** -> AI Confidence: **99.24%**
1727. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MemoizedValueClassAbstractReplacements.kt`** -> AI Confidence: **99.24%**
1728. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MfvcNode.kt`** -> AI Confidence: **99.24%**
1729. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MfvcNodeInstance.kt`** -> AI Confidence: **99.24%**
1730. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/extensions/JvmIrDeclarationOrigin.kt`** -> AI Confidence: **99.24%**
1731. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/IrInlineReferenceLocator.kt`** -> AI Confidence: **99.24%**
1732. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmIrTypeUtils.kt`** -> AI Confidence: **99.24%**
1733. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/mapping/IrTypeMapper.kt`** -> AI Confidence: **99.24%**
1734. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cgen/InteropIrUtils.kt`** -> AI Confidence: **99.24%**
1735. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/Ir.kt`** -> AI Confidence: **99.24%**
1736. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/TypeTransformer.kt`** -> AI Confidence: **99.24%**
1737. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/ExcludeDeclarationsFromCodegen.kt`** -> AI Confidence: **99.24%**
1738. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrActualizer.kt`** -> AI Confidence: **99.24%**
1739. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/SpecialFakeOverrideSymbolsResolver.kt`** -> AI Confidence: **99.24%**
1740. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/IrAnnotationMatchingKmpChecker.kt`** -> AI Confidence: **99.24%**
1741. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/FunctionInlining.kt`** -> AI Confidence: **99.24%**
1742. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/InlineFunctionResolver.kt`** -> AI Confidence: **99.24%**
1743. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/OuterThisInInlineFunctionsSpecialAccessorLowering.kt`** -> AI Confidence: **99.24%**
1744. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/SyntheticAccessorLowering.kt`** -> AI Confidence: **99.24%**
1745. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/CallInterceptor.kt`** -> AI Confidence: **99.24%**
1746. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/InstructionsUnfolder.kt`** -> AI Confidence: **99.24%**
1747. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/IrTreeBuildUtils.kt`** -> AI Confidence: **99.24%**
1748. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/checker/EvaluationMode.kt`** -> AI Confidence: **99.24%**
1749. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/preprocessor/IrInterpreterConstGetterPreprocessor.kt`** -> AI Confidence: **99.24%**
1750. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/Proxy.kt`** -> AI Confidence: **99.24%**
1751. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/Wrapper.kt`** -> AI Confidence: **99.24%**
1752. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/KClassState.kt`** -> AI Confidence: **99.24%**
1753. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/KTypeState.kt`** -> AI Confidence: **99.24%**
1754. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstOnlyNecessaryTransformer.kt`** -> AI Confidence: **99.24%**
1755. **`compiler/ir/ir.objcinterop/src/org/jetbrains/kotlin/ir/objcinterop/IrObjCOverridablilityCondidtion.kt`** -> AI Confidence: **99.24%**
1756. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/KotlinUtils.kt`** -> AI Confidence: **99.24%**
1757. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ClassGenerator.kt`** -> AI Confidence: **99.24%**
1758. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/StatementGenerator.kt`** -> AI Confidence: **99.24%**
1759. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/ArrayAccessAssignmentReceiver.kt`** -> AI Confidence: **99.24%**
1760. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/expressions/IrExpressions.kt`** -> AI Confidence: **99.24%**
1761. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/symbols/impl/IrSymbolImpl.kt`** -> AI Confidence: **99.24%**
1762. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/IrTypeSubstitutor.kt`** -> AI Confidence: **99.24%**
1763. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/IrTypeSystemContext.kt`** -> AI Confidence: **99.24%**
1764. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/impl/IrSimpleTypeImpl.kt`** -> AI Confidence: **99.24%**
1765. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/ConstantValueGenerator.kt`** -> AI Confidence: **99.24%**
1766. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DataClassMembersGenerator.kt`** -> AI Confidence: **99.24%**
1767. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrTypeUtils.kt`** -> AI Confidence: **99.24%**
1768. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/RenderIrElement.kt`** -> AI Confidence: **99.24%**
1769. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/TypeTranslator.kt`** -> AI Confidence: **99.24%**
1770. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TransformerVoidPrinter.kt`** -> AI Confidence: **99.24%**
1771. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/CheckTreeConsistencyVisitor.kt`** -> AI Confidence: **99.24%**
1772. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/diagnostics/LibrarySpecialCompatibilityChecker.kt`** -> AI Confidence: **99.24%**
1773. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/BasicIrModuleDeserializer.kt`** -> AI Confidence: **99.24%**
1774. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IdSignatureDeserializer.kt`** -> AI Confidence: **99.24%**
1775. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/KotlinIrLinker.kt`** -> AI Confidence: **99.24%**
1776. **`compiler/ir/serialization.jklib/src/org/jetbrains/kotlin/ir/backend/jklib/JKlibIrLinker.kt`** -> AI Confidence: **99.24%**
1777. **`compiler/ir/serialization.jklib/src/org/jetbrains/kotlin/ir/backend/jklib/JKlibIrMangler.kt`** -> AI Confidence: **99.24%**
1778. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/wasm/WasmKlibExportingDeclaration.kt`** -> AI Confidence: **99.24%**
1779. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/IrUtils.kt`** -> AI Confidence: **99.24%**
1780. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanPartialModuleDeserializer.kt`** -> AI Confidence: **99.24%**
1781. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/JavacWrapper.kt`** -> AI Confidence: **99.24%**
1782. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedClass.kt`** -> AI Confidence: **99.24%**
1783. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/utils.kt`** -> AI Confidence: **99.24%**
1784. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtNamedFunction.kt`** -> AI Confidence: **99.24%**
1785. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/psiUtil/psiUtils.kt`** -> AI Confidence: **99.24%**
1786. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/ElementTypeUtils.kt`** -> AI Confidence: **99.24%**
1787. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/StubUtils.kt`** -> AI Confidence: **99.24%**
1788. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/model/NewConstraintSystemImpl.kt`** -> AI Confidence: **99.24%**
1789. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/CallableReferenceResolution.kt`** -> AI Confidence: **99.24%**
1790. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/UnitTypeConversions.kt`** -> AI Confidence: **99.24%**
1791. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/CallableReferencesCandidateFactory.kt`** -> AI Confidence: **99.24%**
1792. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/SimpleCandidateFactory.kt`** -> AI Confidence: **99.24%**
1793. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/results/FlatSignatureUtils.kt`** -> AI Confidence: **99.24%**
1794. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/scopes/utils/ScopeUtils.kt`** -> AI Confidence: **99.24%**
1795. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/inferencelogs/FirInferenceLogsDumper.kt`** -> AI Confidence: **99.24%**
1796. **`compiler/util-io/src/org/jetbrains/kotlin/konan/file/ZipUtil.kt`** -> AI Confidence: **99.24%**
1797. **`compiler/util-klib-abi/src/org/jetbrains/kotlin/library/abi/impl/LibraryAbiReaderImpl.kt`** -> AI Confidence: **99.24%**
1798. **`compiler/util-klib/src/org/jetbrains/kotlin/library/loader/KlibLoader.kt`** -> AI Confidence: **99.24%**
1799. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/load/java/typeEnhancement/AbstractSignatureParts.kt`** -> AI Confidence: **99.24%**
1800. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/load/kotlin/typeSignatureMapping.kt`** -> AI Confidence: **99.24%**
1801. **`core/descriptors.jvm/src/org/jetbrains/kotlin/builtins/jvm/JavaToKotlinClassMapper.kt`** -> AI Confidence: **99.24%**
1802. **`core/descriptors.jvm/src/org/jetbrains/kotlin/builtins/jvm/JvmBuiltInsCustomizer.kt`** -> AI Confidence: **99.24%**
1803. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/components/ReflectKotlinClass.kt`** -> AI Confidence: **99.24%**
1804. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/structure/ReflectJavaMember.kt`** -> AI Confidence: **99.24%**
1805. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/CompileTimeConstant.kt`** -> AI Confidence: **99.24%**
1806. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/synthetic/FunInterfaceConstructorsSyntheticScope.kt`** -> AI Confidence: **99.24%**
1807. **`core/descriptors/src/org/jetbrains/kotlin/types/KotlinTypeFactory.kt`** -> AI Confidence: **99.24%**
1808. **`core/descriptors/src/org/jetbrains/kotlin/types/error/ErrorUtils.kt`** -> AI Confidence: **99.24%**
1809. **`core/descriptors/src/org/jetbrains/kotlin/types/flexibleTypes.kt`** -> AI Confidence: **99.24%**
1810. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/AnnotationDeserializer.kt`** -> AI Confidence: **99.24%**
1811. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/DescriptorKCallable.kt`** -> AI Confidence: **99.24%**
1812. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/util.kt`** -> AI Confidence: **99.24%**
1813. **`generators/protobufCompare/GenerateProtoBufCompare.kt`** -> AI Confidence: **99.24%**
1814. **`generators/tests/org/jetbrains/kotlin/generators/arguments/GenerateGradleOptions.kt`** -> AI Confidence: **99.24%**
1815. **`jps/jps-common/src/org/jetbrains/kotlin/arguments/CompilerArgumentsDeserializer.kt`** -> AI Confidence: **99.24%**
1816. **`jps/jps-plugin/src/org/jetbrains/kotlin/compilerRunner/JpsKotlinCompilerRunner.kt`** -> AI Confidence: **99.24%**
1817. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/incremental/CacheVersionManager.kt`** -> AI Confidence: **99.24%**
1818. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/KotlinJvmModuleBuildTarget.kt`** -> AI Confidence: **99.24%**
1819. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsDynamicCallChecker.kt`** -> AI Confidence: **99.24%**
1820. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsDynamicDeclarationChecker.kt`** -> AI Confidence: **99.24%**
1821. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsModuleChecker.kt`** -> AI Confidence: **99.24%**
1822. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsNameCharsChecker.kt`** -> AI Confidence: **99.24%**
1823. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsQualifierChecker.kt`** -> AI Confidence: **99.24%**
1824. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsRuntimeAnnotationChecker.kt`** -> AI Confidence: **99.24%**
1825. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/nativeAnnotationCheckers.kt`** -> AI Confidence: **99.24%**
1826. **`js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/JsAstMapperVisitor.kt`** -> AI Confidence: **99.24%**
1827. **`kotlin-native/Interop/Runtime/src/jvm/kotlin/kotlinx/cinterop/JvmUtils.kt`** -> AI Confidence: **99.24%**
1828. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/jvm/main.kt`** -> AI Confidence: **99.24%**
1829. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/Boxing.kt`** -> AI Confidence: **99.24%**
1830. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/DependenciesTracker.kt`** -> AI Confidence: **99.24%**
1831. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/TopLevelPhases.kt`** -> AI Confidence: **99.24%**
1832. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/ClassLayoutBuilder.kt`** -> AI Confidence: **99.24%**
1833. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/IrUtils.kt`** -> AI Confidence: **99.24%**
1834. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/CodeGenerator.kt`** -> AI Confidence: **99.24%**
1835. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/DebugUtils.kt`** -> AI Confidence: **99.24%**
1836. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/IntrinsicGenerator.kt`** -> AI Confidence: **99.24%**
1837. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/KotlinObjCClassInfoGenerator.kt`** -> AI Confidence: **99.24%**
1838. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ExpectToActualDefaultValueCopier.kt`** -> AI Confidence: **99.24%**
1839. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InnerClassLowering.kt`** -> AI Confidence: **99.24%**
1840. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InteropCallConvertors.kt`** -> AI Confidence: **99.24%**
1841. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InteropLowering.kt`** -> AI Confidence: **99.24%**
1842. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/RedundantCoercionsCleaner.kt`** -> AI Confidence: **99.24%**
1843. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/StaticInitializersLowering.kt`** -> AI Confidence: **99.24%**
1844. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/ComputeTypesPass.kt`** -> AI Confidence: **99.24%**
1845. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DataFlowIR.kt`** -> AI Confidence: **99.24%**
1846. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/CacheSerializationSupport.kt`** -> AI Confidence: **99.24%**
1847. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/nativeFullCrossDist.kt`** -> AI Confidence: **99.24%**
1848. **`libraries/kotlinx-metadata/jvm/src/kotlin/metadata/jvm/internal/JvmMetadataExtensions.kt`** -> AI Confidence: **99.24%**
1849. **`libraries/kotlinx-metadata/jvm/src/kotlin/metadata/jvm/internal/JvmReadUtils.kt`** -> AI Confidence: **99.24%**
1850. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/jsr223/KotlinJsr223InvocableScriptEngine.kt`** -> AI Confidence: **99.24%**
1851. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/repl/legacyReplEvaluation.kt`** -> AI Confidence: **99.24%**
1852. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/reports/MethodReport.kt`** -> AI Confidence: **99.24%**
1853. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/tasks/ClassTask.kt`** -> AI Confidence: **99.24%**
1854. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/tasks/JarTask.kt`** -> AI Confidence: **99.24%**
1855. **`libraries/tools/gradle/fus-statistics-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/fus/internal/GradleBuildFusStatisticsBuildService.kt`** -> AI Confidence: **99.24%**
1856. **`libraries/tools/gradle/regression-benchmark-templates/src/main/kotlin/org/jetbrains/kotlin/gradle/benchmark/BenchmarkTemplate.kt`** -> AI Confidence: **99.24%**
1857. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/extras.kt`** -> AI Confidence: **99.24%**
1858. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinClasspath.kt`** -> AI Confidence: **99.24%**
1859. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/Kotlin2JsIrBeIncrementalCompilationIT.kt`** -> AI Confidence: **99.24%**
1860. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MPPBuildReproducibilityIT.kt`** -> AI Confidence: **99.24%**
1861. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MppHighlightingTestDataWithGradleIT.kt`** -> AI Confidence: **99.24%**
1862. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppCrossCompilationPublicationIT.kt`** -> AI Confidence: **99.24%**
1863. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppDslAssociateCompilationsIT.kt`** -> AI Confidence: **99.24%**
1864. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/CocoaPodsPodspecIT.kt`** -> AI Confidence: **99.24%**
1865. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/BuildOptions.kt`** -> AI Confidence: **99.24%**
1866. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/cocoapodsTestHelpers.kt`** -> AI Confidence: **99.24%**
1867. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/daemonHelpers.kt`** -> AI Confidence: **99.24%**
1868. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/fileAssertions.kt`** -> AI Confidence: **99.24%**
1869. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/osConditions.kt`** -> AI Confidence: **99.24%**
1870. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/testAssertions.kt`** -> AI Confidence: **99.24%**
1871. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/xctestHelpers.kt`** -> AI Confidence: **99.24%**
1872. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/reportUtils.kt`** -> AI Confidence: **99.24%**
1873. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/KaptWithoutKotlincTask.kt`** -> AI Confidence: **99.24%**
1874. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/testing/TCServiceMessageOutputStreamHandler.kt`** -> AI Confidence: **99.24%**
1875. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/testing/TCServiceMessagesTestExecutor.kt`** -> AI Confidence: **99.24%**
1876. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/PropertiesProvider.kt`** -> AI Confidence: **99.24%**
1877. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/SubpluginEnvironment.kt`** -> AI Confidence: **99.24%**
1878. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/StyledToolingDiagnostic.kt`** -> AI Confidence: **99.24%**
1879. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ToolingDiagnosticRenderingOptions.kt`** -> AI Confidence: **99.24%**
1880. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/KotlinTargetAlreadyDeclaredChecker.kt`** -> AI Confidence: **99.24%**
1881. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/PreHmppDependenciesUsageChecker.kt`** -> AI Confidence: **99.24%**
1882. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/hierarchy/defaultKotlinHierarchySetup.kt`** -> AI Confidence: **99.24%**
1883. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeBinaryDependencyResolver.kt`** -> AI Confidence: **99.24%**
1884. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeTransformedMetadataDependencyResolver.kt`** -> AI Confidence: **99.24%**
1885. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/resolveCinteropDependency.kt`** -> AI Confidence: **99.24%**
1886. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/CompositeMetadataArtifactImpl.kt`** -> AI Confidence: **99.24%**
1887. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinUsages.kt`** -> AI Confidence: **99.24%**
1888. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/ModuleIds.kt`** -> AI Confidence: **99.24%**
1889. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/SourceSetVisibilityProvider.kt`** -> AI Confidence: **99.24%**
1890. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/SymbolicLinkToFrameworkTask.kt`** -> AI Confidence: **99.24%**
1891. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationK2MultiplatformConfigurator.kt`** -> AI Confidence: **99.24%**
1892. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCreateLifecycleTasksSideEffect.kt`** -> AI Confidence: **99.24%**
1893. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/PomDependenciesRewriter.kt`** -> AI Confidence: **99.24%**
1894. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/publication/rewritePomForKotlinDomApiCompat.kt`** -> AI Confidence: **99.24%**
1895. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/BuildReportsService.kt`** -> AI Confidence: **99.24%**
1896. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/NodeJsEnvironmentConfigurator.kt`** -> AI Confidence: **99.24%**
1897. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/resolver/KotlinRootNpmResolver.kt`** -> AI Confidence: **99.24%**
1898. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/utils.kt`** -> AI Confidence: **99.24%**
1899. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpackConfig.kt`** -> AI Confidence: **99.24%**
1900. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerDependent.kt`** -> AI Confidence: **99.24%**
1901. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/XcodeDefaultTestDevicesValueSource.kt`** -> AI Confidence: **99.24%**
1902. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/nodejs/BaseNodeJsEnvSpec.kt`** -> AI Confidence: **99.24%**
1903. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/KotlinJsIrLinkConfig.kt`** -> AI Confidence: **99.24%**
1904. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/publishing/CheckSigningTask.kt`** -> AI Confidence: **99.24%**
1905. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/tasksUtils.kt`** -> AI Confidence: **99.24%**
1906. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/configurations.kt`** -> AI Confidence: **99.24%**
1907. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/ConfigurationsTest.kt`** -> AI Confidence: **99.24%**
1908. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CInteropMetadataDependencyTransformationTaskTest.kt`** -> AI Confidence: **99.24%**
1909. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CompositeMetadataArtifactTest.kt`** -> AI Confidence: **99.24%**
1910. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/DisabledNativeCacheTest.kt`** -> AI Confidence: **99.24%**
1911. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/IdeKotilnCompilerArgumentsResolverTest.kt`** -> AI Confidence: **99.24%**
1912. **`libraries/tools/kotlin-main-kts/src/org/jetbrains/kotlin/mainKts/scriptDef.kt`** -> AI Confidence: **99.24%**
1913. **`libraries/tools/kotlin-stdlib-docs/plugins/dokka-version-filter-plugin/src/main/kotlin/org/jetbrains/dokka/kotlinlang/VersionFilterTransformer.kt`** -> AI Confidence: **99.24%**
1914. **`native/cli-native/src/org/jetbrains/kotlin/cli/bc/K2Native.kt`** -> AI Confidence: **99.24%**
1915. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/cir/CirName.kt`** -> AI Confidence: **99.24%**
1916. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/mergedtree/CirProvidedClassifiersByModules.kt`** -> AI Confidence: **99.24%**
1917. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/metadata/CirSerializers.kt`** -> AI Confidence: **99.24%**
1918. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/metadata/CirTreeSerializer.kt`** -> AI Confidence: **99.24%**
1919. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/metadata/utils/MetadataDeclarationsComparator.kt`** -> AI Confidence: **99.24%**
1920. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/stats/RawStatsCollector.kt`** -> AI Confidence: **99.24%**
1921. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/transformer/InlineTypeAliasCirNodeTransformer.kt`** -> AI Confidence: **99.24%**
1922. **`native/commonizer/tests/org/jetbrains/kotlin/commonizer/utils/assertions.kt`** -> AI Confidence: **99.24%**
1923. **`native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/HostExecutor.kt`** -> AI Confidence: **99.24%**
1924. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCNameOverridesChecker.kt`** -> AI Confidence: **99.24%**
1925. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeThreadLocalChecker.kt`** -> AI Confidence: **99.24%**
1926. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeThrowsChecker.kt`** -> AI Confidence: **99.24%**
1927. **`native/native.tests/stress/testData/stress_gc_allocations.kt`** -> AI Confidence: **99.24%**
1928. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/KtObjCExportFile.kt`** -> AI Confidence: **99.24%**
1929. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCConstructor.kt`** -> AI Confidence: **99.24%**
1930. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCObjectType.kt`** -> AI Confidence: **99.24%**
1931. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCProperty.kt`** -> AI Confidence: **99.24%**
1932. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/withNullabilityOf.kt`** -> AI Confidence: **99.24%**
1933. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportHeaderGenerator.kt`** -> AI Confidence: **99.24%**
1934. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirFunctionFromKtSymbol.kt`** -> AI Confidence: **99.24%**
1935. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirInitFromKtSymbol.kt`** -> AI Confidence: **99.24%**
1936. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirVariableFromKtSymbol.kt`** -> AI Confidence: **99.24%**
1937. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirParentProviderImpl.kt`** -> AI Confidence: **99.24%**
1938. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/StandaloneSirTypeNamer.kt`** -> AI Confidence: **99.24%**
1939. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/utils/AnalysisApiUtils.kt`** -> AI Confidence: **99.24%**
1940. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/jvm/JvmAtomicfuIrBuilder.kt`** -> AI Confidence: **99.24%**
1941. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/BuildMetrics.kt`** -> AI Confidence: **99.24%**
1942. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposableTargetChecker.kt`** -> AI Confidence: **99.24%**
1943. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/FirUtils.kt`** -> AI Confidence: **99.24%**
1944. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ClassStabilityFieldSerializationPlugin.kt`** -> AI Confidence: **99.24%**
1945. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/CopyDefaultValuesFromExpectLowering.kt`** -> AI Confidence: **99.24%**
1946. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/IrInlineReferenceLocator.kt`** -> AI Confidence: **99.24%**
1947. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/hiddenfromobjc/AddHiddenFromObjCLowering.kt`** -> AI Confidence: **99.24%**
1948. **`plugins/jvm-abi-gen/src/org/jetbrains/kotlin/jvm/abi/JvmAbiOutputExtension.kt`** -> AI Confidence: **99.24%**
1949. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/annotationProcessing.kt`** -> AI Confidence: **99.24%**
1950. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/incremental/incrementalProcessors.kt`** -> AI Confidence: **99.24%**
1951. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/incremental/javacVisitors.kt`** -> AI Confidence: **99.24%**
1952. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/javac/KaptJavaFileObject.kt`** -> AI Confidence: **99.24%**
1953. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/SignatureParserVisitor.kt`** -> AI Confidence: **99.24%**
1954. **`plugins/kotlin-dataframe/kotlin-dataframe.backend/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/IrBodyFiller.kt`** -> AI Confidence: **99.24%**
1955. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/toDataFrame.kt`** -> AI Confidence: **99.24%**
1956. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/DefaultValuesUtils.kt`** -> AI Confidence: **99.24%**
1957. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrGeneratorUtils.kt`** -> AI Confidence: **99.24%**
1958. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrPreGenerator.kt`** -> AI Confidence: **99.24%**
1959. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrSerializableProperties.kt`** -> AI Confidence: **99.24%**
1960. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializableCompanionIrGenerator.kt`** -> AI Confidence: **99.24%**
1961. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializerIrGenerator.kt`** -> AI Confidence: **99.24%**
1962. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/extensions/SerializationDescriptorSerializerPlugin.kt`** -> AI Confidence: **99.24%**
1963. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/resolve/KSerializerDescriptorResolver.kt`** -> AI Confidence: **99.24%**
1964. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/SerializationFirSupertypesExtension.kt`** -> AI Confidence: **99.24%**
1965. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/SerializationFirUtils.kt`** -> AI Confidence: **99.24%**
1966. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/checkers/FirSerializationPluginCallChecker.kt`** -> AI Confidence: **99.24%**
1967. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/checkers/SerializationFirCheckerUtils.kt`** -> AI Confidence: **99.24%**
1968. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/services/ContextualSerializersProvider.kt`** -> AI Confidence: **99.24%**
1969. **`plugins/lombok/lombok.k1/src/org/jetbrains/kotlin/lombok/processor/BuilderProcessor.kt`** -> AI Confidence: **99.24%**
1970. **`plugins/lombok/lombok.k1/src/org/jetbrains/kotlin/lombok/processor/GetterProcessor.kt`** -> AI Confidence: **99.24%**
1971. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/AllArgsConstructorGeneratorPart.kt`** -> AI Confidence: **99.24%**
1972. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/utils.kt`** -> AI Confidence: **99.24%**
1973. **`plugins/noarg/noarg.k1/src/org/jetbrains/kotlin/noarg/diagnostic/CliNoArgDeclarationChecker.kt`** -> AI Confidence: **99.24%**
1974. **`plugins/noarg/noarg.k2/src/org/jetbrains/kotlin/noarg/fir/FirNoArgDeclarationChecker.kt`** -> AI Confidence: **99.24%**
1975. **`plugins/parcelize/parcelize-compiler/parcelize.k1/src/org/jetbrains/kotlin/parcelize/ParcelizeResolveExtension.kt`** -> AI Confidence: **99.24%**
1976. **`plugins/parcelize/parcelize-compiler/parcelize.k1/src/org/jetbrains/kotlin/parcelize/serializers/ParcelSerializer.kt`** -> AI Confidence: **99.24%**
1977. **`plugins/parcelize/parcelize-compiler/parcelize.k2/src/org/jetbrains/kotlin/parcelize/fir/diagnostics/FirParcelizeAnnotationChecker.kt`** -> AI Confidence: **99.24%**
1978. **`plugins/parcelize/parcelize-compiler/parcelize.k2/src/org/jetbrains/kotlin/parcelize/fir/diagnostics/FirParcelizeClassChecker.kt`** -> AI Confidence: **99.24%**
1979. **`plugins/parcelize/parcelize-compiler/parcelize.k2/src/org/jetbrains/kotlin/parcelize/fir/diagnostics/FirParcelizeConstructorChecker.kt`** -> AI Confidence: **99.24%**
1980. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/CompanionGenerator.kt`** -> AI Confidence: **99.24%**
1981. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/ExternalClassGenerator.kt`** -> AI Confidence: **99.24%**
1982. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/supertypeswithoverrides/MissingOverrideStatusTransformer.kt`** -> AI Confidence: **99.24%**
1983. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/ir/AbstractTransformerForGenerator.kt`** -> AI Confidence: **99.24%**
1984. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/definitions/ScriptCompilationConfigurationFromLegacyTemplate.kt`** -> AI Confidence: **99.24%**
1985. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/definitions/definitions.kt`** -> AI Confidence: **99.24%**
1986. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/resolve/LazyScriptDescriptor.kt`** -> AI Confidence: **99.24%**
1987. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/AbstractScriptEvaluationExtension.kt`** -> AI Confidence: **99.24%**
1988. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/ScriptJvmCompilerImpls.kt`** -> AI Confidence: **99.24%**
1989. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/compilationContext.kt`** -> AI Confidence: **99.24%**
1990. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/k2RefinementUtil.kt`** -> AI Confidence: **99.24%**
1991. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/irLowerings/ScriptLowering.kt`** -> AI Confidence: **99.24%**
1992. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/reader/ReplSystemInWrapper.kt`** -> AI Confidence: **99.24%**
1993. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/services/FirScriptDefinitionProviderService.kt`** -> AI Confidence: **99.24%**
1994. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/CallType.kt`** -> AI Confidence: **99.24%**
1995. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/ShadowedDeclarationsFilter.kt`** -> AI Confidence: **99.24%**
1996. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/scopeUtils.kt`** -> AI Confidence: **99.24%**
1997. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/stripMetadata.kt`** -> AI Confidence: **99.24%**
1998. **`repo/gradle-build-conventions/gradle-plugins-common/src/main/kotlin/plugins/KotlinBuildPublishingPlugin.kt`** -> AI Confidence: **99.24%**
1999. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/FirWasmJsAssociatedObjectChecker.kt`** -> AI Confidence: **99.24%**
2000. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/WasmExportAnnotationChecker.kt`** -> AI Confidence: **99.24%**
2001. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/WasmImportAnnotationChecker.kt`** -> AI Confidence: **99.24%**
2002. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/WasmWasiExternalDeclarationChecker.kt`** -> AI Confidence: **99.24%**
2003. **`compiler/android-tests/tests/org/jetbrains/kotlin/android/tests/run/RunUtils.java`** -> AI Confidence: **99.24%**
2004. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/RemappingClassBuilder.java`** -> AI Confidence: **99.24%**
2005. **`compiler/cli/cli-base/src/com/intellij/openapi/util/ObjectNode.java`** -> AI Confidence: **99.24%**
2006. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/resolve/jvm/KotlinJavaPsiFacade.java`** -> AI Confidence: **99.24%**
2007. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/Errors.java`** -> AI Confidence: **99.24%**
2008. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DescriptorResolver.java`** -> AI Confidence: **99.24%**
2009. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ModifiersChecker.java`** -> AI Confidence: **99.24%**
2010. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/ArgumentTypeResolver.java`** -> AI Confidence: **99.24%**
2011. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ReifiedTypeParameterSubstitutionChecker.java`** -> AI Confidence: **99.24%**
2012. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/results/OverloadResolutionResultsUtil.java`** -> AI Confidence: **99.24%**
2013. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/results/ResolutionResultsHandler.java`** -> AI Confidence: **99.24%**
2014. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tasks/AbstractTracingStrategy.java`** -> AI Confidence: **99.24%**
2015. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/constants/CompileTimeConstantChecker.java`** -> AI Confidence: **99.24%**
2016. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/DataFlowAnalyzer.java`** -> AI Confidence: **99.24%**
2017. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/ExpressionTypingServices.java`** -> AI Confidence: **99.24%**
2018. **`compiler/preloader/src/org/jetbrains/kotlin/preloading/Preloader.java`** -> AI Confidence: **99.24%**
2019. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/SemanticWhitespaceAwarePsiBuilderImpl.java`** -> AI Confidence: **99.24%**
2020. **`compiler/tests-common/testFixtures/com/intellij/execution/configurations/ParametersList.java`** -> AI Confidence: **99.24%**
2021. **`compiler/tests-common/testFixtures/com/intellij/openapi/util/objectTree/ThrowableInterner.java`** -> AI Confidence: **99.24%**
2022. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/descriptors/JavaMethodDescriptor.java`** -> AI Confidence: **99.24%**
2023. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/descriptors/JavaPropertyDescriptor.java`** -> AI Confidence: **99.24%**
2024. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/FunctionDescriptorImpl.java`** -> AI Confidence: **99.24%**
2025. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeUtils.java`** -> AI Confidence: **99.24%**
2026. **`js/js.frontend/src/org/jetbrains/kotlin/js/patterns/PatternBuilder.java`** -> AI Confidence: **99.24%**
2027. **`js/js.frontend/src/org/jetbrains/kotlin/js/translate/utils/AnnotationsUtils.java`** -> AI Confidence: **99.24%**
2028. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/incremental/FileCopier.java`** -> AI Confidence: **99.24%**
2029. **`kotlin-native/runtime/src/crashHandler/impl/cpp/CrashHandler.cpp`** -> AI Confidence: **99.24%**
2030. **`kotlin-native/runtime/src/externalCallsChecker/impl/cpp/CallsChecker.cpp`** -> AI Confidence: **99.24%**
2031. **`kotlin-native/runtime/src/main/cpp/KAssert.cpp`** -> AI Confidence: **99.24%**
2032. **`kotlin-native/runtime/src/main/cpp/KString.cpp`** -> AI Confidence: **99.24%**
2033. **`kotlin-native/runtime/src/main/cpp/MemoryUsageInfo.cpp`** -> AI Confidence: **99.24%**
2034. **`kotlin-native/runtime/src/main/cpp/Porting.cpp`** -> AI Confidence: **99.24%**
2035. **`kotlin-native/runtime/src/main/cpp/Worker.cpp`** -> AI Confidence: **99.24%**
2036. **`kotlin-native/runtime/src/mm/cpp/ThreadSuspensionTest.cpp`** -> AI Confidence: **99.24%**
2037. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/InlineFunctionsCollector.kt`** -> AI Confidence: **99.23%**
2038. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/lifetime/KotlinReadActionConfinementLifetimeToken.kt`** -> AI Confidence: **99.23%**
2039. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/packages/KotlinPackageProviderBase.kt`** -> AI Confidence: **99.23%**
2040. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/renderers/KaFunctionalTypeRenderer.kt`** -> AI Confidence: **99.23%**
2041. **`build-common/src/org/jetbrains/kotlin/incremental/KotlinClassInfo.kt`** -> AI Confidence: **99.23%**
2042. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/JvmCompilerArguments.kt`** -> AI Confidence: **99.23%**
2043. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/SMAPBuilder.kt`** -> AI Confidence: **99.23%**
2044. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/repl/KotlinJsr223JvmInvocableScriptEngine.kt`** -> AI Confidence: **99.23%**
2045. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/findMainClass.kt`** -> AI Confidence: **99.23%**
2046. **`compiler/cli/cli-runner/src/org/jetbrains/kotlin/runner/Main.kt`** -> AI Confidence: **99.23%**
2047. **`compiler/daemon/daemon-client/src/main/kotlin/BasicCompilerServicesWithResultsFacadeServer.kt`** -> AI Confidence: **99.23%**
2048. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNativeAnnotationCheckers.kt`** -> AI Confidence: **99.23%**
2049. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirUnderscoreHelpers.kt`** -> AI Confidence: **99.23%**
2050. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/experimental/EmptyRangeChecker.kt`** -> AI Confidence: **99.23%**
2051. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCatchParameterChecker.kt`** -> AI Confidence: **99.23%**
2052. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTypeVisibilityHelpers.kt`** -> AI Confidence: **99.23%**
2053. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirDelegationInExpectClassSyntaxChecker.kt`** -> AI Confidence: **99.23%**
2054. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/FirMissingDependencyStorage.kt`** -> AI Confidence: **99.23%**
2055. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirDefaultParametersResolver.kt`** -> AI Confidence: **99.23%**
2056. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/declarations/ArrayOfUtils.kt`** -> AI Confidence: **99.23%**
2057. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/expressions/SubstitutionUtils.kt`** -> AI Confidence: **99.23%**
2058. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/calls/TypeVariableTypeRemovingSubstitutor.kt`** -> AI Confidence: **99.23%**
2059. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/ClassMembers.kt`** -> AI Confidence: **99.23%**
2060. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirAnnotationRenderer.kt`** -> AI Confidence: **99.23%**
2061. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirModifierRenderer.kt`** -> AI Confidence: **99.23%**
2062. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/Annotations.kt`** -> AI Confidence: **99.23%**
2063. **`compiler/frontend.common/src/org/jetbrains/kotlin/util/ServiceLoaderLite.kt`** -> AI Confidence: **99.23%**
2064. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/components/AbstractJavaResolverCache.kt`** -> AI Confidence: **99.23%**
2065. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmOverloadFilter.kt`** -> AI Confidence: **99.23%**
2066. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmOverridesBackwardCompatibilityHelper.kt`** -> AI Confidence: **99.23%**
2067. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmPlatformOverloadsSpecificityComparator.kt`** -> AI Confidence: **99.23%**
2068. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ClassInheritsJavaSealedClassChecker.kt`** -> AI Confidence: **99.23%**
2069. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmInlineApplicabilityChecker.kt`** -> AI Confidence: **99.23%**
2070. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmSimpleNameBacktickChecker.kt`** -> AI Confidence: **99.23%**
2071. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/PolymorphicSignatureCallChecker.kt`** -> AI Confidence: **99.23%**
2072. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/variable/VariableControlFlowInfo.kt`** -> AI Confidence: **99.23%**
2073. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ResolutionToPrivateConstructorOfSealedClassChecker.kt`** -> AI Confidence: **99.23%**
2074. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/VarargWrongExecutionOrderChecker.kt`** -> AI Confidence: **99.23%**
2075. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ActualTypealiasToSpecialAnnotationChecker.kt`** -> AI Confidence: **99.23%**
2076. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DeprecationInheritanceChecker.kt`** -> AI Confidence: **99.23%**
2077. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/PrivateInlineFunctionsReturningAnonymousObjectsChecker.kt`** -> AI Confidence: **99.23%**
2078. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/multiproject/ModulesApiHistory.kt`** -> AI Confidence: **99.23%**
2079. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/CompilationException.kt`** -> AI Confidence: **99.23%**
2080. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/TailSuspendCallsCollector.kt`** -> AI Confidence: **99.23%**
2081. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/JsPerFileCache.kt`** -> AI Confidence: **99.23%**
2082. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IntIncr.kt`** -> AI Confidence: **99.23%**
2083. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/WasmModuleFragmentGenerator.kt`** -> AI Confidence: **99.23%**
2084. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/SamTypeFactory.kt`** -> AI Confidence: **99.23%**
2085. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/model/Element.kt`** -> AI Confidence: **99.23%**
2086. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/symbol/SymbolPrinter.kt`** -> AI Confidence: **99.23%**
2087. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/ClassifierResolver.kt`** -> AI Confidence: **99.23%**
2088. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/IdentifierResolver.kt`** -> AI Confidence: **99.23%**
2089. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/ResolveHelper.kt`** -> AI Confidence: **99.23%**
2090. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/lexer/KtTokens.kt`** -> AI Confidence: **99.23%**
2091. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/ErrorCandidateFactory.kt`** -> AI Confidence: **99.23%**
2092. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/ScopeTowerProcessors.kt`** -> AI Confidence: **99.23%**
2093. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/ContractSerializer.kt`** -> AI Confidence: **99.23%**
2094. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/SerializerExtensionBase.kt`** -> AI Confidence: **99.23%**
2095. **`compiler/testData/ir/irText/expressions/useImportedMember.kt`** -> AI Confidence: **99.23%**
2096. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/resolver/impl/KotlinLibraryResolverImpl.kt`** -> AI Confidence: **99.23%**
2097. **`compiler/util-klib/src/org/jetbrains/kotlin/library/loader/KlibPlatformChecker.kt`** -> AI Confidence: **99.23%**
2098. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/ErasedOverridabilityCondition.kt`** -> AI Confidence: **99.23%**
2099. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/structure/ReflectJavaClass.kt`** -> AI Confidence: **99.23%**
2100. **`core/descriptors/src/org/jetbrains/kotlin/incremental/utils.kt`** -> AI Confidence: **99.23%**
2101. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/PrimitiveTypeUtil.kt`** -> AI Confidence: **99.23%**
2102. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeAttributes.kt`** -> AI Confidence: **99.23%**
2103. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/KotlinTypePreparator.kt`** -> AI Confidence: **99.23%**
2104. **`core/deserialization.common/src/org/jetbrains/kotlin/serialization/deserialization/ValueClassUtil.kt`** -> AI Confidence: **99.23%**
2105. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/ClassDeserializer.kt`** -> AI Confidence: **99.23%**
2106. **`core/reflection.jvm/src/kotlin/reflect/full/KCallables.kt`** -> AI Confidence: **99.23%**
2107. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsBuiltinNameClashChecker.kt`** -> AI Confidence: **99.23%**
2108. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsModuleCallChecker.kt`** -> AI Confidence: **99.23%**
2109. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CStubsManager.kt`** -> AI Confidence: **99.23%**
2110. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/LlvmModuleSpecificationImpl.kt`** -> AI Confidence: **99.23%**
2111. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/CallGraphBuilder.kt`** -> AI Confidence: **99.23%**
2112. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/ModuleDeserializerProvider.kt`** -> AI Confidence: **99.23%**
2113. **`kotlin-native/runtime/src/main/kotlin/kotlin/Throwable.kt`** -> AI Confidence: **99.23%**
2114. **`kotlin-native/tools/kdumputil/src/io/inputStream.kt`** -> AI Confidence: **99.23%**
2115. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/ReadUtils.kt`** -> AI Confidence: **99.23%**
2116. **`libraries/scripting/dependencies-maven/src/kotlin/script/experimental/dependencies/maven/impl/mavenSettings.kt`** -> AI Confidence: **99.23%**
2117. **`libraries/stdlib/jvm/src/kotlin/text/regex/Regex.kt`** -> AI Confidence: **99.23%**
2118. **`libraries/tools/dukat/src/main/kotlin/org/jetbrains/kotlin/tools/dukat/wasm/translator.kt`** -> AI Confidence: **99.23%**
2119. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/AppleSiliconIT.kt`** -> AI Confidence: **99.23%**
2120. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/diagnosticsAssertions.kt`** -> AI Confidence: **99.23%**
2121. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/TeamCityMessageCommonClient.kt`** -> AI Confidence: **99.23%**
2122. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/SyncLanguageSettingsWithKotlinExtensionSetupAction.kt`** -> AI Confidence: **99.23%**
2123. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/applyUserDefinedAttributes.kt`** -> AI Confidence: **99.23%**
2124. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/factory/KotlinCompilationDependencyConfigurationsFactories.kt`** -> AI Confidence: **99.23%**
2125. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/UklibFragmentPlatformAttribute.kt`** -> AI Confidence: **99.23%**
2126. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropMetadataDependencyClasspath.kt`** -> AI Confidence: **99.23%**
2127. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/internal/CleanableStoreImpl.kt`** -> AI Confidence: **99.23%**
2128. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/cacheKlibUtils.kt`** -> AI Confidence: **99.23%**
2129. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/assertions.kt`** -> AI Confidence: **99.23%**
2130. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/jdk/LinuxJdkProvider.kt`** -> AI Confidence: **99.23%**
2131. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeConflictingOverloadsDispatcher.kt`** -> AI Confidence: **99.23%**
2132. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeHiddenFromObjCInheritanceChecker.kt`** -> AI Confidence: **99.23%**
2133. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeIdentifierChecker.kt`** -> AI Confidence: **99.23%**
2134. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/platform/ObjCOverridabilityCondition.kt`** -> AI Confidence: **99.23%**
2135. **`native/kotlin-test-native-xctest/src/nativeMain/kotlin/NativeTestObserver.kt`** -> AI Confidence: **99.23%**
2136. **`native/native.tests/testData/gc/worker10.kt`** -> AI Confidence: **99.23%**
2137. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCHeader.kt`** -> AI Confidence: **99.23%**
2138. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/BridgeGenerationUtils.kt`** -> AI Confidence: **99.23%**
2139. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/PackageFlatteningSirDeclarationProvider.kt`** -> AI Confidence: **99.23%**
2140. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/GoldenTransformRule.kt`** -> AI Confidence: **99.23%**
2141. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposeTypeResolutionInterceptorExtension.kt`** -> AI Confidence: **99.23%**
2142. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/Nulls.kt`** -> AI Confidence: **99.23%**
2143. **`plugins/lombok/lombok.k1/src/org/jetbrains/kotlin/lombok/processor/SetterProcessor.kt`** -> AI Confidence: **99.23%**
2144. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/definitions/LazyScriptDefinitionProvider.kt`** -> AI Confidence: **99.23%**
2145. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/util/jsCodeUtils.kt`** -> AI Confidence: **99.23%**
2146. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/TypeCheckingProcedure.java`** -> AI Confidence: **99.23%**
2147. **`kotlin-native/runtime/src/main/cpp/ObjCInteropUtils.h`** -> AI Confidence: **99.23%**
2148. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/native-cocoapods-single/pod_dependency/src/foo.m`** -> AI Confidence: **99.23%**
2149. **`native/native.tests/testData/CInterop/simple/include/A.h`** -> AI Confidence: **99.23%**
2150. **`kotlin-native/runtime/src/alloc/custom/cpp/CustomAllocatorTest.cpp`** -> AI Confidence: **99.23%**
2151. **`kotlin-native/runtime/src/launcher/cpp/launcher.cpp`** -> AI Confidence: **99.23%**
2152. **`kotlin-native/runtime/src/main/cpp/ObjCExceptions.cpp`** -> AI Confidence: **99.23%**
2153. **`kotlin-native/runtime/src/main/cpp/concurrent/UtilityThread.hpp`** -> AI Confidence: **99.23%**
2154. **`kotlin-native/runtime/src/main/cpp/dtoa/fltconst.h`** -> AI Confidence: **99.23%**
2155. **`kotlin-native/runtime/src/mm/cpp/SafePointTest.cpp`** -> AI Confidence: **99.23%**
2156. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/ApiVersionCallsPreprocessingMethodTransformer.kt`** -> AI Confidence: **99.22%**
2157. **`core/reflection.jvm/src/kotlin/reflect/jvm/KCallablesJvm.kt`** -> AI Confidence: **99.22%**
2158. **`libraries/tools/kotlin-stdlib-gen/src/templates/Aggregates.kt`** -> AI Confidence: **99.22%**
2159. **`kotlin-native/runtime/src/main/cpp/Common.h`** -> AI Confidence: **99.22%**
2160. **`generators/builtins/primitives/WasmPrimitivesGenerator.kt`** -> AI Confidence: **99.2%**
2161. **`js/js.translator/src/org/jetbrains/kotlin/js/inline/clean/IfStatementReduction.kt`** -> AI Confidence: **99.2%**
2162. **`libraries/stdlib/src/kotlin/time/Duration.kt`** -> AI Confidence: **99.2%**
2163. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/publication/Scenario.kt`** -> AI Confidence: **99.2%**
2164. **`native/external-projects-test-utils/src/org/jetbrains/kotlin/konan/test/testDependencies.kt`** -> AI Confidence: **99.2%**
2165. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/OverrideUtils.kt`** -> AI Confidence: **99.2%**
2166. **`native/swift/swift-export-standalone-integration-tests/simple/testData/execution/specialTypes/specialTypes.swift`** -> AI Confidence: **99.2%**
2167. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/CliFe10AnalysisFacade.kt`** -> AI Confidence: **99.18%**
2168. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10JavaInteroperabilityComponent.kt`** -> AI Confidence: **99.18%**
2169. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeCreator.kt`** -> AI Confidence: **99.18%**
2170. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/signatures/KaFe10VariableSignature.kt`** -> AI Confidence: **99.18%**
2171. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/KaFe10FileSymbol.kt`** -> AI Confidence: **99.18%**
2172. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescNamedClassSymbol.kt`** -> AI Confidence: **99.18%**
2173. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescNamedFunctionSymbol.kt`** -> AI Confidence: **99.18%**
2174. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescSyntheticJavaPropertySymbol.kt`** -> AI Confidence: **99.18%**
2175. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescSyntheticJavaPropertySymbolForOverride.kt`** -> AI Confidence: **99.18%**
2176. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescValueParameterSymbol.kt`** -> AI Confidence: **99.18%**
2177. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescEnumEntrySymbolPointer.kt`** -> AI Confidence: **99.18%**
2178. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescFunctionSymbolPointer.kt`** -> AI Confidence: **99.18%**
2179. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescNamedClassSymbolPointer.kt`** -> AI Confidence: **99.18%**
2180. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescSamConstructorSymbolPointer.kt`** -> AI Confidence: **99.18%**
2181. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescSyntheticFieldSymbolPointer.kt`** -> AI Confidence: **99.18%**
2182. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiBackingFieldSymbol.kt`** -> AI Confidence: **99.18%**
2183. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiDefaultPropertySetterSymbol.kt`** -> AI Confidence: **99.18%**
2184. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiNamedFunctionSymbol.kt`** -> AI Confidence: **99.18%**
2185. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiPropertyGetterSymbol.kt`** -> AI Confidence: **99.18%**
2186. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiPropertySetterSymbol.kt`** -> AI Confidence: **99.18%**
2187. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiValueParameterSymbol.kt`** -> AI Confidence: **99.18%**
2188. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10ErrorType.kt`** -> AI Confidence: **99.18%**
2189. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10FunctionType.kt`** -> AI Confidence: **99.18%**
2190. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10IntersectionType.kt`** -> AI Confidence: **99.18%**
2191. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/KaFe10DebugTypeRenderer.kt`** -> AI Confidence: **99.18%**
2192. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10InvokeFunctionReference.kt`** -> AI Confidence: **99.18%**
2193. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/util/DescriptorsToSourceUtilsIde.kt`** -> AI Confidence: **99.18%**
2194. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/ArgumentsConverterGenerator.kt`** -> AI Confidence: **99.18%**
2195. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/FirUtils.kt`** -> AI Confidence: **99.18%**
2196. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/annotations/KaFirAnnotationListForDeclaration.kt`** -> AI Confidence: **99.18%**
2197. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirEvaluator.kt`** -> AI Confidence: **99.18%**
2198. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirTypeCreator.kt`** -> AI Confidence: **99.18%**
2199. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/compilation/CodeFragmentContextDeclarationCache.kt`** -> AI Confidence: **99.18%**
2200. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/contracts/firContractUtils.kt`** -> AI Confidence: **99.18%**
2201. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirArrayAccessReference.kt`** -> AI Confidence: **99.18%**
2202. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirDestructuringDeclarationReference.kt`** -> AI Confidence: **99.18%**
2203. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/FirCallableFilteringScope.kt`** -> AI Confidence: **99.18%**
2204. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/FirJavaDeclaredMembersOnlyScope.kt`** -> AI Confidence: **99.18%**
2205. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/signatures/KaFirFunctionSignature.kt`** -> AI Confidence: **99.18%**
2206. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirAnonymousFunctionSymbol.kt`** -> AI Confidence: **99.18%**
2207. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirContextParameterSymbol.kt`** -> AI Confidence: **99.18%**
2208. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirContextReceiverBasedContextParameterSymbol.kt`** -> AI Confidence: **99.18%**
2209. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirDefaultBackingFieldSymbol.kt`** -> AI Confidence: **99.18%**
2210. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirEnumEntrySymbol.kt`** -> AI Confidence: **99.18%**
2211. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirLocalVariableSymbol.kt`** -> AI Confidence: **99.18%**
2212. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirNamedClassSymbolBase.kt`** -> AI Confidence: **99.18%**
2213. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPsiJavaClassSymbol.kt`** -> AI Confidence: **99.18%**
2214. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPsiJavaTypeParameterSymbol.kt`** -> AI Confidence: **99.18%**
2215. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirReceiverParameterSymbol.kt`** -> AI Confidence: **99.18%**
2216. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirTypeAliasSymbol.kt`** -> AI Confidence: **99.18%**
2217. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirBackingFieldSymbolPointer.kt`** -> AI Confidence: **99.18%**
2218. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirJavaFieldSymbolPointer.kt`** -> AI Confidence: **99.18%**
2219. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirPrimaryConstructorSymbolPointer.kt`** -> AI Confidence: **99.18%**
2220. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirPsiBasedPropertySymbolPointer.kt`** -> AI Confidence: **99.18%**
2221. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirScriptParameterSymbolPointer.kt`** -> AI Confidence: **99.18%**
2222. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirScriptSymbolPointer.kt`** -> AI Confidence: **99.18%**
2223. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTypeParameterSymbolPointer.kt`** -> AI Confidence: **99.18%**
2224. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirValueParameterSymbolPointer.kt`** -> AI Confidence: **99.18%**
2225. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirErrorType.kt`** -> AI Confidence: **99.18%**
2226. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/FirQualifierPartPointer.kt`** -> AI Confidence: **99.18%**
2227. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/scopesUtils.kt`** -> AI Confidence: **99.18%**
2228. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseIllegalPsiException.kt`** -> AI Confidence: **99.18%**
2229. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseResolver.kt`** -> AI Confidence: **99.18%**
2230. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseTypeRelationChecker.kt`** -> AI Confidence: **99.18%**
2231. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/sessions/KaBaseSessionProvider.kt`** -> AI Confidence: **99.18%**
2232. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/util/LibraryUtils.kt`** -> AI Confidence: **99.18%**
2233. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/declarations/KotlinCompositeDeclarationProvider.kt`** -> AI Confidence: **99.18%**
2234. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/packages/KotlinCachingPackageProviderFactory.kt`** -> AI Confidence: **99.18%**
2235. **`analysis/analysis-api-standalone/analysis-api-fir-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneFirCompilerPluginsProvider.kt`** -> AI Confidence: **99.18%**
2236. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/projectStructure/StandaloneProjectFactory.kt`** -> AI Confidence: **99.18%**
2237. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/builder/KaSourceModuleBuilder.kt`** -> AI Confidence: **99.18%**
2238. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaReferenceShortener.kt`** -> AI Confidence: **99.18%**
2239. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaResolver.kt`** -> AI Confidence: **99.18%**
2240. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaTypeProvider.kt`** -> AI Confidence: **99.18%**
2241. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/annotations/renderers/KaAnnotationQualifierRenderer.kt`** -> AI Confidence: **99.18%**
2242. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/annotations/renderers/KaAnnotationUseSiteTargetRenderer.kt`** -> AI Confidence: **99.18%**
2243. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/KaRendererCodeStyle.kt`** -> AI Confidence: **99.18%**
2244. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/KaClassifierBodyRenderer.kt`** -> AI Confidence: **99.18%**
2245. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/KaDeclarationNameRenderer.kt`** -> AI Confidence: **99.18%**
2246. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaCallableReturnTypeRenderer.kt`** -> AI Confidence: **99.18%**
2247. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaCallableSignatureRenderer.kt`** -> AI Confidence: **99.18%**
2248. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/classifiers/KaNamedClassOrObjectSymbolRenderer.kt`** -> AI Confidence: **99.18%**
2249. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/KaTypeRenderer.kt`** -> AI Confidence: **99.18%**
2250. **`analysis/decompiled/decompiler-native/src/org/jetbrains/kotlin/analysis/decompiler/konan/KlibMetadataStubBuilder.kt`** -> AI Confidence: **99.18%**
2251. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/KotlinClsStubBuilder.kt`** -> AI Confidence: **99.18%**
2252. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/KotlinMetadataStubBuilder.kt`** -> AI Confidence: **99.18%**
2253. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/KotlinBuiltInMetadataStubBuilder.kt`** -> AI Confidence: **99.18%**
2254. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/file/KtDecompiledFile.kt`** -> AI Confidence: **99.18%**
2255. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/CallableClsStubBuilder.kt`** -> AI Confidence: **99.18%**
2256. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtDefaultAnnotationArgumentReference.kt`** -> AI Confidence: **99.18%**
2257. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/LLResolutionFacade.kt`** -> AI Confidence: **99.18%**
2258. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/targets/LLFirResolveTarget.kt`** -> AI Confidence: **99.18%**
2259. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/targets/LLFirWholeElementResolveTarget.kt`** -> AI Confidence: **99.18%**
2260. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/FileStructureElementDiagnosticRetriever.kt`** -> AI Confidence: **99.18%**
2261. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/LLFirDiagnosticVisitor.kt`** -> AI Confidence: **99.18%**
2262. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirIdeRegisteredPluginAnnotations.kt`** -> AI Confidence: **99.18%**
2263. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirProvider.kt`** -> AI Confidence: **99.18%**
2264. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/providerUtils.kt`** -> AI Confidence: **99.18%**
2265. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/resolve/extensions/LLFirResolveExtensionTool.kt`** -> AI Confidence: **99.18%**
2266. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/resolver/AllCandidatesResolver.kt`** -> AI Confidence: **99.18%**
2267. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirSession.kt`** -> AI Confidence: **99.18%**
2268. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/JvmStubDeserializedBuiltInsContainerSource.kt`** -> AI Confidence: **99.18%**
2269. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinStubBasedLibraryMultifileClassPartCallableSymbolProvider.kt`** -> AI Confidence: **99.18%**
2270. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLModuleWithDependenciesSymbolProvider.kt`** -> AI Confidence: **99.18%**
2271. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLNativeForwardDeclarationsSymbolProvider.kt`** -> AI Confidence: **99.18%**
2272. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/utils.kt`** -> AI Confidence: **99.18%**
2273. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirReturnTypeCalculatorWithJump.kt`** -> AI Confidence: **99.18%**
2274. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/TestSuppressor.kt`** -> AI Confidence: **99.18%**
2275. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/firTestUtils.kt`** -> AI Confidence: **99.18%**
2276. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/services/ErrorResistanceServiceRegistrar.kt`** -> AI Confidence: **99.18%**
2277. **`analysis/stubs/testFixtures/org/jetbrains/kotlin/analysis/stubs/StubsTestEngine.kt`** -> AI Confidence: **99.18%**
2278. **`build-common/src/org/jetbrains/kotlin/incremental/IncrementalJvmCache.kt`** -> AI Confidence: **99.18%**
2279. **`build-common/src/org/jetbrains/kotlin/incremental/JavaClassesSerializerExtension.kt`** -> AI Confidence: **99.18%**
2280. **`build-common/src/org/jetbrains/kotlin/incremental/storage/externalizers.kt`** -> AI Confidence: **99.18%**
2281. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/serialization/json/base/AllNamedTypeSerializer.kt`** -> AI Confidence: **99.18%**
2282. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/serialization/json/kotlinReleaseVersionSerializers.kt`** -> AI Confidence: **99.18%**
2283. **`compiler/backend/src/org/jetbrains/kotlin/codegen/OriginCollectingClassBuilderFactory.kt`** -> AI Confidence: **99.18%**
2284. **`compiler/backend/src/org/jetbrains/kotlin/codegen/classFileUtils.kt`** -> AI Confidence: **99.18%**
2285. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/LambdaInfo.kt`** -> AI Confidence: **99.18%**
2286. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/inlineIntrinsics.kt`** -> AI Confidence: **99.18%**
2287. **`compiler/backend/src/org/jetbrains/kotlin/codegen/serialization/JvmCodegenStringTable.kt`** -> AI Confidence: **99.18%**
2288. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/AbiStabilityModeConversionTest.kt`** -> AI Confidence: **99.18%**
2289. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/AnnotationDefaultTargetModeConversionTest.kt`** -> AI Confidence: **99.18%**
2290. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/AssertionsModeConversionTest.kt`** -> AI Confidence: **99.18%**
2291. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/CompatqualAnnotationsModeConversionTest.kt`** -> AI Confidence: **99.18%**
2292. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/JdkReleaseConversionTest.kt`** -> AI Confidence: **99.18%**
2293. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/JspecifyAnnotationsModeConversionTest.kt`** -> AI Confidence: **99.18%**
2294. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/JvmDefaultModeConversionTest.kt`** -> AI Confidence: **99.18%**
2295. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/NameBasedDestructuringModeConversionTest.kt`** -> AI Confidence: **99.18%**
2296. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/StringConcatModeConversionTest.kt`** -> AI Confidence: **99.18%**
2297. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/VerifyIrModeConversionTest.kt`** -> AI Confidence: **99.18%**
2298. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/WhenExpressionsModeConversionTest.kt`** -> AI Confidence: **99.18%**
2299. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/BtaVersionsCompilationTestArgumentProvider.kt`** -> AI Confidence: **99.18%**
2300. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/DefaultStrategyAgnosticCompilationTestArgumentProvider.kt`** -> AI Confidence: **99.18%**
2301. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/IncrementalCompilationSmokeTest.kt`** -> AI Confidence: **99.18%**
2302. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/AbiStabilityModeConversionTest.kt`** -> AI Confidence: **99.18%**
2303. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/AssertionsModeConversionTest.kt`** -> AI Confidence: **99.18%**
2304. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/CompatqualAnnotationsModeConversionTest.kt`** -> AI Confidence: **99.18%**
2305. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/IgnoredAnnotationsForBridgesConversionTest.kt`** -> AI Confidence: **99.18%**
2306. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/JdkReleaseConversionTest.kt`** -> AI Confidence: **99.18%**
2307. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/JspecifyAnnotationsModeConversionTest.kt`** -> AI Confidence: **99.18%**
2308. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/JvmDefaultModeConversionTest.kt`** -> AI Confidence: **99.18%**
2309. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/LambdasModeConversionTest.kt`** -> AI Confidence: **99.18%**
2310. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/ProfileCompilerCommandConversionTest.kt`** -> AI Confidence: **99.18%**
2311. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/SamConversionsModeConversionTest.kt`** -> AI Confidence: **99.18%**
2312. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/StringConcatModeConversionTest.kt`** -> AI Confidence: **99.18%**
2313. **`compiler/build-tools/kotlin-build-tools-compat/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/compat/KotlinToolchainsV1Adapter.kt`** -> AI Confidence: **99.18%**
2314. **`compiler/build-tools/kotlin-build-tools-cri-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/cri/CriDataDeserializerImpl.kt`** -> AI Confidence: **99.18%**
2315. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/BuildToolsApiBuildICReporter.kt`** -> AI Confidence: **99.18%**
2316. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/icAdapters.kt`** -> AI Confidence: **99.18%**
2317. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/argumentTransforms.kt`** -> AI Confidence: **99.18%**
2318. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/constantsAndUtils.kt`** -> AI Confidence: **99.18%**
2319. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/CliKotlinAsJavaSupport.kt`** -> AI Confidence: **99.18%**
2320. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/KotlinCoreEnvironment.kt`** -> AI Confidence: **99.18%**
2321. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/jarfs/FastJarFileSystem.kt`** -> AI Confidence: **99.18%**
2322. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/jarfs/FastJarVirtualFile.kt`** -> AI Confidence: **99.18%**
2323. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/config/JvmContentRoots.kt`** -> AI Confidence: **99.18%**
2324. **`compiler/cli/cli-jklib/src/org/jetbrains/kotlin/cli/jklib/FirJKlibSessionFactory.kt`** -> AI Confidence: **99.18%**
2325. **`compiler/cli/cli-jklib/src/org/jetbrains/kotlin/cli/jklib/pipeline/JKlibPipelinePhases.kt`** -> AI Confidence: **99.18%**
2326. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebBackendPipelinePhase.kt`** -> AI Confidence: **99.18%**
2327. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebCliPipeline.kt`** -> AI Confidence: **99.18%**
2328. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebKlibSerializationPipelinePhase.kt`** -> AI Confidence: **99.18%**
2329. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/js/JsBackendPipelinePhase.kt`** -> AI Confidence: **99.18%**
2330. **`compiler/cli/cli-jvm/javac-integration/src/org/jetbrains/kotlin/cli/jvm/javac/JavacWrapperRegistrar.kt`** -> AI Confidence: **99.18%**
2331. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/TopDownAnalyzerFacadeForJVM.kt`** -> AI Confidence: **99.18%**
2332. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/jvmArguments.kt`** -> AI Confidence: **99.18%**
2333. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmBackendPipelinePhase.kt`** -> AI Confidence: **99.18%**
2334. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/AbstractMetadataSerializer.kt`** -> AI Confidence: **99.18%**
2335. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/CommonAnalysis.kt`** -> AI Confidence: **99.18%**
2336. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/K1LegacyMetadataSerializer.kt`** -> AI Confidence: **99.18%**
2337. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/KotlinMetadataCompiler.kt`** -> AI Confidence: **99.18%**
2338. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/pipeline/metadata/MetadataLegacySerializerPhase.kt`** -> AI Confidence: **99.18%**
2339. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeFir2IrPipelinePhase.kt`** -> AI Confidence: **99.18%**
2340. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeKlibIrPhase.kt`** -> AI Confidence: **99.18%**
2341. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/PipelineActions.kt`** -> AI Confidence: **99.18%**
2342. **`compiler/compiler-runner-unshaded/src/org/jetbrains/kotlin/compilerRunner/CompilerOutputParser.kt`** -> AI Confidence: **99.18%**
2343. **`compiler/config/configuration-keys-generator/src/org/jetbrains/kotlin/config/keys/generator/model/KeysContainer.kt`** -> AI Confidence: **99.18%**
2344. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/NonSuppressibleErrorNamesGenerator.kt`** -> AI Confidence: **99.18%**
2345. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/model/ErrorListDiagnosticListRenderer.kt`** -> AI Confidence: **99.18%**
2346. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/diagnostics/js/FirJsErrorsDefaultMessages.kt`** -> AI Confidence: **99.18%**
2347. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsDynamicDeclarationChecker.kt`** -> AI Confidence: **99.18%**
2348. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExternalInheritorOnlyChecker.kt`** -> AI Confidence: **99.18%**
2349. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsInheritanceFunctionChecker.kt`** -> AI Confidence: **99.18%**
2350. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsMultipleInheritanceChecker.kt`** -> AI Confidence: **99.18%**
2351. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsExternalArgumentCallChecker.kt`** -> AI Confidence: **99.18%**
2352. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/FirJvmAnnotationHelper.kt`** -> AI Confidence: **99.18%**
2353. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/FirJvmInlineCheckerComponent.kt`** -> AI Confidence: **99.18%**
2354. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmConflictsChecker.kt`** -> AI Confidence: **99.18%**
2355. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmInlineApplicabilityChecker.kt`** -> AI Confidence: **99.18%**
2356. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmRedundantRepeatableChecker.kt`** -> AI Confidence: **99.18%**
2357. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmThrowsChecker.kt`** -> AI Confidence: **99.18%**
2358. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirSynchronizedAnnotationChecker.kt`** -> AI Confidence: **99.18%**
2359. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaClassInheritsKtPrivateClassExpressionChecker.kt`** -> AI Confidence: **99.18%**
2360. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaGenericVarianceViolationTypeChecker.kt`** -> AI Confidence: **99.18%**
2361. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaUnnecessaryNotNullChecker.kt`** -> AI Confidence: **99.18%**
2362. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmSerializableLambdaChecker.kt`** -> AI Confidence: **99.18%**
2363. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirUnsupportedSyntheticCallableReferenceChecker.kt`** -> AI Confidence: **99.18%**
2364. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/type/FirArrayOfNullableNothingTypeChecker.kt`** -> AI Confidence: **99.18%**
2365. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeForwardDeclarationGetClassCallChecker.kt`** -> AI Confidence: **99.18%**
2366. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeHelpers.kt`** -> AI Confidence: **99.18%**
2367. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCActionChecker.kt`** -> AI Confidence: **99.18%**
2368. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCNameOverridesChecker.kt`** -> AI Confidence: **99.18%**
2369. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCOutletChecker.kt`** -> AI Confidence: **99.18%**
2370. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCVariadicMethodOverrideChecker.kt`** -> AI Confidence: **99.18%**
2371. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeVariadicCallableReferenceChecker.kt`** -> AI Confidence: **99.18%**
2372. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/expression/FirWasmDefinedExternallyCallChecker.kt`** -> AI Confidence: **99.18%**
2373. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirWebCommonNativeAnnotationCheckers.kt`** -> AI Confidence: **99.18%**
2374. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirJsQualifierChecker.kt`** -> AI Confidence: **99.18%**
2375. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirKeywordUtils.kt`** -> AI Confidence: **99.18%**
2376. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/SourceHelpers.kt`** -> AI Confidence: **99.18%**
2377. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/context/CheckerContext.kt`** -> AI Confidence: **99.18%**
2378. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/context/MutableCheckerContext.kt`** -> AI Confidence: **99.18%**
2379. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnnotationClassInheritanceChecker.kt`** -> AI Confidence: **99.18%**
2380. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnyDeprecationChecker.kt`** -> AI Confidence: **99.18%**
2381. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirBadInheritedJavaSignaturesChecker.kt`** -> AI Confidence: **99.18%**
2382. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCompanionBlockChecker.kt`** -> AI Confidence: **99.18%**
2383. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCompanionBlockMemberChecker.kt`** -> AI Confidence: **99.18%**
2384. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDelegationSuperCallInEnumConstructorChecker.kt`** -> AI Confidence: **99.18%**
2385. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirEnumEntryInitializationChecker.kt`** -> AI Confidence: **99.18%**
2386. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExpectActualClassifiersAreInBetaChecker.kt`** -> AI Confidence: **99.18%**
2387. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirLargeArityFunctionImportChecker.kt`** -> AI Confidence: **99.18%**
2388. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirLocalExtensionPropertyChecker.kt`** -> AI Confidence: **99.18%**
2389. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirManyCompanionObjectsChecker.kt`** -> AI Confidence: **99.18%**
2390. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMissingDependencyClassForLambdaReceiverChecker.kt`** -> AI Confidence: **99.18%**
2391. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMissingDependencySupertypeInDeclarationsChecker.kt`** -> AI Confidence: **99.18%**
2392. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMixedFunctionalTypesInSupertypesChecker.kt`** -> AI Confidence: **99.18%**
2393. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptInAnnotationClassChecker.kt`** -> AI Confidence: **99.18%**
2394. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptInEnumEntryChecker.kt`** -> AI Confidence: **99.18%**
2395. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPropertyInitializationChecker.kt`** -> AI Confidence: **99.18%**
2396. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirRequiresOptInOnExpectChecker.kt`** -> AI Confidence: **99.18%**
2397. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirSealedInterfaceAllowedChecker.kt`** -> AI Confidence: **99.18%**
2398. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirVolatileAnnotationChecker.kt`** -> AI Confidence: **99.18%**
2399. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/experimental/RedundantInterpolationPrefixCheckerLiteral.kt`** -> AI Confidence: **99.18%**
2400. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirAssignmentOperatorCallChecker.kt`** -> AI Confidence: **99.18%**
2401. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirBreakOrContinueJumpsAcrossFunctionBoundaryChecker.kt`** -> AI Confidence: **99.18%**
2402. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirConstructorCallChecker.kt`** -> AI Confidence: **99.18%**
2403. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCustomEnumEntriesMigrationQualifierChecker.kt`** -> AI Confidence: **99.18%**
2404. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCustomEnumEntriesMigrationReferenceChecker.kt`** -> AI Confidence: **99.18%**
2405. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptInUsageQualifierChecker.kt`** -> AI Confidence: **99.18%**
2406. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirPrivateToThisAccessChecker.kt`** -> AI Confidence: **99.18%**
2407. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirReceiverAccessBeforeSuperCallChecker.kt`** -> AI Confidence: **99.18%**
2408. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSealedClassConstructorCallChecker.kt`** -> AI Confidence: **99.18%**
2409. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTrimMarginBlankPrefixChecker.kt`** -> AI Confidence: **99.18%**
2410. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirWhenSubjectChecker.kt`** -> AI Confidence: **99.18%**
2411. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/RedundantCallOfConversionMethodChecker.kt`** -> AI Confidence: **99.18%**
2412. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/FirAnonymousUnusedParamChecker.kt`** -> AI Confidence: **99.18%**
2413. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/UselessCallOnNotNullChecker.kt`** -> AI Confidence: **99.18%**
2414. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirCommaInWhenConditionChecker.kt`** -> AI Confidence: **99.18%**
2415. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirFunctionTypeParametersSyntaxChecker.kt`** -> AI Confidence: **99.18%**
2416. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirLocalVariableTypeParametersSyntaxChecker.kt`** -> AI Confidence: **99.18%**
2417. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirArrayOfNothingTypeChecker.kt`** -> AI Confidence: **99.18%**
2418. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDefinitelyNotNullableChecker.kt`** -> AI Confidence: **99.18%**
2419. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDslMarkerPropagationChecker.kt`** -> AI Confidence: **99.18%**
2420. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDuplicateParameterNameInFunctionTypeChecker.kt`** -> AI Confidence: **99.18%**
2421. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirKotlinActualAnnotationHasNoEffectInKotlinTypeChecker.kt`** -> AI Confidence: **99.18%**
2422. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/Fir2KlibMetadataSerializer.kt`** -> AI Confidence: **99.18%**
2423. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/firUtils.kt`** -> AI Confidence: **99.18%**
2424. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirJvmSessionFactory.kt`** -> AI Confidence: **99.18%**
2425. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirMetadataSessionFactory.kt`** -> AI Confidence: **99.18%**
2426. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirSessionConfigurator.kt`** -> AI Confidence: **99.18%**
2427. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/KlibBasedSymbolProvider.kt`** -> AI Confidence: **99.18%**
2428. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/KlibIcCacheBasedSymbolProvider.kt`** -> AI Confidence: **99.18%**
2429. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/MetadataSymbolProvider.kt`** -> AI Confidence: **99.18%**
2430. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/NativeForwardDeclarationsSymbolProvider.kt`** -> AI Confidence: **99.18%**
2431. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/AnnotationDeserializerWithProtocol.kt`** -> AI Confidence: **99.18%**
2432. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaClass.kt`** -> AI Confidence: **99.18%**
2433. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaConstructor.kt`** -> AI Confidence: **99.18%**
2434. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/FirJvmDeserializationExtension.kt`** -> AI Confidence: **99.18%**
2435. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/firBuiltinSymbolProviders.kt`** -> AI Confidence: **99.18%**
2436. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaAnnotationSyntheticPropertiesScope.kt`** -> AI Confidence: **99.18%**
2437. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/resolve/FirJavaClassMapper.kt`** -> AI Confidence: **99.18%**
2438. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirAnnotationSerializer.kt`** -> AI Confidence: **99.18%**
2439. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirDirectJavaActualDeclarationExtractor.kt`** -> AI Confidence: **99.18%**
2440. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmBackendClassResolver.kt`** -> AI Confidence: **99.18%**
2441. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/JvmFir2IrExtensions.kt`** -> AI Confidence: **99.18%**
2442. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrScopeCache.kt`** -> AI Confidence: **99.18%**
2443. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/FirProviderWithGeneratedFiles.kt`** -> AI Confidence: **99.18%**
2444. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/ConstantUtils.kt`** -> AI Confidence: **99.18%**
2445. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/IrElementsCreationUtils.kt`** -> AI Confidence: **99.18%**
2446. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/descriptors/FirModuleDescriptor.kt`** -> AI Confidence: **99.18%**
2447. **`compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/generators/tests/GenerateModularizedIsolatedTests.kt`** -> AI Confidence: **99.18%**
2448. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/ClassBuildingContext.kt`** -> AI Confidence: **99.18%**
2449. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/ConstructorBuildingContext.kt`** -> AI Confidence: **99.18%**
2450. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/PropertyBuildingContext.kt`** -> AI Confidence: **99.18%**
2451. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/extensions/utils/AbstractSimpleClassPredicateMatchingService.kt`** -> AI Confidence: **99.18%**
2452. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/calls/FirReceivers.kt`** -> AI Confidence: **99.18%**
2453. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirCachingCompositeSymbolProvider.kt`** -> AI Confidence: **99.18%**
2454. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/transformers/ReturnTypeCalculatorForFullBodyResolve.kt`** -> AI Confidence: **99.18%**
2455. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/FirIntersectionScopeOverrideChecker.kt`** -> AI Confidence: **99.18%**
2456. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirAbstractSimpleImportingScope.kt`** -> AI Confidence: **99.18%**
2457. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirAbstractStarImportingScope.kt`** -> AI Confidence: **99.18%**
2458. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirClassAnySynthesizedMemberScope.kt`** -> AI Confidence: **99.18%**
2459. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirDefaultStarImportingScope.kt`** -> AI Confidence: **99.18%**
2460. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirLazyNestedClassifierScope.kt`** -> AI Confidence: **99.18%**
2461. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirLocalScope.kt`** -> AI Confidence: **99.18%**
2462. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirNestedClassifierScope.kt`** -> AI Confidence: **99.18%**
2463. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/fir/WhenEntry.kt`** -> AI Confidence: **99.18%**
2464. **`compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiConversionUtils.kt`** -> AI Confidence: **99.18%**
2465. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirStatusTransformerExtension.kt`** -> AI Confidence: **99.18%**
2466. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/ResolveUtils.kt`** -> AI Confidence: **99.18%**
2467. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/QualifierReceiver.kt`** -> AI Confidence: **99.18%**
2468. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/TowerResolveManager.kt`** -> AI Confidence: **99.18%**
2469. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirImportResolveTransformer.kt`** -> AI Confidence: **99.18%**
2470. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirImplicitBodyResolve.kt`** -> AI Confidence: **99.18%**
2471. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/mpp/FirExpectActualMatcherTransformer.kt`** -> AI Confidence: **99.18%**
2472. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/mpp/FirExpectActualResolver.kt`** -> AI Confidence: **99.18%**
2473. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/ContextSensitiveResolution.kt`** -> AI Confidence: **99.18%**
2474. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/model.kt`** -> AI Confidence: **99.18%**
2475. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/FirGeneration.kt`** -> AI Confidence: **99.18%**
2476. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/FirSession.kt`** -> AI Confidence: **99.18%**
2477. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/Primitives.kt`** -> AI Confidence: **99.18%**
2478. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/DeprecationsProvider.kt`** -> AI Confidence: **99.18%**
2479. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/impl/FirDeclarationStatusImpl.kt`** -> AI Confidence: **99.18%**
2480. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/diagnostics/ConeSimpleDiagnostic.kt`** -> AI Confidence: **99.18%**
2481. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/builder/FirAnnotationArgumentMappingBuilder.kt`** -> AI Confidence: **99.18%**
2482. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/impl/FirResolvedArgumentList.kt`** -> AI Confidence: **99.18%**
2483. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/FirVariableSymbol.kt`** -> AI Confidence: **99.18%**
2484. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/ParameterNameTypeAttribute.kt`** -> AI Confidence: **99.18%**
2485. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/utils/exceptions/firExceptionUtils.kt`** -> AI Confidence: **99.18%**
2486. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/ImplementationConfigurator.kt`** -> AI Confidence: **99.18%**
2487. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PsiPositioningStrategies.kt`** -> AI Confidence: **99.18%**
2488. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/rendering/CommonRenderers.kt`** -> AI Confidence: **99.18%**
2489. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaElementCollectionFromPsiArrayUtil.kt`** -> AI Confidence: **99.18%**
2490. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/ClassifierResolutionContext.kt`** -> AI Confidence: **99.18%**
2491. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/PackagePartClassUtils.kt`** -> AI Confidence: **99.18%**
2492. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/AbstractJavaClassFinder.kt`** -> AI Confidence: **99.18%**
2493. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/components/LazyResolveBasedCache.kt`** -> AI Confidence: **99.18%**
2494. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/kotlin/incremental/IncrementalPackagePartProvider.kt`** -> AI Confidence: **99.18%**
2495. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmAdditionalClassPartsProvider.kt`** -> AI Confidence: **99.18%**
2496. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmPlatformAnnotationFeaturesSupport.kt`** -> AI Confidence: **99.18%**
2497. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ExplicitMetadataChecker.kt`** -> AI Confidence: **99.18%**
2498. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SamInterfaceConstructorReferenceCallChecker.kt`** -> AI Confidence: **99.18%**
2499. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SuperCallWithDefaultArgumentsChecker.kt`** -> AI Confidence: **99.18%**
2500. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/platform/JavaGenericVarianceViolationTypeChecker.kt`** -> AI Confidence: **99.18%**
2501. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/instructions/jumps/ConditionalJumpInstruction.kt`** -> AI Confidence: **99.18%**
2502. **`compiler/frontend/src/org/jetbrains/kotlin/cfg/cfgContainingDeclarationUtils.kt`** -> AI Confidence: **99.18%**
2503. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/diagnostics/factories/DebugInfoDiagnosticFactory1.kt`** -> AI Confidence: **99.18%**
2504. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/ESDataFlowValue.kt`** -> AI Confidence: **99.18%**
2505. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/adaptiveClassifierNamePolicy.kt`** -> AI Confidence: **99.18%**
2506. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnalyzingUtils.kt`** -> AI Confidence: **99.18%**
2507. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/CompositeBindingContext.kt`** -> AI Confidence: **99.18%**
2508. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DelegateInferenceSession.kt`** -> AI Confidence: **99.18%**
2509. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/RecursiveContractHelper.kt`** -> AI Confidence: **99.18%**
2510. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/AbstractClassInstantiationChecker.kt`** -> AI Confidence: **99.18%**
2511. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/SuspendConversionCallChecker.kt`** -> AI Confidence: **99.18%**
2512. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/results/FlatSignatureForResolvedCall.kt`** -> AI Confidence: **99.18%**
2513. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/PSIKotlinCalls.kt`** -> AI Confidence: **99.18%**
2514. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/codegen/FunctionsFromAnyGenerator.kt`** -> AI Confidence: **99.18%**
2515. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/declarations/AbstractPsiBasedDeclarationProvider.kt`** -> AI Confidence: **99.18%**
2516. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/declarations/DeclarationProviderFactoryService.kt`** -> AI Confidence: **99.18%**
2517. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyAnnotations.kt`** -> AI Confidence: **99.18%**
2518. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyTypeAliasDescriptor.kt`** -> AI Confidence: **99.18%**
2519. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/scopes/LocalRedeclarationChecker.kt`** -> AI Confidence: **99.18%**
2520. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/FakeCallResolver.kt`** -> AI Confidence: **99.18%**
2521. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/ValueParameterResolver.kt`** -> AI Confidence: **99.18%**
2522. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/AbiSnapshot.kt`** -> AI Confidence: **99.18%**
2523. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/CompilerRunnerUtils.kt`** -> AI Confidence: **99.18%**
2524. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalJvmCompilerRunnerBase.kt`** -> AI Confidence: **99.18%**
2525. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/InputsCache.kt`** -> AI Confidence: **99.18%**
2526. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/impl/InlinedClassSnapshotter.kt`** -> AI Confidence: **99.18%**
2527. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/dirtyFiles/JvmSourcesToCompileCalculator.kt`** -> AI Confidence: **99.18%**
2528. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/IrElementTransformerVoidWithContext.kt`** -> AI Confidence: **99.18%**
2529. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/Lower.kt`** -> AI Confidence: **99.18%**
2530. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/ValueRemapper.kt`** -> AI Confidence: **99.18%**
2531. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ArrayConstructorLowering.kt`** -> AI Confidence: **99.18%**
2532. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/DelegatedPropertyOptimizationLowering.kt`** -> AI Confidence: **99.18%**
2533. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/SpecialBridgeMethods.kt`** -> AI Confidence: **99.18%**
2534. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/KlibSyntheticAccessorGenerator.kt`** -> AI Confidence: **99.18%**
2535. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/RangeUntilHandler.kt`** -> AI Confidence: **99.18%**
2536. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/UntilHandler.kt`** -> AI Confidence: **99.18%**
2537. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/phaser/PhaseFactories.kt`** -> AI Confidence: **99.18%**
2538. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/JsLoweringPhases.kt`** -> AI Confidence: **99.18%**
2539. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/HashCalculatorForIC.kt`** -> AI Confidence: **99.18%**
2540. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ir/IrBuilder.kt`** -> AI Confidence: **99.18%**
2541. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/CopyAccessorBodyLowerings.kt`** -> AI Confidence: **99.18%**
2542. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/InlineObjectsWithPureInitializationLowering.kt`** -> AI Confidence: **99.18%**
2543. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsInnerClassesSupport.kt`** -> AI Confidence: **99.18%**
2544. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsInventNamesForLocalClasses.kt`** -> AI Confidence: **99.18%**
2545. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsReturnableBlockLowering.kt`** -> AI Confidence: **99.18%**
2546. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrepareCollectionsToExportLowering.kt`** -> AI Confidence: **99.18%**
2547. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrepareExportedDefaultImplementationsLowering.kt`** -> AI Confidence: **99.18%**
2548. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrepareValueClassesToBeExportedLowering.kt`** -> AI Confidence: **99.18%**
2549. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrivateMembersLowering.kt`** -> AI Confidence: **99.18%**
2550. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/SecondaryCtorLowering.kt`** -> AI Confidence: **99.18%**
2551. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/CallsLowering.kt`** -> AI Confidence: **99.18%**
2552. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/PrimitiveContainerMemberCallTransformer.kt`** -> AI Confidence: **99.18%**
2553. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/cleanup/CleanupLowering.kt`** -> AI Confidence: **99.18%**
2554. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsClassGenerator.kt`** -> AI Confidence: **99.18%**
2555. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/JsGenerationContext.kt`** -> AI Confidence: **99.18%**
2556. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/serialization/JsIrAstSerializer.kt`** -> AI Confidence: **99.18%**
2557. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrInlineCallGenerator.kt`** -> AI Confidence: **99.18%**
2558. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrInlineIntrinsicsSupport.kt`** -> AI Confidence: **99.18%**
2559. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/PrivateTypeFromNonPrivateInlineUsageChecker.kt`** -> AI Confidence: **99.18%**
2560. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/GetJavaObjectType.kt`** -> AI Confidence: **99.18%**
2561. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/HandleResultOfReflectiveAccess.kt`** -> AI Confidence: **99.18%**
2562. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IntrinsicFunction.kt`** -> AI Confidence: **99.18%**
2563. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IrCheckNotNull.kt`** -> AI Confidence: **99.18%**
2564. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IteratorNext.kt`** -> AI Confidence: **99.18%**
2565. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/JavaClassProperty.kt`** -> AI Confidence: **99.18%**
2566. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/NewArray.kt`** -> AI Confidence: **99.18%**
2567. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/FacadeClassSourceShimForFragmentCompilation.kt`** -> AI Confidence: **99.18%**
2568. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/JvmGeneratorExtensionsImpl.kt`** -> AI Confidence: **99.18%**
2569. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/OrphanedExpectUtils.kt`** -> AI Confidence: **99.18%**
2570. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/DirectInvokeLowering.kt`** -> AI Confidence: **99.18%**
2571. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/EnumExternalEntriesLowering.kt`** -> AI Confidence: **99.18%**
2572. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FragmentSharedVariablesLowering.kt`** -> AI Confidence: **99.18%**
2573. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InterfaceDefaultCallsLowering.kt`** -> AI Confidence: **99.18%**
2574. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmDefaultParameterInjector.kt`** -> AI Confidence: **99.18%**
2575. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmInventNamesForLocalClasses.kt`** -> AI Confidence: **99.18%**
2576. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmValueClassAbstractLowering.kt`** -> AI Confidence: **99.18%**
2577. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/MakePropertyDelegateMethodsStaticLowering.kt`** -> AI Confidence: **99.18%**
2578. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PatchLambdaOffsetsLowering.kt`** -> AI Confidence: **99.18%**
2579. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ResolveInlineCalls.kt`** -> AI Confidence: **99.18%**
2580. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SingletonOrConstantDelegationLowering.kt`** -> AI Confidence: **99.18%**
2581. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/StaticDefaultFunctionLowering.kt`** -> AI Confidence: **99.18%**
2582. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/indy/SamDelegatingLambdaBlock.kt`** -> AI Confidence: **99.18%**
2583. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmBackendContext.kt`** -> AI Confidence: **99.18%**
2584. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmIrTypeSystemContext.kt`** -> AI Confidence: **99.18%**
2585. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/Reporting.kt`** -> AI Confidence: **99.18%**
2586. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/Utils.kt`** -> AI Confidence: **99.18%**
2587. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TestProcessor.kt`** -> AI Confidence: **99.18%**
2588. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/dce/WasmUselessDeclarationsRemover.kt`** -> AI Confidence: **99.18%**
2589. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenContexts/WasmDeclarationCodegenContext.kt`** -> AI Confidence: **99.18%**
2590. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenContexts/WasmFunctionCodegenContext.kt`** -> AI Confidence: **99.18%**
2591. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/DeclarationGenerator.kt`** -> AI Confidence: **99.18%**
2592. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/TypeGenerator.kt`** -> AI Confidence: **99.18%**
2593. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/ExplicitlyCastExternalTypesLowering.kt`** -> AI Confidence: **99.18%**
2594. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/GenericReturnTypeLowering.kt`** -> AI Confidence: **99.18%**
2595. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/TryCatchCanonicalization.kt`** -> AI Confidence: **99.18%**
2596. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmCallableReferenceLowering.kt`** -> AI Confidence: **99.18%**
2597. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmPropertyReferenceLowering.kt`** -> AI Confidence: **99.18%**
2598. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/Annotations.kt`** -> AI Confidence: **99.18%**
2599. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/FunctionDefaultParametersActualizer.kt`** -> AI Confidence: **99.18%**
2600. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrActualizationErrors.kt`** -> AI Confidence: **99.18%**
2601. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/CommonLoweringPhases.kt`** -> AI Confidence: **99.18%**
2602. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/InlineFunctionSerializationPreProcessing.kt`** -> AI Confidence: **99.18%**
2603. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/stack/Frame.kt`** -> AI Confidence: **99.18%**
2604. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/Primitive.kt`** -> AI Confidence: **99.18%**
2605. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/AnonymousInitializerGenerator.kt`** -> AI Confidence: **99.18%**
2606. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DataClassMembersGenerator.kt`** -> AI Confidence: **99.18%**
2607. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DeclarationGenerator.kt`** -> AI Confidence: **99.18%**
2608. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/IrSyntheticDeclarationGenerator.kt`** -> AI Confidence: **99.18%**
2609. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ScriptGenerator.kt`** -> AI Confidence: **99.18%**
2610. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/StandaloneDeclarationGenerator.kt`** -> AI Confidence: **99.18%**
2611. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/SyntheticDeclarationsGenerator.kt`** -> AI Confidence: **99.18%**
2612. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/TypeTranslatorImpl.kt`** -> AI Confidence: **99.18%**
2613. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/lazy/IrLazyClass.kt`** -> AI Confidence: **99.18%**
2614. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/IrBuiltInsOverSymbolFinder.kt`** -> AI Confidence: **99.18%**
2615. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/SymbolFinder.kt`** -> AI Confidence: **99.18%**
2616. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/builders/ExpressionHelpers.kt`** -> AI Confidence: **99.18%**
2617. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/FakeOverrideBuilderStrategy.kt`** -> AI Confidence: **99.18%**
2618. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/ImplementationConfigurator.kt`** -> AI Confidence: **99.18%**
2619. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/IrTree.kt`** -> AI Confidence: **99.18%**
2620. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TransformerPrinter.kt`** -> AI Confidence: **99.18%**
2621. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TypeTransformerPrinter.kt`** -> AI Confidence: **99.18%**
2622. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TypeTransformerVoidPrinter.kt`** -> AI Confidence: **99.18%**
2623. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/context/CheckerContext.kt`** -> AI Confidence: **99.18%**
2624. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/expression/IrCallTypeChecker.kt`** -> AI Confidence: **99.18%**
2625. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/expression/IrCrossFileFieldUsageChecker.kt`** -> AI Confidence: **99.18%**
2626. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/expression/IrValueAccessScopeChecker.kt`** -> AI Confidence: **99.18%**
2627. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/MissingDeclarationStubGenerator.kt`** -> AI Confidence: **99.18%**
2628. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageSources.kt`** -> AI Confidence: **99.18%**
2629. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageSupportForLinkerImpl.kt`** -> AI Confidence: **99.18%**
2630. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageUtils.kt`** -> AI Confidence: **99.18%**
2631. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/overrides/FakeOverrideChecker.kt`** -> AI Confidence: **99.18%**
2632. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrFileDeserializer.kt`** -> AI Confidence: **99.18%**
2633. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrFileSerializer.kt`** -> AI Confidence: **99.18%**
2634. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrSymbolDeserializer.kt`** -> AI Confidence: **99.18%**
2635. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/mangle/descriptor/DescriptorMangleComputer.kt`** -> AI Confidence: **99.18%**
2636. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/checkers/JsKlibCheckers.kt`** -> AI Confidence: **99.18%**
2637. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/lower/serialization/ir/JsExportUtils.kt`** -> AI Confidence: **99.18%**
2638. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/lower/serialization/ir/JsIrLinker.kt`** -> AI Confidence: **99.18%**
2639. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanForwardDeclarationModuleDeserializer.kt`** -> AI Confidence: **99.18%**
2640. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanIrLinker.kt`** -> AI Confidence: **99.18%**
2641. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedAnnotation.kt`** -> AI Confidence: **99.18%**
2642. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedTypeParameter.kt`** -> AI Confidence: **99.18%**
2643. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightPsiLiteral.kt`** -> AI Confidence: **99.18%**
2644. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/lexer/KDocLexer.kt`** -> AI Confidence: **99.18%**
2645. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinParserDefinition.kt`** -> AI Confidence: **99.18%**
2646. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/ParseUtils.kt`** -> AI Confidence: **99.18%**
2647. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtClass.kt`** -> AI Confidence: **99.18%**
2648. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtConstructor.kt`** -> AI Confidence: **99.18%**
2649. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtContextReceiver.kt`** -> AI Confidence: **99.18%**
2650. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtEnumEntrySuperclassReferenceExpression.kt`** -> AI Confidence: **99.18%**
2651. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtNameReferenceExpression.kt`** -> AI Confidence: **99.18%**
2652. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtOperationReferenceExpression.kt`** -> AI Confidence: **99.18%**
2653. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtQualifiedExpression.kt`** -> AI Confidence: **99.18%**
2654. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/psiUtil/StringTemplateExpressionManipulator.kt`** -> AI Confidence: **99.18%**
2655. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtClassElementType.kt`** -> AI Confidence: **99.18%**
2656. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtConstantExpressionElementType.kt`** -> AI Confidence: **99.18%**
2657. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinConstantValue.kt`** -> AI Confidence: **99.18%**
2658. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinContractEffectStubImpl.kt`** -> AI Confidence: **99.18%**
2659. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinEnumEntryStubImpl.kt`** -> AI Confidence: **99.18%**
2660. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinPropertyStubImpl.kt`** -> AI Confidence: **99.18%**
2661. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinStubBaseImpl.kt`** -> AI Confidence: **99.18%**
2662. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/Utils.kt`** -> AI Confidence: **99.18%**
2663. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/NewConstraintSystem.kt`** -> AI Confidence: **99.18%**
2664. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/ConstraintSystemCompletionContext.kt`** -> AI Confidence: **99.18%**
2665. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/candidate/CallableReferenceResolutionCandidate.kt`** -> AI Confidence: **99.18%**
2666. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/ResolutionAtoms.kt`** -> AI Confidence: **99.18%**
2667. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/ResolvedCallAtoms.kt`** -> AI Confidence: **99.18%**
2668. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/util/functionTypeResolveUtils.kt`** -> AI Confidence: **99.18%**
2669. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/AnnotationSerializer.kt`** -> AI Confidence: **99.18%**
2670. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/nullabilityFromOverridden.fir.kt`** -> AI Confidence: **99.18%**
2671. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/nullabilityFromOverridden.kt`** -> AI Confidence: **99.18%**
2672. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/overridingDefaultQualifier.fir.kt`** -> AI Confidence: **99.18%**
2673. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/overridingDefaultQualifier.kt`** -> AI Confidence: **99.18%**
2674. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/nullabilityFromOverridden.kt`** -> AI Confidence: **99.18%**
2675. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/overridingDefaultQualifier.kt`** -> AI Confidence: **99.18%**
2676. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/resolve/lazy/JvmResolveUtil.kt`** -> AI Confidence: **99.18%**
2677. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/KlibMetadataPackageFragment.kt`** -> AI Confidence: **99.18%**
2678. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/impl/KlibMetadataDeserializedPackageFragmentsFactoryImpl.kt`** -> AI Confidence: **99.18%**
2679. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/impl/KlibMetadataModuleDescriptorFactoryImpl.kt`** -> AI Confidence: **99.18%**
2680. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/impl/KlibResolvedModuleDescriptorsFactoryImpl.kt`** -> AI Confidence: **99.18%**
2681. **`compiler/util-klib/src/org/jetbrains/kotlin/library/KlibLayoutReader.kt`** -> AI Confidence: **99.18%**
2682. **`compiler/util-klib/src/org/jetbrains/kotlin/library/KlibSizeInfo.kt`** -> AI Confidence: **99.18%**
2683. **`compiler/util-klib/src/org/jetbrains/kotlin/library/components/KlibIrComponent.kt`** -> AI Confidence: **99.18%**
2684. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/builtins/jvm/JavaToKotlinClassMap.kt`** -> AI Confidence: **99.18%**
2685. **`core/descriptors.jvm/src/org/jetbrains/kotlin/builtins/jvm/JvmBuiltInClassDescriptorFactory.kt`** -> AI Confidence: **99.18%**
2686. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/components/JavaAnnotationMapper.kt`** -> AI Confidence: **99.18%**
2687. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/descriptors/util.kt`** -> AI Confidence: **99.18%**
2688. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/LazyJavaPackageFragmentProvider.kt`** -> AI Confidence: **99.18%**
2689. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaClassMemberScope.kt`** -> AI Confidence: **99.18%**
2690. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaPackageFragment.kt`** -> AI Confidence: **99.18%**
2691. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/JavaFlexibleTypeDeserializer.kt`** -> AI Confidence: **99.18%**
2692. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/structure/ReflectJavaClassifierType.kt`** -> AI Confidence: **99.18%**
2693. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/constantValues.kt`** -> AI Confidence: **99.18%**
2694. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/GivenFunctionsMemberScope.kt`** -> AI Confidence: **99.18%**
2695. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/MemberScope.kt`** -> AI Confidence: **99.18%**
2696. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/TypeIntersectionScope.kt`** -> AI Confidence: **99.18%**
2697. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeSubstitution.kt`** -> AI Confidence: **99.18%**
2698. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/NewKotlinTypeChecker.kt`** -> AI Confidence: **99.18%**
2699. **`core/deserialization.common/src/org/jetbrains/kotlin/serialization/deserialization/MetadataUtil.kt`** -> AI Confidence: **99.18%**
2700. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/AbstractDeserializedPackageFragmentProvider.kt`** -> AI Confidence: **99.18%**
2701. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/AnnotationAndConstantLoaderImpl.kt`** -> AI Confidence: **99.18%**
2702. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedMemberDescriptor.kt`** -> AI Confidence: **99.18%**
2703. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedTypeParameterDescriptor.kt`** -> AI Confidence: **99.18%**
2704. **`core/reflection.jvm/src/kotlin/reflect/full/KTypes.kt`** -> AI Confidence: **99.18%**
2705. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/JavaAnnotationConstructor.kt`** -> AI Confidence: **99.18%**
2706. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/JavaKNamedFunction.kt`** -> AI Confidence: **99.18%**
2707. **`generators/tree-generator-common/src/org/jetbrains/kotlin/generators/tree/printer/common.kt`** -> AI Confidence: **99.18%**
2708. **`jps/jps-common/src/org/jetbrains/kotlin/platform/impl/JsIdePlatformKind.kt`** -> AI Confidence: **99.18%**
2709. **`jps/jps-common/src/org/jetbrains/kotlin/platform/impl/JvmIdePlatformKind.kt`** -> AI Confidence: **99.18%**
2710. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/incremental/JpsLookupStorage.kt`** -> AI Confidence: **99.18%**
2711. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsDefinedExternallyCallChecker.kt`** -> AI Confidence: **99.18%**
2712. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExternalInheritorOnlyChecker.kt`** -> AI Confidence: **99.18%**
2713. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsIdentifierChecker.kt`** -> AI Confidence: **99.18%**
2714. **`js/js.serializer/src/org/jetbrains/kotlin/serialization/js/kotlinJavascriptPackageFragmentProvider.kt`** -> AI Confidence: **99.18%**
2715. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/test/tools/SwcRunner.kt`** -> AI Confidence: **99.18%**
2716. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CacheStorage.kt`** -> AI Confidence: **99.18%**
2717. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/EntryPoint.kt`** -> AI Confidence: **99.18%**
2718. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/FeaturedLibraries.kt`** -> AI Confidence: **99.18%**
2719. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/TopDownAnalyzerFacadeForKonan.kt`** -> AI Confidence: **99.18%**
2720. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cexport/CAdapterCodegen.kt`** -> AI Confidence: **99.18%**
2721. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cgen/CBridgeGen.kt`** -> AI Confidence: **99.18%**
2722. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/CacheBuilding.kt`** -> AI Confidence: **99.18%**
2723. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/Frontend.kt`** -> AI Confidence: **99.18%**
2724. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/cstruct/CStructVarClassGenerator.kt`** -> AI Confidence: **99.18%**
2725. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/LlvmFunctionPrototype.kt`** -> AI Confidence: **99.18%**
2726. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/objcexport/WritableTypeInfo.kt`** -> AI Confidence: **99.18%**
2727. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/runtime/RuntimeLinkage.kt`** -> AI Confidence: **99.18%**
2728. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/CastsLowering.kt`** -> AI Confidence: **99.18%**
2729. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ContractsDslRemover.kt`** -> AI Confidence: **99.18%**
2730. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/DataClassOperatorsLowering.kt`** -> AI Confidence: **99.18%**
2731. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/GenericCallsReturnTypeEraser.kt`** -> AI Confidence: **99.18%**
2732. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InlineClassPropertyAccessorsLowering.kt`** -> AI Confidence: **99.18%**
2733. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InteropBridgesNameInventor.kt`** -> AI Confidence: **99.18%**
2734. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeAnnotationImplementationLowering.kt`** -> AI Confidence: **99.18%**
2735. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/PropertyReferenceLowering.kt`** -> AI Confidence: **99.18%**
2736. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ReturnsInsertionLowering.kt`** -> AI Confidence: **99.18%**
2737. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/SamSuperTypesChecker.kt`** -> AI Confidence: **99.18%**
2738. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/SpecialInteropIntrinsicsLowering.kt`** -> AI Confidence: **99.18%**
2739. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TestsInitializer.kt`** -> AI Confidence: **99.18%**
2740. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TypeOperatorLowering.kt`** -> AI Confidence: **99.18%**
2741. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/ExternalDeclarationFileNameProvider.kt`** -> AI Confidence: **99.18%**
2742. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanInteropModuleDeserializer.kt`** -> AI Confidence: **99.18%**
2743. **`kotlin-native/backend.native/tests/samples/objc/src/objcMain/kotlin/Window.kt`** -> AI Confidence: **99.18%**
2744. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/CompareDistributionSignatures.kt`** -> AI Confidence: **99.18%**
2745. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/nativeDistribution/NativeDistribution.kt`** -> AI Confidence: **99.18%**
2746. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/platformLibs/updateDefFileDependencies.kt`** -> AI Confidence: **99.18%**
2747. **`kotlin-native/performance/buildSrc/src/main/kotlin/CodeSizeTask.kt`** -> AI Confidence: **99.18%**
2748. **`kotlin-native/performance/buildSrc/src/main/kotlin/benchmark/BenchmarkingPlugin.kt`** -> AI Confidence: **99.18%**
2749. **`kotlin-native/prepare/kotlin-native-compiler-embeddable/tests/kotlin/org/jetbrains/kotlin/native/compiler/embeddable/CompilerEmbeddableSmokeTests.kt`** -> AI Confidence: **99.18%**
2750. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/internal/RuntimeUtils.kt`** -> AI Confidence: **99.18%**
2751. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/internal/reflect/KClassEx.kt`** -> AI Confidence: **99.18%**
2752. **`libraries/examples/annotation-processor-example/src/main/kotlin/example/ExampleAnnotationProcessor.kt`** -> AI Confidence: **99.18%**
2753. **`libraries/examples/scripting/jvm-embeddable-host/src/org/jetbrains/kotlin/script/examples/jvm/embeddable/host/host.kt`** -> AI Confidence: **99.18%**
2754. **`libraries/examples/scripting/jvm-simple-script/host/src/org/jetbrains/kotlin/script/examples/jvm/simple/host/host.kt`** -> AI Confidence: **99.18%**
2755. **`libraries/kotlin.test/common/src/main/kotlin/kotlin/test/Assertions.kt`** -> AI Confidence: **99.18%**
2756. **`libraries/kotlinx-metadata/jvm/src/kotlin/metadata/jvm/KotlinModuleMetadata.kt`** -> AI Confidence: **99.18%**
2757. **`libraries/kotlinx-metadata/klib/src/kotlinx/metadata/klib/KlibModuleMetadata.kt`** -> AI Confidence: **99.18%**
2758. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/common/KotlinCommonMetadata.kt`** -> AI Confidence: **99.18%**
2759. **`libraries/scripting/common/src/kotlin/script/experimental/util/propertiesCollection.kt`** -> AI Confidence: **99.18%**
2760. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/jsr223/KotlinJsr223ScriptEngineImpl.kt`** -> AI Confidence: **99.18%**
2761. **`libraries/stdlib/jdk7/src/kotlin/io/path/PathReadWrite.kt`** -> AI Confidence: **99.18%**
2762. **`libraries/stdlib/jvm/src/kotlin/internal/PlatformImplementations.kt`** -> AI Confidence: **99.18%**
2763. **`libraries/stdlib/jvm/src/kotlin/util/MathJVM.kt`** -> AI Confidence: **99.18%**
2764. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/AbiComparatorMain.kt`** -> AI Confidence: **99.18%**
2765. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/metadataUtils.kt`** -> AI Confidence: **99.18%**
2766. **`libraries/tools/abi-validation/kgp-integration-tests/src/test/kotlin/org/jetbrains/abi/tools/test/KlibVerificationTests.kt`** -> AI Confidence: **99.18%**
2767. **`libraries/tools/gradle/generators/native-cache-kotlin-version/src/main/kotlin/org/jetbrains/kotlin/gradle/generators/native/cache/version/NativeCacheKotlinVersionsGenerator.kt`** -> AI Confidence: **99.18%**
2768. **`libraries/tools/gradle/generators/native-cache-kotlin-version/src/test/kotlin/GenerateKotlinVersionTest.kt`** -> AI Confidence: **99.18%**
2769. **`libraries/tools/gradle/kotlin-gradle-ecosystem-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/ecosystem/KotlinEcosystemPlugin.kt`** -> AI Confidence: **99.18%**
2770. **`libraries/tools/kotlin-compose-compiler/src/common/kotlin/org/jetbrains/kotlin/compose/compiler/gradle/ComposeCompilerGradlePluginExtension.kt`** -> AI Confidence: **99.18%**
2771. **`libraries/tools/kotlin-gradle-plugin-dsl-codegen/src/main/kotlin/org/jetbrains/kotlin/generators/gradle/dsl/mppPresetFunctionsCodegen.kt`** -> AI Confidence: **99.18%**
2772. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinDependencyForwardCompatibilityTest.kt`** -> AI Confidence: **99.18%**
2773. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/IdeaKotlinExtraTest.kt`** -> AI Confidence: **99.18%**
2774. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/IdeaKotlinModelObjectGraphTest.kt`** -> AI Confidence: **99.18%**
2775. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/ReflectionTestUtils.kt`** -> AI Confidence: **99.18%**
2776. **`libraries/tools/kotlin-gradle-plugin-idea/src/testFixtures/kotlin/org/jetbrains/kotlin/gradle/idea/testFixtures/tcs/TestIdeaKotlinDependencySerializer.kt`** -> AI Confidence: **99.18%**
2777. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BuildCacheIT.kt`** -> AI Confidence: **99.18%**
2778. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ExecutionStrategyIT.kt`** -> AI Confidence: **99.18%**
2779. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KlibBasedMppIT.kt`** -> AI Confidence: **99.18%**
2780. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/Kotlin2JsGradlePluginIT.kt`** -> AI Confidence: **99.18%**
2781. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinDaemonJvmArgsTest.kt`** -> AI Confidence: **99.18%**
2782. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinSpecificDependenciesIT.kt`** -> AI Confidence: **99.18%**
2783. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MppIdeDependencyResolutionIT.kt`** -> AI Confidence: **99.18%**
2784. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/PgpHelpersTest.kt`** -> AI Confidence: **99.18%**
2785. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/TaskExecutionDiagnosticsIT.kt`** -> AI Confidence: **99.18%**
2786. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/TestFixturesIT.kt`** -> AI Confidence: **99.18%**
2787. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KT50161AndroidBuildCacheTest.kt`** -> AI Confidence: **99.18%**
2788. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KaptAndroidExternalIT.kt`** -> AI Confidence: **99.18%**
2789. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KotlinAndroidIT.kt`** -> AI Confidence: **99.18%**
2790. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/CheckXcodeTargetsConfigurationIT.kt`** -> AI Confidence: **99.18%**
2791. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportPersistentPackageLockIntegrationTests.kt`** -> AI Confidence: **99.18%**
2792. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportXcodeIntegrationIT.kt`** -> AI Confidence: **99.18%**
2793. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/XcodeDirectIntegrationIT.kt`** -> AI Confidence: **99.18%**
2794. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppDiagnosticsIt.kt`** -> AI Confidence: **99.18%**
2795. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppJvmWithJavaIT.kt`** -> AI Confidence: **99.18%**
2796. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/TestCancellationIT.kt`** -> AI Confidence: **99.18%**
2797. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/publication/prepareProjectForConsumption.kt`** -> AI Confidence: **99.18%**
2798. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/resources/MultiplatformResourcesPublicationIT.kt`** -> AI Confidence: **99.18%**
2799. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/resources/publicationProject.kt`** -> AI Confidence: **99.18%**
2800. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/AppleFrameworkIT.kt`** -> AI Confidence: **99.18%**
2801. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/KotlinNativeCompilerDownloadIT.kt`** -> AI Confidence: **99.18%**
2802. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/KotlinNativeDependenciesDownloadIT.kt`** -> AI Confidence: **99.18%**
2803. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/KotlinNativeDisableCacheIT.kt`** -> AI Confidence: **99.18%**
2804. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/NativeDownloadAndPlatformLibsIT.kt`** -> AI Confidence: **99.18%**
2805. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/NativeExternalDependenciesIT.kt`** -> AI Confidence: **99.18%**
2806. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/compilationAssertions.kt`** -> AI Confidence: **99.18%**
2807. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/problemsApiTestUtils.kt`** -> AI Confidence: **99.18%**
2808. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/testGradleBuildInjection.kt`** -> AI Confidence: **99.18%**
2809. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/xCodeVersion.kt`** -> AI Confidence: **99.18%**
2810. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/util/reportSourceSetCommonizerDependencies.kt`** -> AI Confidence: **99.18%**
2811. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/util/resolveIdeDependencies.kt`** -> AI Confidence: **99.18%**
2812. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/AndroidSimpleComposeApp/src/main/java/org/jetbrains/kotlin/android/example/ui/theme/Theme.kt`** -> AI Confidence: **99.18%**
2813. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/compilerPlugins/incrementalChangeInPlugin/plugin/src/main/kotlin/test/compiler/plugin/MyMethodGenerator.kt`** -> AI Confidence: **99.18%**
2814. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/androidx-navigation-safe-args/src/main/java/test/androidx/navigation/MainActivity.kt`** -> AI Confidence: **99.18%**
2815. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/scriptingComposeInterop/app/src/test/kotlin/script/ComposeMainKtsTest.kt`** -> AI Confidence: **99.18%**
2816. **`libraries/tools/kotlin-gradle-plugin-npm-versions-codegen/src/main/kotlin/org/jetbrains/kotlin/generators/gradle/targets/js/VersionFetcher.kt`** -> AI Confidence: **99.18%**
2817. **`libraries/tools/kotlin-gradle-plugin-npm-versions-codegen/src/main/kotlin/org/jetbrains/kotlin/generators/gradle/targets/js/main.kt`** -> AI Confidence: **99.18%**
2818. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/CompilerSystemPropertiesService.kt`** -> AI Confidence: **99.18%**
2819. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleCompilerRunnerWithWorkers.kt`** -> AI Confidence: **99.18%**
2820. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/artifacts/KotlinMetadataArtifact.kt`** -> AI Confidence: **99.18%**
2821. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/KotlinSourceSetConvention.kt`** -> AI Confidence: **99.18%**
2822. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/KotlinDependenciesManagement.kt`** -> AI Confidence: **99.18%**
2823. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/subpluginUtils.kt`** -> AI Confidence: **99.18%**
2824. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinCompilationProcessor.kt`** -> AI Confidence: **99.18%**
2825. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSetProcessor.kt`** -> AI Confidence: **99.18%**
2826. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinTargetConfigurator.kt`** -> AI Confidence: **99.18%**
2827. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ProblemsReporter.kt`** -> AI Confidence: **99.18%**
2828. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/CInteropInputChecker.kt`** -> AI Confidence: **99.18%**
2829. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/ComposePluginSuggestApplyChecker.kt`** -> AI Confidence: **99.18%**
2830. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/IncorrectCompileOnlyDependenciesChecker.kt`** -> AI Confidence: **99.18%**
2831. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/KmpPartiallyResolvedDependenciesChecker.kt`** -> AI Confidence: **99.18%**
2832. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/MultipleSourceSetRootsInCompilationChecker.kt`** -> AI Confidence: **99.18%**
2833. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/NativeVersionChecker.kt`** -> AI Confidence: **99.18%**
2834. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/IdeAdditionalArtifactResolver.kt`** -> AI Confidence: **99.18%**
2835. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/IdeMultiplatformImportImpl.kt`** -> AI Confidence: **99.18%**
2836. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeCommonizedNativePlatformDependencyResolver.kt`** -> AI Confidence: **99.18%**
2837. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeJvmAndAndroidSourceDependencyResolver.kt`** -> AI Confidence: **99.18%**
2838. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/factories.kt`** -> AI Confidence: **99.18%**
2839. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/internal/MavenPublicationComponentAccessor.kt`** -> AI Confidence: **99.18%**
2840. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinCompilationFactory.kt`** -> AI Confidence: **99.18%**
2841. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/MetadataDependencyTransformationTask.kt`** -> AI Confidence: **99.18%**
2842. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/ProjectMetadataProviderImpl.kt`** -> AI Confidence: **99.18%**
2843. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/CopyDsymDuringArchiving.kt`** -> AI Confidence: **99.18%**
2844. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/CreateBuildSystemDirectory.kt`** -> AI Confidence: **99.18%**
2845. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/XCFrameworkTask.kt`** -> AI Confidence: **99.18%**
2846. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/XcodeVersionTask.kt`** -> AI Confidence: **99.18%**
2847. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/internal/SwiftExportAction.kt`** -> AI Confidence: **99.18%**
2848. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/CheckCocoaPodsHasNoSwiftPMDependencies.kt`** -> AI Confidence: **99.18%**
2849. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/swiftPMDependenciesMetadata.kt`** -> AI Confidence: **99.18%**
2850. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/syncPackageSwiftLock.kt`** -> AI Confidence: **99.18%**
2851. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/xcodeProjectParsing.kt`** -> AI Confidence: **99.18%**
2852. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/CreateCInteropTasksSideEffect.kt`** -> AI Confidence: **99.18%**
2853. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationCompilerOptionsConfigurator.kt`** -> AI Confidence: **99.18%**
2854. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationImpl.kt`** -> AI Confidence: **99.18%**
2855. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/factory/KotlinCompilationSourceSetsContainerFactories.kt`** -> AI Confidence: **99.18%**
2856. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/internal/projectStructureMetadataConfiguration.kt`** -> AI Confidence: **99.18%**
2857. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/kotlinCompilations.kt`** -> AI Confidence: **99.18%**
2858. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/KotlinTargetResourcesPublicationImpl.kt`** -> AI Confidence: **99.18%**
2859. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/publication/KotlinAndroidTargetResourcesPublication.kt`** -> AI Confidence: **99.18%**
2860. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/publication/KotlinJvmTargetResourcesPublication.kt`** -> AI Confidence: **99.18%**
2861. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/consumption/UnzippedUklibToPlatformCompilationTransform.kt`** -> AI Confidence: **99.18%**
2862. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/publication/UklibFromKGPModel.kt`** -> AI Confidence: **99.18%**
2863. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/serialization/uklibDeserialization.kt`** -> AI Confidence: **99.18%**
2864. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/AbstractKotlinSourceSet.kt`** -> AI Confidence: **99.18%**
2865. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/KotlinAndroidSourceSetFactory.kt`** -> AI Confidence: **99.18%**
2866. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/checker/MultiplatformLayoutV2AndroidStyleSourceDirUsageChecker.kt`** -> AI Confidence: **99.18%**
2867. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/KotlinBuildStatsLoggerService.kt`** -> AI Confidence: **99.18%**
2868. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/KotlinBuildStatsServicesRegistry.kt`** -> AI Confidence: **99.18%**
2869. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/binaryen/BinaryenEnvSpec.kt`** -> AI Confidence: **99.18%**
2870. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/JsBinaries.kt`** -> AI Confidence: **99.18%**
2871. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinBrowserJsIr.kt`** -> AI Confidence: **99.18%**
2872. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsIrTarget.kt`** -> AI Confidence: **99.18%**
2873. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinNodeJsIr.kt`** -> AI Confidence: **99.18%**
2874. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/LibraryConfigurator.kt`** -> AI Confidence: **99.18%**
2875. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/WebpackConfigurator.kt`** -> AI Confidence: **99.18%**
2876. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/nodejs/NodeJsExec.kt`** -> AI Confidence: **99.18%**
2877. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/nodejs/NodeJsSetupTask.kt`** -> AI Confidence: **99.18%**
2878. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/KotlinNpmResolutionManager.kt`** -> AI Confidence: **99.18%**
2879. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/resolver/KotlinCompilationNpmResolver.kt`** -> AI Confidence: **99.18%**
2880. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/karma/KotlinKarma.kt`** -> AI Confidence: **99.18%**
2881. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpack.kt`** -> AI Confidence: **99.18%**
2882. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpackRunner.kt`** -> AI Confidence: **99.18%**
2883. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnPlugin.kt`** -> AI Confidence: **99.18%**
2884. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnWorkspaces.kt`** -> AI Confidence: **99.18%**
2885. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeConfigureBinariesSideEffect.kt`** -> AI Confidence: **99.18%**
2886. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeTarget.kt`** -> AI Confidence: **99.18%**
2887. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeTargetPreset.kt`** -> AI Confidence: **99.18%**
2888. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeTestRunFactories.kt`** -> AI Confidence: **99.18%**
2889. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/DummyFrameworkTask.kt`** -> AI Confidence: **99.18%**
2890. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/AbstractCInteropCommonizerTask.kt`** -> AI Confidence: **99.18%**
2891. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropConfigurations.kt`** -> AI Confidence: **99.18%**
2892. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropMetadataDependencyTransformationTask.kt`** -> AI Confidence: **99.18%**
2893. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/NativeAppleSimulatorTCServiceMessagesClient.kt`** -> AI Confidence: **99.18%**
2894. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/toolchain/NativeToolchainProjectSetupAction.kt`** -> AI Confidence: **99.18%**
2895. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/toolchain/NativeVersionValueSource.kt`** -> AI Confidence: **99.18%**
2896. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/WasmBinaryTransformRegisteringSetupAction.kt`** -> AI Confidence: **99.18%**
2897. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/binaryen/BinaryenExec.kt`** -> AI Confidence: **99.18%**
2898. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/TasksProvider.kt`** -> AI Confidence: **99.18%**
2899. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/abi/KotlinAbiUpdateTask.kt`** -> AI Confidence: **99.18%**
2900. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/KaptConfig.kt`** -> AI Confidence: **99.18%**
2901. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/publishing/CheckPomTask.kt`** -> AI Confidence: **99.18%**
2902. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/testing/internal/TestReportService.kt`** -> AI Confidence: **99.18%**
2903. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/CurrentBuildIdentifier.kt`** -> AI Confidence: **99.18%**
2904. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/compilerOptions.kt`** -> AI Confidence: **99.18%**
2905. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/gradleUtils.kt`** -> AI Confidence: **99.18%**
2906. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/klibUtils.kt`** -> AI Confidence: **99.18%**
2907. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/processes/ExecAsyncHandle.kt`** -> AI Confidence: **99.18%**
2908. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeAndroidDependencyResolutionTest.kt`** -> AI Confidence: **99.18%**
2909. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT56143CinteropConfigurationAttributes.kt`** -> AI Confidence: **99.18%**
2910. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT61652AddSourceSetInSubpluginAndEarlyTaskMaterialization.kt`** -> AI Confidence: **99.18%**
2911. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CInteropCommonizerTaskTest.kt`** -> AI Confidence: **99.18%**
2912. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/DefaultHierarchySetupTest.kt`** -> AI Confidence: **99.18%**
2913. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/EmbedAndSignTaskTests.kt`** -> AI Confidence: **99.18%**
2914. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/IdeMultiplatformImportActionTest.kt`** -> AI Confidence: **99.18%**
2915. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinHierarchyBuilderTest.kt`** -> AI Confidence: **99.18%**
2916. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinHierarchyDslTest.kt`** -> AI Confidence: **99.18%**
2917. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinJvmRunTest.kt`** -> AI Confidence: **99.18%**
2918. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/NativeDistributionCommonizerLockTest.kt`** -> AI Confidence: **99.18%**
2919. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/compilerArgumetns/KotlinNativeCompileArgumentsTest.kt`** -> AI Confidence: **99.18%**
2920. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/CompilerDiagnosticsProblemsReporterHelpersTest.kt`** -> AI Confidence: **99.18%**
2921. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/fus/FUSGeneratedSourcesTest.kt`** -> AI Confidence: **99.18%**
2922. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/fus/FUSWebMainSourceSetTest.kt`** -> AI Confidence: **99.18%**
2923. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/fus/FUSWebTestSourceSetTest.kt`** -> AI Confidence: **99.18%**
2924. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/sources/android/getKotlinSourceSetOrFail.kt`** -> AI Confidence: **99.18%**
2925. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/MultiplatformExtensionTest.kt`** -> AI Confidence: **99.18%**
2926. **`libraries/tools/kotlin-gradle-plugin/src/gradle811/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CompilerDiagnosticsProblemsReporterG811.kt`** -> AI Confidence: **99.18%**
2927. **`libraries/tools/kotlin-gradle-plugin/src/gradle86/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CompilerDiagnosticsProblemsReporterG86.kt`** -> AI Confidence: **99.18%**
2928. **`libraries/tools/kotlin-gradle-plugin/src/gradle86/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ProblemsReporterG86.kt`** -> AI Confidence: **99.18%**
2929. **`libraries/tools/kotlin-gradle-plugin/src/gradle88/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CompilerDiagnosticsProblemsReporterG88.kt`** -> AI Confidence: **99.18%**
2930. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/classloaders/ClassLoadersCacheTest.kt`** -> AI Confidence: **99.18%**
2931. **`libraries/tools/kotlin-main-kts-test/test/org/jetbrains/kotlin/mainKts/test/mainKtsTest.kt`** -> AI Confidence: **99.18%**
2932. **`libraries/tools/kotlin-maven-plugin-test/src/it/test-lombok-with-kapt/annotation-processor/src/main/kotlin/DualGeneratorProcessor.kt`** -> AI Confidence: **99.18%**
2933. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/MavenTestArgumentsProvider.kt`** -> AI Confidence: **99.18%**
2934. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/MavenTestExecutionContext.kt`** -> AI Confidence: **99.18%**
2935. **`libraries/tools/kotlin-privacy-manifests-plugin/src/main/kotlin/PrivacyManifestsPlugin.kt`** -> AI Confidence: **99.18%**
2936. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/mappings/string/StringCasingTestGenerator.kt`** -> AI Confidence: **99.18%**
2937. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/ranges/RangesGenerator.kt`** -> AI Confidence: **99.18%**
2938. **`libraries/tools/kotlinp/jvm/testFixtures/org/jetbrains/kotlin/kotlinp/jvm/test/CompareMetadataHandler.kt`** -> AI Confidence: **99.18%**
2939. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/PlatformIntegerCommonizer.kt`** -> AI Confidence: **99.18%**
2940. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/facade.kt`** -> AI Confidence: **99.18%**
2941. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/konan/DefaultModulesProvider.kt`** -> AI Confidence: **99.18%**
2942. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/mergedtree/CirNode.kt`** -> AI Confidence: **99.18%**
2943. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/mergedtree/PlatformWidthIndex.kt`** -> AI Confidence: **99.18%**
2944. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/tree/deserializer/CirTreeFunctionDeserializer.kt`** -> AI Confidence: **99.18%**
2945. **`native/commonizer/tests/org/jetbrains/kotlin/commonizer/utils/InlineSourceBuilder.kt`** -> AI Confidence: **99.18%**
2946. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeSharedImmutableChecker.kt`** -> AI Confidence: **99.18%**
2947. **`native/native.tests/testData/gc/worker_bound_reference0.kt`** -> AI Confidence: **99.18%**
2948. **`native/native.tests/testData/interop/objc/kt56402/kt56402.kt`** -> AI Confidence: **99.18%**
2949. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/StubbingSirDeclarationProvider.kt`** -> AI Confidence: **99.18%**
2950. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirClassFromKtSymbol.kt`** -> AI Confidence: **99.18%**
2951. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirFunctionFromKtPropertySymbol.kt`** -> AI Confidence: **99.18%**
2952. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirOperatorFromKtSymbol.kt`** -> AI Confidence: **99.18%**
2953. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/SirOperatorTranslationStrategy.kt`** -> AI Confidence: **99.18%**
2954. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/TypeTranslationUtils.kt`** -> AI Confidence: **99.18%**
2955. **`native/swift/swift-export-standalone-integration-tests/src/org/jetbrains/kotlin/swiftexport/standalone/test/AbstractSwiftExportTest.kt`** -> AI Confidence: **99.18%**
2956. **`native/swift/swift-export-standalone/src/org/jetbrains/kotlin/swiftexport/standalone/SwiftExportRunner.kt`** -> AI Confidence: **99.18%**
2957. **`plugins/allopen/allopen.cli/src/org/jetbrains/kotlin/allopen/AllOpenPlugin.kt`** -> AI Confidence: **99.18%**
2958. **`plugins/assign-plugin/assign-plugin.k1/src/org/jetbrains/kotlin/assignment/plugin/ValueContainerAssignResolutionAltererExtension.kt`** -> AI Confidence: **99.18%**
2959. **`plugins/assign-plugin/assign-plugin.k2/src/org/jetbrains/kotlin/assignment/plugin/k2/FirAssignAnnotationMatchingService.kt`** -> AI Confidence: **99.18%**
2960. **`plugins/assign-plugin/assign-plugin.k2/src/org/jetbrains/kotlin/assignment/plugin/k2/FirAssignmentPluginAssignAltererExtension.kt`** -> AI Confidence: **99.18%**
2961. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/common/AbstractAtomicSymbols.kt`** -> AI Confidence: **99.18%**
2962. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/native/NativeAtomicSymbols.kt`** -> AI Confidence: **99.18%**
2963. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractCompilerTest.kt`** -> AI Confidence: **99.18%**
2964. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractComposeDiagnosticsTest.kt`** -> AI Confidence: **99.18%**
2965. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/LiveLiteralTransformTests.kt`** -> AI Confidence: **99.18%**
2966. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/LiveLiteralV2TransformTests.kt`** -> AI Confidence: **99.18%**
2967. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/RuntimeTests.kt`** -> AI Confidence: **99.18%**
2968. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/facade/K1CompilerFacade.kt`** -> AI Confidence: **99.18%**
2969. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/AnnotationUtils.kt`** -> AI Confidence: **99.18%**
2970. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/hiddenfromobjc/AddHiddenFromObjCSerializationPlugin.kt`** -> AI Confidence: **99.18%**
2971. **`plugins/jvm-abi-gen/src/org/jetbrains/kotlin/jvm/abi/JvmAbiComponentRegistrar.kt`** -> AI Confidence: **99.18%**
2972. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/javac/KaptTreeMaker.kt`** -> AI Confidence: **99.18%**
2973. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptTypeMapper.kt`** -> AI Confidence: **99.18%**
2974. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/util/PrettyWithWorkarounds.kt`** -> AI Confidence: **99.18%**
2975. **`plugins/kotlin-dataframe/kotlin-dataframe.cli/src/org/jetbrains/kotlinx/dataframe/plugin/FirDataFrameComponentRegistrar.kt`** -> AI Confidence: **99.18%**
2976. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/DataSchemaInfoCheckers.kt`** -> AI Confidence: **99.18%**
2977. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ImportedSchemasCheckers.kt`** -> AI Confidence: **99.18%**
2978. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/TokenContentGenerator.kt`** -> AI Confidence: **99.18%**
2979. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/impl/PropertyName.kt`** -> AI Confidence: **99.18%**
2980. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/parse.kt`** -> AI Confidence: **99.18%**
2981. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/select.kt`** -> AI Confidence: **99.18%**
2982. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/split.kt`** -> AI Confidence: **99.18%**
2983. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/update.kt`** -> AI Confidence: **99.18%**
2984. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/extensions/SerializationLoweringExtension.kt`** -> AI Confidence: **99.18%**
2985. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/VersionReader.kt`** -> AI Confidence: **99.18%**
2986. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/FirSerializationMetadataSerializerPlugin.kt`** -> AI Confidence: **99.18%**
2987. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/services/DependencySerializationInfoProvider.kt`** -> AI Confidence: **99.18%**
2988. **`plugins/kotlinx-serialization/testData/boxIr/intrinsicsConsistency.kt`** -> AI Confidence: **99.18%**
2989. **`plugins/kotlinx-serialization/testData/boxIr/intrinsicsNonReified.kt`** -> AI Confidence: **99.18%**
2990. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/AbstractBuilderGenerator.kt`** -> AI Confidence: **99.18%**
2991. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/AbstractConstructorGeneratorPart.kt`** -> AI Confidence: **99.18%**
2992. **`plugins/noarg/noarg.backend/src/org/jetbrains/kotlin/noarg/NoArgFullConstructorIrGenerationExtension.kt`** -> AI Confidence: **99.18%**
2993. **`plugins/noarg/noarg.backend/src/org/jetbrains/kotlin/noarg/noArgIrUtils.kt`** -> AI Confidence: **99.18%**
2994. **`plugins/parcelize/parcelize-compiler/parcelize.backend/src/org/jetbrains/kotlin/parcelize/AndroidIrBuilder.kt`** -> AI Confidence: **99.18%**
2995. **`plugins/parcelize/parcelize-compiler/parcelize.backend/src/org/jetbrains/kotlin/parcelize/IrParcelerScope.kt`** -> AI Confidence: **99.18%**
2996. **`plugins/parcelize/parcelize-compiler/parcelize.k1/src/org/jetbrains/kotlin/parcelize/serializers/ParcelSerializers.kt`** -> AI Confidence: **99.18%**
2997. **`plugins/parcelize/parcelize-compiler/parcelize.k1/src/org/jetbrains/kotlin/parcelize/serializers/ParcelizeExtensionBase.kt`** -> AI Confidence: **99.18%**
2998. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/DataFrameLikeReturnTypeInjector.kt`** -> AI Confidence: **99.18%**
2999. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/SomeAdditionalSupertypeGenerator.kt`** -> AI Confidence: **99.18%**
3000. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/SupertypeWithArgumentGenerator.kt`** -> AI Confidence: **99.18%**
3001. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/DataFrameLikeTypeMembersGenerator.kt`** -> AI Confidence: **99.18%**
3002. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/MembersOfSerializerGenerator.kt`** -> AI Confidence: **99.18%**
3003. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/NestedClassGeneratorWithLocalClassesSupport.kt`** -> AI Confidence: **99.18%**
3004. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/TopLevelDeclarationsGenerator.kt`** -> AI Confidence: **99.18%**
3005. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/TopLevelPrivateSuspendFunctionGenerator.kt`** -> AI Confidence: **99.18%**
3006. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/ir/IrTransformerForICTesting.kt`** -> AI Confidence: **99.18%**
3007. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/ir/MetadataExtensionEmitter.kt`** -> AI Confidence: **99.18%**
3008. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/builder/parameter/ExplanationFactory.kt`** -> AI Confidence: **99.18%**
3009. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/function/PowerAssertFunctionFactory.kt`** -> AI Confidence: **99.18%**
3010. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/function/PowerAssertSelfCallTransformer.kt`** -> AI Confidence: **99.18%**
3011. **`plugins/power-assert/power-assert-compiler/power-assert.frontend/src/org/jetbrains/kotlin/powerassert/checkers/PowerAssertRuntimeChecker.kt`** -> AI Confidence: **99.18%**
3012. **`plugins/power-assert/power-assert-compiler/testFixtures/org/jetbrains/kotlin/powerassert/RuntimeTestServices.kt`** -> AI Confidence: **99.18%**
3013. **`plugins/sam-with-receiver/sam-with-receiver.k2/src/org/jetbrains/kotlin/samWithReceiver/k2/FirSamWithReceiverConventionTransformer.kt`** -> AI Confidence: **99.18%**
3014. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/resolve/FirReplHistoryScope.kt`** -> AI Confidence: **99.18%**
3015. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/resolve/LazyScriptClassMemberScope.kt`** -> AI Confidence: **99.18%**
3016. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/resolve/legacyWrappers.kt`** -> AI Confidence: **99.18%**
3017. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/FirScriptingSamWithReceiverExtensionRegistrar.kt`** -> AI Confidence: **99.18%**
3018. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/JvmCliScriptEvaluationExtension.kt`** -> AI Confidence: **99.18%**
3019. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/definitions/CliScriptConfigurationsProvider.kt`** -> AI Confidence: **99.18%**
3020. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/definitions/ScriptCompilationConfigurationProviderImpl.kt`** -> AI Confidence: **99.18%**
3021. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/fir/CollectAdditionalScriptSourcesExtension.kt`** -> AI Confidence: **99.18%**
3022. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/ReplPackageViewDescriptorFactory.kt`** -> AI Confidence: **99.18%**
3023. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/ScriptJvmK2CompilerImpl.kt`** -> AI Confidence: **99.18%**
3024. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/GenericReplChecker.kt`** -> AI Confidence: **99.18%**
3025. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/ReplCodeAnalyzer.kt`** -> AI Confidence: **99.18%**
3026. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/services/Fir2IrReplSnippetConfiguratorExtensionImpl.kt`** -> AI Confidence: **99.18%**
3027. **`plugins/scripting/scripting-ide-services/src/org/jetbrains/kotlin/scripting/ide_services/compiler/KJvmReplCompilerWithIdeServices.kt`** -> AI Confidence: **99.18%**
3028. **`prepare/compiler-client-embeddable/tests/kotlin/org/jetbrains/kotlin/compiler/client/CompilerClientIT.kt`** -> AI Confidence: **99.18%**
3029. **`prepare/compiler-embeddable/tests/kotlin/org/jetbrains/kotlin/compiler/embeddable/CompilerEmbeddableSmokeTests.kt`** -> AI Confidence: **99.18%**
3030. **`repo/gradle-build-conventions/binary-compatibility-extended/src/main/kotlin/tasks/BcvApiCheckTask.kt`** -> AI Confidence: **99.18%**
3031. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/CommonUtil.kt`** -> AI Confidence: **99.18%**
3032. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/UnzipJsc.kt`** -> AI Confidence: **99.18%**
3033. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/UnzipWasmtime.kt`** -> AI Confidence: **99.18%**
3034. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/plugins/CustomVariantPublishingDsl.kt`** -> AI Confidence: **99.18%**
3035. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/plugins/DexMethodCount.kt`** -> AI Confidence: **99.18%**
3036. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/repoArtifacts.kt`** -> AI Confidence: **99.18%**
3037. **`repo/gradle-build-conventions/gradle-plugins-common/src/main/kotlin/sbom.kt`** -> AI Confidence: **99.18%**
3038. **`repo/gradle-build-conventions/project-tests-convention/src/main/kotlin/ProjectTestsExtension.kt`** -> AI Confidence: **99.18%**
3039. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/WasmExternalInheritanceChecker.kt`** -> AI Confidence: **99.18%**
3040. **`compiler/backend/src/org/jetbrains/kotlin/codegen/AbstractClassBuilder.java`** -> AI Confidence: **99.18%**
3041. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/InlineAdapter.java`** -> AI Confidence: **99.18%**
3042. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/messages/OutputMessageUtil.java`** -> AI Confidence: **99.18%**
3043. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/repl/ReplClassLoader.java`** -> AI Confidence: **99.18%**
3044. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaAnnotationImpl.java`** -> AI Confidence: **99.18%**
3045. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaElementImpl.java`** -> AI Confidence: **99.18%**
3046. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaTypeImpl.java`** -> AI Confidence: **99.18%**
3047. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnnotationResolverImpl.java`** -> AI Confidence: **99.18%**
3048. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/FunctionDescriptorUtil.java`** -> AI Confidence: **99.18%**
3049. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/diagnostics/DiagnosticsElementsCache.java`** -> AI Confidence: **99.18%**
3050. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/ResolveSessionUtils.java`** -> AI Confidence: **99.18%**
3051. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/data/KtClassOrObjectInfo.java`** -> AI Confidence: **99.18%**
3052. **`compiler/frontend/src/org/jetbrains/kotlin/types/BoundsSubstitutor.java`** -> AI Confidence: **99.18%**
3053. **`compiler/frontend/src/org/jetbrains/kotlin/types/SubstitutionUtils.java`** -> AI Confidence: **99.18%**
3054. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/ExpressionTypingUtils.java`** -> AI Confidence: **99.18%**
3055. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/ForLoopConventionsChecker.java`** -> AI Confidence: **99.18%**
3056. **`compiler/frontend/src/org/jetbrains/kotlin/util/slicedMap/Slices.java`** -> AI Confidence: **99.18%**
3057. **`compiler/preloader/instrumentation/src/org/jetbrains/kotlin/preloading/ProfilingInstrumenterExample.java`** -> AI Confidence: **99.18%**
3058. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtAnnotationEntry.java`** -> AI Confidence: **99.18%**
3059. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtBinaryExpression.java`** -> AI Confidence: **99.18%**
3060. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtCollectionLiteralExpression.java`** -> AI Confidence: **99.18%**
3061. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtElementImpl.java`** -> AI Confidence: **99.18%**
3062. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtExpressionImplStub.java`** -> AI Confidence: **99.18%**
3063. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtParameter.java`** -> AI Confidence: **99.18%**
3064. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtStubbedPsiUtil.java`** -> AI Confidence: **99.18%**
3065. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtSuperTypeCallEntry.java`** -> AI Confidence: **99.18%**
3066. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtSuperTypeListEntry.java`** -> AI Confidence: **99.18%**
3067. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtTypeParameter.java`** -> AI Confidence: **99.18%**
3068. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtTypeParameterListOwnerStub.java`** -> AI Confidence: **99.18%**
3069. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtUserType.java`** -> AI Confidence: **99.18%**
3070. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtObjectElementType.java`** -> AI Confidence: **99.18%**
3071. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/integration/KotlinIntegrationTestBase.java`** -> AI Confidence: **99.18%**
3072. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/jvm/compiler/LoadDescriptorUtil.java`** -> AI Confidence: **99.18%**
3073. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/AbstractLazyTypeParameterDescriptor.java`** -> AI Confidence: **99.18%**
3074. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/ClassConstructorDescriptorImpl.java`** -> AI Confidence: **99.18%**
3075. **`jps/jps-platform-api-signatures/src/org/jetbrains/jps/builders/java/dependencyView/Callbacks.java`** -> AI Confidence: **99.18%**
3076. **`js/js.ast/src/org/jetbrains/kotlin/js/backend/ast/AbstractNode.java`** -> AI Confidence: **99.18%**
3077. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/testOld/utils/JsTestUtils.java`** -> AI Confidence: **99.18%**
3078. **`libraries/tools/kotlin-maven-plugin-test/src/it/test-respect-compile-source-root/myPlugin/src/main/java/AddCustomSourceRootsMojo.java`** -> AI Confidence: **99.18%**
3079. **`native/objcexport-header-generator/testData/headers/classTypePropertyTranslation/!classTypePropertyTranslation.h`** -> AI Confidence: **99.18%**
3080. **`native/objcexport-header-generator/testData/headers/extensionsMangling/!extensionsMangling.h`** -> AI Confidence: **99.18%**
3081. **`native/objcexport-header-generator/testData/headers/functionWithReservedMethodNameAndReturnType/!functionWithReservedMethodNameAndReturnType.h`** -> AI Confidence: **99.18%**
3082. **`native/objcexport-header-generator/testData/headers/simpleDataClass/!simpleDataClass.h`** -> AI Confidence: **99.18%**
3083. **`native/objcexport-header-generator/testData/headers/specialFunctionNames/!specialFunctionNames.h`** -> AI Confidence: **99.18%**
3084. **`native/objcexport-header-generator/testData/headers/specialFunctionNamesExplicitMethodFamily/!specialFunctionNamesExplicitMethodFamily.h`** -> AI Confidence: **99.18%**
3085. **`kotlin-native/runtime/src/alloc/custom/cpp/HeapTest.cpp`** -> AI Confidence: **99.18%**
3086. **`kotlin-native/runtime/src/alloc/legacy/cpp/ObjectFactoryTest.cpp`** -> AI Confidence: **99.18%**
3087. **`kotlin-native/runtime/src/gc/cms/cpp/Barriers.cpp`** -> AI Confidence: **99.18%**
3088. **`kotlin-native/runtime/src/gc/cms/cpp/GCImpl.cpp`** -> AI Confidence: **99.18%**
3089. **`kotlin-native/runtime/src/gc/pmcs/cpp/AuxiliaryGCThreads.cpp`** -> AI Confidence: **99.18%**
3090. **`kotlin-native/runtime/src/gc/pmcs/cpp/GCImpl.cpp`** -> AI Confidence: **99.18%**
3091. **`kotlin-native/runtime/src/gc/pmcs/cpp/GCImplTest.cpp`** -> AI Confidence: **99.18%**
3092. **`kotlin-native/runtime/src/gc/stms/cpp/GCImpl.cpp`** -> AI Confidence: **99.18%**
3093. **`kotlin-native/runtime/src/main/cpp/ExceptionsTest.cpp`** -> AI Confidence: **99.18%**
3094. **`kotlin-native/runtime/src/main/cpp/MultiSourceQueueTest.cpp`** -> AI Confidence: **99.18%**
3095. **`kotlin-native/runtime/src/main/cpp/Natives.cpp`** -> AI Confidence: **99.18%**
3096. **`kotlin-native/runtime/src/main/cpp/concurrent/Mutex.hpp`** -> AI Confidence: **99.18%**
3097. **`kotlin-native/runtime/src/main/cpp/concurrent/ParallelProcessorTest.cpp`** -> AI Confidence: **99.18%**
3098. **`kotlin-native/runtime/src/main/cpp/concurrent/ScopedThreadTest.cpp`** -> AI Confidence: **99.18%**
3099. **`kotlin-native/runtime/src/mm/cpp/ExternalRCRefRegistryTest.cpp`** -> AI Confidence: **99.18%**
3100. **`kotlin-native/runtime/src/mm/cpp/ExtraObjectDataTest.cpp`** -> AI Confidence: **99.18%**
3101. **`kotlin-native/runtime/src/mm/cpp/ObjectTraversalTest.cpp`** -> AI Confidence: **99.18%**
3102. **`analysis/analysis-api/testData/components/compileTimeConstantProvider/evaluate/complexLogicExpression.kt`** -> AI Confidence: **99.17%**
3103. **`analysis/analysis-api/testData/components/dataFlowInfoProvider/exitPointSnapshot/controlFlow/conditionalJumps/break4.kt`** -> AI Confidence: **99.17%**
3104. **`analysis/analysis-api/testData/components/dataFlowInfoProvider/exitPointSnapshot/controlFlow/exitPointEquivalence/multipleBreaks.kt`** -> AI Confidence: **99.17%**
3105. **`analysis/analysis-api/testData/components/dataFlowInfoProvider/exitPointSnapshot/defaultValues/incrementPostfix.kt`** -> AI Confidence: **99.17%**
3106. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/loopLabel.kt`** -> AI Confidence: **99.17%**
3107. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/loopLabelBreak.kt`** -> AI Confidence: **99.17%**
3108. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/loopLabelBreakLabel.kt`** -> AI Confidence: **99.17%**
3109. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/loopLabelBreakUsed.kt`** -> AI Confidence: **99.17%**
3110. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/try.kt`** -> AI Confidence: **99.17%**
3111. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryBlockBlock.kt`** -> AI Confidence: **99.17%**
3112. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryBlockBlockUsed.kt`** -> AI Confidence: **99.17%**
3113. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryBlockInner.kt`** -> AI Confidence: **99.17%**
3114. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryBlockInnerUsed.kt`** -> AI Confidence: **99.17%**
3115. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryCatchArg.kt`** -> AI Confidence: **99.17%**
3116. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryCatchArgUsed.kt`** -> AI Confidence: **99.17%**
3117. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryCatchBlock.kt`** -> AI Confidence: **99.17%**
3118. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryCatchBlockInner.kt`** -> AI Confidence: **99.17%**
3119. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryCatchBlockInnerUsed.kt`** -> AI Confidence: **99.17%**
3120. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryCatchBlockUsed.kt`** -> AI Confidence: **99.17%**
3121. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryFinallyBlock.kt`** -> AI Confidence: **99.17%**
3122. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryFinallyBlockInner.kt`** -> AI Confidence: **99.17%**
3123. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryFinallyBlockInnerUsed.kt`** -> AI Confidence: **99.17%**
3124. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryFinallyBlockUsed.kt`** -> AI Confidence: **99.17%**
3125. **`analysis/analysis-api/testData/components/expressionInfoProvider/isUsedAsExpression/tryUsed.kt`** -> AI Confidence: **99.17%**
3126. **`analysis/analysis-api/testData/components/resolver/allByPsi/contextSensitiveResolution/otherExpectedTypePositions/functionalTypes.kt`** -> AI Confidence: **99.17%**
3127. **`analysis/analysis-api/testData/components/resolver/allByPsi/contextSensitiveResolution/otherExpectedTypePositions/tryCatchStatementsEnum.kt`** -> AI Confidence: **99.17%**
3128. **`analysis/analysis-api/testData/components/resolver/allByPsi/contextSensitiveResolution/otherExpectedTypePositions/whenIfLastStatement.kt`** -> AI Confidence: **99.17%**
3129. **`analysis/analysis-api/testData/components/resolver/allByPsi/destructuring/nameBasedDestructuringFullForm.kt`** -> AI Confidence: **99.17%**
3130. **`analysis/analysis-api/testData/components/resolver/allByPsi/destructuring/nameBasedDestructuringShortFormAfter.kt`** -> AI Confidence: **99.17%**
3131. **`analysis/analysis-api/testData/components/resolver/allByPsi/operators/nonCallBinary.kt`** -> AI Confidence: **99.17%**
3132. **`analysis/analysis-api/testData/components/resolver/singleByPsi/arrayAccess/set.kt`** -> AI Confidence: **99.17%**
3133. **`analysis/analysis-api/testData/components/symbolDeclarationRenderer/renderDeclaration/intersectionType.kt`** -> AI Confidence: **99.17%**
3134. **`analysis/low-level-api-fir/testData/getOrBuildFir/expressions/tryExpression.kt`** -> AI Confidence: **99.17%**
3135. **`analysis/low-level-api-fir/testData/getOrBuildFir/expressions/tryExpressionScript.kts`** -> AI Confidence: **99.17%**
3136. **`compiler/fir/analysis-tests/testData/resolve/cfg/binaryOperations.kt`** -> AI Confidence: **99.17%**
3137. **`compiler/fir/analysis-tests/testData/resolve/collectionLiteralInLambdaReturningAnnotation.kt`** -> AI Confidence: **99.17%**
3138. **`compiler/fir/analysis-tests/testData/resolve/contextSensitiveResolutionUsingExpectedType/otherExpectedTypePositions/functionalTypes.kt`** -> AI Confidence: **99.17%**
3139. **`compiler/fir/analysis-tests/testData/resolve/contextSensitiveResolutionUsingExpectedType/otherExpectedTypePositions/tryCatchStatementsEnum.kt`** -> AI Confidence: **99.17%**
3140. **`compiler/fir/analysis-tests/testData/resolve/contextSensitiveResolutionUsingExpectedType/otherExpectedTypePositions/whenIfLastStatement.kt`** -> AI Confidence: **99.17%**
3141. **`compiler/fir/analysis-tests/testData/resolve/destructuring/nameBasedDestructuringFullForm.kt`** -> AI Confidence: **99.17%**
3142. **`compiler/fir/analysis-tests/testData/resolve/destructuring/nameBasedDestructuringShortFormAfter.kt`** -> AI Confidence: **99.17%**
3143. **`compiler/fir/analysis-tests/testData/resolve/exhaustiveness/negative/missingBooleanBranch.kt`** -> AI Confidence: **99.17%**
3144. **`compiler/fir/analysis-tests/testData/resolve/exhaustiveness/negative/missingElse.kt`** -> AI Confidence: **99.17%**
3145. **`compiler/fir/analysis-tests/testData/resolve/exhaustiveness/positive/exhaustiveness_enum.kt`** -> AI Confidence: **99.17%**
3146. **`compiler/fir/analysis-tests/testData/resolve/exhaustiveness/positive/exhaustiveness_enumJava.kt`** -> AI Confidence: **99.17%**
3147. **`compiler/fir/analysis-tests/testData/resolve/exhaustiveness/positive/exhaustiveness_smartcastedBoolean.kt`** -> AI Confidence: **99.17%**
3148. **`compiler/fir/analysis-tests/testData/resolve/smartcasts/boundSmartcasts/boundSmartcastsInBranches.kt`** -> AI Confidence: **99.17%**
3149. **`compiler/fir/analysis-tests/testData/resolve/smartcasts/casts.kt`** -> AI Confidence: **99.17%**
3150. **`compiler/fir/analysis-tests/testData/resolve/smartcasts/loops/endlessLoops.kt`** -> AI Confidence: **99.17%**
3151. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/CheckersConfiguration.kt`** -> AI Confidence: **99.17%**
3152. **`compiler/psi/psi-impl/testData/psi/Expressions_ERR.kt`** -> AI Confidence: **99.17%**
3153. **`compiler/psi/psi-impl/testData/psi/NewLinesValidOperations.kt`** -> AI Confidence: **99.17%**
3154. **`compiler/psi/psi-impl/testData/psi/annotation/at/kt21055.kt`** -> AI Confidence: **99.17%**
3155. **`compiler/psi/psi-impl/testData/psi/complicateLTGT.kt`** -> AI Confidence: **99.17%**
3156. **`compiler/psi/psi-impl/testData/psi/complicateLTGTE.kt`** -> AI Confidence: **99.17%**
3157. **`compiler/psi/psi-impl/testData/psi/destructuring/shortPositionBasedDestructuringErrors.kt`** -> AI Confidence: **99.17%**
3158. **`compiler/psi/psi-impl/testData/psi/greatSyntacticShift/nullableTypes.kt`** -> AI Confidence: **99.17%**
3159. **`compiler/psi/psi-impl/testData/psi/operators/untilOperatorGreater.kt`** -> AI Confidence: **99.17%**
3160. **`compiler/testData/cfg-variables/bugs/doWhileAssignment.kt`** -> AI Confidence: **99.17%**
3161. **`compiler/testData/cfg-variables/bugs/kt4764.kt`** -> AI Confidence: **99.17%**
3162. **`compiler/testData/cfg-variables/lexicalScopes/tryScope.kt`** -> AI Confidence: **99.17%**
3163. **`compiler/testData/cfg/controlStructures/Finally.kt`** -> AI Confidence: **99.17%**
3164. **`compiler/testData/cfg/tailCalls/tryCatchFinally.kt`** -> AI Confidence: **99.17%**
3165. **`compiler/testData/diagnostics/tests/cast/classVsClassIsCheck.fir.kt`** -> AI Confidence: **99.17%**
3166. **`compiler/testData/diagnostics/tests/cast/classVsClassIsCheck.kt`** -> AI Confidence: **99.17%**
3167. **`compiler/testData/diagnostics/tests/constantEvaluator/constant/duplicateLabelWithNonTrivialCondition_disabled.fir.kt`** -> AI Confidence: **99.17%**
3168. **`compiler/testData/diagnostics/tests/constantEvaluator/constant/duplicateLabelWithNonTrivialCondition_disabled.kt`** -> AI Confidence: **99.17%**
3169. **`compiler/testData/diagnostics/tests/constantEvaluator/constant/duplicateLabelWithNonTrivialCondition_enabled.kt`** -> AI Confidence: **99.17%**
3170. **`compiler/testData/diagnostics/tests/constantEvaluator/usesVariableAsConstant/binaryTypes.fir.kt`** -> AI Confidence: **99.17%**
3171. **`compiler/testData/diagnostics/tests/constantEvaluator/usesVariableAsConstant/binaryTypes.kt`** -> AI Confidence: **99.17%**
3172. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/assignedInTryWithCatch.fir.kt`** -> AI Confidence: **99.17%**
3173. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/assignedInTryWithCatch.kt`** -> AI Confidence: **99.17%**
3174. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/deadCode/kt2585_1.fir.kt`** -> AI Confidence: **99.17%**
3175. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/deadCode/kt2585_1.kt`** -> AI Confidence: **99.17%**
3176. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/deadCode/kt3162tryAsInitializer.kt`** -> AI Confidence: **99.17%**
3177. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/lambdaCaptureUninitializedProperty.fir.kt`** -> AI Confidence: **99.17%**
3178. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/lambdaCaptureUninitializedProperty.kt`** -> AI Confidence: **99.17%**
3179. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/reassignmentInTryCatchWithJumps.fir.kt`** -> AI Confidence: **99.17%**
3180. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/reassignmentInTryCatchWithJumps.kt`** -> AI Confidence: **99.17%**
3181. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/tryWithAssignmentUsedInCatch.kt`** -> AI Confidence: **99.17%**
3182. **`compiler/testData/diagnostics/tests/controlStructures/breakContinueInCrossInlineLambda.kt`** -> AI Confidence: **99.17%**
3183. **`compiler/testData/diagnostics/tests/controlStructures/breakContinueInNoInlineLambda.kt`** -> AI Confidence: **99.17%**
3184. **`compiler/testData/diagnostics/tests/controlStructures/ifWhenToAnyComplexExpressions.fir.kt`** -> AI Confidence: **99.17%**
3185. **`compiler/testData/diagnostics/tests/controlStructures/ifWhenToAnyComplexExpressions.kt`** -> AI Confidence: **99.17%**
3186. **`compiler/testData/diagnostics/tests/controlStructures/ifWhenWithoutElse.fir.kt`** -> AI Confidence: **99.17%**
3187. **`compiler/testData/diagnostics/tests/controlStructures/ifWhenWithoutElse.kt`** -> AI Confidence: **99.17%**
3188. **`compiler/testData/diagnostics/tests/controlStructures/kt10322.fir.kt`** -> AI Confidence: **99.17%**
3189. **`compiler/testData/diagnostics/tests/controlStructures/kt10322.kt`** -> AI Confidence: **99.17%**
3190. **`compiler/testData/diagnostics/tests/controlStructures/kt51711.kt`** -> AI Confidence: **99.17%**
3191. **`compiler/testData/diagnostics/tests/controlStructures/kt770.kt351.kt735_StatementType.fir.kt`** -> AI Confidence: **99.17%**
3192. **`compiler/testData/diagnostics/tests/controlStructures/kt770.kt351.kt735_StatementType.kt`** -> AI Confidence: **99.17%**
3193. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/AndOr.fir.kt`** -> AI Confidence: **99.17%**
3194. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/AndOr.kt`** -> AI Confidence: **99.17%**
3195. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/ArrayAccess.fir.kt`** -> AI Confidence: **99.17%**
3196. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/ArrayAccess.kt`** -> AI Confidence: **99.17%**
3197. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/BinaryExpression.fir.kt`** -> AI Confidence: **99.17%**
3198. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/BinaryExpression.kt`** -> AI Confidence: **99.17%**
3199. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/DoWhileCondition.fir.kt`** -> AI Confidence: **99.17%**
3200. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/DoWhileCondition.kt`** -> AI Confidence: **99.17%**
3201. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/IfThenElse.fir.kt`** -> AI Confidence: **99.17%**
3202. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/IfThenElse.kt`** -> AI Confidence: **99.17%**
3203. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/TryFinally.fir.kt`** -> AI Confidence: **99.17%**
3204. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/TryFinally.kt`** -> AI Confidence: **99.17%**
3205. **`compiler/testData/diagnostics/tests/expressions/UnusedExpressionByLocation.fir.kt`** -> AI Confidence: **99.17%**
3206. **`compiler/testData/diagnostics/tests/expressions/UnusedExpressionByLocation.kt`** -> AI Confidence: **99.17%**
3207. **`compiler/testData/diagnostics/tests/functionLiterals/return/IfWithoutElse.fir.kt`** -> AI Confidence: **99.17%**
3208. **`compiler/testData/diagnostics/tests/functionLiterals/return/IfWithoutElse.kt`** -> AI Confidence: **99.17%**
3209. **`compiler/testData/diagnostics/tests/functionLiterals/return/LocalReturnUnitWithBodyExpression.fir.kt`** -> AI Confidence: **99.17%**
3210. **`compiler/testData/diagnostics/tests/functionLiterals/return/LocalReturnUnitWithBodyExpression.kt`** -> AI Confidence: **99.17%**
3211. **`compiler/testData/diagnostics/tests/functionTypeInitializerTypeMismatch.fir.kt`** -> AI Confidence: **99.17%**
3212. **`compiler/testData/diagnostics/tests/generics/nullability/smartCastRefinedClass.fir.kt`** -> AI Confidence: **99.17%**
3213. **`compiler/testData/diagnostics/tests/generics/nullability/smartCastRefinedClass.kt`** -> AI Confidence: **99.17%**
3214. **`compiler/testData/diagnostics/tests/incompleteCode/controlStructuresErrors.fir.kt`** -> AI Confidence: **99.17%**
3215. **`compiler/testData/diagnostics/tests/incompleteCode/controlStructuresErrors.kt`** -> AI Confidence: **99.17%**
3216. **`compiler/testData/diagnostics/tests/inference/callableReferences/kt55931.fir.kt`** -> AI Confidence: **99.17%**
3217. **`compiler/testData/diagnostics/tests/inference/callableReferences/kt55931.kt`** -> AI Confidence: **99.17%**
3218. **`compiler/testData/diagnostics/tests/inference/completion/partialForIltWithNothing.fir.kt`** -> AI Confidence: **99.17%**
3219. **`compiler/testData/diagnostics/tests/inference/completion/partialForIltWithNothing.kt`** -> AI Confidence: **99.17%**
3220. **`compiler/testData/diagnostics/tests/inference/constraints/complexDependencyWihtoutProperConstraints.fir.kt`** -> AI Confidence: **99.17%**
3221. **`compiler/testData/diagnostics/tests/inference/constraints/complexDependencyWihtoutProperConstraints.kt`** -> AI Confidence: **99.17%**
3222. **`compiler/testData/diagnostics/tests/initializedAfterRethrow.fir.kt`** -> AI Confidence: **99.17%**
3223. **`compiler/testData/diagnostics/tests/initializedAfterRethrow.kt`** -> AI Confidence: **99.17%**
3224. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/inlineExtensionFunction.fir.kt`** -> AI Confidence: **99.17%**
3225. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/inlineExtensionFunction.kt`** -> AI Confidence: **99.17%**
3226. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/lambdaAsGeneric.fir.kt`** -> AI Confidence: **99.17%**
3227. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/lambdaAsGeneric.kt`** -> AI Confidence: **99.17%**
3228. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/lambdaAsNonFunction.fir.kt`** -> AI Confidence: **99.17%**
3229. **`compiler/testData/diagnostics/tests/inline/nonLocalBreakContinue/lambdaAsNonFunction.kt`** -> AI Confidence: **99.17%**
3230. **`compiler/testData/diagnostics/tests/inline/wrongUsage.kt`** -> AI Confidence: **99.17%**
3231. **`compiler/testData/diagnostics/tests/inlineClasses/identityComparisonWithInlineClasses.fir.kt`** -> AI Confidence: **99.17%**
3232. **`compiler/testData/diagnostics/tests/inlineClasses/identityComparisonWithInlineClasses.kt`** -> AI Confidence: **99.17%**
3233. **`compiler/testData/diagnostics/tests/nullabilityAndSmartCasts/kt1680.kt`** -> AI Confidence: **99.17%**
3234. **`compiler/testData/diagnostics/tests/nullabilityAndSmartCasts/kt1778.fir.kt`** -> AI Confidence: **99.17%**
3235. **`compiler/testData/diagnostics/tests/nullabilityAndSmartCasts/kt1778.kt`** -> AI Confidence: **99.17%**
3236. **`compiler/testData/diagnostics/tests/nullableTypes/notUselessComparasionAfterSmartcast.fir.kt`** -> AI Confidence: **99.17%**
3237. **`compiler/testData/diagnostics/tests/nullableTypes/notUselessComparasionAfterSmartcast.kt`** -> AI Confidence: **99.17%**
3238. **`compiler/testData/diagnostics/tests/platformTypes/nullabilityWarnings/elvis.fir.kt`** -> AI Confidence: **99.17%**
3239. **`compiler/testData/diagnostics/tests/platformTypes/nullabilityWarnings/elvis.kt`** -> AI Confidence: **99.17%**
3240. **`compiler/testData/diagnostics/tests/regressions/kt10243.fir.kt`** -> AI Confidence: **99.17%**
3241. **`compiler/testData/diagnostics/tests/regressions/kt10243.kt`** -> AI Confidence: **99.17%**
3242. **`compiler/testData/diagnostics/tests/resolve/priority/extensionVsMember.kt`** -> AI Confidence: **99.17%**
3243. **`compiler/testData/diagnostics/tests/resolve/underscoreInCatchBlockWithEnabledFeature.fir.kt`** -> AI Confidence: **99.17%**
3244. **`compiler/testData/diagnostics/tests/resolve/underscoreInCatchBlockWithEnabledFeature.kt`** -> AI Confidence: **99.17%**
3245. **`compiler/testData/diagnostics/tests/senselessComparison/parenthesized.fir.kt`** -> AI Confidence: **99.17%**
3246. **`compiler/testData/diagnostics/tests/senselessComparison/parenthesized.kt`** -> AI Confidence: **99.17%**
3247. **`compiler/testData/diagnostics/tests/smartCasts/castchecks/castInTryWithCatch.fir.kt`** -> AI Confidence: **99.17%**
3248. **`compiler/testData/diagnostics/tests/smartCasts/castchecks/castInTryWithCatch.kt`** -> AI Confidence: **99.17%**
3249. **`compiler/testData/diagnostics/tests/smartCasts/comparisonOfBuiltInTypesUnderOr.fir.kt`** -> AI Confidence: **99.17%**
3250. **`compiler/testData/diagnostics/tests/smartCasts/comparisonOfBuiltInTypesUnderOr.kt`** -> AI Confidence: **99.17%**
3251. **`compiler/testData/diagnostics/tests/smartCasts/elvis/basicOff.fir.kt`** -> AI Confidence: **99.17%**
3252. **`compiler/testData/diagnostics/tests/smartCasts/elvis/basicOff.kt`** -> AI Confidence: **99.17%**
3253. **`compiler/testData/diagnostics/tests/smartCasts/ifWhenExprNonNull.fir.kt`** -> AI Confidence: **99.17%**
3254. **`compiler/testData/diagnostics/tests/smartCasts/ifWhenExprNonNull.kt`** -> AI Confidence: **99.17%**
3255. **`compiler/testData/diagnostics/tests/smartCasts/intersectionScope/flexibleTypes.fir.kt`** -> AI Confidence: **99.17%**
3256. **`compiler/testData/diagnostics/tests/smartCasts/intersectionScope/flexibleTypes.kt`** -> AI Confidence: **99.17%**
3257. **`compiler/testData/diagnostics/tests/smartCasts/loops/assignElvisIfBreakInsideWhileTrue.fir.kt`** -> AI Confidence: **99.17%**
3258. **`compiler/testData/diagnostics/tests/smartCasts/loops/assignElvisIfBreakInsideWhileTrue.kt`** -> AI Confidence: **99.17%**
3259. **`compiler/testData/diagnostics/tests/smartCasts/loops/elvisBreakInsideDoWhile.fir.kt`** -> AI Confidence: **99.17%**
3260. **`compiler/testData/diagnostics/tests/smartCasts/loops/elvisBreakInsideDoWhile.kt`** -> AI Confidence: **99.17%**
3261. **`compiler/testData/diagnostics/tests/smartCasts/loops/elvisIfBreakInsideWhileTrue.kt`** -> AI Confidence: **99.17%**
3262. **`compiler/testData/diagnostics/tests/smartCasts/loops/elvisInsideDoWhile.fir.kt`** -> AI Confidence: **99.17%**
3263. **`compiler/testData/diagnostics/tests/smartCasts/loops/elvisInsideDoWhile.kt`** -> AI Confidence: **99.17%**
3264. **`compiler/testData/diagnostics/tests/smartCasts/loops/elvisLeftBreakInsideWhileTrue.kt`** -> AI Confidence: **99.17%**
3265. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifBlockInsideDoWhile.fir.kt`** -> AI Confidence: **99.17%**
3266. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifBlockInsideDoWhile.kt`** -> AI Confidence: **99.17%**
3267. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifBreakAssignInsideWhileTrue.fir.kt`** -> AI Confidence: **99.17%**
3268. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifBreakAssignInsideWhileTrue.kt`** -> AI Confidence: **99.17%**
3269. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifBreakExprInsideWhileTrue.fir.kt`** -> AI Confidence: **99.17%**
3270. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifBreakExprInsideWhileTrue.kt`** -> AI Confidence: **99.17%**
3271. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifElseBlockInsideDoWhile.fir.kt`** -> AI Confidence: **99.17%**
3272. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifElseBlockInsideDoWhile.kt`** -> AI Confidence: **99.17%**
3273. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifInsideDoWhile.fir.kt`** -> AI Confidence: **99.17%**
3274. **`compiler/testData/diagnostics/tests/smartCasts/loops/ifInsideDoWhile.kt`** -> AI Confidence: **99.17%**
3275. **`compiler/testData/diagnostics/tests/smartCasts/loops/leftElvisBreakInsideWhileTrue.fir.kt`** -> AI Confidence: **99.17%**
3276. **`compiler/testData/diagnostics/tests/smartCasts/loops/leftElvisBreakInsideWhileTrue.kt`** -> AI Confidence: **99.17%**
3277. **`compiler/testData/diagnostics/tests/smartCasts/loops/nestedLoopsWithBreak.fir.kt`** -> AI Confidence: **99.17%**
3278. **`compiler/testData/diagnostics/tests/smartCasts/loops/nestedLoopsWithBreak.kt`** -> AI Confidence: **99.17%**
3279. **`compiler/testData/diagnostics/tests/smartCasts/loops/nestedLoopsWithLongBreak.fir.kt`** -> AI Confidence: **99.17%**
3280. **`compiler/testData/diagnostics/tests/smartCasts/loops/nestedLoopsWithLongBreak.kt`** -> AI Confidence: **99.17%**
3281. **`compiler/testData/diagnostics/tests/smartCasts/loops/nestedLoopsWithLongContinue.fir.kt`** -> AI Confidence: **99.17%**
3282. **`compiler/testData/diagnostics/tests/smartCasts/loops/nestedLoopsWithLongContinue.kt`** -> AI Confidence: **99.17%**
3283. **`compiler/testData/diagnostics/tests/smartCasts/loops/useInsideDoWhile.fir.kt`** -> AI Confidence: **99.17%**
3284. **`compiler/testData/diagnostics/tests/smartCasts/loops/useInsideDoWhile.kt`** -> AI Confidence: **99.17%**
3285. **`compiler/testData/diagnostics/tests/smartCasts/loops/whileNullAssignToSomething.fir.kt`** -> AI Confidence: **99.17%**
3286. **`compiler/testData/diagnostics/tests/smartCasts/loops/whileNullAssignToSomething.kt`** -> AI Confidence: **99.17%**
3287. **`compiler/testData/diagnostics/tests/smartCasts/safecalls/insideIfExpr.kt`** -> AI Confidence: **99.17%**
3288. **`compiler/testData/diagnostics/tests/smartCasts/varInAccessor.fir.kt`** -> AI Confidence: **99.17%**
3289. **`compiler/testData/diagnostics/tests/smartCasts/varInAccessor.kt`** -> AI Confidence: **99.17%**
3290. **`compiler/testData/diagnostics/tests/smartCasts/variables/ifElseBlockInsideDoWhile.fir.kt`** -> AI Confidence: **99.17%**
3291. **`compiler/testData/diagnostics/tests/smartCasts/variables/ifElseBlockInsideDoWhile.kt`** -> AI Confidence: **99.17%**
3292. **`compiler/testData/diagnostics/tests/smartCasts/variables/ifElseBlockInsideDoWhileWithBreak.fir.kt`** -> AI Confidence: **99.17%**
3293. **`compiler/testData/diagnostics/tests/smartCasts/variables/ifElseBlockInsideDoWhileWithBreak.kt`** -> AI Confidence: **99.17%**
3294. **`compiler/testData/diagnostics/tests/smartCasts/variables/ifNullAssignment.fir.kt`** -> AI Confidence: **99.17%**
3295. **`compiler/testData/diagnostics/tests/smartCasts/variables/ifNullAssignment.kt`** -> AI Confidence: **99.17%**
3296. **`compiler/testData/diagnostics/tests/suppress/oneWarning/onBlockStatementSameLine.fir.kt`** -> AI Confidence: **99.17%**
3297. **`compiler/testData/diagnostics/tests/suppress/oneWarning/onBlockStatementSameLine.kt`** -> AI Confidence: **99.17%**
3298. **`compiler/testData/diagnostics/tests/syntax/complicatedLTGT.fir.kt`** -> AI Confidence: **99.17%**
3299. **`compiler/testData/diagnostics/tests/syntax/complicatedLTGT.kt`** -> AI Confidence: **99.17%**
3300. **`compiler/testData/diagnostics/tests/syntax/complicatedLTGTE.kt`** -> AI Confidence: **99.17%**
3301. **`compiler/testData/diagnostics/tests/syntax/forInStringWithIndexNameBasedDestructuringFullForm.fir.kt`** -> AI Confidence: **99.17%**
3302. **`compiler/testData/diagnostics/tests/syntax/forInStringWithIndexNameBasedDestructuringFullForm.kt`** -> AI Confidence: **99.17%**
3303. **`compiler/testData/diagnostics/tests/typeParameters/implicitNothingAgainstNotNothingExpectedType.fir.kt`** -> AI Confidence: **99.17%**
3304. **`compiler/testData/diagnostics/tests/typeParameters/implicitNothingAgainstNotNothingExpectedType.kt`** -> AI Confidence: **99.17%**
3305. **`compiler/testData/diagnostics/tests/when/guard/expectedTypeInGuard.fir.kt`** -> AI Confidence: **99.17%**
3306. **`compiler/testData/diagnostics/tests/when/guard/expectedTypeInGuard.kt`** -> AI Confidence: **99.17%**
3307. **`compiler/testData/diagnostics/tests/when/guard/smartCasts.fir.kt`** -> AI Confidence: **99.17%**
3308. **`compiler/testData/diagnostics/tests/when/guard/smartCasts.kt`** -> AI Confidence: **99.17%**
3309. **`compiler/testData/diagnostics/tests/when/guard/suggestGuard.fir.kt`** -> AI Confidence: **99.17%**
3310. **`compiler/testData/diagnostics/tests/when/guard/suggestGuard.kt`** -> AI Confidence: **99.17%**
3311. **`compiler/testData/diagnostics/testsWithJsStdLibAndBackendCompilation/jsCode/inlinedReturnBreakContinue/lambdaPassedToInlineFunction.kt`** -> AI Confidence: **99.17%**
3312. **`compiler/testData/diagnostics/testsWithJsStdLibAndBackendCompilation/jsCode/inlinedReturnBreakContinue/withReturnValueDoWhileContinue.kt`** -> AI Confidence: **99.17%**
3313. **`compiler/testData/diagnostics/testsWithJsStdLibAndBackendCompilation/jsCode/inlinedReturnBreakContinue/withReturnValueNested.kt`** -> AI Confidence: **99.17%**
3314. **`compiler/testData/ir/interpreter/exceptions/getCauseMessage.kt`** -> AI Confidence: **99.17%**
3315. **`compiler/testData/ir/irText/expressions/badBreakContinue.kt`** -> AI Confidence: **99.17%**
3316. **`compiler/testData/ir/irText/expressions/breakContinueInWhen.kt`** -> AI Confidence: **99.17%**
3317. **`compiler/testData/ir/irText/expressions/ifElseIf.kt`** -> AI Confidence: **99.17%**
3318. **`compiler/testData/ir/irText/expressions/kt27933.kt`** -> AI Confidence: **99.17%**
3319. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/types/expandedTypeUtils.kt`** -> AI Confidence: **99.17%**
3320. **`core/descriptors/src/org/jetbrains/kotlin/types/error/ErrorScopeKind.kt`** -> AI Confidence: **99.17%**
3321. **`gradle/versions.gradle.kts`** -> AI Confidence: **99.17%**
3322. **`js/js.translator/testData/box/esModules/export/exportFileWithTopLevelProperty.kt`** -> AI Confidence: **99.17%**
3323. **`js/js.translator/testData/box/esModules/export/exportTopLevelProperty.kt`** -> AI Confidence: **99.17%**
3324. **`js/js.translator/testData/box/expression/evaluationOrder/assignToArrayElementWithSideEffect.kt`** -> AI Confidence: **99.17%**
3325. **`js/js.translator/testData/box/expression/evaluationOrder/callWithBreakContinueReturn.kt`** -> AI Confidence: **99.17%**
3326. **`js/js.translator/testData/box/expression/for/forIteratesOverArray.kt`** -> AI Confidence: **99.17%**
3327. **`js/js.translator/testData/box/expression/for/labeledForWithContinue.kt`** -> AI Confidence: **99.17%**
3328. **`js/js.translator/testData/box/expression/try/tryCatchDynamic.kt`** -> AI Confidence: **99.17%**
3329. **`js/js.translator/testData/box/expression/when/whenWithIf.kt`** -> AI Confidence: **99.17%**
3330. **`js/js.translator/testData/box/expression/while/whileWithComplexOneStatement.kt`** -> AI Confidence: **99.17%**
3331. **`js/js.translator/testData/box/java/arrayList/removeWithIndexOutOfBounds.kt`** -> AI Confidence: **99.17%**
3332. **`js/js.translator/testData/box/java/arrayList/toArray.kt`** -> AI Confidence: **99.17%**
3333. **`js/js.translator/testData/box/jsCode/operators.kt`** -> AI Confidence: **99.17%**
3334. **`js/js.translator/testData/box/vararg/jsExternalVarargCtor.kt`** -> AI Confidence: **99.17%**
3335. **`js/js.translator/testData/box/vararg/jsExternalVarargFun.kt`** -> AI Confidence: **99.17%**
3336. **`js/js.translator/testData/incremental/invalidation/crossModuleModifyClassAncestors/main/m.kt`** -> AI Confidence: **99.17%**
3337. **`js/js.translator/testData/incremental/invalidation/modifyClassAncestors/main/m.kt`** -> AI Confidence: **99.17%**
3338. **`js/js.translator/testData/lineNumbers/andAndWithSideEffect.kt`** -> AI Confidence: **99.17%**
3339. **`js/js.translator/testData/lineNumbers/catch.kt`** -> AI Confidence: **99.17%**
3340. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/MappingBridgeGeneratorImpl.kt`** -> AI Confidence: **99.17%**
3341. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/StubIrExtensions.kt`** -> AI Confidence: **99.17%**
3342. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/gradle/plugin/konan/KonanCliRunner.kt`** -> AI Confidence: **99.17%**
3343. **`kotlin-native/performance/ring/src/commonMain/kotlin/org/jetbrains/ring/OctoTest/basicTest.kt`** -> AI Confidence: **99.17%**
3344. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/internal/NumberConverter.kt`** -> AI Confidence: **99.17%**
3345. **`kotlin-native/tools/with-link-args/disable-stage.init.gradle.kts`** -> AI Confidence: **99.17%**
3346. **`libraries/kotlin.test/wasm/src/main/kotlin/kotlin/test/FrameworkTestArguments.kt`** -> AI Confidence: **99.17%**
3347. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/jsr223/propertiesFromContext.kt`** -> AI Confidence: **99.17%**
3348. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/util/identifiers.kt`** -> AI Confidence: **99.17%**
3349. **`libraries/stdlib/native-wasm/src/generated/_StringLowercase.kt`** -> AI Confidence: **99.17%**
3350. **`libraries/stdlib/src/kotlin/text/HexFormat.kt`** -> AI Confidence: **99.17%**
3351. **`libraries/stdlib/unsigned/src/kotlin/UProgressionUtil.kt`** -> AI Confidence: **99.17%**
3352. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/e_exp.kt`** -> AI Confidence: **99.17%**
3353. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/e_hypot.kt`** -> AI Confidence: **99.17%**
3354. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/e_rem_pio2.kt`** -> AI Confidence: **99.17%**
3355. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/s_atan.kt`** -> AI Confidence: **99.17%**
3356. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/s_expm1.kt`** -> AI Confidence: **99.17%**
3357. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/s_log1p.kt`** -> AI Confidence: **99.17%**
3358. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/s_rint.kt`** -> AI Confidence: **99.17%**
3359. **`libraries/stdlib/wasm/src/kotlin/text/FloatingPointParser.kt`** -> AI Confidence: **99.17%**
3360. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/compareLists.kt`** -> AI Confidence: **99.17%**
3361. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/legacyConfigurationConsumer/consumer/build.gradle.kts`** -> AI Confidence: **99.17%**
3362. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/AppleSdk.kt`** -> AI Confidence: **99.17%**
3363. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmRange.kt`** -> AI Confidence: **99.17%**
3364. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/semver.kt`** -> AI Confidence: **99.17%**
3365. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/internal/KotlinOptionsFreeArgsDeprecation.kt`** -> AI Confidence: **99.17%**
3366. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/formattingUtils.kt`** -> AI Confidence: **99.17%**
3367. **`libraries/tools/kotlin-stdlib-docs/build.gradle.kts`** -> AI Confidence: **99.17%**
3368. **`libraries/tools/kotlin-stdlib-gen/src/templates/Comparables.kt`** -> AI Confidence: **99.17%**
3369. **`libraries/tools/kotlin-stdlib-gen/src/templates/Elements.kt`** -> AI Confidence: **99.17%**
3370. **`libraries/tools/kotlin-stdlib-gen/src/templates/Ranges.kt`** -> AI Confidence: **99.17%**
3371. **`libraries/tools/kotlin-stdlib-gen/src/templates/Strings.kt`** -> AI Confidence: **99.17%**
3372. **`libraries/tools/kotlin-stdlib-gen/src/templates/dsl/FamilyProperties.kt`** -> AI Confidence: **99.17%**
3373. **`native/base/src/main/kotlin/org/jetbrains/kotlin/backend/konan/cKeywords.kt`** -> AI Confidence: **99.17%**
3374. **`native/objcexport-header-generator/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCInterfaceOrder.kt`** -> AI Confidence: **99.17%**
3375. **`native/swift/sir/src/org/jetbrains/kotlin/sir/SirCallableKind.kt`** -> AI Confidence: **99.17%**
3376. **`plugins/power-assert/power-assert-runtime/src/commonMain/kotlin/kotlin/powerassert/DefaultMessage.kt`** -> AI Confidence: **99.17%**
3377. **`plugins/scripting/scripting-compiler/testData/compiler/fib_std.kts`** -> AI Confidence: **99.17%**
3378. **`repo/gradle-build-conventions/gradle-plugins-common/src/main/kotlin/gradle-plugin-common-configuration.gradle.kts`** -> AI Confidence: **99.17%**
3379. **`repo/gradle-build-conventions/test-data-manager-convention/src/main/kotlin/test-data-manager-root.gradle.kts`** -> AI Confidence: **99.17%**
3380. **`repo/gradle-settings-conventions/kotlin-bootstrap/src/main/kotlin/kotlin-bootstrap.settings.gradle.kts`** -> AI Confidence: **99.17%**
3381. **`compiler/cli/bin/kotlinc`** -> AI Confidence: **99.17%**
3382. **`kotlin-native/tools/with-link-args/with-link-args`** -> AI Confidence: **99.17%**
3383. **`repo/scripts/create_branch_from_tag.sh`** -> AI Confidence: **99.17%**
3384. **`scripts/build-kotlin-compiler.sh`** -> AI Confidence: **99.17%**
3385. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/engine/repl.js`** -> AI Confidence: **99.17%**
3386. **`js/js.translator/testData/js-optimizer/while-condition-folding/doWhileWithNestedContinue.optimized.js`** -> AI Confidence: **99.17%**
3387. **`js/js.translator/testData/js-optimizer/while-condition-folding/doWhileWithNestedContinue.original.js`** -> AI Confidence: **99.17%**
3388. **`js/js.translator/testData/typescript-export/wasm/default/default__main.ts`** -> AI Confidence: **99.17%**
3389. **`js/js.translator/testData/typescript-export/wasm/generics/generics__main.ts`** -> AI Confidence: **99.17%**
3390. **`native/native.tests/testData/interop/objc/messaging/messaging.m`** -> AI Confidence: **99.17%**
3391. **`native/native.tests/testData/interop/objc/safepointSignposts/cinterop.m`** -> AI Confidence: **99.17%**
3392. **`native/native.tests/testData/interop/objc/tests/customString.m`** -> AI Confidence: **99.17%**
3393. **`native/native.tests/testData/interop/objc/tests/initWithCustomSelector.m`** -> AI Confidence: **99.17%**
3394. **`native/native.tests/testData/interop/swift/initWithExternalRCRef_leak/cinterop.m`** -> AI Confidence: **99.17%**
3395. **`kotlin-native/runtime/src/alloc/custom/cpp/FixedBlockPage.hpp`** -> AI Confidence: **99.17%**
3396. **`kotlin-native/runtime/src/alloc/custom/cpp/NextFitPage.hpp`** -> AI Confidence: **99.17%**
3397. **`kotlin-native/runtime/src/gcScheduler/common/cpp/HeapGrowthController.hpp`** -> AI Confidence: **99.17%**
3398. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/commonizeCurlInterop/libs/include/curl/typecheck-gcc.h`** -> AI Confidence: **99.17%**
3399. **`native/native.tests/testData/framework/objcexport/coroutines.swift`** -> AI Confidence: **99.17%**
3400. **`native/native.tests/testData/framework/objcexport/enumValues.swift`** -> AI Confidence: **99.17%**
3401. **`native/native.tests/testData/framework/objcexport/interfaceMethodNameMangling.swift`** -> AI Confidence: **99.17%**
3402. **`native/native.tests/testData/framework/objcexport/kt43780.swift`** -> AI Confidence: **99.17%**
3403. **`native/native.tests/testData/framework/objcexport/swiftNameMangling.swift`** -> AI Confidence: **99.17%**
3404. **`native/swift/swift-export-standalone-integration-tests/simple/testData/execution/char/char.swift`** -> AI Confidence: **99.17%**
3405. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/KotlinFe10CompilerPluginsProvider.kt`** -> AI Confidence: **99.16%**
3406. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10CompilerFacility.kt`** -> AI Confidence: **99.16%**
3407. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ScopeProvider.kt`** -> AI Confidence: **99.16%**
3408. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeInformationProvider.kt`** -> AI Confidence: **99.16%**
3409. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeRelationChecker.kt`** -> AI Confidence: **99.16%**
3410. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10VisibilityChecker.kt`** -> AI Confidence: **99.16%**
3411. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/scopes/KaFe10FileScope.kt`** -> AI Confidence: **99.16%**
3412. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/scopes/KaFe10ScopeResolution.kt`** -> AI Confidence: **99.16%**
3413. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/signatures/KaFe10FunctionSignature.kt`** -> AI Confidence: **99.16%**
3414. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescKotlinPropertySymbol.kt`** -> AI Confidence: **99.16%**
3415. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiKotlinPropertySymbol.kt`** -> AI Confidence: **99.16%**
3416. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiNamedClassSymbol.kt`** -> AI Confidence: **99.16%**
3417. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/Fe10SyntheticPropertyAccessorReference.kt`** -> AI Confidence: **99.16%**
3418. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10DefaultAnnotationArgumentReference.kt`** -> AI Confidence: **99.16%**
3419. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/base/KtFe10PolyVariantResolver.kt`** -> AI Confidence: **99.16%**
3420. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/base/KtFe10Reference.kt`** -> AI Confidence: **99.16%**
3421. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/FirSyntheticFunctionInterfaceSourceProvider.kt`** -> AI Confidence: **99.16%**
3422. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaFirSessionProvider.kt`** -> AI Confidence: **99.16%**
3423. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaSymbolByFirBuilder.kt`** -> AI Confidence: **99.16%**
3424. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/annotations/firAnnotationUtils.kt`** -> AI Confidence: **99.16%**
3425. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompilerPluginGeneratedDeclarationsProvider.kt`** -> AI Confidence: **99.16%**
3426. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompletionCandidateChecker.kt`** -> AI Confidence: **99.16%**
3427. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirJavaInteroperabilityComponent.kt`** -> AI Confidence: **99.16%**
3428. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolveExtensionInfoProvider.kt`** -> AI Confidence: **99.16%**
3429. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirScopeProvider.kt`** -> AI Confidence: **99.16%**
3430. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSymbolInformationProvider.kt`** -> AI Confidence: **99.16%**
3431. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirTypeProvider.kt`** -> AI Confidence: **99.16%**
3432. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirTypeRelationChecker.kt`** -> AI Confidence: **99.16%**
3433. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/referenceShortenerUtils.kt`** -> AI Confidence: **99.16%**
3434. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/projectStructure/KaFirLibraryTargetPlatformContentScopeRefiner.kt`** -> AI Confidence: **99.16%**
3435. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirReference.kt`** -> AI Confidence: **99.16%**
3436. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/DeclarationsInPackageProvider.kt`** -> AI Confidence: **99.16%**
3437. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/KaFirFileScope.kt`** -> AI Confidence: **99.16%**
3438. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirBackingFieldSymbol.kt`** -> AI Confidence: **99.16%**
3439. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirConstructorSymbol.kt`** -> AI Confidence: **99.16%**
3440. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSymbol.kt`** -> AI Confidence: **99.16%**
3441. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirTypeParameterSymbol.kt`** -> AI Confidence: **99.16%**
3442. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/firSymbolUtils.kt`** -> AI Confidence: **99.16%**
3443. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirEnumEntrySymbolPointer.kt`** -> AI Confidence: **99.16%**
3444. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirJavaSyntheticPropertyAccessorFunctionSymbolPointer.kt`** -> AI Confidence: **99.16%**
3445. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirJavaSyntheticPropertySymbolPointer.kt`** -> AI Confidence: **99.16%**
3446. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirLocalClassFromCompilerPluginSymbolPointer.kt`** -> AI Confidence: **99.16%**
3447. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirMemberSymbolPointer.kt`** -> AI Confidence: **99.16%**
3448. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirNestedInLocalClassFromCompilerPluginSymbolPointer.kt`** -> AI Confidence: **99.16%**
3449. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirResultPropertySymbolPointer.kt`** -> AI Confidence: **99.16%**
3450. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTopLevelFunctionSymbolPointer.kt`** -> AI Confidence: **99.16%**
3451. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTopLevelPropertySymbolPointer.kt`** -> AI Confidence: **99.16%**
3452. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTypeAliasedConstructorMemberPointer.kt`** -> AI Confidence: **99.16%**
3453. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirClassErrorType.kt`** -> AI Confidence: **99.16%**
3454. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/qualifiers/UsualClassTypeQualifierBuilder.kt`** -> AI Confidence: **99.16%**
3455. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/typeCreation/KaFirTypeCreator.kt`** -> AI Confidence: **99.16%**
3456. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/ConeDiagnosticPointer.kt`** -> AI Confidence: **99.16%**
3457. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/ktSymbolUtils.kt`** -> AI Confidence: **99.16%**
3458. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/typeUtils.kt`** -> AI Confidence: **99.16%**
3459. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/annotations/KaAnnotationImpl.kt`** -> AI Confidence: **99.16%**
3460. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseSignatureSubstitutor.kt`** -> AI Confidence: **99.16%**
3461. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/contracts/description/KaBaseValues.kt`** -> AI Confidence: **99.16%**
3462. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/references/KotlinReferenceProvidersServiceImpl.kt`** -> AI Confidence: **99.16%**
3463. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/symbols/pointers/KaBasePsiSymbolPointer.kt`** -> AI Confidence: **99.16%**
3464. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/util/kotlinPsiUtils.kt`** -> AI Confidence: **99.16%**
3465. **`analysis/analysis-api-standalone/analysis-api-fir-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneFirDirectInheritorsProvider.kt`** -> AI Confidence: **99.16%**
3466. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneDeclarationIndexImpl.kt`** -> AI Confidence: **99.16%**
3467. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneDeclarationProvider.kt`** -> AI Confidence: **99.16%**
3468. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/projectStructure/ApplicationServiceRegistration.kt`** -> AI Confidence: **99.16%**
3469. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/projectStructure/PluginStructureProvider.kt`** -> AI Confidence: **99.16%**
3470. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/impl/KaModuleUtils.kt`** -> AI Confidence: **99.16%**
3471. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/impl/KotlinStandaloneProjectStructureProvider.kt`** -> AI Confidence: **99.16%**
3472. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaTypeInformationProvider.kt`** -> AI Confidence: **99.16%**
3473. **`analysis/decompiled/decompiler-native/src/org/jetbrains/kotlin/analysis/decompiler/konan/KlibLoadingMetadataCache.kt`** -> AI Confidence: **99.16%**
3474. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/KotlinBuiltInDecompiler.kt`** -> AI Confidence: **99.16%**
3475. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/ClsContractBuilder.kt`** -> AI Confidence: **99.16%**
3476. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/KotlinAsJavaSupportBase.kt`** -> AI Confidence: **99.16%**
3477. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/elements/FakeFileForLightClass.kt`** -> AI Confidence: **99.16%**
3478. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/InvalidFirElementTypeException.kt`** -> AI Confidence: **99.16%**
3479. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/AbstractFirIdeDiagnosticsCollector.kt`** -> AI Confidence: **99.16%**
3480. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/FileStructure.kt`** -> AI Confidence: **99.16%**
3481. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/FirLazyBodiesCalculator.kt`** -> AI Confidence: **99.16%**
3482. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/LLFirResolveDesignationCollector.kt`** -> AI Confidence: **99.16%**
3483. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirIdePredicateBasedProvider.kt`** -> AI Confidence: **99.16%**
3484. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirPrivateVisibleFromDifferentModuleExtension.kt`** -> AI Confidence: **99.16%**
3485. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/resolver/SingleCandidateResolver.kt`** -> AI Confidence: **99.16%**
3486. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/FirScriptingCompilerExtensionIdeRegistrar.kt`** -> AI Confidence: **99.16%**
3487. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirSessionCache.kt`** -> AI Confidence: **99.16%**
3488. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirSessionCacheStorageInvalidator.kt`** -> AI Confidence: **99.16%**
3489. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/DeserializedContainerSourceProviders.kt`** -> AI Confidence: **99.16%**
3490. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedAnnotationDeserializer.kt`** -> AI Confidence: **99.16%**
3491. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedFirContractDeserializer.kt`** -> AI Confidence: **99.16%**
3492. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedFirMemberDeserializer.kt`** -> AI Confidence: **99.16%**
3493. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinSourceSymbolProvider.kt`** -> AI Confidence: **99.16%**
3494. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinStubBasedLibrarySymbolProvider.kt`** -> AI Confidence: **99.16%**
3495. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/combined/LLCombinedKotlinSymbolProvider.kt`** -> AI Confidence: **99.16%**
3496. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/combined/LLCombinedPackageDelegationSymbolProvider.kt`** -> AI Confidence: **99.16%**
3497. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirAnnotationArgumentsLazyResolver.kt`** -> AI Confidence: **99.16%**
3498. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirCompilerAnnotationsLazyResolver.kt`** -> AI Confidence: **99.16%**
3499. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirImplicitTypesLazyResolver.kt`** -> AI Confidence: **99.16%**
3500. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirStatusLazyResolver.kt`** -> AI Confidence: **99.16%**
3501. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirSupertypeLazyResolver.kt`** -> AI Confidence: **99.16%**
3502. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirTargetResolver.kt`** -> AI Confidence: **99.16%**
3503. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirTypeLazyResolver.kt`** -> AI Confidence: **99.16%**
3504. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/PostponedSymbolsForAnnotationResolutionAttribute.kt`** -> AI Confidence: **99.16%**
3505. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/FirElementFinder.kt`** -> AI Confidence: **99.16%**
3506. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/LLFlightRecorder.kt`** -> AI Confidence: **99.16%**
3507. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/firCheckResolvedUtils.kt`** -> AI Confidence: **99.16%**
3508. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/utils.kt`** -> AI Confidence: **99.16%**
3509. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/AbstractFirLazyDeclarationResolveTestCase.kt`** -> AI Confidence: **99.16%**
3510. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/compiler/based/LLDiagnosticParameterChecker.kt`** -> AI Confidence: **99.16%**
3511. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/services/PackagePartProviderTestImpl.kt`** -> AI Confidence: **99.16%**
3512. **`build-common/src/org/jetbrains/kotlin/incremental/CompilationTransaction.kt`** -> AI Confidence: **99.16%**
3513. **`build-common/src/org/jetbrains/kotlin/incremental/IncrementalJsCache.kt`** -> AI Confidence: **99.16%**
3514. **`build-common/src/org/jetbrains/kotlin/incremental/protoDifferenceUtils.kt`** -> AI Confidence: **99.16%**
3515. **`build-common/src/org/jetbrains/kotlin/incremental/storage/LazyStorage.kt`** -> AI Confidence: **99.16%**
3516. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/serialization/json/ReleaseDependentSerializer.kt`** -> AI Confidence: **99.16%**
3517. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/serialization/json/base/SetTypeSerializer.kt`** -> AI Confidence: **99.16%**
3518. **`compiler/backend/src/org/jetbrains/kotlin/codegen/AssertCodegenUtil.kt`** -> AI Confidence: **99.16%**
3519. **`compiler/backend/src/org/jetbrains/kotlin/codegen/ClassFileFactory.kt`** -> AI Confidence: **99.16%**
3520. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/GeneratedCodeMarkers.kt`** -> AI Confidence: **99.16%**
3521. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/ObjectTransformer.kt`** -> AI Confidence: **99.16%**
3522. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/SourceCompilerForInline.kt`** -> AI Confidence: **99.16%**
3523. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/OptimizationMethodVisitor.kt`** -> AI Confidence: **99.16%**
3524. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/BoxedBasicValue.kt`** -> AI Confidence: **99.16%**
3525. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/FixStackAnalyzer.kt`** -> AI Confidence: **99.16%**
3526. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/FixStackContext.kt`** -> AI Confidence: **99.16%**
3527. **`compiler/backend/src/org/jetbrains/kotlin/codegen/state/typeMappingUtil.kt`** -> AI Confidence: **99.16%**
3528. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/scenario/dslModuleCache.kt`** -> AI Confidence: **99.16%**
3529. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/CompilationServiceImpl.kt`** -> AI Confidence: **99.16%**
3530. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/jvm/operations/JvmCompilationOperationImpl.kt`** -> AI Confidence: **99.16%**
3531. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/CliTrace.kt`** -> AI Confidence: **99.16%**
3532. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/JvmPackagePartProvider.kt`** -> AI Confidence: **99.16%**
3533. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/KotlinCliJavaFileManagerImpl.kt`** -> AI Confidence: **99.16%**
3534. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/IcCaches.kt`** -> AI Confidence: **99.16%**
3535. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebFrontendPipelinePhase.kt`** -> AI Confidence: **99.16%**
3536. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/wasm/KotlinIr2WasmIrCompiler.kt`** -> AI Confidence: **99.16%**
3537. **`compiler/cli/cli-jvm/javac-integration/src/org/jetbrains/kotlin/cli/jvm/javac/JavacWrapperKotlinResolverImpl.kt`** -> AI Confidence: **99.16%**
3538. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmConfigurationPipelinePhase.kt`** -> AI Confidence: **99.16%**
3539. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/pipeline/metadata/MetadataConfigurationPipelinePhase.kt`** -> AI Confidence: **99.16%**
3540. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/writeKlib.kt`** -> AI Confidence: **99.16%**
3541. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/FirSessionConstructionUtils.kt`** -> AI Confidence: **99.16%**
3542. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/arguments.kt`** -> AI Confidence: **99.16%**
3543. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/fir/FirDiagnosticsCompilerResultsReporter.kt`** -> AI Confidence: **99.16%**
3544. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/messages/AnalyzerWithCompilerReport.kt`** -> AI Confidence: **99.16%**
3545. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/utils.kt`** -> AI Confidence: **99.16%**
3546. **`compiler/cli/src/org/jetbrains/kotlin/cli/jvm/compiler/VfsBasedProjectEnvironment.kt`** -> AI Confidence: **99.16%**
3547. **`compiler/cli/src/org/jetbrains/kotlin/cli/jvm/plugins/PluginCliParser.kt`** -> AI Confidence: **99.16%**
3548. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/FrontendFilesForPluginsGenerationPipelinePhase.kt`** -> AI Confidence: **99.16%**
3549. **`compiler/compiler-runner-unshaded/src/org/jetbrains/kotlin/compilerRunner/KotlinCompilerRunnerUtils.kt`** -> AI Confidence: **99.16%**
3550. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/KotlinCompileDaemon.kt`** -> AI Confidence: **99.16%**
3551. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/KotlinRemoteReplService.kt`** -> AI Confidence: **99.16%**
3552. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/report/BuildReportICReporter.kt`** -> AI Confidence: **99.16%**
3553. **`compiler/fir/analysis-tests/legacy-fir-tests/testFixtures/org/jetbrains/kotlin/fir/java/JavaClassRendering.kt`** -> AI Confidence: **99.16%**
3554. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsActualExternalInterfaceSuggestJsNoRuntimeChecker.kt`** -> AI Confidence: **99.16%**
3555. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExportedActualMatchExpectChecker.kt`** -> AI Confidence: **99.16%**
3556. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExternalChecker.kt`** -> AI Confidence: **99.16%**
3557. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExternalFileChecker.kt`** -> AI Confidence: **99.16%**
3558. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsModuleChecker.kt`** -> AI Confidence: **99.16%**
3559. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNameCharsChecker.kt`** -> AI Confidence: **99.16%**
3560. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNameClashFileTopLevelDeclarationsChecker.kt`** -> AI Confidence: **99.16%**
3561. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNoRuntimeDeclarationChecker.kt`** -> AI Confidence: **99.16%**
3562. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsRuntimeAnnotationChecker.kt`** -> AI Confidence: **99.16%**
3563. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsDefinedExternallyCallChecker.kt`** -> AI Confidence: **99.16%**
3564. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsNoRuntimeUsageCheckers.kt`** -> AI Confidence: **99.16%**
3565. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirAccidentalOverrideClashChecker.kt`** -> AI Confidence: **99.16%**
3566. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirImplementationByDelegationWithDifferentGenericSignatureChecker.kt`** -> AI Confidence: **99.16%**
3567. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJavaClassInheritsKtPrivateClassDeclarationChecker.kt`** -> AI Confidence: **99.16%**
3568. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmFunctionDelegateMemberNameClashChecker.kt`** -> AI Confidence: **99.16%**
3569. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirOverloadsChecker.kt`** -> AI Confidence: **99.16%**
3570. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirOverrideJavaNullabilityWarningChecker.kt`** -> AI Confidence: **99.16%**
3571. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirRepeatableAnnotationChecker.kt`** -> AI Confidence: **99.16%**
3572. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirArrayOfNullableNothingExpressionChecker.kt`** -> AI Confidence: **99.16%**
3573. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirInterfaceDefaultMethodCallChecker.kt`** -> AI Confidence: **99.16%**
3574. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaAnnotationsChecker.kt`** -> AI Confidence: **99.16%**
3575. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaClassOnCompanionChecker.kt`** -> AI Confidence: **99.16%**
3576. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaSamInterfaceConstructorReferenceChecker.kt`** -> AI Confidence: **99.16%**
3577. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmIdentityEqualsOnJavaValueBasedClass.kt`** -> AI Confidence: **99.16%**
3578. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmIdentitySensitiveCallWithValueTypeObjectChecker.kt`** -> AI Confidence: **99.16%**
3579. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmInconsistentOperatorFromJavaCallChecker.kt`** -> AI Confidence: **99.16%**
3580. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmMissingBuiltInDeclarationChecker.kt`** -> AI Confidence: **99.16%**
3581. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmModuleAccessibilityQualifiedAccessChecker.kt`** -> AI Confidence: **99.16%**
3582. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmPackageNameAnnotationsChecker.kt`** -> AI Confidence: **99.16%**
3583. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmPolymorphicSignatureCallChecker.kt`** -> AI Confidence: **99.16%**
3584. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirSyntheticPropertyWithoutJavaOriginChecker.kt`** -> AI Confidence: **99.16%**
3585. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeExternalDeclarationChecker.kt`** -> AI Confidence: **99.16%**
3586. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeForwardDeclarationTypeOperatorChecker.kt`** -> AI Confidence: **99.16%**
3587. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeHiddenFromObjCInheritanceChecker.kt`** -> AI Confidence: **99.16%**
3588. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeIdentityHashCodeCallOnValueTypeObjectChecker.kt`** -> AI Confidence: **99.16%**
3589. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCNameUtilities.kt`** -> AI Confidence: **99.16%**
3590. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCOverrideInitChecker.kt`** -> AI Confidence: **99.16%**
3591. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCStringAsVariadicChecker.kt`** -> AI Confidence: **99.16%**
3592. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjcOverrideApplicabilityChecker.kt`** -> AI Confidence: **99.16%**
3593. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeSharedImmutableChecker.kt`** -> AI Confidence: **99.16%**
3594. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeSpecificAtomicChecker.kt`** -> AI Confidence: **99.16%**
3595. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeThreadLocalChecker.kt`** -> AI Confidence: **99.16%**
3596. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeVariadicFunctionPointerChecker.kt`** -> AI Confidence: **99.16%**
3597. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/FirWasmJsCastChecker.kt`** -> AI Confidence: **99.16%**
3598. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/FirWasmJsCodeHelpers.kt`** -> AI Confidence: **99.16%**
3599. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmExportAnnotationChecker.kt`** -> AI Confidence: **99.16%**
3600. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmExternalChecker.kt`** -> AI Confidence: **99.16%**
3601. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmImportAnnotationChecker.kt`** -> AI Confidence: **99.16%**
3602. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmJsAssociatedObjectChecker.kt`** -> AI Confidence: **99.16%**
3603. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmJsModuleChecker.kt`** -> AI Confidence: **99.16%**
3604. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmWasiExternalDeclarationChecker.kt`** -> AI Confidence: **99.16%**
3605. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirJsExportAnnotationChecker.kt`** -> AI Confidence: **99.16%**
3606. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirAbstractNativeRttiChecker.kt`** -> AI Confidence: **99.16%**
3607. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirJsCodeConstantArgumentChecker.kt`** -> AI Confidence: **99.16%**
3608. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/FirOverridesBackwardCompatibilityHelper.kt`** -> AI Confidence: **99.16%**
3609. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/FirSourceUtils.kt`** -> AI Confidence: **99.16%**
3610. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/FirPropertyInitializationAnalyzer.kt`** -> AI Confidence: **99.16%**
3611. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FE10LikeConeSubstitutor.kt`** -> AI Confidence: **99.16%**
3612. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirInlineCheckerPlatformSpecificComponent.kt`** -> AI Confidence: **99.16%**
3613. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirTypeCompatibilityHelpers.kt`** -> AI Confidence: **99.16%**
3614. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/SourceNavigator.kt`** -> AI Confidence: **99.16%**
3615. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/config/FirOptInLanguageVersionSettingsChecker.kt`** -> AI Confidence: **99.16%**
3616. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirActualAnnotationsMatchExpectChecker.kt`** -> AI Confidence: **99.16%**
3617. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnyTypeAliasChecker.kt`** -> AI Confidence: **99.16%**
3618. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCompanionExtensionChecker.kt`** -> AI Confidence: **99.16%**
3619. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirConstructorAllowedChecker.kt`** -> AI Confidence: **99.16%**
3620. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirContextReceiversDeprecatedDeclarationChecker.kt`** -> AI Confidence: **99.16%**
3621. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirContextualPropertyWithBackingFieldChecker.kt`** -> AI Confidence: **99.16%**
3622. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDataClassNonPublicConstructorChecker.kt`** -> AI Confidence: **99.16%**
3623. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDataObjectContentChecker.kt`** -> AI Confidence: **99.16%**
3624. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDelegateFieldTypeMismatchChecker.kt`** -> AI Confidence: **99.16%**
3625. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDelegatedPropertyChecker.kt`** -> AI Confidence: **99.16%**
3626. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExplicitBackingFieldForbiddenChecker.kt`** -> AI Confidence: **99.16%**
3627. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFunctionReturnChecker.kt`** -> AI Confidence: **99.16%**
3628. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInitializerTypeMismatchChecker.kt`** -> AI Confidence: **99.16%**
3629. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlineBodySimpleFunctionChecker.kt`** -> AI Confidence: **99.16%**
3630. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirLocalEntityNotAllowedChecker.kt`** -> AI Confidence: **99.16%**
3631. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMultipleDefaultsInheritedFromSupertypesChecker.kt`** -> AI Confidence: **99.16%**
3632. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNonMemberFunctionsChecker.kt`** -> AI Confidence: **99.16%**
3633. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNotImplementedOverrideSimpleEnumEntryChecker.kt`** -> AI Confidence: **99.16%**
3634. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirObjectConstructorChecker.kt`** -> AI Confidence: **99.16%**
3635. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOperatorModifierChecker.kt`** -> AI Confidence: **99.16%**
3636. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptInImportsChecker.kt`** -> AI Confidence: **99.16%**
3637. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPrimaryConstructorSuperTypeChecker.kt`** -> AI Confidence: **99.16%**
3638. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPublishedApiChecker.kt`** -> AI Confidence: **99.16%**
3639. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTailrecFunctionChecker.kt`** -> AI Confidence: **99.16%**
3640. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTypeParametersInObjectChecker.kt`** -> AI Confidence: **99.16%**
3641. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirUnnamedPropertyChecker.kt`** -> AI Confidence: **99.16%**
3642. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/crv/FirReturnValueOverrideChecker.kt`** -> AI Confidence: **99.16%**
3643. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/crv/helpers.kt`** -> AI Confidence: **99.16%**
3644. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/ArrayEqualityCanBeReplacedWithContentEquals.kt`** -> AI Confidence: **99.16%**
3645. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirAbstractClassInstantiationChecker.kt`** -> AI Confidence: **99.16%**
3646. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirAbstractSuperCallChecker.kt`** -> AI Confidence: **99.16%**
3647. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirArrayOfNothingQualifierChecker.kt`** -> AI Confidence: **99.16%**
3648. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCallableReferenceChecker.kt`** -> AI Confidence: **99.16%**
3649. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCommonAtomicReferenceToPrimitiveCallChecker.kt`** -> AI Confidence: **99.16%**
3650. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirContextParameterInCalledSignatureChecker.kt`** -> AI Confidence: **99.16%**
3651. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirContractNotFirstStatementChecker.kt`** -> AI Confidence: **99.16%**
3652. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCustomEnumEntriesMigrationAccessChecker.kt`** -> AI Confidence: **99.16%**
3653. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDeprecatedSmartCastChecker.kt`** -> AI Confidence: **99.16%**
3654. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDivisionByZeroChecker.kt`** -> AI Confidence: **99.16%**
3655. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDslMarkerUseSiteChecker.kt`** -> AI Confidence: **99.16%**
3656. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirExpressionAnnotationChecker.kt`** -> AI Confidence: **99.16%**
3657. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirIncompatibleClassExpressionChecker.kt`** -> AI Confidence: **99.16%**
3658. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineExposedLessVisibleTypeQualifiedAccessChecker.kt`** -> AI Confidence: **99.16%**
3659. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirMissingDependencySupertypeInQualifiedAccessExpressionsChecker.kt`** -> AI Confidence: **99.16%**
3660. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirNotNullAssertionChecker.kt`** -> AI Confidence: **99.16%**
3661. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptionalExpectationExpressionChecker.kt`** -> AI Confidence: **99.16%**
3662. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirProtectedConstructorNotInSuperCallChecker.kt`** -> AI Confidence: **99.16%**
3663. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirRecursiveProblemChecker.kt`** -> AI Confidence: **99.16%**
3664. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSpreadOfNullableChecker.kt`** -> AI Confidence: **99.16%**
3665. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSuperCallWithDefaultsChecker.kt`** -> AI Confidence: **99.16%**
3666. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSuperReferenceChecker.kt`** -> AI Confidence: **99.16%**
3667. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSuperclassNotAccessibleFromInterfaceChecker.kt`** -> AI Confidence: **99.16%**
3668. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTypeParameterInQualifiedAccessChecker.kt`** -> AI Confidence: **99.16%**
3669. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUninitializedEnumChecker.kt`** -> AI Confidence: **99.16%**
3670. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUnsupportedArrayLiteralChecker.kt`** -> AI Confidence: **99.16%**
3671. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUselessElvisChecker.kt`** -> AI Confidence: **99.16%**
3672. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirVarargWithNonTrivialUpperBoundInferredToNothingChecker.kt`** -> AI Confidence: **99.16%**
3673. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirVisibilityQualifierChecker.kt`** -> AI Confidence: **99.16%**
3674. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/FirUnusedExpressionChecker.kt`** -> AI Confidence: **99.16%**
3675. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantModalityModifierSyntaxChecker.kt`** -> AI Confidence: **99.16%**
3676. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantReturnUnitType.kt`** -> AI Confidence: **99.16%**
3677. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantSingleExpressionStringTemplateChecker.kt`** -> AI Confidence: **99.16%**
3678. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirDelegationInInterfaceSyntaxChecker.kt`** -> AI Confidence: **99.16%**
3679. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirMissingConstructorKeywordSyntaxChecker.kt`** -> AI Confidence: **99.16%**
3680. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirPrefixAndSuffixSyntaxChecker.kt`** -> AI Confidence: **99.16%**
3681. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirUnresolvedInMiddleOfImportChecker.kt`** -> AI Confidence: **99.16%**
3682. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirWhenGuardChecker.kt`** -> AI Confidence: **99.16%**
3683. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirContextualFunctionTypeChecker.kt`** -> AI Confidence: **99.16%**
3684. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDeprecatedTypeChecker.kt`** -> AI Confidence: **99.16%**
3685. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirInlineExposedLessVisibleTypeChecker.kt`** -> AI Confidence: **99.16%**
3686. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirMissingDependencyClassInTypeAliasTypeChecker.kt`** -> AI Confidence: **99.16%**
3687. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirOptionalExpectationTypeChecker.kt`** -> AI Confidence: **99.16%**
3688. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirSuspendModifierChecker.kt`** -> AI Confidence: **99.16%**
3689. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirUnsupportedModifiersInFunctionTypeParameterChecker.kt`** -> AI Confidence: **99.16%**
3690. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirUpperBoundViolatedTypeChecker.kt`** -> AI Confidence: **99.16%**
3691. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/RedundantNullableChecker.kt`** -> AI Confidence: **99.16%**
3692. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/AbstractDiagnosticCollector.kt`** -> AI Confidence: **99.16%**
3693. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/AbstractDiagnosticCollectorVisitor.kt`** -> AI Confidence: **99.16%**
3694. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/components/ControlFlowAnalysisDiagnosticComponent.kt`** -> AI Confidence: **99.16%**
3695. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/components/LossDiagnosticCollectorComponent.kt`** -> AI Confidence: **99.16%**
3696. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/IncrementalPassThroughLookupTrackerComponent.kt`** -> AI Confidence: **99.16%**
3697. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/backend/LenientModeMissingActualDeclarationProvider.kt`** -> AI Confidence: **99.16%**
3698. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/ConstInliner.kt`** -> AI Confidence: **99.16%**
3699. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/analyse.kt`** -> AI Confidence: **99.16%**
3700. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/convertToIr.kt`** -> AI Confidence: **99.16%**
3701. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/referenceAllCommonDependencies.kt`** -> AI Confidence: **99.16%**
3702. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirAbstractSessionFactory.kt`** -> AI Confidence: **99.16%**
3703. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/KlibBasedAnnotationDeserializer.kt`** -> AI Confidence: **99.16%**
3704. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/MetadataLibraryBasedSymbolProvider.kt`** -> AI Confidence: **99.16%**
3705. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/AbstractFirDeserializedSymbolProvider.kt`** -> AI Confidence: **99.16%**
3706. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/AnnotationDeserializationUtil.kt`** -> AI Confidence: **99.16%**
3707. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirContractDeserializer.kt`** -> AI Confidence: **99.16%**
3708. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirMemberDeserializer.kt`** -> AI Confidence: **99.16%**
3709. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JavaScopeProvider.kt`** -> AI Confidence: **99.16%**
3710. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JvmSupertypeUpdater.kt`** -> AI Confidence: **99.16%**
3711. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/utils.kt`** -> AI Confidence: **99.16%**
3712. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/FirJvmConstDeserializer.kt`** -> AI Confidence: **99.16%**
3713. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/OptionalAnnotationClassesProvider.kt`** -> AI Confidence: **99.16%**
3714. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/enhancement/FirAnnotationTypeQualifierResolver.kt`** -> AI Confidence: **99.16%**
3715. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaClassUseSiteMemberScope.kt`** -> AI Confidence: **99.16%**
3716. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaOverridabilityRules.kt`** -> AI Confidence: **99.16%**
3717. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaOverrideChecker.kt`** -> AI Confidence: **99.16%**
3718. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/resolve/scopes/JvmMappedScopes.kt`** -> AI Confidence: **99.16%**
3719. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/scopes/jvm/FirJvmDelegatedMembersFilter.kt`** -> AI Confidence: **99.16%**
3720. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/scopes/jvm/JvmMappedScope.kt`** -> AI Confidence: **99.16%**
3721. **`compiler/fir/fir-native/src/org/jetbrains/kotlin/fir/backend/native/FirNativeOverrideChecker.kt`** -> AI Confidence: **99.16%**
3722. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/firKlibSerialization.kt`** -> AI Confidence: **99.16%**
3723. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmElementAwareStringTable.kt`** -> AI Confidence: **99.16%**
3724. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmTypeMapper.kt`** -> AI Confidence: **99.16%**
3725. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirMetadataSerializer.kt`** -> AI Confidence: **99.16%**
3726. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrBuiltinSymbolsContainer.kt`** -> AI Confidence: **99.16%**
3727. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrConverter.kt`** -> AI Confidence: **99.16%**
3728. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrDeclarationStorage.kt`** -> AI Confidence: **99.16%**
3729. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrPluginContext.kt`** -> AI Confidence: **99.16%**
3730. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/FirExportCheckerVisitor.kt`** -> AI Confidence: **99.16%**
3731. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrClassifiersGenerator.kt`** -> AI Confidence: **99.16%**
3732. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrDataClassMembersGenerator.kt`** -> AI Confidence: **99.16%**
3733. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrLazyDeclarationsGenerator.kt`** -> AI Confidence: **99.16%**
3734. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/ScopeUtils.kt`** -> AI Confidence: **99.16%**
3735. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyClass.kt`** -> AI Confidence: **99.16%**
3736. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyProperty.kt`** -> AI Confidence: **99.16%**
3737. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyPropertyAccessor.kt`** -> AI Confidence: **99.16%**
3738. **`compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/FirResolveModularizedTotalKotlinTestPure.kt`** -> AI Confidence: **99.16%**
3739. **`compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/NonFirResolveModularizedTotalKotlinTestPure.kt`** -> AI Confidence: **99.16%**
3740. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/extensions/FirExtensionDeclarationsSymbolProvider.kt`** -> AI Confidence: **99.16%**
3741. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/extensions/FirSwitchableExtensionDeclarationsSymbolProvider.kt`** -> AI Confidence: **99.16%**
3742. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/LookupTagUtils.kt`** -> AI Confidence: **99.16%**
3743. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/ToSymbolUtils.kt`** -> AI Confidence: **99.16%**
3744. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/FirKotlinScopeProvider.kt`** -> AI Confidence: **99.16%**
3745. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirDeclaredMemberScopeProvider.kt`** -> AI Confidence: **99.16%**
3746. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirFakeOverrideGenerator.kt`** -> AI Confidence: **99.16%**
3747. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirIntegerConstantOperatorScope.kt`** -> AI Confidence: **99.16%**
3748. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirOverrideUtils.kt`** -> AI Confidence: **99.16%**
3749. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirPackageMemberScope.kt`** -> AI Confidence: **99.16%**
3750. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirSingleLevelDefaultStarImportingScope.kt`** -> AI Confidence: **99.16%**
3751. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/fir/ClassWrapper.kt`** -> AI Confidence: **99.16%**
3752. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/fir/ValueParameter.kt`** -> AI Confidence: **99.16%**
3753. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/Context.kt`** -> AI Confidence: **99.16%**
3754. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/Destructuring.kt`** -> AI Confidence: **99.16%**
3755. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirPredicateBasedProviderImpl.kt`** -> AI Confidence: **99.16%**
3756. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/CollectionLiteralResolution.kt`** -> AI Confidence: **99.16%**
3757. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/CollectionLiteralResolutionUtils.kt`** -> AI Confidence: **99.16%**
3758. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/StdlibFactoryFunctionsUtils.kt`** -> AI Confidence: **99.16%**
3759. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/ConeResolutionAtoms.kt`** -> AI Confidence: **99.16%**
3760. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/ConstructorProcessing.kt`** -> AI Confidence: **99.16%**
3761. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/CandidateCollector.kt`** -> AI Confidence: **99.16%**
3762. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/ResolutionStageRunner.kt`** -> AI Confidence: **99.16%**
3763. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/TypeArgumentMapping.kt`** -> AI Confidence: **99.16%**
3764. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/FirTowerResolver.kt`** -> AI Confidence: **99.16%**
3765. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/TowerLevelHandler.kt`** -> AI Confidence: **99.16%**
3766. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/PostponedArgumentsAnalyzer.kt`** -> AI Confidence: **99.16%**
3767. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirCommonDeclarationsMappingSymbolProvider.kt`** -> AI Confidence: **99.16%**
3768. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirQualifierResolverImpl.kt`** -> AI Confidence: **99.16%**
3769. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirSealedClassInheritorsProcessor.kt`** -> AI Confidence: **99.16%**
3770. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirStatusResolveTransformer.kt`** -> AI Confidence: **99.16%**
3771. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirSyntheticCallGenerator.kt`** -> AI Confidence: **99.16%**
3772. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirTotalResolveProcessor.kt`** -> AI Confidence: **99.16%**
3773. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/IntegerLiteralAndOperatorApproximationTransformer.kt`** -> AI Confidence: **99.16%**
3774. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/BodyResolveUtils.kt`** -> AI Confidence: **99.16%**
3775. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirArrayOfCallTransformer.kt`** -> AI Confidence: **99.16%**
3776. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/LocalClassesResolution.kt`** -> AI Confidence: **99.16%**
3777. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/AbstractFirSpecificAnnotationResolveTransformer.kt`** -> AI Confidence: **99.16%**
3778. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/FirAnnotationArgumentsTransformer.kt`** -> AI Confidence: **99.16%**
3779. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/FirCompanionGenerationProcessor.kt`** -> AI Confidence: **99.16%**
3780. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/FirCompilerRequiredAnnotationsResolveTransformer.kt`** -> AI Confidence: **99.16%**
3781. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/scopes/ImportingScopes.kt`** -> AI Confidence: **99.16%**
3782. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/scopes/impl/FirActualizingScope.kt`** -> AI Confidence: **99.16%**
3783. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/FirLookupTrackerComponent.kt`** -> AI Confidence: **99.16%**
3784. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/declarations/ImplicitReceiverUtils.kt`** -> AI Confidence: **99.16%**
3785. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/expressions/ReferenceUtils.kt`** -> AI Confidence: **99.16%**
3786. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/ImplicitValueStorage.kt`** -> AI Confidence: **99.16%**
3787. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/DfaVariables.kt`** -> AI Confidence: **99.16%**
3788. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/cfg/CFGNode.kt`** -> AI Confidence: **99.16%**
3789. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/transformers/publishedApiEffectiveVisibility.kt`** -> AI Confidence: **99.16%**
3790. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/FirBasedSymbol.kt`** -> AI Confidence: **99.16%**
3791. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/FirClassLikeSymbol.kt`** -> AI Confidence: **99.16%**
3792. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/visitors/FirDefaultTransformer.kt`** -> AI Confidence: **99.16%**
3793. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/LightTreePositioningStrategy.kt`** -> AI Confidence: **99.16%**
3794. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/VirtualFileKotlinClass.kt`** -> AI Confidence: **99.16%**
3795. **`compiler/frontend.common/src/org/jetbrains/kotlin/KtSourceElement.kt`** -> AI Confidence: **99.16%**
3796. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/sam/JavaBasedSamConversionResolver.kt`** -> AI Confidence: **99.16%**
3797. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/BadInheritedJavaSignaturesChecker.kt`** -> AI Confidence: **99.16%**
3798. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/DefaultCheckerInTailrec.kt`** -> AI Confidence: **99.16%**
3799. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/EnumDeclaringClassDeprecationChecker.kt`** -> AI Confidence: **99.16%**
3800. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaAnnotationCallChecker.kt`** -> AI Confidence: **99.16%**
3801. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaClassOnCompanionChecker.kt`** -> AI Confidence: **99.16%**
3802. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmDefaultChecker.kt`** -> AI Confidence: **99.16%**
3803. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmModuleAccessibilityChecker.kt`** -> AI Confidence: **99.16%**
3804. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/MissingBuiltInDeclarationChecker.kt`** -> AI Confidence: **99.16%**
3805. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SynchronizedAnnotationOnLambdaChecker.kt`** -> AI Confidence: **99.16%**
3806. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/UpperBoundViolatedInTypealiasConstructorChecker.kt`** -> AI Confidence: **99.16%**
3807. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/WarningAwareUpperBoundChecker.kt`** -> AI Confidence: **99.16%**
3808. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/multiplatform/JavaActualAnnotationArgumentExtractor.kt`** -> AI Confidence: **99.16%**
3809. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/ControlFlowInstructionsGenerator.kt`** -> AI Confidence: **99.16%**
3810. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/variable/PseudocodeVariableDataCollector.kt`** -> AI Confidence: **99.16%**
3811. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/CollectionLiteralResolver.kt`** -> AI Confidence: **99.16%**
3812. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/FiniteBoundRestrictionChecker.kt`** -> AI Confidence: **99.16%**
3813. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/LazyTopDownAnalyzer.kt`** -> AI Confidence: **99.16%**
3814. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/OperatorModifierChecker.kt`** -> AI Confidence: **99.16%**
3815. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/VariableTypeAndInitializerResolver.kt`** -> AI Confidence: **99.16%**
3816. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/GenericCandidateResolver.kt`** -> AI Confidence: **99.16%**
3817. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ConstructorHeaderCallChecker.kt`** -> AI Confidence: **99.16%**
3818. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/EnumEntryVsCompanionPriorityCallChecker.kt`** -> AI Confidence: **99.16%**
3819. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/SelfCallInNestedObjectConstructorChecker.kt`** -> AI Confidence: **99.16%**
3820. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/constraintIncorporation.kt`** -> AI Confidence: **99.16%**
3821. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/DataFlowValueFactoryImpl.kt`** -> AI Confidence: **99.16%**
3822. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/IdentifierInfo.kt`** -> AI Confidence: **99.16%**
3823. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewCallArguments.kt`** -> AI Confidence: **99.16%**
3824. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewCallableReferenceResolvedCall.kt`** -> AI Confidence: **99.16%**
3825. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewResolvedCallImpl.kt`** -> AI Confidence: **99.16%**
3826. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/PSICallResolver.kt`** -> AI Confidence: **99.16%**
3827. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/StubTypesBasedInferenceSession.kt`** -> AI Confidence: **99.16%**
3828. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/AnnotationClassTargetAndRetentionChecker.kt`** -> AI Confidence: **99.16%**
3829. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ClassifierUsageChecker.kt`** -> AI Confidence: **99.16%**
3830. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DelegationChecker.kt`** -> AI Confidence: **99.16%**
3831. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/KotlinVersionStringAnnotationValueChecker.kt`** -> AI Confidence: **99.16%**
3832. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/MissingDependencyClassChecker.kt`** -> AI Confidence: **99.16%**
3833. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/MissingDependencySupertypeChecker.kt`** -> AI Confidence: **99.16%**
3834. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/MultiFieldValueClassAnnotationsChecker.kt`** -> AI Confidence: **99.16%**
3835. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ReifiedTypeParameterAnnotationChecker.kt`** -> AI Confidence: **99.16%**
3836. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ReturnValueAnnotationChecker.kt`** -> AI Confidence: **99.16%**
3837. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SuspendLimitationsChecker.kt`** -> AI Confidence: **99.16%**
3838. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/TrailingCommaChecker.kt`** -> AI Confidence: **99.16%**
3839. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/diagnostics/KotlinSuppressCache.kt`** -> AI Confidence: **99.16%**
3840. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/LazyImportScope.kt`** -> AI Confidence: **99.16%**
3841. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/DestructuringDeclarationResolver.kt`** -> AI Confidence: **99.16%**
3842. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/PreliminaryDeclarationVisitor.kt`** -> AI Confidence: **99.16%**
3843. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/SenselessComparisonChecker.kt`** -> AI Confidence: **99.16%**
3844. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/BuildHistoryJvmICRunner.kt`** -> AI Confidence: **99.16%**
3845. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalFirJvmCompilerRunner.kt`** -> AI Confidence: **99.16%**
3846. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalJsCompilerRunner.kt`** -> AI Confidence: **99.16%**
3847. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathChangesComputer.kt`** -> AI Confidence: **99.16%**
3848. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathSnapshotShrinker.kt`** -> AI Confidence: **99.16%**
3849. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/javaInterop/ChangedJavaFilesProcessor.kt`** -> AI Confidence: **99.16%**
3850. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/javaInterop/JavaInteropCoordinator.kt`** -> AI Confidence: **99.16%**
3851. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/parsing/parseFileUtils.kt`** -> AI Confidence: **99.16%**
3852. **`compiler/incremental-compilation-impl/tests/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathSnapshotTestCommon.kt`** -> AI Confidence: **99.16%**
3853. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/TailRecursionCallsCollector.kt`** -> AI Confidence: **99.16%**
3854. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/extensions/IrPluginContextImpl.kt`** -> AI Confidence: **99.16%**
3855. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/IrUtils.kt`** -> AI Confidence: **99.16%**
3856. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AbstractFunctionReferenceLowering.kt`** -> AI Confidence: **99.16%**
3857. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AbstractSuspendFunctionsLowering.kt`** -> AI Confidence: **99.16%**
3858. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AbstractValueUsageTransformer.kt`** -> AI Confidence: **99.16%**
3859. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AnnotationImplementationTransformer.kt`** -> AI Confidence: **99.16%**
3860. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/FinallyBlocksLowering.kt`** -> AI Confidence: **99.16%**
3861. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InitializersLowering.kt`** -> AI Confidence: **99.16%**
3862. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/KlibAssertionLowering.kt`** -> AI Confidence: **99.16%**
3863. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/LocalDeclarationsLowering.kt`** -> AI Confidence: **99.16%**
3864. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/LowerUtils.kt`** -> AI Confidence: **99.16%**
3865. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/PropertiesLowering.kt`** -> AI Confidence: **99.16%**
3866. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/SharedVariablesPrimitiveBoxSpecializationLowering.kt`** -> AI Confidence: **99.16%**
3867. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/SingleAbstractMethodLowering.kt`** -> AI Confidence: **99.16%**
3868. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/StringConcatenationLowering.kt`** -> AI Confidence: **99.16%**
3869. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/TailrecLowering.kt`** -> AI Confidence: **99.16%**
3870. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/coroutines/AddContinuationToFunctionCallsLowering.kt`** -> AI Confidence: **99.16%**
3871. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/coroutines/AddContinuationToFunctionsLowering.kt`** -> AI Confidence: **99.16%**
3872. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/AvoidLocalFOsInInlineFunctionsLowering.kt`** -> AI Confidence: **99.16%**
3873. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/InlineCallCycleCheckerLowering.kt`** -> AI Confidence: **99.16%**
3874. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/LocalClasses.kt`** -> AI Confidence: **99.16%**
3875. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/SyntheticAccessorGenerator.kt`** -> AI Confidence: **99.16%**
3876. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/HeaderInfo.kt`** -> AI Confidence: **99.16%**
3877. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/HeaderProcessor.kt`** -> AI Confidence: **99.16%**
3878. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/ProgressionType.kt`** -> AI Confidence: **99.16%**
3879. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/IndicesHandlers.kt`** -> AI Confidence: **99.16%**
3880. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/WithIndexHandler.kt`** -> AI Confidence: **99.16%**
3881. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/optimizations/LivenessAnalysis.kt`** -> AI Confidence: **99.16%**
3882. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/phaser/PerformByIrFilePhase.kt`** -> AI Confidence: **99.16%**
3883. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/JsCommonBackendContext.kt`** -> AI Confidence: **99.16%**
3884. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/Dce.kt`** -> AI Confidence: **99.16%**
3885. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/UselessDeclarationsRemover.kt`** -> AI Confidence: **99.16%**
3886. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/JsIrLinkerLoader.kt`** -> AI Confidence: **99.16%**
3887. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/CaptureStackTraceInThrowables.kt`** -> AI Confidence: **99.16%**
3888. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ClassReferenceLowering.kt`** -> AI Confidence: **99.16%**
3889. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ConstLowering.kt`** -> AI Confidence: **99.16%**
3890. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/CreateScriptFunctionsPhase.kt`** -> AI Confidence: **99.16%**
3891. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/EnumClassLowering.kt`** -> AI Confidence: **99.16%**
3892. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ExcludeSyntheticDeclarationsFromExportLowering.kt`** -> AI Confidence: **99.16%**
3893. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/InteropCallableReferenceLowering.kt`** -> AI Confidence: **99.16%**
3894. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/InvokeStaticInitializersLowering.kt`** -> AI Confidence: **99.16%**
3895. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsAnnotationImplementationLowering.kt`** -> AI Confidence: **99.16%**
3896. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsBridgesConstruction.kt`** -> AI Confidence: **99.16%**
3897. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsCallableReferenceLowering.kt`** -> AI Confidence: **99.16%**
3898. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsClassUsageInReflectionLowering.kt`** -> AI Confidence: **99.16%**
3899. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsCodeOutliningLowering.kt`** -> AI Confidence: **99.16%**
3900. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsDefaultParameterInjector.kt`** -> AI Confidence: **99.16%**
3901. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsStaticLowering.kt`** -> AI Confidence: **99.16%**
3902. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/MainFunctionCallWrapperLowering.kt`** -> AI Confidence: **99.16%**
3903. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ObjectLowering.kt`** -> AI Confidence: **99.16%**
3904. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrimitiveCompanionLowering.kt`** -> AI Confidence: **99.16%**
3905. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/WebCallableReferenceLowering.kt`** -> AI Confidence: **99.16%**
3906. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/EnumIntrinsicsTransformer.kt`** -> AI Confidence: **99.16%**
3907. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/ReflectionCallsTransformer.kt`** -> AI Confidence: **99.16%**
3908. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/JsSuspendFunctionWithGeneratorsLowering.kt`** -> AI Confidence: **99.16%**
3909. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/JsSuspendFunctionsLowering.kt`** -> AI Confidence: **99.16%**
3910. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsIntrinsicTransformers.kt`** -> AI Confidence: **99.16%**
3911. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/jsCode.kt`** -> AI Confidence: **99.16%**
3912. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrTypeAnnotationCollector.kt`** -> AI Confidence: **99.16%**
3913. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/JvmMethodSignatureClashDetector.kt`** -> AI Confidence: **99.16%**
3914. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/PromisedValue.kt`** -> AI Confidence: **99.16%**
3915. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/CompareTo.kt`** -> AI Confidence: **99.16%**
3916. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IrIntrinsicMethods.kt`** -> AI Confidence: **99.16%**
3917. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/AnonymousObjectSuperConstructorLowering.kt`** -> AI Confidence: **99.16%**
3918. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/AssertionLowering.kt`** -> AI Confidence: **99.16%**
3919. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/EnumClassLowering.kt`** -> AI Confidence: **99.16%**
3920. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ExternalPackageParentPatcherLowering.kt`** -> AI Confidence: **99.16%**
3921. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/GenerateJvmDefaultCompatibilityBridges.kt`** -> AI Confidence: **99.16%**
3922. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/IndyLambdaMetafactoryLowering.kt`** -> AI Confidence: **99.16%**
3923. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InterfaceSuperCallsLowering.kt`** -> AI Confidence: **99.16%**
3924. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmArgumentNullabilityAssertionsLowering.kt`** -> AI Confidence: **99.16%**
3925. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmBuiltInsLowering.kt`** -> AI Confidence: **99.16%**
3926. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmDefaultArgumentStubGenerator.kt`** -> AI Confidence: **99.16%**
3927. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmDefaultConstructorLowering.kt`** -> AI Confidence: **99.16%**
3928. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmLocalDeclarationsLowering.kt`** -> AI Confidence: **99.16%**
3929. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmOverloadsAnnotationLowering.kt`** -> AI Confidence: **99.16%**
3930. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ObjectClassLowering.kt`** -> AI Confidence: **99.16%**
3931. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PropertyReferenceLowering.kt`** -> AI Confidence: **99.16%**
3932. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/RepeatedAnnotationLowering.kt`** -> AI Confidence: **99.16%**
3933. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ReplaceKFunctionInvokeWithFunctionInvoke.kt`** -> AI Confidence: **99.16%**
3934. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ReplaceNumberToCharCallSitesLowering.kt`** -> AI Confidence: **99.16%**
3935. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SpecialAccess.kt`** -> AI Confidence: **99.16%**
3936. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/StaticInitializersLowering.kt`** -> AI Confidence: **99.16%**
3937. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SuspendLambdaLowering.kt`** -> AI Confidence: **99.16%**
3938. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SyntheticAccessorLowering.kt`** -> AI Confidence: **99.16%**
3939. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ToArrayLowering.kt`** -> AI Confidence: **99.16%**
3940. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmSharedVariablesManager.kt`** -> AI Confidence: **99.16%**
3941. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/IrJvmFlexibleType.kt`** -> AI Confidence: **99.16%**
3942. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/metadata/DescriptorMetadataSerializer.kt`** -> AI Confidence: **99.16%**
3943. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/overrides/IrJavaIncompatibilityRulesOverridabilityCondition.kt`** -> AI Confidence: **99.16%**
3944. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/BackendWasmSymbols.kt`** -> AI Confidence: **99.16%**
3945. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/dce/Dce.kt`** -> AI Confidence: **99.16%**
3946. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenContexts/WasmTrackedTypeCodegenContext.kt`** -> AI Confidence: **99.16%**
3947. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/IrFileToWasmIrGenerator.kt`** -> AI Confidence: **99.16%**
3948. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/locationUtils.kt`** -> AI Confidence: **99.16%**
3949. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/AssociatedObjectsLowering.kt`** -> AI Confidence: **99.16%**
3950. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/EraseVirtualDispatchReceiverParametersTypes.kt`** -> AI Confidence: **99.16%**
3951. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/FieldInitializersLowering.kt`** -> AI Confidence: **99.16%**
3952. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/InvokeOnExportedFunctionExitLowering.kt`** -> AI Confidence: **99.16%**
3953. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmStringConcatenationLowering.kt`** -> AI Confidence: **99.16%**
3954. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/generateMainFunctionCalls.kt`** -> AI Confidence: **99.16%**
3955. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/serialization/WasmDeserializer.kt`** -> AI Confidence: **99.16%**
3956. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/DwarfGenerator.kt`** -> AI Confidence: **99.16%**
3957. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/ExpectActualCollector.kt`** -> AI Confidence: **99.16%**
3958. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/ExpectActualLinker.kt`** -> AI Confidence: **99.16%**
3959. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrActualizerUtils.kt`** -> AI Confidence: **99.16%**
3960. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrExpectActualMap.kt`** -> AI Confidence: **99.16%**
3961. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/InlineFunctionBodyPreprocessor.kt`** -> AI Confidence: **99.16%**
3962. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/checkers/IrInlineDeclarationChecker.kt`** -> AI Confidence: **99.16%**
3963. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/IrInterpreterEnvironment.kt`** -> AI Confidence: **99.16%**
3964. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/intrinsics/IntrinsicImplementations.kt`** -> AI Confidence: **99.16%**
3965. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/stack/CallStack.kt`** -> AI Confidence: **99.16%**
3966. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/Complex.kt`** -> AI Confidence: **99.16%**
3967. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/KFunctionState.kt`** -> AI Confidence: **99.16%**
3968. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/KPropertyState.kt`** -> AI Confidence: **99.16%**
3969. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstEvaluationContext.kt`** -> AI Confidence: **99.16%**
3970. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstExpressionTransformer.kt`** -> AI Confidence: **99.16%**
3971. **`compiler/ir/ir.objcinterop/src/org/jetbrains/kotlin/ir/objcinterop/ObjCInterop.kt`** -> AI Confidence: **99.16%**
3972. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/descriptors/IrBuiltInsOverDescriptors.kt`** -> AI Confidence: **99.16%**
3973. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/descriptors/IrDescriptorBasedFunctionFactory.kt`** -> AI Confidence: **99.16%**
3974. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/BodyGenerator.kt`** -> AI Confidence: **99.16%**
3975. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DelegatedPropertyGenerator.kt`** -> AI Confidence: **99.16%**
3976. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/EnumClassMembersGenerator.kt`** -> AI Confidence: **99.16%**
3977. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/Generator.kt`** -> AI Confidence: **99.16%**
3978. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/fragments/FragmentCompilerSymbolTableDecorator.kt`** -> AI Confidence: **99.16%**
3979. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/KtDiagnosticReporterWithImplicitIrBasedContext.kt`** -> AI Confidence: **99.16%**
3980. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/CopyIrTreeWithSymbolsForFakeOverrides.kt`** -> AI Confidence: **99.16%**
3981. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/irTypePredicates.kt`** -> AI Confidence: **99.16%**
3982. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DescriptorSymbolTableExtension.kt`** -> AI Confidence: **99.16%**
3983. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/ElementPrinter.kt`** -> AI Confidence: **99.16%**
3984. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/IrTreeSymbolsVisitorPrinter.kt`** -> AI Confidence: **99.16%**
3985. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/symbol/SymbolRemapperPrinter.kt`** -> AI Confidence: **99.16%**
3986. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/symbol/SymbolVisitorPrinter.kt`** -> AI Confidence: **99.16%**
3987. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/IrValidator.kt`** -> AI Confidence: **99.16%**
3988. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/DumpIrReferenceRenderingAsSignatureStrategy.kt`** -> AI Confidence: **99.16%**
3989. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/ClassifierExplorer.kt`** -> AI Confidence: **99.16%**
3990. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/overrides/FakeOverrides.kt`** -> AI Confidence: **99.16%**
3991. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/DeclarationTable.kt`** -> AI Confidence: **99.16%**
3992. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrBodyDeserializer.kt`** -> AI Confidence: **99.16%**
3993. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrDeclarationDeserializer.kt`** -> AI Confidence: **99.16%**
3994. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/LegacyDescriptorUtils.kt`** -> AI Confidence: **99.16%**
3995. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/mangle/ir/IrExportCheckerVisitor.kt`** -> AI Confidence: **99.16%**
3996. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/mangle/ir/IrMangleComputer.kt`** -> AI Confidence: **99.16%**
3997. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/metadata/KlibMetadataMonolithicSerializer.kt`** -> AI Confidence: **99.16%**
3998. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/metadata/KlibMetadataSerializerExtension.kt`** -> AI Confidence: **99.16%**
3999. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/serializeModuleIntoKlib.kt`** -> AI Confidence: **99.16%**
4000. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/signature/IdSignatureComputers.kt`** -> AI Confidence: **99.16%**
4001. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/ModulesStructure.kt`** -> AI Confidence: **99.16%**
4002. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/checkers/expressions/JsKlibJsCodeCallChecker.kt`** -> AI Confidence: **99.16%**
4003. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/klib.kt`** -> AI Confidence: **99.16%**
4004. **`compiler/ir/serialization.jvm/src/org/jetbrains/kotlin/backend/jvm/serialization/JvmIdSignatureDescriptor.kt`** -> AI Confidence: **99.16%**
4005. **`compiler/ir/serialization.jvm/src/org/jetbrains/kotlin/ir/backend/jvm/serialization/JvmIrLinker.kt`** -> AI Confidence: **99.16%**
4006. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/ObjCFunctionNameMangleComputer.kt`** -> AI Confidence: **99.16%**
4007. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/loadNativeKlibs.kt`** -> AI Confidence: **99.16%**
4008. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/KotlinClassifiersCache.kt`** -> AI Confidence: **99.16%**
4009. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/symbols/SymbolBasedClass.kt`** -> AI Confidence: **99.16%**
4010. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightMethodImpl.kt`** -> AI Confidence: **99.16%**
4011. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtToJvmAnnotationsConverter.kt`** -> AI Confidence: **99.16%**
4012. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinLightParser.kt`** -> AI Confidence: **99.16%**
4013. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtClassOrObject.kt`** -> AI Confidence: **99.16%**
4014. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtCodeFragment.kt`** -> AI Confidence: **99.16%**
4015. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtPsiFactory.kt`** -> AI Confidence: **99.16%**
4016. **`compiler/resolution/src/org/jetbrains/kotlin/contracts/interpretation/ContractInterpretationDispatcher.kt`** -> AI Confidence: **99.16%**
4017. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/ClassicTypeSystemContextForCS.kt`** -> AI Confidence: **99.16%**
4018. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/NewOverloadingConflictResolver.kt`** -> AI Confidence: **99.16%**
4019. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/DescriptorRelatedInferenceUtils.kt`** -> AI Confidence: **99.16%**
4020. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/components/ClassicConstraintSystemUtilContext.kt`** -> AI Confidence: **99.16%**
4021. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/multiplatform/ClassicExpectActualMatchingContext.kt`** -> AI Confidence: **99.16%**
4022. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/scopes/LexicalChainedScope.kt`** -> AI Confidence: **99.16%**
4023. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/checkers/KotlinMultiFileTestWithJava.kt`** -> AI Confidence: **99.16%**
4024. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/fir/FirResolveBench.kt`** -> AI Confidence: **99.16%**
4025. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/TestsJsonMapGenerator.kt`** -> AI Confidence: **99.16%**
4026. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/models/LinkedSpecTest.kt`** -> AI Confidence: **99.16%**
4027. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/parsers/CommonParser.kt`** -> AI Confidence: **99.16%**
4028. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/parsers/Patterns.kt`** -> AI Confidence: **99.16%**
4029. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/parsers/TestCasesParser.kt`** -> AI Confidence: **99.16%**
4030. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/parsers/TestInfoParser.kt`** -> AI Confidence: **99.16%**
4031. **`compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt`** -> AI Confidence: **99.16%**
4032. **`compiler/util-klib-abi/src/org/jetbrains/kotlin/library/abi/parser/KlibParsingCursorExtensions.kt`** -> AI Confidence: **99.16%**
4033. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaAnnotationDescriptor.kt`** -> AI Confidence: **99.16%**
4034. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaClassDescriptor.kt`** -> AI Confidence: **99.16%**
4035. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaPackageScope.kt`** -> AI Confidence: **99.16%**
4036. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaScope.kt`** -> AI Confidence: **99.16%**
4037. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaStaticClassScope.kt`** -> AI Confidence: **99.16%**
4038. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/AbstractBinaryClassAnnotationAndConstantLoader.kt`** -> AI Confidence: **99.16%**
4039. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/BinaryClassAnnotationAndConstantLoaderImpl.kt`** -> AI Confidence: **99.16%**
4040. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/descriptorBasedTypeSignatureMapping.kt`** -> AI Confidence: **99.16%**
4041. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/SubpackagesScope.kt`** -> AI Confidence: **99.16%**
4042. **`core/descriptors/src/org/jetbrains/kotlin/resolve/calls/inference/CapturedTypeConstructor.kt`** -> AI Confidence: **99.16%**
4043. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/SubstitutingScope.kt`** -> AI Confidence: **99.16%**
4044. **`core/descriptors/src/org/jetbrains/kotlin/types/KotlinType.kt`** -> AI Confidence: **99.16%**
4045. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/ClassicTypeSystemContext.kt`** -> AI Confidence: **99.16%**
4046. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/NewCapturedType.kt`** -> AI Confidence: **99.16%**
4047. **`core/descriptors/src/org/jetbrains/kotlin/util/modifierChecks.kt`** -> AI Confidence: **99.16%**
4048. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/TypeDeserializer.kt`** -> AI Confidence: **99.16%**
4049. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedClassDescriptor.kt`** -> AI Confidence: **99.16%**
4050. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedMemberScope.kt`** -> AI Confidence: **99.16%**
4051. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KPackageImpl.kt`** -> AI Confidence: **99.16%**
4052. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KTypeParameterImpl.kt`** -> AI Confidence: **99.16%**
4053. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/RuntimeTypeMapper.kt`** -> AI Confidence: **99.16%**
4054. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/typeOfImpl.kt`** -> AI Confidence: **99.16%**
4055. **`generators/ide-iml-to-gradle-generator/src/org/jetbrains/kotlin/generators/imltogradle/Util.kt`** -> AI Confidence: **99.16%**
4056. **`jps/jps-common/src/org/jetbrains/kotlin/config/KotlinFacetSettings.kt`** -> AI Confidence: **99.16%**
4057. **`jps/jps-plugin/src/org/jetbrains/jps/builders/java/dependencyView/NullabilityAnnotationsTracker.kt`** -> AI Confidence: **99.16%**
4058. **`jps/jps-plugin/src/org/jetbrains/kotlin/compilerRunner/CompilerRunnerUtil.kt`** -> AI Confidence: **99.16%**
4059. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/statistic/JpsStatisticsReportService.kt`** -> AI Confidence: **99.16%**
4060. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/KotlinModuleBuildTarget.kt`** -> AI Confidence: **99.16%**
4061. **`js/js.frontend/src/org/jetbrains/kotlin/js/analyze/TopDownAnalyzerFacadeForJS.kt`** -> AI Confidence: **99.16%**
4062. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsCallChecker.kt`** -> AI Confidence: **99.16%**
4063. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsNativeRttiChecker.kt`** -> AI Confidence: **99.16%**
4064. **`js/js.parser/src/org/jetbrains/kotlin/js/parser/JsParser.kt`** -> AI Confidence: **99.16%**
4065. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/test/utils/JsIrIncrementalDataProvider.kt`** -> AI Confidence: **99.16%**
4066. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/test/utils/RunnerUtils.kt`** -> AI Confidence: **99.16%**
4067. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/defFileDependencies.kt`** -> AI Confidence: **99.16%**
4068. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/common/AbstractValueUsageTransformer.kt`** -> AI Confidence: **99.16%**
4069. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/BuiltInFictitiousFunctionIrClassFactory.kt`** -> AI Confidence: **99.16%**
4070. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CachedLibraries.kt`** -> AI Confidence: **99.16%**
4071. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/KonanDriver.kt`** -> AI Confidence: **99.16%**
4072. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cgen/CBridgeGenUtils.kt`** -> AI Confidence: **99.16%**
4073. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/NativeCompilerDriver.kt`** -> AI Confidence: **99.16%**
4074. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/utilities/LlvmPassesUtilities.kt`** -> AI Confidence: **99.16%**
4075. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/NewIrUtils.kt`** -> AI Confidence: **99.16%**
4076. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/linkKlibs.kt`** -> AI Confidence: **99.16%**
4077. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/BinaryInterface.kt`** -> AI Confidence: **99.16%**
4078. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/AddFunctionSupertypeToSuspendFunctionLowering.kt`** -> AI Confidence: **99.16%**
4079. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/BridgesBuilding.kt`** -> AI Confidence: **99.16%**
4080. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/CacheInfoBuilder.kt`** -> AI Confidence: **99.16%**
4081. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/CoroutinesVarSpillingLowering.kt`** -> AI Confidence: **99.16%**
4082. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/EnumClassLowering.kt`** -> AI Confidence: **99.16%**
4083. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/EnumConstructorsLowering.kt`** -> AI Confidence: **99.16%**
4084. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InitializersLowering.kt`** -> AI Confidence: **99.16%**
4085. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeFunctionReferenceLowering.kt`** -> AI Confidence: **99.16%**
4086. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeInlineFunctionResolver.kt`** -> AI Confidence: **99.16%**
4087. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeReflectionIrBuilder.kt`** -> AI Confidence: **99.16%**
4088. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/PostInlineLowering.kt`** -> AI Confidence: **99.16%**
4089. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/StaticCallableReferenceOptimization.kt`** -> AI Confidence: **99.16%**
4090. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/StringConcatenationTypeNarrowing.kt`** -> AI Confidence: **99.16%**
4091. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/UnboxInlineLowering.kt`** -> AI Confidence: **99.16%**
4092. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/VarargLowering.kt`** -> AI Confidence: **99.16%**
4093. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExport.kt`** -> AI Confidence: **99.16%**
4094. **`kotlin-native/backend.native/tests/samples/objc/src/objcMain/kotlin/Async.kt`** -> AI Confidence: **99.16%**
4095. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/IrSignaturesExtractor.kt`** -> AI Confidence: **99.16%**
4096. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/KlibToolCommands.kt`** -> AI Confidence: **99.16%**
4097. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/KotlinpBasedMetadataDumper.kt`** -> AI Confidence: **99.16%**
4098. **`kotlin-native/performance/buildSrc/src/main/kotlin/RunKotlinNativeTask.kt`** -> AI Confidence: **99.16%**
4099. **`kotlin-native/tools/kdumputil/src/kdump/hprof/converter.kt`** -> AI Confidence: **99.16%**
4100. **`kotlin-native/tools/kdumputil/src/main.kt`** -> AI Confidence: **99.16%**
4101. **`libraries/examples/scripting/jvm-maven-deps/host/src/org/jetbrains/kotlin/script/examples/jvm/resolve/maven/host/host.kt`** -> AI Confidence: **99.16%**
4102. **`libraries/scripting/dependencies-maven/src/kotlin/script/experimental/dependencies/maven/impl/aether.kt`** -> AI Confidence: **99.16%**
4103. **`libraries/stdlib/src/kotlin/uuid/Uuid.kt`** -> AI Confidence: **99.16%**
4104. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/FieldsListChecker.kt`** -> AI Confidence: **99.16%**
4105. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/MethodsListChecker.kt`** -> AI Confidence: **99.16%**
4106. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/tasks/CheckerConfiguration.kt`** -> AI Confidence: **99.16%**
4107. **`libraries/tools/abi-validation/abi-tools/src/main/kotlin/org/jetbrains/kotlin/abi/tools/impl/AbiToolsImpl.kt`** -> AI Confidence: **99.16%**
4108. **`libraries/tools/analysis-api-based-klib-reader/src/org/jetbrains/kotlin/analysis/api/klib/reader/readKlibDeclarationAddresses.kt`** -> AI Confidence: **99.16%**
4109. **`libraries/tools/analysis-api-based-klib-reader/test/org/jetbrains/kotlin/analysis/api/klib/reader/tests/GetSymbolsTest.kt`** -> AI Confidence: **99.16%**
4110. **`libraries/tools/dukat/src/main/kotlin/org/jetbrains/kotlin/tools/dukat/wasm/convertToModel.kt`** -> AI Confidence: **99.16%**
4111. **`libraries/tools/gradle/kotlin-compiler-args-properties/src/common/kotlin/org/jetbrains/kotlin/gradle/arguments/GradleKotlinCompilerArgumentsPlugin.kt`** -> AI Confidence: **99.16%**
4112. **`libraries/tools/ide-plugin-dependencies-validator/src/org/jetbrains/kotlin/ide/plugin/dependencies/validator/ExperimentalAnnotationListChecker.kt`** -> AI Confidence: **99.16%**
4113. **`libraries/tools/kotlin-compose-compiler/src/common/kotlin/org/jetbrains/kotlin/compose/compiler/gradle/internal/ComposeAgpMappingFile.kt`** -> AI Confidence: **99.16%**
4114. **`libraries/tools/kotlin-gradle-plugin-api/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinTarget.kt`** -> AI Confidence: **99.16%**
4115. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BuildReportsIT.kt`** -> AI Confidence: **99.16%**
4116. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/CommonizerIT.kt`** -> AI Confidence: **99.16%**
4117. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ExplicitApiIT.kt`** -> AI Confidence: **99.16%**
4118. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/JvmTargetValidationTest.kt`** -> AI Confidence: **99.16%**
4119. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/PublishingHelpersTest.kt`** -> AI Confidence: **99.16%**
4120. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/ExternalAndroidTargetIT.kt`** -> AI Confidence: **99.16%**
4121. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/SeparateKmpCompilationIT.kt`** -> AI Confidence: **99.16%**
4122. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/publication/MppPublicationCompatibilityIT.kt`** -> AI Confidence: **99.16%**
4123. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/CocoaPodsXcodeIT.kt`** -> AI Confidence: **99.16%**
4124. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/GeneralNativeIT.kt`** -> AI Confidence: **99.16%**
4125. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/argumentProviders.kt`** -> AI Confidence: **99.16%**
4126. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/xcodeTestHelpers.kt`** -> AI Confidence: **99.16%**
4127. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/util/SwiftExportUtils.kt`** -> AI Confidence: **99.16%**
4128. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleKotlinCompilerRunner.kt`** -> AI Confidence: **99.16%**
4129. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/btapi/BuildToolsApiCompilationWork.kt`** -> AI Confidence: **99.16%**
4130. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/KotlinMultiplatformSourceSetCheckers.kt`** -> AI Confidence: **99.16%**
4131. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/KotlinNativeBinaryContainer.kt`** -> AI Confidence: **99.16%**
4132. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/Kapt3KotlinGradleSubplugin.kt`** -> AI Confidence: **99.16%**
4133. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/classloaders/ClassLoadersCache.kt`** -> AI Confidence: **99.16%**
4134. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kotlinDomApiDependencyManagement.kt`** -> AI Confidence: **99.16%**
4135. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kotlinTestDependencyManagement.kt`** -> AI Confidence: **99.16%**
4136. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/testing/TCServiceMessagesClient.kt`** -> AI Confidence: **99.16%**
4137. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/transforms/ClasspathEntrySnapshotTransform.kt`** -> AI Confidence: **99.16%**
4138. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinGradleFinishBuildHandler.kt`** -> AI Confidence: **99.16%**
4139. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/abi/internal/Multiplatform.kt`** -> AI Confidence: **99.16%**
4140. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/abi/internal/Utils.kt`** -> AI Confidence: **99.16%**
4141. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CheckKotlinGradlePluginConfigurationErrors.kt`** -> AI Confidence: **99.16%**
4142. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CompilerDiagnosticsProblemsReporter.kt`** -> AI Confidence: **99.16%**
4143. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/KotlinToolingDiagnostics.kt`** -> AI Confidence: **99.16%**
4144. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/KotlinToolingDiagnosticsCollector.kt`** -> AI Confidence: **99.16%**
4145. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/AndroidPublicationNotConfiguredChecker.kt`** -> AI Confidence: **99.16%**
4146. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/DisabledCinteropCommonizationInHmppProjectChecker.kt`** -> AI Confidence: **99.16%**
4147. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/GradleDeprecatedPropertyChecker.kt`** -> AI Confidence: **99.16%**
4148. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/MissingNativeStdlibChecker.kt`** -> AI Confidence: **99.16%**
4149. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/NativeBinaryConfigurationChecker.kt`** -> AI Confidence: **99.16%**
4150. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/SupportedNativeHostChecker.kt`** -> AI Confidence: **99.16%**
4151. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/hierarchy/RedundantDependsOnEdgesTracker.kt`** -> AI Confidence: **99.16%**
4152. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdePlatformCinteropDependencyResolver.kt`** -> AI Confidence: **99.16%**
4153. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeProjectToProjectCInteropDependencyResolver.kt`** -> AI Confidence: **99.16%**
4154. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeSourcesVariantsResolver.kt`** -> AI Confidence: **99.16%**
4155. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/resolveNativeDistributionDependency.kt`** -> AI Confidence: **99.16%**
4156. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/AbstractKotlinTarget.kt`** -> AI Confidence: **99.16%**
4157. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/GenerateProjectStructureMetadata.kt`** -> AI Confidence: **99.16%**
4158. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinProjectStructureMetadata.kt`** -> AI Confidence: **99.16%**
4159. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinProjectStructureMetadataExtractorFactoryDeprecated.kt`** -> AI Confidence: **99.16%**
4160. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinTargetSoftwareComponentImpl.kt`** -> AI Confidence: **99.16%**
4161. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/MetadataDependencyTransformationTaskInputs.kt`** -> AI Confidence: **99.16%**
4162. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/AppleXcodeTasks.kt`** -> AI Confidence: **99.16%**
4163. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/SwiftImportSetupAction.kt`** -> AI Confidence: **99.16%**
4164. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCreateCompilationArchiveTask.kt`** -> AI Confidence: **99.16%**
4165. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinMetadataCompilationTargetPlatformConfiguration.kt`** -> AI Confidence: **99.16%**
4166. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/external/createExternalKotlinCompilation.kt`** -> AI Confidence: **99.16%**
4167. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/metadataCompileClasspathConfiguration.kt`** -> AI Confidence: **99.16%**
4168. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/ExportTargetPublicationCoordinates.kt`** -> AI Confidence: **99.16%**
4169. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/Publishing.kt`** -> AI Confidence: **99.16%**
4170. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/AssembleHierarchicalResourcesTask.kt`** -> AI Confidence: **99.16%**
4171. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/consumption/UklibConsumptionSetupAction.kt`** -> AI Confidence: **99.16%**
4172. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/serialization/uklibSerialization.kt`** -> AI Confidence: **99.16%**
4173. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/KotlinAndroidSourceSets.kt`** -> AI Confidence: **99.16%**
4174. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/configurator/MultiplatformLayoutV2DependsOnConfigurator.kt`** -> AI Confidence: **99.16%**
4175. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/BuildFinishBuildService.kt`** -> AI Confidence: **99.16%**
4176. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/BuildFusService.kt`** -> AI Confidence: **99.16%**
4177. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/FusMetrics.kt`** -> AI Confidence: **99.16%**
4178. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/BuildMetricsService.kt`** -> AI Confidence: **99.16%**
4179. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/configureReporing.kt`** -> AI Confidence: **99.16%**
4180. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/android/KotlinAndroidTarget.kt`** -> AI Confidence: **99.16%**
4181. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/AbstractSetupTask.kt`** -> AI Confidence: **99.16%**
4182. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/KotlinJsCompilation.kt`** -> AI Confidence: **99.16%**
4183. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/d8/D8EnvSpec.kt`** -> AI Confidence: **99.16%**
4184. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/DefaultIncrementalSyncTask.kt`** -> AI Confidence: **99.16%**
4185. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsBinaryContainer.kt`** -> AI Confidence: **99.16%**
4186. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsIrLink.kt`** -> AI Confidence: **99.16%**
4187. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmDependencyExtension.kt`** -> AI Confidence: **99.16%**
4188. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/resolver/KotlinCompilationNpmResolution.kt`** -> AI Confidence: **99.16%**
4189. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/resolver/KotlinProjectNpmResolver.kt`** -> AI Confidence: **99.16%**
4190. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpackCssRule.kt`** -> AI Confidence: **99.16%**
4191. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnBasics.kt`** -> AI Confidence: **99.16%**
4192. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmCompilation.kt`** -> AI Confidence: **99.16%**
4193. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/metadata/KotlinMetadataTargetConfigurator.kt`** -> AI Confidence: **99.16%**
4194. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/NativeCompilerDownloader.kt`** -> AI Confidence: **99.16%**
4195. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/KotlinCocoapodsPlugin.kt`** -> AI Confidence: **99.16%**
4196. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/AddKotlinPlatformIntegersSupportLibrary.kt`** -> AI Confidence: **99.16%**
4197. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerConfigurations.kt`** -> AI Confidence: **99.16%**
4198. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerDependencies.kt`** -> AI Confidence: **99.16%**
4199. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerTask.kt`** -> AI Confidence: **99.16%**
4200. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropPropagatedDependencies.kt`** -> AI Confidence: **99.16%**
4201. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CommonizerTasks.kt`** -> AI Confidence: **99.16%**
4202. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/PlatformLibrariesGenerator.kt`** -> AI Confidence: **99.16%**
4203. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/SetupKotlinNativePlatformDependenciesAndStdlib.kt`** -> AI Confidence: **99.16%**
4204. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/commonizerTarget.kt`** -> AI Confidence: **99.16%**
4205. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/tasks/FatFrameworkTask.kt`** -> AI Confidence: **99.16%**
4206. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/tasks/KotlinNativeLink.kt`** -> AI Confidence: **99.16%**
4207. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/tasks/KotlinNativeTasks.kt`** -> AI Confidence: **99.16%**
4208. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/toolchain/KotlinNativeProvider.kt`** -> AI Confidence: **99.16%**
4209. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/WasmBinaryPreparationSetupAction.kt`** -> AI Confidence: **99.16%**
4210. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/nodejs/BaseNodeJsRootExtension.kt`** -> AI Confidence: **99.16%**
4211. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/DefaultKotlinJavaToolchain.kt`** -> AI Confidence: **99.16%**
4212. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/Kotlin2JsCompile.kt`** -> AI Confidence: **99.16%**
4213. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/TasksOutputsBackup.kt`** -> AI Confidence: **99.16%**
4214. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/Kotlin2JsCompileConfig.kt`** -> AI Confidence: **99.16%**
4215. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/KotlinCompileConfig.kt`** -> AI Confidence: **99.16%**
4216. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/testing/internal/KotlinTestReport.kt`** -> AI Confidence: **99.16%**
4217. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/testing/internal/KotlinTestsRegistry.kt`** -> AI Confidence: **99.16%**
4218. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tooling/BuildKotlinToolingMetadataTask.kt`** -> AI Confidence: **99.16%**
4219. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/internal/compilerRunner/native/KotlinNativeToolRunner.kt`** -> AI Confidence: **99.16%**
4220. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT37051CInteropArtifactTest.kt`** -> AI Confidence: **99.16%**
4221. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KTIJ25227CompilerArgumentsIdeCompatibilityTest.kt`** -> AI Confidence: **99.16%**
4222. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/DisabledCInteropCommonizationWarningTest.kt`** -> AI Confidence: **99.16%**
4223. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ExternalKotlinTargetApiTests.kt`** -> AI Confidence: **99.16%**
4224. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinAndroidTargetResourcesPublicationTests.kt`** -> AI Confidence: **99.16%**
4225. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinTargetVariantResourcesResolutionTests.kt`** -> AI Confidence: **99.16%**
4226. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/MppPublicationTest.kt`** -> AI Confidence: **99.16%**
4227. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/MultiplatformSecondaryOutgoingVariantsTest.kt`** -> AI Confidence: **99.16%**
4228. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ZipUtilsTest.kt`** -> AI Confidence: **99.16%**
4229. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/diagnosticUtils.kt`** -> AI Confidence: **99.16%**
4230. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/utils/processes/ExecAsyncHandleTest.kt`** -> AI Confidence: **99.16%**
4231. **`libraries/tools/kotlin-gradle-plugin/src/gradle811/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ProblemsReporterG811.kt`** -> AI Confidence: **99.16%**
4232. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/statistics/BuildSessionLoggerTest.kt`** -> AI Confidence: **99.16%**
4233. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/ranges/OtherLowercaseRangesGenerator.kt`** -> AI Confidence: **99.16%**
4234. **`native/base/src/main/kotlin/org/jetbrains/kotlin/backend/konan/InlineClasses.kt`** -> AI Confidence: **99.16%**
4235. **`native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/FirebaseCloudXCTestExecutor.kt`** -> AI Confidence: **99.16%**
4236. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeForwardDeclarationRttiChecker.kt`** -> AI Confidence: **99.16%**
4237. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCComment.kt`** -> AI Confidence: **99.16%**
4238. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportLazy.kt`** -> AI Confidence: **99.16%**
4239. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportTranslator.kt`** -> AI Confidence: **99.16%**
4240. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/NameUtils.kt`** -> AI Confidence: **99.16%**
4241. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/BridgeProvider/TypeBridging.kt`** -> AI Confidence: **99.16%**
4242. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirCustomTypeTranslatorImpl.kt`** -> AI Confidence: **99.16%**
4243. **`native/swift/swift-export-standalone/src/org/jetbrains/kotlin/swiftexport/standalone/translation/ModuleTranslation.kt`** -> AI Confidence: **99.16%**
4244. **`plugins/allopen/allopen.k2/src/org/jetbrains/kotlin/allopen/fir/FirAllOpenStatusTransformer.kt`** -> AI Confidence: **99.16%**
4245. **`plugins/assign-plugin/assign-plugin.k1/src/org/jetbrains/kotlin/assignment/plugin/diagnostics/AssignmentPluginDeclarationChecker.kt`** -> AI Confidence: **99.16%**
4246. **`plugins/assign-plugin/assign-plugin.k2/src/org/jetbrains/kotlin/assignment/plugin/k2/diagnostics/FirAssignmentPluginFunctionCallChecker.kt`** -> AI Confidence: **99.16%**
4247. **`plugins/assign-plugin/assign-plugin.k2/src/org/jetbrains/kotlin/assignment/plugin/k2/diagnostics/FirAssignmentPluginFunctionChecker.kt`** -> AI Confidence: **99.16%**
4248. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/js/AtomicfuJsIrTransformer.kt`** -> AI Confidence: **99.16%**
4249. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/jvm/JvmAtomicSymbols.kt`** -> AI Confidence: **99.16%**
4250. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/diagnostic/AtomicfuPropertyChecker.kt`** -> AI Confidence: **99.16%**
4251. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractMultiPlatformIntegrationTest.kt`** -> AI Confidence: **99.16%**
4252. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ControlFlowTransformTests.kt`** -> AI Confidence: **99.16%**
4253. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/GroupAnalysisCompilerTest.kt`** -> AI Confidence: **99.16%**
4254. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposableAnnotationChecker.kt`** -> AI Confidence: **99.16%**
4255. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposableAnnotationChecker.kt`** -> AI Confidence: **99.16%**
4256. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposableTargetChecker.kt`** -> AI Confidence: **99.16%**
4257. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunInterfaceLowering.kt`** -> AI Confidence: **99.16%**
4258. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/DurableKeyTransformer.kt`** -> AI Confidence: **99.16%**
4259. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/LiveLiteralTransformer.kt`** -> AI Confidence: **99.16%**
4260. **`plugins/compose/compiler-hosted/src/test/kotlin/androidx/compose/compiler/plugins/kotlin/services/ComposeTestUtils.kt`** -> AI Confidence: **99.16%**
4261. **`plugins/compose/group-mapping/src/main/kotlin/androidx/compose/compiler/mapping/ClassInfo.kt`** -> AI Confidence: **99.16%**
4262. **`plugins/js-plain-objects/compiler-plugin/js-plain-objects.backend/src/org/jetbrains/kotlinx/jso/compiler/backend/JsObjectLoweringExtension.kt`** -> AI Confidence: **99.16%**
4263. **`plugins/js-plain-objects/compiler-plugin/js-plain-objects.k2/src/org/jetbrains/kotlinx/jso/compiler/fir/JsPlainObjectsFunctionsGenerator.kt`** -> AI Confidence: **99.16%**
4264. **`plugins/js-plain-objects/compiler-plugin/js-plain-objects.k2/src/org/jetbrains/kotlinx/jso/compiler/fir/checkers/FirJsPlainObjectsPluginClassChecker.kt`** -> AI Confidence: **99.16%**
4265. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/javac/KaptJavaLog.kt`** -> AI Confidence: **99.16%**
4266. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/KaptPlugin.kt`** -> AI Confidence: **99.16%**
4267. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptDocCommentKeeper.kt`** -> AI Confidence: **99.16%**
4268. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptLineMappingCollector.kt`** -> AI Confidence: **99.16%**
4269. **`plugins/kotlin-dataframe/kotlin-dataframe.backend/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/IrImportedSchemaGenerator.kt`** -> AI Confidence: **99.16%**
4270. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ExpressionAnalysisAdditionalChecker.kt`** -> AI Confidence: **99.16%**
4271. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/FunctionCallTransformer.kt`** -> AI Confidence: **99.16%**
4272. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ImportedSchemasCompanionGenerator.kt`** -> AI Confidence: **99.16%**
4273. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ImportedSchemasGenerator.kt`** -> AI Confidence: **99.16%**
4274. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/TopLevelExtensionsGenerator.kt`** -> AI Confidence: **99.16%**
4275. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/DataFrameAdapter.kt`** -> AI Confidence: **99.16%**
4276. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/SimpleCol.kt`** -> AI Confidence: **99.16%**
4277. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/convert.kt`** -> AI Confidence: **99.16%**
4278. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/gather.kt`** -> AI Confidence: **99.16%**
4279. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/groupBy.kt`** -> AI Confidence: **99.16%**
4280. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrBuilderWithPluginContext.kt`** -> AI Confidence: **99.16%**
4281. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/SerializationContextInFile.kt`** -> AI Confidence: **99.16%**
4282. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/FirSerializableProperty.kt`** -> AI Confidence: **99.16%**
4283. **`plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/services/FirSerializablePropertiesProvider.kt`** -> AI Confidence: **99.16%**
4284. **`plugins/kotlinx-serialization/testData/boxIr/intrinsicsStarProjections.kt`** -> AI Confidence: **99.16%**
4285. **`plugins/kotlinx-serialization/testFixtures/org/jetbrains/kotlinx/serialization/serializationConfiguration.kt`** -> AI Confidence: **99.16%**
4286. **`plugins/lombok/lombok.k1/src/org/jetbrains/kotlin/lombok/processor/AllArgsConstructorProcessor.kt`** -> AI Confidence: **99.16%**
4287. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/DeclarationWithValueAnnStatusTransformer.kt`** -> AI Confidence: **99.16%**
4288. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/LombokConstructorsGenerator.kt`** -> AI Confidence: **99.16%**
4289. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/RequiredArgsConstructorGeneratorPart.kt`** -> AI Confidence: **99.16%**
4290. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/SuperBuilderGenerator.kt`** -> AI Confidence: **99.16%**
4291. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/generators/WithGenerator.kt`** -> AI Confidence: **99.16%**
4292. **`plugins/lombok/testFixtures/org/jetbrains/kotlin/lombok/LombokTestServices.kt`** -> AI Confidence: **99.16%**
4293. **`plugins/noarg/noarg.k2/src/org/jetbrains/kotlin/noarg/fir/FirNoArgConstructorGenerator.kt`** -> AI Confidence: **99.16%**
4294. **`plugins/parcelize/parcelize-compiler/parcelize.backend/src/org/jetbrains/kotlin/parcelize/IrParcelSerializers.kt`** -> AI Confidence: **99.16%**
4295. **`plugins/parcelize/parcelize-compiler/parcelize.backend/src/org/jetbrains/kotlin/parcelize/ParcelizeFirIrTransformer.kt`** -> AI Confidence: **99.16%**
4296. **`plugins/parcelize/parcelize-compiler/parcelize.backend/src/org/jetbrains/kotlin/parcelize/ParcelizeIrTransformer.kt`** -> AI Confidence: **99.16%**
4297. **`plugins/parcelize/parcelize-compiler/parcelize.backend/src/org/jetbrains/kotlin/parcelize/irUtils.kt`** -> AI Confidence: **99.16%**
4298. **`plugins/parcelize/parcelize-compiler/parcelize.k2/src/org/jetbrains/kotlin/parcelize/fir/FirParcelizeDeclarationGenerator.kt`** -> AI Confidence: **99.16%**
4299. **`plugins/parcelize/parcelize-compiler/parcelize.k2/src/org/jetbrains/kotlin/parcelize/fir/diagnostics/FirParcelizeFunctionChecker.kt`** -> AI Confidence: **99.16%**
4300. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/AllOpenMatcherBasedStatusTransformer.kt`** -> AI Confidence: **99.16%**
4301. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/AllPublicVisibilityTransformer.kt`** -> AI Confidence: **99.16%**
4302. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/checkers/SignedNumberCallChecker.kt`** -> AI Confidence: **99.16%**
4303. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/AdditionalMembersGenerator.kt`** -> AI Confidence: **99.16%**
4304. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/generators/NestedClassGeneratorWithSupertypesDependantOnAnnotationArgument.kt`** -> AI Confidence: **99.16%**
4305. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/fir/types/FirNumberSignAttributeExtension.kt`** -> AI Confidence: **99.16%**
4306. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/ir/AllPropertiesConstructorIrGenerator.kt`** -> AI Confidence: **99.16%**
4307. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/ir/PluginFunctionKindsTransformer.kt`** -> AI Confidence: **99.16%**
4308. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/ir/SourceElementChecker.kt`** -> AI Confidence: **99.16%**
4309. **`plugins/plugin-sandbox/src/org/jetbrains/kotlin/plugin/sandbox/ir/TransformerForAddingAnnotations.kt`** -> AI Confidence: **99.16%**
4310. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/IrUtils.kt`** -> AI Confidence: **99.16%**
4311. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/PowerAssertBuiltIns.kt`** -> AI Confidence: **99.16%**
4312. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/builder/parameter/DefaultMessageParameterBuilder.kt`** -> AI Confidence: **99.16%**
4313. **`plugins/power-assert/power-assert-compiler/power-assert.frontend/src/org/jetbrains/kotlin/powerassert/checkers/PowerAssertAnnotationChecker.kt`** -> AI Confidence: **99.16%**
4314. **`plugins/power-assert/power-assert-compiler/power-assert.frontend/src/org/jetbrains/kotlin/powerassert/checkers/utils.kt`** -> AI Confidence: **99.16%**
4315. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/resolve/scriptAnnotationsPreprocessing.kt`** -> AI Confidence: **99.16%**
4316. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/ScriptingCompilerConfigurationExtension.kt`** -> AI Confidence: **99.16%**
4317. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/extensions/ScriptingProcessSourcesBeforeCompilingExtension.kt`** -> AI Confidence: **99.16%**
4318. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/K2ReplCompiler.kt`** -> AI Confidence: **99.16%**
4319. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/KJvmReplCompilerBase.kt`** -> AI Confidence: **99.16%**
4320. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/jvmCompilationUtil.kt`** -> AI Confidence: **99.16%**
4321. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/irLowerings/ReplSnippetLowering.kt`** -> AI Confidence: **99.16%**
4322. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/GenericReplCompiler.kt`** -> AI Confidence: **99.16%**
4323. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/ReplImplicitsExtensionsResolutionFilter.kt`** -> AI Confidence: **99.16%**
4324. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/ReplInterpreter.kt`** -> AI Confidence: **99.16%**
4325. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/reader/ConsoleReplCommandReader.kt`** -> AI Confidence: **99.16%**
4326. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/services/Fir2IrScriptConfiguratorExtensionImpl.kt`** -> AI Confidence: **99.16%**
4327. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/services/FirReplSnippetConfiguratorExtensionImpl.kt`** -> AI Confidence: **99.16%**
4328. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/services/FirScriptResolutionConfigurationExtensionImpl.kt`** -> AI Confidence: **99.16%**
4329. **`repo/artifacts-tests/src/test/kotlin/org/jetbrains/kotlin/code/GradleMetadataTest.kt`** -> AI Confidence: **99.16%**
4330. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/resolve-dependencies.gradle.kts`** -> AI Confidence: **99.16%**
4331. **`repo/gradle-build-conventions/generators/src/main/kotlin/generatorTasks.kt`** -> AI Confidence: **99.16%**
4332. **`repo/gradle-build-conventions/gradle-plugins-documentation/src/main/kotlin/helpers.kt`** -> AI Confidence: **99.16%**
4333. **`repo/gradle-build-conventions/project-tests-convention/src/main/kotlin/nativeTest.kt`** -> AI Confidence: **99.16%**
4334. **`repo/gradle-build-conventions/project-tests-convention/src/main/kotlin/objcExportHeaderGeneratorTest.kt`** -> AI Confidence: **99.16%**
4335. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/WasmExternalDeclarationChecker.kt`** -> AI Confidence: **99.16%**
4336. **`wasm/wasm.tests/testFixtures/org/jetbrains/kotlin/wasm/test/utils/DirectiveTestUtils.kt`** -> AI Confidence: **99.16%**
4337. **`compiler/backend.common.jvm/src/org/jetbrains/kotlin/codegen/AsmUtil.java`** -> AI Confidence: **99.16%**
4338. **`compiler/backend/src/org/jetbrains/kotlin/codegen/GeneratedClassLoader.java`** -> AI Confidence: **99.16%**
4339. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/modules/ModuleXmlParser.java`** -> AI Confidence: **99.16%**
4340. **`compiler/cli/src/com/intellij/openapi/progress/impl/CoreProgressManager.java`** -> AI Confidence: **99.16%**
4341. **`compiler/cli/src/org/jetbrains/kotlin/cli/jvm/compiler/CompileEnvironmentUtil.java`** -> AI Confidence: **99.16%**
4342. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/FileBasedKotlinClass.java`** -> AI Confidence: **99.16%**
4343. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/util/ConstUtils.java`** -> AI Confidence: **99.16%**
4344. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/sam/JavaSingleAbstractMethodUtils.java`** -> AI Confidence: **99.16%**
4345. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/DiagnosticUtils.java`** -> AI Confidence: **99.16%**
4346. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/TabledDescriptorRenderer.java`** -> AI Confidence: **99.16%**
4347. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnalyzerExtensions.java`** -> AI Confidence: **99.16%**
4348. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/BindingContextUtils.java`** -> AI Confidence: **99.16%**
4349. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/CompileTimeConstantUtils.java`** -> AI Confidence: **99.16%**
4350. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/PlatformClassesMappedToKotlinChecker.java`** -> AI Confidence: **99.16%**
4351. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/CallResolver.java`** -> AI Confidence: **99.16%**
4352. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/context/ResolutionContext.java`** -> AI Confidence: **99.16%**
4353. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/model/ResolvedCallImpl.java`** -> AI Confidence: **99.16%**
4354. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/inline/InlineUtil.java`** -> AI Confidence: **99.16%**
4355. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyClassDescriptor.java`** -> AI Confidence: **99.16%**
4356. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyTypeParameterDescriptor.java`** -> AI Confidence: **99.16%**
4357. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/ExpressionTypingVisitorForStatements.java`** -> AI Confidence: **99.16%**
4358. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/TypeReconstructionUtil.java`** -> AI Confidence: **99.16%**
4359. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/diagnostics/PsiDiagnosticUtils.java`** -> AI Confidence: **99.16%**
4360. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtElementImplStub.java`** -> AI Confidence: **99.16%**
4361. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtNamedDeclarationStub.java`** -> AI Confidence: **99.16%**
4362. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtPackageDirective.java`** -> AI Confidence: **99.16%**
4363. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtProperty.java`** -> AI Confidence: **99.16%**
4364. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtValueArgument.java`** -> AI Confidence: **99.16%**
4365. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/LambdaExpressionElementType.java`** -> AI Confidence: **99.16%**
4366. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtPropertyElementType.java`** -> AI Confidence: **99.16%**
4367. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinPlaceHolderStubImpl.java`** -> AI Confidence: **99.16%**
4368. **`compiler/tests-common/testFixtures/com/intellij/execution/configurations/PathEnvironmentVariableUtil.java`** -> AI Confidence: **99.16%**
4369. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/cfg/CFGraphToDotFilePrinter.java`** -> AI Confidence: **99.16%**
4370. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/jvm/compiler/ExpectedLoadErrorsUtil.java`** -> AI Confidence: **99.16%**
4371. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/descriptors/JavaClassConstructorDescriptor.java`** -> AI Confidence: **99.16%**
4372. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/DescriptorVisibilities.java`** -> AI Confidence: **99.16%**
4373. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/PropertyDescriptorImpl.java`** -> AI Confidence: **99.16%**
4374. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/SimpleFunctionDescriptorImpl.java`** -> AI Confidence: **99.16%**
4375. **`core/descriptors/src/org/jetbrains/kotlin/types/DescriptorSubstitutor.java`** -> AI Confidence: **99.16%**
4376. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeSubstitutor.java`** -> AI Confidence: **99.16%**
4377. **`core/deserialization.common.jvm/src/org/jetbrains/kotlin/load/kotlin/header/ReadKotlinClassHeaderAnnotationVisitor.java`** -> AI Confidence: **99.16%**
4378. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectionFactoryImpl.java`** -> AI Confidence: **99.16%**
4379. **`core/util.runtime/src/org/jetbrains/kotlin/storage/LockBasedStorageManager.java`** -> AI Confidence: **99.16%**
4380. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/testOld/utils/DirectiveTestUtils.java`** -> AI Confidence: **99.16%**
4381. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/java/org/jetbrains/kotlin/gradle/incapt/IncrementalAggregatingProcessor.java`** -> AI Confidence: **99.16%**
4382. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/java/org/jetbrains/kotlin/gradle/incapt/IncrementalAggregatingReferencingClasspathProcessor.java`** -> AI Confidence: **99.16%**
4383. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/java/org/jetbrains/kotlin/gradle/incapt/IncrementalBinaryIsolatingProcessor.java`** -> AI Confidence: **99.16%**
4384. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/ExecuteKotlinScriptMojo.java`** -> AI Confidence: **99.16%**
4385. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/K2JVMCompileMojo.java`** -> AI Confidence: **99.16%**
4386. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/KotlinLifecycleParticipant.java`** -> AI Confidence: **99.16%**
4387. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/kapt/AnnotationProcessingManager.java`** -> AI Confidence: **99.16%**
4388. **`libraries/tools/kotlin-maven-plugin/src/main/java/org/jetbrains/kotlin/maven/kapt/KaptJVMCompilerMojo.java`** -> AI Confidence: **99.16%**
4389. **`wasm/wasm.debug.browsers/src/formatters/index.mjs`** -> AI Confidence: **99.16%**
4390. **`kotlin-native/runtime/src/alloc/custom/cpp/CustomAllocator.cpp`** -> AI Confidence: **99.16%**
4391. **`kotlin-native/runtime/src/alloc/custom/cpp/Heap.cpp`** -> AI Confidence: **99.16%**
4392. **`kotlin-native/runtime/src/gc/common/cpp/GCStatistics.cpp`** -> AI Confidence: **99.16%**
4393. **`kotlin-native/runtime/src/main/cpp/Exceptions.cpp`** -> AI Confidence: **99.16%**
4394. **`kotlin-native/runtime/src/main/cpp/Runtime.cpp`** -> AI Confidence: **99.16%**
4395. **`kotlin-native/runtime/src/main/cpp/concurrent/MutexTest.cpp`** -> AI Confidence: **99.16%**
4396. **`kotlin-native/runtime/src/mm/cpp/ExternalRCRef.cpp`** -> AI Confidence: **99.16%**
4397. **`kotlin-native/runtime/src/mm/cpp/MemoryDump.cpp`** -> AI Confidence: **99.16%**
4398. **`kotlin-native/runtime/src/source_info/core_symbolication/cpp/SourceInfo.cpp`** -> AI Confidence: **99.16%**
4399. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/InlineDelegatedPropertyAccessorsAnalyzer.kt`** -> AI Confidence: **99.15%**
4400. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirTypeInformationProvider.kt`** -> AI Confidence: **99.15%**
4401. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirDefaultAnnotationArgumentReference.kt`** -> AI Confidence: **99.15%**
4402. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/ReadWriteAccessCheckerFirImpl.kt`** -> AI Confidence: **99.15%**
4403. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirArrayOfSymbolProvider.kt`** -> AI Confidence: **99.15%**
4404. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirClassLikeSymbolPointer.kt`** -> AI Confidence: **99.15%**
4405. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirMemberFunctionSymbolPointer.kt`** -> AI Confidence: **99.15%**
4406. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirMemberPropertySymbolPointer.kt`** -> AI Confidence: **99.15%**
4407. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirSecondaryConstructorSymbolPointer.kt`** -> AI Confidence: **99.15%**
4408. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/pointerUtils.kt`** -> AI Confidence: **99.15%**
4409. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/annotations/KaBaseNamedAnnotationValue.kt`** -> AI Confidence: **99.15%**
4410. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseDataFlowProvider.kt`** -> AI Confidence: **99.15%**
4411. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseTypeProvider.kt`** -> AI Confidence: **99.15%**
4412. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/contracts/description/KaBaseEffects.kt`** -> AI Confidence: **99.15%**
4413. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/contracts/description/booleans/KaBaseLogicalCombinators.kt`** -> AI Confidence: **99.15%**
4414. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/contracts/description/booleans/KaBasePredicates.kt`** -> AI Confidence: **99.15%**
4415. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/projectStructure/KaBaseResolutionScope.kt`** -> AI Confidence: **99.15%**
4416. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/signatures/KaBaseVariableSignature.kt`** -> AI Confidence: **99.15%**
4417. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/symbols/pointers/KaBaseCachedSymbolPointer.kt`** -> AI Confidence: **99.15%**
4418. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/symbols/pointers/KaBaseContextParameterSymbolPointer.kt`** -> AI Confidence: **99.15%**
4419. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/rendererUtils.kt`** -> AI Confidence: **99.15%**
4420. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/superTypes/KaSuperTypesFilter.kt`** -> AI Confidence: **99.15%**
4421. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaSymbol.kt`** -> AI Confidence: **99.15%**
4422. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/DirectoryBasedClassFinder.kt`** -> AI Confidence: **99.15%**
4423. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/DirectoryBasedDataFinder.kt`** -> AI Confidence: **99.15%**
4424. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KDocReference.kt`** -> AI Confidence: **99.15%**
4425. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtInvokeFunctionReference.kt`** -> AI Confidence: **99.15%**
4426. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtSimpleNameReference.kt`** -> AI Confidence: **99.15%**
4427. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/elements/KtLightElementBase.kt`** -> AI Confidence: **99.15%**
4428. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/LLFirLazyDeclarationResolver.kt`** -> AI Confidence: **99.15%**
4429. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/LLResolutionFacadeService.kt`** -> AI Confidence: **99.15%**
4430. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/FileElementFactory.kt`** -> AI Confidence: **99.15%**
4431. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/statistics/LLStatisticsService.kt`** -> AI Confidence: **99.15%**
4432. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinSymbolNamesProvider.kt`** -> AI Confidence: **99.15%**
4433. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/combined/LLSelectingCombinedSymbolProvider.kt`** -> AI Confidence: **99.15%**
4434. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirExpectActualMatcherLazyResolver.kt`** -> AI Confidence: **99.15%**
4435. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirLazyResolver.kt`** -> AI Confidence: **99.15%**
4436. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/stateKeeperUtils.kt`** -> AI Confidence: **99.15%**
4437. **`build-common/src/org/jetbrains/kotlin/incremental/AbstractIncrementalCache.kt`** -> AI Confidence: **99.15%**
4438. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/JsCompilerArguments.kt`** -> AI Confidence: **99.15%**
4439. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/MetadataCompilerArguments.kt`** -> AI Confidence: **99.15%**
4440. **`compiler/backend/src/org/jetbrains/kotlin/codegen/JvmBackendClassResolver.kt`** -> AI Confidence: **99.15%**
4441. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/BasicTypeInterpreter.kt`** -> AI Confidence: **99.15%**
4442. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/assertions/filesAssertions.kt`** -> AI Confidence: **99.15%**
4443. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testKotlinLogger/kotlin/KotlinLoggerSeverityWerrorTest.kt`** -> AI Confidence: **99.15%**
4444. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/internal/wrappers/KotlinWrapperPre2_3_20.kt`** -> AI Confidence: **99.15%**
4445. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/KotlinToolchainsImpl.kt`** -> AI Confidence: **99.15%**
4446. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/modules/CoreJrtFileSystem.kt`** -> AI Confidence: **99.15%**
4447. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmCliPipeline.kt`** -> AI Confidence: **99.15%**
4448. **`compiler/cli/cli-runner/src/org/jetbrains/kotlin/runner/runners.kt`** -> AI Confidence: **99.15%**
4449. **`compiler/config/configuration-keys-generator/src/org/jetbrains/kotlin/config/keys/generator/CommonConfigurationKeysContainer.kt`** -> AI Confidence: **99.15%**
4450. **`compiler/config/configuration-keys-generator/src/org/jetbrains/kotlin/config/keys/generator/model/KeysContainerGenerator.kt`** -> AI Confidence: **99.15%**
4451. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/RemoteLookupTrackerClient.kt`** -> AI Confidence: **99.15%**
4452. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsSymbolChecker.kt`** -> AI Confidence: **99.15%**
4453. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/FirJvmNamesChecker.kt`** -> AI Confidence: **99.15%**
4454. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/FirJvmAnnotationsPlatformSpecificSupportComponent.kt`** -> AI Confidence: **99.15%**
4455. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeIdentifierChecker.kt`** -> AI Confidence: **99.15%**
4456. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCNameCallableChecker.kt`** -> AI Confidence: **99.15%**
4457. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/FirWasmJsExportHelpers.kt`** -> AI Confidence: **99.15%**
4458. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirWebReflectionAPICallChecker.kt`** -> AI Confidence: **99.15%**
4459. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirMissingDependencySupertypeUtils.kt`** -> AI Confidence: **99.15%**
4460. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirSinceKotlinHelpers.kt`** -> AI Confidence: **99.15%**
4461. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/config/FirSuppressedDiagnosticsCheckers.kt`** -> AI Confidence: **99.15%**
4462. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDataClassPrimaryConstructorChecker.kt`** -> AI Confidence: **99.15%**
4463. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFunctionNameChecker.kt`** -> AI Confidence: **99.15%**
4464. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlinePropertyChecker.kt`** -> AI Confidence: **99.15%**
4465. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/PlatformClassMappedToKotlinImportsChecker.kt`** -> AI Confidence: **99.15%**
4466. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirGenericQualifierOnConstructorCallChecker.kt`** -> AI Confidence: **99.15%**
4467. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineBodyResolvedQualifierChecker.kt`** -> AI Confidence: **99.15%**
4468. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineBodyVariableAssignmentChecker.kt`** -> AI Confidence: **99.15%**
4469. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineExposedLessVisibleThisReceiverChecker.kt`** -> AI Confidence: **99.15%**
4470. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirPackageOnLhsQualifierChecker.kt`** -> AI Confidence: **99.15%**
4471. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUnderscoreChecker.kt`** -> AI Confidence: **99.15%**
4472. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirWhenReturnTypeChecker.kt`** -> AI Confidence: **99.15%**
4473. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantSetterParameterTypeChecker.kt`** -> AI Confidence: **99.15%**
4474. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaClassMembersEnhancementScope.kt`** -> AI Confidence: **99.15%**
4475. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/types/jvm/FirJavaTypeRef.kt`** -> AI Confidence: **99.15%**
4476. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirProvidedDeclarationsForMetadataService.kt`** -> AI Confidence: **99.15%**
4477. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrSymbolsMappingForLazyClasses.kt`** -> AI Confidence: **99.15%**
4478. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/FirRetentionAnnotationHelpers.kt`** -> AI Confidence: **99.15%**
4479. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/expressions/FirInlineConstTrackerComponent.kt`** -> AI Confidence: **99.15%**
4480. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/ExplicitFieldsUtils.kt`** -> AI Confidence: **99.15%**
4481. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/Scopes.kt`** -> AI Confidence: **99.15%**
4482. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/AbstractFirOverrideScope.kt`** -> AI Confidence: **99.15%**
4483. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirOuterClassManager.kt`** -> AI Confidence: **99.15%**
4484. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirProviderImpl.kt`** -> AI Confidence: **99.15%**
4485. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/LocalVariableScopeStorage.kt`** -> AI Confidence: **99.15%**
4486. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/contracts/description/ConeContractRenderer.kt`** -> AI Confidence: **99.15%**
4487. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/references/FirReferenceUtils.kt`** -> AI Confidence: **99.15%**
4488. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirCallableSignatureRenderer.kt`** -> AI Confidence: **99.15%**
4489. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirResolvedNamedReferenceRenderer.kt`** -> AI Confidence: **99.15%**
4490. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/scopes/FirCompositeScope.kt`** -> AI Confidence: **99.15%**
4491. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/scopes/FirTypeScope.kt`** -> AI Confidence: **99.15%**
4492. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/printer/utils.kt`** -> AI Confidence: **99.15%**
4493. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaPackageImpl.kt`** -> AI Confidence: **99.15%**
4494. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/annotationArgumentsImpl.kt`** -> AI Confidence: **99.15%**
4495. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/KotlinBinaryClassCache.kt`** -> AI Confidence: **99.15%**
4496. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/VirtualFileFinder.kt`** -> AI Confidence: **99.15%**
4497. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmDelegationFilter.kt`** -> AI Confidence: **99.15%**
4498. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/StrictfpApplicabilityChecker.kt`** -> AI Confidence: **99.15%**
4499. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/UnsupportedSyntheticCallableReferenceChecker.kt`** -> AI Confidence: **99.15%**
4500. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/instructions/eval/accessInstructions.kt`** -> AI Confidence: **99.15%**
4501. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/PsiConstantParser.kt`** -> AI Confidence: **99.15%**
4502. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/PlatformIncompatibilityDiagnosticRenderer.kt`** -> AI Confidence: **99.15%**
4503. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ContextReceiversUtil.kt`** -> AI Confidence: **99.15%**
4504. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/FunctionsFromAny.kt`** -> AI Confidence: **99.15%**
4505. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ApiVersionCallChecker.kt`** -> AI Confidence: **99.15%**
4506. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/InfixCallChecker.kt`** -> AI Confidence: **99.15%**
4507. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/NamedFunAsExpressionChecker.kt`** -> AI Confidence: **99.15%**
4508. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/UnderscoreUsageChecker.kt`** -> AI Confidence: **99.15%**
4509. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/UnsupportedUntilRangeDeclarationChecker.kt`** -> AI Confidence: **99.15%**
4510. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/constraintSystemUtils.kt`** -> AI Confidence: **99.15%**
4511. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DeprecatedClassifierUsageChecker.kt`** -> AI Confidence: **99.15%**
4512. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DynamicReceiverChecker.kt`** -> AI Confidence: **99.15%**
4513. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/InfixModifierChecker.kt`** -> AI Confidence: **99.15%**
4514. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/OptionalExpectationUsageChecker.kt`** -> AI Confidence: **99.15%**
4515. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/StubForBuilderInferenceParameterTypeChecker.kt`** -> AI Confidence: **99.15%**
4516. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/TailrecFunctionChecker.kt`** -> AI Confidence: **99.15%**
4517. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ValueParameterUsageInDefaultArgumentChecker.kt`** -> AI Confidence: **99.15%**
4518. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/diagnostics/MutableDiagnosticsWithSuppression.kt`** -> AI Confidence: **99.15%**
4519. **`compiler/frontend/src/org/jetbrains/kotlin/types/RangeUtil.kt`** -> AI Confidence: **99.15%**
4520. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/PreliminaryLoopVisitor.kt`** -> AI Confidence: **99.15%**
4521. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/definitelyNotNullDeprecation.kt`** -> AI Confidence: **99.15%**
4522. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/BuildDiffsStorage.kt`** -> AI Confidence: **99.15%**
4523. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathEntrySnapshotter.kt`** -> AI Confidence: **99.15%**
4524. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/InMemoryCacheWithEviction.kt`** -> AI Confidence: **99.15%**
4525. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/snapshots/LazyClasspathSnapshot.kt`** -> AI Confidence: **99.15%**
4526. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ErrorReportingContext.kt`** -> AI Confidence: **99.15%**
4527. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/utils.kt`** -> AI Confidence: **99.15%**
4528. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/ICUtils.kt`** -> AI Confidence: **99.15%**
4529. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/AnnotationConstructorLowering.kt`** -> AI Confidence: **99.15%**
4530. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/NativeGetterSetterTransformer.kt`** -> AI Confidence: **99.15%**
4531. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/inline/RemoveInlineDeclarationsWithReifiedTypeParametersLowering.kt`** -> AI Confidence: **99.15%**
4532. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/CompilationOutputs.kt`** -> AI Confidence: **99.15%**
4533. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/IrFunctionToJsTransformer.kt`** -> AI Confidence: **99.15%**
4534. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/AnnotationUtils.kt`** -> AI Confidence: **99.15%**
4535. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/BinaryOp.kt`** -> AI Confidence: **99.15%**
4536. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/Clone.kt`** -> AI Confidence: **99.15%**
4537. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/EnumIntrinsics.kt`** -> AI Confidence: **99.15%**
4538. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/UndiscoveredExpectUtils.kt`** -> AI Confidence: **99.15%**
4539. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/mapping/GenericSignatureMapper.kt`** -> AI Confidence: **99.15%**
4540. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/dwarf/LineProgram.kt`** -> AI Confidence: **99.15%**
4541. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/DefinedDeclarationsResolver.kt`** -> AI Confidence: **99.15%**
4542. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/markAdditionalExportedDeclarations.kt`** -> AI Confidence: **99.15%**
4543. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/serialization/WasmSerializer.kt`** -> AI Confidence: **99.15%**
4544. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/WasmInlineClassesUtils.kt`** -> AI Confidence: **99.15%**
4545. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/reflection/KClassProxy.kt`** -> AI Confidence: **99.15%**
4546. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/Common.kt`** -> AI Confidence: **99.15%**
4547. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ErrorExpressionGenerator.kt`** -> AI Confidence: **99.15%**
4548. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/LocalFunctionGenerator.kt`** -> AI Confidence: **99.15%**
4549. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/samConversions.kt`** -> AI Confidence: **99.15%**
4550. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/CallBuilder.kt`** -> AI Confidence: **99.15%**
4551. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/SafeCallReceiver.kt`** -> AI Confidence: **99.15%**
4552. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/builders/Scope.kt`** -> AI Confidence: **99.15%**
4553. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DescriptorToIrUtil.kt`** -> AI Confidence: **99.15%**
4554. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/SymbolTableExtension.kt`** -> AI Confidence: **99.15%**
4555. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/TypeRemapper.kt`** -> AI Confidence: **99.15%**
4556. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TypeVisitorVoidPrinter.kt`** -> AI Confidence: **99.15%**
4557. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/issues/KotlinIrLinkerIssues.kt`** -> AI Confidence: **99.15%**
4558. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/issues/SignatureClashDetector.kt`** -> AI Confidence: **99.15%**
4559. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IdSignatureSerializer.kt`** -> AI Confidence: **99.15%**
4560. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrModuleDeserializer.kt`** -> AI Confidence: **99.15%**
4561. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/metadata/DynamicTypeDeserializer.kt`** -> AI Confidence: **99.15%**
4562. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/signature/IdSignatureDescriptor.kt`** -> AI Confidence: **99.15%**
4563. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/checkers/declarations/JsKlibPossibleFileClashWarning.kt`** -> AI Confidence: **99.15%**
4564. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanIrFileSerializer.kt`** -> AI Confidence: **99.15%**
4565. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanLibrarySpecialCompatibilityChecker.kt`** -> AI Confidence: **99.15%**
4566. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/symbols/utils.kt`** -> AI Confidence: **99.15%**
4567. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedMethod.kt`** -> AI Confidence: **99.15%**
4568. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightParameterList.kt`** -> AI Confidence: **99.15%**
4569. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/KotlinParser.kt`** -> AI Confidence: **99.15%**
4570. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/kdoc/psi/impl/KDocName.kt`** -> AI Confidence: **99.15%**
4571. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtObjectDeclaration.kt`** -> AI Confidence: **99.15%**
4572. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtPrimaryConstructor.kt`** -> AI Confidence: **99.15%**
4573. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtPropertyAccessor.kt`** -> AI Confidence: **99.15%**
4574. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/psiUtil/KtStringTemplateExpressionManipulator.kt`** -> AI Confidence: **99.15%**
4575. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtFileStubBuilder.kt`** -> AI Confidence: **99.15%**
4576. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/model/ConstraintStorage.kt`** -> AI Confidence: **99.15%**
4577. **`compiler/resolution/src/org/jetbrains/kotlin/contracts/interpretation/EffectsInterpreters.kt`** -> AI Confidence: **99.15%**
4578. **`compiler/resolution/src/org/jetbrains/kotlin/contracts/model/structure/Values.kt`** -> AI Confidence: **99.15%**
4579. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/scopes/LexicalScopeStorage.kt`** -> AI Confidence: **99.15%**
4580. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/fir/FirAnalyzerFacade.kt`** -> AI Confidence: **99.15%**
4581. **`compiler/tests-mutes/mutes-junit4/src/org/jetbrains/kotlin/test/MuteWithDatabaseWatcher.kt`** -> AI Confidence: **99.15%**
4582. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/SectionsJsonMapGenerator.kt`** -> AI Confidence: **99.15%**
4583. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/models/AbstractSpecTest.kt`** -> AI Confidence: **99.15%**
4584. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/validators/DiagnosticTestTypeValidator.kt`** -> AI Confidence: **99.15%**
4585. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/KlibMetadataClassDataFinder.kt`** -> AI Confidence: **99.15%**
4586. **`compiler/util-klib/src/org/jetbrains/kotlin/library/impl/lowLevelWriters.kt`** -> AI Confidence: **99.15%**
4587. **`compiler/util-klib/src/org/jetbrains/kotlin/library/loader/KlibLoaderResult.kt`** -> AI Confidence: **99.15%**
4588. **`core/compiler.common/src/org/jetbrains/kotlin/builtins/StandardNames.kt`** -> AI Confidence: **99.15%**
4589. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/types/RawType.kt`** -> AI Confidence: **99.15%**
4590. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/components/ReflectJavaClassFinder.kt`** -> AI Confidence: **99.15%**
4591. **`core/descriptors/src/org/jetbrains/kotlin/builtins/functions/BuiltInFictitiousFunctionClassFactory.kt`** -> AI Confidence: **99.15%**
4592. **`core/descriptors/src/org/jetbrains/kotlin/builtins/functions/FunctionInvokeDescriptor.kt`** -> AI Confidence: **99.15%**
4593. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/LazyPackageViewDescriptorImpl.kt`** -> AI Confidence: **99.15%**
4594. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/ModuleDescriptorImpl.kt`** -> AI Confidence: **99.15%**
4595. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/TypeAliasConstructorDescriptor.kt`** -> AI Confidence: **99.15%**
4596. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/IntegerLiteralTypeConstructor.kt`** -> AI Confidence: **99.15%**
4597. **`core/descriptors/src/org/jetbrains/kotlin/resolve/sam/samConstructorUtils.kt`** -> AI Confidence: **99.15%**
4598. **`core/descriptors/src/org/jetbrains/kotlin/types/IntersectionTypeConstructor.kt`** -> AI Confidence: **99.15%**
4599. **`core/descriptors/src/org/jetbrains/kotlin/types/SpecialTypes.kt`** -> AI Confidence: **99.15%**
4600. **`core/descriptors/src/org/jetbrains/kotlin/types/StubTypes.kt`** -> AI Confidence: **99.15%**
4601. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/utils.kt`** -> AI Confidence: **99.15%**
4602. **`core/reflection.jvm/src/kotlin/reflect/full/K1Implementation.kt`** -> AI Confidence: **99.15%**
4603. **`core/reflection.jvm/src/kotlin/reflect/full/KClassifiers.kt`** -> AI Confidence: **99.15%**
4604. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectKFunction.kt`** -> AI Confidence: **99.15%**
4605. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectKParameter.kt`** -> AI Confidence: **99.15%**
4606. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/calls/CallerImpl.kt`** -> AI Confidence: **99.15%**
4607. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/MutableCollectionKClass.kt`** -> AI Confidence: **99.15%**
4608. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/ReflectTypeSystemContext.kt`** -> AI Confidence: **99.15%**
4609. **`generators/ide-iml-to-gradle-generator/src/org/jetbrains/kotlin/generators/imltogradle/flattenExportedTransitiveDependencies.kt`** -> AI Confidence: **99.15%**
4610. **`generators/tests/org/jetbrains/kotlin/generators/mockJDK/filterMockJdk.kt`** -> AI Confidence: **99.15%**
4611. **`jps/jps-common/src/org/jetbrains/kotlin/config/moduleSourceRootPropertiesSerializers.kt`** -> AI Confidence: **99.15%**
4612. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/KotlinTargetsIndex.kt`** -> AI Confidence: **99.15%**
4613. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/impl/LookupUsageRegistrar.kt`** -> AI Confidence: **99.15%**
4614. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExportAnnotationChecker.kt`** -> AI Confidence: **99.15%**
4615. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsMultipleInheritanceChecker.kt`** -> AI Confidence: **99.15%**
4616. **`js/js.serializer/src/org/jetbrains/kotlin/serialization/js/DynamicTypeDeserializer.kt`** -> AI Confidence: **99.15%**
4617. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/testOld/JsTestChecker.kt`** -> AI Confidence: **99.15%**
4618. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cexport/CAdapterTypeTranslator.kt`** -> AI Confidence: **99.15%**
4619. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/VariableManager.kt`** -> AI Confidence: **99.15%**
4620. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeInventNamesForLocalClasses.kt`** -> AI Confidence: **99.15%**
4621. **`kotlin-native/backend.native/tests/samples/tensorflow/src/tensorflowMain/kotlin/HelloTensorflow.kt`** -> AI Confidence: **99.15%**
4622. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/Utils.kt`** -> AI Confidence: **99.15%**
4623. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/nativeDistribution/LLVMDistributionSource.kt`** -> AI Confidence: **99.15%**
4624. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/DescriptorSignaturesRenderer.kt`** -> AI Confidence: **99.15%**
4625. **`kotlin-native/performance/objcinterop/src/nativeMain/kotlin/org/jetbrains/objCinteropBenchmarks/complexNumbers.kt`** -> AI Confidence: **99.15%**
4626. **`kotlin-native/tools/compiler-cache-invalidator/src/org/jetbrains/kotlin/nativecacheinvalidator/NativeCacheInvalidator.kt`** -> AI Confidence: **99.15%**
4627. **`libraries/scripting/common/src/kotlin/script/experimental/api/scriptCompilation.kt`** -> AI Confidence: **99.15%**
4628. **`libraries/stdlib/jvm/src/kotlin/collections/MapsJVM.kt`** -> AI Confidence: **99.15%**
4629. **`libraries/stdlib/jvm/src/kotlin/io/FileReadWrite.kt`** -> AI Confidence: **99.15%**
4630. **`libraries/stdlib/jvm/src/kotlin/io/ReadWrite.kt`** -> AI Confidence: **99.15%**
4631. **`libraries/stdlib/native-wasm/src/kotlin/text/regex/AbstractCharClass.kt`** -> AI Confidence: **99.15%**
4632. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/InnerClassesListChecker.kt`** -> AI Confidence: **99.15%**
4633. **`libraries/tools/binary-compatibility-validator/src/test/kotlin/org.jetbrains.kotlin.tools.tests/KlibPublicAPITest.kt`** -> AI Confidence: **99.15%**
4634. **`libraries/tools/kotlin-gradle-plugin-dsl-codegen/src/main/kotlin/org/jetbrains/kotlin/generators/gradle/dsl/mppNativeBinaryDSLCodegen.kt`** -> AI Confidence: **99.15%**
4635. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinResolvedBinaryDependency.kt`** -> AI Confidence: **99.15%**
4636. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinUnresolvedBinaryDependency.kt`** -> AI Confidence: **99.15%**
4637. **`libraries/tools/kotlin-gradle-plugin-idea/src/testFixtures/kotlin/org/jetbrains/kotlin/gradle/idea/testFixtures/tcs/ideaDependencyMatcherBuilders.kt`** -> AI Confidence: **99.15%**
4638. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BrokenMacosTestInterceptor.kt`** -> AI Confidence: **99.15%**
4639. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/KmpIncrementalCompilationMiscIT.kt`** -> AI Confidence: **99.15%**
4640. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/FatFrameworkIT.kt`** -> AI Confidence: **99.15%**
4641. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/outputAssertions.kt`** -> AI Confidence: **99.15%**
4642. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/localAnnotationProcessor/annotation-processor/src/main/java/TestAnnotationProcessor.kt`** -> AI Confidence: **99.15%**
4643. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/incremental/ClasspathAnalyzer.kt`** -> AI Confidence: **99.15%**
4644. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/AndroidPluginWithoutAndroidTargetChecker.kt`** -> AI Confidence: **99.15%**
4645. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/CinteropCrossCompilationChecker.kt`** -> AI Confidence: **99.15%**
4646. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/ConfigurationOnDemandSupportChecker.kt`** -> AI Confidence: **99.15%**
4647. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/DeprecatedNativeHostChecker.kt`** -> AI Confidence: **99.15%**
4648. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/hierarchy/KotlinHierarchyBuilderImpl.kt`** -> AI Confidence: **99.15%**
4649. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/CheckSandboxAndWriteProtectionTask.kt`** -> AI Confidence: **99.15%**
4650. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/SerializationTools.kt`** -> AI Confidence: **99.15%**
4651. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/internal/SwiftExportedModule.kt`** -> AI Confidence: **99.15%**
4652. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationAssociator.kt`** -> AI Confidence: **99.15%**
4653. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationFriendPathsResolver.kt`** -> AI Confidence: **99.15%**
4654. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/resolve/KotlinTargetResourcesResolution.kt`** -> AI Confidence: **99.15%**
4655. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/KotlinAndroidSourceSetInfo.kt`** -> AI Confidence: **99.15%**
4656. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/MetricsWriter.kt`** -> AI Confidence: **99.15%**
4657. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/LockCopyTask.kt`** -> AI Confidence: **99.15%**
4658. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmTargetTestFixturesSideEffect.kt`** -> AI Confidence: **99.15%**
4659. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerGroup.kt`** -> AI Confidence: **99.15%**
4660. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/NativeDistributionCommonizerLock.kt`** -> AI Confidence: **99.15%**
4661. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/yarn/BaseYarnRootEnvSpec.kt`** -> AI Confidence: **99.15%**
4662. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/gradleConfigurationUtils.kt`** -> AI Confidence: **99.15%**
4663. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/reportUtils.kt`** -> AI Confidence: **99.15%**
4664. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/resourceUtils.kt`** -> AI Confidence: **99.15%**
4665. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/AssembleHierarchicalResourcesTaskSourceSetWalkTests.kt`** -> AI Confidence: **99.15%**
4666. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ConfigurationOnDemandSupportValidationTest.kt`** -> AI Confidence: **99.15%**
4667. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/TestApiDependenciesCheckerTest.kt`** -> AI Confidence: **99.15%**
4668. **`libraries/tools/kotlin-gradle-plugin/src/gradle88/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ProblemsReporterG88.kt`** -> AI Confidence: **99.15%**
4669. **`libraries/tools/kotlin-gradle-plugin/src/testFixtures/kotlin/org/jetbrains/kotlin/gradle/testing/ResolutionTesting.kt`** -> AI Confidence: **99.15%**
4670. **`libraries/tools/kotlin-gradle-statistics/src/main/kotlin/org/jetbrains/kotlin/statistics/BuildSessionLogger.kt`** -> AI Confidence: **99.15%**
4671. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/MavenVerifierExtensions.kt`** -> AI Confidence: **99.15%**
4672. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/ranges/OtherUppercaseRangesGenerator.kt`** -> AI Confidence: **99.15%**
4673. **`libraries/tools/kotlinp/jvm/src/org/jetbrains/kotlin/kotlinp/jvm/utils.kt`** -> AI Confidence: **99.15%**
4674. **`native/analysis-api-based-test-utils/src/org/jetbrains/kotlin/export/test/AnalysisApiAssertions.kt`** -> AI Confidence: **99.15%**
4675. **`native/base/src/main/kotlin/org/jetbrains/kotlin/backend/konan/descriptors/LegacyDescriptorUtils.kt`** -> AI Confidence: **99.15%**
4676. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/cli/nativeTasks.kt`** -> AI Confidence: **99.15%**
4677. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/konan/LibraryCommonizer.kt`** -> AI Confidence: **99.15%**
4678. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/metadata/flags.kt`** -> AI Confidence: **99.15%**
4679. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCOverrideApplicabilityChecker.kt`** -> AI Confidence: **99.15%**
4680. **`native/kotlin-test-native-xctest/src/nativeMain/kotlin/NativeTestRunner.kt`** -> AI Confidence: **99.15%**
4681. **`native/kotlin-test-native-xctest/src/nativeMain/kotlin/configuration.kt`** -> AI Confidence: **99.15%**
4682. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/KtObjCExportModuleNaming.kt`** -> AI Confidence: **99.15%**
4683. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/definedThrows.kt`** -> AI Confidence: **99.15%**
4684. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/getObjCDocumentedAnnotations.kt`** -> AI Confidence: **99.15%**
4685. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/buildCompanionProperty.kt`** -> AI Confidence: **99.15%**
4686. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/resolveObjCNameAnnotation.kt`** -> AI Confidence: **99.15%**
4687. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToMappedObjCType.kt`** -> AI Confidence: **99.15%**
4688. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCObject.kt`** -> AI Confidence: **99.15%**
4689. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/CustomTypeMapper.kt`** -> AI Confidence: **99.15%**
4690. **`native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutinesWithPackageFlattening/golden_result/main/main.kt`** -> AI Confidence: **99.15%**
4691. **`native/swift/swift-export-standalone-integration-tests/src/org/jetbrains/kotlin/swiftexport/standalone/test/SwiftExportValidator.kt`** -> AI Confidence: **99.15%**
4692. **`native/utils/src/org/jetbrains/kotlin/konan/util/DefFile.kt`** -> AI Confidence: **99.15%**
4693. **`plugins/allopen/allopen.k1/src/org/jetbrains/kotlin/allopen/AllOpenDeclarationAttributeAltererExtension.kt`** -> AI Confidence: **99.15%**
4694. **`plugins/compose/compiler-hosted/runtime-tests/src/commonTest/kotlin/androidx/compose/compiler/test/CompositionTests.kt`** -> AI Confidence: **99.15%**
4695. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposablePropertyChecker.kt`** -> AI Confidence: **99.15%**
4696. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/javac/KaptJavaFileManager.kt`** -> AI Confidence: **99.15%**
4697. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/analyzeRefinedCallShape.kt`** -> AI Confidence: **99.15%**
4698. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/Interpreter.kt`** -> AI Confidence: **99.15%**
4699. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/cumSum.kt`** -> AI Confidence: **99.15%**
4700. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/dataFrameOf.kt`** -> AI Confidence: **99.15%**
4701. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/rename.kt`** -> AI Confidence: **99.15%**
4702. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/xs.kt`** -> AI Confidence: **99.15%**
4703. **`plugins/kotlinx-serialization/kotlinx-serialization.common/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/RuntimeVersions.kt`** -> AI Confidence: **99.15%**
4704. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/SerializationPluginErrorsRendering.kt`** -> AI Confidence: **99.15%**
4705. **`plugins/lombok/lombok.k1/src/org/jetbrains/kotlin/lombok/LombokSyntheticJavaPartsProvider.kt`** -> AI Confidence: **99.15%**
4706. **`plugins/lombok/lombok.k1/src/org/jetbrains/kotlin/lombok/processor/RequiredArgsConstructorProcessor.kt`** -> AI Confidence: **99.15%**
4707. **`plugins/lombok/lombok.k1/src/org/jetbrains/kotlin/lombok/processor/WithProcessor.kt`** -> AI Confidence: **99.15%**
4708. **`plugins/lombok/lombok.k2/src/org/jetbrains/kotlin/lombok/k2/config/annotationUtils.kt`** -> AI Confidence: **99.15%**
4709. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/diagram/SourceFile.kt`** -> AI Confidence: **99.15%**
4710. **`plugins/power-assert/power-assert-compiler/power-assert.backend/src/org/jetbrains/kotlin/powerassert/function/PowerAssertGetExplanationTransformer.kt`** -> AI Confidence: **99.15%**
4711. **`plugins/power-assert/power-assert-compiler/testFixtures/org/jetbrains/kotlin/powerassert/JunitTestServices.kt`** -> AI Confidence: **99.15%**
4712. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/definitions/LazyScriptDefinitionFromDiscoveredClass.kt`** -> AI Confidence: **99.15%**
4713. **`plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/definitions/ScriptDefinition.kt`** -> AI Confidence: **99.15%**
4714. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/K2ReplEvaluator.kt`** -> AI Confidence: **99.15%**
4715. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/impl/loadCompilerPlugins.kt`** -> AI Confidence: **99.15%**
4716. **`plugins/scripting/scripting-compiler/src/org/jetbrains/kotlin/scripting/compiler/plugin/repl/jvmReplCompilation.kt`** -> AI Confidence: **99.15%**
4717. **`repo/artifacts-tests/src/test/kotlin/org/jetbrains/kotlin/code/MavenMetadataTest.kt`** -> AI Confidence: **99.15%**
4718. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/UnzipWasmEdge.kt`** -> AI Confidence: **99.15%**
4719. **`repo/gradle-settings-conventions/internal-gradle-setup/src/test/kotlin/SyntheticPropertiesGeneratorTest.kt`** -> AI Confidence: **99.15%**
4720. **`wasm/wasm.frontend/src/org/jetbrains/kotlin/wasm/resolve/diagnostics/WasmJsFunAnnotationChecker.kt`** -> AI Confidence: **99.15%**
4721. **`compiler/backend.common.jvm/src/org/jetbrains/kotlin/resolve/jvm/AsmTypes.java`** -> AI Confidence: **99.15%**
4722. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/messages/GroupingMessageCollector.java`** -> AI Confidence: **99.15%**
4723. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/DiagnosticFactoryToRendererMap.java`** -> AI Confidence: **99.15%**
4724. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/model/DataFlowInfoForArgumentsImpl.java`** -> AI Confidence: **99.15%**
4725. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/DeclarationScopeProviderImpl.java`** -> AI Confidence: **99.15%**
4726. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/KtNodeType.java`** -> AI Confidence: **99.15%**
4727. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtFunctionType.java`** -> AI Confidence: **99.15%**
4728. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtNamedDeclarationNotStubbed.java`** -> AI Confidence: **99.15%**
4729. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtStringTemplateEntry.java`** -> AI Confidence: **99.15%**
4730. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtTypeProjection.java`** -> AI Confidence: **99.15%**
4731. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/types/expressions/OperatorConventions.java`** -> AI Confidence: **99.15%**
4732. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/testOld/utils/AstSearchUtil.java`** -> AI Confidence: **99.15%**
4733. **`libraries/kotlinx-metadata/jvm/src/kotlin/metadata/jvm/KotlinClassHeader.java`** -> AI Confidence: **99.15%**
4734. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/java/org/jetbrains/kotlin/gradle/incapt/IncrementalIsolatingProcessor.java`** -> AI Confidence: **99.15%**
4735. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/java/org/jetbrains/kotlin/gradle/incapt/IncrementalProcessor.java`** -> AI Confidence: **99.15%**
4736. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/java/org/jetbrains/kotlin/gradle/incapt/IncrementalProcessorReferencingClasspath.java`** -> AI Confidence: **99.15%**
4737. **`kotlin-native/runtime/src/libbacktrace/c/posix.c`** -> AI Confidence: **99.15%**
4738. **`native/objcexport-header-generator/testData/dependencies/arrayList/!arrayList.h`** -> AI Confidence: **99.15%**
4739. **`native/objcexport-header-generator/testData/dependencies/propertyAnnotation/!propertyAnnotation.h`** -> AI Confidence: **99.15%**
4740. **`native/objcexport-header-generator/testData/headers/anonymousFunctions/!anonymousFunctions.h`** -> AI Confidence: **99.15%**
4741. **`native/objcexport-header-generator/testData/headers/cProperties/!cProperties.h`** -> AI Confidence: **99.15%**
4742. **`native/objcexport-header-generator/testData/headers/classWithHidesFromObjCAnnotation/!classWithHidesFromObjCAnnotation.h`** -> AI Confidence: **99.15%**
4743. **`native/objcexport-header-generator/testData/headers/classWithKDoc/!classWithKDoc.h`** -> AI Confidence: **99.15%**
4744. **`native/objcexport-header-generator/testData/headers/classWithManyMembers/!classWithManyMembers.h`** -> AI Confidence: **99.15%**
4745. **`native/objcexport-header-generator/testData/headers/classWithMustBeDocumentedAnnotation/!classWithMustBeDocumentedAnnotation.h`** -> AI Confidence: **99.15%**
4746. **`native/objcexport-header-generator/testData/headers/classWithObjCNameAnnotation/!classWithObjCNameAnnotation.h`** -> AI Confidence: **99.15%**
4747. **`native/objcexport-header-generator/testData/headers/classWithUnresolvedSuperType/!classWithUnresolvedSuperType.h`** -> AI Confidence: **99.15%**
4748. **`native/objcexport-header-generator/testData/headers/dispatchAndExtensionReceiverWithMustBeDocumentedAnnotation/!dispatchAndExtensionReceiverWithMustBeDocumentedAnnotation.h`** -> AI Confidence: **99.15%**
4749. **`native/objcexport-header-generator/testData/headers/emptyTopLevelFacades/!emptyTopLevelFacades.h`** -> AI Confidence: **99.15%**
4750. **`native/objcexport-header-generator/testData/headers/extensionOfPrimitiveType/!extensionOfPrimitiveType.h`** -> AI Confidence: **99.15%**
4751. **`native/objcexport-header-generator/testData/headers/extensionWithPrimitiveParameter/!extensionWithPrimitiveParameter.h`** -> AI Confidence: **99.15%**
4752. **`native/objcexport-header-generator/testData/headers/functionParametersAnnotatedWithObjCName/!functionParametersAnnotatedWithObjCName.h`** -> AI Confidence: **99.15%**
4753. **`native/objcexport-header-generator/testData/headers/functionWithMustBeDocumentedAnnotation/!functionWithMustBeDocumentedAnnotation.h`** -> AI Confidence: **99.15%**
4754. **`native/objcexport-header-generator/testData/headers/functionWithReservedMethodName/!functionWithReservedMethodName.h`** -> AI Confidence: **99.15%**
4755. **`native/objcexport-header-generator/testData/headers/functionsAnnotatedWithObjCName/!functionsAnnotatedWithObjCName.h`** -> AI Confidence: **99.15%**
4756. **`native/objcexport-header-generator/testData/headers/genericExtension/!genericExtension.h`** -> AI Confidence: **99.15%**
4757. **`native/objcexport-header-generator/testData/headers/interfaceWithMustBeDocumentedAnnotation/!interfaceWithMustBeDocumentedAnnotation.h`** -> AI Confidence: **99.15%**
4758. **`native/objcexport-header-generator/testData/headers/internalPublicApi/!internalPublicApi.h`** -> AI Confidence: **99.15%**
4759. **`native/objcexport-header-generator/testData/headers/mangleInitConstructors/!mangleInitConstructors.h`** -> AI Confidence: **99.15%**
4760. **`native/objcexport-header-generator/testData/headers/mangleProperty/!mangleProperty.h`** -> AI Confidence: **99.15%**
4761. **`native/objcexport-header-generator/testData/headers/memberFunctionSignatureOrder/!memberFunctionSignatureOrder.h`** -> AI Confidence: **99.15%**
4762. **`native/objcexport-header-generator/testData/headers/methodsMangling/!methodsMangling.h`** -> AI Confidence: **99.15%**
4763. **`native/objcexport-header-generator/testData/headers/objCMappedMixedTypesExtension/!objCMappedMixedTypesExtension.h`** -> AI Confidence: **99.15%**
4764. **`native/objcexport-header-generator/testData/headers/objCMappedPropertyExtension/!objCMappedPropertyExtension.h`** -> AI Confidence: **99.15%**
4765. **`native/objcexport-header-generator/testData/headers/objCNameWithReceiver/!objCNameWithReceiver.h`** -> AI Confidence: **99.15%**
4766. **`native/objcexport-header-generator/testData/headers/parameterWithMustBeDocumentedAnnotation/!parameterWithMustBeDocumentedAnnotation.h`** -> AI Confidence: **99.15%**
4767. **`native/objcexport-header-generator/testData/headers/privateCompanion/!privateCompanion.h`** -> AI Confidence: **99.15%**
4768. **`native/objcexport-header-generator/testData/headers/privateGenericSuperInterface/!privateGenericSuperInterface.h`** -> AI Confidence: **99.15%**
4769. **`native/objcexport-header-generator/testData/headers/privateSuperInterface/!privateSuperInterface.h`** -> AI Confidence: **99.15%**
4770. **`native/objcexport-header-generator/testData/headers/privateSuperInterfaceWithCovariantOverride/!privateSuperInterfaceWithCovariantOverride.h`** -> AI Confidence: **99.15%**
4771. **`native/objcexport-header-generator/testData/headers/privateTopLevelClassProperty/!privateTopLevelClassProperty.h`** -> AI Confidence: **99.15%**
4772. **`native/objcexport-header-generator/testData/headers/propertyWithObjCNameAnnotation/!propertyWithObjCNameAnnotation.h`** -> AI Confidence: **99.15%**
4773. **`native/objcexport-header-generator/testData/headers/receiverWithMustBeDocumentedAnnotation/!receiverWithMustBeDocumentedAnnotation.h`** -> AI Confidence: **99.15%**
4774. **`native/objcexport-header-generator/testData/headers/releaseKeywordAsMethodName/!releaseKeywordAsMethodName.h`** -> AI Confidence: **99.15%**
4775. **`native/objcexport-header-generator/testData/headers/samInterface/!samInterface.h`** -> AI Confidence: **99.15%**
4776. **`native/objcexport-header-generator/testData/headers/samePropertyAndFunctionName/!samePropertyAndFunctionName.h`** -> AI Confidence: **99.15%**
4777. **`native/objcexport-header-generator/testData/headers/simpleClass/!simpleClass.h`** -> AI Confidence: **99.15%**
4778. **`native/objcexport-header-generator/testData/headers/simpleInterface/!simpleInterface.h`** -> AI Confidence: **99.15%**
4779. **`native/objcexport-header-generator/testData/headers/sinceVersionAnnotation/!sinceVersionAnnotation.h`** -> AI Confidence: **99.15%**
4780. **`native/objcexport-header-generator/testData/headers/sourceFileWithDotInName/!sourceFileWithDotInName.h`** -> AI Confidence: **99.15%**
4781. **`native/objcexport-header-generator/testData/headers/topLevelFunction/!topLevelFunction.h`** -> AI Confidence: **99.15%**
4782. **`native/objcexport-header-generator/testData/headers/topLevelFunctionWithNumberReturn/!topLevelFunctionWithNumberReturn.h`** -> AI Confidence: **99.15%**
4783. **`native/objcexport-header-generator/testData/headers/topLevelProperty/!topLevelProperty.h`** -> AI Confidence: **99.15%**
4784. **`native/objcexport-header-generator/testData/headers/varWithPrivateSetterTranslatedAsImmutableProperty/!varWithPrivateSetterTranslatedAsImmutableProperty.h`** -> AI Confidence: **99.15%**
4785. **`kotlin-native/runtime/src/alloc/common/cpp/RunLoopFinalizerProcessor.hpp`** -> AI Confidence: **99.15%**
4786. **`kotlin-native/runtime/src/alloc/custom/cpp/FixedBlockPage.cpp`** -> AI Confidence: **99.15%**
4787. **`kotlin-native/runtime/src/gc/cms/cpp/Barriers.hpp`** -> AI Confidence: **99.15%**
4788. **`kotlin-native/runtime/src/gc/pmcs/cpp/Barriers.cpp`** -> AI Confidence: **99.15%**
4789. **`kotlin-native/runtime/src/mm/cpp/SafePoint.cpp`** -> AI Confidence: **99.15%**
4790. **`kotlin-native/runtime/src/mm/cpp/ThreadStateTest.cpp`** -> AI Confidence: **99.15%**
4791. **`kotlin-native/runtime/src/mm/cpp/ThreadSuspension.cpp`** -> AI Confidence: **99.15%**
4792. **`native/native.tests/testData/CExport/InterfaceV1/concurrentTerminate/main.cpp`** -> AI Confidence: **99.15%**
4793. **`kotlin-native/llvmDebugInfoC/src/scripts/konan_lldb.py`** -> AI Confidence: **99.15%**
4794. **`kotlin-native/runtime/src/gcScheduler/aggressive/cpp/SafePointTrackerTest.cpp`** -> AI Confidence: **99.14%**
4795. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/permissions/KaBaseAnalysisPermissionChecker.kt`** -> AI Confidence: **99.13%**
4796. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/declarations/KotlinFileBasedDeclarationProvider.kt`** -> AI Confidence: **99.13%**
4797. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/modifiers/renderers/KaRendererModalityModifierProvider.kt`** -> AI Confidence: **99.13%**
4798. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/modifiers/renderers/KaRendererVisibilityModifierProvider.kt`** -> AI Confidence: **99.13%**
4799. **`analysis/analysis-internal-utils/src/org/jetbrains/kotlin/analysis/utils/psiUtils.kt`** -> AI Confidence: **99.13%**
4800. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/NonLocalDeclarationUtils.kt`** -> AI Confidence: **99.13%**
4801. **`build-common/src/org/jetbrains/kotlin/modules/KotlinModuleXmlBuilder.kt`** -> AI Confidence: **99.13%**
4802. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/CommonJsAndWasmArguments.kt`** -> AI Confidence: **99.13%**
4803. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/InlineScopesGenerator.kt`** -> AI Confidence: **99.13%**
4804. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/InplaceArgumentsMethodTransformer.kt`** -> AI Confidence: **99.13%**
4805. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MaxStackFrameSizeAndLocalsCalculator.kt`** -> AI Confidence: **99.13%**
4806. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/inlineArgumentsInPlace.kt`** -> AI Confidence: **99.13%**
4807. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/NegatedJumpsMethodTransformer.kt`** -> AI Confidence: **99.13%**
4808. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/arguments/preprocessCommandLineArguments.kt`** -> AI Confidence: **99.13%**
4809. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/plugins/PluginsOptionsParser.kt`** -> AI Confidence: **99.13%**
4810. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/compiler/plugin/ExtensionRegistrationUtils.kt`** -> AI Confidence: **99.13%**
4811. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/constant/ConstantValueUtils.kt`** -> AI Confidence: **99.13%**
4812. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/PrimitiveComparison.kt`** -> AI Confidence: **99.13%**
4813. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/substitution/AbstractConeSubstitutor.kt`** -> AI Confidence: **99.13%**
4814. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/substitution/ConeRawScopeSubstitutor.kt`** -> AI Confidence: **99.13%**
4815. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/ConeTypePreparator.kt`** -> AI Confidence: **99.13%**
4816. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/TypeUnification.kt`** -> AI Confidence: **99.13%**
4817. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/ConeEquivalentCallConflictResolver.kt`** -> AI Confidence: **99.13%**
4818. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/DesignationState.kt`** -> AI Confidence: **99.13%**
4819. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/comparators/FirCallableDeclarationComparator.kt`** -> AI Confidence: **99.13%**
4820. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/comparators/FirMemberDeclarationComparator.kt`** -> AI Confidence: **99.13%**
4821. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/comparators/FirTypeParameterRefComparator.kt`** -> AI Confidence: **99.13%**
4822. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirAllModifierRenderer.kt`** -> AI Confidence: **99.13%**
4823. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirPropertyAccessorRenderer.kt`** -> AI Confidence: **99.13%**
4824. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/printer/ElementPrinter.kt`** -> AI Confidence: **99.13%**
4825. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/UnreachableCodeLightTreeHelper.kt`** -> AI Confidence: **99.13%**
4826. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaClassifierTypeImpl.kt`** -> AI Confidence: **99.13%**
4827. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/FunctionDelegateMemberNameClashChecker.kt`** -> AI Confidence: **99.13%**
4828. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/effects/PsiReturnsEffectParser.kt`** -> AI Confidence: **99.13%**
4829. **`compiler/frontend/src/org/jetbrains/kotlin/extensions/AnnotationBasedExtension.kt`** -> AI Confidence: **99.13%**
4830. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ConfusingWhenBranchSyntaxChecker.kt`** -> AI Confidence: **99.13%**
4831. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DataClassDeclarationChecker.kt`** -> AI Confidence: **99.13%**
4832. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SealedInterfaceAllowedChecker.kt`** -> AI Confidence: **99.13%**
4833. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/AbiSnapshotDiffService.kt`** -> AI Confidence: **99.13%**
4834. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/IrWhenUtils.kt`** -> AI Confidence: **99.13%**
4835. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsPropertyAccessorInlineLowering.kt`** -> AI Confidence: **99.13%**
4836. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/SwitchOptimizer.kt`** -> AI Confidence: **99.13%**
4837. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/JsMainFunctionDetector.kt`** -> AI Confidence: **99.13%**
4838. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmLocalDeclarationPopupLowering.kt`** -> AI Confidence: **99.13%**
4839. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/irConstExpressionValuesEqualityChecker.kt`** -> AI Confidence: **99.13%**
4840. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DynamicCalls.kt`** -> AI Confidence: **99.13%**
4841. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/declarationStartOffset.kt`** -> AI Confidence: **99.13%**
4842. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/IrUtils.kt`** -> AI Confidence: **99.13%**
4843. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrFakeOverrideUtils.kt`** -> AI Confidence: **99.13%**
4844. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrInlineUtils.kt`** -> AI Confidence: **99.13%**
4845. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/transform.kt`** -> AI Confidence: **99.13%**
4846. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/declaration/IrFunctionParametersChecker.kt`** -> AI Confidence: **99.13%**
4847. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/wasm/declarations/WasmKlibExportsChecker.kt`** -> AI Confidence: **99.13%**
4848. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/KDocLinkParser.kt`** -> AI Confidence: **99.13%**
4849. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/AbstractKotlinParsing.kt`** -> AI Confidence: **99.13%**
4850. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/EditCommaSeparatedListHelper.kt`** -> AI Confidence: **99.13%**
4851. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KotlinStringLiteralTextEscaper.kt`** -> AI Confidence: **99.13%**
4852. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtTypeReference.kt`** -> AI Confidence: **99.13%**
4853. **`compiler/resolution.common.jvm/src/org/jetbrains/kotlin/resolve/jvm/JvmTypeSpecificityComparator.kt`** -> AI Confidence: **99.13%**
4854. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/NewCommonSuperTypeCalculator.kt`** -> AI Confidence: **99.13%**
4855. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/LegacyVariableReadinessCalculator.kt`** -> AI Confidence: **99.13%**
4856. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/VariableReadinessCalculator.kt`** -> AI Confidence: **99.13%**
4857. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/mpp/matcherCheckerCommonUtils.kt`** -> AI Confidence: **99.13%**
4858. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/CallableReferenceArgumentResolver.kt`** -> AI Confidence: **99.13%**
4859. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/typeConversions.kt`** -> AI Confidence: **99.13%**
4860. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/multiplatform/ExpectedActualResolver.kt`** -> AI Confidence: **99.13%**
4861. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/AbstractTwoAttributesMetaInfoProcessor.kt`** -> AI Confidence: **99.13%**
4862. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/FirIdenticalCheckerHelper.kt`** -> AI Confidence: **99.13%**
4863. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/inferencelogs/MermaidInferenceLogsDumper.kt`** -> AI Confidence: **99.13%**
4864. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/TestExceptionsComparator.kt`** -> AI Confidence: **99.13%**
4865. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/fir/FirCfgConsistencyChecker.kt`** -> AI Confidence: **99.13%**
4866. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/validators/AbstractTestValidator.kt`** -> AI Confidence: **99.13%**
4867. **`compiler/util/src/org/jetbrains/kotlin/utils/psiUtils.kt`** -> AI Confidence: **99.13%**
4868. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/load/java/propertiesConventionUtil.kt`** -> AI Confidence: **99.13%**
4869. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/types/RawProjectionComputer.kt`** -> AI Confidence: **99.13%**
4870. **`core/descriptors.jvm/src/org/jetbrains/kotlin/resolve/jvm/inlineClassManglingRules.kt`** -> AI Confidence: **99.13%**
4871. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/ConstantValueFactory.kt`** -> AI Confidence: **99.13%**
4872. **`core/descriptors/src/org/jetbrains/kotlin/types/ClassifierBasedTypeConstructor.kt`** -> AI Confidence: **99.13%**
4873. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/IntersectionType.kt`** -> AI Confidence: **99.13%**
4874. **`core/descriptors/src/org/jetbrains/kotlin/util/scopeUtils.kt`** -> AI Confidence: **99.13%**
4875. **`core/deserialization.common/src/org/jetbrains/kotlin/serialization/deserialization/ProtoBufContractDeserializer.kt`** -> AI Confidence: **99.13%**
4876. **`core/deserialization.common/src/org/jetbrains/kotlin/serialization/deserialization/ProtoEnumFlags.kt`** -> AI Confidence: **99.13%**
4877. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KotlinKProperty.kt`** -> AI Confidence: **99.13%**
4878. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/calls/AnnotationConstructorCaller.kt`** -> AI Confidence: **99.13%**
4879. **`generators/builtins/floorDivMod.kt`** -> AI Confidence: **99.13%**
4880. **`generators/builtins/ranges.kt`** -> AI Confidence: **99.13%**
4881. **`generators/main/GeneratorsFileUtil.kt`** -> AI Confidence: **99.13%**
4882. **`generators/tree-generator-common/src/org/jetbrains/kotlin/generators/tree/AbstractBuilderPrinter.kt`** -> AI Confidence: **99.13%**
4883. **`generators/tree-generator-common/src/org/jetbrains/kotlin/generators/tree/AbstractFieldPrinter.kt`** -> AI Confidence: **99.13%**
4884. **`generators/tree-generator-common/src/org/jetbrains/kotlin/generators/tree/AbstractImplementationPrinter.kt`** -> AI Confidence: **99.13%**
4885. **`generators/tree-generator-common/src/org/jetbrains/kotlin/generators/tree/AbstractVisitorPrinter.kt`** -> AI Confidence: **99.13%**
4886. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsReifiedNativeChecker.kt`** -> AI Confidence: **99.13%**
4887. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/engine/ExternalTool.kt`** -> AI Confidence: **99.13%**
4888. **`js/js.translator/src/org/jetbrains/kotlin/js/inline/clean/MoveTemporaryVariableDeclarationToAssignment.kt`** -> AI Confidence: **99.13%**
4889. **`js/js.translator/src/org/jetbrains/kotlin/js/inline/clean/RedundantCallElimination.kt`** -> AI Confidence: **99.13%**
4890. **`js/typescript-printer/src/org/jetbrains/kotlin/ir/backend/js/tsexport/ExportModelToTsDeclarations.kt`** -> AI Confidence: **99.13%**
4891. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/SimpleBridgeGeneratorImpl.kt`** -> AI Confidence: **99.13%**
4892. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/StubIrMetadataEmitter.kt`** -> AI Confidence: **99.13%**
4893. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/TargetAbiInfo.kt`** -> AI Confidence: **99.13%**
4894. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/internal/test/TestRunner.kt`** -> AI Confidence: **99.13%**
4895. **`libraries/scripting/common/src/kotlin/script/experimental/api/scriptEvaluation.kt`** -> AI Confidence: **99.13%**
4896. **`libraries/scripting/dependencies/src/kotlin/script/experimental/dependencies/FileSystemDependenciesResolver.kt`** -> AI Confidence: **99.13%**
4897. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/BasicJvmReplEvaluator.kt`** -> AI Confidence: **99.13%**
4898. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/impl/KJvmCompiledScript.kt`** -> AI Confidence: **99.13%**
4899. **`libraries/stdlib/jvm/src/kotlin/collections/builders/MapBuilder.kt`** -> AI Confidence: **99.13%**
4900. **`libraries/stdlib/jvm/src/kotlin/text/StringsJVM.kt`** -> AI Confidence: **99.13%**
4901. **`libraries/stdlib/src/kotlin/time/Instant.kt`** -> AI Confidence: **99.13%**
4902. **`libraries/stdlib/src/kotlin/util/Result.kt`** -> AI Confidence: **99.13%**
4903. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/tasks/DirTask.kt`** -> AI Confidence: **99.13%**
4904. **`libraries/tools/abi-validation/abi-tools/src/main/kotlin/org/jetbrains/kotlin/abi/tools/impl/klib/KlibAbiDumpFileMerger.kt`** -> AI Confidence: **99.13%**
4905. **`libraries/tools/abi-validation/abi-tools/src/main/kotlin/org/jetbrains/kotlin/abi/tools/impl/klib/KlibReading.kt`** -> AI Confidence: **99.13%**
4906. **`libraries/tools/binary-compatibility-validator/src/test/kotlin/org.jetbrains.kotlin.tools.tests/utils.kt`** -> AI Confidence: **99.13%**
4907. **`libraries/tools/dukat/src/main/kotlin/org/jetbrains/kotlin/tools/dukat/download.kt`** -> AI Confidence: **99.13%**
4908. **`libraries/tools/dukat/src/main/kotlin/org/jetbrains/kotlin/tools/dukat/wasm/resolveTypes.kt`** -> AI Confidence: **99.13%**
4909. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/nativeTestHelpers.kt`** -> AI Confidence: **99.13%**
4910. **`libraries/tools/kotlin-gradle-plugin/build.gradle.kts`** -> AI Confidence: **99.13%**
4911. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/XcodeEnvironment.kt`** -> AI Confidence: **99.13%**
4912. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/transformMetadataLibraries.kt`** -> AI Confidence: **99.13%**
4913. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/GradleNodeModuleBuilder.kt`** -> AI Confidence: **99.13%**
4914. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/LockStoreTask.kt`** -> AI Confidence: **99.13%**
4915. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmProjectModules.kt`** -> AI Confidence: **99.13%**
4916. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmVersions.kt`** -> AI Confidence: **99.13%**
4917. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/PackageJson.kt`** -> AI Confidence: **99.13%**
4918. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/MavenTestProject.kt`** -> AI Confidence: **99.13%**
4919. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/jdk/OsxJavaHomeProvider.kt`** -> AI Confidence: **99.13%**
4920. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/jdk/WindowsJdkProvider.kt`** -> AI Confidence: **99.13%**
4921. **`libraries/tools/kotlin-stdlib-gen/src/generators/math/mathTestGeneratorMain.kt`** -> AI Confidence: **99.13%**
4922. **`libraries/tools/kotlinp/jvm/src/org/jetbrains/kotlin/kotlinp/jvm/Main.kt`** -> AI Confidence: **99.13%**
4923. **`libraries/tools/stats-analyser/src/org/jetbrains/kotlin/stats/FileUtils.kt`** -> AI Confidence: **99.13%**
4924. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/PropertyCommonizer.kt`** -> AI Confidence: **99.13%**
4925. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/utils/misc.kt`** -> AI Confidence: **99.13%**
4926. **`native/native.tests/testData/samples/standalone_notr_long_running.kt`** -> AI Confidence: **99.13%**
4927. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateEnumMembers.kt`** -> AI Confidence: **99.13%**
4928. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCFunctionType.kt`** -> AI Confidence: **99.13%**
4929. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirDeclarationNamerImpl.kt`** -> AI Confidence: **99.13%**
4930. **`plugins/compose/group-mapping/src/main/kotlin/androidx/compose/compiler/mapping/bytecode/BytecodeTokenizer.kt`** -> AI Confidence: **99.13%**
4931. **`plugins/jvm-abi-gen/src/org/jetbrains/kotlin/jvm/abi/JvmAbiMetadataProcessor.kt`** -> AI Confidence: **99.13%**
4932. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/explode.kt`** -> AI Confidence: **99.13%**
4933. **`plugins/kotlinx-serialization/testData/boxIr/delegatedProperty.kt`** -> AI Confidence: **99.13%**
4934. **`plugins/scripting/scripting-ide-common/src/org/jetbrains/kotlin/scripting/ide_common/idea/util/extensionsUtils.kt`** -> AI Confidence: **99.13%**
4935. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/YarnAndNpmSupressor.kt`** -> AI Confidence: **99.13%**
4936. **`repo/gradle-build-conventions/buildsrc-compat/src/main/kotlin/build-time-report.gradle.kts`** -> AI Confidence: **99.13%**
4937. **`wasm/wasm.ir/src/org/jetbrains/kotlin/wasm/ir/convertors/WasmBinaryToIR.kt`** -> AI Confidence: **99.13%**
4938. **`wasm/wasm.ir/src/org/jetbrains/kotlin/wasm/ir/convertors/WasmIrToBinary.kt`** -> AI Confidence: **99.13%**
4939. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/Usage.java`** -> AI Confidence: **99.13%**
4940. **`compiler/psi/parser/src/org/jetbrains/kotlin/kdoc/parser/KDocParser.java`** -> AI Confidence: **99.13%**
4941. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtNamedDeclarationUtil.java`** -> AI Confidence: **99.13%**
4942. **`kotlin-native/runtime/src/libbacktrace/c/sort.c`** -> AI Confidence: **99.13%**
4943. **`kotlin-native/runtime/src/main/cpp/objc_support/NSNotificationSubscriptionTest.mm`** -> AI Confidence: **99.13%**
4944. **`kotlin-native/runtime/src/objc/cpp/ObjCInteropUtilsClasses.mm`** -> AI Confidence: **99.13%**
4945. **`kotlin-native/common/files/src/main/cpp/Files.cpp`** -> AI Confidence: **99.13%**
4946. **`kotlin-native/runtime/src/alloc/custom/cpp/NextFitPage.cpp`** -> AI Confidence: **99.13%**
4947. **`kotlin-native/runtime/src/main/cpp/TypeInfo.cpp`** -> AI Confidence: **99.13%**
4948. **`kotlin-native/runtime/src/main/cpp/concurrent/ScopedThread.cpp`** -> AI Confidence: **99.13%**
4949. **`kotlin-native/runtime/src/test_support/cpp/CompilerGenerated.cpp`** -> AI Confidence: **99.13%**
4950. **`analysis/analysis-api/testData/components/dataFlowInfoProvider/exitPointSnapshot/controlFlow/differentTargets/break.kt`** -> AI Confidence: **99.11%**
4951. **`analysis/analysis-api/testData/components/dataFlowInfoProvider/exitPointSnapshot/controlFlow/unconditionalJumps/break4.kt`** -> AI Confidence: **99.11%**
4952. **`analysis/low-level-api-fir/testData/getOrBuildFir/partialBodyAnalysis/conditions2.kt`** -> AI Confidence: **99.11%**
4953. **`compiler/fir/analysis-tests/testData/resolve/inference/equalityRhsInDependentContext.kt`** -> AI Confidence: **99.11%**
4954. **`compiler/fir/raw-fir/psi2fir/testData/rawBuilder/declarations/multiDeclarations.kt`** -> AI Confidence: **99.11%**
4955. **`compiler/psi/psi-impl/testData/psi/destructuring/annotationOnFullNameBasedDestructuring.kt`** -> AI Confidence: **99.11%**
4956. **`compiler/psi/psi-impl/testData/psi/suggestGuardSyntax.kt`** -> AI Confidence: **99.11%**
4957. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/kt2972.kt`** -> AI Confidence: **99.11%**
4958. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/reassignmentInTryCatch.fir.kt`** -> AI Confidence: **99.11%**
4959. **`compiler/testData/diagnostics/tests/controlFlowAnalysis/reassignmentInTryCatch.kt`** -> AI Confidence: **99.11%**
4960. **`compiler/testData/diagnostics/tests/controlStructures/emptyIf.kt`** -> AI Confidence: **99.11%**
4961. **`compiler/testData/diagnostics/tests/crv/controlFlow.fir.kt`** -> AI Confidence: **99.11%**
4962. **`compiler/testData/diagnostics/tests/crv/controlFlow.kt`** -> AI Confidence: **99.11%**
4963. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/When.fir.kt`** -> AI Confidence: **99.11%**
4964. **`compiler/testData/diagnostics/tests/dataFlowInfoTraversal/When.kt`** -> AI Confidence: **99.11%**
4965. **`compiler/testData/diagnostics/tests/explicitDefinitelyNotNullableViaIntersection/isAsOperators.kt`** -> AI Confidence: **99.11%**
4966. **`compiler/testData/diagnostics/tests/explicitDefinitelyNotNullableViaIntersection/isAsOperatorsEnabled.kt`** -> AI Confidence: **99.11%**
4967. **`compiler/testData/diagnostics/tests/functionLiterals/return/IfWithoutElseWithExplicitType.fir.kt`** -> AI Confidence: **99.11%**
4968. **`compiler/testData/diagnostics/tests/functionLiterals/return/IfWithoutElseWithExplicitType.kt`** -> AI Confidence: **99.11%**
4969. **`compiler/testData/diagnostics/tests/functionTypeInitializerTypeMismatch.kt`** -> AI Confidence: **99.11%**
4970. **`compiler/testData/diagnostics/tests/inference/coercionToUnit/coercionToUnitForIfAsLastExpressionInLambda.fir.kt`** -> AI Confidence: **99.11%**
4971. **`compiler/testData/diagnostics/tests/inference/coercionToUnit/coercionToUnitForIfAsLastExpressionInLambda.kt`** -> AI Confidence: **99.11%**
4972. **`compiler/testData/diagnostics/tests/regressions/kt35668.fir.kt`** -> AI Confidence: **99.11%**
4973. **`compiler/testData/diagnostics/tests/regressions/kt35668.kt`** -> AI Confidence: **99.11%**
4974. **`compiler/testData/diagnostics/tests/smartCasts/binaryOperatorsWithJumps.fir.kt`** -> AI Confidence: **99.11%**
4975. **`compiler/testData/diagnostics/tests/smartCasts/binaryOperatorsWithJumps.kt`** -> AI Confidence: **99.11%**
4976. **`compiler/testData/diagnostics/tests/smartCasts/binaryOperatorsWithJumps_before.fir.kt`** -> AI Confidence: **99.11%**
4977. **`compiler/testData/diagnostics/tests/smartCasts/binaryOperatorsWithJumps_before.kt`** -> AI Confidence: **99.11%**
4978. **`compiler/testData/diagnostics/tests/smartCasts/ifCascadeExprNotNull.fir.kt`** -> AI Confidence: **99.11%**
4979. **`compiler/testData/diagnostics/tests/smartCasts/ifCascadeExprNotNull.kt`** -> AI Confidence: **99.11%**
4980. **`compiler/testData/diagnostics/tests/smartCasts/loops/nestedLoops.fir.kt`** -> AI Confidence: **99.11%**
4981. **`compiler/testData/diagnostics/tests/smartCasts/loops/nestedLoops.kt`** -> AI Confidence: **99.11%**
4982. **`compiler/testData/diagnostics/tests/smartCasts/throwInTry.fir.kt`** -> AI Confidence: **99.11%**
4983. **`compiler/testData/diagnostics/tests/smartCasts/throwInTry.kt`** -> AI Confidence: **99.11%**
4984. **`compiler/testData/diagnostics/tests/smartCasts/variables/capturedWithControlJumps.fir.kt`** -> AI Confidence: **99.11%**
4985. **`compiler/testData/diagnostics/tests/smartCasts/variables/capturedWithControlJumps.kt`** -> AI Confidence: **99.11%**
4986. **`compiler/testData/diagnostics/tests/smartCasts/varnotnull/nestedLoops.fir.kt`** -> AI Confidence: **99.11%**
4987. **`compiler/testData/diagnostics/tests/smartCasts/varnotnull/nestedLoops.kt`** -> AI Confidence: **99.11%**
4988. **`compiler/testData/diagnostics/testsWithJsStdLibAndBackendCompilation/jsCode/inlinedReturnBreakContinue/withReturnValue.kt`** -> AI Confidence: **99.11%**
4989. **`js/js.translator/testData/box/expression/evaluationOrder/intrinsicComplex.kt`** -> AI Confidence: **99.11%**
4990. **`js/js.translator/testData/box/expression/if/nestedIf.kt`** -> AI Confidence: **99.11%**
4991. **`js/js.translator/testData/box/expression/when/whenWithOneStmWhen.kt`** -> AI Confidence: **99.11%**
4992. **`js/js.translator/testData/box/labels/peculiarNames.kt`** -> AI Confidence: **99.11%**
4993. **`js/js.translator/testData/box/simple/breakDoWhile.kt`** -> AI Confidence: **99.11%**
4994. **`js/js.translator/testData/box/simple/continueDoWhile.kt`** -> AI Confidence: **99.11%**
4995. **`js/js.translator/testData/incremental/invalidation/multiPlatformClashFileNames/main/m.kt`** -> AI Confidence: **99.11%**
4996. **`js/js.translator/testData/incremental/invalidation/multiPlatformClashFileNamesWithCrossModuleInliner/main/m.kt`** -> AI Confidence: **99.11%**
4997. **`kotlin-native/performance/ring/src/commonMain/kotlin/org/jetbrains/ring/PrimeListBenchmark.kt`** -> AI Confidence: **99.11%**
4998. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/s_ilogb.kt`** -> AI Confidence: **99.11%**
4999. **`libraries/stdlib/wasm/src/kotlin/math/fdlibm/s_tanh.kt`** -> AI Confidence: **99.11%**
5000. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/exceptionUtils.kt`** -> AI Confidence: **99.11%**
5001. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/BridgeProvider/StringUtils.kt`** -> AI Confidence: **99.11%**
5002. **`kotlin-native/runtime/src/gc/common/cpp/MarkAndSweepUtils.hpp`** -> AI Confidence: **99.11%**
5003. **`kotlin-native/runtime/src/gc/common/cpp/TracingGCTest.hpp`** -> AI Confidence: **99.11%**
5004. **`kotlin-native/runtime/src/gcScheduler/common/cpp/MutatorAssists.hpp`** -> AI Confidence: **99.11%**
5005. **`kotlin-native/runtime/src/main/cpp/RepeatedTimer.hpp`** -> AI Confidence: **99.11%**
5006. **`kotlin-native/runtime/src/main/cpp/objc_support/RunLoopTestSupport.hpp`** -> AI Confidence: **99.11%**
5007. **`native/native.tests/testData/framework/objcexport/objCName.swift`** -> AI Confidence: **99.11%**
5008. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/commonizeSQLiteAndCurlInterop/libs/include/curl/typecheck-gcc.h`** -> AI Confidence: **99.1%**
5009. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/Fe10AnalysisFacade.kt`** -> AI Confidence: **99.09%**
5010. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ReferenceShortener.kt`** -> AI Confidence: **99.09%**
5011. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ResolveExtensionInfoProvider.kt`** -> AI Confidence: **99.09%**
5012. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SignatureSubstitutor.kt`** -> AI Confidence: **99.09%**
5013. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescAnonymousFunctionSymbol.kt`** -> AI Confidence: **99.09%**
5014. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescAnonymousObjectSymbol.kt`** -> AI Confidence: **99.09%**
5015. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescDefaultPropertyGetterSymbol.kt`** -> AI Confidence: **99.09%**
5016. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescDefaultPropertySetterSymbol.kt`** -> AI Confidence: **99.09%**
5017. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescJavaFieldSymbol.kt`** -> AI Confidence: **99.09%**
5018. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescLocalVariableSymbol.kt`** -> AI Confidence: **99.09%**
5019. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescPropertyGetterSymbol.kt`** -> AI Confidence: **99.09%**
5020. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescPropertySetterSymbol.kt`** -> AI Confidence: **99.09%**
5021. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescTypeAliasSymbol.kt`** -> AI Confidence: **99.09%**
5022. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescTypeParameterSymbol.kt`** -> AI Confidence: **99.09%**
5023. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiDefaultBackingFieldSymbol.kt`** -> AI Confidence: **99.09%**
5024. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiLoopParameterLocalVariableSymbol.kt`** -> AI Confidence: **99.09%**
5025. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiTypeParameterSymbol.kt`** -> AI Confidence: **99.09%**
5026. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/base/KaFe10Type.kt`** -> AI Confidence: **99.09%**
5027. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/base/DummyKtFe10ReferenceResolutionHelper.kt`** -> AI Confidence: **99.09%**
5028. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/base/KtFe10ReferenceResolutionHelper.kt`** -> AI Confidence: **99.09%**
5029. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/generatorUtils.kt`** -> AI Confidence: **99.09%**
5030. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/rendererrs/AbstractDiagnosticsDataClassRenderer.kt`** -> AI Confidence: **99.09%**
5031. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaFirSession.kt`** -> AI Confidence: **99.09%**
5032. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirDiagnosticProvider.kt`** -> AI Confidence: **99.09%**
5033. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirInternalCacheStorage.kt`** -> AI Confidence: **99.09%**
5034. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSessionComponent.kt`** -> AI Confidence: **99.09%**
5035. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/diagnostics/KaAbstractFirDiagnostic.kt`** -> AI Confidence: **99.09%**
5036. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirInvokeFunctionReference.kt`** -> AI Confidence: **99.09%**
5037. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/KaFirBasedScope.kt`** -> AI Confidence: **99.09%**
5038. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/KaFirDelegatingTypeScope.kt`** -> AI Confidence: **99.09%**
5039. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/KaFirPackageScope.kt`** -> AI Confidence: **99.09%**
5040. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirJavaFieldSymbol.kt`** -> AI Confidence: **99.09%**
5041. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSamConstructorSymbol.kt`** -> AI Confidence: **99.09%**
5042. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSyntheticJavaPropertySymbol.kt`** -> AI Confidence: **99.09%**
5043. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSyntheticPropertyGetterSymbol.kt`** -> AI Confidence: **99.09%**
5044. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSyntheticPropertySetterSymbol.kt`** -> AI Confidence: **99.09%**
5045. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirDefinitelyNotNullType.kt`** -> AI Confidence: **99.09%**
5046. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/annotations/annotationValues.kt`** -> AI Confidence: **99.09%**
5047. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/resolution/KaBaseAnnotationCall.kt`** -> AI Confidence: **99.09%**
5048. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/resolution/KaBaseDelegatedConstructorCall.kt`** -> AI Confidence: **99.09%**
5049. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/resolution/KaBaseImplicitInvokeCall.kt`** -> AI Confidence: **99.09%**
5050. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/resolution/KaBaseSimpleFunctionCall.kt`** -> AI Confidence: **99.09%**
5051. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/resolution/KaBaseSimpleVariableAccessCall.kt`** -> AI Confidence: **99.09%**
5052. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/api/standalone/StandaloneAnalysisAPISessionBuilder.kt`** -> AI Confidence: **99.09%**
5053. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/impl/KaLibraryModuleImpl.kt`** -> AI Confidence: **99.09%**
5054. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/impl/KaScriptModuleImpl.kt`** -> AI Confidence: **99.09%**
5055. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/KaSession.kt`** -> AI Confidence: **99.09%**
5056. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaCompilerFacility.kt`** -> AI Confidence: **99.09%**
5057. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/KaDeclarationRenderer.kt`** -> AI Confidence: **99.09%**
5058. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/impl/KaDeclarationRendererForSource.kt`** -> AI Confidence: **99.09%**
5059. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/resolution/KaCalls.kt`** -> AI Confidence: **99.09%**
5060. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaFunctionSymbol.kt`** -> AI Confidence: **99.09%**
5061. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaVariableSymbol.kt`** -> AI Confidence: **99.09%**
5062. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/types/KaType.kt`** -> AI Confidence: **99.09%**
5063. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/types/typeCreation/KaTypeCreator.kt`** -> AI Confidence: **99.09%**
5064. **`analysis/analysis-api/testData/components/resolver/allByPsi/imports/topLevelObjectWithBaseClass.kt`** -> AI Confidence: **99.09%**
5065. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/KotlinAsJavaSupport.kt`** -> AI Confidence: **99.09%**
5066. **`analysis/low-level-api-fir/low-level-api-fir-compiler-tests/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/compiler/based/TestGenerator.kt`** -> AI Confidence: **99.09%**
5067. **`analysis/low-level-api-fir/low-level-api-fir-native-compiler-tests/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/konan/compiler/based/AbstractLLNativeDiagnosticsTestBase.kt`** -> AI Confidence: **99.09%**
5068. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/FirDesignationState.kt`** -> AI Confidence: **99.09%**
5069. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/LLFirModuleResolveComponents.kt`** -> AI Confidence: **99.09%**
5070. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/NonLocalAnnotationVisitor.kt`** -> AI Confidence: **99.09%**
5071. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirBuiltinsAndCloneableSessionProvider.kt`** -> AI Confidence: **99.09%**
5072. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirLibrarySessionProvider.kt`** -> AI Confidence: **99.09%**
5073. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/services/LLRealFirElementByPsiElementChooser.kt`** -> AI Confidence: **99.09%**
5074. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLEmptyKotlinSymbolProvider.kt`** -> AI Confidence: **99.09%**
5075. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLFirJavaSymbolProvider.kt`** -> AI Confidence: **99.09%**
5076. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/TestGenerator.kt`** -> AI Confidence: **99.09%**
5077. **`analysis/stubs/testFixtures/org/jetbrains/kotlin/analysis/stubs/CompiledStubsTestEngine.kt`** -> AI Confidence: **99.09%**
5078. **`build-common/src/org/jetbrains/kotlin/incremental/impl/ExtraClassInfoGenerator.kt`** -> AI Confidence: **99.09%**
5079. **`compiler/backend.common.jvm/src/org/jetbrains/kotlin/codegen/CommonVariableAsmNameManglingUtils.kt`** -> AI Confidence: **99.09%**
5080. **`compiler/backend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/TypeMappingModeExtensions.kt`** -> AI Confidence: **99.09%**
5081. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/BuildersCompatibilitySmokeTest.kt`** -> AI Confidence: **99.09%**
5082. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/CompilerArgumentCompatibilityTest.kt`** -> AI Confidence: **99.09%**
5083. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/BuildersCompatibilitySmokeTest.kt`** -> AI Confidence: **99.09%**
5084. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/CompilerPluginsUnsupportedTest.kt`** -> AI Confidence: **99.09%**
5085. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/LookupTrackerTest.kt`** -> AI Confidence: **99.09%**
5086. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/SnapshotPathSmokeTest.kt`** -> AI Confidence: **99.09%**
5087. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testDefaultOptions/kotlin/DaemonExecutionPolicyDefaultsTest.kt`** -> AI Confidence: **99.09%**
5088. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testDefaultOptions/kotlin/JvmClasspathSnapshottingOperationDefaultsTest.kt`** -> AI Confidence: **99.09%**
5089. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testDefaultOptions/kotlin/JvmCompilationOperationDefaultsTest.kt`** -> AI Confidence: **99.09%**
5090. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testExample/kotlin/ExampleIncrementalCompilationTest.kt`** -> AI Confidence: **99.09%**
5091. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testExample/kotlin/ExampleIncrementalScenarioTest.kt`** -> AI Confidence: **99.09%**
5092. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testExample/kotlin/ExampleNonIncrementalCompilationTest.kt`** -> AI Confidence: **99.09%**
5093. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testFirRunner/kotlin/SingleModuleFirRunnerIncrementalTest.kt`** -> AI Confidence: **99.09%**
5094. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testInputChangesTracking/kotlin/SourceChangesTrackingTest.kt`** -> AI Confidence: **99.09%**
5095. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/jvm/operations/JvmCompilationOperation.kt`** -> AI Confidence: **99.09%**
5096. **`compiler/build-tools/kotlin-build-tools-cri-impl/src/test/kotlin/CriSerializationTest.kt`** -> AI Confidence: **99.09%**
5097. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/arguments/CompilerPluginsRelated.kt`** -> AI Confidence: **99.09%**
5098. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/jvm/JvmSnapshotBasedIncrementalCompilationConfigurationImpl.kt`** -> AI Confidence: **99.09%**
5099. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/jvm/operations/JvmClasspathSnapshottingOperationImpl.kt`** -> AI Confidence: **99.09%**
5100. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/BtaCompilerArgument.kt`** -> AI Confidence: **99.09%**
5101. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/CliDiagnosticReporting.kt`** -> AI Confidence: **99.09%**
5102. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/arguments/JavaTypeEnhancementStateParser.kt`** -> AI Confidence: **99.09%**
5103. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/CliLightClassGenerationSupport.kt`** -> AI Confidence: **99.09%**
5104. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/cliJavaModuleUtils.kt`** -> AI Confidence: **99.09%**
5105. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/modules/JavaModuleGraph.kt`** -> AI Confidence: **99.09%**
5106. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/utils/parametersMap.kt`** -> AI Confidence: **99.09%**
5107. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/klib/TopDownAnalyzerFacadeForJSIR.kt`** -> AI Confidence: **99.09%**
5108. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/legacy/pipeline/compilerPipelineData.kt`** -> AI Confidence: **99.09%**
5109. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFir2IrPipelinePhase.kt`** -> AI Confidence: **99.09%**
5110. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/MetadataUtils.kt`** -> AI Confidence: **99.09%**
5111. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/resolve/KonanLibrariesResolveSupport.kt`** -> AI Confidence: **99.09%**
5112. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/PipelineArtifacts.kt`** -> AI Confidence: **99.09%**
5113. **`compiler/daemon/daemon-common/src/org/jetbrains/kotlin/daemon/common/ClientUtils.kt`** -> AI Confidence: **99.09%**
5114. **`compiler/daemon/daemon-common/src/org/jetbrains/kotlin/daemon/common/FileSystemUtils.kt`** -> AI Confidence: **99.09%**
5115. **`compiler/fir/analysis-tests/testData/resolve/annotations/wrongDslMarkerTargets.kt`** -> AI Confidence: **99.09%**
5116. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/FirDiagnosticsList.kt`** -> AI Confidence: **99.09%**
5117. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/FirJsDiagnosticsList.kt`** -> AI Confidence: **99.09%**
5118. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/FirJvmDiagnosticsList.kt`** -> AI Confidence: **99.09%**
5119. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/FirNativeDiagnosticsList.kt`** -> AI Confidence: **99.09%**
5120. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsReifiedJsNoRuntimeChecker.kt`** -> AI Confidence: **99.09%**
5121. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirDeclarationJavaNullabilityWarningCheckers.kt`** -> AI Confidence: **99.09%**
5122. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirUpperBoundsChecker.kt`** -> AI Confidence: **99.09%**
5123. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/diagnostics/native/FirNativeErrorsDefaultMessages.kt`** -> AI Confidence: **99.09%**
5124. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativePackageDirectiveChecker.kt`** -> AI Confidence: **99.09%**
5125. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirMultipleJsExportDefaultAnnotationChecker.kt`** -> AI Confidence: **99.09%**
5126. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/CheckersComponent.kt`** -> AI Confidence: **99.09%**
5127. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/context/CheckerContextForProvider.kt`** -> AI Confidence: **99.09%**
5128. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/checkers/CheckersContainers.kt`** -> AI Confidence: **99.09%**
5129. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/extensions/FirExtensionRegistrar.kt`** -> AI Confidence: **99.09%**
5130. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/ComponentsContainers.kt`** -> AI Confidence: **99.09%**
5131. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirNativeSessionFactory.kt`** -> AI Confidence: **99.09%**
5132. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirWasmSessionFactory.kt`** -> AI Confidence: **99.09%**
5133. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/FirSyntheticPropertiesStorage.kt`** -> AI Confidence: **99.09%**
5134. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/AnnotationsLoader.kt`** -> AI Confidence: **99.09%**
5135. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/enhancement/FirJavaAnnotationList.kt`** -> AI Confidence: **99.09%**
5136. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmBackendExtension.kt`** -> AI Confidence: **99.09%**
5137. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrCommonMemberStorage.kt`** -> AI Confidence: **99.09%**
5138. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrComponentsStorage.kt`** -> AI Confidence: **99.09%**
5139. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrExtensions.kt`** -> AI Confidence: **99.09%**
5140. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyConstructor.kt`** -> AI Confidence: **99.09%**
5141. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyField.kt`** -> AI Confidence: **99.09%**
5142. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyTypeAlias.kt`** -> AI Confidence: **99.09%**
5143. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/FunctionBuildingContext.kt`** -> AI Confidence: **99.09%**
5144. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/FunctionCopyUtils.kt`** -> AI Confidence: **99.09%**
5145. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/GeneratedDeclarationValidation.kt`** -> AI Confidence: **99.09%**
5146. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirDelegatingSymbolProvider.kt`** -> AI Confidence: **99.09%**
5147. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirEmptySymbolProvider.kt`** -> AI Confidence: **99.09%**
5148. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirExtensionSyntheticFunctionInterfaceProvider.kt`** -> AI Confidence: **99.09%**
5149. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/FirOverrideChecker.kt`** -> AI Confidence: **99.09%**
5150. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirDynamicScope.kt`** -> AI Confidence: **99.09%**
5151. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/fir/DestructuringDeclaration.kt`** -> AI Confidence: **99.09%**
5152. **`compiler/fir/raw-fir/light-tree2fir/testFixtures/org/jetbrains/kotlin/fir/lightTree/AbstractLightTree2FirConverterTestCase.kt`** -> AI Confidence: **99.09%**
5153. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/FirReplSnippetConfiguratorExtension.kt`** -> AI Confidence: **99.09%**
5154. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/FirScriptConfiguratorExtension.kt`** -> AI Confidence: **99.09%**
5155. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirExpressionResolutionExtension.kt`** -> AI Confidence: **99.09%**
5156. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirFunctionCallRefinementExtension.kt`** -> AI Confidence: **99.09%**
5157. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/BodyResolveComponents.kt`** -> AI Confidence: **99.09%**
5158. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirTypeResolver.kt`** -> AI Confidence: **99.09%**
5159. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/CallInfo.kt`** -> AI Confidence: **99.09%**
5160. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirInferenceSession.kt`** -> AI Confidence: **99.09%**
5161. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirLibrarySessionProvider.kt`** -> AI Confidence: **99.09%**
5162. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/FirAnnotationArgumentsProcessor.kt`** -> AI Confidence: **99.09%**
5163. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/TypeUtils.kt`** -> AI Confidence: **99.09%**
5164. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/calls/ResolutionDiagnostic.kt`** -> AI Confidence: **99.09%**
5165. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/ExpectActualAttributes.kt`** -> AI Confidence: **99.09%**
5166. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/impl/FirDefaultPropertyBackingField.kt`** -> AI Confidence: **99.09%**
5167. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/synthetic/FirSyntheticProperty.kt`** -> AI Confidence: **99.09%**
5168. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/synthetic/FirSyntheticPropertyAccessor.kt`** -> AI Confidence: **99.09%**
5169. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirPartialModifierRenderer.kt`** -> AI Confidence: **99.09%**
5170. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/Types.kt`** -> AI Confidence: **99.09%**
5171. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/rendering/LanguageFeatureMessageRenderer.kt`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportPopularSwiftPMDependenciesTests.kt` -> **21.0228%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `99` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `134211` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `native/swift/swift-export-standalone/resources/swift/KotlinCoroutineSupport.swift` (SWIFT) -> Cumulative Risk: **768.23**
- **Archetype:** `file_cluster_16` (Distance: 11.561 IQR)
- **Magnitude:** 249.76 | **LOC:** 277 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9997%)
- **Heaviest Functions:** `next` (Impact: 24.3), `emit` (Impact: 8.2), `next` (Impact: 7.1)

### 2. `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/KotlinxCoroutinesCore/KotlinxCoroutinesCore.swift` (SWIFT) -> Cumulative Risk: **746.17**
- **Archetype:** `file_cluster_4` (Distance: 11.718 IQR)
- **Magnitude:** 0.32 | **LOC:** 232 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `emit` (Impact: 43.8), `emit` (Impact: 43.8), `flowCollector` (Impact: 43.3)

### 3. `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/KotlinxCoroutinesCore/KotlinxCoroutinesCore.kt` (KOTLIN) -> Cumulative Risk: **723.54**
- **Archetype:** `file_cluster_0` (Distance: 10.981 IQR)
- **Magnitude:** 0.25 | **LOC:** 188 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9981%), Concurrency (99.5805%)
- **Heaviest Functions:** `kotlinx_coroutines_flow_FlowCollector_em` (Impact: 21.2), `kotlinx_coroutines_flow_MutableSharedFlo` (Impact: 21.2), `kotlinx_coroutines_flow_FlowCollector__T` (Impact: 13.4)

### 4. `native/swift/swift-export-standalone-integration-tests/coroutines/testData/execution/sequences/sequences.kt` (KOTLIN) -> Cumulative Risk: **693.66**
- **Archetype:** `file_cluster_4` (Distance: 11.694 IQR)
- **Magnitude:** 0.05 | **LOC:** 72 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `testFailing` (Impact: 2.0), `testDiscarding` (Impact: 2.0), `testUpdateValue` (Impact: 1.9)

### 5. `libraries/stdlib/src/kotlin/collections/SlidingWindow.kt` (KOTLIN) -> Cumulative Risk: **682.11**
- **Archetype:** `file_cluster_16` (Distance: 12.303 IQR)
- **Magnitude:** 208.52 | **LOC:** 206 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9607%), Tech Debt (99.6433%), Concurrency (98.8373%)
- **Heaviest Functions:** `windowedIterator` (Impact: 65.7), `toArray` (Impact: 16.9), `removeFirst` (Impact: 8.9)

### 6. `compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtDeclarationStub.java` (JAVA) -> Cumulative Risk: **677.56**
- **Archetype:** `file_cluster_4` (Distance: 12.221 IQR)
- **Magnitude:** 62.08 | **LOC:** 60 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getNavigationElement` (Impact: 7.6), `getOriginalElement` (Impact: 7.0), `getDocComment` (Impact: 2.7)

### 7. `kotlin-native/runtime/src/main/cpp/ConditionVariableTest.cpp` (CPP) -> Cumulative Risk: **676.26**
- **Archetype:** `file_cluster_4` (Distance: 12.706 IQR)
- **Magnitude:** 342.8 | **LOC:** 354 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8473%)
- **Heaviest Functions:** `ConditionVariableTest` (Impact: 25.6), `GetName` (Impact: 9.0), `ConditionVariableTest` (Impact: 8.5)

### 8. `compiler/testData/ir/interpreter/helpers/Strings.kt` (KOTLIN) -> Cumulative Risk: **674.58**
- **Archetype:** `file_cluster_0` (Distance: 12.504 IQR)
- **Magnitude:** 0.11 | **LOC:** 84 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.8739%)
- **Heaviest Functions:** `trim` (Impact: 30.6), `elementAtOrElse` (Impact: 8.8), `toCollection` (Impact: 8.8)

### 9. `libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt` (KOTLIN) -> Cumulative Risk: **667.63**
- **Archetype:** `file_cluster_4` (Distance: 13.17 IQR)
- **Magnitude:** 217.1 | **LOC:** 226 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.6604%)
- **Heaviest Functions:** `yieldAll` (Impact: 50.9), `hasNext` (Impact: 16.7), `next` (Impact: 11.2)

### 10. `libraries/stdlib/jvm/src/kotlin/text/regex/Regex.kt` (KOTLIN) -> Cumulative Risk: **663.04**
- **Archetype:** `file_cluster_13` (Distance: 12.921 IQR)
- **Magnitude:** 254.28 | **LOC:** 420 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9621%), Concurrency (99.7493%), State Flux (85.1341%)
- **Heaviest Functions:** `constructor` (Impact: 67.4), `split` (Impact: 21.8), `splitToSequence` (Impact: 15.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.936 IQR)
- **Top Global Matches:** file_cluster_0: 13.936, file_cluster_8: 14.265, file_cluster_11: 14.302
- **Magnitude:** 26015.72 | **LOC:** 11868 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2874%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `importFromBlock` (Impact: 554.4)
  * `singleExpressionImpl` (Impact: 510.2)
  * `arrayElement` (Impact: 377.3)
  * `keyword` (Impact: 360.0)
  * `propertyName` (Impact: 302.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3842`, `structural_boundaries: 2895`, `args: 1506`, `func_start: 3420`, `class_start: 167`
* *Risk/State:* `safety_bypasses: 537`, `state_mutation: 1853`, `duplicate_logic: 1987`
* *Architecture:* `api: 1688`, `import: 6`
* *Defense:* `safety: 781`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.antlr.v4.runtime.atn.*, java.util.Iterator, java.util.List, org.jetbrains.kotlin.js.parser.antlr.JavaScriptParserBase, org.antlr.v4.runtime.tree.*, org.antlr.v4.runtime.*, org.jetbrains.kotlin.js.parser.antlr.JavaScriptRuleContext, java.util.ArrayList...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `libraries/stdlib/js/src/kotlin/js/math.polyfills.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.058 IQR)
- **Top Global Matches:** file_cluster_0: 12.058, file_cluster_8: 12.151, file_cluster_11: 12.721
- **Magnitude:** 3704.39 | **LOC:** 308 | **CtrlFlow:** 63.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.654%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 50`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 135`
* *Architecture:* `api: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.483 IQR)
- **Top Global Matches:** file_cluster_13: 14.483, file_cluster_11: 14.618, file_cluster_8: 14.762
- **Magnitude:** 3247.14 | **LOC:** 2154 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (90.9633%), Tech Debt (98.4004%)
**Top Internal Functions/Classes:**
  * `toKaResolutionAttempt` (Impact: 669.0)
  * `transformErrorReference` (Impact: 624.1)
  * `toKaSymbolResolutionAttempt` (Impact: 596.1)
  * `buildKaCall` (Impact: 139.6)
  * `createCompoundArrayAccessCall` (Impact: 60.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 309`, `args: 95`, `func_start: 62`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 407`, `planned_debt: 2`, `duplicate_logic: 17`, `orphaned_logic: 15`
* *Architecture:* `api: 1`, `import: 83`
* *Defense:* `safety: 223`, `doc: 15`, `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` org.jetbrains.kotlin.fir.FirElement, org.jetbrains.kotlin.fir.scopes.impl.declaredMemberScope, org.jetbrains.kotlin.fir.realPsi, org.jetbrains.kotlin.types.Variance, org.jetbrains.kotlin.analysis.api.types.KaType, org.jetbrains.kotlin.idea.references.KtReference, org.jetbrains.kotlin.analysis.api.types.KaSubstitutor, org.jetbrains.kotlin.fir.symbols.impl.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/libbacktrace/c/dwarf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.991 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.249 IQR)
- **Top Global Matches:** file_cluster_8: 13.991, file_cluster_13: 14.198, file_cluster_0: 14.284
- **Magnitude:** 2784.9 | **LOC:** 4416 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.8603%), Tech Debt (20.8267%)
**Top Internal Functions/Classes:**
  * `build_address_map` (Impact: 635.5)
    * *Intent:* /* The name of the function. */
  * `read_function_entry` (Impact: 174.7)
  * `read_function_info` (Impact: 64.9)
  * `read_lnct` (Impact: 63.9)
  * `read_v2_paths` (Impact: 53.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 293`, `args: 17`, `func_start: 16`, `class_start: 70`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1187`, `fragile_debt: 4`, `orphaned_logic: 6`
* *Architecture:* `api: 297`, `import: 8`
* *Defense:* `safety: 23`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` errno.h, stdlib.h, types.h, backtrace.h, filenames.h, config.h, internal.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.925 IQR)
- **Top Global Matches:** file_cluster_11: 13.925, file_cluster_13: 13.942, file_cluster_0: 13.997
- **Magnitude:** 2646.62 | **LOC:** 5145 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.7892%), Tech Debt (33.5899%)
**Top Internal Functions/Classes:**
  * `visitFunctionInScope` (Impact: 537.2)
    * *Intent:* * 123, * $composer, * (0b110 and $dirty) or // 1st param has same state that our 1st param does * 0b...
  * `asSourceOrEarlyExitGroup` (Impact: 308.1)
  * `extractParamMetaFromScopes` (Impact: 154.2)
  * `isLambda` (Impact: 53.1)
  * `visitFunctionAccess` (Impact: 39.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 483`, `structural_boundaries: 289`, `args: 166`, `func_start: 125`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 603`, `dead_code: 26`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `api: 19`, `import: 45`
* *Defense:* `safety: 123`, `doc: 19`, `immutability_locks: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` org.jetbrains.kotlin.backend.common.lower.DeclarationIrBuilder, org.jetbrains.kotlin.ir.expressions.impl.*, org.jetbrains.kotlin.ir.builders.declarations.addValueParameter, org.jetbrains.kotlin.ir.expressions.*, org.jetbrains.kotlin.platform.konan.isNative, org.jetbrains.kotlin.ir.symbols.UnsafeDuringIrConstructionAPI, org.jetbrains.kotlin.ir.builders.irReturn, org.jetbrains.kotlin.descriptors.Modality...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinParsing.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.614 IQR)
- **Top Global Matches:** file_cluster_8: 9.614, file_cluster_7: 10.251, file_cluster_0: 10.318
- **Magnitude:** 2091.08 | **LOC:** 2820 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.98%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `parseContextParameterOrReceiverList` (Impact: 384.4)
  * `advance` (Impact: 345.4)
  * `parseTypeArgumentList` (Impact: 297.4)
  * `parsePropertyComponent` (Impact: 60.9)
    * *Intent:* * annotationList * : "@" (annotationUseSiteTarget ":")? "[" unescapedAnnotation+ "]" * ; * * annotat...
  * `parseMultiDeclarationEntry` (Impact: 53.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 143`, `args: 78`, `func_start: 238`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 8`, `duplicate_logic: 103`, `orphaned_logic: 21`
* *Architecture:* `api: 17`, `import: 14`
* *Defense:* `safety: 22`, `doc: 5`, `test: 16`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.intellij.psi.tree.TokenSet, java.util.function.Supplier, org.jetbrains.kotlin.lexer.KtTokens, org.jetbrains.kotlin.parsing.KotlinParsing.AnnotationParsingMode.*, org.jetbrains.kotlin.parsing.KotlinWhitespaceAndCommentsBindersKt.TRAILING_ALL_BINDER, org.jetbrains.kotlin.lexer.KtSingleValueToken, com.intellij.openapi.diagnostic.Logger, org.jetbrains.kotlin.parsing.KotlinWhitespaceAndCommentsBindersKt.PRECEDING_ALL_BINDER...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirDeclarationBuilder.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.068 IQR)
- **Top Global Matches:** file_cluster_13: 14.068, file_cluster_2: 14.182, file_cluster_11: 14.232
- **Magnitude:** 2065.94 | **LOC:** 2974 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.2942%), Tech Debt (9.017%)
**Top Internal Functions/Classes:**
  * `convertClass` (Impact: 450.2)
  * `convertFunctionDeclaration` (Impact: 99.0)
  * `convertGetterOrSetter` (Impact: 78.0)
  * `convertValueParameter` (Impact: 27.6)
  * `convertBlockExpressionWithoutBuilding` (Impact: 25.6)
    * *Intent:* /** * @see org.jetbrains.kotlin.parsing.KotlinParsing.parseBlockExpression */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 170`, `args: 115`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 885`, `planned_debt: 5`
* *Architecture:* `api: 7`, `import: 51`
* *Defense:* `safety: 48`, `doc: 78`, `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` org.jetbrains.kotlin.fir.types.*, org.jetbrains.kotlin.fir.lightTree.fir.modifier.TypeProjectionModifierList, org.jetbrains.kotlin.fir.symbols.FirBasedSymbol, org.jetbrains.kotlin.fir.lightTree.fir.modifier.ModifierList, org.jetbrains.kotlin.utils.addToStdlib.runIf, org.jetbrains.kotlin.descriptors.annotations.AnnotationUseSiteTarget, org.jetbrains.kotlin.descriptors.annotations.AnnotationUseSiteTarget.*, org.jetbrains.kotlin.fir.contracts.builder.buildRawContractDescription...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.47 IQR)
- **Top Global Matches:** file_cluster_13: 13.47, file_cluster_0: 13.561, file_cluster_11: 13.569
- **Magnitude:** 2024.42 | **LOC:** 2368 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.1746%), Tech Debt (56.0528%)
**Top Internal Functions/Classes:**
  * `transformQualifiedAccessExpression` (Impact: 666.9)
  * `tryResolveIndexedAccessAugmentedAssignme` (Impact: 110.9)
  * `transformSuperReceiver` (Impact: 49.9)
  * `transformAugmentedAssignment` (Impact: 43.5)
  * `withTypeArgumentsForBareType` (Impact: 39.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 273`, `args: 103`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 330`, `dead_code: 6`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `api: 46`, `import: 60`
* *Defense:* `safety: 143`, `doc: 8`, `test: 3`, `immutability_locks: 182`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` org.jetbrains.kotlin.fir.declarations.utils.isExternal, org.jetbrains.kotlin.fir.types.*, org.jetbrains.kotlin.fir.resolve.calls.findTypesForSuperCandidates, org.jetbrains.kotlin.types.TypeApproximatorConfiguration, org.jetbrains.kotlin.fir.resolve.calls.ConeResolutionAtom, org.jetbrains.kotlin.fir.resolve.calls.InaccessibleImplicitReceiverValue, org.jetbrains.kotlin.fir.expressions.impl.FirResolvedArgumentList, org.jetbrains.kotlin.fir.symbols.impl.FirCallableSymbol...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/DefaultErrorMessages.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.333 IQR)
- **Top Global Matches:** file_cluster_11: 14.333, file_cluster_8: 14.346, file_cluster_13: 14.39
- **Magnitude:** 1707.94 | **LOC:** 1343 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.5184%), Tech Debt (10.45%)
**Top Internal Functions/Classes:**
  * `getMap` (Impact: 15.8)
  * `adaptGenerics2` (Impact: 12.3)
  * `getRendererForDiagnostic` (Impact: 11.8)
  * `render` (Impact: 9.4)
  * `adaptGenerics1` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 271`, `args: 28`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 1614`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `import: 19`
* *Defense:* `safety: 16`, `doc: 1`, `test: 4`, `sync_locks: 3`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` org.jetbrains.kotlin.resolve.multiplatform.K1ExpectActualCompatibility.Incompatible, kotlin.Pair, org.jetbrains.kotlin.descriptors.MemberDescriptor, org.jetbrains.kotlin.diagnostics.rendering.RenderingContext.of, org.jetbrains.kotlin.diagnostics.rendering.Renderers.NAME, kotlin.collections.CollectionsKt, java.lang.reflect.Modifier, java.util.*...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirDataFlowAnalyzer.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.763 IQR)
- **Top Global Matches:** file_cluster_13: 12.763, file_cluster_0: 12.864, file_cluster_11: 12.875
- **Magnitude:** 1674.92 | **LOC:** 1931 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.0083%), Tech Debt (36.9367%)
**Top Internal Functions/Classes:**
  * `buildSmartCastStatement` (Impact: 595.4)
  * `processConditionalContract` (Impact: 116.5)
    * *Intent:* // expression == non-null const -> expression != null
  * `exitBooleanNot` (Impact: 86.7)
  * `mapElement` (Impact: 85.6)
  * `exitVariableInitialization` (Impact: 80.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 182`, `args: 102`, `func_start: 78`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 111`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 14`, `concurrency: 13`, `import: 33`
* *Defense:* `safety: 92`, `doc: 12`, `immutability_locks: 161`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` org.jetbrains.kotlin.fir.declarations.utils.lambdaArgumentParent, org.jetbrains.kotlin.fir.resolve.transformers.body.resolve.FirAbstractBodyResolveTransformer, org.jetbrains.kotlin.fir.resolve.calls.ImplicitValue, org.jetbrains.kotlin.fir.symbols.FirBasedSymbol, org.jetbrains.kotlin.fir.types.*, org.jetbrains.kotlin.types.SmartcastStability, org.jetbrains.kotlin.fir.declarations.impl.FirDefaultPropertyAccessor, org.jetbrains.kotlin.fir.symbols.impl.FirRegularClassSymbol...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirExpressionBuilder.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.024 IQR)
- **Top Global Matches:** file_cluster_13: 14.024, file_cluster_8: 14.143, file_cluster_11: 14.155
- **Magnitude:** 1648.74 | **LOC:** 1743 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.4267%), Tech Debt (16.4528%)
**Top Internal Functions/Classes:**
  * `convertQualifiedExpression` (Impact: 49.5)
  * `convertCallExpression` (Impact: 49.5)
  * `convertBinaryExpressionFallback` (Impact: 43.6)
  * `convertWhenExpression` (Impact: 40.9)
  * `wrapExpressionIfNeeded` (Impact: 33.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 175`, `args: 90`, `func_start: 50`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 865`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 6`, `import: 50`
* *Defense:* `safety: 45`, `doc: 97`, `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` org.jetbrains.kotlin.descriptors.EffectiveVisibility, org.jetbrains.kotlin.fir.declarations.FirReplSnippet, org.jetbrains.kotlin.fir.declarations.FirScript, org.jetbrains.kotlin.fir.references.buildErrorNamedReferenceWithNoName, org.jetbrains.kotlin.fir.symbols.impl.FirAnonymousFunctionSymbol, org.jetbrains.kotlin.fir.symbols.impl.FirLocalPropertySymbol, org.jetbrains.kotlin.fir.types.FirTypeRef, org.jetbrains.kotlin.utils.addToStdlib.runIf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiRawFirBuilder.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.865 IQR)
- **Top Global Matches:** file_cluster_13: 13.865, file_cluster_11: 13.932, file_cluster_0: 13.969
- **Magnitude:** 1640.8 | **LOC:** 3963 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.2172%), Tech Debt (30.2941%)
**Top Internal Functions/Classes:**
  * `toFirProperty` (Impact: 205.4)
  * `toFirValueParameter` (Impact: 34.9)
  * `visitCallExpression` (Impact: 30.1)
  * `toFirDeclaration` (Impact: 28.9)
  * `extractReplElements` (Impact: 26.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 208`, `args: 92`, `func_start: 68`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 773`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 6`
* *Architecture:* `api: 25`, `concurrency: 6`, `import: 54`
* *Defense:* `safety: 103`, `doc: 5`, `immutability_locks: 152`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` com.intellij.psi.PsiElement, org.jetbrains.kotlin.fir.symbols.FirBasedSymbol, org.jetbrains.kotlin.fir.references.buildErrorNamedReferenceWithNoName, org.jetbrains.kotlin.fir.types.*, org.jetbrains.kotlin.utils.addToStdlib.runIf, com.intellij.util.AstLoadingFilter, org.jetbrains.kotlin.descriptors.annotations.AnnotationUseSiteTarget.*, org.jetbrains.kotlin.fir.contracts.builder.buildRawContractDescription...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MethodInliner.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.639 IQR)
- **Top Global Matches:** file_cluster_13: 12.639, file_cluster_11: 12.756, file_cluster_8: 12.86
- **Magnitude:** 1640.76 | **LOC:** 1246 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (90.1058%)
**Top Internal Functions/Classes:**
  * `doInline` (Impact: 507.3)
  * `markPlacesForInlineAndRemoveInlinable` (Impact: 334.9)
  * `preprocessNodeBeforeInline` (Impact: 194.0)
  * `prepareNode` (Impact: 67.1)
  * `transformCaptured` (Impact: 34.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 106`, `args: 44`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 193`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 2`, `import: 32`
* *Defense:* `safety: 30`, `test: 6`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` org.jetbrains.kotlin.codegen.optimization.common.isMeaningful, org.jetbrains.kotlin.codegen.inline.coroutines.markNoinlineLambdaIfSuspend, org.jetbrains.org.objectweb.asm.commons.MethodRemapper, org.jetbrains.kotlin.codegen.inline.coroutines.surroundInvokesWithSuspendMarkersIfNeeded, org.jetbrains.kotlin.codegen.optimization.ApiVersionCallsPreprocessingMethodTransformer, org.jetbrains.org.objectweb.asm.Label, org.jetbrains.org.objectweb.asm.commons.InstructionAdapter, org.jetbrains.org.objectweb.asm.tree.analysis.Frame...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/analysis/ComposableTargetCheckerTests.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_2` (Drift: 9.837 IQR)
- **Top Global Matches:** file_cluster_2: 9.837, file_cluster_0: 9.898, file_cluster_8: 9.9
- **Magnitude:** 1633.18 | **LOC:** 573 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.0026%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 147`, `args: 98`, `func_start: 98`, `class_start: 14`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 31`
* *Defense:* `safety: 18`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` androidx.compose.foundation.text.BasicText, org.junit.Test, androidx.compose.runtime.Composable, androidx.compose.compiler.plugins.kotlin.Classpath, androidx.compose.compiler.plugins.kotlin.AbstractComposeDiagnosticsTest, androidx.compose.runtime.ComposableTarget, androidx.compose.runtime.ComposableTargetMarker, androidx.compose.runtime.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PositioningStrategies.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.234 IQR)
- **Top Global Matches:** file_cluster_0: 13.234, file_cluster_11: 13.311, file_cluster_16: 13.349
- **Magnitude:** 1632.48 | **LOC:** 1297 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.1143%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `mark` (Impact: 503.1)
  * `mark` (Impact: 64.3)
  * `mark` (Impact: 49.9)
  * `mark` (Impact: 37.5)
  * `mark` (Impact: 33.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 357`, `args: 111`, `func_start: 91`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 37`, `planned_debt: 1`, `duplicate_logic: 82`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 228`, `doc: 2`, `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.intellij.psi.tree.TokenSet, com.intellij.lang.ASTNode, org.jetbrains.kotlin.lexer.KtTokens, org.jetbrains.kotlin.psi.*, org.jetbrains.kotlin.psi.psiUtil.*, org.jetbrains.kotlin.utils.sure, org.jetbrains.kotlin.utils.addToStdlib.firstIsInstanceOrNull, org.jetbrains.kotlin.utils.addToStdlib.UnsafeCastFunction...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrorsDefaultMessages.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.18 IQR)
- **Top Global Matches:** file_cluster_13: 14.18, file_cluster_8: 14.658, file_cluster_0: 14.742
- **Magnitude:** 1629.02 | **LOC:** 3934 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.4868%), Tech Debt (8.761%)
**Top Internal Functions/Classes:**
  * `compute` (Impact: 10.8)
  * `render` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 1124`, `args: 5`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 130`, `state_mutation: 1400`, `planned_debt: 5`, `orphaned_logic: 1`
* *Architecture:* `api: 13`, `concurrency: 120`, `import: 934`
* *Defense:* `safety: 293`, `doc: 3`, `test: 4`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.jetbrains.kotlin.fir.analysis.diagnostics.FirErrors.PACKAGE_CONFLICTS_WITH_CLASSIFIER, org.jetbrains.kotlin.fir.analysis.diagnostics.FirErrors.INCOMPATIBLE_CLASS, org.jetbrains.kotlin.fir.analysis.diagnostics.FirErrors.FUNCTION_DECLARATION_WITH_NO_NAME, org.jetbrains.kotlin.fir.analysis.diagnostics.FirErrors.SUPER_CALL_FROM_PUBLIC_INLINE, org.jetbrains.kotlin.fir.analysis.diagnostics.FirErrors.CONSTRUCTOR_OR_SUPERTYPE_ON_TYPEALIAS_WITH_TYPE_PROJECTION, org.jetbrains.kotlin.fir.analysis.diagnostics.FirErrors.ACTUAL_TYPE_ALIAS_TO_NULLABLE_TYPE, org.jetbrains.kotlin.fir.analysis.diagnostics.FirErrors.DATA_CLASS_WITHOUT_PARAMETERS, org.jetbrains.kotlin.fir.analysis.diagnostics.FirErrors.INAPPLICABLE_ALL_TARGET_IN_MULTI_ANNOTATION...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/libbacktrace/c/elf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.115 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.778 IQR)
- **Top Global Matches:** file_cluster_8: 14.115, file_cluster_13: 14.27, file_cluster_0: 14.39
- **Magnitude:** 1621.02 | **LOC:** 4920 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.0425%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `elf_uncompress_lzma` (Impact: 166.8)
    * *Intent:* bits per entry. */ /* Number of entries we allocate to for one code table. We get a page for the two...
  * `elf_zlib_fetch` (Impact: 158.9)
    * *Intent:* unsigned char e_ident[EI_NIDENT]; /* ELF "magic number" */ b_elf_half e_type; /* Identifies object f...
  * `elf_zlib_inflate_table` (Impact: 107.4)
  * `backtrace_initialize` (Impact: 39.7)
  * `elf_uncompress_zdebug` (Impact: 29.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 77`, `args: 12`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 887`
* *Architecture:* `io: 1`, `api: 165`, `import: 11`
* *Defense:* `safety: 43`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` errno.h, unistd.h, stdlib.h, types.h, backtrace.h, stdio.h, stat.h, config.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/libbacktrace/c/macho.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.287 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.768 IQR)
- **Top Global Matches:** file_cluster_8: 13.287, file_cluster_13: 13.481, file_cluster_0: 13.615
- **Magnitude:** 1576.86 | **LOC:** 1379 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.241%), Tech Debt (10.4233%)
**Top Internal Functions/Classes:**
  * `macho_add_dsym` (Impact: 339.3)
  * `macho_add_symtab` (Impact: 132.2)
  * `backtrace_initialize` (Impact: 67.7)
  * `macho_add_fat` (Impact: 66.9)
  * `macho_add_dwarf_segment` (Impact: 53.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 139`, `args: 14`, `func_start: 12`, `class_start: 47`
* *Risk/State:* `state_mutation: 514`, `fragile_debt: 2`
* *Architecture:* `api: 290`, `import: 8`
* *Defense:* `safety: 13`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` stdlib.h, types.h, backtrace.h, dirent.h, dyld.h, config.h, internal.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libraries/stdlib/src/kotlin/time/Duration.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.693 IQR)
- **Top Global Matches:** file_cluster_0: 12.693, file_cluster_8: 13.047, file_cluster_7: 13.195
- **Magnitude:** 1508.36 | **LOC:** 1629 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2323%), Tech Debt (87.6534%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 500.2)
    * *Intent:* * If a duration-returning operation provided in `kotlin.time` produces a duration value that doesn't...
  * `parseDefaultStringFormat` (Impact: 90.8)
    * *Intent:* /** * Parses default duration format (e.g., `"1h 30m"`, `"45s"`, `"500ms"`). * Note: While `"Infinit...
  * `parseIsoStringFormat` (Impact: 81.8)
    * *Intent:* /** * Parses ISO-8601 duration format (e.g., `"PT1H30M45S"`). * * @param value the full input string...
  * `isInMillis` (Impact: 70.7)
  * `times` (Impact: 50.0)
    * *Intent:* /** * Returns a duration whose value is this duration value multiplied by the given [scale] number. ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 152`, `args: 79`, `func_start: 66`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 167`, `planned_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 121`, `import: 3`
* *Defense:* `safety: 157`, `doc: 154`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` kotlin.math.*, kotlin.contracts.*, kotlin.jvm.JvmInline
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/KotlinParsing.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.777 IQR)
- **Top Global Matches:** file_cluster_8: 11.777, file_cluster_13: 11.822, file_cluster_2: 12.045
- **Magnitude:** 1452.26 | **LOC:** 2922 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.11%), Tech Debt (55.5886%)
**Top Internal Functions/Classes:**
  * `parseContextParameterOrReceiverList` (Impact: 440.8)
  * `doParseModifierListBody` (Impact: 63.3)
  * `parsePropertyComponent` (Impact: 60.2)
    * *Intent:* * : "@" (annotationUseSiteTarget ":")? unescapedAnnotation * ; * * annotationList * : "@" (annotatio...
  * `parseMultiDeclarationEntry` (Impact: 51.3)
  * `parseTypeRefContents` (Impact: 49.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 167`, `args: 70`, `func_start: 66`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 171`, `dead_code: 5`, `duplicate_logic: 14`
* *Architecture:* `api: 18`, `import: 27`
* *Defense:* `safety: 39`, `doc: 5`, `immutability_locks: 147`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.jetbrains.kotlin.kmp.lexer.KtTokens.TRY_KEYWORD, com.intellij.platform.syntax.syntaxElementTypeSetOf, org.jetbrains.kotlin.kmp.lexer.KtTokens.THIS_KEYWORD, org.jetbrains.kotlin.kmp.lexer.KtTokens.WHILE_KEYWORD, org.jetbrains.kotlin.kmp.lexer.KtTokens.DO_KEYWORD, org.jetbrains.kotlin.kmp.lexer.KtTokens, org.jetbrains.kotlin.kmp.lexer.KtTokens.CONTRACT_MODIFIER, org.jetbrains.kotlin.kmp.parser.KtNodeTypes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/js.ast/src/org/jetbrains/kotlin/js/backend/JsToStringGenerationVisitor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.882 IQR)
- **Top Global Matches:** file_cluster_8: 10.882, file_cluster_0: 11.068, file_cluster_7: 11.45
- **Magnitude:** 1437.68 | **LOC:** 2044 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.977%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visitObjectLiteral` (Impact: 56.6)
  * `printJsBlock` (Impact: 48.7)
  * `visitImport` (Impact: 45.1)
  * `visitDocComment` (Impact: 42.5)
  * `visitExport` (Impact: 36.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 167`, `args: 117`, `func_start: 520`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 22`, `dead_code: 1`, `duplicate_logic: 126`
* *Architecture:* `api: 125`, `import: 8`
* *Defense:* `safety: 113`, `doc: 8`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.jetbrains.kotlin.js.backend.ast.*, it.unimi.dsi.fastutil.objects.ObjectOpenHashSet, org.jetbrains.kotlin.js.util.TextOutput, org.jetbrains.kotlin.js.backend.ast.JsVars.JsVar, java.util.*, org.jetbrains.annotations.NotNull, org.jetbrains.annotations.Nullable, org.jetbrains.kotlin.js.common.IdentifierPolicyKt...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/IrToBitcode.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.34 IQR)
- **Top Global Matches:** file_cluster_8: 12.34, file_cluster_11: 12.536, file_cluster_13: 12.547
- **Magnitude:** 1385.84 | **LOC:** 2960 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.919%), Tech Debt (96.8479%)
**Top Internal Functions/Classes:**
  * `overrideRuntimeGlobals` (Impact: 57.4)
  * `evaluateConstantValueImpl` (Impact: 48.7)
    * *Intent:* //-------------------------------------------------------------------------//
  * `visitSimpleFunction` (Impact: 37.2)
  * `call` (Impact: 37.1)
  * `genHandler` (Impact: 27.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 462`, `structural_boundaries: 354`, `args: 195`, `func_start: 166`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 76`, `state_mutation: 174`, `dead_code: 1`, `planned_debt: 16`, `fragile_debt: 4`, `duplicate_logic: 20`, `orphaned_logic: 13`
* *Architecture:* `io: 4`, `api: 1`, `import: 35`
* *Defense:* `safety: 135`, `doc: 16`, `test: 11`, `sync_locks: 1`, `immutability_locks: 278`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` org.jetbrains.kotlin.backend.common.lower.coroutines.getOrCreateFunctionWithContinuationStub, org.jetbrains.kotlin.ir.visitors.IrVisitorVoid, org.jetbrains.kotlin.backend.konan.ir.*, org.jetbrains.kotlin.konan.target.Family, org.jetbrains.kotlin.ir.util.isNullable, org.jetbrains.kotlin.descriptors.Modality, org.jetbrains.kotlin.backend.konan.llvm.objc.processBindClassToObjCNameAnnotations, org.jetbrains.kotlin.ir.objcinterop.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/gc/common/cpp/TracingGCTest.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.207 IQR)
- **Local Micro-Species:** `Cluster 2: Verification & Unit Testing` (Drift: 5.182 IQR)
- **Top Global Matches:** file_cluster_4: 14.207, file_cluster_8: 14.213, file_cluster_13: 14.345
- **Magnitude:** 1380.14 | **LOC:** 1370 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.1752%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `TYPED_TEST_P` (Impact: 27.5)
  * `TYPED_TEST_P` (Impact: 25.8)
  * `TYPED_TEST_P` (Impact: 20.8)
  * `TYPED_TEST_P` (Impact: 20.6)
  * `TYPED_TEST_P` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 206`, `args: 128`, `func_start: 58`, `class_start: 10`
* *Risk/State:* `state_mutation: 998`, `planned_debt: 2`, `duplicate_logic: 47`
* *Architecture:* `api: 8`, `concurrency: 78`, `import: 18`
* *Defense:* `safety: 23`, `test: 155`, `sync_locks: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` AllocatorTestSupport.hpp, SingleThreadExecutor.hpp, thread, condition_variable, SafePoint.hpp, mutex, ExtraObjectData.hpp, FinalizerHooksTestSupport.hpp...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kotlin-native/runtime/src/main/cpp/dtoa/cbigint.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.091 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.249 IQR)
- **Top Global Matches:** file_cluster_8: 14.091, file_cluster_12: 14.381, file_cluster_11: 14.492
- **Magnitude:** 1321.26 | **LOC:** 905 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (33.5583%)
**Top Internal Functions/Classes:**
  * `timesTenToTheEHighPrecision` (Impact: 68.1)
  * `toDoubleHighPrecision` (Impact: 65.9)
  * `highestSetBit` (Impact: 50.5)
  * `lowestSetBit` (Impact: 50.5)
  * `addHighPrecision` (Impact: 35.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 46`, `args: 41`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 839`, `orphaned_logic: 13`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cbigint.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/main/cpp/ClockTest.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.344 IQR)
- **Local Micro-Species:** `Cluster 2: Verification & Unit Testing` (Drift: 5.862 IQR)
- **Top Global Matches:** file_cluster_4: 13.344, file_cluster_8: 13.711, file_cluster_13: 13.869
- **Magnitude:** 1278.46 | **LOC:** 1162 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `durationName` (Impact: 36.9)
  * `ManualClockTest` (Impact: 20.3)
  * `ManualClockTest` (Impact: 8.1)
    * *Intent:* // Nothing pending anymore.
  * `GetName` (Impact: 7.6)
  * `clockName` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 295`, `args: 154`, `func_start: 85`, `class_start: 6`
* *Risk/State:* `state_mutation: 641`, `duplicate_logic: 82`
* *Architecture:* `api: 4`, `concurrency: 294`, `import: 13`
* *Defense:* `safety: 39`, `test: 132`, `sync_locks: 39`, `immutability_locks: 84`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tuple, shared_mutex, condition_variable, mutex, ClockTestSupport.hpp, ScopedThread.hpp, TestSupport.hpp, type_traits...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/bodies/KaVariableInitializerRenderer.kt` (KOTLIN) | Magnitude: 15.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 15, import: 7, decorators: 5
- `compiler/testData/asJava/lightClasses/lightClassByPsi/propertyAnnotations.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 18, immutability_locks: 15, indent_spaces: 14, encapsulation: 6
- `compiler/testData/diagnostics/tests/multiplatform/directJavaActualization/directJavaActualization_javaStatics.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, decorators: 3, indent_spaces: 3
- `compiler/testData/diagnostics/tests/multiplatform/directJavaActualization/directJavaActualization_javaStatics.ll.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, decorators: 3, indent_spaces: 3
- `libraries/stdlib/src/kotlin/coroutines/CoroutinesH.kt` (KOTLIN) | Magnitude: 32.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 7, generics: 5, structural_boundaries: 4, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/moduleData.kt` (KOTLIN) | Magnitude: 233.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 250, branch: 80, immutability_locks: 51, state_mutation: 43
- `compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/OptimisedWhenGenerator.kt` (KOTLIN) | Magnitude: 257.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, state_mutation: 84, branch: 64, immutability_locks: 43
- `compiler/testData/diagnostics/tests/controlStructures/ifWhenWithoutElse.fir.kt` (KOTLIN) | Magnitude: 0.11 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 58, args: 42, state_mutation: 42, immutability_locks: 27
- `compiler/testData/diagnostics/tests/controlStructures/ifWhenWithoutElse.kt` (KOTLIN) | Magnitude: 0.11 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 58, args: 42, state_mutation: 42, immutability_locks: 27
- `libraries/stdlib/wasm/src/kotlin/math/fdlibm/e_fmod.kt` (KOTLIN) | Magnitude: 289.8 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 193, indent_spaces: 140, branch: 48, bitwise_ops: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `js/js.translator/testData/incremental/invalidation/jsCodeWithConstStringFromOtherModule/lib2/inlineFunction.0.6.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, structural_boundaries: 2, branch: 1, args: 1
- `js/js.translator/testData/incremental/invalidation/jsCodeWithConstStringFromOtherModuleWithIntraModuleInliner/lib2/inlineFunction.0.6.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, structural_boundaries: 2, branch: 1, args: 1
- `core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/structure/reflectClassUtil.kt` (KOTLIN) | Magnitude: 16.24 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 43, indent_spaces: 43, reflection_metaprogramming: 32, branch: 17
- `js/js.translator/testData/box/esModules/jsModule/externalClass.mjs` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 4, structural_boundaries: 3, args: 3, func_start: 3
- `compiler/fir/analysis-tests/testData/resolve/inlineClasses/inlineClassConstructor.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 17, reflection_metaprogramming: 16, immutability_locks: 13, generics: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsIrProgramFragment.kt` (KOTLIN) | Magnitude: 228.72 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 229, immutability_locks: 84, structural_boundaries: 67, state_mutation: 54
- `generators/tests/org/jetbrains/kotlin/generators/arguments/DefaultValues.kt` (KOTLIN) | Magnitude: 57.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 39, generics: 39, structural_boundaries: 34
- `compiler/testData/compileJavaAgainstKotlin/method/MapOfKString.java` (JAVA) | Magnitude: 0.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 7, scientific: 4, indent_spaces: 4, generics: 3
- `analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaLocalVariableSymbolRenderer.kt` (KOTLIN) | Magnitude: 19.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 12, import: 7, api: 3
- `analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/K2IdeBuiltiInSupport.kt` (KOTLIN) | Magnitude: 25.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 17, args: 6, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `js/js.translator/testData/box/esModules/jsModule/externalConstructor.mjs` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, branch: 1, structural_boundaries: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `compiler/build-tools/kotlin-build-tools-compat/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/compat/arguments/argumentUtils.kt` (KOTLIN) | Magnitude: 17.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, generics: 12, indent_spaces: 9, api: 6
- `compiler/config/configuration-keys-generator/src/org/jetbrains/kotlin/config/keys/generator/model/KeysContainer.kt` (KOTLIN) | Magnitude: 53.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 147, immutability_locks: 58, structural_boundaries: 29, generics: 28
- `compiler/fir/analysis-tests/testData/resolve/checkers/notUselessCast_2.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, generics: 7, args: 5
- `compiler/fir/analysis-tests/testData/resolve/innerClasses/inCallableReferenceLHS/withPackage.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, generics: 7, args: 3
- `compiler/fir/analysis-tests/testData/resolve/innerClasses/inCallableReferenceLHS/withPackage.latestLV.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, generics: 7, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/visibility.kt` (KOTLIN) | Magnitude: 37.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 10, branch: 9, state_mutation: 6
- `plugins/kotlin-dataframe/testData/box/groupBy_min.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, explicit_casts: 20, immutability_locks: 18, scientific: 11
- `libraries/tools/abi-comparator/comparator.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: safety_bypasses: 10, args: 4, state_mutation: 4, io: 2
- `libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/NonSynchronizedMetricsContainer.kt` (KOTLIN) | Magnitude: 0.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 16, generics: 11, branch: 8
- `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirKeywordUtils.kt` (KOTLIN) | Magnitude: 20.66 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, ui_framework: 54, structural_boundaries: 38, immutability_locks: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ControlFlowTransformTestsNoSource.kt` (KOTLIN) | Magnitude: 37.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 197, structural_boundaries: 60, decorators: 43, ui_framework: 40
- `compiler/testData/diagnostics/tests/delegatedProperty/inference/successfulProvideDelegateLeadsToRedGetValue.fir.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: generics: 6, structural_boundaries: 4, ui_framework: 3, planned_debt: 3
- `compiler/testData/diagnostics/tests/delegatedProperty/inference/successfulProvideDelegateLeadsToRedGetValue.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: generics: 6, structural_boundaries: 4, ui_framework: 3, planned_debt: 3
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/AndroidDaggerProject/app/src/main/java/com/example/dagger/kotlin/DemoActivity.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, ui_framework: 2, import: 2
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/android-dagger/app/src/main/java/com/example/dagger/kotlin/DemoActivity.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, ui_framework: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `compiler/psi/psi-impl/testData/psi/annotation/functionalTypes/withoutParentheses/withParameter.kt` (KOTLIN) | Magnitude: 0.05 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 38, concurrency: 27, structural_boundaries: 12, args: 11
- `js/js.translator/testData/box/vararg/jsExternalVarargSuspend.kt` (KOTLIN) | Magnitude: 0.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 62, structural_boundaries: 37, branch: 19
- `js/js.translator/testData/box/esModules/main/suspendMainThrows.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, concurrency: 6, branch: 5, structural_boundaries: 5
- `js/js.translator/testData/box/main/suspendMainThrows.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, concurrency: 6, branch: 5, structural_boundaries: 5
- `kotlin-native/runtime/src/gc/common/cpp/TracingGCTest.hpp` (CPP) | Magnitude: 1380.14 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 998, indent_spaces: 953, structural_boundaries: 206, test: 155

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `compiler/testData/diagnostics/tests/crvFull/localOverrides.fir.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 12, planned_debt: 10, args: 8
- `libraries/tools/kotlin-gradle-plugin/build.gradle.kts` (KOTLIN) | Magnitude: 6.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 425, state_mutation: 44, immutability_locks: 26, branch: 24
- `compiler/testData/diagnostics/tests/targetedBuiltIns/backwardCompatibility/basic.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 8, planned_debt: 5, indent_spaces: 5, args: 3
- `compiler/testData/ir/interpreter/helpers/Regex.kt` (KOTLIN) | Magnitude: 0.03 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 34, api: 25, structural_boundaries: 23, planned_debt: 21
- `compiler/testData/diagnostics/tests/smartCasts/kt32358_3.fir.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, planned_debt: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `compiler/psi/psi-impl/testData/psi/kdoc/StartCodeBlockAfterTwoOrMoreLineBreaks.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1, class_start: 1
- `analysis/analysis-api/testData/components/resolver/singleByPsi/kDoc/blockTags/allTagSectionsRequiringSubjects.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1, args: 1, func_start: 1
- `libraries/kotlin.test/js/src/main/kotlin/kotlin/test/FrameworkAdapter.kt` (KOTLIN) | Magnitude: 22.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 4, api: 3, args: 2
- `libraries/kotlin.test/wasm/src/main/kotlin/kotlin/test/FrameworkAdapter.kt` (KOTLIN) | Magnitude: 22.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 4, api: 3, args: 2
- `native/swift/sir-printer/testData/commented_class.golden.swift` (SWIFT) | Magnitude: 0.01 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 1, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `compiler/fir/analysis-tests/testData/resolve/contextParameters/explicit/genericOverloads.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 38, generics: 34, args: 31, func_start: 30
- `compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/Other.kt` (KOTLIN) | Magnitude: 36.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, immutability_locks: 29, structural_boundaries: 17, state_mutation: 8
- `compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/SpecialBridge.kt` (KOTLIN) | Magnitude: 14.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, import: 5, immutability_locks: 2, indent_spaces: 2
- `compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/TypeGenerator.kt` (KOTLIN) | Magnitude: 88.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 56, immutability_locks: 24, structural_boundaries: 19
- `compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/symbols/impl/IrFakeOverrideSymbol.kt` (KOTLIN) | Magnitude: 4.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 17, import: 11, immutability_locks: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `kotlin-native/tools/compiler-cache-invalidator/build.gradle.kts` (KOTLIN) | Magnitude: 1.63 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, state_mutation: 1, dead_code: 1
- `native/commonizer/testData/propertyCommonization/setters/original/jvm/package_root.kt` (KOTLIN) | Magnitude: 0.03 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 13, indent_spaces: 8, api: 4, encapsulation: 3
- `analysis/analysis-api/testData/components/scopeProvider/combinedDeclaredMemberScope/enumClassWithFinalMembers.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, immutability_locks: 2, args: 1
- `analysis/analysis-api/testData/components/scopeProvider/declaredMemberScope/enumClassWithFinalMembers.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, immutability_locks: 2, args: 1
- `analysis/analysis-api/testData/components/scopeProvider/memberScope/enumClassWithFinalMembers.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, immutability_locks: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/internal/wrappers/KotlinWrapperPre2_4_0.kt` -> Churn: **100.0%** | Cog Load: 15.6643% | Debt: 98.6623%
- `compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/arguments/CompilerArgumentValueAdapter.kt` -> Churn: **100.0%** | Cog Load: 18.3952% | Debt: 99.8839%
- `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirCallCompletionResultsWriterTransformer.kt` -> Churn: **94.64%** | Cog Load: 45.7921% | Debt: 95.877%
- `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/main/main.kt` -> Churn: **88.56%** | Cog Load: 23.8237% | Debt: 76.1462%
- `compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/BtaCompilerArgument.kt` -> Churn: **81.55%** | Cog Load: 53.0491% | Debt: 74.4868%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt` -> **Denis.Zharkov** (100.0% isolated ownership) | Magnitude: 3247.14
- `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt` -> **Derek Xu** (100.0% isolated ownership) | Magnitude: 2646.62
- `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt` -> **Denis.Zharkov** (100.0% isolated ownership) | Magnitude: 2024.42
- `compiler/arguments/src/org/jetbrains/kotlin/arguments/description/JvmCompilerArguments.kt` -> **Iveta Kovalenko** (100.0% isolated ownership) | Magnitude: 1028.6
- `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/IrSourcePrinter.kt` -> **Derek Xu** (100.0% isolated ownership) | Magnitude: 978.88

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/nodejs/NodeJsExec.kt` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/nodejs/WasmNodeJsRootPlugin.kt` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/Project.kt` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 97.7062%)
- `compiler/frontend/src/org/jetbrains/kotlin/resolve/DeclarationResolver.kt` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 21.146%)
- `compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/extensions/IrGenerationExtension.kt` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 97.5348%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/compiler.common/src/org/jetbrains/kotlin/name/Name.java` -> **Severity: 469.473** (Blast Radius: 4.74 * Doc Risk: 99.045%)
- `compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt` -> **Severity: 316.045** (Blast Radius: 6.984 * Doc Risk: 45.2527%)
- `analysis/symbol-light-classes/testData/additionalFiles/NotNull.java` -> **Severity: 169.498** (Blast Radius: 8.08 * Doc Risk: 20.9775%)
- `analysis/symbol-light-classes/testData/additionalFiles/Nullable.java` -> **Severity: 85.251** (Blast Radius: 4.429 * Doc Risk: 19.2484%)
- `compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/ExecutionPolicy.kt` -> **Severity: 83.9** (Blast Radius: 0.839 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
