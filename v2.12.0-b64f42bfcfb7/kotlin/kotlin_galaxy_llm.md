# ARCHITECTURAL_BRIEF: kotlin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/JetBrains/kotlin` |
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
- **Scope:** 111712 analyzed artifact(s), 3240703 LOC.
- **Load-bearing artifact:** `compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt` -- 1621 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrorsDefaultMessages.kt` -- pulls in 934 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `libraries/stdlib/common/src/generated/_Arrays.kt` at magnitude 11812.82 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 111712 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8195 |
| Total LOC | 3240703 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.2% |
| Dominant Lang | KOTLIN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7203 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0823 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1704 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| KOTLIN | 67435 | 2525471 | 60.4% |
| PLAINTEXT | 36136 | 5 | 32.3% |
| JAVA | 4447 | 540296 | 4.0% |
| MAKEFILE | 493 | 2780 | 0.4% |
| CPP | 483 | 53067 | 0.4% |
| XML | 450 | 0 | 0.4% |
| GROOVY | 379 | 6906 | 0.3% |
| OBJECTIVE-C | 360 | 17233 | 0.3% |
| JAVASCRIPT | 340 | 6017 | 0.3% |
| SWIFT | 284 | 28961 | 0.3% |
| JSON | 253 | 21155 | 0.2% |
| MARKDOWN | 240 | 0 | 0.2% |
| TYPESCRIPT | 162 | 10223 | 0.1% |
| C | 89 | 15742 | 0.1% |
| SHELL | 45 | 1865 | 0.0% |
| PHP | 30 | 6094 | 0.0% |
| BATCH | 19 | 833 | 0.0% |
| PROTO | 17 | 1933 | 0.0% |
| RUBY | 13 | 179 | 0.0% |
| HTML | 7 | 73 | 0.0% |
| M4 | 7 | 9 | 0.0% |
| CSS | 5 | 231 | 0.0% |
| PYTHON | 5 | 1249 | 0.0% |
| DOCKERFILE | 5 | 158 | 0.0% |
| YAML | 4 | 187 | 0.0% |
| CSV | 2 | 22 | 0.0% |
| SCALA | 1 | 5 | 0.0% |
| YACC | 1 | 9 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 111709 |
| utf-8 | bom | 3 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 52%, Interface Declarations Files 9%, Declarative / Non-Code 7%, Parameter Forwarders Files 7%, Generic / Templated Code Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 75329 | 67.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 36375 | 32.6% |
| Static: Minified & Vendor Opaque Mass | 8 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8195*

**Composition by Extension & Reason:**
- `.kt`: 1041x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 137x Excluded: Neighborhood Micro-Mass Limit Exceeded, 104x Excluded (Machine-Generated Source Code Signature: 21 LOC)
- `.txt`: 863x Excluded: Neighborhood Micro-Mass Limit Exceeded, 428x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 2450 commas in 571 LOC)
- `.info`: 1041x Excluded (Unsupported Extension: '.info')
- `no_extension`: 229x Unsupported Format (.undeterminable), 155x Excluded (Unsupported Extension: '.instructions'), 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.args`: 449x Excluded (Unsupported Extension: '.args')
- `.disabled`: 373x Unsupported Format (.disabled)
- `.def`: 55x Statistical Anomaly (Z-Score: -3372.50 < -4.55), 48x Statistical Anomaly (Z-Score: -5620.83 < -4.55), 35x Statistical Anomaly (Z-Score: -50587.50 < -4.55)
- `.new`: 202x Excluded (Unsupported Extension: '.new'), 3x Unsupported Format (.new)
- `.pom`: 192x Unsupported Format (.pom)
- `.java`: 104x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Saturation: Line 6 exceeds 500 chars), 4x Excluded (Saturation: Line 98 exceeds 500 chars)
- `.values`: 153x Excluded (Unsupported Extension: '.values')
- `.iml`: 116x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 99x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 7 exceeds 500 chars), 2x Excluded (Saturation: Line 31 exceeds 500 chars)
- `.dot`: 106x Excluded (Unsupported Extension: '.dot'), 1x Unsupported Format (.dot)
- `.class`: 94x Excluded (Explicitly Denied Extension: '.class')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 19.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 29.6 | 36.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 23.1 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 78.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 96.1 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 53733 | 11025 | 0 | `compiler/testData/codegen/box/primitiveTypes/crossTypeEquals.kt` |
| cleanup | 1580 | 679 | 0 | `compiler/testData/diagnostics/tests/Serializable.fir.kt` |
| guards | 233536 | 25718 | 4 | `analysis/analysis-api-fir/gen/org/jetbrains/kotlin/analysis/api/fir/diagnostics/KaFirDiagnosticsImpl.kt` |
| danger | 215018 | 36728 | 4 | `libraries/stdlib/common/src/generated/_Arrays.kt` |
| concurrency | 18303 | 3055 | 0 | `kotlin-native/runtime/test/concurrent/AtomicArrayTest.kt` |
| connectivity | 181743 | 21211 | 2 | `libraries/stdlib/common/src/generated/_Arrays.kt` |
| io | 19467 | 3253 | 0 | `compiler/tests-spec/tests/org/jetbrains/kotlin/spec/checkers/DiagnosticsTestSpecGenerated.java` |
| crypto | 1 | 1 | 0 | `kotlin-native/tools/llvm_builder/package.py` |
| ipc | 137 | 71 | 0 | `libraries/mvnw` |
| time | 209 | 86 | 0 | `kotlin-native/runtime/src/main/cpp/Clock.hpp` |
| serialization | 196 | 66 | 0 | `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/Kotlin2JsGradlePluginIT.kt` |
| regex | 8928 | 1332 | 0 | `compiler/tests-spec/tests/org/jetbrains/kotlin/spec/checkers/DiagnosticsTestSpecGenerated.java` |
| events | 1950 | 523 | 0 | `compiler/resolution/src/org/jetbrains/kotlin/resolve/calls/model/KotlinCallDiagnostics.kt` |
| tests | 203353 | 13957 | 1 | `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveCallTestGenerated.java` |
| docs | 33139 | 7151 | 0 | `libraries/stdlib/common/src/generated/_Arrays.kt` |
| debt | 48413 | 9070 | 0 | `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` |
| mutation | 497900 | 45298 | 8 | `libraries/stdlib/common/src/generated/_Arrays.kt` |
| dead_code | 173490 | 50681 | 2 | `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveCallTestGenerated.java` |
| credential | 308 | 112 | 0 | `js/js.translator/testData/package-lock.json` |
| threat | 2361 | 91 | 0 | `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptLexer.java` |
| ml_ai | 5732 | 896 | 0 | `kotlin-native/performance/startup/src/commonMain/kotlin/org/jetbrains/startup/SingletonInitBenchmark.kt` |
| ui | 8666 | 976 | 0 | `plugins/compose/compiler-hosted/integration-tests/src/jvmTest/kotlin/androidx/compose/compiler/plugins/kotlin/ControlFlowTransformTests.kt` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `compiler/tests-spec/tests/org/jetbrains/kotlin/spec/checkers/DiagnosticsTestSpecGenerated.java` (Hits: 378)
- `settings.gradle` (Hits: 237)
- `compiler/tests-spec/tests/org/jetbrains/kotlin/spec/codegen/BlackBoxCodegenTestSpecGenerated.java` (Hits: 234)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **File.kt** (`compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt`) — 1621 inbound connections
2. **Name.java** (`core/compiler.common/src/org/jetbrains/kotlin/name/Name.java`) — 1467 inbound connections
3. **FqName.kt** (`core/compiler.common/src/org/jetbrains/kotlin/name/FqName.kt`) — 914 inbound connections
4. **TestMetadata.java** (`compiler/test-infrastructure-utils.common/testFixtures/org/jetbrains/kotlin/test/TestMetadata.java`) — 892 inbound connections
5. **KtTestUtil.java** (`compiler/test-infrastructure-utils/testFixtures/org/jetbrains/kotlin/test/util/KtTestUtil.java`) — 860 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **FirErrorsDefaultMessages.kt** (`compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrorsDefaultMessages.kt`) — 934 outbound dependencies
2. **loadInterpreter.kt** (`plugins/kotlin-dataframe/kotlin-dataframe.k2/src/org/jetbrains/kotlinx/dataframe/plugin/loadInterpreter.kt`) — 328 outbound dependencies
3. **FirErrors.kt** (`compiler/fir/checkers/gen/org/jetbrains/kotlin/fir/analysis/diagnostics/FirErrors.kt`) — 142 outbound dependencies
4. **FirJvmErrorsDefaultMessages.kt** (`compiler/fir/checkers/checkers.jvm/src/org/jetbrains/kotlin/fir/analysis/diagnostics/jvm/FirJvmErrorsDefaultMessages.kt`) — 124 outbound dependencies
5. **KaFirCompilerFacility.kt** (`analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/components/KaFirCompilerFacility.kt`) — 110 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `init` **(Compute Cores)** (@ `compiler/tests-spec/testData/diagnostics/notLinked/dfa/pos/1.fir.kt`) -> Impact: **895.8** | LOC: 736
- `init` **(Compute Cores)** (@ `compiler/tests-spec/testData/diagnostics/notLinked/dfa/pos/1.fir.kt`) -> Impact: **895.8** | LOC: 736
- `init` **(Compute Cores)** (@ `compiler/tests-spec/testData/diagnostics/notLinked/dfa/pos/1.fir.kt`) -> Impact: **895.8** | LOC: 735
- `init` **(Compute Cores)** (@ `compiler/tests-spec/testData/diagnostics/notLinked/dfa/pos/1.kt`) -> Impact: **895.8** | LOC: 736
- `init` **(Compute Cores)** (@ `compiler/tests-spec/testData/diagnostics/notLinked/dfa/pos/1.kt`) -> Impact: **895.8** | LOC: 736
- `init` **(Compute Cores)** (@ `compiler/tests-spec/testData/diagnostics/notLinked/dfa/pos/1.kt`) -> Impact: **895.8** | LOC: 735
- `elf_add` **(Many-Argument Workhorses)** (@ `kotlin-native/runtime/src/libbacktrace/c/elf.c`) -> Impact: **716.5** | LOC: 806
  * *Intent:* base_address is determined. */
- `PrintStack` **(Many-Argument Workhorses)** (@ `kotlin-native/tools/minidump-analyzer/src/main/cpp/main.cc`) -> Impact: **543.8** | LOC: 638
  * *Intent:* // PrintStack prints the call stack in |stack| to stdout, in a reasonably // useful form. Module, function, and source file names are displayed if // ...
- `init` **(Compute Cores)** (@ `compiler/tests-spec/testData/diagnostics/notLinked/dfa/pos/1.fir.kt`) -> Impact: **384.1** | LOC: 302
- `init` **(Compute Cores)** (@ `compiler/tests-spec/testData/diagnostics/notLinked/dfa/pos/1.kt`) -> Impact: **384.1** | LOC: 302

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/proto` | 171 | 27831.8 | 16.7% | 95.69% |
| `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver` | 27 | 24656.58 | 0.0% | 0.0% |
| `libraries/stdlib/common/src/generated` | 14 | 22087.6 | 30.52% | 41.85% |
| `analysis/analysis-api-standalone/tests-gen/org/jetbrains/kotlin/analysis/api/standalone/fir/test/cases/generated/cases/components/resolver` | 11 | 13184.02 | 0.0% | 0.0% |
| `analysis/analysis-api-fe10/tests-gen/org/jetbrains/kotlin/analysis/api/fe10/test/cases/generated/cases/components/resolver` | 8 | 12907.76 | 0.0% | 0.0% |
| `kotlin-native/runtime/src/libbacktrace/c` | 13 | 10319.28 | 64.27% | 24.63% |
| `analysis/low-level-api-fir/tests-gen/org/jetbrains/kotlin/analysis/low/level/api/fir` | 42 | 10116.86 | 0.0% | 98.62% |
| `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated` | 6 | 9589.74 | 5.38% | 85.73% |
| `kotlin-native/runtime/src/main/cpp` | 132 | 8984.32 | 18.74% | 44.2% |
| `compiler/frontend/src/org/jetbrains/kotlin/resolve` | 89 | 8351.82 | 14.92% | 28.58% |

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
- `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveCallTestGenerated.java` -> **976** Orphaned Functions | **122** Duplicates
- `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveCandidatesTestGenerated.java` -> **976** Orphaned Functions | **122** Duplicates
- `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveReferenceTestGenerated.java` -> **976** Orphaned Functions | **122** Duplicates
- `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveSymbolTestGenerated.java` -> **976** Orphaned Functions | **122** Duplicates
- `analysis/low-level-api-fir/tests-gen/org/jetbrains/kotlin/analysis/low/level/api/fir/resolve/SourceResolveCandidatesFirTreeConsistencyTestGenerated.java` -> **975** Orphaned Functions | **122** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `libraries/scripting/dependencies-maven/test/kotlin/script/experimental/test/AetherResolveSessionTest.kt` -> **96.1253%** Exposure
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/SwiftPMImportPopularSwiftPMDependenciesTests.kt` -> **20.0708%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `61` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `182955` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `libraries/stdlib/common/src/generated/_Arrays.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.762)
- **Top Global Matches:** file_cluster_0: 8.762, file_cluster_5: 9.86, file_cluster_12: 10.563
- **Magnitude:** 11812.82 | **LOC:** 26959 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.9%), Complexity Load (formerly Cognitive Load) (44.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `joinTo` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /** * Appends the string from all the elements separated using [separator] and using the given [pref...
  * `joinTo` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /** * Appends the string from all the elements separated using [separator] and using the given [pref...
  * `joinTo` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /** * Appends the string from all the elements separated using [separator] and using the given [pref...
  * `joinTo` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /** * Appends the string from all the elements separated using [separator] and using the given [pref...
  * `joinTo` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /** * Appends the string from all the elements separated using [separator] and using the given [pref...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1053 instances
* *State Mutation (weighted view):* 3188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2372`, `structural_boundaries: 4231`, `args: 1846`, `func_start: 1801`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 1082`, `unreferenced_by_name: 20`
* *Architecture:* `api: 1835`, `import: 4`
* *Defense:* `safety: 119`, `doc: 1835`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` kotlin.contracts.*, kotlin.random.*, kotlin.ranges.contains, kotlin.ranges.reversed
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/js.parser/src/org/jetbrains/kotlin/js/parser/antlr/generated/JavaScriptParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 11.379)
- **Top Global Matches:** file_cluster_5: 11.379, file_cluster_12: 12.042, file_cluster_7: 13.443
- **Magnitude:** 7391.92 | **LOC:** 11868 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **10**; blast radius 0.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (58.9%), Guard Balance (formerly Safety Score) (53.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `singleExpressionImpl` **(Many-Argument Workhorses)** (Impact: 187.5)
  * `importFromBlock` **(Compute Cores)** (Impact: 128.8)
  * `arrayElement` **(Compute Cores)** (Impact: 88.1)
  * `keyword` **(I/O & Config Routines)** (Impact: 69.9)
  * `classElementName` **(Compute Cores)** (Impact: 69.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 260 instances
* *State Mutation (weighted view):* 855
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1909`, `structural_boundaries: 3152`, `args: 1506`, `func_start: 1506`, `class_start: 167`
* *Risk/State:* `safety_bypasses: 537`, `state_mutation: 335`, `duplicate_logic: 483`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1678`, `import: 6`
* *Defense:* `safety: 781`, `doc: 1`, `sync_locks: 2`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` java.util.ArrayList, java.util.Iterator, java.util.List, org.antlr.v4.runtime.*, org.antlr.v4.runtime.atn.*, org.antlr.v4.runtime.dfa.DFA, org.antlr.v4.runtime.misc.*, org.antlr.v4.runtime.tree.*...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `kotlin-native/runtime/src/libbacktrace/c/elf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.628)
- **Top Global Matches:** file_cluster_6: 6.628, file_cluster_4: 8.5, file_cluster_16: 15.535
- **Magnitude:** 4590.82 | **LOC:** 4920 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elf_add` **(Many-Argument Workhorses)** (Impact: 716.5)
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
* *Amplified Cascading Flux:* 783 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2484
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 363`, `args: 57`, `func_start: 42`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 918`
* *Architecture:* `api: 26`, `import: 11`
* *Defense:* `safety: 113`, `immutability_locks: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 9):` backtrace.h, config.h, errno.h, internal.h, link.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libraries/stdlib/common/src/generated/_UArrays.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.006)
- **Top Global Matches:** file_cluster_0: 9.006, file_cluster_13: 9.676, file_cluster_16: 9.816
- **Magnitude:** 4469.54 | **LOC:** 11751 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%), Complexity Load (formerly Cognitive Load) (36.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `take` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * Returns a list containing first [n] elements. * * */
  * `take` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * Returns a list containing first [n] elements. * * */
  * `take` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * Returns a list containing first [n] elements. * * */
  * `take` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * Returns a list containing first [n] elements. * * */
  * `maxBy` **(Stateful Encapsulated Methods)** (Impact: 8.1)
    * *Intent:* /** * Returns the first element yielding the largest value of the given [selector] function. * * If ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 388 instances
* *State Mutation (weighted view):* 1164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 868`, `structural_boundaries: 1657`, `args: 712`, `func_start: 688`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 388`, `unreferenced_by_name: 12`
* *Architecture:* `api: 704`, `import: 4`
* *Defense:* `safety: 44`, `doc: 704`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` kotlin.contracts.*, kotlin.random.*, kotlin.ranges.contains, kotlin.ranges.reversed
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kotlin-native/runtime/src/libbacktrace/c/dwarf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.616)
- **Top Global Matches:** file_cluster_6: 6.616, file_cluster_8: 11.695, file_cluster_4: 13.726
- **Magnitude:** 3843.7 | **LOC:** 4416 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 0.029; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.1%), Guard Balance (formerly Safety Score) (72.1%)
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
* *Amplified Cascading Flux:* 550 instances
* *State Mutation (weighted view):* 1740
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 616`, `structural_boundaries: 812`, `args: 62`, `func_start: 59`, `class_start: 159`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 640`, `fragile_debt: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 67`, `immutability_locks: 150`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 7):` backtrace.h, config.h, errno.h, filenames.h, internal.h, stdlib.h, string.h, types.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `compiler/tests-spec/tests/org/jetbrains/kotlin/spec/checkers/DiagnosticsTestSpecGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 8.122)
- **Top Global Matches:** file_cluster_13: 8.122, file_cluster_10: 9.245, file_cluster_11: 9.302
- **Magnitude:** 3349.36 | **LOC:** 8140 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **8**; blast radius 0.013; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (37.1%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3012`, `args: 1775`, `func_start: 1398`, `class_start: 377`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 26`, `duplicate_logic: 377`, `unreferenced_by_name: 158`
* *Architecture:* `io: 378`, `api: 1398`, `import: 8`
* *Defense:* `safety: 36`, `doc: 1`, `test: 1776`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.kotlin.test.JUnit3RunnerWithInners, org.jetbrains.kotlin.test.KotlinTestUtils, org.jetbrains.kotlin.test.TestMetadata, org.jetbrains.kotlin.test.util.KtTestUtil, org.junit.runner.RunWith
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `compiler/fir/raw-fir/psi2fir/src/org/jetbrains/kotlin/fir/builder/PsiRawFirBuilder.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.617)
- **Top Global Matches:** file_cluster_4: 7.617, file_cluster_12: 8.377, file_cluster_16: 9.866
- **Magnitude:** 2936.5 | **LOC:** 3963 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **54**; blast radius 0.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.2%)
- **Documentation Coverage:** 96.9697% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitNamedFunction` **(Many-Argument Workhorses)** (Impact: 67.6)
  * `extractSuperTypeListEntriesTo` **(Many-Argument Workhorses)** (Impact: 66.3)
  * `toFirPropertyAccessor` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `toFirConstructor` **(Many-Argument Workhorses)** (Impact: 57.2)
    * *Intent:* /** */
  * `toFirProperty` **(Many-Argument Workhorses)** (Impact: 49.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 329 instances
* *State Mutation (weighted view):* 1505
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 481`, `structural_boundaries: 327`, `args: 192`, `func_start: 136`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 847`, `planned_debt: 9`
* *Architecture:* `api: 52`, `concurrency: 1`, `import: 54`
* *Defense:* `safety: 206`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 30):` com.intellij.extapi.psi.StubBasedPsiElementBase, com.intellij.psi.PsiElement, com.intellij.psi.PsiErrorElement, com.intellij.psi.tree.IElementType, com.intellij.psi.util.childrenOfType, com.intellij.util.AstLoadingFilter, org.jetbrains.kotlin.*, org.jetbrains.kotlin.builtins.StandardNames...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveCallTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.429)
- **Top Global Matches:** file_cluster_13: 7.429, file_cluster_12: 9.048, file_cluster_2: 10.095
- **Magnitude:** 2776.4 | **LOC:** 7341 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9133% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1366`, `args: 1192`, `func_start: 1192`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 78`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 976`
* *Architecture:* `io: 78`, `api: 1192`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2382`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fir.test.configurators.AnalysisApiFirTestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveCallTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveCandidatesTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.429)
- **Top Global Matches:** file_cluster_13: 7.429, file_cluster_12: 9.048, file_cluster_2: 10.095
- **Magnitude:** 2776.4 | **LOC:** 7341 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9133% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1366`, `args: 1192`, `func_start: 1192`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 78`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 976`
* *Architecture:* `io: 78`, `api: 1192`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2382`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fir.test.configurators.AnalysisApiFirTestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveCandidatesTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveReferenceTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.429)
- **Top Global Matches:** file_cluster_13: 7.429, file_cluster_12: 9.048, file_cluster_2: 10.095
- **Magnitude:** 2776.4 | **LOC:** 7341 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9133% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1366`, `args: 1192`, `func_start: 1192`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 78`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 976`
* *Architecture:* `io: 78`, `api: 1192`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2382`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fir.test.configurators.AnalysisApiFirTestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveReferenceTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveSymbolTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.429)
- **Top Global Matches:** file_cluster_13: 7.429, file_cluster_12: 9.048, file_cluster_2: 10.095
- **Magnitude:** 2776.4 | **LOC:** 7341 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9133% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1366`, `args: 1192`, `func_start: 1192`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 78`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 976`
* *Architecture:* `io: 78`, `api: 1192`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2382`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fir.test.configurators.AnalysisApiFirTestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveSymbolTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/low-level-api-fir/tests-gen/org/jetbrains/kotlin/analysis/low/level/api/fir/resolve/SourceResolveCandidatesFirTreeConsistencyTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.45)
- **Top Global Matches:** file_cluster_13: 7.45, file_cluster_12: 9.06, file_cluster_2: 10.107
- **Magnitude:** 2773.34 | **LOC:** 7317 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (33.2%), Connectivity (formerly Api Exposure) (15.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 99.9566% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1354`, `args: 1191`, `func_start: 1191`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 78`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 975`
* *Architecture:* `io: 78`, `api: 1191`, `import: 7`
* *Defense:* `doc: 1`, `test: 2382`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 7):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.kotlin.test.TestMetadata, org.jetbrains.kotlin.test.util.KtTestUtil, org.junit.jupiter.api.Nested, org.junit.jupiter.api.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fe10/tests-gen/org/jetbrains/kotlin/analysis/api/fe10/test/cases/generated/cases/components/resolver/Fe10IdeNormalAnalysisSourceModuleResolveCallTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.416)
- **Top Global Matches:** file_cluster_13: 7.416, file_cluster_12: 9.051, file_cluster_2: 10.086
- **Magnitude:** 2757.56 | **LOC:** 7291 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1356`, `args: 1184`, `func_start: 1184`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 77`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 969`
* *Architecture:* `io: 77`, `api: 1184`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2366`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fe10.test.configurator.AnalysisApiFe10TestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveCallTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fe10/tests-gen/org/jetbrains/kotlin/analysis/api/fe10/test/cases/generated/cases/components/resolver/Fe10IdeNormalAnalysisSourceModuleResolveCandidatesTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.416)
- **Top Global Matches:** file_cluster_13: 7.416, file_cluster_12: 9.051, file_cluster_2: 10.086
- **Magnitude:** 2757.56 | **LOC:** 7291 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1356`, `args: 1184`, `func_start: 1184`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 77`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 969`
* *Architecture:* `io: 77`, `api: 1184`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2366`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fe10.test.configurator.AnalysisApiFe10TestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveCandidatesTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fe10/tests-gen/org/jetbrains/kotlin/analysis/api/fe10/test/cases/generated/cases/components/resolver/Fe10IdeNormalAnalysisSourceModuleResolveReferenceTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.416)
- **Top Global Matches:** file_cluster_13: 7.416, file_cluster_12: 9.051, file_cluster_2: 10.086
- **Magnitude:** 2757.56 | **LOC:** 7291 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1356`, `args: 1184`, `func_start: 1184`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 77`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 969`
* *Architecture:* `io: 77`, `api: 1184`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2366`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fe10.test.configurator.AnalysisApiFe10TestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveReferenceTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fe10/tests-gen/org/jetbrains/kotlin/analysis/api/fe10/test/cases/generated/cases/components/resolver/Fe10IdeNormalAnalysisSourceModuleResolveSymbolTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.416)
- **Top Global Matches:** file_cluster_13: 7.416, file_cluster_12: 9.051, file_cluster_2: 10.086
- **Magnitude:** 2757.56 | **LOC:** 7291 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1356`, `args: 1184`, `func_start: 1184`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 77`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 969`
* *Architecture:* `io: 77`, `api: 1184`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2366`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fe10.test.configurator.AnalysisApiFe10TestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveSymbolTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-standalone/tests-gen/org/jetbrains/kotlin/analysis/api/standalone/fir/test/cases/generated/cases/components/resolver/FirStandaloneNormalAnalysisSourceModuleResolveCallTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.416)
- **Top Global Matches:** file_cluster_13: 7.416, file_cluster_12: 9.051, file_cluster_2: 10.086
- **Magnitude:** 2757.56 | **LOC:** 7291 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1356`, `args: 1184`, `func_start: 1184`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 77`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 969`
* *Architecture:* `io: 77`, `api: 1184`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2366`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveCallTest, org.jetbrains.kotlin.analysis.api.standalone.fir.test.configurators.AnalysisApiFirStandaloneModeTestConfiguratorFactory, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-standalone/tests-gen/org/jetbrains/kotlin/analysis/api/standalone/fir/test/cases/generated/cases/components/resolver/FirStandaloneNormalAnalysisSourceModuleResolveCandidatesTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.416)
- **Top Global Matches:** file_cluster_13: 7.416, file_cluster_12: 9.051, file_cluster_2: 10.086
- **Magnitude:** 2757.56 | **LOC:** 7291 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1356`, `args: 1184`, `func_start: 1184`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 77`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 969`
* *Architecture:* `io: 77`, `api: 1184`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2366`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveCandidatesTest, org.jetbrains.kotlin.analysis.api.standalone.fir.test.configurators.AnalysisApiFirStandaloneModeTestConfiguratorFactory, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-standalone/tests-gen/org/jetbrains/kotlin/analysis/api/standalone/fir/test/cases/generated/cases/components/resolver/FirStandaloneNormalAnalysisSourceModuleResolveReferenceTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.416)
- **Top Global Matches:** file_cluster_13: 7.416, file_cluster_12: 9.051, file_cluster_2: 10.086
- **Magnitude:** 2757.56 | **LOC:** 7291 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1356`, `args: 1184`, `func_start: 1184`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 77`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 969`
* *Architecture:* `io: 77`, `api: 1184`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2366`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveReferenceTest, org.jetbrains.kotlin.analysis.api.standalone.fir.test.configurators.AnalysisApiFirStandaloneModeTestConfiguratorFactory, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-standalone/tests-gen/org/jetbrains/kotlin/analysis/api/standalone/fir/test/cases/generated/cases/components/resolver/FirStandaloneNormalAnalysisSourceModuleResolveSymbolTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.416)
- **Top Global Matches:** file_cluster_13: 7.416, file_cluster_12: 9.051, file_cluster_2: 10.086
- **Magnitude:** 2757.56 | **LOC:** 7291 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1356`, `args: 1184`, `func_start: 1184`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 77`, `planned_debt: 2`, `duplicate_logic: 122`, `unreferenced_by_name: 969`
* *Architecture:* `io: 77`, `api: 1184`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 2366`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveSymbolTest, org.jetbrains.kotlin.analysis.api.standalone.fir.test.configurators.AnalysisApiFirStandaloneModeTestConfiguratorFactory, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/tests-gen/org/jetbrains/kotlin/jvm/compiler/LoadJavaTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.494)
- **Top Global Matches:** file_cluster_12: 8.494, file_cluster_13: 9.0, file_cluster_7: 9.559
- **Magnitude:** 2316.98 | **LOC:** 5317 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **70** in-repo importer(s); it depends on **8**; blast radius 0.059; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (40.9%), Connectivity (formerly Api Exposure) (14.6%), Concurrency Surface (formerly Concurrency) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1550`, `args: 1098`, `func_start: 999`, `class_start: 101`
* *Risk/State:* `safety_bypasses: 101`, `duplicate_logic: 97`, `unreferenced_by_name: 523`
* *Architecture:* `io: 101`, `api: 1000`, `concurrency: 2`, `import: 8`
* *Defense:* `doc: 1`, `test: 1099`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.kotlin.test.JUnit3RunnerWithInners, org.jetbrains.kotlin.test.KotlinTestUtils, org.jetbrains.kotlin.test.TestMetadata, org.jetbrains.kotlin.test.util.KtTestUtil, org.junit.runner.RunWith
  * `Imported By (In-Degree: 70):` (Excluded from Brief to save tokens)

### `compiler/tests-gen/org/jetbrains/kotlin/jvm/compiler/javac/LoadJavaUsingJavacTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.494)
- **Top Global Matches:** file_cluster_12: 8.494, file_cluster_13: 9.0, file_cluster_7: 9.559
- **Magnitude:** 2316.98 | **LOC:** 5317 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (40.9%), Connectivity (formerly Api Exposure) (14.6%), Concurrency Surface (formerly Concurrency) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
  * `runTest` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1550`, `args: 1098`, `func_start: 999`, `class_start: 101`
* *Risk/State:* `safety_bypasses: 101`, `duplicate_logic: 97`, `unreferenced_by_name: 523`
* *Architecture:* `io: 101`, `api: 1000`, `concurrency: 2`, `import: 8`
* *Defense:* `doc: 1`, `test: 1099`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.kotlin.test.JUnit3RunnerWithInners, org.jetbrains.kotlin.test.KotlinTestUtils, org.jetbrains.kotlin.test.TestMetadata, org.jetbrains.kotlin.test.util.KtTestUtil, org.junit.runner.RunWith
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/compose/compiler-hosted/src/main/java/androidx/compose/compiler/plugins/kotlin/lower/ComposableFunctionBodyTransformer.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.897)
- **Top Global Matches:** file_cluster_4: 6.897, file_cluster_12: 7.942, file_cluster_16: 8.666
- **Magnitude:** 2285.5 | **LOC:** 5145 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **45**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (58.0%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 98.4906% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildPreambleStatementsAndReturnIfSkippingPossible` **(Many-Argument Workhorses)** (Impact: 137.5)
  * `visitNonRestartableComposableFunction` **(Many-Argument Workhorses)** (Impact: 67.7)
    * *Intent:* // At a high level, without useNonSkippingGroupOptimization, a non-restartable composable // functio...
  * `visitWhen` **(Compute Cores)** (Impact: 54.7)
  * `visitComposableLambda` **(Many-Argument Workhorses)** (Impact: 54.6)
    * *Intent:* // Composable lambdas are always wrapped with a ComposableLambda class, which has its own // group i...
  * `visitRestartableComposableFunction` **(Many-Argument Workhorses)** (Impact: 51.6)
    * *Intent:* // Most composable function declarations will be restartable. At a high level, this means // that fo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 177 instances
* *State Mutation (weighted view):* 696
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 611`, `structural_boundaries: 466`, `args: 269`, `func_start: 207`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 342`, `dead_code: 6`, `planned_debt: 10`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `import: 45`
* *Defense:* `safety: 155`, `doc: 20`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 31):` androidx.compose.compiler.plugins.kotlin.*, androidx.compose.compiler.plugins.kotlin.analysis.*, kotlin.math.abs, kotlin.math.absoluteValue, kotlin.math.ceil, kotlin.math.min, org.jetbrains.kotlin.backend.common.FileLoweringPass, org.jetbrains.kotlin.backend.common.extensions.IrPluginContext...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisLibrarySourceModuleResolveCallTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.412)
- **Top Global Matches:** file_cluster_13: 7.412, file_cluster_12: 8.996, file_cluster_2: 10.09
- **Magnitude:** 2257.78 | **LOC:** 5977 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (14.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.8933% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1117`, `args: 969`, `func_start: 969`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 65`, `planned_debt: 2`, `duplicate_logic: 80`, `unreferenced_by_name: 816`
* *Architecture:* `io: 65`, `api: 969`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 1936`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fir.test.configurators.AnalysisApiFirTestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveCallTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisLibrarySourceModuleResolveCandidatesTestGenerated.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.412)
- **Top Global Matches:** file_cluster_13: 7.412, file_cluster_12: 8.996, file_cluster_2: 10.09
- **Magnitude:** 2257.78 | **LOC:** 5977 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (33.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%), Connectivity (formerly Api Exposure) (14.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.9%)
- **Documentation Coverage:** 99.8933% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfigurator` **(Annotated & Test Methods)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
  * `run` **(Encapsulated Accessors)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1117`, `args: 969`, `func_start: 969`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 65`, `planned_debt: 2`, `duplicate_logic: 80`, `unreferenced_by_name: 816`
* *Architecture:* `io: 65`, `api: 969`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 1936`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` com.intellij.testFramework.TestDataPath, java.io.File, java.util.regex.Pattern, org.jetbrains.annotations.NotNull, org.jetbrains.kotlin.analysis.api.fir.test.configurators.AnalysisApiFirTestConfiguratorFactory, org.jetbrains.kotlin.analysis.api.impl.base.test.cases.components.resolver.AbstractResolveCandidatesTest, org.jetbrains.kotlin.analysis.test.framework.services.TargetPlatformEnum, org.jetbrains.kotlin.analysis.test.framework.test.configurators.AnalysisApiMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `compiler/testData/codegen/box/arrays/arraysOfInlineClass/arrayOfInlineClassOfArrayOfInlineClass.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 12, branch: 3, structural_boundaries: 3, args: 3
- `compiler/testData/codegen/boxJvm/inlineClasses/jvmStaticFunInInlineClassCompanionGeneric.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, class_start: 3, args: 2
- `plugins/scripting/scripting-compiler-impl/src/org/jetbrains/kotlin/scripting/definitions/LazyScriptDefinitionProvider.kt` (KOTLIN) | Magnitude: 50.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 27, core_var_decl: 18, encapsulation: 15
- `libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/UnsupportedKotlinLanguageVersionsMetadata.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, encapsulation: 4, api: 3
- `native/native.tests/testData/codegen/kclass/kclass0.kt` (KOTLIN) | Magnitude: 0.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 514, core_var_decl: 301, design_camel_case: 232, structural_boundaries: 170

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `kotlin-native/runtime/src/alloc/custom/cpp/SingleObjectPage.cpp` (CPP) | Magnitude: 13.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 10, args: 7, func_start: 7
- `compiler/testData/codegen/boxModernJdk/testsWithJava21/typeSwitch/whenByTypeSwitchNullCheck.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 7, branch: 5, panics_and_aborts: 5
- `compiler/testData/klib/syntheticAccessors/topLevelPrivate/crossFilePrivateLeak/contextSensitiveResolutionTypePositionWithCopyOfDefaultValue.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 6, args: 4, indent_spaces: 4, func_start: 3
- `compiler/testData/klib/syntheticAccessors/topLevelPrivate/crossModulePrivateLeak/contextSensitiveResolutionTypePositionWithCopyOfDefaultValue.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 6, args: 4, indent_spaces: 4, func_start: 3
- `compiler/testData/klib/syntheticAccessors/topLevelPrivate/singleFile/contextSensitiveResolutionTypePositionWithCopyOfDefaultValue.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 6, args: 4, indent_spaces: 4, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `libraries/tools/kotlin-gradle-plugin/src/functionalTest/kotlin/org/jetbrains/kotlin/gradle/util/androidUtils.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, import: 6, args: 5
- `compiler/testData/diagnostics/tests/inference/callableReferences/conversionLastStatementInLambda.fir.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, branch: 4, structural_boundaries: 4, args: 4
- `compiler/testData/diagnostics/tests/inference/callableReferences/conversionLastStatementInLambda.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, branch: 4, structural_boundaries: 4, args: 4
- `analysis/analysis-api-fir/src/org/jetbrains/kotlin/analysis/api/fir/scopes/FirJavaDeclaredMembersOnlyScope.kt` (KOTLIN) | Magnitude: 21.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 24, import: 10, args: 9
- `compiler/testData/codegen/boxJvm/reflection/call/returnUnit.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `native/executors/src/main/kotlin/org/jetbrains/kotlin/native/executors/XcodeProject.kt` (KOTLIN) | Magnitude: 41.26 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 112, core_var_decl: 25, structural_boundaries: 17, state_mutation: 16
- `analysis/analysis-api-impl-base/src/org/jetbrains/kotlin/analysis/api/impl/base/references/KaBaseSimpleNameReference.kt` (KOTLIN) | Magnitude: 27.82 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 27, branch: 18, safety: 16
- `compiler/testData/codegen/boxJvm/reflection/mapping/methodsFromObject.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 12, args: 5, func_start: 5
- `jps/jps-platform-api-signatures/src/org/jetbrains/jps/dependency/java/JvmElementUsage.java` (JAVA) | Magnitude: 18.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, args: 6, func_start: 5
- `compiler/container/src/org/jetbrains/kotlin/container/Storage.kt` (KOTLIN) | Magnitude: 137.12 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 46, branch: 33, reflection_metaprogramming: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `compiler/tests/org/jetbrains/kotlin/jvm/compiler/CustomGeneratedClassesTest.kt` (KOTLIN) | Magnitude: 10.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 15, import: 11, core_var_decl: 9
- `libraries/tools/abi-validation/abi-tools-api/src/test/kotlin/org/jetbrains/kotlin/abi/tools/KlibTargetNameTest.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 70, test: 23, structural_boundaries: 10, generics: 7
- `analysis/analysis-api/src/org/jetbrains/kotlin/analysis/api/renderer/declarations/renderers/callables/KaScriptSymbolRenderer.kt` (KOTLIN) | Magnitude: 8.66 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, import: 6, api: 3
- `jps/jps-plugin/testData/comparison/jvmOnly/packageFacadeMultifileClassChanged/new2.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 4, encapsulation: 4, args: 3, func_start: 3
- `jps/jps-plugin/testData/comparison/jvmOnly/packageFacadeMultifileClassChanged/old1.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 4, encapsulation: 4, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `compiler/testData/loadJava/compiledKotlin/prop/ExtVarIntTInClass.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 3, structural_boundaries: 2, panics_and_aborts: 2, class_start: 1
- `compiler/testData/loadJava/compiledKotlin/prop/ExtVarIntTQInClass.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 3, structural_boundaries: 2, panics_and_aborts: 2, class_start: 1
- `compiler/testData/loadJava/compiledKotlin/prop/ExtVarTIntInClass.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 3, structural_boundaries: 2, panics_and_aborts: 2, class_start: 1
- `compiler/testData/loadJava/compiledKotlin/prop/ExtVarTQIntInClass.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 3, structural_boundaries: 2, panics_and_aborts: 2, class_start: 1
- `compiler/testData/codegen/boxJvm/builtinStubMethods/nonTrivialUpperBound.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 8, generics: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `analysis/low-level-api-fir/src/org/jetbrains/kotlin/analysis/low/level/api/fir/transformers/LLFirLazyPhaseResolverByPhase.kt` (KOTLIN) | Magnitude: 14.9 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 12, structural_boundaries: 6, import: 2
- `compiler/testData/diagnostics/tests/dataFlowInfoTraversal/AndOr.fir.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 7, branch: 6, structural_boundaries: 2, args: 2
- `compiler/testData/diagnostics/tests/dataFlowInfoTraversal/AndOr.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 7, branch: 6, structural_boundaries: 2, args: 2
- `compiler/testData/codegen/box/multiplatform/k1/defaultArguments/inheritedViaAnotherInterfaceIndirectly.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 16, core_var_decl: 9, class_start: 7
- `compiler/testData/codegen/box/multiplatform/k2/defaultArguments/inheritedViaAnotherInterfaceIndirectly.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 16, core_var_decl: 9, class_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `analysis/analysis-api/testData/components/resolver/singleByPsi/withErrors/privateMember.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, indent_spaces: 2
- `libraries/stdlib/jvm/src/kotlin/io/FileReadWrite.kt` (KOTLIN) | Magnitude: 110.72 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 44, core_var_decl: 40, io: 26
- `compiler/resolution.common/src/org/jetbrains/kotlin/resolve/calls/inference/components/TypeVariableDependencyInformationProvider.kt` (KOTLIN) | Magnitude: 108.94 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 141, structural_boundaries: 46, branch: 36, encapsulation: 25
- `kotlin-native/klib/src/org/jetbrains/kotlin/cli/klib/klibUtils.kt` (KOTLIN) | Magnitude: 4.88 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 7, import: 3, indent_spaces: 3, args: 2
- `compiler/resolution/src/org/jetbrains/kotlin/contracts/model/functors/SubstitutingFunctor.kt` (KOTLIN) | Magnitude: 41.54 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 26, branch: 15, core_var_decl: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirRootIdePackageInCliDeprecations.kt` (KOTLIN) | Magnitude: 6.72 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 12, import: 9, reflection_metaprogramming: 5
- `kotlin-native/runtime/src/libbacktrace/c/simple.c` (C) | Magnitude: 31.4 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 31, pointers: 16, structural_boundaries: 14, state_mutation: 11
- `compiler/fir/checkers/checkers.web.common/src/org/jetbrains/kotlin/fir/analysis/web/common/checkers/declaration/FirMultipleJsExportDefaultAnnotationChecker.kt` (KOTLIN) | Magnitude: 5.0 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 14, import: 13, reflection_metaprogramming: 5
- `compiler/testData/diagnostics/tests/modifiers/const/ifConstVal.kt` (KOTLIN) | Magnitude: 0.02 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 16, core_var_decl: 10, globals: 9, immutability_locks: 9
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/cinteropImport/dep-with-cinterop/src/commonMain/kotlin/pkg/common.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 2, class_start: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/kotlin/org/jetbrains/kotlin/gradle/apple/GenerateSyntheticLinkageImportProjectTests.kt` (KOTLIN) | Magnitude: 0.06 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 260, core_var_decl: 77, design_snake_case: 57, structural_boundaries: 45
- `libraries/tools/kotlin-gradle-plugin-integration-tests/src/test/resources/testProject/new-mpp-android-source-sets/lib/src/commonMain/kotlin/CommonApi.kt` (KOTLIN) | Magnitude: 0.0 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1
- `analysis/low-level-api-fir/testData/lazyAnnotations/annotations/jvmName_getter_property.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 2, decorators: 1, reflection_metaprogramming: 1, dependency_injection: 1
- `analysis/low-level-api-fir/testData/lazyAnnotations/classIds/jvmName_getter_property.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 2, decorators: 1, reflection_metaprogramming: 1, dependency_injection: 1
- `analysis/low-level-api-fir/testData/lazyAnnotations/contains/jvmName_getter_property.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 2, decorators: 1, reflection_metaprogramming: 1, dependency_injection: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/driver/phases/TopLevelPhases.kt` (KOTLIN) | Magnitude: 211.16 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 377, core_var_decl: 83, structural_boundaries: 81, design_camel_case: 56
- `plugins/kotlinx-serialization/kotlinx-serialization.k2/src/org/jetbrains/kotlinx/serialization/compiler/fir/checkers/FirSerializationPluginClassChecker.kt` (KOTLIN) | Magnitude: 461.24 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 626, branch: 176, structural_boundaries: 144, core_var_decl: 105
- `core/reflection.jvm/src/kotlin/reflect/jvm/internal/ConvertFromJava.kt` (KOTLIN) | Magnitude: 172.56 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 206, branch: 66, core_var_decl: 61, structural_boundaries: 58
- `compiler/fir/fir2ir/jvm-backend/src/org/jetbrains/kotlin/fir/backend/jvm/FirJvmSerializerExtension.kt` (KOTLIN) | Magnitude: 223.16 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 319, structural_boundaries: 89, branch: 77, import: 38
- `compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/convertToIr.kt` (KOTLIN) | Magnitude: 162.44 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 412, structural_boundaries: 105, import: 54, core_var_decl: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `libraries/tools/kotlin-gradle-plugin-idea/src/testFixtures/kotlin/org/jetbrains/kotlin/gradle/idea/testFixtures/utils/serializationUtil.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 15, args: 6, core_var_decl: 6
- `compiler/testData/compileJavaAgainstKotlin/class/ImplementsListString.java` (JAVA) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, core_var_decl: 2, design_snake_case: 2
- `js/js.translator/testData/typescript-export/js/selective-export/selective-export.d.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, args: 10, func_start: 7
- `compiler/build-tools/kotlin-build-tools-api-forward-compatibility-tests/src/testCompatibility/kotlin/arguments/ScriptResolverEnvironmentConversionTest.kt` (KOTLIN) | Magnitude: 44.94 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 199, decorators: 35, test: 34, structural_boundaries: 32
- `plugins/kotlin-dataframe/testFixtures/org/jetbrains/kotlin/fir/dataframe/AbstractDataFrameBlackBoxCodegenTest.kt` (KOTLIN) | Magnitude: 5.98 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 25, import: 17, class_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `compiler/backend/src/org/jetbrains/kotlin/codegen/optimization/temporaryVals/TemporaryVariablesEliminationTransformer.kt` (KOTLIN) | Magnitude: 299.2 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 344, branch: 94, core_var_decl: 77, design_camel_case: 61
- `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/cfa/FirCallsEffectAnalyzer.kt` (KOTLIN) | Magnitude: 90.64 | Delta: **0.168** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 49, branch: 35, import: 27
- `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/declaration/FirAnnotationClassDeclarationChecker.kt` (KOTLIN) | Magnitude: 110.06 | Delta: **0.183** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 66, branch: 49, import: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `kotlin-native/runtime/src/mm/cpp/Weak.cpp` (CPP) | Magnitude: 9.64 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 14, import: 5, core_var_decl: 5
- `analysis/low-level-api-fir/tests-gen/org/jetbrains/kotlin/analysis/low/level/api/fir/SourceDeprecationsResolveTestGenerated.java` (JAVA) | Magnitude: 114.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 251, test: 96, decorators: 96, structural_boundaries: 73
- `libraries/stdlib/js/src/kotlin/wasmJs/JsException.kt` (KOTLIN) | Magnitude: 16.68 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: decorators: 5, structural_boundaries: 2, api: 2, doc: 2
- `analysis/analysis-api-fe10/tests-gen/org/jetbrains/kotlin/analysis/api/fe10/test/cases/generated/cases/components/scopeProvider/Fe10IdeNormalAnalysisSourceModuleFileScopeTestGenerated.java` (JAVA) | Magnitude: 12.84 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 26, import: 16, decorators: 10
- `analysis/analysis-api-fe10/tests-gen/org/jetbrains/kotlin/analysis/api/fe10/test/cases/generated/cases/components/symbolInfoProvider/Fe10IdeNormalAnalysisSourceModuleFunctionalInterfaceBySamConstructorTestGenerated.java` (JAVA) | Magnitude: 12.84 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 26, import: 16, decorators: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `kotlin-native/backend.native/compiler/ir/backend.native/src/org/jetbrains/kotlin/backend/konan/lower/ReturnsInsertionLowering.kt` (KOTLIN) | Magnitude: 31.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 22, import: 15, branch: 6
- `compiler/fir/checkers/src/org/jetbrains/kotlin/fir/analysis/checkers/FirMissingDependencySupertypeUtils.kt` (KOTLIN) | Magnitude: 18.5 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 15, import: 10, reflection_metaprogramming: 8
- `compiler/testData/codegen/box/binaryOp/divisionByZero.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, core_var_decl: 7, design_snake_case: 7, design_short_vars: 7
- `compiler/testData/codegen/box/functions/functionExpression/functionExpression.kt` (KOTLIN) | Magnitude: 0.01 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 16, panics_and_aborts: 14, branch: 11
- `libraries/scripting/jvm-host-test/test/kotlin/script/experimental/jvmhost/test/commonUtil.kt` (KOTLIN) | Magnitude: 17.58 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 10, branch: 5, core_var_decl: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `compiler/build-tools/kotlin-build-tools-api/src/main/kotlin/org/jetbrains/kotlin/buildtools/api/internal/wrappers/KotlinWrapperPre2_4_0.kt` -> Churn: **100.0%** | Cog Load: 22.3921% | Debt: 96.257%
- `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/main/main.kt` -> Churn: **88.56%** | Cog Load: 16.8888% | Debt: 95.4162%
- `native/swift/swift-export-standalone-integration-tests/coroutines/testData/generation/coroutines/golden_result/KotlinxCoroutinesCore/KotlinxCoroutinesCore.kt` -> Churn: **81.55%** | Cog Load: 46.1248% | Debt: 99.3683%
- `compiler/build-tools/kotlin-build-tools-api/gen/org/jetbrains/kotlin/buildtools/api/arguments/JvmCompilerArguments.kt` -> Churn: **73.25%** | Cog Load: 0.0% | Debt: 64.0359%
- `compiler/build-tools/kotlin-build-tools-compat/gen/org/jetbrains/kotlin/buildtools/internal/compat/arguments/CommonCompilerArgumentsImpl.kt` -> Churn: **73.25%** | Cog Load: 100.0% | Debt: 12.9704%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveCallTestGenerated.java` -> **Oleg Makeev** (100.0% isolated ownership) | Magnitude: 2776.4
- `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveCandidatesTestGenerated.java` -> **Oleg Makeev** (100.0% isolated ownership) | Magnitude: 2776.4
- `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveReferenceTestGenerated.java` -> **Oleg Makeev** (100.0% isolated ownership) | Magnitude: 2776.4
- `analysis/analysis-api-fir/tests-gen/org/jetbrains/kotlin/analysis/api/fir/test/cases/generated/cases/components/resolver/FirIdeNormalAnalysisSourceModuleResolveSymbolTestGenerated.java` -> **Oleg Makeev** (100.0% isolated ownership) | Magnitude: 2776.4
- `analysis/analysis-api-fe10/tests-gen/org/jetbrains/kotlin/analysis/api/fe10/test/cases/generated/cases/components/resolver/Fe10IdeNormalAnalysisSourceModuleResolveCallTestGenerated.java` -> **Oleg Makeev** (100.0% isolated ownership) | Magnitude: 2757.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `compiler/util-io/src/org/jetbrains/kotlin/konan/file/File.kt` -> **Severity: 799.0** (Blast Radius: 7.99 * Doc Risk: 100.0%)
- `core/compiler.common/src/org/jetbrains/kotlin/name/Name.java` -> **Severity: 438.0** (Blast Radius: 4.38 * Doc Risk: 100.0%)
- `compiler/util-io/src/org/jetbrains/kotlin/util/Util.kt` -> **Severity: 430.4** (Blast Radius: 4.304 * Doc Risk: 100.0%)
- `compiler/testData/codegen/box/evaluate/intrinsicConst/kCallableName.kt` -> **Severity: 282.8** (Blast Radius: 2.828 * Doc Risk: 100.0%)
- `compiler/build-tools/kotlin-build-tools-api-tests/src/main/kotlin/compilation/model/Project.kt` -> **Severity: 271.5** (Blast Radius: 2.715 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 9694 literal sites + 274 sites through wrappers = 9968
- **`memory_alloc`:** 4030 literal sites + 53 sites through wrappers = 4083
- **`panics_and_aborts`:** 140757 literal sites + 12415 sites through wrappers = 153172

- `errorWithAttachment` (function, panics_and_aborts, primitive): 163 call sites in 102 files -- `compiler/util/src/org/jetbrains/kotlin/utils/exceptions/ExceptionAttachmentBuilder.kt`
- `whileAnalysing` (function, panics_and_aborts, primitive): 96 call sites in 8 files -- `compiler/fir/tree/src/org/jetbrains/kotlin/fir/Utils.kt`
- `foo` (function, panics_and_aborts, primitive): 64 call sites in 1 files -- `compiler/testData/codegen/box/coroutines/suspendCallsInArguments.kt`
- `createCirTreeFromSourceCode` (function, panics_and_aborts, primitive): 55 call sites in 12 files -- `native/commonizer/tests/org/jetbrains/kotlin/commonizer/utils/InlineSourceBuilder.kt`
- `readInt` (function, panics_and_aborts, primitive): 54 call sites in 1 files -- `compiler/ir/backend.js/src/org/jetbrains/kotlin/ir/backend/js/utils/serialization/JsIrAstDeserializer.kt`
- `fetch64` (function, panics_and_aborts, primitive): 48 call sites in 1 files -- `compiler/ir/serialization.common/src/org/jetbrains/kotlin/backend/common/serialization/CityHash.kt`
- `createIrFile` (function, panics_and_aborts, primitive): 47 call sites in 1 files -- `compiler/ir/ir.validation/test/org/jetbrains/kotlin/ir/validation/IrValidatorTest.kt`
- `funWithReturnsFalse` (function, panics_and_aborts, primitive): 44 call sites in 16 files -- `compiler/tests-spec/testData/diagnostics/helpers/contractFunctions.kt`
- `substitutorByMap` (function, panics_and_aborts, primitive): 42 call sites in 36 files -- `compiler/fir/providers/src/org/jetbrains/kotlin/fir/resolve/substitution/ConeSubstitutorByMap.kt`
- `fibonacci` (function, panics_and_aborts, primitive): 41 call sites in 1 files -- `libraries/stdlib/test/collections/SequenceTest.kt`
- `shouldNotBeCalled` (function, panics_and_aborts, primitive): 39 call sites in 1 files -- `compiler/javac-wrapper/src/org/jetbrains/kotlin/javac/resolve/KotlinClassifiersCache.kt`
- `analyzeForTest` (function, panics_and_aborts, primitive): 38 call sites in 31 files -- `analysis/analysis-test-framework/testFixtures/org/jetbrains/kotlin/analysis/test/framework/base/AbstractAnalysisApiBasedTest.kt`
*(+6088 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 669414 call pairs -- scoped 36.5%, unique 1.2%, ambiguous 45.9%, external 16.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| kotlin | 518186 | 32.9% | 1.0% | 49.9% | 16.2% |
| java | 122029 | 54.4% | 0.3% | 36.1% | 9.1% |
| cpp | 13906 | 28.7% | 4.0% | 25.1% | 42.2% |
| swift | 7377 | 24.4% | 6.3% | 10.9% | 58.4% |
| objective-c | 3135 | 15.1% | 36.9% | 5.2% | 42.9% |
| c | 2622 | 7.9% | 6.9% | 0.3% | 85.0% |
| javascript | 745 | 47.7% | 0.0% | 6.6% | 45.8% |
| typescript | 536 | 19.0% | 0.0% | 16.4% | 64.6% |
| python | 409 | 24.9% | 0.0% | 1.0% | 74.1% |
| shell | 211 | 20.9% | 0.0% | 0.0% | 79.1% |

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
