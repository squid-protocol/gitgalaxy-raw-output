# ARCHITECTURAL_BRIEF: kotlin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/JetBrains/kotlin` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 102961 analyzed artifact(s), 2431379 LOC.
- **Load-bearing artifact:** `compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt` -- 1310 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrorsDefaultMessages.kt` -- pulls in 934 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` at magnitude 8941.72 (structural weight, not risk).
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
| Total Artifacts | 119907 |
| Analyzed Artifacts (Scanned) | 102961 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16946 |
| Total LOC | 2431379 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 85.9% |
| Dominant Lang | KOTLIN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6523 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1097 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.2204 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 925 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| KOTLIN | 62120 | 2115071 | 60.3% |
| PLAINTEXT | 34478 | 5 | 33.5% |
| JAVA | 2889 | 166612 | 2.8% |
| CPP | 521 | 53911 | 0.5% |
| MAKEFILE | 493 | 2788 | 0.5% |
| XML | 444 | 0 | 0.4% |
| GROOVY | 372 | 5931 | 0.4% |
| OBJECTIVE-C | 352 | 15803 | 0.3% |
| JAVASCRIPT | 324 | 5577 | 0.3% |
| SWIFT | 282 | 28923 | 0.3% |
| MARKDOWN | 185 | 0 | 0.2% |
| TYPESCRIPT | 159 | 10213 | 0.2% |
| JSON | 102 | 3664 | 0.1% |
| C | 85 | 10764 | 0.1% |
| SHELL | 42 | 1417 | 0.0% |
| PHP | 30 | 6094 | 0.0% |
| BATCH | 18 | 663 | 0.0% |
| PROTO | 17 | 1933 | 0.0% |
| RUBY | 13 | 179 | 0.0% |
| M4 | 7 | 9 | 0.0% |
| HTML | 6 | 61 | 0.0% |
| CSS | 5 | 231 | 0.0% |
| PYTHON | 5 | 1249 | 0.0% |
| DOCKERFILE | 5 | 158 | 0.0% |
| YAML | 3 | 87 | 0.0% |
| CSV | 2 | 22 | 0.0% |
| SCALA | 1 | 5 | 0.0% |
| YACC | 1 | 9 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `5.208`
> **Composition Archetype:** `Flat Modular Platform` (z +5.21; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 54%, Interface Declarations Files 9%, Declarative / Non-Code 7%, Parameter Forwarders Files 7%, Generic / Templated Code Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 68298 | 66.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 34662 | 33.7% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16946*

**Composition by Extension & Reason:**
- `.kt`: 5831x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 125x Excluded: Neighborhood Micro-Mass Limit Exceeded, 104x Excluded (Machine-Generated Source Code Signature: 21 LOC)
- `.txt`: 1134x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 752x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.java`: 1671x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 6 exceeds 500 chars), 3x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.info`: 970x Excluded (Unsupported Extension: '.info'), 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kts`: 587x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.out`: 560x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 224x Unsupported Format (.undeterminable), 155x Excluded (Unsupported Extension: '.instructions'), 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.log`: 477x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.args`: 449x Excluded (Unsupported Extension: '.args')
- `.disabled`: 373x Unsupported Format (.disabled)
- `.def`: 55x Statistical Anomaly (Z-Score: -3372.50 < -4.55), 48x Statistical Anomaly (Z-Score: -5620.83 < -4.55), 35x Statistical Anomaly (Z-Score: -50587.50 < -4.55)
- `.new`: 192x Excluded (Unsupported Extension: '.new'), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.new)
- `.pom`: 192x Unsupported Format (.pom)
- `.json`: 161x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 6753 LOC), 1x Excluded (Massive Static Asset Blob: 17658 LOC)
- `.values`: 153x Excluded (Unsupported Extension: '.values')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 20.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 34.4 | 50.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.6 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 23.1 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 78.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 20.1 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 57072 | 10184 | 0 | `compiler/testData/codegen/box/primitiveTypes/crossTypeEquals.kt` |
| cleanup | 1444 | 613 | 0 | `compiler/testData/diagnostics/tests/Serializable.fir.kt` |
| guards | 199879 | 22220 | 4 | `kotlin-native/performance/startup/src/commonMain/kotlin/org/jetbrains/startup/SingletonInitBenchmark.kt` |
| danger | 182398 | 33083 | 4 | `native/swift/swift-export-standalone-integration-tests/external/testData/generation/kotlinx-serialization-core/golden_result/KotlinStdlib/KotlinStdlib.h` |
| concurrency | 16952 | 2911 | 0 | `plugins/atomicfu/atomicfu-compiler/src/org/jetbrains/kotlinx/atomicfu/compiler/backend/common/AbstractAtomicfuTransformer.kt` |
| connectivity | 90809 | 18087 | 1 | `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` |
| io | 9794 | 1983 | 0 | `settings.gradle` |
| crypto | 1 | 1 | 0 | `kotlin-native/tools/llvm_builder/package.py` |
| ipc | 109 | 58 | 0 | `libraries/tools/kotlin-maven-plugin-test/src/test/resources/maven-wrapper/mvnw` |
| time | 188 | 76 | 0 | `kotlin-native/runtime/src/main/cpp/Clock.hpp` |
| serialization | 191 | 63 | 0 | `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/Kotlin2JsGradlePluginIT.kt` |
| regex | 1153 | 431 | 0 | `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/MppIdeDependencyResolutionIT.kt` |
| events | 1453 | 426 | 0 | `compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/KotlinCallDiagnostics.kt` |
| tests | 55933 | 12098 | 1 | `compiler/testData/codegen/box/primitiveTypes/crossTypeEquals.kt` |
| docs | 26359 | 5512 | 0 | `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParserBaseListener.java` |
| debt | 30646 | 7695 | 0 | `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` |
| mutation | 431805 | 41420 | 8 | `compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiRawFirBuilder.kt` |
| dead_code | 103970 | 47370 | 2 | `kotlin-native/performance/ring/src/commonMain/kotlin/org/jetbrains/ring/InheritanceBenchmark.kt` |
| credential | 278 | 93 | 0 | `js/js.translator/testData/package-lock.json` |
| threat | 67699 | 16347 | 1 | `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/commonizeSQLiteAndCurlInterop/libs/sqlite3.h` |
| ml_ai | 4938 | 776 | 0 | `kotlin-native/performance/startup/src/commonMain/kotlin/org/jetbrains/startup/SingletonInitBenchmark.kt` |
| ui | 8263 | 933 | 0 | `plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ControlFlowTransformTests.kt` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `settings.gradle` (Hits: 237)
- `libraries/tools/kotlin-maven-plugin-test/src/test/resources/maven-wrapper/mvnw` (Hits: 89)
- `libraries/stdlib/jvm/src/kotlin/io/files/Utils.kt` (Hits: 72)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **File.kt** (`compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt`) — 1310 inbound connections
2. **Name.java** (`core/compiler.common/src/org/jetbrains/kotlin/name/Name.java`) — 1275 inbound connections
3. **NotNull.java** (`analysis/symbol-light-classes/testData/additionalFiles/NotNull.java`) — 876 inbound connections
4. **FqName.kt** (`core/compiler.common/src/org/jetbrains/kotlin/name/FqName.kt`) — 852 inbound connections
5. **Project.kt** (`compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/Project.kt`) — 820 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **FirErrorsDefaultMessages.kt** (`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrorsDefaultMessages.kt`) — 934 outbound dependencies
2. **loadInterpreter.kt** (`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/loadInterpreter.kt`) — 328 outbound dependencies
3. **FirJvmErrorsDefaultMessages.kt** (`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/diagnostics/jvm/FirJvmErrorsDefaultMessages.kt`) — 124 outbound dependencies
4. **KaFirCompilerFacility.kt** (`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompilerFacility.kt`) — 110 outbound dependencies
5. **IrFileSerializer.kt** (`compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/IrFileSerializer.kt`) — 107 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `elf_add` **(Many-Argument Workhorses)** (@ `kotlin-native/runtime/src/libbacktrace/c/elf.c`) -> Impact: **724.7** | LOC: 806
  * *Intent:* base_address is determined. */
- `PrintStack` **(Many-Argument Workhorses)** (@ `kotlin-native/tools/minidump-analyzer/src/main/cpp/main.cc`) -> Impact: **543.8** | LOC: 638
  * *Intent:* // PrintStack prints the call stack in |stack| to stdout, in a reasonably // useful form. Module, function, and source file names are displayed if // ...
- `createModuleArtifact` **(Many-Argument Workhorses)** (@ `compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/ic/CacheUpdater.kt`) -> Impact: **321.6** | LOC: 750
- `irSetSlotUncertain` **(Stateful Encapsulated Methods)** (@ `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt`) -> Impact: **320.9** | LOC: 1610
- `lower` **(Many-Argument Workhorses)** (@ `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/CastsOptimization.kt`) -> Impact: **311.0** | LOC: 885
- `elf_uncompress_lzma_block` **(Many-Argument Workhorses)** (@ `kotlin-native/runtime/src/libbacktrace/c/elf.c`) -> Impact: **308.6** | LOC: 685
  * *Intent:* decompression. */
- `elf_zlib_inflate` **(Many-Argument Workhorses)** (@ `kotlin-native/runtime/src/libbacktrace/c/elf.c`) -> Impact: **296.7** | LOC: 693
  * *Intent:* /* Inflate a zlib stream from PIN/SIN to POUT/SOUT. Return 1 on success, 0 on some error parsing the stream. */
- `translateExtensions` **(Stateful Encapsulated Methods)** (@ `native/objcexport-header-generator/impl/k1/src/org/jetbrains/kotlin/backend/konan/objcexport/ObjCExportTranslator.kt`) -> Impact: **276.8** | LOC: 1067
- `singleExpressionImpl` **(Many-Argument Workhorses)** (@ `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java`) -> Impact: **259.6** | LOC: 724
- `importFromBlock` **(Compute Cores)** (@ `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java`) -> Impact: **244.8** | LOC: 176

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/proto` | 171 | 28702.9 | 17.28% | 95.69% |
| `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated` | 6 | 11224.84 | 8.49% | 85.73% |
| `kotlin-native/runtime/src/libbacktrace/c` | 13 | 10412.78 | 65.31% | 30.04% |
| `kotlin-native/runtime/src/main/cpp` | 131 | 9226.2 | 21.51% | 35.56% |
| `compiler/frontend/src/org/jetbrains/kotlin/resolve` | 89 | 8702.32 | 15.35% | 32.73% |
| `compiler/ir/backend.jvm/lower/src/org/jetbrains/kotlin/backend/jvm/lower` | 90 | 7777.7 | 48.33% | 51.71% |
| `compiler/psi/psi-api/src/org/jetbrains/kotlin/psi` | 195 | 7208.2 | 7.07% | 65.92% |
| `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower` | 29 | 6854.54 | 30.55% | 46.85% |
| `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration` | 132 | 5743.28 | 45.46% | 39.09% |
| `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations` | 14 | 5431.98 | 53.12% | 42.58% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/projectStructure/KaFirLibraryTargetPlatformContentScopeRefiner.kt` -> **100.0%** Exposure
- `analysis/analysis-api/testData/components/compilerFacility/compilation/codeFragments/capturing/localFunctionWithMultiFileClass.kt` -> **100.0%** Exposure
- `analysis/analysis-api/testData/components/compilerFacility/compilation/codeFragments/capturing/localFunctionsInNestedClass.kt` -> **100.0%** Exposure
- `analysis/analysis-api/testData/components/compilerFacility/compilation/defaultImpls.kt` -> **100.0%** Exposure
- `analysis/analysis-api/testData/components/compilerFacility/compilation/defaultImplsCLIOnly.kt` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/KaFe10Session.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/InlineDelegatedPropertyAccessorsAnalyzer.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fe10/src/org/jetbrains/kotlin/analysis/api/descriptors/utils/InlineFunctionAnalyzer.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/compilation/CodeFragmentContextDeclarationCache.kt` -> **100.0%** Exposure
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/inlineStackDataUtils.kt` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` -> **7** Orphaned Functions | **483** Duplicates
- `kotlin-native/performance/ring/src/commonMain/kotlin/org/jetbrains/ring/InheritanceBenchmark.kt` -> **435** Orphaned Functions | **0** Duplicates
- `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParserBaseListener.java` -> **324** Orphaned Functions | **0** Duplicates
- `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParserListener.java` -> **320** Orphaned Functions | **0** Duplicates
- `analysis/stubs/testData/builtins/stubs/kotlin.kotlin_builtins.decompiled.text.kt` -> **15** Orphaned Functions | **247** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportPopularSwiftPMDependenciesTests.kt` -> **20.0708%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `32` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `148612` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 8941.72 | **LOC:** 11868 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **10**; blast radius 0.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.6%), Mutation Surface (formerly State Flux) (59.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `singleExpressionImpl` **(Many-Argument Workhorses)** (Impact: 259.6)
  * `importFromBlock` **(Compute Cores)** (Impact: 244.8)
  * `arrayElement` **(Compute Cores)** (Impact: 167.1)
  * `classElementName` **(Compute Cores)** (Impact: 132.8)
  * `propertyName` **(Compute Cores)** (Impact: 131.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 264 instances
* *State Mutation (weighted view):* 863
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3285`, `structural_boundaries: 3152`, `args: 1506`, `func_start: 1506`, `class_start: 167`
* *Risk/State:* `safety_bypasses: 537`, `state_mutation: 335`, `duplicate_logic: 483`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1678`, `import: 6`
* *Defense:* `safety: 781`, `doc: 1`, `sync_locks: 2`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 9.2e-05
  * `Imports (Out-Degree: 2):` java.util.ArrayList, java.util.Iterator, java.util.List, org.antlr.v4.runtime.*, org.antlr.v4.runtime.atn.*, org.antlr.v4.runtime.dfa.DFA, org.antlr.v4.runtime.misc.*, org.antlr.v4.runtime.tree.*...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `kotlin-native/runtime/src/libbacktrace/c/elf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4633.82 | **LOC:** 4920 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elf_add` **(Many-Argument Workhorses)** (Impact: 724.7)
    * *Intent:* base_address is determined. */
  * `elf_uncompress_lzma_block` **(Many-Argument Workhorses)** (Impact: 308.6)
    * *Intent:* decompression. */
  * `elf_zlib_inflate` **(Many-Argument Workhorses)** (Impact: 296.7)
    * *Intent:* /* Inflate a zlib stream from PIN/SIN to POUT/SOUT. Return 1 on success, 0 on some error parsing the...
  * `elf_zlib_inflate_table` **(Many-Argument Workhorses)** (Impact: 100.4)
    * *Intent:* Returns 1 on success, 0 on error. */
  * `elf_uncompress_lzma` **(Many-Argument Workhorses)** (Impact: 76.4)
    * *Intent:* will carry on in that case. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 791 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2500
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 603`, `structural_boundaries: 363`, `args: 57`, `func_start: 42`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 918`
* *Architecture:* `api: 26`, `import: 11`
* *Defense:* `safety: 113`, `immutability_locks: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` backtrace.h, config.h, errno.h, internal.h, link.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/libbacktrace/c/dwarf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3845.7 | **LOC:** 4416 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_attribute` **(Many-Argument Workhorses)** (Impact: 244.7)
    * *Intent:* *IS_VALID to 1. We don't try to store the value of other attribute forms, because we don't care abou...
  * `read_function_entry` **(Many-Argument Workhorses)** (Impact: 211.9)
    * *Intent:* /* Read one entry plus all its children. Add function addresses to VEC. Returns 1 on success, 0 on e...
  * `find_address_ranges` **(Many-Argument Workhorses)** (Impact: 152.6)
    * *Intent:* read, 0 if there is some error. */
  * `dwarf_lookup_pc` **(Many-Argument Workhorses)** (Impact: 123.3)
    * *Intent:* 0 if not. */
  * `add_ranges_from_rnglists` **(Many-Argument Workhorses)** (Impact: 109.5)
    * *Intent:* /* Call ADD_RANGE for each range read from .debug_rnglists, as used in DWARF version 5. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 551 instances
* *State Mutation (weighted view):* 1742
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 618`, `structural_boundaries: 812`, `args: 62`, `func_start: 59`, `class_start: 159`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 640`, `fragile_debt: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 67`, `immutability_locks: 150`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` backtrace.h, config.h, errno.h, filenames.h, internal.h, stdlib.h, string.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiRawFirBuilder.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2787.2 | **LOC:** 3963 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **54**; blast radius 0.021; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.0%), Complexity Load (formerly Cognitive Load) (82.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.8339% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitNamedFunction` **(Many-Argument Workhorses)** (Impact: 67.6)
  * `extractSuperTypeListEntriesTo` **(Many-Argument Workhorses)** (Impact: 66.3)
  * `toFirProperty` **(Many-Argument Workhorses)** (Impact: 49.1)
  * `visitWhenExpression` **(Many-Argument Workhorses)** (Impact: 48.1)
  * `visitClassOrObject` **(Many-Argument Workhorses)** (Impact: 46.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 340 instances
* *State Mutation (weighted view):* 1527
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 491`, `structural_boundaries: 327`, `args: 179`, `func_start: 123`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 847`, `dead_code: 1`, `planned_debt: 9`
* *Architecture:* `api: 51`, `concurrency: 1`, `import: 54`
* *Defense:* `safety: 206`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000592
  * `Imports (Out-Degree: 11):` com.intellij.extapi.psi.StubBasedPsiElementBase, com.intellij.psi.PsiElement, com.intellij.psi.PsiErrorElement, com.intellij.psi.tree.IElementType, com.intellij.psi.util.childrenOfType, com.intellij.util.AstLoadingFilter, org.jetbrains.kotlin.*, org.jetbrains.kotlin.builtins.StandardNames...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2621.8 | **LOC:** 5145 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **45**; blast radius 0.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (60.0%)
- **Documentation Coverage:** 98.6301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `irSetSlotUncertain` **(Stateful Encapsulated Methods)** (Impact: 320.9)
  * `buildPreambleStatementsAndReturnIfSkippingPossible` **(Many-Argument Workhorses)** (Impact: 137.5)
  * `visitNonRestartableComposableFunction` **(Many-Argument Workhorses)** (Impact: 67.7)
    * *Intent:* // At a high level, without useNonSkippingGroupOptimization, a non-restartable composable // functio...
  * `visitWhen` **(Compute Cores)** (Impact: 54.7)
  * `visitComposableLambda` **(Many-Argument Workhorses)** (Impact: 54.6)
    * *Intent:* // Composable lambdas are always wrapped with a ComposableLambda class, which has its own // group i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 698
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 627`, `structural_boundaries: 466`, `args: 266`, `func_start: 204`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 342`, `dead_code: 43`, `planned_debt: 10`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `import: 45`
* *Defense:* `safety: 155`, `doc: 20`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000543
  * `Imports (Out-Degree: 10):` androidx.compose.compiler.plugins.kotlin.*, androidx.compose.compiler.plugins.kotlin.analysis.*, kotlin.math.abs, kotlin.math.absoluteValue, kotlin.math.ceil, kotlin.math.min, org.jetbrains.kotlin.backend.common.FileLoweringPass, org.jetbrains.kotlin.backend.common.extensions.IrPluginContext...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirDeclarationBuilder.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1954.7 | **LOC:** 2974 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **51**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.7%)
- **Documentation Coverage:** 24.3056% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertPrimaryConstructor` **(Many-Argument Workhorses)** (Impact: 90.6)
    * *Intent:* /** * primaryConstructor branch */
  * `convertPropertyDeclaration` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* /** */
  * `convertFunctionDeclaration` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* /** */
  * `convertGetterOrSetter` **(Many-Argument Workhorses)** (Impact: 68.2)
    * *Intent:* /** */
  * `convertClass` **(Many-Argument Workhorses)** (Impact: 63.0)
    * *Intent:* /***** DECLARATIONS *****/ /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 228 instances
* *State Mutation (weighted view):* 966
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 209`, `args: 156`, `func_start: 75`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 510`, `planned_debt: 5`
* *Architecture:* `api: 7`, `import: 51`
* *Defense:* `safety: 72`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 4.9e-05
  * `Imports (Out-Degree: 17):` com.intellij.lang.LighterASTNode, com.intellij.psi.TokenType, com.intellij.util.diff.FlyweightCapableTreeStructure, org.jetbrains.kotlin.*, org.jetbrains.kotlin.ElementTypeUtils.isExpression, org.jetbrains.kotlin.KtNodeTypes.*, org.jetbrains.kotlin.builtins.StandardNames, org.jetbrains.kotlin.config.AnalysisFlags...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/frontend/src/org/jetbrains/kotlin/diagnostics/rendering/DefaultErrorMessages.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1645.24 | **LOC:** 1343 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **23**; blast radius 0.06; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Complexity Load (formerly Cognitive Load) (87.9%), Debt Markers (formerly Tech Debt) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `adaptGenerics2` **(Generic / Templated Code)** (Impact: 12.3)
  * `adaptGenerics1` **(Generic / Templated Code)** (Impact: 7.1)
    * *Intent:* // Those methods are needed to fix problems with java type system and kotlin variance
  * `getRendererForDiagnostic` **(Defensive Guards)** (Impact: 6.2)
  * `render` **(Defensive Guards)** (Impact: 4.7)
  * `getMap` **(Annotated & Test Methods)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 391 instances
* *State Mutation (weighted view):* 1586
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 281`, `args: 28`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 804`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 19`
* *Defense:* `safety: 16`, `doc: 1`, `test: 4`, `sync_locks: 3`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.06
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002605
  * `Imports (Out-Degree: 8):` com.intellij.openapi.util.io.FileUtil, java.lang.reflect.Field, java.lang.reflect.Modifier, java.util.*, kotlin.Pair, kotlin.collections.CollectionsKt, org.jetbrains.annotations.NotNull, org.jetbrains.annotations.Nullable...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrorsDefaultMessages.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1505.38 | **LOC:** 3934 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **934**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.8%), Complexity Load (formerly Cognitive Load) (72.6%), Concurrency Surface (formerly Concurrency) (63.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compute` **(Defensive Guards)** (Impact: 7.3)
  * `render` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 209 instances
* *Concurrency (weighted view):* 120
* *State Mutation (weighted view):* 1297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 1135`, `args: 5`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 126`, `state_mutation: 879`, `planned_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 20`, `import: 934`
* *Defense:* `safety: 268`, `doc: 3`, `test: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.intellij.openapi.util.io.FileUtil, org.jetbrains.kotlin.config.LanguageFeature, org.jetbrains.kotlin.diagnostics.DiagnosticBaseContext, org.jetbrains.kotlin.diagnostics.KtDiagnosticFactoryToRendererMap, org.jetbrains.kotlin.diagnostics.KtDiagnosticRenderers.CLASS_ID, org.jetbrains.kotlin.diagnostics.KtDiagnosticRenderers.CLASS_ID_RELATIVE_NAME_ONLY, org.jetbrains.kotlin.diagnostics.KtDiagnosticRenderers.COLLECTION, org.jetbrains.kotlin.diagnostics.KtDiagnosticRenderers.EMPTY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/llvm/IrToBitcode.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1323.92 | **LOC:** 2960 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (60.0%), Guard Balance (formerly Safety Score) (55.8%), Mutation Surface (formerly State Flux) (43.8%)
- **Documentation Coverage:** 79.2899% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrapException` **(Stateful Encapsulated Methods)** (Impact: 237.1)
    * *Intent:* /** * Called, when exception is caught in this block. Result expception would be rethrown instead. *...
  * `overrideRuntimeGlobals` **(Defensive Guards)** (Impact: 33.0)
  * `evaluateConstantValueImpl` **(Defensive Guards)** (Impact: 31.6)
  * `evaluateOperatorCall` **(Many-Argument Workhorses)** (Impact: 25.4)
    * *Intent:* // TODO: Intrinsify?
  * `call` **(Many-Argument Workhorses)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `structural_boundaries: 416`, `args: 238`, `func_start: 205`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 60`, `dead_code: 1`, `planned_debt: 20`, `fragile_debt: 5`, `duplicate_logic: 4`, `unreferenced_by_name: 14`
* *Architecture:* `io: 4`, `api: 9`, `import: 35`
* *Defense:* `safety: 126`, `doc: 35`, `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` kotlinx.cinterop.*, llvm.*, org.jetbrains.kotlin.backend.common.compilationException, org.jetbrains.kotlin.backend.common.ir.isUnconditional, org.jetbrains.kotlin.backend.common.lower.coroutines.getOrCreateFunctionWithContinuationStub, org.jetbrains.kotlin.backend.konan.*, org.jetbrains.kotlin.backend.konan.cexport.CAdapterCodegen, org.jetbrains.kotlin.backend.konan.cexport.CAdapterExportedElements...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/DevirtualizationAnalysis.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1173.92 | **LOC:** 1896 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%)
- **Documentation Coverage:** 96.875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `devirtualize` **(Many-Argument Workhorses)** (Impact: 113.0)
  * `analyze` **(I/O & Config Routines)** (Impact: 55.6)
  * `visitCall` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `dfgNodeToConstraintNode` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* /** * Takes a function DFG's node and creates a constraint graph node corresponding to it. * Also cr...
  * `writeField` **(Many-Argument Workhorses)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 204`, `args: 110`, `func_start: 78`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 166`, `dead_code: 1`, `planned_debt: 8`
* *Architecture:* `api: 10`, `import: 31`
* *Defense:* `safety: 62`, `doc: 6`, `test: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 1e-05
  * `Imports (Out-Degree: 6):` java.util.*, org.jetbrains.kotlin.backend.common.lower.createIrBuilder, org.jetbrains.kotlin.backend.common.lower.irBlock, org.jetbrains.kotlin.backend.common.pop, org.jetbrains.kotlin.backend.common.push, org.jetbrains.kotlin.backend.konan.*, org.jetbrains.kotlin.backend.konan.ir.isBoxOrUnboxCall, org.jetbrains.kotlin.backend.konan.lower.getObjectClassInstanceFunction...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/CastsOptimization.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1161.82 | **LOC:** 1351 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **30**; blast radius 0.009; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (86.8%), Complexity Load (formerly Cognitive Load) (85.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lower` **(Many-Argument Workhorses)** (Impact: 311.0)
  * `and` **(Compute Cores)** (Impact: 44.7)
    * *Intent:* // TODO: Support type hierarchy here (KT-77671).
  * `buildEqEq` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `setVariable` **(Defensive Guards)** (Impact: 36.2)
  * `or` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* // TODO: Support type hierarchy here (KT-77671).
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 205`, `args: 91`, `func_start: 75`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 105`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 15`, `import: 30`
* *Defense:* `safety: 52`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 1e-05
  * `Imports (Out-Degree: 4):` java.util.*, org.jetbrains.kotlin.backend.common.BodyLoweringPass, org.jetbrains.kotlin.backend.common.ir.isUnconditional, org.jetbrains.kotlin.backend.common.lower.at, org.jetbrains.kotlin.backend.common.lower.createIrBuilder, org.jetbrains.kotlin.backend.common.pop, org.jetbrains.kotlin.backend.common.push, org.jetbrains.kotlin.backend.konan.Context...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1142.46 | **LOC:** 2368 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **60**; blast radius 0.012; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.5%), Complexity Load (formerly Cognitive Load) (54.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Guard Balance (formerly Safety Score) (46.4%)
- **Documentation Coverage:** 90.9605% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformQualifiedAccessExpression` **(Many-Argument Workhorses)** (Impact: 55.3)
  * `transformFunctionCallInternal` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `transformSuperReceiver` **(Many-Argument Workhorses)** (Impact: 41.4)
  * `transformDelegatedConstructorCall` **(Defensive Guards)** (Impact: 35.0)
  * `prepareContextSensitiveAlternativeIfNeeded` **(Defensive Guards)** (Impact: 29.0)
    * *Intent:* /** * For expression in a form like `MyEnum.X` and mode=[ResolutionMode.ContextDependent], it sets `...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 325`, `args: 126`, `func_start: 98`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 154`, `dead_code: 7`, `planned_debt: 5`
* *Architecture:* `api: 41`, `import: 60`
* *Defense:* `safety: 194`, `doc: 8`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000179
  * `Imports (Out-Degree: 17):` kotlin.contracts.ExperimentalContracts, kotlin.contracts.contract, org.jetbrains.kotlin.*, org.jetbrains.kotlin.config.AnalysisFlags, org.jetbrains.kotlin.config.LanguageFeature, org.jetbrains.kotlin.descriptors.ClassKind, org.jetbrains.kotlin.fir.*, org.jetbrains.kotlin.fir.declarations.*...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `compiler/psi/parser/src/org/jetbrains/kotlin/parsing/KotlinParsing.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1134.24 | **LOC:** 2820 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.6%), Mutation Surface (formerly State Flux) (52.5%), Complexity Load (formerly Cognitive Load) (29.0%)
- **Documentation Coverage:** 94.2029% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseClassOrObject` **(Many-Argument Workhorses)** (Impact: 83.5)
    * *Intent:* * primaryConstructor? * (":" annotations delegationSpecifier{","})? * typeConstraints * (classBody? ...
  * `parseCommonDeclaration` **(Defensive Guards)** (Impact: 51.5)
  * `parseMultiDeclarationEntry` **(Many-Argument Workhorses)** (Impact: 47.2)
    * *Intent:* /* * (SimpleName (":" type){","}) */
  * `parseProperty` **(Compute Cores)** (Impact: 37.1)
    * *Intent:* * variableDeclarationEntry * : SimpleName (":" type)? * ; * * property * : modifiers ("val" | "var")...
  * `parsePropertyComponent` **(Compute Cores)** (Impact: 37.1)
    * *Intent:* /* * propertyComponent * : modifiers ("get" | "set") * : * ( "get" "(" ")" * | * "set" "(" modifiers...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 251`, `args: 128`, `func_start: 123`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 65`, `dead_code: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 11`
* *Architecture:* `api: 22`, `import: 14`
* *Defense:* `safety: 38`, `doc: 6`, `test: 28`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.intellij.lang.PsiBuilder, com.intellij.lang.WhitespacesBinders, com.intellij.openapi.diagnostic.Logger, com.intellij.psi.tree.IElementType, com.intellij.psi.tree.TokenSet, java.util.function.Supplier, org.jetbrains.annotations.Contract, org.jetbrains.annotations.NotNull...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/multiplatform-parsing/common/src/org/jetbrains/kotlin/kmp/parser/utils/KotlinParsing.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1130.62 | **LOC:** 2922 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **27**; blast radius 0.012; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (68.9%), Guard Balance (formerly Safety Score) (59.1%), Complexity Load (formerly Cognitive Load) (18.1%)
- **Documentation Coverage:** 92.0354% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseClassOrObject` **(Many-Argument Workhorses)** (Impact: 83.1)
    * *Intent:* * primaryConstructor? * (":" annotations delegationSpecifier{","})? * typeConstraints * (classBody? ...
  * `parseProperty` **(Compute Cores)** (Impact: 50.0)
    * *Intent:* * variableDeclarationEntry * : SimpleName (":" type)? * ; * * property * : modifiers ("val" | "var")...
  * `doParseModifierListBody` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `parseTypeRefContents` **(Many-Argument Workhorses)** (Impact: 47.5)
    * *Intent:* // The extraRecoverySet is needed for the foo(bar<x, 1, y>(z)) case, to tell whether we should stop ...
  * `parseMultiDeclarationEntry` **(Many-Argument Workhorses)** (Impact: 45.3)
    * *Intent:* /* * (SimpleName (":" type){","}) */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 457`, `structural_boundaries: 285`, `args: 107`, `func_start: 101`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 60`, `dead_code: 7`, `planned_debt: 1`
* *Architecture:* `api: 11`, `import: 27`
* *Defense:* `safety: 25`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 1e-05
  * `Imports (Out-Degree: 2):` com.intellij.platform.syntax.SyntaxElementType, com.intellij.platform.syntax.SyntaxElementTypeSet, com.intellij.platform.syntax.emptySyntaxElementTypeSet, com.intellij.platform.syntax.parser.SyntaxTreeBuilder, com.intellij.platform.syntax.parser.WhitespacesBinders, com.intellij.platform.syntax.syntaxElementTypeSetOf, org.jetbrains.annotations.Contract, org.jetbrains.kotlin.kmp.lexer.KtTokens...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kotlin-native/runtime/src/libbacktrace/c/macho.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1118.42 | **LOC:** 1379 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.4%), Complexity Load (formerly Cognitive Load) (81.4%), Debt Markers (formerly Tech Debt) (10.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `macho_add` **(Many-Argument Workhorses)** (Impact: 175.3)
    * *Intent:* */
  * `macho_add_symtab` **(Many-Argument Workhorses)** (Impact: 105.7)
    * *Intent:* /* Add symbol table information for a Mach-O file. */
  * `backtrace_initialize` **(Many-Argument Workhorses)** (Impact: 62.4)
    * *Intent:* #ifdef HAVE_MACH_O_DYLD_H /* Initialize the backtrace data we need from a Mach-O executable using th...
  * `macho_add_fat` **(Many-Argument Workhorses)** (Impact: 59.1)
    * *Intent:* /* Look through a fat file to find the relevant executable. Returns 1 on success, 0 on failure (in b...
  * `macho_add_dsym` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* 0 on failure. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 159 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 174`, `args: 22`, `func_start: 14`, `class_start: 51`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 170`, `fragile_debt: 2`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 14`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` backtrace.h, config.h, dirent.h, internal.h, dyld.h, stdlib.h, string.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/fir/raw-fir/light-tree2fir/src/org/jetbrains/kotlin/fir/lightTree/converter/LightTreeRawFirExpressionBuilder.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1111.34 | **LOC:** 1743 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **50**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.8%)
- **Documentation Coverage:** 29.8701% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertCallExpression` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* /** */
  * `convertQualifiedExpression` **(Defensive Guards)** (Impact: 33.2)
    * *Intent:* /** */
  * `convertWhenExpression` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /** */
  * `wrapExpressionIfNeeded` **(Stateful Encapsulated Methods)** (Impact: 28.5)
  * `convertBinaryExpressionFallback` **(Compute Cores)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 147 instances
* *State Mutation (weighted view):* 598
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 178`, `args: 90`, `func_start: 50`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 304`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 50`
* *Defense:* `safety: 45`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` com.intellij.lang.LighterASTNode, com.intellij.psi.TokenType, com.intellij.util.diff.FlyweightCapableTreeStructure, org.jetbrains.kotlin.*, org.jetbrains.kotlin.ElementTypeUtils.getOperationSymbol, org.jetbrains.kotlin.ElementTypeUtils.isExpression, org.jetbrains.kotlin.KtNodeTypes.*, org.jetbrains.kotlin.descriptors.EffectiveVisibility...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/kapt/kapt-compiler/src/org/jetbrains/kotlin/kapt/stubs/KaptStubConverter.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1109.8 | **LOC:** 1612 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **86**; blast radius 0.009; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (55.9%), Complexity Load (formerly Cognitive Load) (28.7%), Guard Balance (formerly Safety Score) (26.1%), Debt Markers (formerly Tech Debt) (8.9%)
- **Documentation Coverage:** 98.9011% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertMethod` **(Many-Argument Workhorses)** (Impact: 106.6)
  * `extractMethodSignatureTypes` **(Many-Argument Workhorses)** (Impact: 105.5)
  * `convertClass` **(Many-Argument Workhorses)** (Impact: 87.7)
    * *Intent:* /** * Returns false for the inner classes or if the origin for the class was not found. */
  * `checkIfAnnotationValueMatches` **(Defensive Guards)** (Impact: 56.3)
  * `getCallableDeclaration` **(Defensive Guards)** (Impact: 42.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 335`, `args: 100`, `func_start: 66`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 35`, `planned_debt: 4`
* *Architecture:* `io: 5`, `api: 8`, `import: 86`
* *Defense:* `safety: 201`, `doc: 1`, `test: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 1e-05
  * `Imports (Out-Degree: 30):` com.intellij.psi.PsiElement, com.sun.tools.javac.code.Flags, com.sun.tools.javac.code.TypeTag, com.sun.tools.javac.parser.Tokens, com.sun.tools.javac.tree.JCTree, com.sun.tools.javac.tree.JCTree.*, com.sun.tools.javac.tree.TreeMaker, com.sun.tools.javac.tree.TreeScanner...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/dfa/FirDataFlowAnalyzer.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1097.7 | **LOC:** 1931 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **33**; blast radius 0.012; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (49.2%), Complexity Load (formerly Cognitive Load) (48.3%), Connectivity (formerly Api Exposure) (47.3%)
- **Documentation Coverage:** 91.8819% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processConditionalContract` **(Many-Argument Workhorses)** (Impact: 84.6)
  * `processEq` **(Many-Argument Workhorses)** (Impact: 75.2)
  * `exitVariableInitialization` **(Many-Argument Workhorses)** (Impact: 61.9)
  * `mapElement` **(Stateful Encapsulated Methods)** (Impact: 40.7)
  * `addTypeOperatorStatements` **(Many-Argument Workhorses)** (Impact: 32.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 308`, `args: 187`, `func_start: 142`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 39`, `dead_code: 11`, `planned_debt: 3`
* *Architecture:* `api: 93`, `concurrency: 14`, `import: 33`
* *Defense:* `safety: 130`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000207
  * `Imports (Out-Degree: 11):` kotlinx.collections.immutable.persistentSetOf, kotlinx.collections.immutable.toPersistentSet, org.jetbrains.kotlin.config.LanguageFeature, org.jetbrains.kotlin.contracts.description.LogicOperationKind, org.jetbrains.kotlin.contracts.description.canBeRevisited, org.jetbrains.kotlin.descriptors.isObject, org.jetbrains.kotlin.fir.*, org.jetbrains.kotlin.fir.contracts.description.*...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `compiler/frontend/src/org/jetbrains/kotlin/types/expressions/BasicExpressionTypingVisitor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1081.6 | **LOC:** 1814 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **78**; blast radius 0.009; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.8%), Debt Markers (formerly Tech Debt) (51.6%)
- **Documentation Coverage:** 98.1481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkLValue` **(Many-Argument Workhorses)** (Impact: 73.4)
    * *Intent:* /** * @return {@code true} iff expression can be assigned to */
  * `checkPossiblyQualifiedSuper` **(Many-Argument Workhorses)** (Impact: 67.7)
  * `visitBinaryExpression` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `visitUnaryExpression` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `resolveArrayAccessSpecialMethod` **(Many-Argument Workhorses)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 266`, `args: 79`, `func_start: 75`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 130`, `state_mutation: 60`, `dead_code: 1`, `planned_debt: 6`, `unreferenced_by_name: 23`
* *Architecture:* `api: 34`, `import: 68`
* *Defense:* `safety: 154`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 1e-05
  * `Imports (Out-Degree: 38):` com.google.common.collect.Lists, com.intellij.psi.PsiElement, com.intellij.psi.StubBasedPsiElement, com.intellij.psi.tree.IElementType, com.intellij.psi.tree.TokenSet, com.intellij.psi.util.PsiTreeUtil, java.util.Collection, java.util.Collections...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/optimizations/EscapeAnalysis.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1032.8 | **LOC:** 1827 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%), Complexity Load (formerly Cognitive Load) (59.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Defensive Guards)** (Impact: 54.9)
  * `analyze` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `paintNodes` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `buildDrains` **(I/O & Config Routines)** (Impact: 41.4)
  * `computeLifetimes` **(I/O & Config Routines)** (Impact: 28.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 96 instances
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 195`, `args: 104`, `func_start: 74`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 123`, `planned_debt: 10`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 77`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.jetbrains.kotlin.backend.common.peek, org.jetbrains.kotlin.backend.common.pop, org.jetbrains.kotlin.backend.common.push, org.jetbrains.kotlin.backend.konan.*, org.jetbrains.kotlin.backend.konan.Context, org.jetbrains.kotlin.backend.konan.DirectedGraphCondensationBuilder, org.jetbrains.kotlin.backend.konan.DirectedGraphMultiNode, org.jetbrains.kotlin.backend.konan.ir.annotations.Escapes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/main/cpp/dtoa/cbigint.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1019.56 | **LOC:** 905 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 89.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `timesTenToTheEHighPrecision` **(Many-Argument Workhorses)** (Impact: 68.8)
  * `toDoubleHighPrecision` **(Many-Argument Workhorses)** (Impact: 65.9)
  * `addHighPrecision` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `compareHighPrecision` **(Compute Cores)** (Impact: 34.7)
  * `highestSetBit` **(Compute Cores)** (Impact: 33.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 190 instances
* *State Mutation (weighted view):* 578
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 46`, `args: 41`, `func_start: 22`
* *Risk/State:* `state_mutation: 198`, `unreferenced_by_name: 12`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cbigint.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 985.26 | **LOC:** 2154 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **83**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.3%), Complexity Load (formerly Cognitive Load) (20.9%), Guard Balance (formerly Safety Score) (20.7%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildKaCall` **(Many-Argument Workhorses)** (Impact: 118.3)
    * *Intent:* /** * Core call construction logic. Assumes the caller has already handled compound access. */
  * `toKaResolutionAttempt` **(Defensive Guards)** (Impact: 57.2)
  * `createKtPartiallyAppliedSymbolForImplicitInvoke` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `createCompoundArrayAccessCall` **(Many-Argument Workhorses)** (Impact: 27.8)
  * `createKaCallForVariableAccessConvention` **(Many-Argument Workhorses)** (Impact: 27.5)
    * *Intent:* /** * Handle compound assignment with variable */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 377`, `args: 118`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 103`, `dead_code: 4`, `planned_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`, `import: 83`
* *Defense:* `safety: 310`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` com.intellij.openapi.diagnostic.logger, org.jetbrains.kotlin.KtFakeSourceElementKind, org.jetbrains.kotlin.KtSourceElement, org.jetbrains.kotlin.analysis.api.KaNonPublicApi, org.jetbrains.kotlin.analysis.api.diagnostics.KaDiagnostic, org.jetbrains.kotlin.analysis.api.fir.*, org.jetbrains.kotlin.analysis.api.fir.references.*, org.jetbrains.kotlin.analysis.api.fir.symbols.KaFirArrayOfSymbolProvider.arrayOfSymbol...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/fir/raw-fir/raw-fir.common/src/org/jetbrains/kotlin/fir/builder/AbstractRawFirBuilder.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 959.08 | **LOC:** 1526 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **48**; blast radius 0.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.7%), Connectivity (formerly Api Exposure) (28.6%)
- **Documentation Coverage:** 93.3673% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateComponentAccess` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `generateIncrementOrDecrementBlockForArrayAccess` **(Many-Argument Workhorses)** (Impact: 32.7)
    * *Intent:* * * given: * ++a[b, c] * * result: * { * val <array> = a * val <index0> = b * val <index1> = c * <ar...
  * `generateConstantExpressionByLiteral` **(Compute Cores)** (Impact: 30.4)
  * `createDataClassCopyFunction` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `generateIndexedAccessAugmentedAssignment` **(Many-Argument Workhorses)** (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 212`, `args: 89`, `func_start: 70`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 240`, `dead_code: 1`
* *Architecture:* `api: 37`, `import: 48`
* *Defense:* `safety: 44`, `doc: 7`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 4e-05
  * `Imports (Out-Degree: 15):` com.intellij.psi.PsiElement, com.intellij.psi.tree.IElementType, kotlin.contracts.ExperimentalContracts, kotlin.contracts.InvocationKind, kotlin.contracts.contract, org.jetbrains.kotlin.*, org.jetbrains.kotlin.KtNodeTypes.*, org.jetbrains.kotlin.builtins.StandardNames...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `compiler/backend/src/org/jetbrains/kotlin/codegen/coroutines/CoroutineTransformerMethodVisitor.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 946.94 | **LOC:** 1933 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.009; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (23.4%)
- **Documentation Coverage:** 48.7805% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateLvtAccordingToLiveness` **(Many-Argument Workhorses)** (Impact: 83.3)
    * *Intent:* /* * Before ApiVersion 2.2. * We do not want to spill dead variables, thus, we shrink its LVT record...
  * `min` **(Defensive Guards)** (Impact: 61.3)
  * `calculateVariablesToSpill` **(Many-Argument Workhorses)** (Impact: 54.7)
    * *Intent:* // We consider variable liveness to avoid problems with inline suspension functions: // <spill varia...
  * `transformCallAndReturnStateLabel` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `spillVariables` **(Many-Argument Workhorses)** (Impact: 36.9)
    * *Intent:* /** * Main logic here: A variable can be either alive or dead, and it can be visible by debugger or ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 188`, `args: 83`, `func_start: 72`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 65`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 48`, `doc: 4`, `test: 6`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 1e-05
  * `Imports (Out-Degree: 9):` kotlin.math.max, org.jetbrains.kotlin.codegen.*, org.jetbrains.kotlin.codegen.inline.*, org.jetbrains.kotlin.codegen.optimization.common.*, org.jetbrains.kotlin.codegen.optimization.fixStack.FixStackMethodTransformer, org.jetbrains.kotlin.codegen.state.JvmBackendConfig, org.jetbrains.kotlin.load.java.JvmAbi, org.jetbrains.kotlin.resolve.jvm.AsmTypes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `libraries/stdlib/src/kotlin/time/Duration.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 914.74 | **LOC:** 1629 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.008; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 10.303% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 204.6)
    * *Intent:* // A temporary workaround for KT-81995, the constructor has to be private once the issue is resolved...
  * `parseDefaultStringFormat` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* /** * Parses default duration format (e.g., `"1h 30m"`, `"45s"`, `"500ms"`). * Note: While `"Infinit...
  * `parseIsoStringFormat` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* /** * Parses ISO-8601 duration format (e.g., `"PT1H30M45S"`). * */
  * `times` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* /** * Returns a duration whose value is this duration value multiplied by the given [scale] number. ...
  * `toString` **(I/O & Config Routines)** (Impact: 27.2)
    * *Intent:* * with one of sub-second units: `ms` (milliseconds), `us` (microseconds), or `ns` (nanoseconds): * `...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 139`, `args: 79`, `func_start: 66`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 52`, `planned_debt: 1`
* *Architecture:* `api: 88`, `import: 3`
* *Defense:* `safety: 10`, `doc: 87`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` kotlin.contracts.*, kotlin.jvm.JvmInline, kotlin.math.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/internal/wrappers/KotlinWrapperPre2_4_0.kt` -> Churn: **100.0%** | Cog Load: 22.3921% | Debt: 96.4258%
- `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/main/main.kt` -> Churn: **88.56%** | Cog Load: 16.8888% | Debt: 95.6075%
- `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/KotlinxCoroutinesCore/KotlinxCoroutinesCore.kt` -> Churn: **81.55%** | Cog Load: 46.1248% | Debt: 99.4533%
- `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnnotationChecker.kt` -> Churn: **73.25%** | Cog Load: 52.8467% | Debt: 15.1569%
- `native/swift/sir-providers/src/org/jetbrains/kotlin/sir/providers/impl/BridgeProvider/TypeBridging.kt` -> Churn: **73.25%** | Cog Load: 61.3572% | Debt: 83.962%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt` -> **Derek Xu** (100.0% isolated ownership) | Magnitude: 2621.8
- `compiler/fir/resolve/src/org/jetbrains/kotlin/fir/resolve/transformers/body/resolve/FirExpressionsResolveTransformer.kt` -> **Denis.Zharkov** (100.0% isolated ownership) | Magnitude: 1142.46
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirResolver.kt` -> **Denis.Zharkov** (100.0% isolated ownership) | Magnitude: 985.26
- `compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrVisitor.kt` -> **Denis.Zharkov** (100.0% isolated ownership) | Magnitude: 901.86
- `compiler/fir/fir-serialization/src/org/jetbrains/kotlin/fir/serialization/FirElementSerializer.kt` -> **Mikhail Glukhikh** (100.0% isolated ownership) | Magnitude: 858.96

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/descriptors/src/org/jetbrains/kotlin/types/KotlinType.kt` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 93.6121%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `core/compiler.common/src/org/jetbrains/kotlin/name/ClassId.kt` -> **Severity: 1.243** (Embedded: 0.0176 * Error Risk: 70.6956%)
- `core/compiler.common/src/org/jetbrains/kotlin/name/FqName.kt` -> **Severity: 1.026** (Embedded: 0.0189 * Error Risk: 54.4096%)
- `libraries/stdlib/native-wasm/src/kotlin/text/regex/Pattern.kt` -> **Severity: 0.917** (Embedded: 0.01 * Error Risk: 91.7527%)
- `compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt` -> **Severity: 0.913** (Embedded: 0.017 * Error Risk: 53.6699%)
- `core/compiler.common/src/org/jetbrains/kotlin/name/Name.java` -> **Severity: 0.888** (Embedded: 0.0248 * Error Risk: 35.7996%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt` -> **Severity: 572.2** (Blast Radius: 5.722 * Doc Risk: 100.0%)
- `compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/Project.kt` -> **Severity: 368.2** (Blast Radius: 3.682 * Doc Risk: 100.0%)
- `core/compiler.common/src/org/jetbrains/kotlin/name/Name.java` -> **Severity: 334.1** (Blast Radius: 3.341 * Doc Risk: 100.0%)
- `core/compiler.common/src/org/jetbrains/kotlin/name/FqName.kt` -> **Severity: 265.1** (Blast Radius: 2.651 * Doc Risk: 100.0%)
- `compiler/fir/tree/src/org/jetbrains/kotlin/fir/FirSession.kt` -> **Severity: 112.5** (Blast Radius: 1.125 * Doc Risk: 100.0%)

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
