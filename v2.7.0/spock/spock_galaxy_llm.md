# ARCHITECTURAL_BRIEF: spock
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/spockframework/spock` |
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
| Total Artifacts | 1420 |
| Analyzed Artifacts (Scanned) | 1251 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 169 |
| Total LOC | 68857 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 88.1% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.555 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1996 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6675 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 85 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 665 | 30931 | 53.2% |
| GROOVY | 525 | 37833 | 42.0% |
| PLAINTEXT | 46 | 1 | 3.7% |
| XML | 9 | 0 | 0.7% |
| BATCH | 2 | 74 | 0.2% |
| MARKDOWN | 1 | 0 | 0.1% |
| SHELL | 1 | 4 | 0.1% |
| JSON | 1 | 4 | 0.1% |
| YAML | 1 | 10 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1204 | 96.2% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 169*

**Composition by Extension & Reason:**
- `.groovy`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 16 exceeds 500 chars), 3x Excluded (Saturation: Line 7 exceeds 500 chars)
- `no_extension`: 13x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 249 LOC)
- `.adoc`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kts`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.java`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.imockmaker`: 2x Unsupported Format (.imockmaker)
- `.json5`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lines`: 1x Excluded (Unsupported Extension: '.lines')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.6 | 3.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 35.0 | 42.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.9 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 47.9 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 94.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.3 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 77.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1099 | 289 | 2 | `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` |
| cleanup | 35 | 13 | 0 | `spock-specs/src/test/groovy/org/spockframework/mock/runtime/mockito/MockitoStaticMocksSpec.groovy` |
| guards | 5080 | 635 | 10 | `spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java` |
| danger | 2974 | 522 | 6 | `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` |
| concurrency | 622 | 135 | 1 | `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` |
| connectivity | 4234 | 747 | 8 | `spock-core/src/main/java/org/spockframework/compiler/AstNodeCache.java` |
| io | 437 | 75 | 0 | `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirInterceptor.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 1 | 0 | `spock-core/src/main/java/org/spockframework/util/JavaProcessThreadDumpCollector.java` |
| time | 27 | 6 | 0 | `spock-core/src/main/java/spock/util/time/MutableClock.java` |
| serialization | 9 | 7 | 0 | `spock-core/src/main/java/org/spockframework/runtime/SpecRunHistory.java` |
| regex | 35 | 25 | 0 | `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java` |
| events | 17 | 4 | 0 | `spock-specs/src/test/groovy/spock/util/concurrent/PollingConditionsSpec.groovy` |
| tests | 5963 | 418 | 12 | `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` |
| docs | 1179 | 489 | 2 | `spock-core/src/main/java/spock/mock/MockingApi.java` |
| debt | 880 | 160 | 1 | `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` |
| mutation | 9728 | 802 | 21 | `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` |
| dead_code | 4065 | 807 | 8 | `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionEvaluation.groovy` |
| credential | 1 | 1 | 0 | `spock-specs/src/test/groovy/org/spockframework/util/ExceptionUtilSpec.groovy` |
| threat | 243 | 104 | 0 | `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovyMocksForGroovyClasses.groovy` |
| ml_ai | 85 | 26 | 0 | `spock-core/src/main/java/spock/config/ParallelConfiguration.java` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.2**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirInterceptor.java` (Hits: 39)
- `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` (Hits: 32)
- `spock-specs/src/test/groovy/org/spockframework/smoke/extension/TempDirExtensionSpec.groovy` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Specification.java** (`spock-core/src/main/java/spock/lang/Specification.java`) — 249 inbound connections
2. **EmbeddedSpecification.groovy** (`spock-specs/src/test/groovy/org/spockframework/EmbeddedSpecification.groovy`) — 97 inbound connections
3. **Issue.java** (`spock-core/src/main/java/spock/lang/Issue.java`) — 72 inbound connections
4. **GroovyRuntimeUtil.java** (`spock-core/src/main/java/org/spockframework/runtime/GroovyRuntimeUtil.java`) — 53 inbound connections
5. **Nullable.java** (`spock-core/src/main/java/org/spockframework/util/Nullable.java`) — 49 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ByteBuddyMockFactory.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/ByteBuddyMockFactory.java`) — 32 outbound dependencies
2. **MockMakerRegistry.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/MockMakerRegistry.java`) — 28 outbound dependencies
3. **MockitoMockMakerImpl.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/mockito/MockitoMockMakerImpl.java`) — 26 outbound dependencies
4. **SpockMockPostprocessor.java** (`spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java`) — 26 outbound dependencies
5. **ConditionRewriter.java** (`spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `register` (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> Impact: **166.0** | LOC: 632
- `filterForTags` (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> Impact: **102.0** | LOC: 136
  * *Intent:* /** * Filter the includee's text for the specified tags and push the result. * * @param document The currently rendered document * @param reader The c...
- `render` (@ `spock-core/src/main/java/org/spockframework/runtime/condition/EditPathRenderer.java`) -> Impact: **54.6** | LOC: 53
- `writeString` (@ `spock-core/src/main/java/org/spockframework/util/JsonWriter.java`) -> Impact: **53.2** | LOC: 74
- `respond` (@ `spock-core/src/main/java/org/spockframework/mock/EmptyOrDummyResponse.java`) -> Impact: **53.0** | LOC: 70
- `verify` (@ `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java`) -> Impact: **50.7** | LOC: 62
- `evaluateExpression` (@ `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/UnrollIterationNameProvider.java`) -> Impact: **48.5** | LOC: 50
- `intercept` (@ `spock-core/src/main/java/org/spockframework/runtime/extension/AbstractMethodInterceptor.java`) -> Impact: **41.7** | LOC: 43
- `processBlocks` (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> Impact: **34.4** | LOC: 133
- `verifyMethodCondition` (@ `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java`) -> Impact: **33.9** | LOC: 30
  * *Intent:* // method calls with spread-dot operator are not rewritten, hence this method doesn't have to care about spread-dot

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `config` | 1 | 5000.0 | 0.0% | 0.0% |
| `spock-core/src/main/java/org/spockframework/runtime` | 82 | 4755.28 | 21.49% | 36.81% |
| `spock-core/src/main/java/org/spockframework/compiler` | 26 | 3180.46 | 21.32% | 48.44% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/mock` | 62 | 2229.94 | 15.33% | 0.0% |
| `spock-core/src/main/java/org/spockframework/util` | 50 | 2132.24 | 11.92% | 18.77% |
| `spock-core/src/main/java/org/spockframework/mock/runtime` | 44 | 1766.5 | 22.84% | 43.44% |
| `spock-core/src/main/java/org/spockframework/runtime/extension/builtin` | 53 | 1669.3 | 17.28% | 14.37% |
| `spock-core/src/main/groovy/spock/util` | 3 | 1192.08 | 12.73% | 31.06% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/extension` | 37 | 1188.1 | 9.04% | 0.0% |
| `spock-core/src/main/java/org/spockframework/runtime/model` | 40 | 1183.6 | 7.73% | 25.87% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `spock-core/src/main/java/org/spockframework/buildsupport/SpecClassFileVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/AbstractSpecVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/model/BlockParseInfo.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/model/ISpecVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/mock/runtime/IMockMaker.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `spock-core/src/main/java/org/spockframework/runtime/FailedStringComparisonRenderer.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/runtime/SpecInfoBuilder.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/runtime/condition/EditPathRenderer.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/UnrollExtension.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/AbstractMultiset.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionEvaluation.groovy` -> **56** Orphaned Functions | **0** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionRendering.groovy` -> **53** Orphaned Functions | **0** Duplicates
- `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` -> **47** Orphaned Functions | **4** Duplicates
- `spock-core/src/main/java/org/spockframework/compiler/ExpressionReplacingVisitorSupport.java` -> **48** Orphaned Functions | **0** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/InvalidWhereBlocks.groovy` -> **48** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4648` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `spock-core/src/main/java/org/spockframework/runtime/ParameterizedFeatureChildExecutor.java` (JAVA) -> Cumulative Risk: **784.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 129.18 | **LOC:** 120 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9995%)
- **Heaviest Functions:** `ParameterizedFeatureChildExecutor` (Impact: 27.6), `executionFinished` (Impact: 14.7), `executionFinished` (Impact: 5.6)

### 2. `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` (JAVA) -> Cumulative Risk: **650.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 473.8 | **LOC:** 868 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.968%), Tech Debt (99.5713%), Documentation (98.0583%)
- **Heaviest Functions:** `rewriteCondition` (Impact: 15.2), `rewriteToSpockRuntimeCall` (Impact: 13.4), `surroundWithTryCatch` (Impact: 12.6)

### 3. `spock-core/src/main/java/org/spockframework/mock/runtime/MockInteraction.java` (JAVA) -> Cumulative Risk: **648.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 117.64 | **LOC:** 185 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.989%), Tech Debt (99.9698%)
- **Heaviest Functions:** `MockInteraction` (Impact: 12.2), `matchesTargetAndMethod` (Impact: 7.6), `computeSimilarityScore` (Impact: 6.7)

### 4. `spock-core/src/main/java/org/spockframework/compiler/SpecParser.java` (JAVA) -> Cumulative Risk: **636.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 198.72 | **LOC:** 300 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Safety Score (93.6368%)
- **Heaviest Functions:** `buildBlocks` (Impact: 17.9), `buildFixtureMethod` (Impact: 15.4), `addBlock` (Impact: 13.1)

### 5. `spock-core/src/main/java/org/spockframework/runtime/AsyncRunListener.java` (JAVA) -> Cumulative Risk: **632.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 79.1 | **LOC:** 112 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%)
- **Heaviest Functions:** `AsyncRunListener` (Impact: 6.1), `run` (Impact: 3.7), `addEvent` (Impact: 3.0)

### 6. `spock-core/src/main/java/org/spockframework/runtime/ExpressionInfoConverter.java` (JAVA) -> Cumulative Risk: **631.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 225.9 | **LOC:** 422 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9361%), State Flux (99.8907%)
- **Heaviest Functions:** `startOf` (Impact: 9.4), `visitTernaryExpression` (Impact: 6.3), `visitShortTernaryExpression` (Impact: 6.2)

### 7. `spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java` (JAVA) -> Cumulative Risk: **624.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 498.52 | **LOC:** 998 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8727%), Tech Debt (95.0417%), Safety Score (92.8594%)
- **Heaviest Functions:** `next` (Impact: 14.9), `createIterators` (Impact: 14.7), `haveNext` (Impact: 13.4)

### 8. `spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java` (JAVA) -> Cumulative Risk: **617.24**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 398.56 | **LOC:** 893 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8225%), Safety Score (89.6876%)
- **Heaviest Functions:** `visitMethodAgain` (Impact: 15.6), `visitCleanupBlock` (Impact: 11.8), `moveVariableDeclarations` (Impact: 9.8)

### 9. `spock-core/src/main/java/org/spockframework/compiler/ExpressionReplacingVisitorSupport.java` (JAVA) -> Cumulative Risk: **614.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 231.28 | **LOC:** 419 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9991%), State Flux (99.6401%), Documentation (98.1818%)
- **Heaviest Functions:** `replaceExpr` (Impact: 4.6), `visitArrayExpression` (Impact: 3.2), `replaceAllExprs` (Impact: 3.1)

### 10. `spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java` (JAVA) -> Cumulative Risk: **614.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 275.28 | **LOC:** 454 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8599%), Documentation (96.1538%), Safety Score (91.3384%)
- **Heaviest Functions:** `invoke` (Impact: 19.7), `runFeature` (Impact: 7.9), `doRunCleanup` (Impact: 7.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `config/code-signing-secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1009.68 | **LOC:** 1381 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.9458%), Tech Debt (93.183%)
**Top Internal Functions/Classes:**
  * `visitClass` (Impact: 27.2)
  * `visitAllImports` (Impact: 25.5)
  * `visitPropertyExpression` (Impact: 22.0)
  * `visitMethod` (Impact: 19.4)
  * `compileScript` (Impact: 18.9)
    * *Intent:* * * @param script * the source code to be compiled. If invalid, a compile error occurs * @param comp...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 71`, `args: 119`, `func_start: 114`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 34`, `duplicate_logic: 4`, `unreferenced_by_name: 47`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 23`, `doc: 15`, `sync_locks: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` groovy.transform.*, java.lang.reflect.Modifier, java.security.CodeSource, java.util.Collections.disjoint, org.apache.groovy.io.StringBuilderWriter, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 545.36 | **LOC:** 713 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.8123%), Tech Debt (38.8683%)
**Top Internal Functions/Classes:**
  * `register` (Impact: 166.0)
  * `filterForTags` (Impact: 102.0)
    * *Intent:* /** * Filter the includee's text for the specified tags and push the result. * * @param document The...
  * `processBlocks` (Impact: 34.4)
  * `filterForLines` (Impact: 20.4)
    * *Intent:* /** * Filter the includee's text for the specified line ranges and push the result. * * @param docum...
  * `determineTagsToFilterFor` (Impact: 18.8)
    * *Intent:* /** * Determine the tags to filter for from the attributes. * To be consistent with the Asciidoctor ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 72`, `args: 38`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 51`, `dead_code: 20`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 7`, `import: 16`
* *Defense:* `safety: 2`, `doc: 17`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.IOException, java.lang.Boolean.parseBoolean, java.lang.String.format, java.lang.String.join, java.nio.charset.StandardCharsets.UTF_8, java.nio.file.Files.readString, java.nio.file.Path, java.util.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 518.86 | **LOC:** 2144 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.9993%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `"Accessing real fields through global spy works like in reality"` (Impact: 8.5)
    * *Intent:* /** * This test should verify that the resolution logic around fields and properties * works identic...
  * `overwriteSuperField` (Impact: 3.3)
  * `"calls real method if mocked call provides no result"` (Impact: 2.6)
  * `"does not call real method if mocked call provides result"` (Impact: 2.6)
  * `"calls real method if call isn't mocked"` (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 171`, `args: 126`, `func_start: 126`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 280`, `duplicate_logic: 2`, `unreferenced_by_name: 24`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 4`, `doc: 1`, `test: 453`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` java.lang.reflect.Modifier, java.util.regex.Pattern, org.spockframework.runtime.GroovyRuntimeUtil, spock.lang.*, spock.util.environment.Jvm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 498.52 | **LOC:** 998 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.418%), Tech Debt (95.0417%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 14.9)
  * `createIterators` (Impact: 14.7)
  * `haveNext` (Impact: 13.4)
  * `getPreviousDataTableProviders` (Impact: 12.8)
  * `DataProviderMultiplier` (Impact: 12.7)
    * *Intent:* /** * Creates a new data provider multiplier that handles two sets of plain data providers as factor...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 187`, `args: 60`, `func_start: 58`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 86`, `dead_code: 2`, `duplicate_logic: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 52`, `import: 10`
* *Defense:* `safety: 39`, `doc: 18`, `immutability_locks: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.io.PrintWriter, java.io.StringWriter, java.util.*, java.util.Collections.emptyIterator, java.util.Collections.singletonList, java.util.stream.Collectors.toList, org.jetbrains.annotations.NotNull, org.spockframework.runtime.GroovyRuntimeUtil.closeQuietly...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 473.8 | **LOC:** 868 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4892%), Tech Debt (99.5713%)
**Top Internal Functions/Classes:**
  * `rewriteCondition` (Impact: 15.2)
  * `rewriteToSpockRuntimeCall` (Impact: 13.4)
  * `surroundWithTryCatch` (Impact: 12.6)
  * `extractVariableNumber` (Impact: 12.1)
    * *Intent:* // extractVariableNumber(record(expr)) == // extractVariableNumber($spock_valueRecorder.record($spoc...
  * `visitBinaryExpression` (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 228`, `args: 65`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 114`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 35`
* *Architecture:* `io: 11`, `api: 42`, `import: 23`
* *Defense:* `safety: 17`, `doc: 2`, `sync_locks: 31`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` java.lang.reflect.Constructor, java.lang.reflect.Method, java.util.ArrayList, java.util.Arrays.asList, java.util.Collections.singletonList, java.util.List, java.util.regex.Pattern, org.codehaus.groovy.ast.ClassNode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 416.78 | **LOC:** 984 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.6146%), Tech Debt (14.3725%)
**Top Internal Functions/Classes:**
  * `rewriteBinaryWhereStat` (Impact: 23.7)
  * `rewriteTableLikeParameterization` (Impact: 17.7)
  * `rewriteMultiParameterization` (Impact: 14.9)
  * `turnIntoSimpleParameterization` (Impact: 14.5)
  * `verifyDerivedDataVariableIsNotCombined` (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 217`, `args: 83`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 58`, `dead_code: 10`, `duplicate_logic: 2`
* *Architecture:* `io: 32`, `api: 8`, `import: 13`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.lang.Boolean.FALSE, java.lang.Boolean.TRUE, java.util.*, java.util.function.Function, java.util.function.Function.identity, java.util.stream.Collectors, java.util.stream.Collectors.*, org.codehaus.groovy.ast.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 398.56 | **LOC:** 893 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.9649%), Tech Debt (72.9319%)
**Top Internal Functions/Classes:**
  * `visitMethodAgain` (Impact: 15.6)
  * `visitCleanupBlock` (Impact: 11.8)
    * *Intent:* */
  * `moveVariableDeclarations` (Impact: 9.8)
    * *Intent:* /* * Moves variable declarations from one statement list to another. Initializer * expressions are k...
  * `transformRhsExpressionIfNecessary` (Impact: 9.6)
  * `moveInteractions` (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 222`, `args: 64`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 75`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 14`
* *Architecture:* `io: 17`, `api: 21`, `import: 16`
* *Defense:* `safety: 15`, `doc: 1`, `sync_locks: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` java.lang.reflect.InvocationTargetException, java.util.*, java.util.Arrays.asList, java.util.Collections.singletonList, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.*, org.codehaus.groovy.syntax.Token...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 389.38 | **LOC:** 354 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.8446%), Tech Debt (64.309%)
**Top Internal Functions/Classes:**
  * `createMockImpl` (Impact: 25.7)
  * `thrownImpl` (Impact: 11.3)
  * `checkExceptionThrown` (Impact: 11.2)
  * `GroovySpyImpl` (Impact: 10.2)
  * `createMock` (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 104`, `args: 65`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 1`, `planned_debt: 16`
* *Architecture:* `api: 59`, `import: 10`
* *Defense:* `doc: 1`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0018
  * `Imports (Out-Degree: 2):` groovy.lang.Closure, groovy.transform.stc.ClosureParams, groovy.transform.stc.SecondParam, groovy.transform.stc.ThirdParam, java.lang.reflect.Type, java.util.*, java.util.Collections.emptyMap, java.util.Collections.singletonMap...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 310.82 | **LOC:** 448 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (27.5506%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `verify` (Impact: 50.7)
  * `verifyMethodCondition` (Impact: 33.9)
    * *Intent:* // method calls with spread-dot operator are not rewritten, hence this method doesn't have to care a...
  * `conditionFailedWithException` (Impact: 24.0)
  * `parse` (Impact: 16.5)
  * `verify` (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 109`, `args: 32`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 22`, `dead_code: 1`
* *Architecture:* `api: 21`, `import: 24`
* *Defense:* `safety: 9`, `doc: 2`, `test: 4`, `sync_locks: 13`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` groovy.lang.Closure, groovy.lang.DelegatesTo, groovy.transform.stc.ClosureParams, groovy.transform.stc.FromString, java.util.*, java.util.function.Consumer, java.util.function.Function, java.util.stream.Collectors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/util/ReflectionUtil.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 305.34 | **LOC:** 417 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.0152%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDefaultValue` (Impact: 27.7)
  * `isClassVisibleInClassloader` (Impact: 11.3)
    * *Intent:* /** * Checks if the {@code classToCheck} is visible by the passed {@code classLoader} * * @param cla...
  * `hasAnyOfTypes` (Impact: 10.7)
  * `hasValidArguments` (Impact: 9.2)
  * `getMethodByName` (Impact: 9.1)
    * *Intent:* /** * Finds a public method with the given name declared in the given * class/interface or one of it...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 120`, `args: 46`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 10`, `dead_code: 1`
* *Architecture:* `io: 7`, `api: 37`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 30`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025179
  * `Imports (Out-Degree: 0):` java.io.File, java.io.IOException, java.lang.annotation.Annotation, java.lang.reflect.*, java.net.URL, java.security.CodeSource, java.util.*, java.util.Arrays.asList...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 275.28 | **LOC:** 454 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.7041%), Tech Debt (36.5832%)
**Top Internal Functions/Classes:**
  * `invoke` (Impact: 19.7)
  * `runFeature` (Impact: 7.9)
  * `doRunCleanup` (Impact: 7.4)
  * `doRunSetupSpec` (Impact: 7.3)
  * `doRunSetup` (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 105`, `args: 64`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 46`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.lang.System.arraycopy, java.util.Arrays, java.util.Arrays.copyOfRange, java.util.Collections, java.util.List, org.spockframework.runtime.extension.IMethodInterceptor, org.spockframework.runtime.extension.MethodInvocation, org.spockframework.runtime.model.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 252.86 | **LOC:** 422 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.2012%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isInitializerOrFixtureMethod` (Impact: 9.2)
  * `collectAll` (Impact: 6.5)
  * `filterFeatures` (Impact: 6.0)
  * `toFeatureName` (Impact: 6.0)
  * `collectSpecHierarchy` (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 111`, `args: 90`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 32`
* *Architecture:* `api: 70`, `import: 13`
* *Defense:* `doc: 1`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.121
  * `Choke Point (Betweenness):` 0.004675 | `Ripple Effect (Closeness):` 0.114779
  * `Imports (Out-Degree: 9):` java.util.*, java.util.Comparator.comparingInt, java.util.function.BiConsumer, java.util.function.Function, java.util.function.Supplier, org.spockframework.runtime.IFeatureFilter, org.spockframework.runtime.IFeatureSortOrder, org.spockframework.runtime.IMethodNameMapper...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 235.1 | **LOC:** 402 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.412%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAnnotation` (Impact: 10.9)
  * `toArgumentArray` (Impact: 10.1)
    * *Intent:* /** * Turns an argument list obtained from AstUtil.getArguments() into an Object[] array * suitable ...
  * `getInvocationTarget` (Impact: 7.6)
  * `getAssertionMessage` (Impact: 7.4)
  * `isDynamicTypedExpression` (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 122`, `args: 42`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 21`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 40`, `import: 9`
* *Defense:* `safety: 27`, `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.972
  * `Choke Point (Betweenness):` 0.000316 | `Ripple Effect (Closeness):` 0.091129
  * `Imports (Out-Degree: 2):` java.util.*, java.util.Collections.emptyList, java.util.Collections.singletonList, java.util.regex.Pattern, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.*, org.codehaus.groovy.runtime.dgmimpl.arrays.IntegerArrayGetAtMetaMethod...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/ExpressionReplacingVisitorSupport.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 231.28 | **LOC:** 419 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.8188%), Tech Debt (99.9991%)
**Top Internal Functions/Classes:**
  * `replaceExpr` (Impact: 4.6)
  * `visitArrayExpression` (Impact: 3.2)
  * `replaceAllExprs` (Impact: 3.1)
  * `visitPropertyExpression` (Impact: 2.1)
  * `visitRangeExpression` (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 81`, `args: 55`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 64`, `unreferenced_by_name: 48`
* *Architecture:* `api: 56`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ListIterator, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.*, org.codehaus.groovy.classgen.BytecodeExpression
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/ExpressionInfoConverter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 225.9 | **LOC:** 422 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.9108%), Tech Debt (99.9361%)
**Top Internal Functions/Classes:**
  * `startOf` (Impact: 9.4)
    * *Intent:* // searches for token backwards from beginning of node (exclusive) // IDEA: move to class TextPositi...
  * `visitTernaryExpression` (Impact: 6.3)
  * `visitShortTernaryExpression` (Impact: 6.2)
  * `visitBinaryExpression` (Impact: 4.8)
  * `visitPropertyExpression` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 89`, `args: 44`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 52`, `unreferenced_by_name: 34`
* *Architecture:* `api: 39`, `import: 14`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.util.ArrayList, java.util.Arrays, java.util.Arrays.asList, java.util.Collections.emptyList, java.util.Collections.singletonList, java.util.List, org.codehaus.groovy.ast.ASTNode, org.codehaus.groovy.ast.expr.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 200.18 | **LOC:** 411 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.7246%), Tech Debt (8.8223%)
**Top Internal Functions/Classes:**
  * `determinePrimaryCandidate` (Impact: 12.8)
  * `getBeanName` (Impact: 12.3)
  * `registerSpy` (Impact: 10.6)
  * `register` (Impact: 8.4)
  * `getExistingBeans` (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 101`, `args: 32`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 18`, `planned_debt: 1`
* *Architecture:* `api: 8`, `import: 24`
* *Defense:* `safety: 8`, `doc: 6`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.502
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0008
  * `Imports (Out-Degree: 5):` java.util.*, java.util.Arrays.asList, java.util.concurrent.ConcurrentHashMap, org.spockframework.runtime.model.FieldInfo, org.spockframework.spring.SpringBean, org.spockframework.spring.SpringExtensionException, org.spockframework.spring.SpringSpy, org.springframework.aop.scope.ScopedProxyUtils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/SpecParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 198.72 | **LOC:** 300 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.3136%), Tech Debt (63.6736%)
**Top Internal Functions/Classes:**
  * `buildBlocks` (Impact: 17.9)
  * `buildFixtureMethod` (Impact: 15.4)
  * `addBlock` (Impact: 13.1)
  * `visitMethod` (Impact: 11.9)
  * `isFixtureMethod` (Impact: 9.4)
    * *Intent:* // IDEA: check for misspellings other than wrong capitalization
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 67`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 31`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 8`, `api: 8`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.List, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.ConstantExpression, org.codehaus.groovy.ast.stmt.Statement, org.spockframework.compiler.AstUtil.hasAnnotation, org.spockframework.compiler.model.*, org.spockframework.util.Identifiers.*, spock.lang.Shared...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/DeepBlockRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 189.5 | **LOC:** 370 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.9139%), Tech Debt (33.5856%)
**Top Internal Functions/Classes:**
  * `handleImplicitCondition` (Impact: 13.2)
  * `doVisitBinaryExpression` (Impact: 11.3)
  * `handleThrownCall` (Impact: 9.6)
  * `handleInteraction` (Impact: 8.0)
  * `handleImplicitCallOnMethodParam` (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 70`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 22`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 10`, `import: 10`
* *Defense:* `safety: 13`, `doc: 1`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.List, org.codehaus.groovy.ast.Parameter, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.expr.MethodCallExpression.NO_ARGUMENTS, org.codehaus.groovy.ast.stmt.AssertStatement, org.codehaus.groovy.ast.stmt.ExpressionStatement, org.codehaus.groovy.ast.stmt.Statement, org.codehaus.groovy.syntax.Types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/model/FeatureInfo.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 182.3 | **LOC:** 445 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.3522%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hasBytecodeName` (Impact: 11.8)
    * *Intent:* /** * Tells if any of the methods associated with this feature has the specified * name in bytecode....
  * `addImpliedFeature` (Impact: 7.8)
    * *Intent:* /** * Adds the given feature as implied by this feature. * The given feature must be within the same...
  * `addScopedMethodInterceptor` (Impact: 3.9)
    * *Intent:* * featureInfo.addScopedMethodInterceptor(featureInfo.getParent().getInitializerMethod(), invocation ...
  * `setDeclarationOrder` (Impact: 1.6)
  * `setExecutionOrder` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 91`, `args: 56`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 26`
* *Architecture:* `api: 55`, `import: 9`
* *Defense:* `doc: 16`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.706
  * `Choke Point (Betweenness):` 0.003977 | `Ripple Effect (Closeness):` 0.11592
  * `Imports (Out-Degree: 8):` java.lang.reflect.AnnotatedElement, java.util.*, org.spockframework.runtime.extension.IBlockListener, org.spockframework.runtime.extension.IDataDriver, org.spockframework.runtime.extension.IMethodInterceptor, org.spockframework.runtime.model.parallel.ExclusiveResource, org.spockframework.runtime.model.parallel.ExecutionMode, org.spockframework.util.Beta...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/util/TeePrintStream.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 174.66 | **LOC:** 353 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.4916%), Tech Debt (78.9089%)
**Top Internal Functions/Classes:**
  * `clearError` (Impact: 4.7)
  * `printf` (Impact: 4.4)
  * `format` (Impact: 4.4)
  * `append` (Impact: 4.4)
  * `write` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 52`, `args: 44`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 11`
* *Architecture:* `api: 44`, `import: 4`
* *Defense:* `safety: 2`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` groovy.lang.MissingMethodException, java.io.*, java.util.*, java.util.Arrays.asList, java.util.concurrent.CopyOnWriteArrayList, org.spockframework.runtime.GroovyRuntimeUtil
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/mock/runtime/InteractionBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 170.94 | **LOC:** 201 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.9659%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setRangeCount` (Impact: 12.3)
  * `addEqualArg` (Impact: 7.4)
  * `convertCount` (Impact: 7.4)
  * `setArgListKind` (Impact: 5.7)
  * `setFixedCount` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 54`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`
* *Architecture:* `api: 39`, `import: 2`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` groovy.lang.Closure, java.util.*, org.spockframework.lang.*, org.spockframework.mock.*, org.spockframework.mock.constraint.*, org.spockframework.mock.response.*, org.spockframework.runtime.InvalidSpecException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/InteractionRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 169.58 | **LOC:** 396 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.6946%), Tech Debt (15.1684%)
**Top Internal Functions/Classes:**
  * `parseCall` (Impact: 13.3)
  * `setCall` (Impact: 12.1)
  * `addArgs` (Impact: 10.8)
  * `addArg` (Impact: 9.9)
  * `selectNameConstraint` (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 79`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 25`, `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.*, java.util.Arrays.asList, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.ExpressionStatement, org.codehaus.groovy.syntax.Types, org.spockframework.compiler.AstUtil.createDirectMethodCall, org.spockframework.compiler.AstUtil.primitiveConstExpression...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/SpecInfoBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 166.76 | **LOC:** 238 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.8294%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createFeature` (Impact: 23.8)
  * `findMethod` (Impact: 5.8)
  * `build` (Impact: 5.6)
  * `buildFixtureMethods` (Impact: 5.5)
  * `buildFields` (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 45`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 49`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.808
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0032
  * `Imports (Out-Degree: 1):` java.lang.reflect.*, java.util.*, java.util.Arrays.asList, java.util.Comparator.comparingInt, java.util.stream.Collectors, org.spockframework.runtime.model.*, org.spockframework.util.*, spock.lang.Specification
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/util/inspector/AstInspector.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 166.1 | **LOC:** 531 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1393%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `visitAnnotations` (Impact: 8.0)
  * `visitConstructorOrMethod` (Impact: 7.4)
  * `getExpressions` (Impact: 6.0)
  * `indexAstNodes` (Impact: 5.5)
  * `visitStatement` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 101`, `args: 44`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 16`
* *Architecture:* `io: 12`, `api: 36`, `import: 14`
* *Defense:* `safety: 8`, `doc: 23`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.501
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.0056
  * `Imports (Out-Degree: 1):` groovy.lang.GroovyClassLoader, java.io.File, java.io.IOException, java.security.CodeSource, java.util.ArrayList, java.util.Collections.emptyList, java.util.HashMap, java.util.List...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 518.86
- `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 416.78
- `spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 398.56
- `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 389.38
- `spock-core/src/main/java/org/spockframework/compiler/SpecParser.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 198.72

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `spock-core/src/main/java/spock/lang/Specification.java` -> **Severity: 0.481** (Bridge: 0.0109 * Flux: 44.2886%)
- `spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java` -> **Severity: 0.445** (Bridge: 0.0047 * Flux: 95.108%)
- `spock-core/src/main/java/org/spockframework/runtime/model/FeatureInfo.java` -> **Severity: 0.311** (Bridge: 0.004 * Flux: 78.1336%)
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/StepwiseExtension.java` -> **Severity: 0.101** (Bridge: 0.001 * Flux: 99.6316%)
- `spock-core/src/main/java/org/spockframework/runtime/model/MethodInfo.java` -> **Severity: 0.067** (Bridge: 0.0007 * Flux: 99.9972%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `spock-core/src/main/java/spock/lang/Specification.java` -> **Severity: 17.787** (Embedded: 0.2058 * Error Risk: 86.4403%)
- `spock-core/src/main/java/org/spockframework/util/ExceptionUtil.java` -> **Severity: 11.266** (Embedded: 0.1398 * Error Risk: 80.5786%)
- `spock-core/src/main/java/org/spockframework/util/ObjectUtil.java` -> **Severity: 10.136** (Embedded: 0.1035 * Error Risk: 97.8959%)
- `spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java` -> **Severity: 9.462** (Embedded: 0.1148 * Error Risk: 82.4327%)
- `spock-core/src/main/java/org/spockframework/runtime/GroovyRuntimeUtil.java` -> **Severity: 8.992** (Embedded: 0.122 * Error Risk: 73.6893%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `spock-core/src/main/java/org/spockframework/lang/Wildcard.java` -> **Severity: 1612.3** (Blast Radius: 16.123 * Doc Risk: 100.0%)
- `spock-specs/src/test/groovy/org/spockframework/EmbeddedSpecification.groovy` -> **Severity: 1511.5** (Blast Radius: 15.115 * Doc Risk: 100.0%)
- `spock-core/src/main/java/org/spockframework/lang/ISpecificationContext.java` -> **Severity: 1198.2** (Blast Radius: 11.982 * Doc Risk: 100.0%)
- `spock-core/src/main/java/org/spockframework/util/ExceptionUtil.java` -> **Severity: 1091.2** (Blast Radius: 13.64 * Doc Risk: 80.0%)
- `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` -> **Severity: 764.282** (Blast Radius: 8.972 * Doc Risk: 85.1852%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
