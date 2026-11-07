# ARCHITECTURAL_BRIEF: spock
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/spockframework/spock` |
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
- **Scope:** 1301 analyzed artifact(s), 71622 LOC.
- **Load-bearing artifact:** `spock-core/src/main/java/spock/lang/Specification.java` -- 247 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `spock-core/src/main/java/org/spockframework/mock/runtime/ByteBuddyMockFactory.java` -- pulls in 32 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `config/code-signing-secring.gpg` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 1420 |
| Analyzed Artifacts (Scanned) | 1301 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 119 |
| Total LOC | 71622 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 91.6% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5958 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2069 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.1981 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 101 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 665 | 30931 | 51.1% |
| GROOVY | 557 | 39240 | 42.8% |
| PLAINTEXT | 45 | 1 | 3.5% |
| YAML | 11 | 607 | 0.8% |
| XML | 9 | 0 | 0.7% |
| KOTLIN | 5 | 616 | 0.4% |
| MARKDOWN | 3 | 0 | 0.2% |
| JSON | 2 | 47 | 0.2% |
| SHELL | 2 | 106 | 0.2% |
| BATCH | 2 | 74 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1300 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 15%, State Mutators Files 15%, Interface Declarations Files 12%, Declarative / Non-Code 12%, Encapsulated Accessors Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1253 | 96.3% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 47 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 119*

**Composition by Extension & Reason:**
- `.groovy`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 12x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unresolved Ambiguity (No Retainable Structure)
- `.adoc`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.java`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.imockmaker`: 2x Unsupported Format (.imockmaker)
- `.lines`: 1x Excluded (Unsupported Extension: '.lines')
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.jar`: 1x Excluded (Explicitly Denied Extension: '.jar')
- `.testengine`: 1x Unsupported Format (.testengine)
- `.dsld`: 1x Unsupported Format (.dsld)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.9 | 31.7 | 45.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.2 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 76.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1103 | 291 | 2 | `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` |
| cleanup | 35 | 13 | 0 | `spock-specs/src/test/groovy/org/spockframework/mock/runtime/mockito/MockitoStaticMocksSpec.groovy` |
| guards | 5241 | 656 | 10 | `spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java` |
| danger | 3107 | 547 | 6 | `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` |
| concurrency | 626 | 139 | 1 | `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` |
| connectivity | 4272 | 768 | 8 | `spock-core/src/main/java/org/spockframework/compiler/AstNodeCache.java` |
| io | 484 | 77 | 0 | `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirInterceptor.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 2 | 0 | `gradlew` |
| time | 27 | 6 | 0 | `spock-core/src/main/java/spock/util/time/MutableClock.java` |
| serialization | 9 | 7 | 0 | `spock-core/src/main/java/org/spockframework/runtime/SpecRunHistory.java` |
| regex | 52 | 30 | 0 | `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java` |
| events | 19 | 5 | 0 | `spock-specs/src/test/groovy/spock/util/concurrent/PollingConditionsSpec.groovy` |
| tests | 5963 | 418 | 12 | `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` |
| docs | 1266 | 499 | 2 | `spock-core/src/main/java/spock/mock/MockingApi.java` |
| debt | 898 | 164 | 1 | `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` |
| mutation | 10274 | 830 | 21 | `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` |
| dead_code | 4176 | 854 | 8 | `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionEvaluation.groovy` |
| credential | 1 | 1 | 0 | `spock-specs/src/test/groovy/org/spockframework/util/ExceptionUtilSpec.groovy` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 87 | 27 | 0 | `spock-core/src/main/java/spock/config/ParallelConfiguration.java` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1154**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirInterceptor.java` (Hits: 39)
- `spock-specs/src/test/groovy/org/spockframework/smoke/extension/TempDirExtensionSpec.groovy` (Hits: 32)
- `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Specification.java** (`spock-core/src/main/java/spock/lang/Specification.java`) — 247 inbound connections
2. **EmbeddedSpecification.groovy** (`spock-specs/src/test/groovy/org/spockframework/EmbeddedSpecification.groovy`) — 97 inbound connections
3. **Issue.java** (`spock-core/src/main/java/spock/lang/Issue.java`) — 72 inbound connections
4. **SpockRuntime.java** (`spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java`) — 65 inbound connections
5. **GroovyRuntimeUtil.java** (`spock-core/src/main/java/org/spockframework/runtime/GroovyRuntimeUtil.java`) — 63 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ByteBuddyMockFactory.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/ByteBuddyMockFactory.java`) — 32 outbound dependencies
2. **MockMakerRegistry.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/MockMakerRegistry.java`) — 28 outbound dependencies
3. **MockitoMockMakerImpl.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/mockito/MockitoMockMakerImpl.java`) — 26 outbound dependencies
4. **SpockMockPostprocessor.java** (`spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java`) — 26 outbound dependencies
5. **ConditionRewriter.java** (`spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `register` **(Stateful Encapsulated Methods)** (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> Impact: **132.0** | LOC: 632
- `filterForTags` **(Many-Argument Workhorses)** (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> Impact: **88.8** | LOC: 136
  * *Intent:* /** * Filter the includee's text for the specified tags and push the result. * * @param document The currently rendered document * @param reader The c...
- `respond` **(Compute Cores)** (@ `spock-core/src/main/java/org/spockframework/mock/EmptyOrDummyResponse.java`) -> Impact: **50.2** | LOC: 70
- `verify` **(Many-Argument Workhorses)** (@ `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java`) -> Impact: **40.1** | LOC: 62
- `writeString` **(Compute Cores)** (@ `spock-core/src/main/java/org/spockframework/util/JsonWriter.java`) -> Impact: **39.1** | LOC: 74
- `render` **(Many-Argument Workhorses)** (@ `spock-core/src/main/java/org/spockframework/runtime/condition/EditPathRenderer.java`) -> Impact: **38.6** | LOC: 53
- `verifyMethodCondition` **(Many-Argument Workhorses)** (@ `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java`) -> Impact: **30.3** | LOC: 30
  * *Intent:* // method calls with spread-dot operator are not rewritten, hence this method doesn't have to care about spread-dot
- `evaluateExpression` **(Many-Argument Workhorses)** (@ `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/UnrollIterationNameProvider.java`) -> Impact: **28.5** | LOC: 50
- `visitClass` **(Callbacks & Closures)** (@ `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy`) -> Impact: **27.2** | LOC: 63
- `getDefaultValue` **(Defensive Guards)** (@ `spock-core/src/main/java/org/spockframework/util/ReflectionUtil.java`) -> Impact: **26.3** | LOC: 16

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `config` | 1 | 5000.0 | 0.0% | 0.0% |
| `spock-core/src/main/java/org/spockframework/runtime` | 82 | 4147.98 | 18.38% | 46.32% |
| `spock-core/src/main/java/org/spockframework/compiler` | 26 | 3034.26 | 19.79% | 48.44% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/mock` | 62 | 2206.44 | 14.66% | 0.0% |
| `spock-core/src/main/java/org/spockframework/util` | 50 | 1914.54 | 9.96% | 20.41% |
| `spock-core/src/main/java/org/spockframework/mock/runtime` | 44 | 1578.9 | 19.99% | 46.35% |
| `spock-core/src/main/java/org/spockframework/runtime/extension/builtin` | 53 | 1483.3 | 14.69% | 18.69% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/extension` | 37 | 1178.1 | 8.65% | 0.0% |
| `spock-core/src/main/groovy/spock/util` | 3 | 1168.08 | 12.49% | 30.92% |
| `spock-core/src/main/java/org/spockframework/runtime/model` | 40 | 1149.6 | 6.7% | 29.32% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `spock-core/src/main/java/org/spockframework/buildsupport/SpecClassFileVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/AbstractSpecVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/model/BlockParseInfo.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/model/ISpecVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/mock/runtime/IMockMaker.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `gradlew` -> **100.0%** Exposure
- `spock-specs/src/test/groovy/org/spockframework/util/AbstractMultisetSpec.groovy` -> **100.0%** Exposure
- `spock-specs/src/test/groovy/spock/util/concurrent/BlockingVariablesSpec.groovy` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/runtime/FailedStringComparisonRenderer.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/runtime/SpecInfoBuilder.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionEvaluation.groovy` -> **56** Orphaned Functions | **0** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionRendering.groovy` -> **53** Orphaned Functions | **0** Duplicates
- `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` -> **47** Orphaned Functions | **4** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/InvalidWhereBlocks.groovy` -> **48** Orphaned Functions | **0** Duplicates
- `spock-core/src/main/java/org/spockframework/compiler/ExpressionReplacingVisitorSupport.java` -> **48** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `4677` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `config/code-signing-secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.112)
- **Top Global Matches:** file_cluster_12: 8.112, file_cluster_15: 9.204, file_cluster_16: 9.299
- **Magnitude:** 985.68 | **LOC:** 1381 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 0.77; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (92.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.3%), Guard Balance (formerly Safety Score) (52.9%)
- **Documentation Coverage:** 97.037% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitClass` **(Callbacks & Closures)** (Impact: 27.2)
  * `visitAllImports` **(Stateful Encapsulated Methods)** (Impact: 25.5)
  * `visitPropertyExpression` **(Defensive Guards)** (Impact: 20.6)
  * `visitMethod` **(I/O & Config Routines)** (Impact: 19.4)
  * `call` **(Compute Cores)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 336`, `structural_boundaries: 71`, `args: 119`, `func_start: 114`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 34`, `duplicate_logic: 4`, `unreferenced_by_name: 47`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 23`, `doc: 15`, `sync_locks: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.77
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.004919
  * `Imports (Out-Degree: 2):` groovy.transform.*, java.lang.reflect.Modifier, java.security.CodeSource, java.util.Collections.disjoint, org.apache.groovy.io.StringBuilderWriter, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.*...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.064)
- **Top Global Matches:** file_cluster_11: 8.064, file_cluster_15: 8.256, file_cluster_12: 8.739
- **Magnitude:** 518.86 | **LOC:** 2144 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.342; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.5%), Complexity Load (formerly Cognitive Load) (38.0%), Connectivity (formerly Api Exposure) (1.5%)
- **Documentation Coverage:** 99.2248% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `"Accessing real fields through global spy works like in reality"` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* /** * This test should verify that the resolution logic around fields and properties * works identic...
  * `overwriteSuperField` **(Parameter Forwarders)** (Impact: 3.3)
  * `"calls real method if mocked call provides no result"` **(I/O & Config Routines)** (Impact: 2.6)
  * `"does not call real method if mocked call provides result"` **(I/O & Config Routines)** (Impact: 2.6)
  * `"calls real method if call isn't mocked"` **(Interface Declarations)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 171`, `args: 126`, `func_start: 126`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 280`, `duplicate_logic: 2`, `unreferenced_by_name: 24`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 4`, `doc: 1`, `test: 453`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` java.lang.reflect.Modifier, java.util.regex.Pattern, org.spockframework.runtime.GroovyRuntimeUtil, spock.lang.*, spock.util.environment.Jvm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.815)
- **Top Global Matches:** file_cluster_4: 10.815, file_cluster_6: 11.937, file_cluster_5: 13.632
- **Magnitude:** 474.16 | **LOC:** 713 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.633; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.4%), Complexity Load (formerly Cognitive Load) (50.2%)
- **Documentation Coverage:** 48.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `register` **(Stateful Encapsulated Methods)** (Impact: 132.0)
  * `filterForTags` **(Many-Argument Workhorses)** (Impact: 88.8)
    * *Intent:* /** * Filter the includee's text for the specified tags and push the result. * * @param document The...
  * `processBlocks` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `filterForLines` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* /** * Filter the includee's text for the specified line ranges and push the result. * * @param docum...
  * `determineTagsToFilterFor` **(Stateful Encapsulated Methods)** (Impact: 18.8)
    * *Intent:* /** * Determine the tags to filter for from the attributes. * To be consistent with the Asciidoctor ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 72`, `args: 38`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 51`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 7`, `import: 16`
* *Defense:* `safety: 2`, `doc: 17`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000769
  * `Imports (Out-Degree: 0):` java.io.IOException, java.lang.Boolean.parseBoolean, java.lang.String.format, java.lang.String.join, java.nio.charset.StandardCharsets.UTF_8, java.nio.file.Files.readString, java.nio.file.Path, java.util.*...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.187)
- **Top Global Matches:** file_cluster_5: 7.187, file_cluster_7: 9.597, file_cluster_12: 9.954
- **Magnitude:** 463.72 | **LOC:** 998 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (95.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `next` **(I/O & Config Routines)** (Impact: 14.9)
  * `haveNext` **(Stateful Encapsulated Methods)** (Impact: 11.6)
  * `createDataProviderIterators` **(I/O & Config Routines)** (Impact: 11.6)
  * `estimateNumIterations` **(Stateful Encapsulated Methods)** (Impact: 11.5)
  * `DataProviderMultiplier` **(Many-Argument Workhorses)** (Impact: 9.9)
    * *Intent:* /** * Creates a new data provider multiplier that handles two sets of plain data providers as factor...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 187`, `args: 60`, `func_start: 58`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 86`, `duplicate_logic: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 52`, `import: 10`
* *Defense:* `safety: 39`, `doc: 18`, `immutability_locks: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.017369
  * `Imports (Out-Degree: 16):` java.io.PrintWriter, java.io.StringWriter, java.util.*, java.util.Collections.emptyIterator, java.util.Collections.singletonList, java.util.stream.Collectors.toList, org.jetbrains.annotations.NotNull, org.spockframework.runtime.GroovyRuntimeUtil.closeQuietly...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.305)
- **Top Global Matches:** file_cluster_5: 7.305, file_cluster_12: 7.412, file_cluster_7: 8.405
- **Magnitude:** 441.0 | **LOC:** 868 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.382; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.8%)
- **Documentation Coverage:** 98.0583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rewriteCondition` **(Stateful Encapsulated Methods)** (Impact: 15.2)
  * `extractVariableNumber` **(Type Conversions)** (Impact: 12.1)
    * *Intent:* // extractVariableNumber(record(expr)) == // extractVariableNumber($spock_valueRecorder.record($spoc...
  * `rewriteToSpockRuntimeCall` **(Stateful Encapsulated Methods)** (Impact: 8.5)
  * `rewriteStaticMethodCondition` **(Stateful Encapsulated Methods)** (Impact: 8.4)
  * `rewriteMethodCondition` **(Stateful Encapsulated Methods)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 228`, `args: 65`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 114`, `planned_debt: 1`, `unreferenced_by_name: 35`
* *Architecture:* `io: 11`, `api: 42`, `import: 23`
* *Defense:* `safety: 17`, `doc: 2`, `sync_locks: 31`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.382
  * `Choke Point (Betweenness):` 0.001768 | `Ripple Effect (Closeness):` 0.068336
  * `Imports (Out-Degree: 11):` java.lang.reflect.Constructor, java.lang.reflect.Method, java.util.ArrayList, java.util.Arrays.asList, java.util.Collections.singletonList, java.util.List, java.util.regex.Pattern, org.codehaus.groovy.ast.ClassNode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.283)
- **Top Global Matches:** file_cluster_5: 6.283, file_cluster_12: 8.222, file_cluster_7: 10.071
- **Magnitude:** 401.98 | **LOC:** 984 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.401; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (27.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rewriteBinaryWhereStat` **(Defensive Guards)** (Impact: 23.7)
  * `rewriteTableLikeParameterization` **(Stateful Encapsulated Methods)** (Impact: 16.0)
  * `rewriteMultiParameterization` **(Stateful Encapsulated Methods)** (Impact: 14.9)
  * `turnIntoSimpleParameterization` **(Compute Cores)** (Impact: 14.5)
  * `verifyDerivedDataVariableIsNotCombined` **(Stateful Encapsulated Methods)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 217`, `args: 83`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 58`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 32`, `api: 8`, `import: 13`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.401
  * `Choke Point (Betweenness):` 0.002054 | `Ripple Effect (Closeness):` 0.078048
  * `Imports (Out-Degree: 15):` java.lang.Boolean.FALSE, java.lang.Boolean.TRUE, java.util.*, java.util.function.Function, java.util.function.Function.identity, java.util.stream.Collectors, java.util.stream.Collectors.*, org.codehaus.groovy.ast.*...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.672)
- **Top Global Matches:** file_cluster_5: 6.672, file_cluster_12: 7.481, file_cluster_7: 7.95
- **Magnitude:** 383.06 | **LOC:** 893 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **21**; blast radius 1.598; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (72.9%), Guard Balance (formerly Safety Score) (67.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitMethodAgain` **(Defensive Guards)** (Impact: 14.2)
  * `transformRhsExpressionIfNecessary` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `visitCleanupBlock` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* */
  * `moveVariableDeclarations` **(Stateful Encapsulated Methods)** (Impact: 8.1)
    * *Intent:* /* * Moves variable declarations from one statement list to another. Initializer * expressions are k...
  * `handleWhereBlock` **(Stateful Encapsulated Methods)** (Impact: 8.0)
    * *Intent:* // where block must be rewritten before all other blocks // s.t. missing method parameters are added...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 222`, `args: 64`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 75`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 14`
* *Architecture:* `io: 17`, `api: 21`, `import: 16`
* *Defense:* `safety: 15`, `doc: 1`, `sync_locks: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.598
  * `Choke Point (Betweenness):` 0.022423 | `Ripple Effect (Closeness):` 0.091379
  * `Imports (Out-Degree: 23):` java.lang.reflect.InvocationTargetException, java.util.*, java.util.Arrays.asList, java.util.Collections.singletonList, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.*, org.codehaus.groovy.syntax.Token...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.489)
- **Top Global Matches:** file_cluster_5: 8.489, file_cluster_7: 10.914, file_cluster_14: 11.657
- **Magnitude:** 269.62 | **LOC:** 448 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **65** in-repo importer(s); it depends on **25**; blast radius 18.662; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (68.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `verifyMethodCondition` **(Many-Argument Workhorses)** (Impact: 30.3)
    * *Intent:* // method calls with spread-dot operator are not rewritten, hence this method doesn't have to care a...
  * `conditionFailedWithException` **(Many-Argument Workhorses)** (Impact: 18.3)
  * `parse` **(Compute Cores)** (Impact: 16.5)
  * `verify` **(Many-Argument Workhorses)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 109`, `args: 32`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 22`
* *Architecture:* `api: 21`, `import: 24`
* *Defense:* `safety: 9`, `doc: 2`, `test: 4`, `sync_locks: 13`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.662
  * `Choke Point (Betweenness):` 0.006058 | `Ripple Effect (Closeness):` 0.049962
  * `Imports (Out-Degree: 18):` groovy.lang.Closure, groovy.lang.DelegatesTo, groovy.transform.stc.ClosureParams, groovy.transform.stc.FromString, java.util.*, java.util.function.Consumer, java.util.function.Function, java.util.stream.Collectors...
  * `Imported By (In-Degree: 65):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.028)
- **Top Global Matches:** file_cluster_12: 8.028, file_cluster_7: 8.118, file_cluster_5: 8.588
- **Magnitude:** 264.68 | **LOC:** 454 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **12**; blast radius 0.676; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%), Concurrency Surface (formerly Concurrency) (62.2%)
- **Documentation Coverage:** 96.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invoke` **(Stateful Encapsulated Methods)** (Impact: 17.5)
  * `runFeature` **(Compute Cores)** (Impact: 7.9)
  * `createSpecInstance` **(Defensive Guards)** (Impact: 6.3)
  * `doRunSetup` **(Stateful Encapsulated Methods)** (Impact: 5.6)
  * `doRunCleanup` **(Stateful Encapsulated Methods)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 105`, `args: 64`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 46`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.676
  * `Choke Point (Betweenness):` 0.00078 | `Ripple Effect (Closeness):` 0.019131
  * `Imports (Out-Degree: 13):` java.lang.System.arraycopy, java.util.Arrays, java.util.Arrays.copyOfRange, java.util.Collections, java.util.List, org.spockframework.runtime.extension.IMethodInterceptor, org.spockframework.runtime.extension.MethodInvocation, org.spockframework.runtime.model.*...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_5: 6.609, file_cluster_12: 9.892, file_cluster_0: 10.738
- **Magnitude:** 248.26 | **LOC:** 422 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **59** in-repo importer(s); it depends on **14**; blast radius 7.095; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.1%), Connectivity (formerly Api Exposure) (81.5%), Guard Balance (formerly Safety Score) (62.6%), Complexity Load (formerly Cognitive Load) (31.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isInitializerOrFixtureMethod` **(Compute Cores)** (Impact: 7.5)
  * `collectAll` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `toFeatureName` **(Annotated & Test Methods)** (Impact: 4.6)
  * `filterFeatures` **(Compute Cores)** (Impact: 4.5)
  * `collectSpecHierarchy` **(Stateful Encapsulated Methods)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 111`, `args: 90`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 32`
* *Architecture:* `api: 70`, `import: 13`
* *Defense:* `doc: 1`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.095
  * `Choke Point (Betweenness):` 0.006733 | `Ripple Effect (Closeness):` 0.155279
  * `Imports (Out-Degree: 10):` java.util.*, java.util.Comparator.comparingInt, java.util.function.BiConsumer, java.util.function.Function, java.util.function.Supplier, org.spockframework.runtime.IFeatureFilter, org.spockframework.runtime.IFeatureSortOrder, org.spockframework.runtime.IMethodNameMapper...
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.566)
- **Top Global Matches:** file_cluster_5: 10.566, file_cluster_14: 11.977, file_cluster_7: 13.673
- **Magnitude:** 242.48 | **LOC:** 354 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **14**; blast radius 1.006; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.9%), Debt Markers (formerly Tech Debt) (64.3%)
- **Documentation Coverage:** 99.0826% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createMockImpl` **(Stateful Encapsulated Methods)** (Impact: 13.1)
  * `checkExceptionThrown` **(Generic / Templated Code)** (Impact: 7.8)
  * `GroovySpyImpl` **(Generic / Templated Code)** (Impact: 7.8)
  * `createStaticMockImpl` **(Stateful Encapsulated Methods)** (Impact: 7.2)
  * `createMock` **(Stateful Encapsulated Methods)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 104`, `args: 65`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 1`, `planned_debt: 16`
* *Architecture:* `api: 59`, `import: 10`
* *Defense:* `doc: 1`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.006
  * `Choke Point (Betweenness):` 0.000401 | `Ripple Effect (Closeness):` 0.004708
  * `Imports (Out-Degree: 8):` groovy.lang.Closure, groovy.transform.stc.ClosureParams, groovy.transform.stc.SecondParam, groovy.transform.stc.ThirdParam, java.lang.reflect.Type, java.util.*, java.util.Collections.emptyMap, java.util.Collections.singletonMap...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/util/ReflectionUtil.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.647)
- **Top Global Matches:** file_cluster_5: 7.647, file_cluster_7: 11.016, file_cluster_12: 11.675
- **Magnitude:** 231.44 | **LOC:** 417 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **9**; blast radius 15.893; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.1%), Guard Balance (formerly Safety Score) (80.0%), Mutation Surface (formerly State Flux) (72.0%), Concurrency Surface (formerly Concurrency) (42.9%)
- **Documentation Coverage:** 75.9494% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDefaultValue` **(Defensive Guards)** (Impact: 26.3)
  * `isClassVisibleInClassloader` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* /** * Checks if the {@code classToCheck} is visible by the passed {@code classLoader} * * @param cla...
  * `hasValidArguments` **(Generic / Templated Code)** (Impact: 7.5)
  * `collectAnnotationRecursive` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `getClassFile` **(Generic / Templated Code)** (Impact: 6.2)
    * *Intent:* /** * Returns the class file for the given class (which has been verified to exist in the returned l...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 120`, `args: 46`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 10`
* *Architecture:* `io: 7`, `api: 37`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 30`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.893
  * `Choke Point (Betweenness):` 0.000673 | `Ripple Effect (Closeness):` 0.190379
  * `Imports (Out-Degree: 3):` java.io.File, java.io.IOException, java.lang.annotation.Annotation, java.lang.reflect.*, java.net.URL, java.security.CodeSource, java.util.*, java.util.Arrays.asList...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/ExpressionReplacingVisitorSupport.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.366)
- **Top Global Matches:** file_cluster_12: 7.366, file_cluster_7: 7.728, file_cluster_5: 7.879
- **Magnitude:** 229.88 | **LOC:** 419 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.342; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.5%)
- **Documentation Coverage:** 98.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `replaceExpr` **(Compute Cores)** (Impact: 3.2)
  * `visitArrayExpression` **(Annotated & Test Methods)** (Impact: 3.2)
  * `replaceAllExprs` **(Encapsulated Accessors)** (Impact: 3.1)
  * `visitPropertyExpression` **(Annotated & Test Methods)** (Impact: 2.1)
  * `visitRangeExpression` **(Annotated & Test Methods)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 81`, `args: 55`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 64`, `unreferenced_by_name: 48`
* *Architecture:* `api: 56`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` java.util.List, java.util.ListIterator, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.*, org.codehaus.groovy.classgen.BytecodeExpression
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.769)
- **Top Global Matches:** file_cluster_5: 8.769, file_cluster_7: 9.347, file_cluster_14: 9.349
- **Magnitude:** 224.3 | **LOC:** 402 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **14**; blast radius 4.836; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (78.2%), Complexity Load (formerly Cognitive Load) (18.9%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toArgumentArray` **(Generic / Templated Code)** (Impact: 10.1)
    * *Intent:* /** * Turns an argument list obtained from AstUtil.getArguments() into an Object[] array * suitable ...
  * `getInvocationTarget` **(Type Conversions)** (Impact: 7.6)
  * `getAnnotation` **(Type Conversions)** (Impact: 7.4)
  * `isDynamicTypedExpression` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `isJavaIdentifier` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 122`, `args: 42`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 21`
* *Architecture:* `io: 5`, `api: 40`, `import: 9`
* *Defense:* `safety: 27`, `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.836
  * `Choke Point (Betweenness):` 0.024147 | `Ripple Effect (Closeness):` 0.109941
  * `Imports (Out-Degree: 4):` java.util.*, java.util.Collections.emptyList, java.util.Collections.singletonList, java.util.regex.Pattern, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.*, org.codehaus.groovy.runtime.dgmimpl.arrays.IntegerArrayGetAtMetaMethod...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/ExpressionInfoConverter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.025)
- **Top Global Matches:** file_cluster_12: 7.025, file_cluster_5: 7.153, file_cluster_7: 7.758
- **Magnitude:** 194.6 | **LOC:** 422 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.591; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startOf` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* // searches for token backwards from beginning of node (exclusive) // IDEA: move to class TextPositi...
  * `visitMethodCallExpression` **(Generic / Templated Code)** (Impact: 3.6)
  * `visitArrayExpression` **(Generic / Templated Code)** (Impact: 3.5)
  * `visitBinaryExpression` **(Annotated & Test Methods)** (Impact: 3.4)
  * `visitPropertyExpression` **(Annotated & Test Methods)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 89`, `args: 44`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 52`, `unreferenced_by_name: 34`
* *Architecture:* `api: 39`, `import: 14`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.591
  * `Choke Point (Betweenness):` 0.001018 | `Ripple Effect (Closeness):` 0.036054
  * `Imports (Out-Degree: 7):` java.util.ArrayList, java.util.Arrays, java.util.Arrays.asList, java.util.Collections.emptyList, java.util.Collections.singletonList, java.util.List, org.codehaus.groovy.ast.ASTNode, org.codehaus.groovy.ast.expr.*...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/DeepBlockRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.44)
- **Top Global Matches:** file_cluster_12: 6.44, file_cluster_16: 7.709, file_cluster_5: 8.411
- **Magnitude:** 186.1 | **LOC:** 370 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 0.509; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%), Complexity Load (formerly Cognitive Load) (36.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleImplicitCondition` **(Stateful Encapsulated Methods)** (Impact: 13.2)
  * `doVisitBinaryExpression` **(Stateful Encapsulated Methods)** (Impact: 11.3)
  * `handleThrownCall` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `handleInteraction` **(Stateful Encapsulated Methods)** (Impact: 8.0)
  * `handleOldCall` **(Stateful Encapsulated Methods)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 70`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 22`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 10`, `import: 10`
* *Defense:* `safety: 13`, `doc: 1`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.509
  * `Choke Point (Betweenness):` 0.003249 | `Ripple Effect (Closeness):` 0.078327
  * `Imports (Out-Degree: 10):` java.util.List, org.codehaus.groovy.ast.Parameter, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.expr.MethodCallExpression.NO_ARGUMENTS, org.codehaus.groovy.ast.stmt.AssertStatement, org.codehaus.groovy.ast.stmt.ExpressionStatement, org.codehaus.groovy.ast.stmt.Statement, org.codehaus.groovy.syntax.Types...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/SpecParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.018)
- **Top Global Matches:** file_cluster_5: 7.018, file_cluster_12: 7.267, file_cluster_7: 8.237
- **Magnitude:** 178.72 | **LOC:** 300 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.384; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.0%), Complexity Load (formerly Cognitive Load) (70.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildBlocks` **(Stateful Encapsulated Methods)** (Impact: 13.6)
  * `visitMethod` **(Compute Cores)** (Impact: 11.9)
  * `buildFixtureMethod` **(Stateful Encapsulated Methods)** (Impact: 9.7)
  * `addBlock` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `isFixtureMethod` **(Stateful Encapsulated Methods)** (Impact: 8.0)
    * *Intent:* // IDEA: check for misspellings other than wrong capitalization
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 67`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 31`, `unreferenced_by_name: 6`
* *Architecture:* `io: 8`, `api: 8`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.384
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.000769
  * `Imports (Out-Degree: 11):` java.util.List, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.ConstantExpression, org.codehaus.groovy.ast.stmt.Statement, org.spockframework.compiler.AstUtil.hasAnnotation, org.spockframework.compiler.model.*, org.spockframework.util.Identifiers.*, spock.lang.Shared...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.248)
- **Top Global Matches:** file_cluster_5: 5.248, file_cluster_12: 7.693, file_cluster_7: 9.392
- **Magnitude:** 176.28 | **LOC:** 411 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **26**; blast radius 0.849; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%), Complexity Load (formerly Cognitive Load) (14.9%)
- **Documentation Coverage:** 78.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBeanName` **(Stateful Encapsulated Methods)** (Impact: 12.3)
  * `determinePrimaryCandidate` **(Stateful Encapsulated Methods)** (Impact: 8.8)
  * `register` **(Stateful Encapsulated Methods)** (Impact: 8.4)
  * `registerSpy` **(Stateful Encapsulated Methods)** (Impact: 6.6)
  * `determineBeanName` **(Stateful Encapsulated Methods)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 101`, `args: 32`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 18`, `planned_debt: 1`
* *Architecture:* `api: 8`, `import: 24`
* *Defense:* `safety: 8`, `doc: 6`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.849
  * `Choke Point (Betweenness):` 0.000149 | `Ripple Effect (Closeness):` 0.002306
  * `Imports (Out-Degree: 7):` java.util.*, java.util.Arrays.asList, java.util.concurrent.ConcurrentHashMap, org.spockframework.runtime.model.FieldInfo, org.spockframework.spring.SpringBean, org.spockframework.spring.SpringExtensionException, org.spockframework.spring.SpringSpy, org.springframework.aop.scope.ScopedProxyUtils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/util/TeePrintStream.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.168)
- **Top Global Matches:** file_cluster_13: 5.168, file_cluster_11: 6.65, file_cluster_15: 6.932
- **Magnitude:** 173.56 | **LOC:** 353 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.537; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (78.9%), Guard Balance (formerly Safety Score) (50.0%), Mutation Surface (formerly State Flux) (13.9%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printf` **(Parameter Forwarders)** (Impact: 4.4)
  * `format` **(Parameter Forwarders)** (Impact: 4.4)
  * `append` **(Parameter Forwarders)** (Impact: 4.4)
  * `write` **(Parameter Forwarders)** (Impact: 4.3)
  * `printf` **(Annotated & Test Methods)** (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 52`, `args: 44`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 11`
* *Architecture:* `api: 44`, `import: 4`
* *Defense:* `safety: 2`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.537
  * `Choke Point (Betweenness):` 0.000102 | `Ripple Effect (Closeness):` 0.002129
  * `Imports (Out-Degree: 2):` groovy.lang.MissingMethodException, java.io.*, java.util.*, java.util.Arrays.asList, java.util.concurrent.CopyOnWriteArrayList, org.spockframework.runtime.GroovyRuntimeUtil
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/model/FeatureInfo.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.625)
- **Top Global Matches:** file_cluster_5: 7.625, file_cluster_0: 9.413, file_cluster_12: 9.489
- **Magnitude:** 172.2 | **LOC:** 445 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **10**; blast radius 7.517; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.1%), Mutation Surface (formerly State Flux) (65.0%), Guard Balance (formerly Safety Score) (57.1%)
- **Documentation Coverage:** 70.3704% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hasBytecodeName` **(Compute Cores)** (Impact: 10.3)
    * *Intent:* /** * Tells if any of the methods associated with this feature has the specified * name in bytecode....
  * `addImpliedFeature` **(Generic / Templated Code)** (Impact: 5.0)
    * *Intent:* /** * Adds the given feature as implied by this feature. * The given feature must be within the same...
  * `addScopedMethodInterceptor` **(Callbacks & Closures)** (Impact: 2.1)
    * *Intent:* * featureInfo.addScopedMethodInterceptor(featureInfo.getParent().getInitializerMethod(), invocation ...
  * `setDeclarationOrder` **(Parameter Forwarders)** (Impact: 1.6)
  * `setExecutionOrder` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 91`, `args: 56`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 26`
* *Architecture:* `api: 55`, `import: 9`
* *Defense:* `doc: 16`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.01011 | `Ripple Effect (Closeness):` 0.157052
  * `Imports (Out-Degree: 12):` java.lang.reflect.AnnotatedElement, java.util.*, org.spockframework.runtime.extension.IBlockListener, org.spockframework.runtime.extension.IDataDriver, org.spockframework.runtime.extension.IMethodInterceptor, org.spockframework.runtime.model.parallel.ExclusiveResource, org.spockframework.runtime.model.parallel.ExecutionMode, org.spockframework.util.Beta...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/InteractionRewriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.825)
- **Top Global Matches:** file_cluster_7: 7.825, file_cluster_5: 7.861, file_cluster_12: 8.34
- **Magnitude:** 162.18 | **LOC:** 396 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.382; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.4%), Guard Balance (formerly Safety Score) (73.3%), Complexity Load (formerly Cognitive Load) (21.5%), Debt Markers (formerly Tech Debt) (15.2%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseCall` **(Defensive Guards)** (Impact: 13.3)
  * `setCall` **(Stateful Encapsulated Methods)** (Impact: 12.1)
  * `addArg` **(Stateful Encapsulated Methods)** (Impact: 9.9)
  * `addArgs` **(Stateful Encapsulated Methods)** (Impact: 9.8)
  * `selectNameConstraint` **(Stateful Encapsulated Methods)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 79`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 18`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 25`, `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.382
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.068336
  * `Imports (Out-Degree: 6):` java.util.*, java.util.Arrays.asList, org.codehaus.groovy.ast.*, org.codehaus.groovy.ast.expr.*, org.codehaus.groovy.ast.stmt.ExpressionStatement, org.codehaus.groovy.syntax.Types, org.spockframework.compiler.AstUtil.createDirectMethodCall, org.spockframework.compiler.AstUtil.primitiveConstExpression...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/mock/runtime/InteractionBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.403)
- **Top Global Matches:** file_cluster_15: 7.403, file_cluster_12: 7.841, file_cluster_11: 8.307
- **Magnitude:** 160.24 | **LOC:** 201 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (59.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setRangeCount` **(Defensive Guards)** (Impact: 8.3)
  * `convertCount` **(Stateful Encapsulated Methods)** (Impact: 7.4)
  * `setArgListKind` **(Compute Cores)** (Impact: 5.7)
  * `setFixedCount` **(Defensive Guards)** (Impact: 4.7)
  * `addEqualPropertyName` **(Compute Cores)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 54`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`
* *Architecture:* `api: 39`, `import: 2`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.378
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.001025
  * `Imports (Out-Degree: 3):` groovy.lang.Closure, java.util.*, org.spockframework.lang.*, org.spockframework.mock.*, org.spockframework.mock.constraint.*, org.spockframework.mock.response.*, org.spockframework.runtime.InvalidSpecException
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/ParameterizedFeatureNodeStatuses.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.263)
- **Top Global Matches:** file_cluster_2: 6.263, file_cluster_13: 6.933, file_cluster_15: 6.937
- **Magnitude:** 159.5 | **LOC:** 892 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.342; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.2%), Complexity Load (formerly Cognitive Load) (6.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `'should be failing if some uprolled iterations are erroring and some failing'` **(I/O & Config Routines)** (Impact: 4.0)
  * `'should be failing if all uprolled iterations are erroring'` **(I/O & Config Routines)** (Impact: 4.0)
  * `'exceptions in iteration interceptors should not affect other iterations'` **(I/O & Config Routines)** (Impact: 4.0)
  * `'should be error if some uprolled iterations are erroring and some skipped'` **(I/O & Config Routines)** (Impact: 3.9)
  * `'should be failing if all uprolled iterations are failing'` **(I/O & Config Routines)** (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 54`, `args: 50`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 9`, `unreferenced_by_name: 24`
* *Architecture:* `import: 4`
* *Defense:* `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.opentest4j.*, org.spockframework.EmbeddedSpecification, org.spockframework.runtime.SpockComparisonFailure, spock.lang.Issue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/util/inspector/AstInspector.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.367)
- **Top Global Matches:** file_cluster_5: 6.367, file_cluster_12: 9.48, file_cluster_7: 9.698
- **Magnitude:** 158.2 | **LOC:** 531 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **17**; blast radius 1.239; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Guard Balance (formerly Safety Score) (65.8%), Mutation Surface (formerly State Flux) (51.4%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 43.5897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitAnnotations` **(Type Conversions)** (Impact: 6.6)
  * `visitConstructorOrMethod` **(Stateful Encapsulated Methods)** (Impact: 5.7)
  * `visitStatement` **(Type Conversions)** (Impact: 4.7)
  * `doVisitMethodCall` **(Stateful Encapsulated Methods)** (Impact: 4.7)
  * `getExpressions` **(Stateful Encapsulated Methods)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 101`, `args: 44`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 16`, `unreferenced_by_name: 20`
* *Architecture:* `io: 12`, `api: 36`, `import: 14`
* *Defense:* `safety: 8`, `doc: 23`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.239
  * `Choke Point (Betweenness):` 0.000312 | `Ripple Effect (Closeness):` 0.00538
  * `Imports (Out-Degree: 2):` groovy.lang.GroovyClassLoader, java.io.File, java.io.IOException, java.security.CodeSource, java.util.ArrayList, java.util.Collections.emptyList, java.util.HashMap, java.util.List...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `spock-core/src/main/java/org/spockframework/runtime/condition/DiffedCollectionRenderer.java` (JAVA) | Magnitude: 5.54 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, api: 2, branch: 1
- `spock-core/src/main/java/spock/lang/Subject.java` (JAVA) | Magnitude: 2.36 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, decorators: 6, indent_spaces: 6, doc: 3
- `spock-core/src/main/java/org/spockframework/builder/PojoBuilder.java` (JAVA) | Magnitude: 7.26 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 11, import: 4, api: 3
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryConditionContext.java` (JAVA) | Magnitude: 9.42 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, args: 3, func_start: 3
- `spock-core/src/main/java/org/spockframework/compiler/condition/VerifyMethodRewriter.java` (JAVA) | Magnitude: 9.88 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, import: 7, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `spock-specs/src/test/groovy/org/spockframework/smoke/RecorderScope.groovy` (GROOVY) | Magnitude: 18.8 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 17, args: 12, test: 11
- `spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/VerifyAllMethodsAstSpec/methods_without_condition_declarations_stay_unchanged.groovy` (GROOVY) | Magnitude: 3.72 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, api: 2, args: 1
- `spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/VerifyMethodsAstSpec/methods_without_condition_declarations_stay_unchanged.groovy` (GROOVY) | Magnitude: 3.72 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, api: 2, args: 1
- `spock-specs/src/test/groovy/org/spockframework/smoke/mock/MockCreationWithClosure.groovy` (GROOVY) | Magnitude: 17.22 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 19, args: 11, func_start: 9
- `spock-specs/src/test/groovy/org/spockframework/smoke/extension/TimeoutExtension.groovy` (GROOVY) | Magnitude: 64.84 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 199, test: 40, structural_boundaries: 34, func_start: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `spock-specs/src/test/groovy/org/spockframework/smoke/extension/PendingFeatureExtensionSpec.groovy` (GROOVY) | Magnitude: 136.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 423, test: 80, structural_boundaries: 65, args: 53
- `spock-specs/src/test/groovy/org/spockframework/mock/AutoAttachSpec.groovy` (GROOVY) | Magnitude: 3.7 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, import: 3, state_mutation: 2
- `spock-guice/src/test/groovy/org/spockframework/guice/InjectionExamples.groovy` (GROOVY) | Magnitude: 16.14 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 21, decorators: 16, safety: 15
- `spock-specs/src/test/groovy/org/spockframework/smoke/ast/AstSpec.groovy` (GROOVY) | Magnitude: 41.76 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 34, test: 32, core_var_decl: 14
- `spock-specs/src/test/groovy/org/spockframework/smoke/SharedFieldsInSuperclass.groovy` (GROOVY) | Magnitude: 5.94 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 10, decorators: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `spock-core/src/main/java/org/spockframework/util/GenericTypeReflectorUtil.java` (JAVA) | Magnitude: 37.68 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 22, import: 9, branch: 7
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryIterationInterceptor.java` (JAVA) | Magnitude: 70.1 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 36, import: 11, core_var_decl: 11
- `spock-core/src/main/java/org/spockframework/runtime/StandardStreamsCapturer.java` (JAVA) | Magnitude: 78.68 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 21, branch: 13, args: 9
- `spock-spring/src/main/java/org/spockframework/spring/AbstractSpringTestExecutionListener.java` (JAVA) | Magnitude: 27.1 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 25, api: 11, args: 10
- `spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java` (JAVA) | Magnitude: 264.68 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 344, structural_boundaries: 105, args: 64, state_mutation: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `spock-core/src/main/java/org/spockframework/runtime/condition/DiffedArrayRenderer.java` (JAVA) | Magnitude: 8.54 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, api: 2, core_var_decl: 2
- `spock-testkit/src/test/groovy/spock/testkit/testsources/ExampleTestCase.groovy` (GROOVY) | Magnitude: 3.68 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 7, args: 3, func_start: 3
- `spock-spring/src/main/java/org/spockframework/spring/xml/WrapWithSpyBeanDefinitionParser.java` (JAVA) | Magnitude: 9.06 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 10, api: 4, args: 3
- `spock-testkit/src/test/groovy/spock/testkit/testsources/InheritedParentTestCase.groovy` (GROOVY) | Magnitude: 3.7 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, args: 3, func_start: 3
- `spock-spring/src/test/java/org/spockframework/spring/mock/imported/example/ExampleExtraInterface.java` (JAVA) | Magnitude: 2.18 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `spock-core/src/main/java/org/spockframework/mock/constraint/RegexPropertyNameConstraint.java` (JAVA) | Magnitude: 10.56 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, safety_bypasses: 5, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `build-logic/settings.gradle` (GROOVY) | Magnitude: 11.66 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 3, branch: 2, args: 2
- `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/InvalidWhereBlocks.groovy` (GROOVY) | Magnitude: 118.02 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 340, test: 111, structural_boundaries: 79, args: 52
- `spock-specs/src/test/groovy/org/spockframework/mock/runtime/JavaMockFactorySpec.groovy` (GROOVY) | Magnitude: 19.2 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 19, branch: 8, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `spock-junit4/src/test/groovy/org/spockframework/junit4/junit/JUnitFixtureMethods.groovy` (GROOVY) | Magnitude: 40.28 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 99, test: 32, structural_boundaries: 25, args: 18
- `spock-core/src/main/java/spock/mock/MockMakers.java` (JAVA) | Magnitude: 7.64 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, import: 13, indent_spaces: 11, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `spock-core/src/main/java/org/spockframework/compiler/model/FixtureMethod.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `spock-core/src/main/java/org/spockframework/compiler/model/HelperMethod.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `spock-specs/src/test/groovy/org/spockframework/groovy/GroovyVarArgs.groovy` (GROOVY) | Magnitude: 3.7 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, indent_spaces: 2
- `spock-core/src/main/java/org/spockframework/util/IncompatibleGroovyVersionException.java` (JAVA) | Magnitude: 3.74 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `spock-spring/src/main/java/org/spockframework/spring/mock/Definition.java` (JAVA) | Magnitude: 2.3 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `spock-core/src/main/java/org/spockframework/runtime/model/SpecElementInfo.java` (JAVA) | Magnitude: 45.14 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 26, api: 15, args: 14
- `spock-specs/src/test/groovy/org/spockframework/runtime/extension/AnnotationDrivenExtensionSpec.groovy` (GROOVY) | Magnitude: 34.64 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 28, decorators: 17, args: 13
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/IncludeExcludeExtension.java` (JAVA) | Magnitude: 73.88 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 26, branch: 19, args: 10
- `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` (JAVA) | Magnitude: 441.0 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 642, structural_boundaries: 228, core_var_decl: 121, state_mutation: 114
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/UnrollExtension.java` (JAVA) | Magnitude: 87.08 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 27, core_var_decl: 20, design_camel_case: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `spock-core/src/main/java/org/spockframework/compiler/InteractionRewriter.java` (JAVA) | Magnitude: 162.18 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 276, structural_boundaries: 79, branch: 53, encapsulation: 37
- `spock-core/src/main/java/spock/util/time/MutableClock.java` (JAVA) | Magnitude: 56.76 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 20, api: 19, args: 18
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionRendering.groovy` (GROOVY) | Magnitude: 140.44 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 535, structural_boundaries: 160, core_var_decl: 87, design_snake_case: 83
- `spock-core/src/main/java/org/spockframework/runtime/FailedEqualityComparisonRenderer.java` (JAVA) | Magnitude: 42.72 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 14, branch: 10, safety_bypasses: 7
- `spock-junit4/src/main/java/org/spockframework/junit4/JUnitDescriptionGenerator.java` (JAVA) | Magnitude: 18.92 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 12, branch: 4, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `spock-specs/src/test-groovy-ge-4.0/groovy/org/spockframework/smoke/condition/ConditionG4Spec.groovy` (GROOVY) | Magnitude: 8.34 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, branch: 5, args: 4
- `spock-core/src/main/java/org/spockframework/runtime/extension/ExtensionUtil.java` (JAVA) | Magnitude: 19.32 | Delta: **0.182** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, branch: 5, api: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `build.gradle` -> Churn: **51.21%** | Cog Load: 81.6922% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 401.98
- `spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 383.06
- `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java` -> **Christoph Loy** (100.0% isolated ownership) | Magnitude: 269.62
- `spock-core/src/main/java/org/spockframework/compiler/DeepBlockRewriter.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 186.1
- `spock-core/src/main/java/org/spockframework/compiler/SpecParser.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 178.72

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` -> **Severity: 2.313** (Bridge: 0.0241 * Flux: 95.8004%)
- `spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java` -> **Severity: 2.238** (Bridge: 0.0224 * Flux: 99.7982%)
- `spock-core/src/main/java/org/spockframework/mock/ClosureParameterTypeFromVariableType.java` -> **Severity: 2.161** (Bridge: 0.0219 * Flux: 98.474%)
- `spock-core/src/main/java/spock/lang/Specification.java` -> **Severity: 1.939** (Bridge: 0.0438 * Flux: 44.2886%)
- `spock-core/src/main/java/org/spockframework/runtime/SpockExecutionContext.java` -> **Severity: 0.731** (Bridge: 0.0074 * Flux: 98.8634%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `spock-core/src/main/java/spock/lang/Specification.java` -> **Severity: 19.657** (Embedded: 0.2457 * Error Risk: 80.0%)
- `spock-core/src/main/java/org/spockframework/util/ExceptionUtil.java` -> **Severity: 16.912** (Embedded: 0.2114 * Error Risk: 80.0%)
- `spock-core/src/main/java/org/spockframework/util/ReflectionUtil.java` -> **Severity: 15.23** (Embedded: 0.1904 * Error Risk: 80.0%)
- `spock-core/src/main/java/org/spockframework/runtime/GroovyRuntimeUtil.java` -> **Severity: 15.216** (Embedded: 0.2065 * Error Risk: 73.6893%)
- `spock-core/src/main/java/org/spockframework/util/ObjectUtil.java` -> **Severity: 14.254** (Embedded: 0.1782 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java` -> **Severity: 1866.2** (Blast Radius: 18.662 * Doc Risk: 100.0%)
- `spock-core/src/main/java/org/spockframework/util/ExceptionUtil.java` -> **Severity: 1540.24** (Blast Radius: 19.253 * Doc Risk: 80.0%)
- `spock-core/src/main/java/org/spockframework/runtime/GroovyRuntimeUtil.java` -> **Severity: 1282.164** (Blast Radius: 20.327 * Doc Risk: 63.0769%)
- `spock-specs/src/test/groovy/org/spockframework/EmbeddedSpecification.groovy` -> **Severity: 1232.7** (Blast Radius: 12.327 * Doc Risk: 100.0%)
- `spock-core/src/main/java/org/spockframework/util/ReflectionUtil.java` -> **Severity: 1207.064** (Blast Radius: 15.893 * Doc Risk: 75.9494%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 264 literal sites + 2 sites through wrappers = 266
- **`panics_and_aborts`:** 585 literal sites + 63 sites through wrappers = 648

- `unsupported` (function, panics_and_aborts, primitive): 23 call sites in 3 files -- `spock-core/src/main/java/org/spockframework/util/AbstractExpressionConverter.java`
- `clone` (function, panics_and_aborts, primitive): 10 call sites in 1 files -- `spock-core/src/main/java/org/spockframework/runtime/SpockExecutionContext.java`
- `execute` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `spock-core/src/main/java/org/spockframework/runtime/NamespacedExtensionStore.java`
- `sneakyThrow` (function, panics_and_aborts, primitive): 6 call sites in 3 files -- `spock-core/src/main/java/org/spockframework/util/ExceptionUtil.java`
- `threadLocalMockData` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `spock-core/src/main/java/org/spockframework/mock/runtime/mockito/MockitoMockMakerImpl.java`
- `createCondition` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/ConditionalExtension.java`
- `iterationConditionResult` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/ConditionalExtension.java`
- `syncWithThread` (function, debug_prints, primitive): 2 call sites in 1 files -- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TimeoutInterceptor.java`
- `c` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spock-specs/src/test/groovy/org/spockframework/smoke/GroovyCallChain.groovy`
- `c` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spock-specs/src/test/java/org/spockframework/smoke/JavaCallChain.java`
- `currentProcessId` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spock-core/src/main/java/org/spockframework/util/JavaProcessThreadDumpCollector.java`
- `featureConditionResult` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/ConditionalExtension.java`
*(+6 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 16737 call pairs -- scoped 29.7%, unique 1.6%, ambiguous 31.8%, external 37.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 9783 | 34.2% | 2.3% | 30.5% | 33.0% |
| groovy | 6897 | 23.5% | 0.5% | 33.7% | 42.4% |
| kotlin | 48 | 12.5% | 0.0% | 16.7% | 70.8% |
| shell | 9 | 33.3% | 0.0% | 0.0% | 66.7% |

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
