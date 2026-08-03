# ARCHITECTURAL_BRIEF: kotlin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/kotlin` |
| **Timestamp** | `2026-08-03T21:02:45.746461+00:00` |
| **Scan Duration** | `152.98s` |
| **Git Branch** | `master` |
| **Git Commit** | `bcdc78880f23dd07f10607332e8a89a5e72d4e9a` |
| **Git Remote** | `https://github.com/JetBrains/kotlin` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 51718 malicious artifacts.

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
> **Architectural Drift Z-Score:** `3.984`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 39595 | 47.4% |
| file_cluster_13 | 6076 | 7.3% |
| file_cluster_16 | 4535 | 5.4% |
| file_cluster_0 | 1550 | 1.9% |
| file_cluster_9 | 176 | 0.2% |
| file_cluster_2 | 117 | 0.1% |
| file_cluster_4 | 58 | 0.1% |
| file_cluster_17 | 56 | 0.1% |
| file_cluster_11 | 41 | 0.0% |
| file_cluster_6 | 34 | 0.0% |
| file_cluster_12 | 29 | 0.0% |
| file_cluster_7 | 5 | 0.0% |
| file_cluster_15 | 4 | 0.0% |

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
| Cognitive Load Exposure | 0.0 | 100.0 | 15.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 13.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.7 | 0.7 | 0.0 |
| API Exposure | 0.0 | 19.1 | 1.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 69.1 | 80.0 | 100.0 |
| Instability Exposure | 0.0 | 23.1 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.0 | 26.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
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

- `transformQualifiedAccessExpression` (@ `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt`) -> Impact: **4333.9** | LOC: 1114
- `toKaSymbolResolutionAttempt` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt`) -> Impact: **3848.2** | LOC: 1083
- `doInline` (@ `compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MethodInliner.kt`) -> Impact: **3592.9** | LOC: 740
- `mark` (@ `compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PositioningStrategies.kt`) -> Impact: **3323.1** | LOC: 661
- `compileImpl` (@ `compiler/daemon/src/org/jetbrains/kotlin/daemon/CompileServiceImpl.kt`) -> Impact: **3251.8** | LOC: 683
- `parseContextParameterOrReceiverList` (@ `compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/KotlinParsing.kt`) -> Impact: **2840.8** | LOC: 815
- `constructor` (@ `libraries/stdlib/src/kotlin/time/Duration.kt`) -> Impact: **2507.5** | LOC: 925
  * *Intent:* * If a duration-returning operation provided in `kotlin.time` produces a duration value that doesn't fit into the above range, * the returned `Duratio...
- `parseContextParameterOrReceiverList` (@ `compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinParsing.java`) -> Impact: **2450.5** | LOC: 800
- `resultIsActuallyAny` (@ `compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/ExpressionCodegen.kt`) -> Impact: **2291.1** | LOC: 742
- `build_address_map` (@ `kotlin-native/runtime/src/libbacktrace/c/dwarf.c`) -> Impact: **2113.9** | LOC: 883
  * *Intent:* /* The name of the function. */

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `computeExpectedType` (@ `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ExpressionTypeProvider.kt`) -> **O(2^N) [Recursive]**
- `createSignature` (@ `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10Resolver.kt`) -> **O(2^N) [Recursive]**
- `getFakeContainingKtModule` (@ `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolRelationProvider.kt`) -> **O(2^N) [Recursive]**
- `calculateCallableId` (@ `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/base/fe10DescUtils.kt`) -> **O(2^N) [Recursive]**
- `renderType` (@ `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/KaFe10DebugTypeRenderer.kt`) -> **O(2^N) [Recursive]**
- `buildKtType` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaSymbolByFirBuilder.kt`) -> **O(2^N) [Recursive]**
- `buildValueParameterSymbol` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaSymbolByFirBuilder.kt`) -> **O(2^N) [Recursive]**
- `buildNamedFunctionSymbol` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaSymbolByFirBuilder.kt`) -> **O(2^N) [Recursive]**
- `buildContextParameterSymbol` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaSymbolByFirBuilder.kt`) -> **O(2^N) [Recursive]**
- `doesParentUseChild` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirExpressionInformationProvider.kt`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `singletonInitialize` (@ `kotlin-native/performance/startup/src/commonMain/kotlin/org/jetbrains/startup/SingletonInitBenchmark.kt`) -> DB Complexity: **502**
- `convertClass` (@ `compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirDeclarationBuilder.kt`) -> DB Complexity: **303**
- `native_path_[Truncated]` (@ `libraries/tools/kotlin-maven-plugin-test/src/test/resources/maven-wrapper/mvnw`) -> DB Complexity: **283**
  * *Intent:* # OS specific support.
- `toKaSymbolResolutionAttempt` (@ `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt`) -> DB Complexity: **201**
- `toFirProperty` (@ `compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiRawFirBuilder.kt`) -> DB Complexity: **191**
- `build_address_map` (@ `kotlin-native/runtime/src/libbacktrace/c/dwarf.c`) -> DB Complexity: **175**
  * *Intent:* /* The name of the function. */
- `visitFunctionInScope` (@ `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt`) -> DB Complexity: **166**
  * *Intent:* * 123, * $composer, * (0b110 and $dirty) or // 1st param has same state that our 1st param does * 0b11000 // 2nd parameter is "static" * ) * } * * Rec...
- `Anonymous_Block_[Truncated]` (@ `kotlin-native/tools/scripts/update_apple_frameworks.sh`) -> DB Complexity: **166**
- `functionClassName` (@ `compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/descriptors/IrDescriptorBasedFunctionFactory.kt`) -> DB Complexity: **144**
- `configure` (@ `compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/ImplementationConfigurator.kt`) -> DB Complexity: **137**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/proto` | 171 | 45268.8 | 7.49% | 45.78% |
| `compiler/frontend/src/org/jetbrains/kotlin/resolve` | 89 | 24364.77 | 21.64% | 37.69% |
| `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration` | 132 | 20595.88 | 73.69% | 71.68% |
| `compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower` | 90 | 18205.6 | 56.9% | 34.59% |
| `compiler/psi/psi-api/src/org/jetbrains/kotlin/psi` | 195 | 17876.43 | 11.69% | 57.09% |
| `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower` | 29 | 16385.7 | 48.5% | 29.32% |
| `kotlin-native/runtime/src/main/cpp` | 131 | 16048.5 | 47.3% | 69.04% |
| `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components` | 32 | 13932.04 | 25.25% | 48.98% |
| `compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower` | 65 | 13755.42 | 68.29% | 43.67% |
| `compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower` | 44 | 12252.98 | 48.99% | 36.67% |

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
- `compiler/testData/diagnostics/tests/overload/noConflictingOverloadsWithDeprecatedHidden/FunctionsInMemberScope.latestLV.kt` -> **0** Orphaned Functions | **250** Duplicates
- `compiler/testData/diagnostics/tests/overload/noConflictingOverloadsWithDeprecatedHidden/FunctionsInMemberScope.ll.kt` -> **0** Orphaned Functions | **250** Duplicates
- `compiler/testData/diagnostics/tests/overload/noConflictingOverloadsWithDeprecatedHidden/FunctionsInPackage.latestLV.kt` -> **0** Orphaned Functions | **250** Duplicates
- `compiler/testData/diagnostics/tests/overload/noConflictingOverloadsWithDeprecatedHidden/FunctionsInPackage.ll.kt` -> **0** Orphaned Functions | **250** Duplicates
- `compiler/testData/diagnostics/tests/overload/noConflictingOverloadsWithDeprecatedHidden/FunctionsOnTopLevel.latestLV.kt` -> **0** Orphaned Functions | **250** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/CliFe10AnalysisFacade.kt`** -> AI Confidence: **99.48%**
2. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/Fe10AnalysisFacade.kt`** -> AI Confidence: **99.48%**
3. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/KaFe10SessionProvider.kt`** -> AI Confidence: **99.48%**
4. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/KotlinFe10CompilerPluginsProvider.kt`** -> AI Confidence: **99.48%**
5. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/annotations/KaFe10AnnotationsList.kt`** -> AI Confidence: **99.48%**
6. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10CompilerFacility.kt`** -> AI Confidence: **99.48%**
7. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10CompletionCandidateChecker.kt`** -> AI Confidence: **99.48%**
8. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10DataFlowProvider.kt`** -> AI Confidence: **99.48%**
9. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10DiagnosticProvider.kt`** -> AI Confidence: **99.48%**
10. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10Evaluator.kt`** -> AI Confidence: **99.48%**
11. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ExpressionInformationProvider.kt`** -> AI Confidence: **99.48%**
12. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ExpressionTypeProvider.kt`** -> AI Confidence: **99.48%**
13. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10JavaInteroperabilityComponent.kt`** -> AI Confidence: **99.48%**
14. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ReferenceShortener.kt`** -> AI Confidence: **99.48%**
15. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10Resolver.kt`** -> AI Confidence: **99.48%**
16. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ScopeProvider.kt`** -> AI Confidence: **99.48%**
17. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SubstitutorProvider.kt`** -> AI Confidence: **99.48%**
18. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolDeclarationOverridesProvider.kt`** -> AI Confidence: **99.48%**
19. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolInformationProvider.kt`** -> AI Confidence: **99.48%**
20. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolProvider.kt`** -> AI Confidence: **99.48%**
21. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolRelationProvider.kt`** -> AI Confidence: **99.48%**
22. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeCreator.kt`** -> AI Confidence: **99.48%**
23. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeInformationProvider.kt`** -> AI Confidence: **99.48%**
24. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeProvider.kt`** -> AI Confidence: **99.48%**
25. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeRelationChecker.kt`** -> AI Confidence: **99.48%**
26. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10VisibilityChecker.kt`** -> AI Confidence: **99.48%**
27. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/contracts/descriptorContractUtils.kt`** -> AI Confidence: **99.48%**
28. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/references/ReadWriteAccessCheckerDescriptorsImpl.kt`** -> AI Confidence: **99.48%**
29. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/scopes/KaFe10FileScope.kt`** -> AI Confidence: **99.48%**
30. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/scopes/KaFe10PackageScope.kt`** -> AI Confidence: **99.48%**
31. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/scopes/KaFe10ScopeResolution.kt`** -> AI Confidence: **99.48%**
32. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/signatures/KaFe10FunctionSignature.kt`** -> AI Confidence: **99.48%**
33. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/signatures/KaFe10VariableSignature.kt`** -> AI Confidence: **99.48%**
34. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/KaFe10FileSymbol.kt`** -> AI Confidence: **99.48%**
35. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/KaFe10PackageSymbol.kt`** -> AI Confidence: **99.48%**
36. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescAnonymousFunctionSymbol.kt`** -> AI Confidence: **99.48%**
37. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescAnonymousObjectSymbol.kt`** -> AI Confidence: **99.48%**
38. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescConstructorSymbol.kt`** -> AI Confidence: **99.48%**
39. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescContextReceiverBasedContextParameterSymbol.kt`** -> AI Confidence: **99.48%**
40. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescDefaultBackingFieldSymbol.kt`** -> AI Confidence: **99.48%**
41. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescDefaultPropertySetterSymbol.kt`** -> AI Confidence: **99.48%**
42. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescEnumEntrySymbol.kt`** -> AI Confidence: **99.48%**
43. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescJavaFieldSymbol.kt`** -> AI Confidence: **99.48%**
44. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescKotlinPropertySymbol.kt`** -> AI Confidence: **99.48%**
45. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescLocalVariableSymbol.kt`** -> AI Confidence: **99.48%**
46. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescNamedClassSymbol.kt`** -> AI Confidence: **99.48%**
47. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescNamedFunctionSymbol.kt`** -> AI Confidence: **99.48%**
48. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescPropertyGetterSymbol.kt`** -> AI Confidence: **99.48%**
49. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescPropertySetterSymbol.kt`** -> AI Confidence: **99.48%**
50. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescSamConstructorSymbol.kt`** -> AI Confidence: **99.48%**
51. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescSyntheticFieldSymbol.kt`** -> AI Confidence: **99.48%**
52. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescSyntheticJavaPropertySymbol.kt`** -> AI Confidence: **99.48%**
53. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescSyntheticJavaPropertySymbolForOverride.kt`** -> AI Confidence: **99.48%**
54. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescTypeAliasSymbol.kt`** -> AI Confidence: **99.48%**
55. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescTypeParameterSymbol.kt`** -> AI Confidence: **99.48%**
56. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DescValueParameterSymbol.kt`** -> AI Confidence: **99.48%**
57. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10DynamicFunctionDescValueParameterSymbol.kt`** -> AI Confidence: **99.48%**
58. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/KaFe10ReceiverParameterSymbol.kt`** -> AI Confidence: **99.48%**
59. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/base/KaFe10DescSymbol.kt`** -> AI Confidence: **99.48%**
60. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/descriptorBased/base/fe10DescUtils.kt`** -> AI Confidence: **99.48%**
61. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescEnumEntrySymbolPointer.kt`** -> AI Confidence: **99.48%**
62. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescFunctionSymbolPointer.kt`** -> AI Confidence: **99.48%**
63. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescNamedClassSymbolPointer.kt`** -> AI Confidence: **99.48%**
64. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescSamConstructorSymbolPointer.kt`** -> AI Confidence: **99.48%**
65. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10DescSyntheticFieldSymbolPointer.kt`** -> AI Confidence: **99.48%**
66. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10PackageSymbolPointer.kt`** -> AI Confidence: **99.48%**
67. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10PsiDefaultBackingFieldSymbolPointer.kt`** -> AI Confidence: **99.48%**
68. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/pointers/KaFe10PsiDefaultSetterParameterSymbolPointer.kt`** -> AI Confidence: **99.48%**
69. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiAnonymousFunctionSymbol.kt`** -> AI Confidence: **99.48%**
70. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiAnonymousObjectSymbol.kt`** -> AI Confidence: **99.48%**
71. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiBackingFieldSymbol.kt`** -> AI Confidence: **99.48%**
72. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiClassInitializerSymbol.kt`** -> AI Confidence: **99.48%**
73. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiConstructorSymbol.kt`** -> AI Confidence: **99.48%**
74. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiContextParameterSymbol.kt`** -> AI Confidence: **99.48%**
75. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiContextReceiverBasedContextParameterSymbol.kt`** -> AI Confidence: **99.48%**
76. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiDefaultBackingFieldSymbol.kt`** -> AI Confidence: **99.48%**
77. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiDefaultPropertyGetterSymbol.kt`** -> AI Confidence: **99.48%**
78. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiDefaultPropertySetterSymbol.kt`** -> AI Confidence: **99.48%**
79. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiDefaultSetterParameterSymbol.kt`** -> AI Confidence: **99.48%**
80. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiDestructuringDeclarationSymbol.kt`** -> AI Confidence: **99.48%**
81. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiEnumEntrySymbol.kt`** -> AI Confidence: **99.48%**
82. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiKotlinPropertySymbol.kt`** -> AI Confidence: **99.48%**
83. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiLiteralAnonymousFunctionSymbol.kt`** -> AI Confidence: **99.48%**
84. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiLocalVariableSymbol.kt`** -> AI Confidence: **99.48%**
85. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiLoopParameterLocalVariableSymbol.kt`** -> AI Confidence: **99.48%**
86. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiNamedClassSymbol.kt`** -> AI Confidence: **99.48%**
87. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiNamedFunctionSymbol.kt`** -> AI Confidence: **99.48%**
88. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiPropertyGetterSymbol.kt`** -> AI Confidence: **99.48%**
89. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiPropertySetterSymbol.kt`** -> AI Confidence: **99.48%**
90. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiScriptSymbol.kt`** -> AI Confidence: **99.48%**
91. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiTypeAliasSymbol.kt`** -> AI Confidence: **99.48%**
92. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiTypeParameterSymbol.kt`** -> AI Confidence: **99.48%**
93. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/KaFe10PsiValueParameterSymbol.kt`** -> AI Confidence: **99.48%**
94. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/base/KaFe10PsiSymbol.kt`** -> AI Confidence: **99.48%**
95. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/symbols/psiBased/base/KaFe10PsiSymbolUtils.kt`** -> AI Confidence: **99.48%**
96. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10CapturedType.kt`** -> AI Confidence: **99.48%**
97. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10ClassErrorType.kt`** -> AI Confidence: **99.48%**
98. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10DefinitelyNotNullType.kt`** -> AI Confidence: **99.48%**
99. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10DynamicType.kt`** -> AI Confidence: **99.48%**
100. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10ErrorType.kt`** -> AI Confidence: **99.48%**
101. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10FlexibleType.kt`** -> AI Confidence: **99.48%**
102. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10FunctionType.kt`** -> AI Confidence: **99.48%**
103. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10IntersectionType.kt`** -> AI Confidence: **99.48%**
104. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10NewCapturedType.kt`** -> AI Confidence: **99.48%**
105. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10TypeParameterType.kt`** -> AI Confidence: **99.48%**
106. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/KaFe10UsualClassType.kt`** -> AI Confidence: **99.48%**
107. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/base/KaFe10Type.kt`** -> AI Confidence: **99.48%**
108. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/types/typeCreation/KaFe10TypeCreator.kt`** -> AI Confidence: **99.48%**
109. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/InlineDelegatedPropertyAccessorsAnalyzer.kt`** -> AI Confidence: **99.48%**
110. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/InlineFunctionsCollector.kt`** -> AI Confidence: **99.48%**
111. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/KaFe10DebugTypeRenderer.kt`** -> AI Confidence: **99.48%**
112. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/KaFe10JvmTypeMapperContext.kt`** -> AI Confidence: **99.48%**
113. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/KaFe10TypeSystemCommonBackendContextForTypeMapping.kt`** -> AI Confidence: **99.48%**
114. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/Fe10KDocReference.kt`** -> AI Confidence: **99.48%**
115. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/Fe10SyntheticPropertyAccessorReference.kt`** -> AI Confidence: **99.48%**
116. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10ArrayAccessReference.kt`** -> AI Confidence: **99.48%**
117. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10CollectionLiteralReference.kt`** -> AI Confidence: **99.48%**
118. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10ConstructorDelegationReference.kt`** -> AI Confidence: **99.48%**
119. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10DefaultAnnotationArgumentReference.kt`** -> AI Confidence: **99.48%**
120. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10DestructuringDeclarationEntry.kt`** -> AI Confidence: **99.48%**
121. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10ForLoopInReference.kt`** -> AI Confidence: **99.48%**
122. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10InvokeFunctionReference.kt`** -> AI Confidence: **99.48%**
123. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10PropertyDelegationMethodsReference.kt`** -> AI Confidence: **99.48%**
124. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/KtFe10SimpleNameReference.kt`** -> AI Confidence: **99.48%**
125. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/base/KtFe10PolyVariantResolver.kt`** -> AI Confidence: **99.48%**
126. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/base/KtFe10Reference.kt`** -> AI Confidence: **99.48%**
127. **`analysis/analysis-api-fe10/src/org/jetbrains/kotlin/references/fe10/util/DescriptorsToSourceUtilsIde.kt`** -> AI Confidence: **99.48%**
128. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/ArgumentsConverterGenerator.kt`** -> AI Confidence: **99.48%**
129. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/HLDiagnosticConverter.kt`** -> AI Confidence: **99.48%**
130. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/rendererrs/AbstractDiagnosticsDataClassRenderer.kt`** -> AI Confidence: **99.48%**
131. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/rendererrs/FirDiagnosticToKaDiagnosticConverterRenderer.kt`** -> AI Confidence: **99.48%**
132. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/rendererrs/KaDiagnosticClassImplementationRenderer.kt`** -> AI Confidence: **99.48%**
133. **`analysis/analysis-api-fir/analysis-api-fir-generator/src/org/jetbrains/kotlin/analysis/api/fir/generator/rendererrs/KaDiagnosticClassRenderer.kt`** -> AI Confidence: **99.48%**
134. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/FirSyntheticFunctionInterfaceSourceProvider.kt`** -> AI Confidence: **99.48%**
135. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/FirUtils.kt`** -> AI Confidence: **99.48%**
136. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaFirDefaultImportsProvider.kt`** -> AI Confidence: **99.48%**
137. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaFirSession.kt`** -> AI Confidence: **99.48%**
138. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaFirSessionProvider.kt`** -> AI Confidence: **99.48%**
139. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/KaSymbolByFirBuilder.kt`** -> AI Confidence: **99.48%**
140. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/annotations/KaFirAnnotationListForDeclaration.kt`** -> AI Confidence: **99.48%**
141. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/annotations/KaFirAnnotationListForType.kt`** -> AI Confidence: **99.48%**
142. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/annotations/firAnnotationUtils.kt`** -> AI Confidence: **99.48%**
143. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompilerFacility.kt`** -> AI Confidence: **99.48%**
144. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompilerPluginGeneratedDeclarationsProvider.kt`** -> AI Confidence: **99.48%**
145. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompletionCandidateChecker.kt`** -> AI Confidence: **99.48%**
146. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirDataFlowProvider.kt`** -> AI Confidence: **99.48%**
147. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirDiagnosticProvider.kt`** -> AI Confidence: **99.48%**
148. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirEvaluator.kt`** -> AI Confidence: **99.48%**
149. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirExpressionInformationProvider.kt`** -> AI Confidence: **99.48%**
150. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirExpressionTypeProvider.kt`** -> AI Confidence: **99.48%**
151. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirInternalCacheStorage.kt`** -> AI Confidence: **99.48%**
152. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirJavaInteroperabilityComponent.kt`** -> AI Confidence: **99.48%**
153. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirKDocProvider.kt`** -> AI Confidence: **99.48%**
154. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirOriginalPsiProvider.kt`** -> AI Confidence: **99.48%**
155. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirReferenceShortener.kt`** -> AI Confidence: **99.48%**
156. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolveExtensionInfoProvider.kt`** -> AI Confidence: **99.48%**
157. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt`** -> AI Confidence: **99.48%**
158. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirScopeProvider.kt`** -> AI Confidence: **99.48%**
159. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSessionComponent.kt`** -> AI Confidence: **99.48%**
160. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSignatureSubstitutor.kt`** -> AI Confidence: **99.48%**
161. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSubstitutorProvider.kt`** -> AI Confidence: **99.48%**
162. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSymbolDeclarationOverridesProvider.kt`** -> AI Confidence: **99.48%**
163. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSymbolInformationProvider.kt`** -> AI Confidence: **99.48%**
164. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirSymbolRelationProvider.kt`** -> AI Confidence: **99.48%**
165. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirTypeCreator.kt`** -> AI Confidence: **99.48%**
166. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirTypeInformationProvider.kt`** -> AI Confidence: **99.48%**
167. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirTypeProvider.kt`** -> AI Confidence: **99.48%**
168. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirTypeRelationChecker.kt`** -> AI Confidence: **99.48%**
169. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirVisibilityChecker.kt`** -> AI Confidence: **99.48%**
170. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/compilation/CodeFragmentContextDeclarationCache.kt`** -> AI Confidence: **99.48%**
171. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/inlineStackDataUtils.kt`** -> AI Confidence: **99.48%**
172. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/referenceShortenerUtils.kt`** -> AI Confidence: **99.48%**
173. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/contracts/firContractUtils.kt`** -> AI Confidence: **99.48%**
174. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/diagnostics/KaAbstractFirDiagnostic.kt`** -> AI Confidence: **99.48%**
175. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/evaluate/FirAnnotationValueConverter.kt`** -> AI Confidence: **99.48%**
176. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/evaluate/FirCompileTimeConstantEvaluator.kt`** -> AI Confidence: **99.48%**
177. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/projectStructure/KaFirLibraryTargetPlatformContentScopeRefiner.kt`** -> AI Confidence: **99.48%**
178. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/psiUtils.kt`** -> AI Confidence: **99.48%**
179. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/ClassicKDocReferenceResolver.kt`** -> AI Confidence: **99.48%**
180. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/FirReferenceResolveHelper.kt`** -> AI Confidence: **99.48%**
181. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KDocReferenceResolver.kt`** -> AI Confidence: **99.48%**
182. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirArrayAccessReference.kt`** -> AI Confidence: **99.48%**
183. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirCollectionLiteralReference.kt`** -> AI Confidence: **99.48%**
184. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirConstructorDelegationReference.kt`** -> AI Confidence: **99.48%**
185. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirDefaultAnnotationArgumentReference.kt`** -> AI Confidence: **99.48%**
186. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirDestructuringDeclarationReference.kt`** -> AI Confidence: **99.48%**
187. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirForLoopInReference.kt`** -> AI Confidence: **99.48%**
188. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirInvokeFunctionReference.kt`** -> AI Confidence: **99.48%**
189. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirKDocReference.kt`** -> AI Confidence: **99.48%**
190. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirPropertyDelegationMethodsReference.kt`** -> AI Confidence: **99.48%**
191. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirReference.kt`** -> AI Confidence: **99.48%**
192. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirReferenceResolver.kt`** -> AI Confidence: **99.48%**
193. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/KaFirSimpleNameReference.kt`** -> AI Confidence: **99.48%**
194. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/references/ReadWriteAccessCheckerFirImpl.kt`** -> AI Confidence: **99.48%**
195. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/DeclarationsInPackageProvider.kt`** -> AI Confidence: **99.48%**
196. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/FirCallableFilteringScope.kt`** -> AI Confidence: **99.48%**
197. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/FirExcludingNonInnerClassesScope.kt`** -> AI Confidence: **99.48%**
198. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/FirJavaDeclaredMembersOnlyScope.kt`** -> AI Confidence: **99.48%**
199. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/FirNoClassifiersScope.kt`** -> AI Confidence: **99.48%**
200. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/FirNonStaticMembersScope.kt`** -> AI Confidence: **99.48%**
201. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/KaFirFileScope.kt`** -> AI Confidence: **99.48%**
202. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/KaFirNonStarImportingScope.kt`** -> AI Confidence: **99.48%**
203. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/KaFirPackageScope.kt`** -> AI Confidence: **99.48%**
204. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/KaFirStarImportingScope.kt`** -> AI Confidence: **99.48%**
205. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/signatures/KaFirFunctionSignature.kt`** -> AI Confidence: **99.48%**
206. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/signatures/KaFirVariableSignature.kt`** -> AI Confidence: **99.48%**
207. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirAnonymousFunctionSymbol.kt`** -> AI Confidence: **99.48%**
208. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirAnonymousObjectSymbol.kt`** -> AI Confidence: **99.48%**
209. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirArrayOfSymbolProvider.kt`** -> AI Confidence: **99.48%**
210. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirBackingFieldSymbol.kt`** -> AI Confidence: **99.48%**
211. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirBasePropertyAccessorSymbol.kt`** -> AI Confidence: **99.48%**
212. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirClassInitializerSymbol.kt`** -> AI Confidence: **99.48%**
213. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirConstructorSymbol.kt`** -> AI Confidence: **99.48%**
214. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirContextParameterSymbol.kt`** -> AI Confidence: **99.48%**
215. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirContextReceiverBasedContextParameterSymbol.kt`** -> AI Confidence: **99.48%**
216. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirDefaultBackingFieldSymbol.kt`** -> AI Confidence: **99.48%**
217. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirDefaultPropertyGetterSymbol.kt`** -> AI Confidence: **99.48%**
218. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirDefaultPropertySetterSymbol.kt`** -> AI Confidence: **99.48%**
219. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirDefaultSetterValueParameter.kt`** -> AI Confidence: **99.48%**
220. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirDestructuringDeclarationSymbol.kt`** -> AI Confidence: **99.48%**
221. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirEnumEntryInitializerSymbol.kt`** -> AI Confidence: **99.48%**
222. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirEnumEntrySymbol.kt`** -> AI Confidence: **99.48%**
223. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirFileSymbol.kt`** -> AI Confidence: **99.48%**
224. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirKotlinPropertySymbol.kt`** -> AI Confidence: **99.48%**
225. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirLocalVariableSymbol.kt`** -> AI Confidence: **99.48%**
226. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirNamedClassSymbol.kt`** -> AI Confidence: **99.48%**
227. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirNamedClassSymbolBase.kt`** -> AI Confidence: **99.48%**
228. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirNamedFunctionSymbol.kt`** -> AI Confidence: **99.48%**
229. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPackageSymbol.kt`** -> AI Confidence: **99.48%**
230. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPropertyGetterSymbol.kt`** -> AI Confidence: **99.48%**
231. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPropertySetterSymbol.kt`** -> AI Confidence: **99.48%**
232. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPsiJavaClassSymbol.kt`** -> AI Confidence: **99.48%**
233. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPsiJavaTypeParameterSymbol.kt`** -> AI Confidence: **99.48%**
234. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirPsiSymbol.kt`** -> AI Confidence: **99.48%**
235. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirReceiverParameterSymbol.kt`** -> AI Confidence: **99.48%**
236. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSamConstructorSymbol.kt`** -> AI Confidence: **99.48%**
237. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSymbol.kt`** -> AI Confidence: **99.48%**
238. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSymbolProvider.kt`** -> AI Confidence: **99.48%**
239. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSyntheticJavaPropertySymbol.kt`** -> AI Confidence: **99.48%**
240. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSyntheticPropertyGetterSymbol.kt`** -> AI Confidence: **99.48%**
241. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirSyntheticPropertySetterSymbol.kt`** -> AI Confidence: **99.48%**
242. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirTypeAliasSymbol.kt`** -> AI Confidence: **99.48%**
243. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirTypeParameterSymbol.kt`** -> AI Confidence: **99.48%**
244. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirTypeParameterSymbolBase.kt`** -> AI Confidence: **99.48%**
245. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/KaFirValueParameterSymbol.kt`** -> AI Confidence: **99.48%**
246. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/firSymbolUtils.kt`** -> AI Confidence: **99.48%**
247. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirBackingFieldSymbolPointer.kt`** -> AI Confidence: **99.48%**
248. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirClassLikeSymbolPointer.kt`** -> AI Confidence: **99.48%**
249. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirDynamicFunctionSymbolPointer.kt`** -> AI Confidence: **99.48%**
250. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirDynamicPropertySymbolPointer.kt`** -> AI Confidence: **99.48%**
251. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirEnumEntryInitializerSymbolPointer.kt`** -> AI Confidence: **99.48%**
252. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirEnumEntrySymbolPointer.kt`** -> AI Confidence: **99.48%**
253. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirJavaFieldSymbolPointer.kt`** -> AI Confidence: **99.48%**
254. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirJavaSyntheticPropertyAccessorFunctionSymbolPointer.kt`** -> AI Confidence: **99.48%**
255. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirJavaSyntheticPropertySymbolPointer.kt`** -> AI Confidence: **99.48%**
256. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirLocalClassFromCompilerPluginSymbolPointer.kt`** -> AI Confidence: **99.48%**
257. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirMemberFunctionSymbolPointer.kt`** -> AI Confidence: **99.48%**
258. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirMemberPropertySymbolPointer.kt`** -> AI Confidence: **99.48%**
259. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirMemberSymbolPointer.kt`** -> AI Confidence: **99.48%**
260. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirNestedInLocalClassFromCompilerPluginSymbolPointer.kt`** -> AI Confidence: **99.48%**
261. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirPackageSymbolPointer.kt`** -> AI Confidence: **99.48%**
262. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirPrimaryConstructorSymbolPointer.kt`** -> AI Confidence: **99.48%**
263. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirPsiBasedPropertySymbolPointer.kt`** -> AI Confidence: **99.48%**
264. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirResultPropertySymbolPointer.kt`** -> AI Confidence: **99.48%**
265. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirSamConstructorSymbolPointer.kt`** -> AI Confidence: **99.48%**
266. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirScriptParameterSymbolPointer.kt`** -> AI Confidence: **99.48%**
267. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirScriptSymbolPointer.kt`** -> AI Confidence: **99.48%**
268. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirSecondaryConstructorSymbolPointer.kt`** -> AI Confidence: **99.48%**
269. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTopLevelCallableSymbolPointer.kt`** -> AI Confidence: **99.48%**
270. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTopLevelFunctionSymbolPointer.kt`** -> AI Confidence: **99.48%**
271. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTopLevelPropertySymbolPointer.kt`** -> AI Confidence: **99.48%**
272. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTypeAliasedConstructorMemberPointer.kt`** -> AI Confidence: **99.48%**
273. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirTypeParameterSymbolPointer.kt`** -> AI Confidence: **99.48%**
274. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/KaFirValueParameterSymbolPointer.kt`** -> AI Confidence: **99.48%**
275. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/symbols/pointers/pointerUtils.kt`** -> AI Confidence: **99.48%**
276. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirCapturedType.kt`** -> AI Confidence: **99.48%**
277. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirClassErrorType.kt`** -> AI Confidence: **99.48%**
278. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirDefinitelyNotNullType.kt`** -> AI Confidence: **99.48%**
279. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirDynamicType.kt`** -> AI Confidence: **99.48%**
280. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirErrorType.kt`** -> AI Confidence: **99.48%**
281. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirFlexibleType.kt`** -> AI Confidence: **99.48%**
282. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirFunctionType.kt`** -> AI Confidence: **99.48%**
283. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirIntersectionType.kt`** -> AI Confidence: **99.48%**
284. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirSubstitutor.kt`** -> AI Confidence: **99.48%**
285. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirTypeParameterType.kt`** -> AI Confidence: **99.48%**
286. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/KaFirUsualClassType.kt`** -> AI Confidence: **99.48%**
287. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/qualifiers/ErrorClassTypeQualifierBuilder.kt`** -> AI Confidence: **99.48%**
288. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/qualifiers/UsualClassTypeQualifierBuilder.kt`** -> AI Confidence: **99.48%**
289. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/types/typeCreation/KaFirTypeCreator.kt`** -> AI Confidence: **99.48%**
290. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/ConeDiagnosticPointer.kt`** -> AI Confidence: **99.48%**
291. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/ConeTypePointer.kt`** -> AI Confidence: **99.48%**
292. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/FirQualifierPartPointer.kt`** -> AI Confidence: **99.48%**
293. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/KaFirCacheCleaner.kt`** -> AI Confidence: **99.48%**
294. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/errorUtils.kt`** -> AI Confidence: **99.48%**
295. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/firUtils.kt`** -> AI Confidence: **99.48%**
296. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/ktSymbolUtils.kt`** -> AI Confidence: **99.48%**
297. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/scopesUtils.kt`** -> AI Confidence: **99.48%**
298. **`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/utils/typeUtils.kt`** -> AI Confidence: **99.48%**
299. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/annotations/KaAnnotationImpl.kt`** -> AI Confidence: **99.48%**
300. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/annotations/KaBaseEmptyAnnotationList.kt`** -> AI Confidence: **99.48%**
301. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/annotations/KaBaseNamedAnnotationValue.kt`** -> AI Confidence: **99.48%**
302. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseAnalysisScopeProviderImpl.kt`** -> AI Confidence: **99.48%**
303. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseDataFlowProvider.kt`** -> AI Confidence: **99.48%**
304. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseIllegalPsiException.kt`** -> AI Confidence: **99.48%**
305. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseKDocProvider.kt`** -> AI Confidence: **99.48%**
306. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseResolver.kt`** -> AI Confidence: **99.48%**
307. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseSignatureSubstitutor.kt`** -> AI Confidence: **99.48%**
308. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseTypeCreator.kt`** -> AI Confidence: **99.48%**
309. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseTypeProvider.kt`** -> AI Confidence: **99.48%**
310. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaBaseTypeRelationChecker.kt`** -> AI Confidence: **99.48%**
311. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/components/KaRendererImpl.kt`** -> AI Confidence: **99.48%**
312. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/contracts/description/KaBaseEffects.kt`** -> AI Confidence: **99.48%**
313. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/contracts/description/KaBaseValues.kt`** -> AI Confidence: **99.48%**
314. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/contracts/description/booleans/KaBaseLogicalCombinators.kt`** -> AI Confidence: **99.48%**
315. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/contracts/description/booleans/KaBasePredicates.kt`** -> AI Confidence: **99.48%**
316. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/imports/KaBaseDefaultImportsProvider.kt`** -> AI Confidence: **99.48%**
317. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/java/KaBaseJavaModuleResolver.kt`** -> AI Confidence: **99.48%**
318. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/java/KaBaseKotlinJavaPsiFacade.kt`** -> AI Confidence: **99.48%**
319. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/projectStructure/KaBaseResolutionScope.kt`** -> AI Confidence: **99.48%**
320. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/projectStructure/KaBaseResolutionScopeProvider.kt`** -> AI Confidence: **99.48%**
321. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/projectStructure/KaBuiltinsModuleImpl.kt`** -> AI Confidence: **99.48%**
322. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/references/KaBaseSimpleNameReference.kt`** -> AI Confidence: **99.48%**
323. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/references/KotlinReferenceProvidersServiceImpl.kt`** -> AI Confidence: **99.48%**
324. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/sessions/KaBaseSessionProvider.kt`** -> AI Confidence: **99.48%**
325. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/signatures/KaBaseVariableSignature.kt`** -> AI Confidence: **99.48%**
326. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/symbols/pointers/KaBaseCachedSymbolPointer.kt`** -> AI Confidence: **99.48%**
327. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/symbols/pointers/KaBaseContextParameterSymbolPointer.kt`** -> AI Confidence: **99.48%**
328. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/symbols/pointers/KaBasePsiSymbolPointer.kt`** -> AI Confidence: **99.48%**
329. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/types/typeCreation/KaBaseTypeCreator.kt`** -> AI Confidence: **99.48%**
330. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/util/DiagnosticUtils.kt`** -> AI Confidence: **99.48%**
331. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/util/LibraryUtils.kt`** -> AI Confidence: **99.48%**
332. **`analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/util/kotlinPsiUtils.kt`** -> AI Confidence: **99.48%**
333. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/declarations/KotlinCompositeDeclarationProvider.kt`** -> AI Confidence: **99.48%**
334. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/lifetime/KotlinReadActionConfinementLifetimeToken.kt`** -> AI Confidence: **99.48%**
335. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/packages/KotlinCachingPackageProviderFactory.kt`** -> AI Confidence: **99.48%**
336. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/packages/KotlinPackageProviderBase.kt`** -> AI Confidence: **99.48%**
337. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/projectStructure/KaDanglingFileModuleImpl.kt`** -> AI Confidence: **99.48%**
338. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/projectStructure/KotlinProjectStructureProviderBase.kt`** -> AI Confidence: **99.48%**
339. **`analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/projectStructure/utils.kt`** -> AI Confidence: **99.48%**
340. **`analysis/analysis-api-standalone/analysis-api-fir-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneFirCompilerPluginsProvider.kt`** -> AI Confidence: **99.48%**
341. **`analysis/analysis-api-standalone/analysis-api-fir-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneFirDirectInheritorsProvider.kt`** -> AI Confidence: **99.48%**
342. **`analysis/analysis-api-standalone/analysis-api-fir-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/services/LLStandaloneFirElementByPsiElementChooser.kt`** -> AI Confidence: **99.48%**
343. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneAnnotationsResolver.kt`** -> AI Confidence: **99.48%**
344. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneDeclarationIndexImpl.kt`** -> AI Confidence: **99.48%**
345. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneDeclarationProvider.kt`** -> AI Confidence: **99.48%**
346. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/declarations/KotlinStandaloneIndexBuilder.kt`** -> AI Confidence: **99.48%**
347. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/packages/KotlinStandalonePackageProvider.kt`** -> AI Confidence: **99.48%**
348. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/projectStructure/ApplicationServiceRegistration.kt`** -> AI Confidence: **99.48%**
349. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/projectStructure/PluginStructureProvider.kt`** -> AI Confidence: **99.48%**
350. **`analysis/analysis-api-standalone/analysis-api-standalone-base/src/org/jetbrains/kotlin/analysis/api/standalone/base/projectStructure/StandaloneProjectFactory.kt`** -> AI Confidence: **99.48%**
351. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/api/standalone/StandaloneAnalysisAPISessionBuilder.kt`** -> AI Confidence: **99.48%**
352. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/builder/KaLibraryModuleBuilder.kt`** -> AI Confidence: **99.48%**
353. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/builder/KaLibrarySourceModuleBuilder.kt`** -> AI Confidence: **99.48%**
354. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/builder/KaModuleProviderBuilder.kt`** -> AI Confidence: **99.48%**
355. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/builder/KaScriptModuleBuilder.kt`** -> AI Confidence: **99.48%**
356. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/builder/KaSdkModuleBuilder.kt`** -> AI Confidence: **99.48%**
357. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/builder/KaSourceModuleBuilder.kt`** -> AI Confidence: **99.48%**
358. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/impl/KaModuleUtils.kt`** -> AI Confidence: **99.48%**
359. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/impl/KaNotUnderContentRootModuleImpl.kt`** -> AI Confidence: **99.48%**
360. **`analysis/analysis-api-standalone/src/org/jetbrains/kotlin/analysis/project/structure/impl/KotlinStandaloneProjectStructureProvider.kt`** -> AI Confidence: **99.48%**
361. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/KaSession.kt`** -> AI Confidence: **99.48%**
362. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/analyze.kt`** -> AI Confidence: **99.48%**
363. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaCompilerFacility.kt`** -> AI Confidence: **99.48%**
364. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaCompletionCandidateChecker.kt`** -> AI Confidence: **99.48%**
365. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaExpressionInformationProvider.kt`** -> AI Confidence: **99.48%**
366. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaJavaInteroperabilityComponent.kt`** -> AI Confidence: **99.48%**
367. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaKDocProvider.kt`** -> AI Confidence: **99.48%**
368. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaReferenceShortener.kt`** -> AI Confidence: **99.48%**
369. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaRenderer.kt`** -> AI Confidence: **99.48%**
370. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaResolver.kt`** -> AI Confidence: **99.48%**
371. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaScopeProvider.kt`** -> AI Confidence: **99.48%**
372. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaSignatureSubstitutor.kt`** -> AI Confidence: **99.48%**
373. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaSubstitutorProvider.kt`** -> AI Confidence: **99.48%**
374. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaTypeCreator.kt`** -> AI Confidence: **99.48%**
375. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaTypeInformationProvider.kt`** -> AI Confidence: **99.48%**
376. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaTypeProvider.kt`** -> AI Confidence: **99.48%**
377. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaTypeRelationChecker.kt`** -> AI Confidence: **99.48%**
378. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/components/KaVisibilityChecker.kt`** -> AI Confidence: **99.48%**
379. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/contracts/description/contractRendering.kt`** -> AI Confidence: **99.48%**
380. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/projectStructure/KaModule.kt`** -> AI Confidence: **99.48%**
381. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/projectStructure/danglingFiles.kt`** -> AI Confidence: **99.48%**
382. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/annotations/KaAnnotationRenderer.kt`** -> AI Confidence: **99.48%**
383. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/annotations/KaRendererAnnotationsFilter.kt`** -> AI Confidence: **99.48%**
384. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/annotations/renderers/KaAnnotationArgumentsRenderer.kt`** -> AI Confidence: **99.48%**
385. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/annotations/renderers/KaAnnotationListRenderer.kt`** -> AI Confidence: **99.48%**
386. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/annotations/renderers/KaAnnotationQualifierRenderer.kt`** -> AI Confidence: **99.48%**
387. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/annotations/renderers/KaAnnotationUseSiteTargetRenderer.kt`** -> AI Confidence: **99.48%**
388. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/contextReceivers/KaContextReceiversRenderer.kt`** -> AI Confidence: **99.48%**
389. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/contextReceivers/renderers/KaContextReceiverLabelRenderer.kt`** -> AI Confidence: **99.48%**
390. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/base/contextReceivers/renderers/KaContextReceiverListRenderer.kt`** -> AI Confidence: **99.48%**
391. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/KaDeclarationRenderer.kt`** -> AI Confidence: **99.48%**
392. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/KaRendererCodeStyle.kt`** -> AI Confidence: **99.48%**
393. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/bodies/KaVariableInitializerRenderer.kt`** -> AI Confidence: **99.48%**
394. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/modifiers/renderers/KaModifierListRenderer.kt`** -> AI Confidence: **99.48%**
395. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/modifiers/renderers/KaRendererOtherModifiersProvider.kt`** -> AI Confidence: **99.48%**
396. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/rendererUtils.kt`** -> AI Confidence: **99.48%**
397. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/KaCallableParameterRenderer.kt`** -> AI Confidence: **99.48%**
398. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/KaClassifierBodyRenderer.kt`** -> AI Confidence: **99.48%**
399. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/KaDeclarationNameRenderer.kt`** -> AI Confidence: **99.48%**
400. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/KaTypeParametersRenderer.kt`** -> AI Confidence: **99.48%**
401. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaCallableReturnTypeRenderer.kt`** -> AI Confidence: **99.48%**
402. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaCallableSignatureRenderer.kt`** -> AI Confidence: **99.48%**
403. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaConstructorSymbolRenderer.kt`** -> AI Confidence: **99.48%**
404. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaFunctionSymbolRenderer.kt`** -> AI Confidence: **99.48%**
405. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaJavaFieldSymbolRenderer.kt`** -> AI Confidence: **99.48%**
406. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaKotlinPropertySymbolRenderer.kt`** -> AI Confidence: **99.48%**
407. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaLocalVariableSymbolRenderer.kt`** -> AI Confidence: **99.48%**
408. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaPropertyAccessorsRenderer.kt`** -> AI Confidence: **99.48%**
409. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaSyntheticJavaPropertySymbolRenderer.kt`** -> AI Confidence: **99.48%**
410. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/classifiers/KaNamedClassOrObjectSymbolRenderer.kt`** -> AI Confidence: **99.48%**
411. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/classifiers/KaSingleTypeParameterSymbolRenderer.kt`** -> AI Confidence: **99.48%**
412. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/superTypes/KaSuperTypesCallArgumentsRenderer.kt`** -> AI Confidence: **99.48%**
413. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/superTypes/KaSuperTypesFilter.kt`** -> AI Confidence: **99.48%**
414. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/KaTypeRenderer.kt`** -> AI Confidence: **99.48%**
415. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/renderers/KaClassTypeQualifierRenderer.kt`** -> AI Confidence: **99.48%**
416. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/renderers/KaFlexibleTypeRenderer.kt`** -> AI Confidence: **99.48%**
417. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/renderers/KaFunctionalTypeRenderer.kt`** -> AI Confidence: **99.48%**
418. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/renderers/KaTypeErrorTypeRenderer.kt`** -> AI Confidence: **99.48%**
419. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/types/renderers/KaTypeProjectionRenderer.kt`** -> AI Confidence: **99.48%**
420. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/resolution/KaCalls.kt`** -> AI Confidence: **99.48%**
421. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/resolution/KaSymbolResolutionAttempt.kt`** -> AI Confidence: **99.48%**
422. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaClassLikeSymbol.kt`** -> AI Confidence: **99.48%**
423. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaDebugSymbolRenderer.kt`** -> AI Confidence: **99.48%**
424. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaSymbol.kt`** -> AI Confidence: **99.48%**
425. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaSymbolProvider.kt`** -> AI Confidence: **99.48%**
426. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/symbols/KaVariableSymbol.kt`** -> AI Confidence: **99.48%**
427. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/types/KaType.kt`** -> AI Confidence: **99.48%**
428. **`analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/utils/errors/exceptionAttachmentBuilderHelpers.kt`** -> AI Confidence: **99.48%**
429. **`analysis/analysis-api/testData/components/compilerFacility/compilation/sourceLibModuleInlineFuncChains.kt`** -> AI Confidence: **99.48%**
430. **`analysis/analysis-test-framework/testFixtures/org/jetbrains/kotlin/analysis/test/framework/utils/commonTestUtils.kt`** -> AI Confidence: **99.48%**
431. **`analysis/decompiled/decompiler-js/src/org/jetbrains/kotlin/analysis/decompiler/js/KotlinJavaScriptMetadataStubBuilder.kt`** -> AI Confidence: **99.48%**
432. **`analysis/decompiled/decompiler-native/src/org/jetbrains/kotlin/analysis/decompiler/konan/KlibLoadingMetadataCache.kt`** -> AI Confidence: **99.48%**
433. **`analysis/decompiled/decompiler-native/src/org/jetbrains/kotlin/analysis/decompiler/konan/KlibMetadataStubBuilder.kt`** -> AI Confidence: **99.48%**
434. **`analysis/decompiled/decompiler-native/src/org/jetbrains/kotlin/analysis/decompiler/konan/NearFileClassDataFinder.kt`** -> AI Confidence: **99.48%**
435. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/ClsClassFinder.kt`** -> AI Confidence: **99.48%**
436. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/ClsKotlinBinaryClassCache.kt`** -> AI Confidence: **99.48%**
437. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/DirectoryBasedClassFinder.kt`** -> AI Confidence: **99.48%**
438. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/DirectoryBasedDataFinder.kt`** -> AI Confidence: **99.48%**
439. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/KotlinClsStubBuilder.kt`** -> AI Confidence: **99.48%**
440. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/KotlinJvmAnnotationArgumentsCollector.kt`** -> AI Confidence: **99.48%**
441. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/KotlinMetadataStubBuilder.kt`** -> AI Confidence: **99.48%**
442. **`analysis/decompiled/decompiler-to-file-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/file/MetadataClsAnnotationLoader.kt`** -> AI Confidence: **99.48%**
443. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/BuiltinsVirtualFileProvider.kt`** -> AI Confidence: **99.48%**
444. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/KotlinBuiltInDecompiler.kt`** -> AI Confidence: **99.48%**
445. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/KotlinBuiltInMetadataStubBuilder.kt`** -> AI Confidence: **99.48%**
446. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/KotlinClassFileDecompiler.kt`** -> AI Confidence: **99.48%**
447. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/KotlinDecompiledFileViewProvider.kt`** -> AI Confidence: **99.48%**
448. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/file/KtDecompiledFile.kt`** -> AI Confidence: **99.48%**
449. **`analysis/decompiled/decompiler-to-psi/src/org/jetbrains/kotlin/analysis/decompiler/psi/text/decompiledTextBuilder.kt`** -> AI Confidence: **99.48%**
450. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/CallableClsStubBuilder.kt`** -> AI Confidence: **99.48%**
451. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/ClassClsStubBuilder.kt`** -> AI Confidence: **99.48%**
452. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/ClsContractBuilder.kt`** -> AI Confidence: **99.48%**
453. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/ClsStubBuilderContext.kt`** -> AI Confidence: **99.48%**
454. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/TypeClsStubBuilder.kt`** -> AI Confidence: **99.48%**
455. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/clsStubBuilding.kt`** -> AI Confidence: **99.48%**
456. **`analysis/decompiled/decompiler-to-stubs/src/org/jetbrains/kotlin/analysis/decompiler/stub/typeAliasClsStubBuilding.kt`** -> AI Confidence: **99.48%**
457. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KDocReference.kt`** -> AI Confidence: **99.48%**
458. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtCollectionLiteralReference.kt`** -> AI Confidence: **99.48%**
459. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtDefaultAnnotationArgumentReference.kt`** -> AI Confidence: **99.48%**
460. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtInvokeFunctionReference.kt`** -> AI Confidence: **99.48%**
461. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtReference.kt`** -> AI Confidence: **99.48%**
462. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/KtSimpleNameReference.kt`** -> AI Confidence: **99.48%**
463. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/ReadWriteAccessChecker.kt`** -> AI Confidence: **99.48%**
464. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/SyntheticPropertyAccessorReference.kt`** -> AI Confidence: **99.48%**
465. **`analysis/kt-references/src/org/jetbrains/kotlin/idea/references/referenceUtils.kt`** -> AI Confidence: **99.48%**
466. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/KotlinAsJavaSupport.kt`** -> AI Confidence: **99.48%**
467. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/KotlinAsJavaSupportBase.kt`** -> AI Confidence: **99.48%**
468. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/LightClassUtil.kt`** -> AI Confidence: **99.48%**
469. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/elements/FakeFileForLightClass.kt`** -> AI Confidence: **99.48%**
470. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/elements/KotlinLightMethodUtils.kt`** -> AI Confidence: **99.48%**
471. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/elements/KtLightAnnotationsValues.kt`** -> AI Confidence: **99.48%**
472. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/elements/KtLightElementBase.kt`** -> AI Confidence: **99.48%**
473. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/finder/JavaElementFinder.kt`** -> AI Confidence: **99.48%**
474. **`analysis/light-classes-base/src/org/jetbrains/kotlin/asJava/lightClassUtils.kt`** -> AI Confidence: **99.48%**
475. **`analysis/low-level-api-fir/low-level-api-fir-compiler-tests/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/compiler/based/AbstractLLBlackBoxTestBase.kt`** -> AI Confidence: **99.48%**
476. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/LLFirLazyDeclarationResolver.kt`** -> AI Confidence: **99.48%**
477. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/LLResolutionFacadeService.kt`** -> AI Confidence: **99.48%**
478. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/FirDesignation.kt`** -> AI Confidence: **99.48%**
479. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/InvalidFirElementTypeException.kt`** -> AI Confidence: **99.48%**
480. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/LLResolutionFacade.kt`** -> AI Confidence: **99.48%**
481. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/LowLevelFirApiFacade.kt`** -> AI Confidence: **99.48%**
482. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/targets/LLFirResolveTarget.kt`** -> AI Confidence: **99.48%**
483. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/targets/LLFirWholeElementResolveTarget.kt`** -> AI Confidence: **99.48%**
484. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/api/targets/LLPartialBodyAnalysisState.kt`** -> AI Confidence: **99.48%**
485. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/compile/CodeFragmentCapturedValueAnalyzer.kt`** -> AI Confidence: **99.48%**
486. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/compile/CodeFragmentScopeProvider.kt`** -> AI Confidence: **99.48%**
487. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/compile/CompilationPeerCollector.kt`** -> AI Confidence: **99.48%**
488. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/AbstractFirIdeDiagnosticsCollector.kt`** -> AI Confidence: **99.48%**
489. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/FileStructureElementDiagnosticRetriever.kt`** -> AI Confidence: **99.48%**
490. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/LLFirDiagnosticReporter.kt`** -> AI Confidence: **99.48%**
491. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/LLFirDiagnosticVisitor.kt`** -> AI Confidence: **99.48%**
492. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostics/fir/ContextCollectingDiagnosticCollectorVisitor.kt`** -> AI Confidence: **99.48%**
493. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/element/builder/FirElementBuilder.kt`** -> AI Confidence: **99.48%**
494. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/builder/LLFirDeclrationsCacheForModule.kt`** -> AI Confidence: **99.48%**
495. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/builder/LLFirLockProvider.kt`** -> AI Confidence: **99.48%**
496. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/FileElementFactory.kt`** -> AI Confidence: **99.48%**
497. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/FileStructure.kt`** -> AI Confidence: **99.48%**
498. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/FileStructureElement.kt`** -> AI Confidence: **99.48%**
499. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/FirElementsRecorder.kt`** -> AI Confidence: **99.48%**
500. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/LLElementMapper.kt`** -> AI Confidence: **99.48%**
501. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/LLFirDeclarationModificationService.kt`** -> AI Confidence: **99.48%**
502. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/file/structure/inBlockModification.kt`** -> AI Confidence: **99.48%**
503. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/FirLazyBodiesCalculator.kt`** -> AI Confidence: **99.48%**
504. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/LLFirModuleLazyDeclarationResolver.kt`** -> AI Confidence: **99.48%**
505. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/LLFirResolveDesignationCollector.kt`** -> AI Confidence: **99.48%**
506. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/NonLocalAnnotationVisitor.kt`** -> AI Confidence: **99.48%**
507. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/lazy/resolve/RawFirNonLocalDeclarationBuilder.kt`** -> AI Confidence: **99.48%**
508. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/projectStructure/LLFirBuiltinsSessionFactory.kt`** -> AI Confidence: **99.48%**
509. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/projectStructure/LLFirModuleData.kt`** -> AI Confidence: **99.48%**
510. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/projectStructure/sessionFactoryHelpers.kt`** -> AI Confidence: **99.48%**
511. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/FirCallableSignature.kt`** -> AI Confidence: **99.48%**
512. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirBuiltinsAndCloneableSessionProvider.kt`** -> AI Confidence: **99.48%**
513. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirIdePredicateBasedProvider.kt`** -> AI Confidence: **99.48%**
514. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirIdeRegisteredPluginAnnotations.kt`** -> AI Confidence: **99.48%**
515. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirLibrarySessionProvider.kt`** -> AI Confidence: **99.48%**
516. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirPrivateVisibleFromDifferentModuleExtension.kt`** -> AI Confidence: **99.48%**
517. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLFirProvider.kt`** -> AI Confidence: **99.48%**
518. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/LLSealedInheritorsProvider.kt`** -> AI Confidence: **99.48%**
519. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/providers/providerUtils.kt`** -> AI Confidence: **99.48%**
520. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/resolve/extensions/LLFirResolveExtensionTool.kt`** -> AI Confidence: **99.48%**
521. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/resolver/AllCandidatesResolver.kt`** -> AI Confidence: **99.48%**
522. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/resolver/SingleCandidateResolver.kt`** -> AI Confidence: **99.48%**
523. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/resolver/candidateInfoProviders.kt`** -> AI Confidence: **99.48%**
524. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/resolver/resolverUtils.kt`** -> AI Confidence: **99.48%**
525. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/services/LLFirJavaAnnotationProvider.kt`** -> AI Confidence: **99.48%**
526. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirAbstractSessionFactory.kt`** -> AI Confidence: **99.48%**
527. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirCommonSessionFactory.kt`** -> AI Confidence: **99.48%**
528. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirJsSessionFactory.kt`** -> AI Confidence: **99.48%**
529. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirJvmSessionFactory.kt`** -> AI Confidence: **99.48%**
530. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirNativeSessionFactory.kt`** -> AI Confidence: **99.48%**
531. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirSession.kt`** -> AI Confidence: **99.48%**
532. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirSessionCache.kt`** -> AI Confidence: **99.48%**
533. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirSessionCacheStorageInvalidator.kt`** -> AI Confidence: **99.48%**
534. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/LLFirWasmSessionFactory.kt`** -> AI Confidence: **99.48%**
535. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/sessions/structure/LLSessionStatisticsCalculator.kt`** -> AI Confidence: **99.48%**
536. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/statistics/LLStatisticsService.kt`** -> AI Confidence: **99.48%**
537. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/DeserializedContainerSourceProviders.kt`** -> AI Confidence: **99.48%**
538. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/JvmStubDeserializedBuiltInsContainerSource.kt`** -> AI Confidence: **99.48%**
539. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedAnnotationDeserializer.kt`** -> AI Confidence: **99.48%**
540. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedClassDeserialization.kt`** -> AI Confidence: **99.48%**
541. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedFirContractDeserializer.kt`** -> AI Confidence: **99.48%**
542. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedFirMemberDeserializer.kt`** -> AI Confidence: **99.48%**
543. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/stubBased/deserialization/StubBasedFirTypeDeserializer.kt`** -> AI Confidence: **99.48%**
544. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLDanglingFileDependenciesSymbolProvider.kt`** -> AI Confidence: **99.48%**
545. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLJvmClassFileBasedSymbolProvider.kt`** -> AI Confidence: **99.48%**
546. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinSourceSymbolProvider.kt`** -> AI Confidence: **99.48%**
547. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinStubBasedLibraryMultifileClassPartCallableSymbolProvider.kt`** -> AI Confidence: **99.48%**
548. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinStubBasedLibrarySymbolProvider.kt`** -> AI Confidence: **99.48%**
549. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinSymbolNamesProvider.kt`** -> AI Confidence: **99.48%**
550. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLKotlinSymbolProvider.kt`** -> AI Confidence: **99.48%**
551. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLModuleWithDependenciesSymbolProvider.kt`** -> AI Confidence: **99.48%**
552. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLNativeForwardDeclarationsSymbolProvider.kt`** -> AI Confidence: **99.48%**
553. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/LLSubstitutionScopeKeyFactory.kt`** -> AI Confidence: **99.48%**
554. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/combined/LLCombinedJavaSymbolProvider.kt`** -> AI Confidence: **99.48%**
555. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/combined/LLCombinedKotlinSymbolProvider.kt`** -> AI Confidence: **99.48%**
556. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/combined/LLCombinedPackageDelegationSymbolProvider.kt`** -> AI Confidence: **99.48%**
557. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/combined/LLCombinedSyntheticFunctionSymbolProvider.kt`** -> AI Confidence: **99.48%**
558. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/combined/LLSelectingCombinedSymbolProvider.kt`** -> AI Confidence: **99.48%**
559. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/factories/LLBinaryOriginLibrarySymbolProviderFactory.kt`** -> AI Confidence: **99.48%**
560. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/factories/LLLibrarySymbolProviderFactory.kt`** -> AI Confidence: **99.48%**
561. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/factories/LLStubOriginLibrarySymbolProviderFactory.kt`** -> AI Confidence: **99.48%**
562. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/symbolProviders/utils.kt`** -> AI Confidence: **99.48%**
563. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirAbstractBodyTargetResolver.kt`** -> AI Confidence: **99.48%**
564. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirAnnotationArgumentsLazyResolver.kt`** -> AI Confidence: **99.48%**
565. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirBodyLazyResolver.kt`** -> AI Confidence: **99.48%**
566. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirCompilerAnnotationsLazyResolver.kt`** -> AI Confidence: **99.48%**
567. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirConstantEvaluationLazyResolver.kt`** -> AI Confidence: **99.48%**
568. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirContractsLazyResolver.kt`** -> AI Confidence: **99.48%**
569. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirExpectActualMatcherLazyResolver.kt`** -> AI Confidence: **99.48%**
570. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirImplicitTypesLazyResolver.kt`** -> AI Confidence: **99.48%**
571. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirLazyResolver.kt`** -> AI Confidence: **99.48%**
572. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirReturnTypeCalculatorWithJump.kt`** -> AI Confidence: **99.48%**
573. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirStatusLazyResolver.kt`** -> AI Confidence: **99.48%**
574. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirSupertypeLazyResolver.kt`** -> AI Confidence: **99.48%**
575. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirTargetResolver.kt`** -> AI Confidence: **99.48%**
576. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirTypeLazyResolver.kt`** -> AI Confidence: **99.48%**
577. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLJumpingPhaseComputationSessionForLocalClassesProvider.kt`** -> AI Confidence: **99.48%**
578. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/PostponedSymbolsForAnnotationResolutionAttribute.kt`** -> AI Confidence: **99.48%**
579. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/ContextCollector.kt`** -> AI Confidence: **99.48%**
580. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/FirDeclarationForCompiledElementSearcher.kt`** -> AI Confidence: **99.48%**
581. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/FirElementFinder.kt`** -> AI Confidence: **99.48%**
582. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/ImplementationPlatformKind.kt`** -> AI Confidence: **99.48%**
583. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/LLContainingClassCalculator.kt`** -> AI Confidence: **99.48%**
584. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/LLFlightRecorder.kt`** -> AI Confidence: **99.48%**
585. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/containingFileUtils.kt`** -> AI Confidence: **99.48%**
586. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/declarationUtils.kt`** -> AI Confidence: **99.48%**
587. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/exceptionUtils.kt`** -> AI Confidence: **99.48%**
588. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/firCheckResolvedUtils.kt`** -> AI Confidence: **99.48%**
589. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/stateKeeperUtils.kt`** -> AI Confidence: **99.48%**
590. **`analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/util/utils.kt`** -> AI Confidence: **99.48%**
591. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/AbstractFirLazyDeclarationResolveTestCase.kt`** -> AI Confidence: **99.48%**
592. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/AbstractPartialRawFirBuilderTestCase.kt`** -> AI Confidence: **99.48%**
593. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/TestSuppressor.kt`** -> AI Confidence: **99.48%**
594. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/compiler/based/LLDiagnosticParameterChecker.kt`** -> AI Confidence: **99.48%**
595. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/compiler/based/LLFirPhaseVerifier.kt`** -> AI Confidence: **99.48%**
596. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/compiler/based/LowLevelFirAnalyzerFacade.kt`** -> AI Confidence: **99.48%**
597. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/diagnostic/compiler/based/facades/LLFirAnalyzerFacadeFactoryWithPreresolveInReversedOrder.kt`** -> AI Confidence: **99.48%**
598. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/firTestUtils.kt`** -> AI Confidence: **99.48%**
599. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/resolve/utils.kt`** -> AI Confidence: **99.48%**
600. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/services/ErrorResistanceServiceRegistrar.kt`** -> AI Confidence: **99.48%**
601. **`analysis/low-level-api-fir/testFixtures/org/jetbrains/kotlin/analysis/low/level/api/fir/services/PackagePartProviderTestImpl.kt`** -> AI Confidence: **99.48%**
602. **`analysis/stubs/testFixtures/org/jetbrains/kotlin/analysis/stubs/CompiledStubsTestEngine.kt`** -> AI Confidence: **99.48%**
603. **`analysis/stubs/testFixtures/org/jetbrains/kotlin/analysis/stubs/StubsTestEngine.kt`** -> AI Confidence: **99.48%**
604. **`analysis/stubs/testFixtures/org/jetbrains/kotlin/analysis/stubs/additionalStubInfoExtractor.kt`** -> AI Confidence: **99.48%**
605. **`benchmarks/src/org/jetbrains/kotlin/benchmarks/AbstractSimpleFileBenchmark.kt`** -> AI Confidence: **99.48%**
606. **`build-common/src/org/jetbrains/kotlin/compilerRunner/argumentsToStrings.kt`** -> AI Confidence: **99.48%**
607. **`build-common/src/org/jetbrains/kotlin/idea/explicitDefaultSubstitutors.kt`** -> AI Confidence: **99.48%**
608. **`build-common/src/org/jetbrains/kotlin/incremental/AbstractIncrementalCache.kt`** -> AI Confidence: **99.48%**
609. **`build-common/src/org/jetbrains/kotlin/incremental/ChangesCollector.kt`** -> AI Confidence: **99.48%**
610. **`build-common/src/org/jetbrains/kotlin/incremental/CompilationTransaction.kt`** -> AI Confidence: **99.48%**
611. **`build-common/src/org/jetbrains/kotlin/incremental/IncrementalJsCache.kt`** -> AI Confidence: **99.48%**
612. **`build-common/src/org/jetbrains/kotlin/incremental/IncrementalJvmCache.kt`** -> AI Confidence: **99.48%**
613. **`build-common/src/org/jetbrains/kotlin/incremental/JavaClassesSerializerExtension.kt`** -> AI Confidence: **99.48%**
614. **`build-common/src/org/jetbrains/kotlin/incremental/JavaClassesTrackerImpl.kt`** -> AI Confidence: **99.48%**
615. **`build-common/src/org/jetbrains/kotlin/incremental/KotlinClassInfo.kt`** -> AI Confidence: **99.48%**
616. **`build-common/src/org/jetbrains/kotlin/incremental/LookupStorage.kt`** -> AI Confidence: **99.48%**
617. **`build-common/src/org/jetbrains/kotlin/incremental/buildUtil.kt`** -> AI Confidence: **99.48%**
618. **`build-common/src/org/jetbrains/kotlin/incremental/impl/ExtraClassInfoGenerator.kt`** -> AI Confidence: **99.48%**
619. **`build-common/src/org/jetbrains/kotlin/incremental/protoDifferenceUtils.kt`** -> AI Confidence: **99.48%**
620. **`build-common/src/org/jetbrains/kotlin/incremental/storage/BasicMap.kt`** -> AI Confidence: **99.48%**
621. **`build-common/src/org/jetbrains/kotlin/incremental/storage/ClassOneToManyMap.kt`** -> AI Confidence: **99.48%**
622. **`build-common/src/org/jetbrains/kotlin/incremental/storage/IdToFileMap.kt`** -> AI Confidence: **99.48%**
623. **`build-common/src/org/jetbrains/kotlin/incremental/storage/LazyStorage.kt`** -> AI Confidence: **99.48%**
624. **`build-common/src/org/jetbrains/kotlin/incremental/storage/SourceToOutputMaps.kt`** -> AI Confidence: **99.48%**
625. **`build-common/src/org/jetbrains/kotlin/incremental/storage/externalizers.kt`** -> AI Confidence: **99.48%**
626. **`compiler/android-tests/tests/org/jetbrains/kotlin/android/tests/AndroidTestGenerator.kt`** -> AI Confidence: **99.48%**
627. **`compiler/android-tests/tests/org/jetbrains/kotlin/android/tests/CodegenTestsOnAndroidGenerator.kt`** -> AI Confidence: **99.48%**
628. **`compiler/android-tests/tests/org/jetbrains/kotlin/android/tests/CodegenTestsOnAndroidRunner.kt`** -> AI Confidence: **99.48%**
629. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/CommonCompilerArguments.kt`** -> AI Confidence: **99.48%**
630. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/CommonKlibBasedCompilerArguments.kt`** -> AI Confidence: **99.48%**
631. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/JsCompilerArguments.kt`** -> AI Confidence: **99.48%**
632. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/MetadataCompilerArguments.kt`** -> AI Confidence: **99.48%**
633. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/NativeCompilerArguments.kt`** -> AI Confidence: **99.48%**
634. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/WasmCompilerArguments.kt`** -> AI Confidence: **99.48%**
635. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/removed/removedJsCompilerArguments.kt`** -> AI Confidence: **99.48%**
636. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/description/removed/removedJvmCompilerArguments.kt`** -> AI Confidence: **99.48%**
637. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/serialization/json/ReleaseDependentSerializer.kt`** -> AI Confidence: **99.48%**
638. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/serialization/json/base/AllNamedTypeSerializer.kt`** -> AI Confidence: **99.48%**
639. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/serialization/json/base/SetTypeSerializer.kt`** -> AI Confidence: **99.48%**
640. **`compiler/arguments/src/org/jetbrains/kotlin/arguments/serialization/json/kotlinReleaseVersionSerializers.kt`** -> AI Confidence: **99.48%**
641. **`compiler/backend.common.jvm/src/org/jetbrains/kotlin/types/AbstractTypeMapper.kt`** -> AI Confidence: **99.48%**
642. **`compiler/backend/src/org/jetbrains/kotlin/codegen/AssertCodegenUtil.kt`** -> AI Confidence: **99.48%**
643. **`compiler/backend/src/org/jetbrains/kotlin/codegen/ClassFileFactory.kt`** -> AI Confidence: **99.48%**
644. **`compiler/backend/src/org/jetbrains/kotlin/codegen/JvmBackendClassResolver.kt`** -> AI Confidence: **99.48%**
645. **`compiler/backend/src/org/jetbrains/kotlin/codegen/OriginCollectingClassBuilderFactory.kt`** -> AI Confidence: **99.48%**
646. **`compiler/backend/src/org/jetbrains/kotlin/codegen/StringConcatGenerator.kt`** -> AI Confidence: **99.48%**
647. **`compiler/backend/src/org/jetbrains/kotlin/codegen/TransformationMethodVisitor.kt`** -> AI Confidence: **99.48%**
648. **`compiler/backend/src/org/jetbrains/kotlin/codegen/classFileUtils.kt`** -> AI Confidence: **99.48%**
649. **`compiler/backend/src/org/jetbrains/kotlin/codegen/codegenUtil.kt`** -> AI Confidence: **99.48%**
650. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/ChangeBoxingMethodTransformer.kt`** -> AI Confidence: **99.48%**
651. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/CoroutineTransformerMethodVisitor.kt`** -> AI Confidence: **99.48%**
652. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/GeneratedCodeMarkers.kt`** -> AI Confidence: **99.48%**
653. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/RedundantLocalsEliminationMethodTransformer.kt`** -> AI Confidence: **99.48%**
654. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/SpilledVariableFieldTypesAnalysis.kt`** -> AI Confidence: **99.48%**
655. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/SuspendFunctionGenerationStrategy.kt`** -> AI Confidence: **99.48%**
656. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/TailCallOptimization.kt`** -> AI Confidence: **99.48%**
657. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/coroutineCodegenUtil.kt`** -> AI Confidence: **99.48%**
658. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/processUninitializedStores.kt`** -> AI Confidence: **99.48%**
659. **`compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/resumePointDependentAnalysis.kt`** -> AI Confidence: **99.48%**
660. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/AnonymousObjectTransformer.kt`** -> AI Confidence: **99.48%**
661. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/LambdaInfo.kt`** -> AI Confidence: **99.48%**
662. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/LocalVarRemapper.kt`** -> AI Confidence: **99.48%**
663. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MethodInliner.kt`** -> AI Confidence: **99.48%**
664. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MethodInlinerUtil.kt`** -> AI Confidence: **99.48%**
665. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/ObjectTransformer.kt`** -> AI Confidence: **99.48%**
666. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/RegeneratedLambdaFieldRemapper.kt`** -> AI Confidence: **99.48%**
667. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/ReifiedTypeInliner.kt`** -> AI Confidence: **99.48%**
668. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/SMAPBuilder.kt`** -> AI Confidence: **99.48%**
669. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/SourceCompilerForInline.kt`** -> AI Confidence: **99.48%**
670. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/coroutines/CoroutineTransformer.kt`** -> AI Confidence: **99.48%**
671. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/defaultMethodUtil.kt`** -> AI Confidence: **99.48%**
672. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/inlineCodegenUtils.kt`** -> AI Confidence: **99.48%**
673. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/inlineIntrinsics.kt`** -> AI Confidence: **99.48%**
674. **`compiler/backend/src/org/jetbrains/kotlin/codegen/inline/typeOf.kt`** -> AI Confidence: **99.48%**
675. **`compiler/backend/src/org/jetbrains/kotlin/codegen/intrinsics/TypeIntrinsics.kt`** -> AI Confidence: **99.48%**
676. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/CapturedVarsOptimizationMethodTransformer.kt`** -> AI Confidence: **99.48%**
677. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/ConstantConditionEliminationMethodTransformer.kt`** -> AI Confidence: **99.48%**
678. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/DeadCodeEliminationMethodTransformer.kt`** -> AI Confidence: **99.48%**
679. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/OptimizationMethodVisitor.kt`** -> AI Confidence: **99.48%**
680. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/RedundantCheckCastElimination.kt`** -> AI Confidence: **99.48%**
681. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/RedundantNopsCleanupMethodTransformer.kt`** -> AI Confidence: **99.48%**
682. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/BoxedBasicValue.kt`** -> AI Confidence: **99.48%**
683. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/BoxingInterpreter.kt`** -> AI Confidence: **99.48%**
684. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/PopBackwardPropagationTransformer.kt`** -> AI Confidence: **99.48%**
685. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/RedundantBoxingInterpreter.kt`** -> AI Confidence: **99.48%**
686. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/RedundantBoxingMethodTransformer.kt`** -> AI Confidence: **99.48%**
687. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/boxing/StackPeepholeOptimizationsTransformer.kt`** -> AI Confidence: **99.48%**
688. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/common/FastAnalyzer.kt`** -> AI Confidence: **99.48%**
689. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/common/Util.kt`** -> AI Confidence: **99.48%**
690. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/AnalyzeTryCatchBlocks.kt`** -> AI Confidence: **99.48%**
691. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/BasicTypeInterpreter.kt`** -> AI Confidence: **99.48%**
692. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/FixStackAnalyzer.kt`** -> AI Confidence: **99.48%**
693. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/FixStackContext.kt`** -> AI Confidence: **99.48%**
694. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/fixStack/FixStackMethodTransformer.kt`** -> AI Confidence: **99.48%**
695. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/nullCheck/NullabilityInterpreter.kt`** -> AI Confidence: **99.48%**
696. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/nullCheck/RedundantNullCheckMethodTransformer.kt`** -> AI Confidence: **99.48%**
697. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/temporaryVals/FastStoreLoadAnalyzer.kt`** -> AI Confidence: **99.48%**
698. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/temporaryVals/TemporaryVals.kt`** -> AI Confidence: **99.48%**
699. **`compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/temporaryVals/TemporaryVariablesEliminationTransformer.kt`** -> AI Confidence: **99.48%**
700. **`compiler/backend/src/org/jetbrains/kotlin/codegen/serialization/JvmCodegenStringTable.kt`** -> AI Confidence: **99.48%**
701. **`compiler/backend/src/org/jetbrains/kotlin/codegen/serialization/JvmSerializerExtension.kt`** -> AI Confidence: **99.48%**
702. **`compiler/backend/src/org/jetbrains/kotlin/codegen/state/GenerationState.kt`** -> AI Confidence: **99.48%**
703. **`compiler/backend/src/org/jetbrains/kotlin/codegen/state/KotlinTypeMapper.kt`** -> AI Confidence: **99.48%**
704. **`compiler/backend/src/org/jetbrains/kotlin/codegen/state/inlineClassManglingUtils.kt`** -> AI Confidence: **99.48%**
705. **`compiler/backend/src/org/jetbrains/kotlin/codegen/state/typeMappingUtil.kt`** -> AI Confidence: **99.48%**
706. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/CompilerArgumentCompatibilityTest.kt`** -> AI Confidence: **99.48%**
707. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/AbiStabilityModeConversionTest.kt`** -> AI Confidence: **99.48%**
708. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/AddModulesConversionTest.kt`** -> AI Confidence: **99.48%**
709. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/AnnotationDefaultTargetModeConversionTest.kt`** -> AI Confidence: **99.48%**
710. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/AssertionsModeConversionTest.kt`** -> AI Confidence: **99.48%**
711. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/ClasspathConversionTest.kt`** -> AI Confidence: **99.48%**
712. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/CompatqualAnnotationsModeConversionTest.kt`** -> AI Confidence: **99.48%**
713. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/DisablePhasesConversionTest.kt`** -> AI Confidence: **99.48%**
714. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/DumpDirectoryConversionTest.kt`** -> AI Confidence: **99.48%**
715. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/DumpPerfConversionTest.kt`** -> AI Confidence: **99.48%**
716. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/FriendPathsConversionTest.kt`** -> AI Confidence: **99.48%**
717. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/JavaSourceRootsConversionTest.kt`** -> AI Confidence: **99.48%**
718. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/JdkHomeConversionTest.kt`** -> AI Confidence: **99.48%**
719. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/JdkReleaseConversionTest.kt`** -> AI Confidence: **99.48%**
720. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/JspecifyAnnotationsModeConversionTest.kt`** -> AI Confidence: **99.48%**
721. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/Jsr305ConversionTest.kt`** -> AI Confidence: **99.48%**
722. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/JvmDefaultModeConversionTest.kt`** -> AI Confidence: **99.48%**
723. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/KlibConversionTest.kt`** -> AI Confidence: **99.48%**
724. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/KotlinHomeConversionTest.kt`** -> AI Confidence: **99.48%**
725. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/LambdasModeConversionTest.kt`** -> AI Confidence: **99.48%**
726. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/ModulePathConversionTest.kt`** -> AI Confidence: **99.48%**
727. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/NameBasedDestructuringModeConversionTest.kt`** -> AI Confidence: **99.48%**
728. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/NullabilityAnnotationsConversionTest.kt`** -> AI Confidence: **99.48%**
729. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/OptInConversionTest.kt`** -> AI Confidence: **99.48%**
730. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/PhasesToDumpAfterConversionTest.kt`** -> AI Confidence: **99.48%**
731. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/PhasesToDumpBeforeConversionTest.kt`** -> AI Confidence: **99.48%**
732. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/PhasesToDumpConversionTest.kt`** -> AI Confidence: **99.48%**
733. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/PhasesToValidateAfterConversionTest.kt`** -> AI Confidence: **99.48%**
734. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/PhasesToValidateBeforeConversionTest.kt`** -> AI Confidence: **99.48%**
735. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/PhasesToValidateConversionTest.kt`** -> AI Confidence: **99.48%**
736. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/ProfileCompilerCommandConversionTest.kt`** -> AI Confidence: **99.48%**
737. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/SamConversionsModeConversionTest.kt`** -> AI Confidence: **99.48%**
738. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/ScriptResolverEnvironmentConversionTest.kt`** -> AI Confidence: **99.48%**
739. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/ScriptTemplatesConversionTest.kt`** -> AI Confidence: **99.48%**
740. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/StringConcatModeConversionTest.kt`** -> AI Confidence: **99.48%**
741. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/SuppressWarningConversionTest.kt`** -> AI Confidence: **99.48%**
742. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/VerbosePhasesConversionTest.kt`** -> AI Confidence: **99.48%**
743. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/VerifyIrModeConversionTest.kt`** -> AI Confidence: **99.48%**
744. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/WarningLevelConfigConversionTest.kt`** -> AI Confidence: **99.48%**
745. **`compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/WhenExpressionsModeConversionTest.kt`** -> AI Confidence: **99.48%**
746. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/BaseCompilationTest.kt`** -> AI Confidence: **99.48%**
747. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/assertions/filesAssertions.kt`** -> AI Confidence: **99.48%**
748. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/AbstractModule.kt`** -> AI Confidence: **99.48%**
749. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/BtaV2StrategyAgnosticCompilationTestArgumentProvider.kt`** -> AI Confidence: **99.48%**
750. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/BtaVersionsCompilationTestArgumentProvider.kt`** -> AI Confidence: **99.48%**
751. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/DefaultStrategyAgnosticCompilationTestArgumentProvider.kt`** -> AI Confidence: **99.48%**
752. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/JvmModule.kt`** -> AI Confidence: **99.48%**
753. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/Project.kt`** -> AI Confidence: **99.48%**
754. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/scenario/dslModuleCache.kt`** -> AI Confidence: **99.48%**
755. **`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/scenario/scenarioDsl.kt`** -> AI Confidence: **99.48%**
756. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testBuildMetrics/kotlin/MetricsTestUtilities.kt`** -> AI Confidence: **99.48%**
757. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testBuildMetrics/kotlin/SmokeCompilationMetricsTest.kt`** -> AI Confidence: **99.48%**
758. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testBuildMetrics/kotlin/SmokeJvmClasspathSnapshottingMetricsTest.kt`** -> AI Confidence: **99.48%**
759. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/BtaClassesClashTest.kt`** -> AI Confidence: **99.48%**
760. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/CancellationCompatibilitySmokeTest.kt`** -> AI Confidence: **99.48%**
761. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/ExampleCompatibilityCompilationTest.kt`** -> AI Confidence: **99.48%**
762. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/IncrementalCompilationSmokeTest.kt`** -> AI Confidence: **99.48%**
763. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/LookupTrackerTest.kt`** -> AI Confidence: **99.48%**
764. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/NonIncrementalCompilationSmokeTest.kt`** -> AI Confidence: **99.48%**
765. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/AbiStabilityModeConversionTest.kt`** -> AI Confidence: **99.48%**
766. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/AddModulesConversionTest.kt`** -> AI Confidence: **99.48%**
767. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/AnnotationDefaultTargetModeConversionTest.kt`** -> AI Confidence: **99.48%**
768. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/AssertionsModeConversionTest.kt`** -> AI Confidence: **99.48%**
769. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/BaseArgumentTest.kt`** -> AI Confidence: **99.48%**
770. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/ClasspathConversionTest.kt`** -> AI Confidence: **99.48%**
771. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/CompatqualAnnotationsModeConversionTest.kt`** -> AI Confidence: **99.48%**
772. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/DisablePhasesConversionTest.kt`** -> AI Confidence: **99.48%**
773. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/DumpDirectoryConversionTest.kt`** -> AI Confidence: **99.48%**
774. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/DumpPerfConversionTest.kt`** -> AI Confidence: **99.48%**
775. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/FriendPathsConversionTest.kt`** -> AI Confidence: **99.48%**
776. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/IgnoredAnnotationsForBridgesConversionTest.kt`** -> AI Confidence: **99.48%**
777. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/JavaSourceRootsConversionTest.kt`** -> AI Confidence: **99.48%**
778. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/JdkHomeConversionTest.kt`** -> AI Confidence: **99.48%**
779. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/JdkReleaseConversionTest.kt`** -> AI Confidence: **99.48%**
780. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/JspecifyAnnotationsModeConversionTest.kt`** -> AI Confidence: **99.48%**
781. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/Jsr305ConversionTest.kt`** -> AI Confidence: **99.48%**
782. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/JvmDefaultModeConversionTest.kt`** -> AI Confidence: **99.48%**
783. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/KlibConversionTest.kt`** -> AI Confidence: **99.48%**
784. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/KotlinHomeConversionTest.kt`** -> AI Confidence: **99.48%**
785. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/LambdasModeConversionTest.kt`** -> AI Confidence: **99.48%**
786. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/ModulePathConversionTest.kt`** -> AI Confidence: **99.48%**
787. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/NameBasedDestructuringModeConversionTest.kt`** -> AI Confidence: **99.48%**
788. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/NullabilityAnnotationsConversionTest.kt`** -> AI Confidence: **99.48%**
789. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/OptInConversionTest.kt`** -> AI Confidence: **99.48%**
790. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/PhasesToDumpAfterConversionTest.kt`** -> AI Confidence: **99.48%**
791. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/PhasesToDumpBeforeConversionTest.kt`** -> AI Confidence: **99.48%**
792. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/PhasesToDumpConversionTest.kt`** -> AI Confidence: **99.48%**
793. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/PhasesToValidateAfterConversionTest.kt`** -> AI Confidence: **99.48%**
794. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/PhasesToValidateBeforeConversionTest.kt`** -> AI Confidence: **99.48%**
795. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/PhasesToValidateConversionTest.kt`** -> AI Confidence: **99.48%**
796. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/ProfileCompilerCommandConversionTest.kt`** -> AI Confidence: **99.48%**
797. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/SamConversionsModeConversionTest.kt`** -> AI Confidence: **99.48%**
798. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/ScriptResolverEnvironmentConversionTest.kt`** -> AI Confidence: **99.48%**
799. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/ScriptTemplatesConversionTest.kt`** -> AI Confidence: **99.48%**
800. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/StringConcatModeConversionTest.kt`** -> AI Confidence: **99.48%**
801. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/SuppressWarningConversionTest.kt`** -> AI Confidence: **99.48%**
802. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/VerbosePhasesConversionTest.kt`** -> AI Confidence: **99.48%**
803. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/VerifyIrModeConversionTest.kt`** -> AI Confidence: **99.48%**
804. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/WarningLevelConfigConversionTest.kt`** -> AI Confidence: **99.48%**
805. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompatibility/kotlin/arguments/WhenExpressionsModeConversionTest.kt`** -> AI Confidence: **99.48%**
806. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompilerPlugins/kotlin/CompilerPluginsConfigurationInputsTrackingTest.kt`** -> AI Confidence: **99.48%**
807. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompilerPlugins/kotlin/CompilerPluginsCustomArgumentConfigurationTest.kt`** -> AI Confidence: **99.48%**
808. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompilerPlugins/kotlin/CompilerPluginsCustomArgumentSmokeTest.kt`** -> AI Confidence: **99.48%**
809. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCompilerPlugins/kotlin/ScriptingTest.kt`** -> AI Confidence: **99.48%**
810. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCrossModuleIncrementalChanges/kotlin/ClasspathSnapshottingWithDebugInfoTest.kt`** -> AI Confidence: **99.48%**
811. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCrossModuleIncrementalChanges/kotlin/InlinedLambdaChangeTest.kt`** -> AI Confidence: **99.48%**
812. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testCrossModuleIncrementalChanges/kotlin/RegularInlineFunTest.kt`** -> AI Confidence: **99.48%**
813. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testDaemonOptions/kotlin/DaemonLogConfigurationTest.kt`** -> AI Confidence: **99.48%**
814. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testDefaultOptions/kotlin/JvmSnapshotBasedIncrementalCompilationConfigurationDefaultsTest.kt`** -> AI Confidence: **99.48%**
815. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testEscapableCharacters/kotlin/EscapableCharactersInPathTest.kt`** -> AI Confidence: **99.48%**
816. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testFirRunner/kotlin/ClassicMultiprojectFirRunnerIncrementalTest.kt`** -> AI Confidence: **99.48%**
817. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testFirRunner/kotlin/SingleModuleFirRunnerIncrementalTest.kt`** -> AI Confidence: **99.48%**
818. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testInputChangesTracking/kotlin/ConfigurationInputsTrackingTest.kt`** -> AI Confidence: **99.48%**
819. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testKotlinLogger/kotlin/KotlinLoggerCustomRendererTest.kt`** -> AI Confidence: **99.48%**
820. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testKotlinLogger/kotlin/KotlinLoggerSeverityRoutingTest.kt`** -> AI Confidence: **99.48%**
821. **`compiler/build-tools/kotlin-build-tools-api-tests/src/testKotlinLogger/kotlin/KotlinLoggerSeverityWerrorTest.kt`** -> AI Confidence: **99.48%**
822. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/CompilationService.kt`** -> AI Confidence: **99.48%**
823. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/KotlinToolchains.kt`** -> AI Confidence: **99.48%**
824. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/internal/wrappers/KotlinWrapperPre2_3_20.kt`** -> AI Confidence: **99.48%**
825. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/internal/wrappers/KotlinWrapperPre2_4_0.kt`** -> AI Confidence: **99.48%**
826. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/jvm/JvmPlatformToolchain.kt`** -> AI Confidence: **99.48%**
827. **`compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/jvm/operations/JvmCompilationOperation.kt`** -> AI Confidence: **99.48%**
828. **`compiler/build-tools/kotlin-build-tools-compat/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/compat/KotlinToolchainsV1Adapter.kt`** -> AI Confidence: **99.48%**
829. **`compiler/build-tools/kotlin-build-tools-cri-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/cri/CriDataDeserializerImpl.kt`** -> AI Confidence: **99.48%**
830. **`compiler/build-tools/kotlin-build-tools-cri-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/cri/CriDataSerializerImpl.kt`** -> AI Confidence: **99.48%**
831. **`compiler/build-tools/kotlin-build-tools-cri-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/cri/dataEntries.kt`** -> AI Confidence: **99.48%**
832. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/BuildOperationImpl.kt`** -> AI Confidence: **99.48%**
833. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/BuildToolsApiBuildICReporter.kt`** -> AI Confidence: **99.48%**
834. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/CancellableBuildOperationImpl.kt`** -> AI Confidence: **99.48%**
835. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/ClasspathEntrySnapshotImpl.kt`** -> AI Confidence: **99.48%**
836. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/CompilationServiceImpl.kt`** -> AI Confidence: **99.48%**
837. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/KotlinToolchainsImpl.kt`** -> AI Confidence: **99.48%**
838. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/arguments/CompilerArgumentValueAdapter.kt`** -> AI Confidence: **99.48%**
839. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/cri/CriFileIdToPathDataDeserializationOperationImpl.kt`** -> AI Confidence: **99.48%**
840. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/cri/CriLookupDataDeserializationOperationImpl.kt`** -> AI Confidence: **99.48%**
841. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/cri/CriSubtypeDataDeserializationOperationImpl.kt`** -> AI Confidence: **99.48%**
842. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/daemonAdapters.kt`** -> AI Confidence: **99.48%**
843. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/executionPolicyImpls.kt`** -> AI Confidence: **99.48%**
844. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/icAdapters.kt`** -> AI Confidence: **99.48%**
845. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/jvm/JvmPlatformToolchainImpl.kt`** -> AI Confidence: **99.48%**
846. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/jvm/JvmSnapshotBasedIncrementalCompilationConfigurationImpl.kt`** -> AI Confidence: **99.48%**
847. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/jvm/operations/DiscoverScriptExtensionsOperationImpl.kt`** -> AI Confidence: **99.48%**
848. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/jvm/operations/JvmClasspathSnapshottingOperationImpl.kt`** -> AI Confidence: **99.48%**
849. **`compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/jvm/operations/JvmCompilationOperationImpl.kt`** -> AI Confidence: **99.48%**
850. **`compiler/build-tools/kotlin-build-tools-impl/src/test/kotlin/CancellableOperationTest.kt`** -> AI Confidence: **99.48%**
851. **`compiler/build-tools/kotlin-build-tools-impl/src/test/kotlin/KotlinLoggerMessageCollectorAdapterTest.kt`** -> AI Confidence: **99.48%**
852. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/BtaApiGenerator.kt`** -> AI Confidence: **99.48%**
853. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/BtaCompilerArgument.kt`** -> AI Confidence: **99.48%**
854. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/BtaImplGenerator.kt`** -> AI Confidence: **99.48%**
855. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/Main.kt`** -> AI Confidence: **99.48%**
856. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/argumentTransforms.kt`** -> AI Confidence: **99.48%**
857. **`compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/constantsAndUtils.kt`** -> AI Confidence: **99.48%**
858. **`compiler/cli/cli-arguments-generator/src/org/jetbrains/kotlin/cli/arguments/generator/Main.kt`** -> AI Confidence: **99.48%**
859. **`compiler/cli/cli-base/src/com/intellij/mock/MockProject.kt`** -> AI Confidence: **99.48%**
860. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/CompilerConfigurationCreation.kt`** -> AI Confidence: **99.48%**
861. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/arguments/argumentUtils.kt`** -> AI Confidence: **99.48%**
862. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/arguments/parseCommandLineArguments.kt`** -> AI Confidence: **99.48%**
863. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/moduleVisibilityImpl.kt`** -> AI Confidence: **99.48%**
864. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/repl/KotlinJsr223JvmInvocableScriptEngine.kt`** -> AI Confidence: **99.48%**
865. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/common/repl/ReplApi.kt`** -> AI Confidence: **99.48%**
866. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/ClasspathRootsResolver.kt`** -> AI Confidence: **99.48%**
867. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/CliKotlinAsJavaSupport.kt`** -> AI Confidence: **99.48%**
868. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/CliLightClassGenerationSupport.kt`** -> AI Confidence: **99.48%**
869. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/CliTrace.kt`** -> AI Confidence: **99.48%**
870. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/CliVirtualFileFinder.kt`** -> AI Confidence: **99.48%**
871. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/JvmPackagePartProvider.kt`** -> AI Confidence: **99.48%**
872. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/KotlinCliJavaFileManagerImpl.kt`** -> AI Confidence: **99.48%**
873. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/KotlinCoreApplicationEnvironment.kt`** -> AI Confidence: **99.48%**
874. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/KotlinCoreEnvironment.kt`** -> AI Confidence: **99.48%**
875. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/coreEnvironmentUtils.kt`** -> AI Confidence: **99.48%**
876. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/jarfs/FastJarFileSystem.kt`** -> AI Confidence: **99.48%**
877. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/jarfs/FastJarHandler.kt`** -> AI Confidence: **99.48%**
878. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/jarfs/FastJarVirtualFile.kt`** -> AI Confidence: **99.48%**
879. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/config/JvmContentRoots.kt`** -> AI Confidence: **99.48%**
880. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/index/JvmDependenciesIndexImpl.kt`** -> AI Confidence: **99.48%**
881. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/index/SingleJavaFileRootsIndex.kt`** -> AI Confidence: **99.48%**
882. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/modules/CliJavaModuleFinder.kt`** -> AI Confidence: **99.48%**
883. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/modules/CliJavaModuleResolver.kt`** -> AI Confidence: **99.48%**
884. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/modules/CoreJrtFileSystem.kt`** -> AI Confidence: **99.48%**
885. **`compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/modules/CoreJrtVirtualFile.kt`** -> AI Confidence: **99.48%**
886. **`compiler/cli/cli-jklib/src/org/jetbrains/kotlin/cli/jklib/FirJKlibSessionFactory.kt`** -> AI Confidence: **99.48%**
887. **`compiler/cli/cli-jklib/src/org/jetbrains/kotlin/cli/jklib/K2JKlibCompiler.kt`** -> AI Confidence: **99.48%**
888. **`compiler/cli/cli-jklib/src/org/jetbrains/kotlin/cli/jklib/pipeline/JKlibCliPipeline.kt`** -> AI Confidence: **99.48%**
889. **`compiler/cli/cli-jklib/src/org/jetbrains/kotlin/cli/jklib/pipeline/JKlibPipelinePhases.kt`** -> AI Confidence: **99.48%**
890. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/Helpers.kt`** -> AI Confidence: **99.48%**
891. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/IcCaches.kt`** -> AI Confidence: **99.48%**
892. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/K2JSCompiler.kt`** -> AI Confidence: **99.48%**
893. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/K2JsCompilerImpl.kt`** -> AI Confidence: **99.48%**
894. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/KotlinWasmCompiler.kt`** -> AI Confidence: **99.48%**
895. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/KotlinWebCompilerBase.kt`** -> AI Confidence: **99.48%**
896. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/klib/TopDownAnalyzerFacadeForJSIR.kt`** -> AI Confidence: **99.48%**
897. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/klib/TopDownAnalyzerFacadeForWasm.kt`** -> AI Confidence: **99.48%**
898. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/js/klib/prepareAnalyzedSourceModule.kt`** -> AI Confidence: **99.48%**
899. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebBackendPipelinePhase.kt`** -> AI Confidence: **99.48%**
900. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebCliPipeline.kt`** -> AI Confidence: **99.48%**
901. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebConfigurationPhase.kt`** -> AI Confidence: **99.48%**
902. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebFir2IrPipelinePhase.kt`** -> AI Confidence: **99.48%**
903. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebFrontendPipelinePhase.kt`** -> AI Confidence: **99.48%**
904. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebKlibInliningPipelinePhase.kt`** -> AI Confidence: **99.48%**
905. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebKlibSerializationPipelinePhase.kt`** -> AI Confidence: **99.48%**
906. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/WebPipelineArtifacts.kt`** -> AI Confidence: **99.48%**
907. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/js/JsBackendPipelinePhase.kt`** -> AI Confidence: **99.48%**
908. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/js/JsConfigurationUpdater.kt`** -> AI Confidence: **99.48%**
909. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/wasm/KotlinIr2WasmIrCompiler.kt`** -> AI Confidence: **99.48%**
910. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/wasm/KotlinIr2WasmIrCompilerIC.kt`** -> AI Confidence: **99.48%**
911. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/wasm/WasmBackendPipelinePhase.kt`** -> AI Confidence: **99.48%**
912. **`compiler/cli/cli-js/src/org/jetbrains/kotlin/cli/pipeline/web/wasm/WasmConfigurationUpdater.kt`** -> AI Confidence: **99.48%**
913. **`compiler/cli/cli-jvm/javac-integration/src/org/jetbrains/kotlin/cli/jvm/javac/JavacLogger.kt`** -> AI Confidence: **99.48%**
914. **`compiler/cli/cli-jvm/javac-integration/src/org/jetbrains/kotlin/cli/jvm/javac/JavacWrapperKotlinResolverImpl.kt`** -> AI Confidence: **99.48%**
915. **`compiler/cli/cli-jvm/javac-integration/src/org/jetbrains/kotlin/cli/jvm/javac/JavacWrapperRegistrar.kt`** -> AI Confidence: **99.48%**
916. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/common/FirJvmSessionConstructionUtils.kt`** -> AI Confidence: **99.48%**
917. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/K2JVMCompiler.kt`** -> AI Confidence: **99.48%**
918. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/KotlinToJVMBytecodeCompiler.kt`** -> AI Confidence: **99.48%**
919. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/TopDownAnalyzerFacadeForJVM.kt`** -> AI Confidence: **99.48%**
920. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/cliCompilerUtils.kt`** -> AI Confidence: **99.48%**
921. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/findMainClass.kt`** -> AI Confidence: **99.48%**
922. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/firFindMainClass.kt`** -> AI Confidence: **99.48%**
923. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/legacy/pipeline/jvmCompilerPipeline.kt`** -> AI Confidence: **99.48%**
924. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/compiler/legacy/pipeline/jvmIncrementalCompilerPipelineLightTree.kt`** -> AI Confidence: **99.48%**
925. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/jvmArguments.kt`** -> AI Confidence: **99.48%**
926. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmBackendPipelinePhase.kt`** -> AI Confidence: **99.48%**
927. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmCliPipeline.kt`** -> AI Confidence: **99.48%**
928. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmConfigurationPipelinePhase.kt`** -> AI Confidence: **99.48%**
929. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFir2IrPipelinePhase.kt`** -> AI Confidence: **99.48%**
930. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFrontendPipelinePhase.kt`** -> AI Confidence: **99.48%**
931. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmPipelineArtifacts.kt`** -> AI Confidence: **99.48%**
932. **`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmScriptPipelineStep.kt`** -> AI Confidence: **99.48%**
933. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/AbstractMetadataSerializer.kt`** -> AI Confidence: **99.48%**
934. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/CommonAnalysis.kt`** -> AI Confidence: **99.48%**
935. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/K1LegacyMetadataSerializer.kt`** -> AI Confidence: **99.48%**
936. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/K1MetadataKlibSerializer.kt`** -> AI Confidence: **99.48%**
937. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/KotlinMetadataCompiler.kt`** -> AI Confidence: **99.48%**
938. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/pipeline/metadata/MetadataCliPipeline.kt`** -> AI Confidence: **99.48%**
939. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/pipeline/metadata/MetadataConfigurationPipelinePhase.kt`** -> AI Confidence: **99.48%**
940. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/pipeline/metadata/MetadataFrontendPipelinePhase.kt`** -> AI Confidence: **99.48%**
941. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/pipeline/metadata/MetadataKlibSerializerPhase.kt`** -> AI Confidence: **99.48%**
942. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/pipeline/metadata/MetadataLegacySerializerPhase.kt`** -> AI Confidence: **99.48%**
943. **`compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/pipeline/metadata/MetadataPipelineArtifacts.kt`** -> AI Confidence: **99.48%**
944. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/Fir2Ir.kt`** -> AI Confidence: **99.48%**
945. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/FirNativeSerializer.kt`** -> AI Confidence: **99.48%**
946. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/NativeFir2IrExtensions.kt`** -> AI Confidence: **99.48%**
947. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/NativeFirstStageCompilationConfig.kt`** -> AI Confidence: **99.48%**
948. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/PreSerializingLowerings.kt`** -> AI Confidence: **99.48%**
949. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeConfigurationPhase.kt`** -> AI Confidence: **99.48%**
950. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeFir2IrPipelinePhase.kt`** -> AI Confidence: **99.48%**
951. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeFrontendPipelinePhase.kt`** -> AI Confidence: **99.48%**
952. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeKlibCliPipeline.kt`** -> AI Confidence: **99.48%**
953. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeKlibIrPhase.kt`** -> AI Confidence: **99.48%**
954. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/pipeline/NativeKlibPipelineArtifacts.kt`** -> AI Confidence: **99.48%**
955. **`compiler/cli/cli-native-klib/src/main/kotlin/org/jetbrains/kotlin/native/writeKlib.kt`** -> AI Confidence: **99.48%**
956. **`compiler/cli/cli-runner/src/org/jetbrains/kotlin/runner/runners.kt`** -> AI Confidence: **99.48%**
957. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/CLICompiler.kt`** -> AI Confidence: **99.48%**
958. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/FirSessionConstructionUtils.kt`** -> AI Confidence: **99.48%**
959. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/GroupedKtSources.kt`** -> AI Confidence: **99.48%**
960. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/arguments.kt`** -> AI Confidence: **99.48%**
961. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/fir/FirDiagnosticsCompilerResultsReporter.kt`** -> AI Confidence: **99.48%**
962. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/klibArguments.kt`** -> AI Confidence: **99.48%**
963. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/messages/AnalyzerWithCompilerReport.kt`** -> AI Confidence: **99.48%**
964. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/messages/PlainTextMessageRenderer.kt`** -> AI Confidence: **99.48%**
965. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/output/outputUtils.kt`** -> AI Confidence: **99.48%**
966. **`compiler/cli/src/org/jetbrains/kotlin/cli/common/utils.kt`** -> AI Confidence: **99.48%**
967. **`compiler/cli/src/org/jetbrains/kotlin/cli/jvm/compiler/IncrementalCompilationContextUtils.kt`** -> AI Confidence: **99.48%**
968. **`compiler/cli/src/org/jetbrains/kotlin/cli/jvm/compiler/VfsBasedProjectEnvironment.kt`** -> AI Confidence: **99.48%**
969. **`compiler/cli/src/org/jetbrains/kotlin/cli/jvm/plugins/PluginCliParser.kt`** -> AI Confidence: **99.48%**
970. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/AbstractCliPipeline.kt`** -> AI Confidence: **99.48%**
971. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/AbstractConfigurationPhase.kt`** -> AI Confidence: **99.48%**
972. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/FrontendFilesForPluginsGenerationPipelinePhase.kt`** -> AI Confidence: **99.48%**
973. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/PipelineActions.kt`** -> AI Confidence: **99.48%**
974. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/PipelineArtifacts.kt`** -> AI Confidence: **99.48%**
975. **`compiler/cli/src/org/jetbrains/kotlin/cli/pipeline/PipelinePhase.kt`** -> AI Confidence: **99.48%**
976. **`compiler/compiler-runner-unshaded/src/org/jetbrains/kotlin/compilerRunner/CompilerOutputParser.kt`** -> AI Confidence: **99.48%**
977. **`compiler/compiler-runner-unshaded/src/org/jetbrains/kotlin/compilerRunner/KotlinCompilerRunnerUtils.kt`** -> AI Confidence: **99.48%**
978. **`compiler/config/configuration-keys-generator/src/org/jetbrains/kotlin/config/keys/generator/CommonConfigurationKeysContainer.kt`** -> AI Confidence: **99.48%**
979. **`compiler/config/configuration-keys-generator/src/org/jetbrains/kotlin/config/keys/generator/model/KeysContainer.kt`** -> AI Confidence: **99.48%**
980. **`compiler/config/configuration-keys-generator/src/org/jetbrains/kotlin/config/keys/generator/model/KeysContainerGenerator.kt`** -> AI Confidence: **99.48%**
981. **`compiler/container/src/org/jetbrains/kotlin/container/Storage.kt`** -> AI Confidence: **99.48%**
982. **`compiler/daemon/daemon-client/src/main/kotlin/BasicCompilerServicesWithResultsFacadeServer.kt`** -> AI Confidence: **99.48%**
983. **`compiler/daemon/daemon-client/src/main/kotlin/CompilerCallbackServicesFacadeServer.kt`** -> AI Confidence: **99.48%**
984. **`compiler/daemon/daemon-client/src/main/kotlin/KotlinCompilerClient.kt`** -> AI Confidence: **99.48%**
985. **`compiler/daemon/daemon-common/src/org/jetbrains/kotlin/daemon/common/CompilationOptions.kt`** -> AI Confidence: **99.48%**
986. **`compiler/daemon/daemon-common/src/org/jetbrains/kotlin/daemon/common/CompileService.kt`** -> AI Confidence: **99.48%**
987. **`compiler/daemon/daemon-common/src/org/jetbrains/kotlin/daemon/common/DaemonParams.kt`** -> AI Confidence: **99.48%**
988. **`compiler/daemon/daemon-common/src/org/jetbrains/kotlin/daemon/common/NetworkUtils.kt`** -> AI Confidence: **99.48%**
989. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/CompileServiceImpl.kt`** -> AI Confidence: **99.48%**
990. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/KotlinCompileDaemon.kt`** -> AI Confidence: **99.48%**
991. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/KotlinRemoteReplService.kt`** -> AI Confidence: **99.48%**
992. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/LazyClasspathWatcher.kt`** -> AI Confidence: **99.48%**
993. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/RemoteLookupTrackerClient.kt`** -> AI Confidence: **99.48%**
994. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/report/BuildReportICReporter.kt`** -> AI Confidence: **99.48%**
995. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/report/DebugMessagesICReporter.kt`** -> AI Confidence: **99.48%**
996. **`compiler/daemon/src/org/jetbrains/kotlin/daemon/report/getICReporter.kt`** -> AI Confidence: **99.48%**
997. **`compiler/fir/analysis-tests/legacy-fir-tests/testFixtures/org/jetbrains/kotlin/fir/BuiltInsDeserializationForFirTestCase.kt`** -> AI Confidence: **99.48%**
998. **`compiler/fir/analysis-tests/legacy-fir-tests/testFixtures/org/jetbrains/kotlin/fir/java/JavaClassRendering.kt`** -> AI Confidence: **99.48%**
999. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/Generator.kt`** -> AI Confidence: **99.48%**
1000. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/Main.kt`** -> AI Confidence: **99.48%**
1001. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/NonSuppressibleErrorNamesGenerator.kt`** -> AI Confidence: **99.48%**
1002. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/FirDiagnosticsList.kt`** -> AI Confidence: **99.48%**
1003. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/model/DiagnosticGroup.kt`** -> AI Confidence: **99.48%**
1004. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/model/DiagnosticList.kt`** -> AI Confidence: **99.48%**
1005. **`compiler/fir/checkers/checkers-component-generator/src/org/jetbrains/kotlin/fir/checkers/generator/diagnostics/model/ErrorListDiagnosticListRenderer.kt`** -> AI Confidence: **99.48%**
1006. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/diagnostics/js/FirJsErrorsDefaultMessages.kt`** -> AI Confidence: **99.48%**
1007. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/FirJsHelpers.kt`** -> AI Confidence: **99.48%**
1008. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/FirJsModuleCheckUtils.kt`** -> AI Confidence: **99.48%**
1009. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsActualExternalInterfaceSuggestJsNoRuntimeChecker.kt`** -> AI Confidence: **99.48%**
1010. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsBuiltinNameClashChecker.kt`** -> AI Confidence: **99.48%**
1011. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsDynamicDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1012. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExportDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1013. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExportedActualMatchExpectChecker.kt`** -> AI Confidence: **99.48%**
1014. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExternalChecker.kt`** -> AI Confidence: **99.48%**
1015. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExternalFileChecker.kt`** -> AI Confidence: **99.48%**
1016. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsExternalInheritorOnlyChecker.kt`** -> AI Confidence: **99.48%**
1017. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsInheritanceClassChecker.kt`** -> AI Confidence: **99.48%**
1018. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsInheritanceFunctionChecker.kt`** -> AI Confidence: **99.48%**
1019. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsModuleChecker.kt`** -> AI Confidence: **99.48%**
1020. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsMultipleInheritanceChecker.kt`** -> AI Confidence: **99.48%**
1021. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNameCharsChecker.kt`** -> AI Confidence: **99.48%**
1022. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNameChecker.kt`** -> AI Confidence: **99.48%**
1023. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNameClashClassMembersChecker.kt`** -> AI Confidence: **99.48%**
1024. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNameClashFileTopLevelDeclarationsChecker.kt`** -> AI Confidence: **99.48%**
1025. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNativeAnnotationCheckers.kt`** -> AI Confidence: **99.48%**
1026. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsNoRuntimeDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1027. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsPackageDirectiveChecker.kt`** -> AI Confidence: **99.48%**
1028. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsPropertyDelegationByDynamicChecker.kt`** -> AI Confidence: **99.48%**
1029. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsRuntimeAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1030. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsStaticChecker.kt`** -> AI Confidence: **99.48%**
1031. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/declaration/FirJsSymbolChecker.kt`** -> AI Confidence: **99.48%**
1032. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsDefinedExternallyCallChecker.kt`** -> AI Confidence: **99.48%**
1033. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsDynamicCallChecker.kt`** -> AI Confidence: **99.48%**
1034. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsExternalArgumentCallChecker.kt`** -> AI Confidence: **99.48%**
1035. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsModuleGetClassCallChecker.kt`** -> AI Confidence: **99.48%**
1036. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsModuleQualifiedAccessChecker.kt`** -> AI Confidence: **99.48%**
1037. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsNoRuntimeUsageCheckers.kt`** -> AI Confidence: **99.48%**
1038. **`compiler/fir/checkers/checkers.js/src/org/jetbrains/kotlin/fir/analysis/js/checkers/expression/FirJsReifiedJsNoRuntimeChecker.kt`** -> AI Confidence: **99.48%**
1039. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/diagnostics/jvm/FirJvmErrorsDefaultMessages.kt`** -> AI Confidence: **99.48%**
1040. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/FirJvmNamesChecker.kt`** -> AI Confidence: **99.48%**
1041. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/FirJavaNullabilityWarningUpperBoundsProvider.kt`** -> AI Confidence: **99.48%**
1042. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/FirJvmAnnotationHelper.kt`** -> AI Confidence: **99.48%**
1043. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/FirJvmAnnotationsPlatformSpecificSupportComponent.kt`** -> AI Confidence: **99.48%**
1044. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/FirJvmInlineCheckerComponent.kt`** -> AI Confidence: **99.48%**
1045. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirAccidentalOverrideClashChecker.kt`** -> AI Confidence: **99.48%**
1046. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirDeclarationJavaNullabilityWarningCheckers.kt`** -> AI Confidence: **99.48%**
1047. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirImplementationByDelegationWithDifferentGenericSignatureChecker.kt`** -> AI Confidence: **99.48%**
1048. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirIncompatibleAnnotationsChecker.kt`** -> AI Confidence: **99.48%**
1049. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJavaClassInheritsKtPrivateClassDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1050. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmConflictsChecker.kt`** -> AI Confidence: **99.48%**
1051. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmDefaultChecker.kt`** -> AI Confidence: **99.48%**
1052. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmExposeBoxedChecker.kt`** -> AI Confidence: **99.48%**
1053. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmExternalDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1054. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmFieldApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
1055. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmFunctionDelegateMemberNameClashChecker.kt`** -> AI Confidence: **99.48%**
1056. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmInlineApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
1057. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmNameChecker.kt`** -> AI Confidence: **99.48%**
1058. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmRecordChecker.kt`** -> AI Confidence: **99.48%**
1059. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmRedundantRepeatableChecker.kt`** -> AI Confidence: **99.48%**
1060. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmStaticChecker.kt`** -> AI Confidence: **99.48%**
1061. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmSyntheticApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
1062. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmThrowsChecker.kt`** -> AI Confidence: **99.48%**
1063. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirJvmVersionOverloadsChecker.kt`** -> AI Confidence: **99.48%**
1064. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirOverloadsChecker.kt`** -> AI Confidence: **99.48%**
1065. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirOverrideJavaNullabilityWarningChecker.kt`** -> AI Confidence: **99.48%**
1066. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirPropertyHidesJavaFieldChecker.kt`** -> AI Confidence: **99.48%**
1067. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirRepeatableAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1068. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirStrictfpApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
1069. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirSynchronizedAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1070. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/declaration/FirUpperBoundsChecker.kt`** -> AI Confidence: **99.48%**
1071. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirArrayOfNullableNothingExpressionChecker.kt`** -> AI Confidence: **99.48%**
1072. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirExpressionJavaNullabilityWarningCheckers.kt`** -> AI Confidence: **99.48%**
1073. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirFieldAccessShadowedByInvisibleKotlinProperty.kt`** -> AI Confidence: **99.48%**
1074. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirInterfaceDefaultMethodCallChecker.kt`** -> AI Confidence: **99.48%**
1075. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaAnnotationsChecker.kt`** -> AI Confidence: **99.48%**
1076. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaClassInheritsKtPrivateClassExpressionChecker.kt`** -> AI Confidence: **99.48%**
1077. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaClassOnCompanionChecker.kt`** -> AI Confidence: **99.48%**
1078. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaGenericVarianceViolationTypeChecker.kt`** -> AI Confidence: **99.48%**
1079. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaSamConstructorNullabilityChecker.kt`** -> AI Confidence: **99.48%**
1080. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaSamInterfaceConstructorReferenceChecker.kt`** -> AI Confidence: **99.48%**
1081. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaUnnecessaryNotNullChecker.kt`** -> AI Confidence: **99.48%**
1082. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJavaUnnecessarySafeCallChecker.kt`** -> AI Confidence: **99.48%**
1083. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmIdentityEqualsOnJavaValueBasedClass.kt`** -> AI Confidence: **99.48%**
1084. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmIdentitySensitiveCallWithValueTypeObjectChecker.kt`** -> AI Confidence: **99.48%**
1085. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmInconsistentOperatorFromJavaCallChecker.kt`** -> AI Confidence: **99.48%**
1086. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmInlineTargetQualifiedAccessChecker.kt`** -> AI Confidence: **99.48%**
1087. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmMissingBuiltInDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1088. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmModuleAccessibilityQualifiedAccessChecker.kt`** -> AI Confidence: **99.48%**
1089. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmPackageNameAnnotationsChecker.kt`** -> AI Confidence: **99.48%**
1090. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmPolymorphicSignatureCallChecker.kt`** -> AI Confidence: **99.48%**
1091. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmProtectedInSuperClassCompanionCallChecker.kt`** -> AI Confidence: **99.48%**
1092. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmSerializableLambdaChecker.kt`** -> AI Confidence: **99.48%**
1093. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirJvmSuspensionPointInsideMutexLockChecker.kt`** -> AI Confidence: **99.48%**
1094. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirSyntheticPropertyWithoutJavaOriginChecker.kt`** -> AI Confidence: **99.48%**
1095. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/FirUnsupportedSyntheticCallableReferenceChecker.kt`** -> AI Confidence: **99.48%**
1096. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/expression/firJavaValueBasedClassUtils.kt`** -> AI Confidence: **99.48%**
1097. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/type/FirArrayOfNullableNothingTypeChecker.kt`** -> AI Confidence: **99.48%**
1098. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/type/FirFunctionalTypeParameterNameChecker.kt`** -> AI Confidence: **99.48%**
1099. **`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/jvm/checkers/type/FirJvmModuleAccessibilityTypeChecker.kt`** -> AI Confidence: **99.48%**
1100. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/diagnostics/native/FirNativeErrorsDefaultMessages.kt`** -> AI Confidence: **99.48%**
1101. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeCastChecker.kt`** -> AI Confidence: **99.48%**
1102. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeExternalDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1103. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeForwardDeclarationGetClassCallChecker.kt`** -> AI Confidence: **99.48%**
1104. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeForwardDeclarationReifiedChecker.kt`** -> AI Confidence: **99.48%**
1105. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeForwardDeclarationTypeOperatorChecker.kt`** -> AI Confidence: **99.48%**
1106. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeHelpers.kt`** -> AI Confidence: **99.48%**
1107. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeHiddenFromObjCInheritanceChecker.kt`** -> AI Confidence: **99.48%**
1108. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeIdentifierChecker.kt`** -> AI Confidence: **99.48%**
1109. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeIdentityHashCodeCallOnValueTypeObjectChecker.kt`** -> AI Confidence: **99.48%**
1110. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCActionChecker.kt`** -> AI Confidence: **99.48%**
1111. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCNameCallableChecker.kt`** -> AI Confidence: **99.48%**
1112. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCNameChecker.kt`** -> AI Confidence: **99.48%**
1113. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCNameOverridesChecker.kt`** -> AI Confidence: **99.48%**
1114. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCNameUtilities.kt`** -> AI Confidence: **99.48%**
1115. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCOutletChecker.kt`** -> AI Confidence: **99.48%**
1116. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCOverrideInitChecker.kt`** -> AI Confidence: **99.48%**
1117. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCRefinementAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1118. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCRefinementChecker.kt`** -> AI Confidence: **99.48%**
1119. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCRefinementOverridesChecker.kt`** -> AI Confidence: **99.48%**
1120. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCStringAsVariadicChecker.kt`** -> AI Confidence: **99.48%**
1121. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjCVariadicMethodOverrideChecker.kt`** -> AI Confidence: **99.48%**
1122. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeObjcOverrideApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
1123. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeSharedImmutableChecker.kt`** -> AI Confidence: **99.48%**
1124. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeSpecificAtomicChecker.kt`** -> AI Confidence: **99.48%**
1125. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeThreadLocalChecker.kt`** -> AI Confidence: **99.48%**
1126. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeThrowsChecker.kt`** -> AI Confidence: **99.48%**
1127. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeVariadicCallableReferenceChecker.kt`** -> AI Confidence: **99.48%**
1128. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeVariadicFunctionPointerChecker.kt`** -> AI Confidence: **99.48%**
1129. **`compiler/fir/checkers/checkers.native/src/org/jetbrains/kotlin/fir/analysis/native/checkers/FirNativeVariadicSpreadChecker.kt`** -> AI Confidence: **99.48%**
1130. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/diagnostics/wasm/FirWasmErrorsDefaultMessages.kt`** -> AI Confidence: **99.48%**
1131. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/FirWasmJsCastChecker.kt`** -> AI Confidence: **99.48%**
1132. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/FirWasmJsCodeHelpers.kt`** -> AI Confidence: **99.48%**
1133. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/FirWasmJsEqualityChecker.kt`** -> AI Confidence: **99.48%**
1134. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/FirWasmJsExportHelpers.kt`** -> AI Confidence: **99.48%**
1135. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmExportAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1136. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmExternalChecker.kt`** -> AI Confidence: **99.48%**
1137. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmExternalFileChecker.kt`** -> AI Confidence: **99.48%**
1138. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmExternalInheritanceChecker.kt`** -> AI Confidence: **99.48%**
1139. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmImportAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1140. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmJsAssociatedObjectChecker.kt`** -> AI Confidence: **99.48%**
1141. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmJsFunAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1142. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmJsInteropTypesChecker.kt`** -> AI Confidence: **99.48%**
1143. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmJsModuleChecker.kt`** -> AI Confidence: **99.48%**
1144. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/declaration/FirWasmWasiExternalDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1145. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/expression/FirWasmDefinedExternallyCallChecker.kt`** -> AI Confidence: **99.48%**
1146. **`compiler/fir/checkers/checkers.wasm/src/org/jetbrains/kotlin/fir/analysis/wasm/checkers/expression/FirWasmJsCodeCallChecker.kt`** -> AI Confidence: **99.48%**
1147. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/diagnostics/web/common/FirWebCommonErrorsDefaultMessages.kt`** -> AI Confidence: **99.48%**
1148. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirJsExportAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1149. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirMultipleJsExportDefaultAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1150. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirWebCommonExternalChecker.kt`** -> AI Confidence: **99.48%**
1151. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirWebCommonExternalPropertyAccessorChecker.kt`** -> AI Confidence: **99.48%**
1152. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirWebCommonNativeAnnotationCheckers.kt`** -> AI Confidence: **99.48%**
1153. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirAbstractNativeRttiChecker.kt`** -> AI Confidence: **99.48%**
1154. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirAbstractReifiedOnDeclarationWithoutRuntimeChecker.kt`** -> AI Confidence: **99.48%**
1155. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirJsCodeConstantArgumentChecker.kt`** -> AI Confidence: **99.48%**
1156. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirJsQualifierChecker.kt`** -> AI Confidence: **99.48%**
1157. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/expression/FirWebReflectionAPICallChecker.kt`** -> AI Confidence: **99.48%**
1158. **`compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/declarations/utils/FirWebCommonHelpers.kt`** -> AI Confidence: **99.48%**
1159. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/CheckersComponent.kt`** -> AI Confidence: **99.48%**
1160. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/FirOverridesBackwardCompatibilityHelper.kt`** -> AI Confidence: **99.48%**
1161. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/FirSourceUtils.kt`** -> AI Confidence: **99.48%**
1162. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/FirCallsEffectAnalyzer.kt`** -> AI Confidence: **99.48%**
1163. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/FirPropertyInitializationAnalyzer.kt`** -> AI Confidence: **99.48%**
1164. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/VariableInitializationCheckProcessor.kt`** -> AI Confidence: **99.48%**
1165. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/util/PropertyInitializationInfoCollector.kt`** -> AI Confidence: **99.48%**
1166. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/ConeTypeCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
1167. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FE10LikeConeSubstitutor.kt`** -> AI Confidence: **99.48%**
1168. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirAnnotationHelpers.kt`** -> AI Confidence: **99.48%**
1169. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirCastDiagnosticsHelpers.kt`** -> AI Confidence: **99.48%**
1170. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirConflictsHelpers.kt`** -> AI Confidence: **99.48%**
1171. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirHelpers.kt`** -> AI Confidence: **99.48%**
1172. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirInconsistentTypeParameterHelpers.kt`** -> AI Confidence: **99.48%**
1173. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirInlineCheckerPlatformSpecificComponent.kt`** -> AI Confidence: **99.48%**
1174. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirKeywordUtils.kt`** -> AI Confidence: **99.48%**
1175. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirMissingDependencySupertypeUtils.kt`** -> AI Confidence: **99.48%**
1176. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirRootIdePackageInCliDeprecations.kt`** -> AI Confidence: **99.48%**
1177. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirSinceKotlinHelpers.kt`** -> AI Confidence: **99.48%**
1178. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirTypeCompatibilityHelpers.kt`** -> AI Confidence: **99.48%**
1179. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirUnderscoreHelpers.kt`** -> AI Confidence: **99.48%**
1180. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirUpperBoundViolatedHelpers.kt`** -> AI Confidence: **99.48%**
1181. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/ModifiersCompatibilityUtils.kt`** -> AI Confidence: **99.48%**
1182. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/ProjectionRelationCheckerImpl.kt`** -> AI Confidence: **99.48%**
1183. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/SourceHelpers.kt`** -> AI Confidence: **99.48%**
1184. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/SourceNavigator.kt`** -> AI Confidence: **99.48%**
1185. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/config/FirOptInLanguageVersionSettingsChecker.kt`** -> AI Confidence: **99.48%**
1186. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/config/FirSuppressedDiagnosticsCheckers.kt`** -> AI Confidence: **99.48%**
1187. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/context/CheckerContext.kt`** -> AI Confidence: **99.48%**
1188. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/context/MutableCheckerContext.kt`** -> AI Confidence: **99.48%**
1189. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/context/PersistentCheckerContext.kt`** -> AI Confidence: **99.48%**
1190. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirActualAnnotationsMatchExpectChecker.kt`** -> AI Confidence: **99.48%**
1191. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirActualTypeAliasChecker.kt`** -> AI Confidence: **99.48%**
1192. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAmbiguousAnonymousTypeChecker.kt`** -> AI Confidence: **99.48%**
1193. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1194. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnnotationClassDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1195. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnnotationClassInheritanceChecker.kt`** -> AI Confidence: **99.48%**
1196. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnonymousInitializerInInterfaceChecker.kt`** -> AI Confidence: **99.48%**
1197. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnyDeprecationChecker.kt`** -> AI Confidence: **99.48%**
1198. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnyTypeAliasChecker.kt`** -> AI Confidence: **99.48%**
1199. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirBadInheritedJavaSignaturesChecker.kt`** -> AI Confidence: **99.48%**
1200. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirClassVarianceChecker.kt`** -> AI Confidence: **99.48%**
1201. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCommonConstructorDelegationIssuesChecker.kt`** -> AI Confidence: **99.48%**
1202. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCompanionBlockChecker.kt`** -> AI Confidence: **99.48%**
1203. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCompanionBlockMemberChecker.kt`** -> AI Confidence: **99.48%**
1204. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCompanionExtensionChecker.kt`** -> AI Confidence: **99.48%**
1205. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirConflictsDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1206. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirConstPropertyChecker.kt`** -> AI Confidence: **99.48%**
1207. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirConstructorAllowedChecker.kt`** -> AI Confidence: **99.48%**
1208. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirContextParametersDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1209. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirContextReceiversDeprecatedDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1210. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirContextualPropertyWithBackingFieldChecker.kt`** -> AI Confidence: **99.48%**
1211. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirContractChecker.kt`** -> AI Confidence: **99.48%**
1212. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCoroutineContextAsContextParameterDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1213. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirCyclicTypeBoundsChecker.kt`** -> AI Confidence: **99.48%**
1214. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDataClassConsistentDataCopyAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1215. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDataClassNonPublicConstructorChecker.kt`** -> AI Confidence: **99.48%**
1216. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDataClassPrimaryConstructorChecker.kt`** -> AI Confidence: **99.48%**
1217. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDataObjectContentChecker.kt`** -> AI Confidence: **99.48%**
1218. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDelegateFieldTypeMismatchChecker.kt`** -> AI Confidence: **99.48%**
1219. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDelegateUsesExtensionPropertyTypeParameterChecker.kt`** -> AI Confidence: **99.48%**
1220. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDelegatedPropertyChecker.kt`** -> AI Confidence: **99.48%**
1221. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDelegationSuperCallInEnumConstructorChecker.kt`** -> AI Confidence: **99.48%**
1222. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDestructuringDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1223. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDynamicReceiverChecker.kt`** -> AI Confidence: **99.48%**
1224. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirDynamicSupertypeChecker.kt`** -> AI Confidence: **99.48%**
1225. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirEnumClassSimpleChecker.kt`** -> AI Confidence: **99.48%**
1226. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirEnumCompanionInEnumConstructorCallChecker.kt`** -> AI Confidence: **99.48%**
1227. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirEnumEntriesRedeclarationChecker.kt`** -> AI Confidence: **99.48%**
1228. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirEnumEntryInitializationChecker.kt`** -> AI Confidence: **99.48%**
1229. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExpectActualClassifiersAreInBetaChecker.kt`** -> AI Confidence: **99.48%**
1230. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExpectActualDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1231. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExpectConsistencyChecker.kt`** -> AI Confidence: **99.48%**
1232. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExpectRefinementChecker.kt`** -> AI Confidence: **99.48%**
1233. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExplicitBackingFieldForbiddenChecker.kt`** -> AI Confidence: **99.48%**
1234. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExplicitBackingFieldsUnsupportedChecker.kt`** -> AI Confidence: **99.48%**
1235. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExposedVisibilityDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1236. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirExtensionShadowedByMemberChecker.kt`** -> AI Confidence: **99.48%**
1237. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFiniteBoundRestrictionChecker.kt`** -> AI Confidence: **99.48%**
1238. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFunInterfaceDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1239. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFunctionNameChecker.kt`** -> AI Confidence: **99.48%**
1240. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFunctionParameterChecker.kt`** -> AI Confidence: **99.48%**
1241. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirFunctionReturnChecker.kt`** -> AI Confidence: **99.48%**
1242. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirIllegalCompanionBlockMemberChecker.kt`** -> AI Confidence: **99.48%**
1243. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirImplementationMismatchChecker.kt`** -> AI Confidence: **99.48%**
1244. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirImplicitNothingReturnTypeChecker.kt`** -> AI Confidence: **99.48%**
1245. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirImplicitReturnTypeAnnotationMissingDependencyChecker.kt`** -> AI Confidence: **99.48%**
1246. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirImportsChecker.kt`** -> AI Confidence: **99.48%**
1247. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInapplicableLateinitChecker.kt`** -> AI Confidence: **99.48%**
1248. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInfixFunctionDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1249. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInitializerTypeMismatchChecker.kt`** -> AI Confidence: **99.48%**
1250. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlineBodySimpleFunctionChecker.kt`** -> AI Confidence: **99.48%**
1251. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlineClassDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1252. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlineDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1253. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlinePropertyChecker.kt`** -> AI Confidence: **99.48%**
1254. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirInlinedLambdaNonSourceAnnotationsChecker.kt`** -> AI Confidence: **99.48%**
1255. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirKClassWithIncorrectTypeArgumentChecker.kt`** -> AI Confidence: **99.48%**
1256. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirLargeArityFunctionImportChecker.kt`** -> AI Confidence: **99.48%**
1257. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirLocalEntityNotAllowedChecker.kt`** -> AI Confidence: **99.48%**
1258. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirLocalExtensionPropertyChecker.kt`** -> AI Confidence: **99.48%**
1259. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirManyCompanionObjectsChecker.kt`** -> AI Confidence: **99.48%**
1260. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMemberFunctionsChecker.kt`** -> AI Confidence: **99.48%**
1261. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMemberPropertiesChecker.kt`** -> AI Confidence: **99.48%**
1262. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMethodOfAnyImplementedInInterfaceChecker.kt`** -> AI Confidence: **99.48%**
1263. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMissingDependencyClassForLambdaReceiverChecker.kt`** -> AI Confidence: **99.48%**
1264. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMissingDependencyClassForParameterChecker.kt`** -> AI Confidence: **99.48%**
1265. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMissingDependencySupertypeInDeclarationsChecker.kt`** -> AI Confidence: **99.48%**
1266. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMixedFunctionalTypesInSupertypesChecker.kt`** -> AI Confidence: **99.48%**
1267. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirModifierChecker.kt`** -> AI Confidence: **99.48%**
1268. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirMultipleDefaultsInheritedFromSupertypesChecker.kt`** -> AI Confidence: **99.48%**
1269. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNestedClassChecker.kt`** -> AI Confidence: **99.48%**
1270. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNonExpansiveInheritanceRestrictionChecker.kt`** -> AI Confidence: **99.48%**
1271. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNonMemberFunctionsChecker.kt`** -> AI Confidence: **99.48%**
1272. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNotImplementedOverrideChecker.kt`** -> AI Confidence: **99.48%**
1273. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirNotImplementedOverrideSimpleEnumEntryChecker.kt`** -> AI Confidence: **99.48%**
1274. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirObjectConstructorChecker.kt`** -> AI Confidence: **99.48%**
1275. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOpenMemberChecker.kt`** -> AI Confidence: **99.48%**
1276. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOperatorModifierChecker.kt`** -> AI Confidence: **99.48%**
1277. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOperatorOfChecker.kt`** -> AI Confidence: **99.48%**
1278. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptInAnnotationClassChecker.kt`** -> AI Confidence: **99.48%**
1279. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptInEnumEntryChecker.kt`** -> AI Confidence: **99.48%**
1280. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptInImportsChecker.kt`** -> AI Confidence: **99.48%**
1281. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptInMarkedDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1282. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOptionalExpectationDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1283. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOuterClassArgumentsRequiredChecker.kt`** -> AI Confidence: **99.48%**
1284. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirOverrideChecker.kt`** -> AI Confidence: **99.48%**
1285. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPackageConflictsWithClassifierChecker.kt`** -> AI Confidence: **99.48%**
1286. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPrimaryConstructorSuperTypeChecker.kt`** -> AI Confidence: **99.48%**
1287. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPropertyAccessorsTypesChecker.kt`** -> AI Confidence: **99.48%**
1288. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPropertyFieldTypeChecker.kt`** -> AI Confidence: **99.48%**
1289. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPropertyFromParameterChecker.kt`** -> AI Confidence: **99.48%**
1290. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPropertyInitializationChecker.kt`** -> AI Confidence: **99.48%**
1291. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPropertyTypeParametersChecker.kt`** -> AI Confidence: **99.48%**
1292. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirPublishedApiChecker.kt`** -> AI Confidence: **99.48%**
1293. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirReifiedTypeParameterChecker.kt`** -> AI Confidence: **99.48%**
1294. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirRequiresOptInOnExpectChecker.kt`** -> AI Confidence: **99.48%**
1295. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirReservedUnderscoreDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1296. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirSealedInterfaceAllowedChecker.kt`** -> AI Confidence: **99.48%**
1297. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirSealedSupertypeChecker.kt`** -> AI Confidence: **99.48%**
1298. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirSupertypesChecker.kt`** -> AI Confidence: **99.48%**
1299. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirSuspendAnonymousFunctionChecker.kt`** -> AI Confidence: **99.48%**
1300. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirSuspendLimitationsChecker.kt`** -> AI Confidence: **99.48%**
1301. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTailrecFunctionChecker.kt`** -> AI Confidence: **99.48%**
1302. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirThrowableSubclassChecker.kt`** -> AI Confidence: **99.48%**
1303. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTopLevelPropertiesChecker.kt`** -> AI Confidence: **99.48%**
1304. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTypeConstraintsChecker.kt`** -> AI Confidence: **99.48%**
1305. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTypeParameterBoundsChecker.kt`** -> AI Confidence: **99.48%**
1306. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTypeParameterVarianceChecker.kt`** -> AI Confidence: **99.48%**
1307. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirTypeParametersInObjectChecker.kt`** -> AI Confidence: **99.48%**
1308. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirUnnamedPropertyChecker.kt`** -> AI Confidence: **99.48%**
1309. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirUnusedCheckerBase.kt`** -> AI Confidence: **99.48%**
1310. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirValueClassDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1311. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirValueParameterDefaultValueTypeMismatchChecker.kt`** -> AI Confidence: **99.48%**
1312. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirVersionOverloadsChecker.kt`** -> AI Confidence: **99.48%**
1313. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirVolatileAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1314. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/NiceContractSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1315. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/PlatformClassMappedToKotlinImportsChecker.kt`** -> AI Confidence: **99.48%**
1316. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/crv/FirReturnValueAnnotationsChecker.kt`** -> AI Confidence: **99.48%**
1317. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/crv/FirReturnValueOverrideChecker.kt`** -> AI Confidence: **99.48%**
1318. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/crv/FirUnusedReturnValueChecker.kt`** -> AI Confidence: **99.48%**
1319. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/crv/helpers.kt`** -> AI Confidence: **99.48%**
1320. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/declarationUtils.kt`** -> AI Confidence: **99.48%**
1321. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/experimental/EmptyRangeChecker.kt`** -> AI Confidence: **99.48%**
1322. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/experimental/RedundantInterpolationPrefixCheckerLiteral.kt`** -> AI Confidence: **99.48%**
1323. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/AbstractFirReflectionApiCallChecker.kt`** -> AI Confidence: **99.48%**
1324. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/ArrayEqualityCanBeReplacedWithContentEquals.kt`** -> AI Confidence: **99.48%**
1325. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirAbstractClassInstantiationChecker.kt`** -> AI Confidence: **99.48%**
1326. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirAbstractSuperCallChecker.kt`** -> AI Confidence: **99.48%**
1327. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirAnnotationExpressionChecker.kt`** -> AI Confidence: **99.48%**
1328. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirArrayOfNothingQualifierChecker.kt`** -> AI Confidence: **99.48%**
1329. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirAssignmentOperatorCallChecker.kt`** -> AI Confidence: **99.48%**
1330. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirBreakOrContinueJumpsAcrossFunctionBoundaryChecker.kt`** -> AI Confidence: **99.48%**
1331. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCallableReferenceChecker.kt`** -> AI Confidence: **99.48%**
1332. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCastOperatorsChecker.kt`** -> AI Confidence: **99.48%**
1333. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCatchParameterChecker.kt`** -> AI Confidence: **99.48%**
1334. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirClassLiteralChecker.kt`** -> AI Confidence: **99.48%**
1335. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCommonAtomicReferenceToPrimitiveCallChecker.kt`** -> AI Confidence: **99.48%**
1336. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirConflictsExpressionChecker.kt`** -> AI Confidence: **99.48%**
1337. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirConstructorCallChecker.kt`** -> AI Confidence: **99.48%**
1338. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirContextParameterInCalledSignatureChecker.kt`** -> AI Confidence: **99.48%**
1339. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirContextSensitiveResolutionAmbiguityChecker.kt`** -> AI Confidence: **99.48%**
1340. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirContractNotFirstStatementChecker.kt`** -> AI Confidence: **99.48%**
1341. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirConventionFunctionCallChecker.kt`** -> AI Confidence: **99.48%**
1342. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCustomEnumEntriesMigrationAccessChecker.kt`** -> AI Confidence: **99.48%**
1343. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCustomEnumEntriesMigrationQualifierChecker.kt`** -> AI Confidence: **99.48%**
1344. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirCustomEnumEntriesMigrationReferenceChecker.kt`** -> AI Confidence: **99.48%**
1345. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDataClassCopyUsageWillBecomeInaccessibleChecker.kt`** -> AI Confidence: **99.48%**
1346. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDeprecatedSmartCastChecker.kt`** -> AI Confidence: **99.48%**
1347. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDeprecationChecker.kt`** -> AI Confidence: **99.48%**
1348. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDivisionByZeroChecker.kt`** -> AI Confidence: **99.48%**
1349. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirDslMarkerUseSiteChecker.kt`** -> AI Confidence: **99.48%**
1350. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirEqualityCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
1351. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirExhaustiveWhenChecker.kt`** -> AI Confidence: **99.48%**
1352. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirExpressionAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1353. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirExpressionWithErrorTypeChecker.kt`** -> AI Confidence: **99.48%**
1354. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirForLoopChecker.kt`** -> AI Confidence: **99.48%**
1355. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirForLoopStatementAssignmentChecker.kt`** -> AI Confidence: **99.48%**
1356. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirFunctionReturnTypeMismatchChecker.kt`** -> AI Confidence: **99.48%**
1357. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirGenericQualifierOnConstructorCallChecker.kt`** -> AI Confidence: **99.48%**
1358. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirImplicitPropertyTypeMakesBehaviorOrderDependantChecker.kt`** -> AI Confidence: **99.48%**
1359. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirIncompatibleClassExpressionChecker.kt`** -> AI Confidence: **99.48%**
1360. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineBodyResolvableExpressionChecker.kt`** -> AI Confidence: **99.48%**
1361. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineBodyResolvedQualifierChecker.kt`** -> AI Confidence: **99.48%**
1362. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineBodyVariableAssignmentChecker.kt`** -> AI Confidence: **99.48%**
1363. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineExposedLessVisibleThisReceiverChecker.kt`** -> AI Confidence: **99.48%**
1364. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirInlineExposedLessVisibleTypeQualifiedAccessChecker.kt`** -> AI Confidence: **99.48%**
1365. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirKotlinActualAnnotationHasNoEffectInKotlinExpressionChecker.kt`** -> AI Confidence: **99.48%**
1366. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirLargeArityFunctionCallableReferenceChecker.kt`** -> AI Confidence: **99.48%**
1367. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirLateinitIntrinsicApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
1368. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirMissingDependencyClassChecker.kt`** -> AI Confidence: **99.48%**
1369. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirMissingDependencySupertypeInQualifiedAccessExpressionsChecker.kt`** -> AI Confidence: **99.48%**
1370. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirMultiDollarInterpolationChecker.kt`** -> AI Confidence: **99.48%**
1371. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirNamedVarargChecker.kt`** -> AI Confidence: **99.48%**
1372. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirNotNullAssertionChecker.kt`** -> AI Confidence: **99.48%**
1373. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptInAnnotationCallChecker.kt`** -> AI Confidence: **99.48%**
1374. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptInUsageAccessChecker.kt`** -> AI Confidence: **99.48%**
1375. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptInUsageBaseChecker.kt`** -> AI Confidence: **99.48%**
1376. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptInUsageQualifierChecker.kt`** -> AI Confidence: **99.48%**
1377. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirOptionalExpectationExpressionChecker.kt`** -> AI Confidence: **99.48%**
1378. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirPackageOnLhsQualifierChecker.kt`** -> AI Confidence: **99.48%**
1379. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirParenthesizedLhsSetOperatorChecker.kt`** -> AI Confidence: **99.48%**
1380. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirParenthesizedLhsVariableAssignmentChecker.kt`** -> AI Confidence: **99.48%**
1381. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirPrivateToThisAccessChecker.kt`** -> AI Confidence: **99.48%**
1382. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirProjectionsOnNonClassTypeArgumentChecker.kt`** -> AI Confidence: **99.48%**
1383. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirPropertyAccessTypeArgumentsChecker.kt`** -> AI Confidence: **99.48%**
1384. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirProtectedConstructorNotInSuperCallChecker.kt`** -> AI Confidence: **99.48%**
1385. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirQualifierWithTypeArgumentsChecker.kt`** -> AI Confidence: **99.48%**
1386. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirReassignmentAndInvisibleSetterChecker.kt`** -> AI Confidence: **99.48%**
1387. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirReceiverAccessBeforeSuperCallChecker.kt`** -> AI Confidence: **99.48%**
1388. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirRecursiveProblemChecker.kt`** -> AI Confidence: **99.48%**
1389. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirReifiedChecker.kt`** -> AI Confidence: **99.48%**
1390. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirReturnSyntaxAndLabelChecker.kt`** -> AI Confidence: **99.48%**
1391. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSealedClassConstructorCallChecker.kt`** -> AI Confidence: **99.48%**
1392. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSingleNamedFunctionChecker.kt`** -> AI Confidence: **99.48%**
1393. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSpreadOfNullableChecker.kt`** -> AI Confidence: **99.48%**
1394. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirStandaloneQualifierChecker.kt`** -> AI Confidence: **99.48%**
1395. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSuperCallWithDefaultsChecker.kt`** -> AI Confidence: **99.48%**
1396. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSuperReferenceChecker.kt`** -> AI Confidence: **99.48%**
1397. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSuperclassNotAccessibleFromInterfaceChecker.kt`** -> AI Confidence: **99.48%**
1398. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirSuspendCallChecker.kt`** -> AI Confidence: **99.48%**
1399. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirThrowExpressionTypeChecker.kt`** -> AI Confidence: **99.48%**
1400. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTrimMarginBlankPrefixChecker.kt`** -> AI Confidence: **99.48%**
1401. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTypeArgumentsNotAllowedExpressionChecker.kt`** -> AI Confidence: **99.48%**
1402. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTypeArgumentsOfQualifierOfCallableReferenceChecker.kt`** -> AI Confidence: **99.48%**
1403. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTypeParameterInQualifiedAccessChecker.kt`** -> AI Confidence: **99.48%**
1404. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirTypeVisibilityHelpers.kt`** -> AI Confidence: **99.48%**
1405. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUnderscoreChecker.kt`** -> AI Confidence: **99.48%**
1406. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUninitializedEnumChecker.kt`** -> AI Confidence: **99.48%**
1407. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUnnecessarySafeCallChecker.kt`** -> AI Confidence: **99.48%**
1408. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUnsupportedArrayLiteralChecker.kt`** -> AI Confidence: **99.48%**
1409. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUpperBoundViolatedQualifiedAccessExpressionChecker.kt`** -> AI Confidence: **99.48%**
1410. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirUselessElvisChecker.kt`** -> AI Confidence: **99.48%**
1411. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirVarargWithNonTrivialUpperBoundInferredToNothingChecker.kt`** -> AI Confidence: **99.48%**
1412. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirVisibilityQualifierChecker.kt`** -> AI Confidence: **99.48%**
1413. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirWhenConditionChecker.kt`** -> AI Confidence: **99.48%**
1414. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirWhenReturnTypeChecker.kt`** -> AI Confidence: **99.48%**
1415. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/FirWhenSubjectChecker.kt`** -> AI Confidence: **99.48%**
1416. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/PlatformClassMappedToKotlinConstructorCallChecker.kt`** -> AI Confidence: **99.48%**
1417. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/expression/RedundantCallOfConversionMethodChecker.kt`** -> AI Confidence: **99.48%**
1418. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/CanBeValChecker.kt`** -> AI Confidence: **99.48%**
1419. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/FirAnonymousUnusedParamChecker.kt`** -> AI Confidence: **99.48%**
1420. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/FirUnusedExpressionChecker.kt`** -> AI Confidence: **99.48%**
1421. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantModalityModifierSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1422. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantReturnUnitType.kt`** -> AI Confidence: **99.48%**
1423. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantSetterParameterTypeChecker.kt`** -> AI Confidence: **99.48%**
1424. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantSingleExpressionStringTemplateChecker.kt`** -> AI Confidence: **99.48%**
1425. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/RedundantVisibilityModifierSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1426. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/UnreachableCodeChecker.kt`** -> AI Confidence: **99.48%**
1427. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/UnusedVariableAssignmentChecker.kt`** -> AI Confidence: **99.48%**
1428. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/extra/UselessCallOnNotNullChecker.kt`** -> AI Confidence: **99.48%**
1429. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirAnnotatedBinaryExpressionChecker.kt`** -> AI Confidence: **99.48%**
1430. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirCommaInWhenConditionChecker.kt`** -> AI Confidence: **99.48%**
1431. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirConfusingWhenBranchSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1432. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirDelegationInExpectClassSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1433. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirDelegationInInterfaceSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1434. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirExplicitApiDeclarationChecker.kt`** -> AI Confidence: **99.48%**
1435. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirFunctionTypeParametersSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1436. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirLocalVariableTypeParametersSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1437. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirMissingConstructorKeywordSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1438. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirPrefixAndSuffixSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1439. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1440. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirTypeParameterSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1441. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirUnderscoredTypeArgumentSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1442. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirUnresolvedInMiddleOfImportChecker.kt`** -> AI Confidence: **99.48%**
1443. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/syntax/FirWhenGuardChecker.kt`** -> AI Confidence: **99.48%**
1444. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirArrayOfNothingTypeChecker.kt`** -> AI Confidence: **99.48%**
1445. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirContextualFunctionTypeChecker.kt`** -> AI Confidence: **99.48%**
1446. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDefinitelyNotNullableChecker.kt`** -> AI Confidence: **99.48%**
1447. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDeprecatedTypeChecker.kt`** -> AI Confidence: **99.48%**
1448. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDslMarkerPropagationChecker.kt`** -> AI Confidence: **99.48%**
1449. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDuplicateParameterNameInFunctionTypeChecker.kt`** -> AI Confidence: **99.48%**
1450. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirDynamicUnsupportedChecker.kt`** -> AI Confidence: **99.48%**
1451. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirFunctionalTypeParameterSyntaxChecker.kt`** -> AI Confidence: **99.48%**
1452. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirInlineExposedLessVisibleTypeChecker.kt`** -> AI Confidence: **99.48%**
1453. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirKotlinActualAnnotationHasNoEffectInKotlinTypeChecker.kt`** -> AI Confidence: **99.48%**
1454. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirMissingDependencyClassInTypeAliasTypeChecker.kt`** -> AI Confidence: **99.48%**
1455. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirOptInUsageTypeRefChecker.kt`** -> AI Confidence: **99.48%**
1456. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirOptionalExpectationTypeChecker.kt`** -> AI Confidence: **99.48%**
1457. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirProjectionRelationChecker.kt`** -> AI Confidence: **99.48%**
1458. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirStarProjectionModifierChecker.kt`** -> AI Confidence: **99.48%**
1459. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirSuspendModifierChecker.kt`** -> AI Confidence: **99.48%**
1460. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirTypeAnnotationChecker.kt`** -> AI Confidence: **99.48%**
1461. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirUnsupportedDefaultValueInFunctionTypeParameterChecker.kt`** -> AI Confidence: **99.48%**
1462. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirUnsupportedModifiersInFunctionTypeParameterChecker.kt`** -> AI Confidence: **99.48%**
1463. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/FirUpperBoundViolatedTypeChecker.kt`** -> AI Confidence: **99.48%**
1464. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/PlatformClassMappedToKotlinTypeRefChecker.kt`** -> AI Confidence: **99.48%**
1465. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/RedundantNullableChecker.kt`** -> AI Confidence: **99.48%**
1466. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/type/TypeArgumentsInPackagesTypeRefChecker.kt`** -> AI Confidence: **99.48%**
1467. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/AbstractDiagnosticCollector.kt`** -> AI Confidence: **99.48%**
1468. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/AbstractDiagnosticCollectorVisitor.kt`** -> AI Confidence: **99.48%**
1469. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/components/ControlFlowAnalysisDiagnosticComponent.kt`** -> AI Confidence: **99.48%**
1470. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/components/DiagnosticComponentsFactory.kt`** -> AI Confidence: **99.48%**
1471. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/components/ErrorNodeDiagnosticCollectorComponent.kt`** -> AI Confidence: **99.48%**
1472. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/collectors/components/LossDiagnosticCollectorComponent.kt`** -> AI Confidence: **99.48%**
1473. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrorsDefaultMessages.kt`** -> AI Confidence: **99.48%**
1474. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirExpectActualAnnotationIncompatibilityDiagnosticRenderers.kt`** -> AI Confidence: **99.48%**
1475. **`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/coneDiagnosticToFirDiagnostic.kt`** -> AI Confidence: **99.48%**
1476. **`compiler/fir/cones/src/org/jetbrains/kotlin/fir/renderer/ConeTypeRenderer.kt`** -> AI Confidence: **99.48%**
1477. **`compiler/fir/cones/src/org/jetbrains/kotlin/fir/renderer/ConeTypeRendererForReadability.kt`** -> AI Confidence: **99.48%**
1478. **`compiler/fir/cones/src/org/jetbrains/kotlin/fir/types/ConeAttributes.kt`** -> AI Confidence: **99.48%**
1479. **`compiler/fir/cones/src/org/jetbrains/kotlin/fir/types/ConeTypeUtils.kt`** -> AI Confidence: **99.48%**
1480. **`compiler/fir/diagnostic-renderers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirAdaptiveTypeRenderingKey.kt`** -> AI Confidence: **99.48%**
1481. **`compiler/fir/diagnostic-renderers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirDiagnosticRenderers.kt`** -> AI Confidence: **99.48%**
1482. **`compiler/fir/dump/src/org/jetbrains/kotlin/fir/dump/HtmlFirDump.kt`** -> AI Confidence: **99.48%**
1483. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/IncrementalPassThroughLookupTrackerComponent.kt`** -> AI Confidence: **99.48%**
1484. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/backend/Fir2IrFakeOverrideStrategy.kt`** -> AI Confidence: **99.48%**
1485. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/backend/LenientModeMissingActualDeclarationProvider.kt`** -> AI Confidence: **99.48%**
1486. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/extensions/FirExtensionRegistrar.kt`** -> AI Confidence: **99.48%**
1487. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/ConstInliner.kt`** -> AI Confidence: **99.48%**
1488. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/Fir2KlibMetadataSerializer.kt`** -> AI Confidence: **99.48%**
1489. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/IrCommonToPlatformDependencyActualizerMapContributor.kt`** -> AI Confidence: **99.48%**
1490. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/analyse.kt`** -> AI Confidence: **99.48%**
1491. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/convertToIr.kt`** -> AI Confidence: **99.48%**
1492. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/firUtils.kt`** -> AI Confidence: **99.48%**
1493. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/referenceAllCommonDependencies.kt`** -> AI Confidence: **99.48%**
1494. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/AbstractFirKlibSessionFactory.kt`** -> AI Confidence: **99.48%**
1495. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/ComponentsContainers.kt`** -> AI Confidence: **99.48%**
1496. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirAbstractSessionFactory.kt`** -> AI Confidence: **99.48%**
1497. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirJsSessionFactory.kt`** -> AI Confidence: **99.48%**
1498. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirJvmIncrementalCompilationSymbolProviders.kt`** -> AI Confidence: **99.48%**
1499. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirJvmSessionFactory.kt`** -> AI Confidence: **99.48%**
1500. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirMetadataSessionFactory.kt`** -> AI Confidence: **99.48%**
1501. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirNativeSessionFactory.kt`** -> AI Confidence: **99.48%**
1502. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirSessionConfigurator.kt`** -> AI Confidence: **99.48%**
1503. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/FirWasmSessionFactory.kt`** -> AI Confidence: **99.48%**
1504. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/KlibBasedAnnotationDeserializer.kt`** -> AI Confidence: **99.48%**
1505. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/KlibBasedSymbolProvider.kt`** -> AI Confidence: **99.48%**
1506. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/KlibIcCacheBasedSymbolProvider.kt`** -> AI Confidence: **99.48%**
1507. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/MetadataLibraryBasedSymbolProvider.kt`** -> AI Confidence: **99.48%**
1508. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/MetadataSymbolProvider.kt`** -> AI Confidence: **99.48%**
1509. **`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/session/NativeForwardDeclarationsSymbolProvider.kt`** -> AI Confidence: **99.48%**
1510. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/AbstractFirDeserializedSymbolProvider.kt`** -> AI Confidence: **99.48%**
1511. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/AnnotationDeserializationUtil.kt`** -> AI Confidence: **99.48%**
1512. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/AnnotationDeserializerWithProtocol.kt`** -> AI Confidence: **99.48%**
1513. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/ClassDeserialization.kt`** -> AI Confidence: **99.48%**
1514. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirConstDeserializer.kt`** -> AI Confidence: **99.48%**
1515. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirContractDeserializer.kt`** -> AI Confidence: **99.48%**
1516. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirDeserializationExtension.kt`** -> AI Confidence: **99.48%**
1517. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirEnumEntryDeserializerAccessUtil.kt`** -> AI Confidence: **99.48%**
1518. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirKDocDeserializer.kt`** -> AI Confidence: **99.48%**
1519. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirMemberDeserializer.kt`** -> AI Confidence: **99.48%**
1520. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/deserialization/FirTypeDeserializer.kt`** -> AI Confidence: **99.48%**
1521. **`compiler/fir/fir-deserialization/src/org/jetbrains/kotlin/fir/resolve/providers/impl/firBuiltinSymbolProviders.kt`** -> AI Confidence: **99.48%**
1522. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/FirJavaElementFinder.kt`** -> AI Confidence: **99.48%**
1523. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/FirJavaFacade.kt`** -> AI Confidence: **99.48%**
1524. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/FirJavaVisibilityChecker.kt`** -> AI Confidence: **99.48%**
1525. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JavaScopeProvider.kt`** -> AI Confidence: **99.48%**
1526. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JavaSymbolProvider.kt`** -> AI Confidence: **99.48%**
1527. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JavaTypeConversion.kt`** -> AI Confidence: **99.48%**
1528. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JavaUtils.kt`** -> AI Confidence: **99.48%**
1529. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/JvmSupertypeUpdater.kt`** -> AI Confidence: **99.48%**
1530. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaClass.kt`** -> AI Confidence: **99.48%**
1531. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaConstructor.kt`** -> AI Confidence: **99.48%**
1532. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaExternalAnnotation.kt`** -> AI Confidence: **99.48%**
1533. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaField.kt`** -> AI Confidence: **99.48%**
1534. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaMethod.kt`** -> AI Confidence: **99.48%**
1535. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaTypeParameter.kt`** -> AI Confidence: **99.48%**
1536. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/FirJavaValueParameter.kt`** -> AI Confidence: **99.48%**
1537. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/declarations/utils.kt`** -> AI Confidence: **99.48%**
1538. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/AnnotationsLoader.kt`** -> AI Confidence: **99.48%**
1539. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/FirJvmConstDeserializer.kt`** -> AI Confidence: **99.48%**
1540. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/FirJvmDeserializationExtension.kt`** -> AI Confidence: **99.48%**
1541. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/JvmBinaryAnnotationDeserializer.kt`** -> AI Confidence: **99.48%**
1542. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/JvmClassFileBasedSymbolProvider.kt`** -> AI Confidence: **99.48%**
1543. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/OptionalAnnotationClassesProvider.kt`** -> AI Confidence: **99.48%**
1544. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/deserialization/firBuiltinSymbolProviders.kt`** -> AI Confidence: **99.48%**
1545. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/enhancement/FirAnnotationTypeQualifierResolver.kt`** -> AI Confidence: **99.48%**
1546. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/enhancement/FirJavaAnnotationList.kt`** -> AI Confidence: **99.48%**
1547. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/enhancement/SignatureEnhancement.kt`** -> AI Confidence: **99.48%**
1548. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/enhancement/javaTypeUtils.kt`** -> AI Confidence: **99.48%**
1549. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/javaAnnotationsMapping.kt`** -> AI Confidence: **99.48%**
1550. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaAnnotationSyntheticPropertiesScope.kt`** -> AI Confidence: **99.48%**
1551. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaClassMembersEnhancementScope.kt`** -> AI Confidence: **99.48%**
1552. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaClassStaticEnhancementScope.kt`** -> AI Confidence: **99.48%**
1553. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaClassStaticUseSiteScope.kt`** -> AI Confidence: **99.48%**
1554. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaClassUseSiteMemberScope.kt`** -> AI Confidence: **99.48%**
1555. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaOverridabilityRules.kt`** -> AI Confidence: **99.48%**
1556. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaOverrideChecker.kt`** -> AI Confidence: **99.48%**
1557. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/java/scopes/JavaScopeUtils.kt`** -> AI Confidence: **99.48%**
1558. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/resolve/FirJavaClassMapper.kt`** -> AI Confidence: **99.48%**
1559. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/resolve/calls/jvm/JvmCallConflictResolverFactory.kt`** -> AI Confidence: **99.48%**
1560. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/resolve/calls/jvm/JvmPlatformOverloadsConflictResolver.kt`** -> AI Confidence: **99.48%**
1561. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/resolve/scopes/JvmMappedScopes.kt`** -> AI Confidence: **99.48%**
1562. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/scopes/jvm/FirJvmDelegatedMembersFilter.kt`** -> AI Confidence: **99.48%**
1563. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/scopes/jvm/JvmMappedScope.kt`** -> AI Confidence: **99.48%**
1564. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/scopes/jvm/SignatureUtils.kt`** -> AI Confidence: **99.48%**
1565. **`compiler/fir/fir-jvm/src/org/jetbrains/kotlin/fir/types/jvm/FirJavaTypeRef.kt`** -> AI Confidence: **99.48%**
1566. **`compiler/fir/fir-native/src/org/jetbrains/kotlin/fir/backend/native/FirNativeOverrideChecker.kt`** -> AI Confidence: **99.48%**
1567. **`compiler/fir/fir-native/src/org/jetbrains/kotlin/fir/backend/native/interop/FirObjCInterop.kt`** -> AI Confidence: **99.48%**
1568. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirAnnotationSerializer.kt`** -> AI Confidence: **99.48%**
1569. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirContractSerializer.kt`** -> AI Confidence: **99.48%**
1570. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirElementSerializer.kt`** -> AI Confidence: **99.48%**
1571. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirKLibSerializerExtension.kt`** -> AI Confidence: **99.48%**
1572. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirProvidedDeclarationsForMetadataService.kt`** -> AI Confidence: **99.48%**
1573. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirSerializerExtension.kt`** -> AI Confidence: **99.48%**
1574. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirSerializerExtensionBase.kt`** -> AI Confidence: **99.48%**
1575. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/constant/FirToConstantValueTransformer.kt`** -> AI Confidence: **99.48%**
1576. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/firKlibSerialization.kt`** -> AI Confidence: **99.48%**
1577. **`compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/serializationUtil.kt`** -> AI Confidence: **99.48%**
1578. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirBuiltinsSerializer.kt`** -> AI Confidence: **99.48%**
1579. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirDirectJavaActualDeclarationExtractor.kt`** -> AI Confidence: **99.48%**
1580. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmBackendClassResolver.kt`** -> AI Confidence: **99.48%**
1581. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmBackendExtension.kt`** -> AI Confidence: **99.48%**
1582. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmElementAwareStringTable.kt`** -> AI Confidence: **99.48%**
1583. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmSerializerExtension.kt`** -> AI Confidence: **99.48%**
1584. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmTypeMapper.kt`** -> AI Confidence: **99.48%**
1585. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirMetadataSerializer.kt`** -> AI Confidence: **99.48%**
1586. **`compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/JvmFir2IrExtensions.kt`** -> AI Confidence: **99.48%**
1587. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrBuiltinSymbolsContainer.kt`** -> AI Confidence: **99.48%**
1588. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrClassifierStorage.kt`** -> AI Confidence: **99.48%**
1589. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrCommonMemberStorage.kt`** -> AI Confidence: **99.48%**
1590. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrConversionScope.kt`** -> AI Confidence: **99.48%**
1591. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrConverter.kt`** -> AI Confidence: **99.48%**
1592. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrDeclarationStorage.kt`** -> AI Confidence: **99.48%**
1593. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrImplicitCastInserter.kt`** -> AI Confidence: **99.48%**
1594. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrIrGeneratedDeclarationsRegistrar.kt`** -> AI Confidence: **99.48%**
1595. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrPluginContext.kt`** -> AI Confidence: **99.48%**
1596. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrScopeCache.kt`** -> AI Confidence: **99.48%**
1597. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrSymbolsMappingForLazyClasses.kt`** -> AI Confidence: **99.48%**
1598. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrTypeConverter.kt`** -> AI Confidence: **99.48%**
1599. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrVisitor.kt`** -> AI Confidence: **99.48%**
1600. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/FirDeclarationsContentCleaner.kt`** -> AI Confidence: **99.48%**
1601. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/FirExportCheckerVisitor.kt`** -> AI Confidence: **99.48%**
1602. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/FirMetadataSource.kt`** -> AI Confidence: **99.48%**
1603. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/FirProviderWithGeneratedFiles.kt`** -> AI Confidence: **99.48%**
1604. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/IrBuiltInsOverFir.kt`** -> AI Confidence: **99.48%**
1605. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/AdapterGenerator.kt`** -> AI Confidence: **99.48%**
1606. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/CallAndReferenceGenerator.kt`** -> AI Confidence: **99.48%**
1607. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/ClassMemberGenerator.kt`** -> AI Confidence: **99.48%**
1608. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrCallableDeclarationsGenerator.kt`** -> AI Confidence: **99.48%**
1609. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrClassifiersGenerator.kt`** -> AI Confidence: **99.48%**
1610. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrDataClassMembersGenerator.kt`** -> AI Confidence: **99.48%**
1611. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrLazyDeclarationsGenerator.kt`** -> AI Confidence: **99.48%**
1612. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/Fir2IrLazyFakeOverrideGenerator.kt`** -> AI Confidence: **99.48%**
1613. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/OperatorExpressionGenerator.kt`** -> AI Confidence: **99.48%**
1614. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/ConstantUtils.kt`** -> AI Confidence: **99.48%**
1615. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/ImplicitConversionUtils.kt`** -> AI Confidence: **99.48%**
1616. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/IrElementsCreationUtils.kt`** -> AI Confidence: **99.48%**
1617. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/OffsetUtils.kt`** -> AI Confidence: **99.48%**
1618. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/OriginUtils.kt`** -> AI Confidence: **99.48%**
1619. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/ScopeUtils.kt`** -> AI Confidence: **99.48%**
1620. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/SymbolConversionUtils.kt`** -> AI Confidence: **99.48%**
1621. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/utils/VariousUtils.kt`** -> AI Confidence: **99.48%**
1622. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/descriptors/FirModuleDescriptor.kt`** -> AI Confidence: **99.48%**
1623. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/AbstractFir2IrLazyDeclaration.kt`** -> AI Confidence: **99.48%**
1624. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/AbstractFir2IrLazyFunction.kt`** -> AI Confidence: **99.48%**
1625. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyClass.kt`** -> AI Confidence: **99.48%**
1626. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyField.kt`** -> AI Confidence: **99.48%**
1627. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyProperty.kt`** -> AI Confidence: **99.48%**
1628. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyPropertyAccessor.kt`** -> AI Confidence: **99.48%**
1629. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazyPropertyForPureField.kt`** -> AI Confidence: **99.48%**
1630. **`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/lazy/Fir2IrLazySimpleFunction.kt`** -> AI Confidence: **99.48%**
1631. **`compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/FirResolveModularizedTotalKotlinTestPure.kt`** -> AI Confidence: **99.48%**
1632. **`compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/NonFirResolveModularizedTotalKotlinTestPure.kt`** -> AI Confidence: **99.48%**
1633. **`compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/generators/tests/GenerateModularizedIsolatedTests.kt`** -> AI Confidence: **99.48%**
1634. **`compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/moduleData.kt`** -> AI Confidence: **99.48%**
1635. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/ClassBuildingContext.kt`** -> AI Confidence: **99.48%**
1636. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/ConstructorBuildingContext.kt`** -> AI Confidence: **99.48%**
1637. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/DeclarationBuildingContext.kt`** -> AI Confidence: **99.48%**
1638. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/FunctionBuildingContext.kt`** -> AI Confidence: **99.48%**
1639. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/PropertyBuildingContext.kt`** -> AI Confidence: **99.48%**
1640. **`compiler/fir/plugin-utils/src/org/jetbrains/kotlin/fir/plugin/SimpleFunctionBuildingContext.kt`** -> AI Confidence: **99.48%**
1641. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/CopyUtils.kt`** -> AI Confidence: **99.48%**
1642. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/FirVisibilityChecker.kt`** -> AI Confidence: **99.48%**
1643. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/FirAnnotationUtils.kt`** -> AI Confidence: **99.48%**
1644. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/FirAnnotationsPlatformSpecificSupportComponent.kt`** -> AI Confidence: **99.48%**
1645. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/FirHiddenDeprecationProvider.kt`** -> AI Confidence: **99.48%**
1646. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/FirRetentionAnnotationHelpers.kt`** -> AI Confidence: **99.48%**
1647. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/GeneratedDeclarationValidation.kt`** -> AI Confidence: **99.48%**
1648. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/OperatorFunctionChecks.kt`** -> AI Confidence: **99.48%**
1649. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/ValueClassesUtils.kt`** -> AI Confidence: **99.48%**
1650. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/declarationUtils.kt`** -> AI Confidence: **99.48%**
1651. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/declarations/deprecationUtils.kt`** -> AI Confidence: **99.48%**
1652. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/expressions/FirConstChecks.kt`** -> AI Confidence: **99.48%**
1653. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/expressions/FirExpressionEvaluator.kt`** -> AI Confidence: **99.48%**
1654. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/expressions/FirInlineConstTrackerComponent.kt`** -> AI Confidence: **99.48%**
1655. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/extensions/FirDeclarationGenerationExtension.kt`** -> AI Confidence: **99.48%**
1656. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/extensions/FirExtensionDeclarationsSymbolProvider.kt`** -> AI Confidence: **99.48%**
1657. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/extensions/FirSwitchableExtensionDeclarationsSymbolProvider.kt`** -> AI Confidence: **99.48%**
1658. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/extensions/utils/AbstractSimpleClassPredicateMatchingService.kt`** -> AI Confidence: **99.48%**
1659. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/ContainingClassUtils.kt`** -> AI Confidence: **99.48%**
1660. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/ExplicitFieldsUtils.kt`** -> AI Confidence: **99.48%**
1661. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/LookupTagUtils.kt`** -> AI Confidence: **99.48%**
1662. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/ScopeUtils.kt`** -> AI Confidence: **99.48%**
1663. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/SupertypeUtils.kt`** -> AI Confidence: **99.48%**
1664. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/ToSymbolUtils.kt`** -> AI Confidence: **99.48%**
1665. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/TypeExpansionUtils.kt`** -> AI Confidence: **99.48%**
1666. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/calls/FirReceivers.kt`** -> AI Confidence: **99.48%**
1667. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/calls/ImplicitValue.kt`** -> AI Confidence: **99.48%**
1668. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/calls/Synthetics.kt`** -> AI Confidence: **99.48%**
1669. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/FirCachedSymbolNamesProvider.kt`** -> AI Confidence: **99.48%**
1670. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/FirProvider.kt`** -> AI Confidence: **99.48%**
1671. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/FirSymbolProvider.kt`** -> AI Confidence: **99.48%**
1672. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirCachingCompositeSymbolProvider.kt`** -> AI Confidence: **99.48%**
1673. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirCompositeSymbolProvider.kt`** -> AI Confidence: **99.48%**
1674. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/transformers/PhaseUtils.kt`** -> AI Confidence: **99.48%**
1675. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/transformers/ReturnTypeCalculatorForFullBodyResolve.kt`** -> AI Confidence: **99.48%**
1676. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/CallableCopyTypeCalculator.kt`** -> AI Confidence: **99.48%**
1677. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/FirIntersectionScopeOverrideChecker.kt`** -> AI Confidence: **99.48%**
1678. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/FirKotlinScopeProvider.kt`** -> AI Confidence: **99.48%**
1679. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/FirOverrideService.kt`** -> AI Confidence: **99.48%**
1680. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/FirPlatformClassMapper.kt`** -> AI Confidence: **99.48%**
1681. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/PlatformSpecificOverridabilityRules.kt`** -> AI Confidence: **99.48%**
1682. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/Scopes.kt`** -> AI Confidence: **99.48%**
1683. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/AbstractFirOverrideScope.kt`** -> AI Confidence: **99.48%**
1684. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/AbstractFirUseSiteMemberScope.kt`** -> AI Confidence: **99.48%**
1685. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirAbstractImportingScope.kt`** -> AI Confidence: **99.48%**
1686. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirAbstractProviderBasedScope.kt`** -> AI Confidence: **99.48%**
1687. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirAbstractSimpleImportingScope.kt`** -> AI Confidence: **99.48%**
1688. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirAbstractStarImportingScope.kt`** -> AI Confidence: **99.48%**
1689. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirClassAnySynthesizedMemberScope.kt`** -> AI Confidence: **99.48%**
1690. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirClassDeclaredMemberScope.kt`** -> AI Confidence: **99.48%**
1691. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirClassSubstitutionScope.kt`** -> AI Confidence: **99.48%**
1692. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirClassUseSiteMemberScope.kt`** -> AI Confidence: **99.48%**
1693. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirDeclaredMemberScopeProvider.kt`** -> AI Confidence: **99.48%**
1694. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirDefaultStarImportingScope.kt`** -> AI Confidence: **99.48%**
1695. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirDelegatedMemberScope.kt`** -> AI Confidence: **99.48%**
1696. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirDynamicScope.kt`** -> AI Confidence: **99.48%**
1697. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirEnumEntriesSupport.kt`** -> AI Confidence: **99.48%**
1698. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirFakeOverrideGenerator.kt`** -> AI Confidence: **99.48%**
1699. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirGeneratedScopes.kt`** -> AI Confidence: **99.48%**
1700. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirIntegerConstantOperatorScope.kt`** -> AI Confidence: **99.48%**
1701. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirLazyNestedClassifierScope.kt`** -> AI Confidence: **99.48%**
1702. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirLocalScope.kt`** -> AI Confidence: **99.48%**
1703. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirMemberTypeParameterScope.kt`** -> AI Confidence: **99.48%**
1704. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirNestedClassifierScope.kt`** -> AI Confidence: **99.48%**
1705. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirNestedClassifierScopeWithSubstitution.kt`** -> AI Confidence: **99.48%**
1706. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirOnlyCallablesScope.kt`** -> AI Confidence: **99.48%**
1707. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirOnlyClassifiersScope.kt`** -> AI Confidence: **99.48%**
1708. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirOverrideUtils.kt`** -> AI Confidence: **99.48%**
1709. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirPackageMemberScope.kt`** -> AI Confidence: **99.48%**
1710. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirScopeWithCallableCopyReturnTypeUpdater.kt`** -> AI Confidence: **99.48%**
1711. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirScriptDeclarationsScope.kt`** -> AI Confidence: **99.48%**
1712. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirSingleLevelDefaultStarImportingScope.kt`** -> AI Confidence: **99.48%**
1713. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirStandardOverrideChecker.kt`** -> AI Confidence: **99.48%**
1714. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirStaticScope.kt`** -> AI Confidence: **99.48%**
1715. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirTrivialEnumEntryScope.kt`** -> AI Confidence: **99.48%**
1716. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirTypeIntersectionScope.kt`** -> AI Confidence: **99.48%**
1717. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/FirTypeIntersectionScopeContext.kt`** -> AI Confidence: **99.48%**
1718. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/scopes/impl/TypeAliasConstructorsSubstitutingScope.kt`** -> AI Confidence: **99.48%**
1719. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/ConeInferenceContext.kt`** -> AI Confidence: **99.48%**
1720. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/ConeTypeContext.kt`** -> AI Confidence: **99.48%**
1721. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/FirCorrespondingSupertypesCache.kt`** -> AI Confidence: **99.48%**
1722. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/FirFunctionTypeKindServiceImpl.kt`** -> AI Confidence: **99.48%**
1723. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/FirMissingDependencyStorage.kt`** -> AI Confidence: **99.48%**
1724. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/FunctionalTypeUtils.kt`** -> AI Confidence: **99.48%**
1725. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/InferenceUtils.kt`** -> AI Confidence: **99.48%**
1726. **`compiler/fir/providers/src/org/jetbrains/kotlin/fir/types/TypeUtils.kt`** -> AI Confidence: **99.48%**
1727. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/LightTree2Fir.kt`** -> AI Confidence: **99.48%**
1728. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/LightTreeParsingErrorListener.kt`** -> AI Confidence: **99.48%**
1729. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/AbstractLightTreeRawFirBuilder.kt`** -> AI Confidence: **99.48%**
1730. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/ConverterUtil.kt`** -> AI Confidence: **99.48%**
1731. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirDeclarationBuilder.kt`** -> AI Confidence: **99.48%**
1732. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirExpressionBuilder.kt`** -> AI Confidence: **99.48%**
1733. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/fir/ClassWrapper.kt`** -> AI Confidence: **99.48%**
1734. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/fir/DestructuringDeclaration.kt`** -> AI Confidence: **99.48%**
1735. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/fir/ValueParameter.kt`** -> AI Confidence: **99.48%**
1736. **`compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/fir/WhenEntry.kt`** -> AI Confidence: **99.48%**
1737. **`compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiConversionUtils.kt`** -> AI Confidence: **99.48%**
1738. **`compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiRawFirBuilder.kt`** -> AI Confidence: **99.48%**
1739. **`compiler/fir/raw-fir/psi2fir/testFixtures/org/jetbrains/kotlin/fir/builder/AbstractRawFirBuilderSourceElementMappingTestCase.kt`** -> AI Confidence: **99.48%**
1740. **`compiler/fir/raw-fir/psi2fir/testFixtures/org/jetbrains/kotlin/fir/builder/AbstractRawFirBuilderTestCase.kt`** -> AI Confidence: **99.48%**
1741. **`compiler/fir/raw-fir/psi2fir/tests/org/jetbrains/kotlin/fir/builder/RawFirBuilderTotalKotlinTestCase.kt`** -> AI Confidence: **99.48%**
1742. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/AbstractRawFirBuilder.kt`** -> AI Confidence: **99.48%**
1743. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/Context.kt`** -> AI Confidence: **99.48%**
1744. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/ConversionUtils.kt`** -> AI Confidence: **99.48%**
1745. **`compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/Destructuring.kt`** -> AI Confidence: **99.48%**
1746. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirExpressionResolutionExtension.kt`** -> AI Confidence: **99.48%**
1747. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirPredicateBasedProviderImpl.kt`** -> AI Confidence: **99.48%**
1748. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirRegisteredPluginAnnotations.kt`** -> AI Confidence: **99.48%**
1749. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirStatusTransformerExtension.kt`** -> AI Confidence: **99.48%**
1750. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/FirSupertypeGenerationExtension.kt`** -> AI Confidence: **99.48%**
1751. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/RawUserTypeBuilder.kt`** -> AI Confidence: **99.48%**
1752. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/extensions/generatedDeclarationsUtils.kt`** -> AI Confidence: **99.48%**
1753. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/CollectionLiteralResolution.kt`** -> AI Confidence: **99.48%**
1754. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/CollectionLiteralResolutionUtils.kt`** -> AI Confidence: **99.48%**
1755. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/ContextSensitiveResolutionUtils.kt`** -> AI Confidence: **99.48%**
1756. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirDefaultParametersResolver.kt`** -> AI Confidence: **99.48%**
1757. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirDoubleColonExpressionResolver.kt`** -> AI Confidence: **99.48%**
1758. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirOuterClassManager.kt`** -> AI Confidence: **99.48%**
1759. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirSamResolver.kt`** -> AI Confidence: **99.48%**
1760. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/FirTypeResolver.kt`** -> AI Confidence: **99.48%**
1761. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/ImplicitIntegerCoercion.kt`** -> AI Confidence: **99.48%**
1762. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/QualifiedNameResolution.kt`** -> AI Confidence: **99.48%**
1763. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/ResolveUtils.kt`** -> AI Confidence: **99.48%**
1764. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/StdlibFactoryFunctionsUtils.kt`** -> AI Confidence: **99.48%**
1765. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/ArgumentUtils.kt`** -> AI Confidence: **99.48%**
1766. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/ConeResolutionAtoms.kt`** -> AI Confidence: **99.48%**
1767. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/ConstructorProcessing.kt`** -> AI Confidence: **99.48%**
1768. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/FirCallResolver.kt`** -> AI Confidence: **99.48%**
1769. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/QualifierReceiver.kt`** -> AI Confidence: **99.48%**
1770. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/SuperCalls.kt`** -> AI Confidence: **99.48%**
1771. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/VisibilityUtils.kt`** -> AI Confidence: **99.48%**
1772. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/CallInfo.kt`** -> AI Confidence: **99.48%**
1773. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/Candidate.kt`** -> AI Confidence: **99.48%**
1774. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/CandidateCollector.kt`** -> AI Confidence: **99.48%**
1775. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/CandidateFactory.kt`** -> AI Confidence: **99.48%**
1776. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/candidate/FirNamedReferenceWithCandidate.kt`** -> AI Confidence: **99.48%**
1777. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/ConeCallConflictResolver.kt`** -> AI Confidence: **99.48%**
1778. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/ConeOverloadConflictResolver.kt`** -> AI Confidence: **99.48%**
1779. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/EagerLambdaResolution.kt`** -> AI Confidence: **99.48%**
1780. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/FirDeclarationOverloadabilityHelperImpl.kt`** -> AI Confidence: **99.48%**
1781. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/overloads/FirOverloadByLambdaReturnTypeResolver.kt`** -> AI Confidence: **99.48%**
1782. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/ArgumentCheckingProcessor.kt`** -> AI Confidence: **99.48%**
1783. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/CheckArguments.kt`** -> AI Confidence: **99.48%**
1784. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/CheckCallableReferenceExpectedType.kt`** -> AI Confidence: **99.48%**
1785. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/CollectTypeVariableUsagesInfo.kt`** -> AI Confidence: **99.48%**
1786. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/CreateFreshTypeVariableSubstitutorStage.kt`** -> AI Confidence: **99.48%**
1787. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/FirArgumentsToParametersMapper.kt`** -> AI Confidence: **99.48%**
1788. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/ResolutionStageRunner.kt`** -> AI Confidence: **99.48%**
1789. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/ResolutionStages.kt`** -> AI Confidence: **99.48%**
1790. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/TypeArgumentMapping.kt`** -> AI Confidence: **99.48%**
1791. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/FirInvokeResolveTowerExtension.kt`** -> AI Confidence: **99.48%**
1792. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/FirTowerResolveTask.kt`** -> AI Confidence: **99.48%**
1793. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/FirTowerResolver.kt`** -> AI Confidence: **99.48%**
1794. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/TowerLevelHandler.kt`** -> AI Confidence: **99.48%**
1795. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/TowerLevels.kt`** -> AI Confidence: **99.48%**
1796. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/tower/TowerResolveManager.kt`** -> AI Confidence: **99.48%**
1797. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirDataFlowAnalyzer.kt`** -> AI Confidence: **99.48%**
1798. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirLocalVariableAssignmentAnalyzer.kt`** -> AI Confidence: **99.48%**
1799. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/CollectionLiteralBoundsCollector.kt`** -> AI Confidence: **99.48%**
1800. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/CompletionModeCalculator.kt`** -> AI Confidence: **99.48%**
1801. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/ConeConstraintSystemUtilContext.kt`** -> AI Confidence: **99.48%**
1802. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/ConstraintSystemCompleter.kt`** -> AI Confidence: **99.48%**
1803. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirCallCompleter.kt`** -> AI Confidence: **99.48%**
1804. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirDelegatedPropertyInferenceSession.kt`** -> AI Confidence: **99.48%**
1805. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirInferenceLogger.kt`** -> AI Confidence: **99.48%**
1806. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirInferenceSession.kt`** -> AI Confidence: **99.48%**
1807. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/FirPCLAInferenceSession.kt`** -> AI Confidence: **99.48%**
1808. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/InferenceComponents.kt`** -> AI Confidence: **99.48%**
1809. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/InferenceUtils.kt`** -> AI Confidence: **99.48%**
1810. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/inference/PostponedArgumentsAnalyzer.kt`** -> AI Confidence: **99.48%**
1811. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/optimization/FirReachabilityAnalyzer.kt`** -> AI Confidence: **99.48%**
1812. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirCloneableSymbolProvider.kt`** -> AI Confidence: **99.48%**
1813. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirCommonDeclarationsMappingSymbolProvider.kt`** -> AI Confidence: **99.48%**
1814. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirLibrarySessionProvider.kt`** -> AI Confidence: **99.48%**
1815. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirProviderImpl.kt`** -> AI Confidence: **99.48%**
1816. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirQualifierResolverImpl.kt`** -> AI Confidence: **99.48%**
1817. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirTypeCandidateCollector.kt`** -> AI Confidence: **99.48%**
1818. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/providers/impl/FirTypeResolverImpl.kt`** -> AI Confidence: **99.48%**
1819. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirCallCompletionResultsWriterTransformer.kt`** -> AI Confidence: **99.48%**
1820. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirConstantEvaluationProcessor.kt`** -> AI Confidence: **99.48%**
1821. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirImportResolveTransformer.kt`** -> AI Confidence: **99.48%**
1822. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirResolveProcessor.kt`** -> AI Confidence: **99.48%**
1823. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirSealedClassInheritorsProcessor.kt`** -> AI Confidence: **99.48%**
1824. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirSpecificTypeResolverTransformer.kt`** -> AI Confidence: **99.48%**
1825. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirStatusResolveTransformer.kt`** -> AI Confidence: **99.48%**
1826. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirStatusResolver.kt`** -> AI Confidence: **99.48%**
1827. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirSupertypesResolution.kt`** -> AI Confidence: **99.48%**
1828. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirSyntheticCallGenerator.kt`** -> AI Confidence: **99.48%**
1829. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirTotalResolveProcessor.kt`** -> AI Confidence: **99.48%**
1830. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirTypeResolveTransformer.kt`** -> AI Confidence: **99.48%**
1831. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirWhenExhaustivenessComputer.kt`** -> AI Confidence: **99.48%**
1832. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/IntegerLiteralAndOperatorApproximationTransformer.kt`** -> AI Confidence: **99.48%**
1833. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/LambdaArgumentEffectsTransformer.kt`** -> AI Confidence: **99.48%**
1834. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/TransformUtils.kt`** -> AI Confidence: **99.48%**
1835. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/BodyResolveContext.kt`** -> AI Confidence: **99.48%**
1836. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/BodyResolveUtils.kt`** -> AI Confidence: **99.48%**
1837. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/DeclarationApproximationUtils.kt`** -> AI Confidence: **99.48%**
1838. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirAbstractBodyResolveTransformer.kt`** -> AI Confidence: **99.48%**
1839. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirAbstractBodyResolveTransformerDispatcher.kt`** -> AI Confidence: **99.48%**
1840. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirArrayOfCallTransformer.kt`** -> AI Confidence: **99.48%**
1841. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirBodyResolveTransformerAdapters.kt`** -> AI Confidence: **99.48%**
1842. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirControlFlowStatementsResolveTransformer.kt`** -> AI Confidence: **99.48%**
1843. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirDeclarationsResolveTransformer.kt`** -> AI Confidence: **99.48%**
1844. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt`** -> AI Confidence: **99.48%**
1845. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirImplicitBodyResolve.kt`** -> AI Confidence: **99.48%**
1846. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/LocalClassesResolution.kt`** -> AI Confidence: **99.48%**
1847. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/bareTypes.kt`** -> AI Confidence: **99.48%**
1848. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/setUnnamedContextParameterNames.kt`** -> AI Confidence: **99.48%**
1849. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/contracts/ConeEffectExtractor.kt`** -> AI Confidence: **99.48%**
1850. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/contracts/FirAbstractContractResolveTransformerDispatcher.kt`** -> AI Confidence: **99.48%**
1851. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/contracts/FirContractResolveTransformerAdapter.kt`** -> AI Confidence: **99.48%**
1852. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/mpp/FirExpectActualMatcherTransformer.kt`** -> AI Confidence: **99.48%**
1853. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/mpp/FirExpectActualMatchingContextImpl.kt`** -> AI Confidence: **99.48%**
1854. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/mpp/FirExpectActualResolver.kt`** -> AI Confidence: **99.48%**
1855. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/mpp/annotationCompareUtils.kt`** -> AI Confidence: **99.48%**
1856. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/AbstractFirSpecificAnnotationResolveTransformer.kt`** -> AI Confidence: **99.48%**
1857. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/FirAnnotationArgumentsProcessor.kt`** -> AI Confidence: **99.48%**
1858. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/FirAnnotationArgumentsTransformer.kt`** -> AI Confidence: **99.48%**
1859. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/FirCompanionGenerationProcessor.kt`** -> AI Confidence: **99.48%**
1860. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/plugin/FirCompilerRequiredAnnotationsResolveTransformer.kt`** -> AI Confidence: **99.48%**
1861. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/scopes/ImportingScopes.kt`** -> AI Confidence: **99.48%**
1862. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/scopes/impl/FirActualizingScope.kt`** -> AI Confidence: **99.48%**
1863. **`compiler/fir/resolve/src/org/jetbrains/kotlin/fir/scopes/impl/FirDefaultSimpleImportingScope.kt`** -> AI Confidence: **99.48%**
1864. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/EffectiveVisibilityUtils.kt`** -> AI Confidence: **99.48%**
1865. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/FirEqualsOverrideHelpers.kt`** -> AI Confidence: **99.48%**
1866. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/FirLookupTrackerComponent.kt`** -> AI Confidence: **99.48%**
1867. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/PrivateToThisUtils.kt`** -> AI Confidence: **99.48%**
1868. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/ScopeUtils.kt`** -> AI Confidence: **99.48%**
1869. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/declarations/ArrayOfUtils.kt`** -> AI Confidence: **99.48%**
1870. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/declarations/FirMustUseReturnValueStatusComponent.kt`** -> AI Confidence: **99.48%**
1871. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/declarations/ImplicitReceiverUtils.kt`** -> AI Confidence: **99.48%**
1872. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/expressions/ReferenceUtils.kt`** -> AI Confidence: **99.48%**
1873. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/expressions/SubstitutionUtils.kt`** -> AI Confidence: **99.48%**
1874. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/mainFunctionDetection.kt`** -> AI Confidence: **99.48%**
1875. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/CallableIdUtils.kt`** -> AI Confidence: **99.48%**
1876. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/ContextSensitiveResolution.kt`** -> AI Confidence: **99.48%**
1877. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/DeclarationUtils.kt`** -> AI Confidence: **99.48%**
1878. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/ImplicitValueStorage.kt`** -> AI Confidence: **99.48%**
1879. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/LocalVariableScopeStorage.kt`** -> AI Confidence: **99.48%**
1880. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/calls/ResolutionDiagnostic.kt`** -> AI Confidence: **99.48%**
1881. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/calls/TypeVariableTypeRemovingSubstitutor.kt`** -> AI Confidence: **99.48%**
1882. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/DfaVariables.kt`** -> AI Confidence: **99.48%**
1883. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/LogicSystem.kt`** -> AI Confidence: **99.48%**
1884. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/VariableStorage.kt`** -> AI Confidence: **99.48%**
1885. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/cfg/CFGNode.kt`** -> AI Confidence: **99.48%**
1886. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/cfg/CFGNodeRenderer.kt`** -> AI Confidence: **99.48%**
1887. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/cfg/ControlFlowGraphRenderer.kt`** -> AI Confidence: **99.48%**
1888. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/contracts.kt`** -> AI Confidence: **99.48%**
1889. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/dfa/model.kt`** -> AI Confidence: **99.48%**
1890. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/diagnostics/ConeDiagnostics.kt`** -> AI Confidence: **99.48%**
1891. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/inference/model/FirConstraintPositionAndErrors.kt`** -> AI Confidence: **99.48%**
1892. **`compiler/fir/semantics/src/org/jetbrains/kotlin/fir/resolve/transformers/publishedApiEffectiveVisibility.kt`** -> AI Confidence: **99.48%**
1893. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/ClassMembers.kt`** -> AI Confidence: **99.48%**
1894. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/EnumClassUtils.kt`** -> AI Confidence: **99.48%**
1895. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/FirGeneration.kt`** -> AI Confidence: **99.48%**
1896. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/FirSession.kt`** -> AI Confidence: **99.48%**
1897. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/Primitives.kt`** -> AI Confidence: **99.48%**
1898. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/Utils.kt`** -> AI Confidence: **99.48%**
1899. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/contracts/description/ConeContractRenderer.kt`** -> AI Confidence: **99.48%**
1900. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/DeprecationsProvider.kt`** -> AI Confidence: **99.48%**
1901. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/ExpectActualAttributes.kt`** -> AI Confidence: **99.48%**
1902. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/FirDeclarationAttributes.kt`** -> AI Confidence: **99.48%**
1903. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/impl/FirDeclarationStatusImpl.kt`** -> AI Confidence: **99.48%**
1904. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/impl/FirDefaultPropertyAccessor.kt`** -> AI Confidence: **99.48%**
1905. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/synthetic/FirSyntheticProperty.kt`** -> AI Confidence: **99.48%**
1906. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/synthetic/FirSyntheticPropertyBuilder.kt`** -> AI Confidence: **99.48%**
1907. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/utils/FirDeclarationUtil.kt`** -> AI Confidence: **99.48%**
1908. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/declarations/utils/declarationAttributes.kt`** -> AI Confidence: **99.48%**
1909. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/diagnostics/ConeSimpleDiagnostic.kt`** -> AI Confidence: **99.48%**
1910. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/FirArgumentUtil.kt`** -> AI Confidence: **99.48%**
1911. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/FirExpressionUtil.kt`** -> AI Confidence: **99.48%**
1912. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/builder/FirAnnotationArgumentMappingBuilder.kt`** -> AI Confidence: **99.48%**
1913. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/builder/FirAnonymousFunctionExpressionBuilder.kt`** -> AI Confidence: **99.48%**
1914. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/builder/FirAnonymousObjectExpressionBuilder.kt`** -> AI Confidence: **99.48%**
1915. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/builder/FirConstExpressionBuilder.kt`** -> AI Confidence: **99.48%**
1916. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/impl/FirAnnotationArgumentMappingImpl.kt`** -> AI Confidence: **99.48%**
1917. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/impl/FirAnonymousFunctionExpressionImpl.kt`** -> AI Confidence: **99.48%**
1918. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/impl/FirAnonymousObjectExpressionImpl.kt`** -> AI Confidence: **99.48%**
1919. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/impl/FirContractCallBlock.kt`** -> AI Confidence: **99.48%**
1920. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/impl/FirResolvedArgumentList.kt`** -> AI Confidence: **99.48%**
1921. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/expressions/impl/FirSingleExpressionBlock.kt`** -> AI Confidence: **99.48%**
1922. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/extensions/FirExtensionService.kt`** -> AI Confidence: **99.48%**
1923. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/extensions/FirPredicateBasedProvider.kt`** -> AI Confidence: **99.48%**
1924. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/references/FirReferenceUtils.kt`** -> AI Confidence: **99.48%**
1925. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirAnnotationRenderer.kt`** -> AI Confidence: **99.48%**
1926. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirCallableSignatureRenderer.kt`** -> AI Confidence: **99.48%**
1927. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirDeclarationRenderer.kt`** -> AI Confidence: **99.48%**
1928. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirModifierRenderer.kt`** -> AI Confidence: **99.48%**
1929. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirRenderer.kt`** -> AI Confidence: **99.48%**
1930. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/renderer/FirResolvedNamedReferenceRenderer.kt`** -> AI Confidence: **99.48%**
1931. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/scopes/FirCompositeScope.kt`** -> AI Confidence: **99.48%**
1932. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/scopes/FirDelegatingContainingNamesAwareScope.kt`** -> AI Confidence: **99.48%**
1933. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/scopes/FirTypeScope.kt`** -> AI Confidence: **99.48%**
1934. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/FirBasedSymbol.kt`** -> AI Confidence: **99.48%**
1935. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/FirLazyDeclarationResolver.kt`** -> AI Confidence: **99.48%**
1936. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/FirCallableSymbol.kt`** -> AI Confidence: **99.48%**
1937. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/FirClassLikeSymbol.kt`** -> AI Confidence: **99.48%**
1938. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/FirFunctionSymbol.kt`** -> AI Confidence: **99.48%**
1939. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/FirTypeParameterSymbol.kt`** -> AI Confidence: **99.48%**
1940. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/FirVariableSymbol.kt`** -> AI Confidence: **99.48%**
1941. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/symbols/impl/Utils.kt`** -> AI Confidence: **99.48%**
1942. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/ConeIntegerLiteralTypeImpl.kt`** -> AI Confidence: **99.48%**
1943. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/FirFunctionTypeKindService.kt`** -> AI Confidence: **99.48%**
1944. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/FirTypeUtils.kt`** -> AI Confidence: **99.48%**
1945. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/ParameterNameTypeAttribute.kt`** -> AI Confidence: **99.48%**
1946. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/builder/FirErrorTypeRefBuilder.kt`** -> AI Confidence: **99.48%**
1947. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/builder/FirUserTypeRefBuilder.kt`** -> AI Confidence: **99.48%**
1948. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/impl/FirErrorTypeRefImpl.kt`** -> AI Confidence: **99.48%**
1949. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/impl/FirImplicitBuiltinTypeRef.kt`** -> AI Confidence: **99.48%**
1950. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/impl/FirUserTypeRefImpl.kt`** -> AI Confidence: **99.48%**
1951. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/types/impl/ResolvedImplicitTypeRef.kt`** -> AI Confidence: **99.48%**
1952. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/utils/exceptions/firExceptionUtils.kt`** -> AI Confidence: **99.48%**
1953. **`compiler/fir/tree/src/org/jetbrains/kotlin/fir/visitors/FirDefaultTransformer.kt`** -> AI Confidence: **99.48%**
1954. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/FirTree.kt`** -> AI Confidence: **99.48%**
1955. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/ImplementationConfigurator.kt`** -> AI Confidence: **99.48%**
1956. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/Main.kt`** -> AI Confidence: **99.48%**
1957. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/printer/BuilderPrinter.kt`** -> AI Confidence: **99.48%**
1958. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/printer/ImplementationPrinter.kt`** -> AI Confidence: **99.48%**
1959. **`compiler/fir/tree/tree-generator/src/org/jetbrains/kotlin/fir/tree/generator/printer/utils.kt`** -> AI Confidence: **99.48%**
1960. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/cfg/UnreachableCode.kt`** -> AI Confidence: **99.48%**
1961. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/LightTreePositioningStrategies.kt`** -> AI Confidence: **99.48%**
1962. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/LightTreePositioningStrategy.kt`** -> AI Confidence: **99.48%**
1963. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PositioningStrategies.kt`** -> AI Confidence: **99.48%**
1964. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PositioningStrategy.kt`** -> AI Confidence: **99.48%**
1965. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PsiPositioningStrategies.kt`** -> AI Confidence: **99.48%**
1966. **`compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/rendering/CommonRenderers.kt`** -> AI Confidence: **99.48%**
1967. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/fileClasses/JvmFileClassUtil.kt`** -> AI Confidence: **99.48%**
1968. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaClassImpl.kt`** -> AI Confidence: **99.48%**
1969. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaElementCollectionFromPsiArrayUtil.kt`** -> AI Confidence: **99.48%**
1970. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/JavaPackageImpl.kt`** -> AI Confidence: **99.48%**
1971. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/annotationArgumentsImpl.kt`** -> AI Confidence: **99.48%**
1972. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/Annotations.kt`** -> AI Confidence: **99.48%**
1973. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/BinaryClassSignatureParser.kt`** -> AI Confidence: **99.48%**
1974. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/BinaryJavaClass.kt`** -> AI Confidence: **99.48%**
1975. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/ClassifierResolutionContext.kt`** -> AI Confidence: **99.48%**
1976. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/java/structure/impl/classFiles/Methods.kt`** -> AI Confidence: **99.48%**
1977. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/KotlinBinaryClassCache.kt`** -> AI Confidence: **99.48%**
1978. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/PackagePartClassUtils.kt`** -> AI Confidence: **99.48%**
1979. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/VirtualFileFinder.kt`** -> AI Confidence: **99.48%**
1980. **`compiler/frontend.common.jvm/src/org/jetbrains/kotlin/load/kotlin/VirtualFileKotlinClass.kt`** -> AI Confidence: **99.48%**
1981. **`compiler/frontend.common/src/org/jetbrains/kotlin/KtSourceElement.kt`** -> AI Confidence: **99.48%**
1982. **`compiler/frontend.common/src/org/jetbrains/kotlin/diagnostics/KtDiagnostic.kt`** -> AI Confidence: **99.48%**
1983. **`compiler/frontend.common/src/org/jetbrains/kotlin/diagnostics/KtDiagnosticFactory.kt`** -> AI Confidence: **99.48%**
1984. **`compiler/frontend.common/src/org/jetbrains/kotlin/diagnostics/impl/PendingDiagnosticsReporterImpl.kt`** -> AI Confidence: **99.48%**
1985. **`compiler/frontend.common/src/org/jetbrains/kotlin/util/AnalysisExceptions.kt`** -> AI Confidence: **99.48%**
1986. **`compiler/frontend.common/src/org/jetbrains/kotlin/util/ServiceLoaderLite.kt`** -> AI Confidence: **99.48%**
1987. **`compiler/frontend.common/src/org/jetbrains/kotlin/util/metadataHelpers.kt`** -> AI Confidence: **99.48%**
1988. **`compiler/frontend.java/src/org/jetbrains/kotlin/frontend/java/di/injection.kt`** -> AI Confidence: **99.48%**
1989. **`compiler/frontend.java/src/org/jetbrains/kotlin/inline/inlineUtil.kt`** -> AI Confidence: **99.48%**
1990. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/AbstractJavaClassFinder.kt`** -> AI Confidence: **99.48%**
1991. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/JavaClassFinderImpl.kt`** -> AI Confidence: **99.48%**
1992. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/components/AbstractJavaResolverCache.kt`** -> AI Confidence: **99.48%**
1993. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/components/FilesByFacadeFqNameIndexer.kt`** -> AI Confidence: **99.48%**
1994. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/components/LazyResolveBasedCache.kt`** -> AI Confidence: **99.48%**
1995. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/java/sam/JavaBasedSamConversionResolver.kt`** -> AI Confidence: **99.48%**
1996. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/kotlin/incremental/IncrementalPackageFragmentProvider.kt`** -> AI Confidence: **99.48%**
1997. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/kotlin/incremental/IncrementalPackagePartProvider.kt`** -> AI Confidence: **99.48%**
1998. **`compiler/frontend.java/src/org/jetbrains/kotlin/load/kotlin/moduleVisibilityUtils.kt`** -> AI Confidence: **99.48%**
1999. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmAdditionalClassPartsProvider.kt`** -> AI Confidence: **99.48%**
2000. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmDeclarationReturnTypeSanitizer.kt`** -> AI Confidence: **99.48%**
2001. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmDelegationFilter.kt`** -> AI Confidence: **99.48%**
2002. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmOverloadFilter.kt`** -> AI Confidence: **99.48%**
2003. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmOverridesBackwardCompatibilityHelper.kt`** -> AI Confidence: **99.48%**
2004. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmPlatformAnnotationFeaturesSupport.kt`** -> AI Confidence: **99.48%**
2005. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmPlatformOverloadsSpecificityComparator.kt`** -> AI Confidence: **99.48%**
2006. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/JvmResolverForModuleFactory.kt`** -> AI Confidence: **99.48%**
2007. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/RuntimeAssertions.kt`** -> AI Confidence: **99.48%**
2008. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/annotations/jvmAnnotationUtil.kt`** -> AI Confidence: **99.48%**
2009. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ApiVersionIsAtLeastArgumentsChecker.kt`** -> AI Confidence: **99.48%**
2010. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/BadInheritedJavaSignaturesChecker.kt`** -> AI Confidence: **99.48%**
2011. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ClassInheritsJavaSealedClassChecker.kt`** -> AI Confidence: **99.48%**
2012. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/DefaultCheckerInTailrec.kt`** -> AI Confidence: **99.48%**
2013. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/EnumDeclaringClassDeprecationChecker.kt`** -> AI Confidence: **99.48%**
2014. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ExplicitMetadataChecker.kt`** -> AI Confidence: **99.48%**
2015. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ExternalFunChecker.kt`** -> AI Confidence: **99.48%**
2016. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/FileClassAnnotationsChecker.kt`** -> AI Confidence: **99.48%**
2017. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/InconsistentOperatorFromJavaCallChecker.kt`** -> AI Confidence: **99.48%**
2018. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/InlinePlatformCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
2019. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/InterfaceDefaultMethodCallChecker.kt`** -> AI Confidence: **99.48%**
2020. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaAnnotationCallChecker.kt`** -> AI Confidence: **99.48%**
2021. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaClassOnCompanionChecker.kt`** -> AI Confidence: **99.48%**
2022. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaNullabilityChecker.kt`** -> AI Confidence: **99.48%**
2023. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaOverrideWithWrongNullabilityOverrideChecker.kt`** -> AI Confidence: **99.48%**
2024. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JavaTypeAccessibilityChecker.kt`** -> AI Confidence: **99.48%**
2025. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmAnnotationsTargetNonExistentAccessorChecker.kt`** -> AI Confidence: **99.48%**
2026. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmArrayVariableInLoopAssignmentChecker.kt`** -> AI Confidence: **99.48%**
2027. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmDefaultChecker.kt`** -> AI Confidence: **99.48%**
2028. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmFieldApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
2029. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmInlineApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
2030. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmModuleAccessibilityChecker.kt`** -> AI Confidence: **99.48%**
2031. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmMultifileClassStateChecker.kt`** -> AI Confidence: **99.48%**
2032. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmPropertyVsFieldAmbiguityCallChecker.kt`** -> AI Confidence: **99.48%**
2033. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmRecordApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
2034. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmSerializableLambdaAnnotationChecker.kt`** -> AI Confidence: **99.48%**
2035. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmSimpleNameBacktickChecker.kt`** -> AI Confidence: **99.48%**
2036. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmSyntheticApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
2037. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/JvmSyntheticAssignmentChecker.kt`** -> AI Confidence: **99.48%**
2038. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/MissingBuiltInDeclarationChecker.kt`** -> AI Confidence: **99.48%**
2039. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/PolymorphicSignatureCallChecker.kt`** -> AI Confidence: **99.48%**
2040. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ProtectedInSuperClassCompanionCallChecker.kt`** -> AI Confidence: **99.48%**
2041. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/ProtectedSyntheticExtensionCallChecker.kt`** -> AI Confidence: **99.48%**
2042. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/RepeatableAnnotationChecker.kt`** -> AI Confidence: **99.48%**
2043. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SamInterfaceConstructorReferenceCallChecker.kt`** -> AI Confidence: **99.48%**
2044. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/StrictfpApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
2045. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SuperCallWithDefaultArgumentsChecker.kt`** -> AI Confidence: **99.48%**
2046. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SuspendInFunInterfaceChecker.kt`** -> AI Confidence: **99.48%**
2047. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SuspensionPointInsideMutexLockChecker.kt`** -> AI Confidence: **99.48%**
2048. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/SynchronizedAnnotationOnLambdaChecker.kt`** -> AI Confidence: **99.48%**
2049. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/UnsupportedSyntheticCallableReferenceChecker.kt`** -> AI Confidence: **99.48%**
2050. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/UpperBoundViolatedInTypealiasConstructorChecker.kt`** -> AI Confidence: **99.48%**
2051. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/WarningAwareUpperBoundChecker.kt`** -> AI Confidence: **99.48%**
2052. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/checkers/declarationCheckers.kt`** -> AI Confidence: **99.48%**
2053. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/jvmConstants.kt`** -> AI Confidence: **99.48%**
2054. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/modules/JavaModuleInfo.kt`** -> AI Confidence: **99.48%**
2055. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/multiplatform/JavaActualAnnotationArgumentExtractor.kt`** -> AI Confidence: **99.48%**
2056. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/multiplatform/OptionalAnnotationPackageFragmentProvider.kt`** -> AI Confidence: **99.48%**
2057. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/platform/JavaGenericVarianceViolationTypeChecker.kt`** -> AI Confidence: **99.48%**
2058. **`compiler/frontend.java/src/org/jetbrains/kotlin/resolve/jvm/platform/JvmDefaultImportsProvider.kt`** -> AI Confidence: **99.48%**
2059. **`compiler/frontend.java/src/org/jetbrains/kotlin/synthetic/JavaSyntheticPropertiesScope.kt`** -> AI Confidence: **99.48%**
2060. **`compiler/frontend.java/src/org/jetbrains/kotlin/synthetic/JavaSyntheticScopes.kt`** -> AI Confidence: **99.48%**
2061. **`compiler/frontend.java/src/org/jetbrains/kotlin/synthetic/SamAdapterFunctionsScope.kt`** -> AI Confidence: **99.48%**
2062. **`compiler/frontend.java/src/org/jetbrains/kotlin/synthetic/syntheticExtensionsUtils.kt`** -> AI Confidence: **99.48%**
2063. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/ConstructorConsistencyChecker.kt`** -> AI Confidence: **99.48%**
2064. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/ControlFlowInformationProviderImpl.kt`** -> AI Confidence: **99.48%**
2065. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/ControlFlowProcessor.kt`** -> AI Confidence: **99.48%**
2066. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/PseudocodeTraverser.kt`** -> AI Confidence: **99.48%**
2067. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/ControlFlowInstructionsGenerator.kt`** -> AI Confidence: **99.48%**
2068. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/PseudocodeImpl.kt`** -> AI Confidence: **99.48%**
2069. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/instructions/eval/accessInstructions.kt`** -> AI Confidence: **99.48%**
2070. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/instructions/eval/operationInstructions.kt`** -> AI Confidence: **99.48%**
2071. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/instructions/jumps/ConditionalJumpInstruction.kt`** -> AI Confidence: **99.48%**
2072. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/instructions/jumps/NondeterministicJumpInstruction.kt`** -> AI Confidence: **99.48%**
2073. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/instructions/special/LocalFunctionDeclarationInstruction.kt`** -> AI Confidence: **99.48%**
2074. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/pseudocode/pseudocodeUtils.kt`** -> AI Confidence: **99.48%**
2075. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/variable/PseudocodeVariableDataCollector.kt`** -> AI Confidence: **99.48%**
2076. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/variable/PseudocodeVariablesData.kt`** -> AI Confidence: **99.48%**
2077. **`compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/variable/VariableControlFlowInfo.kt`** -> AI Confidence: **99.48%**
2078. **`compiler/frontend/src/org/jetbrains/kotlin/analyzer/AbstractResolverForProject.kt`** -> AI Confidence: **99.48%**
2079. **`compiler/frontend/src/org/jetbrains/kotlin/analyzer/AnalyzerFacade.kt`** -> AI Confidence: **99.48%**
2080. **`compiler/frontend/src/org/jetbrains/kotlin/analyzer/ResolverForSingleModuleProject.kt`** -> AI Confidence: **99.48%**
2081. **`compiler/frontend/src/org/jetbrains/kotlin/analyzer/common/CommonResolverForModuleFactory.kt`** -> AI Confidence: **99.48%**
2082. **`compiler/frontend/src/org/jetbrains/kotlin/backend/common/SimpleMemberScope.kt`** -> AI Confidence: **99.48%**
2083. **`compiler/frontend/src/org/jetbrains/kotlin/cfg/WhenChecker.kt`** -> AI Confidence: **99.48%**
2084. **`compiler/frontend/src/org/jetbrains/kotlin/cfg/cfgContainingDeclarationUtils.kt`** -> AI Confidence: **99.48%**
2085. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/CheckerDebugInfoReporter.kt`** -> AI Confidence: **99.48%**
2086. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/diagnostics/TextDiagnostic.kt`** -> AI Confidence: **99.48%**
2087. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/diagnostics/factories/DebugInfoDiagnosticFactory0.kt`** -> AI Confidence: **99.48%**
2088. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/diagnostics/factories/DebugInfoDiagnosticFactory1.kt`** -> AI Confidence: **99.48%**
2089. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/utils/CheckerTestUtil.kt`** -> AI Confidence: **99.48%**
2090. **`compiler/frontend/src/org/jetbrains/kotlin/checkers/utils/DebugInfoUtil.kt`** -> AI Confidence: **99.48%**
2091. **`compiler/frontend/src/org/jetbrains/kotlin/context/context.kt`** -> AI Confidence: **99.48%**
2092. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/ContextInfoToDataFlowInfo.kt`** -> AI Confidence: **99.48%**
2093. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/ContractDeserializerImpl.kt`** -> AI Confidence: **99.48%**
2094. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/ESDataFlowValue.kt`** -> AI Confidence: **99.48%**
2095. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/EffectSystem.kt`** -> AI Confidence: **99.48%**
2096. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/EffectsExtractingVisitor.kt`** -> AI Confidence: **99.48%**
2097. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/ContractParsingDiagnosticsCollector.kt`** -> AI Confidence: **99.48%**
2098. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/ContractParsingServices.kt`** -> AI Confidence: **99.48%**
2099. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/PsiConditionParser.kt`** -> AI Confidence: **99.48%**
2100. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/PsiConstantParser.kt`** -> AI Confidence: **99.48%**
2101. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/PsiContractParserDispatcher.kt`** -> AI Confidence: **99.48%**
2102. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/PsiContractsUtils.kt`** -> AI Confidence: **99.48%**
2103. **`compiler/frontend/src/org/jetbrains/kotlin/contracts/parsing/effects/PsiCallsEffectParser.kt`** -> AI Confidence: **99.48%**
2104. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/ClassicPositioningStrategies.kt`** -> AI Confidence: **99.48%**
2105. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/diagnosticUtils.kt`** -> AI Confidence: **99.48%**
2106. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/PlatformIncompatibilityDiagnosticRenderer.kt`** -> AI Confidence: **99.48%**
2107. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/Renderers.kt`** -> AI Confidence: **99.48%**
2108. **`compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/adaptiveClassifierNamePolicy.kt`** -> AI Confidence: **99.48%**
2109. **`compiler/frontend/src/org/jetbrains/kotlin/extensions/internal/TypeResolutionInterceptor.kt`** -> AI Confidence: **99.48%**
2110. **`compiler/frontend/src/org/jetbrains/kotlin/frontend/di/injection.kt`** -> AI Confidence: **99.48%**
2111. **`compiler/frontend/src/org/jetbrains/kotlin/idea/MainFunctionDetector.kt`** -> AI Confidence: **99.48%**
2112. **`compiler/frontend/src/org/jetbrains/kotlin/psi/synthetics/SyntheticClassOrObjectDescriptor.kt`** -> AI Confidence: **99.48%**
2113. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AllUnderImportScope.kt`** -> AI Confidence: **99.48%**
2114. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnalyzingUtils.kt`** -> AI Confidence: **99.48%**
2115. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnnotationChecker.kt`** -> AI Confidence: **99.48%**
2116. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnnotationResolver.kt`** -> AI Confidence: **99.48%**
2117. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/AnnotationUseSiteTargetChecker.kt`** -> AI Confidence: **99.48%**
2118. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/CollectionLiteralResolver.kt`** -> AI Confidence: **99.48%**
2119. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/CompositeBindingContext.kt`** -> AI Confidence: **99.48%**
2120. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ContextReceiversUtil.kt`** -> AI Confidence: **99.48%**
2121. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DataClassDescriptorResolver.kt`** -> AI Confidence: **99.48%**
2122. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DeclarationResolver.kt`** -> AI Confidence: **99.48%**
2123. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DeclarationsChecker.kt`** -> AI Confidence: **99.48%**
2124. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DelegateInferenceSession.kt`** -> AI Confidence: **99.48%**
2125. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DelegatedPropertyResolver.kt`** -> AI Confidence: **99.48%**
2126. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DelegatingBindingTrace.kt`** -> AI Confidence: **99.48%**
2127. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DelegationResolver.kt`** -> AI Confidence: **99.48%**
2128. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/DescriptorToSourceUtils.kt`** -> AI Confidence: **99.48%**
2129. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ExposedVisibilityChecker.kt`** -> AI Confidence: **99.48%**
2130. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/FiniteBoundRestrictionChecker.kt`** -> AI Confidence: **99.48%**
2131. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/FunctionDescriptorResolver.kt`** -> AI Confidence: **99.48%**
2132. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/FunctionsFromAny.kt`** -> AI Confidence: **99.48%**
2133. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/LateinitModifierApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
2134. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/LazyExplicitImportScope.kt`** -> AI Confidence: **99.48%**
2135. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/LazyTopDownAnalyzer.kt`** -> AI Confidence: **99.48%**
2136. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/LocalVariableResolver.kt`** -> AI Confidence: **99.48%**
2137. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ModifiersChecker.kt`** -> AI Confidence: **99.48%**
2138. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/NonExpansiveInheritanceRestrictionChecker.kt`** -> AI Confidence: **99.48%**
2139. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/OperatorModifierChecker.kt`** -> AI Confidence: **99.48%**
2140. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/OverloadChecker.kt`** -> AI Confidence: **99.48%**
2141. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/OverloadResolver.kt`** -> AI Confidence: **99.48%**
2142. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/OverrideResolver.kt`** -> AI Confidence: **99.48%**
2143. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/QualifiedExpressionResolveUtil.kt`** -> AI Confidence: **99.48%**
2144. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/QualifiedExpressionResolver.kt`** -> AI Confidence: **99.48%**
2145. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/RecursiveContractHelper.kt`** -> AI Confidence: **99.48%**
2146. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/ShadowedExtensionChecker.kt`** -> AI Confidence: **99.48%**
2147. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/TypeBinding.kt`** -> AI Confidence: **99.48%**
2148. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/TypeResolver.kt`** -> AI Confidence: **99.48%**
2149. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/UpperBoundChecker.kt`** -> AI Confidence: **99.48%**
2150. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/VariableTypeAndInitializerResolver.kt`** -> AI Confidence: **99.48%**
2151. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/VarianceChecker.kt`** -> AI Confidence: **99.48%**
2152. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/bindingContextUtil/BindingContextUtils.kt`** -> AI Confidence: **99.48%**
2153. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/CallCompleter.kt`** -> AI Confidence: **99.48%**
2154. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/CallExpressionResolver.kt`** -> AI Confidence: **99.48%**
2155. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/CandidateResolver.kt`** -> AI Confidence: **99.48%**
2156. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/DiagnosticReporterByTrackingStrategy.kt`** -> AI Confidence: **99.48%**
2157. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/DiagnosticReporterImpl.kt`** -> AI Confidence: **99.48%**
2158. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/DslMarkerUtils.kt`** -> AI Confidence: **99.48%**
2159. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/GenericCandidateResolver.kt`** -> AI Confidence: **99.48%**
2160. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/AbstractClassInstantiationChecker.kt`** -> AI Confidence: **99.48%**
2161. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/AbstractReflectionApiCallChecker.kt`** -> AI Confidence: **99.48%**
2162. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ApiVersionCallChecker.kt`** -> AI Confidence: **99.48%**
2163. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/AssigningNamedArgumentToVarargChecker.kt`** -> AI Confidence: **99.48%**
2164. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/BuilderInferenceAssignmentChecker.kt`** -> AI Confidence: **99.48%**
2165. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CallChecker.kt`** -> AI Confidence: **99.48%**
2166. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CallableReferenceCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
2167. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CapturingInClosureChecker.kt`** -> AI Confidence: **99.48%**
2168. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CompanionLHSRelatedCheckers.kt`** -> AI Confidence: **99.48%**
2169. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ConstructorHeaderCallChecker.kt`** -> AI Confidence: **99.48%**
2170. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ContractNotAllowedCallChecker.kt`** -> AI Confidence: **99.48%**
2171. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/CustomEnumEntriesMigrationCallChecker.kt`** -> AI Confidence: **99.48%**
2172. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/DeprecatedCallChecker.kt`** -> AI Confidence: **99.48%**
2173. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/DslScopeViolationCallChecker.kt`** -> AI Confidence: **99.48%**
2174. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/EnumEntryVsCompanionPriorityCallChecker.kt`** -> AI Confidence: **99.48%**
2175. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/EqualityCallChecker.kt`** -> AI Confidence: **99.48%**
2176. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ImplicitNothingAsTypeParameterCallChecker.kt`** -> AI Confidence: **99.48%**
2177. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/IncorrectCapturedApproximationCallChecker.kt`** -> AI Confidence: **99.48%**
2178. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/InfixCallChecker.kt`** -> AI Confidence: **99.48%**
2179. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/InlineChecker.kt`** -> AI Confidence: **99.48%**
2180. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/LambdaWithSuspendModifierCallChecker.kt`** -> AI Confidence: **99.48%**
2181. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/LateinitIntrinsicApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
2182. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/NamedFunAsExpressionChecker.kt`** -> AI Confidence: **99.48%**
2183. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/NewSchemeOfIntegerOperatorResolutionChecker.kt`** -> AI Confidence: **99.48%**
2184. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/NullableVarargArgumentCallChecker.kt`** -> AI Confidence: **99.48%**
2185. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/OperatorCallChecker.kt`** -> AI Confidence: **99.48%**
2186. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ProtectedConstructorCallChecker.kt`** -> AI Confidence: **99.48%**
2187. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ReferencingToUnderscoreNamedParameterOfCatchBlockChecker.kt`** -> AI Confidence: **99.48%**
2188. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ResolutionToPrivateConstructorOfSealedClassChecker.kt`** -> AI Confidence: **99.48%**
2189. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/ResultTypeWithNullableOperatorsChecker.kt`** -> AI Confidence: **99.48%**
2190. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/SelfCallInNestedObjectConstructorChecker.kt`** -> AI Confidence: **99.48%**
2191. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/SuspendConversionCallChecker.kt`** -> AI Confidence: **99.48%**
2192. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/SynchronizedByValueChecker.kt`** -> AI Confidence: **99.48%**
2193. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/UnderscoreUsageChecker.kt`** -> AI Confidence: **99.48%**
2194. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/UnsupportedUntilRangeDeclarationChecker.kt`** -> AI Confidence: **99.48%**
2195. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/UselessElvisCallChecker.kt`** -> AI Confidence: **99.48%**
2196. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/VarargWrongExecutionOrderChecker.kt`** -> AI Confidence: **99.48%**
2197. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/checkers/coroutineCallChecker.kt`** -> AI Confidence: **99.48%**
2198. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/context/ResolutionResultsCache.kt`** -> AI Confidence: **99.48%**
2199. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/BuilderInferenceSession.kt`** -> AI Confidence: **99.48%**
2200. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/BuilderInferenceUtil.kt`** -> AI Confidence: **99.48%**
2201. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/ConstraintSystemBuilderImpl.kt`** -> AI Confidence: **99.48%**
2202. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/ConstraintSystemImpl.kt`** -> AI Confidence: **99.48%**
2203. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/TypeBoundsImpl.kt`** -> AI Confidence: **99.48%**
2204. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/constraintIncorporation.kt`** -> AI Confidence: **99.48%**
2205. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/inference/constraintSystemUtils.kt`** -> AI Confidence: **99.48%**
2206. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/results/FlatSignatureForResolvedCall.kt`** -> AI Confidence: **99.48%**
2207. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/DataFlowInfoImpl.kt`** -> AI Confidence: **99.48%**
2208. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/DataFlowUtils.kt`** -> AI Confidence: **99.48%**
2209. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/DataFlowValueFactoryImpl.kt`** -> AI Confidence: **99.48%**
2210. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/DataFlowValueKindUtils.kt`** -> AI Confidence: **99.48%**
2211. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/IdentifierInfo.kt`** -> AI Confidence: **99.48%**
2212. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/smartcasts/SmartCastManager.kt`** -> AI Confidence: **99.48%**
2213. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tasks/TracingStrategyForImplicitConstructorDelegationCall.kt`** -> AI Confidence: **99.48%**
2214. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tasks/dynamicCalls.kt`** -> AI Confidence: **99.48%**
2215. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/KotlinResolutionCallbacksImpl.kt`** -> AI Confidence: **99.48%**
2216. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/KotlinResolutionStatelessCallbacksImpl.kt`** -> AI Confidence: **99.48%**
2217. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/KotlinToResolvedCallTransformer.kt`** -> AI Confidence: **99.48%**
2218. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewAbstractResolvedCall.kt`** -> AI Confidence: **99.48%**
2219. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewCallArguments.kt`** -> AI Confidence: **99.48%**
2220. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewCallableReferenceResolvedCall.kt`** -> AI Confidence: **99.48%**
2221. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewResolutionOldInference.kt`** -> AI Confidence: **99.48%**
2222. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/NewResolvedCallImpl.kt`** -> AI Confidence: **99.48%**
2223. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/PSICallResolver.kt`** -> AI Confidence: **99.48%**
2224. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/PSIKotlinCalls.kt`** -> AI Confidence: **99.48%**
2225. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/ResolvedAtomCompleter.kt`** -> AI Confidence: **99.48%**
2226. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/tower/StubTypesBasedInferenceSession.kt`** -> AI Confidence: **99.48%**
2227. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/util/CallResolverUtil.kt`** -> AI Confidence: **99.48%**
2228. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/util/callUtil.kt`** -> AI Confidence: **99.48%**
2229. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/calls/util/resolvedCallUtil.kt`** -> AI Confidence: **99.48%**
2230. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ActualClassifierMustHasTheSameMembersAsNonFinalExpectClassifierChecker.kt`** -> AI Confidence: **99.48%**
2231. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ActualTypealiasToSpecialAnnotationChecker.kt`** -> AI Confidence: **99.48%**
2232. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/AnnotationClassTargetAndRetentionChecker.kt`** -> AI Confidence: **99.48%**
2233. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ClassifierUsageChecker.kt`** -> AI Confidence: **99.48%**
2234. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ConstModifierChecker.kt`** -> AI Confidence: **99.48%**
2235. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ContextualDeclarationChecker.kt`** -> AI Confidence: **99.48%**
2236. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/CyclicAnnotationsChecker.kt`** -> AI Confidence: **99.48%**
2237. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DataObjectContentChecker.kt`** -> AI Confidence: **99.48%**
2238. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DelegationChecker.kt`** -> AI Confidence: **99.48%**
2239. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DeprecatedClassifierUsageChecker.kt`** -> AI Confidence: **99.48%**
2240. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DeprecatedSinceKotlinAnnotationChecker.kt`** -> AI Confidence: **99.48%**
2241. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DeprecationInheritanceChecker.kt`** -> AI Confidence: **99.48%**
2242. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/DynamicReceiverChecker.kt`** -> AI Confidence: **99.48%**
2243. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/EnumCompanionInEnumConstructorCallChecker.kt`** -> AI Confidence: **99.48%**
2244. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ExpectActualClassifiersAreInBetaChecker.kt`** -> AI Confidence: **99.48%**
2245. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ExpectActualInTheSameModuleChecker.kt`** -> AI Confidence: **99.48%**
2246. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ExpectedActualDeclarationChecker.kt`** -> AI Confidence: **99.48%**
2247. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ExplicitApiDeclarationChecker.kt`** -> AI Confidence: **99.48%**
2248. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/FunInterfaceDeclarationChecker.kt`** -> AI Confidence: **99.48%**
2249. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/InfixModifierChecker.kt`** -> AI Confidence: **99.48%**
2250. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/InlineParameterChecker.kt`** -> AI Confidence: **99.48%**
2251. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/KClassWithIncorrectTypeArgumentChecker.kt`** -> AI Confidence: **99.48%**
2252. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/KotlinVersionStringAnnotationValueChecker.kt`** -> AI Confidence: **99.48%**
2253. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/MissingDependencyClassChecker.kt`** -> AI Confidence: **99.48%**
2254. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/MissingDependencySupertypeChecker.kt`** -> AI Confidence: **99.48%**
2255. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/MultiFieldValueClassAnnotationsChecker.kt`** -> AI Confidence: **99.48%**
2256. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/NullableExtensionOperatorWithSafeCallChecker.kt`** -> AI Confidence: **99.48%**
2257. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/OptInMarkerDeclarationAnnotationChecker.kt`** -> AI Confidence: **99.48%**
2258. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/OptInUsageChecker.kt`** -> AI Confidence: **99.48%**
2259. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/OptionalExpectationChecker.kt`** -> AI Confidence: **99.48%**
2260. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/OptionalExpectationUsageChecker.kt`** -> AI Confidence: **99.48%**
2261. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/PassingProgressionAsCollectionCallChecker.kt`** -> AI Confidence: **99.48%**
2262. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/PrimitiveNumericComparisonCallChecker.kt`** -> AI Confidence: **99.48%**
2263. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/PrivateInlineFunctionsReturningAnonymousObjectsChecker.kt`** -> AI Confidence: **99.48%**
2264. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/PublishedApiUsageChecker.kt`** -> AI Confidence: **99.48%**
2265. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ReifiedTypeParameterAnnotationChecker.kt`** -> AI Confidence: **99.48%**
2266. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ResolutionWithStubTypesChecker.kt`** -> AI Confidence: **99.48%**
2267. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ResultClassInReturnTypeChecker.kt`** -> AI Confidence: **99.48%**
2268. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ReturnValueAnnotationChecker.kt`** -> AI Confidence: **99.48%**
2269. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SealedInheritorInSameModuleChecker.kt`** -> AI Confidence: **99.48%**
2270. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SealedInheritorInSamePackageChecker.kt`** -> AI Confidence: **99.48%**
2271. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/StubForBuilderInferenceParameterTypeChecker.kt`** -> AI Confidence: **99.48%**
2272. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SuspendFunctionAsSupertypeChecker.kt`** -> AI Confidence: **99.48%**
2273. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/SuspendLimitationsChecker.kt`** -> AI Confidence: **99.48%**
2274. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/TailrecFunctionChecker.kt`** -> AI Confidence: **99.48%**
2275. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/TrailingCommaChecker.kt`** -> AI Confidence: **99.48%**
2276. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/UnderscoreChecker.kt`** -> AI Confidence: **99.48%**
2277. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ValueClassDeclarationChecker.kt`** -> AI Confidence: **99.48%**
2278. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ValueParameterUsageInDefaultArgumentChecker.kt`** -> AI Confidence: **99.48%**
2279. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/VolatileAnnotationChecker.kt`** -> AI Confidence: **99.48%**
2280. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/codegen/CodegenUtil.kt`** -> AI Confidence: **99.48%**
2281. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/codegen/FunctionsFromAnyGenerator.kt`** -> AI Confidence: **99.48%**
2282. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/constants/evaluate/ConstantExpressionEvaluator.kt`** -> AI Confidence: **99.48%**
2283. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/deprecation/Deprecation.kt`** -> AI Confidence: **99.48%**
2284. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/deprecation/DeprecationResolver.kt`** -> AI Confidence: **99.48%**
2285. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/deprecation/deprecationUtil.kt`** -> AI Confidence: **99.48%**
2286. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/diagnostics/KotlinSuppressCache.kt`** -> AI Confidence: **99.48%**
2287. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/diagnostics/MutableDiagnosticsWithSuppression.kt`** -> AI Confidence: **99.48%**
2288. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/extensions/SyntheticResolveExtension.kt`** -> AI Confidence: **99.48%**
2289. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/inline/InlineAnalyzerExtension.kt`** -> AI Confidence: **99.48%**
2290. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/FileScopeFactory.kt`** -> AI Confidence: **99.48%**
2291. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/FileScopeProvider.kt`** -> AI Confidence: **99.48%**
2292. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/LazyDeclarationResolver.kt`** -> AI Confidence: **99.48%**
2293. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/LazyImportScope.kt`** -> AI Confidence: **99.48%**
2294. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/declarations/AbstractPsiBasedDeclarationProvider.kt`** -> AI Confidence: **99.48%**
2295. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/declarations/CliDeclarationProviderFactoryService.kt`** -> AI Confidence: **99.48%**
2296. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/declarations/DeclarationProviderFactoryService.kt`** -> AI Confidence: **99.48%**
2297. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/AbstractLazyMemberScope.kt`** -> AI Confidence: **99.48%**
2298. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/ClassResolutionScopesSupport.kt`** -> AI Confidence: **99.48%**
2299. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyAnnotations.kt`** -> AI Confidence: **99.48%**
2300. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyClassMemberScope.kt`** -> AI Confidence: **99.48%**
2301. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyPackageMemberScope.kt`** -> AI Confidence: **99.48%**
2302. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/lazy/descriptors/LazyTypeAliasDescriptor.kt`** -> AI Confidence: **99.48%**
2303. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/repl/ReplState.kt`** -> AI Confidence: **99.48%**
2304. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/scopes/LocalRedeclarationChecker.kt`** -> AI Confidence: **99.48%**
2305. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/scopes/receivers/Qualifier.kt`** -> AI Confidence: **99.48%**
2306. **`compiler/frontend/src/org/jetbrains/kotlin/resolve/sinceKotlinUtil.kt`** -> AI Confidence: **99.48%**
2307. **`compiler/frontend/src/org/jetbrains/kotlin/storage/LockBasedLazyResolveStorageManager.kt`** -> AI Confidence: **99.48%**
2308. **`compiler/frontend/src/org/jetbrains/kotlin/types/CastDiagnosticsUtil.kt`** -> AI Confidence: **99.48%**
2309. **`compiler/frontend/src/org/jetbrains/kotlin/types/RangeUtil.kt`** -> AI Confidence: **99.48%**
2310. **`compiler/frontend/src/org/jetbrains/kotlin/types/enumCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
2311. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/DestructuringDeclarationResolver.kt`** -> AI Confidence: **99.48%**
2312. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/DoubleColonExpressionResolver.kt`** -> AI Confidence: **99.48%**
2313. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/FakeCallResolver.kt`** -> AI Confidence: **99.48%**
2314. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/FunctionsTypingVisitor.kt`** -> AI Confidence: **99.48%**
2315. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/LabelResolver.kt`** -> AI Confidence: **99.48%**
2316. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/LocalClassifierAnalyzer.kt`** -> AI Confidence: **99.48%**
2317. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/PatternMatchingTypingVisitor.kt`** -> AI Confidence: **99.48%**
2318. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/PreliminaryDeclarationVisitor.kt`** -> AI Confidence: **99.48%**
2319. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/PreliminaryLoopVisitor.kt`** -> AI Confidence: **99.48%**
2320. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/SenselessComparisonChecker.kt`** -> AI Confidence: **99.48%**
2321. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/ValueParameterResolver.kt`** -> AI Confidence: **99.48%**
2322. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/definitelyNotNullDeprecation.kt`** -> AI Confidence: **99.48%**
2323. **`compiler/frontend/src/org/jetbrains/kotlin/types/expressions/unqualifiedSuper/unqualifiedSuper.kt`** -> AI Confidence: **99.48%**
2324. **`compiler/frontend/src/org/jetbrains/kotlin/util/IncrementalTrackerUtil.kt`** -> AI Confidence: **99.48%**
2325. **`compiler/frontend/src/org/jetbrains/kotlin/util/declarationUtil.kt`** -> AI Confidence: **99.48%**
2326. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/AbiSnapshot.kt`** -> AI Confidence: **99.48%**
2327. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/BuildDiffsStorage.kt`** -> AI Confidence: **99.48%**
2328. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/BuildHistoryJvmICRunner.kt`** -> AI Confidence: **99.48%**
2329. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/CompilerPluginFilesCache.kt`** -> AI Confidence: **99.48%**
2330. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/CompilerRunnerUtils.kt`** -> AI Confidence: **99.48%**
2331. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalCompilerRunner.kt`** -> AI Confidence: **99.48%**
2332. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalFirJvmCompilerRunner.kt`** -> AI Confidence: **99.48%**
2333. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalJsCompilerRunner.kt`** -> AI Confidence: **99.48%**
2334. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalJvmCompilerRunner.kt`** -> AI Confidence: **99.48%**
2335. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/IncrementalJvmCompilerRunnerBase.kt`** -> AI Confidence: **99.48%**
2336. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/InputsCache.kt`** -> AI Confidence: **99.48%**
2337. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathChangesComputer.kt`** -> AI Confidence: **99.48%**
2338. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathEntrySnapshotter.kt`** -> AI Confidence: **99.48%**
2339. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathSnapshotSerializer.kt`** -> AI Confidence: **99.48%**
2340. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathSnapshotShrinker.kt`** -> AI Confidence: **99.48%**
2341. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/InMemoryCacheWithEviction.kt`** -> AI Confidence: **99.48%**
2342. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/impl/BasicClassInfo.kt`** -> AI Confidence: **99.48%**
2343. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/impl/ClassListSnapshotter.kt`** -> AI Confidence: **99.48%**
2344. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/impl/InlinedClassSnapshotter.kt`** -> AI Confidence: **99.48%**
2345. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/classpathDiff/impl/SingleClassSnapshotter.kt`** -> AI Confidence: **99.48%**
2346. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/dirtyFiles/ClasspathSnapshotBasedImpactDeterminer.kt`** -> AI Confidence: **99.48%**
2347. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/dirtyFiles/DirtyFilesProvider.kt`** -> AI Confidence: **99.48%**
2348. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/dirtyFiles/HistoryFilesBasedImpactDeterminer.kt`** -> AI Confidence: **99.48%**
2349. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/dirtyFiles/JvmSourcesToCompileCalculator.kt`** -> AI Confidence: **99.48%**
2350. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/dirtyFiles/changesDetectionUtils.kt`** -> AI Confidence: **99.48%**
2351. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/incrementalFirCacheUtils.kt`** -> AI Confidence: **99.48%**
2352. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/javaInterop/ChangedJavaFilesProcessor.kt`** -> AI Confidence: **99.48%**
2353. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/javaInterop/JavaInteropCoordinator.kt`** -> AI Confidence: **99.48%**
2354. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/multiproject/ModulesApiHistory.kt`** -> AI Confidence: **99.48%**
2355. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/parsing/parseFileUtils.kt`** -> AI Confidence: **99.48%**
2356. **`compiler/incremental-compilation-impl/src/org/jetbrains/kotlin/incremental/snapshots/LazyClasspathSnapshot.kt`** -> AI Confidence: **99.48%**
2357. **`compiler/incremental-compilation-impl/testFixtures/org/jetbrains/kotlin/incremental/AbstractIncrementalCompilerRunnerTestBase.kt`** -> AI Confidence: **99.48%**
2358. **`compiler/incremental-compilation-impl/testFixtures/org/jetbrains/kotlin/incremental/utils/classpathSnapshotUtils.kt`** -> AI Confidence: **99.48%**
2359. **`compiler/incremental-compilation-impl/tests/org/jetbrains/kotlin/incremental/classpathDiff/ClasspathSnapshotTestCommon.kt`** -> AI Confidence: **99.48%**
2360. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/CommonBackendContext.kt`** -> AI Confidence: **99.48%**
2361. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/CommonBackendErrors.kt`** -> AI Confidence: **99.48%**
2362. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/CompilationException.kt`** -> AI Confidence: **99.48%**
2363. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ErrorReportingContext.kt`** -> AI Confidence: **99.48%**
2364. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/IrElementTransformerVoidWithContext.kt`** -> AI Confidence: **99.48%**
2365. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/Lower.kt`** -> AI Confidence: **99.48%**
2366. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/RunPreSerializationLoweringPhases.kt`** -> AI Confidence: **99.48%**
2367. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/TailRecursionCallsCollector.kt`** -> AI Confidence: **99.48%**
2368. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/TailSuspendCallsCollector.kt`** -> AI Confidence: **99.48%**
2369. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/extensions/IrPluginContext.kt`** -> AI Confidence: **99.48%**
2370. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/extensions/IrPluginContextImpl.kt`** -> AI Confidence: **99.48%**
2371. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/BackendSymbols.kt`** -> AI Confidence: **99.48%**
2372. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/ExpectSymbolTransformer.kt`** -> AI Confidence: **99.48%**
2373. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/IrInlineUtils.kt`** -> AI Confidence: **99.48%**
2374. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/IrUtils.kt`** -> AI Confidence: **99.48%**
2375. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/KlibSharedVariablesManager.kt`** -> AI Confidence: **99.48%**
2376. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/PreSerializationSymbols.kt`** -> AI Confidence: **99.48%**
2377. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/ir/ValueRemapper.kt`** -> AI Confidence: **99.48%**
2378. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AbstractFunctionReferenceLowering.kt`** -> AI Confidence: **99.48%**
2379. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AbstractPropertyReferenceLowering.kt`** -> AI Confidence: **99.48%**
2380. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AbstractSuspendFunctionsLowering.kt`** -> AI Confidence: **99.48%**
2381. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AbstractValueUsageTransformer.kt`** -> AI Confidence: **99.48%**
2382. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/AnnotationImplementationTransformer.kt`** -> AI Confidence: **99.48%**
2383. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ArrayConstructorLowering.kt`** -> AI Confidence: **99.48%**
2384. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ClosureAnnotator.kt`** -> AI Confidence: **99.48%**
2385. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ConstEvaluationLowering.kt`** -> AI Confidence: **99.48%**
2386. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/DefaultArgumentFunctionFactory.kt`** -> AI Confidence: **99.48%**
2387. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/DefaultArgumentStubGenerator.kt`** -> AI Confidence: **99.48%**
2388. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/DelegatedPropertyOptimizationLowering.kt`** -> AI Confidence: **99.48%**
2389. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/EnumWhenLowering.kt`** -> AI Confidence: **99.48%**
2390. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ExpectDeclarationRemover.kt`** -> AI Confidence: **99.48%**
2391. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ExpressionBodyTransformer.kt`** -> AI Confidence: **99.48%**
2392. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/FinallyBlocksLowering.kt`** -> AI Confidence: **99.48%**
2393. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/FlattenStringConcatenationLowering.kt`** -> AI Confidence: **99.48%**
2394. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/IfNullExpressionsFusionLowering.kt`** -> AI Confidence: **99.48%**
2395. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InitializersLowering.kt`** -> AI Confidence: **99.48%**
2396. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InlineClassDeclarationLowering.kt`** -> AI Confidence: **99.48%**
2397. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InnerClassesLowering.kt`** -> AI Confidence: **99.48%**
2398. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InventNamesForLocalClasses.kt`** -> AI Confidence: **99.48%**
2399. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/InventNamesForLocalFunctions.kt`** -> AI Confidence: **99.48%**
2400. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/KlibAssertionLowering.kt`** -> AI Confidence: **99.48%**
2401. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/KotlinNothingValueExceptionLowering.kt`** -> AI Confidence: **99.48%**
2402. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/LateinitLowering.kt`** -> AI Confidence: **99.48%**
2403. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/LocalDeclarationPopupLowering.kt`** -> AI Confidence: **99.48%**
2404. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/LocalDeclarationsLowering.kt`** -> AI Confidence: **99.48%**
2405. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/LowerUtils.kt`** -> AI Confidence: **99.48%**
2406. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/MethodsFromAnyGeneratorForLowerings.kt`** -> AI Confidence: **99.48%**
2407. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/PropertiesLowering.kt`** -> AI Confidence: **99.48%**
2408. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/RangeContainsLowering.kt`** -> AI Confidence: **99.48%**
2409. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/RedundantCastsRemoverLowering.kt`** -> AI Confidence: **99.48%**
2410. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/ReturnableBlockTransformer.kt`** -> AI Confidence: **99.48%**
2411. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/SharedVariablesLowering.kt`** -> AI Confidence: **99.48%**
2412. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/SharedVariablesPrimitiveBoxSpecializationLowering.kt`** -> AI Confidence: **99.48%**
2413. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/SingleAbstractMethodLowering.kt`** -> AI Confidence: **99.48%**
2414. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/SpecialBridgeMethods.kt`** -> AI Confidence: **99.48%**
2415. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/StringConcatenationLowering.kt`** -> AI Confidence: **99.48%**
2416. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/TailrecLowering.kt`** -> AI Confidence: **99.48%**
2417. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/UpgradeCallableReferences.kt`** -> AI Confidence: **99.48%**
2418. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/VersionOverloadsLowering.kt`** -> AI Confidence: **99.48%**
2419. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/coroutines/AddContinuationToFunctionCallsLowering.kt`** -> AI Confidence: **99.48%**
2420. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/coroutines/AddContinuationToFunctionsLowering.kt`** -> AI Confidence: **99.48%**
2421. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/AvoidLocalFOsInInlineFunctionsLowering.kt`** -> AI Confidence: **99.48%**
2422. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/InlineCallCycleCheckerLowering.kt`** -> AI Confidence: **99.48%**
2423. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/KlibSyntheticAccessorGenerator.kt`** -> AI Confidence: **99.48%**
2424. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/LocalClasses.kt`** -> AI Confidence: **99.48%**
2425. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/inline/SyntheticAccessorGenerator.kt`** -> AI Confidence: **99.48%**
2426. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/ForLoopsLowering.kt`** -> AI Confidence: **99.48%**
2427. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/HeaderInfo.kt`** -> AI Confidence: **99.48%**
2428. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/HeaderProcessor.kt`** -> AI Confidence: **99.48%**
2429. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/IndexedGetLoopHeader.kt`** -> AI Confidence: **99.48%**
2430. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/IterableLoopHeader.kt`** -> AI Confidence: **99.48%**
2431. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/JavaLikeCounterLoopBuilder.kt`** -> AI Confidence: **99.48%**
2432. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/NumericForLoopHeader.kt`** -> AI Confidence: **99.48%**
2433. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/ProgressionLoopHeader.kt`** -> AI Confidence: **99.48%**
2434. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/ProgressionType.kt`** -> AI Confidence: **99.48%**
2435. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/Utils.kt`** -> AI Confidence: **99.48%**
2436. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/WithIndexLoopHeader.kt`** -> AI Confidence: **99.48%**
2437. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/DefaultProgressionHandler.kt`** -> AI Confidence: **99.48%**
2438. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/DefaultSequenceHandler.kt`** -> AI Confidence: **99.48%**
2439. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/DownToHandler.kt`** -> AI Confidence: **99.48%**
2440. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/IndexedGetIterationHandlers.kt`** -> AI Confidence: **99.48%**
2441. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/IndicesHandlers.kt`** -> AI Confidence: **99.48%**
2442. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/RangeToHandler.kt`** -> AI Confidence: **99.48%**
2443. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/RangeUntilHandler.kt`** -> AI Confidence: **99.48%**
2444. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/ReversedHandler.kt`** -> AI Confidence: **99.48%**
2445. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/StepHandler.kt`** -> AI Confidence: **99.48%**
2446. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/UntilHandler.kt`** -> AI Confidence: **99.48%**
2447. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/handlers/WithIndexHandler.kt`** -> AI Confidence: **99.48%**
2448. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/optimizations/LivenessAnalysis.kt`** -> AI Confidence: **99.48%**
2449. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/optimizations/PropertyAccessorInlineLowering.kt`** -> AI Confidence: **99.48%**
2450. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/phaser/DumperVerifier.kt`** -> AI Confidence: **99.48%**
2451. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/phaser/PerformByIrFilePhase.kt`** -> AI Confidence: **99.48%**
2452. **`compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/phaser/PhaseFactories.kt`** -> AI Confidence: **99.48%**
2453. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/BackendJsSymbols.kt`** -> AI Confidence: **99.48%**
2454. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/JsCommonBackendContext.kt`** -> AI Confidence: **99.48%**
2455. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/JsIrBackendContext.kt`** -> AI Confidence: **99.48%**
2456. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/JsLoweringPhases.kt`** -> AI Confidence: **99.48%**
2457. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/compilerWithIC.kt`** -> AI Confidence: **99.48%**
2458. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/Dce.kt`** -> AI Confidence: **99.48%**
2459. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/JsUsefulDeclarationProcessor.kt`** -> AI Confidence: **99.48%**
2460. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/UsefulDeclarationProcessor.kt`** -> AI Confidence: **99.48%**
2461. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/UselessDeclarationsRemover.kt`** -> AI Confidence: **99.48%**
2462. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/dce/utils.kt`** -> AI Confidence: **99.48%**
2463. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/CacheUpdater.kt`** -> AI Confidence: **99.48%**
2464. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/HashCalculatorForIC.kt`** -> AI Confidence: **99.48%**
2465. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/ICUtils.kt`** -> AI Confidence: **99.48%**
2466. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/IdSignatureHashCalculator.kt`** -> AI Confidence: **99.48%**
2467. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/IncrementalCache.kt`** -> AI Confidence: **99.48%**
2468. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/JsIrLinkerLoader.kt`** -> AI Confidence: **99.48%**
2469. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/JsPerFileCache.kt`** -> AI Confidence: **99.48%**
2470. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/KotlinLibraryHeader.kt`** -> AI Confidence: **99.48%**
2471. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ir/IrBuilder.kt`** -> AI Confidence: **99.48%**
2472. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ir/exportUtils.kt`** -> AI Confidence: **99.48%**
2473. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/jsCompiler.kt`** -> AI Confidence: **99.48%**
2474. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/jsexport/ExportModelGenerator.kt`** -> AI Confidence: **99.48%**
2475. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/jsexport/ExportModelToJsStatements.kt`** -> AI Confidence: **99.48%**
2476. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/AnnotationConstructorLowering.kt`** -> AI Confidence: **99.48%**
2477. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/AutoboxingTransformer.kt`** -> AI Confidence: **99.48%**
2478. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/BlockDecomposerLowering.kt`** -> AI Confidence: **99.48%**
2479. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/BooleanPropertyInExternalLowering.kt`** -> AI Confidence: **99.48%**
2480. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/BridgesConstruction.kt`** -> AI Confidence: **99.48%**
2481. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/CaptureStackTraceInThrowables.kt`** -> AI Confidence: **99.48%**
2482. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ClassReferenceLowering.kt`** -> AI Confidence: **99.48%**
2483. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/CollectClassDefaultConstructorsLowering.kt`** -> AI Confidence: **99.48%**
2484. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ConstLowering.kt`** -> AI Confidence: **99.48%**
2485. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/CopyAccessorBodyLowerings.kt`** -> AI Confidence: **99.48%**
2486. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/CreateScriptFunctionsPhase.kt`** -> AI Confidence: **99.48%**
2487. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6AddBoxParameterLowering.kt`** -> AI Confidence: **99.48%**
2488. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6ConstructorBoxParameterOptimizationLowering.kt`** -> AI Confidence: **99.48%**
2489. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6ConstructorCallLowering.kt`** -> AI Confidence: **99.48%**
2490. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6ConstructorLowering.kt`** -> AI Confidence: **99.48%**
2491. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ES6PrimaryConstructorOptimizationLowering.kt`** -> AI Confidence: **99.48%**
2492. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/EnumClassLowering.kt`** -> AI Confidence: **99.48%**
2493. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/EscapedIdentifiersLowering.kt`** -> AI Confidence: **99.48%**
2494. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ExcludeSyntheticDeclarationsFromExportLowering.kt`** -> AI Confidence: **99.48%**
2495. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ExternalEnumUsagesLowering.kt`** -> AI Confidence: **99.48%**
2496. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ExternalPropertyOverridingLowering.kt`** -> AI Confidence: **99.48%**
2497. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ImplicitlyExportedDeclarationsMarkingLowering.kt`** -> AI Confidence: **99.48%**
2498. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/InlineObjectsWithPureInitializationLowering.kt`** -> AI Confidence: **99.48%**
2499. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/InteropCallableReferenceLowering.kt`** -> AI Confidence: **99.48%**
2500. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/InvokeStaticInitializersLowering.kt`** -> AI Confidence: **99.48%**
2501. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsAnnotationImplementationLowering.kt`** -> AI Confidence: **99.48%**
2502. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsBridgesConstruction.kt`** -> AI Confidence: **99.48%**
2503. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsCallableReferenceLowering.kt`** -> AI Confidence: **99.48%**
2504. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsClassUsageInReflectionLowering.kt`** -> AI Confidence: **99.48%**
2505. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsCodeOutliningLowering.kt`** -> AI Confidence: **99.48%**
2506. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsDefaultArgumentFunctionFactory.kt`** -> AI Confidence: **99.48%**
2507. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsDefaultArgumentStubGenerator.kt`** -> AI Confidence: **99.48%**
2508. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsDefaultParameterInjector.kt`** -> AI Confidence: **99.48%**
2509. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsInlineClassDeclarationLowering.kt`** -> AI Confidence: **99.48%**
2510. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsInnerClassesSupport.kt`** -> AI Confidence: **99.48%**
2511. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsInventNamesForLocalClasses.kt`** -> AI Confidence: **99.48%**
2512. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsReturnableBlockLowering.kt`** -> AI Confidence: **99.48%**
2513. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsSingleAbstractMethodLowering.kt`** -> AI Confidence: **99.48%**
2514. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsStaticLowering.kt`** -> AI Confidence: **99.48%**
2515. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/JsStringConcatenationLowering.kt`** -> AI Confidence: **99.48%**
2516. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/MainFunctionCallWrapperLowering.kt`** -> AI Confidence: **99.48%**
2517. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/MoveBodilessDeclarationsToSeparatePlace.kt`** -> AI Confidence: **99.48%**
2518. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/MultipleCatchesLowering.kt`** -> AI Confidence: **99.48%**
2519. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ObjectLowering.kt`** -> AI Confidence: **99.48%**
2520. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrepareCollectionsToExportLowering.kt`** -> AI Confidence: **99.48%**
2521. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrepareExportedDefaultImplementationsLowering.kt`** -> AI Confidence: **99.48%**
2522. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrepareValueClassesToBeExportedLowering.kt`** -> AI Confidence: **99.48%**
2523. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrimaryConstructorLowering.kt`** -> AI Confidence: **99.48%**
2524. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrimitiveCompanionLowering.kt`** -> AI Confidence: **99.48%**
2525. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PrivateMembersLowering.kt`** -> AI Confidence: **99.48%**
2526. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PropertyLazyInitLowering.kt`** -> AI Confidence: **99.48%**
2527. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PropertyReferenceLowering.kt`** -> AI Confidence: **99.48%**
2528. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/PurifyObjectInstanceGettersLowering.kt`** -> AI Confidence: **99.48%**
2529. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/SecondaryCtorLowering.kt`** -> AI Confidence: **99.48%**
2530. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/StaticMembersLowering.kt`** -> AI Confidence: **99.48%**
2531. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/TestGenerator.kt`** -> AI Confidence: **99.48%**
2532. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/ThrowableLowering.kt`** -> AI Confidence: **99.48%**
2533. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/TypeOperatorLowering.kt`** -> AI Confidence: **99.48%**
2534. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/VarargLowering.kt`** -> AI Confidence: **99.48%**
2535. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/WebCallableReferenceLowering.kt`** -> AI Confidence: **99.48%**
2536. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/BoxedLongCallsTransformer.kt`** -> AI Confidence: **99.48%**
2537. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/CallsLowering.kt`** -> AI Confidence: **99.48%**
2538. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/CallsLoweringUtils.kt`** -> AI Confidence: **99.48%**
2539. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/EnumIntrinsicsTransformer.kt`** -> AI Confidence: **99.48%**
2540. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/EqualityAndComparisonCallsTransformer.kt`** -> AI Confidence: **99.48%**
2541. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/MethodsOfAnyCallsTransformer.kt`** -> AI Confidence: **99.48%**
2542. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/NativeGetterSetterTransformer.kt`** -> AI Confidence: **99.48%**
2543. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/NumberOperatorCallsTransformer.kt`** -> AI Confidence: **99.48%**
2544. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/PrimitiveContainerMemberCallTransformer.kt`** -> AI Confidence: **99.48%**
2545. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/calls/ReflectionCallsTransformer.kt`** -> AI Confidence: **99.48%**
2546. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/cleanup/CleanupLowering.kt`** -> AI Confidence: **99.48%**
2547. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/AddContinuationToFunctionCallsLowering.kt`** -> AI Confidence: **99.48%**
2548. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/JsSuspendArityStoreLowering.kt`** -> AI Confidence: **99.48%**
2549. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/JsSuspendFunctionWithGeneratorsLowering.kt`** -> AI Confidence: **99.48%**
2550. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/JsSuspendFunctionsLowering.kt`** -> AI Confidence: **99.48%**
2551. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/PrepareSuspendFunctionsForExportLowering.kt`** -> AI Confidence: **99.48%**
2552. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/ReplaceSuspendIntrinsicLowering.kt`** -> AI Confidence: **99.48%**
2553. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/StateMachineBuilder.kt`** -> AI Confidence: **99.48%**
2554. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/coroutines/SuspendLoweringUtils.kt`** -> AI Confidence: **99.48%**
2555. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/inline/RemoveInlineDeclarationsWithReifiedTypeParametersLowering.kt`** -> AI Confidence: **99.48%**
2556. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/lower/transformers/ConvertMemberToStatic.kt`** -> AI Confidence: **99.48%**
2557. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/CompilationOutputs.kt`** -> AI Confidence: **99.48%**
2558. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/IrElementToJsExpressionTransformer.kt`** -> AI Confidence: **99.48%**
2559. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/IrElementToJsStatementTransformer.kt`** -> AI Confidence: **99.48%**
2560. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/IrFunctionToJsTransformer.kt`** -> AI Confidence: **99.48%**
2561. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/IrModuleToJsTransformer.kt`** -> AI Confidence: **99.48%**
2562. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsCallTransformer.kt`** -> AI Confidence: **99.48%**
2563. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsClassGenerator.kt`** -> AI Confidence: **99.48%**
2564. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsIntrinsicTransformers.kt`** -> AI Confidence: **99.48%**
2565. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsIrProgramFragment.kt`** -> AI Confidence: **99.48%**
2566. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsNameLinkingNamer.kt`** -> AI Confidence: **99.48%**
2567. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/JsPolyfills.kt`** -> AI Confidence: **99.48%**
2568. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/Merger.kt`** -> AI Confidence: **99.48%**
2569. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/jsAstUtils.kt`** -> AI Confidence: **99.48%**
2570. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/transformers/irToJs/jsCode.kt`** -> AI Confidence: **99.48%**
2571. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/tsexport/ExportModelGenerator.kt`** -> AI Confidence: **99.48%**
2572. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/tsexport/TransitiveExportCollector.kt`** -> AI Confidence: **99.48%**
2573. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/AnnotationUtils.kt`** -> AI Confidence: **99.48%**
2574. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/IrJsUtils.kt`** -> AI Confidence: **99.48%**
2575. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/IrTypeUtils.kt`** -> AI Confidence: **99.48%**
2576. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/JsGenerationContext.kt`** -> AI Confidence: **99.48%**
2577. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/JsInlineClassesUtils.kt`** -> AI Confidence: **99.48%**
2578. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/NameTables.kt`** -> AI Confidence: **99.48%**
2579. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/misc.kt`** -> AI Confidence: **99.48%**
2580. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/serialization/JsIrAstDeserializer.kt`** -> AI Confidence: **99.48%**
2581. **`compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/serialization/JsIrAstSerializer.kt`** -> AI Confidence: **99.48%**
2582. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/AnnotationCodegen.kt`** -> AI Confidence: **99.48%**
2583. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/ClassCodegen.kt`** -> AI Confidence: **99.48%**
2584. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/CoroutineCodegen.kt`** -> AI Confidence: **99.48%**
2585. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/EnumEntriesIntrinsicMappingsCacheImpl.kt`** -> AI Confidence: **99.48%**
2586. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/ExpressionCodegen.kt`** -> AI Confidence: **99.48%**
2587. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/FunctionCodegen.kt`** -> AI Confidence: **99.48%**
2588. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrInlineCallGenerator.kt`** -> AI Confidence: **99.48%**
2589. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrInlineCodegen.kt`** -> AI Confidence: **99.48%**
2590. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrInlineDefaultCodegen.kt`** -> AI Confidence: **99.48%**
2591. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrInlineIntrinsicsSupport.kt`** -> AI Confidence: **99.48%**
2592. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrSourceCompilerForInline.kt`** -> AI Confidence: **99.48%**
2593. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/IrTypeAnnotationCollector.kt`** -> AI Confidence: **99.48%**
2594. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/JvmMethodSignatureClashDetector.kt`** -> AI Confidence: **99.48%**
2595. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/PrivateTypeFromNonPrivateInlineUsageChecker.kt`** -> AI Confidence: **99.48%**
2596. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/PromisedValue.kt`** -> AI Confidence: **99.48%**
2597. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/SwitchGenerator.kt`** -> AI Confidence: **99.48%**
2598. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/irCodegenUtils.kt`** -> AI Confidence: **99.48%**
2599. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/BinaryOp.kt`** -> AI Confidence: **99.48%**
2600. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/Clone.kt`** -> AI Confidence: **99.48%**
2601. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/CompareTo.kt`** -> AI Confidence: **99.48%**
2602. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/EnumIntrinsics.kt`** -> AI Confidence: **99.48%**
2603. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/Equals.kt`** -> AI Confidence: **99.48%**
2604. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/GetClassByDescriptor.kt`** -> AI Confidence: **99.48%**
2605. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/GetJavaObjectType.kt`** -> AI Confidence: **99.48%**
2606. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/GetJavaPrimitiveType.kt`** -> AI Confidence: **99.48%**
2607. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/HandleResultOfReflectiveAccess.kt`** -> AI Confidence: **99.48%**
2608. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/HashCode.kt`** -> AI Confidence: **99.48%**
2609. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IntIncr.kt`** -> AI Confidence: **99.48%**
2610. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IntrinsicFunction.kt`** -> AI Confidence: **99.48%**
2611. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IntrinsicMethod.kt`** -> AI Confidence: **99.48%**
2612. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IrCheckNotNull.kt`** -> AI Confidence: **99.48%**
2613. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IrIllegalArgumentException.kt`** -> AI Confidence: **99.48%**
2614. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IrIntrinsicMethods.kt`** -> AI Confidence: **99.48%**
2615. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/IteratorNext.kt`** -> AI Confidence: **99.48%**
2616. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/JavaClassProperty.kt`** -> AI Confidence: **99.48%**
2617. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/JvmDebuggerInvokeSpecial.kt`** -> AI Confidence: **99.48%**
2618. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/JvmInvokeDynamic.kt`** -> AI Confidence: **99.48%**
2619. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/NewArray.kt`** -> AI Confidence: **99.48%**
2620. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/SignatureString.kt`** -> AI Confidence: **99.48%**
2621. **`compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/intrinsics/UnsafeCoerce.kt`** -> AI Confidence: **99.48%**
2622. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/FacadeClassSourceShimForFragmentCompilation.kt`** -> AI Confidence: **99.48%**
2623. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/JvmGeneratorExtensionsImpl.kt`** -> AI Confidence: **99.48%**
2624. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/JvmIrCodegenFactory.kt`** -> AI Confidence: **99.48%**
2625. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/OrphanedExpectUtils.kt`** -> AI Confidence: **99.48%**
2626. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/SymbolTableWithBuiltInsDeduplication.kt`** -> AI Confidence: **99.48%**
2627. **`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/UndiscoveredExpectUtils.kt`** -> AI Confidence: **99.48%**
2628. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/AddContinuationLowering.kt`** -> AI Confidence: **99.48%**
2629. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/AdditionalClassAnnotationLowering.kt`** -> AI Confidence: **99.48%**
2630. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/AnonymousObjectSuperConstructorLowering.kt`** -> AI Confidence: **99.48%**
2631. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/AssertionLowering.kt`** -> AI Confidence: **99.48%**
2632. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/BridgeLowering.kt`** -> AI Confidence: **99.48%**
2633. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/CollectionStubMethodLowering.kt`** -> AI Confidence: **99.48%**
2634. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/DirectInvokeLowering.kt`** -> AI Confidence: **99.48%**
2635. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/EnumClassLowering.kt`** -> AI Confidence: **99.48%**
2636. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/EnumExternalEntriesLowering.kt`** -> AI Confidence: **99.48%**
2637. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ExternalPackageParentPatcherLowering.kt`** -> AI Confidence: **99.48%**
2638. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FakeLocalVariablesForBytecodeInlinerLowering.kt`** -> AI Confidence: **99.48%**
2639. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FileClassLowering.kt`** -> AI Confidence: **99.48%**
2640. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FragmentSharedVariablesLowering.kt`** -> AI Confidence: **99.48%**
2641. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FunctionNVarargBridgeLowering.kt`** -> AI Confidence: **99.48%**
2642. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/FunctionReferenceLowering.kt`** -> AI Confidence: **99.48%**
2643. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/GenerateJvmDefaultCompatibilityBridges.kt`** -> AI Confidence: **99.48%**
2644. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/GenerateMultifileFacades.kt`** -> AI Confidence: **99.48%**
2645. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/IndyLambdaMetafactoryLowering.kt`** -> AI Confidence: **99.48%**
2646. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InheritedDefaultMethodsOnClassesLowering.kt`** -> AI Confidence: **99.48%**
2647. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InterfaceDefaultCallsLowering.kt`** -> AI Confidence: **99.48%**
2648. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InterfaceLowering.kt`** -> AI Confidence: **99.48%**
2649. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InterfaceObjectCallsLowering.kt`** -> AI Confidence: **99.48%**
2650. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/InterfaceSuperCallsLowering.kt`** -> AI Confidence: **99.48%**
2651. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmAnnotationImplementationTransformer.kt`** -> AI Confidence: **99.48%**
2652. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmArgumentNullabilityAssertionsLowering.kt`** -> AI Confidence: **99.48%**
2653. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmBuiltInsLowering.kt`** -> AI Confidence: **99.48%**
2654. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmDefaultArgumentStubGenerator.kt`** -> AI Confidence: **99.48%**
2655. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmDefaultConstructorLowering.kt`** -> AI Confidence: **99.48%**
2656. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmDefaultParameterInjector.kt`** -> AI Confidence: **99.48%**
2657. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmInlineClassLowering.kt`** -> AI Confidence: **99.48%**
2658. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmInlineMultiFieldValueClassLowering.kt`** -> AI Confidence: **99.48%**
2659. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmInventNamesForLocalClasses.kt`** -> AI Confidence: **99.48%**
2660. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmIrLowerUtils.kt`** -> AI Confidence: **99.48%**
2661. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmLateinitLowering.kt`** -> AI Confidence: **99.48%**
2662. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmLocalDeclarationsLowering.kt`** -> AI Confidence: **99.48%**
2663. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmOptimizationLowering.kt`** -> AI Confidence: **99.48%**
2664. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmOverloadsAnnotationLowering.kt`** -> AI Confidence: **99.48%**
2665. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmPropertiesLowering.kt`** -> AI Confidence: **99.48%**
2666. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmSafeCallChainFoldingLowering.kt`** -> AI Confidence: **99.48%**
2667. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmSingleAbstractMethodLowering.kt`** -> AI Confidence: **99.48%**
2668. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmStaticAnnotationLowering.kt`** -> AI Confidence: **99.48%**
2669. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmStringConcatenationLowering.kt`** -> AI Confidence: **99.48%**
2670. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/JvmValueClassAbstractLowering.kt`** -> AI Confidence: **99.48%**
2671. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/MainMethodGenerationLowering.kt`** -> AI Confidence: **99.48%**
2672. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/MakePropertyDelegateMethodsStaticLowering.kt`** -> AI Confidence: **99.48%**
2673. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/MappedEnumWhenLowering.kt`** -> AI Confidence: **99.48%**
2674. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/MoveCompanionObjectFieldsLowering.kt`** -> AI Confidence: **99.48%**
2675. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ObjectClassLowering.kt`** -> AI Confidence: **99.48%**
2676. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PatchLambdaOffsetsLowering.kt`** -> AI Confidence: **99.48%**
2677. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PolymorphicSignatureLowering.kt`** -> AI Confidence: **99.48%**
2678. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PrepareCallableReferencesForInlining.kt`** -> AI Confidence: **99.48%**
2679. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ProcessOptionalAnnotations.kt`** -> AI Confidence: **99.48%**
2680. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PropertyReferenceDelegationLowering.kt`** -> AI Confidence: **99.48%**
2681. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/PropertyReferenceLowering.kt`** -> AI Confidence: **99.48%**
2682. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/RecordEnclosingMethodsLowering.kt`** -> AI Confidence: **99.48%**
2683. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/RepeatedAnnotationLowering.kt`** -> AI Confidence: **99.48%**
2684. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ReplaceKFunctionInvokeWithFunctionInvoke.kt`** -> AI Confidence: **99.48%**
2685. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ReplaceNumberToCharCallSitesLowering.kt`** -> AI Confidence: **99.48%**
2686. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ResolveInlineCalls.kt`** -> AI Confidence: **99.48%**
2687. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SingletonOrConstantDelegationLowering.kt`** -> AI Confidence: **99.48%**
2688. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SingletonReferencesLowering.kt`** -> AI Confidence: **99.48%**
2689. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SpecialAccess.kt`** -> AI Confidence: **99.48%**
2690. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/StaticCallableReferenceLowering.kt`** -> AI Confidence: **99.48%**
2691. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/StaticDefaultFunctionLowering.kt`** -> AI Confidence: **99.48%**
2692. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/StaticInitializersLowering.kt`** -> AI Confidence: **99.48%**
2693. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SuspendLambdaLowering.kt`** -> AI Confidence: **99.48%**
2694. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/SyntheticAccessorLowering.kt`** -> AI Confidence: **99.48%**
2695. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/TailCallOptimizationLowering.kt`** -> AI Confidence: **99.48%**
2696. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/ToArrayLowering.kt`** -> AI Confidence: **99.48%**
2697. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/TypeAliasAnnotationMethodsLowering.kt`** -> AI Confidence: **99.48%**
2698. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/TypeOperatorLowering.kt`** -> AI Confidence: **99.48%**
2699. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/TypeSwitchLowering.kt`** -> AI Confidence: **99.48%**
2700. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/UniqueLoopLabelsLowering.kt`** -> AI Confidence: **99.48%**
2701. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/VarargLowering.kt`** -> AI Confidence: **99.48%**
2702. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/indy/LambdaMetafactoryArguments.kt`** -> AI Confidence: **99.48%**
2703. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/indy/SamDelegatingLambdaBlock.kt`** -> AI Confidence: **99.48%**
2704. **`compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower/irValidation.kt`** -> AI Confidence: **99.48%**
2705. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/InlineClassAbi.kt`** -> AI Confidence: **99.48%**
2706. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmBackendContext.kt`** -> AI Confidence: **99.48%**
2707. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmBackendErrors.kt`** -> AI Confidence: **99.48%**
2708. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmBackendExtension.kt`** -> AI Confidence: **99.48%**
2709. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmCachedDeclarations.kt`** -> AI Confidence: **99.48%**
2710. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmInnerClassesSupport.kt`** -> AI Confidence: **99.48%**
2711. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmIrAttributes.kt`** -> AI Confidence: **99.48%**
2712. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmIrSpecialAnnotationSymbolProvider.kt`** -> AI Confidence: **99.48%**
2713. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmIrTypeSystemContext.kt`** -> AI Confidence: **99.48%**
2714. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmSharedVariablesManager.kt`** -> AI Confidence: **99.48%**
2715. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmSymbols.kt`** -> AI Confidence: **99.48%**
2716. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/JvmSyntheticAccessorGenerator.kt`** -> AI Confidence: **99.48%**
2717. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MemoizedInlineClassReplacements.kt`** -> AI Confidence: **99.48%**
2718. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MemoizedMultiFieldValueClassReplacements.kt`** -> AI Confidence: **99.48%**
2719. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MemoizedValueClassAbstractReplacements.kt`** -> AI Confidence: **99.48%**
2720. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MfvcNode.kt`** -> AI Confidence: **99.48%**
2721. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MfvcNodeFactory.kt`** -> AI Confidence: **99.48%**
2722. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/MfvcNodeInstance.kt`** -> AI Confidence: **99.48%**
2723. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/extensions/ClassBuilderExtensionAdapter.kt`** -> AI Confidence: **99.48%**
2724. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/extensions/JvmIrDeclarationOrigin.kt`** -> AI Confidence: **99.48%**
2725. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/IrArrayBuilder.kt`** -> AI Confidence: **99.48%**
2726. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/IrInlineReferenceLocator.kt`** -> AI Confidence: **99.48%**
2727. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/IrJvmFlexibleType.kt`** -> AI Confidence: **99.48%**
2728. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmDefaultUtils.kt`** -> AI Confidence: **99.48%**
2729. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmIrCoroutineUtils.kt`** -> AI Confidence: **99.48%**
2730. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmIrInlineUtils.kt`** -> AI Confidence: **99.48%**
2731. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmIrTypeUtils.kt`** -> AI Confidence: **99.48%**
2732. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/ir/JvmIrUtils.kt`** -> AI Confidence: **99.48%**
2733. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/mapping/GenericSignatureMapper.kt`** -> AI Confidence: **99.48%**
2734. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/mapping/IrTypeMapper.kt`** -> AI Confidence: **99.48%**
2735. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/mapping/IrTypeMapping.kt`** -> AI Confidence: **99.48%**
2736. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/mapping/MethodSignatureMapper.kt`** -> AI Confidence: **99.48%**
2737. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/metadata/DescriptorMetadataSerializer.kt`** -> AI Confidence: **99.48%**
2738. **`compiler/ir/backend.jvm/src/org/jetbrains/kotlin/backend/jvm/overrides/IrJavaIncompatibilityRulesOverridabilityCondition.kt`** -> AI Confidence: **99.48%**
2739. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/IrTypeInlineClassesSupport.kt`** -> AI Confidence: **99.48%**
2740. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/NativeCompilationConfig.kt`** -> AI Confidence: **99.48%**
2741. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/Reporting.kt`** -> AI Confidence: **99.48%**
2742. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cgen/InteropIrUtils.kt`** -> AI Confidence: **99.48%**
2743. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/checkers/EscapeAnalysisChecker.kt`** -> AI Confidence: **99.48%**
2744. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/Intrinsics.kt`** -> AI Confidence: **99.48%**
2745. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/Ir.kt`** -> AI Confidence: **99.48%**
2746. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/Utils.kt`** -> AI Confidence: **99.48%**
2747. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/annotations/BindClassToObjCName.kt`** -> AI Confidence: **99.48%**
2748. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/SpecialBackendChecksTraversal.kt`** -> AI Confidence: **99.48%**
2749. **`compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TestProcessor.kt`** -> AI Confidence: **99.48%**
2750. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/BackendWasmSymbols.kt`** -> AI Confidence: **99.48%**
2751. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/WasmBackendContext.kt`** -> AI Confidence: **99.48%**
2752. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/WasmLoweringPhases.kt`** -> AI Confidence: **99.48%**
2753. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/compilerWithIC.kt`** -> AI Confidence: **99.48%**
2754. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/dce/Dce.kt`** -> AI Confidence: **99.48%**
2755. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/dce/WasmUsefulDeclarationProcessor.kt`** -> AI Confidence: **99.48%**
2756. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/dce/WasmUselessDeclarationsRemover.kt`** -> AI Confidence: **99.48%**
2757. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/dwarf/LineProgram.kt`** -> AI Confidence: **99.48%**
2758. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/export/ExportModelGenerator.kt`** -> AI Confidence: **99.48%**
2759. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ic/IrFactoryImplForWasmIC.kt`** -> AI Confidence: **99.48%**
2760. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/ClassInfo.kt`** -> AI Confidence: **99.48%**
2761. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/DefinedDeclarationsResolver.kt`** -> AI Confidence: **99.48%**
2762. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/WasmCompiledFragments.kt`** -> AI Confidence: **99.48%**
2763. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/WasmCompiledModuleFragment.kt`** -> AI Confidence: **99.48%**
2764. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenContexts/WasmDeclarationCodegenContext.kt`** -> AI Confidence: **99.48%**
2765. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenContexts/WasmFunctionCodegenContext.kt`** -> AI Confidence: **99.48%**
2766. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenContexts/WasmLinkerDataCodegenContext.kt`** -> AI Confidence: **99.48%**
2767. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenContexts/WasmTrackedTypeCodegenContext.kt`** -> AI Confidence: **99.48%**
2768. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenContexts/WasmTypeCodegenContext.kt`** -> AI Confidence: **99.48%**
2769. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/BodyGenerator.kt`** -> AI Confidence: **99.48%**
2770. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/DeclarationGenerator.kt`** -> AI Confidence: **99.48%**
2771. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/ImportsGenerator.kt`** -> AI Confidence: **99.48%**
2772. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/IrFileToWasmIrGenerator.kt`** -> AI Confidence: **99.48%**
2773. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/OptimisedWhenGenerator.kt`** -> AI Confidence: **99.48%**
2774. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/TypeGenerator.kt`** -> AI Confidence: **99.48%**
2775. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/TypeTransformer.kt`** -> AI Confidence: **99.48%**
2776. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/codegenGenerators/WasmModuleFragmentGenerator.kt`** -> AI Confidence: **99.48%**
2777. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/ir2wasm/locationUtils.kt`** -> AI Confidence: **99.48%**
2778. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/AssociatedObjectsLowering.kt`** -> AI Confidence: **99.48%**
2779. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/BuiltInsLowering.kt`** -> AI Confidence: **99.48%**
2780. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/ComplexExternalDeclarationsToTopLevelFunctionsLowering.kt`** -> AI Confidence: **99.48%**
2781. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/EraseVirtualDispatchReceiverParametersTypes.kt`** -> AI Confidence: **99.48%**
2782. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/ExcludeDeclarationsFromCodegen.kt`** -> AI Confidence: **99.48%**
2783. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/ExplicitlyCastExternalTypesLowering.kt`** -> AI Confidence: **99.48%**
2784. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/FieldInitializersLowering.kt`** -> AI Confidence: **99.48%**
2785. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/GenerateWasmTests.kt`** -> AI Confidence: **99.48%**
2786. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/GenericReturnTypeLowering.kt`** -> AI Confidence: **99.48%**
2787. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/InvokeOnExportedFunctionExitLowering.kt`** -> AI Confidence: **99.48%**
2788. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/JsCodeCallsLowering.kt`** -> AI Confidence: **99.48%**
2789. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/JsInteropFunctionsLowering.kt`** -> AI Confidence: **99.48%**
2790. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/TryCatchCanonicalization.kt`** -> AI Confidence: **99.48%**
2791. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/UnitToVoidLowering.kt`** -> AI Confidence: **99.48%**
2792. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/VirtualDispatchReceiverExtraction.kt`** -> AI Confidence: **99.48%**
2793. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmBridgesConstruction.kt`** -> AI Confidence: **99.48%**
2794. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmCallableReferenceLowering.kt`** -> AI Confidence: **99.48%**
2795. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmPropertyReferenceLowering.kt`** -> AI Confidence: **99.48%**
2796. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmPurifyObjectInstanceGettersLowering.kt`** -> AI Confidence: **99.48%**
2797. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmStaticCallableReferenceLowering.kt`** -> AI Confidence: **99.48%**
2798. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmStringConcatenationLowering.kt`** -> AI Confidence: **99.48%**
2799. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmStringSwitchOptimizerLowering.kt`** -> AI Confidence: **99.48%**
2800. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmTypeOperatorLowering.kt`** -> AI Confidence: **99.48%**
2801. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WasmVarargExpressionLowering.kt`** -> AI Confidence: **99.48%**
2802. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/WhenBranchOptimiserLowering.kt`** -> AI Confidence: **99.48%**
2803. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/generateMainFunctionCalls.kt`** -> AI Confidence: **99.48%**
2804. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/lower/markAdditionalExportedDeclarations.kt`** -> AI Confidence: **99.48%**
2805. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/serialization/WasmDeserializer.kt`** -> AI Confidence: **99.48%**
2806. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/serialization/WasmSerializer.kt`** -> AI Confidence: **99.48%**
2807. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/Annotations.kt`** -> AI Confidence: **99.48%**
2808. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/DwarfGenerator.kt`** -> AI Confidence: **99.48%**
2809. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/SourceMapGenerator.kt`** -> AI Confidence: **99.48%**
2810. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/Utils.kt`** -> AI Confidence: **99.48%**
2811. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/utils/WasmInlineClassesUtils.kt`** -> AI Confidence: **99.48%**
2812. **`compiler/ir/backend.wasm/src/org/jetbrains/kotlin/backend/wasm/wasmCompiler.kt`** -> AI Confidence: **99.48%**
2813. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/ExpectActualCollector.kt`** -> AI Confidence: **99.48%**
2814. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/ExpectActualLinker.kt`** -> AI Confidence: **99.48%**
2815. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/FunctionDefaultParametersActualizer.kt`** -> AI Confidence: **99.48%**
2816. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrActualizationErrors.kt`** -> AI Confidence: **99.48%**
2817. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrActualizer.kt`** -> AI Confidence: **99.48%**
2818. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrActualizerUtils.kt`** -> AI Confidence: **99.48%**
2819. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrExpectActualMap.kt`** -> AI Confidence: **99.48%**
2820. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/IrExpectActualMatchingContext.kt`** -> AI Confidence: **99.48%**
2821. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/SpecialFakeOverrideSymbolsResolver.kt`** -> AI Confidence: **99.48%**
2822. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/IrAnnotationConflictingDefaultArgumentValueKmpChecker.kt`** -> AI Confidence: **99.48%**
2823. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/IrAnnotationMatchingKmpChecker.kt`** -> AI Confidence: **99.48%**
2824. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/IrJavaDirectActualizationDefaultParametersInActualKmpChecker.kt`** -> AI Confidence: **99.48%**
2825. **`compiler/ir/ir.actualization/src/main/kotlin/org/jetbrains/kotlin/backend/common/actualizer/checker/IrKotlinActualAnnotationOnJavaKmpChecker.kt`** -> AI Confidence: **99.48%**
2826. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/CommonLoweringPhases.kt`** -> AI Confidence: **99.48%**
2827. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/FunctionInlining.kt`** -> AI Confidence: **99.48%**
2828. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/InlineFunctionBodyPreprocessor.kt`** -> AI Confidence: **99.48%**
2829. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/InlineFunctionResolver.kt`** -> AI Confidence: **99.48%**
2830. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/InlineFunctionSerializationPreProcessing.kt`** -> AI Confidence: **99.48%**
2831. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/OuterThisInInlineFunctionsSpecialAccessorLowering.kt`** -> AI Confidence: **99.48%**
2832. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/SyntheticAccessorLowering.kt`** -> AI Confidence: **99.48%**
2833. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/checkers/IrInlineDeclarationChecker.kt`** -> AI Confidence: **99.48%**
2834. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/diagnostics/IrInlinerErrors.kt`** -> AI Confidence: **99.48%**
2835. **`compiler/ir/ir.inline/src/org/jetbrains/kotlin/ir/inline/konan/NativeFirstPhaseLoweringPhases.kt`** -> AI Confidence: **99.48%**
2836. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/CallInterceptor.kt`** -> AI Confidence: **99.48%**
2837. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/InstructionsUnfolder.kt`** -> AI Confidence: **99.48%**
2838. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/IrInterpreter.kt`** -> AI Confidence: **99.48%**
2839. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/IrInterpreterEnvironment.kt`** -> AI Confidence: **99.48%**
2840. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/IrTreeBuildUtils.kt`** -> AI Confidence: **99.48%**
2841. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/Utils.kt`** -> AI Confidence: **99.48%**
2842. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/checker/EvaluationMode.kt`** -> AI Confidence: **99.48%**
2843. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/checker/IrInterpreterCommonChecker.kt`** -> AI Confidence: **99.48%**
2844. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/intrinsics/IntrinsicImplementations.kt`** -> AI Confidence: **99.48%**
2845. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/preprocessor/IrInterpreterConstGetterPreprocessor.kt`** -> AI Confidence: **99.48%**
2846. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/preprocessor/IrInterpreterKCallableNamePreprocessor.kt`** -> AI Confidence: **99.48%**
2847. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/CommonProxy.kt`** -> AI Confidence: **99.48%**
2848. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/Proxy.kt`** -> AI Confidence: **99.48%**
2849. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/reflection/AbstractKPropertyProxy.kt`** -> AI Confidence: **99.48%**
2850. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/reflection/KClassProxy.kt`** -> AI Confidence: **99.48%**
2851. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/reflection/KFunctionProxy.kt`** -> AI Confidence: **99.48%**
2852. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/stack/CallStack.kt`** -> AI Confidence: **99.48%**
2853. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/stack/Frame.kt`** -> AI Confidence: **99.48%**
2854. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/Common.kt`** -> AI Confidence: **99.48%**
2855. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/Complex.kt`** -> AI Confidence: **99.48%**
2856. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/ExceptionState.kt`** -> AI Confidence: **99.48%**
2857. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/Primitive.kt`** -> AI Confidence: **99.48%**
2858. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/State.kt`** -> AI Confidence: **99.48%**
2859. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/Wrapper.kt`** -> AI Confidence: **99.48%**
2860. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/KClassState.kt`** -> AI Confidence: **99.48%**
2861. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/KFunctionState.kt`** -> AI Confidence: **99.48%**
2862. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/KPropertyState.kt`** -> AI Confidence: **99.48%**
2863. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/KTypeState.kt`** -> AI Confidence: **99.48%**
2864. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/state/reflection/ReflectionState.kt`** -> AI Confidence: **99.48%**
2865. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstAnnotationTransformer.kt`** -> AI Confidence: **99.48%**
2866. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstDeclarationAnnotationTransformer.kt`** -> AI Confidence: **99.48%**
2867. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstEvaluationContext.kt`** -> AI Confidence: **99.48%**
2868. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstExpressionTransformer.kt`** -> AI Confidence: **99.48%**
2869. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstOnlyNecessaryTransformer.kt`** -> AI Confidence: **99.48%**
2870. **`compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/transformer/IrConstTransformer.kt`** -> AI Confidence: **99.48%**
2871. **`compiler/ir/ir.objcinterop/src/org/jetbrains/kotlin/ir/objcinterop/IrObjCOverridablilityCondidtion.kt`** -> AI Confidence: **99.48%**
2872. **`compiler/ir/ir.objcinterop/src/org/jetbrains/kotlin/ir/objcinterop/ObjCInterop.kt`** -> AI Confidence: **99.48%**
2873. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/KotlinUtils.kt`** -> AI Confidence: **99.48%**
2874. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/Psi2IrTranslator.kt`** -> AI Confidence: **99.48%**
2875. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/descriptors/IrBuiltInsOverDescriptors.kt`** -> AI Confidence: **99.48%**
2876. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/descriptors/IrDescriptorBasedFunctionFactory.kt`** -> AI Confidence: **99.48%**
2877. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/descriptors/IrExpressionBuilders.kt`** -> AI Confidence: **99.48%**
2878. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/AnonymousInitializerGenerator.kt`** -> AI Confidence: **99.48%**
2879. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ArgumentsGenerationUtils.kt`** -> AI Confidence: **99.48%**
2880. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/AssignmentGenerator.kt`** -> AI Confidence: **99.48%**
2881. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/BodyGenerator.kt`** -> AI Confidence: **99.48%**
2882. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/BranchingExpressionGenerator.kt`** -> AI Confidence: **99.48%**
2883. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/CallGenerator.kt`** -> AI Confidence: **99.48%**
2884. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ClassGenerator.kt`** -> AI Confidence: **99.48%**
2885. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ConstantValueGeneratorImpl.kt`** -> AI Confidence: **99.48%**
2886. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DataClassMembersGenerator.kt`** -> AI Confidence: **99.48%**
2887. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DeclarationGenerator.kt`** -> AI Confidence: **99.48%**
2888. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DeclarationStubGeneratorImpl.kt`** -> AI Confidence: **99.48%**
2889. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/DelegatedPropertyGenerator.kt`** -> AI Confidence: **99.48%**
2890. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/EnumClassMembersGenerator.kt`** -> AI Confidence: **99.48%**
2891. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ErrorExpressionGenerator.kt`** -> AI Confidence: **99.48%**
2892. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/FunctionGenerator.kt`** -> AI Confidence: **99.48%**
2893. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/Generator.kt`** -> AI Confidence: **99.48%**
2894. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/GeneratorContext.kt`** -> AI Confidence: **99.48%**
2895. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/IrSyntheticDeclarationGenerator.kt`** -> AI Confidence: **99.48%**
2896. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/LocalClassGenerator.kt`** -> AI Confidence: **99.48%**
2897. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/LocalFunctionGenerator.kt`** -> AI Confidence: **99.48%**
2898. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/LoopExpressionGenerator.kt`** -> AI Confidence: **99.48%**
2899. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ModuleGenerator.kt`** -> AI Confidence: **99.48%**
2900. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/OperatorExpressionGenerator.kt`** -> AI Confidence: **99.48%**
2901. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/PropertyGenerator.kt`** -> AI Confidence: **99.48%**
2902. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/ReflectionReferencesGenerator.kt`** -> AI Confidence: **99.48%**
2903. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/SamTypeFactory.kt`** -> AI Confidence: **99.48%**
2904. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/StandaloneDeclarationGenerator.kt`** -> AI Confidence: **99.48%**
2905. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/StatementGenerator.kt`** -> AI Confidence: **99.48%**
2906. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/SyntheticDeclarationsGenerator.kt`** -> AI Confidence: **99.48%**
2907. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/TryCatchExpressionGenerator.kt`** -> AI Confidence: **99.48%**
2908. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/TypeTranslatorImpl.kt`** -> AI Confidence: **99.48%**
2909. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/fragments/FragmentCompilerSymbolTableDecorator.kt`** -> AI Confidence: **99.48%**
2910. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/fragments/FragmentDeclarationGenerator.kt`** -> AI Confidence: **99.48%**
2911. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/fragments/FragmentModuleGenerator.kt`** -> AI Confidence: **99.48%**
2912. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/generators/samConversions.kt`** -> AI Confidence: **99.48%**
2913. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/ArrayAccessAssignmentReceiver.kt`** -> AI Confidence: **99.48%**
2914. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/CallBuilder.kt`** -> AI Confidence: **99.48%**
2915. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/DynamicMemberLValue.kt`** -> AI Confidence: **99.48%**
2916. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/PropertyLValue.kt`** -> AI Confidence: **99.48%**
2917. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/SafeCallReceiver.kt`** -> AI Confidence: **99.48%**
2918. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/intermediate/SafeExtensionInvokeCallReceiver.kt`** -> AI Confidence: **99.48%**
2919. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/lazy/IrLazyClass.kt`** -> AI Confidence: **99.48%**
2920. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/lazy/IrLazyField.kt`** -> AI Confidence: **99.48%**
2921. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/lazy/IrLazyFunction.kt`** -> AI Confidence: **99.48%**
2922. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/lazy/IrLazyProperty.kt`** -> AI Confidence: **99.48%**
2923. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/lazy/LazyScopedTypeParametersResolver.kt`** -> AI Confidence: **99.48%**
2924. **`compiler/ir/ir.psi2ir/src/org/jetbrains/kotlin/psi2ir/transformations/InsertImplicitCasts.kt`** -> AI Confidence: **99.48%**
2925. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/IrBuiltIns.kt`** -> AI Confidence: **99.48%**
2926. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/IrBuiltInsOverSymbolFinder.kt`** -> AI Confidence: **99.48%**
2927. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/IrDiagnosticReporter.kt`** -> AI Confidence: **99.48%**
2928. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/KtDiagnosticReporterWithImplicitIrBasedContext.kt`** -> AI Confidence: **99.48%**
2929. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/SymbolFinder.kt`** -> AI Confidence: **99.48%**
2930. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/builders/ExpressionHelpers.kt`** -> AI Confidence: **99.48%**
2931. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/builders/IrBuilder.kt`** -> AI Confidence: **99.48%**
2932. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/builders/Primitives.kt`** -> AI Confidence: **99.48%**
2933. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/builders/Scope.kt`** -> AI Confidence: **99.48%**
2934. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/builders/declarations/IrDeclarationBuilder.kt`** -> AI Confidence: **99.48%**
2935. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/builders/declarations/declarationBuilders.kt`** -> AI Confidence: **99.48%**
2936. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/declarations/IrDeclarations.kt`** -> AI Confidence: **99.48%**
2937. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/declarations/IrFactory.kt`** -> AI Confidence: **99.48%**
2938. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/declarations/IrFunction.kt`** -> AI Confidence: **99.48%**
2939. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/declarations/IrPackageFragments.kt`** -> AI Confidence: **99.48%**
2940. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/declarations/IrValueParameter.kt`** -> AI Confidence: **99.48%**
2941. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/descriptors/IrBasedDescriptors.kt`** -> AI Confidence: **99.48%**
2942. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/descriptors/IrBuiltinFunctionDescriptor.kt`** -> AI Confidence: **99.48%**
2943. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/descriptors/IrDelegateDescriptor.kt`** -> AI Confidence: **99.48%**
2944. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/expressions/IrExpressions.kt`** -> AI Confidence: **99.48%**
2945. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/expressions/IrMemberAccessExpression.kt`** -> AI Confidence: **99.48%**
2946. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/expressions/impl/builders.kt`** -> AI Confidence: **99.48%**
2947. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/CopyIrTreeWithSymbolsForFakeOverrides.kt`** -> AI Confidence: **99.48%**
2948. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/FakeOverrideBuilderStrategy.kt`** -> AI Confidence: **99.48%**
2949. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/FakeOverrideCopier.kt`** -> AI Confidence: **99.48%**
2950. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/IrFakeOverrideBuilder.kt`** -> AI Confidence: **99.48%**
2951. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/overrides/IrOverrideChecker.kt`** -> AI Confidence: **99.48%**
2952. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/symbols/impl/IrSymbolImpl.kt`** -> AI Confidence: **99.48%**
2953. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/IrType.kt`** -> AI Confidence: **99.48%**
2954. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/IrTypeSubstitutor.kt`** -> AI Confidence: **99.48%**
2955. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/IrTypeSystemContext.kt`** -> AI Confidence: **99.48%**
2956. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/impl/IrSimpleTypeImpl.kt`** -> AI Confidence: **99.48%**
2957. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/irTypePredicates.kt`** -> AI Confidence: **99.48%**
2958. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/types/irTypes.kt`** -> AI Confidence: **99.48%**
2959. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/AdditionalIrUtils.kt`** -> AI Confidence: **99.48%**
2960. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/ConstantValueGenerator.kt`** -> AI Confidence: **99.48%**
2961. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DataClassMembersGenerator.kt`** -> AI Confidence: **99.48%**
2962. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DeepCopyIrTreeWithSymbols.kt`** -> AI Confidence: **99.48%**
2963. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DescriptorSymbolTableExtension.kt`** -> AI Confidence: **99.48%**
2964. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DescriptorToIrUtil.kt`** -> AI Confidence: **99.48%**
2965. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/DumpIrTree.kt`** -> AI Confidence: **99.48%**
2966. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrTypeErasureUtils.kt`** -> AI Confidence: **99.48%**
2967. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrTypeUtils.kt`** -> AI Confidence: **99.48%**
2968. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrUtils.kt`** -> AI Confidence: **99.48%**
2969. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/RenderIrElement.kt`** -> AI Confidence: **99.48%**
2970. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/TypeRemapper.kt`** -> AI Confidence: **99.48%**
2971. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/TypeTranslator.kt`** -> AI Confidence: **99.48%**
2972. **`compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/dumpKotlinLike.kt`** -> AI Confidence: **99.48%**
2973. **`compiler/ir/ir.tree/testFixtures/org/jetbrains/kotlin/ir/TestIrBuiltins.kt`** -> AI Confidence: **99.48%**
2974. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/ImplementationConfigurator.kt`** -> AI Confidence: **99.48%**
2975. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/IrSymbolTree.kt`** -> AI Confidence: **99.48%**
2976. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/IrTree.kt`** -> AI Confidence: **99.48%**
2977. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/Main.kt`** -> AI Confidence: **99.48%**
2978. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/model/Element.kt`** -> AI Confidence: **99.48%**
2979. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/DeepCopyIrTreeWithSymbolsPrinter.kt`** -> AI Confidence: **99.48%**
2980. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/ElementPrinter.kt`** -> AI Confidence: **99.48%**
2981. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/ImplementationPrinter.kt`** -> AI Confidence: **99.48%**
2982. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/IrTreeSymbolsVisitorPrinter.kt`** -> AI Confidence: **99.48%**
2983. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TransformerPrinter.kt`** -> AI Confidence: **99.48%**
2984. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TransformerVoidPrinter.kt`** -> AI Confidence: **99.48%**
2985. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TypeTransformerPrinter.kt`** -> AI Confidence: **99.48%**
2986. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TypeTransformerVoidPrinter.kt`** -> AI Confidence: **99.48%**
2987. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TypeVisitorPrinter.kt`** -> AI Confidence: **99.48%**
2988. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/TypeVisitorVoidPrinter.kt`** -> AI Confidence: **99.48%**
2989. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/symbol/SymbolImplementationPrinter.kt`** -> AI Confidence: **99.48%**
2990. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/symbol/SymbolPrinter.kt`** -> AI Confidence: **99.48%**
2991. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/symbol/SymbolRemapperPrinter.kt`** -> AI Confidence: **99.48%**
2992. **`compiler/ir/ir.tree/tree-generator/src/org/jetbrains/kotlin/ir/generator/print/symbol/SymbolVisitorPrinter.kt`** -> AI Confidence: **99.48%**
2993. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/IrValidator.kt`** -> AI Confidence: **99.48%**
2994. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/IrValidatorConfig.kt`** -> AI Confidence: **99.48%**
2995. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/CheckTreeConsistencyVisitor.kt`** -> AI Confidence: **99.48%**
2996. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/CheckerUtils.kt`** -> AI Confidence: **99.48%**
2997. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/context/CheckerContext.kt`** -> AI Confidence: **99.48%**
2998. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/context/ValueScopeUpdater.kt`** -> AI Confidence: **99.48%**
2999. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/expression/IrCallTypeChecker.kt`** -> AI Confidence: **99.48%**
3000. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/expression/IrCrossFileFieldUsageChecker.kt`** -> AI Confidence: **99.48%**
3001. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/expression/IrNothingTypeExpressionChecker.kt`** -> AI Confidence: **99.48%**
3002. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/expression/IrValueAccessScopeChecker.kt`** -> AI Confidence: **99.48%**
3003. **`compiler/ir/ir.validation/src/org/jetbrains/kotlin/ir/validation/checkers/type/IrTypeParameterScopeChecker.kt`** -> AI Confidence: **99.48%**
3004. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/DumpIrReferenceRenderingAsSignatureStrategy.kt`** -> AI Confidence: **99.48%**
3005. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/KlibLoaderExtensions.kt`** -> AI Confidence: **99.48%**
3006. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/diagnostics/LibrarySpecialCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
3007. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/diagnostics/SerializationErrors.kt`** -> AI Confidence: **99.48%**
3008. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/issues/KotlinIrLinkerIssues.kt`** -> AI Confidence: **99.48%**
3009. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/issues/SignatureClashDetector.kt`** -> AI Confidence: **99.48%**
3010. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/ClassifierExplorer.kt`** -> AI Confidence: **99.48%**
3011. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/MissingDeclarationStubGenerator.kt`** -> AI Confidence: **99.48%**
3012. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageErrorMessages.kt`** -> AI Confidence: **99.48%**
3013. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageSources.kt`** -> AI Confidence: **99.48%**
3014. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageSupportForLinkerImpl.kt`** -> AI Confidence: **99.48%**
3015. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageSupportForLoweringsImpl.kt`** -> AI Confidence: **99.48%**
3016. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartialLinkageUtils.kt`** -> AI Confidence: **99.48%**
3017. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/linkage/partial/PartiallyLinkedIrTreePatcher.kt`** -> AI Confidence: **99.48%**
3018. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/overrides/FakeOverrideChecker.kt`** -> AI Confidence: **99.48%**
3019. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/overrides/FakeOverrides.kt`** -> AI Confidence: **99.48%**
3020. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/BasicIrModuleDeserializer.kt`** -> AI Confidence: **99.48%**
3021. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/DeclarationTable.kt`** -> AI Confidence: **99.48%**
3022. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/DescriptorByIdSignatureFinderImpl.kt`** -> AI Confidence: **99.48%**
3023. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IdSignatureDeserializer.kt`** -> AI Confidence: **99.48%**
3024. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IdSignatureSerializer.kt`** -> AI Confidence: **99.48%**
3025. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrBodyDeserializer.kt`** -> AI Confidence: **99.48%**
3026. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrDeclarationDeserializer.kt`** -> AI Confidence: **99.48%**
3027. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrFileDeserializer.kt`** -> AI Confidence: **99.48%**
3028. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrFileSerializer.kt`** -> AI Confidence: **99.48%**
3029. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrModuleDeserializer.kt`** -> AI Confidence: **99.48%**
3030. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrModuleSerializer.kt`** -> AI Confidence: **99.48%**
3031. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrSymbolDeserializer.kt`** -> AI Confidence: **99.48%**
3032. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/KotlinIrLinker.kt`** -> AI Confidence: **99.48%**
3033. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/LegacyDescriptorUtils.kt`** -> AI Confidence: **99.48%**
3034. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/NonLinkingIrInlineFunctionDeserializer.kt`** -> AI Confidence: **99.48%**
3035. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/encodings/BinaryFlags.kt`** -> AI Confidence: **99.48%**
3036. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/mangle/descriptor/DescriptorMangleComputer.kt`** -> AI Confidence: **99.48%**
3037. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/mangle/ir/IrExportCheckerVisitor.kt`** -> AI Confidence: **99.48%**
3038. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/mangle/ir/IrMangleComputer.kt`** -> AI Confidence: **99.48%**
3039. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/metadata/DynamicTypeDeserializer.kt`** -> AI Confidence: **99.48%**
3040. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/metadata/KlibMetadataMonolithicSerializer.kt`** -> AI Confidence: **99.48%**
3041. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/metadata/KlibMetadataSerializer.kt`** -> AI Confidence: **99.48%**
3042. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/metadata/KlibMetadataSerializerExtension.kt`** -> AI Confidence: **99.48%**
3043. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/serializeModuleIntoKlib.kt`** -> AI Confidence: **99.48%**
3044. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/signature/IdSignatureComputers.kt`** -> AI Confidence: **99.48%**
3045. **`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/signature/IdSignatureDescriptor.kt`** -> AI Confidence: **99.48%**
3046. **`compiler/ir/serialization.jklib/src/org/jetbrains/kotlin/ir/backend/jklib/JKlibIrLinker.kt`** -> AI Confidence: **99.48%**
3047. **`compiler/ir/serialization.jklib/src/org/jetbrains/kotlin/ir/backend/jklib/JKlibIrMangler.kt`** -> AI Confidence: **99.48%**
3048. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/KlibMetadataIncrementalSerializer.kt`** -> AI Confidence: **99.48%**
3049. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/ModulesStructure.kt`** -> AI Confidence: **99.48%**
3050. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/checkers/JsKlibCheckers.kt`** -> AI Confidence: **99.48%**
3051. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/checkers/JsKlibErrors.kt`** -> AI Confidence: **99.48%**
3052. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/checkers/declarations/JsKlibPossibleFileClashWarning.kt`** -> AI Confidence: **99.48%**
3053. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/checkers/expressions/JsKlibJsCodeCallChecker.kt`** -> AI Confidence: **99.48%**
3054. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/klib.kt`** -> AI Confidence: **99.48%**
3055. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/loadWebKlibs.kt`** -> AI Confidence: **99.48%**
3056. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/lower/serialization/ir/JsExportUtils.kt`** -> AI Confidence: **99.48%**
3057. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/lower/serialization/ir/JsIrLinker.kt`** -> AI Confidence: **99.48%**
3058. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/lower/serialization/ir/JsMangler.kt`** -> AI Confidence: **99.48%**
3059. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/wasm/WasmExportUtils.kt`** -> AI Confidence: **99.48%**
3060. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/wasm/WasmKlibCheckers.kt`** -> AI Confidence: **99.48%**
3061. **`compiler/ir/serialization.js/src/org/jetbrains/kotlin/ir/backend/js/wasm/WasmKlibExportingDeclaration.kt`** -> AI Confidence: **99.48%**
3062. **`compiler/ir/serialization.jvm/src/org/jetbrains/kotlin/backend/jvm/serialization/JvmIdSignatureDescriptor.kt`** -> AI Confidence: **99.48%**
3063. **`compiler/ir/serialization.jvm/src/org/jetbrains/kotlin/ir/backend/jvm/serialization/JvmIrLinker.kt`** -> AI Confidence: **99.48%**
3064. **`compiler/ir/serialization.jvm/src/org/jetbrains/kotlin/ir/backend/jvm/serialization/JvmMangler.kt`** -> AI Confidence: **99.48%**
3065. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/IrUtils.kt`** -> AI Confidence: **99.48%**
3066. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanFakeOverrideClassFilter.kt`** -> AI Confidence: **99.48%**
3067. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanForwardDeclarationModuleDeserializer.kt`** -> AI Confidence: **99.48%**
3068. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanIrFileSerializer.kt`** -> AI Confidence: **99.48%**
3069. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanIrLinker.kt`** -> AI Confidence: **99.48%**
3070. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanLibrarySpecialCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
3071. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanMangler.kt`** -> AI Confidence: **99.48%**
3072. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanPartialModuleDeserializer.kt`** -> AI Confidence: **99.48%**
3073. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/ObjCFunctionNameMangleComputer.kt`** -> AI Confidence: **99.48%**
3074. **`compiler/ir/serialization.native/src/org/jetbrains/kotlin/backend/konan/serialization/loadNativeKlibs.kt`** -> AI Confidence: **99.48%**
3075. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/JavacWrapper.kt`** -> AI Confidence: **99.48%**
3076. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/ClassifierResolver.kt`** -> AI Confidence: **99.48%**
3077. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/IdentifierResolver.kt`** -> AI Confidence: **99.48%**
3078. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/KotlinClassifiersCache.kt`** -> AI Confidence: **99.48%**
3079. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/ResolveHelper.kt`** -> AI Confidence: **99.48%**
3080. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/symbols/FakeSymbolBasedClass.kt`** -> AI Confidence: **99.48%**
3081. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/symbols/SymbolBasedClass.kt`** -> AI Confidence: **99.48%**
3082. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/symbols/symbolBasedAnnotationArguments.kt`** -> AI Confidence: **99.48%**
3083. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/symbols/symbolBasedTypes.kt`** -> AI Confidence: **99.48%**
3084. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/symbols/utils.kt`** -> AI Confidence: **99.48%**
3085. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedAnnotation.kt`** -> AI Confidence: **99.48%**
3086. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedClass.kt`** -> AI Confidence: **99.48%**
3087. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedField.kt`** -> AI Confidence: **99.48%**
3088. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedMethod.kt`** -> AI Confidence: **99.48%**
3089. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/TreeBasedTypeParameter.kt`** -> AI Confidence: **99.48%**
3090. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/treeBasedTypes.kt`** -> AI Confidence: **99.48%**
3091. **`compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/wrappers/trees/utils.kt`** -> AI Confidence: **99.48%**
3092. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/LightClassGenerationSupport.kt`** -> AI Confidence: **99.48%**
3093. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KotlinLightTypeParameterListBuilder.kt`** -> AI Confidence: **99.48%**
3094. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightMemberImpl.kt`** -> AI Confidence: **99.48%**
3095. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightMethodImpl.kt`** -> AI Confidence: **99.48%**
3096. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightModifierList.kt`** -> AI Confidence: **99.48%**
3097. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightModifierListDescriptorBased.kt`** -> AI Confidence: **99.48%**
3098. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightParameterList.kt`** -> AI Confidence: **99.48%**
3099. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightPsiClassObjectAccessExpression.kt`** -> AI Confidence: **99.48%**
3100. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtLightPsiLiteral.kt`** -> AI Confidence: **99.48%**
3101. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/KtToJvmAnnotationsConverter.kt`** -> AI Confidence: **99.48%**
3102. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/elements/lightAnnotations.kt`** -> AI Confidence: **99.48%**
3103. **`compiler/light-classes/src/org/jetbrains/kotlin/asJava/utils.kt`** -> AI Confidence: **99.48%**
3104. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/lexer/KDocLexer.kt`** -> AI Confidence: **99.48%**
3105. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/lexer/KtTokens.kt`** -> AI Confidence: **99.48%**
3106. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/KDocParser.kt`** -> AI Confidence: **99.48%**
3107. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/KotlinParser.kt`** -> AI Confidence: **99.48%**
3108. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/KotlinExpressionParsing.kt`** -> AI Confidence: **99.48%**
3109. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/KotlinParsing.kt`** -> AI Confidence: **99.48%**
3110. **`compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/SemanticWhitespaceAwareSyntaxBuilders.kt`** -> AI Confidence: **99.48%**
3111. **`compiler/psi/parser/src/org/jetbrains/kotlin/kdoc/parser/KDocLinkParser.kt`** -> AI Confidence: **99.48%**
3112. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinLightParser.kt`** -> AI Confidence: **99.48%**
3113. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinParserDefinition.kt`** -> AI Confidence: **99.48%**
3114. **`compiler/psi/parser/src/org/jetbrains/kotlin/parsing/ParseUtils.kt`** -> AI Confidence: **99.48%**
3115. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/KotlinElementTypeProvider.kt`** -> AI Confidence: **99.48%**
3116. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/kdoc/psi/impl/KDocName.kt`** -> AI Confidence: **99.48%**
3117. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/kdoc/psi/impl/KDocTag.kt`** -> AI Confidence: **99.48%**
3118. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtClass.kt`** -> AI Confidence: **99.48%**
3119. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtClassBody.kt`** -> AI Confidence: **99.48%**
3120. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtClassOrObject.kt`** -> AI Confidence: **99.48%**
3121. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtCodeFragment.kt`** -> AI Confidence: **99.48%**
3122. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtCommonFile.kt`** -> AI Confidence: **99.48%**
3123. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtConstructor.kt`** -> AI Confidence: **99.48%**
3124. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtContextReceiver.kt`** -> AI Confidence: **99.48%**
3125. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtEnumEntrySuperclassReferenceExpression.kt`** -> AI Confidence: **99.48%**
3126. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtImportAlias.kt`** -> AI Confidence: **99.48%**
3127. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtNameReferenceExpression.kt`** -> AI Confidence: **99.48%**
3128. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtNamedFunction.kt`** -> AI Confidence: **99.48%**
3129. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtObjectDeclaration.kt`** -> AI Confidence: **99.48%**
3130. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtOperationReferenceExpression.kt`** -> AI Confidence: **99.48%**
3131. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtPrimaryConstructor.kt`** -> AI Confidence: **99.48%**
3132. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtPropertyAccessor.kt`** -> AI Confidence: **99.48%**
3133. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtPsiFactory.kt`** -> AI Confidence: **99.48%**
3134. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtQualifiedExpression.kt`** -> AI Confidence: **99.48%**
3135. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/KtTypeAlias.kt`** -> AI Confidence: **99.48%**
3136. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/TypeRefHelpers.kt`** -> AI Confidence: **99.48%**
3137. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/addRemoveModifier.kt`** -> AI Confidence: **99.48%**
3138. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/createByPattern.kt`** -> AI Confidence: **99.48%**
3139. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/psiUtil/ClassIdCalculator.kt`** -> AI Confidence: **99.48%**
3140. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/psiUtil/ktPsiUtil.kt`** -> AI Confidence: **99.48%**
3141. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/psiUtil/psiUtils.kt`** -> AI Confidence: **99.48%**
3142. **`compiler/psi/psi-api/src/org/jetbrains/kotlin/psi/utils/ConstantExpressionUtils.kt`** -> AI Confidence: **99.48%**
3143. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/BlockExpressionElementType.kt`** -> AI Confidence: **99.48%**
3144. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/ElementTypeUtils.kt`** -> AI Confidence: **99.48%**
3145. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/kdoc/psi/impl/KDocImpl.kt`** -> AI Confidence: **99.48%**
3146. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/impl/KotlinElementTypeProviderImpl.kt`** -> AI Confidence: **99.48%**
3147. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/psiUtil/KtStringTemplateExpressionManipulator.kt`** -> AI Confidence: **99.48%**
3148. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/psiUtil/StringTemplateExpressionManipulator.kt`** -> AI Confidence: **99.48%**
3149. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/StubUtils.kt`** -> AI Confidence: **99.48%**
3150. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtAnnotationEntryElementType.kt`** -> AI Confidence: **99.48%**
3151. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtAnnotationUseSiteTargetElementType.kt`** -> AI Confidence: **99.48%**
3152. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtBlockStringTemplateEntryElementType.kt`** -> AI Confidence: **99.48%**
3153. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtClassElementType.kt`** -> AI Confidence: **99.48%**
3154. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtClassLiteralExpressionElementType.kt`** -> AI Confidence: **99.48%**
3155. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtCollectionLiteralExpressionElementType.kt`** -> AI Confidence: **99.48%**
3156. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtConstantExpressionElementType.kt`** -> AI Confidence: **99.48%**
3157. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtContractEffectElementType.kt`** -> AI Confidence: **99.48%**
3158. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtEnumEntryElementType.kt`** -> AI Confidence: **99.48%**
3159. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtFileElementType.kt`** -> AI Confidence: **99.48%**
3160. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtFileStubBuilder.kt`** -> AI Confidence: **99.48%**
3161. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtFunctionTypeElementType.kt`** -> AI Confidence: **99.48%**
3162. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtImportAliasElementType.kt`** -> AI Confidence: **99.48%**
3163. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtPlaceHolderWithTextStubElementType.kt`** -> AI Confidence: **99.48%**
3164. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtPrimaryConstructorElementType.kt`** -> AI Confidence: **99.48%**
3165. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtPropertyAccessorElementType.kt`** -> AI Confidence: **99.48%**
3166. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtScriptElementType.kt`** -> AI Confidence: **99.48%**
3167. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtSecondaryConstructorElementType.kt`** -> AI Confidence: **99.48%**
3168. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtStringInterpolationPrefixElementType.kt`** -> AI Confidence: **99.48%**
3169. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtTypeAliasElementType.kt`** -> AI Confidence: **99.48%**
3170. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/elements/KtValueArgumentElementType.kt`** -> AI Confidence: **99.48%**
3171. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinConstantValue.kt`** -> AI Confidence: **99.48%**
3172. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinContractEffectStubImpl.kt`** -> AI Confidence: **99.48%**
3173. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinEnumEntryStubImpl.kt`** -> AI Confidence: **99.48%**
3174. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinFileStubImpl.kt`** -> AI Confidence: **99.48%**
3175. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinFileStubKindImpl.kt`** -> AI Confidence: **99.48%**
3176. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinFunctionStubImpl.kt`** -> AI Confidence: **99.48%**
3177. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinPropertyStubImpl.kt`** -> AI Confidence: **99.48%**
3178. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/KotlinStubBaseImpl.kt`** -> AI Confidence: **99.48%**
3179. **`compiler/psi/psi-impl/src/org/jetbrains/kotlin/psi/stubs/impl/Utils.kt`** -> AI Confidence: **99.48%**
3180. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/ConstraintSystemBuilder.kt`** -> AI Confidence: **99.48%**
3181. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/NewConstraintSystem.kt`** -> AI Confidence: **99.48%**
3182. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/ConstraintIncorporator.kt`** -> AI Confidence: **99.48%**
3183. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/ConstraintInjector.kt`** -> AI Confidence: **99.48%**
3184. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/ConstraintSystemCompletionContext.kt`** -> AI Confidence: **99.48%**
3185. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/InferenceLogger.kt`** -> AI Confidence: **99.48%**
3186. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/PostponedArgumentInputTypesResolver.kt`** -> AI Confidence: **99.48%**
3187. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/ResultTypeResolver.kt`** -> AI Confidence: **99.48%**
3188. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/TypeCheckerStateForConstraintSystem.kt`** -> AI Confidence: **99.48%**
3189. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/TypeVariableDependencyInformationProvider.kt`** -> AI Confidence: **99.48%**
3190. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/VariableFixationFinder.kt`** -> AI Confidence: **99.48%**
3191. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/model/ConstraintPositionAndErrors.kt`** -> AI Confidence: **99.48%**
3192. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/model/ConstraintStorage.kt`** -> AI Confidence: **99.48%**
3193. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/model/MutableConstraintStorage.kt`** -> AI Confidence: **99.48%**
3194. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/model/NewConstraintSystemImpl.kt`** -> AI Confidence: **99.48%**
3195. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/mpp/AbstractExpectActualAnnotationMatchChecker.kt`** -> AI Confidence: **99.48%**
3196. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/mpp/AbstractExpectActualChecker.kt`** -> AI Confidence: **99.48%**
3197. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/mpp/AbstractExpectActualMatcher.kt`** -> AI Confidence: **99.48%**
3198. **`compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/mpp/ExpectActualMatchingContext.kt`** -> AI Confidence: **99.48%**
3199. **`compiler/resolution.common/src/org/jetbrains/kotlin/types/AbstractTypeApproximator.kt`** -> AI Confidence: **99.48%**
3200. **`compiler/resolution/src/org/jetbrains/kotlin/contracts/interpretation/ContractInterpretationDispatcher.kt`** -> AI Confidence: **99.48%**
3201. **`compiler/resolution/src/org/jetbrains/kotlin/contracts/interpretation/EffectsInterpreters.kt`** -> AI Confidence: **99.48%**
3202. **`compiler/resolution/src/org/jetbrains/kotlin/contracts/model/functors/SubstitutingFunctor.kt`** -> AI Confidence: **99.48%**
3203. **`compiler/resolution/src/org/jetbrains/kotlin/contracts/model/structure/Values.kt`** -> AI Confidence: **99.48%**
3204. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/KotlinCallResolver.kt`** -> AI Confidence: **99.48%**
3205. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/AdditionalDiagnosticReporter.kt`** -> AI Confidence: **99.48%**
3206. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/ArgumentsToParametersMapper.kt`** -> AI Confidence: **99.48%**
3207. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/ArgumentsUtils.kt`** -> AI Confidence: **99.48%**
3208. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/CallableReferenceResolution.kt`** -> AI Confidence: **99.48%**
3209. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/ClassicTypeSystemContextForCS.kt`** -> AI Confidence: **99.48%**
3210. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/CompletionModeCalculator.kt`** -> AI Confidence: **99.48%**
3211. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/KotlinCallCompleter.kt`** -> AI Confidence: **99.48%**
3212. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/NewOverloadingConflictResolver.kt`** -> AI Confidence: **99.48%**
3213. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/PostponeArgumentsChecks.kt`** -> AI Confidence: **99.48%**
3214. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/PostponedArgumentsAnalyzer.kt`** -> AI Confidence: **99.48%**
3215. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/ResolutionParts.kt`** -> AI Confidence: **99.48%**
3216. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/SamTypeConversions.kt`** -> AI Confidence: **99.48%**
3217. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/SimpleArgumentsChecks.kt`** -> AI Confidence: **99.48%**
3218. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/UnitTypeConversions.kt`** -> AI Confidence: **99.48%**
3219. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/candidate/CallableReferenceResolutionCandidate.kt`** -> AI Confidence: **99.48%**
3220. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/components/candidate/ResolutionCandidate.kt`** -> AI Confidence: **99.48%**
3221. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/DescriptorRelatedInferenceUtils.kt`** -> AI Confidence: **99.48%**
3222. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/components/ClassicConstraintSystemUtilContext.kt`** -> AI Confidence: **99.48%**
3223. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/components/KotlinConstraintSystemCompleter.kt`** -> AI Confidence: **99.48%**
3224. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/components/NewTypeSubstitutor.kt`** -> AI Confidence: **99.48%**
3225. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/components/SimpleConstraintSystemImpl.kt`** -> AI Confidence: **99.48%**
3226. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/inference/model/TypeVariable.kt`** -> AI Confidence: **99.48%**
3227. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/CallableReferencesCandidateFactory.kt`** -> AI Confidence: **99.48%**
3228. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/KotlinCallArguments.kt`** -> AI Confidence: **99.48%**
3229. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/KotlinCallDiagnostics.kt`** -> AI Confidence: **99.48%**
3230. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/ResolutionAtoms.kt`** -> AI Confidence: **99.48%**
3231. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/ResolvedCallAtoms.kt`** -> AI Confidence: **99.48%**
3232. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/SimpleCandidateFactory.kt`** -> AI Confidence: **99.48%**
3233. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/results/FlatSignatureUtils.kt`** -> AI Confidence: **99.48%**
3234. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/results/OverloadingConflictResolver.kt`** -> AI Confidence: **99.48%**
3235. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tasks/synthesizedInvokes.kt`** -> AI Confidence: **99.48%**
3236. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/ErrorCandidateFactory.kt`** -> AI Confidence: **99.48%**
3237. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/ImplicitScopeTower.kt`** -> AI Confidence: **99.48%**
3238. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/InvokeProcessors.kt`** -> AI Confidence: **99.48%**
3239. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/ScopeTowerProcessors.kt`** -> AI Confidence: **99.48%**
3240. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/TowerLevels.kt`** -> AI Confidence: **99.48%**
3241. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/tower/TowerResolver.kt`** -> AI Confidence: **99.48%**
3242. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/util/FakeCallableDescriptorForObject.kt`** -> AI Confidence: **99.48%**
3243. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/util/functionTypeResolveUtils.kt`** -> AI Confidence: **99.48%**
3244. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/util/isFromStdlibJre7Or8.kt`** -> AI Confidence: **99.48%**
3245. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/multiplatform/ClassicExpectActualMatchingContext.kt`** -> AI Confidence: **99.48%**
3246. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/multiplatform/K1AbstractExpectActualAnnotationMatchChecker.kt`** -> AI Confidence: **99.48%**
3247. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/multiplatform/K1AbstractExpectActualCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
3248. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/multiplatform/K1ExpectActualMatchingContext.kt`** -> AI Confidence: **99.48%**
3249. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/scopes/LexicalChainedScope.kt`** -> AI Confidence: **99.48%**
3250. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/scopes/LexicalScopeStorage.kt`** -> AI Confidence: **99.48%**
3251. **`compiler/resolution/src/org/jetbrains/kotlin/resolve/scopes/utils/ScopeUtils.kt`** -> AI Confidence: **99.48%**
3252. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/AnnotationSerializer.kt`** -> AI Confidence: **99.48%**
3253. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/ContractSerializer.kt`** -> AI Confidence: **99.48%**
3254. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/DescriptorAwareStringTable.kt`** -> AI Confidence: **99.48%**
3255. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/DescriptorSerializer.kt`** -> AI Confidence: **99.48%**
3256. **`compiler/serialization/src/org/jetbrains/kotlin/serialization/SerializerExtensionBase.kt`** -> AI Confidence: **99.48%**
3257. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jspecify/strictMode/interconnectedGenerics.kt`** -> AI Confidence: **99.48%**
3258. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/defaultAnnotationAppliedToType.kt`** -> AI Confidence: **99.48%**
3259. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/defaultAnnotationAppliedToTypeForCompiledJava.kt`** -> AI Confidence: **99.48%**
3260. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/overrideWithTypeUseInClasspath.fir.kt`** -> AI Confidence: **99.48%**
3261. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/overrideWithTypeUseInClasspath.kt`** -> AI Confidence: **99.48%**
3262. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/overrideWithTypeUseInClasspathWithArray.fir.kt`** -> AI Confidence: **99.48%**
3263. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/overrideWithTypeUseInClasspathWithArray.kt`** -> AI Confidence: **99.48%**
3264. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/springNullableWithTypeUse.kt`** -> AI Confidence: **99.48%**
3265. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/typeArguments.fir.kt`** -> AI Confidence: **99.48%**
3266. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/typeArguments.kt`** -> AI Confidence: **99.48%**
3267. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/jsr305/typeUseVsMethodConflict.kt`** -> AI Confidence: **99.48%**
3268. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/overrideOfMethodWithParametricNullness.kt`** -> AI Confidence: **99.48%**
3269. **`compiler/testData/diagnostics/foreignAnnotationsTests/java8Tests/warningModeForHeadType.kt`** -> AI Confidence: **99.48%**
3270. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/irrelevantQualifierNicknames.kt`** -> AI Confidence: **99.48%**
3271. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/dontIgnoreAnnotationsWithoutTarget.kt`** -> AI Confidence: **99.48%**
3272. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/elvis.kt`** -> AI Confidence: **99.48%**
3273. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/localInference.fir.kt`** -> AI Confidence: **99.48%**
3274. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/localInference.kt`** -> AI Confidence: **99.48%**
3275. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/safeCalls.kt`** -> AI Confidence: **99.48%**
3276. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/equalsOnNonNull.fir.kt`** -> AI Confidence: **99.48%**
3277. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/equalsOnNonNull.kt`** -> AI Confidence: **99.48%**
3278. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/fieldsAreNullable.kt`** -> AI Confidence: **99.48%**
3279. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/nullabilityFromOverridden.fir.kt`** -> AI Confidence: **99.48%**
3280. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/nullabilityFromOverridden.kt`** -> AI Confidence: **99.48%**
3281. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/overridingDefaultQualifier.fir.kt`** -> AI Confidence: **99.48%**
3282. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/overridingDefaultQualifier.kt`** -> AI Confidence: **99.48%**
3283. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/springNullable.fir.kt`** -> AI Confidence: **99.48%**
3284. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/springNullable.kt`** -> AI Confidence: **99.48%**
3285. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/springNullablePackage.fir.kt`** -> AI Confidence: **99.48%**
3286. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/nullabilityWarnings/typeQualifierDefault/springNullablePackage.kt`** -> AI Confidence: **99.48%**
3287. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/fieldsAreNullable.kt`** -> AI Confidence: **99.48%**
3288. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/forceFlexibility.kt`** -> AI Confidence: **99.48%**
3289. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/forceFlexibleOverOverrides.kt`** -> AI Confidence: **99.48%**
3290. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/nullabilityFromOverridden.kt`** -> AI Confidence: **99.48%**
3291. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/overridingDefaultQualifier.kt`** -> AI Confidence: **99.48%**
3292. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/springNullable.kt`** -> AI Confidence: **99.48%**
3293. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305/typeQualifierDefault/springNullablePackage.kt`** -> AI Confidence: **99.48%**
3294. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305NullabilityWarnings/migration/customMigration.fir.kt`** -> AI Confidence: **99.48%**
3295. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/jsr305NullabilityWarnings/migration/customMigration.kt`** -> AI Confidence: **99.48%**
3296. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/typeQualifierDefault/defaultAndNicknameMigrationPolicy.fir.kt`** -> AI Confidence: **99.48%**
3297. **`compiler/testData/diagnostics/foreignAnnotationsTests/tests/typeQualifierDefault/defaultAndNicknameMigrationPolicy.kt`** -> AI Confidence: **99.48%**
3298. **`compiler/testData/diagnostics/tests/imports/ImportFromCompanionObject.fir.kt`** -> AI Confidence: **99.48%**
3299. **`compiler/testData/diagnostics/tests/imports/ImportFromCompanionObject.kt`** -> AI Confidence: **99.48%**
3300. **`compiler/testData/diagnostics/tests/imports/ImportFromObject.fir.kt`** -> AI Confidence: **99.48%**
3301. **`compiler/testData/diagnostics/tests/imports/ImportFromObject.kt`** -> AI Confidence: **99.48%**
3302. **`compiler/testData/diagnostics/tests/imports/Imports.fir.kt`** -> AI Confidence: **99.48%**
3303. **`compiler/testData/diagnostics/tests/imports/Imports.kt`** -> AI Confidence: **99.48%**
3304. **`compiler/testData/diagnostics/tests/imports/twoImportLists.fir.kt`** -> AI Confidence: **99.48%**
3305. **`compiler/testData/diagnostics/tests/imports/twoImportLists.kt`** -> AI Confidence: **99.48%**
3306. **`compiler/testData/diagnostics/tests/javac/Lambda.fir.kt`** -> AI Confidence: **99.48%**
3307. **`compiler/testData/diagnostics/tests/javac/Lambda.kt`** -> AI Confidence: **99.48%**
3308. **`compiler/testData/diagnostics/tests/scopes/inheritance/statics/staticFunAndPropertyImport.kt`** -> AI Confidence: **99.48%**
3309. **`compiler/testData/ir/irText/expressions/useImportedMember.kt`** -> AI Confidence: **99.48%**
3310. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/FirErrorsDefaultMessagesHelper.kt`** -> AI Confidence: **99.48%**
3311. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/SteppingTestUtils.kt`** -> AI Confidence: **99.48%**
3312. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/inferencelogs/FirInferenceLogsDumper.kt`** -> AI Confidence: **99.48%**
3313. **`compiler/tests-common-new/testFixtures/org/jetbrains/kotlin/test/utils/inferencelogs/MarkdownInferenceLogsDumper.kt`** -> AI Confidence: **99.48%**
3314. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/asJava/PsiClassRenderer.kt`** -> AI Confidence: **99.48%**
3315. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/cfg/pseudocodeUtils.kt`** -> AI Confidence: **99.48%**
3316. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/checkers/CompilerTestLanguageVersionSettings.kt`** -> AI Confidence: **99.48%**
3317. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/checkers/KotlinMultiFileTestWithJava.kt`** -> AI Confidence: **99.48%**
3318. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/fir/FirResolveBench.kt`** -> AI Confidence: **99.48%**
3319. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/resolve/calls/AbstractResolvedConstructorDelegationCallsTests.kt`** -> AI Confidence: **99.48%**
3320. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/resolve/lazy/lazyResolveTestUtils.kt`** -> AI Confidence: **99.48%**
3321. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/serialization/builtins/BuiltinsTestUtils.kt`** -> AI Confidence: **99.48%**
3322. **`compiler/tests-common/testFixtures/org/jetbrains/kotlin/tests/di/injection.kt`** -> AI Confidence: **99.48%**
3323. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/fir/FirAnalyzerFacade.kt`** -> AI Confidence: **99.48%**
3324. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/fir/FirTestSessionFactoryHelper.kt`** -> AI Confidence: **99.48%**
3325. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/fir/session/FirSessionFactoryHelper.kt`** -> AI Confidence: **99.48%**
3326. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/native/FakeTopDownAnalyzerFacadeForNative.kt`** -> AI Confidence: **99.48%**
3327. **`compiler/tests-compiler-utils/testFixtures/org/jetbrains/kotlin/resolve/lazy/JvmResolveUtil.kt`** -> AI Confidence: **99.48%**
3328. **`compiler/tests-integration/tests/org/jetbrains/kotlin/jvm/compiler/AllNullabilityAnnotationsAreSetUp.kt`** -> AI Confidence: **99.48%**
3329. **`compiler/tests-mutes/mutes-junit4/src/org/jetbrains/kotlin/test/MuteWithDatabaseWatcher.kt`** -> AI Confidence: **99.48%**
3330. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/Common.kt`** -> AI Confidence: **99.48%**
3331. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/SectionsJsonMapGenerator.kt`** -> AI Confidence: **99.48%**
3332. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/TestsJsonMapGenerator.kt`** -> AI Confidence: **99.48%**
3333. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/models/AbstractSpecTest.kt`** -> AI Confidence: **99.48%**
3334. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/models/LinkedSpecTest.kt`** -> AI Confidence: **99.48%**
3335. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/models/NotLinkedSpecTest.kt`** -> AI Confidence: **99.48%**
3336. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/parsers/CommonParser.kt`** -> AI Confidence: **99.48%**
3337. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/parsers/Patterns.kt`** -> AI Confidence: **99.48%**
3338. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/parsers/TestCasesParser.kt`** -> AI Confidence: **99.48%**
3339. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/parsers/TestInfoParser.kt`** -> AI Confidence: **99.48%**
3340. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/spec/HtmlSpecLoader.kt`** -> AI Confidence: **99.48%**
3341. **`compiler/tests-spec/testFixtures/org/jetbrains/kotlin/spec/utils/validators/DiagnosticTestTypeValidator.kt`** -> AI Confidence: **99.48%**
3342. **`compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt`** -> AI Confidence: **99.48%**
3343. **`compiler/util-io/src/org/jetbrains/kotlin/konan/file/ZipUtil.kt`** -> AI Confidence: **99.48%**
3344. **`compiler/util-klib-abi/src/org/jetbrains/kotlin/library/abi/impl/LibraryAbiReaderImpl.kt`** -> AI Confidence: **99.48%**
3345. **`compiler/util-klib-abi/src/org/jetbrains/kotlin/library/abi/parser/KlibParsingCursorExtensions.kt`** -> AI Confidence: **99.48%**
3346. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/KlibDeserializedContainerSource.kt`** -> AI Confidence: **99.48%**
3347. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/KlibMetadataClassDataFinder.kt`** -> AI Confidence: **99.48%**
3348. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/KlibMetadataModuleDescriptorFactory.kt`** -> AI Confidence: **99.48%**
3349. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/KlibMetadataPackageFragment.kt`** -> AI Confidence: **99.48%**
3350. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/impl/KlibMetadataDeserializedPackageFragmentsFactoryImpl.kt`** -> AI Confidence: **99.48%**
3351. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/impl/KlibMetadataModuleDescriptorFactoryImpl.kt`** -> AI Confidence: **99.48%**
3352. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/impl/KlibModuleDescriptorFactoryImpl.kt`** -> AI Confidence: **99.48%**
3353. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/impl/KlibResolvedModuleDescriptorsFactoryImpl.kt`** -> AI Confidence: **99.48%**
3354. **`compiler/util-klib-metadata/src/org/jetbrains/kotlin/library/metadata/resolver/impl/KotlinLibraryResolverImpl.kt`** -> AI Confidence: **99.48%**
3355. **`compiler/util-klib/src/org/jetbrains/kotlin/library/KlibLayoutReader.kt`** -> AI Confidence: **99.48%**
3356. **`compiler/util-klib/src/org/jetbrains/kotlin/library/KlibSizeInfo.kt`** -> AI Confidence: **99.48%**
3357. **`compiler/util-klib/src/org/jetbrains/kotlin/library/KotlinLibrary.kt`** -> AI Confidence: **99.48%**
3358. **`compiler/util-klib/src/org/jetbrains/kotlin/library/SearchPathResolver.kt`** -> AI Confidence: **99.48%**
3359. **`compiler/util-klib/src/org/jetbrains/kotlin/library/components/KlibIrComponent.kt`** -> AI Confidence: **99.48%**
3360. **`compiler/util-klib/src/org/jetbrains/kotlin/library/components/KlibMetadataComponent.kt`** -> AI Confidence: **99.48%**
3361. **`compiler/util-klib/src/org/jetbrains/kotlin/library/impl/KlibImpl.kt`** -> AI Confidence: **99.48%**
3362. **`compiler/util-klib/src/org/jetbrains/kotlin/library/impl/KlibManifestComponentWriterImpl.kt`** -> AI Confidence: **99.48%**
3363. **`compiler/util-klib/src/org/jetbrains/kotlin/library/impl/lowLevelWriters.kt`** -> AI Confidence: **99.48%**
3364. **`compiler/util-klib/src/org/jetbrains/kotlin/library/loader/KlibLoader.kt`** -> AI Confidence: **99.48%**
3365. **`compiler/util-klib/src/org/jetbrains/kotlin/library/loader/KlibLoaderResult.kt`** -> AI Confidence: **99.48%**
3366. **`compiler/util-klib/src/org/jetbrains/kotlin/library/loader/KlibPlatformChecker.kt`** -> AI Confidence: **99.48%**
3367. **`compiler/util-klib/src/org/jetbrains/kotlin/library/writer/KlibWriter.kt`** -> AI Confidence: **99.48%**
3368. **`compiler/util/src/org/jetbrains/kotlin/utils/KotlinExceptionWithAttachments.kt`** -> AI Confidence: **99.48%**
3369. **`compiler/util/src/org/jetbrains/kotlin/utils/LibraryUtils.kt`** -> AI Confidence: **99.48%**
3370. **`compiler/util/src/org/jetbrains/kotlin/utils/kapt/MemoryLeakDetector.kt`** -> AI Confidence: **99.48%**
3371. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/builtins/jvm/JavaToKotlinClassMap.kt`** -> AI Confidence: **99.48%**
3372. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/load/java/AbstractAnnotationTypeQualifierResolver.kt`** -> AI Confidence: **99.48%**
3373. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/load/java/typeEnhancement/AbstractSignatureParts.kt`** -> AI Confidence: **99.48%**
3374. **`core/compiler.common.jvm/src/org/jetbrains/kotlin/load/kotlin/typeSignatureMapping.kt`** -> AI Confidence: **99.48%**
3375. **`core/compiler.common/src/org/jetbrains/kotlin/builtins/StandardNames.kt`** -> AI Confidence: **99.48%**
3376. **`core/compiler.common/src/org/jetbrains/kotlin/stats/MarkdownReportRenderer.kt`** -> AI Confidence: **99.48%**
3377. **`core/compiler.common/src/org/jetbrains/kotlin/stats/StatsCalculator.kt`** -> AI Confidence: **99.48%**
3378. **`core/compiler.common/src/org/jetbrains/kotlin/types/AbstractTypeChecker.kt`** -> AI Confidence: **99.48%**
3379. **`core/compiler.common/src/org/jetbrains/kotlin/types/model/TypeSystemContext.kt`** -> AI Confidence: **99.48%**
3380. **`core/compiler.common/src/org/jetbrains/kotlin/util/PerformanceManager.kt`** -> AI Confidence: **99.48%**
3381. **`core/descriptors.jvm/src/org/jetbrains/kotlin/builtins/jvm/JavaToKotlinClassMapper.kt`** -> AI Confidence: **99.48%**
3382. **`core/descriptors.jvm/src/org/jetbrains/kotlin/builtins/jvm/JvmBuiltInClassDescriptorFactory.kt`** -> AI Confidence: **99.48%**
3383. **`core/descriptors.jvm/src/org/jetbrains/kotlin/builtins/jvm/JvmBuiltIns.kt`** -> AI Confidence: **99.48%**
3384. **`core/descriptors.jvm/src/org/jetbrains/kotlin/builtins/jvm/JvmBuiltInsCustomizer.kt`** -> AI Confidence: **99.48%**
3385. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/ErasedOverridabilityCondition.kt`** -> AI Confidence: **99.48%**
3386. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/JavaIncompatibilityRulesOverridabilityCondition.kt`** -> AI Confidence: **99.48%**
3387. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/components/JavaAnnotationMapper.kt`** -> AI Confidence: **99.48%**
3388. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/descriptors/util.kt`** -> AI Confidence: **99.48%**
3389. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/LazyJavaPackageFragmentProvider.kt`** -> AI Confidence: **99.48%**
3390. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/context.kt`** -> AI Confidence: **99.48%**
3391. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/JvmPackageScope.kt`** -> AI Confidence: **99.48%**
3392. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaAnnotationDescriptor.kt`** -> AI Confidence: **99.48%**
3393. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaClassDescriptor.kt`** -> AI Confidence: **99.48%**
3394. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaClassMemberScope.kt`** -> AI Confidence: **99.48%**
3395. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaPackageFragment.kt`** -> AI Confidence: **99.48%**
3396. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaPackageScope.kt`** -> AI Confidence: **99.48%**
3397. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaScope.kt`** -> AI Confidence: **99.48%**
3398. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaStaticClassScope.kt`** -> AI Confidence: **99.48%**
3399. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/LazyJavaTypeParameterDescriptor.kt`** -> AI Confidence: **99.48%**
3400. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/descriptors/SyntheticJavaClassDescriptor.kt`** -> AI Confidence: **99.48%**
3401. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/types/JavaTypeResolver.kt`** -> AI Confidence: **99.48%**
3402. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/types/RawSubstitution.kt`** -> AI Confidence: **99.48%**
3403. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/lazy/types/RawType.kt`** -> AI Confidence: **99.48%**
3404. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/specialBuiltinMembers.kt`** -> AI Confidence: **99.48%**
3405. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/typeEnhancement/signatureEnhancement.kt`** -> AI Confidence: **99.48%**
3406. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/typeEnhancement/typeEnhancement.kt`** -> AI Confidence: **99.48%**
3407. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/java/utils.kt`** -> AI Confidence: **99.48%**
3408. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/AbstractBinaryClassAnnotationAndConstantLoader.kt`** -> AI Confidence: **99.48%**
3409. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/BinaryClassAnnotationAndConstantLoaderImpl.kt`** -> AI Confidence: **99.48%**
3410. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/DeserializationComponentsForJava.kt`** -> AI Confidence: **99.48%**
3411. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/DeserializedDescriptorResolver.kt`** -> AI Confidence: **99.48%**
3412. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/JavaFlexibleTypeDeserializer.kt`** -> AI Confidence: **99.48%**
3413. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/descriptorBasedTypeSignatureMapping.kt`** -> AI Confidence: **99.48%**
3414. **`core/descriptors.jvm/src/org/jetbrains/kotlin/load/kotlin/methodSignatureMapping.kt`** -> AI Confidence: **99.48%**
3415. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/components/PackagePartScopeCache.kt`** -> AI Confidence: **99.48%**
3416. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/components/ReflectJavaClassFinder.kt`** -> AI Confidence: **99.48%**
3417. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/components/ReflectKotlinClass.kt`** -> AI Confidence: **99.48%**
3418. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/components/ReflectKotlinClassFinder.kt`** -> AI Confidence: **99.48%**
3419. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/structure/ReflectJavaClass.kt`** -> AI Confidence: **99.48%**
3420. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/structure/ReflectJavaClassifierType.kt`** -> AI Confidence: **99.48%**
3421. **`core/descriptors.runtime/src/org/jetbrains/kotlin/descriptors/runtime/structure/ReflectJavaMember.kt`** -> AI Confidence: **99.48%**
3422. **`core/descriptors/src/org/jetbrains/kotlin/builtins/BuiltInsLoader.kt`** -> AI Confidence: **99.48%**
3423. **`core/descriptors/src/org/jetbrains/kotlin/builtins/ReflectionTypes.kt`** -> AI Confidence: **99.48%**
3424. **`core/descriptors/src/org/jetbrains/kotlin/builtins/functionTypes.kt`** -> AI Confidence: **99.48%**
3425. **`core/descriptors/src/org/jetbrains/kotlin/builtins/functions/BuiltInFictitiousFunctionClassFactory.kt`** -> AI Confidence: **99.48%**
3426. **`core/descriptors/src/org/jetbrains/kotlin/builtins/functions/FunctionClassDescriptor.kt`** -> AI Confidence: **99.48%**
3427. **`core/descriptors/src/org/jetbrains/kotlin/builtins/functions/FunctionInterfaceFactory.kt`** -> AI Confidence: **99.48%**
3428. **`core/descriptors/src/org/jetbrains/kotlin/builtins/functions/FunctionInvokeDescriptor.kt`** -> AI Confidence: **99.48%**
3429. **`core/descriptors/src/org/jetbrains/kotlin/builtins/suspendFunctionTypes.kt`** -> AI Confidence: **99.48%**
3430. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/NotFoundClasses.kt`** -> AI Confidence: **99.48%**
3431. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/annotations/annotationUtil.kt`** -> AI Confidence: **99.48%**
3432. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/descriptorUtil.kt`** -> AI Confidence: **99.48%**
3433. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/AbstractTypeAliasDescriptor.kt`** -> AI Confidence: **99.48%**
3434. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/LazyPackageViewDescriptorImpl.kt`** -> AI Confidence: **99.48%**
3435. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/ModuleAwareClassDescriptor.kt`** -> AI Confidence: **99.48%**
3436. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/ModuleDescriptorImpl.kt`** -> AI Confidence: **99.48%**
3437. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/PackageFragmentDescriptorImpl.kt`** -> AI Confidence: **99.48%**
3438. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/SubpackagesScope.kt`** -> AI Confidence: **99.48%**
3439. **`core/descriptors/src/org/jetbrains/kotlin/descriptors/impl/TypeAliasConstructorDescriptor.kt`** -> AI Confidence: **99.48%**
3440. **`core/descriptors/src/org/jetbrains/kotlin/incremental/utils.kt`** -> AI Confidence: **99.48%**
3441. **`core/descriptors/src/org/jetbrains/kotlin/renderer/DescriptorRenderer.kt`** -> AI Confidence: **99.48%**
3442. **`core/descriptors/src/org/jetbrains/kotlin/renderer/DescriptorRendererImpl.kt`** -> AI Confidence: **99.48%**
3443. **`core/descriptors/src/org/jetbrains/kotlin/renderer/DescriptorRendererOptionsImpl.kt`** -> AI Confidence: **99.48%**
3444. **`core/descriptors/src/org/jetbrains/kotlin/resolve/DescriptorUtils.kt`** -> AI Confidence: **99.48%**
3445. **`core/descriptors/src/org/jetbrains/kotlin/resolve/SealedClassInheritorsProvider.kt`** -> AI Confidence: **99.48%**
3446. **`core/descriptors/src/org/jetbrains/kotlin/resolve/annotationsForResolveUtils.kt`** -> AI Confidence: **99.48%**
3447. **`core/descriptors/src/org/jetbrains/kotlin/resolve/calls/inference/CapturedTypeConstructor.kt`** -> AI Confidence: **99.48%**
3448. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/CompileTimeConstant.kt`** -> AI Confidence: **99.48%**
3449. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/IntegerLiteralTypeConstructor.kt`** -> AI Confidence: **99.48%**
3450. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/IntegerValueTypeConstructor.kt`** -> AI Confidence: **99.48%**
3451. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/PrimitiveTypeUtil.kt`** -> AI Confidence: **99.48%**
3452. **`core/descriptors/src/org/jetbrains/kotlin/resolve/constants/constantValues.kt`** -> AI Confidence: **99.48%**
3453. **`core/descriptors/src/org/jetbrains/kotlin/resolve/inlineClassesUtils.kt`** -> AI Confidence: **99.48%**
3454. **`core/descriptors/src/org/jetbrains/kotlin/resolve/sam/SamConversionResolverImpl.kt`** -> AI Confidence: **99.48%**
3455. **`core/descriptors/src/org/jetbrains/kotlin/resolve/sam/samConstructorUtils.kt`** -> AI Confidence: **99.48%**
3456. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/AbstractScopeAdapter.kt`** -> AI Confidence: **99.48%**
3457. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/ChainedMemberScope.kt`** -> AI Confidence: **99.48%**
3458. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/GivenFunctionsMemberScope.kt`** -> AI Confidence: **99.48%**
3459. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/InnerClassesScopeWrapper.kt`** -> AI Confidence: **99.48%**
3460. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/MemberScope.kt`** -> AI Confidence: **99.48%**
3461. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/StaticScopeForKotlinEnum.kt`** -> AI Confidence: **99.48%**
3462. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/SubstitutingScope.kt`** -> AI Confidence: **99.48%**
3463. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/TypeIntersectionScope.kt`** -> AI Confidence: **99.48%**
3464. **`core/descriptors/src/org/jetbrains/kotlin/resolve/scopes/synthetic/FunInterfaceConstructorsSyntheticScope.kt`** -> AI Confidence: **99.48%**
3465. **`core/descriptors/src/org/jetbrains/kotlin/types/CapturedTypeApproximation.kt`** -> AI Confidence: **99.48%**
3466. **`core/descriptors/src/org/jetbrains/kotlin/types/IntersectionTypeConstructor.kt`** -> AI Confidence: **99.48%**
3467. **`core/descriptors/src/org/jetbrains/kotlin/types/KotlinType.kt`** -> AI Confidence: **99.48%**
3468. **`core/descriptors/src/org/jetbrains/kotlin/types/KotlinTypeFactory.kt`** -> AI Confidence: **99.48%**
3469. **`core/descriptors/src/org/jetbrains/kotlin/types/KotlinTypeRefinerImpl.kt`** -> AI Confidence: **99.48%**
3470. **`core/descriptors/src/org/jetbrains/kotlin/types/SpecialTypes.kt`** -> AI Confidence: **99.48%**
3471. **`core/descriptors/src/org/jetbrains/kotlin/types/StubTypes.kt`** -> AI Confidence: **99.48%**
3472. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeAliasExpander.kt`** -> AI Confidence: **99.48%**
3473. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeAttributes.kt`** -> AI Confidence: **99.48%**
3474. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeParameterUpperBoundEraser.kt`** -> AI Confidence: **99.48%**
3475. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeSubstitution.kt`** -> AI Confidence: **99.48%**
3476. **`core/descriptors/src/org/jetbrains/kotlin/types/TypeUtils.kt`** -> AI Confidence: **99.48%**
3477. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/ClassicTypeSystemContext.kt`** -> AI Confidence: **99.48%**
3478. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/KotlinTypePreparator.kt`** -> AI Confidence: **99.48%**
3479. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/KotlinTypeRefiner.kt`** -> AI Confidence: **99.48%**
3480. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/NewCapturedType.kt`** -> AI Confidence: **99.48%**
3481. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/NewKotlinTypeChecker.kt`** -> AI Confidence: **99.48%**
3482. **`core/descriptors/src/org/jetbrains/kotlin/types/checker/utils.kt`** -> AI Confidence: **99.48%**
3483. **`core/descriptors/src/org/jetbrains/kotlin/types/error/ErrorUtils.kt`** -> AI Confidence: **99.48%**
3484. **`core/descriptors/src/org/jetbrains/kotlin/types/flexibleTypes.kt`** -> AI Confidence: **99.48%**
3485. **`core/descriptors/src/org/jetbrains/kotlin/util/modifierChecks.kt`** -> AI Confidence: **99.48%**
3486. **`core/deserialization.common.jvm/src/org/jetbrains/kotlin/load/kotlin/AbstractBinaryClassAnnotationLoader.kt`** -> AI Confidence: **99.48%**
3487. **`core/deserialization.common.jvm/src/org/jetbrains/kotlin/load/kotlin/JvmPackagePartSource.kt`** -> AI Confidence: **99.48%**
3488. **`core/deserialization.common/src/org/jetbrains/kotlin/serialization/deserialization/MetadataUtil.kt`** -> AI Confidence: **99.48%**
3489. **`core/deserialization.common/src/org/jetbrains/kotlin/serialization/deserialization/ProtoContainer.kt`** -> AI Confidence: **99.48%**
3490. **`core/deserialization.common/src/org/jetbrains/kotlin/serialization/deserialization/ValueClassUtil.kt`** -> AI Confidence: **99.48%**
3491. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/AbstractDeserializedPackageFragmentProvider.kt`** -> AI Confidence: **99.48%**
3492. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/AnnotationAndConstantLoaderImpl.kt`** -> AI Confidence: **99.48%**
3493. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/AnnotationDeserializer.kt`** -> AI Confidence: **99.48%**
3494. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/ClassDeserializer.kt`** -> AI Confidence: **99.48%**
3495. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/DeserializedPackageFragmentImpl.kt`** -> AI Confidence: **99.48%**
3496. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/MemberDeserializer.kt`** -> AI Confidence: **99.48%**
3497. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/MetadataPackageFragmentProvider.kt`** -> AI Confidence: **99.48%**
3498. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/TypeDeserializer.kt`** -> AI Confidence: **99.48%**
3499. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/builtins/BuiltInsLoaderImpl.kt`** -> AI Confidence: **99.48%**
3500. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/builtins/BuiltInsPackageFragmentImpl.kt`** -> AI Confidence: **99.48%**
3501. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/context.kt`** -> AI Confidence: **99.48%**
3502. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedClassDescriptor.kt`** -> AI Confidence: **99.48%**
3503. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedMemberDescriptor.kt`** -> AI Confidence: **99.48%**
3504. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedMemberScope.kt`** -> AI Confidence: **99.48%**
3505. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedPackageMemberScope.kt`** -> AI Confidence: **99.48%**
3506. **`core/deserialization/src/org/jetbrains/kotlin/serialization/deserialization/descriptors/DeserializedTypeParameterDescriptor.kt`** -> AI Confidence: **99.48%**
3507. **`core/metadata.jvm/src/org/jetbrains/kotlin/metadata/jvm/deserialization/JvmProtoBufUtil.kt`** -> AI Confidence: **99.48%**
3508. **`core/metadata.jvm/src/org/jetbrains/kotlin/metadata/jvm/deserialization/ModuleMapping.kt`** -> AI Confidence: **99.48%**
3509. **`core/metadata.jvm/src/org/jetbrains/kotlin/metadata/jvm/serialization/JvmStringTable.kt`** -> AI Confidence: **99.48%**
3510. **`core/reflection.jvm/src/kotlin/reflect/full/K1Implementation.kt`** -> AI Confidence: **99.48%**
3511. **`core/reflection.jvm/src/kotlin/reflect/full/KCallables.kt`** -> AI Confidence: **99.48%**
3512. **`core/reflection.jvm/src/kotlin/reflect/full/KClasses.kt`** -> AI Confidence: **99.48%**
3513. **`core/reflection.jvm/src/kotlin/reflect/full/KClassifiers.kt`** -> AI Confidence: **99.48%**
3514. **`core/reflection.jvm/src/kotlin/reflect/full/KTypes.kt`** -> AI Confidence: **99.48%**
3515. **`core/reflection.jvm/src/kotlin/reflect/jvm/KTypesJvm.kt`** -> AI Confidence: **99.48%**
3516. **`core/reflection.jvm/src/kotlin/reflect/jvm/ReflectJvmMapping.kt`** -> AI Confidence: **99.48%**
3517. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ConvertFromJava.kt`** -> AI Confidence: **99.48%**
3518. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ConvertFromMetadata.kt`** -> AI Confidence: **99.48%**
3519. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/DescriptorKCallable.kt`** -> AI Confidence: **99.48%**
3520. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/DescriptorKFunction.kt`** -> AI Confidence: **99.48%**
3521. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/DescriptorKParameter.kt`** -> AI Confidence: **99.48%**
3522. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/DescriptorKProperty.kt`** -> AI Confidence: **99.48%**
3523. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/JavaAnnotationConstructor.kt`** -> AI Confidence: **99.48%**
3524. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/JavaKConstructor.kt`** -> AI Confidence: **99.48%**
3525. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/JavaKFunction.kt`** -> AI Confidence: **99.48%**
3526. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/JavaKNamedFunction.kt`** -> AI Confidence: **99.48%**
3527. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KClassImpl.kt`** -> AI Confidence: **99.48%**
3528. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KDeclarationContainerImpl.kt`** -> AI Confidence: **99.48%**
3529. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KPackageImpl.kt`** -> AI Confidence: **99.48%**
3530. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KTypeParameterImpl.kt`** -> AI Confidence: **99.48%**
3531. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KotlinKConstructor.kt`** -> AI Confidence: **99.48%**
3532. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/KotlinKFunction.kt`** -> AI Confidence: **99.48%**
3533. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectKCallable.kt`** -> AI Confidence: **99.48%**
3534. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectKFunction.kt`** -> AI Confidence: **99.48%**
3535. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectKParameter.kt`** -> AI Confidence: **99.48%**
3536. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectKProperty.kt`** -> AI Confidence: **99.48%**
3537. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/ReflectionObjectRenderer.kt`** -> AI Confidence: **99.48%**
3538. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/RuntimeTypeMapper.kt`** -> AI Confidence: **99.48%**
3539. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/calls/CallerImpl.kt`** -> AI Confidence: **99.48%**
3540. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/calls/ValueClassAwareCaller.kt`** -> AI Confidence: **99.48%**
3541. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/fakeOverrides.kt`** -> AI Confidence: **99.48%**
3542. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/AbstractKType.kt`** -> AI Confidence: **99.48%**
3543. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/DescriptorKType.kt`** -> AI Confidence: **99.48%**
3544. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/KTypeSubstitutor.kt`** -> AI Confidence: **99.48%**
3545. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/MutableCollectionKClass.kt`** -> AI Confidence: **99.48%**
3546. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/ReflectTypeSystemContext.kt`** -> AI Confidence: **99.48%**
3547. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/types/typeOfImpl.kt`** -> AI Confidence: **99.48%**
3548. **`core/reflection.jvm/src/kotlin/reflect/jvm/internal/util.kt`** -> AI Confidence: **99.48%**
3549. **`core/reflection.jvm/src/kotlin/reflect/jvm/reflectLambda.kt`** -> AI Confidence: **99.48%**
3550. **`core/util.runtime/src/org/jetbrains/kotlin/utils/addToStdlib.kt`** -> AI Confidence: **99.48%**
3551. **`dependencies/kotlin-build-gradle-plugin/src/BuildPropertiesService.kt`** -> AI Confidence: **99.48%**
3552. **`dependencies/kotlin-build-gradle-plugin/src/localProperties.kt`** -> AI Confidence: **99.48%**
3553. **`generators/builtins/unsignedTypes.kt`** -> AI Confidence: **99.48%**
3554. **`generators/evaluate/GenerateOperationsMap.kt`** -> AI Confidence: **99.48%**
3555. **`generators/ide-iml-to-gradle-generator/src/org/jetbrains/kotlin/generators/imltogradle/Main.kt`** -> AI Confidence: **99.48%**
3556. **`generators/ide-iml-to-gradle-generator/src/org/jetbrains/kotlin/generators/imltogradle/Util.kt`** -> AI Confidence: **99.48%**
3557. **`generators/ide-iml-to-gradle-generator/src/org/jetbrains/kotlin/generators/imltogradle/flattenExportedTransitiveDependencies.kt`** -> AI Confidence: **99.48%**
3558. **`generators/protobufCompare/GenerateProtoBufCompare.kt`** -> AI Confidence: **99.48%**
3559. **`generators/tests/org/jetbrains/kotlin/generators/arguments/DefaultValues.kt`** -> AI Confidence: **99.48%**
3560. **`generators/tests/org/jetbrains/kotlin/generators/arguments/GenerateGradleOptions.kt`** -> AI Confidence: **99.48%**
3561. **`generators/tests/org/jetbrains/kotlin/generators/mockJDK/filterMockJdk.kt`** -> AI Confidence: **99.48%**
3562. **`generators/tree-generator-common/src/org/jetbrains/kotlin/generators/tree/printer/common.kt`** -> AI Confidence: **99.48%**
3563. **`generators/tree-generator-common/src/org/jetbrains/kotlin/generators/tree/printer/printUtils.kt`** -> AI Confidence: **99.48%**
3564. **`jps/jps-common/src/org/jetbrains/kotlin/arguments/CompilerArgumentsDeserializer.kt`** -> AI Confidence: **99.48%**
3565. **`jps/jps-common/src/org/jetbrains/kotlin/config/KotlinFacetSettings.kt`** -> AI Confidence: **99.48%**
3566. **`jps/jps-common/src/org/jetbrains/kotlin/config/facetSerialization.kt`** -> AI Confidence: **99.48%**
3567. **`jps/jps-common/src/org/jetbrains/kotlin/config/moduleSourceRootPropertiesSerializers.kt`** -> AI Confidence: **99.48%**
3568. **`jps/jps-common/src/org/jetbrains/kotlin/platform/compat/compatConversions.kt`** -> AI Confidence: **99.48%**
3569. **`jps/jps-common/src/org/jetbrains/kotlin/platform/impl/JsIdePlatformKind.kt`** -> AI Confidence: **99.48%**
3570. **`jps/jps-common/src/org/jetbrains/kotlin/platform/impl/JvmIdePlatformKind.kt`** -> AI Confidence: **99.48%**
3571. **`jps/jps-common/src/org/jetbrains/kotlin/platform/impl/NativeIdePlatformKind.kt`** -> AI Confidence: **99.48%**
3572. **`jps/jps-plugin/src/org/jetbrains/jps/builders/java/dependencyView/NullabilityAnnotationsTracker.kt`** -> AI Confidence: **99.48%**
3573. **`jps/jps-plugin/src/org/jetbrains/kotlin/compilerRunner/CompilerRunnerUtil.kt`** -> AI Confidence: **99.48%**
3574. **`jps/jps-plugin/src/org/jetbrains/kotlin/compilerRunner/JpsKotlinCompilerRunner.kt`** -> AI Confidence: **99.48%**
3575. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/incremental/CacheVersionManager.kt`** -> AI Confidence: **99.48%**
3576. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/incremental/JpsIncrementalCache.kt`** -> AI Confidence: **99.48%**
3577. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/incremental/JpsLookupStorage.kt`** -> AI Confidence: **99.48%**
3578. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/incremental/KotlinCompilerReferenceIndexBuilder.kt`** -> AI Confidence: **99.48%**
3579. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/incremental/KotlinDataContainerTargetType.kt`** -> AI Confidence: **99.48%**
3580. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/model/ModuleSettings.kt`** -> AI Confidence: **99.48%**
3581. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/model/Serializer.kt`** -> AI Confidence: **99.48%**
3582. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/statistic/JpsBuilderMetricReporterImpl.kt`** -> AI Confidence: **99.48%**
3583. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/statistic/JpsFileReportService.kt`** -> AI Confidence: **99.48%**
3584. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/statistic/JpsStatisticsReportService.kt`** -> AI Confidence: **99.48%**
3585. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/KotlinJvmModuleBuildTarget.kt`** -> AI Confidence: **99.48%**
3586. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/KotlinModuleBuildTarget.kt`** -> AI Confidence: **99.48%**
3587. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/KotlinTargetsIndex.kt`** -> AI Confidence: **99.48%**
3588. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/KotlinUnsupportedModuleBuildTarget.kt`** -> AI Confidence: **99.48%**
3589. **`jps/jps-plugin/src/org/jetbrains/kotlin/jps/targets/impl/LookupUsageRegistrar.kt`** -> AI Confidence: **99.48%**
3590. **`js/js.config/src/org/jetbrains/kotlin/utils/JsLibraryUtils.kt`** -> AI Confidence: **99.48%**
3591. **`js/js.frontend/src/org/jetbrains/kotlin/frontend/js/di/injection.kt`** -> AI Confidence: **99.48%**
3592. **`js/js.frontend/src/org/jetbrains/kotlin/js/analyze/TopDownAnalyzerFacadeForJS.kt`** -> AI Confidence: **99.48%**
3593. **`js/js.frontend/src/org/jetbrains/kotlin/js/naming/NameSuggestion.kt`** -> AI Confidence: **99.48%**
3594. **`js/js.frontend/src/org/jetbrains/kotlin/js/naming/encodeSignature.kt`** -> AI Confidence: **99.48%**
3595. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsBuiltinNameClashChecker.kt`** -> AI Confidence: **99.48%**
3596. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsCallChecker.kt`** -> AI Confidence: **99.48%**
3597. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsDefinedExternallyCallChecker.kt`** -> AI Confidence: **99.48%**
3598. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsDynamicCallChecker.kt`** -> AI Confidence: **99.48%**
3599. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsDynamicDeclarationChecker.kt`** -> AI Confidence: **99.48%**
3600. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExportAnnotationChecker.kt`** -> AI Confidence: **99.48%**
3601. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExportDeclarationChecker.kt`** -> AI Confidence: **99.48%**
3602. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExternalArgumentCallChecker.kt`** -> AI Confidence: **99.48%**
3603. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExternalChecker.kt`** -> AI Confidence: **99.48%**
3604. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExternalFileChecker.kt`** -> AI Confidence: **99.48%**
3605. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsExternalInheritorOnlyChecker.kt`** -> AI Confidence: **99.48%**
3606. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsIdentifierChecker.kt`** -> AI Confidence: **99.48%**
3607. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsInheritanceChecker.kt`** -> AI Confidence: **99.48%**
3608. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsModuleCallChecker.kt`** -> AI Confidence: **99.48%**
3609. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsModuleCheckUtil.kt`** -> AI Confidence: **99.48%**
3610. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsModuleChecker.kt`** -> AI Confidence: **99.48%**
3611. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsMultipleInheritanceChecker.kt`** -> AI Confidence: **99.48%**
3612. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsNameCharsChecker.kt`** -> AI Confidence: **99.48%**
3613. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsNameChecker.kt`** -> AI Confidence: **99.48%**
3614. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsNameClashChecker.kt`** -> AI Confidence: **99.48%**
3615. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsNativeRttiChecker.kt`** -> AI Confidence: **99.48%**
3616. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsQualifierChecker.kt`** -> AI Confidence: **99.48%**
3617. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsReflectionAPICallChecker.kt`** -> AI Confidence: **99.48%**
3618. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/diagnostics/JsRuntimeAnnotationChecker.kt`** -> AI Confidence: **99.48%**
3619. **`js/js.frontend/src/org/jetbrains/kotlin/js/resolve/nativeAnnotationCheckers.kt`** -> AI Confidence: **99.48%**
3620. **`js/js.parser/src/org/jetbrains/kotlin/js/parser/JsParser.kt`** -> AI Confidence: **99.48%**
3621. **`js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/JsAstExtensions.kt`** -> AI Confidence: **99.48%**
3622. **`js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/JsAstMapperVisitor.kt`** -> AI Confidence: **99.48%**
3623. **`js/js.serializer/src/org/jetbrains/kotlin/serialization/js/DynamicTypeDeserializer.kt`** -> AI Confidence: **99.48%**
3624. **`js/js.serializer/src/org/jetbrains/kotlin/serialization/js/KotlinJavascriptPackageFragment.kt`** -> AI Confidence: **99.48%**
3625. **`js/js.serializer/src/org/jetbrains/kotlin/serialization/js/KotlinJavascriptSerializationUtil.kt`** -> AI Confidence: **99.48%**
3626. **`js/js.serializer/src/org/jetbrains/kotlin/serialization/js/kotlinJavascriptPackageFragmentProvider.kt`** -> AI Confidence: **99.48%**
3627. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/test/tools/SwcRunner.kt`** -> AI Confidence: **99.48%**
3628. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/test/utils/JsIrIncrementalDataProvider.kt`** -> AI Confidence: **99.48%**
3629. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/test/utils/RunnerUtils.kt`** -> AI Confidence: **99.48%**
3630. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/testOld/JsTestChecker.kt`** -> AI Confidence: **99.48%**
3631. **`js/js.tests/testFixtures/org/jetbrains/kotlin/js/testOld/utils/JsTestCliUtils.kt`** -> AI Confidence: **99.48%**
3632. **`js/js.translator/src/org/jetbrains/kotlin/js/inline/clean/RedundantStatementElimination.kt`** -> AI Confidence: **99.48%**
3633. **`js/js.translator/src/org/jetbrains/kotlin/js/inline/clean/TemporaryVariableElimination.kt`** -> AI Confidence: **99.48%**
3634. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/ExportModelGenerator.kt`** -> AI Confidence: **99.48%**
3635. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/TypeExporter.kt`** -> AI Confidence: **99.48%**
3636. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/TypeParameterScope.kt`** -> AI Confidence: **99.48%**
3637. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/TypeScriptExportRunner.kt`** -> AI Confidence: **99.48%**
3638. **`js/typescript-export-standalone/src/org/jetbrains/kotlin/js/tsexport/exportModelUtils.kt`** -> AI Confidence: **99.48%**
3639. **`kotlin-native/Interop/Indexer/src/main/kotlin/org/jetbrains/kotlin/native/interop/indexer/ModuleSupport.kt`** -> AI Confidence: **99.48%**
3640. **`kotlin-native/Interop/Indexer/src/main/kotlin/org/jetbrains/kotlin/native/interop/indexer/Utils.kt`** -> AI Confidence: **99.48%**
3641. **`kotlin-native/Interop/Runtime/src/jvm/kotlin/kotlinx/cinterop/JvmCallbacks.kt`** -> AI Confidence: **99.48%**
3642. **`kotlin-native/Interop/Runtime/src/jvm/kotlin/kotlinx/cinterop/JvmUtils.kt`** -> AI Confidence: **99.48%**
3643. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/StubIrDriver.kt`** -> AI Confidence: **99.48%**
3644. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/defFileDependencies.kt`** -> AI Confidence: **99.48%**
3645. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/jvm/InteropLibraryCreation.kt`** -> AI Confidence: **99.48%**
3646. **`kotlin-native/Interop/StubGenerator/src/org/jetbrains/kotlin/native/interop/gen/jvm/main.kt`** -> AI Confidence: **99.48%**
3647. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/common/AbstractValueUsageTransformer.kt`** -> AI Confidence: **99.48%**
3648. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/Boxing.kt`** -> AI Confidence: **99.48%**
3649. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/BuiltInFictitiousFunctionIrClassFactory.kt`** -> AI Confidence: **99.48%**
3650. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CStubsManager.kt`** -> AI Confidence: **99.48%**
3651. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CacheBuilder.kt`** -> AI Confidence: **99.48%**
3652. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CacheStorage.kt`** -> AI Confidence: **99.48%**
3653. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CacheSupport.kt`** -> AI Confidence: **99.48%**
3654. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CachedLibraries.kt`** -> AI Confidence: **99.48%**
3655. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/CompilerOutput.kt`** -> AI Confidence: **99.48%**
3656. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/Context.kt`** -> AI Confidence: **99.48%**
3657. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/DependenciesTracker.kt`** -> AI Confidence: **99.48%**
3658. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/EntryPoint.kt`** -> AI Confidence: **99.48%**
3659. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/FeaturedLibraries.kt`** -> AI Confidence: **99.48%**
3660. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/KonanCompilerFrontendServices.kt`** -> AI Confidence: **99.48%**
3661. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/KonanDriver.kt`** -> AI Confidence: **99.48%**
3662. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/Linker.kt`** -> AI Confidence: **99.48%**
3663. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/LlvmModuleSpecificationImpl.kt`** -> AI Confidence: **99.48%**
3664. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/NativeGenerationState.kt`** -> AI Confidence: **99.48%**
3665. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/NativeSecondStageCompilationConfig.kt`** -> AI Confidence: **99.48%**
3666. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/OptimizationPipeline.kt`** -> AI Confidence: **99.48%**
3667. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/SetupConfiguration.kt`** -> AI Confidence: **99.48%**
3668. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/TopDownAnalyzerFacadeForKonan.kt`** -> AI Confidence: **99.48%**
3669. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cexport/CAdapterApiExporter.kt`** -> AI Confidence: **99.48%**
3670. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cexport/CAdapterCodegen.kt`** -> AI Confidence: **99.48%**
3671. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cexport/CAdapterGenerator.kt`** -> AI Confidence: **99.48%**
3672. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cexport/CAdapterTypeTranslator.kt`** -> AI Confidence: **99.48%**
3673. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cgen/CBridgeGen.kt`** -> AI Confidence: **99.48%**
3674. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/cgen/CBridgeGenUtils.kt`** -> AI Confidence: **99.48%**
3675. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/NativeCompilerDriver.kt`** -> AI Confidence: **99.48%**
3676. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/BackendPhases.kt`** -> AI Confidence: **99.48%**
3677. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/Bitcode.kt`** -> AI Confidence: **99.48%**
3678. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/BitcodeGeneration.kt`** -> AI Confidence: **99.48%**
3679. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/CacheBuilding.kt`** -> AI Confidence: **99.48%**
3680. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/Frontend.kt`** -> AI Confidence: **99.48%**
3681. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/LTO.kt`** -> AI Confidence: **99.48%**
3682. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/LinkKlibs.kt`** -> AI Confidence: **99.48%**
3683. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/NativeLoweringPhases.kt`** -> AI Confidence: **99.48%**
3684. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/ObjCExport.kt`** -> AI Confidence: **99.48%**
3685. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/TopLevelPhases.kt`** -> AI Confidence: **99.48%**
3686. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/utilities/LlvmPassesUtilities.kt`** -> AI Confidence: **99.48%**
3687. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/injection.kt`** -> AI Confidence: **99.48%**
3688. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/ClassLayoutBuilder.kt`** -> AI Confidence: **99.48%**
3689. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/FunctionsWithoutBoundCheckGenerator.kt`** -> AI Confidence: **99.48%**
3690. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/IrUtils.kt`** -> AI Confidence: **99.48%**
3691. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/NewIrUtils.kt`** -> AI Confidence: **99.48%**
3692. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/DescriptorToIrTranslationUtils.kt`** -> AI Confidence: **99.48%**
3693. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/IrProviderForCEnumAndCStructStubs.kt`** -> AI Confidence: **99.48%**
3694. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/cenum/CEnumByValueFunctionGenerator.kt`** -> AI Confidence: **99.48%**
3695. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/cenum/CEnumClassGenerator.kt`** -> AI Confidence: **99.48%**
3696. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/cenum/CEnumCompanionGenerator.kt`** -> AI Confidence: **99.48%**
3697. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/cenum/CEnumVarClassGenerator.kt`** -> AI Confidence: **99.48%**
3698. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/cstruct/CStructVarClassGenerator.kt`** -> AI Confidence: **99.48%**
3699. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/ir/interop/cstruct/CStructVarCompanionGenerator.kt`** -> AI Confidence: **99.48%**
3700. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/linkKlibs.kt`** -> AI Confidence: **99.48%**
3701. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/BinaryInterface.kt`** -> AI Confidence: **99.48%**
3702. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/CodeGenerator.kt`** -> AI Confidence: **99.48%**
3703. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/ContextUtils.kt`** -> AI Confidence: **99.48%**
3704. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/DebugUtils.kt`** -> AI Confidence: **99.48%**
3705. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/Imports.kt`** -> AI Confidence: **99.48%**
3706. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/IntrinsicGenerator.kt`** -> AI Confidence: **99.48%**
3707. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/IrToBitcode.kt`** -> AI Confidence: **99.48%**
3708. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/KotlinObjCClassInfoGenerator.kt`** -> AI Confidence: **99.48%**
3709. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/LlvmDeclarations.kt`** -> AI Confidence: **99.48%**
3710. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/LlvmFunctionPrototype.kt`** -> AI Confidence: **99.48%**
3711. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/LlvmPassesProfile.kt`** -> AI Confidence: **99.48%**
3712. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/RTTIGenerator.kt`** -> AI Confidence: **99.48%**
3713. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/VariableManager.kt`** -> AI Confidence: **99.48%**
3714. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/objc/BindClassToObjCNameCodeGenerator.kt`** -> AI Confidence: **99.48%**
3715. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/objc/linkObjC.kt`** -> AI Confidence: **99.48%**
3716. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/objcexport/ObjCExportCodeGenerator.kt`** -> AI Confidence: **99.48%**
3717. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/objcexport/WritableTypeInfo.kt`** -> AI Confidence: **99.48%**
3718. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/runtime/RuntimeLinkage.kt`** -> AI Confidence: **99.48%**
3719. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/AddFunctionSupertypeToSuspendFunctionLowering.kt`** -> AI Confidence: **99.48%**
3720. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/Autoboxing.kt`** -> AI Confidence: **99.48%**
3721. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/BridgesBuilding.kt`** -> AI Confidence: **99.48%**
3722. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/BuiltinOperatorLowering.kt`** -> AI Confidence: **99.48%**
3723. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/CacheInfoBuilder.kt`** -> AI Confidence: **99.48%**
3724. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/CachesAbiLowering.kt`** -> AI Confidence: **99.48%**
3725. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/CastsLowering.kt`** -> AI Confidence: **99.48%**
3726. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ConstructorsLowering.kt`** -> AI Confidence: **99.48%**
3727. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ContractsDslRemover.kt`** -> AI Confidence: **99.48%**
3728. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/CoroutinesVarSpillingLowering.kt`** -> AI Confidence: **99.48%**
3729. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/DataClassOperatorsLowering.kt`** -> AI Confidence: **99.48%**
3730. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/EnumClassLowering.kt`** -> AI Confidence: **99.48%**
3731. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/EnumConstructorsLowering.kt`** -> AI Confidence: **99.48%**
3732. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ExpectToActualDefaultValueCopier.kt`** -> AI Confidence: **99.48%**
3733. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/GenericCallsReturnTypeEraser.kt`** -> AI Confidence: **99.48%**
3734. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InitializersLowering.kt`** -> AI Confidence: **99.48%**
3735. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InlineClassPropertyAccessorsLowering.kt`** -> AI Confidence: **99.48%**
3736. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InnerClassLowering.kt`** -> AI Confidence: **99.48%**
3737. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InteropBridgesNameInventor.kt`** -> AI Confidence: **99.48%**
3738. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InteropCallConvertors.kt`** -> AI Confidence: **99.48%**
3739. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/InteropLowering.kt`** -> AI Confidence: **99.48%**
3740. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeAnnotationImplementationLowering.kt`** -> AI Confidence: **99.48%**
3741. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeDefaultParameterInjector.kt`** -> AI Confidence: **99.48%**
3742. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeFunctionReferenceLowering.kt`** -> AI Confidence: **99.48%**
3743. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeInlineFunctionResolver.kt`** -> AI Confidence: **99.48%**
3744. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeInventNamesForLocalClasses.kt`** -> AI Confidence: **99.48%**
3745. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeIrInliner.kt`** -> AI Confidence: **99.48%**
3746. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeReflectionIrBuilder.kt`** -> AI Confidence: **99.48%**
3747. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeSingleAbstractMethodLowering.kt`** -> AI Confidence: **99.48%**
3748. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/NativeSuspendFunctionLowering.kt`** -> AI Confidence: **99.48%**
3749. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ObjectClassLowering.kt`** -> AI Confidence: **99.48%**
3750. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/PostInlineLowering.kt`** -> AI Confidence: **99.48%**
3751. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/PropertyReferenceLowering.kt`** -> AI Confidence: **99.48%**
3752. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/RedundantCoercionsCleaner.kt`** -> AI Confidence: **99.48%**
3753. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/RemoveCastsFromNothingLowering.kt`** -> AI Confidence: **99.48%**
3754. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ReturnsInsertionLowering.kt`** -> AI Confidence: **99.48%**
3755. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/SamSuperTypesChecker.kt`** -> AI Confidence: **99.48%**
3756. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/SpecialInteropIntrinsicsLowering.kt`** -> AI Confidence: **99.48%**
3757. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/SpecialObjCValidationLowering.kt`** -> AI Confidence: **99.48%**
3758. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/StaticCallableReferenceOptimization.kt`** -> AI Confidence: **99.48%**
3759. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/StaticInitializersLowering.kt`** -> AI Confidence: **99.48%**
3760. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/StringConcatenationTypeNarrowing.kt`** -> AI Confidence: **99.48%**
3761. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TestsDumper.kt`** -> AI Confidence: **99.48%**
3762. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TestsInitializer.kt`** -> AI Confidence: **99.48%**
3763. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TypeOfProcessingLowering.kt`** -> AI Confidence: **99.48%**
3764. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/TypeOperatorLowering.kt`** -> AI Confidence: **99.48%**
3765. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/UnboxInlineLowering.kt`** -> AI Confidence: **99.48%**
3766. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/VarargLowering.kt`** -> AI Confidence: **99.48%**
3767. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/VolatileFieldsLowering.kt`** -> AI Confidence: **99.48%**
3768. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/objcexport/InfoPListBuilder.kt`** -> AI Confidence: **99.48%**
3769. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExport.kt`** -> AI Confidence: **99.48%**
3770. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportCodeSpec.kt`** -> AI Confidence: **99.48%**
3771. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/CallGraphBuilder.kt`** -> AI Confidence: **99.48%**
3772. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/CastsOptimization.kt`** -> AI Confidence: **99.48%**
3773. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/ComputeTypesPass.kt`** -> AI Confidence: **99.48%**
3774. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DCE.kt`** -> AI Confidence: **99.48%**
3775. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DFGBuilder.kt`** -> AI Confidence: **99.48%**
3776. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DataFlowIR.kt`** -> AI Confidence: **99.48%**
3777. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DevirtualizationAnalysis.kt`** -> AI Confidence: **99.48%**
3778. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/EscapeAnalysis.kt`** -> AI Confidence: **99.48%**
3779. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/KonanBCEForLoopBodyTransformer.kt`** -> AI Confidence: **99.48%**
3780. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/PreCodegenInliner.kt`** -> AI Confidence: **99.48%**
3781. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/StaticInitializersOptimization.kt`** -> AI Confidence: **99.48%**
3782. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/CacheSerializationSupport.kt`** -> AI Confidence: **99.48%**
3783. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/ExternalDeclarationFileNameProvider.kt`** -> AI Confidence: **99.48%**
3784. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/KonanInteropModuleDeserializer.kt`** -> AI Confidence: **99.48%**
3785. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/ModuleDeserializerProvider.kt`** -> AI Confidence: **99.48%**
3786. **`kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/serialization/ProtoUtils.kt`** -> AI Confidence: **99.48%**
3787. **`kotlin-native/backend.native/tests/samples/objc/src/objcMain/kotlin/Async.kt`** -> AI Confidence: **99.48%**
3788. **`kotlin-native/backend.native/tests/samples/objc/src/objcMain/kotlin/Window.kt`** -> AI Confidence: **99.48%**
3789. **`kotlin-native/backend.native/tests/samples/tensorflow/src/tensorflowMain/kotlin/HelloTensorflow.kt`** -> AI Confidence: **99.48%**
3790. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/CompareDistributionSignatures.kt`** -> AI Confidence: **99.48%**
3791. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/Utils.kt`** -> AI Confidence: **99.48%**
3792. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/bitcode/CompileToBitcodePlugin.kt`** -> AI Confidence: **99.48%**
3793. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/cpp/CompilationDatabasePlugin.kt`** -> AI Confidence: **99.48%**
3794. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/cpp/CompileToExecutable.kt`** -> AI Confidence: **99.48%**
3795. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/cpp/GenerateCompilationDatabase.kt`** -> AI Confidence: **99.48%**
3796. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/cpp/GitClangFormat.kt`** -> AI Confidence: **99.48%**
3797. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/cpp/RunGTest.kt`** -> AI Confidence: **99.48%**
3798. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/dependencies/NativeDependenciesDownloader.kt`** -> AI Confidence: **99.48%**
3799. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/dependencies/NativeDependenciesDownloaderPlugin.kt`** -> AI Confidence: **99.48%**
3800. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/dependencies/NativeDependenciesPlugin.kt`** -> AI Confidence: **99.48%**
3801. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/gradle/plugin/konan/tasks/KonanCompileTask.kt`** -> AI Confidence: **99.48%**
3802. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/gradle/plugin/konan/tasks/KonanInteropTask.kt`** -> AI Confidence: **99.48%**
3803. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/interop/NativeInteropPlugin.kt`** -> AI Confidence: **99.48%**
3804. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/nativeDistribution/InvalidateStaleCaches.kt`** -> AI Confidence: **99.48%**
3805. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/nativeDistribution/LLVMDistributionSource.kt`** -> AI Confidence: **99.48%**
3806. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/nativeDistribution/NativeDistribution.kt`** -> AI Confidence: **99.48%**
3807. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/nativeDistribution/PrepareDistributionFingerprint.kt`** -> AI Confidence: **99.48%**
3808. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/nativeFullCrossDist.kt`** -> AI Confidence: **99.48%**
3809. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/platformLibs/updateDefFileDependencies.kt`** -> AI Confidence: **99.48%**
3810. **`kotlin-native/build-tools/src/main/kotlin/org/jetbrains/kotlin/tools/NativePlugin.kt`** -> AI Confidence: **99.48%**
3811. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/DescriptorSignaturesRenderer.kt`** -> AI Confidence: **99.48%**
3812. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/IrSignaturesExtractor.kt`** -> AI Confidence: **99.48%**
3813. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/KlibToolCommands.kt`** -> AI Confidence: **99.48%**
3814. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/KlibToolIrLinker.kt`** -> AI Confidence: **99.48%**
3815. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/KotlinpBasedMetadataDumper.kt`** -> AI Confidence: **99.48%**
3816. **`kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/ModuleDescriptorLoader.kt`** -> AI Confidence: **99.48%**
3817. **`kotlin-native/performance/benchmarksAnalyzer/src/commonMain/kotlin/org/jetbrains/analyzer/Statistics.kt`** -> AI Confidence: **99.48%**
3818. **`kotlin-native/performance/benchmarksAnalyzer/src/commonMain/kotlin/org/jetbrains/analyzer/SummaryBenchmarksReport.kt`** -> AI Confidence: **99.48%**
3819. **`kotlin-native/performance/buildSrc/src/main/kotlin/CodeSizeTask.kt`** -> AI Confidence: **99.48%**
3820. **`kotlin-native/performance/buildSrc/src/main/kotlin/GenerateSwiftPackageTask.kt`** -> AI Confidence: **99.48%**
3821. **`kotlin-native/performance/buildSrc/src/main/kotlin/JsonReportTask.kt`** -> AI Confidence: **99.48%**
3822. **`kotlin-native/performance/buildSrc/src/main/kotlin/RunKotlinNativeTask.kt`** -> AI Confidence: **99.48%**
3823. **`kotlin-native/performance/buildSrc/src/main/kotlin/benchmark/BenchmarkingPlugin.kt`** -> AI Confidence: **99.48%**
3824. **`kotlin-native/performance/objcinterop/src/nativeMain/kotlin/org/jetbrains/objCinteropBenchmarks/complexNumbers.kt`** -> AI Confidence: **99.48%**
3825. **`kotlin-native/performance/ring/src/commonMain/kotlin/org/jetbrains/ring/WeakRefBenchmark.kt`** -> AI Confidence: **99.48%**
3826. **`kotlin-native/prepare/kotlin-native-compiler-embeddable/tests/kotlin/org/jetbrains/kotlin/native/compiler/embeddable/CompilerEmbeddableSmokeTests.kt`** -> AI Confidence: **99.48%**
3827. **`kotlin-native/runtime/src/main/kotlin/kotlin/Throwable.kt`** -> AI Confidence: **99.48%**
3828. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/concurrent/Internal.kt`** -> AI Confidence: **99.48%**
3829. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/internal/RuntimeUtils.kt`** -> AI Confidence: **99.48%**
3830. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/internal/concurrent/Monitor.kt`** -> AI Confidence: **99.48%**
3831. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/internal/reflect/KClassEx.kt`** -> AI Confidence: **99.48%**
3832. **`kotlin-native/runtime/src/main/kotlin/kotlin/native/ref/Cleaner.kt`** -> AI Confidence: **99.48%**
3833. **`kotlin-native/tools/compiler-cache-invalidator/src/org/jetbrains/kotlin/nativecacheinvalidator/NativeCacheInvalidator.kt`** -> AI Confidence: **99.48%**
3834. **`kotlin-native/tools/kdumputil/src/io/inputStream.kt`** -> AI Confidence: **99.48%**
3835. **`kotlin-native/tools/kdumputil/src/kdump/hprof/converter.kt`** -> AI Confidence: **99.48%**
3836. **`kotlin-native/tools/kdumputil/src/main.kt`** -> AI Confidence: **99.48%**
3837. **`kotlin-native/utilities/cli-runner/src/org/jetbrains/kotlin/cli/utilities/GeneratePlatformLibraries.kt`** -> AI Confidence: **99.48%**
3838. **`kotlin-native/utilities/cli-runner/src/org/jetbrains/kotlin/cli/utilities/InteropCompiler.kt`** -> AI Confidence: **99.48%**
3839. **`kotlin-native/utilities/cli-runner/src/org/jetbrains/kotlin/cli/utilities/main.kt`** -> AI Confidence: **99.48%**
3840. **`libraries/examples/annotation-processor-example/src/main/kotlin/example/ExampleAnnotationProcessor.kt`** -> AI Confidence: **99.48%**
3841. **`libraries/examples/scripting/jvm-embeddable-host/src/org/jetbrains/kotlin/script/examples/jvm/embeddable/host/host.kt`** -> AI Confidence: **99.48%**
3842. **`libraries/examples/scripting/jvm-maven-deps/host/src/org/jetbrains/kotlin/script/examples/jvm/resolve/maven/host/host.kt`** -> AI Confidence: **99.48%**
3843. **`libraries/examples/scripting/jvm-simple-script/host/src/org/jetbrains/kotlin/script/examples/jvm/simple/host/host.kt`** -> AI Confidence: **99.48%**
3844. **`libraries/kotlin.test/common/src/main/kotlin/kotlin/test/Assertions.kt`** -> AI Confidence: **99.48%**
3845. **`libraries/kotlinx-metadata/jvm/src/kotlin/metadata/jvm/KotlinModuleMetadata.kt`** -> AI Confidence: **99.48%**
3846. **`libraries/kotlinx-metadata/jvm/src/kotlin/metadata/jvm/internal/JvmMetadataExtensions.kt`** -> AI Confidence: **99.48%**
3847. **`libraries/kotlinx-metadata/jvm/src/kotlin/metadata/jvm/internal/JvmReadUtils.kt`** -> AI Confidence: **99.48%**
3848. **`libraries/kotlinx-metadata/klib/src/kotlinx/metadata/klib/KlibModuleMetadata.kt`** -> AI Confidence: **99.48%**
3849. **`libraries/kotlinx-metadata/klib/src/kotlinx/metadata/klib/impl/klibMetadataExtensions.kt`** -> AI Confidence: **99.48%**
3850. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/FlagDelegatesImpl.kt`** -> AI Confidence: **99.48%**
3851. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/ReadUtils.kt`** -> AI Confidence: **99.48%**
3852. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/Readers.kt`** -> AI Confidence: **99.48%**
3853. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/Writers.kt`** -> AI Confidence: **99.48%**
3854. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/common/BuiltInMetadataExtensions.kt`** -> AI Confidence: **99.48%**
3855. **`libraries/kotlinx-metadata/src/kotlin/metadata/internal/common/KotlinCommonMetadata.kt`** -> AI Confidence: **99.48%**
3856. **`libraries/scripting/common/src/kotlin/script/experimental/util/propertiesCollection.kt`** -> AI Confidence: **99.48%**
3857. **`libraries/scripting/dependencies-maven/src/kotlin/script/experimental/dependencies/maven/MavenDependenciesResolver.kt`** -> AI Confidence: **99.48%**
3858. **`libraries/scripting/dependencies-maven/src/kotlin/script/experimental/dependencies/maven/impl/aether.kt`** -> AI Confidence: **99.48%**
3859. **`libraries/scripting/dependencies-maven/src/kotlin/script/experimental/dependencies/maven/impl/mavenSettings.kt`** -> AI Confidence: **99.48%**
3860. **`libraries/scripting/jsr223/src/kotlin/script/experimental/jsr223/KotlinJsr223DefaultScript.kt`** -> AI Confidence: **99.48%**
3861. **`libraries/scripting/jsr223/src/kotlin/script/experimental/jsr223/KotlinJsr223DefaultScriptEngineFactory.kt`** -> AI Confidence: **99.48%**
3862. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/jsr223/KotlinJsr223InvocableScriptEngine.kt`** -> AI Confidence: **99.48%**
3863. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/jsr223/KotlinJsr223ScriptEngineImpl.kt`** -> AI Confidence: **99.48%**
3864. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/jvmScriptCompilation.kt`** -> AI Confidence: **99.48%**
3865. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/jvmScriptSaving.kt`** -> AI Confidence: **99.48%**
3866. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/repl/legacyReplCompilation.kt`** -> AI Confidence: **99.48%**
3867. **`libraries/scripting/jvm-host/src/kotlin/script/experimental/jvmhost/repl/legacyReplEvaluation.kt`** -> AI Confidence: **99.48%**
3868. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/jvmScriptEvaluation.kt`** -> AI Confidence: **99.48%**
3869. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/jvmScriptingHostConfiguration.kt`** -> AI Confidence: **99.48%**
3870. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/util/jvmClassLoaderUtil.kt`** -> AI Confidence: **99.48%**
3871. **`libraries/scripting/jvm/src/kotlin/script/experimental/jvm/util/jvmClasspathUtil.kt`** -> AI Confidence: **99.48%**
3872. **`libraries/stdlib/jdk7/src/kotlin/io/path/PathReadWrite.kt`** -> AI Confidence: **99.48%**
3873. **`libraries/stdlib/jdk7/src/kotlin/io/path/PathUtils.kt`** -> AI Confidence: **99.48%**
3874. **`libraries/stdlib/jdk8/src/kotlin/internal/jdk8/JDK8PlatformImplementations.kt`** -> AI Confidence: **99.48%**
3875. **`libraries/stdlib/jvm/src/kotlin/collections/MapsJVM.kt`** -> AI Confidence: **99.48%**
3876. **`libraries/stdlib/jvm/src/kotlin/internal/PlatformImplementations.kt`** -> AI Confidence: **99.48%**
3877. **`libraries/stdlib/jvm/src/kotlin/io/FileReadWrite.kt`** -> AI Confidence: **99.48%**
3878. **`libraries/stdlib/jvm/src/kotlin/io/ReadWrite.kt`** -> AI Confidence: **99.48%**
3879. **`libraries/stdlib/jvm/src/kotlin/io/encoding/Base64IOStream.kt`** -> AI Confidence: **99.48%**
3880. **`libraries/stdlib/jvm/src/kotlin/text/regex/Regex.kt`** -> AI Confidence: **99.48%**
3881. **`libraries/stdlib/jvm/src/kotlin/util/MathJVM.kt`** -> AI Confidence: **99.48%**
3882. **`libraries/stdlib/jvm/test/utils/LazyJVMTest.kt`** -> AI Confidence: **99.48%**
3883. **`libraries/stdlib/native-wasm/src/kotlin/text/regex/AbstractCharClass.kt`** -> AI Confidence: **99.48%**
3884. **`libraries/stdlib/src/kotlin/uuid/Uuid.kt`** -> AI Confidence: **99.48%**
3885. **`libraries/stdlib/wasm/wasi/src/kotlin/time/TimeSources.kt`** -> AI Confidence: **99.48%**
3886. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/AbiComparatorMain.kt`** -> AI Confidence: **99.48%**
3887. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/FieldsListChecker.kt`** -> AI Confidence: **99.48%**
3888. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/GenericMetadataChecker.kt`** -> AI Confidence: **99.48%**
3889. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/InnerClassesListChecker.kt`** -> AI Confidence: **99.48%**
3890. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/MethodsListChecker.kt`** -> AI Confidence: **99.48%**
3891. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/checkers/metadataUtils.kt`** -> AI Confidence: **99.48%**
3892. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/reports/ClassReport.kt`** -> AI Confidence: **99.48%**
3893. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/reports/MethodReport.kt`** -> AI Confidence: **99.48%**
3894. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/tasks/CheckerConfiguration.kt`** -> AI Confidence: **99.48%**
3895. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/tasks/ClassTask.kt`** -> AI Confidence: **99.48%**
3896. **`libraries/tools/abi-comparator/src/main/kotlin/org/jetbrains/kotlin/abicmp/tasks/JarTask.kt`** -> AI Confidence: **99.48%**
3897. **`libraries/tools/abi-validation/abi-tools-tests/src/sharedTests/kotlin/org/jetbrains/kotlin/abi/tools/tests/KlibDumpSamples.kt`** -> AI Confidence: **99.48%**
3898. **`libraries/tools/abi-validation/abi-tools/src/main/kotlin/org/jetbrains/kotlin/abi/tools/impl/AbiToolsImpl.kt`** -> AI Confidence: **99.48%**
3899. **`libraries/tools/abi-validation/abi-tools/src/main/kotlin/org/jetbrains/kotlin/abi/tools/impl/jvm/KotlinSignaturesLoading.kt`** -> AI Confidence: **99.48%**
3900. **`libraries/tools/abi-validation/abi-tools/src/test/kotlin/org/jetbrains/kotlin/abi/tools/impl/FiltersMatcherTests.kt`** -> AI Confidence: **99.48%**
3901. **`libraries/tools/abi-validation/abi-tools/src/test/kotlin/org/jetbrains/kotlin/abi/tools/impl/KlibAbiMergingTest.kt`** -> AI Confidence: **99.48%**
3902. **`libraries/tools/abi-validation/abi-tools/src/test/kotlin/org/jetbrains/kotlin/abi/tools/impl/KlibTargetHierarchyTest.kt`** -> AI Confidence: **99.48%**
3903. **`libraries/tools/abi-validation/kgp-integration-tests/src/test/kotlin/org/jetbrains/abi/tools/test/KlibVerificationTests.kt`** -> AI Confidence: **99.48%**
3904. **`libraries/tools/analysis-api-based-klib-reader/src/org/jetbrains/kotlin/analysis/api/klib/reader/PackageFragmentReadingContext.kt`** -> AI Confidence: **99.48%**
3905. **`libraries/tools/analysis-api-based-klib-reader/src/org/jetbrains/kotlin/analysis/api/klib/reader/createKaModules.kt`** -> AI Confidence: **99.48%**
3906. **`libraries/tools/analysis-api-based-klib-reader/src/org/jetbrains/kotlin/analysis/api/klib/reader/getAllLibraryModules.kt`** -> AI Confidence: **99.48%**
3907. **`libraries/tools/analysis-api-based-klib-reader/src/org/jetbrains/kotlin/analysis/api/klib/reader/readKlibDeclarationAddresses.kt`** -> AI Confidence: **99.48%**
3908. **`libraries/tools/analysis-api-based-klib-reader/test/org/jetbrains/kotlin/analysis/api/klib/reader/tests/GetSymbolsTest.kt`** -> AI Confidence: **99.48%**
3909. **`libraries/tools/analysis-api-based-klib-reader/test/org/jetbrains/kotlin/analysis/api/klib/reader/tests/ReadKlibDeclarationAddressesBlackBoxTest.kt`** -> AI Confidence: **99.48%**
3910. **`libraries/tools/binary-compatibility-validator/src/test/kotlin/org.jetbrains.kotlin.tools.tests/KlibPublicAPITest.kt`** -> AI Confidence: **99.48%**
3911. **`libraries/tools/dukat/src/main/kotlin/org/jetbrains/kotlin/tools/dukat/wasm/convertToModel.kt`** -> AI Confidence: **99.48%**
3912. **`libraries/tools/dukat/src/main/kotlin/org/jetbrains/kotlin/tools/dukat/wasm/translator.kt`** -> AI Confidence: **99.48%**
3913. **`libraries/tools/gradle/fus-statistics-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/fus/BuildUidService.kt`** -> AI Confidence: **99.48%**
3914. **`libraries/tools/gradle/fus-statistics-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/fus/internal/BuildCloseFusStatisticsBuildService.kt`** -> AI Confidence: **99.48%**
3915. **`libraries/tools/gradle/fus-statistics-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/fus/internal/BuildFlowFusStatisticsBuildService.kt`** -> AI Confidence: **99.48%**
3916. **`libraries/tools/gradle/fus-statistics-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/fus/internal/GradleBuildFusStatisticsBuildService.kt`** -> AI Confidence: **99.48%**
3917. **`libraries/tools/gradle/fus-statistics-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/fus/internal/InternalGradleBuildFusStatisticsService.kt`** -> AI Confidence: **99.48%**
3918. **`libraries/tools/gradle/generators/native-cache-kotlin-version/src/main/kotlin/org/jetbrains/kotlin/gradle/generators/native/cache/version/NativeCacheKotlinVersionsGenerator.kt`** -> AI Confidence: **99.48%**
3919. **`libraries/tools/gradle/generators/native-cache-kotlin-version/src/test/kotlin/GenerateKotlinVersionTest.kt`** -> AI Confidence: **99.48%**
3920. **`libraries/tools/gradle/kotlin-compiler-args-properties/src/common/kotlin/org/jetbrains/kotlin/gradle/arguments/GradleKotlinCompilerArgumentsPlugin.kt`** -> AI Confidence: **99.48%**
3921. **`libraries/tools/gradle/kotlin-gradle-ecosystem-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/ecosystem/KotlinEcosystemPlugin.kt`** -> AI Confidence: **99.48%**
3922. **`libraries/tools/gradle/regression-benchmark-templates/src/main/kotlin/org/jetbrains/kotlin/gradle/benchmark/BenchmarkTemplate.kt`** -> AI Confidence: **99.48%**
3923. **`libraries/tools/ide-plugin-dependencies-validator/src/org/jetbrains/kotlin/ide/plugin/dependencies/validator/ExperimentalAnnotationListChecker.kt`** -> AI Confidence: **99.48%**
3924. **`libraries/tools/ide-plugin-dependencies-validator/src/org/jetbrains/kotlin/ide/plugin/dependencies/validator/KotlinParsingUtils.kt`** -> AI Confidence: **99.48%**
3925. **`libraries/tools/kotlin-compose-compiler/src/common/kotlin/org/jetbrains/kotlin/compose/compiler/gradle/ComposeCompilerGradlePluginExtension.kt`** -> AI Confidence: **99.48%**
3926. **`libraries/tools/kotlin-compose-compiler/src/common/kotlin/org/jetbrains/kotlin/compose/compiler/gradle/internal/ComposeAgpMappingFile.kt`** -> AI Confidence: **99.48%**
3927. **`libraries/tools/kotlin-compose-compiler/src/functionalTest/kotlin/org/jetbrains/kotlin/compose/compiler/gradle/ExtensionConfigurationTest.kt`** -> AI Confidence: **99.48%**
3928. **`libraries/tools/kotlin-compose-compiler/src/functionalTest/kotlin/org/jetbrains/kotlin/compose/compiler/gradle/testUtils/functionalTestDsl.kt`** -> AI Confidence: **99.48%**
3929. **`libraries/tools/kotlin-compose-compiler/src/test/kotlin/org/jetbrains/kotlin/compose/compiler/gradle/internal/ComposeWithAgpConfigTest.kt`** -> AI Confidence: **99.48%**
3930. **`libraries/tools/kotlin-gradle-plugin-api/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/abi/AbiValidationExtension.kt`** -> AI Confidence: **99.48%**
3931. **`libraries/tools/kotlin-gradle-plugin-api/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinCompilation.kt`** -> AI Confidence: **99.48%**
3932. **`libraries/tools/kotlin-gradle-plugin-api/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinTarget.kt`** -> AI Confidence: **99.48%**
3933. **`libraries/tools/kotlin-gradle-plugin-api/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/IncrementalSyncTask.kt`** -> AI Confidence: **99.48%**
3934. **`libraries/tools/kotlin-gradle-plugin-api/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/KotlinTaskConfigs.kt`** -> AI Confidence: **99.48%**
3935. **`libraries/tools/kotlin-gradle-plugin-dsl-codegen/src/main/kotlin/org/jetbrains/kotlin/generators/gradle/dsl/mppNativeBinaryDSLCodegen.kt`** -> AI Confidence: **99.48%**
3936. **`libraries/tools/kotlin-gradle-plugin-dsl-codegen/src/main/kotlin/org/jetbrains/kotlin/generators/gradle/dsl/mppPresetFunctionsCodegen.kt`** -> AI Confidence: **99.48%**
3937. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/extras.kt`** -> AI Confidence: **99.48%**
3938. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinClasspath.kt`** -> AI Confidence: **99.48%**
3939. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinProjectArtifactDependency.kt`** -> AI Confidence: **99.48%**
3940. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinResolvedBinaryDependency.kt`** -> AI Confidence: **99.48%**
3941. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinSourceDependency.kt`** -> AI Confidence: **99.48%**
3942. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/main/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinUnresolvedBinaryDependency.kt`** -> AI Confidence: **99.48%**
3943. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinDependencyBackwardsCompatibilityTest.kt`** -> AI Confidence: **99.48%**
3944. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinDependencyForwardCompatibilityTest.kt`** -> AI Confidence: **99.48%**
3945. **`libraries/tools/kotlin-gradle-plugin-idea-proto/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/proto/tcs/IdeaKotlinDependencySerializationTest.kt`** -> AI Confidence: **99.48%**
3946. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/serialize/IdeaJavaIoSerializableExtrasSerializerTest.kt`** -> AI Confidence: **99.48%**
3947. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/IdeaKotlinEntityAnnotationUtils.kt`** -> AI Confidence: **99.48%**
3948. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/IdeaKotlinEntityTest.kt`** -> AI Confidence: **99.48%**
3949. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/IdeaKotlinExtraTest.kt`** -> AI Confidence: **99.48%**
3950. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/IdeaKotlinModelObjectGraphTest.kt`** -> AI Confidence: **99.48%**
3951. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/ReflectionTestUtils.kt`** -> AI Confidence: **99.48%**
3952. **`libraries/tools/kotlin-gradle-plugin-idea/src/test/kotlin/org/jetbrains/kotlin/gradle/idea/test/tcs/assertNodeContainsSerialVersionUID.kt`** -> AI Confidence: **99.48%**
3953. **`libraries/tools/kotlin-gradle-plugin-idea/src/testFixtures/kotlin/org/jetbrains/kotlin/gradle/idea/testFixtures/tcs/TestIdeaKotlinDependencySerializer.kt`** -> AI Confidence: **99.48%**
3954. **`libraries/tools/kotlin-gradle-plugin-idea/src/testFixtures/kotlin/org/jetbrains/kotlin/gradle/idea/testFixtures/tcs/ideaDependencyMatcherBuilders.kt`** -> AI Confidence: **99.48%**
3955. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BrokenMacosTestInterceptor.kt`** -> AI Confidence: **99.48%**
3956. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BuildCacheIT.kt`** -> AI Confidence: **99.48%**
3957. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BuildCacheRelocationIT.kt`** -> AI Confidence: **99.48%**
3958. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BuildReportsIT.kt`** -> AI Confidence: **99.48%**
3959. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BuildScriptInjectionIT.kt`** -> AI Confidence: **99.48%**
3960. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BuildStatisticsWithKtorIT.kt`** -> AI Confidence: **99.48%**
3961. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/BuildToolsApiJvmCompilationIT.kt`** -> AI Confidence: **99.48%**
3962. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/CommonizerIT.kt`** -> AI Confidence: **99.48%**
3963. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/CompilerOptionsIT.kt`** -> AI Confidence: **99.48%**
3964. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/CompilerOptionsProjectIT.kt`** -> AI Confidence: **99.48%**
3965. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/CompilerReferenceIndexIT.kt`** -> AI Confidence: **99.48%**
3966. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ComposeIT.kt`** -> AI Confidence: **99.48%**
3967. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ConfigurationAvoidanceIT.kt`** -> AI Confidence: **99.48%**
3968. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ConfigurationCacheIT.kt`** -> AI Confidence: **99.48%**
3969. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/DeterministicBuildIT.kt`** -> AI Confidence: **99.48%**
3970. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/DifferentClassloadersIT.kt`** -> AI Confidence: **99.48%**
3971. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ExecutionStrategyIT.kt`** -> AI Confidence: **99.48%**
3972. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ExplicitApiIT.kt`** -> AI Confidence: **99.48%**
3973. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/FusPluginIT.kt`** -> AI Confidence: **99.48%**
3974. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/FusStatisticsIT.kt`** -> AI Confidence: **99.48%**
3975. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/GradleCompatibilityIT.kt`** -> AI Confidence: **99.48%**
3976. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/GradleDaemonMemoryIT.kt`** -> AI Confidence: **99.48%**
3977. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/HierarchicalMppIT.kt`** -> AI Confidence: **99.48%**
3978. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/IncrementalCompilationMultiProjectIT.kt`** -> AI Confidence: **99.48%**
3979. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/IncrementalJavaChangeIT.kt`** -> AI Confidence: **99.48%**
3980. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/JvmBinariesDslIT.kt`** -> AI Confidence: **99.48%**
3981. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/JvmDefaultIT.kt`** -> AI Confidence: **99.48%**
3982. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/JvmTargetValidationTest.kt`** -> AI Confidence: **99.48%**
3983. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/K2KotlinxSerializationIT.kt`** -> AI Confidence: **99.48%**
3984. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/K2Tests.kt`** -> AI Confidence: **99.48%**
3985. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KaptIT.kt`** -> AI Confidence: **99.48%**
3986. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KaptIncrementalIT.kt`** -> AI Confidence: **99.48%**
3987. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KaptIncrementalWithAggregatingApt.kt`** -> AI Confidence: **99.48%**
3988. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KaptIncrementalWithIsolatingApt.kt`** -> AI Confidence: **99.48%**
3989. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KlibBasedMppIT.kt`** -> AI Confidence: **99.48%**
3990. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KmpPartiallyResolvedDependenciesCheckerIT.kt`** -> AI Confidence: **99.48%**
3991. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/Kotlin2JsGradlePluginIT.kt`** -> AI Confidence: **99.48%**
3992. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/Kotlin2JsIrBeIncrementalCompilationIT.kt`** -> AI Confidence: **99.48%**
3993. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinDaemonIT.kt`** -> AI Confidence: **99.48%**
3994. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinDaemonJvmArgsTest.kt`** -> AI Confidence: **99.48%**
3995. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinGradlePluginIT.kt`** -> AI Confidence: **99.48%**
3996. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinJavaToolchainTest.kt`** -> AI Confidence: **99.48%**
3997. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinJsLibraryGradlePluginIT.kt`** -> AI Confidence: **99.48%**
3998. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinSpecificDependenciesIT.kt`** -> AI Confidence: **99.48%**
3999. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinToolingMetadataIT.kt`** -> AI Confidence: **99.48%**
4000. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinTopLevelDependenciesIT.kt`** -> AI Confidence: **99.48%**
4001. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/KotlinWasmGradlePluginIT.kt`** -> AI Confidence: **99.48%**
4002. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/LoggingConfigurationIT.kt`** -> AI Confidence: **99.48%**
4003. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MPPBuildReproducibilityIT.kt`** -> AI Confidence: **99.48%**
4004. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MacosCapableConfigurationCacheIT.kt`** -> AI Confidence: **99.48%**
4005. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MppCInteropDependencyTransformationIT.kt`** -> AI Confidence: **99.48%**
4006. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MppHighlightingTestDataWithGradleIT.kt`** -> AI Confidence: **99.48%**
4007. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MppIdeDependencyResolutionIT.kt`** -> AI Confidence: **99.48%**
4008. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/NodeJsGradlePluginIT.kt`** -> AI Confidence: **99.48%**
4009. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/PackageManagerGradlePluginIT.kt`** -> AI Confidence: **99.48%**
4010. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/PgpHelpersTest.kt`** -> AI Confidence: **99.48%**
4011. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ProblemsApiIT.kt`** -> AI Confidence: **99.48%**
4012. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/PublishingHelpersTest.kt`** -> AI Confidence: **99.48%**
4013. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/ScriptingIT.kt`** -> AI Confidence: **99.48%**
4014. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/SimpleKotlinGradleIT.kt`** -> AI Confidence: **99.48%**
4015. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/TaskExecutionDiagnosticsIT.kt`** -> AI Confidence: **99.48%**
4016. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/TaskOutputsBackupIT.kt`** -> AI Confidence: **99.48%**
4017. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/TestFixturesIT.kt`** -> AI Confidence: **99.48%**
4018. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/UpToDateIT.kt`** -> AI Confidence: **99.48%**
4019. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/WasmPackageManagerGradlePluginIT.kt`** -> AI Confidence: **99.48%**
4020. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/ExternalAndroidTargetIT.kt`** -> AI Confidence: **99.48%**
4021. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KT50161AndroidBuildCacheTest.kt`** -> AI Confidence: **99.48%**
4022. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KaptAndroidExternalIT.kt`** -> AI Confidence: **99.48%**
4023. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KaptAndroidIT.kt`** -> AI Confidence: **99.48%**
4024. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KaptAndroidIncrementalIT.kt`** -> AI Confidence: **99.48%**
4025. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KotlinAndroidIT.kt`** -> AI Confidence: **99.48%**
4026. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KotlinAndroidMppCompilationIT.kt`** -> AI Confidence: **99.48%**
4027. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/android/KotlinAndroidMppPublicationIT.kt`** -> AI Confidence: **99.48%**
4028. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/ApplePrivacyManifestIT.kt`** -> AI Confidence: **99.48%**
4029. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/CheckXcodeTargetsConfigurationIT.kt`** -> AI Confidence: **99.48%**
4030. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportIdeModelTests.kt`** -> AI Confidence: **99.48%**
4031. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportKotlinNativeTestTask.kt`** -> AI Confidence: **99.48%**
4032. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportPersistentPackageLockIntegrationTests.kt`** -> AI Confidence: **99.48%**
4033. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportPopularSwiftPMDependenciesTests.kt`** -> AI Confidence: **99.48%**
4034. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportXcodeIntegrationIT.kt`** -> AI Confidence: **99.48%**
4035. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/XcodeDirectIntegrationIT.kt`** -> AI Confidence: **99.48%**
4036. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/XcodeDirectIntegrationUpgradeSequenceIT.kt`** -> AI Confidence: **99.48%**
4037. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/spmImportTestUtils.kt`** -> AI Confidence: **99.48%**
4038. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/experimental/TryNextIT.kt`** -> AI Confidence: **99.48%**
4039. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/CommonCodeWithPlatformSymbolsIT.kt`** -> AI Confidence: **99.48%**
4040. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/KmpIncrementalCompilationMiscIT.kt`** -> AI Confidence: **99.48%**
4041. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppCompilerPluginsIT.kt`** -> AI Confidence: **99.48%**
4042. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppCompositeBuildIT.kt`** -> AI Confidence: **99.48%**
4043. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppCrossCompilationPublicationIT.kt`** -> AI Confidence: **99.48%**
4044. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppDiagnosticsIt.kt`** -> AI Confidence: **99.48%**
4045. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppDslAppAndLibIT.kt`** -> AI Confidence: **99.48%**
4046. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppDslAssociateCompilationsIT.kt`** -> AI Confidence: **99.48%**
4047. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppDslPomIT.kt`** -> AI Confidence: **99.48%**
4048. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppDslSourcesJarIT.kt`** -> AI Confidence: **99.48%**
4049. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppJvmWithJavaIT.kt`** -> AI Confidence: **99.48%**
4050. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppMetadataResolutionIT.kt`** -> AI Confidence: **99.48%**
4051. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppOptionalExpectationIT.kt`** -> AI Confidence: **99.48%**
4052. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppSharedNativeCompileIT.kt`** -> AI Confidence: **99.48%**
4053. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppTestsIT.kt`** -> AI Confidence: **99.48%**
4054. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/MppUnsupportedKotlinNativeHostIT.kt`** -> AI Confidence: **99.48%**
4055. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/SeparateKmpCompilationIT.kt`** -> AI Confidence: **99.48%**
4056. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/TestCancellationIT.kt`** -> AI Confidence: **99.48%**
4057. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/publication/MppPublicationCompatibilityIT.kt`** -> AI Confidence: **99.48%**
4058. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/publication/prepareProjectForConsumption.kt`** -> AI Confidence: **99.48%**
4059. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/resources/AndroidMultiplatformResourcesIT.kt`** -> AI Confidence: **99.48%**
4060. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/resources/MultiplatformResourcesConsumptionIT.kt`** -> AI Confidence: **99.48%**
4061. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/resources/MultiplatformResourcesPublicationIT.kt`** -> AI Confidence: **99.48%**
4062. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/mpp/resources/publicationProject.kt`** -> AI Confidence: **99.48%**
4063. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/AppleFrameworkIT.kt`** -> AI Confidence: **99.48%**
4064. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/AppleFrameworkWithCocoapodsIT.kt`** -> AI Confidence: **99.48%**
4065. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/AppleSiliconIT.kt`** -> AI Confidence: **99.48%**
4066. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/CinteropIT.kt`** -> AI Confidence: **99.48%**
4067. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/CocoaPodsGitIT.kt`** -> AI Confidence: **99.48%**
4068. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/CocoaPodsIT.kt`** -> AI Confidence: **99.48%**
4069. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/CocoaPodsPodspecIT.kt`** -> AI Confidence: **99.48%**
4070. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/CocoaPodsXcodeIT.kt`** -> AI Confidence: **99.48%**
4071. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/FatFrameworkIT.kt`** -> AI Confidence: **99.48%**
4072. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/GeneralNativeIT.kt`** -> AI Confidence: **99.48%**
4073. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/KlibCrossCompilationNativeIT.kt`** -> AI Confidence: **99.48%**
4074. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/KotlinNativeCompilerDownloadIT.kt`** -> AI Confidence: **99.48%**
4075. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/KotlinNativeDependenciesDownloadIT.kt`** -> AI Confidence: **99.48%**
4076. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/KotlinNativeDisableCacheIT.kt`** -> AI Confidence: **99.48%**
4077. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/KotlinNativeLinkIT.kt`** -> AI Confidence: **99.48%**
4078. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/NativeDownloadAndPlatformLibsIT.kt`** -> AI Confidence: **99.48%**
4079. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/NativeDownloadAndPlatformLibsNonParallelIT.kt`** -> AI Confidence: **99.48%**
4080. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/NativeExternalDependenciesIT.kt`** -> AI Confidence: **99.48%**
4081. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/NativeIncrementalCompilationIT.kt`** -> AI Confidence: **99.48%**
4082. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/SwiftExportDslIT.kt`** -> AI Confidence: **99.48%**
4083. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/SwiftExportIT.kt`** -> AI Confidence: **99.48%**
4084. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/SwiftExportXCIT.kt`** -> AI Confidence: **99.48%**
4085. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/XCFrameworkIT.kt`** -> AI Confidence: **99.48%**
4086. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/native/XCFrameworkResourcesIT.kt`** -> AI Confidence: **99.48%**
4087. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/BuildOptions.kt`** -> AI Confidence: **99.48%**
4088. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/KGPBaseTest.kt`** -> AI Confidence: **99.48%**
4089. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/argumentProviders.kt`** -> AI Confidence: **99.48%**
4090. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/cocoapodsTestHelpers.kt`** -> AI Confidence: **99.48%**
4091. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/compilationAssertions.kt`** -> AI Confidence: **99.48%**
4092. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/daemonHelpers.kt`** -> AI Confidence: **99.48%**
4093. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/diagnosticsAssertions.kt`** -> AI Confidence: **99.48%**
4094. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/fileAssertions.kt`** -> AI Confidence: **99.48%**
4095. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/osConditions.kt`** -> AI Confidence: **99.48%**
4096. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/outputAssertions.kt`** -> AI Confidence: **99.48%**
4097. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/problemsApiTestUtils.kt`** -> AI Confidence: **99.48%**
4098. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/testAssertions.kt`** -> AI Confidence: **99.48%**
4099. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/testDsl.kt`** -> AI Confidence: **99.48%**
4100. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/testHelpers.kt`** -> AI Confidence: **99.48%**
4101. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/xCodeVersion.kt`** -> AI Confidence: **99.48%**
4102. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/xcodeTestHelpers.kt`** -> AI Confidence: **99.48%**
4103. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/testbase/xctestHelpers.kt`** -> AI Confidence: **99.48%**
4104. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/uklibs/KmpGradlePublicationMetadataIT.kt`** -> AI Confidence: **99.48%**
4105. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/uklibs/KmpResolutionIT.kt`** -> AI Confidence: **99.48%**
4106. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/uklibs/UklibConsumptionGranularMetadataTransformationIT.kt`** -> AI Confidence: **99.48%**
4107. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/uklibs/UklibConsumptionIT.kt`** -> AI Confidence: **99.48%**
4108. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/uklibs/UklibInterprojectConsumptionIT.kt`** -> AI Confidence: **99.48%**
4109. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/uklibs/UklibPublicationIT.kt`** -> AI Confidence: **99.48%**
4110. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/uklibs/resolutionTesting.kt`** -> AI Confidence: **99.48%**
4111. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/uklibs/uklibTestingUtils.kt`** -> AI Confidence: **99.48%**
4112. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/util/SwiftExportUtils.kt`** -> AI Confidence: **99.48%**
4113. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/util/jsonReportUtil.kt`** -> AI Confidence: **99.48%**
4114. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/util/reportSourceSetCommonizerDependencies.kt`** -> AI Confidence: **99.48%**
4115. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/util/resolveIdeDependencies.kt`** -> AI Confidence: **99.48%**
4116. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/AndroidProject/Android/root/kotlin/org/jetbrains/kotlin/gradle/test/androidalfa/MainActivity2.kt`** -> AI Confidence: **99.48%**
4117. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/AndroidSimpleComposeApp/src/main/java/org/jetbrains/kotlin/android/example/ui/theme/Theme.kt`** -> AI Confidence: **99.48%**
4118. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/compilerPlugins/incrementalChangeInPlugin/plugin/src/main/kotlin/test/compiler/plugin/MyMethodGenerator.kt`** -> AI Confidence: **99.48%**
4119. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/android-databinding/app/src/main/java/com/example/databinding/EnumAdapter.kt`** -> AI Confidence: **99.48%**
4120. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/android-databinding/library/src/main/java/org/maw/library/TestView.kt`** -> AI Confidence: **99.48%**
4121. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/android-dbflow/app/src/main/java/mobi/porquenao/poc/kotlin/ui/BaseActivity.kt`** -> AI Confidence: **99.48%**
4122. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/android-dbflow/app/src/main/java/mobi/porquenao/poc/kotlin/ui/MainAdapter.kt`** -> AI Confidence: **99.48%**
4123. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/android-realm/src/main/java/io/realm/examples/kotlin/KotlinExampleActivity.kt`** -> AI Confidence: **99.48%**
4124. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/androidx-navigation-safe-args/src/main/java/test/androidx/navigation/DestinationFragment1.kt`** -> AI Confidence: **99.48%**
4125. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/androidx-navigation-safe-args/src/main/java/test/androidx/navigation/DestinationFragment2.kt`** -> AI Confidence: **99.48%**
4126. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/androidx-navigation-safe-args/src/main/java/test/androidx/navigation/MainActivity.kt`** -> AI Confidence: **99.48%**
4127. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/androidx-navigation-safe-args/src/main/java/test/androidx/navigation/StartFragment.kt`** -> AI Confidence: **99.48%**
4128. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/kt33847/processor/src/main/kotlin/Processor.kt`** -> AI Confidence: **99.48%**
4129. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/kapt2/localAnnotationProcessor/annotation-processor/src/main/java/TestAnnotationProcessor.kt`** -> AI Confidence: **99.48%**
4130. **`libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/scriptingComposeInterop/app/src/test/kotlin/script/ComposeMainKtsTest.kt`** -> AI Confidence: **99.48%**
4131. **`libraries/tools/kotlin-gradle-plugin-npm-versions-codegen/src/main/kotlin/org/jetbrains/kotlin/generators/gradle/targets/js/VersionFetcher.kt`** -> AI Confidence: **99.48%**
4132. **`libraries/tools/kotlin-gradle-plugin-npm-versions-codegen/src/main/kotlin/org/jetbrains/kotlin/generators/gradle/targets/js/main.kt`** -> AI Confidence: **99.48%**
4133. **`libraries/tools/kotlin-gradle-plugin-tcs-android/src/main/kotlin/org/jetbrains/kotlin/gradle/android/AndroidTargetPrototype.kt`** -> AI Confidence: **99.48%**
4134. **`libraries/tools/kotlin-gradle-plugin-tcs-android/src/main/kotlin/org/jetbrains/kotlin/gradle/android/androidBootClasspath.kt`** -> AI Confidence: **99.48%**
4135. **`libraries/tools/kotlin-gradle-plugin-tcs-android/src/main/kotlin/org/jetbrains/kotlin/gradle/android/createAndroidCompilation.kt`** -> AI Confidence: **99.48%**
4136. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/CompilerSystemPropertiesService.kt`** -> AI Confidence: **99.48%**
4137. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleCliCommonizer.kt`** -> AI Confidence: **99.48%**
4138. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleCompilationResults.kt`** -> AI Confidence: **99.48%**
4139. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleCompilerRunnerWithWorkers.kt`** -> AI Confidence: **99.48%**
4140. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleIncrementalCompilerServicesFacadeImpl.kt`** -> AI Confidence: **99.48%**
4141. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleKotlinCompilerRunner.kt`** -> AI Confidence: **99.48%**
4142. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/GradleKotlinCompilerWork.kt`** -> AI Confidence: **99.48%**
4143. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/btapi/BuildSessionService.kt`** -> AI Confidence: **99.48%**
4144. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/btapi/BuildToolsApiCompilationWork.kt`** -> AI Confidence: **99.48%**
4145. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/btapi/GradleBuildToolsApiCompilerRunner.kt`** -> AI Confidence: **99.48%**
4146. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/compilerRunner/reportUtils.kt`** -> AI Confidence: **99.48%**
4147. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/artifacts/KotlinJsKlibArtifact.kt`** -> AI Confidence: **99.48%**
4148. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/artifacts/KotlinJvmJarArtifact.kt`** -> AI Confidence: **99.48%**
4149. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/artifacts/KotlinMetadataArtifact.kt`** -> AI Confidence: **99.48%**
4150. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/artifacts/KotlinNativeHostSpecificMetadataArtifact.kt`** -> AI Confidence: **99.48%**
4151. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/artifacts/KotlinNativeKlibArtifact.kt`** -> AI Confidence: **99.48%**
4152. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/artifacts/KotlinTargetArtifact.kt`** -> AI Confidence: **99.48%**
4153. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/KotlinMultiplatformExtension.kt`** -> AI Confidence: **99.48%**
4154. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/KotlinMultiplatformSourceSetCheckers.kt`** -> AI Confidence: **99.48%**
4155. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/KotlinNativeBinaryContainer.kt`** -> AI Confidence: **99.48%**
4156. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/KotlinProjectExtension.kt`** -> AI Confidence: **99.48%**
4157. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/KotlinSourceSetConvention.kt`** -> AI Confidence: **99.48%**
4158. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/dsl/ToolchainDsl.kt`** -> AI Confidence: **99.48%**
4159. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/incremental/incrementalModuleInfo.kt`** -> AI Confidence: **99.48%**
4160. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/ClassLoadersCachingBuildService.kt`** -> AI Confidence: **99.48%**
4161. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/CompilerArgumentAware.kt`** -> AI Confidence: **99.48%**
4162. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/KotlinDependenciesManagement.kt`** -> AI Confidence: **99.48%**
4163. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/ProcessedFilesCache.kt`** -> AI Confidence: **99.48%**
4164. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/TeamCityMessageCommonClient.kt`** -> AI Confidence: **99.48%**
4165. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/compilerOptionsDslHelpers.kt`** -> AI Confidence: **99.48%**
4166. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/diagnostics/AgpWithBuiltInKotlinAppliedCheck.kt`** -> AI Confidence: **99.48%**
4167. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/exec.kt`** -> AI Confidence: **99.48%**
4168. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/Kapt3KotlinGradleSubplugin.kt`** -> AI Confidence: **99.48%**
4169. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/KaptGenerateStubsTask.kt`** -> AI Confidence: **99.48%**
4170. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/KaptTask.kt`** -> AI Confidence: **99.48%**
4171. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/KaptWithoutKotlincTask.kt`** -> AI Confidence: **99.48%**
4172. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/classloaders/ClassLoadersCache.kt`** -> AI Confidence: **99.48%**
4173. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/incremental/ClasspathAnalyzer.kt`** -> AI Confidence: **99.48%**
4174. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kotlinDomApiDependencyManagement.kt`** -> AI Confidence: **99.48%**
4175. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kotlinTestDependencyManagement.kt`** -> AI Confidence: **99.48%**
4176. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/properties/PropertiesBuildService.kt`** -> AI Confidence: **99.48%**
4177. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/stdlibDependencyManagement.kt`** -> AI Confidence: **99.48%**
4178. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/subpluginUtils.kt`** -> AI Confidence: **99.48%**
4179. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/testing/TCServiceMessageOutputStreamHandler.kt`** -> AI Confidence: **99.48%**
4180. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/testing/TCServiceMessagesClient.kt`** -> AI Confidence: **99.48%**
4181. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/testing/TCServiceMessagesTestExecutor.kt`** -> AI Confidence: **99.48%**
4182. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/transforms/ClasspathEntrySnapshotTransform.kt`** -> AI Confidence: **99.48%**
4183. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/logging/GradleErrorMessageCollector.kt`** -> AI Confidence: **99.48%**
4184. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/AbstractKotlinPlugin.kt`** -> AI Confidence: **99.48%**
4185. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/BuildFinishedListenerService.kt`** -> AI Confidence: **99.48%**
4186. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/Kotlin2JvmSourceSetProcessor.kt`** -> AI Confidence: **99.48%**
4187. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinAndroidPlugin.kt`** -> AI Confidence: **99.48%**
4188. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinBaseApiPlugin.kt`** -> AI Confidence: **99.48%**
4189. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinCommonSourceSetProcessor.kt`** -> AI Confidence: **99.48%**
4190. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinCompilationInfo.kt`** -> AI Confidence: **99.48%**
4191. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinCompilationProcessor.kt`** -> AI Confidence: **99.48%**
4192. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinGradleBuildServices.kt`** -> AI Confidence: **99.48%**
4193. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinGradleFinishBuildHandler.kt`** -> AI Confidence: **99.48%**
4194. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinJsIrSourceSetProcessor.kt`** -> AI Confidence: **99.48%**
4195. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinPluginLifecycleImpl.kt`** -> AI Confidence: **99.48%**
4196. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinPluginWrapper.kt`** -> AI Confidence: **99.48%**
4197. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinSourceSetProcessor.kt`** -> AI Confidence: **99.48%**
4198. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/KotlinTargetConfigurator.kt`** -> AI Confidence: **99.48%**
4199. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/PropertiesProvider.kt`** -> AI Confidence: **99.48%**
4200. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/StatisticsBuildFlowManager.kt`** -> AI Confidence: **99.48%**
4201. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/SubpluginEnvironment.kt`** -> AI Confidence: **99.48%**
4202. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/VariantImplementationFactories.kt`** -> AI Confidence: **99.48%**
4203. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/abi/internal/AbiValidationExtension.kt`** -> AI Confidence: **99.48%**
4204. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/abi/internal/Configs.kt`** -> AI Confidence: **99.48%**
4205. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/abi/internal/Multiplatform.kt`** -> AI Confidence: **99.48%**
4206. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/abi/internal/Utils.kt`** -> AI Confidence: **99.48%**
4207. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CheckKotlinGradlePluginConfigurationErrors.kt`** -> AI Confidence: **99.48%**
4208. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CompilerDiagnosticsProblemsReporter.kt`** -> AI Confidence: **99.48%**
4209. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/KotlinToolingDiagnostics.kt`** -> AI Confidence: **99.48%**
4210. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/KotlinToolingDiagnosticsCollector.kt`** -> AI Confidence: **99.48%**
4211. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ProblemsReporter.kt`** -> AI Confidence: **99.48%**
4212. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/StyledToolingDiagnostic.kt`** -> AI Confidence: **99.48%**
4213. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ToolingDiagnosticRenderingOptions.kt`** -> AI Confidence: **99.48%**
4214. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/AndroidPluginWithoutAndroidTargetChecker.kt`** -> AI Confidence: **99.48%**
4215. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/AndroidPublicationNotConfiguredChecker.kt`** -> AI Confidence: **99.48%**
4216. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/CInteropInputChecker.kt`** -> AI Confidence: **99.48%**
4217. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/CinteropCrossCompilationChecker.kt`** -> AI Confidence: **99.48%**
4218. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/ComposePluginSuggestApplyChecker.kt`** -> AI Confidence: **99.48%**
4219. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/ConfigurationOnDemandSupportChecker.kt`** -> AI Confidence: **99.48%**
4220. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/DeprecatedNativeHostChecker.kt`** -> AI Confidence: **99.48%**
4221. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/DisabledCinteropCommonizationInHmppProjectChecker.kt`** -> AI Confidence: **99.48%**
4222. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/GradleDeprecatedPropertyChecker.kt`** -> AI Confidence: **99.48%**
4223. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/IncorrectCompileOnlyDependenciesChecker.kt`** -> AI Confidence: **99.48%**
4224. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/InternalGradlePropertiesUsageChecker.kt`** -> AI Confidence: **99.48%**
4225. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/KmpPartiallyResolvedDependenciesChecker.kt`** -> AI Confidence: **99.48%**
4226. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/KotlinSourceSetTreeDependsOnMismatchChecker.kt`** -> AI Confidence: **99.48%**
4227. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/KotlinTargetAlreadyDeclaredChecker.kt`** -> AI Confidence: **99.48%**
4228. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/MissingNativeStdlibChecker.kt`** -> AI Confidence: **99.48%**
4229. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/MultipleSourceSetRootsInCompilationChecker.kt`** -> AI Confidence: **99.48%**
4230. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/NativeBinaryConfigurationChecker.kt`** -> AI Confidence: **99.48%**
4231. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/NativeVersionChecker.kt`** -> AI Confidence: **99.48%**
4232. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/OverriddenKotlinNativeHomeChecker.kt`** -> AI Confidence: **99.48%**
4233. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/PreHmppDependenciesUsageChecker.kt`** -> AI Confidence: **99.48%**
4234. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/SupportedNativeHostChecker.kt`** -> AI Confidence: **99.48%**
4235. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/SwiftExportModuleNameChecker.kt`** -> AI Confidence: **99.48%**
4236. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/TestApiDependenciesChecker.kt`** -> AI Confidence: **99.48%**
4237. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/UnusedSourceSetsChecker.kt`** -> AI Confidence: **99.48%**
4238. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/checkers/WasmSourceSetsNotFoundChecker.kt`** -> AI Confidence: **99.48%**
4239. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/hierarchy/KotlinHierarchyBuilderImpl.kt`** -> AI Confidence: **99.48%**
4240. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/hierarchy/RedundantDependsOnEdgesTracker.kt`** -> AI Confidence: **99.48%**
4241. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/hierarchy/defaultKotlinHierarchySetup.kt`** -> AI Confidence: **99.48%**
4242. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/IdeAdditionalArtifactResolver.kt`** -> AI Confidence: **99.48%**
4243. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/IdeMultiplatformImport.kt`** -> AI Confidence: **99.48%**
4244. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/IdeMultiplatformImportAction.kt`** -> AI Confidence: **99.48%**
4245. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/IdeMultiplatformImportFactory.kt`** -> AI Confidence: **99.48%**
4246. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/IdeMultiplatformImportImpl.kt`** -> AI Confidence: **99.48%**
4247. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/IdeResolveDependenciesTask.kt`** -> AI Confidence: **99.48%**
4248. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeArtifactResolutionQuerySourcesResolver.kt`** -> AI Confidence: **99.48%**
4249. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeBinaryDependencyResolver.kt`** -> AI Confidence: **99.48%**
4250. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeCInteropMetadataDependencyClasspathResolver.kt`** -> AI Confidence: **99.48%**
4251. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeCommonizedCinteropDependencyResolver.kt`** -> AI Confidence: **99.48%**
4252. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeCommonizedNativePlatformDependencyResolver.kt`** -> AI Confidence: **99.48%**
4253. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeDependsOnDependencyResolver.kt`** -> AI Confidence: **99.48%**
4254. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeJvmAndAndroidPlatformDependencyResolver.kt`** -> AI Confidence: **99.48%**
4255. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeJvmAndAndroidSourceDependencyResolver.kt`** -> AI Confidence: **99.48%**
4256. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeKonanDistributionLibsService.kt`** -> AI Confidence: **99.48%**
4257. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeNativeStdlibDependencyResolver.kt`** -> AI Confidence: **99.48%**
4258. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeOriginalMetadataDependencyResolver.kt`** -> AI Confidence: **99.48%**
4259. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdePlatformCinteropDependencyResolver.kt`** -> AI Confidence: **99.48%**
4260. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeProjectToProjectCInteropDependencyResolver.kt`** -> AI Confidence: **99.48%**
4261. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeSourcesVariantsResolver.kt`** -> AI Confidence: **99.48%**
4262. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeTransformedMetadataDependencyResolver.kt`** -> AI Confidence: **99.48%**
4263. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/IdeVisibleMultiplatformSourceDependencyResolver.kt`** -> AI Confidence: **99.48%**
4264. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/resolveCinteropDependency.kt`** -> AI Confidence: **99.48%**
4265. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/dependencyResolvers/resolveNativeDistributionDependency.kt`** -> AI Confidence: **99.48%**
4266. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/ide/factories.kt`** -> AI Confidence: **99.48%**
4267. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/internal/KotlinSecondaryVariantsDataSharing.kt`** -> AI Confidence: **99.48%**
4268. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/internal/MavenPublicationComponentAccessor.kt`** -> AI Confidence: **99.48%**
4269. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/AbstractKotlinTarget.kt`** -> AI Confidence: **99.48%**
4270. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/CompositeMetadataArtifactImpl.kt`** -> AI Confidence: **99.48%**
4271. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/DefaultKotlinDependencyHandler.kt`** -> AI Confidence: **99.48%**
4272. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/GenerateProjectStructureMetadata.kt`** -> AI Confidence: **99.48%**
4273. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/GranularMetadataTransformation.kt`** -> AI Confidence: **99.48%**
4274. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/InternalKotlinTarget.kt`** -> AI Confidence: **99.48%**
4275. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinCommonCompilation.kt`** -> AI Confidence: **99.48%**
4276. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinCompilationFactory.kt`** -> AI Confidence: **99.48%**
4277. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinDependencies.kt`** -> AI Confidence: **99.48%**
4278. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinLLDBScript.kt`** -> AI Confidence: **99.48%**
4279. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinMultiplatformTargetPresetSetupAction.kt`** -> AI Confidence: **99.48%**
4280. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinProjectStructureMetadata.kt`** -> AI Confidence: **99.48%**
4281. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinProjectStructureMetadataExtractorFactoryDeprecated.kt`** -> AI Confidence: **99.48%**
4282. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinSoftwareComponent.kt`** -> AI Confidence: **99.48%**
4283. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinTargetSoftwareComponentImpl.kt`** -> AI Confidence: **99.48%**
4284. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/KotlinUsages.kt`** -> AI Confidence: **99.48%**
4285. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/MetadataDependencyTransformationTask.kt`** -> AI Confidence: **99.48%**
4286. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/MetadataDependencyTransformationTaskInputs.kt`** -> AI Confidence: **99.48%**
4287. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/ModuleIds.kt`** -> AI Confidence: **99.48%**
4288. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/ProjectMetadataProviderImpl.kt`** -> AI Confidence: **99.48%**
4289. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/SourceSetVisibilityProvider.kt`** -> AI Confidence: **99.48%**
4290. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/SyncLanguageSettingsWithKotlinExtensionSetupAction.kt`** -> AI Confidence: **99.48%**
4291. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/AppleXcodeTasks.kt`** -> AI Confidence: **99.48%**
4292. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/CheckSandboxAndWriteProtectionTask.kt`** -> AI Confidence: **99.48%**
4293. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/CheckXcodeTargetsConfigurationTask.kt`** -> AI Confidence: **99.48%**
4294. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/CopyDsymDuringArchiving.kt`** -> AI Confidence: **99.48%**
4295. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/CreateBuildSystemDirectory.kt`** -> AI Confidence: **99.48%**
4296. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/SerializationTools.kt`** -> AI Confidence: **99.48%**
4297. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/SymbolicLinkToFrameworkTask.kt`** -> AI Confidence: **99.48%**
4298. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/XCFrameworkTask.kt`** -> AI Confidence: **99.48%**
4299. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/XcodeMessageReporting.kt`** -> AI Confidence: **99.48%**
4300. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/XcodeVersionService.kt`** -> AI Confidence: **99.48%**
4301. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/XcodeVersionTask.kt`** -> AI Confidence: **99.48%**
4302. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/SetupSwiftExportDSL.kt`** -> AI Confidence: **99.48%**
4303. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/SwiftExport.kt`** -> AI Confidence: **99.48%**
4304. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/SwiftExportExtension.kt`** -> AI Confidence: **99.48%**
4305. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/internal/SwiftExportAction.kt`** -> AI Confidence: **99.48%**
4306. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/internal/SwiftExportInit.kt`** -> AI Confidence: **99.48%**
4307. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/internal/SwiftExportedDependency.kt`** -> AI Confidence: **99.48%**
4308. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/internal/SwiftExportedModule.kt`** -> AI Confidence: **99.48%**
4309. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/tasks/BuildSPMSwiftExportPackage.kt`** -> AI Confidence: **99.48%**
4310. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/tasks/GenerateSPMPackageFromSwiftExport.kt`** -> AI Confidence: **99.48%**
4311. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/tasks/MergeStaticLibrariesTask.kt`** -> AI Confidence: **99.48%**
4312. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftexport/tasks/SwiftExportTask.kt`** -> AI Confidence: **99.48%**
4313. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/CheckCocoaPodsHasNoSwiftPMDependencies.kt`** -> AI Confidence: **99.48%**
4314. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/ComputeLocalPackageDependencyInputFiles.kt`** -> AI Confidence: **99.48%**
4315. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/ConvertSyntheticSwiftPMImportProjectIntoDefFile.kt`** -> AI Confidence: **99.48%**
4316. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/FetchSyntheticImportProjectPackages.kt`** -> AI Confidence: **99.48%**
4317. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/GenerateSyntheticLinkageImportProject.kt`** -> AI Confidence: **99.48%**
4318. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/SerializeSwiftPMDependenciesMetadata.kt`** -> AI Confidence: **99.48%**
4319. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/SwiftImportSetupAction.kt`** -> AI Confidence: **99.48%**
4320. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/SwiftPMImportExtension.kt`** -> AI Confidence: **99.48%**
4321. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/swiftPMDependenciesMetadata.kt`** -> AI Confidence: **99.48%**
4322. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/syncPackageSwiftLock.kt`** -> AI Confidence: **99.48%**
4323. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/xcodeIntegrations.kt`** -> AI Confidence: **99.48%**
4324. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/apple/swiftimport/xcodeProjectParsing.kt`** -> AI Confidence: **99.48%**
4325. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/applyUserDefinedAttributes.kt`** -> AI Confidence: **99.48%**
4326. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/CreateCInteropTasksSideEffect.kt`** -> AI Confidence: **99.48%**
4327. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationAssociator.kt`** -> AI Confidence: **99.48%**
4328. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationCompilerOptionsConfigurator.kt`** -> AI Confidence: **99.48%**
4329. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationFriendPathsResolver.kt`** -> AI Confidence: **99.48%**
4330. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationImpl.kt`** -> AI Confidence: **99.48%**
4331. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationK2MultiplatformConfigurator.kt`** -> AI Confidence: **99.48%**
4332. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationProcessorSideEffect.kt`** -> AI Confidence: **99.48%**
4333. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCompilationSourceSetInclusion.kt`** -> AI Confidence: **99.48%**
4334. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCreateCompilationArchiveTask.kt`** -> AI Confidence: **99.48%**
4335. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCreateLifecycleTasksSideEffect.kt`** -> AI Confidence: **99.48%**
4336. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinCreateNativeCompileTasksSideEffect.kt`** -> AI Confidence: **99.48%**
4337. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/KotlinMetadataCompilationTargetPlatformConfiguration.kt`** -> AI Confidence: **99.48%**
4338. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/factory/KotlinCompilationDependencyConfigurationsFactories.kt`** -> AI Confidence: **99.48%**
4339. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/factory/KotlinCompilationSourceSetsContainerFactories.kt`** -> AI Confidence: **99.48%**
4340. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/compilationImpl/factory/KotlinCompilerOptionsFactories.kt`** -> AI Confidence: **99.48%**
4341. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/external/ExternalKotlinCompilationDescriptor.kt`** -> AI Confidence: **99.48%**
4342. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/external/ExternalKotlinTargetComponent.kt`** -> AI Confidence: **99.48%**
4343. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/external/ExternalKotlinTargetSoftwareComponent.kt`** -> AI Confidence: **99.48%**
4344. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/external/ExternalKotlinTargetSourcesJarUtils.kt`** -> AI Confidence: **99.48%**
4345. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/external/createExternalKotlinCompilation.kt`** -> AI Confidence: **99.48%**
4346. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/external/createExternalKotlinTarget.kt`** -> AI Confidence: **99.48%**
4347. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/internal/DeprecatedMppGradlePropertiesMigrationSetupAction.kt`** -> AI Confidence: **99.48%**
4348. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/internal/ProjectStructureMetadataTransformAction.kt`** -> AI Confidence: **99.48%**
4349. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/internal/projectStructureMetadataConfiguration.kt`** -> AI Confidence: **99.48%**
4350. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/kotlinCompilations.kt`** -> AI Confidence: **99.48%**
4351. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/kotlinVariants.kt`** -> AI Confidence: **99.48%**
4352. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/metadataCompileClasspathConfiguration.kt`** -> AI Confidence: **99.48%**
4353. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/mppSourcesJar.kt`** -> AI Confidence: **99.48%**
4354. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/DefaultPomDependenciesRewriter.kt`** -> AI Confidence: **99.48%**
4355. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/ExportRootModuleCoordinates.kt`** -> AI Confidence: **99.48%**
4356. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/ExportTargetPublicationCoordinates.kt`** -> AI Confidence: **99.48%**
4357. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/PomDependenciesRewriter.kt`** -> AI Confidence: **99.48%**
4358. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/Publishing.kt`** -> AI Confidence: **99.48%**
4359. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/publishing/rewriteKmpDependenciesInPom.kt`** -> AI Confidence: **99.48%**
4360. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/AssembleHierarchicalResourcesTask.kt`** -> AI Confidence: **99.48%**
4361. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/KotlinTargetResourcesPublicationImpl.kt`** -> AI Confidence: **99.48%**
4362. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/publication/KotlinAndroidTargetResourcesPublication.kt`** -> AI Confidence: **99.48%**
4363. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/publication/KotlinJvmTargetResourcesPublication.kt`** -> AI Confidence: **99.48%**
4364. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/publication/KotlinTargetVariantResourcesPublication.kt`** -> AI Confidence: **99.48%**
4365. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/registerAssembleHierarchicalResourcesTask.kt`** -> AI Confidence: **99.48%**
4366. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/resolve/KotlinTargetResourcesResolution.kt`** -> AI Confidence: **99.48%**
4367. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/resources/resolve/ResolveResourcesFromDependenciesTask.kt`** -> AI Confidence: **99.48%**
4368. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/UklibFragmentPlatformAttribute.kt`** -> AI Confidence: **99.48%**
4369. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/consumption/UklibConsumptionSetupAction.kt`** -> AI Confidence: **99.48%**
4370. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/consumption/UnzippedUklibToPlatformCompilationTransform.kt`** -> AI Confidence: **99.48%**
4371. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/publication/ArchiveUklibTask.kt`** -> AI Confidence: **99.48%**
4372. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/publication/UklibFromKGPModel.kt`** -> AI Confidence: **99.48%**
4373. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/publication/UklibPublicationSetupAction.kt`** -> AI Confidence: **99.48%**
4374. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/publication/locateOrRegisterArchiveUklibTask.kt`** -> AI Confidence: **99.48%**
4375. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/publication/rewritePomForKotlinDomApiCompat.kt`** -> AI Confidence: **99.48%**
4376. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/serialization/uklibDeserialization.kt`** -> AI Confidence: **99.48%**
4377. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/mpp/uklibs/serialization/uklibSerialization.kt`** -> AI Confidence: **99.48%**
4378. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/registerKotlinPluginExtensions.kt`** -> AI Confidence: **99.48%**
4379. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/AbstractKotlinSourceSet.kt`** -> AI Confidence: **99.48%**
4380. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/DefaultKotlinSourceSet.kt`** -> AI Confidence: **99.48%**
4381. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/DefaultLanguageSettingsBuilder.kt`** -> AI Confidence: **99.48%**
4382. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/InternalKotlinSourceSet.kt`** -> AI Confidence: **99.48%**
4383. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/KotlinDependencyScope.kt`** -> AI Confidence: **99.48%**
4384. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/KotlinSourceSetFactory.kt`** -> AI Confidence: **99.48%**
4385. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/KotlinAndroidSourceSetFactory.kt`** -> AI Confidence: **99.48%**
4386. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/KotlinAndroidSourceSetInfo.kt`** -> AI Confidence: **99.48%**
4387. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/KotlinAndroidSourceSets.kt`** -> AI Confidence: **99.48%**
4388. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/checker/MultiplatformLayoutV2AgpRequirementChecker.kt`** -> AI Confidence: **99.48%**
4389. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/checker/MultiplatformLayoutV2AndroidStyleSourceDirUsageChecker.kt`** -> AI Confidence: **99.48%**
4390. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/sources/android/configurator/MultiplatformLayoutV2DependsOnConfigurator.kt`** -> AI Confidence: **99.48%**
4391. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/BuildFinishBuildService.kt`** -> AI Confidence: **99.48%**
4392. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/BuildFusService.kt`** -> AI Confidence: **99.48%**
4393. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/FlowActionBuildFusService.kt`** -> AI Confidence: **99.48%**
4394. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/FusMetrics.kt`** -> AI Confidence: **99.48%**
4395. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/KotlinBuildStatsBeanService.kt`** -> AI Confidence: **99.48%**
4396. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/KotlinBuildStatsLoggerService.kt`** -> AI Confidence: **99.48%**
4397. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/KotlinBuildStatsServicesRegistry.kt`** -> AI Confidence: **99.48%**
4398. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/plugin/statistics/kotlinBuildStatisticsUtils.kt`** -> AI Confidence: **99.48%**
4399. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/BuildMetricsService.kt`** -> AI Confidence: **99.48%**
4400. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/BuildReportsService.kt`** -> AI Confidence: **99.48%**
4401. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/MetricsWriter.kt`** -> AI Confidence: **99.48%**
4402. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/TaskExecutionResult.kt`** -> AI Confidence: **99.48%**
4403. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/configureReporing.kt`** -> AI Confidence: **99.48%**
4404. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/report/reportDataUtil.kt`** -> AI Confidence: **99.48%**
4405. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/scripting/internal/ScriptingGradleSubplugin.kt`** -> AI Confidence: **99.48%**
4406. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/CreateNonPackedKlibVariantsSideEffect.kt`** -> AI Confidence: **99.48%**
4407. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/CreateTargetConfigurationsSideEffect.kt`** -> AI Confidence: **99.48%**
4408. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/android/AndroidProjectHandler.kt`** -> AI Confidence: **99.48%**
4409. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/android/KotlinAndroidTarget.kt`** -> AI Confidence: **99.48%**
4410. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/android/KotlinAndroidTargetPreset.kt`** -> AI Confidence: **99.48%**
4411. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/AbstractSetupTask.kt`** -> AI Confidence: **99.48%**
4412. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/KotlinJsCompilation.kt`** -> AI Confidence: **99.48%**
4413. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/KotlinJsPlugin.kt`** -> AI Confidence: **99.48%**
4414. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/binaryen/BinaryenEnvSpec.kt`** -> AI Confidence: **99.48%**
4415. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/binaryen/BinaryenExtension.kt`** -> AI Confidence: **99.48%**
4416. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/d8/D8EnvSpec.kt`** -> AI Confidence: **99.48%**
4417. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/d8/D8Exec.kt`** -> AI Confidence: **99.48%**
4418. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/d8/D8RootExtension.kt`** -> AI Confidence: **99.48%**
4419. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/dsl/KotlinWasmTargetDsl.kt`** -> AI Confidence: **99.48%**
4420. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/dsl/WebpackRulesDsl.kt`** -> AI Confidence: **99.48%**
4421. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/internal/RewriteSourceMapFilterReader.kt`** -> AI Confidence: **99.48%**
4422. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/DefaultIncrementalSyncTask.kt`** -> AI Confidence: **99.48%**
4423. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/JsBinaries.kt`** -> AI Confidence: **99.48%**
4424. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/JsEnvironmentConfigurator.kt`** -> AI Confidence: **99.48%**
4425. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinBrowserJsIr.kt`** -> AI Confidence: **99.48%**
4426. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsBinaryContainer.kt`** -> AI Confidence: **99.48%**
4427. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsIrCompilationFactory.kt`** -> AI Confidence: **99.48%**
4428. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsIrLink.kt`** -> AI Confidence: **99.48%**
4429. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsIrSubTarget.kt`** -> AI Confidence: **99.48%**
4430. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsIrTarget.kt`** -> AI Confidence: **99.48%**
4431. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsIrTargetConfigurator.kt`** -> AI Confidence: **99.48%**
4432. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinJsIrTargetPreset.kt`** -> AI Confidence: **99.48%**
4433. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinNodeJsIr.kt`** -> AI Confidence: **99.48%**
4434. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/KotlinWasmTargetPreset.kt`** -> AI Confidence: **99.48%**
4435. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/LibraryConfigurator.kt`** -> AI Confidence: **99.48%**
4436. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/NodeJsEnvironmentConfigurator.kt`** -> AI Confidence: **99.48%**
4437. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/SwcConfigurator.kt`** -> AI Confidence: **99.48%**
4438. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/ir/WebpackConfigurator.kt`** -> AI Confidence: **99.48%**
4439. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/nodejs/NodeJsExec.kt`** -> AI Confidence: **99.48%**
4440. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/nodejs/NodeJsRootPlugin.kt`** -> AI Confidence: **99.48%**
4441. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/nodejs/NodeJsSetupTask.kt`** -> AI Confidence: **99.48%**
4442. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/AbstractNodeModulesCache.kt`** -> AI Confidence: **99.48%**
4443. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/BaseNpmExtension.kt`** -> AI Confidence: **99.48%**
4444. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/GradleNodeModulesCache.kt`** -> AI Confidence: **99.48%**
4445. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/KotlinNpmResolutionManager.kt`** -> AI Confidence: **99.48%**
4446. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/LockCopyTask.kt`** -> AI Confidence: **99.48%**
4447. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/Npm.kt`** -> AI Confidence: **99.48%**
4448. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmApiExecution.kt`** -> AI Confidence: **99.48%**
4449. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmDependency.kt`** -> AI Confidence: **99.48%**
4450. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmDependencyExtension.kt`** -> AI Confidence: **99.48%**
4451. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmExtension.kt`** -> AI Confidence: **99.48%**
4452. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/NpmProject.kt`** -> AI Confidence: **99.48%**
4453. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/resolver/KotlinCompilationNpmResolution.kt`** -> AI Confidence: **99.48%**
4454. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/resolver/KotlinCompilationNpmResolver.kt`** -> AI Confidence: **99.48%**
4455. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/resolver/KotlinProjectNpmResolver.kt`** -> AI Confidence: **99.48%**
4456. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/resolver/KotlinRootNpmResolver.kt`** -> AI Confidence: **99.48%**
4457. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/tasks/KotlinNpmInstallTask.kt`** -> AI Confidence: **99.48%**
4458. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/tasks/KotlinPackageJsonTask.kt`** -> AI Confidence: **99.48%**
4459. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/npm/tasks/KotlinToolingSetupTask.kt`** -> AI Confidence: **99.48%**
4460. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/subtargets/DefaultDistribution.kt`** -> AI Confidence: **99.48%**
4461. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/swc/GenerateSwcConfig.kt`** -> AI Confidence: **99.48%**
4462. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/swc/SwcEnvSpec.kt`** -> AI Confidence: **99.48%**
4463. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/swc/SwcExec.kt`** -> AI Confidence: **99.48%**
4464. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/swc/SwcPlugin.kt`** -> AI Confidence: **99.48%**
4465. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/JSServiceMessages.kt`** -> AI Confidence: **99.48%**
4466. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/KotlinJsTest.kt`** -> AI Confidence: **99.48%**
4467. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/KotlinJsTestFramework.kt`** -> AI Confidence: **99.48%**
4468. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/KotlinWasmD8.kt`** -> AI Confidence: **99.48%**
4469. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/KotlinWasmNode.kt`** -> AI Confidence: **99.48%**
4470. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/karma/KotlinKarma.kt`** -> AI Confidence: **99.48%**
4471. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/mocha/KotlinMocha.kt`** -> AI Confidence: **99.48%**
4472. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/typescript/TypeScriptValidationTask.kt`** -> AI Confidence: **99.48%**
4473. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/utils.kt`** -> AI Confidence: **99.48%**
4474. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpack.kt`** -> AI Confidence: **99.48%**
4475. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpackConfig.kt`** -> AI Confidence: **99.48%**
4476. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpackCssRule.kt`** -> AI Confidence: **99.48%**
4477. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpackRule.kt`** -> AI Confidence: **99.48%**
4478. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/webpack/KotlinWebpackRunner.kt`** -> AI Confidence: **99.48%**
4479. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/LockCopyTask.kt`** -> AI Confidence: **99.48%**
4480. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnBasics.kt`** -> AI Confidence: **99.48%**
4481. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnPlugin.kt`** -> AI Confidence: **99.48%**
4482. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnPluginApplier.kt`** -> AI Confidence: **99.48%**
4483. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnRootExtension.kt`** -> AI Confidence: **99.48%**
4484. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnSetupTask.kt`** -> AI Confidence: **99.48%**
4485. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/js/yarn/YarnWorkspaces.kt`** -> AI Confidence: **99.48%**
4486. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmAndroidCompilation.kt`** -> AI Confidence: **99.48%**
4487. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmAndroidCompilationFactory.kt`** -> AI Confidence: **99.48%**
4488. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmBinariesDsl.kt`** -> AI Confidence: **99.48%**
4489. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmCompilation.kt`** -> AI Confidence: **99.48%**
4490. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmCompilationFactory.kt`** -> AI Confidence: **99.48%**
4491. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmCompilationWireJavaSourcesSideEffect.kt`** -> AI Confidence: **99.48%**
4492. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmTarget.kt`** -> AI Confidence: **99.48%**
4493. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmTargetTestFixturesSideEffect.kt`** -> AI Confidence: **99.48%**
4494. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmTestRunFactory.kt`** -> AI Confidence: **99.48%**
4495. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinJvmWithJavaTargetPreset.kt`** -> AI Confidence: **99.48%**
4496. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinWithJavaCompilation.kt`** -> AI Confidence: **99.48%**
4497. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/KotlinWithJavaCompilationFactory.kt`** -> AI Confidence: **99.48%**
4498. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/jvm/tasks/KotlinJvmRun.kt`** -> AI Confidence: **99.48%**
4499. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/metadata/KotlinMetadataTargetConfigurator.kt`** -> AI Confidence: **99.48%**
4500. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/ConfigureFrameworkExportSideEffect.kt`** -> AI Confidence: **99.48%**
4501. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/DefaultCInteropSettings.kt`** -> AI Confidence: **99.48%**
4502. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KonanPropertiesBuildService.kt`** -> AI Confidence: **99.48%**
4503. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeCompilation.kt`** -> AI Confidence: **99.48%**
4504. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeConfigureBinariesSideEffect.kt`** -> AI Confidence: **99.48%**
4505. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeTarget.kt`** -> AI Confidence: **99.48%**
4506. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeTargetPreset.kt`** -> AI Confidence: **99.48%**
4507. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinNativeTestRunFactories.kt`** -> AI Confidence: **99.48%**
4508. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/KotlinSharedNativeCompilationFactory.kt`** -> AI Confidence: **99.48%**
4509. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/NativeBinaries.kt`** -> AI Confidence: **99.48%**
4510. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/NativeCompilerDownloader.kt`** -> AI Confidence: **99.48%**
4511. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/CocoapodsExtension.kt`** -> AI Confidence: **99.48%**
4512. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/KotlinCocoapodsPlugin.kt`** -> AI Confidence: **99.48%**
4513. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/AbstractPodInstallTask.kt`** -> AI Confidence: **99.48%**
4514. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/DefFileTask.kt`** -> AI Confidence: **99.48%**
4515. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/DummyFrameworkTask.kt`** -> AI Confidence: **99.48%**
4516. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/PodBuildTask.kt`** -> AI Confidence: **99.48%**
4517. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/PodGenTask.kt`** -> AI Confidence: **99.48%**
4518. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/PodInstallSyntheticTask.kt`** -> AI Confidence: **99.48%**
4519. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/PodInstallTask.kt`** -> AI Confidence: **99.48%**
4520. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/cocoapods/tasks/PodspecTask.kt`** -> AI Confidence: **99.48%**
4521. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/AbstractCInteropCommonizerTask.kt`** -> AI Confidence: **99.48%**
4522. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/AddKotlinPlatformIntegersSupportLibrary.kt`** -> AI Confidence: **99.48%**
4523. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerArtifactTypeAttribute.kt`** -> AI Confidence: **99.48%**
4524. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerConfigurations.kt`** -> AI Confidence: **99.48%**
4525. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerDependencies.kt`** -> AI Confidence: **99.48%**
4526. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerDependent.kt`** -> AI Confidence: **99.48%**
4527. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerGroup.kt`** -> AI Confidence: **99.48%**
4528. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropCommonizerTask.kt`** -> AI Confidence: **99.48%**
4529. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropConfigurations.kt`** -> AI Confidence: **99.48%**
4530. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropMetadataDependencyClasspath.kt`** -> AI Confidence: **99.48%**
4531. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropMetadataDependencyTransformationTask.kt`** -> AI Confidence: **99.48%**
4532. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CInteropPropagatedDependencies.kt`** -> AI Confidence: **99.48%**
4533. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CommonizerTasks.kt`** -> AI Confidence: **99.48%**
4534. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/CopyCInteropCommonizerTaskOutputForIdeTask.kt`** -> AI Confidence: **99.48%**
4535. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/KotlinNativeDownloadTask.kt`** -> AI Confidence: **99.48%**
4536. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/NativeAppleSimulatorTCServiceMessagesClient.kt`** -> AI Confidence: **99.48%**
4537. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/NativeDistributionCommonizerLock.kt`** -> AI Confidence: **99.48%**
4538. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/NativeDistributionCommonizerTask.kt`** -> AI Confidence: **99.48%**
4539. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/PlatformLibrariesGenerator.kt`** -> AI Confidence: **99.48%**
4540. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/SetupKotlinNativePlatformDependenciesAndStdlib.kt`** -> AI Confidence: **99.48%**
4541. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/XcodeDefaultTestDevicesValueSource.kt`** -> AI Confidence: **99.48%**
4542. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/internal/commonizerTarget.kt`** -> AI Confidence: **99.48%**
4543. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/tasks/FatFrameworkTask.kt`** -> AI Confidence: **99.48%**
4544. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/tasks/KotlinNativeCompilerArgBuilder.kt`** -> AI Confidence: **99.48%**
4545. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/tasks/KotlinNativeLink.kt`** -> AI Confidence: **99.48%**
4546. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/tasks/KotlinNativeTasks.kt`** -> AI Confidence: **99.48%**
4547. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/tasks/KotlinNativeTest.kt`** -> AI Confidence: **99.48%**
4548. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/toolchain/KotlinNativeBundleBuildService.kt`** -> AI Confidence: **99.48%**
4549. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/toolchain/KotlinNativeProvider.kt`** -> AI Confidence: **99.48%**
4550. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/toolchain/NativeToolchainProjectSetupAction.kt`** -> AI Confidence: **99.48%**
4551. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/native/toolchain/NativeVersionValueSource.kt`** -> AI Confidence: **99.48%**
4552. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/WasmBinaryPreparationSetupAction.kt`** -> AI Confidence: **99.48%**
4553. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/WasmBinaryTransformRegisteringSetupAction.kt`** -> AI Confidence: **99.48%**
4554. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/binaryen/BinaryenExec.kt`** -> AI Confidence: **99.48%**
4555. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/binaryen/BinaryenPlugin.kt`** -> AI Confidence: **99.48%**
4556. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/binaryen/BinaryenSetupTask.kt`** -> AI Confidence: **99.48%**
4557. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/d8/D8Plugin.kt`** -> AI Confidence: **99.48%**
4558. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/d8/D8SetupTask.kt`** -> AI Confidence: **99.48%**
4559. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/internal/WasmBinaryTransform.kt`** -> AI Confidence: **99.48%**
4560. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/nodejs/WasmNodeJsRootPlugin.kt`** -> AI Confidence: **99.48%**
4561. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/nodejs/WasmNpmTooling.kt`** -> AI Confidence: **99.48%**
4562. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/npm/WasmNpmExtension.kt`** -> AI Confidence: **99.48%**
4563. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/yarn/WasmYarnPlugin.kt`** -> AI Confidence: **99.48%**
4564. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/wasm/yarn/WasmYarnRootExtension.kt`** -> AI Confidence: **99.48%**
4565. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/nodejs/BaseNodeJsEnvSpec.kt`** -> AI Confidence: **99.48%**
4566. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/nodejs/BaseNodeJsRootExtension.kt`** -> AI Confidence: **99.48%**
4567. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/nodejs/NodeJsPluginApplier.kt`** -> AI Confidence: **99.48%**
4568. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/nodejs/NodeJsRootPluginApplier.kt`** -> AI Confidence: **99.48%**
4569. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/yarn/BaseYarnRootEnvSpec.kt`** -> AI Confidence: **99.48%**
4570. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/targets/web/yarn/BaseYarnRootExtension.kt`** -> AI Confidence: **99.48%**
4571. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/AbstractKotlinCompile.kt`** -> AI Confidence: **99.48%**
4572. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/CleanDataTask.kt`** -> AI Confidence: **99.48%**
4573. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/DefaultKotlinJavaToolchain.kt`** -> AI Confidence: **99.48%**
4574. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/GradleCompileTaskProvider.kt`** -> AI Confidence: **99.48%**
4575. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/K2MultiplatformStructure.kt`** -> AI Confidence: **99.48%**
4576. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/Kotlin2JsCompile.kt`** -> AI Confidence: **99.48%**
4577. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/KotlinCompile.kt`** -> AI Confidence: **99.48%**
4578. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/KotlinCompileCommon.kt`** -> AI Confidence: **99.48%**
4579. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/KotlinTest.kt`** -> AI Confidence: **99.48%**
4580. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/TasksOutputsBackup.kt`** -> AI Confidence: **99.48%**
4581. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/TasksProvider.kt`** -> AI Confidence: **99.48%**
4582. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/abi/KotlinAbiCheckTaskImpl.kt`** -> AI Confidence: **99.48%**
4583. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/abi/KotlinAbiUpdateTask.kt`** -> AI Confidence: **99.48%**
4584. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/AbstractKotlinCompileConfig.kt`** -> AI Confidence: **99.48%**
4585. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/KaptConfig.kt`** -> AI Confidence: **99.48%**
4586. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/KaptGenerateStubsConfig.kt`** -> AI Confidence: **99.48%**
4587. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/Kotlin2JsCompileConfig.kt`** -> AI Confidence: **99.48%**
4588. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/KotlinCompileConfig.kt`** -> AI Confidence: **99.48%**
4589. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/configuration/KotlinJsIrLinkConfig.kt`** -> AI Confidence: **99.48%**
4590. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/internal/CleanableStoreImpl.kt`** -> AI Confidence: **99.48%**
4591. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/publishing/CheckPomTask.kt`** -> AI Confidence: **99.48%**
4592. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/publishing/CheckSigningTask.kt`** -> AI Confidence: **99.48%**
4593. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/publishing/GeneratePgpKeys.kt`** -> AI Confidence: **99.48%**
4594. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/publishing/UploadPgpKeyTask.kt`** -> AI Confidence: **99.48%**
4595. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/publishing/helpers.kt`** -> AI Confidence: **99.48%**
4596. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tasks/tasksUtils.kt`** -> AI Confidence: **99.48%**
4597. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/testing/internal/KotlinTestReport.kt`** -> AI Confidence: **99.48%**
4598. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/testing/internal/KotlinTestsRegistry.kt`** -> AI Confidence: **99.48%**
4599. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/testing/internal/TestReportService.kt`** -> AI Confidence: **99.48%**
4600. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/tooling/BuildKotlinToolingMetadataTask.kt`** -> AI Confidence: **99.48%**
4601. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/CurrentBuildIdentifier.kt`** -> AI Confidence: **99.48%**
4602. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/Future.kt`** -> AI Confidence: **99.48%**
4603. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/LazyResolvedConfigurationComponent.kt`** -> AI Confidence: **99.48%**
4604. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/LazyResolvedConfigurationWithArtifacts.kt`** -> AI Confidence: **99.48%**
4605. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/cacheKlibUtils.kt`** -> AI Confidence: **99.48%**
4606. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/compilerOptions.kt`** -> AI Confidence: **99.48%**
4607. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/configurations.kt`** -> AI Confidence: **99.48%**
4608. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/fileUtils.kt`** -> AI Confidence: **99.48%**
4609. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/gradleConfigurationUtils.kt`** -> AI Confidence: **99.48%**
4610. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/gradleUtils.kt`** -> AI Confidence: **99.48%**
4611. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/klibUtils.kt`** -> AI Confidence: **99.48%**
4612. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/processes/ExecAsyncHandle.kt`** -> AI Confidence: **99.48%**
4613. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/providerApiUtils.kt`** -> AI Confidence: **99.48%**
4614. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/reportUtils.kt`** -> AI Confidence: **99.48%**
4615. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/resourceUtils.kt`** -> AI Confidence: **99.48%**
4616. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/storedProperty.kt`** -> AI Confidence: **99.48%**
4617. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/internal/compilerRunner/native/KotlinNativeToolRunner.kt`** -> AI Confidence: **99.48%**
4618. **`libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/internal/compilerRunner/native/nativeCompilerRunner.kt`** -> AI Confidence: **99.48%**
4619. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/KotlinTopLevelDependenciesTest.kt`** -> AI Confidence: **99.48%**
4620. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/LazyResolvedConfigurationTest.kt`** -> AI Confidence: **99.48%**
4621. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/ResolvableMetadataConfigurationTest.kt`** -> AI Confidence: **99.48%**
4622. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/SourceSetDependenciesResolution.kt`** -> AI Confidence: **99.48%**
4623. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/StdlibVersionAlignmentTest.kt`** -> AI Confidence: **99.48%**
4624. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/ExternalAndroidTargetPrototypeSmokeTest.kt`** -> AI Confidence: **99.48%**
4625. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeAndroidDependencyResolutionTest.kt`** -> AI Confidence: **99.48%**
4626. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeBinaryDependencyResolverTest.kt`** -> AI Confidence: **99.48%**
4627. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeJvmAndAndroidDependencyResolutionTest.kt`** -> AI Confidence: **99.48%**
4628. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeKotlinTestResolutionTest.kt`** -> AI Confidence: **99.48%**
4629. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeNativePlatformDependencyResolverTest.kt`** -> AI Confidence: **99.48%**
4630. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeOpaqueFileDependencyResolutionTest.kt`** -> AI Confidence: **99.48%**
4631. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeSourceSetConstraintTest.kt`** -> AI Confidence: **99.48%**
4632. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/IdeSourcesAndDocumentationResolutionTest.kt`** -> AI Confidence: **99.48%**
4633. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/PrepareKotlinIdeaImportTaskTest.kt`** -> AI Confidence: **99.48%**
4634. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/dependencyResolutionTests/tcs/StdlibJsExplicitDependencyResolutionTest.kt`** -> AI Confidence: **99.48%**
4635. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/ArchiveReproducibilityTest.kt`** -> AI Confidence: **99.48%**
4636. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/ConfigurationsTest.kt`** -> AI Confidence: **99.48%**
4637. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/JvmAndAndroidIntermediateSourceSetTest.kt`** -> AI Confidence: **99.48%**
4638. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT37051CInteropArtifactTest.kt`** -> AI Confidence: **99.48%**
4639. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT41506WithJavaSourceSet.kt`** -> AI Confidence: **99.48%**
4640. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT56143CinteropConfigurationAttributes.kt`** -> AI Confidence: **99.48%**
4641. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT58280JvmWithJavaTestCompileClasspath.kt`** -> AI Confidence: **99.48%**
4642. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT60388PlainJvmDependingOnJvmWithJavaTest.kt`** -> AI Confidence: **99.48%**
4643. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT61376CInteropCommonizerConfigurationsTest.kt`** -> AI Confidence: **99.48%**
4644. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT61652AddSourceSetInSubpluginAndEarlyTaskMaterialization.kt`** -> AI Confidence: **99.48%**
4645. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT67636JvmWithJavaSetSrcDirsTest.kt`** -> AI Confidence: **99.48%**
4646. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT69330StableFriendPathsArchiveTaskDependencyTest.kt`** -> AI Confidence: **99.48%**
4647. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT71206AssociatedCompilationDependencyBump.kt`** -> AI Confidence: **99.48%**
4648. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KT71398KotlinNativeBundleConfigurationOnUnsupportedPlatform.kt`** -> AI Confidence: **99.48%**
4649. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KTIJ25227CompilerArgumentsIdeCompatibilityTest.kt`** -> AI Confidence: **99.48%**
4650. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/regressionTests/KotlinJvmFunctionalTest.kt`** -> AI Confidence: **99.48%**
4651. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/AssembleHierarchicalResourcesTaskSourceSetWalkTests.kt`** -> AI Confidence: **99.48%**
4652. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/AssembleHierarchicalResourcesTaskTests.kt`** -> AI Confidence: **99.48%**
4653. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/BuildKotlinToolingMetadataTest.kt`** -> AI Confidence: **99.48%**
4654. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CInteropCommonizerConfigurationTests.kt`** -> AI Confidence: **99.48%**
4655. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CInteropCommonizerTaskTest.kt`** -> AI Confidence: **99.48%**
4656. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CInteropMetadataDependencyTransformationTaskTest.kt`** -> AI Confidence: **99.48%**
4657. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CocoapodsUnitTests.kt`** -> AI Confidence: **99.48%**
4658. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CommonizerTaskTests.kt`** -> AI Confidence: **99.48%**
4659. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CompilationSpecificPluginPath.kt`** -> AI Confidence: **99.48%**
4660. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CompilerArgumentsLogLevelTest.kt`** -> AI Confidence: **99.48%**
4661. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CompositeMetadataArtifactTest.kt`** -> AI Confidence: **99.48%**
4662. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ConfigurationOnDemandSupportValidationTest.kt`** -> AI Confidence: **99.48%**
4663. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/CrossCompilationWithCinteropTests.kt`** -> AI Confidence: **99.48%**
4664. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/DefaultHierarchySetupTest.kt`** -> AI Confidence: **99.48%**
4665. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/DisabledCInteropCommonizationWarningTest.kt`** -> AI Confidence: **99.48%**
4666. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/DisabledNativeCacheTest.kt`** -> AI Confidence: **99.48%**
4667. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/EmbedAndSignTaskTests.kt`** -> AI Confidence: **99.48%**
4668. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ExternalKotlinTargetApiTests.kt`** -> AI Confidence: **99.48%**
4669. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ExternalKotlinTargetSourcesJarUtilsTest.kt`** -> AI Confidence: **99.48%**
4670. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/IdeKotilnCompilerArgumentsResolverTest.kt`** -> AI Confidence: **99.48%**
4671. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/IdeMultiplatformImportActionTest.kt`** -> AI Confidence: **99.48%**
4672. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/JvmSecondaryOutgoingVariantsTest.kt`** -> AI Confidence: **99.48%**
4673. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/K2MultiplatformStructureTest.kt`** -> AI Confidence: **99.48%**
4674. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KaptApiTest.kt`** -> AI Confidence: **99.48%**
4675. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KmpDslSourceSetDiagnosticsTest.kt`** -> AI Confidence: **99.48%**
4676. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KmpPartiallyResolvedDependenciesCheckerTests.kt`** -> AI Confidence: **99.48%**
4677. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinAndroidDependsOnEdgesTest.kt`** -> AI Confidence: **99.48%**
4678. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinAndroidTargetResourcesPublicationTests.kt`** -> AI Confidence: **99.48%**
4679. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinCompilationArchiveTasksTest.kt`** -> AI Confidence: **99.48%**
4680. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinCompileToolTest.kt`** -> AI Confidence: **99.48%**
4681. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinHierarchyBuilderTest.kt`** -> AI Confidence: **99.48%**
4682. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinHierarchyDslTest.kt`** -> AI Confidence: **99.48%**
4683. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinHierarchyTemplateTest.kt`** -> AI Confidence: **99.48%**
4684. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinJvmRunTest.kt`** -> AI Confidence: **99.48%**
4685. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinJvmTargetResourcesPublicationTests.kt`** -> AI Confidence: **99.48%**
4686. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinMetadataTargetCompilationsTest.kt`** -> AI Confidence: **99.48%**
4687. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinMultiplatformSourceSetConventionsTest.kt`** -> AI Confidence: **99.48%**
4688. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinNativeLinkTest.kt`** -> AI Confidence: **99.48%**
4689. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinNativeToolchainTest.kt`** -> AI Confidence: **99.48%**
4690. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinPluginLifecycleTest.kt`** -> AI Confidence: **99.48%**
4691. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinPublishingAdhocSoftwareComponentTest.kt`** -> AI Confidence: **99.48%**
4692. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinSubpluginApiTest.kt`** -> AI Confidence: **99.48%**
4693. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinTargetResourcesPublicationImplTests.kt`** -> AI Confidence: **99.48%**
4694. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinTargetVariantResourcesPublicationTests.kt`** -> AI Confidence: **99.48%**
4695. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/KotlinTargetVariantResourcesResolutionTests.kt`** -> AI Confidence: **99.48%**
4696. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/LanguageSettingsTests.kt`** -> AI Confidence: **99.48%**
4697. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/LifecycleAwaitFinalPropertyValueTest.kt`** -> AI Confidence: **99.48%**
4698. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/MachOTest.kt`** -> AI Confidence: **99.48%**
4699. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/MppPublicationTest.kt`** -> AI Confidence: **99.48%**
4700. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/MultiplatformIncorrectCompileOnlyDependenciesValidationTest.kt`** -> AI Confidence: **99.48%**
4701. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/MultiplatformSecondaryOutgoingVariantsTest.kt`** -> AI Confidence: **99.48%**
4702. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/NativeDistributionCommonizerLockTest.kt`** -> AI Confidence: **99.48%**
4703. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/PluginManagerUtilTest.kt`** -> AI Confidence: **99.48%**
4704. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ProjectCompilerOptionsTests.kt`** -> AI Confidence: **99.48%**
4705. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/PropertiesBuildServiceTest.kt`** -> AI Confidence: **99.48%**
4706. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/PublishJvmEnvironmentAttributeTest.kt`** -> AI Confidence: **99.48%**
4707. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ResourcesTasksTest.kt`** -> AI Confidence: **99.48%**
4708. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/SerializationToolsTest.kt`** -> AI Confidence: **99.48%**
4709. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/SwiftExportUnitTests.kt`** -> AI Confidence: **99.48%**
4710. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/SwiftPMImportIdeModelTests.kt`** -> AI Confidence: **99.48%**
4711. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/SwiftPMImportUnitTests.kt`** -> AI Confidence: **99.48%**
4712. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/TestApiDependenciesCheckerTest.kt`** -> AI Confidence: **99.48%**
4713. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/TestFixturesTest.kt`** -> AI Confidence: **99.48%**
4714. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/WhenEvaluatedTest.kt`** -> AI Confidence: **99.48%**
4715. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/XCFrameworkCocoaPodsTest.kt`** -> AI Confidence: **99.48%**
4716. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/XCFrameworkTaskTest.kt`** -> AI Confidence: **99.48%**
4717. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/ZipUtilsTest.kt`** -> AI Confidence: **99.48%**
4718. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/checkers/AgpCompatibilityCheckTest.kt`** -> AI Confidence: **99.48%**
4719. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/checkers/AgpWithBuiltInKotlinAppliedCheckTest.kt`** -> AI Confidence: **99.48%**
4720. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/compilerArgumetns/Kotlin2JsCompileArgumentsTest.kt`** -> AI Confidence: **99.48%**
4721. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/compilerArgumetns/KotlinCompileArgumentsTest.kt`** -> AI Confidence: **99.48%**
4722. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/compilerArgumetns/KotlinCompileCommonArgumentsTest.kt`** -> AI Confidence: **99.48%**
4723. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/compilerArgumetns/KotlinNativeCompileArgumentsTest.kt`** -> AI Confidence: **99.48%**
4724. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/AndroidPublicationNotConfiguredTest.kt`** -> AI Confidence: **99.48%**
4725. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/CompilerDiagnosticsProblemsReporterHelpersTest.kt`** -> AI Confidence: **99.48%**
4726. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/DiagnosticsReportingFunctionalTest.kt`** -> AI Confidence: **99.48%**
4727. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/KMPWithAndroidDiagnosticsTest.kt`** -> AI Confidence: **99.48%**
4728. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/KotlinSourceSetTreeDependsOnMismatchTest.kt`** -> AI Confidence: **99.48%**
4729. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/SourceSetsAccessInAndroidExtensionTest.kt`** -> AI Confidence: **99.48%**
4730. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/ToolingDiagnosticOutputTest.kt`** -> AI Confidence: **99.48%**
4731. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/diagnosticsTests/WasmSourceSetsNotFoundErrorTest.kt`** -> AI Confidence: **99.48%**
4732. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/fus/FUSGeneratedSourcesTest.kt`** -> AI Confidence: **99.48%**
4733. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/fus/FUSWebMainSourceSetTest.kt`** -> AI Confidence: **99.48%**
4734. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/fus/FUSWebTestSourceSetTest.kt`** -> AI Confidence: **99.48%**
4735. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/fus/fusTestUtils.kt`** -> AI Confidence: **99.48%**
4736. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/jvm/JvmFirIncrementalCompilationTest.kt`** -> AI Confidence: **99.48%**
4737. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/report/ConfigureReportingTest.kt`** -> AI Confidence: **99.48%**
4738. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/sourceSets/DefaultKotlinSourceSetTest.kt`** -> AI Confidence: **99.48%**
4739. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/sources/SourceSetVisibilityFromAssociatedCompilationsTest.kt`** -> AI Confidence: **99.48%**
4740. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/sources/android/MultiplatformAndroidSourceSetLayoutV2Test.kt`** -> AI Confidence: **99.48%**
4741. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/sources/android/getKotlinSourceSetOrFail.kt`** -> AI Confidence: **99.48%**
4742. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/uklibs/ResolutionTestingTests.kt`** -> AI Confidence: **99.48%**
4743. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/uklibs/UklibDeserializationTests.kt`** -> AI Confidence: **99.48%**
4744. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/uklibs/UklibFromKGPFragmentsTests.kt`** -> AI Confidence: **99.48%**
4745. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/uklibs/UklibInterprojectResolutionTests.kt`** -> AI Confidence: **99.48%**
4746. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/uklibs/UklibResolutionWithMockComponents.kt`** -> AI Confidence: **99.48%**
4747. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/unitTests/uklibs/generateMockRepository.kt`** -> AI Confidence: **99.48%**
4748. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/MultiplatformExtensionTest.kt`** -> AI Confidence: **99.48%**
4749. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/assertions.kt`** -> AI Confidence: **99.48%**
4750. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/buildProject.kt`** -> AI Confidence: **99.48%**
4751. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/diagnosticUtils.kt`** -> AI Confidence: **99.48%**
4752. **`libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/utils/processes/ExecAsyncHandleTest.kt`** -> AI Confidence: **99.48%**
4753. **`libraries/tools/kotlin-gradle-plugin/src/gradle811/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CompilerDiagnosticsProblemsReporterG811.kt`** -> AI Confidence: **99.48%**
4754. **`libraries/tools/kotlin-gradle-plugin/src/gradle811/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ProblemsReporterG811.kt`** -> AI Confidence: **99.48%**
4755. **`libraries/tools/kotlin-gradle-plugin/src/gradle82/kotlin/org/jetbrains/kotlin/gradle/plugin/PluginWrappers.kt`** -> AI Confidence: **99.48%**
4756. **`libraries/tools/kotlin-gradle-plugin/src/gradle86/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CompilerDiagnosticsProblemsReporterG86.kt`** -> AI Confidence: **99.48%**
4757. **`libraries/tools/kotlin-gradle-plugin/src/gradle86/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ProblemsReporterG86.kt`** -> AI Confidence: **99.48%**
4758. **`libraries/tools/kotlin-gradle-plugin/src/gradle88/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/CompilerDiagnosticsProblemsReporterG88.kt`** -> AI Confidence: **99.48%**
4759. **`libraries/tools/kotlin-gradle-plugin/src/gradle88/kotlin/org/jetbrains/kotlin/gradle/plugin/diagnostics/ProblemsReporterG88.kt`** -> AI Confidence: **99.48%**
4760. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/classloaders/ClassLoadersCacheTest.kt`** -> AI Confidence: **99.48%**
4761. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/incremental/ClassAbiExtractorTest.kt`** -> AI Confidence: **99.48%**
4762. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/incremental/ClassTypeExtractorVisitorTest.kt`** -> AI Confidence: **99.48%**
4763. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/incremental/ClasspathAnalyzerTest.kt`** -> AI Confidence: **99.48%**
4764. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/incremental/ClasspathSnapshotTest.kt`** -> AI Confidence: **99.48%**
4765. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/internal/testing/TCServiceMessageOutputStreamHandlerTest.kt`** -> AI Confidence: **99.48%**
4766. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/internal/testing/tcsmc/TCServiceMessagesClientTest.kt`** -> AI Confidence: **99.48%**
4767. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/plugin/BuildFinishedListenerServiceLincheckTest.kt`** -> AI Confidence: **99.48%**
4768. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/statistics/BuildSessionLoggerTest.kt`** -> AI Confidence: **99.48%**
4769. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/targets/js/testing/karma/KotlinKarmaTest.kt`** -> AI Confidence: **99.48%**
4770. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/targets/native/toolchain/NativeVersionValueSourceTest.kt`** -> AI Confidence: **99.48%**
4771. **`libraries/tools/kotlin-gradle-plugin/src/test/kotlin/org/jetbrains/kotlin/gradle/utils/CastIsolatedKotlinPluginClassLoaderAwareTest.kt`** -> AI Confidence: **99.48%**
4772. **`libraries/tools/kotlin-gradle-plugin/src/testFixtures/kotlin/org/jetbrains/kotlin/gradle/testing/ResolutionTesting.kt`** -> AI Confidence: **99.48%**
4773. **`libraries/tools/kotlin-gradle-statistics/src/main/kotlin/org/jetbrains/kotlin/statistics/BuildSessionLogger.kt`** -> AI Confidence: **99.48%**
4774. **`libraries/tools/kotlin-gradle-statistics/src/main/kotlin/org/jetbrains/kotlin/statistics/fileloggers/MetricsContainer.kt`** -> AI Confidence: **99.48%**
4775. **`libraries/tools/kotlin-gradle-statistics/src/test/kotlin/org/jetbrains/kotlin/statistics/ModuleChangesCatchingTest.kt`** -> AI Confidence: **99.48%**
4776. **`libraries/tools/kotlin-main-kts-test/test/org/jetbrains/kotlin/mainKts/test/mainKtsIT.kt`** -> AI Confidence: **99.48%**
4777. **`libraries/tools/kotlin-main-kts-test/test/org/jetbrains/kotlin/mainKts/test/mainKtsTest.kt`** -> AI Confidence: **99.48%**
4778. **`libraries/tools/kotlin-main-kts/src/org/jetbrains/kotlin/mainKts/jsr223/KotlinJsr223MainKtsScriptEngineFactory.kt`** -> AI Confidence: **99.48%**
4779. **`libraries/tools/kotlin-maven-plugin-test/src/it/test-kapt-annotationProcessorPaths-without-version/annotation-processor-second-version/src/main/kotlin/ExampleAnnotationProcessor.kt`** -> AI Confidence: **99.48%**
4780. **`libraries/tools/kotlin-maven-plugin-test/src/it/test-kapt-generateKotlinCode/annotation-processor/src/main/kotlin/ExampleAnnotationProcessor.kt`** -> AI Confidence: **99.48%**
4781. **`libraries/tools/kotlin-maven-plugin-test/src/it/test-lombok-with-kapt/annotation-processor/src/main/kotlin/DualGeneratorProcessor.kt`** -> AI Confidence: **99.48%**
4782. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/MavenTestArgumentsProvider.kt`** -> AI Confidence: **99.48%**
4783. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/MavenTestExecutionContext.kt`** -> AI Confidence: **99.48%**
4784. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/MavenVerifierExtensions.kt`** -> AI Confidence: **99.48%**
4785. **`libraries/tools/kotlin-maven-plugin-test/src/test/kotlin/org/jetbrains/kotlin/maven/test/jdk/LinuxJdkProvider.kt`** -> AI Confidence: **99.48%**
4786. **`libraries/tools/kotlin-privacy-manifests-plugin/src/main/kotlin/PrivacyManifestsPlugin.kt`** -> AI Confidence: **99.48%**
4787. **`libraries/tools/kotlin-stdlib-docs/plugins/dokka-version-filter-plugin/src/main/kotlin/org/jetbrains/dokka/kotlinlang/VersionFilterTransformer.kt`** -> AI Confidence: **99.48%**
4788. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/GenerateUnicodeData.kt`** -> AI Confidence: **99.48%**
4789. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/mappings/oneToMany/OneToManyMappingsGenerator.kt`** -> AI Confidence: **99.48%**
4790. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/mappings/oneToOne/MappingsGenerator.kt`** -> AI Confidence: **99.48%**
4791. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/mappings/string/StringCasingTestGenerator.kt`** -> AI Confidence: **99.48%**
4792. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/mappings/string/StringLowercaseGenerator.kt`** -> AI Confidence: **99.48%**
4793. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/ranges/OtherLowercaseRangesGenerator.kt`** -> AI Confidence: **99.48%**
4794. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/ranges/OtherUppercaseRangesGenerator.kt`** -> AI Confidence: **99.48%**
4795. **`libraries/tools/kotlin-stdlib-gen/src/generators/unicode/ranges/RangesGenerator.kt`** -> AI Confidence: **99.48%**
4796. **`libraries/tools/kotlin-tooling-core/src/test/kotlin/org/jetbrains/kotlin/tooling/core/ExtrasSerializableTest.kt`** -> AI Confidence: **99.48%**
4797. **`libraries/tools/kotlinp/jvm/src/org/jetbrains/kotlin/kotlinp/jvm/utils.kt`** -> AI Confidence: **99.48%**
4798. **`libraries/tools/kotlinp/jvm/testFixtures/org/jetbrains/kotlin/kotlinp/jvm/test/CompareMetadataHandler.kt`** -> AI Confidence: **99.48%**
4799. **`libraries/tools/stats-analyser/tests/org/jetbrains/kotlin/stats/TestData.kt`** -> AI Confidence: **99.48%**
4800. **`native/analysis-api-based-test-utils/src/org/jetbrains/kotlin/export/test/AnalysisApiAssertions.kt`** -> AI Confidence: **99.48%**
4801. **`native/analysis-api-based-test-utils/src/org/jetbrains/kotlin/export/test/InlineSourceCodeAnalysisExtension.kt`** -> AI Confidence: **99.48%**
4802. **`native/analysis-api-based-test-utils/src/org/jetbrains/kotlin/export/test/createAnalysisSession.kt`** -> AI Confidence: **99.48%**
4803. **`native/base/src/main/kotlin/org/jetbrains/kotlin/backend/konan/InlineClasses.kt`** -> AI Confidence: **99.48%**
4804. **`native/base/src/main/kotlin/org/jetbrains/kotlin/backend/konan/descriptors/LegacyDescriptorUtils.kt`** -> AI Confidence: **99.48%**
4805. **`native/cli-native/src/org/jetbrains/kotlin/cli/bc/K2Native.kt`** -> AI Confidence: **99.48%**
4806. **`native/cli-native/src/org/jetbrains/kotlin/cli/bc/oneStageMode.kt`** -> AI Confidence: **99.48%**
4807. **`native/commonizer-api/test/org/jetbrains/kotlin/commonizer/utils/konanHome.kt`** -> AI Confidence: **99.48%**
4808. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/CommonizerParameters.kt`** -> AI Confidence: **99.48%**
4809. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/cir/CirName.kt`** -> AI Confidence: **99.48%**
4810. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/cir/CirProvided.kt`** -> AI Confidence: **99.48%**
4811. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/cli/nativeTasks.kt`** -> AI Confidence: **99.48%**
4812. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/AbstractFunctionOrPropertyCommonizer.kt`** -> AI Confidence: **99.48%**
4813. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/AnnotationsCommonizer.kt`** -> AI Confidence: **99.48%**
4814. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/CallableValueParametersCommonizer.kt`** -> AI Confidence: **99.48%**
4815. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/ClassOrTypeAliasTypeCommonizer.kt`** -> AI Confidence: **99.48%**
4816. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/core/PlatformIntegerCommonizer.kt`** -> AI Confidence: **99.48%**
4817. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/facade.kt`** -> AI Confidence: **99.48%**
4818. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/konan/DefaultModulesProvider.kt`** -> AI Confidence: **99.48%**
4819. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/konan/LibraryCommonizer.kt`** -> AI Confidence: **99.48%**
4820. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/mergedtree/CirClassifierIndex.kt`** -> AI Confidence: **99.48%**
4821. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/mergedtree/CirFictitiousFunctionClassifiers.kt`** -> AI Confidence: **99.48%**
4822. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/mergedtree/CirNode.kt`** -> AI Confidence: **99.48%**
4823. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/mergedtree/CirProvidedClassifiersByModules.kt`** -> AI Confidence: **99.48%**
4824. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/mergedtree/PlatformWidthIndex.kt`** -> AI Confidence: **99.48%**
4825. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/metadata/CirSerializers.kt`** -> AI Confidence: **99.48%**
4826. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/metadata/CirTreeSerializer.kt`** -> AI Confidence: **99.48%**
4827. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/metadata/flags.kt`** -> AI Confidence: **99.48%**
4828. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/metadata/utils/MetadataDeclarationsComparator.kt`** -> AI Confidence: **99.48%**
4829. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/stats/RawStatsCollector.kt`** -> AI Confidence: **99.48%**
4830. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/transformer/InlineTypeAliasCirNodeTransformer.kt`** -> AI Confidence: **99.48%**
4831. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/transformer/ReApproximationCirNodeTransformer.kt`** -> AI Confidence: **99.48%**
4832. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/tree/deserializer/CirTreeFunctionDeserializer.kt`** -> AI Confidence: **99.48%**
4833. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/tree/deserializer/CirTreeModuleDeserializer.kt`** -> AI Confidence: **99.48%**
4834. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/tree/deserializer/CirTreePropertyDeserializer.kt`** -> AI Confidence: **99.48%**
4835. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/tree/deserializer/CirTreeTypeAliasDeserializer.kt`** -> AI Confidence: **99.48%**
4836. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/tree/deserializer/RootCirTreeDeserializer.kt`** -> AI Confidence: **99.48%**
4837. **`native/commonizer/src/org/jetbrains/kotlin/commonizer/tree/mergeCirTree.kt`** -> AI Confidence: **99.48%**
4838. **`native/commonizer/tests/org/jetbrains/kotlin/commonizer/utils/InlineSourceBuilder.kt`** -> AI Confidence: **99.48%**
4839. **`native/commonizer/tests/org/jetbrains/kotlin/commonizer/utils/InlineSourceBuilderImpl.kt`** -> AI Confidence: **99.48%**
4840. **`native/commonizer/tests/org/jetbrains/kotlin/commonizer/utils/assertions.kt`** -> AI Confidence: **99.48%**
4841. **`native/commonizer/tests/org/jetbrains/kotlin/commonizer/utils/metadataCompilation.kt`** -> AI Confidence: **99.48%**
4842. **`native/commonizer/tests/org/jetbrains/kotlin/commonizer/utils/mocks.kt`** -> AI Confidence: **99.48%**
4843. **`native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/FirebaseCloudXCTestExecutor.kt`** -> AI Confidence: **99.48%**
4844. **`native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/HostExecutor.kt`** -> AI Confidence: **99.48%**
4845. **`native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/XcodeSimulatorExecutor.kt`** -> AI Confidence: **99.48%**
4846. **`native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/cli/cli.kt`** -> AI Confidence: **99.48%**
4847. **`native/frontend/src/org/jetbrains/kotlin/descriptors/konan/utils.kt`** -> AI Confidence: **99.48%**
4848. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeConflictingOverloadsDispatcher.kt`** -> AI Confidence: **99.48%**
4849. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeForwardDeclarationRttiChecker.kt`** -> AI Confidence: **99.48%**
4850. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeHiddenFromObjCInheritanceChecker.kt`** -> AI Confidence: **99.48%**
4851. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeIdentifierChecker.kt`** -> AI Confidence: **99.48%**
4852. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCNameChecker.kt`** -> AI Confidence: **99.48%**
4853. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCNameOverridesChecker.kt`** -> AI Confidence: **99.48%**
4854. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCOverrideApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
4855. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCRefinementAnnotationChecker.kt`** -> AI Confidence: **99.48%**
4856. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCRefinementChecker.kt`** -> AI Confidence: **99.48%**
4857. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeObjCRefinementOverridesChecker.kt`** -> AI Confidence: **99.48%**
4858. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeSharedImmutableChecker.kt`** -> AI Confidence: **99.48%**
4859. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeThreadLocalChecker.kt`** -> AI Confidence: **99.48%**
4860. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/diagnostics/NativeThrowsChecker.kt`** -> AI Confidence: **99.48%**
4861. **`native/frontend/src/org/jetbrains/kotlin/resolve/konan/platform/ObjCOverridabilityCondition.kt`** -> AI Confidence: **99.48%**
4862. **`native/kotlin-test-native-xctest/src/nativeMain/kotlin/NativeTestObserver.kt`** -> AI Confidence: **99.48%**
4863. **`native/kotlin-test-native-xctest/src/nativeMain/kotlin/NativeTestRunner.kt`** -> AI Confidence: **99.48%**
4864. **`native/kotlin-test-native-xctest/src/nativeMain/kotlin/configuration.kt`** -> AI Confidence: **99.48%**
4865. **`native/native.tests/stress/testData/stress_gc_allocations.kt`** -> AI Confidence: **99.48%**
4866. **`native/native.tests/testData/framework/objcexport/coroutines.kt`** -> AI Confidence: **99.48%**
4867. **`native/native.tests/testData/framework/objcexport/values.kt`** -> AI Confidence: **99.48%**
4868. **`native/native.tests/testData/gc/cleaner_basic.kt`** -> AI Confidence: **99.48%**
4869. **`native/native.tests/testData/gc/cleaner_workers.kt`** -> AI Confidence: **99.48%**
4870. **`native/native.tests/testData/gc/worker10.kt`** -> AI Confidence: **99.48%**
4871. **`native/native.tests/testData/gc/worker_bound_reference0.kt`** -> AI Confidence: **99.48%**
4872. **`native/native.tests/testData/interop/objc/friendly_dealloc/friendly_dealloc.kt`** -> AI Confidence: **99.48%**
4873. **`native/native.tests/testData/interop/objc/kt56402/kt56402.kt`** -> AI Confidence: **99.48%**
4874. **`native/native.tests/testFixtures/org/jetbrains/kotlin/generators/tests/GenerateNativeTests.kt`** -> AI Confidence: **99.48%**
4875. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/KtObjCExportFile.kt`** -> AI Confidence: **99.48%**
4876. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/KtObjCExportModuleNaming.kt`** -> AI Confidence: **99.48%**
4877. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/definedThrows.kt`** -> AI Confidence: **99.48%**
4878. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/getInlineTargetTypeOrNull.kt`** -> AI Confidence: **99.48%**
4879. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/getMethodBridge.kt`** -> AI Confidence: **99.48%**
4880. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/getObjCDocumentedAnnotations.kt`** -> AI Confidence: **99.48%**
4881. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/analysisApiUtils/isVisibleInObjC.kt`** -> AI Confidence: **99.48%**
4882. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/buildCompanionProperty.kt`** -> AI Confidence: **99.48%**
4883. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/resolveObjCNameAnnotation.kt`** -> AI Confidence: **99.48%**
4884. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToMappedObjCType.kt`** -> AI Confidence: **99.48%**
4885. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToNSEnum.kt`** -> AI Confidence: **99.48%**
4886. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCClass.kt`** -> AI Confidence: **99.48%**
4887. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCComment.kt`** -> AI Confidence: **99.48%**
4888. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCConstructor.kt`** -> AI Confidence: **99.48%**
4889. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCHeader.kt`** -> AI Confidence: **99.48%**
4890. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCMethod.kt`** -> AI Confidence: **99.48%**
4891. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCObject.kt`** -> AI Confidence: **99.48%**
4892. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCObjectType.kt`** -> AI Confidence: **99.48%**
4893. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCParameters.kt`** -> AI Confidence: **99.48%**
4894. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCProperty.kt`** -> AI Confidence: **99.48%**
4895. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCProtocol.kt`** -> AI Confidence: **99.48%**
4896. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/translateToObjCType.kt`** -> AI Confidence: **99.48%**
4897. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/valueParametersAssociated.kt`** -> AI Confidence: **99.48%**
4898. **`native/objcexport-header-generator/impl/analysis-api/src/org/jetbrains/kotlin/objcexport/withNullabilityOf.kt`** -> AI Confidence: **99.48%**
4899. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/CustomTypeMapper.kt`** -> AI Confidence: **99.48%**
4900. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportHeaderGenerator.kt`** -> AI Confidence: **99.48%**
4901. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportLazy.kt`** -> AI Confidence: **99.48%**
4902. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportMapper.kt`** -> AI Confidence: **99.48%**
4903. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportNamer.kt`** -> AI Confidence: **99.48%**
4904. **`native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportTranslator.kt`** -> AI Confidence: **99.48%**
4905. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/SirDeclarationFromKtSymbolProvider.kt`** -> AI Confidence: **99.48%**
4906. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/StubbingSirDeclarationProvider.kt`** -> AI Confidence: **99.48%**
4907. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirClassFromKtSymbol.kt`** -> AI Confidence: **99.48%**
4908. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirEnumFromKtSymbol.kt`** -> AI Confidence: **99.48%**
4909. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirFunctionFromKtPropertySymbol.kt`** -> AI Confidence: **99.48%**
4910. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirFunctionFromKtSymbol.kt`** -> AI Confidence: **99.48%**
4911. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirInitFromKtSymbol.kt`** -> AI Confidence: **99.48%**
4912. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirOperatorFromKtSymbol.kt`** -> AI Confidence: **99.48%**
4913. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirProtocolFromKtSymbol.kt`** -> AI Confidence: **99.48%**
4914. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/nodes/SirVariableFromKtSymbol.kt`** -> AI Confidence: **99.48%**
4915. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/BridgeGenerationUtils.kt`** -> AI Confidence: **99.48%**
4916. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/NameUtils.kt`** -> AI Confidence: **99.48%**
4917. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/SirOperatorTranslationStrategy.kt`** -> AI Confidence: **99.48%**
4918. **`native/swift/sir-light-classes/src/org/jetbrains/sir/lightclasses/utils/TypeTranslationUtils.kt`** -> AI Confidence: **99.48%**
4919. **`native/swift/sir-printer/src/org/jetbrains/sir/printer/SirPrinter.kt`** -> AI Confidence: **99.48%**
4920. **`native/swift/sir-printer/src/org/jetbrains/sir/printer/impl/SirAsSwiftSourcesPrinter.kt`** -> AI Confidence: **99.48%**
4921. **`native/swift/sir-printer/tests/org/jetbrains/kotlin/sir/printer/SirAsSwiftSourcesPrinterTests.kt`** -> AI Confidence: **99.48%**
4922. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/SirSession.kt`** -> AI Confidence: **99.48%**
4923. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/BridgeProvider/SirBridgeProviderImpl.kt`** -> AI Confidence: **99.48%**
4924. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/BridgeProvider/TypeBridging.kt`** -> AI Confidence: **99.48%**
4925. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/PackageFlatteningSirDeclarationProvider.kt`** -> AI Confidence: **99.48%**
4926. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirCustomTypeTranslatorImpl.kt`** -> AI Confidence: **99.48%**
4927. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirDeclarationChildrenProviderImpl.kt`** -> AI Confidence: **99.48%**
4928. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirOneToOneModuleProvider.kt`** -> AI Confidence: **99.48%**
4929. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirParentProviderImpl.kt`** -> AI Confidence: **99.48%**
4930. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirTypeProviderImpl.kt`** -> AI Confidence: **99.48%**
4931. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/SirVisibilityCheckerImpl.kt`** -> AI Confidence: **99.48%**
4932. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/StandaloneSirTypeNamer.kt`** -> AI Confidence: **99.48%**
4933. **`native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/utils/AnalysisApiUtils.kt`** -> AI Confidence: **99.48%**
4934. **`native/swift/sir/tree-generator/src/org/jetbrains/kotlin/sir/tree/generator/Main.kt`** -> AI Confidence: **99.48%**
4935. **`native/swift/sir/tree-generator/src/org/jetbrains/kotlin/sir/tree/generator/config/AbstractSwiftIrTreeBuilder.kt`** -> AI Confidence: **99.48%**
4936. **`native/swift/sir/tree-generator/src/org/jetbrains/kotlin/sir/tree/generator/printer/ElementPrinter.kt`** -> AI Confidence: **99.48%**
4937. **`native/swift/sir/tree-generator/src/org/jetbrains/kotlin/sir/tree/generator/printer/ImplementationPrinter.kt`** -> AI Confidence: **99.48%**
4938. **`native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/KotlinxCoroutinesCore/KotlinxCoroutinesCore.kt`** -> AI Confidence: **99.48%**
4939. **`native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/main/main.kt`** -> AI Confidence: **99.48%**
4940. **`native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutinesWithPackageFlattening/golden_result/main/main.kt`** -> AI Confidence: **99.48%**
4941. **`native/swift/swift-export-standalone-integration-tests/src/org/jetbrains/kotlin/swiftexport/standalone/test/AbstractSwiftExportExecutionTest.kt`** -> AI Confidence: **99.48%**
4942. **`native/swift/swift-export-standalone-integration-tests/src/org/jetbrains/kotlin/swiftexport/standalone/test/AbstractSwiftExportTest.kt`** -> AI Confidence: **99.48%**
4943. **`native/swift/swift-export-standalone-integration-tests/src/org/jetbrains/kotlin/swiftexport/standalone/test/AbstractSwiftExportWithResultValidationTest.kt`** -> AI Confidence: **99.48%**
4944. **`native/swift/swift-export-standalone-integration-tests/src/org/jetbrains/kotlin/swiftexport/standalone/test/SwiftExportValidator.kt`** -> AI Confidence: **99.48%**
4945. **`native/swift/swift-export-standalone/resources/swift/KotlinCoroutineSupport.kt`** -> AI Confidence: **99.48%**
4946. **`native/swift/swift-export-standalone/src/org/jetbrains/kotlin/swiftexport/standalone/SwiftExportRunner.kt`** -> AI Confidence: **99.48%**
4947. **`native/swift/swift-export-standalone/src/org/jetbrains/kotlin/swiftexport/standalone/builders/buildSwiftModule.kt`** -> AI Confidence: **99.48%**
4948. **`native/swift/swift-export-standalone/src/org/jetbrains/kotlin/swiftexport/standalone/session/StandaloneSirSession.kt`** -> AI Confidence: **99.48%**
4949. **`native/swift/swift-export-standalone/src/org/jetbrains/kotlin/swiftexport/standalone/translation/ModuleTranslation.kt`** -> AI Confidence: **99.48%**
4950. **`native/utils/src/org/jetbrains/kotlin/konan/library/SearchPathResolver.kt`** -> AI Confidence: **99.48%**
4951. **`native/utils/src/org/jetbrains/kotlin/konan/library/components/KlibBitcodeComponent.kt`** -> AI Confidence: **99.48%**
4952. **`native/utils/src/org/jetbrains/kotlin/konan/library/components/KlibNativeIncludedBinariesComponent.kt`** -> AI Confidence: **99.48%**
4953. **`native/utils/src/org/jetbrains/kotlin/konan/library/writer/NativeKlibWriterUtils.kt`** -> AI Confidence: **99.48%**
4954. **`native/utils/src/org/jetbrains/kotlin/konan/util/DefFile.kt`** -> AI Confidence: **99.48%**
4955. **`native/utils/src/org/jetbrains/kotlin/konan/util/DependencyDownloader.kt`** -> AI Confidence: **99.48%**
4956. **`native/utils/src/org/jetbrains/kotlin/konan/util/DependencyProcessor.kt`** -> AI Confidence: **99.48%**
4957. **`native/utils/testFixtures/org/jetbrains/kotlin/konan/library/AbstractNativeKlibWriterTest.kt`** -> AI Confidence: **99.48%**
4958. **`plugins/allopen/allopen.cli/src/org/jetbrains/kotlin/allopen/AllOpenPlugin.kt`** -> AI Confidence: **99.48%**
4959. **`plugins/allopen/allopen.k1/src/org/jetbrains/kotlin/allopen/AllOpenDeclarationAttributeAltererExtension.kt`** -> AI Confidence: **99.48%**
4960. **`plugins/allopen/allopen.k2/src/org/jetbrains/kotlin/allopen/fir/FirAllOpenStatusTransformer.kt`** -> AI Confidence: **99.48%**
4961. **`plugins/allopen/testFixtures/org/jetbrains/kotlin/allopen/AllOpenEnvironmentConfigurator.kt`** -> AI Confidence: **99.48%**
4962. **`plugins/assign-plugin/assign-plugin.cli/src/org/jetbrains/kotlin/assignment/plugin/ValueContainerAssignmentPlugin.kt`** -> AI Confidence: **99.48%**
4963. **`plugins/assign-plugin/assign-plugin.k1/src/org/jetbrains/kotlin/assignment/plugin/ValueContainerAssignResolutionAltererExtension.kt`** -> AI Confidence: **99.48%**
4964. **`plugins/assign-plugin/assign-plugin.k1/src/org/jetbrains/kotlin/assignment/plugin/diagnostics/AssignmentPluginDeclarationChecker.kt`** -> AI Confidence: **99.48%**
4965. **`plugins/assign-plugin/assign-plugin.k2/src/org/jetbrains/kotlin/assignment/plugin/k2/FirAssignAnnotationMatchingService.kt`** -> AI Confidence: **99.48%**
4966. **`plugins/assign-plugin/assign-plugin.k2/src/org/jetbrains/kotlin/assignment/plugin/k2/FirAssignmentPluginAssignAltererExtension.kt`** -> AI Confidence: **99.48%**
4967. **`plugins/assign-plugin/assign-plugin.k2/src/org/jetbrains/kotlin/assignment/plugin/k2/diagnostics/FirAssignmentPluginFunctionCallChecker.kt`** -> AI Confidence: **99.48%**
4968. **`plugins/assign-plugin/assign-plugin.k2/src/org/jetbrains/kotlin/assignment/plugin/k2/diagnostics/FirAssignmentPluginFunctionChecker.kt`** -> AI Confidence: **99.48%**
4969. **`plugins/assign-plugin/testFixtures/org/jetbrains/kotlin/assignment/plugin/AssignmentPluginTests.kt`** -> AI Confidence: **99.48%**
4970. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/common/AbstractAtomicSymbols.kt`** -> AI Confidence: **99.48%**
4971. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/common/AbstractAtomicfuIrBuilder.kt`** -> AI Confidence: **99.48%**
4972. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/common/AbstractAtomicfuTransformer.kt`** -> AI Confidence: **99.48%**
4973. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/js/AtomicfuJsIrTransformer.kt`** -> AI Confidence: **99.48%**
4974. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/js/TransformerUtil.kt`** -> AI Confidence: **99.48%**
4975. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/jvm/AtomicfuJvmIrTransformer.kt`** -> AI Confidence: **99.48%**
4976. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/jvm/JvmAtomicSymbols.kt`** -> AI Confidence: **99.48%**
4977. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/jvm/JvmAtomicfuIrBuilder.kt`** -> AI Confidence: **99.48%**
4978. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/native/AtomicfuNativeIrTransformer.kt`** -> AI Confidence: **99.48%**
4979. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/native/NativeAtomicSymbols.kt`** -> AI Confidence: **99.48%**
4980. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/native/NativeAtomicfuIrBuilder.kt`** -> AI Confidence: **99.48%**
4981. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/diagnostic/AtomicfuPropertyChecker.kt`** -> AI Confidence: **99.48%**
4982. **`plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/extensions/AtomicfuLoweringExtension.kt`** -> AI Confidence: **99.48%**
4983. **`plugins/atomicfu/atomicfu-compiler/testFixtures/org/jetbrains/kotlinx/atomicfu/runners/AbstractAtomicfuPluginTestRunners.kt`** -> AI Confidence: **99.48%**
4984. **`plugins/atomicfu/atomicfu-compiler/testFixtures/org/jetbrains/kotlinx/atomicfu/runners/AtomicfuExtensionRegistrarConfigurator.kt`** -> AI Confidence: **99.48%**
4985. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractCompilerTest.kt`** -> AI Confidence: **99.48%**
4986. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractComposeDiagnosticsTest.kt`** -> AI Confidence: **99.48%**
4987. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractIrTransformTest.kt`** -> AI Confidence: **99.48%**
4988. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractLiveLiteralTransformTests.kt`** -> AI Confidence: **99.48%**
4989. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/AbstractMultiPlatformIntegrationTest.kt`** -> AI Confidence: **99.48%**
4990. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ClassStabilityTransformTests.kt`** -> AI Confidence: **99.48%**
4991. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/CodegenMetadataTests.kt`** -> AI Confidence: **99.48%**
4992. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ComposeBytecodeCodegenTest.kt`** -> AI Confidence: **99.48%**
4993. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ComposeCallResolverTests.kt`** -> AI Confidence: **99.48%**
4994. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ComposeCrossModuleTests.kt`** -> AI Confidence: **99.48%**
4995. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ComposerParamSignatureTests.kt`** -> AI Confidence: **99.48%**
4996. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ComposerParamTransformTests.kt`** -> AI Confidence: **99.48%**
4997. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ContextParametersTransformTests.kt`** -> AI Confidence: **99.48%**
4998. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ControlFlowTransformTests.kt`** -> AI Confidence: **99.48%**
4999. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/FunctionBodySkippingTransformTests.kt`** -> AI Confidence: **99.48%**
5000. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/FunctionKeyMetaAnnotationsTests.kt`** -> AI Confidence: **99.48%**
5001. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/GoldenTransformRule.kt`** -> AI Confidence: **99.48%**
5002. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/GroupAnalysisCompilerTest.kt`** -> AI Confidence: **99.48%**
5003. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/LambdaMemoizationTransformTests.kt`** -> AI Confidence: **99.48%**
5004. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/LiveLiteralTransformTests.kt`** -> AI Confidence: **99.48%**
5005. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/LiveLiteralV2TransformTests.kt`** -> AI Confidence: **99.48%**
5006. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/RememberIntrinsicTransformTests.kt`** -> AI Confidence: **99.48%**
5007. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/RunComposableTests.kt`** -> AI Confidence: **99.48%**
5008. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/RuntimeTests.kt`** -> AI Confidence: **99.48%**
5009. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ScopeComposabilityTests.kt`** -> AI Confidence: **99.48%**
5010. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/StaticExpressionDetectionTests.kt`** -> AI Confidence: **99.48%**
5011. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/StrongSkippingModeTransformTests.kt`** -> AI Confidence: **99.48%**
5012. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/TargetAnnotationsTransformTests.kt`** -> AI Confidence: **99.48%**
5013. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/analysis/ComposableCheckerTests.kt`** -> AI Confidence: **99.48%**
5014. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/analysis/ComposableDeclarationCheckerTests.kt`** -> AI Confidence: **99.48%**
5015. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/analysis/ComposableTargetCheckerTests.kt`** -> AI Confidence: **99.48%**
5016. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/analysis/ComposeMultiplatformCheckerTests.kt`** -> AI Confidence: **99.48%**
5017. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/facade/K1CompilerFacade.kt`** -> AI Confidence: **99.48%**
5018. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/facade/K2CompilerFacade.kt`** -> AI Confidence: **99.48%**
5019. **`plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/facade/KotlinCompilerFacade.kt`** -> AI Confidence: **99.48%**
5020. **`plugins/compose/compiler-hosted/runtime-tests/src/commonTest/kotlin/androidx/compose/compiler/test/CompositionTests.kt`** -> AI Confidence: **99.48%**
5021. **`plugins/compose/compiler-hosted/runtime-tests/src/jvmTest/kotlin/androidx/compose/compiler/test/JvmCompositionTests.kt`** -> AI Confidence: **99.48%**
5022. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/BuildMetrics.kt`** -> AI Confidence: **99.48%**
5023. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/ComposeIrGenerationExtension.kt`** -> AI Confidence: **99.48%**
5024. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/ComposePlugin.kt`** -> AI Confidence: **99.48%**
5025. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/VersionChecker.kt`** -> AI Confidence: **99.48%**
5026. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/analysis/Stability.kt`** -> AI Confidence: **99.48%**
5027. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/AnnotationUtils.kt`** -> AI Confidence: **99.48%**
5028. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposableAnnotationChecker.kt`** -> AI Confidence: **99.48%**
5029. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposableCallChecker.kt`** -> AI Confidence: **99.48%**
5030. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposableDeclarationChecker.kt`** -> AI Confidence: **99.48%**
5031. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposableTargetChecker.kt`** -> AI Confidence: **99.48%**
5032. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposeDiagnosticSuppressor.kt`** -> AI Confidence: **99.48%**
5033. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k1/ComposeTypeResolutionInterceptorExtension.kt`** -> AI Confidence: **99.48%**
5034. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposableAnnotationChecker.kt`** -> AI Confidence: **99.48%**
5035. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposableCallChecker.kt`** -> AI Confidence: **99.48%**
5036. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposableFunctionChecker.kt`** -> AI Confidence: **99.48%**
5037. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposablePropertyChecker.kt`** -> AI Confidence: **99.48%**
5038. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposableTargetChecker.kt`** -> AI Confidence: **99.48%**
5039. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposeErrors.kt`** -> AI Confidence: **99.48%**
5040. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/ComposeFirExtensions.kt`** -> AI Confidence: **99.48%**
5041. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/k2/FirUtils.kt`** -> AI Confidence: **99.48%**
5042. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/AbstractComposeLowering.kt`** -> AI Confidence: **99.48%**
5043. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ClassStabilityFieldSerializationPlugin.kt`** -> AI Confidence: **99.48%**
5044. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ClassStabilityTransformer.kt`** -> AI Confidence: **99.48%**
5045. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableDefaultParamLowering.kt`** -> AI Confidence: **99.48%**
5046. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunInterfaceLowering.kt`** -> AI Confidence: **99.48%**
5047. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt`** -> AI Confidence: **99.48%**
5048. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableLambdaAnnotator.kt`** -> AI Confidence: **99.48%**
5049. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableTargetAnnotationsTransformer.kt`** -> AI Confidence: **99.48%**
5050. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableTypeRemapper.kt`** -> AI Confidence: **99.48%**
5051. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableVersionOverloadsLowering.kt`** -> AI Confidence: **99.48%**
5052. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposerIntrinsicTransformer.kt`** -> AI Confidence: **99.48%**
5053. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposerLambdaMemoization.kt`** -> AI Confidence: **99.48%**
5054. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposerParamTransformer.kt`** -> AI Confidence: **99.48%**
5055. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/CopyDefaultValuesFromExpectLowering.kt`** -> AI Confidence: **99.48%**
5056. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/DurableFunctionKeyTransformer.kt`** -> AI Confidence: **99.48%**
5057. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/DurableKeyTransformer.kt`** -> AI Confidence: **99.48%**
5058. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/IrInlineReferenceLocator.kt`** -> AI Confidence: **99.48%**
5059. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/IrSourcePrinter.kt`** -> AI Confidence: **99.48%**
5060. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/KlibAssignableParamTransformer.kt`** -> AI Confidence: **99.48%**
5061. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/LiveLiteralTransformer.kt`** -> AI Confidence: **99.48%**
5062. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/WrapJsComposableLambdaLowering.kt`** -> AI Confidence: **99.48%**
5063. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/hiddenfromobjc/AddHiddenFromObjCLowering.kt`** -> AI Confidence: **99.48%**
5064. **`plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/hiddenfromobjc/AddHiddenFromObjCSerializationPlugin.kt`** -> AI Confidence: **99.48%**
5065. **`plugins/compose/compiler-hosted/src/test/kotlin/androidx/compose/compiler/plugins/kotlin/ComposeCompilerBoxTests.kt`** -> AI Confidence: **99.48%**
5066. **`plugins/compose/compiler-hosted/src/test/kotlin/androidx/compose/compiler/plugins/kotlin/services/ComposeTestUtils.kt`** -> AI Confidence: **99.48%**
5067. **`plugins/compose/group-mapping/src/main/kotlin/androidx/compose/compiler/mapping/ClassInfo.kt`** -> AI Confidence: **99.48%**
5068. **`plugins/compose/group-mapping/src/main/kotlin/androidx/compose/compiler/mapping/group/GroupAnalysis.kt`** -> AI Confidence: **99.48%**
5069. **`plugins/js-plain-objects/compiler-plugin/js-plain-objects.backend/src/org/jetbrains/kotlinx/jso/compiler/backend/JsObjectLoweringExtension.kt`** -> AI Confidence: **99.48%**
5070. **`plugins/js-plain-objects/compiler-plugin/js-plain-objects.k2/src/org/jetbrains/kotlinx/jso/compiler/fir/JsPlainObjectsFunctionsGenerator.kt`** -> AI Confidence: **99.48%**
5071. **`plugins/js-plain-objects/compiler-plugin/js-plain-objects.k2/src/org/jetbrains/kotlinx/jso/compiler/fir/checkers/FirJsPlainObjectsPluginClassChecker.kt`** -> AI Confidence: **99.48%**
5072. **`plugins/js-plain-objects/compiler-plugin/js-plain-objects.k2/src/org/jetbrains/kotlinx/jso/compiler/fir/services/JsPlainObjectsPropertiesProvider.kt`** -> AI Confidence: **99.48%**
5073. **`plugins/js-plain-objects/compiler-plugin/testFixtures/org/jetbrains/kotlinx/jso/jsObjectConfiguration.kt`** -> AI Confidence: **99.48%**
5074. **`plugins/jvm-abi-gen/src/org/jetbrains/kotlin/jvm/abi/JvmAbiClassBuilderInterceptor.kt`** -> AI Confidence: **99.48%**
5075. **`plugins/jvm-abi-gen/src/org/jetbrains/kotlin/jvm/abi/JvmAbiComponentRegistrar.kt`** -> AI Confidence: **99.48%**
5076. **`plugins/jvm-abi-gen/src/org/jetbrains/kotlin/jvm/abi/JvmAbiOutputExtension.kt`** -> AI Confidence: **99.48%**
5077. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/KaptContext.kt`** -> AI Confidence: **99.48%**
5078. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/ProcessorLoader.kt`** -> AI Confidence: **99.48%**
5079. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/annotationProcessing.kt`** -> AI Confidence: **99.48%**
5080. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/incremental/incrementalProcessors.kt`** -> AI Confidence: **99.48%**
5081. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/incremental/javacVisitors.kt`** -> AI Confidence: **99.48%**
5082. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/javac/KaptJavaFileManager.kt`** -> AI Confidence: **99.48%**
5083. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/javac/KaptJavaLog.kt`** -> AI Confidence: **99.48%**
5084. **`plugins/kapt/kapt-base/src/org/jetbrains/kotlin/kapt/base/stubs/KaptStubLineInformation.kt`** -> AI Confidence: **99.48%**
5085. **`plugins/kapt/kapt-cli/src/KaptCli.kt`** -> AI Confidence: **99.48%**
5086. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/EfficientProcessorLoader.kt`** -> AI Confidence: **99.48%**
5087. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/FirKaptAnalysisHandlerExtension.kt`** -> AI Confidence: **99.48%**
5088. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/KaptPlugin.kt`** -> AI Confidence: **99.48%**
5089. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/javac/KaptJavaFileObject.kt`** -> AI Confidence: **99.48%**
5090. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/javac/KaptTreeMaker.kt`** -> AI Confidence: **99.48%**
5091. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/ErrorTypeCorrector.kt`** -> AI Confidence: **99.48%**
5092. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptDocCommentKeeper.kt`** -> AI Confidence: **99.48%**
5093. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptLineMappingCollector.kt`** -> AI Confidence: **99.48%**
5094. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptStubConverter.kt`** -> AI Confidence: **99.48%**
5095. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptTypeMapper.kt`** -> AI Confidence: **99.48%**
5096. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/SignatureParserVisitor.kt`** -> AI Confidence: **99.48%**
5097. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/parseParameters.kt`** -> AI Confidence: **99.48%**
5098. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/util/MessageCollectorBackedKaptLogger.kt`** -> AI Confidence: **99.48%**
5099. **`plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/util/PrettyWithWorkarounds.kt`** -> AI Confidence: **99.48%**
5100. **`plugins/kotlin-dataframe/kotlin-dataframe.backend/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/IrBodyFiller.kt`** -> AI Confidence: **99.48%**
5101. **`plugins/kotlin-dataframe/kotlin-dataframe.backend/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/IrImportedSchemaGenerator.kt`** -> AI Confidence: **99.48%**
5102. **`plugins/kotlin-dataframe/kotlin-dataframe.cli/src/org/jetbrains/kotlinx/dataframe/plugin/FirDataFrameComponentRegistrar.kt`** -> AI Confidence: **99.48%**
5103. **`plugins/kotlin-dataframe/kotlin-dataframe.common/src/org/jetbrains/kotlinx/dataframe/plugin/utils/Names.kt`** -> AI Confidence: **99.48%**
5104. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/analyzeRefinedCallShape.kt`** -> AI Confidence: **99.48%**
5105. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/DataRowSchemaSupertype.kt`** -> AI Confidence: **99.48%**
5106. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/DataSchemaInfoCheckers.kt`** -> AI Confidence: **99.48%**
5107. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ExpressionAnalysisAdditionalChecker.kt`** -> AI Confidence: **99.48%**
5108. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/FunctionCallTransformer.kt`** -> AI Confidence: **99.48%**
5109. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ImportedSchemasCheckers.kt`** -> AI Confidence: **99.48%**
5110. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ImportedSchemasCompanionGenerator.kt`** -> AI Confidence: **99.48%**
5111. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ImportedSchemasGenerator.kt`** -> AI Confidence: **99.48%**
5112. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/ReturnTypeBasedReceiverInjector.kt`** -> AI Confidence: **99.48%**
5113. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/TokenContentGenerator.kt`** -> AI Confidence: **99.48%**
5114. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/TopLevelExtensionsGenerator.kt`** -> AI Confidence: **99.48%**
5115. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/extensions/impl/PropertyName.kt`** -> AI Confidence: **99.48%**
5116. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/DataFrameAdapter.kt`** -> AI Confidence: **99.48%**
5117. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/Interpreter.kt`** -> AI Confidence: **99.48%**
5118. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/PluginDataFrameSchemaParser.kt`** -> AI Confidence: **99.48%**
5119. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/SimpleCol.kt`** -> AI Confidence: **99.48%**
5120. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/Nulls.kt`** -> AI Confidence: **99.48%**
5121. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/convert.kt`** -> AI Confidence: **99.48%**
5122. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/cumSum.kt`** -> AI Confidence: **99.48%**
5123. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/dataFrameOf.kt`** -> AI Confidence: **99.48%**
5124. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/gather.kt`** -> AI Confidence: **99.48%**
5125. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/groupBy.kt`** -> AI Confidence: **99.48%**
5126. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/implode.kt`** -> AI Confidence: **99.48%**
5127. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/joinDsl.kt`** -> AI Confidence: **99.48%**
5128. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/parse.kt`** -> AI Confidence: **99.48%**
5129. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/rename.kt`** -> AI Confidence: **99.48%**
5130. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/select.kt`** -> AI Confidence: **99.48%**
5131. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/split.kt`** -> AI Confidence: **99.48%**
5132. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/statistics.kt`** -> AI Confidence: **99.48%**
5133. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/toDataFrame.kt`** -> AI Confidence: **99.48%**
5134. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/update.kt`** -> AI Confidence: **99.48%**
5135. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/impl/api/xs.kt`** -> AI Confidence: **99.48%**
5136. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/interpret.kt`** -> AI Confidence: **99.48%**
5137. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/loadInterpreter.kt`** -> AI Confidence: **99.48%**
5138. **`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/utils/firFactories.kt`** -> AI Confidence: **99.48%**
5139. **`plugins/kotlin-dataframe/testData/box/diff.kt`** -> AI Confidence: **99.48%**
5140. **`plugins/kotlin-dataframe/testData/box/duplicatedSignature.kt`** -> AI Confidence: **99.48%**
5141. **`plugins/kotlin-dataframe/testData/box/flexibleReturnType.kt`** -> AI Confidence: **99.48%**
5142. **`plugins/kotlin-dataframe/testData/box/toDataFrame.kt`** -> AI Confidence: **99.48%**
5143. **`plugins/kotlin-dataframe/testData/box/toDataFrameValueTypes.kt`** -> AI Confidence: **99.48%**
5144. **`plugins/kotlin-dataframe/testFixturesResources/testUtils.kt`** -> AI Confidence: **99.48%**
5145. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/BaseIrGenerator.kt`** -> AI Confidence: **99.48%**
5146. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/DefaultValuesUtils.kt`** -> AI Confidence: **99.48%**
5147. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/Instantiator.kt`** -> AI Confidence: **99.48%**
5148. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrBuilderWithPluginContext.kt`** -> AI Confidence: **99.48%**
5149. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrGeneratorUtils.kt`** -> AI Confidence: **99.48%**
5150. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrPreGenerator.kt`** -> AI Confidence: **99.48%**
5151. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrPredicates.kt`** -> AI Confidence: **99.48%**
5152. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/IrSerializableProperties.kt`** -> AI Confidence: **99.48%**
5153. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializableCompanionIrGenerator.kt`** -> AI Confidence: **99.48%**
5154. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializableIrGenerator.kt`** -> AI Confidence: **99.48%**
5155. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializationJvmIrIntrinsicSupport.kt`** -> AI Confidence: **99.48%**
5156. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializerForEnumsGenerator.kt`** -> AI Confidence: **99.48%**
5157. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializerForInlineClassGenerator.kt`** -> AI Confidence: **99.48%**
5158. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializerIrGenerator.kt`** -> AI Confidence: **99.48%**
5159. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/backend/ir/SerializerSearchUtil.kt`** -> AI Confidence: **99.48%**
5160. **`plugins/kotlinx-serialization/kotlinx-serialization.backend/src/org/jetbrains/kotlinx/serialization/compiler/extensions/SerializationLoweringExtension.kt`** -> AI Confidence: **99.48%**
5161. **`plugins/kotlinx-serialization/kotlinx-serialization.cli/src/org/jetbrains/kotlinx/serialization/compiler/extensions/SerializationComponentRegistrar.kt`** -> AI Confidence: **99.48%**
5162. **`plugins/kotlinx-serialization/kotlinx-serialization.common/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/RuntimeVersions.kt`** -> AI Confidence: **99.48%**
5163. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/SerializationContextInFile.kt`** -> AI Confidence: **99.48%**
5164. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/SerializationPluginDeclarationChecker.kt`** -> AI Confidence: **99.48%**
5165. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/SerializationPluginErrorsRendering.kt`** -> AI Confidence: **99.48%**
5166. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/TypeUtil.kt`** -> AI Confidence: **99.48%**
5167. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/diagnostic/VersionReader.kt`** -> AI Confidence: **99.48%**
5168. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/extensions/SerializationDescriptorSerializerPlugin.kt`** -> AI Confidence: **99.48%**
5169. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/extensions/SerializationResolveExtension.kt`** -> AI Confidence: **99.48%**
5170. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/resolve/KSerializationUtil.kt`** -> AI Confidence: **99.48%**
5171. **`plugins/kotlinx-serialization/kotlinx-serialization.k1/src/org/jetbrains/kotlinx/serialization/compiler/resolve/KSerializerDescriptorResolver.kt`** -> AI Confidence: **99.48%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptLexer.java` -> **100.0%** Exposure
- `js/js.translator/testData/typescript-export/js/suspend-functions/suspend-functions.kt` -> **0.0001%** Exposure
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/ApplePrivacyManifestIT.kt` -> **0.0001%** Exposure
### Exploit Generation Surface
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10CompilerFacility.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ExpressionTypeProvider.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10Resolver.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10ScopeProvider.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolDeclarationOverridesProvider.kt` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/assertions/filesAssertions.kt` -> **100.0%** Exposure
- `compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/KotlinToolchains.kt` -> **100.0%** Exposure
- `compiler/cli/cli-metadata/src/org/jetbrains/kotlin/cli/metadata/KotlinMetadataCompiler.kt` -> **100.0%** Exposure
- `compiler/cli/cli-runner/src/org/jetbrains/kotlin/runner/Main.kt` -> **100.0%** Exposure
- `compiler/daemon/src/org/jetbrains/kotlin/daemon/KotlinCompileDaemon.kt` -> **100.0%** Exposure
### Raw Memory Manipulation
- `kotlin-native/runtime/src/libbacktrace/c/dwarf.c` -> **10.0%** Exposure
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/commonizeSQLiteAndCurlInterop/libs/sqlite3ext.h` -> **10.0%** Exposure
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/commonizeSQLiteInterop/libs/sqlite3ext.h` -> **10.0%** Exposure
- `kotlin-native/runtime/src/libbacktrace/c/mmap.c` -> **9.9999%** Exposure
- `kotlin-native/runtime/src/libbacktrace/c/include/internal.h` -> **9.9997%** Exposure
### Hardcoded Payload Artifacts
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportPopularSwiftPMDependenciesTests.kt` -> **21.0228%** Exposure
### Algorithmic DoS Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10CompilerFacility.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10Resolver.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SignatureSubstitutor.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10SymbolDeclarationOverridesProvider.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/components/KaFe10TypeProvider.kt` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `99` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `134211` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `native/swift/swift-export-standalone/resources/swift/KotlinCoroutineSupport.swift` (SWIFT) -> Cumulative Risk: **962.95**
- **Archetype:** `file_cluster_16` (Distance: 11.5 IQR)
- **Magnitude:** 406.26 | **LOC:** 277 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `next` (Impact: 74.5), `init` (Impact: 24.3), `compareAndSet` (Impact: 21.1)

### 2. `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/KotlinxCoroutinesCore/KotlinxCoroutinesCore.swift` (SWIFT) -> Cumulative Risk: **941.91**
- **Archetype:** `file_cluster_4` (Distance: 11.709 IQR)
- **Magnitude:** 0.61 | **LOC:** 232 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `emit` (Impact: 140.4), `emit` (Impact: 140.4), `flowCollector` (Impact: 103.6)

### 3. `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/KotlinxCoroutinesCore/KotlinxCoroutinesCore.kt` (KOTLIN) -> Cumulative Risk: **923.52**
- **Archetype:** `file_cluster_0` (Distance: 11.29 IQR)
- **Magnitude:** 0.49 | **LOC:** 188 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `kotlinx_coroutines_flow_FlowCollector_em` (Impact: 80.0), `kotlinx_coroutines_flow_MutableSharedFlo` (Impact: 80.0), `kotlinx_coroutines_flow_FlowCollector__T` (Impact: 73.4)

### 4. `libraries/stdlib/src/kotlin/collections/SlidingWindow.kt` (KOTLIN) -> Cumulative Risk: **917.94**
- **Archetype:** `file_cluster_16` (Distance: 12.398 IQR)
- **Magnitude:** 392.92 | **LOC:** 206 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `windowedIterator` (Impact: 193.1), `toArray` (Impact: 32.6), `removeFirst` (Impact: 20.9)

### 5. `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/calls/stages/TypeArgumentMapping.kt` (KOTLIN) -> Cumulative Risk: **895.9**
- **Archetype:** `file_cluster_13` (Distance: 12.688 IQR)
- **Magnitude:** 139.68 | **LOC:** 106 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `check` (Impact: 61.4), `computeDefaultMappingForRawTypeMember` (Impact: 14.8), `check` (Impact: 8.3)

### 6. `libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt` (KOTLIN) -> Cumulative Risk: **890.77**
- **Archetype:** `file_cluster_16` (Distance: 13.557 IQR)
- **Magnitude:** 463.7 | **LOC:** 226 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `yieldAll` (Impact: 326.9), `yieldAll` (Impact: 30.2), `iterator` (Impact: 12.3)

### 7. `kotlin-native/runtime/src/gc/cms/cpp/GCImplTest.cpp` (CPP) -> Cumulative Risk: **885.54**
- **Archetype:** `file_cluster_4` (Distance: 13.86 IQR)
- **Magnitude:** 259.6 | **LOC:** 156 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `TYPED_TEST_P` (Impact: 76.5), `TYPED_TEST_P` (Impact: 27.9), `ConcurrentMarkAndSweepTest` (Impact: 1.8)

### 8. `kotlin-native/runtime/src/main/kotlin/kotlin/coroutines/intrinsics/IntrinsicsNative.kt` (KOTLIN) -> Cumulative Risk: **871.95**
- **Archetype:** `file_cluster_16` (Distance: 12.702 IQR)
- **Magnitude:** 161.62 | **LOC:** 325 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.1073%)
- **Heaviest Functions:** `createCoroutineFromSuspendFunction` (Impact: 50.7), `createSimpleCoroutineForSuspendFunction` (Impact: 40.6), `createContinuationArgumentFromCallback` (Impact: 8.6)

### 9. `compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/generators/AdapterGenerator.kt` (KOTLIN) -> Cumulative Risk: **870.78**
- **Archetype:** `file_cluster_13` (Distance: 13.265 IQR)
- **Magnitude:** 1259.1 | **LOC:** 798 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `createAdapteeCallForCallableReference` (Impact: 224.0), `removeExternalProjections` (Impact: 219.8), `createAdapterFunctionForCallableReferenc` (Impact: 102.1)

### 10. `compiler/ir/backend.common/src/org/jetbrains/kotlin/backend/common/lower/loops/WithIndexLoopHeader.kt` (KOTLIN) -> Cumulative Risk: **866.24**
- **Archetype:** `file_cluster_11` (Distance: 23.317 IQR)
- **Magnitude:** 138.94 | **LOC:** 170 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `init` (Impact: 80.9), `initializeIteration` (Impact: 19.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.217 IQR)
- **Top Global Matches:** file_cluster_0: 14.217, file_cluster_8: 14.541, file_cluster_11: 14.548
- **Magnitude:** 7147.22 | **LOC:** 11868 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (86.2374%), Tech Debt (81.6103%)
**Top Internal Functions/Classes:**
  * `importFromBlock` (Impact: 554.4 | O(N^1) | DB: 10)
  * `exportFromBlock` (Impact: 284.8 | O(N^1) | DB: 8)
  * `importNamespace` (Impact: 273.4 | O(N^1) | DB: 6)
  * `moduleExportName` (Impact: 270.5 | O(N^1) | DB: 3)
  * `statement` (Impact: 153.3 | O(N^1) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3842`, `structural_boundaries: 2895`, `args: 1863`, `func_start: 3420`, `class_start: 167`
* *Risk/State:* `safety_bypasses: 537`, `state_mutation: 2345`, `duplicate_logic: 185`
* *Architecture:* `api: 1686`, `import: 6`
* *Defense:* `safety: 781`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.List, org.antlr.v4.runtime.atn.*, org.jetbrains.kotlin.js.parser.antlr.JavaScriptParserBase, org.antlr.v4.runtime.*, org.antlr.v4.runtime.misc.*, java.util.Iterator, org.jetbrains.kotlin.js.parser.antlr.JavaScriptRuleContext, org.antlr.v4.runtime.tree.*...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/PositioningStrategies.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.551 IQR)
- **Top Global Matches:** file_cluster_0: 13.551, file_cluster_16: 13.559, file_cluster_11: 13.681
- **Magnitude:** 5481.48 | **LOC:** 1297 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (88.6681%), Tech Debt (99.8553%)
**Top Internal Functions/Classes:**
  * `mark` (Impact: 3323.1 | O(2^N) | DB: 10)
  * `mark` (Impact: 436.4 | O(2^N))
  * `mark` (Impact: 225.5 | O(2^N))
  * `findStartingPsiElementForDeclarationName` (Impact: 171.3 | O(2^N))
  * `mark` (Impact: 141.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `args: 110`, `func_start: 91`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 37`, `planned_debt: 1`, `duplicate_logic: 25`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 228`, `doc: 2`, `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.jetbrains.kotlin.lexer.KtTokens.*, org.jetbrains.kotlin.psi.*, com.intellij.psi.tree.IElementType, org.jetbrains.kotlin.lexer.KtTokens, com.intellij.psi.*, com.intellij.psi.util.descendants, com.intellij.psi.util.elementType, org.jetbrains.kotlin.psi.psiUtil.*...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.831 IQR)
- **Top Global Matches:** file_cluster_13: 13.831, file_cluster_8: 13.927, file_cluster_0: 13.942
- **Magnitude:** 5410.22 | **LOC:** 2368 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 107
- **Risk Profile:** Cognitive Load (80.338%), Tech Debt (22.6826%)
**Top Internal Functions/Classes:**
  * `transformQualifiedAccessExpression` (Impact: 4333.9 | O(2^N) | DB: 107)
  * `tryResolveIndexedAccessAugmentedAssignme` (Impact: 349.7 | O(N^6) | DB: 29)
  * `transformIndexedAccessAugmentedAssignmen` (Impact: 83.2 | O(N^5) | DB: 1)
  * `extractSuperTypeDeclaration` (Impact: 48.4 | O(2^N))
  * `createFunctionCall` (Impact: 38.2 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `args: 103`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 332`, `dead_code: 6`, `planned_debt: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 12`, `import: 60`
* *Defense:* `safety: 143`, `doc: 8`, `test: 3`, `immutability_locks: 182`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` org.jetbrains.kotlin.fir.symbols.impl.FirVariableSymbol, org.jetbrains.kotlin.fir.resolve.calls.candidate.FirErrorReferenceWithCandidate, org.jetbrains.kotlin.fir.scopes.impl.isWrappedIntegerOperatorForUnsignedType, org.jetbrains.kotlin.fir.expressions.*, org.jetbrains.kotlin.fir.symbols.impl.FirConstructorSymbol, org.jetbrains.kotlin.fir.declarations.utils.replSnippetDelegatedPropertyCopies, org.jetbrains.kotlin.fir.resolve.calls.candidate.Candidate, org.jetbrains.kotlin.name.SpecialNames...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `libraries/stdlib/js/src/kotlin/js/math.polyfills.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.387 IQR)
- **Top Global Matches:** file_cluster_8: 12.387, file_cluster_0: 12.397, file_cluster_7: 12.94
- **Magnitude:** 5116.12 | **LOC:** 308 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (85.654%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `args: 29`, `func_start: 14`
* *Risk/State:* `state_mutation: 135`
* *Architecture:* `api: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.774 IQR)
- **Top Global Matches:** file_cluster_13: 14.774, file_cluster_11: 14.955, file_cluster_8: 14.961
- **Magnitude:** 4933.94 | **LOC:** 2154 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 201
- **Risk Profile:** Cognitive Load (92.0599%), Tech Debt (73.7697%)
**Top Internal Functions/Classes:**
  * `toKaSymbolResolutionAttempt` (Impact: 3848.2 | O(2^N) | DB: 201)
  * `toKaReceiverValue` (Impact: 244.9 | O(2^N) | DB: 2)
  * `collectCallCandidates` (Impact: 91.2 | O(2^N) | DB: 8)
  * `toFirTypeArgumentsMapping` (Impact: 41.0 | O(N^3))
  * `toFirTypeArgumentsMapping` (Impact: 40.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `args: 97`, `func_start: 62`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 411`, `planned_debt: 2`, `duplicate_logic: 10`, `orphaned_logic: 5`
* *Architecture:* `api: 1`, `import: 83`
* *Defense:* `safety: 223`, `doc: 15`, `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` org.jetbrains.kotlin.lexer.KtTokens, org.jetbrains.kotlin.analysis.api.utils.errors.withPsiEntry, org.jetbrains.kotlin.analysis.api.fir.utils.withSymbolAttachment, org.jetbrains.kotlin.analysis.api.fir.references.*, org.jetbrains.kotlin.analysis.utils.printer.parentOfType, org.jetbrains.kotlin.psi.KtPsiUtil.deparenthesize, org.jetbrains.kotlin.analysis.api.types.KaType, org.jetbrains.kotlin.fir.resolve.FirResolvedSymbolOrigin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/frontend.common-psi/src/org/jetbrains/kotlin/diagnostics/LightTreePositioningStrategies.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.034 IQR)
- **Top Global Matches:** file_cluster_8: 12.034, file_cluster_16: 12.106, file_cluster_13: 12.437
- **Magnitude:** 4327.42 | **LOC:** 1883 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (21.3792%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `mark` (Impact: 551.9 | O(2^N) | DB: 8)
  * `mark` (Impact: 488.0 | O(2^N))
  * `mark` (Impact: 236.6 | O(2^N))
  * `mark` (Impact: 236.4 | O(2^N))
  * `mark` (Impact: 143.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 470`, `args: 109`, `func_start: 82`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 91`, `fragile_debt: 1`, `duplicate_logic: 64`, `orphaned_logic: 1`
* *Architecture:* `import: 15`
* *Defense:* `safety: 121`, `doc: 4`, `immutability_locks: 226`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.jetbrains.kotlin.lexer.KtTokens.*, com.intellij.psi.tree.IElementType, org.jetbrains.kotlin.KtSourceElement, org.jetbrains.kotlin.utils.addToStdlib.runUnless, org.jetbrains.kotlin.lexer.KtTokens, com.intellij.util.diff.FlyweightCapableTreeStructure, com.intellij.lang.LighterASTNode, org.jetbrains.kotlin.util.getChildren...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/KotlinParsing.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.96 IQR)
- **Top Global Matches:** file_cluster_8: 11.96, file_cluster_13: 12.11, file_cluster_2: 12.256
- **Magnitude:** 4156.66 | **LOC:** 2922 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (49.0208%), Tech Debt (15.5229%)
**Top Internal Functions/Classes:**
  * `parseContextParameterOrReceiverList` (Impact: 2840.8 | O(2^N) | DB: 58)
  * `doParseModifierListBody` (Impact: 428.4 | O(2^N) | DB: 5)
  * `parseImportDirective` (Impact: 97.2 | O(N^5) | DB: 4)
  * `parseCommonDeclaration` (Impact: 85.3 | O(N^4))
    * *Intent:* /* * toplevelObject * : package * : class * : extension * : function * : property * : typeAlias * : ...
  * `parsePackageName` (Impact: 80.2 | O(N^5) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `args: 69`, `func_start: 66`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 171`, `dead_code: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 12`, `import: 27`
* *Defense:* `safety: 39`, `doc: 5`, `immutability_locks: 147`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.jetbrains.kotlin.kmp.parser.KtNodeTypes, org.jetbrains.kotlin.kmp.lexer.KtTokens.WHEN_KEYWORD, org.jetbrains.kotlin.kmp.lexer.KtTokens.CONTINUE_KEYWORD, com.intellij.platform.syntax.parser.SyntaxTreeBuilder, org.jetbrains.kotlin.kmp.lexer.KtTokens.BREAK_KEYWORD, org.jetbrains.annotations.Contract, org.jetbrains.kotlin.kmp.lexer.KtTokens.FUN_MODIFIER, com.intellij.platform.syntax.SyntaxElementTypeSet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/IrToBitcode.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.681 IQR)
- **Top Global Matches:** file_cluster_8: 12.681, file_cluster_13: 12.973, file_cluster_11: 13.012
- **Magnitude:** 4154.14 | **LOC:** 2960 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (40.919%), Tech Debt (95.1031%)
**Top Internal Functions/Classes:**
  * `call` (Impact: 208.6 | O(2^N) | DB: 4)
  * `overrideRuntimeGlobals` (Impact: 196.0 | O(N^6))
  * `evaluateOperatorCall` (Impact: 172.6 | O(2^N) | DB: 1)
  * `scope` (Impact: 159.3 | O(2^N))
    * *Intent:* // support of initilaization of object in following case: // open class Base(val field: ...) // Chil...
  * `evaluateConstantValueImpl` (Impact: 158.7 | O(N^6))
    * *Intent:* //-------------------------------------------------------------------------//
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 462`, `args: 292`, `func_start: 166`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 76`, `state_mutation: 174`, `dead_code: 1`, `planned_debt: 16`, `fragile_debt: 4`, `duplicate_logic: 18`, `orphaned_logic: 12`
* *Architecture:* `io: 4`, `api: 1`, `import: 35`
* *Defense:* `safety: 135`, `doc: 16`, `test: 11`, `sync_locks: 1`, `immutability_locks: 278`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` kotlinx.cinterop.*, org.jetbrains.kotlin.backend.konan.lower.*, org.jetbrains.kotlin.backend.common.ir.isUnconditional, org.jetbrains.kotlin.ir.declarations.*, llvm.*, org.jetbrains.kotlin.backend.konan.cexport.CAdapterExportedElements, org.jetbrains.kotlin.config.nativeBinaryOptions.SourceInfoType, org.jetbrains.kotlin.backend.konan.cgen.CBridgeOrigin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.241 IQR)
- **Top Global Matches:** file_cluster_13: 14.241, file_cluster_11: 14.267, file_cluster_8: 14.298
- **Magnitude:** 4113.22 | **LOC:** 5145 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 166
- **Risk Profile:** Cognitive Load (82.44%), Tech Debt (16.2647%)
**Top Internal Functions/Classes:**
  * `visitFunctionInScope` (Impact: 1697.2 | O(N^6) | DB: 166)
    * *Intent:* * 123, * $composer, * (0b110 and $dirty) or // 1st param has same state that our 1st param does * 0b...
  * `visitFunctionAccess` (Impact: 255.2 | O(2^N) | DB: 1)
  * `isLambda` (Impact: 146.6 | O(N^5) | DB: 6)
  * `visitReturn` (Impact: 127.5 | O(2^N) | DB: 2)
    * *Intent:* // This is a workaround for d8 generating duplicate line number entries // whenever a branch without...
  * `visitWhen` (Impact: 127.4 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 483`, `args: 169`, `func_start: 124`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 607`, `dead_code: 26`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 7`, `import: 45`
* *Defense:* `safety: 123`, `doc: 19`, `immutability_locks: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` org.jetbrains.kotlin.ir.expressions.impl.*, org.jetbrains.kotlin.platform.isJs, org.jetbrains.kotlin.ir.builders.irReturn, org.jetbrains.kotlin.ir.symbols.impl.IrVariableSymbolImpl, org.jetbrains.kotlin.ir.IrElement, org.jetbrains.kotlin.ir.builders.irBlockBody, org.jetbrains.kotlin.name.SpecialNames, org.jetbrains.kotlin.backend.common.extensions.IrPluginContext...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/backend/src/org/jetbrains/kotlin/codegen/inline/MethodInliner.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.946 IQR)
- **Top Global Matches:** file_cluster_13: 12.946, file_cluster_8: 13.071, file_cluster_11: 13.115
- **Magnitude:** 3832.46 | **LOC:** 1246 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (80.6807%), Tech Debt (26.7589%)
**Top Internal Functions/Classes:**
  * `doInline` (Impact: 3592.9 | O(2^N) | DB: 81)
  * `doInline` (Impact: 15.1 | O(2^N))
  * `recordTransformation` (Impact: 12.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `args: 44`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 197`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 32`
* *Defense:* `safety: 30`, `test: 6`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` org.jetbrains.org.objectweb.asm.Type, org.jetbrains.kotlin.codegen.inline.coroutines.markNoinlineLambdaIfSuspend, org.jetbrains.kotlin.codegen.*, org.jetbrains.kotlin.codegen.inline.coroutines.surroundInvokesWithSuspendMarkersIfNeeded, org.jetbrains.kotlin.codegen.optimization.fixStack.*, org.jetbrains.kotlin.codegen.optimization.ApiVersionCallsPreprocessingMethodTransformer, org.jetbrains.kotlin.codegen.optimization.temporaryVals.TemporaryVariablesEliminationTransformer, org.jetbrains.kotlin.codegen.optimization.common.isMeaningful...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/libbacktrace/c/dwarf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.016 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.255 IQR)
- **Top Global Matches:** file_cluster_8: 14.016, file_cluster_13: 14.223, file_cluster_0: 14.31
- **Magnitude:** 3799.8 | **LOC:** 4416 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 175
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (15.3414%)
**Top Internal Functions/Classes:**
  * `build_address_map` (Impact: 2113.9 | O(N^6) | DB: 175)
    * *Intent:* /* The name of the function. */
  * `read_function_info` (Impact: 64.9 | O(N^1) | DB: 21)
  * `backtrace_dwarf_add` (Impact: 40.9 | O(N^1) | DB: 9)
  * `dwarf_fileline` (Impact: 29.2 | O(N^1) | DB: 7)
    * *Intent:* // Skip attributes.
  * `build_dwarf_data` (Impact: 16.8 | O(N^1) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 293`, `args: 33`, `func_start: 16`, `class_start: 70`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1187`, `fragile_debt: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 297`, `import: 8`
* *Defense:* `safety: 23`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` string.h, backtrace.h, stdlib.h, config.h, filenames.h, errno.h, types.h, internal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/daemon/src/org/jetbrains/kotlin/daemon/CompileServiceImpl.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.534 IQR)
- **Top Global Matches:** file_cluster_13: 12.534, file_cluster_8: 12.668, file_cluster_11: 12.68
- **Magnitude:** 3798.8 | **LOC:** 1351 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (62.8255%), Tech Debt (68.1542%)
**Top Internal Functions/Classes:**
  * `compileImpl` (Impact: 3251.8 | O(2^N) | DB: 53)
  * `gracefulShutdown` (Impact: 71.5 | O(N^6) | DB: 2)
  * `getPerformanceMetrics` (Impact: 68.4 | O(N^5) | DB: 7)
  * `shutdownWithDelay` (Impact: 27.0 | O(N^5) | DB: 4)
  * `exceptionLoggingTimerThread` (Impact: 25.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `args: 93`, `func_start: 78`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 159`, `planned_debt: 15`, `duplicate_logic: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 10`, `api: 3`, `import: 75`
* *Defense:* `safety: 31`, `sync_locks: 17`, `immutability_locks: 90`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` org.jetbrains.kotlin.build.report.DoNothingBuildReporter, org.jetbrains.kotlin.incremental.js.IncrementalDataProvider, org.jetbrains.kotlin.incremental.components.LookupTracker, com.intellij.openapi.vfs.impl.jar.CoreJarFileSystem, com.intellij.openapi.util.Disposer, org.jetbrains.kotlin.incremental.multiproject.EmptyModulesApiHistory, org.jetbrains.kotlin.incremental.multiproject.ModulesApiHistoryJs, org.jetbrains.kotlin.load.kotlin.incremental.components.IncrementalCompilationComponents...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiRawFirBuilder.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.178 IQR)
- **Top Global Matches:** file_cluster_13: 14.178, file_cluster_11: 14.28, file_cluster_0: 14.285
- **Magnitude:** 3682.6 | **LOC:** 3963 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 191
- **Risk Profile:** Cognitive Load (83.2172%), Tech Debt (15.0047%)
**Top Internal Functions/Classes:**
  * `toFirProperty` (Impact: 1237.5 | O(2^N) | DB: 191)
  * `toFirValueParameter` (Impact: 226.0 | O(2^N) | DB: 17)
  * `toFirDeclaration` (Impact: 187.7 | O(2^N) | DB: 2)
  * `toFirEnumEntry` (Impact: 144.8 | O(2^N) | DB: 37)
  * `visitCallExpression` (Impact: 99.3 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `args: 100`, `func_start: 68`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 773`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 24`, `concurrency: 6`, `import: 54`
* *Defense:* `safety: 103`, `doc: 5`, `immutability_locks: 152`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` org.jetbrains.kotlin.fir.types.impl.ConeClassLikeTypeImpl, org.jetbrains.kotlin.fir.declarations.utils.*, org.jetbrains.kotlin.fir.references.builder.buildExplicitSuperReference, org.jetbrains.kotlin.fir.references.builder.buildSimpleNamedReference, org.jetbrains.kotlin.fir.expressions.*, org.jetbrains.kotlin.fir.types.builder.*, org.jetbrains.kotlin.fir.extensions.extensionService, org.jetbrains.kotlin.fir.symbols.impl.*...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `libraries/stdlib/src/kotlin/time/Duration.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.921 IQR)
- **Top Global Matches:** file_cluster_0: 12.921, file_cluster_8: 13.181, file_cluster_7: 13.325
- **Magnitude:** 3620.56 | **LOC:** 1629 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (34.6843%), Tech Debt (24.678%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 2507.5 | O(2^N) | DB: 6)
    * *Intent:* * If a duration-returning operation provided in `kotlin.time` produces a duration value that doesn't...
  * `parseDefaultStringFormat` (Impact: 262.3 | O(N^5) | DB: 24)
    * *Intent:* /** * Parses default duration format (e.g., `"1h 30m"`, `"45s"`, `"500ms"`). * Note: While `"Infinit...
  * `parseIsoStringFormat` (Impact: 238.3 | O(N^5) | DB: 13)
    * *Intent:* /** * Parses ISO-8601 duration format (e.g., `"PT1H30M45S"`). * * @param value the full input string...
  * `parse` (Impact: 81.1 | O(N^4) | DB: 7)
    * *Intent:* /** * Parses a long integer from the string starting at the specified index. * * @param value The st...
  * `parseDuration` (Impact: 57.1 | O(N^3) | DB: 3)
    * *Intent:* /** * Parses a duration string in either ISO-8601 or default format. * * @param value the string to ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `args: 77`, `func_start: 66`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 167`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 117`, `import: 3`
* *Defense:* `safety: 157`, `doc: 154`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` kotlin.math.*, kotlin.jvm.JvmInline, kotlin.contracts.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinParsing.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.714 IQR)
- **Top Global Matches:** file_cluster_8: 9.714, file_cluster_7: 10.346, file_cluster_0: 10.446
- **Magnitude:** 3412.28 | **LOC:** 2820 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (16.4284%), Tech Debt (33.9766%)
**Top Internal Functions/Classes:**
  * `parseContextParameterOrReceiverList` (Impact: 2450.5 | O(2^N))
  * `doParseModifierListBody` (Impact: 294.0 | O(2^N))
  * `parseCommonDeclaration` (Impact: 151.6 | O(N^5))
    * *Intent:* /* * toplevelObject * : package * : class * : extension * : function * : property * : typeAlias * : ...
  * `parsePackageName` (Impact: 86.4 | O(N^5))
  * `parseImportDirective` (Impact: 75.7 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 143`, `args: 108`, `func_start: 253`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 8`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 17`, `import: 14`
* *Defense:* `safety: 22`, `doc: 5`, `test: 16`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` org.jetbrains.kotlin.lexer.KtTokens.*, com.intellij.openapi.diagnostic.Logger, com.intellij.psi.tree.IElementType, org.jetbrains.annotations.Contract, org.jetbrains.kotlin.parsing.KotlinWhitespaceAndCommentsBindersKt.TRAILING_ALL_BINDER, org.jetbrains.kotlin.lexer.KtTokens, java.util.function.Supplier, org.jetbrains.annotations.NotNull...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptStubConverter.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.281 IQR)
- **Top Global Matches:** file_cluster_13: 13.281, file_cluster_8: 13.389, file_cluster_17: 13.612
- **Magnitude:** 3314.9 | **LOC:** 1612 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (37.9347%), Tech Debt (9.4231%)
**Top Internal Functions/Classes:**
  * `checkIfAnnotationValueMatches` (Impact: 463.3 | O(2^N))
  * `extractMethodSignatureTypes` (Impact: 375.4 | O(N^6) | DB: 5)
  * `convertMethod` (Impact: 351.6 | O(N^5) | DB: 2)
  * `convertFirType` (Impact: 181.4 | O(2^N))
  * `checkIfValidTypeName` (Impact: 168.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `args: 80`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 68`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 9`, `import: 86`
* *Defense:* `safety: 182`, `test: 3`, `immutability_locks: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` org.jetbrains.kotlin.fir.symbols.impl.FirClassSymbol, org.jetbrains.kotlin.descriptors.annotations.Annotations, org.jetbrains.kotlin.builtins.jvm.JavaToKotlinClassMap, org.jetbrains.kotlin.resolve.descriptorUtil.isCompanionObject, org.jetbrains.kotlin.KtPsiSourceElement, org.jetbrains.kotlin.fir.resolve.transformers.resolveToPackageOrClass, org.jetbrains.kotlin.codegen.coroutines.SUSPEND_FUNCTION_COMPLETION_PARAMETER_NAME, org.jetbrains.kotlin.kapt.base.javac.reportKaptError...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirExpressionBuilder.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.286 IQR)
- **Top Global Matches:** file_cluster_13: 14.286, file_cluster_8: 14.332, file_cluster_11: 14.455
- **Magnitude:** 3013.54 | **LOC:** 1743 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (42.4267%), Tech Debt (16.4528%)
**Top Internal Functions/Classes:**
  * `convertQualifiedExpression` (Impact: 164.6 | O(N^6) | DB: 18)
  * `convertCallExpression` (Impact: 159.6 | O(N^6) | DB: 27)
  * `convertBinaryExpressionFallback` (Impact: 143.6 | O(N^6) | DB: 14)
  * `convertWhenExpression` (Impact: 130.9 | O(N^6) | DB: 43)
  * `wrapExpressionIfNeeded` (Impact: 112.7 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `args: 90`, `func_start: 50`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 865`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 6`, `import: 50`
* *Defense:* `safety: 45`, `doc: 97`, `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` org.jetbrains.kotlin.fir.references.FirNamedReference, org.jetbrains.kotlin.fir.expressions.impl.buildSingleExpressionBlock, org.jetbrains.kotlin.fir.lightTree.fir.addDestructuringStatements, org.jetbrains.kotlin.fir.references.builder.buildExplicitSuperReference, org.jetbrains.kotlin.fir.references.builder.buildSimpleNamedReference, com.intellij.util.diff.FlyweightCapableTreeStructure, org.jetbrains.kotlin.fir.expressions.*, org.jetbrains.kotlin.name.SpecialNames...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirDeclarationBuilder.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.345 IQR)
- **Top Global Matches:** file_cluster_13: 14.345, file_cluster_2: 14.408, file_cluster_8: 14.537
- **Magnitude:** 2976.24 | **LOC:** 2974 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 303
- **Risk Profile:** Cognitive Load (60.0877%), Tech Debt (9.017%)
**Top Internal Functions/Classes:**
  * `convertClass` (Impact: 1435.2 | O(N^6) | DB: 303)
  * `convertValueParameter` (Impact: 89.1 | O(N^6) | DB: 22)
  * `convertBlockExpressionWithoutBuilding` (Impact: 85.5 | O(N^6) | DB: 3)
    * *Intent:* /** * @see org.jetbrains.kotlin.parsing.KotlinParsing.parseBlockExpression */
  * `parsePackageParts` (Impact: 57.0 | O(N^6) | DB: 1)
  * `convertAnnotationEntry` (Impact: 52.7 | O(N^4) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `args: 118`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 885`, `planned_debt: 5`
* *Architecture:* `api: 5`, `import: 51`
* *Defense:* `safety: 48`, `doc: 78`, `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` org.jetbrains.kotlin.fir.types.impl.ConeClassLikeTypeImpl, org.jetbrains.kotlin.fir.declarations.utils.*, org.jetbrains.kotlin.fir.references.builder.buildExplicitSuperReference, org.jetbrains.kotlin.fir.references.builder.buildSimpleNamedReference, com.intellij.util.diff.FlyweightCapableTreeStructure, org.jetbrains.kotlin.fir.expressions.*, org.jetbrains.kotlin.fir.lightTree.fir.*, org.jetbrains.kotlin.fir.types.builder.*...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/frontend/src/org/jetbrains/kotlin/resolve/DeclarationsChecker.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.498 IQR)
- **Top Global Matches:** file_cluster_8: 11.498, file_cluster_13: 11.7, file_cluster_2: 11.724
- **Magnitude:** 2830.12 | **LOC:** 1162 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (26.7135%), Tech Debt (22.1169%)
**Top Internal Functions/Classes:**
  * `withTrace` (Impact: 569.4 | O(2^N))
  * `checkPropertyInitializer` (Impact: 388.1 | O(N^6) | DB: 2)
  * `reportMustBeInitialized` (Impact: 307.9 | O(2^N))
  * `checkFunction` (Impact: 293.7 | O(2^N))
  * `isImplementingMethodOfAnyInternal` (Impact: 136.3 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `args: 66`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 28`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 1`, `import: 31`
* *Defense:* `safety: 72`, `test: 1`, `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` org.jetbrains.kotlin.resolve.inline.isInlineOnly, org.jetbrains.kotlin.lexer.KtTokens, org.jetbrains.kotlin.types.typeUtil.contains, org.jetbrains.kotlin.types.typeUtil.constituentTypes, org.jetbrains.kotlin.types.typeUtil.isArrayOfNothing, org.jetbrains.kotlin.config.LanguageVersionSettings, org.jetbrains.kotlin.builtins.KotlinBuiltIns, org.jetbrains.kotlin.resolve.source.KotlinSourceElement...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/frontend/src/org/jetbrains/kotlin/resolve/constants/evaluate/ConstantExpressionEvaluator.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.672 IQR)
- **Top Global Matches:** file_cluster_8: 12.672, file_cluster_13: 12.79, file_cluster_11: 13.121
- **Magnitude:** 2726.02 | **LOC:** 1294 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (30.1947%), Tech Debt (50.5109%)
**Top Internal Functions/Classes:**
  * `evaluateCall` (Impact: 263.7 | O(N^6) | DB: 6)
  * `checkInnerPartsOfCompileTimeConstant` (Impact: 151.0 | O(N^6))
  * `visitBinaryExpression` (Impact: 116.2 | O(N^5) | DB: 7)
  * `visitConstantExpression` (Impact: 111.9 | O(N^5) | DB: 7)
  * `visitSimpleNameExpression` (Impact: 111.2 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 466`, `args: 85`, `func_start: 73`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 100`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 23`, `import: 49`
* *Defense:* `safety: 110`, `test: 4`, `immutability_locks: 158`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` org.jetbrains.kotlin.resolve.calls.util.getEffectiveExpectedType, org.jetbrains.kotlin.lexer.KtTokens, org.jetbrains.kotlin.resolve.constants.evaluate.CompileTimeType.*, org.jetbrains.kotlin.resolve.descriptorUtil.isCompanionObject, org.jetbrains.kotlin.diagnostics.reportDiagnosticOnce, org.jetbrains.kotlin.config.LanguageVersionSettings, org.jetbrains.kotlin.builtins.KotlinBuiltIns, org.jetbrains.kotlin.resolve.calls.model.ResolvedCall...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `compiler/ir/backend.jvm/codegen/src/org/jetbrains/kotlin/backend/jvm/codegen/ExpressionCodegen.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.22 IQR)
- **Top Global Matches:** file_cluster_13: 12.22, file_cluster_8: 12.341, file_cluster_11: 12.496
- **Magnitude:** 2643.38 | **LOC:** 1622 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (63.1426%), Tech Debt (11.3295%)
**Top Internal Functions/Classes:**
  * `resultIsActuallyAny` (Impact: 2291.1 | O(2^N) | DB: 14)
  * `getSuspensionPointKind` (Impact: 73.6 | O(2^N))
  * `visitVariable` (Impact: 32.5 | O(N^5) | DB: 2)
  * `handleBlock` (Impact: 32.3 | O(N^3) | DB: 1)
  * `visitDelegatingConstructorCall` (Impact: 22.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `args: 65`, `func_start: 55`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 68`, `dead_code: 4`, `planned_debt: 7`
* *Architecture:* `api: 10`, `import: 64`
* *Defense:* `safety: 56`, `test: 4`, `immutability_locks: 148`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` org.jetbrains.org.objectweb.asm.Type, org.jetbrains.kotlin.ir.symbols.IrValueParameterSymbol, org.jetbrains.kotlin.backend.jvm.intrinsics.JavaClassProperty, org.jetbrains.kotlin.ir.IrElement, org.jetbrains.kotlin.descriptors.CallableDescriptor, org.jetbrains.kotlin.backend.jvm.ir.*, org.jetbrains.kotlin.codegen.*, org.jetbrains.kotlin.codegen.state.JvmBackendConfig...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `compiler/fir/dump/src/org/jetbrains/kotlin/fir/dump/HtmlFirDump.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.763 IQR)
- **Top Global Matches:** file_cluster_8: 11.763, file_cluster_13: 12.224, file_cluster_7: 12.376
- **Magnitude:** 2606.1 | **LOC:** 1897 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (12.2536%), Tech Debt (99.9646%)
**Top Internal Functions/Classes:**
  * `describeVerbose` (Impact: 128.9 | O(2^N) | DB: 1)
  * `generate` (Impact: 113.5 | O(2^N))
  * `generate` (Impact: 94.6 | O(2^N))
  * `generate` (Impact: 87.0 | O(2^N))
  * `generate` (Impact: 86.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `args: 164`, `func_start: 137`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 62`, `duplicate_logic: 69`, `orphaned_logic: 3`
* *Architecture:* `io: 14`, `api: 3`, `concurrency: 1`, `import: 42`
* *Defense:* `safety: 142`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` org.jetbrains.kotlin.fir.expressions.impl.FirUnitExpression, org.jetbrains.kotlin.fir.declarations.utils.classId, org.jetbrains.kotlin.fir.resolve.diagnostics.ConeInapplicableCandidateError, org.jetbrains.kotlin.fir.resolve.toSymbol, org.jetbrains.kotlin.fir.expressions.*, org.jetbrains.kotlin.types.ConstantValueKind, java.io.File, org.jetbrains.kotlin.fir.references.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/libbacktrace/c/macho.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.328 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.774 IQR)
- **Top Global Matches:** file_cluster_8: 13.328, file_cluster_13: 13.521, file_cluster_0: 13.655
- **Magnitude:** 2592.66 | **LOC:** 1379 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (85.241%), Tech Debt (10.4233%)
**Top Internal Functions/Classes:**
  * `macho_add_dsym` (Impact: 1289.6 | O(2^N) | DB: 88)
  * `macho_add_symtab` (Impact: 193.6 | O(N^2) | DB: 47)
  * `macho_add_fat` (Impact: 97.9 | O(N^2) | DB: 19)
  * `macho_add_dwarf_segment` (Impact: 77.9 | O(N^2) | DB: 6)
  * `macho_syminfo` (Impact: 50.2 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 139`, `args: 29`, `func_start: 12`, `class_start: 47`
* *Risk/State:* `state_mutation: 514`, `fragile_debt: 2`
* *Architecture:* `api: 290`, `import: 8`
* *Defense:* `safety: 13`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` string.h, backtrace.h, dyld.h, dirent.h, stdlib.h, config.h, types.h, internal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirDataFlowAnalyzer.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.064 IQR)
- **Top Global Matches:** file_cluster_13: 13.064, file_cluster_8: 13.073, file_cluster_0: 13.176
- **Magnitude:** 2432.82 | **LOC:** 1931 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (70.7413%), Tech Debt (9.2653%)
**Top Internal Functions/Classes:**
  * `buildSmartCastStatement` (Impact: 1970.6 | O(N^6) | DB: 30)
  * `mapElement` (Impact: 284.0 | O(N^6) | DB: 2)
  * `createSnapshot` (Impact: 16.8 | O(2^N) | DB: 4)
  * `reset` (Impact: 5.4 | O(2^N) | DB: 1)
    * *Intent:* /** * Replaces all state of this [DataFlowAnalyzerContext] with those from [source]. *
  * `newAssignmentIndex` (Impact: 5.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `args: 100`, `func_start: 78`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 111`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 5`, `concurrency: 13`, `import: 33`
* *Defense:* `safety: 92`, `doc: 12`, `immutability_locks: 161`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` org.jetbrains.kotlin.fir.resolve.calls.ImplicitValue, org.jetbrains.kotlin.fir.expressions.*, org.jetbrains.kotlin.types.ConstantValueKind, org.jetbrains.kotlin.fir.references.*, org.jetbrains.kotlin.fir.declarations.utils.lambdaArgumentParent, org.jetbrains.kotlin.contracts.description.LogicOperationKind, org.jetbrains.kotlin.fir.resolve.substitution.substitutorByMap, kotlinx.collections.immutable.toPersistentSet...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `compiler/frontend/cfg/src/org/jetbrains/kotlin/cfg/ControlFlowProcessor.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.113 IQR)
- **Top Global Matches:** file_cluster_8: 12.113, file_cluster_13: 12.275, file_cluster_7: 12.66
- **Magnitude:** 2402.34 | **LOC:** 1701 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (30.2992%), Tech Debt (30.691%)
**Top Internal Functions/Classes:**
  * `visitWhenExpression` (Impact: 115.3 | O(N^6) | DB: 3)
  * `visitBinaryExpression` (Impact: 114.0 | O(N^6))
  * `generateTryAndCatches` (Impact: 93.9 | O(N^6) | DB: 8)
  * `visitAssignment` (Impact: 85.8 | O(N^5) | DB: 5)
  * `getCorrespondingLoop` (Impact: 85.8 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `args: 94`, `func_start: 88`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 126`, `planned_debt: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 37`, `import: 50`
* *Defense:* `safety: 64`, `test: 4`, `immutability_locks: 174`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` org.jetbrains.kotlin.contracts.description.isDefinitelyVisited, org.jetbrains.kotlin.resolve.bindingContextUtil.getEnclosingFunctionDescriptor, org.jetbrains.kotlin.resolve.bindingContextUtil.recordUsedAsExpression, org.jetbrains.kotlin.resolve.descriptorUtil.parentsWithSelf, org.jetbrains.kotlin.types.typeUtil.isUnit, org.jetbrains.kotlin.contracts.description.EventOccurrencesRange, org.jetbrains.kotlin.resolve.scopes.receivers.*, org.jetbrains.kotlin.resolve.BindingTrace...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `libraries/stdlib/jvm/src/kotlin/reflect/TypesJVM.kt` (KOTLIN) | Magnitude: 56.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, args: 29, func_start: 29, branch: 23
- `libraries/tools/abi-validation/abi-tools-tests/src/compiling/kotlin/cases/marker/marker.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, decorators: 5, class_start: 4, state_mutation: 2
- `compiler/psi/psi-impl/testData/psi/secondaryConstructors/basic.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, decorators: 4, func_start: 3, duplicate_logic: 3
- `native/objcexport-header-generator/testData/dependencies/propertyAnnotation/Foo.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 4, state_mutation: 2, immutability_locks: 2, class_start: 1
- `compiler/testData/asJava/lightClasses/lightClassByPsi/delegatesWithAnnotations.java` (JAVA) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 19, api: 14, indent_spaces: 13, decorators: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirLocalVariableAssignmentAnalyzer.kt` (KOTLIN) | Magnitude: 431.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 185, branch: 63, state_mutation: 51, args: 27
- `compiler/ir/ir.interpreter/src/org/jetbrains/kotlin/ir/interpreter/proxy/CommonProxy.kt` (KOTLIN) | Magnitude: 242.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, branch: 44, state_mutation: 31, panics_and_aborts: 15
- `compiler/resolution.common/src/org/jetbrains/kotlin/types/AbstractTypeApproximator.kt` (KOTLIN) | Magnitude: 777.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 147, branch: 78, immutability_locks: 22, panics_and_aborts: 21
- `js/js.translator/testData/box/crossModuleRef/topLevelProperty.kt` (KOTLIN) | Magnitude: 0.03 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 11, indent_spaces: 8, state_mutation: 6, panics_and_aborts: 6
- `js/js.translator/testData/box/crossModuleRefIR/topLevelProperty.kt` (KOTLIN) | Magnitude: 0.03 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 11, indent_spaces: 8, state_mutation: 6, panics_and_aborts: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/utils/reflectionUtils.kt` (KOTLIN) | Magnitude: 0.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 12, indent_spaces: 12, doc: 4, reflection_metaprogramming: 4
- `js/js.translator/testData/box/reflection/kClass.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 11, indent_spaces: 7, safety: 5, branch: 1
- `libraries/stdlib/src/kotlin/text/UHexExtensions.kt` (KOTLIN) | Magnitude: 74.72 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 44, decorators: 36, reflection_metaprogramming: 22, api: 12
- `compiler/testData/diagnostics/tests/testsWithExplicitApi/inlineClasses.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 4, reflection_metaprogramming: 4, immutability_locks: 4
- `js/js.translator/testData/box/esModules/jsModule/externalClass.mjs` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 4, structural_boundaries: 3, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `compiler/testData/compileJavaAgainstKotlin/method/MapOfKString.java` (JAVA) | Magnitude: 0.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 7, scientific: 4, indent_spaces: 4, generics: 3
- `compiler/arguments/src/org/jetbrains/kotlin/arguments/dsl/types/CompatqualAnnotationsMode.kt` (KOTLIN) | Magnitude: 23.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 8, import: 5, immutability_locks: 3
- `compiler/arguments/src/org/jetbrains/kotlin/arguments/dsl/types/LambdasMode.kt` (KOTLIN) | Magnitude: 23.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 8, import: 5, immutability_locks: 3
- `compiler/arguments/src/org/jetbrains/kotlin/arguments/dsl/types/SamConversionsMode.kt` (KOTLIN) | Magnitude: 23.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 8, import: 5, immutability_locks: 3
- `compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/SharedApiClassesClassLoader.kt` (KOTLIN) | Magnitude: 48.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, branch: 8, encapsulation: 7, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `js/js.translator/testData/box/esModules/jsModule/externalConstructor.mjs` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, branch: 1, structural_boundaries: 1, args: 1
- `compiler/testData/diagnostics/tests/when/ExhaustiveSelftype.fir.kt` (KOTLIN) | Magnitude: 0.1 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 51, indent_spaces: 28, branch: 17, safety: 15
- `compiler/testData/diagnostics/tests/controlStructures/ifWhenWithoutElse.fir.kt` (KOTLIN) | Magnitude: 0.14 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 58, args: 42, state_mutation: 42, immutability_locks: 27
- `compiler/testData/diagnostics/tests/controlStructures/ifWhenWithoutElse.kt` (KOTLIN) | Magnitude: 0.14 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 58, args: 42, state_mutation: 42, immutability_locks: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/projectStructure/KaModule.kt` (KOTLIN) | Magnitude: 47.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, doc: 32, immutability_locks: 32, api: 31
- `build-common/src/org/jetbrains/kotlin/idea/explicitDefaultSubstitutors.kt` (KOTLIN) | Magnitude: 9.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, generics: 10, immutability_locks: 10, import: 8
- `compiler/fir/analysis-tests/testData/resolve/overloadResolution/discriminateSuspendFunctionTypeAfter.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 16, generics: 15, func_start: 14, indent_spaces: 14
- `compiler/testData/diagnostics/nativeTests/specialBackendChecks/cInterop/t43.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 1, func_start: 1, safety_bypasses: 1, decorators: 1
- `compiler/testData/diagnostics/nativeTests/specialBackendChecks/cInterop/t44.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 1, func_start: 1, safety_bypasses: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `compiler/fir/modularized-tests/testFixtures/org/jetbrains/kotlin/fir/modularizedTestConfiguration.kt` (KOTLIN) | Magnitude: 92.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 67, state_mutation: 28, branch: 16, immutability_locks: 16
- `libraries/tools/abi-comparator/comparator.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: safety_bypasses: 10, args: 4, state_mutation: 4, io: 2
- `compiler/testData/diagnostics/tests/smartCasts/varnotnull/inference.fir.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 15, indent_spaces: 14, immutability_locks: 2, branch: 1
- `compiler/testData/diagnostics/tests/smartCasts/varnotnull/inference.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 15, indent_spaces: 14, explicit_casts: 2, immutability_locks: 2
- `native/swift/swift-export-standalone-integration-tests/simple/testData/generation/functional_type/golden_result/optional_closure/optional_closure.swift` (SWIFT) | Magnitude: 0.09 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 26, branch: 15, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirKeywordUtils.kt` (KOTLIN) | Magnitude: 35.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, ui_framework: 54, immutability_locks: 20, import: 19
- `compiler/frontend/src/org/jetbrains/kotlin/resolve/checkers/ConstModifierChecker.kt` (KOTLIN) | Magnitude: 115.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, branch: 26, ui_framework: 12, panics_and_aborts: 11
- `analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/modifiers/renderers/KaRendererVisibilityModifierProvider.kt` (KOTLIN) | Magnitude: 246.4 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, branch: 19, ui_framework: 16, safety: 10
- `compiler/testData/ir/irText/firProblems/timesInBuilder.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, args: 7, func_start: 7, ui_framework: 4
- `native/swift/swift-export-standalone-integration-tests/simple/testData/execution/generics/generics.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 10, func_start: 10, generics: 10, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `compiler/testData/diagnostics/tests/suspendConversion/inGenericArgument.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, state_mutation: 6, concurrency: 6, branch: 2
- `kotlin-native/runtime/src/gc/common/cpp/TracingGCTest.hpp` (CPP) | Magnitude: 1692.34 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 998, indent_spaces: 953, structural_boundaries: 206, test: 155
- `kotlin-native/runtime/src/alloc/common/cpp/RunLoopFinalizerProcessor.hpp` (CPP) | Magnitude: 57.32 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 36, concurrency: 12, import: 10
- `kotlin-native/runtime/src/gcScheduler/common/cpp/MutatorAssistsTest.cpp` (CPP) | Magnitude: 792.58 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 398, indent_spaces: 385, args: 79, branch: 60
- `kotlin-native/runtime/src/main/cpp/concurrent/ParallelProcessor.hpp` (CPP) | Magnitude: 363.68 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 209, state_mutation: 88, structural_boundaries: 53, pointers: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `compiler/testData/diagnostics/tests/inference/lambdaParameterTypeInElvis.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 4, func_start: 4, planned_debt: 4, indent_spaces: 3
- `compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/compat.kt` (KOTLIN) | Magnitude: 25.68 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, sec_high_risk_execution: 12, immutability_locks: 5, branch: 4
- `libraries/tools/kotlin-gradle-plugin/build.gradle.kts` (KOTLIN) | Magnitude: 6.9 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 425, state_mutation: 44, immutability_locks: 26, branch: 24
- `compiler/testData/diagnostics/tests/inference/kt63982.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 4, indent_spaces: 4, branch: 3, planned_debt: 3
- `kotlin-native/performance/ring/src/commonMain/kotlin/org/jetbrains/ring/DeltaBlueBenchmark.kt` (KOTLIN) | Magnitude: 399.04 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 269, state_mutation: 159, branch: 63, args: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `native/swift/sir-printer/testData/commented_class.golden.swift` (SWIFT) | Magnitude: 0.01 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 1, class_start: 1, api: 1
- `libraries/stdlib/jvm/src/kotlin/io/files/FilePathComponents.kt` (KOTLIN) | Magnitude: 39.22 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, io: 17, doc: 15, api: 13
- `compiler/ir/ir.tree/src/org/jetbrains/kotlin/ir/util/IrElementConstructorIndicator.kt` (KOTLIN) | Magnitude: 12.04 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 1, api: 1, doc: 1, globals: 1
- `analysis/analysis-api/testData/components/resolver/singleByPsi/kDoc/blockTags/paramBlockTag.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, class_start: 1, state_mutation: 1
- `analysis/analysis-api/testData/components/resolver/singleByPsi/kDoc/blockTags/prioritiesWithSameNames.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, class_start: 1, state_mutation: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/restrictedAnalysis/KaBaseRestrictedAnalysisException.kt` (KOTLIN) | Magnitude: 12.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 2, class_start: 1, api: 1, import: 1
- `analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/KaEngineService.kt` (KOTLIN) | Magnitude: 13.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: class_start: 1, api: 1, doc: 1, decorators: 1
- `analysis/analysis-api-platform-interface/src/org/jetbrains/kotlin/analysis/api/platform/restrictedAnalysis/KaRestrictedAnalysisException.kt` (KOTLIN) | Magnitude: 13.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: class_start: 1, api: 1, doc: 1, decorators: 1
- `analysis/analysis-api/testData/components/resolver/allByPsi/contextSensitiveResolution/otherExpectedTypePositions/notNullAssertionEnum.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 12, safety_bypasses: 7, generics: 4, args: 3
- `compiler/fir/analysis-tests/testData/resolve/arguments/genericVarargInferredToNullableNothing.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 6, func_start: 6, generics: 6, indent_spaces: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `kotlin-native/tools/compiler-cache-invalidator/build.gradle.kts` (KOTLIN) | Magnitude: 1.63 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, state_mutation: 1, dead_code: 1
- `analysis/analysis-api/testData/components/scopeProvider/combinedDeclaredMemberScope/innerClass.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 6, indent_spaces: 4, dead_code: 1
- `analysis/analysis-api/testData/components/scopeProvider/declaredMemberScope/innerClass.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 6, indent_spaces: 4, dead_code: 1
- `analysis/analysis-api/testData/components/scopeProvider/memberScope/innerClass.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 6, indent_spaces: 4, dead_code: 1
- `analysis/analysis-api/testData/components/scopeProvider/staticDeclaredMemberScope/innerClass.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 6, indent_spaces: 4, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/internal/wrappers/KotlinWrapperPre2_4_0.kt` -> Churn: **100.0%** | Cog Load: 15.4222% | Debt: 91.5681%
- `compiler/build-tools/kotlin-build-tools-impl/src/main/kotlin/org/jetbrains/kotlin/buildtools/internal/arguments/CompilerArgumentValueAdapter.kt` -> Churn: **100.0%** | Cog Load: 18.3952% | Debt: 99.5656%
- `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/FirCallCompletionResultsWriterTransformer.kt` -> Churn: **94.64%** | Cog Load: 45.7921% | Debt: 95.877%
- `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/main/main.kt` -> Churn: **88.56%** | Cog Load: 23.8237% | Debt: 76.1462%
- `compiler/build-tools/kotlin-build-tools-options-generator/src/org/jetbrains/kotlin/buildtools/options/generator/BtaCompilerArgument.kt` -> Churn: **81.55%** | Cog Load: 53.0491% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt` -> **Denis.Zharkov** (100.0% isolated ownership) | Magnitude: 5410.22
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt` -> **Denis.Zharkov** (100.0% isolated ownership) | Magnitude: 4933.94
- `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt` -> **Derek Xu** (100.0% isolated ownership) | Magnitude: 4113.22
- `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/IrSourcePrinter.kt` -> **Derek Xu** (100.0% isolated ownership) | Magnitude: 2308.08
- `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/analysis/Stability.kt` -> **Derek Xu** (100.0% isolated ownership) | Magnitude: 1592.8

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

- `compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt` -> **Severity: 697.883** (Blast Radius: 6.984 * Doc Risk: 99.926%)
- `core/compiler.common/src/org/jetbrains/kotlin/name/Name.java` -> **Severity: 474.0** (Blast Radius: 4.74 * Doc Risk: 100.0%)
- `analysis/symbol-light-classes/testData/additionalFiles/NotNull.java` -> **Severity: 446.091** (Blast Radius: 8.08 * Doc Risk: 55.2093%)
- `core/compiler.common/src/org/jetbrains/kotlin/name/FqName.kt` -> **Severity: 358.456** (Blast Radius: 3.593 * Doc Risk: 99.765%)
- `analysis/symbol-light-classes/testData/additionalFiles/Nullable.java` -> **Severity: 225.011** (Blast Radius: 4.429 * Doc Risk: 50.804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
